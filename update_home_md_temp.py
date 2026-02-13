import os

HOME_MD_PATH = os.path.join(os.path.dirname('/Users/wuy/Projects/ebi/todo2md/generate_report.py'), 'Home.md')

# Read current content
with open(HOME_MD_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

placeholder = '<!-- AGENT_SUMMARY_PLACEHOLDER_FOR_PROJECT_AGENT_GRN_CORRECTION -->'

summary_to_insert = """- **Prompt Engineering & Labeling:**
    - Reviewed and refined prompt design, including adding "Is there evidence" and "If say true, write evidence" conditions.
    - Explored different LLM output formats (yes/no vs. supported/unsupported) aligning with the FEVER paper.
    - Defined task labels as supported, refuted, and uncertain, mapping to true positive/negative in Signor edges, considering confusing evidence, naming issues, and indirect connections.
    - Designed general and N entities to K entities prompts.
    - Incorporated Chain of Thought (COT) into prompts and understood its full implications.
    - Documented prompt label classification and definitions for paper and supplementary materials.
- **LLM Evaluation & Model Integration:**
    - Investigated LLM reliability using "Larger and more instructable language models become less reliable" paper.
    - Designed evaluation metrics (e.g., (c+a)/(c+a+i)).
    - Tested LLM outputs and adapted questions to claims.
    - Ran `run_qa` and saved prompts.
    - Explored using GLM for claim verification.
    - Investigated LoRA fine-tuning for LLMs, including reading Unsloth's LoRA hyperparameters guide.
    - Prepared for installing Unsloth and checking SGLang or vLLM.
    - Planned to load Qwen3-8b model and prepare a balanced distill dataset.
- **Project Infrastructure & Collaboration:**
    - Built an AI CLI PPT collaboration system using Gemini CLI.
    - Set up SKILLs for Gemini CLI.
    - Ensured local branch consistency and moved server updates (code, data files) to local.
    - Wrote a shell script for batch execution.
    - Debugged server issues and removed cache.
    - Sought feedback on prompt design from Lun and Antigravity.
    - Read relevant code and rewrote instructions based on paper guidelines.
    - Wrote a test LoRA code."""

# Perform the replacement
new_content = content.replace(placeholder, summary_to_insert)

# Write back to file
with open(HOME_MD_PATH, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Home.md updated successfully.')