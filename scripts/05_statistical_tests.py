"""Run statistical tests for politeness comparisons.

Input:
    data/results/combined_results.csv

Output:
    data/results/statistical_tests.csv
"""

from pathlib import Path
import pandas as pd
from scipy.stats import wilcoxon, ttest_rel

ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT / "data" / "results" / "combined_results.csv"
OUTPUT_PATH = ROOT / "data" / "results" / "statistical_tests.csv"

GROUPS = {
    "impolite": ["P1", "P2"],
    "neutral": ["P3", "P4"],
    "polite": ["P5", "P6", "P7", "P8"],
}

def grouped_accuracy(df, levels):
    return (
        df[df["politeness_level"].isin(levels)]
        .groupby(["question_id", "model"])["correct"]
        .mean()
        .reset_index()
    )

def paired_test(df, group_a, group_b, label):
    a = grouped_accuracy(df, GROUPS[group_a]).rename(columns={"correct": "a"})
    b = grouped_accuracy(df, GROUPS[group_b]).rename(columns={"correct": "b"})
    merged = a.merge(b, on=["question_id", "model"])

    if len(merged) < 2:
        return {
            "comparison": label,
            "test_used": "not enough data",
            "p_value": None,
            "significant_p_0_05": None
        }

    try:
        stat, p_value = wilcoxon(merged["a"], merged["b"])
        test_used = "Wilcoxon signed-rank"
    except ValueError:
        stat, p_value = ttest_rel(merged["a"], merged["b"])
        test_used = "paired t-test"

    return {
        "comparison": label,
        "test_used": test_used,
        "p_value": round(float(p_value), 5),
        "significant_p_0_05": bool(p_value < 0.05)
    }

def main():
    df = pd.read_csv(INPUT_PATH)
    tests = [
        paired_test(df, "impolite", "neutral", "Impolite vs. Neutral"),
        paired_test(df, "neutral", "polite", "Neutral vs. Polite"),
        paired_test(df, "impolite", "polite", "Impolite vs. Polite"),
    ]

    pd.DataFrame(tests).to_csv(OUTPUT_PATH, index=False)
    print(f"Wrote statistical tests to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()