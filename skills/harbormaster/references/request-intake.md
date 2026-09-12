# Request intake and handoff

Use this guide to start a request proportionately. It is an intake and
handoff aid, not a scheduler, runtime, provider router, or requirement that
every request use the full Harbormaster route.

## Start with four facts

Before routing material work, establish:

- the intended result and what would count as acceptance;
- the current account or seat and whether it is authorized for the result;
- the authorized surfaces and the minimum write scope;
- facts already supplied by the requester, reused without another approval
  ceremony.

If a fact is unknown, record it as unknown instead of inventing authority,
capacity, approval, or completion.

## Route classes

| Class | Use when | Smallest proportionate response |
|---|---|---|
| Simple answer | A direct question can be answered from supplied or safe-to-read context. | Answer directly. Do not open a workflow, worktree, approval cycle, or all-skill scan. |
| Read-only inquiry | A bounded question needs source, log, or state inspection but no writes. | State the question, scope, authorized sources, evidence, and limits. Stop when the question is answered. |
| Implementation | A material artifact must be created or changed. | Give an explicit handoff with exact revision, context, acceptance, isolated scope when warranted, and a reviewer separate from the builder. |
| Signal or learning | A completed material result, decision, gain, or failure warrants feedback; otherwise record no material signal. | Hand the bounded result to the evidence/learning receiver without changing role authority. |

These classes can become successive stages. For example, a read-only inquiry
may reveal a bounded implementation need; do not relabel the whole request as
"implementation" until that need is established.

## Role family and selection

Keep one seat for each function. The following public skill names are the
Navy Yard request family; no task should activate all of them:

`admiral`, `navy-yard-admiral`, `architect`, `navy-yard-architect`, `bosun`,
`navy-yard-bosun`, `harbormaster`, `navy-yard-parliamentarian`,
`navy-yard-stargazer`, `learning-experience-designer`,
`kwt-workspace-workflow`, and `lighthouse-keeper`.

Selection rules:

- A version-pinned or user-selected role contract controls. Do not replace or
  silently reinterpret it.
- Standalone `admiral`, `architect`, and `bosun` procedures and the
  corresponding `navy-yard-*` governed record packages are separate
  implementations of those functions. Do not invent precedence or invoke both
  as duplicate seats.
- If neither implementation is explicitly selected, use the single
  implementation already assigned to the work item or authorized by current
  local policy. If that choice is unavailable or ambiguous, record the unknown
  and route through Harbormaster without promoting a wrapper.
- Use `navy-yard-parliamentarian` for an actual authority conflict.
- Use `navy-yard-stargazer` only for a bounded external-discovery candidate.
- Use `learning-experience-designer` when work bears a learning record.
- Use `kwt-workspace-workflow` for isolated implementation only, not trivial
  or read-only requests.
- Use `lighthouse-keeper` for a material result or an explicit no-material-
  signal path.
- RoboRev and Superpowers participate through their independently verified
  capabilities and receipts. Installation is handled elsewhere; missing
  tooling is an explicit limitation, not a fabricated pass or duplicate setup.

## Handoff record

A delivery handoff carries, in the target package's existing envelope where
possible:

- account or seat and the receiving function;
- work item and exact source plus revision;
- implementation evidence and verification commands/results;
- independent review evidence, distinct from the builder;
- GitHub or Linear state where applicable, marked unknown when unavailable;
- unresolved limits, blocked/partial/published state, and next receiver.

Unknown, blocked, partial, and published remain distinct. A launch or task
completion claim is not verification evidence.

## Walkthroughs

### Simple answer

Request: "What does this setting control?"

Intake class: simple answer. Reuse the supplied configuration; read only the
authorized local file if needed; answer with the controlling fact. No work
item, KWT, implementation handoff, or all-family activation.

### Bounded code repair

Request: "Fix this failing test without changing public behavior."

Intake class: implementation. Confirm the intended behavior, failing command,
repository, and exact commit. Assign one builder and one independent reviewer;
they are not the same seat. Use KWT only when isolated implementation is
warranted and supported. Deliver exact revision, command result, review
evidence, GitHub/Linear state, and limits. If the reviewer finds unresolved
defects, return the state as partial or blocked rather than published.

### Authority conflict

Request: two records disagree about which role may approve a deployment.

Intake class: read-only inquiry until the conflict is established. Assemble
the conflicting citations and unresolved question, then hand it to
`navy-yard-parliamentarian`. Preserve the unresolved state in the handoff.
Harbormaster does not settle rule precedence, and Bosun does not become the
independent reviewer of its own builder.
