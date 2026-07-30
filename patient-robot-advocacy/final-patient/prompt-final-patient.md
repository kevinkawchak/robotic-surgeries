## prompt-final-patient

**Stage 8 of 8.** Output directory: [`../final-patient/`](../final-patient). Produces the
polished, publication-quality source. There is no `publication/` subdirectory at this
stage.

### Objective

Take `../full-patient/` to maximum quality. This stage is a senior author's proof-reading
pass, not a rewrite: every correction identified while building Stage 7 is implemented, and
every figure, table, and page is re-examined until it is self-standing.

### Corrections carried forward from `full-patient`

The stage begins by listing, in `output-final-patient.md`, every defect found in Stage 7 -
figure overlaps, captions outside the line-length band, tables short of `\textwidth`,
stranded lines, overfull boxes, and sections that end with a single orphaned line - and
then fixes each one. The list and the fix are both recorded.

### Author formatting methods to learn and apply

1. **`\clearpage`.** Each major section starts on a fresh page from `main.tex`, so no
   section's opening paragraph is stranded at the foot of the previous section's last page.
2. **Table column widths.** Re-measure every table against its longest actual cell.
   Fixed columns are `>{\raggedright\arraybackslash}p{...}`; one `Y` column absorbs the
   remainder; the sum lands exactly on `\textwidth`; `\tabcolsep` 5pt; `\arraystretch` 1.18.
   A table that would break across a page either gets `\needspace` above it or is
   converted to `xltabular` with a repeated header.
3. **`\vspace` and `\hspace`.** `\vspace{-0.7cm}` between every figure and its caption,
   identical for all thirty. `\vspace{0.3em}` above and below a full-width table.
   `\vspace{0.6em}` before a signature block. `\hspace` only inside a table cell or a
   header line, never to fake indentation in body text.
4. **`\raggedbottom` plus `\RaggedRight`** with `\RaggedRightRightskip=0pt plus 2em`, so
   interword spacing is even and no line runs past the right margin.
5. **Widow, orphan, and broken penalties at 10000**, so no single line is stranded on the
   next page and no paragraph ends with a one-word or two-word line.

### Verification checklist (every item is checked, and the result recorded)

| # | Check | Method |
|:--|:--|:--|
| 1 | Thirty figures, numbered 1 to 30, no gaps and no duplicates | grep the `\figcaption` lines in order |
| 2 | Every caption is at most three lines with balanced character counts | count characters per `\\`-separated line |
| 3 | Every figure has exactly `\vspace{-0.7cm}` before its caption | grep pairs; count must equal 30 |
| 4 | No figure has a box overlap, an arrow through a box, or a label on a line | re-derive bounding boxes; second independent pass |
| 5 | Every curved connector declares an explicit looseness | grep `to[out=` and require `looseness=` |
| 6 | Every table equals `\textwidth` and every fixed column is ragged-right | sum the widths plus `\tabcolsep`; grep the column specs |
| 7 | Every `\cite` key resolves and every URL and DOI is clickable | bibtex log has no warnings; visual check of the reference list |
| 8 | No link runs past the right margin | zero overfull boxes in the bibliography |
| 9 | No em dash, en dash pair, or triple dash anywhere | grep for the characters and for `--` and `---` |
| 10 | Every codified reference uses `§`, not `SS` or `Section` | grep |
| 11 | Palette compliance in every figure | grep each figure for colour tokens outside the permitted set |
| 12 | Compiles clean with `pdflatex -> bibtex -> pdflatex -> pdflatex` | zero errors, zero overfull boxes above 5pt |

### Rules for this stage

1. Commits: `main.tex`, `patientstyle.sty`, `references.bib`, `README.md`, and one per
   section file; the second-to-last commit fixes all errors across all files; the last
   commit lands `final-patient-LaTeX.zip`, `output-final-patient.md`, and then the
   remaining repository updates - root `README.md` (two new sections only), `CHANGELOG.md`
   (v1.0.0), `releases.md` (v1.0.0), and `../prompts/output-patient.md`.
2. No `publication/` subdirectory under `final-patient/`.
3. No PNG, no JPG. Single dashes only. Nothing in this stage may reduce the completeness
   of any figure or section relative to `full-patient`.
