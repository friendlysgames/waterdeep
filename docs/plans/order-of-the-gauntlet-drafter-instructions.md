# Order of the Gauntlet Drafter Instructions (Session 45)

Every `prose-drafter` working on an Order of the Gauntlet folder follows this page first, then its folder's section of the brief.

## Read first

1. **The brief.** Read all of `docs/plans/order-of-the-gauntlet-conversion-brief.md`. The user decisions, standing defaults, renames and your folder's section are binding.
2. **Your research report** in `docs/plans/order-of-the-gauntlet-research/`, for source facts and line references. Where the report offers options, the brief has already chosen.
3. **The first-commit draft of your folder (R).** It is your input and it is in place in `campaign/quests/faction-events/order-of-the-gauntlet/<folder>/`. A read-only copy is at `/tmp/claude-0/-home-user-waterdeep/19a91aac-b9d5-5e3a-b464-72b606906164/scratchpad/ootg-orig/order-of-the-gauntlet/<folder>/`.
4. **The pre-restore files (PREV)**, as a fact source only, at `/tmp/claude-0/-home-user-waterdeep/19a91aac-b9d5-5e3a-b464-72b606906164/scratchpad/ootg-prev/order-of-the-gauntlet/<folder>/`. Don't copy their structure or prose. You overwrite R.
5. **The model pages.** Copy their page shapes exactly. The Lords' Alliance set (Session 44) is the newest application of the method; Doom Raiders is also the voice model ("DR reads better").

   | Page type | Model |
   |---|---|
   | Mission overview | `campaign/quests/faction-events/lords-alliance/m04-the-archer-above/overview.md` and `.../doom-raiders/m03-the-missing-snobeedle/overview.md` |
   | Mission event | `.../lords-alliance/m04-the-archer-above/ev-01-*.md` and `.../doom-raiders/m03-the-missing-snobeedle/ev-01-the-missing-snobeedle.md` |
   | Multi-event mission | `.../lords-alliance/m05-fentrees-ledger/` and `.../doom-raiders/m04-silencing-skeemo/` |
   | First Meeting | `.../lords-alliance/00-first-meeting/ev-01-first-meeting.md` and `.../emerald-enclave/00-first-meeting/` |
   | Standalone | `.../lords-alliance/s01-*/` and `.../doom-raiders/s01-davils-arrest/` |
   | Rank event | `.../lords-alliance/r03-redknife/` and `.../doom-raiders/r03-wolf/ev-01-wolf.md` |
   | Design notes | `.../doom-raiders/m03-the-missing-snobeedle/design-notes.md` |

   For s02, also read `force-grey/s01-the-full-picture/` for its evidence table. Read one DR and one BD event of your page type with its overview and design notes, plus the matching LA page, in full before drafting. The user asked for this.
6. **The mechanics reference.** `docs/plans/order-of-the-gauntlet-mechanics-reference.md` covers every roster at three, four and five characters, every ally's Power, and the rank tables. Don't invent CR math or stat values.
7. **Sources.** Check `sources/SOURCE_GUIDE.md`, `sources/adventure-wdh.json`, `sources/Appendix_B_-_Player_Factions.md` and `sources/Appendix_C_-_Player_Faction_Missions.md` before writing a source beat.

## Skills to load before drafting

- `ember-voice`. Section 2a is binding.
- `character-voices`: `voices/order-of-the-gauntlet.md` for Savra and the Order; `voices/cassalanters.md` for Gysheer and Victoro; `voices/xanathars-guild.md` for Pell and Guild agents; `voices/manshoons-zhentarim.md` for Splinter agents; `voices/independents-adversaries.md` for Kelso; `voices/bregan-daerthe.md` or the matching file for Gaxly; check each NPC's profile.
- `adventure-reloaded`, `dnd-adventure-text`, `ember-adventure-style`, `foundry-journal`.

## Page skeletons

