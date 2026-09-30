# Doom Raiders Conversion Brief

## Context

The Harper faction events went from restored first-commit drafts to finished Ember-voice adventure text in Session 35, and got a voice pass in Session 37. The user wants the Doom Raiders done the same way. Step 1 is already committed and pushed as `68c2acd`: all 26 Doom Raiders files are restored to their first commits and are now the rewrite input.

Five Sonnet 5.5 `source-researcher` agents have already produced:
- a Harper-model conversion spec;
- per-event source and problem reports for the First Meeting, s01, s02, r03–r50, M1–M3 and M4–M6;
- a cross-campaign reader audit.

Those reports read the pre-restore text, so every line reference in them gets re-verified against the restored drafts (Phase A below).

**The user's decisions (this session):**
1. **Manshoon gate:** gate on a new outcome, **Manshoon Named**, set at the Faction Outposts Interrogation House.
   - Until it is marked, Doom Raider NPCs say "Floxin's cell", "the other cell" or "the Splinter". The Doom Raiders believe Floxin leads the Splinter.
   - Once it is marked, they may name Manshoon. The same gate governs calling Kolat Towers his home.
   - The truth appears in GM-only text.
2. **M6 conflict:** **Force Field Gap Intel** moves to the end of M5, as Ziraj's surveillance notes surfacing. M6 becomes a hunt that runs after Kolat Towers, and its outcomes feed r25 and Vault of Dragons.
3. **Yellowspire (M5):** a return visit.
   - If Faction Outposts 5B ran, the relay has been rebuilt and reinforced.
   - If 5B didn't run, M5 uses the arc-e layout.
   - Both cases put it in the Castle Ward with Amath and the acolytes, matching WDH and arc-e.
4. **Scope:** rewrite only the Doom Raiders event files, plus 7 new design-notes files. Every contradiction outside the folder goes into a new **Doom Raiders** out-of-scope section. Nothing outside the folder is edited.

## Conversion spec (from the finished Harper files)

**Page shapes**
- **Event pages:**
  - `# Title` (plain title, no "Doom Raiders Mission N —" prefix).
  - A `> [!gamemaster]**Gamemaster's Summary**` in the form "This Social Event occurs when… In this Event, the party can:" with bullets.
  - Descriptive `### Scene` headings: the Brief first; no Act labels, no `Hook`/`Background` scenes unless needed.
  - Then `### Renown Opportunities`, `### Aftermath` and `### Concluding the Event`.
  - The event closes with `> [!gamemaster]**Event Outcomes**` (`- **Name** — when to mark; read by **Reader**`) and `> [!gamemaster]**Next Steps**`. Next Steps states the member-specific gate and ends "awards no Milestone Points".
  - After that come `## Overview` (one line, player-facing) and `## Summary` (the first-person journal).
- **Overview pages:**
  - `# Title: Overview`, then `[!gamemaster]**Quest Requirements**` containing `#### Difficulty` and `#### Milestone Progression`.
  - Then `## Hook`, `## Background`, the scene sections, `## Renown Opportunities`, `## Aftermath`, `## Involved Characters`, `## Dangers & Enemies` and `## Overview`.
- **Design notes:** `# Design Notes: Title`, then 3–4 short `##` sections covering the rationale, the source departures, and pointers to the out-of-scope notes.

**Blocks**
- Every block uses `> [!type]**Title**`.
- Readalouds have a bare `>` line after the tag, open on the place and end in motion.
- `[!social]` blocks start with `Name (Alignment, Species, pronouns) :: descriptor`.
- `[!qna]` answers are actual quoted lines.
- Every fight is a `[!hazard]`: an ordinary 2024 stat block, `#### X's Tactics`, a surrender or retreat condition, and a non-combat route. There are no boss blocks and no "Combat Phases".
- Every check reads "**DC N Ability (Skill)**" and has a stated fallback.

