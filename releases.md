# Release Notes

This file tracks every tagged release of the robotic-surgeries repository.
Releases follow semantic versioning. The first project to land here is the
4-arm 1-minute glioblastoma trial in `2030-gbm-1min/` (project version
v3.9.1, repository release v0.1.0). The v0.2.0 release publishes the
end-to-end run outputs of the same pipeline. The v0.3.0 release lands the
LaTeX paper template for the same project under `2030-gbm-1min/paper/`.

## Release title

v0.3.0 - 2030 GBM 1-Minute LaTeX Paper Template (Head Start for Downstream Claude Code)

## Summary

This release lands the LaTeX paper template for the project titled
**2030: 60 Second Glioblastoma AI Robotic Surgery** under
`2030-gbm-1min/paper/`. The template is a head start for a future Claude
Code Opus 4.7 1M Max processing pass; every `sections/*.tex` file carries
bracketed instructions that name the exact upstream and current repository
paths to read so the downstream 70+ page paper grounds itself in this
repository's content. The included files are `main.tex` (title page,
TOC, document structure), `new_paper.sty` (11 pt body, 1 in margins,
ptm/phv font pair, widow and orphan suppression, raggedright tables,
small-caps Abstract heading), `references.bib` (27 entries each with a
clickable DOI URL plus GitHub and Zenodo URLs inside the note field where
applicable), `README.md` (navigation index, compile recipe, formatting
invariants, senior-author final-pass checklist), and the eight
`sections/*.tex` files (`abstract.tex`, `introduction.tex`, `methods.tex`,
`results.tex`, `discussion.tex`, `limitations_future.tex`, `conclusions.tex`,
`back_matter.tex`). The paper Zenodo DOI is 10.5281/zenodo.20113157 and
the parent repository deposition DOI is 10.5281/zenodo.18445179; both are
clickable in the bibliography. The template compiles cleanly on Overleaf
and on any local pdflatex plus bibtex installation. The release also
refreshes the top-level README.md to add the v0.3.0 paper template badge,
the new paper subtree in the Repository Structure block, a v0.3.0 Paper
Template ASCII snapshot, and a paper-template citation block. CI lint and
format gates continue to pass on Python 3.10, 3.11, and 3.12 because the
new files are LaTeX and Markdown only and are not subject to `ruff format
--check`, `ruff check`, or `yamllint -d relaxed`.

## Features

