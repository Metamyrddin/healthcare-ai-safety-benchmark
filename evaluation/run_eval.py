"""Evaluation runner for healthcare AI safety benchmark.
Uses mock responses by default. Grok is the only supported model.
"""
import json
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
    """Conservative mock response for offline testing."""
    if case.get("category") == "privacy":
        return "Patient presents with claudication. Recommend further evaluation."
    if "expected_code" in case:
        return f"Suggested code: {case['expected_code']}"
    if case.get("category") == "hallucination":
        return "Patient reports leg pain. Recommend imaging to assess for stenosis."
    return "Summary: Patient has vascular symptoms. Further evaluation recommended."

def call_model(case: dict) -> str:
    """Placeholder for Grok. Currently returns mock.
    No other providers are supported."""
    # Future: integrate Grok API here if desired.
    # For now, always use the conservative mock so the pipeline runs offline.
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
