## prompt-3-d2

**Stage 3 of 8.** Output directory: [`../d2/`](../d2). Produces the **D2-type**
machine-readable diagram sources for the Patient Robot Advocacy paper.

### Objective

Author the D2-type diagram sources. D2 is chosen wherever the patient's question is
**"how much of this is there, and how does it group?"** - containment, true two-dimensional
tabulation, typed record schemas, and stepwise reveals. A concern list of twenty-one items
is unreadable as prose and unreadable as a flowchart; as six nested containers it is
readable in one glance.

### Figure allocation (7 of 30)

| Fig | D2 construct | Paper section | Patient-advocacy perspective |
|:--|:--|:--|:--|
| 4 | `grid-rows` / `grid-columns` | § 2 Summary | Schedule of activities from the patient's chair |
| 5 | nested containers | § 3 Concerns | Twenty-one documented concerns in six families |
| 11 | `sql_table` shapes | § 4 Objectives | Endpoint registry with a plain-language column |
| 16 | `layers` / `steps` | § 6 Who joins | The five choices the participant keeps |
| 21 | container + grid panel | § 7 Operating room | Force caps and vascular no-fly envelope |
| 26 | grid of cards (full page) | § 9 Visits | Ten robot-type instruction cards, PDAC-adapted |
| 29 | grid matrix | § 11 Accountability | Responsibility matrix, who answers for what |

### Rules for this stage

1. One file per figure, named `fig-NN-slug.d2`, with `NN` the paper-wide figure number
   (`04`, `05`, `11`, `16`, `21`, `26`, `29`). The file is valid D2: real `shape:`,
   `style.fill`, `style.stroke`, `grid-rows`, `sql_table`, and `layers` declarations, so
   the source renders outside LaTeX without editing.
2. A leading `# Figure NN.` comment block states the title, the patient concern answered,
   the paper section, and `# TikZ:` notes telling the `full-patient` stage how to draw the
   figure with the `d2*` vocabulary of `patientstyle.sty`.
3. **Palette (hard limit, per diagram):** `protoblue #00417A`, `protogray #6C757D`, white,
   black strokes and text; at most three grayscale fills `#E9ECEF`, `#CED4DA`, `#9AA1A8`;
   at most two lighter blues `#3C7DB2`, `#DCE8F1`; black fill used sparingly.
4. Containment must carry meaning. Nothing that belongs to the patient may be drawn inside
   a container owned by the sponsor, the site, or the regulator; that separation is the
   argument the figure makes.
5. Grids must be true grids: declared rows and columns, no free-floating cells, no cell
   straddling two columns, and no arrow crossing a cell boundary without a labelled port.
6. Do not copy the D2 section of `../inputs/phase-1-six-platform-diagrams.zip`.
7. No PNG, no JPG. One commit per figure file, pushed on write; a final commit lands
   `README.md` and `output-d2.md`.

### Sources to draw on

`../inputs/phase-1-trial-protocol.zip` § 1.3 (schedule of activities), § 3 (objectives and
endpoints), § 6 (force caps, no-fly gating), § 10 (oversight bodies);
`../research/research-b.md` (the sixteen-concern table and the ten minimum-information
items); `../research/research-a.md` (the six Gemini concern families);
`../inputs/patient-robot-instructions.tex` (the ten robot types, to be re-scoped from the
NSCLC and general-oncology setting to this PDAC Whipple protocol).
