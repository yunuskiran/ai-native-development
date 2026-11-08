# M1 architecture report — Engineering with AI: Beyond Vibe Coding

Date: **2026-10-31 (Australia/Melbourne)**. Status: **M1 ARCHITECTURE ACCEPTED BY THE AUTHOR**, decision A06. The author approved the presented package after reviewing its handoff. The delivery details below retain the distinction between planning and execution. This is not M2 research completion, a manuscript, an executed case or experiment evidence.

Approval scope: the audience, word budget, chapter boundaries and vendor-access approval case are accepted as architecture. Exact runtime/framework/database/host/model versions, source validation, technical case readiness and later milestone gates remain open. The [M2 work plan](M2_WORK_PLAN.md) describes the next evidence phase.

## Outcome and authority

All fourteen author-supplied chapter titles and their order are preserved in [OUTLINE.md](../OUTLINE.md). Each now has an original architecture brief with one reader question, outcomes, exclusions, dependencies, abstract, 5–8 planned sections, artifact/evidence needs and handoffs. The briefs are planning documents, not chapter prose.

The proposed allocation is **66,500 words of main text**, plus 3,500 for appendices and 2,000 for front/back matter: **72,000 planned words**, excluding bibliography/index and runnable companion code. The four method chapters each receive 5,500 words; the full common case receives 8,000. These are editorial proposals requiring author review, not actual manuscript counts or a print-page estimate.

The case language/runtime family is **author-selected TypeScript / Node.js**. The synthetic tenant-scoped vendor-access approval domain and its behavioral requirements are now a concrete proposal, not an accepted domain change or frozen experiment baseline. Web/UI framework, database, exact versions, selected host/model and method adapters remain unselected pending evidence/compatibility review.

## Architecture and repetition controls

- Chapters 1–3 own history, proportionate engineering discipline, and method/tool/evidence vocabulary respectively.
- Chapter 3 supplies brief SDD and common-case prerequisites; chapter 8 owns full SDD lifecycle analysis, and chapter 11 owns the complete case.
- Chapters 4–7 ask the same comparison questions while keeping native artifacts and distinctive explanations. No product is added as a fifth peer method.
- Chapter 9 owns evidence-qualified comparison; chapter 10 owns conditional project selection, adoption and exit decisions.
- Testing and security apply from the first example. Chapter 12 consolidates their evidence and operational boundaries; chapter 13 adds diagnosis/recovery.
- Chapter 14 labels future scenarios and their assumptions. No forecast is a present capability assertion.

The [cross-reference map](CROSS_REFERENCE_MAP.md) makes each concept's home and prerequisite/depth references explicit. The [diagram plan](DIAGRAM_PLAN.md) specifies original assets, evidence and accessibility needs without copying outside artwork. The earlier twelve-slot outline patch remains superseded; the optional fourteen-chapter scope-notes patch remains unapplied. M1 boundaries are separate review artifacts, not a silent edit of the author's outline.

## Deliverables and execution record

Thirty files were added during M1 preparation: eight root planning/navigation documents, the scorecard template, fourteen chapter briefs, and seven research/editorial files including this report and the machine-readable plan. Eight existing M0/outline/task records were updated for current authority and carry-forward status. The original master plan was preserved.

