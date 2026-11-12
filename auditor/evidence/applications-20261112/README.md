# First application contract/code sweep — 2026-11-12

Source: EShapiro2/GLP main at `5c17c4aa069743d990d993ca23c65200df982754`. All 2,530 extracted source files were checked against Git blob IDs from that source tree. The source ZIP was obtained by read-only Actions run 43316846386; its 20 MB archive is not duplicated here. The required CSSN model inputs are retained under sources/; other inputs remain available at the immutable source commit, with hashes in the results. sha256.json hashes the saved evidence.

## Results

- Original build run 43316846386: five exact platform reproductions (gkk, gsg, gsn, gc, gb); refusal for gsnp, gai, gff and cssn. Both scripts exit 1, no timeout.
- Follow-up run 43318139408: the diagnostic-only print patch exposes all refusal reasons; unchanged APPS suite finishes in 310 seconds, exit 1, 183 pass / 60 fail / 3 known red counted separately. The original complete log is in application-tests.zip; application-tests/summary.json gives every ordinary check name. The 60 failed assertions are not 60 independent defects.
- Targeted run 43319256439: all four affected committed app directories fail direct loading. GAI/GSNP: typed scripted-person incompatibilities; GFF: obsolete menu syntax; CSSN: duplicate Expr alternative. Interactive REPL exits 0 after errors and :quit; inspect the logs, not just exit status. No timeout.
- cssn-rules.py: actual source terms, two bounded reachable failing traces and successful controls. This is a declarative calculation, not GLP/phone execution. The first local auditor parser attempt accidentally selected a procedure declaration; selecting the fact line fixed the auditor script. That attempt is not a GLP failure.
- app-certificates.py: seven phone/platform static comparisons. GAI and GSNP mismatch; gkk/gsg/gc/gb agree. GSN repeats its existing, separately tracked finding at this main pin; its proposed branch correction was already verified and is not counted anew.

## Reproduction

With the pinned GLP checkout as GLP:

```sh
python3 cssn-rules.py GLP
python3 app-certificates.py GLP
cd GLP/glp_runtime
dart pub get --enforce-lockfile
cd ..
bash programs/apps/compile.sh --check
bash programs/cssn/compile.sh --check
GLP_SECTIONS=APPS bash test/run_all_tests.sh
```

The three workflow sources under auditor/checks/applications-20261112 pin dependencies/actions and document the exact commands. Execution branch audit-applications-20261112 is never merged into main. No GLP source was changed remotely. Diagnostic print instrumentation affects only a disposable checkout.

## Limits and continuation

No physical devices or Flutter tests; no full application state-space, economic/security proof or current AI-attestation semantic validation. Passing historical plays do not validate changed contracts. CSSN and GAI/GSNP are the initial substantive application focus; GFF compilation and GC/GB existing test coverage are narrower. Current GAI:2 attestation-to-key/developer binding needs a separate semantic review before any claim of a fault. No such finding is asserted here.

Core papers remain on hold until all six existing core findings have answers. This sweep did not read or alter those papers/reports. Continue application contract/code work and verify project responses without routine user go-aheads. No persistent project workers or background monitoring are running.

## Final source check

GLP main advanced to 3a9fa6842264e10bb9529fd5bdc05226163fca20. source-final-delta.json records all intervening commits/changed paths and the exact two corrected GSC blobs now integrated. The current application's five new findings are unaffected by that comparison. The APPS numeric results above remain at 5c17c4a, before the new GSN expected-output lines. No new paper review or whole-suite re-execution is implied.
