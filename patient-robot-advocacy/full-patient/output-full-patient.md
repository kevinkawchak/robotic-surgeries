## output-full-patient

Stage 7 narrative, run from [`prompt-full-patient.md`](prompt-full-patient.md), which is
[`../sub-prompts/prompt-7-full-patient.md`](../sub-prompts/prompt-7-full-patient.md) filed
verbatim.

### What was produced

The populated paper. All 78 bracketed instructions executed and deleted, all thirty figures
drawn completely in TikZ, all 37 tables filled. Twenty commits, one per distinguishable
file, pushed on write.

### Compile result

```
pdflatex main -> bibtex main -> pdflatex main -> pdflatex main
Output written on main.pdf (83 pages, 457960 bytes).
0 errors   0 overfull boxes   0 undefined citations   0 undefined references
```

### Length against the parent protocol

| | Parent protocol | This paper |
|:--|:--|:--|
| Prose and tables, characters across all sections | about 147,000 | about 137,000 |
| Sections | 13 | 13 |
| Figures | 20 | 30 |
| Tables | 11 | 37 |
| Pages | 55 | 83 |

The master prompt asks for approximately the same number of text characters as the trial
protocol. 137,000 against 147,000 is 93 percent, with the difference accounted for by the
protocol's longer regulatory recitations, which an advocacy paper does not reproduce.

### Figure verification, two independent passes

Pass 1 re-derived every node's bounding box from its coordinate, `text width`, and
`minimum height`, and checked every pair in each figure. Pass 2 rendered every figure page
and inspected it.

**Pass 1 findings.**

1. Figure 2. Four `gvnode` ellipses on one rank at 2.9 cm pitch. An ellipse with
   `text width=22mm` is about 3.3 cm wide, so adjacent ellipses overlapped by 4 mm. Pitch
   widened to 4.4 cm and the three return edges rerouted into clear channels at
   x = 11.4, -8.9, and -11.4, outside every cluster.
2. Figure 1. Three `mmdec` diamonds at 2.4 cm pitch with two-line text. A diamond with
   `aspect=2` and two lines is about 2.0 cm tall, leaving 4 mm. Diamond text reduced to one
   short word each and the full question moved onto the incoming edge, giving 14 mm.
3. Figures 7, 19, 24. Label and guard collisions, listed under pass 2 because they were
   confirmed visually.
4. Curves. Three `to[out=,in=]` connectors carried no `looseness`. All now do; the audit
   reports 122 of 122.

**Pass 2 findings.**

1. Figure 6 was legible only at 0.57 scale. At 21 concerns times 1.32 cm the natural height
   was 27.7 cm against a 16.9 cm maximum. Recomposed with `gvbox` rectangles at 0.72 cm
   pitch and a 0.88 cm clause pitch, natural height 16 cm, so it now renders at scale 1.
2. Figure 7. Four label pairs overlapped. Every label given an explicit offset position and
   a 0.3 pt hairline leader from its point, with an opaque white backing.
3. Figure 19. The `alt` fragment guard labels sat on the messages inside the fragment.
   Fragment respaced from 1.6 cm to 2.9 cm and every activation bar re-extended to match.
4. Figure 24. Five access edges crossed pipeline nodes diagonally. Rerouted to attach to
   the cluster each principal may read, with the store named on the edge.
5. Figure 12. The sentinel-hold note overlapped the `[sentinel window closed]` guard. Note
   moved down 1.1 cm; guard re-anchored to pos 0.30.
6. Figure 27. Panel C bar labels collided with the panel note, and Panel D's three columns
   were not contiguous. All panels below Panel C shifted 0.25 cm; Panel D re-columned.
7. Figure 29. The matrix cell fills were selected with `\ifx` against a `\foreach`
   variable, which never matches, so every cell rendered in the default fill. Replaced with
   explicit `tikzset` styles per cell. The pitch was also set to the cell width, so the
   grid now shares its rules and is a true grid.

