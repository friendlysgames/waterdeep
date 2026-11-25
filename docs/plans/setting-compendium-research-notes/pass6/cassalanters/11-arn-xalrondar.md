# Pass 6 research notes: Arn Xalrondar

Page: `campaign/setting/notable-figures/cassalanters/11-arn-xalrondar.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR. Arn is a cult fanatic of Asmodeus who lives on the upper floor of the Converted Windmill with Seffia Naelryke. Cassalanter secrecy applies: nobody outside the household and the cult knows about the pact.
Model format: `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md`
Companion notes: `docs/plans/setting-compendium-research-notes/pass6/cassalanters/12-rella-asp.md`

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes are shown as plain quotes. Tags such as `{@creature ...}` are left as written.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. These PDFs were read as rendered page images and their quotes are transcriptions. Check exact wording with `pdftotext -layout` before any quote goes into prose:
  - `sources/5. Faction Outposts.pdf`: printed pp.39-41 = PDF pp.4-6 (Asmodean Shrine, Converted Windmill). Printed p.40 = PDF p.5 (roster).
  - `sources/6. Faction Response Teams.pdf`: printed pp.52-53 = PDF pp.4-5 (Seffia's team and letter), printed p.55 = PDF p.7 (Vevette's card).
  - `sources/10. Lair  Cassalanter Villa.pdf`: printed p.81 = PDF p.5 (adventure roster).
  - `sources/17. Outpost and Lair Revelation Lists.pdf`: printed p.122 = PDF p.2 (Asmodean Shrine revelations).
  - `sources/7. Other Response Teams.pdf` PDF pp.1-3 and `sources/27. Addendum A Night in Trollskull Manor.pdf` PDF p.1 were read; neither names Arn.
- Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-cassalanters/11-arn-xalrondar.txt` is `NOT FOUND`. No wiki line in `sources/research/` (grep for "Xalrondar" across every `*wiki*` file) names him.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki (none).
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **The page says Arn gave the Stone to the spined devil. The campaign decided Eye #2.** Arn page line 21 and line 25 say "Stone of Golorr". Seffia's page records that the Session 47 consistency pass changed the object to Eye #2 and that Arn's spined devil carries the Eye (`10-seffia-naelryke.md` Draft Notes, line 99). The Gazetteer already says "sent the Eye away" (`southern-ward.md:137`). The devil episode is a quest-time event (section C, rows 4, 5, 8, 10).
2. **Arn's rank is "lieutenant" in one file and "partner" in three others.** `arc-g-cassalanter-villa.md:21` says "her lieutenant". Arn's page (line 25), Seffia's page (line 32) and Victoro's page (line 55) say partner.
3. **Morale and faith conflict with the structure doc.** Arn's page says he "does not retreat unless Seffia orders it" (line 23) and has "theological certainty as bedrock" (line 13). `arc-g-cassalanter-villa.md:100` says "Pragmatic, not devout — if the operation is clearly failing, he surrenders and cooperates for clemency." The voice profile says he "never speaks of his faith to outsiders" (`cassalanters.md:201`).
4. **The villa handprints have no source.** Arn's page (line 21) and `southern-ward.md:133` say the apartment handprints "match those at Cassalanter Villa". No campaign or adventure file describes handprints at the villa. Do not state it as fact. Keep it as `[research]` or drop it.
5. **Household status is mixed.** `10-cassalanters.md:52` counts Arn among the villa's "sixteen named staff" and the "six cult members". `10-cassalanters.md:53` and `southern-ward.md:62` say he lives at the Windmill. `arc-g-cassalanter-villa.md:21` says he "has never set foot in the temple" yet is one of "six souls who know what lies beneath". Cult membership is firm (`asmodeus.md:72`, `10-cassalanters.md:103`).
6. **Alignment, species, pronouns and sex agree across every source.** LE, Tethyrian human, he/him (male in the adventure). The stat-block name differs ("Cult Fanatic" on the page, "Cultist Fanatic" in the Factions Guide). See B and D6.

---

## A. Background facts by theme

### A1. Origin, birth and early life

No source gives Arn's birthplace, family, age, childhood or how he came to Asmodeus. The only personal descriptors are these.

> "Lord Cassalanter sent Arn and Seffia on a mission to retrieve the {@item Stone of Golorr|WDH} from his family's mausoleum. He also gave them secret orders to dispose of three other members of the cult whom he couldn't trust to keep quiet about the stone."
> — `sources/adventure-wdh.json:13219` (Converted Windmill: Summer, "Cult Fanatics", page 88; the mission text is pre-campaign)

(rest of the passage covers: "Arn and Seffia would be horrified to learn that they failed in so simple a task; they try to correct their mistake by killing Vaelle Lurval if she's with the party (see \"Mausoleum: Summer\").")

### A2. Family, household and residence

> "The villa employs sixteen named staff, and ten of them know nothing about the temple (`arc-g-cassalanter-villa.md` line 91). The six cult members are Willifort the butler, Tissina Khyret the attendant, Nana Rosse the twins' caretaker, Jandar Chergoba the head chef, and the field pair Seffia Naelryke and Arn Xalrondar. The other ten are Corvo (footman), Pela (laundress), Marchello (gardener), Fiorella (cook's assistant), Doro (stable hand), Lissette (upstairs maid), Rennet (scullion), Maesta (housekeeper), Tomas (night watchman) and Bressa (nursemaid). Maesta manages the non-cult staff and is loyal to the household's reputation, not to the Cassalanters themselves."
> — `campaign/setting/organizations/10-cassalanters.md:52` (Structure, "Household staff")

