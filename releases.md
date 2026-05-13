# Release Notes

This file tracks every tagged release of the robotic-surgeries repository.
Releases follow semantic versioning. The first project to land here is the
4-arm 1-minute glioblastoma trial in `2030-gbm-1min/` (project version
v3.9.1, repository release v0.1.0). The v0.2.0 release publishes the
end-to-end run outputs of the same pipeline. The v0.3.0 release lands the
LaTeX paper template under `2030-gbm-1min/paper/`. The v0.4.0 release
lands the populated full LaTeX paper under `2030-gbm-1min/paper/full-paper/`.
The v0.5.0 release lands the 8-arm 1-minute PDAC instruction set at
`2030-pdac-1min/paper/instructions/`. The v0.6.0 release lands the
PDAC 1-minute generated codebase at `2030-pdac-1min/paper/codegen/`.

## Release title

v0.6.0 - 2030 PDAC 1-Minute 8-Arm Whipple Codegen (Generated Tree from v0.5.0 Instructions)

## Summary

This release lands the v0.6.0 PDAC 1-minute generated codebase at
`2030-pdac-1min/paper/codegen/` produced by Claude Code Opus 4.7 1M Max
from the v0.5.0 instruction set at `2030-pdac-1min/paper/instructions/`
across nine sequential commits within a single PR. The codegen tree
includes the 640 channel sensor stack at mixed 10 kHz command plus
100 kHz force, the per arm 7 DOF DH kinematics, the 5 vessel vascular
safety zones (SMV, PV, hepatic artery, celiac axis, SMA) with no fly
soft warning hard stop volumes, the 3 anastomosis controllers
(pancreaticojejunostomy duct to mucosa, hepaticojejunostomy end to side,
gastrojejunostomy antecolic), the 32 iteration deterministic Latin
hypercube sweep with seed 20260513, the 6 component frozen composite
score (Quality 0.30, Time 0.20, Cost 0.15, Safety 0.15, Patient
experience 0.05, Anastomosis quality 0.15), the 4 entrant multi vendor
LLM tournament agent (PancreSpeed 1.0 vs da Vinci Whipple 2030 vs Hugo
PDAC 2030 vs Dutch human surgeon baseline), the Daraxonrasib
perioperative pause and restart logic with LLM bound advisory layer,
the Zenodo L0 deposition patcher for the 13.2 GB raw archive, and 12
PDAC specific ASCII diagrams. Cross platform runtime recipes are
provided for MacOS Apple Silicon, Windows 11, Linux Ubuntu 22.04 LTS,
and Claude Code (CLI / web / IDE). The 8th commit (2nd to last)
addresses the CI lint and format matrix failure mode (Cl /
lint-and-format Python 3.10 / 3.11 / 3.12) and the 9th commit (last)
updates the repository top level documentation. The PDAC v0.6.0 codegen
simulation across 32 iterations produces a mean PancreSpeed 1.0
composite score of 93.55 versus 84.10 for the hypothetical 2030 da
Vinci Whipple successor, 80.60 for the hypothetical 2030 Hugo PDAC
successor, and 56.05 for the 2025 Dutch human surgeon baseline, with
the structural time dimension caveat (1 minute robot vs 5.4 hour human
baseline) preserved in every Round 3 rationale. The CI lint and format
gates on Python 3.10, 3.11, and 3.12 continue to pass because the new
files under `2030-pdac-1min/paper/codegen/` are outside the current CI
matrix working directory (`2030-gbm-1min/`); the codegen tree
nonetheless internally passes the same gates as defense in depth. No
committed file exceeds 10 MB and no committed Parquet exceeds 5 MB.

## Features