**Retired content to remove**
- Act headings.
- `#### Milestone: None`.
- `True / False` flags.
- "Award +N Renown" inside outcomes.
- Old sidebars.
- "Read Before Running".
- "Specific dialogue is presented below".
- Defensive rules-lawyer GM text.

**Membership (R3)**
- Renown text reads "Each participating Doom Raiders member gains N base Renown" and "**+1 Renown:** condition". Companions gain none.
- Briefs and debriefs are for members only.
- Gates read "when an individual Doom Raiders member reaches Renown N".
- **Doom Raiders Joined** and the rank outcomes are marked per recipient.
- The First Meeting is per candidate, and a PC already in another faction gets no offer.
- Rank benefits get written procedures and are tracked per PC.

**Renown**
- Base Renown is 2/2/3/3/4/4, matching guide 07 and the CLAUDE.md calibration.
- Bonuses are listed explicitly.
- Mission gates are recomputed so they can be reached from a Renown 1 start.

**Voice**
- Load `ember-voice`, `character-voices` (`voices/doom-raiders.md`, plus the other docs for Soluun, Esvele, Kelso and Fala), `adventure-reloaded`, `dnd-adventure-text`, `ember-adventure-style` and `foundry-journal`.
- Speech is in character with real profanity at each profile's level, averaging 12 or more words per sentence. Narration averages 18 or more. No forced joins.
- Minor NPCs without profiles are voiced from the event text and listed in the design notes.

## Per-folder content fixes (source-first; WDH/Appendix C wins over drafts)

**00-first-meeting (+ new design-notes)**
- Davil's Two Zhentarims answer names Floxin as fronting "the other cell" (WDH: vague, "someone we thought was long dead").
- The ask becomes "anything on the other cell or Floxin".
- Recruitment is per candidate.
- **Yagra Courteous** is read as an outcome name, and the retired flag format is logged as out of scope.
- The Istrid loan uses guide 07's 200 gp; the 400 gp in Trollskull ev-04 is logged.
- Add a refusal path and a Yagra beat.

**M1 The Dockside Killer**
- Restore the source's shape: Gorra on Night 1 and Heldar on Nights 2–3.
- Restore the Seven Masks *Blood Wedding* playbill with the DC 12/14 Rongquan Mystere lead, which BD-M4 and arc-e rely on.
- Soluun's disownment is a cover story (NF page and arc-e); he rejects Lolth.
- Remove the phase construct.
- Fix Heldar's reader: M2 reads **Heldar Survived**, or the outcome is dropped.
- Change "several months" to weeks, before Tarsakh 20.

**M2 The Poisoned Delivery**
- Restore the mint vials (DC 20 Arcana or *detect poison and disease*).
- Restore Esvele at the God Catcher, 15 pp.
- Restore the death of Cevin Rallygar and the Wazoo notice (DC 14/18).
- Restore the Davil confrontation, where he evades.
- Davil's knowledge follows one line: he does not know until M4.
- **Coffer Returned** gets a real M4 reader or is cut.
- Esvele is House Rosznar.

**M3 The Missing Snobeedle**
- Tashlyn briefs, because this is after the arrest.
- Dasher has been gone six months; Blossom is "old".
- The meeting is at the Waymoot at highsun, and he offers a 200 gp bribe.
- Restore the payoff: Emmek Frewn is bankrolled with Doom Raider money through Istrid.
- Kelso is voiced to his profile and placed in the Field Ward (OotG-M3).
- Any Wererat fight gets CR 2.0 numbers.
- The Faction Outposts reader claims are logged, not invented.

**M4 Silencing Skeemo**
- Tashlyn briefs: "make it look like an accident".
- Restore the double-agent gambit: Insight DC 18 shows partial truth, and DC 14 shows the fear.
- Restore a capture-alive branch.
- Add an accident-staging mechanic.
- Fix concentration: *Fly* and *greater invisibility* can't run together, and *Fly* lasts 10 minutes.
- Rebuild the entry-route to chase mapping so it has no contradictions.
- If he escapes, **Skeemo at Kolat Towers** is set; the name is gated in speech.
- R1 wording follows decision 1.