> "**Field operatives and outposts:** Seffia Naelryke commands the family's precise field team from the Converted Windmill on Coachlamp Lane in the Southern Ward, where Arn Xalrondar lives with her in plain dress."
> — `campaign/setting/organizations/10-cassalanters.md:53`

> "Only the family, its personal attendants and its guards live in the house, and the other servants arrive before dawn from homes in the Dock Ward and the Field Ward (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/10-cassalanters.md:48` (Structure, "The villa")

> "- **Arn Xalrondar** (cult operative, field security) — handles outpost logistics. Has never entered the temple. Follows Seffia's orders. Pragmatic, not devout — if the operation is clearly failing, he surrenders and cooperates for clemency."
> — `campaign/structure/arc-g-cassalanter-villa.md:100` (Questioning Staff, "Cult Staff"; structure doc, pending conversion)

> "The household holds six souls who know what lies beneath. Willifort Crowelle, doppelganger, serves Asmodeus with genuine devotion — the family is secondary. Tissina Khyret, Ammalia's attendant, is a cult fanatic who joined out of loyalty to Ammalia personally — she does not know the contract's full terms. Laiba \"Nana\" Rosse, the twins' caretaker, is a cult fanatic who joined the cult to remain close to the children — she would betray the Cassalanters to save Terenzio and Elzerina. Jandar Chergoba, head chef, is a cult fanatic bound by debt — Victoro holds a financial obligation over him that converted into cult service. Seffia Naelryke commands the external operations team and knows the cult's military posture. Arn Xalrondar, her lieutenant, handles field security for the outposts and has never set foot in the temple."
> — `campaign/structure/arc-g-cassalanter-villa.md:21` (Quest Opener)

### A3. How he joined the cult and rose to his post

No source dates his joining or gives his route into the cult. The role descriptions are these.

> "- **Arn Xalrondar** — Tethyrian human cult fanatic (Asmodeus), lawful evil. Cult fanatic, Seffia's partner at the Windmill on Coachlamp Lane. See the **Arn Xalrondar** page in Notable Figures."
> — `campaign/setting/organizations/10-cassalanters.md:103` (Key Members)

> "- **Seffia Naelryke** — Tethyrian human cult fanatic (Asmodeus), lawful evil. Cult fanatic, loyal to Asmodeus, stationed at the Converted Windmill with Arn Xalrondar. Keeps a letter from Lord Cassalanter confirming that her ritual identified the Eye in the Brandath Crypts, and she prizes it. See the **Seffia Naelryke** page in Notable Figures."
> — `campaign/setting/organizations/10-cassalanters.md:102` (Key Members; the rank context for the pair)

> "- **Seffia Naelryke** and **Arn Xalrondar:** Seffia commands the field team and answers to Victoro, and Arn is her partner. Victoro does not know that their mission to the Brandath Crypts left a witness alive."
> — `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:55` (Relationships)

