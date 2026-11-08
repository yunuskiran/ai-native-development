# 1. The Evolution of AI-Assisted Development

> Author manuscript · completed 2026-11-05 · C01 · Documentary method accounts and synthetic teaching examples. Source and execution scope are summarized in the front matter and source notes.

<!-- C01-S01 -->
## A bounded history, with dates

A developer asks an assistant to add an approval button. The assistant changes a component, adds an endpoint and writes a test. The screen looks convincing. Before accepting the change, someone still has to answer a less visible question: who is allowed to approve whose request?

That question is the starting point of this book. Producing an implementation and establishing that the implementation is acceptable are different kinds of work. An AI system may participate in both. A team needs a way to connect them.

Four selected sources help frame the change in scope. On June 29, 2021, GitHub announced the technical preview of Copilot, describing assistance that proposed lines and functions using the surrounding code. This is one historical marker for a particular product, rather than a founding date for AI-assisted programming. [GitHub's announcement](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/)

In October 2022, Yao and colleagues introduced ReAct, which interleaved reasoning with actions that obtained information from an external environment. Its tasks included question answering and interactive decision making. This supplies an example of a research pattern for acting and observing, not an organization-level software delivery process. [ReAct, first-version metadata and abstract](https://arxiv.org/abs/2210.03629v1)

The 2024 SWE-agent paper described a system for navigating repositories, editing files and executing programs through an interface designed for a language-model agent. It gives us a concrete software-engineering example of delegated actions and feedback. Its benchmark results do not measure the four frameworks compared in this book. [SWE-agent, first-version metadata and abstract](https://arxiv.org/abs/2405.15793v1)

On July 31, 2025, AWS introduced its AI-Driven Development Life Cycle in an article that described AI preparing plans and artifacts across inception, construction and operations, with people validating consequential decisions. That article supplies a primary statement of the proposed lifecycle. Its claims about faster delivery remain the publisher's claims. [AWS's original AI-DLC article](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/)

These anchors concern a product preview, research patterns and a proposed lifecycle. They are different units of evidence, not consecutive generations of one system. They do not establish that ReAct caused the frameworks' development, or that every team passed through the same stages. Code suggestions, delegated changes and coordinated workflows can coexist in one project.

The useful historical question is therefore specific: what work does a source say the system undertakes, under what conditions, and what remains for someone else to decide? A feature announcement can establish that a vendor described a capability at a particular time. It cannot, by itself, establish widespread adoption, a productivity improvement or the disappearance of a human responsibility.

We will use this selective history to distinguish changes in the boundary of work delegated to a system. The founding histories of the four frameworks and broader adoption trends need separate evidence; these anchors do not establish either.

<!-- C01-S02 -->
## From assistance to delegated work

Consider three instructions a developer might give an AI system:

1. Complete this validation expression.
2. Add the request-approval behavior and show the changes.
3. Investigate the requirement, propose an implementation plan, make the change and assemble evidence for acceptance.

These are illustrative instructions, not records of executed sessions. Each delegates a different boundary of work. The first leaves the surrounding decisions with the developer. The second gives the system room to choose a design. The third also delegates parts of investigation, planning and verification.

As that boundary expands, more assumptions can enter the result. An approval endpoint needs a rule for the actor, the target request and the current state. A plan needs a view of which behavior is already agreed and which behavior remains undecided. A verification report needs a reason to treat its checks as relevant to the requirement.

For this book, we will describe delegation through those concrete responsibilities rather than assign a single autonomy label to an entire project. Who may edit files? Who may settle an ambiguous business rule? Who may accept a test failure? Who may merge or release? Different answers can apply to the same assistant in different tasks.

A methodology becomes relevant when it gives these activities a repeatable arrangement: how work starts, what records carry decisions, when people intervene, how checks are performed and how changes are reconciled. The editor, terminal or coding host is part of the execution environment. It can enable or restrict that arrangement, but its presence does not tell us which arrangement the team follows.

That distinction defines the comparison in the rest of the book. BMAD Method, the selected GSD lineage, AWS AI-DLC and AI Unified Process (AIUP) are the four framework subjects. Spec-Driven Development (SDD) is a cross-cutting approach whose meaning and artifact policies require separate examination. A tool can implement pieces of several approaches. Counting it as another peer methodology would obscure the question we are trying to answer.

### Follow the responsibility as the work changes shape

Imagine asking an assistant to explain a failing lookup in an existing repository. The immediate output is an explanation that an engineer can test against the code. If the engineer instead asks a tool-using agent to investigate and repair it, the expected work may now include choosing files, running commands, interpreting results and changing a query. The business intent is the same, but the agent has more opportunities to act on an incorrect assumption before someone inspects it.

The engineering record needs to match that wider assignment. “Fix the lookup” gives the agent little basis for deciding whether to alter a shared query or add a check at one route. “A tenant B actor must be unable to retrieve a known A request, while A's authorized read must still work” gives the assignment a testable boundary. A record can also state that the approved change concerns a local repository and that release is a separate decision. With that information, the next engineer can tell where the assignment ends and which decision needs a person.

This example illustrates a distinction that applies throughout the book. Assistance can reduce the work of discovering and editing. Delegation asks the team to decide which judgments a tool may make along the way. The review question changes from “is this suggested line right?” to “did the work preserve the conditions we agreed to, and what evidence covers that claim?” Both kinds of work can occur in the same session.

<!-- C01-S03 -->
## Responsibilities that need owners

Our running example is a small vendor-access approval service. A requester asks for a vendor to receive temporary access; an eligible person in the same customer organization decides the request. The service records the decision. It does not provision access in another system. This is the book's synthetic case, with requirements defined in the [case specification](../../CASE_STUDY_SPEC.md).

Suppose the requester also holds an administrator role. May that person approve the request? In this case, the answer is no. That is a product rule, CS-05. A framework may help elicit the rule or carry it into a plan. A generated class cannot establish the organization's desired rule merely by implementing one interpretation.

We will use an explicit ownership record when discussing this case:

| Responsibility | Decision the case needs | Proposed owner in the exercise |
|---|---|---|
| Product intent | Self-approval stays forbidden when roles overlap | Author acting as product decision owner |
| Technical design | Where and how the chosen implementation enforces the rule | Implementing engineer, with technical review |
| Acceptance | Which positive and negative observations would establish the agreed behavior | Acceptance reviewer, independent of the implementation output |
| Change control | Whether a new approval policy applies to existing requests | Product decision owner, recorded before the change episode |
| Operation | What evidence would justify running and supporting the service | Assigned operator and release owner in a future operational exercise |

These are proposed duties, not a completed staffing record. One person may hold several duties, but the record should expose that overlap. An AI-generated review does not create an independent human reviewer.

The ownership question matters even when an answer appears obvious. If an assistant infers that administrators can do everything, the resulting code may be internally consistent and still violate CS-05. If it infers that a new policy applies retroactively, a technically successful migration may change promises already made to users. Those are hypothetical failure paths we can investigate, not incidents observed in this project.

### Describe authority before choosing a workflow

A practical delegation brief can fit in a few sentences. The engineer authorizes investigation of a reproducible defect in a local branch. The assistant may inspect source, edit the affected implementation and run the existing checks. The product owner retains the decision about externally visible behavior where the current contract is ambiguous. The release owner retains the decision about using the resulting artifact in a stateful environment. The brief also identifies the observation that would make the investigation useful.

This division can change during work. An investigation may reveal that the reported defect comes from a deliberate rule. A local repair may expose a migration need. The contributor should record that discovery where it affects the next action, along with the owner of any new decision. In this way, escalation becomes a specific request to settle a condition rather than a broad instruction to approve everything again.

Consider a generated recommendation to remove a validation guard. The implementation might become simpler, and the reported example might begin to pass. The delegation brief gives the reviewer a way to ask whether removing that guard changes an accepted boundary. The engineer can then inspect its callers and associated requirements before accepting the patch. The quality of that review depends on a retrievable rule and a relevant observation.

<!-- C01-S04 -->
## A maintenance change as a running question

Begin with a deliberately small change: repair an approval path that lets a requester approve their own item when they also have the approver role. This is an illustrative maintenance question. The repository does not yet contain that implementation or an observed defect.

The visible output might be a conditional check and a regression test. To assess it, we would first identify the decision being repaired. The intended rule is independent of which role labels the requester holds. The negative example starts with a pending request and an overlapping-role requester trying to approve it. A separate positive example starts with an equivalent pending request and an eligible, different approver in the same tenant. Keeping the starting state comparable prevents a terminal-state rejection from masquerading as evidence of the self-approval rule.

Next comes the boundary of the repair. Does the application expose one decision route or several? Is role membership checked when the decision is made? Could a foreign-tenant request be found through a direct identifier? These are questions for source inspection and the eventual acceptance contract. We do not know their answers before a baseline exists.

Finally, there is the evidence boundary. A test named `prevents self-approval` is a useful clue, but its assertion must exercise the forbidden action. A passing check of a hidden button would establish something about that interface; it would leave the server's decision behavior unresolved. In the planned case, acceptance includes business-interface checks for the rule.

The same maintenance request gives us several distinct artifacts: an agreed rule, a bounded change, a rationale for the chosen location and observations from relevant checks. A methodology can prescribe how those artifacts relate. Its value for this task remains a question to evaluate, including the effort required to prepare and maintain them.

This small example also prevents process size from becoming a proxy for rigor. A short repair may need a short record. A policy change affecting concurrent decisions and existing requests needs different investigation. We will ask whether each selected framework can express the appropriate amount of work, while retaining the obligations that matter for the change.

### Make the first maintenance question observable

Suppose a maintainer sees a report that an actor in B can retrieve a request owned by A. The first useful record identifies the observed path and the intended behavior. If the report contains only a screenshot of an error, the maintainer still needs a known A request, an eligible A identity, a B identity and a way to exercise the same request under both. A reproduction establishes what happened at a particular boundary before anyone proposes a repair.

Now consider what an agent could infer from the repository. It may find a data model with a tenant field and a helper used by most routes. Those are useful clues. They cannot settle the intended error or disclosure behavior if the owner never made that choice. A reviewer can authorize a narrow change after resolving the relevant part of the contract. Any broader decision about membership lifecycle or privilege inheritance can be handled separately.

Follow the change back to the original report after editing. If the direct lookup is corrected, inspect other consumers of the changed helper and see whether permitted access still works. Record which paths were exercised and what remains open. This small narrative provides the thread for later chapters: define a boundary, keep the decision available, and collect evidence at the place where the behavior can be observed.

<!-- C01-S05 -->
## What changed, what is uncertain

The central hypothesis of this book is that making intent, decision rights and acceptance evidence explicit can make AI-driven engineering easier to inspect and reproduce. It is a hypothesis to examine through documented mechanisms and bounded exercises. It is not an established performance advantage for any named framework.

Documentation can show that a workflow calls for a plan or review. It cannot show that the operator read the plan, that the review found the relevant defect or that the additional step justified its cost. A later execution record would need to establish those observations for its own conditions. Even a successful synthetic exercise would leave questions about teams, larger systems and longer maintenance periods.

We will therefore keep three kinds of statement distinct. A source may **prescribe** an activity. A recorded execution may **show** what happened in one run. An editorial argument may **recommend** a choice under declared constraints. Readers should be able to tell which kind they are reading without reconstructing the research process.

The evidence can challenge the thesis. If a framework adds artifacts that no one uses to make or check a decision, that is a cost worth recording. If a lightweight path preserves the necessary rule with less work, it deserves serious consideration. If a sophisticated review chain misses the relevant boundary, its existence cannot stand in for acceptance evidence.

We have not run the four-way case study. There is no measured winner, productivity multiplier or production-readiness result in this introduction. The comparison begins with questions whose answers could change our choices.

### Notice which part of engineering became cheaper to repeat

Consider a team investigating a fault in a reporting service. A suggested patch can be produced quickly, but the team still has to find out which customers encountered the fault, whether the report is relied on for reconciliation and which historical data the fix should affect. Those decisions involve evidence the repository may only partly contain. If a contributor can generate several plausible patches, the team needs an efficient way to distinguish their assumptions.

One investigation begins with a paired fixture. Reproduce an incorrect total and a correct total that could be broken by the same change. Ask the assistant to identify the query and its callers, then record the observations that led to a proposed repair. The team can discard two patches and retain the investigation because the accepted behavior and reproduction still apply. The useful intermediate product is an account another engineer can inspect without starting over.

This is why the book keeps returning to revision and context. In an ordinary review, two diffs with identical code may look equivalent. If one was checked against an old fixture, while the other has a current observation from the path the customer uses, they support different decisions. The distinction also applies to documents. A policy written yesterday may still govern the work if it remains accepted, while a test from an hour ago may already be stale because a query changed.

For an organization experimenting with AI assistance, a modest first question is whether a second engineer can recover the evidence for a change. Give them the accepted intent and the repository, and see whether they can find the decisive observation and its scope. The result can inform how the team writes handoffs. Productivity across projects would require a different study and a broader body of evidence.

### Read the next success claim with one question

When someone reports that an agent completed a change, ask which decision the evidence lets a reviewer make. A generated patch may be ready for inspection. A local test may justify continued integration. A reviewed boundary observation may justify accepting a specific behavior. A release decision may require a wider packet. The answer should identify the candidate and the observation.

Use this question while reading the method accounts. Locate the work each arrangement organizes and the point at which a person interprets its output. The same question will connect the documentary descriptions to the case, the assurance chapter and the final discussion of future evaluation.

<!-- C01-S06 -->
## Questions for the rest of the book

The next chapter develops a practical response to development driven mainly by successive plausible outputs. Chapter 3 establishes the vocabulary used to compare processes. The four method chapters then examine selected, dated profiles through their own artifacts and decision paths. Chapter 8 gives Spec-Driven Development its cross-cutting treatment.

Chapters 9 and 10 have different jobs. The comparison chapter asks what the evidence supports. The selection chapter asks what a team should do under stated constraints, including when a narrow practice or small repair path is enough. The case chapter is where planned exercises must become reproducible records or remain explicitly labeled walkthroughs.

Across those chapters, keep the approval button in mind. A convincing screen gives us something to inspect. The engineering work is to establish which decisions produced it, which behavior it owes its users, and what evidence supports accepting it.
