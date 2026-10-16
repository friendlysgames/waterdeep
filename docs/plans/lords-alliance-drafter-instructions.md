# Lords' Alliance Drafter Instructions (Session 44)

Every `prose-drafter` working on a Lords' Alliance folder follows this page first, then its folder's section of the brief.

## Read first

1. **The brief.** Read all of `docs/plans/lords-alliance-conversion-brief.md`. The user decisions, standing defaults, renames and your folder's section are binding.
2. **Your research report** in `docs/plans/lords-alliance-research/`, for source facts and line references. Where the report offers options, the brief has already chosen.
3. **The first-commit draft of your folder (R).** It is your input. It lives at `/tmp/claude-0/-home-user-waterdeep/f91bf122-6992-582e-a45c-3f8e22918b72/scratchpad/la-orig/lords-alliance/<folder>/`.
4. **The current files in your folder (PREV)**, as a fact source only. Don't copy their structure or prose. You overwrite them. A copy is at `/tmp/claude-0/-home-user-waterdeep/f91bf122-6992-582e-a45c-3f8e22918b72/scratchpad/la-prev/lords-alliance/<folder>/`.
5. **The model pages.** These are finished Doom Raiders files. Copy their page shapes exactly. DR is also the voice model: the user said "DR reads better".

   | Page type | Model |
   |---|---|
   | Mission overview | `campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/overview.md` |
   | Mission event | `.../doom-raiders/m03-the-missing-snobeedle/ev-01-the-missing-snobeedle.md` |
   | Multi-event mission | `.../doom-raiders/m04-silencing-skeemo/` |
   | First Meeting | `.../doom-raiders/00-first-meeting/ev-01-first-meeting.md` |
   | Standalone | `.../doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md` |
   | Rank event | `.../doom-raiders/r03-wolf/ev-01-wolf.md` |
   | Design notes | `.../doom-raiders/m03-the-missing-snobeedle/design-notes.md` |

6. **The newest model.** The Emerald Enclave set (Session 43) is the latest application of this method. Read the matching EE page alongside the DR model:
   - `emerald-enclave/m04-the-grells-in-the-dock-ward/` for a mission;
   - `emerald-enclave/00-first-meeting/` for the First Meeting;
   - `emerald-enclave/r03-summerstrider/` for a rank event.

   For s02, also read `force-grey/s01-the-full-picture/` for its three-route evidence table.
7. **The mechanics reference.** `docs/plans/lords-alliance-mechanics-reference.md` covers:
   - every roster at three, four and five characters;
   - every ally's Power;
   - the r10 introductions and legal ceiling;
   - the Watch-files table;
   - the r25 response-team intel and Masked Lord tables;
   - every stat value.

   Don't invent CR math or stat values.
8. **Sources.** Check `sources/SOURCE_GUIDE.md`, `sources/adventure-wdh.json`, `sources/Appendix_B_-_Player_Factions.md` and `sources/Appendix_C_-_Player_Faction_Missions.md` before writing a source beat.

## Skills to load before drafting

- `ember-voice`. Section 2a is binding.
- `character-voices`:
  - `voices/lords-alliance.md` for Jalester;
  - `voices/city-officials.md` for Laeral and any Watch officer with a profile;
  - `voices/independents-allies.md` for Esloon Bezant, Durnan and Saeth Cromley (check each);
  - `voices/xanathars-guild.md` for Guild agents (M1, M5);
  - `voices/manshoons-zhentarim.md` for Splinter agents (M2, M3);
  - `voices/harpers.md` for Mirt, if mentioned.
- `adventure-reloaded`
- `dnd-adventure-text`
- `ember-adventure-style`
- `foundry-journal`

## Page skeletons (from the DR models)

- **Model pages read in full first.** Before drafting, read in full one DR and one BD event of your page type with its overview and design notes, plus the EE equivalent. The user asked for this.
- **Mission overview**
  - `# Title: Overview`
  - `> [!gamemaster]**Quest Requirements**`, with the gate sentence, `#### Difficulty` (an italic level line plus stat blocks used) and `#### Milestone Progression` ("This faction mission awards no Milestone Points.")
  - `## Hook`
  - `## Background`, optionally followed by a `What Is Actually True` block
  - one `##` per scene or event, one paragraph each
  - `## Renown Opportunities`
  - `## Aftermath`
  - `## Involved Characters` (`- **Name** (Faction): role`)
  - `## Dangers & Enemies`
  - `## Overview` (two player-safe sentences)
