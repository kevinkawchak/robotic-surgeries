# README — Daraxonrasib PDAC Baseline Chunk Set
## For: Claude Code Opus 4.7 (1M context) — New Physical AI Oncology Trial Paper

**Source document:** research-1.docx  
**Baseline date of source:** May 12, 2026  
**Drug:** Daraxonrasib (RMC-6236) — investigational oral RAS(ON) multi-selective inhibitor  
**Sponsor:** Revolution Medicines  
**Disease:** Pancreatic ductal adenocarcinoma (PDAC)  
**Total chunks:** 5 markdown files + this README  
**Citation system:** Every evidence-bearing sentence in chunks 1–4 ends with a bracketed number [N]. All [N] values map sequentially to BibTeX entries in chunk 5. Do not infer URLs from body text; all URLs live exclusively inside BibTeX entries in chunk 5.

---

## File inventory and individual descriptions

### chunk_01_executive_rationale_chronology.md

**What it contains:** The document title block, scope statement, citation method note, medical and regulatory caveat, then three full sections of the source:

- **Section 1 — Executive baseline:** Eight sentences establishing the May 12, 2026 status snapshot. Contains the pivotal headline numbers: median OS 13.2 months vs. 6.7 months, hazard ratio 0.40, p < 0.0001 from the RASolute 302 Phase 3 intent-to-treat population. Cites refs [1]–[5].
- **Section 2 — Disease rationale and mechanism:** Six sentences covering the RAS mutation prevalence in PDAC (>90%), the RAS(ON) GTP-bound inhibition mechanism, the cyclophilin A tri-complex pharmacology, preclinical xenograft evidence, the 300 mg dose prediction, and the multi-selective breadth versus single-allele KRAS inhibitors. Cites refs [2], [4], [6], [7].
- **Section 3 — Development chronology and evidence map:** A 16-row chronological table spanning May 2022 through May 7, 2026, with each row containing a date, a specific event, and that event's baseline significance. Cites refs [1]–[4], [6], [8]–[18].

**Key numbers in this chunk:** OS HR 0.40, p < 0.0001, ITT mOS 13.2 vs. 6.7 months, 300 mg once-daily Phase 3 dose.

**Cross-file correlations for chunk 1:**
- The 16 events in the chronology table each have a corresponding detailed narrative in chunk 2 (individual trial histories) or chunk 3 (regulatory events and 2026 updates).
- The dose (300 mg) established in Section 2 reappears in every trial description in chunk 2, in the portfolio table in chunk 3, and in the RASolute 302 efficacy discussion throughout.
- Every citation number [N] in this chunk has a resolvable BibTeX entry in chunk 5; refs [1], [2], [4], [6] are particularly high-frequency anchors across all chunks.
- The scope statement in this chunk governs the evidentiary limits applicable to all other chunks: data only through May 12, 2026; no FDA approval as of that date.

---

### chunk_02_trial_by_trial_phase_history.md

**What it contains:** Section 4 of the source in full, covering five sequential subsections:

- **Section 4.1 — RMC-6236-001 (Phase 1/2 monotherapy foundation):** Twelve sentences. Covers trial design, ClinicalTrials.gov record (NCT05379985), eligibility criteria, ESMO 2023 data (111 patients, 65 PDAC, 20% ORR, 87% DCR), adverse event profile from ESMO, the NEJM Phase 1-2 publication data (168 PDAC patients, 96% any-grade TRAE, 30% grade ≥3), specific efficacy numbers in 26 second-line RAS G12 patients (ORR 35%, mDOR 8.2 mo, mPFS 8.5 mo, mOS 13.1 mo), and in 38 second-line broader RAS-mutant patients (ORR 29%, mDOR 8.2 mo, mPFS 8.1 mo, mOS 15.6 mo). Cites refs [4], [8], [9].
- **Section 4.2 — RMC-GI-102 (Phase 1/2 combination platform):** Ten sentences. Covers NCT06445062, AACR 2026 first-line PDAC combination cohort (40 patients, dara 200 mg + GnP, ORR 58%, 1 CR, 6-mo PFS 84%, 6-mo OS 90%, grade ≥3 AEs: anemia 33%, neutropenia 20%, fatigue 18%), and first-line monotherapy cohort (300 mg, ORR 47%, DCR 92%, 1 CR, 6-mo PFS 71%, 6-mo OS 83%, grade ≥3 TRAE 38%). Cites refs [18], [19].
- **Section 4.3 — RASolute 302 (Phase 3 previously treated metastatic PDAC):** Eleven sentences. Covers full trial design, 1:1 randomization, 500-patient enrollment, primary endpoints (PFS and OS by BICR in RAS G12 population), secondary endpoints, April 13 2026 topline positive readout, ITT OS result (13.2 vs. 6.7 months, HR 0.40), tolerability statement, finality declaration for PFS/OS, and pending ASCO 2026 Plenary presentation. Cites refs [1], [2], [10].
- **Section 4.4 — RASolute 303 (Phase 3 first-line metastatic pancreatic adenocarcinoma):** Five sentences. Covers three-arm design (dara vs. dara+GnP vs. GnP), NCT07491445, start date March 9 2026, 900-patient enrollment estimate, RAS-genotype-agnostic enrollment, and relationship to Phase 1/2 AACR data. Cites refs [17], [18], [20].
- **Section 4.5 — RASolute 304 (Phase 3 adjuvant/resected PDAC):** Six sentences. Covers two-arm design (dara vs. observation), NCT07252232, start December 15 2025, 500-patient enrollment, eligibility (R0/R1 resection, ECOG 0-1, RAS mutation documented), primary endpoint (investigator-assessed DFS), secondary endpoints (OS, BICR DFS, 1- and 2-year DFS/OS rates, safety, PK), and adjuvant strategic rationale. Cites refs [15], [21].

