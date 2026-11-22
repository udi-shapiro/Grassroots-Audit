# Secure Friendship eight-play trace checked — 22 November 2026

Both new recordings are public. [The stale trace](https://github.com/EShapiro2/GLP/blob/e6b768b5fb487e2a96d336926f994627d9ae177f/cascade/Secure-Friendship/run.log#L48-L53) shows no stale retry after Accept. [The below-threshold trace](https://github.com/EShapiro2/GLP/blob/e6b768b5fb487e2a96d336926f994627d9ae177f/cascade/Secure-Friendship/run.log#L41-L46) shows one statement, threshold two and no Accept. Keep the live-loss and offline controls open. See [stage 64](../../stages/64-pr76-secure-friendship-eight-play-verification-20261122.json).

---

# Secure Friendship threshold and stale retry fixtures checked — 22 November 2026

The audit checked both [fixture source](https://github.com/EShapiro2/GLP/blob/ba79cda1265b6aa7231fadd67770e3f2bf649795/programs/vglp/cva/secure_friendship/self.glp#L312-L352) and [threshold source](https://github.com/EShapiro2/GLP/blob/225430f3925d044455f080aa34b1e4f4bd89bee8/programs/vglp/cva/secure_friendship/self.glp#L275-L304). Publish the new logs with attempt and Ready ordering and final state. The offline and actual-loss controls remain open. See [stage 63](../../stages/63-pr76-secure-friendship-threshold-and-retry-20261122.json).

---

# Regenerated Secure Friendship cascade checked — 22 November 2026

[The public trace](https://github.com/EShapiro2/GLP/blob/dd7f57027e3206c417aa382c8d99015631804f3d/cascade/Secure-Friendship/run.log#L34-L39) shows Bob keeping Alicia and the acceptance record. No targeted Restore starts or votes occur after Accept. The [SPM reply](https://github.com/udi-shapiro/Grassroots-Audit/pull/76#issuecomment-7075300665) still ties the remaining controls to GSC’s state loss. See [stage 60](../../stages/60-pr76-secure-friendship-public-cascade-20261122.json).

---

# Secure Friendship state-loss dependency — 21 November 2026

[SPM clarified](https://github.com/udi-shapiro/Grassroots-Audit/pull/76#issuecomment-7070879744) that the scratch refusals were before Accept and that Carol made no later Restore friend attempt. After GSC’s in-run fault, exercise both notice orders, successful recovery and loss of Bob’s acceptance record. See [stage 59](../../stages/59-pr76-secure-friendship-state-loss-dependency-20261121.json).

---

# Secure Friendship scratch run recorded — 21 November 2026

The [SPM reply](https://github.com/udi-shapiro/Grassroots-Audit/pull/76#issuecomment-7070804026) reports both stale Restore refusals. The [fixture revision](https://github.com/EShapiro2/GLP/commit/ceb43d73724b8b8ca9eae5c0c6749163f69382af) changes only comments. [Draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) preserves this result under Finding 4. Next check both notification orders, positive replacement recovery and actual loss of the receiver’s acceptance record.

---

# Secure Friendship Restore friend receiver guard checked — 21 November 2026

[Draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) records the [catalogue change](https://github.com/EShapiro2/GLP/blob/65796c8f9495e71948b52a4335c801deb63448a9/calculus/contracts/Secure-Friendship/term.glp.txt). The two isolated guards reject the old friendship when either the receiver holds acceptance of a replacement or the sender holds the matching notice. The earlier public platform and log still need regeneration. See [stage 57](../../stages/57-pr76-restore-friend-receiver-guard-20261121.json).

After regeneration, record a refusal both before and after Tell change, and a positive recovery of the new friendship when it is absent after state loss.

# Forbidden wildcard compiler adopted on GLP main — 21 November 2026

[Draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) records the [compiler adoption](https://github.com/EShapiro2/GLP/commit/411150bedadcff6827abb7624bc027757d891f9e) and the independent replay of the 91-term scanner. Secure Friendship’s stored platform and trace still predate the fix. [SPM reports](https://github.com/udi-shapiro/Grassroots-Audit/pull/76#issuecomment-7070662249) that ordinary Restore is blocked with the new compiler. Restore friend still permits an older friendship record before Carol receives Tell change. The catalogue revision and corrected public traces remain pending. See [stage 56](../../stages/56-pr76-forbidden-wildcard-compiler-adoption-20261121.json).

Wait for the Restore friend receiver guard and run both Tell change delivery orders. Preserve a positive replacement recovery from actual lost state.

# Adopted Restore guard and catalogue reconciliation — 21 November 2026

[Draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) records that the [adopted Restore guard](https://github.com/EShapiro2/GLP/blob/b590ada9801ab4000ab319b11970648871411828/cascade/Secure-Friendship/platform.vglp#L234) still permits old Alice’s Restore in the [public trace](https://github.com/EShapiro2/GLP/blob/b590ada9801ab4000ab319b11970648871411828/cascade/Secure-Friendship/run.log#L34-L39). The 738-schema count now matches public main. [Calculus](https://github.com/udi-shapiro/Grassroots-Audit/pull/76#issuecomment-7070186436) attributes its extra 26 to the excluded Promoted Matching term. vGLP’s compiler correction is pending. See [stage 55](../../stages/55-pr76-adopted-restore-and-count-reconciliation-20261121.json).

Retest the old-Alice refusal and Restore friend with the concrete replacement fact after the common compiler correction. Preserve the adopted failing trace as a control.

# Forbidden wildcard scope in the public catalogue — 21 November 2026

[Draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) records a public count of 737 affected schema entries in 42 of 91 catalogue terms on GLP main `2aa20416b81bc42a8ad330a688c31f03e27b91b4`, plus one entry on the Calculus branch. The [compiler report](https://github.com/udi-shapiro/Grassroots-Audit/blob/6f0663aab7ebcc9b2dfebf5eeaf2d2b00f9abf00/programs/vglp/cva/compiler/text.glp.md#related-open-finding-forbidden-wildcards) links three generated examples and the common source path. Calculus’s wider count needs its exact input inventory. Runtime verification remains pending. See [stage 54](../../stages/54-pr76-forbidden-wildcard-catalogue-scope-20261121.json).

Retest ordinary Restore and Restore friend once the compiler correction and regenerated platform are public. Keep the custody and offline controls distinct.

# Secure Friendship forbidden wildcard checked — 21 November 2026

[Draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) records [SPM’s failed Restore control](https://github.com/udi-shapiro/Grassroots-Audit/pull/76#issuecomment-7069656729). The [generated forbidden-atom check](https://github.com/EShapiro2/GLP/blob/2aa20416b81bc42a8ad330a688c31f03e27b91b4/cascade/Secure-Friendship/platform.vglp#L5008-L5028) can accept an absent test with `any` despite a concrete matching fact. The same source path affects Restore friend. This qualifies the earlier check of the intended catalogue guard. A corrected platform and public traces remain pending. See [stage 53](../../stages/53-pr76-secure-friendship-forbidden-wildcard-20261121.json).

Publish the runtime trace with Bob holding accepted(alicia, alice) and a matching Restore attempt. Repeat the same negative control and an unrelated-restorer positive control after correction. Check Restore friend with Carol’s replacement notice too.

# Secure Friendship ordinary Restore guard checked — 21 November 2026

[Draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) records the [catalogue guard](https://github.com/EShapiro2/GLP/blob/fb822922dd8c2fa32ceff15882d5a494188bd89c/calculus/contracts/Secure-Friendship/term.glp.txt). It blocks the old restorer when Bob retains the acceptance fact. Actual state loss that deletes that fact remains a GSC question. The adopted source and stored GLP trace at the inspected pins are the earlier versions. See [stage 52](../../stages/52-pr76-secure-friendship-restore-guard-20261121.json).

Verify the regenerated Restore refusal once recorded. Add a positive recovery case where Alicia’s friendship is actually lost and preserve the marker retention condition.

# Secure Friendship custodian and recovery traces checked — 21 November 2026

[Draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) records the two new plays at GLP main `2aa20416b81bc42a8ad330a688c31f03e27b91b4`. The [custodian trace](https://github.com/EShapiro2/GLP/blob/2aa20416b81bc42a8ad330a688c31f03e27b91b4/cascade/Secure-Friendship/run.log#L27-L32) checks the two-party replacement and Carol’s notice. The [recovery trace](https://github.com/EShapiro2/GLP/blob/2aa20416b81bc42a8ad330a688c31f03e27b91b4/cascade/Secure-Friendship/run.log#L34-L39) restores old Alice before Tell change commits. Calculus acknowledges the path and proposes a guard. A published correction and positive live-loss control remain pending. See [stage 51](../../stages/51-pr76-secure-friendship-six-play-recording-20261121.json).

Keep the recorded running-old-Alice case separate from offline identity loss. Check the proposed Restore guard with the acceptance record retained and audit how it survives or is recovered after a real state loss. Add a positive control that actually deletes Alicia’s friendship and both notification orders.

# Secure Friendship recovery fixture checked — 21 November 2026

[Draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) records the [SPM recovery fixture](https://github.com/EShapiro2/GLP/blob/b1596a1914f9e068c53dd0b682d4af4044b7686e/programs/vglp/cva/secure_friendship/self.glp). Bob starts with `state_loss` and old Alice remains online. The generated ordinary Restore guard explains the reported return of the old friendship. The public log still covers the earlier four plays. A recorded trace and a positive live-loss recovery control remain pending. See [stage 50](../../stages/50-pr76-secure-friendship-recovery-fixture-20261121.json).

Check the public trace once Code records the new play. Keep the configured running-old-identity case distinct from the paper’s identity-loss model. Add a positive case after actual loss of Alicia’s friendship and check both delivery orders.

# Secure Friendship main recovery and offline blocker — 21 November 2026

[Draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) records the [two-party Accept trace](https://github.com/EShapiro2/GLP/blob/2a248be193c55fe39b0d941496d4885441e6d71b/cascade/Secure-Friendship/run.log#L18) and replacement-aware recovery schemas at GLP main `2a248be193c55fe39b0d941496d4885441e6d71b`. SPM reports that taking old Alice offline stalls Carol’s Tell before she can vouch. The generated lock and tally support that mechanism. [vGLP’s proposal](https://github.com/udi-shapiro/Grassroots-Audit/pull/76#issuecomment-7069004310) awaits Udi’s decision. The public custodian, offline and recovery controls remain pending. See [stage 49](../../stages/49-pr76-secure-friendship-offline-blocker-20261121.json).

Publish the offline trace with Carol’s held Tell attempt before vouching and pin the actual configuration. Check the custodian and notice play at its own version. Test replacement-aware recovery with an older recorded friendship and a replacement fact in both delivery orders.

# Secure Friendship identity-loss roles checked — 21 November 2026

[Draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) preserves the Calculus and SPM replies. The [new catalogue term](https://github.com/EShapiro2/GLP/blob/42a4a5964d0151122715bd9f38d7195f1bd2c4d8/calculus/contracts/Secure-Friendship/term.glp.txt) removes old Alice from the state tests and effects of the two Accept acts. The earlier main trace includes her vote. SPM reports a successful scratch run. Public adoption, an [offline control](https://github.com/udi-shapiro/Grassroots-Audit/pull/76#issuecomment-7068705219), and the follow-up for recovering Bob remain pending. See [stage 48](../../stages/48-pr76-secure-friendship-identity-loss-20261121.json).

Preserve the four-play scratch result as a project claim. Check whether a new public fixture makes the old machine unavailable after record delivery and whether it covers both Accept acts and Tell change. Inspect and test recovery with a stale record and a replacement notice after the proposed follow-up lands.

# Secure Friendship controls confirmed on GLP main — 21 November 2026

[Draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) records integration at GLP main `ff6579e19e58f01e0c2bc8793407ea9d8d2e2f1d`. The [four-play log](https://github.com/EShapiro2/GLP/blob/ff6579e19e58f01e0c2bc8793407ea9d8d2e2f1d/cascade/Secure-Friendship/run.log), manifest, fixture and both vGLP platform copies match the previously checked recording. Python checks confirmed the Secure Friendship numeral spelling and stamped term. Source checks confirmed the compiler and checker changes. Code reports 4,205 passes at the earlier `ff122013ff3f68f570b1ef983540cd2005013ed0` pin. Independent runtime verification, live loss and re-keying remain open. See [stage 47](../../stages/47-pr76-secure-friendship-main-integration-20261121.json).

Independently rerun the four focused plays when Dart is available. Keep live-loss recovery in both delivery orders and custodian re-keying open. Verify the canonical correspondence claim against the public vGLP paper.

# Secure Friendship threshold and Restore friend controls checked — 21 November 2026

[Draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) records two independently checked controls from the [public four-play log](https://github.com/EShapiro2/GLP/blob/a56485a68e01d7452cf75d301283f779f1b1625d/cascade/Secure-Friendship/run.log) at GLP `a56485a68e01d7452cf75d301283f779f1b1625d`. Bob’s one-voucher view precedes Dave’s second qualified voucher and the first Accept attempt, which commits. With startup loss, Alice refuses Restore friend solely because her friendship with Carol is present. The audit ran Python checks on the stored trace. GLP main integration, runtime reruns, live loss and re-keying remain pending. See [stage 46](../../stages/46-pr76-threshold-and-restore-friend-controls-20261121.json).

Independently rerun the focused plays when Dart is available. Keep Findings 4 and 5 open for live loss and both recovery orders, and custodian re-keying. Verify the canonical correspondence claim against the public vGLP paper and its hypotheses.

# Secure Friendship startup-loss control checked — 21 November 2026

[Draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) records the [two-play log](https://github.com/EShapiro2/GLP/blob/ff122013ff3f68f570b1ef983540cd2005013ed0/cascade/Secure-Friendship/run.log). The startup-loss run isolates an existing-friendship refusal for Restore. The replacement log contains no negative Accept, so the [audit reply](https://github.com/udi-shapiro/Grassroots-Audit/pull/76#issuecomment-7066552253) requests a paired voucher-threshold control. See [stage 45](../../stages/45-pr76-startup-loss-and-voucher-controls-20261121.json). Check integration on GLP main and request the public paired threshold control already named in PR discussion. Keep the live-loss finding open for actual state deletion and both recovery orders. Independently run the plays and focused numeric controls when a GLP runtime is available.

# Secure Friendship public cascade play checked — 21 November 2026

[Draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) records the matching regenerated platforms and the [public cascade log](https://github.com/EShapiro2/GLP/blob/f1f8898c79fa8763fecb827dfcc8f7c3c88f5789/cascade/Secure-Friendship/run.log) at GLP `f1f8898c79fa8763fecb827dfcc8f7c3c88f5789`. The log records custodian and threshold delivery, then Vouch, Present, Accept and Tell friends. The audit checked the stored evidence. Independent runtime controls and live-loss recovery remain pending. See [stage 44](../../stages/44-pr76-public-secure-friendship-cascade-play-20261121.json). Verify GLP main integration against the recorded artifact blobs. Run the focused play, checker and VG controls when a GLP runtime is available, with negative and competing voucher cases. Keep Finding 4 open for live loss and both delivery orders, and Finding 5 open for runtime controls and re-keying. Draft #76 awaits review.

# Secure Friendship adopted module and reported play — 21 November 2026

[Draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) records public GLP `a6fc2475b4346c80198886ce4ccb40481c3687e4`. The adopted module now matches the corrected catalogue and stamp, while both stored platforms retain the earlier literal. SPM reports a completed play with a freshly generated platform. Its expected public cascade log is pending. See [stage 43](../../stages/43-pr76-reprinted-module-and-reported-play-20261121.json). Check the public main pin after cascade regeneration. Compare the adopted term, catalogue stamp, cascade platform and play copy, verify the play mapping, and inspect the published cascade/Secure-Friendship/run.log when present. Independently run the play and focused checker and VG controls with a GLP runtime. Finding 5 remains open for runtime and re-keying. Finding 4 remains open for live-loss modelling.

# Secure Friendship combined source checked — 21 November 2026

[Draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) records Code’s combined branch `bbf840928ca69182356ba46bcecebfac120ff5bf`. Its new catalogue term matches the stamp, while the adopted module and play still use `val(2)`. The checker guard and regenerated artifacts remain pending at this pin. See [stage 42](../../stages/42-pr76-combined-source-awaits-regeneration-20261121.json). At the next public combined pin, verify the regenerated adopted module, catalogue stamp and play platform agree, and confirm the checker guard landed. Run the focused checker and Section VG controls, then the Secure Friendship play when a GLP runtime is available. Finding 5 remains open for runtime and re-keying. Draft #76 awaits review.

# Secure Friendship numeric correction checked on branches — 21 November 2026

[Draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) records the [printer correction](https://github.com/EShapiro2/GLP/commit/ff6fe9aeda7e2fc59f5d348459ff0b11437d1790), [checker guard](https://github.com/EShapiro2/GLP/commit/f4ef10dbf7b8834eecd23eb6169f4425879d27f9) and [compiler integration branch](https://github.com/EShapiro2/GLP/commit/1246d8c8531418a0c36a21cdd31e7c7ddf489b9d). The printer emits `num(2)` and the Secure Friendship term matches its stamp. The checker source rejects numeric `val(N)` in arguments and expressions. Full integration and runtime remain pending. See [stage 41](../../stages/41-pr76-compiler-printer-checker-branches-20261121.json). Check combined public integration, including regenerated source terms, verdict stamps and platforms. Independently execute the GSC numeric argument and expression controls, Section VG double control and Secure Friendship play when GLP runtime is available. Finding 5 stays open for play and re-keying; draft #76 awaits review.

# Secure Friendship Identity record follow-up — 21 November 2026

[Draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) records the [vGLP compiler change](https://github.com/EShapiro2/GLP/commit/950cc0267de9531143fe515d6a196c206c1a419f) and the Calculus printer’s current `val(2)` output. Both are relevant to the reported Identity record rejection. The reported full-play pass awaits a combined public pin and independent execution. See [stage 40](../../stages/40-pr76-identity-record-compiler-printer-20261121.json). Track integration of the vGLP compiler and Calculus printer changes, including public regenerated terms and checks. Independently run the focused Section VG control and Secure Friendship play once combined artifacts and GLP runtime are available. GSC owns the checker question. Finding 5 stays open and draft #76 awaits review.

# Secure Friendship checkpoint guard and play checked — 21 November 2026

[Draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) records the checkpoint guard at public GLP `ec20d0da9f50e0c0a90b5bd2d40dd03c0d6f1fc4`. It stops repeats while the marker remains. The [play](https://github.com/EShapiro2/GLP/blob/4a7e0e2a00327a06da94d7569237afdfdd51b8f5/programs/vglp/cva/secure_friendship/self.glp) is public on a branch and uses the pinned main platform. SPM reports rejection at Identity record. The audit confirmed the numeric binding in source and did not run the play. See [stage 39](../../stages/39-pr76-checkpoint-guard-and-public-play-20261121.json). Reproduce the reported local Identity record rejection using the public branch play and collect the actual local state and numeric binding. Then test Present, voucher counting, Accept and Tell friends. Checkpoint record delivery and live-loss recovery remain open. Draft #76 awaits review.

# Secure Friendship checkpoint play blocker recorded — 21 November 2026

[Audit draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) preserves [SPM’s run-limit report](https://github.com/udi-shapiro/Grassroots-Audit/pull/76#issuecomment-7061318777). At public GLP `6c14d338145f6a65c6c1727cd71c7d46cb51e2b7`, Checkpoint remains enabled after adding its marker. The Python source check does not exercise GLP scheduling. The manifest still lists no play. See [stage 38](../../stages/38-pr76-checkpoint-play-blocker-20261121.json). Inspect the public checkpoint correction and verify that a nontrivial update still fires and a repeated unchanged checkpoint does not. Then run the pinned Secure Friendship play for Vouch, Present, Accept and Tell friends, including voucher-count and notification controls. Findings 3 and 5 remain open. Draft #76 awaits review.

# Secure Friendship and GSC project follow-ups — 21 November 2026

[Audit draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) preserves the project replies on re-keying and live-loss modelling. Public GLP `6c14d338145f6a65c6c1727cd71c7d46cb51e2b7` still has the separate custodian effects and no Secure Friendship play. [GSC’s paper follow-up](https://github.com/udi-shapiro/Grassroots-Audit/pull/30#issuecomment-7061253610) reports edits pending the Overleaf handoff. GSC says the marked state-loss proposal has yet to be submitted. See [stage 37](../../stages/37-pr30-50-76-gsc-spm-followups-20261121.json). GSC’s paper revision needs a public version and the #30 report still needs the requested scope and publication corrections. Separately, the GSC live-loss proposal is pending submission. Calculus’s one-step re-keying grammar proposal awaits a decision. SPM’s behavioural plays still need public source and independent execution. Draft #76 awaits review.

# Secure Friendship catalogue term reconciled — 21 November 2026

[Audit draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) preserves Calculus’s two dated replies. At public GLP `6c14d338145f6a65c6c1727cd71c7d46cb51e2b7`, the reprinted catalogue term matches the verdict stamp and the body in the adopted module and its cascade copy. The manifest still records no Secure Friendship play. Finding 5 remains open for custodian replacement and behavioural checks. See [stage 36](../../stages/36-pr76-catalogue-term-reconciled-20261121.json). Draft #76 awaits review and ticket mapping. Continue Finding 5 verification with custodian replacement, voucher counting and notifications on a runnable Secure Friendship platform. Finding 4 still awaits the GSC fault-model decision. Calculus #75 retains its held verdicts and separate item 5 decision.

# Secure Friendship Present artifacts checked — 21 November 2026

[Audit draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) preserves the new SPM and Code replies. At public GLP `ee7162e0c773cb42c3c461d65e41ecbc83eaffd8`, both stored platforms contain the no-field Present button and the earlier refusal is gone. The catalogue hash mismatch, custodian replacement and runtime checks remain open. Code reports Section TY passed. The audit ran source and status checks. See [stage 35](../../stages/35-pr76-present-platform-integration-20261121.json). Review audit draft #76 and settle ticket mapping. Calculus to reconcile term and verdict stamp and resolve custodian replacement. GSC’s model decision and an executable loss control are needed for both recovery delivery orders. Run a focused Secure Friendship play for record delivery, replacement, and notifications when available.

# Secure Friendship findings prepared for review — 21 November 2026

[Audit draft #76](https://github.com/udi-shapiro/Grassroots-Audit/pull/76) preserves Ohad Eitan’s revised report, dated project answers and all five findings from [PR #50](https://github.com/udi-shapiro/Grassroots-Audit/pull/50). At public GLP `e8ebce875d7a4ab42314712445ca87f33163121c`, Python source assertions confirmed the stored CVA refusal for the missing Present button and the catalogue term’s verdict-stamp mismatch. No GLP compiler, checker or runtime ran. The draft has 30 reports, 28 findings and zero unanswered. Review the five dispositions and ticket mapping before merging.

See [stage 34](../../stages/34-pr50-secure-friendship-report-20261121.json). Review draft #76 and agree final dispositions for the five findings before creating linked tickets and merging. SPM and Calculus need to supply a Present button, reconcile the catalogue term and stamp, and record focused delivery, loss/recovery and replacement behavior on a compiled platform. Continue the recorded core verification queue after prioritized application work. All six core answers are already present.

# Public GLP integration checked — 21 November 2026

At GLP `e8ebce875d7a4ab42314712445ca87f33163121c`, GO’s regenerated platform artifacts and all 39 Calculus rebuild inputs match the earlier pins. [PR #71](https://github.com/udi-shapiro/Grassroots-Audit/pull/71) and [PR #75](https://github.com/udi-shapiro/Grassroots-Audit/pull/75) record integration and await review. [SPM’s follow-up](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7059738642) points to the integrated Secure Friendship module. Its refreshed cascade record contains the matching module and a stored checker verdict, but the CVA compiler refused the platform because the guarded Present act has no button. [Refusal record](https://github.com/EShapiro2/GLP/blob/e8ebce875d7a4ab42314712445ca87f33163121c/cascade/Secure-Friendship/platform.vglp) No GLP run was independently executed in this follow-up. See [stage 33](../../stages/33-glp-main-integration-pr50-71-75-20261121.json).

# Secure Friendship module rebuild confirmed — 20 November 2026

[SPM’s follow-up](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7058299451) links public GLP `589d1f22be5ddda803fde15e1ef19acbab0eb1ea`. The adopted module at that pin matches the independent Python rebuild byte for byte. Its term matches the published verdict stamp, while the stored catalogue term differs at Accept. The cascade manifest is unchanged. [PR #50](https://github.com/udi-shapiro/Grassroots-Audit/pull/50) remains open with changes requested. No GLP checker or runtime ran. See [stage 31](../../stages/31-pr50-spm-regenerated-module-20261120.json).

# Secure Friendship rebuilt from public GLP — 20 November 2026

[SPM’s follow-up](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7058086928) cites public GLP `6b8f8463295918b31b5dde02722d692ac990c64a`. The pinned Python tools reproduce the published full schemas from both adopted and catalogue inputs. The rebuilt Accept differs from the stored catalogue term and matches the published verdict stamp. The checked-in module retains the earlier logic. [Audit reply](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7058124083) records the differences. Audit PR #50 remains open with changes requested. No GLP checker or runtime ran. See [stage 30](../../stages/30-pr50-spm-public-rebuild-20261120.json).

# SPM reports a superseding Secure Friendship revision — 20 November 2026

[SPM's dated follow-up](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053864701) attributes fixes for Findings 2, 4 and 5 to Calculus `27ae7275`, superseding `8524842f`. The public GLP contract and generated schemas at `aaadc7613508ca44e132b0f9b2e283323225fc3f` still match the previous baseline. PR #50 is open at the same report head `c6386390267fc83ada253af068ef6ea653cdae6a`. Independent verification awaits the public adoption revision. See [stage 22](../../stages/22-pr50-spm-superseding-revision-20261120.json).

# Calculus follow-up to Secure Friendship review — 20 November 2026

[Calculus's dated follow-up](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053633313) claims fixes to threshold delivery, recovery, vouchers and replacement notifications. At public GLP `aaadc7613508ca44e132b0f9b2e283323225fc3f` the generated schemas still show the earlier behavior, and the baseline's stored verdict already says `syntactically_grassroots`. [The audit reply](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053676773) records the evidence and requests a public adoption revision and behavioral checks. PR #50 remains open at `c6386390267fc83ada253af068ef6ea653cdae6a`. No runtime or compiler check ran. Preserve Ohad's proposal, SPM's disagreement and Calculus's follow-up under the original finding identifiers. See [stage 21](../../stages/21-pr50-calculus-follow-up-20261120.json).

# SPM reply to Secure Friendship review — 20 November 2026

[SPM's dated reply](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053164176) disputes the English rewrite and narrows the remaining defects to Logic pragmas. The contract/schema blobs are unchanged at inspected public GLP. GLP PR #86 closed without merging, and audit PR #50's head remains unchanged. Preserve the disagreement under the original IDs in the next report revision with public evidence. See [stage 20](../../stages/20-pr68-gsa-and-spm-reply-20261120.json).

# PR #50 state-recovery revision — 2026-11-19 UTC

[PR #50](https://github.com/udi-shapiro/Grassroots-Audit/pull/50), head `c6386390267fc83ada253af068ef6ea653cdae6a`, changes Finding 4 only. [Review 5971010401](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#pullrequestreview-5971010401) asks that recovery choose the newest valid friendship transition regardless of delivery order and define handling for conflicting records with the same version. The existing restore guard disables the same restore while the restored friendship is present, although the schema has no per-loss identifier.

GLP main `31774246c35770d6441598576267a88f620d6e37` still has the original Secure Friendship contract and schema blobs. The new head `160ed2a48244d9cdd105f62671c64396718ee34a` of GLP PR #86 is open and changes only English. No cascade or runtime check ran. The original review's remaining findings and publication prerequisites stand. See [stage 15](../../stages/15-pr50-spm-revision-20261119.json) for pins, discussion and next checks.

# PR #50 Secure Friendship report review — 2026-11-17

PR [#50](https://github.com/udi-shapiro/Grassroots-Audit/pull/50), head `ace65838944396c4a6a777d2b31c8ec17cc0bf72`, proposes five findings at the correct mirrored path `programs/social/spm/Secure-Friendship.txt.md`, attributed to Ohad Eitan (SPM co-author) with Claude. Review [5944513543](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#pullrequestreview-5944513543) requests changes; the PR is not merged and no tickets were opened.

Independent source inspection pinned GLP `2edbcd8c6ab343dd4d6fad5421f8e6e5386d3266`, contract blob `1618b54fcadb0cd33167b63b07ed437c5df5e9fc`, generated blob `177c072290dfd160d5363a431172cc7ed04d425d`, and open GLP PR #86 head `7701a2a4649fa40cec0472249447225a9685357a`. Finding 3 is supported. Findings 1, 2 and 4 require narrowing: the preamble already says Alice names custodians; `send_record` can run after a pre-existing friendship and its negative record guard prevents the same custodian delivery repeating; `restore` self-disables by adding the missing friendship. Finding 5's main dataflow gaps are source-visible, while the underscore matching claim still needs cited matcher semantics or a focused reproduction.

The accepted SPM GPT auditor owns the independent report; preserve Ohad/Claude as proposer attribution. Contributor cascade/sGLP claims remain attributed: this run executed no GLP or status tool. A corrected five-finding publication would require `ISSUES.md`, regenerated `sections/status-table.tex`, and totals 29 reports / 21 findings / 5 unanswered / 13 unresolved / 8 verified corrected. Create native tickets only after corrected finding texts are accepted. GLP PR #86 is an open English-only proposal, not a verified correction or project answer. Exact evidence and next steps: `auditor/stages/12-pr50-spm-review-20261117.json`.

# SPM auditor assignment

Source: GLP `f68fbcbc3ef91b9707037ef7e5dfdb302acd1458`. Published name: Securing People and their Machines. Paper keys: SPM.

Status: queued; no substantive coverage claimed and no active dedicated session. Begin with auditor/roster.md, project-structure.json, coordination.md and current main rules. Pin current papers and relevant code before review. Preserve source paths and review the project's papers and code together. Do not infer an unpresented paper's key or version. Record exact scope and a handover after each bounded work unit.
