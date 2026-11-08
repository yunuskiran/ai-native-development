# 8. Spec-Driven Development as an Approach

Status: **M1 ARCHITECTURE BRIEF — NOT MANUSCRIPT**. Author-supplied title/order preserved. Chapter ID: C08. Approved planning allocation: **4,500 words**. M1 architecture accepted by the author on 2026-10-31; factual support still requires M2 evidence gates.

## Reader question

What does it mean for specifications to guide development over time, and how can that policy cut across different methodologies?

## Reader outcomes

- Distinguish specification lifecycle patterns and attribute the analytical vocabulary.
- Separate a specification, general context, an executable contract and generated test code.
- Evaluate ownership, disagreement and change costs across the four selected profiles.

## Scope and dependencies

Own the full SDD lifecycle discussion and attribution. Exclude a fifth-method ranking, an entire requirements-writing manual and unsupported synchronization guarantees.

Prerequisites: C03 supplies the primer; C04–C07 provide qualified artifact examples. M2 must verify exact maintenance policies.

## Proposed abstract

This chapter will synthesize specification policies after readers have seen four concrete process frameworks. It will attribute and qualify the spec-first, spec-anchored and spec-as-source distinction, then examine who owns specifications, how disagreement is resolved and what makes an artifact mechanically checkable. The shared policy-change episode will expose retention, code-edit and reconciliation choices without assuming that any pattern is a maturity level or that generated code is deterministic. The chapter will connect specifications to acceptance evidence and maintenance costs while keeping SDD an approach rather than a fifth peer method.

## Planned sections

| Section ID | Section | Purpose / evidence-bearing example |
|---|---|---|
| C08-S01 | From the primer to a lifecycle policy | Revisit brief definitions and identify the ownership/retention questions that need deeper treatment. |
| C08-S02 | Three attributed patterns, not a ladder | Explain spec-first/anchored/as-source with caveats and source-specific meanings. |
| C08-S03 | Specifications, context and executable contracts | State what is behavior guidance, general memory and mechanically checked evidence. |
| C08-S04 | Who resolves disagreement | Plan examples where requirements, code and tests conflict; make decision rights explicit. |
| C08-S05 | One policy change across native artifacts | Trace the common E2 change using each selected profile without forcing one notation. |
| C08-S06 | Costs, drift and useful limits | Examine review/maintenance effort and where a persistent spec may or may not pay for itself. |
| C08-S07 | Apply the lens without creating a fifth arm | Hand off explicit policy questions to comparison and selection. |

## Artifacts and evidence needs

Original specification-lifecycle diagram and a policy-change trace across four native artifact sets.

M0 S13/C06 supports attribution within recorded scope; S09 provides AIUP self-description, not outcome validation. M2 must inspect retention, code-edit and reconciliation policies for each selected profile. Executability and drift prevention remain unverified until demonstrated.

Source IDs refer to the [M0 source ledger](../research/SOURCE_LEDGER.md). They are research leads, not completed M2 dossiers. F01–F11 refer to the [comparison framework](../COMPARISON_FRAMEWORK.md). No benchmark outcomes or accepted implementation are implied.

## Handoffs and acceptance

C09 includes the SDD lens in comparison; C10 uses it as a project constraint; C11 supplies the detailed change record.

Brief acceptance: one distinct reader question, outcomes and exclusions; 7 planned sections; original example/artifact role; explicit evidence gaps; coherent handoffs and proposed budget. Chapter prose requires later authorization and source/technical review.