**Cross-file correlations for chunk 2:**
- Every trial in this chunk appears as a single-row summary in the portfolio table in chunk 3 (Section 5). Chunk 2 is the detailed narrative; chunk 3 is the synthesized lookup table.
- RMC-6236-001 (4.1) is the safety and dose-selection foundation that validates the 300 mg dose used in RASolute 302 (4.3) and described in chunk 1 (mechanism section).
- RMC-GI-102 combination data (4.2) is explicitly described as the clinical bridge supporting RASolute 303 (4.4), making these two subsections causally linked.
- The RASolute 302 efficacy outcome (4.3) is the central anchor of chunk 1's executive summary, chunk 3's regulatory events, and chunk 4's baseline interpretation guidance.
- RASolute 304 (4.5) eligibility criteria (R0/R1 resection, post-perioperative chemotherapy) define a PDAC population that does not overlap with the metastatic populations in 4.1–4.3, which is important for new trial design in the AI oncology paper.
- All [N] citations resolve to chunk 5; refs [4], [18], [10], [1] are the most critical for this chunk.

---

### chunk_03_portfolio_regulatory_2026updates.md

**What it contains:** Three sections:

- **Section 5 — Trial portfolio table:** A five-row summary table listing each trial (name, NCT number, setting/design, status/date markers with citations, and role in baseline). This is the quickest cross-reference lookup for all five active trials. Cites refs [1], [4], [8], [10], [18]–[21].
- **Section 6 — Regulatory status and access pathway:** Ten sentences covering FDA Breakthrough Therapy designation (June 23, 2025, for KRAS G12 previously treated metastatic PDAC), FDA Orphan Drug Designation (October 27, 2025), CNPV pilot selection (October 2025, non-transferable, 1–2 month intended review timeline), May 1 2026 expanded access safe-to-proceed letter (request April 28, signed April 30), physician-only request process, NDA intent statement (May 6, 2026), and EMA Orphan Drug Designation opinion. Cites refs [3], [12]–[14], [22]–[24].
- **Section 7 — 2026 updates and breakthroughs through May 12, 2026:** Nine sentences walking through each major 2026 milestone in chronological order: February 25 (enrollment complete), April 2 (RASolute 303 patients begin), April 13 (Phase 3 positive readout), April 21 ASCO announcement, April 21 AACR data, May 1 expanded access, May 6-7 NEJM publication, and the evidentiary status interpretation as of May 12. Cites refs [1]–[4], [16]–[18].

**Cross-file correlations for chunk 3:**
- The portfolio table (Section 5) is a direct condensation of the five subsections in chunk 2; every row maps 1:1 to a subsection in chunk 2 for full narrative detail.
- The regulatory designations in Section 6 are milestone entries also present in the chronology table in chunk 1 (Section 3): Breakthrough Therapy (June 2025), CNPV (October 2025), Orphan Drug (October 2025), expanded access (May 2026).
- Section 7's "2026 breakthroughs" section is a cross-cutting synthesis of events from the chronology table (chunk 1), the RASolute 302 trial narrative (chunk 2 Section 4.3), and the AACR first-line data (chunk 2 Section 4.2).
- The evidentiary status statement at the end of Section 7 — that PFS and OS are final but subgroup and safety details are pending ASCO — directly controls the guidance in chunk 4's baseline interpretation (Section 9).
- Regulatory anchor language in Section 6 is repeated and synthesized in chunk 4 Section 9's "main regulatory anchor" sentence.

