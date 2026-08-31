# Intake at the dock

## Trigger

An external request, Linear issue/project, Notion observation, evaluator
failure, Fleet signal, maintenance need, or capability opportunity arrives.

## Procedure

1. Preserve the raw request and source provenance.
2. Create a stable `WorkItem` identifier.
3. Link the work to an existing Linear project or create a proposed linkage.
4. Classify sensitivity and initial priority without silently escalating it.
5. Identify duplicate, related, parent, blocking, and superseding records.
6. Place the item in `queued` or `triaging`.
7. Emit `work.created` and assign the next triage action to Harbormaster.

## Output

`WorkItem` plus an intake observation. Intake does not imply execution
authorization.
