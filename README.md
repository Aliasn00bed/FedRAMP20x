# fedramp-sdr

Compiles a FedRAMP CR26 Security Decision Record from git-tracked authored
records + collected evidence, validates it against the vendored schema, and
renders the human-readable copy from the same build.

## Layout

```
manifest/    fedramp-consolidated-rules.json (pinned upstream snapshot)
             manifest.json (derived -- rebuilt by `make manifest`)
schemas/     vendored FedRAMP JSON Schemas (validation never hits the network)
records/     AUTHORED. One YAML file per rule (frr/) and per KSI (ksi/).
             This is what you edit and PR-review. Never hand-edit sdr.json.
evidence/
  collected/    APPEND-ONLY. One *.jsonl per collector. Machine-written.
  assessments/  APPEND-ONLY. 3PAO / independent-assessor input, kept
                separate so it can't be edited by the same pipeline that
                writes implementation claims.
tooling/     the four scripts (build_manifest, sdr_scaffold, sdr_compile,
             sdr_render) -- reusable, not project-specific.
sdr.json     BUILD OUTPUT. Machine-readable SDR. Not committed (see below).
sdr.md       BUILD OUTPUT. Human-readable SDR, rendered from sdr.json.
coverage.json BUILD OUTPUT. Findings: missing records, stale evidence,
             schema errors, unmet automation minimums.
```

## First run (dry run -- proves the pipeline works, no content needed)

```
make dry-run
```

Runs the full compile against whatever is in `records/` and `evidence/`
right now -- on a fresh checkout that's nothing, so every rule and KSI shows
up as a BLOCKING gap. That's expected and correct: it confirms schema
validation, the local `$ref` resolution, and the render step all work,
before you've written a single line of real content. Output goes to `/tmp/`
so it can never be confused with a real build.

## Standing it up for real

```
make manifest    # only needed after you intentionally bump the rules snapshot
make scaffold    # generates records/frr/*.yaml and records/ksi/*.yaml stubs
                 # -- safe to re-run any time; never overwrites existing files
```

Then edit the stubs in `records/`. Each file has `status`, `implementation`,
`validation`, and (for KSIs) `tests` as the fields to fill in. Commit these
as normal PRs.

Point your collectors at `evidence/collected/<collector-name>.jsonl`, one
JSON object per line, per the contract documented in `tooling/sdr_compile.py`.
Point your 3PAO's output at `evidence/assessments/<name>.jsonl` the same way.

```
make build       # compiles sdr.json + sdr.md + coverage.json, always exits 0
make strict      # same, but fails the command (exit 1) on BLOCKING/SCHEMA
                 #   findings -- use this one in CI merge/release gates
```

Read `coverage.json` (or the inline findings in `sdr.md`) after any build to
see what's missing.

## What to commit

Commit `records/`, `evidence/` history, `manifest/fedramp-consolidated-rules.json`,
and `tooling/`. **Do not** commit `sdr.json`, `sdr.md`, or `coverage.json` on
every commit to `main` -- they're fully derived and would just be merge-conflict
noise. Two reasonable options for the build outputs themselves:

- Have CI publish them as workflow artifacts / to a dedicated `published`
  branch or release asset on a schedule, so there's always a latest copy
  without cluttering `main`'s history.
- Commit them only at tagged submission points (`git tag cr26-2026-Q4-submission`)
  so there's an auditable snapshot tied to an actual FedRAMP submission,
  without every intermediate iteration living in history.

This repo's `.gitignore` assumes the first option. Change it if you want the
second.

## Bumping the ruleset

FedRAMP publishes `fedramp-consolidated-rules.json` on its own cadence.
Bumping it is a deliberate act, not automatic:

```
curl -o manifest/fedramp-consolidated-rules.json \
  https://raw.githubusercontent.com/FedRAMP/rules/main/fedramp-consolidated-rules.json
make manifest
make scaffold   # picks up any newly-added rules/KSIs as new stub files
```

Review the diff in `manifest/manifest.json` before merging -- a version bump
can change `force` (MAY->MUST), add rule-specific artifacts, or change a
cadence, any of which changes what's required of you.
