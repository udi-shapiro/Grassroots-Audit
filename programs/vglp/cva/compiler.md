# Audit report: programs/vglp/cva/compiler

Project: vGLP
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: 7976014a5f9b5fefc33abcc922d491abc41dfad5
Other source versions: The source files at the GLP commit above.

Scope: Stage 2: the accessible contract/pragma boundary and source availability for the compilation audit.
Coverage: Read the compiler README's pragma/form interface, the pragma reader's term handling, and the generated GSN schema/tab declarations. Executed the actual Bash/Perl reader with pinned inputs. The common text.glp template was fetched and searched for protocol entry points, not audited in full. The current vGLP PDF blob was identified but its bytes could not be retrieved with the available routes. No end-to-end compiler, two-phase commit, type checker or runtime result is claimed.

## Checks completed

The [boundary check](https://github.com/udi-shapiro/Grassroots-Audit/blob/f41ab3efdb7511e870452dd1b95df85e7b45ee14/auditor/checks/stage2-sweep/pragma_boundary.py) executes `pragmas.sh`, rather than a Python translation of its behavior. The [result](https://github.com/udi-shapiro/Grassroots-Audit/blob/f41ab3efdb7511e870452dd1b95df85e7b45ee14/auditor/evidence/stage2-sweep-20261112/pragma-boundary-result.json) records:

- GKK, GSG and GSN inheritance in their expected order.
- Successful parsing of GSN's pragmas with its schema term extracted from the pinned generated platform.
- Rejection of a controlled copy with the Post text field removed, naming the missing variable x.

Exploratory invocations without the schema term were rejected because the reader could not resolve act names. They are not counted as successful compilation checks. These boundary tests establish neither correctness of GSC-to-vGLP compilation nor correctness/liveness of its transaction protocol.

The inspected generated GSN platform preserves the source's group-delivery precondition and the `received_in` Posts tab. The resulting contract problem is tracked once, under [GSC's GSN report](../../gsc/GSN.glp.md), not duplicated as a compiler finding.

## Pending paper and execution coverage

The intended current paper is `papers/vGLP.pdf` at papers commit `fb269c2a16e42bf505e37274106e54e8a1c04bbb`, blob `3b9b0aa4d7587a289105184d039f3b85fcd396dd` (2,685,068 bytes). The connector's contents call returned an empty payload for this large PDF; its blob reader rejected binary decoding. Public download attempts were blocked. The older project attachment was not substituted for this version.

The next pass needs this exact paper (or a clearly identified successor), Dart execution, and a review of the generated transaction state machine against the paper's reservation, abort, commit and fairness obligations. No independent fault was established within this narrow vGLP boundary scope; the unexamined obligations remain open.
