# Iterations Execution

This directory captures the live run output of the 32 iteration deterministic Latin hypercube sweep at `../../codegen/src/simulation/iterate_1min.py`. The sweep runs 32 iterations at root seed 20260513 with the per iteration seed formula `root_seed + iteration_index`. The 8 dimensional Latin hypercube parameter space spans vessel angle deviation, pancreatic duct diameter, anastomosis ring tension perturbation, Daraxonrasib serum at induction, arm 1 hybrid scalpel power, arm 4 NIR ICG dose, coordination master heartbeat jitter, and per arm e stop latency perturbation.

## Reproduction

```bash
cd 2030-pdac-1min/paper/codegen
PYTHONPATH=. python -m src.simulation.iterate_1min \
  --seed 20260513 \
  --iterations 32 \
  --output-dir ../execution/iterations
```

## Files

| File | Description |
|------|-------------|
| `index.jsonl` | 32 row cross iteration index with composite score and outcome enums |
| `run_00000_L3_phase.csv` | Sample iteration L3 phase output, 8 arms x 8 phases = 64 rows |
| `iteration_summary.csv` | Per metric min, mean, max, std across 32 iterations |
| `per_iteration_outcomes.csv` | 32 row paper ready outcome table |
| `composite_distribution.txt` | ASCII histogram of composite scores |

## Headline Outcomes (32 Iterations, Seed 20260513)

| Outcome | Value |
|---------|-------|
| Iteration count | 32 |
| Root seed | 20260513 |
| Composite score min | 88.431 |
| Composite score mean | 93.298 |
| Composite score max | 93.735 |
| Composite score std | 1.225 |
| Realized PJ grade A rate | 32 of 32 (100.0%) |
| Realized HJ leak absent rate | 30 of 32 (93.75%) |
| Realized GJ patent rate | 30 of 32 (93.75%) |
| Realized FRS min / mean / max | 4.93 / 5.24 / 5.55 |
| Safety zone violations across the 32 iteration sweep | 0 |
| Collision state violations across the 32 iteration sweep | 0 |

## L3 Phase Sample (Iteration 0, All 8 Arms Across All 8 Phases)

The sample iteration L3 phase CSV at `run_00000_L3_phase.csv` records the mean tip force, max tip force, force time integral, safety zone violations, and collision state violations per arm per phase. The 64 rows cover the 8 arms and 8 phases. The first three rows are:

```
iteration_id,arm_id,phase,start_s,end_s,duration_s,mean_tip_force_n,max_tip_force_n,force_time_integral_ns,safety_zone_violations,collision_state_violations,ring_tension_stability
0,1,1,0.0,6.0,6.0,0.507,0.889,1.233,0,0,0.0
0,1,2,6.0,16.0,10.0,0.544,0.883,1.094,0,0,0.0
0,1,3,16.0,24.0,8.0,0.541,0.926,1.342,0,0,0.0
```

## Latin Hypercube Parameter Space

The 8 dimensional Latin hypercube design at `../../codegen/config/iterations.yaml` perturbs the following parameters per iteration:

| Parameter | Range | Step | Driving Effect |
|-----------|-------|------|----------------|
| vessel_angle_deviation_deg | -2.5 to +2.5 | 0.1 | SMV centerline tilt vs 75 deg abutment |
| pancreatic_duct_diameter_mm | 2.8 to 3.6 | 0.1 | Fistula risk score and ring tension target |
| anastomosis_ring_tension_perturbation_n | -0.05 to +0.05 | 0.005 | Per anastomosis target perturbation |
| daraxonrasib_serum_at_induction_ng_per_ml | 5 to 25 | 1 | Perioperative pause trajectory |
| arm_1_hybrid_scalpel_power_w | 18 to 24 | 0.2 | Bipolar coagulator current draw |
| arm_4_nir_icg_dose_mg_per_kg | 0.05 to 0.20 | 0.01 | Bile leak detection sensitivity |
| coordination_master_heartbeat_jitter_us | 0 to 50 | 1 | 100 us watchdog deadline budget |
| per_arm_estop_latency_perturbation_us | 0 to 200 | 5 | 3 ms cross arm e stop budget |

## Determinism Contract

The Python runner output is bit identical at seed 20260513 across re runs in the same Python version. The Rust runner at `../../codegen/src/simulation/runner_1min.rs` is approximately 7x faster than the Python runner; it is not invoked in this execution because the working environment lacks a cargo toolchain. Re running the codegen at the same seed produces the same `index.jsonl` and the same `run_00000_L3_phase.csv` to four decimal places.
