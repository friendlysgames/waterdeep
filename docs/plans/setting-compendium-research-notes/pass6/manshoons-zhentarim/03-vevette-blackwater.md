# Pass 6 research notes: Vevette Blackwater

Page: `campaign/setting/notable-figures/manshoons-zhentarim/03-vevette-blackwater.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md` (the `manshoons-zhentarim/06-ott-steeltoes.md` path named in the generic instructions does not exist; the Ott notes are in the `xanathars-guild` folder)
Day-one frame used: Ches 1, 1492 DR. Vevette is one of Manshoon's lieutenants, at Kolat Towers, holding a pass-amulet and a teleporter signet ring. Everything about the Stone theft, the chase, the theater, the Kolat Towers fight and the Doom Raiders letters is quest-time (section C and E).
Pass 5 ruling on her alignment: `docs/plans/setting-compendium-pass5-brief.md:80`, quoted in full in D1.

Method and caveats:
- Campaign files: Read and Grep, quoted from the file. Line numbers are from tool output.
- Published adventure: `sources/adventure-wdh.json`. Quotes are the JSON string. `{@creature ...}` tags are left as written. JSON escapes (`\"`) are shown as plain quotes.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. The PDF quotes below were transcribed from the rendered page images. Each one is marked **[image transcription]**. Check every one against `pdftotext -layout` before it goes into prose.
- Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-manshoons-zhentarim/03-vevette-blackwater.txt` (the Forgotten Realms Wiki page for Vevette Blackwater). Its citation keys are `WDH5e-p76`, `WDH5e-p148`, `WDH5e-p158` and `WDH5e-p4`, which are *Waterdeep: Dragon Heist* 5e. The wiki's prose prints no edition, so it is tagged 5e from the key. A second wiki line is in the fandom dump (see A11).
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written.

---

## A. Background facts by theme

### A1. Origin and childhood

**Abuse and recruitment (Alexandrian, the only source for a childhood)**
> "VEVETTE BLACKWATER: When she was a young girl, Vevette was abused by her mother. A Zhentarim agent came to her when she was twelve, put a blade in her hand, and asked if she wanted to take control of her life. She did. And she's been in the Black Network ever since."
> — `sources/5. Faction Outposts.pdf`? No: `sources/6. Faction Response Teams.pdf`, printed p.55 [PDF p.7] (section "ZHENTARIM RESPONSE TEAMS") **[image transcription]**

> "Vevette's past manifests itself in a deep streak of cruelty and ruthlessness, but to most outward appearance she is a charming bon vivant. She has fiery red hair with two streaks of brilliant platinum, which can actually glow on her command."
> — `sources/6. Faction Response Teams.pdf`, printed p.55 [PDF p.7] **[image transcription]**

Context: these are the first two paragraphs of the Alexandrian's Vevette entry. The entry continues with the Seffia card (see A5). The Alexandrian gives no mother's name, no birthplace and no date for the recruitment. Nothing else in the campaign or the adventure says the mother was abusive, so this is an Alexandrian-only fact.

**Campaign and adventure: no childhood, no family, no birthplace.** Searched; see F1.

### A2. Former life before the Zhentarim

> "Vevette was a vicious pirate before she joined the Zhentarim and rose to become one of {@creature Manshoon|WDH}'s favored lieutenants. She cackles madly in the face of danger and loves a good chase. She knows the streets, alleys, and rooftops of Waterdeep well."
> — `sources/adventure-wdh.json:8532` (keyed encounter "Rooftop Chase: Winter", page 72, id `18d`; rest of the passage covers chase mechanics)

Generic corroboration only, not about Vevette (the adventure's Appendix B entry for the monster type "Swashbuckler", page 216):
> "{@creature Swashbuckler|VGM|Swashbucklers} are charming ne'er-do-wells who live by their own codes of honor. They crave notoriety, often indulge in romantic trysts, and eke out livings as pirates and corsairs, rarely staying in one place for too long."
> — `sources/adventure-wdh.json:32599` (section `Swashbuckler`, `:32595`, page 216)

Wiki: no pirate years. The wiki's lead line is the only biography line (see A11).

### A3. How she rose, and her rank

> "Vevette and Agorn are two of {@creature Manshoon|WDH}'s most trusted followers. Vevette commands the wizard's forces against the Xanathar Guild, while Agorn commands those who oppose the Zhents that aren't loyal to {@creature Manshoon|WDH}. At the moment, they are resting in the sanctum while awaiting orders from {@creature Manshoon|WDH}."
> — `sources/adventure-wdh.json:30130` (keyed area E8, the brazier room; section "Zhents", id `426`, page 159)

> "Manshoon's response teams consist of: 1 lieutenant (Vevette, Urstul, or Agorn) 3-4 thugs"
> — `sources/6. Faction Response Teams.pdf`, printed p.55 [PDF p.7] **[image transcription; the bullets are listed as separate lines in the image]**

> "Vevette was one of the lieutenants of Manshoon."
> — `wiki` (scratchpad file `03-vevette-blackwater.txt`, line 71, citation `WDH5e-p148`)

Rank: the adventure says "lieutenants" and "most trusted followers". The wiki says "high-ranking member" (line 62). The campaign says "most trusted field lieutenant" (NF page, Relationships; see C, row 25) and "coordinates strike teams from Kolat Towers" (`campaign/setting/organizations/09-manshoons-zhentarim.md:58`, quoted in A4).

### A4. Her job in the cell (campaign, day-one)

> "- **Lieutenants and field teams:** Urstul Floxin is the chief field operative and leads the thugs who work the streets. Vevette Blackwater coordinates strike teams from Kolat Towers and leads the forces that fight Xanathar's Guild, and in the published adventure Agorn Fuoco leads those that fight the Zhents who are not loyal to Manshoon (**Vevette Blackwater**; *Dragon Heist*, 5e). Vira Solkan is a plant inside Blackstaff Tower (**Castle Ward**)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:58`

> "**Vevette Blackwater** — swashbuckler + 3–4 **thugs**."
> — `campaign/guides/factions/10-manshoons-zhentarim.md:11`

> "All three Zhentarim response teams consist of a lieutenant plus 3–4 **thugs**. Every lieutenant carries a pass-amulet to Kolat Towers and will try to destroy it if capture seems certain, except Agorn, who trades his to save himself."
> — `campaign/guides/factions/10-manshoons-zhentarim.md:7`

> "- **Sidra Romeir** — Calishite human veteran, lawful evil, and Manshoon's most trusted lieutenant, stationed at Kolat Towers. She holds the teleport rings when lieutenants leave the Towers, and if captured lieutenants are killed she gives their rings to Kaevja `[research]`. See the **Sidra Romeir** page in Notable Figures."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:97` (Sidra's line; given here because it governs the ring custody Vevette's team uses)

### A5. Belongings

**Pass-amulet and teleporter ring**
> "All of Manshoon's lieutenants carry pass-amulets to Kolat Towers (see Part 4), but will attempt to destroy them if it looks as if they are being captured. (Except Agorn, that feckless weasel, who will attempt to barter it for his own life.) They leave their teleport rings with Sidra Romeir when journeying outside Kolat Towers."
> — `sources/6. Faction Response Teams.pdf`, printed p.55 [PDF p.7] **[image transcription; the parenthesis about Sidra and Kaevja after this sentence is not quoted]**

> "* Has a teleporter signet ring."
> — `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p.94 [PDF p.3], roster footnote; the roster row reads "Vevette Blackwater* + Agorn Fuoco*" **[image transcription; the row alignment in the roster is layout-dependent, so the room column is not used]**

