# Context assembly

Context is part of capability. A skill file alone is not a sufficient context
package for consequential work.

## Minimum ContextPackage

Every dispatched work item should include, or explicitly mark as unavailable:

1. **Identity:** stable work item, project, repository, branch/workspace, and
   related Linear, Notion, Beads, design, and evaluation identifiers.
2. **Purpose:** the request in its original language and the intended use.
3. **Scope:** in-scope, out-of-scope, deliverable, acceptance criteria, and
   expected next decision.
4. **Design:** design record, claims, evidence, warrants, boundaries, and
   unresolved questions when design is required.
5. **Project memory:** client context, prior decisions, precedents, examples,
   previous attempts, known failures, and what good/done look like.
6. **Production environment:** selected workbench, tools, repository state,
   permitted model/agent surfaces, and artifact format.
7. **Evaluation:** harness, evaluators, test commands, review expectations,
   deployment gates, and required evidence.
8. **Coordination:** accountable Bosun, dependencies, parallel branches,
   handoff recipients, check-in event, budget, and escalation path.

## Completeness levels

| Level | Use |
|---|---|
| `minimal` | Clarifying intake or low-risk discovery only |
| `execution-ready` | Bounded production work with clear acceptance criteria |
| `evaluation-ready` | Work whose result must be tested or compared |
| `deployment-ready` | Work eligible for a policy-controlled release gate |

Harbormaster should never describe a package as `execution-ready` if required
design, authorization, context, or evaluation information is missing.

## Assembly rules

- Prefer authoritative records over summaries.
- Preserve original request language and provenance.
- Link to Notion records rather than copying entire institutional documents into
  Beads.
- Include only the context needed for the receiving bench, while retaining
  stable links to the complete record.
- Record what was not loaded and why.
- Do not merge client/project memory into an unrelated project.
- When sources conflict, preserve both, identify authority, and create a
  reconciliation item rather than silently choosing.
