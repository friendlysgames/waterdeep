# Pass 6 research notes: Ryvarra

Page: `campaign/setting/notable-figures/bregan-daerthe/09-ryvarra.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR. Ryvarra is a Bregan D'aerthe field observer already at the Yawning Portal on day one (watch begins about Alturiak 17, 1492 DR, `campaign/setting/history/08-the-players-arrive.md:86`). Her Trollskull and First Meeting roles are quest time. Cassalanter secrecy and the Lolth rule apply (no Ryvarra source touches either).
Organization page: `campaign/setting/organizations/07-bregan-daerthe.md`
Voice profile: `.claude/skills/character-voices/voices/bregan-daerthe.md` ("### Ryvarra", lines 168-182)
Wiki extract: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-bregan-daerthe/09-ryvarra.txt` contains `NOT FOUND`. No wiki page exists for Ryvarra.

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines from that output.
- Published adventure: `sources/adventure-wdh.json`. Grep for "Ryvarra", "Calimshan", "cloth merchant" and "balcony" in the Yawning Portal passages gave no match for Ryvarra. The adventure has no Ryvarra entry (section B).
- Alexandrian PDFs: no shell, so `pdftotext` could not run. The PDF read below was rendered as page images. Its quote is a transcription and needs a `pdftotext -layout` check before any use in prose.
  - `sources/23. Addendum First Impressions.pdf` (printed pp.162-165 = PDF pp.1-4). Read: PDF pp.1-4 (all of the file).
- Alexandrian `sources/Appendix_B_-_Player_Factions.md`, `Appendix_C`, `Appendix_D`, `Act_III_Arc_D.md`, `Act_III_Arc_E.md`: Grep for "Ryvarra", "observer" and "Yawning" gave no Ryvarra match.
- Wiki: NOT FOUND. Pass 5 wiki bundle `sources/research/pass5-bundles/bregan-daerthe/wiki.txt`: Grep for "Ryvarra" gave no match.
- The pronoun and first-meeting quotes are from `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md`, which the Grep output gave by line.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **Tenure conflicts inside the campaign.** The page says "two weeks of watching the well" (L13) and "executed over months" (L11). The First Meeting says "for three months" (`ev-01-first-meeting.md:28`). Finding Floon and the history page say two weeks. See D1.
2. **Report cadence conflicts.** The page says "weekly" (L15, L25). The First Meeting says "every tenday" (`ev-01-first-meeting.md:28`). See D2.
3. **The Overview is 36 words**, over the 21-word limit (L29). See C row 9.
4. **Quest-time clauses on the page** are the party-directed sentences in Resonance, Emotions, Persona, Morale and Relationships (section C). The "troll" in the voice Greeting sample is a Finding Floon scene (C row 14).
5. **No source names Ryvarra as a member, an associate or a contact in those words.** The organization page lists her under Key Members (`07-bregan-daerthe.md:107`). The published adventure's rule is "A character must be a drow, preferably a male, to join this faction." (`sources/adventure-wdh.json:1296`). Ryvarra is a drow. Drafter must choose the label; section E2 gives the sources.
6. **The Alexandrian "Yawning Portal watcher" seed is not in the PDF.** `SOURCE_GUIDE.md:549` says the First Impressions addendum has "A Bregan D'aerthe watcher in the Yawning Portal". The PDF pages read (PDF pp.1-4) contain no such watcher. See section B and the Not found list.

---

## A. Background facts by theme

### A1. Origin, birth, species, former life
No source gives a birth year, home, house, family, age, or a former life. The only species statement is in campaign quest text and the org page.

**Organization page (Key Members)**
> "- **Ryvarra** — Drow spy and field observer, neutral. Stationed at the Yawning Portal to catalog Undermountain traffic. See the **Ryvarra** page in Notable Figures."
> — `campaign/setting/organizations/07-bregan-daerthe.md:107`

**Finding Floon, the entry (quest text; the only "drow woman" wording)**
> "**Ryvarra** (BD observer) — a drow woman in the observation balcony, posing as a Calimshan cloth merchant, untouched glass of wine in front of her. She has been at that table every evening for two weeks, cataloguing who descends into Undermountain and who comes back. She is never named in this quest. The party notices her only if they specifically ask who is watching the well; they get a description, nothing more."
> — `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:28`

