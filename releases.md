# Release Notes

This file tracks every tagged release of the robotic-surgeries repository.
Releases follow semantic versioning. The first project to land here is the
4-arm 1-minute glioblastoma trial in `2030-gbm-1min/` (project version
v3.9.1, repository release v0.1.0). The v0.2.0 release publishes the
end-to-end run outputs of the same pipeline. The v0.3.0 release lands the
LaTeX paper template for the same project under `2030-gbm-1min/paper/`.
The v0.4.0 release lands the populated full LaTeX paper under
`2030-gbm-1min/paper/full-paper/`. The v0.5.0 release lands the 8-arm
1-minute PDAC instruction set at `2030-pdac-1min/paper/instructions/` for
a future Claude Code Opus 4.7 1M Max session to read and generate the
PDAC simulation tree.

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
The 8th commit (2nd to last) addresses the CI lint and format matrix
failure mode (Cl / lint-and-format Python 3.10 / 3.11 / 3.12) and the
9th commit (last) updates the repository top level documentation.
The PDAC variant explicitly addresses 7 of the 10 approximations
cataloged in the v0.4.0 GBM full paper limitations: doubled iterations
(16 to 32), multi vendor tournament (single vendor to 3 robots plus 1
human), force time integral cap (added), 100 kHz force sampling (10x
finer than GBM), Daraxonrasib precision oncology integration (new), per
vessel safety zones (new), and anastomosis ring tension control (new).
The remaining 3 approximations (synthetic patient, non deterministic
Claude generation, hypothetical 2030 robot) are inherited with explicit
cross simulation caveats. The PDAC variant pairs the 60 second robotic
Whipple with Daraxonrasib (the pan KRAS inhibitor evaluated in the
RASolute 302 and RASolve 301 programs) as the precision oncology
adjuvant to deliver an end to end durable cancer survival outcome
paired with the surgical resection. The CI lint and format gates on
Python 3.10, 3.11, and 3.12 continue to pass because the new files
under `2030-pdac-1min/paper/instructions/` are Markdown only and are
not subject to `ruff format --check`, `ruff check`, or `yamllint -d
relaxed`. No committed file exceeds 10 MB and no committed Parquet
exceeds 5 MB.

## Features

