# Audit report: servers/peoplesweb/web/index.html

Project: Website
Auditor: Website GPT auditor (Codex)
Proposer: Claude (Opus 5.5) for Nimrod Talmon (GCE), 2026-11-17, [audit PR #28](https://github.com/udi-shapiro/Grassroots-Audit/pull/28).
Date: 2026-11-17
GLP commit: e817b136f15a4c9d10cca4f105b86a7636ed7fa7

Scope: How the site shows a parametric contract.
Coverage: Read `notWhy` and `openBtn` in `servers/peoplesweb/web/index.html`, `has_platform` in `servers/peoplesweb/tools/build.py`, step 5 of `cascade.sh`, and `cascade/Ads/manifest.md`, `cascade/Auction/manifest.md` and `cascade/Networked-Organisation/manifest.md`. The site was not run.

## Finding 1: A parametric contract is shown as an app that is missing

Severity: low

Ads, Auction and Networked Organisation are parametric contracts, so by design no platform is compiled for them: each manifest says "a parametric contract has no realisation (GSC, Definition Parametric contract); its instances are compiled", and `cascade.sh`, step 5, says the same. The site shows them as it shows a contract the compiler refused: the pill "Not compiled", and on the contract's page "No app yet. The compiler printed no platform for it." (`notWhy`). A reader takes the three as unfinished.

Proposal: the build reads "Parametric" from the manifest, and the site shows such a contract as a template: a pill "Template", the sentence "A template: only the contracts that fill it in have apps", and links to them (for Auction, Second-Score Auction, which instantiates it).

### Answer

Website (Website #4), 2026-11-18, submitted by Audit #3: a parametric contract is now shown as a template, labeled Parametric, with the contracts that fill it in.

Corrected: [GLP main `64dfdc23188d9b67ff634c91dbc89aa9def88141`](https://github.com/EShapiro2/GLP/commit/64dfdc23188d9b67ff634c91dbc89aa9def88141) incorporates the [Website change `c860408958b94b4727039ee0c4e4e17f58918e65`](https://github.com/EShapiro2/GLP/commit/c860408958b94b4727039ee0c4e4e17f58918e65). [Original reply](https://github.com/udi-shapiro/Grassroots-Audit/pull/28#issuecomment-6977328109).

### Verification

2026-11-18, Website GPT auditor — **verified corrected in the checked build and rendering logic** at GLP main `64dfdc23188d9b67ff634c91dbc89aa9def88141`.

- Source inspection confirmed that the build sets `parametric` from the manifest's `Parametric:` line and that the UI distinguishes templates from compiler refusals. The app panel shows direct dependants under “Used by.”
- In a local fixture, Python ran the pinned manifest classifier and relationship parser against the committed manifests and Second-Score Auction text. Ads, Auction and Networked Organisation passed the classification checks. A concrete manifest and a missing manifest both classified as non-parametric. The parser identified Second-Score Auction as an Auction instance.
- Node ran the pinned badge and app-panel rendering expressions with the resulting data. All three templates displayed the Parametric badge and template explanation, without “No app yet.” Auction linked to Second-Score Auction. A compiler refusal retained its explanation and a live contract retained the Open link.

These checks exercised extracted source with fixture inputs. The full website build, browser navigation and live deployment were outside this verification. [Audit evidence and source pins](https://github.com/udi-shapiro/Grassroots-Audit/blob/7ba37269ccf76c37b817dab04dfa6740e7a2790e/auditor/stages/14-pr28-parametric-20261118.json).
