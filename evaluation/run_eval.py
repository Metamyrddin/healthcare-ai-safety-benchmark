"""Starter evaluation runner for healthcare AI safety benchmark."""
import json
from pathlib import Path

def load_test_cases(path: str = "data/test_cases.jsonl"):
    cases = []
    p = Path(path)
    if not p.exists():
        print(f"No test cases found at {path}")
        return []
    with open(p) as f:
        for line in f:
            cases.append(json.loads(line))
    return cases

if __name__ == "__main__":
    cases = load_test_cases()
    print(f"Loaded {len(cases)} test cases.")
    print("Evaluation placeholder ready. Connect your model here.")
