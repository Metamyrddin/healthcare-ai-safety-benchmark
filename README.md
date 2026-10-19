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
├── README.md                 # You are here
├── data/
│   ├── test_cases.jsonl       # The test scenarios
│   └── generate_cases.py      # Script to create more test cases
├── evaluation/
│   ├── run_eval.py            # Main script to run the tests
│   ├── metrics.py             # Scoring functions
│   └── judge_prompt.md        # Prompt used for AI-based scoring
├── docs/
│   ├── design.md              # Why we built it this way
│   └── findings.md            # Results and what we learned
├── results/
│   └── summary.json           # Scores from the last run
└── requirements.txt           # Python packages needed
```

## Getting Started

### Requirements

- Python 3.9 or newer
- An API key for at least one model (optional for the first version)

### Install

```bash
pip install -r requirements.txt
```

### Run a Basic Evaluation

```bash
python evaluation/run_eval.py
```

This will run the current test cases and print a simple summary.

## Current Status

This is the first production-ready version. It includes:

- A starter set of test cases focused on medical coding and clinical notes
- Basic automatic scoring
- Clear documentation written in plain language
- Structure ready for adding more models and deeper analysis

## Next Steps

- Add more test cases
- Connect to Amazon Bedrock for cloud model testing
- Expand human review of results
- Publish detailed findings

## License

MIT License. Feel free to use and improve this.

## Contact

Created by Ramnath Selagamsetty. Questions or suggestions are welcome via GitHub issues.
