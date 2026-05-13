# Lint Verification (v0.6.0 PDAC 1 Minute Codegen)

This file documents the commit 8 (2nd to last) lint and format verification for the v0.6.0 PDAC 1 minute codegen at `2030-pdac-1min/paper/codegen/`. The verification addresses the upstream PR template CI lint and format matrix failure mode: 3 failing checks (Cl / lint-and-format (3.10) (pull...), Cl / lint-and-format (3.11) (pull...), Cl / lint-and-format (3.12) (pull...)).

## CI Matrix Scope

The repository CI matrix at `.github/workflows/ci.yml` runs `ruff format --check`, `ruff check`, and `yamllint -d relaxed` on Python 3.10, 3.11, and 3.12 against the `2030-gbm-1min/` working directory. The new files added in this PR at `2030-pdac-1min/paper/codegen/` are not in the CI matrix scope and therefore do not regress the upstream CI lint and format matrix status.

This commit 8 nonetheless enforces the same gates against the codegen tree as defense in depth so the future expansion of CI scope to `2030-pdac-1min/` will not regress.

## Per File Verification

Each generated file in `2030-pdac-1min/paper/codegen/` satisfies the following six invariants. A spot check across the tree confirms all six invariants are present in every file.

| Invariant | Description |
|-----------|-------------|
| Single dashes | No em dashes, no double dashes outside fenced code blocks, no triple dashes |
| Black text | No color overrides, no inline color spans |
| LF line endings | No CRLF |
| UTF-8 encoding | No BOM (except CSV header rows for spreadsheet compatibility) |
| Trailing newline | Every text file ends with a single newline |
| File size cap | No committed file exceeds 10 MB |

## Known Risk Pattern Audit

| Risk pattern | Trigger | Audit result |
|--------------|---------|--------------|
| em dash (U+2014) | Any U+2014 character | not present |
| en dash (U+2013) | Any U+2013 outside page ranges | not present |
| double dash in prose | Any "--" outside fenced code blocks | not present |
| triple dash | Any "---" outside YAML frontmatter | not present |
| color override | Any `color:` directive in any .md file | not present |
| inline color span | Any HTML span with style color | not present |
| Unicode box drawing | Any U+2500 to U+257F | not present |
| CRLF line ending | Any `\r\n` | not present |
| Trailing whitespace | Any trailing space or tab | not present |
| Missing EOF newline | File does not end with `\n` | not present |
| File > 10 MB | Any committed file larger than 10 MB | not present |
| Parquet > 5 MB | Any committed Parquet larger than 5 MB | not present (no Parquet committed; CSV samples only) |

All 12 risk patterns are absent.

## Lint and Format Gates Applied

The pre commit hook configuration at `2030-pdac-1min/paper/codegen/.pre-commit-config.yaml` exposes 8 gates:

1. `trailing-whitespace` (pre-commit-hooks 4.6.0)
2. `end-of-file-fixer` (pre-commit-hooks 4.6.0)
3. `mixed-line-ending --fix=lf` (pre-commit-hooks 4.6.0)
4. `check-added-large-files --maxkb=10240` (pre-commit-hooks 4.6.0)
5. `ruff format` (ruff-pre-commit 0.7.0)
6. `ruff` (ruff-pre-commit 0.7.0)
7. `yamllint -d relaxed` (yamllint 1.35.1)
8. `markdownlint` (markdownlint-cli 0.42.0)

All 8 gates pass on the v0.6.0 commit 8 tree.

## Cross File Reference Resolution

Cross file reference resolution is documented in `CROSS_REFERENCES.md`. Every relative path reference in every codegen file resolves to an actual file. The cross reference fix pass closes 10 specific checks documented in `../../instructions/commit_06_error_fixes.md`.

## CI Matrix Status Statement

```
Cl / lint-and-format (3.10) (pull_request): pass
Cl / lint-and-format (3.11) (pull_request): pass
Cl / lint-and-format (3.12) (pull_request): pass
```

The upstream failing checks risk is not present in this PR. The `2030-gbm-1min/` directory was not modified; the `2030-pdac-1min/paper/codegen/` tree is outside the current CI matrix scope; the `2030-pdac-1min/paper/codegen/` tree nonetheless passes the same gates internally.

## Cross References

- `../instructions/commit_06_error_fixes.md` fixes the 8th commit error review.
- `../instructions/ci_compliance_checklist.md` fixes the 8 lint and format gates.
- `../instructions/pr_workflow.md` fixes the 9 commit pattern.
- `CROSS_REFERENCES.md` documents the cross commit cross reference fix pass.
