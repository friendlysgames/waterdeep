# Emerald Enclave Drafter Instructions (Session 43)

Every `prose-drafter` working on a Emerald Enclave folder follows this page first, then its folder's section of the brief.

## Read first

1. **The brief.** Read all of `docs/plans/emerald-enclave-conversion-brief.md`. The user decisions, standing defaults, name fixes and your folder's section are binding.
2. **Your research report** in `docs/plans/emerald-enclave-research/`, for source facts and line references. Where the report offers options, the brief has already chosen.
3. **The restored draft in your folder.** It is your input.
4. **The previous version of your folder**, as a fact source only. Don't copy its structure or prose. It lives at `/tmp/claude-0/-home-user-waterdeep/724ec0d3-1411-5aee-88ce-0e8b98de0e73/scratchpad/ee-prev/campaign/quests/faction-events/emerald-enclave/<folder>/` (git `bc7655e`).
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

6. **The mechanics reference.** `docs/plans/emerald-enclave-mechanics-reference.md` gives every Enclave roster at three, four and five characters, every ally's Power, the charm rules, Jeryth's spell lists, the Tiny Beasts, the anchor and the Ward, and the r03 network table and r10 routes. Don't invent CR math or stat values. There are no intellect devourers in this set.
6a. **The newest model.** Force Grey is the latest application of this method. Read its matching page (for example `force-grey/m03-the-trouble-with-meloon/` for a mission, `force-grey/00-first-meeting/` and `force-grey/r03-junior-griffon/` for First Meeting and rank events) alongside the DR model.
7. **Sources.** Check `sources/SOURCE_GUIDE.md`, `sources/adventure-wdh.json`, `sources/Appendix_B_-_Player_Factions.md` and `sources/Appendix_C_-_Player_Faction_Missions.md` before writing a source beat.

## Skills to load before drafting

- `ember-voice`. Section 2a is binding.
- `character-voices`:
  - `voices/emerald-enclave.md` for Melannor and Jeryth;
  - `voices/independents-allies.md` for Sir Ambrose Everdawn and Durnan;
  - `voices/independents-adversaries.md` for Kelso Fiddlewick;
  - `voices/harpers.md` for Bonnie (and Mirt, if mentioned);
  - `voices/trollskull-community.md` for Tally, if present;
  - `voices/xanathars-guild.md` for Guild dockhands;
  - `voices/manshoons-zhentarim.md` for the Splinter cultists, if present.
- `adventure-reloaded`
- `dnd-adventure-text`
- `ember-adventure-style`
- `foundry-journal`

## Page skeletons (from the DR models)

- **Model pages read in full first.** Before drafting, read in full one DR and one BD event of your page type with its overview and design notes, plus the Harper equivalent. The user asked for this.
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
  - Summary: "occurs when an individual Emerald Enclave member first reaches Renown N…"
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
  - The renown line reads "Each participating Emerald Enclave member gains N base Renown for … Companions gain none."
  - Bonus lines read `- **+1 Renown:** condition`.
  - Briefs and debriefs are for members only.
  - A gate reads "becomes available when an individual Emerald Enclave member reaches Renown N and Nth level".
- **Manshoon.**
  - No speaker or readaloud names Manshoon, or calls Kolat Towers his home, unless **Manshoon Named** is marked for that member. Write it as paired readalouds or a GM line, the way DR m05 does.
  - Enclave speakers otherwise say "the Splinter" or "the other cell".
  - Overview and Involved Characters labels say "the Splinter".
  - Phaulkonmere is one block south of Kolat Towers. Nobody points at the towers or says what they are before the gate.
- **Jarlaxle.** No Enclave speaker names Jarlaxle, Zardoz Zord or Bregan D'aerthe to players. GM text may.
- **Cassalanters.** Suspicion only. Nobody knows they are infernalists. Don't use "herbs dying overnight and birds leaving"; that is the Cassalanter hook's sign.
- **Illuun.** Nobody names it before **Illuun Contact** or **Anchor Destroyed** (see the brief). Jeryth says "Something dreams below."
- **Animal messages.** Every *Animal Messenger* message is 25 words or fewer. Count them, and put the count in a GM line under the readaloud. Use the brief's animal for your event and Phaulkonmere's constants.
- **No intellect devourers, no Wish.** M5's waste is Splinter thrall-conditioning residue.
- **Rules.**
  - 2024 rules and names only, from the mechanics reference.
  - Checks read "**DC N Ability (Skill)**" with a stated fallback.
  - No single check settles a mission.
  - Fights go in `[!hazard]` with `#### X's Tactics`, a surrender or retreat condition and a non-combat route.
- **Zero-prep.** Name the NPCs, fix times and dates, decide the outcomes. Keep clocks to what the scene needs. No timetables or state machines.
- **Voice (`ember-voice` §2a).** These are ranges with a floor and a ceiling. Harper drafters wrote speech far too clipped (8.7–10 words), and one correction overshot to 26-word narration. Hit the range on the first pass.
  - Readaloud: 18–20 words per sentence on average, place then people then motion, ending in motion.
  - GM text: 17–19 words on average, one instruction per sentence, bullets for procedures, under 5% of sentences at 7 words or fewer.
  - Speech: 11–14 words on average, each point made once, cut after four sentences. Every Force Grey drafter wrote speech at 7–10 words even when told the range; aim for the middle of the range.
  - No readaloud or GM sentence past 28 words.
  - Theatrics belong to the characters, never to the narration.
  - Real profanity at each profile's level:
    - Melannor and Jeryth never swear.
    - Melannor uses no contractions and full, even sentences, not fragments.
    - Jeryth speaks one or two short sentences per turn. Hers are the one exception to the speech range.
    - Ambrose uses no contractions and never swears.
    - Bonnie swears dryly in private.
    - Kelso swears constantly.
    - Gerrick swears freely at the Guard.
    - Durnan speaks in two to six words.
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
