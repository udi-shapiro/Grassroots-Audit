# Audit report: programs/social/graph/GAS.glp

Project: GSA
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: c40e6d3ad68b198066ab723d17c05171c0a7de76

Scope: GAS.txt's store/list/trust/install clauses against GAS's added schemas, and the route from a store listing to a host installation.
Coverage: Read the contract and added schemas, the GPD installation requirements, Home/host entry points and the recorded GAS manifest. Reproduced the GAS cascade record and searched the complete pinned `programs`, `glp_runtime`, `glp_multiagent` and `test` trees for `install_from_store`, `trusts_store` and the local certificate producer. [Evidence](https://github.com/udi-shapiro/Grassroots-Audit/tree/d61f8d3f6520ec0ef665d3a7030a517beda982ba/auditor/evidence/currencies-gsa-20261112/gsa).

| Step | Representation at the pinned source |
| --- | --- |
| Open store | `open_store` requires the guardian/service relationship and adds `store` |
| List program | `list` checks the owner's trust in the program's author, signs the item and adds a listing; listing is an undertaken clause |
| Trust/distrust store | `trust_store`/`distrust_store` maintain Alice's store trust; initial trust checks knowledge of the store and guardian |
| Install from store | `install_from_store` requires a trusted store, the current listing and no existing installation; copies the signed item and adds `installed(Alice,item_of(z))` |
| Executable store platform | Absent: the recorded CVA output is `%% not compiled(gas)` |
| Home-to-host bridge | Home installs a local filename and manufactures a certificate; no executable store-listing retrieval/installation bridge was found in the searched implementation |

The install schema does **not** recheck the owner's continuing trust in the developer. This agrees with GAS:4 as written: installation depends on the store being trusted and the program being listed. It is not reported as a missing prerequisite.

The current record is a 34-schema contract/checker/VMAT result followed by a compiler refusal, with no compiled GLP or run. `cascade.sh gas --check` exits 0 because that refusal is exactly the recorded artifact. See [the cascade report](../../../cascade/GAS.md). Consequently, this sweep cannot validate an end-to-end App Store install path. The abstract `installed` state has not been shown here to cause host registration of a verified module.

This is recorded as an implementation/coverage gap, not an additional discovery for every dependency blocked by the same compilation limitation. The independently demonstrated certificate-path fault is [agent.glp Finding 1](core/agent.glp.md). Completion should be evidenced by an executable path from a received listing to the correct installed module, with refusal cases for wrong source/code, invalid certification and untrusted-store provenance. The shared [known-red registry](../../../test/run_all_tests.sh.md) retains the suite's acknowledged failures once.
