# Audit report: programs/currencies/bonds/GB.glp

Project: Currencies
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: c40e6d3ad68b198066ab723d17c05171c0a7de76

Scope: GB.txt against its 22 schemas, the committed app and recorded cascade, with an executable escrow witness and refusal control.
Coverage: Read all clauses and schemas, the calendar/maturity path, app scripts and recorded artifacts. Parsed the source terms to check inheritance, symbolic asset balances, guard sets and date constraints. Ran the unmodified recorded cascade check and the compiled app with audit-only scripts. Evidence, commands and checks are [preserved](https://github.com/udi-shapiro/Grassroots-Audit/tree/d61f8d3f6520ec0ef665d3a7030a517beda982ba/auditor/evidence/currencies-gsa-20261112). No paper investigation or live financial transaction was performed.

## Finding 1: The enforced escrow clause does not encode its beneficiary or condition

Severity: medium

[GB:5](https://github.com/EShapiro2/GLP/blob/c40e6d3ad68b198066ab723d17c05171c0a7de76/programs/currencies/bonds/GB.txt#L17) is marked **enforced**. It describes a deposit with Carol for Bob on a condition agreed by the three, release to Bob when that condition holds, or return to Alice when it fails.

The six [escrow schemas](https://github.com/EShapiro2/GLP/blob/c40e6d3ad68b198066ab723d17c05171c0a7de76/programs/currencies/bonds/GB.glp#L264) encode ordinary bilateral transfers. Their state contains only `identity`, `knows`, `coin` and `bond`; their constraint is `true`. No deposit identifies a beneficiary or condition, no escrow record distinguishes deposited funds from Carol's other holdings, and no release or return references a deposit or agreement. The `u` argument is the asset's issuer, not its beneficiary. The source comment explicitly places the beneficiary and condition in an agreement held by the escrow agent; that explains the implementation but leaves part of the enforced clause outside it.

In the [typed app execution](https://github.com/udi-shapiro/Grassroots-Audit/actions/runs/43328151573), Alice deposits two Alice-coins and two Alice-bonds of maturity 10 with Carol. Carol then acquaints Dave and requests `release_c(carol,dave,alice,1)` and `release_b(carol,dave,alice,10,1)`. Dave consents. Both commit at date 1. The last views show one coin and one bond at Dave and one of each remaining at Carol. No beneficiary, escrow agreement or condition was supplied at any step. If the off-machine agreement had named Bob, this same machine trace could not distinguish it from one naming Dave. The test does not purport to supply an agreement through an input the program lacks.

The refusal control has Dave answer **no** to the same coin release. It records `refused(...,dave,declined)` and keeps both coins and bonds at Carol. Thus the bilateral consent guard works; the missing enforcement is the connection to the agreed escrow. The existing `play_bonds` still loads and reaches its deposit after the witness scripts are added. No production schema or platform logic was changed.

The village script's wait until the escrow agent's day 30 is a scripted person's choice; it does not install a date-30 condition in the escrow schemas. An external condition may legitimately require a trusted person's judgment or attestation, but that boundary must be explicit. Either represent the agreement, beneficiary and relevant authorization/evidence in the enforced protocol, or revise the clause/modality to say precisely which obligations the escrow agent undertakes outside the machine. Do not describe the current arbitrary bilateral transfers as enforcing the entire agreement.

### Answer

Awaiting Currencies' dated answer with a `Corrected:` or `See:` reference.

### Verification

2026-11-12 — Reproduced on the compiled GB app at the pinned source with Dart 3.9.4. Both instrument transfers succeed; the refusal control blocks the transfer. Source-term inspection finds no agreement state or constraint in any of the six escrow schemas. Finding open.

### Other checked properties and limits

GC's seven schemas are inherited exactly. All non-mint instrument transfers conserve their symbolic issuer/maturity/amount totals. Both swap parties guard; only the bearer guards redemption. Bond minting requires maturity strictly later than the issuer's recorded date. A presented bond is redeemable at maturity equality or later, using **the issuer's** date; a bond taken in exchange need not be mature. `first_date` and `advance` are unguarded; the latter increments the recorded date by one without passing the calendar's day. These are source checks, not proof of a trustworthy device clock.

The [GB cascade](../../../cascade/GB.md) reproduces, but its manifest explicitly contains no execution run. The [app report](../../apps/gb.md) distinguishes the app plays from that absent cascade run. Amount-domain validation, arbitrary scheduling/failure recovery, external-condition attestation and economic solvency remain outside this sweep.
