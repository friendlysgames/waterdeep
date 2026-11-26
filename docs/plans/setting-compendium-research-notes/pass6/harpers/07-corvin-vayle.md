# Pass 6 research notes: Corvin Vayle

Page: `campaign/setting/notable-figures/harpers/07-corvin-vayle.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR. Corvin is a minor figure (brief ruling 2), so the short Personality and Connections apply. He still needs a Background (ruling 15) and a `### Voice` block (ruling 16).
Organization page: `campaign/setting/organizations/01-harpers.md`
Factions Guide: `campaign/guides/factions/02-harpers.md`
Voice profile: `.claude/skills/character-voices/voices/harpers.md` ("### Corvin Vayle", lines 119-133)
Wiki: NOT FOUND. The extract `scratchpad/wiki-harpers/07-corvin-vayle.txt` reads "NOT FOUND". No wiki page for him. Nothing in `sources/research/pass5-bundles/harpers/wiki.txt` names him (Grep, case-insensitive "vayle|corvin|maxeene|nessa").

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json` has no Vayle, no Corvin and no Nessa (Grep, case-insensitive). The only Harper-related hit is the Maxeene mission, which is in the Maxeene notes.
- Alexandrian Appendix D: `sources/Appendix_D_-_Running_the_Tavern.md`, lines 289-306 (Candidate 5). Quotes are copied from the Read output. Lines 292-294 sit in a `<div class="fvtt narrative">` block; the paragraph text is quoted as written.
- Alexandrian PDF `sources/27. Addendum A Night in Trollskull Manor.pdf` (38 pages): read as page images, PDF pp.1-20 (printed pp.178-191). The staffing pages are PDF pp.4-5 (printed pp.182-183). The Vayles are not in them. PDF pp.21-38 were not read. Quotes from the PDF are transcriptions. Check them with `pdftotext -layout` before any quote goes into prose.
- Alexandrian PDF `sources/3. Player Character Factions.pdf` (3 pages): read as images, pp.1-3 (printed pp.23-25). No mention of Corvin, Nessa or Maxeene.
- Harpers organization page: the line numbers in older notes (`docs/plans/setting-compendium-research-notes/pass5/harpers.md`, which cites `01-harpers.md:32` to `:34`) are stale. The current file has the Key Members at lines 104-106.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **No source gives Corvin a day-one job.** The Persona calls the twins "servers". The Trollskull guide and Appendix D present them as hire candidates for the Trollskull Manor (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:58`; `sources/Appendix_D_-_Running_the_Tavern.md:289`). The tavern is not open on Ches 1. The PDF says the PCs are rewarded with "an abandoned inn" (PDF p.1), and the quest says "Staff was hired" at the Grand Opening (`campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:159`). Where he works on Ches 1 is unsourced (section F1).
2. **The "minor Harper waypoint" is conditional in the Alexandrian text.** The campaign org page and the Corvin page state it in the present tense (`01-harpers.md:104`, Corvin page L11 and L25). Appendix D says "the tavern will become, de facto, a minor Harper waypoint" and "If Harper-affiliated characters hire them" (`Appendix_D:296`, `:300`). The Trollskull guide says "Tavern becomes a minor Harper waypoint" under Faction Note (`03-staff-and-hiring.md:58`). Section D2.
3. **The Overview is 24 words, over the 21-word limit** (L29). See C row 11.
4. **Corvin is in the Harpers Key Members list but not in the org page's cross-reference list of "the principal Harpers".** `01-harpers.md:161` lists Maxeene among them and leaves out both twins. `campaign/guides/factions/02-harpers.md:82` lists both twins. See D1.
5. **Name collisions.** A Gralhund Villa servant is also named Corvin (`sources/Act_III_Arc_E.md:89` and `:129`). A Trades Ward advocate is Corvin Hallowell (`campaign/gazetteer/waterdeep/trades-ward.md:259`). Neither is this figure. See D4.

---

## A. Background facts by theme

### A1. Origin, family and age
No source gives a birth year, a home district, parents, or a family name. The sourced facts are below.

