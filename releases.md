# Release Notes

This file tracks every tagged release of the robotic-surgeries repository.
Releases follow semantic versioning. The first project to land here is the
4-arm 1-minute glioblastoma trial in `2030-gbm-1min/` (project version
v3.9.1, repository release v0.1.0).

## Release title

v0.1.0 - 4-Arm 1-Minute Glioblastoma Trial Simulation (Medtronic NeuroSpeed 1.0)

## Summary

This release lands the first complete project under robotic-surgeries: the v3.9.1 4-arm 1-minute glioblastoma resection simulation (`2030-gbm-1min/`). The project operationalizes the on-premises LLM thesis at the upper edge of feasible robotic speed: a hypothetical 2030 Medtronic NeuroSpeed 1.0 four-arm parallel stereotactic neurosurgical robot completes a maximal safe gross-total resection of a 4.2 cm right frontal IDH-wildtype glioblastoma in 60 seconds. Per-arm sensors stream at mixed 1 kHz commands plus 10 kHz force; a deterministic 1 kHz heartbeat broadcasts 32-byte status frames with a 1 ms deadline; cumulative tip force across the 4 arms is capped at 12 N on the patient frame; the E-stop budget is 5 ms with a 100 microsecond emergency arm-park trigger. Sixteen deterministic iterations sweep noise, gain, IK tolerance, and heartbeat jitter; per-iteration L1 to L3 plus events Parquet aggregates plus the per-iteration L0 raw Zenodo pointer JSON live under `2030-gbm-1min/data/iterations/`. The release-aggregate L0 raw archive (416 MB across 16 iterations) is deposited to Zenodo (DOI 10.5281/zenodo.18445179).

## Features

- 4-arm Medtronic NeuroSpeed 1.0 specification with 7-DOF DH parameters, per-arm tool assignment (hybrid u-w-p, bipolar+irr, suction+col, iMRI+ALA), and per-arm safety limits (5.0 N tip, 1.0 N lateral, 5 ms E-stop, 8 mm inter-arm clearance).
- 4-phase 60-second procedure timeline (dural opening final 5 s, bulk resection 40 s, margin assessment 10 s, hemostasis withdrawal 5 s) with cross-arm coordination.
- 200-channel sensor schema (50 channels per arm times 4 arms) in JSON Schema 2020-12, Protocol Buffers 3, and Apache Avro.
- Deterministic per-arm sensor sample JSONL and CSV files, deterministic per-arm xyz command CSV samples, and a 60-line ASCII per-second xyz path visualization.
- Python 3.10 ingest, mapping, simulation orchestrator, metrics, and on-prem LLM tournament agent (Anthropic claude-opus-4-7 default, Ollama optional).
- C++20 real-time control loop and 1 kHz heartbeat sender / receiver layer compatible with Linux, MacOS, and Windows toolchains.
- Rust 2021 high-throughput simulation runner with Cargo manifest and optional CUDA feature flag for NVIDIA A100 GPU acceleration.
- 16-iteration sweep generates 80 per-iteration Parquet files (L1 50 ms, L2 1 s, L3 per-phase, events, L0 raw Zenodo pointer JSON) plus the per-release index.jsonl manifest, the cross-iteration DuckDB analytical store, and the iteration_run.txt log.
- Comparison methodology with composite score formula (Quality 0.40, Time 0.25 with structural-advantage call-out, Cost 0.20, Safety 0.10, Patient experience 0.05), 30-row human-surgeon baseline carry-forward across 6 international centers, structured comparison.json, narrative comparison_report.md plus PDF, self-contained Plotly metrics_dashboard.html, and per_arm_contribution.png chart.
- Immutable v3.9.1 release snapshot under `2030-gbm-1min/releases/v3.9.1/` with manifest.json, metrics.json, iterations_index.jsonl, sample_seeds.txt, and zenodo_doi.txt.
- Top-level main README, CHANGELOG, references, and v0.1.0 release notes plus the GitHub Actions CI workflow that exercises ruff format, ruff check, yamllint, and the file size cap on Python 3.10, 3.11, and 3.12.

## Contributors

@kevinkawchak
@claude
@openai
@google-gemini

## Notes

- The 1-minute scenario trivially beats the 1-hour scenario on the time dimension; this advantage is structural and not a fair pairwise comparison. The comparison report and the LLM judge prompt explicitly flag this.
- The 16-iteration committed footprint is approximately 9.7 MB. The release-aggregate L0 raw (416 MB across 16 iterations) lives on Zenodo only; pointer JSON files in `data/` and `data/iterations/` resolve to the deposition.
- All committed files honor the 10 MB per-file cap and the 5 MB committed-Parquet cap. The CI workflow enforces both.
- Python and C++ source files reference IEC 80601-2-77 (per-arm 5.0 N tip, 1.0 N lateral, 5 ms E-stop), IEC 62304 (safety-critical software lifecycle at the 1 kHz heartbeat layer), and 21 CFR 50.30 (task-order lifecycle).
- All instruction files in `kevinkawchak/physical-ai-oncology-trials/competitions/instructions/one_minute_variant/` were read for shared context; no commits were made to that repository under this release.