> "- **Arn Xalrondar:** Her operational partner at the Windmill, who defers to her on planning and covers her in a fight. Unresolved: he acts on his own when she is out of the room, as when he sent the Eye off with a spined devil."
> — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:32` (Connections)

Rank and role, as the sources give them: "Arn Xalrondar, her lieutenant, handles field security for the outposts" (`arc-g-cassalanter-villa.md:21`); "handles outpost logistics" (`arc-g-cassalanter-villa.md:100`); "Seffia Naelryke's operational partner" (`11-arn-xalrondar.md:25`).

### A4. The Brandath Crypts mission and the failed silencing (pre-campaign, undated)

> "Victoro sent Seffia Naelryke and Arn Xalrondar to take it and to silence three cult members who knew too much. The two killed two of them, and the third, a florist named Vaelle Lurval, survived without Victoro knowing it (**Seffia Naelryke**; *Dragon Heist*, 5e)."
> — `campaign/setting/organizations/10-cassalanters.md:29` (History, "Before Ches 1, 1492 DR, undated, the loophole and the Eye"; the sentence before it says "An infernal divination placed Eye #2 of the Stone of Golorr in the Brandath Crypts")

> "Victoro Cassalanter gave her two missions, to retrieve an Eye of the Stone of Golorr from the Brandath Crypts and to silence three cult members who knew too much. She and Arn killed two, and Vaelle Lurval survived. Victoro does not know, and Seffia means to repair the failure without telling him."
> — `campaign/gazetteer/waterdeep/southern-ward.md:129` (Seffia's GM Notes; the Windmill is in the same ward)

> "The three cultists were low-ranking members of {@creature Victoro Cassalanter|WDH}'s cult of Asmodeus. They were betrayed by two cult fanatics acting on orders from Lord Cassalanter, who not only wants the {@item Stone of Golorr|WDH} but also, as a security precaution, intends to eliminate cult members who know too much about it. These three cultists were felled by daggers and {@spell inflict wounds} spells."
> — `sources/adventure-wdh.json:8316` (Mausoleum: Summer, "Left for Dead", page 70)

> "The survivor is Vaelle Lurval (LE female Tethyrian human {@creature cultist}), a 30-year-old Waterdavian florist. She was brought into the cult by her boyfriend, Holiver Tornrudder, who lies dead nearby. The other dead cultist is named Kaeth Warloon."
> — `sources/adventure-wdh.json:8317` (page 70)

> "If she is healed, Vaelle regains consciousness. She reveals that the cult fanatics, Arn Xalrondar and Seffia Naelryke, would likely have taken the stone to an old windmill in the Southern Ward, where they hold their own ceremonies worshiping Asmodeus."
> — `sources/adventure-wdh.json:8318` (page 70; the rest of the passage covers the directions to the windmill and the revenge motive)

The campaign files give Eye #2 as the object (`10-cassalanters.md:29`; `arc-g-cassalanter-villa.md:15`). Seffia's letter is the only written record of the result (section D4).

### A5. Possessions and devotion

> "Under the cot is Arn's Book of Worship: This text with a stylized goat's head drawn in blood upon its plain brown cover, contains a number of \"high prayers\" to Asmodeus and the description of a number of banal demonic rites of worship. On the inside back cover, in simple handwriting, one can read, \"This book belongs to Arn Xalrondar, of the Windmill upon Coachlamp Lane.\""
> — `sources/5. Faction Outposts.pdf` printed p.39 (PDF p.4), Asmodean Shrine, Area 4 — Chapter House. Transcription from a page image; check with `pdftotext -layout`.

> "*Area 4 — Chapter House.* An *animate objects* statue of writhing tentacles (50 hp, AC 10, +6 to hit, 2d20+2 damage), which attacks only on command. Under a cot: *Arn's Book of Worship*, a prayer text with Arn Xalrondar's name and the Windmill's address written inside the back cover."
> — `campaign/guides/factions/11-cassalanters.md:31`

> "- *Arn's Book of Worship* (Asmodean Shrine — inside back cover names Arn and the Windmill)"
> — `campaign/guides/factions/11-cassalanters.md:89` (Revelation List)

### A6. Where he lives and how the Windmill is kept

> "- A decrepit building that used to be a windmill (Dragon Heist). **Seffia Naelryke** and **Arn Xalrondar** live on the upper floor as ordinary tenants, and she does not receive visitors."
> — `campaign/gazetteer/waterdeep/southern-ward.md:62` (Converted Windmill, Coachlamp Lane)

> "CONVERTED WINDMILL (Southern Ward, Coachlamp Lane): Use the description of the Summer version of the Converted Windmill (see *Dragon Heist*, p. 88). It's used as an apartment by Arn Xalrondar (LE male Tethyrian human) and Seffia Naelryke (LE female Tethyrian human), both **cult fanatics**."
> — `sources/5. Faction Outposts.pdf` printed p.41 (PDF p.6). Transcription from a page image; check with `pdftotext -layout`. The bold is in the source.

> "Use the Summer version of the Converted Windmill (DH p. 88). Arn Xalrondar and Seffia Naelryke live here as cult fanatics in plain dress."
> — `campaign/guides/factions/11-cassalanters.md:53`

> "- A Cassalanter steward, Brimel Crestfall, has carried baskets of candles, salt, black wax and wine to the second landing of its stair for years. The family keeps the windmill off its calendar and its house books."
> — `campaign/gazetteer/waterdeep/southern-ward.md:63` (the "for years" refers to the deliveries and the building, not to Arn's own tenure)

> "- Ammalia Cassalanter visits twice a month, alone, in a hired cab with the curtains drawn. The family pays the upper floor's rent in the name of Marra Selby."
> — `campaign/gazetteer/waterdeep/southern-ward.md:68` (GM Notes; "Marra Selby" is named in the ward's "Names with no page" list at line 260)

> "The Converted Windmill on Coachlamp Lane is an Asmodean shrine and a fallback site for the Cassalanters' cult. Seffia Naelryke and Arn Xalrondar keep it, the family pays the rent on the upper floor under a false name, and a ritual room holds a map with the Brandath Crypts circled."
> — `campaign/gazetteer/waterdeep/southern-ward.md:36` (GM Notes; the rest of the passage covers the separate Aveen Street shrine and the temple)

### A7. Relationships to named figures

- **Seffia Naelryke** (partner, the one he defers to). Sources: `10-cassalanters.md:103`, `01-victoro-cassalanter.md:55`, `10-seffia-naelryke.md:32` (quoted in A3), and `11-arn-xalrondar.md:25` ("Seffia Naelryke's operational partner"). Quirk of the pair: "She speaks to Arn in half-sentences that he completes." (`10-seffia-naelryke.md:22`); the gazetteer has the same clause at `southern-ward.md:132`: "She speaks to him in half-sentences that he completes."
- **Victoro Cassalanter** (sent him on the mission; Arn answers to Seffia, who answers to Victoro). "Seffia Naelryke commands the field team and answers to Victoro" (`10-cassalanters.md:51`). "Seffia Naelryke's response team answers to Lord Cassalanter" (`10-cassalanters.md:117`). Victoro's knowledge: "Victoro does not know that their mission to the Brandath Crypts left a witness alive" (`01-victoro-cassalanter.md:55`).
- **Ammalia Cassalanter**: visits the Windmill "twice a month, alone, in a hired cab" (`southern-ward.md:68`). No source gives a direct tie between Arn and Ammalia.
- **Willifort Crowelle**: "Willifort Crowelle links the family to everyone who works for it." (`10-cassalanters.md:51`). No source names an Arn–Willifort link.
- **Vaelle Lurval** (the survivor of the failed silencing): adventure `:8317`–`:8319` (A4). Campaign: "Victoro does not know" (`01-victoro-cassalanter.md:55`). Vaelle has no Notable Figures page (`10-seffia-naelryke.md:98`).
- **Holiver Tornrudder** and **Kaeth Warloon** (the two dead cultists): `sources/adventure-wdh.json:8317` (A4). No campaign file names either.
- **Vevette Blackwater** (Zhentarim): the visiting card is Seffia's, not Arn's. "Vevette carries Seffia Naelryke's Visiting Card. It gives Seffia's address as "the Windmill on Coachlamp Lane"." (`sources/6. Faction Response Teams.pdf` printed p.55, PDF p.7; transcription). Seffia approached Vevette, who refused (`campaign/setting/organizations/10-cassalanters.md:121`).

### A8. Inner life and faith

- Faith: the Arn page says "theological certainty as bedrock" (line 13). The voice profile says "Subordinate devotion that turns into initiative" (`cassalanters.md:198`) and "never speaks of his faith to outsiders" (`cassalanters.md:201`). The Book of Worship has "high prayers" to Asmodeus (PDF p.39). `arc-g-cassalanter-villa.md:100` says "Pragmatic, not devout". Conflict: D3.
- Obedience and independence: "He checks for Seffia before answering." (`cassalanters.md:199`); "He never questions Seffia to her face" (`cassalanters.md:201`).

### A9. Dates, ages and time in post

No source gives Arn's age, date of joining, or the date he moved into the Windmill. The only dated anchors are: the mission is "Before Ches 1, 1492 DR, undated" (`10-cassalanters.md:29`), and Brimel's deliveries have gone on "for years" (`southern-ward.md:63`). The Windmill outpost is dated in the Factions Guide only as a clock: "**Founders' Day Clock (Flamerule 1): 3–5 days.**" (`campaign/guides/factions/11-cassalanters.md:64`).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Arn page, line 5: "> - *Tethyrian human cult fanatic (Asmodeus), lawful evil, he/him*. Stat block: **Cult Fanatic**." (`campaign/setting/notable-figures/cassalanters/11-arn-xalrondar.md:5`)
- Organization page, line 103: "- **Arn Xalrondar** — Tethyrian human cult fanatic (Asmodeus), lawful evil. Cult fanatic, Seffia's partner at the Windmill on Coachlamp Lane. See the **Arn Xalrondar** page in Notable Figures." (`campaign/setting/organizations/10-cassalanters.md:103`)
- Gazetteer, line 131: "**Arn Xalrondar (Lawful Evil, Tethyrian Human, he/him)**" (`campaign/gazetteer/waterdeep/southern-ward.md:131`)
- Adventure, line 13211: "named Arn Xalrondar (LE male Tethyrian human) and Seffia Naelryke (LE female Tethyrian human)." (`sources/adventure-wdh.json:13211`, Converted Windmill: Summer)
- Alexandrian, PDF p.41 (printed): "(LE male Tethyrian human)" (see A6).

**Species**
- Arn page, line 5: "Tethyrian human". Organization page, line 103: "Tethyrian human cult fanatic". Gazetteer, line 131: "Tethyrian Human". Adventure, line 13211: "LE male Tethyrian human". Alexandrian, PDF p.41: "Tethyrian human". All agree.

**Pronouns**
- Arn page, line 5: "he/him". Gazetteer, line 131: "he/him". Adventure, line 13211: "male" (sex, not pronouns). Alexandrian, PDF p.41: "male". The page's pronouns are sourced.

**Stat block**
- Arn page, line 5: "Stat block: **Cult Fanatic**." Affiliation: "**Affiliation:** The Cassalanters (cult)" (line 6).
- Factions Guide, line 45: "**Roster:** 1 **Cultist Fanatic** + 2 **Imps** (Area 1) | 1 **Apprentice Wizard** + 2 **Imps** (Area 2) | 2 **Cultist Fanatics** (Area 4)." (`campaign/guides/factions/11-cassalanters.md:45`)
- Factions Guide, line 62: "**Roster:** Seffia Naelryke (**Cultist Fanatic**) + Arn Xalrondar (**Cultist Fanatic**) + 1 **Imp** (invisible, on watch)." (`campaign/guides/factions/11-cassalanters.md:62`)
- Adventure, line 13211: "two treacherous {@creature cult fanatic||cult fanatics} named Arn Xalrondar". Alexandrian PDF p.41 (printed): "both **cult fanatics**". Alexandrian PDF p.52 (printed, Seffia only): "Seffia Naelryke (**cult fanatic**, MM p. 345)". No separate Arn stat appears in any source.

---

## C. Sentences on the current page that narrate quest-time or depend on a discovery

Current page: `campaign/setting/notable-figures/cassalanters/11-arn-xalrondar.md`. The page has no Background, Personality or Connections section yet. Each row says whether the sentence is day-one and where its fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L5 | "*Tethyrian human cult fanatic (Asmodeus), lawful evil, he/him*. Stat block: **Cult Fanatic**." | Day-one. Stat name conflicts with the Factions Guide (D6) | Section B |
| 2 | L6 | "**Affiliation:** The Cassalanters (cult)" | Day-one | `10-cassalanters.md:103`; `asmodeus.md:72` |
| 3 | L7 | "**Featured in:** Faction Outposts, Cassalanter Villa" | Quest references. Keep out of the body | `arc-e-faction-outposts.md` Scene 6B (line 271); `arc-g-cassalanter-villa.md:100` |
| 4 | L11 | "**Resonance.** Arn should inspire wariness at how completely he defers to Seffia; cold focus when the spined devils arrive and he makes the call himself; and a specific kind of compliance that becomes initiative at the worst moment." | "cold focus when the spined devils arrive and he makes the call himself" is encounter time. The rest is day-one characterization | Encounter: `sources/adventure-wdh.json:13228`; `southern-ward.md:137` |
| 5 | L13 | "**Emotions.** Arn most often feels subordinate devotion to Seffia's operational judgment, theological certainty as bedrock, the particular focus of someone who does what the mission requires without auditing it, and quiet pride in the devil-summoning decision he made under pressure." | "quiet pride in the devil-summoning decision he made under pressure" is quest-time. The other clauses are day-one | Encounter: `sources/adventure-wdh.json:13228`; `southern-ward.md:137` |
| 6 | L15 | "**Motivations.** Arn wants to do what the mission requires, keep the Windmill operational, and trust Seffia's judgment on everything except the moments she is not in the room." | Day-one. The last clause matches Seffia's "Unresolved" hook (`10-seffia-naelryke.md:32`). Motivations stay verbatim | `10-seffia-naelryke.md:32`; `southern-ward.md:137` |
| 7 | L17 | "**Inspirations.** When playing Arn, channel Draco Malfoy (*Harry Potter*, the true believer within a hierarchy), Gaston (*Beauty and the Beast*, the follower who becomes a problem when given a clear target), and any subordinate who is more dangerous than the person giving orders." | Not a fact | n/a |
| 8 | L21 | "**Persona.** To the world, Arn Xalrondar sleeps at the Windmill with Seffia and defers to her judgment on everything that involves planning. To those who investigate, his Book of Worship contains the Windmill's address as the place of assembly, and the handprints in the apartment match those at Cassalanter Villa. Deep down, he made the right call giving the Stone to the spined devil — the mission required it, the Stone escaped, and he will not be talked out of believing the decision was correct." | First sentence: day-one. "To those who investigate, his Book of Worship ... place of assembly": a clue route (routed to Faction Outposts, `11-cassalanters.md:31`); "place of assembly" appears only here and `southern-ward.md:133`. "the handprints ... match those at Cassalanter Villa": unsourced (F9). "Deep down, he made the right call giving the Stone ... the Stone escaped ... will not be talked out of believing the decision was correct": quest-time (the encounter), and the object is wrong (D2) | Book: `sources/5. Faction Outposts.pdf` p.39 (PDF p.4); encounter: `sources/adventure-wdh.json:13228`; `southern-ward.md:137` |
| 9 | L23 | "**Morale.** In a fight, Arn covers Seffia's flanks and does not retreat unless Seffia orders it." | Encounter behaviour, not an event. Keep. Conflicts with `arc-g-cassalanter-villa.md:100` (surrender for clemency) (D3). Matches `10-seffia-naelryke.md:25` ("posts Arn to cover her flanks") | `10-seffia-naelryke.md:25`; `arc-g-cassalanter-villa.md:100` |
| 10 | L25 | "**Relationships.** Arn is the Cassalanter Converted Windmill co-occupant, Seffia Naelryke's operational partner, the cultist whose Book of Worship links directly to the Windmill address (an intelligence seed for any investigation), and the man who sent the Stone of Golorr out with a spined devil rather than allow the party to take it." | "co-occupant" and "operational partner": day-one. "whose Book of Worship links directly to the Windmill address (an intelligence seed for any investigation)": routed clue. "the man who sent the Stone of Golorr out with a spined devil rather than allow the party to take it": quest-time, and the object is wrong (D2) | Routed: `guides/factions/11-cassalanters.md:31`, `:89`; quest: `southern-ward.md:137`; `10-seffia-naelryke.md:99` |
| 11 | L29 | "Arn Xalrondar occupies a windmill in the Southern Ward alongside Seffia Naelryke, defers to her judgment on all matters of planning, and does not draw attention to himself." | Day-one. **28 words** (brief limit 21). Trim in drafting | `southern-ward.md:62`; `10-seffia-naelryke.md:40` |

**Voice profile (`.claude/skills/character-voices/voices/cassalanters.md`, "### Arn Xalrondar" at lines 191-205)**

The file's secrecy header (line 3) says the "after discovery" register is "used only once the party has found the truth". The Arn profile has no after-discovery register. Its lines, with status:

> "*A deferential follower who becomes dangerous the moment he's left to make the call.*" — line 192 (tagline; day-one, but "the moment he's left to make the call" describes the devil decision)

> "- **Sound:** A quiet, earnest, slightly eager voice." — line 194 (day-one)

> "- **Sentence shape:** Short, deferential agreements, then, alone and under pressure, a sudden, firm decision." — line 195 (day-one habit; "under pressure" is an encounter word, not an event)

> "- **Word choice:** Deference (\"Seffia says\"), and plain certainty when he acts." — line 196 (day-one)

> "- **Swearing:** *Casual · Plain · Phrase.* Nervous curses, until he decides." — line 197 (day-one; the swearing stays, adult table)

> "- **Personality in speech:** Subordinate devotion that turns into initiative. He's proud of the spined-devil decision and won't be talked out of it." — line 198. **Quest-time clause:** "He's proud of the spined-devil decision and won't be talked out of it."

> "- **Quirks:** He checks for Seffia before answering." — line 199 (day-one)

> "- **Signature phrases:** \"Seffia says.\" / \"The mission required it.\" / \"I made the right call.\"" — line 200. **Quest-time phrases:** "The mission required it." and "I made the right call." (both refer to the devil decision)

> "- **Never:** He never questions Seffia to her face, never regrets the devil, and never speaks of his faith to outsiders." — line 201. **Quest-time clause:** "never regrets the devil"

> "  - *Greeting:* \"Seffia's not here. You should go.\"" — line 203. Presupposes a visitor at the door (encounter time). Same pattern as Osvaldo's greeting clause in his notes

> "  - *Business:* \"The mission required it. I made the right call.\"" — line 204. **Quest-time** (the devil decision)

> "  - *Under pressure:* \"Shit. Shit. No, I've got this. I've decided.\"" — line 205. Encounter time ("under pressure"); no event named

Quest-time clauses in the profile, for the ruling-16 restatement (none changed yet; the drafter will report changes): lines 198 (second clause), 200 (both phrases), 201 (second clause), 204. Lines 195 and 205 are encounter-time. Line 201's "never speaks of his faith to outsiders" is day-one and stays.

**Routing for the quest-time text (no quest journal exists for the Windmill; the structure doc is authoritative)**
- `campaign/structure/arc-e-faction-outposts.md:271`-`:287` (Scene 6B, "Converted Windmill (Mini-Heist)"): the entry route, the case, the operation and the getaway. Step 5 (line 285): "Arn follows her lead. The imp's ability to escape unseen is the primary complication; the party must neutralize it or accept the escalation consequence."
- `campaign/structure/arc-e-faction-outposts.md:257` (Area 4): "On a shelf: *Arn's Book of Worship*, naming Arn Xalrondar and citing his address as \"the Windmill upon Coachlamp Lane.\""
- `campaign/structure/arc-e-faction-outposts.md:265` (Intel Yield): "*Intel Yield.* Arn's Book of Worship names Arn and the Coachlamp Lane windmill — the bridge to the Converted Windmill."
- `campaign/guides/factions/11-cassalanters.md:31` and `:89` (Asmodean Shrine, Revelation List).
- `sources/adventure-wdh.json:13218`-`:13228` (Converted Windmill: Summer, "Cult Fanatics" and "Devils' Arrival", page 88): the apartment, the mission, and the devils taking the Stone. Routed to **Faction Outposts** Scene 6B.
- `sources/adventure-wdh.json:8316`-`:8319` ("Left for Dead", page 70): the party finds the dead cultists and Vaelle. Routed to a Faction Outposts or Cassalanter Villa event (no journal yet).
- Quest-time mission outcome text: `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:99` (Session 47 change; the devil carries the Eye).

---

## D. Conflicts

**D1. Rank: "lieutenant" or "partner"**
- `campaign/structure/arc-g-cassalanter-villa.md:21`: "Arn Xalrondar, her lieutenant, handles field security for the outposts and has never set foot in the temple."
- `campaign/setting/notable-figures/cassalanters/11-arn-xalrondar.md:25`: "Seffia Naelryke's operational partner"
- `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:32`: "Her operational partner at the Windmill"
- `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:55`: "Arn is her partner."
- Three of the four sources say partner. The structure doc is pending conversion. Not settled here; the orchestrator decides.

**D2. The object he sent away: Stone of Golorr or Eye #2**
- Arn page, line 21: "he made the right call giving the Stone to the spined devil"
- Arn page, line 25: "the man who sent the Stone of Golorr out with a spined devil"
- Gazetteer, `southern-ward.md:137`: "He sent the Eye away with a spined devil rather than let the party take it, and he believes the decision was correct."
- Seffia page, `10-seffia-naelryke.md:99` (Draft Notes): "Her mission is now to retrieve Eye #2 from the Brandath Crypts rather than the Stone of Golorr (Connections, Persona, Secret and the letter line), and Arn's spined devil carries the Eye. The published adventure has Arn hand the Stone itself to a spined devil."
- Published adventure, `sources/adventure-wdh.json:13228`: "whereupon Arn gives one of them the {@item Stone of Golorr|WDH}."
- Ranking: the campaign decision (Eye #2) outranks the adventure. Arn's page is stale on this point.

**D3. Surrender, morale and faith**
- Arn page, line 23: "In a fight, Arn covers Seffia's flanks and does not retreat unless Seffia orders it."
- `campaign/structure/arc-g-cassalanter-villa.md:100`: "Pragmatic, not devout — if the operation is clearly failing, he surrenders and cooperates for clemency."
- Arn page, line 13: "theological certainty as bedrock"
- Voice profile, `cassalanters.md:201`: "he never speaks of his faith to outsiders"
- Ranking: campaign files rank above the adventure, and the adventure has no Arn surrender line. The Notable Figures page and the structure doc disagree; the orchestrator chooses.

**D4. Who performed the divination (who identified Eye #2)**
- Seffia page, line 23: "She keeps a letter from Lord Cassalanter confirming that her ritual identified Eye #2 in the Brandath Crypts."
- `campaign/structure/arc-g-cassalanter-villa.md:15`: "A commune ritual performed in the temple — Asmodeus answering through a pit fiend proxy — identified the Eye's resting place: the crypt of Lady Alethea Brandath, Renaer Neverember's mother, interred in the Brandath Mausoleum in the City of the Dead. Victoro dispatched Seffia Naelryke's team to extract it."
- Alexandrian, `sources/6. Faction Response Teams.pdf` printed p.53 (PDF p.5), Victoro's letter to Seffia: "Seffia—Lady Ammalia and I are both deeply moved by what your ritual accomplished." (transcription)
- Arn is not named in either version. The Arn page does not say who did the divination. The Background should avoid the point or cite both.

**D5. Handprints at the villa**
- Arn page, line 21, and `southern-ward.md:133`: "The handprints in the apartment match those at **Cassalanter Villa**."
- No campaign file, location journal or adventure line describes handprints at the villa. Searched `campaign/locations/cassalanter-villa/`, `campaign/structure/arc-g-cassalanter-villa.md` and the adventure. Not a conflict between two sources; it is an unsourced claim (F9).

**D6. Stat-block name**
- Arn page, line 5: "Stat block: **Cult Fanatic**."
- Factions Guide, line 62: "Arn Xalrondar (**Cultist Fanatic**)"
- Adventure, line 13211: "cult fanatic||cult fanatics" (linked to the MM creature)
- Naming only. The stat block itself is the MM cult fanatic in every source.

**D7. Is he in the temple at the Cult Gathering**
- `arc-g-cassalanter-villa.md:21` and `:100`: "has never set foot in the temple"; "Has never entered the temple."
- `sources/10. Lair  Cassalanter Villa.pdf` printed p.81 (PDF p.5), Temple of Asmodeus (Cult Gathering), roster line: "3d10 cultists + All Named NPCs" (transcription). If Arn is a "named NPC", the roster would bring him to the temple. The campaign files say he is not there. The campaign wins; flag for the Cassalanter Villa journal.

**D8. Household residence**
- `campaign/setting/organizations/10-cassalanters.md:52` counts him among "the villa employs sixteen named staff".
- `campaign/setting/organizations/10-cassalanters.md:53` and `southern-ward.md:62` place him at the Windmill.
- `10-cassalanters.md:48`: "Only the family, its personal attendants and its guards live in the house".
- Not a strict conflict: he is on the staff list and lives elsewhere. The Background must choose a single description.

---

## E. Stale lines in other files (not edited)

- `campaign/gazetteer/waterdeep/southern-ward.md:252`: "Arn's page states no pronouns and no Tethyrian origin, so he/him comes from the page's \"the man\" (`11-arn-xalrondar.md:26`) and Dragon Heist's \"male Tethyrian human\" (`:13211`)." Stale. The page's line 5 now reads "Tethyrian human ... he/him", and line 26 is not "the man".
- `campaign/gazetteer/waterdeep/southern-ward.md:133` and `11-arn-xalrondar.md:21`: the handprints claim (D5), unsourced.
- `campaign/gazetteer/waterdeep/southern-ward.md:137` and `11-arn-xalrondar.md:21`, `:25`: the Stone or the Eye (D2). The gazetteer says Eye; the page says Stone.
- `campaign/structure/arc-g-cassalanter-villa.md:21`: "her lieutenant" (D1).
- `campaign/structure/arc-g-cassalanter-villa.md:100`: "Pragmatic, not devout" and "surrenders" (D3).
- `campaign/guides/factions/11-cassalanters.md:62` and `:45`: "Cultist Fanatic" (D6).
- `campaign/setting/organizations/10-cassalanters.md:52`: Arn among the sixteen named staff (D8).

**Routed quest references (where the events live; none is a day-one fact)**
- Windmill mini-heist and Arn's getaway role: `campaign/structure/arc-e-faction-outposts.md:271`-`:287` (Faction Outposts, Scene 6B).
- Asmodean Shrine Book of Worship and "Meeting Ches 17th" note: `arc-e-faction-outposts.md:249`, `:257`, `:265`, `:281`.
- Seffia's letter (the Eye): `arc-e-faction-outposts.md:283` ("this letter requires either stealth or a confrontation to obtain").
- The devils taking the Eye: `southern-ward.md:137`; `10-seffia-naelryke.md:99`; `sources/adventure-wdh.json:13228`.
- The Cult Gathering: `campaign/structure/arc-g-cassalanter-villa.md:100` ("Has never entered the temple").
- Vaelle Lurval and the dead cultists: `sources/adventure-wdh.json:8316`-`:8319`. No campaign quest event names Vaelle (`10-seffia-naelryke.md:98`).

---

## F. Gaps a Background would need that no source gives

For each gap: the sourced facts the drafter must stay consistent with.

- **F1. Origin, birthplace, family, childhood, age.** No source. Constraints: Tethyrian human (B); male (`adventure-wdh.json:13211`); no campaign file gives a city of origin beyond the Southern Ward residence.
- **F2. How he came to the cult and when.** No source. Constraints: he is a cult fanatic by Ches 1 (`asmodeus.md:72`: "Tissina Khyret, Laiba \"Nana\" Rosse, Jandar Chergoba, Seffia Naelryke and Arn Xalrondar are cult fanatics."). He has "never set foot in the temple" (`arc-g-cassalanter-villa.md:21`). The cult's founding and recruitment are undated (`10-cassalanters.md:178`, a Draft Notes entry).
- **F3. How he got the partner or lieutenant role.** No source. Constraints: Seffia commands; Victoro sent both on the Brandath mission (`adventure-wdh.json:13219`; `10-cassalanters.md:29`).
- **F4. Time in post and the move into the Windmill.** No source. Constraints: the Windmill's use "for years" is Brimel's deliveries (`southern-ward.md:63`). Ammalia's visits are "twice a month" (`southern-ward.md:68`).
- **F5. What he knows of the pact, Osvaldo and the twins.** No source. Constraints: "Victoro and Ammalia have told no one." (`10-cassalanters.md:96`); "Willifort knows." (`10-cassalanters.md:129`); the six named cult members are the people who "know what lies beneath" (`arc-g-cassalanter-villa.md:21`), which includes Arn. Nobody outside the household and the cult knows about the pact, so Arn's knowledge is a cult-level question.
- **F6. His relationship to Vaelle Lurval, Holiver Tornrudder and Kaeth Warloon.** No campaign tie. Constraints: the adventure gives only the killing (`adventure-wdh.json:8316`) and Vaelle's identity (`:8317`).
- **F7. Family, home, or a person he cares for besides Seffia.** No source.
- **F8. His own craft or work before the cult.** No source. Constraints: "handles field security for the outposts" (`arc-g-cassalanter-villa.md:21`); "handles outpost logistics" (`arc-g-cassalanter-villa.md:100`).
- **F9. The handprints.** No source for the villa handprints (D5). The apartment handprints are sourced only by `southern-ward.md:133`. Keep as `[research]` or drop.
- **F10. Whether he attends the Cult Gathering.** Ambiguous (D7).
- **F11. What he wants for himself.** No source. Motivations (line 15) and Emotions (line 13) are the only wants: "do what the mission requires", "keep the Windmill operational", "trust Seffia's judgment". The personal-goals paragraph must belong to the person (brief ruling 17), and Motivations and Emotions stay verbatim.

---

## G. Inner-life hints (exact quotes)

- Arn page, line 13: "the particular focus of someone who does what the mission requires without auditing it"
- Arn page, line 15: "trust Seffia's judgment on everything except the moments she is not in the room."
- `cassalanters.md:195`: "Short, deferential agreements, then, alone and under pressure, a sudden, firm decision."
- `cassalanters.md:197`: "Nervous curses, until he decides."
- `cassalanters.md:198`: "Subordinate devotion that turns into initiative."
- `cassalanters.md:199`: "He checks for Seffia before answering."
- `cassalanters.md:201`: "He never questions Seffia to her face, never regrets the devil, and never speaks of his faith to outsiders."
- `cassalanters.md:203`: "Seffia's not here. You should go."
- `arc-g-cassalanter-villa.md:100`: "Pragmatic, not devout — if the operation is clearly failing, he surrenders and cooperates for clemency."
- `10-seffia-naelryke.md:32`: "Unresolved: he acts on his own when she is out of the room, as when he sent the Eye off with a spined devil."
- `sources/adventure-wdh.json:13219`: "Arn and Seffia would be horrified to learn that they failed in so simple a task"
- `sources/adventure-wdh.json:13228`: "The cult fanatics do everything in their power to enable the devils to escape."
- Book of Worship, `sources/5. Faction Outposts.pdf` printed p.39: "contains a number of \"high prayers\" to Asmodeus" and "in simple handwriting" (transcription).
- `southern-ward.md:137` (quest-time, do not restate as day-one): "he believes the decision was correct."

No line gives a personal goal beyond Motivations and Emotions.

---

## Cross-references (every `file:line` where Arn appears)

- `campaign/setting/organizations/10-cassalanters.md:29`, `:51`, `:52`, `:53`, `:96`, `:102`, `:103`, `:117`, `:121`, `:129`, `:178`
- `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:55`, `:133`
- `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:41` (Rella and Ivrala only; no Arn tie)
- `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:22`, `:25`, `:32`, `:40`, `:62`, `:75`, `:86`, `:98`, `:99`
- `campaign/setting/deities/asmodeus.md:72`
- `campaign/gazetteer/waterdeep/southern-ward.md:36`, `:62`, `:63`, `:68`, `:69`, `:129`, `:131`, `:132`, `:133`, `:137`, `:252`
- `campaign/guides/factions/11-cassalanters.md:31`, `:45`, `:53`, `:62`, `:89`, `:107`
- `campaign/structure/arc-e-faction-outposts.md:249`, `:257`, `:265`, `:271`, `:281`, `:283`, `:285`
- `campaign/structure/arc-g-cassalanter-villa.md:15`, `:21`, `:91`, `:100`
- `sources/adventure-wdh.json:69`, `:70`, `:8316`, `:8317`, `:8318`, `:8319`, `:13211`, `:13218`, `:13219`, `:13228`
- `sources/SOURCE_GUIDE.md:687` (the Cassalanter backstory .docx, not readable)

## Not found

Searched for `Arn`, `Xalrondar`, `Book of Worship`, `Windmill`, `Coachlamp`, `handprint`, `cult fanatic`:
- Campaign: all of `campaign/`. Arn appears only in the files above. No Arn line in `campaign/setting/villains/cassalanters.md`, `campaign/setting/history/`, `campaign/locations/cassalanter-villa/`, or `campaign/guides/gm-guide/`.
- Adventure: `sources/adventure-wdh.json` (every match listed above; no Arn match in Appendix B or the Ch.6 villa text).
- Alexandrian: PDFs 5, 6, 7 (PDF pp.1-3), 10 (p.5), 17 (p.2) read. The other PDFs were not read for Arn. The Osvaldo notes read PDFs 1 (pp.6-7) and 10 (pp.1-6) for other figures and found no Arn line there.
- Appendices B, C, D and `Act_III_Arc_E.md`: grep for `Xalrondar|Arn\b|Windmill|Book of Worship` returned no Arn line in any of them. Appendix D matched only on Rella and Ivrala (see the Rella notes).
- Wiki: no `NOT FOUND` text. `sources/research/**/wiki*` contains no Xalrondar line.
- `sources/Other remix files/`: `Cassalanters, their tragic backtstory, and Endgame setup.docx` (not readable; `SOURCE_GUIDE.md:687` says it covers the Victoro and Ammalia backstory), and `The Waterdavian's Guide to Waterdeep NPCs (...).docx` (not readable; `SOURCE_GUIDE.md:695` lists it as a secondary NPC reference).
- Vaelle Lurval: no Notable Figures page or campaign event (`10-seffia-naelryke.md:98`).

## Not readable

- `sources/Other remix files/Cassalanters, their tragic backtstory, and Endgame setup.docx`: the SOURCE_GUIDE says it covers the "Victoro & Ammalia backstory, the soul-pact timeline, the children's situation, endgame resolution paths" (`sources/SOURCE_GUIDE.md:687`). It may hold Arn or Seffia material. Needs extraction (`.docx` cannot be opened with these tools).
- `sources/Other remix files/The Waterdavian's Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx`: a secondary NPC reference (`sources/SOURCE_GUIDE.md:695`). It may name Arn. Needs extraction.
