# File Format Conventions (PDAC 1 Minute Variant)

This file fixes the repository wide file format defaults for the PDAC 1 minute variant. The future Claude Code Opus 4.7 1M Max session reads this file to author the per file format pass during code generation.

## File Format Defaults

| File type | Format | Compression | Encoding | Notes |
|-----------|--------|-------------|----------|-------|
| Parquet | Apache Parquet 2.6 | zstd-3 | n/a | Per arm per second L2; per phase L3; per anastomosis L4; events |
| JSONL | JSON Lines | none | UTF-8 | Per arm per tick sensor sample; per arm per tick xyz command sample |
| CSV | RFC 4180 | none | UTF-8 with BOM | Human review samples only |
| JSON | RFC 8259 | none | UTF-8 | Schema files, manifest, pointer |
| Protocol Buffers | proto3 | n/a | n/a | Schema files at schemas/ |
| Avro | Avro 1.11 | snappy | n/a | Schema files at schemas/ |
| YAML | YAML 1.2 | none | UTF-8 | Configuration files at config/ |
| TOML | TOML 1.0 | none | UTF-8 | pyproject.toml only |
| Markdown | GitHub Flavored Markdown | none | UTF-8 | All .md files |
| Python | Python 3.10 syntax | none | UTF-8 | Black compatible via ruff format |
| Rust | Rust 2021 edition | none | UTF-8 | rustfmt default |
| C++ | C++20 | none | UTF-8 | clang-format Google preset with 100 col |
| Shell | POSIX sh or bash | none | UTF-8 | shellcheck SC2154 allowed |
| Text | UTF-8 plain text | none | UTF-8 | ASCII art diagrams, manifests, logs |

## Encoding and Line Endings

All text files are UTF-8 encoded without BOM (the CSV exception is for spreadsheet compatibility). All text files use LF line endings (no CRLF). Trailing whitespace is stripped. Every text file ends with a single trailing newline.

## Parquet Compression

All committed Parquet files use the zstd-3 compression default. The zstd-3 default achieves approximately 4x compression on the L2 and L3 layers and approximately 6x compression on the L4 anastomosis layer. The zstd-3 default also achieves bit identical compressed output across Python pyarrow 17.0+ and Rust parquet 53.0+ for the deterministic seed contract.

## CSV Sample Files

CSV sample files at 2030-pdac-1min/outputs/sensors/sensor_sample_8arm.csv and similar paths are intended for human review only. CSV files include a header row with column names; the column names match the JSON Schema property names from sensor_specification_100khz.md exactly. Numeric values are formatted with 6 significant digits; integer values are formatted without thousands separators.

## YAML Configuration Files

YAML configuration files at 2030-pdac-1min/config/ use 2 space indentation, no tabs, no trailing whitespace, and a single trailing newline. The document-end gate is enabled in yamllint to ensure every YAML file ends with a single trailing newline.

## Markdown Files

Markdown files use single dashes only throughout the body (no em dashes, no double dashes, no triple dashes per the formatting invariants in the parent README). Markdown files use black text only (no color overrides, no inline color spans). Markdown files use ATX style headers (# at the start of a line, no underline style). Markdown files use single backticks for inline code and fenced code blocks (three backticks) for multi line code with optional language hint.

## ASCII Art Diagrams

ASCII art diagrams at 2030-pdac-1min/outputs/diagrams/ use the box drawing characters +, -, |, =, <, >, ^, v, /, \, and the alphanumeric characters. The diagrams do not use Unicode box drawing characters (the U+2500 to U+257F range). The diagrams are stored as .txt files with UTF-8 encoding and LF line endings.

## SVG and PNG

SVG files are allowed for static low density schematics under 100 KB; PNG files are allowed for the metrics summary visualization at 2030-pdac-1min/outputs/viz/metrics_summary.png and similar paths. PNG files use a 24 bit color depth and a 96 DPI resolution; the maximum committed PNG file size is 5 MB.

SVG files are not produced for high frequency time series; a 6.4 million point path would exceed practical SVG size budgets and trigger browser slowdowns.

## Cross References

- ci_compliance_checklist.md fixes the lint and format gates that enforce these conventions.
- chunking_strategy.md fixes the L0 to L4 Parquet chunking pattern.
- file_size_pyramid_1min.md fixes the per iteration committed budget.
- ascii_diagram_guide.md fixes the ASCII art diagram conventions.
