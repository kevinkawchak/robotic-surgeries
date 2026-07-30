## output-draft-patient

Stage 6 narrative, run from
[`prompt-draft-patient.md`](prompt-draft-patient.md), which is
[`../sub-prompts/prompt-6-draft-patient.md`](../sub-prompts/prompt-6-draft-patient.md)
filed verbatim.

### What was produced

A complete, compilable LaTeX scaffold of the paper: `main.tex` with the patient-advocacy
cover page, `patientstyle.sty` carrying all five diagram vocabularies, `references.bib`
merging three bibliographies into one format, thirteen `sections/*.tex` files, a stage
README, and an Overleaf-ready zip. Twenty commits, one per distinguishable file, pushed on
write.

### Compile result

```
pdflatex main -> bibtex main -> pdflatex main -> pdflatex main
Output written on main.pdf (42 pages, 274224 bytes).
0 errors   0 overfull boxes   0 undefined citations   0 undefined references
```

### Decisions made during the stage

1. **The cover page is redesigned, not recoloured.** The master prompt asks for visual
   changes that suit an advocacy paper, especially on the cover, while keeping the colour
   scheme. Four changes: a full-width Corporate Blue banner replaces the centred title
   block; four rounded badges replace the version line; a three-panel strip answers the
   three questions the surveyed literature says patients actually ask, before any
   regulatory text; and the independence statement and the disclaimer are separated so
   each is readable. Every colour used is one of the eleven tokens.

2. **Thirteen sections, one `.tex` each.** Rule 6 requires one section file per `main.tex`
   entry. The thirteen follow the parent protocol's NIH-FDA order but are renamed to the
   question each answers for the participant: Statement of Compliance becomes Statement of
   Patient Commitment, Study Intervention becomes What Happens in the Operating Room, and
   Regulatory Oversight becomes Accountability, Oversight, and Who Answers.

3. **Every bracketed instruction names a file.** There are 78 `\draftinstr{...}` markers
   and not one of them says "expand this". Each names the repository file supplying the
   material, down to the section inside the parent protocol's zip, so Stage 7 has no
   discretion about provenance.

4. **The figure slots are real, not placeholders.** All thirty are live `pafig`
   environments containing a titled node and the source-file label, so the scaffold
   paginates realistically at 42 pages and the `\vspace{-0.7cm}` invariant is exercised
   from this stage forward rather than introduced later.

5. **Tables are final in structure at the draft stage.** Every table already carries its
   final column specification with `>{\raggedright\arraybackslash}p{...}` on every fixed
   column and one `Y` absorbing the remainder. Stage 7 fills cells; it does not
   re-architect tables.

6. **The unfavourable content is written into the scaffold, not deferred.** The
   instructions for \S2.6 (what the study cannot tell you), \S8.1 routes C and D (data that
   cannot be recalled), \S10.5 (the honest denominator), and \S12.3 (the two unsettled
   costs) all say explicitly that the passage must not be softened or trimmed. Putting
   that in the scaffold makes it harder to lose in a later pass.

### Errors found and fixed in the second-to-last commit

The first full compile produced nine overfull horizontal boxes and no errors. All nine were
traced, and all nine were fixed rather than tolerated.

| # | Location | Cause | Fix |
|:--|:--|:--|:--|
| 1 | `main.tex` banner | The tikz node's stroke width pushed the bounding box past the measure | Inner text width reduced by 4pt and the subtitle rebalanced across its two lines |
| 2 | `main.tex` three-panel strip | Three panels at 0.295 plus two gaps at 0.014 exceeded the measure once strokes were counted | Panels reduced to 0.288 and gaps to 0.013 |
| 3 to 7 | Five figure-slot source labels | A path such as `diagrams-python/fig_09_concern_locations.py` has no break point and cannot fit a 24 mm TikZ label | Every source label normalised to a breakable two-line monospace form using the new `\pfb` zero-width break |
| 8 | `sec-11-rights.tex` and `sec-12-references-backmatter.tex` prose | Long `\texttt{...}` repository paths in running text | 50 distinct paths given explicit `\pfb` break points throughout all thirteen sections |
| 9 | `sec-02-concerns.tex` and `sec-03-objectives.tex` tables | The `C` column was measured against the body cells, not the bold header cells "Concerns" and "Timepoint" | Both `C` columns re-measured against their longest actual cell and widened, with the neighbouring `L` column narrowed to keep the sum on the measure |

One non-compile defect was also fixed: the `gvcircleg` style key in `patientstyle.sty`
contained a non-ASCII character, which would have silently failed to match had the style
been used.

### Verification performed

| Check | Result |
|:--|:--|
| Thirty `pafig` environments | pass |
| Thirty `\vspace{-0.7cm}` lines, one per figure | pass |
| Thirty `\figcaption` calls, numbered 1 to 30, no gaps, no duplicates | pass |
| Every caption at most three lines, manually broken | pass |
| Every fixed-width table column uses `>{\raggedright\arraybackslash}p{...}` | pass |
| Every table is a `tabularx` at `\textwidth` | pass, 14 tables |
| Every `\draftinstr` names a repository file | pass, 78 of 78 |
| No em dash, en dash pair, or triple dash | pass |
| Every codified reference uses `§` | pass |
| No PNG, no JPG, no `\includegraphics` | pass |
| Compiles clean through the four-pass sequence | pass, 42 pages |

### Commits in this stage

| # | Commit | File |
|:--|:--|:--|
| 1 | `patientstyle.sty` with the five diagram vocabularies | `patientstyle.sty` |
| 2 | `references.bib` merging three bibliographies | `references.bib` |
| 3 | `main.tex` with the patient-advocacy cover page | `main.tex` |
| 4 to 16 | Thirteen section scaffolds, one commit each | `sections/*.tex` |
| 17 | Stage README and the sub-prompt filed verbatim | `README.md`, `prompt-draft-patient.md` |
| 18 | Fix all errors across all files | 15 files |
| 19 | Overleaf zip and this narrative | `draft-patient-LaTeX.zip`, `output-draft-patient.md` |

### Handoff to Stage 7

[`../full-patient/`](../full-patient) executes every one of the 78 bracketed instructions,
draws all thirty figures completely in TikZ from the five diagram-source directories, and
fills every table. The target body length is approximately that of the parent protocol,
about 170,000 characters across the thirteen sections. Nothing may remain bracketed, and
no figure may keep a placeholder node.
