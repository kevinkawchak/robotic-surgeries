# Multi Arm Coordination Overview (10 kHz Heartbeat)

This document fixes the 8 arm 10 kHz heartbeat broadcast bus for the PDAC 1 minute simulation. The full protocol lives at `../../instructions/multi_arm_coordination_8arm.md` and the C++ implementation lives at `src/coordination/arm_heartbeat_10khz.cpp`.

## Heartbeat Bus Contract

| Property | Value |
|----------|-------|
| Broadcast rate | 10 kHz |
| Broadcast frame size | 64 bytes |
| Per arm response frame size | 32 bytes |
| Watchdog deadline | 100 microseconds |
| Cross arm e stop latency budget | 3 milliseconds |
| Cross arm park latency budget | 50 microseconds |
| Heartbeat sequence wrap | 2 to the 32 |
| Heartbeat frame CRC | 16 bit |

## Force Caps

| Cap | Soft | Hard | Action |
|-----|------|------|--------|
| Per arm tip force (N) | 2.5 | 3.0 | Slow command queue / Per arm e stop |
| Cumulative cross arm tip force (N) | 15.0 | 18.0 | Slow all queues / Cross arm e stop |
| Per arm force time integral (N.s) | 5.0 | 8.0 | Phase 5/6/7 anastomosis pause / Per arm e stop |

## Per Phase Arm Activation

| Phase | Active arms | Idle arms |
|-------|-------------|-----------|
| 1 (exploration, Kocher) | 1, 2, 3, 4 | 5, 6, 7, 8 |
| 2 (vascular control) | 1, 2, 3, 4, 5, 6, 7, 8 | none |
| 3 (uncinate dissection) | 1, 2, 3, 4 | 5, 6, 7, 8 |
| 4 (specimen removal) | 1, 2, 3, 4, 5, 6, 7, 8 | none |
| 5 (pancreaticojejunostomy) | 1, 2, 3, 4, 5 | 6, 7, 8 |
| 6 (hepaticojejunostomy) | 1, 2, 3, 4, 5 | 6, 7, 8 |
| 7 (gastrojejunostomy) | 1, 2, 3, 4 | 5, 6, 7, 8 |
| 8 (hemostasis, drain, withdraw) | 1, 2, 3, 4, 5, 6, 7, 8 | none |

Idle arms maintain the 10 kHz heartbeat broadcast and respond with a heartbeat sequence acknowledgment but do not emit motion commands.

## Collision Avoidance State Machine

| State | Nearest neighbor distance | Action |
|-------|----------------------------|--------|
| Clear | > 30 mm | Normal command execution |
| Proximity | 15 to 30 mm | Velocity scaled to 50 percent |
| Contact | 5 to 15 mm | Velocity scaled to 10 percent; force soft cap 1.5 N |
| Unsafe | < 5 mm | Per arm e stop; cross arm pause until clear |

## Anastomosis Ring Tension Coordination

During Phases 5, 6, and 7 the per arm ring tension sensor is active. The coordination master enforces the per anastomosis ring tension target to within plus or minus 0.05 N at 10 kHz. If the ring tension drifts outside the band for more than 100 milliseconds, the master emits a velocity scale command to restore the target within 100 microseconds.

## Cross References

- `../../instructions/multi_arm_coordination_8arm.md` fixes the full coordination protocol.
- `../../instructions/anastomosis_protocols.md` fixes the per anastomosis ring tension targets.
- `../../instructions/sensor_specification_100khz.md` fixes the heartbeat counter and watchdog channels.
