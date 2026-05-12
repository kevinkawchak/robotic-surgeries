# References - Part 2 of 2 (BibTeX Entries)

This chunk contains the second half of the BibTeX entries from references.bib. These entries cover: cancer-specific LLM applications across multiple cancer types (breast, prostate, lung, liver, brain tumor, pancreatic), oncology decision support, clinical informatics, radiation oncology, LLM context length and inference papers, plus three thematic blocks at the end of the file:

- **INTRODUCTION block** (`01IntroKatsoulakis` through `13IntroNSFNIHFDA`): the citations used in the Introduction subsections of Chunk 02 (Clinical Trials & Digital Twins, Digital Twins in Oncology, PDAC Digital Twin Initiatives). Key entries: `02IntroPhesi`, `03IntroPhesi` (Phesi NSCLC digital twin), `04IntroAltislabs` (Altis Labs lung trial AI), `05IntroWu` (Wu MRI-based TNBC twins), `06IntroBordukova` (generative AI for digital twins), `07IntroWang` (TWIN-GPT), `08IntroFrederick`, `09IntroFrederick` (Frederick National Lab million PDAC patients), `10IntroOsipov` (Cedars-Sinai/Hopkins Molecular Twin), `11IntroJoslyn` (Genentech Tscm digital twins), `12IntroNSFNIHFDA`, `13IntroNSFNIHFDA` (NSF/NIH/FDA digital twin funding)
- **PAPER block** (`01PaperBehrouz`): the Titans memory paper, cited in Chunk 03 (Results: Reports) regarding g25p's higher recall accuracy at large context window
- **Quotes block** (`01QuoteHalbrook` through `08QuoteZitu`): the pull-quote citations scattered through Chunks 05, 07, and 08 — Halbrook on PDAC mortality, Mukund on AI in PDAC, Urooj on PDAC prognosis, Stallard/Balachandran on mRNA vaccines, Tempero on KRAS G12D, Pancreatic Cancer Action Network advocate quote, Andrew on LLMs in cancer care, Zitu on LLMs in cancer research

Note: the file contains plain-text section markers between blocks ("INTRODUCTION", "PAPER", "Quotes") which are not BibTeX entries themselves and should be ignored when parsing — they serve only as visual section dividers in the source file.

