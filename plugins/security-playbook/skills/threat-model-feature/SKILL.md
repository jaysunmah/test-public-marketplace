---
name: threat-model-feature
description: Threat-model a feature or workflow. Use when adding auth, payments, admin access, or sensitive data handling.
version: 1.0.0
---

# Threat Model Feature

Perform a lightweight but practical threat review.

## When to Use

- A feature handles sensitive data or privileged access
- The user wants a security lens before implementation
- The system boundary or trust model is changing

## Instructions

1. Identify actors, assets, and trust boundaries.
2. List realistic abuse cases and likely attacker goals.
3. Review input validation, authorization, and secret exposure risks.
4. Recommend controls that meaningfully reduce risk.
5. Summarize the highest-priority security concerns.