---

### chunk_04_landscape_interpretation_conclusion.md

**What it contains:** Four sections:

- **Section 8 — External and adjacent RAS-targeted landscape:** Ten sentences covering competitive context. Sotorasib/CodeBreaK 100 PDAC (ORR 21%, G12C subset only). MRTX1133 (KRAS G12D, Phase 1/2, terminated due to formulation). Astellas setidegrasib/ASP3082 (KRAS G12D degrader, Phase 3 initiated April 2026, >600 patients, OS primary endpoint, double-blind placebo-controlled). Eli Lilly LY3962673/MOONRAY-01 (Phase 1a/1b, KRAS G12D, 630-patient estimate). Hengrui HRS-4642 (Phase 1, G12D, 102 patients, completed June 2024). Zoldonrasib/RMC-9805 (G12D-selective RAS(ON) inhibitor from Revolution Medicines, RASolute 305 in 1L G12D PDAC initiated February 2026). Cites refs [1], [2], [16], [25]–[29].
- **Section 9 — Baseline interpretation for downstream AI analysis:** Nine sentences providing explicit evidence-strength tiering: second-line PDAC (highest, completed Phase 3 + expanded access), first-line PDAC (moderate, Phase 1/2 + RASolute 303 active), adjuvant PDAC (early, RASolute 304 recruiting). Names the four anchors for AI analysis: efficacy anchor (HR 0.40 ITT OS), safety anchor (NEJM Phase 1-2 grade ≥3 TRAE ~30%), regulatory anchor (BTD + ODD + CNPV + expanded access, no approval), and competitive/market anchor (dara vs. allele-specific G12D agents). Names two primary risks: biological (acquired resistance, compensatory signaling) and clinical operations (eligibility, testing, logistics, payer). Cites refs [1], [3], [4], [6], [18], [21], [27].
- **Section 10 — Practical update checklist after May 12, 2026:** Six action items for updating this baseline: ASCO 2026 full RASolute 302 data, NDA CNPV submission tracking, expanded access process changes, RASolute 303 randomized results, RASolute 304 DFS/OS data, and competitive monitoring (setidegrasib, LY3962673, HRS-4642, zoldonrasib). Cites refs [2], [3], [20], [21], [24], [27].
- **Section 11 — Bottom-line conclusion:** Three sentences. Daraxonrasib is the most clinically advanced broad RAS(ON) PDAC candidate as of May 2026. The program spans a full Phase 3 continuum (metastatic 2L, metastatic 1L, adjuvant). The appropriate stance is optimistic but not complete pending ASCO data, NDA activity, approval, and earlier-line randomized results. Cites refs [1], [5], [24].

**Cross-file correlations for chunk 4:**
- Section 8's competitive landscape agents — sotorasib, MRTX1133, setidegrasib, LY3962673, HRS-4642, zoldonrasib — appear nowhere else in the chunks except in their BibTeX entries (refs [25]–[29] in chunk 5). This section is the only place in the five chunks where external agents are described in detail.
- Section 9's evidence-strength tiering (2L highest, 1L moderate, adjuvant early) directly synthesizes the trial-by-trial detail from chunk 2 and the regulatory milestones from chunk 3.
- The four anchors named in Section 9 are derived from: efficacy anchor → chunk 2 Section 4.3 + chunk 1 Section 1; safety anchor → chunk 2 Section 4.1 (NEJM data); regulatory anchor → chunk 3 Section 6; competitive anchor → chunk 4 Section 8 itself.
- Section 10's update checklist items correspond to specific trials and regulatory events documented in chunks 1–3, making it a forward-looking action list rooted in the factual baseline of the other chunks.
- The "main biological risk" in Section 9 (resistance, compensatory signaling) is rooted in the mechanism described in chunk 1 Section 2 (cyclophilin A tri-complex, RAS(ON) inhibition rationale, ref [6]).

---

### chunk_05_bibtex_references.md

**What it contains:** All 29 BibTeX entries in sequential citation-number order (References 1 through 29), preceded by the citation method preamble from the source document. Each entry uses a unique BibTeX key and contains author, title, year, howpublished or journal, and url fields. No inline citation numbers are embedded in the entries themselves, per the source document's design.

