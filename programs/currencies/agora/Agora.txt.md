# Audit report: programs/currencies/agora/Agora.txt

Project: Currencies (Agora's owner); finding by GCE (Grassroots Contract Examples), Nimrod Talmon's, with Claude
Auditor: Claude (Opus 5.5), for GCE; verification by Grassroots GPT auditor
Date: 2026-11-25
GLP commit: b579ce0d5973082f26e759529202c9c5931fb8bf
Other source versions: GLP main `37d31ca95c6a599113dcf6eb0b8341f8202c3a47`; candidate `bf36ba77bfa9442944f049a27a7dd033308e46d6`, one commit after `c63b27ed9618f112d18db06b3329c94f5c7b70b6`
Ticket: [#140](https://github.com/udi-shapiro/Grassroots-Audit/issues/140) · Source PR: [#141](https://github.com/udi-shapiro/Grassroots-Audit/pull/141) · Index: [ISSUES.md](../../../ISSUES.md)

Scope: whether Withdraw's required atoms bind its places in the initiator's own state.
Coverage: at the pinned commit, Agora's [expanded schemas](https://github.com/EShapiro2/GLP/blob/b579ce0d5973082f26e759529202c9c5931fb8bf/calculus/contracts/Agora/full-schemas.txt#L34-L43), [compiled term](https://github.com/EShapiro2/GLP/blob/b579ce0d5973082f26e759529202c9c5931fb8bf/calculus/contracts/Agora/term.glp.txt#L24-L25) and [adopted interface](https://github.com/EShapiro2/GLP/blob/b579ce0d5973082f26e759529202c9c5931fb8bf/calculus/contracts/Agora/interface-adopted.txt#L10-L11), read as source; Offer, Want and Deliver only as they bear on Withdraw. Candidate source and generated artifacts at `bf36ba77bfa9442944f049a27a7dd033308e46d6` were inspected separately. No GLP runtime or UI was run. Not examined: Notes, Coins, Bonds and Agora's other acts.

## Finding 1: Withdraw does not require the member's own record of her post

Severity: low

Clause 5 lets a member withdraw her post. In the schemas, Withdraw, initiated by an ordinary member Carol, requires `post(Alice,Carol,Item,Mart)`, the keeper Alice's wall record of the post, and the copy of each member it was delivered to. Those atoms are held by others. Of Withdraw's required atoms, Carol holds only identities, and none binds Alice, Item or Mart. The adopted interface accordingly gives Withdraw three open fields, `<alice> <item> <mart>`. Withdraw own differs: its initiator is the keeper, the required `post(Alice,Alice,Item,Mart)` is hers and binds Item and Mart, and its interface line has no fields.

The condition used here is sufficient. A place can be filled from the initiator's state when a required atom she holds contains it. A UI could also use other local data. Carol holds `posted(Carol,Item,Mart)` and may hold `member(Carol,Mart,Alice)`, but Withdraw at the audited version does not require them. The gap concerns the required atoms and the current interface.

Proposed correction: Withdraw also requires that Carol has posted Item to Mart and is a member of the market Mart of Alice. Both facts are in Carol's state. `posted` binds Item and Mart, while the selected `member` fact binds Alice. This does not require membership or keeper uniqueness. Carol can hold more than one membership fact for the same market name through different paths; the keeper-side requirement `post(Alice,Carol,Item,Mart)` selects a membership whose keeper still has the active post. The no-repost history stays because Withdraw removes neither `posted` nor `member`, and Offer and Want require that Carol has not posted Item to Mart.

Binding the places differs from listing only active posts.

1. Before delivery to the poster, Carol holds `posted` and `member`, Alice holds the wall post, and Carol holds no local wall copy. The added facts bind the places locally and the keeper check determines whether Withdraw applies.
2. After delivery to the poster, Carol conditionally also holds `post(Carol,Carol,Item,Mart)`. Withdraw removes that copy along with the keeper's and other delivered copies.
3. After withdrawal, Carol still holds `posted` and `member`, while the wall records are gone. The places remain bound, the keeper check fails, a second Withdraw is refused, and Offer and Want refuse to post Item to Mart again.

With the correction an interface can derive a Withdraw choice from Carol's historical `posted` and `member` facts. Withdrawn posts can still produce such a choice and are rejected by the keeper-side active-post check. Listing only active posts from Carol's state would require a local record present before delivery and removed by Withdraw. That is a separate design choice.

### Answer

Corrected: Currencies (Currencies #24), 2026-11-26 02:56 UTC, submitted by Audit #5. GLP branch `currencies-agora-withdraw-2026-11-26` at `bf36ba77bfa9442944f049a27a7dd033308e46d6` adopts Agora on top of `claude/project-thread-otalyn` at `c63b27ed9618f112d18db06b3329c94f5c7b70b6` (the Calculus contribution is identified there as `c176c60`). It is not on GLP main. Withdraw now requires at Carol's role that Carol has posted Item to Mart and is a member of Mart of Alice. The answer states that these facts bind the keeper, item and market, and that the interface is `Withdraw: Carol [Withdraw]` with no fields. Currencies reports that `adopt.py --check` passed and `cascade.sh agora` returned `syntactically_grassroots` with the platform compiled. Currencies will provide the eventual main commit. [Source comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/141#issuecomment-7181256829)

Currencies (Currencies #24), 2026-11-26 08:44 UTC, submitted by Audit #5.

Corrected: public GLP main `a9d40778a7587dd45ea25aacb42f51146a8ab0d9`, merged at 08:25 UTC, which contains `bf36ba77bfa9442944f049a27a7dd033308e46d6` and its parent `c63b27ed9618f112d18db06b3329c94f5c7b70b6`. Audit #5 reports checking that both cited commits are ancestors of main. [Source comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/178#issuecomment-7186960980)

### Verification

Partly verified by source inspection on 26 November 2026. The public branch resolves exactly to `bf36ba77bfa9442944f049a27a7dd033308e46d6`. GitHub's commit graph shows that it is one commit ahead of `c63b27ed9618f112d18db06b3329c94f5c7b70b6`. The candidate's expanded schema and generated GLP term require all three of `posted(Carol,Item,Mart)`, `member(Carol,Mart,Alice)` and the keeper's active `post(Alice,Carol,Item,Mart)`. Its adopted interface is exactly `Withdraw: Carol [Withdraw]`. The corresponding generated program and cascade artifacts change in the same commit, and the checked-in verdict says `syntactically_grassroots`.

This source inspection verifies the claimed binding change without assuming a unique membership or keeper. It also confirms that Carol's wall copy is conditional on delivery to the poster, while `posted` and `member` are already local before that delivery. The keeper's `post` remains the active-post check, and the historical `posted` fact remains after withdrawal.

The project-reported `adopt.py --check` and `cascade.sh agora` executions were not independently rerun in this verification. Public GLP main `37d31ca95c6a599113dcf6eb0b8341f8202c3a47` still has the old Withdraw schema and the three-field interface. The finding remains open pending integration on GLP main and independent regeneration and cascade checks at the integrated commit.

**Integration follow-up, 26 November 2026.** GitHub's commit graph independently confirms that `bf36ba77bfa9442944f049a27a7dd033308e46d6` and `c63b27ed9618f112d18db06b3329c94f5c7b70b6` are ancestors of public GLP main `a9d40778a7587dd45ea25aacb42f51146a8ab0d9`. Main's expanded schema, interface, generated term, generated program and checked-in verdict are byte-identical to the candidate artifacts. A standalone exact-main check passed 9 of 9 source assertions and 4 of 4 bounded Withdraw projections: Carol's local `posted` and `member` facts bind the values, the keeper's `post` remains the active-post check, withdrawal removes it, and a second withdrawal is blocked while the historical local facts remain.

This verifies source integration and the reported binding behavior. The checked-in verdict reads `syntactically_grassroots`; it was inspected rather than regenerated. The adoption checker, cascade, GLP runtime and UI were unavailable and were not executed. Finding #140 remains open for independent regeneration and cascade execution at the integrated commit.
