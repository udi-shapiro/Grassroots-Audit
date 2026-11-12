# Audit report: programs/apps/compile.sh

Project: Code
Affected application projects: CSSN, GAI and GFF
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: 5c17c4aa069743d990d993ca23c65200df982754

Scope: Stage 3: reproducibility of the eight committed app platforms and CSSN's companion platform from their current contract sources.
Coverage: Executed both documented `--check` commands on Ubuntu 24.04 with Dart 3.9.4 and the enforced dependency lockfile. Inspected the scripts, relevant app documentation, contract sources and diagnostic output. A second run changed one diagnostic print statement in a disposable checkout to expose the compiler's complete refusal text; it changed no contract or compiler logic. The original commands, patch, results and logs are [preserved](https://github.com/udi-shapiro/Grassroots-Audit/tree/284f5316a1ade70083c364ed026a1dcba0329b5c/auditor/evidence/applications-20261112). No source changes were pushed to GLP. No core paper was reviewed.

## Finding 1: Four documented app rebuilds reject their current contracts

Severity: medium

The scripts and app READMEs describe the committed platforms as compiler output from the current owning contracts. At the pinned source, `bash programs/apps/compile.sh --check` exits 1; `bash programs/cssn/compile.sh --check` also exits 1. These are compiler refusals, not timeouts, dependency-install failures or merely formatting differences.

| Application | Result | Compiler diagnostic |
| --- | --- | --- |
| GKK | Exact committed output reproduced | — |
| GSG | Exact committed output reproduced | — |
| GSN | Exact committed output reproduced | — |
| GSNP | Not compiled | Local-specification rejection: `end_guardian`, `retire` |
| GAI | Not compiled | Local-specification rejection: `end_guardian`, `retire` |
| GC | Exact committed output reproduced | — |
| GB | Exact committed output reproduced | — |
| GFF | Not compiled | Effectiveness rejection: `deliver` |
| CSSN | Not compiled | Local-specification rejection: `make_parent`, `end_parent`, `retire` |

The [unaltered execution](https://github.com/udi-shapiro/Grassroots-Audit/actions/runs/43316846386) completed both commands in approximately 109 and 37 seconds respectively. [The diagnostic run](https://github.com/udi-shapiro/Grassroots-Audit/actions/runs/43318139408) identifies the rejected schemas. For GAI/GSNP/CSSN the compiler points to listed guarding roles and their opener/guard sets; for GFF it points to an unguarded schema whose first role cannot determine the needed values under its effectiveness check. These are the implementation's reported reasons, not an independent judgment of the held core-paper definitions.

The acknowledged dependencies in this historical table are now recorded once in [the shared known-red registry](../../test/run_all_tests.sh.md). They are context for this integration report, not new findings per app. The registry preserves exact check names and the source's group explanations; the additional CSSN/GFF observations and direct-load evidence remain part of this one integration finding.

Consequently, a passing play of the committed historical platform cannot validate the current contract-to-app correspondence. For example, the current GFF contract uses the overlay-based `deliver` schema, while its app README still describes the former `deliver_own`/`deliver_on` design. CSSN's README likewise describes 31 schemas, whereas the current instance contains 39. These are supporting examples of the same integration gap, not additional numbered findings.

Coordinate a versioned resolution with the affected app owners. Once the accepted contract/compiler combination is available, regenerate the platforms, align the app scripts and documentation, and require the documented checks to pass. Until then, explicitly label the committed platforms with the older contract version they implement. Do not silence the refusal checks or interpret historical app execution as validation of the revised contracts. The compiler may be correctly refusing unsupported contracts; this report requests a consistent application release, not removal of its safeguards.

### Answer

Awaiting Code's dated coordinated answer, with CSSN, GAI and GFF attribution where relevant, and `Corrected:` or `See:` references.

### Verification

2026-11-12 — All nine rebuild results above were obtained by actual execution at the pinned commit. Five reproduce; four remain blocked. No resolution received.

### Existing application tests

`GLP_SECTIONS=APPS bash test/run_all_tests.sh` completed in 310 seconds with exit 1: **183 passed, 60 failed, and three separately recorded known-red checks**. The harness counted 243 ordinary assertions; the known-red checks are outside that count. GKK (23), GSG (21), GSN (24), GC (56) and GB (27) had no failed assertions in this section. GSNP had 31 failures, GAI 15, GFF 13, plus the aggregate rebuild check failed. These are assertion counts, not 60 independent defects. Several failed assertions depend on unsuccessful app loading/certification, so their expected screen/boot output is absent.

The [test summary](https://github.com/udi-shapiro/Grassroots-Audit/blob/284f5316a1ade70083c364ed026a1dcba0329b5c/auditor/evidence/applications-20261112/application-tests/summary.json) preserves individual check names, and the [original test artifact](https://github.com/udi-shapiro/Grassroots-Audit/blob/284f5316a1ade70083c364ed026a1dcba0329b5c/auditor/evidence/applications-20261112/application-tests.zip) preserves the complete log and result. This is the existing APPS section, including its isolate-based boot fixtures, not execution on physical smartphones. CSSN is outside that section; its separate rebuild was tested above.

A targeted [load diagnostic](https://github.com/udi-shapiro/Grassroots-Audit/actions/runs/43319256439) also tried each of the four committed app directories directly, without regenerating platforms:

| Committed app | Observed load failure |
| --- | --- |
| GAI | Type errors in `person.glp`, including missing `authored/1` and `agent_acquaint/4` alternatives and incompatible view/menu types |
| GSNP | Related type errors in `person.glp` and `plays.glp` |
| GFF | Obsolete `social_menu` declaration rejected by the current widget syntax |
| CSSN | Duplicate `item_of/1` alternative in `Expr` |

The [full load logs](https://github.com/udi-shapiro/Grassroots-Audit/tree/284f5316a1ade70083c364ed026a1dcba0329b5c/auditor/evidence/applications-20261112/application-load) preserve those errors. Each interactive REPL process exited 0 after `:quit`; success was therefore assessed from the actual load output, which reports failure, rather than from its process exit code. Fixing only contract compilation will not suffice: the generated platform, declarations and scripted persons must load together, then the application assertions must be rerun. These load failures are further evidence of the application integration gap; the 60 downstream test failures are not promoted to 60 separate findings.

The rebuild comparison certifies only agreement with compiler output. It does not certify the contracts' mathematical claims, economics, security, or complete phone behavior. The broader application-project audit remains open.

### Source advance during the sweep

At publication, GLP main had advanced to `3a9fa6842264e10bb9529fd5bdc05226163fca20`, integrating the already verified GSN leader-receipt and certificate corrections and updating their GSN test expectations and cascade records. The CSSN/GAI/GSNP/GFF sources involved in this report, the compilation tools and runtime were unchanged in that comparison. The numerical suite results above remain results at `5c17c4a`; the later GSN test expectations were not rerun in this sweep. No held core-paper report was changed.


### Follow-up source observation, 2026-11-12

GLP main `8f6cf17a63a956fa41a0184648cba0882a40ed32` incorporates `2edb7ee` and `69c299b`: GFF's compile input changes from abstract GFF to GFF-I, and the corresponding APPS check label changes. This is a relevant correction attempt, observed after the pinned run above. It does not alter the currency/GSA inputs or `KNOWN_RED_CHECKS`. No new GFF rebuild/load run is claimed in the currency/GSA sweep, so the report does not treat the historical GFF refusal as a tested result on this newer head or claim the whole integration finding is repaired. Code's PR #11 status note says its coordinated answer will follow when corrected; it was not submitted as a formal answer to this finding.
