from pathlib import Path

from embedded_cpp_llm_refactor.metrics import evaluate_refactor
from embedded_cpp_llm_refactor.refactor import refactor_cpp


def test_refactor_replaces_manual_bounds() -> None:
    code = Path("samples/legacy_motor_controller.cpp").read_text(encoding="utf-8")
    report = refactor_cpp(code)

    assert "std::clamp" in report.refactored
    assert "calculate_pwm" in report.generated_test

    evaluation = evaluate_refactor(code, report.refactored)
    assert evaluation.token_overlap > 0.6
    assert evaluation.maintainability_after > 70
    assert evaluation.maintainability_delta > 0
