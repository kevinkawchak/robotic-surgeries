# Chunking Strategy (PDAC 1 Minute Variant)

This file fixes the chunking strategy for the PDAC 1 minute variant. The future Claude Code Opus 4.7 1M Max session reads this file to author the per iteration chunking pipeline at 2030-pdac-1min/src/simulation/chunk_iteration.py and to apply the chunking pattern to the future generated paper at 2030-pdac-1min/paper/full-paper/.

## Why Chunking Matters

A single LLM session has a working memory cap that ranges from 200 K tokens to 1 M tokens depending on the model. The PDAC 1 minute variant generates the following volumes per iteration: 4.8 million force records (100 kHz times 60 seconds times 8 arms), 4.8 million command records (10 kHz times 60 seconds times 8 arms), and approximately 14,000 cross arm coordination events (vessel proximity, collision, anastomosis). Authoring this volume of data inline as markdown would exceed any single session's working memory by 10x to 100x. The chunking strategy therefore divides the generation work into discrete chunks that each fit in the working memory budget and that emit small generator scripts whose runtime output is the full data stream.

## Six Chunking Layers

The PDAC chunking strategy uses six chunking layers, two more than the v3.9.1 GBM variant. The two new PDAC specific layers are L4 (per anastomosis event) and the daraxonrasib trajectory layer.

| Layer | Chunk granularity | Memory budget per chunk | Output |
|-------|-------------------|--------------------------|--------|
| L0 raw | per arm per second | 50,000 tokens | 100 kHz force + 10 kHz cmd Parquet, Zenodo only |
| L1 sample | per arm per 50 ms window | 5,000 tokens | 50 Hz downsampled committed CSV slice |
| L2 aggregate | per arm per second | 500 tokens | 1 Hz per arm aggregate Parquet |
| L3 per phase | per arm per phase | 200 tokens | 1 row per phase per arm Parquet |
| L4 per anastomosis (PDAC specific) | per anastomosis event | 800 tokens | 1 row per anastomosis cross arm Parquet |
| Daraxonrasib trajectory (PDAC specific) | per iteration | 400 tokens | 1 row per iteration Parquet |

The per chunk memory budget is the upper bound; the working memory budget for any single session is the sum of the per chunk budgets across the chunks the session processes plus the fixed overhead of the per chunk prompt template.

## Per Commit Chunking Pattern

The future code generation pass is divided into nine commits (per pr_workflow.md). Each commit operates on a fixed subset of the chunk space. The per commit chunking pattern is reproduced below.

| Commit | Chunks operated on | Memory budget per commit |
|--------|--------------------|---------------------------|
| 1 (project overview + context) | L3 per phase plus daraxonrasib trajectory | 1,800 tokens |
| 2 (sensors) | L0 raw, L1 sample, L2 aggregate generator scripts | 60,000 tokens |
| 3 (xyz mapping) | L0 raw to L2 aggregate generator scripts for the xyz command stream | 60,000 tokens |
| 4 (iterations) | L2, L3, L4, daraxonrasib trajectory aggregator scripts | 2,400 tokens |
| 5 (competition) | L3 per phase plus L4 per anastomosis plus daraxonrasib trajectory plus the per iteration composite score | 3,500 tokens |
| 6 (error fixes) | Cross commit lint, format, cross reference fixes | 5,000 tokens |
| 7 (repository updates) | README, CHANGELOG, releases.md | 5,000 tokens |
| 8 (2nd to last, error fixes) | Cross commit lint, format, cross reference fixes; lint matrix 3.10 / 3.11 / 3.12 | 5,000 tokens |
| 9 (last, repository updates) | README, CHANGELOG, releases.md v0.5.0 | 5,000 tokens |

The largest per commit memory budget is 60,000 tokens for Commits 2 and 3, which author the L0 raw to L2 aggregate generator scripts. The generator scripts themselves are small (approximately 200 lines of Python per script); the 60,000 token budget covers the per chunk prompt template plus the per chunk sensor schema plus the per arm tool assignment table plus the per phase actor list.

## Per Iteration Chunking Pattern

The per iteration generation is also chunked. The future Claude Code session authors a per iteration chunked aggregator pipeline at 2030-pdac-1min/src/simulation/chunk_iteration.py that processes the per iteration L0 raw stream into the L1 to L4 committed layers in eight chunks (one per phase).

| Phase | Chunk granularity | Memory budget per phase chunk | Cumulative iteration memory |
|-------|-------------------|--------------------------------|-----------------------------|
| 1 (exploration, Kocher, 6 s) | per arm per second | 6,000 tokens | 6,000 |
| 2 (vascular control, venous dissection, 10 s) | per arm per second | 10,000 tokens | 16,000 |
| 3 (uncinate dissection, 8 s) | per arm per second | 8,000 tokens | 24,000 |
| 4 (specimen removal, 8 s) | per arm per second | 8,000 tokens | 32,000 |
| 5 (pancreaticojejunostomy, 10 s) | per arm per second plus anastomosis event | 12,000 tokens | 44,000 |
| 6 (hepaticojejunostomy, 6 s) | per arm per second plus anastomosis event | 8,000 tokens | 52,000 |
| 7 (gastrojejunostomy, 6 s) | per arm per second plus anastomosis event | 8,000 tokens | 60,000 |
| 8 (hemostasis verification, drain placement, withdrawal, 6 s) | per arm per second | 6,000 tokens | 66,000 |
| Per iteration cumulative | per phase | per phase | 66,000 |

The per iteration cumulative memory budget is 66,000 tokens, well under any single session's working memory cap. The cross iteration generation budget is 32 iterations times 66,000 tokens equals 2.1 M tokens cumulative, which exceeds any single session. The cross iteration generation is therefore explicitly chunked across 32 sequential per iteration sessions; each session inherits the cross iteration DuckDB index from the prior session and emits the per iteration Parquet files to disk before terminating.

## Source Chunking Pattern Inherited from PDAC Inputs

The four author prior PDAC papers (paper-1 through paper-4 under 2030-pdac-1min/paper/inputs/) and the two research summaries (research-1 daraxonrasib historical timeline and research-2 Whipple procedure evidence baseline) follow a five chunk pattern: chunk_01 (header + executive summary + sections 1 to 4), chunk_02 (sections 5 to 9), chunk_03 (sections 10 to 15), chunk_04 (bibtex refs 1 to 26), chunk_05 (bibtex refs 27 to 52). The future Claude Code session inherits this chunking pattern for the future generated paper at 2030-pdac-1min/paper/full-paper/.

## Cross References

- file_size_pyramid_1min.md fixes the per iteration committed budget across L1 to L4 plus event log.
- sensor_specification_100khz.md fixes the L0 raw schema.
- pr_workflow.md fixes the nine commit pattern.
- commit_04_iterations_1min.md fixes the 32 iteration sweep design.
- zenodo_archive_protocol.md fixes the L0 deposition layout.
