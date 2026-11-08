# Future case-study run protocol

Status: **M1 protocol outline — NO RUNS AUTHORIZED OR EXECUTED**, 2026-10-31. This operationalizes the [M0 readiness assessment](EXPERIMENT_READINESS.md) for the proposed [TypeScript / Node.js case](../CASE_STUDY_SPEC.md). Requirements, domain, framework/database and exact versions remain unfrozen. Owner names are roles until a person is appointed.

## Evidence modes and promotion gate

Default proposed mode: artifact walkthrough with explicit provenance and limitations. A walkthrough may explain a process but cannot report unobserved speed, defects or acceptance passes. An executed comparison requires all essential readiness conditions, independent oracle review, authorized access/budget and a predeclared analysis plan. If controls cannot be met, publish the reason and retain the walkthrough label.

Four method/profile arms share E1/E2/E3 business inputs. SDD is not a fifth arm. Single-method pilots are familiarization, not scored comparison. Separate any native-host demonstration from a common-host comparison. Choose repetitions and blocking after feasibility; 12 or 36 episode runs are planning arithmetic, not a sample-size justification or approved spend.

## Readiness ownership and acceptance evidence

| Item | Accountable role / milestone | Evidence required before execution |
|---|---|---|
| ER01 Scope | Author / M1 review then M4 freeze | Domain, TypeScript/Node constraints, episodes and evidence mode accepted. |
| ER02 Specification | Requirements reviewer / M4 | CS requirements and interface/policy edge cases reviewed; brief/oracle hashes fixed. |
| ER03 Baselines | Implementation engineer + reviewer / M4 | Same episode-specific seed commits and synthetic fixtures; reset procedure demonstrated. |
| ER04 Oracle | Independent technical reviewer / M4 | Tests authored/reviewed apart from generated solutions, negative cases and adjudication rules fixed. |
| ER05 Profiles | Research editor / M2; reviewer / M4 | Source/package/plugin provenance, required/optional steps, permissions and deviations recorded. |
| ER06 Compatibility | Implementation engineer / M4 unscored setup | Each profile's actual setup on chosen host/model/TypeScript stack works, or confounders are explicitly accepted. |
| ER07 Access/resources | Author / before any paid or scored run | Existing access confirmed; run, human-time, token/spend ceilings and stop conditions approved. |
| ER08 Operators/reviewers | Author + reviewer / M4 | People, experience, familiarization, ordering and conflicts documented; review calibration recorded. |
| ER09 Instrumentation | Implementation engineer / M4 | Worker calls, effort, timings, interventions and failures captured; secrets redacted. |
| ER10 Analysis | Research/technical reviewers / before measurements | Metrics, replication/blocking, missing data, exclusions and inference limits pre-registered. |
| ER11 Local scope | Technical reviewer / M4 | Synthetic data, local permissions and operational substitutes specified; no production inference. |
| ER12 Reproduction | Technical reviewer / M4 | Clean run instructions, manifests, actual check outputs and artifact hashes verified. |
| ER13 Gate | Author + technical reviewer / M4 | Signed readiness/disposition and all accepted deviations; otherwise downgrade evidence mode. |

No checkbox is automatically passed by assigning an owner or preparing a document.

## Required run manifest

Record run ID, evidence mode, method/profile and source pins, packages/plugins, task and neutral brief hash, seed/fixture/oracle hashes, actual Node.js/TypeScript and framework/database versions, OS/hardware, host/model identifiers and exposed revisions, reasoning/settings/context policy, operator background, order/block/repetition, permissions, resource ceilings, start/stop boundaries and approved deviations.

Record every subordinate agent/model/tool call when exposed. Unknown telemetry is missing data, never zero. Source/provider recommendations are not a substitute for matching actual model configurations. Provider revision opacity must be disclosed.

## Execution outline for a later authorized milestone

1. Check the approved manifest and restore the common per-episode baseline. Keep generated solutions/holdout checks out of other runs' context.
2. Give the same frozen business brief, external acceptance interface and allowed resources, allowing method-native artifacts and decomposition.
3. Log human decisions, waits, corrections, worker calls and failures under defined event categories. Observe native gates; record any adaptation needed for local-only execution.
4. Stop at completion or an approved cap. Preserve the final attempted commit and unfinished state, including build failures/timeouts.
5. Run independent checks under the frozen disclosure/retry policy. Generated suites are supplemental. Adjudicate disagreement without silently rewriting expectations.
6. Review artifacts/traceability, preserve defects and reruns, and package redacted records. Report per-run states and limitations before any synthesis.

Setup, familiarization, planning, AI execution, active human review, build/test time and recovery are separately recorded and included in appropriate totals. Predefine any excluded external wait and explain it. Counterbalance operator/method order and keep longitudinal evolution on a method's own implementation separate from matched episodes.

## Outcomes and reporting

Report CS acceptance as pass/fail/not-run with locators, elapsed and active-human effort under fixed boundaries, actual exposed usage, defects/repair, sampled traceability/drift and reproduction results. Reviewer judgments need anchored criteria and disclosed uncertainty. No aggregate score or significance claim is specified at M1.

Retain failed, aborted and missing-data runs. An exclusion requires a predeclared reason and a visible record; do not rerun silently to obtain success. A small synthetic solo case supports bounded observations, not causal superiority, organizational adoption, security assurance or production reliability.

Proposed artifact package, to be created only later: manifest, frozen brief/contract, source/seed/oracle references, generated artifacts/commits, event/usage records, actual check outputs, deviations and a reproduction guide. Public hosting, model purchases and release remain separately controlled by the author.
