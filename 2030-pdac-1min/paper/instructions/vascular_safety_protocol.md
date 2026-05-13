# Vascular Safety Protocol (PDAC Specific)

This file fixes the no fly, soft warning, and hard stop volumes around the five named vessels (superior mesenteric vein, portal vein, hepatic artery, celiac axis, superior mesenteric artery) for the PAT-PDAC-0001 patient. The future Claude Code Opus 4.7 1M Max session reads this file to author the vascular safety zone gate at 2030-pdac-1min/src/vascular/safety_zone_gate.py and the per vessel zone configuration at 2030-pdac-1min/config/vascular_safety_zones.yaml.

## Why Vascular Safety Is the Dominant Safety Constraint in PDAC

The pancreaticoduodenectomy operation traces around three vascular danger zones that do not exist in the GBM resection bed. The portomesenteric venous confluence behind the pancreatic neck, the superior mesenteric artery origin at the celiac axis, and the common hepatic artery course define the operative envelope. A 1 mm robotic tip excursion into any of these vessel walls is immediately catastrophic. The vascular safety protocol therefore enforces three nested volumes per vessel and a hard stop at the innermost volume. This is the PDAC specific analogue of the GBM brainstem proximity gate; the PDAC version is stricter because the vessel walls are thinner, the perivascular tissue planes are smaller, and the consequences of arterial wall breach are immediate hemorrhage rather than delayed neurologic deficit.

## Per Vessel Volume Definitions

For each named vessel, three nested volumes are defined: the hard stop volume (inner, robot tip cannot enter under any circumstance), the soft warning volume (middle, robot tip enters with velocity scaled to 10 percent), and the no fly volume (outer, robot tip enters with velocity scaled to 50 percent). The volumes are cylindrical tubes around the vessel centerline; the centerline coordinates and radii are fixed in the table below.

| Vessel | Centerline x (mm) | Centerline y (mm) | Centerline z (mm) | Length (mm) | Hard stop r (mm) | Soft warning r (mm) | No fly r (mm) |
|--------|-------------------|-------------------|-------------------|-------------|------------------|---------------------|---------------|
| Superior mesenteric vein | +15 | -25 to -65 | -45 to -55 | 40 | 2.0 | 4.0 | 6.0 |
| Portal vein | +5 | -55 to -75 | -55 to -50 | 20 | 2.0 | 4.0 | 6.0 |
| Hepatic artery (common) | +5 to +20 | -60 to -65 | -50 to -55 | 18 | 1.5 | 3.0 | 5.0 |
| Celiac axis | +0 to +5 | -65 to -70 | -60 to -55 | 8 | 1.5 | 3.0 | 5.0 |
| Superior mesenteric artery | +0 to +5 | -35 to -65 | -55 to -60 | 30 | 1.5 | 3.0 | 5.0 |

The hard stop radius is approximately one half of the soft warning radius and one third of the no fly radius. The arterial vessels (hepatic artery, celiac axis, superior mesenteric artery) have tighter radii than the venous vessels (superior mesenteric vein, portal vein) because the arterial wall is thinner and the consequences of arterial breach are more immediate.

## Safety Zone Gate Logic

The per arm safety zone gate runs at the 10 kHz command channel rate. For each per arm xyz command, the gate computes the L2 norm distance from the commanded position to the nearest vessel centerline and compares the distance to the per vessel hard stop, soft warning, and no fly radii. The gate emits one of four actions: clear (no scaling), no fly (velocity scaled to 50 percent), soft warning (velocity scaled to 10 percent), or hard stop (per arm e stop).

| Action | Trigger | Velocity scale | Force soft cap (N) | E stop |
|--------|---------|----------------|---------------------|--------|
| Clear | Distance > no fly radius | 100 percent | 3.0 | no |
| No fly | Soft warning radius < Distance <= no fly radius | 50 percent | 2.5 | no |
| Soft warning | Hard stop radius < Distance <= soft warning radius | 10 percent | 1.5 | no |
| Hard stop | Distance <= hard stop radius | 0 percent | 0.0 | yes |

