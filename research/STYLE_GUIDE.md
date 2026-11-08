# Editorial style guide

Status: **M1 draft for author review**, 2026-10-31. Book prose is English; project discussion may remain Turkish. Proposed English convention: consistent US spelling in original prose, preserving original names, titles and quotations. This is an editorial default, not an inferred author preference.

## Voice and argument

Write for developers who already understand ordinary engineering work. Lead with the decision or reader problem, explain the mechanism, then show evidence and limits. Favor concrete examples, short clear paragraphs and precise verbs. Avoid promotional language, universal maturity ladders and treating named methods as personalities. Critique a documented mechanism or observed failure rather than a community or its users.

The book's thesis remains testable. Let a small repair justify lightweight process where the evidence supports it. Distinguish descriptive process guidance from normative recommendations, and show the cost of adoption, review and maintenance as well as possible benefits.

## Names and taxonomy

Preserve all fourteen chapter titles and their order in [OUTLINE.md](../OUTLINE.md), including punctuation. Use BMAD Method in book-level headings; record the source's BMad styling when needed in version notes. Keep the GSD chapter title unchanged; name the chosen lineage/profile in the text rather than silently substituting a product. AWS AI-DLC may retain a source's “Life Cycle” wording in titles. Expand AI Unified Process (AIUP) and Spec-Driven Development (SDD) on first use.

Four frameworks are peer coverage. SDD has a full chapter and applies across them. IDEs, coding agents and process-bearing toolkits are implementation context under the author's scope. Refer to the [terminology file](TERMINOLOGY.md) for proposed operational definitions; do not invent acronym expansions or histories.

## Attribution and uncertainty

| Situation | Wording policy |
|---|---|
| Primary documentation only | “The selected profile prescribes/describes…” with source/version; no inference of runtime enforcement. |
| Maintainer/vendor outcome | “The maintainer reports/claims…” plus conditions; no unattributed multiplier or assurance. |
| Executed observation | State task, versions, operator, budget, outcome and limitations with run locator. |
| Editorial judgment | Identify premises and scenario: “For these constraints, we would…”; no universal winner. |
| Incomplete evidence | Say pending verification or Not assessed; do not assign zero or assert absence. |
| Future discussion | Label forecast/scenario/hypothesis and date any current-state premise. |

Source IDs and claim IDs are working manuscript references, not final bibliography formatting. Cite primary URLs/passages in research records and convert consistently in production. Keep source/quote limits and permissions in the evidence record. No external prompts or figures are copied merely because a repository is public.

## Examples, code and diagrams

Use synthetic tenants, people and vendors. TypeScript / Node.js is the selected example family; exact versions and libraries await compatibility review. Show just enough code to explain a decision. Every future runnable snippet must identify a tested commit, commands and expected interpretation; illustrative fragments must be visibly labeled and cannot count as executable evidence.

Use stable requirement IDs (`CS-01` etc.), chapter/section IDs (`C03-S02` etc.) and future run IDs. Do not pretend artifacts generated from a hypothetical example were produced in an actual run. A drawn workflow is a model; measured events require logs.

All figures must be original or explicitly cleared, with purpose, caption, source/derivation, text alternative and editable source. Avoid color-only distinctions and unreadable code/labels. Method figures preserve native vocabulary but supply a common legend. Do not use a radar chart without valid dimensions and evidence-backed values.

## Chapter pattern and repetition controls

Each chapter brief contains one question, outcomes, scope/dependencies, abstract, 5–8 planned sections, evidence needs and handoffs. Method chapters answer common comparison questions but use distinctive explanations and native artifacts. Do not paste the same introduction or artifact tutorial four times.

Concepts have one primary home in the [cross-reference map](CROSS_REFERENCE_MAP.md). Earlier chapters may give short prerequisite definitions and point to the deeper treatment. Chapter 9 compares evidence; chapter 10 guides selection; chapter 11 owns the full case; chapter 12 consolidates verification obligations already applied throughout. Chapter 13 diagnoses and repairs failures rather than repeat a security checklist.

## Word counting and review

The [word budget](WORD_BUDGET.md) is an allocation proposal, not current manuscript length. Count original prose, list/table text and captions; report code and bibliography/index separately. Chapter briefs are not manuscript and do not consume drafted chapter allocations. Production page counts depend on format and remain unestimated.

Before chapter acceptance: substantive edit, source fact-check, technical validation of runnable material, citation/permissions audit and copyedit under [QUALITY_GATES.md](../QUALITY_GATES.md). AI editorial passes are identified as such and never substituted for independent human review.
