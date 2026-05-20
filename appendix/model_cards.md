# Model Cards / Model Details

The paper uses the original mixed-model design: one closed-source model and two open-source models.

| Model label | Exact model name | Version/date | Type | Access method | Temperature | Max output tokens |
|---|---|---|---|---|---:|---:|
| GPT model | gpt-4o-mini-2024-07-18 | API snapshot recorded on 2026-05-20 | Closed-source | OpenAI-compatible API | 0.0 | 256 |
| Llama model | meta-llama/Llama-3.1-8B-Instruct | Hugging Face checkpoint downloaded on 2026-05-20 | Open-source | Local inference using Transformers | 0.0 | 256 |
| Qwen/Mistral model | Qwen/Qwen2.5-7B-Instruct | Hugging Face checkpoint downloaded on 2026-05-20 | Open-source | Local inference using Transformers | 0.0 | 256 |

## Sample Hardware Details

| Field | Sample value |
|---|---|
| CPU | Intel Core i7-12700H |
| GPU | NVIDIA RTX 4060 Laptop GPU, 8GB VRAM |
| RAM | 32GB |
| Operating system | Windows 11 with WSL2 Ubuntu 22.04 |
| Python version | 3.11 |
| Random seed | 42 |
| Quantization | 4-bit for local models |

## Reproducibility Notes

