## output-patient

The complete Claude markdown output for the master prompt in
[`prompt-patient.md`](prompt-patient.md). This is the narrative record of the run: what was
decided, what was built, what broke, and what was measured. It does not reproduce the code
files, which are in the directories they belong to, and it does not reproduce the eight
sub-prompts, which are in [`../sub-prompts/`](../sub-prompts) and are filed again inside
the three paper stages.

## Process A, generating the sub-prompts

The master prompt asks for two processes: generate the sub-prompts, then execute them. Nine
questions had to be settled before the first sub-prompt could be written, because every
one of them constrains all eight stages.

**1. How many diagrams per type.** The master prompt names five permitted types and forbids
Excalidraw, and it says the counts must follow purpose rather than an equal quota. Thirty
does not divide by five evenly in any case. The split was decided from what each idiom is
for:

| Type | Count | The question the idiom answers |
|:--|:--|:--|
| Mermaid | 9 | What happens, in what order, and who decides. Flowchart, sequence, state, gantt, quadrant |
| D2 | 7 | How much of this is there, and how does it group. Containers, grids, sql tables, layers |
| PlantUML | 5 | What exactly do you guarantee. Use case, state machine, timing, sequence with activation |
| Graphviz | 5 | What depends on what, and can you prove it. Rooted DAG, bipartite, decision tree, fault tree |
| Diagrams (Python) | 4 | Where does this physically live. Clustered infrastructure with pictograms |

Mermaid leads because the paper is mostly narrative and Mermaid is the narrative idiom.
Diagrams (Python) trails because only four questions in the paper are about physical
location.

**2. How the diagram sources become figures.** The five directories hold real
machine-readable sources in the native syntax of each platform: `.md` with fenced mermaid,
`.puml`, `.d2`, `.py`, and `.dot`. The paper does not shell out to those tools, because the
master prompt forbids PNG and JPG and because a paper that cannot be rebuilt from its own
`.tex` is not reproducible. Each figure is redrawn in TikZ in a vocabulary that reproduces
the native idiom: `mm*` styles look like Mermaid output, `uml*` like PlantUML, `d2*` like
D2, `dg*` like Diagrams, `gv*` like Graphviz. Every figure frame carries a monospace tag
naming the source construct, so the reader can see which platform's idiom is being spoken.

**3. The spacing rule.** The master prompt requires `\vspace{-0.7cm}` between every diagram
and its own caption, and requires the distance to be identical for every diagram regardless
of what follows. That rules out shrinkable glue anywhere in the figure environment. The
`pafig` environment closes with a rigid `\vskip 26pt`, the source applies
`\vspace{-0.7cm}`, which is `-19.9pt`, and `\figcaption` opens with `\nointerlineskip`. The
frame-to-caption distance is therefore exactly 6.1 pt, everywhere, and is provable rather
than eyeballed.

**4. The palette.** Eleven tokens and no twelfth: the protocol's Corporate Blue, Gray,
White, and black, plus three grayscale fills, plus two lighter blues, plus a near-black
emphasis fill used sparingly, plus the ORCID green for the ORCID mark alone. Eleven tokens
makes a palette audit a grep, which is why the number is fixed rather than open.

**5. Directory structure.** Modelled on `template/trial-protocol-template.zip` but with
`draft-patient`, `full-patient`, `final-patient` in place of the template's three stages,
five diagram-type directories in place of the template's single `mermaid/`, and no
`publication/` under `final-patient`.

**6. Length.** Approximately the same number of text characters as the parent protocol.
The measurement had to be defined before it could be met, and the definition matters: see
the honesty note under Stage 8 below.

**7. Provenance.** No human procedure on this platform has happened. Every performance
number in the paper is therefore a simulation result or a protocol limit, and the paper
would be dishonest if it did not say so on the same line as the number. Four class letters
were fixed at the outset: M measured, C comparator, S simulation, P protocol limit.

**8. Which concerns.** The two research passes give six families and sixteen numbered
concerns, overlapping on five. De-duplicated, twenty-one. That number is load-bearing: the
paper's § 3 has twenty-one rows, Figure 5 has twenty-one nodes, Figure 6 has twenty-one
left-hand entries, and Figure 7 plots sixteen of them.

**9. The NSCLC input.** `inputs/cancer-patient-journey.zip` is a non-small cell lung cancer
journey. It supplies the journey topology and the stack diagram, and the paper says
explicitly where PDAC differs: a pancreaticoduodenectomy with three anastomoses rather than
a lobectomy with one bronchial closure, a RAS(ON) inhibitor rather than a checkpoint
inhibitor, pancreatic fistula rather than prolonged air leak as the dominant early
complication, and a far lower survival baseline.

## Process B, stages 1 to 5, the diagram sources

