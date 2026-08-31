# Harbormaster

Harbormaster is the Navy Yard's cross-project operational router and flow
manager. It answers:

> Where should this work go, with what context and capacity, and what should happen next?

The canonical package is now organized by responsibility. The previous
flattened upload, numbered copies, and ambiguous filename are preserved under
`legacy/flattened-upload/` for provenance; they are not active interfaces.

## Canonical package boundary

```text
harbormaster/
├── README.md
├── constitution/                 # durable routing boundaries
├── architecture/                 # Work Graph and Chart design
├── roles/                        # institutional seat and manifest
├── skills/harbormaster/          # portable, loadable skill package
│   ├── agents/openai.yaml
│   ├── examples/                 # record examples, not live state
│   ├── references/               # procedure and authority crosswalks
│   ├── schemas/                  # lightweight source contracts
│   ├── scripts/validate_repo.py
│   └── SKILL.md
├── integrations/                 # system-of-record adapters
├── workflows/                    # operational procedures
├── evaluators/                   # deterministic decision checks
├── fixtures/                     # credential-free route cases
├── research/                     # source synthesis
└── legacy/flattened-upload/      # preserved historical upload material
```

## Operating contract

Harbormaster routes and coordinates; it does not perform specialist work or
replace the Architect, Bosun, Fleet, ATS, Conductor, Linear, Notion, Hermes,
Beads, or Superpowers. Its decisions are reconstructable as:

`claim -> evidence -> warrant -> boundary -> routing decision -> next action`

The route path is:

`Linear commitment -> bounded Beads execution reference -> ready frontier -> ContextPackage -> Fleet/ATS query -> Bosun assignment -> authorized dispatch -> evidence/recovery -> artifact + capability harvest`

Ingress is driver-neutral. The same contract may arrive through Hermes or
Codex; provider/model identity remains an input, not a routing rule.

Harbormaster does not independently redefine lifecycle states or authority
rules. The controlling Work Bench crosswalk remains the integration owner's
authority for those decisions.

## Validation

From the repository root:

```text
python skills/harbormaster/scripts/validate_repo.py .
python -m unittest discover -s tests -v
```

These checks establish structural and fixture coherence only. They do not
authenticate connectors, reserve capacity, dispatch live work, or certify a
production control plane.

## Status

This branch is a proposed rehabilitation of the source at commit
`f75bbe034c6424f46058e05aad8c1b7a079ead9b`. It is not merged, pushed, or
activated.
