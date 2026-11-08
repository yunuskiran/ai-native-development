# M0 case-study feasibility and experiment readiness

Status: **NOT READY FOR EXECUTION**, 2026-10-31. This is an original design proposal, not a replacement for the missing `CASE_STUDY_SPEC.md`. No application, harness, trial, pilot or benchmark was run. All quantities below describe proposed design or planning arithmetic, never observed results.

M1 follow-up: the author selected **TypeScript / Node.js**; a new proposed [case specification](../CASE_STUDY_SPEC.md) and [run protocol](RUN_PROTOCOL.md) now make the scope reviewable. They are not a recovered original, approved domain, frozen baseline or executed readiness check. The M0 inventory statements below describe intake; all ER checks remain unpassed.

## Feasibility judgment

The master plan's small B2B multi-tenant workflow is suitable in principle for comparing decomposition, decision rights, artifacts and evidence. It is not yet a controlled experiment. The checkout has no business specification, implementation baseline, test oracle, run manifest or result logs. Model/host access, budget and operator availability have not been established.

| Evidence tier | Judgment | What it can support | Limits |
|---|---|---|---|
| Matched artifact walkthrough | Plausible after requirements and source dossiers are approved | How selected profiles translate the same brief into decisions and artifacts | Cannot establish productivity, correctness or production suitability without execution. |
| Executed comparative episodes | Conditional on controls and readiness checks below | Descriptive outcomes for selected tasks, versions, operators and budgets | One case and a few runs do not justify general causal superiority. |
| Team/enterprise/production comparison | Outside the current evidence plan | Would require actual teams, organizational constraints and operational observation | A solo author or simulated AI roles cannot validate collaboration, compliance or operational reliability claims. |

Recommendation: make the walkthrough a viable deliverable; promote to measured episodes only if the gate passes. This follows the master's fallback policy and does not predetermine results.

## Proposed business slice — author approval required

Candidate: **tenant-scoped vendor-access approvals**. A synthetic customer organization requests temporary access for a vendor; an authorized approver decides; an audit history records the change. Two synthetic tenants allow boundary tests. Roles could be requester, approver and tenant administrator. No real vendor integration, external identity service, messaging, subscription billing or cloud deployment is needed for this proposed slice.

Possible common invariants to freeze in the actual specification:

- An authenticated member sees only their tenant's requests and history, including search/list and direct-ID access.
- The requester cannot approve their own request. Role changes and tenant membership are checked when the decision is made.
- Only allowed state transitions occur; duplicate requests and conflicting concurrent decisions have defined outcomes.
- Decisions record actor, tenant, time and policy version; access to history is tenant-scoped. “Append-only” must be defined and tested rather than assumed from a table name.
- A later policy revision requires two distinct approvers for high-risk requests, with explicit handling of requests already in progress.

These are draft requirements, not an established industry approval standard. Domain, detailed behavior, UI/API contracts, architecture constraints and stack remain D06. The master plan's ASP.NET reference is not enough to choose .NET. S10's .NET plugin listing is a compatibility lead, not a validated adapter.

## Candidate matched episodes

| Episode | Shared input | What to observe | Independent acceptance target to define later |
|---|---|---|---|
| E1 — bounded feature | Same frozen brief and minimal scaffold for each method | Questions, decomposition, necessary human decisions, artifact handoffs and working increment | Correct request/create/read/decision behavior, tenant and role invariants, required history. |
| E2 — policy change | Same seeded working baseline for every method, not each method's E1 output | Specification maintenance, change propagation, regression reasoning and review | Two distinct approvals for high-risk requests and explicit migration semantics; existing valid behavior retained. |
| E3 — boundary defect | Same seeded baseline and same externally observable bug report | Diagnosis, scope control, evidence and cost of a small repair | Predetermined tenant-leakage defect corrected on the affected path, with independent regression checks and no unrelated regressions. |

Use separate common baselines per episode for a matched comparison. Continuing each method's own implementation across episodes is useful longitudinal observation, but then inputs differ; label that a separate walkthrough, not the same controlled result. Fix the bug and hidden checks before measured runs. Do not tune them to discriminate against an observed method.

Four frameworks × three episodes × one repetition would be **12 episode runs**. Three repetitions would be **36**, before familiarization and failed runs. This arithmetic is not a sample-size justification, budget approval, or predicted runtime. Select replication after pilots and a feasibility review. There is no fifth SDD arm. A lightweight control arm would need its own explicit protocol and author approval; it must not be an intentionally careless straw baseline.

## Controls and failure handling

