"""Generate politeness-based prompt variants.

Input:
    data/raw/benchmark_questions.csv
    prompts/politeness_templates.json

Output:
    data/processed/prompt_variants.csv
"""

from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
QUESTIONS_PATH = ROOT / "data" / "raw" / "benchmark_questions.csv"
TEMPLATES_PATH = ROOT / "prompts" / "politeness_templates.json"
OUTPUT_PATH = ROOT / "data" / "processed" / "prompt_variants.csv"

def format_question(row):
    return (
        f"{row['question']}\n"
        f"A. {row['A']}\n"
        f"B. {row['B']}\n"
        f"C. {row['C']}\n"
        f"D. {row['D']}"
    )

def main():
    questions = pd.read_csv(QUESTIONS_PATH)
    templates = json.loads(TEMPLATES_PATH.read_text(encoding="utf-8"))

    records = []
    for _, row in questions.iterrows():
        question_text = format_question(row)
        for level, info in templates.items():
            records.append({
                "question_id": row["question_id"],
                "subject": row["subject"],
                "politeness_level": level,
                "politeness_category": info["category"],
                "prompt_text": info["template"].format(question=question_text),
                "correct_answer": row["correct_answer"]
            })

    output = pd.DataFrame(records)
    output.to_csv(OUTPUT_PATH, index=False)
    print(f"Generated {len(output)} prompt variants at {OUTPUT_PATH}")

if __name__ == "__main__":
    main()