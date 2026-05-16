# README — Deep Research Chunked Files for Physical AI Oncology Trial Paper

## Purpose

This README is provided to Claude Code Opus 4.7 (1M context) Max to assist in processing all five chunked markdown files derived from the source document `Deep-Research-B.docx`. The source document is a deep-research synthesis report (structured as an academic white paper) reviewing four major 2026 AI/oncology projects and their relevance to building a new physical AI oncology trial paper. All five chunk files together constitute the complete, unabridged text of the original document. No content has been paraphrased, summarized, or abbreviated; every chunk is word-for-word from the source.

---

## File Index

| File | Contents | Approx. Tokens |
|---|---|---|
| `chunk_01_executive_summary_and_fully_automated_sponsor.md` | Executive Summary + Fully Automated Sponsor section (Kawchak 2026) | ~1,100 |
| `chunk_02_federated_learning_and_patient_prediction.md` | Federated Learning Platform section + Accelerated Patient Prediction section (both Kawchak 2026) | ~1,200 |
| `chunk_03_clinagent.md` | ClinAgent section (Yan 2026, Harrisburg Univ.) | ~750 |
| `chunk_04_comparative_overview_and_implications.md` | Comparative Overview table + Development Timeline narrative + Sources + Code/Data Availability + Implications | ~650 |
| `chunk_05_bibtex_references.md` | All five BibTeX entries + inline URL citations as they appear in the source document | ~400 |

---

## Detailed Description of Each Chunk File

### chunk_01_executive_summary_and_fully_automated_sponsor.md

**What it contains:**
- The **Executive Summary** of the entire source document, which introduces all four projects, states the overarching thesis (Claude Code compresses trial development timelines from months to days), and names key metrics (288 automated decisions, 100% code-review completion, AUC > 0.89, 72% spec accuracy).
- The complete **Fully Automated Sponsor (Kawchak 2026)** section, covering: Institution, Domain, Application, Role of Claude Code, Prototyping Method & Timeline, Hardware/Software Stack, Data & Provenance, Validation & Performance, Regulatory/Ethical Status, Deployment & Use, Limitations & Failures, and Implications subsections.

**Key facts and figures introduced in this chunk:**
- Claude Code version: Opus 4.6
- 108 Python modules generated; ~75 files; 13 commits in 72 minutes
- 24-hour simulation; 155 virtual cancer patients; 288 automated sponsor decisions
- NVIDIA Isaac Gym, Amazon AWS, PyBullet, MCP tools cited
- ICH E6, 21 CFR, IRB compliance encoded in simulation
- 75 annotated diagrams produced; consent summaries generated
- KukA robots mentioned as future integration target
- Zenodo DOI: 10.5281/zenodo.19396256

**Cross-references to other chunks:**
- The Executive Summary introduces ALL four projects; detailed treatment of the other three is in chunks 02, 03, and 04.
- The Fully Automated Sponsor is row 1 of the Comparative Overview Table in chunk 04.
- Reference [1] (BibTeX entry `kawchak2026sponsor` in chunk 05) is the primary citation for this entire section.
- "Hardware demands were minimal" and "Core i5" references from this section are elaborated in chunk 02 (Patient Prediction).
- The MCP framework discussed here is the same infrastructure discussed in the Federated Learning Platform (chunk 02) and ClinAgent (chunk 03).

---

### chunk_02_federated_learning_and_patient_prediction.md

**What it contains:**
- The complete **Federated Learning Platform (Kawchak 2026)** section, covering: Institution, Domain, Application, Role of Claude Code, Prototyping Method & Timeline, Hardware/Software Stack, Data & Provenance, Validation & Performance, Regulatory/Ethical Status, Deployment & Use, Limitations & Failures, and Implications subsections.
- The complete **Accelerated Patient Prediction (Kawchak 2026)** section, covering the same subsection structure.

**Key facts and figures — Federated Learning Platform:**
- Claude Code version: Opus 4.6 (dual-AI peer review with OpenAI Codex)
- 5 MCP servers (Clinical Data, Imaging, Audit Ledger, plus two others)
- 23 exposed tools; 668/668 test functions passed; 31/31 code recommendations resolved (100%)
- 381 files, 288 KLOC in code repository
- Node.js, Python, Angular, AWS, Google Cloud, FHIR, DICOM/HL7
- HIPAA, FDA CFR Part 11, ICH E6 compliance embedded
- Zenodo DOI: 10.5281/zenodo.18795507

