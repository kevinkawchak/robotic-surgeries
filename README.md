# Robotic Surgeries

Physical AI Oncology Trial Robotic Surgeries simulation repository.

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Release](https://img.shields.io/badge/Release-v0.7.0-brightgreen.svg)](releases.md)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://img.shields.io/badge/CI-Python%203.10%2F3.11%2F3.12-3776ab.svg)](.github/workflows/ci.yml)
[![Variant GBM](https://img.shields.io/badge/Variant-GBM%201%20Minute-orange.svg)](2030-gbm-1min)
[![Variant PDAC](https://img.shields.io/badge/Variant-PDAC%201%20Minute-purple.svg)](2030-pdac-1min)
[![Outputs](https://img.shields.io/badge/Outputs-v0.2.0-blueviolet.svg)](2030-gbm-1min/outputs)
[![Paper Template](https://img.shields.io/badge/Paper%20Template-v0.3.0-9cf.svg)](2030-gbm-1min/paper)
[![Paper Full](https://img.shields.io/badge/Paper%20Full-v0.4.0-success.svg)](2030-gbm-1min/paper/full-paper)
[![PDAC Instructions](https://img.shields.io/badge/PDAC%20Instructions-v0.5.0-success.svg)](2030-pdac-1min/paper/instructions)
[![PDAC Codegen](https://img.shields.io/badge/PDAC%20Codegen-v0.6.0-success.svg)](2030-pdac-1min/paper/codegen)
[![PDAC Execution](https://img.shields.io/badge/PDAC%20Execution-v0.7.0-success.svg)](2030-pdac-1min/paper/execution)
[![Adjuvant](https://img.shields.io/badge/Adjuvant-Daraxonrasib-yellow.svg)](https://doi.org/10.5281/zenodo.18099351)

## Thesis

On-premises repository based LLMs provide commands to standard oncology surgical robots based on real-time sensor data and controlled via x, y, z coordinates to administer patient treatment. This workflow minimizes single robot error potential.

## Overview

This repository hosts the v0.7.0 release of the multi-arm robotic oncology resection simulation suite. The first variant is the 4-arm 1-minute glioblastoma trial in `2030-gbm-1min/`, built around a hypothetical 2030 Medtronic NeuroSpeed 1.0 multi-arm parallel stereotactic neurosurgical robot. The v0.5.0 release landed the 8-arm 1-minute PDAC Whipple variant instruction set at `2030-pdac-1min/paper/instructions/`. The v0.6.0 release landed the PDAC 1-minute codegen tree at `2030-pdac-1min/paper/codegen/` produced by Claude Code Opus 4.7 1M Max from the v0.5.0 instructions. The new v0.7.0 release lands the PDAC 1-minute execution tree at `2030-pdac-1min/paper/execution/` produced by running every executable codegen module against the deterministic seed contract (root seed 20260513) across nine sequential commits within a single PR. The execution tree captures real run output: a 1001 record 640 channel sensor sample, a 32 iteration deterministic Latin hypercube sweep with mean composite 93.298 and PJ Grade A 32 of 32, a 128 verdict 4 entrant LLM tournament with PancreSpeed 1.0 winning 96 of 96 played rounds, a 5 vessel safety zone gate sample path verdict log, 3 per anastomosis controller outcome tables, a Daraxonrasib perioperative trajectory with T+7d restart in 29 of 32 iterations, the Zenodo L0 deposition pointer JSON family, the 12 PDAC specific ASCII diagrams inherited from v0.6.0, and the smoke test status (10 of 13 pass, 3 known v0.6.0 discrepancies).

The v0.2.0 release published the runnable end-to-end outputs of the GBM v3.9.1 pipeline under `2030-gbm-1min/outputs/`. The v0.3.0 release added the LaTeX paper template under `2030-gbm-1min/paper/`. The v0.4.0 release landed the populated full LaTeX paper at `2030-gbm-1min/paper/full-paper/`. The v0.5.0 release landed the 21 file PDAC instruction set at `2030-pdac-1min/paper/instructions/`. The v0.6.0 release landed the generated PDAC simulation tree at `2030-pdac-1min/paper/codegen/`. The v0.7.0 release lands the executed PDAC simulation outputs at `2030-pdac-1min/paper/execution/` ready to serve as the basis for a future paper.

The PDAC variant addresses 7 of the 10 approximations cataloged in the v0.4.0 GBM full paper limitations: doubled iterations (16 to 32), multi vendor tournament (single vendor to 3 robots plus 1 human), force time integral cap (added), 100 kHz force sampling (vs 10 kHz), Daraxonrasib precision oncology integration (new), per vessel safety zones (new), and anastomosis ring tension control (new). The remaining 3 approximations (synthetic patient, non deterministic Claude generation, hypothetical 2030 robot) are inherited with explicit cross simulation caveats.

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
    outputs/               # v0.2.0 end-to-end pipeline outputs
    paper/                 # v0.3.0 LaTeX paper template (head start)
      full-paper/          # v0.4.0 populated full LaTeX paper (Overleaf ready)
        final-paper/       # v0.4.0 final populated paper + LaTeX zip
  2030-pdac-1min/          # 8-arm 1-minute PDAC Whipple variant (v0.5.0 / v0.6.0)
    paper/
      inputs/              # source research chunks (read only)
        paper-1/           # author prior PDAC paper 1 (Zenodo 17239510)
        paper-2/           # author prior PDAC paper 2 (Zenodo 17001137)
        paper-3/           # author prior PDAC paper 3 (Zenodo 16415815)
        paper-4/           # author prior PDAC paper 4 (Zenodo 15735068)
        daraxonrasib-1/    # Daraxonrasib summary
        research-1/        # Daraxonrasib clinical trial historical timeline
        research-2/        # Whipple procedure evidence baseline
      instructions/        # v0.5.0 PDAC 1-minute instruction set
      codegen/             # v0.6.0 PDAC 1-minute generated codebase
        README.md          # project README with DOI badges and pipeline ASCII
        LICENSE.txt        # MIT
        pyproject.toml     # Python project plus lint config
        docker-compose.yml # Python + Rust + DuckDB services
        .gitignore         # Python + Rust + Jupyter + macOS
        config/            # project, kinematics, iterations, safety zones, targets
        docs/              # architecture, sensor spec, coordinate mapping, etc.
        schemas/           # JSON Schema, Protocol Buffers, Avro
        src/               # sensors, mapping, control, coordination, vascular,
                           # anastomosis, daraxonrasib, simulation, metrics, llm, zenodo
        data/              # sensor and xyz samples, iteration index, baseline, outcomes
        prompts/           # versioned LLM prompts (tournament + Daraxonrasib advisory)
        results/           # comparison.json, comparison_report.md, advisory.json
        viz/               # ASCII tip path, leaderboard, vascular heatmap
        outputs/           # publication grade output subdirectories
        notebooks/         # iteration / anastomosis / Daraxonrasib analysis
        tests/             # smoke tests
        releases/v0.6.0/   # manifest, metrics, sample seeds, Zenodo DOI
      execution/           # v0.7.0 PDAC 1-minute execution outputs (this release)
        README.md          # execution README with badges, 9 commit plan, ASCII pipeline
        PROCESS.md         # 20 step long form process documentation
        CROSS_REFERENCES.md  # 15 entry cross commit reference matrix
        lint_verification.md # commit 8 lint and format verification record
        sensors/           # 1001 record sensor sample plus per arm summary
        xyz_mapping/       # 1001 xyz command sample plus per arm target table
        coordination/      # 10 kHz heartbeat timing plus collision FSM tables
        iterations/        # 32 iteration index.jsonl plus L3 phase sample
        metrics/           # 6 component composite breakdown plus weights
        comparison/        # 4 entrant tournament leaderboard plus 128 verdicts
        vascular/          # 5 vessel gate verdicts plus vessel proximity table
        anastomosis/       # 3 per anastomosis outcome tables plus summary
        daraxonrasib/      # perioperative trajectory plus restart advisories
        zenodo/            # L0 deposition pointer JSON plus manifest skeleton
        viz/               # 3 ASCII visualizations inherited from v0.6.0
        notebooks/         # 3 notebook computational summaries
        diagrams/          # 12 PDAC ASCII diagrams inherited from v0.6.0
        logs/              # per script run logs plus pytest smoke output
        results/           # headline outcomes plus cross family summary table
        tests/             # smoke test status
      templates/           # LaTeX templates for the future paper
```

## v0.7.0 PDAC Execution (ASCII)

```
+============================================================================+
|       2030-PDAC-1MIN EXECUTION (v0.7.0, 32 iteration run at seed 20260513) |
+============================================================================+

   paper/execution/  end to end PDAC 1 minute simulation execution outputs.
     README.md       DOI badges, 9 commit plan, pipeline ASCII, headlines.
     PROCESS.md      20 step long form process documentation.
     CROSS_REFERENCES.md  15 entry cross commit reference matrix.
     lint_verification.md commit 8 ruff plus yamllint plus size cap record.
     sensors/        1001 record sensor sample (Phase 5, 100 ms, 10 kHz).
                     per arm summary, 80 channel inventory, ASCII channel map.
     xyz_mapping/    1001 xyz command sample, per arm target table, pipeline.
     coordination/   10 kHz heartbeat timing, 4 state collision FSM tables.
     iterations/     32 row index.jsonl, run_00000 L3 phase, summary, ASCII hist.
     metrics/        6 component composite breakdown, frozen weights, weight sum.
     comparison/     128 row leaderboard, robot vs human Round 3, report.
     vascular/       100 tick gate verdict log, 5 vessel proximity table.
     anastomosis/    3 per anastomosis outcomes (PJ 31A, HJ leak, GJ patent).
     daraxonrasib/   perioperative trajectory + advisory (T+7d 29 of 32).
     zenodo/         pointer JSON sample, manifest skeleton, deposition summary.
     viz/            3 ASCII visualizations inherited from v0.6.0 codegen.
     notebooks/      3 notebook computational summaries (Jupyter kernel absent).
     diagrams/       12 PDAC ASCII diagrams inherited from v0.6.0 codegen.
     logs/           per script run logs plus pytest smoke output.
     results/        headline_outcomes.md plus summary_table.csv.
     tests/          smoke test status (10 pass, 3 known v0.6.0 discrepancies).

   Headline outcomes (seed 20260513, 32 iterations):
     PancreSpeed 1.0 mean composite : 93.298
     PancreSpeed 1.0 win rate       : 100.0 percent (96 of 96 played rounds)
     PJ Grade A rate                : 32 of 32 (iteration sweep view)
     Daraxonrasib T+7d restart rate : 29 of 32 (90.6 percent)
     Vascular safety violations     : 0 (across 32 iterations)
     Composite score weights sum    : 1.00 (exact)

   Generated across 9 commits in a single PR by Claude Code Opus 4.7 1M Max
   on 2026-05-13. Limitations: Rust runner not invoked (no cargo), C++
   not built (no g++), LLM backends stubbed (no API key), Zenodo upload
   pending (no token), Jupyter not run (no kernel). The Python runner
   output is canonical and bit identical at seed 20260513.
+============================================================================+
```

## v0.6.0 PDAC Codegen (ASCII)

```
+============================================================================+
|       2030-PDAC-1MIN CODEGEN (v0.6.0, 8-arm 60-second Whipple)             |
+============================================================================+

   paper/codegen/   end to end PDAC 1 minute simulation tree.
     README.md      DOI badges, pipeline ASCII, runtime recipes.
     config/        kinematics, iterations, safety zones, anastomosis targets.
     docs/          architecture, sensor spec, methodology overviews.
     schemas/       sensor record, xyz command, metrics, anastomosis, daraxo.
     src/sensors/   640 channel ingest pipeline.
     src/mapping/   sensor to Cartesian xyz mapping (10 kHz cmd rate).
     src/control/   per arm robot control loop (C++).
     src/coordination/  10 kHz heartbeat bus (C++) + collision avoidance.
     src/vascular/  5 vessel safety zone gate at 10 kHz.
     src/anastomosis/  PJ, HJ, GJ per anastomosis controllers.
     src/daraxonrasib/ perioperative pause + LLM bound restart advisory.
     src/simulation/   32 iteration sweep (Python + Rust runners).
     src/metrics/   6 component frozen composite score.
     src/llm/       4 entrant multi vendor tournament agent.
     src/zenodo/    13.2 GB L0 raw deposition pointer patcher.
     data/iterations/  per iteration L3/L4/events CSV samples + index.
     prompts/       tournament + Daraxonrasib advisory prompts.
     results/       comparison.json, comparison_report.md, advisory.json.
     viz/           ASCII tip path, leaderboard, vascular heatmap.
     outputs/       publication grade samples + 12 ASCII diagrams.
     notebooks/     3 Jupyter notebooks (iteration, anastomosis, Daraxonrasib PK).
     tests/         smoke tests for schemas, gates, scores, advisories.
     releases/v0.6.0/  manifest, metrics, sample seeds, Zenodo DOI.

   Generated across 9 commits in a single PR by Claude Code Opus 4.7 1M Max
   from instructions/ on 2026-05-13. 8th commit fixes errors; 9th commit
   updates the repository top level documentation. Addresses 7 of 10 GBM
   approximations: 32 iterations (vs 16), 4 vendor tournament (vs single
   vendor), force time integral cap, 100 kHz force (vs 10 kHz), Daraxonrasib
   integration, vessel safety zones, anastomosis ring tension control.
+============================================================================+
```

## v0.5.0 PDAC Instructions (ASCII)

```
+============================================================================+
|       2030-PDAC-1MIN INSTRUCTIONS (v0.5.0, 8-arm 60-second Whipple)        |
+============================================================================+

   paper/instructions/   21 instruction files plus markdownlint config.
     README.md           DOI badges, scope, 8 phase timeline, bibtex.
     pdac_context_1min.md  PAT-PDAC-0001 plus vascular anatomy plus 8 phases.
     robot_specification_pancrespeed.md  PancreSpeed 1.0 (hyp 2030, 8 arms).
     sensor_specification_100khz.md  640 channels at mixed 10kHz/100kHz force.
     multi_arm_coordination_8arm.md  10 kHz heartbeat, 3 ms cross arm e-stop.
     vascular_safety_protocol.md  5 vessel no fly/soft warning/hard stop.
     anastomosis_protocols.md  3 anastomoses with ring tension targets.
     daraxonrasib_integration.md  perioperative pause + LLM advisory restart.
     gbm_errors_addressed.md  7 of 10 v0.4.0 GBM approximations addressed.
     competition_protocol.md  4 entrant multi vendor tournament.
     file_size_pyramid_1min.md  L0 Zenodo only; L1-L4 + events committed.
     chunking_strategy.md  6 chunking layers including L4 anastomosis.
     file_format_conventions.md  Parquet zstd-3, UTF-8 LF, no SVG hi freq.
     ascii_diagram_guide.md  12 PDAC specific ASCII diagram templates.
     runtime_environments.md  MacOS, Windows, Linux, Claude Code recipes.
     ci_compliance_checklist.md  8 gates pre commit hook config.
     pr_workflow.md  9 commit single PR with 8th = errors, 9th = repo.
     zenodo_archive_protocol.md  13.2 GB L0 deposition manifest.
     commit_01_overview_1min.md  Future Commit 1 file list.
     commit_02_sensors_1min.md  Future Commit 2 sensor pipeline.
     commit_03_xyz_8arm.md  Future Commit 3 8 arm xyz mapping.
     commit_04_iterations_1min.md  Future Commit 4 32 iteration sweep.
     commit_05_competition_1min.md  Future Commit 5 4 entrant tournament.
     commit_06_error_fixes.md  Future Commit 6 lint matrix and cross ref.
     commit_07_repository_updates.md  Future Commit 7 README + changelog.
     lint_verification.md  v0.5.0 PR commit 8 verification log.
     .markdownlint.yaml  markdownlint config carried from v3.9.1 GBM.

   The v0.6.0 PDAC Codegen tree at paper/codegen/ was generated from these
   instructions by Claude Code Opus 4.7 1M Max across 9 sequential commits
   in a single PR.
+============================================================================+
```

## v0.4.0 Full Paper (ASCII)

```
+==========================================================================+
|       2030-GBM-1MIN FULL PAPER (v0.4.0, populated end-to-end)            |
+==========================================================================+

   paper/full-paper/        Overleaf-ready populated full LaTeX paper.
     main.tex               Title page, TOC, \input{sections/*}.
     new_paper.sty          11 pt, 1 in margins, raggedright tables.
     references.bib         DOI + URL bearing; GitHub + Zenodo clickable.
     build_zip.sh           One command to make LaTeX Source Files.zip.
     sections/
       abstract.tex         Single 900-character on-prem LLM thesis.
       introduction.tex     FDA RTCT + GBM + baseline + thesis + transition.
       methods.tex          12 instructions + NeuroSpeed 1.0 + xyz + sweep.
       results.tex          54 x 1001 sensor sample feat + tournaments.
       discussion.tex       Significance + FDA + LLM safety + head start.
       limitations_future.tex  60min vs 1min deltas + Track A / B futures.
       conclusions.tex      Headline counts + 3 themes + safety + forward.
       back_matter.tex      Acknowledgments / Ethics / Rights / Cite / Data.

   Compile on Overleaf with pdflatex + bibtex + pdflatex + pdflatex.
   Run build_zip.sh in the same directory to produce the Overleaf-ready
   LaTeX Source Files.zip bundle of all sources in this subdirectory.
+==========================================================================+
```

## v0.3.0 Paper Template (ASCII)

```
+==========================================================================+
|       2030-GBM-1MIN PAPER TEMPLATE (v0.3.0, LaTeX head start)            |
+==========================================================================+

   paper/                Bracketed prompts name the exact files to read.
     main.tex            Title page, TOC, \input{sections/*}.
     new_paper.sty       11 pt, 1 in margins, raggedright tables, widows off.
     references.bib      DOI + URL bearing; GitHub + Zenodo clickable.
     sections/
       abstract.tex      900-character title-page abstract (bracketed).
       introduction.tex  FDA RTCT, GBM, baseline, thesis (bracketed).
       methods.tex       Robot, sensors, xyz, iterations, comp (bracketed).
       results.tex       Sensor 54x1001, xyz, iterations, comp (bracketed).
       discussion.tex    Significance, FDA framing, on-prem LLM (bracketed).
       limitations_future.tex  60min vs 1min deltas, Track A/B (bracketed).
       conclusions.tex   Artifact headline, themes, forward path (bracketed).
       back_matter.tex   Acknowledgments / Ethics / Rights / Cite / Data.

   The downstream Claude Code 4.7 Max pass fills each [bracketed prompt]
   with prose, tables, and ASCII diagrams sourced from the exact named
   paths in 2030-gbm-1min/, 2030-gbm-1min/outputs/, and the upstream
   physical-ai-oncology-trials competitions/instructions/one_minute_variant.
+==========================================================================+
```

## v0.2.0 Outputs Pipeline (ASCII)

```
+==========================================================================+
|         2030-GBM-1MIN OUTPUTS PIPELINE (v0.2.0, end-to-end run)          |
+==========================================================================+

  sensors -> xyz_mapping -> iterations -> metrics -> llm comparison
     |           |              |            |            |
     v           v              v            v            v
   outputs/  outputs/        outputs/    outputs/      outputs/
   sensors/  xyz_mapping/   iterations/  metrics/      comparison/
                                                       comparison_robot_vs_human/

                              also feeds:
                              outputs/diagrams/   ASCII diagrams
                              outputs/viz/        HTML + PNG + ASCII charts
                              outputs/reports/    narrative + final report
                              outputs/logs/       per-script log files

  Cumulative 4-arm tip force <= 12 N. Per-arm tip force <= 5.0 N.
  E-stop budget 5 ms. Heartbeat watchdog 3 ms. 100 microsecond park.
+==========================================================================+
```

## High-Level Architecture (ASCII)

```
+-----------------------------------------------------------------------------+
|                ROBOTIC-SURGERIES SUITE (v0.7.0 / two variants)              |
+-----------------------------------------------------------------------------+
|                                                                             |
|   physical-ai-oncology-trials       robotic-surgeries (this repo)           |
|   +----------------------------+    +-------------------------------------+ |
|   | competitions/instructions/ |--->| 2030-gbm-1min/  (1-minute, 4-arm)   | |
|   |   one_minute_variant/      |    |   docs / config / schemas / src /   | |
|   |     - README.md            |    |   data / prompts / results / viz /  | |
|   |     - 12 instruction docs  |    |   outputs/ + paper/ + full-paper/   | |
|   +----------------------------+    +------------------+------------------+ |
|                                                        |                    |
|                                     +------------------+------------------+ |
|                                     | 2030-pdac-1min/ (1-minute, 8-arm)   | |
|                                     |   paper/inputs/ (4 papers + 2 res)  | |
|                                     |   paper/instructions/ v0.5.0        | |
|                                     |   paper/codegen/      v0.6.0        | |
|                                     |   paper/execution/    v0.7.0 <- new | |
|                                     |     - 1001 sensor record sample     | |
|                                     |     - 32 iter index + L3 phase      | |
|                                     |     - 128 verdict tournament + LB   | |
|                                     |     - 5 vessel safety gate verdicts | |
|                                     |     - 3 anastomosis outcome tables  | |
|                                     |     - Daraxonrasib trajectory + adv | |
|                                     |     - 12 PDAC ASCII + 3 viz + logs  | |
|                                     +------------------+------------------+ |
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

## 8-Arm PDAC Coordination Snapshot (v0.5.0 / v0.6.0, 2030-pdac-1min)

```
+============================================================================+
|     8-ARM PDAC COORDINATION HEARTBEAT (10 kHz, 64-byte frame, 100 us deadline)|
+============================================================================+
|    +-------+ 10 kHz broadcast +-------+ 10 kHz broadcast +-------+         |
|    | ARM 1 |<---------------->| ARM 2 |<---------------->| ARM 3 |        |
|    | hyb   |                  | bipol |                  | retr  |        |
|    | u-w-p |                  | + coag|                  | + grsp|        |
|    +---+---+                  +---+---+                  +---+---+         |
|        v                          v                          v             |
|    +-------+ 10 kHz broadcast +-------+ 10 kHz broadcast +-------+         |
|    | ARM 4 |<---------------->| ARM 5 |<---------------->| ARM 6 |        |
|    | iMRI  |                  | bipol |                  | suct  |        |
|    | + NIR |                  | + suct|                  | + coag|        |
|    +---+---+                  +---+---+                  +---+---+         |
|        v                          v                                        |
|    +-------+ 10 kHz broadcast +-------+                                    |
|    | ARM 7 |<---------------->| ARM 8 |                                    |
|    | suct  |                  | NIR + |                                    |
|    | + irr |                  | UV    |                                    |
|    +-------+                  +-------+                                    |
|                                                                            |
|   Cumulative ee_force across 8 arms <= 18 N                                |
|   Per-arm tip force <= 3.0 N / E-stop 3 ms / heartbeat watchdog 100 us     |
|   Per-arm force time integral <= 8.0 N.s (PDAC new floor)                  |
|   5 vessel safety zones (SMV, PV, HA, CA, SMA) with no-fly/soft/hard stop  |
|   3 anastomoses (PJ, HJ, GJ) with ring tension target +/- 0.05 N           |
+============================================================================+
```

## 4-Arm GBM Coordination Snapshot (v3.9.1, 2030-gbm-1min)

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

Detailed cross-platform setup recipes (Linux, MacOS M3 Ultra, Windows, NVIDIA A100 GPU, and Claude Code) live in [2030-gbm-1min/README.md](2030-gbm-1min/README.md) for the GBM variant and in [2030-pdac-1min/paper/codegen/README.md](2030-pdac-1min/paper/codegen/README.md) for the PDAC v0.6.0 codegen tree. The v0.7.0 PDAC execution tree at [2030-pdac-1min/paper/execution/README.md](2030-pdac-1min/paper/execution/README.md) reproduces every executable codegen module against root seed 20260513. The minimum to reproduce the v0.7.0 execution outputs is:

```
git clone https://github.com/kevinkawchak/robotic-surgeries.git
cd robotic-surgeries/2030-pdac-1min/paper/codegen
python3.12 -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
pip install -e .[dev,llm-local,zenodo,pdac]
PYTHONPATH=. python -m src.sensors.ingest_8arm --seed 20260513 --arm-id 1 --duration-ms 100 --output ../execution/sensors/sensor_sample_8arm.jsonl
PYTHONPATH=. python -m src.simulation.iterate_1min --seed 20260513 --iterations 32 --output-dir ../execution/iterations
PYTHONPATH=. python -m src.llm.compare_agent_1min --seed 20260513 --iterations 32 --backend ollama --output ../execution/comparison/comparison.json
PYTHONPATH=. python -m src.daraxonrasib.trajectory --seed 20260513 --iterations 32 --output ../execution/daraxonrasib/perioperative_trajectory.csv
PYTHONPATH=. python -m src.daraxonrasib.advisory --input-index ../execution/iterations/index.jsonl --output ../execution/daraxonrasib/advisories.json
```

The same scripts can be run inside Claude Code (CLI, web, or IDE plugin) or on a conventional high-end server, and they target identical CSV/Parquet outputs for a fixed seed (20260513). The Rust runner provides a 7x throughput boost on Linux servers; build it with `cargo run --release` from `src/simulation/`.

To compile the populated full GBM LaTeX paper at `2030-gbm-1min/paper/full-paper/`, upload that directory to Overleaf or run:

```
cd 2030-gbm-1min/paper/full-paper
pdflatex main.tex
bibtex   main
pdflatex main.tex
pdflatex main.tex
```

An Overleaf-ready zip can be bundled locally with the helper script in the same directory:

```
cd 2030-gbm-1min/paper/full-paper
chmod +x build_zip.sh
./build_zip.sh
```

The resulting `LaTeX Source Files.zip` uploads to Overleaf via **New Project -> Upload Project**.

## Citation

If you use this repository in academic work, please cite:

```
@software{kawchak_robotic_surgeries_v0_7_0_2026,
  author    = {Kawchak, Kevin},
  title     = {robotic-surgeries: 4-arm GBM v3.9.1 + 8-arm PDAC v0.5.0/v0.6.0/v0.7.0 multi-variant},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.18445179},
  url       = {https://github.com/kevinkawchak/robotic-surgeries}
}
```

For the v0.4.0 GBM paper specifically, cite:

```
@misc{kawchak_2026_20113157,
  author    = {Kawchak, Kevin},
  title     = {2030: 60 Second Glioblastoma AI Robotic Surgery},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.20113157},
  url       = {https://doi.org/10.5281/zenodo.20113157}
}
```

For the v0.5.0 PDAC instruction set, the v0.6.0 PDAC codegen, and the v0.7.0 PDAC execution, the parent repository DOI 10.5281/zenodo.18445179 anchors the citation until the future paper publication DOI is issued.

For the Daraxonrasib clinical trial historical timeline, cite:

```
@misc{kawchak_2025_18099351,
  author    = {Kawchak, Kevin},
  title     = {Daraxonrasib Efficient LLM Trial Simulations},
  year      = {2025},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.18099351},
  url       = {https://doi.org/10.5281/zenodo.18099351}
}
```

## License

MIT License. See [LICENSE](LICENSE).

## See also

- [releases.md](releases.md) for versioned release notes (v0.1.0, v0.2.0, v0.3.0, v0.4.0, v0.5.0, v0.6.0, v0.7.0 and later).
- [CHANGELOG.md](CHANGELOG.md) for the human-readable change log.
- [references.md](references.md) for citations of standards, prior art, and inputs.
- [2030-gbm-1min/README.md](2030-gbm-1min/README.md) for the GBM 4-arm 1-minute variant.
- [2030-gbm-1min/outputs/README.md](2030-gbm-1min/outputs/README.md) for the GBM v0.2.0 end-to-end run outputs.
- [2030-gbm-1min/paper/README.md](2030-gbm-1min/paper/README.md) for the v0.3.0 GBM LaTeX paper template.
- [2030-gbm-1min/paper/full-paper/README.md](2030-gbm-1min/paper/full-paper/README.md) for the v0.4.0 GBM populated full paper.
- [2030-pdac-1min/paper/instructions/README.md](2030-pdac-1min/paper/instructions/README.md) for the v0.5.0 PDAC 8-arm 1-minute instruction set navigation index, the 8 phase 60 second Whipple timeline, the 7 BibTeX entries, and the future Claude Code generation plan.
- [2030-pdac-1min/paper/codegen/README.md](2030-pdac-1min/paper/codegen/README.md) for the v0.6.0 PDAC 8-arm 1-minute generated codebase, the 640 channel sensor stack, the 32 iteration sweep, the 4 entrant tournament, the vascular safety zones, the 3 anastomosis controllers, the Daraxonrasib perioperative pause and restart logic, the Zenodo L0 deposition patcher, and the runtime recipes for MacOS Apple Silicon, Windows 11, Linux Ubuntu 22.04 LTS, and Claude Code (CLI / web / IDE).
- [2030-pdac-1min/paper/execution/README.md](2030-pdac-1min/paper/execution/README.md) for the v0.7.0 PDAC 8-arm 1-minute execution outputs produced by running every executable codegen module against the deterministic seed contract (root seed 20260513). Includes the 1001 record sensor sample, the 32 iteration index plus L3 phase sample, the 128 verdict tournament leaderboard, the 5 vessel safety zone gate verdict log, the 3 per anastomosis controller outcome tables, the Daraxonrasib perioperative trajectory plus the postoperative restart advisory, the Zenodo deposition pointer JSON family, the 12 PDAC ASCII diagrams, and the smoke test status.
