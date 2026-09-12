# Design rationale

## Decision

Harbormaster is a control-plane role and skill over a federated Work Graph.
Beads is a bounded agent-execution ledger, not the database for the entire
Navy Yard.

## Why this shape

The attached architecture memo identifies distinct authorities:

- Linear: human commitments and project state;
- Notion: institutional memory and design reasoning;
- Hermes: routing and reconciliation;
- Beads: active agent work, dependencies, handoffs, and session continuity;
- Superpowers: execution method;
- Fleet: current capacity;
- ATS: empirical capability evidence;
- Navy Yard Chart: human navigation projection.

This preserves the Navy Yard principle that durable infrastructure should
survive changing tenants. It also preserves the distinction between:

- what the Architect says should be built;
- where Harbormaster routes it;
- how the Bosun keeps it moving;
- what Fleet can provide;
- what ATS has evidence to support.

## Implementation posture

Start with a read-oriented router and Chart projection. Add bounded dispatch
only after routing records, context completeness, capacity signals, and stall
recovery pass the evaluators in this repository.
