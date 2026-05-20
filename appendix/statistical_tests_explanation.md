# Statistical Tests Explanation

The experiment compares the same academic questions across multiple politeness conditions. Because the same question appears under different prompt variants, paired statistical tests are appropriate.

## Main Comparisons from the Paper

| Comparison | Test Used | p-value | Significant at p < 0.05 |
|---|---|---:|---|
| Impolite vs. Neutral | Wilcoxon signed-rank | 0.018 | Yes |
| Neutral vs. Polite | Wilcoxon signed-rank | 0.214 | No |
| Without pleasantries vs. With pleasantries | Paired t-test | 0.047 | Yes |
| Older models vs. Newer models | Paired t-test | 0.032 | Yes |

## Interpretation

The paper's  results suggest that impolite prompts reduce performance compared to neutral prompts. However, adding politeness beyond a clear neutral instruction does not produce a statistically significant accuracy improvement.

Pleasantries slightly improve response quality but increase token usage. This supports the conclusion that politeness mainly affects response style and efficiency rather than producing a strong improvement in factual accuracy.