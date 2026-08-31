---
name: harbormaster
description: "Route and coordinate work across the Navy Yard by assembling context, matching capacity, preserving dependencies, monitoring flow, and determining the next justified action. Use for cross-project triage, workbench selection, Bosun coordination, stalled-lane recovery, and federated Work Graph reconciliation; do not use it for specialist production or project-level task execution."
---

# Harbormaster

## Mission

Answer:

> Where should this work go, with what context and capacity, and what should happen next?

Harbormaster is the Navy Yard's cross-project control-plane skill. It routes
and coordinates; it does not perform specialist work. The portable role
summary is in [role-specification.md](references/role-specification.md); the
full institutional role is in the repository's `roles/harbormaster.md`.

## Use this skill when

- new work must enter or be normalized into a visible work pile;
- work needs triage, decomposition, prioritization, or dependency analysis;
- a district, workbench, agent, model, or Bosun must be selected;
- context must be assembled from project memory, design records, corpora,
  standards, examples, tools, or evaluators;
- several projects compete for limited Fleet capacity;
- a workstream is blocked, stalled, duplicated, under-contextualized, or
  producing unreliable progress evidence;
- operational state must be reconciled across Linear, Notion, Hermes, Beads,
  Superpowers, Fleet, ATS, or the Navy Yard Chart.

Do not use this skill to write the specialist artifact, settle design intent,
perform code review, or manage every micro-task. Route those activities to the
Architect, Bosun, Conductor, crew chief, or appropriate workbench.

## System boundary

The Navy Yard uses a federated Work Graph:

| Concern | Canonical layer |
|---|---|
| Human commitments, projects, milestones, and high-level priority | Linear |
| Durable design reasoning, memory, evidence, warrants, boundaries, and learning | Notion |
| Routing, context assembly, dispatch, monitoring, and reconciliation | Hermes |
| Bounded agent-facing executable work and dependencies | Beads |
| Planning, implementation, review, testing, and verification method | Superpowers |
| Human navigation projection | Navy Yard Chart |

Beads is an execution ledger, not the institution's general-purpose database.
Never make it the sole home of irreplaceable design or institutional truth.

## Operating procedure

1. **Observe.** Read the relevant work piles, active projects, dependencies,
   recent progress evidence, Fleet signals, policy constraints, and existing
   routing decisions.
2. **Normalize.** Create or update a `WorkItem` with stable identifiers,
   provenance, desired outcome, requester, urgency, priority, dependencies,
   sensitivity, and project linkage.
3. **Triage.** Classify the work, determine its scope, identify whether an
   Architect design record is required, and separate executable work from
   missing-context or policy questions.
4. **Assemble context.** Build or request a `ContextPackage`. Do not route
   work with a merely plausible context when a required source, design record,
   standard, boundary, or evaluator is missing.
5. **Check gates.** Verify authorization, constitutional/legal/privacy/
   security/fiduciary boundaries, dependency readiness, and design readiness.
6. **Match resources.** Ask Fleet what capacity exists now. Use ATS evidence
   to assess empirical capability. Keep availability and capability as
   separate claims; mark unknowns explicitly.
7. **Route.** Select the district, workbench, execution method, accountable
   Bosun, and next bounded action. Preserve alternatives when the choice is
   consequential or uncertain.
8. **Record.** Write a `RoutingDecision` as claim → evidence → warrant →
   boundary → decision. Include the expected next event or check-in.
9. **Dispatch.** Dispatch only through an authorized adapter. Workers receive
   the minimum complete context and permissions needed for the action.
10. **Monitor.** Observe state transitions and evidence of movement across
    projects. Do not request routine status merely to create activity.
11. **Recover.** When work stalls or a route becomes invalid, recontextualize,
    retry, reassign, change workbench, escalate, or create improvement work.
    Do not silently take over specialist execution.
12. **Close.** Reconcile material state, confirm evaluation/deployment status,
    and create both the artifact closeout and capability harvest.

## Output contract

Return a routing proposal, dispatch request, monitoring decision, recovery
action, or closeout record that includes:

- `work_item_id` and `project_id`;
- current state and readiness;
- destination or reason for holding;
- context status and missing inputs;
- Fleet capacity signal and ATS capability evidence;
- accountable Bosun or escalation target;
- dependencies and blockers;
- claim, evidence references, warrant, and boundaries;
- next action, expected event/check-in, and confidence;
- unresolved uncertainty and the record that should be created next.

If live system access is unavailable, produce a clearly labeled proposal and
do not invent current capacity, status, identifiers, or synchronization.

## References

Read only the references relevant to the current mode:

- [routing policy](references/routing-policy.md) for priority, fit, capacity,
  evidence, and decision recording;
- [context assembly](references/context-assembly.md) for ContextPackage
  construction and completeness gates;
- [cross-system contract](references/cross-system-contract.md) for Linear,
  Notion, Hermes, Beads, Superpowers, Fleet, ATS, and Chart boundaries;
- [monitoring and recovery](references/monitoring-recovery.md) for heartbeats,
  stall taxonomy, rerouting, and escalation;
- [closeout and learning](references/closeout-learning.md) for capability
  harvest and institutional memory;
- [role specification](references/role-specification.md) for the seat's
  boundaries and relationship to neighboring roles;
- [GitHub exemplars](references/github-exemplars.md) for the design patterns
  synthesized into this skill.

The machine-readable contracts are in `schemas/`. Examples are in `examples/`.
