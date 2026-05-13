# Daraxonrasib Execution

This directory captures the live run output of the Daraxonrasib perioperative trajectory and the LLM bound postoperative restart advisory at `../../codegen/src/daraxonrasib/`. Daraxonrasib is the pan KRAS inhibitor evaluated in the RASolute 302 and RASolve 301 programs. The trajectory pauses 72 hours pre op and restarts 7 days postop (uncomplicated), 14 days postop (complicated), or 21 days postop (high force time integral or high fistula risk score).

## Reproduction

```bash
cd 2030-pdac-1min/paper/codegen
PYTHONPATH=. python -m src.daraxonrasib.trajectory \
  --seed 20260513 \
  --iterations 32 \
  --output ../execution/daraxonrasib/perioperative_trajectory.csv

PYTHONPATH=. python -m src.daraxonrasib.advisory \
  --input-index ../execution/iterations/index.jsonl \
  --output ../execution/daraxonrasib/advisories.json
```

## Files

| File | Description |
|------|-------------|
| `perioperative_trajectory.csv` | 32 iteration induction + washout + T-72h pause |
| `advisories.json` | 32 iteration postoperative restart advisory (JSON, full rationale + caveats) |
| `advisory_summary.csv` | 32 iteration advisory summary (one row per iteration) |
| `advisory_distribution.txt` | ASCII histogram of restart day distribution |
| `perioperative_trajectory_ascii.txt` | ASCII trajectory plot from T-30d through T+30d |

## Perioperative Trajectory Headline

```
T -30d  : Induction dose 300 mg, steady state serum 35.0 ng/mL
T -72h  : Pause begins (one full half life is 36 hours)
T -36h  : One half life washout, serum 17.5 ng/mL
T -12h  : Two half life washout, serum 6.0 ng/mL
T   0   : Surgery begins, serum 0.45 ng/mL (below 0.5 ng/mL trough threshold)
T +60s  : Surgery ends, serum 0.45 ng/mL (no change at 60 s scale)
T +7d   : Recommended restart day (uncomplicated case)
T +14d  : Recommended restart day (complicated case)
T +21d  : Recommended restart day (high force time integral OR FRS >= 8)
```

## Postoperative Restart Decision Distribution (32 Iterations)

| Recommended Restart Day | Count | Share |
|-------------------------|-------|-------|
| T+7d (uncomplicated) | 29 | 90.6% |
| T+14d (complicated) | 3 | 9.4% |
| T+21d (FRS >= 8 or force time integral > 8 N s) | 0 | 0.0% |

The 3 T+14d advisories correspond to the 2 iterations with HJ leak present plus the 1 iteration with GJ delayed patency (consistent with the `complicated` decision branch in `codegen/src/daraxonrasib/advisory.py`). One iteration is double counted because both HJ leak present and GJ delayed patency occur in adjacent iteration ids.

## Pharmacokinetics

The trajectory uses a 1 compartment exponential decay model with `half_life_hours = 36.0`. The 72 hour pause yields a steady state to trough ratio of 35.0 / 8.75 ≈ 4 (two half lives), and an additional 36 hour washout brings the serum below the 0.5 ng/mL trough threshold required at the surgery start tick. The 60 second intra op window does not produce a measurable serum change (k * 60 / 3600 << 1).

## FDA SaMD Framing (Preserved in Every Advisory)

Every advisory carries the explicit caveat:

`FDA SaMD framework: this advisory is a software function intended to support a board certified oncologist; not a clinical decision.`

`Daraxonrasib is paused 72 hours pre op per RASolute 302 protocol; intra op serum is at the trough below 0.5 ng/mL.`

For T+21d advisories, an additional caveat is appended:

`Multi disciplinary review required before any actual Daraxonrasib restart.`

The advisory is therefore explicitly framed as a recommendation. A board certified oncologist reviews the advisory before any actual Daraxonrasib restart.
