---
name: review-slow-query
description: Review a slow query and suggest likely improvement paths. Use when performance bottlenecks seem query-related.
version: 1.0.0
---

# Review Slow Query

Investigate query performance without jumping straight to rewrites.

## When to Use

- A query became slow in production or staging
- A report or endpoint is timing out
- The team needs a first-pass tuning review

## Instructions

1. Identify filters, joins, sorts, and scan-heavy operations.
2. Note likely index, cardinality, or data-shape concerns.
3. Distinguish query-shape issues from schema issues.
4. Recommend the smallest high-leverage change first.
5. Summarize the likely cause of slowness.
