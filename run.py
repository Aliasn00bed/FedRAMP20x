#!/usr/bin/env python3
"""
Mirrors every Makefile target, for machines without `make` (plain Windows
cmd/PowerShell without WSL or Git Bash + make installed).

    python run.py dry-run
    python run.py scaffold
    python run.py build
    python run.py strict
    python run.py manifest
    python run.py clean

Behaves identically to the matching `make <target>` -- same arguments, same
exit codes. Internal glob expansion means it is Windows-safe where invoking
the Makefile's own `*.jsonl` shell globs directly would not be.
"""
import subprocess, sys, os, shutil

TRACK = "20x"
KLASS = "c"
PKG_URI = "https://trust.example.com/cpo.json"
SCHEMA = "schemas/fedramp-security-decision-record-schema-2026-06-24.json"
RULES_SRC = "manifest/fedramp-consolidated-rules.json"
MANIFEST = "manifest/manifest.json"
PY = sys.executable  # use whichever python is running this, not a hardcoded name


def run(args):
    print("+", " ".join(args))
    r = subprocess.run(args)
    return r.returncode


def manifest():
    return run([PY, "tooling/build_manifest.py", "--rules", RULES_SRC,
                "--track", TRACK, "--klass", KLASS, "--out", MANIFEST])


def scaffold():
    return run([PY, "tooling/sdr_scaffold.py", "--manifest", MANIFEST,
                "--dir", "records"])


def _compile(out, coverage, render, today=None, strict=False):
    os.makedirs("evidence/collected", exist_ok=True)
    os.makedirs("evidence/assessments", exist_ok=True)
    args = [PY, "tooling/sdr_compile.py",
            "--manifest", MANIFEST, "--schema", SCHEMA,
            "--package-uri", PKG_URI,
            "--evidence", "evidence/collected/*.jsonl",
            "--assessments", "evidence/assessments/*.jsonl",
            "--out", out, "--coverage", coverage, "--render", render]
    if today:
        args += ["--today", today]
    if strict:
        args += ["--strict"]
    return run(args)


def build():
    return _compile("sdr.json", "coverage.json", "sdr.md")


def strict():
    return _compile("sdr.json", "coverage.json", "sdr.md", strict=True)


def dry_run():
    tmp = os.environ.get("TEMP", "/tmp")
    rc = _compile(os.path.join(tmp, "sdr.dryrun.json"),
                  os.path.join(tmp, "coverage.dryrun.json"),
                  os.path.join(tmp, "sdr.dryrun.md"),
                  today="2026-09-18")
    import json
    cov = json.load(open(os.path.join(tmp, "coverage.dryrun.json")))
    print("--- dry run coverage summary ---")
    print(cov["counts"])
    return rc


def clean():
    for f in ("sdr.json", "sdr.md", "coverage.json"):
        if os.path.exists(f):
            os.remove(f)
    return 0


TARGETS = {
    "manifest": manifest, "scaffold": scaffold, "build": build,
    "strict": strict, "dry-run": dry_run, "clean": clean,
}

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in TARGETS:
        print(f"usage: python run.py [{'|'.join(TARGETS)}]")
        sys.exit(1)
    sys.exit(TARGETS[sys.argv[1]]())