**First Meeting, the stat line (quest text)**
> "Ryvarra (Neutral, Drow, she/her) :: Jarlaxle's field observer at the Yawning Portal, who plays a Calimshan cloth merchant in the middle of a long negotiation."
> — `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:83`

**Villains page**
> "- **Ryvarra** is a field observer at the Yawning Portal who catalogs Undermountain traffic for his Waterdeep network. She is the first sign that he had eyes on the party from their first night in the city (the **Ryvarra** page)."
> — `campaign/setting/villains/jarlaxle.md:60` (the "first night" clause is quest-time framing; see C row 11)

**Published adventure**
> No Ryvarra entry. Grep for "Ryvarra" and "Calimshan" in `sources/adventure-wdh.json` returned no match. The Yawning Portal passages (`sources/adventure-wdh.json:1465` onward) name Durnan, Volo, Yagra, Krentz, Meloon, Davil and Bonnie, and no drow watcher.

**Alexandrian, First Impressions (PDF pp.1-4, printed pp.162-165)**
> The four pages read contain the Yawning Portal opening, the Friendly Faces handout, the Dip and the troll. No "watcher", "observer" or Bregan D'aerthe figure appears. Transcription check not possible (no `pdftotext`).
> — `sources/23. Addendum First Impressions.pdf` PDF pp.1-4
> Conflicts with `sources/SOURCE_GUIDE.md:549`: "- A Bregan D'aerthe watcher in the Yawning Portal: a subtle first seed of Jarlaxle's surveillance network"

### A2. How she joined and rose
No source. The org page's Key Members line is the only placement (A1). The Factions Guide has no Ryvarra entry (searched `campaign/guides/factions/08-bregan-daerthe.md` for "Ryvarra", "Margo" and "observer", with no match).

Her post is set in the org page's Structure section:
> "**The Waterdeep network:** Ryvarra watches the well at the Yawning Portal from the balcony, and Quilm files a weekly intelligence report for Jarlaxle."
> — `campaign/setting/organizations/07-bregan-daerthe.md:67`

### A3. Post and time in post
- The history page dates her watch to about Alturiak 17, 1492 DR, derived:
> "- About Alturiak 17, 1492 DR (derived): Ryvarra begins watching the Yawning Portal."
> — `campaign/setting/history/08-the-players-arrive.md:86`
- Same page, the Yawning Portal paragraph:
> "- Ryvarra watches the Yawning Portal from the observation balcony, posing as a Calimshan cloth merchant. She has sat there every evening for two weeks when the party arrives, which is about Alturiak 17, 1492 DR. `[research]`"
> — `campaign/setting/history/08-the-players-arrive.md:42`
- Arithmetic check (for the drafter): Alturiak has 30 days, so Alturiak 17 is two weeks before Ches 1. The history page and Finding Floon agree on "two weeks". The "three months" line in the First Meeting does not (D1).

### A4. Faith
Not stated in any source. The Lolth rule (`campaign/setting/history/03-bregan-daerthes-long-road.md:34`, "- This is where the campaign rule starts. Jarlaxle rejected Lolth, Bregan D'aerthe rejects her, and its members speak of her as the goddess they walked away from.") binds any faith the drafter gives her.

### A5. Signature belongings and cover
**Page, Persona (cover)**
> "**Persona.** To the world, Ryvarra is a Calimshan cloth merchant taking her evening wine at a reserved table while trade negotiations drag on. To those who observe carefully, she never drinks from the glass, never takes notes, and her Calimshan accent slips in ways a trained ear notices (DC 14 Insight)."
> — `campaign/setting/notable-figures/bregan-daerthe/09-ryvarra.md:21` (the sentence continues with the quest-time clause in C row 6)

**First Meeting, the tell (quest text)**
> "Any character who talks with Ryvarra for a few minutes and makes a successful **DC 14 Wisdom (Insight)** check notices two things. Her Calimshan accent slips on certain words into a flatter, more precise cadence, and the wine in her glass is exactly as full as when she sat down."
> — `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:117`

**Voice profile, cover detail**
> "- **Swearing:** *Stingy · Plain · Clipped.* None in cover. In private, one cold drow curse."
> — `.claude/skills/character-voices/voices/bregan-daerthe.md:174`

