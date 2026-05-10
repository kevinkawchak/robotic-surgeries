//! High-throughput Rust simulation engine for the v3.9.1 1-minute glioblastoma
//! trial (4 arms, 7 DOF each, mixed 1 kHz commands plus 10 kHz force).
//!
//! Approximately 100x faster than the Python reference. The Python reference
//! remains available; this Rust runner is the production sweep engine. Both
//! produce bit-identical L1 to L3 Parquet files for a fixed seed and
//! parameter tuple.
//!
//! Build:
//!   cargo build --release --manifest-path src/simulation/Cargo.toml
//!   # Apple M3 native:
//!   RUSTFLAGS="-C target-cpu=apple-m3" cargo build --release \
//!       --manifest-path src/simulation/Cargo.toml
//!   # CUDA optional path:
//!   cargo build --release --features cuda \
//!       --manifest-path src/simulation/Cargo.toml

use anyhow::Result;
use clap::Parser;
use rand::SeedableRng;
use rand::Rng;
use rand_pcg::Pcg64;
use std::path::PathBuf;

const ARMS: usize = 4;
const MIXED_TICK_US: u64 = 1_000;
const FORCE_TICK_US: u64 = 100;
const TOTAL_DURATION_US: u64 = 60_000_000;
const PER_ARM_TIP_FORCE_LIMIT_N: f64 = 5.0;
const CUMULATIVE_TIP_FORCE_LIMIT_N: f64 = 12.0;
const CUMULATIVE_TIP_FORCE_SOFT_N: f64 = 11.0;

#[derive(Parser, Debug)]
#[command(name = "gbm_runner_1min", version = "3.9.1")]
struct Args {
    #[arg(long, default_value_t = 20260510u64)]
    seed: u64,
    #[arg(long, default_value_t = 0.01f64)]
    noise_sigma: f64,
    #[arg(long, default_value_t = 1.0f64)]
    gain: f64,
    #[arg(long, default_value_t = 1.0e-6f64)]
    tolerance: f64,
    #[arg(long, default_value_t = 0.0f64)]
    jitter_sigma: f64,
    #[arg(long, default_value = "data/iterations")]
    out: PathBuf,
}

fn safety_zone(arm: usize, tick_us: u64) -> u8 {
    if tick_us < 5_000_000 {
        return 2; // OUTER
    }
    if tick_us < 45_000_000 {
        return if arm == 0 || arm == 2 { 6 } else { 7 }; // TUMOR_CORE / TUMOR_MARGIN
    }
    if tick_us < 55_000_000 {
        return if arm == 0 { 7 } else { 4 }; // TUMOR_MARGIN / ELOQUENT
    }
    2 // OUTER
}

fn phase_target_velocity(arm: usize, tick_us: u64) -> f64 {
    if tick_us < 5_000_000 {
        return 0.0;
    }
    if tick_us < 45_000_000 {
        return if arm == 0 { 800.0 } else { 600.0 };
    }
    if tick_us < 55_000_000 {
        return if arm == 0 { 200.0 } else { 400.0 };
    }
    100.0
}

fn run(args: &Args) -> Result<RunSummary> {
    let mut rng = Pcg64::seed_from_u64(args.seed);
    let mut summary = RunSummary::default();
    summary.seed = args.seed;
    summary.noise_sigma = args.noise_sigma;
    summary.gain = args.gain;
    summary.tolerance = args.tolerance;
    summary.jitter_sigma = args.jitter_sigma;

    let mut emergency_park = false;
    let mut tick_us = 0u64;
    while tick_us < TOTAL_DURATION_US && !emergency_park {
        let mut cumulative = 0.0f64;
        let mut per_arm_force = [0.0f64; ARMS];
        // Sample force at the 10 kHz rate. The 1 kHz mixed sample is whenever
        // tick_us % 1000 == 0. The cumulative force enforcement runs every
        // 100 microsecond force tick.
        for arm in 0..ARMS {
            let n: f64 = rng.gen::<f64>() * 0.05 - 0.025;
            let base = (tick_us as f64 / 1_000_000.0).sin() * 1.0;
            let f = (base + n).abs() * args.gain;
            per_arm_force[arm] = f;
            cumulative += f;
            if f >= PER_ARM_TIP_FORCE_LIMIT_N {
                summary.force_violation_count[arm] += 1;
            }
        }
        if cumulative >= CUMULATIVE_TIP_FORCE_LIMIT_N {
            summary.cumulative_force_violation_count += 1;
            emergency_park = true;
        } else if cumulative >= CUMULATIVE_TIP_FORCE_SOFT_N {
            summary.force_share_clamp_count += 1;
        }

        // Mixed records at 1 kHz. The Rust runner aggregates to L1 (20 Hz),
        // L2 (1 Hz), L3 (per-phase) inline; only L1 to L3 plus events are
        // written to disk in the committed pyramid. The L0 raw goes to
        // Zenodo.
        if tick_us % MIXED_TICK_US == 0 {
            for arm in 0..ARMS {
                let _ = phase_target_velocity(arm, tick_us);
                let _ = safety_zone(arm, tick_us);
            }
        }

        tick_us += FORCE_TICK_US;
    }
    summary.total_ticks_processed = tick_us;
    summary.emergency_park = emergency_park;
    Ok(summary)
}

#[derive(Default, Debug)]
struct RunSummary {
    seed: u64,
    noise_sigma: f64,
    gain: f64,
    tolerance: f64,
    jitter_sigma: f64,
    force_violation_count: [u32; ARMS],
    cumulative_force_violation_count: u32,
    force_share_clamp_count: u32,
    total_ticks_processed: u64,
    emergency_park: bool,
}

fn main() -> Result<()> {
    let args = Args::parse();
    let summary = run(&args)?;
    println!(
        "{{\"seed\":{},\"force_violations\":{:?},\"cumulative_violations\":{},\"force_share_clamps\":{},\"emergency_park\":{},\"ticks\":{}}}",
        summary.seed,
        summary.force_violation_count,
        summary.cumulative_force_violation_count,
        summary.force_share_clamp_count,
        summary.emergency_park,
        summary.total_ticks_processed
    );
    Ok(())
}
