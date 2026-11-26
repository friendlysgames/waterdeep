# Pass 6 research notes: Chirada

Page: `campaign/setting/notable-figures/gralhunds/05-chirada.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Chirada's Missive (dated Ches 10), her Eye hunt and her Yellowspire watch are quest-time. Section C lists each sentence on the page that depends on them, with the file where each already lives.
Sizing: the brief's ruling 2 names major NPCs as heads, villains, lieutenants and Trollskull staff. Chirada is a field operative, so the sizing is the drafter's or orchestrator's call.
Organization page: `campaign/setting/organizations/12-house-gralhund.md`
Factions Guide: `campaign/guides/factions/13-house-gralhund.md`
Voice profile: `.claude/skills/character-voices/voices/gralhunds.md` (### Chirada, lines 79-93)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`
Wiki extract: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-gralhunds/05-chirada.txt` is **NOT FOUND** (one line, "NOT FOUND"). There is no wiki page for Chirada. The pass5 bundle has no Chirada wiki text.

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json` has **no** line naming Chirada (Grep over the whole JSON for "Chirada" returned nothing). The Alexandrian Act III files `Act_III_Arc_D.md` and `Act_III_Arc_E.md` do not name her either.
- Alexandrian PDFs were read as page images (no shell, so no `pdftotext`). `sources/4. Gralhund Villa.pdf` PDF p.5 (printed p.30) carries the Missive text; `sources/7. Other Response Teams.pdf` PDF p.1 (printed p.57) carries the unnamed spy. Both quotes are transcriptions. **Check with `pdftotext -layout` before any of them goes into prose.**
- No file was edited except this notes file. No Edit tool was available in this run, so this file was written whole. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **The Missive's wording differs between the current file and the Alexandrian text.** The current `g12-family-library.md:13` says "an Eye of the Stone". The Alexandrian (printed p. 30) says "the Second Eye". The current Chirada page says "the Eye of the Stone of Golorr". Older bundle copies of the page say "Second Eye". See D1.
2. **Almost all of the page is quest-time.** The Missive (Ches 10), the Yellowspire watch, the Eye hunt and "the Gralhund household in disarray" all come after day one. Sections C and E2 list them. The day-one core is her job, her look and her cover.
3. **Her Eye motivation is tied to a quest event.** The Zhentarim's theft of the Eye from the warehouse is in **Finding Floon** (`campaign/locations/zhentarim-warehouse/z05-offices.md:11`). The page's "the Eye she believes the Zhentarim took" depends on it. See C.
4. **No source gives her an origin, a date of service, a rank or a personal life.** See F.
5. **The "Mulan" ethnicity and "she/her" are on the page and the org page only.** No other source names her ethnicity. See B3.

---

## A. Background facts by theme

### A1. Origin, family and early life

No source gives Chirada's birthplace, birth name, family, age or early life. The wiki has no page (`wiki 05-chirada.txt` line 1: "NOT FOUND"). The only sourced identity facts are her role and her ethnicity.

**Campaign, org page, Key Members**
> "- **Chirada** — Mulan human operative, neutral, she/her. A Gralhund intelligence operative who keeps out of notice on the city's streets. See the **Chirada** page in Notable Figures."
> — `campaign/setting/organizations/12-house-gralhund.md:88`

**Campaign, org page, Contacts**
> "- **Contacts:** **Yalah Gralhund** (head of the house), **Orond Gralhund** (receives callers), **Chirada** (field operative)"
> — `campaign/setting/organizations/12-house-gralhund.md:8`

**Campaign, org page, Retainers**
> "- **Retainers:** Hrabbaz guards both Gralhunds and is more loyal to Yalah. Hurv Taldred keeps the yard with two mastiffs, and the Gralhunds paid a necromancer to ritually change the three of them into shadows from sundown to dawn. Chirada works as an intelligence operative in the city."
> — `campaign/setting/organizations/12-house-gralhund.md:47`

**Campaign, Factions Guide, the house's operative**
> "- Chirada is the house's intelligence operative and the team's spy. She leads the team in the field, because the other two are muscle."
> — `campaign/guides/factions/13-house-gralhund.md:42`

### A2. How she came to the house, and how she rose

No source gives her recruitment, a date of service, or a rank. The org page's Retainers line (`12-house-gralhund.md:47`) names her as an intelligence operative in the city. The Factions Guide names her as the team's spy (`13-house-gralhund.md:42`).

### A3. Her trade and methods

**Campaign, page, Morale (the method is day-one; the Eye clause is quest-time)**
> "**Morale.** Chirada does not fight if she can avoid it. Her response to exposure is withdrawal, misdirection, and a subsequent approach from a different direction. If cornered, or if the party signals genuine cooperation, she negotiates — she has nothing to gain from dying over an Eye she has not yet found, and information is worth more than pride."
> — `campaign/setting/notable-figures/gralhunds/05-chirada.md:23`

