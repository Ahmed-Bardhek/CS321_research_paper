"""Evaluate model outputs.

This script extracts a predicted multiple-choice answer and compares it with the
reference answer.

Input:
    outputs/model_outputs/combined_model_outputs.json

Output:
    data/results/combined_results.csv
"""

from pathlib import Path
import json
import re
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT / "outputs" / "model_outputs" / "combined_model_outputs.json"
OUTPUT_PATH = ROOT / "data" / "results" / "combined_results.csv"

def extract_answer(text: str):
    match = re.search(r"\b([ABCD])\b", text.upper())
    return match.group(1) if match else None

def estimate_quality(correct: int, response_text: str) -> int:
    if correct and len(response_text.split()) >= 8:
        return 5
    if correct:
        return 4
    if len(response_text.split()) >= 8:
        return 2
    return 1

def main():
    records = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    rows = []

    for record in records:
        predicted = extract_answer(record["response_text"])
        correct = int(predicted == record["correct_answer"])

        rows.append({
            **record,
            "predicted_answer": predicted,
            "correct": correct,
            "quality_score": estimate_quality(correct, record["response_text"]),
            "input_tokens": len(record["prompt_text"].split()),
            "output_tokens": len(record["response_text"].split()),
            "total_tokens": len(record["prompt_text"].split()) + len(record["response_text"].split())
        })

    df = pd.DataFrame(rows)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Wrote evaluated results to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()