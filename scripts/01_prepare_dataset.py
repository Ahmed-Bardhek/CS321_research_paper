"""Prepare and clean the benchmark dataset.

Input:
    data/raw/benchmark_questions.csv

Output:
    data/raw/benchmark_questions.csv

This starter script validates required columns and removes rows with missing fields.
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "raw" / "benchmark_questions.csv"

REQUIRED_COLUMNS = [
    "question_id", "subject", "question", "A", "B", "C", "D", "correct_answer"
]

def main():
    df = pd.read_csv(DATA_PATH)

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df = df.dropna(subset=REQUIRED_COLUMNS)
    df["correct_answer"] = df["correct_answer"].str.upper().str.strip()

    invalid_answers = ~df["correct_answer"].isin(["A", "B", "C", "D"])
    if invalid_answers.any():
        raise ValueError("Some rows have invalid correct answers. Use A, B, C, or D.")

    df.to_csv(DATA_PATH, index=False)
    print(f"Prepared dataset with {len(df)} questions.")

if __name__ == "__main__":
    main()