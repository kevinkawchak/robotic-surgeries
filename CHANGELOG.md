# Changelog

All notable changes to this repository are documented in this file.
Format: Keep a Changelog. Versioning: Semantic Versioning.

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