- **Mission overview**
  - `# Title: Overview`
  - `> [!gamemaster]**Quest Requirements**`, with the gate sentence, `#### Difficulty` (an italic level line plus stat blocks used) and `#### Milestone Progression` ("This faction mission awards no Milestone Points.")
  - `## Hook`, `## Background` (optionally followed by `What Is Actually True`), one `##` per scene or event, `## Renown Opportunities`, `## Aftermath`, `## Involved Characters` (`- **Name** (Faction): role`), `## Dangers & Enemies`, `## Overview` (two player-safe sentences).
- **Mission event**
  - `# Title`
  - `> [!gamemaster]**Gamemaster's Summary**`: "This … Event begins when … and ends when … In this Event, the party can:", then 4–6 bullets, then the membership line.
  - `> [!gamemaster]**Who Knows What**` or `**What Is Actually True**` (bullets) before the first `###`.
  - `### The Brief`: GM framing line, a readaloud with the brief in quoted speech, a `[!social]` block, about 5 `[!qna]` blocks. Savra states the deadline.
  - 3–6 named `###` scenes.
  - `### Renown Opportunities`: the debrief with Savra, readalouds keyed to outcomes, then `> [!gamemaster]**Mission Renown**`.
  - `### Aftermath` (GM prose only).
  - `### Concluding the Event`: one sentence, then `**Event Outcomes**`, then `**Next Steps**`.
  - `## Overview` (one sentence), `## Summary` (first-person plural, 3–4 sentences).
- **Splitting a mission.** Split only where the brief says so. Mission Renown lives in the last event. Earlier events say "Nothing is awarded here" and chain with "Continue with **X**".
- **Rank event**
  - No overview file. Summary: "occurs when an individual Order of the Gauntlet member first reaches Renown N…"
  - Hook scene, `What Is Actually True`, `### Naming the Rank`, one `###` per benefit. Each benefit is an exploration block with a per-member procedure: contact, place, notice, limit, delay, loss rule.
  - "The rank event awards no Renown." Outcome "mark with the recipient's name", plus a per-member tracking line.
  - A member whose Renown later drops keeps the rank, and the benefits pause.
- **Design notes**
  - `# Design Notes: Title`, 3–4 `##` sections of plain paragraphs (no `***run-in***` headings): what the source gave, what changed, departures from the source.
  - A last section, `## Invented Names and Open Items`.
  - 15–35 lines.

## Hard rules

- **Blocks.** `> [!type]**Title**` for `readaloud`, `gamemaster`, `social`, `qna`, `exploration` and `hazard` only.
  - Readalouds have a bare `>` line after the tag and quote their speech.
  - Social blocks open `Name (Alignment, Species, pronouns) :: descriptor`, followed by a topics list and a "will not discuss" line.
  - qna answers are a single quoted paragraph.
- **Retired content: remove all of it.** `[GM]` zones, `[!narrative]`, `[!dialogue]`, `[!npc-narrative]`, `[!profile]`, `[!design]`, `[!lore]`, `[!abstract]`, `[!note]`, `[!info]`, `[!warning]`, `[!sidebar]`; True/False flags, `Milestone:` headings, `## Read Aloud`, "Act N" scene labels; "Arc X" labels (name the quest); "Award +N" in outcomes; "the GM decides" text.
- **Endings.** Every event ends:
  - `### Concluding the Event`;
  - then `> [!gamemaster]**Event Outcomes**`, with lines `- **Name** — mark when…; read by **Reader**`, adding "(unconverted)" for quests not yet converted;
  - then `> [!gamemaster]**Next Steps**` (the member gate, ending "awards no Milestone Points");
  - then `## Overview` and `## Summary`.
- **Outcomes.** Every outcome has exactly one writer and at least one reader. Keep the brief's names exactly; other files match on them. Aim for 2–6 outcomes per event.
- **Membership.**
  - The renown line reads "Each participating Order of the Gauntlet member gains N base Renown for … Companions gain none."
  - Bonus lines read `- **+1 Renown:** condition`.
  - Briefs and debriefs are for members only.
  - A gate reads "becomes available when an individual Order of the Gauntlet member reaches Renown N and Nth level".
