---
name: review-module-boundaries
description: Review module boundaries for cohesion and dependency health. Use when teams suspect architectural drift.
version: 1.0.0
---

# Review Module Boundaries

Look for architectural drift before suggesting major rewrites.

## When to Use

- A backend package feels hard to reason about
- Responsibilities are split across the wrong layers
- New work keeps adding coupling instead of clarity

## Instructions

1. Identify the main responsibilities of each module.
2. Flag leaky abstractions or circular dependencies.
3. Distinguish structural issues from naming-only problems.
4. Recommend boundary changes that reduce future churn.
5. Summarize the highest-value cleanup opportunities.
