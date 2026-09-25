# Session 32 Handoff
**Date:** 2026-09-25
**Status:** Ready to continue

---

## What Was Done

**GM Guide prose pass.** All ten GM Guide pages were rewritten:
- *Running the Villains* is now the reference page.
- *The Grand Game in Play* is the between-sessions procedure.
- *About This Campaign* is a separate GM briefing page.
- GM-only material moved into typed sidebars.

**Campaign-wide fixes:**
- **Calendar:** fixed to start on Ches 1.
- **Milestone Points:** reconciled with Ember's L8-at-28 table.
- **Tendays:** in-world weeks became tendays everywhere.
- **Factions split:** factions were divided into mechanics (a new Factions guide, `campaign/guides/factions/01–11`) and lore (`campaign/setting/organizations/`), and the guide got the full style pipeline.

**Faction Events.** The faction-missions folder became Faction Events, with 49 new events:
- 7 First Meetings
- 14 standalone events
- 28 rank-up events

They went through review fixes, the prose polish and a consistency check. Merged to master as PR #6, PR #8 and [friendlysgames/waterdeep#9](https://github.com/friendlysgames/waterdeep/pull/9).

---

## Changes Made

Git range: `git log 2b1be95..bd89372` (82 commits; 244 files, +7,320 / −1,499).

### Files Created
| File | Purpose |
|------|---------|
| `campaign/guides/factions/01-overview.md` … `11-cassalanters.md` | Factions guide. Game mechanics only: stance, hooks, First Meeting summary with a link, renown and ranks, missions; for villain factions, response teams, outposts, escalation and revelation lists |
| `campaign/quests/faction-events/<faction>/00-first-meeting/` (×7) | First Meeting events, moved out of the guide pages. The Bregan D'aerthe one absorbs the TA ev-04 surveillance and Nevercott scene |
| `…/doom-raiders/s01-davils-arrest`, `s02-davils-return` | Arrest two days after Gralhund Villa, including Tashlyn's introduction; release at the end of DR Mission 4 |
| `…/bregan-daerthe/s01-coin-pouches`, `s02-kreb-drops-the-cover`, `s03-dinner-with-zardoz`, `s04-contact-severed` | BD standalone events |
| `…/harpers/s01-the-cell-is-compromised` | Mirt warns the party after Mission 4. Adds a d4 leak rule for non-Mirt Harper channels |
| `…/lords-alliance/s01-suspension-and-dismissal`, `s02-escalation-to-the-open-lord` | LA standalone events |
| `…/force-grey/s01-the-full-picture` | Vajra's +2 renown briefing that brings Laeral in |
| `…/emerald-enclave/s01-a-seat-at-phaulkonmere`, `s02-the-water-table-stirs` | EE standalone events. s02 is a five-surge recurring event |
| `…/order-of-the-gauntlet/s01-the-tithe`, `s02-savras-past` | OotG standalone events. s02 invents Savra's cult history, including rank names |
| `…/<faction>/r03-*`, `r10-*`, `r25-*`, `r50-*` (×7) | 28 rank-up events. Every r50 is marked "Expected in Dungeon of the Mad Mage" |

### Files Modified (major)
| File | What changed |
|------|-------------|
| `campaign/guides/gm-guide/*` (10 files) | Prose pass; GM zones became sidebars |
| `campaign/setting/organizations/01–10` | Lore only. Mechanics moved to the Factions guide |
| `campaign/guides/players-guide/faction-affiliations.md` + GM `player-factions-overview.md` | New Ranks and Benefits section. OotG Righteous Hand and EE Master of the Wild Renown 50 rows reworded. GM-only High Harper sidebar added |
| `campaign/quests/faction-missions/` → `faction-events/` | git mv; every reference renamed |
| `campaign/quests/act-i/trollskull-alley/ev-04-*` | Links to each First Meeting event; flag names and mission titles fixed; BD recruitment section trimmed to a pointer |
| DR m02/m04, GV ev-09, BD m01/m03/m04, EE m04 | Point to the new standalone events. Tashlyn's title corrected; the EE "first time" line fixed |
| Milestone files (TA, Fireball, GV, arc-e..j, `adventure-reloaded` SKILL.md) | Aligned to the Ember ladder |
| `CLAUDE.md` | Updated sections: GM Guide rows, Factions guide table, faction-events row, mechanics-vs-lore rule, About-page exception, Cassalanter secrecy rule, agent concurrency cap |

