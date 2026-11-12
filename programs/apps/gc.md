# Audit report: programs/apps/gc

Project: Currencies
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: c40e6d3ad68b198066ab723d17c05171c0a7de76

Scope: GC's committed app against GC's schemas and its recorded cascade.
Coverage: Read the app README, `self.glp`, wrapper and scripted plays; compared concrete schema names with the contract and phone certificate. The app's `platform.vglp` is byte-identical to `cascade/GC/platform.vglp`, which was regenerated and checked in this sweep. All seven schema names match.

GC's [contract report](../currencies/coins/GC.glp.md) records the checked permissions and asset accounting. The [cascade report](../../cascade/GC.md) records four replayed examples. The app has its own `play_coins` and village scripts; these must not be confused with the four cascade plays. The prior [APPS execution](compile.sh.md#existing-application-tests), at `5c17c4a`, had 56 passing GC assertions; those are historical results, not a new APPS run in this sweep.

No independent new app finding in this scope. UI input validation, arbitrary interleavings and physical-phone execution remain untested here. Known-red suite entries are centralized in [the test registry](../../test/run_all_tests.sh.md), without per-app duplicate findings.
