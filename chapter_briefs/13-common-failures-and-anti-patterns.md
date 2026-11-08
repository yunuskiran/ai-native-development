# 13. Common Failures and Anti-Patterns

Status: **M1 ARCHITECTURE BRIEF — NOT MANUSCRIPT**. Author-supplied title/order preserved. Chapter ID: C13. Approved planning allocation: **3,500 words**. M1 architecture accepted by the author on 2026-10-31; factual support still requires M2 evidence gates.

## Reader question

How can engineers recognize and recover from recurring failures in AI-assisted process, context and verification?

## Reader outcomes

- Build a symptom-to-evidence-to-recovery diagnosis without treating every plausible cause as verified.
- Recognize process/context/verification failures across method boundaries.
- Preserve failed attempts and choose proportionate remediation with regression evidence.

## Scope and dependencies

Own diagnostic and recovery patterns. Exclude repeating C02's framing, C12's full checklists and unsupported claims that a named method uniquely causes a failure.

Prerequisites: C02 discipline, C09 evidence qualification, C11 actual records if available and C12 acceptance boundaries.

## Proposed abstract

This chapter will turn documented limitations and observed case problems into a diagnostic guide. It will organize failures by observable symptom, likely mechanism, detection evidence, recovery and recurrence prevention, keeping anecdotes and hypotheses distinct from established patterns. Examples will cover ambiguous intent, stale specifications, lost context, ceremony without useful decisions and circular validation. A small repair will keep recovery proportionate, while a serious tenant-boundary problem will show why narrow fixes still need meaningful evidence. The chapter will reference earlier foundations and checks instead of repeating them or assigning blame to a method's users.

## Planned sections

| Section ID | Section | Purpose / evidence-bearing example |
|---|---|---|
| C13-S01 | A diagnostic pattern with evidence labels | Define symptom, conditions, hypothesized cause, checks, recovery and prevention. |
| C13-S02 | Ambiguous intent and invisible decisions | Plan a bounded example where specification/decision correction precedes code changes. |
| C13-S03 | Stale artifacts and lost context | Inspect disagreement, handoff omissions and recovery across a session or policy change. |
| C13-S04 | Ceremony without useful decisions | Examine excessive artifacts and missing ownership without assuming less process is always better. |
| C13-S05 | Circular checks and false completion | Use independent counterexamples to distinguish success assertions from accepted behavior. |
| C13-S06 | Repair narrowly and retain the record | Plan small and boundary-critical repairs with logs, regression checks and failed attempts. |
| C13-S07 | Use failure to update process choices | Connect repeated evidence to profile changes, exit conditions and open research questions. |

## Artifacts and evidence needs

Failure-pattern cards with evidence type, conditions, diagnostic checks and recovery; no invented incident histories.

M2 must substantiate any claimed recurring pattern from primary first-hand reports; M4 may supply actual case failures. Hypothetical examples remain labeled. Do not manufacture failed runs to populate a narrative.

Source IDs refer to the [M0 source ledger](../research/SOURCE_LEDGER.md). They are research leads, not completed M2 dossiers. F01–F11 refer to the [comparison framework](../COMPARISON_FRAMEWORK.md). No benchmark outcomes or accepted implementation are implied.

## Handoffs and acceptance

C10's selection record gains update/exit triggers; C14 closes with uncertainties exposed by current evidence.

Brief acceptance: one distinct reader question, outcomes and exclusions; 7 planned sections; original example/artifact role; explicit evidence gaps; coherent handoffs and proposed budget. Chapter prose requires later authorization and source/technical review.

