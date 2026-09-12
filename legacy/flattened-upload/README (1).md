# Harbormaster

Harbormaster is the Navy Yard's operational routing and flow-management role.
It answers one question:

> Where should this work go, with what context and capacity, and what should happen next?

This repository contains both:

- the institutional role specification in `roles/harbormaster.md`; and
- the loadable, model-agnostic skill in `skills/harbormaster/`.

Harbormaster coordinates work across projects, districts, workbenches, agents,
and resources. It does not perform specialist work and does not replace the
Bosun, Architect, Fleet Manager, ATS, Conductor, Linear, Notion, Hermes, or
Superpowers.

## Navy Yard system boundary

The repository implements the following federated Work Graph decision:

| Layer | System | Authority |
|---|---|---|
| Human commitments | Linear | Initiatives, projects, milestones, owners, priorities, high-level dependencies, and meaningful updates |
| Institutional memory | Notion | Constitution, design records, claims, evidence, warrants, boundaries, precedents, client context, and lessons |
| Control plane | Hermes | Intake, context assembly, routing, dispatch, monitoring, reconciliation, and follow-up creation |
| Agent execution ledger | Beads | Bounded executable work, dependencies, claims, handoffs, blockers, and session continuity |
| Execution method | Superpowers | Brainstorming, planning, implementation, review, testing, and verification |
| Navigation projection | Navy Yard Chart | A read-oriented view of linked project, work, capacity, evidence, and risk state |

Beads is deliberately bounded. It is not the database for the entire Navy
Yard. No irreplaceable institutional truth should live only in Beads.

## Repository map

```text
harbormaster/
├── README.md
├── constitution/             # durable operating principles and boundaries
├── architecture/             # federated Work Graph and Chart design
├── roles/                    # institutional seat specification
├── skills/harbormaster/      # portable Codex/Claude Code skill package
├── integrations/             # adapters and authority contracts
├── workflows/                # operational procedures
├── evaluators/               # harness-facing quality checks
├── fixtures/                 # adversarial and representative cases
├── research/                 # GitHub exemplar synthesis
└── tests/                    # deterministic repository checks
```

## Install the skill

Copy `skills/harbormaster/` into the target harness's skill directory, or load
the repository through the harness's plugin/marketplace mechanism. The skill is
designed to work with Claude Code, OpenAI Codex, Hermes, and other agent
harnesses that can read Markdown instructions and structured records.

The package is intentionally provider-neutral. Models, accounts, and vendors
are Fleet resources, not architectural assumptions.

## Operating contract

Every material route should be explainable through:

```text
claim → evidence → warrant → boundary → routing decision → next action
```

Every active project should have one accountable Bosun. Harbormaster sees the
flow across many projects; the Bosun manages tactical movement inside one
project or bounded workstream.

## Validation

From the repository root:

```bash
python3 skills/harbormaster/scripts/validate_repo.py .
```

The validator checks the skill package, required references, schemas, and
fixtures. It does not replace a live integration harness.

## Status

Version `0.1.0` is an architecture-ready first release. It specifies the
control-plane contract and read-oriented behavior before adding live mutation
against Linear, Notion, Hermes, or Beads.
