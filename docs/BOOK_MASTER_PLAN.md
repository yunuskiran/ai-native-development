# Book Master Plan — from research to publication

**Document status:** Proposed operating plan; human approval required before production milestones.  
**Version:** 0.1 / 2026-10-30.

## 1. Mission

Create an original, independent English technical book that compares modern AI-driven software development methodologies, distinguishes them from tooling, illustrates them through a common case study, and gives readers a reproducible decision-making system. Do **not** endorse a method by default or generate a one-shot generic manuscript.

The purpose is not to rank GitHub stars or showcase the latest prompt commands. It is to answer: **How should engineering teams structure decisions, artifacts, implementation, quality and governance when AI participates throughout the lifecycle?**

## 2. Editorial thesis

The engineering bottleneck shifts from typing code toward making decisions explicit, managing context, constraining changes, evaluating outputs, and operating software responsibly. Different methods address those needs with different amounts of ceremony, actor coordination and specification formality. The best method depends on project conditions, not its popularity.

Treat this thesis as an argument to test, not a proven universal law. Present counterexamples, such as tiny fixes where full planning creates needless overhead.

## 3. Coverage map

### Primary named methodologies/frameworks
- BMAD Method.
- GSD (Get Shit Done): framework/process layer, distinct from standalone GSD coding-agent product.
- AWS AI-Driven Development Lifecycle (AI-DLC).
- AI Unified Process (AIUP).

### Cross-cutting idea
- Spec-Driven Development (SDD): what specifications mean, how they persist, and the difference between spec-first / spec-anchored / spec-as-source patterns where substantiated.

### Context, not peers
- GitHub Spec Kit, OpenSpec, Kiro, Task Master AI, Agent Skills, various coding agents. Mention only when illuminating method implementation and label appropriately.
- Existing software engineering practices: Agile, TDD, BDD, DDD, architecture decision records, CI/CD and threat modeling as comparators or foundations, not inventions of AI methods.

### Coverage-change policy
If another meaningful new method emerges during research, propose it to the author with evidence of its distinctive process, source maturity and relevance before adding a main chapter. Do not silently bloat the book.

## 4. Editorial workstreams

### Research and fact checking
- Build an evidence ledger: source title, publisher/author, official URL, first published/updated/accessed date, version/commit, supportable claims, quote/licence warning, confidence and limitations.
- For each method, record origin/history, current official terminology, workflow, artifact outputs, decision rights, primary design tradeoffs, supported project types and documented limitations.
- Separate *vendor intentions* from *observed engineering outcomes*. No unsourced statement that a method is 2x faster, cheaper, safer or enterprise-ready.
- Every chapter references primary sources and, where feasible, independent analyses or well-described field reports.

### Book architecture
- Finalize thesis, audience and TOC, distinguish conceptual chapters from method chapters, set word budgets and repetition controls.
- Prepare glossary, terminology taxonomy, diagram plan, cross-reference map and consistent scorecards.
- Write chapter abstracts and reader outcomes before full prose.

### Case study and experiments
- Build one common set of business requirements, success conditions, architecture constraints and acceptance tests.
- Show *how each method decomposes the same work*, not just a separate fully built app that hides confounding factors.
- Where true side-by-side executions are feasible, use matched tasks, same AI/model versions, equivalent budgets and transparent logs.
- Present all measured outcomes with limitations; if controls cannot be met, publish a qualitative walkthrough instead of a false benchmark.

### Technical validation
- Choose supported framework versions before code starts; record exact model/version and run date.
- Run automated tests, build, lint, dependency/security scans, and key usage flows for reference sample, capturing real outcomes.
- Independently review authentication, multi-tenancy boundaries, injection risks, data leakage, secrets and deployment caveats.
- Code examples must either correspond to a tested commit or be labeled illustrative.

### Editing and publication
- Use a substantive edit, technical fact check, copyedit, citations audit, links audit, accessibility review and cross-format QA.
- Check consistent wording, capitalization and trademark notices.
- Build EPUB and print PDF from clean manuscript; validate TOC, footnotes, figure captions, code line wrapping, font embedding rights and metadata.
- Publishing accounts and final upload remain author-controlled.

## 5. Milestone gates

