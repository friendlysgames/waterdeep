# Session 39 Handoff
**Date:** 2026-10-01
**Status:** Ready to continue. The Bregan D'aerthe faction events are converted and merged, and so are the Doom Raiders consistency fixes.

---

## What Was Done

This session converted all of the Bregan D'aerthe (BD) faction events from their restored first-commit drafts into finished Ember-voice adventure text, the same way the Doom Raiders were done in Session 38.

The method was:
- restore the files;
- research with five Sonnet 5.5 agents;
- get the plan approved;
- write the brief and the mechanics reference;
- draft each folder with `prose-drafter`;
- run voicecheck and a main-session review;
- run a consistency pass and fix what it found;
- write the out-of-scope log.

**Mid-session changes:**
- The user cut M2b and asked for a new standalone event, s05 The Killer's Fate, where Soluun is expelled. A matching sidebar went into Doom Raiders M1.
- The user ruled that Jarlaxle knows about the Cassalanter pact through his spy Vessa. That ruling now runs through every BD event.
- A Doom Raiders consistency pass, which checks DR events against each other first, found 10 blocking issues. All are fixed.
- The user introduced a new rule: each document gets its own PR and is merged as it lands. PRs #44–#63 were merged under it.

---

## Changes Made

Git range: `git log f71f6c4..HEAD`, where `f71f6c4` is the merge of the Session 38 handoff. It covers 32 non-merge commits.

### Files Modified
| File | What changed |
|------|-------------|
| `campaign/quests/faction-events/bregan-daerthe/**` | The whole folder is restored to its first commits (`45a8a64`) and then rewritten on the DR/Harper page model. Each event has descriptive scenes, members-only briefs and renown, named Event Outcomes, 2024 stat blocks, the **Jarlaxle Unmasked** gate, and source beats from WDH and Appendix B/C. This covers the First Meeting, M1–M6, s01–s04 and r03/r10/r25/r50. |
| `campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/ev-01-the-dockside-killer.md` | Adds a "Bregan D'aerthe Members" GM sidebar. The Soluun outcomes now feed BD s05 (expelled, not back aboard). The disc is a company forgery. |
| `campaign/quests/faction-events/doom-raiders/**` | Applies the Session 39 DR QA fixes. Skeemo's two months, Davil's release on the fifth day, Tashlyn Contact, the Wolf web with no names, the Yellowspire chain, the M3 Wererat roster, quoted speech, readers, "Southern Ward", and Kolat Towers gated in speech. |
| `CLAUDE.md` | Faction-events counts are now 42 missions and 15 standalones. Adds the new **PR and merge per document** rule. The Cassalanter secrecy rule gains the Jarlaxle/Vessa exception. |
| `.claude/skills/character-voices/voices/bregan-daerthe.md` | Vessa now knows about the pact and reports only to the captain (main session edit). |
| `docs/plans/harpers-out-of-scope-notes.md` | Adds new sections: "Bregan D'aerthe event rewrite (Session 39)" and "Doom Raiders consistency pass (Session 39)", plus follow-ups from the Cassalanter ruling. Decision 1 is answered and line 288 is corrected. |

### Files Created
| File | Purpose |
|------|---------|
| `bregan-daerthe/s05-the-killers-fate/` (ev-01, design-notes) | New event in which Soluun is expelled for real, BD members witness it, and the witness rule applies. Sets **Soluun Expelled**. |
| Design notes in BD 00, s01–s04 and r03–r50 | The folders that previously had none. |
| `bregan-daerthe/m04…/ev-02-twelve-minutes.md`, `m05…/ev-02-the-debrief.md`, `m06…/ev-02-before-dawn.md` | Second event pages. |
| `docs/plans/bregan-daerthe-conversion-brief.md` | The approved plan and the user's rulings. |
| `docs/plans/bregan-daerthe-drafter-instructions.md` | The shared hard rules every drafter reads. |
| `docs/plans/bregan-daerthe-mechanics-reference.md` | CR 2.0 rosters checked against the 2024 Monster Manual, the invented limpet charge, and 2024 underwater rules taken from the XPHB/XDMG data. |
| `docs/plans/bregan-daerthe-research/01–08` | The five research reports, the consistency pass, the drafters' out-of-scope notes, and the QA rulings. |
| `docs/plans/doom-raiders-consistency-pass-s39.md`, `doom-raiders-qa-fix-rulings-s39.md` | The DR QA report and its rulings. |

