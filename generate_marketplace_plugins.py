from __future__ import annotations

import json
from pathlib import Path


ROOT = Path("/Users/jma/projects/test-public-marketplace")
PLUGINS_ROOT = ROOT / "plugins"
MARKETPLACE_PATH = ROOT / ".claude-plugin" / "marketplace.json"
AUTHOR = {"name": "Test Author", "email": "test@example.com"}
BASE_HOMEPAGE = "https://github.com/jaysunmah/test-marketplace/tree/main/plugins/{name}"


PLUGINS = [
    {
        "name": "api-design-studio",
        "description": "API design and contract review workflows for REST and event-driven services",
        "category": "development",
        "skills": [
            {
                "name": "design-rest-endpoint",
                "description": "Design REST endpoints and request or response schemas. Use when adding or revising API surfaces.",
                "body": """# Design REST Endpoint

Use this skill to draft clean HTTP APIs and keep contracts consistent.

## When to Use

- The user wants to add a new REST endpoint
- An existing endpoint needs better naming, status codes, or schema shape
- API design needs a lightweight review before implementation

## Instructions

1. Identify the resource, caller, and primary workflow.
2. Recommend resource-oriented paths and consistent verbs.
3. Define request and response fields with explicit required and optional behavior.
4. Cover validation, pagination, filtering, and error cases when relevant.
5. Call out compatibility risks before suggesting breaking changes.
""",
            },
            {
                "name": "review-api-contract",
                "description": "Review API contracts for consistency, compatibility, and implementation readiness. Use for OpenAPI, JSON schema, or internal API docs.",
                "body": """# Review API Contract

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
""",
            },
        ],
        "rules": [
            {
                "filename": "rest-contracts.mdc",
                "description": "Use consistent REST contract conventions for API design tasks",
                "alwaysApply": True,
                "globs": None,
                "body": """- Prefer plural resource paths such as `/users` and `/orders`.
- Use stable identifiers in URLs and keep mutable display fields in the body.
- Document success and error payloads together so clients can implement against the full contract.
- Avoid introducing breaking response shape changes without noting a migration path.
""",
            },
            {
                "filename": "schema-evolution.mdc",
                "description": "Apply when reviewing API schema changes and versioning",
                "alwaysApply": False,
                "globs": ["**/*.json", "**/*.yaml", "**/*.yml", "**/*.md"],
                "body": """- Prefer additive schema changes over destructive ones.
- Mark deprecated fields explicitly and explain the replacement.
- Keep enum growth in mind when recommending client-side branching.
- Note whether a change affects persistence, caching, or downstream integrations.
""",
            },
        ],
        "agents": [
            {
                "name": "contract-reviewer",
                "description": "API contract reviewer. Use when endpoint definitions or schemas need a focused review.",
                "body": """You are an API contract specialist.

When invoked:
1. Identify the resource model and intended consumers
2. Review naming, status codes, and payload consistency
3. Check compatibility and migration concerns
4. Flag ambiguous or underspecified behavior
5. Return a concise set of recommended contract changes
""",
            },
            {
                "name": "event-schema-advisor",
                "description": "Event schema specialist. Use when proposing webhooks, queues, or pub-sub payloads.",
                "body": """You review event-driven interfaces for clarity and durability.

When invoked:
1. Check event names and trigger semantics
2. Verify payload fields are stable and versionable
3. Highlight idempotency and ordering assumptions
4. Recommend metadata needed for observability and replay
5. Summarize producer and consumer risks
""",
            },
        ],
        "commands": [
            {
                "filename": "draft-api.md",
                "description": "Draft a new API contract from requirements",
                "argument_hint": "<resource-name>",
                "body": """Design a draft API contract for the requested resource.

1. Clarify the primary workflow and caller.
2. Propose REST endpoints or event interfaces as appropriate.
3. Define request and response shapes.
4. Include validation notes, auth considerations, and error handling.
5. End with open questions that the team should answer before implementation.
""",
            }
        ],
    },
    {
        "name": "incident-response-kit",
        "description": "Incident triage, postmortem writing, and operational recovery guidance for engineering teams",
        "category": "operations",
        "skills": [
            {
                "name": "triage-production-incident",
                "description": "Triage production incidents and structure the immediate response. Use when the user describes an outage, regression, or customer-facing failure.",
                "body": """# Triage Production Incident

Guide a fast, structured incident response.

## When to Use

- A system is down or degraded
- Error rates, latency, or data quality changed unexpectedly
- The user needs a calm triage checklist

## Instructions

1. Establish current impact, affected users, and severity.
2. Separate symptom collection from root cause guesses.
3. Suggest the safest mitigation or rollback first.
4. Capture timeline checkpoints as you learn more.
5. End with a clear status update and next investigative step.
""",
            },
            {
                "name": "write-postmortem",
                "description": "Write a blameless postmortem after an incident. Use when the team needs a timeline, impact summary, and follow-up actions.",
                "body": """# Write Postmortem

Turn incident notes into a blameless review.

## When to Use

- Recovery is complete and follow-up documentation is needed
- The team wants a structured retrospective
- Multiple contributing factors need to be summarized clearly

## Instructions

1. Summarize impact in plain language.
2. Build a timeline from detection through recovery.
3. Distinguish root causes from contributing factors.
4. Capture what helped and what slowed recovery.
5. Convert lessons into concrete follow-up actions with owners.
""",
            },
        ],
        "rules": [
            {
                "filename": "blameless-language.mdc",
                "description": "Keep incident analysis blameless and action-oriented",
                "alwaysApply": True,
                "globs": None,
                "body": """- Describe actions and system behavior rather than assigning fault to individuals.
- Prefer evidence-backed statements over speculation.
- Separate mitigation steps from long-term prevention work.
- End incident summaries with the current status and next checkpoint.
""",
            },
            {
                "filename": "timeline-format.mdc",
                "description": "Apply when drafting incident timelines or recovery notes",
                "alwaysApply": False,
                "globs": ["**/*.md"],
                "body": """- Record timestamps in a single timezone per document.
- Keep each timeline entry short and evidence-based.
- Note when a hypothesis was formed versus when it was confirmed.
- Include both customer impact and operator actions.
""",
            },
        ],
        "agents": [
            {
                "name": "incident-commander",
                "description": "Incident lead facilitator. Use when coordinating triage and comms during an outage.",
                "body": """You are acting as an incident commander.

When invoked:
1. Determine severity and affected user groups
2. Keep the response focused on mitigation and facts
3. Recommend clear status updates for stakeholders
4. Track open questions and owners
5. Escalate follow-up work after recovery
""",
            },
            {
                "name": "postmortem-editor",
                "description": "Postmortem writing specialist. Use when rough incident notes need to become a publishable review.",
                "body": """You turn fragmented incident notes into a clean postmortem.

When invoked:
1. Build a coherent timeline
2. Remove blame-oriented language
3. Clarify root cause and contributing factors
4. Group action items by prevention, detection, and recovery
5. Produce a concise executive summary
""",
            },
        ],
        "commands": [
            {
                "filename": "incident-brief.md",
                "description": "Create a concise incident status brief",
                "argument_hint": "[service-name]",
                "body": """Create a status brief for the incident.

1. Summarize impact and current severity.
2. State what is known, unknown, and being investigated.
3. Recommend the next update window.
4. Keep the tone factual and calm.
""",
            }
        ],
    },
    {
        "name": "data-pipeline-workbench",
        "description": "Workflow helpers for batch jobs, ETL design, and data quality checks",
        "category": "data",
        "skills": [
            {
                "name": "design-batch-job",
                "description": "Design a batch processing job with clear inputs, outputs, and retry behavior. Use when planning ETL or scheduled processing.",
                "body": """# Design Batch Job

Design dependable scheduled data workflows.

## When to Use

- A new ETL or backfill is needed
- The user needs a plan for retries, checkpoints, or partitioning
- A pipeline is growing beyond an ad hoc script

## Instructions

1. Define source systems, transforms, and outputs.
2. Clarify batch boundaries, partitioning, and idempotency.
3. Recommend failure handling and retry rules.
4. Note monitoring signals and data quality checks.
5. Call out operational costs such as reprocessing and late data.
""",
            },
            {
                "name": "audit-data-quality",
                "description": "Audit data quality risks and suggest validation checks. Use when metrics drift, backfills fail, or tables seem unreliable.",
                "body": """# Audit Data Quality

Review the trustworthiness of a data pipeline.

## When to Use

- Table counts or dashboard metrics changed unexpectedly
- A backfill produced suspicious results
- The team wants stronger validation around a dataset

## Instructions

1. Identify critical fields, joins, and derived metrics.
2. Suggest freshness, null, uniqueness, and range checks.
3. Highlight lineage gaps and silent failure modes.
4. Recommend alert thresholds that avoid noise.
5. Summarize the top integrity risks.
""",
            },
        ],
        "rules": [
            {
                "filename": "pipeline-safety.mdc",
                "description": "Use resilient design patterns for batch and ETL workflows",
                "alwaysApply": True,
                "globs": None,
                "body": """- Prefer idempotent writes and checkpointed progress where feasible.
- Make late-arriving data behavior explicit.
- Document how retries interact with duplicate creation or partial outputs.
- Include data quality checks close to the transform that can fail.
""",
            },
            {
                "filename": "sql-review.mdc",
                "description": "Apply when reviewing SQL transformations or warehouse models",
                "alwaysApply": False,
                "globs": ["**/*.sql", "**/*.py", "**/*.md"],
                "body": """- Name intermediate datasets for intent, not implementation detail.
- Be explicit about join cardinality assumptions.
- Note whether a query is safe for incremental re-runs.
- Prefer readable transformations over dense one-shot SQL when maintainability matters.
""",
            },
        ],
        "agents": [
            {
                "name": "pipeline-reviewer",
                "description": "Batch pipeline reviewer. Use for ETL design and scheduled job reliability reviews.",
                "body": """You evaluate data pipelines for operational safety.

When invoked:
1. Map the pipeline stages and ownership boundaries
2. Review idempotency, retries, and recovery options
3. Check observability and data quality coverage
4. Flag scaling or cost concerns
5. Return the highest-value improvements first
""",
            },
            {
                "name": "warehouse-model-auditor",
                "description": "Warehouse modeling specialist. Use when tables, marts, or transformations need a maintainability review.",
                "body": """You review analytical data models for clarity and correctness.

When invoked:
1. Check naming and layering conventions
2. Review derivation logic and metric semantics
3. Highlight lineage or freshness blind spots
4. Recommend validation queries or tests
5. Summarize downstream consumer risks
""",
            },
        ],
        "commands": [
            {
                "filename": "plan-backfill.md",
                "description": "Plan a safe data backfill",
                "argument_hint": "<dataset-name>",
                "body": """Plan a safe backfill for the requested dataset.

1. Define the date range and source of truth.
2. Describe safeguards against duplicates and partial writes.
3. Include validation steps before and after execution.
4. Call out rollback or retry strategy.
""",
            }
        ],
    },
    {
        "name": "design-qa-assistant",
        "description": "Design handoff, UI acceptance review, and visual QA helpers for product teams",
        "category": "design",
        "skills": [
            {
                "name": "run-visual-qa",
                "description": "Run a visual QA pass against a UI change. Use when comparing implementation quality against a design spec or intended UX.",
                "body": """# Run Visual QA

Review whether a UI implementation is ready to ship.

## When to Use

- A new screen or component needs design QA
- The user reports spacing, alignment, or state mismatches
- A design handoff needs a concise implementation checklist

## Instructions

1. Identify the primary layout, states, and responsive breakpoints.
2. Check spacing, hierarchy, copy, and interaction affordances.
3. Look for missing hover, loading, empty, and error states.
4. Prioritize issues by user impact and polish.
5. Provide a tight acceptance checklist at the end.
""",
            },
            {
                "name": "translate-design-handoff",
                "description": "Translate product or design notes into implementation-ready guidance. Use when a UI concept needs concrete engineering tasks.",
                "body": """# Translate Design Handoff

Turn design intent into a practical build plan.

## When to Use

- A designer shared notes, screenshots, or component requirements
- Engineering needs a breakdown of states and interactions
- The team wants a simpler build checklist from a dense handoff

## Instructions

1. Extract components, states, and interaction patterns.
2. Distinguish layout constraints from visual polish details.
3. Note reusable primitives versus one-off work.
4. Call out missing behavior specs or accessibility details.
5. Organize the result as an engineering-oriented implementation plan.
""",
            },
        ],
        "rules": [
            {
                "filename": "ui-acceptance.mdc",
                "description": "Use consistent UI acceptance criteria when reviewing product surfaces",
                "alwaysApply": True,
                "globs": None,
                "body": """- Check default, loading, empty, success, and error states for user-facing flows.
- Keep acceptance feedback concrete and tied to visible behavior.
- Prioritize accessibility and clarity before pixel-perfect polish.
- When design intent is unclear, identify the missing decision explicitly.
""",
            },
            {
                "filename": "copy-and-labels.mdc",
                "description": "Apply when reviewing product copy and interface labels",
                "alwaysApply": False,
                "globs": ["**/*.md", "**/*.tsx", "**/*.jsx", "**/*.html"],
                "body": """- Prefer action-oriented labels over internal jargon.
- Keep helper text short and specific.
- Ensure destructive actions are clearly labeled.
- Match placeholder text to the input's expected format.
""",
            },
        ],
        "agents": [
            {
                "name": "ui-qa-reviewer",
                "description": "UI QA specialist. Use when validating layouts, states, and polish before release.",
                "body": """You review UI changes for acceptance quality.

When invoked:
1. Identify the intended user flow
2. Check layout, states, and interaction clarity
3. Highlight accessibility or content issues
4. Separate must-fix problems from nice-to-have polish
5. Return a concise ship-readiness summary
""",
            },
            {
                "name": "design-handoff-editor",
                "description": "Design handoff editor. Use when rough design notes need to become an engineering checklist.",
                "body": """You convert design intent into a crisp implementation brief.

When invoked:
1. Extract components and states
2. Clarify responsive and accessibility requirements
3. Identify reusable primitives
4. Note open questions or missing specs
5. Produce a prioritized build checklist
""",
            },
        ],
        "commands": [
            {
                "filename": "qa-screen.md",
                "description": "Review a screen implementation against expected UX",
                "argument_hint": "<screen-name>",
                "body": """Perform a UI QA review for the named screen.

1. Summarize the user goal for the screen.
2. Review layout, content hierarchy, and critical states.
3. Flag must-fix issues first, then polish items.
4. End with a short acceptance recommendation.
""",
            }
        ],
    },
    {
        "name": "docs-ops-studio",
        "description": "Documentation maintenance helpers for changelogs, runbooks, and internal technical guides",
        "category": "documentation",
        "skills": [
            {
                "name": "refresh-runbook",
                "description": "Refresh or expand an operational runbook. Use when a procedure is stale, fragmented, or hard to follow.",
                "body": """# Refresh Runbook

Improve operational documentation without losing concrete steps.

## When to Use

- A runbook is outdated or incomplete
- Incident learnings need to be folded into docs
- A procedure needs clearer prerequisites or rollback steps

## Instructions

1. Identify the audience, trigger, and success condition.
2. Reorganize the runbook around prerequisites, execution, validation, and rollback.
3. Convert vague steps into concrete operator actions.
4. Flag missing screenshots, commands, or owners.
5. End with a short maintenance checklist.
""",
            },
            {
                "name": "draft-release-notes",
                "description": "Draft release notes from a set of changes. Use when summarizing a release for internal or external audiences.",
                "body": """# Draft Release Notes

Summarize product or engineering changes in a readable format.

## When to Use

- A release branch or milestone needs notes
- The team wants an internal launch summary
- Changelog entries need to be grouped by audience impact

## Instructions

1. Group changes by user-facing theme rather than commit history.
2. Highlight behavior changes, fixes, and known follow-ups.
3. Keep the tone factual and concise.
4. Separate internal implementation detail from user impact.
5. Call out anything that still needs validation before release.
""",
            },
        ],
        "rules": [
            {
                "filename": "docs-clarity.mdc",
                "description": "Keep technical documentation concise, structured, and action-oriented",
                "alwaysApply": True,
                "globs": None,
                "body": """- Lead with purpose and intended audience.
- Prefer stepwise procedures over dense paragraphs for operational tasks.
- Explain why a step matters when the consequence is non-obvious.
- Surface prerequisites and rollback paths early.
""",
            },
            {
                "filename": "changelog-style.mdc",
                "description": "Apply when writing release notes or changelog entries",
                "alwaysApply": False,
                "globs": ["**/*.md"],
                "body": """- Describe user-visible outcomes before implementation details.
- Group related changes together to reduce noise.
- Avoid commit-by-commit narration.
- Note known limitations or staged rollouts when relevant.
""",
            },
        ],
        "agents": [
            {
                "name": "runbook-editor",
                "description": "Runbook editing specialist. Use when procedures need clearer operator guidance.",
                "body": """You edit operational documentation for clarity and usability.

When invoked:
1. Identify audience and operational trigger
2. Reorder content around actionability
3. Check for missing prerequisites, validation, and rollback steps
4. Remove ambiguity and stale phrasing
5. Return a concise revised structure
""",
            },
            {
                "name": "release-notes-writer",
                "description": "Release notes specialist. Use when a set of changes needs a polished summary.",
                "body": """You write release notes that balance accuracy with readability.

When invoked:
1. Group changes by user or team impact
2. Distinguish fixes, improvements, and known follow-ups
3. Remove low-signal implementation noise
4. Keep tone concise and factual
5. Produce a ship-ready summary
""",
            },
        ],
        "commands": [
            {
                "filename": "update-runbook.md",
                "description": "Rewrite a runbook into a clearer operator guide",
                "argument_hint": "<doc-topic>",
                "body": """Rewrite or improve the runbook for the requested topic.

1. Identify the runbook's operator and trigger.
2. Reorganize into prerequisites, steps, validation, and rollback.
3. Flag missing ownership or escalation details.
4. End with unresolved documentation gaps.
""",
            }
        ],
    },
    {
        "name": "migration-planner",
        "description": "Planning helpers for framework upgrades, service migrations, and phased rollouts",
        "category": "development",
        "skills": [
            {
                "name": "plan-service-migration",
                "description": "Plan a staged service migration. Use when moving systems, APIs, or storage without a full cutover at once.",
                "body": """# Plan Service Migration

Create a migration path that reduces risk.

## When to Use

- A service, datastore, or API needs to be replaced
- The team wants phases instead of a big-bang migration
- Rollout, rollback, and compatibility details are unclear

## Instructions

1. Define source and target systems plus migration constraints.
2. Break the work into phases with measurable checkpoints.
3. Cover dual-write, read shadowing, or compatibility periods when relevant.
4. Make rollback points explicit.
5. End with key unknowns that need validation.
""",
            },
            {
                "name": "audit-upgrade-risk",
                "description": "Audit risks for framework or dependency upgrades. Use when planning a major version bump or infrastructure change.",
                "body": """# Audit Upgrade Risk

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
""",
            },
        ],
        "rules": [
            {
                "filename": "phased-rollouts.mdc",
                "description": "Use phased rollout planning for risky migrations or upgrades",
                "alwaysApply": True,
                "globs": None,
                "body": """- Prefer staged rollouts with measurable checkpoints over big-bang cutovers.
- Identify rollback points before recommending irreversible steps.
- Keep compatibility periods explicit when two systems coexist.
- Define success criteria for each migration phase.
""",
            },
            {
                "filename": "upgrade-checklist.mdc",
                "description": "Apply when reviewing dependency or framework upgrades",
                "alwaysApply": False,
                "globs": ["**/package.json", "**/pyproject.toml", "**/go.mod", "**/*.md"],
                "body": """- Distinguish build-time issues from runtime and operational regressions.
- Verify test coverage around changed integration boundaries.
- Note any schema, config, or environment changes required.
- Prefer narrow, observable rollout slices where possible.
""",
            },
        ],
        "agents": [
            {
                "name": "migration-architect",
                "description": "Migration planning specialist. Use when replacing systems or phasing rollouts.",
                "body": """You design safe migration strategies.

When invoked:
1. Identify constraints and compatibility requirements
2. Break the migration into phases
3. Define validation and rollback points
4. Highlight operational and coordination risks
5. Return a practical staged plan
""",
            },
            {
                "name": "upgrade-investigator",
                "description": "Upgrade risk specialist. Use when planning major version bumps or platform changes.",
                "body": """You assess upgrade risk before execution.

When invoked:
1. Map impacted packages or services
2. Identify likely breakpoints
3. Recommend test and rollout strategies
4. Call out required code or config changes
5. Summarize the minimum safe path forward
""",
            },
        ],
        "commands": [
            {
                "filename": "migration-plan.md",
                "description": "Create a phased migration plan",
                "argument_hint": "<system-name>",
                "body": """Create a phased migration plan for the named system.

1. Define current and target state.
2. Break the work into rollout phases.
3. Include validation and rollback criteria for each phase.
4. End with the highest-risk assumptions.
""",
            }
        ],
    },
    {
        "name": "observability-auditor",
        "description": "Monitoring, alert review, and telemetry coverage guidance for production services",
        "category": "operations",
        "skills": [
            {
                "name": "audit-alerting",
                "description": "Audit alert quality and signal coverage. Use when teams have noisy pages, blind spots, or unclear severity thresholds.",
                "body": """# Audit Alerting

Improve alert quality without creating extra noise.

## When to Use

- Alerts are too noisy or not actionable
- A recent incident revealed missing telemetry
- The team wants better severity and routing guidelines

## Instructions

1. Identify the most important user-impacting signals.
2. Distinguish page-worthy conditions from dashboard-only indicators.
3. Recommend threshold, duration, and ownership improvements.
4. Note missing runbook links or investigative context.
5. Summarize the biggest telemetry gaps.
""",
            },
            {
                "name": "design-sli-slo",
                "description": "Design service-level indicators and objectives. Use when a team needs better reliability targets and measurement.",
                "body": """# Design SLI SLO

Create practical reliability targets tied to user experience.

## When to Use

- A service lacks explicit reliability goals
- The team wants to define error budget policy
- Existing dashboards do not map clearly to customer impact

## Instructions

1. Define the user journey or operation to measure.
2. Recommend meaningful availability, latency, or correctness indicators.
3. Suggest realistic objectives and measurement windows.
4. Explain what consumes error budget.
5. Note instrumentation that must exist before targets are enforced.
""",
            },
        ],
        "rules": [
            {
                "filename": "alert-actionability.mdc",
                "description": "Keep alerts actionable and tied to clear owners",
                "alwaysApply": True,
                "globs": None,
                "body": """- Alerts should describe user impact or service health degradation, not raw system trivia alone.
- Prefer alerts with clear owners, dashboards, and runbook links.
- Keep severity thresholds explicit and defensible.
- Avoid paging on symptoms that are better handled by trend monitoring.
""",
            },
            {
                "filename": "telemetry-gaps.mdc",
                "description": "Apply when reviewing monitoring or observability coverage",
                "alwaysApply": False,
                "globs": ["**/*.md", "**/*.yaml", "**/*.yml", "**/*.json"],
                "body": """- Tie telemetry to critical user journeys or system invariants.
- Note where logs, metrics, and traces should complement one another.
- Prefer a few high-signal indicators over many weak ones.
- Highlight missing labels or dimensions that block useful debugging.
""",
            },
        ],
        "agents": [
            {
                "name": "alert-reviewer",
                "description": "Alerting specialist. Use when paging rules or monitors need a quality review.",
                "body": """You review operational alerts for usefulness and signal quality.

When invoked:
1. Identify the service goal being protected
2. Review thresholds, severity, and owner clarity
3. Flag noisy or low-actionability alerts
4. Suggest missing dashboards or runbooks
5. Return the top alerting fixes first
""",
            },
            {
                "name": "slo-coach",
                "description": "SLO design specialist. Use when teams need practical reliability targets.",
                "body": """You help teams define meaningful service objectives.

When invoked:
1. Clarify the user-facing operation
2. Recommend SLIs and measurement windows
3. Check instrumentation prerequisites
4. Explain error budget tradeoffs
5. Produce a concise target proposal
""",
            },
        ],
        "commands": [
            {
                "filename": "review-alerts.md",
                "description": "Review alerting for a service",
                "argument_hint": "<service-name>",
                "body": """Review the alerting posture for the requested service.

1. Identify user-impacting failure modes.
2. Recommend which signals should page versus trend.
3. Flag missing owners, dashboards, or runbook context.
4. End with the top three alerting improvements.
""",
            }
        ],
    },
    {
        "name": "release-train-manager",
        "description": "Release readiness, rollout coordination, and launch checklist helpers for product engineering",
        "category": "productivity",
        "skills": [
            {
                "name": "prepare-release-checklist",
                "description": "Prepare a release readiness checklist. Use when coordinating launches across engineering, QA, and operations.",
                "body": """# Prepare Release Checklist

Build a practical release checklist for a coordinated launch.

## When to Use

- Multiple teams need a shared release checklist
- Launch readiness is spread across several docs or chats
- The user wants a concise go or no-go framework

## Instructions

1. List the required validation gates before launch.
2. Separate pre-release, launch-window, and post-release steps.
3. Capture owners and dependencies where known.
4. Highlight rollback triggers and comms expectations.
5. End with unresolved risks.
""",
            },
            {
                "name": "assess-rollout-risk",
                "description": "Assess rollout risk and propose guardrails. Use when launching a risky feature, migration, or infrastructure change.",
                "body": """# Assess Rollout Risk

Estimate rollout risk and tighten the safety plan.

## When to Use

- A launch affects critical user flows
- The feature is behind a flag or staged rollout
- Teams need more confidence before shipping

## Instructions

1. Identify the main failure modes and blast radius.
2. Recommend canaries, flags, or staged exposure when appropriate.
3. Clarify what metrics define a healthy rollout.
4. Define who watches the launch and for how long.
5. Summarize the minimum safe launch plan.
""",
            },
        ],
        "rules": [
            {
                "filename": "release-readiness.mdc",
                "description": "Use explicit release gates and rollback criteria for launches",
                "alwaysApply": True,
                "globs": None,
                "body": """- State the go or no-go decision criteria up front.
- Keep rollback triggers observable and specific.
- Separate required launch checks from optional polish work.
- Assign ownership for launch-window monitoring and communications.
""",
            },
            {
                "filename": "staged-rollout-language.mdc",
                "description": "Apply when documenting feature flags or staged release plans",
                "alwaysApply": False,
                "globs": ["**/*.md", "**/*.json", "**/*.yaml", "**/*.yml"],
                "body": """- Describe each rollout stage and its target audience clearly.
- Tie rollout advancement to specific health checks.
- Note whether the change is reversible at each stage.
- Keep stakeholder communication expectations explicit.
""",
            },
        ],
        "agents": [
            {
                "name": "release-coordinator",
                "description": "Release coordination specialist. Use when organizing launch checklists and cross-team readiness.",
                "body": """You coordinate release readiness.

When invoked:
1. Identify launch scope and dependencies
2. Build a clear readiness checklist
3. Highlight missing owners or blockers
4. Define monitoring and rollback expectations
5. Return a concise launch recommendation
""",
            },
            {
                "name": "rollout-risk-reviewer",
                "description": "Rollout risk reviewer. Use when a launch needs better guardrails or staged exposure.",
                "body": """You review rollout plans for operational safety.

When invoked:
1. Identify blast radius and failure modes
2. Recommend canaries, flags, or staged ramps
3. Define health metrics and stop conditions
4. Note comms and staffing requirements
5. Summarize the safest rollout path
""",
            },
        ],
        "commands": [
            {
                "filename": "launch-checklist.md",
                "description": "Generate a launch checklist for a release",
                "argument_hint": "<release-name>",
                "body": """Generate a launch checklist for the named release.

1. Separate preflight, launch-window, and follow-up tasks.
2. Include validation, monitoring, and rollback criteria.
3. Call out blockers or missing owners.
4. End with a go or no-go recommendation framework.
""",
            }
        ],
    },
    {
        "name": "security-playbook",
        "description": "Security review helpers for auth changes, secrets handling, and threat-oriented design discussions",
        "category": "security",
        "skills": [
            {
                "name": "threat-model-feature",
                "description": "Threat-model a feature or workflow. Use when adding auth, payments, admin access, or sensitive data handling.",
                "body": """# Threat Model Feature

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
""",
            },
            {
                "name": "review-secret-handling",
                "description": "Review how secrets, tokens, or credentials are handled. Use when integrating external services or changing deployment configuration.",
                "body": """# Review Secret Handling

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
""",
            },
        ],
        "rules": [
            {
                "filename": "security-baseline.mdc",
                "description": "Apply a practical security baseline when reviewing sensitive features",
                "alwaysApply": True,
                "globs": None,
                "body": """- Treat auth, payments, admin actions, and secret handling as security-sensitive by default.
- Prefer least privilege and explicit authorization checks.
- Avoid suggesting patterns that expose secrets to clients or logs.
- Call out validation, auditability, and abuse-case gaps clearly.
""",
            },
            {
                "filename": "input-and-output-review.mdc",
                "description": "Apply when reviewing data flow across trust boundaries",
                "alwaysApply": False,
                "globs": ["**/*.ts", "**/*.tsx", "**/*.js", "**/*.py", "**/*.md"],
                "body": """- Check untrusted inputs at entry points and dangerous outputs at sinks.
- Prefer safe APIs and parameterization over string interpolation.
- Note where escaping, sanitization, or content validation is required.
- Highlight secrets, tokens, and personally sensitive fields explicitly.
""",
            },
        ],
        "agents": [
            {
                "name": "security-reviewer",
                "description": "Security-focused reviewer. Use when implementing auth, secrets, payments, or sensitive workflows.",
                "body": """You are a security reviewer focused on practical risk reduction.

When invoked:
1. Identify security-sensitive code paths or design areas
2. Check for injection, auth, exposure, and secret handling risks
3. Review trust boundaries and validation assumptions
4. Recommend concrete mitigations
5. Report findings by severity
""",
            },
            {
                "name": "threat-modeler",
                "description": "Threat modeling specialist. Use when a new feature changes trust boundaries or introduces privileged actions.",
                "body": """You build lightweight threat models for engineering decisions.

When invoked:
1. Map actors, assets, and entry points
2. Identify abuse cases and likely attacker goals
3. Review existing controls and gaps
4. Prioritize mitigations by impact and feasibility
5. Summarize residual risk
""",
            },
        ],
        "commands": [
            {
                "filename": "security-review.md",
                "description": "Run a lightweight security review",
                "argument_hint": "[feature-name]",
                "body": """Perform a lightweight security review for the named feature.

1. Identify trust boundaries and sensitive assets.
2. Flag likely abuse cases or implementation risks.
3. Suggest practical mitigations.
4. End with the highest-severity concerns first.
""",
            }
        ],
    },
    {
        "name": "test-automation-lab",
        "description": "Test planning and failure-analysis helpers for unit, integration, and end-to-end coverage",
        "category": "quality",
        "skills": [
            {
                "name": "plan-test-matrix",
                "description": "Plan a focused test matrix. Use when adding features, fixing regressions, or deciding what coverage matters most.",
                "body": """# Plan Test Matrix

Design the smallest useful set of tests that protects the change.

## When to Use

- A feature or bug fix needs a test strategy
- Existing coverage feels broad but not confidence-building
- The team wants to avoid redundant test cases

## Instructions

1. Identify the highest-risk behaviors and boundaries.
2. Separate unit, integration, and end-to-end needs.
3. Prefer a few high-signal scenarios over exhaustive combinatorics.
4. Call out setup cost and test flakiness risks.
5. End with the recommended minimum coverage set.
""",
            },
            {
                "name": "analyze-test-failure",
                "description": "Analyze failing tests and suggest the likeliest root causes. Use when failures are noisy, flaky, or hard to interpret.",
                "body": """# Analyze Test Failure

Turn noisy failure output into a debugging path.

## When to Use

- A test suite failed and the signal is unclear
- Flaky behavior is slowing down delivery
- A regression needs a targeted diagnosis

## Instructions

1. Distinguish deterministic failures from flaky or environmental ones.
2. Narrow the likely layer: setup, application logic, integration, or test itself.
3. Suggest the smallest next step to confirm the root cause.
4. Recommend whether the fix belongs in product code or the test harness.
5. Summarize the most likely diagnosis.
""",
            },
        ],
        "rules": [
            {
                "filename": "test-signal.mdc",
                "description": "Favor high-signal, maintainable tests over redundant coverage",
                "alwaysApply": True,
                "globs": None,
                "body": """- Prefer tests that protect user-visible behavior or critical invariants.
- Avoid adding broad, repetitive cases that only restate implementation detail.
- Note flakiness and setup cost when recommending coverage.
- Keep verification aligned with the change's actual risk.
""",
            },
            {
                "filename": "failure-analysis.mdc",
                "description": "Apply when interpreting failing test output or proposing follow-up tests",
                "alwaysApply": False,
                "globs": ["**/*.test.*", "**/*.spec.*", "**/*.md"],
                "body": """- Separate probable root cause from secondary failures.
- Call out environmental or ordering assumptions that make tests flaky.
- Prefer minimal reproductions for confusing regressions.
- Suggest additional tests only when they materially reduce risk.
""",
            },
        ],
        "agents": [
            {
                "name": "test-strategist",
                "description": "Test strategy specialist. Use when deciding what automated coverage a change actually needs.",
                "body": """You design pragmatic, high-signal test strategies.

When invoked:
1. Identify the main risks introduced by the change
2. Recommend the smallest meaningful set of tests
3. Balance unit, integration, and end-to-end coverage
4. Call out flakiness or setup complexity
5. Return a prioritized test plan
""",
            },
            {
                "name": "failure-triager",
                "description": "Test failure triager. Use when failing suites need root-cause analysis.",
                "body": """You investigate test failures methodically.

When invoked:
1. Separate primary and secondary failures
2. Identify likely product-code versus test-harness issues
3. Suggest the next confirming experiment
4. Note flakiness or environment factors
5. Summarize the likeliest root cause
""",
            },
        ],
        "commands": [
            {
                "filename": "test-plan.md",
                "description": "Create a lean test plan for a change",
                "argument_hint": "<change-name>",
                "body": """Create a lean test plan for the requested change.

1. Identify the main risk areas.
2. Recommend the minimum useful automated coverage.
3. Note any manual checks that still matter.
4. End with likely flakiness or maintenance concerns.
""",
            }
        ],
    },
]


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n")