**Twin, with Nessa (Persona, Relationships; the Trollskull appendix)**
> "Corvin and Nessa Vayle are a package hire for the tavern staff, a minor Harper waypoint through Corvin's courier role, and Trollskull Manor server candidates detailed in the **Trollskull Manor** guide. His twin sister is **Nessa Vayle**."
> — `campaign/setting/notable-figures/harpers/07-corvin-vayle.md:25`

> "*CN female/male humans, Commoner. They come as a pair. One is a Harper courier.*"
> — `sources/Appendix_D_-_Running_the_Tavern.md:290` (heading at `:289`: "**Candidate 5 — the Twins: Nessa and Corvin Vayle**")

> "Illuskan human twins" — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58` (the row reads "| 5 | **Nessa & Corvin Vayle** | CN Illuskan human twins |")

**Age, upbringing, and how long they have worked bars (Appendix D narrative, the interview)**
> "They arrive together — a young woman and a young man, identical in height, both with sharp cheekbones and the particular watchfulness of people who grew up in a city and learned early to pay attention. The woman speaks; the man looks around the room. "We're a package," she says. "Nessa and Corvin Vayle. We've been working bars in pairs since we were sixteen — one takes the floor, one handles the back and the cellar. We don't work apart. We work cheap because we work fast and because frankly we need the combined wage to afford rent in the North Ward." The man glances back. "We're good," he says simply."
> — `sources/Appendix_D_-_Running_the_Tavern.md:293`

Corvin is "the man" in that passage. "The woman" is Nessa.

### A2. The courier role (how he came to the Harpers' service)
Only the courier role is sourced. The recruiting event is not.

> "Corvin, the quieter one, is also a part-time courier for the Harpers — not an agent, just a trusted carrier who moves messages between contacts. He does not bring this work into the tavern deliberately, but a Harper contact may occasionally leave a message at the bar for him, and the tavern will become, de facto, a minor Harper waypoint. Mirt knows the Vayles; this is not accidental."
> — `sources/Appendix_D_-_Running_the_Tavern.md:296`

> "Corvin is a Harper courier (not a field agent). Tavern becomes a minor Harper waypoint. Mirt's network has already accounted for their placement."
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58` (Faction Note column)

> "- **Corvin Vayle** — Illuskan human twin; runs a minor Harper waypoint through a courier role. See the **Corvin Vayle** page in Notable Figures."
> — `campaign/setting/organizations/01-harpers.md:104` (Key Members)

### A3. Rank, post and standing with Mirt
> "Corvin, the quieter one, is also a part-time courier for the Harpers — not an agent, just a trusted carrier who moves messages between contacts." (Appendix D:296, quoted in A2)

> "**Hidden Quality:** DC 14 Insight during the interview reveals that Corvin's attention to the room is more systematic than curiosity. Asking him about it directly prompts him to confirm, with some relief, that he does "some courier work" and that it "occasionally overlaps with his social life." He will not name the Harpers unless the characters already have Harper connections."
> — `sources/Appendix_D_-_Running_the_Tavern.md:298`

> "**Faction Note:** Corvin is a Harper courier. Harper party members will find Mirt already knows the Vayles — this was not accidental. If Harper-affiliated characters hire them, Mirt considers the tavern a confirmed waypoint and will occasionally route sensitive documents through it. This is an asset and a liability."
> — `sources/Appendix_D_-_Running_the_Tavern.md:300`

