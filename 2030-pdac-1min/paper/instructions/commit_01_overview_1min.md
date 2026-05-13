# Commit 1: Project Overview

This file fixes the Future Commit 1 file list and authoring instructions for the PDAC 1 minute variant. The future Claude Code Opus 4.7 1M Max session authors the future generated code project skeleton in this commit.

## Commit 1 File List

The future Commit 1 emits the following files at 2030-pdac-1min/.

| File | Purpose | Approx size |
|------|---------|-------------|
| README.md | Project README with DOI badges, ASCII pipeline diagram, 9 commit per PR plan | 18 KB |
| LICENSE.txt | MIT License | 1 KB |
| pyproject.toml | Python project configuration with dev, llm-local, zenodo, pdac extras | 1.2 KB |
| docker-compose.yml | Local container orchestration for Python + Rust + DuckDB services | 2 KB |
| .gitignore | Standard Python + Rust gitignore | 0.5 KB |
| docs/architecture_8arm.md | Architecture overview with 8 arm coordination ASCII | 10 KB |
| docs/sensor_spec_640ch.md | Sensor specification with 80 channel per arm table | 12 KB |
| docs/coordinate_mapping_8arm.md | Coordinate mapping overview with 7 DOF DH parameter table | 14 KB |
| docs/iteration_design_32.md | 32 iteration sweep design with Latin hypercube parameter space | 11 KB |
| docs/comparison_methodology_4vendor.md | Four entrant tournament methodology with frozen composite weights | 13 KB |
| docs/multi_arm_coordination_8arm.md | Multi arm coordination overview with 10 kHz heartbeat ASCII | 10 KB |
| docs/vascular_safety_protocol.md | Vascular safety zone overview with 5 vessel zone table | 9 KB |
| docs/anastomosis_protocols.md | Three anastomosis protocol overview with target tables | 11 KB |
| docs/daraxonrasib_integration.md | Daraxonrasib perioperative trajectory overview | 8 KB |

All docs files are Markdown only and not subject to ruff or yamllint gates.

## Commit 1 Authoring Order

1. Generate README.md grounding the project on the PDAC clinical context from pdac_context_1min.md and the on prem LLM thesis from the parent README at 2030-pdac-1min/paper/instructions/README.md.
2. Generate LICENSE.txt as the standard MIT License with copyright 2026 Kevin Kawchak.
3. Generate pyproject.toml with Python >= 3.10, dev extras (ruff, pytest, mypy), llm-local extras (anthropic, ollama, vllm, openai), zenodo extras (requests, hashlib), and pdac extras (scipy, pandas, pyarrow, duckdb, scikit-learn, matplotlib).
4. Generate docker-compose.yml with three services: python (the per iteration sweep runner), rust (the high throughput runner), and duckdb (the cross iteration index server).
5. Generate .gitignore with standard Python + Rust + Jupyter + macOS DS_Store + .venv exclusions.
6. Generate the nine docs files in the order above, each grounded in the corresponding paper/instructions/ file.

## Cross References

- README.md fixes the project structure and the 9 commit workflow.
- pr_workflow.md fixes the 9 commit pattern.
- pdac_context_1min.md fixes the patient and procedure context.
- robot_specification_pancrespeed.md fixes the 8 arm robot platform.
- sensor_specification_100khz.md fixes the 640 channel sensor stack.
- multi_arm_coordination_8arm.md fixes the 10 kHz heartbeat.
- vascular_safety_protocol.md fixes the 5 vessel zones.
- anastomosis_protocols.md fixes the 3 anastomosis targets.
- daraxonrasib_integration.md fixes the perioperative trajectory.