| Control | Proposed rule |
|---|---|
| Unit of comparison | Frozen method source + implementation profile + task episode + operator/host/model configuration. Publish that unit alongside every observation. |
| Shared vs free choices | Same business brief, externally visible acceptance contract and allowed infrastructure. Allow native artifact names, phase structure and decomposition. Do not force an AIUP use-case template onto the other methods. |
| Models and hosts | Prefer one compatible host and exact model settings. Record provider identifier, exposed model revision, effort, context limits and date for every agent call. If exact revisions or shared hosts cannot be controlled, disclose the confounder and downgrade claims. |
| Resources | Author-approved wall-time, active-human-time and token/spend ceilings; identical maximum tool/network permissions. Charge all worker/model calls to the run. Do not flatten native orchestration and then describe the intervention as the unmodified method. |
| Fidelity | Record required core steps, optional add-ons, defaults, profile overrides and deviations. Separate a common-host profile comparison from native-stack demonstrations. Preapprove local substitutes for deployment rather than skipping stages silently. |
| Learning and carryover | Familiarize operators on different work before scoring; reset context, project state and caches under a written rule. Counterbalance method order. Do not transfer generated solutions or hidden acceptance tests between runs. Log prior experience. |
| Acceptance oracle | Human-reviewed tests prepared before measured runs, independent of each method's generated tests. Use synthetic fixtures, success/failure cases and tenant-boundary checks. Holdout checks and adjudication rules fixed in advance. |
| Blind review where feasible | Evaluate de-identified outputs against the same criteria; record when artifact styles reveal method identity. Human reviewers need conflicts and calibration recorded. |
| Failures | Retain timeouts, broken builds, aborted runs and missing telemetry. Predefine allowed recovery and exclusions; never rerun silently until success or drop a failed method. |
| Freeze and drift | Hash seed commits, brief, oracle and configurations. Record method/plugin/package pins and permitted updates. Model drift or tool changes can require a new experimental block rather than pooled numbers. |
| Analysis | Publish per-run observations and distributions if repeated. No significance claims, universal rankings or causal claims without adequate design. Keep missing values explicit; no invented scores. |

## Measurement definitions to finalize before trials

| Observation | Operational definition to pre-register | Important limit |
|---|---|---|
| Acceptance outcome | Pass/fail for each frozen requirement/invariant on final artifact commit | A generated test suite passing is not an independent acceptance pass. |
| Elapsed time | Start/end boundaries, including AI execution, build waits, review gates, recovery and external waits as separate components | Report setup/familiarization separately and in total adoption effort; do not hide costs. |
| Human effort | Active minutes and decision/correction events classified under a fixed rubric | Subjective activity logs need consistent treatment and reviewer checks. |
| Resource use | Actual input/output/cache units and worker calls; monetary estimate only from dated rates and observed usage | Subscription costs and unavailable telemetry must be disclosed, not imputed as zero. |
| Defects and repair | Independent failed checks at checkpoints, severity/adjudication rule and subsequent repair work | Avoid defining “quality” as raw defect count or coverage percentage alone. |
| Traceability and drift | Sampled links among requirement, artifact, code and tests, plus explicit contradictions after E2 | Presence of documents or a model's assertion is not correctness. |
| Artifact usefulness / overhead | Required decisions captured, review effort and later retrieval task under an anchored rubric | Document/page count is not a benefit or a cost by itself. |
| Reproduction | Clean-environment commands, version manifest, test results and output hashes | A rerun may differ; reproducible procedure does not promise deterministic generation. |

No aggregate numeric score is proposed at M0. Runtime, security, portability and maintainability all remain **Not assessed**.

## Experiment readiness checklist

An unchecked box is work remaining, not failure of a method.

- [ ] **ER01 — Scope:** Author approves domain, stack, task episodes and qualitative/measured evidence tier (D06–D08).
- [ ] **ER02 — Specification:** Requirements, constraints, non-goals, identifiers, edge cases and policy-change behavior reviewed and frozen.
- [ ] **ER03 — Baselines:** Identical per-episode seed commits, synthetic fixtures and reset procedure verified; longitudinal variants separated.
- [ ] **ER04 — Oracle:** Independent acceptance/holdout checks and adjudication rules reviewed, runnable and frozen before measured runs.
- [ ] **ER05 — Method profiles:** Required/optional steps, exact source/package/plugin versions, licences and deviations reviewed for all four.
- [ ] **ER06 — Compatibility:** Each selected profile completes an unscored install/smoke exercise on the same proposed host/model/stack, or confounders are accepted explicitly.
- [ ] **ER07 — Access and budget:** Existing authorized model access confirmed; author sets time/spend ceilings and stop conditions. New paid services require author action.
- [ ] **ER08 — Operators:** Familiarization, experience disclosure, run order and reviewer independence/calibration recorded.
- [ ] **ER09 — Instrumentation:** All worker calls, timing, interventions, recovery and telemetry captured; redaction protects credentials and personal data.
- [ ] **ER10 — Analysis:** Metrics, replication, exclusions, missing-data treatment and reporting limitations pre-registered before measurements.
- [ ] **ER11 — Local safety/operations scope:** Synthetic-only data, local execution, tool permissions and operational substitutes defined; no production claims from a local demo.
- [ ] **ER12 — Evidence packaging:** Run manifest, source/artifact hashes, commands, actual checks and logs tested in a clean reproduction exercise.
- [ ] **ER13 — Gate:** Author and technical reviewer accept readiness and deviations. If essential controls fail, use a labeled walkthrough and record why.

M0 output is this checklist and feasibility analysis. Filling the checklist, implementing tests and running pilots belong to later authorized milestones. External hosting or publication remains author-controlled.
