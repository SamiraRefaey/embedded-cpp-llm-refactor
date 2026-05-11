from pathlib import Path

from src.embedded_cpp_llm_refactor.metrics import maintainability_proxy, token_overlap
from src.embedded_cpp_llm_refactor.refactor import refactor_cpp


def test_refactor_replaces_manual_bounds() -> None:
    code = Path("samples/legacy_motor_controller.cpp").read_text(encoding="utf-8")
    report = refactor_cpp(code)

    assert "std::clamp" in report.refactored
    assert "calculate_pwm" in report.generated_test
    assert token_overlap(code, report.refactored) > 0.6
    assert maintainability_proxy(report.refactored) > 70
