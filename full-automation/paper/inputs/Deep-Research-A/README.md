# README — Chunked Source Document for Physical AI Oncology Trial Paper

**Prepared for:** Claude Code Opus 4.7 (1M context) Max  
**Source file:** `Deep-Research-A.docx`  
**Paper title:** Medical AI Applications with Full-Day Automation (2026)  
**Purpose:** This README and the three accompanying `.md` files constitute the complete, word-for-word content of the source document, split into logical chunks for downstream synthesis into a new physical AI oncology trial paper.

---

## File Inventory

| File | Contents | Role in source document |
|---|---|---|
| `chunk1_paper_text.md` | Full main body narrative | Title + all prose paragraphs + 5 case-study bullets + synthesis and oncology-relevance sections |
| `chunk2_tables_references.md` | Annotated inline citations (【1】–【6】) and hyperlinked footnotes | Structured reference list as it appears inline in the document, with anchor-text URLs |
| `chunk3_bibtex.md` | Six BibTeX entries | Machine-readable bibliography block appearing at the end of the source document |

---

## chunk1_paper_text.md — Detail

**What it contains:**  
The complete main body of the paper, preserved word for word, including:

- The opening framing paragraph establishing that 2026 healthcare projects used Claude Code with cron-style automation.
- Five bullet-point case studies, each a self-contained narrative:
  1. **CureCancerMagic** — patient coordination app; 10-ticket autonomous chain; auto-committed code across tickets with zero failures (cite key: `feld2026curecancermagic` / 【2】).
  2. **PostVisit.ai** — interventional cardiologist-built AI care platform; won 3rd among ~13,000 teams at Anthropic Feb 2026 hackathon; built in 7 days without conventional code (cite keys: `ship2026doctor` / 【3】, `zurbano2026postvisit` / 【4】).
  3. **ClinicalTrials.gov MCP server** — headless agent querying NIH trial registry; explicit recommendation to schedule nightly automated reports without human intervention (cite key: `vinkius2026clinicaltrials` / 【1】).
  4. **HL7→FHIR migration agent** — Claude Code translating hospital HL7 v2 messages to FHIR protocols; outputs pull requests; all patient data kept synthetic (cite key: `devdigest2026hl7` / 【6】).
  5. **Cloud Routines and scheduling** — April 2026 Anthropic feature enabling saved prompts to run nightly, weekly, or via API/GitHub event on Anthropic's servers even when user machine is offline; contrasted with session-bound /loop command (cite key: `anthropic2026routines` / 【5】).
- A synthesis paragraph linking all five cases under the theme of unattended, schedule-driven Claude Code agent workflows.
- A "Relevance to Automated Oncology Trials" closing section that explicitly connects each case to oncology trial operations (EHR polling, consent dashboards, symptom triage, HL7/FHIR data reconciliation).

**Key themes for oncology trial paper synthesis:**  
Autonomous multi-step pipelines; cron/scheduled headless execution; healthcare data integration (EHR, FHIR, HL7); zero-human-intervention code deployment; domain expert–driven rapid prototyping; 24/7 continuous agent operation.

**Cross-references to other chunks:**  
- Every in-text citation marker 【1】–【6】 resolves to a full annotated entry in `chunk2_tables_references.md` and to a BibTeX entry in `chunk3_bibtex.md`.
- The citation key mapping is: 【1】 → `vinkius2026clinicaltrials`, 【2】 → `feld2026curecancermagic`, 【3】 → `ship2026doctor`, 【4】 → `zurbano2026postvisit`, 【5】 → `anthropic2026routines`, 【6】 → `devdigest2026hl7`.

---

## chunk2_tables_references.md — Detail

**What it contains:**  
The structured reference section of the source document in two sub-sections:

1. **Annotated Inline Citations (【1】–【6】)** — Each entry gives the citation number, author/title in italics, publication venue, year, a parenthetical description of the content, and one or more hyperlink anchors with fragment identifiers pointing to specific quoted passages.
2. **Hyperlinked Footnotes** — Numbered markdown footnote-style links `[[1]]`–`[[5]]` with display titles and bare URLs, as they appear at the document's end.

**Note on "tables":** The source document contains no formal tabular data (no HTML or markdown tables, no spreadsheet-style rows/columns). This chunk therefore holds the closest equivalent structured content: the ordered, numbered reference list that in a traditional paper would accompany or follow the main text, analogous to a reference table.

**Key details for oncology paper use:**  
- Each annotated entry includes the line-range locators (e.g., 【1†L107-L110】) from the original source retrieval, useful for tracing exact quoted passages back to primary sources.
- URLs are complete and can be resolved to verify currency of each source as of 2026.
- Footnote [[1]] (The Hidden Power of Claude Scheduled Tasks for Data Scientists, thedatawriter.substack.com) does not have a corresponding BibTeX entry in chunk3; it appears only as a contextual footnote in the prose of chunk1.

**Cross-references to other chunks:**  
- Citation numbers 【1】–【6】 here correspond directly to in-text markers in `chunk1_paper_text.md`.
- All six numbered annotations (【1】–【6】) have matching BibTeX entries in `chunk3_bibtex.md`; use the author–year key (e.g., `vinkius2026clinicaltrials`) to match them.
- Footnote [[1]] (substack.com URL) has no BibTeX counterpart in chunk3.

