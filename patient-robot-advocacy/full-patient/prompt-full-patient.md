## prompt-7-full-patient

**Stage 7 of 8.** Output directory: [`../full-patient/`](../full-patient). Produces the
fully populated LaTeX paper with all thirty figures drawn.

### Objective

Execute every `\draftinstr{...}` left by Stage 6. The bracketed instruction is deleted and
replaced by the prose, table, or figure it called for, drawn from the exact repository file
it named. Nothing is invented where a source exists; nothing is left bracketed.

### What changes from `draft-patient`

1. **Prose.** Each of the thirteen sections is written out in full. The paper targets
   approximately the same body-character count as
   `../inputs/phase-1-trial-protocol.zip` (about 170,000 characters across its sections),
   distributed across the thirteen sections in proportion to how much the patient needs
   from each.
2. **Figures.** All thirty `pafig` environments are drawn completely in TikZ from the
   sources in `../mermaid/`, `../plantuml/`, `../d2/`, `../diagrams-python/`, and
   `../graphviz/`. Each figure is comprehensive: no placeholder nodes, no
   "detail omitted", and the same level of completeness from Figure 1 to Figure 30.
3. **Tables.** Every table is filled with quantitative data from the author's sources and
   is exactly `\textwidth` wide.

### Column-width optimisation (author method, inherited)

Follow the method used in `../inputs/phase-1-trial-protocol.zip`: fixed `L{...}` widths for
label columns whose longest cell is known, `C{...}` for short categorical columns, and one
`Y` flexible column absorbing the remainder so the table lands exactly on `\textwidth`.
Set the widths from the longest cell actually present, not from a guess, and keep
`\tabcolsep` at 5pt and `\arraystretch` at 1.18. Every fixed-width column is declared
`>{\raggedright\arraybackslash}p{...}`.

### Figure verification (perform twice, independently)

For every one of the thirty figures, confirm:

- **a) No overlap.** No text box overlaps another text box; no arrow passes through a text
  box; no edge label sits on top of an edge or a node. Re-derive each node's bounding box
  from its coordinate, `text width`, and `minimum height`, and check every pair.
- **b) Curve looseness.** Every curved connector declares an explicit looseness. Use
  `to[out=,in=,looseness=0.8]` for a short detour, `looseness=1.1` for a wide sweep, and
  never leave the default on a curve longer than 3 cm.
- **c) Box spacing.** At least 6 mm of clear space between adjacent node edges on the same
  rank, and at least 9 mm between ranks, so no two boxes appear to touch.

Record the result of both passes in `output-full-patient.md`.

### Spacing invariant (Rule c of the master prompt)

Every figure, without exception, is followed by exactly:

```
\end{pafig}
\vspace{-0.7cm}
\figcaption{Figure NN. ...}
```

The `pafig` environment supplies a fixed `\addvspace` before the frame and `\figcaption`
supplies a fixed `\addvspace` after the caption, so the whitespace signature is identical
for all thirty figures regardless of what follows them.

### Caption invariant (Rule b of the master prompt)

Each caption is at most three lines, broken manually with `\\`, and the lines have similar
character counts (target 95 to 105 characters per line, maximum spread 12 characters
between the longest and shortest line of the same caption).

### Rules for this stage

1. Commits: `main.tex`, `patientstyle.sty`, `references.bib`, `README.md`, and one per
   section file; second-to-last commit fixes all errors; last commit lands
   `full-patient-LaTeX.zip` and `output-full-patient.md`. 20 commits.
2. Single dashes only. `§` for codified references. Clickable URLs and DOIs; no link may
   run past the right margin. No line may be left with one or two words. No PNG, no JPG.
3. The stage must compile with `pdflatex -> bibtex -> pdflatex -> pdflatex`, with zero
   overfull boxes wider than 5pt.
