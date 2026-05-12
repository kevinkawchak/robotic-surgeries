# References - Part 1 of 2 (BibTeX Entries)

This chunk contains the first half of the BibTeX entries from references.bib. These entries cover: AI tools/platforms (Claude, ChatGPT, Gemini, Grok, Meta AI), the author Kawchak's prior Zenodo/ChemRxiv/bioRxiv publications, GitHub repositories, software tools (Google Colab, Google Docs, VS Code, LangChain, AutoGen, CrewAI), foundational LLM/agent papers, and biopharmaceutical and bioprocess engineering references. Cite keys here are referenced throughout the paper main text by their handle, including:

- AI models: `ChatGPTo3`, `ChatGPTo3Card`, `ChatGPTo3pro`, `ChatGPTo3pro2`, `Sonnet4`, `Opus4`, `Claude4`, `Grok3`, `Gemini25ProPreview0605`, `Gemini25Pro`, `OpenAI_GPT-4o`, `MetaAI`
- Platforms: `Google_AI_Studio`, `GoogleColab`, `GoogleDocs`, `Visual_Studio_Code`
- Author prior works: `15KawchakAgent`, `16KawchakLung`, `17KawchakGlioblastoma`, `18KawchakPDAC` (this paper)
- Code repositories: `GitHub24Jun25` (PDAC DT code), `GitHub23Mar25`, `GitHub24Apr25`, `GitHub29May25`
- Foundational paper cited in Reports section: `01PaperBehrouz` (Titans memory paper — though note this entry actually appears in the INTRODUCTION block of Part 2, this Part 1 chunk does not contain that exact entry)

These references support Chunks 02 (Methods/Software), 03 (Results: Reports — context recall claim), and the Data Availability section in Chunk 08.

