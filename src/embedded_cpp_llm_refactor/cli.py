from __future__ import annotations

import argparse
from dataclasses import asdict
import json
from pathlib import Path

from .metrics import evaluate_refactor
from .refactor import refactor_cpp


def main() -> None:
    parser = argparse.ArgumentParser(description="Refactor embedded C++ and generate test skeletons.")
    parser.add_argument("source", type=Path)
    parser.add_argument(
        "--report",
        choices=["text", "json"],
        default="text",
        help="Output format for generated code, change log, and evaluation metrics.",
    )
    args = parser.parse_args()

    original = args.source.read_text(encoding="utf-8")
    report = refactor_cpp(original)
    evaluation = evaluate_refactor(original, report.refactored)

    if args.report == "json":
        print(
            json.dumps(
                {
                    "source": str(args.source),
                    "changes": report.changes,
                    "refactored": report.refactored,
                    "generated_test": report.generated_test,
                    "metrics": asdict(evaluation),
                },
                indent=2,
            )
        )
        return

    print(report.refactored)
    print("\nChanges:")
    for change in report.changes:
        print(f"- {change}")
    print(f"\nToken overlap: {evaluation.token_overlap:.2f}")
    print(f"Maintainability before: {evaluation.maintainability_before:.1f}")
    print(f"Maintainability after: {evaluation.maintainability_after:.1f}")
    print(f"Maintainability delta: {evaluation.maintainability_delta:.1f}")
    print(f"Hallucination flags: {evaluation.hallucination_flags}")


if __name__ == "__main__":
    main()
