# Harper Drafter Instructions (Session 41)

Every `prose-drafter` working on a Harper folder follows this page first, then its folder's section of the brief.

## Read first

1. **The brief.** Read all of `docs/plans/harpers-conversion-brief.md`. The user decisions, standing defaults, name fixes and your folder's section are binding.
2. **Your research report** in `docs/plans/harpers-research/`, for source facts and line references. Where the report offers options, the brief has already chosen.
3. **The restored draft in your folder.** It is your input.
4. **The previous version of your folder**, as a fact source only. Don't copy its structure or prose. It lives at `/tmp/claude-0/-home-user-waterdeep/6f58d0d2-f379-5140-92f5-a2193a7fb83a/scratchpad/harpers-prev/<folder>/` (git `7215515`).
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

6. **The mechanics reference.** `docs/plans/harpers-mechanics-reference.md` gives every roster, every ally's Power, the gazer, Nihiloor's occupying devourer and its extraction procedure, and Mirt's statistics. Don't invent CR math.
7. **Sources.** Check `sources/SOURCE_GUIDE.md`, `sources/adventure-wdh.json`, `sources/Appendix_B_-_Player_Factions.md` and `sources/Appendix_C_-_Player_Faction_Missions.md` before writing a source beat.

## Skills to load before drafting

- `ember-voice`. Section 2a is binding.
- `character-voices`:
  - `voices/harpers.md` for Mirt, Remi, Mattrim, Bonnie, Maxeene, Corene and Variel;
  - `voices/doom-raiders.md` for Davil and Yagra;
  - `voices/bregan-daerthe.md` for Jarlaxle/Erystian;
  - `voices/xanathars-guild.md` if Guild staff speak;
  - `voices/independents-allies.md` and `voices/city-officials.md` for Renaer, Laeral and Jalester as needed.
- `adventure-reloaded`
- `dnd-adventure-text`
- `ember-adventure-style`
- `foundry-journal`

## Page skeletons (from the DR models)

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
  - `### The Brief`: GM framing line, a readaloud with the brief in quoted speech, a `[!social]` block, about 5 `[!qna]` blocks.
  - 3–6 named `###` scenes.
  - `### Renown Opportunities`: debrief readalouds keyed to outcomes, then `> [!gamemaster]**Mission Renown**`.
  - `### Aftermath` (GM prose only).
  - `### Concluding the Event`: one sentence, then `**Event Outcomes**`, then `**Next Steps**`.
  - `## Overview` (one sentence)
  - `## Summary` (first-person plural, 3–4 sentences)
- **Splitting a mission.** Split only where a stage has its own state or clock (DR m04). Mission Renown lives in the last event. Earlier events say "Nothing is awarded here" and chain with "Continue with **X**".
- **Rank event**
  - No overview file.
  - Summary: "occurs when an individual Harper member first reaches Renown N…"
  - Hook scene, `What Is Actually True`, `### Naming the Rank`, one `###` per benefit. Each benefit is an exploration block with a per-member procedure: contact, place, notice, limit, delay, loss rule.
  - "The rank event awards no Renown."
  - Outcome "mark with the recipient's name", plus a per-member tracking line.
  - A member whose Renown later drops keeps the rank, and the benefits are suspended.
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
  - `[GM]` zones, `[!profile]`, `[!design]`, `[!abstract]`, `[!note]`, `[!info]`, `[!warning]`, `[!sidebar]`;
  - True/False flags, `Milestone:` headings, `## Read Aloud`;
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
  - The renown line reads "Each participating Harper member gains N base Renown for … Companions gain none."
  - Bonus lines read `- **+1 Renown:** condition`.
  - Briefs and debriefs are for members only.
  - A gate reads "becomes available when an individual Harper member reaches Renown N and Nth level".
- **Manshoon.**
  - No speaker or readaloud names Manshoon, or calls Kolat Towers his home, unless **Manshoon Named** is marked for that member. Write it as paired readalouds or a GM line, the way DR m05 does.
  - Harpers otherwise say "the Splinter", "the other cell" or "the Black Network has split".
  - Overview and Involved Characters labels say "the Splinter".
- **Jarlaxle.**
  - Read **Jarlaxle Unmasked** as the brief says.
  - He never shows reverence for Lolth; any mention is contempt.
  - Zardoz never mentions drow or the Underdark.
- **Cassalanters.** Suspicion only. Nobody knows they are infernalists.
- **Remallia.** Her Harper role is hidden until M4. Before then, in Harper text, she is at most a noble hostess.
- **Rules.**
  - 2024 rules and names only, from the mechanics reference.
  - Checks read "**DC N Ability (Skill)**" with a stated fallback.
  - No single check settles a mission.
  - Fights go in `[!hazard]` with `#### X's Tactics`, a surrender or retreat condition and a non-combat route.
- **Zero-prep.** Name the NPCs, fix times and dates, decide the outcomes. Keep clocks to what the scene needs. No timetables or state machines.
- **Voice (`ember-voice` §2a).** These are ranges, not floors.
  - Readaloud: 17–21 words per sentence, place then people then motion, ending in motion.
  - GM text: 15–20 words, one instruction per sentence, bullets for procedures.
  - Speech: 11–15 words, each point made once, cut after four sentences.
  - Theatrics belong to the characters, never to the narration.
  - Real profanity at each profile's level. Mirt never swears on business.
  - None of the following:
    - fragment stacks, tricolons, "not X but Y", punchline endings, epigrams;
    - "quietly", "simply", "just" as padding;
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
  - Replace the restored draft's content completely, but keep the file names. Add `ev-02` files only where the brief allows.
  - Don't touch anything else. Don't commit.

## Report back (short)

1. Files written.
2. Outcomes set and read.
3. Invented names.
4. Any contradiction outside your folder, with file:line, for the out-of-scope log.
