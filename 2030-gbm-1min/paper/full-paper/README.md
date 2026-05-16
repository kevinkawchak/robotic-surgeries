# 2030 GBM 1-Minute Full Paper (May 11, 2026)

This directory holds the populated full LaTeX paper for the project
titled **2030: 60 Second Glioblastoma AI Robotic Surgery**. The
end-to-end paper compiles as a PDF in Overleaf or any local
`pdflatex` + `bibtex` installation. This README is the navigation
index for the populated paper directory; the upstream bracketed
template lives at `../sections/` and at `../main.tex`,
`../new_paper.sty`, `../references.bib`, and `../README.md`.

[![Paper DOI](https://img.shields.io/badge/Paper%20DOI-10.5281%2Fzenodo.20113157-blue)](https://doi.org/10.5281/zenodo.20113157)
[![Repo DOI](https://img.shields.io/badge/Repo%20DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Release](https://img.shields.io/badge/Release-v0.4.0-brightgreen.svg)](../../../releases.md)
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Variant](https://img.shields.io/badge/Variant-1%20Minute-orange.svg)](../../README.md)
[![CI](https://img.shields.io/badge/CI-lint--and--format-green.svg)](../../../.github/workflows/ci.yml)

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

## Pipeline diagram (4-arm 60-second 1-minute trial)

```
   4-Arm Sensor Streams          Per-Arm XYZ Commands      1-Min vs Human Compare
   (50 ch/arm x 4 arms,    --->  (per-arm phase-      -->  (on-prem LLM judge,
   200 ch total at mixed         conditioned 1 kHz         4-entity tournament)
   1 kHz + 10 kHz force)         with 5 ms e-stop)
  +-----------------------+    +------------------------+    +----------------+
  | Arm 1 hyb u-w-p cut   | -> | Per-arm x, y, z, q,    | -> | Quality 0.40   |
  | Arm 2 bipolar coag    |    | linear_vel up to       |    | Time     0.25  |
  | Arm 3 suction collect |    | 1,000 mm/s, force      |    | Cost     0.20  |
  | Arm 4 iMRI + 5-ALA    |    | clamp 5 N/arm, tool,   |    | Safety   0.10  |
  | 1 kHz heartbeat bus   |    | 7-state command enum   |    | PtExp    0.05  |
  | 12 N cumulative cap   |    | + heartbeat watchdog   |    | structural-t   |
  +-----------------------+    +------------------------+    +----------------+
             |                             |                         |
             v                             v                         v
  +-----------------------+    +-----------------------+   +----------------+
  | NeuroSpeed 1.0 (2030) |    | 4-phase 60s timeline  |   | Robot 88.53    |
  | 4 arms x 7 DOF, 28    |    | P1 dural 0-5s, P2     |   | Human 70.35    |
  | DOF total, 0.1 mm RMS |    | bulk 5-45s @ 800      |   | Robot wins all |
  | at 1,000 mm/s, 5 ms   |    | mm cubed per s, P3    |   | 4 r-v-h pairs  |
  | e-stop, 800 mm cubed  |    | margin 45-55s, P4     |   | conf 0.955 to  |
  | per s peak via hybrid |    | hemostasis 55-60s     |   | 1.000          |
  | u-w-p removal         |    | (pre-op precomputed)  |   | (1-min vs 1-h) |
  +-----------------------+    +-----------------------+   +----------------+
             |                             |                       |
             v                             v                       v
  +-----------------------------------------------------------------------------+
  | v0.4.0: Full LaTeX paper at 2030-gbm-1min/paper/full-paper/ populated by    |
  | Claude Code Opus 4.7 1M Max from the bracketed template at                  |
  | 2030-gbm-1min/paper/sections/. Compiles as PDF in Overleaf with pdflatex    |
  | plus bibtex plus pdflatex plus pdflatex. References carry DOIs plus URLs    |
  | plus clickable GitHub plus Zenodo links. ORCID iD links to                  |
  | https://orcid.org/0009-0007-5457-8667.                                      |
  +-----------------------------------------------------------------------------+
```

## File layout

```
2030-gbm-1min/paper/full-paper/
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
    abstract.tex            (one paragraph, target 900 chars)
    introduction.tex        (FDA RTCT + on-prem LLM thesis +
                            transition to 60-second robotic surgery)
    methods.tex             (12 instructions, NeuroSpeed 1.0, sensor
                            stack, xyz mapping, iterations, code env)
    results.tex             (instruction count, code tree, end-to-end
                            outputs, iteration sweep, LLM tournament,
                            54 x 1001 sensor sample feat)
    discussion.tex          (significance, FDA framing, on-prem LLM
                            single-robot error minimization, head
                            start, practical real-life insights)
    limitations_future.tex  (approximations vs generated vs executed,
                            60min vs 1min deltas, cross-simulation
                            limits, Track A vs Track B futures)
    conclusions.tex         (artifact headline, three persistent
                            themes, safety implications, forward path)
    back_matter.tex         (Acknowledgments, Ethical Disclosures,
                            Rights and Permissions, Cite This Article,
                            Data Availability)
```

## Section inventory

| Order | Section | File | Approx. length |
|:------|:--------|:-----|:---------------|
| 1 | Abstract | sections/abstract.tex | 1 paragraph (about 900 chars) |
| 2 | Introduction | sections/introduction.tex | 5 subsections, about 4 pages |
| 3 | Methods | sections/methods.tex | 6 subsections, about 6 pages |
| 4 | Results | sections/results.tex | 6 subsections, about 6 pages |
| 5 | Discussion | sections/discussion.tex | 5 subsections, about 4 pages |
| 6 | Limitations and Future Work | sections/limitations_future.tex | 5 subsections, about 5 pages |
| 7 | Conclusions | sections/conclusions.tex | 4 thematic blocks, about 2 pages |
| 8 | References | references.bib (ieeetr style) | 25 entries |
| 9 | Back Matter | sections/back_matter.tex | 5 short sections |

## Reference inventory by category

| Category | Bibtex keys | Count |
|:---------|:------------|:------|
| This paper plus parent repositories | kawchak_2026_20113157, repo-robotic-surgeries, repo-physical-ai-oncology-trials | 3 |
| Author's prior glioblastoma and trial work | kawchak_2025_17774560, kawchak_2025_15549831, kawchak_2025_17614396, kawchak_2026_19994945 | 4 |
| Upstream 12-file instruction directory | one-minute-variant-instructions | 1 |
| FDA 28 April 2026 RTCT announcement | fda2026realtime | 1 |
| Glioblastoma clinical context | Stupp2005Glioblastoma, Sanai2011GBMResection, Stummer20055ALA | 3 |
| Robotic neurosurgery prior art | rosa-one-brain, Lefranc2014ROSAStereotaxy, Kalakoti2019RoboticsReview | 3 |
| IEC and FDA standards plus SaMD plus 21 CFR | iec-80601-2-77, iec-62304, cfr-21-50-30, fda-samd | 4 |
| Reporting standards (TRIPOD+AI, CREMLS) | Collins2024TRIPODAI, ElEmam2024CREMLS | 2 |
| AI / LLM tooling | claude-code, claude-opus-47, claude-sonnet-46, chatgpt-thinking, google-gemini-overview | 5 |
| Local LLM inference backends | ollama, vllm | 2 |
| Deterministic simulation + data formats | apache-arrow, duckdb, zenodo | 3 |
| Total | (sum of above) | 31 |

## Compile recipe

The LaTeX paper compiles cleanly on Overleaf (recommended) and on
any local `pdflatex` + `bibtex` installation. The expected sequence is:

```
pdflatex main.tex
bibtex   main
pdflatex main.tex
pdflatex main.tex
```

Do not compile the PDF as part of the template-population pass. The
PDF rendering is left to Overleaf or to the user's local install.

## LaTeX Source Files.zip recipe

The Overleaf-ready bundle is created on demand from the LaTeX sources
in this directory. The minimal recipe (Linux, MacOS) is:

```
cd 2030-gbm-1min/paper/full-paper
zip -r "LaTeX Source Files.zip" main.tex new_paper.sty references.bib sections/
```

On Windows PowerShell:

```
cd 2030-gbm-1min\paper\full-paper
Compress-Archive -Path main.tex,new_paper.sty,references.bib,sections -DestinationPath "LaTeX Source Files.zip"
```

The resulting zip uploads directly to Overleaf via **New Project ->
Upload Project**. The orcid_icon.png file is optional; new_paper.sty
falls back to a green "iD" tag if the PNG is missing.

## AVAILABLE DIRECTORIES (upstream and current)

The full paper is generated from three directories, all read-only
from the perspective of this PR.

**A. Instructions to generate code** (read-only context):

- Primary: `kevinkawchak/physical-ai-oncology-trials/tree/main/competitions/instructions/one_minute_variant/`. The 12 hand-authored files are: `README.md`, `commit_01_overview_1min.md`, `commit_02_sensors_1min.md`, `commit_03_xyz_4arm.md`, `commit_04_iterations_1min.md`, `commit_05_competition_1min.md`, `file_size_pyramid_1min.md`, `glioblastoma_context_1min.md`, `multi_arm_coordination.md`, `robot_specification_neurospeed.md`, `sensor_specification_10khz.md`, `zenodo_archive_protocol.md`.

**B. Code generation** (read-only context):

- Primary: `kevinkawchak/robotic-surgeries/tree/main/2030-gbm-1min/`. Notable subdirs: `docs/`, `config/`, `schemas/`, `src/{sensors,mapping,control,coordination,simulation,metrics,llm,zenodo}/`, `data/`, `prompts/`, `results/`, `viz/`, `notebooks/`, `logs/`, `releases/v3.9.1/`, and `paper/` (this directory's parent).

**C. Code execution** (read-only context):

- Primary: `kevinkawchak/robotic-surgeries/tree/main/2030-gbm-1min/outputs/`. Notable subdirs: `sensors/` (the 54 x 1001 `sensor_sample_4arm.csv` table), `xyz_mapping/`, `iterations/`, `metrics/`, `comparison/`, `comparison_robot_vs_human/`, `diagrams/`, `viz/`, `reports/`, `logs/`.

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

## Senior-author final-pass checklist

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

The repository CI matrix runs `ruff format --check`, `ruff check`, and
`yamllint -d relaxed` on Python 3.10, 3.11, and 3.12 against the
`2030-gbm-1min/` tree. The new files under
`2030-gbm-1min/paper/full-paper/` are LaTeX and Markdown only and are
not subject to those gates, so this PR does not regress the upstream
CI `Cl / lint-and-format` status. See `../../../.github/workflows/ci.yml`.

## License

The paper template inherits the repository MIT license for code
artifacts. The paper text itself is distributed under the Creative
Commons Attribution 4.0 International License (CC BY 4.0).