**Key facts and figures — Accelerated Patient Prediction:**
- Claude Code version: Opus 4.7 Max
- 4 simulated trial scenarios; 7-day (168h) continuous sponsor extension
- Hourly code commits (~24/day); 1M-token context window utilized
- ML AUC > 0.89, surpassing Huang 2025 Cox regression baseline AUC 0.89
- Hardware: Core i5-6200U laptop, 4 GB RAM (final validation); Amazon EC2 g5.24xlarge (development)
- XGBoost, TensorFlow, scikit-learn cited; Python ML pipeline
- 93,000+ synthetic observations; Huang 2025 data patterned
- Zenodo DOI: 10.5281/zenodo.19994945

**Cross-references to other chunks:**
- Both projects belong to the same Kawchak 2026 author group introduced in chunk 01.
- The Federated Learning Platform and Patient Prediction are rows 2 and 3 of the Comparative Overview Table in chunk 04.
- References [2] and [3] (BibTeX entries `kawchak2026federated` and `kawchak2026prediction` in chunk 05) are the primary citations for these sections.
- The MCP server architecture described in Federated Learning connects directly to the MCP tools used in the Fully Automated Sponsor (chunk 01) and ClinAgent (chunk 03).
- The "dual-AI review" (Claude Code + Codex) methodology is unique to this chunk; no other section uses it.
- The Core i5 / 4 GB RAM hardware reference in Patient Prediction answers the "hardware demands were minimal" claim made in the Executive Summary (chunk 01) and repeated in the closing narrative (chunk 04).

---

### chunk_03_clinagent.md

**What it contains:**
- The complete **ClinAgent (Yan 2026)** section, covering: Institution, Domain, Application, Role of Claude Code, Prototyping Method & Timeline, Hardware/Software Stack, Data & Provenance, Validation & Performance, Regulatory/Ethical Status, Deployment & Use, Limitations & Failures, and Implications subsections.

**Key facts and figures:**
- Author: J. Yan; Institution: Harrisburg University of Science & Technology
- Published as medRxiv preprint, January 2026
- 9 skill modules implemented (study setup through eSubmission packaging)
- SAS/CDISC workflows; TLF (table/listing/figure) generation
- Claude Code: model-agnostic; demonstrated with Claude Code (Enterprise/Pro tier)
- Python 3.11+, pandas, pyreadstat, openpyxl, MCP SDK (Python & TypeScript)
- 11 ADaM domains, 93,239 synthetic observations (Python Faker library)
- Phase 2 cardiovascular trial specs used ("STUDY-A"); no PHI
- 100% precision on log/data deterministic checks (1 error, 7 warnings found correctly)
- 56 variables validated correctly
- 72.1% overall accuracy for AI-generated table specifications; >96% for simple domains
- ~30–50% baseline accuracy for generic LLMs without domain guidance
- 12–24 FTE-months typically required for Phase 3 trial programming (avoided by ClinAgent)
- License: MIT open-source on GitHub
- DOI: 10.64898/2026.01.09.26343542

**Cross-references to other chunks:**
- ClinAgent is the only non-Kawchak project; it comes from Harrisburg University (Yan 2026), not the Pittsburgh AI Lab.
- ClinAgent is row 4 of the Comparative Overview Table in chunk 04.
- Reference [4] (BibTeX entry `yan2026clinagent` in chunk 05) is the primary citation for this section.
- The "MCP tools for data I/O" architecture in ClinAgent is philosophically and technically aligned with the MCP servers described in the Federated Learning Platform (chunk 02) and the MCP regulatory tools in the Fully Automated Sponsor (chunk 01).
- The 93,239 synthetic observations in ClinAgent parallel the synthetic patient data approach used across all Kawchak projects (chunks 01 and 02).
- The 72.1% accuracy benchmark in ClinAgent is the only performance figure below 100% across all projects; this nuance is summarized in the Comparative Overview (chunk 04).
- ClinAgent's CDISC compliance and eSubmission packaging are the most directly applicable components to a new physical AI oncology trial paper's regulatory submission workflow.

