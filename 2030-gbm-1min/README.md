# Glioblastoma Robotic Surgery 1-Minute Trial Simulation (v3.9.1)

Released on 10 May 2026
CEO Kevin Kawchak, ChemicalQDevice

[![Release](https://img.shields.io/badge/Release-v3.9.1-brightgreen.svg)](https://github.com/kevinkawchak/robotic-surgeries)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Resolution](https://img.shields.io/badge/Resolution-1ms-blue.svg)](https://github.com/kevinkawchak/robotic-surgeries)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.txt)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776ab.svg)](pyproject.toml)
[![Variant](https://img.shields.io/badge/Variant-1%20Minute-orange.svg)](https://github.com/kevinkawchak/robotic-surgeries/tree/main/2030-gbm-1min)

## Project Narrative

On-premises repository based LLMs provide commands to standard oncology surgical robots based on real-time sensor data and controlled via x, y, z coordinates to administer patient treatment. This workflow minimizes single robot error potential. The 1-minute variant operationalizes that thesis at the upper edge of feasible robotic speed: the entire glioblastoma resection completes in 60 seconds across four cooperating arms that share a single deterministic real-time bus.

- Patient: PAT-GBM-0001 (62-year-old female, IDH-wildtype glioblastoma WHO grade 4, right frontal lobe, 4.2 cm maximum diameter).
- Procedure: stereotactic-guided open craniotomy with maximal safe resection completed in 60 seconds. Pre-op anesthesia, registration, dural opening, and multi-arm setup are precomputed and frozen at simulation start.
- Robot: hypothetical 2030 Medtronic NeuroSpeed 1.0 multi-arm parallel stereotactic neurosurgical robot. Four cooperating 7-DOF arms coordinated at a 1 kHz heartbeat with a 5 ms E-stop latency budget.
- Resolution: mixed 1 kHz commands plus 10 kHz force per arm. Total channel count is 200 (50 channels per arm times 4 arms).
- Duration: 60 seconds across 4 phases (60,000 mixed ticks plus 540,000 force-only ticks per arm).
- Iterations: 16 deterministic iterations per benchmarked configuration with a per-iteration committed footprint of approximately 510 KB.

## Quick Start

The platform supports MacOS, Windows, and Linux for both Claude Code execution and conventional high-end server processing. Each runtime is documented in detail below; this Quick Start covers the common path on each platform.

### Linux (Ubuntu 22.04 LTS or later)

```
# 1. System packages
sudo apt-get update
sudo apt-get install -y python3.10 python3.10-venv python3.10-dev \
                        build-essential cmake protobuf-compiler \
                        libarrow-dev libparquet-dev pandoc texlive-xetex \
                        rustc cargo

# 2. Python environment
python3.10 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .[dev,llm-local,zenodo]

# 3. Build native components
cargo build --release --manifest-path src/simulation/Cargo.toml
g++ -std=c++20 -O2 -o build/robot_loop_4arm \
    src/control/robot_loop_4arm.cpp src/coordination/arm_heartbeat.cpp \
    -larrow -lpthread

# 4. Run a single iteration smoke test
python -m src.simulation.iterate_1min --seed 20260510 --iterations 1
```

### MacOS (M3 Ultra or Intel)

```
# 1. Homebrew packages
brew install python@3.10 cmake protobuf apache-arrow pandoc rustup-init llvm
rustup-init -y
source "$HOME/.cargo/env"

# 2. Python environment
python3.10 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .[dev,llm-local,zenodo]

# 3. Build native components with M3 optimizations
RUSTFLAGS="-C target-cpu=apple-m3" \
  cargo build --release --manifest-path src/simulation/Cargo.toml
clang++ -std=c++20 -O2 -o build/robot_loop_4arm \
    src/control/robot_loop_4arm.cpp src/coordination/arm_heartbeat.cpp \
    -larrow -lpthread

# 4. Run a single iteration smoke test (under 30 s wall-clock on M3 Ultra)
python -m src.simulation.iterate_1min --seed 20260510 --iterations 1
```

### Windows (Windows 11 with PowerShell 7)

```
# 1. Install Python 3.10, Visual Studio Build Tools 2022, Rustup, vcpkg
winget install Python.Python.3.10
winget install Microsoft.VisualStudio.2022.BuildTools
winget install Rustlang.Rustup
git clone https://github.com/microsoft/vcpkg ; .\vcpkg\bootstrap-vcpkg.bat
.\vcpkg\vcpkg install arrow protobuf

# 2. Python environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -e .[dev,llm-local,zenodo]

# 3. Build native components
cargo build --release --manifest-path src\simulation\Cargo.toml
cl /std:c++20 /O2 /Fe:build\robot_loop_4arm.exe `
   src\control\robot_loop_4arm.cpp src\coordination\arm_heartbeat.cpp `
   /I.\vcpkg\installed\x64-windows\include /link arrow.lib

# 4. Run a single iteration smoke test
python -m src.simulation.iterate_1min --seed 20260510 --iterations 1
```

### NVIDIA A100 GPU Recipe

The 4-arm 10 kHz force physics simulator benefits from GPU acceleration on the per-arm finite-element tissue model. The Rust runner exposes an optional CUDA path gated by the `cuda` feature flag.

```
sudo apt-get install -y nvidia-cuda-toolkit
nvcc --version
cargo build --release --features cuda --manifest-path src/simulation/Cargo.toml
python -m src.simulation.iterate_1min --seed 20260510 --iterations 1 --jobs 1
```

Expected single-iteration wall-clock on A100: 12 seconds.

### Claude Code Execution

The repository is organized so that Claude Code (CLI, web, or IDE plugin) can drive the same scripts. Activate the venv, then invoke any module via:

```
claude "run: python -m src.simulation.iterate_1min --seed 20260510 --iterations 1"
```

Claude Code reads the `pyproject.toml` and `Cargo.toml` files to detect the language toolchain. The session-start hook in `.claude/settings.json` installs missing dependencies on the first session of each cloned environment.

## Repository Tree

```
2030-gbm-1min/
  README.md
  LICENSE.txt
  pyproject.toml
  docker-compose.yml
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
    sensor_record_4arm.schema.json
    sensor_record_4arm.proto
    sensor_record_4arm.avsc
    xyz_command_4arm.schema.json
    xyz_command_4arm.proto
    metrics.schema.json
  src/
    sensors/ingest_4arm.py
    mapping/sensor_to_xyz_4arm.py
    control/robot_loop_4arm.cpp
    coordination/arm_heartbeat.cpp
    simulation/iterate_1min.py
    simulation/runner_1min.rs
    simulation/Cargo.toml
    metrics/compute_1min.py
    llm/compare_agent_1min.py
    zenodo/patch_pointers.py
  data/
    sensor_sample_4arm.jsonl
    sensor_sample_4arm.csv
    sensor_l0_raw_4arm.zenodo_pointer.json
    xyz_trace_sample_arm1.csv
    xyz_trace_sample_arm2.csv
    xyz_trace_sample_arm3.csv
    xyz_trace_sample_arm4.csv
    xyz_trace_4arm.zenodo_pointer.json
    human_surgeon_baseline.csv
    robot_outcomes_1min.parquet
    iterations/
      run_NNNNN_L1_50ms.parquet
      run_NNNNN_L2_1s.parquet
      run_NNNNN_L3_phase.parquet
      run_NNNNN_events.parquet
      run_NNNNN_L0_raw.zenodo_pointer.json
      index.jsonl
      aggregate.duckdb
  prompts/
    comparison_prompt_1min.md
  results/
    comparison.json
    comparison_report.md
    comparison_report.pdf
  viz/
    xyz_path_4arm.txt
    metrics_dashboard.html
    metrics_summary.png
    per_arm_contribution.png
  notebooks/
    iteration_analysis_1min.ipynb
  logs/
    iteration_run.txt
  releases/v3.9.1/
    manifest.json
    metrics.json
    iterations_index.jsonl
    sample_seeds.txt
    zenodo_doi.txt
```

## Per-Commit Roadmap

The v3.9.1 release lands as one pull request composed of seven sequential commits.

1. Project skeleton: README, architecture document with Mermaid diagram, embedded multi-arm coordination overview, pyproject.toml, docker-compose.yml, project.yaml, MIT LICENSE.txt, and the ASCII operating-suite snapshot.
2. Sensor specifications for 200 channels (50 per arm times 4 arms) at mixed 1 kHz plus 10 kHz force, JSON Schema plus Protocol Buffers plus Avro, the 1,000 record JSONL and CSV samples, the canonical Python ingest script, the release-aggregate Zenodo pointer, and the embedded file size pyramid.
3. Coordinate mapping for 4 cooperating arms: deterministic sensor-to-xyz transformation, JSON Schema and proto for per-arm xyz commands, kinematics YAML with 7-DOF DH parameters, Python mapper, C++20 real-time control loop, C++20 heartbeat coordination layer, per-arm CSV samples, ASCII path visualization, and the per-arm xyz Zenodo pointer.
4. Iteration design: 16-iteration deterministic sweep across noise, gain, solver tolerance, and heartbeat jitter parameters; YAML configuration; Python orchestrator; Rust high-throughput runner; per-iteration L1 to L3 plus events Parquet aggregates; per-iteration L0 Zenodo pointers; manifest; DuckDB analytical store; Jupyter notebook; execution log.
5. Competition and comparison: methodology document; metric schema; human surgeon baseline carry-forward; aggregated robot outcomes; metric computation script; on-prem LLM comparison agent with Anthropic claude-opus-4-7 default; versioned prompt; structured results; markdown and PDF reports; HTML dashboard; static summary chart; per-arm contribution chart; v3.9.1 release snapshot; Zenodo pointer patching.
6. Error fixes across all generated files: ruff format, ruff check, yamllint, file size cap, cross-reference, and CI lint-and-format compliance for Python 3.10, 3.11, and 3.12.
7. Repository-wide updates: top-level README with diagrams and badges, releases.md with the v3.9.1 release notes block, CHANGELOG.md, references.md.

## Verification Block

After all seven commits land, the following must pass on a fresh clone.

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
