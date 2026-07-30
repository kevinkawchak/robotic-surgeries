## output-diagrams-python

Stage 4 narrative, run from
[`../sub-prompts/prompt-4-diagrams-python.md`](../sub-prompts/prompt-4-diagrams-python.md).

### What was produced

Four Diagrams (Python)-type sources, figures 9, 17, 24, and 30 of the paper's thirty. One
of the four is a full-page figure. One commit per file, pushed on write, plus a README
commit and this narrative.

### Why four and not more

The master prompt forbids equal quotas and requires the count to follow purpose. This idiom
answers exactly one question well: where does a thing physically live. Four of the paper's
questions are of that kind, and forcing a fifth would have meant drawing a process as
though it were a rack.

### Decisions made during the stage

1. **Three of the four figures argue by absence.** The most persuasive thing an
   infrastructure diagram can do for a patient worried about cybersecurity is show the
   cable that is not there. Figures 9, 17, and 24 each carry a struck-through or entirely
   missing edge, and each says in its docstring that the absence is the argument.

2. **Figure 17 lists what does cross the boundary.** A diagram that showed only a sealed
   box would be false: a signed model build and a protocol version cross the boundary
   before the procedure, and reports to the FDA and the IRB cross it afterwards. Naming all
   three, and marking only the intra-procedural path as absent, is the accurate claim.

3. **Figure 24 states retention in years, per store.** "Retained as required by
   regulation" is not an answer. The figure prints 10 or 15 years on each store tile and
   lists, per store, the roles that may read it. A role that is absent from a list cannot
   read that store, and no edge is drawn for it.

4. **Figure 30 is the weakest part of the argument, and closes the paper.** Cost and
   post-trial continuity sit in the honest-gap quadrant of Figure 7. Two items are marked
   `open` in the payer table: lost income, and continued drug access after closure. Both
   remain open, and the figure says so on the tile rather than in a footnote. The
   legislative proposal that would close them is drawn as a dotted edge, not a solid one,
   because it is a proposal.

5. **The NSCLC distinction is stated in code.** Figure 17's docstring carries a
   "Distinguished from the NSCLC journey" block naming the four differences that matter to
   a PDAC reader: eight arms rather than four, three anastomoses rather than one bronchial
   closure, the vascular exclusion envelope around the superior mesenteric and portal
   veins, and the different dominant early complication.

6. **Lint standards were applied even though CI does not reach this directory.** The
   repository's `lint-and-format` job runs `ruff` against `2030-gbm-1min` only. These files
   are held to the same standard so that widening the lint scope later cannot break the
   build.

### Verification performed

| Check | Result |
|:--|:--|
| Four files present, figure numbers 9, 17, 24, 30 | pass |
| `python -m py_compile` on all four | pass |
| `ruff format --check .` | pass |
| `ruff check .` | pass, no findings |
| Import guard present, `build()` returns cleanly without the `diagrams` package | pass |
| `show=False` and `outformat="svg"` on every `Diagram` | pass, no raster output possible |
| Palette declared once as module constants and referenced everywhere | pass |
| Protocol limits printed on tiles match the parent protocol | pass, checked against § 6 |
| Every curved connector in the rendering notes declares an explicit `looseness` | pass |
| Per-diagram palette budget respected | pass, maximum two grays and one lighter blue |
| No figure reproduces a figure from either input archive | pass |

### Commits in this stage

| # | Commit | File |
|:--|:--|:--|
| 1 | Figure 9, concern-to-component address map | `fig_09_concern_locations.py` |
| 2 | Figure 17, full-page operating room and on-premises stack | `fig_17_operating_room_stack.py` |
| 3 | Figure 24, data pipeline with per-store read lists | `fig_24_data_pipeline.py` |
| 4 | Figure 30, post-trial continuity and payer map | `fig_30_post_trial_continuity.py` |
| 5 | Stage README | `README.md` |
| 6 | This narrative | `output-diagrams-python.md` |

### Handoff to Stage 5

[`../graphviz/`](../graphviz) takes figures 2, 6, 13, 20, and 28, the last of the diagram
stages. The boundary: Stage 4 answers "where does it live"; Stage 5 answers "what depends
on what, and can you prove it". Figure 17 here shows the boxes; Figure 20 there shows,
as a fault tree, which box catches which failure, and Figure 28 traces every number in the
paper back to the source that produced it.
