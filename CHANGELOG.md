# Changelog

All notable changes to this repository are documented in this file.
Format: Keep a Changelog. Versioning: Semantic Versioning.

## v0.5.0 - 2026-05-13

### Added

- `2030-pdac-1min/paper/instructions/` directory containing the v0.5.0 PDAC 1-minute robotic surgery instruction set. New files: `README.md` (top level orientation with 7 bibtex entries), `pdac_context_1min.md` (PAT-PDAC-0001 plus 8 phase 60 second timeline plus vascular anatomy plus three anastomosis targets), `robot_specification_pancrespeed.md` (hypothetical 2030 Medtronic PancreSpeed 1.0 eight arm specification), `sensor_specification_100khz.md` (640 channel sensor stack at 100 kHz force plus 10 kHz command), `multi_arm_coordination_8arm.md` (10 kHz heartbeat broadcast with 100 microsecond watchdog and 3 ms cross arm e stop), `file_size_pyramid_1min.md` (5 layer per iteration pyramid: L1 publication sample, L2 1 Hz aggregate, L3 per phase, L4 per anastomosis, event log), `chunking_strategy.md` (6 chunking layers including the PDAC specific L4 anastomosis and daraxonrasib trajectory layer), `file_format_conventions.md` (Parquet zstd-3 default plus UTF-8 LF line endings), `ascii_diagram_guide.md` (12 PDAC specific ASCII diagram templates), `competition_protocol.md` (4 entrant multi vendor tournament: PancreSpeed 1.0 vs da Vinci Whipple 2030 vs Hugo PDAC 2030 vs Dutch human surgeon baseline), `runtime_environments.md` (MacOS Apple Silicon, Windows 11, Linux Ubuntu 22.04 LTS, Claude Code CLI, Claude Code Web), `ci_compliance_checklist.md` (8 lint and format gates), `pr_workflow.md` (9 commit single PR with 8th commit reserved for error fixes and 9th commit reserved for repository updates), `vascular_safety_protocol.md` (5 named vessel no fly soft warning hard stop volumes), `anastomosis_protocols.md` (3 anastomosis protocols with ring tension and manometry targets), `daraxonrasib_integration.md` (perioperative pause and restart logic plus LLM bound advisory layer), `gbm_errors_addressed.md` (catalog of 7 of 10 v0.4.0 GBM approximations addressed by PDAC), `zenodo_archive_protocol.md` (13.2 GB L0 deposition manifest contract), `commit_01_overview_1min.md`, `commit_02_sensors_1min.md`, `commit_03_xyz_8arm.md` (8 arm Cartesian xyz mapping with per arm 7 DOF DH parameter table), `commit_04_iterations_1min.md` (32 iteration deterministic sweep with Latin hypercube parameter space), `commit_05_competition_1min.md`, `commit_06_error_fixes.md`, `commit_07_repository_updates.md`, `lint_verification.md` (this PR's commit 8 verification log), `.markdownlint.yaml` (markdownlint config).
- 7 BibTeX entries embedded at the bottom of `2030-pdac-1min/paper/instructions/README.md`: 4 author prior PDAC papers (paper-1 Zenodo 17239510, paper-2 Zenodo 17001137, paper-3 Zenodo 16415815, paper-4 Zenodo 15735068), 1 prior 60 second glioblastoma robotic surgery paper (kawchak_2026_20113157 Zenodo 20113157), 1 Daraxonrasib historical timeline (kawchak_2025_18099351 Zenodo 18099351). All entries follow the cite key plus author plus title plus month plus year plus publisher plus doi plus url BibTeX field schema.
- v0.5.0 release badge, PDAC variant badge, Daraxonrasib adjuvant badge, PDAC Instructions badge in the top level `README.md`.
- v0.5.0 PDAC Instructions ASCII snapshot in the top level `README.md` above the v0.4.0 Full Paper ASCII snapshot.
- 8 arm PDAC Coordination Snapshot ASCII in the top level `README.md` next to the 4 arm GBM Coordination Snapshot.
- `2030-pdac-1min/` subtree expanded in the top level `README.md` Repository Structure block to show the 25 file paper/instructions/ contents plus the 7 paper/inputs/ subdirectories.
- High Level Architecture ASCII diagram in the top level `README.md` extended with the 2030-pdac-1min/ tree pointing at the on prem LLM tournament agent.
- This v0.5.0 entry in `CHANGELOG.md` plus the matching `releases.md` block.

### Changed

- Top level `README.md` updated with v0.5.0 release badge, PDAC variant badge, Daraxonrasib adjuvant badge, v0.5.0 PDAC Instructions ASCII snapshot, 8 arm PDAC coordination snapshot, 2030-pdac-1min/ subtree in Repository Structure block, See also pointer to `2030-pdac-1min/paper/instructions/README.md`, updated citation block referencing v0.5.0 plus the kawchak_2025_18099351 Daraxonrasib historical timeline citation.
- `releases.md` prepended with v0.5.0 release notes block per the FORMAT (Release title / Summary / Features / Contributors / Notes).
- @kevinkawchak added the `2030-pdac-1min/paper/inputs/` chunked input research papers (paper-1 through paper-4 PDAC papers, daraxonrasib-1 summary, research-1 daraxonrasib clinical trial historical timeline, research-2 Whipple procedure evidence baseline) on 2026-05-11 and 2026-05-12.
- @claude (this session) authored the v0.5.0 PDAC instruction set at `2030-pdac-1min/paper/instructions/` across nine sequential commits within a single PR on 2026-05-13.

### Fixed

- CI lint and format matrix on Python 3.10, 3.11, and 3.12 continues to pass. The 25 new files under `2030-pdac-1min/paper/instructions/` are Markdown only plus one YAML config (`.markdownlint.yaml`) and are not subject to `ruff format --check` or `ruff check`. The `.markdownlint.yaml` is gated by `yamllint -d relaxed` and passes. Resolves the upstream `Cl / lint-and-format (3.10)`, `(3.11)`, and `(3.12)` failing checks risk for this PR.
- The 8th commit (2nd to last in this 9 commit single PR) at `2030-pdac-1min/paper/instructions/lint_verification.md` documents the per file lint and format verification across all 21 instruction Markdown files plus the .markdownlint.yaml config: single dashes only (no em dashes, no double dashes, no triple dashes), black text only, LF line endings, UTF-8 encoding without BOM, single trailing newline, file size under 25 KB.
- File size cap check passes; no committed file exceeds 10 MB. The largest new file is `2030-pdac-1min/paper/instructions/README.md` at approximately 22 KB.
- Parquet size cap check passes; no committed Parquet exceeds 5 MB. The PDAC instruction set does not commit any Parquet files; Parquet files will be committed by the future Claude Code session that generates the 2030-pdac-1min/ simulation tree.
- Cross file reference resolution passes; every relative path reference in every instruction file resolves to an actual file in `2030-pdac-1min/paper/instructions/`. The cross reference matrix is documented in `lint_verification.md`.

### Notes

- The 21 PDAC instruction files preserve all formatting invariants: single dashes only, black text only, plain GitHub Flavored Markdown, ASCII diagrams in `.txt` files or Mermaid blocks in `.md` files, no SVG for high frequency time series, single trailing newline, LF line endings, UTF-8 encoding without BOM.
- The future Claude Code Opus 4.7 1M Max session that reads this instruction set generates the full `2030-pdac-1min/` simulation tree across nine sequential commits within a single PR per the `pr_workflow.md`. The 9 commits are: (1) project overview docs configs, (2) sensors, (3) xyz mapping, (4) iterations, (5) competition, (6) vascular safety + anastomosis, (7) Daraxonrasib + Zenodo + viz, (8) error fixes for CI lint matrix, (9) repository updates.
- The PDAC variant addresses 7 of 10 approximations from the v0.4.0 GBM full paper limitations: doubled iterations (16 to 32), multi vendor tournament (single vendor to 3 robots plus 1 human), force time integral cap (added), 100 kHz force sampling (10x finer than GBM), Daraxonrasib precision oncology integration (new), per vessel safety zones (new), and anastomosis ring tension control (new). The remaining 3 approximations (synthetic patient, non deterministic Claude generation, hypothetical 2030 robot) are inherited with explicit cross simulation caveats.
- The work positions the United States to remain Number 1 in the world regarding patient safety, efficacy, and speed benefits in oncological robotic surgeries in clinical trials by extending the FDA 28 April 2026 Real Time Clinical Trials proof of concept program from pharmacology into the surgical theater under the FDA Software as a Medical Device framework, applied to PDAC (the deadliest major solid tumor with five year overall survival below 13 percent and a 2025 Dutch nationwide cohort 1000 robotic pancreaticoduodenectomy mean ideal outcome rate of 47 percent) and paired with Daraxonrasib (the pan KRAS inhibitor evaluated in RASolute 302 second line metastatic PDAC and that expanded into front line metastatic PDAC via RASolve 301).
- The PDAC 1 minute target outcomes in simulation are: conversion rate 0 percent (vs Dutch 10.1 percent), grade B/C postoperative pancreatic fistula rate under 5 percent (vs Dutch 24.4 percent), 90 day mortality under 0.5 percent (vs Dutch 3.9 percent), with the structural caveat that simulation against simulation is held against the 2025 Dutch cohort numbers as the human baseline.
- The deterministic seed for the future generated 32 iteration sweep is 20260513. The per iteration seed is derived as `root_seed + iteration_index` where `iteration_index in [0, 31]`.

## v0.4.0 - 2026-05-11

### Added

- `2030-gbm-1min/paper/full-paper/` populated full LaTeX paper for **2030: 60 Second Glioblastoma AI Robotic Surgery**. New files: `main.tex` (preamble, title page, TOC, section input wiring), `new_paper.sty` (carried forward verbatim from the v0.3.0 template), `references.bib` (carried forward verbatim from the v0.3.0 template), `README.md` (DOI badges, ASCII pipeline diagram, section inventory, reference inventory, compile recipe, formatting invariants, senior-author final-pass checklist), `build_zip.sh` (one-command helper that produces the Overleaf-ready `LaTeX Source Files.zip` bundle), and 8 populated `sections/*.tex` files (`abstract.tex`, `introduction.tex`, `methods.tex`, `results.tex`, `discussion.tex`, `limitations_future.tex`, `conclusions.tex`, `back_matter.tex`).
- Every bracketed instruction in the v0.3.0 template has been replaced with prose, tables, and ASCII diagrams grounded in the upstream `physical-ai-oncology-trials/competitions/instructions/one_minute_variant/` directory, the generated `2030-gbm-1min/` tree, and the end-to-end execution outputs under `2030-gbm-1min/outputs/` (including the 54 column by 1001 row sensor sample table at `outputs/sensors/sensor_sample_4arm.csv`).
- 1 raggedright comparison table for ROSA ONE Brain v3.0 vs hypothetical NeuroSpeed 1.0 (introduction); 1 per-arm 7-DOF DH parameter table (methods); 1 sensor-sample slice (methods); 1 per-arm command-state distribution table (methods); 1 per-platform wall-clock table (methods); 1 instruction-file inventory table (results); 1 per-iteration sweep table (results); 2 LLM tournament leaderboards (results); 1 realized-benefits table (discussion); 1 4-arm cross-check matrix (discussion); 1 checking-step head-start table (discussion); 1 three-way accounting table (limitations); 1 60-min vs 1-min delta table (limitations); 1 Track A vs Track B trade-off table (limitations). Every table uses the `{>{\raggedright\arraybackslash}p{Xcm}}` column type with the mandatory `\raggedright\arraybackslash` prefix on every column width value.
- 4-arm coordination heartbeat ASCII snapshot embedded in introduction.tex; ASCII pipeline diagram embedded in the full-paper README.
- Top-level README.md refreshed to include the v0.4.0 release badge, the new Paper Full badge that points at `2030-gbm-1min/paper/full-paper`, the new v0.4.0 Full Paper ASCII snapshot above the v0.3.0 Paper Template snapshot, the new full-paper subtree in the Repository Structure block, the updated Overleaf compile recipe pointing at `2030-gbm-1min/paper/full-paper/`, the new `build_zip.sh` recipe, and the updated citation block referencing v0.4.0.
- This v0.4.0 entry in `CHANGELOG.md` plus the matching `releases.md` block.

### Changed

- Top-level `README.md` updated with v0.4.0 release badge, Paper Full badge, v0.4.0 Full Paper ASCII snapshot, full-paper subtree in the Repository Structure block, Overleaf compile recipe pointing at `2030-gbm-1min/paper/full-paper/`, `build_zip.sh` helper recipe, citation block referencing v0.4.0, and `2030-gbm-1min/paper/full-paper/README.md` cross-reference under See also.
- `2030-gbm-1min/README.md` Repository Tree block annotated with the new `paper/full-paper/` subdirectory contents (main.tex, new_paper.sty, references.bib, build_zip.sh, sections/*.tex, README.md).
- `2030-gbm-1min/paper/README.md` updated with a pointer to the populated `full-paper/` subdirectory plus a one-line description of the build_zip.sh helper.
- @kevinkawchak added LaTeX source files and LaTeX zip file to main/2030-gbm-1min/paper/full-paper/final-paper on 2026-05-11.
- @kevinkawchak added paper-1, paper-2, paper-3, and paper-4 chunked files and README files to robotic-surgeries/tree/main/2030-pdac-1min/paper/inputs on 2026-05-11 and 2026-05-12.
- @kevinkawchak added research-1 chunked files and README files to robotic-surgeries/tree/main/2030-pdac-1min/paper/inputs/research-1 and inputs/research-2 on 2026-05-12.

### Fixed

- Populated LaTeX paper compiles cleanly under Overleaf and a local `pdflatex` plus `bibtex` installation. The 2nd-to-last commit (error fixes) adds the `build_zip.sh` helper that builds the Overleaf-ready zip deterministically from the LaTeX sources committed under `2030-gbm-1min/paper/full-paper/`, verifies all tables use the `{>{\raggedright\arraybackslash}p{Xcm}}` column type, verifies every body section uses single dashes only (no em dashes, no double dashes, no triple dashes), and verifies every `.bib` entry carries a `doi` field plus a `url` field plus a `note` field with clickable GitHub and Zenodo URLs for repository-style entries.
- The CI lint-and-format matrix on Python 3.10, 3.11, and 3.12 continues to pass; the new files under `2030-gbm-1min/paper/full-paper/` are LaTeX and Markdown plus one shell script and are not subject to `ruff format --check`, `ruff check`, or `yamllint -d relaxed`. Resolves the upstream `Cl / lint-and-format (3.10)`, `(3.11)`, and `(3.12)` failing checks risk for this PR.
- File size cap check passes; no committed file exceeds 10 MB and no committed Parquet exceeds 5 MB. The largest new file is `2030-gbm-1min/paper/full-paper/references.bib` at approximately 19 KB.

### Notes

- See the v0.4.0 Notes section of releases.md for the full notes block, the 9 formatting invariants checklist, the Overleaf-ready LaTeX Source Files.zip recipe, the paper DOI 10.5281/zenodo.20113157, and the FDA Real Time Clinical Trials framing.

## v0.3.0 - 2026-05-11

### Added

- `2030-gbm-1min/paper/` LaTeX paper template (head start for a future Claude Code Opus 4.7 1M Max processing pass). New files: `main.tex` (title page, TOC, document structure), `new_paper.sty` (11 pt body, 1 in margins, ptm/phv font pair, widow/orphan suppression, raggedright tables, small-caps Abstract heading), `references.bib` (DOI + URL bearing bibliography with clickable GitHub and Zenodo URLs preserved in the note field), `README.md` (navigation index, compile recipe, formatting invariants, senior-author final-pass checklist), and the eight `sections/*.tex` files (`abstract.tex`, `introduction.tex`, `methods.tex`, `results.tex`, `discussion.tex`, `limitations_future.tex`, `conclusions.tex`, `back_matter.tex`).
- See the v0.3.0 releases.md block for the full inventory.

### Changed

- See the v0.3.0 releases.md block for the full changed list.

### Fixed

- See the v0.3.0 releases.md block for the full fixed list.

### Notes

- See the v0.3.0 releases.md block for the full notes.

## v0.2.0 - 2026-05-10

See the v0.2.0 entry in the prior version of CHANGELOG.md for the v3.9.1 outputs tree under `2030-gbm-1min/outputs/`.

## v0.1.0 - 2026-05-10

See the v0.1.0 entry in the prior version of CHANGELOG.md for the 4-arm 1-minute glioblastoma trial first variant under `2030-gbm-1min/`.
