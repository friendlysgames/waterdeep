# Session 40 Handoff
**Date:** 2026-10-07
**Status:** Ready to continue

---

## What Was Done

The user read the converted Bregan D'aerthe events and found them "very flowy and elaborate to the point of being complicated and hard to understand". The cause was twofold:
- `ember-voice` set sentence-length floors and demanded "flowing/generous" prose with no ceiling.
- `prose-polisher` had been invoked without its `file:` / `mode: apply` parameters, so it skipped its pipeline.

The main session split the Ember voice by text type (readaloud, GM text, speech) in the voice skills, the polisher agent, the drafter instructions and CLAUDE.md. All 18 BD folders were then re-polished with the full pipeline. Each folder was checked against HEAD for lost DCs, names and headings, run through `voicecheck.py`, and given its own PR and merge. The in-folder contradictions the polishers surfaced were fixed, and the out-of-folder ones were logged. Doom Raiders was deliberately not re-polished.

---

## Changes Made

Git range: `3cc9da7..HEAD` (Session 39 handoff to the out-of-scope log update). PRs #65–#84, all merged to master.

### Files Modified
| File | What changed |
|------|-------------|
| `.claude/skills/ember-voice/SKILL.md` | New section 2a, "By Text Type". Floors become ranges: readaloud 17–21 (≤20% at 30+ words), GM text 15–20 (≤15% at 30+), speech 11–15. Rule 2 now reads "read easily, never chain more than two clauses", rule 8 "one fact per sentence, bullets for procedures", and rule 10 "Say it once" (was "Be generous"). Adds a clarity-first note quoting the user. |
| `.claude/skills/humanize-prose/SKILL.md`, `.claude/skills/character-voices/SKILL.md` | Aligned with 2a; "flowing/generous" removed. |
| `.claude/agents/prose-polisher.md` | Stage 4 rhythm uses the 2a ranges and adds "never leave prose elaborate". |
| `CLAUDE.md` | The Ember voice rule is rewritten by text type, quoting the user. |
| `docs/plans/bregan-daerthe-drafter-instructions.md` | The voice line now uses the 2a ranges. |
| `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/` | Clarity re-polish. Fixed the "Whom They Follow" bullets that had fallen outside their block. |
| `.../m01-*/`, `.../m02-*/`, `.../m03-*/` | Clarity re-polish. |
| `.../m04-the-compromised-eye/` | Re-polish plus a second speech pass (ev-01 speech went from 17.8 to 12.0 words a sentence). |
| `.../m05-the-theaters-back-room/` | Re-polish plus a second speech pass. Fixes: the Lifted Stub Advantage window ("from twenty past eight"), the "captain's in the box" line gated on **Zardoz Introduced**, the overview's lobby time, and a stray Who Knows What paragraph returned to its block. |
| `.../m06-the-dive/` | Re-polish. Fixes: Taking Nell said "three ways" but listed four, and Nell's leftover paper bird is now her lantern. |
| `.../s01-*/`, `.../s02-kreb-drops-the-cover/`, `.../s04-contact-severed/` | Re-polish. s02 also cuts a tea flourish that contradicted the scene. |
| `.../s03-dinner-with-zardoz/` | Re-polish. Fixes: the Insight check now says "last two sentences", and the design notes' **Nar'l Eliminated** dinner now matches the event. |
| `.../s05-the-killers-fate/` | Re-polish. Soluun's disc answer now matches the GM text: the company struck the forgery. |
| `.../r03-soldier/`, `.../r10-officer/` | Re-polish. r10 also has one not-X-but-Y line rewritten. |
| `.../r25-commander/` | Re-polish plus a second pass on readaloud and speech. Fixes: Pelsha is white-haired throughout, the Seat answer is fixed, and a stale design-notes claim is removed. |
| `.../r50-houseless-noble/` | Re-polish. Fixes: the Lolth "prayer" line is cut (contempt rule), and the first-page / second-page mismatch on the Menzoberranzan leaf is resolved. |
| `docs/plans/harpers-out-of-scope-notes.md` | New "Bregan D'aerthe clarity pass (Session 39)" section. Marks `player-factions-overview.md:182` resolved, corrects the M5 ward claim, and adds the guide 08:33 Laeral recipient. |

