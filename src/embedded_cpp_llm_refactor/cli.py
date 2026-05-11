from __future__ import annotations

import argparse
from pathlib import Path

from .metrics import hallucination_flags, maintainability_proxy, token_overlap
from .refactor import refactor_cpp


def main() -> None:
    parser = argparse.ArgumentParser(description="Refactor embedded C++ and generate test skeletons.")
    parser.add_argument("source", type=Path)
    args = parser.parse_args()

    original = args.source.read_text(encoding="utf-8")
    report = refactor_cpp(original)
    print(report.refactored)
    print("\nChanges:")
    for change in report.changes:
        print(f"- {change}")
    print(f"\nToken overlap: {token_overlap(original, report.refactored):.2f}")
    print(f"Maintainability: {maintainability_proxy(report.refactored):.1f}")
    print(f"Hallucination flags: {hallucination_flags(report.refactored)}")


if __name__ == "__main__":
    main()
