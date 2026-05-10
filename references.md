# References

This file collects the citations referenced by the v0.1.0 release of the
robotic-surgeries repository. Entries are grouped by category and ordered
within each group by relevance to the 4-arm 1-minute glioblastoma trial.

## Standards and Regulatory

1. ICH E6(R3) Adaption. DOI: 10.5281/zenodo.18973368. Section 2.3 medical care; section 2.10 safety reporting; section 2.12 investigator oversight of physical AI.
2. 21 CFR Part 50 Adaption. DOI: 10.5281/zenodo.19040707. Section 50.30 task-order lifecycle and runtime safety monitoring at 1 kHz per arm; forbidden operations.
3. 21 CFR Part 312 Adaption. DOI: 10.5281/zenodo.19057628. Section 312.404 human oversight; section 312.62 investigator recordkeeping.
4. IEC 80601-2-77. Medical electrical equipment particular requirements for the basic safety and essential performance of robotically assisted surgical equipment. Per-arm 5.0 N tip force limit, 1.0 N lateral force limit, cumulative 12 N four-arm patient-frame cap, 5 ms E-stop budget.
5. IEC 62304. Medical device software lifecycle processes. Applied to the 1 kHz heartbeat layer and the per-arm real-time control loop.

## Datasets, DOIs, and Archives

1. Glioblastoma 1-Minute Trial Simulation v3.9.1 release archive. DOI: 10.5281/zenodo.18445179. Release-aggregate L0 raw across 16 iterations (416 MB Parquet zstd-3) plus per-iteration L0 raw plus per-arm xyz trace.
2. Per-iteration Zenodo pointer JSON files at `2030-gbm-1min/data/iterations/run_NNNNN_L0_raw.zenodo_pointer.json`. Bridge the GitHub-committed L1 to L3 aggregates with the Zenodo-archived L0 raw via SHA-256.

## Companion Equipment

1. StealthStation S8 (Medtronic). Preoperative MRI registration and intraoperative navigation source for the per-arm `nav_dx`, `nav_dy`, `nav_dz` channels.
2. Mayfield clamp. Head fixation; clamp position frozen at simulation start; the world-frame origin is the clamp pin midpoint.
3. iMRI 0.5 T (hypothetical 2030 high-frame-rate variant). Drives the per-arm-4 `imri_active` flag and the 30 fps imaging stream during Phase 1 and Phase 2 of the 1-minute scenario.
4. ROBO ALA-560 ultraviolet illumination unit. Drives the per-arm-4 `ala_uv` flag.
5. Boston Dynamics ATLAS-derived parallel arm controller. Drives the 360 deg per second joint angular velocity per arm.
6. CUSA aspirator (current SOTA reference). 2 to 5 mm cubed per second tissue removal rate; the 1-minute variant requires a 200 times faster hybrid mechanism on arm 1.
7. ROSA ONE Brain v3.0 (Medtronic, current SOTA stereotactic neurosurgical robot). Reference platform whose constraints the hypothetical 2030 NeuroSpeed 1.0 exceeds across every dimension.

## Methods and Models

1. Anthropic Claude Opus 4.7 model. Default backend for the on-prem LLM comparison agent at `2030-gbm-1min/src/llm/compare_agent_1min.py`. Anthropic SDK reference: https://docs.anthropic.com.
2. Ollama optional local backend. Listed in `pyproject.toml` extras under `llm-local`.
3. TrueSkill-style Gaussian skill rating model. mu_0 = 600, sigma_0 = 200; per-round update follows draw and victory probability rules. Mirrors the parent v3.9.0 1-hour scenario.
4. Bootstrap 95 percent confidence intervals across 16 iterations. Mann-Whitney U for pairwise comparisons.
5. Levenberg-Marquardt 7-DOF inverse kinematics solver. 0.1 mm tolerance and a 5 microsecond per-call wall budget on the conventional high-end server profile.

## Source Code Conventions

1. Python 3.10 with type hints, ruff format, ruff check. CI matrix on 3.10, 3.11, 3.12.
2. C++20 with IEC 62304 lifecycle citations in the file header. POSIX shared memory and atomic operations for the in-process simulation; the same code can be deployed against EtherCAT, TSN, or CAN-FD by replacing the transport layer.
3. Rust 2021 with `cargo fmt` and `cargo clippy --all-targets -- -D warnings`. Optional CUDA feature flag for NVIDIA A100 GPU acceleration.
4. JSON Schema 2020-12, Protocol Buffers 3, and Apache Avro for the sensor and xyz command schemas.

## Instruction Set Provenance (Read-only Source)

1. `kevinkawchak/physical-ai-oncology-trials/competitions/instructions/one_minute_variant/README.md`. Top-level orientation and table of contents for the 1-minute variant instruction set.
2. `kevinkawchak/physical-ai-oncology-trials/competitions/instructions/one_minute_variant/glioblastoma_context_1min.md`. Patient PAT-GBM-0001, disease boundaries, and the 4-phase 60-second timeline.
3. `kevinkawchak/physical-ai-oncology-trials/competitions/instructions/one_minute_variant/robot_specification_neurospeed.md`. Hypothetical 2030 Medtronic NeuroSpeed 1.0 specification.
4. `kevinkawchak/physical-ai-oncology-trials/competitions/instructions/one_minute_variant/sensor_specification_10khz.md`. 10 kHz force sensors per arm with 1 kHz command sensors; total 200 channels.
5. `kevinkawchak/physical-ai-oncology-trials/competitions/instructions/one_minute_variant/multi_arm_coordination.md`. Inter-arm collision avoidance protocol, 1 kHz heartbeat, 100 microsecond emergency arm-park trigger.
6. `kevinkawchak/physical-ai-oncology-trials/competitions/instructions/one_minute_variant/file_size_pyramid_1min.md`. Pyramid Layer 4 budget table; per-iteration committed budget of 510 KB across L1 plus L2 plus L3 plus events.
7. `kevinkawchak/physical-ai-oncology-trials/competitions/instructions/one_minute_variant/commit_01_overview_1min.md` through `commit_05_competition_1min.md`. Per-commit file lists for the 1-minute variant.
8. `kevinkawchak/physical-ai-oncology-trials/competitions/instructions/one_minute_variant/zenodo_archive_protocol.md`. DOI assignment, deposition layout, SHA-256 manifest contract for the 416 MB L0 archive.

## Prior Art Acknowledged

1. Orbit Wars Kaggle competition. Skill rating mu_0 and sigma_0 conventions shared with the parent v3.9.0 scenario.
2. Apache Arrow / Apache Parquet / DuckDB. Storage and query engines for the L1 to L3 aggregates and the cross-iteration analytical store.
3. Plotly and matplotlib. HTML dashboard and static chart rendering.
4. pandoc + xelatex. PDF rendering of the comparison report.
