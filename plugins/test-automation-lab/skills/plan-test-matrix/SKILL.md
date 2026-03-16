---
name: plan-test-matrix
description: Plan a focused test matrix. Use when adding features, fixing regressions, or deciding what coverage matters most.
version: 1.0.0
---

# Plan Test Matrix

Design the smallest useful set of tests that protects the change.

## When to Use

- A feature or bug fix needs a test strategy
- Existing coverage feels broad but not confidence-building
- The team wants to avoid redundant test cases

## Instructions

1. Identify the highest-risk behaviors and boundaries.
2. Separate unit, integration, and end-to-end needs.
3. Prefer a few high-signal scenarios over exhaustive combinatorics.
4. Call out setup cost and test flakiness risks.
5. End with the recommended minimum coverage set.
