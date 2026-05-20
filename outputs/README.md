# Outputs Folder

This folder contains generated output files for the LLM politeness experiment.

## Contents

```text
outputs/
├── model_outputs/
│   ├── gpt_model_outputs.json
│   ├── llama_model_outputs.json
│   ├── qwen_mistral_model_outputs.json
│   ├── combined_model_outputs.json
│   └── combined_model_outputs.csv
├── logs/
│   ├── experiment_log.txt
│   └── run_metadata.json
└── summaries/
    ├── run_summary.json
    └── output_summary.md
```

## File Descriptions

- `gpt_model_outputs.json`: generated outputs for the GPT model condition.
- `llama_model_outputs.json`: generated outputs for the Llama model condition.
- `qwen_mistral_model_outputs.json`: generated outputs for the Qwen/Mistral model condition.
- `combined_model_outputs.json`: all generated output records combined.
- `combined_model_outputs.csv`: compact tabular version of the combined outputs.
- `experiment_log.txt`: human-readable log of the output-generation run.
- `run_metadata.json`: machine-readable run metadata.
- `output_summary.md`: readable summary of aggregate output metrics.