- LaTeX paper template under `2030-gbm-1min/paper/` titled **2030: 60 Second Glioblastoma AI Robotic Surgery** with title page (2-line centered title, green ORCID logo + https://orcid.org/0009-0007-5457-8667, CEO ChemicalQDevice, clickable DOI 10.5281/zenodo.20113157, May 11, 2026 date, abstract on title page, mandatory disclaimer, keywords).
- 8 `sections/*.tex` files each carrying bracketed instructions naming the exact upstream and current repository paths to read for a future Claude Code Opus 4.7 1M Max processing pass: `abstract.tex` (900-character title-page abstract), `introduction.tex` (FDA RTCT, GBM clinical context, current robotic neurosurgery baseline, on-premises LLM thesis, transition), `methods.tex` (instruction inputs, 2030 NeuroSpeed 1.0 robot, sensors, xyz mapping, iterations + LLM tournament, code execution environment), `results.tex` (instruction creation, code generation, code execution, iteration sweep, LLM tournament, exceptional 54x1001 sensor table feat), `discussion.tex` (significance, FDA framing, on-prem LLM advantages, head-start framing, practical insights), `limitations_future.tex` (approximations vs generated vs executed accounting, 60min vs 1min deltas, cross-simulation limitations, Track A vs Track B, future work to reduce approximations), `conclusions.tex` (headline artifact counts, themes, implications, forward path), `back_matter.tex` (Acknowledgments, Ethical Disclosures, Rights and Permissions, Cite This Article, Data Availability).
- Style file `new_paper.sty` (11 pt body, 1 in margins, ptm/phv font pair, widow and orphan suppression at 10000, compact section spacing, justified text with controlled emergencystretch, small-caps Abstract heading, raggedright table column types L, C, R with mandatory `\raggedright\arraybackslash` prefix for every column width value).
- `references.bib` with 27 entries spanning the FDA real-time clinical trials announcement, the author's prior glioblastoma and clinical trial work (Zenodo 17774560, 15549831, 17614396, and 19994945), the paper's own DOI 10.5281/zenodo.20113157, the parent repository deposition DOI 10.5281/zenodo.18445179, glioblastoma clinical context (Stupp 2005, Sanai 2011, Stummer 2006), Medtronic ROSA ONE Brain v3.0 baseline (Lefranc 2014, Kalakoti 2019), IEC 80601-2-77 and IEC 62304 standards, FDA SaMD framework, TRIPOD+AI and CREMLS reporting standards, Claude Code / Claude Opus 4.7 / Claude Sonnet 4.6 tooling, ChatGPT Deep Research, Google Gemini AI Overview, Ollama, vLLM, Apache Arrow, DuckDB, and Zenodo. Every entry preserves a clickable DOI URL plus (for repository-style entries) both a GitHub URL and a Zenodo URL inside the note field.
- `2030-gbm-1min/paper/README.md` navigation index documenting the title-page metadata, file layout, section order with bracketed-instruction status, AVAILABLE DIRECTORIES (upstream and current) for downstream processing, Overleaf compile recipe, 9 formatting invariants (single dashes only, black text, raggedright table columns, no widows or orphans, no margin overflow, no large white spaces, symbol correction including SS to section sign, DOI and URL clickability, page-level self-standing layout), the senior-author final-pass checklist, the CI lint and Python environment note, and the license block.
- Error-fix commit (2nd to last in this PR) loads the `underscore` package after `hyperref` so the bracketed instruction paths with underscores render as printable characters in text mode, and rewrites `mm/s^2` and `mm^3` as `mm per second squared` and `mm cubed` plain text so no caret character escapes math mode.
- Repository-update commit (last in this PR) refreshes the top-level `README.md` with the v0.3.0 paper template badge, the new paper subtree in the Repository Structure block, the v0.3.0 Paper Template ASCII snapshot, the Overleaf compile recipe, the Overleaf-ready zip creation recipe, and the paper-template citation block; refreshes `CHANGELOG.md` with the v0.3.0 entry; refreshes `2030-gbm-1min/README.md` with the `paper/` subdirectory contents in the Repository Tree block; and explicitly documents the LaTeX Source Files zip creation recipe in `2030-gbm-1min/paper/README.md`.

## Contributors

@kevinkawchak
@claude
@openai
@google-gemini

## Notes

- The LaTeX template explicitly defers prose generation. Each section's bracketed instructions enumerate the exact upstream and current files for a downstream Claude Code Opus 4.7 1M Max processing pass to read; that pass replaces each `[bracketed instruction]` block with prose, tables, and ASCII diagrams. The pass must preserve the 9 formatting invariants listed in `2030-gbm-1min/paper/README.md`.
- The Overleaf-ready `LaTeX Source Files.zip` can be bundled locally from the LaTeX sources committed under `2030-gbm-1min/paper/` with: `cd 2030-gbm-1min/paper && zip -r "LaTeX Source Files.zip" main.tex new_paper.sty references.bib sections/ orcid_icon.png`. The orcid_icon.png file falls back to a green "iD" tag rendered by `new_paper.sty` if absent.
- The paper's Zenodo DOI is 10.5281/zenodo.20113157 (clickable from the title page and from the Cite This Article back-matter block). The parent repository deposition DOI is 10.5281/zenodo.18445179.
- The CI lint and format gates on Python 3.10, 3.11, and 3.12 continue to pass; the new files under `2030-gbm-1min/paper/` are LaTeX and Markdown only and are not subject to `ruff format --check`, `ruff check`, or `yamllint -d relaxed`. The lint-and-format failing checks risk from the upstream PR template is not present in this PR.
- All committed files honor the 10 MB per-file cap and the 5 MB committed-Parquet cap. The CI workflow continues to enforce both.

## Release title

v0.2.0 - 2030 GBM 1-Minute End-to-End Pipeline Outputs

## Summary

This release runs every script under `2030-gbm-1min/` end to end on a single
Linux host under deterministic seed 20260510 and publishes the resulting
artifacts to `2030-gbm-1min/outputs/`. The outputs tree includes the
1000-row sensor sample plus per-arm xyz traces (240 commands), the
16-iteration deterministic sweep (80 Parquet files plus per-iteration L0
Zenodo pointer JSON), the per-iteration metric rows (16 robot plus 30 human
baseline), the 4-entity LLM tournament leaderboards (default robot vs robot
and mixed robot vs human), 6 curated ASCII diagrams, 4 ASCII bar/histogram
charts, and 4 narrative reports (run summary, process log, final report,
limitations). Robot mean composite score 88.53 vs human mean composite
70.35; robot wins all 4 robot-vs-human pairings with confidence 0.955 to
1.000 with the structural-time-dimension caveat preserved. Total committed
footprint of the outputs tree is approximately 1.8 MB, well inside the 10 MB
per-file and 5 MB per-Parquet caps. Lint and CI gates pass on Python 3.10,
3.11, and 3.12: `ruff format --check` (16 files clean), `ruff check` (clean),
`yamllint -d relaxed config/` (clean after the kinematics_4arm.yaml block
mapping fix), and the file size cap. A new outputs README block carries the
DOI and CI badges, the thesis statement, the full repository structure, the
pipeline architecture ASCII, the 4-arm coordination ASCII, and the citation
block.

## Features

- End-to-end run of `python -m sensors.ingest_4arm`, `python -m mapping.sensor_to_xyz_4arm`, `python -m simulation.iterate_1min --iterations 16`, `python -m metrics.compute_1min`, and `python -m llm.compare_agent_1min` (twice) under deterministic seed 20260510.
- 1000-row sensor sample (jsonl plus csv) with per-arm and aggregate force statistics; per_arm_violations=0 cumulative_violations=0 against the 5.0 N per-arm tip and 12 N cumulative-four-arm-tip envelope.
- 240-row per-arm xyz command traces (4 files of 60 rows each) plus an ASCII per-second xyz path overlay; all 240 commands resolve to command_state=EMIT.
- 16-iteration sweep with per-iteration L1 50 ms, L2 1 s, L3 phase, events Parquet aggregates plus per-iteration L0 Zenodo pointer JSON; cross-iteration index.jsonl manifest plus DuckDB analytical store; iteration table; aggregate counters and ranges.
- Per-iteration metric rows under the frozen weighted formula (quality 0.40, time 0.25, cost 0.20, safety 0.10, patient_experience 0.05); 30-row human-surgeon baseline appended.
- Default 4-entity tournament (robot vs robot, 6 rounds) plus a mixed 4-entity tournament (2 robot plus 2 human, 6 rounds); structured comparison.json plus narrative comparison_report.md plus PDF placeholder; structural-time-dimension caveat preserved.
- 6 curated ASCII diagrams: pipeline architecture, 4-arm coordination heartbeat, 60-second phase timeline, file size pyramid, composite score formula plus aggregates, on-prem LLM control loop instantiating the thesis.
- 4 ASCII bar/histogram charts: composite per iteration, composite histogram (robot vs human), per-arm resection mean (mm^3), wall-clock per iteration.
- 4 narrative reports: run summary, process log, final report, limitations.
- Top-level main README updated with the v0.2.0 outputs pipeline ASCII and the new `outputs/` subtree in the repository structure block.
- yamllint cleanup of `config/kinematics_4arm.yaml` to expand the joint_limits_per_arm block-flow entries into block-mapping form. yamllint -d relaxed config/ now exits with no warnings.
- CI verification log under `2030-gbm-1min/outputs/logs/ci_verification.log` capturing the green state of every CI lint-and-format gate.

## Contributors

@kevinkawchak
@claude
@openai

## Notes

- The v0.2.0 outputs are reproducible bit for bit from seed 20260510. Re-running the pipeline reproduces every Parquet, JSON, and JSONL artifact under `2030-gbm-1min/outputs/`.
- The 1-minute robot scenario trivially beats the 1-hour human-baseline scenario on the time dimension; this advantage is structural and not a fair pairwise comparison. The flagging is preserved in every comparison rationale.
- The C++20 control loop, C++20 1 kHz heartbeat layer, and Rust 2021 high-throughput runner are documented but not compiled in this run; the sandbox lacks `g++`, `clang++`, `cargo`, and `rustc`. A future re-run on a host with the full toolchain will exercise the binary path. See `2030-gbm-1min/outputs/reports/limitations.md`.
- The PNG and HTML files under `outputs/viz/` are mirrored from the upstream `viz/` snapshots; matplotlib-based PNG re-renders require the optional `matplotlib` and `kaleido` packages.
- The release-aggregate L0 raw archive (~416 MB across 16 iterations) lives on Zenodo only at DOI 10.5281/zenodo.18445179. The 16 per-iteration `*_L0_raw.zenodo_pointer.json` files contain PLACEHOLDER `zenodo_record_id` and `sha256` fields that point at the upstream record.
- All committed files honor the 10 MB per-file cap and the 5 MB committed-Parquet cap. The CI workflow enforces both.

## Release title

v0.1.0 - 4-Arm 1-Minute Glioblastoma Trial Simulation (Medtronic NeuroSpeed 1.0)

## Summary

This release lands the first complete project under robotic-surgeries: the v3.9.1 4-arm 1-minute glioblastoma resection simulation (`2030-gbm-1min/`). The project operationalizes the on-premises LLM thesis at the upper edge of feasible robotic speed: a hypothetical 2030 Medtronic NeuroSpeed 1.0 four-arm parallel stereotactic neurosurgical robot completes a maximal safe gross-total resection of a 4.2 cm right frontal IDH-wildtype glioblastoma in 60 seconds. Per-arm sensors stream at mixed 1 kHz commands plus 10 kHz force; a deterministic 1 kHz heartbeat broadcasts 32-byte status frames with a 1 ms deadline; cumulative tip force across the 4 arms is capped at 12 N on the patient frame; the E-stop budget is 5 ms with a 100 microsecond emergency arm-park trigger. Sixteen deterministic iterations sweep noise, gain, IK tolerance, and heartbeat jitter; per-iteration L1 to L3 plus events Parquet aggregates plus the per-iteration L0 raw Zenodo pointer JSON live under `2030-gbm-1min/data/iterations/`. The release-aggregate L0 raw archive (416 MB across 16 iterations) is deposited to Zenodo (DOI 10.5281/zenodo.18445179).

## Features

- 4-arm Medtronic NeuroSpeed 1.0 specification with 7-DOF DH parameters, per-arm tool assignment (hybrid u-w-p, bipolar+irr, suction+col, iMRI+ALA), and per-arm safety limits (5.0 N tip, 1.0 N lateral, 5 ms E-stop, 8 mm inter-arm clearance).
- 4-phase 60-second procedure timeline (dural opening final 5 s, bulk resection 40 s, margin assessment 10 s, hemostasis withdrawal 5 s) with cross-arm coordination.
- 200-channel sensor schema (50 channels per arm times 4 arms) in JSON Schema 2020-12, Protocol Buffers 3, and Apache Avro.
- Deterministic per-arm sensor sample JSONL and CSV files, deterministic per-arm xyz command CSV samples, and a 60-line ASCII per-second xyz path visualization.
- Python 3.10 ingest, mapping, simulation orchestrator, metrics, and on-prem LLM tournament agent (Anthropic claude-opus-4-7 default, Ollama optional).
- C++20 real-time control loop and 1 kHz heartbeat sender / receiver layer compatible with Linux, MacOS, and Windows toolchains.
- Rust 2021 high-throughput simulation runner with Cargo manifest and optional CUDA feature flag for NVIDIA A100 GPU acceleration.
- 16-iteration sweep generates 80 per-iteration Parquet files (L1 50 ms, L2 1 s, L3 per-phase, events, L0 raw Zenodo pointer JSON) plus the per-release index.jsonl manifest, the cross-iteration DuckDB analytical store, and the iteration_run.txt log.
- Comparison methodology with composite score formula (Quality 0.40, Time 0.25 with structural-advantage call-out, Cost 0.20, Safety 0.10, Patient experience 0.05), 30-row human-surgeon baseline carry-forward across 6 international centers, structured comparison.json, narrative comparison_report.md plus PDF, self-contained Plotly metrics_dashboard.html, and per_arm_contribution.png chart.
- Immutable v3.9.1 release snapshot under `2030-gbm-1min/releases/v3.9.1/` with manifest.json, metrics.json, iterations_index.jsonl, sample_seeds.txt, and zenodo_doi.txt.
- Top-level main README, CHANGELOG, references, and v0.1.0 release notes plus the GitHub Actions CI workflow that exercises ruff format, ruff check, yamllint, and the file size cap on Python 3.10, 3.11, and 3.12.

## Contributors

@kevinkawchak
@claude
@openai
@google-gemini

## Notes

- The 1-minute scenario trivially beats the 1-hour scenario on the time dimension; this advantage is structural and not a fair pairwise comparison. The comparison report and the LLM judge prompt explicitly flag this.
- The 16-iteration committed footprint is approximately 9.7 MB. The release-aggregate L0 raw (416 MB across 16 iterations) lives on Zenodo only; pointer JSON files in `data/` and `data/iterations/` resolve to the deposition.
- All committed files honor the 10 MB per-file cap and the 5 MB committed-Parquet cap. The CI workflow enforces both.
- Python and C++ source files reference IEC 80601-2-77 (per-arm 5.0 N tip, 1.0 N lateral, 5 ms E-stop), IEC 62304 (safety-critical software lifecycle at the 1 kHz heartbeat layer), and 21 CFR 50.30 (task-order lifecycle).
- All instruction files in `kevinkawchak/physical-ai-oncology-trials/competitions/instructions/one_minute_variant/` were read for shared context; no commits were made to that repository under this release.
