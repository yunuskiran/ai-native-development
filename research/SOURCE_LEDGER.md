# M0 source ledger

Book: **Engineering with AI: Beyond Vibe Coding**. Access date for every inspected record: **2026-10-31, Australia/Melbourne**. This is an M0 identity and evidence audit, not the completed M2 evidence base. No author source list was supplied at intake; M1 now provides a [sources index](../SOURCES.md) without expanding the original inspection claims.

## Evidence rules used in this session

- **INSPECTED** means the stated page or file sections were retrieved and examined in this session. It does not mean the implementation was installed, its claims independently confirmed, or the entire linked site read.
- **DOCUMENTED** means a primary source describes a process or artifact. **CLAIM ONLY** means a publisher or maintainer asserts an outcome. **ANALYSIS** identifies this book project's interpretation. These are separate from confidence in transcription.
- **NOT VERIFIED IN THIS SESSION** applies to uninspected material and unsupported factual claims. It never means false. Missing documentation is not evidence that a method lacks a feature.
- GitHub material was retrieved with the connected GitHub read-only fetch tool. Web pages were opened with the web tool. Search snippets were discovery aids, not the final authority where direct retrieval succeeded.
- Dates below are explicitly publication dates, Git commit dates, or connector-reported file modification dates. The latter are not first-publication dates. Unknown dates remain unknown. Research pins are candidates, not approved experimental versions.
- No external book, website, artwork, prompt collection, or source repository was mirrored into this checkout. Notes are independent summaries. Unless stated otherwise, licence and trademark documents have **NOT VERIFIED IN THIS SESSION** status; a README badge is not a completed permissions audit.

## Inspected source records

### S01 — BMad Method: main-branch README

