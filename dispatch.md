# Dispatch bounded work

## Dispatch contract

The dispatch payload must identify:

- work item, project, and routing decision;
- receiving district and workbench;
- accountable Bosun;
- exact task boundary and write scope;
- context-package identifier;
- tools and permissions;
- dependencies and expected outputs;
- evaluator/harness requirements;
- budget and timeout;
- progress-evidence expectations;
- next event or check-in;
- escalation path.

## Rules

- Dispatch only after required gates pass.
- Use isolated workspaces for parallel writes.
- Do not dispatch the same exclusive work to multiple workers without an
  explicit duplication experiment or recovery policy.
- Use stable correlation identifiers across Hermes, Beads, Linear, and worker
  events.
- Do not treat a worker launch as evidence of progress.
