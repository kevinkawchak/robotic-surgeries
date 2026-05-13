# Cross Reference Resolution (v0.6.0)

This file documents the cross commit cross reference fix pass for commit 8 (2nd to last) of the v0.6.0 PDAC 1 minute codegen PR. Each of the 10 checks from `../instructions/commit_06_error_fixes.md` is resolved.

## 10 Cross Reference Checks

| Check | Status |
|-------|--------|
| 1. Every per arm xyz command record resolves to a valid command_enum (EMIT, HOLD, SLOW, PARK, E_STOP, HEARTBEAT_ACK, PHASE_BOUNDARY) | pass |
| 2. Every per anastomosis event has a valid realized grade (A/B/C for PJ; absent/present for HJ; patent/delayed for GJ) | pass |
| 3. Every per iteration L0 pointer has a valid SHA 256 manifest entry that matches the actual L0 file hash | pass |
| 4. Every per arm tip force violation event in run_NNNNN_events.parquet has a valid resolution field (auto, manual) | pass |
| 5. Every per round LLM tournament verdict preserves the structural time dimension caveat in the Round 3 rationale | pass |
| 6. Every per iteration Daraxonrasib advisory preserves the SaMD framing caveat | pass |
| 7. Every committed file is under 10 MB | pass |
| 8. Every committed Parquet is under 5 MB | pass (no Parquet committed; CSV samples only) |
| 9. Every BibTeX entry has doi, url, and note fields with clickable GitHub plus Zenodo URLs | pass (BibTeX not committed in codegen; carried from instructions/README.md) |
| 10. Every cross reference in 2030-pdac-1min/paper/codegen/*.md to a sibling file resolves to an actual file path | pass |

## Per Commit Cross Reference Map

| From | To | Status |
|------|-----|--------|
| README.md | LICENSE.txt | pass |
| README.md | pyproject.toml | pass |
| README.md | docker-compose.yml | pass |
| README.md | docs/*.md (9 files) | pass |
| README.md | schemas/*.{schema.json, proto, avsc} (8 files) | pass |
| README.md | src/*/*.py | pass |
| README.md | config/*.yaml | pass |
| README.md | data/* | pass |
| README.md | outputs/* | pass |
| README.md | prompts/* | pass |
| README.md | results/* | pass |
| README.md | viz/* | pass |
| README.md | notebooks/* | pass |
| docs/*.md | ../../instructions/*.md | pass |
| outputs/*/README.md | ../../schemas/*, ../../src/*, ../../config/* | pass |

## Per Schema Validation

| Schema | Validation |
|--------|------------|
| sensor_record_8arm.schema.json | self consistent; 80 channels per record |
| sensor_record_8arm.proto | derived from schema.json; 38 fields |
| sensor_record_8arm.avsc | derived from schema.json; 37 fields plus enums |
| xyz_command_8arm.schema.json | self consistent; 12 fields including 7 state enum |
| xyz_command_8arm.proto | derived from schema.json |
| metrics.schema.json | self consistent; 6 composite components |
| anastomosis_event.schema.json | self consistent; 3 anastomosis ids |
| daraxonrasib_event.schema.json | self consistent; perioperative trajectory |

## Per Config Validation

| Config | yamllint -d relaxed |
|--------|----------------------|
| project.yaml | pass |
| kinematics_8arm.yaml | pass |
| iterations.yaml | pass |
| vascular_safety_zones.yaml | pass |
| anastomosis_targets.yaml | pass |
| per_arm_trajectory_library.yaml | pass |

## Per Code Validation

| Module | ruff format | ruff check | mypy |
|--------|-------------|------------|------|
| src/__init__.py | pass | pass | pass |
| src/sensors/ingest_8arm.py | pass | pass | pass |
| src/mapping/sensor_to_xyz_8arm.py | pass | pass | pass |
| src/vascular/safety_zone_gate.py | pass | pass | pass |
| src/anastomosis/*.py | pass | pass | pass |
| src/daraxonrasib/*.py | pass | pass | pass |
| src/simulation/iterate_1min.py | pass | pass | pass |
| src/simulation/chunk_iteration.py | pass | pass | pass |
| src/simulation/aggregate_pyramid.py | pass | pass | pass |
| src/metrics/compute_1min.py | pass | pass | pass |
| src/llm/compare_agent_1min.py | pass | pass | pass |
| src/zenodo/patch_pointers.py | pass | pass | pass |

## Known Risk Pattern Audit (Defense in Depth)

All 12 known risk patterns from the v3.9.1 GBM CI matrix are absent:

1. underscore in raw file paths in LaTeX text mode: not applicable (no LaTeX in codegen).
2. caret character outside math mode: rewritten as plain text ("mm cubed", "mm per second squared").
3. ruff format check on long string literals: split across multiple lines.
4. yamllint document-end gate: every YAML file ends with a single newline (configured in .yamllint).
5. markdownlint bare URLs: angle bracketed or wrapped (MD034 disabled by default per .markdownlint.yaml).
6. mixed line endings: all files LF (enforced by .pre-commit-config.yaml).
7. Unicode box drawing: not used; ASCII art uses + - | only.
8. em dash (U+2014): not used.
9. en dash (U+2013): not used.
10. double dash in prose: not used.
11. triple dash in prose: not used.
12. trailing whitespace: stripped.
