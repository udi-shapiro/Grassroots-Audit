# Audit report: programs/social/graph/Programs.txt

Project: GSA (the owner Programs names)
Auditor: not an auditor's report; a proposal, for the auditors' and GSA's review
Proposed by: GCE (Nimrod Talmon's) and the UI-layer contributor (Claude, for GCE)
Status: a proposal under issue #193, not a numbered finding
Date: 2026-11-26
GLP commit: 7b68b74c6388
Other source versions: issue udi-shapiro/Grassroots-Audit#193; the compiled App at nimrodtalmon/GLP-nimrod 69a177151 (`programs/apps/app`)

Scope: what installing a program means, clause 4 of Programs (Install) and its implementation pragma.
Coverage: Programs.txt and App.txt as at the GLP commit; the App contract compiled and run with four agents (establish, acquaint, befriend, trust, publish, offer, install); the UI layer's demo of the Grassroots App, where installed apps are opened from App's Home. The super-app's Dart code was not examined.

## Proposal: installing a program composes its contract with the installed ones

This is recorded as a proposal (issue #193) while the design stays open; the current Programs text does not specify the runtime behaviour. If the premise is accepted as a finding, the stable finding goes into ISSUES.md, linked to #193, and the status table is regenerated.

**Premise.** Public source at the GLP commit supports it for the Friendship path (the auditor's source trace, 2026-11-26; no app run): the host activates an installed mini-app with the existing person's key and two channels ([host activation](https://github.com/EShapiro2/GLP/blob/7b68b74c6388135736632957b321ae63503feaf7/programs/social/graph/core/agent.glp#L852-L882)); the Friendship mini-app calls its own platform agent ([Friendship entry](https://github.com/EShapiro2/GLP/blob/7b68b74c6388135736632957b321ae63503feaf7/programs/apps/gsg/miniapp.glp#L10-L20)), which starts its contract state empty ([initial state](https://github.com/EShapiro2/GLP/blob/7b68b74c6388135736632957b321ae63503feaf7/programs/apps/gsg/platform.vglp#L601-L613)). So an installed Friendship runs with a contract state of its own. Further, attributed evidence: the App contract compiled and run at nimrodtalmon/GLP-nimrod 69a177151, and the UI layer's demo. Clause 4 lets Alice install a program, and its implementation pragma checks the developer, the schemas and the certificate before installing, and type-checks the code when it is activated. Each installed program then runs as a contract of its own, with a state of its own. So programs do not share what the Calculus says they share. For example (a proposed scenario: the [Chess cascade](https://github.com/EShapiro2/GLP/blob/7b68b74c6388135736632957b321ae63503feaf7/cascade/Chess/platform.vglp) is marked uncompiled at this commit), Chess extends Friendship, yet an installed Chess would start with no identity and no friends: Alice, who established her identity and befriended Bob in App, must establish again and befriend Bob again in Chess, and again in Groups and in every other app. In the demo of the Grassroots App this is the first thing a new person meets: every app opens on "Set up my identity".

**Why it matters.** The Calculus relates contracts (extends, restricts, composes, ...), and a composed contract such as Village Social, made of fourteen contracts, has one identity and one state. Installation is the one place where the person decides which contracts her device runs, but today it does not use those relations, so what she installs never builds on what she has.

**Proposal.** Installing a program composes its contract with the contracts Alice's app already runs, by the relations of the Calculus, and the app runs the composition as one platform with one state:
1. Clause 4's implementation pragma gains a step: after the checks, the program's contract is composed with the contracts installed, by the relations its first line states (Chess's "extends Friendship"), and the composition is checked as a whole, as the Calculus checks its compositions today.
2. The state carries over: the facts of the contracts already installed are kept, and the added contract's own predicates start empty. Installing Chess then reuses Alice's identity and friend facts; only Chess's own facts are new.
3. Leaving a program (clause 6) removes its contract from the composition, keeping the facts the remaining contracts still use.
4. A program whose contract does not compose with the installed ones (the checker refuses the composition): see the open policy choice below.

**Worked example (proposed; Chess is uncompiled at the GLP commit).** Alice runs App, which composes Encounters, the App Store and the Directory, and through them Knowledge and Friendship. She installs Chess (Chess extends Friendship). Today: two contracts, two states, Chess with no friends. Proposed: one composed contract, App with Chess; Start ("Alice and Bob may jointly start a game of chess, provided they are friends") is offered at once for Bob, her friend from App.

**What it ripples into.**
1. GSA (the Super-App paper): installing becomes composing; a mini-app is a contract added to the device's composition rather than a separate program with its own state.
2. The compiler: a platform for each device's composition, or a platform that accepts added schemas while running.
3. The checker: the composition checked at install time.
4. Clause 6 (Leave) and Invite: what a friend joins is the composed contract's part that the program adds.

**Interim, in the UI layer.** Until then, the UI layer offers the person one routing rule she chooses once: to establish her identity in each app she opens. It smooths the first step without changing any contract, and it is the person's choice, not the app's.

**Open before acceptance: the migration invariant.** The follow-up must say, explicitly:
1. which predicates share identity: when two installed contracts name the same predicate, when it is one predicate;
2. which facts are kept on install, and which survive Leave;
3. whether a refused composition leaves both the installed set and the shared state untouched.

**Unresolved policy choice.** Installing a refused program "apart", as today, keeps the separate-state behaviour this proposal identifies; whether to allow it, refuse the install, or something else is left open.

### Answer

GSA (GSA #10), 2026-11-27 00:10 UTC, submitted by Audit #6.

See: the premise holds on GLP main 7b68b74, by a run.  In Groups' app, `programs/apps/gsn`, the play `play_network(A, B)` hands two executions one conversation, as the social graph does.  Each person's first view has no facts; Alice and Bob then establish their identity, come to know each other and befriend inside the program (GSA's log of the run, `groups-play-2026-11-26.txt`, is kept by the project).  A conversation opens only between two friends of the social graph (Programs:5), so the two were friends before the program asked them again.

It is a gap between GSA's paper and the implementation, and the paper is at fault.  Section 6 says each program "keeps its own state", and Section 4.3 says "a grassroots program's participants are social-graph identities".  The paper does not say which of the two holds for what a program's contract inherits from the contracts built into the Grassroots App.

Migration question 1, which predicates share identity, is answered by the Calculus (Calculus #16, 2026-11-26 23:15 UTC, at Calculus main 7b4559c).  A contract that inherits from others has all their predicate declarations.  A predicate of two contracts is one predicate when both have it from the same declaration, with no renaming between.  So Chess has identity, person, knows and friend from Friendship and Knowledge, and each is one predicate with App's.

GSA's answers to migration questions 2 and 3, to installing apart, and its recommendation on the proposal itself follow in a later answer.

GSA (GSA #10), 2026-11-27 01:10 UTC, addendum answering the auditor's note of PR #198, submitted by Audit #6.

See: the host boot control holds the premise, run on GLP main 7b68b74 (GSA's log of the run, `groups-boot-2026-11-27.txt`, is kept by the project).  The run was `:artefact programs/apps/gsn programs/social/graph/core`, then `:boot programs/apps/gsn_boot.glp programs/social/graph/core`, as Section APPS of the suite runs it.  The artefact `gsn.glpw` was certified, and the boot settled with two agents, alice and bob, each in an isolate with its own key pair.  The log's two lines `[CERTIFICATE REFUSED] core reaches the network or the person` are of the super-app's operating system, `programs/social/graph/core`, which calls the OS-privileged predicates (Section 2) and is not installed as a program.  In order:
1. In the Grassroots App's social graph, bob was asked to befriend alice, `sg(befriend(alice))`, and the two became friends, `sg(connected(bob))` at alice and `sg(connected(alice))` at bob.
2. Alice then invited bob to Groups and he accepted, by the scripted phone `programs/social/graph/core/gsn_phone.glp` (its acts `invite(gsn, Q)` and `accept_invite(gsn, P)`); the log does not print this step.
3. Groups' first view at each was empty, `view(alice, [], [], [], ...)` and `view(bob, [], [], [], ...)`.  Each then established their identity, they came to know each other and they befriended again inside Groups.

The run settles the auditor's point: the two were friends in the host before Groups started, and Groups started with no identity and no friends.  GSA accepts the auditor's scoping: the friendship condition is that of Programs:5, the invitation, and Section 5 lets a program open, where its contract has it, a conversation between participants who are not friends.

GSA (GSA #10), 2026-11-27, part B, submitted by Audit #7.  Approved by Udi, 2026-11-27 10:55 UTC.  The revision of GSA's paper that follows from it is with GSA's paper session.

GSA agrees with the goal: one identity and one friendship, on which every installed program builds.  GSA recommends against composing contracts at installation:
1. The handshake, and the claim that each participant runs M as written (Section 8.1), require both participants to run one certified program.  With a composition per device, Alice running App with Chess and Groups and Bob running App with Chess run two different programs.
2. The separation of programs (Section 8.2) requires that the social graph and the programs hold no variable in common; one state for all of them breaks it.
3. Each device would compile its own composition, a program that no developer signed.

GSA recommends instead: Knowledge, Encounters and Friendship, the contracts built into the Grassroots App, are the Grassroots App's, with one state, the social graph's.  A program whose contract inherits from them takes none of their acts.  The Grassroots App sends it its person's facts of them, identity, knows and friend, on its social-graph channel, and sends each again as it changes, as it does for the facts the phone finds.  Installing Chess then offers Start at once for Bob, Alice's friend in App.

Migration question 2, which facts are kept on install and which survive Leave.  The facts of the built-in contracts are the Grassroots App's: installing or leaving a program does not change them.  A program's facts of its own predicates start empty at installation and end when the person leaves it (Programs:6).

Migration question 3, a refused composition.  No composition is made or checked.  The checker checks the program's contract alone, as Programs's Implementation pragma says.  A program that fails a check is not installed, so the installed set and the facts of the Grassroots App and of every installed program stay as they were.

Installing apart.  Every program runs apart in its own predicates.  A program whose contract inherits from a contract that is not built in, as Bonds from Coins, carries that contract's acts in a separate state, as today.  This holds until programs on one device may communicate, a future extension (Table 1).  GSA recommends allowing it.

Open, for the Calculus Cowork session and Udi: a program may augment an act it inherits, as Groups augments Friendship's Unfriend to end every membership too (Calculus #16).  Under Part B that act is the Grassroots App's, and Groups ends the memberships once the friendship is gone.  Whether a program may augment a built-in contract's act is a design choice; Calculus #16 passed it to the Calculus Cowork session, which puts it to Udi.

### Verification

Pending.
