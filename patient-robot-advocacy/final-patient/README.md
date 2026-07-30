# final-patient - Stage 8, the polished source set (v1.0.0)

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Stage](https://img.shields.io/badge/Stage-8%20of%208-00417A.svg)](../sub-prompts/prompt-8-final-patient.md)
[![Paper](https://img.shields.io/badge/Paper-Draft%201.0-00417A.svg)](main.tex)
[![Figures](https://img.shields.io/badge/Figures-30%2C%20in%20ascending%20order-00417A.svg)](sections)
[![Tables](https://img.shields.io/badge/Tables-43%2C%20all%20breakable-00417A.svg)](sections)
[![Pages](https://img.shields.io/badge/Pages-88-6C757D.svg)](main.tex)
[![Length](https://img.shields.io/badge/Length%20vs%20parent%20protocol-108%25-6C757D.svg)](#length-against-the-parent-protocol)
[![Compiles](https://img.shields.io/badge/pdfLaTeX-0%20errors%2C%200%20overfull-brightgreen.svg)](main.tex)
[![Overleaf](https://img.shields.io/badge/Overleaf-ready%20zip-6C757D.svg)](final-patient-LaTeX.zip)
[![Raster](https://img.shields.io/badge/Raster%20images-none-6C757D.svg)](.)
[![Release](https://img.shields.io/badge/Release-v1.0.0-orange.svg)](../../releases.md)

The last of the eight stages, run from
[`../sub-prompts/prompt-8-final-patient.md`](../sub-prompts/prompt-8-final-patient.md)
and filed here as [`prompt-final-patient.md`](prompt-final-patient.md). It is a senior
author's proof-reading pass over [`../full-patient/`](../full-patient), not a rewrite: no
figure loses a node, no section loses a paragraph, and every change is either a defect fix
or an addition.

There is **no `publication/` subdirectory** at this stage, as the master prompt requires.

## Files

| File | What it is |
|:--|:--|
| [`main.tex`](main.tex) | Cover page, keywords, three-page clickable contents, one `\input` per section with `\clearpage` between them |
| [`patientstyle.sty`](patientstyle.sty) | The style file, with the Stage 8 pagination machinery added |
| [`references.bib`](references.bib) | 51 entries, carried from Stage 7 byte for byte |
| [`sections/`](sections) | Thirteen `.tex` files, one per paper section |
| [`final-patient-LaTeX.zip`](final-patient-LaTeX.zip) | Overleaf-ready bundle, sources only |
| [`prompt-final-patient.md`](prompt-final-patient.md) | The Stage 8 sub-prompt, filed verbatim |
| [`output-final-patient.md`](output-final-patient.md) | The Stage 8 narrative: every defect found, and the fix |

## What Stage 8 changed

| | full-patient | final-patient |
|:--|:--|:--|
| Pages with a trailing gap over 3 cm | 41 of 83 | 16 of 88 |
| Worst trailing gap | 21.6 cm | 20.3 cm, all but five on a section's last page |
| Overfull boxes | 0 reported, 2 vertical | 0 |
| Content running past the foot of a page | 2 tables | none |
| Figure numbers in ascending order | no, two pairs inverted | yes, 1 to 30 |
| Unbreakable tables | 36 of 37 | 0 of 43 |
| Stranded headings | 2 | 0 |
| Contents | 4 pages, the fourth nearly empty | 3 pages |
| Visible text characters | 129,078 | 168,275 |
| Length against the parent protocol | 83 percent | 108 percent |

## The five defects Stage 7 left, and the fix for each

**1. Figures stranded whole pages.** Every figure was set inline, so a figure taller than
the space left on the page forced a break and left that space empty. Forty-one of
eighty-three pages carried a trailing gap over 3 cm, the worst 21.6 cm.

*Fix.* Each figure-plus-caption is wrapped in a `pafloat`, a `figure` float placed `!tb`.
Running text now closes the page and the figure heads the next one. Float parameters are
set so a float page is built only when the floats would fill 94 percent of it, and
`main.tex` still clears the page between sections, so no figure leaves the section that
discusses it. The spacing invariant is untouched: `pafig` drops its leading 14 pt and
`\figcaption` its trailing 13 pt inside a float, but the rigid `\vskip 26pt` that pairs
with `\vspace{-0.7cm}` is kept, so the frame-to-caption distance is **6.1 pt for all
thirty figures**, floating or inline.

**2. Two tables ran off the foot of a page.** A `tabularx` is one unbreakable box. Where a
heading was immediately followed by one, `\@nobreak` prevented the break and the page
overfilled instead, by 143 pt in the worst case, printing a table row past the bottom
margin.

*Fix.* Every table of more than two rows is now an `xltabular` with `\endfirsthead`,
`\endhead`, `\endfoot`, and `\endlastfoot`, so it fills the page it starts on and continues
overleaf under a repeated header with a continuation line. Forty-three of forty-three
tables are breakable, and the count of unbreakable boxes in the document is zero.

**3. Two headings were the last thing on their page.** `\@afterheading` stops a break
directly after a heading, but when the heading itself lands on the last line the page
overfills instead.

*Fix.* `\subsection` reserves itself plus three lines and `\subsubsection` plus two, so the
heading and the start of its text move together.

**4. Two pairs of figures were out of order.** The operative-envelope figure was numbered
21 but appeared before the fault tree numbered 20, and the calendar was numbered 25 but
appeared before the data pipeline numbered 24.

*Fix.* 20 exchanged with 21 and 24 with 25, applied to the captions, to every prose and
table cross-reference, to the figure inventory in § 13.2, and to the four diagram source
files, which were renamed so each still carries the number of the figure it draws. The
per-type counts are unchanged, because each swap exchanges one figure each way.

**5. The paper was 17 percent short of the parent protocol.** Measured like for like, with
markup and diagram sources stripped from both, Stage 7 carried 129,078 visible characters
against the protocol's 155,222.

*Fix.* Fifteen subsections were added across the thirteen sections, none of them padding
and each answering a question the surveyed literature records participants asking. The
paper now carries 168,275 characters, which is 108 percent of the protocol.

## Length against the parent protocol

| | Parent protocol | This paper |
|:--|:--|:--|
| Visible text characters, markup and diagrams stripped | 155,222 | 168,275 |
| Sections | 13 | 13 |
| Figures | 20 | 30 |
| Tables | 11 | 43 |
| Pages | 55 | 88 |

The comparison strips comments, `tikzpicture` and `pafig` blocks, and LaTeX control
sequences from both documents, so it measures what a reader reads rather than how the two
macro styles differ.

## The author's formatting methods, applied

| Method | Where it is used here |
|:--|:--|
| `\clearpage` | Between all thirteen sections, from `main.tex`, so no section opens at the foot of the previous section's last page |
| `\needspace` | Before every `\subsection` and `\subsubsection`, and inside `pafig` when a figure is set inline rather than floated |
| Table column widths | Fixed `L{...}`, `C{...}`, `R{...}` measured against the longest cell actually present, including the bold header; one `Y` column absorbs the remainder; `\tabcolsep` 5 pt, `\arraystretch` 1.18; every table lands exactly on `\textwidth` |
| `\vspace` | `-0.7cm` between every figure and its caption, identical for all thirty; `0.30em` above and below a full-width table |
| `\hspace` | Only inside table cells and header lines, never to fake indentation in body text |
| `\raggedbottom` with `\RaggedRight` | `\RaggedRightRightskip` `0pt plus 2em`, so interword spacing is even and no line runs past the right margin |
| Widow, orphan, and broken penalties | All at 10000, with `\finalhyphendemerits` 10000 and a stretchable `\parfillskip`, so no line is stranded and no paragraph ends in one or two words |

## Verification, every item checked

| # | Check | Result |
|:--|:--|:--|
| 1 | Thirty figures, ascending, 1 to 30, no gaps or duplicates | pass, read from document order |
| 2 | Every caption at most three lines, balanced | pass, 30 of 30 in band, spread at most 12 |
| 3 | Exactly `\vspace{-0.7cm}` before every caption | 30 of 30 |
| 4 | No box overlap, no arrow through a box, no label on a line | pass, third independent pass |
| 5 | Every curved connector declares a looseness | 122 of 122 |
| 6 | Every table at `\textwidth`, every fixed column ragged-right | 43 of 43, 0 raw `p{}` columns |
| 7 | Every `\cite` resolves, every DOI and URL clickable | 0 undefined citations, 0 bibtex warnings |
| 8 | No link past the right margin | 0 overfull boxes anywhere |
| 9 | No em dash, en dash, or triple dash in text | 0 |
| 10 | `§` and not `SS` for every codified reference | 0 occurrences of `SS` in text |
| 11 | Palette compliance | 10 tokens used in the sections, no eleventh |
| 12 | Clean compile | 0 errors, 0 overfull, 88 pages |
| 13 | No raster images | 0 `\includegraphics`, 0 PNG, 0 JPG |

## Files from other directories used here

| Source | Used for | Where |
|:--|:--|:--|
| [`../full-patient/`](../full-patient) | the entire content: sources, figures, tables, bibliography | every file |
| [`../mermaid/`](../mermaid) | 9 figure sources | figures 1, 3, 7, 10, 14, 19, 23, 24, 27 |
| [`../plantuml/`](../plantuml) | 5 figure sources | figures 8, 12, 15, 18, 22 |
| [`../d2/`](../d2) | 7 figure sources | figures 4, 5, 11, 16, 20, 26, 29 |
| [`../diagrams-python/`](../diagrams-python) | 4 figure sources | figures 9, 17, 25, 30 |
| [`../graphviz/`](../graphviz) | 5 figure sources | figures 2, 6, 13, 21, 28 |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) | every clinical fact, limit, endpoint, and oversight body, and the length target | all thirteen sections |
| [`../inputs/patient-priority-physical-ai.zip`](../inputs) | the patient-as-priority premise and the bill framing | § 1, § 6, § 12 |
| [`../inputs/cancer-patient-journey.zip`](../inputs) | the journey and stack topology, NSCLC, distinguished from PDAC | § 2, § 7, figures 3, 17, 25 |
| [`../inputs/patient-robot-instructions.tex`](../inputs) | the ten instruction sheets, re-scoped to PDAC | § 9.5, § 9.7, figure 26 |
| [`../research/research-a.md`](../research) | the six Gemini concern families | § 3 |
| [`../research/research-b.md`](../research) | the sixteen ChatGPT concerns and their references | § 3, bibliography |
| [`../references/references.bib`](../references) | the author works and the H. R. 9510 v5 citation | § 6, § 12 |
| [`../template/trial-protocol-template.zip`](../template) | the directory layout this stage sits in | this directory |

## Compiling

```
pdflatex main -> bibtex main -> pdflatex main -> pdflatex main
```

Verified on TeX Live 2023: **88 pages, 0 errors, 0 overfull boxes, 0 undefined citations,
0 undefined references**. [`final-patient-LaTeX.zip`](final-patient-LaTeX.zip) contains
`main.tex`, `patientstyle.sty`, `references.bib`, and `sections/`, with no auxiliary files,
and uploads to Overleaf unmodified.

## License

Released under CC BY 4.0; reproduced U.S. Government regulatory text is used under
17 U.S.C. § 105. Author: Kevin Kawchak, CEO ChemicalQDevice
([ORCID 0009-0007-5457-8667](https://orcid.org/0009-0007-5457-8667)).
