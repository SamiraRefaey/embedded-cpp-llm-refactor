# Embedded C++ Code Refactoring using LLMs

Research-oriented AI engineering project for safer embedded C++ modernization and unit test generation. The implementation includes a deterministic local refactoring engine that mirrors the structure expected from an LLM-assisted workflow, plus metrics used to evaluate generated changes.

## Features

- Embedded C++ refactoring pipeline
- Rule-based baseline for LLM output comparison
- Unit test skeleton generation
- Maintainability and similarity metrics
- CLI demo and tests

## Run Locally

```bash
python -m pip install pytest
python -m pytest
python -m src.embedded_cpp_llm_refactor.cli samples/legacy_motor_controller.cpp
```

## Research Metrics

- AST similarity proxy
- CodeBLEU-style token overlap proxy
- Maintainability score
- Hallucination risk flags for unsafe generated APIs

## Production Extension

Use this repository as the non-confidential version of the M.Sc. research project. A production implementation can add:

- Tree-sitter C++ parsing
- LLM/SLM model adapters
- Prompt versioning
- Compiler-in-the-loop validation
- GoogleTest generation
- Static analysis with clang-tidy