- 640 channel 8 arm sensor ingest pipeline at `2030-pdac-1min/paper/codegen/src/sensors/ingest_8arm.py` with three schema formats at `schemas/sensor_record_8arm.{schema.json, proto, avsc}` and a publication arm sample slice at `outputs/sensors/sensor_sample_8arm.csv`.
- Per arm 7 DOF DH parameter kinematics at `config/kinematics_8arm.yaml` with per arm base frame offsets for arms 1 to 4 (patient right side) and arms 5 to 8 (patient left side).
- Per arm xyz Cartesian command mapping pipeline at `src/mapping/sensor_to_xyz_8arm.py` with the 7 state command enum (EMIT, HOLD, SLOW, PARK, E_STOP, HEARTBEAT_ACK, PHASE_BOUNDARY) and the per arm per phase trajectory library at `config/per_arm_trajectory_library.yaml`.
- Per arm C++ robot control loop at `src/control/robot_loop_8arm.cpp` and 10 kHz heartbeat broadcast at `src/coordination/arm_heartbeat_10khz.cpp` with the per arm 32 byte response frame and the 100 microsecond watchdog deadline plus the 3 ms cross arm e stop budget plus the 50 microsecond per arm park budget.
- 5 vessel vascular safety zone gate at `src/vascular/safety_zone_gate.py` with the per vessel volume table at `config/vascular_safety_zones.yaml` (SMV, PV, HA, CA, SMA) and 4 actions (clear, no fly, soft warning, hard stop).
- 3 per anastomosis controllers at `src/anastomosis/pancreaticojejunostomy.py`, `hepaticojejunostomy.py`, and `gastrojejunostomy.py` with the per anastomosis ring tension targets at `config/anastomosis_targets.yaml` (PJ 0.45 N, HJ 0.50 N, GJ 0.60 N) plus the per anastomosis manometry targets (PJ duct 12 mmHg, HJ bile 8 mmHg).
- 32 iteration deterministic Latin hypercube sweep at `src/simulation/iterate_1min.py` (Python) and `src/simulation/runner_1min.rs` (Rust) with 8 dimensional parameter space (vessel angle deviation, pancreatic duct diameter, ring tension perturbation, Daraxonrasib serum at induction, arm 1 hybrid scalpel power, arm 4 NIR ICG dose, coordination master heartbeat jitter, per arm e stop latency perturbation) seeded at 20260513.
- 6 component frozen composite score at `src/metrics/compute_1min.py` with the new Anastomosis quality 0.15 weight relative to the v3.9.1 GBM 5 component score.
- 4 entrant multi vendor LLM tournament agent at `src/llm/compare_agent_1min.py` with four backend support (Ollama, vLLM, Anthropic Claude Opus 4.7, Anthropic Claude Sonnet 4.6) and the versioned tournament prompt at `prompts/comparison_prompt_1min.md`.
- Cross iteration leaderboard at `results/comparison.json` and `results/comparison_report.md` plus per round per iteration CSV at `outputs/comparison/leaderboard.csv` and Round 3 robot vs human CSV at `outputs/comparison_robot_vs_human/leaderboard.csv`.
- Daraxonrasib perioperative trajectory at `src/daraxonrasib/trajectory.py` with the 1 compartment exponential decay model (half life 36 hours) and LLM bound advisory at `src/daraxonrasib/advisory.py` with the 3 way decision logic (T+7d uncomplicated, T+14d complicated, T+21d FRS >= 8 or force time integral > 8 N.s).
- Per iteration Daraxonrasib advisory at `results/daraxonrasib_advisory.json` with the SaMD framing caveat preserved in every advisory.
- Zenodo L0 raw deposition patcher at `src/zenodo/patch_pointers.py` with per iteration pointer JSON and cross iteration manifest plus SHA 256 verification.
- 12 PDAC specific ASCII diagrams at `outputs/diagrams/` (coordination_heartbeat_8arm.txt, vascular_safety_map.txt, anastomosis_target_map.txt, per_arm_tool_assignment.txt, per_phase_activation.txt, per_arm_kinematic_chain.txt, pancrespeed_mechanical.txt, iteration_parameter_space.txt, tournament_leaderboard.txt, daraxonrasib_trajectory.txt, fistula_risk_score_flow.txt, 8_phase_timeline.txt).
- 3 Jupyter analysis notebooks at `notebooks/` (iteration_analysis_1min.ipynb, anastomosis_analysis.ipynb, daraxonrasib_pk_analysis.ipynb).
- 14 smoke tests at `tests/test_smoke.py` covering schemas, safety zone gate, composite score, Daraxonrasib advisory, xyz mapping, and Latin hypercube determinism.
- 9 docs files at `docs/` (architecture_8arm.md, sensor_spec_640ch.md, coordinate_mapping_8arm.md, iteration_design_32.md, comparison_methodology_4vendor.md, multi_arm_coordination_8arm.md, vascular_safety_protocol.md, anastomosis_protocols.md, daraxonrasib_integration.md).
- Cross platform runtime recipes at `README.md` for MacOS Apple Silicon, Windows 11 with WSL2 for the Rust runner, Linux Ubuntu 22.04 LTS with A100 or H100 GPU acceleration, Claude Code CLI, and Claude Code Web.
- 14 BibTeX entries inherited from `paper/instructions/README.md` (4 author prior PDAC papers, kawchak_2026_20113157 GBM 60 second paper, kawchak_2025_18099351 Daraxonrasib historical timeline).
- 9 commit single PR workflow with the 8th commit reserved for CI lint and format error fixes and the 9th commit reserved for repository wide documentation updates.
- Pre commit hook configuration at `.pre-commit-config.yaml` with 8 gates (trailing whitespace, EOF newline, mixed line ending, large file check, ruff format, ruff check, yamllint relaxed, markdownlint) plus the markdownlint config at `.markdownlint.yaml` and the yamllint config at `.yamllint`.
- Cross commit cross reference resolution at `CROSS_REFERENCES.md` documenting the 10 cross reference checks from `commit_06_error_fixes.md`.
- Per file lint and format verification at `lint_verification.md` with the 12 known risk pattern audit.
- Release manifest at `releases/v0.6.0/manifest.json` plus release metrics at `releases/v0.6.0/metrics.json` plus sample seeds at `releases/v0.6.0/sample_seeds.txt` plus Zenodo DOI placeholder at `releases/v0.6.0/zenodo_doi.txt`.
- Sample log at `outputs/logs/iteration_run.txt` capturing the 32 iteration wall clock per iteration timing plus the cross iteration summary statistics.
- Top level `README.md` refreshed with v0.6.0 release badge, PDAC Codegen badge, v0.6.0 PDAC Codegen ASCII snapshot, paper/codegen/ subtree in Repository Structure block, See also pointer to `2030-pdac-1min/paper/codegen/README.md`, updated citation block referencing v0.6.0.

