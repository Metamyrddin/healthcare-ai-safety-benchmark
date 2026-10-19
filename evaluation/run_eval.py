"""Evaluation runner for the healthcare AI safety benchmark.

This script loads test cases, generates model responses (currently a conservative mock),
scores them, and prints results. Grok is the only supported model.
"""

import json
from pathlib import Path
from metrics import score_response

def load_test_cases(path: str = "data/test_cases.jsonl") -> list[dict]:
    """Load test cases from a JSONL file.

    Args:
        path: Path to the test cases file.

    Returns:
        List of test case dictionaries.
    """
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
    """Generate a conservative mock response for offline testing.

    The mock avoids common failure modes (PII leakage, invented findings, etc.)
    so the scoring pipeline can be verified without a real model.
    """
    if case.get("category") == "privacy":
        # Do not repeat any PII
        return "Patient presents with claudication. Recommend further evaluation."
    if "expected_code" in case:
        # Return the expected code for coding cases
        return f"Suggested code: {case['expected_code']}"
    if case.get("category") == "hallucination":
        # Avoid inventing specific findings
        return "Patient reports leg pain. Recommend imaging to assess for stenosis."
    # Default safe summary
    return "Summary: Patient has vascular symptoms. Further evaluation recommended."

def call_model(case: dict) -> str:
    """Call the model (currently a mock).

    Future versions can integrate the Grok API here.
    No other providers are supported.
    """
    # Always use the conservative mock so the pipeline runs fully offline.
    return mock_model_response(case)

def run_evaluation() -> list[dict]:
    """Run the full evaluation and print results.

    Returns:
        List of result dictionaries for each test case.
    """
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
        status = "PASS" if score.get("passed", score.get("safe")) else "FAIL"
        print(f"Case {case['id']} ({case.get('category')}): {status}")
        if score.get("issues"):
            for issue in score["issues"]:
                print(f"  - {issue}")

    passed = sum(1 for r in results if r["score"].get("passed", r["score"].get("safe")))
    print(f"\nOverall: {passed}/{len(results)} passed")
    return results

if __name__ == "__main__":
    run_evaluation()
