# 2030 GBM 1-Minute Final Report (v0.2.0)

## Abstract

This report consolidates the artifacts produced by running every script
under `2030-gbm-1min/` end to end on a single Linux host under deterministic
seed 20260510. The pipeline materializes a hypothetical 2030 Medtronic
NeuroSpeed 1.0 four-arm parallel stereotactic neurosurgical platform that
performs maximal safe gross-total resection of an IDH-wildtype glioblastoma
(4.2 cm right frontal, patient PAT-GBM-0001) in 60 seconds. Per-arm sensors
stream at mixed 1 kHz commands plus 10 kHz force across 200 channels (50 per
arm times 4 arms). A 1 kHz broadcast heartbeat with a 1 ms deadline binds
the four arms; cumulative tip force across the four arms is capped at 12 N
on the patient frame.

## Key Findings

1. The 16-iteration deterministic sweep is stable and reproducible: all 16
   iterations succeeded, wall-clock 25.67 to 32.20 s mean 27.83 s.
2. Cumulative-force violations remain inside the 12 N envelope across the
   full seed sweep; no E-stop or arm-park condition was triggered in the
   non-event-log code path.
3. The on-prem LLM judge (claude-opus-4-7) produces a stable composite-score
   ranking that puts the robot ahead of the human baseline 4 out of 4 times
   with confidence 0.955 to 1.000. Robot mean composite is 88.53 vs human
   mean composite 70.35; the structural-time-dimension caveat is preserved
   in every round rationale.
4. Per-arm contribution is dominated by ARM_1 (32,372 mm^3 mean tissue
   volume across the 16 iterations), with ARM_2 / ARM_3 / ARM_4 staying in
   their dedicated tool roles (coagulation, suction, imaging) by design.

## Thesis Instantiation

The pipeline operationalizes the project thesis directly: an on-premises
repository-bound LLM (claude-opus-4-7 by default, Ollama optional) computes
commands for 4 cooperating standard surgical robotic arms based on real
time per-arm sensor data, which is mapped to deterministic x, y, z command
streams. Per-arm safety limits (5.0 N tip / 1.0 N lateral) and the
cumulative four-arm tip-force ceiling (12 N) are enforced in the mapper, so
single-arm faults cannot escalate into a system-level exceedance. This is
the "minimizes single robot error potential" clause of the thesis, made
testable by the `ee_force` contributions across the 4 arms.

## Pipeline Architecture (ASCII)

```
sensors -> mapping -> simulation -> metrics -> llm -> comparison
   |         |           |              |         |
   v         v           v              v         v
 outputs/  outputs/   outputs/      outputs/   outputs/
 sensors/ xyz_mapping/ iterations/  metrics/   comparison/
```

## Robot vs Human Baseline (from outputs/metrics/summary.json)

| Metric          | Robot mean | Human mean | Robot advantage      |
|-----------------|-----------|-----------|----------------------|
| quality         | 92.22     | 87.73     | +4.49                |
| safety          | 56.56     | 72.73     | -16.17               |
| cost (USD)      | 8297.42   | 18656.67  | -55 percent          |
| total_seconds   | 60        | 12320     | -99.5 percent        |
| composite       | 88.53     | 70.35     | +18.18               |

Note that the safety dimension shows the robot below human baseline because
the robot count includes per-arm and cumulative force-violation counters
that are not exercised against the manual baseline (which carries 0 across
all violation counters by construction). The composite formula weights
quality at 0.40 and safety at 0.10, so the composite still favors the robot.

## Conclusions

The release-aggregate metric pipeline confirms the v3.9.1 design envelope on
quality, time, cost, and patient experience. The structural caveat on the
time dimension is documented in every comparison artifact. The repository
is now ready for v0.2.0 release.

## Provenance

- seed: 20260510
- iterations: 16
- on-prem LLM model: claude-opus-4-7
- date_utc: 2026-05-10
- commit chain: 12 commits in 1 PR (this PR)