---

## chunk3_bibtex.md — Detail

**What it contains:**  
Six BibTeX entries exactly as they appear in the source document, wrapped in a fenced code block for syntax preservation. Entry types and keys:

| BibTeX key | Entry type | Author | Year | Venue |
|---|---|---|---|---|
| `vinkius2026clinicaltrials` | @misc | Vinkius | 2026 | Vinkius website |
| `feld2026curecancermagic` | @misc | Feld, Brad | 2026 | Blog (adventuresinclaude.ai) |
| `ship2026doctor` | @article | Ship X/TechX | 2026 | TechX (Medium) |
| `zurbano2026postvisit` | @misc | Zurbano, Jeffrey Loren | 2026 | LinkedIn post |
| `anthropic2026routines` | @misc | Anthropic | 2026 | Claude Code Documentation |
| `devdigest2026hl7` | @article | Developers Digest | 2026 | Developers Digest |

**Key details for oncology paper use:**  
- All six entries are gray literature (blog posts, documentation, social media, and trade publications) — no peer-reviewed journal articles are present in the source. The new oncology trial paper will need to supplement these with peer-reviewed clinical and AI/ML literature.
- All entries are dated 2026 and thus represent the current state-of-the-art baseline as of the source document's publication date.
- The `url` field is populated for all six entries; no `doi` fields are present.
- Entry types @misc and @article are used; @misc is used for web/documentation/social sources, @article for Medium/trade-journal-style publications.

**Cross-references to other chunks:**  
- Each key maps back to a 【N】 citation marker in `chunk1_paper_text.md` and to an annotated entry in `chunk2_tables_references.md` (see the citation key mapping table in the chunk1 section above).

---

## How All Three Chunks Relate to Each Other

```
chunk1_paper_text.md          chunk2_tables_references.md       chunk3_bibtex.md
─────────────────────         ───────────────────────────       ────────────────
Main narrative body      ←→   Annotated inline ref list    ←→   BibTeX entries
【1】–【6】 in-text        →   【1】–【6】 full annotations   →   @key entries
Case study prose         ←    Passage locators (†L lines)        Machine-readable
Oncology synthesis       ←    URL verification                   bibliography
```

- **chunk1 → chunk2:** Every 【N】 marker in chunk1 prose resolves to a full annotated entry in chunk2, providing author, title, venue, description, and URL.
- **chunk2 → chunk3:** Each annotated entry in chunk2 has a corresponding BibTeX key in chunk3 for citation management and formatted bibliography generation.
- **chunk1 → chunk3:** Direct key-to-citation-number mapping allows any BibTeX key to be placed inline in new paper drafts to replace 【N】 markers.
- **chunk2 only:** Footnote [[1]] (substack.com) appears in chunk2's hyperlinked footnotes section but has no BibTeX counterpart in chunk3 — it is a supplementary contextual link, not a formal citation.

---

## Instructions for Claude Code Opus 4.7 Max

When using these files to assist in drafting a new physical AI oncology trial paper:

1. **Treat chunk1 as the primary content source.** All case-study narratives, thematic arguments, and the oncology-relevance framing are here. Synthesize from this when constructing new paper sections on AI agent workflows, scheduling, and healthcare automation.

2. **Use chunk2 to verify and expand citations.** Before citing any 【N】 marker from chunk1 in the new paper, resolve it against chunk2 to confirm the source title, author, venue, and URL. The passage locators (e.g., 【1†L107-L110】) indicate the specific lines within each source that support the cited claim.

3. **Use chunk3 to generate the new paper's bibliography.** The six BibTeX entries are ready to import. Since all sources are 2026 gray literature, plan to supplement with peer-reviewed oncology and AI literature for the new trial paper. The new paper's bibliography should clearly distinguish between these foundational 2026 AI deployment examples (from chunk3) and any clinical evidence literature added during drafting.

4. **Citation key mapping (quick reference):**
   - 【1】 = `vinkius2026clinicaltrials` (ClinicalTrials.gov MCP, scheduled headless queries)
   - 【2】 = `feld2026curecancermagic` (CureCancerMagic, autonomous ticket chain)
   - 【3】 = `ship2026doctor` (PostVisit.ai, hackathon win)
   - 【4】 = `zurbano2026postvisit` (PostVisit.ai, LinkedIn description)
   - 【5】 = `anthropic2026routines` (Claude Code Routines feature, official docs)
   - 【6】 = `devdigest2026hl7` (HL7→FHIR migration agent)

5. **No tables exist in the source.** chunk2 holds structured reference content only. If the new oncology trial paper requires data tables (patient demographics, outcome metrics, trial arms, etc.), these must be created fresh from new trial data — nothing in these three chunks provides tabular clinical data.

6. **Oncology-specific bridging point:** The closing section of chunk1 ("Relevance to Automated Oncology Trials") is the direct conceptual bridge from the source document to the new paper's subject matter. Use it as a scaffolding outline: each function named there (EHR polling, consent dashboards, symptom triage, FHIR reconciliation) represents a candidate section or workflow component in the new trial paper.
