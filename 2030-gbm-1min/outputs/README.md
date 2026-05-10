# 2030 GBM 1-Minute Outputs (Work In Progress)

This directory accumulates the artifacts produced by running every script under
`2030-gbm-1min/` in sequence. The README is rewritten progressively across
commits as new artifacts land. The final form (after the last content commit)
includes DOI badges, a repository structure block, ASCII diagrams, and a full
results table.

## Status

This commit lays down the empty subdirectory scaffold so subsequent commits can
write into deterministic locations. All deeper sections are populated by later
commits in this PR.

## Scaffold

```
outputs/
  sensors/        sensor ingestion outputs and validation logs
  xyz_mapping/    per-arm xyz command traces and ASCII path
  iterations/     16-iteration per-run aggregates and index
  metrics/        per-iteration metric rows and outcomes parquet/json
  comparison/     LLM tournament comparison.json plus reports
  diagrams/       generated ASCII diagrams and tables
  viz/            HTML dashboard, static charts, ASCII overlays
  reports/        consolidated narrative reports and run summary
  logs/           run logs from each script invocation
```
