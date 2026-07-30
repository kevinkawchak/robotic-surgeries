## prompt-4-diagrams-python

**Stage 4 of 8.** Output directory: [`../diagrams-python/`](../diagrams-python). Produces
the **Diagrams (Python)-type** machine-readable diagram sources for the Patient Robot
Advocacy paper.

### Objective

Author the Diagrams (Python)-type sources. `mingrammer/diagrams` is chosen wherever the
patient's question is **"where does this physically live?"** - which box holds the model,
which cable it runs on, which room the console is in, which network the data never leaves.
Concerns 10 and 11 of the ChatGPT set (privacy, recording, secondary use; cybersecurity and
network dependence) cannot be answered by a flowchart. They are answered by an
infrastructure diagram that shows the air gap.

### Figure allocation (4 of 30)

| Fig | Diagrams construct | Paper section | Patient-advocacy perspective |
|:--|:--|:--|:--|
| 9 | clustered node map | § 3 Concerns | Where each documented concern physically lives |
| 17 | deployment (full page) | § 7 Operating room | Operating room and on-premises stack, air gap shown |
| 24 | data pipeline | § 9 Visits | Capture, hash chain, and exactly who can read it |
| 30 | lifecycle architecture | § 12 Rights | Post-trial continuity, cost coverage, and device support |

### Rules for this stage

1. One file per figure, named `fig-NN-slug.py`, with `NN` the paper-wide figure number
   (`09`, `17`, `24`, `30`). Each file is a runnable, import-guarded
   `mingrammer/diagrams` script: a module docstring, `from diagrams import ...`, a
   `with Diagram(...)` block, `Cluster` groupings, and `Edge` styling that carries the
   palette. Guard the import so the file is lint-clean and executes as a no-op when the
   `diagrams` package is absent.
2. The module docstring states the figure number, the title, the patient concern answered,
   the paper section, and the TikZ rendering notes for the `dg*` vocabulary of
   `patientstyle.sty`.
3. **Palette (hard limit, per diagram):** `protoblue #00417A`, `protogray #6C757D`, white,
   black strokes and text; at most three grayscale fills `#E9ECEF`, `#CED4DA`, `#9AA1A8`;
   at most two lighter blues `#3C7DB2`, `#DCE8F1`; black fill used sparingly. Declare the
   palette once as module-level constants and reference the constants everywhere.
4. Every node carries a vector pictogram in the LaTeX rendering; no raster provider icons.
   The paper draws each node as a rounded tile with the pictogram inside and the label set
   beneath it, exactly as `mingrammer/diagrams` lays out a node.
5. Code style: 4-space indentation, double-quoted strings, no line above 100 characters,
   no unused imports, and no wildcard imports, so `ruff format --check` and `ruff check`
   pass if the repository lint scope is ever widened to this directory.
6. Do not copy the Diagrams (Python) section of
   `../inputs/phase-1-six-platform-diagrams.zip`.
7. No PNG, no JPG; `Diagram(..., show=False)` and no rendered output committed. One commit
   per figure file, pushed on write; a final commit lands `README.md` and
   `output-diagrams-python.md`.

### Sources to draw on

`../inputs/phase-1-trial-protocol.zip` § 6 (eight-arm platform, 10 kHz heartbeat bus,
on-premises inference), § 8 (assessments and telemetry), § 10 (audit trail, 21 CFR part
11); `../research/research-b.md` concerns 10, 11, 12, 13, 16;
`../inputs/cancer-patient-journey.zip` (the autonomous single-patient journey stack, NSCLC,
to be re-scoped to PDAC); `../references/references.bib` (`FDACyber2026`, `FDATrans2024`).
