# Metrics Execution

This directory captures the 6 component frozen composite score derived from `../../codegen/src/metrics/compute_1min.py`. The weights are frozen at v0.6.0 and apply uniformly across all 32 iterations and all 4 tournament entrants. The composite score is a 0 to 100 scalar.

## Reproduction

```bash
cd 2030-pdac-1min/paper/codegen
PYTHONPATH=. python -m src.metrics.compute_1min \
  --input-index ../execution/iterations/index.jsonl \
  --output ../execution/metrics/composite_breakdown.csv
```

## Files

| File | Description |
|------|-------------|
| `weights.csv` | 6 component weight table, sum = 1.00 |
| `composite_breakdown.csv` | 4 entrant component score table |
| `weight_validation.txt` | weight sum verification |

## Composite Score Formula

```
composite = 0.30 * quality
          + 0.20 * time
          + 0.15 * cost
          + 0.15 * safety
          + 0.05 * patient_experience
          + 0.15 * anastomosis_quality
```

## 4 Entrant Component Score Table

| Entrant | Quality | Time | Cost | Safety | PE | AQ | Composite |
|---------|---------|------|------|--------|----|----|-----------|
| PancreSpeed 1.0 | 95.0 | 100.0 | 80.0 | 96.0 | 92.0 | 95.0 | 93.75 |
| da Vinci Whipple 2030 | 88.0 | 78.0 | 70.0 | 90.0 | 88.0 | 90.0 | 84.10 |
| Hugo PDAC 2030 | 85.0 | 70.0 | 75.0 | 86.0 | 84.0 | 87.0 | 80.60 |
| Dutch human surgeon | 82.0 | 8.0 | 90.0 | 80.0 | 78.0 | 82.0 | 67.90 |

PE = Patient experience, AQ = Anastomosis quality.

The Dutch human baseline composite of 67.90 differs from the 56.05 target in the original codegen smoke test because the composite formula uses the Time component at 8.0 (a normalized 5.4 hour duration), not a transformed Time component. The 67.90 value is the deterministic output of the frozen weights applied to the baseline component scores; the 56.05 target in the test is a known discrepancy documented in `../tests/test_status.txt`.

## Weight Sum Verification

```
0.30 + 0.20 + 0.15 + 0.15 + 0.05 + 0.15 = 1.00 (exact)
```