### Files Created
| File | Purpose |
|------|---------|
| `docs/plans/bregan-daerthe-clarity-pass.md` | The clarity brief and its addendum: cut 15–25%, use plain words, say it once. |
| `session 40 handoff.md` | This file. |

---

## Key Decisions

### Split the Ember voice by text type
**Decision:** Each text type has its own target, given as a range rather than a floor:
- **Readaloud:** trimmed flow, 17–21 words a sentence.
- **GM text:** plain and procedural, 15–20 words, one instruction per sentence, bullets for procedures.
- **Speech:** follows the character, 11–15 words, each point made once.

Theatrics belong to the characters, never to the narration.

**Reasoning:** The "flowing/generous" rule and the minimum lengths produced elaborate text that was hard to run.
> "Reading everything in BD, it feels like a lot of it, including narrative, dialogue and even standard GM text, is very flowy and elaborate to the point of being complicated and hard to understand." — User
> "DR reads better, I think it's the fact that members of DR lack BD's theatrics. Go ahead with BD for now." — User
> "The agents aren't reading the right skills, I don't think" — User. Chose "Split by text type (Recommended)".

### BD only; DR is not re-polished
**Decision:** The clarity pass covered BD only. Doom Raiders stays as it is until the user asks.
> "Go ahead with BD for now." — User

---

## Rules and Instructions

All earlier rules stay in force. Added or reinforced this session:

- **Ember voice by text type** (CLAUDE.md, `ember-voice` 2a): ranges, not floors. Never polish into elaborate prose; never chain more than two clauses.
- **Invoke prose-polisher with its parameters.** Every target file gets its own `file: <absolute path>` and `mode: apply` block. Without them the agent skips its pipeline. This was the root cause of the first, too-light clarity pass.
- **Polishers can't run voicecheck** (they have no shell tool). The main session must run `voicecheck.py`, or the clarity checker, on every polished folder before committing. When speech or narration is out of range, send the folder back to the same agent with numeric targets.
- **Rate limits:** the session limit stopped five agents, and then the weekly limit stopped them again. Each time they were resumed with SendMessage after the reset, never taken over inline.

---

## Problems Solved

- **The first clarity pass was too light** (2–3% cut). Cause: no polisher parameters, plus conflicting voice guidance. Fix: the 2a skill update, then a rerun with the proper `file:` / `mode:` blocks.
- **Speech over range after a single pass** in M4 (17.8), M5 (16.1 and 16.9) and r25 (15.7, with readaloud at 22.7 and 30% of sentences at 30+ words). Fix: targeted second passes by the same agents, sent with the measured numbers.
- **In-folder contradictions surfaced by the polishers:** s03, s05, M5, M6, r25 and r50, as listed in Changes Made.
- **One TELL in r10** (a not-X-but-Y line in the folio loss rule). Rewritten by the main session.

---

## Outstanding Work

### New this session
- [ ] **DR clarity polish.** Deferred by the user ("Go ahead with BD for now"). Use the BD method: the polisher with `file:` / `mode: apply` blocks and the 2a instructions, then the clarity check, a second pass when speech is out of range, and a PR per folder.
- [ ] **Clarity pass for the other converted factions** (Harpers and the rest) under 2a, if the user wants it. They were drafted under the old floors.
- [ ] **M6 harbor naming.** M6 says both "Deepwater Harbor" (ev-01 Underwater Rules) and "the harbor" (overview). Settle one name with the Faire location pages.
- [ ] **r25 dead branch.** Krebbyg "keeps out of the scene" if **Kreb Unmasked** is unmarked, but s02 always marks it before r25. Cut the branch in a later pass.
- [ ] **Guide 08:33.** Change "Dread Lord renown" to Commander, and name Laeral as the gold's recipient or drop her.

