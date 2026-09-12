# Navy Yard Chart

The Chart is a role-specific read projection of the Work Graph, not another
source of truth and not a required graph database.

## First projection

The initial read-only Chart should show:

- Linear projects and commitments;
- active Beads work and ready frontier;
- dependencies and blockers;
- current Bosun and workbench assignments;
- Fleet availability and reservations;
- recent evaluator failures and regressions;
- pending capability improvements;
- policy or reconciliation holds.

## Seat-specific projections

| Seat | Primary view |
|---|---|
| Admiral | Delivery, capability gain, bottlenecks, strategic priority, institutional health |
| Harbormaster | Ready work, routing, dependencies, capacity, stalls, next actions |
| Bosun | One project's route, blockers, progress evidence, and handoffs |
| Fleet Manager | Resource inventory, availability, quota, health, and substitutions |
| Architect | Design records, claims, evidence, warrants, boundaries, and evaluators |
| ATS | Harnesses, evaluator runs, scores, regressions, and comparisons |