### Files Deleted
| File | Reason |
|------|--------|
| `bregan-daerthe/m02b-the-betrayal-pitch/` | Cut by the user. It duplicated Fireball ev-04's ledger heist and Sea Maidens Faire's Betrayal Pitch. |

---

## Key Decisions

### Restore first, from true first commits
**Decision:** All 30 BD files were restored to their first commits. The history was unshallowed first, and git follow was used across the faction-missions → faction-events rename. Each restored file was blob-verified.
> "return the BD missions to their original commit state" — User, this session

### Jarlaxle ladder: Jarlaxle Unmasked gate
**Decision:**
- Nevercott briefs M1, M2 and M4.
- s03 hands the member over to Zardoz.
- Speakers say "the captain" or "J." until **Jarlaxle Unmasked** is marked.
- The writers of that outcome (Fireball ev-04 and Sea Maidens Faire) are outside the folder and are logged.

### M6 is the limpet charge
**Decision:**
- Xanathar's divers plant a charge on the *Scarlet Marpenoth*.
- It happens after Kolat Towers, at L7, at a reserve berth at Smugglers' Dock after the Faire sails on Tarsakh 20.
- Eye #3 is not the prize.

**Reasoning:** The draft's sunken Eye #3 broke the Eye canon.

### M2 Wazoo is the source's lurid piece
**Decision:** The exposé is about devil worship among unnamed families, with no temple detail. This was later superseded in part by the Cassalanter ruling below: Jarlaxle knows, so the piece is a pressure play, not a fishing expedition.

### M2b cut
**Decision:** The folder is deleted, and the Pitch stays with Sea Maidens Faire. (The user chose "Cut M2b".)

### Soluun is expelled for real, in a new standalone event
**Decision:**
- If Soluun survives DR M1, Jarlaxle expels him. This happens in BD s05 The Killer's Fate.
- A BD member who was at DR M1 hears "You were there." and loses 1 Renown unless they explain themselves. Nothing worse happens.
- An expelled Soluun later sells the *Marpenoth*'s mooring (M6).

The user chose "Expel for real", "New standalone" and "Knows, says little".
> "this is where one of the DR out of scope notes becomes relevant, what to do with the killer?" — User, this session

### DR M1 BD-members sidebar
> "we should also add a sidebar in the DR mission with the killer for 'BD faction members'. Add it as a task for when all BD missions are done" — User, this session

### Jarlaxle knows the Cassalanter pact
**Decision:**
- The spy is Vessa, the BD doppelganger in Cassalanter society.
- No speaker volunteers the pact.
- A member who states it or shows proof gets an admission that never names Vessa, which sets **Cassalanter Pact Shared with BD**. Cassalanter Villa (unconverted) reads it.
- The ruling was applied across the whole BD folder.
> "Jarlaxle knows about the Cassalanters, he has a spy there. He won't tell the members unless they figure it out themselves" — User, this session
> "This needs to be updated throughout the BD faction events" — User, this session

### Standing defaults applied
- Gates are Join/L2, R3/L3, R5/L4, R8/L5, R10/L6 and R13/L7. Base renown is 2/2/3/3/4/4.
- Membership and **BD Contact Severed** are per member.
- Source wins:
  - Ott is a dwarf Cultist Fanatic.
  - The windmill is in the Southern Ward, on Coachlamp Lane.
  - Nar'l's tenure is "a year".
  - Krebbyg and Zardoz follow their voice profiles.
- Soluun uses the Scout stat block everywhere. Krebbyg and Fel'rekt use the WDH Drow Gunslinger.
- Rank loss suspends benefits; the rank is kept.

### DR QA rulings
- Skeemo served for two months.
- Davil is released on the fifth day after the Silencing Skeemo debrief.
- The Wolf web names no teams before the letters.
- Kolat Towers is named in speech only behind **Manshoon Named**.

The full list is in `docs/plans/doom-raiders-qa-fix-rulings-s39.md`.
> "It should be an internal checker as well, between other DR events" — User, this session

---

## Rules and Instructions

All earlier rules stay in force. Added this session:

- **PR and merge per document:** Every reviewed document is pushed, then a PR is opened and merged straight away. Then fast-forward the branch to master. This is now in CLAUDE.md.
  > "new rule, PR and merge as each document is written/edited" — User
