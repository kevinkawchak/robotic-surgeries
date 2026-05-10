# 2030 GBM 1-Minute Outputs (v0.2.0)

Released on 10 May 2026
CEO Kevin Kawchak, ChemicalQDevice

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Release](https://img.shields.io/badge/Release-v0.2.0-brightgreen.svg)](../../releases.md)
[![Project](https://img.shields.io/badge/Project-v3.9.1-orange.svg)](../README.md)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](../LICENSE.txt)
[![Python](https://img.shields.io/badge/Python-3.10%2F3.11%2F3.12-3776ab.svg)](../pyproject.toml)
[![CI](https://img.shields.io/badge/CI-lint--and--format-green.svg)](../../.github/workflows/ci.yml)
[![Resolution](https://img.shields.io/badge/Resolution-1ms-blue.svg)](../docs/sensor_spec.md)

## Thesis

On-premises repository based LLMs provide commands to standard oncology
surgical robots based on real-time sensor data and controlled via x, y, z
coordinates to administer patient treatment. This workflow minimizes single
robot error potential.

## Overview

This directory holds every artifact produced by running every script under
`2030-gbm-1min/` end to end. The runs were performed on a single machine
under deterministic seed 20260510 so the artifacts are reproducible bit for
bit. Each subsystem owns its own subdirectory and its own README; the file
you are reading is the consolidated view.

The scripts were exercised in this order:

1. `python -m sensors.ingest_4arm` (sensor ingestion + validate)
2. `python -m mapping.sensor_to_xyz_4arm` (per-arm xyz mapper + ASCII path)
3. `python -m simulation.iterate_1min` (16-iteration sweep)
4. `python -m metrics.compute_1min` (per-iteration metric rows)
5. `python -m llm.compare_agent_1min` (4-entity tournament, 2 runs)

## Repository Structure

```
2030-gbm-1min/outputs/
  README.md                              this file
  sensors/                                sensor ingestion outputs
    sensor_sample_4arm.jsonl              1000-row mixed-rate sample
    sensor_sample_4arm.csv                1000-row flat sample
    summary.json                          per-arm and aggregate stats
    README.md
  xyz_mapping/                            xyz mapper outputs
    xyz_trace_sample_arm{1..4}.csv        60-row per-arm xyz traces
    xyz_path_4arm.txt                     ASCII per-second xyz overlay
    summary.json                          per-arm xyz range and counters
    README.md
  iterations/                             16-iteration sweep aggregates
    run_000NN_L1_50ms.parquet             50 ms aggregate per arm
    run_000NN_L2_1s.parquet               1 s aggregate per arm
    run_000NN_L3_phase.parquet            per-phase aggregate per arm
    run_000NN_events.parquet              event log per iteration
    run_000NN_L0_raw.zenodo_pointer.json  1 KB pointer to Zenodo L0
    index.jsonl                           cross-iteration manifest
    aggregate.duckdb                      DuckDB analytical store
    iteration_table.md                    full per-iteration table
    summary.json                          aggregate counters and ranges
    README.md
  metrics/                                per-iteration metric rows
    robot_outcomes_1min.parquet           46 rows (16 robot + 30 human)
    robot_outcomes_1min.json              json mirror for the LLM agent
    robot_outcomes_mixed_4.json           mixed tournament input
    iteration_metric_table.md             ranked composite table
    summary.json                          robot vs human aggregates
    README.md
  comparison/                             default robot-vs-robot tournament
    comparison.json
    comparison_report.md
    comparison_report.pdf
    README.md
  comparison_robot_vs_human/              mixed robot+human tournament
    comparison.json
    comparison_report.md
    comparison_report.pdf
  diagrams/                               curated ASCII diagrams
    pipeline_architecture.txt
    four_arm_coordination.txt
    phase_timeline.txt
    data_size_pyramid.txt
    composite_score_formula.txt
    thesis_loop.txt
    per_iteration_composite_table.md
    README.md
  viz/                                    static and ASCII visualizations
    metrics_dashboard.html
    metrics_summary.png
    per_arm_contribution.png
    xyz_path_4arm.txt
    composite_bar_chart.txt
    composite_histogram.txt
    per_arm_resection_chart.txt
    wall_clock_chart.txt
    README.md
  reports/                                consolidated narrative reports
    run_summary.md
    final_report.md
    process_log.md
    limitations.md
    README.md
  logs/                                   per-script log files
    sensor_ingest.log
    xyz_mapping.log
    iteration_run.txt
    metrics.log
    comparison.log
```

## Pipeline Architecture (ASCII)

```
+==========================================================================+
|                 2030-GBM-1MIN PIPELINE (v3.9.1, 1-Minute Variant)        |
+==========================================================================+

  +--------------+    +--------------+    +-----------------+
  | sensors      |--->| mapping      |--->| simulation      |
  | ingest_4arm  |    | sensor_to_xyz|    | iterate_1min    |
  | (1 kHz cmd + |    | _4arm        |    |  16 iterations  |
  |  10 kHz force|    |  CSV + ASCII |    |  L1 50 ms       |
  |  per arm)    |    |  per-arm     |    |  L2 1 s         |
  +------+-------+    +------+-------+    |  L3 phase       |
         |                   |            |  events         |
         |                   |            |  L0 -> Zenodo   |
         v                   v            +--------+--------+
  outputs/sensors/   outputs/xyz_mapping/          |
                                                   v
                                          outputs/iterations/
                                                   |
                                                   v
                                       +-----------+----------+
                                       | metrics              |
                                       | compute_1min         |
                                       |  composite formula   |
                                       +-----------+----------+
                                                   |
                                                   v
                                       +-----------+----------+
                                       | llm                  |
                                       | compare_agent_1min   |
                                       |  4-entity tournament |
                                       |  claude-opus-4-7     |
                                       +-----------+----------+
                                                   |
                                                   v
                            outputs/comparison/   outputs/viz/
                            outputs/comparison_robot_vs_human/

  Cumulative 4-arm tip force <= 12 N. Per-arm tip force <= 5.0 N.
  E-stop budget 5 ms. Heartbeat watchdog 3 ms. 100 microsecond park.
+==========================================================================+
```

## 4-Arm Coordination Snapshot

```
+==========================================================================+
|     4-ARM COORDINATION HEARTBEAT (1 kHz, 32-byte frame, 1 ms deadline)   |
+==========================================================================+
|        +-------+  1 kHz broadcast  +-------+                             |
|        | ARM 1 |<----------------->| ARM 2 |                             |
|        | hyb.  |                   | bipol |                             |
|        | u-w-p |                   | + irr |                             |
|        +---+---+                   +---+---+                             |
|            |                           |                                 |
|            v                           v                                 |
|        +-------+                   +-------+                             |
|        | ARM 3 |<----------------->| ARM 4 |                             |
|        | suct. |  1 kHz broadcast  | iMRI  |                             |
|        | + col |                   | + ALA |                             |
|        +-------+                   +-------+                             |
|    Cumulative ee_force across 4 arms <= 12 N                             |
|    Per-arm tip force <= 5.0 N / E-stop 5 ms / heartbeat watchdog 3 ms    |
+==========================================================================+
```

## Composite Score Aggregates

| Metric                       | Robot (n=16) min | Robot mean | Robot max | Human (n=30) min | Human mean | Human max |
|------------------------------|------------------|-----------|-----------|------------------|-----------|-----------|
| quality_score                | 90.07            | 92.22     | 93.89     | 82.00            | 87.73     | 92.00     |
| safety_score                 | 30.00            | 56.56     | 90.00     | 69.00            | 72.73     | 77.00     |
| cost_usd                     | 8061.37          | 8297.42   | 8738.26   | 17700.0          | 18656.67  | 19500.0   |
| total_seconds                | 60.00            | 60.00     | 60.00     | 11250            | 12320     | 13500     |
| composite_score              | 86.02            | 88.53     | 92.37     | 66.70            | 70.35     | 73.50     |
| resection_completeness_pct   | 93.68            | 95.91     | 97.64     | -                | -         | -         |
| eloquent_preservation_score  | 85.07            | 87.22     | 88.89     | -                | -         | -         |
| predicted_kps_day_30         | 80.06            | 81.77     | 83.11     | -                | -         | -         |

## Mixed Tournament Result

| Rank | Entity                      | Composite | Skill mu | Skill sigma |
|------|-----------------------------|-----------|----------|-------------|
| 1    | this_project_v3_9_1_1min    | 88.46     | 671.36   | 96.50       |
| 2    | this_project_v3_9_1_1min    | 87.73     | 672.85   | 94.75       |
| 3    | HUM-001                     | 71.40     | 600.00   | 200.00      |
| 4    | HUM-002                     | 68.60     | 600.00   | 200.00      |

Robot wins all 4 robot-vs-human pairings with confidence 0.955 to 1.000. The
structural-time-dimension caveat is preserved in every round rationale.

## Citation

```
@software{kawchak_gbm_1min_outputs_v0_2_0_2026,
  author       = {Kawchak, Kevin},
  title        = {2030-gbm-1min outputs v0.2.0 (4-arm Medtronic NeuroSpeed
                  1.0 1-minute glioblastoma trial)},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {v0.2.0},
  doi          = {10.5281/zenodo.18445179},
  url          = {https://doi.org/10.5281/zenodo.18445179}
}
```

## License

This directory inherits the project MIT license. See
[../LICENSE.txt](../LICENSE.txt).
