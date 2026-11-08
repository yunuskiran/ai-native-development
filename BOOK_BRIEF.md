# Engineering with AI: Beyond Vibe Coding — book brief

Status: **M1 architecture accepted by the author**, decision A06. Language: English. Date: 2026-10-31.
Authority: [master plan](docs/BOOK_MASTER_PLAN.md), [author-supplied outline](OUTLINE.md), and decisions A03–A06 in the [decision log](research/DECISION_LOG.md). Audience, planning length, chapter boundaries and the case direction below were accepted with M1. Factual evidence and implementation readiness remain separate gates.

## Reader problem and promise

An engineering team wants AI to contribute beyond isolated code suggestions, but has no defensible way to choose how requirements, context, implementation and review should work together. This book will help readers compare four process frameworks under explicit project conditions, inspect their artifacts and decision rights, and plan a local evaluation. It will separate documented mechanisms, interested-party claims and observed outcomes.

The proposed thesis is that explicit decisions, durable context, constrained changes and credible evaluation become central engineering work when AI participates throughout delivery. Test that thesis against small repairs, uncertain requirements, existing code and process overhead. Do not assume every task needs a complete lifecycle or that more artifacts mean better engineering.

## Proposed audience and prerequisites

- Primary: practicing software engineers, technical leads and software architects choosing or adapting a team development process.
- Secondary: hands-on engineering managers and experienced developers evaluating AI-assisted delivery. Beginners can follow the reasoning but are not the primary teaching target.
- Prerequisites: Git, ordinary application architecture, basic automated tests, code review and experience maintaining at least one application. TypeScript examples explain decisions rather than teach the language or Node.js from scratch.

After reading, a reader should be able to distinguish methodology from host/tooling, map a method's required decisions and artifacts, evaluate specification lifecycle policy, choose a process for a stated scenario, assess evidence limits and reproduce the disclosed procedure without expecting identical model output.

## Coverage and boundaries

The fixed sequence has fourteen chapters in [OUTLINE.md](OUTLINE.md). BMAD, GSD's framework lineage, AWS AI-DLC and AIUP receive equally scrutinized deep dives. SDD has its own chapter 8 and remains a lens across all four. Shared concepts appear briefly before the deep dives and are expanded in their owner chapters.

IDEs, coding agents, Spec Kit, OpenSpec and other implementations appear where they explain a mechanism or a confounder. They do not become competing peer methodologies. Acknowledge process-bearing toolkits honestly; exclusion from main chapters is editorial scope, not a claim that they lack process content.

No universal winner, league table, productivity multiplier or “enterprise-ready” conclusion is promised. Installation catalogs, exhaustive prompt libraries, a language tutorial, a full SaaS operations manual and forecasts presented as facts are outside scope. Existing engineering practices retain their established attribution.

## Case and evidence strategy

Author-selected technology family: **TypeScript / Node.js**. Proposed domain: a synthetic, multi-tenant vendor-access approval SaaS, pending domain approval. The [case specification](CASE_STUDY_SPEC.md) separates common business outcomes from method-native artifacts and leaves framework, database, host/model and exact versions open.

Introduce the business problem in chapter 3, use one bounded shared increment in chapters 4–7, compare artifact trails in chapters 8–10 and give the full account in chapter 11. Testing/security obligations apply throughout, with chapter 12 owning the consolidated treatment. Chapter 11's “Real-World” title means realistic engineering constraints unless genuine field deployment is documented; no production history will be invented.

The minimum viable evidence product is an honestly labeled artifact walkthrough. Executed comparisons require a frozen protocol, acceptance oracle, supported profiles, authorized resources and actual records. Method-source facts come from M2 dossiers; effectiveness requires stronger evidence. See the [research protocol](RESEARCH_PROTOCOL.md) and [future run protocol](research/RUN_PROTOCOL.md).

## Length, voice and original contribution

Proposed main text: **66,500 words**; additional planning allowances: 3,500 for appendices and 2,000 for front/back matter, excluding the bibliography/index and runnable companion code. This is a proposed 72,000-word editorial budget, not written manuscript or a page-count guarantee. See the [word budget](research/WORD_BUDGET.md).

Write clear, practical English for readers who can program. Use original examples, measured claims only when measured, and enough code to make decisions concrete. Four comparable methods, an original common case and a transparent decision instrument distinguish the proposed contribution. Public-scope competitor review is not a certification of full-text originality.

## M1 acceptance and later decisions

The author accepted the primary audience, planning word budget, chapter boundaries and vendor-access domain in A06. Implementation/evidence decisions remain on the [open-question register](research/OPEN_QUESTIONS.md). No book prose, paid services, experiments, deployment or publication is authorized by this architecture approval.