**Entry type breakdown:**
- `@article` entries (peer-reviewed journals): refs [4] (NEJM, Wolpin 2026), [6] (Cancer Discovery, Jiang 2024), [7] (J Med Chem, Cregg 2025), [25] (NEJM, Strickler 2023) — 4 entries
- `@misc` entries (press releases, trial records, regulatory documents): refs [1]–[3], [5], [8]–[24], [26]–[29] — 25 entries

**Individual entry significance for new trial paper:**
- **[1] revmed2026_rasolute302_topline** — Primary efficacy source; all OS and HR claims trace here.
- **[2] revmed2026_asco_rasolute302** — Source for trial design details, mutation enrollment criteria, endpoint definitions, and ASCO presentation notice.
- **[3] fda2026_expanded_access_daraxonrasib** — FDA regulatory source for expanded access; governs access pathway claims in chunk 3.
- **[4] wolpin2026_daraxonrasib_pretreated_pdac** — The NEJM peer-reviewed publication; primary source for Phase 1-2 safety, dose selection, ORR, DOR, PFS, OS in 2L PDAC. DOI: 10.1056/NEJMoa2505783.
- **[6] jiang2024_rmc6236_translational** — Cancer Discovery translational paper; primary source for mechanism, tri-complex pharmacology, preclinical xenograft data, dose prediction. DOI: 10.1158/2159-8290.CD-24-0027.
- **[7] cregg2025_discovery_daraxonrasib** — J Med Chem drug discovery paper; source for tri-complex and cyclophilin A mechanism claim. DOI: 10.1021/acs.jmedchem.4c02314.
- **[10] clinicaltrials2026_nct06625320** — ClinicalTrials.gov record for RASolute 302; authoritative source for enrollment number (500), start date, and completion estimates.
- **[12] revmed2025_breakthrough_therapy** — Source for Breakthrough Therapy designation date (June 23, 2025) and qualifying population (KRAS G12 mutations).
- **[18] revmed2026_aacr_firstline_data** — Source for all first-line Phase 1/2 combination and monotherapy data (ORR 58%, 47%; 6-mo PFS/OS metrics).
- **[27] astellas2026_setidegrasib_phase3** — Source for setidegrasib Phase 3 design, enrollment target, and OS primary endpoint; key competitive reference.

**Cross-file correlations for chunk 5:**
- Every [N] citation in chunks 1 through 4 resolves to the correspondingly numbered entry in chunk 5. The mapping is strictly sequential: [1] = first entry, [2] = second entry, through [29].
- The four `@article` peer-reviewed entries ([4], [6], [7], [25]) carry the highest evidentiary weight and should be treated as primary literature sources in a new oncology trial paper.
- Entries [8], [10], [19]–[21], [26], [28], [29] are ClinicalTrials.gov records providing trial design parameters, enrollment numbers, and completion timelines that appear in chunk 2's trial narratives and chunk 3's portfolio table.
- Entries [3], [12], [13], [14], [22] are FDA and regulatory sources that substantiate the regulatory pathway claims in chunk 3 Section 6.
- The ASCO and AACR press release entries ([2], [18]) are corporate communications; they are used as evidence for conference presentation dates and first-line data points but should be distinguished from peer-reviewed sources in a new paper's Methods and References.

---

## How all five chunked files correlate to each other

The five chunks represent a layered, mutually dependent knowledge structure. Reading them in order reveals a logical progression from rationale → evidence → synthesis → interpretation → sources.

**Logical flow across chunks:**

Chunk 1 establishes the drug's identity, the disease context, the molecular mechanism, the headline efficacy result (HR 0.40, mOS 13.2 vs. 6.7 months), and the full chronological event sequence. It is the entry point and highest-density summary layer.

Chunk 2 expands each trial referenced in the chronology table (chunk 1) into full narrative detail, providing patient numbers, specific efficacy metrics (ORR, DOR, PFS, OS), adverse event rates, eligibility criteria, and design parameters for all five trials (RMC-6236-001, RMC-GI-102, RASolute 302, 303, 304). Chunk 2 is the evidence layer.

Chunk 3 synthesizes chunk 2's five-trial detail into a single lookup table (Section 5) and then documents the regulatory milestones and access framework built on that evidence base (Section 6), followed by a chronological narrative of 2026 breakthroughs that links back to both chunk 1's timeline and chunk 2's trial-level data (Section 7). Chunk 3 is the synthesis and regulatory layer.

Chunk 4 applies the evidence from chunks 1–3 to four analytical tasks: competitive positioning (how daraxonrasib stands versus external agents not covered elsewhere), evidence-strength tiering for downstream AI use, a forward-looking update checklist, and a bottom-line conclusion. Chunk 4 is the interpretation and application layer.