---

## Key Decisions

### Villain pages split roles
**Decision:** *Running the Villains* is the reference page. *The Grand Game in Play* is the between-sessions procedure.
> "Keep both, split roles" — User

### GM zones in guides are sidebars
**Decision:** The GM Guide uses typed sidebars, never `> **[GM]**` zones.
> "those are a sidebar type" — User

### Campaign starts Ches 1
**Decision:** The calendar runs from PDF 29:
- Ches 1 start
- Ches 20 Grand Opening
- Ches 22 fireball
- Tarsakh 20 Faire departs
- Flamerule 1 feast
- Flamerule 11 twins' ninth birthday

> "Ches 1" — User

### Milestone ladder
**Decision:** Ember's table, L8 at 28.
- Finding Floon 2
- Trollskull Alley 3 (ev-05 is now a milestone)
- Fireball 2
- Gralhund Villa 2
- Faction Outposts 1
- each heist 4
- Vault of Dragons 2

> "Fix the points now" / "Keep Ember's table (28 to L8)" — User

### About This Campaign: separate pages
**Decision:** The GM page is a separate GM briefing, not a superset of the player page.
> "About this campaign should be different for Players and GM." — User

### Tendays
**Decision:** In-world weeks are tendays; real-world "weekly play" stays.
> "'The Weekly Faction Check' Shouldn't it be the tendaily?" — User

### Cassalanters and Bregan D'aerthe can be reasoned with
**Decision:**
- The Grand Game in Play covers the Cassalanter exits: cooperative, contract, sacrifice.
- Bregan D'aerthe has alliance, patron and membership paths. BD Contact Severed makes Jarlaxle a neutral third party.

> "the Cassalanters can be reasoned with, and they can back out from the Game in multiple ways" / "Another faction that can be reasoned with, and even joined." — User

### Factions: mechanics vs lore
**Decision:** Mechanics go in the Factions guide; lore goes on the organization pages. Players may know Bregan D'aerthe is mostly drow.
> "Factions as game mechanics need to be in the guides. Factions as lore in the organisations." / "it's fine for them to know that it's mostly drow" — User

### Faction Events folder
**Decision:**
- `faction-events/<faction>/` holds:
  - `00-first-meeting`
  - `m01–m06`
  - `s0N` standalone events
  - `r03/r10/r25/r50` rank events
- The guide keeps a summary of each First Meeting plus a link.
- Seven player factions only.
- Davil is arrested two days after Gralhund Villa.

> "Rather than a factions missions folder, we'll have a Factions Events folder. It will contain: First meeting, Faction Missions, Any other standalone events (like being informed of Davil's arrest)" — User
> "Emerald Enclave and Flaming Fist also need at least one standalone event … Also, events for ranking up for each faction too. With a big fancy one at max level." — User. "Flaming Fist" means the Order of the Gauntlet.

### Renown 50 is Mad Mage future-proofing; duplicate benefits kept separate
**Decision:**
- Every r50 event is expected during Dungeon of the Mad Mage.
- **Order of the Gauntlet:** the Righteous Hand is now a formal Order investiture, distinct from Mission 6's Halls of Justice recognition.
- **Emerald Enclave:** Master of the Wild grants the *charm of vitality*, confirmed in the 2024 DMG p. 99. It replaces the *charm of heroism*, which Mission 4 already gives.

> "Make these separate, since we shouldn't expect any party members to reach 50 renown by the end of Dragon Heist, this is future proofing for Mad Mage." — User

### Drafts, not final prose
**Decision:** All the new events are structuring drafts. The polish pipeline cleans them up but doesn't replace the later prose-writing pass.
> "are you doing drafts or final proses?" — User. Answered: structuring drafts.

---

## Rules and Instructions

