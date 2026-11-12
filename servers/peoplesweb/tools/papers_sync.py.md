# Audit report: servers/peoplesweb/tools/papers_sync.py

Project: Website
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: 66732717819d4d200070c60ac2a46d6b2228131a
Other source versions: Original baseline at `7976014a5f9b5fefc33abcc922d491abc41dfad5`: `papers_sync.py` blob `88298dc4a060aa098492957fb19e4f7f4198eb3d`; `papers.py` blob `3743b1701993443a5260d7d31a0a7e74a30f934c`

Scope: Invalidation of the paper-build cache when the website's build configuration changes.
Coverage: Read `papers_sync.py` and its registry inputs, then exercised the real `main()` cache decision with offline fixtures replacing fetch, git, arXiv lookup and PDF generation. The positive control changes the paper repository commit. No network call, credential access, real LaTeX build, GLP source modification, or production deployment was performed. This is not a full audit of the build or deployment system.

Responsibility: Website in the current map; originally GSA. The transfer is recorded below.

Current status: **Verified resolved** at the GLP commit in the header. The original reproduction and answer remain below in chronological order.

## Finding 1: Build configuration changes do not invalidate a cached paper PDF

Severity: medium

At [lines 140–149](https://github.com/EShapiro2/GLP/blob/7976014a5f9b5fefc33abcc922d491abc41dfad5/servers/peoplesweb/tools/papers_sync.py#L140), a paper is rebuilt only when its repository HEAD differs from the saved HEAD or its target PDF is missing. The selected `SOURCES[key]['main']` and the `FIXES[key]` transformations are also build inputs, but neither participates in that decision or the saved build identity. They reside in the GLP website registry, separately from the paper's repository.

After an initial successful build, correcting the registry's selected main file or changing a transformation while the paper repository remains at the same commit leaves the earlier PDF in place. The hourly sweep does not repair this merely by pulling the changed GLP registry. The fault can keep an incorrect or superseded rendering published until the paper repository changes or the cached target is removed. A stale production PDF has not been demonstrated here; the faulty cache decision has been reproduced.

### Reproduction

Run the [offline reproduction script](https://github.com/udi-shapiro/Grassroots-Audit/blob/10aafafb23ba73afda468ce1e2003d1ce8d4daa9/auditor/checks/paper-build-cache.py) against a checkout of GLP at the original baseline commit `7976014a5f9b5fefc33abcc922d491abc41dfad5`:

```sh
python3 paper-build-cache.py /path/to/GLP
```

The fixture writes a text payload in place of a PDF so that the chosen inputs can be inspected. It does not replace the cache decision. The results were:

| Event | Total build calls | Output |
| --- | ---: | --- |
| Initial build at source commit A | 1 | `first.tex`, no transformations |
| Change main file to `corrected.tex`, keep A | 1 | Still `first.tex` |
| Add a transformation, keep A | 1 | Still no transformations |
| Change source commit to B | 2 | `corrected.tex` and the transformation |

The changed-source control confirms that the fixture can rebuild. Exact source blob IDs and observed results are in the [recorded execution](https://github.com/udi-shapiro/Grassroots-Audit/blob/10aafafb23ba73afda468ce1e2003d1ce8d4daa9/auditor/stages/01-cache-reproduction.json).

The cache identity should include the selected source file and transformations, together with the source revision and any other configuration that changes the generated output. Verification should cover unchanged inputs (reuse), each changed build input (rebuild), and preservation of the last successful PDF when the replacement build fails.

### Answer

Awaiting the responsible project's dated answer and a `Corrected:` or `See:` reference.

Website (Website #1), 2026-11-12, submitted by Audit #1.

Corrected: [GLP 026e121a00a7f6c4bdb603a2187d104d2dadc026](https://github.com/EShapiro2/GLP/commit/026e121a00a7f6c4bdb603a2187d104d2dadc026), on the branch `Website`.

### Verification

2026-11-12 — Finding reproduced against the pinned source using the offline fixture. No correction has been received or verified; the finding remains open.

### Ownership transfer and current-source reproduction, 2026-11-12

The current `directories.py` assigns `servers/peoplesweb` to Website, completing the transfer declared when this report was first published under GSA. Finding 1 follows the path to Website without renumbering.

Re-executed the cache probe against `f68fbcbc3ef91b9707037ef7e5dfdb302acd1458`, `papers_sync.py` blob `621e6354b71668bd33316143815a9147235ce214`. The build count remained 1 after changing the configured main file and remained 1 after changing FIXES; changing the source revision raised it to 2. The current working-directory/build changes do not alter this cache decision. [Result](https://github.com/udi-shapiro/Grassroots-Audit/blob/bbf5e90e34c28e1a77697df696365238a47b5b02/auditor/evidence/core-20261112/cache-recheck.json). External git/build/arXiv operations were deterministic fixtures; this checks the actual cache orchestration, not a real LaTeX build. No correction verified; Finding 1 remains open.

### Correction verification after PR #6, 2026-11-12

**Verified resolved for the reported cache-configuration fault.** Preserved Website's attributed answer from [PR #6](https://github.com/udi-shapiro/Grassroots-Audit/pull/6), now merged. The cited correction adds the selected main file and FIXES to a persisted recipe and compares it before reusing a PDF. Its source blob `80840182bd3b03efc205e975293be16507e5924a` is also present on GLP main at `66732717819d4d200070c60ac2a46d6b2228131a`; the answer's original “Website branch” location is retained as submitted.

The same independent cache probe now records build counts 1, 2, 3, 4 after initial build, main-file change, FIXES change and source-revision change, respectively. Additional controls verify reuse when unchanged, rebuild of a legacy state lacking a recipe, retention of the old PDF and recipe on a failed rebuild, and successful retry with error clearing. [Results](https://github.com/udi-shapiro/Grassroots-Audit/blob/bbf5e90e34c28e1a77697df696365238a47b5b02/auditor/evidence/core-20261112/cache-correction.json) and [controls](https://github.com/udi-shapiro/Grassroots-Audit/blob/bbf5e90e34c28e1a77697df696365238a47b5b02/auditor/evidence/core-20261112/cache-correction-controls.json) identify the checked bytes. This verifies cache orchestration with external git, LaTeX and arXiv calls replaced by deterministic fixtures; no claim about deployment or a live paper build is made. Earlier same-day open observations above precede this response and remain as history.