```bibtex


@misc{Claude, url={https://claude.ai/}, title={Talk with Claude, an AI assistant from Anthropic. Introducing Project.}, year={2024}, author={Claude}, language={en} }

@misc{ChatGPT_2024, url={https://apps.apple.com/us/app/chatgpt/id6448311069}, title={Introducing ChatGPT for iOS OpenAI’s latest advancements at your fingertips.}, author={ChatGPT}, journal={App Store}, year={2024}, month={aug}, language={en-US} }

@misc{OpenAI_GPT-4o, url={https://platform.openai.com/docs/models/gpt-4o}, author={OpenAI}, year={2024}, language={en}, Title={OpenAI Flagship Models. Our versatile, high-intelligence flagship model. Text and image input, text output. 128k context length. Smarter model, higher price per token} }

@misc{OpenAI_GPT-o1, url={https://openai.com/chatgpt/pricing/}, author={OpenAI}, year={2024}, language={en}, Title={OpenAI o1 Pricing. Get the best of OpenAI with the highest level of access. Everything in Plus. Unlimited access to o1, o1-mini, GPT-4o, and voice (audio only.) Higher limits for video and screensharing in voice.} }

@misc{o3mini, url={https://openai.com/index/openai-o3-mini/}, author={OpenAI}, year={2025}, language={en}, Title={OpenAI o3-mini} }

@misc{o3minicard, url={https://openai.com/index/o3-mini-system-card/}, author={OpenAI}, year={2025}, language={en}, Title={OpenAI o3-mini System Card} }

@misc{ChatGPTo3, url={https://openai.com/index/introducing-o3-and-o4-mini/}, author={OpenAI}, year={2025}, language={en}, Title={Introducing OpenAI o3 and o4-mini}}

@misc{ChatGPTo3Card, url={https://openai.com/index/o3-o4-mini-system-card/}, author={OpenAI}, year={2025}, language={en}, Title={OpenAI o3 and o4-mini System Card. Read the System Card}}

@misc{ChatGPTo3pro, url={https://community.openai.com/t/o3-is-80-cheaper-and-introducing-o3-pro/1284925}, author={OpenAI}, year={2025}, month={June}, language={en}, Title={O3 is 80% cheaper and introducing o3-pro}}

@misc{ChatGPTo3pro2, url={https://platform.openai.com/docs/models/o3-pro}, author={OpenAI}, year={2025}, month={June}, language={en}, Title={o3-pro | Version of o3 with more compute for better responses}}


@misc{MetaAI, url={https://www.meta.ai/}, author={Meta AI}, year={2025}, month={June}, language={en}, Title={Meta AI Chat Interface}}




@misc{GPT4.5, url={https://openai.com/index/introducing-gpt-4-5/}, author={OpenAI}, year={2025}, language={en}, Title={Introducing GPT-4.5} }

@misc{GPT4.5Card, url={https://openai.com/index/gpt-4-5-system-card/}, author={OpenAI}, year={2025}, language={en}, Title={OpenAI GPT-4.5 System Card} }

@misc{Grok3, url={https://x.ai/news/grok-3}, author={xAI}, year={2025}, language={en}, Title={Grok 3 Beta — The Age of Reasoning Agents} }

@misc{GoogleColab, url={https://colab.research.google.com/}, language={en}, author={Google Colab}}

@misc{Visual_Studio_Code, url={https://code.visualstudio.com/}, abstractNote={Visual Studio Code redefines AI-powered coding with GitHub Copilot for building and debugging modern web and cloud applications. Visual Studio Code is free and available on your favorite platform - Linux, macOS, and Windows.}, author={Visual Studio Code}, language={en} }

@misc{GoogleDocs, title={Google Docs: Online Document & PDF Editor}, url={https://workspace.google.com/products/docs/}, abstractNote={Create online documents and edit PDFs with Google Docs. Collaborate in real-time from any device and use AI to generate drafts, templates, and more.}, journal={Google Workspace}, author={Workspace, Google}, language={en} }

@misc{Sequoia, url={https://www.youtube.com/watch?v=sal78ACtGTc}, title={What's next for AI agentic workflows ft. Andrew Ng of AI Fund}, author={Sequoia Capital}}

@misc{LangChain, url={https://www.langchain.com/}, abstractNote={LangChain’s suite of products supports developers along each step of their development journey.}, author={LangChain}, language={en} }

@misc{AutoGen, url={https://microsoft.github.io/autogen/stable//index.html}, abstractNote={Top-level documentation for AutoGen, a framework for developing applications using AI agents }, author={AutoGen} }

@misc{CrewAI, url={https://www.crewai.com/}, author={CrewAI} }

@misc{WSJ, url={https://www.youtube.com/watch?v=-mIjwN1o7nE}, title={Andrew Ng on AI's Potential Effect on the Labor Force | WSJ}, author={WSJ News}}

@misc{o1Prompt, url={https://x.com/daniel_mac8/status/1878283032215408886}, title={The Anatomy of an o1 Prompt}, author={@benhylak}}

@misc{Claude_web, url={https://www.anthropic.com/news/web-search}, abstractNote={You can now use Claude to search the internet to provide more up-to-date and relevant responses.}, language={en}, author={Claude} }


@misc{KawchakAgents, url={https://www.youtube.com/watch?v=vyOtowbGwG0&t=247s}, title={Cancer Drug Discovery AI Agentic Workflow R&D}, author={ChemicalQDevice}}


@misc{deepresearch, url={https://openai.com/index/introducing-deep-research/}, author={OpenAI}, year={2025}, language={en}, Title={Introducing deep research. An agent that uses reasoning to synthesize large amounts of online information and complete multi-step research tasks for you. Available to Pro users today, Plus and Team next.} }

@misc{GeminiGoogle, url={https://gemini.google.com}, Note={Get help with writing, planning, learning, and more from Google AI.}, journal={Gemini}, language={en-US} }


@misc{Google_AI_Studio, url={https://aistudio.google.com/prompts/new_chat}, author={Google AI Studio}, year={2025}, title={What will you build? Push Gemini to the limits of what AI can do, powered by the Gemini API. This experimental model is for feedback and testing only. No production use.} }

@misc{Gemini25ProPreview0605, url={https://blog.google/products/gemini/gemini-2-5-pro-latest-preview/}, author={Google AI Studio}, year={2025}, month={june}, title={Try the latest Gemini 2.5 Pro before general availability.}}

@misc{Gemini25Pro, url={https://blog.google/products/gemini/gemini-2-5-model-family-expands/}, author={Google AI Studio}, year={2025}, month={june}, title={We’re expanding our Gemini 2.5 family of models}}



@misc{Google_Scholar, url={https://scholar.google.com/}, Title={Google Scholar provides a simple way to broadly search for scholarly literature. Search across a wide variety of disciplines and sources: articles, theses, books, abstracts and court opinions.}, author={Google Scholar} }


@misc{Claude_3.5_Sonnet, url={https://www.anthropic.com/news/claude-3-5-sonnet}, abstractNote={Introducing Claude 3.5 Sonnet—our most intelligent model yet. Sonnet now outperforms competitor models and Claude 3 Opus on key evaluations, at twice the speed.}, author={Claude}, language={en} }

@misc{Claude_3.5_Sonnet_New, url={https://www.anthropic.com/news/3-5-models-and-computer-use}, Title={Introducing computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku}, language={en}, author={Claude} }

@misc{Claude_3.7_Sonnet, url={https://www.anthropic.com/news/claude-3-7-sonnet}, Title={Claude 3.7 Sonnet and Claude Code. Feb 24, 2025}, language={en}, author={Claude} }

@misc{Claude_3.7_Sonnet_2, url={https://www.anthropic.com/claude/sonnet}, Title={Claude 3.7 Sonnet Hybrid reasoning model}, language={en}, author={Claude} }

@misc{Claude4Sonnet, url={https://www.anthropic.com/news/claude-4}, Title={Introducing Claude 4}, language={en}, author={Claude}}

@misc{Sonnet4, url={https://www.anthropic.com/claude/sonnet}, Title={Claude Sonnet 4 Hybrid reasoning model with superior intelligence for high-volume use cases, and 200K context window}, language={en}, author={Claude}}

@misc{Claude4, url={https://www.anthropic.com/news/claude-4}, Title={Introducing Claude 4}, language={en}, author={Claude}}

@misc{Opus4, url={https://www.anthropic.com/claude/opus}, Title={Hybrid reasoning model that pushes the frontier for coding and AI agents, featuring a 200K context window}, language={en}, author={Claude}}


@misc{01Kawchak_Kevin_10Jul24, author = {Kawchak, Kevin}, 
  title        = {Large Language Models for Early Phase GenAI Drug Discovery, Large Language Model (LLM) performance for drug discovery applications.},
  year         = {2024},
  url          = {https://doi.org/10.5281/zenodo.14967943},   
  doi          = {10.5281/zenodo.14967943},                  
  publisher    = {Zenodo},
  organization = {ChemicalQDevice},
  language     = {en},
}

@misc{02Kawchak_Kevin_18Jul24, author = {Kawchak, Kevin},
  title        = {Extra Large Language Models Benchmarking for Medicinal Chemistry},
  year         = {2024},
  url          = {https://doi.org/10.5281/zenodo.14968018},    
  doi          = {10.5281/zenodo.14968018},                   
  publisher    = {Zenodo},
  organization = {ChemicalQDevice},
  language     = {en},
}

@misc{03Kawchak_Kevin_23Jul24, author = {Kawchak, Kevin},
  title        = {LLM-Retrieval Augmented Generation for Drug Shortages},
  year         = {2024},
  url          = {https://doi.org/10.5281/zenodo.14968072},    
  doi          = {10.5281/zenodo.14968072},                   
  publisher    = {Zenodo},
  organization = {ChemicalQDevice},
  language     = {en},
}

@misc{04Kawchak_Kevin_01Aug24, author = {Kawchak, Kevin},
  title        = {Total Synthesis Guidance for Chemists},
  year         = {2024},
  url          = {https://doi.org/10.5281/zenodo.14968133},    
  doi          = {10.5281/zenodo.14968133},                   
  publisher    = {Zenodo},
  organization = {ChemicalQDevice},
  language     = {en},
}

@article{05kawchak2024lmm,
  title={LMM Chemical Research with Document Retrieval}, url={https://doi.org/10.26434/chemrxiv-2024-p91gm}, DOI={10.26434/chemrxiv-2024-p91gm}, publisher={ChemRxiv}, journal={ChemRxiv}, author={Kawchak, Kevin}, year={2024}, month=aug, language={en} }


@article{06Kawchak_2024_LMM_Determination, title={LMM Spectrometric Determination of an Organic Compound}, url={https://doi.org/10.26434/chemrxiv-2024-qtnkj}, DOI={10.26434/chemrxiv-2024-qtnkj}, publisher={ChemRxiv}, author={Kawchak, Kevin}, year={2024}, month=aug, language={en}, journal={ChemRxiv} }


@article{07kawchak2024C15,
  title={High Dimensional and Complex Spectrometric Data Analysis of an Organic Compound using Large Multimodal Models and Chained Outputs}, url={https://doi.org/10.26434/chemrxiv-2024-06gf1}, DOI={10.26434/chemrxiv-2024-06gf1}, publisher={ChemRxiv}, journal={ChemRxiv}, author={Kawchak, Kevin}, year={2024}, month=sep, language={en} }

@article{08kawchak2024Paclitaxel,
  title={Paclitaxel Biosynthesis AI Breakthrough}, url={https://doi.org/10.26434/chemrxiv-2024-pqjd3}, DOI={10.26434/chemrxiv-2024-pqjd3}, publisher={ChemRxiv}, journal={ChemRxiv}, author={Kawchak, Kevin}, year={2024}, month=oct, language={en} }

@article{09Kawchak_mAbBioprocess_2024, title={Monoclonal Antibody Bioprocess Engineering Advancements Using Conversational Artificial Intelligence}, url={https://doi.org/10.26434/chemrxiv-2024-3m7m1}, DOI={10.26434/chemrxiv-2024-3m7m1}, publisher={ChemRxiv}, journal={ChemRxiv}, author={Kawchak, Kevin}, year={2024}, month=oct, language={en} }

@article{10Kawchak_mAbInContext_2024, title={mAb Bioprocess Engineering In-Context Table Forecasts using Conversational AI Literature Insight Generations}, url={https://doi.org/10.26434/chemrxiv-2024-jzbj0}, DOI={10.26434/chemrxiv-2024-jzbj0}, publisher={ChemRxiv}, journal={ChemRxiv}, author={Kawchak, Kevin}, year={2024}, month=dec, language={en} }


@article{11Kawchak2024CancerVs, title={Cancer vs. Conversational Artificial Intelligence}, url={https://doi.org/10.1101/2024.12.28.630597}, DOI={10.1101/2024.12.28.630597}, journal={bioRxiv}, author={Kawchak, Kevin}, year={2024}, month=dec, language={en} }


@misc{12KawchakLLMBevClinical, author = {Kawchak, Kevin},
  title        = {Clinical decision support based on Bevacizumab cancer trials and pushing the limitations of advanced LLMs},
  year         = {2025},
  url          = {https://doi.org/10.5281/zenodo.14968162},    
  doi          = {10.5281/zenodo.14968162},                   
  publisher    = {Zenodo},
  organization = {ChemicalQDevice},
  month        = jan,
  language     = {en}
}


@misc{13KawchakLLMGemBev, author = {Kawchak, Kevin},
  title        = {Gemini Update Clinical decision support based on Bevacizumab cancer trials and pushing the limitations of advanced LLMs},
  year         = {2025},
  url          = {https://doi.org/10.5281/zenodo.14968289},    
  doi          = {10.5281/zenodo.14968289},                  
  publisher    = {Zenodo},
  organization = {ChemicalQDevice},
  month        = feb,
  language     = {en}
}


@misc{14KawchakCost, author = {Kawchak, Kevin},
  title        = {Cost containment of global monoclonal antibody drugs and cancer clinical trials via LLM focused reasoning},
  year         = {2025},
  url          = {https://doi.org/10.5281/zenodo.14968404},    
  doi          = {10.5281/zenodo.14968404},                  
  publisher    = {Zenodo},
  organization = {ChemicalQDevice},
  month        = feb,
  language     = {en}
}


@misc{15KawchakAgent, author = {Kawchak, Kevin},
  title        = {Autonomous LLM Agent and scalable Reasoning LLM for generating cancer drug industry cost solutions},
  year         = {2025},
  url          = {https://doi.org/10.5281/zenodo.15072843},    
  doi          = {10.5281/zenodo.15072843},                  
  publisher    = {Zenodo},
  organization = {ChemicalQDevice},
  month        = mar,
  language     = {en}
}


@misc{16KawchakLung, author = {Kawchak, Kevin},
  title        = {AI revolution toward the cure of lung adenocarcinoma},
  year         = {2025},
  url          = {https://doi.org/10.5281/zenodo.15278152},    
  doi          = {10.5281/zenodo.15278152},                  
  publisher    = {Zenodo},
  organization = {ChemicalQDevice},
  month        = apr,
  language     = {en}
}


@misc{17KawchakGlioblastoma, author = {Kawchak, Kevin},
  title        = {10 Year Glioblastoma Clinical Trial Meta-Analyses by Autonomous AI at Scale. Survival, HR, AE, and RoB scored in AI Reports and Charts, including Verifications},
  year         = {2025},
  url          = {https://doi.org/10.5281/zenodo.15549831},    
  doi          = {10.5281/zenodo.15549831},                  
  publisher    = {Zenodo},
  organization = {ChemicalQDevice},
  month        = may,
  language     = {en}
}

@misc{18KawchakPDAC, author = {Kawchak, Kevin},
  title        = {End-to-End Pancreatic Ductal Adenocarcinoma Digital Twin Clinical Trial Proposals},
  year         = {2025},
  url          = {https://doi.org/10.5281/zenodo.15735068},    
  doi          = {10.5281/zenodo.15735068},                  
  publisher    = {Zenodo},
  organization = {ChemicalQDevice},
  month        = jun,
  language     = {en}
}




@misc{GitHub23Mar25, url={https://github.com/kevinkawchak/LLMs-Pharmaceutical/tree/main/Code/Drug%20Discovery/Agentic-LLM}, abstractNote={AI cancer drug industry R&D. Contribute to kevinkawchak/LLMs-Pharmaceutical development by creating an account on GitHub.}, journal={GitHub}, language={en}, author = {Kawchak, Kevin}, title={LLMs-Pharmaceutical}, doi = {10.5281/zenodo.13273141} }


@misc{GitHub24Apr25, url={https://github.com/kevinkawchak/LLMs-Pharmaceutical/tree/main/Code/Drug%20Discovery/Multi-LLM}, title={LLMs-Pharmaceutical. AI cancer clinical trial data fusion}, journal={GitHub}, language={en}, author = {Kawchak, Kevin}, doi = {10.5281/zenodo.13273141} }



@misc{GitHub29May25, url={https://github.com/kevinkawchak/LLMs-Pharmaceutical/tree/main/Code/Drug%20Discovery/Quad-LLM}, title={LLMs-Pharmaceutical. AI cancer clinical trial data fusion}, journal={GitHub}, language={en}, author = {Kawchak, Kevin}, doi = {10.5281/zenodo.13273141} }



@misc{GitHub24Jun25, url={https://github.com/kevinkawchak/LLMs-Pharmaceutical/tree/main/Code/Digital_Twin_PDAC}, title={LLMs-Pharmaceutical. AI cancer clinical trial data fusion}, journal={GitHub}, language={en}, author = {Kawchak, Kevin}, doi = {10.5281/zenodo.13273141} }



@article{Parthiban_Vijeesh_Gayathri_Shanmugaraj_Sharma_Sathishkumar_2023, title={Artificial intelligence-driven systems engineering for next-generation plant-derived biopharmaceuticals}, volume={14}, ISSN={1664-462X}, url={https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2023.1252166/full}, DOI={10.3389/fpls.2023.1252166}, journal={Frontiers in Plant Science}, author={Parthiban, Subramanian and Vijeesh, Thandarvalli and Gayathri, Thashanamoorthi and Shanmugaraj, Balamurugan and Sharma, Ashutosh and Sathishkumar, Ramalingam}, year={2023}, month=nov, language={English} }

@article{Smiatek_Clemens_Herrera_Arnold_Knapp_Presser_Jung_Wucherpfennig_Bluhmki_2021, title={Generic and specific recurrent neural network models: Applications for large and small scale biopharmaceutical upstream processes}, volume={31}, ISSN={2215-017X}, url={https://www.sciencedirect.com/science/article/pii/S2215017X21000564}, DOI={10.1016/j.btre.2021.e00640}, journal={Biotechnology Reports}, author={Smiatek, Jens and Clemens, Christoph and Herrera, Liliana Montano and Arnold, Sabine and Knapp, Bettina and Presser, Beate and Jung, Alexander and Wucherpfennig, Thomas and Bluhmki, Erich}, year={2021}, month=sep, pages={e00640} }

@article{Wainaina_Taherzadeh_2023, title={Automation and artificial intelligence in filamentous fungi-based bioprocesses: A review}, volume={369}, ISSN={0960-8524}, url={https://www.sciencedirect.com/science/article/pii/S0960852422017540}, DOI={10.1016/j.biortech.2022.128421}, journal={Bioresource Technology}, author={Wainaina, Steven and Taherzadeh, Mohammad J.}, year={2023}, month=feb, pages={128421} }

@article{Vinestock_Short_Ward_Guo_2024, title={Computer-aided chemical engineering research advances in precision fermentation}, volume={58}, ISSN={2214-7993}, url={https://www.sciencedirect.com/science/article/pii/S2214799324000742}, DOI={10.1016/j.cofs.2024.101196}, journal={Current Opinion in Food Science}, author={Vinestock, Tom and Short, Michael and Ward, Keeran and Guo, Miao}, year={2024}, month=aug, pages={101196} }

@misc{What_Are_Large_Language_Models_(LLMs)?_2023, url={https://www.ibm.com/topics/large-language-models}, abstractNote={Large language models are AI systems capable of understanding and generating human language by processing vast amounts of text data.}, year={2023}, month=nov, language={en}, author={IBM} }

@misc{Comparison_of_AI_Models_across_Quality, url={https://artificialanalysis.ai/models}, abstractNote={Comparison and analysis of AI models across key performance metrics including quality, price, output speed, latency, context window & others.}, language={en}, author={artificialanalysis.ai} }

@article{pal2023chatgpt,
  title={ChatGPT or LLM in next-generation drug discovery and development: pharmaceutical and biotechnology companies can make use of the artificial intelligence-based device for a faster way of drug discovery and development},
  author={Pal, Soumen and Bhattacharya, Manojit and Islam, Md Aminul and Chakraborty, Chiranjib},
  journal={International Journal of Surgery},
  volume={109},
  number={12},
  pages={4382--4384},
  year={2023},
  url={https://journals.lww.com/international-journal-of-surgery/fulltext/2023/12000/chatgpt_or_llm_in_next_generation_drug_discovery.78.aspx},
  publisher={LWW}
}

@article{Chen_Liu_Wang_Shen_2024, title={Validation of an LLM-based Multi-Agent Framework for Protein Engineering in Dry Lab and Wet Lab}, url={http://arxiv.org/abs/2411.06029}, DOI={10.48550/arXiv.2411.06029}, note={arXiv:2411.06029 [q-bio]}, number={arXiv:2411.06029}, publisher={arXiv}, author={Chen, Zan and Liu, Yungeng and Wang, Yu Guang and Shen, Yiqing}, year={2024}, month=nov, journal={arXiv}, volume={n/a} }

@article{Liu_Wang_GenoTex2024, title={GenoTEX: A Benchmark for Evaluating LLM-Based Exploration of Gene Expression Data in Alignment with Bioinformaticians}, url={http://arxiv.org/abs/2406.15341}, DOI={10.48550/arXiv.2406.15341}, note={arXiv:2406.15341 [cs, q-bio]}, number={arXiv:2406.15341}, journal={arXiv}, author={Liu, Haoyang and Wang, Haohan}, year={2024}, month=jun, volume={n/a} }

@article{M._Bran_Cox_Schilter_Baldassari_White_Schwaller_2024, title={Augmenting large language models with chemistry tools}, volume={6}, rights={2024 The Author(s)}, ISSN={2522-5839}, url={https://www.nature.com/articles/s42256-024-00832-8}, DOI={10.1038/s42256-024-00832-8}, number={5}, journal={Nature Machine Intelligence}, author={M. Bran, Andres and Cox, Sam and Schilter, Oliver and Baldassari, Carlo and White, Andrew D. and Schwaller, Philippe}, year={2024}, month=may, pages={525–535}, language={en} }

@article{Li_Kilicoglu_Xu_Zhang_2024, title={BiomedRAG: A Retrieval Augmented Large Language Model for Biomedicine}, url={http://arxiv.org/abs/2405.00465}, DOI={10.48550/arXiv.2405.00465}, note={arXiv:2405.00465 [cs]}, number={arXiv:2405.00465}, journal={arXiv}, author={Li, Mingchen and Kilicoglu, Halil and Xu, Hua and Zhang, Rui}, year={2024}, month=may, volume={n/a} }

@article{Chen_Li_Wang_Du_Yu_Lu_Li_Qiu_Pan_Huang_et_al._2024, title={Chemist-X: Large Language Model-empowered Agent for Reaction Condition Recommendation in Chemical Synthesis}, url={http://arxiv.org/abs/2311.10776}, DOI={10.48550/arXiv.2311.10776}, note={arXiv:2311.10776 [cs]}, number={arXiv:2311.10776}, journal={arXiv}, author={Chen, Kexin and Li, Junyou and Wang, Kunyi and Du, Yuyang and Yu, Jiahui and Lu, Jiamin and Li, Lanqing and Qiu, Jiezhong and Pan, Jianzhang and Huang, Yi and Fang, Qun and Heng, Pheng Ann and Chen, Guangyong}, year={2024}, month={apr}, volume={n/a} }

@article{Ramos_Collison_White_2024, title={A Review of Large Language Models and Autonomous Agents in Chemistry}, rights={Creative Commons Attribution 4.0 International}, url={https://arxiv.org/abs/2407.01603}, DOI={10.48550/ARXIV.2407.01603}, author={Ramos, Mayk Caldas and Collison, Christopher J. and White, Andrew D.}, year={2024}, journal={arXiv}}

@inproceedings{Guo_Nan_Zhou_Guo_Guo_Surve_Liang_Chawla_Wiest_Zhang_2024, title={Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation}, url={https://openreview.net/forum?id=t1mAXb4Cop#discussion}, author={Guo, Kehan and Nan, Bozhao and Zhou, Yujun and Guo, Taicheng and Guo, Zhichun and Surve, Mihir and Liang, Zhenwen and Chawla, Nitesh V. and Wiest, Olaf and Zhang, Xiangliang}, year={2024}, month=nov, language={en}, booktitle={OpenReview.net} }

@article{Tan_2024, title={A Transformer Based Generative Chemical Language AI Model for Structural Elucidation of Organic Compounds}, url={http://arxiv.org/abs/2410.14719}, DOI={10.48550/arXiv.2410.14719}, note={arXiv:2410.14719 [physics, q-bio]}, number={arXiv:2410.14719}, journal={arXiv}, author={Tan, Xiaofeng}, year={2024}, month=oct, volume={n/a} }


@article{Chacko_Sondhi_Praveen_Luska_Hernandez_2024, title={Spectro: A multi-modal approach for molecule elucidation using IR and NMR data}, url={https://chemrxiv.org/engage/chemrxiv/article-details/6724fb5b7be152b1d0ae66f8}, DOI={10.26434/chemrxiv-2024-37v2j}, journal={ChemRxiv}, author={Chacko, Edwin and Sondhi, Rudra and Praveen, Arnav and Luska, Kylie L. and Hernandez, Rodrigo Alejandro Vargas}, year={2024}, month=nov, language={en} }

@article{Weggen_Seidel_Bean_Wendeler_Hubbuch_2023, title={Kinetic studies and CFD-based reaction modeling for insights into the scalability of ADC conjugation reactions}, volume={11}, ISSN={2296-4185}, url={https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2023.1123842/full}, DOI={10.3389/fbioe.2023.1123842}, journal={Frontiers in Bioengineering and Biotechnology}, author={Weggen, Jan Tobias and Seidel, Janik and Bean, Ryan and Wendeler, Michaela and Hubbuch, Jürgen}, year={2023}, month=apr, language={English} }

@article{Bauer_Boettger_Papadaki_Leitner_Klostermann_Kettenberger_Georges_Larraillet_Gluhacevic_von_Kruechten_Hillringhaus_et_al._2024, title={Procollagen-lysine 2-oxoglutarate 5-dioxygenases are responsible for 5R-hydroxylysine modification of therapeutic T-cell bispecific monoclonal antibodies produced by Chinese hamster ovary cells}, volume={12}, ISSN={2296-4185}, url={https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2024.1414408/full}, DOI={10.3389/fbioe.2024.1414408}, journal={Frontiers in Bioengineering and Biotechnology}, author={Bauer, Niels and Boettger, Marco and Papadaki, Styliani and Leitner, Tanja and Klostermann, Stefan and Kettenberger, Hubert and Georges, Guy and Larraillet, Vincent and Gluhacevic von Kruechten, Dino and Hillringhaus, Lars and Vogt, Annette and Ausländer, Simon and Popp, Oliver}, year={2024}, month=oct, language={English} }

@article{Reis-Claro_Silva_Moutinho_Garcia_Pereira-Castro_Moreira_2024, title={Application of the iPLUS non-coding sequence in improving biopharmaceuticals production}, volume={12}, ISSN={2296-4185}, url={https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2024.1355957/full}, DOI={10.3389/fbioe.2024.1355957}, journal={Frontiers in Bioengineering and Biotechnology}, author={Reis-Claro, Inês and Silva, Maria Inês and Moutinho, Ana and Garcia, Beatriz C. and Pereira-Castro, Isabel and Moreira, Alexandra}, year={2024}, month=feb, language={English} }

@misc{Frontiers_in_Bioengineering_and_Biotechnology, url={https://www.frontiersin.org/journals/bioengineering-and-biotechnology}, abstractNote={A multidisciplinary journal that accelerates the development of biological therapies, devices, processes and technologies to improve our lives by bridging the gap between discoveries and their appl...}, author={Frontiers} }

@article{Yu_Guo_Zhang_Bo_Liang_Wang_Yang_2022, title={Comparative multiomics analysis of cell physiological state after culture in a basket bioreactor}, volume={12}, rights={2022 The Author(s)}, ISSN={2045-2322}, url={https://www.nature.com/articles/s41598-022-24687-4}, DOI={10.1038/s41598-022-24687-4}, number={1}, journal={Scientific Reports}, author={Yu, Shouzhi and Guo, Miaomiao and Zhang, Yadan and Bo, Cunpei and Liang, Hongyang and Wang, Hui and Yang, Xiaoming}, year={2022}, month=nov, pages={20161}, language={en} }

@article{Kawchak_mAb_In-Context_2024, title={mAb Bioprocess Engineering In-Context Table Forecasts using Conversational AI Literature Insight Generations}, url={https://chemrxiv.org/engage/chemrxiv/article-details/674804b05a82cea2fa3af213}, DOI={10.26434/chemrxiv-2024-jzbj0}, journal={ChemRxiv}, author={Kawchak, Kevin}, year={2024}, month=dec, language={en}}




```
