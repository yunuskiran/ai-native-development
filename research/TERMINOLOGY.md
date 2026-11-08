# M0 terminology and taxonomy

Status: research recommendation for author review, 2026-10-31. This file is not an approved book glossary. Source IDs refer to the [source ledger](SOURCE_LEDGER.md); wording marked “book convention” is our operational definition.

## Taxonomy verdict

Retain **four named methodologies/process frameworks and one cross-cutting approach**. “Five methods” would imply equivalence that the coverage map does not support. SDD can describe how each framework treats specifications; it is not automatically a fifth implementation arm. These classifications serve this book's reader question, not a universal certification scheme. [C01, C06](SOURCE_LEDGER.md#claim-register)

| Coverage item | Classification for this book | Evidence for inclusion | Ambiguity to expose |
|---|---|---|---|
| BMAD Method / BMad Method | Named adaptable development method with agent/workflow implementations | Primary README describes explicit planning, implementation and specialized perspectives; stable source candidate is `6.12.4`. [S01–S02](SOURCE_LEDGER.md#s01--bmad-method-main-branch-readme) | Capitalization and vocabulary evolve. Main-branch v7 preview and stable v6.12 differ; optional testing modules are separate interventions. Do not invent an acronym expansion. |
| GSD (Get Shit Done), framework lineage | Agent-hosted process/context framework; exact lineage requires author decision | Old repository points to Core; Core documents persistent planning and a phase loop. [S03–S04](SOURCE_LEDGER.md#s03--former-gsd-framework-repository-migration-notice) | Current Core uses “Git. Ship. Done.” Select historical GSD or current Core explicitly. The source manifest says `1.19.0`; an older README highlight is not the version authority. |
| AWS AI-Driven Development Lifecycle (AI-DLC) | Vendor-origin lifecycle methodology; evaluate a named implementation profile separately | AWS's original account and AWS Labs workflow source describe decision/review structures. [S07–S08](SOURCE_LEDGER.md#s07--aws-original-ai-dlc-introduction) | Primary article uses “Life Cycle” in its title. The original three-phase account and current five-phase implementation require a mapping; profile names and ceremony are version-dependent. “AWS” does not establish cloud deployment as a requirement. |
| AI Unified Process (AIUP) | Named iterative requirements/use-case methodology with implementation plugins | Methodology page and portable workflow source describe persistent specifications and review. [S09–S10](SOURCE_LEDGER.md#s09--aiup-methodology-website) | Separate the method, its core, construction plugins and Studio product. A plugin's advertised stack support is not verified compatibility. “Unified Process” ancestry does not make every historical UP practice an AIUP requirement. |
| Spec-Driven Development (SDD) | Cross-cutting approach to the role and lifecycle of specifications | An attributed three-pattern lens supplies useful questions across frameworks. [S13](SOURCE_LEDGER.md#s13--sdd-terminology-birgitta-böckelers-first-hand-analysis) | An emerging label, not a single versioned standard. Do not infer a method's spec lifecycle from the SDD label alone. |

Selection rule: include the four frameworks because the author chose them and each supplies process guidance beyond a single prompt. Compare **documented method version + implementation profile + operating conditions**. The scope can be defended without declaring every other process toolkit “just a tool.”

## Three SDD patterns: attributed analytical vocabulary

The labels below are attributed to Birgitta Böckeler's 2025 analysis, not presented as our invention or as a standards body's levels. They describe artifact policy rather than a quality ladder. [S13](SOURCE_LEDGER.md#s13--sdd-terminology-birgitta-böckelers-first-hand-analysis)

| Label | Question to ask in the book | Evidence needed before applying it |
|---|---|---|
| Spec-first | Is a specification used before implementation? | A dated workflow passage and an example artifact. This alone says nothing conclusive about long-term maintenance. |
| Spec-anchored | Does the specification persist and govern later changes? | Retention, change ownership and reconciliation rules, plus a maintenance example. |
| Spec-as-source | Are human edits directed to specifications while implementation is generated from them? | Explicit code-edit policy, regeneration boundaries and reproducibility limits. Generated code is not assumed deterministic. |

AIUP explicitly describes itself as spec-anchored; that is self-classification, not evidence that drift is prevented in practice. [S09](SOURCE_LEDGER.md#s09--aiup-methodology-website) The other methods' positions remain **Not assessed** until their selected profiles and maintenance behavior are reviewed. A specification can be useful without adopting the strictest pattern.

## Implementation context, not extra peer chapters

| Name/category | Treatment | Boundary |
|---|---|---|
| GSD Pi | Coding-agent product with process features; context only | Different from GSD Core. Excluding it preserves the master's framework/product distinction. [S05–S06](SOURCE_LEDGER.md#s05--former-gsd-2-repository-separate-migration-notice) |
| Kiro | Product family with specification workflows | Describe the surface/version used; do not rank an IDE against AIUP or AWS AI-DLC. [S16](SOURCE_LEDGER.md#s16--kiro-official-specs-documentation) |
| GitHub Spec Kit | Toolkit with substantive process/template content | Context under the master plan. Its scope is not reducible to an editor or CLI command. [S14](SOURCE_LEDGER.md#s14--github-spec-kit-context-not-an-additional-main-comparison-arm) |
| OpenSpec | Specification/change workflow implementation, also described as a framework | Context by editorial choice; acknowledge its process content. [S15](SOURCE_LEDGER.md#s15--openspec-context-with-workflow-content) |
| Other coding agents/IDEs | Execution hosts and interfaces | Host/model differences are confounders to record, not methodology wins. Individual host capabilities remain unreviewed. |
| Task Master AI / Agent Skills | Context candidates named in the master plan | Specific definitions, ownership and versioned capabilities: **NOT VERIFIED IN THIS SESSION**. Do not write factual profiles yet. |

## Book conventions requiring approval

| Term | Working meaning / usage rule |
|---|---|
| AI-driven / AI-assisted / AI-native | Quote or attribute a source's label, then describe who proposes, executes and approves. Do not impose an unsupported universal autonomy scale. |
| Vibe coding | For this book, a proposed observable pattern: implementation proceeds from conversational intent without consistently preserved decisions or acceptance evidence. Avoid using it as a label for all informal development, novices, or small tasks. Historical origin: **NOT VERIFIED IN THIS SESSION**. |
| Methodology / method / process framework | Use the creator's name and explain the actual decisions, roles, artifacts and feedback loops. Do not claim that shared classification makes their scope identical. |
| Specification | A maintained description of required behavior or constraints. Record its owner, scope, change policy and validation. A long prompt is not automatically a specification. |
| Executable specification | Reserve for an artifact with a defined mechanical validation/execution path. Natural-language guidance to an agent alone does not establish executability. |
| Source of truth | State truth **for what**, which artifact prevails on conflict, and who can change it. The phrase is not proof of synchronization. |
| Context engineering | Deliberate selection, persistence and transfer of information to an agent. Documented mechanisms can be compared; claimed quality gains need evidence. |
| Decision right / human gate | Who may decide, what evidence they see, and whether approval is advisory or enforced. Ask rather than assume a pause in a prompt is an enforced control. |
| Traceability | An inspectable link among requirement, decision, implementation and test. Presence, completeness and correctness are separate questions. |
| Phase / milestone / unit / bolt | Preserve each method's native term with a mapping. GSD's phase is not assumed equivalent to an AWS lifecycle phase. Counts do not measure ceremony fairly. |
| Test coverage | Specify requirement/scenario coverage or code coverage explicitly. Passing a generated suite does not establish acceptance-test independence. |
| Benchmark / walkthrough | Benchmark: an executed comparison under a disclosed protocol. Walkthrough: a documented example of applying a process. Never report the second as the first. |
| Reproducible | Inputs, versions, commands and records permit a rerun and comparison. Identical LLM output is not promised. |
| Independent review | Review by someone outside the authoring process with disclosed interests. Additional AI role passes do not constitute independent human validation. |
| Not assessed / not supported / absent | Different states: insufficient evidence; outside a documented profile; confirmed missing in a defined snapshot. Do not substitute one for another. |
| Enterprise-ready / faster / safer | Interested-party claims until operational criteria and independent or reproducible evidence support them. No default ratings. |

Existing engineering practices named in the master plan remain foundations. Credit established requirements engineering, Agile, TDD, BDD, DDD, ADRs, CI/CD and threat modeling where used; detailed historical attributions await M2 verification.
