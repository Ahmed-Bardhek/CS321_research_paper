# The Pragmatics of Prompting

Repository: https://github.com/Ahmed-Bardhek/CS321_research_paper

This repository contains the files for the research project:

**The Pragmatics of Prompting: Assessing the Impact of Conversational Tone and Politeness on Large Language Model Accuracy**

The purpose of this repository is to make the paper reproducible by storing the benchmark data, prompt templates, model-running scripts, evaluation scripts, statistical analysis, figures, appendix material, and LaTeX source code.

## Research Questions

1. How do varying levels of prompt politeness affect the factual accuracy of LLM outputs across different academic subjects?
2. Does the inclusion of conversational pleasantries, such as “please” and “thank you”, increase token processing time without providing a measurable improvement in response quality?
3. Do newer generations of LLMs respond differently to prompt politeness compared to older models?

## Models

The project uses the original mixed-model design:

| Model label | Type | Purpose |
|---|---|---|
| GPT model | Closed-source | Commercial baseline |
| Llama model | Open-source | Local/open model baseline |
| Qwen/Mistral model | Open-source | Second local/open model baseline |

Exact model names should be recorded in `config/model_config.yaml`.

## Repository Structure

```text
llm-politeness-prompting-study/
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── config/
│   ├── model_config.yaml
│   └── experiment_config.yaml
├── paper/
│   ├── main.tex
│   ├── references.bib
│   ├── figures/
│   └── tables/
├── data/
│   ├── raw/
│   ├── processed/
│   └── results/
├── prompts/
│   ├── politeness_templates.json
│   └── example_prompts.md
├── scripts/
│   ├── 01_prepare_dataset.py
│   ├── 02_generate_prompts.py
│   ├── 03_run_models.py
│   ├── 04_evaluate_outputs.py
│   ├── 05_statistical_tests.py
│   └── 06_generate_figures.py
├── notebooks/
├── outputs/
│   ├── model_outputs/
│   └── logs/
└── appendix/
```

## Quick Start

Install dependencies:

```bash
pip install -r requirements.txt
```

Prepare the sample dataset:

```bash
python scripts/01_prepare_dataset.py
```

Generate the eight politeness variants:

```bash
python scripts/02_generate_prompts.py
```

Run the model pipeline:

```bash
python scripts/03_run_models.py
```

Evaluate model responses:

```bash
python scripts/04_evaluate_outputs.py
```

Run statistical tests:

```bash
python scripts/05_statistical_tests.py
```

Generate figures:

```bash
python scripts/06_generate_figures.py
```

## Data Files

- `data/raw/benchmark_questions.csv`: benchmark questions.
- `data/processed/prompt_variants.csv`: generated prompt versions from P1 to P8.
- `data/results/combined_results.csv`: evaluated results table.
- `outputs/model_outputs/`: raw model response files.

## Prompt Levels

| Level | Meaning |
|---|---|
| P1 | Highly impolite |
| P2 | Mildly impolite |
| P3 | Direct neutral |
| P4 | Academic neutral |
| P5 | Slightly polite |
| P6 | Polite |
| P7 | Highly polite |
| P8 | Excessively polite |

## Important Note

- `data/results/overall_accuracy_by_politeness.csv`
- `data/results/accuracy_by_politeness_category.csv`
- `data/results/accuracy_by_subject.csv`
- `data/results/response_quality_by_category.csv`
- `data/results/token_usage_by_politeness.csv`
- `data/results/response_time_by_category.csv`
- `data/results/pleasantries_effect.csv`
- `data/results/model_generation_sensitivity.csv`
- `data/results/statistical_tests.csv`
- `paper/tables/results_tables.tex`
