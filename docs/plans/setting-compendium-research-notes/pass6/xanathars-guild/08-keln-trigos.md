# Pass 6 research notes: Keln Trigos

Page: `campaign/setting/notable-figures/xanathars-guild/08-keln-trigos.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Instructions: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/pass6-researcher-instructions.md`

Method and caveats:
- Campaign files: Read and Grep, quoted from the file. Line numbers are from tool output.
- Published adventure: `sources/adventure-wdh.json`. No line names Keln, Trigos, the Terasse Estate, Elsambul's Lane or a Guild passphrase (grep, all forms). The only Guild gathering line in it is the sewer staircase (quoted in A9).
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. Every PDF quote below was transcribed from the rendered page image. Cite as printed page with PDF page in brackets. Check exact wording with `pdftotext -layout` before any quote goes into prose. PDFs read in full: `sources/5. Faction Outposts.pdf` (PDF pp.1 to 13, printed pp.36 to 48); `sources/11. Lair  Xanathar’s Lair.pdf` (PDF pp.1 to 9, printed pp.83 to 91). `sources/17. Outpost and Lair Revelation Lists.pdf` read at PDF pp.1 to 3 (printed pp.121 to 123); the Xanathar section ends on printed p.123, and later pages were not read.
- Wiki: there is no Keln Trigos wiki page. `scratchpad/wiki-xg/Keln_Trigos.txt` reads "NOT FOUND". A search of every `sources/research/**` file for Keln, Trigos, Terasse, Elsambul, Tiefling priest and healer returned no wiki.txt hit (the hits are campaign snapshots in `campaign-hits.txt` files). The Xanathar guild wiki (`sources/research/pass5-bundles/xanathars-guild/wiki.txt`) has no Terasse, clinic, estate or outpost line.
- Source rank used: campaign files, then the published adventure (no Keln content), then the Alexandrian PDFs and appendices, then the wiki (no Keln content).
- No file was edited except this notes file. The page was not written.

## Key findings for the drafter

- **The "Tier 1 outpost keeper" label has no source.** It appears only on the target page at line 25. No file uses "Tier 1" for an outpost or a person. In the campaign, "Tier" numbers the escalation tiers and starts at 2 (Suspicious), 3 (Alert) and 4 (Lockdown) (`campaign/structure/arc-e-faction-outposts.md:155`, `:171`, `:213`; `campaign/guides/factions/10-manshoons-zhentarim.md:31`). The Unaware tier has no number in `campaign/guides/gm-guide/running-the-villains.md:47`. An older Guild page Contacts line also used the words "(outpost keepers)" (quoted at E2). The current Guild page no longer uses them.
- **Day-one core, supported by the campaign files and the Alexandrian PDF:** Keln is a tiefling priest, neutral evil, who runs the Terasse Estate, a rowhouse on Elsambul's Lane in the Castle Ward. The estate offers healing behind a passphrase and is also a gladiatorial gathering point. The campaign and the PDF agree on this.
- **Quest-time material on the page:** the "outpost keeper" and "Tier 1" label, the Morale line that has Keln send a message to Xanathar (this is the Faction Outposts Getaway step, `campaign/structure/arc-e-faction-outposts.md:155`), and the "gladiatorial transport route" manager line (no source gives Keln that role; see D6).

---

## A. Background facts by theme

### A1. Origin, family, former life, birth

No source gives any of these. Searched: Keln, Trigos and "tiefling" across `campaign/`, `sources/` (adventure, Appendices B to D, Act III Arc E, SOURCE_GUIDE), `docs/` and the wiki bundles. Only the entries below exist.

> "- **Keln Trigos** — Tiefling priest (Xanathar's Guild), neutral evil. Stationed at the Terasse Estate. Provides healing for the Guild's agents and manages the audience that gathers there for the gladiatorial fights. See the **Keln Trigos** page in Notable Figures."
> — `campaign/setting/organizations/08-xanathars-guild.md:107` (Key Members). This is the only Key Members line that gives a role. No line gives an origin.

See F1.

### A2. How he joined the Guild and rose in it

No Keln-specific entry. The general membership test is the only sourced route:

> "- **Crime Is the Entry Fee:** Anyone can join, but an applicant must first pass a test that always involves a serious crime. The crime might be murdering a member who failed Xanathar, kidnapping a Waterdhavian, collecting a ransom or looting a warehouse. After that, advancement depends on wiles and on the ability to dispose of rivals, and the competition is fierce and often deadly."
> — `campaign/setting/organizations/08-xanathars-guild.md:32`

The published ranks are listed as "The published ranks for members, from lowest to highest, are Eyestalker, Agent of the Eye, Eye Ray, Guild Boss and Hand of the Eye" (`campaign/setting/organizations/08-xanathars-guild.md:45`). Keln is not placed on the ladder anywhere.

Role labels, by source:
> "***Roster.*** Keln Trigos (**priest**) + 2 **guards** + 3 Guild agents (**thug** stat block)."
> — `campaign/guides/factions/09-xanathars-guild.md:33` (Terasse Estate entry, Roster)

> "*Step 5 — Getaway.* Keln Trigos (priest) and his guards raise the alarm when any objective area is breached: the trap door seals from below, the front door bars, and a flying snake courier carries word to the Lair."
> — `campaign/structure/arc-e-faction-outposts.md:155` (Faction Outposts, Step 5; quest-state, see C)

> "It is occupied by a Xanatharian operative named Keln Trigos, a tiefling **priest** (MM p. 348)."
> — Alexandrian `sources/5. Faction Outposts.pdf`, printed p.42 [PDF p.7] (transcribed from image; check with pdftotext)

> "He reports to a Xanathar Guild lieutenant named Keln Trigos at the Terasse Estate on Elsambul's Lane — an address that will become relevant in the Grand Game investigation."
> — `sources/Appendix_C_-_Player_Faction_Missions.md:116` (Arc H-1 "The Talking Mare", Scene 5; quest text, see D2)

