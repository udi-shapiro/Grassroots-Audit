# Audit report: servers/peoplesweb

Project: Website
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: f68fbcbc3ef91b9707037ef7e5dfdb302acd1458
Other source versions: Papers branch `f4ae6121866387641f2941e3e9bf46e5fd964e7d`; previous baseline main `7976014a5f9b5fefc33abcc922d491abc41dfad5`.

Scope: The updated project/contract ownership map and paper artifact inventory.
Coverage: Executed current directory/paper registry modules over the complete pinned tracked-path fixture; verified all 64 reused owner headers against unchanged Git blob identities. This is metadata/placement coverage, not substantive review of all projects or a check of the deployed site.

## Updated baseline

The source now lists **31 projects in PROJECTS**, of which 20 hold 27 paper keys, plus **six named support projects in NO_PAPER**: Code, Coordination, Website, Audit, Phones and GCE. These give 37 assignments, not 37 active sessions. All 64 contracts occur exactly once; the source map reports no tree faults or uncovered top-level/shared-container entries.

The 11 added project rows are GBM, CFRI, IVMAT, GFWC, CDWC, GPW, Secure-GLP, P99, DDD, KYC and LBM. Their unpresented papers are not assigned invented keys. GFWC, GPW and P99 now hold their directories under their project rows. Currencies' AGORA directory also sits beside its papers. The source still assigns `programs/lbm` to GRH; the separately listed LBM project does not silently acquire it. GNA's paper remains held by GSA even where a directory's legacy responsibility label is GNA.

`servers/peoplesweb` now explicitly belongs to Website. The transfer announced in the previous baseline is complete. The [build-cache finding](peoplesweb/tools/papers_sync.py.md) follows that ownership. The Earlier papers list still has 11 entries outside the project roster, awaiting a project responsibility decision.

## Current paper artifacts

There are **26 built PDFs for the 27 project paper keys**. VMAT, CGP, GPBD and CGMS now have built artifacts; SRC now maps to `papers/SRC.pdf`. The distinct GGGA draft is not presented/built by the current registry. Entries below identify versions, not completed reads.

| Project | Paper key | Artifact at the pinned papers commit |
| --- | --- | --- |
| GLP | GLP-Spec | [`papers/GLP-Spec.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/GLP-Spec.pdf) |
| GLP | TGLP | [`papers/TGLP.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/TGLP.pdf) |
| GLP | IGLP | [`papers/IGLP.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/IGLP.pdf) |
| VMAT | VMAT | [`papers/VMAT.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/VMAT.pdf) |
| vGLP | vGLP | [`papers/vGLP.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/vGLP.pdf) |
| sGLP | sGLP | [`papers/sGLP.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/sGLP.pdf) |
| GSC | GSC | [`papers/GSC.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/GSC.pdf) |
| GSA | GSA | [`papers/GSA.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/GSA.pdf) |
| GSA | GNA | [`papers/GNA.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/GNA.pdf) |
| SPM | SPM | [`papers/SPM.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/SPM.pdf) |
| Currencies | GC | [`papers/GC.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/GC.pdf) |
| Currencies | GB | [`papers/GB.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/GB.pdf) |
| Currencies | SGC | [`papers/SGC.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/SGC.pdf) |
| Currencies | GCC | [`papers/GCC.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/GCC.pdf) |
| GAI | GAI | [`papers/GAI.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/GAI.pdf) |
| CSSN | CSSN | [`papers/CSSN.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/CSSN.pdf) |
| GFF | GFF | [`papers/GFF.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/GFF.pdf) |
| GGGA | GGGA | Draft not presented/built by current registry; await an accessible version |
| GGGA | SRC | [`papers/SRC.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/SRC.pdf) |
| GO | GO | [`papers/GO.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/GO.pdf) |
| GRH | GRH | [`papers/GRH.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/GRH.pdf) |
| CGP | CGP | [`papers/CGP.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/CGP.pdf) |
| GPAT | GPAT | [`papers/GPAT.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/GPAT.pdf) |
| GPBD | GPBD | [`papers/GPBD.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/GPBD.pdf) |
| DSA | DSA | [`papers/DSA.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/DSA.pdf) |
| CCDG | CCDG | [`papers/CCDG.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/CCDG.pdf) |
| CGMS | CGMS | [`papers/CGMS.pdf`](https://github.com/EShapiro2/GLP/blob/f4ae6121866387641f2941e3e9bf46e5fd964e7d/papers/CGMS.pdf) |

## Evidence and history

The [reproduced hierarchy and blob manifest](https://github.com/udi-shapiro/Grassroots-Audit/blob/bbf5e90e34c28e1a77697df696365238a47b5b02/auditor/stages/02-core-structure.json) and [check](https://github.com/udi-shapiro/Grassroots-Audit/blob/bbf5e90e34c28e1a77697df696365238a47b5b02/auditor/checks/core-20261112/structure.py) preserve the current result. The complete earlier baseline remains at [its original commit](https://github.com/udi-shapiro/Grassroots-Audit/blob/10aafafb23ba73afda468ce1e2003d1ce8d4daa9/auditor/stages/01-source-baseline.json); its earlier counts and missing PDFs are historical observations, not current blockers.

GLP's papers publisher replaces the branch with a parentless commit. The seven PDFs actually examined in Stage 2 are therefore preserved in [the audit evidence](https://github.com/udi-shapiro/Grassroots-Audit/blob/bbf5e90e34c28e1a77697df696365238a47b5b02/auditor/evidence/core-20261112/papers), with their exact hashes. Other artifact links above still need byte preservation when substantively audited. The metadata fixture does not execute project code. No new ownership-map finding is asserted.
