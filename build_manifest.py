#!/usr/bin/env python3
"""
Build an evidence-requirements manifest from the FedRAMP CR26 consolidated rules.

Output: one row per (rule, certification class) with the evidence artifacts that
must be collected, the JSON schema the submission validates against (if any),
and any timeframe that sets a collection cadence / SLA clock.

Usage:
  python build_manifest.py --rules fedramp-consolidated-rules.json \
      --track 20x --klass c --out manifest.json
"""
import argparse, json, csv, sys, urllib.request

RULES_URL = "https://raw.githubusercontent.com/FedRAMP/rules/main/fedramp-consolidated-rules.json"
CLASSES = ["a", "b", "c", "d"]


def load(path_or_none):
    if path_or_none:
        with open(path_or_none) as f:
            return json.load(f)
    with urllib.request.urlopen(RULES_URL) as r:
        return json.load(r)


def flatten_artifacts(art, klass):
    """artifacts is {scope: [str]} where scope is 'all' or a class letter."""
    if not art:
        return []
    out = []
    for scope, items in art.items():
        if scope == "all" or scope == klass:
            out.extend(items)
    return out


def resolve(rule, klass):
    """Collapse varies_by_class onto a flat view for one class."""
    view = {k: v for k, v in rule.items() if k != "varies_by_class"}
    vbc = rule.get("varies_by_class") or {}
    if vbc:
        if klass not in vbc:
            # Source-data quirk: some entries only key a subset of classes
            # (e.g. five KSIs key only 'b'/'c'). Absence is NOT the same as
            # "not applicable" -- flag it for human review instead of dropping.
            view["_class_unspecified"] = True
            view["_classes_defined"] = sorted(vbc.keys())
            return view
        view.update(vbc[klass])
    return view


def cadence(v):
    n, t = v.get("timeframe_num"), v.get("timeframe_type")
    if n and t:
        return f"{n} {t}"
    lo, hi = v.get("timeframe_num_min"), v.get("timeframe_num_max")
    if lo and hi and t:
        return f"{lo}-{hi} {t}"
    return None


def build(data, track, klass, audience):
    rows = []
    for rs_id, rs in data["FRR"].items():
        for subset, groups in rs["data"].items():
            if subset not in ("all", track):
                continue
            for group, rules in groups.items():
                for rid, rule in rules.items():
                    v = resolve(rule, klass)
                    if audience and audience not in v.get("affects", []):
                        continue
                    arts = flatten_artifacts(v.get("artifacts"), klass)
                    schema = (v.get("schema") or {}).get("url")
                    rows.append({
                        "rule_id": rid,
                        "ruleset": rs_id,
                        "ruleset_name": rs["info"]["name"],
                        "subset": subset,
                        "group": group,
                        "name": v.get("name"),
                        "force": v.get("force"),
                        "affects": v.get("affects", []),
                        "statement": v.get("statement"),
                        "artifacts": arts,
                        "artifact_count": len(arts),
                        "schema_url": schema,
                        "cadence": cadence(v),
                        "related": v.get("related", []),
                        "terms": v.get("terms", []),
                        "last_updated": (v.get("updated") or [{}])[0].get("date"),
                        "automatable_hint": bool(schema) or bool(cadence(v)),
                        "class_unspecified": bool(v.get("_class_unspecified")),
                        "classes_defined": v.get("_classes_defined", []),
                    })
    return rows


def ksi_rows(data, klass):
    """KSIs also vary by class; some do not exist below a given class."""
    out = []
    for fam, fv in data["KSI"].items():
        for kid, k in fv["indicators"].items():
            v = resolve(k, klass)
            stmt = v.get("statement")
            if not stmt:
                out.append({"ksi_id": kid, "family": fam, "name": v.get("name"),
                            "statement": None, "controls": v.get("controls", []),
                            "optional_at_this_class": False,
                            "class_unspecified": True,
                            "classes_defined": v.get("_classes_defined", [])})
                continue
            out.append({
                "ksi_id": kid,
                "family": fam,
                "family_name": fv["name"],
                "name": v.get("name"),
                "statement": stmt,
                "optional_at_this_class": stmt.startswith("**Optional:**"),
                "class_unspecified": bool(v.get("_class_unspecified")),
                "classes_defined": v.get("_classes_defined", []),
                "controls": v.get("controls", []),
            })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rules")
    ap.add_argument("--track", default="20x", choices=["20x", "rev5"])
    ap.add_argument("--klass", default="c", choices=CLASSES)
    ap.add_argument("--audience", default="Providers")
    ap.add_argument("--out", default="manifest.json")
    a = ap.parse_args()

    data = load(a.rules)
    rows = build(data, a.track, a.klass, a.audience)
    ksis = ksi_rows(data, a.klass)

    unspec = [k["ksi_id"] for k in ksis if k.get("class_unspecified")]
    unspec_r = [r["rule_id"] for r in rows if r.get("class_unspecified")]
    mandatory = [k for k in ksis
                 if not k["optional_at_this_class"] and not k.get("class_unspecified")]

    # automation obligation for KSIs scales with class
    min_methods = {"a": 0, "b": 1, "c": 2, "d": 4}[a.klass]

    manifest = {
        "source_version": data["info"]["version"],
        "source_last_updated": data["info"]["last_updated"],
        "track": a.track,
        "class": a.klass,
        "audience": a.audience,
        "default_artifacts": data["info"]["default_artifacts"],
        "ksi_min_automated_methods_each": min_methods,
        "needs_human_review": {"ksis": unspec, "rules": unspec_r},
        "rule_count": len(rows),
        "rules_with_named_artifacts": sum(1 for r in rows if r["artifacts"]),
        "distinct_schemas": sorted({r["schema_url"] for r in rows if r["schema_url"]}),
        "key_security_indicators": ksis,
        "rules": sorted(rows, key=lambda r: r["rule_id"]),
    }

    with open(a.out, "w") as f:
        json.dump(manifest, f, indent=2)

    csv_path = a.out.rsplit(".", 1)[0] + ".csv"
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["rule_id", "ruleset", "name", "force", "cadence",
                    "schema_url", "artifact"])
        for r in rows:
            if r["artifacts"]:
                for art in r["artifacts"]:
                    w.writerow([r["rule_id"], r["ruleset"], r["name"], r["force"],
                                r["cadence"] or "", r["schema_url"] or "", art])
            else:
                w.writerow([r["rule_id"], r["ruleset"], r["name"], r["force"],
                            r["cadence"] or "", r["schema_url"] or "",
                            "(default artifacts apply)"])

    print(f"version {manifest['source_version']}  track={a.track} class={a.klass}")
    print(f"  {manifest['rule_count']} applicable rules")
    print(f"  {manifest['rules_with_named_artifacts']} with rule-specific artifacts")
    print(f"  {len(manifest['distinct_schemas'])} distinct submission schemas")
    print(f"  {len(ksis)} KSIs in scope ({len(mandatory)} mandatory at this class)")
    print(f"  x {min_methods} automated methods each = "
          f"{len(mandatory)*min_methods} required automated checks")
    if unspec or unspec_r:
        print(f"  REVIEW: class '{a.klass}' undefined in source for "
              f"{len(unspec)} KSI(s) {unspec} and {len(unspec_r)} rule(s) {unspec_r}")
    print(f"  wrote {a.out} and {csv_path}")


if __name__ == "__main__":
    main()
