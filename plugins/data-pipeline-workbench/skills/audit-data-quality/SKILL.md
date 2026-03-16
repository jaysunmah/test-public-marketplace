---
name: audit-data-quality
description: Audit data quality risks and suggest validation checks. Use when metrics drift, backfills fail, or tables seem unreliable.
version: 1.0.0
---

# Audit Data Quality

Review the trustworthiness of a data pipeline.

## When to Use

- Table counts or dashboard metrics changed unexpectedly
- A backfill produced suspicious results
- The team wants stronger validation around a dataset

## Instructions

1. Identify critical fields, joins, and derived metrics.
2. Suggest freshness, null, uniqueness, and range checks.
3. Highlight lineage gaps and silent failure modes.
4. Recommend alert thresholds that avoid noise.
5. Summarize the top integrity risks.
