# Daraxonrasib Integration (Precision Oncology Adjuvant)

This file fixes the Daraxonrasib precision oncology adjuvant integration for the PDAC 1 minute variant. The future Claude Code Opus 4.7 1M Max session reads this file to author the perioperative trajectory pipeline at 2030-pdac-1min/src/daraxonrasib/trajectory.py, the LLM bound advisory layer at 2030-pdac-1min/src/daraxonrasib/advisory.py, and the per iteration Daraxonrasib event tracking at 2030-pdac-1min/data/iterations/run_NNNNN_daraxonrasib.parquet.

## Why Daraxonrasib Integration Is the PDAC Differentiator

Daraxonrasib (formerly RMC-6236, Revolution Medicines and Roche pan KRAS inhibitor) is a small molecule pan KRAS inhibitor that selectively inhibits the active GTP bound state of KRAS G12X, G13X, and Q61X mutations. The May 2025 RASolute 302 randomized Phase III trial of Daraxonrasib monotherapy versus chemotherapy in second line metastatic PDAC met its primary endpoint of overall survival (preliminary HR approximately 0.55, median OS approximately 13.5 vs 7.8 months). The October 2025 RASolve 301 expansion enrolled the broader pan KRAS mutation cohort in front line metastatic PDAC versus chemotherapy with chemo plus Daraxonrasib combination arms. As of May 2026, the FDA accelerated approval review for Daraxonrasib in second line KRAS G12 mutant metastatic PDAC is anticipated by Q4 2026; the full approval review is anticipated by Q2 2027. The PDAC 1 minute robotic surgery scenario therefore frames Daraxonrasib as the precision oncology adjuvant that the 60 second robotic Whipple pairs with for the durable cancer survival outcome.

## Why Perioperative Pause and Restart Logic

Daraxonrasib has a half life of approximately 36 hours and is associated with reversible cutaneous, hepatic, and gastrointestinal adverse events. The RASolute 302 perioperative protocol pauses Daraxonrasib 72 hours before any major surgical procedure to allow the serum concentration to fall below the active threshold and to allow any cutaneous, hepatic, or gastrointestinal adverse event to resolve. The protocol restarts Daraxonrasib 7 days postoperatively if the surgical recovery is uncomplicated (no grade B or C pancreatic fistula, no major hemorrhage, no sepsis) and 14 days postoperatively if the surgical recovery involves any of these complications. The PDAC 1 minute variant honors this protocol exactly; the simulation does not administer Daraxonrasib intraoperatively, and the intraoperative serum concentration is at the trough level (below 0.5 ng/mL).

## Perioperative Trajectory Table

The perioperative Daraxonrasib trajectory for PAT-PDAC-0001 is fixed in the table below. The trajectory is identical across all 32 iterations and is part of the deterministic seed contract.

| Time relative to surgery | Daraxonrasib dose | Serum concentration target (ng/mL) | Action |
|---------------------------|-------------------|-------------------------------------|--------|
| T-30 days | 300 mg PO daily | 35 +/- 10 | Standard induction dosing |
| T-7 days | 300 mg PO daily | 35 +/- 10 | Continued standard dosing |
| T-72 hours (pre op pause) | 0 mg | 35 +/- 10 (decaying) | Pause Daraxonrasib administration |
| T-36 hours | 0 mg | 17 +/- 5 (decayed by 1 half life) | Single dose washout monitoring |
| T-12 hours | 0 mg | 6 +/- 2 (decayed by 2 half lives) | Continued washout |
| T 0 (intraoperative) | 0 mg | < 0.5 (trough, below active threshold) | Surgical procedure begins |
| T+60 seconds (intraoperative end) | 0 mg | < 0.5 (trough) | Surgical procedure ends |
| T+24 hours postop | 0 mg | < 0.5 (trough) | Postop monitoring |
| T+72 hours postop | 0 mg | < 0.5 (trough) | Anastomosis assessment |
| T+7 days postop (if uncomplicated) | 300 mg PO daily | 35 +/- 10 (re inducting) | Restart Daraxonrasib |
| T+14 days postop (if complicated) | 300 mg PO daily | 35 +/- 10 (delayed re inducting) | Restart Daraxonrasib with caveat |

The per iteration Daraxonrasib trajectory is recorded in 2030-pdac-1min/data/iterations/run_NNNNN_daraxonrasib.parquet as a single row per iteration with the following fields: iteration_id, seed, induction_dose_mg, induction_serum_ng_per_ml, t_minus_72h_pause_applied, t_zero_serum_ng_per_ml, t_plus_60_seconds_serum_ng_per_ml, t_plus_7d_restart_recommended, t_plus_14d_restart_recommended, restart_recommendation_rationale.

