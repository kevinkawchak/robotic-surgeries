# Multi Arm Coordination (8 Arm, 10 kHz Heartbeat)

This file fixes the inter arm coordination protocol for the eight arm PDAC 1 minute variant. The future Claude Code Opus 4.7 1M Max session reads this file to author the per arm 10 kHz heartbeat broadcast bus at 2030-pdac-1min/src/coordination/arm_heartbeat_10khz.cpp and the collision avoidance state machine at 2030-pdac-1min/src/coordination/arm_collision_avoidance.cpp.

## Heartbeat Bus Contract

The heartbeat bus is a deterministic 10 kHz broadcast bus that connects all eight arms to a single coordination master. The coordination master broadcasts a fixed 64 byte frame every 100 microseconds (10 kHz). Each arm consumes the broadcast frame and contributes its own 32 byte response frame within the same 100 microsecond window. The cross arm watchdog deadline is 100 microseconds; if any arm fails to acknowledge the broadcast within the deadline, the cross arm e stop is triggered and all eight arms park within 50 microseconds.

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

The heartbeat bus rate (10 kHz) is 10x faster than the v3.9.1 GBM 1 kHz heartbeat. The faster rate is required because the eight arms operate in three named anastomosis events where micro motions of any one arm directly affect the ring tension at another arm. A 1 kHz heartbeat at 1 ms granularity would miss the 100 microsecond ring tension transients that the duct to mucosa pancreaticojejunostomy demands.

## Cross Arm Force Caps

The per arm tip force cap is 3 N (60 percent tighter than the v3.9.1 GBM 5 N cap because PDAC tissue is more fragile and the pancreatic duct is more sensitive than the GBM resection bed). The cumulative cross arm tip force cap is 18 N (50 percent looser than the v3.9.1 GBM 12 N cap because eight arms cooperate vs four).

| Cap | Value | Trigger threshold | Action |
|-----|-------|-------------------|--------|
| Per arm tip force (soft) | 2.5 N | 2.5 N | Slow command queue |
| Per arm tip force (hard) | 3.0 N | 3.0 N | Per arm e stop |
| Cumulative cross arm tip force (soft) | 15.0 N | 15.0 N | Slow all command queues |
| Cumulative cross arm tip force (hard) | 18.0 N | 18.0 N | Cross arm e stop |
| Per arm force time integral (soft) | 5.0 N.s | 5.0 N.s | Phase 5/6/7 anastomosis arm pause |
| Per arm force time integral (hard) | 8.0 N.s | 8.0 N.s | Per arm e stop |

The soft cap triggers a command queue slow down at the affected arm or across all arms; the hard cap triggers an immediate e stop. The per arm e stop latency budget is 3 ms; the cross arm e stop latency budget is 3 ms; the per arm park latency budget is 50 microseconds. These are 40 percent tighter than the v3.9.1 GBM 5 ms e stop and 100 microsecond park budgets.

## Per Arm Phase Activation Schedule

The per arm phase activation schedule fixes which arms are active during each phase. The schedule is identical across all 32 iterations and is part of the deterministic seed contract.

| Phase | Active arms | Idle arms |
|-------|-------------|-----------|
| 1 (exploration, Kocher) | 1, 2, 3, 4 | 5, 6, 7, 8 |
| 2 (vascular control, venous dissection) | 1, 2, 3, 4, 5, 6, 7, 8 | none |
| 3 (uncinate dissection, artery first) | 1, 2, 3, 4 | 5, 6, 7, 8 |
| 4 (specimen removal, en bloc resection) | 1, 2, 3, 4, 5, 6, 7, 8 | none |
| 5 (pancreaticojejunostomy) | 1, 2, 3, 4, 5 | 6, 7, 8 |
| 6 (hepaticojejunostomy) | 1, 2, 3, 4, 5 | 6, 7, 8 |
| 7 (gastrojejunostomy) | 1, 2, 3, 4 | 5, 6, 7, 8 |
| 8 (hemostasis verification, drain placement, withdrawal) | 1, 2, 3, 4, 5, 6, 7, 8 | none |

The idle arms maintain the 10 kHz heartbeat broadcast and respond with a heartbeat sequence acknowledgment but do not emit motion commands. The cross arm collision avoidance state machine treats idle arms as proximity obstacles and the active arms route around them.

## Collision Avoidance State Machine

The per arm collision avoidance state machine is a four state finite state machine. The state is broadcast every 100 microseconds on the per arm heartbeat response frame and is consumed by the coordination master.

