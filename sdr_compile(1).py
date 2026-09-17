#!/usr/bin/env python3
"""
Compile authored records + collected evidence into a Security Decision Record.

  authored YAML (git, PR-reviewed)  --.
  collector evidence (JSONL, append) --+--> sdr.json  (schema-validated)
  assessor input (JSONL, separate)  --'    + coverage.json (gaps & staleness)

The SDR is a BUILD ARTIFACT. Never hand-edit it; edit the inputs and rebuild.
That is also what satisfies CDS-CSO-CBF, which requires automation to keep
human-readable and machine-readable forms consistent.

Evidence record contract (one JSON object per line):
  {"rule_id"|"ksi_id": "...", "evidenceType": "Configuration",
   "evidenceDescription": "...", "evidenceLocation": "https://...",
   "evidenceText": "...", "lastUpdated": "2026-09-17",
   "collector": "...", "sha256": "..."}
'collector' and 'sha256' are dropped before emit (not in the FedRAMP schema)
but are retained in the coverage report for provenance.
"""
import argparse, json, os, sys, glob, datetime as dt

try:
    import yaml, jsonschema
    from referencing import Registry, Resource
except ImportError:
    sys.exit("pip install pyyaml jsonschema")

SCHEMA_FIELDS = {"evidenceType", "evidenceDescription", "evidenceLocation",
                 "evidenceText", "lastUpdated"}
DAYS = {"days": 1, "bizdays": 1.4, "weeks": 7, "months": 30.4, "years": 365}


def load_records(d, key):
    out = {}
    for p in sorted(glob.glob(f"{d}/*.yaml")):
        r = yaml.safe_load(open(p))
        if r and r.get(key):
            r["_path"] = p
            out[r[key]] = r
    return out


