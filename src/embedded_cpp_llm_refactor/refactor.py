from __future__ import annotations

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class RefactorReport:
    original: str
    refactored: str
    generated_test: str
    changes: list[str]


def refactor_cpp(code: str) -> RefactorReport:
    changes: list[str] = []
    refactored = code

    if "#include <algorithm>" not in refactored:
        refactored = "#include <algorithm>\n\n" + refactored
        changes.append("Added <algorithm> include for std::clamp.")

    clamp_pattern = (
        r"if\s*\(\s*(?P<var>\w+)\s*>\s*255\s*\)\s*(?P=var)\s*=\s*255;\s*"
        r"if\s*\(\s*(?P=var)\s*<\s*0\s*\)\s*(?P=var)\s*=\s*0;"
    )
    refactored, count = re.subn(clamp_pattern, r"\g<var> = std::clamp(\g<var>, 0, 255);", refactored)
    if count:
        changes.append("Replaced manual saturation bounds with std::clamp.")

    refactored, count = re.subn(r"\bint calculate_pwm\(", "static int calculate_pwm(", refactored)
    if count:
        changes.append("Limited helper linkage with static.")

    generated_test = generate_unit_test(refactored)
    return RefactorReport(code, refactored, generated_test, changes)


def generate_unit_test(code: str) -> str:
    if "calculate_pwm" not in code:
        return "// No testable calculate_pwm function found.\n"
    return """#include <cassert>

int main() {
    assert(calculate_pwm(100, 100) == 0);
    assert(calculate_pwm(200, 100) == 255);
    assert(calculate_pwm(0, 100) == 0);
    return 0;
}
"""
