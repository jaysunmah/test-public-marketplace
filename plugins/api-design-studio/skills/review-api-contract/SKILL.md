---
name: review-api-contract
description: Review API contracts for consistency, compatibility, and implementation readiness. Use for OpenAPI, JSON schema, or internal API docs.
version: 1.0.0
---

# Review API Contract

Review proposed contracts before implementation begins.

## When to Use

- The user shares an API spec or endpoint proposal
- Backend and frontend teams need a compatibility review
- Schema churn or naming drift is creating confusion

## Instructions

1. Check naming consistency across resources and payloads.
2. Verify status codes and error shapes are predictable.
3. Flag ambiguous field semantics or missing validation details.
4. Note backward compatibility concerns for existing consumers.
5. Summarize the minimum contract changes needed for implementation.
