# Routing policy

Harbormaster should not reduce routing to an opaque numerical score. Use hard
gates first, then transparent tie-breaks.

## Routing gates

1. **Boundary and authorization:** Is the action inside constitutional, legal,
   privacy, security, accessibility, fiduciary, and account permissions?
2. **Design readiness:** Does consequential work have an approved or otherwise
   authorized `DesignRecord` with success criteria and evaluator requirements?
3. **Dependency readiness:** Are prerequisites complete, or is the work
   explicitly a valid parallel branch?
4. **Context completeness:** Does the receiving bench have the minimum complete
   context to act without inventing requirements?
5. **Capacity feasibility:** Does Fleet report usable capacity in the needed
   window, with the required permissions and toolchain?

Failure at a gate creates a hold, clarification, escalation, or improvement
work item. It is not a reason to improvise around the gate.

## Tie-break order

Among routes that pass the gates, prefer in this order:

1. critical safety, legal, security, or production recovery work;
2. work that unblocks the largest number of ready or high-priority dependents;
3. Admiral/Linear strategic priority and deadline;
4. strongest task-to-workbench and task-to-resource fit;
5. strongest ATS evidence under comparable conditions;
6. continuity where switching would lose meaningful context;
7. lower cost, latency, or opportunity cost;
8. fair treatment of projects competing for scarce capacity.

The exact policy may be configured by the Admiral, but the selected policy
version must be recorded with every material route.

## Availability versus capability

These are different claims:

- **Fleet claim:** this resource is available, usable, and authorized in a
  defined window;
- **ATS claim:** this resource has demonstrated a level of performance on a
  comparable task and harness;
- **Harbormaster decision:** given both claims and the relevant boundaries,
  this resource is the best justified route now.

If either claim is missing, record `unknown` and route conservatively.

## Parallelism

Parallelize only when:

- work items are independent or their interfaces are explicit;
- workers have isolated workspaces or non-overlapping write scope;
- the merge or synthesis point is named;
- the receiving Bosun can observe the fan-out and fan-in;
- the expected coordination cost is lower than serial execution.

Do not parallelize merely because multiple agents are available.

## Decision record

Every consequential route records:

```text
claim: what route is believed to be best
evidence: Fleet, ATS, context, dependency, policy, and prior-work references
warrant: why the evidence supports the route
boundaries: constraints that rule out alternatives
decision: selected district, bench, Bosun, resources, and next action
alternatives: credible alternatives and why they were not selected
uncertainty: what could change the decision
```