- **Manshoon.** No speaker or readaloud names Manshoon, or calls Kolat Towers his, unless **Manshoon Named** is marked for that member. Savra says "the Splinter" or "the other cell". Overview, Involved Characters and Summary labels say "the Splinter".
- **Jarlaxle and Illuun.** No speaker names Jarlaxle, Zardoz Zord or Bregan D'aerthe to players before **Jarlaxle Unmasked** (say "the carnival fleet"), and no speaker names Illuun.
- **Cassalanters.** Suspicion only. Nobody knows they are infernalists. The only discovery beats are M4 and M5 (see the brief). Never state the pact, its terms, "twelve acts", "the Reckoning", a deadline, "contractual counterpart" or "infernal rider". Use "a household errand" or "the family". Gysheer, Halek Farran and the secretary are hired agents, not household staff. Savra does not say what the family worships.
- **Contact.** Savra at the door, except the written breaks in the brief (First Meeting when nobody is home, M5, M6, the rank summons). Notes are one short paragraph, signed "S.B.". Each Brief from M1 to M5 states its deadline in Savra's speech.
- **No intellect devourers, no *Wish*, no 2014 names.** Never "Thug", "Cult Fanatic" or plain "Veteran". Valdra appears nowhere.
- **Rules.**
  - 2024 rules and names only, from the mechanics reference.
  - Checks read "**DC N Ability (Skill)**" with a stated fallback. No single check settles a mission.
  - Investigations give three independent leads, never three checks in a row.
  - Fights go in `[!hazard]` with `#### X's Tactics`, a surrender or retreat condition and a non-combat route. Enemies spread their attacks.
- **Zero-prep.** Name the NPCs, fix times and dates, decide the outcomes. Keep clocks to what the scene needs.
- **Voice (`ember-voice` §2a).** These are ranges with a floor and a ceiling. Hit them on the first pass.
  - Readaloud: 18–20 words per sentence on average, place then people then motion, ending in motion.
  - GM text: 17–19 words on average, one instruction per sentence, bullets for procedures, under 5% of sentences at 7 words or fewer.
  - Speech: 11–14 words on average, each point made once, cut after four sentences. Earlier drafters wrote speech at 7–10 words even when told the range; aim for the middle.
  - No readaloud or GM sentence past 28 words. GM sentences sit at 15–24 words, not 30+.
  - Every spoken line in a readaloud or qna is wrapped in "double quotes" (`> > "…"`). A quoted document, such as a note or ledger page, stays unquoted.
  - Theatrics belong to the characters, never to the narration.
  - Real profanity at each profile's level. Savra swears in short clipped bursts, rarely. Pell, Kelso, Gysheer, Guild and Splinter toughs and the cultists swear freely at their own level.
  - None of: fragment stacks, tricolons, "not X but Y", punchline endings, epigrams; "quietly", "simply", "just" as padding; stacked adjectives or "as if" flourishes. Use plain words: "says", not "observes".
  - You can't run `voicecheck.py`; the main session will. Write as if it will be run.
- **Length.** Overview 60–90 lines; single-event mission 300–450; split events 150–300 each; First Meeting 350–450; standalone 200–300; rank event 220–330; design notes 15–35. Don't pad.
- **Scope.**
  - Write only the files in your folder, plus its `design-notes.md`.
  - Replace R's content completely. Keep the file names, except where the brief gives new event file names (M4's two events, and M2's second event if renamed).
  - Don't delete files; the main session removes obsolete ones. Don't touch anything else. Don't commit.

## Report back (short)

1. Files written.
2. Outcomes set and read.
3. Invented names, each collision-checked with a grep of `campaign/`.
4. Any contradiction outside your folder, with file:line, for the out-of-scope log.
