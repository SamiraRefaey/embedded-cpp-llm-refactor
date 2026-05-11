from __future__ import annotations

from dataclasses import dataclass
import re


TOKEN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*|\d+|==|<=|>=|[{}();,=*+-]")


@dataclass(frozen=True)
class EvaluationResult:
    token_overlap: float
    maintainability_before: float
    maintainability_after: float
    maintainability_delta: float
    hallucination_flags: list[str]


def tokens(code: str) -> list[str]:
    return TOKEN_RE.findall(code)


def token_overlap(reference: str, candidate: str) -> float:
    reference_tokens = set(tokens(reference))
    candidate_tokens = set(tokens(candidate))
    if not reference_tokens:
        return 0.0
    return len(reference_tokens & candidate_tokens) / len(reference_tokens)


def maintainability_proxy(code: str) -> float:
    line_count = max(len([line for line in code.splitlines() if line.strip()]), 1)
    branch_count = len(re.findall(r"\b(if|for|while|switch)\b", code))
    score = 100 - (line_count * 0.8) - (branch_count * 4.0)
    return max(0.0, min(100.0, score))


def hallucination_flags(code: str) -> list[str]:
    risky = []
    for api in ["delay", "malloc", "free", "new ", "delete "]:
        if api in code:
            risky.append(f"Potential embedded safety issue: {api.strip()}")
    return risky


def evaluate_refactor(original: str, candidate: str) -> EvaluationResult:
    before = maintainability_proxy(original)
    after = maintainability_proxy(candidate)
    return EvaluationResult(
        token_overlap=token_overlap(original, candidate),
        maintainability_before=before,
        maintainability_after=after,
        maintainability_delta=after - before,
        hallucination_flags=hallucination_flags(candidate),
    )
