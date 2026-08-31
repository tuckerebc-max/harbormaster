# Contributing

Changes should preserve the Navy Yard's role and system boundaries.

Before submitting a change:

1. run `python skills/harbormaster/scripts/validate_repo.py .`;
2. run the skill validator against `skills/harbormaster/`;
3. add or update a representative fixture when behavior changes;
4. record whether the change affects role scope, routing policy, schemas,
   adapters, evaluators, or only documentation;
5. do not add provider-specific behavior to the core role contract.

Any change that alters authority, priority, boundary, or deployment behavior
should include a short decision record in the pull request.
