# Audit report: servers/peoplesweb/web/index.html

Project: Website
Auditor: none; a proposal by Claude (Opus 5.5) for Nimrod Talmon, of the project GCE
Date: 2026-11-17
GLP commit: e817b136f15a4c9d10cca4f105b86a7636ed7fa7

Scope: How the site shows a parametric contract.
Coverage: Read `notWhy` and `openBtn` in `servers/peoplesweb/web/index.html`, `has_platform` in `servers/peoplesweb/tools/build.py`, step 5 of `cascade.sh`, and `cascade/Ads/manifest.md`, `cascade/Auction/manifest.md` and `cascade/Networked-Organisation/manifest.md`. The site was not run.

## Finding 1: A parametric contract is shown as an app that is missing

Severity: low

Ads, Auction and Networked Organisation are parametric contracts, so by design no platform is compiled for them: each manifest says "a parametric contract has no realisation (GSC, Definition Parametric contract); its instances are compiled", and `cascade.sh`, step 5, says the same. The site shows them as it shows a contract the compiler refused: the pill "Not compiled", and on the contract's page "No app yet. The compiler printed no platform for it." (`notWhy`). A reader takes the three as unfinished.

Proposal: the build reads "Parametric" from the manifest, and the site shows such a contract as a template: a pill "Template", the sentence "A template: only the contracts that fill it in have apps", and links to them (for Auction, Second-Score Auction, which instantiates it).

### Answer

### Verification
