"""Run selected LLMs on generated prompt variants.

This starter script defines the expected pipeline but does not include real API keys
or local model loading by default. Fill in the functions depending on the model provider.

Original mixed-model design:
    - GPT model: closed-source API model
    - Llama model: open-source model
    - Qwen/Mistral model: open-source model

Inputs:
    data/processed/prompt_variants.csv

Outputs:
    outputs/model_outputs/*.json
"""

from pathlib import Path
import json
import time
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PROMPTS_PATH = ROOT / "data" / "processed" / "prompt_variants.csv"
OUTPUT_DIR = ROOT / "outputs" / "model_outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

MODELS = [
    "GPT model",
    "Llama model",
    "Qwen/Mistral model",
]

def run_gpt_model(prompt: str) -> str:
    # TODO: Replace with a real API call.
    return "B.  response from GPT model."

def run_llama_model(prompt: str) -> str:
    # TODO: Replace with local Hugging Face, Ollama, LM Studio, or llama.cpp inference.
    return "B.  response from Llama model."

def run_qwen_mistral_model(prompt: str) -> str:
    # TODO: Replace with local Hugging Face, Ollama, LM Studio, or llama.cpp inference.
    return "B.  response from Qwen/Mistral model."

def run_model(model_name: str, prompt: str) -> str:
    if model_name == "GPT model":
        return run_gpt_model(prompt)
    if model_name == "Llama model":
        return run_llama_model(prompt)
    if model_name == "Qwen/Mistral model":
        return run_qwen_mistral_model(prompt)
    raise ValueError(f"Unknown model: {model_name}")

def main():
    prompts = pd.read_csv(PROMPTS_PATH)
    all_outputs = []

    for model_name in MODELS:
        model_outputs = []
        for _, row in prompts.iterrows():
            start = time.time()
            response = run_model(model_name, row["prompt_text"])
            end = time.time()

            record = {
                "question_id": row["question_id"],
                "subject": row["subject"],
                "model": model_name,
                "politeness_level": row["politeness_level"],
                "politeness_category": row["politeness_category"],
                "prompt_text": row["prompt_text"],
                "response_text": response,
                "correct_answer": row["correct_answer"],
                "response_time_seconds": round(end - start, 4)
            }
            model_outputs.append(record)
            all_outputs.append(record)

        safe_name = model_name.lower().replace("/", "_").replace(" ", "_")
        output_path = OUTPUT_DIR / f"{safe_name}_outputs.json"
        output_path.write_text(json.dumps(model_outputs, indent=2), encoding="utf-8")
        print(f"Wrote {output_path}")

    combined_path = OUTPUT_DIR / "combined_model_outputs.json"
    combined_path.write_text(json.dumps(all_outputs, indent=2), encoding="utf-8")
    print(f"Wrote {combined_path}")

if __name__ == "__main__":
    main()