# Audit report: papers/VMAT.pdf

Project: VMAT
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: f68fbcbc3ef91b9707037ef7e5dfdb302acd1458
Other source versions: Paper key VMAT; papers commit `f4ae6121866387641f2941e3e9bf46e5fd964e7d`; PDF blob `18c4dd39c6a9f8bba390e936baf5254c3d3233ef`; SHA-256 `b12e7f63b26aa333a577ba4860866fcb43b09ed9d6ef6ab18faad21b9e44a807`; [preserved PDF](https://github.com/udi-shapiro/Grassroots-Audit/blob/bbf5e90e34c28e1a77697df696365238a47b5b02/auditor/evidence/core-20261112/papers/VMAT.pdf).

Scope: Stage 2: current foundations, containment, equivalence, liveness and their interface to the cascade.
Coverage: Read the current 28-page PDF, including its appendices, with focused checks of containment, countable transition classes, partial equivalence, if-then-else and protocol closure. This is a paper review, not an independent mechanisation of every proof or an execution of a VMAT implementation.

## Current-version reconciliation

This PDF supersedes the earlier preliminary reading of arXiv:2604.25596v2 (4 July 2026) recorded in PR #5, when the inspected papers snapshot contained no VMAT PDF. The older fallback is not used to assert a fault in the current cascade.

In particular, Appendix D explicitly waives a class's liveness obligation if any participant has stopped, whether or not that participant is a guard. The earlier question about stopped machine participants versus guarding persons is resolved at the definition level by this current text; it is not an open numbered finding.

No independent numbered fault is established in this pass. The current compilation interfaces still require the cross-project checks recorded in the IGLP, vGLP and sGLP reports. Reading this foundation does not validate those implementations or discharge their distinct proof obligations.

### Rebuilt-paper check before publication

The republished PDF at papers commit `ccdd5433d72286571c065a28a0efb4cb2b151957` has different PDF bytes but identical `pdftotext -layout` output to the examined version. The [preserved refresh](https://github.com/udi-shapiro/Grassroots-Audit/tree/b2693dc4e5a41bd4a8386915af9bca5efd98ac50/auditor/evidence/core-refresh-20261112/papers) therefore introduces no changed extracted definitions or proof text for this report. This is text-identity verification, not a pixel comparison.

## Proposed related work on volition guards

26 November 2026. We propose citing four precedents in the VMAT paper. They address distinct parts of the question: can a transaction depend on one or more people being willing for it to happen?

| Precedent | Where willingness enters the formal model |
| --- | --- |
| Nash [1] | In the two-person bargaining problem, each individual can withhold consent to an action affecting their own well-being. Mutual consent is a premise of the bargaining model. The object Nash derives is a bargaining outcome. |
| Myerson [2] | Each player $i$ independently lists the people $S_i$ with whom they wish to form a link. The link $ij$ forms iff $j\in S_i$ and $i\in S_j$. This gives a direct precedent for bilateral friendship formation. |
| Esparza and Desel [3] | A marking assigns each agent $a$ a set $x(a)$ of negotiations it is ready to enter. An atomic negotiation $n$ is enabled iff $n\in x(a)$ for every party $a\in P_n$. The outcome determines the parties’ subsequent readiness. This is the closest of the four to the set-membership test in VMAT. |
| Bartoletti and Zunino [4] | In BitML, a branch $A:D$ requires authorization by $A$. Their example allows Alice to authorize a withdrawal paying Bob, after which any participant may fire the branch. When the branch requires several authorizations, all must be present in the configuration. This is a direct precedent for naming the parties whose approval a contract act requires. |

**Suggested text for the paper.** Consent as a condition of joint action appears in Nash’s bargaining model [1]. Myerson gives an explicit bilateral rule for forming a social link from independently expressed choices [2]. Esparza and Desel give an operational rule requiring an atomic negotiation to belong to every party’s current readiness set [3]. BitML permits a contract branch to require authorization by designated parties [4]. In VMAT, a transaction $t$ specifies a set $Q$ of machine participants and a guard set $G\subseteq Q$ of persons. In addition to the machine precondition, execution requires $[t]\in V_p$ for every $p\in G$, where $V_p$ is that person’s current volitional state and $[t]$ is the transaction’s equivalence class. A person may change $V_p$ while the machine state stays fixed. This separates whose machine takes part, whose willingness is required, and whether that willingness still holds when the act occurs.

### References

1. John F. Nash, Jr. (1950). “The Bargaining Problem.” *Econometrica* 18(2), 155–162. See p. 155 for the consent assumption. [Original paper](https://www.rasmusen.org/GI/reader/12a.nash.bargaining.1950.pdf)
2. Roger B. Myerson (1991). *Game Theory: Analysis of Conflict*. Cambridge, MA, Harvard University Press, p. 448. The simultaneous link-announcement example is also restated with its set-membership rule in [Matthew O. Jackson’s survey](https://web.stanford.edu/~jacksonm/netsurv.pdf).
3. Javier Esparza and Jörg Desel (2013). “On Negotiation as Concurrency Primitive.” *CONCUR 2013 – Concurrency Theory*, LNCS 8052, 440–454. See the definition of an enabled atom under “Semantics.” [Original paper](https://www.fernuni-hagen.de/sttp/docs/2013onnegotiationasconcurrencyprimitive.pdf)
4. Massimo Bartoletti and Roberto Zunino (2018). “BitML: A Calculus for Bitcoin Smart Contracts.” *Proceedings of the 2018 ACM SIGSAC Conference on Computer and Communications Security*. See “Authorizations” in the operational semantics for the withdrawal example and the multiple-authorization rule. [Paper](https://eprint.iacr.org/2018/122.pdf) · [DOI](https://doi.org/10.1145/3243734.3243795)