def make_readme(plugin: dict) -> str:
    return "\n".join(
        [
            f"# {plugin['name'].replace('-', ' ').title()}",
            "",
            f"{plugin['description']}.",
            "",
            "## Included Components",
            "",
            f"- {len(plugin['skills'])} skills for recurring workflows",
            f"- {len(plugin['rules'])} rules for persistent guidance",
            f"- {len(plugin['agents'])} specialized agents for focused tasks",
            f"- {len(plugin['commands'])} slash command for quick entry points",
            "",
            "## Structure",
            "",
            "```",
            f"{plugin['name']}/",
            "├── .claude-plugin/",
            "│   └── plugin.json",
            "├── agents/",
            "├── commands/",
            "├── rules/",
            "├── skills/",
            "└── README.md",
            "```",
            "",
            "## Themes",
            "",
            f"This plugin is aimed at {plugin['category']} work and is intentionally packaged with multiple realistic, focused components rather than a single demo file.",
        ]
    )


def make_rule(rule: dict) -> str:
    lines = [
        "---",
        f"description: {rule['description']}",
        f"alwaysApply: {str(rule['alwaysApply']).lower()}",
    ]
    globs = rule.get("globs")
    if globs:
        lines.append("globs:")
        lines.extend([f"  - {glob}" for glob in globs])
    lines.extend(["---", "", rule["body"].rstrip()])
    return "\n".join(lines)