> "Manshoon's lieutenants wear special rings that let them access Manshoon's sanctuary atop the Outer Tower (although they don't know that this is actually an extradimensional space; they think he just lives up there)."
> — `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p.95 [PDF p.4] **[image transcription]**

**Potions**
> "Vevette's chest has three {@item potion of healing||potions of healing}."
> — `sources/adventure-wdh.json:30221` (sanctum sleeping room, section "Treasure", id `42d`, page 160)

**Seffia Naelryke's visiting card**
> "Vevette carries Seffia Naelryke's Visiting Card. It gives Seffia's address as "the Windmill on Coachlamp Lane". (GM Note: Seffia approached Vevette in order to open a discrete line of communication between the Cassalanters and Manshoon, but her overtures were rebuffed. After their experiences with Xanathar, the Zhentarim suspected a trap.)"
> — `sources/6. Faction Response Teams.pdf`, printed p.55 [PDF p.7] **[image transcription]**

> "Seffia approached Vevette in order to open a discrete line of communication" — see the same PDF. The campaign's own form of the card is in `campaign/setting/notable-figures/manshoons-zhentarim/03-vevette-blackwater.md:21` (quoted in C, row 21) and `campaign/guides/factions/11-cassalanters.md:88` (quoted in D4).

**Revelation list entries**
> "Seffia Naelryke's Visiting Card (Response Team: Vevette Blackwater)"
> — `sources/17. Outpost and Lair Revelation Lists.pdf`, printed p.123 [PDF p.3] **[image transcription; under CONVERTED WINDMILL]**

> "Report to Agorn Fuoco (Response Team: Vevette Blackwater)"
> — `sources/17. Outpost and Lair Revelation Lists.pdf`, printed p.123 [PDF p.3] **[image transcription; under XANATHAR SEWER HIDEOUT, TAKE 2]**

Context: the second entry is a Xanathar-side revelation carried by Vevette's team. The campaign files treat it as the Xanathar's Guild revelation (`campaign/setting/organizations/09-manshoons-zhentarim.md`, Draft Notes, line 165, names the Agorn report as a Factions Guide mechanic on `09-xanathars-guild.md` line 95).

### A6. Where she sleeps and works

> "{@creature Kaevja Cynavern|wdh}, Vevette Blackwater, Agorn Fuoco, {@creature Zhent Martial Arts Adept|wdh|Havia Quickknife}, and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush} all sleep here."
> — `sources/adventure-wdh.json:30212` (sanctum room with five beds, id `42c`, page 160)

> "Vevette resided inside [[Kolat Tower]] with her master Manshoon."
> — wiki (scratchpad file, line 65, citation `WDH5e-p158`)

> "- **Kaevja Cynavern** ..." — not quoted; see A7.

Campaign: `campaign/structure/arc-i-kolat-towers.md:156` places her in the Reading Room (quoted in E2). The adventure has her in the sanctum brazier room (30130) and in the sleeping room (30212). The two adventure rooms are different; the campaign file does not use the sleeping room.

### A7. Relationships (sourced)

**Agorn Fuoco (fellow lieutenant, shared sanctum room)**
> "Vevette takes a seat behind them and surreptitiously passes the {@item Stone of Golorr|WDH} to Agorn."
> — `sources/adventure-wdh.json:9133` (theater scene, page 76; rest of the passage covers Agorn, Amath Sercent and the Harper Remallia Haventree in the audience; this sentence is quest-time, see C and E)

Relationship with Agorn beyond shared duty: no source (F5).

**Kaevja Cynavern, Havia Quickknife, Mookie Plush**
> See A6, `sources/adventure-wdh.json:30212`. Kaevja's role as sanctum alarm: `campaign/setting/organizations/09-manshoons-zhentarim.md:55` (Structure paragraph, "The sanctum"). No source says how Vevette feels about them.

**Sidra Romeir**
> See A4, `campaign/setting/organizations/09-manshoons-zhentarim.md:97` (Sidra gives the rings out).

**Manshoon**
> See A3, `sources/adventure-wdh.json:30130` ("two of {@creature Manshoon|WDH}'s most trusted followers"). Campaign: `campaign/setting/notable-figures/manshoons-zhentarim/03-vevette-blackwater.md:25` ("Manshoon's most trusted field lieutenant").

**Seffia Naelryke (Cassalanters, rebuffed)**
> "- **Vevette Blackwater:** Seffia approached her to open a channel between the Cassalanters and the Zhentarim, and Vevette refused, suspecting a trap. Unresolved: no contact since, and Vevette still carries Seffia's visiting card, which gives the Windmill's address."
> — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:36`

**Doom Raiders**: no source ties Vevette to the Doom Raiders. See Two Zhentarims (E3).

### A8. Name, pronunciation

