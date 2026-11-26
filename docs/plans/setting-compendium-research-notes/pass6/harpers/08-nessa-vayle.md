# Pass 6 research notes: Nessa Vayle

Page: `campaign/setting/notable-figures/harpers/08-nessa-vayle.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR. Nessa is a minor figure (brief ruling 2): the short Personality and Connections apply. She still needs a Background (ruling 15) and a `### Voice` block (ruling 16).
User ruling (brief line 74, "Key Members labels"): "Keep and note the tie." Nessa stays on the Harpers' Key Members list. Her own page keeps "Unaffiliated". The caller's message cited `organizations/01-harpers.md:101` for this ruling. Line 101 is Bonnie's bullet. Nessa's bullet is line 105 (see D1).
Organization page: `campaign/setting/organizations/01-harpers.md`
Factions Guide: `campaign/guides/factions/02-harpers.md`
Voice profile: `.claude/skills/character-voices/voices/harpers.md` ("### Nessa Vayle", lines 137-151)
Wiki: NOT FOUND. The extract `scratchpad/wiki-harpers/08-nessa-vayle.txt` reads "NOT FOUND". No wiki page for her. Nothing in `sources/research/pass5-bundles/harpers/wiki.txt` names her (Grep, case-insensitive "vayle|corvin|maxeene|nessa").

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json` has no Vayle, no Corvin and no Nessa (Grep, case-insensitive).
- Alexandrian Appendix D: `sources/Appendix_D_-_Running_the_Tavern.md`, lines 289-306 (Candidate 5). Quotes are copied from the Read output. Lines 292-294 sit in a `<div class="fvtt narrative">` block; the paragraph text is quoted as written.
- Alexandrian PDF `sources/27. Addendum A Night in Trollskull Manor.pdf`: PDF pp.1-20 read as page images (printed pp.178-191). The staffing pages (PDF pp.4-5, printed pp.182-183) do not name the Vayles. PDF pp.21-38 were not read. Quotes from the PDF are transcriptions; check them with `pdftotext -layout` before use.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **Her affiliation is the open conflict.** Her own page says "Unaffiliated" (`campaign/setting/notable-figures/harpers/08-nessa-vayle.md:6`). The Harpers page puts her in the same "Fronts and covers" paragraph as the Harper covers (`campaign/setting/organizations/01-harpers.md:62`). The org page lists her under Key Members (`01-harpers.md:105`). Its own Draft Notes flag the label (`01-harpers.md:181`). The user ruling keeps her in Key Members with the looser tie. Write her Connections as "Unaffiliated", with her brother's Harper work and the org page's "who knows not to ask" as the tie. Section D1.
2. **Citation error in the ruling.** Brief line 74 and the caller's message cite `01-harpers.md:101` for Nessa. Line 101 is Bonnie's bullet ("- **Bonnie** — Doppelganger; leader of a five-doppelganger operation at the Yawning Portal, independent of the Harpers."). Nessa's bullet is at `01-harpers.md:105`.
3. **The Overview is 24 words, over the 21-word limit** (L29). The same sentence is on Corvin's page. See C row 11.
4. **No source gives Nessa a day-one job** (section F1). The Trollskull guide and Appendix D present the twins as hire candidates. The tavern opens only after renovation (`campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:159`).
5. **Name collision.** The Doom Raiders' assassin in the Ardragon event is Nessa Thorne (`campaign/quests/faction-events/doom-raiders/r25-ardragon/ev-01-ardragon.md:137`). She is not this figure. Section D4.

---

## A. Background facts by theme

### A1. Origin, family and age
No source gives a birth year, a home district, parents, or a family name. The sourced facts are below.

**Twin, with Corvin (Persona, Relationships; the org page; the Trollskull appendix)**
> "Corvin and Nessa Vayle are a package hire for the tavern staff, a minor Harper waypoint through Corvin's courier role, and Trollskull Manor server candidates detailed in the **Trollskull Manor** guide. Her twin brother is **Corvin Vayle**."
> — `campaign/setting/notable-figures/harpers/08-nessa-vayle.md:25`

> "- **Nessa Vayle** — Illuskan human twin; Corvin's sister, who knows not to ask. See the **Nessa Vayle** page in Notable Figures."
> — `campaign/setting/organizations/01-harpers.md:105` (Key Members)

> "*CN female/male humans, Commoner. They come as a pair. One is a Harper courier.*"
> — `sources/Appendix_D_-_Running_the_Tavern.md:290` (heading at `:289`: "**Candidate 5 — the Twins: Nessa and Corvin Vayle**")

**Age, upbringing, and the years working bars (Appendix D narrative, the interview)**
> "They arrive together — a young woman and a young man, identical in height, both with sharp cheekbones and the particular watchfulness of people who grew up in a city and learned early to pay attention. The woman speaks; the man looks around the room. "We're a package," she says. "Nessa and Corvin Vayle. We've been working bars in pairs since we were sixteen — one takes the floor, one handles the back and the cellar. We don't work apart. We work cheap because we work fast and because frankly we need the combined wage to afford rent in the North Ward." The man glances back. "We're good," he says simply."
> — `sources/Appendix_D_-_Running_the_Tavern.md:293`

Nessa is "the woman" in that passage. Her line, "we need the combined wage to afford rent in the North Ward", is the only money fact in any source about the pair.

**Role on the floor (campaign guide, the staff table)**
The full row (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:58`): "| 5 | **Nessa & Corvin Vayle** | CN Illuskan human twins | Arrive together. Nessa speaks; Corvin is silent and scanning. \"We're a package. Nessa handles front of house; I handle the room.\" DC 14 Insight detects Corvin's attention to the room is more systematic than curiosity — cataloguing, not curious. Together they count as two full servers running at exceptional coordination. | Corvin is a Harper courier (not a field agent). Tavern becomes a minor Harper waypoint. Mirt's network has already accounted for their placement. | 10 gp (both) | +2 Revenue. Corvin passes one piece of Harper network intelligence/tenday if party is Harper-affiliated or asks. Combination with Kassia: +5 additional Revenue on any tenday all three work full shifts. |"