def load_evidence(paths):
    ev = {}
    for p in paths:
        if not os.path.exists(p):
            continue
        for n, line in enumerate(open(p), 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                e = json.loads(line)
            except json.JSONDecodeError as err:
                print(f"  WARN {p}:{n} bad JSON, skipped ({err})", file=sys.stderr)
                continue
            k = e.get("rule_id") or e.get("ksi_id")
            if not k:
                print(f"  WARN {p}:{n} no rule_id/ksi_id, skipped", file=sys.stderr)
                continue
            ev.setdefault(k, []).append(e)
    return ev


def clean(e):
    return {k: v for k, v in e.items() if k in SCHEMA_FIELDS and v is not None}


def stale_after(cadence):
    if not cadence:
        return None
    try:
        num, unit = cadence.split()
        if "-" in num:
            num = num.split("-")[1]
        return float(num) * DAYS.get(unit, 1)
    except Exception:
        return None


def age_days(iso, today):
    try:
        return (today - dt.date.fromisoformat(iso[:10])).days
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--records", default="records")
    ap.add_argument("--evidence", nargs="*", default=["evidence/collected.jsonl"])
    ap.add_argument("--assessments", nargs="*", default=["evidence/assessments.jsonl"])
    ap.add_argument("--schema", required=True)
    ap.add_argument("--package-uri", required=True)
    ap.add_argument("--version", default="0.1.0")
    ap.add_argument("--update-source", default="sdr_compile.py")
    ap.add_argument("--out", default="sdr.json")
    ap.add_argument("--coverage", default="coverage.json")
    ap.add_argument("--render", default="sdr.md",
                    help="human-readable output path (set to '' to skip)")
    ap.add_argument("--today", default=None)
    ap.add_argument("--strict", action="store_true",
                    help="exit nonzero if any blocking gap is found")
    a = ap.parse_args()

    today = dt.date.fromisoformat(a.today) if a.today else dt.date.today()
    m = json.load(open(a.manifest))
    rules_meta = {r["rule_id"]: r for r in m["rules"]}
    ksis_meta = {k["ksi_id"]: k for k in m["key_security_indicators"]}
    min_methods = m["ksi_min_automated_methods_each"]

    frr_rec = load_records(f"{a.records}/frr", "rule_id")
    ksi_rec = load_records(f"{a.records}/ksi", "ksi_id")
    ev = load_evidence(a.evidence)
    assess = load_evidence(a.assessments)

    findings = []

    def flag(sev, target, msg):
        findings.append({"severity": sev, "target": target, "message": msg})

    # ---------- FRR ----------
    frr_out = []
    for rid, meta in rules_meta.items():
        rec = frr_rec.get(rid)
        if not rec:
            flag("BLOCKING", rid, "applicable rule has no authored record")
            continue
        entry = {"frrID": rid}
        if rec.get("status"):
            entry["frrImplementationStatus"] = rec["status"]
        impl = [s for s in (rec.get("implementation") or []) if s]
        if not impl and rec.get("not_implemented_rationale"):
            impl = [rec["not_implemented_rationale"]]
            if not rec.get("accepted_by"):
                flag("BLOCKING", rid,
                     "not implemented but no senior official recorded in accepted_by")
            if not rec.get("risk_to_customers"):
                flag("BLOCKING", rid,
                     "not implemented but risk_to_customers is empty")
        if not impl:
            flag("BLOCKING", rid, "frrImplementation is empty (schema-required)")
            continue
        entry["frrImplementation"] = impl
        if rec.get("validation"):
            entry["frrValidation"] = [s for s in rec["validation"] if s]
        else:
            flag("MAJOR", rid, "no internal validation statement")
        if assess.get(rid):
            entry["frrAssessment"] = [x.get("evidenceDescription", "")
                                      for x in assess[rid]]
        else:
            flag("MINOR", rid, "no independent assessment recorded")

        # artifact + freshness checks
        got = ev.get(rid, [])
        need = meta["artifacts"]
        if need and not got:
            flag("MAJOR", rid,
                 f"{len(need)} rule-specific artifact(s) named, none collected")
        limit = stale_after(meta["cadence"])
        for e in got:
            ag = age_days(e.get("lastUpdated", ""), today)
            if ag is None:
                flag("MAJOR", rid, "evidence has missing/unparseable lastUpdated")
            elif limit and ag > limit:
                flag("BLOCKING", rid,
                     f"evidence is {ag}d old; {meta['cadence']} cadence allows ~{int(limit)}d")
        frr_out.append(entry)

    # ---------- KSI ----------
    ksi_out = []
    for kid, meta in ksis_meta.items():
        if meta.get("class_unspecified"):
            flag("REVIEW", kid, "class not defined in source ruleset")
        rec = ksi_rec.get(kid)
        if not rec:
            flag("BLOCKING", kid, "in-scope KSI has no authored record")
            continue
        got = [clean(e) for e in ev.get(kid, [])]
        tests = rec.get("tests") or []
        entry = {
            "ksiId": kid,
            "ksiImplementation": [s for s in (rec.get("implementation") or []) if s],
            "ksiValidation": [s for s in (rec.get("validation") or []) if s],
            "ksiAssessment": [x.get("evidenceDescription", "")
                              for x in assess.get(kid, [])],
            "ksiTests": tests,
            "ksiEvidence": got,
        }
        if rec.get("status"):
            entry["ksiImplementationStatus"] = rec["status"]
        # all five are schema-required for KSIs
        for f in ("ksiImplementation", "ksiValidation", "ksiAssessment",
                  "ksiTests", "ksiEvidence"):
            if not entry[f]:
                flag("BLOCKING", kid, f"{f} is empty (schema-required for KSIs)")
        if not meta.get("optional_at_this_class") and len(tests) < min_methods:
            flag("BLOCKING", kid,
                 f"{len(tests)} automated method(s); class {m['class']} requires "
                 f"{min_methods} per FRC-CSX-VVK")
        ksi_out.append(entry)

    # ---------- emit ----------
    sdr = {
        "certificationPackageOverviewUri": a.package_uri,
        "metadata": {
            "version": a.version,
            "lastUpdated": dt.datetime.now(dt.timezone.utc)
                             .strftime("%Y-%m-%dT%H:%M:%SZ"),
            "updateSource": a.update_source,
        },
        "fedRampRequirements": frr_out,
        "keySecurityIndicators": ksi_out,
    }

    # The SDR schema $refs fedramp-common-definitions by absolute https URL.
    # Vendor the whole schema directory and resolve locally -- never let a
    # validator reach the network, or your build depends on fedramp.gov uptime
    # AND silently tracks upstream drift instead of your pinned copy.
    schema = json.load(open(a.schema))
    registry = Registry()
    for p in glob.glob(os.path.join(os.path.dirname(a.schema) or ".", "*.json")):
        try:
            doc = json.load(open(p))
        except json.JSONDecodeError:
            continue
        if "$id" in doc:
            registry = registry.with_resource(
                doc["$id"], Resource.from_contents(doc))
    validator = jsonschema.Draft202012Validator(schema, registry=registry)
    errs = sorted(validator.iter_errors(sdr), key=lambda e: list(e.path))
    for e in errs:
        flag("SCHEMA", "/".join(str(x) for x in e.path) or "(root)", e.message)

    json.dump(sdr, open(a.out, "w"), indent=2)
    counts = {}
    for f in findings:
        counts[f["severity"]] = counts.get(f["severity"], 0) + 1
    json.dump({
        "generated": sdr["metadata"]["lastUpdated"],
        "ruleset_version": m["source_version"],
        "schema_version": schema.get("$schemaVersion"),
        "track": m["track"], "class": m["class"],
        "counts": counts,
        "rules_emitted": len(frr_out), "rules_applicable": len(rules_meta),
        "ksis_emitted": len(ksi_out), "ksis_in_scope": len(ksis_meta),
        "findings": findings,
    }, open(a.coverage, "w"), indent=2)

    print(f"SDR      {a.out}  ({len(frr_out)}/{len(rules_meta)} rules, "
          f"{len(ksi_out)}/{len(ksis_meta)} KSIs)")
    print(f"schema   {'VALID' if not errs else str(len(errs)) + ' ERROR(S)'}"
          f"  (v{schema.get('$schemaVersion')})")
    print(f"coverage {a.coverage}  " +
          ", ".join(f"{k}={v}" for k, v in sorted(counts.items())) or "clean")

    # Render the human-readable copy from this same run's outputs, in the same
    # process invocation, so the two formats can never drift apart between a
    # JSON build and a separate doc build (per CDS-CSO-CBF).
    if a.render:
        import sdr_render
        coverage_obj = json.load(open(a.coverage))
        sdr_render.render(sdr, coverage_obj, m, a.render)
        print(f"render   {a.render}")

    if a.strict and (counts.get("BLOCKING") or counts.get("SCHEMA")):
        sys.exit(1)


if __name__ == "__main__":
    main()
