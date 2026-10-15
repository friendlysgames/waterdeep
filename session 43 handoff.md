# Session 43 Handoff
**Date:** 2026-10-15
**Status:** Ready to continue

---

## What Was Done

The Emerald Enclave faction events were rewritten from scratch with the Session 41/42 method, and all ten steps are done.

**Rewrite.**
- All 21 Enclave files were restored to their first commits.
- Five research agents read whole DR/BD/Force Grey/Harper model events.
- The plan, brief, drafter instructions, mechanics reference and consistency rulings went into `docs/plans/`.
- prose-drafter agents redrafted all 13 folders in three waves, with voicecheck and rhythm passes.

**Consistency and companion pages.**
- A consistency-checker pass produced rulings A1–A28. They were fixed folder by folder.
- The companion pages were then aligned: the Factions Guide, the organization page, four Notable Figures pages, the rank rows, Trollskull, and the Bonnie branches in Harper and Force Grey.
- Outside contradictions were logged.

**Merges.** Every document was PR'd and merged on its own (#106–#132). Two user corrections came at the end: the tavern fee floor and the Enclave's infernal sensing.

---

## Changes Made

Git range: `5382433..HEAD`.

### Files Modified
| File | What changed |
|------|-------------|
| `campaign/quests/faction-events/emerald-enclave/*/` (13 folders) | Full rewrite on the DR/FG model. Ember blocks, Event Outcomes, base renown plus three +1s, the shared gate ladder, per-member rank procedures, counted *Animal Messenger* messages, secrecy gates, and a design-notes page per folder. |
| `m02-…/ev-02-the-final-dawn.md`, `m04-…/ev-01-the-search.md` + `ev-02-the-nest.md`, `m06-…/ev-01-the-descent.md` + `ev-02-the-anchor.md` | New split events. They replace `ev-02-brandath-crypt-revelation.md`, `m04 ev-01-the-grells-in-the-dock-ward.md` and `m06 ev-01-the-dreamers-reach.md`, which are deleted. |
| `campaign/guides/factions/04-emerald-enclave.md` | The gates, renown, rank rows, mission summaries, Southern Ward, Manshoon gate, an infernal-but-unattributed Cassalanter hook and the M6 Vault default. The Jeryth's Manner sidebar and the herb-sprig hook are removed. |
| `campaign/setting/organizations/03-emerald-enclave.md` | `[!gamemaster]` format, Southern Ward, *Animal Messenger*, and a What Is Actually True block covering Illuun, Manshoon, the infernal sensing and Jarlaxle. |
| `notable-figures/emerald-enclave/01-melannor-fellbranch.md`, `02-jeryth-phaulkon.md` | `[!gamemaster]`, voice rules, current event titles, and the Illuun name gate. |
| `notable-figures/independents-allies/17-sir-ambrose-everdawn.md` | Knight block, Ten Nights listed as M2, no volunteered crypt knowledge. |
| `notable-figures/independents-adversaries/03-kelso-fiddlewick.md` | Field Ward, Wererat block, a middleman buyer with the Splinter customer in GM text only. |
| `guides/players-guide/faction-affiliations.md`, `guides/gm-guide/player-factions-overview.md` | The Enclave rank rows (superset rule) and the Enclave row in Running the Player Factions. |
| `quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md` | The Enclave renovation row (druid craft plus timber, −250 gp, oak ask). The Emerald Enclave Joined heading is no longer True/False. |
| `guides/trollskull-manor/02-operating-costs.md` | The renovation bullet matches the First Meeting. The ward-fee cut was removed, then restored on the user's ruling. |
| `harpers/m03-the-doppelganger-auditions/overview.md` + `design-notes.md`, `force-grey/m03-…/ev-01-the-tenday-watch.md`, `force-grey/m04-…/ev-02-nihiloors-wing.md` | **Bonnie Departed** branches. |
| `.claude/skills/character-voices/voices/independents-allies.md` | Ambrose is a "knight of Kelemvor", not a paladin. |
| `CLAUDE.md` | The Cassalanter secrecy rule gains the Enclave infernal-sensing exception. |
| `docs/plans/harpers-out-of-scope-notes.md` | New section, "Emerald Enclave event rewrite (Session 43)". |

