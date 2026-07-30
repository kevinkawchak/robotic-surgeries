# full-patient - Stage 7, the populated paper with all thirty figures (v1.0.0)

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Stage](https://img.shields.io/badge/Stage-7%20of%208-00417A.svg)](../sub-prompts/prompt-7-full-patient.md)
[![Paper](https://img.shields.io/badge/Paper-Draft%201.0-00417A.svg)](main.tex)
[![Figures drawn](https://img.shields.io/badge/Figures%20drawn-30%20of%2030-00417A.svg)](sections)
[![Tables](https://img.shields.io/badge/Tables-37-00417A.svg)](sections)
[![Pages](https://img.shields.io/badge/Pages-83-6C757D.svg)](main.tex)
[![Compiles](https://img.shields.io/badge/pdfLaTeX-0%20errors%2C%200%20overfull-brightgreen.svg)](main.tex)
[![Overleaf](https://img.shields.io/badge/Overleaf-ready%20zip-6C757D.svg)](full-patient-LaTeX.zip)
[![Raster](https://img.shields.io/badge/Raster%20images-none-6C757D.svg)](.)
[![Release](https://img.shields.io/badge/Release-v1.0.0-orange.svg)](../../releases.md)

Stage 7 of the eight-stage build, run from
[`../sub-prompts/prompt-7-full-patient.md`](../sub-prompts/prompt-7-full-patient.md).
Every one of the 78 `\draftinstr{...}` bracketed instructions left by
[`../draft-patient/`](../draft-patient) has been executed and deleted, all thirty figures
are drawn completely in TikZ from the five diagram-source directories, and every table is
filled from the author's quantitative sources.

## Files

| File | What it is |
|:--|:--|
| [`main.tex`](main.tex) | Cover page, keywords, clickable table of contents, one `\input` per section, `\clearpage` between sections |
| [`patientstyle.sty`](patientstyle.sty) | Carried from Stage 6, with the `pafig` and `\figcaption` spacing made rigid |
| [`references.bib`](references.bib) | 51 entries in one format; every DOI printed as text and hyperlinked |
| [`sections/`](sections) | Thirteen `.tex` files, one per paper section |
| [`full-patient-LaTeX.zip`](full-patient-LaTeX.zip) | Overleaf-ready bundle |
| [`prompt-full-patient.md`](prompt-full-patient.md) | The Stage 7 sub-prompt, filed verbatim |
| [`output-full-patient.md`](output-full-patient.md) | The Stage 7 narrative and both figure-verification passes |

## What changed from `draft-patient`

| | draft-patient | full-patient |
|:--|:--|:--|
| Bracketed instructions | 78 | 0 |
| Figures drawn in full | 0 of 30 (slots only) | 30 of 30 |
| Prose and tables, characters | about 46,000 | about 137,000 |
| Tables filled | column specs only | 37 tables, every cell filled |
| Pages | 41 | 83 |
| Figure spacing | `\addvspace`, shrinkable | rigid `\vskip`, identical for all 30 |
| Captions | 2 unbalanced lines | 3 balanced lines, all 30 inside the band |

The parent protocol carries about 147,000 characters of prose and tables across its
thirteen sections. This paper carries about 137,000, which is the "approximately the same
number of text characters" the master prompt asks for.

## Column-width optimisation, using the author's method

Every table follows the method used in
[`../inputs/phase-1-trial-protocol.zip`](../inputs): fixed `L{...}` widths for label
columns whose longest cell is known, `C{...}` for short categorical columns, and one `Y`
flexible column absorbing the remainder so the table lands exactly on `\textwidth`. Widths
are set from the longest cell **actually present**, including the bold header cell, which
is where two tables in Stage 6 were mis-measured. `\tabcolsep` stays at 5pt and
`\arraystretch` at 1.18.

One table, the twenty-one-concern index in § 3.7, exceeds a page and is therefore an
`xltabular` with a repeated header rather than a `tabularx`, which is the author's
convention for a table that must break.

## The spacing invariant, now exact

`pafig` closes with a rigid `\vskip 26pt`; the source then applies `\vspace{-0.7cm}`, which
is `-19.9pt`; `\figcaption` opens with `\nointerlineskip`, so no interline glue is added,
and closes with a rigid `\vskip 13pt`. The distance from the frame rule to the first
caption line is therefore exactly **6.1pt for every one of the thirty figures**, whatever
precedes or follows them on the page. Stage 6 used `\begin{center}`, whose shrinkable
`\topsep` glue made the distance vary by up to 6pt and, on one page, pulled a caption onto
the frame rule.

## Figure verification, performed twice

The sub-prompt requires two independent passes over all thirty figures. Both were run and
both are recorded in [`output-full-patient.md`](output-full-patient.md).

| Check | Pass 1 finding | Pass 2 finding | Resolution |
|:--|:--|:--|:--|
| a) No box, arrow, or label overlap | Figure 2 ellipse row overlapped at 2.9 cm pitch; Figure 7 labels collided in four places; Figure 19 `alt` guards sat on messages; Figure 24 access edges crossed pipeline nodes | Figure 6 legible only at 0.57 scale | Pitch widened to 4.4 cm; labels given explicit offsets with hairline leaders; `alt` fragment respaced; access edges rerouted to cluster borders; Figure 6 recomposed to fit at scale 1 |
| b) Curved connectors declare looseness | 3 curves without an explicit looseness | 0 remaining | Every `to[out=,in=]` now carries `looseness=` |
| c) Clear space between boxes | Figure 1 diamonds at 2.4 cm pitch were 4 mm apart | none | Diamond text reduced to one short word, giving 14 mm |
| Grid figures share their rules | Figure 29 had 2.5 mm inter-cell gaps | none | Pitch set to cell width so the grid is a true grid |

## Palette compliance

Eleven colour tokens exist and no figure uses a twelfth. Per figure the budget is at most
three grayscale fills, at most two lighter blues, and black fill sparingly. The audit is in
the stage narrative; the maximum grayscale use in the paper is three, in Figure 20 only,
where the three grades mark barrier strength.

## Files from other directories used here

| Source | Used for | Where |
|:--|:--|:--|
| [`../draft-patient/`](../draft-patient) | the scaffold, the cover page, the section order, the 78 instructions | every file |
| [`../mermaid/`](../mermaid) | 9 figure sources and their TikZ rendering notes | figures 1, 3, 7, 10, 14, 19, 23, 25, 27 |
| [`../plantuml/`](../plantuml) | 5 figure sources | figures 8, 12, 15, 18, 22 |
| [`../d2/`](../d2) | 7 figure sources | figures 4, 5, 11, 16, 21, 26, 29 |
| [`../diagrams-python/`](../diagrams-python) | 4 figure sources | figures 9, 17, 24, 30 |
| [`../graphviz/`](../graphviz) | 5 figure sources | figures 2, 6, 13, 20, 28 |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) | every clinical fact, limit, endpoint, and oversight body | all thirteen sections |
| [`../inputs/patient-priority-physical-ai.zip`](../inputs) | the patient-as-priority premise and the bill framing | § 1, § 6, § 12 |
| [`../inputs/cancer-patient-journey.zip`](../inputs) | the journey and stack topology, NSCLC, distinguished from PDAC in § 2.3 and § 7.1 | § 2, § 7, figures 3, 17, 24 |
| [`../inputs/patient-robot-instructions.tex`](../inputs) | the ten instruction sheets, re-scoped to PDAC and stripped of raster images | § 9.6, § 9.7, figure 26 |
| [`../research/research-a.md`](../research) | the six Gemini concern families | § 3 |
| [`../research/research-b.md`](../research) | the sixteen ChatGPT concerns, the ten consent items, the thirteen references | § 3, § 6.5, bibliography |
| [`../references/references.bib`](../references) | the author works and the H. R. 9510 v5 citation | § 6, § 12 |

## Compiling

```
pdflatex main -> bibtex main -> pdflatex main -> pdflatex main
```

Verified locally on TeX Live 2023: 83 pages, 0 errors, 0 overfull boxes, 0 undefined
citations, 0 undefined references.

## License

Released under CC BY 4.0; reproduced U.S. Government regulatory text is used under
17 U.S.C. § 105. Author: Kevin Kawchak, CEO ChemicalQDevice
([ORCID 0009-0007-5457-8667](https://orcid.org/0009-0007-5457-8667)).
