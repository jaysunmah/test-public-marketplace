---
name: plan-backend-refactor
description: Plan an incremental backend refactor. Use when service boundaries, module ownership, or dependency direction have become messy.
version: 1.0.0
---

# Plan Backend Refactor

Create a low-risk plan for untangling backend code.

## When to Use

- A service or module has grown too broad
- Dependency direction is unclear or cyclic
- The team wants an incremental cleanup plan

## Instructions

1. Identify the current seam lines and ownership boundaries.
2. Separate mechanical extraction from behavioral changes.
3. Prefer staged moves that preserve runtime behavior.
4. Call out integration points and rollback concerns.
5. End with the smallest useful first step.