### Files Created
| File | Purpose |
|------|---------|
| `docs/plans/emerald-enclave-plan.md` | The approved plan, with research findings. |
| `docs/plans/emerald-enclave-conversion-brief.md` | Binding: user decisions, defaults, renames, outcome table, per-folder briefs. |
| `docs/plans/emerald-enclave-drafter-instructions.md` | Drafter rules with numeric voice ranges and the wave-1 lessons. |
| `docs/plans/emerald-enclave-mechanics-reference.md` | CR 2.0 rosters, allies, charms, Jeryth's spell lists, the r03 network, the r10 routes, the anchor, the Ward ring. |
| `docs/plans/emerald-enclave-consistency-rulings.md` | Rulings A1–A28 and the dispatch table. |
| `docs/plans/emerald-enclave-research/00`–`05` | The research brief and the five research reports. |

---

## Key Decisions

### Bonnie and the doppelganger crew
**Decision:** The Enclave makes the crew leave Waterdeep, Bonnie included. If **Bonnie Harper Operative** is marked, the party can win her a reprieve (DC 15 Charisma (Persuasion)). **Doppelgangers Departed** and **Bonnie Departed** are separate outcomes, with a two-tenday grace period. Harper M3 is unavailable once **Bonnie Departed** is marked.
> "Bonnie is made to leave, unless she has been made a Harper, in which case the party can convince the Enclave that she's not a threat" — User, this session

### M6 level
**Decision:** The Dreamer's Reach is Renown 13, 7th level, after Kolat Towers and The Fouled Channel. Three-heist parties play it after the Vault.
> "L7 post-Kolat (FG precedent)" — User, this session

### Kelso's role
**Decision:** Kelso is a middleman who bought Edric's names. The Splinter appears as his customer in GM text only.
> "Kelso, a middleman (Recommended)" — User, this session

### Trollskull renovation help
**Decision:** The 250 gp of help is druid craft (*Mold Earth*, *Shape Water*, *Plant Growth*, *Stone Shape*) plus donated timber laid by Tally, given once, with the oak ask. *Fabricate* is gone.
> "Druid craft + timber (Recommended)" — User, this session

### Ward-fee cut stays
**Decision:** The Enclave's Watchful Order ward-fee cut stays in `02-operating-costs.md` with the 5 gp floor, as a passive standing benefit with no event.
> "don't drop it, it's just a passive thing, it doesn't need an event" — User, this session

### The Enclave senses infernal influence
**Decision:** The Enclave can sense infernal influence in the Sea Ward, but nobody in it knows whose it is. This is recorded in CLAUDE.md.
> "The Enclave can know that there's infernal influence in the city, they just don't know who" — User, this session

### Defaults accepted from the plan (the user did not overrule them)
- Phaulkonmere is in the Southern Ward, one block south of Kolat Towers.
- There are no intellect devourers in the Enclave set; M5's waste is Splinter thrall-conditioning residue.
- Renames: Gerrick Goodbarrel → Thatchley, Raeve Solnath → Imre Daskov, Wenna Droit → Hesta Droit, Tobiah Fenn → Tobiah Ashby.
- Illuun's name reaches a member only through **Anchor Destroyed** or the Stone. **Illuun Contact** gives the presence only (ruling A8).
- Rank benefits are per member. *Revivify* and *Reincarnate* are not on Jeryth's lists. r10 and r25 share one casting per quest. City sewers count as "surface". Melannor stays Neutral Good.

---

## Rules and Instructions

All earlier rules stay in force. Added or reinforced this session:

