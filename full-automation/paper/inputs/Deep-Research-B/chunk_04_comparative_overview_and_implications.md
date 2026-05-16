# Comparative Overview

| **Project** | **Domain / Institution** | **Claude Code Version** | **Prototyping & Timeline** | **Key Results/Perf.** | **Status/Notes** |
| --- | --- | --- | --- | --- | --- |
| Fully Automated Sponsor | Oncology trial sponsor (Pittsburgh AI Lab) | Opus 4.6 | End-to-end built in hours via prompts; 13 commits in 72 min | 288 trial decisions automated; 100% simulated compliance | Simulation-only; prototype for autonomous trial sponsor. |
| Federated AI Trials Platform | Oncology trial infrastructure | Opus 4.6 (via peer-review) | Developed over months; code iterated via dual-AI review | 23 tools validated; 668/668 tests passed; 100% code fix rate | Prototype platform; integrates HIPAA, FHIR, audit features. |
| Patient Prediction (4 sims) | Oncology trial analytics | Opus 4.7 Max | 4 simulated trial scenarios (hours-to-days); hourly commit cadence | ML AUC > 0.89 (better than Cox baseline); 1M-token context used | Proof-of-concept; improves outcome modeling with agentic ML. |
| ClinAgent (Stat Prog) | Clinical trial statistical programming (Harrisburg U) | Any agent (demonstrated w/Claude) | Skill-framework built and validated by Jan 2026; iterative skill testing | 100% precision log/data checks; 72.1% spec derivation accuracy | Open-source tool; aids CDISC compliance; no patient data needed. |
| **Industry Case Studies** | Schrödinger (chemistry), Axiom Bio (toxicology) | Opus 4.x (Sonnet/Opus) | Ongoing use (2025–26) at leading pharma/biotech | "Ideas to code in minutes…10× faster" (Schrödinger); "billions of tokens" for toxicity features (Axiom) | Corporate adoptions; not public projects but evidence of value. |

## Development Timeline (2026)

**Figure:** Milestones for 2026 projects prototyped with Claude Code. (Murugappan's mCRC CRF case is noted from informal report.)

These examples underscore that *Claude Code-enabled prototyping* can compress what used to be months of programming into days or hours. Across projects the **hardware demands were minimal** (even a laptop could run the final models), and the **tech stacks** combined Claude Code with domain APIs (SAS I/O, FHIR/MCP servers, Python ML). Performance metrics were uniformly strong – e.g. code generation success rates near 100%, model accuracies exceeding baselines, and end-to-end tasks completed without manual coding.

However, all of these are currently at **prototype** stage. None have regulatory clearance or clinical deployment (authors explicitly note outputs need human review). Reported limitations include the 0–30% error/hallucination rate inherent to LLMs (requiring oversight) and the "n=1" nature of simulated data. Still, they demonstrate that Claude Code can deliver *production-grade code rapidly*. In particular, the oncology-focused trials show how AI can automate even heavily regulated workflows: future robotic trial setups could use these agents to generate protocols, CRFs, and analysis scripts on the fly, subject to audit. The convergence of Claude Code with MCP and AI agent methods suggests that **automated Physical AI oncology trial workflows** – where robots execute experiments and AI manages data – are plausible in the near term.

## Sources

The above analysis is based on 2026 publications and announcements. Kawchak et al.'s trial simulation papers (2026) report the Claude Code usage and metrics. Yan (2026) details ClinAgent's validation results. Company case quotes (Anthropic news) illustrate real-world uptake. No clinical deployments of these systems were found by May 15, 2026.

## Code and Data Availability

All cited works are open-access. Kawchak's projects are on Zenodo with DOI references. ClinAgent source is on GitHub. Data used in simulations were synthetic as described.

## Implications

Together, these projects point toward a future in which much of oncology trial design and execution could be co-ordinated by AI agents. Rapid prototyping tools like Claude Code empower clinicians and researchers (even without deep coding expertise) to build complex decision support and automation pipelines almost instantly. For regulated clinical workflows, it will be critical to combine these capabilities with robust audit trails (as shown in ClinAgent) and safety governance (as in the sponsor architecture). The 2026 projects demonstrate that, with appropriate guardrails, AI can achieve *end-to-end* trial automation in simulation – a harbinger of next-generation "Physical AI" trials.
