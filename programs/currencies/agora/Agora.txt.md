# Audit report: programs/currencies/agora/Agora.txt

Project: Currencies (Agora's owner); finding by GCE (Grassroots Contract Examples), Nimrod Talmon's, with Claude
Auditor: Claude (Opus 5.5), for GCE
Date: 2026-11-25
GLP commit: b579ce0d5973082f26e759529202c9c5931fb8bf
Other source versions: none
Ticket: [#140](https://github.com/udi-shapiro/Grassroots-Audit/issues/140) · Index: [ISSUES.md](../../../ISSUES.md)

Scope: whether Withdraw's required atoms bind its places in the initiator's own state.
Coverage: at the pinned commit, Agora's [expanded schemas](https://github.com/EShapiro2/GLP/blob/b579ce0d5973082f26e759529202c9c5931fb8bf/calculus/contracts/Agora/full-schemas.txt#L34-L43), [compiled term](https://github.com/EShapiro2/GLP/blob/b579ce0d5973082f26e759529202c9c5931fb8bf/calculus/contracts/Agora/term.glp.txt#L24-L25) and [adopted interface](https://github.com/EShapiro2/GLP/blob/b579ce0d5973082f26e759529202c9c5931fb8bf/calculus/contracts/Agora/interface-adopted.txt#L10-L11), read as source; Offer, Want and Deliver only as they bear on Withdraw. No GLP runtime or UI was run. Not examined: Notes, Coins, Bonds and Agora's other acts.

## Finding 1: Withdraw does not require the member's own record of her post

Severity: low

Clause 5 lets a member withdraw her post. In the schemas, Withdraw, initiated by an ordinary member Carol, requires `post(Alice,Carol,Item,Mart)`, the keeper Alice's wall record of the post, and the copy of each member it was delivered to. These atoms are held by others. Of Withdraw's required atoms, Carol holds only identities, and none binds Alice, Item or Mart. The adopted interface accordingly gives Withdraw three open fields, `<alice> <item> <mart>`. Withdraw own differs: its initiator is the keeper, the required `post(Alice,Alice,Item,Mart)` is hers and binds Item and Mart, and its interface line has no fields.

The condition used here is sufficient, not necessary: a place can be filled from the initiator's state when a required atom she holds contains it. A UI could also use other local data; Carol does hold `posted(Carol,Item,Mart)` and `member(Carol,Mart,Alice)` today, but Withdraw does not require them. So the gap is in what the required atoms and the current interface do, not in what every possible UI must do.

Proposed correction: Withdraw also requires that Carol has posted Item to Mart and is a member of the market Mart of Alice. Both facts are in Carol's state, so the condition stays local. `posted` binds Item and Mart, and `member` then binds Alice, since Join allows one membership per market name. The keeper-side requirement `post(Alice,Carol,Item,Mart)` stays, and so does the no-repost history: Withdraw removes neither fact, and Offer and Want require that Carol has not posted Item to Mart.

Binding the places is not the same as listing only active posts. `posted` and `member` are history:

1. Before delivery: Carol holds `posted` and `member`, Alice holds the post. The places are bound locally, the keeper check holds, and Withdraw applies.
2. After delivery to the poster: Carol also holds her wall copy `post(Carol,Carol,Item,Mart)`. As in case 1; Withdraw also removes her copy.
3. After withdrawal: Carol still holds `posted` and `member`, and no wall record of the post remains. The places are still bound, but the keeper check fails, so a second Withdraw is refused, and Offer and Want refuse to post Item to Mart again.

So with the correction an interface can offer Withdraw for each of Carol's `posted` facts, withdrawn posts included; the keeper refuses those. Listing only active posts from Carol's state would need a record at Carol that Withdraw removes. Before delivery Carol holds none, since her wall copy arrives only by Deliver to poster. That is a separate choice and is not proposed here.

### Answer

Awaiting a project response.

### Verification

Pending verification.