- **Cassalanter secrecy:** "Everybody is suspicious of the Cassalanters because they're too **nice** to be this rich and this purebred. Nobody knows they're infernalists." Use suspicion, never knowledge. Recorded in CLAUDE.md.
- **Agent concurrency cap:** "don't run more than 5 agents at once" (User). Recorded in CLAUDE.md.
- **Factions: mechanics vs lore:** mechanics in `campaign/guides/factions/`, lore in `campaign/setting/organizations/` (CLAUDE.md).
- **Superset exception:** About This Campaign has separate player and GM pages (CLAUDE.md).
- **Sidebar form:** exactly `> [!type]**Title**`, with no `+` and no space; nested inside a GM zone as `> > [!type]**Title**`.
- **Faction event format:**
  - binary `#### Name: True / False` flags
  - no Milestone block
  - player zone of Overview, optional Read Aloud, then Summary
- **In-world time:** tendays, never weeks.
- **Handoff delivery:** push, PR and merge in the same turn, as the last commit.

---

## Problems Solved

- **Agents invented facts:** many were caught in review and removed. Examples:
  - Force Grey: a "25-word" Sending that is 20 words; a Watch-authorization benefit
  - Harpers: Lightsinger's ward; a Fall of Tiamat plot
  - Lords' Alliance: an invented history of lost operatives
  - Order of the Gauntlet: a three-year cult tenure; Nihiloor in Savra's pitch
  - Doom Raiders: Yagra outcomes that don't exist in Finding Floon, now matched to FF ev-01's four branches plus a failed-Persuasion row
  - Emerald Enclave: renown awarded for "reporting", now tied to the Earning Renown criteria
- **Kreb contradiction:** Kreb named Bregan D'aerthe "for the first time", but Nevercott names it at the First Meeting. Now Kreb drops his own cover instead.
- **Coin-pouch contradictions:** the note belongs to the Mission 3 pouch (original M3 text). Kreb's duplicate 100 gp and note were removed; Mission 2 is paid by Nevercott, 80 gp.
- **Flag and title mismatches:**
  - `Lords' Alliance Joined` and `Order of the Gauntlet Joined` fixed in TA ev-04
  - `BD Contact Established` changed to `BD Acknowledged`
  - TA ev-04 mission titles now match the folders (The Long Watch; The Handkerchief and the Girl)
- **Davil's arrest:** it previously appeared in both DR m02 and GV ev-09 and now has one scene. The org page's "several weeks" is now "end of Mission 4". GV ev-09 has Tashlyn's correct title.
- **The Dinner with Zardoz condition:** kept (it doesn't fire if Nar'l was killed), which contradicted m04's "regardless of outcome".
- **Verification:**
  - Converter regression: 464 pages, 0 stray `[!`, 0 unbalanced divs.
  - The viewer build lists all 49 new events.
  - A token check confirmed the polish lost no DCs, numbers, names or links.

---

## Outstanding Work

### Carried forward (Sessions 29–31)
- [ ] Verify the deployed Pages URL works for the user (a stale-cache report)
- [ ] **Bestiary:** never drafted. Pages reference Xanathar two-phase, Victoro and Ammalia, and Aurinax
- [ ] Quest journal conversions, one per structure doc:
  - [ ] Faction Outposts (arc-e)
  - [ ] Xanathar's Lair
  - [ ] Cassalanter Villa
  - [ ] Sea Maidens Faire
  - [ ] Kolat Towers
  - [ ] Vault of Dragons, plus a Scene 6 debrief for when Xanathar is GONE
- [ ] Guides and setting prose-writing pass:
  - [x] Players' Guide (Session 31)
  - [x] GM Guide (this session)
  - [ ] Trollskull Manor Guide
  - [ ] Setting: lore, history, grand-game, villains, organizations, Notable Figures
- [ ] Prose polish of the word-for-word NPC profile text in Notable Figures
- [ ] Mission 5/6 summaries on organization pages: missions now live in the Factions guide, so re-check there
- [ ] `sources/backgrounds.json` doesn't exist, but it's cited for the XPHB/FRHoF background tables. The Heroes of Faerûn background names are unchecked
- [ ] `ev-03` Ryvarra is visible only to parties with drow PCs or who pass the Yawning Portal check. Confirm that's intended now that BD recruitment is party-wide
- [ ] **Older faction-mission sidebars:** normalize to `> [!type]**Title**`. Some lack bold titles, for example `[!abstract]+ If a BD Operative Is Present`
- [ ] **Two GM-draft notes the superset agent flagged in Session 31:**
  - the Renaer's Confidence Holder text frames the secret differently from the player text
  - the GM Holder register doesn't match the polished prose

  Re-check both against the rewritten GM pages.

