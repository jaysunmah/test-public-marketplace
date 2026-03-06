---
description: Review the current PR for bugs, security issues, and code quality
argument-hint: [pr-number]
allowed-tools: [Read, Glob, Grep, Shell]
---

Review the current pull request for:

1. **Bugs**: Logic errors, edge cases, null references
2. **Security**: Injection vulnerabilities, auth issues, data exposure
3. **Code Quality**: Naming, structure, DRY violations, complexity

If a PR number is provided, review that specific PR. Otherwise, review the current branch's diff against main.
