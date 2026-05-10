# Robotic Surgeries

Physical AI Oncology Trial Robotic Surgeries simulation repository.

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Release](https://img.shields.io/badge/Release-v0.1.0-brightgreen.svg)](releases.md)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://img.shields.io/badge/CI-Python%203.10%2F3.11%2F3.12-3776ab.svg)](.github/workflows/ci.yml)
[![Variant](https://img.shields.io/badge/Variant-1%20Minute-orange.svg)](2030-gbm-1min)

## Thesis

On-premises repository based LLMs provide commands to standard oncology surgical robots based on real-time sensor data and controlled via x, y, z coordinates to administer patient treatment. This workflow minimizes single robot error potential.

## Overview

This repository hosts the v0.1.0 release of the multi-arm robotic glioblastoma resection simulation suite. The first project under this umbrella is the 4-arm 1-minute variant in `2030-gbm-1min/`, built around a hypothetical 2030 Medtronic NeuroSpeed 1.0 multi-arm parallel stereotactic neurosurgical robot. Each arm carries 7 degrees of freedom and is sampled at mixed 1 kHz commands plus 10 kHz force per arm; the four arms cooperate over a deterministic 1 kHz heartbeat broadcast bus with a 5 ms E-stop budget and a 12 N cumulative force cap on the patient frame.

Subsequent variants under this same repository will explore longer durations, alternative robot platforms, and additional cancer sites. The shared instruction layer continues to live in `kevinkawchak/physical-ai-oncology-trials` and is read in the future to generate sibling output trees here.

## Repository Structure

```
robotic-surgeries/
  README.md                # this file
  releases.md              # versioned release notes (v0.1.0 and later)
  CHANGELOG.md             # human-readable change log per release
  references.md            # citations for standards, prior art, and inputs
  LICENSE                  # MIT
  .github/workflows/ci.yml # ruff format / ruff check / yamllint matrix
  2030-gbm-1min/           # 4-arm 1-minute glioblastoma trial (v0.1.0 first variant)
    README.md
    LICENSE.txt
    pyproject.toml
    docker-compose.yml
    .gitignore
    docs/                  # architecture, sensor spec, coordination, methodology
    config/                # project, kinematics, iterations YAML
    schemas/               # JSON Schema, Protocol Buffers, Avro
    src/                   # sensors, mapping, control, coordination, simulation,
                           # metrics, llm, zenodo
    data/                  # sensor and xyz samples, baseline, outcomes
    data/iterations/       # 16-iteration L1/L2/L3/events Parquet, index, DuckDB
    prompts/               # versioned LLM prompt
    results/               # comparison.json, comparison_report.{md,pdf}
    viz/                   # ASCII path, HTML dashboard, PNG charts
    notebooks/             # iteration analysis Jupyter notebook
    logs/                  # iteration_run.txt
    releases/v3.9.1/       # immutable per-version snapshot
```

## High-Level Architecture (ASCII)

```
+-----------------------------------------------------------------------------+
|                ROBOTIC-SURGERIES SUITE (v0.1.0 / first variant)             |
+-----------------------------------------------------------------------------+
|                                                                             |
|   physical-ai-oncology-trials       robotic-surgeries (this repo)           |
|   +----------------------------+    +-------------------------------------+ |
|   | competitions/instructions/ |--->| 2030-gbm-1min/  (1-minute, 4-arm)   | |
|   |   one_minute_variant/      |    |   docs / config / schemas / src /   | |
|   |     - README.md            |    |   data / prompts / results / viz /  | |
|   |     - 12 instruction docs  |    |   notebooks / logs / releases/v3.9.1| |
|   +----------------------------+    +------------------+------------------+ |
|                                                        |                    |
|                                                        v                    |
|                                            +-----------+-----------+        |
|                                            | On-prem LLM (Anthropic|        |
|                                            | claude-opus-4-7) +    |        |
|                                            | tournament agent      |        |
|                                            +-----------+-----------+        |
|                                                        |                    |
|                                                        v                    |
|                                            +-----------+-----------+        |
|                                            | Zenodo L0 raw archive |        |
|                                            | DOI 10.5281/...18445179|       |
|                                            +-----------------------+        |
+-----------------------------------------------------------------------------+
```

## 4-Arm Coordination Snapshot (v3.9.1, 2030-gbm-1min)

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

## Quick Start

Detailed cross-platform setup recipes (Linux, MacOS M3 Ultra, Windows, NVIDIA A100 GPU, and Claude Code) live in [2030-gbm-1min/README.md](2030-gbm-1min/README.md). The minimum is:

```
git clone https://github.com/kevinkawchak/robotic-surgeries.git
cd robotic-surgeries/2030-gbm-1min
python3.10 -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
pip install -e .[dev,llm-local,zenodo]
python -m src.simulation.iterate_1min --seed 20260510 --iterations 1
```

The same scripts can be run inside Claude Code (CLI, web, or IDE plugin) or on a conventional high-end server, and they target identical Parquet outputs for a fixed seed.

## Citation

If you use this repository in academic work, please cite:

```
@software{kawchak_robotic_surgeries_v0_1_0_2026,
  author    = {Kawchak, Kevin},
  title     = {robotic-surgeries: 4-arm 1-minute glioblastoma trial v0.1.0},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.18445179},
  url       = {https://github.com/kevinkawchak/robotic-surgeries}
}
```

## License

MIT License. See [LICENSE](LICENSE).

## See also

- [releases.md](releases.md) for versioned release notes (v0.1.0 and later).
- [CHANGELOG.md](CHANGELOG.md) for the human-readable change log.
- [references.md](references.md) for citations of standards, prior art, and inputs.
- [2030-gbm-1min/README.md](2030-gbm-1min/README.md) for the project narrative, file generation outcomes, and per-commit roadmap of the 4-arm 1-minute variant.
