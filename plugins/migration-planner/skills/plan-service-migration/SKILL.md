---
name: plan-service-migration
description: Plan a staged service migration. Use when moving systems, APIs, or storage without a full cutover at once.
version: 1.0.0
---

# Plan Service Migration

Create a migration path that reduces risk.

## When to Use

- A service, datastore, or API needs to be replaced
- The team wants phases instead of a big-bang migration
- Rollout, rollback, and compatibility details are unclear

## Instructions

1. Define source and target systems plus migration constraints.
2. Break the work into phases with measurable checkpoints.
3. Cover dual-write, read shadowing, or compatibility periods when relevant.
4. Make rollback points explicit.
5. End with key unknowns that need validation.
