# Setting Compendium Rebuild: Pass 0 Pilot Findings

Companion to `setting-compendium-rebuild-plan.md` and `setting-compendium-pilot-brief.md`. Written at the end of Pass 0. It records what the six pilot pages showed about the templates, the rulings made while building them, and the stale campaign files those rulings leave behind. Nothing else in the plan starts until the template decisions in section 2 are answered.

## 1. Pilot pages

| Type | Page | Notes |
|---|---|---|
| Era | `setting/history/05-a-debt-in-blood.md` | Rulings applied; soul coins removed |
| Ward | `gazetteer/waterdeep/castle-ward.md` | 259 lines; 14 landmarks, 9 characters |
| Deity | `setting/deities/asmodeus.md` | FRHoF with SCAG fallbacks for alignment, domains, symbol |
| Organization pair | `setting/organizations/10-cassalanters.md`, `setting/faction-operations/10-cassalanters.md` | Operations page diffed line for line against `guides/factions/11-cassalanters.md` |
| Notable Figure | `setting/notable-figures/cassalanters/10-seffia-naelryke.md` | Roleplay paragraphs verified word for word |
| Villain | `setting/villains/xanathar.md` | Tables verbatim |

Research notes are in the session scratchpad only (`notes/ward-castle-research.md`, `notes/deity-asmodeus-research.md`). The Castle Ward note is the starting point for Pass 3, so rebuild it from `adventure-wdh.json` Ch.9 lines 31003-31027 if the scratchpad is gone.

## 2. Template decisions needed from the user

Each item shows the problem the pilot found and the recommendation.

