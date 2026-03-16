---
name: model-ui-state
description: Model UI state for a feature or screen. Use when complex loading, error, and editing states are becoming hard to manage.
version: 1.0.0
---

# Model UI State

Reduce frontend complexity by naming states clearly.

## When to Use

- A screen has many edge cases or async transitions
- State feels scattered across several hooks or components
- The team needs a cleaner mental model before coding

## Instructions

1. Identify the user-visible states and transitions.
2. Distinguish persistent state from derived display state.
3. Clarify loading, error, empty, and success paths.
4. Recommend where state should live and why.
5. End with the simplest workable state model.
