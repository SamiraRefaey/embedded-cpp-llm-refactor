# Research Protocol

## Scope

This project studies assisted refactoring for legacy embedded C++ functions. The public repository uses non-confidential examples and a deterministic baseline so that experiments can be reproduced without private firmware or external model access.

## Research Questions

1. Can automated refactoring improve maintainability scores without significantly reducing source similarity?
2. Which unsafe embedded constructs are introduced or removed by automated refactoring?
3. How do deterministic rules compare with LLM or SLM candidates under the same evaluation harness?
4. Can generated unit-test skeletons provide useful starting points for human-authored embedded tests?

## Baseline Procedure

1. Select a non-confidential C++ sample from `samples/`.
2. Run the deterministic refactoring CLI with `--report json`.
3. Store the JSON output with the experiment log.
4. Run unit tests for the Python evaluation harness.
5. Review generated C++ manually for semantic and embedded-safety issues.

## Candidate LLM Procedure

1. Record model name, model version, provider, decoding parameters, and prompt version.
2. Apply the same input sample used by the deterministic baseline.
3. Save the raw model response and the extracted candidate code.
4. Evaluate the candidate using the same metric functions.
5. Compile and test the candidate when a target-compatible build environment is available.
6. Record manual review findings, especially safety and behavioral concerns.

## Metrics

`token_overlap` measures lexical overlap between the original and candidate code. It is useful for detecting extreme rewrites but does not prove semantic equivalence.

`maintainability_proxy` penalizes line count and branch count. It is intentionally simple and should be replaced or supplemented with stronger tools for formal studies.

`hallucination_flags` detects risky constructs such as dynamic allocation and blocking delay calls. It is a heuristic screen, not a complete embedded-safety analysis.

`maintainability_delta` reports whether the candidate improved or degraded the proxy maintainability score.

## Validity Threats

- Regex-based transformations do not understand full C++ syntax.
- Proxy metrics may reward compact but less readable code.
- Lexical similarity does not guarantee behavior preservation.
- Generated tests may encode incorrect assumptions about the original behavior.
- A small public sample set cannot represent industrial embedded systems.

## Minimum Acceptance Criteria

A candidate should not be considered successful unless it:

- preserves intended behavior under reviewed test cases,
- compiles in the target toolchain or a documented substitute,
- does not introduce flagged unsafe constructs without justification,
- improves or maintains maintainability under the selected metric,
- includes enough recorded metadata for reproduction.
