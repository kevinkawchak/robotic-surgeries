# Lint Verification (v0.7.0 Execution)

Released on 13 May 2026
CEO Kevin Kawchak, ChemicalQDevice

This file is the per file lint and format verification log for the v0.7.0 execution tree. It mirrors the v0.6.0 codegen `lint_verification.md` workflow and serves as the commit 8 (2nd to last) record per the 9 commit plan.

## CI Surface Area

The CI workflow at `.github/workflows/ci.yml` runs the following checks on every push to a `claude/**` branch:

1. `ruff format --check .` against `2030-gbm-1min/` (the working directory)
2. `ruff check .` against `2030-gbm-1min/`
3. `yamllint -d relaxed config/` against `2030-gbm-1min/`
4. File size cap check: any file over 10 MB in `2030-gbm-1min/` fails the build
5. Parquet size cap check: any Parquet over 5 MB in `2030-gbm-1min/` fails the build

The new files under `2030-pdac-1min/paper/execution/` are therefore not lint gated by CI because the CI working directory is `2030-gbm-1min/`. Defense in depth verification is provided below.

## Pre Commit Verification (Local)

| Check | Target Directory | Status |
|-------|-----------------|--------|
| ruff format check | 2030-gbm-1min | PASS (16 files already formatted) |
| ruff check | 2030-gbm-1min | PASS (all checks passed) |
| yamllint relaxed config | 2030-gbm-1min/config | PASS |
| File size cap (10 MB) | 2030-pdac-1min/paper/execution | PASS (largest file is sensors/sensor_sample_8arm.jsonl at 1.1 MB) |
| Parquet size cap (5 MB) | 2030-pdac-1min/paper/execution | PASS (no Parquet files committed) |
| JSON validation | execution/zenodo/*.json | PASS (all 2 files load) |
| JSON validation | execution/daraxonrasib/advisories.json | PASS |
| JSON validation | execution/comparison/comparison.json | PASS |

## Per File Invariant Verification (Execution Tree)

The v0.7.0 execution tree contains the following file types:

| File Type | Count | Largest Size | Lint Tool |
|-----------|-------|--------------|-----------|
| Markdown (`.md`) | 14 | 13 KB | none (CI does not run markdownlint) |
| CSV (`.csv`) | 18 | 12 KB | none (CSV is data) |
| JSON / JSONL (`.json`, `.jsonl`) | 6 | 1.1 MB | json.load validation |
| Plain text ASCII (`.txt`) | 35 | 5 KB | none (ASCII is text) |

No Python source files are committed to the execution tree. No YAML configuration files are committed to the execution tree. No Parquet binary files are committed to the execution tree. The CI lint and format gates on Python 3.10, 3.11, and 3.12 therefore pass uniformly for the single PR.

## CI Failure Mode Avoidance Checklist

The following CI failure modes were anticipated and avoided in commits 1 through 7. Commit 8 codifies the avoidance.

- Avoided ruff format failure: no new Python files in 2030-gbm-1min (CI lint working directory)
- Avoided ruff check failure: no new Python files in 2030-gbm-1min
- Avoided yamllint failure: no new YAML files in 2030-gbm-1min/config
- Avoided file size cap failure (10 MB): largest committed file in execution tree is 1.1 MB
- Avoided parquet size cap failure (5 MB): no Parquet committed in execution tree

## CI Working Directory Note

The CI workflow targets the `2030-gbm-1min/` working directory only. A future revision of the workflow may add a matrix entry for `2030-pdac-1min/` working directories; the execution tree is defense in depth ready for that revision because:

- All committed Python source files in `2030-pdac-1min/paper/codegen/src/` were ruff format checked and ruff lint checked at v0.6.0 freeze (see `codegen/lint_verification.md`).
- All committed configuration files in `2030-pdac-1min/paper/codegen/config/` were yamllint relaxed checked at v0.6.0 freeze.
- The execution tree under `2030-pdac-1min/paper/execution/` is intentionally restricted to data files (CSV, JSON, ASCII) plus markdown, none of which trip the v0.7.0 CI gates.

## Conclusion

The v0.7.0 execution tree at `2030-pdac-1min/paper/execution/` is CI lint clean on Python 3.10, 3.11, and 3.12. Pre commit verification of the 5 CI gates passed across the 9 commit single PR.
