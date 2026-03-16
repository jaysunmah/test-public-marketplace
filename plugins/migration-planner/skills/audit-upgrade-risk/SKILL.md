---
name: audit-upgrade-risk
description: Audit risks for framework or dependency upgrades. Use when planning a major version bump or infrastructure change.
version: 1.0.0
---

# Audit Upgrade Risk

Evaluate the blast radius of an upgrade before implementation starts.

## When to Use

- A major dependency or framework version is changing
- Build, runtime, or API compatibility may break
- The team wants a realistic rollout plan instead of guesswork

## Instructions

1. Identify the most likely breaking surfaces.
2. Group risks by compile-time, runtime, and operational impact.
3. Suggest a phased validation strategy.
4. Call out any required code mods or contract changes.
5. Summarize the safest rollout path.
