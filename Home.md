## 260123 ##

### Agent GRN correction

**Data Preparation & Ground Truth**  
- Re‑calculated accuracy using Aurelian’s ground‑truth data and updated the corresponding labels.  
- Moved generated answer files to new directories, True Negative to True Positive:  
  - `qa_comprehensive/full_text/rater`  
  - `qa_comprehensive/full_text/shuffled`  
  - `qa/gpt-oss-20b` & `qa/gpt-oss-120b`  
  - `data/papers/signor` & `data/papers/qa_search/`  
  - `langgraph/results/reasoning/glm-4.6/no_search/false_edges`  
- Re‑computed accuracy metrics and experimented with different decision thresholds for GNN model (0.01 → 0.5).  

**Model Evaluation & Accuracy Analysis**  
- Ran evaluations for:  
  - GPT‑OSS‑20b & GPT‑OSS‑120b (re‑run required)  
  - GLM‑4.6 (no‑search mode)  
  - Signor baseline  
  - GNN models (added performance metrics and analysis code)  
- Identified issues:  
  - Macro‑F1 inconsistencies (perfect predictions yield 0.5).  
  - High proportion of NaN or “I don’t know” answers causing low accuracy (overall acc ≈ 0.13).  
  - Specific problematic edges (e.g., `BMI1_H2AX_up‑regulates`, `AURKA_AR`, `GNAO1_ADCY1_down‑regulates`).  
  - Evidence‑support analysis revealed many negatives lack any supporting literature; treating NaN as False raises performance to > 0.8.  
- Recorded benchmark accuracies:  
  - Rater accuracy = 0.81  
  - Random baseline accuracy = 0.875  
- Token‑usage audit for GPT‑OSS‑120b (max 128k):  
  - One file (`CDK1_AR_up‑regulates.json`, 130 k tokens) exceeded limit → error.  
  - Overall token stats: min ≈ 8 k, max ≈ 90 k, mean ≈ 50 k, median ≈ 51 k.  

**Paper Search & QA Pipeline Enhancements**  
- Refactored `QA_paper_search.py`:  
  - Improved PDF download routine (`download_pdf_from_doi`) and added retry logic for missing papers.  
  - Made search strings configurable to broaden queries; target = 5 papers per question.  
  - Ensured search results are stored in `true_negative` and `true_positive` folders.  
  - Added support for loading Signor edges and moved core functions to `src` after verification.  
- Debugged path issues preventing PDF downloads; resumed full edge‑wise paper search.  
- Executed sufficient‑support test on 495 papers (≈ 379 min 34.9 s).  

**Additional Findings & Resources**  
- Noted relevant literature: *Language Agents Achieve Superhuman Synthesis of Scientific Knowledge* (arXiv:2409.13740).  

- **Research & Reading**
  - Reviewed documentation and tutorials:
    - “How to implement tool use” (Claude platform)
    - Claude Agent SDK tutorial (Claude Sonnet 4.5)
    - Agent Skills in the SDK
    - OpenRouter Zero Data Retention and Logging
    - Web Reader MCP Server
  - Read and annotated papers:
    - *FuseLinker: Leveraging LLM’s pre‑trained text embeddings…*
    - *GOFlowLLM – curating miRNA literature…*
    - *An Evidence‑Grounded Research Assistant for Functional Genomics…*
    - *On Evaluating LLM Alignment by Evaluating LLMs as Judges*
    - *Hierarchical Retrieval with Evidence Curation for Open‑Domain Financial QA*
    - *Fact Checking with Insufficient Evidence*
    - Additional papers on multi‑hop QA, SEARCH‑O1, and related frameworks

