# Audit report: papers/TGLP.pdf

Project: GLP
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: f68fbcbc3ef91b9707037ef7e5dfdb302acd1458
Other source versions: Paper key TGLP; papers commit `f4ae6121866387641f2941e3e9bf46e5fd964e7d`; PDF blob `3906a08d72e2afdf9c8c8c0c3f0293eac191ccc1`; SHA-256 `9d8558b3d4561967ae61bb31695c75a22d138cd5b5c03f24cb5e464edea64347`; [preserved PDF](https://github.com/udi-shapiro/Grassroots-Audit/blob/f41ab3efdb7511e870452dd1b95df85e7b45ee14/auditor/evidence/stage2-sweep-20261112/TGLP.pdf).

Scope: Stage 2: whether the type rules exclude the existing finite pair-completion counterexample.
Coverage at first publication (extended below): Read Sections 2, 4 and 5, including the operational rules, strict well-typing, input coverage and preservation/soundness proof. Visually checked the clause-typing definition. The derivation below is a paper-rule derivation, not a type-checker result. Parameterised/module typing and the remaining appendices require further audit.

## Related open finding: GLP-Spec, Finding 1

This extends [GLP-Spec Finding 1](GLP-Spec.pdf.md#finding-1-pair-completion-has-no-finite-fixed-point-for-an-admissible-writer-match); it is not a second count of that fault.

The following uses a closed, productive regular type, with no wildcard:

```prolog
T ::= a ; f(T).
procedure p(T, T?).
p(f(X?), X).

% Initial goal:
p(Y, Y?)
```

Under Definition 45 (Moded Head), the head becomes `p(up:f(up:X), down:X?)`. Its two variable positions have dual types T and T?; its paths are consistent with the declaration. Thus Definition 49's head condition and head-head pair condition hold, and the empty body satisfies its body condition. The second argument is the only input: its complemented head reader accepts every input path at the root, so Definition 412's input coverage holds. The initial goal puts its writer at output T and reader at input T?, again dual. These are the type rules printed on pp. 10–13, not an inference from runtime behavior.

The writer match is still `{Y := f(X?), X := Y?}`, whose pair completion requires a finite T0 satisfying `T0 = f(T0)`. Typing by the recursive type T does not produce such a finite term. TGLP Definition 25 repeats the fixed-point completion, and Sections 2 and 5 use it for outcomes and soundness.

The existing finding therefore cannot be dismissed merely by invoking these well-typing rules. Any proposed type-based exclusion must identify an additional stated restriction and its preservation argument. Record the shared repair and project response under GLP-Spec Finding 1, then check its consistency here. At first publication typed compiler acceptance had not been tested; the dated follow-up below closes that gap.

## Follow-up coverage, 2026-11-12

The same PDF blob was verified at papers commit `f4ae6121866387641f2941e3e9bf46e5fd964e7d`. Read further in Appendix C.3, the parameterised rules in D, module definitions and expansion in E, and the beginning of F (through the start of F.2). This remains a partial review of parameterised/module proofs, not their completed verification.

Actual typed acceptance and execution now confirm the earlier derivation: [GLP-Spec Finding 1's runtime evidence](GLP-Spec.pdf.md#executed-typed-runtime-evidence-2026-11-12). The finite control succeeds, and the paired goal is accepted and creates a cyclic structure in the runtime. Keep the response and finding number in that report. No additional independent finding is counted here.

### Rebuilt-paper check before publication

The republished PDF at papers commit `ccdd5433d72286571c065a28a0efb4cb2b151957` has different PDF bytes but identical `pdftotext -layout` output to the examined version. The [preserved refresh](https://github.com/udi-shapiro/Grassroots-Audit/tree/b2693dc4e5a41bd4a8386915af9bca5efd98ac50/auditor/evidence/core-refresh-20261112/papers) therefore introduces no changed extracted definitions or proof text for this report. This is text-identity verification, not a pixel comparison.
