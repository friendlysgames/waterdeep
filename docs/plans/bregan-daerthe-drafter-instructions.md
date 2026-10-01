# Bregan D'aerthe Drafter Instructions (Session 39)

Every `prose-drafter` working on a Bregan D'aerthe folder follows this page, then its own folder brief.

## Read first

1. `docs/plans/bregan-daerthe-conversion-brief.md`. Read the whole thing. The user decisions, standing defaults and your folder's section are binding.
2. The research report for your folder, in `docs/plans/bregan-daerthe-research/`. Use it for source facts and line references. Where it lists options, the brief has already chosen.
3. The restored draft in your folder. It is your input: keep what the brief keeps, fix what it fixes.
4. The model pages, which are finished Doom Raiders files. Copy their page shapes exactly:
   - mission overview: `campaign/quests/faction-events/doom-raiders/m03-the-missing-snobeedle/overview.md`
   - mission event: `.../doom-raiders/m03-the-missing-snobeedle/ev-01-the-missing-snobeedle.md`
   - First Meeting: `.../doom-raiders/00-first-meeting/ev-01-first-meeting.md`
   - standalone: `.../doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md`
   - rank event: `.../doom-raiders/r03-wolf/ev-01-wolf.md`
   - design notes: `.../doom-raiders/m03-the-missing-snobeedle/design-notes.md`
5. `docs/plans/bregan-daerthe-mechanics-reference.md` for every fight's roster and numbers, once it is filled in. Don't invent CR math.
6. The sources the report cites. Check `sources/SOURCE_GUIDE.md`, `sources/adventure-wdh.json`, `sources/Appendix_B_-_Player_Factions.md` and `sources/Appendix_C_-_Player_Faction_Missions.md` before writing a source beat.

## Skills to load before drafting

`ember-voice`, `character-voices` (`voices/bregan-daerthe.md`, plus `voices/xanathars-guild.md` for Nar'l, Ott and Xanathar, `voices/cassalanters.md` for Cassalanter staff, and `voices/doom-raiders.md` for Davil or Gorra), `adventure-reloaded`, `dnd-adventure-text`, `ember-adventure-style` and `foundry-journal`.

## Hard rules

- **Blocks.** Use `> [!type]**Title**` for `readaloud`, `gamemaster`, `social`, `qna`, `exploration` and `hazard`, as in the model pages. Readalouds have a bare `>` line after the tag and quote their speech.
- **Retired content.** Remove all of it: `[GM]` zones, `[!profile]`, `[!design]`, `[!note]`, `[!info]`, `[!warning]`, True/False flags, `Milestone:` headings, `## Read Aloud`, "Arc X" labels (name quests instead: **Sea Maidens Faire**, **Xanathar's Lair**), "Award +N" inside outcomes, and defensive "the GM decides" text.
- **Endings.** Every event ends with `### Concluding the Event`, then `> [!gamemaster]**Event Outcomes**` (`- **Name** — mark when…; read by **Reader**`), then `> [!gamemaster]**Next Steps**` (member gate, ending "awards no Milestone Points"), then `## Overview` (one player-facing line) and `## Summary` (first-person plural journal).
- **Outcome readers.** Every outcome you set needs a reader. That can be a BD event in this folder set, a named quest marked "(unconverted)", or a line in your report back to me.
- **Membership.** It is individual. Write "Each participating Bregan D'aerthe member gains N base Renown", plus "**+1 Renown:** condition" lines, in a `[!gamemaster]**Mission Renown**` block. Companions gain none. Briefs and debriefs are for members only.
- **Jarlaxle.** No speaker says "Jarlaxle" unless **Jarlaxle Unmasked** is marked for that member. Write the gate as paired readalouds or a GM line, the way DR gates **Manshoon Named**. Until then BD speakers say "the captain" or "J.". GM text may state the truth. Zardoz never mentions drow, the Underdark or Luskan.
- **Lolth.** Bregan D'aerthe rejects her. Any mention is contempt. A spider symbol is the rejected goddess under a blade.
- **Cassalanters.** Nobody knows they're infernalists. Use suspicion only.
- **Manshoon.** Don't name him. If the Splinter comes up, say "the other cell" or "the Splinter".
- **Rules.** Use 2024 rules and names only. There is no Thug, Veteran, Cult Fanatic, Drow or Swashbuckler. Use the names in the mechanics reference. Checks read "**DC N Ability (Skill)**" with a stated fallback. No single check settles a mission.
- **Zero-prep.** Name the NPCs, fix the times and dates, and decide the outcomes.
- **Voice.** Speech averages 12+ words a sentence; narration averages 18+. Real profanity at each profile's level. No fragment stacks, tricolons, "not X but Y", punchline endings, or "quietly", "simply" or "just" as padding. You can't run `voicecheck.py`; I will. Write as if it will be run.
- **Scope.** Edit only the files in your folder, plus a `design-notes.md` if the brief asks for one. Don't touch anything else, and don't commit.

## Report back

Keep the report short:
1. the files written;
2. the outcomes set and read;
3. invented names;
4. any contradiction outside your folder that you hit, with file:line, for the out-of-scope log.