---

### chunk_04_comparative_overview_and_implications.md

**What it contains:**
- The **Comparative Overview** table (5 rows: 4 research projects + Industry Case Studies row), comparing all projects across Domain/Institution, Claude Code Version, Prototyping & Timeline, Key Results/Performance, and Status/Notes.
- The **Development Timeline (2026)** section with figure caption referencing Murugappan's mCRC CRF case.
- The closing **narrative paragraph** synthesizing hardware, tech stack, performance, and prototype status across all projects.
- The **Sources** declaration paragraph.
- The **Code and Data Availability** statement.
- The **Implications** closing paragraph synthesizing the convergence of Claude Code, MCP, and AI agent methods toward automated Physical AI oncology trial workflows.

**Key facts and figures unique to this chunk:**
- Industry Case Studies row: Schrödinger (chemistry) and Axiom Bio (toxicology) — Opus 4.x (Sonnet/Opus); "ideas to code in minutes, 10× faster" (Schrödinger); "billions of tokens" for drug-toxicity features (Axiom Bio)
- Murugappan's mCRC CRF case referenced informally
- "0–30% error/hallucination rate inherent to LLMs" stated as a known limitation
- Confirms: no clinical deployments found as of May 15, 2026
- All cited works open-access; Kawchak on Zenodo; ClinAgent on GitHub

**Cross-references to other chunks:**
- This chunk is the synthesis and summary of all content in chunks 01–03; it introduces no new project sections but compiles their key metrics into the table.
- Every row in the Comparative Overview Table maps directly to a section in chunks 01 (row 1), 02 (rows 2 and 3), and 03 (row 4).
- The Industry Case Studies row (row 5) is supplementary; the primary source is Reference [5] (BibTeX entry `anthropic2026lifesciences` in chunk 05).
- The "Development Timeline" figure caption references Murugappan's mCRC CRF, which does not have its own section in this document; it is an informal/ancillary reference.
- The Implications paragraph in this chunk consolidates the individual implications paragraphs at the end of each project section in chunks 01, 02, and 03.
- The statement "no clinical deployments found by May 15, 2026" in Sources provides the temporal anchor for the entire document.

---

### chunk_05_bibtex_references.md

**What it contains:**
- Five complete BibTeX entries for all numbered references in the document:
  1. `kawchak2026sponsor` — Fully Automated Sponsor (Zenodo)
  2. `kawchak2026federated` — Federated Learning Platform (Zenodo)
  3. `kawchak2026prediction` — Accelerated Patient Prediction (Zenodo)
  4. `yan2026clinagent` — ClinAgent (medRxiv)
  5. `anthropic2026lifesciences` — Claude for Life Sciences (Anthropic News)
- Two inline URL citation records as they appear verbatim in the source document (healthaiinsiders.com and researchgate.net).

**Cross-references to other chunks:**
- `kawchak2026sponsor` [1] → cited throughout chunk 01 (Fully Automated Sponsor section and Executive Summary)
- `kawchak2026federated` [2] → cited throughout chunk 02 (Federated Learning Platform section)
- `kawchak2026prediction` [3] → cited throughout chunk 02 (Accelerated Patient Prediction section) and once in chunk 01 (Executive Summary hardware claim)
- `yan2026clinagent` [4] → cited throughout chunk 03 (ClinAgent section) and once in chunk 01 (Executive Summary accuracy claim)
- `anthropic2026lifesciences` [5] → cited in chunk 04 (Industry Case Studies row and Implications) and once in chunk 01 (Executive Summary clinician empowerment claim)
- The researchgate.net URL corresponds to `yan2026clinagent` [4] references [2], [3], [4] as labeled inline in the source document — these are internal footnote numbers pointing to specific text spans in the ClinAgent paper's ResearchGate page, not separate publications.
- The healthaiinsiders.com URL corresponds to references [1] and [5] inline, linking back to both Kawchak's sponsor work and the Anthropic life sciences news.

---

## How All Chunked Files Correlate to Each Other