- **Mission event**
  - `# Title`
  - `> [!gamemaster]**Gamemaster's Summary**`: "This … Event begins when … and ends when … In this Event, the party can:", then 4–6 bullets, then the membership line.
  - `> [!gamemaster]**Who Knows What**` or `**What Is Actually True**` (bullets) before the first `###`.
  - `### The Brief`: GM framing line, a readaloud with the brief in quoted speech, a `[!social]` block, about 5 `[!qna]` blocks. Jalester states the deadline.
  - 3–6 named `###` scenes.
  - `### Renown Opportunities`: the debrief with Jalester, readalouds keyed to outcomes, then `> [!gamemaster]**Mission Renown**`.
  - `### Aftermath` (GM prose only).
  - `### Concluding the Event`: one sentence, then `**Event Outcomes**`, then `**Next Steps**`.
  - `## Overview` (one sentence)
  - `## Summary` (first-person plural, 3–4 sentences)
- **Splitting a mission.** Split only where the brief says so. Mission Renown lives in the last event. Earlier events say "Nothing is awarded here" and chain with "Continue with **X**".
- **Rank event**
  - No overview file.
  - Summary: "occurs when an individual Lords' Alliance member first reaches Renown N…"
  - Hook scene, `What Is Actually True`, `### Naming the Rank`, one `###` per benefit. Each benefit is an exploration block with a per-member procedure: contact, place, notice, limit, delay, loss rule.
  - "The rank event awards no Renown."
  - Outcome "mark with the recipient's name", plus a per-member tracking line.
  - A member whose Renown later drops, or who is suspended, keeps the rank, and the benefits are suspended.
- **Design notes**
  - `# Design Notes: Title`
  - 3–4 `##` sections of plain paragraphs (no `***run-in***` headings): what the source gave, what changed, departures from the source.
  - A last section, `## Invented Names and Open Items`.
  - 15–35 lines.

## Hard rules

- **Blocks.** `> [!type]**Title**` for `readaloud`, `gamemaster`, `social`, `qna`, `exploration` and `hazard` only.
  - Readalouds have a bare `>` line after the tag and quote their speech.
  - Social blocks open `Name (Alignment, Species, pronouns) :: descriptor`, followed by a topics list and a "will not discuss" line.
  - qna answers are a single quoted paragraph.
- **Retired content: remove all of it.** That means:
  - `[GM]` zones, `[!narrative]`, `[!dialogue]`, `[!npc-narrative]`, `[!profile]`, `[!design]`, `[!lore]`, `[!abstract]`, `[!note]`, `[!info]`, `[!warning]`, `[!sidebar]`;
  - True/False flags, `Milestone:` headings, `## Read Aloud`, "Act N" scene labels;
  - "Arc X" labels (name the quest instead);
  - "Award +N" in outcomes;
  - "the GM decides" text, and defensive auditor-style GM text.
- **Endings.** Every event ends:
  - `### Concluding the Event`;
  - then `> [!gamemaster]**Event Outcomes**`, with lines in the form `- **Name** — mark when…; read by **Reader**`, adding "(unconverted)" for quests not yet converted;
  - then `> [!gamemaster]**Next Steps**` (the member gate, ending "awards no Milestone Points");
  - then `## Overview` and `## Summary`.
- **Outcomes.**
  - Every outcome has exactly one writer and at least one reader.
  - Keep the brief's names exactly; other files match on them.
  - Aim for 2–6 outcomes per event.
- **Membership.**
  - The renown line reads "Each participating Lords' Alliance member gains N base Renown for … Companions gain none."
  - Bonus lines read `- **+1 Renown:** condition`.
  - Briefs and debriefs are for members only.
  - A gate reads "becomes available when an individual Lords' Alliance member reaches Renown N and Nth level".
- **Manshoon.**
  - No speaker or readaloud names Manshoon, or calls Kolat Towers his, unless **Manshoon Named** is marked for that member. Write it as paired readalouds or a GM line, the way DR m05 does.
  - Alliance speakers otherwise say "the Splinter" or "the other cell".
  - Overview, Involved Characters and Summary labels say "the Splinter".
