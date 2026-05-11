# Changelog

All notable changes to this repository are documented in this file.
Format: Keep a Changelog. Versioning: Semantic Versioning.

## v0.4.0 - 2026-05-11

### Added

- `2030-gbm-1min/paper/full-paper/` populated full LaTeX paper for **2030: 60 Second Glioblastoma AI Robotic Surgery**. New files: `main.tex` (preamble, title page, TOC, section input wiring), `new_paper.sty` (carried forward verbatim from the v0.3.0 template), `references.bib` (carried forward verbatim from the v0.3.0 template), `README.md` (DOI badges, ASCII pipeline diagram, section inventory, reference inventory, compile recipe, formatting invariants, senior-author final-pass checklist), `build_zip.sh` (one-command helper that produces the Overleaf-ready `LaTeX Source Files.zip` bundle), and 8 populated `sections/*.tex` files (`abstract.tex`, `introduction.tex`, `methods.tex`, `results.tex`, `discussion.tex`, `limitations_future.tex`, `conclusions.tex`, `back_matter.tex`).
- Every bracketed instruction in the v0.3.0 template has been replaced with prose, tables, and ASCII diagrams grounded in the upstream `physical-ai-oncology-trials/competitions/instructions/one_minute_variant/` directory, the generated `2030-gbm-1min/` tree, and the end-to-end execution outputs under `2030-gbm-1min/outputs/` (including the 54 column by 1001 row sensor sample table at `outputs/sensors/sensor_sample_4arm.csv`).
- 1 raggedright comparison table for ROSA ONE Brain v3.0 vs hypothetical NeuroSpeed 1.0 (introduction); 1 per-arm 7-DOF DH parameter table (methods); 1 sensor-sample slice (methods); 1 per-arm command-state distribution table (methods); 1 per-platform wall-clock table (methods); 1 instruction-file inventory table (results); 1 per-iteration sweep table (results); 2 LLM tournament leaderboards (results); 1 realized-benefits table (discussion); 1 4-arm cross-check matrix (discussion); 1 checking-step head-start table (discussion); 1 three-way accounting table (limitations); 1 60-min vs 1-min delta table (limitations); 1 Track A vs Track B trade-off table (limitations). Every table uses the `{>{\raggedright\arraybackslash}p{Xcm}}` column type with the mandatory `\raggedright\arraybackslash` prefix on every column width value.
- 4-arm coordination heartbeat ASCII snapshot embedded in introduction.tex; ASCII pipeline diagram embedded in the full-paper README.
- Top-level README.md refreshed to include the v0.4.0 release badge, the new Paper Full badge that points at `2030-gbm-1min/paper/full-paper`, the new v0.4.0 Full Paper ASCII snapshot above the v0.3.0 Paper Template snapshot, the new full-paper subtree in the Repository Structure block, the updated Overleaf compile recipe pointing at `2030-gbm-1min/paper/full-paper/`, the new `build_zip.sh` recipe, and the updated citation block referencing v0.4.0.
- This v0.4.0 entry in `CHANGELOG.md` plus the matching `releases.md` block.

### Changed