- **PR and merge per document, again after each edit.** *(User: "remember the rule, pr and merge as each doc is drafted, then after each edit")*
- **Cassalanter secrecy exception for the Enclave.** It may sense infernal influence but never knows whose it is (CLAUDE.md).
- **Passive faction benefits need no delivering event.** Don't strip a guide perk just because no event hands it over. *(User: "it's just a passive thing, it doesn't need an event")*
- **Drafters still need numeric rhythm passes.** Rhythm passes that lengthened speech pushed GM sentences past 28 words, so send exact split lists for the second pass.
- **Agents with no shell can't `git rm`.** The main session removes obsolete split files.

---

## Problems Solved

- **The restored drafts used the retired formats** (`[GM]`, True/False flags, Arc labels). All are replaced with the Ember blocks and Event Outcomes.
- **Unreachable gates.** M4 and M5 named Faction Outposts (L4) as their reader, which can never happen. Their readers were retargeted: **Pier 17 Investigated** to Xanathar's Lair, **Imre Identified** to Kolat Towers, **Cultists Escaped** to the Vault.
- **Rules errors fixed:**
  - *Animal Messenger* messages ran 39–70 words; all are now 25 words or fewer, counted.
  - The Giant Eagle is a Celestial.
  - "Dazed", *Fabricate* and Ambrose as a "Paladin" are gone.
  - The charm texts now follow the 2024 DMG.
- **Ungated "Manshoon Splinter" lines** (13 of them) were removed.
- **Cross-folder contradictions** were fixed through rulings A1–A28:
  - the M5/M6 cistern geometry;
  - the r50 hold;
  - travel times;
  - name collisions;
  - the grell count;
  - stale design-note entries.
- **Collision with Lords' Alliance.** **Undermountain Commission Accepted** is replaced by **Illuun Watch Accepted**.

---

## Outstanding Work

### New this session
- [ ] **Wire the Enclave outcomes into unconverted quests.** See the out-of-scope notes, "Emerald Enclave event rewrite (Session 43)" §1:
  - Faction Outposts: Manshoon Named, Splinter Site Reported, Traitor Identified, Imre Identified.
  - Xanathar's Lair: Pier 17 Investigated, as a casing aid at X4.
  - Kolat Towers: Imre Identified.
  - Vault of Dragons: Cultists Escaped, Anchor Destroyed, Illuun Contact, Brandath Crypts Visited, Jeryth's Message Received. It also needs an "if not run" default for M6 and a notice rule for Jeryth.
  - The Vault also needs an outcome for the Stone naming Illuun at Full Awakening.
