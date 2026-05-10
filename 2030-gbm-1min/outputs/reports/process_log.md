# Process Log

This document records, in narrative form, the entire process used to
materialize the outputs tree. Each step is reproducible from the seed
20260510 plus the script invocation as documented in
`outputs/logs/`.

## Step 1 - Repository inventory

Surveyed the `2030-gbm-1min/` tree to map runnable entry points to their
expected output locations. Confirmed the 19 source files under `src/` (Python
plus C++ plus Rust) and the 11 Python click CLI scripts under `src/sensors`,
`src/mapping`, `src/simulation`, `src/metrics`, `src/llm`, and `src/zenodo`.
Identified the on-disk artifacts already present under `data/`, `viz/`,
`results/`, and `releases/v3.9.1/` so that re-running into `outputs/` would
not corrupt the upstream committed snapshots. The C++ control loop
(`robot_loop_4arm.cpp`), C++ heartbeat layer (`arm_heartbeat.cpp`), and Rust
high-throughput runner (`runner_1min.rs`) are documented but not compiled in
this environment because the Linux 6.18.5 sandbox lacks `g++`, `clang++`,
`cargo`, `rustc`, `apache-arrow`, and `pandoc`. These limitations are listed
explicitly in `outputs/reports/limitations.md`.

## Step 2 - Sensor ingestion

Invoked `python -m sensors.ingest_4arm --seed 20260510 --out outputs/sensors
--emit-sample --emit-csv-sample` to produce a 1000-row JSONL sample and a
1000-row CSV sample. Subsequently invoked `--validate` on the JSONL output
and confirmed `per_arm_violations=0 cumulative_violations=0` against the
5.0 N per-arm tip and 12 N cumulative-four-arm-tip envelope. Per-arm row
counts: 250 each across ARM_1, ARM_2, ARM_3, ARM_4. Robot state distribution:
READY 256, ACTIVE 496, COMPLETE 248. Safety zone distribution: OUTER 504,
TUMOR_CORE 124, TUMOR_MARGIN 186, ELOQUENT 186.

## Step 3 - xyz mapping

Invoked `python -m mapping.sensor_to_xyz_4arm --seed 20260510
--csv-sample-out-dir outputs/xyz_mapping --ascii-viz-out
outputs/xyz_mapping/xyz_path_4arm.txt`. Each per-arm CSV holds a 60-tick
trace covering 6 ms of phase 2 bulk resection (sample at 100 microsecond
cadence starting at tick_us=5000000). All 240 commands resolve to
command_state=EMIT under the seed.

## Step 4 - 16-iteration sweep

Invoked `python -m simulation.iterate_1min --seed 20260510 --iterations 16
--out outputs/iterations`. The deterministic sweep linearly interpolates
sensor noise sigma 0.01 to 0.05 mm, force gain 0.8 to 1.2, heartbeat jitter
sigma 0 to 50 microseconds, and log-interpolates IK tolerance 1e-6 to 1e-3.
Each iteration emits 5 files (L1 50 ms, L2 1 s, L3 phase, events Parquet
plus L0 Zenodo pointer JSON). The cross-iteration index.jsonl manifest, the
DuckDB analytical store, and the iteration_run.txt log are written
alongside. Total on-disk footprint 352 KB.

## Step 5 - Metric computation

Invoked `python -m metrics.compute_1min --iterations-dir outputs/iterations
--baseline data/human_surgeon_baseline.csv --out
outputs/metrics/robot_outcomes_1min.parquet --aggregate-iterations`. Per
iteration the script applies the frozen weighted formula (quality 0.40, time
0.25, cost 0.20, safety 0.10, patient_experience 0.05) over the iteration
record. The 30-row human-surgeon baseline is appended for downstream
comparison. A JSON mirror is also produced for the LLM agent input which
expects a JSON array. A mixed 4-row outcomes file (2 robot + 2 human) is
constructed for the second tournament.

## Step 6 - LLM tournament

Invoked `python -m llm.compare_agent_1min --backend anthropic --model
claude-opus-4-7 --tournament-size 4 --results-dir outputs/comparison`. The
script computes pairwise weighted-delta winners over the first 4 outcomes
rows. A second invocation with the mixed 4-row file produces the
robot-vs-human leaderboard. Robot wins all 4 robot-vs-human rounds with
confidence 0.955 to 1.000. The structural-time-dimension caveat is preserved
in every round rationale.

## Step 7 - ASCII diagrams and tables

Curated 6 ASCII diagrams plus a per-iteration composite-score markdown
table. The diagrams summarize the pipeline architecture, 4-arm coordination
heartbeat, 60-second phase timeline, file size pyramid, composite formula
plus aggregates, and the on-prem LLM control loop instantiating the thesis.

## Step 8 - Visualization renders

Generated 4 ASCII bar / histogram charts: composite per iteration, composite
histogram (robot vs human), per-arm resection mean (mm^3), and wall-clock
per iteration. The upstream Plotly HTML dashboard and the static PNG charts
are mirrored from the upstream `viz/` folder; PNG bytes are placeholder
because matplotlib is not present in the sandbox.

## Step 9 - Outputs README

Composed the publication-grade README with DOI plus CI plus license badges,
the thesis block, the full repository structure, the pipeline architecture
ASCII, the 4-arm coordination ASCII, the robot-vs-human aggregate table, the
mixed tournament leaderboard, the citation block, and the license pointer.

## Step 10 - Consolidated reports

Collected the run summary, the process log (this document), the final
narrative report, and the limitations log under `outputs/reports/`.

## Step 11 - Lint and CI fix sweep

Ran `ruff format --check 2030-gbm-1min/`, `ruff check 2030-gbm-1min/`, and
`yamllint -d relaxed 2030-gbm-1min/config/` against the full directory and
fixed any offenders. Confirmed the file size cap step passes.

## Step 12 - Repository-wide v0.2.0 update

Updated the top-level main README (repository structure plus diagrams to
include the new outputs tree), appended the v0.2.0 block to releases.md
following the supplied format, and appended the v0.2.0 block to CHANGELOG.md.