> "- **Information Is the Currency:** ... Corvin Vayle passes folded notes between orders and Maxeene the draft horse listens at the hitching posts. ..."
> — `campaign/setting/organizations/01-harpers.md:36` (the full sentence is quoted here; the paragraph continues with the wiki's habit of informants)

> "Remi sends messages to her spies by a silver raven figurine, Variel's stories carry reports, Corvin passes folded notes, Maxeene listens at hitching posts and Mattrim watches the Zhentarim agents who drink at the Yawning Portal."
> — `campaign/setting/organizations/01-harpers.md:74` (Gathering information)

> "**Fronts and covers:** ... and Corvin and Nessa Vayle are servers who come as a pair. Maxeene is hired out by the day from a stand off Fillet Lane."
> — `campaign/setting/organizations/01-harpers.md:62` (the paragraph begins "Most Harper agents live a double life (Forgotten Realms Wiki, *Harpers*, edition not stated).")

### A4. Trade and skills (day-one, from the Persona and the appendix)
> "To the world, the Vayle twins are inseparable servers who learned to work together by arguing about everything and are excellent at the job. To those who hire both, Corvin is the one who sometimes passes a folded note to a specific regular."
> — `campaign/setting/notable-figures/harpers/07-corvin-vayle.md:21`

> "They are good — faster together than most single servers are alone, with a near-wordless shorthand built from a lifetime of twin coordination."
> — `sources/Appendix_D_-_Running_the_Tavern.md:296`

> "Together they count as two full servers running at exceptional coordination."
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58`

### A5. Relationships (named figures)
- **Nessa (twin).** See A1 (`07-corvin-vayle.md:25`; `08-nessa-vayle.md:25`).
- **Mirt.** "Mirt knows the Vayles; this is not accidental." (`sources/Appendix_D_-_Running_the_Tavern.md:296`). "Mirt's network has already accounted for their placement." (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:58`).
- **Trollskull Manor.** "Trollskull Manor server candidates detailed in the **Trollskull Manor** guide" (`07-corvin-vayle.md:25`). Row 5 of the staff table is at `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58`, under the header at `:50`: "**Server Candidates (5 gp/tenday standard; hire two)**". The Vayles are the only pair in that table and the wage is "10 gp (both)".
- **Harpers.** Key Members at `campaign/setting/organizations/01-harpers.md:104`. The Harpers' stance on the Vayles is not given in any Harper source beyond the Key Members line.

### A6. Faith
Not stated in any source.

### A7. Signature belongings
Not stated in any source. The voice profile gives a gesture: "Corvin taps the tray twice when he has a note for someone." (`.claude/skills/character-voices/voices/harpers.md:127`).

### A8. Habits and manner
> "Corvin goes suddenly specific and quiet when he's passing a message." — `.claude/skills/character-voices/voices/harpers.md:126`

> "Asking him about it directly prompts him to confirm, with some relief, that he does "some courier work"" — `sources/Appendix_D_-_Running_the_Tavern.md:298` (quoted in A3)

> "Nessa speaks; Corvin is silent and scanning." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58`

> "Corvin, the quieter one," — `sources/Appendix_D_-_Running_the_Tavern.md:296`

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Page: "*Illuskan human twin, chaotic neutral, he/him*. Stat block: **Commoner**." — `campaign/setting/notable-figures/harpers/07-corvin-vayle.md:5`
- Appendix D: "*CN female/male humans, Commoner. They come as a pair. One is a Harper courier.*" — `sources/Appendix_D_-_Running_the_Tavern.md:290`
- Trollskull guide: "CN Illuskan human twins" — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58`
- Organization page: "Illuskan human twin" — `campaign/setting/organizations/01-harpers.md:104`
- Consistent. Chaotic neutral in all four.

**Species**
- Page: "Illuskan human" (L5).
- Organization page: "Illuskan human twin" (`01-harpers.md:104`).
- Trollskull guide: "Illuskan human twins" (`03-staff-and-hiring.md:58`).
- Appendix D: "humans" only (`Appendix_D:290`). No ethnicity given. The Illuskan tag comes from the campaign, so it is the campaign's word.

**Pronouns**
- Page: "he/him" (`07-corvin-vayle.md:5`).
- Appendix D: "the man" and "he says simply" (`Appendix_D:293`): "\"We're good,\" he says simply."
- Consistent.

**Stat block**
- Page: "Stat block: **Commoner**." (`07-corvin-vayle.md:5`)
- Appendix D: "Commoner" (`Appendix_D:290`).
- Consistent.

---

## C. Sentences on the current page that narrate quest time or depend on a condition

