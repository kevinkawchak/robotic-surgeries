# Commit 6 (Future): Error Fixes

This file fixes the Future Commit 6 (the 8th commit of the nine commit single PR per pr_workflow.md, also known as the 2nd to last commit) error review and patch instructions for the PDAC 1 minute variant. The future Claude Code Opus 4.7 1M Max session reads this file to author the per file lint and format pass and the cross commit cross reference fix pass.

## Goal of the Error Fix Commit

The 8th commit explicitly addresses the upstream PR template CI lint and format matrix failure mode: 3 failing checks (Cl / lint-and-format (3.10) (pull...), Cl / lint-and-format (3.11) (pull...), Cl / lint-and-format (3.12) (pull...)). The 8th commit runs the pre commit hook configuration from ci_compliance_checklist.md across every committed file in 2030-pdac-1min/ and emits per file lint and format fixes.

## Per File Lint and Format Pass

The per file lint and format pass runs the following gates in order. Each gate must pass before the next gate runs.

1. ruff format --check on every .py file in 2030-pdac-1min/. Any unformatted line triggers a ruff format fix.
2. ruff check on every .py file in 2030-pdac-1min/. Any lint violation triggers a manual fix.
3. mypy --strict on every .py file in 2030-pdac-1min/src/. Any type error triggers a manual fix.
4. yamllint -d relaxed on every .yaml and .yml file in 2030-pdac-1min/. Any yamllint error triggers a manual fix.
5. markdownlint -c .markdownlint.yaml on every .md file in 2030-pdac-1min/. Any markdownlint error triggers a manual fix.
6. pre-commit on every committed file in 2030-pdac-1min/. Any trailing whitespace, missing EOF newline, or CRLF line ending triggers a fix.
7. Custom file size cap script on every committed file in 2030-pdac-1min/. Any file > 10 MB triggers a manual review.
8. Custom Parquet size cap script on every committed Parquet file in 2030-pdac-1min/data/iterations/. Any Parquet > 5 MB triggers a manual review.

All eight gates must pass before the final 9th commit is allowed to merge.

## Cross Commit Cross Reference Fix Pass

The cross commit cross reference fix pass runs the following checks. Each check produces a fix if it fails.

1. Every per arm xyz command record in data/xyz_command_sample_8arm.jsonl resolves to a valid command_enum value (one of EMIT, HOLD, SLOW, PARK, E_STOP, HEARTBEAT_ACK, PHASE_BOUNDARY).
2. Every per anastomosis event in run_NNNNN_L4_anastomosis.parquet has a valid realized grade (one of A, B, C for PJ; absent, present for HJ; patent, delayed for GJ).
3. Every per iteration L0 pointer in run_NNNNN_L0_raw.zenodo_pointer.json has a valid SHA 256 manifest entry that matches the actual L0 file hash.
4. Every per arm tip force violation in run_NNNNN_events.parquet has a valid resolution field (one of auto, manual).
5. Every per round LLM tournament verdict in results/comparison.json preserves the structural time dimension caveat in the rationale.
6. Every per iteration Daraxonrasib advisory in results/daraxonrasib_advisory.json preserves the SaMD framing caveat in the rationale.
7. Every committed file is under 10 MB.
8. Every committed Parquet is under 5 MB.
9. Every BibTeX entry in references.bib (when present) has a doi field, a url field, and a note field with clickable GitHub plus Zenodo URLs (the latter for repository style entries only).
10. Every cross reference in 2030-pdac-1min/paper/instructions/*.md to a sibling file in the same directory resolves to an actual file path.

## Known Risk Patterns from the v3.9.1 GBM CI Matrix

The v3.9.1 GBM CI matrix flagged the following risk patterns. The PDAC 8th commit explicitly checks for each pattern.

1. underscore character in raw file paths in LaTeX text mode. Fix: load the underscore package after hyperref.
2. caret character outside math mode (e.g. mm^3, mm/s^2). Fix: rewrite as plain text (mm cubed, mm per second squared).
3. ruff format check fails on long string literals. Fix: split long strings across multiple lines.
4. yamllint fails on missing document end newline. Fix: add a single trailing newline to every YAML file.
5. markdownlint fails on bare URLs. Fix: wrap bare URLs in angle brackets (the markdownlint MD034 rule is allowed in this repository, so this is a soft warning rather than a hard fail).
6. Pre commit fails on mixed line endings. Fix: convert all files to LF line endings.

## Commit Message Pattern for the 8th Commit

The 8th commit message follows the pattern:

```
v0.5.0 commit 8/9: error fixes for CI lint matrix 3.10/3.11/3.12

* ruff format and ruff check passes on all .py files in 2030-pdac-1min/
* yamllint -d relaxed passes on all .yaml and .yml files
* markdownlint passes on all .md files
* pre-commit passes on all committed files
* file size cap: no committed file exceeds 10 MB
* Parquet size cap: no committed Parquet exceeds 5 MB
* cross reference fix pass: 10 checks documented in commit_06_error_fixes.md
* known risk patterns from v3.9.1 GBM CI matrix: 6 patterns checked
```

## Cross References

- ci_compliance_checklist.md fixes the lint and format gates.
- pr_workflow.md fixes the nine commit pattern.
- file_format_conventions.md fixes the file format defaults.
- gbm_errors_addressed.md fixes the seven specific GBM approximations that this PDAC variant addresses.
