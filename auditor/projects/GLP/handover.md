# GLP auditor: first formal-semantics scope

Date: 2026-11-12
GLP main: `7976014a5f9b5fefc33abcc922d491abc41dfad5`
Papers branch inspected: `fb269c2a16e42bf505e37274106e54e8a1c04bbb`

## Read first

Read ../../coordination.md, ../../stages.md, the accepted main plan, and `papers/GLP-Spec.pdf.md` with subsequent answers. The exact read scope and source blob IDs are in ../../stages/02-glp-scope.json. Preserved PDF bytes are under ../../evidence/glp-20261112/; verify their recorded SHA-256 digests before reading.

## Established

The initial formal finding uses `p(f(X?), X).` and the goal `p(Y,Y?)`. Both meet the untyped definitions' SO/SRSW and renaming conditions. Their writer MGU exists, but reader/pair completion requires a finite term T=f(T), which is impossible by term height. Under reader erasure, ordinary finite-term LP unification fails the occurs check. GLP-Spec 2.6/2.11 and proof E.1 need to address this domain gap. IGLP 3.5–3.8 repeat the definitions.

The independent Python certificate in ../../checks/pair-completion.py verifies the finite-term calculations and a noncyclic control. It is not an emulator of the runtime and is not evidence of compiler acceptance. The report carries one high-severity paper finding, not a runtime finding.

## Implementation and execution limits

Examined relevant parts of bytecode/runner.dart, runtime/commit.dart and runtime/heap_fcp.dart. The runner contains occurs/own-reader checks for repeated head writers; the heap detects some pointer cycles. These checks alone do not settle the paper's general substitution domain or the end-to-end example. No Dart or Flutter SDK was available; no typed program or Dart test was executed. The typed-front-end behavior is explicitly unresolved. No GLP code was modified.

## Next

1. Finish publishing the prepared report and record the PR and commit.
2. Read GLP's response to the example. Verify any new restriction or term domain against both the definitions and the LP-correspondence proof. Preserve attributed answers and the finding number.
3. Examine TGLP's admissibility rules and obtain a supported Dart execution environment before claiming the typed runtime accepts or rejects the example. A type restriction can repair the paper's general statement only if its scope is stated and its preservation justified.
4. Continue the GLP audit with clause/guard failure and suspension semantics and the scheduling/refinement obligations. Keep those results separate from this single counterexample. Later review remaining paper sections, type checker/compiler and multiagent correspondence; they are not covered yet.

This work was performed in the coordinating conversation, not a separately running persistent process. Monitoring is not active.