The appendix does not assign roles inside the pair: "one takes the floor, one handles the back and the cellar" (`Appendix_D:293`). The guide does: "Nessa handles front of house" (`03-staff-and-hiring.md:58`). Campaign ranks higher.

### A2. Trade and skills
> "They are good — faster together than most single servers are alone, with a near-wordless shorthand built from a lifetime of twin coordination." — `sources/Appendix_D_-_Running_the_Tavern.md:296`

> "To the world, the Vayle twins are inseparable servers who learned to work together by arguing about everything and are excellent at the job." — `campaign/setting/notable-figures/harpers/08-nessa-vayle.md:21`

> "Together they count as two full servers running at exceptional coordination." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58`

### A3. How she came to the pair's work, and the Harper tie
No source gives her own Harper history or a recruiter. What the sources give:

> "We're a package," she says. "Nessa and Corvin Vayle." — `sources/Appendix_D_-_Running_the_Tavern.md:293` (the pair's introduction; the passage says nothing about a Harper role for Nessa)

> "Corvin, the quieter one, is also a part-time courier for the Harpers — not an agent, just a trusted carrier who moves messages between contacts." — `sources/Appendix_D_-_Running_the_Tavern.md:296` (this is about Corvin only)

> "Asking him about it directly prompts him to confirm, with some relief, that he does "some courier work" and that it "occasionally overlaps with his social life." He will not name the Harpers unless the characters already have Harper connections." — `sources/Appendix_D_-_Running_the_Tavern.md:298` (about Corvin only)

> "Remi is the gracious lady of House Ulbrinter, Mirt is a moneylender, Mattrim Mereg is a middling bard at the Yawning Portal, Variel Duskwhisper is a touring musician, and Corvin and Nessa Vayle are servers who come as a pair." — `campaign/setting/organizations/01-harpers.md:62` (the paragraph "**Fronts and covers:**" opens "Most Harper agents live a double life (Forgotten Realms Wiki, *Harpers*, edition not stated).")

### A4. Relationships (named figures)
- **Corvin (twin brother).** See A1. "Her twin brother is **Corvin Vayle**." (`08-nessa-vayle.md:25`)
- **Mirt.** "Mirt knows the Vayles; this is not accidental." (`sources/Appendix_D_-_Running_the_Tavern.md:296`). "Mirt's network has already accounted for their placement." (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:58`). The Mirt link is shared with Corvin.
- **Harpers (org page).** "Corvin's sister, who knows not to ask." (`campaign/setting/organizations/01-harpers.md:105`). The org page never states that Nessa knows the Harpers. "Knows not to ask" is the only Harper-facing fact about her in a source.
- **Trollskull Manor.** "Trollskull Manor server candidates detailed in the **Trollskull Manor** guide" (`08-nessa-vayle.md:25`). The guide row is at `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58`.