Five stages, one per diagram type, each producing machine-readable sources, a directory
README, and a stage narrative. Forty commits in total.

The rule that shaped all five: each source is a real file in its platform's syntax that
would render if fed to that platform, and each carries a header comment stating the figure
number, the section it serves, and the concern it answers. The TikZ that eventually draws
it lives in the paper, not here, so the two can be compared.

Three decisions worth recording.

**Pictograms without raster images.** Diagrams (Python) renders node icons as PNGs. PNG is
forbidden, so twenty `\glyph*` macros were written as TikZ line art: a server, a rack, a
camera, an arm, a database, a shield, a person, and so on. They are crude by comparison
with the originals and they are vector, which the master prompt requires.

**Quantitative primitives.** Figure 27 is a five-panel dashboard, and a dashboard drawn by
hand node by node is unmaintainable. Six primitives were written instead: `\hbarrow`,
`\vbarcol`, `\vbarpair`, `\ciband`, `\legkey`, `\donutseg`. They are used by Figures 18,
27, and 28.

**No figure invented a number.** Every quantity in every figure resolves to the parent
protocol, to a cited comparator, or to a stated simulation. Where a figure needed a number
the protocol does not carry, the figure says so rather than inventing one.

## Stage 6, draft-patient

The scaffold. Thirteen sections, the cover page, the style file, the bibliography, and
seventy-eight `\draftinstr{...}` bracketed instructions naming the exact repository file
each later stage must read. Twenty commits.

The cover page is the patient-advocacy variant the master prompt asks for: the parent
protocol's colour scheme unchanged, its furniture replaced. A full-width Corporate Blue
banner instead of a centred title block, four badges instead of a version line, and a
three-panel strip stating what the paper answers before any regulatory text appears: who is
in control, what could go wrong, what is this costing me.

The stage compiled clean at 42 pages with every figure slot empty, which was the point: a
scaffold that does not compile is not a scaffold.

## Stage 7, full-patient

Every bracketed instruction executed, all thirty figures drawn, all tables filled.
Twenty-six commits, six more than planned, because five figures had to be rebuilt after the
verification passes.

The sub-prompt requires the figures to be verified twice, independently. Both passes ran
and both found real defects.

**Pass 1, by re-deriving bounding boxes from coordinates, `text width`, and
`minimum height`, and checking every pair.** Figure 2's four ellipses on one rank at 2.9 cm
pitch overlapped by 4 mm; pitch widened to 4.4 cm and the return edges rerouted into clear
orthogonal channels. Figure 1's three decision diamonds at 2.4 cm pitch left 4 mm; the
diamond text was reduced to one word each and the question moved onto the incoming edge.
Three curved connectors carried no `looseness`.

**Pass 2, by rendering every figure page and reading it.** Figure 6 was legible only at
0.57 scale, so it was recomposed from ellipses to rectangles at a 0.72 cm pitch and now
renders at scale 1. Figure 7's labels collided in four places and were given explicit
offsets with 0.3 pt hairline leaders. Figure 19's `alt` fragment guards sat on the
messages. Figure 24's access edges crossed pipeline nodes diagonally. Figure 12's sentinel
note overlapped a guard. Figure 27's panel C labels collided with its note. Figure 29's
matrix cells all rendered in the default fill.

That last one is worth the detail, because it is the failure mode most likely to recur. The
cell fills were selected with `\ifx` against a `\foreach` variable, which compares a macro
to a character and therefore never matches. Replacing it with `\def` inside the loop
produced `TeX capacity exceeded [input stack size=10000]`. The fix was `\tikzset` styles
per cell class plus a `\racell{col}{row}{letter}{style}` macro. Figures 25 and 26 had the
same conditional-inside-`\foreach` pattern and were rebuilt the same way.

The stage ended at 83 pages, 0 errors, 0 overfull boxes.

## Stage 8, final-patient

The senior author's proof-reading pass. Twenty commits. The full record is in
[`../final-patient/output-final-patient.md`](../final-patient/output-final-patient.md);
what follows is what a reader of this file needs.

**Eight defects were found and listed before any of them was fixed**, which is what the
sub-prompt asks for. Figures set inline stranded the space they could not fit into, on 41
of 83 pages. Two unbreakable tables printed content past the bottom margin. Two headings
were the last thing on their page. Two pairs of figures appeared out of numeric order. The
contents spilled two entries onto a nearly empty fourth page. Captions had drifted out of
the balance band. Eleven cross-references pointed at the wrong subsection once the new
subsections renumbered three sections. And the paper was short of the parent protocol.

