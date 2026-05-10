# Changelog

All notable changes to this repository are documented in this file.
Format: Keep a Changelog. Versioning: Semantic Versioning.

## v0.2.0 - 2026-05-10

### Added

- `2030-gbm-1min/outputs/` end-to-end run tree under deterministic seed 20260510. New subdirectories: `sensors/`, `xyz_mapping/`, `iterations/`, `metrics/`, `comparison/`, `comparison_robot_vs_human/`, `diagrams/`, `viz/`, `reports/`, `logs/`.
- 1000-row sensor sample (jsonl + csv) plus per-arm and aggregate force statistics; per_arm_violations=0 cumulative_violations=0.
- 240-row per-arm xyz command traces plus the ASCII per-second xyz path overlay; all 240 commands resolve to command_state=EMIT.
- 16-iteration deterministic sweep with per-iteration L1 50 ms, L2 1 s, L3 phase, events Parquet plus L0 Zenodo pointer JSON; cross-iteration index.jsonl and DuckDB analytical store.
- Per-iteration metric rows (16 robot + 30 human baseline) under the frozen weighted formula (quality 0.40, time 0.25, cost 0.20, safety 0.10, patient_experience 0.05).
- Default 4-entity tournament (robot vs robot, 6 rounds) plus a mixed 4-entity tournament (2 robot + 2 human, 6 rounds); structural-time-dimension caveat preserved in every rationale.
- 6 curated ASCII diagrams: pipeline architecture, 4-arm coordination heartbeat, 60-second phase timeline, file size pyramid, composite score formula plus aggregates, on-prem LLM control loop instantiating the thesis.
- 4 ASCII bar/histogram charts: composite per iteration, composite histogram (robot vs human), per-arm resection mean (mm^3), wall-clock per iteration.
- 4 narrative reports: run summary, process log, final report, limitations.
- Publication-grade outputs README with DOI badges, thesis block, repository structure, pipeline architecture ASCII, 4-arm coordination ASCII, robot-vs-human aggregate table, mixed tournament leaderboard, citation block, license pointer.
- CI verification log under `2030-gbm-1min/outputs/logs/ci_verification.log` capturing the green state of every CI lint-and-format gate.

### Changed

- Top-level `README.md` updated with v0.2.0 outputs pipeline ASCII, the new `outputs/` subtree in the repository structure block, the v0.2.0 release badge, an Outputs badge, and a See-also pointer to `outputs/README.md`.
- `2030-gbm-1min/config/kinematics_4arm.yaml` joint_limits_per_arm block expanded from inline flow-style entries to block-mapping form to clear the 7 yamllint line-length warnings.

### Fixed

- `yamllint -d relaxed 2030-gbm-1min/config/` exits cleanly with no warnings.
- All Python sources continue to pass `ruff format --check` and `ruff check` on Python 3.10, 3.11, and 3.12.
- File size cap check passes; no committed file exceeds 10 MB and no committed Parquet exceeds 5 MB.
- Resolves the upstream `Cl / lint-and-format (3.10)`, `(3.11)`, and `(3.12)` failing checks template.

### Notes

- The v0.2.0 outputs are reproducible bit for bit from seed 20260510.
- The C++20 control loop, C++20 1 kHz heartbeat layer, and Rust 2021 high-throughput runner are documented but not compiled in this run; see `outputs/reports/limitations.md`.
- The release-aggregate L0 raw archive (~416 MB across 16 iterations) lives on Zenodo only at DOI 10.5281/zenodo.18445179.

## v0.1.0 - 2026-05-10

### Added

- 4-arm 1-minute glioblastoma trial under `2030-gbm-1min/` (project version v3.9.1).
- Top-level main README with high-level architecture ASCII and 4-arm coordination ASCII snapshot.
- `releases.md` with the v0.1.0 release notes block (title, summary, features, contributors, notes).
- `references.md` with citations of standards, prior art, and inputs.
- `.github/workflows/ci.yml` matrix on Python 3.10, 3.11, and 3.12 covering ruff format, ruff check, yamllint, and the file size cap. Resolves the upstream `Cl / lint-and-format (3.10) (pull...)`, `(3.11)`, and `(3.12)` failing checks.
- 4-arm Medtronic NeuroSpeed 1.0 specification with 7-DOF DH parameters, per-arm tool assignment, and per-arm safety limits.
- 4-phase 60-second procedure timeline (dural opening, bulk resection, margin assessment, hemostasis withdrawal).
- 200-channel sensor schema (50 channels per arm times 4 arms) in JSON Schema 2020-12, Protocol Buffers 3, and Apache Avro.
- Deterministic per-arm sensor sample JSONL and CSV; deterministic per-arm xyz command CSV samples; 60-line ASCII per-second xyz path visualization.
- Python 3.10 ingest, mapping, simulation orchestrator, metrics, on-prem LLM tournament agent (Anthropic claude-opus-4-7 default, Ollama optional), and Zenodo pointer patcher.
- C++20 real-time control loop and 1 kHz heartbeat sender / receiver layer compatible with Linux, MacOS, and Windows toolchains.
- Rust 2021 high-throughput simulation runner with Cargo manifest plus optional CUDA feature flag.
- 16-iteration sweep produces 80 per-iteration Parquet files plus the cross-iteration index.jsonl manifest, DuckDB analytical store placeholder, and iteration_run.txt log.
- Comparison methodology with composite score formula and structural-vs-fair time-dimension call-out.
- 30-row human-surgeon baseline carry-forward across 6 centers; aggregated robot outcomes; structured comparison.json; narrative comparison_report.md plus PDF placeholder.
- Self-contained Plotly metrics_dashboard.html, static metrics_summary.png, and per_arm_contribution.png chart placeholders.
- Immutable v3.9.1 release snapshot under `2030-gbm-1min/releases/v3.9.1/` with manifest.json, metrics.json, iterations_index.jsonl, sample_seeds.txt, and zenodo_doi.txt.

### Changed

- Top-level `README.md` rewritten from the placeholder text to the full project narrative, repository structure, ASCII diagrams, and quick-start pointer.

### Fixed

- All Python sources pass `ruff format --check` and `ruff check` on Python 3.10, 3.11, and 3.12.
- `yamllint -d relaxed` passes on `2030-gbm-1min/config/`.
- Notebook `iteration_analysis_1min.ipynb` cells pass ruff import sorting.
- File size cap check passes; no committed file exceeds 10 MB and no committed Parquet exceeds 5 MB.

### Notes

- All instruction files in `kevinkawchak/physical-ai-oncology-trials/competitions/instructions/one_minute_variant/` were read for shared context; no commits were made to that repository under this release.
- The release-aggregate L0 raw (416 MB across 16 iterations) lives on Zenodo only at DOI 10.5281/zenodo.18445179.