### A5. Faith
Not stated in any source.

### A6. Signature belongings
Not stated in any source.

### A7. Habits and manner
> "Nessa's practiced incuriosity about what Corvin sometimes does." — `campaign/setting/notable-figures/harpers/08-nessa-vayle.md:13`

> "To those who ask Nessa about it, she asked once, his answer was satisfactory, and she stopped asking." — `campaign/setting/notable-figures/harpers/08-nessa-vayle.md:21`

> "Nessa's incuriosity is loud and deliberate (\"Not asking. Don't care.\")." — `.claude/skills/character-voices/voices/harpers.md:144`

> "Nessa is louder." — `.claude/skills/character-voices/voices/harpers.md:140`

> "Nessa speaks; Corvin is silent and scanning." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58`

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Page: "*Illuskan human twin, chaotic neutral, she/her*. Stat block: **Commoner**." — `campaign/setting/notable-figures/harpers/08-nessa-vayle.md:5`
- Appendix D: "*CN female/male humans, Commoner. They come as a pair. One is a Harper courier.*" — `sources/Appendix_D_-_Running_the_Tavern.md:290`
- Trollskull guide: "CN Illuskan human twins" — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58`
- Organization page: "Illuskan human twin" — `campaign/setting/organizations/01-harpers.md:105`
- Consistent. Chaotic neutral in all four.

**Species**
- Page: "Illuskan human" (L5).
- Organization page: "Illuskan human twin" (`01-harpers.md:105`).
- Trollskull guide: "Illuskan human twins" (`03-staff-and-hiring.md:58`).
- Appendix D: "humans" only (`Appendix_D:290`). No ethnicity given.

**Pronouns**
- Page: "she/her" (`08-nessa-vayle.md:5`).
- Appendix D: "The woman speaks" and "she says" (`Appendix_D:293`): "\"We're a package,\" she says."
- Consistent.

**Stat block**
- Page: "Stat block: **Commoner**." (`08-nessa-vayle.md:5`)
- Appendix D: "Commoner" (`Appendix_D:290`).
- Consistent.

---

