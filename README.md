# Healthcare AI Safety Benchmark

This project tests how safe and accurate AI models are when they work with healthcare information.

## What This Project Does

AI models are starting to help with medical tasks like reading doctor's notes, suggesting codes for billing, or answering questions about patient care. But they can make mistakes. Sometimes they invent facts, get too confident when they should be careful, or handle private information poorly.

This benchmark gives AI models a set of realistic healthcare situations and checks how well they do. It looks for specific problems like:

- Making up medical facts (hallucinations)
- Being too sure when the answer is unclear
- Leaking private patient information
- Treating different patients unfairly
- Not following safety rules when instructions conflict

## Why This Matters

Healthcare is high-stakes. A small mistake can affect real people. This project helps measure those risks so we can understand which models are safer to use and where they still need work.

## How It Works

1. We create test cases that look like real clinical notes or coding tasks.
2. We send those cases to different AI models.
3. We score the answers automatically and check some by hand.
4. We report what went wrong and how often.

## Project Structure

```
healthcare-ai-safety-benchmark/
├── README.md
├── requirements.txt
├── data/
│   └── test_cases.jsonl
├── evaluation/
│   ├── run_eval.py
│   └── metrics.py
└── results/
```

## Getting Started

```bash
pip install -r requirements.txt
python evaluation/run_eval.py
```

## License

MIT License.

## Contact

Created by Ram Setty.
