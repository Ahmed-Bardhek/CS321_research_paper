"""Generate figures for the paper.

Input:
    data/results/combined_results.csv

Output:
    paper/figures/*.png
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT / "data" / "results" / "combined_results.csv"
FIG_DIR = ROOT / "paper" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

def save_accuracy_by_politeness(df):
    grouped = df.groupby("politeness_level")["correct"].mean().reset_index()

    plt.figure()
    plt.plot(grouped["politeness_level"], grouped["correct"], marker="o")
    plt.xlabel("Politeness level")
    plt.ylabel("Accuracy")
    plt.title("Accuracy by Politeness Level")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "accuracy_by_politeness.png", dpi=300)
    plt.close()

def save_token_usage(df):
    grouped = df.groupby("politeness_level")["total_tokens"].mean().reset_index()

    plt.figure()
    plt.bar(grouped["politeness_level"], grouped["total_tokens"])
    plt.xlabel("Politeness level")
    plt.ylabel("Average total tokens")
    plt.title("Token Usage by Politeness Level")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "token_usage.png", dpi=300)
    plt.close()

def save_response_time(df):
    grouped = df.groupby("politeness_level")["response_time_seconds"].mean().reset_index()

    plt.figure()
    plt.plot(grouped["politeness_level"], grouped["response_time_seconds"], marker="o")
    plt.xlabel("Politeness level")
    plt.ylabel("Average response time, seconds")
    plt.title("Response Time by Politeness Level")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "response_time.png", dpi=300)
    plt.close()

def main():
    df = pd.read_csv(INPUT_PATH)
    save_accuracy_by_politeness(df)
    save_token_usage(df)
    save_response_time(df)
    print(f"Figures saved to {FIG_DIR}")

if __name__ == "__main__":
    main()