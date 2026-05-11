# Embedded C++ Refactoring with LLM Assistance

This repository is a research-oriented prototype for studying how LLM-assisted workflows can modernize legacy embedded C++ and generate starter unit tests while preserving safety constraints.

The current implementation is intentionally deterministic. It provides a transparent local baseline that can be compared against future LLM or SLM outputs without relying on private source code, paid APIs, or nondeterministic model behavior.

## Research Goals

- Evaluate whether automated refactoring can improve maintainability of embedded C++ snippets.
- Compare deterministic rules with LLM-generated refactoring candidates.
- Track unsafe generated constructs, including dynamic allocation and blocking delay calls.
- Generate simple unit-test skeletons that can be extended into framework-specific tests.
- Keep the public repository reproducible and free of confidential production code.

## Repository Layout

```text
src/embedded_cpp_llm_refactor/   Python package and CLI
samples/                         Non-confidential embedded C++ sample inputs
tests/                           Pytest regression tests
docs/research_protocol.md         Methodology, metrics, and validity notes
docs/experiment_log_template.md   Template for recording model experiments
```

## Quick Start

```bash
python -m pip install -e .
python -m pip install -r requirements-dev.txt
python -m pytest
python -m embedded_cpp_llm_refactor.cli samples/legacy_motor_controller.cpp
```

Structured output for experiment logging:

```bash
python -m embedded_cpp_llm_refactor.cli samples/legacy_motor_controller.cpp --report json
```

If installed as a package, the CLI entry point is:

```bash
embedded-cpp-refactor samples/legacy_motor_controller.cpp --report json
```

## Current Baseline

The deterministic baseline performs a small, auditable set of transformations:

- Adds required standard-library includes for generated replacements.
- Replaces simple manual PWM saturation logic with `std::clamp`.
- Limits helper function linkage where appropriate.
- Generates a minimal assertion-based unit-test skeleton.
- Computes maintainability, token-overlap, and embedded-safety risk metrics.

## Metrics

The repository currently includes lightweight proxy metrics:

- `token_overlap`: lexical similarity between the original and candidate code.
- `maintainability_proxy`: line and branch-count based maintainability score.
- `hallucination_flags`: heuristic detection of risky embedded APIs.
- `maintainability_delta`: difference between candidate and original scores.

These metrics are not substitutes for compiler validation, hardware-in-the-loop testing, or expert review. They are included to make the baseline measurable and reproducible while future work adds stronger analysis.

## Research Extensions

Planned extensions for a fuller MSc or publication-quality study:

- Tree-sitter or clang-based C++ parsing.
- Prompt and model version tracking.
- Compiler-in-the-loop validation.
- GoogleTest or Unity/Ceedling test generation.
- Static analysis with `clang-tidy` and MISRA-oriented checks.
- Dataset manifests with anonymization notes.
- Statistical comparison of deterministic, LLM, and SLM variants.

## Reproducibility

Record every experiment using [docs/experiment_log_template.md](docs/experiment_log_template.md). At minimum, log:

- input sample or dataset version,
- tool or model version,
- prompt version if using an LLM,
- generated diff or output artifact,
- metric output,
- compile/test result,
- manual safety-review notes.

## Limitations

This repository does not claim production-ready semantic refactoring. The current parser is regex-based, the test generator is illustrative, and the metrics are proxies. Production use requires proper C++ parsing, compilation, static analysis, target-specific constraints, and reviewer approval.