- **Cassalanter secrecy exception:** Jarlaxle knows through Vessa and tells no member until they work it out. This is now in CLAUDE.md.
- **Research agents are spawned, not done inline:**
  > "spawning research agents rather than researching yourself" — User
- **Consistency checks include internal cross-event consistency** within a faction, not only cross-faction checks.
- **Rate limits:** Agents stopped on the limit three times. Each was resumed with SendMessage after the reset, as CLAUDE.md requires. Resumed agents don't appear in the user's background-task list.

---

## Problems Solved

- **Shallow clone:** First-commit lookup failed until `git fetch --unshallow`.
- **Mechanics from memory:** The encounter-builder recalled 2014 underwater rules. The main session replaced them with the 2024 XPHB/XDMG text from the 5etools-mirror-3 book data.
  - Piercing weapons are fine underwater.
  - There is no crossbow exception.
  - Potions of water breathing last 24 hours.
  - The breath-holding rule is not in the data, so missions supply *Water Breathing*.
- **2024 creature checks:** Bugbear Warrior, Intellect Devourer (hosts are already dead), Beholder Zombie (four rays, no antimagic cone), Grell and Cultist Fanatic are verified. There is no 2024 Drow, Swashbuckler or Thug.
- **The six-Bugbear Night 1 would wipe a level 4 party:** M3 now uses scaled rosters.
- **The PR merged before the push arrived:** PR #44 merged at an earlier head. The remainder went out as #45.
- **First BD QA pass:** 14 blocking issues fixed. Readers, contacts, M4 timing, stat blocks, the lighter after Tarsakh 20, and others.
- **DR QA:** 10 blocking issues fixed. Skeemo's tenure, Soluun's outcomes, the disc, the M3 roster, Ziraj's damage, Tashlyn Contact, the Wolf names, the Yellowspire chain, the M3 reward timing, and Davil's release date.

---

## Outstanding Work

### New this session
- [ ] **Answer the remaining BD decisions** at the end of the BD section of `docs/plans/harpers-out-of-scope-notes.md`:
  - the Zord cover's origin;
  - whether Fireball ev-04 sets **Jarlaxle Unmasked**;
  - per-member wording in guide 08;
  - where Renown 25 and 50 come from for every faction.
- [ ] **Write the outside readers and writers** for the new BD outcomes when each quest is converted:
  - **Jarlaxle Unmasked:** Fireball ev-04 and Sea Maidens Faire.
  - **Faction Outposts:** **Windmill Raided**, **Windmill Map Taken**, **Windmill Clean Exit**, **Seven Masks Raided**, **Ott Kept/Lost**.
  - **Sea Maidens Faire:** the Soluun outcomes, **BD Watchers Sold**, **BD Contact Severed**, and the fates of Krebbyg and Fel'rekt.
  - **Cassalanter Villa:** **Florette Reported**, **Cassalanter Pact Shared with BD**, the Wazoo outcomes, **Esvele Hostile** (DR M2).
  - **Xanathar's Lair:** the Nar'l outcomes, **Nar'l Bypass Learned**.
  - **Vault of Dragons:** **Marpenoth Saved/Crippled/Lost**, **Guild Survivor Escaped**, **Brandath Lead from Brimel**, BD Commander's proposal.
  - **OotG M2:** **Black Viper Source Noted**.
- [ ] **Fix the BD companion pages** once the user widens scope:
  - guide 08 (exposé wording, Renown 5 extraction, "Dread Lord", "the party" wording);
  - org page 07;
  - `villains/jarlaxle.md:51` (name Vessa);
  - the Notable Figures pages: stat names, Featured-in lists that still name The Betrayal Pitch, Soluun's cover story, Nar'l's tenure, Ott's "Cult Fanatic".
- [ ] **Act I–II contradictions logged for BD:** Trollskull ev-03, ev-04 and ev-07; Fireball ev-01 and ev-04; Gralhund ev-01 and ev-09 (including Istrid fleeing, which conflicts with DR).
- [ ] **Accept or replace the invented names.** The BD list is in the out-of-scope log. Three first names collide between DR and BD: Ilmra, Odalys, Ilsa.
- [ ] **Voice profile for J.B. Nevercott:** none exists. Skills are written by the main session, so this needs a user request.
- [ ] **Reconcile the OotG M3 wererat silver rule** with the 2024 Wererat.

