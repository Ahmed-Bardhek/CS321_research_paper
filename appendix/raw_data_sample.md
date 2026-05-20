# Raw Data Sample

The paper reports  experimental results. The following fields are used for each model response.

| Field | Example |
|---|---|
| question_id | Q001 |
| subject | Computer Science |
| model | GPT model |
| politeness_level | P4 |
| prompt_text | For the following academic question, choose the correct answer and briefly justify it: ... |
| response_text | B. Queue uses First-In-First-Out ordering. |
| correct_answer | B |
| predicted_answer | B |
| correctness | 1 |
| quality_score | 5 |
| input_tokens | 40 |
| output_tokens | 82 |
| response_time_seconds | 1.91 |

For full aggregate values, see:

- `data/results/overall_accuracy_by_politeness.csv`
- `data/results/accuracy_by_politeness_category.csv`
- `data/results/token_usage_by_politeness.csv`
- `data/results/statistical_tests.csv`