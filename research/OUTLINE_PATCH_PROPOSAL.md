# M0 outline critique and separate patch proposal

Status: **M0 REVIEW UPDATED AFTER AUTHOR INPUT**, 2026-10-31. `OUTLINE.md` was absent at intake; the author has now supplied fourteen chapter titles and their order. They are recorded verbatim in [OUTLINE.md](../OUTLINE.md). The initial twelve-slot proposal is **SUPERSEDED** and retained below for provenance. No change to the fourteen titles or their order is proposed.

## Review of the author's fourteen-chapter structure

The structure supports the intended book: context and foundations, four comparable methods, SDD as an approach, comparison and selection, a shared SaaS case, quality/failures and a forward-looking close. A dedicated chapter 8 is consistent with SDD being cross-cutting rather than a fifth competing methodology.

| Chapter | Narrative job / practical boundary to preserve | Review finding and proposed scope control |
|---|---|---|
| 1. The Evolution of AI-Assisted Development | Historical context and changing engineering responsibilities | Keep history bounded and sourced. Leave the practical critique of informal development to chapter 2 and the taxonomy to chapter 3. |
| 2. Beyond Vibe Coding | Explain what disciplined engineering adds and when lightweight work suffices | Avoid repeating the history. Use observable failure/decision patterns rather than labeling every conversational workflow careless. Reserve the full failure catalog for chapter 13. |
| 3. Understanding AI-Driven Methodologies | Establish the shared comparison vocabulary and research questions | Briefly introduce SDD, method/tool boundaries, evaluation criteria and the common SaaS problem so chapters 4–7 have prerequisites. Full SDD treatment remains chapter 8; full implementation remains chapter 11. |
| 4. BMAD Method — Deep Dive | Explain the selected profile's decisions, artifacts and bounded example | Use the same questions and business increment as chapters 5–7. Core vs add-ons and exact version remain explicit; do not repeat common foundations. |
| 5. GSD — Deep Dive | Explain the chosen framework lineage, context policy and workflow | Keep the author's title. Resolve historical GSD vs current Core in scope/version notes, not by silently renaming the chapter or treating Pi as a peer method. |
| 6. AWS AI-DLC — Deep Dive | Explain lifecycle concepts and a specific implementation profile | Distinguish concept, version and profile without turning the chapter into a vendor tool tutorial. |
| 7. AI Unified Process — Deep Dive | Explain use-case ownership, persistent artifacts and review | Apply equal evidence requirements and the same original business increment. Avoid recreating the existing AIUP book's tutorial or borrowing its sample application. |
| 8. Spec-Driven Development as an Approach | Synthesize specification lifecycle choices across the four methods | Give spec-first/anchored/as-source their attributed, qualified treatment here. Refer back to method artifacts; do not present SDD as a fifth peer trial arm. |
| 9. Comparing the Methodologies | Compare documented mechanisms and available evidence | Distinguish facts, claims, observations and uncertainty. Show tradeoffs on a common instrument; reserve scenario-based recommendations for chapter 10. |
| 10. Choosing the Right Methodology | Turn comparison into conditional project decisions | Use scenarios, constraints and decision reasons. Reference the case in chapter 11, and avoid assuming results exist before experiments have happened. |
| 11. Real-World Case Study: Building a SaaS | Give the complete requirements, artifact trails, implementation and reproduction account | Introduce the business problem briefly in chapter 3 and reuse a small slice in 4–7; this chapter owns the full case. “Real-World” means realistic requirements unless actual field deployment is documented. No fabricated production history or benchmark. |
| 12. Testing, Security & Production Readiness | Consolidate acceptance evidence, review duties and operational boundaries | Tests and security criteria must apply to earlier examples as well. This chapter deepens them; it is not where verification first starts. Local demonstrations cannot prove production readiness. |
| 13. Common Failures and Anti-Patterns | Explain diagnosis, causes, consequences and recovery across methods | Reference chapter 2's framing and chapter 12's checks; focus on method-specific failures and remedies rather than repeat their content. |
| 14. The Future of AI-Native Engineering | Close with implications, open questions and scenario analysis | Label projections as projections and date current-state claims. Avoid presenting forecasts as established evidence. |

The main risks are overlap among 1–3, SDD prerequisites before chapter 8, comparison vs selection in 9–10, the late full-case introduction, and quality appearing late. These can be handled through chapter boundaries and cross-references **without changing the author's sequence**. The table is M0 critique, not completed M1 briefs or chapter abstracts.

Independence remains an execution question: original case requirements, equally applied questions in chapters 4–7, cross-method synthesis in 8–10 and transparent evidence in 11–13. A public-scope comparison cannot establish full-text originality; see [competitive positioning](COMPETITOR_POSITIONING.md).

## Current separate patch proposal — scope notes only

The [scope-notes patch](proposals/OUTLINE_14_SCOPE_NOTES.patch) proposes appending short boundaries to the supplied outline. It changes no chapter title, number or order and remains **UNAPPLIED**. Reader value: clarify prerequisites and reduce repetition while preserving the author's structure. Cost: M1 must enforce the boundaries in briefs and cross-references. Affected files if adopted: `OUTLINE.md`, later chapter briefs and the cross-reference plan. Author approval is still required before applying these optional notes.