### Carried forward from Session 39
- [ ] **Answer the remaining BD decisions** at the end of the BD section of `docs/plans/harpers-out-of-scope-notes.md`:
  - the Zord cover's origin;
  - whether Fireball ev-04 sets **Jarlaxle Unmasked**;
  - per-member wording in guide 08;
  - where Renown 25 and 50 come from for every faction.
- [ ] **Write the outside readers and writers** for the BD outcomes as each quest is converted:
  - **Jarlaxle Unmasked:** Fireball ev-04 and Sea Maidens Faire.
  - **Faction Outposts:** **Windmill Raided**, **Windmill Map Taken**, **Windmill Clean Exit**, **Seven Masks Raided** and **Ott Kept/Lost**.
  - **Sea Maidens Faire:** the Soluun outcomes, **BD Watchers Sold**, **BD Contact Severed**, and the fates of Krebbyg and Fel'rekt.
  - **Cassalanter Villa:** **Florette Reported**, **Cassalanter Pact Shared with BD**, the Wazoo outcomes and **Esvele Hostile**.
  - **Xanathar's Lair:** the Nar'l outcomes and **Nar'l Bypass Learned**.
  - **Vault of Dragons:** **Marpenoth Saved/Crippled/Lost**, **Guild Survivor Escaped**, **Brandath Lead from Brimel** and the BD Commander proposal.
  - **OotG M2:** **Black Viper Source Noted**.