## LLM Bound Advisory Layer

The LLM bound advisory layer at 2030-pdac-1min/src/daraxonrasib/advisory.py emits a per iteration advisory on the timing of postoperative Daraxonrasib restart based on the per iteration realized anastomosis quality, the per arm cumulative force exposure, the per iteration realized fistula risk score, and the per iteration realized event log. The advisory is produced at the 60 second mark of the simulation (T+60 seconds) and is recorded in 2030-pdac-1min/results/daraxonrasib_advisory.json.

The advisory prompt is reproduced in skeleton below. The future Claude Code session fills in the per iteration inputs.

```
You are the on premises LLM advisor for the PDAC 1 minute robotic surgery.
You will emit a per iteration advisory on the timing of postoperative
Daraxonrasib restart.

Inputs:
  - per iteration realized FRS (0 to 10)
  - per iteration realized grade B/C fistula classification
  - per arm cumulative force exposure (N.s)
  - per iteration realized event log (e stop, collision, vessel hard stop)
  - per anastomosis ring tension stability (RMSE from target)
  - per anastomosis manometry stability (RMSE from target)
  - per anastomosis bile spectrophotometry signal (max 410 nm above baseline)

Decision logic:
  - If realized grade B/C fistula = absent AND all anastomoses stable AND no
    intraoperative event => recommend T+7d Daraxonrasib restart
  - If realized grade B/C fistula = present OR any anastomosis unstable OR
    any intraoperative event => recommend T+14d Daraxonrasib restart
  - If realized FRS >= 8 OR per arm force time integral > 8.0 N.s =>
    recommend T+21d Daraxonrasib restart with multi disciplinary review

Emit a JSON advisory with fields:
  iteration_id: integer
  recommended_restart_day: 7, 14, or 21
  rationale: 200 word prose grounded in the per iteration L4 anastomosis data
  caveats: list of strings
```

The advisory is intended as a software function under the FDA SaMD framework. The advisory is not a clinical decision; it is a recommendation that a board certified oncologist reviews before any actual Daraxonrasib restart.

## RASolute 302 and RASolve 301 Protocol Anchors

The perioperative trajectory and the LLM bound advisory layer are anchored in the RASolute 302 and RASolve 301 protocol documents. The protocol documents are not committed to this repository (they are proprietary to Revolution Medicines and Roche). The PDAC 1 minute variant inherits the perioperative pause and restart logic from the publicly disclosed protocol summary in the Daraxonrasib historical timeline at 2030-pdac-1min/paper/inputs/research-1/.

## ASCII Trajectory

The Daraxonrasib perioperative trajectory ASCII is reproduced below for orientation. The future Claude Code session generates the equivalent at 2030-pdac-1min/outputs/diagrams/daraxonrasib_trajectory.txt.

```
+============================================================================+
|     DARAXONRASIB PERIOPERATIVE TRAJECTORY (PAT-PDAC-0001, 300 mg PO QD)    |
+============================================================================+
|                                                                            |
|  serum (ng/mL)                                                             |
|        35.0 +--------+                                                     |
|             |        |                                                     |
|             |        |\                                                    |
|        17.5 |        | \\                                                   |
|             |        |  \\                                                  |
|             |        |   \\___                                              |
|         6.0 |        |       \___                                          |
|             |        |           \___                                      |
|         0.5 |        |               \____________ . . . . . _____________ |
|             +--------+--------+-----+-----+------+-----------+-------------+
|             T-30d T-72h    T-36h  T-12h T 0  T+60s        T+7d (or T+14d) |
|                  PAUSE                  TROUGH        RESTART  RESTART     |
|                                                                            |
|  legend: solid line = on drug, dashed line = paused, after surgery line    |
|          dotted then solid line = restart                                  |
|          half life approximately 36 hours; 2 half lives clears below 0.5  |
|          ng/mL active threshold; trough maintained intraoperatively       |
+============================================================================+
```

## Cross References

- pdac_context_1min.md fixes the Daraxonrasib eligibility for PAT-PDAC-0001.
- anastomosis_protocols.md fixes the realized grade classification that the advisory consumes.
- multi_arm_coordination_8arm.md fixes the per arm force time integral that the advisory consumes.
- competition_protocol.md fixes the on premises LLM backend that the advisory uses.
- commit_04_iterations_1min.md fixes the per iteration Daraxonrasib trajectory Parquet schema.
- commit_05_competition_1min.md fixes the advisory prompt at prompts/daraxonrasib_advisory_prompt.md.
