# Pancreatic Cancer Robotic Surgery Simulation Instructions (v0.5.0)

Released on 13 May 2026
CEO Kevin Kawchak, ChemicalQDevice

[![Release](https://img.shields.io/badge/Release-v0.5.0-brightgreen.svg)](https://github.com/kevinkawchak/robotic-surgeries)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Resolution](https://img.shields.io/badge/Resolution-0.1ms-blue.svg)](https://github.com/kevinkawchak/robotic-surgeries)
[![Variant](https://img.shields.io/badge/Variant-1%20Minute-orange.svg)](https://github.com/kevinkawchak/robotic-surgeries/tree/main/2030-pdac-1min)
[![Disease](https://img.shields.io/badge/Disease-PDAC-purple.svg)](https://github.com/kevinkawchak/robotic-surgeries/tree/main/2030-pdac-1min)
[![Adjuvant](https://img.shields.io/badge/Adjuvant-Daraxonrasib-yellow.svg)](https://doi.org/10.5281/zenodo.18099351)

This directory contains the v0.5.0 instruction set that a future Claude Code Opus 4.7 1M Max session will execute to produce a complete, end to end pancreatic ductal adenocarcinoma (PDAC) robotic surgery clinical trial simulation at 100 microsecond (0.0001 s) resolution. No simulation files are produced by this PR. The future session reads these instruction files and authors the simulation across nine sequential commits within a single pull request. The instruction set extends the v3.9.1 1 minute glioblastoma variant from kevinkawchak/physical-ai-oncology-trials/tree/main/competitions/instructions/one_minute_variant/ with PDAC specific sensors, an 8 arm robot platform, vascular safety zones, anastomosis protocols, and Daraxonrasib precision oncology adjunct integration.

## Thesis

On premises repository based LLMs provide commands to standard oncology surgical robots based on real time sensor data and controlled via x, y, z coordinates to administer patient treatment. This workflow minimizes single robot error potential. The PDAC 1 minute variant operationalizes that thesis for the most technically demanding solid tumor resection in oncological surgery, the pancreaticoduodenectomy (Whipple procedure), executed in 60 seconds across eight cooperating arms that share a deterministic 10 kHz heartbeat bus. The work positions Daraxonrasib (the pan KRAS inhibitor evaluated in the RASolute 302 and RASolve 301 programs and tracked through the daraxonrasib historical timeline cited below) as the precision oncology adjuvant that the 60 second robotic Whipple procedure pairs with.

## Disease Impact and Why PDAC Is Harder Than GBM

Pancreatic ductal adenocarcinoma is the third leading cause of cancer death in the United States and the fourth in the European Union. The five year overall survival of PDAC remains below 13 percent and is the lowest among major solid tumors. The Whipple procedure is the most technically demanding of all curative intent abdominal oncology operations. It involves the resection and reconstruction of four luminal structures (the pancreas, the duodenum, the common bile duct, and the stomach or pylorus) and the dissection of two named vessels (the superior mesenteric vein and the portal vein) plus the artery first or uncinate first approach to the superior mesenteric artery. The leading lethal postoperative pathway is the cascade from pancreatic fistula, intra abdominal infection, hemorrhage, sepsis, and failure to rescue. A robotic Whipple at 60 seconds therefore must coordinate eight arms across the dissection, three named anastomoses (pancreaticojejunostomy, hepaticojejunostomy, gastrojejunostomy), vascular control, and hemostasis verification, all under the patient safety floors established by IEC 80601-2-77, 21 CFR 50.30, and the FDA Software as a Medical Device framework. The 2025 Dutch nationwide cohort of 1000 robotic pancreaticoduodenectomies reported conversion of 10.1 percent, Clavien Dindo grade III or higher complications of 41.3 percent, grade B/C postoperative pancreatic fistula of 24.4 percent, in hospital or 30 day mortality of 3.9 percent, and a mean ideal outcome rate of 47 percent. The instruction set in this directory targets a 2030 simulation in which the eight arm hypothetical Medtronic PancreSpeed 1.0 platform reduces the conversion rate to 0 percent in simulation, the grade B/C fistula rate to under 5 percent in simulation, and the 90 day mortality to under 0.5 percent in simulation, with the structural caveat that the comparison is simulation against simulation and the human baseline is held at the 2025 Dutch cohort numbers.

## Scope

- One simulated patient: PAT-PDAC-0001 (68 year old, head of pancreas PDAC, 3.4 cm tumor abutting the superior mesenteric vein at 75 degrees, KRAS G12D mutant, MSI stable, CA 19 9 of 412 U/mL at diagnosis, ECOG performance status 1, neoadjuvant modified FOLFIRINOX times 4 cycles completed, Daraxonrasib eligible per the RASolute 302 broad pan KRAS criteria).
- One surgical procedure: classic pancreaticoduodenectomy (Whipple) with pylorus preservation, with portomesenteric venous resection if vessel margin requires it, with artery first uncinate dissection, with pancreaticojejunostomy and hepaticojejunostomy and gastrojejunostomy reconstruction, and with a single pass through cumulative force, hemostasis verification, and final margin scan.
- One simulation duration: 60 seconds (60,000 ms for 10 kHz command channels and 600,000 ticks for 100 kHz force channels). The pre op anesthesia, port placement, and table positioning are precomputed and frozen at simulation start; the simulation begins at the moment the eight arms are docked, the artery first window is open, and the four major vascular landmarks have been identified by the imaging arms.
- One primary surgical robot: hypothetical 2030 Medtronic PancreSpeed 1.0 eight arm parallel coelomic oncology robot. The current SOTA Intuitive da Vinci SP and Medtronic Hugo RAS platforms cannot perform a 60 second Whipple because their per arm end effector velocity, joint angular velocity, E stop latency, positioning accuracy at the vessel surface, and force resolution are each 5 to 500 times short of the requirement.
- Sensor sampling rate: mixed 100 kHz force channels and 10 kHz other channels per arm.
- Channel schema: 80 channels per arm times 8 arms equals 640 total channels.
- Iteration count: 32 deterministic iterations per benchmarked configuration. Doubled from the v3.9.1 16 iterations because the PDAC scenario has more free parameters (vessel angle, fistula risk score, anastomosis ring tension, Daraxonrasib serum concentration trajectory) and the per iteration committed data is partitioned across eight arms with a tighter L1 budget per arm.
- Competition: this project's 60 second PancreSpeed run versus three competitor robotic platforms (the prior 60 second GBM ROSA ONE Brain v3.0 baseline from the v3.9.1 release, a hypothetical 2030 Intuitive da Vinci SP successor platform, and a hypothetical 2030 Medtronic Hugo RAS oncology successor platform) versus the 2025 Dutch human surgeon baseline (1000 robot assisted Whipples reported with mean ideal outcome rate 47 percent). All four entrants are scored under the frozen composite score weights and the structural time dimension caveat (1 minute robot versus 4 to 8 hour human baseline) is preserved in every rationale.

## Procedure Phase Timeline (8 phases, 60 seconds total)

The PDAC 1 minute scenario requires its own phase boundaries. The GBM 1 minute 4 phase 60 second timeline does not apply to this variant. The PDAC variant timeline is fixed in pdac_context_1min.md and is reproduced here for orientation.

| Phase | Start (s) | End (s) | Duration (s) | Description |
|-------|-----------|---------|--------------|-------------|
| Pre op (precomputed, not in committed simulation) | T-3600 | T+0 | 60 minutes | Anesthesia, port placement, table positioning, eight arm docking, artery first window opening, four major vascular landmark identification; frozen at simulation start |
| Phase 1 exploration and Kocher maneuver | 0.000 | 6.000 | 6 s | Arms 1 and 2 perform Kocher maneuver, arm 3 retracts duodenum, arm 4 ultrasound mapping of portal vein and superior mesenteric vein, arms 5 to 8 stand by under heartbeat watchdog |
| Phase 2 vascular control and venous dissection | 6.000 | 16.000 | 10 s | Arm 1 dissects superior mesenteric vein; arm 2 dissects portal vein; arm 3 controls hepatic artery; arm 4 ultrasound continues; arms 5 and 6 bipolar coagulate venous branches; arm 7 suctions; arm 8 imaging |
| Phase 3 uncinate dissection (artery first) | 16.000 | 24.000 | 8 s | Arm 1 performs artery first uncinate dissection from the superior mesenteric artery; arm 2 retracts mesentery; arm 3 controls celiac axis; arm 4 ultrasound continues; arms 5 to 8 support |
| Phase 4 specimen removal and en bloc resection | 24.000 | 32.000 | 8 s | Arms 1 and 2 remove the en bloc specimen (pancreatic head, duodenum, distal bile duct, gallbladder, regional lymph nodes); arms 3 and 4 hemostasis on the resection bed; arms 5 to 8 verify negative margins |
| Phase 5 pancreaticojejunostomy reconstruction | 32.000 | 42.000 | 10 s | Arms 1 and 2 perform the duct to mucosa pancreaticojejunostomy with arms 3 and 4 retracting; arm 5 monitors anastomosis ring tension; arms 6 to 8 stabilize the bowel loop |
| Phase 6 hepaticojejunostomy reconstruction | 42.000 | 48.000 | 6 s | Arms 1 and 2 perform the hepaticojejunostomy with arms 3 and 4 retracting; arm 5 monitors bile leak via near infrared indocyanine green; arms 6 to 8 stabilize |
| Phase 7 gastrojejunostomy reconstruction | 48.000 | 54.000 | 6 s | Arms 1 and 2 perform the antecolic gastrojejunostomy or duodenojejunostomy (pylorus preserving); arm 3 retracts; arm 4 confirms patency; arms 5 to 8 stabilize |
| Phase 8 hemostasis verification, drain placement, and arm withdrawal | 54.000 | 60.000 | 6 s | Arms 1 and 3 retract; arm 2 final hemostasis pass; arm 4 ultrasound final margin scan; arms 5 and 6 place two closed suction drains near the pancreaticojejunostomy and the hepaticojejunostomy; arm 7 confirms gastrojejunostomy patency; arm 8 records final near infrared scan and prepares for the 60 second mark |

## Why a Future Pass

A 60 second mixed 100 kHz force plus 10 kHz command resolution surgical simulation across 8 arms contains 6.4 million records per 100 kHz channel and 600,000 records per 10 kHz channel. Authoring that volume of data inline as markdown would exceed the working memory of any single LLM session. The instruction set therefore directs the future Claude Code session to (a) author small generator scripts that produce the full data files at runtime and (b) author small human review samples directly. This mirrors the chunking pattern used by the existing competition input papers under physical-ai-oncology-trials/competitions/inputs/ and the prior v3.9.1 chunking strategy. For the PDAC 1 minute variant the per iteration committed data is approximately 980 KB across pyramid levels L1, L2, L3, and the event log. The committed total across 32 iterations is approximately 31.4 MB plus 2.0 MB of fixed overhead, for a total of 33.4 MB. The 33.4 MB total exceeds the GBM 9.7 MB total because PDAC committed data covers eight arms, eight surgical phases, three anastomosis events per iteration, and Daraxonrasib serum concentration tracking per iteration. The full L0 raw at mixed 10 kHz plus 100 kHz force is 412 MB per iteration and 13.2 GB across 32 iterations; the L0 raw is archived to Zenodo per zenodo_archive_protocol.md and is never committed to Git. The single largest committed file is constrained to remain under the GitHub 10 MB cap and every Parquet under 5 MB by the CI compliance addendum in commit_06_error_fixes.md.

## Instruction Files (this directory)

| File | Purpose |
|------|---------|
| README.md | This file. Top level orientation, scope, phase timeline, and table of contents. |
| pdac_context_1min.md | Patient PAT-PDAC-0001, disease, KRAS G12D mutation status, neoadjuvant therapy history, Daraxonrasib eligibility, and the 8 phase 60 second procedure timeline. |
| robot_specification_pancrespeed.md | Medtronic PancreSpeed 1.0 specification; 8 arms; 1,200 mm/s; 100 kHz force; 1,600 mm cubed per second peak removal; 0.05 mm RMS positioning at 1,200 mm/s; 3 ms E stop. |
| sensor_specification_100khz.md | 100 kHz force sensors per arm with 10 kHz command sensors and PDAC specific sensors (NIR indocyanine green imaging, vessel surface proximity, pancreatic duct manometry, anastomosis ring tension, bile spectrophotometry); total 640 channels (80 per arm times 8 arms). |
| multi_arm_coordination_8arm.md | Inter arm collision avoidance protocol; 10 kHz heartbeat; 50 microsecond emergency arm park trigger; cumulative cross arm tip force cap of 18 N; per arm tip force cap of 3 N. |
| file_size_pyramid_1min.md | Pyramid 5 budget table; per iteration committed budget of 980 KB across L1 plus L2 plus L3 plus events plus the anastomosis event log. |
| chunking_strategy.md | How to chunk 100 kHz force and 10 kHz command data so a future LLM does not exceed memory. Builds on the v3.9.1 chunking strategy with the PDAC specific L4 layer for anastomosis events. |
| file_format_conventions.md | Repository wide file format defaults. Parquet zstd-3 default. JSONL line oriented. CSV human readable samples. ASCII for diagrams. Markdown for prose. |
| ascii_diagram_guide.md | ASCII and Mermaid diagram replacements for SVG. New 8 arm coordination template. New PancreSpeed mechanical schematic template. |
| competition_protocol.md | Four entrant multi vendor tournament protocol with frozen composite weights. Builds on the v3.9.1 4 entrant pattern with three new robot vendors instead of one prior version snapshot. |
| runtime_environments.md | MacOS Apple Silicon, Windows 11, Linux Ubuntu 22.04, NVIDIA A100, NVIDIA H100, and Claude Code (CLI, web, IDE) execution recipes for the future generated simulation tree at 2030-pdac-1min/. |
| ci_compliance_checklist.md | Pre commit ruff format check, ruff check, yamllint d relaxed, file size cap, Parquet size cap, line ending, and trailing whitespace gates that the future generated code must pass. |
| pr_workflow.md | Nine commit single PR workflow definition for the future code generation pass. |
| vascular_safety_protocol.md | PDAC specific vascular safety zones around the superior mesenteric vein, portal vein, hepatic artery, celiac axis, and superior mesenteric artery. Defines no fly volumes, soft warning volumes, and hard stop volumes. |
| anastomosis_protocols.md | Three anastomosis protocols: pancreaticojejunostomy duct to mucosa, hepaticojejunostomy end to side, and gastrojejunostomy or duodenojejunostomy antecolic. Defines anastomosis ring tension targets, fistula risk score inputs, and bile spectrophotometry leak detection thresholds. |
| daraxonrasib_integration.md | Daraxonrasib precision oncology adjuvant integration. Defines the serum concentration trajectory, the perioperative pause and restart logic per RASolute 302 and RASolve 301 protocols, the LLM bound advisory layer, and the per iteration Daraxonrasib eligibility tracking. |
| gbm_errors_addressed.md | Catalog of approximations, errors, and caveats from the v3.9.1 GBM 1 minute project and the v0.4.0 GBM full paper that this PDAC variant explicitly addresses. Cross references commit_06_error_fixes.md. |
| zenodo_archive_protocol.md | DOI assignment, deposition layout, SHA 256 manifest contract for the 13.2 GB L0 archive across 32 iterations. |
| commit_01_overview_1min.md | Future Commit 1 file list for the PDAC 1 minute variant; PDAC context, robot spec, vascular safety. |
| commit_02_sensors_1min.md | Future Commit 2 sensor specs covering 640 channels at mixed 100 kHz force plus 10 kHz command rates; pyramid output schema. |
| commit_03_xyz_8arm.md | Future Commit 3 coordinate mapping for 8 arms; per arm safety zone gating; cross arm coordination; anastomosis ring tension control loop. |
| commit_04_iterations_1min.md | Future Commit 4 32 iteration sweep at 1 minute; 50 Hz committed L1; mixed 10 kHz command plus 100 kHz force Zenodo L0. |
| commit_05_competition_1min.md | Future Commit 5 four entrant multi vendor tournament; vs three competitor robotic platforms; vs Dutch human surgeon baseline. |
| commit_06_error_fixes.md | Future Commit 6 error review and patch instructions across the PDAC output tree; addresses lint, format, cross reference, and the seven specific GBM approximations cataloged in gbm_errors_addressed.md. |
| commit_07_repository_updates.md | Future Commit 7 README, CHANGELOG, releases.md instructions for the future generated code PR. |

## Future Output Tree (Reference)

The output tree intentionally lives at 2030-pdac-1min/ so that this paper/instructions/ directory remains a pure specification and the generated simulation lives next to its peers in the same repository. The output tree is parallel to the 2030-gbm-1min/ tree; nothing in the GBM tree is modified.

```
2030-pdac-1min/
  README.md
  LICENSE.txt
  pyproject.toml
  docker-compose.yml
  .gitignore
  docs/
    architecture_8arm.md
    sensor_spec_640ch.md
    coordinate_mapping_8arm.md
    iteration_design_32.md
    comparison_methodology_4vendor.md
    multi_arm_coordination_8arm.md
    vascular_safety_protocol.md
    anastomosis_protocols.md
    daraxonrasib_integration.md
  config/
    project.yaml
    kinematics_8arm.yaml
    iterations.yaml
    vascular_safety_zones.yaml
    anastomosis_targets.yaml
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
    sensors/ingest_8arm.py
    mapping/sensor_to_xyz_8arm.py
    control/robot_loop_8arm.cpp
    coordination/arm_heartbeat_10khz.cpp
    vascular/safety_zone_gate.py
    anastomosis/pancreaticojejunostomy.py
    anastomosis/hepaticojejunostomy.py
    anastomosis/gastrojejunostomy.py
    daraxonrasib/trajectory.py
    daraxonrasib/advisory.py
    simulation/iterate_1min.py
    simulation/runner_1min.rs
    metrics/compute_1min.py
    llm/compare_agent_1min.py
    zenodo/patch_pointers.py
  data/
    sensor_sample_8arm.jsonl
    sensor_sample_8arm.csv
    iterations/
      run_NNNNN_L1_20ms.parquet
      run_NNNNN_L2_1s.parquet
      run_NNNNN_L3_phase.parquet
      run_NNNNN_L4_anastomosis.parquet
      run_NNNNN_events.parquet
      run_NNNNN_L0_raw.zenodo_pointer.json
      index.jsonl
      aggregate.duckdb
    human_surgeon_baseline.csv
    robot_outcomes_1min.parquet
  prompts/
    comparison_prompt_1min.md
    daraxonrasib_advisory_prompt.md
  results/
    comparison.json
    comparison_report.md
    comparison_report.pdf
  viz/
    xyz_path_8arm.txt
    metrics_dashboard.html
    metrics_summary.png
    vascular_safety_heatmap.html
  notebooks/
    iteration_analysis_1min.ipynb
    anastomosis_analysis.ipynb
    daraxonrasib_pk_analysis.ipynb
  logs/
    iteration_run.txt
  releases/
    v0.5.0/
      manifest.json
      metrics.json
      iterations_index.jsonl
      sample_seeds.txt
      zenodo_doi.txt
  paper/
    inputs/             # source research chunks (read only context)
    instructions/       # this directory
    templates/          # LaTeX templates for the future paper
```

## Single PR Single Prompt Workflow

This directory is produced by a single prompt across nine commits within one pull request, with the eighth commit reserved for error fixes and the ninth commit reserved for repository wide updates. The nine commits in this PR are:

1. README.md (this file), pdac_context_1min.md.
2. sensor_specification_100khz.md, multi_arm_coordination_8arm.md.
3. vascular_safety_protocol.md, anastomosis_protocols.md, commit_03_xyz_8arm.md.
4. file_size_pyramid_1min.md, chunking_strategy.md, commit_04_iterations_1min.md, commit_01_overview_1min.md, commit_02_sensors_1min.md.
5. robot_specification_pancrespeed.md, competition_protocol.md, commit_05_competition_1min.md.
6. runtime_environments.md, ci_compliance_checklist.md, file_format_conventions.md, pr_workflow.md, ascii_diagram_guide.md.
7. daraxonrasib_integration.md, gbm_errors_addressed.md, zenodo_archive_protocol.md, commit_06_error_fixes.md, commit_07_repository_updates.md.
8. Error fixes across all PDAC instruction files; addresses any lint, format, or cross reference issues that would cause the GitHub Cl / lint-and-format (3.10) (pull...), (3.11) (pull...), and (3.12) (pull...) checks to fail.
9. Repository wide updates to README.md, releases.md (v0.5.0 release notes block per the FORMAT specified), and CHANGELOG.md.

## Conventions Inherited Repository Wide

- All instruction files in this directory use single dashes only. No em dashes, no double dashes, no triple dashes.
- All instruction files use black text only. No color overrides, no inline color spans.
- All instruction files use plain GitHub Flavored Markdown.
- All future generated diagrams use ASCII text inside .txt files or Mermaid blocks inside .md files. SVG files are not produced for high frequency time series; SVG remains acceptable for static low density schematics under 100 KB.
- All committed files in the PDAC 1 minute variant must remain under 10 MB; all committed Parquet files must remain under 5 MB. The CI compliance addendum in commit_06_error_fixes.md enforces this.

## Differentiators from the v3.9.1 GBM 1 Minute Variant

This PDAC 1 minute variant differs from the v3.9.1 GBM 1 minute variant in seven concrete ways. Each differentiator is grounded in PDAC clinical complexity and in the approximations and errors learned from the v0.4.0 GBM full paper at 2030-gbm-1min/paper/full-paper/final-paper/.

1. Eight cooperating arms instead of four. The Whipple procedure requires more concurrent dissection, reconstruction, retraction, and imaging workstreams than a GBM craniotomy. Eight arms cover Kocher, vascular dissection, uncinate dissection, specimen removal, three anastomoses, hemostasis verification, and drain placement.
2. 100 kHz force sampling instead of 10 kHz. The fistula risk score sensitivity to pancreatic duct manometry and anastomosis ring tension dynamics requires 10x finer force sampling.
3. 640 sensor channels instead of 200. Eight arms times 80 channels per arm covers the standard arm channels plus PDAC specific channels (NIR indocyanine green imaging, vessel surface proximity, pancreatic duct manometry, anastomosis ring tension, bile spectrophotometry).
4. 32 iterations instead of 16. The PDAC scenario has more free parameters and requires a larger sweep to bound the cumulative force violation rate at the 95 percent confidence interval, addressing the cumulative force clamp ablation gap noted in 2030-gbm-1min/paper/full-paper/final-paper/sections/limitations_future.tex.
5. Four entrant multi vendor tournament from the start instead of single vendor with prior version snapshots. Three competitor robotic platforms are included (Intuitive da Vinci SP successor, Medtronic Hugo RAS oncology successor, Verb Surgical successor) plus the Dutch human surgeon baseline. This addresses the single vendor gap noted in 2030-gbm-1min/paper/full-paper/final-paper/sections/limitations_future.tex.
6. Daraxonrasib precision oncology adjuvant integration. The instruction set explicitly defines the perioperative Daraxonrasib pause and restart logic, the serum concentration trajectory, and the LLM bound advisory layer per the RASolute 302 and RASolve 301 protocols. No equivalent adjuvant integration exists in the GBM variant.
7. PDAC specific vascular safety zones and anastomosis protocols. The vascular_safety_protocol.md and anastomosis_protocols.md files define no fly volumes, soft warning volumes, and hard stop volumes around the named PDAC vessels and the three anastomosis events, none of which exist in the GBM variant.

## Source Citations

The PDAC 1 minute variant draws on existing repository content. Each instruction file cites its sources inline with relative paths. Primary anchors are listed below for orientation.

- A. kevinkawchak/physical-ai-oncology-trials/tree/main/competitions/instructions/ and the one_minute_variant/ subdirectory. Source for the chunking strategy, file format conventions, ASCII diagram guide, runtime environments, competition protocol, CI compliance checklist, and seven commit single PR workflow that this PDAC variant inherits and extends to nine commits.
- B. kevinkawchak/robotic-surgeries/tree/main/2030-gbm-1min/ and its subdirectories. Source for the generated simulation tree pattern, the per arm 7 DOF DH kinematics table pattern, the per iteration pyramid Parquet layout, and the on premises LLM tournament pattern that the PDAC variant scales to eight arms.
- C. kevinkawchak/robotic-surgeries/tree/main/2030-gbm-1min/paper/full-paper/final-paper/. Source for the approximations vs generated vs executed accounting pattern, the 60 min vs 1 min formal delta table pattern, the Track A vs Track B trade off table pattern, and the 10 concrete future work deliverables, all of which are extended in gbm_errors_addressed.md and commit_06_error_fixes.md to address the seven specific PDAC additions to the future work list.
- D. kevinkawchak/robotic-surgeries/tree/main/2030-pdac-1min/paper/inputs/. Source for the four author prior PDAC papers (paper-1 through paper-4), the daraxonrasib summary (daraxonrasib-1), the Whipple procedure evidence baseline (research-2), and the Daraxonrasib clinical trial historical timeline (research-1).

## Bibliography

The following BibTeX entries anchor the prior author works and the prior clinical developments that this PDAC 1 minute instruction set builds from. They will be carried into the future generated paper at 2030-pdac-1min/paper/full-paper/ as the canonical reference set for the on premises LLM thesis applied to the 60 second robotic Whipple procedure.

### Prior author PDAC papers

```bibtex
@misc{kawchak_2025_17239510,
  author       = {Kawchak, Kevin},
  title        = {Accelerating FDA Compliance and Cost Efficiency of
                   in silico Clinical Trials via AI Digital Twin
                   Pancreatic Cancer Simulation
                  },
  month        = oct,
  year         = 2025,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.17239510},
  url          = {https://doi.org/10.5281/zenodo.17239510},
}

@misc{kawchak_2025_17001137,
  author       = {Kawchak, Kevin},
  title        = {QSP Metastatic Pancreatic Cancer AI Clinical Trial
                   Simulation From Protocol to Prediction: Code,
                   VVUQ, and Playbook
                  },
  month        = aug,
  year         = 2025,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.17001137},
  url          = {https://doi.org/10.5281/zenodo.17001137},
}

@misc{kawchak_2025_16415815,
  author       = {Kawchak, Kevin},
  title        = {ChatGPT 100,000 Patient 24-Month In Silico Phase
                   III 5-Arm Pancreatic Cancer Clinical Trial
                   Triplicate
                  },
  month        = jul,
  year         = 2025,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.16415815},
  url          = {https://doi.org/10.5281/zenodo.16415815},
}

@misc{kawchak_2025_15735068,
  author       = {Kawchak, Kevin},
  title        = {End-to-End Pancreatic Ductal Adenocarcinoma
                   Digital Twin Clinical Trial Proposals
                  },
  month        = jun,
  year         = 2025,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.15735068},
  url          = {https://doi.org/10.5281/zenodo.15735068},
}
```

### Prior 60 second glioblastoma robotic surgery paper

```bibtex
@misc{kawchak_2026_20113157,
  author       = {Kawchak, Kevin},
  title        = {2030: 60 Second Glioblastoma AI Robotic Surgery},
  month        = may,
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20113157},
  url          = {https://doi.org/10.5281/zenodo.20113157},
}
```

### Daraxonrasib historical context

```bibtex
@misc{kawchak_2025_18099351,
  author       = {Kawchak, Kevin},
  title        = {Daraxonrasib Efficient LLM Trial Simulations},
  month        = dec,
  year         = 2025,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.18099351},
  url          = {https://doi.org/10.5281/zenodo.18099351},
}
```

## License

The instruction set inherits the repository MIT license for code artifacts. The instruction text itself is distributed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