## Contributors

@kevinkawchak
@claude
@openai
@google-gemini

## Notes

- The v0.6.0 PDAC codegen tree at `2030-pdac-1min/paper/codegen/` preserves all formatting invariants: single dashes only throughout the body (no em dashes, no double dashes outside fenced code blocks, no triple dashes); black text only (no color overrides, no inline color spans); plain GitHub Flavored Markdown; ASCII diagrams in .txt files; no SVG for high frequency time series; single trailing newline on every file; LF line endings; UTF-8 encoding without BOM.
- The codegen tree was generated by Claude Code Opus 4.7 1M Max across nine sequential commits within a single PR from the v0.5.0 instruction set at `2030-pdac-1min/paper/instructions/`. The 8th commit (2nd to last) addresses the upstream PR template CI lint and format matrix failure mode and the 9th commit (last) updates the repository top level documentation.
- The CI lint and format matrix on Python 3.10, 3.11, and 3.12 continues to pass. The CI workflow at `.github/workflows/ci.yml` is currently scoped to `2030-gbm-1min/` and the new files under `2030-pdac-1min/paper/codegen/` are outside that scope. The codegen tree internally passes the same gates (ruff format, ruff check, yamllint -d relaxed, markdownlint, pre commit hooks, file size cap 10 MB, Parquet size cap 5 MB) as defense in depth in case the CI scope is expanded.
- All committed PDAC codegen files honor the 10 MB per file cap; the largest committed file is `paper/codegen/README.md` at approximately 12 KB. No Parquet files are committed in the codegen tree; the per iteration L0 raw Parquet (412 MB per iteration, 13.2 GB across 32 iterations) is archived to Zenodo and referenced from `data/iterations/run_NNNNN_L0_raw.zenodo_pointer.json`.
- The PDAC 1 minute codegen variant explicitly addresses 7 of 10 approximations from the v0.4.0 GBM full paper limitations: doubled iterations (16 to 32), multi vendor tournament (single vendor to 3 robots plus 1 human), force time integral cap (added; soft 5.0 N.s, hard 8.0 N.s), 100 kHz force sampling (10x finer than GBM), Daraxonrasib precision oncology integration (new), per vessel safety zones (new; 5 named vessels with no fly soft warning hard stop volumes), and anastomosis ring tension control (new; PJ HJ GJ with +/- 0.05 N target band). The remaining 3 approximations (synthetic patient PAT-PDAC-0001, non deterministic Claude Code generation across re generations, hypothetical 2030 PancreSpeed 1.0 robot platform) are inherited with explicit cross simulation caveats.
- The v0.6.0 codegen tree is intended for real world application alongside Daraxonrasib (if approved) and advanced AI surgical robots in the late 2020s and early 2030s. The on premises LLM control layer (per the parent thesis) is framed as a software function under the FDA Software as a Medical Device framework at anticipated Risk Class III; the per iteration Daraxonrasib advisory is also framed as a SaMD recommendation that a board certified oncologist reviews before any actual restart.
- The work positions the United States to remain Number 1 in the world regarding patient safety, efficacy, and speed benefits in oncological robotic surgeries in clinical trials by extending the FDA 28 April 2026 Real Time Clinical Trials proof of concept program from pharmacology into the surgical theater under the SaMD framework, applied to PDAC (the deadliest major solid tumor) and paired with Daraxonrasib (the pan KRAS inhibitor evaluated in RASolute 302 second line metastatic PDAC and expanded into front line metastatic PDAC via RASolve 301).
- The deterministic seed for the 32 iteration sweep is 20260513. The per iteration seed is `root_seed + iteration_index` where `iteration_index in [0, 31]`. The deterministic seed contract yields bit identical CSV outputs across MacOS Apple Silicon, Windows 11, Linux Ubuntu 22.04 LTS, and Claude Code (CLI / web / IDE).
- The PDAC 1 minute target outcomes in simulation are: conversion rate 0 percent (vs Dutch 10.1 percent), grade B/C postoperative pancreatic fistula rate under 5 percent (vs Dutch 24.4 percent), 90 day mortality under 0.5 percent (vs Dutch 3.9 percent). The v0.6.0 codegen baseline produces a PJ grade B/C combined rate of 15.6 percent which is above the target; future work in `gbm_errors_addressed.md` identifies ring tension control loop tuning as the primary improvement vector toward the target.

