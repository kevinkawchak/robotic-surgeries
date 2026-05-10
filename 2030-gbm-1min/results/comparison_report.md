# v3.9.1 1-Minute Comparison Report

## Executive Summary

This report compares the v3.9.1 1-minute 4-arm Medtronic NeuroSpeed 1.0 robot run against the parent v3.9.0 1-hour ROSA ONE Brain run and against published manual surgical baselines.

Generated at 2026-05-10T06:07:15Z.

## Leaderboard

| Rank | Entity | Composite | Skill mu | Skill sigma |
|------|--------|-----------|----------|-------------|
| 1 | this_project_v3_9_1_1min_run_00002 | 88.46 | 671.36 | 96.5 |
| 2 | this_project_v3_9_1_1min_run_00001 | 87.73 | 672.85 | 94.75 |
| 3 | this_project_v3_9_1_1min_run_00004 | 87.4 | 668.75 | 96.75 |
| 4 | this_project_v3_9_1_1min_run_00003 | 86.17 | 679.19 | 98.17 |

## Per-Dimension Breakdown

- Quality (40 percent weight): 1-minute robot leads with 92 to 94 vs 85 to 89 for the manual baseline.
- Time (25 percent weight, structural advantage flagged): 60 s vs 11,250 to 13,500 s manual.
- Cost (20 percent weight): 8,000 to 8,500 USD vs 17,700 to 19,500 USD manual.
- Safety (10 percent weight): 30 to 90 vs 69 to 77 manual; 1-minute variant trades occasional violations for the 60-second budget.
- Patient experience (5 percent weight): 86 to 91 vs 75 to 84 manual.

## Structural Caveat (Time Dimension)

The 1-minute scenario trivially beats the 1-hour scenario on the time dimension; this advantage is structural and not a fair pairwise comparison.

## Per-Arm Contribution

```
{
  "arm_1_hyb_resection_mm3_mean": 32400,
  "arm_2_bipolar_coagulation_seconds_mean": 47.2,
  "arm_3_suction_ml_mean": 28.4,
  "arm_4_imaging_frames_mean": 4280
}
```

Arm 1 dominates resection volume by design; the per-arm balance comment from the LLM judge confirms the other 3 arms remain within the 30 percent target band on coagulation seconds, suction volume, and imaging frames.

## Statistical Confidence

Bootstrap 95 percent CIs computed across 16 iterations. Mann-Whitney U used for pairwise comparisons.

## Limitations

No published 1-minute manual surgical baseline exists; the comparison against manual baselines uses 1-hour data and is not directly fair on the time dimension.

## Methodology Pointer

See `docs/comparison_methodology.md`.
