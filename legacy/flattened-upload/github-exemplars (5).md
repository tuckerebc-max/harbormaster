# GitHub exemplar synthesis

These repositories were selected for their contribution to Harbormaster's
control-plane problem. They are patterns to adapt, not dependencies to copy
wholesale.

| Exemplar | Pattern extracted | Navy Yard use |
|---|---|---|
| [Gas Town](https://github.com/gastownhall/gastown) | Mayor, Rigs, Convoys, Witness/Deacon health, Refinery, escalation, scheduler | Cross-project flow, project containers, worker health, merge/recovery lanes |
| [Beads](https://github.com/gastownhall/beads) | Persistent dependency graph, ready frontier, atomic claim, memory, history | Bounded agent-execution ledger within the federated Work Graph |
| [GitHub Agentic Workflows](https://github.com/github/gh-aw) | Orchestrator/worker, safe outputs, scoped permissions, async dispatch, correlation IDs | Guarded dispatch and explicit handoffs |
| [AIDA](https://github.com/joemooney/aida) | Stable spec IDs, code-to-intent traces, typed relationships, impact queries | Claim/evidence/warrant traceability and reconstruction |
| [CC-Manager](https://github.com/agent-next/cc-manager) | Priority queue, worktree workers, budgets, SSE, persistence, auto-merge | Scheduler and operational telemetry patterns |
| [`wshobson/agents`](https://github.com/wshobson/agents) | Portable multi-harness plugins, agents, skills, progressive disclosure | Provider-neutral package and harness adapters |
| [Superpowers](https://github.com/obra/superpowers) | Spec → plan → fresh subagent → review → final verification | Execution method after routing |
| [LangGraph](https://github.com/langchain-ai/langgraph) | Durable state, interruption, recovery, human-in-loop | Resumable Harbormaster state machine |
| [OpenHands Agent Canvas](https://github.com/OpenHands/OpenHands) | Multi-backend control center, automations, issue decomposition | Unified operational surface across agent backends |
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | Differentiated roles and explicit software-company SOPs | Role separation and repeatable route formulas |

## Selection judgment

The strongest direct precedent is Gas Town plus Beads. The strongest Navy Yard
adaptation is a federation: Linear and Notion retain their authority while
Hermes coordinates and Beads represents only active agent execution.

Do not make the Harbormaster a copy of a generic supervisor agent. Its unique
responsibility is evidence-backed movement across projects, workbenches,
capacity pools, policy boundaries, and institutional memory.
