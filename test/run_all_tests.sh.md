# Audit report: test/run_all_tests.sh

Project: Code
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: c40e6d3ad68b198066ab723d17c05171c0a7de76

Scope: A single audit record for `KNOWN_RED_CHECKS`, as requested by Udi. This is an inventory and reporting policy, not a new defect report or a new full-suite execution.
Coverage: Parsed the exact-name array and read `_known_red_check`, `_check_pass` and `_check_fail`. The array has **23 distinct entries**: three APPS checks and twenty SG checks. [Machine-readable registry](https://github.com/udi-shapiro/Grassroots-Audit/blob/d61f8d3f6520ec0ef665d3a7030a517beda982ba/auditor/evidence/currencies-gsa-20261112/known-red-registry.json). The source advance to `8f6cf17a63a956fa41a0184648cba0882a40ed32` changes GFF's APPS label elsewhere; this array is unchanged.

A listed failure increments the known-red count and does not fail the suite. A listed success fails the rot guard until the obsolete entry is removed. Matching is by exact check name. Report these acknowledged reds here once; component reports link here and do not create new findings for each affected app or assertion. An unlisted failure retains its harness classification, but several assertions caused by one defect still do not become several findings.

| Source comment's group | Entries | Recorded dependency / responsibility |
| --- | ---: | --- |
| GAI/GSNP compilation transition | 3 | GnW joint-guardian compilation limitation; vGLP ruling/dependency and GAI's apps |
| CSSN super-app port | 11 | GSG's hosting port |
| Retired handwritten CSSN/childsafe fixtures | 9 | GSG's port of replaced/deleted examples, recorded while the project was dormant |

The group labels above summarize the source comments; they do not reassign project ownership. These are historical named checks, not 23 new audit findings.

### GAI/GSNP GnW compilation transition

```text
APPS gai: platform.vglp is what vGLP's compiler prints from GAI.glp
APPS gsnp: platform.vglp is what vGLP's compiler prints from GSNP.glp
APPS gai: platform.vglp is the platform of the recorded run of the cascade on GAI
```

### CSSN super-app port

```text
SG two mini-apps at once: bob connected and greeted under it
SG two mini-apps on two smartphones: and its message arrives
SG super-app hosts the child-safe platform: alice connected to bob
SG super-app hosts the child-safe platform: bob connected and greeted
SG super-app hosts the child-safe platform: no failed play
SG two mini-apps at once: alice connected under the child-safe platform
SG two mini-apps on two smartphones: the child-safe friendship holds
SG child-safe platform on two smartphones: alice is connected to bob
SG child-safe platform on two smartphones: bob is connected to alice
SG child-safe platform on two smartphones: alice's message reaches bob
SG two mini-apps at once: no failed play
```

### Retired handwritten CSSN/childsafe fixtures

```text
SG super-app: cssn's artefact is refused a certificate
SG super-app: load_file gives cssn's artefact as text
SG super-app: the super-app installs no text
SG super-app: the child-safe platform's artefact is certified
SG two mini-apps at once: alice's swap settles
SG two mini-apps at once: bob's swap settles
SG two mini-apps on two smartphones: the currency's conversation opens
SG two mini-apps on two smartphones: alice's swap settles
SG two mini-apps on two smartphones: bob's swap settles
```

### Relationship to published findings

[Application integration Finding 1](../programs/apps/compile.sh.md) remains the single report for the observed contract/platform/load integration gap, with acknowledged limitations distinguished from additional observations. The earlier APPS run's 183 pass / 60 ordinary fail / 3 known red counts stay pinned to that run; no new SG or full-suite totals are asserted here. The complete list above also covers the SG names, even though those twenty entries were not rerun in the currency/GSA sweep.

The new GB escrow and GSA certificate cases are distinct semantic checks, absent from this registry. They are not relabeled known-red suite failures. No test expectations or source allowlist entries were changed by the auditor.