The page is Ches 1. Each row gives the status and where the fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L5 | "*Illuskan human twin, chaotic neutral, he/him*. Stat block: **Commoner**." | Day-one (section B) | `sources/Appendix_D_-_Running_the_Tavern.md:290` |
| 2 | L6 | "- **Affiliation:** Harpers (covertly)" | Day-one label. "covertly" is the page's own word; the org page does not say it | `campaign/setting/organizations/01-harpers.md:104`; `01-harpers.md:62` ("Most Harper agents live a double life") |
| 3 | L7 | "- **Featured in:** Background figure; no scripted appearance." | Day-one. No quest file names Corvin (Grep). The Trollskull guide lists the Vayles as hire candidates, which is not a scene | `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58` |
| 4 | L11 | "**Resonance.** The Vayles should inspire amusement with their sibling dynamic (they bicker constantly but function as a single efficient unit); and useful surprise when Corvin's courier role makes the tavern a minor Harper waypoint." | The sibling part is day-one. "makes the tavern a minor Harper waypoint" depends on the party hiring them (Appendix D:300). Keep verbatim (ruling 3); flag for the drafter | `sources/Appendix_D_-_Running_the_Tavern.md:296`, `:300` |
| 5 | L13 | "**Emotions.** The Vayles most often feel competitive affection for each other, casual professionalism, and Corvin's private focus when a message needs to pass." | Day-one. Keep | `.claude/skills/character-voices/voices/harpers.md:126` |
| 6 | L15 | "**Motivations.** The Vayles want to work somewhere interesting enough to stay at, maintain the arrangement that lets them operate as a unit, and pass whatever Corvin needs to pass without Nessa having to know about it." | Day-one. Keep. The "work somewhere" wish matches F1: they do not have a day-one employer in any source | Section F1 |
| 7 | L17 | "**Inspirations.** When playing the Vayles, channel Fred and George Weasley (*Harry Potter*), Tweedledee and Tweedledum (*Alice in Wonderland*, if they ran a pub with military efficiency), and Chang and Eng Bunker (the linked-pair metaphor)." | Not a fact. Keep | n/a |
| 8 | L21 | "**Persona.** To the world, the Vayle twins are inseparable servers who learned to work together by arguing about everything and are excellent at the job. To those who hire both, Corvin is the one who sometimes passes a folded note to a specific regular." | Day-one. "To those who hire both" is a world-facing statement and is fine | `sources/Appendix_D_-_Running_the_Tavern.md:293`, `:296` |
| 9 | L23 | "**Morale.** In a fight, the Vayles grab each other and run. They are not paid enough for that." | Encounter behaviour, day-one. Keep | n/a |
| 10 | L25 | "**Relationships.** Corvin and Nessa Vayle are a package hire for the tavern staff, a minor Harper waypoint through Corvin's courier role, and Trollskull Manor server candidates detailed in the **Trollskull Manor** guide. His twin sister is **Nessa Vayle**." | "a minor Harper waypoint" is conditional (see row 4). "server candidates" is day-one (the candidate pool). Nothing else is quest time | `campaign/guides/trollskull-manor/03-staff-and-hiring.md:50`, `:58` |
| 11 | L27-29 | "## Overview" / "Inseparable twins who work as servers, bicker about everything, and function as a single efficient unit without ever having formally agreed to do so." | Day-one. **24 words** (brief limit 21). Draft a shorter Overview | `sources/Appendix_D_-_Running_the_Tavern.md:293` |

