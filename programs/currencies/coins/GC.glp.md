# Audit report: programs/currencies/coins/GC.glp

Project: Currencies
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: c40e6d3ad68b198066ab723d17c05171c0a7de76

Scope: GC.txt against its seven schemas, the committed GC app and the recorded GC cascade. Application contracts/code only; no currency or core paper review.
Coverage: Read the complete contract and schemas, app declarations, scripted plays and currency phone certificate; parsed the actual schema terms for asset and guard checks; executed `bash cascade.sh gc --check` with Dart 3.9.4 on Ubuntu 24.04, enforcing the committed dependency lockfile.

| Clause | Schemas / implementation | Result in this scope |
| --- | --- | --- |
| Inherited GKK | `establish`, `acquaint`, `introduce` | Identity and knowledge prerequisites retained |
| GC:1 Minting | `mint` | Only the issuer's own coins added; issuer guards |
| GC:2 Swap | `swap` | Both parties guard; mutual knowledge; both amounts and issuers preserved in the exchange |
| GC:3 Payment | `pay` | Payer guards; payer knows payee; payee receives its own coins |
| GC:4 Redemption | `redeem` | Bearer guards; one issuer coin returned for one coin held by the issuer; no issuer veto introduced |
| GC:5 Pricing | Undertaken clause, no schema | Not represented as a machine-enforced pricing promise |

The [parsed-source checks](https://github.com/udi-shapiro/Grassroots-Audit/blob/d61f8d3f6520ec0ef665d3a7030a517beda982ba/auditor/checks/currencies-gsa-20261112/currency-source-checks.py) confirm that all seven GC schemas occur unchanged in GB; every non-mint asset transfer balances by issuer, amount and instrument; and GC's signed phone list names exactly its seven concrete app schemas. These checks assume the schemas' positive-whole-number multiplicity domain. They are not a runtime proof that malformed amounts are rejected.

The [actual cascade replay](https://github.com/udi-shapiro/Grassroots-Audit/actions/runs/43327789171) reproduces all recorded artifacts and all four plays byte-for-byte under the driver's normalization: payment/swap, redemption, contention, and refusal. See [the cascade report](../../../cascade/GC.md) and [the app report](../../apps/gc.md).

No new finding in this bounded GC scope. Remaining work includes malformed/zero/negative amount inputs, broad concurrent executions and failure recovery, physical-phone behavior, and the economic claims of the papers. Passing replay establishes reproducibility of these examples, not solvency or complete correctness.
