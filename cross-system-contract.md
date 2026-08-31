# Federated Work Graph contract

The Navy Yard uses multiple systems with explicit authority boundaries.

| Layer | System | Canonical responsibility |
|---|---|---|
| Commitment ledger | Linear | Initiatives, projects, milestones, owners, priority, high-level dependencies, and human-visible updates |
| Institutional memory | Notion | Constitution, design records, claims, evidence, warrants, boundaries, precedents, client context, and lessons |
| Control plane | Hermes | Intake, context assembly, routing, dispatch, monitoring, reconciliation, and follow-up creation |
| Agent execution ledger | Beads | Bounded executable work, dependencies, claims, handoffs, blockers, and session continuity |
| Execution method | Superpowers | Brainstorming, planning, implementation, review, testing, and verification |
| Navigation projection | Navy Yard Chart | Read-oriented synthesis for a specific seat or question |
| Capacity service | Fleet | Inventory, availability, reservations, quotas, health, and operational constraints |
| Capability evidence | ATS | Harnesses, evaluators, runs, comparisons, regressions, and empirical performance |

## Identifier contract

Cross-system records may carry:

```text
linear_initiative_id
linear_project_id
linear_issue_id
bead_id
notion_page_id
design_record_id
evaluation_run_id
fleet_resource_id
workbench_id
routing_decision_id
```

Identifiers are references, not permission to duplicate the source record.

## Synchronization rules

1. Every synchronized object declares its source system and authority fields.
2. Hermes performs explicit reconciliation; it does not create ambiguous silent
   two-way synchronization.
3. Linear receives meaningful project state, not every Beads heartbeat.
4. Notion receives durable reasoning and learning, not transient session noise.
5. Beads may contain links to design records but does not replace them.
6. The Chart is generated from source records and is not a new system of record.
7. Conflicts become visible `reconciliation` work rather than overwrites.

## Status mapping

Status names may differ by system. Store a canonical operational state and the
source-system projection:

```text
queued | triaging | awaiting_context | awaiting_design | ready | reserved
dispatched | in_progress | blocked | evaluating | awaiting_decision
complete | deployed | harvested | cancelled | superseded
```
