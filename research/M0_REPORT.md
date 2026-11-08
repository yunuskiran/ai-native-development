# M0 foundation report — Engineering with AI: Beyond Vibe Coding

Review date: **2026-10-31 (Australia/Melbourne)**.

**Historical milestone record:** after this M0 handoff and outline review, the author explicitly authorized M1 and selected TypeScript / Node.js. The stopping status and missing-input observations below record the M0 stage, not the current work state. See the [M1 report](M1_REPORT.md) for current deliverables and remaining decisions.

**Status: STOP — AWAIT AUTHOR REVIEW.** M0 research package prepared within the available inputs, updated after the author supplied fourteen chapter titles/order during review. That structure is now recorded in [OUTLINE.md](../OUTLINE.md) and reviewed in the [outline critique](OUTLINE_PATCH_PROPOSAL.md). The initial twelve-slot alternative is superseded. The author review gate has not passed; M1 has not started and no book chapters were written. The actual case specification remains unavailable.

## Findings

1. The checkout initially contained only `docs/BOOK_MASTER_PLAN.md` outside Git metadata. Its scope is coherent and evidence-conscious, but most of the operating documents it references are absent. No conflicting author versions were available to reconcile; the conflict is between the assumed document set and this checkout.
2. **Four frameworks plus cross-cutting SDD** is a defensible editorial taxonomy. It should not become five equivalent methods or trial arms. Toolkits may contain process guidance; their exclusion from main chapters is an explicit scope choice. See [terminology](TERMINOLOGY.md) and ledger [C01/C08](SOURCE_LEDGER.md#claim-register).
3. Version and identity must be part of the comparison unit. BMad's stable/preview lines, GSD's framework/product distinction and migration notices, AWS concept/implementation phase descriptions, and AIUP's core/plugin boundary all require explicit qualification. See [sources S01–S10](SOURCE_LEDGER.md).
4. Independence from the AIUP/Apress book requires more than a new title. The proposed contribution is conditional cross-method choice using original requirements, equally applied comparison questions and inspectable evidence. Public-scope review does not certify full-text originality. Adjacent publisher titles also use “Beyond Vibe Coding”; the requested working title is preserved. See [positioning](COMPETITOR_POSITIONING.md), sources S11–S12/S17–S19 and decision D12.
5. The B2B SaaS case is feasible in principle as a bounded walkthrough, but it is **not ready for experiments**. The [readiness assessment](EXPERIMENT_READINESS.md) proposes shared requirements, three episodes, independent acceptance evidence, controls and a qualitative fallback. No empirical outcomes, scores or method rankings exist.
6. The author-supplied fourteen-chapter sequence is workable without renaming or reordering chapters. The M0 review now identifies scope boundaries among chapters 1–3, SDD prerequisites before chapter 8, comparison vs selection in 9–10, case introduction before the full chapter 11, and quality throughout before chapter 12. Optional scope notes remain a separate, unapplied proposal.

## Requested reading and file inventory

The requested order was honored for available material: checked for `AGENTS.md`, read the master plan, then checked the remaining requested inputs in order. Repository-wide file enumeration and ancestor guidance checks found no `AGENTS.md`. Missing inputs were not fabricated or described as read.

| Requested order | Input | Intake finding / consequence |
|---|---|---|
| 1 | `AGENTS.md` | Missing; no additional repository guidance available. |
| 2 | `BOOK_MASTER_PLAN.md` | Found at `docs/BOOK_MASTER_PLAN.md`; read in full, version 0.1 dated 2026-10-30. Preserved. |
| 3 | `BOOK_BRIEF.md` | Missing; audience, length and detailed promise require author decisions. |
| 4 | `OUTLINE.md` | Missing; actual chapter overlap/flow cannot be reviewed. |
| 5 | `RESEARCH_PROTOCOL.md` | Missing; M0 uses explicit provisional evidence rules in the ledger. |
| 6 | `COMPARISON_FRAMEWORK.md` | Missing; master's dimensions retained, no scores inferred. |
| 7 | `CASE_STUDY_SPEC.md` | Missing; domain/stack/acceptance details not frozen. |
| 8 | `QUALITY_GATES.md` | Missing; master milestone gates remain the available policy. |
| 9 | `SOURCES.md` | Missing; cannot audit the author's intended bibliography or all its claims. |
| 10a | `ROADMAP.md` | Missing; master M0–M7 sequence is the available roadmap. |
| 10b | `TASKS.md` | Missing at intake; created for this run and kept current. |

Author review follow-up: `OUTLINE.md` is now supplied through the chat and recorded verbatim. Its structural M0 review is complete. With `TASKS.md` also created, eight requested inputs remain absent; the table above preserves the intake inventory.

`templates/METHOD_SCORECARD.md`, referenced by the master, was also absent. No source application, tests, manuscript, experimental logs or existing research directory was present. The local branch had no commits or tracked files; the master was already untracked. No branch, commit, checkout replacement or Git-history mutation was performed.

Original master SHA-256 at intake and preservation check:

`cf8d65f94375f59e246ea855587588b988ab4f1c04e09dc15d85e6372ac06cc6`

## Sources inspected and limits

The [source ledger](SOURCE_LEDGER.md) has **19 source records**, with direct URLs, inspected scope, date/version information, supportable claims, rights cautions and confidence limits. Records may contain multiple related files; 19 is not a count of independent studies.

| Record group | Inspected material | Evidentiary boundary |
|---|---|---|
| S01–S02 | BMad READMEs, stable manifest, commit metadata | Stable `6.12.4` source candidate vs main preview; no registry/runtime validation. |
| S03–S06 | GSD migration notices, Core README/manifest/phase-loop sections, Pi overview | Framework and coding-agent product distinguished; full provenance unresolved. |
| S07–S08 | AWS introduction and pinned Workflows README/profile sections | Original lifecycle vs current implementation; no efficacy inference. |
| S09–S10 | AIUP methodology and pinned marketplace/workflow sections | Documented artifact lifecycle and plugin boundary; no compatibility guarantee. |
| S11–S12 | Apress public metadata/contents and AIUP publications page | Existing book's advertised scope; full text uninspected. |
| S13 | Böckeler's first-hand SDD analysis | Attributed terminology, not an industry standard or current tool assessment. |
| S14–S16 | Spec Kit/OpenSpec introductory README sections and Kiro specs docs | Implementation/process context, not extra peer chapters. |
| S17 | Comparative preprint abstract and submission record | Prior-work lead only; full paper and rubric unreviewed. |
| S18–S19 | O'Reilly and Pragmatic publisher catalog pages | Adjacent scope/title wording; no full-book judgment or title-rights conclusion. |

Online browsing and read-only GitHub access were available. Failed tag-list requests, a failed extensionless AIUP URL and a publisher redirect with no readable lines are recorded with successful alternatives where available. No claim relies on pretending those failed requests succeeded. No credentials were requested, paid access acquired, external services changed, or full external books/sites copied.

## Conflicts, assumptions and evidence gaps

| Issue | M0 handling | What remains |
|---|---|---|
| Master references absent documents and templates | Preserved originals; proposals have separate names and statuses | Restore authoritative originals or authorize reconstruction (D01/D11). |
| “Five methods” vs four methods plus SDD | Recommended the master's distinction | Author taxonomy approval (D04); no empirical classification implied. |
| GSD old name/location vs Core/Pi continuations | Followed primary notices and read destinations; did not substitute silently | Author's intended framework snapshot (D02). |
| BMad source-line labels vs dated ETA, and README highlight vs GSD manifest | Prefer exact source identities; record stale indicators | Validate package/release provenance and choose snapshots (D03). |
| AWS phase count and ceremony depend on concept/profile/version | Documented mapping need; setup-stage counting convention noted | Detailed mapping and selected profile enforcement review (R03). |
| Master's ASP.NET caution vs no chosen stack | Did not infer .NET requirement | Author domain/stack decision and compatibility work (D06/R04). |
| Matched requirements vs method-specific artifacts | Proposed common acceptance outcomes with native artifacts retained | Protocol, baseline, oracle, resources and actual runs (D07/R08). |
| Performance and suitability assertions | Retained as attributed claims or **Not assessed** | Independent outcome evidence and/or transparent executed trials (U01). |
| Independence and title differentiation | Public-scope competitor review, original case candidate, unchanged working title | Full-text originality, permissions and packaging decisions (D10/D12). |

Origin histories, precise acronym expansions, legal reuse permissions, shared-host compatibility, field effectiveness and the missing bibliography's claims remain **NOT VERIFIED IN THIS SESSION**. The complete [open-question register](OPEN_QUESTIONS.md) separates author decisions D01–D12 from research tasks R01–R10. These gaps are explicit limitations, not adverse findings about the methods.

## Outline and case-study disposition

The [outline review](OUTLINE_PATCH_PROPOSAL.md) now critiques all fourteen author-supplied chapters for overlap, narrative, practicality, balance and independence. The supplied titles/order are preserved in [OUTLINE.md](../OUTLINE.md). The initial twelve-slot add-file patch is **SUPERSEDED — DO NOT APPLY**, retained only for provenance. The current [scope-notes patch](proposals/OUTLINE_14_SCOPE_NOTES.patch) proposes brief boundaries without changing any title or order; it remains unapplied. This resolves the missing-outline structural review, not the wider M0 gate or future chapter fact-checking.

The case-study notes propose synthetic tenant-scoped vendor-access approvals as an option, not an adopted domain change. Thirteen readiness conditions remain unchecked. They cover scope, frozen requirements, baselines, independent oracle, versioned profiles, compatibility, authorized resources, operators/reviewers, instrumentation, analysis, local scope, reproduction and approval. A local solo demo cannot substantiate team or production claims. The experiment design contains planning arithmetic only; no benchmarks were invented or simulated.

## Files created or edited

The initial eleven deliverables below were new files at M0 intake. During author review, `OUTLINE.md` and a scope-notes patch were added, and the affected M0 documents/task register were updated. The pre-existing master plan remains unchanged; no author material was moved or deleted.

| File | Purpose |
|---|---|
| [SOURCE_LEDGER.md](SOURCE_LEDGER.md) | Primary-source audit, claim register and validation backlog. |
| [TERMINOLOGY.md](TERMINOLOGY.md) | Taxonomy, naming cautions and proposed glossary conventions. |
| [OPEN_QUESTIONS.md](OPEN_QUESTIONS.md) | Author choices, research backlog and working assumptions. |
| [COMPETITOR_POSITIONING.md](COMPETITOR_POSITIONING.md) | Public-scope independence and market-positioning analysis. |
| [M0_REPORT.md](M0_REPORT.md) | This review package and stopping status. |
| [OUTLINE_PATCH_PROPOSAL.md](OUTLINE_PATCH_PROPOSAL.md) | Critique, candidate narrative and adoption conditions. |
| [OUTLINE_M0_CANDIDATE.patch](proposals/OUTLINE_M0_CANDIDATE.patch) | Superseded twelve-slot proposal, historical only; do not apply. |
| [EXPERIMENT_READINESS.md](EXPERIMENT_READINESS.md) | Feasibility, proposed episodes/controls and readiness checklist. |
| [M1_WORK_PLAN.md](M1_WORK_PLAN.md) | Small architecture tasks with dependencies and acceptance criteria. |
| [DECISION_LOG.md](DECISION_LOG.md) | Authorized scope vs provisional recommendations. |
| [TASKS.md](../TASKS.md) | Execution record; author approvals and blocked-input reviews left open. |
| [OUTLINE.md](../OUTLINE.md) | Author-supplied fourteen titles/order, preserved verbatim during review. |
| [OUTLINE_14_SCOPE_NOTES.patch](proposals/OUTLINE_14_SCOPE_NOTES.patch) | Current optional scope-note addition; unapplied, with titles/order unchanged. |

## Proposed M1 work and author review

The [M1 plan](M1_WORK_PLAN.md) proposes seventeen task rows: establish authoritative inputs/layout; reconcile the brief and research protocol; define the comparison framework and blank scorecard; specify the case and future run protocol; refine boundaries within the supplied fourteen-chapter outline; prepare abstract/brief batches, split into one-chapter tasks where needed; set style, word budgets and cross-references; reconcile gates/source index/roadmap; then obtain author architecture sign-off. Every task has explicit acceptance criteria. None was executed as M1 work.

For the M0 gate the author must decide:

1. Restore the eight requested inputs still missing, or explicitly authorize proposed replacements and a canonical file layout. The supplied outline and created task register are already recorded.
2. Confirm four frameworks plus SDD, GSD lineage and stable/current version policy, including the AWS mapping.
3. Set primary audience, length/depth and disposition of the optional scope notes. The author's fourteen titles/order are the structural reference; no chapter-count change is proposed.
4. Choose case domain/stack, evidence tier and resource ceilings; retain the walkthrough fallback if controls fail.
5. Record independent review/full-text access plans and title-positioning follow-up, without claiming those reviews already happened.
6. Approve, amend or reject this M0 package and explicitly authorize M1 if ready.

These are the user-requested review decisions and the master plan's M0 gate, not an additional approval flow imposed by this run.

## Local verification

- Required M0 outputs and task register checked for presence and mutually consistent scope/status.
- Relative local Markdown links and heading anchors checked. The initial twelve-slot patch passed `git apply --check` when the outline was absent; it is now superseded and must not be applied. The current scope-notes patch passes its own applicability check and remains unapplied.
- Original master hash matches intake. The fourteen author-supplied titles/order were checked against `OUTLINE.md`; no case implementation or manuscript was created.
- Source and rights limitations remain visible. Outline structural review is now complete; case-spec review, approvals, experiments and later milestones remain unchecked. No new external research was performed during this outline follow-up.

This is documentation verification, not application testing or experimental evidence. It does not validate full external books or all outbound links within source material.

**STOP — AWAIT AUTHOR REVIEW.**