## C. Sentences on the current page that narrate quest time or depend on a condition

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L5 | "*Illuskan human twin, chaotic neutral, she/her*. Stat block: **Commoner**." | Day-one (section B) | `sources/Appendix_D_-_Running_the_Tavern.md:290` |
| 2 | L6 | "- **Affiliation:** Unaffiliated" | Day-one. Conflicts with the org page's Key Members list and the Harpers page's "servers who come as a pair" line. Kept by the user ruling (brief line 74). See D1 | `campaign/setting/organizations/01-harpers.md:105`, `:62`, `:181` |
| 3 | L7 | "- **Featured in:** Background figure; no scripted appearance." | Day-one. No quest file names Nessa (Grep). The Trollskull guide lists the twins as hire candidates, which is not a scene | `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58` |
| 4 | L11 | "**Resonance.** The Vayles should inspire amusement with their sibling dynamic (they bicker constantly but function as a single efficient unit)." | Day-one. Keep. The same sibling dynamic is in the Appendix's "They are good" passage | `sources/Appendix_D_-_Running_the_Tavern.md:296` |
| 5 | L13 | "**Emotions.** The Vayles most often feel competitive affection for each other, casual professionalism, and Nessa's practiced incuriosity about what Corvin sometimes does." | Day-one. Keep | `.claude/skills/character-voices/voices/harpers.md:144` (the voice profile's "Not asking") |
| 6 | L15 | "**Motivations.** The Vayles want to work somewhere interesting enough to stay at, maintain the arrangement that lets them operate as a unit, and pass whatever Corvin needs to pass without Nessa having to know about it." | Day-one. Keep. "work somewhere" matches F1 | Section F1 |
| 7 | L17 | "**Inspirations.** When playing the Vayles, channel Fred and George Weasley (*Harry Potter*), Tweedledee and Tweedledum (*Alice in Wonderland*, if they ran a pub with military efficiency), and Chang and Eng Bunker (the linked-pair metaphor)." | Not a fact. Keep | n/a |
| 8 | L21 | "**Persona.** To the world, the Vayle twins are inseparable servers who learned to work together by arguing about everything and are excellent at the job. To those who hire both, Corvin is the one who sometimes passes a folded note to a specific regular. To those who ask Nessa about it, she asked once, his answer was satisfactory, and she stopped asking." | Day-one. "To those who hire both" is world-facing and fine. The Corvin sentence is sourced to the org page's "Corvin Vayle passes folded notes between orders" (`01-harpers.md:36`) | `sources/Appendix_D_-_Running_the_Tavern.md:293`; `campaign/setting/organizations/01-harpers.md:36` |
| 9 | L23 | "**Morale.** In a fight, the Vayles grab each other and run. They are not paid enough for that." | Encounter behaviour, day-one. Keep. No other source describes it | Page only |
| 10 | L25 | "**Relationships.** Corvin and Nessa Vayle are a package hire for the tavern staff, a minor Harper waypoint through Corvin's courier role, and Trollskull Manor server candidates detailed in the **Trollskull Manor** guide. Her twin brother is **Corvin Vayle**." | "a minor Harper waypoint through Corvin's courier role" is conditional on the party's hiring (Appendix D:300) and is about Corvin's role, not Nessa's. Keep verbatim (ruling 3), flag. "server candidates" is day-one | `sources/Appendix_D_-_Running_the_Tavern.md:300`; `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58` |
| 11 | L27-29 | "## Overview" / "Inseparable twins who work as servers, bicker about everything, and function as a single efficient unit without ever having formally agreed to do so." | Day-one. **24 words** (brief limit 21). Draft a shorter Overview | `sources/Appendix_D_-_Running_the_Tavern.md:293` |

**Voice profile (`.claude/skills/character-voices/voices/harpers.md`, "### Nessa Vayle", L137-151)**
- L138 tagline: "*Twin server who argues about everything and finishes her brother's work, if not his sentences.*" Day-one.
- L140 Sound: "A quick, bright voice, nearly identical to her twin's and always slightly overlapping his. Corvin is a touch lower and slower. Nessa is louder." Day-one.
- L141 Sentence shape, L142 Word choice, L143 Swearing ("*Punctuation · Colourful · Rant.*", "piss off", "you absolute shit"), L144 Personality in speech, L145 Quirks, L146 Signature phrases, L147 Never. All day-one. The Swearing line stays (adult table).
- L144: "Nessa's incuriosity is loud and deliberate (\"Not asking. Don't care.\")." Day-one habit.
- L150 Business sample: "Corvin: \"The gentleman by the window left this for you. Said you'd know what it's about.\"" The sample is spoken by Corvin, not Nessa. Judgment flag, the same as the Corvin file (L132).
- L149 Greeting: "Nessa: \"Table for four?\" Corvin: \"Five, she can't count.\" Nessa: \"Five. Piss off, Corvin.\"" Day-one.
- L151 Under pressure: "Nessa: \"Right, we're leaving.\" Corvin: \"We are definitely leaving.\"" Day-one.

**Routed to quests:** none. No quest file names Nessa Vayle (Grep, case-insensitive). The Doom Raiders' Nessa Thorne is a different person (D4).

---

## D. Conflicts

**D1. Nessa's affiliation (the open conflict)**

Her own page:
- "> - **Affiliation:** Unaffiliated" — `campaign/setting/notable-figures/harpers/08-nessa-vayle.md:6`

The Harpers organization page, Key Members:
- "- **Nessa Vayle** — Illuskan human twin; Corvin's sister, who knows not to ask. See the **Nessa Vayle** page in Notable Figures." — `campaign/setting/organizations/01-harpers.md:105`

The Harpers organization page, "Fronts and covers" paragraph, which lists the twins with the Harper agents. The sentence in full: "Remi is the gracious lady of House Ulbrinter, Mirt is a moneylender, Mattrim Mereg is a middling bard at the Yawning Portal, Variel Duskwhisper is a touring musician, and Corvin and Nessa Vayle are servers who come as a pair." — `campaign/setting/organizations/01-harpers.md:62`. The paragraph opens "Most Harper agents live a double life (Forgotten Realms Wiki, *Harpers*, edition not stated)."

The Harpers organization page, cross-references (the twins are missing from the list of "the principal Harpers"):
- "- **Mirt**, **Remallia "Remi" Haventree**, **Mattrim "Threestrings" Mereg**, **Corene Wyldath**, **Variel Duskwhisper**, **Maxeene** (Notable Figures): the principal Harpers" — `campaign/setting/organizations/01-harpers.md:161`

The Harpers organization page's own Draft Notes:
- "> - **Conflicts:** Affiliation labels. `04-bonnie.md:6` reads \"Independent (potential Harper operative)\" and `08-nessa-vayle.md:6` reads \"Unaffiliated\", yet both stay under Key Members. The Bonnie bullet now says she is independent of the Harpers." — `campaign/setting/organizations/01-harpers.md:181`

The user ruling (Session 53) in the brief:
- "- **Key Members labels.** \"Keep and note the tie.\" Zelifarn, Bonnie and Nessa Vayle stay on the organization pages, which already note the looser tie (`07-bregan-daerthe.md:103`, `01-harpers.md:101` and `:105`). Their figure pages keep their own labels." — `docs/plans/setting-compendium-pass6-brief.md:74`. Line 101 in the org page is Bonnie's bullet; the Nessa bullet is `:105`.

The earlier handoff (Session 52):
- "- [ ] **Key Members labels:** Zelifarn (`07-bregan-daerthe.md`; his page says \"None (friendly to Bregan D'aerthe; not an operative)\"), Bonnie and Nessa Vayle (`01-harpers.md`; their pages say \"Independent\" and \"Unaffiliated\"). Recommendation: keep as listed." — `session 52 handoff.md:105`

Higher rank: the org page's Key Members list and the user ruling keep her in Key Members. Her own page keeps "Unaffiliated". The Harpers page's "servers who come as a pair" line does not say she is a Harper agent, but it places her among the covers. The drafter must choose one reading and write it in Connections. The Background should not state a Harper role for her.

**D2. Who gives the floor and the back**
- Campaign guide: "Nessa handles front of house; I handle the room." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58`
- Appendix D (Alexandrian, lower rank): "one takes the floor, one handles the back and the cellar." — `sources/Appendix_D_-_Running_the_Tavern.md:293` (no name assigned)
- Higher rank: campaign (the guide). Not a true conflict: the appendix does not name who takes which role.

**D3. "Minor Harper waypoint": present tense or conditional** (applies to Nessa's Relationships line)
- Present tense: "runs a minor Harper waypoint through a courier role" (`campaign/setting/organizations/01-harpers.md:104`, which is Corvin's line).
- Conditional: "If Harper-affiliated characters hire them, Mirt considers the tavern a confirmed waypoint" (`sources/Appendix_D_-_Running_the_Tavern.md:300`).
- Higher rank: campaign (the org page and the guide). The guide's Effect column is conditional. The drafter should write it as conditional.

**D4. Name collision (not this figure)**
- `campaign/quests/faction-events/doom-raiders/r25-ardragon/ev-01-ardragon.md:137`: "Crew Two is the assassin Nessa Thorne (she/her) and the spies Garrick Pell and Bree Ostler."
- `campaign/quests/faction-events/doom-raiders/r25-ardragon/ev-01-ardragon.md:158`: "If Crew Two comes, the assassin is Nessa Thorne and says the same things in her own words."
- No Notable Figures page for Nessa Thorne exists (Grep). Do not conflate.

**D5. Waypoint and the day-one employer.** Appendix D describes the tavern "will become" a waypoint only once the twins work there (`Appendix_D:296`). The guide calls them "server candidates" (`03-staff-and-hiring.md:50`). No source says where Nessa works on Ches 1. See F1.

---

## E. Stale lines in other files (do not edit) and routed references

**E1. Stale or conflicting lines in other files**
- `docs/plans/setting-compendium-research-notes/pass5/harpers.md:237` and `:238` quote the org page's Nessa line and cite `01-harpers.md:33`. Current line: `01-harpers.md:105`. The pass5 notes are stale on the org-page line numbers.
- `docs/plans/setting-compendium-pass3-closeout.md:64`: "Corvin Hallowell (Davil's Arrest) is not the Harper Corvin Nessa Vayle." Name typo; the campaign line is `campaign/gazetteer/waterdeep/trades-ward.md:259`: "Corvin Hallowell is not the Harper Corvin Vayle, whose page exists."
- `docs/plans/npc-pronouns-table-group-b.md:35` names "harpers/07-corvin-nessa-vayle.md". The current files are `07-corvin-vayle.md` and `08-nessa-vayle.md` (`docs/plans/npc-pronouns-table.md:61`).
- `campaign/setting/organizations/01-harpers.md:181` (quoted in D1) is the org page's own Draft Notes.

**E2. Routed references**
- None for Nessa's own sentences.

**E3. Trollskull hire, quest time**
- `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:159`: quoted in full in the Findings (see the Corvin notes, Findings 1). The Vayles are not named there.

---

## F. Gaps a Background needs that no source gives

**F1. Where she works on Ches 1, and whether she is employed.** No source. The Trollskull Manor is "an abandoned inn" at the start (`sources/27. Addendum A Night in Trollskull Manor.pdf`, PDF p.1, printed p.178; transcription). The twins are "Server Candidates" (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:50`, `:58`). The Persona calls them "servers" (`08-nessa-vayle.md:21`). Keep the Background consistent with both. Do not write an employer. `[research]` if the drafter names a Ches 1 employer.

