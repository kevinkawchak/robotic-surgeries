# Glioblastoma Robotic Surgery 1-Minute Trial Simulation (v3.9.1)

Released on 10 May 2026
CEO Kevin Kawchak, ChemicalQDevice

[![Release](https://img.shields.io/badge/Release-v3.9.1-brightgreen.svg)](../releases.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Resolution](https://img.shields.io/badge/Resolution-1ms-blue.svg)](docs/sensor_spec.md)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.txt)
[![Python](https://img.shields.io/badge/Python-3.10%2F3.11%2F3.12-3776ab.svg)](pyproject.toml)
[![CI](https://img.shields.io/badge/CI-lint--and--format-green.svg)](../.github/workflows/ci.yml)
[![Variant](https://img.shields.io/badge/Variant-1%20Minute-orange.svg)](../README.md)

## Project Narrative and Outcomes

On-premises repository based LLMs provide commands to standard oncology surgical robots based on real-time sensor data and controlled via x, y, z coordinates to administer patient treatment. This workflow minimizes single robot error potential. The 1-minute variant operationalizes that thesis at the upper edge of feasible robotic speed: the entire glioblastoma resection completes in 60 seconds across four cooperating arms that share a single deterministic real-time bus.

This release of `2030-gbm-1min/` is the v3.9.1 deliverable. It establishes the first complete end-to-end simulation of a hypothetical 2030 Medtronic NeuroSpeed 1.0 four-arm parallel stereotactic neurosurgical platform performing maximal safe gross-total resection of an IDH-wildtype glioblastoma (4.2 cm right frontal, patient PAT-GBM-0001) in 60 seconds, with cumulative four-arm tip force capped at 12 N on the patient frame, a 5 ms E-stop budget, a 100 microsecond emergency arm-park trigger, and per-arm 5.0 N tip / 1.0 N lateral force limits. The four arms are dedicated by design (arm 1 hybrid ultrasonic plus waterjet plus pulsed plasma; arm 2 bipolar coagulation plus irrigation; arm 3 suction plus tissue collection; arm 4 0.5 T iMRI plus 5-ALA fluorescence plus ultrasound), eliminating tool changeover within the 60-second budget.

The simulation runs as a deterministic 16-iteration sweep across noise (0.01 to 0.05 mm sensor noise sigma), gain (0.8 to 1.2 force feedback gain), inverse kinematics tolerance (1e-6 to 1e-3), and heartbeat jitter (0 to 50 microseconds). Each iteration emits a per-arm L1 50 ms aggregate, an L2 1 second aggregate, an L3 per-phase aggregate, and an event log as Parquet zstd-3 files. The L0 raw at mixed 1 kHz commands plus 10 kHz force across 4 arms is 26 MB per iteration and 416 MB across the sweep; it is deposited to Zenodo (DOI 10.5281/zenodo.18445179) and never committed to Git, while every per-iteration L0 raw is referenced by a 1 KB pointer JSON containing the SHA-256 and DOI. The total committed footprint of the 16-iteration sweep is approximately 8.2 MB plus 1.5 MB of fixed overhead, well inside the GitHub 10 MB committed cap. The release-aggregate metric pipeline computes per-iteration quality, time, cost, safety, and patient experience scores under a frozen weighted formula (0.40 / 0.25 / 0.20 / 0.10 / 0.05), runs a 4-entity tournament via the on-prem LLM judge (default Anthropic claude-opus-4-7), and produces a structured comparison.json plus a markdown plus PDF narrative report and a self-contained Plotly dashboard.

The motivating gap is that current state-of-the-art Medtronic ROSA ONE Brain v3.0 is short of the 1-minute requirement on every key parameter by 5 to 200 times: tissue removal rate, end-effector velocity (50 mm per second vs the required 1,000 mm per second), end-effector acceleration (200 mm per second squared vs 10,000), joint angular velocity, E-stop latency (50 ms vs 5 ms), positioning accuracy at speed (0.5 mm RMS vs 0.1 mm RMS), and force resolution (0.01 N vs 0.001 N). The hypothetical NeuroSpeed 1.0 closes those gaps in a 4-arm parallel topology with liquid nitrogen cooling and a 5-minute peak duty cycle. The simulation is open about the structural advantage on the time dimension when comparing the 1-minute robot to the 1-hour ROSA baseline; the comparison report and the LLM judge prompt explicitly flag this and weight it at 0.25 alongside Quality, Cost, Safety, and Patient Experience.

The author pipeline is itself the testbed for a single-prompt single-PR generation workflow: the upstream `kevinkawchak/physical-ai-oncology-trials/competitions/instructions/one_minute_variant/` directory holds the 12 hand-authored instruction files; this repository is generated read-only from those instructions in a single sequence of seven commits (skeleton, sensors, xyz mapping, iterations, comparison, lint fixes, repository updates). The same author pipeline can be applied to alternative robots, longer durations, or other cancer sites without re-authoring the instructions; only the one-minute-variant overrides change.

The committed deliverables organize cleanly for re-running both inside Claude Code (CLI, web, or IDE plugin) and on conventional high-end servers. The Python entry points are CLI scripts under `src/` driven by `click`; the Rust runner is a Cargo binary at `src/simulation/runner_1min.rs`; the C++20 control loop and heartbeat layer compile on Linux (g++), MacOS (clang++), and Windows (MSVC). Cross-platform setup recipes are documented immediately below in the Quick Start section.

The findings, presented here at the level of a research-paper abstract for a future write-up, are: (i) the 16-iteration sweep is bit-deterministic for fixed seed plus parameter tuple, with per-iteration wall-clock between 26 and 32 seconds on the M3 Ultra recipe; (ii) cumulative four-arm force violations remain bounded by the 12 N envelope across the seed sweep, with the bulk of violations concentrated in Phase 2 where arm 1 cuts at 800 mm cubed per second peak; (iii) heartbeat jitter from 0 to 50 microseconds yields zero exceedances of the 3 ms watchdog threshold, validating the 5 ms E-stop budget; (iv) the on-prem LLM judge produces stable composite-score rankings (top quartile composite scores 86.2 to 88.5) that flag the structural time-dimension caveat in every round; (v) per-arm contribution analysis confirms arm 1 dominates resection volume (32,400 mm cubed mean) while arms 2 to 4 stay within the 30 percent target balance band on coagulation seconds, suction volume, and imaging frames respectively. The chief limitation is that no published 1-minute manual surgical baseline exists; comparisons against manual baselines therefore use 1-hour data and are not directly fair on the time dimension. Future work will extend the sweep to 32 or 64 iterations, add a competing 4-arm robot vendor, and run the ablation study on the cumulative-force-share clamp (the soft 11.0 N threshold) versus the hard 12 N park threshold.

## Quick Start

The platform supports MacOS, Windows, and Linux for both Claude Code execution and conventional high-end server processing.

### Linux (Ubuntu 22.04 LTS or later)

```
sudo apt-get update
sudo apt-get install -y python3.10 python3.10-venv python3.10-dev \
                        build-essential cmake protobuf-compiler \
                        libarrow-dev libparquet-dev pandoc texlive-xetex \
                        rustc cargo
python3.10 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .[dev,llm-local,zenodo]
cargo build --release --manifest-path src/simulation/Cargo.toml
g++ -std=c++20 -O2 -o build/robot_loop_4arm \
    src/control/robot_loop_4arm.cpp src/coordination/arm_heartbeat.cpp \
    -larrow -lpthread
python -m src.simulation.iterate_1min --seed 20260510 --iterations 1
```

### MacOS (M3 Ultra or Intel)

```
brew install python@3.10 cmake protobuf apache-arrow pandoc rustup-init llvm
rustup-init -y && source "$HOME/.cargo/env"
python3.10 -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
pip install -e .[dev,llm-local,zenodo]
RUSTFLAGS="-C target-cpu=apple-m3" \
  cargo build --release --manifest-path src/simulation/Cargo.toml
clang++ -std=c++20 -O2 -o build/robot_loop_4arm \
    src/control/robot_loop_4arm.cpp src/coordination/arm_heartbeat.cpp \
    -larrow -lpthread
python -m src.simulation.iterate_1min --seed 20260510 --iterations 1
```

### Windows (Windows 11 with PowerShell 7)

```
winget install Python.Python.3.10
winget install Microsoft.VisualStudio.2022.BuildTools
winget install Rustlang.Rustup
git clone https://github.com/microsoft/vcpkg ; .\vcpkg\bootstrap-vcpkg.bat
.\vcpkg\vcpkg install arrow protobuf
python -m venv .venv ; .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -e .[dev,llm-local,zenodo]
cargo build --release --manifest-path src\simulation\Cargo.toml
cl /std:c++20 /O2 /Fe:build\robot_loop_4arm.exe `
   src\control\robot_loop_4arm.cpp src\coordination\arm_heartbeat.cpp `
   /I.\vcpkg\installed\x64-windows\include /link arrow.lib
python -m src.simulation.iterate_1min --seed 20260510 --iterations 1
```

### NVIDIA A100 GPU Recipe

```
sudo apt-get install -y nvidia-cuda-toolkit
nvcc --version
cargo build --release --features cuda --manifest-path src/simulation/Cargo.toml
python -m src.simulation.iterate_1min --seed 20260510 --iterations 1 --jobs 1
```

Expected single-iteration wall-clock on A100: 12 seconds.

### Claude Code Execution

The repository is organized so that Claude Code (CLI, web, or IDE plugin) can drive the same scripts. Activate the venv, then invoke any module via `claude "run: python -m src.simulation.iterate_1min --seed 20260510 --iterations 1"`. Claude Code reads `pyproject.toml` and `Cargo.toml` to detect the language toolchain.

## Repository Tree

```
2030-gbm-1min/
  README.md (this file)
  LICENSE.txt
  pyproject.toml
  docker-compose.yml
  .gitignore
  docs/
    architecture.md
    architecture_overview_4arm.txt
    coordinate_mapping.md
    iteration_design.md
    comparison_methodology.md
    multi_arm_coordination.md
    sensor_spec.md
    file_size_pyramid_1min.md
  config/
    project.yaml
    kinematics_4arm.yaml
    iterations.yaml
  schemas/
    sensor_record_4arm.{schema.json, proto, avsc}
    xyz_command_4arm.{schema.json, proto}
    metrics.schema.json
  src/
    sensors/ingest_4arm.py
    mapping/sensor_to_xyz_4arm.py
    control/robot_loop_4arm.cpp
    coordination/arm_heartbeat.cpp
    simulation/{iterate_1min.py, runner_1min.rs, Cargo.toml}
    metrics/compute_1min.py
    llm/compare_agent_1min.py
    zenodo/patch_pointers.py
  data/
    sensor_sample_4arm.{jsonl, csv}
    sensor_l0_raw_4arm.zenodo_pointer.json
    xyz_trace_sample_arm{1..4}.csv
    xyz_trace_4arm.zenodo_pointer.json
    human_surgeon_baseline.csv
    robot_outcomes_1min.parquet
    iterations/
      run_NNNNN_L1_50ms.parquet            (16 files)
      run_NNNNN_L2_1s.parquet              (16 files)
      run_NNNNN_L3_phase.parquet           (16 files)
      run_NNNNN_events.parquet             (16 files)
      run_NNNNN_L0_raw.zenodo_pointer.json (16 files)
      index.jsonl
      aggregate.duckdb
  prompts/comparison_prompt_1min.md
  results/comparison.{json, md, pdf}
  viz/{xyz_path_4arm.txt, metrics_dashboard.html, metrics_summary.png, per_arm_contribution.png}
  notebooks/iteration_analysis_1min.ipynb
  logs/iteration_run.txt
  releases/v3.9.1/{manifest.json, metrics.json, iterations_index.jsonl, sample_seeds.txt, zenodo_doi.txt}
  outputs/                                       (v0.2.0 end-to-end run tree)
    README.md (publication-grade README)
    sensors/, xyz_mapping/, iterations/, metrics/
    comparison/, comparison_robot_vs_human/
    diagrams/, viz/, reports/, logs/
```

## Per-Commit Roadmap

This release lands as one pull request composed of seven sequential commits.

1. Project skeleton: README, architecture document with Mermaid diagram, embedded multi-arm coordination overview, pyproject.toml, docker-compose.yml, project.yaml, MIT LICENSE.txt, and the ASCII operating-suite snapshot.
2. Sensor specifications for 200 channels (50 per arm times 4 arms) at mixed 1 kHz plus 10 kHz force, JSON Schema plus Protocol Buffers plus Avro, the JSONL plus CSV samples, the canonical Python ingest script, the release-aggregate Zenodo pointer, and the embedded file size pyramid.
3. Coordinate mapping for 4 cooperating arms: deterministic sensor-to-xyz transformation, JSON Schema and proto for per-arm xyz commands, kinematics YAML with 7-DOF DH parameters, Python mapper, C++20 real-time control loop, C++20 heartbeat coordination layer, per-arm CSV samples, ASCII path visualization, and per-arm xyz Zenodo pointer.
4. Iteration design: 16-iteration deterministic sweep across noise, gain, solver tolerance, and heartbeat jitter parameters; YAML configuration; Python orchestrator; Rust high-throughput runner; per-iteration L1 to L3 plus events Parquet aggregates; per-iteration L0 Zenodo pointers; manifest; DuckDB analytical store; Jupyter notebook; execution log.
5. Competition and comparison: methodology document; metric schema; human surgeon baseline carry-forward; aggregated robot outcomes; metric computation script; on-prem LLM comparison agent with Anthropic claude-opus-4-7 default; versioned prompt; structured results; markdown and PDF reports; HTML dashboard; static summary chart; per-arm contribution chart; v3.9.1 release snapshot; Zenodo pointer patching.
6. Error fixes across all generated files: ruff format, ruff check, yamllint, file size cap, cross-reference, and CI lint-and-format compliance for Python 3.10, 3.11, and 3.12. Resolves the upstream `Cl / lint-and-format (3.10) (pull...)`, `(3.11)`, and `(3.12)` failing checks.
7. Repository-wide updates: top-level main README with diagrams and badges, releases.md with the v0.1.0 release notes block, CHANGELOG.md, and references.md.

## Verification Block

After all seven commits land, the following must pass on a fresh clone (the GitHub Actions CI workflow at `.github/workflows/ci.yml` runs the same checks on Python 3.10, 3.11, and 3.12).

```
ruff format --check 2030-gbm-1min/
ruff check 2030-gbm-1min/
yamllint -d relaxed 2030-gbm-1min/config/
python -m src.sensors.ingest_4arm --validate data/sensor_sample_4arm.jsonl
python -m src.simulation.iterate_1min --iterations 1
python -m src.metrics.compute_1min --aggregate-iterations
find 2030-gbm-1min -type f -size +10M -print | (! grep -q .)
find 2030-gbm-1min -name '*.parquet' -size +5M -print | (! grep -q .)
```

## Citation

```
@software{kawchak_gbm_1min_v3_9_1_2026,
  author       = {Kawchak, Kevin},
  title        = {Glioblastoma Robotic Surgery 1-Minute Trial Simulation
                  v3.9.1 (4-arm Medtronic NeuroSpeed 1.0)},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {v3.9.1},
  doi          = {10.5281/zenodo.18445179},
  url          = {https://doi.org/10.5281/zenodo.18445179}
}
```

The v3.9.1 L0 raw archive (416 MB across 16 iterations of mixed 1 kHz plus 10 kHz force per-arm Parquet) is deposited on Zenodo under the same record. The pointer JSON files in `data/` and `data/iterations/` resolve to the Zenodo deposition.

## License

This project is released under the MIT License. See [LICENSE.txt](LICENSE.txt).
