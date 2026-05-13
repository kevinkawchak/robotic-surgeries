# Anastomosis Output (v0.6.0)

[![Release](https://img.shields.io/badge/Release-v0.6.0-brightgreen.svg)](../../../../releases.md)
[![Anastomoses](https://img.shields.io/badge/Anastomoses-3-purple.svg)](../../config/anastomosis_targets.yaml)

## Three Anastomosis Targets

| Anastomosis | Phase | Ring tension target (N) | Manometry target (mmHg) | Duration (s) |
|-------------|-------|--------------------------|-------------------------|--------------|
| Pancreaticojejunostomy (duct to mucosa) | 5 | 0.45 +/- 0.05 | 12 +/- 2 | 10 |
| Hepaticojejunostomy (end to side) | 6 | 0.50 +/- 0.05 | 8 +/- 2 | 6 |
| Gastrojejunostomy (antecolic) | 7 | 0.60 +/- 0.05 | n/a | 6 |

## Realized Outcomes Across 32 Iterations

| Anastomosis | Best outcome rate | Worst outcome rate |
|-------------|--------------------|---------------------|
| Pancreaticojejunostomy grade A | 27 of 32 (84.4 percent) | grade B 5 of 32 (15.6 percent), grade C 0 of 32 |
| Hepaticojejunostomy leak absent | 31 of 32 (96.9 percent) | leak present 1 of 32 (3.1 percent) |
| Gastrojejunostomy patent | 31 of 32 (96.9 percent) | delayed 1 of 32 (3.1 percent) |

The PDAC target rate of grade B/C combined < 5 percent is not yet met in the v0.6.0 baseline. Future work in `gbm_errors_addressed.md` identifies ring tension control loop tuning as the primary improvement vector.

## Cross References

- `../../config/anastomosis_targets.yaml` per anastomosis target table.
- `../../src/anastomosis/pancreaticojejunostomy.py` PJ controller.
- `../../src/anastomosis/hepaticojejunostomy.py` HJ controller.
- `../../src/anastomosis/gastrojejunostomy.py` GJ controller.
- `../../../instructions/anastomosis_protocols.md` full protocol.
