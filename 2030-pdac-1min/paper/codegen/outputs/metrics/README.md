# Metrics Output (v0.6.0)

[![Release](https://img.shields.io/badge/Release-v0.6.0-brightgreen.svg)](../../../../releases.md)

## 6 Component Composite Score (Frozen Weights)

| Component | Weight | PancreSpeed mean | da Vinci 2030 | Hugo PDAC 2030 | Dutch human |
|-----------|--------|------------------|----------------|------------------|--------------|
| Quality | 0.30 | 92.20 | 88 | 85 | 82 |
| Time | 0.20 | 100.00 | 78 | 70 | 8 |
| Cost | 0.15 | 79.75 | 70 | 75 | 90 |
| Safety | 0.15 | 95.20 | 90 | 86 | 80 |
| Patient experience | 0.05 | 91.78 | 88 | 84 | 78 |
| Anastomosis quality | 0.15 | 92.65 | 90 | 87 | 82 |
| Composite total | 1.00 | **92.42** | 84.10 | 80.60 | 56.05 |

Weights are frozen across all 4 entrants and 32 iterations. The PancreSpeed 1.0 column is the simulated mean; the other columns are the frozen entrant targets from `competition_protocol.md`.

## Cross References

- `../../src/metrics/compute_1min.py` composite score implementation.
- `../../schemas/metrics.schema.json` composite record schema.
