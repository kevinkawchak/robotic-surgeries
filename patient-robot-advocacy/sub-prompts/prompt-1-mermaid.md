## prompt-1-mermaid

**Stage 1 of 8.** Output directory: [`../mermaid/`](../mermaid). Produces the
**mermaid-type** machine-readable diagram sources for the Patient Robot Advocacy paper.

### Objective

Author the mermaid-type diagram sources for the paper *Patient Robot Advocacy: A Phase 1,
First-in-Human, PDAC Clinical Trial Protocol of a LLM-Directed Robotic Whipple with
Daraxonrasib (RMC-6236)*. Mermaid is chosen wherever the patient's question is **"what
happens, in what order, and who decides?"** - decisions in time. Every other question
belongs to one of the four sibling stages.

### Figure allocation (9 of 30)

| Fig | Mermaid construct | Paper section | Patient-advocacy perspective |
|:--|:--|:--|:--|
| 1 | `flowchart TD` | § 1 Commitment | The seven commitments, consent to day 90 |
| 3 | `flowchart LR` (full page) | § 2 Summary | Journey schema annotated "what you decide here" |
| 7 | `quadrantChart` | § 3 Concerns | Concern prevalence against strength of answer |
| 10 | `flowchart TD` | § 4 Objectives | Objective, endpoint, and what it means for you |
| 14 | `flowchart TD` | § 6 Who joins | Eligibility with self-selection and opt-outs |
| 19 | `sequenceDiagram` | § 7 Operating room | Advise, approve, execute, log |
| 23 | `stateDiagram-v2` | § 8 Stopping | Consent lifecycle with version re-consent |
| 25 | `gantt` | § 9 Visits | Patient visit timeline, screening to 24 months |
| 27 | `xychart` + CI panel (full page) | § 10 Numbers | Quantitative reassurance dashboard |

### Rules for this stage

1. One file per figure, named `fig-NN-slug.md`, where `NN` is the paper-wide figure
   number (`01`, `03`, `07`, `10`, `14`, `19`, `23`, `25`, `27`). Sequential paper
   numbering is preserved across all five diagram stages; the gaps in this stage are
   filled by the sibling stages.
2. Each file opens with an H2 heading `## Figure NN. <title>`, then a **Patient concern
   answered** line, then the fenced ```mermaid block, then a **Palette** table, then a
   **TikZ rendering notes** section that tells the `full-patient` stage exactly how to
   draw the figure with the `mm*` vocabulary of `patientstyle.sty`.
3. **Palette (hard limit, per diagram):** Corporate Blue `#00417A` (`protoblue`),
   Professional Gray `#6C757D` (`protogray`), Classic White `#FFFFFF`, black strokes and
   text; **at most three grayscale fills** - light `#E9ECEF` (`pagrayl`), medium
   `#CED4DA` (`pagraym`), medium-dark `#9AA1A8` (`pagrayd`); and **at most two lighter
   shades of `protoblue`** - `#3C7DB2` (`pablue1`) and `#DCE8F1` (`pablue2`). Black fill
   (`#222222`, `padark`) is used sparingly and never for more than two nodes.
4. Do not copy any figure from `../inputs/phase-1-six-platform-diagrams.zip` or from
   `../inputs/phase-1-trial-protocol.zip`. Every figure is a new composition whose
   subject is the patient's concern, not the sponsor's process.
5. No PNG, no JPG. Sources are Markdown-fenced Mermaid text; the paper renders them as
   vector TikZ.
6. One commit per figure file, pushed the moment it is written. A final commit lands
   `README.md` and `output-mermaid.md` for the stage.

### Sources to draw on

`../inputs/phase-1-trial-protocol.zip` (schema, schedule of activities, endpoints, e-stop
budget, 3+3 escalation); `../research/research-a.md` (Gemini concern set);
`../research/research-b.md` (ChatGPT 16-concern set); `../inputs/cancer-patient-journey.zip`
(autonomous single-patient journey, NSCLC, to be distinguished from PDAC);
`../inputs/patient-priority-physical-ai.zip` (patient as priority participant);
`../references/references.bib` and the protocol `.bib` for citations.