The per arm e stop latency budget is 3 ms; the per arm park latency budget is 50 microseconds. The hard stop action is logged as a per iteration vessel hard stop event in run_NNNNN_events.parquet.

## Phase Specific Zone Activation

The per vessel zone activation is phase specific. Each phase activates a subset of the five vessel zones; phases that do not require dissection near a vessel deactivate the corresponding zones.

| Phase | Active vessel zones | Deactivated vessel zones |
|-------|---------------------|--------------------------|
| 1 (exploration, Kocher) | None | All |
| 2 (vascular control, venous dissection) | SMV, PV, hepatic artery | Celiac axis, SMA |
| 3 (uncinate dissection, artery first) | SMA, celiac axis | SMV, PV, hepatic artery |
| 4 (specimen removal, en bloc resection) | All five | None |
| 5 (pancreaticojejunostomy) | SMV, PV (proximity only) | Hepatic artery, celiac axis, SMA |
| 6 (hepaticojejunostomy) | Hepatic artery (proximity only) | SMV, PV, celiac axis, SMA |
| 7 (gastrojejunostomy) | None | All |
| 8 (hemostasis verification, drain placement, withdrawal) | All five (passive check) | None |

## Vessel Surface Proximity Sensor Integration

The vessel surface proximity sensor (100 kHz, confocal laser triangulation, 0.01 mm resolution) is per arm and is the primary measurement input to the safety zone gate. The sensor measures the distance from the per arm tip to the nearest vessel surface within the active vessel zone set for the current phase. If the proximity sensor reports a distance below the hard stop radius, the per arm e stop is triggered immediately at the 100 kHz sample rate (one tick latency, equivalent to 10 microseconds). This is 300x faster than the 3 ms cross arm e stop latency budget and provides a defense in depth layer beyond the 10 kHz command channel safety zone gate.

## ASCII Vessel Map

The vascular safety zone map for PAT-PDAC-0001 is reproduced below for orientation. The future Claude Code session generates the equivalent ASCII at 2030-pdac-1min/outputs/diagrams/vascular_safety_map.txt.

```
+==========================================================================+
|     VASCULAR SAFETY ZONES (PAT-PDAC-0001, 5 named vessels)               |
+==========================================================================+
|                                                                          |
|  patient frame (mm, origin = umbilicus):                                 |
|  x = right, y = caudal, z = anterior                                     |
|                                                                          |
|              +----------- celiac axis (1.5/3.0/5.0) ----------+          |
|              |                                                |          |
|              v                                                v          |
|     hepatic artery (1.5/3.0/5.0) ----+                                   |
|                                       \                                  |
|                                        v                                 |
|     superior mesenteric vein <-->  portomesenteric    +-> portal vein    |
|     (2.0/4.0/6.0)                  confluence         |   (2.0/4.0/6.0)  |
|                                                       |                  |
|                                       |               |                  |
|                                       v               v                  |
|                       superior mesenteric artery (1.5/3.0/5.0)           |
|                                                                          |
|     legend: (hard stop r / soft warning r / no fly r) in mm              |
|     hard stop: per arm e stop, 3 ms budget, 50 us park                   |
|     soft warning: velocity 10 percent, force soft cap 1.5 N              |
|     no fly: velocity 50 percent, force soft cap 2.5 N                    |
+==========================================================================+
```

## Cross References

- pdac_context_1min.md fixes the vascular anatomy reference table.
- sensor_specification_100khz.md fixes the vessel surface proximity sensor.
- multi_arm_coordination_8arm.md fixes the cross arm e stop latency budget.
- commit_03_xyz_8arm.md fixes the per arm xyz command schema that the safety zone gate consumes.
- commit_06_error_fixes.md fixes the lint and format gates on the per vessel zone configuration.
