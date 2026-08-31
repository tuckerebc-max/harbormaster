# Monitoring and recovery

Harbormaster monitors flow, not people. The signal is whether work is moving
with credible evidence toward its intended state.

## Progress evidence

Useful progress evidence includes:

- a state transition with timestamp and actor;
- a committed artifact or reviewable diff;
- a completed test or evaluator run;
- a resolved dependency;
- a new validated discovery;
- a recorded decision or handoff;
- a completed context or environment setup step.

“The agent is running” is not sufficient progress evidence.

## Stall taxonomy

| Condition | Meaning | First response |
|---|---|---|
| Waiting | A named external event is pending | Record event and expected expiry; do not nag |
| Blocked | A prerequisite or policy condition prevents progress | Identify blocker owner and create/route unblock work |
| Stalled | No credible progress within the expected window | Inspect last evidence, context, and worker health |
| Failing | Work produces evaluator, tool, or environment failures | Route repair or recontextualization work |
| Festering | Work remains open while value, scope, or ownership has decayed | Re-triage, split, supersede, or close with rationale |
| Lost | State or handoff cannot be reconstructed | Recover from durable records and create an incident |

## Recovery ladder

Use the smallest intervention likely to restore flow:

1. refresh or inspect the current state;
2. ask the Bosun for a structured blocker/progress record;
3. supply missing context or repair the execution environment;
4. retry the same worker when the failure is transient;
5. dispatch a fresh worker with a narrower handoff;
6. change workbench or resource when evidence supports the change;
7. escalate to Fleet, Architect, General Counsel, Parliamentarian, or Admiral;
8. supersede, pause, or close the work when the original route is no longer
   justified.

Each recovery action records why it was selected and what would trigger the
next step.

## Monitoring cadence

Cadence should be policy-driven by work type and risk. Use event-driven
signals when possible. A heartbeat is warranted when it supports a decision;
it is not warranted merely to prove that Harbormaster is active.