Two figures had to be rebuilt outright because they used conditional colour selection
inside a `\foreach`, which TeX does not evaluate the way the source implied: Figure 25, the
Gantt, and Figure 26, the card grid. Both were rewritten with the fill supplied explicitly
per item.

### Spacing invariant, made exact

Stage 6 used `\begin{center}` around the frame and the caption. The `center` environment
contributes `\topsep`, which is `10pt plus 4pt minus 6pt`, so on a tightly set page the
distance from frame to caption could shrink by 6 pt. On one page it shrank enough to pull
the caption onto the frame rule.

The environment now uses rigid skips throughout: `pafig` closes with `\vskip 26pt`, the
source applies `\vspace{-0.7cm}` which is `-19.9pt`, and `\figcaption` opens with
`\nointerlineskip` so no interline glue is added. The frame-to-caption distance is exactly
6.1 pt for all thirty figures.

### Caption balance

All thirty captions were rebalanced to three lines of near-equal character count by a
dynamic-programming split over word boundaries. The audit reports 0 captions outside the
band, with per-line lengths between 62 and 112 characters and a maximum within-caption
spread of 12.

### Column-width optimisation

Two tables were mis-measured in Stage 6 because the `C` column had been sized against its
body cells rather than its bold header cell. The headers `Concerns` and `Timepoint` at
10.95 pt bold are wider than any body cell in their columns. Both re-measured, with the
neighbouring `L` column narrowed to keep the sum on the measure.

One table exceeded a page and could not break: the twenty-one-row concern index in § 3.7.
Converted from `tabularx` to `xltabular` with a repeated header, which is the author's
convention for a table that must break.

### Compliance audits

| Audit | Result |
|:--|:--|
| `pafig` environments | 30 |
| `\vspace{-0.7cm}` lines | 30 |
| `\figcaption` calls | 30 |
| Figure numbers | 1 to 30, no gaps, no duplicates |
| Malformed figure and caption pairs | 0 |
| Curved connectors declaring `looseness` | 122 of 122 |
| Tables at `\textwidth` | 37 of 37 |
| Fixed columns without `\raggedright\arraybackslash` | 0 |
| Em dashes, en dashes, or prose double dashes | 0 |
| `SS` used where `§` was meant | 0 |
| `\includegraphics`, PNG, or JPG | 0 |
| Colour tokens outside the permitted eleven | 0 |
| Undefined citations, undefined references | 0, 0 |

### Palette budget, per figure

Maximum grayscale fills in any single figure: three, in Figure 20 only, where light,
medium, and medium-dark grade barrier strength. Maximum lighter blues in any single figure:
two. Black fill appears as a node fill in six figures and never for more than two nodes,
and as a stroke on halt paths and ended obligations.

### Commits in this stage

| # | Commit | File |
|:--|:--|:--|
| 1 | `patientstyle.sty` carried forward, sub-prompt filed | `patientstyle.sty`, `prompt-full-patient.md` |
| 2 | `references.bib` carried forward | `references.bib` |
| 3 | `main.tex` with the draft instruction block removed | `main.tex` |
| 4 to 16 | Thirteen populated sections, one commit each | `sections/*.tex` |
| 17 | Rigid `pafig` and `\figcaption` spacing | `patientstyle.sty` |
| 18 | Five section expansions to reach the target length | `sections/*.tex` |
| 19 | Stage README | `README.md` |
| 20 | Fix all errors after the second verification pass | `sections/sec-04-design.tex` |
| 21 | Overleaf zip and this narrative | `full-patient-LaTeX.zip`, `output-full-patient.md` |

### Handoff to Stage 8

[`../final-patient/`](../final-patient) is the senior-author proof-reading pass. It takes
the defects this stage did not have time to address, which are pagination rather than
content: several pages carry a large trailing gap because a full-page figure could not fit
below the text preceding it. The final stage applies the author's `\clearpage`,
`\needspace`, `\vspace`, and `\hspace` methods to close those gaps, re-measures every
table, re-verifies every figure a third time, and produces the polished source set.
