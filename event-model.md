# Event model

Important transitions should emit durable events so the yard can create useful
follow-on work without executive attention at every step.

## Core events

```text
work.created
work.triaged
context.requested
context.ready
design.required
design.approved
route.proposed
route.accepted
dispatch.requested
work.started
bosun.heartbeat
work.blocked
work.stalled
fleet.capacity_changed
fleet.resource_throttled
evaluation.failed
evaluation.regression_detected
work.reassigned
escalation.created
work.completed
deployment.completed
capability.harvest_requested
capability.harvested
reconciliation.required
```

Every event should include a correlation ID, source record, actor, timestamp,
canonical state, and provenance.
