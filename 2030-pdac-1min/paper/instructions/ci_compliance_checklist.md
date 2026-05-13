# CI Compliance Checklist (PDAC 1 Minute Variant)

This file fixes the pre commit CI compliance checklist for the future generated PDAC 1 minute simulation tree at 2030-pdac-1min/. The future Claude Code Opus 4.7 1M Max session reads this file to author the pre commit hook configuration at 2030-pdac-1min/.pre-commit-config.yaml and the per file lint and format pass that the 8th commit (error fixes) executes.

## Why CI Compliance Matters

The v3.9.1 GBM 1 minute variant identified the GitHub CI lint and format matrix as a recurring failure mode for the upstream PR template: 3 failing checks (Cl / lint-and-format (3.10) (pull...), (3.11) (pull...), (3.12) (pull...)). The PDAC 1 minute variant explicitly addresses this failure mode in the 8th commit (2nd to last) which runs the pre commit hook configuration across every committed file in 2030-pdac-1min/ and emits per file lint and format fixes before the final 9th commit.

## Lint and Format Gates

The pre commit hook configuration runs eight gates on the future generated code.

| Gate | Tool | Scope | Trigger condition |
|------|------|-------|-------------------|
| Ruff format check | ruff format --check | All .py files | Any unformatted line |
| Ruff lint check | ruff check | All .py files | Any lint violation |
| Mypy type check (strict) | mypy --strict | All .py files in src/ | Any type error |
| Yamllint relaxed | yamllint -d relaxed | All .yaml, .yml files | Any yamllint error |
| Markdownlint | markdownlint -c .markdownlint.yaml | All .md files | Any markdownlint error |
| Pre commit (trailing whitespace, EOF newline, line endings) | pre-commit | All committed files | Any pre commit violation |
| File size cap (10 MB) | custom Python script | All committed files | Any file > 10 MB |
| Parquet size cap (5 MB) | custom Python script | All committed Parquet files | Any Parquet > 5 MB |

All eight gates must pass before the final 9th commit is allowed to merge.

## Pyproject.toml Lint Configuration

The future generated pyproject.toml at 2030-pdac-1min/pyproject.toml includes the following lint configuration block. The block is identical to the v3.9.1 GBM pyproject.toml lint configuration plus the PDAC specific anastomosis and daraxonrasib module exclusions.

```
[tool.ruff]
line-length = 100
target-version = "py310"
extend-exclude = [
    ".venv",
    "build",
    "dist",
    "data/iterations",
    "outputs",
    "paper/inputs",
    "paper/templates",
]

[tool.ruff.lint]
select = ["E", "F", "I", "N", "D", "UP", "B", "A", "C4", "T20", "PT", "RUF"]
ignore = ["D100", "D101", "D102", "D103", "D104", "D105", "D107"]

[tool.ruff.lint.per-file-ignores]
"tests/*" = ["D", "S101"]
"src/anastomosis/*" = ["D102"]
"src/daraxonrasib/*" = ["D102"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
line-ending = "lf"

[tool.mypy]
python_version = "3.10"
strict = true
ignore_missing_imports = true
exclude = [".venv", "build", "dist", "data/iterations", "outputs"]
```

The Python 3.10 target version ensures compatibility across the 3.10, 3.11, and 3.12 CI lint matrix.

## Yamllint Configuration

The yamllint configuration uses the relaxed preset with one addition: the document-end gate is enabled (document-end: enable) to ensure every YAML file ends with a single trailing newline. This addresses the trailing newline gap noted in the v3.9.1 GBM CI matrix.

## Markdownlint Configuration

The markdownlint configuration enforces single dashes only, no em dashes, no double dashes, no triple dashes (per the formatting invariants in the parent README). The configuration also enforces single backticks for inline code, fenced code blocks for multi line code, and ATX style headers.

```
# .markdownlint.yaml
default: true
MD007:                    # unordered list indentation
  indent: 2
MD013: false              # line length
MD025: false              # multiple top level headers
MD033: false              # inline HTML
MD034: false              # bare URL
MD041: false              # first line top level header
```

## Pre Commit Hook Configuration

The pre commit hook configuration is reproduced below for orientation. The future Claude Code session authors the equivalent .pre-commit-config.yaml at 2030-pdac-1min/.pre-commit-config.yaml.

```
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: mixed-line-ending
        args: ["--fix=lf"]
      - id: check-yaml
      - id: check-json
      - id: check-toml
      - id: check-added-large-files
        args: ["--maxkb=10240"]
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.7.0
    hooks:
      - id: ruff
      - id: ruff-format
  - repo: https://github.com/adrienverge/yamllint
    rev: v1.35.1
    hooks:
      - id: yamllint
        args: ["-d", "relaxed"]
  - repo: https://github.com/igorshubovych/markdownlint-cli
    rev: v0.42.0
    hooks:
      - id: markdownlint
```

## Cross References

- runtime_environments.md fixes the Python 3.10 / 3.11 / 3.12 lint matrix.
- pr_workflow.md fixes the nine commit pattern; the 8th commit runs the pre commit hook configuration.
- file_format_conventions.md fixes the file format defaults that the lint and format gates enforce.
- commit_06_error_fixes.md fixes the 8th commit error review.