Chunk 5 is the citation infrastructure that makes all factual claims in chunks 1–4 traceable and verifiable. Every [N] citation in any of the first four chunks maps to entry N in chunk 5. Chunk 5 also records URLs, DOIs, authors, and publication details that do not appear in the body text.

**Key data threads running through all five chunks:**

The 300 mg once-daily dose appears in chunk 1 (mechanism/dose prediction), chunk 2 (dose-selection narrative in 4.1, RASolute 302 dose in 4.3, first-line monotherapy dose in 4.2), chunk 3 (portfolio table), and resolves to citations in chunk 5 that trace to the NEJM publication and ClinicalTrials.gov records.

The OS hazard ratio of 0.40 and the ITT mOS values of 13.2 versus 6.7 months appear in chunk 1 (executive summary), chunk 2 (RASolute 302 narrative), chunk 3 (portfolio table, 2026 updates), chunk 4 (efficacy anchor in baseline interpretation), and resolve to ref [1] in chunk 5.

The NEJM Wolpin 2026 publication (ref [4]) provides data cited in chunk 1 (grade ≥3 TRAE in 30%, PDAC mutation prevalence), chunk 2 (all RMC-6236-001 efficacy and safety numbers), chunk 3 (portfolio table, May 7 2026 publication milestone), and chunk 4 (safety anchor). Its BibTeX entry in chunk 5 is the single most cited peer-reviewed source across the set.

The expanded access FDA action of May 1, 2026 (ref [3]) is referenced in chunk 1 (chronology row), chunk 3 (regulatory section and 2026 updates), and chunk 4 (regulatory anchor and operations risk) and resolves to the FDA news release in chunk 5.

---

## Guidance for new physical AI oncology trial paper

The intended use of this chunk set is as a reference-quality baseline for Claude Code Opus 4.7 (1M context) to assist in constructing a new clinical trial paper involving physical AI applications in oncology, with daraxonrasib in PDAC as the drug and disease context.

**Recommended processing approach:**

Load all five chunks simultaneously given the 1M context window. Chunk 5 should be treated as a live reference layer: any factual claim in a new Methods, Background, or Discussion section that originates from this baseline should be traceable to the appropriate [N] citation and confirmed against the corresponding BibTeX entry in chunk 5 before inclusion.

Chunk 4 Section 9 (baseline interpretation for downstream AI analysis) was written specifically to guide AI-assisted analysis and should be the first section read after the executive summary (chunk 1 Section 1) to understand the evidentiary confidence levels before constructing any new claims.

Chunk 2 Sections 4.1 and 4.3 contain the highest-density quantitative evidence (specific ORR, PFS, OS, AE rate numbers) and are the primary resources for populating any Results-adjacent or Background-efficacy sections in a new paper.

Chunk 3 Section 6 contains the complete regulatory status as of May 12, 2026, and is the authoritative source for any regulatory context statements in a new Introduction or Discussion section.

Chunk 4 Section 8 contains the competitive landscape and is the only place in the five chunks where non-daraxonrasib agents (sotorasib, setidegrasib, LY3962673, HRS-4642, zoldonrasib, MRTX1133) are described with their trial status and efficacy data. This section is essential for any comparative or positioning language in a new paper.

The update checklist in chunk 4 Section 10 defines the data that were explicitly pending as of May 12, 2026 (ASCO 2026 full Phase 3 data, NDA submission, RASolute 303 and 304 randomized results). Any new trial paper referencing post-May 12, 2026 data should annotate those updates separately and distinguish them from this baseline.

**Evidentiary hierarchy across the chunk set (from strongest to weakest):**

Tier 1 (peer-reviewed primary literature): refs [4], [6], [7], [25] — chunk 5 @article entries  
Tier 2 (FDA regulatory documents): refs [3], [13], [22] — chunk 5 FDA @misc entries  
Tier 3 (ClinicalTrials.gov records): refs [8], [10], [19]–[21], [26], [28], [29] — chunk 5 CT.gov @misc entries  
Tier 4 (sponsor press releases and corporate updates): refs [1], [2], [5], [9], [11], [12], [14]–[18], [23], [24], [27] — chunk 5 company @misc entries

For a peer-reviewed oncology trial paper, Tier 1 and Tier 2 sources should be cited directly; Tier 3 trial records support design and enrollment claims; Tier 4 corporate sources should be used only for sponsor statements and milestones not yet available in peer-reviewed form, and should be explicitly identified as company communications in the citations.
