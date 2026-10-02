#!/usr/bin/env python3
"""
Generate authoring stubs from a CR26 manifest.

Creates one YAML file per applicable rule and per in-scope KSI. These files are
the HUMAN input surface: narrative, status, and declared evidence sources.
They are versioned in git and reviewed by pull request.

They deliberately do NOT hold evidence payloads. Evidence arrives from
collectors at build time (see sdr_compile.py). Regenerating is safe: existing
files are never overwritten unless --force is passed.
"""
import argparse, json, os, sys

try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")

HEADER = """# AUTHORED RECORD -- edit the narrative fields below.
# Generated from CR26 {version} (track {track}, class {klass}).
# 'rule_statement' and 'artifacts_required' are reference copies from the
# ruleset; the compiler re-reads them from the manifest and ignores edits here.
"""


def stub_for_rule(r, klass):
    return {
        "rule_id": r["rule_id"],
        "kind": "FRR",
        "name": r["name"],
        "force": r["force"],
        "rule_statement": r["statement"],
        "artifacts_required": r["artifacts"] or "(default artifacts apply)",
        "schema_url": r["schema_url"],
        "cadence": r["cadence"],
        # ---- authored fields ----
        "status": "Not Implemented",
        "implementation": [],
        "validation": [],
        "not_implemented_rationale": None,
        "risk_to_customers": None,
        "accepted_by": None,
        "evidence_sources": [],
        "owner": None,
    }


def stub_for_ksi(k, min_methods):
    return {
        "ksi_id": k["ksi_id"],
        "kind": "KSI",
        "name": k["name"],
        "family": k["family"],
        "rule_statement": k["statement"],
        "controls": k.get("controls", []),
        "optional_at_this_class": k.get("optional_at_this_class", False),
        "min_automated_methods": min_methods,
        # ---- authored fields ----
        "status": "Not Implemented",
        "implementation": [],
        "validation": [],
        "measure_cycle": None,
        "tests": [],
        "evidence_sources": [],
        "owner": None,
    }


def write(path, obj, header, force):
    if os.path.exists(path) and not force:
        return False
    with open(path, "w") as f:
        f.write(header)
        yaml.safe_dump(obj, f, sort_keys=False, allow_unicode=True,
                       default_flow_style=False, width=100)
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--dir", default="records")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()

    m = json.load(open(a.manifest))
    hdr = HEADER.format(version=m["source_version"], track=m["track"],
                        klass=m["class"])
    os.makedirs(f"{a.dir}/frr", exist_ok=True)
    os.makedirs(f"{a.dir}/ksi", exist_ok=True)

    new = skipped = 0
    review = set(m["needs_human_review"]["rules"]) | set(m["needs_human_review"]["ksis"])

    for r in m["rules"]:
        p = f"{a.dir}/frr/{r['rule_id']}.yaml"
        h = hdr
        if r["rule_id"] in review:
            h += ("# REVIEW: this class is not defined for this rule in the source\n"
                  "# ruleset. Confirm applicability before certifying.\n")
        new += write(p, stub_for_rule(r, m["class"]), h, a.force) or 0
        skipped += 0 if write.__name__ else 0

    for k in m["key_security_indicators"]:
        p = f"{a.dir}/ksi/{k['ksi_id']}.yaml"
        h = hdr
        if k.get("class_unspecified"):
            h += ("# REVIEW: this class is not defined for this KSI in the source\n"
                  "# ruleset (defined for: %s).\n" % ", ".join(k.get("classes_defined", [])))
        new += write(p, stub_for_ksi(k, m["ksi_min_automated_methods_each"]), h, a.force) or 0

    total = len(m["rules"]) + len(m["key_security_indicators"])
    print(f"scaffold: {new} created, {total - new} already existed, {total} total")
    print(f"  -> {a.dir}/frr/  and  {a.dir}/ksi/")


if __name__ == "__main__":
    main()
