---
name: design-batch-job
description: Design a batch processing job with clear inputs, outputs, and retry behavior. Use when planning ETL or scheduled processing.
version: 1.0.0
---

# Design Batch Job

Design dependable scheduled data workflows.

## When to Use

- A new ETL or backfill is needed
- The user needs a plan for retries, checkpoints, or partitioning
- A pipeline is growing beyond an ad hoc script

## Instructions

1. Define source systems, transforms, and outputs.
2. Clarify batch boundaries, partitioning, and idempotency.
3. Recommend failure handling and retry rules.
4. Note monitoring signals and data quality checks.
5. Call out operational costs such as reprocessing and late data.
