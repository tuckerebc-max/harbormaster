# Hermes adapter

Hermes is the control-plane integration surface. It may provide:

- intake and normalization;
- context retrieval and package assembly;
- routing proposal and decision persistence;
- dispatch to agent/model/workbench backends;
- event subscriptions;
- status reconciliation;
- follow-up and capability-improvement creation.

Hermes must expose source identifiers and operational evidence rather than
becoming an opaque super-database. Provider/model identity remains Fleet
configuration.
