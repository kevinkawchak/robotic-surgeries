# 2030 GBM 1-Minute Paper Template (May 11, 2026)

This directory holds the LaTeX paper template for the project titled
**2030: 60 Second Glioblastoma AI Robotic Surgery**. The template is a
head start for a future Claude Code Opus 4.7 1M Max processing pass:
every `sections/*.tex` file carries bracketed instructions that name
the exact upstream and current repository paths to read, what to
process, how to process the files synergistically, and where to place
the resulting prose, tables, and ASCII diagrams. This README is the
navigation index for the template.

[![Paper DOI](https://img.shields.io/badge/Paper%20DOI-10.5281%2Fzenodo.20113157-blue)](https://doi.org/10.5281/zenodo.20113157)
[![Repo DOI](https://img.shields.io/badge/Repo%20DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Release](https://img.shields.io/badge/Release-v0.3.0-brightgreen.svg)](../../releases.md)
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Variant](https://img.shields.io/badge/Variant-1%20Minute-orange.svg)](../README.md)
[![CI](https://img.shields.io/badge/CI-lint--and--format-green.svg)](../../.github/workflows/ci.yml)

## Title page metadata

```
Title:    2030: 60 Second Glioblastoma AI Robotic Surgery (two lines, centered)
Author:   Kevin Kawchak  (green ORCID logo + https://orcid.org/0009-0007-5457-8667)
Affil:    CEO ChemicalQDevice
DOI:      10.5281/zenodo.20113157  (https://doi.org/10.5281/zenodo.20113157)
Date:     May 11, 2026
```

The abstract sits on the title page directly under the author block.
The disclaimer follows the abstract (two lines). The Introduction
section starts on the title page (page 1). The Table of Contents is
the first item on page 2. The remaining sections follow in the order
listed below.

## File layout

```
2030-gbm-1min/paper/
  README.md                 (this file)
  main.tex                  (preamble, title page, TOC, \input lines)
  new_paper.sty             (style file; 11 pt body, 1 in margins,
                            widow/orphan suppression, table columns,
                            small-caps Abstract heading, raggedright)
  references.bib            (DOI + URL bearing bibliography; clickable
                            GitHub and Zenodo URLs preserved in note)
  orcid_icon.png            (green ORCID logo, optional;
                            new_paper.sty falls back to a green "iD"
                            tag if absent)
  LaTeX Source Files.zip    (added in commit 14; Overleaf-ready bundle)
  sections/
    abstract.tex            (one paragraph, 900 chars target;
                            instructions in [brackets])
    introduction.tex        (FDA RTCT + on-prem LLM thesis +
                            transition to robotic surgery; bracketed)
    methods.tex             (robot, sensors, xyz, iterations, comp;
                            bracketed)
    results.tex             (sensor 54x1001 table, xyz, iterations,
                            comp leaderboards; bracketed)
    discussion.tex          (significance, FDA framing, on-prem LLM
                            advantages; bracketed)
    limitations_future.tex  (60min vs 1min deltas, approximations,
                            Track A vs Track B; bracketed)
    conclusions.tex         (artifact headline, themes, forward path;
                            bracketed)
    back_matter.tex         (Acknowledgments, Ethical Disclosures,
                            Rights and Permissions, Cite This Article,
                            Data Availability; final prose)
```

## Section order and bracketed-instruction status

The downstream 70+ page paper assembled by a future Claude Code Opus
4.7 1M Max pass replaces each `[bracketed instruction]` block with
prose, tables, and ASCII diagrams sourced from the exact directories
listed in the brackets. The bracketed instructions in this template
are NOT processed in this commit set.

| Order | Section | Bracketed prompts |
|:-----|:--------|:------------------|
| 1 | Abstract | yes |
| 2 | Introduction | yes |
| 3 | Methods | yes |
| 4 | Results | yes |
| 5 | Discussion | yes |
| 6 | Limitations and Future Work | yes |
| 7 | Conclusions | yes |
| 8 | References | no (bibliography file) |
| 9 | Acknowledgments / Ethical Disclosures / Rights and Permissions / Cite This Article / Data Availability | no (final prose) |

## AVAILABLE DIRECTORIES (upstream and current)

A future Claude Code processing pass must read from these directories
when expanding the bracketed prompts.

**A. Instructions to generate code** (read-only context):

- Primary: `kevinkawchak/physical-ai-oncology-trials/tree/main/competitions/instructions/one_minute_variant/` and subdirectories. The 12 hand-authored files are: `README.md`, `commit_01_overview_1min.md`, `commit_02_sensors_1min.md`, `commit_03_xyz_4arm.md`, `commit_04_iterations_1min.md`, `commit_05_competition_1min.md`, `file_size_pyramid_1min.md`, `glioblastoma_context_1min.md`, `multi_arm_coordination.md`, `robot_specification_neurospeed.md`, `sensor_specification_10khz.md`, `zenodo_archive_protocol.md`.
- Secondary (only if additional context is necessary): `kevinkawchak/physical-ai-oncology-trials/tree/main/competitions/instructions/`.

**B. Code generation** (read-only context):

- Primary: `kevinkawchak/robotic-surgeries/tree/main/2030-gbm-1min/` and subdirectories. Notable subdirs: `docs/`, `config/`, `schemas/`, `src/{sensors,mapping,control,coordination,simulation,metrics,llm,zenodo}/`, `data/`, `data/iterations/`, `prompts/`, `results/`, `viz/`, `notebooks/`, `logs/`, `releases/v3.9.1/`, and `paper/` (this directory).

**C. Code execution** (read-only context):

- Primary: `kevinkawchak/robotic-surgeries/tree/main/2030-gbm-1min/outputs/` and subdirectories. Notable subdirs: `sensors/` (contains the 54x1001 `sensor_sample_4arm.csv` table that no human team could produce in due time), `xyz_mapping/`, `iterations/`, `metrics/`, `comparison/`, `comparison_robot_vs_human/`, `diagrams/`, `viz/`, `reports/`, `logs/`.
- Additional context (only if necessary): `kevinkawchak/physical-ai-oncology-trials/tree/main/competitions/` and subdirectories.

## Compile recipe

The LaTeX template compiles cleanly on Overleaf (recommended) and on
any local `pdflatex` + `bibtex` installation. The expected sequence is:

```
pdflatex main.tex
bibtex   main
pdflatex main.tex
pdflatex main.tex
```

Do not compile the PDF as part of the template-population pass. Only
the LaTeX zip is provided at `2030-gbm-1min/paper/LaTeX Source Files.zip`
in the final commit of this PR.

## Formatting invariants (must be preserved downstream)

These invariants are non-negotiable. A downstream Claude Code pass
that violates any of them must self-correct before reporting completion.

1. **Single dashes only** throughout the body. Do not introduce em
   dashes, en dashes (other than in page ranges in `references.bib`),
   double dashes, or triple dashes.
2. **Black text** throughout. `\hypersetup` forces `urlcolor`,
   `linkcolor`, `citecolor`, and `filecolor` to black. ORCID green is
   the only non-black accent and is restricted to the ORCID logo.
3. **Raggedright table columns**. Every table cell must use a column
   type that starts with `\raggedright\arraybackslash`, for example
   `{>{\raggedright\arraybackslash}p{2cm}}`. Every width value in
   every table must have `\raggedright\arraybackslash` prepended.
4. **No widows, no orphans**. `\widowpenalty=10000` and
   `\clubpenalty=10000` in `new_paper.sty` forbid single-line top or
   bottom isolation. A downstream pass that produces a single or
   two-word line stranded from its paragraph must reflow.
5. **No text running off the right margin**. `\sloppy`,
   `\emergencystretch=3em`, and `\UrlBreaks` in `main.tex` cover the
   common cases; downstream prose that still runs off must shorten or
   rebreak the offending line.
6. **No large white spaces between words**. River spacing is
   controlled by `\tolerance=1200` and `\emergencystretch`. If a
   river still appears, the surrounding paragraph must be tightened
   or a `\raggedright` block applied locally.
7. **Symbol correction**. Replace `SS` with `\S` where the reference
   semantics are "section" (for example `\S 3.1`). Do not introduce
   any character not in the prior template's allowed set.
8. **DOIs and URLs in the bibliography**. Every `references.bib`
   entry that has a DOI carries a `doi` field, a `url` field that
   resolves through `https://doi.org/<doi>`, and a `note` field that
   embeds both the GitHub URL and the Zenodo URL inside `\url{...}`
   when the entry is a repository-style reference. Both render as
   separate clickable hyperlinks in the final PDF bibliography.
9. **Page-level self-standing layout**. Each section and page should
   read self-standingly without overcrowding. Some white space is
   acceptable; large empty pages are not.

## Senior-author final-pass checklist

A senior-author final pass closes the template-population step. The
checklist is:

- Symbols: every `SS` standing in for a section sign rewritten as `\S`.
- Dashes: every `--`, `---`, `\textendash`, `\textemdash` rewritten
  as a single `-`.
- Raggedright: every `p{Xcm}` column rewritten as
  `>{\raggedright\arraybackslash}p{Xcm}`.
- White space: every isolated 1 or 2 word line at the top or bottom
  of a page reflowed.
- Margin overflow: every line that runs into the right margin shortened.
- TOC: every section, subsection, Acknowledgments, Ethical
  Disclosures, Rights and Permissions, Cite This Article, Data
  Availability, and References appears in the on-screen TOC.
- DOIs: every `https://doi.org/<doi>` link in `references.bib` is
  clickable and the bibliography lists both the GitHub URL and the
  Zenodo URL for repository-style entries.
- ORCID: the green ORCID logo or "iD" tag on the title page resolves
  to `https://orcid.org/0009-0007-5457-8667`.

## CI lint and Python environment

The repository CI matrix runs `ruff format --check`, `ruff check`, and
`yamllint -d relaxed` on Python 3.10, 3.11, and 3.12 against the
entire `2030-gbm-1min/` tree. The error-fix commit in this PR ensures
the LaTeX sources, the bibliography, and the supporting Markdown all
honor the same line-length and trailing-whitespace conventions so the
upstream CI `Cl / lint-and-format` failures do not recur. See
`../../.github/workflows/ci.yml`.

## License

The paper template inherits the repository MIT license for code
artifacts. The paper text itself is distributed under the Creative
Commons Attribution 4.0 International License (CC BY 4.0).
