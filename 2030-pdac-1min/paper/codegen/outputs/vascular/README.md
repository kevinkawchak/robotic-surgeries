# Vascular Safety Output (v0.6.0)

[![Release](https://img.shields.io/badge/Release-v0.6.0-brightgreen.svg)](../../../../releases.md)
[![Vessels](https://img.shields.io/badge/Vessels-5-purple.svg)](../../config/vascular_safety_zones.yaml)

## Five Named Vessels

The vascular safety zone gate at `../../src/vascular/safety_zone_gate.py` monitors the following five named vessels in the patient frame (origin = umbilicus):

| Vessel | Hard stop r (mm) | Soft warning r (mm) | No fly r (mm) | Active phases |
|--------|------------------|---------------------|---------------|----------------|
| Superior mesenteric vein | 2.0 | 4.0 | 6.0 | 2, 4, 5, 8 |
| Portal vein | 2.0 | 4.0 | 6.0 | 2, 4, 5, 8 |
| Hepatic artery (common) | 1.5 | 3.0 | 5.0 | 2, 4, 6, 8 |
| Celiac axis | 1.5 | 3.0 | 5.0 | 3, 4, 8 |
| Superior mesenteric artery | 1.5 | 3.0 | 5.0 | 3, 4, 8 |

## Safety Zone Gate Actions

| Action | Trigger | Velocity scale | Force soft cap (N) | E stop |
|--------|---------|----------------|---------------------|--------|
| Clear | Distance > no fly r | 100 percent | 3.0 | no |
| No fly | Soft warning r < Distance <= no fly r | 50 percent | 2.5 | no |
| Soft warning | Hard stop r < Distance <= soft warning r | 10 percent | 1.5 | no |
| Hard stop | Distance <= hard stop r | 0 percent | 0.0 | yes |

## Cross References

- `../../config/vascular_safety_zones.yaml` per vessel volume table.
- `../../src/vascular/safety_zone_gate.py` gate implementation.
- `../../../instructions/vascular_safety_protocol.md` full protocol.
