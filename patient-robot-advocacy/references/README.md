# references - author bibliography for the Patient Robot Advocacy build (v1.0.0)

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Entries](https://img.shields.io/badge/Author%20entries-52-00417A.svg)](references.bib)
[![Bill](https://img.shields.io/badge/H.R.%209510%20v5-10.5281%2Fzenodo.20619762-blue.svg)](https://doi.org/10.5281/zenodo.20619762)
[![Span](https://img.shields.io/badge/Span-Aug%202024%20to%20Jul%202026-6C757D.svg)](references.bib)
[![Format](https://img.shields.io/badge/Format-doi%20%2B%20url%20%2B%20note-6C757D.svg)](references.bib)

[`references.bib`](references.bib) is the author's up-to-date reference set. It is the
authority for every author-work citation in the paper and, in particular, for the
**legislation citation**: bill references use **H. R. 9510 v5**,
[`10.5281/zenodo.20619762`](https://doi.org/10.5281/zenodo.20619762), and supersede the
earlier H. R. 9501 to H. R. 9507 numbering used inside
[`../inputs/patient-priority-physical-ai.zip`](../inputs).

## The legislative lineage, newest first

| Key | Work | DOI |
|:--|:--|:--|
| `hr9510billv5` | H. R. 9510 (Bill v5.0) 2026 - **the citation this paper uses** | [10.5281/zenodo.20619762](https://doi.org/10.5281/zenodo.20619762) |
| `congress9510` | Earning the Congress's Vote: A New Oncology Trial Framework for Enacting H. R. 9510 | [10.5281/zenodo.20726461](https://doi.org/10.5281/zenodo.20726461) |
| `fedlawhr9510` | From H. R. 9510 to Federal Law: A Narrative Case for Verified Physical AI Oncology Trials | [10.5281/zenodo.20685379](https://doi.org/10.5281/zenodo.20685379) |
| `hr9510billv4` | H. R. 9510 (Bill v4.0) 2026 | [10.5281/zenodo.20576907](https://doi.org/10.5281/zenodo.20576907) |
| `hr9510billv3` | H. R. 9510 (Bill v3.0) 2026 | [10.5281/zenodo.20535429](https://doi.org/10.5281/zenodo.20535429) |
| `verifygenact` | Verification Before Generation Act of 2026 | [10.5281/zenodo.20485580](https://doi.org/10.5281/zenodo.20485580) |
| `vvuqoncobill` | VVUQ Physical AI Oncology Trial Bill | [10.5281/zenodo.20454870](https://doi.org/10.5281/zenodo.20454870) |
| `paibillprior` | Patient Priority of Proposed U.S. Bills for Physical AI Oncology Clinical Trials | [10.5281/zenodo.20045457](https://doi.org/10.5281/zenodo.20045457) |

## Patient-facing author works the paper leans on most

| Key | Work | Used in |
|:--|:--|:--|
| `paipatientjr` | A Cancer Patient's Journey Through a Regulated Physical AI Oncology Trial | § 2, § 7, § 9; Figures 3, 9, 17, 24 |
| `paipredict4x` | Accelerated Patient Prediction in Physical AI Oncology Clinical Trials: 4 Extensive Simulations | § 10; Figures 27, 28 |
| `pdac060s2030` | 2030: 60 Second PDAC Robotic Whipple Procedure and Daraxonrasib Simulation | § 7, § 10; Figures 17, 20, 27 |
| `h2pancrevvuq` | Mobile Pancreatic Cancer Unitree H2 Surgical Humanoid with Priority VVUQ | § 9; Figure 26 |
| `humanoid4sit` | Threefold Humanoid 24/7 Adverse Event Oncology Trial Response Team | § 9, § 11; Figure 26 |
| `onpremwhippl` | On-Premises LLM-Directed Robotic Pancreaticoduodenectomy with Perioperative Daraxonrasib | all sections |
| `phase1ind` | Investigational New Drug Application, Daraxonrasib, Phase 1 | § 5, § 12 |
| `cfr050paiuni` | Adaption: 21 CFR Part 50, End-to-End Physical AI Oncology Trial Unification | § 6, § 8 |
| `cfr312paiuni` | Adaption: 21 CFR Part 312, End-to-End Physical AI Oncology Trial Unification | § 1, § 11 |
| `paisitedocpk` | Physical AI Oncology Clinical Trial Site Complete Documentation Package | § 11 |
| `paiautospons` | Fully Automated Sponsor: Physical AI Oncology Clinical Trial Platform | § 6; Figure 15 |
| `natlpaiplatf` | National Platform for Physical AI Oncology Trials | § 12; Figure 30 |
| `rasolute302` | Daraxonrasib or Chemotherapy in Previously Treated Metastatic Pancreatic Cancer | § 4, § 7, § 10 |

## How this file is merged into the paper bibliography

The paper bibliography at [`../final-patient/references.bib`](../final-patient) is built
from three sources, all normalised to one BibTeX format:

| Source | Contributes | Normalisation applied |
|:--|:--|:--|
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `references.bib` | the clinical, CFR, FDA, and consensus-standard entries | none; this file defines the format |
| this `references.bib` | the author works and the H. R. 9510 v5 legislation citation | `doi` + `url` + `note` triad added so every entry prints a clickable DOI |
| [`../research/research-b.md`](../research) | the thirteen patient-perception entries | already in the target format; merged verbatim |

Every entry that carries a DOI prints the DOI as text and hyperlinks it to
`https://doi.org/<doi>`, and long URLs break on any character so no link runs past the
right margin.

## Files from other directories used here

| Source | Used for |
|:--|:--|
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) | the BibTeX format all entries are normalised to |
| [`../research/research-b.md`](../research) | the thirteen new patient-perception entries |
| [`../inputs/patient-priority-physical-ai.zip`](../inputs) | the bill lineage superseded by H. R. 9510 v5 |

## License

Released under CC BY 4.0. Author: Kevin Kawchak, CEO ChemicalQDevice
([ORCID 0009-0007-5457-8667](https://orcid.org/0009-0007-5457-8667)).