**The float carrier** is the largest change. Every figure-plus-caption is wrapped in a
`pafloat`, so running text closes the page and the figure heads the next one. Three
placements were built and measured before `!tb` was kept; `!tp` was rejected because the
`!` makes LaTeX ignore `\floatpagefraction`, so a tall float takes a float page in
preference to the head of the next text page and leaves that page empty. Pages with a
trailing gap over 3 cm fell from 41 of 83 to 15 of 88, and eleven of the fifteen that
remain are a section's last page, which follows directly from the `\clearpage` the prompt
requires between sections.

**Every table is now breakable.** Forty-three of forty-three are `xltabular` with a
repeated header, so no table can run off the foot of a page.

**A correction to Stage 7's own reporting.** Stage 7 claimed 137,000 characters against the
protocol's 147,000, or 93 percent. That comparison counted raw source lines, which flatters
the paper, because its tables carry more markup per visible character than the protocol's.
Measured like for like, with comments, diagram sources, and LaTeX control sequences
stripped from both documents, Stage 7 carried **129,078 visible characters against 155,222,
which is 83 percent, not 93**. Fifteen subsections were added across the thirteen sections
to close the gap, none of them padding, and the paper now carries **168,275 characters, 108
percent of the parent protocol**.

**A figure renumber.** Two pairs appeared out of order. Both figures were in the right
subsection in each case, so the numbers moved rather than the figures: 20 exchanged with
21, 24 with 25, applied to the captions, to fifteen cross-references, to six short-form
`Fig` labels inside Figure 5, to the figure inventory, to the cover panel, and to the four
diagram source files, which were renamed so each still carries the number of the figure it
draws. `full-patient/` was deliberately left alone, because its PDF and archive were built
under the old numbering and are internally consistent; its README carries a note.

## What the finished paper contains

| | Value |
|:--|:--|
| Pages | 88 |
| Sections | 13 |
| Figures | 30, five types, ascending order of appearance |
| Tables | 43, all at body text width, all breakable |
| Visible text characters | 168,275, against the parent protocol's 155,222 |
| Bibliography | 51 entries, every DOI printed and hyperlinked |
| Documented concerns answered | 21, each with its answer class |
| Raster images | none |
| pdfLaTeX | 0 errors, 0 overfull boxes, 0 undefined citations, 0 undefined references |

## What the rules required, and where each is satisfied

| Rule from the master prompt | Where it is satisfied |
|:--|:--|
| Commit only to `robotic-surgeries` | Every commit in this build is in this repository |
| 30 diagrams, five types, no Excalidraw | Five directories, no `excalidraw` vocabulary exists |
| Numbered sequentially 1 to 30 | Verified from document order, ascending, no gaps |
| Caption lines of similar length, at most three | 30 of 30 in band, spread at most 12 characters |
| `\vspace{-0.7cm}` between diagram and caption, identical everywhere | 30 of 30, and the distance is a rigid 6.1 pt |
| Palette plus three grays and two lighter blues | Eleven tokens, audited by grep |
| Directory structure from the template, no `publication/` | `final-patient/` has no `publication/` |
| Comprehensive README per directory with badges | Fifteen READMEs, each naming the files it used from elsewhere |
| Bill citations use H. R. 9510 v5, `10.5281/zenodo.20619762` | § 12 and the cover, and `references.bib` |
| NSCLC distinguished from PDAC | § 2.4 and § 7.1, four named differences |
| Ten robot instruction sets adapted to PDAC | § 9.7, and Figure 26 |
| No PNG or JPG | 0 raster images, 0 `\includegraphics` |
| Tables at body text width, professional column widths | 43 of 43 at `\textwidth`, 0 raw `p{}` columns |
| Every stage compiles in Overleaf | Three archives, each verified with the four-pass build |
| DOI in the form `10.5281/zenodo.xxxxxxxx` with hyperlink | Cover page, twice, and the badges |
| Single dashes only | 0 em dashes, 0 en dashes, 0 prose double dashes |
| `§` and not `SS` | 0 occurrences |
| `\raggedright` with even interword spacing, nothing past the right margin | `\RaggedRight` with `0pt plus 2em`, 0 overfull boxes |
| No stranded single lines | Widow, orphan, and broken penalties at 10000 |
| `prompts/prompt-patient.md` verbatim | Filed unmodified |
| `prompts/output-patient.md` | This file |

## What is open

Three things, stated rather than left to be found.

The eleven section-end gaps are structural. A thirteen-section document whose sections each
start on a fresh page will end up to thirteen of them part way down a page, and closing
them would mean either removing the `\clearpage` the prompt requires or writing text to
fill space.

`../full-patient/` carries the old figure numbering, deliberately, with a note.

The paper is 108 percent of the parent protocol rather than exactly 100. The excess is in
sections 1, 2, and 7, where the participant-facing material has no counterpart in a
protocol written for a regulator. Trimming to hit a character count exactly would remove
the parts that justify the paper existing.