```bibtex
% Begin Introduction
@article{Naik_Prather_Gurda, title={Synchronous Bilateral Breast Cancer: A Case Report Piloting and Evaluating the Implementation of the AI-Powered Large Language Model (LLM) ChatGPT}, volume={15}, ISSN={2168-8184}, url={https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10183235/}, DOI={10.7759/cureus.37587}, number={4}, journal={Cureus}, author={Naik, Himani R and Prather, Andrew D and Gurda, Grzegorz T}, pages={e37587}, year={2023} }

@article{Tariq_Luo_Urooj_Das_Jeong_Trivedi_Patel_Banerjee_2024, title={Domain-specific LLM Development and Evaluation – A Case-study for Prostate Cancer}, rights={© 2024, Posted by Cold Spring Harbor Laboratory. This pre-print is available under a Creative Commons License (Attribution 4.0 International), CC BY 4.0, as described at http://creativecommons.org/licenses/by/4.0/}, url={https://www.medrxiv.org/content/10.1101/2024.03.15.24304362v3}, DOI={10.1101/2024.03.15.24304362}, journal={medRxiv}, author={Tariq, Amara and Luo, Man and Urooj, Aisha and Das, Avisha and Jeong, Jiwoong and Trivedi, Shubham and Patel, Bhavik and Banerjee, Imon}, year={2024}, month=mar, language={en} }

@article{Li_Huang_Yeung_Blaes_Johnson_Liu_Xu_Zhang_2024, title={CancerLLM: A Large Language Model in Cancer Domain}, url={http://arxiv.org/abs/2406.10459}, DOI={10.48550/arXiv.2406.10459}, note={arXiv:2406.10459}, number={arXiv:2406.10459}, journal={arXiv}, author={Li, Mingchen and Huang, Jiatan and Yeung, Jeremy and Blaes, Anne and Johnson, Steven and Liu, Hongfang and Xu, Hua and Zhang, Rui}, year={2024}, month=sep }


@article{gilbert2024using,
  title={Using a Large Language Model (LLM) for Automated Extraction of Discrete Elements from Clinical Notes for Creation of Cancer Databases},
  author={Gilbert, M and Crutchfield, A and Luo, B and Thind, K and Ghanem, AI and Siddiqui, F},
  journal={International Journal of Radiation Oncology, Biology, Physics},
  volume={120},
  number={2},
  pages={e625},
  year={2024},
  url={https://www.redjournal.org/article/S0360-3016(24)02137-0/},
  publisher={Elsevier}
}

@inproceedings{Kim_Lee_Park_Eo_Youn_Lee_Hwang_2024, address={Cham}, title={LLM-Guided Multi-modal Multiple Instance Learning for 5-Year Overall Survival Prediction of Lung Cancer}, ISBN={9783031723841}, DOI={10.1007/978-3-031-72384-1_23}, booktitle={Medical Image Computing and Computer Assisted Intervention – MICCAI 2024}, publisher={Springer Nature Switzerland}, author={Kim, Kyungwon and Lee, Yongmoon and Park, Doohyun and Eo, Taejoon and Youn, Daemyung and Lee, Hyesang and Hwang, Dosik}, editor={Linguraru, Marius George and Dou, Qi and Feragen, Aasa and Giannarou, Stamatia and Glocker, Ben and Lekadir, Karim and Schnabel, Julia A.}, year={2024}, pages={239–249}, language={en}, url={https://link.springer.com/chapter/10.1007/978-3-031-72384-1_23}}

@article{Li_Zheng_Li_Dai_Wang_Chen_2024, title={LKAN: LLM-Based Knowledge-Aware Attention Network for Clinical Staging of Liver Cancer}, ISSN={2168-2208}, url={https://ieeexplore.ieee.org/abstract/document/10713996/authors#authors}, DOI={10.1109/JBHI.2024.3478809}, journal={IEEE Journal of Biomedical and Health Informatics}, author={Li, Ya and Zheng, Xuecong and Li, Jiaping and Dai, Qingyun and Wang, Chang-Dong and Chen, Min}, year={2024}, pages={1–14} }

@inproceedings{Gubanov_Pyayt_Karolak_2024, address={New York, NY, USA}, series={CIKM ’24}, title={CancerKG.ORG - A Web-scale, Interactive, Verifiable Knowledge Graph-LLM Hybrid for Assisting with Optimal Cancer Treatment and Care}, ISBN={9798400704369}, url={https://dl.acm.org/doi/10.1145/3627673.3680094}, DOI={10.1145/3627673.3680094}, booktitle={Proceedings of the 33rd ACM International Conference on Information and Knowledge Management}, publisher={Association for Computing Machinery}, author={Gubanov, Michael and Pyayt, Anna and Karolak, Aleksandra}, year={2024}, month=oct, pages={4497–4505}, collection={CIKM ’24} }

@article{Oh_Park_Byun_Cho_Lee_Kim_Ye_2024, title={LLM-driven multimodal target volume contouring in radiation oncology}, volume={15}, rights={2024 The Author(s)}, ISSN={2041-1723}, url={https://www.nature.com/articles/s41467-024-53387-y}, DOI={10.1038/s41467-024-53387-y}, number={1}, journal={Nature Communications}, author={Oh, Yujin and Park, Sangjoon and Byun, Hwa Kyung and Cho, Yeona and Lee, Ik Jae and Kim, Jin Sung and Ye, Jong Chul}, year={2024}, month=oct, pages={9186}, language={en} }

@article{khanmohammadi2024novel,
  title={A Novel Localized Student-Teacher LLM for Enhanced Toxicity Extraction in Radiation Oncology},
  author={Khanmohammadi, R and Ghanem, AI and Verdecchia, K and Hall, R and Elshaikh, MA and Movsas, B and Bagher-Ebadian, H and Chetty, IJ and Ghassemi, MM and Thind, K},
  journal={International Journal of Radiation Oncology, Biology, Physics},
  volume={120},
  number={2},
  pages={e632--e633},
  year={2024},
  url={https://www.redjournal.org/article/S0360-3016(24)02154-0/fulltext},
  publisher={Elsevier}
}

@article{Iivanainen_Lagus_Viertolahti_Sippola_Koivunen_2024, title={Investigating large language model (LLM) performance using in-context learning (ICL) for interpretation of ESMO and NCCN guidelines for lung cancer.}, volume={42}, ISSN={0732-183X, 1527-7755}, url={https://ascopubs.org/doi/10.1200/JCO.2024.42.16_suppl.e13637}, DOI={10.1200/JCO.2024.42.16_suppl.e13637}, number={16}, journal={Journal of Clinical Oncology}, author={Iivanainen, Sanna and Lagus, Jarkko and Viertolahti, Henri and Sippola, Lauri and Koivunen, Jussi}, year={2024}, month=jun, pages={e13637–e13637}, language={en} }

@article{Hao_Holmes_Waddle_Yu_Vickers_Preston_Margolin_Löckenhoff_Vashistha_Ghassemi_et_al._2024, title={Outlining the Borders for LLM Applications in Patient Education: Developing an Expert-in-the-Loop LLM-Powered Chatbot for Prostate Cancer Patient Education}, url={http://arxiv.org/abs/2409.19100}, DOI={10.48550/arXiv.2409.19100}, note={arXiv:2409.19100}, number={arXiv:2409.19100}, journal={arXiv}, author={Hao, Yuexing and Holmes, Jason and Waddle, Mark and Yu, Nathan and Vickers, Kirstin and Preston, Heather and Margolin, Drew and Löckenhoff, Corinna E. and Vashistha, Aditya and Ghassemi, Marzyeh and Kalantari, Saleh and Liu, Wei}, year={2024}, month=sep }

@article{benary2023leveraging,
  title={Leveraging large language models for decision support in personalized oncology},
  author={Benary, Manuela and Wang, Xing David and Schmidt, Max and Soll, Dominik and Hilfenhaus, Georg and Nassir, Mani and Sigler, Christian and Kn{\"o}dler, Maren and Keller, Ulrich and Beule, Dieter and others},
  journal={JAMA Network Open},
  volume={6},
  number={11},
  pages={e2343689--e2343689},
  year={2023},
  url={https://jamanetwork.com/journals/jamanetworkopen/article-abstract/2812097},
  publisher={American Medical Association}
}

@article{Bibault_Wu_2024, title={A web-based, LLM-powered AI symptom summarization tool (ASST) for monitoring of breast cancer treatment toxicity.}, volume={42}, ISSN={0732-183X, 1527-7755}, url={https://ascopubs.org/doi/10.1200/JCO.2024.42.16_suppl.e13622}, DOI={10.1200/JCO.2024.42.16_suppl.e13622}, number={16}, journal={Journal of Clinical Oncology}, author={Bibault, Jean-Emmanuel and Wu, David Jh}, year={2024}, month=jun, pages={e13622–e13622}, language={en} }

@article{Das_Maheswari_Siddiqui_Arora_Paul_Nanshi_Udbalkar_Sarvade_Chaturvedi_Shvartsman_et_al._2024, title={Improved precision oncology question-answering using agentic LLM}, rights={© 2024, Posted by Cold Spring Harbor Laboratory. The copyright holder for this pre-print is the author. All rights reserved. The material may not be redistributed, re-used or adapted without the author’s permission.}, url={https://www.medrxiv.org/content/10.1101/2024.09.20.24314076v2}, DOI={10.1101/2024.09.20.24314076}, journal={medRxiv}, author={Das, Rangan and Maheswari, K. and Siddiqui, Shaheen and Arora, Nikita and Paul, Ankush and Nanshi, Jeet and Udbalkar, Varun and Sarvade, Apoorva and Chaturvedi, Harsha and Shvartsman, Tammy and Masih, Shet and Thippeswamy, R. and Patil, Shekar and Nirni, S. S. and Garsson, Brian and Bandyopadhyay, Sanghamitra and Maulik, Ujjwal and Farooq, Mohammed and Sengupta, Debarka}, year={2024}, month=oct, language={en} }

@article{Lammert_Dreyer_Mathes_Kuligin_Borm_Schatz_Kiechle_Lörsch_Jung_Lange_et_al._2024, title={Expert-Guided Large Language Models for Clinical Decision Support in Precision Oncology}, ISSN={2473-4284}, url={https://ascopubs.org/doi/10.1200/PO-24-00478}, DOI={10.1200/PO-24-00478}, number={8}, journal={JCO Precision Oncology}, author={Lammert, Jacqueline and Dreyer, Tobias and Mathes, Sonja and Kuligin, Leonid and Borm, Kai J. and Schatz, Ulrich A. and Kiechle, Marion and Lörsch, Alisa M. and Jung, Johannes and Lange, Sebastian and Pfarr, Nicole and Durner, Anna and Schwamborn, Kristina and Winter, Christof and Ferber, Dyke and Kather, Jakob Nikolas and Mogler, Carolin and Illert, Anna L. and Tschochohei, Maximilian}, year={2024}, month=oct, pages={e2400478}, language={en} }

@article{Park_Patterson_Acitores_Cortina_Gu_Hur_Tatonetti_2024, address={Rochester, NY}, type={SSRN Scholarly Paper}, journal={SSRN}, title={Enhancing Early Detection of Pancreatic Cancer by Leveraging Llm Embeddings in Ehr-Based Prediction Models}, url={https://papers.ssrn.com/abstract=4905373}, number={4905373}, author={Park, Jiheum and Patterson, Jason and Acitores Cortina, Jose M. and Gu, Tian and Hur, Chin and Tatonetti, Nicholas}, year={2024}, month=jul, language={en} }

@article{Hao_Holmes_Hobson_Bennett_Ebner_Routman_Shiraishi_Patel_Yu_Hallemeier_et_al._2024, title={Retrospective Comparative Analysis of Prostate Cancer In-Basket Messages: Responses from Closed-Domain LLM vs. Clinical Teams}, url={http://arxiv.org/abs/2409.18290}, DOI={10.48550/arXiv.2409.18290}, note={arXiv:2409.18290}, number={arXiv:2409.18290}, journal={arXiv}, author={Hao, Yuexing and Holmes, Jason M. and Hobson, Jared and Bennett, Alexandra and Ebner, Daniel K. and Routman, David M. and Shiraishi, Satomi and Patel, Samir H. and Yu, Nathan Y. and Hallemeier, Chris L. and Ball, Brooke E. and Waddle, Mark R. and Liu, Wei}, year={2024}, month=sep }

@article{Griewing_Gremke_Wagner_Lingenfelder_Kuhn_Boekhoff_2023, title={Challenging ChatGPT 3.5 in Senology—An Assessment of Concordance with Breast Cancer Tumor Board Decision Making}, volume={13}, rights={http://creativecommons.org/licenses/by/3.0/}, ISSN={2075-4426}, url={https://www.mdpi.com/2075-4426/13/10/1502}, DOI={10.3390/jpm13101502}, number={10}, journal={Journal of Personalized Medicine}, author={Griewing, Sebastian and Gremke, Niklas and Wagner, Uwe and Lingenfelder, Michael and Kuhn, Sebastian and Boekhoff, Jelena}, year={2023}, month=oct, pages={1502}, language={en} }

@article{Alasker_Alsalamah_Alshathri_Almansour_Alsalamah_Alghafees_AlKhamees_Alsaikhan_2024, title={Performance of large language models (LLMs) in providing prostate cancer information}, volume={24}, ISSN={1471-2490}, url={https://doi.org/10.1186/s12894-024-01570-0}, DOI={10.1186/s12894-024-01570-0}, number={1}, journal={BMC Urology}, author={Alasker, Ahmed and Alsalamah, Seham and Alshathri, Nada and Almansour, Nura and Alsalamah, Faris and Alghafees, Mohammad and AlKhamees, Mohammad and Alsaikhan, Bader}, year={2024}, month=aug, pages={177}, language={en} }

@article{Sorin_Glicksberg_Artsi_Barash_Konen_Nadkarni_Klang_2024, title={Utilizing large language models in breast cancer management: systematic review}, volume={150}, ISSN={1432-1335}, url={https://doi.org/10.1007/s00432-024-05678-6}, DOI={10.1007/s00432-024-05678-6}, number={3}, journal={Journal of Cancer Research and Clinical Oncology}, author={Sorin, Vera and Glicksberg, Benjamin S. and Artsi, Yaara and Barash, Yiftach and Konen, Eli and Nadkarni, Girish N. and Klang, Eyal}, year={2024}, month=mar, pages={140}, language={en} }

@article{Sorin_Glicksberg_Barash_Konen_Nadkarni_Klang_2023, title={Applications of Large Language Models (LLMs) in Breast Cancer Care}, rights={© 2023, Posted by Cold Spring Harbor Laboratory. The copyright holder for this pre-print is the author. All rights reserved. The material may not be redistributed, re-used or adapted without the author’s permission.}, url={https://www.medrxiv.org/content/10.1101/2023.11.04.23298081v1}, DOI={10.1101/2023.11.04.23298081}, journal={medRxiv}, author={Sorin, Vera and Glicksberg, Benjamin S. and Barash, Yiftach and Konen, Eli and Nadkarni, Girish and Klang, Eyal}, year={2023}, month=nov, language={en} }

@inproceedings{Manjunath_Lerner_Dunn_2024, address={Cham}, title={Towards Interactive and Interpretable Image Retrieval-Based Diagnosis: Enhancing Brain Tumor Classification with LLM Explanations and Latent Structure Preservation}, ISBN={9783031665356}, DOI={10.1007/978-3-031-66535-6_35}, booktitle={Artificial Intelligence in Medicine}, publisher={Springer Nature Switzerland}, author={Manjunath, Pranav and Lerner, Brian and Dunn, Timothy}, editor={Finkelstein, Joseph and Moskovitch, Robert and Parimbelli, Enea}, year={2024}, pages={335–349}, language={en} }

@article{Lammert_Dreyer_Lörsch_Jung_Lange_Pfarr_Durner_Kiechle_Schatz_Mathes, title={Large language models for precision oncology: Clinical decision support through expert-guided learning.}, volume={42}, ISSN={0732-183X, 1527-7755}, url={https://ascopubs.org/doi/10.1200/JCO.2024.42.16_suppl.e13609}, DOI={10.1200/JCO.2024.42.16_suppl.e13609}, number={16}, journal={Journal of Clinical Oncology}, author={Lammert, Jacqueline and Dreyer, Tobias F. and Lorsch, Alisa M. and Jung, Johannes and Lange, Sebastian and Pfarr, Nicole and Durner, Anna and Kiechle, Marion B. and Schatz, Ulrich A. and Mathes, Sonja and Schwamborn, Kristina and Winter, Christof and Mogler, Carolin and Illert, Anna Lena and Tschochohei, Maximilian}, year={2024}, month=jun, pages={e13609–e13609}, language={en} }

@article{Choi_Song_Shin_Chang_Jang_2023, title={Developing prompts from large language model for extracting clinical information from pathology and ultrasound reports in breast cancer}, volume={41}, ISSN={2234-1900}, url={https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10556835/}, DOI={10.3857/roj.2023.00633}, number={3}, journal={Radiation Oncology Journal}, author={Choi, Hyeon Seok and Song, Jun Yeong and Shin, Kyung Hwan and Chang, Ji Hyun and Jang, Bum-Sup}, year={2023}, month=sep, pages={209–216} }

@article{longwell2024performance,
  title={Performance of Large Language Models on Medical Oncology Examination Questions},
  author={Longwell, Jack B and Hirsch, Ian and Binder, Fernando and Conchas, Galileo Arturo Gonzalez and Mau, Daniel and Jang, Raymond and Krishnan, Rahul G and Grant, Robert C},
  journal={JAMA Network Open},
  volume={7},
  number={6},
  pages={e2417641--e2417641},
  year={2024},
  url={https://jamanetwork.com/journals/jamanetworkopen/article-abstract/2820094},
  publisher={American Medical Association}
}


@article{Yang_Xu_2024, title={LLM4THP: a computing tool to identify tumor homing peptides by molecular and sequence representation of large language model based on two-layer ensemble model strategy}, volume={56}, ISSN={1438-2199}, url={https://doi.org/10.1007/s00726-024-03422-5}, DOI={10.1007/s00726-024-03422-5}, number={1}, journal={Amino Acids}, author={Yang, Sen and Xu, Piao}, year={2024}, month=oct, pages={62}, language={en} }

@inproceedings{Ahmad_Mamatjan_Wali_Mamatjan_2024, title={The Development of CanPrompt Strategy in Large Language Models for Cancer Care}, ISSN={2994-9408}, url={https://ieeexplore.ieee.org/abstract/document/10702147}, DOI={10.1109/CIBCB58642.2024.10702147}, booktitle={2024 IEEE Conference on Computational Intelligence in Bioinformatics and Computational Biology (CIBCB)}, author={Ahmad, Noman and Mamatjan, Ehsan and Wali, Tursun and Mamatjan, Yasin}, year={2024}, month=aug, pages={1–6} }

@article{Sun_Zhang_Lu_Qin_Gou_Guo_Peng_Zhang_Yang_Liu_et_al._2023, title={Large language models completely understand molecular characteristics of squamous cervical cancer}, url={https://www.researchsquare.com/article/rs-2855719/v1}, DOI={10.21203/rs.3.rs-2855719/v1}, author={Sun, Chaoyang and Zhang, Weizhi and Lu, Funian and Qin, Tianyu and Gou, Yujie and Guo, Ensong and Peng, Di and Zhang, Li and Yang, Bin and Liu, Si and Han, Cheng and Fu, Shanshan and Song, Kun and Xia, Bairong and Zou, Dongling and Shen, Yuanming and Huang, He and Zhou, Shengtao and Yuan, Cunzhong and Shu, Yao and Pi, Yanan and Wang, Shuxiang and Chen, Wenjuan and Wang, Haixia and Zhong, Lin and Yuan, Li and Wen, Baogang and Yang, Siqi and Wan, Ting and Fan, Junpeng and Fu, Yu and Liu, Dan and Xiao, Rourou and Zhang, Chi and Wei, Yuxiang and Peng, Wenju and Huang, Xinhe and Wang, Beibei and Wu, Peng and Kong, Beihua and Mills, Gordon and Ma, Ding and Chen, Gang and Xue, Yu}, year={2023}, month=may, journal={Research Square} }

@article{Pan_Withnell_Secrier_2024, title={Classifying epithelial-mesenchymal transition states in single cell cancer data using large language models}, rights={© 2024, Posted by Cold Spring Harbor Laboratory. This pre-print is available under a Creative Commons License (Attribution-NonCommercial 4.0 International), CC BY-NC 4.0, as described at http://creativecommons.org/licenses/by-nc/4.0/}, url={https://www.biorxiv.org/content/10.1101/2024.08.16.608311v1}, DOI={10.1101/2024.08.16.608311}, journal={bioRxiv}, author={Pan, Shi and Withnell, Eloise and Secrier, Maria}, year={2024}, month=aug, language={en} }

@article{zack2024abstract,
  title={Abstract B074: Clinical inference of location and trajectory of pancreatic cancer from radiology reports using zero-shot LLM},
  author={Zack, Travis Ian and Sushil, Madhumita and Miao, Brenda and Demirci, Arda and Kasap, Corynn and Tempero, Margaret and Butte, Atul and Collisson, Eric},
  journal={Cancer Research},
  volume={84},
  number={2\_Supplement},
  pages={B074--B074},
  year={2024},
  url={https://aacrjournals.org/cancerres/article/84/2_Supplement/B074/732654},
  publisher={AACR}
}

@article{Yu_Wang_Wang_Wei_Pei_2024, title={Decoding Critical Targets and Signaling Pathways in EBV-Mediated Diseases Using Large Language Models}, volume={16}, rights={http://creativecommons.org/licenses/by/3.0/}, ISSN={1999-4915}, url={https://www.mdpi.com/1999-4915/16/11/1660}, DOI={10.3390/v16111660}, number={11}, journal={Viruses}, author={Yu, Jingwen and Wang, Yaohao and Wang, Haidong and Wei, Zhi and Pei, Yonggang}, year={2024}, month=nov, pages={1660}, language={en} }
% End Introduction

@misc{Gemini_2.0_Flash_Thinking_Experimental_2024, url={https://deepmind.google/technologies/gemini/flash-thinking/}, Title={Gemini 2.0 Flash Thinking Experimental is our enhanced reasoning model, capable of showing its thoughts to improve performance and explainability.}, journal={Google DeepMind}, author={Google DeepMind}, year={2024}, month=dec, language={en} }

@misc{deepseek-ai/DeepSeek-R1_2025, rights={MIT}, url={https://github.com/deepseek-ai/DeepSeek-R1}, publisher={DeepSeek}, author={DeepSeek}, year={2025}, Title={We introduce our first-generation reasoning models, DeepSeek-R1-Zero and DeepSeek-R1. DeepSeek-R1-Zero, a model trained via large-scale reinforcement learning (RL) without supervised fine-tuning (SFT) as a preliminary step, demonstrated remarkable performance on reasoning}, month=jan }


@article{An_Ma_Lin_Zheng_Lou_2024, title={Make Your LLM Fully Utilize the Context}, url={http://arxiv.org/abs/2404.16811}, DOI={10.48550/arXiv.2404.16811}, note={arXiv:2404.16811}, number={arXiv:2404.16811}, journal={arXiv}, author={An, Shengnan and Ma, Zexiong and Lin, Zeqi and Zheng, Nanning and Lou, Jian-Guang}, year={2024}, month=apr }

@inproceedings{Li_Shao_Xie_Sheng_Zheng_Gonzalez_Stoica_Ma_Zhang_2023, title={How Long Can Context Length of Open-Source LLMs truly Promise?}, url={https://openreview.net/forum?id=LywifFNXV5}, author={Li, Dacheng and Shao, Rulin and Xie, Anze and Sheng, Ying and Zheng, Lianmin and Gonzalez, Joseph and Stoica, Ion and Ma, Xuezhe and Zhang, Hao}, year={2023}, month=nov, booktitle={openreview}, language={en} }

@article{Pal_Karkhanis_Roberts_Dooley_Sundararajan_Naidu_2023, title={Giraffe: Adventures in Expanding Context Lengths in LLMs}, url={http://arxiv.org/abs/2308.10882}, DOI={10.48550/arXiv.2308.10882}, note={arXiv:2308.10882}, number={arXiv:2308.10882}, journal={arXiv}, author={Pal, Arka and Karkhanis, Deep and Roberts, Manley and Dooley, Samuel and Sundararajan, Arvind and Naidu, Siddartha}, year={2023}, month=aug }

@misc{OpenAI_GPT_o1_modelcard, url={https://openai.com/index/openai-o1-system-card/}, author={OpenAI}, year={2024}, language={en}, Title={OpenAI o1 System Card. This report outlines the safety work carried out prior to releasing OpenAI o1, including external red teaming and frontier risk evaluations according to our Preparedness Framework.} }


@misc{OpenAI_12days, url={https://openai.com/12-days/}, author={OpenAI}, year={2024}, language={en}, Title={OpenAI 12 days: o3 preview & call for safety researchers. Deliberative alignment: reasoning enables safer language models Introducing our new alignment strategy for o-series models, which are directly taught safety specifications and how to reason over them.} }

@misc{OpenAI_500, url={https://openai.com/index/announcing-the-stargate-project/}, author={OpenAI}, year={2024}, language={en}, Title={OpenAI Stargate Project. The Stargate Project is a new company which intends to invest USD 500 billion over the next four years building new AI infrastructure for OpenAI in the United States. } }



@misc{OpenAI_GPT_40_modelcard, url={https://openai.com/index/gpt-4o-system-card/}, author={OpenAI}, year={2024}, language={en}, Title={OpenAI 40 System Card. This report outlines the safety work carried out prior to releasing GPT-4o including external red teaming, frontier risk evaluations according to our Preparedness Framework, and an overview of the mitigations we built in to address key risk areas.} }

@misc{LLM_Databricks, url={https://tinyurl.com/3e7596at}, abstractNote={Learn best practices for optimizing LLM inference performance on Databricks.}, author={Databricks}, Title={LLM Inference Performance Engineering: Best Practices. Large Language Models (LLMs) generate text in a two-step process: "prefill", where the tokens in the input prompt are processed in parallel, and "decoding", where text is generated one 'token' at a time in an autoregressive manner.}, year={2023}, month=oct, language={en-US} }

@misc{A_guide_to_LLM_inference, url={https://www.baseten.co/blog/llm-transformer-inference-guide/}, abstractNote={Learn if LLM inference is compute or memory bound to fully utilize GPU power. Get insights on better GPU resource utilization.}, author={Baseten}, language={en} }

@article{Li_Jiang_Gadepally_Tiwari_2024, title={LLM Inference Serving: Survey of Recent Advances and Opportunities}, url={http://arxiv.org/abs/2407.12391}, DOI={10.48550/arXiv.2407.12391}, note={arXiv:2407.12391}, number={arXiv:2407.12391}, journal={arXiv}, author={Li, Baolin and Jiang, Yankai and Gadepally, Vijay and Tiwari, Devesh}, year={2024}, month=jul }

@article{Ferraris_Audrito_Caro_Poncibò_2025, title={The architecture of language: Understanding the mechanics behind LLMs}, volume={1}, ISSN={3033-3733}, url={https://www.cambridge.org/core/journals/cambridge-forum-on-ai-law-and-governance/article/architecture-of-language-understanding-the-mechanics-behind-llms/E3DDEFB9C04883733380E04331D6F782}, DOI={10.1017/cfl.2024.16}, journal={Cambridge Forum on AI: Law and Governance}, author={Ferraris, Andrea Filippo and Audrito, Davide and Caro, Luigi Di and Poncibò, Cristina}, year={2025}, month={jan}, pages={e11}, language={en} }

@article{Zhou_Ning_Hong_Fu_Xu_Li_Lou_Wang_Yuan_Li_et_al._2024, title={A Survey on Efficient Inference for Large Language Models}, url={http://arxiv.org/abs/2404.14294}, DOI={10.48550/arXiv.2404.14294}, note={arXiv:2404.14294}, number={arXiv:2404.14294}, journal={arXiv}, author={Zhou, Zixuan and Ning, Xuefei and Hong, Ke and Fu, Tianyu and Xu, Jiaming and Li, Shiyao and Lou, Yuming and Wang, Luning and Yuan, Zhihang and Li, Xiuhong and Yan, Shengen and Dai, Guohao and Zhang, Xiao-Ping and Dong, Yuhan and Wang, Yu}, year={2024}, month=jul }

@article{Yuan_Shang_Zhou_Dong_Zhou_Xue_Wu_Li_Gu_Lee_et_al._2024, title={LLM Inference Unveiled: Survey and Roofline Model Insights}, url={http://arxiv.org/abs/2402.16363}, DOI={10.48550/arXiv.2402.16363}, note={arXiv:2402.16363}, number={arXiv:2402.16363}, journal={arXiv}, author={Yuan, Zhihang and Shang, Yuzhang and Zhou, Yang and Dong, Zhen and Zhou, Zhe and Xue, Chenhao and Wu, Bingzhe and Li, Zhikai and Gu, Qingyi and Lee, Yong Jae and Yan, Yan and Chen, Beidi and Sun, Guangyu and Keutzer, Kurt}, year={2024}, month=may }

@article{Li_Fu_Shi_Huang_Lu_2024, title={Efficient LLMs Training and Inference: An Introduction}, ISSN={2169-3536}, url={https://ieeexplore.ieee.org/abstract/document/10756602}, DOI={10.1109/ACCESS.2024.3501358}, journal={IEEE Access}, author={Li, Rui and Fu, Deji and Shi, Chunyu and Huang, Zhilan and Lu, Gang}, year={2024}, pages={1–1} }

@article{Nazi_Hossain_Mamun_2025, title={Evaluation of open and closed-source LLMs for low-resource language with zero-shot, few-shot, and chain-of-thought prompting}, volume={10}, ISSN={2949-7191}, url={https://www.sciencedirect.com/science/article/pii/S2949719124000724}, DOI={10.1016/j.nlp.2024.100124}, journal={Natural Language Processing Journal}, author={Nazi, Zabir Al and Hossain, Md. Rajib and Mamun, Faisal Al}, year={2025}, month=mar, pages={100124} }

@article{Xu_Hao_Zong_Wang_Zhang_Wang_Lan_Gong_Ouyang_Meng_et_al._2025, title={Towards Large Reasoning Models: A Survey on Scaling LLM Reasoning Capabilities}, url={http://arxiv.org/abs/2501.09686}, DOI={10.48550/arXiv.2501.09686}, note={arXiv:2501.09686}, number={arXiv:2501.09686}, journal={arXiv}, author={Xu, Fengli and Hao, Qianyue and Zong, Zefang and Wang, Jingwei and Zhang, Yunke and Wang, Jingyi and Lan, Xiaochong and Gong, Jiahui and Ouyang, Tianjian and Meng, Fanjin and Shao, Chenyang and Yan, Yuwei and Yang, Qinglong and Song, Yiwen and Ren, Sijian and Hu, Xinyuan and Li, Yu and Feng, Jie and Gao, Chen and Li, Yong}, year={2025}, month=jan }












INTRODUCTION
INTRODUCTION
INTRODUCTION

@article{01IntroKatsoulakis, title={Digital twins for health: a scoping review}, volume={7}, rights={2024 The Author(s)}, ISSN={2398-6352}, url={https://www.nature.com/articles/s41746-024-01073-0}, DOI={10.1038/s41746-024-01073-0}, number={1}, journal={npj Digital Medicine}, author={Katsoulakis, Evangelia and Wang, Qi and Wu, Huanmei and Shahriyari, Leili and Fletcher, Richard and Liu, Jinwei and Achenie, Luke and Liu, Hongfang and Jackson, Pamela and Xiao, Ying and Syeda-Mahmood, Tanveer and Tuli, Richard and Deng, Jun}, year={2024}, month=mar, pages={1–11}, language={en} }
@misc{02IntroPhesi, url={https://www.appliedclinicaltrialsonline.com/view/a-digital-twin-on-kras-g12c-nsclc-patients-with-sca-measured-by-pfs}, abstractNote={Digital twins, defined as a typical demographic patient profile in a specific population, have the potential to help clinical trial design.}, journal={Applied Clinical Trials}, year={2022}, month=apr, language={en}, author={Applied Clinical Trials} }
@misc{03IntroPhesi, url={https://www.phesi.com/}, abstractNote={AI-driven solutions enable life sciences companies turn real world clinical trial data to their advantage, simulating clinical outcomes.}, journal={Phesi}, language={en-US}, author={Phesi} }
@misc{04IntroAltislabs, url={https://tinyurl.com/bdhjdt3v}, author={Altis Labs, Inc.} }
@article{05IntroWu, title={MRI-based digital twins to improve treatment response of breast cancer by optimizing neoadjuvant chemotherapy regimens}, volume={8}, rights={2025 The Author(s)}, ISSN={2398-6352}, url={https://www.nature.com/articles/s41746-025-01579-1}, DOI={10.1038/s41746-025-01579-1}, number={1}, journal={npj Digital Medicine}, author={Wu, Chengyue and Lima, Ernesto A. B. F. and Stowers et al.}, year={2025}, month=apr, pages={1–13}, language={en} }
@article{06IntroBordukova, title={Generative artificial intelligence empowers digital twins in drug discovery and clinical trials}, volume={19}, ISSN={1746-0441, 1746-045X}, DOI={10.1080/17460441.2023.2273839}, number={1}, journal={Expert Opinion on Drug Discovery}, author={Bordukova, Maria and Makarov, Nikita and Rodriguez-Esteban, Raul and Schmich, Fabian and Menden, Michael P.}, year={2024}, month=jan, pages={33–42}, language={en} }
@article{07IntroWang, title={TWIN-GPT: Digital Twins for Clinical Trials via Large Language Model}, ISSN={1551-6857, 1551-6865}, DOI={10.1145/3674838}, journal={ACM Transactions on Multimedia Computing, Communications, and Applications}, author={Wang, Yue and Fu, Tianfan et al.}, year={2024}, month=jul, pages={3674838}, language={en} }
@misc{08IntroFrederick, url={https://frederick.cancer.gov/node/646}, title={Digital twins have the potential to forge a path toward advances in cancer care and research.}, language={en}, author={Frederick National Laboratory} }
@misc{09IntroFrederick, url={https://bigcare.uci.edu/wp-content/uploads/sites/29/Eric_Stahlberg_BigCARELecture-Given.pdf}, title={Around the Corner:
Peering into the Future for
Personalized Precision Health}, language={en}, author={Frederick National Laboratory} }
@article{10IntroOsipov, title={The Molecular Twin artificial-intelligence platform integrates multi-omic data to predict outcomes for pancreatic adenocarcinoma patients}, volume={5}, rights={2024 The Author(s)}, ISSN={2662-1347}, url={https://www.nature.com/articles/s43018-023-00697-7}, DOI={10.1038/s43018-023-00697-7}, number={2}, journal={Nature Cancer}, author={Osipov, Arsen and Nikolic, Ognjen and Gertych et al.}, year={2024}, month=feb, pages={299–314}, language={en} }
@article{11IntroJoslyn, title={Digital twins elucidate critical role of Tscm in clinical persistence of TCR-engineered cell therapy}, volume={10}, rights={2024 The Author(s)}, ISSN={2056-7189}, url={https://www.nature.com/articles/s41540-024-00335-7}, DOI={10.1038/s41540-024-00335-7}, number={1}, journal={npj Systems Biology and Applications}, author={Joslyn, Louis R. and Huang, Weize et al.}, year={2024}, month=jan, pages={1–12}, language={en} }
@misc{12IntroNSFNIHFDA, url={https://www.nsf.gov/news/nsf-nih-fda-support-research-digital-twin-technology}, abstractNote={The U.S. National Science Foundation, in collaboration with the National Institutes of Health (NIH) and the Food and Drug Administration (FDA), has awarded over…}, year={2024}, author={U.S. National Science Foundation}, month=oct, language={en} }
@misc{13IntroNSFNIHFDA, url={https://www.linkedin.com/pulse/nsf-nih-fda-support-research-digital-twins-biomedical-buchsbaum-bciye}, abstractNote={A tri-agency working group worked hard to move this forward and reviewers per standard NSF process reviewed a lot of superb grant applications. The result of all of this teamwork and collaboration is perhaps the most fun story to share: grants were funded! This was just released today! $6 million in}, language={en}, author={Jeffrey Buchsbaum} }


PAPER
PAPER
PAPER
@article{01PaperBehrouz, title={Titans: Learning to Memorize at Test Time}, url={http://arxiv.org/abs/2501.00663}, DOI={10.48550/arXiv.2501.00663}, note={arXiv:2501.00663}, number={arXiv:2501.00663}, publisher={arXiv}, author={Behrouz, Ali and Zhong, Peilin and Mirrokni, Vahab}, year={2024}, journal={arXiv}, month=dec }

Quotes
Quotes
Quotes
@article{01QuoteHalbrook, title={Pancreatic Cancer: Advances and Challenges}, volume={186}, ISSN={0092-8674}, url={https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10182830/}, DOI={10.1016/j.cell.2023.02.014}, number={8}, journal={Cell}, author={Halbrook, Christopher J. and Lyssiotis, Costas A. and Pasca di Magliano, Marina and Maitra, Anirban}, year={2023}, month=apr, pages={1729–1754} }
@article{02QuoteMukund, title={Pancreatic Ductal Adenocarcinoma (PDAC): A Review of Recent Advancements Enabled by Artificial Intelligence}, volume={16}, ISSN={2072-6694}, url={https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11201559/}, DOI={10.3390/cancers16122240}, number={12}, journal={Cancers}, author={Mukund, Ashwin and Afridi, Muhammad Ali and Karolak, Aleksandra and Park, Margaret A. and Permuth, Jennifer B. and Rasool, Ghulam}, year={2024}, month=jun, pages={2240} }
@article{03QuoteUrooj, title={FDA endorses NALIRIFOX for metastatic pancreatic adenocarcinoma: an editorial}, volume={86}, ISSN={2049-0801}, url={https://journals.lww.com/10.1097/MS9.0000000000002564}, DOI={10.1097/MS9.0000000000002564}, number={10}, journal={Annals of Medicine & Surgery}, author={Urooj, Wajiha and Ahmed, Bisma et al.}, year={2024}, month=oct, pages={5685–5687}, language={en} }
@misc{04QuoteStallard, title={In Early-Phase Pancreatic Cancer Clinical Trial, Investigational mRNA Vaccine Induces Sustained Immune Activity in Small Patient Group | Memorial Sloan Kettering Cancer Center}, url={https://www.mskcc.org/news/can-mrna-vaccines-fight-pancreatic-cancer-msk-clinical-researchers-are-trying-find-out}, abstractNote={Learn how MSK researchers are deploying mRNA vaccines against pancreatic cancer.}, author={Stallard, Jim}, year={2025}, month=feb, language={en} }
@misc{05QuoteTempero, url={https://www.ucsf.edu/news/2024/03/427231/can-new-drug-candidate-cure-pancreatic-cancer}, abstractNote={A new drug candidate permanently modifies a wily cancer-causing mutation, paving the way for making pancreatic cancer treatable, or perhaps even curable.}, year={2024}, month=mar, language={en}, author={University of California San Francisco} }
@misc{06QuotePanCan, title={Survivors Share Words of Inspiration, Hope}, url={https://pancan.org/news/survivors-favorite-quotes/}, abstractNote={Check out some favorite quotes form pancreatic cancer survivors.}, journal={Pancreatic Cancer Action Network}, author={Axelrod, Alexandra}, year={2017}, month=dec, language={en} }
@article{07QuoteAndrew, title={Large language models for improving cancer diagnosis and management in primary health care settings}, volume={4}, ISSN={2949-916X}, DOI={10.1016/j.glmedi.2024.100157}, journal={Journal of Medicine, Surgery, and Public Health}, author={Andrew, Albert and Tizzard, Ethan}, year={2024}, month=dec, pages={100157} }
@article{08QuoteZitu, title={Large language models in cancer: potentials, risks, and safeguards}, volume={2}, ISSN={2976-8705}, url={https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11703354/}, DOI={10.1093/bjrai/ubae019}, number={1}, journal={Bjr Artificial Intelligence}, author={Zitu, Md Muntasir and Le, Tuan Dung et al.}, year={2024}, month=dec, pages={ubae019} }
```
