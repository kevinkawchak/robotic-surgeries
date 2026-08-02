# Project Plan — Phase 1, First-in-Human PDAC Trial of an LLM-Advised Robotic Whipple with Perioperative Daraxonrasib (RMC-6236)

**Program:** ChemicalQDevice / Kawchak, K.
**Plan version:** 1.0 · **Date:** August 1, 2026
**Parent protocol:** *A Phase 1, First-in-Human, Combined IND/IDE Clinical Trial Protocol of On-Premises LLM-Directed Robotic Pancreaticoduodenectomy with Perioperative Daraxonrasib (RMC-6236) in KRAS-Mutated PDAC* — [10.5281/zenodo.20780121](https://doi.org/10.5281/zenodo.20780121) (final protocol, `trial-protocol/final-protocol/publication/`)
**Companion works:** Patient Robot Advocacy ([21720120](https://doi.org/10.5281/zenodo.21720120)) · IND draft ([21097442](https://doi.org/10.5281/zenodo.21097442)) · Funding Application v2.0, RFA-RM-27-001 ([21317266](https://doi.org/10.5281/zenodo.21317266)) · Phase 2 protocol ([20807027](https://doi.org/10.5281/zenodo.20807027))

> **Disclaimer.** This is an independent research and program-planning document. It is not medical, legal, or regulatory advice; it is not an active IND or IDE; and it is not endorsed by the FDA, NIH, HHS, CMS, an IRB, ICH, Revolution Medicines, Intuitive Surgical, Medtronic, or any clinical site. Every regulatory pathway, standard version, funding term, and contact named here must be verified against the live source before use. Dollar figures and durations are planning estimates, not quotations.

---

## 0. Executive summary

The protocol is complete as a *document*. It is not yet executable as a *program*. The gap is not writing — it is that the protocol presumes an investigational device that does not exist, a drug the sponsor does not control, a nonclinical package that has not been generated, and a funding envelope roughly five to seven times larger than the award the program has been targeting.

This plan converts the protocol into an executable program by doing four things:

1. **Resolving the device question first** (§3). The protocol's eight-arm, 56-DOF, 640-channel, 1,200 mm/s platform is a simulation construct derived from the author's 2030 PancreSpeed modeling work. No such device is manufactured, and building one is a $150M+, 8–10-year medical-device program on its own. The recommended scope is **Option B: keep the LLM advisory layer as the investigational device and run it as a non-actuating overlay on an already-cleared surgical robot.** This preserves the entire scientific claim of the program — that a verified, on-premises LLM can improve a Whipple under human authority — while making the IDE achievable in ~2 years instead of ~9.
2. **Sequencing the regulatory work correctly** (§5). Two applications, one protocol: an IDE to CDRH for the advisory device and a sponsor-investigator IND to CDER for perioperative daraxonrasib, preceded by a Pre-RFD for jurisdiction, a Q-Submission for the device, and a Type B pre-IND for the drug. The IND is not viable without a Letter of Authorization from Revolution Medicines — that is the program's single hardest external dependency and it belongs at the front, not the middle.
3. **Building the nonclinical package the protocol currently omits** (§6). The protocol gates first-in-human use on simulation alone (≥1000 runs, ≥2 frameworks, USL ≥7.0). FDA will not accept simulation alone for a first-in-human surgical system. The plan adds bench verification with tolerance intervals, ≥10 cadaveric pancreaticoduodenectomies, and a GLP porcine survival study — the conventional evidence spine, with the simulation campaign layered on top of it rather than in place of it.
4. **Fixing four design confounds before they reach the FDA** (§7.2). The most serious is that dose level is perfectly confounded with operative case order: every DL1 participant is also one of the first three cases ever performed. The fix is a device-only lead-in cohort (Cohort 0) plus prespecified CUSUM learning-curve analysis.

**Program shape at a glance**

| | |
|:--|:--|
| Recommended scope | LLM advisory device (Option B) + perioperative daraxonrasib |
| Regulatory | IDE (CDRH, significant risk) + sponsor-investigator IND (CDER), single protocol |
| Nonclinical | Bench + cadaver (n≥10) + GLP porcine survival (n≥16) + Phase 0 simulation |
| Clinical | n = 3 (Cohort 0, device only) + up to 18 (3+3, DL1–DL3) = **up to 21 treated** |
| Sites | 1 high-volume academic HPB center (2 surgeons credentialed) |
| Time to first patient | **~30 months** from program start |
| Time to RP2D + feasibility readout | **~52 months** |
| Time to final CSR (24-mo OS) | **~75 months** |
| Total program cost | **$21M – $28M** (Option B); Pioneer award at $3.5M covers ~14% |
| Hard gates | 9 (G0–G8), four of them kill-capable |

---

## 1. What "success" means

The program is not successful because the operation is fast. Define success explicitly, in advance, because it governs every downstream trade-off.

**Primary definition of success (program-level):**

> An IDE-approved, IND-cleared, IRB-approved Phase 1 study completes accrual at a single center with no device-attributable death and no unrecovered breach of the cyber-physical safety envelope; a daraxonrasib RP2D is declared; device feasibility is demonstrated at the prespecified task-completion threshold; and the FDA accepts a Phase 2 briefing package.

**Success criteria and thresholds**

| # | Criterion | Threshold | Source |
|:--|:--|:--|:--|
| S1 | Regulatory | IDE approved and IND safe-to-proceed without clinical hold | §5 |
| S2 | Device safety | 0 device-attributable deaths; 0 uncontained no-fly breaches; all E-stops within latency spec | Protocol §7.1, §9.4.6 |
| S3 | Drug safety | MTD/RP2D declared with <2/6 DLTs at the selected level | Protocol §4.3 |
| S4 | Feasibility | ≥80% of procedures complete all assigned tasks without conversion attributable to device malfunction | Protocol §3.1 |
| S5 | Oncologic non-degradation | R0 rate, ISGPS B/C fistula, Clavien-Dindo III+, 90-day mortality all with exact 95% CIs whose point estimates do not exceed the Dutch 2025 benchmarks (24.4%, 41.3%, 3.9% at 30d) | Protocol §3.2 |
| S6 | Advisory integrity | ≥95% concordance between LLM advisory output and the independent hard-coded safety gate; 0 instances of an advisory reaching an actuator without gate clearance | Protocol §3.3 |
| S7 | Evidentiary | 100% of procedures replayable from deterministic seed + repository commit; audit chain intact under Part 11 | Protocol §10.9 |
| S8 | Participant-facing | Every one of the seven Patient Robot Advocacy commitments verifiably met and independently checkable | Advocacy paper |
| S9 | Program | Phase 2 protocol ([20807027](https://doi.org/10.5281/zenodo.20807027)) accepted at a Type C or End-of-Phase-1 meeting | §5.6 |

**Explicit non-goals.** Procedure-time reduction is *not* an endpoint of this trial and must not be presented as one. The 60-second Whipple figure from the 2030 simulation work ([20196639](https://doi.org/10.5281/zenodo.20196639)) is a modeling artifact of a hypothetical platform; introducing it into a first-in-human context invites the reviewer to conclude the sponsor has confused simulation with clinical evidence. Keep it out of the IND, the IDE, the consent form, and every site-facing document.

---

## 2. Feasibility triage — nine findings that determine whether this program can run

These are ordered by how early they can kill the program. Each carries a required action and an owner.

| # | Finding | Severity | Required action | Gate |
|:--|:--|:--|:--|:--|
| **F1** | **The eight-arm platform does not exist.** The 56-DOF / 640-channel / 1,200 mm/s / ≤3 ms cross-arm E-stop specification originates in the author's 2030 PancreSpeed 1.0 simulation. There is no manufacturer, model number, software version, or FDA-cleared configuration to place on an IDE. | **Critical** | Execute the scope decision in §3. Replace every occurrence of the hypothetical platform in submission-facing documents with a named, identifiable system. | G0 |
| **F2** | **The sponsor does not control the drug.** A sponsor-investigator IND for daraxonrasib requires either a full CMC/nonclinical package or a Letter of Authorization from Revolution Medicines permitting FDA to cross-reference their files. | **Critical** | Open the RevMed channel in week 1 (§4 WS-2). Secure LOA + Investigator's Brochure + supply agreement + medical-monitor terms. | G1 |
| **F3** | **"First-in-human" is wrong for the drug.** Daraxonrasib is in Phase 3 (RASolute 302, RASolve 301) with Breakthrough Therapy designation. Calling it first-in-human is a factual error that will cost credibility with FDA, RevMed, and any site. | High | Retitle: *first prospective evaluation of the integrated LLM-advised surgical workflow, and first evaluation of daraxonrasib in a perioperative curative-intent setting.* The FIH claim attaches to the **device and the perioperative schedule**, not the molecule. | G0 |
| **F4** | **"LLM-Directed" contradicts the protocol body.** The title says directed; §6.1.1 says the LLM is "a second-opinion advisory oracle held strictly outside the robot vendor kinematic stack, never as an autonomous controller." A reviewer who reads only the title assumes an autonomous surgical AI. | High | Adopt **"LLM-advised"** program-wide — the term already used in Funding Application v2.0. Retitle the protocol at the next amendment. | G0 |
| **F5** | **Simulation-only nonclinical gating is insufficient.** Protocol §4.3 gates FIH on ≥1000 sims across ≥2 frameworks and USL ≥7.0. FDA expects bench V&V, cadaveric, and GLP animal survival data for a first-in-human surgical system. | **Critical** | Build the full nonclinical spine (§6). Keep Phase 0 simulation as an *additional* gate, not a substitute. | G4 |
| **F6** | **Dose level is confounded with the surgical learning curve.** Under 3+3 with sentinel staggering, DL1 participants are by construction cases 1–3 (or 1–6). Any dose-response signal is inseparable from operator experience. | High | Add **Cohort 0** (device-only lead-in, n=3, no investigational perioperative drug schedule) and prespecify CUSUM learning-curve analysis with case order as a covariate (§7.2). | G5 |
| **F7** | **The Physical AI opt-out is not operationally defined.** If the advisory layer *is* the investigational device, a participant who opts out contributes no device data yet is still exposed to surgery. The protocol says opt-out does not affect eligibility but does not say what happens to the analysis populations or the 3+3 count. | High | Specify: opted-out participants remain in Safety and DLT-evaluable populations, are excluded from Device-Evaluable, are replaced for the feasibility endpoint, and are told this in the consent form (§7.4). | G5 |
| **F8** | **Sponsor-investigator conflict of interest is structural.** The Sponsor-Investigator is CEO of the entity developing the device under study and would also chair the program. §10.11 discloses this; disclosure alone will not satisfy an academic IRB or a COI committee for an FIH device trial. | High | Transfer safety and escalation authority to bodies with no financial interest: independent DSMB chair, independent medical monitor, an ISM with stop authority, and an institutional COI management plan filed before IRB submission (§9.3). | G5 |
| **F9** | **The award does not fund the trial.** NIH Director's Pioneer Award at ~$700K direct/yr × 5 yr ≈ $3.5M. Realistic Option B program cost is $21–28M. Pioneer also requires 51% effort in years 1–3. | High | Adopt the stacked funding architecture in §12. Treat Pioneer as the scientific-leadership anchor, not the trial budget. Resolve the effort commitment as an explicit go/no-go. | G0 |

---

## 3. Scope decision — the device question

Everything downstream depends on this. Decide it in the first 60 days.

### 3.1 The three options

| | **Option A — Build the 8-arm platform** | **Option B — Advisory overlay on a cleared robot** *(recommended)* | **Option C — Software-only, no robot** |
|:--|:--|:--|:--|
| Investigational device | Novel 8-arm parallel coelomic platform | The on-premises LLM advisory system (SaMD) + its safety-gate module | Advisory system used for planning/rehearsal only, not intraoperatively |
| Surgical platform | Must be designed, built, verified | Commercially available, FDA-cleared multi-port robot used within its cleared indication | Conventional or robotic surgery, unchanged |
| Regulatory | IDE for a Class II/III novel surgical robot; full 60601 / 80601-2-77 / 14971 / 62304 / 10993 program | IDE for significant-risk SaMD with intraoperative display; 62304 / 14971 / 62366 / cybersecurity / PCCP | Possibly non-significant-risk; may qualify for abbreviated IDE |
| Nonclinical burden | Full electromechanical V&V, sterilization, biocompatibility, EMC, animal, cadaver | Bench + cadaver + GLP porcine for the *advisory workflow*; robot itself already cleared | Bench + simulation; no animal |
| Time to FIH | 8–10 years | **~30 months** | ~18 months |
| Cost | $150M+ | **$21–28M** | $6–9M |
| Preserves the scientific claim? | Yes | **Yes** — the claim is about verified LLM advice under human authority, not about arm count | Partially — loses the intraoperative claim entirely |
| Feasible for this sponsor | No | **Yes** | Yes, but scientifically thin |

### 3.2 Recommendation — Option B

**Adopt Option B.** The intellectual contribution of this program is the *assurance architecture*: verification-before-generation, the hard-coded independent safety gate with final authority, deterministic replay from seed and commit, the ten-gate VVUQ suite, the tiered telemetry pyramid, and the participant-facing opt-out. None of that requires eight arms. All of it is testable on a cleared platform, and testing it there is *stronger* evidence, because the surgical variable is held constant and the advisory layer is the only thing under investigation.

**Concretely, under Option B:**

- The surgical robot is a commercially available, FDA-cleared multi-port system, used strictly within its cleared indication and per its labeling, operated by a credentialed surgeon. It is **not** an investigational device in this study.
- The **investigational device** is the on-premises LLM advisory system together with the independent safety-gate module and the intraoperative display. It is **non-actuating by architecture** — it has no electrical or software path to any actuator. This is not a policy, it is a wiring constraint, and it must be demonstrable by design review and by a physical air-gap test in the V&V protocol.
- Sensor data reaches the advisory system through a read-only tap. Vascular proximity gating, force-envelope monitoring, and E-stop advisory alerts are computed on this tap and surfaced to the surgeon; the surgeon acts.
- Where the protocol's hard caps (≤3 N per arm, ≤18 N cumulative, ≤3 ms cross-arm E-stop, 100 µs watchdog) exceed what the cleared robot natively enforces, they become **monitored-and-alerted thresholds** rather than enforced clamps. State this transparently in the IDE. Do not claim enforcement the hardware cannot deliver.
- The eight operative phases (P1–P8), the three anastomoses with their ring-tension bands, and the five-vessel no-fly geometry survive as **advisory context and analysis structure**, which is where their evidentiary value actually lies.

**What is lost, stated plainly:** the closed-loop force clamping and the ≤3 ms cross-arm halt. Those are properties of a platform that does not exist. Nothing verifiable is lost, because nothing about them has ever been measured on hardware.

**Retain Option A as the Phase 3+/platform roadmap**, funded separately, informed by the Phase 1 telemetry. Say so explicitly in the funding narrative — it converts an unbuildable claim into a credible long-horizon vision.

---

## 4. Program architecture — eleven workstreams

Each workstream has an objective, a named owner role, key deliverables, upstream dependencies, and an exit criterion tied to a gate.

### WS-1 · Regulatory Strategy & Submissions
**Owner:** Regulatory Lead (contract, device+drug dual-competent) · **Exit:** G5
Own the Pre-RFD, Q-Sub, pre-IND, IDE, IND, and all subsequent amendments and safety reports. Maintain the regulatory correspondence file and the single source of truth for which claims are supportable. Detailed sequence in §5.

**Deliverables:** Pre-RFD package · Q-Sub briefing book + meeting minutes · Type B pre-IND briefing book + minutes · IDE application · IND (Form 1571/1572/3674) · Investigator's Brochure incorporation · annual reports · IND/IDE safety reports · End-of-Phase-1 briefing package.

### WS-2 · Drug Access & Industry Partnership
**Owner:** Sponsor-Investigator + BD advisor · **Exit:** G1 (hard gate)
Secure daraxonrasib. Without this, there is no drug arm. Follow the outreach sequence already drafted in `funding/potential-partners/UC-San-Diego/priority-steps.md`.

**Deliverables:** Non-confidential one-pager + 2-page synopsis (send these first, never the full LaTeX package) · CDA · scientific feasibility meeting · **Letter of Authorization for FDA cross-reference** · current Investigator's Brochure · drug supply agreement with quantities, labeling, shipping, accountability, and destruction terms · pharmacovigilance/SUSAR reciprocity agreement · medical-monitor arrangement · written assessment of overlap with RASolute 304 and other company-sponsored studies.

**Contingency if RevMed declines:** (a) re-approach after the next External Sponsored Research window opens; (b) if daraxonrasib reaches approval during the program, pivot to an IND for the new perioperative use of an approved drug — still an IND, but CMC burden collapses; (c) as a last resort, substitute a KRAS-targeted agent whose sponsor will partner, accepting that the RASolute anchoring in §4.3 must be rebuilt.

### WS-3 · Device Engineering & Design Controls
**Owner:** Head of Engineering / Quality · **Exit:** G2 (design freeze), G4 (V&V complete)
Stand up a real quality system and produce a real Design History File for the advisory device.

**Deliverables:** ISO 13485-aligned QMS (FDA QMSR-aligned) · Design & Development Plan · design inputs/outputs traceability matrix · ISO 14971 risk management file with hazard analysis covering AI-specific hazards (hallucinated advisory, stale context, silent degradation, adversarial input, automation bias) · IEC 62304 software lifecycle at Class C · IEC 62366-1 usability engineering file + summative human-factors validation · cybersecurity: threat model, SBOM, §524B documentation, penetration test report · read-only-tap and non-actuation architecture proof · design freeze + DHF · Predetermined Change Control Plan (PCCP) for model and prompt updates.

### WS-4 · LLM Advisory System & VVUQ
**Owner:** AI Assurance Lead · **Exit:** G4
Make the advisory layer defensible. This is the program's differentiator and its highest-scrutiny component.

**Deliverables:** model card (weights, version, quantization, inference stack, hash) · **locked model** — no online learning, temperature 0, fixed seed, air-gapped inference · constrained output schema (enumerated advisory types, never free text, never coordinates that could be executed) · verification-before-generation gate surface with accept/block/escalate semantics and per-decision logging · the ten-gate VVUQ suite bound to named consensus standards, with verification fraction, validation agreement, relative error, and CoV bounds reported per gate · adversarial and out-of-distribution test battery · degradation detection with the §8.3.6 trigger (three consecutive procedures or 24 cumulative hours below acceptance criteria) · TRIPOD+AI and CREMLS reporting artifacts · deterministic replay harness (seed + commit → byte-identical decision trace).

**Non-negotiable design rules.** (1) The hard-coded safety gate is independent of the LLM, is separately verified, and has final authority — an advisory that the gate blocks is never displayed as actionable. (2) No advisory output is ever electrically capable of reaching an actuator. (3) Every advisory is logged with its full input context before it is displayed, not after.

### WS-5 · Nonclinical Evidence
**Owner:** Preclinical Lead · **Exit:** G4 (hard gate)
See §6 for the full plan. Bench → cadaver → GLP porcine survival → Phase 0 simulation.

### WS-6 · Clinical Site, IRB & Governance
**Owner:** Clinical Operations Lead · **Exit:** G5, G6
**Deliverables:** site selection and qualification visit reports · clinical trial agreement · IRB submission and approval (single IRB) · COI management plan · DSMB charter + member recruitment and contracts · Independent Safety Monitor appointments · Physical AI Safety Review Committee charter (≤90-day cadence) · delegation-of-authority log · site initiation visit · clinical trial liability insurance and subject-injury compensation terms · CMS IDE study approval submission if Medicare coverage of routine costs is sought (novel FIH device is expected to be **Category A**; the device itself will not be covered).

### WS-7 · Data Systems, Part 11 & Telemetry
**Owner:** Data Engineering Lead · **Exit:** G5
**Deliverables:** validated EDC with Part 11 audit trails, e-signatures, RBAC · hash-chained append-only audit ledger binding the seven Physical AI record types (§10.9) · tiered telemetry pyramid (L0 raw lossless → compressed feature/event streams → summaries) with sizing and cost model · the −24 h / +72 h preservation routine around any reportable Physical AI event · HIPAA Safe Harbor de-identification pipeline (all 18 identifiers) · deny-by-default authorization · Zenodo controlled-access deposition workflow for the L0 tier · disaster recovery and retention through the §312.57 period · **computer system validation package** (IQ/OQ/PQ) — this is routinely underestimated and is a common audit finding.

### WS-8 · Biostatistics & Analysis
**Owner:** Trial Statistician · **Exit:** G5, G8
**Deliverables:** Statistical Analysis Plan (prespecified before FPI) · estimands for every endpoint per ICH E9(R1), with explicit intercurrent-event strategies for open conversion, opt-out, withdrawal, and death · 3+3 operating-characteristic simulation report · CUSUM learning-curve analysis specification · exact (Clopper–Pearson) interval conventions · DSMB reporting templates and cohort dossiers · validated, version-controlled, seed-fixed analysis environment · blinded independent attribution charter separating drug-attributable from device/procedure-attributable events.

### WS-9 · Surgical Training, Credentialing & Human Factors
**Owner:** Surgical Lead · **Exit:** G6
This workstream is where FIH surgical trials most often fail, and it is thin in the current protocol.
**Deliverables:** operator credentialing standard — minimum institutional and per-surgeon robotic Whipple volume, documented against published learning-curve evidence · simulator curriculum on the advisory system · ≥20 cadaveric and ≥10 porcine cases per credentialed surgeon before first patient · backup-operator qualification and handoff drills (≤2 s handoff) · full-team dry runs including E-stop, conversion-to-open, and advisory-failure scenarios · **automation-bias countermeasures** — display design, mandatory acknowledgment semantics, and a periodic assessment of whether surgeons are over-relying on the advisory · conversion-to-open drill logs · human-factors summative validation feeding WS-3.

### WS-10 · Participant Advocacy, Consent & Community
**Owner:** Participant Advocacy Lead (independent of the surgical team) · **Exit:** G5, ongoing
Operationalize the seven commitments from the Patient Robot Advocacy paper so each is *checkable by the participant*, which is the paper's own standard.
**Deliverables:** plain-language protocol summary written to be read *before* the consent conversation · consent form with a distinct, separately-initialed Physical AI disclosure and opt-out section · explicit therapeutic-misconception language · a **Patient Advisory Board** (≥3 members: PDAC survivor/caregiver, patient-safety advocate, community representative) convened before IRB submission and consulted at every amendment · translated materials and qualified interpreters · a participant-facing one-page "what the study owes you" card mapping each of the seven commitments to the protocol clause that makes it enforceable · re-consent workflow triggered by any change to the advisory system's risk profile · independent consent monitor for the first three participants and any participant flagged as vulnerable.

### WS-11 · Program Management, Funding & Dissemination
**Owner:** Program Director · **Exit:** continuous
**Deliverables:** integrated master schedule with the G0–G8 gates · risk register (§14) reviewed monthly · funding architecture and submission calendar (§12) · monthly gate reports · publication plan with dual GitHub + Zenodo deposition under CC BY 4.0 · ClinicalTrials.gov registration before first participant and results reporting within statutory windows · the LLM-driven documentation pipeline (mermaid → draft → full → final) applied to protocol amendments, cohort dossiers, and the CSR, per [21018646](https://doi.org/10.5281/zenodo.21018646) — with the standing caveat from that paper that only preparation time compresses; regulatory review clocks and clinical follow-up do not.

---

## 5. Regulatory strategy & submission sequence

### 5.1 Two applications, one protocol

The drug and the device are **not** physically or chemically combined and are not co-packaged or cross-labeled. They are two investigational articles used under one protocol. The likely correct structure is therefore a **concurrent IDE (CDRH) and sponsor-investigator IND (CDER)** — not a single combination-product application. The protocol's phrase "combined IND/IDE" is accurate as a description of the *study*, not of a single submission.

**Do not assume this.** File a **Pre-RFD** with the Office of Combination Products early: it is free, informal, and typically far faster than a formal Request for Designation under 21 CFR Part 3. Getting jurisdiction and lead-center wrong is a six-to-twelve-month error.

### 5.2 The clinical decision support question

Section 520(o)(1)(E) of the FD&C Act excludes certain CDS software from the device definition. The exclusion requires, among other things, that the clinician be able to **independently review the basis** for the recommendation. In a time-critical intraoperative context, a surgeon cannot meaningfully re-derive an LLM's reasoning mid-dissection. **Plan on the advisory system being a regulated device.** Argue the opposite only if FDA raises it, and never build a schedule that depends on the carve-out applying.

### 5.3 Submission sequence

| Seq | Submission | To | Timing | Purpose |
|:--|:--|:--|:--|:--|
| R1 | **Pre-RFD** | OCP | M3 | Jurisdiction and lead center; confirm concurrent IND+IDE structure |
| R2 | **Q-Submission (Pre-Sub)** | CDRH | M6 | Device classification, SR determination, nonclinical test plan adequacy, AI/PCCP approach, human-factors plan, endpoint acceptability |
| R3 | **Type B pre-IND meeting** | CDER | M9 | Perioperative schedule, DLT definition and attribution, 3+3 adequacy, LOA sufficiency, safety reporting for a surgical population |
| R4 | **Q-Sub follow-up** | CDRH | M15 | Close out feedback from R2; agree final V&V and animal protocols before executing them |
| R5 | **IDE application** | CDRH | M22 | 30-day FDA review; concurrent IRB review |
| R6 | **IND submission** | CDER | M24 | 30-day safe-to-proceed clock |
| R7 | **IRB submission** | sIRB | M23 | Parallel with R5/R6; IRB must approve the SR device determination |
| R8 | **ClinicalTrials.gov registration** | NIH | before FPI | Interventional; drug component Phase 1; device component Phase N/A; Primary Purpose: Device Feasibility + dose-finding |
| R9 | **CMS IDE study approval** | CMS | M24 | If Medicare coverage of routine costs is sought; expect Category A |
| R10 | **Annual reports / safety reports** | both | ongoing | §312.32/§312.33; §812.150; 7-day and 15-day expedited timelines; the six Physical AI triggers of §8.3.6 |
| R11 | **End-of-Phase-1 / Type C meeting** | both | M54 | Phase 2 alignment; autonomy-graduation discussion |

### 5.4 Questions to put to FDA in writing (draft these now)

At Q-Sub (R2):
1. Does the Agency agree the advisory system is the investigational device and the cleared surgical robot, used within its cleared indication, is not?
2. Does the Agency agree the proposed nonclinical package (bench + cadaver n≥10 + GLP porcine survival n≥16 + Phase 0 simulation) is adequate to support FIH?
3. Is the proposed PCCP scope for model, prompt, and threshold updates acceptable, and what triggers a new IDE supplement versus falling inside the PCCP?
4. Does the Agency agree the non-actuating architecture (read-only tap, no actuator path) is an acceptable risk control, and what evidence demonstrates it?
5. Is the task-completion feasibility endpoint acceptable as proposed, and is ≥80% an acceptable threshold?

At pre-IND (R3):
6. Is the LOA cross-reference sufficient, or is additional CMC required for perioperative use?
7. Does the Agency agree with the DLT definition and the blinded attribution process separating drug toxicity from surgical complication?
8. Is the perioperative pause-and-restart schedule (T+7/T+14/T+21 keyed to ISGPS grade and trough) acceptable as an investigational schedule, and does the advisory that recommends it constitute part of the device?
9. Does the Agency accept Cohort 0 (device-only lead-in) as proposed?

Question 8 matters more than it looks: an advisory that recommends a *drug restart day* may be regulated differently from one that gives intraoperative surgical guidance. Resolve it before the IDE, not after.

### 5.5 Standing regulatory obligations
21 CFR Part 11 (electronic records) · Part 50 (human subjects) · Part 54 (financial disclosure) · Part 56 (IRB) · Part 312 (IND, incl. §312.23(g) system description, §312.32 safety reports, §312.57 records) · Part 812 (IDE) · ICH E6(R3) GCP · ICH E9/E9(R1) · applicable state law.

The Physical AI overlay (Subpart J, §312.400–405) invoked in the protocol is the **author's own adaptation** ([19057628](https://doi.org/10.5281/zenodo.19057628)), not codified law. In submission-facing documents, present it as a **voluntary sponsor-imposed control framework that exceeds current requirements** — that framing is a strength. Presenting it as existing regulation is a factual error a reviewer will catch immediately.

---

## 6. Nonclinical evidence plan

The protocol's Phase 0 simulation gate is necessary and not sufficient. Build the conventional spine underneath it.

| Tier | Study | Scale | Acceptance criteria | Months |
|:--|:--|:--|:--|:--|
| **N1** | Bench verification | Full V&V protocol suite | Advisory latency, gate decision latency, display refresh, and E-stop *alerting* latency each meet spec with a one-sided 95%/95% tolerance interval; **non-actuation proof** by design review + physical air-gap test; force/proximity computation accuracy vs. reference instrumentation | M8–M16 |
| **N2** | Adversarial & OOD battery | ≥500 scripted scenarios | Zero unsafe advisories that survive the gate; degradation detected within the specified window in 100% of injected-fault cases; no advisory emitted on out-of-distribution input without an explicit uncertainty flag | M12–M18 |
| **N3** | Phase 0 simulation campaign | ≥1000 procedures, ≥2 independent frameworks | USL ≥7.0; cross-framework consistency; sim-to-real trajectory gap <2 mm and force gap <0.5 N once N4/N5 data exist to compare against | M10–M20 |
| **N4** | Cadaveric feasibility | ≥10 pancreaticoduodenectomies, ≥2 surgeons | All eight operative phases and all three anastomoses completed with the advisory active; advisory-to-gate concordance ≥95%; no advisory contradicting anatomic ground truth on adjudicated review | M16–M20 |
| **N5** | GLP porcine survival | n≥16 (12 advisory-active, 4 control), 30-day survival | Survival ≥ historical control; no advisory-attributable injury on blinded necropsy; anastomotic integrity confirmed; full telemetry captured and replayable | M17–M22 |
| **N6** | Human factors summative | ≥15 representative users | No use error with potential for serious harm; automation-bias probes show surgeons override incorrect advisories at the prespecified rate | M18–M22 |
| **N7** | Cybersecurity | Threat model + independent pentest | No unmitigated vulnerability of moderate or higher severity; SBOM complete; §524B package complete | M14–M20 |

**Sim-to-real closure.** N3's fidelity claim is only meaningful once measured against N4/N5. Sequence it so the simulation campaign is *re-run and re-scored* after cadaver and animal data exist. Reporting a sim-to-real gap computed against nothing but other simulations is the single most likely place for a reviewer to lose confidence in the whole assurance argument.

---

## 7. Clinical execution plan

### 7.1 Design as amended

| Element | Protocol as written | **Recommended** |
|:--|:--|:--|
| Cohorts | 3+3 across DL1–DL3 | **Cohort 0 (device-only lead-in, n=3)** then 3+3 across DL1–DL3 |
| Total treated | up to 18 | **up to 21** |
| Doses | 160 / 220 / 300 mg QD | unchanged |
| DLT window | 28 days | unchanged |
| Staggering | sentinel, DSMB review between cases | unchanged, and extended to Cohort 0 |
| Sites | 1 | unchanged |
| Screening | ~36 to yield 18 | **~42 to yield 21** |
| Accrual | 1–2/month | 1–1.5/month realistic with staggering |

### 7.2 Cohort 0 and the learning-curve confound

**The problem.** With sentinel staggering, participant *i* is operation *i*. DL1 = cases 1–3 (or 1–6). Every dose comparison is also an experience comparison, and any adverse signal at DL1 is uninterpretable: was it the dose, or was it the first case ever performed?

**The fix, three parts:**
1. **Cohort 0 (n=3):** robotic Whipple with the advisory system active, daraxonrasib managed per institutional standard perioperative practice rather than the investigational pause-and-restart schedule. This isolates device safety before any investigational drug schedule is layered on. DSMB must clear Cohort 0 before DL1 opens.
2. **CUSUM learning curve:** prespecify cumulative-sum analysis of operative time, blood loss, task completion, and advisory-override rate against case order, reported for each credentialed surgeon.
3. **Case order as covariate:** in every supportive analysis of dose effect, report case order alongside dose level and state explicitly that the design cannot separate them. Say this in the CSR rather than letting a reviewer discover it.

### 7.3 DLT attribution

Separating a drug DLT from a surgical complication in a post-Whipple patient is genuinely hard — the confusable events (transaminitis, diarrhea, rash, cytopenias, fatigue) overlap the postoperative course. Required machinery:
- A **blinded attribution committee** — at minimum a medical oncologist and an HPB surgeon, both independent of the operative team, both blinded to dose level, adjudicating every Grade ≥3 event to drug / device / procedure / disease / concurrent illness, with the option of "indeterminate."
- A **prespecified DLT dictionary** listing, by CTCAE term, which events count as DLTs in the perioperative window and which are presumed surgical unless evidence indicates otherwise.
- **Indeterminate events count as DLTs** for escalation purposes. Conservative, defensible, and it removes the incentive to adjudicate toward escalation.

### 7.4 Operationalizing the Physical AI opt-out

The opt-out is the ethical centerpiece of the program. It must be mechanically real.

| Question | Specification |
|:--|:--|
| What is switched off? | The intraoperative advisory display and the LLM inference path. The independent hard-coded safety gate and telemetry capture remain active — they are patient-protective, not advisory. Say this in the consent form. |
| Is the operation different? | No. Same surgeon, same cleared robot, same technique. The surgeon does not see advisory output. |
| Is the participant still enrolled? | Yes. They remain in the Safety and DLT-evaluable populations and contribute to the drug arm in full. |
| Device endpoint? | Excluded from the Device-Evaluable population; **replaced** so the feasibility endpoint retains its denominator. |
| Can they opt out later? | Yes, up to the moment of incision, and the operative team must be able to disable the advisory path in under 60 seconds — this is a tested, timed procedure in the dry-run protocol, not an aspiration. |
| Documented where? | Source document, CRF, and the hash-chained audit trail, with the timestamp of election and of any change. |
| Told to the participant? | All of the above, in the consent form, in plain language, before the consent conversation. |

### 7.5 Accrual realism

At a high-volume center performing ~50–80 Whipples annually, the eligible fraction (resectable/borderline-resectable, KRAS G12-mutated ≈ 85–90% of PDAC, ECOG 0–1, anatomically suitable, willing) plus sentinel staggering and 28-day DLT windows realistically yields **1–1.5 participants/month**. Twenty-one participants ≈ **16–22 months of accrual**. Plan for 22. If accrual falls below 0.75/month for two consecutive quarters, activate a pre-qualified second site (prepare the CTA and IRB reliance agreement in advance rather than starting from zero at month 40).

---

## 8. Data, statistics & reproducibility

- **SAP finalized and signed before first patient in.** No exceptions.
- **Estimands** per ICH E9(R1) for every endpoint, with intercurrent-event strategies named for: open conversion, advisory opt-out, drug discontinuation, withdrawal, death, and loss to follow-up.
- **Exact (Clopper–Pearson) two-sided 95% CIs** on every proportion. Never a Wald interval at n≤21.
- **No efficacy interim, no alpha spent on dose selection**, per protocol §9.
- **Two parallel safety streams** — clinical AEs (MedDRA/CTCAE v5) and the device telemetry stream (E-stop activations and latencies, envelope excursions, gating events, advisory accept/block/escalate counts) — reported together in every DSMB dossier, never separately.
- **Individual participant listings in full.** At n≤21 every aggregate must be traceable to its records.
- **Reproducibility contract:** the analysis runs in a version-controlled, validated environment under a fixed seed; every figure in the CSR carries the commit hash that produced it; the L0 telemetry tier permits deterministic replay of any procedure on FDA request.
- **TRIPOD+AI** for the advisory component and **CREMLS** for the ML system, both prespecified rather than retrofitted at publication.

**One statistical caution to state up front:** with n≤21 and no comparator, this trial can detect a catastrophic device problem and can rule out a very high SAE rate. It cannot detect a modest degradation in surgical quality. Zero events in 18 still admits a true rate up to ~18%. Say this in the protocol, the consent form, and the CSR. Overclaiming precision at this sample size is the most common way a well-run Phase 1 loses credibility.

---

## 9. Governance, safety oversight & ethics

### 9.1 Four-tier oversight

| Tier | Body | Cadence | Authority |
|:--|:--|:--|:--|
| 1 | **Independent Safety Monitor** | every procedure | Real-time stop authority, independent of the operating team |
| 2 | **DSMB** | each cohort boundary + any trigger | Escalate / expand / pause / halt; applies the §9.4.6 halt rules |
| 3 | **Physical AI Safety Review Committee** | ≤90 days + ad hoc | Reviews autonomy-bearing behavior, gate decisions, USL, every software change; recommends USL reassessment |
| 4 | **IRB + FDA** | continuing review + reports | Approval, suspension, clinical hold |

**Prespecified halt rules (from protocol §9.4.6, retained):** device-related or procedure-related SAE rate ≥1/3 within a cohort, or two device-related deaths at any point → mandatory DSMB review and possible halt. Additional pause triggers: any unexpected device-related SAE, any breach of a hard cyber-physical limit, any pre-procedure safety-matrix failure.

### 9.2 Change control for the advisory system
**No software, model, prompt, or threshold change reaches a participant without:** (1) assessment against the PCCP, (2) Phase 0 re-validation against both simulation frameworks, (3) USL reassessment, (4) Physical AI Safety Review Committee concurrence, (5) IDE supplement if outside the PCCP. The build in the operating room is byte-identical to the build that was tested, and that identity is verified by hash at the pre-procedure safety matrix.

### 9.3 Conflict of interest — required structure
Disclosure is not management. Before IRB submission:
- Sponsor-Investigator **recuses** from all escalation, halt, and attribution decisions.
- DSMB chair, medical monitor, ISM, and attribution committee members have **no financial interest** in ChemicalQDevice and no reporting line to it.
- Institutional COI committee reviews and approves a written management plan.
- The consent form **discloses** that the sponsor developed the advisory system and that the person who designed it is not the person deciding whether it is safe to continue.
- Consent is obtained by someone who is neither the treating surgeon nor an employee of the sponsor.

### 9.4 The seven participant commitments
Take the Patient Robot Advocacy paper's own test — every commitment must name something the participant can check — and build a one-page participant card mapping each commitment to its enforcing protocol clause. Validate the card with the Patient Advisory Board (WS-10) before IRB submission. If a commitment cannot be tied to a clause that makes it enforceable, either add the clause or remove the commitment. Do not ship an unenforceable promise: the advocacy paper's own argument is that reassurance without a checkable referent reads as marketing.

---

## 10. Site strategy

**Site selection criteria (weighted):** institutional Whipple volume ≥50/yr and an established robotic pancreatic program (25%) · per-surgeon robotic Whipple volume above the published learning-curve plateau, ≥2 such surgeons (20%) · IRB and CTO experience with significant-risk IDE studies (15%) · research pharmacy capable of investigational-product handling (10%) · ICU, interventional radiology, and therapeutic endoscopy for fistula rescue (10%) · IT willing to host an air-gapped on-premises inference node inside the OR network boundary (10%) · institutional appetite for an FIH AI-surgical study and the associated insurance (10%).

That last criterion is decisive far more often than the clinical ones. Test it in the first meeting.

**Named candidates in the repository:** UC San Diego Moores Cancer Center (Rebekah White, MD — pancreatic surgical oncology; Gregory Botta, MD PhD — GI medical oncology; Moores CTO) and Scripps (Scripps Research Translational Institute / Digital Trials Center; Scripps Health pancreatic program). The Scripps approach drafted in the repo — lead with the public AI portfolio, introduce the trial only after interest — is sound and should be preserved. Approach at least four institutions; expect two to decline on the IT/air-gap or insurance criterion alone.

**Sequence per site:** non-confidential portfolio → 45-minute feasibility meeting with surgeon + oncologist + CTO → written feasibility assessment → site qualification visit → CTA and budget negotiation → IRB → SIV. Budget 6–9 months from first contact to activated site, longer if the CTA involves novel indemnification terms for an AI device.

---

## 11. Master schedule & stage gates

### 11.1 Gates

| Gate | Name | Month | Criteria | Kill-capable |
|:--|:--|:--|:--|:--|
| **G0** | Program viability | M3 | Scope decision made (§3); FIH/naming corrections applied (F3, F4); PI effort resolved; ≥1 site LOI; ≥1 drug-supply conversation opened | **Yes** |
| **G1** | Drug access | M9 | RevMed LOA + IB + supply agreement executed, or a documented contingency in force | **Yes** |
| **G2** | Design freeze | M14 | Design inputs/outputs locked; DHF open; ISO 14971 risk file complete; non-actuation architecture proven | No |
| **G3** | Regulatory alignment | M16 | Q-Sub and pre-IND minutes received; nonclinical plan and endpoints agreed; no unresolved Agency objection | **Yes** |
| **G4** | Nonclinical complete | M23 | N1–N7 all pass; USL ≥7.0; sim-to-real <2 mm / <0.5 N measured against cadaver+animal data | **Yes** |
| **G5** | Clearance to proceed | M28 | IDE approved; IND safe-to-proceed; IRB approved; DSMB seated; COI plan approved; SAP signed | No |
| **G6** | Site ready / FPI | M30 | Credentialing complete; dry runs passed including opt-out drill; pre-procedure safety matrix passing; first participant consented | No |
| **G7** | Cohort gates | rolling | DSMB escalate / expand / pause / halt at each cohort boundary; Cohort 0 clears before DL1 | No |
| **G8** | Primary readout | M52 | Accrual complete; 90-day pathology complete; MTD/RP2D declared; feasibility endpoint reported | No |

### 11.2 Timeline

| Phase | Months | Content |
|:--|:--|:--|
| **P0 · Definition** | M0–M6 | Scope decision; corrections F1–F4; RevMed and site outreach; regulatory lead hired; Pre-RFD; funding submissions |
| **P1 · Design & alignment** | M6–M16 | QMS stand-up; design controls; LLM assurance build; Q-Sub (M6) and pre-IND (M9); design freeze (M14) |
| **P2 · Nonclinical** | M14–M23 | Bench V&V; adversarial battery; cadaver (M16–20); GLP porcine (M17–22); human factors; cybersecurity; Phase 0 re-scored against real data |
| **P3 · Submission** | M22–M28 | IDE (M22); IRB (M23); IND (M24); CMS (M24); registration; DSMB seating; SAP |
| **P4 · Activation** | M27–M30 | SIV; credentialing; dry runs; pharmacy setup; **FPI ~M30** |
| **P5 · Accrual** | M30–M52 | Cohort 0 → DL1 → DL2 → DL3 with sentinel staggering and DSMB gates; ~1–1.5/month |
| **P6 · Primary analysis** | M49–M55 | Last-patient 90-day pathology; database lock; MTD/RP2D; feasibility readout; **CSR interim** |
| **P7 · Long-term follow-up** | M52–M75 | q12wk to 24-month OS for the last participant |
| **P8 · Close & transition** | M72–M78 | Final CSR; End-of-Phase-1 meeting; Phase 2 briefing package; full data and code deposition |

**Critical path:** RevMed LOA (G1) → pre-IND (R3) → GLP porcine (N5) → IDE/IND (R5/R6) → site activation → FPI. Everything else has float. Protect these five.

**Compressibility.** The LLM documentation pipeline genuinely compresses the authoring of the IDE, IND, IRB package, SAP, cohort dossiers, and CSR — the author's own finding is that papers finish in 1–4 days. It does **not** compress: the 30-day IND clock, the 30-day IDE review, IRB turnaround, the GLP porcine 30-day survival window, the 28-day DLT windows, sentinel staggering, accrual rate, or 24-month OS follow-up. Realistic saving on a 75-month program: **4–7 months**, concentrated in P1 and P3. Claim that, and no more.

---

## 12. Budget & funding

### 12.1 Cost estimate (Option B, 6.5 years)

| Category | Low | High | Notes |
|:--|--:|--:|:--|
| Device engineering, QMS, design controls | $4.5M | $6.0M | Includes ISO 13485 stand-up, DHF, V&V, human factors, cybersecurity |
| LLM assurance & VVUQ | $2.0M | $3.0M | Assurance lead + engineers; on-prem inference hardware; adversarial battery |
| Nonclinical (bench, cadaver, GLP porcine) | $2.5M | $4.0M | GLP animal survival is the largest single line |
| Regulatory (consulting + submissions) | $1.5M | $2.0M | Dual device+drug competence commands a premium |
| Clinical trial conduct (21 participants) | $2.8M | $4.0M | ~$130–190K per participant at an academic center for a complex surgical trial |
| CRO monitoring (robotics/AI-competent) | $1.5M | $2.2M | Includes cyber-physical source-data verification |
| Data systems, Part 11, CSV, telemetry storage | $1.5M | $2.5M | L0 raw tier storage is a real recurring cost — size it early |
| Governance (DSMB, ISM, PAISRC, attribution cmte) | $0.6M | $0.9M | Member honoraria across 6.5 years |
| Insurance & indemnification | $0.8M | $1.5M | FIH AI-surgical liability; quote this early, it can move the whole model |
| Program management & administration | $1.8M | $2.5M | |
| Patient advocacy, consent, translation, PAB | $0.3M | $0.5M | |
| Publication, deposition, dissemination | $0.2M | $0.3M | |
| **Total** | **$20.0M** | **$29.4M** | Plan to **$24M** with 15% contingency |

Option A (build the platform) adds **$150M+** and 6–8 years. Option C reduces to $6–9M but forfeits the intraoperative claim.

### 12.2 Funding architecture

Pioneer at ~$700K direct/yr × 5 ≈ **$3.5M ≈ 14%** of need. Stack:

| Source | Target | Role | Timing |
|:--|--:|:--|:--|
| NIH Director's Pioneer (RFA-RM-27-001) | $3.5M | Scientific leadership; the assurance science | resubmit per cycle |
| NCI SBIR/STTR Phase I→II (+ Fast-Track/Bridge) | $3–5M | Device engineering and V&V | M0, M12 |
| Industry in-kind — drug supply (RevMed) | $1–3M equiv. | Daraxonrasib + IB + LOA | G1 |
| Industry — robot partner co-investment | $2–5M | Platform access, integration engineering, possible IDE co-sponsorship | M6+ |
| NIH UG3/UH3 or R01 (device/trial mechanism) | $5–8M | Clinical trial conduct | M12, M24 |
| PanCAN / Lustgarten / philanthropy | $2–4M | Clinical costs, patient advocacy | M6+ |
| Institutional / site cost-share | $1–2M | Infrastructure, IRB, some clinical | at CTA |
| State (e.g., CIRM-analogue, CA programs) | $1–3M | Infrastructure | M12+ |

**Funding rule:** do not open the IDE until at least the device engineering and nonclinical lines (~$9–13M) are committed or contracted. Running out of money between design freeze and IDE is the most expensive failure mode available — the DHF goes stale, the model version drifts, and the nonclinical work must be repeated.

**Pioneer effort commitment (51% years 1–3) is a genuine constraint** for a CEO also running the company. Resolve it at G0: either commit, restructure the role, or select a mechanism without that requirement.

---

## 13. Organization & staffing

| Role | FTE | When | Notes |
|:--|--:|:--|:--|
| Sponsor-Investigator | 0.5–1.0 | M0 | Recused from safety/escalation decisions (§9.3) |
| Program Director | 1.0 | M0 | Owns schedule, gates, risk register |
| Regulatory Lead (device + drug) | 1.0 | **M0 — hire first** | The single highest-leverage hire |
| Head of Engineering / Quality | 1.0 | M2 | QMS, DHF, design controls |
| AI Assurance Lead | 1.0 | M2 | VVUQ, model governance, PCCP |
| Software engineers | 3–4 | M3 | Advisory system, gate, telemetry |
| Preclinical Lead | 0.5 | M8 | Cadaver + GLP animal |
| Clinical Operations Lead | 1.0 | M12 | Site, IRB, governance, CRO |
| Trial Statistician | 0.5 | M12 | SAP, DSMB dossiers |
| Data Engineering Lead | 1.0 | M6 | Part 11, CSV, telemetry pyramid |
| Surgical Lead (site PI) | 0.2 | M12 | Credentialing, training, HF |
| Participant Advocacy Lead | 0.3 | M12 | Independent of surgical team |
| Quality / CSV specialist | 0.5 | M8 | Validation packages |
| CRO, DSMB, ISM, attribution cmte, medical monitor | contracted | M18+ | Independent by construction |

**Hire the Regulatory Lead before anything else.** Most of the findings in §2 are ones an experienced dual-competent regulatory professional would have surfaced at the outline stage.

---

## 14. Risk register (top 20)

Scored L(1–5) × I(1–5).

| # | Risk | L | I | Score | Mitigation | Owner |
|:--|:--|--:|--:|--:|:--|:--|
| R1 | RevMed declines drug supply/LOA | 3 | 5 | 15 | Early, professional, non-confidential first contact; parallel contingencies (§WS-2); monitor approval timeline | S-I |
| R2 | Program proceeds on the hypothetical 8-arm platform | 3 | 5 | 15 | Force the §3 decision at G0; make it a documented, dated decision | Prog Dir |
| R3 | FDA requires more nonclinical than planned | 3 | 4 | 12 | Q-Sub question 2 asked in writing at M6; do not execute animal work before the answer | Reg Lead |
| R4 | Funding shortfall between design freeze and IDE | 4 | 4 | 16 | Do not open IDE until $9–13M committed; stage-gate spend | Prog Dir |
| R5 | No site accepts an FIH AI-surgical study | 3 | 5 | 15 | Approach ≥4 institutions; test IT/air-gap and insurance appetite in meeting 1 | Clin Ops |
| R6 | Accrual below plan | 4 | 3 | 12 | Pre-qualify a second site with CTA and reliance agreement ready at M36 | Clin Ops |
| R7 | Device-related SAE triggers halt | 2 | 5 | 10 | Cohort 0; sentinel staggering; ISM per procedure; conversion always available | DSMB |
| R8 | DLT attribution disputes stall escalation | 4 | 3 | 12 | Blinded attribution committee + prespecified DLT dictionary; indeterminate counts as DLT | Statistician |
| R9 | Model or prompt drift between validation and use | 3 | 4 | 12 | Hash-verified build at every pre-procedure matrix; locked weights; no online learning | AI Assurance |
| R10 | Automation bias — surgeon over-reliance | 3 | 4 | 12 | HF countermeasures; override-rate monitoring; PAISRC review; display design | Surgical Lead |
| R11 | Cybersecurity incident on the inference node | 2 | 5 | 10 | Air-gapped on-prem; deny-by-default; pentest; §524B package; 7/15-day reporting ready | Eng/Quality |
| R12 | COI objection blocks IRB approval | 3 | 4 | 12 | Full §9.3 structure filed *before* submission, not in response to a query | S-I |
| R13 | Insurance unobtainable or prohibitive | 3 | 4 | 12 | Quote at M6, not M24; it can change the scope decision | Prog Dir |
| R14 | Pioneer effort requirement unmet | 3 | 3 | 9 | Resolve at G0; alternative mechanisms identified | S-I |
| R15 | Telemetry storage cost exceeds model | 3 | 2 | 6 | Size the L0 tier at M6 with real sampling rates; tiering policy set before FPI | Data Eng |
| R16 | Key person dependency on the Sponsor-Investigator | 4 | 4 | 16 | Document everything; hire Program Director and Regulatory Lead early; succession plan | Prog Dir |
| R17 | Opt-out uptake high enough to starve the device endpoint | 2 | 3 | 6 | Replacement rule (§7.4); track and report opt-out rate as a study finding in its own right | Clin Ops |
| R18 | Robot partner declines platform access | 3 | 4 | 12 | Two candidate platforms in parallel; purchase/lease as fallback | Prog Dir |
| R19 | Reviewer conflates simulation results with clinical evidence | 4 | 3 | 12 | Segregate simulation provenance in every document; never cite a simulated figure without labeling it | Reg Lead |
| R20 | Publication of preliminary results compromises the trial | 2 | 3 | 6 | Publication plan gates release until DSMB and database lock | Prog Dir |

Review monthly. Any risk reaching score ≥16 escalates to a gate review.

---

## 15. Kill criteria

State these now, while nobody is invested, and honor them.

1. **No drug.** No LOA and no viable contingency by **M12** → stop the drug arm; consider a device-only feasibility study.
2. **No device identity.** No named, obtainable surgical platform and no executed scope decision by **M6** → stop.
3. **Nonclinical failure.** GLP porcine survival shows advisory-attributable injury, or the adversarial battery produces an unsafe advisory that survives the gate → stop and redesign; do not amend the acceptance criteria to fit the result.
4. **Regulatory.** FDA requires evidence the program cannot generate within 3 years of G3 → stop or restructure to Option C.
5. **Funding.** Less than $9M committed by **M18** → pause before the nonclinical spend rather than after.
6. **Safety in-trial.** Two device-related deaths, or a device-related SAE rate ≥1/3 in any cohort → halt per §9.4.6 and do not resume without independent root-cause review.
7. **Integrity.** Any loss of audit-chain integrity that cannot be reconstructed → halt patient-facing activity until reconstructed and independently verified.

---

## 16. First 90 days

| # | Action | By | Owner |
|:--|:--|:--|:--|
| 1 | Convene the scope decision (§3); document the choice with a date and a rationale | D+14 | S-I |
| 2 | Correct "first-in-human" (drug) and "LLM-Directed" → "LLM-advised" across all outward-facing materials | D+21 | S-I |
| 3 | Post the Regulatory Lead role; interview dual device+drug candidates | D+14 | S-I |
| 4 | Send the RevMed non-confidential one-pager + 2-page synopsis + biosketch + budget range + dependency matrix (never the full package) | D+7 | S-I |
| 5 | Request the UCSD 45-minute feasibility meeting (White / Botta / Moores CTO) | D+7 | S-I |
| 6 | Execute the Scripps inbound portfolio strategy already drafted in the repo | D+30 | S-I |
| 7 | Draft the Pre-RFD; identify the two candidate robotic platforms | D+45 | Reg Lead |
| 8 | Obtain an indicative clinical-trial liability insurance quote for an FIH AI-surgical study | D+60 | Prog Dir |
| 9 | Resolve the Pioneer 51% effort question in writing | D+30 | S-I |
| 10 | Build the integrated master schedule with G0–G8 and stand up the risk register | D+30 | Prog Dir |
| 11 | Scope the QMS engagement (ISO 13485 / QMSR); get three quotes | D+60 | Eng/Quality |
| 12 | Convene the Patient Advisory Board; draft the seven-commitments participant card | D+90 | Advocacy Lead |
| 13 | Draft the Q-Sub briefing book skeleton with the five questions in §5.4 | D+90 | Reg Lead |
| 14 | Size the L0 telemetry tier against real sampling rates; produce the storage cost model | D+90 | Data Eng |
| 15 | Publish protocol v2.0 incorporating Appendix A amendments | D+90 | S-I |

---

## 17. Recommended protocol amendments (Appendix A)

| # | Section | Change |
|:--|:--|:--|
| A1 | Title, §1.1 | "LLM-Directed" → "LLM-advised"; scope the FIH claim to the device and the perioperative schedule, not to daraxonrasib |
| A2 | §1.1, §6.1.1 | Replace the hypothetical eight-arm platform with the named cleared robot + the advisory system as the investigational device; restate force/E-stop caps as monitored thresholds where not hardware-enforced |
| A3 | §4.1, §5, §9.2 | Add Cohort 0 (n=3, device-only lead-in); total treated up to 21; screening ~42 |
| A4 | §4.3 | Add bench, cadaveric (n≥10), and GLP porcine survival (n≥16) to the Phase 0 gate; require sim-to-real to be scored against cadaver/animal data |
| A5 | §9 | Add CUSUM learning-curve analysis and case order as a covariate; add the Device-Evaluable population and the opt-out replacement rule |
| A6 | §8.3, §9 | Add the blinded attribution committee charter and the prespecified DLT dictionary; indeterminate events count as DLTs |
| A7 | §10.1 | Fully specify the opt-out per §7.4 including the <60-second disable procedure and its drill |
| A8 | §10.11 | Replace disclosure-only COI handling with the recusal-and-independence structure of §9.3 |
| A9 | §0 (Compliance) | Reframe the Physical AI Subpart J overlay as a voluntary sponsor-imposed framework exceeding current requirements, with the author's adaptation cited as such |
| A10 | §9.2 | Add the plain statement that n≤21 cannot detect modest degradation in surgical quality |
| A11 | throughout | Label every figure derived from simulation as simulation-derived at the point of use |

---

## 18. Standards index (Appendix C — verify current versions before use)

**Device:** ISO 13485 · FDA QMSR (21 CFR 820, harmonized) · ISO 14971 risk management · IEC 62304 software lifecycle (Class C) · IEC 62366-1 usability · IEC 60601-1 / -1-2 (EMC) / -1-6 · **IEC 80601-2-77** (robotically assisted surgical equipment) · ISO 10993 biocompatibility · FDA premarket cybersecurity guidance + FD&C §524B (SBOM) · FDA PCCP guidance for AI-enabled devices · Good Machine Learning Practice principles · FDA CDS software guidance · FDA early feasibility study guidance.

**Drug/clinical:** 21 CFR 11, 50, 54, 56, 312, 812 · ICH E6(R3) GCP · ICH E9 and E9(R1) estimands · CTCAE v5.0 · MedDRA · Clavien-Dindo · ISGPS 2016 fistula definition · RECIST 1.1.

**Reporting:** TRIPOD+AI · CREMLS · CONSORT (+ extensions) · SPIRIT · ClinicalTrials.gov requirements.

---

## 19. Closing assessment

The scientific idea is sound and the documentation is unusually complete for a program at this stage. The binding constraints are not intellectual — they are that the device must become real, the drug must become obtainable, the nonclinical evidence must be generated rather than simulated, and the money must be roughly seven times what has been sought.

The single decision that determines whether this program ever reaches a patient is §3. Taken as Option B, the whole thing becomes a normal — difficult, expensive, but entirely conventional — first-in-human device program with a well-designed drug arm attached, and the assurance architecture that is the program's actual contribution gets tested on a real patient in about thirty months. Taken as Option A, it remains a paper.

---

*Plan v1.0 · prepared for ChemicalQDevice · not committed to any repository · independent research document, not medical or regulatory advice.*