> "- **Contacts:** **Ahmaergo**, **Keln Trigos** (Guild contacts in the city); **Grinda Garloth** (independent contractor); **Gorath**, **Korgstrod Uxgulm**, **Noska Ur'gray** (field leaders)"
> — `campaign/setting/organizations/08-xanathars-guild.md:8` (Gamemaster's Summary)

No source gives a date for when he joined, when he was posted to the estate, or whether he rose in rank (F3, F4).

### A3. What he runs (day-one)

Gazetteer, the setting page for the ward:
> "- A rowhouse clinic on Elsambul's Lane that asks no questions about injuries. Keln Trigos (Neutral Evil, Tiefling, he/him) runs it and asks no questions about how his patients were hurt."
> — `campaign/gazetteer/waterdeep/castle-ward.md:85` (Terasse Estate, Life in the Ward)

> "- Keln keeps the Terasse outpost for Xanathar's Guild. He holds two passphrases: one opens the clinic's gladiator transport route, and the other opens the route to the Lair."
> — `campaign/gazetteer/waterdeep/castle-ward.md:90` (GM Notes callout)

Guild organization page:
> "- **Terasse Estate.** A rowhouse on Elsambul's Lane in the Castle Ward that Xanathar secretly owns. Keln Trigos runs a healing operation on its upper floors, and the cellar is one of the city's gathering points for the gladiatorial fights, with a trapdoor under the kitchen rug that leads to an underground dock and on to Skullport (**Castle Ward**; **Xanathar's Guild** in the Factions Guide)."
> — `campaign/setting/organizations/08-xanathars-guild.md:55` (under "**The three outposts.**", line 53)

Factions Guide, Terasse Estate entry:
> "A modest rowhouse secretly owned by Xanathar, the Terasse Estate operates on two levels — both under the same roof, both accessible by passphrase, and neither officially connected. Keln Trigos runs a healing operation for Guild agents on the upper floors. Below it, the estate serves as one of Waterdeep's gladiatorial gathering points: those who want to attend the fights in Xanathar's Lair report here; staff ply them with exotic food, then blindfold them and escort them through an underground dock to caverns near Skullport."
> — `campaign/guides/factions/09-xanathars-guild.md:21` (the rest of the Terasse entry covers the Areas; see A4 and A6)

Alexandrian, printed p.42 [PDF p.7]:
> "TERASSE ESTATE (Castle Ward, Elsambul's Lane): The Terasse Estate is a modest rowhouse residence in the Castle Ward which is secretly owned by Xanathar. It is occupied by a Xanatharian operative named Keln Trigos, a tiefling **priest** (MM p. 348). Keln sometimes provides healing services to injured Xanatharians, but the house is more notable because it's a designated gladiatorial gathering point: Those who wish to attend the gladiatorial combats in Xanathar's Lair must go to one of these gathering points (there are several throughout the city, some heading through the sewers to X1, others following the route described below) in order to be escorted, as a group, to the games (and back)."
> — `sources/5. Faction Outposts.pdf`, printed p.42 [PDF p.7] (transcribed from image; "the gladiatorial combats" wording to be checked)

### A4. Passphrases and the two services

Factions Guide, Area 1:
> "**Area 1 — Front Door.** Two passphrases control entry. For healing services: "I heard the red hand was hot." For gladiatorial gatherings: "the bawdy star shines bright tonight.""
> — `campaign/guides/factions/09-xanathars-guild.md:23`

Structure doc, Step 2:
> "*Step 2 — Case the Target.* A modest, unremarkable rowhouse. Two kinds of visitors come: those seeking healing (legitimate front), and those attending gladiatorial events in Xanathar's Lair. Two passphrases control entry: "I heard the red hand was hot" accesses the healing operation; "the bawdy star shines bright tonight" gets a guest past the front rooms."
> — `campaign/structure/arc-e-faction-outposts.md:149`

Alexandrian, printed p.42 [PDF p.7]:
> "Area 1 – Front Door: Those coming to the Terasse Estate must give a specific knock and an accompanying pass-phrase to be given entrance. There are two different combinations, one for healing services ("I heard the red hand was hot") and another for the gladiatorial gatherings ("the bawdy star shines bright tonight")."

Gazetteer (conflicts with the above; see D4):
> "- Keln keeps the Terasse outpost for Xanathar's Guild. He holds two passphrases: one opens the clinic's gladiator transport route, and the other opens the route to the Lair."
> — `campaign/gazetteer/waterdeep/castle-ward.md:90`

### A5. Faith

No deity is named for Keln in any file. The only faith-adjacent words are his title and his spell use:
> "In a fight, Keln uses priestly spells to hold ground, calls his guards, and sends a message to Xanathar. He does not run — the building is his responsibility."
> — `campaign/setting/notable-figures/xanathars-guild/08-keln-trigos.md:23` (Morale; the spells are not named)

Keln is not in `campaign/setting/deities/` (no hit). Grep for Keln across `campaign/` returns no deity page. See F2.

### A6. Places, belongings and daily work

Alexandrian, Areas 3, 4 and 6-7 (printed pp.42-43 [PDF pp.7-8]):
> "Area 3 – Kitchen: A large rug of reddish scales covers the floor here. This can be thrown back to reveal a trap door with a narrow staircase leading down to an underground dock. Those heading to the gladiatorial gatherings will be blindfolded before being led down the stairs, and the blindfolds will remain in place until the boat arrive at another secret dock in the caverns near Skullport. This dock connects to a passage which intersects the one leading from Area X4 of Xanathar's Lair to the Guts & Garter in Skullport."
> — `sources/5. Faction Outposts.pdf`, printed p.42 [PDF p.7] / printed p.43 [PDF p.8] (transcribed from image; the Area 3 entry is on printed p.43)

> "Area 4 – Storeroom: Trigost's larder and healing supplies."
> — Alexandrian, printed p.43 [PDF p.8] (the source spells the name "Trigost's")

> "Area 6-7 – Master Suite: This is Trigos' bedchamber, with walk-in closet."
> — Alexandrian, printed p.43 [PDF p.8]

> "Desk: Trigos has a variety of expensive stationaries and writing utensils for performing his correspondence, but he also hs a burn-pot that he obviously uses to destroy that correspondence on a regular basis."
> — Alexandrian, printed p.43 [PDF p.8] ("hs" is the source's typo; the "he" pronoun is in this sentence)

> "Areas 8-10 – Sick Rooms: These bedrooms are used by Xanatharian agents who come to Trigos for his healing arts."
> — Alexandrian, printed p.43 [PDF p.8]

Factions Guide, Area 6-7 and Area 5:
> "**Area 6–7 — Master Suite.** Keln's desk holds *Instructions for Gladiatorial Weaponry* from Ahmaergo: a shipment of exotic weapons is being sent by Grinda Garloth for the next gladiatorial audience."
> — `campaign/guides/factions/09-xanathars-guild.md:29`

> "**Area 5 — Upper Landing.** A tapestry depicting a stylized beholder with humanoids bowing before it hangs on the wall. The hanging logbook (*Injury Reports*) records patients under pseudonyms; one recent entry notes that an arrow wound was the result of "incautious observation of the windmill on Coachlamp Lane.""
> — `campaign/guides/factions/09-xanathars-guild.md:27` (the logbook is not stated to be Keln's; "patients under pseudonyms" is the source's wording)

### A7. Who he treats, and the Guild's view of him

> "Keln Trigos runs a quiet healing clinic in a Castle Ward rowhouse, offering professional medical care with no questions asked about how you got hurt."
> — `campaign/setting/notable-figures/xanathars-guild/08-keln-trigos.md:29` (Overview)

Guild page, on who the Guild kills and when:
> "- **Underlings Are Disposable:** Xanathar disposes of underlings it no longer trusts in its gladiatorial arena, in a manner it finds entertaining. Whenever it flies into a rage it tends to kill random minions (*Dragon Heist*, 5e). The wiki adds that in 1492 DR members can be killed at any time at the beholder's whim (Forgotten Realms Wiki, *Xanthar's Thieves' Guild*, 5e)."
> — `campaign/setting/organizations/08-xanathars-guild.md:34`

This is the only sourced basis for the Persona's "what happens to people the Guild stops using" (see C and F9).

### A8. Relationships to named figures

**Ahmaergo** (letters to Keln):
> "**Area 6–7 — Master Suite.** Keln's desk holds *Instructions for Gladiatorial Weaponry* from Ahmaergo: a shipment of exotic weapons is being sent by Grinda Garloth for the next gladiatorial audience."
> — `campaign/guides/factions/09-xanathars-guild.md:29`

Alexandrian, printed p.43 [PDF p.8]:
> "One recent bit of correspondence he hasn't had a chance to reply to yet, however, is Instructions for Gladiatorial Weaponry: "The shipment of special weapons that X requested will be sent by Grinda Garloth in Mistshore. See that they're bundled up and sent along with the next audience procession. -Ahmaergo" (GM Note: If it becomes notable, this is simple a bunch of vicious-looking oddities — many of them foreign weapons from distant lands — destined for the gladiatorial combats.)"
> — `sources/5. Faction Outposts.pdf`, printed p.43 [PDF p.8] (transcribed from image)

Ahmaergo's role on the Guild page:
> "Ahmaergo handles logistics: gladiatorial procurement, outpost resupply, discipline. Most orders that bear Xanathar's name are written by Ahmaergo."
> — `campaign/setting/organizations/08-xanathars-guild.md:101` (Key Members)

**Grinda Garloth** (supplier to the estate):
> "**Area D2 — Grinda's Chest.** 500 gp and the *Note Regarding Gladiatorial Weaponry* from Ahmaergo, confirming the weapon delivery to Terasse Estate and citing Xanathar's expectation of "exotic gutting.""
> — `campaign/guides/factions/09-xanathars-guild.md:43`

**Gorath, Korgstrod Uxgulm, Noska Ur'gray** (escalation):
> "***Escalation.*** Xanathar moves to Suspicious (Tier 2). If a second Xanathar outpost has already been hit, it moves directly to Alert (Tier 3), and Gorath's team deploys within 2 days to the last known party location. **Founders' Day Clock: 2–4 days.**"
> — `campaign/guides/factions/09-xanathars-guild.md:35`
(No source names any working link between Keln and Gorath, Korgstrod or Noska. Gorath's team is the response to the Terasse outpost; see E3.)

**Xanathar** (the gladiatorial audience):
> "**Gladiatorial fights.** The arena in the lair holds tournaments before an audience, and the Terasse Estate is one of the places where that audience gathers. The games continue because the arena revenue continues (see GM Notes)."
> — `campaign/setting/organizations/08-xanathars-guild.md:73`

**Vosk** (a Guild spy whose report reaches Keln; quest text, see D2 and D9):
> "Unknown to Maxeene — and to the party, unless they notice — a Xanathar Guild **Spy** named Vosk has been watching Maxeene for the past three days."
> — `sources/Appendix_C_-_Player_Faction_Missions.md:110` (Arc H-1, Scene 5)

**Harko** (a cipher note from a Guild courier, "K"; quest text):
> "**Harko's Coat.** In the inside left pocket is a folded note written in Xanathar Guild cipher."
> — `sources/Appendix_C_-_Player_Faction_Missions.md:519` (Arc LA-2, "Finding Harko")
> "The decoded contents identify two upcoming "disruption targets" — a specific intersection in the Trades Ward and a named warehouse in the Dock Ward — and reference a Guild contact by the letter K, meeting "at the eastern staircase" at a time that is two days away. K is Keln Trigos, based at the Terasse Estate on Elsambul's Lane."
> — same line `:519` (the decoded note is quest content; the sentence about the decoded contents is the second quote)

No source links Keln to Nar'l Xibrindas, Nihiloor, Ott Steeltoes, Thorvin Twinbeard or Noska Ur'gray. Searched by folder: `campaign/setting/notable-figures/xanathars-guild/` names Keln only in its own page and in `02-ahmaergo.md:134` (routed).

### A9. The lair route and the sewer staircase (adventure, day-one)

The published adventure gives the lair's entrance as the Castle Ward sewer staircase and does not name the estate:
> "Bregan D'aerthe knows that the safest route to the beholder's lair is a secret staircase in the sewers of the Castle Ward."
> — `sources/adventure-wdh.json:15149` (the same JSON string continues with Nar'l and the Bregan D'aerthe source; the grep output cut the line's opening)

> "Characters are most likely to enter {@creature Xanathar|WDH}'s lair by this route: a spiral staircase accessible from the Castle Ward's sewers and hidden behind a secret door."
> — `sources/adventure-wdh.json:17063`

### A10. Access to the gathering points (Lair, printed pp.83 and 86)

> "Throughout the festival season, Xanathar hosts gladiatorial games every 2-4 days. As noted in Part 3B, those interested in attending the fights must learn the secret pass phrases and go to gladiatorial gathering points throughout the city."
> — Alexandrian `sources/11. Lair  Xanathar’s Lair.pdf`, printed p.83 [PDF p.1] (transcribed from image)

> "Entrance: Generally speaking, there are three methods of entry to Xanathar's Lair. You can come in the secret entrance (X1), you can try to sneak in from Skullport (X4), or you can be brought in as part of the audience for the gladiatorial games (also via X4, but almost certainly arriving in X6 before you'll have a chance to slip away)."
> — Alexandrian Lair, printed p.86 [PDF p.4] (transcribed from image; the Keln estate is not named in the Lair PDF)

---

## B. Alignment, species, pronouns, stat block

**Alignment: neutral evil** (no conflict)
- Current page: "*Tiefling priest (Xanathar's Guild), neutral evil, he/him*. Stat block: **Priest**." — `campaign/setting/notable-figures/xanathars-guild/08-keln-trigos.md:5`
- Gazetteer: "Keln Trigos (Neutral Evil, Tiefling, he/him)" — `campaign/gazetteer/waterdeep/castle-ward.md:85`
- Guild page: "- **Keln Trigos** — Tiefling priest (Xanathar's Guild), neutral evil." — `campaign/setting/organizations/08-xanathars-guild.md:107`
- Alexandrian, Lair, Outposts and Revelation Lists: no alignment given.
- Adventure: no Keln line.

**Species: Tiefling** (no conflict)
- Current page: "*Tiefling priest ...*" — `08-keln-trigos.md:5`
- Gazetteer: "Tiefling" — `castle-ward.md:85`
- Guild page: "Tiefling priest" — `08-xanathars-guild.md:107`
- Alexandrian: "a tiefling **priest** (MM p. 348)" — printed p.42 [PDF p.7]

**Pronouns: he/him** (no conflict)
- Current page: "he/him" — `08-keln-trigos.md:5`
- Gazetteer: "he/him" — `castle-ward.md:85`
- Alexandrian: "he" in the Desk entry ("he obviously uses to destroy that correspondence", printed p.43 [PDF p.8]); "his correspondence" and "his healing arts" in the same pages.
- Pronoun table: `docs/plans/npc-pronouns-table-group-c.md:34` (lists the same two sources).

**Stat block: Priest** (label consistent; edition unclear)
- Current page: "Stat block: **Priest**." — `08-keln-trigos.md:5`
- Factions Guide: "***Roster.*** Keln Trigos (**priest**) + 2 **guards** + 3 Guild agents (**thug** stat block)." — `campaign/guides/factions/09-xanathars-guild.md:33`
- Structure doc: "Keln Trigos (priest)" — `campaign/structure/arc-e-faction-outposts.md:155`
- Alexandrian: "a tiefling **priest** (MM p. 348)" — printed p.42 [PDF p.7]. The source prints "MM" with no edition. The orchestrator should confirm which Monster Manual page 348 belongs to before the stat block is cited.
- The Lair PDF's stat reference (printed p.91 [PDF p.9]) does not list the priest. Its list includes "Ott Steeltoes – dwarf cultist, MM p. 345 (DH p. 214)" and does not include Keln.

**Affiliation: Xanathar's Guild** (no conflict)
- Current page: "**Affiliation:** Xanathar's Guild" — `08-keln-trigos.md:6`
- Guild page: "Tiefling priest (Xanathar's Guild)" — `08-xanathars-guild.md:107`
- Gazetteer: "keeps the Terasse outpost for Xanathar's Guild" — `castle-ward.md:90`
- Group folder: `campaign/setting/notable-figures/xanathars-guild/`.

**Species, adventure**: none.

---

## C. Sentences on the current page

Current page: `campaign/setting/notable-figures/xanathars-guild/08-keln-trigos.md`. "Day-one" means the sentence has a source and no quest gate is needed. "Quest-time" means it narrates a breach, a route, a rescue or an event.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Tiefling priest (Xanathar's Guild), neutral evil, he/him*. Stat block: **Priest**." | Day-one. Consistent (B). | `08-xanathars-guild.md:107`; `castle-ward.md:85`; Alexandrian p.42 |
| 2 | L6 | "**Affiliation:** Xanathar's Guild" | Day-one. | `08-xanathars-guild.md:107` |
| 3 | L7 | "**Featured in:** **Faction Outposts**, **Xanathar's Lair**" | Quest references. Faction Outposts: `campaign/structure/arc-e-faction-outposts.md:143` to `:157` (4A). Xanathar's Lair: `campaign/structure/arc-f-xanathars-lair.md:337` (Scene 4, the Terasse outpost) and `:339` (Notable Figures list). Keln does not appear in the Lair PDF text or rosters (printed pp.83 to 91 read). See D8. | as stated |
| 4 | L11 | "**Resonance.** Keln should inspire surface comfort with his healer's professional warmth; growing unease as the clinic's real purpose becomes clear; and cold realization that the blindfolded guests never ask where they are going." | Day-one. "blindfolded guests" is in the Factions Guide. | `campaign/guides/factions/09-xanathars-guild.md:21`; Alexandrian p.43 (Area 3) |
| 5 | L13 | "**Emotions.** Keln most often feels efficient professional pride, the specific calm of someone who has decided knowing less is safer, practical care for the patients he actually heals, and clinical indifference to what happens after they leave his care." | Day-one. RP text; the clinic's no-questions stance is sourced. | `castle-ward.md:85` ("runs it and asks no questions about how his patients were hurt") |
| 6 | L15 | "**Motivations.** Keln wants to run the Terasse Estate operation smoothly, provide Xanathar with a reliable healing and transport service, and avoid becoming interesting to anyone with authority." | Day-one for the estate and healing. "transport service" is not Keln's role in any source (D6). | `campaign/guides/factions/09-xanathars-guild.md:21` (blindfolding is done by "staff") |
| 7 | L17 | "**Inspirations.** When playing Keln, channel Nucky Thompson (*Boardwalk Empire*), Dr. Jacoby (*Twin Peaks*, the professional with a sideline), and the coroner in any crime procedural who is more helpful than he ought to be." | Not a fact. Keep as the GM block. | n/a |
| 8 | L21 (a) | "**Persona.** To the world, Keln Trigos runs a quiet healing operation in a Castle Ward rowhouse and asks no questions about how you got hurt." | Day-one. | `castle-ward.md:85` |
| 9 | L21 (b) | "To those who know the passphrases, the building runs two entirely separate services that have never been officially linked, and both function without incident." | Day-one in substance. "never been officially linked" paraphrases "neither officially connected". | `campaign/guides/factions/09-xanathars-guild.md:21` ("both accessible by passphrase, and neither officially connected") |
| 10 | L21 (c) | "Deep down, he has worked for Xanathar long enough to understand what happens to people the Guild stops using, and he is therefore very reliable." | Day-one attitude. The basis ("what happens to people the Guild stops using") has a partial source; "long enough" has none. | `campaign/setting/organizations/08-xanathars-guild.md:34` ("Underlings Are Disposable"); no source for his tenure (F4, F9) |
| 11 | L23 (a) | "In a fight, Keln uses priestly spells to hold ground, calls his guards, and sends a message to Xanathar." | Mixed. "calls his guards" follows the Factions Guide roster (2 guards). "sends a message to Xanathar" is the Faction Outposts Getaway, a quest-state breach response. "priestly spells" has no source. | Guards: `campaign/guides/factions/09-xanathars-guild.md:33`. Message: `campaign/structure/arc-e-faction-outposts.md:155` ("a flying snake courier carries word to the Lair"). Spells: none (F7). |
| 12 | L23 (b) | "He does not run — the building is his responsibility." | No source. | none (F8) |
| 13 | L25 (a) | "**Relationships.** Keln is the Tier 1 outpost keeper of Xanathar's Guild (Terasse Estate, Elsambul's Lane, Castle Ward)," (line 25 continues in rows 14 and 15) | "Tier 1" is unsourced (Key findings; D1). "outpost keeper" is an old Guild Contacts label (E2). The estate, lane and ward are day-one (B, A3). | `castle-ward.md:90` ("keeps the Terasse outpost"); `08-xanathars-guild.md:55` |
| 14 | L25 (b) | "the manager of the gladiatorial transport route (healing services and Lair access under the same roof)," | Quest-adjacent and unsourced for Keln. The Factions Guide gives the blindfolding to "staff". "healing services and Lair access under the same roof" paraphrases the Factions Guide's "both under the same roof". | `campaign/guides/factions/09-xanathars-guild.md:21` ("both under the same roof"; "staff ply them with exotic food, then blindfold them"); D6 |
| 15 | L25 (c) | "and the keeper of two passphrases that access very different services." | Day-one. The passphrases are the estate's. "keeper" is the gazetteer's word for holding them ("He holds two passphrases"). | `castle-ward.md:90`; `campaign/guides/factions/09-xanathars-guild.md:23` (two services, D4) |
| 16 | L29 | "Keln Trigos runs a quiet healing clinic in a Castle Ward rowhouse, offering professional medical care with no questions asked about how you got hurt." | Day-one. Overview is 25 words; the brief caps it at 21 (drafter). | `castle-ward.md:85` |

**Voice profile (`.claude/skills/character-voices/voices/xanathars-guild.md`, `### Keln Trigos` at line 137)**: checked line by line for quest-time clauses. None found. Each line is day-one or RP text:
- Line 138 tagline: "*A warm, professional healer who asks no questions and has made very sure he never learns the answers.*"
- Line 143, Swearing: "*Stingy · Plain · Clipped.* Once, quietly, when a patient dies on his table." (a patient's death, not a Faction Outposts event; day-one habit)
- Line 146, Signature phrases: "\"No need to tell me.\" / \"You'll mend.\" / \"That's not my department.\""
- Line 147, Never: "He never asks how anyone was hurt, never mentions the blindfolded guests, and never becomes interesting to the Watch."
- Line 150, Sample line, Business: "\"Healing is fifty gold. The other matter isn't my department; you'll want the back door.\"" (the price has no other source; F6)
- Line 151, Sample line, Under pressure: "\"I just heal people. Whatever this is, it's not my department.\""
The profile has no "Tier", no breach, no capture and no Event Outcome. No profile change is needed for ruling 1.

---

## D. Conflicts

**D1. "Tier 1 outpost keeper" against no source**
- Current page: "Keln is the Tier 1 outpost keeper of Xanathar's Guild" — `08-keln-trigos.md:25`
- The campaign's only Tier numbers are escalation tiers: "**Escalation: Xanathar moves to Suspicious (Tier 2).**" — `campaign/structure/arc-e-faction-outposts.md:155`; "***Escalation.*** Xanathar moves to Suspicious (Tier 2)." — `campaign/guides/factions/09-xanathars-guild.md:35`
- Higher source: none supports "Tier 1" for a person or an outpost. Drop the phrase. The gazetteer's "keeps the Terasse outpost" (`castle-ward.md:90`) is the only campaign support for "keeper" and "outpost".

**D2. Role labels**
- Priest: "Keln Trigos (**priest**)" — `campaign/guides/factions/09-xanathars-guild.md:33`; "Tiefling priest" — `campaign/setting/organizations/08-xanathars-guild.md:107`
- Operative: "a Xanatharian operative named Keln Trigos" — Alexandrian printed p.42 [PDF p.7]
- Lieutenant: "a Xanathar Guild lieutenant named Keln Trigos" — `sources/Appendix_C_-_Player_Faction_Missions.md:116` (quest text, Arc H-1)
- Guild contact: "Keln Trigos (Guild contacts in the city)" — `campaign/setting/organizations/08-xanathars-guild.md:8`
- Higher source: the campaign (priest, `08-xanathars-guild.md:107` and `factions/09-xanathars-guild.md:33`). "lieutenant" in Appendix C is a quest mission's aside; the orchestrator decides whether it matters.

**D3. Location: Castle Ward against the Dock Ward**
- Castle Ward: "A rowhouse on Elsambul's Lane in the Castle Ward" — `campaign/setting/organizations/08-xanathars-guild.md:55`; "(Castle Ward, Elsambul's Lane)" — `campaign/guides/factions/09-xanathars-guild.md:17`; "*Castle Ward, Elsambul's Lane.*" — `campaign/structure/arc-e-faction-outposts.md:145`; Alexandrian printed p.42 [PDF p.7]; Appendix C: "the Terasse Estate on Elsambul's Lane" — `sources/Appendix_C_-_Player_Faction_Missions.md:116`.
- Dock Ward: "the location of one Guild outpost in the Dock Ward — the Terasse Estate's side entrance on Copper Alley, used for weapons transfers." — `sources/Appendix_C_-_Player_Faction_Missions.md:660` (Arc LA-4, "The Rooftop Assassin", the offer of Ziraj the Hunter, a Doom Raiders operative; the line is his offer, not a campaign ruling). Copper Alley appears in no campaign file.
- Higher source: the campaign (Castle Ward, Elsambul's Lane; `castle-ward.md:85`). The Appendix line is a quest-time offer. The page keeps the Castle Ward.

**D4. What the passphrases open**
- Gazetteer: "one opens the clinic's gladiator transport route, and the other opens the route to the Lair." — `campaign/gazetteer/waterdeep/castle-ward.md:90`
- Factions Guide: "For healing services: "I heard the red hand was hot." For gladiatorial gatherings: "the bawdy star shines bright tonight."" — `campaign/guides/factions/09-xanathars-guild.md:23`
- Structure doc: "gets a guest past the front rooms" (the gladiatorial passphrase, in full in A4) — `campaign/structure/arc-e-faction-outposts.md:149`
- Alexandrian: "one for healing services ("I heard the red hand was hot") and another for the gladiatorial gatherings ("the bawdy star shines bright tonight")" — printed p.42 [PDF p.7]
- Higher source: the Factions Guide, the structure doc and the Alexandrian agree: the second passphrase opens the gathering, not the Lair route. The gazetteer's wording is the outlier. The orchestrator decides which to follow for the page; the page's Persona (`08-keln-trigos.md:21`) follows neither exactly.

**D5. Who the healing is for**
- "Keln Trigos runs a healing operation for Guild agents on the upper floors." — `campaign/guides/factions/09-xanathars-guild.md:21`; "Provides healing for the Guild's agents" — `campaign/setting/organizations/08-xanathars-guild.md:107`
- "Keln sometimes provides healing services to injured Xanatharians" — Alexandrian printed p.42 [PDF p.7]
- "A rowhouse clinic on Elsambul's Lane that asks no questions about injuries." — `campaign/gazetteer/waterdeep/castle-ward.md:85`; the page's Overview (`08-keln-trigos.md:29`) and Persona (`:21`) follow the gazetteer.
- Higher source: campaign. Two campaign files say "Guild agents" (factions and org) and the gazetteer says a public clinic. The orchestrator decides. The entry rule (a passphrase, Alexandrian printed p.42) suits the public-clinic version.

**D6. The transport role**
- Current page: "the manager of the gladiatorial transport route" — `08-keln-trigos.md:25`; Motivations: "provide Xanathar with a reliable healing and transport service" — `:15`.
- Gazetteer: "one opens the clinic's gladiator transport route" — `castle-ward.md:90`.
- Factions Guide: "staff ply them with exotic food, then blindfold them and escort them through an underground dock" — `campaign/guides/factions/09-xanathars-guild.md:21`. The subject is "staff", not Keln.
- Alexandrian: "Those heading to the gladiatorial gatherings will be blindfolded before being led down the stairs" — printed p.43 [PDF p.8]. No named subject.
- Guild page, current: "manages the audience that gathers there for the gladiatorial fights" — `campaign/setting/organizations/08-xanathars-guild.md:107`.
- Guild page, Draft Notes (stale quote of an earlier Key Members line): "manages the gladiatorial audience transports to the Lair" — `campaign/setting/organizations/08-xanathars-guild.md:194`. The current line 107 no longer contains that wording. The pass5 note quoted the earlier line at `docs/plans/setting-compendium-research-notes/pass5/xanathars-guild.md:179`.
- Higher source: the Guild page's current line 107 (campaign). It does not say he runs transports. The page's "manager of the gladiatorial transport route" is stale wording. The Draft Notes line 194 is stale.

**D7. Where the gathering route goes (quest-state; route only, not day-one)**
- To "caverns near Skullport": "escort them through an underground dock to caverns near Skullport" — `campaign/guides/factions/09-xanathars-guild.md:21`; Alexandrian printed p.43: "the blindfolds will remain in place until the boat arrive at another secret dock in the caverns near Skullport" [PDF p.8].
- To "Area X4": "Optional: follow a guest being transported to the gladiatorial event." and "transported by boat to Area X4 of Xanathar's Lair." — `campaign/structure/arc-e-faction-outposts.md:153`. The Lair PDF gives the same X4 route: "(also via X4, but almost certainly arriving in X6 before you'll have a chance to slip away)" — printed p.86 [PDF p.4]. Alexandrian printed p.43 says the dock "connects to a passage which intersects the one leading from Area X4" — not the same as entering X4.
- To "Area X1": "escorted blind to Area X1 as if attending the gladiatorial fights." — `sources/Appendix_C_-_Player_Faction_Missions.md:1877` (Arc FG-4, Force Grey M4 "Destroy the Intellect Factory", Scene 2). Alexandrian printed p.42: "some heading through the sewers to X1, others following the route described below".
- Higher source: the Alexandrian Lair PDF (X4 for the audience route, printed p.86) and the Factions Guide (caverns near Skullport). The X1 line is in Appendix C. The orchestrator decides. The page needs only "a route to the Lair".

**D8. "Lair" as a featured quest**
- "Featured in: Faction Outposts, Xanathar's Lair" — `08-keln-trigos.md:7`
- The Lair PDF (printed pp.83 to 91) names no Keln and no Terasse. It names "gladiatorial gathering points throughout the city" (printed p.83). The roster lists (printed pp.89 and 90) have no Keln. The only campaign support is the list at `campaign/structure/arc-f-xanathars-lair.md:339`.

**D9. The Vosk line in the Harpers design note**
- "Both sources leave the watcher a minor Xanathar's Guild Spy named Vosk, who reports to Keln Trigos." — `campaign/quests/faction-events/harpers/m01-the-talking-mare/design-notes.md:5`
- The design note says "Both sources" (Appendix C and Dragon Heist). The published adventure has no Vosk (grep of `sources/adventure-wdh.json`, no match). Among the sources searched, only Appendix C (`:110` to `:128`) and this design note name Vosk. The design note's "Dragon Heist" attribution is not supported by the adventure text.

**D10. Source guide describes the Xanathar outposts differently**
- "**Xanathar Guild outposts:**" lists "Dock Ward gambling den", "Sewer monitoring station near Trollskull Alley" and "Underdock warehouse" — `sources/SOURCE_GUIDE.md:208` to `:211`.
- The Alexandrian PDF's Xanathar outposts are the Terasse Estate, Grinda Garloth's and the Orb Confectioners sewer hideout (printed pp.42 to 44 [PDF pp.7 to 9]). None of the SOURCE_GUIDE items matches. The PDF is the source; the guide's list is stale.

**D11. Estate ownership wording**
- "secretly owned by Xanathar" — Alexandrian printed p.42 [PDF p.7]; "that Xanathar secretly owns" — `campaign/setting/organizations/08-xanathars-guild.md:55`; "A modest rowhouse secretly owned by Xanathar" — `campaign/guides/factions/09-xanathars-guild.md:21`. Consistent. No conflict.

---

## E. Stale lines in other files (not edited) and routed quest references

### E1. Setting pages that carry quest references (campaign-start rule)

- `campaign/gazetteer/waterdeep/castle-ward.md:11`: "> - **Faction Outposts** sends the party to Terasse Estate and Yellowspire. **Xanathar's Lair** can be entered by a secret stair in the Castle Ward sewers, and **Kolat Towers** can be entered through the Yellowspire teleportation circle." (quest routing on a setting page)
- `campaign/gazetteer/waterdeep/castle-ward.md:90`: the GM Notes callout (see D4 and D6). It also reads "Keln keeps the Terasse outpost for Xanathar's Guild" (outpost term).
- `campaign/gazetteer/waterdeep/castle-ward.md:215`: "- `sources/Act_III_Arc_E.md` and `5. Faction Outposts.pdf`: Yellowspire and Terasse Estate." Stale source. `Act_III_Arc_E.md` does not mention Terasse, Keln or the gladiatorial route (grep, no match). Only the PDF does.
- `campaign/gazetteer/waterdeep/castle-ward.md:236`: "- **Keln Trigos**: keeper of Terasse Estate (see the Terasse Estate entry)."
- `campaign/gazetteer/waterdeep/castle-ward.md:275`: "> - **Routed facts:** Keln Trigos (demoted character) moved into the Terasse Estate entry, with his GM Notes as a callout there."
- `campaign/gazetteer/waterdeep/southern-ward.md:74`: "- Hook: **Faction Outposts** treats it as an encounter-plus outpost. A letter there threatens the mechanical beholder's delivery to Terasse Estate, and correspondence with Nar'l Xibrindas gives guildsigns that lead toward **Xanathar's Lair**." (quest hook on a setting page)
- `campaign/gazetteer/waterdeep/southern-ward.md:220`: "- **Castle Ward**: Yellowspire, Terasse Estate and the water table that Jeryth watches."
- `campaign/setting/geography/waterdeep.md:39`: a table row for Castle Ward lists "Terasse Estate" among its sites.
- `campaign/setting/geography/waterdeep.md:100`: a table row "**Faction Outposts** | Yellowspire and Terasse Estate, the Zhentarim house on Brindul Alley and the shrine on Aveen Street ..." (quest routing on a setting page; the row continues past the quoted part)
- `campaign/setting/geography/undermountain-and-skullport.md:124`, `:135`, `:164`: the trapdoor and the Castle Ward cross-reference; `:164` is a "Routed facts" line.

### E2. Guild page (`campaign/setting/organizations/08-xanathars-guild.md`)

- Contacts label changed since the Pass 5 note. The Pass 5 note quotes the earlier line: "- **Contacts:** **Ahmaergo**, **Keln Trigos**, **Grinda Garloth** (outpost keepers); **Gorath**, **Korgstrod Uxgulm**, **Noska Ur'gray** (response team leaders)" — `docs/plans/setting-compendium-research-notes/pass5/xanathars-guild.md:174` (quoting `08-xanathars-guild.md:6`). The current line 8 says "(Guild contacts in the city)".
- Draft Notes line 194 quotes Key Members, Keln as "manages the gladiatorial audience transports to the Lair." The current line 107 differs (D6). Stale.
- Line 53, "**The three outposts.**", is a day-one heading on a lore page; the drafter may need to consider the word "outpost" as a location label. This is a page-wide term, not a Keln-only line.
- Line 147 (Sources): "`campaign/guides/factions/09-xanathars-guild.md` (lines 21, 53): the Terasse Estate's cellar and the sweets shop, as places only". The Factions Guide line numbers still match (21, 53).

### E3. Factions Guide and structure doc (quest-state)

- `campaign/guides/factions/09-xanathars-guild.md:17` to `:35` (Terasse Estate entry), `:88` to `:90` and `:102` (Revelation List), `:112` (Notable Figures list).
- `campaign/structure/arc-e-faction-outposts.md:143` to `:157` (4A), with "Keln Trigos (priest) and his guards raise the alarm" at `:155`.
- `campaign/structure/arc-e-faction-outposts.md:149` (passphrases) and `:153` (Operation objectives).

### E4. Other campaign references (day-one or setting)

- `campaign/setting/notable-figures/xanathars-guild/02-ahmaergo.md:134`: "> - **Routed to quests:** The Terasse Estate, Orb Confectioners and Interrogation House letters from Ahmaergo live in `campaign/structure/arc-e-faction-outposts.md` (lines 153, 167, 169, 183 and 351) and `campaign/guides/factions/09-xanathars-guild.md` (lines 29, 43 and 57), for **Faction Outposts**."
- `campaign/structure/arc-f-xanathars-lair.md:337`: "- **Faction Outposts**, Scene 4 (Xanathar Outposts) — Terasse Estate, Grinda Garloth's, Orb Confectioners. Entry methods seeded in **Faction Outposts** are executed in Scene 2."
- `campaign/structure/arc-f-xanathars-lair.md:339`: "- **Notable Figures** — Full NPC profiles for Xanathar, Ahmaergo, Nar'l Xibrindas, Nihiloor, Noska Ur'gray, Ott Steeltoes, Thorvin Twinbeard, Keln Trigos, Grinda Garloth, Korgstrod Uxgulm, Gorath."

### E5. Routed quest references (quest-state; kept off the day-one page)

- **Faction Outposts, Terasse Estate (4A)**: `campaign/structure/arc-e-faction-outposts.md:143` to `:157`; `campaign/guides/factions/09-xanathars-guild.md:17` to `:35` and `:88` to `:102`; Alexandrian `sources/5. Faction Outposts.pdf` printed pp.42 to 44 [PDF pp.7 to 9]; Revelation Lists `sources/17. Outpost and Lair Revelation Lists.pdf`, printed p.123 [PDF p.3]: under "TERASSE ESTATE": "A Directive Regarding Materiel (Grinda Garloth)", "On the Delivery of a Mechanical Beholder (Xanathar Sewer Hideout 2)", "Report from Seffia Naelryke (Cassalanter Villa)"; under "LAIR: XANATHAR'S LAIR": "Gladiatorial Gathering Point (Terasse Estate)".
- **Lords' Alliance M2, Harko's cipher note ("K")**: `sources/Appendix_C_-_Player_Faction_Missions.md:519` and `:546`; `campaign/quests/faction-events/lords-alliance/m02-the-exiles-return/overview.md:28`, `:65`, `:75`; `ev-01-the-exiles-return.md:22`, `:301`, `:431` to `:437`, `:492`, `:503`, `:512`; `design-notes.md:38`. Quotes:
  - "> - The cipher note in his coat is a Guild courier's note that names "K", who is Keln Trigos of the Terasse Estate. Nobody in this mission can know that." — `overview.md:28`
  - "> - The cipher note names "K" and an eastern staircase on Elsambul's Lane. K is Keln Trigos of the Terasse Estate, and nobody in this Event can know that yet." — `ev-01-the-exiles-return.md:22`
  - "- **Terasse Cipher Taken** — mark when a member gives Jalester Harko's cipher note, decoded or not. Read by **Faction Outposts** (unconverted) as a fourth path into the Terasse Estate, by the eastern staircase on Elsambul's Lane." — `ev-01-the-exiles-return.md:512`
- **Harpers M1, the Vosk watcher**: `sources/Appendix_C_-_Player_Faction_Missions.md:110` to `:128` (Arc H-1, Scene 5 and "If the Party Notices Vosk"); `campaign/quests/faction-events/harpers/m01-the-talking-mare/design-notes.md:5`. The reporting line (`Appendix_C:116`) is quest text. The Keln page may not use it as a Connections fact without a route (orchestrator's call).
- **Doom Raiders LA-4, Ziraj's offer (Copper Alley)**: `sources/Appendix_C_-_Player_Faction_Missions.md:654` (Ziraj's header), `:660` and `:681`: "The Terasse Estate intelligence, if Ziraj's trade was accepted, is a Grand Game bonus clue."
- **Force Grey M4, the gathering-point route**: `sources/Appendix_C_-_Player_Faction_Missions.md:1875` to `:1877` (Arc FG-4, Scene 2). "**The Gathering Point Route** (if the party has a Guild passphrase from any investigation): through one of the Terasse Estate gathering points, escorted blind to Area X1 as if attending the gladiatorial fights."

### E6. Stale copies (snapshots, not edited)

- `sources/research/pass5-bundles/xanathars-guild/campaign-hits.txt:624`: the old summary line, "*Tiefling priest (Xanathar's Guild), neutral evil, he/him*. Stat block: **Priest**." (matches current line 5).
- `sources/research/pass5-bundles/xanathars-guild/campaign-hits.txt:664`: "- **Keln Trigos** — Tiefling priest (Xanathar's Guild), neutral evil. Stationed at the Terasse Estate. Provides healing for the Guild's agents and manages the gladiatorial audience transports to the Lair. See the **Keln Trigos** page in Notable Figures." (the pre-ruling Guild line; the current line is `08-xanathars-guild.md:107`).
- `sources/research/pass3-bundles/guilds/campaign-hits.txt:813`: "> - *Tiefling priest (Xanathar's Guild), neutral evil*. Stat block: **Priest**." (no pronouns; the pronouns were added later).
- `sources/research/pass3-bundles/guilds/campaign-hits.txt:839`: the same older Guild line as `pass5` `:664`.

---

## F. Gaps (what a Background would need that no source gives)

Each gap lists the suggested modest inference. The drafter tags any inference `[research]`. None of these is an invented plot fact.

1. **Birth, family, early life, where he trained as a healer.** No source. Inference: "He had a healer's training before the Guild" `[research]`, which fits "his healer's professional warmth" (`08-keln-trigos.md:11`) and the Alexandrian's "healing arts" (printed p.43). No place or teacher.
2. **Deity or faith.** No source names a god. "priest" and "priestly spells" (`08-keln-trigos.md:23`) are the only faith text. Inference: leave the god unnamed, or say "a priest's training" `[research]`. Do not link any god, including the Cassalanter or Asmodean line (Cassalanter secrecy).
3. **How he joined the Guild.** The general test is at `campaign/setting/organizations/08-xanathars-guild.md:32`. No Keln entry. Inference: he passed the same test as any applicant `[research]`.
4. **When he was posted to the Terasse Estate, and how long he has run it.** No source gives a date. The estate is "secretly owned by Xanathar" (Alexandrian printed p.42). Inference: no date; "has run the estate for some years" is not supported and should be left out, or tagged `[research]` as a guess the orchestrator must approve.
5. **Rank.** Only "priest" (role) and "Guild contacts in the city" (`08-xanathars-guild.md:8`). The "lieutenant" in Appendix C is a quest aside (D2). Inference: he holds no rank on the ladder `[research]`.
6. **His healing price and clinic hours.** Only the voice profile's "Healing is fifty gold" (`.claude/skills/character-voices/voices/xanathars-guild.md:150`). Inference: keep it in the voice block only; do not give it as a fact.
7. **Priestly spells and Morale.** Not named in any source. The Priest stat block is cited (MM p.348, edition not printed). Inference: "priestly spells" follows the Priest stat block `[research]`; name no spells.
8. **Morale: "He does not run".** No source. Inference: keep it as a habit tagged `[research]`, or cut it.
9. **Why Xanathar trusts him, and what he knows.** The Persona says "he has worked for Xanathar long enough" (`08-keln-trigos.md:21`) with no source. The Guild page gives only "Underlings Are Disposable" (`08-xanathars-guild.md:34`). Inference: "Xanathar keeps him because he keeps the estate quiet" `[research]`, which the Factions Guide's "neither officially connected" (`09-xanathars-guild.md:21`) supports.
10. **Relations with Gorath, Korgstrod, Noska, Nar'l, Nihiloor, Ott.** No source. The escalation chain (`09-xanathars-guild.md:35`) names Gorath's team as the response to a second outpost hit, not a relationship with Keln. Inference: none `[research]`.
11. **Keln's appearance.** No source gives any. Inference: none, or leave to the drafter `[research]`.
12. **Keln's own fate, and whether the estate is still his.** No source. The routed Faction Outposts quest decides it. Do not state it on the day-one page.
13. **Whether the healing is for everyone or for Guild agents.** Conflict D5; no single source. Inference: the public clinic is the setting's version (`castle-ward.md:85`) and the Guild's agents are patients too `[research]`.
14. **The transport route and who runs it.** Conflict D6; no source names Keln as the blindfolding party. Inference: "staff" run the route, under Keln's roof `[research]`.

---

## Not found

Searched (terms): Keln, Trigos, Terasse, Elsambul, "Tier 1", "outpost keeper", passphrase, pass phrase, blindfold, healer, Tiefling priest, Vosk, Castle Ward (with Guild context).

Files searched with no Keln content (or no hit):
- `sources/adventure-wdh.json` (no Keln, Trigos, Terasse, Elsambul, Vosk, healer; the "blindfolded" hit at line 9749 is Amath Sercent's captive, not Keln's route)
- `sources/adventure-wdmm.json` (no hit)
- `sources/Act_III_Arc_E.md` (no Terasse, Keln, Trigos or gladiatorial hit)
- `sources/Appendix_B_-_Player_Factions.md` (no hit for Keln, Trigos, Terasse or gladiatorial)
- `sources/Appendix_D_-_Running_the_Tavern.md` (no hit)
- `sources/SOURCE_GUIDE.md` (no Keln; the outposts list at `:208` to `:211` does not name Terasse, see D10)
- `sources/research/**/wiki.txt` (no Keln, Trigos, Terasse or Elsambul line; `scratchpad/wiki-xg/Keln_Trigos.txt` "NOT FOUND"; the Xanathar guild wiki has no clinic or estate line)
- `campaign/setting/villains/xanathar.md`, `campaign/setting/villains/jarlaxle.md`, `campaign/setting/villains/manshoon.md` (no Keln, Terasse)
- `campaign/setting/history/` (no Keln, Terasse)
- `campaign/setting/lore/` and `campaign/setting/the-grand-game/` (no Keln, Terasse)
- `campaign/setting/notable-figures/xanathars-guild/` (Keln only in its own page; `02-ahmaergo.md:134` routed)
- `campaign/setting/deities/` (no Keln; no Keln deity)
- `campaign/guides/trollskull-manor/`, `campaign/guides/gm-guide/` (no Keln hit in the campaign-wide grep except as listed)
- `.claude/skills/character-voices/SKILL.md` (line 33 lists Keln in the `voices/xanathars-guild.md` file)

Gaps tested with the searches above: any origin, family, rank history, deity, appearance or tenure line. None exists.

---

## Not readable

- `sources/Other remix files/*.docx`: not opened (no tools). `sources/SOURCE_GUIDE.md` lists "The Waterdavian's Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx" as a broad NPC reference. It may name Keln. The SOURCE_GUIDE does not list Keln as covered there. The orchestrator should extract it and search for Keln, Trigos, Terasse.
- The two Alexandrian PDFs cited above were read as rendered images. Their quotes are transcriptions. `sources/17. Outpost and Lair Revelation Lists.pdf` was read at PDF pp.1 to 3 only.

## Not run

- `voicecheck.py` was not run (research only).
- The page was not written. No file was edited except this notes file.
