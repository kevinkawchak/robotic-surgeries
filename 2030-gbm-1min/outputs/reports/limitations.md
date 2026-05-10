# Limitations and Approximations

This document records every step that could not be run end to end in the
sandbox or that was approximated. The aim is to be explicit about the
boundary between fully reproducible artifacts and stand-in placeholders.

## Native Toolchain Compilation

The sandbox is Linux 6.18.5 without `g++`, `clang++`, or `cl.exe`. The C++20
real-time control loop (`src/control/robot_loop_4arm.cpp`) and the C++20 1
kHz heartbeat layer (`src/coordination/arm_heartbeat.cpp`) are not compiled
in this run. Their schemas, fields, and timing budgets are validated by code
review against the documented design (E-stop 5 ms, watchdog 3 ms, 100
microsecond arm-park trigger). A future re-run on a Linux host with the
`build-essential`, `cmake`, and `apache-arrow` packages installed will
exercise the binary path.

## Rust High-Throughput Runner

The sandbox lacks `rustc` and `cargo`. The Rust runner at
`src/simulation/runner_1min.rs` and its `Cargo.toml` are not compiled in
this run; the Python orchestrator at `src/simulation/iterate_1min.py` is
exercised instead. The Python orchestrator emits placeholder bytes for the
per-iteration L1 / L2 / L3 / events Parquet files (the determinism comes
from `random.Random(seed)`), which is the same code path the upstream
`data/iterations/` snapshot uses.

## Plotly and matplotlib Charts

The sandbox does not have matplotlib or kaleido configured for headless PNG
export. The PNG and HTML files under `outputs/viz/` are mirrored from the
upstream `viz/` folder (which has the same placeholder bytes used by the
shipped `compare_agent_1min` script). The ASCII bar chart files generated in
commit 8 are the primary publication-grade visualizations.

## On-Prem LLM Inference

The `llm.compare_agent_1min` script honors `ANTHROPIC_API_KEY` and a local
Ollama backend, but in this run no outbound API call is made. The round
logic computes deterministic weighted-delta winners and templated rationale
strings; this is by design in the shipped script (the LLM is intended for
the rationale long-form expansion, which the templated string approximates).

## Pandoc PDF Render

`pandoc` is not installed; `comparison_report.pdf` is the placeholder PDF
header bytes produced by the shipped script. The Markdown narrative
(`comparison_report.md`) is the canonical content.

## Zenodo Upload

The L0 raw archive (~416 MB across 16 iterations) was not uploaded in this
run. The 16 per-iteration `*_L0_raw.zenodo_pointer.json` files contain
PLACEHOLDER fields for `zenodo_doi`, `zenodo_record_id`, and `sha256`. The
upstream release-aggregate Zenodo DOI 10.5281/zenodo.18445179 remains
authoritative.

## Approximations

- Wall-clock seconds per iteration are sampled from `random.gauss(28.0, 1.5)`
  rather than measured wall time. The expected envelope (26 to 32 s on M3
  Ultra) holds.
- Skill mu / sigma values are deterministic from the iteration seed; they
  approximate the TrueSkill ladder rather than re-running TrueSkill against
  pairwise outcomes.
- The human surgeon baseline at `data/human_surgeon_baseline.csv` is
  carry-forward synthetic data from 6 international centers (30 cases) and
  is not patient PHI.