### Carried forward from Session 38
- [ ] Faction Outposts must write Yellowspire Ledger Taken, Yellowspire Letters Taken and Yellowspire Clean Exit. 5B must add the relay ledger and coded letters.
- [ ] Kolat Towers must name Vevette's fate, the K18 rune and the Doom Raiders parallel-operation result as outcomes.
- [ ] Gralhund Villa's Floxin Status flag must become named Event Outcomes.
- [ ] ~~Settle Soluun's fate with Jarlaxle~~ Done in BD s05. Sea Maidens Faire still needs to read it.
- [ ] Faction Outposts must write **Manshoon Named** and **Yellowspire Raided**.
- [ ] Wire the Doom Raiders outcomes into their readers, arc-e through arc-j (see the Session 38 list).
- [ ] Fix the Doom Raiders companion pages: guide 07, org page 06, the Notable Figures pages, `structural-rules.md:9`, `player-factions-overview.md:186`.
- [ ] Act I–II Doom Raiders contradictions: Finding Floon ev-01:115, Trollskull ev-04, Fireball ev-01:204, Gralhund ev-01 and ev-09.
- [ ] Accept or replace the DR invented names.
- [ ] Renown 25 and 50 reachability for all factions.
- [ ] Voice profiles for recurring minor DR NPCs.
- [ ] Confirm the three viewer changes on the live site.

### Carried forward from Session 37 and earlier
- [ ] Answer the six decisions in `docs/plans/harpers-out-of-scope-notes.md`. Decision 1 is now answered for Jarlaxle and BD.
- [ ] One-faction membership wording on four guide pages.
- [ ] Wire the Harper outcomes into their readers; give minor Harper NPCs voice profiles.
- [ ] Remaining non-rule inconsistencies: Finding Floon "two nights", Gralhund "two tendays", Vajra, Istrid's loan, coin-pouch timing (now settled inside BD).
- [ ] Confirm the Ember styling on the live site. Use the Artifact files map if the viewer is republished. Convert the old `[GM]` zones in Finding Floon and Trollskull.
- [ ] Bestiary; convert arc-e through arc-j; prose pass on the guides and setting pages; polish the Notable Figures profiles; recheck the Mission 5/6 summaries on the organization pages.
- [ ] `sources/backgrounds.json`; BD `ev-03` Ryvarra visibility; normalize sidebar titles in other factions; Renaer's Confidence holder framing.
- [ ] Ember organizations JSON; BD guide Renown 5+ extraction; Trollskull Founders' Day wording; Asmodean Shrine Area 3; `#### Milestone: None` in other factions' events; Doom Raiders Viper muscle on Yagra's Notable Figures page; earlier invented details.
- [ ] Remaining faction rewrites: Lords' Alliance, Emerald Enclave, Order of the Gauntlet, Force Grey. Use the Session 38/39 method: restore, research agents, plan, brief, mechanics reference, drafters, QA, PR per document.
- [ ] Older items: voice-run tooling portability, reproducible global skills, legacy automation references, the Astra/Sol defaults, Harper private Site.

---

## Warnings and Caveats

- **Nothing outside BD and DR reads the new outcomes yet.** Until arc-e through arc-j are converted, a GM has to carry them by hand. That includes **Jarlaxle Unmasked**, which nothing writes.
- **The limpet-charge mechanic is invented.** The Dawn Clock and the detonation damage are flagged as invented in the mechanics reference.
- **2024 stat data is not in the repo.** The XMM, XPHB and XDMG files were downloaded to the session scratchpad. Re-download them from `5etools-mirror-3/5etools-src` if needed.
- **voicecheck false positives remain:** Zardoz's toast in BD s03 is flagged as "not-X-but-Y", and "Keep it, quietly" in DR r50 is a path name.
- **Faire timing:** BD M5 assumes the Faire is still in harbor at 6th level. The design notes flag this.
- **Coach-grab outcomes:** DR M2's coach-grab marks both **Delivery Refused** and **Esvele Hostile**.

---

## Where to Start Next Session

Read this handoff and CLAUDE.md, then the end of `docs/plans/harpers-out-of-scope-notes.md`. It holds the BD and DR Session 39 sections and the open decisions. Wait for the user to name the next task. A further faction rewrite (Lords' Alliance, Emerald Enclave, Order of the Gauntlet or Force Grey) would follow the Session 39 method: restore from true first commits, spawn research agents, plan, brief, mechanics reference against 2024 data, drafters (5 at a time), voicecheck, consistency pass (internal first), out-of-scope log. Each document gets its own PR and is merged as it lands.
