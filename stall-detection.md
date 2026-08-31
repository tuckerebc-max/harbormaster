# Stall-detection evaluator

Given an event stream, determine whether Harbormaster correctly identifies
waiting, blocked, stalled, failing, festering, and lost work.

Pass when the response uses credible progress evidence, applies a proportionate
recovery action, names an owner and next event, and avoids unnecessary status
polling.