| State | Condition | Action |
|-------|-----------|--------|
| Clear | Nearest neighbor distance > 30 mm | Normal command execution |
| Proximity | 15 mm <= Nearest neighbor distance <= 30 mm | Velocity scaled to 50 percent |
| Contact | 5 mm <= Nearest neighbor distance < 15 mm | Velocity scaled to 10 percent; force soft cap 1.5 N |
| Unsafe | Nearest neighbor distance < 5 mm | Per arm e stop; cross arm pause until clear |

The nearest neighbor distance is the L2 norm distance from the per arm end effector position to the nearest other arm end effector position. The distance is computed at 10 kHz by the coordination master and broadcast to all eight arms.

## ASCII Schematic

The 8 arm coordination heartbeat schematic is reproduced below for orientation. The future Claude Code session generates the equivalent ASCII at 2030-pdac-1min/outputs/diagrams/coordination_heartbeat_8arm.txt.

```
+==========================================================================+
|     8-ARM COORDINATION HEARTBEAT (10 kHz, 64-byte frame, 100 us deadline)|
+==========================================================================+
|    +-------+ 10 kHz broadcast +-------+ 10 kHz broadcast +-------+       |
|    | ARM 1 |<---------------->| ARM 2 |<---------------->| ARM 3 |      |
|    | hyb   |                  | bipol |                  | retr  |      |
|    | u-w-p |                  | + coag|                  | + grsp|      |
|    +---+---+                  +---+---+                  +---+---+       |
|        |                          |                          |           |
|        v                          v                          v           |
|    +-------+ 10 kHz broadcast +-------+ 10 kHz broadcast +-------+       |
|    | ARM 4 |<---------------->| ARM 5 |<---------------->| ARM 6 |      |
|    | iMRI  |                  | bipol |                  | suct  |      |
|    | + NIR |                  | + suct|                  | + coag|      |
|    +---+---+                  +---+---+                  +---+---+       |
|        |                          |                          |           |
|        v                          v                          v           |
|    +-------+ 10 kHz broadcast +-------+                                  |
|    | ARM 7 |<---------------->| ARM 8 |                                  |
|    | suct  |                  | NIR + |                                  |
|    | + irr |                  | UV    |                                  |
|    +-------+                  +-------+                                  |
|                                                                          |
|   COORDINATION MASTER (deterministic, 10 kHz, 64-byte frame, 16-bit CRC) |
|     - broadcasts every 100 us, expects per arm ack within 100 us         |
|     - cross arm e stop latency budget 3 ms                               |
|     - per arm park latency budget 50 us                                  |
|   Per arm tip force cap 3.0 N hard, 2.5 N soft                           |
|   Cumulative cross arm tip force cap 18.0 N hard, 15.0 N soft            |
|   Per arm force time integral cap 8.0 N.s hard, 5.0 N.s soft             |
+==========================================================================+
```

## Cross Arm Force Time Integral Tracking

The per arm force time integral is the integral of the per arm tip force scalar over the phase duration. The integral is reset at every phase boundary and re initialized to zero. The integral is tracked at 100 kHz and the per phase value is recorded in the L3 per phase Parquet at 2030-pdac-1min/data/iterations/run_NNNNN_L3_phase.parquet.

The per arm force time integral cap (soft 5.0 N.s, hard 8.0 N.s) addresses the cumulative force violation rate gap noted in the v3.9.1 GBM full paper at 2030-gbm-1min/paper/full-paper/final-paper/sections/limitations_future.tex. The v3.9.1 GBM 16 iteration sweep did not bound the cumulative force violation rate at the 95 percent confidence interval; the PDAC variant tightens this by (a) doubling the iteration count to 32, (b) adding the per arm force time integral cap, and (c) tracking the integral in the committed L3 layer.

## Anastomosis Ring Tension Coordination

During Phases 5, 6, and 7 (pancreaticojejunostomy, hepaticojejunostomy, gastrojejunostomy), the per arm ring tension sensor is active and the ring tension target is fixed in anastomosis_protocols.md. The cross arm ring tension coordination master enforces the per anastomosis ring tension target to within +/- 0.05 N at 10 kHz. If the ring tension drifts outside the +/- 0.05 N band, the coordination master emits a velocity scale command to the suturing arm and the retracting arm in opposite directions to restore the target tension within 100 microseconds.

## Cross References

- pdac_context_1min.md fixes the 8 phase timeline and the per arm tool assignment.
- sensor_specification_100khz.md fixes the 640 channel sensor stack.
- vascular_safety_protocol.md fixes the per vessel safety volumes that the coordination master enforces.
- anastomosis_protocols.md fixes the per anastomosis ring tension targets that the coordination master tracks.
- commit_03_xyz_8arm.md fixes the per arm xyz command schema that the coordination master consumes.
- commit_04_iterations_1min.md fixes the 32 iteration sweep design that the coordination master is benchmarked against.
