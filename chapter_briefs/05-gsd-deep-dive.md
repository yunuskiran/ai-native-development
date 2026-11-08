# 5. GSD — Deep Dive

Status: **M1 ARCHITECTURE BRIEF — NOT MANUSCRIPT**. Author-supplied title/order preserved. Chapter ID: C05. Approved planning allocation: **5,500 words**. M1 architecture accepted by the author on 2026-10-31; factual support still requires M2 evidence gates.

## Reader question

How does the selected GSD framework lineage organize bounded work and persistent context, and what must people verify?

## Reader outcomes

- Distinguish framework lineage from a similarly named coding-agent product.
- Inspect persistent context and handoffs rather than assume context management prevents errors.
- Assess recovery, tiny-change overhead and acceptance under a specified profile.

## Scope and dependencies

Own the chosen GSD framework profile and context/artifact mechanisms. Exclude product comparisons, a universal context-window guarantee and silent adoption of Core as the author's historical target.

Prerequisites: C03; D02 lineage disposition and M2 provenance/profile dossier before factual drafting.

## Proposed abstract

This chapter will make the GSD lineage decision visible while preserving the author's chapter title. It will distinguish the framework process from a standalone coding-agent product, then follow a selected profile's discussion, planning, execution and verification records for the common increment. Particular attention will go to context transfer, worker boundaries and recovery after a session reset. A bounded repair will test the cost of applying the full loop. Context-window and reliability statements will remain attributed claims until supported by actual evidence, with all host/model and version dependencies disclosed.

## Planned sections

| Section ID | Section | Purpose / evidence-bearing example |
|---|---|---|
| C05-S01 | Name the lineage and snapshot | Resolve historical GSD versus Core for this edition and record product exclusions. |
| C05-S02 | Discuss decisions before decomposition | Trace implementation questions and the human record for the shared increment. |
| C05-S03 | Plan bounded work with persistent state | Examine native plans, dependencies and continuity across sessions. |
| C05-S04 | Execute with explicit context boundaries | Record worker inputs, orchestration and host/model-dependent assumptions. |
| C05-S05 | Verify, recover and close the work | Separate generated verification from independent acceptance and preserve failures. |
| C05-S06 | Small repairs and policy changes | Examine a reduced loop and existing-code episode without copying another method's artifacts. |
| C05-S07 | Limits and conditional fit | Apply F01–F11 and distinguish context design claims from observed outcomes. |

## Artifacts and evidence needs

Versioned framework lineage note, context-handoff map and native phase artifact trail.

M0 S03–S06/C03 establish inspected notices and descriptions only. D02 remains open; M2 must resolve provenance/profile and M4 must validate actual orchestration and compatibility. Fixed context-size and reliability assertions are unmeasured claims.

Source IDs refer to the [M0 source ledger](../research/SOURCE_LEDGER.md). They are research leads, not completed M2 dossiers. F01–F11 refer to the [comparison framework](../COMPARISON_FRAMEWORK.md). No benchmark outcomes or accepted implementation are implied.

## Handoffs and acceptance

C08 examines retained specifications; C09 compares evidence; C13 covers diagnosis/recovery patterns.

Brief acceptance: one distinct reader question, outcomes and exclusions; 7 planned sections; original example/artifact role; explicit evidence gaps; coherent handoffs and proposed budget. Chapter prose requires later authorization and source/technical review.

