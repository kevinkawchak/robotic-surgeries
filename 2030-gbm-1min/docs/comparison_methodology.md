# Comparison Methodology (v3.9.1, 4-Arm 1-Minute Variant)

## Comparison Goal

Rank this project's 1-minute robot run against the parent v3.9.0 1-hour ROSA ONE Brain run, against prior v3.9.1 release snapshots, and against published manual surgical baselines across quality, time, cost, safety, and patient experience.

## Metric Definitions

- Quality (40 percent weight): composite of resection completeness percentage, eloquent cortex preservation score, and PSL Omniscient and Omnipresent dimensions.
- Time (25 percent weight): total seconds from procedure start to final E-stop or COMPLETE state. The 1-minute variant trivially beats the 1-hour parent on this dimension; the comparison report calls this out as structural and not a fair pairwise comparison.
- Cost (20 percent weight): consumables, robot depreciation amortized over expected lifetime use, OR time, anesthesia time. Liquid nitrogen cooling consumables for the NeuroSpeed 1.0 contribute additional cost.
- Safety (10 percent weight): inverse of (per-arm force violation count plus cumulative force violation count plus E-stop count plus AE count plus heartbeat miss count).
- Patient experience (5 percent weight): predicted post-operative KPS at 30 days from a fixed regression model.

## Composite Score Formula

```
composite_score = 0.40 * quality_score
                + 0.25 * (100 - normalized_time_score)
                + 0.20 * (100 - normalized_cost_score)
                + 0.10 * safety_score
                + 0.05 * patient_experience_score
```

Weights are frozen at v3.9.1 and match v3.9.0.

## Skill Rating Model

Gaussian N(mu, sigma squared) with mu_0 = 600 and sigma_0 = 200, mirroring the Orbit Wars Kaggle competition and the parent v3.9.0. Per-round update follows TrueSkill-style draw and victory probability rules.

## Multi-Round Tournament Structure

Default tournament size 4 for the 1-minute variant due to the smaller iteration count of 16; scalable to 8 if iterations scale to 32. The tournament generates 6 pairwise rounds at size 4 (C(4, 2)).

## Per-Arm Contribution Analysis

Which of the 4 arms contributed the most tissue removal, the most coagulation work, the most suction volume, the most imaging frames, and which had the highest force violation rate. The per-arm contribution chart in `viz/per_arm_contribution.png` plots the per-iteration distribution per arm.

## Statistical Methods

- Bootstrap 95 percent confidence intervals across 16 iterations.
- Mann-Whitney U for pairwise comparisons.

## Cross-References

- `prompts/comparison_prompt_1min.md`: versioned LLM prompt used by the comparison agent.
- `src/metrics/compute_1min.py`: per-iteration metric computation.
- `src/llm/compare_agent_1min.py`: tournament agent that calls the on-prem LLM (claude-opus-4-7 default).