- Publisher: BMad Code organization / repository maintainers. [Inspected README, pinned and matched to initial main read](https://github.com/bmad-code-org/BMAD-METHOD/blob/61e01f82644c4bb533750cfa0d6d61ab61d2cc9b/README.md); [resolved commit](https://github.com/bmad-code-org/BMAD-METHOD/commit/61e01f82644c4bb533750cfa0d6d61ab61d2cc9b).
- Snapshot: `61e01f82644c4bb533750cfa0d6d61ab61d2cc9b`; commit 2026-10-18; file modification 2026-10-18. First publication unknown. Status: **INSPECTED**, README including release-line and ecosystem sections.
- Supports: the main README distinguishes a stable v6.12 line and v7 preview alpha. It describes adaptable planning and specialized workflows hosted in coding tools.
- Limit: its stated v7 ETA, 2026-10-16, predates this session despite the preview label. Do not infer that a release occurred from an ETA or floating docs. Confidence: high for retrieved wording; release finality unresolved.
- Rights: README asserts MIT and identifies trademarks; the underlying legal files were not inspected.

### S02 — BMad Method: stable-branch source and manifest

- Publisher: same maintainers. [Stable README](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/README.md); [package manifest](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/package.json).
- Snapshot: `V6.12` resolved to `bab9082c3e884e0d72c759bcd1a6d90bcc01be84`, commit 2026-10-14; manifest version `6.12.4`. README file modification 2026-08-30. First publication unknown. Status: **INSPECTED**, README and manifest version.
- Supports: a concrete stable-line research candidate, process scaled to work size, and separately distributed optional modules.
- Limit: registry publication and release assets were not checked. A source manifest is not proof of the installed package. Testing add-ons must not be silently counted as core capabilities. Confidence: high for source identity; runtime behavior not assessed.

### S03 — Former GSD framework repository: migration notice

- Publisher: `gsd-build/get-shit-done` maintainers. [Pinned notice](https://github.com/gsd-build/get-shit-done/blob/bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815/README.md).
- Snapshot: `bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815`, commit 2026-05-31; README file modification 2026-05-31. First publication unknown. Status: **INSPECTED**, complete short notice.
- Supports: this repository says development moved to `open-gsd/gsd-core`.
- Limit: establishes a maintainer-declared destination, not an independent account of ownership, history, package safety, or all community forks. Search results still surfaced older documentation. Confidence: high for notice, history incomplete.

### S04 — GSD Core: README, manifest, phase loop

- Publisher: Open GSD maintainers. [README](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/README.md), [manifest](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/package.json), [phase-loop explanation](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/explanation/the-phase-loop.md).
- Snapshot: `72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc`, commit 2026-10-26; manifest `@opengsd/gsd-core` version `1.19.0`. README file modification 2026-07-15; phase-loop file 2026-06-02. First publication unknown. Status: **INSPECTED**, README, manifest identity, phase/artifact/context sections of explanation.
- Supports: an agent-hosted process framework; discuss, plan, execute, verify and ship, with an optional UI step; persistent planning artifacts and fresh-context worker design. Current branding expands GSD as “Git. Ship. Done.”
- Limit: older “what's new 1.7.0” README pointer does not supersede the manifest. Fixed context-window numbers and prevention of context degradation are maintainer descriptions/claims, not portable model guarantees. Effectiveness **CLAIM ONLY**. Confidence: high for documented structure, no runtime validation.
- Rights: README asserts MIT; licence text not inspected.

### S05 — Former GSD 2 repository: separate migration notice

- Publisher: `gsd-build/gsd-2` maintainers. [Inspected README](https://github.com/gsd-build/gsd-2/blob/main/README.md).
- Version: floating `main`, no immutable pin resolved; file modification 2026-05-22. First publication unknown. Status: **INSPECTED**, complete short notice.
- Supports: this different repository points to `open-gsd/gsd-pi`.
- Limit: no basis for treating the framework and this product lineage as one experimental intervention. Confidence: high for notice; provenance beyond the notice not assessed.

### S06 — GSD Pi: product boundary

- Publisher: Open GSD maintainers. [Pinned README](https://github.com/open-gsd/gsd-pi/blob/f2756216ccf6bbe9af2fc677f5eafef986727e4e/README.md).
- Snapshot: `f2756216ccf6bbe9af2fc677f5eafef986727e4e`, commit 2026-10-30; README file modification 2026-10-29, displays release `v1.23.0`. First publication unknown. Status: **INSPECTED**, overview, release/status, installation and migration sections.
- Supports: self-description as a local coding agent with workflow and Git automation, distinct from a framework hosted in another agent.
- Limit: release display not validated against assets or manifest; no installation performed. Keep as context unless author changes scope. Confidence: high for product description. Rights badge only; no reuse approved.

### S07 — AWS: original AI-DLC introduction

- Author/publisher: Raja SP, AWS DevOps & Developer Productivity Blog. [Article](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/).
- Published 2025-07-31; no separate update date or immutable version obtained. Status: **INSPECTED**, methodology, phases, benefits and author sections.
- Supports: vendor-defined lifecycle with inception, construction and operations; human decisions and collaborative elaboration/construction; repository context artifacts.
- Limit: faster delivery and improved quality are **CLAIM ONLY** here. The linked white paper was not inspected. Confidence: high for the original description, no effectiveness inference. Copyrighted prose/diagrams: cite and redraw independently if needed.

### S08 — AWS Labs: AI-DLC Workflows implementation

- Publisher: `awslabs/aidlc-workflows` maintainers. [README](https://github.com/awslabs/aidlc-workflows/blob/3939a8b9182f2e4153b92028057a7be74e0684c2/README.md); [workflow profiles](https://github.com/awslabs/aidlc-workflows/blob/3939a8b9182f2e4153b92028057a7be74e0684c2/docs/guide/workflow-profiles.md).
- Snapshot: `3939a8b9182f2e4153b92028057a7be74e0684c2`, commit 2026-10-30; README displays `2.11.2`, file modification 2026-10-30; profiles file 2026-10-26. First publication unknown. Status: **INSPECTED**, overview and profile/ceremony descriptions.
- Supports: documented implementation has five phases and 33 stages overall, with task-specific routes. Profile tables count 30 post-initialization stages, excluding three setup stages; that is a counting convention, not by itself a contradiction. Profile choice changes review and ceremony defaults.
- Limit: do not merge this implementation silently with S07's three-phase account. Approval enforcement and supported harnesses need code/runtime review. Model recommendations are not experimental controls. Confidence: high for documentation; execution not assessed.
- Rights: README asserts MIT-0. Legal file, specification PDF and release package not inspected.

### S09 — AIUP: methodology website

- Author/publisher: Simon Martinelli / AI Unified Process. [Methodology](https://unifiedprocess.ai/methodology.html).
- No publication/update date or immutable version obtained. Status: **INSPECTED**, phases, greenfield/brownfield and spec-lifecycle sections.
- Supports: four iterative phases; persistent use cases and requirements; human review; explicit self-placement in spec-anchored development.
- Limit: maintained alignment, comprehensive traceability, safe changes and broad suitability are design intentions or **CLAIM ONLY**, not measured guarantees. Confidence: high for self-description. Copyrighted site; no diagrams copied.

### S10 — AIUP: marketplace implementation and workflow

- Publisher: AI Unified Process maintainers. [README](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/README.md); [workflow](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/docs/workflow.md).
- Snapshot: `3ad51b0707e9bed6e54b9de46ebc2f28d7afa960`, commit and file modifications 2026-10-29. No single umbrella semantic version established. First publication unknown. Status: **INSPECTED**, overview, plugin choices, workflow and artifact flow sections.
- Supports: stack-independent core, construction adapters, specifications and traceable review/test artifacts. The README lists a Blazor/.NET combined plugin alongside other stack options.
- Limit: listing is not proof of compatibility with the book's eventual stack. Plugin versions, prompts, tests and installation remain unvalidated. Source header asserts Apache-2.0; LICENSE/NOTICE audit outstanding. Confidence: high for documented layout.

### S11 — Apress/Springer Nature: existing book metadata and contents

- Author: Simon Martinelli. Publisher: Apress. [Publisher page](https://link.springer.com/book/10.1007/979-8-8688-2851-5), DOI `10.1007/979-8-8688-2851-5`.
- First edition; eBook published 2026-08-12, softcover 2026-08-13; ISBNs `979-8-8688-2851-5` and `979-8-8688-2850-8`. Status: **INSPECTED**, public description, contents and bibliographic fields only.
- Supports: *Spec-Driven Development: From Specs to Code with AI Agents* centers AIUP and includes a simple task-manager case. Scope overlaps specification-to-implementation guidance.
- Limit: full text **NOT VERIFIED IN THIS SESSION**; no purchase or subscription used. Cannot certify whole-book originality or infer detailed treatment from headings. Confidence: high for metadata, limited for coverage. Copyrighted publication: no chapter text downloaded or reproduced.

### S12 — AIUP: publications page

- Publisher: Simon Martinelli / AI Unified Process. [Publications](https://unifiedprocess.ai/publications.html).
- States August 2026 book publication; page update unknown, no immutable version. Status: **INSPECTED**, book and companion-guide descriptions.
- Supports: creator's account of the book and a separate free use-case-writing guide; both occupy instructional territory relevant to positioning.
- Limit: same interested source family as S09–S11, not independent corroboration of value. Guide full text **NOT VERIFIED IN THIS SESSION**. Confidence: high for advertised scope, not reading experience.

### S13 — SDD terminology: Birgitta Böckeler's first-hand analysis

- Author: Birgitta Böckeler; host: Martin Fowler's website. [Article](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html).
- Published 2025-10-15; no immutable version obtained. Status: **INSPECTED**, definition, three specification-lifecycle patterns and evaluation caveats.
- Supports: attribution of spec-first, spec-anchored and spec-as-source as an analytical distinction. This is a primary source for that author's taxonomy, not a standards-body definition.
- Limit: tool observations reflect the author's dated trials, not current feature validation or a comparative benchmark. Confidence: high for attribution, limited generalization. No figure copied.

### S14 — GitHub Spec Kit: context, not an additional main comparison arm

- Publisher: GitHub repository maintainers. [README](https://github.com/github/spec-kit/blob/main/README.md).
- Floating `main`; file modification 2026-10-20; first publication and immutable pin not established. Status: **INSPECTED**, introductory toolkit/process sections.
- Supports: toolkit includes prescribed processes and templates; calling it merely an editor would be inaccurate.
- Limit: broad feature inventory and runtime behavior not reviewed. Exclusion from main chapters is the author's scope choice, not proof it lacks methodology content. Confidence: high for inspected scope. Rights not audited.

### S15 — OpenSpec: context with workflow content

- Publisher: Fission AI repository maintainers. [README](https://github.com/Fission-AI/OpenSpec/blob/main/README.md).
- Floating `main`; file modification 2026-10-30; first publication and immutable pin not established. Status: **INSPECTED**, philosophy and proposal/apply/archive example.
- Supports: specification/change workflow implementation. Maintainers also use framework terminology.
- Limit: promotional preference/suitability claims are not comparative findings. Scope exclusion does not settle its universal classification. Confidence: high for documented example. Rights not audited.

### S16 — Kiro: official specs documentation

- Publisher: Kiro. [Specs documentation](https://kiro.dev/docs/specs/).
- Page says updated 2026-10-15; first publication and immutable version unknown. Status: **INSPECTED**, artifact structure, workflow and capability table.
- Supports: a product implements specification workflows with requirements/bug analysis, design and task artifacts; surfaces have different capabilities.
- Limit: product workflow does not make the IDE a peer methodology. No current subscription, model access or installation verified. Confidence: high for docs, no runtime inference. Rights not audited.

### S17 — Adjacent comparative research

- Author: Sanderson Oliveira de Macedo. [arXiv record](https://arxiv.org/abs/2606.04967v1), *From Prompt to Process: a Process Taxonomy and Comparative Assessment of Frameworks Supporting AI Software Development Agents*.
- Version 1 submitted 2026-06-03. Status: **INSPECTED**, abstract and submission metadata only.
- Supports: prior work explicitly compares process frameworks including BMAD and GSD. A claim that this book is the first such comparison would be unsupported.
- Limit: full paper, rubric, evidence and peer-review status **NOT VERIFIED IN THIS SESSION**. Do not adopt its scores as findings. Confidence: high for abstract scope only. Licence text not inspected.

### S18 — O'Reilly: adjacent book and title overlap

- Author: Addy Osmani. Publisher: O'Reilly Media. [Publisher catalog page](https://www.oreilly.com/library/view/beyond-vibe-coding/9798341634749/).
- Catalog dates the book to August 2025; update date/immutable page version unknown. Catalog identifier `9798341634749` (do not assume this identifies every format). Status: **INSPECTED**, public metadata, overview and contents only.
- Supports: *Beyond Vibe Coding: From Coder to AI-Era Developer* already occupies nearby practical AI-development territory and shares wording with our subtitle.
- Limit: full text **NOT VERIFIED IN THIS SESSION**. This is an editorial differentiation issue, not a title-rights determination. Confidence: high for catalog facts, limited for detailed coverage. No chapter text obtained.

### S19 — Pragmatic Bookshelf: adjacent process book and title overlap

- Author: Uberto Barbini. Publisher: The Pragmatic Programmers. [Publisher page](https://pragprog.com/titles/ubaidev/process-over-magic-beyond-vibe-coding/).
- Page states June 2026, edition 1, ISBN `9798888652008`; page update/immutable version unknown. Status: **INSPECTED**, public description, metadata and contents only.
- Supports: *Process Over Magic: Beyond Vibe Coding* discusses controlled assistant workflows, rules, existing code and team practices; similar subtitle vocabulary already exists.
- Limit: full text **NOT VERIFIED IN THIS SESSION**; publisher productivity language is **CLAIM ONLY**. No extracts downloaded. Confidence: high for public positioning. No legal or quality ranking inferred.

## Claim register

| ID | Claim and allowed use | Evidence | State / remaining work |
|---|---|---|---|
| C01 | Four named frameworks plus SDD is a useful editorial coverage map. | S01–S04, S07–S10, S13 | **ANALYSIS**; author approval pending; not five equivalent experimental arms. |
| C02 | BMad stable and preview source lines must be distinguished. | S01–S02 | **DOCUMENTED**; `6.12.4` is a source candidate, not an approved installed release. |
| C03 | Old GSD repository directs readers to Core; Pi has a separate agent-product description. | S03–S06 | **DOCUMENTED**; history and author's intended edition unresolved. |
| C04 | Original AWS lifecycle and current workflow implementation have different scope/phase descriptions. | S07–S08 | **DOCUMENTED**; map versions explicitly; do not call the two descriptions an established implementation error. |
| C05 | AIUP maintains use cases through an iterative lifecycle; concrete plugins vary. | S09–S10 | **DOCUMENTED**; compatibility and fidelity of a selected profile untested. |
| C06 | The three SDD patterns are an attributed lens, not a universal maturity score. | S13; self-classification in S09 | **ANALYSIS** grounded in an attributed distinction. |
| C07 | The Apress book already covers AIUP-centered SDD with a task-manager case. | S11–S12 | **DOCUMENTED**, public scope only. Full-text comparison remains open. |
| C08 | Spec Kit/OpenSpec have process content; Kiro is a product with workflows. | S14–S16 | **DOCUMENTED**; exclusion from peer chapters follows the master plan. |
| C09 | Comparative process-taxonomy work predates this proposed book. | S17 | **DOCUMENTED** at abstract level; detailed literature review pending. |
| C10 | Nearby books already use “Beyond Vibe Coding” in their titles. | S18–S19 | **DOCUMENTED**; preserve the author's title while reviewing differentiation. |
| U01 | Any named method improves speed, cost, quality, security, or enterprise readiness. | Interested sources assert some benefits; no book experiment exists. | **NOT VERIFIED IN THIS SESSION** as an outcome; **CLAIM ONLY** when attributed. |
| U02 | Origin dates, acronym expansions, founder histories and complete migration histories. | Not established by this limited audit. | **NOT VERIFIED IN THIS SESSION**; research in M2 before prose. |
| U03 | Permission to reuse source prompts, diagrams, code, logos or trademarks. | README/header notices only. | **NOT VERIFIED IN THIS SESSION**; no reuse clearance granted. |
| U04 | All four frameworks work with one exact host, model and application stack. | Selected READMEs list integrations. | **NOT VERIFIED IN THIS SESSION**; feasibility check required before trials. |
| U05 | No prior publication substantially resembles the planned manuscript. | Public scope review only. | **NOT VERIFIED IN THIS SESSION**; cannot establish a negative from this search. |
| U06 | All claims in the author's intended source list and outline are checked. | Both absent at intake; author later supplied fourteen titles/order, now structurally reviewed. M1 added an index and chapter briefs, not an original author bibliography or completed dossiers. | **NOT VERIFIED IN THIS SESSION** for detailed future chapter claims; the outline/briefs are architecture, not fact-checked prose. |

## Retrieval limitations and next validation work

1. GitHub fetch rejected tag-list API requests for the old GSD repository, GSD Core and AWS Workflows with `HTTPError: 400`, endpoint not allowed. These attempts produced no inspected tag lists. Read-only commit endpoints and pinned file retrieval succeeded instead. No release assets or registry versions were inferred from them.
2. Opening `https://unifiedprocess.ai/methodology` failed. Following the website's navigation succeeded at the canonical `.html` URL recorded in S09. This is an access/path correction, not evidence that the methodology is inaccessible.
3. Floating websites, S05, S14 and S15 remain date-stamped observations. Before substantive drafting, obtain durable permitted references or record page hashes/short claim receipts and recheck material changes. Pinned repository URLs also link outward to changing documentation; their outbound pages were not thereby inspected.
4. Complete per-method dossiers in M2: origin, precise terms, required/optional artifacts, decision rights, task size, solo/team and brownfield variants, testing, operations, portability, documented limitations and counterevidence. Every assertion needs a passage locator and evidence type. Do not convert absence of evidence into a negative score.
5. Seek independent field reports or controlled research with disclosed tasks, model/host versions, operator skill and costs. S17 is a literature lead, not performance validation. No methodology rankings or numeric scores have been produced.
6. Title discovery used two bounded searches: the exact proposed title phrase, and “Beyond Vibe Coding” with book/publisher terms. The directly opened publisher pages S18–S19 support the identified overlaps; the search does not establish that the full proposed title is unique. A Pragmatic secure-domain redirect initially returned no readable lines; its canonical publisher page succeeded. Nonpublisher copies surfaced by search were not opened or used.

## Subsequent M2 research

[M2_SOURCE_LEDGER.md](M2_SOURCE_LEDGER.md) and [M2_REPORT.md](M2_REPORT.md) extend this historical audit with actual source inspections, locators, dossiers and explicit limits. Earlier M0 verification states remain dated observations; they are not silently upgraded.
