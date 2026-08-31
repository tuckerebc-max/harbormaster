# Triage and route

## Procedure

1. Determine whether the item is delivery, maintenance, research, evaluation,
   capability improvement, policy, or reconciliation work.
2. Determine the project and whether the work should remain a project-level
   commitment or become bounded agent execution.
3. Identify dependencies and the current ready frontier.
4. Check whether an Architect design record is required.
5. Assemble or request the `ContextPackage`.
6. Check constitutional, legal, privacy, security, accessibility, fiduciary,
   and authorization boundaries.
7. Identify candidate districts, workbenches, Bosuns, and resources.
8. Query Fleet for current capacity and ATS for comparable capability evidence.
9. Apply the routing policy and preserve rejected alternatives when material.
10. Write the `RoutingDecision`.
11. Either hold with a named missing condition or dispatch the next bounded
    action.

## Valid hold reasons

```text
awaiting_context
awaiting_design
awaiting_authorization
awaiting_dependency
awaiting_capacity
awaiting_policy_interpretation
awaiting_reconciliation
```