- [ ] **Fix the BD companion pages:**
  - guide 08: the exposé wording, the Renown 5 extraction, "Dread Lord", the "the party" wording, and :58, where Jarlaxle assigns the Spy against r10's contact;
  - org page 07;
  - `villains/jarlaxle.md:51`, which should name Vessa;
  - the Notable Figures pages: stat names; Featured-in lists that still name The Betrayal Pitch (Jarlaxle :8, Krebbyg `04`:8, Nar'l `03`:8); Soluun's cover story; Nar'l's tenure; Ott's "Cult Fanatic".
- [ ] **Act I–II contradictions logged for BD:**
  - Trollskull ev-03, ev-04 and ev-07;
  - Fireball ev-01 and ev-04;
  - Gralhund ev-01 and ev-09, including Istrid fleeing, which conflicts with DR.
- [ ] **Accept or replace the invented names.** Three first names collide between DR and BD: Ilmra, Odalys and Ilsa.
- [ ] **Voice profile for J.B. Nevercott.** Skills are written by the main session, so this needs a user request.
- [ ] **Reconcile the OotG M3 wererat silver rule** with the 2024 Wererat.
- [ ] **Structure docs and SOURCE_GUIDE (logged):**
  - SOURCE_GUIDE :219 puts the windmill in the North Ward;
  - arc-j :55, :75 and :322 (Mission 6 wording, and "Manshoon outpost");
  - arc-h :9 and :71 put the ships at a Mistshore pier, while the Faire overview says Smugglers' Dock.

### Carried forward from Session 38
- [ ] Faction Outposts must write **Yellowspire Ledger Taken**, **Yellowspire Letters Taken** and **Yellowspire Clean Exit**. 5B must add the relay ledger and the coded letters.
- [ ] Kolat Towers must name Vevette's fate, the K18 rune and the Doom Raiders parallel-operation result as outcomes.
- [ ] Gralhund Villa's Floxin Status flag must become named Event Outcomes.
- [ ] Sea Maidens Faire must read Soluun's fate (from BD s05).
- [ ] Faction Outposts must write **Manshoon Named** and **Yellowspire Raided**.
- [ ] Wire the Doom Raiders outcomes into their readers, arc-e through arc-j.
- [ ] Fix the Doom Raiders companion pages: guide 07, org page 06, the Notable Figures pages, `structural-rules.md:9` and `player-factions-overview.md:186`.
- [ ] Act I–II Doom Raiders contradictions: Finding Floon ev-01:115, Trollskull ev-04, Fireball ev-01:204, and Gralhund ev-01 and ev-09.
- [ ] Accept or replace the DR invented names.
- [ ] Settle Renown 25 and 50 reachability for all factions.
- [ ] Voice profiles for recurring minor DR NPCs.
- [ ] Confirm the three viewer changes on the live site.

### Carried forward from Session 37 and earlier
- [ ] Answer the six decisions in `docs/plans/harpers-out-of-scope-notes.md`. Decision 1 is answered for Jarlaxle and BD.
- [ ] One-faction membership wording on four guide pages.
- [ ] Wire the Harper outcomes into their readers, and give minor Harper NPCs voice profiles.
- [ ] Remaining non-rule inconsistencies: Finding Floon "two nights", Gralhund "two tendays", Vajra, and Istrid's loan.
- [ ] Confirm the Ember styling on the live site, and use the Artifact files map if the viewer is republished. Convert the old `[GM]` zones in Finding Floon and Trollskull.
- [ ] Bestiary; convert arc-e through arc-j; prose pass on the guides and setting pages; polish the Notable Figures profiles; recheck the Mission 5/6 summaries on the organization pages.
- [ ] `sources/backgrounds.json`; BD `ev-03` Ryvarra visibility; normalize sidebar titles in other factions; Renaer's Confidence holder framing.
- [ ] Ember organizations JSON; Trollskull Founders' Day wording; Asmodean Shrine Area 3; `#### Milestone: None` in other factions' events; Doom Raiders Viper muscle on Yagra's Notable Figures page; earlier invented details.
- [ ] Remaining faction rewrites: Lords' Alliance, Emerald Enclave, Order of the Gauntlet and Force Grey. Use the Session 38/39 method, and draft directly under ember-voice 2a.
- [ ] Older items: voice-run tooling portability, reproducible global skills, legacy automation references, the Astra/Sol defaults, and the Harper private Site.

---

## Warnings and Caveats

- **The clarity checker is not in the repo.** `claritycheck.sh` lived in the session scratchpad. It compares HEAD with the working tree for DC counts, bold terms, headings and block titles, then runs voicecheck. Recreate it, or run `voicecheck.py` on each file and diff the DC and bold counts by hand.
- **Some files sit slightly outside the 2a ranges, accepted on purpose:**
  - **Narration on the short side:** r10 at 15.4 and r25 at 15.8.
  - **Narration slightly long:** s02 at 21.9 and M5 at 21.9.
  - **Speech:** s03 at 15.6, and M4 ev-02 at 15.7.
  - **Design notes:** M3's have 25% of sentences at 30+ words.
- **git stash@{0}** ("BD clarity partial edits (stopped agents, conflicting skill guidance)") is obsolete, since every folder was redone. It can be dropped.
- **voicecheck false positives:** Zardoz's toast in BD s03, and "Keep it, quietly" in DR r50.
- **Nothing outside BD and DR reads the new outcomes yet.** That includes **Jarlaxle Unmasked**, which nothing writes.
- **The M6 limpet charge is invented:** the Dawn Clock and detonation numbers are flagged in the mechanics reference.

---

## Where to Start Next Session

Read this handoff and CLAUDE.md. Then read `ember-voice` section 2a: every new draft and polish must follow its by-text-type ranges.

If the user asks for the DR clarity pass, use the BD method:
- one `prose-polisher` per folder, at most 5 at once, each file given its own `file:` and `mode: apply` block plus the 2a targets and invariants;
- after each agent reports, run `voicecheck.py`, compare DC and bold counts with HEAD, and send a second pass when speech is over 15;
- commit with a "why" message, then PR and merge per folder.

Otherwise wait for the user to name the next task.