**Campaign, page, Persona (the look and the spotting rule; the last sentence is quest-time)**
> "**Persona.** To the world, Chirada does not register at street level — she is a woman across the street reading, a vendor browsing her own stall, a courier with a wrong address. To anyone who makes the DC 15 Perception check that spots her, she is a competent operative doing exactly what the party is doing, for a different employer."
> — `campaign/setting/notable-figures/gralhunds/05-chirada.md:21` (the sentences after "Deep down," are quest-time; see C)

**Campaign, Factions Guide, the spotting rule (DC 15)**
> "Chirada herself (**Faction Outposts**, Yellowspire; DC 15 Wisdom (Perception) to spot her across the street). If the party reaches her, she can give the Yellowspire teleportal lead."
> — `campaign/guides/factions/13-house-gralhund.md:84`

**Campaign, Factions Guide, how she is reached (quest-time)**
> "**Reaching Chirada.** She does not fight if she can avoid it. If she is cornered, or the party offers to cooperate, she negotiates, because she has nothing to gain from dying over an Eye she hasn't found. A party that reaches her before the team moves can learn the Yellowspire teleportal lead from her, including the access phrase. She trades information for information."
> — `campaign/guides/factions/13-house-gralhund.md:55`

### A4. Her faith

None. No source gives Chirada a faith or a cult link. She is not named in the cult passages (`campaign/locations/gralhund-villa/g16-master-bedroom.md:14`; `campaign/setting/organizations/12-house-gralhund.md:110`). Do not place her in the cult without a `[design]` tag, and the cult is GM-only (F9).

### A5. Signature belongings

None sourced. Her one named object is the Missive she signed (quest-time; see C).

### A6. How long in post

