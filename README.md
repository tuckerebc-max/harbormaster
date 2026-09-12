# Harbormaster

Harbormaster is the Navy Yard's cross-project operational router and flow
manager. It answers:

> Where should this work go, with what context and capacity, and what should happen next?

The canonical package is organized by responsibility. Numbered copies and the
ambiguous filename from the former flattened upload are preserved under
`legacy/flattened-upload/`; the full original source remains in Git history.

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

From the repository root, using Python 3.9 or later:

```text
python -m pip install -r requirements.txt
python skills/harbormaster/scripts/validate_repo.py .
python -m unittest discover -s tests -v
```

These checks establish structural and fixture coherence only. They do not
authenticate connectors, reserve capacity, dispatch live work, or certify a
production control plane.

## Install the skill

Copy the entire `skills/harbormaster/` directory into the target harness's
skill directory. Keep its `agents`, `references`, `schemas`, and `examples`
companions together. The validator script checks a full source repository;
an installed skill folder alone does not contain the repository fixtures and
role records required for that check.

## Status

Version `0.1.0` specifies the routing contract and provides local package
validation. Live connector adapters and an event-replay routing harness
remain future work. The recovery retains the original upload at
`f75bbe034c6424f46058e05aad8c1b7a079ead9b` and the August 31 rehabilitation at
`dc4e8b75442acbf5704a898ca292854c197b53c0` in its history.