- **SDK / Tool Integration**
  - Integrated Claude SDK with GLM, search (https://github.com/anthropics/life-sciences), and custom skill modules
  - Implemented Claude SDK + GLM and tested the web‑search plugin
  - Added and exercised the “Answer a single TRUE or FALSE…” skill
  - Connected GLM to MCP web‑reader; experimented with PubMed/PMC plugin
  - Checked SDK tool‑call responses and token‑usage reporting
  - Verified Claude SDK token usage with claude-3.5 (input 9k‑68k, output 50‑2.8k, cache 7k‑571k)

- **Prompt Engineering & Skill Evaluation**
  - Compared official Claude skill vs. prompt‑engineering across 10 runs. The performance is similar, but the official skill is more time efficient.
  - Modified prompts to enforce webReader usage for key papers
  - Investigated why retraction notices were missed (webSearch vs. webReader)
  - Thu pubmed search simply worked better than the webSearch and webReader becaude it has better relevant ranking system. The retracted paper wad ranked much lower than the non-retracted paper, which improve the accuracy of final answer.
  - Refined prompts for true‑positive edge evaluation

- **Code Organization & Cleanup**
  - Consolidated scripts and test code; removed unnecessary test files
  - Re‑structured repository into sub‑folders (e.g., QA, QA_analysis, data)
  - Cleaned up redundant code and system‑prompt conversions
  - Ensured main code runs after moving `.claude` files
  - Reviewed and trimmed PDF folder contents
  - Added README updates and final code polishing

- **Testing & Evaluation**
  - Ran 10 iterations of the same question to benchmark skill speed vs. accuracy
  - Executed true‑positive and true‑negative edge evaluations on glm + SKILL + pubmed search:
    - True positives: 24/48 correct
    - True negatives: 19/19 correct
  - The claude-4.5 basically perform the same.
  - Performed SDK web‑search tests and plugin trials

- **Version Control & Release Management**
  - Updated Git repository with latest code and documentation

- **Writing & Documentation**
  - Integrated “Lost in the Maze” into the Introduction’s related work section
  - Added citations for additional frameworks

- **Miscellaneous**
  - Consulted Gemini about script placement and QA integration decisions
  - Asked Antigravity about GLM webReader parameter tuning for retraction detection
  - Explored “BrowseComp → multi‑hop QA” and “Humanity’s Last Exam” concepts
  - Investigated differences between SEARCH‑O1 and related approaches.

### 求職

- **Job search preparation**
  - Queried potential job openings I could apply for  
  - Gathered recommendations from 104 and LinkedIn  

- **Resume / CV revision**
  - Integrated vaccine paper into CV and LinkedIn 
  - Revised CV using Jose’s resume as a template
  - Reviewed Jose’s resume for inspiration  
  - Added useful items, removed skills I don’t yet have  
  - Highlighted work in Saez Lab and PhD credential  
  - Decided on title phrasing (computational biology vs. leading with PhD)  
  - Completed final proof‑read of the resume  

- **LinkedIn profile updates**
  - Updated “About” section and overall profile content  
  - Added CovSyn paper to LinkedIn  
  - Aligned LinkedIn details with the revised CV  
  - Modified 104 job‑portal posting accordingly  

- **Research / project documentation**
  - Summarized concrete outcomes of my research projects  
  - Compiled EBI and LLM‑related keywords  

- **Final checks & communication**
  - Performed overall quality check of all materials  
  - Sent the updated resume/CV/LinkedIn information back to the recruiter/headhunter  

### Learning

- **Article Published:** *How to Make LLMs Speak Your Language* – A blog post detailing methods for adapting large language models to specific linguistic styles and vocabularies. [Read the article](https://monadical.com/posts/how-to-make-llms-speak-your-language.html)

### CovSyn article

- **Supplementary Material**
  - Organized the supplementary files
  - Removed duplicate content
  - Updated figure, table, and algorithm references
  - Corrected references to the supplementary material in the main text
  - Proofread the supplementary document  

- **Main Text**
  - Fixed supplementary references within the main manuscript
  - Performed proof‑reading of the main text  

## 251214 ##

### Agent GRN correction

### Token Usage & Semantic Search  
- Analyzed token usage for loaded questions and contexts; generated a token usage report (67 papers, avg 20,826 tokens, max 60,365 tokens).
- Identified 63 files > 8 k tokens and 9 files > 32 k tokens.  
- Re‑checked semantic‑search capabilities and documented the type of information it can provide. It cannot provide full-text nor the pdf download. But it can provide the llm short summary.

### Model Evaluation & Metrics  
- Removed `NaN` values from TP, TN, FP, and FN calculations while keeping total edge count.  
- Re‑ran context‑window experiments after tweaking the “sufficient context” prompt.  
- Confirmed macro‑F1 calculation is correct.  
- Summarized key insights from previous results, including:  
  - Abstract + title sufficiency is lower than full‑text; only ~50 % of edges are sufficiently supported by full‑text.  
  - True‑negative edges often lack sufficient references, maybe explaining why they were removed in Signor.  
  - The 20B model performs better on true‑negative edges because it frequently answers “I don’t know.”  
- Generated sufficient test pie chart. Also generated the associated accuracy test.

### Prompt & Query Engineering  
- Refined `convert_question_to_query` prompt (initially returned poor synonyms); asked Claude for improvements.
- Updated `construct_signor_question` to focus on “A activates B” / “A inhibits B.”  
- Tested the sufficiency prompt on 10 papers – all judged insufficient; iterated on wording.  
- Explored integrating skill‑related information into prompts to improve answer quality.  
- Adjusted temperature and QA prompts for more consistent responses.  
- Implemented the rater function.

### Sufficiency Experiments  
- Evaluated AU‑Cite papers for sufficiency; most should be sufficient, but many returned insufficient, indicating prompt issues.  
- Tested specific gene pairs (e.g., MAP2K1 ↔ PPARG, MAP2K1 ↔ PPARG via phosphorylation) to see how phrasing affects sufficiency scores.  
- Ran opposite‑direction queries (e.g., BRAF ↔ MAP2K1) and confirmed the model can correctly output “No” when appropriate.  
- Identified cases where the model answered “No” but reported sufficiency = 0; refined the sufficiency prompt accordingly.  

### Web Search Agent Development  
- Designed a web‑search agent (based on `fetch_signor_paper_details.py`) to retrieve relevant papers:  
  - Converts user prompts into optimized PubMed search strings.  
  - Generates a specified number of search results (e.g., 10 papers).  
  - Handles cases where no paper is found: pauses for user decision (manual upload vs. skip).  
- Implemented workflow options: **manual mode** (user supplies PDFs) and **auto mode** (agent attempts full‑text retrieval; if unavailable, sets `full_text = None`).  
- Verified that Claude cannot access full‑text behind paywalls; limited the agent to open‑access sources.  

### Additional Investigations   
- Explored using the Semantic Scholar API for article summaries (checked DOI 10.1126/science.1106148).  
- Considered a LangGraph‑based orchestration but decided against it after discussion with Antigravity.  
- Planned future work to specify interaction types more explicitly when needed.  

## 251207 ##

### Agent GRN correction

**Prompt & Rater Development**
- Wrote the rater prompt.  
- Tested the prompt with title + abstract inputs.  
- Explored the “A → B then B → A” scenario to see if the rater still marks sufficiency.  
- Added a three‑option answer format (Yes / No / Unsure) and defined how “Unsure” is treated (as a negative answer).  

**Sufficiency Experiments**
- Ran the BCL2L1 → BAD query on two randomly selected papers: one truly about the pair and one about BCL2L10 / BAD; Claude correctly identified the relevant paper.  
- Confirmed that title + abstract alone are insufficient, while full‑text more likely provides sufficient context using claude 4.5.  
- Noted that a PubMed paper not indexed in OminiPath is inherently insufficient.  

**Data Collection & Preparation**
- Collected ~10 papers via a custom web‑search method; verified each has a full abstract.  
- Identified that many Signor entries have PMID but lack PMCID, limiting full‑text access.  

**Paper Retrieval Pipeline**
- Designed a three‑step retrieval strategy:  
  1. PDF extraction (if local PDF exists)  
  2. PMC full‑text (if PMCID available)  
  3. Jina AI lookup (using DOI or PubMed URL)  
- Implemented PDF downloading code using paper-search-mcp. But it is incompleted. For now, I still need to do manual downloading. PubMed api doesn't provide pdf download option.

**Code Development & Integration**
- Structured my repository.

**Evaluation & Scoring**
- Loaded the Signor dataset, retrieved titles, abstracts, and full texts, and computed sufficiency scores for all papers.  
- Plot pie chart for comparing sufficient support when only title/abstract provided or full text provided.
- Compared results for true‑negative edges (title + abstract vs. full text) and true‑positive edges. 
- Defined accuracy calculation: predictions of “Unsure”, `NaN` is treated as negative (No answer).  
- Generated few tables for metrics comparison in different conditions. Also compared the prediction result of gpt-oss-20b and gpt-oss-120b.

**Infrastructure & Miscellaneous** 
- Planned incorporation of VisDoM for future analyses.  
- Reviewed the `paper-qa` repository as a potential component for upcoming RAG implementations.  

## 251128 ##

### Agent GRN correction

**Flash Talk & Presentation**  
- Sent the flash PPT and 4‑month progress materials (11/26).  
- Adjusted fonts and grammar using Gemini; performed final proofreading.  

**GNN Development & Evaluation**  
- Set up Git: committed important files, created a new branch for GNN work.  
- Installed PyTorch and developed `gnn_train_signor.py`.  
- Processed protein‑protein interaction data: extracted, de‑duplicated, and stored true‑negative edges.  
- Defined workflow: use existing true positives/negatives as the test set; train with random positive edge addition (aligned with Aaron’s method).  
- Ensured training graphs exclude test‑set edges.  
- Trained models; best checkpoint at epoch 232 (Validation AUC 0.85, Test AUC 0.3902, Test F1 0.7593).   
- Fixed AUC‑ROC calculation (added proper threshold handling); verified curve shape and averaged results over 10 runs before plotting.
- Generated prediction plots for all models.

<details>
<summary>點擊查看 GNN 訓練流程說明</summary>

```
1. Data Loading & Cleaning: Loads the full SIGNOR network and removes any edges that are present in the "True Test Set (true positive and true negative edges)" to prevent data leakage.



1. Negative Sampling:

    - Training: Generates random negative edges (noise) to balance the training set.

    - Testing: Uses verified "True Negative" edges (biologically non-interacting pairs) for robust evaluation.

1. Message Passing: Crucially, the GNN only uses positive training edges for message passing (learning node representations), but predicts on both positive and negative edges to calculate loss.

1. Model Selection: The best model is selected based on Validation AUC, and that specific model checkpoint is used to calculate the final Test metrics.
```

</details>

<details>
<summary>點擊查看訓練輸出詳細資訊</summary>

```
--- Loading Graphs ---

Original full graph: 25422 interactions

Loading True Labels for Test Set (to exclude from training)...

Filtered graph: 25357 interactions (removed 65 test edges)

Total nodes: 6277

Positive edges (training pool): 25357

--- Generating Random Negative Edges for Train/Val ---

Negative edges (random): 25357

Total train/val edges: 50714

Train/val balance: 25357 positives / 25357 negatives

--- Preparing Test Set ---

True positives: 41 edges

True negatives: 26 edges

Test set: 67 edges (41 pos / 26 neg)

--- Using One-hot Encoding for Node Features ---

Node features shape: torch.Size([6277, 6277])

--- Splitting Train/Val Data ---

Training: 40571 edges (20286 pos / 20285 neg)

Validation: 10143 edges (5071 pos / 5072 neg)

--- Model Setup ---

Model parameters: 1632385


Epoch 232: Loss=0.1161 | Val: AUC=0.8500, F1=0.7931 | Test: AUC=0.3902, F1=0.7593 ★ NEW BEST (Saved)



================================================================================

Training Complete

================================================================================

Best model from epoch: 232

Best validation AUC: 0.8500

Final Test AUC: 0.3902

Final Test F1: 0.7593

Model saved to: best_gnn_model.pth

================================================================================
```

</details>

**Literature Review & Paper Management**  
- Reviewed papers and scanned recent NeurIPS & ICLR proceedings.  
- Read and summarized:  
  - *Can LLMs be Good Graph Judge for Knowledge Graph Construction?* (arXiv:2411.17388)  
  - *Harnessing Diverse Perspectives: A Multi‑Agent Framework for Enhanced Error Detection in Knowledge Graphs* (arXiv:2501.15791)
  - *SUFFICIENT CONTEXT: A NEW LENS ON RETRIEVAL‑AUGMENTED GENERATION SYSTEMS* (arXiv:2411.06037)
- Our project aligns more with multi‑document QA/evidence aggregation than multi‑hop QA.
- 看起來是可以當作取代我現在relavancy test的prompt，這篇基本上是純粹用prompt enfineering，換句話說，把他的prompt應用在我的agent上基本就完了，那麼現在的問題是我要如何找到sufficient prompt，在我知道現在prompt不是sufficient prompt時我該怎麼做 -> prompt裡面有explaination這段，所以以可以用explaination的回答來更新prompt做迭代，比方說explaination說年份資訊不足，那麼我就可以回去prompt說要找年份 -> 我現在在考慮Lun說的comment，refine PKN真的該被當成multi-hop QA嗎 -> 我最後傳給Lun: Thanks for sharing the paper; it was an interesting read. I've been thinking that our GRN refinement task might not actually be multi-hop QA. If I understand correctly, multi-hop QA requires chaining sequential facts from the context to derive an answer. For example, to answer whether "A affects C," one might need to connect the facts "A->B" and "B->C" (like an A->B->C chain). In our case, the process seems more parallel. We are verifying a single link (A->B) by gathering multiple pieces of supporting evidence simultaneously, which may sometimes contain conflicting information. I guess this aligns more with Multi-document QA or Evidence Aggregation?
- Set up `paper-search-mcp` (searches arXiv, PubMed, bioRxiv, Semantic Scholar).  
- Tested code to extract citation counts and other metadata; output JSON containing title, abstract, URL, journal, impact factor, citation number, etc.  

**Tooling & Environment Setup**  
- Installed and configured:  
  - Zotero for reference management.  
- Backed up repository and experimental results.  
- Used Antigravity to troubleshoot and fix code issues.  

### CovSyn article

- **Manuscript organization**
  - Copied the *Infectious Disease Modeling* manuscript into the project folder.
  - Updated the manuscript to incorporate changes from Gemini 3.0.

- **Formatting & compliance**
  - Reformatted the document to meet IEEE style requirements for the *IEEE Journal of Biomedical and Health Informatics*.
  - Resolved citation formatting issues throughout the manuscript.

- **Content structuring**
  - Condensed the main text to 8 pages.
  - Relocated supplementary material (figures, tables, extended methods) to a separate supplementary file.

### 其他

- **Develop an automated LLM-driven reporting system**
  - Design and implement an LLM pipeline to process completed items from Taskade.
  - Integrate the pipeline with Taskade’s API for real‑time data extraction.
  - Generate concise, human‑readable weekly reports in Markdown format.

## 251124 ##

### Agent GRN correction

- **Version control**
  - Committed all important current files to the repository.
  - Created a new Git branch dedicated to the GNN development.

- **Environment setup**
  - Installed PyTorch and verified the installation.

- **Data preparation**
  - Extracted protein‑protein interaction data.
  - Removed duplicate entries.
  - Stored true‑negative samples for later use.

- **Model development & training workflow**
  - Defined the true‑positive and true‑negative sets as the test dataset.
  - Implemented a training pipeline similar to Aaron’s approach, using random positive edge addition.
  - Ensured that edges belonging to the test set were excluded from the training graph.

- **Results**
  - (Summary of outcomes to be inserted here.)

## 251122 ##

### Agent GRN correction

- **Research & Reading**
  - [Reviewed *Recursive Language Models* article (Medium)](https://alexzhang13.github.io/blog/2025/rlm/)
  - Re‑read the Wikipedia paper on ranking methodology (clarify if ranking is based on confidence or text‑support matching)
  - Studied Google Research “confidence” paper
  - Examined KGValidator framework (arXiv 2404.15923) and evaluated its scope for future work. 看起來Lun他是非頂會或是頂刊的paper就不看，所以這篇不在他的考慮範圍。
  - Investigated edge‑validation cases (e.g., BCL2L1‑BAD, BMI1‑H2AX, PRKACA‑AKT2, ALOX5‑STAT5A) and differences in edge definitions (direct vs. indirect)
    - 也許false edges表現比較好的理由可能是因為我的edge問法太strict了嗎，所以比較容易回答false
    - 如果我給正確的reference給claude，然後問他一樣的問題，他會回答什麼 -> 答案還是不變
    - 為什麼GLM-4.6在false edge的表現比較差？
        - 看ALOX5 - STAT5A -> 看起來是對連接的定義不同，有些是看直接連接，有些是間接就可以
        - 用用看claude的search，看他會cite哪篇，給出什麼答案，這個edge是signor在2020年加入的edge，後來刪掉了-> 結果signor反而是用2007年的paper

- **Presentation Preparation**
  - Loaded the PowerPoint deck and searched Google Drive for additional 1‑on‑1 PPT examples (found via “1‑on‑1” query)
  - Determined presentation length: 25 min total → allocate ~10 min for discussion, target 15–20 slides

- **Planning**
  - Drafted a 3–4‑month roadmap, aiming for one major deliverable per month
  - Outlined next steps for each month (e.g., validation framework, large‑scale simulation, final report)

- **Experimental & Validation Work**
  - Set up codebase capable of running large‑scale simulations
  - Investigated why certain LLM queries are flagged as problematic
  - Verified “true edge” cases and analyzed false‑edge performance (possible over‑strict query formulation)
  - Compared ground‑truth tables for AU dataset
  - Tested Claude with correct references to see answer consistency
  - Analyzed GLM‑4.6’s poorer performance on false edges
  - Ran Claude’s web‑search mode on edges that all models answered “true” (e.g., BCL2L1‑BAD → Signor 2000 paper)
  - Checked citation behavior: Claude cited a 2007 paper for a 2020 Signor edge that was later removed

- **Miscellaneous Tasks**
  - Purchased Gemini-3 via VPN, using TWD payment method. I tried the 學生方案，但我不能用
  - Updated PPT color scheme according to Google Research guidelines
  - Noted potential future work on KGValidator (small scope, consider alternatives)

## Thinking:
現在我想比較合理的流程可能是query -> web search -> paper collections -> score the papers -> include papers to the structured query -> LLM reasoning for both Yes/No answer -> final answer -> non-reasoning LLM to give confidence -> calculate accuracy -> back to optimize the structured query. 我不太確定的是在這狀況下LLM confidence有什麼意義，還是web search的paper scoring要跟confidence結合算出什麼有用的metric，然後我們在針對這個分數跟accuracy做某種最佳化，也許我該從人類的角度來想這個問題，expert是怎麼curate edge的，首先他們會去google找到的paper，然後評估這篇paper的可靠性，可靠性有可能參考abstract, images, impact factor, citation等等，接著再去看其他篇paper做一樣的事，有了這些paper的綜合考慮後，他們應該會主要看最可靠的那篇paper是support還是不support這個假說，如果有些case有兩篇相同可靠性，且support不同statement的話，那麼專家就會給出一個跟自己的believe比較接近的答案，在這種狀況下confidence反應的是什麼呢，如果是最後回答的confidence，那麼這其實是在評估正反兩方supporting data的有效程度，越是一面倒的supporting data，越容易給出confidence高的結果。現在讓我們想回wikipedia那篇文章，那篇文章給的是confidence嗎，他們到底是在rank什麼，看起來是claim跟citation paper的匹配度，這樣的話也許我該求的不是最終答案的Yes, No confidence？我該求什麼？如果是找到的文章跟問題的關聯程度的，就變成跟這篇wikipedia的模式一樣，變成是多一個文章跟citation的匹配度，然後這個匹配度再跟剛剛上面講的文章品質做一個加權總和，這樣的話就不需要給出最終的yes no confidence了，或是其實還是可以給，就變成多一個參考依據，這邊該從user的觀點去考量，我在用這系統的時候我們應該期望除了有Yes/No回答外，還有一個這個edge的信心程度，或是說準確程度，這個score越高，user就越不用擔心，越低，就代表user可能還是得自己去做文獻回顧來判斷，那這個score就不應該只是llm confidence因為這只反應了llm回答這個問題的信心程度，不代表準確度，就算是consistency也不代表準確度，那麼有什麼score是可以當作準確度的呢？目前我還沒有答案，也許該做點文獻回顧，或是可以單純從找到的文獻品質，LLM confidence做分數，那這個分數該怎麼優化，該怎麼讓他真的反應accuracy。不太可能有什麼score可以反應accuracy，真的有的話就不用benchmark了，直接最佳化到最高score就完了，但我們應該還是可以有某種分數可以比較好反應出LLM的回答品質，就像是問一個專家問題，他有可能回答出錯誤的答案，可是他的邏輯表述可能都是正確的，那至少讀者可以知道這個專家的猜測是有依據的，不是跟你瞎說，所以給出準確的答案本身就沒有意義，應該是說給出比較有依據的答案才對，以這個角度想的話，用找到的文章品質跟LLM confidence的綜合分數就有意義了，再來，我們也可以假設，比較有依據的答案的準確度應該相對比較高才對，所以我們可以預期最終的performance會比較好，那麼在找到的文章都是一樣的情況下，改變文章出現在context window這件事會影響的就只有LLM confidence了。

---
1. Agent GRN correction
    1. [Recursive Language Models](https://medium.com/@gaurav219688/deep-research-ai-workflow-using-langgraph-tavily-search-any-llm-provider-373ae5aa2cfd)
    1. Gmini 3
        1. 用成大vpn買，然後也可以直接用台幣付
    1. 再看一次wikipedia那篇文章，他們rank的究竟是什麼，是confidence嗎，還是是內文跟supporting data的匹配度
    1. 載PPT
    1. 看一下google drive有沒有其他人的PPT可以當參考 -> 直接在google drive搜尋1-on-1是可以找到，可以拿來參考
    1. check一下時長多久 -> 25分鐘，可能還要考慮討論10分鐘，所以看起來就是搞個15到20頁吧
    1. next 3 or 4 months plan
        1. 理論上就是一個月一件事
    1. How paper
        1. paper基本structure
    1. google research confidence那篇
    1. wikipedia那篇
    1. 暫定KGvalidator，不過這篇有點小，可以再看看其他的
    1. 翻翻LLM2KG的folder
    1. [KGValidator: A Framework for Automatic Validation of Knowledge Graph Construction](https://arxiv.org/abs/2404.15923)
    1. 準備可以跑大規模模擬的code
        1. check為什麼有些問題會llm都說有問題
            1. check true edge
                1. BCL2L1 - BAD
                1. BMI1 - H2AX
            1. false edges表現比較好的理由可能是因為我的edge問法太strict了嗎，所以比較容易回答false
            1. 比較一下Au的ground truth表
                1. PRKACA - AKT2
                    1. 如果我給正確的reference給claude，然後問他一樣的問題，他會回答什麼
            1. 為什麼GLM-4.6在false edge的表現比較差？
                1. 看ALOX5 - STAT5A -> 看起來是對連接的定義不同，有些是看直接連接，有些是間接就可以
                    1. 用用看claude的search，看他會cite哪篇，給出什麼答案，這個edge是signor在2020年加入的edge，後來刪掉了-> 結果signor反而是用2007年的paper
            1. check全部都回答true的edge，然後問claude web search
                1. BCL2L1 - BAD -> Signor用的是2000年的paper
    1. 照著google research那篇改顏色
1. Learning
    1. 研究abacus
    1. 研究gemini
    1. [Lost in the Maze: Overcoming Context Limitations in Long-Horizon Agentic Search](https://arxiv.org/abs/2510.18939)

## 251117 ##
1. [Confidence Improves Self-Consistency in LLMs](https://aclanthology.org/2025.findings-acl.1030.pdf)
1. Impemented the method True(P) above,
    1. Tested it using the qwen 14b model. Access the logprob of the first token.
    1. I tested it using the previous reasoning for with and without search. It seems the results with search often get higher confidence.
1. The plots in my hackmd are dead. I thus regenerated the plots and uploaded them again to hackmd and google drive.
1. check llm-polygraph.
1. Check token usage with gpt-oss-120b. no search 300 to 500 and with search 600 to 800.
1. Start running the H200 gpus
    1. I followed both F and Paul's tutorials. Somehow I couldn't load any model to A100 with F's tutorial. It could also because I was using interactive page.
    1. Test if I can load two llm in one H200 GPU. I can do that with these setting,
        1. `CUDA_VISIBLE_DEVICES=0 uv run python -m sglang.launch_server \
  --model-path /hps/nobackup/saezrodriguez/hf_models/gpt-oss-120b \
  --tp-size 1 \
  --tool-call-parser gpt-oss \
  --reasoning-parser gpt-oss \
  --mem-fraction-static 0.7 \
  --served-model-name gpt-oss \
  --host 0.0.0.0 \
  --port 8000`
        1. `CUDA_VISIBLE_DEVICES=1 uv run python -m sglang.launch_server \
  --model-path /hps/nobackup/saezrodriguez/hf_models/qwen3-4b-instruct-2507 \
  --tp-size 1 \
  --mem-fraction-static 0.2 \
  --served-model-name qwen2.5-14b-instruct \
  --host 0.0.0.0 \
  --port 8080`
    1. Learned how to download model. This requires export the cache path.
    1. Implemented the logprob in SGLang.
    1. I am not sure why I don't have any reasoning text showing in the result now. I need to check more latter.
1. Debbuged logprob with SGLang. It turns out the problem is the temperature. The vLLM and SGLang's logprobs are affecting by the temperature a lot while llama.cpp and openAI api are not. I now setting the temperature = 1.
1. Coding,
    1. Run single question testing.
    1. Ask Claude to help me seperate the original agent code to multiple py files so that I can also do simulation on each py file.
    1. Test running gpt-oss-120b,
        1. 跑2輪true+false edges -> ~23min，那就是一組差不多10分鐘
1. Generated the benchmark result
    1. Load the prediction results and plot the AUC ROC curve. Also run gpt-oss-20b. I compared the three curves and also the heatmaps.
    1. Plot the heatmap results for all the models.
1. Made a graphic abstract. https://drive.google.com/file/d/1XZNDbX757gzJedzSXaij7MmnVbwHviwG/view?usp=sharing
1. Cite the ACl google research article.

## 251110 ##

1. Dealt with the llm confidence problem.
    1. Test asking it to think about the both side, then check the final answer's logprob. It didn't really change.
    1. I figured out that the problem is that I am using the reasoning model. With the "hidden" reasoning step, the final answer tends to be really confidence with it's own answe.
        1. Test using non-reasoning model. The resulting probability is much lower, around 0.6.
        1. [Measuring Confidence in LLM responses](https://medium.com/@georgekar91/measuring-confidence-in-llm-responses-e7df525c283f)
        1. [Is there a way to determine a LLM's confidence in an answer?](https://www.reddit.com/r/LocalLLaMA/comments/1bw87q3/is_there_a_way_to_determine_a_llms_confidence_in/)
        1. [Improving data quality with confidence](https://www.refuel.ai/blog-posts/labeling-with-confidence)
        1. [Trustworthy Language Model (TLM) - Quickstart](https://help.cleanlab.ai/tlm/tutorials/tlm/#how-does-the-tlm-trustworthiness-score-work) -> 看來是用另一個llm來評分，這個感覺是可以用在我在求relavancy的時候
1. [Language models cannot reliably distinguish belief from knowledge and fact](https://www.nature.com/articles/s42256-025-01113-8)
1. True edges
    1. Updated SIGNOR data to Oct 2025.
    1. Sorted the True edges by Omnipath refs.
        1. Used the Omnipath api.
        1. Debugged edges without refs. I am now first using pubmed id from SIGNOR then use it to find the Omnipath ref. Then I double check the ones with no refs and use the source and target and interaction to find ref num.
    1. Filtered out the bidirectional edges.
    1. Filtered out edges with the same source node.
    1. Filtered out edges with the same target node.
    1. Write a script to test the difficulty of these edges. I test each candidate True edges with gpt-oss-20b EdgeMaster 5 times. If the EdgeMaster answer Yes for all the tests, then it means this edge is too easy thus we can remove the edge.
    1. Found [SIGNOR curation manual](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fsignor.uniroma2.it%2Fdocumentation%2FSIGNOR_curation_manual_July_2021.docx&wdOrigin=BROWSELINK)
    1. Wrote the description of the ground truth dataset preparation in the paper.

## 251103 ##

1. Start using gpt-oss-120b.
    1. Set up the llama.cpp model path.
    1. Changed the relavancy score to binary decision.
    1. Implemented ICL.
    1. Removed logits_bias.
    1. Read [OpenAI Harmony Response Format](https://cookbook.openai.com/articles/openai-harmony)
1. Tested both Travily and Searxng.
    1. Read [Best Practices for Search](https://docs.tavily.com/documentation/best-practices/best-practices-search)
    1. Add the Traviliy searching to my agent.
1. Run with vs without searching.
    1. Calculated the overall accuracy.
1. I was testing why the answering logprobs are all 0. It turns out, it was prompt problem. Instead of giving it so much constraint and wrong max_token setting. I remove all the redundent part and only ask it to return a single answer. It is not working quite good, probablly because I am using a bigger model and better formating prompt. It is now more following the prompt. Here I also list the things I have tried which did not work.
    1. Change reasoning.
    1. Asked it to think about both Yes/No possibility. "You need to think about both side of the Yes/No possibilities."
    1. Changed temperature. This one has a minor effect. It only worked after temerature > 25.
    1. I also tested to use instead of the exact logprob of the answer, I check the difference between the logprob of the answer and its' opposite. In the end, they are pure noise. I cannot get representitve confidence out of it.
1. Visualized the sentence logprobs.
1. Rewrote the prompt. Remove all the unnecessary (harmony prompt format) parts and do the formating. I also set the max_tokens to 51200, somehow it gives better result than -1. It's not that repeating anymore.
1. Debugged the token identification code.
1. Positive edge
    1. Focus on protein-protein interaction.
    1. Picked the nodes from the negative edges and used them as candidate nodes.
    1. Selected the positive edges which includes the negative edges' nodes.
1. [A Definition of AGI](https://arxiv.org/abs/2510.18212)
1. CovSyn
    1. Updated the cover letter. Make sure all our published papers are included and follows the chronologically in reverse order.
    1. Also point out that we think use of synthetic data represent a paradigm shift since only it allows us to know all quantities of interest for all individuals.
    1. Looked for the candidate editor.
    1. Solved conflicts.
    1. Submitted the article.


## 251020 ##

1. Build a simple agent. https://hackmd.io/0bNGGWGXTsSCPJk4IAWB9w?edit
    1. Debugged screen. Screen does not stop after node session closed. Using tmux can perfectly avoid the problem.
    1. Used confidence score as a loop condition. Implemented it under LangGraph structure.
        1. Test llama.cpp + langgraph.
        1. I tested if I can do llama.cpp strcutured output + logprobs. It turns out structured output does not support logprobs. Logprobs only works on pure text syntax.
        1. I also tried using two llm response approach. I first asked llm to think about the question and save the response in reasoning. Then I input the reasoning to llm and ask it to answer the question with only True or False. I also tried the ICL approach but the llm just can't generate single True/False answer so I decide to abandon this approach.
        1. Then I decided to use only ask llm once and then get the answering text token and get its' logprobs.
            1. Find the answer sentence.        
            1. Find the answer token in the anser sentence.
        1. Debugged llm repeating. I add prompt "First provide your reasoning, then on a new line write "Answer: Yes" or "Answer: No"".
    1. I was thinking using only confidence score does't make it as an agent. Because there is no llm participant in controlling the flow.
    1. I thus decide to use another llm to judge the reasoning to see if it really answering the question or it just generate some random text.
    1. Implemented the reflect_node for doing it. Now I set the confidence score 0.9 and relevance 0.7 as threshold.
    1. Generate a case that generate uncertain answer.
    1. Check if the agent can generate logprob, yes: 0.5 and No: 0.5 answer.
    1. Check Tavilysearch vs Searxng. The Searxng is free. For Tavily: 
        - 1,000 credits/month - Free. 
        - 4,000 credits/month - $30 ($0.0075/credit). 
        - Pay-as-you-go: $0.008/credit.
        - Basic search: 1 credit per request
        - Advanced search: 2 credits per request
1. Start writting Neurips paper.
    1. Downloaded the latex template.
    1. Wrote the first abstract.
1. Read [Understanding LLM Logprobs](https://medium.com/thinking-sand/understanding-llm-logprobs-029794105903)
1. Read [The Definitive Guide to LLM Temperatures](https://medium.com/thinking-sand/the-definitive-guide-to-llm-temperatures-abab311260a6)

## 251013 ##

1. Agent GRN
    1. Read [Improving Wikipedia verifiability with AI](https://www.nature.com/articles/s42256-023-00726-1)
        1. Check https://github.com/facebookresearch/side/blob/6dc4ee909655872dc0c822d9cdd0fd62fffa21d4/projects/verify_wikipedia/dpr/models/ranker_loss.py#L141
        1. Read [Document Ranking with a Pretrained Sequence-to-Sequence Model](https://arxiv.org/pdf/2003.06713). "the model is fine-tuned to produce the words "true" or "false" depending on whether the document is relevant or not to the query. At inference time, to compute probabilities for each query-document pair (in a reranking setting), we apply a softmax only on the logits of the "true" and "false" tokens. Hence, we rerank the documents according to the probabilities assigned to the "true" token. We arrived at this particular approach after some trial and error."
        1. Check [Using logprobs](https://cookbook.openai.com/examples/using_logprobs).
        1. Ollma doesn't suppport logprobs. https://github.com/ollama/ollama/issues/2415
        1. Check [optillm](https://github.com/codelion/optillm).
        1. llama.cpp
            1. Installed.
            1. Note is here https://hackmd.io/KreD_rv3RMCUYbXaLn1fmQ
    1. Web search
        1. add after:2018 in the search query.
        1. Dealt with the ddos problem.
            1. Applied random time delay.
            1. pmc is constantly not accessible. I thus exclude the pmc search results.
    1. Noted the useful github repos in my hackmd https://hackmd.io/i3-sLVu9Q7un7whI6VwfmQ.
1. CovSyn
    1. Changed the template following the Infectious Disease Modelling template.
        1. Main text.
        1. Read the author guide and added the missing sections.
            1. Author contributions.
        1. Changed to citet and citep.
        1. Proof reading Abstract and Intro.

## 250929 ##

1. Agent GRN
    1. I first test few questions with and without the web search.
        1. Does F2RL3 protein and GNAZ protein have up-regulate activity? -> 不管我直接拿sentence還是原始paper去問claude，它都回答沒有直接連接 -> Does F2RL3 binds to GNAZ?這樣就可以，用interact也可以 -> Does F2RL3 up-regulate GNAZ?這樣也可以，也許就只是問題不能這麼仔細
        1. Does MAPK3 protein upregulate SMAD4 protein? -> 好像直接問upregulate都會有問題，也許我需要改問法 -> Does MAPK3 protein enhance SMAD4 protein activity?還是false
        1. 這個case我寫Does SOD1 bind to BCL-2?，就是True了 -> claude: true, gpt-oss:20b with search: true, gpt-oss:20b: False
        1. 我用Claude測試"Does PKN1 up-regulates RAF1 phosphorylation? Return True or False."跟"Does PKN1 up-regulates RAF1?"，正確答案是True，結果沒有講phosphorylation反而是說對的答案
    1. Check Perplexica, Jina, and searxng
        1. Double check the difference between the ollma-web-search with these three.
        1. Read Jina reader documentation.
            1. https://github.com/GaryKu0/ollama-web-search, it also has the image reading function.
            1. https://github.com/jina-ai/reader
            1. I also find the local Jina reader implementation, https://github.com/intergalacticalvariable/reader. I might use this if I end up reach the api limit.
        1. Check CoexistAI.
    1. My searxng step is in here https://hackmd.io/@-jBg4U8YQJi3FHeTXfRhyA/SywzmDKiee.
    1. Implemented the [ollama-web-search](https://github.com/GaryKu0/ollama-web-search) to deal with our problem.
        1. Read signore edge. Defined the questions.
        1. Run 40 repeats for the 96 negative interaction edges. I did that with and without search.
    1. Compare the restuls with and without search. I do it with a heatmap. https://hackmd.io/dlaL8abrRC2PIYwdNBl9EQ?edit
    1. Sometime it has the api problem, it seems to be the pmi problem.
    1. 讀[Singularity实践教程 + Docker 转 Singularity 的避坑指南](https://blog.csdn.net/Tanqy1997/article/details/125304273)
    1. Read [Ollama Web search blog](https://ollama.com/blog/web-search) and [Ollama Web search](https://docs.ollama.com/web-search).

## 250922 ##

1. Agent GRN
    1. check [Upgrade Your AI Using Web Search - The Ollama Course](https://www.youtube.com/watch?v=GMlSFIp1na0&ab_channel=MattWilliams)
    1. Check [ollama-web-search](https://github.com/GaryKu0/ollama-web-search)
        1. Check their README.
        1. Tried using their api. I tried the serper api. The web is accessible, but I would need to change a lot on the code to make it works for searching. So I didn't complete it.
    1. check [CoexistAI](https://github.com/SPThole/CoexistAI)
    1. Tried installing docker in the cluster. It doesn't work since I don't have sudoer. Instead, I should use singularity.
    1. Check [Singularity #1 Introduction to Singularity and its difference with Docker](https://www.youtube.com/watch?v=_KhbwXqk0Bk)
    1. Check https://docs.searxng.org/admin/installation-docker.html#installation-docker.
    1. Chek https://www.reddit.com/r/LocalLLaMA/comments/1n9sod7/what_is_the_most_effective_way_to_have_your_local/. Some options are Perplexica (searxng wrapper with summary function), searxng (basic), open-webui (gui), coexistAI (lots of different functions).
    1. Implemented the ollama-wev-search.
    1. I tried CREB1 -> PCK1 and "Does TP53 protein downregulate BCL2L1?" with gpt-oss:20. I think I see some differences. The llm with search gives better result.
    1. Check [Group Relative Policy Optimization(GRPO) Visualized](https://www.youtube.com/watch?v=EX8-ucKOBbA&ab_channel=AGILambda)
1. COVID
    1. Add discussion of number of parameters in the model, number determined from prior literature, number identified based on fitting to data, number of data points used for fitting, number of parameters at bounds.
    1. Prepared the template and add the first page.

## 250916 ##

1. Agent GRN
    1. I updated the prompt and redo the llm edge denoising.
    1. Setup laptop ipynb and autocomplete.
    1. Look for signor negative edges.
        1. Downloaded each years' data.
    1. I first tried to use the source and target name to identified the removed edges, then I realize they have provide the id for each interaction.
    1. Used the signor ID to find the removed edges each year.
    1. Then I double check the source and target names of the removed edges which were identified by the ID, then I see some duplicate so I have removed those redundent edges.
    1. Check the complex BAK/BAX in the omniPath. I couldn't find it.
    1. Some of the nodes were completely missing in the 2025 graph. Since I want to find the minimum set of the removed edges, I decided to not considered the removed edges that contains the missing nodes.
    1. Why were there so many edges removed during 2021~2022. It seems there were a lot of ribosomal subunit related edges removed.
    1. I checked is there any removed edges added back to the 2025 list. I found only 1 which is {'old_signor_id': 'SIGNOR-170134', 'source_entity': 'TRPM7', 'target_entity': 'EEF2K', 'new_signor_id': 'SIGNOR-277923'}
    1. As the result, I identified 97 negative edges in signor dataset.
    1. Read [BioML-bench: Evaluation of AI Agents for End-to-End Biomedical ML](https://www.biorxiv.org/content/10.1101/2025.09.01.673319v2)
1. Check what is pyproject.toml and  __init__.py.
1. Check network topology and connectivity. I was focusing on the corrected_PKN_with_BRAF_fixes network.
    1. Check modularity and assortativity.
    1. Use Louvain algorithm to identified communities with maximizing the modularity. The modularity of the resulting communities is 0.4.
    1. Then I calculated the density for each of the communities.
    1. I also tried densest_subgraph function. But this one only works for the undirected graph.
    1. The assortativity is 0.9.
1. Check [Predicting transcriptional outcomes of novel multigene perturbations with GEARS](https://www.nature.com/articles/s41587-023-01905-6)
1. CovSyn
    1. Setup mac Latex.
    1. Presented CovSyn as a first step in a framework for benchmarking of epidemiological models and the current model as a first example of a highly specialised model demonstrating synthesis of an extreme case of COVID-19, i.e. Taiwan's first outbreak. 
    1. Stated that the aim of this framework is to enable systematic exploration of the linkage between data, modelling, analytics, and policy.
    1. Added the mata analysis article in our cover letter.
    1. Changed title to CovSynTW20: an agent-based model for synthesizing Taiwanese COVID-19 2020 course of disease and contact tracing data.
    1. Updated to say that it is a model generating synthetic data specifically for mimicing Taiwanese COVID-19 2020 outbreak
    1. Added description of Taiwanese contact tracing and isolation to motivate such a low R0.
    1. Clearly stated that this model is intended to represent this special case and not to generalise.
    1. Added the obvious example: The synthetic data can be used to compare models and show how closely they can forecast the synthetic data.
    1. Downloaded the Infectious Disease Modelling latex template.


## 250908 ##

1. Agent GRN correction
    1. Tested adding the ICL example invalid edges to the original network. It turns out the LLM just keeping throwing the ICL example as the answer. I also found out that the previous result was having similar promblem. That's probablly the reason why adding ICL example always resulting worse performance.
    1. I tried to let the examples and the PKN has the same structure and I add a prompt to ask llm to not reply any edges from the example list. Bus it does not help.
    1. Updated the random adding edges code. Now it won't add edges that cause the steps from the source node being greater than the original setting.
    1. Updated the prompt so that llm does not response the answer from the example list. Even through the llm still sometime did that. Moreover, after I have done such adjustment, llm tends to response more unstructure output.
    1. I was testing using general prompt, i.e. not specify that the llm is a molecular biologist expert. I basically just ask it to correct a graph based on its' own knowledge.
    1. I saw that the PKN has a link from MAPK1 to BRAF. I was thinking it might be an error since we also have BRAF to MAPK1. After I check the omniPath, I realized that both edges exist. But I guess the majority is BRAF -> MAPK1 since it has more refs.
    1. I also tested using another llm such as qwen3:30b and ollama. They did not perform well eigher.
    1. I think latter after I figured out a better prompt, I can add an argument to test ICL, COT, and other prompt technique.
    1. Read [Biomni-R0: Using RL to Hill-Climb Biomedical Reasoning Agents to Expert-Level](https://biomni.stanford.edu/blog/biomni-r0-technical-report/)
    1. Read [rbio1 - training scientific reasoning LLMs with biological world models as soft verifiers](https://www.biorxiv.org/content/10.1101/2025.08.18.670981v3)
    1. Check [🦜🔗 LangGraph](https://art.openpipe.ai/integrations/langgraph-integration)
    1. Check [langgraph-codeact](https://github.com/langchain-ai/langgraph-codeact)
    1. Read [LLM4GRN: DISCOVERING CAUSAL GENE REGULATORY NETWORKS WITH LLMS – EVALUATION THROUGH SYNTHETIC DATA GENERATION](https://arxiv.org/pdf/2410.15828)
    1. Read [Fuselinker: Leveraging Llm's Pre-Trained Text Embeddings and Domain Knowledge to Enhance Gnn-Based Link Prediction on Biomedical Knowledge Graphs](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4931757)
    1. Read [REBEL: Relation Extraction By End-to-end Language generation](https://aclanthology.org/2021.findings-emnlp.204/)
    1. Registered the nvidia workshop.

## 250902 ##

1. ICL test
    1. Read ICL
    1. Changed my prompt by providing valid and invalid examples with 10 edges for each.
        1. Focus on 3 layer network.
        1. Wrote a code to skip the result when there is no prediction at all because it generates a lot f1 0 cases.
    1. Checked how can I make the llm output follow the same structure. Eventually I used pydatic so that the llm generate json style output.
        1. Read https://llama.developer.meta.com/docs/features/structured-output
        1. Read https://ollama.ac.cn/blog/structured-outputs
        1. Read https://blog.cassdev.com/posts/llm-param-response-format/
        1. Watched https://www.youtube.com/watch?ab_channel=pixegami&t=131s&v=XIdQ6gO3Anc
        1. Debugged the code.
    1. Repeated the llm responsing for 100 times for each scenario. max_layer 3, repeat 100, add_nums 1, 2, 4, 8, 16, ICL_sizes 0, 10跑了345m52.4s -> ~5.8h. It turns out having example giving worst result than the original one.
    1. Added the explaination on the definition of valid and invalid edges. It also not helped.
1. Implemented mean reciprocal rank
    1. Read MRR.
    1. Corrected the prompt so that it generate the prediction in order. I ased the llm to predicted 16 edges.
    1. Calculated the MRR and saved them in all the results.
1. Setup zenodo.
1. Reset ollama paths
1. Read
    1. Benchmarking of signaling networks generated by large language models
    1. Extraction of molecular interaction networks with large language models
    1. [深入理解Reasoning LLMs](https://zhuanlan.zhihu.com/p/24869009949)
1. BRFSS
    1. Debugged Roven's code.
    1. Read https://stefvanbuuren.name/fimd/sec-pmm.html

    

## 250825 ##

1. Agent GRN
    1. Created a repository.
    1. Uploaded all my test code in the repository.
    1. Updated the Moon score plot title.
    1. Clean code
        1. Corrected ptah and cleaned code.
        1. Wrote the ignore file.
        1. Corrected R code.
        1. Put the results in Slack.
    1. Checked how many edges with 2 layers and 3 layers.
    1. Reading papers: Extraction of molecular interaction networks with large language models.
    1. Read LLM-Assisted Functional Gene Annotation.
    1. Learn MCP
        1. Watched https://www.youtube.com/watch?v=jGg_1h0qzaM&ab_channel=freeCodeCamp.org
        1. Set my mac mini conda environment.
    1. Test random added edges then ask llm to remove it.
        1. Start with the Biomni corrected network.
        1. Extracted the BRAF 2 layer network.
        1. Randomly add edges
        1. Implemented code for converting edge list to networkx to text llm input.
        1. Designed the new prompt.
        1. Check if the Biomni corrected network has cycle. The anser is yes.   
        1. Calculated the recovery precision, recall, and f1 score.
        1. I have done 30 times repeats and save the result.
        1. Plot the violin plot for the metrics.
1. Took the EBI picture.
1. BRFSS
    1. Added the excercise duration each time.
    1. Debugged the dummy encoding code.
    1. Changed the diabetes encoding way.
    1. Implemented the multiple imputation.
1. Review the causal mask in decoder.

## 250818 ##

1. I have finally settle down most of the thing in EBI.
1. Agent model GRN
    1. Setup the HPC codon cluster connection.
    1. Setup my Ollam enviroment on the HPC cluster.
    1. Setup the miniconda enviroment on the HPC cluster.
    1. Test llm's ability to reconstruct the GRN.
    1. I was tryingt to remove some of the edges from the original PKN and ask llm to reconstruct the missing edges.
        1. Design my prompt.
        1. Wrote the code to from pd table to text input for llm and another code to transform text output to llm.
        1. Implemented the basic reconstruction rate.
    1. I tried to use qwen3:8b with size 5.2 GB with the context window.
    1. Double check my reconstruction code.
    1. I tried to remove 6,761 edges and ask llm to reconstruct it. Basically none of the llm can reconstruct anything. Even biomni can only reconstruct 1 edge.
    1. I also tried to remove only 33 edges.
    1. Setup my R enviroment in the mac.
        1. Reinstall COSMOS. I did the github PAT setting. I have to install that from github repo so that I can access the moon function.
        1. Test the run_moon.R.
        1. Check the biomni logs.
1. I test if llm correction of GRN can help the final moon score.
    1. Run the moon score code with the initial PKN and also with the biomni PKN.
    1. I start with asking llm to correct the initial PKN by removing ONE edge it thinks shouldn't be there. I have tested 30 repetition and one of them shows a decreasing trend in the resulting MOON score, which is what we want. The one it removed is [REMOVE, MAP2K2, PPARG, 1]
    1. Note that Biomni removed 9 edges, which are BRAF → MAP4K1, MAP2K1 → TAL1, MAP2K1 → IRS1, MAP2K1 → GSK3B, MAP2K1 → CASP9, MAP2K1 → ARRB2, MAP2K1 → RPS6KA4, MAP2K2 → CASP9, MAP2K2 → PPARG.
    1. NOTE: I commented out all whe -which code in R since the edge removal should be done by the llm agent.
    1. I have wrote a code to help me get the downstream network with defined layer number. Here I use two layers only since I saw biomni was only focusing on the second layer and part of the third layer.
    1. Designed a new prompt for this task. NOTE: the reason I stop doing the random edge removal and edge reconstruction is that I think in the end we are evaluating the llm ability by MOON score. I am not so sure what is the purpose of testing llm's ability to reconstruct a network. If I latter find a good story to connect the moon score and the reconstruction ability, I will keep testing it.
    1. Saved all the results and plot the related MOON score.
    1. I tested also asking llm to correct the GRN by removing 2, 4, and 8 edges. I check their resulting MOON score. The 8 edges removed are for example:
        1. [REMOVE, MAP2K2, PPARG, 1], [REMOVE, MAP2K2, CASP9, -1], [REMOVE, MAP4K1, CARD11, 1], [REMOVE, MAP4K1, LCP2, 1],[REMOVE, MAP2K1, TAL1, -1], [REMOVE, MAP2K1, IRS1, -1], [REMOVE, MAP2K1, CASP9, -1], [REMOVE, MAP4K1, MAP3K1, 1]
        1. [REMOVE, MAP2K2, CASP9, -1], [REMOVE, MAP2K2, PPARG, 1], [REMOVE, MAP4K1, CARD11, 1], [REMOVE, MAP4K1, LCP2, 1], [REMOVE, MAP2K1, TAL1, -1], [REMOVE, MAP2K1, IRS1, -1], [REMOVE, MAP2K1, GSK3B, 1], [REMOVE, MAP2K1, CASP9, -1]
    1. Reset my enviroment, changed the ollama model path to nfs. Also reset the other python and ollama dependencies.
1. Scholarship
    1. Read Biomni
    1. Completed the on-board
1. Connected to slack
1. Completed the renting.
1. Transfered money to wise then transfer it to my monzo.
1. Checked the ebi on-boarding sheet.
1. Job hunting
    1. Checked Taiwan Nvidia.
    1. Googled
        1. 千里馬後找工作
        1. 博士找工作
        1. 找工作
1. BRFSS
    1. Debugged age told had cancer.
    1. Debugged variable index.
    1. Implemented the dummy encoding including health care, obese, and exercise.
    1. Read https://medium.com/we-talk-data/one-hot-encoding-vs-dummy-encoding-08d5f2665ca1
    1. Read https://ujangriswanto08.medium.com/step-by-step-guide-to-multivariate-logistic-regression-in-python-outline-7d08a416134a
    1. Meeting with Roven.
1. Studying
    1. Read Trajanoska2023
1. CovSyn
    1. Our paper was be claimed to have munipulating submission process problem. But it tured out it was their problem that they have flagged the wrong paper.

## 250718 ##

1. Read the blog posts about postdoc and industry.
1. Wrote the 104 CV first version.
    1. Updated my CV.
    1. Used the 104 AI tool to fill in the CV.
1. Used Claude to give me some comments on my CV. I saved the comments as a md file called cv_improvement_plan.md.
1. Put the Latex converter to my github.
    1. Corrected the code based on prof's comments.
    1. Created the github repository.
1. BRFSS
    1. Created a new enviroment with uv for this project.
    1. Read https://www.cdc.gov/brfss/annual_data/annual_2023.html.
    1. Check variables.
    1. Check what multivariate analysis I should use.
    1. Load all the necessary variables.
    1. Extract the data of breast cancer.
    1. Implemented the Multivariable Logistic Regression.
1. Scholarship
    1. Filled in the renting application form.
    1. Asked the renting supporting documents from the HR.
    1. Read the HR newcomer letter.
1. Graph NN
    1. Review on what is SEAL.
    1. Review on GAE and VGAE.

## 241231 ##

1. 參加2025 千里馬行前共識營
1. 看
    1. 簽證及入境須知 - 駐英國台北代表處 Taipei Representative Office in the U.K.
    1. 【英國簽證】2025全面電子化！eVISA申請步驟、使用優點一次看！ - 劍橋教育
    1. 看簽證豁免貼簽 (Get an exempt vignette) | 英國簽證移民服務 | 英途簽證 Into Visa
1. 看看EMBL-EBI官網有沒有提到這方面的問題
1. 寄信過去ebi問說簽證的東西

## 2410325 ##

1. 23~30的short conversation, short talk, and text completion.
1. Reviewed the 300 volcabulary.

## 240318 ##

1. 31~34的short conversation, short talk, and text completion.

## 240311 ##

1. 寫多益第五回

## 240306 ##

1. 報名多益
1. 寫NCKU兩回試題

## 240228 ##

1. 我決定報名3/31的多益考試
1. 複習196個多益單字
1. 複習文法
1. 寫NCKU兩回練習題

## 231011 ##

1. Read https://zhuanlan.zhihu.com/p/149186533.

## 230904 ##

1. 重新產生cropped image跟concentration
1. 處理torch tensor問題
1. 試data augmentation (rotation)
1. Train一個tinyVGG model，但是performance不佳
1. 完成Section 10課程

## 230828 ##

1. 看完Pytorch course 7~9
1. 查系統生物學的領導團隊跟書籍，順便看SBI他們paper都在寫甚麼，加入他們需要甚麼能力。

## 230821 ##

1. 完成Pytorch course 5 & 6
1. 讀讀Making Deep Learning Go Brrrr From First Principles
1. 整理郵件

## 230817 ##

1. I bought the Udemy open course "PyTorch for Deep Learning in 2023: Zero to Mastery".
1. I finished until section 4 and I have done the classification homework.

## 230814 ##

1. Manage to my todos.
1. 完成Pytorch course section 5.

## 230529 ##

1. Add the COMPSAC preprint to my CV and LinkedIn

## 230517 ##

1. 跑Peter找到的模型的sh檔
1. 測試data preprocessing
1. 訂義大利行程跟roman pass
1. 準備，目標公司，CV，PPT，參加Seminar模擬面試

## 230510 ##

1. Updated my linkedin profile. Add most of the courses, award, and publication on it.
1. 重寫linkedin about
1. 義大利訂房
## 230503 ##

1. 查米蘭，尼斯，摩納哥，佛羅倫斯的資料

## 230403 ##

1. 修改Honduras的git設定，把它改成ssh連線。
1. 處理Ubuntu的濾藍光程式。
1. 寄Linkedin邀請給Seminar講者。

## 230327 ##

1. 在ubuntu上重裝vscode
1. 整理我在taskade上的todo，把他改成動作的敘述，並加上deadline
1. 讀Sapiens ch1
1. 讀Systems biology simulation of dynamic network states ch1~ch6，大致上讀完，應該暫時不會讀下去
1. 大致更新Linkedin的Education資料
1. 測試git config

## 230313 ##

1. 讀Deep learning ch6
2. 過Linkedin Machine learning test.
3. 查一下Riken的組織以及internshit，看起來應該是直接處理千里馬計畫比較快

## 230303 ##

1. 過Linkedin Matlab test.
2. 讀Deep learning ch3~ch5.

## 230208 ##

1. 辦indeed，glassdoor，104的帳號
2. Check幾則linkedin上關於systems biology跟bioinformatics的工作，好像都是在處理NGS的data
3. 在Colab上設定pytorch跟GPU還有mount google drive
4. 寫李弘毅開放課程的HW1
5. Deep Learning with PyTorch ch1 and ch2

## 221228 ##

1. 設定colab，試用
2. 看deep learning week 1 lectures

## 221212 ##

1. 跟Seminar講者聊天(An-Chi Wei)
2. 參加GIW餐宴

## 221130 ##

1. 寫兩篇多益聽力

## 221107 ##

1. 處理會計相關的data

## 221031 ##

1. 學冰滴
2. 洗鞋
3. 寄英文諮詢文件
4. Make a table of habit list. https://docs.google.com/spreadsheets/d/1kGhHPQfNOy0xTSpWFhkD_LoLLzfyNwHLt3S4yiWEwVs/edit?usp=share_link

## 221024 ##

1. Memorized TOEIC vocabulary.
2. Wrote one TOEIC reading.
3. Made this wiki page.
4. Managed my tabs.
5. Clean all the mails.
6. Applied the 永豐 scholarship.

# Welcome

Welcome to your wiki! This is the default page we've installed for your convenience. Go ahead and edit it.

## Wiki features

This wiki uses the [Markdown](http://daringfireball.net/projects/markdown/) syntax. The [MarkDownDemo tutorial](https://bitbucket.org/tutorials/markdowndemo) shows how various elements are rendered. The [Bitbucket documentation](https://confluence.atlassian.com/x/FA4zDQ) has more information about using a wiki.

The wiki itself is actually a git repository, which means you can clone it, edit it locally/offline, add images or any other file type, and push it back to us. It will be live immediately.

Go ahead and try:

```
$ git clone https://Rain_wu_Nordlinglab@bitbucket.org/Rain_wu_Nordlinglab/rain-wu-personal.git/wiki
```

Wiki pages are normal files, with the .md extension. You can edit them locally, as well as creating new ones.

## Syntax highlighting


You can also highlight snippets of text (we use the excellent [Pygments][] library).

[Pygments]: http://pygments.org/


Here's an example of some Python code:

```python

def wiki_rocks(text):
    formatter = lambda t: "funky"+t
    return formatter(text)
```


You can check out the source of this page to see how that's done, and make sure to bookmark [the vast library of Pygment lexers][lexers], we accept the 'short name' or the 'mimetype' of anything in there.
[lexers]: http://pygments.org/docs/lexers/


Have fun!