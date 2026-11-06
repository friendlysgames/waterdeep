# Setting Compendium Rebuild: Pass 1 (History) Brief

Binding brief for every Pass 1 drafter. It adds to, and does not replace, `docs/plans/setting-compendium-pilot-brief.md` (draft register, page frame, report format, rules 1-10). Read that brief, the Page templates and Page rules in `docs/plans/setting-compendium-rebuild-plan.md`, and the approved model page `campaign/setting/history/05-a-debt-in-blood.md`. Copy that page's shape for every Era page.

## What changed since the pilot brief

1. **The wiki is available, offline.** Pre-extracted Forgotten Realms Wiki pages (raw wikitext, current to 21 Oct 2026) are in `/tmp/claude-0/-home-user-waterdeep/283da031-9ebf-5164-82ad-20ed9fcff02f/scratchpad/research/wiki/*.txt` (one file per page; large pages need `offset`/`limit` reads). It is source rank 4: campaign files and the published adventure outrank it. Take facts and paraphrase; never copy its prose. Record each page used in Source References as `Forgotten Realms Wiki, <Page title> (edition cited: <book/edition>)`. If you need a wiki page that is not in the folder, say so in your report; do not guess.
2. **Approved template rules** (rebuild plan, "Page rules"): everything except the player-safe Overview is the GM layer; open items go in one deletable `> **[GM]**` `#### Draft Notes` callout at the very bottom (Research, Conflicts, Routed facts); `#### GM Notes` is the default GM callout and `#### Secret` is reserved for hidden facts that change play; inline `[research]` tags stay in place; the `~Volo` aside is optional; no dated Timeline when the span is unknown.
3. **Rulings that bind this pass** (findings note section 3): Xanathar is "it/its"; the current Xanathar is a beholder named Zushaxx and Kirukesai was one of the previous Xanathars; the guild is always "Xanathar's Guild" (never "Xanathar Guild"); Cassalanter pact facts are settled on the Era 5 page (read it; do not contradict it); Cassalanter secrecy rule in CLAUDE.md applies (nobody outside the household and the cult knows, except Jarlaxle through Vessa); Bregan D'aerthe has rejected Lolth; two Zhentarims; no soul coins.
4. **Stale source warning.** The old `campaign/setting/history.md` is an older outline and some of its facts are stale. Move its facts, but where a fact conflicts with a campaign page written later (Notable Figures, Villains, Organizations, quest and location journals, GM Guide), the newer page wins; put the conflict in Draft Notes with both file:line references. Do not copy Era 5 from it.
5. **Verification before use.** Verify every NPC, faction and place name against `campaign/setting/` and `campaign/locations/` before using it. Check dates, offices and relationships against `sources/adventure-wdh.json` and the wiki before stating them. Anything none of these settles is `[research]`.
6. Until the prose pass, every page may carry its full GM information, including in the Overview. The prose pass writes the player-safe version of each Overview (the Zardoz Zord rule, the Cassalanter secrecy rule and the spoiler rule apply then).

## Page set (file names fixed; Era 5 already exists)

| File in `campaign/setting/history/` | H1 | Reads (besides history.md and the wiki files) |
|---|---|---|
| `00-the-history.md` | The History (hub) | all child pages |
| `01-ahghairons-gifts.md` | Ahghairon's Gifts | `waterdeep-lore.md` (governance, dragonward) |
| `02-the-long-shadow.md` | The Long Shadow | `villains/xanathar.md`, `organizations/08-xanathars-guild.md` |
| `03-bregan-daerthes-long-road.md` | Bregan D'aerthe's Long Road | `villains/jarlaxle.md`, `organizations/07-bregan-daerthe.md` or the matching file |
| `04-the-founding-of-chains.md` | The Founding of Chains | `villains/manshoon.md`, Zhentarim and Doom Raiders organization pages |
| `05-a-debt-in-blood.md` | A Debt in Blood | already done, do not edit |
| `06-the-open-lords-fall.md` | The Open Lord's Fall | `waterdeep-lore.md`, `villains/` pages, Renaer's and Laeral's Notable Figures pages |
| `07-a-city-watching-itself.md` | A City Watching Itself | `grand-game.md`, Laeral's Notable Figures page |
| `08-the-players-arrive.md` | The Players Arrive | `guides/gm-guide/structural-rules.md`, `running-the-villains.md`, quest journals Finding Floon and Fireball! (overviews only) |
| `09-timekeeping-and-the-festival-calendar.md` | Timekeeping and the Festival Calendar | `waterdeep-lore.md` lines 41-47, `guides/gm-guide/structural-rules.md`, Calendar of Harptos wiki pages |

Era 5's span and Timeline are being researched separately. Do not touch it.

## Era page body (from the rebuild plan, as the model page implements it)

Metadata (Keywords, Span, Other Names); Gamemaster's Summary; Lore Summary (3-6 bullets); narrative H3s, one per beat group of the old era block; optional `~Volo` quote slot, at most one per page and only when it adds something; `## Overview` (player-safe prose, 2-4 sentences, public history only); Secret/GM Notes only when needed; Draft Notes last. Fill the Span from sources where a year is sourced (`1035 DR` for the wards, and so on); otherwise write the relative span and mark `[research]`. If the old block's "time before campaign" is stale or unsourced, say so in Draft Notes. Verbatim facts move; invented flavor does not.

## Rules specific to the Timekeeping and Festival Calendar page

Include the Calendar of Harptos basics the campaign uses (tenday, months, the festival days between months), the campaign calendar (Ches 1 start, Ches 20 Grand Opening, Tarsakh 20, Flamerule 1 Founders' Day, Flamerule 11), and the festival table from `waterdeep-lore.md` lines 41-47 with its campaign function column. Settle any date conflicts against `structural-rules.md` and the quest overviews (they win), and list conflicts in Draft Notes. Founders' Day belongs on this page, not duplicated on the Era 5 page.

## Report format

As in the pilot brief, plus: for each page, the old-block bullets and where each landed (a table), the wiki pages used, every conflict found (file:line both sides), and every fact you could not house.
