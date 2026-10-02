#!/usr/bin/env python3
"""
Render the human-readable Security Decision Record from the SAME compiled
sdr.json (+ coverage.json + manifest.json) that produced the machine-readable
copy -- never from the authored YAML directly.

This is what makes CDS-CSO-CBF ("use automation to ensure information remains
consistent between human-readable and machine-readable formats") true by
construction rather than by discipline: both formats are two views over one
already-validated object, generated in the same run. If sdr_compile.py is
invoked without --no-render, this script runs automatically on its output.

Output is a single Markdown file. Markdown satisfies "human-readable" and
converts cleanly to PDF/HTML/docx downstream if a submission needs a specific
container format -- that conversion is presentation, not a second source of
truth, so it stays out of this script.
"""
import argparse, json, sys, datetime as dt
from collections import defaultdict

STATUS_MARK = {
    "Implemented": "✅ Implemented",
    "Partially Implemented": "🟡 Partially Implemented",
    "Not Implemented": "🔴 Not Implemented",
    None: "⬜ No record",
}
SEV_MARK = {"BLOCKING": "🔴 BLOCKING", "MAJOR": "🟠 MAJOR",
            "MINOR": "🟡 MINOR", "REVIEW": "🔵 REVIEW", "SCHEMA": "🟣 SCHEMA"}


def load(p):
    with open(p) as f:
        return json.load(f)


def bullets(items, empty="_none recorded_"):
    items = [i for i in (items or []) if i]
    if not items:
        return empty
    return "\n".join(f"- {i}" for i in items)


def evidence_table(items):
    items = items or []
    if not items:
        return "_no evidence attached_\n"
    rows = ["| Type | Description | Location / Text | Last Updated |",
            "|---|---|---|---|"]
    for e in items:
        loc = e.get("evidenceLocation") or (
            f"`{e.get('evidenceText','')[:60]}`" if e.get("evidenceText") else "")
        rows.append(f"| {e.get('evidenceType','')} | {e.get('evidenceDescription','')} "
                    f"| {loc} | {e.get('lastUpdated','')} |")
    return "\n".join(rows) + "\n"


def findings_block(findings, target):
    hits = [f for f in findings if f["target"] == target]
    if not hits:
        return ""
    lines = ["", "> **Open findings:**"]
    for f in hits:
        lines.append(f"> - {SEV_MARK.get(f['severity'], f['severity'])}: {f['message']}")
    return "\n".join(lines) + "\n"


def render(sdr, coverage, manifest, out_path):
    findings = coverage["findings"]
    frr_meta = {r["rule_id"]: r for r in manifest["rules"]}
    ksi_meta = {k["ksi_id"]: k for k in manifest["key_security_indicators"]}
    frr_by_id = {e["frrID"]: e for e in sdr["fedRampRequirements"]}
    ksi_by_id = {e["ksiId"]: e for e in sdr["keySecurityIndicators"]}

    lines = []
    a = lines.append
    md = sdr["metadata"]
    a(f"# Security Decision Record")
    a("")
    a(f"**Certification Package:** {sdr['certificationPackageOverviewUri']}  ")
    a(f"**SDR version:** {md['version']}  ")
    a(f"**Last updated:** {md['lastUpdated']} (source: {md['updateSource']})  ")
    a(f"**Ruleset:** CR26 {coverage['ruleset_version']}, "
      f"track {coverage['track']}, class {coverage['class'].upper()}  ")
    a(f"**Schema version:** {coverage.get('schema_version','n/a')}  ")
    a("")
    a("> Generated automatically from `sdr.json`. Do not hand-edit this file --")
    a("> edit the authored records or evidence inputs and rebuild.")
    a("")

    # ---- summary ----
    a("## Summary")
    a("")
    counts = coverage["counts"]
    a(f"- FedRAMP Requirements: {coverage['rules_emitted']}/"
      f"{coverage['rules_applicable']} applicable rules have a record")
    a(f"- Key Security Indicators: {coverage['ksis_emitted']}/"
      f"{coverage['ksis_in_scope']} in-scope KSIs have a record")
    if counts:
        a(f"- Open findings: " + ", ".join(
            f"{SEV_MARK.get(k,k)} × {v}" for k, v in sorted(counts.items())))
    else:
        a("- Open findings: none")
    a("")

    # ---- FRR, grouped by ruleset ----
    a("## FedRAMP Requirements")
    a("")
    by_ruleset = defaultdict(list)
    for rid, meta in frr_meta.items():
        by_ruleset[(meta["ruleset"], meta["ruleset_name"])].append(rid)
    for (rs_id, rs_name), rids in sorted(by_ruleset.items()):
        a(f"### {rs_id} — {rs_name}")
        a("")
        for rid in sorted(rids):
            meta = frr_meta[rid]
            entry = frr_by_id.get(rid)
            status = entry.get("frrImplementationStatus") if entry else None
            a(f"#### `{rid}` {meta['name']}  {STATUS_MARK.get(status, status)}")
            a("")
            a(f"*{meta['force']}* — {meta['statement']}")
            a("")
            if meta.get("artifacts"):
                a("**Artifacts required:** " + "; ".join(meta["artifacts"]))
                a("")
            if entry:
                a("**Implementation**")
                a(bullets(entry.get("frrImplementation")))
                a("")
                a("**Internal validation**")
                a(bullets(entry.get("frrValidation")))
                a("")
                a("**Independent assessment**")
                a(bullets(entry.get("frrAssessment")))
                a("")
            else:
                a("_No authored record for this rule._")
                a("")
            fb = findings_block(findings, rid)
            if fb:
                a(fb)
            a("---")
            a("")

    # ---- KSI, grouped by family ----
    a("## Key Security Indicators")
    a("")
    by_family = defaultdict(list)
    for kid, meta in ksi_meta.items():
        by_family[(meta["family"], meta["family_name"])].append(kid)
    for (fam, fam_name), kids in sorted(by_family.items()):
        a(f"### {fam} — {fam_name}")
        a("")
        for kid in sorted(kids):
            meta = ksi_meta[kid]
            entry = ksi_by_id.get(kid)
            status = entry.get("ksiImplementationStatus") if entry else None
            a(f"#### `{kid}` {meta['name']}  {STATUS_MARK.get(status, status)}")
            a("")
            if meta.get("statement"):
                a(meta["statement"])
                a("")
            if meta.get("controls"):
                a("**Controls:** " + ", ".join(c.upper() for c in meta["controls"]))
                a("")
            if entry:
                a("**Implementation**")
                a(bullets(entry.get("ksiImplementation")))
                a("")
                a("**Internal validation**")
                a(bullets(entry.get("ksiValidation")))
                a("")
                a("**Independent assessment**")
                a(bullets(entry.get("ksiAssessment")))
                a("")
                a(f"**Automated methods** (class requires "
                  f"{manifest['ksi_min_automated_methods_each']}):")
                a(bullets(entry.get("ksiTests")))
                a("")
                a("**Evidence**")
                a("")
                a(evidence_table(entry.get("ksiEvidence")))
            else:
                a("_No authored record for this KSI._")
                a("")
            fb = findings_block(findings, kid)
            if fb:
                a(fb)
            a("---")
            a("")

    with open(out_path, "w") as f:
        f.write("\n".join(lines))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sdr", default="sdr.json")
    ap.add_argument("--coverage", default="coverage.json")
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--out", default="sdr.md")
    a = ap.parse_args()
    render(load(a.sdr), load(a.coverage), load(a.manifest), a.out)
    print(f"rendered {a.out}")


if __name__ == "__main__":
    main()