**F2. Birth year, birth name, home, parents, family.** No source. Only "people who grew up in a city" (`Appendix_D:293`) applies to both twins. Do not name a parent or relative (brief ruling 17).

**F3. Her own Harper history, if any.** No source. Campaign: "Corvin's sister, who knows not to ask" (`01-harpers.md:105`); "servers who come as a pair" (`01-harpers.md:62`). No source says she has ever carried a message, met Mirt alone or worked a Harper task.

**F4. Personal wants that belong to Nessa alone.** The sources give only shared wants: "The Vayles want to work somewhere interesting enough to stay at, maintain the arrangement that lets them operate as a unit, and pass whatever Corvin needs to pass without Nessa having to know about it." (`08-nessa-vayle.md:15`). The practical want is shared: "we need the combined wage to afford rent in the North Ward" (`Appendix_D:293`). Any individual goal is `[design]`.

**F5. Faith, fears, losses, a person she cares about.** None in any source.

**F6. How she came to the pair's trade.** Only "We've been working bars in pairs since we were sixteen" (`Appendix_D:293`).

---

## G. Source facts that hint at the figure's inner life (do not contradict)

- "Nessa's practiced incuriosity about what Corvin sometimes does." — `campaign/setting/notable-figures/harpers/08-nessa-vayle.md:13`
- "To those who ask Nessa about it, she asked once, his answer was satisfactory, and she stopped asking." — `campaign/setting/notable-figures/harpers/08-nessa-vayle.md:21`
- "Nessa's incuriosity is loud and deliberate (\"Not asking. Don't care.\")." — `.claude/skills/character-voices/voices/harpers.md:144`
- "Corvin's sister, who knows not to ask." — `campaign/setting/organizations/01-harpers.md:105`
- "we need the combined wage to afford rent in the North Ward" — `sources/Appendix_D_-_Running_the_Tavern.md:293`
- "We've been working bars in pairs since we were sixteen" — `sources/Appendix_D_-_Running_the_Tavern.md:293`
- "They are not paid enough for that." — `campaign/setting/notable-figures/harpers/08-nessa-vayle.md:23`
- "Nessa handles front of house; I handle the room." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58`
- "the particular watchfulness of people who grew up in a city and learned early to pay attention." — `sources/Appendix_D_-_Running_the_Tavern.md:293`

---

## Not found

- Nessa's birth year, home, parents, family name, age beyond "a young woman", date of joining the Harpers, recruiter, faith, signature belongings, losses, fears, personal goals. Searched: `campaign/` (Grep "vayle|corvin|nessa", case-insensitive), `sources/adventure-wdh.json` (no hit), `sources/*.md` (Grep), `sources/research/` (Grep), `sources/SOURCE_GUIDE.md` (no Vayle or Nessa hit), root session handoffs (Grep), `docs/plans/` (Grep, planning notes only).
- Alexandrian PDF `27. Addendum A Night in Trollskull Manor.pdf`, PDF pp.4-5 (staffing) read: no Vayle. PDF pp.21-38 not read.
- Alexandrian PDF `3. Player Character Factions.pdf`, pp.1-3 read: no Nessa.
- Wiki: NOT FOUND; no pass5 bundle hit.

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. `sources/SOURCE_GUIDE.md:695` lists "The Waterdavian's Guide to Waterdeep NPCs ... .docx" as "Broad NPC reference", and `docs/plans/harpers-research/03-m01-m03.md:7` says it "is the only one likely to hold Maxeene, Mattrim or Bonnie material". Not checked for Nessa.
- `sources/27. Addendum A Night in Trollskull Manor.pdf`, PDF pp.21-38: not read.