### A6. Relationships (named figures)
**Harper spy at the same well (org page)**
> "- **The Harpers (neutral `[research]`):** No campaign file records contact between the two. A company observer, Ryvarra, watches the Yawning Portal's well, where the Harper spy Mattrim Mereg keeps his cover, and the Harpers keep an informant at the Sea Maidens Faire (**The Harpers**)."
> — `campaign/setting/organizations/07-bregan-daerthe.md:84`
**Castle Ward gazetteer, same room**
> "- Durnan owns it and charges standard prices. Mattrim \"Threestrings\" Mereg plays here, Bonnie pours, Davil Starsong keeps a room, and a Bregan D'aerthe observer, Ryvarra, watches the well from the balcony."
> — `campaign/gazetteer/waterdeep/castle-ward.md:45`

**Jarlaxle (employer)**
> "- **Vessa**, **Ryvarra** and **Quilm:** His operatives in the Cassalanter social circle, at the Yawning Portal and across the city, who send him intelligence."
> — `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:54`
**Nar'l and Vessa (org page, the company's placements)**
> "- **Keep an Asset Inside Every Rival:** The company is skilled at infiltrating criminal organizations, and Nar'l Xibrindas advises Xanathar while he reports to Jarlaxle by *Sending* spell. Ryvarra watches Undermountain traffic from the Yawning Portal, and Vessa sits in the Cassalanters' social circle. Jarlaxle is said to have an operative inside every major faction `[research]`."
> — `campaign/setting/organizations/07-bregan-daerthe.md:38`

**Quilm (fellow reporter)**
> "- **Gathering information:** Each nimblewright feeds a crystal ball aboard the *Scarlet Marpenoth*, so every sale is also a listening post. Nar'l reports by *Sending* spell, Ryvarra and Quilm file weekly reports, and Fenerus gathers coded messages from dead drops across the Trades Ward for Krebbyg to collect every two days."
> — `campaign/setting/organizations/07-bregan-daerthe.md:75`

**Route for the Villains page**: "Ryvarra" appears in `campaign/setting/villains/jarlaxle.md:21` and `:60`; see C.

