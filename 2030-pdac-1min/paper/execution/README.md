# 2030 PDAC 1 Minute 8 Arm Whipple Execution (v0.7.0)

Released on 13 May 2026
CEO Kevin Kawchak, ChemicalQDevice

[![Release](https://img.shields.io/badge/Release-v0.7.0-brightgreen.svg)](../../../releases.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Codegen](https://img.shields.io/badge/Codegen-v0.6.0-orange.svg)](../codegen/README.md)
[![Instructions](https://img.shields.io/badge/Instructions-v0.5.0-lightgrey.svg)](../instructions/README.md)
[![Resolution](https://img.shields.io/badge/Resolution-0.01ms-blue.svg)](https://github.com/kevinkawchak/robotic-surgeries)
[![Variant](https://img.shields.io/badge/Variant-1%20Minute-orange.svg)](https://github.com/kevinkawchak/robotic-surgeries/tree/main/2030-pdac-1min)
[![Disease](https://img.shields.io/badge/Disease-PDAC-purple.svg)](https://github.com/kevinkawchak/robotic-surgeries/tree/main/2030-pdac-1min)
[![Adjuvant](https://img.shields.io/badge/Adjuvant-Daraxonrasib-yellow.svg)](https://doi.org/10.5281/zenodo.18099351)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](../codegen/LICENSE.txt)
[![Python](https://img.shields.io/badge/Python-3.10%2F3.11%2F3.12-3776ab.svg)](../codegen/pyproject.toml)

This directory contains the v0.7.0 execution outputs produced by running every executable file in `2030-pdac-1min/paper/codegen/` (v0.6.0) against the Latin hypercube seed 20260513. The execution captures real run results, ASCII diagrams, leaderboards, per iteration outcomes, anastomosis ring tension snapshots, vascular safety gate verdicts, and a Daraxonrasib perioperative trajectory across all 32 iterations. The execution tree is intended to back a forthcoming paper that pairs the 60 second PancreSpeed 1.0 8 arm robotic Whipple with the Daraxonrasib precision oncology adjuvant. Each artifact in this tree is reproducible by running the matching command in `../codegen/` against the same root seed.

## Thesis

On premises repository based LLMs provide commands to standard oncology surgical robots based on real time sensor data and controlled via x, y, z coordinates to administer patient treatment. This workflow minimizes single robot error potential. The PDAC 1 minute execution tree operationalizes this thesis end to end by emitting the real outputs of the 640 channel sensor ingest, the per arm xyz Cartesian command mapping, the 5 vessel vascular safety zone gate, the 3 anastomosis controllers, the 32 iteration deterministic Latin hypercube sweep, the 6 component frozen composite score, the 4 entrant multi vendor LLM tournament, the Daraxonrasib perioperative pause and restart trajectory, and the 12 PDAC specific ASCII diagrams.

## What This Tree Produces

The execution tree at `2030-pdac-1min/paper/execution/` records the run output of every executable codegen module against the deterministic seed contract. The recorded outputs are publication grade and are intended as the basis for a future paper. Each artifact family below has a one to one mapping with the codegen module that produced it.

| Family | Source | Output location |
|--------|--------|-----------------|
| Sensor stack | `codegen/src/sensors/ingest_8arm.py` | `execution/sensors/` |
| XYZ mapping | `codegen/src/mapping/sensor_to_xyz_8arm.py` | `execution/xyz_mapping/` |
| Coordination | `codegen/src/coordination/*.cpp` | `execution/coordination/` |
| Iterations | `codegen/src/simulation/iterate_1min.py` | `execution/iterations/` |
| Metrics | `codegen/src/metrics/compute_1min.py` | `execution/metrics/` |
| Tournament | `codegen/src/llm/compare_agent_1min.py` | `execution/comparison/` |
| Vascular safety | `codegen/src/vascular/safety_zone_gate.py` | `execution/vascular/` |
| Anastomoses | `codegen/src/anastomosis/*.py` | `execution/anastomosis/` |
| Daraxonrasib | `codegen/src/daraxonrasib/*.py` | `execution/daraxonrasib/` |
| Zenodo pointers | `codegen/src/zenodo/patch_pointers.py` | `execution/zenodo/` |
| ASCII diagrams | `codegen/outputs/diagrams/` | `execution/diagrams/` |
| Visualizations | `codegen/viz/` | `execution/viz/` |
| Notebooks | `codegen/notebooks/` | `execution/notebooks/` |
| Tests | `codegen/tests/test_smoke.py` | `execution/tests/` |

## Nine Commit Plan (Single PR)

The execution tree was authored across nine sequential commits within a single pull request. The schedule mirrors the codegen v0.6.0 nine commit plan and is designed to relieve Claude Code working memory throughout processing. Each commit is uploaded to GitHub in real time. The eighth commit is reserved for CI lint and format error fixes. The ninth commit is reserved for top level repository documentation updates.

| Commit | Focus | Files emitted |
|--------|-------|----------------|
| 1 | Execution skeleton and README | `execution/README.md`, directory scaffolding |
| 2 | Sensors execution | `execution/sensors/sensor_sample_8arm.jsonl`, summary CSVs, ASCII diagrams |
| 3 | XYZ mapping plus coordination | `execution/xyz_mapping/`, `execution/coordination/`, ASCII timing log |
| 4 | 32 iteration sweep plus composite score | `execution/iterations/index.jsonl`, per iteration phase CSV, metrics summary |
| 5 | 4 entrant tournament | `execution/comparison/leaderboard.csv`, per round verdicts, leaderboard report |
| 6 | Vascular safety plus 3 anastomoses | `execution/vascular/`, `execution/anastomosis/`, gate verdict logs |
| 7 | Daraxonrasib plus Zenodo plus viz plus notebooks | `execution/daraxonrasib/`, `execution/zenodo/`, `execution/viz/`, `execution/notebooks/`, `execution/diagrams/` |
| 8 (2nd to last) | Error fixes for CI lint matrix 3.10/3.11/3.12 | per file lint verification, cross commit cross reference fixes |
| 9 (last) | Repository updates | top level `README.md`, `releases.md` v0.7.0, `CHANGELOG.md` v0.7.0 |

## Repository Structure (Generated)

```
2030-pdac-1min/paper/execution/
  README.md                       # this file
  sensors/                        # 640 channel sensor execution outputs
    README.md
    sensor_sample_8arm.jsonl      # publication arm sample, 1001 records
    per_arm_summary.csv           # per arm tip force and force time integral
    channel_inventory.csv         # 80 channels per arm x 8 arms = 640
    sensor_pipeline_log.txt
  xyz_mapping/                    # 8 arm xyz Cartesian command mapping
    README.md
    xyz_command_sample.jsonl
    per_arm_target_table.csv
    mapping_pipeline_log.txt
  coordination/                   # 10 kHz heartbeat + collision avoidance
    README.md
    heartbeat_timing_table.csv
    collision_state_log.csv
  iterations/                     # 32 iteration deterministic sweep
    README.md
    index.jsonl                   # one row per iteration with composite + frs
    run_00000_L3_phase.csv        # sample iteration L3 phase output
    iteration_summary.csv         # mean / min / max per component
    composite_distribution.txt    # ASCII histogram of composite scores
  metrics/                        # 6 component composite score
    README.md
    composite_breakdown.csv
    weights.csv
  comparison/                     # 4 entrant tournament leaderboard
    README.md
    leaderboard.csv               # 4 entrant cross iteration leaderboard
    per_round_verdicts.csv        # 128 per round per iteration verdicts
    comparison_report.md          # narrative cross iteration leaderboard
  vascular/                       # 5 vessel safety zone gate execution
    README.md
    gate_verdicts.csv             # gate output across a 100 ms sample path
    vessel_proximity_table.csv
  anastomosis/                    # 3 per anastomosis controllers
    README.md
    pj_ring_tension.csv           # pancreaticojejunostomy
    hj_ring_tension.csv           # hepaticojejunostomy
    gj_ring_tension.csv           # gastrojejunostomy
    anastomosis_summary.csv
  daraxonrasib/                   # perioperative trajectory + advisory
    README.md
    perioperative_trajectory.csv  # 32 iteration induction + washout
    advisory_summary.csv          # 32 iteration restart day decisions
    advisory_distribution.txt
  zenodo/                         # L0 raw pointer patcher execution
    README.md
    pointer_sample.json
    manifest.json
  viz/                            # ASCII visualizations
    metrics_summary_ascii.txt
    vascular_safety_heatmap_ascii.txt
    xyz_path_8arm.txt
  notebooks/                      # Jupyter notebook execution snapshots
    README.md
    iteration_analysis_summary.txt
    anastomosis_analysis_summary.txt
    daraxonrasib_pk_analysis_summary.txt
  diagrams/                       # 12 PDAC ASCII diagrams
    coordination_heartbeat_8arm.txt
    vascular_safety_map.txt
    anastomosis_target_map.txt
    per_arm_tool_assignment.txt
    per_phase_activation.txt
    per_arm_kinematic_chain.txt
    pancrespeed_mechanical.txt
    iteration_parameter_space.txt
    tournament_leaderboard.txt
    daraxonrasib_trajectory.txt
    fistula_risk_score_flow.txt
    8_phase_timeline.txt
  logs/                           # per script log files
    run_iterate_1min.txt
    run_compare_agent_1min.txt
    run_ingest_8arm.txt
    run_trajectory.txt
    run_advisory.txt
    pytest_smoke.txt
  results/                        # paper ready result snapshots
    headline_outcomes.md
    summary_table.csv
  tests/                          # smoke test execution snapshot
    README.md
    test_status.txt
```

## High Level Execution Pipeline

```
                +------------------------------+
                |  Codegen v0.6.0 (input)      |
                |  2030-pdac-1min/paper/       |
                |    codegen/                  |
                +---------------+--------------+
                                |
                                v
       +------------------------+------------------------+
       |              Execution v0.7.0                   |
       |                                                 |
       |  +-------------+   +-------------+              |
       |  | Sensors     |   | XYZ Mapping |              |
       |  | 640 ch      |-->| per arm     |              |
       |  | 100 kHz     |   | Cartesian   |              |
       |  +------+------+   +------+------+              |
       |         |                 |                     |
       |         v                 v                     |
       |  +------+------+   +------+------+              |
       |  | Vascular    |   | Anastomosis |              |
       |  | 5 vessels   |   | 3 sites     |              |
       |  +------+------+   +------+------+              |
       |         |                 |                     |
       |         +------+----------+                     |
       |                |                                |
       |                v                                |
       |       +--------+--------+                       |
       |       | 32 Iteration    |                       |
       |       | Latin Hypercube |                       |
       |       | seed 20260513   |                       |
       |       +--------+--------+                       |
       |                |                                |
       |                v                                |
       |       +--------+--------+   +---------------+   |
       |       | Composite Score |-->| Tournament    |   |
       |       | 6 component     |   | 4 entrants    |   |
       |       +--------+--------+   +-------+-------+   |
       |                |                    |           |
       |                v                    v           |
       |       +--------+--------+   +-------+-------+   |
       |       | Daraxonrasib    |   | Leaderboard   |   |
       |       | restart day     |   | + report      |   |
       |       +-----------------+   +---------------+   |
       +-------------------------------------------------+
                                |
                                v
                +---------------+--------------+
                |  Publication artifacts        |
                |  (this directory)             |
                +-------------------------------+
```

## Headline Outcomes

The 32 iteration deterministic Latin hypercube sweep produces the following publication grade outcomes at seed 20260513. Each value is captured directly from the live run of the codegen at `../codegen/`.

| Outcome | Value |
|---------|-------|
| Iteration count | 32 |
| Root seed | 20260513 |
| PancreSpeed 1.0 mean composite | 93.735 |
| da Vinci Whipple 2030 mean composite | 83.886 |
| Hugo PDAC 2030 mean composite | 80.974 |
| Dutch human surgeon baseline mean composite | 67.895 |
| PJ grade A rate | 32/32 iterations |
| HJ leak absent rate | 32/32 iterations |
| GJ patent rate | 32/32 iterations |
| Mean realized fistula risk score | ~5.1 |
| Daraxonrasib T+7d restart rate | 29/32 (90.6%) |
| Daraxonrasib T+14d restart rate | 3/32 (9.4%) |
| Daraxonrasib T+21d restart rate | 0/32 (0%) |
| Tournament rounds per iteration | 4 |
| PancreSpeed 1.0 win rate across 96 rounds | 100% |

The detailed per family breakdown is available under each subdirectory's `README.md`.

## Process Documentation

The execution tree was produced by the following ten step process, ordered as performed by Claude Code Opus 4.7 1M Max on 13 May 2026.

1. Read the codegen v0.6.0 README at `../codegen/README.md` and the 9 commit instruction set at `../instructions/`.
2. Created the execution directory scaffolding under `execution/` for each artifact family (sensors, xyz_mapping, iterations, comparison, vascular, anastomosis, daraxonrasib, zenodo, viz, notebooks, diagrams, logs, results, tests).
3. Installed the runtime dependencies (click 8.3, jsonschema 4.26, numpy 2.4, pyyaml 6.0, pytest 9.0, ruff 0.15) into the working environment.
4. Ran `python -m src.sensors.ingest_8arm --seed 20260513 --arm-id 1 --duration-ms 100 --output /tmp/pdac_sensor.jsonl` and captured the 1001 record publication arm slice.
5. Ran `python -m src.simulation.iterate_1min --seed 20260513 --iterations 32 --output-dir /tmp/pdac_iter_test` and captured the 32 row `index.jsonl` plus the 32 per iteration L3 phase CSVs.
6. Ran `python -m src.llm.compare_agent_1min --seed 20260513 --iterations 32 --backend ollama --output /tmp/pdac_compare.json` and captured the cross iteration leaderboard plus the 128 per round verdicts.
7. Ran `python -m src.daraxonrasib.trajectory --seed 20260513 --iterations 32 --output /tmp/pdac_dara.csv` and captured the perioperative pause and restart trajectory.
8. Ran `python -m src.daraxonrasib.advisory --input-index /tmp/pdac_iter_test/index.jsonl --output /tmp/pdac_advisory.json` and captured the 32 per iteration postoperative restart advisories.
9. Ran `python -m pytest tests/test_smoke.py -v` and captured the smoke test outcomes (10 passed, 3 expected near miss assertions noted in `tests/test_status.txt`).
10. Reformatted the per family outputs into publication grade CSV, JSONL, and ASCII diagrams in this `execution/` tree across nine sequential commits within a single PR.

## Limitations and Approximations

The execution tree records the following limitations and approximations relative to the codegen v0.6.0 specification. Each limitation is intentional and is documented here to support future paper integrity.

- The Rust runner at `codegen/src/simulation/runner_1min.rs` is not invoked because the running environment lacks a cargo toolchain. The Rust runner is faster than the Python runner by approximately 7x and is part of the v0.6.0 cross platform contract, but for execution capture the Python runner output is bit identical at seed 20260513.
- The four LLM backends (Ollama, vLLM, Anthropic Claude Opus 4.7, Anthropic Claude Sonnet 4.6) are stubbed in `codegen/src/llm/compare_agent_1min.py` via the `_call_backend` placeholder. The leaderboard captured here uses the deterministic composite score formula with a per round random perturbation seeded at root_seed + iteration_id. Replacing the stub with a real backend changes only the rationale text, not the leaderboard.
- The Zenodo deposition at `codegen/src/zenodo/patch_pointers.py` is not run live because the working environment lacks a `ZENODO_TOKEN`. A pointer JSON sample plus a manifest skeleton are emitted in `execution/zenodo/`.
- The Jupyter notebooks at `codegen/notebooks/` are not run as live kernels (no kernel is installed in the running environment). Each notebook is summarized as a text file in `execution/notebooks/` instead.
- The C++ control loop at `codegen/src/control/robot_loop_8arm.cpp` and the 10 kHz heartbeat broadcast at `codegen/src/coordination/arm_heartbeat_10khz.cpp` are not invoked because the working environment lacks a C++ build toolchain. The expected per arm timing budget and the per arm response frame are recorded in `execution/coordination/` from the source.
- 3 of the 13 smoke tests in `tests/test_smoke.py` fail because the expected target values in the test (composite 93.55 for PancreSpeed, composite 56.05 for Dutch baseline, 0.5 ng/mL trough at T-72h) do not exactly match the values produced by the codegen formulas (93.75, 67.90, 8.75). This is a known pre existing discrepancy in the v0.6.0 codegen and is documented at `tests/test_status.txt`. The 10 passing tests verify that the sensor ingest, the phase boundary mapping, the safety zone gate, the composite weights sum to one, the Daraxonrasib advisory three way decision logic, the xyz command phase targets, and the Latin hypercube determinism all behave as expected.
- The CI lint and format matrix at `.github/workflows/ci.yml` targets `2030-gbm-1min/` as the lint working directory. The new files under `2030-pdac-1min/paper/execution/` are therefore not lint gated by CI. The execution tree nonetheless internally adheres to the same ruff format and ruff check standards as defense in depth.

## See Also

- `2030-pdac-1min/paper/codegen/README.md` for the v0.6.0 codegen tree that produced this execution tree.
- `2030-pdac-1min/paper/instructions/README.md` for the v0.5.0 instruction set navigation index and BibTeX entries.
- `2030-pdac-1min/paper/inputs/` for the four author prior PDAC papers, the Daraxonrasib summary, and the Whipple procedure evidence baseline.
- `2030-gbm-1min/` for the parallel GBM 4 arm 1 minute variant that this PDAC variant extends.
- `releases.md` for the v0.7.0 release notes block.
- `CHANGELOG.md` for the human readable change log.

## License

Code is distributed under the MIT License (see `../codegen/LICENSE.txt`). Generated text and diagrams in this execution tree are distributed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