- [ ] **Structure-doc Enclave lines:**
  - arc-e:85 (ward);
  - arc-f:59/:61 (the X1/X4 dock);
  - arc-g:535 (ley line "beneath Phaulkonmere" is in the wrong ward);
  - arc-j:47/:83/:274;
  - arc-h:128 (the Tarsakh 15 departure shifts Sarna's dates);
  - the Illuun descriptions in arc-c, arc-e and arc-h.
- [ ] **Act I–II Enclave lines:**
  - Trollskull ev-03:20, where the Tally–Melannor link now comes at the First Meeting;
  - the Fireball! and Gralhund Melannor hooks overlap s02 Surge One.
- [ ] **Lords' Alliance r50 :156** still uses Undermountain Commission Accepted and the retired blocks.
- [ ] **OotG M3 design notes** claim Splinter intel from Kelso that the event doesn't contain.
- [ ] **Notable Figures leftovers:**
  - the Harpers organization page and Bonnie's page say only Mattrim knows her nature;
  - Tally's page :8 lists M1;
  - Durnan's page uses the "Veteran" block;
  - Gerrick Thatchley has no page;
  - `appendix-a-npc-roster.md` is missing.
- [ ] **Confirm the readings** in out-of-scope §5:
  - r10 beast replaced once per campaign;
  - the M4 grell flee rule;
  - the r25 8th-level spell components;
  - the M6 *water breathing* scroll and condition texts.
- [ ] **Accept or replace the Session 43 invented names** (out-of-scope §6).
- [ ] **Voice profiles** for the recurring Enclave minor NPCs (Gerrick, Sarna Dath, Sorrel Hartwick), if the user asks.

### Carried forward from Session 42
- [ ] **Wire the Force Grey outcomes into unconverted quests** (out-of-scope "Force Grey event rewrite (Session 42)" §2):
  - Xanathar's Lair: Pool Destroyed, Placement Records Taken, Captive Freed, Nihiloor Fled, Nihiloor Identified Party.
  - Sea Maidens Faire: Zelifarn Contacted, Zelifarn Befriended, Submarine Reported, Offerings Returned / Kept.
  - Vault of Dragons: Vajra Briefed, Tower Attack Stopped, Splinter Testimony Recorded, Orvyn Ledger Delivered, Vira Caught / Escaped, Buried Thing Reported. It also needs gold-path outcome names for r50.
- [ ] **Act I–II Force Grey fixes:**
  - Trollskull ev-04:79, :109-110 (Force Grey Joined flag), :31, :61;
  - ev-05:55, :83 (Meloon Met flag, to become an Event Outcome);
  - ev-06:73;
  - Trollskull design-notes:49;
  - notable-patrons :55, :57, :61;
  - Gralhund ev-01:94.
- [ ] **Structure-doc Force Grey lines:** arc-b :145, :367; arc-e :377; arc-f :39; arc-g :43, :537; arc-i :41; arc-j :41, :51.
- [ ] **BD M3 `ev-01-three-nights.md:287`** devourer brain line.
- [ ] **Harper M5 ev-02** should read **Pool Destroyed**.
- [ ] **Notable Figures leftovers (Force Grey):**
  - Laeral :8;
  - Durnan :12/:26 "rarely says two words";
  - Orvyn Dall has no page or voice;
  - Vajra, Meloon, Nihiloor and Hlam still use `> **[GM]**`.
- [ ] **Accept or replace the Session 42 invented names.**
- [ ] **Voice profiles for Force Grey minor NPCs**, if asked.

### Carried forward from Session 41 and earlier
- [ ] **Answer the four Session 41 Harper decisions** in the out-of-scope notes. Decision 3, Enclave M3 vs Harper M3 on Bonnie, is now settled by this session's Bonnie ruling.
- [ ] **Wire the Harper outcomes into unconverted quests.**
- [ ] **Trollskull ev-04:97-98**, the party-level Harpers Joined; also the other True/False Joined headings at ev-04:100-110.
- [ ] **Act I–II Harper lines:** Remallia (Trollskull ev-04:91, Fireball ev-02:96, staff guide :84); Trollskull ev-07:51, ev-04:71; Saeth Cromley (Fireball ev-01:37).
- [ ] **Structure docs (Harper):** arc-e:495, arc-f:31, arc-i:19/247/265, arc-i:75-77, arc-j:43.
- [ ] **Notable Figures (Harper):** Ahmaergo `02:6`, Remallia `02:6`, Variel `06:8`, and Mattrim as "the only person" who knows about Bonnie.
- [ ] **Accept or replace the Session 41 invented names.**
- [ ] **Clarity/voice pass on the remaining factions**; **DR clarity polish** (deferred).
- [ ] **BD items:**
  - M6 harbor naming;
  - r25 dead branch;
  - guide 08:33;
  - the remaining BD decisions;
  - BD outcome readers and writers;
  - BD companion pages;
  - Act I–II BD contradictions;
  - BD and DR invented names (Ilmra, Odalys and Ilsa collide).
- [ ] **Voice profile for J.B. Nevercott.**
- [ ] **OotG M3** wererat silver rule.
- [ ] **SOURCE_GUIDE:219**; arc-j :55/:75/:322; arc-h :9/:71.
- [ ] **Faction Outposts writes:** Yellowspire Ledger/Letters Taken, Clean Exit, Manshoon Named, Yellowspire Raided. 5B must add the relay ledger and coded letters.
- [ ] **Kolat Towers outcomes:** Vevette, the K18 rune, the DR parallel result.
- [ ] **Gralhund:** Floxin Status becomes named outcomes.
- [ ] **Sea Maidens Faire:** read Soluun's fate.
- [ ] **DR outcomes and companion pages:**
  - wire the DR outcomes into arc-e through arc-j;
  - fix guide 07, org page 06, the Notable Figures pages, `structural-rules.md:9` and `player-factions-overview.md:186`;
  - fix the Act I–II DR contradictions;
  - accept or replace the DR invented names;
  - settle Renown 25/50 reachability for all factions;
  - voice profiles for recurring minor DR NPCs;
  - confirm the three viewer changes.
- [ ] **The six decisions** in "Decisions Needed Before Fixing".
- [ ] **One-faction membership wording** on four guide pages.
- [ ] **Voice profiles for minor Harper NPCs.**
- [ ] **Remaining non-rule inconsistencies:** Finding Floon "two nights", Gralhund "two tendays", Vajra, Istrid's loan.
- [ ] **Ember styling on the live site**, and convert the `[GM]` zones in Finding Floon and Trollskull.
- [ ] **Bestiary.** Nihiloor's block is in `force-grey-mechanics-reference.md` §4.
- [ ] **Convert arc-e through arc-j.**
- [ ] **Guides and setting:** prose pass on the guides and setting pages; Notable Figures polish; recheck the M5/M6 summaries on the other organization pages.
- [ ] **Misc carried items:**
  - `sources/backgrounds.json`;
  - BD ev-03 Ryvarra;
  - sidebar titles;
  - Renaer's Confidence holder;
  - Ember organizations JSON;
  - Trollskull Founders' Day;
  - Asmodean Shrine Area 3;
  - `#### Milestone: None` in the other factions;
  - DR Viper muscle;
  - earlier invented details.
- [ ] **Remaining faction rewrites: Lords' Alliance and Order of the Gauntlet**, using the Session 41/42/43 method.
- [ ] **Older items:** voice-run tooling portability, reproducible global skills, legacy automation references, the Astra/Sol defaults, the Harper private Site.

---

## Warnings and Caveats

- **The previous Enclave version is in git at `bc7655e`.** The scratchpad copy (`ee-prev/`) dies with this container. Use `git show bc7655e:<path>`.
- **Accepted voicecheck residue:**
  - the Factions Guide `04` and the organization page are table-heavy, with 6–12% short sentences and several 30–34-word table cells;
  - the Notable Figures "Featured in" lines run long by design;
  - Jeryth's page keeps two template-driven "profound abstraction" flags (the Resonance and Relationships fields).
- **The Factions Guide `04` Earning Renown bullets** keep the faction-level +1/+2 awards that the other faction guides also use. They are separate from the mission +1s.
- **The Xanathar's Lair hook in guide `04`** was written by the drafter (aberrant-creature accounts plus the Pier 17 casing aid). Confirm it when Xanathar's Lair is converted.
- **Jeryth's notice rule at the Vault is undefined.** r10 and r25 set three and seven days, and M6 has her say she no longer needs notice. The Vault conversion must pick one.
- **The `longsent.py` checker is scratchpad-only** and is lost with the container. It flags false positives at closing-quote boundaries.

---

## Where to Start Next Session

Read this handoff and CLAUDE.md. If the user names the Lords' Alliance or Order of the Gauntlet rewrite, follow the Session 41/42/43 method in the Session 42 Rules and Instructions. Use `docs/plans/emerald-enclave-*` as the newest template for the plan, brief, drafter instructions, mechanics reference and rulings, and use the 5etools-mirror-3 data for every rules check. For further Enclave work, read `docs/plans/emerald-enclave-conversion-brief.md` and the "Emerald Enclave event rewrite (Session 43)" section of `docs/plans/harpers-out-of-scope-notes.md` first. Otherwise wait for the user to name the next task.
