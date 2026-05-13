# Cross References (v0.7.0 Execution)

Released on 13 May 2026
CEO Kevin Kawchak, ChemicalQDevice

This file documents the cross commit cross reference checks for the v0.7.0 execution tree. Each check verifies that an artifact emitted in one commit is correctly referenced by an artifact emitted in another commit within the single PR. The checks mirror the v0.6.0 codegen `CROSS_REFERENCES.md` workflow.

## Cross Reference Matrix

| # | Source Commit | Target Commit | Reference Type | Status |
|---|--------------|--------------|----------------|--------|
| 1 | Commit 1 README badge: codegen v0.6.0 | Codegen v0.6.0 README at `../codegen/README.md` | URL link | RESOLVED |
| 2 | Commit 1 README badge: DOI 10.5281/zenodo.18445179 | Zenodo deposition at `zenodo/manifest.json` | DOI link | RESOLVED |
| 3 | Commit 2 sensors README: per arm summary | `sensors/per_arm_summary.csv` | file ref | RESOLVED |
| 4 | Commit 3 xyz_mapping README: per arm target table | `xyz_mapping/per_arm_target_table.csv` | file ref | RESOLVED |
| 5 | Commit 4 iterations README: index.jsonl | Commit 4 `iterations/index.jsonl` | file ref | RESOLVED |
| 6 | Commit 4 iterations README: composite distribution | Commit 4 `iterations/composite_distribution.txt` | file ref | RESOLVED |
| 7 | Commit 5 comparison README: 32 iteration tournament | Commit 4 `iterations/index.jsonl` (input) | data flow | RESOLVED |
| 8 | Commit 5 comparison README: leaderboard | `comparison/leaderboard.csv` | file ref | RESOLVED |
| 9 | Commit 6 vascular README: gate verdicts | `vascular/gate_verdicts.csv` | file ref | RESOLVED |
| 10 | Commit 6 anastomosis README: PJ outcomes | `anastomosis/pj_outcomes.csv` | file ref | RESOLVED |
| 11 | Commit 7 daraxonrasib README: trajectory CSV | `daraxonrasib/perioperative_trajectory.csv` | file ref | RESOLVED |
| 12 | Commit 7 daraxonrasib README: advisory JSON | `daraxonrasib/advisories.json` | file ref | RESOLVED |
| 13 | Commit 7 zenodo README: pointer JSON | `zenodo/run_00000_L0_raw.zenodo_pointer.json` | file ref | RESOLVED |
| 14 | Commit 7 results README: headline outcomes | `results/headline_outcomes.md` | file ref | RESOLVED |
| 15 | Commit 8 lint verification: file size caps | All committed files (1.1 MB max) | constraint | RESOLVED |

## Internal Cross Family References

The execution tree references the codegen tree via path relative references (`../codegen/...`). The following internal cross family references were validated:

- `execution/iterations/index.jsonl` is consumed by `execution/daraxonrasib/advisories.json` via the `codegen/src/daraxonrasib/advisory.py` advisory module.
- `execution/iterations/index.jsonl` is also referenced by `execution/comparison/comparison.json` for the leaderboard cross iteration aggregation.
- `execution/metrics/composite_breakdown.csv` matches the per entrant component values cited in `execution/comparison/comparison_report.md`.
- `execution/anastomosis/anastomosis_summary.csv` references the iteration sweep view at `execution/iterations/index.jsonl` as the publication number alongside the per controller view.
- `execution/daraxonrasib/advisory_distribution.txt` references the 3 way decision logic in `codegen/src/daraxonrasib/advisory.py`.
- `execution/zenodo/manifest.json` references the deposition DOI 10.5281/zenodo.18445179 carried from `codegen/releases/v0.6.0/zenodo_doi.txt`.

## External Cross Family References (Pointing Outward)

The execution tree references the following external locations:

- `https://doi.org/10.5281/zenodo.18445179` (DOI badge, Zenodo deposition)
- `https://doi.org/10.5281/zenodo.18099351` (DOI badge, Daraxonrasib historical timeline)
- `https://github.com/kevinkawchak/robotic-surgeries` (GitHub repository)

All three external references are HTTPS and stable.

## Inbound Cross References

The following files in the rest of the repository reference the v0.7.0 execution tree:

- `releases.md` v0.7.0 block (added in commit 9)
- `CHANGELOG.md` v0.7.0 entry (added in commit 9)
- Top level `README.md` repository structure block (updated in commit 9)
- Top level `README.md` v0.7.0 badge (added in commit 9)
- Top level `README.md` v0.7.0 PDAC execution ASCII snapshot (added in commit 9)
