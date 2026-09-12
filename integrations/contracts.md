# Harbormaster interface inventory

This is the proposed adapter surface for the rehabilitated package. The
controlling Work Bench crosswalk remains authoritative for lifecycle states,
authority rules, and future versioned JSON contracts.

| Interface | Source of truth | Harbormaster contract |
|---|---|---|
| `WorkItem` | Linear commitment plus source provenance | Normalize addressable work without changing commitment state. |
| `ContextPackage` | Hermes assembly over authorized records | Carry purpose, scope, design, memory, standards, tools, evaluation, coordination, omissions, and provenance. |
| `RoutingDecision` | Hermes decision record | Preserve claim, evidence, warrant, boundaries, alternatives, policy version, capacity/ATS references, decision, uncertainty, and next event. |
| `ProgressEvidence` | Worker/Bosun/evaluator records | Accept artifacts, tests, resolved dependencies, decisions, or validated discoveries; a heartbeat alone is not completion. |
| `CapacityOffer` | Fleet | Preserve availability, permission, quota, cost, concurrency, expiry, and constraints separately from capability. |
| `Escalation` | Hermes/approval record | Name the blocked condition, decision owner, evidence, options, severity, expiry, and disposition. |
| `CapabilityHarvest` | Notion/learning record | Record artifact outcome and capability outcome separately; adoption remains human-gated. |

## Driver-neutral ingress

An ingress adapter accepts either `hermes` or `codex` as `source_channel` and
must preserve `principal_id`, `profile_id`, `actor_id`, `session_id`,
`correlation_id`, `idempotency_key`, `context_package_id`, `routing_decision_id`,
and the exact task boundary. It returns a bounded execution reference and
does not infer a different lifecycle or authority state from the driver.

## Execution reference

The minimum bounded Beads reference is:

```yaml
bead_id: bead_<opaque-id>
linear_issue_id: <committed-work-ref>
project_id: <project-ref>
context_package_id: cp_<opaque-id>
routing_decision_id: route_<opaque-id>
dependencies: []
ready_frontier: true | false | unknown
scope: {in: [], out: []}
write_scope: <isolated workspace/ref>
acceptance: []
budget: {tokens: null, time_minutes: null, cost_class: null}
expires_at: <utc-or-null>
```

The reference points to bounded agent-facing work; it is not a replacement
for the Linear commitment or durable design record.

## Receipt chain

Each adapter should emit or retain a receipt linking:

`ingress -> ContextPackage -> RoutingDecision -> Beads reference -> Bosun assignment -> execution evidence -> review/verification -> artifact outcome + capability harvest`

Unknown, partial, expired, and rolled-back outcomes remain visible until
reconciled. No receipt is proof of human acceptance or release.
