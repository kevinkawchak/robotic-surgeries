# Release Notes

This file tracks every tagged release of the robotic-surgeries repository.
Releases follow semantic versioning. The first project to land here is the
4-arm 1-minute glioblastoma trial in `2030-gbm-1min/` (project version
v3.9.1, repository release v0.1.0). The v0.2.0 release publishes the
end-to-end run outputs of the same pipeline. The v0.3.0 release lands the
LaTeX paper template for the same project under `2030-gbm-1min/paper/`.
The v0.4.0 release lands the populated full LaTeX paper under
`2030-gbm-1min/paper/full-paper/`.

## Release title

v0.4.0 - 2030 GBM 1-Minute Full LaTeX Paper (Populated, Overleaf Ready)

## Summary

This release lands the populated full LaTeX paper at
`2030-gbm-1min/paper/full-paper/` titled **2030: 60 Second Glioblastoma AI
Robotic Surgery**. Every bracketed instruction in the v0.3.0 template has
been replaced with prose, tables, and ASCII diagrams grounded in the
upstream `kevinkawchak/physical-ai-oncology-trials/competitions/instructions/one_minute_variant/`
directory, the generated `2030-gbm-1min/` tree, and the end-to-end
execution outputs under `2030-gbm-1min/outputs/`. The populated paper
opens with the on-premises repository based LLM thesis and frames the
work as an opportunistic extension of the FDA 28 April 2026 Real-Time
Clinical Trials announcement from pharmacology into the surgical theater.
The headline result is the robot mean composite score of 88.53 versus
human mean composite 70.35 across the mixed 4-entity LLM tournament,
with the structural-time-dimension caveat (1-minute robot vs 1-hour human
baseline) preserved in every rationale. The exceptional processing feat
that no human team could produce in the time budget is the 54 column by
1001 row sensor sample table at
`2030-gbm-1min/outputs/sensors/sensor_sample_4arm.csv`. The paper Zenodo
DOI is 10.5281/zenodo.20113157 and the parent repository deposition DOI
is 10.5281/zenodo.18445179; both are clickable from the title page and
from the bibliography. The full paper compiles cleanly on Overleaf and
on any local pdflatex plus bibtex installation. A one-command
`build_zip.sh` helper in the same directory produces the Overleaf-ready
`LaTeX Source Files.zip` bundle. The release also refreshes the
top-level `README.md` with the v0.4.0 release badge, the Paper Full
badge, the new full-paper subtree in the Repository Structure block,
a v0.4.0 Full Paper ASCII snapshot, the updated Overleaf compile recipe,
and an updated citation block. The CI lint and format gates on Python
3.10, 3.11, and 3.12 continue to pass because the new files under
`2030-gbm-1min/paper/full-paper/` are LaTeX and Markdown only and are
not subject to `ruff format --check`, `ruff check`, or `yamllint -d
relaxed`. No committed file exceeds 10 MB and no committed Parquet
exceeds 5 MB.

## Features

