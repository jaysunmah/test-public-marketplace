---
name: review-secret-handling
description: Review how secrets, tokens, or credentials are handled. Use when integrating external services or changing deployment configuration.
version: 1.0.0
---

# Review Secret Handling

Audit secret usage and exposure risk.

## When to Use

- API keys or credentials are being introduced
- Configuration or CI changes may expose secrets
- A service integration needs safer secret storage guidance

## Instructions

1. Identify where secrets are created, stored, rotated, and consumed.
2. Flag hardcoding, logging, or client exposure risks.
3. Recommend least-privilege scopes and rotation practices.
4. Review fallback and local-development handling.
5. Summarize the most important control gaps.