| Milestone | Output | Review gate |
|---|---|---|
| M0 — Foundation | Research backlog, methodology taxonomy, source ledger, competitive positioning, outline critique | Author approves scope and no-tool confusion |
| M1 — Book architecture | Approved outline, detailed abstracts, style guide refinements, word budget, chapter cross-ref map | Author signs off before prose |
| M2 — Evidence base | Source dossiers per method, contested claims, version snapshots, permission checks | Technical reviewer verifies sourcing |
| M3 — Pilot | Introduction, one method chapter, decision chapter sample, pilot case study | Author reviews voice, rigor, depth |
| M4 — Case study | Frozen requirements, harness, reproducible trials or qualitative workflows, actual tests and logs | Technical approval and disclosed limitations |
| M5 — Manuscript | All chapters written, citations and tables complete, cross-references resolved | Developmental edit |
| M6 — Editorial/QA | Fact check, independent technical review, copyedit, originality and legal/trademark review | No blocking issues |
| M7 — Publishing | Final Markdown, EPUB, PDF, print/eBook proof checklist, companion release | Final human sign-off; publish manually |

No milestone is automatically approved by an AI agent. The task is not complete just because text exists.

## 6. Chapter authoring lifecycle

For each chapter, follow exactly:
1. **Brief** — one-sentence question, audience outcome, scope boundaries, dependencies.
2. **Research** — approved sources; unsupported claims enumerated.
3. **Outline** — 5–8 major sections with narrative and concrete examples.
4. **Draft** — readable prose, original diagrams/tables, citations and controlled word count.
5. **Technical review** — verify every method-specific statement, code and terminology.
6. **Editorial review** — cut repetition, improve continuity, remove promotional phrasing.
7. **Gate** — update chapter quality checklist and status; unresolved claims remain flagged.

Method chapters share the same structure and comparison questions but must not be formulaic or copy-pasted.

## 7. Roles (simulated editorial perspectives)

- **Research editor:** Finds and evaluates sources, identifies ambiguity.
- **Methodology analyst:** Classifies approaches, compares fairly.
- **Technical author:** Writes accessible, precise explanations and examples.
- **Implementation engineer:** Builds, runs and records case-study experiments.
- **Independent reviewer:** Tries to falsify claims; checks experiments and security.
- **Copy editor:** Improves flow, clarity and consistency.
- **Production editor:** Builds EPUB/PDF, performs export QA.

Codex can adopt these **roles as review passes**, but role labels do not constitute independent human validation. Human approval and outside technical review are still required.

## 8. Comparison methodology

Use `COMPARISON_FRAMEWORK.md` and `templates/METHOD_SCORECARD.md`. Evaluate explicit decision rights, planning overhead, artifact lifecycle, requirements traceability, context management, solo/team suitability, brownfield suitability, testing, deployment governance, portability and maintainability. Assess method features from primary sources; assess claimed effectiveness only with independent evidence or reproducible tests.

**Never fill scores based on intuition alone.** Use confidence labels, mark `Not assessed` when evidence is insufficient and allow tradeoffs where no winner exists.

## 9. Example-study design

Use `CASE_STUDY_SPEC.md`. The common story is a realistic small B2B multi-tenant workflow SaaS. We will compare how approaches handle specification and implementation of the same scoped features. Fix requirements before experimental runs; retain a locked baseline plus logged changes.

Don't turn this book into an ASP.NET Core tutorial. Include just enough code to explain the engineering decision; link larger runnable examples in a companion repository if authorized.

## 10. Source, legal and ethical constraints

- Cite external ideas/claims with source-specific notes; don't reproduce original artwork or full proprietary prompts.
- Check licences and trademarks of names/logos before publishing; no implying partnerships.
- Avoid copying the AIUP author's existing Apress book. Our book must focus on independent *cross-method choice*, contrasting multiple methods with a distinct case study and original evidence.
- If methodology versions evolve mid-draft, keep original reproducible research snapshot and note material updates in an appendix rather than rewriting comparisons silently.
- For contested value claims (productivity, quality, speed) use uncertainty and disclose conflicts of interest.

## 11. Publication gates

Prior to release verify: professional edit, executable samples, source completeness, fact checking, honest experimental evidence, author identity/byline, permissions/licence audit, citations/reference conversion, image accessibility, EPUB navigation and validator results, PDF page rendering and bleed/trim checks, actual KDP specifications on upload date, cover rights, proof copy review and final metadata. KDP acceptance is not guaranteed by generating a PDF.

## 12. Change control

Keep decisions in `research/DECISION_LOG.md`. When adding/removing a named method, changing the case-study domain or changing the chapter count, create a change proposal with reader value, affected files, costs and risks. Only merge on author approval. The freeze point for research claims must be recorded for each edition.

## 13. Definition of success

A reader can pick a method for a concrete scenario and defend the choice, replicate key examples, identify when **not** to introduce heavy process and explain the limits of every comparison. Every substantial claim is supported, qualified or explicitly marked as analysis. The author has reviewed and approved all production assets.