- Populated full LaTeX paper under `2030-gbm-1min/paper/full-paper/` titled **2030: 60 Second Glioblastoma AI Robotic Surgery**. Title page carries the two-line centered title, the green ORCID logo plus https://orcid.org/0009-0007-5457-8667, CEO ChemicalQDevice, the clickable Zenodo DOI 10.5281/zenodo.20113157, the May 11 2026 release date, the abstract, the mandatory disclaimer, and the keywords.
- 8 populated `sections/*.tex` files: `abstract.tex` (single 900-character paragraph anchored on the on-prem LLM thesis), `introduction.tex` (5 subsections covering FDA RTCT, GBM clinical context, NeuroSpeed vs ROSA ONE Brain v3.0 baseline, on-prem LLM thesis with 4-arm coordination ASCII, and transition to the 16-iteration sweep), `methods.tex` (6 subsections covering 12 instruction inputs, the NeuroSpeed 1.0 robot with the 7-DOF DH parameter table per arm, the 200-channel sensor stack plus the 54 column by 1001 row sample slice, the per-arm xyz mapping with all 240 commands resolving to EMIT, the 16-iteration deterministic sweep with seed 20260510 and frozen composite weights, and the cross-platform execution environment), `results.tex` (6 subsections covering the 12-file 130 KB upstream instruction inventory, the 8.2 MB generated tree, the 10 outputs subdirectories, the per-iteration sweep table, the two LLM tournament leaderboards with the 88.53 vs 70.35 headline, and the exceptional 54 column by 1001 row sensor sample feat), `discussion.tex` (5 subsections covering the 240x to 480x compression significance, the respectful FDA framing, the 4-arm cross-check matrix for LLM safety, the head-start framing with the checking-step table, and the practical real-life insights), `limitations_future.tex` (5 subsections covering the three-way approximated-generated-executed accounting, the 60-min vs 1-min formal delta table, the cross-simulation limitations, the Track A vs Track B trade-off table, and the 10 concrete future-work deliverables), `conclusions.tex` (artifact headline counts, the three persistent themes, the safety implications, and the forward path), and `back_matter.tex` (Acknowledgments, Ethical Disclosures, Rights and Permissions, Cite This Article, Data Availability).
- Style file `new_paper.sty` carried forward verbatim from the template; 11 pt body, 1 in margins, ptm/phv font pair, widow and orphan suppression at 10000, compact section spacing, justified text with controlled emergencystretch, small-caps Abstract heading, and raggedright table column types L, C, R with the mandatory `\raggedright\arraybackslash` prefix for every column width value.
- `references.bib` carried forward verbatim from the template; every entry carries a clickable DOI URL plus (for repository-style entries) both a GitHub URL and a Zenodo URL inside the note field so both render as separate clickable hyperlinks in the rendered bibliography.
- `build_zip.sh` helper at `2030-gbm-1min/paper/full-paper/build_zip.sh` that produces the Overleaf-ready `LaTeX Source Files.zip` bundle deterministically from the LaTeX sources in the same directory. The script supports both the system `zip` command and Python 3 zipfile module as a fallback. Tested on Linux Ubuntu 22.04 LTS, MacOS Apple Silicon, and Git Bash on Windows 11.
- Full-paper README at `2030-gbm-1min/paper/full-paper/README.md` with the Paper DOI, Repo DOI, Release, License, Variant, and CI badges; an ASCII pipeline diagram of the 4-arm sensor streams feeding per-arm xyz commands feeding the on-premises LLM tournament; the full file layout; the per-section length inventory; the per-category reference inventory; the compile recipe; the LaTeX Source Files.zip recipe for Linux / MacOS and Windows PowerShell; the AVAILABLE DIRECTORIES (upstream and current) for downstream processing; the 9 formatting invariants; the senior-author final-pass checklist; the CI lint and Python environment note; and the license block.
- Top-level `README.md` refreshed with the v0.4.0 release badge, the new Paper Full badge that points at `2030-gbm-1min/paper/full-paper`, the new v0.4.0 Full Paper ASCII snapshot above the v0.3.0 Paper Template snapshot, the new full-paper subtree in the Repository Structure block, the updated Overleaf compile recipe pointing at `2030-gbm-1min/paper/full-paper/`, the new `build_zip.sh` recipe, and the updated citation block referencing v0.4.0.
- `CHANGELOG.md` updated with the v0.4.0 entry under Added (the populated paper and the build_zip.sh helper), Changed (top-level README and 2030-gbm-1min README and paper README updates), Fixed (the Cl / lint-and-format Python 3.10 / 3.11 / 3.12 matrix remains green), and Notes.
- `2030-gbm-1min/paper/README.md` updated with a pointer to the populated `full-paper/` subdirectory; `2030-gbm-1min/README.md` Repository Tree block extended with the `full-paper/` subdirectory contents.

## Contributors

@kevinkawchak
@claude
@openai
@google-gemini

## Notes

- The populated full paper preserves all formatting invariants enforced by the v0.3.0 template: single dashes only throughout the body (no em dashes, no double dashes, no triple dashes); black text only via the hypersetup block in main.tex; raggedright table columns (every column width value prepends `\raggedright\arraybackslash`); widow and orphan suppression via `\widowpenalty=10000` and `\clubpenalty=10000` in new_paper.sty; no text running off the right margin via `\sloppy` and `\emergencystretch=3em`; the section sign `\S` used in place of `SS`; clickable DOIs and clickable GitHub plus Zenodo URLs in every repository-style bibliography entry; and page-level self-standing layout without overcrowding.
- The Overleaf-ready `LaTeX Source Files.zip` is built on demand from the LaTeX sources committed under `2030-gbm-1min/paper/full-paper/`. Run `./build_zip.sh` in that directory after `chmod +x build_zip.sh`. The script falls back to the Python 3 zipfile module if the `zip` command is unavailable.
- The paper's Zenodo DOI is 10.5281/zenodo.20113157 (clickable from the title page and from the Cite This Article back-matter block). The parent repository deposition DOI is 10.5281/zenodo.18445179.
- The CI lint and format gates on Python 3.10, 3.11, and 3.12 continue to pass; the new files under `2030-gbm-1min/paper/full-paper/` are LaTeX and Markdown plus one shell script and are not subject to `ruff format --check`, `ruff check`, or `yamllint -d relaxed`. The lint-and-format failing checks risk from the upstream PR template is not present in this PR.
- All committed files honor the 10 MB per-file cap and the 5 MB committed-Parquet cap.
- The work positions the United States to remain Number 1 in the world regarding patient safety, efficacy, and speed benefits in oncological robotic surgeries in clinical trials by extending the FDA 28 April 2026 Real-Time Clinical Trials proof-of-concept program from pharmacology into the surgical theater.

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

See CHANGELOG.md for v0.2.0 details; the outputs tree is reproducible from
the deterministic seed 20260510 and lives at `2030-gbm-1min/outputs/`.

## Release title

v0.1.0 - 2030 GBM 1-Minute Trial Skeleton (First Variant)

## Summary

See CHANGELOG.md for v0.1.0 details; the 4-arm 1-minute glioblastoma trial
first variant lives at `2030-gbm-1min/`.
