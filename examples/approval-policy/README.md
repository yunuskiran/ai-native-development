# Approval-policy teaching example

Original TypeScript model for the book. It handles one sequential approval transition over trusted in-memory domain records. It is **not the SaaS, a framework implementation or an independently reviewed acceptance oracle**.

Run from the repository root:

```sh
node --test examples/approval-policy/approval-policy.test.ts
```

No package installation or external service is needed. The locally observed runtime is **Node.js v26.13.0**. Other runtimes are not verified here. Node's built-in TypeScript stripping executes erasable syntax without type-checking; `tsc` is not available on the session PATH, so static type-checking is **NOT PERFORMED**. [Node TypeScript documentation](https://nodejs.org/api/typescript.html)

The checks address selected policy expectations behind CS-04/05/06/07/12/13. They do not complete those requirements' application acceptance: no authentication, request reader, database, audit, idempotency-key contract, rejected-decision operation, HTTP disclosure policy, race safety or persistence is modeled. In particular, `duplicate_actor` means no second approval count; it does not implement CS-08 retry semantics.

Inputs assume coherent, established domain records. Type annotations are not runtime input validation. Internal reason codes must not be exposed as a production error contract. The function does not mutate its input; actual transactional correctness still needs a chosen persistence/concurrency design and independent checks.

Tests are authored alongside the model from the stated case expectations. Passing them is a narrow local observation, not independent validation, a method score, a benchmark or production-readiness evidence. See the [execution record](../../research/evidence/POLICY_MODEL_RUN.json) for the actual command/result and file identities.
