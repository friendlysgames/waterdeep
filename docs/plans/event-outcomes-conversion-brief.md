# Event Outcomes Conversion Brief (Session 51)

Binding brief for converting the retired `#### Name: True / False` headings and the "attunement" wording in the four Act I and II quest journals to named Event Outcomes. Source of the findings: the Session 51 legacy-format audit (73 headings in 28 files). Rulings come from the user in Session 51.

## Rule being applied

`CLAUDE.md`, Standing Rules, "Event Outcomes (replaces binary flags)":

> Campaign state is recorded as named Event Outcomes, never `#### Flag: True / False` headings or attunement blocks. `### Concluding the Event` ends with `> [!gamemaster]**Event Outcomes**` listing each outcome (`- **Outcome Name** — when to mark it; read by …`), then `> [!gamemaster]**Next Steps**`. An outcome keeps its established name so every reader still matches; later events read it in GM text ("If the party marked **BD Contact Severed**…"). No "Award X" language in outcomes; awards stay in the scene blocks.

Exemplar to copy: `campaign/quests/faction-events/force-grey/r10-senior-griffon/ev-01-senior-griffon.md`, lines 265 to 280 (the end of `### Concluding the Event`).

## Conversion rules

1. **One heading and its sentence become one bullet.** `#### Jarlaxle Informed: True / False` plus its body becomes `- **Jarlaxle Informed** — mark when …; read by …`. The old "True = A" becomes the "mark when" clause or the "read by" clause, whichever it described. Keep the outcome name exactly as the heading wrote it (the text before the colon).
2. **False meanings.** If the old text said what happens when the outcome is False and a reader depends on it, keep that in the reader's clause ("If not marked, …"). Drop "False" lines that only restate the absence.
3. **Heading-form outcomes with no True / False** (for example "Lords' Alliance Joined", "BD Contact Severed", "Jarlaxle Unmasked (per character)") move into the same list. Keep any per-character or per-member wording they carry.
4. **Outcomes that exist only in scene prose** ("Award **X** attunement" with no heading) get a bullet in the list too, and the scene line becomes "Mark **X**." Write "Mark", never "Award", in scene text for an outcome.
5. **Inline state.** "Set *X: True*" becomes "Mark **X**". "Set *X: False*" becomes "Do not mark **X**". "If *X: True*" becomes "If **X** is marked". "If *X: False*" becomes "If **X** is not marked".
6. **Retired words.** "attunement" (as campaign state), "flag" and "Yes / No" become "Event Outcome" or the outcome's name. Real D&D attunement (a magic item, an attunement slot) stays. `fireball/ev-02-the-house-of-inspired-hands.md:68` and `fireball/ev-04-the-sea-maidens-faire.md:72` are real and stay.
7. **`> **[GM]**` Next Steps blocks** at the end of the section become `> [!gamemaster]**Next Steps**` as in the exemplar. Do not touch other `[GM]` blocks.
8. **Flowcharts** (`flowchart.md`): rename every "Attunement" heading, column and label to "Event Outcome", and make every outcome name match the name the writing event uses.
9. **Do not invent.** No new outcomes, readers, DCs, rewards or scene content beyond what the old text states. If the old text is ambiguous or a reader is missing, leave it and report it.
10. **Voice.** Plain GM text, one instruction per sentence, no em-dash flourishes beyond the `—` the bullet format uses. Run `python3 .claude/skills/ember-voice/scripts/voicecheck.py <file>` on every changed file. Fix any TELL on a line you wrote. Pre-existing TELLs on lines you did not touch are out of scope.

## Rulings (user, Session 51)

- **Decision 2 (Finding Floon):** the body text and the flowchart use the heading names **Yagra Courteous** and **Durnan Acknowledged**. The Doom Raiders First Meeting already reads those names. Do not edit it.
- **Decision 3 (Gralhund Villa):** `ev-09-aftermath.md` stops reading a "Stone Holder" outcome. It reads **Stone Secured** (written by ev-06 and ev-07) and **Stone Recovered** (written by ev-08). Who holds the Stone when neither is marked comes from what happened in the ev-06 to ev-08 scene text (Bregan D'aerthe's Fel'rekt takes it, or it is lost to the Zhentarim, Xanathar or the nimblewright). Rewrite ev-09's three readers and flowchart row 102 that way.

## Report format (return this, do not commit)

For each changed file: path, and a one-line list of what changed. Then a section "Needs a ruling" with the exact quote, file and line for anything ambiguous, and a section "Left alone" for any hit you judged to be real D&D attunement or out of scope. Quote lines in full; the orchestrator cannot see your tool results.
