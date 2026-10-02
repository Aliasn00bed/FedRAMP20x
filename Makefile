TRACK      := 20x
CLASS      := c
PKG_URI    := https://trust.example.com/cpo.json
SCHEMA     := schemas/fedramp-security-decision-record-schema-2026-06-24.json
RULES_SRC  := manifest/fedramp-consolidated-rules.json
MANIFEST   := manifest/manifest.json

.PHONY: manifest scaffold build dry-run strict clean refresh-rules

# Rebuild manifest.json from the pinned rules snapshot. Run this whenever you
# intentionally bump manifest/fedramp-consolidated-rules.json, not on every commit.
manifest:
	python3 tooling/build_manifest.py --rules $(RULES_SRC) \
		--track $(TRACK) --klass $(CLASS) --out $(MANIFEST)

# Generate stub YAML for any rule/KSI that doesn't have a record yet.
# Never overwrites existing authored files.
scaffold:
	python3 tooling/sdr_scaffold.py --manifest $(MANIFEST) --dir records

# Compile whatever records + evidence currently exist into sdr.json,
# coverage.json and sdr.md. Non-blocking: always exits 0, meant for local
# iteration and CI status checks -- read coverage.json / sdr.md for gaps.
build:
	python3 tooling/sdr_compile.py \
		--manifest $(MANIFEST) \
		--schema $(SCHEMA) \
		--package-uri $(PKG_URI) \
		--evidence evidence/collected/*.jsonl \
		--assessments evidence/assessments/*.jsonl \
		--out sdr.json --coverage coverage.json --render sdr.md

# Same as build, but with a fixed --today and no real evidence required --
# this is the "does the pipeline run end-to-end" dry run. Safe against an
# empty evidence/ directory; every rule will just show as a gap.
dry-run:
	@mkdir -p evidence/collected evidence/assessments
	@touch evidence/collected/.keep evidence/assessments/.keep
	python3 tooling/sdr_compile.py \
		--manifest $(MANIFEST) \
		--schema $(SCHEMA) \
		--package-uri $(PKG_URI) \
		--evidence evidence/collected/*.jsonl \
		--assessments evidence/assessments/*.jsonl \
		--out /tmp/sdr.dryrun.json --coverage /tmp/coverage.dryrun.json \
		--render /tmp/sdr.dryrun.md --today 2026-09-18
	@echo "--- dry run coverage summary ---"
	@python3 -c "import json; c=json.load(open('/tmp/coverage.dryrun.json')); print(c['counts'])"

# CI gate: same as build, but fails (nonzero exit) on any BLOCKING or SCHEMA
# finding. This is what a merge/release check should call.
strict:
	python3 tooling/sdr_compile.py \
		--manifest $(MANIFEST) \
		--schema $(SCHEMA) \
		--package-uri $(PKG_URI) \
		--evidence evidence/collected/*.jsonl \
		--assessments evidence/assessments/*.jsonl \
		--out sdr.json --coverage coverage.json --render sdr.md \
		--strict

clean:
	rm -f sdr.json sdr.md coverage.json /tmp/sdr.dryrun.* /tmp/coverage.dryrun.*