**Voice profile (`.claude/skills/character-voices/voices/harpers.md`, "### Corvin Vayle", L119-133)**
- L120 tagline: "*Twin server who argues about everything and finishes his sister's work, if not her sentences.*" Day-one.
- L122 Sound: "A quick, bright voice, nearly identical to his twin's and always slightly overlapping hers. Corvin is a touch lower and slower. Nessa is louder." Day-one.
- L124 Word choice, L125 Swearing ("Punctuation · Colourful · Rant." with "piss off" and "you absolute shit"), L126 Personality in speech, L127 Quirks, L128 Signature phrases, L129 Never. All day-one. The Swearing line stays (adult table).
- L126: "Corvin goes suddenly specific and quiet when he's passing a message." Day-one habit.
- L132 Business sample: "Corvin: \"The gentleman by the window left this for you. Said you'd know what it's about.\"" Judgment flag. The line is a generic example, but "left this for you" speaks to a party member as a message recipient, which is the Harper-courier situation. The drafter decides whether it stays. Nothing in the campaign names a note left for a PC by the Vayles.
- L131 Greeting: "Nessa: \"Table for four?\" Corvin: \"Five, she can't count.\" Nessa: \"Five. Piss off, Corvin.\"" Day-one.
- L133 Under pressure: "Nessa: \"Right, we're leaving.\" Corvin: \"We are definitely leaving.\"" Day-one.

**Routed to quests:** none of the page's sentences narrates a quest event. No quest file in `campaign/quests/` names Corvin or Nessa Vayle (Grep, case-insensitive). The Harpers quests that mention a courier or a clerk name other people (`s01-the-cell-is-compromised`, `m04-a-friends-house`).

---

## D. Conflicts

**D1. Whether the Vayles are in the Harpers' principal list**
- Organization page, Key Members: "- **Corvin Vayle** — Illuskan human twin; runs a minor Harper waypoint through a courier role. See the **Corvin Vayle** page in Notable Figures." — `campaign/setting/organizations/01-harpers.md:104`
- Organization page, cross-references: "- **Mirt**, **Remallia "Remi" Haventree**, **Mattrim "Threestrings" Mereg**, **Corene Wyldath**, **Variel Duskwhisper**, **Maxeene** (Notable Figures): the principal Harpers" — `01-harpers.md:161` (Corvin is not named)
- Factions Guide, cross-references: "- Notable Figures: **Mirt**, **Remallia "Remi" Haventree**, **Mattrim "Threestrings" Mereg**, **Bonnie**, **Corene Wyldath**, **Variel Duskwhisper**, **Corvin Vayle**, **Nessa Vayle**, **Maxeene**" — `campaign/guides/factions/02-harpers.md:82`
- Higher rank: the org page's Key Members list (campaign) puts him in the Harpers. The cross-reference list at `01-harpers.md:161` leaves him out. The drafter should not write him as "principal".

