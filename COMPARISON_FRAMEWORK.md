# Comparison framework

Status: **M1 instrument draft**, 2026-10-31. No method scores or effectiveness findings are filled. Use with the [blank scorecard](templates/METHOD_SCORECARD.md), [research protocol](RESEARCH_PROTOCOL.md) and [case specification](CASE_STUDY_SPEC.md).

## Unit, scope and reporting policy

Compare BMAD Method, the selected GSD framework lineage, AWS AI-DLC and AIUP through named source snapshots and implementation profiles. Treat SDD as an artifact-lifecycle lens across all four. Record host, model, add-ons, settings, task size, operator background and operating conditions. Do not attribute a host's feature, optional module or stack adapter to the core method without qualification.

Classify each observation as documented design, source-reported outcome, field observation, controlled observation or editorial analysis. Keep feature availability, evidence strength and suitability separate. Default an unanswered dimension to **Not assessed**. The M0 source candidates are not adopted run versions.

## Dimensions and observable questions

| ID | Dimension | Questions / inspectable evidence | Outcome evidence required before claiming effectiveness |
|---|---|---|---|
| F01 | Decision rights | Who proposes, approves, changes scope and can stop work? Are gates advisory, prompted or mechanically enforced? Inspect workflow rules and decision records. | Actual gate events, bypass behavior, operator interventions and deviations. |
| F02 | Planning overhead and scale | What is required for tiny repairs, features and uncertain initiatives? Separate required steps from optional depth. | Setup, planning/review and active-human time under matched scopes; later rework also reported. |
| F03 | Artifact lifecycle | What is created, owned, retained, retired and reconciled? What happens on disagreement? | Artifact changes through E2, detected contradictions and human repair effort. |
| F04 | Requirements traceability | How do requirement IDs reach plans, code, tests and review? Is presence checked separately from correctness? | Independent sample of valid/missing/incorrect links, not a generated coverage assertion alone. |
| F05 | Context management | What is loaded, persisted, reset and passed to workers? Are limits host-dependent? | Recorded context inputs, omissions, recovery and errors; no fixed-window performance guarantee. |
| F06 | Solo/team operation | Who performs business, architecture, implementation and review duties? How are handoffs and conflicting decisions handled? | Observed operators/teams and their constraints. Solo simulation cannot establish organizational benefit. |
| F07 | Brownfield suitability | How is existing behavior discovered and accepted as a baseline? How are change scope and legacy constraints preserved? | Matched E2/E3 baselines, regression evidence and inspection of unintended changes. |
| F08 | Testing and acceptance | Which tests and acceptance reviews are prescribed; who owns the oracle? How are failures and disagreement resolved? | Independent frozen checks, actual build/test outputs and retained failures. |
| F09 | Deployment governance and operations | What approvals, evidence, observability, rollback and maintenance are in scope? Distinguish a local exercise from production operation. | Actual environment/operational records; local plans alone support a documented-design conclusion only. |
| F10 | Portability and dependencies | Which parts require a host, provider, plugin, stack or service? Can artifacts survive migration? | A defined migration/smoke exercise, actual constraints and workarounds, with changes disclosed. |
| F11 | Maintainability | Who maintains specs, code and generated assets after a change? How are drift and upgrades handled? | E2/E3 changes and follow-up evidence; one successful build does not establish long-term maintainability. |

## Cross-cutting SDD lens

Ask whether specifications precede implementation, persist through maintenance and govern changes, and whether humans may edit code directly. Attribute spec-first, spec-anchored and spec-as-source terminology through [ledger S13](research/SOURCE_LEDGER.md#s13--sdd-terminology-birgitta-böckelers-first-hand-analysis). These are patterns, not ordinal maturity scores. Record spec ownership, conflict policy and validation; “source of truth” alone is insufficient evidence.

## Qualitative coding and limits

For a mechanism use **documented core**, **documented optional**, **documented external dependency**, **not found in inspected scope**, or **not assessed**, with source/profile qualifiers. For observed behavior use a dated observation and its conditions. Only use “absent” after a defined exhaustive check of the selected scope; explain that check.

For case acceptance, report requirement-level pass/fail/not-run with actual evidence. Neither those states nor documentation categories are converted into an aggregate ranking. A future numeric rubric requires observable anchors, reviewer calibration, missing-data rules and an approved analysis plan before data collection. No intuition-based radar chart or weighted total is permitted.

The method chapters share the same questions but use native artifacts and distinctive explanation. Chapter 9 owns evidence comparison; chapter 10 owns conditional selection. A selection record states scenario, non-negotiable constraints, candidate profiles, evidence/uncertainty, tradeoffs, adoption cost, a reversible pilot and exit conditions. It is advice for those conditions, not a universal winner.

## Instrument acceptance

Every F01–F11 row must be addressable in each dossier with a passage/record or a gap. Preserve conflicting evidence, failures and exceptions. A reviewer must be able to distinguish required process from optional tooling and assess the same bounded work without assuming all phases or artifact counts are equivalent. Current fulfillment: **documentary evidence mapped in [COMPARISON_EVIDENCE.md](research/COMPARISON_EVIDENCE.md); independent review and runtime/effectiveness assessment remain pending**.
