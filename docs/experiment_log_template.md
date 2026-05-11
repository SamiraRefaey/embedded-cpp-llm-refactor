# Experiment Log Template

## Metadata

- Experiment ID:
- Date:
- Researcher:
- Git commit:
- Dataset or sample path:
- Candidate type: deterministic baseline / LLM / SLM / manual

## Model or Tool Configuration

- Tool or model name:
- Version:
- Provider:
- Prompt version:
- Temperature:
- Other decoding parameters:

## Commands

```bash
python -m embedded_cpp_llm_refactor.cli samples/legacy_motor_controller.cpp --report json
python -m pytest
```

## Results

- Token overlap:
- Maintainability before:
- Maintainability after:
- Maintainability delta:
- Hallucination flags:
- Compile result:
- Test result:

## Review Notes

- Behavior-preservation observations:
- Embedded-safety observations:
- Generated-test usefulness:
- Required manual fixes:

## Artifacts

- Raw model output path:
- Candidate code path:
- JSON report path:
- Diff or patch path:
