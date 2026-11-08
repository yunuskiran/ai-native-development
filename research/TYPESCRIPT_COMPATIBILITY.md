# TypeScript / Node.js compatibility — M2 documentary assessment

Prepared: **2026-11-01**. Evidence snapshot: **2026-10-31, Australia/Melbourne**. The author chose TypeScript / Node.js; framework, database, host/model and exact versions remain unselected. This note examines source requirements, not an installed or tested common environment. [Claims](evidence/CLAIMS.json); [source receipts](evidence/SOURCE_RECEIPTS.json).

## Keep three dependency layers separate

1. **Method distribution/engine:** the software needed to install or run the framework.
2. **Coding host/model:** dispatch, hooks, context metrics, permissions and provider access.
3. **Application stack:** the Node/TypeScript compiler, web framework, database and test pipeline used by the case.

A method's installer minimum is not automatically the application's target runtime, and host support is not equivalent feature coverage. Shared language alone does not establish matched conditions.

## Documentary compatibility matrix

| Scope | Inspected requirement or boundary | Interpretation / unresolved work |
|---|---|---|
| BMAD stable source | Manifest Node >=20.12.0; README additionally names Python/uv. Build benefits from worker/reviewer capabilities. | B-C01; [B01](M2_SOURCE_LEDGER.md#m2-b01), [B03](M2_SOURCE_LEDGER.md#m2-b03), [B10](M2_SOURCE_LEDGER.md#m2-b10). No TS application starter or host behavior was executed. |
| GSD Core research source | Install guide says Node 18+; same-pin engines say Node >=24 and npm >=10. Host adapters have documented capability differences. | G-C03/G-C04. Treat the higher manifest declaration as a constraint to investigate, not as a completed installation check. Source pin differs from release tag. |
| AWS Workflows source | Native installer/engine does not require Node/Bun; manual-copy path differs. | A-C07. This says nothing conclusive about the SaaS runtime; do not force every method engine to share its implementation language. |
| AIUP core / combined Node adapter | Core artifacts feed a NestJS/Drizzle/PostgreSQL backend and Next.js App Router; tests include Docker-backed database paths. | U-C04. This is a documented native TypeScript path, not an approved stack or actual working installation. |
| Node runtime | Official release table identifies Node 24 as LTS at the snapshot. Version-24 docs separately describe TypeScript stripping and its limits. | T-C01/T-C02. A candidate major can meet the Core source floor; exact patch and package compatibility are not frozen. |
| Nest application vs CLI | Official guide distinguishes app requirements from higher CLI-generator requirements, including a Node 24.15+ CLI path. | T-C03; [W17](M2_SOURCE_LEDGER.md#m2-w17), Prerequisites. A broad “Node 24” label alone is not a complete generator requirement. |
| Next.js / TypeScript | Snapshot docs state minimum Node 20.9 and TypeScript 5.1. These are documentation floors, not chosen package pins. | T-C03; [W18](M2_SOURCE_LEDGER.md#m2-w18), System requirements / Set up TypeScript. Adapter compatibility with particular releases remains untested. |
| Decorator/test compilation | TypeScript documents metadata emission; AIUP's adapter identifies metadata-transformer requirements for its backend tests. | T-C04; [U02](M2_SOURCE_LEDGER.md#m2-u02), [U07](M2_SOURCE_LEDGER.md#m2-u07), [W19](M2_SOURCE_LEDGER.md#m2-w19). No compiler configuration was run. |

## Candidate, not an adopted run freeze

**Research recommendation:** evaluate a maintained Node 24 patch satisfying the actual CLI/package requirements, alongside a pinned TypeScript/compiler/test toolchain. This candidate follows the inspected release status and source constraints; it does not establish runtime equivalence. Node 26 is also shown as LTS in the snapshot table, but no automatic upgrade choice is made. Recheck supported patches and exact dependency requirements at the eventual run freeze.

Direct execution of `.ts` files must not be substituted for the adapter's build/test pipeline. Node's lightweight stripping does not perform static typechecking, ignores `tsconfig` behavior and does not supply the decorator transformation required by the documented adapter path (T-C02). Keep compilation/typechecking, tests and acceptance as distinct records.

Two case-design options remain reviewable:

- Use the documented native Node adapter stack as a common application stack across all four methods, with neutral scaffolding and equal acceptance requirements. This introduces UI/database/test dependencies that must earn their place in the book's bounded example.
- Keep a smaller framework-neutral Node interface and explicitly adapt the AIUP construction path. Record that adaptation and its cost as part of the intervention; do not call it the unchanged native adapter.

Neither option is silently adopted. The approved domain and TypeScript family remain intact. No install command, global configuration, paid model access, server or deployment was executed in M2.

## Readiness still required

Before any matched execution: select source-vs-release policy and exact method/plugins; resolve GSD's runtime discrepancy; choose the common host/model and record capability exceptions; pin compiler/framework/database/test packages; freeze a neutral scaffold and independent oracle; then demonstrate unscored setup for each selected profile. ER05/ER06 remain unpassed. A documentary matrix cannot replace those checks or establish security/production readiness.
