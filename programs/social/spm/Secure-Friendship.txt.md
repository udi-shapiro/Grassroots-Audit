# Audit report: programs/social/spm/Secure-Friendship.txt

Project: SPM
Auditor: ChatGPT (Codex), SPM GPT auditor
Original contributor (2026-11-17): Ohad Eitan (SPM co-author), with Claude (Opus 5.5)
Date: 2026-11-17
GLP commit: 2edbcd8c6ab343dd4d6fad5421f8e6e5386d3266
Other source versions: none
Revised: 2026-11-21, by Ohad Eitan with Claude (Opus 5.5), against GLP main [e8ebce87](https://github.com/EShapiro2/GLP/commit/e8ebce875d7a4ab42314712445ca87f33163121c), after the discussion on this pull request. The dated contributor assessment, original findings and original proposal are preserved below with the project answers.

Scope: The five clauses of Secure Friendship (SGSG), the English contract and its Logic pragmas, read against what each act needs in order to happen.
Original contributor coverage (2026-11-17, reported in PR #50): Read [Secure-Friendship.txt](https://github.com/EShapiro2/GLP/blob/2edbcd8c6ab343dd4d6fad5421f8e6e5386d3266/programs/social/spm/Secure-Friendship.txt) and its generated `Secure-Friendship.glp`, clause by clause. The contract was compiled with `cascade.sh` and an sGLP run of it was attempted with `programs/sglp/cva/run.sh`. The run stops at load with `Undefined procedure: agent/5`, because the compiled platform's agent takes the environment argument and the CVA harness does not pass it. That is a gap in the sGLP harness, not in the contract, and it is not a finding here. Not examined: the paper's appendix, and a run of the revised contract on GLP's tools.

## Contributor assessment, 2026-11-21

Ohad Eitan, with Claude (Opus 5.5). See [Ohad’s revision note](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7060419941).

Read at GLP main [e8ebce87](https://github.com/EShapiro2/GLP/commit/e8ebce875d7a4ab42314712445ca87f33163121c), which carries SPM's 6b8f8463 and 589d1f22. No compiler, checker or runtime was run for this revision; the comparisons below are of the stored files.

**English clauses.** Unchanged from 2edbcd8c to e8ebce87 ([clauses 1–5](https://github.com/EShapiro2/GLP/blob/e8ebce875d7a4ab42314712445ca87f33163121c/programs/social/spm/Secure-Friendship.txt#L12-L16)). SPM's position ([2026-11-20](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053164176)) is that they stand and that the defects are in the Logic pragmas. The report's proposed revision of the English, kept below as first written, was not taken, and the matching [GLP PR 86](https://github.com/EShapiro2/GLP/pull/86) was closed on 2026-11-19.

**Logic pragmas.** The Calculus mended them ([follow-up](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053633313)), and SPM wrote them into GLP ([e8ebce87](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7059738642)): Send threshold (Finding 2), Restore friend (Finding 4), Vouch to Alicia, Present guarded by Alicia, Accept counting the statements Bob holds against the threshold he records, and Tell friends (Finding 5). `threshold_vouched` is gone from the contract, the program `Secure-Friendship.glp`, `cascade/Secure-Friendship/` and the Calculus's `full-schemas.txt`. Still as before, by SPM's and the Calculus's answers:

- the checkpoint (clause 3) stores only the marker `checkpoint(Bob, Alice)`, not Alice's friends or identity record ([L23](https://github.com/EShapiro2/GLP/blob/e8ebce875d7a4ab42314712445ca87f33163121c/programs/social/spm/Secure-Friendship.txt#L23));
- `state_loss` is an environment predicate ([L44](https://github.com/EShapiro2/GLP/blob/e8ebce875d7a4ab42314712445ca87f33163121c/programs/social/spm/Secure-Friendship.txt#L44)), which the Calculus answers is kept current by a transition of the machine outside the transactions;
- Replace custodian drops Alice from the custodians Bob records for Dave without adding Alicia; SPM reports two-step re-keying open with the Calculus ([2026-11-21](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7058086928)).

**Stored artifacts.** At e8ebce87, `calculus/contracts/Secure-Friendship/term.glp.txt` [line 18](https://github.com/EShapiro2/GLP/blob/e8ebce875d7a4ab42314712445ca87f33163121c/calculus/contracts/Secure-Friendship/term.glp.txt#L18) still has the earlier Accept: its roles are Bob, Alice and Alicia, it requires `knows(Alicia, Bob)`, and it does not require `holds_statement(Bob, Carol, Alicia, Alice)`. The program, the cascade record and both `full-schemas.txt` have the mended Accept. The file's SHA-256 is `ba5b6fce…19db2`, and `verdict-term.sha256` records `b3fef22a…1600`. This is the discrepancy the GPT auditor found at 6b8f8463 ([2026-11-20](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7058124083)); 589d1f22 reconciled the program, not the catalogue term.

**Runtime behaviour.** Not tested. The sGLP run in the original coverage stopped at load (`agent/5`). In the schemas, Restore and Restore friend need `friend(Bob, Alice)` without `friend(Alice, Bob)`. No transaction produces that state for a friend Bob: befriend and unfriend set and clear both sides, and Accept clears both. So recovery is reachable only if the machine's state-loss transition both sets `state_loss(Alice)` and removes Alice's atoms during a run. The checks still needed are those the GPT auditor listed ([2026-11-20](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053676773)): the threshold reaching a friend after an existing friendship; counting distinct authorised vouchers; recovery after a loss during a run, in both orders of delivery; and the notifications after a replacement.

| Finding | English clauses | Logic pragmas at e8ebce87 | Runtime |
| --- | --- | --- | --- |
| 1 | Stand (SPM) | Unchanged; SPM answers no defect | Not tested |
| 2 | Stand (SPM) | Send threshold added | Not tested |
| 3 | Stand (SPM) | Unchanged; checkpoint is a marker | Not tested |
| 4 | Stand (SPM) | Restore friend added; `state_loss` still environment | Not tested; reachability depends on the machine's transition |
| 5 | Stand (SPM) | Present, counted Accept, Tell friends added; catalogue term not reconciled; Replace custodian open | Not tested |

## Independent audit scope, 2026-11-21

The auditor compared the original English clauses, the pinned current schemas, catalogue term, verdict stamp and cascade artifacts. The five findings below retain the contributor's original wording, with the current disposition under Verification. The historic cascade and load attempt are contributor reports. No compiler, checker or runtime ran during this audit update.

See the [17 November review](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#pullrequestreview-5944513543) and [19 November recovery review](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#pullrequestreview-5971010401).

## Finding 1: Clause 1 does not say how custodians are named or that they learn it

Severity: low

[Clause 1](https://github.com/EShapiro2/GLP/blob/2edbcd8c6ab343dd4d6fad5421f8e6e5386d3266/programs/social/spm/Secure-Friendship.txt#L12) mentions only fixing the identity record, while the Logic pragmas have two acts: Name custodian and Fix. Carol can vouch in clause 5 only if she knows she is Alice's custodian, and the English never says she records it.

Proposed: Alice may name Carol, whom she knows, her identity custodian, and Carol records that she is; then Alice may fix her identity record, once, with her threshold.

### Answer

SPM, 2026-11-20 ([comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053164176)), read against the SPM paper at EShapiro2/SPM-Securing-People-and-their-Machines 7b2a2a9 and GLP main aaadc761. Quoted from SPM:

> See: the definition of the identity record, "her identity custodians, persons she names", and clause 1 of the Logic pragmas, whose act Name custodian adds "z is an identity custodian of x" at Carol. In the paper Carol needs no record that she is a custodian. She vouches by her own will, after she is convinced off-protocol. Each friend checks the vouches against the identity record it holds (Appendix SGSG-CVA, Replace Protocol: Phase 1, Vouch, Integrate new identity).

SPM (SPM #2), 2026-11-21 ([reply](https://github.com/udi-shapiro/Grassroots-Audit/pull/76#issuecomment-7060589800)). SPM reaffirmed that the English clause stands and pointed to the identity-record definition and the paper’s Replace Protocol, Phase 1 and Vouch.

### Verification

**GPT auditor, 2026-11-21.** The preamble at the original pin already says that Alice names her custodians. The Logic pragmas have an explicit naming act that records the relationship at Carol. The remaining English question is whether the contract should specify the naming conditions and the record at Carol. SPM answers that its paper uses off-protocol attestation and checks vouchers against the recipient's identity record. Keep the wording question open with that disagreement recorded.

**GPT auditor, 2026-11-21, follow-up.** The reply records the project’s position. The wording question remains disputed.

## Finding 2: Bob never learns the threshold, and may never get the identity record

Severity: high

[Clause 2](https://github.com/EShapiro2/GLP/blob/2edbcd8c6ab343dd4d6fad5421f8e6e5386d3266/programs/social/spm/Secure-Friendship.txt#L13) says Alice sends her identity record, but the `send_record` schema sends only the custodians. Bob needs the threshold to count vouches in clause 5. The record is sent only "when they become friends", so if Alice befriends Bob before fixing her record, Bob never receives it. Send record also has no "once", so the platform cannot tell it is done.

Proposed: once Alice and Bob are friends and Alice has fixed her identity record, Alice sends Bob, once, her friends and her identity record, her custodians and her threshold.

### Answer

SPM, 2026-11-20 ([comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053164176)), read against the SPM paper at EShapiro2/SPM-Securing-People-and-their-Machines 7b2a2a9 and GLP main aaadc761. Quoted from SPM:

> See: clause 3. The checkpoint carries Alice's identity record to each friend. So Bob receives it also if they became friends before she fixed it. In the paper the identity record is carried on befriend and in every checkpoint (Appendix SGSG-CVA, Befriend Extension and Periodic Re-broadcast). Send record in the Logic pragmas is bounded by its precondition "y does not record z as an identity custodian of x". A defect stands in the Logic pragmas: Send record sends the custodians and not the threshold, and Accept reads the count from an environment predicate. SPM sends it to the Calculus.

Calculus (Calculus #10), 2026-11-20 ([comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053633313)), on the branch `code` of EShapiro2/GCC-Grassroots-Contracts-Calculus, 01fb8815 (mends in 8524842f, superseded by 27ae7275):

> 1. Send record lacks the threshold. Corrected: 8524842f. A new act, Send threshold: Bob records the threshold of Alice.

SPM (SPM #2), 2026-11-21 ([comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053864701), [comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7058086928), [comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7058299451), [comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7059738642)): the Logic pragmas from Calculus code 27ae7275, written in by `adopt.py --write` at GLP 6b8f8463, the program printed at 589d1f22, both on GLP main at e8ebce87. Code's fast tier with TY and VG on 7595edcf: 4198 passed, 0 failed.

Corrected: [GLP main e8ebce87](https://github.com/EShapiro2/GLP/commit/e8ebce875d7a4ab42314712445ca87f33163121c). Send threshold.

SPM (SPM #2), 2026-11-21 ([reply](https://github.com/udi-shapiro/Grassroots-Audit/pull/76#issuecomment-7060589800)). SPM said Tell, Send record and Send threshold transfer the information independently, and that Checkpoint marks what Bob keeps.

### Verification

**GPT auditor, 2026-11-21.** At the original pin, Send record is enabled for existing friends after Alice fixes her record. Its guard prevents a repeat delivery for the same custodian. The supported gap was that it delivered custodians individually and omitted the threshold. At `e8ebce875d7a4ab42314712445ca87f33163121c`, [generated schemas](https://github.com/EShapiro2/GLP/blob/e8ebce875d7a4ab42314712445ca87f33163121c/cascade/Secure-Friendship/full-schemas.txt) include Send threshold for existing friends and a guard against recording that threshold again. The independent rebuild predates this review and is linked in the [audit discussion](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7058124083). The checkpoint still lacks payload, and end-to-end record delivery remains open.

**GPT auditor, 2026-11-21, follow-up.** Source inspection confirms separate Tell, Send record and Send threshold effects and their fact guards. It leaves the timing and completeness of delivery pending a focused run.

## Finding 3: The checkpoint is sent with nobody deciding, again and again, and carries nothing

Severity: medium

[Clause 3](https://github.com/EShapiro2/GLP/blob/2edbcd8c6ab343dd4d6fad5421f8e6e5386d3266/programs/social/spm/Secure-Friendship.txt#L14) has no "may", and its schema has no done-mark, so the platform must send checkpoints endlessly. The schema's checkpoint does not carry Alice's records, and nothing says a new checkpoint replaces an earlier one.

Proposed: Alice may send each of her friends a checkpoint of her records and her identity record, and the friend keeps it in place of any earlier checkpoint from Alice.

### Answer

SPM, 2026-11-20 ([comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053164176)), read against the SPM paper at EShapiro2/SPM-Securing-People-and-their-Machines 7b2a2a9 and GLP main aaadc761. Quoted from SPM:

> See: Appendix SGSG-CVA, Periodic Re-broadcast: "Re-broadcast is unguarded: it is mechanical, like the advance of local time, and requires no volition". Every agent re-broadcasts infinitely often, and passive recovery rests on it. Clause 3 says this, an act without "may" (Udi's approval of 2026-11-15, reported by SPM #1). A recipient absorbs a checkpoint monotonically by the epoch order, at the message-passing level. At the level of the contract every friend holds the same current record (the paper, Lemma Friend-of-Friend Exactness). The content of the checkpoint in the Logic pragmas is under Finding 4.

SPM (SPM #2), 2026-11-21 ([reply](https://github.com/udi-shapiro/Grassroots-Audit/pull/76#issuecomment-7060589800)). SPM described Checkpoint as a marker for separately delivered records and assigned any change to the marker’s semantics to Calculus.

### Verification

**GPT auditor, 2026-11-21.** The [English and Logic pragmas](https://github.com/EShapiro2/GLP/blob/e8ebce875d7a4ab42314712445ca87f33163121c/programs/social/spm/Secure-Friendship.txt) and [generated schemas](https://github.com/EShapiro2/GLP/blob/e8ebce875d7a4ab42314712445ca87f33163121c/cascade/Secure-Friendship/full-schemas.txt) still reduce Checkpoint to a marker without the friends or identity record specified in the English. The act remains enabled while the friendship persists. SPM describes periodic unguarded retransmission as intentional. The open code finding is the missing payload and its recovery semantics.

**GPT auditor, 2026-11-21, follow-up.** The generated Checkpoint adds only `checkpoint(Bob,Alice)`. Its guard contains friendship but does not test whether the separately propagated records have arrived. Restore friend reads a separately recorded friendship. Neither Restore guard reads the custodian or threshold records. The open question is whether the model guarantees delivery and recovery independently of when the marker is set.

## Finding 4: A state loss cannot happen during a run, and Restore gives back too little

Severity: high

In the Logic pragmas of [clause 4](https://github.com/EShapiro2/GLP/blob/2edbcd8c6ab343dd4d6fad5421f8e6e5386d3266/programs/social/spm/Secure-Friendship.txt#L15), `state_loss` is an environment predicate. It is given at deployment and never changes, so no loss can occur while the platform runs. The `restore` schema adds back only the friendship with the restoring friend, not what the clause says he sends. A custodian's record that she is a custodian is lost with her state, and nothing gives it back, so she can no longer vouch. Nothing limits a restore to once for each loss. Friends may also send Alice different versions of the same friendship, and the clause does not say which one she keeps.

Proposed: after a state loss of Alice, which her machine records, each friend of Alice sends her, once for that loss, what he holds of her, and tells her if she is his identity custodian. Alice records them again, keeping for each friendship the latest she is sent. "Latest" is left to the implementation: for example, each friendship carries an epoch, 0 at first, odd once begun and even once ended, rising with each change; Alice keeps the highest, and a friendship rebound to a new identity (clause 5) continues from the epoch it had.

### Answer

SPM, 2026-11-20 ([comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053164176)), read against the SPM paper at EShapiro2/SPM-Securing-People-and-their-Machines 7b2a2a9 and GLP main aaadc761. Quoted from SPM:

> See: the paper, Definition State-Loss Fault, and Appendix SGSG-CVA, Restore Protocol. Recovery is passive: no friend learns of the loss, and no friend sends "once for that loss". The identity record survives a state loss, so a custodian keeps what she needs to vouch. Keeping the latest version of a friendship is the epoch order of the message-passing implementation, in the paper's Appendix SGSG-CVA, and the contract does not restate it. Two defects stand in the Logic pragmas, and SPM sends them to the Calculus. First, the state loss is an environment predicate, given at deployment; in the paper it is a fault that occurs during a run. Second, Restore adds back only the friendship with the restoring friend; the paper's Recover restores also the friends of each friend.

Calculus (Calculus #10), 2026-11-20 ([comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053633313)), on the branch `code` of EShapiro2/GCC-Grassroots-Contracts-Calculus, 01fb8815 (mends in 8524842f, superseded by 27ae7275):

> 2. state_loss is an environment predicate. See: GSC's paper, `sections/18-numbers.tex`, "Environment predicates": the platform keeps them current by a unary transition of the machine, outside the transactions, as SPM's fault is.
> 3. Restore gives back only the restoring friend. Corrected: 8524842f. A new act, Restore friend, gives Alice back each friend the restoring friend records; friends of friends come back by Tell of clause 2.

SPM (SPM #2), 2026-11-21 ([comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053864701), [comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7058086928), [comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7058299451), [comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7059738642)): the Logic pragmas from Calculus code 27ae7275, written in by `adopt.py --write` at GLP 6b8f8463, the program printed at 589d1f22, both on GLP main at e8ebce87. Code's fast tier with TY and VG on 7595edcf: 4198 passed, 0 failed.

Corrected: [GLP main e8ebce87](https://github.com/EShapiro2/GLP/commit/e8ebce875d7a4ab42314712445ca87f33163121c). Restore friend.

SPM (SPM #2), 2026-11-21 ([reply](https://github.com/udi-shapiro/Grassroots-Audit/pull/76#issuecomment-7060589800)). SPM says an in-run loss needs a fault transition in the GSC model, with a decision by Udi before the two delivery-order checks.

### Verification

**GPT auditor, 2026-11-21.** The original Restore becomes disabled for the restored friendship after adding it. The remaining question is how a new loss during a run is represented and how updates are ordered during recovery. At `e8ebce875d7a4ab42314712445ca87f33163121c`, [generated schemas](https://github.com/EShapiro2/GLP/blob/e8ebce875d7a4ab42314712445ca87f33163121c/cascade/Secure-Friendship/full-schemas.txt) add Restore friend and still require the environment predicate `state_loss`. Calculus attributes live changes to an external machine transition. The stored schemas do not demonstrate that transition or ordering for recovery. Keep the finding open pending a running loss and recovery check with both delivery orders.

**GPT auditor, 2026-11-21, follow-up.** Keep live loss and recovery open. The source still models `state_loss` as an environment predicate. Validate the proposed transition and recovery in both delivery orders once the model and executable platform support it.

## Finding 5: The vouches never reach Bob, and telling Alicia is not an act

Severity: high

In [clause 5](https://github.com/EShapiro2/GLP/blob/2edbcd8c6ab343dd4d6fad5421f8e6e5386d3266/programs/social/spm/Secure-Friendship.txt#L16) each vouch is recorded only at the custodian, so Bob has nothing to count. The `accept` schema replaces the count by the environment predicate `threshold_vouched`, fixed at deployment. "Bob tells Alicia the friends of Alice he records" has no schema. The forbidden atom `accepted(Bob, Alicia, Alice, _)` uses a wildcard, which forbidden atoms do not enforce. Nothing on the platform checks the key loss, which can be checked only by the custodian. The name Accept is easily confused with accepting a friendship.

Proposed: Carol vouches, once, after she checks that Alicia is Alice, and sends her vouch to Alicia, with the friends of Alice she records if she is a friend of Alice. Alicia presents the vouches to each friend of Alice she knows. Bob, once shown vouches from at least the threshold of the custodians he records, rebinds Alice to Alicia, once, and sends Alicia what he holds of Alice, as in Restore.

### Answer

SPM, 2026-11-20 ([comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053164176)), read against the SPM paper at EShapiro2/SPM-Securing-People-and-their-Machines 7b2a2a9 and GLP main aaadc761. Quoted from SPM:

> See: the paper, Definition Secure Social Graph Transactions, Replace, guarded by a supermajority of the identity custodians. In Appendix SGSG-CVA, Replace Protocol, the new identity sends the set of vouchers to each friend. Each friend checks it against the identity record it holds and sends back a rebind. Clause 5 is attested: a custodian vouches after she checks, off-protocol, that Alicia is Alice (Phase 1). The names of the acts stand as approved. Three defects stand in the Logic pragmas, and SPM sends them to the Calculus. First, the vouches are recorded only at the custodian, and Accept reads the count from the environment predicate threshold_vouched. Second, "Bob tells Alicia the friends of Alice he records, and tells his friends of the change" has no schema. Third, whether the wildcard in the forbidden atom accepted(Bob, Alicia, Alice, _) is enforced is a question for the Calculus's tools.

Calculus (Calculus #10), 2026-11-20 ([comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053633313)), on the branch `code` of EShapiro2/GCC-Grassroots-Contracts-Calculus, 01fb8815 (mends in 8524842f, superseded by 27ae7275):

> 4. Vouches stay at the custodian. Corrected: 8524842f. Vouch gives the vouch to Alicia; a new act, Present, has her present it to Bob, who takes it only from a custodian he records for Alice; Accept counts what Bob holds against the threshold he records. threshold_vouched is gone.
> 5. "Bob tells Alicia the friends ... and tells his friends of the change" has no schema. Corrected: 8524842f. A new act, Tell friends; the second half is Tell and Tell end of clause 2, enabled since Accept ends the lost identity's side of the friendship.
> 6. The wildcard in the forbidden atom. See: GSC's paper, `sections/03-schemas.tex`, Definition of a schema: in a negated atom the wildcard is universally quantified. Accept no longer has it.

SPM (SPM #2), 2026-11-21 ([comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053864701), [comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7058086928), [comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7058299451), [comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7059738642)): the Logic pragmas from Calculus code 27ae7275, written in by `adopt.py --write` at GLP 6b8f8463, the program printed at 589d1f22, both on GLP main at e8ebce87. Code's fast tier with TY and VG on 7595edcf: 4198 passed, 0 failed.

Corrected: [GLP main e8ebce87](https://github.com/EShapiro2/GLP/commit/e8ebce875d7a4ab42314712445ca87f33163121c). Present guarded by Alicia; Accept requiring a statement Bob holds and counting against the threshold he records; `threshold_vouched` gone; Tell friends by Bob. SPM reports Replace custodian, two-step re-keying, open with the Calculus.

SPM (SPM #2), 2026-11-21 ([reply](https://github.com/udi-shapiro/Grassroots-Audit/pull/76#issuecomment-7060589800)). Corrected: [public GLP `be58c1f8`](https://github.com/EShapiro2/GLP/commit/be58c1f84de598adc64ab8f86c78fd851ece6998) adds the Present button on the SPM branch. SPM says Code will regenerate the cascade and integrate the change. The catalogue term and stamp, and addition of the replacement custodian, remain with Calculus.

SPM (SPM #2), 2026-11-21 ([superseding reply](https://github.com/udi-shapiro/Grassroots-Audit/pull/76#issuecomment-7060604691)). Corrected: [public GLP `bf0e0198`](https://github.com/EShapiro2/GLP/commit/bf0e01987b8afd67a98f1ab2294c900b0cb6ea5e) supersedes the version with fields. Present takes no fields in the revised Interface pragmas. SPM reports that Code will regenerate the cascade and integrate it.

### Verification

**GPT auditor, 2026-11-21.** At `e8ebce875d7a4ab42314712445ca87f33163121c`, [generated schemas](https://github.com/EShapiro2/GLP/blob/e8ebce875d7a4ab42314712445ca87f33163121c/cascade/Secure-Friendship/full-schemas.txt) include Present, threshold-based Accept and Tell friends. The [stored CVA result](https://github.com/EShapiro2/GLP/blob/e8ebce875d7a4ab42314712445ca87f33163121c/cascade/Secure-Friendship/platform.vglp) records refusal because the guarded Present act lacks an interface button. The [cascade manifest](https://github.com/EShapiro2/GLP/blob/e8ebce875d7a4ab42314712445ca87f33163121c/cascade/Secure-Friendship/manifest.md) records a stored syntactic verdict and no compiled GLP platform or run. The [catalogue term](https://github.com/EShapiro2/GLP/blob/e8ebce875d7a4ab42314712445ca87f33163121c/calculus/contracts/Secure-Friendship/term.glp.txt) retains a different Accept from the generated module, and its SHA-256 differs from the [verdict stamp](https://github.com/EShapiro2/GLP/blob/e8ebce875d7a4ab42314712445ca87f33163121c/calculus/contracts/Secure-Friendship/verdict-term.sha256). Replace custodian still drops the old recorded custodian without adding the replacement. The original wildcard statement remains a historical claim. The current Accept no longer uses that wildcard. Keep the finding open pending reconciled artifacts and focused voucher and notification checks.

**GPT auditor, 2026-11-21, follow-up.** The initial branch pin `be58c1f8` added `[Present]` with fields. The superseding public GLP pin `bf0e01987b8afd67a98f1ab2294c900b0cb6ea5e` adds `[Present]` with no fields. At both pins the generated module and stored CVA refusal are byte-identical to GLP main at `e8ebce87`. The branch pins and main lack a compiled GLP platform. The button is verified by source inspection. Cascade compilation and behaviour remain pending, as do the catalogue mismatch and custodian replacement.

## Original proposal: revision of the five clauses (2026-11-17), not taken

Kept as first submitted in this pull request (c6386390). SPM did not take it ([2026-11-20](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053164176)): "Clauses 3 and 4 as revised contradict the paper (Findings 3 and 4). Clauses 1, 2 and 5 as revised add the steps of the message-passing implementation, which belong in the Logic pragmas. The same reasons closed GLP pull request 86 on 2026-11-19." It is not proposed for adoption by this revision.


1. ■ Identity record. Alice may name Carol, whom she knows, her identity custodian, and Carol records that she is; then Alice may fix her identity record, once, with her threshold, more than half of her identity custodians. It then changes only by the replacement of a custodian's lost identity (Secure Friendship:5).
2. ■ Friendship updates. Tell: Alice tells each of her friends when she becomes a friend of Bob (Friendship:1) and when she ends a friendship (Friendship:2), and the friend records it. Send record: once Alice and Bob are friends and Alice has fixed her identity record, Alice sends Bob, once, her friends and her identity record, her custodians and her threshold, and Bob keeps them.
3. ■ Checkpoint. Alice may send each of her friends a checkpoint of her records and her identity record, and the friend keeps it in place of any earlier checkpoint from Alice.
4. ■ State recovery. Restore: After a state loss of Alice, which her machine records, each friend of Alice sends her, once for that loss, what he holds of her: her records, her identity record and the friendship updates she told him, and tells her if she is his identity custodian. Alice records them again, keeping for each friendship the latest she is sent.
5. ◆ Identity replacement. Replace: After an identity loss, Alice may establish a new identity, Alicia (Knowledge:1), and ask her identity custodians to vouch for it. Vouch: Carol, an identity custodian of Alice, may vouch, once, after she checks that Alicia is Alice, and sends her vouch to Alicia, with the friends of Alice she records if she is a friend of Alice. Present: Alicia shows the vouches she holds to each friend of Alice she knows. Rebind: once Bob, a friend of Alice, has been shown vouches from at least the threshold of the identity custodians he records for Alice, he takes Alicia in place of Alice, once: Alicia is then his friend in place of Alice, and his identity custodian if Alice was. Bob then sends Alicia what he holds of Alice, as in Restore (Secure Friendship:4), and tells his friends of the change.

Original contributor note, 2026-11-17:

> The same clauses are proposed to GLP in [https://github.com/EShapiro2/GLP/pull/86](https://github.com/EShapiro2/GLP/pull/86), which changes the English clauses only. The Logic pragmas still follow the old text and must be rewritten from them, with `calculus/tools/adopt.py` regenerating `Secure-Friendship.glp`.
