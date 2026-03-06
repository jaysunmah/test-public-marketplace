---
name: test-2-skill
description: Provides a lightweight workflow for creating and validating new plugin files in this repository. Use when the user asks to scaffold plugin content, add commands or skills, or verify plugin manifest consistency.
version: 1.0.0
---

# Test 2 Skill

This skill helps create small, valid plugin updates that match the repository's existing plugin structure.

## When to Use

Use this skill when:
- The user asks to add files under `plugins/test-2`
- The user asks to create or update a `SKILL.md` file
- The user needs a quick validation checklist for plugin JSON files

## Instructions

1. Confirm the target plugin path and required file names.
2. Follow existing patterns from neighboring plugin manifests before creating new files.
3. Create minimal, valid files first, then extend only if requested.
4. Validate JSON files after edits and report what changed.

## Quick Validation Checklist

- `plugin.json` has `name`, `description`, and `author`.
- `SKILL.md` contains YAML frontmatter with `name` and `description`.
- New files are placed under the expected plugin directory.