- 21 PDAC instruction files at `2030-pdac-1min/paper/instructions/` totalling approximately 130 KB.
- 8 arm Medtronic PancreSpeed 1.0 hypothetical 2030 robot specification at 100 kHz force, 10 kHz cmd, 3 ms e stop, 50 microsecond per arm park latency, 0.05 mm RMS positioning at 1,200 mm/s, 1,600 mm cubed per second peak tissue removal via hybrid ultrasonic-water-plasma scalpel.
- 640 channel sensor stack (80 channels per arm times 8 arms) covering joint position, joint velocity, joint torque, end effector position, end effector orientation, end effector linear velocity, end effector force at 100 kHz, end effector torque at 100 kHz, tool state, bipolar coag, suction, irrigation, vessel surface proximity, NIR indocyanine green, pancreatic duct manometry, anastomosis ring tension, bile spectrophotometry, ultrasound B mode, heartbeat counter, heartbeat watchdog, per arm tip force, cumulative cross arm tip force, per arm force time integral, engagement depth, e stop state, temperature, power, collision state, tool changer state, task identifier, phase identifier, command queue depth.
- 8 phase 60 second procedure timeline (Phase 1 Kocher 0 to 6 s, Phase 2 vascular control 6 to 16 s, Phase 3 uncinate dissection 16 to 24 s, Phase 4 specimen removal 24 to 32 s, Phase 5 pancreaticojejunostomy 32 to 42 s, Phase 6 hepaticojejunostomy 42 to 48 s, Phase 7 gastrojejunostomy 48 to 54 s, Phase 8 hemostasis verification 54 to 60 s).
- 5 named vessel safety zones (superior mesenteric vein, portal vein, hepatic artery, celiac axis, superior mesenteric artery) with no fly, soft warning, hard stop radii defined per vessel and gated through the 10 kHz command channel rate.
- 3 anastomosis protocols with per anastomosis ring tension target (PJ 0.45 N, HJ 0.50 N, GJ 0.60 N), per anastomosis manometry target (PJ duct 12 mmHg, HJ bile 8 mmHg), and per anastomosis bile spectrophotometry leak detection.
- 32 iteration deterministic sweep with Latin hypercube parameter space (vessel angle deviation, pancreatic duct diameter, ring tension perturbation, Daraxonrasib serum concentration at induction, arm 1 hybrid scalpel power, arm 4 NIR ICG dose, coordination master heartbeat jitter, per arm e stop latency perturbation) and 6 component frozen composite score (Quality 0.30, Time 0.20, Cost 0.15, Safety 0.15, Patient experience 0.05, Anastomosis quality 0.15).
- 4 entrant multi vendor LLM tournament (PancreSpeed 1.0 hypothetical 2030 Medtronic, da Vinci Whipple 2030 hypothetical Intuitive successor, Hugo PDAC 2030 hypothetical Medtronic Hugo successor, Dutch human surgeon baseline from the 2025 nationwide 1000 robotic pancreaticoduodenectomy cohort).
- Daraxonrasib perioperative pause (72 hours pre op) and restart logic (7 days post op if uncomplicated, 14 days if complicated, 21 days if FRS >= 8) with LLM bound advisory layer that emits a per iteration advisory at the 60 second mark grounded in the realized anastomosis quality, per arm cumulative force exposure, per iteration realized FRS, and per iteration realized event log.
- Zenodo archive protocol for the 13.2 GB L0 raw deposition (32 iterations times 412 MB per iteration) with per iteration pointer JSON files plus a cross iteration manifest.
- 7 BibTeX entries embedded at the bottom of the instruction set README (paper-1 Zenodo 17239510 FDA RTCT in silico, paper-2 Zenodo 17001137 QSP metastatic, paper-3 Zenodo 16415815 ChatGPT 100,000 patient, paper-4 Zenodo 15735068 end to end PDAC digital twin, kawchak_2026_20113157 GBM 60 second paper, kawchak_2025_18099351 Daraxonrasib efficient LLM trial simulations).
- 9 commit single PR workflow with 8th commit reserved for error fixes addressing the CI lint matrix and 9th commit reserved for repository updates.
- Cross simulation caveat preserved in 3 of 10 approximations inherited from v3.9.1 GBM (synthetic patient PAT-PDAC-0001, non deterministic Claude generation across runs, hypothetical 2030 robot platform).
- ASCII diagram convention extended with 12 new PDAC specific diagram templates (8 arm coordination heartbeat, vascular safety map, anastomosis target map, per arm tool assignment, per phase activation, kinematic chain, PancreSpeed mechanical schematic, iteration parameter space, tournament leaderboard, Daraxonrasib trajectory, fistula risk score flow, 8 phase timeline).
- Per arm tip force cap tightened from 5.0 N (GBM) to 3.0 N (PDAC). Cumulative cross arm tip force cap loosened from 12.0 N (GBM, 4 arms) to 18.0 N (PDAC, 8 arms). Per arm force time integral cap added (PDAC new floor: soft 5.0 N.s, hard 8.0 N.s). E stop latency tightened from 5 ms (GBM) to 3 ms (PDAC). Per arm park latency tightened from 100 microseconds (GBM) to 50 microseconds (PDAC).
- Heartbeat rate stepped up from 1 kHz (GBM) to 10 kHz (PDAC). Force sample rate stepped up from 10 kHz (GBM) to 100 kHz (PDAC). Command sample rate stepped up from 1 kHz (GBM) to 10 kHz (PDAC).
- markdownlint configuration at `2030-pdac-1min/paper/instructions/.markdownlint.yaml` carried forward from v3.9.1 GBM with one PDAC addition.
- Top level README.md refreshed with v0.5.0 release badge, PDAC variant badge, Daraxonrasib adjuvant badge, v0.5.0 PDAC Instructions ASCII snapshot, 8 arm PDAC coordination snapshot, 2030-pdac-1min/ subtree in Repository Structure block, See also pointer to 2030-pdac-1min/paper/instructions/README.md, citation block referencing v0.5.0.

## Contributors

@kevinkawchak
@claude
@openai
@google-gemini

## Notes

