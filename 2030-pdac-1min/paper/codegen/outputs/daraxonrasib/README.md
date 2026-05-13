# Daraxonrasib Output (v0.6.0)

[![Release](https://img.shields.io/badge/Release-v0.6.0-brightgreen.svg)](../../../../releases.md)
[![DOI](https://img.shields.io/badge/Daraxonrasib%20Timeline-10.5281%2Fzenodo.18099351-yellow)](https://doi.org/10.5281/zenodo.18099351)

This directory documents the per iteration Daraxonrasib perioperative trajectory plus the LLM bound advisory layer outputs for the v0.6.0 PDAC 1 minute 8 arm Whipple simulation.

## Perioperative Trajectory

The perioperative trajectory follows the RASolute 302 protocol: pause Daraxonrasib 72 hours before surgery, maintain trough below 0.5 ng/mL intraoperatively, restart 7 days postoperatively if uncomplicated or 14 days postoperatively if complicated.

| Time relative to surgery | Serum (ng/mL) | Action |
|---------------------------|----------------|--------|
| T-30d | 35 +/- 10 | Standard induction dosing |
| T-72h | 35 +/- 10 (decaying) | Pause |
| T 0 | 0.45 (trough) | Surgery begins |
| T+60s | 0.45 (trough) | Surgery ends |
| T+7d (uncomplicated) | 35 +/- 10 (re inducting) | Restart |
| T+14d (complicated) | 35 +/- 10 (delayed re inducting) | Delayed restart |
| T+21d (FRS >= 8 or force time integral > 8 N.s) | 35 +/- 10 (extended pause) | MDT review |

## Per Iteration Advisory Outputs (32 Iterations)

Across the 32 iteration sweep:

- 27 of 32 iterations (84.4 percent): recommend T+7d restart (PJ grade A, no complication).
- 5 of 32 iterations (15.6 percent): recommend T+14d restart (PJ grade B or HJ leak present or GJ delayed).
- 0 of 32 iterations (0.0 percent): recommend T+21d restart (no iteration hit FRS >= 8 or force time integral > 8 N.s).

## SaMD Framing

The advisory is a software function under the FDA Software as a Medical Device framework. The advisory is not a clinical decision; it is a recommendation that a board certified oncologist reviews before any actual Daraxonrasib restart.

## Cross References

- `../../src/daraxonrasib/trajectory.py` perioperative trajectory implementation.
- `../../src/daraxonrasib/advisory.py` LLM bound advisory implementation.
- `../../prompts/daraxonrasib_advisory_prompt.md` versioned advisory prompt.
- `../../../instructions/daraxonrasib_integration.md` full protocol.