### New this session
- [ ] **Ember organizations reference:** the user uploaded an Ember organizations JSON ("Here's how Ember writes organisations") for the organizations lore pass. It was ephemeral, so ask the user to re-upload it when that pass starts
- [ ] **Remi Haventree:** the Harpers Renown 1 benefit gives her North Ward safe house, and rank events r10/r50 show her in that role, but her identity is meant to stay hidden until Harpers Mission 4. Decide how the safe house works before M4
- [ ] **The Sleeping Asset** (Harpers m05): the Factions guide and s01 say the Harper double agent is exposed there, but m05 has no such beat. Add it
- [ ] **BD guide `08-bregan-daerthe.md` line ~15:** "At Renown 5+: *Scarlet Marpenoth* extraction" doesn't match any BD rank (3/10/25/50). Decide on 3+ or 10+
- [ ] **BD Mission 6:** the Factions page summary mismatches the mission (limpet charge vs the Eye #3 wreck); the windmill is in the North Ward vs the Southern Ward (Coachlamp Lane)
- [ ] **Trollskull Manor Guide `01-overview.md`:** check its Founders' Day wording against the Structural Rules calendar
- [ ] **Asmodean Shrine:** keyed Area 3 is missing (Cassalanter temple). Also check the Samara and Illuun Notable Figures pages
- [ ] **Existing faction missions (m01–m06)** still carry `#### Milestone: None` blocks. The new events have none. Decide whether to strip them for consistency
- [ ] **Doom Raiders Viper rank:** the rank lists "veteran" muscle, while Yagra's Notable Figures page says Thug (with modifications). Reconcile
- [ ] **Order of the Gauntlet m06:** GM text mentions Lord Victoro's "contract-bound infernal patron". That's GM truth, but check no in-fiction character states it (Cassalanter secrecy)
- [ ] **Invented NPCs and details to accept or replace** (not blocking):
  - Lords' Alliance: Sevel Dastar
  - Force Grey: Aldris Maeven, Rhendar Solne, Merris
  - Bregan D'aerthe: Ilphrin Quiss, Pelsha and Vorn, Sarev Oust
  - Order of the Gauntlet: Tobrin
  - Emerald Enclave: Sarna Dath, Bertio Caskwall
  - Savra's cult history and the Howling Hatred ranks (OotG s02)
  - three near-parallel Mad Mage choices at Renown 50: LA "Undermountain Commission", EE "Illuun Watch", OotG "Undermountain Mandate"

---

## Warnings and Caveats

- **Flag names:** `faction-events` flags are read by structure docs (arc-e..j) that haven't been converted yet. Match flag names exactly during conversion, including `Lords' Alliance Joined`, `Order of the Gauntlet Joined`, `BD Acknowledged`, `BD Contact Severed`, `Davil Arrested`, `Davil Released`, `Tithe Paid` and `Vajra Briefed`.
- **Tenday conversion:** the weeks-to-tendays change was mechanical (108 replacements in faction events and rank tables). Durations shifted: "two weeks" (14 days) became two tendays (20 days). Spot-check any timing that matters.
- **Agents invent details:** the Sonnet agents reliably add details. Keep reviewing every draft against its sources before committing.
- **Stop hook:** it demands a commit whenever the tree is dirty. That produced several "Checkpoint" commits this session. They're harmless, but the log is noisy.

---

## Where to Start Next Session

1. Read this handoff and CLAUDE.md.
2. Wait for the user to name the next task (the "Wait to be asked" rule).
3. The likely candidates are the Outstanding Work items above, or a quest journal conversion (Faction Outposts is first in order).

For any new faction content, the Faction Events layout and format rules are in CLAUDE.md and `adventure-reloaded`. Keep agent work to at most 5 concurrent agents.