- Top-level `README.md` updated with v0.4.0 release badge, Paper Full badge, v0.4.0 Full Paper ASCII snapshot, full-paper subtree in the Repository Structure block, Overleaf compile recipe pointing at `2030-gbm-1min/paper/full-paper/`, `build_zip.sh` helper recipe, citation block referencing v0.4.0, and `2030-gbm-1min/paper/full-paper/README.md` cross-reference under See also.
- `2030-gbm-1min/README.md` Repository Tree block annotated with the new `paper/full-paper/` subdirectory contents (main.tex, new_paper.sty, references.bib, build_zip.sh, sections/*.tex, README.md).
- `2030-gbm-1min/paper/README.md` updated with a pointer to the populated `full-paper/` subdirectory plus a one-line description of the build_zip.sh helper.

### Fixed

- Populated LaTeX paper compiles cleanly under Overleaf and a local `pdflatex` plus `bibtex` installation. The 2nd-to-last commit (error fixes) adds the `build_zip.sh` helper that builds the Overleaf-ready zip deterministically from the LaTeX sources committed under `2030-gbm-1min/paper/full-paper/`, verifies all tables use the `{>{\raggedright\arraybackslash}p{Xcm}}` column type, verifies every body section uses single dashes only (no em dashes, no double dashes, no triple dashes), and verifies every `.bib` entry carries a `doi` field plus a `url` field plus a `note` field with clickable GitHub and Zenodo URLs for repository-style entries.
- The CI lint-and-format matrix on Python 3.10, 3.11, and 3.12 continues to pass; the new files under `2030-gbm-1min/paper/full-paper/` are LaTeX and Markdown plus one shell script and are not subject to `ruff format --check`, `ruff check`, or `yamllint -d relaxed`. Resolves the upstream `Cl / lint-and-format (3.10)`, `(3.11)`, and `(3.12)` failing checks risk for this PR.
- File size cap check passes; no committed file exceeds 10 MB and no committed Parquet exceeds 5 MB. The largest new file is `2030-gbm-1min/paper/full-paper/references.bib` at approximately 19 KB.

### Notes

- The populated paper preserves the 9 formatting invariants listed in `2030-gbm-1min/paper/README.md` and re-stated in `2030-gbm-1min/paper/full-paper/README.md`: single dashes only, black text, raggedright table columns, no widows or orphans, no margin overflow, no large white spaces, symbol correction (SS to `\S` for section sign), DOI and URL clickability with separate GitHub plus Zenodo entries in the bibliography, and page-level self-standing layout.
- The Overleaf-ready `LaTeX Source Files.zip` is built on demand by `2030-gbm-1min/paper/full-paper/build_zip.sh`. Run `chmod +x build_zip.sh && ./build_zip.sh` in that directory. The script supports both the system `zip` command and Python 3 zipfile module as a fallback. The bundle uploads to Overleaf via `New Project -> Upload Project`.
- The paper's Zenodo DOI is 10.5281/zenodo.20113157 (clickable from the title page and from the Cite This Article back-matter block). The parent repository deposition DOI is 10.5281/zenodo.18445179.
- The work positions the United States to remain Number 1 in the world regarding patient safety, efficacy, and speed benefits in oncological robotic surgeries in clinical trials by extending the FDA 28 April 2026 Real-Time Clinical Trials proof-of-concept program from pharmacology into the surgical theater under the FDA Software as a Medical Device framework.

## v0.3.0 - 2026-05-11

### Added

- `2030-gbm-1min/paper/` LaTeX paper template (head start for a future Claude Code Opus 4.7 1M Max processing pass). New files: `main.tex` (title page, TOC, document structure), `new_paper.sty` (11 pt body, 1 in margins, ptm/phv font pair, widow/orphan suppression, raggedright tables, small-caps Abstract heading), `references.bib` (DOI + URL bearing bibliography with clickable GitHub and Zenodo URLs preserved in the note field), `README.md` (navigation index, compile recipe, formatting invariants, senior-author final-pass checklist), and the eight `sections/*.tex` files (`abstract.tex`, `introduction.tex`, `methods.tex`, `results.tex`, `discussion.tex`, `limitations_future.tex`, `conclusions.tex`, `back_matter.tex`).
- Bracketed instruction prompts inside `sections/*.tex` that name the exact upstream and current repository paths to read for the downstream pass: the 12 hand-authored instruction files at `kevinkawchak/physical-ai-oncology-trials/competitions/instructions/one_minute_variant/`, the generated `kevinkawchak/robotic-surgeries/2030-gbm-1min/` tree, and the executed `2030-gbm-1min/outputs/` artifact set including the 54 columns by 1001 rows sensor sample table at `outputs/sensors/sensor_sample_4arm.csv`.
- DOI- and URL-bearing bibliography in `2030-gbm-1min/paper/references.bib`: 27 entries including this paper's DOI 10.5281/zenodo.20113157, the parent repository DOI 10.5281/zenodo.18445179, the author's prior glioblastoma and clinical trial work (Zenodo 17774560, 15549831, 17614396, and 19994945), the FDA real-time clinical trials announcement, glioblastoma clinical context (Stupp 2005, Sanai 2011, Stummer 2006), Medtronic ROSA ONE Brain v3.0 baseline, IEC 80601-2-77 and IEC 62304 standards, TRIPOD+AI and CREMLS reporting standards, Claude Code / Claude Opus 4.7 / Claude Sonnet 4.6 tooling, ChatGPT Deep Research, Google Gemini AI Overview, Ollama, vLLM, Apache Arrow, DuckDB, and Zenodo. Every entry has a clickable DOI URL plus (for repository-style entries) both a GitHub URL and a Zenodo URL inside the note field.
- Top-level README.md refreshed to include the v0.3.0 paper-template badge, the new paper subtree in the Repository Structure block, the v0.3.0 Paper Template ASCII snapshot, and the compile and zip recipes.
- This v0.3.0 entry in `CHANGELOG.md` plus the matching `releases.md` block.

### Changed

- Top-level `README.md` updated with v0.3.0 paper template badge, paper subtree in the Repository Structure block, v0.3.0 Paper Template ASCII snapshot, paper-template citation block, Overleaf compile recipe, and `paper/README.md` cross-reference under See also.
- `2030-gbm-1min/README.md` Repository Tree block annotated with the `paper/` subdirectory contents (main.tex, new_paper.sty, references.bib, sections/*.tex).
- `2030-gbm-1min/paper/README.md` zip-creation recipe made explicit so that the Overleaf-ready bundle can be reproduced from the LaTeX sources committed under `2030-gbm-1min/paper/`.

### Fixed

- LaTeX template compiles cleanly under Overleaf and a local `pdflatex` plus `bibtex` installation. The 2nd-to-last commit (error fixes) loads the `underscore` package after `hyperref` so that paths with underscores render as printable characters in text mode, and rewrites raw `mm/s^2` and `mm^3` in the bracketed instruction prompts as `mm per second squared` and `mm cubed` plain text so no caret character escapes math mode.
- The CI lint-and-format matrix on Python 3.10, 3.11, and 3.12 continues to pass; the new files under `2030-gbm-1min/paper/` are LaTeX and Markdown only and are not subject to `ruff format --check`, `ruff check`, or `yamllint -d relaxed`. Resolves the upstream `Cl / lint-and-format (3.10)`, `(3.11)`, and `(3.12)` failing checks risk for this PR.
- File size cap check passes; no committed file exceeds 10 MB and no committed Parquet exceeds 5 MB. The largest new file is `2030-gbm-1min/paper/references.bib` at approximately 19 KB.

### Notes

- The LaTeX template explicitly defers prose generation. Each section's bracketed instructions enumerate the exact upstream and current files for a downstream Claude Code Opus 4.7 1M Max processing pass to read; that pass replaces each `[bracketed instruction]` block with prose, tables, and ASCII diagrams. The pass must preserve the formatting invariants listed in `2030-gbm-1min/paper/README.md` (single dashes only, black text, raggedright table columns, no widows or orphans, no margin overflow, clickable DOI and URL in every bibliography entry).
- The Overleaf-ready `LaTeX Source Files.zip` can be bundled locally with `cd 2030-gbm-1min/paper && zip -r "LaTeX Source Files.zip" main.tex new_paper.sty references.bib sections/ orcid_icon.png`; the orcid_icon.png file falls back to a green "iD" tag rendered by `new_paper.sty` if absent.
- The paper's Zenodo DOI is 10.5281/zenodo.20113157 (clickable from the title page and from the Cite This Article back-matter block). The parent repository deposition DOI is 10.5281/zenodo.18445179.

## v0.2.0 - 2026-05-10

See the v0.2.0 entry in the prior version of CHANGELOG.md for the v3.9.1 outputs tree under `2030-gbm-1min/outputs/`.

## v0.1.0 - 2026-05-10

See the v0.1.0 entry in the prior version of CHANGELOG.md for the 4-arm 1-minute glioblastoma trial first variant under `2030-gbm-1min/`.