- **Jarlaxle.** No Alliance speaker names Jarlaxle, Zardoz Zord or Bregan D'aerthe to players before **Jarlaxle Unmasked**. Say "the carnival fleet". GM text may name him.
- **Cassalanters.** Suspicion only. Nobody knows they are infernalists.
  - Their errands are "a household errand" or "a family matter", never "infernal", "ritual" or "pact".
  - Halek Farran and Emira Volstren are hired agents, not household staff.
- **Illuun and the well.** No speaker names Illuun. Every scene at the Portal's well table gets one GM-only line: anything said there may reach something below, and Jalester does not know.
- **Contact.**
  - Jalester appears in person at the well table, except for the four breaks in the brief (M2, M3, M5, M6).
  - Notes are a short paragraph, signed "J.S.".
  - Each Brief from M1 to M5 states its deadline in Jalester's speech, because s01 reads it.
  - If **Laeral Told of Jalester** is marked, Sevel Dastar replaces Jalester.
- **No intellect devourers, no *Wish*, no 2014 names.** Never "Thug" or plain "Veteran".
- **Rules.**
  - 2024 rules and names only, from the mechanics reference.
  - Checks read "**DC N Ability (Skill)**" with a stated fallback.
  - No single check settles a mission.
  - Investigations give three independent leads (the Three Clue Rule), never three checks in a row.
  - Fights go in `[!hazard]` with `#### X's Tactics`, a surrender or retreat condition and a non-combat route.
- **Zero-prep.** Name the NPCs, fix times and dates, decide the outcomes. Keep clocks to what the scene needs. No timetables or state machines.
- **Voice (`ember-voice` §2a).** These are ranges with a floor and a ceiling. Hit them on the first pass.
  - Readaloud: 18–20 words per sentence on average, place then people then motion, ending in motion.
  - GM text: 17–19 words on average, one instruction per sentence, bullets for procedures, under 5% of sentences at 7 words or fewer.
  - Speech: 11–14 words on average, each point made once, cut after four sentences. Every earlier drafter wrote speech at 7–10 words even when told the range; aim for the middle of the range.
  - No readaloud or GM sentence past 28 words. GM sentences sit at 15–24 words, not 30+.
  - Every spoken line in a readaloud or qna is wrapped in "double quotes" (`> > "…"`), as on the DR/EE models. A quoted document, such as a note or ledger page, stays unquoted.
  - Theatrics belong to the characters, never to the narration.
  - Real profanity at each profile's level:
    - Jalester is level and formal, with rare self-directed swearing. He uses one raw "fuck" only if Faerrel is used against him. He closes every Brief with a question and says "Understood."
    - Laeral never swears in office and speaks in complete, measured sentences.
    - Esloon follows his voice entry. He never says why he left Thay.
    - Guild and Splinter toughs, Harko, Rezka and Ossery Klenn swear freely, each at their own level.
    - Sevel is plain and dry and may swear lightly.
    - Durnan speaks in two to six words.
  - None of the following:
    - fragment stacks, tricolons, "not X but Y", punchline endings, epigrams;
    - "quietly", "simply", "just" as padding (Jalester's order "quietly put him to the sword" is a quoted order and stays);
    - stacked adjectives or "as if" flourishes.
  - Use plain words: "says", not "observes".
  - You can't run `voicecheck.py`; the main session will. Write as if it will be run.
- **Length.** Aim at the DR model lengths:
  - overview 60–90 lines;
  - single-event mission 300–450;
  - split events 150–300 each;
  - First Meeting 350–450;
  - standalone 200–300;
  - rank event 220–330;
  - design notes 15–35.
  - Don't pad to reach them.
- **Scope.**
  - Write only the files in your folder, plus its `design-notes.md`.
  - Replace PREV's content completely. Keep the file names, except where the brief gives new event file names (M1, M5, and M3 only if it splits).
  - Don't delete files; the main session removes obsolete ones.
  - Don't touch anything else. Don't commit.

## Report back (short)

1. Files written.
2. Outcomes set and read.
3. Invented names.
4. Any contradiction outside your folder, with file:line, for the out-of-scope log.
