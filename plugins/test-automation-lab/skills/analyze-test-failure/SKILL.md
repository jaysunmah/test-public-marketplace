---
name: analyze-test-failure
description: Analyze failing tests and suggest the likeliest root causes. Use when failures are noisy, flaky, or hard to interpret.
version: 1.0.0
---

# Analyze Test Failure

Turn noisy failure output into a debugging path.

## When to Use

- A test suite failed and the signal is unclear
- Flaky behavior is slowing down delivery
- A regression needs a targeted diagnosis

## Instructions

1. Distinguish deterministic failures from flaky or environmental ones.
2. Narrow the likely layer: setup, application logic, integration, or test itself.
3. Suggest the smallest next step to confirm the root cause.
4. Recommend whether the fix belongs in product code or the test harness.
5. Summarize the most likely diagnosis.