**M5 The Yellowspire Job**
- It is a return visit, per decision 3.
- It sets **Force Field Gap Intel** (decision 2), read by Kolat Towers Scene 1.
- Rename **Ledger Recovered** to avoid the OotG M5 collision (proposed: **Relay Ledger Recovered**).
- Fix the floor count and the plate check (Perception).
- Give the ten-minute clock a real trigger.
- The amulet hook points to the arc-i method or is cut.

**M6 Ziraj's Last Hunt**
- It runs after Kolat Towers: the kill team is Splinter remnants taking revenge.
- Add a failure branch if Ziraj dies.
- Settle Ziraj's weapon and stat block from his NF page (Assassin, longbow).
- Put Yagra's swearing and Ziraj's 2–5-word speech in line with their profiles.
- Remove the 43-names duplication with arc-i, and log it.
- Outcomes feed r25 and Vault of Dragons.

**s01 Davil's Arrest (+ design-notes)**
- Tashlyn is the WDH source of the rumour: Floxin is the rumoured leader, a warrant is out, scrying fails, and the tip came from inside the Network.
- Fix the calendar chain: the villa is Ches 24, the arrest about Ches 26, the meeting a fixed date.
- Name a Watch contact.
- Make the release efforts a real multi-approach beat with stated odds.
- Outcomes are per member.

**s02 Davil's Return (+ design-notes)**
- Branch on the M4 result: eliminated, captured or escaped.
- Gate the Skeemo-file line so it names Floxin's cell unless **Manshoon Named** is marked.
- Fix the release-timing wording.

**r03 Wolf, r10 Viper, r25 Ardragon, r50 Dread Lord (+ design-notes each)**
- Rank benefits become individual procedures: counters, named contacts, safe-house location.
- R1 gating applies throughout.
- Viper's muscle is reconciled with Yagra's profile.
- Ziraj's favour is once per PC.
- r50 corrects the founders to five, with Yagra a later member, and branches the empty chair on the M4 result.
- r50 adds a real cost to declining.

## Execution

**Phase A — briefs (1 source-researcher, Sonnet 5.5)**
- Write `docs/plans/doom-raiders-conversion-brief.md` with:
  - the spec above;
  - the four decisions;
  - a per-folder fix list with line references re-verified against the restored drafts;
  - the source excerpts each drafter needs.
- The main session reviews it and commits it.

**Phase B — mechanics (encounter-builder, Sonnet 5.5)**
- Write `docs/plans/doom-raiders-mechanics-reference.md` with CR 2.0 numbers for every hazard at 3, 4 and 5 combatants: M1 Soluun (Scout), M3 optional Wererats, M4 Skeemo (Mage), M5 relay defenders, M6 kill team, and r50 ally power.
- `rules-lookup` verifies 2024 records.
- Commit.

**Phase C — drafting (prose-drafter, Sonnet 5.5, at most 5 at once, one editor per folder)**
- Each folder gets its own brief: the conversion brief section, the mechanics reference and the skill list.
- Batch 1: 00-first-meeting, M1, M2, M3, s01.
- Batch 2: M4, M5, M6, s02.
- Batch 3: r03, r10, r25, r50.
- Commit per folder after review.

**Phase D — out-of-scope log**
- Add a `## Doom Raiders event rewrite (Session 38)` section to `docs/plans/harpers-out-of-scope-notes.md`. It covers:
  - guide 07, org page 06, and the Davil, Yagra, Skeemo, Tashlyn and Floxin NF pages;
  - Trollskull ev-04 and Fireball ev-01:204;
  - Gralhund ev-01 and ev-09;
  - Finding Floon ev-01:115;
  - arc-e, arc-f:41, arc-i (Skeemo location, 43 names, outcome names), arc-j:53;
  - **Manshoon Named**, which still needs a writer at the Interrogation House when arc-e is converted.

