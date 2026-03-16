---
name: review-async-interactions
description: Review async interaction design for race conditions and UX gaps. Use when frontend behavior depends on network timing.
version: 1.0.0
---

# Review Async Interactions

Check async UI behavior before it becomes flaky or confusing.

## When to Use

- User actions trigger optimistic or background updates
- Loading and stale-data behavior feels unclear
- Network timing could create awkward UX states

## Instructions

1. Identify request, cancel, retry, and refresh paths.
2. Look for race conditions and stale-data assumptions.
3. Check how errors and retries are communicated to users.
4. Recommend clearer ownership between local and remote state.
5. Summarize the most important interaction risks.
