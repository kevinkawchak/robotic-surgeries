# Anastomosis Protocols Overview (3 Anastomoses)

This document fixes the 3 anastomosis protocol overview. The full protocols live at `../../instructions/anastomosis_protocols.md` and the three per anastomosis controllers live at `src/anastomosis/`.

## Three Anastomosis Targets

| Anastomosis | Ring tension target (N) | Manometry target (mmHg) | Duration (s) | Phase |
|-------------|--------------------------|-------------------------|--------------|-------|
| Pancreaticojejunostomy (duct to mucosa) | 0.45 +/- 0.05 | duct 12 +/- 2 | 10 | 5 |
| Hepaticojejunostomy (end to side) | 0.50 +/- 0.05 | bile 8 +/- 2 | 6 | 6 |
| Gastrojejunostomy (antecolic) | 0.60 +/- 0.05 | n/a | 6 | 7 |

## Fistula Risk Score Inputs

| Input | Source | Range | Weight |
|-------|--------|-------|--------|
| Gland texture | Pre operative imaging | soft / firm | soft = 2, firm = 0 |
| Pathology | Pre operative histology | PDAC / other | PDAC = 0, other = 1 |
| Pancreatic duct diameter (mm) | Pre operative imaging | 1 to 6 | 1 mm = 4, 6 mm = 0 |
| Estimated blood loss (mL) | Intra operative arm 7 suction | 0 to 1000+ | 0 = 0, 1000+ = 4 |

## Realized Grade Classifications

| Anastomosis | Possible realized values |
|-------------|----------------------------|
| Pancreaticojejunostomy | grade A (subclinical), grade B (clinically relevant), grade C (severe, requires reoperation) |
| Hepaticojejunostomy | leak absent, leak present |
| Gastrojejunostomy | patent, delayed gastric emptying |

## Cross References

- `../../instructions/anastomosis_protocols.md` fixes the per anastomosis full protocol.
- `../../instructions/sensor_specification_100khz.md` fixes the ring tension and manometry sensors.
- `../../instructions/multi_arm_coordination_8arm.md` fixes the cross arm ring tension coordination.
