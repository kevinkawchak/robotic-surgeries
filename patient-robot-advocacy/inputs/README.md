# inputs - source material for the Patient Robot Advocacy build (v1.0.0)

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Inputs](https://img.shields.io/badge/Inputs-5-00417A.svg)](.)
[![Protocol DOI](https://img.shields.io/badge/Protocol%20DOI-10.5281%2Fzenodo.20780121-blue.svg)](https://doi.org/10.5281/zenodo.20780121)
[![Patient Priority DOI](https://img.shields.io/badge/Patient%20Priority-10.5281%2Fzenodo.20045457-blue.svg)](https://doi.org/10.5281/zenodo.20045457)
[![Patient Journey DOI](https://img.shields.io/badge/Patient%20Journey-10.5281%2Fzenodo.19119939-blue.svg)](https://doi.org/10.5281/zenodo.19119939)
[![Instructions DOI](https://img.shields.io/badge/Instructions-10.5281%2Fzenodo.18810541-blue.svg)](https://doi.org/10.5281/zenodo.18810541)
[![Raster](https://img.shields.io/badge/Raster%20images-none-6C757D.svg)](.)

Five author sources drive the whole build. Nothing in this directory is modified by the
build; every downstream stage reads from here and writes elsewhere.

## What each input supplies

### 1. `phase-1-trial-protocol.zip`

The parent clinical document: *A Phase 1, First-in-Human, Combined IND/IDE Clinical Trial
Protocol of On-Premises LLM-Directed Robotic Pancreaticoduodenectomy (Whipple) with
Perioperative Daraxonrasib (RMC-6236) in KRAS-Mutated PDAC*, v1.0.0,
[`10.5281/zenodo.20780121`](https://doi.org/10.5281/zenodo.20780121).

| Contents | Consumed by | For |
|:--|:--|:--|
| `main.tex` | [`../draft-patient/main.tex`](../draft-patient) | cover-page structure, TOC pattern, one `\input` per section |
| `protostyle.sty` | `patientstyle.sty` in all three paper stages | palette `#00417A` / `#6C757D`, RaggedRight body, `L`/`C`/`R`/`Y` columns, widow and orphan penalties, PNG-free ORCID mark |
| `references.bib` | `references.bib` in all three paper stages | the exact BibTeX field order and the `doi` + `url` + `note` triad |
| `sections/sec-00` … `sec-12` | all thirteen patient sections | the clinical facts being advocated for: schedule of activities, 3+3 escalation, force caps, e-stop budget, ISGPS grading, oversight bodies, analysis populations |

This is also the **paper template**. The patient paper keeps the protocol's colour scheme
and typography and changes the cover page, the section titles, and the figure vocabulary.

### 2. `patient-priority-physical-ai.zip`

*Patient Priority of Proposed U.S. Bills for Physical AI Oncology Clinical Trials*,
[`10.5281/zenodo.20045457`](https://doi.org/10.5281/zenodo.20045457). Seven proposed bills
(H. R. 9501 to H. R. 9507) written around one premise: the cancer patient, not the doctor,
the nurse, the trial sponsor, the IRB, or the regulator, is the priority participant in a
United States oncology clinical trial.

Consumed by [`../final-patient/sections/sec-11-rights.tex`](../final-patient/sections) and
by Figures 2, 14, 15, 16, and 29. **Citation note:** bill citations in this paper use the
author's updated legislation, **H. R. 9510 v5**,
[`10.5281/zenodo.20619762`](https://doi.org/10.5281/zenodo.20619762), not the earlier
H. R. 9501 to H. R. 9507 numbering.

### 3. `cancer-patient-journey.zip`

*A Cancer Patient's Journey Through a Regulated Physical AI Oncology Trial*,
[`10.5281/zenodo.19119939`](https://doi.org/10.5281/zenodo.19119939). The first fully
autonomous, single-patient journey through a regulated Physical AI oncology clinical trial.

Consumed by Figures 3, 9, 17, and 24 and by
[`../final-patient/sections/sec-01-summary.tex`](../final-patient/sections).
**Scope note:** that simulation is **NSCLC**. This paper is **PDAC**, and every section
that borrows a journey structure from it states the distinction explicitly, because the
operation, the drug, the fistula risk, and the survival baseline all differ.

### 4. `patient-robot-instructions.tex`

*Patient Instructions: Physical AI Oncology Trials - Instructional Sheets for 10 Robot
Types*, [`10.5281/zenodo.18810541`](https://doi.org/10.5281/zenodo.18810541). Ten
self-contained instruction sheets: surgical robots, cobots, radiotherapy positioning
robots, needle-placement robots, companion robots, humanoids, radiotherapy motion-tracking
robots, imaging robots, steerable needle robots, and rehabilitation exoskeletons.

Consumed by [`../final-patient/sections/sec-08-assessments.tex`](../final-patient/sections)
and by Figure 26, where all ten sheets are re-scoped from their original mixed-oncology
setting to this Phase 1 PDAC Whipple protocol: the surgical-robot sheet becomes the
eight-arm Whipple sheet, the imaging sheet becomes the CA 19-9 and RECIST sheet, and so on.
The original file references `images/1.png` to `images/10.png`; **no raster image is
carried into this build**, and the ten sheets are re-expressed as a D2-type card grid.

### 5. `phase-1-six-platform-diagrams.zip`

*A Six-Platform Diagram Atlas of the Phase 1 Physical AI Pancreatic Whipple and
Daraxonrasib Clinical Trial Protocol*, 120 figures across Mermaid, Excalidraw, PlantUML,
D2, Diagrams (Python), and Graphviz, all rendered natively in TikZ.

Consumed by all five diagram stages as **vocabulary context only**. Its `dxstyle.sty`
demonstrates how each platform's idiom is reproduced in TikZ; the patient paper's
`patientstyle.sty` adapts that approach to a restricted palette and a patient-advocacy
subject. **No figure from this atlas is copied.** The Excalidraw section is read for
context and produces no output, because the master prompt excludes Excalidraw diagrams.

## Where each input lands in the paper

| Input | Sections | Figures |
|:--|:--|:--|
| `phase-1-trial-protocol.zip` | all thirteen | all thirty |
| `patient-priority-physical-ai.zip` | § 1, § 6, § 11, § 12 | 2, 14, 15, 16, 29 |
| `cancer-patient-journey.zip` | § 2, § 7, § 9 | 3, 9, 17, 24 |
| `patient-robot-instructions.tex` | § 9 | 26 |
| `phase-1-six-platform-diagrams.zip` | none directly | vocabulary for all thirty |

## License

Released under CC BY 4.0; reproduced U.S. Government regulatory text is used under
17 U.S.C. § 105. Author: Kevin Kawchak, CEO ChemicalQDevice
([ORCID 0009-0007-5457-8667](https://orcid.org/0009-0007-5457-8667)).
