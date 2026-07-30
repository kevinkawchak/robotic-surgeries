## prompt-5-graphviz

**Stage 5 of 8.** Output directory: [`../graphviz/`](../graphviz). Produces the
**Graphviz-type** machine-readable diagram sources for the Patient Robot Advocacy paper.

### Objective

Author the Graphviz-type sources. Graphviz is chosen wherever the patient's question is
**"what depends on what, and can you prove it?"** - pure graph structure with no
narrative sugar: directed acyclic graphs, bipartite maps, fault trees, decision trees, and
provenance chains. When a patient asks "where does that number come from?", the honest
answer is a provenance DAG, not a paragraph.

### Figure allocation (5 of 30)

| Fig | Graphviz construct | Paper section | Patient-advocacy perspective |
|:--|:--|:--|:--|
| 2 | `digraph` rooted DAG | § 1 Commitment | Accountability chain rooted at the patient |
| 6 | bipartite map (full page) | § 3 Concerns | Every concern wired to the clause answering it |
| 13 | decision tree | § 5 Design | 3+3 escalation with the sentinel waiting period |
| 20 | fault tree | § 7 Operating room | Each hazard and the barrier that catches it |
| 28 | provenance DAG | § 10 Numbers | Every quoted number traced back to its source |

### Rules for this stage

1. One file per figure, named `fig-NN-slug.dot`, with `NN` the paper-wide figure number
   (`02`, `06`, `13`, `20`, `28`). The file is valid DOT: a `digraph` or `graph` block with
   real `rankdir`, `node [shape=...]`, `subgraph cluster_*`, `rank=same`, and record-label
   syntax where a record node is used, so `dot -Tsvg` renders it without editing.
2. A leading `// Figure NN.` comment block states the title, the patient concern answered,
   the paper section, and `// TikZ:` notes telling the `full-patient` stage how to draw the
   figure with the `gv*` vocabulary of `patientstyle.sty`.
3. **Palette (hard limit, per diagram):** `protoblue #00417A`, `protogray #6C757D`, white,
   black strokes and text; at most three grayscale fills `#E9ECEF`, `#CED4DA`, `#9AA1A8`;
   at most two lighter blues `#3C7DB2`, `#DCE8F1`; black fill used sparingly.
4. Graph discipline: a DAG has no cycle, a bipartite map has no intra-partition edge, a
   fault tree distinguishes AND gates from OR gates and terminates in basic events, and a
   decision tree has exactly one path from root to each leaf. State the invariant in the
   comment block so the `final-patient` stage can re-verify it.
5. Graphviz's default look is honoured: Times labels, thin black strokes, plain ellipses
   for ordinary nodes, ruled record boxes for structured nodes, dashed cluster subgraphs
   with a corner title.
6. Do not copy the Graphviz section of `../inputs/phase-1-six-platform-diagrams.zip`.
7. No PNG, no JPG. One commit per figure file, pushed on write; a final commit lands
   `README.md` and `output-graphviz.md`.

### Sources to draw on

`../inputs/phase-1-trial-protocol.zip` § 0 (compliance spine), § 4 (3+3 escalation and
sentinel staggering), § 9 (statistics and analysis populations), § 10 (oversight and audit
trail); `../research/research-a.md` (the accountability question, "who is to blame?");
`../research/research-b.md` (concerns 1, 4, 7, 15 and the thirteen numbered sources);
`../inputs/patient-priority-physical-ai.zip` (the patient at the root of the chain, not the
leaf); `../references/references.bib` and the protocol `.bib` for the provenance targets.