**D2. "Minor Harper waypoint": present tense or conditional**
- Present tense: "runs a minor Harper waypoint through a courier role" (`campaign/setting/organizations/01-harpers.md:104`); "a minor Harper waypoint through Corvin's courier role" (`07-corvin-vayle.md:25`).
- Conditional: "the tavern will become, de facto, a minor Harper waypoint" (`sources/Appendix_D_-_Running_the_Tavern.md:296`); "If Harper-affiliated characters hire them, Mirt considers the tavern a confirmed waypoint" (`Appendix_D:300`); "Tavern becomes a minor Harper waypoint" under the Faction Note, with "Corvin passes one piece of Harper network intelligence/tenday if party is Harper-affiliated or asks" (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:58`).
- Higher rank: campaign (the org page and the guide). The guide's own Effect column is conditional. The Appendix is the older source. The drafter should say the waypoint depends on the party's hiring and not treat it as a fixed fact.

**D3. What Corvin passes to the party**
- Trollskull guide (campaign): "Corvin passes one piece of Harper network intelligence/tenday if party is Harper-affiliated or asks." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58`
- Appendix D (Alexandrian): "If the characters are Harper-affiliated, this connection unlocks a minor information channel — Corvin can carry messages for them at no cost and will occasionally bring back relevant street intelligence." — `sources/Appendix_D_-_Running_the_Tavern.md:306`
- Higher rank: campaign (guide). "One piece per tenday" is a mechanic and does not belong in a Background. The Factions Guide gives the same "one piece ... per tenday" mechanic for Variel, not for Corvin (see `campaign/setting/organizations/01-harpers.md:103`).

**D4. Name collisions (not this figure)**
- `sources/Act_III_Arc_E.md:89`: "| G2 — Yard | **Corvin** (Servant/Gardener) |"
- `sources/Act_III_Arc_E.md:129`: "**Corvin**, a weathered older human in a broad canvas hat, is at work near the oaks pulling weeds by hand. He is incurious about visitors as long as they seem to have legitimate business. **Hurv Taldred**, the groundskeeper, is sleeping in the coach house."
- `campaign/gazetteer/waterdeep/trades-ward.md:259`: "Corvin Hallowell is not the Harper Corvin Vayle, whose page exists."
- Campaign files do not name the Gralhund gardener (Grep). The Gralhund gardener is from the Alexandrian remix only. The Vayle is "young" (`Appendix_D:293`).

**D5. Nessa's affiliation** (the twin's label, which affects how Corvin's cover reads)
- "Affiliation: Unaffiliated" — `campaign/setting/notable-figures/harpers/08-nessa-vayle.md:6`. See the Nessa notes.

**D6. Waypoint and the day-one employer.** Appendix D says the tavern "will become" a waypoint only once the Vayles work there (`Appendix_D:296`). The guide says they are candidates (`03-staff-and-hiring.md:50`). The page says "server candidates". No source says where they work on Ches 1. See F1.

---

## E. Stale lines in other files (do not edit) and routed references

**E1. Stale or conflicting lines in other files**
- `docs/plans/setting-compendium-research-notes/pass5/harpers.md:226` quotes the org page as "- **Corvin Vayle** — ..." and cites `01-harpers.md:32`. Current line: `01-harpers.md:104`. The pass5 notes are stale on every org-page line number.
- `docs/plans/setting-compendium-pass3-closeout.md:64`: "Corvin Hallowell (Davil's Arrest) is not the Harper Corvin Nessa Vayle." Name typo ("Corvin Nessa Vayle"). The campaign line is `trades-ward.md:259`: "Corvin Vayle".
- `docs/plans/faerun-ethnicities-research.md:422` repeats the same typo.
- `docs/plans/npc-pronouns-table-group-b.md:35` names "harpers/07-corvin-nessa-vayle.md". The current file is `07-corvin-vayle.md` (the twins have one page each; see `docs/plans/npc-pronouns-table.md:61`).
- `campaign/setting/organizations/01-harpers.md:181` is the org page's own Draft Notes, which says both twins "stay under Key Members" (quoted in the Nessa notes).

**E2. Routed references (quest time, not day-one)**
- None for Corvin's own sentences. The quest files that name the Harpers' cell (`campaign/quests/faction-events/harpers/s01-the-cell-is-compromised/ev-01-the-cell-is-compromised.md:11`) concern the courier and the register, not Corvin. Do not cite them as a Corvin fact.

**E3. Trollskull hire, quest time**
- `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:159`: "Trollskull Manor opened to the public after twelve days of renovation. Staff was hired, three Undermountain threads were seeded at the party, Ammalia Cassalanter attended as a warm and generous first patron with her young twins, and Lif — if appeased — was behind the bar without being asked." The Vayles are not named here. The hire is a quest event (see F1).

---

## F. Gaps a Background needs that no source gives

**F1. Where he works on Ches 1, and whether he is employed.** No source. What the sources say: the Trollskull Manor is abandoned at the start. "In Chapter 2 of the *Dragon Heist* campaign, the PCs are rewarded with the deed to an abandoned inn named Trollskull Manor." (`sources/27. Addendum A Night in Trollskull Manor.pdf`, PDF p.1, printed p.178; transcription). The Vayles are "server candidates" (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:50`, `:58`). The Persona calls them "servers" (`07-corvin-vayle.md:21`). Keep the Background consistent with both: a pair who have worked bars together and are looking for a place to work. Do not write an employer. `[research]` if the drafter names a Ches 1 employer.

**F2. Birth year, birth name, home, parents, family.** No source. Only "people who grew up in a city" (`Appendix_D:293`). Do not name a parent or relative (brief ruling 17: a nameless relative or place is allowed).

**F3. How he came to the courier role, and who recruited him.** No source. Only "Mirt knows the Vayles" (`Appendix_D:296`). The Background can say Mirt's network knew of them without naming who recruited Corvin. `[design]` if invented.

**F4. Personal wants that belong to Corvin alone.** The sources give only shared wants: "The Vayles want to work somewhere interesting enough to stay at, maintain the arrangement that lets them operate as a unit, and pass whatever Corvin needs to pass without Nessa having to know about it." (`07-corvin-vayle.md:15`). The one personal want in a source is the rent: "we need the combined wage to afford rent in the North Ward" (`Appendix_D:293`), which is shared. Any individual goal is `[design]`.

**F5. Faith, fears, losses, a person he cares about.** None in any source.

**F6. Affiliation before he joined the Harpers.** None.

**F7. Whether Nessa knows what Corvin does.** The sources say she does not ask: "To those who ask Nessa about it, she asked once, his answer was satisfactory, and she stopped asking." (`08-nessa-vayle.md:21`). Emotions and Motivations say the same. The Harpers page lists her as a cover (`01-harpers.md:62`). See the Nessa notes, D1.

---

## G. Source facts that hint at the figure's inner life (do not contradict)

- "Corvin's private focus when a message needs to pass." — `campaign/setting/notable-figures/harpers/07-corvin-vayle.md:13`
- "Corvin goes suddenly specific and quiet when he's passing a message." — `.claude/skills/character-voices/voices/harpers.md:126`
- "Asking him about it directly prompts him to confirm, with some relief, that he does \"some courier work\"" — `sources/Appendix_D_-_Running_the_Tavern.md:298`
- "the particular watchfulness of people who grew up in a city and learned early to pay attention." — `sources/Appendix_D_-_Running_the_Tavern.md:293`
- "We've been working bars in pairs since we were sixteen" — `sources/Appendix_D_-_Running_the_Tavern.md:293`
- "They are not paid enough for that." — `campaign/setting/notable-figures/harpers/07-corvin-vayle.md:23`
- "Corvin is a Harper courier (not a field agent)." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58` (the courier is a trusted carrier, not a spy; a Background must not make him an agent)
- Corvin "is the quieter one" and "looks around the room" (`Appendix_D:293`, `:296`).
- The Morale line: "In a fight, the Vayles grab each other and run." (`07-corvin-vayle.md:23`)

---

## Not found

- Corvin's birth year, home, parents, family name, age beyond "young", date of joining the Harpers, recruiter, faith, signature belongings, losses, fears, personal goals. Searched: `campaign/` (Grep "vayle|corvin|nessa", case-insensitive), `sources/adventure-wdh.json` (no hit), `sources/*.md` (Grep), `sources/research/` (Grep), `sources/SOURCE_GUIDE.md` (no Vayle or Corvin hit), root session handoffs (Grep, no biographical fact), `docs/plans/` (Grep, planning notes only).
- Published adventure: "vayle", "corvin" and "nessa" do not appear in `sources/adventure-wdh.json`. Maxeene is the only Harper NPC of this group in the adventure (see the Maxeene notes).
- Alexandrian PDF `27. Addendum A Night in Trollskull Manor.pdf`, PDF pp.4-5 (staffing) read: no Vayle. PDF pp.21-38 not read (patron profiles).
- Alexandrian PDF `3. Player Character Factions.pdf`, pp.1-3 read: no Vayle.
- Wiki: NOT FOUND; no pass5 bundle hit.
- Session 37 and Session 52 handoffs: no Corvin fact. Session 51 handoff line 41 records the split into two pages.

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. `sources/SOURCE_GUIDE.md:695` lists "The Waterdavian's Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place...).docx" as "Broad NPC reference", and `docs/plans/harpers-research/03-m01-m03.md:7` says it "is the only one likely to hold Maxeene, Mattrim or Bonnie material". Not checked for Corvin or Nessa. `sources/SOURCE_GUIDE.md:691` lists "Lif and the Haunting of Trollskull Manor.docx" for "tavern integration" and the Trollskull Manor guide. Not checked for the Vayles.
- `sources/27. Addendum A Night in Trollskull Manor.pdf`, PDF pp.21-38: read not attempted (see Not found).