## Initial architecture-only review — retained for provenance

### Critique based on the master plan before the outline was supplied

| Dimension | What the master plan supports | Risk / proposed adjustment | M1 acceptance criterion |
|---|---|---|---|
| Overlap | Shared method scorecards, glossary, case study and decision chapter | Repeating SDD, testing and context definitions four times could swamp the distinctive mechanisms. Give concepts one home, then show method-specific deltas. | Every recurring concept has an owner chapter and explicit references; method chapters share questions, not repeated exposition. |
| Narrative flow | Independent cross-method choice is the central reader question | Readers need the common business problem and evidence rules before method detail, followed by synthesis after they understand the four methods. | Every chapter's prerequisites appear earlier; readers can follow one case episode through all four treatments. |
| Practicality | Matched tasks and reproducible records | Four complete application tutorials would hide decomposition differences and inflate the manuscript. Compare bounded decisions and artifacts, with larger runnable code deferred to companion assets. | Each method chapter shows the same bounded business increment, required human decisions and acceptance evidence; no full stack tutorial detour. |
| Independence | Master explicitly rejects default AIUP endorsement | A specifications → generation → tests → tools → simple-app progression would occupy nearby instructional territory. Lead with selection and comparison, then use maintenance and failure to test the thesis. | Public-scope overlap matrix completed; lawful full-text review remains scheduled. [Positioning](COMPETITOR_POSITIONING.md) |
| Balance | Ceremony should scale to context | A process-light repair needs to be allowed to succeed; avoid a careless “vibe coding” straw comparator. Fixed chapter order must not imply a ranking. | Tiny-change counterexample and fair success conditions are in briefs; no ordinal league table without evidence. |
| Operational scope | Operations and governance appear in the comparison criteria | A feature-only example cannot validate operational or team claims. Include an operational decision exercise, labeled as such when no production/team observation exists. | Explicit boundary between observed case evidence and discussion-only dimensions. |
| Longevity | Edition snapshots and appendices are planned | Floating commands, plugin names and IDE setup will age quickly. Keep stable reasoning in chapters, dated recipes outside the core narrative. | Each volatile instruction has a snapshot owner and recheck rule. |

These were design risks based on the master plan alone. The author's actual fourteen-chapter structure is now reviewed above. The Apress comparison remains limited to public scope [S11–S12](SOURCE_LEDGER.md#s11--apressspringer-nature-existing-book-metadata-and-contents); adjacent process books and prior research reinforce the need for specific differentiation [S17–S19](SOURCE_LEDGER.md#s17--adjacent-comparative-research).

### Superseded twelve-slot candidate — historical only

The original [candidate patch](proposals/OUTLINE_M0_CANDIDATE.patch) offered twelve chapter slots when the author outline was unavailable. It is now **SUPERSEDED — DO NOT APPLY**. The table below is retained as the original proposal, not as a competing current outline:

| Proposed slot | Editorial purpose |
|---|---|
| 1. Engineering decisions when AI participates | Establish accountability, uncertainty and when lightweight work is enough. |
| 2. Specifications, context and evidence | Introduce SDD as a shared lens and separate intentions from outcomes. |
| 3. The common case and comparison protocol | Define comparable work, acceptance evidence and limits before comparisons. |
| 4. BMAD Method | Examine a chosen version through the common questions. |
| 5. GSD framework lineage | Make the historical/Core choice visible; exclude the Pi product as a peer. |
| 6. AWS AI-DLC | Separate lifecycle concepts from the chosen workflow implementation. |
| 7. AI Unified Process | Give use-case-driven artifacts equal scrutiny and bounded coverage. |
| 8. One change, four artifact trails | Compare decomposition, human decisions and evidence for a bounded feature. |
| 9. Repair, maintenance and specification drift | Test how requirements and code evolve, including tiny changes. |
| 10. Quality, operations and team decision rights | Assess boundaries and review duties, with observed vs unobserved scope explicit. |
| 11. Choosing and adapting a process | Produce conditional scenario decisions with costs, uncertainty and exit criteria. |
| 12. Running your own evaluation | Explain reruns, evidence interpretation and response to version changes. |

Method order follows the request, not an inferred quality order. Chapters 3, 8 and 12 have different jobs: protocol, evidence synthesis and replication. If this separation proves repetitive in M1, merge only through a fresh author-reviewed proposal. No results chapter is promised: slot 8 can report artifact walkthroughs if the experimental gate fails.

### Initial patch impact and adoption conditions — superseded

- Reader value: understand the comparison instrument before process detail, then apply it to change and maintenance decisions.
- Affected files **if adopted later**: `OUTLINE.md`, `BOOK_BRIEF.md`, chapter briefs, cross-reference/word-budget plans, and any restored comparison/case documents. No such adoption happens in M0.
- Cost: twelve slots require a realistic M1 word budget and repetition audit; comparable examples and operational boundaries need additional planning.
- Risk: the actual outline may express stronger author choices; restoring it takes priority. The exact audience, domain and chapter count remain D01/D05/D06 decisions.
- Approval record required: adopt, amend or reject the candidate; identify its base document; record the change in `DECISION_LOG.md`. Do not blindly apply an add-file patch over a restored outline.