### Unified Thesis
All five chunks together argue a single thesis: **Claude Code (Anthropic's agentic coding LLM) can compress oncology clinical trial software development from months to days while producing production-quality, compliance-ready code.** Every section, table, implication, and reference supports this thesis.

### Project Lineage
Three of the four research projects (chunks 01 and 02) belong to the same author (Kawchak 2026) and the same lab ("Physical AI trials lab"). They form a progression:
1. **Sponsor automation** (chunk 01): Can AI run an entire trial sponsor role?
2. **Data federation** (chunk 02, first section): Can AI build the underlying multi-site data infrastructure?
3. **Outcome prediction** (chunk 02, second section): Can AI continuously improve predictive models within the same trial framework?
ClinAgent (chunk 03) is from a different institution (Harrisburg University, Yan 2026) but addresses the downstream statistical programming layer that would consume outputs from the Kawchak infrastructure.

### Shared Architectural Elements Across Chunks
The following technical components appear across multiple chunks and should be understood as a unified ecosystem when building a new paper:

| Component | Appears In |
|---|---|
| Model Context Protocol (MCP) | Chunks 01, 02, 03, 04 |
| Claude Code (Opus 4.6 / 4.7 Max) | Chunks 01, 02, 03, 04, 05 |
| Synthetic patient data (no PHI) | Chunks 01, 02, 03 |
| Python as primary language | Chunks 01, 02, 03, 04 |
| Zenodo open-access publishing | Chunks 01, 02, 05 |
| Regulatory compliance (ICH E6, 21 CFR, HIPAA, CDISC) | Chunks 01, 02, 03, 04 |
| Agentic iterative coding loop | Chunks 01, 02, 03, 04 |
| No clinical deployment as of May 2026 | Chunks 01, 02, 03, 04 |

### Citation-to-Section Mapping
| Chunk | Introduces Content | Primary BibTeX Key (chunk 05) |
|---|---|---|
| 01 | Executive Summary; Fully Automated Sponsor | `kawchak2026sponsor` [1] |
| 02 | Federated Learning Platform | `kawchak2026federated` [2] |
| 02 | Accelerated Patient Prediction | `kawchak2026prediction` [3] |
| 03 | ClinAgent | `yan2026clinagent` [4] |
| 04 | Industry Case Studies (supplementary) | `anthropic2026lifesciences` [5] |
| 04 | Synthesis, Table, Implications | All five references |
| 05 | All BibTeX entries | N/A (this IS the reference file) |

---

## Instructions for Claude Code Opus 4.7 Max

When using these five chunks to write a new physical AI oncology trial paper:

1. **Load all five chunks into context simultaneously.** They are designed to be read together; individual chunks are incomplete without the others.

2. **Use chunk 04's Comparative Overview table as the structural backbone** for any new comparative analysis or methods section you generate.

3. **Treat chunk 05's BibTeX entries as authoritative citations.** Do not infer or fabricate additional citation details; all DOIs and URLs are provided verbatim from the source.

4. **The three Kawchak papers (chunks 01 and 02) form the "Physical AI" infrastructure stack.** When writing about robotics integration, MCP architecture, federated data, or sponsor automation, draw primarily from these sections.

5. **ClinAgent (chunk 03) represents the statistical programming and regulatory submission layer.** When writing about CDISC compliance, TLF generation, or trial data analysis pipelines, draw primarily from this section.

6. **The Executive Summary in chunk 01 is the highest-density single-passage summary** of the entire document and is the best starting reference for establishing scope and context in a new paper's introduction.

7. **All projects are prototypes only** (confirmed in chunk 04). Any new paper must accurately represent this status and must not claim clinical deployment or regulatory approval for any of the cited systems.

8. **The MCP framework is the unifying technical thread** across all projects. A new paper should position MCP as the shared interoperability layer enabling Physical AI oncology trials.

9. **Hardware accessibility is a consistent finding.** The source document specifically emphasizes that even an Intel Core i5 with 4 GB RAM could execute the final models. This is a key translational point for new trial design proposals.

10. **Chunk 04's Implications paragraph** is the strongest existing statement of the convergence thesis and should be directly consulted when drafting a new paper's discussion or conclusion section.
