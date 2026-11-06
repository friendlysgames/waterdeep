# Session 47 Handoff
**Date:** 2026-11-06
**Status:** Ready to continue. Pass 0 (pilot alignment) and Pass 1 (History) are complete and merged to `master`; a full consistency pass over the History journal and the live campaign files is merged. The Factions Guide move, Pass 2 and Pass 3 have not started. A short list of design decisions needs the user (see Outstanding Work, "Decisions needed").

---

## What Was Done

The session finished the setting-compendium template work and then ran Pass 1. The user answered the five template decisions, and the pilot pages were brought into line. A way around Fandom's bot block was found: its official S3 database dump, now used as an offline wiki. Research agents then gathered facts per era, and prose drafters wrote the new `campaign/setting/history/` journal (hub, eight era pages, Timekeeping and the Festival Calendar) and deleted the old `history.md`. The user then ruled on the open design questions, and five consistency checkers and five fix batches applied those rulings across about 145 files. Volo's written voice was added to the skills from the PDF the user supplied, and his four asides were rewritten. Everything is merged ([PR 184](https://github.com/friendlysgames/waterdeep/pull/184) and [PR 185](https://github.com/friendlysgames/waterdeep/pull/185)).

---

## Changes Made

Git range: `97e5495..HEAD` (the "Session 46 handoff" commit to the PR 185 merge, `3721310`); 145 files changed, +2,114 / −604.

### Files Modified (by area)
| Area | What changed |
|------|-------------|
| `campaign/setting/notable-figures/` (25 files) | "Xanathar's Guild", Xanathar as "it", Nihiloor's four-month domination of Xanathar, Nar'l one year placed 1491, Laeral/Mirt advisor inversion, the twins' forfeit on Flamerule 11, Osvaldo nine then and twelve now, Ryvarra two weeks, Jarlaxle's three settled facts, Seffia's mission as an Eye |
| `campaign/setting/` pilot pages | `deities/asmodeus.md`, `villains/xanathar.md`, `organizations/10-cassalanters.md`, `faction-operations/10-cassalanters.md`, `history/05` aligned to the approved templates; Asmodeus pact moved to a Secret; wiki answers (rise, court, doctrine) added |
| `campaign/gazetteer/waterdeep/castle-ward.md` | Trimmed to 9 landmarks and 6 characters; six Castle Ward statues; boundaries, 1035 founding, Watch base, garrison, city-level figures from the wiki |
| `campaign/setting/` other (villains, organizations, `grand-game.md`, `waterdeep-lore.md`) | Guild name, pronouns, no soul coins (999,999 gp and ninety-nine souls), Doom Raiders arrived first, Istrid in the Dock Ward, Walking Statues dormant except the Griffon, retired "ch2" banners removed |
| `campaign/guides/` (gm-guide, factions, trollskull-manor, players-guide) | Guild name, pronouns, GM not DM, active street war not a cold war, Founders' Day feast as the real deadline and the twins' birthday as the contract's due date, ousted not exiled, Interrogation House in the North Ward |
| `campaign/quests/` (act-i, act-ii, faction-events) | Guild name, pronouns, GM not DM, Floon taken last night, Renaer the former Open Lord's son, Yellowspire in the Castle Ward, carnival fleet arrives Ches 21 while the submarine is moored all year, Nar'l one year |
| `campaign/locations/` | Xanathar Sewer Hideout gets the "The Missing Eye" GM block and a Q03 strongbox; Faire overview and `05-scarlet-marpenoth.md` say Eye #3 is kept in U4; warehouse files corrected |
| `campaign/structure/arc-e` to `arc-j` | Eye #1 from the Protector's Enclave, Manshoon holds no Eye, Nar'l one year, Faire timing, Guild name, pronouns, GM not DM, exile wording |
| `.claude/skills/character-voices/voices/independents-allies.md` | New "Volo's written voice" section |
| `.claude/skills/ember-setting-style/SKILL.md` | Historian Aside rules: Volo's voice, 2 to 5 sentences, at most two parentheses; "Xanathar's Guild" in an example |
| `.claude/skills/character-voices/voices/xanathars-guild.md`, `manshoons-zhentarim.md`, `cassalanters.md` | Xanathar "it"; Manshoon's simulacra; Osvaldo "twelve-year-old" voice |
| `.claude/skills/adventure-reloaded/SKILL.md`, `CLAUDE.md` | Setting table and skill pointers retargeted to the History journal |
| `docs/plans/setting-compendium-rebuild-plan.md`, `setting-compendium-pilot-findings.md` | Approved template decisions and page rules recorded; Osvaldo ruling |
| `.claude/skills/update-campaign-viewer/references/viewer-template.html`, `docs/index.html` | Gazetteer added to the journal order; viewer rebuilt |

### Files Created
| File | Purpose |
|------|---------|
| `campaign/setting/history/00-the-history.md` | Hub page |
| `campaign/setting/history/01-ahghairons-gifts.md` … `04-the-founding-of-chains.md`, `06-the-open-lords-fall.md`, `07-a-city-watching-itself.md`, `08-the-players-arrive.md` | Era pages (Era 5 already existed from Session 46) |
| `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md` | Calendar of Harptos, campaign calendar, festival table, Founders' Day |
| `docs/plans/setting-compendium-pass1-brief.md` | Binding brief for Pass 1 drafters (approved template rules, rulings, offline wiki) |
| `docs/plans/setting-compendium-research-notes/` (9 files) | Era research findings and the five consistency-checker reports. **Read these for the unresolved items.** |
| `scripts/fandom-dump/` (`README.md`, `build_index.py`, `getpage.py`) | Rebuild the offline Forgotten Realms Wiki from Fandom's official S3 dump |

### Files Deleted
| File | Reason |
|------|--------|
| `campaign/setting/history.md` | Every block has a home in the new History journal; inbound references retargeted first |

---

## Key Decisions

### Template decisions (the five from the findings note)
**Decision:** Items 1 to 3 adopted as recommended (everything except the Overview is the GM layer; open items in a deletable Draft Notes callout; GM Notes by default, Secret reserved). Deity template adopted **except Appearance**. Ward, Villain and Era trims adopted. Factions Guide pages **move** to `setting/faction-operations/`. The move is **not yet executed**.
> "add all except appearance" — User, this session (deity template)

### The wiki is read from Fandom's official S3 dump
**Decision:** Fandom's Cloudflare challenge blocks automated fetches, so the wiki is read from `s3.amazonaws.com/wikia_xml_dumps/f/fo/forgottenrealms_pages_current.xml.7z` (dated 21 Oct 2026, 173,049 pages). The user pointed out the wiki carries material from games, books and comics that the 5e books do not.
> "wiki contains information from other sources, such as games, books, or comics, which could be useful for lore reasons" — User, this session

### Research agents come before drafters, with the wiki in the prompt
**Decision:** Per the plan's loop, `source-researcher` gathers facts and the findings are saved; only then does `prose-drafter` write.
> "why are you not using a research agent? And include the wiki in the research agent prompt" — User, this session

### Every Cassalanter child is taken at nine
**Decision:** Osvaldo was already nine when the pact was signed (about 1489 DR), so Asmodeus took him at once; he is twelve now (born about 1480, arithmetic). The twins are eight and forfeit at nine on Flamerule 11, 1492.
> "make it so he was taken at 9 years old, so that all kids are taken at 9 years old" — User, this session

### The remix overrides the published X33 detail
**Decision:** The current Xanathar believes it is the original.
> "Yes. Remix overtakes original campaign." — User, this session

### Jarlaxle has known about the vault since reaching Waterdeep
**Decision:** He has known of the Stone, the Eyes and the vault since he reached Waterdeep (in the city by Marpenoth 3, 1491). The *Jarlaxle Informed* outcome records only that the party spoke with him.
> "He's known about it since getting to Waterdeep, whenever that was." — User, this session

### The locket Eye reached Jarlaxle through Xanathar's hideout
**Decision:** The Zhentarim opened Renaer's locket at the warehouse; Xanathar's Guild raided the warehouse and carried the Eye off without knowing what it was; Bregan D'aerthe agents inside the hideout lifted it the night before Ches 1; Manshoon never held it. The chain is the main session's reading of the user's answer.
> "Jarlaxle has men in Xanathar's hideout." — User, this session

### Drafts carry full GM information until the prose pass
**Decision:** The player-safe Overview rule is suspended; the prose pass writes the player-safe versions.
> "write all the GM information for now for everything. We will obfuscate player versions in prose pass later" — User, this session

### The four big consistency rulings
**Decision:** The Scarlet Marpenoth submarine has been in harbor all year and the carnival fleet and parades arrive Ches 21 (option "Sub in harbor all year (Recommended)"); Nar'l has been in the Guild one year, placed 1491 ("One year, placed 1491 (Recommended)"); the hideout gets a short Bregan D'aerthe beat ("Add a short beat (Recommended)"); Renaer stays independent but Harper-adjacent.
> "Independent, Harper adjacent" — User, this session (Renaer)

### Viewer: only the gazetteer
**Decision:** Gazetteer listed between Locations and Quests; the planning docs are not added. The campaign guides were already in the viewer.
> "not the plans, just the gazetteer" — User, this session

### Volo's written voice
**Decision:** Anything Volo writes follows his own *Volo's Guide to Cormyr*: reader address, self-undercutting parentheses, specific advice, ratings, hearsay marked, and trouble as his source. Elminster footnote rebuttals are optional.
> "I want you to update Volo's voice when something is written by him using the attached document as a guide." — User, this session

### Merge before the consistency pass
> "PR and merge before consistency checkers so I have something to look at" — User, this session (PR 184 merged first, PR 185 after the fix pass)

---

## Rules and Instructions

All earlier rules stay in force. Added or reinforced this session:

- **Page rules for the Setting Compendium** (in the rebuild plan): everything except the Overview is the GM layer; open items go in a deletable `#### Draft Notes` callout (Research, Conflicts, Routed facts) at the bottom, inline `[research]` tags stay; `#### GM Notes` is the default, `#### Secret` only for hidden facts that change play; wards 8 to 10 landmarks and 5 to 6 characters; deity pages have no Appearance but a "Using X as a Deity" box; Villain pages have a Background; Era pages' `~Volo` aside is optional and no dated Timeline when the span is unknown.
- **Drafts may carry full GM information, including in Overviews, until the prose pass** (see decisions above).
- **Volo writes in his written voice** (profile in `character-voices/voices/independents-allies.md`; aside rules in `ember-setting-style` §5).
- **Research before drafting.** `source-researcher` first (it cannot write files, so the main session saves its report to a notes file), then `prose-drafter`. Give researchers the pre-extracted wiki folder.
- **A stopped agent cannot be resumed.** Interrupting a turn (or a rejected tool call) stops all background agents; `SendMessage` then refuses. Relaunch them. A rate-limit stop *can* be resumed with `SendMessage`.
- **Never more than 5 agents at once.** Commit only finished batches; keep an agent's half-edited files out of the commit even if the stop hook asks.
- **Skills are written by the main session** (the voice profile and aside rules this session).
- **Wiki rules:** the wiki ranks fourth, below campaign files, the published adventure and the Alexandrian files. Paraphrase; never copy its prose. Campaign divergences stand (Laeral a moon elf and Khelben's widow, Durnan a Masked Lord, the custody wing numbers, the Guard and Watch kept separate) and the wiki value goes in Draft Notes.
- **Do not spoof headers or user agents** to get past a block (carried from Session 46); the S3 dump is a sanctioned route, not a workaround.
- **Xanathar is "it"; always "Xanathar's Guild"; the current Xanathar is Zushaxx; Kirukesai is a previous one** (the wiki spells it Kirukeskai).
- **Wait to be asked.** No pass starts until the user names it.

---

## Problems Solved

- **Fandom blocked from the container:** a Cloudflare challenge (`cf-mitigated: challenge`), not the network policy → the official S3 dump, indexed into SQLite (`scripts/fandom-dump/`).
- **Rate limit stopped four drafters** (twice, across restarts) → resumed the same agents with `SendMessage`.
- **Interrupted tool call stopped five consistency checkers** → relaunched them (they were read-only, nothing lost).
- **Pact-year provenance:** the Era 5 page said the wiki gave no year and also that it did → settled: the wiki states 1489 but derives it from "three years ago" (WDH 18294).
- **Stale `history.md` content** (Era 5 pact values, soul coins, "Doom Raiders split from Manshoon", "simulacra" for clones, "Lord Protector", "Ship Captains council") → replaced with sourced values; each correction logged in the pages' Draft Notes.
- **~100 "Xanathar Guild" lines, ~75 Xanathar pronoun lines, ~120 "DM" lines** → fixed across the campaign in five folder batches.

---

## Outstanding Work

### New this session: decisions needed from the user
- [ ] **Manshoon's Phase 3 "Simulacrum Insurance"** (`villains/manshoon.md` lines 19, 42, 44; `organizations/09-manshoons-zhentarim.md:19`; Manshoon NF lines 23, 25) still says a simulacrum fights while the real Manshoon escapes. It conflicts with "the man in the towers is a clone of a clone". Keep the simulacrum as the clone's insurance, or redesign the phase?
- [ ] **`arc-e-faction-outposts.md:33`** still has Neverember giving Eyes to "a drow arms dealer" and criminal networks, which conflicts with Eye #1 coming from the Protector's Enclave. Also "eleven years ago" for his removal (should be about three).
- [ ] **Cassalanter villain page** (`villains/cassalanters.md` line 17 "Phase 3 The Sacrificers" reads as if the family sacrifices its children; line 21 "Founders' Day is three sessions away"; line 31 lacks the forfeit date). Victoro NF line 17 lacks the 500,000 gp already held.
- [ ] **Confirm Seffia's mission as an Eye** (Eye #2 from the Brandath Crypt) over the published adventure's "retrieve the Stone"; Arn's spined devil now carries the Eye.
- [ ] **Confirm or swap the invented details:** "within days" for Zelifarn's arrival (`arc-h:19`; Force Grey mission 2 may expect an earlier date); the Q03 strongbox and the reassigned guard in the hideout beat; the Luskan aside's ratings; the `(and to be hungry)` line in Volo's Cassalanter aside; "a patience I have rarely met in his trade" (Davil aside).
- [ ] **Volo confirmations:** the Draft Notes on History 01, 03, 04, 05 ask whether Volo was at Ahghairon's Day, in Luskan, drinking with Davil, and dining twice at the villa; his Notable Figure page (`independents-allies/01`) mentions none of it.
- [ ] **Unruled conflicts (left alone, defaults noted in the checker reports):** Vajra's tenure ("three years" vs wiki 1479 DR); Meloon's devourer timing (three tendays vs three months vs 1491) and "an active member of Force Grey"; Savra's departure (three years vs 1491); alignment differences (Vajra, Savra, Skeemo, Jalester, Kalain); Kalain's alignment/stat block; Jalester's species/background; the Xanathar predecessor count (thirteen vs the wiki's "at least fifteenth"); "third son" for Jarlaxle; Kimmuriel omitted; Cassalanters "about half the gold" vs WDH "most of the coin"; Osvaldo's alignment (neutral evil, formerly lawful good).
- [ ] **Interrogation House ward:** `arc-e:117,:201` say "Trade Ward"; `arc-i:15` and the faction guide say North Ward. `arc-i:259-260` still say "the original Manshoon" (meaning "not the simulacrum").
- [ ] **Ott Steeltoes:** `guides/factions/10-manshoons-zhentarim.md:25,27` (captured, "knows nothing of the Eye") vs `arc-f:9` (Ott receives the Eye and places it in Sylgar's bowl).
- [ ] **Terms:** "Brandath Crypts" (the approach) vs "Mausoleum" (the building): used inconsistently in `waterdeep-lore:20`, `running-the-villains:9,23`, History 06/08, `arc-g:15`, `arc-j:11,85`. Kolat Towers is in the Trades Ward (campaign value); `waterdeep-lore.md:46` still says "Cassalanter sacrifice" for Founders' Day (should be "feast").
- [ ] **Eye #3 route in `arc-h:9,15`:** only the "night before Ches 1" timing was added, not the locket/raid/lift sequence.
- [ ] **Sea Maidens Faire rooms 01 to 04** (`locations/sea-maidens-faire/`) were not checked against "submarine moored all year".
- [ ] **Legacy Event Outcomes format:** `fireball/ev-04:125,129-138` "#### Jarlaxle Informed: True / False" headings; "attunement" wording in `gralhund-villa/ev-02:54` and across trollskull-alley/finding-floon/fireball; `villains/jarlaxle.md:3` still says "flag" for Jarlaxle Informed, BD Contact Severed and Ryvarra Identified. `trollskull-alley/ev-07:72` cites the retired "Ch. 3"; `flowchart.md:69` says "before arc ends"; "Bregan D'Aerthe" (capital A) in Finding Floon and Trollskull Alley.
- [ ] **Small page gaps:** `gm-guide/about-this-campaign.md:70,78` lack "twelve now, weekly"; Lord Cassalanter's letter to Seffia is not in the Windmill finds or Revelation List (ops Outposts); the ops Outposts text does not say the outposts gather gold and ritual components; `arc-g:83` Willifort "eight years" is unsourced.
- [ ] **Missing Notable Figure pages** for people the History pages name: Elminster, Khelben Arunsun, Halaster Blackcloak, Piergeiron, Raurlor, Alethea Brandath, Corylus Thann, Thardouk Starbuckler, Dorgar Adarbrent, Zushaxx, Kirukesai, Fzoul Chembryl, Duhlark and Alcedor Kolat, Yvonnel/Doquaio/Gromph Baenre, Beniago, Kimmuriel Oblodra, Vorondar Levelstone, Faerrel Dunblade, Sevel Dastar, Vaelle Lurval, Nim, Rongquan Mystere. (Ahghairon: none planned.)
- [ ] **Wiki items still open:** ward Lifestyle, Languages and dominant faith (the wiki is blank); Warrior's Way and Street of Silver ward; Midsummer, Twin Parades and Fey Day (absent from the wiki dump); the Code Legal's author and date; Areas of Concern for Asmodeus; warlock/oath rules; whether the Doctrine and Rites tenet on the Cassalanters page can now be filled from the Asmodeus page.

### Passes not started (wait for the user to name one)
- [ ] **Execute the Factions Guide move.** The user decided to move the pages to `setting/faction-operations/`. The Cassalanter pilot is duplicated at `guides/factions/11-cassalanters.md` and `setting/faction-operations/10-cassalanters.md` (kept identical in the shared sections). Moving means retargeting `guides/factions/01-overview.md:47`, `gm-guide/grand-game-in-play.md:103`, `gm-guide/structural-rules.md:26,90,122`, `setting/villains/cassalanters.md:57`, the Asmodeus, Xanathar and Seffia pages' "Factions Guide" cross-references, and CLAUDE.md's Factions Guide table, then deleting the guide pages and rebuilding the viewer.
- [ ] **Pass 2 (Deities)** (wiki now available), **Pass 3 (Gazetteer, Geography, Governance & Guilds, Lore)** (resolve the `waterdeep-lore.md` Castle Ward conflicts: Watch HQ and the Masked Lords' seat, Tymora/Selûne temples, "South Ward" and Kolat Towers' ward, the dragonward's trigger, the 90-foot statues, Barnibus's rank, "1,200 guards", Yellowspire's ward in `SOURCE_GUIDE.md:214`, Mirt's Mansion ward), then Passes 4 to 7 as in the plan.
- [ ] **Pass 1 residue:** `SOURCE_GUIDE.md:325,651` ("basement cell"); `structure/arc-g` lines 19, 83, 531 (from Session 46's list); Xanathar open items: the X12 briefing must not say "one of Three"; whether Nihiloor's domination changes the motive and Manshoon rulings (`arc-f:408`).
- [ ] **Era 5 / Pilot follow-ups:** the Asmodeus Tenets line needs Siamorphe (`organizations/10-cassalanters.md:20`); the faction-operations Cross-References and the org page both say "faction operations page" without a viewer check; add the `Brother Haldric Wence` clerk correction wherever the Order's door-warden is mentioned.

### Carried forward from Session 46 (still open)
- [ ] **Do the Order outcomes need a Campaign Viewer check?** (Session 45) The Pages workflow rebuilds on every merge touching `campaign/**` or `docs/**`; the deploy for PR 185 was not confirmed.
- [ ] **Wire the Order outcomes into unconverted quests** (out-of-scope "Order of the Gauntlet event rewrite (Session 45)" §1): Faction Outposts (Splinter Intel Reported, Pell's Debt Held, a Pell beat, "Trade Ward" at arc-e :117/:201/:301), Xanathar's Lair (Savra outside the entrance), Cassalanter Villa ("if not run" readers, an orientation check for the r10 dossier), Kolat Towers (Ardin, the gate for M6), the Vault (Order Recognized default, the three tithe outcomes, tone-only today), Dungeon of the Mad Mage (Righteous Hand Reached, Undermountain Mandate Accepted).
- [ ] **Confirm the Session 45 readings** (§4): Night 1 raven DC 14; the M4 Location use with no key and no check; the Marcheon 2:1 refusal rule against the guide; r10 dossier dates from 1480 DR; the writ honored in Waterdeep, Neverwinter, Baldur's Gate and Daggerford; M6 Hard triggers.
- [ ] **Verify unchecked rules** (§6): a generic +1 weapon is not in `items.json` (the r25 nine-weapon table), the Howling Hatred ranks, *Spirit Guardians* and *Hallow* wording, *Resurrection* revival rules, the Zone of Truth scroll.
- [ ] **Accept or replace the Session 45 invented names** (§5), including the "Brother" cluster (Haldric, Hallin, Osric, Teodric).
- [ ] **Other-file leftovers** (§3): Fireball! ev-01:194 against arc-c:98; Appendix B:402; "Cult Fanatic" in other pages; arc-j :258; arc-h:39 and arc-i Gondafrey threads; M2/M3/s02/M5 design notes still list the neutral-good fix as open.
- [ ] **Voice residue** (§7): table-heavy Factions Guide `05` and org page `04`; M5 narration at 21.9; no voice profiles for the Order's recurring minor NPCs.

### Carried forward from Session 44 (Lords' Alliance)
- [ ] **Wire the LA outcomes into unconverted quests.** See the out-of-scope notes, "Lords' Alliance event rewrite (Session 44)" §1 (Faction Outposts, Xanathar's Lair, Cassalanter Villa, Kolat Towers, the Vault including the Writ "if not run" default, and Dungeon of the Mad Mage).
- [ ] **Other factions' events that read LA ranks:** BD Three Nights :226 and DR Davil's Arrest :162/:239 test "Renown 3 or higher". They should test **Redknife Reached**, and a suspended or dismissed member should fail.
- [ ] **Emerald Enclave r50 design notes :27** still refers to the old True/False Commission outcome.
- [ ] **Gralhund ev-01:91**: the **Jalester Brief Received: True / False** heading.
- [ ] **Confirm the readings** (out-of-scope §4): Esloon at three characters (end-of-round-2 exit, or a round-1 exit); M2's "goes loud" cost; r25's Read or Ruling audience; r03's Manor Beat and sergeant's note; M6's Strategic Argument DCs.
- [ ] **Accept or replace the Session 44 invented names** (out-of-scope §5), including the "Ha-" cluster.
- [ ] **Leftovers on the companion pages:** the Trollskull ev-04 old banner and milestone formats outside the LA rows; the `08-notable-patrons.md` Faerrel line, which conflicts with the voice rule that no event raises Faerrel; Saeth's other stats; Laeral's species (moon elf on her page, human in WDH; now a logged settled divergence); Jalester's age.
- [ ] **Voicecheck residue to polish:** the Factions Guide `03` has 11% short sentences, mostly in tables. Several LA event files sit at 6–8% short GM sentences against the 5% target.
- [ ] **Voice profiles** for recurring LA minor NPCs (Sevel Dastar, Mareva Coile, Berna, Harko, Rezka), if the user asks.

### Carried forward from Session 43
- [ ] **Wire the Enclave outcomes into unconverted quests.** See the out-of-scope notes, "Emerald Enclave event rewrite (Session 43)" §1: Faction Outposts (Manshoon Named, Splinter Site Reported, Traitor Identified, Imre Identified); Xanathar's Lair (Pier 17 Investigated, as a casing aid at X4); Kolat Towers (Imre Identified); Vault of Dragons (Cultists Escaped, Anchor Destroyed, Illuun Contact, Brandath Crypts Visited, Jeryth's Message Received; an "if not run" default for M6; a notice rule for Jeryth; an outcome for the Stone naming Illuun at Full Awakening).
- [ ] **Structure-doc Enclave lines:** arc-e:85 (ward); arc-f:59/:61 (the X1/X4 dock); arc-g:535 (ley line "beneath Phaulkonmere" is in the wrong ward); arc-j:47/:83/:274; arc-h:128 (the Tarsakh 15 departure shifts Sarna's dates); the Illuun descriptions in arc-c, arc-e and arc-h.
- [ ] **Act I–II Enclave lines:** Trollskull ev-03:20 (the Tally–Melannor link now comes at the First Meeting); the Fireball! and Gralhund Melannor hooks overlap s02 Surge One.
- [ ] **OotG M3 design notes** claim Splinter intel from Kelso that the event doesn't contain.
- [ ] **Notable Figures leftovers:** the Harpers organization page and Bonnie's page say only Mattrim knows her nature; Tally's page :8 lists M1; Durnan's page uses the "Veteran" block; Gerrick Thatchley has no page; `appendix-a-npc-roster.md` is missing.
- [ ] **Confirm the readings** in out-of-scope §5: r10 beast replaced once per campaign; the M4 grell flee rule; the r25 8th-level spell components; the M6 *water breathing* scroll and condition texts.
- [ ] **Accept or replace the Session 43 invented names** (out-of-scope §6).
- [ ] **Voice profiles** for the recurring Enclave minor NPCs (Gerrick, Sarna Dath, Sorrel Hartwick), if the user asks.

### Carried forward from Session 42
- [ ] **Wire the Force Grey outcomes into unconverted quests** (out-of-scope "Force Grey event rewrite (Session 42)" §2): Xanathar's Lair (Pool Destroyed, Placement Records Taken, Captive Freed, Nihiloor Fled, Nihiloor Identified Party); Sea Maidens Faire (Zelifarn Contacted, Zelifarn Befriended, Submarine Reported, Offerings Returned / Kept); Vault of Dragons (Vajra Briefed, Tower Attack Stopped, Splinter Testimony Recorded, Orvyn Ledger Delivered, Vira Caught / Escaped, Buried Thing Reported; gold-path outcome names for r50).
- [ ] **Act I–II Force Grey fixes:** Trollskull ev-04:79, :109-110 (Force Grey Joined flag), :31, :61; ev-05:55, :83 (Meloon Met flag, to become an Event Outcome); ev-06:73; Trollskull design-notes:49; notable-patrons :55, :57, :61; Gralhund ev-01:94.
- [ ] **Structure-doc Force Grey lines:** arc-b :145, :367; arc-e :377; arc-f :39; arc-g :43, :537; arc-i :41; arc-j :41, :51.
- [ ] **BD M3 `ev-01-three-nights.md:287`** devourer brain line.
- [ ] **Harper M5 ev-02** should read **Pool Destroyed**.
- [ ] **Notable Figures leftovers (Force Grey):** Laeral :8; Durnan :12/:26 "rarely says two words"; Orvyn Dall has no page or voice; Vajra, Meloon, Nihiloor and Hlam still use `> **[GM]**`.
- [ ] **Accept or replace the Session 42 invented names.**
- [ ] **Voice profiles for Force Grey minor NPCs**, if asked.

### Carried forward from Session 41 and earlier
- [ ] **Answer the four Session 41 Harper decisions** in the out-of-scope notes. Decision 3 (Enclave M3 vs Harper M3 on Bonnie) is settled by the Bonnie ruling.
- [ ] **Wire the Harper outcomes into unconverted quests.**
- [ ] **Trollskull ev-04:97-98**, the party-level Harpers Joined; also the other True/False Joined headings at ev-04:100-110.
- [ ] **Act I–II Harper lines:** Remallia (Trollskull ev-04:91, Fireball ev-02:96, staff guide :84); Trollskull ev-07:51, ev-04:71; Saeth Cromley (Fireball ev-01:37).
- [ ] **Structure docs (Harper):** arc-e:495, arc-f:31, arc-i:19/247/265, arc-i:75-77, arc-j:43.
- [ ] **Notable Figures (Harper):** Ahmaergo `02:6`, Remallia `02:6`, Variel `06:8`, and Mattrim as "the only person" who knows about Bonnie.
- [ ] **Accept or replace the Session 41 invented names.**
- [ ] **Clarity/voice pass on the remaining factions**; **DR clarity polish** (deferred).
- [ ] **BD items:** M6 harbor naming; r25 dead branch; guide 08:33; the remaining BD decisions; BD outcome readers and writers; BD companion pages; Act I–II BD contradictions; BD and DR invented names (Ilmra, Odalys and Ilsa collide).
- [ ] **Voice profile for J.B. Nevercott.**
- [ ] **OotG M3** wererat silver rule.
- [ ] **SOURCE_GUIDE:219**; arc-j :55/:75/:322; arc-h :9/:71.
- [ ] **Faction Outposts writes:** Yellowspire Ledger/Letters Taken, Clean Exit, Manshoon Named, Yellowspire Raided. 5B must add the relay ledger and coded letters.
- [ ] **Kolat Towers outcomes:** Vevette, the K18 rune, the DR parallel result.
- [ ] **Gralhund:** Floxin Status becomes named outcomes.
- [ ] **Sea Maidens Faire:** read Soluun's fate.
- [ ] **DR outcomes and companion pages:** wire the DR outcomes into arc-e through arc-j; fix guide 07, org page 06, the Notable Figures pages, `structural-rules.md:9` and `player-factions-overview.md:186`; fix the Act I–II DR contradictions; accept or replace the DR invented names; settle Renown 25/50 reachability for all factions; voice profiles for recurring minor DR NPCs; confirm the three viewer changes.
- [ ] **The six decisions** in "Decisions Needed Before Fixing".
- [ ] **One-faction membership wording** on four guide pages.
- [ ] **Voice profiles for minor Harper NPCs.**
- [ ] **Remaining non-rule inconsistencies:** Finding Floon "two nights" (now fixed), Gralhund "two tendays", Vajra, Istrid's loan.
- [ ] **Ember styling on the live site**, and convert the `[GM]` zones in Finding Floon and Trollskull.
- [ ] **Bestiary.** Nihiloor's block is in `force-grey-mechanics-reference.md` §4.
- [ ] **Convert arc-e through arc-j.**
- [ ] **Guides and setting:** prose pass on the guides and setting pages; Notable Figures polish; recheck the M5/M6 summaries on the other organization pages.
- [ ] **Misc carried items:** `sources/backgrounds.json`; BD ev-03 Ryvarra; sidebar titles; Renaer's Confidence holder; Ember organizations JSON; Trollskull Founders' Day; Asmodean Shrine Area 3 (now noted in the ops copies, still unchecked against the source); `#### Milestone: None` in the other factions; DR Viper muscle; earlier invented details.
- [ ] **Older items:** voice-run tooling portability, reproducible global skills, legacy automation references, the Astra/Sol defaults, the Harper private Site.

### Done this session (checked off from the Session 46 list)
- [x] Check the network settings → resolved: not the network policy; Fandom's Cloudflare challenge. Wiki read from the S3 dump.
- [x] Answer the five template decisions; decide Factions Guide move or duplicate (move, not executed).
- [x] Start Pass 1 (History), delete `history.md`.
- [x] Fix the stale files the rulings left behind (Cassalanters and Xanathar lists), apart from the items now listed above.
- [x] Castle Ward Draft Notes and pilot follow-ups (children count, Siamorphe left open).

---

## Warnings and Caveats

- **The wiki dump and index live in the scratchpad and are lost with the container.** Rebuild in about two minutes with `scripts/fandom-dump/README.md` (62 MB download from S3, extract, `build_index.py`). The research and consistency notes are now in `docs/plans/setting-compendium-research-notes/` so they survive.
- **Several pages carry invented or derived values**, tagged in each page's Draft Notes: the 1489 pact year and the 1480/1483 birth years (arithmetic), the Era 8 derived dates, the hideout beat's strongbox, "within days" at `arc-h:19`, the Volo aside details.
- **The Eye #3 route is the main session's reading** of one sentence from the user; the chain is recorded in History 06/08, `running-the-villains`, `jarlaxle.md` and the hideout beat. If the user meant something else, change those together.
- **Pages cross-reference pages that do not exist yet** (Waterdeep, The Open Lord and the Masked Lords, The Dragonward and Walking Statues, The Eyes of the Stone, Ahghairon, Skullport): these are Pass 3 targets or lore pages.
- **Overviews are not player-safe for now** by the user's instruction. The prose pass must write the player-safe versions (the Zardoz Zord rule, the Cassalanter secrecy rule and the spoiler rule apply then).
- **`organizations/07-bregan-daerthe.md:58`** names Jarlaxle in its Overview; deliberately left (see above).
- **Pages deploy:** PR 185 triggered the Pages workflow; whether the viewer deployed and renders the History journal was not confirmed.
- **Researcher reliability:** checker reports can be wrong (one claimed "J.B. Nevercott" was not in WDH; it is at `adventure-wdh.json` line 3601). Re-check a claim before acting on it.

---

## Where to Start Next Session

Read this handoff and CLAUDE.md first. Do not start a pass until the user names it. The first useful thing is to ask the user for rulings on the "Decisions needed" list above, starting with Manshoon's Phase 3, `arc-e:33` and the Seffia mission, because every later pass builds on them. Then, when the user names a pass: the **Factions Guide move** (decided, not executed; retarget the inbound links listed in Outstanding Work first), **Pass 2 (Deities)** (rebuild the wiki index from `scripts/fandom-dump/README.md`, then brief `source-researcher` with the extracted wiki files before any drafter), or **Pass 3 (Gazetteer and the rest)**. For any drafting pass, load `ember-voice`, `adventure-reloaded`, `ember-setting-style`, `ttrpg-sourcebook-style` and `foundry-journal`, copy the shape of the approved pilot pages and `campaign/setting/history/05-a-debt-in-blood.md`, use `docs/plans/setting-compendium-pass1-brief.md` as the drafter brief, and run `voicecheck.py` and the stale-reference grep on every returned page yourself (drafters have no shell). The unresolved checker items are in `docs/plans/setting-compendium-research-notes/consistency-*.md`.
