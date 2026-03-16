---
name: review-flag-lifecycle
description: Review feature-flag lifecycle risks. Use when flags accumulate, ownership is unclear, or cleanup gets skipped.
version: 1.0.0
---

# Review Flag Lifecycle

Treat flags as temporary infrastructure, not permanent clutter.

## When to Use

- Old flags are piling up
- Ownership and expiry are unclear
- Launches rely on flags without cleanup discipline

## Instructions

1. Identify the flag's purpose, owner, and expected lifespan.
2. Distinguish kill switches from release flags and experiments.
3. Flag stale conditions, dead branches, or unclear defaults.
4. Recommend cleanup checkpoints and ownership rules.
5. End with the main lifecycle risks.