## Verification (every folder, before its commit)

- `python3 .claude/skills/ember-voice/scripts/voicecheck.py <file>` prints zero TELLs. Speech averages 12 or more words per sentence and narration 18 or more.
- Greps over the folder:
  - "Manshoon" appears only in GM-only blocks or behind a **Manshoon Named** conditional.
  - No `Act 1`, `Milestone:`, `True / False`, "the party reaches Renown", "Award +", `[!design]`, `[!npc-narrative]` or `[!dialogue]`.
- Every Event Outcome name has a real reader in the folder, a named arc-doc reader, or an entry in the out-of-scope log.
- The main session reviews each file for mission depth (multiple beats, no single-check resolution), source fidelity against the brief, and the 2024 creature names.
- A final `consistency-checker` pass (Sonnet 5.5) runs over the whole folder before the last commit, then push to `claude/doom-raiders-faction-events-ykv5c7`.

---

## Source facts per folder (research, Session 38)

Line numbers below were read before the restore; re-find them in the restored drafts. The research agents could not open the Alexandrian PDFs or `sources/Other remix files/Davil and the Doom Raider Zhents + Elf Killer mission and more.docx`. Drafters should read Appendix B (Doom Raiders, ~l.502–692) and Appendix C (Act IIe, from ~l.1167) directly.

**WDH canon (`sources/adventure-wdh.json`)**
- **First meeting (~3990–4038).**
  - A flying snake brings the invitation: "Want to be part of something big? Speak to Davil Starsong at the Yawning Portal."
  - Yagra leads the party to Davil's table.
  - Davil says the Doom Raiders provide "loans, mercenaries, and other services". He also says another Black Network gang "tried to take over the Xanathar Guild. They failed, setting off a war in the streets."
  - He never names Manshoon or Floxin.
- **Tashlyn's information (4029–4035).** She passes on what she knows:
  - The *rumored* leader of the renegade faction is Urstul Floxin.
  - A warrant is out for him, and scrying fails.
  - The botched Renaer kidnapping may draw him back.
  - The meeting is arranged through Yagra, in the City of the Dead.
- **Davil's release (4038).** He is released once the Lords are satisfied.
- **Appendix B (31902–31977).**
  - The five founders are Davil, Istrid, Skeemo, Tashlyn and Ziraj. Yagra joined later.
  - Tashlyn is a City Guard captain under the dwarf magister Vorondar Levelstone at the South Gate.
  - Ziraj kills only when a friend asks.
- **Other WDH details.** Istrid's loans run up to 2,500 gp at 10% per tenday (1455). Davil asks for a 5,000 gp donation (14893). Meloon is hunting Davil (1548).
- **Floxin.**
  - He is a Black Network assassin, Manshoon's field agent.
  - He escapes Gralhund G15a.
  - He will not give up the Stone until he speaks to "his secret master, Manshoon".
  - At Kolat Towers he is punished.
  - His NF page is `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md`.
- **Arc D (`sources/Act_III_Arc_D.md`).**
  - ~l.250 has a "For Doom Raiders Characters: Asking About Floxin" sidebar. The Watch tip against Davil came from inside the Network. Keep the tip; drop "Manshoon's blade" in speech unless **Manshoon Named** is marked.
  - ~l.634 has Tashlyn trading Davil's freedom for proof that Floxin ordered the fireball.

**M1 (Appendix C ZR-1 ~1173–1225; WDH 4055)**
- Davil briefs the party in person.
- There are three stakeout nights at the Muleskull, 2–4 bells.
  - Night 1 brings Harbor Watch officer Gorra (DC 12 Persuasion).
  - Nights 2–3 bring Heldar, a half-elf sailor (**Bandit**).
- Soluun ambushes in the alley. Spotting him takes DC 18 Perception. He flees at half HP over the rooftops.
- The loot is a bloodstained Seven Masks Theater playbill for *Blood Wedding*.
  - DC 12 Intelligence links it to Bregan D'aerthe.
  - DC 14 notes the owner, "Rongquan Mystere", with recent Luskan-backed investment.