### A7. Stat block
- Campaign, the page: "- *Drow spy (Bregan D'aerthe field observer), neutral, she/her*. Stat block: **Spy**." — `campaign/setting/notable-figures/bregan-daerthe/09-ryvarra.md:5`
- Campaign convention, a 2024 name for the block (Florette, Captain Dalloway's watchers): "Florette uses the 2024 **Spy** statistics with a shortsword and no poison, since she would not use poison in a crowded theater." — `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:259`
- Session 50/51 note on the page: "- The Notable Figures pages for Fel'rekt and Ryvarra still list the **Drow Gunslinger** and **Spy** blocks, and the first is not a 2024 name." — `campaign/quests/faction-events/bregan-daerthe/s04-contact-severed/design-notes.md:52`
- No numeric stat block (CR, HP, AC) for Ryvarra in any file read.

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, the page: "- *Drow spy (Bregan D'aerthe field observer), neutral, she/her*." — `campaign/setting/notable-figures/bregan-daerthe/09-ryvarra.md:5`
- Campaign, the org page: "- **Ryvarra** — Drow spy and field observer, neutral." — `campaign/setting/organizations/07-bregan-daerthe.md:107`
- Campaign, the First Meeting tag: "Ryvarra (Neutral, Drow, she/her) :: ..." — `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:83` (the same tag at `:73`)
- Adventure: no entry. Alexandrian: no entry.

**Species**
- "Drow" — `campaign/setting/notable-figures/bregan-daerthe/09-ryvarra.md:5`; `campaign/setting/organizations/07-bregan-daerthe.md:107`; `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:28` ("a drow woman").

**Pronouns**
- "she/her" — `campaign/setting/notable-figures/bregan-daerthe/09-ryvarra.md:5`
- "Ryvarra (Neutral, Drow, she/her)" — `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:73`
- Pronoun table, group C (research note): `docs/plans/npc-pronouns-table-group-c.md:18` (lists the same two sources).

**Ethnicity**: none sourced (drow, not a Faerûn human ethnicity). Calimshan is the cover's nation of origin, not a stated birthplace.

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/bregan-daerthe/09-ryvarra.md` (no Background, no Personality, no Connections yet).

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Drow spy (Bregan D'aerthe field observer), neutral, she/her*. Stat block: **Spy**." | Day-one (B, A7) | section B |
| 2 | L6 | "**Affiliation:** Bregan D'aerthe" | Day-one | `07-bregan-daerthe.md:107` |
| 3 | L7 | "**Featured in:** **Finding Floon**, **Trollskull Alley**" | Quest-name list. It is accurate for the two quests and omits the **Bregan D'aerthe First Meeting** (`ev-01-first-meeting.md:73`) | `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:9` |
| 4 | L11 | "Ryvarra should inspire the particular unease of someone who has been cataloguing the party since before they knew they were interesting; quiet admiration for operational patience executed over months without slipping; and retroactive dread once the party understands that every move they made in the Yawning Portal was already filed and addressed to Jarlaxle." | Mixed. "cataloguing the party since before..." and "every move they made ... was already filed" are quest-time (the party's moves, the reports naming them). "operational patience executed over months" conflicts with "two weeks" (D1). Restate as day-one, or remove the party clauses and route them | `ev-01-first-meeting.md:28`; `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:28` |
| 5 | L13 | "Ryvarra most often feels analytical detachment, the practiced stillness of someone trained to read a room without being read, professional loyalty to Jarlaxle, private curiosity about the party (they are more interesting than most of what she observes), and a controlled impatience she has not let surface in two weeks of watching the well." | Day-one except "private curiosity about the party (they are more interesting ...)", which is a quest-time reference to the party. The "two weeks" clause is day-one | `history/08-the-players-arrive.md:42` |
| 6 | L21 | "Deep down, she has been filing weekly intelligence reports to Jarlaxle since her first night in the city, and her current dispatch names the party by description, details the brawl and the troll fight, and flags them as potential long-term variables." | First clause ("filing weekly intelligence reports ... since her first night in the city") is day-one, but "weekly" conflicts with "every tenday" (D2). Second clause ("her current dispatch names the party ... the brawl and the troll fight") is quest time. Route the second clause | `ev-01-first-meeting.md:28` ("Her latest report names the party, and she tells the lieutenants where the party goes."); `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:105` (the brawl) |
| 7 | L23 | "Approached and questioned directly, Ryvarra excuses herself politely and does not return to that table. No evidence remains — her wine glass is full, her chair is straight, and no one at the adjacent tables can say what she looked like. Cornered or exposed, she fights with a drow's efficiency: targeted, fast, brutal, with every move aimed at an exit." | Encounter register, not a day-one event. It restates the First Meeting branch. Brief ruling 3 keeps Morale verbatim, but the first sentence is the First Meeting branch (`ev-01-first-meeting.md:125` and `:131`). Drafter: keep the sentence as a general habit or restate it as a day-one habit | `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:125` ("Ryvarra listens to the whole accusation with her head tilted a polite degree, and then she lays her napkin beside her plate and rises."); `:131` ("Ryvarra does not return to that table. From the next evening she sits at the far end of the balcony, and the watchers keep their shifts at the manor whatever the party says to her.") |
| 8 | L25 | "Ryvarra is a Bregan D'aerthe field observer stationed at the Yawning Portal to catalog Undermountain traffic, a weekly intelligence source for Jarlaxle's Waterdeep network, and the first evidence (retroactively understood) that Jarlaxle had eyes on the party from their first night in the city." | First two clauses are day-one ("weekly" conflicts with D2). "the first evidence (retroactively understood) that Jarlaxle had eyes on the party from their first night in the city" is quest-time framing, the same claim as `villains/jarlaxle.md:60`. Route it | `villains/jarlaxle.md:60`; `ev-01-first-meeting.md:28` |
| 9 | L29 | "A Calimshan cloth merchant who takes her evening wine at a reserved table at the Yawning Portal — she never drinks from the glass, never takes notes, and her accent slips in ways a trained ear notices." | Day-one. **36 words** (brief limit 21). Draft a shorter Overview | section A5 |
| 10 | L5 (Summary) | "- **Featured in:** **Finding Floon**, **Trollskull Alley**" | See row 3 | |

Voice profile, quest-time clauses (`.claude/skills/character-voices/voices/bregan-daerthe.md`, "### Ryvarra", lines 168-182):
- Line 171, "- **Sound:** A smooth, cultured Calishite accent that slips, now and then, into a colder, more precise drow cadence." — day-one. Spelling differs from the page's "Calimshan" (D4).
- Line 172, "- **Sentence shape:** Polite, economical merchant's small talk. She asks perfectly ordinary questions that are each part of a profile." — day-one.
- Line 173, "- **Word choice:** The cloth trade (weaves, dyes, shipping delays) and polished courtesy. She calls the party \"honoured friends\", as a merchant would." — day-one.
- Line 174, "- **Swearing:** *Stingy · Plain · Clipped.* None in cover. In private, one cold drow curse." — day-one. Adult table: the swearing stays.
- Line 175, "- **Personality in speech:** Analytical detachment. She reads a room without being read. Her curiosity about the party shows in one question too many about their fights." — "about the party" is a quest-time reference (the party's fights). Restate as "in one question too many about strangers' fights" or similar; flag.
- Line 176, "- **Quirks:** She never drinks from her glass. She compliments fabric while clearly looking at the wearer's weapons." — day-one.
- Line 177, "- **Signature phrases:** \"Negotiations are slow.\" / \"Honoured friends.\" / \"What a fascinating evening.\"" — day-one.
- Line 178, "- **Never:** She never takes notes in public, never drinks, and never admits to being anything but a merchant." — day-one.
- Line 180, sample *Greeting*: "Good evening, honoured friends. Forgive me, I couldn't help noticing the troll. Such an eventful place." — **quest time**: "the troll" is the Yawning Portal brawl and the troll (`campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md`, the bar brawl section; `sources/adventure-wdh.json:1647` "In the third round of the brawl, trouble arises from out of the gaping well in the middle of the Yawning Portal's taproom:"). Flag; the drafter needs a day-one replacement line (for example a remark on a stranger in the taproom).
- Line 181, sample *Business*: "Cloth, mostly. Silks from Calimport. And you? You fight for coin, or for something else?" — day-one.
- Line 182, sample *Under pressure*: "(the accent drops away completely) \"Sit down. You're making a scene, and I dislike scenes.\"" — encounter register, not quest time.

---

## D. Conflicts (both sides quoted, higher rank named)

**D1. How long she has watched the well**
- Campaign, the page: "a controlled impatience she has not let surface in two weeks of watching the well." — `campaign/setting/notable-figures/bregan-daerthe/09-ryvarra.md:13`
- Campaign, the page: "operational patience executed over months without slipping" — `campaign/setting/notable-figures/bregan-daerthe/09-ryvarra.md:11`
- Campaign, the First Meeting: "Ryvarra has watched the well from the Yawning Portal's balcony for three months and sends Jarlaxle a report every tenday." — `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:28`
- Campaign, Finding Floon: "She has been at that table every evening for two weeks" — `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:28`
- Campaign, the history page: "She has sat there every evening for two weeks when the party arrives, which is about Alturiak 17, 1492 DR." — `campaign/setting/history/08-the-players-arrive.md:42`
- Higher rank: the day-one history and Finding Floon agree on two weeks. The First Meeting's "three months" conflicts. The Ryvarra page's "months" (L11) also conflicts. Drafter should use two weeks.

**D2. Report cadence**
- Campaign, the page: "Ryvarra wants to file accurate weekly reports to Jarlaxle" — `campaign/setting/notable-figures/bregan-daerthe/09-ryvarra.md:15`
- Campaign, the org page: "Nar reports by *Sending* spell, Ryvarra and Quilm file weekly reports" — `campaign/setting/organizations/07-bregan-daerthe.md:75`
- Campaign, the First Meeting: "sends Jarlaxle a report every tenday" — `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:28`
- Higher rank: campaign on both sides. "Weekly" appears on the page and the org page (two sources); "every tenday" is one quest line. A tenday is a 10-day week in the Faerûn calendar, so the two differ. The `docs/plans/bregan-daerthe-research/06-consistency-pass.md:140` note reads the same conflict. Drafter must choose.

**D3. Visibility: how the party sees her**
- Finding Floon: "The party notices her only if they specifically ask who is watching the well; they get a description, nothing more." — `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:28`
- First Meeting: "any character who visits the Portal during the renovation can see her." — `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:73`
- Trollskull ev-03: "Available only to parties with drow PCs or characters who made the **Yawning Portal** Perception check." — `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:44`
- Higher rank: the Finding Floon quest journal is the first event. The ev-03 gate ("drow PCs or Perception check") is not in Finding Floon. The First Meeting says "any character". Not decided by the sources. This is quest-time mechanics, not day-one lore; it is recorded for the routed section only.

**D4. Accent spelling**
- Page: "her Calimshan accent slips in ways a trained ear notices (DC 14 Insight)" — `campaign/setting/notable-figures/bregan-daerthe/09-ryvarra.md:21`
- Voice: "A smooth, cultured Calishite accent that slips" — `.claude/skills/character-voices/voices/bregan-daerthe.md:171`
- Not a substance conflict. Drafter uses one spelling. The campaign's own usage on the page and in the First Meeting is "Calimshan" (`ev-01-first-meeting.md:117`).

**D5. Where she walks (quest time, recorded for routing)**
- Trollskull ev-03: "Ryvarra (the drow observer from the **Yawning Portal** Event) is spotted near the alley; BD surveillance is seeded" — `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:9`
- First Meeting: "where she walks through Trollskull Alley one morning to look at the manor" — `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:73`
- Finding Floon: "She is never named in this quest." — `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:28`
- Not a day-one conflict; the page says nothing about the alley. Keep it off day one.

**D6. Stat block name**
- Page: "Stat block: **Spy**." — `campaign/setting/notable-figures/bregan-daerthe/09-ryvarra.md:5`
- Session note: "- The Notable Figures pages for Fel'rekt and Ryvarra still list the **Drow Gunslinger** and **Spy** blocks, and the first is not a 2024 name." — `campaign/quests/faction-events/bregan-daerthe/s04-contact-severed/design-notes.md:52`
- Not a conflict for Ryvarra: "Spy" is the 2024 name (`m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:259`).

---

## E. Stale lines in other files (do not edit) and routed quest references

**E1. Stale or conflicting lines in other files**
- `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/design-notes.md:35`: "**Finding Floon** and **The Neighbors** disagree with each other and with the Ryvarra page about her tenure and where she is seen." (the file's own admission of D1 and D3)
- `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:28`: "three months" (D1) and "every tenday" (D2).
- `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:28`: "every evening for two weeks" (agrees with history; disagrees with the First Meeting).
- `campaign/quests/act-i/finding-floon/overview.md:27`: "- **Ryvarra** (Bregan D'aerthe) — drow field observer at the YP balcony; catalogues Undermountain traffic; unnamed in this quest" (agrees with the page).
- `campaign/setting/organizations/07-bregan-daerthe.md:75` and `:67` (cadence and placement; see D2).
- `campaign/setting/history/03-bregan-daerthes-long-road.md` and `sources/SOURCE_GUIDE.md:549` (the Alexandrian watcher claim; see A1). The PDF read does not confirm it.
- `docs/plans/bregan-daerthe-research/02-first-meeting-and-standalones.md:47` (research note) quotes the three-months conflict; it is not a campaign file and is not edited.

**E2. Labels: member, associate or contact**
- Org page places her under "Key Members" (`campaign/setting/organizations/07-bregan-daerthe.md:107`).
- Adventure, faction rule: "A character must be a drow, preferably a male, to join this faction." — `sources/adventure-wdh.json:1296`
- Adventure, non-drow rule: "Jarlaxle employs non-drow operatives as well, none of whom know they're working for him; such individuals aren't considered members of the faction." — `sources/adventure-wdh.json:1298`
- Org page, membership rule: "The non-drow operatives he employs are never counted as members." — `campaign/setting/organizations/07-bregan-daerthe.md:41`
- No source uses "member" or "associate" for Ryvarra. The Villains page calls her a "field observer" (`campaign/setting/villains/jarlaxle.md:60`). Drafter decides the label; the sources support "Bregan D'aerthe field observer" as written.

**E3. Routed quest references (quest time, not day-one)**
- `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:105`: "Bregan D'aerthe: Ryvarra at the balcony table."
- `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:46`: "Mark **Ryvarra Identified** if both checks succeed. Cross-ref the **Ryvarra** page in Notable Figures."
- `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:58`: "- **Ryvarra Identified** — mark when both the Perception and Investigation checks pass, which confirms the Bregan D'aerthe surveillance. When J.B. Nevercott arrives, the party already knows what they are dealing with. Read by **The Factions Come Calling** (ev-04), where it changes how the Bregan D'aerthe recruitment sequence opens."
- `campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:44`: "If **Ryvarra Identified** is marked, his opening shifts."
- `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:73` (the recognition text), `:85` ("Ryvarra is Friendly in manner and Indifferent in fact. She speaks in polished merchant's small talk and calls the party \"honoured friends\"."), `:117` (DC 14 Insight tell), `:125` and `:131` (the confrontation branch), `:197` ("Ryvarra stays at the Portal and keeps filing her reports, because nothing she does is against the law."), `:304` and `:466`.
- `campaign/quests/faction-events/bregan-daerthe/s04-contact-severed/ev-01-contact-severed.md:207`: "Within a tenday Ryvarra's report tells Jarlaxle that a severed character spoke with the Lords' Alliance, and he files the name beside the character's own."
- `campaign/setting/villains/jarlaxle.md:21`: "- **Ryvarra Identified.** **The Neighbors** marks this Event Outcome when both checks succeed. It changes how Nevercott opens his visit and does not change whether the visit happens."
- `campaign/setting/villains/jarlaxle.md:60` (see C row 8).
- `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:162`: "- **Routed to quests:** \"Before the party reached the hideout\" (Eye #3 paragraph) and Ryvarra as \"the first sign that he had eyes on the party from their first night in the city\" (`villains/jarlaxle.md:57`, `:60`)."

---

## F. Gaps a Background needs that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

**F1. Birth year, birth name, home, house, family, age.** None in any file read. Searched: `campaign/` (Grep "Ryvarra", "Verida" and "Calimshan"), `sources/adventure-wdh.json`, `sources/*.md`, `sources/research/`, the wiki bundle. No match. Constraint: the company's founding rule (`campaign/setting/history/03-bregan-daerthes-long-road.md:41`: "- The company was built from rogue males of destroyed houses in Menzoberranzan and Ched Nasad. ... Almost all of them are male, because female drow rarely take orders from a male.") Ryvarra is female. The rule says a female drow "can earn a place by decrying the matriarchy and convincing him she would be an asset" (`campaign/setting/villains/jarlaxle.md:46`). Any origin the drafter gives must sit inside that rule.

**F2. Former life before the company.** None. The page's only past-tense fact is "since her first night in the city" (L21).

**F3. How and when she joined.** None. The history page dates her watch to Alturiak 17, 1492 DR (`campaign/setting/history/08-the-players-arrive.md:86`); it does not date her joining.

**F4. The cover.** The sources give the cover as a Calimshan cloth merchant (`09-ryvarra.md:21`), with the trade (silks, dyes, shipping delays) in the voice profile (`bregan-daerthe.md:173`: "The cloth trade (weaves, dyes, shipping delays)") and "Silks from Calimport" (`bregan-daerthe.md:181`). Constraint: "Calimport" is her stated source of silks, not her home.

**F5. Training, skills.** The page says "a drow's efficiency" (L23). No source gives her weapon or skill list. Her stat block is "Spy" (A7).

**F6. Losses, grudges, people she cares about.** None in any file read.

**F7. Personal goals beyond the company.** None. The page's Motivations give her goals for the company (`09-ryvarra.md:15`). A goal about a craft (cloth, a trade she is practising as cover) or a place is allowed as `[design]`.

**F8. Relationship with Jarlaxle beyond "field observer".** None. Her Motivations give "professional loyalty to Jarlaxle" (`09-ryvarra.md:13`). The villains page gives only the employer link (`jarlaxle.md:60`).

**F9. Relationship with Nar'l, Soluun, Krebbyg, Fel'rekt, Quilm, Margo.** Only Quilm: "Ryvarra and Quilm file weekly reports" (`07-bregan-daerthe.md:75`). No other link is sourced.

**F10. Physical appearance.** None as a day-one fact. The quest scene gives: "a drow woman in the observation balcony, posing as a Calimshan cloth merchant, untouched glass of wine in front of her" (`ev-01-yawning-portal.md:28`). That is the scene, not a fixed description.

**F11. Where she is on Ches 1 and after.** The Yawning Portal balcony (`campaign/gazetteer/waterdeep/castle-ward.md:45`). Quest-time movements (the alley, the Trollskull visit) are not day-one facts.

---

## G. Source facts that hint at the figure's inner life (do not contradict)

- Page: "Ryvarra should inspire ... quiet admiration for operational patience executed over months without slipping" (`campaign/setting/notable-figures/bregan-daerthe/09-ryvarra.md:11`) (note D1 on "months").
- Page: "a controlled impatience she has not let surface in two weeks of watching the well" (`09-ryvarra.md:13`).
- Page: "private curiosity about the party (they are more interesting than most of what she observes)" (`09-ryvarra.md:13`) (quest-time flavor; flagged in C row 5).
- Page: "Ryvarra wants to file accurate weekly reports to Jarlaxle on Undermountain traffic, maintain her cover as a Calimshan cloth merchant for as long as operationally viable, and avoid any action that would compromise Bregan D'aerthe's Waterdeep network." (`09-ryvarra.md:15`).
- Page: "Deep down, she has been filing weekly intelligence reports to Jarlaxle since her first night in the city" (`09-ryvarra.md:21`) (day-one clause).
- Voice, day-one: "She never takes notes in public, never drinks, and never admits to being anything but a merchant." (`.claude/skills/character-voices/voices/bregan-daerthe.md:178`).
- Voice, day-one: "Analytical detachment. She reads a room without being read." (`bregan-daerthe.md:175`).
- Voice, sample: "Cloth, mostly. Silks from Calimport. And you? You fight for coin, or for something else?" (`bregan-daerthe.md:181`).
- Quest text, day-one: "Ryvarra is Friendly in manner and Indifferent in fact." (`ev-01-first-meeting.md:85`) and "When a question turns toward her, she answers with a detail about cloth and asks something back." (`ev-01-first-meeting.md:85`).
- Quest text: "She never drinks from her glass and never writes anything down in public." (`ev-01-first-meeting.md:85`).

---

## Not found

- Birth year, birth name, home, house, family, age, date of joining, former life, faith, losses, grudges, weapon, training, appearance (fixed). Searched: `campaign/` (Grep for "Ryvarra" and "Verida", and for "Calimshan" and "cloth merchant"; the Grep result was over 23 KB, read in full from the saved output), `sources/adventure-wdh.json` (Grep "Ryvarra", "Calimshan", "cloth", "balcony", "observer"), `sources/SOURCE_GUIDE.md`, `sources/*.md` (Grep), `sources/research/` (Grep, including the pass 3, 4 and 5 bundles), `docs/` (Grep, for planning notes only).
- Alexandrian watcher in the Yawning Portal: `SOURCE_GUIDE.md:549` says the First Impressions addendum has one. The PDF pages read (PDF pp.1-4, printed pp.162-165) do not. Not read: the rest of `sources/23. Addendum First Impressions.pdf` (the file has four pages; all four were read, so nothing further).
- Alexandrian PDFs not read for Ryvarra: `sources/1. The Villains.pdf` (only p.5 read in another note), `sources/3. Player Character Factions.pdf`, `sources/26. Addendum Other Collaborators.pdf`. Not read: `sources/27. Addendum A Night in Trollskull Manor.pdf` beyond PDF pp.1-12 (printed pp.178-189). PDF pp.5-12 (the Patron Table, the Topics and Agendas, and the Jarlaxle topic) contain no Ryvarra.
- Wiki: `NOT FOUND` (wiki extract for Ryvarra; the scratchpad file contains only that line). The pass 5 Bregan D'aerthe wiki bundle has no Ryvarra match (Grep).
- The adventure has no Ryvarra. The Yawning Portal section (`sources/adventure-wdh.json:1465`) has no drow watcher.

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. `sources/SOURCE_GUIDE.md:690` lists `Jarlaxle Baenre NPC Guide.docx`; not checked for Ryvarra.
- `sources/Other remix files/` also holds other `.docx` guides that may name a Yawning Portal watcher; not opened.
- PDFs read as images: transcriptions only. `pdftotext -layout` check needed before any quote goes into prose.
