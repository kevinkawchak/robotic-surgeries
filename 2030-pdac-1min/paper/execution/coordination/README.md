# Coordination Execution

This directory captures the timing budget and per arm broadcast response frame for the 10 kHz heartbeat bus and the per arm collision avoidance state machine. The C++ control loop and the 10 kHz heartbeat broadcast at `../../codegen/src/coordination/arm_heartbeat_10khz.cpp` and `../../codegen/src/coordination/arm_collision_avoidance.cpp` are not invoked live because the execution environment lacks a C++ build toolchain. The timing budgets and response frame counts are extracted directly from the source.

## Reproduction (when a C++ toolchain is available)

```bash
cd 2030-pdac-1min/paper/codegen
g++ -O2 -std=c++17 src/coordination/arm_heartbeat_10khz.cpp -o /tmp/heartbeat
g++ -O2 -std=c++17 src/coordination/arm_collision_avoidance.cpp -o /tmp/collision
```

## Files

| File | Description |
|------|-------------|
| `heartbeat_timing_table.csv` | 10 kHz heartbeat per arm response budgets |
| `collision_state_log.csv` | 4 state collision avoidance FSM transition table |
| `coordination_ascii.txt` | ASCII timing diagram |

## Headline Statistics

| Statistic | Value |
|-----------|-------|
| Heartbeat broadcast rate | 10 kHz |
| Per arm response frame | 32 bytes (cumulative 256 bytes across 8 arms) |
| Watchdog deadline | 100 microseconds |
| Cross arm e stop budget | 3 milliseconds |
| Per arm park budget | 50 microseconds |
| Collision avoidance FSM states | 4 (clear, pending, active, recovery) |
| Active arms cap per phase | 8 |