- The 21 PDAC instruction files preserve all formatting invariants: single dashes only throughout the body (no em dashes, no double dashes, no triple dashes); black text only (no color overrides, no inline color spans); plain GitHub Flavored Markdown; ASCII diagrams in .txt files or Mermaid blocks in .md files; no SVG for high frequency time series; single trailing newline on every file; LF line endings; UTF-8 encoding.
- The future Claude Code Opus 4.7 1M Max session that reads this instruction set generates the full `2030-pdac-1min/` simulation tree across nine sequential commits within a single PR per the `pr_workflow.md` specification. The 8th commit (2nd to last) addresses the upstream PR template CI lint and format matrix failure mode (3 failing checks: Cl / lint-and-format Python 3.10, 3.11, 3.12) by running the pre commit hook configuration (ruff format, ruff check, yamllint relaxed, markdownlint, pre commit, file size cap 10 MB, Parquet size cap 5 MB) on every committed file in `2030-pdac-1min/`.
- All committed PDAC instruction files honor the 10 MB per file cap; the largest instruction file is `2030-pdac-1min/paper/instructions/README.md` at approximately 22 KB.
- The work positions the United States to remain Number 1 in the world regarding patient safety, efficacy, and speed benefits in oncological robotic surgeries in clinical trials by extending the FDA 28 April 2026 Real Time Clinical Trials proof of concept program from pharmacology into the surgical theater under the FDA Software as a Medical Device framework, applied to PDAC (the deadliest major solid tumor) and paired with Daraxonrasib (the pan KRAS inhibitor that succeeded in RASolute 302 second line metastatic PDAC and that expanded into front line metastatic PDAC via RASolve 301).
- The 7 BibTeX entries embedded at the bottom of the instruction set README anchor the prior author works (paper-1 Zenodo 17239510, paper-2 Zenodo 17001137, paper-3 Zenodo 16415815, paper-4 Zenodo 15735068, kawchak_2026_20113157 GBM 60 second paper, kawchak_2025_18099351 Daraxonrasib historical timeline) that this PDAC variant builds from.
- The PDAC 1 minute variant explicitly differs from the GBM 1 minute variant in seven concrete ways: 8 arms vs 4 arms (more anastomoses and dissection planes), 100 kHz force vs 10 kHz force (10x finer), 640 sensor channels vs 200 (3.2x more), 32 iterations vs 16 (2x more for tighter 95 percent CI), 4 vendor tournament vs single vendor (closes single vendor gap from v3.9.1), Daraxonrasib integration (new precision oncology adjuvant), and PDAC specific vascular safety + anastomosis protocols (new floor).

## Release title

v0.4.0 - 2030 GBM 1-Minute Full LaTeX Paper (Populated, Overleaf Ready)

## Summary

This release lands the populated full LaTeX paper at
`2030-gbm-1min/paper/full-paper/` titled **2030: 60 Second Glioblastoma AI
Robotic Surgery**. Every bracketed instruction in the v0.3.0 template has
been replaced with prose, tables, and ASCII diagrams grounded in the
upstream `kevinkawchak/physical-ai-oncology-trials/competitions/instructions/one_minute_variant/`
directory, the generated `2030-gbm-1min/` tree, and the end-to-end
execution outputs under `2030-gbm-1min/outputs/`. The populated paper
opens with the on-premises repository based LLM thesis and frames the
work as an opportunistic extension of the FDA 28 April 2026 Real-Time
Clinical Trials announcement from pharmacology into the surgical theater.
The headline result is the robot mean composite score of 88.53 versus
human mean composite 70.35 across the mixed 4-entity LLM tournament,
with the structural-time-dimension caveat (1-minute robot vs 1-hour human
baseline) preserved in every rationale. The exceptional processing feat
that no human team could produce in the time budget is the 54 column by
1001 row sensor sample table at
`2030-gbm-1min/outputs/sensors/sensor_sample_4arm.csv`. The paper Zenodo
DOI is 10.5281/zenodo.20113157 and the parent repository deposition DOI
is 10.5281/zenodo.18445179; both are clickable from the title page and
from the bibliography. The full paper compiles cleanly on Overleaf and
on any local pdflatex plus bibtex installation. A one-command
`build_zip.sh` helper in the same directory produces the Overleaf-ready
`LaTeX Source Files.zip` bundle. The release also refreshes the
top-level `README.md` with the v0.4.0 release badge, the Paper Full
badge, the new full-paper subtree in the Repository Structure block,
a v0.4.0 Full Paper ASCII snapshot, the updated Overleaf compile recipe,
and an updated citation block. The CI lint and format gates on Python
3.10, 3.11, and 3.12 continue to pass because the new files under
`2030-gbm-1min/paper/full-paper/` are LaTeX and Markdown only and are
not subject to `ruff format --check`, `ruff check`, or `yamllint -d
relaxed`. No committed file exceeds 10 MB and no committed Parquet
exceeds 5 MB.

## Features

- Populated full LaTeX paper under `2030-gbm-1min/paper/full-paper/` titled **2030: 60 Second Glioblastoma AI Robotic Surgery**. Title page carries the two-line centered title, the green ORCID logo plus https://orcid.org/0009-0007-5457-8667, CEO ChemicalQDevice, the clickable Zenodo DOI 10.5281/zenodo.20113157, the May 11 2026 release date, the abstract, the mandatory disclaimer, and the keywords.
- 8 populated `sections/*.tex` files: `abstract.tex`, `introduction.tex`, `methods.tex`, `results.tex`, `discussion.tex`, `limitations_future.tex`, `conclusions.tex`, `back_matter.tex`.
- See the v0.4.0 CHANGELOG.md entry for the full feature inventory.

## Contributors

@kevinkawchak
@claude
@openai
@google-gemini

## Notes

- See the v0.4.0 CHANGELOG.md entry for the full notes block.

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
