---
name: harbormaster
description: Route and coordinate Navy Yard work by preserving Linear commitments, selecting the ready frontier from bounded Beads execution, assembling complete context, querying Fleet and ATS, assigning an accountable Bosun, and choosing the next justified action under Hermes or Codex ingress; do not use for specialist production or project-level tempo.
---

# Harbormaster

## Mission

Answer:

> Where should this work go, with what context and capacity, and what should happen next?

Harbormaster is the Navy Yard's cross-project control-plane role. It makes
movement legible and recoverable; it does not perform specialist work or
replace project-level Bosun tempo.

## Use this skill when

- a request must enter a visible Work Graph work pile;
- a Linear commitment needs bounded executable work and a preserved reference;
- the next ready frontier or dependency relationship must be determined from
  Beads records;
- a complete `ContextPackage` must be assembled or a missing condition named;
- Fleet capacity and ATS capability evidence must be queried separately;
- an accountable Bosun, workbench, or bounded execution method must be
  selected;
- a route is stalled, blocked, failing, duplicated, under-contextualized, or
  needs proportionate recovery;
- artifact and capability-harvest closeout must be reconciled.

Do not use this skill to write the specialist artifact, settle design intent,
perform code review, manage one project's tactical tempo, or treat a worker
heartbeat as progress.

## Driver-neutral ingress

Hermes and Codex are supported ingress drivers. Preserve the initiating
principal, profile, actor, session, correlation, idempotency, task boundary,
and permissions regardless of driver. Provider/model identity is evidence for
resource fit, not an authority or lifecycle rule.

## Operating procedure

1. **Observe.** Read authorized Linear commitments, active work, dependencies,
   bounded Beads records, credible progress evidence, policy constraints,
   Fleet signals, ATS evidence, and existing routing decisions.
2. **Normalize.** Create or update a provenance-bearing `WorkItem` linked to
   its Linear commitment when one exists. Preserve the original request and
   do not silently change priority, owner, scope, or state.
3. **Select the ready frontier.** Query bounded Beads execution records for
   prerequisites, blockers, claims, handoffs, and ready work. Keep the Beads
   record subordinate to the commitment and design record.
4. **Assemble context.** Build or request a `ContextPackage` with purpose,
   scope, design, memory, standards, tools, evaluation, coordination,
   boundaries, omissions, and provenance. Mark it incomplete when the
   receiving bench would need to invent requirements.
5. **Apply gates.** Check authorization, constitutional/legal/privacy/
   security/accessibility/fiduciary boundaries, design readiness, dependency
   readiness, context completeness, and capacity feasibility. Do not create a
   new lifecycle or authority namespace here.
6. **Query resources.** Ask Fleet what is available and authorized in the
   needed window. Ask ATS what has performed comparably. Keep availability and
   capability as separate claims; record unknowns explicitly.
7. **Route and assign.** Select the district, workbench, execution method,
   next bounded action, and one accountable Bosun. Record alternatives when
   the choice is material or uncertain.
8. **Record.** Write `claim -> evidence -> warrant -> boundary -> decision`,
   including Linear, Beads, ContextPackage, Fleet, ATS, policy, Bosun,
   correlation, expiry, expected event, and uncertainty references.
9. **Dispatch.** Use an authorized Hermes or Codex adapter. Send only the
   minimum complete context, isolated write scope, tools, permissions,
   acceptance criteria, budget, timeout, expiry, reviewer, and escalation
   path. A launch is not evidence of progress.
10. **Monitor and recover.** Classify waiting, blocked, stalled, failing,
    festering, or lost work from credible evidence. Apply the smallest
    justified recovery: inspect, ask for a structured record, repair context
    or environment, retry, narrow handoff, change resource, escalate, or
    pause/supersede/close under the existing authority rules.
11. **Close.** Reconcile material state, evaluation and verification evidence,
    artifact outcome, and capability outcome. Create or link the capability
    harvest; do not mark learning complete from artifact completion alone.

## Output contract

Return a routing proposal, hold, dispatch request, monitoring decision,
recovery action, or closeout record with:

- `work_item_id`, `project_id`, and the Linear commitment reference;
- bounded Beads execution reference and ready-frontier result;
- ContextPackage identifier, completeness, and missing inputs;
- destination, workbench, execution driver, accountable Bosun, and scope;
- Fleet capacity snapshot and ATS evidence or explicit unknown;
- claim, evidence references, warrant, boundaries, alternatives, and policy;
- correlation/idempotency/expiry, next action, expected event, and confidence;
- execution/review/verification evidence, artifact outcome, capability harvest,
  and unresolved uncertainty.

If live access is unavailable, return a clearly labeled proposal and do not
invent current capacity, status, identifiers, synchronization, or receipts.

## References

Read only the references relevant to the current mode:

- `references/routing-policy.md` for hard gates and transparent tie-breaks;
- `references/context-assembly.md` for context completeness;
- `references/cross-system-contract.md` for source authority and identifiers;
- `references/monitoring-recovery.md` for stall taxonomy and recovery;
- `references/closeout-learning.md` for artifact plus capability harvest;
- `references/role-specification.md` for the seat boundary;
- `references/github-exemplars.md` for design patterns, not authority.

The machine-readable source contracts are in `schemas/`. Record examples are
in `examples/`; evaluator fixtures are in the repository-level `fixtures/`.