- Heldar alive earns 50 gp each. Davil's only comment is "That's interesting."
- The source victims were decapitated by a blade; reconcile that with Soluun's weapon.
- Soluun's NF page (`bregan-daerthe/02-soluun-xibrindas.md`) says the disownment is a cover story. His voice profile is in `voices/bregan-daerthe.md`.

**M2 (ZR-2 ~1229–1285; WDH 4059)**
- Skeemo hands over a silk-lined coffer of four "mind reading" vials. They are poison, and they look, smell and taste of mild mint. Identifying them takes DC 20 Arcana or *detect poison and disease*.
- The delivery goes to Esvele (Black Viper, House Rosznar, Sea Ward) at the God Catcher, for a black velvet pouch of 15 pp.
- The merchant Cevin Rallygar then dies, reported in a Wazoo notice.
  - DC 14 Investigation ties it to a Rosznar-adjacent trading dispute.
  - DC 18 ties it to the Black Viper's pattern.
- Confronted, Davil says "Skeemo operates semi-independently."

**M3 (ZR-3 ~1289–1346; WDH 4064, 1321, 4264)**
- The briefing gives the Snobeedles, 500 gp, and "don't get in trouble with the Watch".
- The party spends three days in the Southern Ward. Arranging the meeting takes DC 18 Persuasion or Intimidation, or DC 14 with rapport.
- The meeting is at the Waymoot at highsun.
- Dasher is a wererat by choice and has been missing about six months. Blossom is an "old druid".
- He offers a 200 gp bribe from the Shard Shunners' fund.
- He reveals that **Emmek Frewn is bankrolled with Doom Raider money through Istrid Horn** (Emmek borrowed 150 gp).
- The party has three choices.
- Kelso, Dasher, Danika Fiddlewick and Brynn Hilltopple work for Emmek against Trollskull Manor.

**M4 (ZR-4 ~1350–1412)**
- Tashlyn sends a flying snake: "make it look like an accident".
- Skeemo is in a hire-dray with five commoners and a driver.
- The source chase is 4 successes before 3 failures. Skeemo then casts *fly*, and *counterspell* can stop it. After that he uses *greater invisibility*, which takes DC 20 Perception or *detect magic* to follow.
- If he escapes, he goes to Kolat Towers.
- Cornered, he claims to be a double agent.
  - DC 18 Insight shows a partial truth.
  - DC 14 Insight shows his fear.
- The party can bring him back alive.
- The satchel holds a spellbook, a *potion of mind reading* and 150 gp.

**M5 / M6.** Neither mission is in the source.
- Yellowspire is Amath Seccent's tower in the Castle Ward (WDH ~7635, Winter Old Tower). arc-e 5B (~l.217–231) adds four acolytes, a one-in-three chance of Agorn Fuoco, and a teleportation circle to Kolat Towers.
- Ziraj's NF page gives him an **Assassin** with modifications and an oversized longbow. Fala shelters him (WDH ~3432). Fala's voice is in `voices/trollskull-community.md`.

**Renown gates.** Rank thresholds are Fang 1, Wolf 3, Viper 10, Ardragon 25, Dread Lord 50. Membership starts at Renown 1. Mission base Renown is 2/2/3/3/4/4.
- Set the mission gates so they are reachable in order from base awards: matching the Harpers: M1 on joining at 2nd level, M2 Renown 3 and 3rd level, M3 Renown 5 and 4th, M4 Renown 8 and 5th, M5 Renown 10 and 6th, M6 Renown 13 and 7th.
- Ranks 25 and 50 need bonus Renown from other sources; say so in the r25 and r50 design notes.

**Outcome readers verified to exist outside the folder.** None use DR outcome names. The arc docs read "Mission N complete" or "renown 10+". Where an outcome's reader is an unconverted arc doc, keep the outcome, name the quest as reader, and list it in the out-of-scope log.