None sourced. The Missive is dated Ches 10: "A *Missive from Castle Ward*, signed "Chirada," dated Ches 10th" (`campaign/locations/gralhund-villa/g12-family-library.md:11`; the line's own markup is `*A Missive from Castle Ward, signed "Chirada," dated Ches 10th:*`). That is the only date for her, and it is quest-time.

---

## B. Alignment, species, pronouns, stat block

**B1. Name tag (page)**
> "- *Mulan human operative, neutral, she/her*. Stat block: **Spy**."
> — `campaign/setting/notable-figures/gralhunds/05-chirada.md:5`

**B2. Alignment**
- Page: "neutral" (`05-chirada.md:5`).
- Org page: "Mulan human operative, neutral, she/her." (`campaign/setting/organizations/12-house-gralhund.md:88`).
- Adventure: none (no Chirada in the JSON).
- Wiki: none (no page).

**B3. Species and ethnicity**
- Page: "Mulan human" (`05-chirada.md:5`).
- Org page: "Mulan human operative" (`12-house-gralhund.md:88`).
- Adventure: none. Alexandrian: none (the unnamed spy is not identified as Mulan).
- Ruling 5 (brief line 39) says humans take a Faerûn ethnicity. The page's "Mulan" is kept as the campaign uses it. The orchestrator decides whether it stays.

**B4. Pronouns**
- Page: "she/her" (`05-chirada.md:5`); the page's own Persona: "she is a woman across the street" (`05-chirada.md:21`).
- Org page: "she/her" (`12-house-gralhund.md:88`).
- Adventure, Alexandrian: none.
- Wiki: none.

**B5. Stat block**
- Page: "Stat block: **Spy**." (`05-chirada.md:5`).
- Factions Guide roster: "**Roster:** Hrabbaz (**Tough**) + Chirada (**Spy**) + 1 **Adept**." (`campaign/guides/factions/13-house-gralhund.md:39`)
- Factions Guide: "Chirada is the house's intelligence operative and the team's spy." (`13-house-gralhund.md:42`)
- Alexandrian, the Gralhund response team (printed p. 57; transcription; the spy is unnamed): "A **spy** (MM p. 349)" (`sources/7. Other Response Teams.pdf` PDF p.1). The Alexandrian does not name Chirada for the spy slot. See D2.
- No CR is sourced for Chirada in any file.

**B6. Affiliation**
- Page: "> - **Affiliation:** House Gralhund" (`05-chirada.md:6`).
- Org page Contacts: "**Chirada** (field operative)" (`12-house-gralhund.md:8`).

---

## C. Sentences on the current page that narrate a quest event or a day-one conflict

Current page: `campaign/setting/notable-figures/gralhunds/05-chirada.md`. The page has no Background, Personality or Connections section yet. Each row says where the quest-time fact already lives.

| # | Line | Sentence (exact) | Status | Where the event already lives |
|---|---|---|---|---|
| 1 | L5 | "- *Mulan human operative, neutral, she/her*. Stat block: **Spy**." | Day-one name tag. Stat label is a Factions Guide assignment, not a source stat (B5) | section B |
| 2 | L6 | "- **Affiliation:** House Gralhund" | Day-one | `campaign/setting/organizations/12-house-gralhund.md:88` (Key Members) |
| 3 | L7 | "- **Featured in:** **Gralhund Villa**, **Faction Outposts**" | Routing list, not narrative | `campaign/quests/act-ii/gralhund-villa/overview.md` and `campaign/structure/arc-e-faction-outposts.md:223` |
| 4 | L11 | "**Resonance.** Chirada should inspire professional respect for how thoroughly she has been following the same evidence trail as the party, unease when the party realizes she was watching Yellowspire from across the street before they arrived, and cautious interest — she is not an enemy by default, and she may be more useful as an informed independent party than as an obstacle." | **Quest-time.** "the same evidence trail as the party" is the Finding Floon and Fireball! trail. "watching Yellowspire from across the street before they arrived" is the Faction Outposts watch. "she is not an enemy by default" is the Chirada Complication | `campaign/structure/arc-e-faction-outposts.md:229` ("She is not an enemy by default — she is a competing investigator following the same evidence trail.") and `campaign/guides/factions/13-house-gralhund.md:100` |
| 5 | L13 | "**Emotions.** Chirada most often feels focused competence, patient determination, professional assessment of how a given situation might be leveraged, and measured irritation when others disrupt a surveillance operation she has been running for weeks." | Day-one character trait, except "a surveillance operation she has been running for weeks" implies a quest-time operation. Flag. The operation is the Yellowspire watch (Ches 10 onward) | `campaign/locations/gralhund-villa/g12-family-library.md:11` (the Ches 10 letter) and `campaign/structure/arc-e-faction-outposts.md:223` |
| 6 | L15 | "**Motivations.** Chirada wants to recover the Eye of the Stone of Golorr she believes the Zhentarim took, for what remains of Gralhund House interests, track the movements of whoever holds the Stone, and complete the mission described in the Missive from Castle Ward without becoming another casualty of the Grand Game." | **Quest-time.** "the Eye ... she believes the Zhentarim took" is the Finding Floon warehouse theft. "for what remains of Gralhund House interests" is post-raid. "track the movements of whoever holds the Stone" is the Stone after Ches 22 and Ches 24. "the mission described in the Missive from Castle Ward" is the Ches 10 letter | `campaign/locations/zhentarim-warehouse/z05-offices.md:11` ("Whoever opened it took the Eye of the Stone of Golorr."); `campaign/locations/gralhund-villa/g12-family-library.md:11`; `campaign/guides/factions/13-house-gralhund.md:26` ("Chirada works alone as a team of one, tracking whoever holds the Stone and the Eye she believes the Zhentarim took.") |
| 7 | L17 | "**Inspirations.** When playing Chirada, channel George Smiley (*Tinker Tailor Soldier Spy*), Maya (*Zero Dark Thirty*), and Melinda May (*Agents of S.H.I.E.L.D.*)." | Not a fact. Keep | n/a |
| 8 | L21 | "**Persona.** To the world, Chirada does not register at street level — she is a woman across the street reading, a vendor browsing her own stall, a courier with a wrong address. To anyone who makes the DC 15 Perception check that spots her, she is a competent operative doing exactly what the party is doing, for a different employer. Deep down, with the Gralhund household in disarray following **Gralhund Villa**, she is the most capable intelligence asset they have left — working independently, without backup, on a mission she intends to complete anyway." | First three sentences: day-one look and spotting rule. "doing exactly what the party is doing" is quest-time (it presumes a party investigating the same trail). The last sentence is **quest-time**: "the Gralhund household in disarray following Gralhund Villa", "the most capable intelligence asset they have left" (post-raid), and "a mission she intends to complete anyway" (the Eye hunt) | `campaign/guides/factions/13-house-gralhund.md:26` ("Yalah In Custody, or dead. Nobody gives orders. ... Chirada works alone as a team of one") and `:131` (the design call that rests on this line); `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:44` (the house's state after the raid) |
| 9 | L23 | "**Morale.** Chirada does not fight if she can avoid it. Her response to exposure is withdrawal, misdirection, and a subsequent approach from a different direction. If cornered, or if the party signals genuine cooperation, she negotiates — she has nothing to gain from dying over an Eye she has not yet found, and information is worth more than pride." | First two sentences: day-one. "an Eye she has not yet found" is quest-time (the Eye is taken in the Finding Floon warehouse and lifted by Bregan D'aerthe; see C6). The rest is day-one | `campaign/guides/factions/13-house-gralhund.md:55` and `campaign/structure/arc-e-faction-outposts.md:223` |
| 10 | L25 | "**Relationships.** Chirada is a Gralhund intelligence operative who signed the Missive from Castle Ward the party found in G12, a competing investigator tracking the Stone through **Gralhund Villa** and into **Faction Outposts**, and a potential intelligence source on the Yellowspire teleportal — including the access phrase — if the party reaches her before she becomes a complication instead." | First clause (operative) is day-one. "signed the Missive from Castle Ward the party found in G12", "tracking the Stone through Gralhund Villa and into Faction Outposts", and "a potential intelligence source on the Yellowspire teleportal" are quest-time | `campaign/locations/gralhund-villa/g12-family-library.md:11` and `:17`; `campaign/quests/act-ii/gralhund-villa/ev-03-daytime-infiltration.md:75` to `:77`; `campaign/guides/factions/13-house-gralhund.md:84` and `:100` |
| 11 | L29 | "A woman whose face keeps turning up at the edges of the party's business: reading across the street, browsing a vendor's stall, gone by the time anyone looks twice." | **Quest-time** in its frame: "the party's business" presumes a party investigating. The image of the watch is day-one, but the sentence depends on the party's presence. Route or rewrite as a day-one description | `campaign/structure/arc-e-faction-outposts.md:223` and `campaign/guides/factions/13-house-gralhund.md:100` |

**Voice profile, quest-time clauses (`.claude/skills/character-voices/voices/gralhunds.md`, "### Chirada", lines 79-93)**

- Line 80 (tagline): "*A quiet, competent operative working the same trail as the party, who speaks like a colleague.*" **Quest-time**: "working the same trail as the party" presumes the party's investigation. Flag; a day-one restatement is the drafter's call under ruling 16.
- Line 82 (Sound): "A low, level, unremarkable voice. It's easy to forget, which is the point." Day-one.
- Line 83 (Sentence shape): "Efficient, professional sentences. She assesses, states and proposes, with no small talk." Day-one.
- Line 84 (Word choice): "Tradecraft: surveillance, \"the asset\", \"the Eye\", \"my employer\". She calls the party \"you lot\" or by role." Day-one. "the Eye" is quest-time vocabulary (see C6); keep as a term she uses.
- Line 85 (Swearing): "*Triggered · Plain · Phrase.* When someone blunders into a surveillance she's spent weeks on (\"You've just blown three weeks of fucking work.\")." **Quest-time**: "a surveillance she's spent weeks on" and the sample line presume the Yellowspire watch. The swearing level is kept (adult table, real profanity in speech). Flag the clause.
- Line 86 (Personality in speech): "Focused competence and determination. She treats the party as professional peers or as obstacles, and says which. She's open to a deal if it serves the mission." Day-one, except "the party" presumes a party. Keep.
- Line 87 (Quirks): "She speaks without looking at the person, watching the street. She knows where they've been and says so plainly." Day-one. "She knows where they've been" presumes a party that has been somewhere; flag lightly.
- Line 88 (Signature phrases): "\"I've been watching you too.\" / \"Same trail, different employer.\" / \"Don't blow my cover.\"" **Quest-time** in its implication: "I've been watching you too" and "Same trail" presume a party on the Grand Game trail. Flag.
- Line 89 (Never): "She never names her employer outright, never gives up the mission, and never makes a scene." Day-one, except "the mission" is the Eye hunt. Keep with the mission read as her standing job.
- Line 91 (Greeting sample): "\"Don't look at me. Keep browsing. I've been watching you since Yellowspire.\"" **Quest-time**: "since Yellowspire" is the Faction Outposts watch. Flag. A day-one sample is the drafter's call.
- Line 92 (Business sample): "\"Same trail, different employer. We can trip over each other, or we can share what we know.\"" **Quest-time** in its frame ("same trail" presumes the party's investigation). Flag.
- Line 93 (Under pressure sample): "\"You've just blown three weeks of fucking work. Move, before they see both of us.\"" **Quest-time**: "three weeks of fucking work" presumes the Yellowspire watch. The swearing stays (adult table). Flag.

**Quest-time clauses in the profile:** lines 80, 85, 88, 91, 92 and 93 (and line 87's "where they've been"). The swearing and the sample lines are kept, with the day-one restatement left to the drafter, under ruling 16.

**Quest-time facts the Background must not restate.** Each lives in the quest, the structure doc or the location journal.

- The Ches 10 Missive: `campaign/locations/gralhund-villa/g12-family-library.md:11` to `:17`; `campaign/quests/act-ii/gralhund-villa/ev-03-daytime-infiltration.md:70` to `:77`; `ev-03b-the-front-door.md:95`.
- The Yellowspire watch and the complication: `campaign/structure/arc-e-faction-outposts.md:223` and `:229`; `campaign/guides/factions/10-manshoons-zhentarim.md:41`.
- The Eye theft and the Stone's movements: `campaign/locations/zhentarim-warehouse/z05-offices.md:11`; `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:114` (`G12 Searched: Chirada Letter Found`).
- The post-raid house: `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:36` (the Yellowspire teleportal lead, "G12 — Chirada letter (if **Chirada Letter Found** is marked)") and `:44`.

---

## D. Conflicts

**D1. The Missive's wording: "an Eye", "the Second Eye", or "the Eye"**
- Current location file: "We are now certain that the Zhentarim took an Eye of the Stone from the warehouse in the Dock Ward, and that their couriers carried it to Yellowspire in the Castle Ward." (`campaign/locations/gralhund-villa/g12-family-library.md:13`)
- Current Chirada page: "the Eye of the Stone of Golorr she believes the Zhentarim took" (`campaign/setting/notable-figures/gralhunds/05-chirada.md:15`)
- Current Gralhund Villa Ches 24 Chirada Letter callout (the daytime infiltration event): "It names an Eye of the Stone, Yellowspire in the Castle Ward, and a suspected teleportal." (`campaign/quests/act-ii/gralhund-villa/ev-03-daytime-infiltration.md:77`)
- Alexandrian (printed p. 30; transcription): "A Missive from Castle Ward: \"We are now certain that the Second Eye was carried from the warehouse in the Dock Ward to Yellowspire in the Castle Ward. I no longer believe that it remains within Yellowspire, however. After observing the Zhentarim traffic here, I am convinced that they must be using a teleportal within the tower. If we wish to track the Second Eye further, we will need to access that teleportal or otherwise determine where it leads. — Chirada\"" (`sources/4. Gralhund Villa.pdf` PDF p.5). Check with `pdftotext`.
- Stale bundle copies: "We are now certain that the Second Eye was carried from the warehouse in the Dock Ward" (`sources/research/pass3-bundles/dock-ward/campaign-hits.txt:35`, quoting an older `g12-family-library.md:13`). The bundle also quotes an older `05-chirada.md:16` with "Second Eye" (`sources/research/pass3-bundles/stone-of-golorr-and-the-eyes/campaign-hits.txt:157`; `sources/research/pass4-bundles/grand-game/campaign-hits.txt:195`). The current files say "an Eye", and the current Chirada page has no "Second Eye".
- Settled by the user (Session 51), campaign: "**Settled by the user (Session 51):** The Eye in the warehouse. Chirada's letter now says the Zhentarim carried an Eye to Yellowspire, which is her mistake: the Guild's raiders carried the locket Eye to the hideout, where Bregan D'aerthe lifted it (`xanathar-sewer-hideout/area-overview.md:72-73`). There is one Eye, not two." (`campaign/gazetteer/waterdeep/dock-ward.md:305`)
- Higher-ranked source: the campaign (Session 51 ruling, `dock-ward.md:305`; `stone-of-golorr-and-the-eyes.md:176`). The Alexandrian's "Second Eye" is superseded. The current text is "an Eye" and "the Eye". Use the current text.

**D2. The response-team spy: Chirada or unnamed**
- Factions Guide: "**Roster:** Hrabbaz (**Tough**) + Chirada (**Spy**) + 1 **Adept**." (`campaign/guides/factions/13-house-gralhund.md:39`)
- Alexandrian (printed p. 57; transcription): "A **spy** (MM p. 349)" (`sources/7. Other Response Teams.pdf` PDF p.1)
- Higher-ranked source: the Alexandrian names no spy, and the campaign names Chirada. The campaign is higher-ranked; the Alexandrian's spy is a generic slot. Not a factual conflict. The orchestrator should know that the Alexandrian team has no name for the spy.

**D3. The Dock Ward and the Candle Lane warehouse**
- Current Missive: "the warehouse in the Dock Ward" (`g12-family-library.md:13`)
- Current g12 note: "The Zhentarim pried the locket open at the Candle Lane warehouse, but Xanathar's Guild raided it the same night, and Bregan D'aerthe lifted the Eye in the Guild's hideout (see Eye #3 in **Running the Villains**)." (`campaign/locations/gralhund-villa/g12-family-library.md:15`)
- Zhentarim Warehouse overview: "The warehouse sits at the back of a walled yard on Candle Lane." (`campaign/locations/zhentarim-warehouse/area-overview.md:22`)
- Gazetteer, Dock Ward: "Chirada's letter in **Gralhund Villa** says the Zhentarim carried an Eye from a warehouse in the Dock Ward to Yellowspire, which is her mistake." (`campaign/gazetteer/waterdeep/dock-ward.md:91`)
- Status: not a settled conflict in the lines read. The files give no ward for Candle Lane. The Missive says "Dock Ward" and the g12 note says "Candle Lane". The Dock Ward gazetteer treats the warehouse as Dock Ward. The drafter should not name a ward for the warehouse until the orchestrator decides.

**D4. The Chirada letter's date and the Gralhund raid's date**
- Current Missive: "A *Missive from Castle Ward*, signed \"Chirada,\" dated Ches 10th" (`g12-family-library.md:11`).
- Current Ches 24 callout: "A *Missive from Castle Ward*, signed \"Chirada,\" dated two weeks prior." (`campaign/quests/act-ii/gralhund-villa/ev-03-daytime-infiltration.md:75`)
- Not a conflict. Two weeks before Ches 24 is Ches 10. The date is quest-time either way.

**D5. Pronouns and the sex of the figure in the Alexandrian**
- The Alexandrian uses no pronoun for Chirada (she is not named in the Alexandrian). The campaign's "she/her" (`05-chirada.md:5`) stands. No conflict found.

**D6. The Eye: where it went (the letter is wrong)**
- Current g12: "Chirada is wrong about where the Eye went." (`g12-family-library.md:15`); Dock Ward: "which is her mistake" (`dock-ward.md:91`). Consistent with the page's "the Eye she believes the Zhentarim took" (`05-chirada.md:15`). No conflict.

---

## E. Stale lines in other files (do not edit), and routed quest references

**E1. Stale or superseded lines**
- `sources/research/pass3-bundles/dock-ward/campaign-hits.txt:35` and `sources/research/pass3-bundles/stone-of-golorr-and-the-eyes/campaign-hits.txt:157`, `sources/research/pass4-bundles/grand-game/campaign-hits.txt:195`: "Second Eye" (older copies; D1).
- `sources/research/pass4-bundles/jarlaxle/campaign-hits.txt:25`: quotes an older `dock-ward.md:315` "Unresolved" note; the current `dock-ward.md:305` says "Settled by the user (Session 51)". Stale.
- `campaign/structure/arc-d-gralhund-villa.md:352`: "**The Second Eye / Yellowspire Teleportal:** In hand if G12 was searched. *A Missive from Castle Ward* and Chirada's name. Pays off in Arc E." Superseded structure doc; uses "Second Eye" (D1).
- `campaign/structure/arc-d-gralhund-villa.md:418`: "**Arc E: Faction Outposts** — Direct successor. *A Missive from Castle Ward* (G12, Scene 3) seeds Yellowspire and Chirada's name." Superseded.
- `campaign/structure/arc-e-faction-outposts.md:229`: "The GM determines whether she arrives during the operation, after it, or is dealt with beforehand based on whether the party noticed her during reconnaissance." Pending-conversion doc; the Factions Guide turns it into a rule (`13-house-gralhund.md:136`).

**E2. Routed quest references (quest-time facts; the day-one page must not restate them)**

Campaign quest files:
- `campaign/quests/act-ii/gralhund-villa/ev-03-daytime-infiltration.md:70` to `:77`: the "The Chirada Letter (G12 — Day and Night)" callout, which says "A *Missive from Castle Ward*, signed \"Chirada,\" dated two weeks prior. The party can read it if they are in G12 and look at the stand — no check required." and "It names an Eye of the Stone, Yellowspire in the Castle Ward, and a suspected teleportal. Chirada is wrong about where the Eye went. This is a direct feed into the Grand Game intelligence network the party will navigate in **Faction Outposts**. Mark **Chirada Letter Found** when the party reads it."
- `ev-03-daytime-infiltration.md:105`: "> - **Chirada Letter Found** — mark when the party finds and reads *A Missive from Castle Ward* on the G12 reading stand; read by **Faction Outposts**, which pays it off with Yellowspire, Chirada's name and the teleportal lead."
- `campaign/quests/act-ii/gralhund-villa/ev-03b-the-front-door.md:95`: "The Chirada letter on the G12 reading stand is visible to anyone who enters the library — no check required. Mark **Chirada Letter Found** when the party reads it."
- `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:36`: "| Yellowspire teleportal lead | G12 — Chirada letter (if **Chirada Letter Found** is marked) | **Faction Outposts** |"
- `campaign/quests/act-ii/gralhund-villa/flowchart.md:98`: "| Chirada Letter Found | ev-03 or ev-03b (also on the G12 room page) | **Faction Outposts** (Yellowspire teleportal lead) |"

Location files:
- `campaign/locations/gralhund-villa/g12-family-library.md:11` to `:17`: the letter's text and the note "Chirada is wrong about where the Eye went. The Zhentarim pried the locket open at the Candle Lane warehouse, but Xanathar's Guild raided it the same night, and Bregan D'aerthe lifted the Eye in the Guild's hideout (see Eye #3 in **Running the Villains**). What she watched was Zhentarim couriers moving between the warehouse and Yellowspire."
- `campaign/locations/gralhund-villa/area-overview.md` has no Chirada line.

Structure and Factions Guide:
- `campaign/structure/arc-e-faction-outposts.md:223`: "*Step 2 — Case the Target.* ... After **Gralhund Villa**, Chirada watches the tower from across the street on any visit — she is tracking the Stone's movements on behalf of remaining Gralhund interests, following up on the *Missive from Castle Ward*. DC 15 Perception to notice her. Cross-ref **Gralhund Villa**, Scene 6 Aftermath and Design Notes."
- `arc-e-faction-outposts.md:229`: "*The Chirada Complication.* If the Gralhunds remain active following **Gralhund Villa**, Chirada may mount her own investigation of the tower, complicating the party's operation. She is not an enemy by default — she is a competing investigator following the same evidence trail. The GM determines whether she arrives during the operation, after it, or is dealt with beforehand based on whether the party noticed her during reconnaissance."
- `arc-e-faction-outposts.md:434`: "| `sources/7. Other Response Teams.pdf` | Gralhund, Open Lord, Unseen, freelancer, and urchin teams. Consulted for the Chirada complication at Yellowspire. |"
- `arc-e-faction-outposts.md:447`: "- **Gralhund Villa** — Predecessor quest. Scene 6 Aftermath defines this quest's starting state: Davil's arrest, Chirada's active investigation, and the *Missive from Castle Ward* thread."
- `campaign/guides/factions/10-manshoons-zhentarim.md:41`: "**Gralhund complication:** If the Gralhunds remain active in the Grand Game, their agent Chirada may be watching Yellowspire from across the street. The Gralhunds may mount their own raid on Yellowspire to access the teleportal, inserting a third party into whatever operation the characters are planning."
- `campaign/guides/factions/13-house-gralhund.md:26`: "- **Yalah In Custody, or dead.** Nobody gives orders. Orond is in shock and makes no move. Chirada works alone as a team of one, tracking whoever holds the Stone and the Eye she believes the Zhentarim took."
- `13-house-gralhund.md:55` and `:84`: quoted in A3.
- `13-house-gralhund.md:100`: "| **Faction Outposts** | Chirada watches Yellowspire from across the street on any visit, tracking the Stone's movements for what remains of the house. A party that spots her on reconnaissance can speak to her before the operation. A party that misses her meets her as a third party during the operation. |"
- `13-house-gralhund.md:131`: "The house acts only while Yalah is Missing. When she is In Custody or dead, Chirada alone acts. This rests on her page (`05-chirada.md:21`): \"the most capable intelligence asset they have left — working independently, without backup\"."

Gazetteer and lore:
- `campaign/gazetteer/waterdeep/dock-ward.md:10`: "**Gralhund Villa** leaves Chirada's letter in the family library, which says the Zhentarim carried an Eye from a Dock Ward warehouse to Yellowspire. She is wrong about where the Eye went."
- `dock-ward.md:91` and `:305`: quoted in D1 and D6.
- `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:114`: "- **G12 Searched: Chirada Letter Found:** Set in **Gralhund Villa**. It pays off in **Faction Outposts**."
- `stone-of-golorr-and-the-eyes.md:162`: "- **Dagult Neverember**, **Renaer Neverember**, **Dalakhar**, **Aurinax**, **Yalah Gralhund**, **Chirada**, **Ott Steeltoes**, **Seffia Naelryke** and **Jeryth Phaulkon**: the people who handle or sense the Stone." (cross-reference only)
- `stone-of-golorr-and-the-eyes.md:176`: "> - **Settled by the user (Session 51):** The Chirada letter. `gralhund-villa/g12-family-library.md` now has Chirada write that the Zhentarim took \"an Eye\" from the warehouse to Yellowspire. She is wrong: the Guild carried the locket Eye off the same night and Bregan D'aerthe lifted it (`running-the-villains.md:25`), so the letter is a spy's mistake and the lead is the Yellowspire teleportal."

Zhentarim warehouse (the Eye's theft, Finding Floon):
- `campaign/locations/zhentarim-warehouse/z05-offices.md:11`: "This is the locket Renaer described. Whoever opened it took the Eye of the Stone of Golorr. What became of the Eye is told in the **Xanathar Sewer Hideout** and **The Eyes of the Stone**. The locket matters to Renaer and to the Stone's backstory."
- `zhentarim-warehouse/area-overview.md:6`: "This location is used during the **Zhentarim Warehouse** Event (ev-03) of Finding Floon." (the warehouse event is Finding Floon)

Alexandrian:
- `sources/4. Gralhund Villa.pdf` PDF p.5 (printed p.30): the Missive text (D1). Transcription.
- `sources/7. Other Response Teams.pdf` PDF p.1 (printed p.57): "A **spy** (MM p. 349)" (D2). Transcription.
- `sources/Act_III_Arc_E.md` and `sources/Act_III_Arc_D.md`: no Chirada.

Published adventure: no Chirada.

**E3. Notes on what the drafter must not carry**
- The "Second Eye" wording (D1).
- "Chirada's active investigation" as a day-one state (`arc-e-faction-outposts.md:447`), which belongs to the quest.

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

**F1. Origin, birthplace and family.** No source. Stay consistent with: "Mulan human operative" (`05-chirada.md:5`; `12-house-gralhund.md:88`). Any origin must stay Mulan (the campaign's ethnicity) and human.

**F2. How she came to the house, and when.** No source. The Factions Guide says she is a "Gralhund intelligence operative who keeps out of notice on the city's streets" (`12-house-gralhund.md:88`, the Key Members line). The org page's Retainers line says she "works as an intelligence operative in the city" (`12-house-gralhund.md:47`). Any recruitment is `[design]`.

**F3. Training and prior career.** No source. The page's "competent operative" (`05-chirada.md:21`) and the "tradecraft" in the voice (`gralhunds.md:84`) are the only hints. Any former career is `[design]`.

**F4. Her relationship to Yalah and to the house.** Sourced: Chirada is "a Gralhund intelligence operative" (`05-chirada.md:25`). Nothing names who she reports to. The voice says she never names "my employer" (`gralhunds.md:89`). Do not name Yalah as her employer without a `[research]` tag, because no file states it.

**F5. Her motivations beyond the Eye.** The page's Motivations is the Eye and the Missive (quest-time; C6). No day-one personal want is sourced. Brief ruling 17 needs a personal want. Any goal must be `[design]`, must not depend on the Eye (a quest object), and must not change the Stone or the Event Outcomes.

**F6. A person she cares about or a loss.** No source. Any person is `[design]`, must not be a new Notable Figure unless a source names them, and must not be a quest character.

**F7. Her faith.** No source. Do not place her in the cult (F9).

**F8. Her age and appearance.** No source gives an age. The page's Persona gives the look: "a woman across the street reading, a vendor browsing her own stall, a courier with a wrong address" (`05-chirada.md:21`). Any age is `[design]`.

**F9. The Asmodean cult.** No source names Chirada in the cult. Cassalanter secrecy: nobody outside the household and the cult knows the pact (CLAUDE.md, "Cassalanter secrecy"). The cult is GM-only (org page Secret callout `12-house-gralhund.md:107` to `:110`). Do not place her in it.

**F10. Stat block.** The "Spy" label is the Factions Guide's assignment (`13-house-gralhund.md:39`, `:42`). No source gives Chirada a stat block or CR.

---

## G. Source facts that hint at the figure's inner life

Quoted exactly. The drafter uses them for the backstory and personal goals (brief ruling 17). Nothing in a Background may contradict them. Lines that depend on the Eye or the Missive are quest-time; they are repeated here only so the drafter knows what she is like, and they are not day-one facts.

- Patience (day-one trait): "patient determination" (`05-chirada.md:13`)
- Assessing people for use (day-one trait): "professional assessment of how a given situation might be leveraged" (`05-chirada.md:13`)
- Information over pride (day-one, the last clause of Morale): "information is worth more than pride" (`05-chirada.md:23`)
- Keeps to the street: "Chirada does not register at street level" (`05-chirada.md:21`)
- Avoids a fight: "Chirada does not fight if she can avoid it." (`05-chirada.md:23`)
- Withdraws and comes back from another angle: "Her response to exposure is withdrawal, misdirection, and a subsequent approach from a different direction." (`05-chirada.md:23`)
- Works alone (quest-time; the Factions Guide repeats it at `13-house-gralhund.md:131`): "working independently, without backup" (`05-chirada.md:21`)
- Never names her employer: "She never names her employer outright, never gives up the mission, and never makes a scene." (voice line 89)
- Speaks without looking at the person: "She speaks without looking at the person, watching the street." (voice line 87)
- Low, forgettable voice: "A low, level, unremarkable voice. It's easy to forget, which is the point." (voice line 82)
- Treats peers as peers or as obstacles: "She treats the party as professional peers or as obstacles, and says which." (voice line 86)
- Competitive with other investigators (quest-time): "a competing investigator" (`05-chirada.md:25`); "a surveillance operation she has been running for weeks" (`05-chirada.md:13`).
- Her confidence in the Eye (quest-time): "she believes the Zhentarim took" (`05-chirada.md:15`), and the letter's "We are now certain" (`g12-family-library.md:13`). The Eye is not the Stone and she is wrong about where it went (`g12-family-library.md:15`).
- The house's loss as she sees it (quest-time): "the most capable intelligence asset they have left" (`05-chirada.md:21`)
