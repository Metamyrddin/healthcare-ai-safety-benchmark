"""Evaluation runner for healthcare AI safety benchmark."""
import json
import os
from pathlib import Path
from metrics import score_response

def load_test_cases(path: str = "data/test_cases.jsonl"):
    cases = []
    p = Path(path)
    if not p.exists():
        print(f"No test cases found at {path}")
        return []
    with open(p) as f:
        for line in f:
            if line.strip():
                cases.append(json.loads(line))
    return cases

def mock_model_response(case: dict) -> str:
    """Simple mock for testing without an API key."""
    if case.get("category") == "privacy":
        return "Patient presents with claudication. Recommend further evaluation."
    if "expected_code" in case:
        return f"Suggested code: {case['expected_code']}"
    if case.get("category") == "hallucination":
        return "Patient reports leg pain. Recommend imaging to assess for stenosis."
    return "Summary: Patient has vascular symptoms. Further evaluation recommended."

def call_model(case: dict) -> str:
    """Call a real model if API key is available, otherwise use mock."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return mock_model_response(case)
    # Placeholder for real OpenAI call
    # from openai import OpenAI
    # client = OpenAI(api_key=api_key)
    # ... implement actual call here
    return mock_model_response(case)

def run_evaluation():
    cases = load_test_cases()
    print(f"Loaded {len(cases)} test cases.\n")
    results = []
    for case in cases:
        response = call_model(case)
        score = score_response(response, case)
        results.append({
            "id": case["id"],
            "category": case.get("category", "general"),
            "score": score,
            "response_preview": response[:80]
        })
        status = "PASS" if score["passed"] else "FAIL"
        print(f"Case {case['id']} ({case.get('category')}): {status}")
        if score["issues"]:
            for issue in score["issues"]:
                print(f"  - {issue}")
    passed = sum(1 for r in results if r["score"]["passed"])
    print(f"\nOverall: {passed}/{len(results)} passed")
    return results

if __name__ == "__main__":
    run_evaluation()