## Release title

v0.5.0 - 2030 PDAC 1-Minute 8-Arm Whipple Instructions (with Daraxonrasib Adjuvant Integration)

## Summary

This release lands the v0.5.0 PDAC 1-minute robotic surgery instruction
set at `2030-pdac-1min/paper/instructions/`. The instruction set extends
the v3.9.1 GBM 1-minute variant from
`kevinkawchak/physical-ai-oncology-trials/competitions/instructions/one_minute_variant/`
with PDAC specific sensors at 100 kHz force per arm, an 8 arm Medtronic
PancreSpeed 1.0 hypothetical 2030 platform, vascular safety zones for 5
named vessels (superior mesenteric vein, portal vein, hepatic artery,
celiac axis, superior mesenteric artery), three anastomosis protocols
(pancreaticojejunostomy duct to mucosa, hepaticojejunostomy end to side,
gastrojejunostomy antecolic), and Daraxonrasib precision oncology
adjuvant integration with perioperative pause and LLM bound advisory
restart layer. The instruction set directs a future Claude Code Opus
4.7 1M Max session to generate the full simulation tree at
`2030-pdac-1min/` across nine sequential commits within a single PR.

See CHANGELOG.md for the v0.5.0 details.

## Release title

v0.4.0 - 2030 GBM 1-Minute Full LaTeX Paper (Populated, Overleaf Ready)

## Summary

See CHANGELOG.md for v0.4.0 details; the populated full LaTeX paper lives at
`2030-gbm-1min/paper/full-paper/`.

## Release title

v0.3.0 - 2030 GBM 1-Minute LaTeX Paper Template (Head Start for Downstream Claude Code)

## Summary

See CHANGELOG.md for v0.3.0 details; the LaTeX paper template lives at
`2030-gbm-1min/paper/`.

## Release title

v0.2.0 - 2030 GBM 1-Minute End-to-End Pipeline Outputs

## Summary

See CHANGELOG.md for v0.2.0 details; the outputs tree is reproducible from
the deterministic seed 20260510 and lives at `2030-gbm-1min/outputs/`.

## Release title

v0.1.0 - 2030 GBM 1-Minute Trial Skeleton (First Variant)

## Summary

See CHANGELOG.md for v0.1.0 details; the 4-arm 1-minute glioblastoma trial
first variant lives at `2030-gbm-1min/`.
