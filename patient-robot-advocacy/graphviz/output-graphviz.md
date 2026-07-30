## output-graphviz

Stage 5 narrative, run from
[`../sub-prompts/prompt-5-graphviz.md`](../sub-prompts/prompt-5-graphviz.md). This is the
last of the five diagram stages; all thirty figure sources now exist.

### What was produced

Five Graphviz-type diagram sources, figures 2, 6, 13, 20, and 28 of the paper's thirty. One
of the five is a full-page figure. One commit per file, pushed on write, plus a README
commit and this narrative.

### The organising idea of the stage

The four preceding stages answer what happens, what is guaranteed, how much there is, and
where it lives. This stage answers the question a sceptical reader asks last: can you prove
the structure is what you say it is. Every figure here states a graph invariant in its
header comment, and the invariant is the claim. A bipartite map that turned out not to be
bipartite would have answered a concern with another concern; a DAG with a cycle would have
a body reviewing itself.

### Decisions made during the stage

1. **Figure 2 inverts the root without overstating the result.** Putting the participant at
   the root of an accountability chart is easy to do dishonestly. The figure resists that by
   drawing only three edges pointing back at the root, each labelled with a specific
   obligation: tell you about a version change, a new risk, or your own results; tell you
   about a study pause; tell you about an adverse event affecting you. Three is what the
   protocol actually owes, and three is what is drawn.

2. **Figure 6 is the load-bearing figure of the paper and is drawn full page.** Twenty-one
   concerns on the left, nineteen clauses on the right, twenty-four edges between them.
   Fourteen edges are solid blue, meaning a hard numeric limit answers the concern; seven
   are solid gray, meaning a procedural guarantee; three are dashed, meaning governance or
   disclosure only. A reader who takes nothing else from the paper can take this figure.

3. **Figure 13 includes the stopping leaf.** The 3+3 rule is usually drawn as an escalation
   ladder. Drawing it as a tree exposes that two of its terminals are stops, one of which
   convenes the DSMB and results in the participant being told. A dose-escalation figure
   without a stopping leaf would misrepresent the rule.

4. **Figure 20 names a single point of failure.** Registration drift beyond 2 mm is caught
   by the deterministic gate and by nothing else. Barrier 5 is filled medium-dark gray and
   labelled `SINGLE BARRIER ONLY`. Fault trees exist to find exactly this, and suppressing
   it would have made the other four barriers less credible.

5. **Figure 28 makes the paper's own numbers auditable.** Nine quoted values, six sources,
   four evidence classes. Two of the nine values are class S, author simulation rather than
   human data. The black rule node at the foot states that every place those two are quoted
   says so on the same line, which is a commitment the body text then has to keep.

6. **All five figures were checked against the atlas.** The parent
   `phase-1-six-platform-diagrams` archive carries twenty Graphviz-type figures. None of
   these five reproduces one of them: the atlas draws the sponsor's system, and these draw
   what the participant is owed, what answers their concerns, and where the evidence came
   from.

### Verification performed

| Check | Result |
|:--|:--|
| Five files present, figure numbers 2, 6, 13, 20, 28 | pass |
| Every file is valid DOT with `rankdir`, node shapes, and cluster subgraphs | pass |
| Every file carries a `// Figure NN.` header block and `// TikZ:` rendering notes | pass |
| Every file states its graph invariant in the header | pass, 5 of 5 |
| Figure 2 acyclic | pass |
| Figure 6 bipartite, 24 edges all cross-partition | pass |
| Figure 13 is a tree, one path per leaf | pass |
| Figure 20 all paths terminate in a basic event, all gates typed | pass |
| Figure 28 no value node without an incoming edge | pass, 9 of 9 |
| Every curved connector in the TikZ notes declares an explicit `looseness` | pass |
| Per-diagram palette budget respected | pass; Figure 20 is the only figure using all three grays, and does so to grade barrier strength |
| No figure reproduces a figure from either input archive | pass |
| No PNG, no JPG | pass |

### Commits in this stage

| # | Commit | File |
|:--|:--|:--|
| 1 | Figure 2, accountability DAG rooted at the participant | `fig-02-accountability-dag.dot` |
| 2 | Figure 6, full-page concern-to-clause bipartite map | `fig-06-concern-to-clause.dot` |
| 3 | Figure 13, 3+3 escalation decision tree | `fig-13-escalation-decision-tree.dot` |
| 4 | Figure 20, hazard and barrier fault tree | `fig-20-hazard-barrier-fault-tree.dot` |
| 5 | Figure 28, evidence provenance DAG | `fig-28-evidence-provenance.dot` |
| 6 | Stage README | `README.md` |
| 7 | This narrative | `output-graphviz.md` |

### All thirty figures now have a source

| Type | Count | Figure numbers |
|:--|:--|:--|
| Mermaid-type | 9 | 1, 3, 7, 10, 14, 19, 23, 25, 27 |
| D2-type | 7 | 4, 5, 11, 16, 21, 26, 29 |
| PlantUML-type | 5 | 8, 12, 15, 18, 22 |
| Graphviz-type | 5 | 2, 6, 13, 20, 28 |
| Diagrams (Python)-type | 4 | 9, 17, 24, 30 |
| **Total** | **30** | **1 to 30, no gaps, no duplicates** |

### Handoff to Stage 6

[`../draft-patient/`](../draft-patient) builds the bracketed LaTeX scaffold: `main.tex`
with the patient-advocacy cover page, `patientstyle.sty` carrying all five diagram
vocabularies, `references.bib` merging three bibliographies into one format, and thirteen
`sections/*.tex` files in which every figure slot and every table is present and every
remaining decision is marked with a `\draftinstr{...}` naming the exact repository file
that supplies it.