| Work | Concrete output / acceptance evidence | Disposition |
|---|---|---|
| M1-01 Authority/layout | [Decision log](DECISION_LOG.md); root planning drafts, `research/`, `chapter_briefs/`, `templates/`; original master remains under `docs/` | Prepared under author authorization; no synthetic `AGENTS.md` or claimed recovered originals. |
| M1-02 Reader brief | [BOOK_BRIEF.md](../BOOK_BRIEF.md) | Promise, proposed primary audience, prerequisites, scope and explicit non-goals. |
| M1-03 Research protocol | [RESEARCH_PROTOCOL.md](../RESEARCH_PROTOCOL.md) | Claim types/states, locators, independence, snapshots, update/rights rules and dossier criteria. |
| M1-04/05 Comparison instrument | [COMPARISON_FRAMEWORK.md](../COMPARISON_FRAMEWORK.md), [blank scorecard](../templates/METHOD_SCORECARD.md) | F01–F11 retained; required/optional/host boundaries, evidence needs and Not assessed rules; no filled rankings. |
| M1-06 Proposed common case | [CASE_STUDY_SPEC.md](../CASE_STUDY_SPEC.md) | Actors, non-goals, TypeScript/Node constraint, fifteen CS requirements, E1/E2/E3 inputs and open interface/policy decisions. All acceptance checks Not run. |
| M1-07 Future run outline | [RUN_PROTOCOL.md](RUN_PROTOCOL.md) | ER01–ER13 roles/milestones/evidence, manifests, controls, failure/missing-data treatment and walkthrough fallback. Readiness is not passed. |
| M1-08 Scope boundaries | [Cross-reference map](CROSS_REFERENCE_MAP.md) and existing [outline critique](OUTLINE_PATCH_PROPOSAL.md) | Supplied titles/order preserved; early prerequisites and later deep treatment separated. |
| M1-09 Chapter briefs | All fourteen briefs linked in [WORD_BUDGET.md](WORD_BUDGET.md) and [CHAPTER_PLAN.json](CHAPTER_PLAN.json) | Questions, outcomes, exclusions, abstracts, 5–8 sections, sources/gaps and handoffs. Chapters 8–14 tracked individually. |
| M1-10 Style | [STYLE_GUIDE.md](STYLE_GUIDE.md), [terminology](TERMINOLOGY.md) | Proposed consistent US English, attribution/uncertainty, names, code/figure labels and repetition rules. Glossary/source facts still require review. |
| M1-11 Budget/maps | [WORD_BUDGET.md](WORD_BUDGET.md), [CROSS_REFERENCE_MAP.md](CROSS_REFERENCE_MAP.md), [DIAGRAM_PLAN.md](DIAGRAM_PLAN.md) | Allocations, concept owners, valid section targets and evidence-based asset requirements. |
| M1-12 Gates | [QUALITY_GATES.md](../QUALITY_GATES.md) | G0–G7 evidence and approvers; independent human review distinguished from AI passes. |
| M1-13 Index/status | [SOURCES.md](../SOURCES.md), [ROADMAP.md](../ROADMAP.md), [TASKS.md](../TASKS.md), [README.md](../README.md) | Existing source scope retained, next research assigned, no premature milestone approvals. |
| M1-14 Review package | This report and document integrity checks | Prepared, then accepted by the author in A06. Source/technical gates remain separate. |

Updated existing files: `OUTLINE.md`, `TASKS.md`, `research/DECISION_LOG.md`, `research/OPEN_QUESTIONS.md`, `research/SOURCE_LEDGER.md`, `research/EXPERIMENT_READINESS.md`, `research/M0_REPORT.md`, `research/M1_WORK_PLAN.md`. The M0 report now identifies itself as a historical handoff record rather than current blocking instructions.

## Sources, results and limits

M1 reused the M0 ledger's **19 records within their recorded inspection limits**. No new online verification was performed, and no current-release/runtime/compatibility claims were added. The [sources index](../SOURCES.md) assigns future dossier work without treating planned sources as inspected citations. No whole external book/site, prompt collection or artwork was copied.

No actual application, test oracle, model run, benchmark, paid service, deployment or publication was produced. The case's fifteen acceptance rows are definitions, not passing tests. Comparison outcomes remain Not assessed. All thirteen experiment readiness conditions remain unpassed, even where a draft document now exists.

Key evidence risks remain GSD lineage choice, stable/preview and concept/profile distinctions, TypeScript/Node adapter compatibility, missing independent outcome evidence, permissions/full-text originality and review resources. Future facts and implementation guidance must be verified against primary evidence in M2 before code/prose rely on them.

## M1 acceptance record

1. **Audience and depth accepted:** practicing software engineers, tech leads and architects with ordinary Git/testing/application experience.
2. **Length and boundaries accepted:** 66,500-word main-text target and chapter ownership, with the fourteen titles/order preserved.
3. **Specific SaaS design accepted:** synthetic vendor-access approvals and the M1 policy design, using TypeScript / Node.js. Exact stack and technical case validation remain later work.
4. **Evidence approach accepted for planning:** common instrument and honest walkthrough fallback. Exact method/profile/version, reviewer and run-budget decisions retain their later gates.

Disposition: the author has accepted these M1 architecture choices in A06. The complete [decision register](OPEN_QUESTIONS.md) retains later implementation/research choices and dependencies. Approval does not convert source leads into validated claims or authorize experiments/publication.

## Verification record

Document integrity checks passed: fourteen exact author titles/order, fourteen consistent briefs with **95 planned sections**, matching manifest/budget allocations (66,500 / 72,000 words), F01–F11 framework/template coverage, fifteen CS definitions and thirteen readiness conditions still unchecked. Local Markdown links/anchors and code fences passed validation across 41 Markdown files. The current scope-notes patch passes `git apply --check` and remains unapplied.

Original master SHA-256 remains `cf8d65f94375f59e246ea855587588b988ab4f1c04e09dc15d85e6372ac06cc6`. There are 44 files outside Git metadata after this work: the fourteen-file M0/outline starting set plus thirty new M1 files. No Git history or original master was modified.

These checks verify architecture consistency only. They are not application tests, source fact-checking, independent technical review or experiment evidence.

**M1 AUTHOR REVIEW GATE PASSED. NEXT: M2 EVIDENCE BASE.**
