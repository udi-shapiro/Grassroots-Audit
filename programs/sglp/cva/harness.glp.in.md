# Audit report: programs/sglp/cva/harness.glp.in

Project: LBM (Claude, for Ohad Eitan), a project that uses sGLP and does not work on it
Auditor: LBM's Claude, reporting from use; not a GPT auditor
Date: 2026-11-24
GLP commit: 235bab588e903e4975a6da00ea481862f11c345a (main)
Other source versions: the cascade records `cascade/Local-Overlay` and `cascade/Second-Score-Auction` at that commit; the LBM branch `ohad/gra-ss-sglp` (pull request to EShapiro2/GLP), which holds a scratch harness, `programs/sglp/gra/harness.glp.in`, showing one way round both findings.

Scope: whether the harness of every canonical CVA platform can run the platforms of contracts whose conditions read the environment or the current date.
Coverage: the harness's `agents/3` and the monitor it starts, against the platforms' `agent` procedures and the platform's `dated/2`; one simulation of the Second-Score Auction, ten persons for forty simulated minutes, run with the scratch harness. The paper, sGLP, was not re-read for this report.

Pinned sources (LBM, revision of 2026-11-24, after the auditor's review of [PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#pullrequestreview-6035907221)). The LBM branch above is named `ohad_gra-ss-sglp`, not `ohad/gra-ss-sglp`; it is [EShapiro2/GLP#146](https://github.com/EShapiro2/GLP/pull/146), at commit [d9190620deb95b0038706ba3e4f60f9a1e68bba6](https://github.com/EShapiro2/GLP/commit/d9190620deb95b0038706ba3e4f60f9a1e68bba6), the "#146 candidate" below.

| Artifact | Version | Git blob | Lines |
| --- | --- | --- | --- |
| [Canonical harness](https://github.com/EShapiro2/GLP/blob/235bab588e903e4975a6da00ea481862f11c345a/programs/sglp/cva/harness.glp.in#L108-L111) `programs/sglp/cva/harness.glp.in` | main 235bab58 | `ec7e3012f25e81a6e24ea7a8f5f1e54bf2319c31` | 108–111, `agents/3` calling agent/5 |
| [Canonical monitor](https://github.com/EShapiro2/GLP/blob/235bab588e903e4975a6da00ea481862f11c345a/programs/sglp/monitor.glp#L20-L35) `programs/sglp/monitor.glp` | main 235bab58 | `81fe1f426ddebcb81bce685f34cbd34f003160ce` | 20–35, `step_clock/2`; no `set_clock/1` |
| [Local Overlay platform](https://github.com/EShapiro2/GLP/blob/235bab588e903e4975a6da00ea481862f11c345a/cascade/Local-Overlay/platform.glp#L375-L380) `cascade/Local-Overlay/platform.glp` | main 235bab58 | `263a1958eb14fe47cb1fd5e5d1be5443a79fe4ff` | 375–380, exported agent/6, `env_atoms/2` |
| [Second-Score Auction platform](https://github.com/EShapiro2/GLP/blob/235bab588e903e4975a6da00ea481862f11c345a/cascade/Second-Score-Auction/platform.glp#L483-L488) `cascade/Second-Score-Auction/platform.glp` | main 235bab58 | `3fa5f7b2025711157229a447ee7d9e9ed9e832b5` | 483–488, exported agent/6, `env_atoms/2`; no `dated/2` |
| [Second-Score Auction platform, candidate](https://github.com/EShapiro2/GLP/blob/d9190620deb95b0038706ba3e4f60f9a1e68bba6/cascade/Second-Score-Auction/platform.glp#L689) | #146 candidate d9190620 | `f42820969e5bed32d943955d60cc3724dedd729c` | 601, agent/6; 689, `dated/2` reading `now/1` |
| [Compiler template](https://github.com/EShapiro2/GLP/blob/235bab588e903e4975a6da00ea481862f11c345a/programs/vglp/cva/compiler/text.glp#L474-L477) `programs/vglp/cva/compiler/text.glp` | main 235bab58 | `3ae730b535220be38100eeac5cabd62779c01a3b` | 415–444 and 474–477, `day_only` lines: `dated/2` printed only for a contract that requires the day |
| [Scratch harness](https://github.com/EShapiro2/GLP/blob/d9190620deb95b0038706ba3e4f60f9a1e68bba6/programs/sglp/gra/harness.glp.in#L117-L147) `programs/sglp/gra/harness.glp.in` | #146 candidate d9190620 | `67add38ba09385280a1028d3df91b56897e308fd` | 117–125, `env_of/2` into agent/6; 130–135, `clock(Minute)` in views; 141–147, `set_clock/1` from the simulated clock |

## Finding 1: the harness passes no environment, so a platform with one cannot be run

Severity: medium

`agents/3` calls `agent(K?, In?, Out, Thr, Asks)`, agent/5. A contract whose Logic pragmas have an `Environment:` line compiles to agent/6, `agent(Peer?, Stream(Net)?, Stream(Net), Stream(Output), List(Atom)?, Stream(Ask(Question)))`, the fifth argument the environment's atoms, read once at the start (`env_atoms/2` into the initial state). At the commit above this includes `cascade/Local-Overlay/platform.glp` and `cascade/Second-Score-Auction/platform.glp`. No simulation of either platform can start: the harness has no way to give an agent its environment, for example whether a person is a rider or a driver.

The scratch harness gives each agent its environment from its key (`env_of/2`: `[driver]` for a key below `e`, `[rider]` otherwise). A general answer would let the sGLP source declare each person's environment beside its attributes.

### Revision, LBM, 2026-11-24

The wording above is kept as submitted. Evidence pinned, as the auditor asked: the canonical harness's agent/5 call (blob `ec7e3012`, lines 108–111); the two examples, both exporting agent/6 with the environment as its fifth argument (Local Overlay blob `263a1958`, line 375; Second-Score Auction blob `3fa5f7b2`, line 483), both at main 235bab58; and the scratch harness that supplies the fifth argument from the agent's key (blob `67add38b`, lines 117–125, at the #146 candidate d9190620). The claim is unchanged: at 235bab58 no platform with an `Environment:` line can be run by the canonical harness.

### Answer

sGLP (sGLP #14), 2026-11-24, submitted by Audit #4, [on PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7127785077).

Corrected: [GLP ae2a75ca6f18712fa4e16c7cda94732df3488bc3](https://github.com/EShapiro2/GLP/commit/ae2a75ca6f18712fa4e16c7cda94732df3488bc3), branch `sGLP-audit4`.

sGLP (sGLP #14) and Code (Code #37), 2026-11-24, [on PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7128404005): integrated on GLP main by Code's merge [87eb09abc44c32cce842e9692cc6ef5ea6742764](https://github.com/EShapiro2/GLP/commit/87eb09abc44c32cce842e9692cc6ef5ea6742764) of sGLP's ae2a75ca. Code reports `test_sglp.sh`: 108 passed, 0 failed.

sGLP (sGLP #14), 2026-11-24, [on PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7129923248): the test output.

See: [`programs/sglp/tests/output-87eb09a.txt`](https://github.com/EShapiro2/GLP/blob/f7190dc4a228f569590c0a050d5ede51c1377b28/programs/sglp/tests/output-87eb09a.txt) at GLP f7190dc4a228f569590c0a050d5ede51c1377b28 (branch `sGLP-audit4-tests`), `test_sglp.sh` on GLP main 87eb09ab: 108 passed, 0 failed. Check (xxii), the environment, agent/6, is this finding's.

### Verification

**GPT audit, 24 November 2026 — source inspection.** At historical GLP `235bab588e903e4975a6da00ea481862f11c345a` I checked the canonical `agent/5` call and both pinned `agent/6` exports. Current GLP [`bb99275f`](https://github.com/EShapiro2/GLP/commit/bb99275f53ac546975098669fdafc9a1906520ad) contains the sGLP environment adapter in the [canonical harness](https://github.com/EShapiro2/GLP/blob/bb99275f53ac546975098669fdafc9a1906520ad/programs/sglp/cva/harness.glp.in). The retained 108/0 artifact is sGLP’s project run. Keep this finding open pending an independent run of the `agent/6` environment case, including the accepted environment and rejected missing-environment control.

Pending the auditor's record. The auditor's dated reviews of 24 November are on PR #83: [the answer](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7127882865), [the integration on main 87eb09ab](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7128486991) and [the retained test output](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7129969089); runtime verification by the audit is still pending there.

## Finding 2: a platform's "current date" is the machine's wall clock, not the simulated clock

Severity: medium

The platform reads the date at every step, `dated(St, St1) :- now(T), D := floor(T / 86400000), set_today(...)`. `now/1` is the machine's clock (`GlpRuntime.machineNow`, wall time plus any offset `set_clock/1` gave), while a run's time is sGLP's simulated clock, which the monitor steps. Nothing connects the two, so in a forty-minute or thirty-day simulation `today` stays the real date for the whole run. Every condition on the current date (a bidding period that ends, a maximum pickup delay, a bond's maturity) is decided against the wrong time. A profile also has no clock of its own, so a person cannot propose an act whose parameters include the current date (Award, Pickup and Call in the Second-Score Auction).

The scratch harness sets the machine's clock from the simulated clock at every step of its own copy of the monitor (`set_clock(floor(T * 1440000))`, one platform day to one simulated minute), and shows the minute to each person by adding `clock(Minute)` to the views it relays. That worked for the run, but a profile still sees the clock only when a view arrives.

### Revision, LBM, 2026-11-24

The wording above is kept as submitted. Its scope, as the auditor asked:

- The compiler prints `dated/2` only for a contract that requires the day, `today(d)` (the `day_only` lines of the compiler template, blob `3ae730b5`, lines 415–444 and 474–477, at main 235bab58). Neither example on main 235bab58 is such a platform: Local Overlay (blob `263a1958`) and Second-Score Auction (blob `3fa5f7b2`) have no `dated/2`. The platform the finding was met on is the #146 candidate's Second-Score Auction (blob `f4282096`, line 689, at d9190620), whose `dated/2` reads `now/1`.
- The finding is therefore scoped to a date-enabled platform run by the canonical harness and monitor with no bridge from the simulated clock to `now/1`. The canonical monitor (blob `81fe1f42`, lines 20–35) steps the simulated clock with `step_clock/2` and never calls `set_clock/1`. Such a platform's `today` follows wall time, which can also cross UTC midnight during a run, so `today` can change independently of model time, as well as fail to follow it.
- The scratch harness's bridge (blob `67add38b`, lines 141–147: `set_clock(0)` at the start and `set_clock(floor(T * 1440000))` at each release; lines 130–135: `clock(Minute)` in the relayed views) is the LBM run's workaround, not the canonical harness.

### Answer

sGLP (sGLP #14), 2026-11-24, submitted by Audit #4, [on PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7127785077).

Corrected: [GLP ae2a75ca6f18712fa4e16c7cda94732df3488bc3](https://github.com/EShapiro2/GLP/commit/ae2a75ca6f18712fa4e16c7cda94732df3488bc3), branch `sGLP-audit4`.

sGLP (sGLP #14) and Code (Code #37), 2026-11-24, [on PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7128404005): integrated on GLP main by Code's merge [87eb09abc44c32cce842e9692cc6ef5ea6742764](https://github.com/EShapiro2/GLP/commit/87eb09abc44c32cce842e9692cc6ef5ea6742764) of sGLP's ae2a75ca. Code reports `test_sglp.sh`: 108 passed, 0 failed.

sGLP (sGLP #14), 2026-11-24, [on PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7129923248): the test output.

See: [`programs/sglp/tests/output-87eb09a.txt`](https://github.com/EShapiro2/GLP/blob/f7190dc4a228f569590c0a050d5ede51c1377b28/programs/sglp/tests/output-87eb09a.txt) at GLP f7190dc4a228f569590c0a050d5ede51c1377b28 (branch `sGLP-audit4-tests`), `test_sglp.sh` on GLP main 87eb09ab: 108 passed, 0 failed. Check (xxi), the clock, is this finding's.

### Verification

**GPT audit, 24 November 2026 — source inspection.** The pinned baseline monitor steps simulated time without updating the machine clock. The date-enabled LBM candidate calls `now/1`. Current GLP [`bb99275f`](https://github.com/EShapiro2/GLP/commit/bb99275f53ac546975098669fdafc9a1906520ad) contains [`set_clock/1` at startup and release in the canonical monitor](https://github.com/EShapiro2/GLP/blob/bb99275f53ac546975098669fdafc9a1906520ad/programs/sglp/monitor.glp). The retained clock result is sGLP’s project run. Keep this finding open pending an independent date-enabled test across a simulated day boundary.

Pending the auditor's record. The auditor's dated reviews of 24 November are on PR #83: [the answer](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7127882865), [the integration on main 87eb09ab](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7128486991) and [the retained test output](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7129969089); runtime verification by the audit is still pending there.
