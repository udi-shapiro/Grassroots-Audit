# Evidence for the first Stage 2 sweep

This directory belongs to the public `GPT-Auditor` continuity branch. Never merge that branch into audit `main`. Published reports link to the immutable commit containing this evidence.

The audit examined GLP main `7976014a5f9b5fefc33abcc922d491abc41dfad5` and papers `fb269c2a16e42bf505e37274106e54e8a1c04bbb`. See `sweep-scope.json` for what was read, executed, blocked or left unexamined. A downloaded file is not automatically an audited file.

`GLP-source-snapshot.zip` contains 15 exact source files, including every input needed by these checks, with their original paths and verified Git blob hashes. `archive-manifest.json` lists them and the archive hash. `source-manifest.json` records all 19 fetched files; the large template and three READMEs are referenced by source commit and hash rather than copied here. This is a selective snapshot, not a full GLP checkout. `pdf-manifest.json` records the two PDFs preserved here. The earlier GLP-Spec and IGLP PDFs are preserved at commit `d769c65447a7a849bdc916c262979d69c1b37dc8`, under `auditor/evidence/glp-20261112/`.

From the root of a checkout of this evidence commit, with Python 3, Bash and Perl installed, run:

```sh
python3 -m zipfile -e auditor/evidence/stage2-sweep-20261112/GLP-source-snapshot.zip auditor/evidence/stage2-sweep-20261112
python3 auditor/checks/stage2-sweep/formal_semantics.py
python3 auditor/checks/stage2-sweep/gsn_contract.py auditor/evidence/stage2-sweep-20261112/GLP
python3 auditor/checks/stage2-sweep/pragma_boundary.py auditor/evidence/stage2-sweep-20261112/GLP
```

The corresponding recorded outputs are `formal-semantics-result.json`, `gsn-contract-result.json` and `pragma-boundary-result.json`. All assertions passed. The first is a deliberately restricted model of finite, unguarded paper rules; its type witness is a recorded manual derivation, not an automated type-checker result. The second calculates selected declarative schema steps and compares certificate metadata. The third executes the actual source's Bash/Perl pragma reader with positive and negative controls. None executes Dart, a GLP compiler, the transaction protocol or a phone application.

The current vGLP and GSC PDFs could not be downloaded through the available routes. VMAT was read through the explicitly versioned arXiv HTML. These limits remain open; they are not inferred successes.
