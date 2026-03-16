---
name: plan-schema-tuning
description: Plan schema tuning or indexing work. Use when a workload outgrows its original database shape.
version: 1.0.0
---

# Plan Schema Tuning

Improve database performance with manageable structural changes.

## When to Use

- Hot paths no longer fit the original schema
- Reads or writes need more predictable scaling
- Index strategy is unclear or outdated

## Instructions

1. Identify the read and write patterns that matter most.
2. Review table growth, skew, and access frequency assumptions.
3. Recommend index, partitioning, or denormalization options carefully.
4. Call out migration and write-amplification tradeoffs.
5. End with a phased tuning plan.
