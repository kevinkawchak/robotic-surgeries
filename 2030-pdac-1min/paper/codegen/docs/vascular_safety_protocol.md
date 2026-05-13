# Vascular Safety Protocol Overview (5 Vessel Zones)

This document fixes the 5 named vessel safety zone overview. The full protocol lives at `../../instructions/vascular_safety_protocol.md` and the gate implementation lives at `src/vascular/safety_zone_gate.py`.

## Five Vessels

| Vessel | Hard stop r (mm) | Soft warning r (mm) | No fly r (mm) |
|--------|------------------|---------------------|---------------|
| Superior mesenteric vein | 2.0 | 4.0 | 6.0 |
| Portal vein | 2.0 | 4.0 | 6.0 |
| Hepatic artery (common) | 1.5 | 3.0 | 5.0 |
| Celiac axis | 1.5 | 3.0 | 5.0 |
| Superior mesenteric artery | 1.5 | 3.0 | 5.0 |

## Safety Zone Gate Logic

| Action | Trigger | Velocity scale | Force soft cap (N) | E stop |
|--------|---------|----------------|---------------------|--------|
| Clear | Distance > no fly r | 100 percent | 3.0 | no |
| No fly | Soft warning r < Distance <= no fly r | 50 percent | 2.5 | no |
| Soft warning | Hard stop r < Distance <= soft warning r | 10 percent | 1.5 | no |
| Hard stop | Distance <= hard stop r | 0 percent | 0.0 | yes |

## Phase Specific Activation

| Phase | Active vessel zones |
|-------|---------------------|
| 1 (exploration) | None |
| 2 (vascular control) | SMV, PV, hepatic artery |
| 3 (uncinate dissection) | SMA, celiac axis |
| 4 (specimen removal) | All five |
| 5 (pancreaticojejunostomy) | SMV, PV (proximity only) |
| 6 (hepaticojejunostomy) | Hepatic artery (proximity only) |
| 7 (gastrojejunostomy) | None |
| 8 (hemostasis, drain, withdraw) | All five (passive check) |

## Vessel Surface Proximity Sensor

The vessel surface proximity sensor at 100 kHz with 0.01 mm resolution is per arm and is the primary measurement input to the safety zone gate. If the proximity sensor reports a distance below the hard stop radius, the per arm e stop is triggered immediately at the 100 kHz sample rate (one tick latency, equivalent to 10 microseconds).

## Cross References

- `../../instructions/vascular_safety_protocol.md` fixes the full vessel volume table.
- `../../instructions/sensor_specification_100khz.md` fixes the vessel surface proximity sensor channel.
- `../../instructions/pdac_context_1min.md` fixes the vascular anatomy reference table.
