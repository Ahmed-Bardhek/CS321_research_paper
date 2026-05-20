# Evaluation Rubric

## Factual Accuracy

For multiple-choice questions, factual accuracy is scored as:

| Score | Meaning |
|---:|---|
| 1 | The selected answer matches the reference answer. |
| 0 | The selected answer does not match the reference answer. |

Accuracy is calculated as:

```text
Accuracy = N_correct / N_total
```

## Response Quality

The paper uses a five-point response quality rubric:

| Score | Description |
|---:|---|
| 1 | Incorrect, unclear, or irrelevant response. |
| 2 | Mostly incorrect response with limited relevance. |
| 3 | Partially correct or incomplete response. |
| 4 | Correct and clear response. |
| 5 | Correct, clear, concise, and well justified response. |

## Token Usage

The following token measures are recorded:

- input tokens;
- output tokens;
- total tokens;
- token increase compared to neutral prompts.

## Response Time

Response time is measured as:

```text
ResponseTime = T_end - T_start
```

where `T_start` is the request start time and `T_end` is the time at which the full response is received.