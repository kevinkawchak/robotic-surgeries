# Run Summary

## Environment

- date_utc: 2026-05-10
- platform: Linux 6.18.5
- python: 3.11.15
- ruff: 0.15.12
- seed: 20260510
- iterations: 16
- on-prem LLM model: claude-opus-4-7

## Pipeline Executed (in order)

| Step | Module                            | Outputs                                    |
|------|-----------------------------------|--------------------------------------------|
| 1    | sensors.ingest_4arm               | outputs/sensors/                           |
| 2    | mapping.sensor_to_xyz_4arm        | outputs/xyz_mapping/                       |
| 3    | simulation.iterate_1min           | outputs/iterations/                        |
| 4    | metrics.compute_1min              | outputs/metrics/                           |
| 5    | llm.compare_agent_1min (default)  | outputs/comparison/                        |
| 6    | llm.compare_agent_1min (mixed)    | outputs/comparison_robot_vs_human/         |

## Headline Outcomes

- 1000-row sensor sample passes the per-arm 5.0 N tip and 12 N cumulative
  four-arm tip force check (0 violations).
- 240 xyz commands resolve to command_state=EMIT (no FORCE_HOLD,
  FORCE_SHARE_CLAMP, or EMERGENCY_PARK gates triggered).
- 16 iterations succeeded (status=succeeded). Wall-clock 25.67 s to 32.20 s,
  mean 27.83 s (matches the 26 to 32 s envelope from the upstream README).
- Heartbeat misses total 37 across the sweep; zero exceedances of the 3 ms
  watchdog threshold (E-stop budget 5 ms validated).
- Robot mean composite 88.53 vs human mean composite 70.35.
- Mixed tournament: robot wins all 4 robot-vs-human rounds with confidence
  0.955 to 1.000.

## Footprint

- outputs/iterations/ on disk: 352 KB
- outputs/sensors/ on disk: 1.2 MB
- outputs/xyz_mapping/ on disk: 36 KB
- outputs/metrics/ on disk: 92 KB
- outputs/comparison/ + comparison_robot_vs_human/ on disk: 24 KB
- outputs/diagrams/ + viz/ on disk: 36 KB
- outputs/logs/ on disk: 16 KB
- TOTAL outputs/ tree on disk: ~1.8 MB
- All committed files honor the 10 MB / 5 MB Parquet caps.
