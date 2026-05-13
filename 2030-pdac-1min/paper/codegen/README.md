# 2030 PDAC 1 Minute 8 Arm Whipple Codegen (v0.6.0)

Released on 13 May 2026
CEO Kevin Kawchak, ChemicalQDevice

[![Release](https://img.shields.io/badge/Release-v0.6.0-brightgreen.svg)](../../../releases.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Resolution](https://img.shields.io/badge/Resolution-0.01ms-blue.svg)](https://github.com/kevinkawchak/robotic-surgeries)
[![Variant](https://img.shields.io/badge/Variant-1%20Minute-orange.svg)](https://github.com/kevinkawchak/robotic-surgeries/tree/main/2030-pdac-1min)
[![Disease](https://img.shields.io/badge/Disease-PDAC-purple.svg)](https://github.com/kevinkawchak/robotic-surgeries/tree/main/2030-pdac-1min)
[![Adjuvant](https://img.shields.io/badge/Adjuvant-Daraxonrasib-yellow.svg)](https://doi.org/10.5281/zenodo.18099351)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.txt)
[![Python](https://img.shields.io/badge/Python-3.10%2F3.11%2F3.12-3776ab.svg)](pyproject.toml)

This directory contains the v0.6.0 generated codebase produced by Claude Code Opus 4.7 1M Max from the v0.5.0 instruction set at `2030-pdac-1min/paper/instructions/`. The simulation models a 60 second pancreaticoduodenectomy (Whipple procedure) on the hypothetical 2030 Medtronic PancreSpeed 1.0 eight arm parallel coelomic oncology robot at mixed 100 kHz force per arm plus 10 kHz command per arm resolution. The 32 iteration deterministic sweep, the 640 channel sensor stack, the 5 vessel vascular safety zones, the 3 anastomosis protocols, and the Daraxonrasib precision oncology adjuvant integration are all generated under a single pull request across nine sequential commits.

## Thesis

On premises repository based LLMs provide commands to standard oncology surgical robots based on real time sensor data and controlled via x, y, z coordinates to administer patient treatment. This workflow minimizes single robot error potential. The PDAC 1 minute codegen tree operationalizes the thesis for the most technically demanding solid tumor resection in oncological surgery, the pancreaticoduodenectomy, executed in 60 seconds across eight cooperating arms that share a deterministic 10 kHz heartbeat bus. The work positions Daraxonrasib (the pan KRAS inhibitor evaluated in the RASolute 302 and RASolve 301 programs) as the precision oncology adjuvant that the 60 second robotic Whipple pairs with for durable cancer survival.

## Why a New Standard of Care

Pancreatic ductal adenocarcinoma is the third leading cause of cancer death in the United States and the fourth in the European Union, with five year overall survival below 13 percent and a 2025 Dutch nationwide cohort 1000 robotic pancreaticoduodenectomy mean ideal outcome rate of 47 percent. The PDAC 1 minute codegen tree targets a future standard of care in which the eight arm PancreSpeed 1.0 platform reduces the conversion rate to 0 percent in simulation, the grade B/C postoperative pancreatic fistula rate to under 5 percent in simulation, and the 90 day mortality to under 0.5 percent in simulation, with the structural caveat that simulation against simulation is held against the 2025 Dutch cohort numbers as the human baseline. The robotic, cartesian, iteration, and competition pipelines codified in this directory are intended for real world application alongside Daraxonrasib (if approved) and advanced AI surgical robots in the late 2020s and early 2030s.

## Project Scope

- One simulated patient: PAT-PDAC-0001 (68 year old male, head of pancreas PDAC, 3.4 cm tumor abutting the superior mesenteric vein at 75 degrees, KRAS G12D mutant, MSI stable, CA 19 9 of 412 U/mL at diagnosis, ECOG 1, neoadjuvant modified FOLFIRINOX times 4 cycles completed, Daraxonrasib eligible per the RASolute 302 broad pan KRAS criteria).
- One surgical procedure: classic pancreaticoduodenectomy with pylorus preservation, with portomesenteric venous resection as needed, with artery first uncinate dissection, with pancreaticojejunostomy and hepaticojejunostomy and gastrojejunostomy reconstruction.
- One simulation duration: 60 seconds (600,000 ticks at 10 kHz command channels and 6,000,000 ticks at 100 kHz force channels per arm).
- One primary surgical robot: hypothetical 2030 Medtronic PancreSpeed 1.0 eight arm parallel coelomic oncology robot.
- One sensor stack: mixed 100 kHz force channels and 10 kHz other channels per arm.
- One channel schema: 80 channels per arm times 8 arms equals 640 total channels.
- One iteration count: 32 deterministic iterations per benchmarked configuration with seed 20260513.
- One competition: this project's PancreSpeed 1.0 run versus three competitor robotic platforms (hypothetical 2030 Intuitive da Vinci Whipple successor, hypothetical 2030 Medtronic Hugo PDAC successor, Dutch human surgeon baseline).

## Nine Commit Plan (Single PR)

| Commit | Focus | Files emitted |
|--------|-------|----------------|
| 1 | Project skeleton and docs | README.md, LICENSE.txt, pyproject.toml, docker-compose.yml, .gitignore, docs/, config/project.yaml |
| 2 | Sensors | schemas/sensor_record_8arm.*, src/sensors/ingest_8arm.py, data/sensor_sample_8arm.*, outputs/sensors/* |
| 3 | XYZ mapping | schemas/xyz_command_8arm.*, src/mapping/sensor_to_xyz_8arm.py, config/kinematics_8arm.yaml, src/control/, src/coordination/ |
| 4 | Iterations | src/simulation/iterate_1min.py, src/simulation/runner_1min.rs, config/iterations.yaml, src/metrics/, data/iterations/ |
| 5 | Competition | src/llm/compare_agent_1min.py, prompts/comparison_prompt_1min.md, results/comparison.json, outputs/comparison/ |
| 6 | Vascular safety plus anastomoses | src/vascular/, src/anastomosis/, config/vascular_safety_zones.yaml, config/anastomosis_targets.yaml |
| 7 | Daraxonrasib plus Zenodo plus viz plus notebooks | src/daraxonrasib/, src/zenodo/, viz/, notebooks/, outputs/diagrams/ |
| 8 (2nd to last) | Error fixes | lint and format fixes; cross commit cross reference fixes |
| 9 (last) | Repository updates | top level README, releases.md v0.6.0, CHANGELOG.md v0.6.0 |

## Repository Tree (Generated)

```
2030-pdac-1min/paper/codegen/
  README.md                       # this file
  LICENSE.txt                     # MIT 2026 Kevin Kawchak
  pyproject.toml                  # Python project plus lint config
  docker-compose.yml              # Python + Rust + DuckDB services
  .gitignore                      # Python + Rust + Jupyter + macOS
  config/
    project.yaml                  # frozen project parameters
    kinematics_8arm.yaml          # per arm 7 DOF DH parameters
    iterations.yaml               # 32 iteration Latin hypercube design
    vascular_safety_zones.yaml    # 5 named vessel safety zones
    anastomosis_targets.yaml      # 3 anastomosis ring tension targets
  docs/
    architecture_8arm.md          # 8 arm overview
    sensor_spec_640ch.md          # 640 channel sensor stack
    coordinate_mapping_8arm.md    # per arm xyz mapping
    iteration_design_32.md        # 32 iteration sweep design
    comparison_methodology_4vendor.md  # 4 entrant tournament
    multi_arm_coordination_8arm.md     # 10 kHz heartbeat bus
    vascular_safety_protocol.md   # 5 vessel zones
    anastomosis_protocols.md      # 3 anastomoses
    daraxonrasib_integration.md   # perioperative trajectory
  schemas/
    sensor_record_8arm.schema.json
    sensor_record_8arm.proto
    sensor_record_8arm.avsc
    xyz_command_8arm.schema.json
    xyz_command_8arm.proto
    metrics.schema.json
    anastomosis_event.schema.json
    daraxonrasib_event.schema.json
  src/
    sensors/                       # 640 channel ingest pipeline
    mapping/                       # sensor to xyz Cartesian command mapping
    control/                       # per arm robot control loop (C++)
    coordination/                  # 10 kHz heartbeat (C++) plus collision avoidance
    vascular/                      # safety zone gate at 10 kHz
    anastomosis/                   # 3 per anastomosis controllers
    daraxonrasib/                  # trajectory plus LLM advisory
    simulation/                    # per iteration sweep runner (Python + Rust)
    metrics/                       # 6 component composite score
    llm/                           # 4 entrant tournament agent
    zenodo/                        # L0 raw pointer patcher
  data/
    sensor_sample_8arm.jsonl       # publication arm slice
    sensor_sample_8arm.csv         # human review slice
    xyz_command_sample_8arm.jsonl  # publication arm xyz command slice
    human_surgeon_baseline.csv     # 2025 Dutch cohort summary
    robot_outcomes_1min.csv        # cross iteration per entrant outcomes
    iterations/
      index.jsonl                  # one row per iteration with seed + composite
      run_00000_L2_1s.csv          # sample iteration L2 (human review)
      run_00000_L3_phase.csv       # sample iteration L3 (human review)
      run_00000_L4_anastomosis.csv # sample iteration L4 (human review)
      run_00000_events.csv         # sample iteration event log
      run_00000_daraxonrasib.csv   # sample iteration Daraxonrasib trajectory
      run_00000_L0_raw.zenodo_pointer.json  # DOI + SHA 256 manifest
  prompts/
    comparison_prompt_1min.md      # 4 entrant tournament prompt
    daraxonrasib_advisory_prompt.md  # postop Daraxonrasib restart prompt
  results/
    comparison.json                # 32 iteration cross entrant verdicts
    comparison_report.md           # cross iteration leaderboard
    daraxonrasib_advisory.json     # per iteration postop advisory
  viz/
    xyz_path_8arm.txt              # ASCII tip path projection
    metrics_summary_ascii.txt      # leaderboard ASCII summary
    vascular_safety_heatmap_ascii.txt # vessel proximity heatmap
  outputs/
    sensors/                       # publication grade sensor sample
    xyz_mapping/                   # publication grade xyz command sample
    iterations/                    # cross iteration aggregate output
    metrics/                       # composite score breakdown
    comparison/                    # 4 entrant cross iteration leaderboard
    comparison_robot_vs_human/     # Round 3 robot vs human leaderboard
    vascular/                      # vessel proximity events
    anastomosis/                   # per anastomosis event log
    daraxonrasib/                  # per iteration trajectory and advisory
    diagrams/                      # 12 PDAC specific ASCII diagrams
    logs/                          # per script log files
  notebooks/
    iteration_analysis_1min.ipynb  # 32 iteration cross arm analysis
    anastomosis_analysis.ipynb     # 3 anastomosis outcome analysis
    daraxonrasib_pk_analysis.ipynb # Daraxonrasib perioperative PK analysis
```

## Quick Start (Cross Platform)

### MacOS Apple Silicon Recipe

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python@3.12 git rustup duckdb
rustup install stable && rustup default stable
git clone https://github.com/kevinkawchak/robotic-surgeries.git
cd robotic-surgeries/2030-pdac-1min/paper/codegen
python3.12 -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
pip install -e .[dev,llm-local,zenodo,pdac]
python -m src.simulation.iterate_1min --seed 20260513 --iterations 1
python -m src.simulation.iterate_1min --seed 20260513 --iterations 32
```

### Windows 11 Recipe (PowerShell)

```powershell
winget install Python.Python.3.12
winget install Git.Git
winget install Rustlang.Rustup
git clone https://github.com/kevinkawchak/robotic-surgeries.git
cd robotic-surgeries\2030-pdac-1min\paper\codegen
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -e .[dev,llm-local,zenodo,pdac]
python -m src.simulation.iterate_1min --seed 20260513 --iterations 1
```

For the Rust runner on Windows, install WSL2 with `wsl --install -d Ubuntu-24.04` and run `cargo run --release` from inside the WSL2 shell.

### Linux Ubuntu 22.04 LTS Recipe (Server, A100 or H100)

```bash
sudo apt update
sudo apt install -y python3.12 python3.12-venv python3-pip git build-essential pkg-config libssl-dev
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
source $HOME/.cargo/env
git clone https://github.com/kevinkawchak/robotic-surgeries.git
cd robotic-surgeries/2030-pdac-1min/paper/codegen
python3.12 -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
pip install -e .[dev,llm-local,zenodo,pdac]
python -m src.simulation.iterate_1min --seed 20260513 --iterations 32 --device cuda
cd src/simulation && cargo run --release --bin runner_1min -- --seed 20260513 --iterations 32
```

### Claude Code (CLI, Web, IDE)

```bash
npm install -g @anthropic/claude-code
cd robotic-surgeries/2030-pdac-1min/paper/codegen
claude code init
```

Claude Code automatically sets up the Python virtual environment and runs the per iteration sweep on demand. The deterministic seed contract (root_seed = 20260513) yields bit identical Parquet outputs across all five platforms.

## Project Outcomes (What This Tree Produces)

The generated tree at this directory authors the following artifact families. Each artifact family is grounded in a specific instruction file at `2030-pdac-1min/paper/instructions/`:

1. The 640 channel sensor stack at mixed 100 kHz force plus 10 kHz command per arm, codified in `schemas/sensor_record_8arm.{schema.json, proto, avsc}` plus `src/sensors/ingest_8arm.py` plus the publication sample at `outputs/sensors/sensor_sample_8arm.csv` of 81 columns by 1001 rows.
2. The per arm 7 DOF DH parameter kinematics at `config/kinematics_8arm.yaml`, the 7 state per arm command enum schema at `schemas/xyz_command_8arm.{schema.json, proto}`, and the cross arm coordination at `src/coordination/arm_heartbeat_10khz.cpp` and `src/coordination/arm_collision_avoidance.cpp`.
3. The 5 named vessel safety zones (superior mesenteric vein, portal vein, hepatic artery, celiac axis, superior mesenteric artery) at `config/vascular_safety_zones.yaml` plus the gate at `src/vascular/safety_zone_gate.py`.
4. The 3 anastomosis protocols (pancreaticojejunostomy duct to mucosa, hepaticojejunostomy end to side, gastrojejunostomy antecolic) at `config/anastomosis_targets.yaml` plus the three per anastomosis controllers at `src/anastomosis/`.
5. The 32 iteration deterministic Latin hypercube sweep at `config/iterations.yaml` plus the Python runner at `src/simulation/iterate_1min.py` plus the Rust high throughput runner at `src/simulation/runner_1min.rs`.
6. The 6 component frozen composite score at `src/metrics/compute_1min.py` (Quality 0.30, Time 0.20, Cost 0.15, Safety 0.15, Patient experience 0.05, Anastomosis quality 0.15).
7. The 4 entrant multi vendor LLM tournament at `src/llm/compare_agent_1min.py` plus the versioned prompt at `prompts/comparison_prompt_1min.md` plus the cross iteration leaderboard at `results/comparison_report.md`.
8. The Daraxonrasib perioperative pause and restart logic at `src/daraxonrasib/trajectory.py` plus the LLM bound advisory layer at `src/daraxonrasib/advisory.py` plus the versioned advisory prompt at `prompts/daraxonrasib_advisory_prompt.md`.
9. The 12 PDAC specific ASCII diagrams at `outputs/diagrams/` (8 arm coordination heartbeat, vascular safety map, anastomosis target map, per arm tool assignment by phase, per phase activation schedule, per arm 7 DOF kinematic chain, PancreSpeed 1.0 mechanical schematic, iteration parameter space, 4 entrant leaderboard, Daraxonrasib trajectory, fistula risk score flow, 60 second 8 phase timeline).
10. The Zenodo deposition layout for the 13.2 GB L0 raw archive at `src/zenodo/patch_pointers.py` plus the per iteration pointer JSON files plus the cross iteration manifest.

## Differentiators from the v3.9.1 GBM 1 Minute Variant

The PDAC 1 minute codegen tree differs from the v3.9.1 GBM 1 minute variant in seven concrete dimensions. Each differentiator is grounded in PDAC clinical complexity and closes a specific approximation from the v0.4.0 GBM full paper limitations.

1. Eight cooperating arms instead of four (closes the 4 arm only gap; enables concurrent dissection plus three anastomoses plus retraction plus imaging).
2. 100 kHz force sampling instead of 10 kHz (closes the high frequency tip dynamics gap; required for fistula risk score sensitivity).
3. 640 sensor channels instead of 200 (closes the PDAC specific sensing gap; adds NIR indocyanine green, vessel surface proximity, pancreatic duct manometry, anastomosis ring tension, bile spectrophotometry).
4. 32 iterations instead of 16 (closes the cumulative force violation 95 percent CI gap).
5. Four entrant multi vendor tournament from the start (closes the single vendor gap; adds three competitor robots plus the Dutch human surgeon baseline).
6. Daraxonrasib precision oncology adjuvant integration (new; closes the durable survival pairing gap).
7. PDAC specific vascular safety zones and anastomosis protocols (new; closes the vessel and reconstruction safety gap).

## License

Code is distributed under the MIT License (see LICENSE.txt). Generated text and diagrams are distributed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

## See Also

- `2030-pdac-1min/paper/instructions/README.md` for the v0.5.0 instruction set navigation index and 7 BibTeX entries.
- `2030-pdac-1min/paper/inputs/` for the four author prior PDAC papers (paper-1 through paper-4), the Daraxonrasib summary (daraxonrasib-1), the Whipple procedure evidence baseline (research-2), and the Daraxonrasib clinical trial historical timeline (research-1).
- `2030-gbm-1min/` for the parallel GBM 4 arm 1 minute variant that this PDAC variant extends.
- `releases.md` for the v0.6.0 release notes.
- `CHANGELOG.md` for the human readable change log.