1. **The Overview no longer ends the player-safe part of a page.** Notable Figure, Villain, Organization and Ward pages all carry GM material both above and below the player-safe `## Overview`. The Overview protects nothing unless the page is gated. Recommendation: treat everything except the Overview as the GM layer and wrap it in `gamemaster` blocks at the Foundry conversion, as Ember does with its own GM sections. The markdown order stays as is.
2. **Where unresolved facts live.** The era page carries `[conflict N]` tags and a numbered Conflicts list inside GM Notes. Recommendation: a deletable `> **[GM]** #### Draft Notes` callout at the bottom of any page that has open items, holding `[research]` and conflict items, so the prose pass can strip it in one move.
3. **Secret versus GM Notes.** The Secret callout is meant to be rare. Four pilot pages use one anyway. Recommendation: default to `#### GM Notes`; keep Secret for hidden facts that change play (the Cassalanter pact, Seffia's failed witness).
4. **Deity template gaps.** Ember deity pages have an Appearance section and a "Using X as a Deity" box. The plan has neither. The 5etools data supplies neither. Recommendation: add both as slots, filled in the wiki pass; add a rule for which name leads the epithet line (the one most Waterdhavians use); and add Plane and Typical Followers to the metadata.
5. **Ward length.** The page is about 250 lines. Recommendation: 8-10 landmarks and 5-6 characters per ward, one Secret, and a hidden-affiliation GM note only where it changes play. Wards with fewer sourced facts will be shorter.
6. **Ward At a Glance.** Ember's fields and the skill's overlap (Influences, Governance, Organizations). Recommendation: one merged set: District Type, Population, Lifestyle, Services, Primary Peoples, Languages, Religion, Governance, Influences, Architecture, Economy, Organizations.
7. **Villain Background slot.** The Villain template has no place for backstory. Recommendation: add `## Background` after the identity line.
8. **Era page details.** Keep the Volo aside optional; name the two GM blocks apart (Gamemaster's Summary and Lore Summary); drop the dated Timeline when the span is unknown.
9. **Faction operations.** The plan assumed the mechanics sat on the organization pages. They sit in `campaign/guides/factions/` (response teams, outposts, escalation, revelation list, and for player factions renown and missions). The pilot copied the Cassalanter guide text into `setting/faction-operations/10-cassalanters.md` and left the guide untouched. Decision: **move** (delete the guide pages and retarget inbound links at `guides/factions/01-overview.md:47`, `gm-guide/grand-game-in-play.md:103`, `gm-guide/structural-rules.md:26,90,122`, `setting/villains/cassalanters.md:57` and `CLAUDE.md`'s Factions Guide table) or **keep both** (duplication, which drifts).
10. **Foundry gating and the viewer.** Factions Guide pages are already read by the viewer. A new journal changes what the viewer shows; plan a rebuild after the move decision.

## 3. Rulings made during the pilot

Source-checked against `adventure-wdh.json`, the Alexandrian files and the campaign's newest pages. "Stale" means a campaign file lags the rest.

**Cassalanters**
- The pact was signed and Osvaldo taken three years ago (about 1489 DR). Stale: `history.md:43`, `deities/asmodeus.md`, the era page's old values.
- Osvaldo was fifteen when taken and is eighteen at campaign start. Stale: `history.md:46`.
- Osvaldo is held in the soundproofed attic, room C24 (`adventure-wdh.json` 20649-20665). Ammalia visits weekly and sits in the room outside the pentagram. Victoro has not entered in months. Stale: org page `:44` (basement), `history.md:46` (temple), `SOURCE_GUIDE.md:325` ("basement cell").
- The contract requires 999,999 gp **and** ninety-nine souls. The family holds about 500,000 gp; the Vault's 500,000 is the shortfall. Stale: `history.md:48`, `notable-figures/cassalanters/04-osvaldo-cassalanter.md:26` ("or").
- **Soul coins are dropped (user).** The ninety-nine souls are the poisoned feast guests. Outposts gather gold and ritual components. Still to change: `villains/cassalanters.md:38-39`, `guides/gm-guide/grand-game-in-play.md:53,67`, `setting/grand-game.md:34`, and the outpost design in the Cassalanter content of `structure/arc-e`. The retired chapter files still mention coins; leave them.
- Motive: financial ruin was the trigger; the deal also bought power, health and long life. Delete "ambition, not desperation" (`history.md:44`, org page `:63`). Open: the link from Neverember's embezzlement to the ruin is campaign-invented (`arc-g:11`).
- Founders' Day (Flamerule 1) is the feast and Ammalia's real deadline, chosen for civic cover and time to verify the terms (`design-notes-running-the-campaign.md:69`). Flamerule 11 is the contract due date. Delete the "soul erosion" rationale.
- Victoro is a public Lathander worshipper and the house is publicly known for Siamorphe (both in the published adventure). "Three centuries" is in no source; use "several generations".
- **CLAUDE.md secrecy rule (user):** now reads "outside the household and the cult". Hurv Taldred's page needs no change.
- Wider stale lines: `arc-g:13` ("nightly"; should be weekly, in the room), `arc-g:19`, `arc-g:83` (Willifort's eight years, no source), `arc-g:531` (Harpers "hold documentation of the infernal contract", breaks the secrecy rule), `history.md` Era 5 (replaced wholesale in Pass 1), `SOURCE_GUIDE.md:651` (Founders' Day labelled Alexandrian).

**Xanathar's Guild**
- Xanathar is "it" (user ruling; the published adventure uses "it"). The current Xanathar is named Kirukesai (user-supplied; in no source).
  - Files still using "he/his" for Xanathar: `notable-figures/xanathars-guild/01-xanathar.md` (13, 15, 17, 23, 25, 27, 31), `organizations/08-xanathars-guild.md` (13, 15, 17, 24, 26), `guides/gm-guide/running-the-villains.md` (21, 54, 71, 73), `grand-game-in-play.md` (63, 72), `guides/factions/09-xanathars-guild.md` (35, 67), `structure/arc-f` (9, 11, 13, 15, 99, 114, 200, 223, 368, 414, 416), `arc-j` (19, 195), `arc-h:360`, `arc-e:81`, and quest events: `gralhund-villa/ev-08:59`, `trollskull-alley/ev-05:65,89`, `lords-alliance/m05/ev-02:130`, `bregan-daerthe/m04` (design-notes:15, overview:27, ev-01:20).
- The guild name is always "Xanathar's Guild" (user ruling). About 160 hits in 68 files use the form without the possessive. Re-run `grep -rn "Xanathar Guild" campaign --include=*.md` and skip `structure/arc-a` to `arc-d` and `ch1`-`ch3` (retired).
- Vault motive: the gold as proof of supremacy and rule over the underworld. It knows the Stone is the key to the vault, but not what the Eye in Sylgar's bowl does, that there are three, or where the vault is. Outliers: `organizations/08-xanathars-guild.md:17` and `arc-j:19` ("kept hidden as leverage"). Open: the Alexandrian briefing says "one of Three"; the campaign's X12 briefing must omit that line.
- Nihiloor has been dominating Xanathar for four months (`arc-f:13,178,408`, org page `:24`). Stale: `notable-figures/xanathars-guild/04-nihiloor.md:22,26` ("equal, no interest in supplanting"). Open: `arc-f:408` says every decision attributed to the beholder was Nihiloor's, which affects the motive and Manshoon rulings.
- Nar'l: Xanathar suspects disloyalty and has set a grell to kill him at the first proof; it does not know he reports to Bregan D'aerthe. Stale: `grand-game-in-play.md:63`, `running-the-villains.md:71,73`, `01-xanathar.md:27`. Tenure is inconsistent (one year in the published adventure; three years in `03-narl:22` and org `:23`; eleven years/months in `arc-f:17,169`).
- Manshoon: an active, low-level street war in the Dock Ward. Stale: `running-the-villains.md:71` ("Cold war").
- Ambition: Guild members survive by hiding their ambitions behind obedience (`history.md:27` and the villain page now say so).
- Side notes: the published adventure never says "goldfish"; Eye #1's origin differs (`running-the-villains.md:21` Neverwinter vs `arc-f:9` drow courier on the Trade Way).

**Castle Ward (from the ward drafter and the research note)**
- `waterdeep-lore.md:14` puts the Watch headquarters and the Masked Lords' seat in the ward (the published adventure has neither); the Palace audience chamber is where petitioners meet the Masked Lords.
- `waterdeep-lore.md:36-37` puts the Tymora and Selûne temples in the Sea Ward; the published adventure is internally split on the Tower of Luck. `player-factions-overview.md:99` puts the Temple of Helm in the Castle Ward; the published adventure puts Helm's Hall in the Southern Ward.
- `waterdeep-lore.md` calls the ward "South Ward" and puts Kolat Towers in the Trades Ward; the published adventure says Southern Ward for both.
- `waterdeep-lore.md:50` says the dragonward blocks dragons "without the Open Lord's permission"; the published adventure says they are physically unable to enter unless touched by the dragonstaff of Ahghairon.
- `waterdeep-lore.md:51` calls all eight statues 90 feet and dormant; the published adventure gives 90 feet only for the original statue.
- `waterdeep-lore.md:27-28` and `grand-game.md:26`: Barnibus is a Watchful Order investigator with a Sea Ward estate, not clearly a magistrate; "personally compromised" and "1,200 guards" have no source.
- `SOURCE_GUIDE.md:214` puts Yellowspire in the Trades Ward; the published adventure and the campaign say Castle Ward.
- Mirt's Mansion: the Castle Ward section of the published adventure places it near the Naval Harbor; another passage and the campaign's Harper event say Sea Ward.
- Laeral's "moon elf, chaotic good" is campaign-only. Durnan as a Masked Lord is campaign-only (the published adventure names Mirt).
- `Brother Haldric Wence` is the Order's clerk (`guides/factions/05-order-of-the-gauntlet.md:64`), not a door-warden.

## 4. Wiki-dependent fields (Passes 2 and 3)

- Wards: Population, Lifestyle, Primary Peoples, Languages and dominant faith are unsourced for the Castle Ward and probably for most wards. Ward boundaries and street grid, Watch garrison size, which Masked Lords live where, prices and rents.
- Deities: Areas of Concern, Appearance, history/origin, relations with other gods, local worship in Waterdeep, and alignment/domains/symbol for FRHoF-only entries. Asmodeus's relations with the other archdevils are not in the 5etools data.
- The wiki host `forgottenrealms.fandom.com` is blocked by the cloud environment's network policy. It needs adding under Allowed domains in the environment settings before those passes.

## 5. Process notes

- Drafters have no shell, so `voicecheck.py`, stale-reference greps and diffs run in the main session. Budget for one review pass per page.
- Two agents hit the account rate limit in the same minute; resume them with SendMessage after the reset.
- Pilot commits are on `claude/trusting-pasteur-a76rfy` and are not merged to master: the templates are not approved yet.