def main() -> None:
    for plugin in PLUGINS:
        plugin_root = PLUGINS_ROOT / plugin["name"]
        write_text(plugin_root / ".claude-plugin" / "plugin.json", json.dumps(
            {
                "name": plugin["name"],
                "description": plugin["description"],
                "version": "1.0.0",
                "author": AUTHOR,
                "keywords": [plugin["category"], "workflow", "assistant"],
            },
            indent=2,
        ))
        write_text(plugin_root / "README.md", make_readme(plugin))

        for skill in plugin["skills"]:
            write_text(
                plugin_root / "skills" / skill["name"] / "SKILL.md",
                "\n".join(
                    [
                        "---",
                        f"name: {skill['name']}",
                        f"description: {skill['description']}",
                        "version: 1.0.0",
                        "---",
                        "",
                        skill["body"].rstrip(),
                    ]
                ),
            )

        for rule in plugin["rules"]:
            write_text(plugin_root / "rules" / rule["filename"], make_rule(rule))

        for agent in plugin["agents"]:
            write_text(
                plugin_root / "agents" / f"{agent['name']}.md",
                "\n".join(
                    [
                        "---",
                        f"name: {agent['name']}",
                        f"description: {agent['description']}",
                        "---",
                        "",
                        agent["body"].rstrip(),
                    ]
                ),
            )

        for command in plugin["commands"]:
            write_text(
                plugin_root / "commands" / command["filename"],
                "\n".join(
                    [
                        "---",
                        f"description: {command['description']}",
                        f"argument-hint: {command['argument_hint']}",
                        "allowed-tools: [Read, Glob, Grep]",
                        "---",
                        "",
                        command["body"].rstrip(),
                    ]
                ),
            )

    marketplace = json.loads(MARKETPLACE_PATH.read_text())
    existing_names = {entry["name"] for entry in marketplace.get("plugins", [])}
    for plugin in PLUGINS:
        if plugin["name"] in existing_names:
            continue
        marketplace["plugins"].append(
            {
                "name": plugin["name"],
                "description": plugin["description"],
                "version": "1.0.0",
                "author": AUTHOR,
                "source": f"./plugins/{plugin['name']}",
                "category": plugin["category"],
                "homepage": BASE_HOMEPAGE.format(name=plugin["name"]),
            }
        )

    write_text(MARKETPLACE_PATH, json.dumps(marketplace, indent=2))
    print(f"Created {len(PLUGINS)} plugins and updated marketplace manifest.")


if __name__ == "__main__":
    main()
