# Daraxonrasib Integration Overview (Perioperative Trajectory)

This document fixes the Daraxonrasib precision oncology adjuvant integration overview. The full protocol lives at `../../instructions/daraxonrasib_integration.md` and the perioperative trajectory lives at `src/daraxonrasib/trajectory.py`. The LLM bound advisory lives at `src/daraxonrasib/advisory.py`.

## Why Daraxonrasib

Daraxonrasib (Revolution Medicines and Roche pan KRAS inhibitor) selectively inhibits the active GTP bound state of KRAS G12X, G13X, and Q61X mutations. The May 2025 RASolute 302 randomized Phase III trial of Daraxonrasib monotherapy versus chemotherapy in second line metastatic PDAC met its primary endpoint of overall survival (preliminary hazard ratio approximately 0.55, median OS approximately 13.5 vs 7.8 months). The October 2025 RASolve 301 expansion enrolled the broader pan KRAS mutation cohort in front line metastatic PDAC. The PDAC 1 minute robotic surgery scenario therefore frames Daraxonrasib as the precision oncology adjuvant that the 60 second robotic Whipple pairs with for the durable cancer survival outcome.

## Perioperative Pause and Restart

The RASolute 302 perioperative protocol pauses Daraxonrasib 72 hours before any major surgical procedure and restarts 7 days postoperatively (uncomplicated recovery) or 14 days postoperatively (complicated recovery). The PDAC 1 minute variant honors this protocol exactly.

| Time relative to surgery | Daraxonrasib dose | Serum (ng/mL) | Action |
|---------------------------|-------------------|----------------|--------|
| T-30 days | 300 mg PO daily | 35 +/- 10 | Standard induction dosing |
| T-72 hours | 0 mg | 35 +/- 10 decaying | Pause |
| T-36 hours | 0 mg | 17 +/- 5 | Single half life washout |
| T-12 hours | 0 mg | 6 +/- 2 | Two half life washout |
| T 0 | 0 mg | < 0.5 | Trough, below active threshold |
| T+60 seconds | 0 mg | < 0.5 | Surgery ends |
| T+7 days (uncomplicated) | 300 mg PO daily | 35 +/- 10 | Restart |
| T+14 days (complicated) | 300 mg PO daily | 35 +/- 10 | Delayed restart |

## LLM Bound Advisory Layer

The LLM bound advisory at `src/daraxonrasib/advisory.py` emits a per iteration advisory on the timing of postoperative Daraxonrasib restart based on the per iteration realized anastomosis quality, the per arm cumulative force exposure, the per iteration realized fistula risk score, and the per iteration realized event log. The advisory is produced at the 60 second mark and is recorded in `results/daraxonrasib_advisory.json`.

Decision logic:

- If realized grade B/C fistula is absent AND all anastomoses stable AND no intraoperative event then recommend T+7d restart.
- If realized grade B/C fistula is present OR any anastomosis unstable OR any intraoperative event then recommend T+14d restart.
- If realized FRS >= 8 OR per arm force time integral > 8.0 N.s then recommend T+21d restart with multi disciplinary review.

## Cross References

- `../../instructions/daraxonrasib_integration.md` fixes the full perioperative protocol.
- `../../instructions/anastomosis_protocols.md` fixes the realized grade classification.
- `../../instructions/multi_arm_coordination_8arm.md` fixes the per arm force time integral.