> "Vevette Blackwater",
> "veh-VET"
> — `sources/adventure-wdh.json:357-358` (pronunciation index entry; the adventure's index is an array of two-string entries)

Wiki pronunciation: `{{Pronounce|veh|VET|refs=...WDH5e-p4...}}` (scratchpad file, line 62).

### A9. Faith

No source. The adventure does not name a deity for her, and the wiki's infobox has no `patron deity` value (scratchpad file, lines 16–18). Campaign: no faith line. See F6.

### A10. Quest-era summary that is day-one: the Stone is not in her hands on Ches 1 in the campaign

Campaign: `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:47`–`:53` (quoted in D2). Do not write a Vevette biography that has her holding the Stone on Ches 1 without a routing line.

### A11. Wiki lines (lower rank; editions tagged as the key gives them)

> "'''Vevette Blackwater''' ({{Pronounce|veh|VET|refs=<ref name="WDH5e-p4">{{Cite book/Waterdeep: Dragon Heist|4}}</ref>}}) was a high-ranking member of [[Manshoon]]'s [[Zhentarim]] in [[Waterdeep]] during the early 1490s [[DR]].<ref name="WDH5e-p148" />"
> — wiki (scratchpad file, line 62; 5e tagged from key `WDH5e-p148`)

> "Vevette resided inside [[Kolat Tower]] with her master Manshoon.<ref name="WDH5e-p158">{{Cite book/Waterdeep: Dragon Heist|158}}</ref>"
> — wiki (scratchpad file, line 65)

> "In [[1492 DR]],{{WDH-time}} if [[Manshoon]] managed to obtain the ''[[Stone of Golorr]]'', after the [[Xanathar's Thieves' Guild]] and some adventurers discovered the ''Stone'''s hiding place devised by the [[dragonborn]] butcher [[Thrakkus]],<ref name="WDH5e-p64">{{Cite book/Waterdeep: Dragon Heist|64}}</ref> Vevette was instructed to deliver the ''Stone'' to the fellow [[Zhent]] [[Agorn Fuoco]] and she managed to deliver it during a performance at the [[Trades Ward of Waterdeep|Trades Ward]] theater called the [[Brizzenbright]].<ref name="WDH5e-p76" />"
> — wiki (scratchpad file, line 68; 5e tagged from key `WDH5e-p76`). Conflicts with the campaign's Stone path (D2) and the theater location (D6).

> "Vevette was one of the lieutenants of Manshoon."
> — wiki (scratchpad file, line 71; `WDH5e-p148`)

Wiki stat and class: `| alignment5e = [[Chaotic evil]]` (line 57); `| class5e = [[Swashbuckler]]` (line 59); `| refs5e = <ref name="WDH5e-p76">` (line 60).

Fandom dump, the "Swashbuckler" page, section "Individuals" (`/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/fandom-dump/forgottenrealms_pages_current.xml`, line 4989891):
> "* [[Vevette Blackwater]], one of the high-ranking officers within the reformed [[Zhentarim]].<ref name="WDH-p97">{{Cite book/Waterdeep: Dragon Heist|97}}</ref>"
> — wiki, edition tagged from key `WDH-p97` (Dragon Heist, 5e inferred). "Reformed Zhentarim" conflicts with the campaign's "reforming a council" wording (D10).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, the page: "*Tethyrian human swashbuckler, lawful evil, she/her*. Stat block: **Swashbuckler**." — `campaign/setting/notable-figures/manshoons-zhentarim/03-vevette-blackwater.md:5`
- Campaign, the organization page: "- **Vevette Blackwater** — Tethyrian human swashbuckler, lawful evil, with fiery red hair streaked platinum that can glow in the dark on her command, charming in public and cruel in private. Seffia Naelryke approached her to open a Cassalanter–Zhentarim communication channel, but Vevette rebuffed her, suspecting a trap, and kept Seffia's visiting card. See the **Vevette Blackwater** page in Notable Figures." — `campaign/setting/organizations/09-manshoons-zhentarim.md:98`
- Campaign, ruling: "Vevette Blackwater is lawful evil (her page)." — `docs/plans/setting-compendium-pass5-brief.md:80`
- Campaign, Trollskull guide: "**Who comes:** Vevette Blackwater (CE swashbuckler, fiery red hair with two platinum streaks) — alone or with two thugs in decent clothes." — `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:40` (**CE**, conflicts; see D1)
- Adventure: "Vevette Blackwater (CE female Tethyrian human {@creature swashbuckler|VGM}; see {@adventure appendix B|WDH|12})" — `sources/adventure-wdh.json:7203` (also `:7734`, `:8531`, `:9132`, `:14783`, `:30120`; all CE)
- Alexandrian, Zhentarim Response Teams: "Stats: CE female Tethyrian human swashbuckler (DH p. 216)." — `sources/6. Faction Response Teams.pdf`, printed p.55 [PDF p.7] **[image transcription]**
- Alexandrian, Kolat Towers stat reference: "Vevette Blackwater (CE female Tethyrian human) – swashbuckler, DH p. 216" — `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p.95 [PDF p.4] **[image transcription]**
- Alexandrian appendix: "**Who comes:** Vevette Blackwater — fiery red hair with two platinum streaks, CE swashbuckler, arrives alone or with two thugs in decent clothes. She is charming, laughs easily, and will absolutely try to extract information through conversation before she tries anything else." — `sources/Appendix_D_-_Running_the_Tavern.md:1549`
- Wiki: "| alignment5e     = [[Chaotic evil]]" — scratchpad file, line 57 (text is `| alignment5e = [[Chaotic evil]]`; the value is "Chaotic evil")

**Species and ethnicity**
- Campaign: "*Tethyrian human swashbuckler, lawful evil, she/her*" (`03-vevette-blackwater.md:5`). Tethyrian is a Faerûn ethnicity (brief ruling 5). Consistent everywhere.
- Adventure: "Vevette Blackwater (CE female Tethyrian human" — `sources/adventure-wdh.json:7203`
- Wiki: "| race           = [[Human]]" (scratchpad line 14); "| ethnicity      = [[Tethyrian]]" (line 15)

**Pronouns**
- Campaign: "she/her" (`03-vevette-blackwater.md:5`).
- Adventure: "female" (`sources/adventure-wdh.json:7203`); "she" (`:8532`: "Vevette was a vicious pirate before she joined the Zhentarim").
- Wiki: "| sex            = Female" (scratchpad line 13).

**Stat block**
- Campaign: "Stat block: **Swashbuckler**." (`03-vevette-blackwater.md:5`)
- Adventure: "{@creature swashbuckler|VGM}" (tag, all instances above). Appendix B has a generic "Swashbuckler" monster entry at page 216 (`sources/adventure-wdh.json:32595`), and it contains no Vevette entry (see F and E).
- Alexandrian, Zhentarim Response Teams: "(DH p. 216)" after the stat line (see B alignment quote above). The same page cites "DH p. 216" for Urstul's assassin stat and for Agorn's bard stat block at p.195.
- Alexandrian, Sea Maidens Faire stat reference, printed p.76 [PDF p.8]: "Khafeyta – female Mulhorandi human swashbuckler (DH p. 216)" **[image transcription]**. This shows the Alexandrian uses DH p.216 for the generic swashbuckler stat, not for a named person.
- Wiki: "| class5e        = [[Swashbuckler]]" (line 59), "refs5e" citing `WDH5e-p76` (line 60).

**Appearance (for name tag and Overview)**
- Campaign: "fiery red hair streaked platinum that can glow in the dark on her command" (`03-vevette-blackwater.md:21`)
- Alexandrian: "She has fiery red hair with two streaks of brilliant platinum, which can actually glow on her command." — printed p.55 **[image transcription]**
- Appendix D: "fiery red hair with two platinum streaks" (`Appendix_D_-_Running_the_Tavern.md:1549`)

---

## C. Every sentence on the current page

Current page: `campaign/setting/notable-figures/manshoons-zhentarim/03-vevette-blackwater.md`. The page has no `> Structuring draft.` line and no `## Background`, `## Personality`, `## Connections`, `## Source References` or Draft Notes yet. Its sections are: H1, Gamemaster's Summary, Roleplaying Information (Resonance, Emotions, Motivations, Inspirations), Character Information (Persona, Morale, Relationships), Overview.

"Day-one OK" means no quest gate is needed. "Quest-time" means the sentence narrates a theft, chase, capture, theater scene or Kolat Towers fight.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L1 | "# Vevette Blackwater" | n/a | n/a |
| 2 | L5 | "*Tethyrian human swashbuckler, lawful evil, she/her*. Stat block: **Swashbuckler**." | Day-one. Alignment conflicts (B, D1) | `organizations/09-manshoons-zhentarim.md:98`; `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:40` (CE) |
| 3 | L6 | "**Affiliation:** Manshoon's Zhentarim" | Day-one OK | `organizations/09-manshoons-zhentarim.md:1` (page title "Manshoon's Zhentarim"); `campaign/guides/factions/10-manshoons-zhentarim.md:1` |
| 4 | L7 | "**Featured in:** **Faction Outposts**, **Sea Maidens Faire**, **Kolat Towers**; **Silencing Skeemo**, **The Yellowspire Job**" | Quest references. The Summary bullet is allowed, but these are routed (E2) | `structure/arc-e-faction-outposts.md:213`; `structure/arc-h-sea-maidens-faire.md:204`; `structure/arc-i-kolat-towers.md:156`; `quests/faction-events/doom-raiders/m04-silencing-skeemo/overview.md:58`; `quests/faction-events/doom-raiders/m05-the-yellowspire-job/overview.md:80` |
| 5 | L11 | "**Resonance.** Vevette should inspire reluctant respect for her audacity (stealing the Stone and fleeing across icy rooftops), wariness with her charm-in-public / cruelty-in-private duality, and satisfaction when the party outmaneuvers her." | Mixed. "stealing the Stone and fleeing across icy rooftops" is quest-time, and it conflicts with the campaign Stone path (D2). The rest is day-one | Theft: `sources/adventure-wdh.json:6747`, `:8531`; campaign Stone path: `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:49`–`:53` |
| 6 | L13 | "**Emotions.** Vevette most often feels confident calculation, theatrical charm, predatory amusement, cold cruelty behind closed doors, operative's pride in her fieldwork, and measured disdain for anyone she considers beneath her." | Day-one | Persona (L21), `sources/adventure-wdh.json:8532` ("cackles madly") for predatory amusement; `sources/6. Faction Response Teams.pdf` p.55 (charm, cruelty) |
| 7 | L15 | "**Motivations.** Vevette wants to serve Manshoon's interests while positioning herself for advancement, keep the Stone in Zhentarim hands, and avoid imprisonment by exploiting the law." | "keep the Stone in Zhentarim hands" is a goal, but the campaign has the Stone with Xanathar's Guild until Ches 20 (D2). "avoid imprisonment by exploiting the law" is day-one | `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:50`–`:51`; `sources/adventure-wdh.json:7741` (the law sentence) |
| 8 | L17 | "**Inspirations.** When playing Vevette, channel Catwoman (*Batman Returns*), Cersei Lannister (*Game of Thrones*), and Irene Adler (*Sherlock Holmes*)." | Not a fact | n/a |
| 9 | L21 (a) | "**Persona.** To the world, Vevette is a swashbuckler with fiery red hair streaked platinum that can glow in the dark on her command." | Day-one | A5 (Alexandrian, appearance) |
| 10 | L21 (b) | "Charming in public, cruel in private." | Day-one | Organization page `:98` (same words) |
| 11 | L21 (c) | "To those she trusts, she carries Seffia Naelryke's visiting card, having rebuffed a Cassalanter backchannel offer she suspected was a trap." | Day-one. The rebuff is before Ches 1 ("no contact since", `campaign/setting/organizations/10-cassalanters.md:86`). The card is a revelation prop; holding it is day-one | `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:36`; `campaign/guides/gm-guide/running-the-villains.md:74` |
| 12 | L21 (d) | "Deep down, she is counting on the law to protect her from serious harm if captured, and she knows she has done nothing to warrant arrest." | Day-one trait. Its source is a quest-chapter line (the capture text), so keep it as a trait | `sources/adventure-wdh.json:7741` ("She's counting on the law to protect her from serious harm, and she knows she has done nothing to warrant arrest.") |
| 13 | L23 (a) | "**Morale.** In a fight, Vevette flees across rooftops with acrobatic skill." | Borderline. Fleeing by rooftop is the chase behaviour. The campaign has no Vevette chase; the adventure does | `sources/adventure-wdh.json:8532` ("she can take the Dash action during the chase"); `:8539` |
| 14 | L23 (b) | "If caught, she surrenders and relies on legal protection." | Quest-time (capture). The trait behind it is day-one (row 12) | `sources/adventure-wdh.json:7741` ("If she is caught, Vevette surrenders.") |
| 15 | L23 (c) | "She does not willingly reveal who has the Stone unless magically compelled." | Quest-time (the Stone was taken from her and given away in the theater). Conflicts with the campaign Stone path (D2) | `sources/adventure-wdh.json:7741` ("She doesn't willingly divulge who has the stone, though the characters can pry the information from her using a {@spell charm person} spell or similar magic.") |
| 16 | L25 (a) | "**Relationships.** Vevette is Manshoon's most trusted field lieutenant, the coordinator of strike team deployments from Kolat Towers, and a swashbuckler whose operational relationship with the Cassalanters consists of a rebuffed contact and a kept visiting card." | Day-one, except that "most trusted" is the adventure's "most trusted followers" (`:30130`) and needs the "field" qualifier. The coordinating role is day-one in the campaign (`organizations/09-manshoons-zhentarim.md:58`) and is also a quest prop (E2) | `organizations/09-manshoons-zhentarim.md:58`; `sources/adventure-wdh.json:30130` |
| 17 | L27 | "A swashbuckler with fiery red hair streaked with platinum that glows on her command." | Day-one | A5 (Alexandrian) |
| 18 | L27 | "She is charming in public, skilled at navigating the law's edges, and takes no assignment she considers beneath her." | Day-one. "skilled at navigating the law's edges" has no source beyond the Alexandrian "bon vivant" and the voice profile (no source for legal skill) | `sources/6. Faction Response Teams.pdf` p.55 (bon vivant); `03-vevette-blackwater.md:13` (beneath her) |

**Voice profile (`.claude/skills/character-voices/voices/manshoons-zhentarim.md`, lines 49–63), quest-time clauses:**
- Line 57 (Quirks): "She makes her hair glow for emphasis. She reminds people she's done nothing they can prove." Day-one.
- Line 60–62 (Sample lines), Business: "*Business:* \"I took it because I was asked to. Who asked is a matter for my advocate.\"" Quest-time. "I took it" is the Stone theft (`sources/adventure-wdh.json:6747`, `:8531`). Restate for the page or change the line.
- Line 63 (Sample lines), Under pressure: "*Under pressure:* \"Catch me on those rooftops, if you can.\" (her hair flares, and she's gone)" Chase line. The only chase is the adventure's (`sources/adventure-wdh.json:8531`–`:8539`). Restate or change.
- Everything else in the profile (tagline, Sound, Sentence shape, Word choice, Swearing, Personality in speech, Signature phrases, Never, Greeting sample line) is day-one. The Swearing line stays.

---

## D. Conflicts

**D1. Alignment: lawful evil against chaotic evil (the most important one)**
- Lawful evil, campaign: "*Tethyrian human swashbuckler, lawful evil, she/her*" (`campaign/setting/notable-figures/manshoons-zhentarim/03-vevette-blackwater.md:5`); "Tethyrian human swashbuckler, lawful evil, with fiery red hair streaked platinum" (`campaign/setting/organizations/09-manshoons-zhentarim.md:98`); pass 5 ruling "Vevette Blackwater is lawful evil (her page)." (`docs/plans/setting-compendium-pass5-brief.md:80`).
- Chaotic evil, published adventure: "Vevette Blackwater (CE female Tethyrian human {@creature swashbuckler|VGM}; see {@adventure appendix B|WDH|12})" at `sources/adventure-wdh.json:7203`, `:7734`, `:8531`, `:9132`, `:14783`, `:30120`.
- Chaotic evil, Alexandrian: "Stats: CE female Tethyrian human swashbuckler (DH p. 216)." (`sources/6. Faction Response Teams.pdf`, printed p.55 [PDF p.7]) **[image transcription]**; "Vevette Blackwater (CE female Tethyrian human) – swashbuckler, DH p. 216" (`sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p.95 [PDF p.4]) **[image transcription]**; "CE swashbuckler" (`sources/Appendix_D_-_Running_the_Tavern.md:1549`).
- Chaotic evil, wiki: "| alignment5e = [[Chaotic evil]]" (scratchpad line 57).
- Chaotic evil, a campaign file (conflicts with the rest of the campaign): "**Who comes:** Vevette Blackwater (CE swashbuckler, fiery red hair with two platinum streaks)" (`campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:40`).
- Where the lawful evil label came from: the old organization page is quoted in a bundle copy, "- **Vevette Blackwater** (DH p. 216) — Human swashbuckler, lawful evil." (`sources/research/pass4-bundles/cassalanters/campaign-hits.txt:843`, a copy of `organizations/09-manshoons-zhentarim.md:25` as it stood). It cites DH p.216, which is the generic Swashbuckler entry (`sources/adventure-wdh.json:32595`), and that entry gives no alignment for any named swashbuckler. No source found that gives lawful evil.
- Higher-ranked source: the campaign files (lawful evil) outrank the adventure, and the pass 5 ruling is a main-session decision. But one campaign file (the Trollskull guide, line 40) says CE, and the org page's own Draft Notes say "chaotic evil in the published adventure (`adventure-wdh.json` line 30120) and lawful evil on her Notable Figures page, which the page follows" (`campaign/setting/organizations/09-manshoons-zhentarim.md:173`). The orchestrator decides.

**D2. The Stone: adventure has Vevette hold it on the rooftops; campaign has no such event**
- Adventure: "Before the characters can lay hands on the stone, a Zhent named Vevette Blackwater grabs it and flees, initiating a chase across icy rooftops (encounter 5, \"Rooftop Chase\")." — `sources/adventure-wdh.json:6747`
- Adventure: "A Zhent named Vevette Blackwater (CE female Tethyrian human {@creature swashbuckler|VGM}; see {@adventure appendix B|WDH|12}) has snatched the {@item Stone of Golorr|WDH} and is fleeing as fast as she can across icy rooftops during a blizzard." — `sources/adventure-wdh.json:8531`
- Campaign: "- **After the vote:** Neverember's spies take the Stone from the Palace and are killed leaving the city. It passes from hand to hand until it reaches Xanathar." (`campaign/setting/lore/stone-of-golorr-and-the-eyes.md:50`)
- Campaign: "- **Ches 20:** Dalakhar steals it from Xanathar's lair on Neverember's orders." (`campaign/setting/lore/stone-of-golorr-and-the-eyes.md:51`)
- Campaign: "- **Ches 22:** The fireball kills Dalakhar. The Gralhund nimblewright takes the Stone from his body and carries it to **Gralhund Villa**, where Yalah Gralhund keeps it in an inner pocket of her breastplate." (`campaign/setting/lore/stone-of-golorr-and-the-eyes.md:52`)
- The campaign has no Vevette theft. No campaign file (structure, quest or guide) records one (search in F and E). The Notable Figures Resonance (L11) and Motivations (L15) keep the adventure's theft.
- Higher-ranked source: the campaign Stone path (`lore/stone-of-golorr-and-the-eyes.md`, a lore file). The orchestrator decides what the Resonance keeps.

**D3. Theater and the Stone's hand-off (Trades Ward against Dock Ward)**
- Adventure: "As this encounter opens, the characters follow a fleeing Zhent swashbuckler into a theater in the Trades Ward called the Brizzenbright. Named after Malkolm Brizzenbright, its dead owner, the establishment has struggled in recent years." — `sources/adventure-wdh.json:9115`
- Wiki: "...the Trades Ward theater called the [[Brizzenbright]]" (scratchpad line 68).
- Campaign: the ghost Malkolm Brizzenbright haunts the Seven Masks Theater in the Dock Ward. The campaign's own note: "The campaign's Malkolm Brizzenbright haunts the Seven Masks Theater in the Dock Ward (`campaign/setting/notable-figures/bregan-daerthe/07-malkolm-brizzenbright.md:7`; `campaign/guides/factions/08-bregan-daerthe.md:101`), so the page does not list a Trades Ward theater." (`campaign/gazetteer/waterdeep/trades-ward.md:248`)
- Higher-ranked source: the campaign (Dock Ward Seven Masks). The theater scene is quest-time in any case (E2).

**D4. Seffia's visiting card: is it on the revelation list?**
- Campaign, Cassalanter guide: "- *Seffia Naelryke's Visiting Card* (Response Team: Vevette Blackwater — gives the Windmill's address)" — `campaign/guides/factions/11-cassalanters.md:88`
- Campaign, org page Draft Notes: "**Gap in the Factions Guide:** Vevette's visiting card from Seffia Naelryke is on her Notable Figures page (`03-vevette-blackwater.md` line 21) and is not in the Factions Guide revelation list." — `campaign/setting/organizations/09-manshoons-zhentarim.md:166`
- Alexandrian: "Seffia Naelryke's Visiting Card (Response Team: Vevette Blackwater)" (`sources/17. Outpost and Lair Revelation Lists.pdf`, printed p.123) **[image transcription]**
- Higher-ranked source: the Cassalanter guide line 88 is a campaign file and shows the card is listed. The org page Draft Notes line 166 is stale.

**D5. "Most trusted" (two named people)**
- Campaign, Sidra: "Manshoon's most trusted lieutenant, stationed at Kolat Towers" (`campaign/setting/organizations/09-manshoons-zhentarim.md:97`).
- Campaign, Vevette: "Manshoon's most trusted field lieutenant" (`03-vevette-blackwater.md:25`).
- Adventure: "Vevette and Agorn are two of {@creature Manshoon|WDH}'s most trusted followers." (`sources/adventure-wdh.json:30130`)
- Not a flat conflict. The "field" qualifier is the only thing that separates Vevette from Sidra in the campaign. The drafter should keep both.

**D6. Stat block citation**
- Adventure tags every mention "{@creature swashbuckler|VGM}" (`sources/adventure-wdh.json:7203` and others). Appendix B's only "Swashbuckler" entry is the generic monster at page 216 (`:32595`–`:32599`), with no Vevette entry.
- Alexandrian cites "DH p. 216" for her (`sources/6. Faction Response Teams.pdf` p.55; `sources/12. Lair  Zhentarim – Kolat Towers.pdf` p.95). The same Alexandrian cites DH p.216 for Khafeyta (`sources/9. Lair – Sea Maidens Faire.pdf` p.76). The Alexandrian's design note says: "Vevette Blackwater and Agorn Fuoco are supposed to appear in Appendix B of Dragon Heist. As far as I can tell, however, they're missing in action, so I've provided more detailed backgrounds for them here." (`sources/6. Faction Response Teams.pdf` p.55) **[image transcription]**. So "DH p. 216" is a stat reference to the generic entry, not a Vevette entry.

**D7. Team size**
- Campaign, Factions Guide: "**Vevette Blackwater** — swashbuckler + 3–4 **thugs**." (`campaign/guides/factions/10-manshoons-zhentarim.md:11`)
- Campaign, Trollskull guide: "— alone or with two thugs in decent clothes." (`campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:40`)
- Alexandrian: "3-4 thugs" (`sources/6. Faction Response Teams.pdf` p.55) **[image transcription]**
- Minor. The Trollskull guide is a different (tavern) situation.

**D8. Wiki "reformed Zhentarim" against campaign "reforming"**
- Fandom dump, Swashbuckler page: "one of the high-ranking officers within the reformed [[Zhentarim]]" (line 4989891).
- Campaign: "The Zhentarim are reforming a council in 1492 DR, and efforts to reclaim and rebuild Zhentil Keep are underway." (`campaign/setting/organizations/09-manshoons-zhentarim.md:27`)
- The wiki is lowest rank. Campaign wins. Listed for completeness.

**D9. Two Zhentarims (no conflict; the rule holds)**
- Campaign: "Anyone who deals with the Zhentarim through Davil is dealing with the Doom Raiders and not with Manshoon. The villains on this page answer only to Manshoon." (`campaign/setting/organizations/09-manshoons-zhentarim.md:19`)
- No source places Vevette in the Doom Raiders. The Doom Raiders quests name her as the Splinter's officer (see E2). The Alexandrian Appendix B renown line lists her as "a named Manshoon operative" (`sources/Appendix_B_-_Player_Factions.md:658`).

---

## E. Stale lines in other files (not to be edited) and routed quest references

### E1. Stale or conflicting lines in other files

- `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:40`: "CE swashbuckler" (D1).
- `campaign/setting/organizations/09-manshoons-zhentarim.md:166`: "is not in the Factions Guide revelation list" (D4); `campaign/guides/factions/11-cassalanters.md:88` lists it.
- `campaign/setting/organizations/09-manshoons-zhentarim.md:173`: the Draft Notes alignment conflict (D1).
- `campaign/structure/arc-i-kolat-towers.md:320`: "**Notable Figures** — Existing profiles: Manshoon, Sidra Romeir, Manafret Cherryport, Vevette Blackwater, Agorn Fuoco, Urstul Floxin, Lady Gondafrey, Skeemo Weirdbottle. New profiles needed: Kaevja Cynavern, Havia Quickknife, Mookie Plush, Yorn the Terror." Vevette's profile exists (this file), so the line is a structure note that is out of date for her. Not a fact conflict.
- `campaign/gazetteer/waterdeep/trades-ward.md:248`: the Brizzenbright theater note (D3). Correct as it stands.

### E2. Routed to quests (quest-time facts and where each already lives)

**Stone theft, chase and theater (adventure only; no campaign structure or quest file has it)**
- Chase and theft: `sources/adventure-wdh.json:6747` ("...a Zhent named Vevette Blackwater grabs it and flees, initiating a chase across icy rooftops..."), `:7203`, `:7734`, `:7741`, `:8531`, `:8532`, `:8539`.
- Theater and hand-off to Agorn: `sources/adventure-wdh.json:9115`, `:9132`, `:9133`, `:9143`, `:9152`; wiki line 68.
- Mistshore and the Old Tower hand-off: `sources/adventure-wdh.json:6748` (Agorn leaves the stone with "a priest of Bane" in the Castle Ward; not Vevette, listed for the chain).

**Faction Outposts (campaign structure)**
- `campaign/structure/arc-e-faction-outposts.md:213` (quoted in full): "**Escalation: Manshoon moves to Alert (Tier 3).** Avareen's flying snakes carry the alarm faster than the party can move; if even one escapes, Manshoon knows within hours. Vevette Blackwater's team deploys within 1d4 days. If Xanathar cross-faction spillover applies, Manshoon moves directly to Lockdown (Tier 4). **Founders' Day Clock: 1–2 days.**"
- `campaign/structure/arc-e-faction-outposts.md:275`: "*Step 1 — Gather Information.* Five paths to the Converted Windmill: Seffia Naelryke's visiting card found on Vevette Blackwater from a Zhentarim response team (Seffia approached Vevette to open a communication channel; Vevette rebuffed her, suspecting a trap, but kept the card); ..." (the rest of the paragraph covers the other four paths).
- `campaign/guides/factions/10-manshoons-zhentarim.md:31` and `:53` (escalation): "Vevette Blackwater's team deploys within 3 days." and "| Alert | Agorn or Vevette's team; orders are to capture, not kill |"
- `campaign/guides/gm-guide/running-the-villains.md:50` and `:74`.

**Sea Maidens Faire (campaign structure)**
- `campaign/structure/arc-h-sea-maidens-faire.md:204`: "**The Strike Team.** Urstul Floxin (if alive from **Gralhund Villa**; if dead, replaced by Vevette Blackwater) + 1 lieutenant + 4 thugs."

**Kolat Towers (campaign structure)**
- `campaign/structure/arc-i-kolat-towers.md:150`: "**E3 — Guard Station.** ... If she is not eliminated silently before she acts, her first action is to cast sending to Manshoon — regardless of his location — and to Agorn Fuoco or Vevette Blackwater in E8." (the quote is the sentence with "Vevette Blackwater in E8"; the rest of the paragraph is Kaevja's)
- `campaign/structure/arc-i-kolat-towers.md:156`: "**E8 — Reading Room.** Vevette Blackwater + Agorn Fuoco (if survived **Faction Outposts**). Vevette fights; Agorn does not if the fight is going badly — he offers his ring (he carries one), Manshoon's daily routine, and the ledger's location in exchange for being allowed to leave." (rest covers the brazier and its trigger)
- `campaign/structure/arc-i-kolat-towers.md:178`: "| 20 min | Vevette's response team arrives at K22 if Vevette is not already present in E8. Full garrison at combat readiness. |"
- `campaign/structure/arc-i-kolat-towers.md:198`: "...and prioritizing objectives that overlap with the party's (Manshoon's operational records, pass-amulet system destruction, Vevette Blackwater captured alive)."
- `campaign/structure/arc-i-kolat-towers.md:259`: "- **Manshoon Destroyed.** Both Manshoon (the clone of a clone) and the simulacrum were eliminated during the raid. The Splinter cell collapses within a tenday — Vevette (if alive) attempts to hold the surviving operatives together but lacks Manshoon's authority and his clone-network insurance. ..."
- `campaign/structure/arc-i-kolat-towers.md:275`: "**Tashlyn Yafeera or Davil Starsong (Doom Raiders).** \"Is it done?\" ... If Vevette Blackwater was captured: \"Good. She has things to answer for. So does the rest of what's left of that network.\" ..."

**Doom Raiders faction missions**
- `campaign/quests/faction-events/doom-raiders/m04-silencing-skeemo/ev-03-the-reckoning.md:150`: "> \"Vevette Blackwater. Good. Now I have a name to go with the hand. I'll take these, and you can keep whatever else you found.\""
- `campaign/quests/faction-events/doom-raiders/m04-silencing-skeemo/overview.md:58`: "- **Vevette Blackwater** (Manshoon's Zhentarim): the hand that receives Skeemo's letters, named only when Tashlyn decodes them."
- `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:10`, `:25`, `:82`, `:188`, `:265`, `:279`, `:417`. Key lines: `:10` "Take three coded letters from Amath Sercent's desk, which name Vevette Blackwater as the coordinator of the Splinter's strike teams."; `:279` "They name Vevette Blackwater as the officer who coordinates the strike teams from Kolat Towers and list the operations she has planned for the coming month."
- `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-02-the-debrief.md:83` and `:216`.
- `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/overview.md:80`: "- **Vevette Blackwater** (Manshoon's Zhentarim): stays at Kolat Towers, and the letters name her as the strike-team coordinator."
- `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md:20`: "> - **Manshoon Destroyed.** The Splinter cell collapsed within a tenday of the raid. If Vevette Blackwater is alive and free, she is holding the survivors together and approved the hunt to keep them loyal. If she was captured or killed, nobody sent Ondra, and she acts for revenge with the agents who still follow her. Either way the Splinter has no plan for the vault."
- `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md:329`: "What Davil says first depends on the Manshoon Event Outcome from **Kolat Towers**. ... If Vevette Blackwater was captured, he adds that Tashlyn will want to question her about this hunt."
- `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/overview.md:21`: "...Who sent her depends on the Manshoon Event Outcome the party marked in **Kolat Towers**: **Manshoon Destroyed** (Vevette Blackwater, if free, or no one), **Manshoon Simulacrum Only** or **Manshoon Alive**..."
- `campaign/quests/faction-events/doom-raiders/r03-wolf/ev-01-wolf.md:126`: "...Once either outcome is marked, the swashbuckler is Vevette Blackwater, the bard is Agorn Fuoco and the assassin is Urstul Floxin, and the answer names them."
- `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/design-notes.md:19`: the Event Outcome list that reads whether "Vevette Blackwater was captured, killed or escaped".

**Other faction missions and tavern**
- `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/ev-02-the-breach.md:20`: "...If Vevette Blackwater is alive and free, she approved it."
- `campaign/quests/faction-events/lords-alliance/r25-warduke/ev-01-warduke.md:196`: table row "| The Splinter | First | A lieutenant who fights with a blade and three or four hired hands, with orders to take prisoners | Vevette Blackwater's crew |"
- Trollskull tavern visit: `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:36`–`:55`, and `sources/Appendix_D_-_Running_the_Tavern.md:1545`–`:1572` (the visit text, "Engaging with the offer without following through is noticed by both factions within two tendays and costs standing with both."). Quest-time (tavern play).
- Renown: `sources/Appendix_B_-_Player_Factions.md:658`: "**Neutralize a named Manshoon operative (+2).** Eliminate or capture one of Manshoon's lieutenants — Urstul Floxin, Vevette Blackwater, Agorn Fuoco, or any other named agent. Delivering a prisoner to Tashlyn earns the full renown; confirmed elimination earns +1."

---

## F. Gaps (what a Background would need that no source gives)

1. **Birthplace, home city and family name.** The Alexandrian gives "her mother" only (A1, `6. Faction Response Teams.pdf` p.55). The wiki gives "Waterdeep, Sword Coast North" as home (scratchpad line 11, `home`), which is the Waterdeep tag, not a birthplace. No mother's name, no siblings, no city of birth. The campaign has no family line.
2. **Age and birth year.** No source. Wiki infobox `dob` and `age` are blank.
3. **The recruiting agent.** The Alexandrian says "A Zhentarim agent" gave her the blade at twelve. No name, no place, no date.
4. **The pirate years.** "a vicious pirate" (`sources/adventure-wdh.json:8532`) only. No ship, crew, port, rival, or date. The generic swashbuckler entry says "pirates and corsairs" (`:32599`), which is not about her.
5. **How she rose and when.** "rose to become one of ... favored lieutenants" (`:8532`). No date, no rung, no named sponsor. Her relationship with Agorn beyond the shared sanctum room and the Stone hand-off has no source.
6. **Faith.** No deity for her in any source. Bane (the Banite cell) is Amath Sercent's, not Vevette's; the campaign ties Vevette to no church.
7. **Why she fears the law.** The campaign says she counts on it (`03-vevette-blackwater.md:21`) and the adventure says so too (`:7741`). Why she trusts it, and whether it ever failed her, has no source.
8. **Her "advocate".** The voice profile has "my advocate" (`voices/manshoons-zhentarim.md:61`). No source names a lawyer or any legal ally.
9. **How she met Manshoon.** Only the Alexandrian's "A Zhentarim agent came to her" (A1). No source says she met him.
10. **Her views on the Doom Raiders and on Davil Starsong.** The campaign and the Doom Raiders quests say the Splinter hates them (`campaign/setting/organizations/09-manshoons-zhentarim.md:86`). No source gives her personal view.
11. **The cards and rings in her hands day to day.** Pass-amulet and teleporter ring are given (A5). No source says she uses either to leave the Towers on Ches 1.
12. **Personal goals beyond the job.** The page has "Motivations" (advancement, keeping the Stone, avoiding prison). No source gives a personal want beyond these.

---

## G. Inner life (exact quotes for backstory and personal goals; the drafter must not contradict them)

- Childhood and recruitment (Alexandrian, printed p.55 **[image transcription]**): "When she was a young girl, Vevette was abused by her mother. A Zhentarim agent came to her when she was twelve, put a blade in her hand, and asked if she wanted to take control of her life. She did. And she's been in the Black Network ever since."
- Temperament, Alexandrian (printed p.55 **[image transcription]**): "Vevette's past manifests itself in a deep streak of cruelty and ruthlessness, but to most outward appearance she is a charming bon vivant."
- Habits, adventure (`sources/adventure-wdh.json:8532`): "She cackles madly in the face of danger and loves a good chase. She knows the streets, alleys, and rooftops of Waterdeep well."
- Self-image, campaign (`03-vevette-blackwater.md:21`, Persona): "Deep down, she is counting on the law to protect her from serious harm if captured, and she knows she has done nothing to warrant arrest."
- The same trait in the adventure (`sources/adventure-wdh.json:7741`): "She's counting on the law to protect her from serious harm, and she knows she has done nothing to warrant arrest." (quest chapter text; trait only)
- Pride, campaign (`03-vevette-blackwater.md:13`, Emotions): "operative's pride in her fieldwork, and measured disdain for anyone she considers beneath her."
- Voice, pride (`.claude/skills/character-voices/voices/manshoons-zhentarim.md:56`): "Her pride in her fieldwork comes out as boasting."
- Voice, never (`voices/manshoons-zhentarim.md:59`): "She never admits a crime, never works for less than she thinks she's worth, and never runs without flair."
- Caution with a stranger's offer, campaign (`03-vevette-blackwater.md:21`): "having rebuffed a Cassalanter backchannel offer she suspected was a trap."
- Her loyalty to Manshoon, adventure (`sources/adventure-wdh.json:30130`): "Vevette and Agorn are two of {@creature Manshoon|WDH}'s most trusted followers."
- Her belongings, adventure (`:30221`): "Vevette's chest has three {@item potion of healing||potions of healing}."
- Her relationship with the Splinter's enemies, adventure (`:30130`): "Vevette commands the wizard's forces against the Xanathar Guild".
- Loss or grief: none in any source.
- Fear: none in any source (Morale gives how she behaves when caught, not what she fears; `03-vevette-blackwater.md:23`).
- Love or attachment: none in any source. The love letters in the sanctum chests belong to Agorn (`sources/adventure-wdh.json:30222`), not to Vevette.

---

## Answers to the brief's specific asks

- Alignment: lawful evil on the campaign page and the pass 5 ruling; chaotic evil in every other source (D1).
- Day-one against quest-time lines: section C (rows 5, 7, 13–16 and the voice lines) and E2.
- Faction label: "Manshoon's Zhentarim" on the page (L6), the organization page (`09-manshoons-zhentarim.md:1`, "Contacts" at `:8`, "Key Members" at `:98`), the Factions Guide (`10-manshoons-zhentarim.md:11`), and the Doom Raiders and Cassalanter pages' references. No source puts her in the Doom Raiders (D9).

---

## Cross-references (every other file:line where the topic appears, with the line)

- `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:26`: "**Relationships.** Manshoon is the leader of the Zhentarim splinter cell, the employer of Urstul Floxin, Sidra Romeir, and Vevette Blackwater, a blackmailer of Masked Lords Jelenn Urmbrusk and Corylus Thann, and a clone-wizard whose response teams are deliberately the weakest in muscle because drawing attention is the one mistake he will not make twice."
- `campaign/setting/villains/manshoon.md:73`: "- Seffia Naelryke of the Cassalanters approached Vevette Blackwater to open a communication channel. Vevette refused, suspecting a trap, and neither side has made contact since."
- `campaign/setting/villains/manshoon.md:116`: "...**Vevette Blackwater**, **Agorn Fuoco**, ... (Notable Figures): profiles for the Relationships table and the notes"
- `campaign/setting/organizations/08-xanathars-guild.md:92`: "...and Vevette Blackwater commands the cell's forces against it (**Manshoon**; *Dragon Heist*, 5e)."
- `campaign/setting/organizations/10-cassalanters.md:86`: "- **Manshoon's Zhentarim (neutral, rebuffed):** Seffia Naelryke approached Vevette Blackwater to open a communication channel, and Vevette refused, suspecting a trap. Neither side has made contact since, ..."
- `campaign/setting/organizations/10-cassalanters.md:121`: "  - Vevette Blackwater of the Zhentarim rebuffed Seffia's approach to open a communication channel, suspecting a trap."
- `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:36` and `:89` (quoted in A7 and above).
- `campaign/guides/gm-guide/running-the-villains.md:50`: "| **Manshoon's Zhentarim** | Normal operations | Flying snake courier network active; Agorn Fuoco and Avareen Windrivver file field reports. Urstul Floxin reviews them | Agorn Fuoco or Vevette Blackwater's team; orders are to capture, not kill | ..."
- `campaign/guides/gm-guide/running-the-villains.md:74`: "| **Manshoon vs. Cassalanters** | Mutual distrust — no contact | Seffia Naelryke approached Vevette Blackwater to open a communication channel. Vevette refused, suspecting a trap. No further contact from either side. | *Seffia Naelryke's Visiting Card* (Vevette Blackwater) |"
- `campaign/guides/factions/11-cassalanters.md:88`: "- *Seffia Naelryke's Visiting Card* (Response Team: Vevette Blackwater — gives the Windmill's address)"
- `campaign/structure/arc-e-faction-outposts.md:213`, `:275` (E2).
- `campaign/structure/arc-h-sea-maidens-faire.md:204` (E2).
- `campaign/structure/arc-i-kolat-towers.md:150`, `:156`, `:178`, `:198`, `:259`, `:275`, `:320` (E2).
- `campaign/quests/faction-events/doom-raiders/...` (E2; full list of lines given there).
- `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/ev-02-the-breach.md:20` (E2).
- `campaign/quests/faction-events/lords-alliance/r25-warduke/ev-01-warduke.md:196` (E2).
- `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:36`–`:55` (E2).
- `campaign/gazetteer/waterdeep/trades-ward.md:248` (D3).
- `campaign/gazetteer/waterdeep/dock-ward.md:76` (the Brizzenbright ghost; the line names Malkolm Brizzenbright as "the theater's founder"; the Seven Masks Theater is named in `trades-ward.md:248`).
- `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:49`–`:53` (D2).
- `campaign/setting/organizations/09-manshoons-zhentarim.md:19`, `:27`, `:55`, `:58`, `:97`, `:98`, `:166`, `:173`.
- `campaign/setting/notable-figures/manshoons-zhentarim/` (all pages): only `01-manshoon.md:26` names her.
- `sources/SOURCE_GUIDE.md:35`: "- **Chapter 8 — Face of the Enemy (Manshoon/Zhentarim):** ... Contains: Manshoon, his simulacrum, Sidra Romeir, Manafret Cherryport, Vevette Blackwater, Agorn Fuoco, Urstul Floxin."
- `sources/adventure-wdh.json` (every line cited above): `:357`–`:358`, `:6747`, `:6748`, `:7203`, `:7734`, `:7741`, `:7742`, `:7743`, `:8531`, `:8532`, `:8539`, `:9115`, `:9132`, `:9133`, `:9143`, `:9152`, `:13479` ("There's a {@chance 50|50 percent chance} that these Zhents are led by one of {@creature Manshoon|WDH}'s lieutenants, either Vevette Blackwater or Agorn Fuoco, if they're still alive (see chapter 8, {@area E8|425})."), `:14783`, `:26763` ("These lieutenants include Sidra Romeir ({@area K2|3db}), {@creature Manafret Cherryport|wdh} ({@area K3|3de}), {@creature Urstul Floxin|wdh} ({@area E5|41d}), Vevette Blackwater and Agorn Fuoco ({@area E8|425}), and ..."), `:29953`, `:29959` ("Vevette Blackwater and Agorn Fuoco (see {@area E8|425})"), `:30120`, `:30130`, `:30212`, `:30221`, `:32595`–`:32599`.
- `sources/Appendix_B_-_Player_Factions.md:658` (E2).
- `sources/Appendix_D_-_Running_the_Tavern.md:1545`–`:1572` (E2, B).
- `sources/6. Faction Response Teams.pdf` p.55; `sources/12. Lair  Zhentarim – Kolat Towers.pdf` pp.94–95; `sources/17. Outpost and Lair Revelation Lists.pdf` p.123 (A5, D).
- `sources/research/pass4-bundles/cassalanters/campaign-hits.txt:843` (the old org page's lawful-evil line, D1).
- `docs/plans/setting-compendium-research-notes/pass5/zhentarim.md:262`–`:269` (the earlier C7 alignment note, which quotes the same CE lines).

---

## Not found

Terms searched: "Vevette", "Blackwater" (the name and its surname only; the search did not use the alias "Vevette Blackwater" separately).

Files searched and what they gave:
- Campaign (whole tree, Grep): listed in Cross-references. No Vevette line in `campaign/quests/act-i/`, `campaign/quests/act-ii/` or `campaign/locations/` (`No matches found`).
- `sources/adventure-wdh.json` (Grep, all lines): the lines listed in Cross-references. No Vevette entry in Appendix B: Monsters and NPCs (`:31685`–`:32806`).
- `sources/Appendix_B_-_Player_Factions.md`, `Appendix_D_-_Running_the_Tavern.md`: found (E2, B). `Appendix_C_-_Player_Faction_Missions.md`: no match. `Act_III_Arc_D.md`, `Act_III_Arc_E.md`, `SOURCE_GUIDE.md`: `SOURCE_GUIDE.md:35` only.
- `sources/research/` (Grep): bundle copies only (pass2, pass3, pass4, pass5). No new source lines beyond those cited.
- Scratchpad wiki folder (`wiki-manshoons-zhentarim/`): the Vevette page only, plus no hit in `05-agorn-fuoco.txt` beyond an omitted line (not checked).
- Fandom dump (`forgottenrealms_pages_current.xml`): the Vevette page (same as the extracted file) and the "Swashbuckler" page's Individuals list (line 4989891). No other Vevette page.
- Alexandrian PDFs read as images, pages checked: `1. The Villains.pdf` (all 7 pages; no Vevette; Zhentarim section at printed p.16), `5. Faction Outposts.pdf` (all 13 pages, printed pp.36–48; no Vevette; Zhentarim interrogation house at p.45 and Yellowspire at p.46 name Avareen, Zorbog and Amath only), `6. Faction Response Teams.pdf` (all 8 pages, printed pp.49–56; Vevette at p.55), `12. Lair  Zhentarim – Kolat Towers.pdf` (all 5 pages, printed pp.92–96; Vevette at pp.94–95), `17. Outpost and Lair Revelation Lists.pdf` (all 4 pages, printed pp.121–124; Vevette at p.123), `21. Faction Reports of the Grand Game.pdf` (all 13 pages, printed pp.142–154; no Vevette), `27. Addendum A Night in Trollskull Manor.pdf` (pages 1–10, printed pp.178–187; no Vevette; the patron "Response Team (or reroll)" entry is not in the extract), `9. Lair – Sea Maidens Faire.pdf` (all 9 pages, printed pp.68–76; no Vevette; Khafeyta at p.76 is a swashbuckler, DH p.216).
- Alexandrian PDFs NOT read for Vevette: `2. Other Factions.pdf`, `3. Player Character Factions.pdf`, `4. Gralhund Villa.pdf`, `7. Other Response Teams.pdf`, `8. The Eyes of the Stone.pdf`, `10. Lair Cassalanter Villa.pdf`, `11. Lair Xanathar's Lair.pdf`, `13. Clues and Timelines.pdf`, `14`–`16`, `18`–`20`, `22`–`26`, `28`–`30`. Not checked for this report.
- Missing from the sources: a birthplace, a mother's name, an age, a faith, the recruiting agent's name, a pirate crew or ship, a date for her rise, a personal relationship with Agorn, and a personal want beyond the job (F).

## Not readable

- `sources/*.pdf` cited above: read as rendered page images, not text. Every PDF quote is marked **[image transcription]**. Check against `pdftotext -layout` before prose use.
- `sources/Other remix files/*.docx`: not opened (cannot be read with these tools). `SOURCE_GUIDE.md:688` lists `Davil and the Doom Raider Zhents + Elf Killer mission and more.docx` (Doom Raider dynamics, which may mention Manshoon's cell). `SOURCE_GUIDE.md:695` lists `The Waterdavian's Guide to Waterdeep NPCs (...).docx` as a "Broad NPC reference", which may contain a Vevette entry. Both need extracting by the caller.
- The scratchpad wiki file `03-vevette-blackwater.txt` and the fandom dump were read as text.

## Not run

- `voicecheck.py` was not run (research only).
- The page was not written. No file was edited except this notes file.
