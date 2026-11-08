# AI Unified Process — M2 source dossier

Status: **research-editor extraction; independent technical review pending**. Access: 2026-10-31. This examines the core and a specific TypeScript/Node construction path, not all adapters as interchangeable. [Claim register](../evidence/CLAIMS.json); [source ledger](../M2_SOURCE_LEDGER.md).

## Identity and source/component versions

Research source: `AI-Unified-Process/marketplace` at `3ad51b0707e9bed6e54b9de46ebc2f28d7afa960`. The combined Node plugin manifest identifies `aiup-nestjs-nextjs` `0.9.0` (U-C05). The repository's latest-release endpoint returned the component tag `aiup-nestjs-nextjs-v0.8.1`, resolving to `24fc9fda…` (V-C02). This is not an umbrella semantic version for the method, nor proof the main snapshot is installed by a release command.

The website and core workflow describe requirements/use cases across inception, elaboration, construction and transition. The earlier public publisher/author material identifies Simon Martinelli with the method; individual adapter manifests have contributor attribution. Do not confuse method authorship, component authorship and repository copyright. A complete first-publication history remains outside established evidence here.

## Workflow, artifacts and decisions

The workflow's artifact map connects requirements, models, use cases, optional processes/test journeys, architecture/decision records and acceptance/release documents (U-C01). Stable references are conventions; actual link completeness still requires checking.

Layered stacks explicitly distinguish agent-alone choices, ask-first issues and prohibited unilateral edits (U-C02). Those defaults are expressly scoped to layered orchestration. The combined Node implementation has its own instructions: reconcile existing features in place, preserve unrelated behavior, add migrations instead of rewriting applied ones and keep implementation separate from test generation (U-C07). Do not extend a rule from one path to every adapter.

## F01–F11 evidence map

All runtime/effectiveness outcomes are **Not assessed**.

| Dimension | Documentary finding or explicit gap | Evidence / qualification |
|---|---|---|
| F01 Decision rights | Layered orchestration has explicit authority categories; combined Node implementation separately constrains edits. | U-C02/U-C07; [U01](../M2_SOURCE_LEDGER.md#m2-u01), L339–L357; [U09](../M2_SOURCE_LEDGER.md#m2-u09), L47–L79. Not one universal adapter policy. |
| F02 Overhead/scale | A durable artifact chain is documented; precise minimal tiny-task procedure/effort was not established here. | U-C01/U-C08. **Not assessed** for overhead; avoid assigning a penalty from document count. |
| F03 Artifact lifecycle | Specs change before downstream reconciliation and are committed with source. | U-C08; U01 L475–L487. Retention is a policy, not proven alignment. |
| F04 Traceability | Stable requirement/use-case/rule/test references and code markers are defined. | U-C01; U01 L113–L136. Correctness and completeness untested. |
| F05 Context | Construction inputs select linked requirement rows, entity model and applicable conventions/decisions. | U01 L319–L337. Quality of chosen context not measured. |
| F06 Solo/team | Artifact producer/consumer and team decision-right records make responsibility inspectable. | U01 L48–L66/L339–L357. Real team coordination effects unassessed. |
| F07 Brownfield | Reverse engineering yields a proposed baseline needing gap/contradiction resolution; Node path reconciles existing code. | U-C08/U-C07. Recovered behavior not independently validated. |
| F08 Testing | Spec lint and semantic review are different; Node tests use unit and real-database API paths. Node coverage-auditor limitation is explicit. | U-C03/U-C04/U-C06; [U07](../M2_SOURCE_LEDGER.md#m2-u07), L22–L32. Generated tests are not our frozen oracle. |
| F09 Operations | Transition covers human acceptance/user/release records. Comprehensive deployment/rollback evidence not established here. | U-C09; U01 L419–L447. **Not assessed** for production operation. |
| F10 Portability | Core has stack-independent artifacts; selected Node construction depends on specific application technologies and Docker tests. | U-C04; [U02](../M2_SOURCE_LEDGER.md#m2-u02), L9–L26/L82–L88. Host/stack execution untested. |
| F11 Maintainability | Specification-first changes, stable IDs and in-place reconciliation are prescribed. | U-C07/U-C08. Long-term synchronization and cost outcomes unassessed. |

## TypeScript/Node implications and documented limitations

The combined adapter assumes NestJS, Drizzle/PostgreSQL and Next.js App Router; it also documents module-import and decorator-metadata concerns (U-C04). Author selection of TypeScript/Node does not itself adopt that full stack. A common-stack choice must be deliberate and applied equally; a custom adapter would be a different intervention with its own effort recorded.

The workflow explicitly states that the combined Node plugin does not yet ship the coverage auditor available through certain other adapters (U-C06). Preserve this qualification when discussing traceability; core terminology alone cannot establish identical automation on every stack. Spec-review's deterministic lint and advisory semantic review also have different blocking authority (U-C03).

For the case, map CS requirements to original use cases and policies; do not borrow the Apress sample application or promote an agent-generated coverage assertion to independent acceptance. The website's spec-anchored self-classification is attribution, not demonstrated drift prevention (S-C02).

## Rights, independence and review handoff

[U05](../M2_SOURCE_LEDGER.md#m2-u05) and [U06](../M2_SOURCE_LEDGER.md#m2-u06) provide Apache-2.0/NOTICE evidence. Component-specific attribution and actual reused assets still need review. Publisher full text was not supplied/purchased; public scope cannot certify complete originality. No external prompts, code or figures are copied here.

Before pilot prose: choose component source-vs-release scope, review the Node limitation and stack decision, preserve core/adapter boundaries and obtain G2 technical review. No controlled AIUP advantage over the other methods was established by this research.
