# 2030 PDAC 1-Minute Draft Paper Template (May 15, 2026)

This directory holds the bracketed draft LaTeX paper template for the
project titled **2030: 60 Second Pancreatic Cancer Whipple Surgery +
Daraxonrasib Simulation**. The template ships with section-level
processing instructions inside `[brackets]` so a future Claude Code
Opus 4.7 1M Max session can expand the draft into the final 70 plus
page paper at `2030-pdac-1min/paper/full-paper/` without re-discovering
which directories and files belong in each section. The bracketed
instructions are **not** processed in the current commit; they are
read by the downstream pass.

[![Paper DOI](https://img.shields.io/badge/Paper%20DOI-10.5281%2Fzenodo.20196639-blue)](https://doi.org/10.5281/zenodo.20196639)
[![Repo DOI](https://img.shields.io/badge/Repo%20DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Release](https://img.shields.io/badge/Release-v0.8.0-brightgreen.svg)](../../../releases.md)
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Variant](https://img.shields.io/badge/Variant-1%20Minute-orange.svg)](../../README.md)
[![Disease](https://img.shields.io/badge/Disease-PDAC-purple.svg)](../instructions/README.md)
[![Adjuvant](https://img.shields.io/badge/Adjuvant-Daraxonrasib-yellow.svg)](https://doi.org/10.5281/zenodo.18099351)
[![CI](https://img.shields.io/badge/CI-lint--and--format-green.svg)](../../../.github/workflows/ci.yml)

## Title page metadata

```
Title:    2030: 60 Second Pancreatic Cancer Whipple Surgery +
          Daraxonrasib Simulation (two lines, centered)
Author:   Kevin Kawchak  (green ORCID logo + https://orcid.org/0009-0007-5457-8667)
Affil:    CEO ChemicalQDevice
DOI:      10.5281/zenodo.20174131  (https://doi.org/10.5281/zenodo.20174131)
Date:     May 15, 2026
```

The abstract sits on the title page directly under the author block.
The disclaimer follows the abstract (two lines). The Introduction
section starts on the title page (page 1). The Table of Contents is
the first item on page 2. The remaining sections follow in the order
listed below.

## Pipeline diagram (8-arm 60-second 1-minute Whipple plus drug)

```
  8-Arm Sensor Streams         Per-Arm XYZ Commands     1-Min vs Human Compare
  (80 ch/arm x 8 arms,    --> (per-arm phase-       --> (on-prem LLM judge,
   640 ch total at mixed       conditioned 10 kHz       4-entrant tournament,
   10 kHz + 100 kHz force)     with 3 ms e-stop)        + Dutch human cohort)
  +-----------------------+    +-----------------------+   +----------------+
  | Arm 1 dissect SMV     | -> | Per-arm x, y, z, q,   |-> | Quality 0.30   |
  | Arm 2 dissect PV      |    | linear_vel up to       |   | Time     0.20  |
  | Arm 3 hep artery ctrl |    | 1,200 mm/s, force      |   | Cost     0.15  |
  | Arm 4 NIR + ICG IM    |    | clamp 3 N/arm, 18 N    |   | Safety   0.15  |
  | Arm 5 PJ ring tension |    | cumulative cap, tool,  |   | PtExp    0.05  |
  | Arm 6 bipolar coag    |    | 9-state command enum   |   | AnastQ   0.15  |
  | Arm 7 suction         |    | + 10 kHz heartbeat     |   | structural-t   |
  | Arm 8 imaging final   |    |   watchdog 100 us      |   | weight delta   |
  +-----------------------+    +-----------------------+   +----------------+
        |                          |                          |
        v                          v                          v
  +-----------------------+    +-----------------------+   +----------------+
  | PancreSpeed 1.0 (2030)|    | 8-phase 60s timeline  |   | Robot 93.735   |
  | 8 arms x 7 DOF, 56    |    | P1 Kocher 0-6s, P2    |   | Human 47.0%    |
  | DOF total, 0.05 mm    |    | vasc 6-16s, P3 unc    |   | ideal outcome  |
  | RMS at 1,200 mm/s,    |    | 16-24s, P4 spec       |   | (Dutch 2025    |
  | 3 ms e-stop, 1,600    |    | 24-32s, P5 PJ 32-42s, |   | n=1000 cohort) |
  | mm cubed per s peak   |    | P6 HJ 42-48s, P7 GJ   |   | conf >= 0.95   |
  | hybrid u-w-p removal  |    | 48-54s, P8 hem 54-60s |   | (1-min vs 4-8h)|
  +-----------------------+    +-----------------------+   +----------------+
           |                                |                       |
           v                                v                       v
  +-----------------------------------------------------------------------------+
  | v0.8.0: Bracketed draft LaTeX paper at                                      |
  | 2030-pdac-1min/paper/draft-paper/ populated by Claude Code Opus 4.7 1M Max  |
  | from instructions/, codegen/, execution/, and inputs/. Downstream Claude    |
  | Code pass expands the bracketed instructions into the final 70+ page paper  |
  | at 2030-pdac-1min/paper/full-paper/. Compiles as PDF in Overleaf with       |
  | pdflatex + bibtex + pdflatex + pdflatex. References carry DOIs + URLs +     |
  | clickable GitHub + Zenodo links.                                            |
  +-----------------------------------------------------------------------------+
```

## File layout

```
2030-pdac-1min/paper/draft-paper/
  README.md                 (this file)
  main.tex                  (preamble, title page, TOC, \input lines)
  new_paper.sty             (style file; 11 pt body, 1 in margins,
                            widow/orphan suppression, table columns,
                            small-caps Abstract heading, raggedright)
  references.bib            (DOI + URL bearing bibliography; clickable
                            GitHub and Zenodo URLs preserved in note)
  LaTeX Source Files.zip    (Overleaf-ready bundle of all the above
                            plus sections/; created in the final
                            error-fixing commit of this PR)
  sections/
    abstract.tex            (one paragraph + bracketed instructions)
    introduction.tex        (FDA RTCT extension + on-prem LLM thesis +
                            transition to 60-second Whipple + brackets)
    methods.tex             (PancreSpeed 1.0, 640-ch sensor stack, xyz
                            mapping, 32 iterations, 4-entrant tournament,
                            Daraxonrasib integration + brackets)
    results.tex             (1001-record sensor sample feat, leaderboard
                            93.735, advisory distribution + brackets)
    discussion.tex          (significance, FDA framing, on-prem LLM
                            single-robot error minimization, head start,
                            practical real-life insights + brackets)
    limitations_future.tex  (approximations vs generated vs executed,
                            60-min vs 1-min deltas, future tracks +
                            brackets)
    conclusions.tex         (artifact headline, persistent themes,
                            safety implications + brackets)
    back_matter.tex         (Acknowledgments, Ethical Disclosures,
                            Rights and Permissions, Cite This Article,
                            Data Availability)
```

## Section inventory

| Order | Section | File | Approx. length when expanded |
|:------|:--------|:-----|:-----------------------------|
| 1 | Abstract | sections/abstract.tex | 1 paragraph (about 900 chars) |
| 2 | Introduction | sections/introduction.tex | 5 subsections, about 4 pages |
| 3 | Methods | sections/methods.tex | 7 subsections, about 8 pages |
| 4 | Results | sections/results.tex | 7 subsections, about 8 pages |
| 5 | Discussion | sections/discussion.tex | 5 subsections, about 5 pages |
| 6 | Limitations and Future Work | sections/limitations_future.tex | 5 subsections, about 6 pages |
| 7 | Conclusions | sections/conclusions.tex | 4 thematic blocks, about 3 pages |
| 8 | References | references.bib (ieeetr style) | 30+ entries with DOI + URL + GitHub + Zenodo |
| 9 | Back Matter | sections/back_matter.tex | 5 short sections |

## AVAILABLE DIRECTORIES (upstream, read-only context)

The future Claude Code Opus 4.7 1M Max pass that expands the bracketed
instructions in this template draws on four read-only context trees.

**A. Instructions to generate code** (read-only context):

- `kevinkawchak/robotic-surgeries/tree/main/2030-pdac-1min/paper/instructions/`. Hand-authored files include `README.md`, `pdac_context_1min.md`, `robot_specification_pancrespeed.md`, `sensor_specification_100khz.md`, `multi_arm_coordination_8arm.md`, `vascular_safety_protocol.md`, `anastomosis_protocols.md`, `daraxonrasib_integration.md`, `competition_protocol.md`, `file_size_pyramid_1min.md`, `chunking_strategy.md`, `file_format_conventions.md`, `runtime_environments.md`, `ci_compliance_checklist.md`, `pr_workflow.md`, `gbm_errors_addressed.md`, `zenodo_archive_protocol.md`, `ascii_diagram_guide.md`, `commit_01_overview_1min.md`, `commit_02_sensors_1min.md`, `commit_03_xyz_8arm.md`, `commit_04_iterations_1min.md`, `commit_05_competition_1min.md`, `commit_06_error_fixes.md`, `commit_07_repository_updates.md`, `lint_verification.md`.

**B. Code generation** (read-only context):

- `kevinkawchak/robotic-surgeries/tree/main/2030-pdac-1min/paper/codegen/`. Notable subdirs: `docs/`, `config/`, `schemas/`, `src/{sensors,mapping,control,coordination,vascular,anastomosis,daraxonrasib,simulation,metrics,llm,zenodo}/`, `data/`, `prompts/`, `results/`, `viz/`, `notebooks/`, `releases/v0.6.0/`, plus `CROSS_REFERENCES.md` and `pyproject.toml`.

**C. Code execution** (read-only context):

- `kevinkawchak/robotic-surgeries/tree/main/2030-pdac-1min/paper/execution/`. Notable subdirs: `sensors/` (the 1001-record `sensor_sample_8arm.jsonl` Phase 5 first 100 ms feat), `xyz_mapping/`, `iterations/`, `metrics/`, `comparison/`, `coordination/`, `vascular/`, `anastomosis/`, `daraxonrasib/`, `diagrams/`, `viz/`, `results/`, `notebooks/`, `tests/`, `logs/`, `zenodo/`, plus `PROCESS.md` and `CROSS_REFERENCES.md`.

**D. Prior author research** (read-only context):

- `kevinkawchak/robotic-surgeries/tree/main/2030-pdac-1min/paper/inputs/`. Subdirs: `paper-1/` through `paper-4/` (the 4 author prior PDAC papers), `daraxonrasib-1/` (Daraxonrasib LLM trial summary), `research-1/` (Daraxonrasib clinical trial historical timeline), `research-2/` (Whipple procedure evidence baseline).
- `kevinkawchak/robotic-surgeries/tree/main/2030-gbm-1min/paper/full-paper/final-paper/`. The v0.4.0 GBM paper that anchors the cross-study comparison.

## Compile recipe

The LaTeX paper compiles cleanly on Overleaf (recommended) and on
any local `pdflatex` + `bibtex` installation. The expected sequence is:

```
pdflatex main.tex
bibtex   main
pdflatex main.tex
pdflatex main.tex
```

Do not compile the PDF as part of this draft-template population
pass. The PDF rendering is left to Overleaf or to the user's local
install.

## LaTeX Source Files.zip recipe

The Overleaf-ready bundle is created on demand from the LaTeX sources
in this directory. The minimal recipe (Linux, MacOS) is:

```
cd 2030-pdac-1min/paper/draft-paper
zip -r "LaTeX Source Files.zip" main.tex new_paper.sty references.bib README.md sections/
```

On Windows PowerShell:

```
cd 2030-pdac-1min\paper\draft-paper
Compress-Archive -Path main.tex,new_paper.sty,references.bib,README.md,sections -DestinationPath "LaTeX Source Files.zip"
```

The resulting zip uploads directly to Overleaf via **New Project ->
Upload Project**. The orcid_icon.png file is optional; new_paper.sty
falls back to a green "iD" tag if the PNG is missing.

## Formatting invariants (must be preserved downstream)

These invariants are non-negotiable. A downstream Claude Code pass
that violates any of them must self-correct before reporting completion.

1. **Single dashes only** throughout the body. Do not introduce em
   dashes, en dashes, double dashes, or triple dashes.
2. **Black text** throughout. `\hypersetup` forces `urlcolor`,
   `linkcolor`, `citecolor`, and `filecolor` to black. ORCID green is
   the only non-black accent and is restricted to the ORCID logo and
   the dark blue section heading accent provided by `new_paper.sty`.
3. **Raggedright table columns**. Every table cell must use a column
   type that starts with `\raggedright\arraybackslash`, for example
   `{>{\raggedright\arraybackslash}p{2cm}}`. Every width value in
   every table must have `\raggedright\arraybackslash` prepended.
4. **No widows, no orphans**. `\widowpenalty=10000` and
   `\clubpenalty=10000` in `new_paper.sty` forbid single-line top or
   bottom isolation.
5. **No text running off the right margin**. `\sloppy`,
   `\emergencystretch=3em`, and `\UrlBreaks` in `main.tex` cover the
   common cases.
6. **No large white spaces between words**. River spacing is
   controlled by `\tolerance=1200` and `\emergencystretch`.
7. **Symbol correction**. Use `\S` for the section sign where the
   semantics are "section" (for example `\S 3.1`). Do not introduce
   `SS` or any character not in the prior template's allowed set.
8. **DOIs and URLs in the bibliography**. Every `references.bib`
   entry that has a DOI carries a `doi` field, a `url` field that
   resolves through `https://doi.org/<doi>`, and a `note` field that
   embeds both the GitHub URL and the Zenodo URL inside `\url{...}`
   when the entry is a repository-style reference.
9. **Page-level self-standing layout**. Each section and page should
   read self-standingly without overcrowding. Some white space is
   acceptable; large empty pages are not.
10. **Avoid 1 to 2 word lines** at the top or bottom of a page.

## Senior-author final-pass checklist (downstream)

A senior-author final pass closes the population step. The checklist is:

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

The repository CI matrix (`.github/workflows/ci.yml`) runs
`ruff format --check`, `ruff check`, and `yamllint -d relaxed` on
Python 3.10, 3.11, and 3.12 against the `2030-gbm-1min/` tree only.
The new files under `2030-pdac-1min/paper/draft-paper/` are LaTeX
and Markdown only and live outside the CI matrix working directory,
so this PR does not regress the upstream CI
`Cl / lint-and-format (3.10) (pull...)`,
`(3.11) (pull...)`, or
`(3.12) (pull...)` checks.

## License

The paper template inherits the repository MIT license for code
artifacts. The paper text itself is distributed under the Creative
Commons Attribution 4.0 International License (CC BY 4.0).
