# End-to-End Pancreatic Ductal Adenocarcinoma Digital Twin Clinical Trial Proposals

**Kevin Kawchak** (ORCID: 0009-0007-5457-8667)
Chief Executive Officer
ChemicalQDevice
San Diego, CA
June 24, 2025
kevink@chemicalqdevice.com

## Abstract

**Question:** Can online clinical trial literature be utilized by artificial intelligence to generate well-informed pancreatic ductal adenocarcinoma (PDAC) digital twin trial proposals?

**Findings:** AI successfully generated 40 meta-analyses in PDAC top research areas at an average word length of 10,196. One verification per meta-analysis was performed using AI automation, and the combined 408,081 word dataset was utilized to generate reports. Reports were separately verified and further visualized by AI. A second dataset consisting of the reports was used by five different AI models to yield five proposals. The proposals were evaluated by five AI judges to determine the top three proposals. Proposal deliverable completion reached a maximum score of 9.60/10, while the top citation proficiency score was 9.20. Prospective trial impact reached a peak score of 8.94, while funding probabilities ranged from 8.54 to 8.66.

**Design:** The framework consisted of 7 AI model combinations; o3re: ChatGPT o3 Research, g25p: Google Gemini 2.5 Pro Preview, son4: Sonnet 4 Extended, grk3: xAI Grok 3, o3pr: ChatGPT o3-pro, ops4: Opus 4 Extended, and o3ch: ChatGPT o3; which were utilized according to model specific advantages. o3re autonomously searched the web and constructed detailed meta-analyses for Dataset 1. g25p was used to verify quantitative data across meta-analyses and reports, and also generated reports. son4 and ops4 were used to produce visualizations in Python for reports and proposals; while grk3 fixed code when necessary. The 6 reports were combined to form Dataset 2, which was an input for the o3pr, ops4, g25p, o3ch, and grk3 proposals. The same 5 models served as judges for the combined proposals, with average scores being used to determine the top 3 proposals. AI run time for core experiments was approximately 14 hours, with paper completion in 27 days.

**Results:** One verification for each meta-analysis was conducted by g25p at an average accuracy of 95%. The same model verified one table for each of the six reports at a self-reported 84.0% accuracy. Both verification accuracies are considered preliminary due to complexities in grounding multiple data types. Meta-analyses by o3re ranged from 6,440-13,033 words with an average time of 19.3 minutes. Reports by g25p averaged 2,538 words and 2.48 minutes, with a Pearson's r coefficient of 0.94. Proposals totaled 8,903 words in 22.32 minutes. Proposal analyses by each of the five models were within 1-2 minutes, except for o3pr at 17.77 minutes. Each proposal included 10 prompt specific deliverables and a main therapy recommendation from a report.

**Importance:** An area of of significance for all 5 proposals was the inclusion of a triple drug combination with the highest Therapeutic Synergy & Viability Score (TSVS) detailed in Report 1. Proposal A utilized the combination as follows: "The DT platform will prospectively simulate a first‑in‑human (FIH) study of the top‑ranked therapeutic triplet—Daraxonrasib + Mitazalimab + Liposomal Irinotecan—identified in Report 1 (predicted TSVS 8.15)." Proposal B also highlighted the therapy: "simulating 10,000 virtual pancreatic cancer patients to de-risk the clinical development of a novel three-drug combination: daraxonrasib (pan-KRAS inhibitor) + mitazalimab (CD40 agonist) + liposomal irinotecan." The drug combination is traceable to source data using meta-analysis MA-23 for Daraxonrasib, MA-15 for Mitazalimab, and a total of 8 Meta-Analyses utilizing Liposomal Irinotecan. This example of data fusion likely indicates functional utility between AI datasets.

**Conclusion:** Enhanced predictive performance and clinical relevance was achieved through a scalable multi-step workflow beginning with meta-analysis and report generations. Source data was utilized effectively across models, yielding AI aware PDAC digital twin trial proposals. Although automated AI verification accuracies were preliminary, reports were translated into top proposals, and screened visualizations were effective in discerning results. Vital trial proposal information obtained from charts revealed important distinctions between the three top proposals across 24 month timelines, multi-part ROI analyses, and budgets ranging from $8.5M-$17.8M. Proposal A by o3pr included the most intriguing digital twin Phase I/early-Phase II trial, with high scores in deliverable completion, citation ability, and chances of funding.

---

**Figure (MainProcessPDACDT):** PDAC Digital twin trial proposal pipeline. [Image: images/BigProcessPDAC.png]
