# Pass 6 research notes: Avareen Windrivver

Page: `campaign/setting/notable-figures/manshoons-zhentarim/06-avareen-windrivver.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Rulings used:
- Ches 1, 1492 DR: Ott Steeltoes is free and tends Sylgar. The Zhentarim kidnap him during the campaign, a quest event routed to **Faction Outposts**. "At the beginning of the campaign ott is free. Then he gets kidnapped." (`docs/plans/setting-compendium-pass6-brief.md:69`)
- The Interrogation House (house, rack, snakes, pass-amulet) is day-one. The captive is not (orchestrator instruction, Session 53).
- Two Zhentarims: Manshoon's cell and the Doom Raiders are separate (`campaign/setting/villains/manshoon.md:19`, quoted in section D).

Method and caveats:
- Campaign files: Read and Grep, quoted from the file. Bullet prefixes (`> - `) are dropped from quotes where the bullet is the sentence.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. Tags such as `{@creature ...}` are left as written. JSON escapes are shown as plain quotes.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. `sources/5. Faction Outposts.pdf` printed p.45 (PDF p.10) and `sources/17. Outpost and Lair Revelation Lists.pdf` printed pp.122-123 (PDF pp.2-3) were read as rendered page images. Those quotes are transcriptions. They must be checked with `pdftotext -layout` before any quote goes into prose.
- Wiki: no entry. The extracts `scratchpad/wiki-manshoons-zhentarim/06-avareen-windrivver.txt` and `07-zorbog-jyarkoth.txt` each read `NOT FOUND`. Grep over every `sources/research/*/wiki.txt` for the name, the surname, "Brindul Alley" and "Interrogation House" returned no file. See the Not found section.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

---

## A. Background facts by theme

### A1. Origin, birth, family, early life

No source gives any of this. The only origin facts are species and nationality.

> "*Illuskan human spy (Zhentarim interrogator), lawful evil, she/her*. Stat block: **Spy**."
> — `campaign/setting/notable-figures/manshoons-zhentarim/06-avareen-windrivver.md:5`

> "This windowless house is occupied by two Zhents loyal to {@creature Manshoon|WDH}-the same individuals that Sora describes. Their names are Avareen Windrivver (LE female Illuskan human {@creature spy}) and Zorbog Jyarkoth (NE male Turami human {@creature thug})."
> — `sources/adventure-wdh.json:7202` (Chapter "Alley: Winter", page 64, entry "Zhentarim Safe House", `:7198`)

> "Avareen Windrivver** ... " — see the Alexandrian entry below; the adventure line is the only other origin fact.

> "ZHENTARIM INTERROGATION HOUSE (Trade Ward, Brindul Alley): Avareen Windrivver (LE female Illuskan human spy) and Zorbog Jyarkoth (NE male Turami human thug) maintain this combination safe house / covert interrogation center."
> — `sources/5. Faction Outposts.pdf`, printed p.45 [PDF p.10] (image transcription; check with `pdftotext -layout`)

Age, from an in-world observer (not a fact about her record). Sora Cuttle is the neighbour in L2:

> "Sora is suspicious of her two neighbors in {@area L1|140}. They come and go at strange hours, sometimes returning from a night's sojourn with blood on their leather armor. If the characters do Sora the courtesy of warning her about the meat, she happily shares her concerns about her naughty neighbors, along with descriptions of them. One is a pale, gaunt woman in her twenties with dark, stringy hair. The other is a much older, dark-skinned man with a bald head, a half-missing ear, and a short white beard."
> — `sources/adventure-wdh.json:7193`

### A2. Joining the Zhentarim and the Splinter

No source gives Avareen's own recruitment. The general policy:

> "The Black Network has an open recruitment policy. Anyone can join. Tenacity and loyalty are highly valued (but not essential) traits in new members."
> — `sources/adventure-wdh.json:1443`

> "- **Recruiting:** The Black Network has an open recruitment policy that prizes tenacity and loyalty without requiring either, but the published adventure says adventurers cannot join Manshoon's cause (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:71`

### A3. The post and how long she has held it

The campaign dates the Splinter's field offices to the clone's build period. The date is derived.

> "- About Nightal 1491 DR" — not used. The usable line is:

> "The clone then spent two years building the Splinter cell, which is about 1490 DR counted back from Ches 1, 1492 DR. `[research]` The structure is hub-and-spoke: Kolat Towers as the command center, with the Interrogation House in the North Ward and Yellowspire in the Castle Ward as field offices."
> — `campaign/setting/history/08-the-players-arrive.md:32`

> "The Splinter is hub and spoke. Kolat Towers is the command center, and the Interrogation House in the North Ward and Yellowspire in the Castle Ward are field offices linked to it by teleportation circles."
> — `campaign/setting/history/04-the-founding-of-chains.md:69`

> "Manshoon's clone fled Undermountain, found the towers abandoned with the force field intact, and took the amulet-making instructions from Duhlark's study. He spent two years building the Splinter."
> — `campaign/setting/history/04-the-founding-of-chains.md:68`

> "The Interrogation House: A windowless house on Brindul Alley in the North Ward, kept by Avareen Windrivver and Zorbog Jyarkoth. A rack and an arcane circle fill the back room, and three black flying snakes nest near the ceiling (**North Ward**; *Dragon Heist*, 5e)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:57`

Her tenure length is not sourced (see F3).

### A4. Rank, reporting line and whom she answers to

> "- **Avareen Windrivver** — Illuskan human spy (Zhentarim interrogator), lawful evil, who maintains the Interrogation House alongside Zorbog; see the **Avareen Windrivver** page in Notable Figures."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:101`

Reporting to Urstul Floxin (field reports), from the Factions Guide escalation table and the GM Guide:

> "| Suspicious | Flying snake courier network; Agorn and Avareen's field reports. Avareen identifies the threat; Urstul reviews field reports |"
> — `campaign/guides/factions/10-manshoons-zhentarim.md:52`

> "| **Manshoon's Zhentarim** | Normal operations | Flying snake courier network active; Agorn Fuoco and Avareen Windrivver file field reports. Urstul Floxin reviews them | Agorn Fuoco or Vevette Blackwater's team; orders are to capture, not kill | Urstul Floxin's team if the others fail; Manshoon issues personal directives by flying snake. Manshoon's simulacrum engages; Sidra Romeir locks down Kolat Towers |"
> — `campaign/guides/gm-guide/running-the-villains.md:50`

Revelation list, Factions Guide (the Urstul directive names her):

> "- *Directive to Urstul Floxin* (Response Team: Urstul Floxin — names Avareen in Brindul Alley)"
> — `campaign/guides/factions/10-manshoons-zhentarim.md:63`

Manshoon's orders to the cell (applies to the house):

> "**Capture and interrogation:** The cell takes prisoners and questions them at the Interrogation House, and Yorn the Terror is the asset it uses when a conversation has stopped working (**Yorn the Terror**). Manshoon prefers a prisoner to a corpse because a prisoner answers questions (**Manshoon**)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:68`

> "Any Zhentarim team sent to attack the characters carries orders to take them as prisoners to the Interrogation House on Brindul Alley. Questioned team members can point the characters toward the house. The lighter roster is intentional. Manshoon wants intelligence, not body counts, and underestimated enemies are more useful to him than dead ones. These teams also keep pressure on the party without forcing a lethal confrontation."
> — `campaign/guides/factions/10-manshoons-zhentarim.md:9`

### A5. The pass-amulet (her signature belonging)

Day-one. Four campaign sources and one Alexandrian source agree that she carries one.

> "All three Zhentarim response teams consist of a lieutenant plus 3–4 **thugs**. Every lieutenant carries a pass-amulet to Kolat Towers and will try to destroy it if capture seems certain, except Agorn, who trades his to save himself."
> — `campaign/guides/factions/10-manshoons-zhentarim.md:7`

> "Front Room. Avareen and Zorbog's quarters. Avareen carries a pass-amulet to Kolat Towers."
> — `campaign/guides/factions/10-manshoons-zhentarim.md:23` (the same paragraph also covers the *Directive to Zorbog*; see C)

> "Avareen carries a pass-amulet for Kolat Tower (see Part 4)."
> — `sources/5. Faction Outposts.pdf`, printed p.45 [PDF p.10] (image transcription)

> "Front Room: Avareen Windrivver (spy) and Zorbog Jyarkoth (thug) with three black flying snakes. Avareen carries a pass-amulet to Kolat Towers; her first instinct if captured is to destroy it. Backroom: a torture rack, an arcane circle, and Ott Steeltoes strapped to a chair."
> — `campaign/structure/arc-e-faction-outposts.md:205` (structure doc; the Ott clause is quest-time, see C)

> "Splinter agents carry pass-amulets that bypass it. Teleportation circles link the towers to Yellowspire in the Castle Ward and to the Interrogation House in the North Ward."
> — `campaign/gazetteer/waterdeep/southern-ward.md:58` (sentence begins "A magical barrier with the properties of a wall of force surrounds the towers.")

The amulet system as a whole:

> "A pass-amulet system replaced a courier network, and the amulets can be revoked from the towers. An extradimensional sanctum behind the towers holds his closest lieutenants and his most sensitive work."
> — `campaign/setting/history/04-the-founding-of-chains.md:70`

> "A pass-amulet system lets him revoke anyone's access from the towers (**Kolat Towers** quest opener)."
> — `campaign/setting/villains/manshoon.md:33` (the sentence is the last one of the bullet; the bullet begins "He spent about two years building the Splinter")

The adventure does not give Avareen an amulet. Grep of `sources/adventure-wdh.json` for "amulet" returns no line naming her.

### A6. Relationships to named figures

- **Zorbog Jyarkoth** (partner): see B and H. Campaign: `campaign/setting/notable-figures/manshoons-zhentarim/06-avareen-windrivver.md:25` ("Zorbog Jyarkoth's operational partner"). Adventure: `sources/adventure-wdh.json:7202`.
- **Urstul Floxin** (reviews her reports, issues directives): `campaign/guides/factions/10-manshoons-zhentarim.md:52` and `:63`; `campaign/guides/gm-guide/running-the-villains.md:50`.
- **Manshoon** (her orders are signed by him; the cell's word is his): `campaign/guides/factions/10-manshoons-zhentarim.md:39`, quoted in G1.
- **Agorn Fuoco** (both file field reports): `campaign/guides/gm-guide/running-the-villains.md:50`. Agorn is the lieutenant who trades his amulet; Avareen's contrast is in G4.
- **Amath Sercent** (note to her at Yellowspire): `campaign/guides/factions/10-manshoons-zhentarim.md:39`, quoted in G1.
- **Ott Steeltoes** (captive in the house): quest-time, see C and E1.
- **Fenerus Stormcastle** (target of her house's directive): `campaign/guides/factions/10-manshoons-zhentarim.md:23`, quoted in C. Quest-time.
- **Vevette Blackwater** (in the house in the adventure, 5e entry): `sources/adventure-wdh.json:7203`, quoted in C. Quest-time in the adventure.
- **Sora Cuttle** (meat-shop neighbour who describes her): `sources/adventure-wdh.json:7193`, quoted in A1.
- **Avaereene** (a different name, a Xanathar's Guild wiki figure; no source links them): see D6.

### A7. Faith, shrines, clergy

None. No source gives Avareen a deity or rite. The Yellowspire faith is Bane (Amath Sercent's, not Avareen's). `campaign/setting/organizations/09-manshoons-zhentarim.md:68` is not relevant.

### A8. Habits, places she goes

> "They come and go at strange hours, sometimes returning from a night's sojourn with blood on their leather armor."
> — `sources/adventure-wdh.json:7193` (this is Sora's observation of both neighbours)

> "Avareen Windrivver, who works from a house in Brindul Alley; Agorn Fuoco, who visits Yellowspire on some evenings; and the field crews that Vevette Blackwater sends out from Kolat Towers."
> — `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:265` (a quest-time ledger; routed, see E)

---

## B. Alignment, species, pronouns, stat block

**Alignment: lawful evil** (all sources agree)
- Campaign, the page: "*Illuskan human spy (Zhentarim interrogator), lawful evil, she/her*. Stat block: **Spy**." — `campaign/setting/notable-figures/manshoons-zhentarim/06-avareen-windrivver.md:5`
- Campaign, the Faction page: "- **Avareen Windrivver** — Illuskan human spy (Zhentarim interrogator), lawful evil, who maintains the Interrogation House alongside Zorbog; see the **Avareen Windrivver** page in Notable Figures." — `campaign/setting/organizations/09-manshoons-zhentarim.md:101`
- Adventure: "(LE female Illuskan human {@creature spy})" — `sources/adventure-wdh.json:7202`
- Alexandrian, printed p.45 [PDF p.10] (image): "Avareen Windrivver (LE female Illuskan human spy)" — `sources/5. Faction Outposts.pdf`

**Species: Illuskan human** (all sources agree)
- Campaign: as above, `06-avareen-windrivver.md:5`, `09-manshoons-zhentarim.md:101`
- Adventure: "Illuskan human" — `sources/adventure-wdh.json:7202`
- Alexandrian (image): "Illuskan human spy" — `sources/5. Faction Outposts.pdf` printed p.45
- Wiki: none.

**Pronouns: she/her** (all sources agree)
- Campaign page: "she/her" — `06-avareen-windrivver.md:5`
- Adventure: "female" — `sources/adventure-wdh.json:7202`
- Alexandrian (image): "LE female Illuskan human spy" — printed p.45
- Campaign voice profile uses "she" and "her" (see C, voice lines).

**Stat block: Spy** (all sources agree)
- Campaign page: "Stat block: **Spy**." — `06-avareen-windrivver.md:5`
- Factions Guide roster: "**Roster:** Avareen Windrivver (**spy**) + Zorbog Jyarkoth (**thug**) + 3 **flying snakes**." — `campaign/guides/factions/10-manshoons-zhentarim.md:29`
- Adventure: "{@creature spy}" — `sources/adventure-wdh.json:7202`

**Name pronunciation (adventure)**
> "Avareen Windrivver",
> "ah-vah-REEN"
> — `sources/adventure-wdh.json:77`-`:78` (the Pronunciation Guide, `:25` heading)

**Appearance (adventure, from Sora; not a campaign fact)**
> "One is a pale, gaunt woman in her twenties with dark, stringy hair."
> — `sources/adventure-wdh.json:7193`

---

## C. Every sentence on the current page, and the quest-time clauses

Current page: `campaign/setting/notable-figures/manshoons-zhentarim/06-avareen-windrivver.md`. "Day-one OK" means no quest gate is needed. "Quest-time" means the sentence narrates a rescue, capture, kidnap or quest event, and must be restated or removed under brief ruling 1.

| # | Line | Sentence (exact, from the file) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Illuskan human spy (Zhentarim interrogator), lawful evil, she/her*. Stat block: **Spy**." | Day-one OK | B above |
| 2 | L6 | "**Affiliation:** Manshoon's Zhentarim" | Day-one OK | `organizations/09-manshoons-zhentarim.md:101` |
| 3 | L7 | "**Featured in:** **Faction Outposts**" | Summary bullet; the brief keeps it. Quest reference | `campaign/structure/arc-e-faction-outposts.md:199` (5A heading "Interrogation House") |
| 4 | L11 | "**Resonance.** Avareen should inspire cold unease with her professional courtesy (nothing about her manner suggests this is a person's house); dread when the party understands what the windowless building is for; and clinical discomfort with someone who finds interrogation simply a job." | Day-one, except "when the party understands what the windowless building is for" (a play prompt that names the party's discovery; borderline, the drafter decides) | The house: `campaign/gazetteer/waterdeep/north-ward.md:38` (Secret) |
| 5 | L13 | "**Emotions.** Avareen most often feels professional detachment, organizational loyalty, the controlled patience of someone who is never in a hurry, measured satisfaction in work done to specification, and a complete absence of interest in the personal dimensions of her work." | Day-one (verbatim keep) | Voice: `.claude/skills/character-voices/voices/manshoons-zhentarim.md:108` ("Satisfaction in a job done correctly") |
| 6 | L15 | "**Motivations.** Avareen wants to run the Brindul Alley operation to Manshoon's specifications, maintain the pass-amulet's security, and deliver outcomes with minimum exposure." | Day-one | Pass-amulet: `campaign/guides/factions/10-manshoons-zhentarim.md:23` |
| 7 | L17 | "**Inspirations.** When playing Avareen, channel Claire Underwood (*House of Cards*), Amy Dunne (*Gone Girl*, the controlled precision), and Hans Landa (*Inglourious Basterds*, the politeness before the menace)." | Not a fact | n/a |
| 8 | L21 (a) | "**Persona.** To the world, Avareen lives in a windowless house in Brindul Alley and is not there to meet her neighbors." | Day-one. The house and the neighbours are sourced by `sources/adventure-wdh.json:7193` and `:7202` | A1, A8 |
| 9 | L21 (b) | "To those who work with her, she is reliable, thorough, and personally uninvested in outcomes." | Day-one; trait, unsourced (F9) | n/a |
| 10 | L21 (c) | "Deep down, she has a pass-amulet to Kolat Towers because Manshoon has never had a reason to question her, and she has taken care that no reason develops." | The amulet is day-one (A5). The "because ... never had a reason to question her" and "taken care that no reason develops" clauses have no source (F5) | A5 |
| 11 | L23 (a) | "In a fight, Avareen fights with a spy's discipline: efficient, targeted, and oriented toward extraction rather than victory." | Day-one; unsourced combat style (F10) | n/a |
| 12 | L23 (b) | "She does not sacrifice herself for the building." | Day-one; unsourced. Consistent with `05-agorn-fuoco.md` contrast (G4) | n/a |
| 13 | L25 (a) | "**Relationships.** Avareen is the Zhentarim interrogation operative at the Brindul Alley Interrogation House," | Day-one | `organizations/09-manshoons-zhentarim.md:57`; `guides/factions/10-manshoons-zhentarim.md:21` |
| 14 | L25 (b) | "Zorbog Jyarkoth's operational partner," | Day-one | A6; H1 |
| 15 | L25 (c) | "a pass-amulet holder for Kolat Towers," | Day-one | A5 |
| 16 | L25 (d) | "and Ott Steeltoes's current jailer." | **QUEST-TIME. Restate or remove.** Ott is free and tends Sylgar on Ches 1, 1492 DR (brief line 69). The captivity is routed to **Faction Outposts**. The page must not say it on day one. | Captivity: `campaign/guides/factions/10-manshoons-zhentarim.md:25` ("Strapped into the rack is **Ott Steeltoes**, a Xanathar's Guild agent captured while the Zhentarim were trying to locate the Eye."). Also `campaign/structure/arc-e-faction-outposts.md:205` ("Backroom: a torture rack, an arcane circle, and Ott Steeltoes strapped to a chair."). Also `sources/adventure-wdh.json:7204` ("Gagged and tied to a chair in the back room of the house is a known member of the Xanathar Guild"). Ruling: `campaign/setting/organizations/08-xanathars-guild.md:105` ("free and tending Sylgar at campaign start") |
| 17 | L29 | "A quiet woman who lives in a windowless house in Brindul Alley and shows no interest in meeting her neighbors. She is polite, unhurried, and entirely professional about whatever it is she does inside." | Day-one OK | A1, A8 |

**Quest-time clauses in the voice profile** (`.claude/skills/character-voices/voices/manshoons-zhentarim.md:101-115`). The profile is copied verbatim into the page under ruling 16. The two lines below are borderline; the rest of the profile is day-one.

> "- **Business:** ..." — the profile line reads: "*Business:* \"Who gave you the map? Let's try that again. Who gave you the map?\""
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:114`

"Who gave you the map?" assumes a party already holding a map. It is not a capture event by itself. The drafter decides whether to keep it.

Full profile, verbatim (`.claude/skills/character-voices/voices/manshoons-zhentarim.md:101-115`):
> "### Avareen Windrivver"
> "*A quiet, polite interrogator who treats what she does as paperwork.*"
> "- **Sound:** A soft, pleasant, unhurried voice with a clerk's neutrality."
> "- **Sentence shape:** Polite, complete, patient sentences. Questions, then a pause, then the same question again."
> "- **Word choice:** Clinical and administrative: \"session\", \"cooperation\", \"to specification\". She calls the subject \"you\" and Zorbog by name."
> "- **Swearing:** *Never · Plain · n/a.* Her politeness is the menace."
> "- **Personality in speech:** Professional detachment. She's uninterested in the personal. Satisfaction in a job done correctly shows as a small \"Thank you.\""
> "- **Quirks:** She repeats a question with identical wording. She says \"Zorbog\" as a complete instruction."
> "- **Signature phrases:** \"Let's try that again.\" / \"Thank you.\" / \"Zorbog.\""
> "- **Never:** She never raises her voice, never hurries, and never gives anyone a reason to doubt her."
> "- **Sample lines:**"
> "  - *Greeting:* \"Please come in. Sit. This will go more smoothly if you're comfortable.\""
> "  - *Business:* \"Who gave you the map? Let's try that again. Who gave you the map?\""
> "  - *Under pressure:* \"Zorbog.\""
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:101-115`

---

## D. Conflicts

Rank: campaign files first, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.

**D1. Ward of the Interrogation House (Brindul Alley): North Ward against Trade Ward**
- Campaign, North Ward (higher; settled by the user in Session 51):
  > "Settled by the user (Session 51): Brindul Alley's ward is the North Ward, as the Zhentarim Factions Guide and `arc-i-kolat-towers.md:15` say. `arc-e-faction-outposts.md:117` and `:201` said "Trade Ward" and now say North Ward. The alley is not in the wiki's North Ward street list."
  > — `campaign/gazetteer/waterdeep/north-ward.md:272` (Draft Notes)
  > "- **Zhentarim Interrogation House** (North Ward, Brindul Alley)" — `campaign/guides/factions/10-manshoons-zhentarim.md:62`
  > "*North Ward, Brindul Alley.* — **Street-level entry point for the Manshoon chain** (for parties with **Gralhund Villa** documents)." — `campaign/structure/arc-e-faction-outposts.md:201`
- Adventure, Trades Ward (lower):
  > "The characters' search for the {@item Stone of Golorr|WDH} leads them to a snow-covered alley in the Trades Ward that contains a windowless Zhentarim safe house ({@area L1|140}) and a meat shop called Cuttle's Meat Pies ({@area L2|141})."
  > — `sources/adventure-wdh.json:7174`
- Alexandrian, printed p.45 [PDF p.10] (image):
  > "ZHENTARIM INTERROGATION HOUSE (Trade Ward, Brindul Alley): Avareen Windrivver (LE female Illuskan human spy) and Zorbog Jyarkoth (NE male Turami human thug) maintain this combination safe house / covert interrogation center."
  > — `sources/5. Faction Outposts.pdf` printed p.45 (image)
- SOURCE_GUIDE summary (a summary, not a source):
  > "- Safe house near Trades Ward with coded correspondence"
  > — `sources/SOURCE_GUIDE.md:215`
- Higher source: the campaign (North Ward). The Alexandrian and the adventure say Trades Ward. The page names only "Brindul Alley", which avoids the question. `[research]` on whether to name a ward at all.

**D2. Ott Steeltoes's captivity during the campaign against free on Ches 1**
- Ruling, campaign (higher):
  > "- **Ott Steeltoes** — Dwarf cult fanatic (Zuggtmoy), neutral evil. Guild field agent and Xanathar's fishkeeper, free and tending Sylgar at campaign start. Wears a leather skullcap stitched with fake beholder eyestalks. See the **Ott Steeltoes** page in Notable Figures."
  > — `campaign/setting/organizations/08-xanathars-guild.md:105`
- Present-tense captivity, campaign (routed to **Faction Outposts**, but written as a present state): `campaign/guides/factions/10-manshoons-zhentarim.md:25`; `campaign/structure/arc-e-faction-outposts.md:205`.
- Present-tense captivity, adventure (lower): `sources/adventure-wdh.json:7204`.
- Higher source: the campaign ruling. The Avareen page line 25 is stale (E1).

**D3. The Stone of Golorr in the house (adventure only)**
> "When the characters first enter the alley, Avareen is in the front doorway of the house, handing the {@item Stone of Golorr|WDH} to a high-ranking Zhent named Vevette Blackwater (CE female Tethyrian human {@creature swashbuckler|VGM}; see {@adventure appendix B|WDH|12}). Zorbog is stoking a fire in the fireplace while quietly observing the transaction. With stone in hand, Vevette scrambles up to the rooftops, leaving Avareen and Zorbog to deal with the survivors of the conflict between the characters and the bugbears."
> — `sources/adventure-wdh.json:7203`

Campaign: the house's contents (rack, circle, snakes, Ott, pass-amulet) do not include the Stone. Quotes: `campaign/structure/arc-e-faction-outposts.md:205`; `campaign/guides/factions/10-manshoons-zhentarim.md:21`-`:25`. Higher source: the campaign. The adventure's Stone scene is a quest event; the drafter should not use it.

**D4. Zorbog's "does not interrogate things" against the house's interrogation role and the Alexandrian directive**
- Campaign, Zorbog page (see the Zorbog notes file): "Deep down, he does not interrogate things."
- Campaign, the house: "Avareen Windrivver and Zorbog Jyarkoth maintain this building as a combination safe house and covert interrogation center." — `campaign/guides/factions/10-manshoons-zhentarim.md:21`
- Alexandrian, printed p.45 (image): "Zorbog is to squeeze Fenerus until he reveals everything he knows about these new participants."
- Higher source: the campaign. This is a tension for the drafter to resolve in the Zorbog page, not a fact conflict on this page.

**D5. Pass-amulet holders: SOURCE_GUIDE summary against the campaign and the Alexandrian**
> "- The force field: surrounds the towers, cannot be penetrated without a pass-amulet. Pass-amulets are held by Manshoon's named lieutenants — PCs must acquire them from an outpost (Yellowspire, see `5. Faction Outposts.pdf`) or by defeating a team in the field."
> — `sources/SOURCE_GUIDE.md:360`

The Alexandrian (printed p.45) and the campaign (`guides/factions/10-manshoons-zhentarim.md:23`) both put the amulet on Avareen at the house. The SOURCE_GUIDE line is a summary and says Yellowspire. Higher source: the campaign.

**D6. Name collision (wiki, not a conflict of fact)**
> "'''Avaereene''' was a [[lich]] and a former [[human]] [[wizard]] who was one of the most trusted agents of the [[Kirukeskai|Xanathar]], the leader of the [[Xanathar Thieves' Guild]] of [[Skullport]]. She oversaw the guild's slavery operations."
> — `sources/research/pass5-bundles/xanathars-guild/wiki.txt:1341`

Campaign: "- **Conflicts:** Avaereene. The wiki says the Guild's slave-taker Avaereene watched Ahmaergo (`wiki.txt:1242` in the notes). The campaign has Avareen Windrivver, a Zhentarim operative (`manshoons-zhentarim/06-avareen-windrivver.md`). No source says they are one figure. The page names neither."
> — `campaign/setting/notable-figures/xanathars-guild/02-ahmaergo.md:139`

Do not link the two. The wiki's Avaereene is a Guild figure of a different era and a different editions' death.

**D7. The adventure's "Brindul Alley" is a different place**
> "This is the lair of the Hand that Sings, a magical phantasm of a hand with a mouth in its palm." — begins the entry
> — `sources/adventure-wdh.json:31303` (entry "Brindul Alley", id 474, page 184; the entry sits in the "Infamous Alleys" inset, `:31283`)

The entry does not say which ward. It is in the adventure's list of alleys to avoid. Do not put the Hand that Sings in the campaign's Brindul Alley without a decision.

**D8. Interrogation House map page**
The Factions Guide says "Use the map for house L1 (DH p. 62)" (`campaign/guides/factions/10-manshoons-zhentarim.md:21`). The adventure's entry for the safe house is on page 64 (`sources/adventure-wdh.json:7198`-`:7199`, "page": 64). The map and the entry may both be right. Not a fact conflict for this page.

---

## E. Stale lines in other files (not edited), and routed quest references

### E1. Stale lines in files that show Ott as a captive, or Avareen as his captor

- `campaign/setting/notable-figures/manshoons-zhentarim/06-avareen-windrivver.md:25` (this page): "and Ott Steeltoes's current jailer." Quest-time on a day-one page. Restate or remove (C16).
- `campaign/setting/notable-figures/xanathars-guild/06-ott-steeltoes.md:148` (the Ott pilot page's draft note): "`notable-figures/manshoons-zhentarim/06-avareen-windrivver.md:25` calls Avareen \"Ott Steeltoes's current jailer\"." Already notes this line as stale.
- `campaign/structure/arc-e-faction-outposts.md:205`: present-tense captivity of Ott in the Backroom (quest structure, routed).
- `campaign/guides/factions/10-manshoons-zhentarim.md:25`: present-tense captivity (quest content, routed).

### E2. North Ward Draft Notes that are now stale

- `campaign/gazetteer/waterdeep/north-ward.md:284`: "- **Names with no page:** Marek Dunmere, Vhaspar Holmdreg, Seldo Wynd, Undevvur Thort, Hessa Dorn, Gaxly Rudderbust, Zorbog Jyarkoth and Ott Steeltoes appear as plain text." Stale once the Zorbog page exists. Avareen is not in this list because her page already exists.
- `campaign/gazetteer/waterdeep/north-ward.md:286`: "- **Other files found wrong (not edited):** `deities/ilmater.md:127` says no North Ward page exists, which is now stale. (`castle-ward.md:165` and `deities/00-the-deities.md:311, 320` were wrong against the table and now follow it.) `arc-e-faction-outposts.md:117,201` write \"Trade Ward\" for Brindul Alley. `sources/SOURCE_GUIDE.md:219` puts the Vault windmill in the North Ward, and `m05-the-theaters-back-room/design-notes.md:36,55` call that wrong and place it in the Southern Ward. `ev-01-the-fireball.md:128` calls Tally \"she\" against the Notable Figures page. The Castle page's six statues omit the Swordmaiden, which is correct, since Dragon Heist places it in the North Ward (`:31275-31276`)."
  Stale for the Brindul Alley clause: `campaign/structure/arc-e-faction-outposts.md:201` now reads "*North Ward, Brindul Alley.*" (D1). `arc-e-faction-outposts.md:117` now reads "through North Ward canvassing". The Trade Ward wording is gone from both.

### E3. Quest-time references to the house (routed)

- **Faction Outposts** (5A, the Interrogation House): `campaign/structure/arc-e-faction-outposts.md:199`-`:213`. The directive, the captive, the escalation. Key lines:
  > "*The Directive to Zorbog.* A flying snake arrives during or shortly after the party enters, bearing a sealed letter addressed to Zorbog. The letter is a *Directive to Zorbog* signed **Manshoon** — the first document in the campaign bearing his name as a signature. It orders the kidnap of Fenerus Stormcastle of Quill Alley, specifying delivery to the Interrogation House within four days."
  > — `campaign/structure/arc-e-faction-outposts.md:207`
  > "*Escalation: Manshoon moves to Alert (Tier 3).* Avareen's flying snakes carry the alarm faster than the party can move; if even one escapes, Manshoon knows within hours." — the sentence begins "**Escalation: Manshoon moves to Alert (Tier 3).** Avareen's flying snakes carry the alarm faster than the party can move; if even one escapes, Manshoon knows within hours." — `campaign/structure/arc-e-faction-outposts.md:213`
  > "*The Kidnap Complication.* The *Directive to Zorbog* orders Fenerus captured within four days of issuance. This complication is live — it fires 1d6+2 days after the directive is issued, regardless of whether the party acts." — `campaign/structure/arc-e-faction-outposts.md:305`
  > "If the party arrives after Fenerus has been taken: the house shows signs of struggle. The coded messages are undisturbed — Zorbog was after Fenerus, not intelligence. The trail leads back to the Interrogation House." — `campaign/structure/arc-e-faction-outposts.md:311`
- **Directive to Zorbog** and the kidnap (quest, Fenerus): `campaign/guides/factions/10-manshoons-zhentarim.md:23` (quoted in C and A5); `campaign/guides/gm-guide/running-the-villains.md:75` ("| **Manshoon vs. Bregan D'aerthe** | Escalating interference | Manshoon has identified Fenerus Stormcastle as a D'aerthe cut-out and ordered his abduction. ... | *Directive to Zorbog Jyarkoth* (Interrogation House), *Letter Regarding Fenerus Stormcastle* (Seven Masks Theater) |").
- **Revelation list**, printed p.122 [PDF p.2] (image): "A Directive to Zorbog (*Zhentarim Interrogation House*)" under "FENERUS STORMCASTLE'S HOUSE" — `sources/17. Outpost and Lair Revelation Lists.pdf` printed p.122.
- **Ott, rescue and the lead to the Lair**: `campaign/guides/factions/10-manshoons-zhentarim.md:27` ("If the party frees him, Ott immediately tries to recruit his rescuers into Xanathar's organization. ..."); `campaign/guides/factions/09-xanathars-guild.md:100` ("- Rescuing Ott Steeltoes (Zhentarim Interrogation House — Ott leads the party back to Xanathar)"); `campaign/structure/arc-e-faction-outposts.md:375` ("*Savra Belabranta (Order of the Gauntlet).* ... If Ott Steeltoes was recovered from the Interrogation House, Savra registers it as a moral victory regardless of the prisoner's faction affiliation."); Alexandrian printed p.45 "Rescuing Ott:".
- **Ott, the Trollskull basement**: `sources/adventure-wdh.json:3629` and `campaign/quests/faction-events/bregan-daerthe/m03-three-nights/` (Bregan D'aerthe quest). Not Avareen.
- **Kolat K22 thugs**: `campaign/structure/arc-i-kolat-towers.md:175` ("| 5 min | 2 thugs arrive at K22 from the Interrogation House via the Yellowspire circle. Kaevja's sending reaches Manshoon and field agents if not silenced. |"). Quest content; Kolat Towers is pending conversion.
- **Yellowspire ledger** (Doom Raiders quest, the pass-amulet carriers): `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:265` (quoted in A8).
- **The Interrogation House as the place the name is first given**: `campaign/setting/villains/manshoon.md:9`: "The party gets his name at the Interrogation House in **Faction Outposts**, which is where the **Manshoon Named** Event Outcome is marked." Quest reference.

### E4. Lieutenants list in the adventure (absence)

> "These lieutenants include Sidra Romeir ({@area K2|3db}), {@creature Manafret Cherryport|wdh} ({@area K3|3de}), {@creature Urstul Floxin|wdh} ({@area E5|41d}), Vevette Blackwater and Agorn Fuoco ({@area E8|425}), and {@creature Zhent Martial Arts Adept|wdh|Havia Quickknife} and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush} ({@area E10|42a})."
> — `sources/adventure-wdh.json:26763`

Avareen is not named in that list. Zorbog is not named there either.

---

## F. Gaps (what a Background would need that no source gives)

Each gap lists the sourced facts the drafter must stay consistent with.

1. **Birth, family, early life, where she grew up.** No source. Consistent with: "Illuskan human" (`06-avareen-windrivver.md:5`; `sources/adventure-wdh.json:7202`); "female" (`:7202`); twenties in appearance (`:7193`, Sora's view).
2. **How and when she joined the Zhentarim, and how she came to the house.** No Avareen-specific source. Consistent with: open recruitment, tenacity and loyalty valued (`sources/adventure-wdh.json:1443`); the Splinter was built about 1490 DR, with the house as a field office (`campaign/setting/history/08-the-players-arrive.md:32`); the Splinter's Interrogation House existed in the cell's first two years `[research]`.
3. **How long she has held the house post.** No source. Derived only: "two years building the Splinter" (`campaign/setting/history/04-the-founding-of-chains.md:68`); the cell's build date is about 1490 DR `[research]` (`history/08:32`). Any tenure longer than about two years needs a `[research]` or `[design]` tag.
4. **How she met Zorbog and why they work together.** No source. Consistent with: "Zorbog Jyarkoth's operational partner" (`06-avareen-windrivver.md:25`); "Avareen's partner at the Interrogation House" (`organizations/09-manshoons-zhentarim.md:102`); both are "Zhents loyal to Manshoon" (`adventure-wdh.json:7202`).
5. **The reason she holds the pass-amulet, and when she was given it.** No source. The page's clause "because Manshoon has never had a reason to question her" is unsourced. Consistent with: the amulet system is Manshoon's ("A pass-amulet system lets him revoke anyone's access from the towers," `manshoon.md:33`) and revocable.
6. **Her relation to Manshoon as a person.** No source beyond the orders. Consistent with: "Manshoon's word is my command." (`campaign/guides/factions/10-manshoons-zhentarim.md:39`, a note she wrote); "Take Prisoners, Not Corpses" (`organizations/09-manshoons-zhentarim.md:38`).
7. **Her view of the work beyond the job.** No source. The page's "a complete absence of interest in the personal dimensions of her work" (`06-avareen-windrivver.md:13`) is the campaign's own line. Keep it; do not contradict it.
8. **Her age, precisely.** Sora's "in her twenties" (`sources/adventure-wdh.json:7193`) is the only figure. Use "twenties" only.
9. **Her temperament toward the victims.** Unsourced trait in the page (`06-avareen-windrivver.md:21`: "reliable, thorough, and personally uninvested in outcomes"). Keep as the campaign's line.
10. **Her combat style.** Unsourced ("fights with a spy's discipline," `06-avareen-windrivver.md:23`). Consistent with the escape-first rule for captured lieutenants (`campaign/guides/factions/10-manshoons-zhentarim.md:7`: "will try to destroy it if capture seems certain").
11. **Her ties outside the cell**, family, friends, a lover. No source.
12. **A place she cares about.** No source. The house is a workplace only.
13. **Whether she is a Zhentarim interrogator by training.** The page calls her an "interrogator" (`06-avareen-windrivver.md:5`); the Alexandrian calls her a "spy" (printed p.45). No training source. Consistent with the Interrogation House's purpose: "covert interrogation center" (`campaign/guides/factions/10-manshoons-zhentarim.md:21`).
14. **The "Avaereene" name.** No source makes the wiki's Guild figure Avaereene and this Avareen the same person (`sources/research/pass5-bundles/xanathars-guild/wiki.txt:1341`; `campaign/setting/notable-figures/xanathars-guild/02-ahmaergo.md:139`). Do not link them.
15. **Her Stone, Eye or Ott knowledge.** Not known to her. No source says what she knows of the Eye. The Alexandrian gives Ott's "They kept asking me about where Xanathar kept the Eye!" (printed p.45, image), not Avareen's knowledge.

---

## G. Inner-life hints (sourced)

Each item is a source fact. The drafter uses them for Background and Personal goals (brief ruling 17). Do not contradict them.

**G1. Contempt for a directive, obedience anyway** (the only sourced reaction of hers):
> "A crumpled note from Avareen to Sercent, full of barely contained contempt: Avareen complains about Manshoon's directive to hand over a broadsheet publisher named Shan Chien for Sercent's \"foul rites,\" but closes with \"Manshoon's word is my command.\""
> — `campaign/guides/factions/10-manshoons-zhentarim.md:39`

The adventure's account of the Shan Chien ritual (the thing she objects to): "Amath has been using this ritual to \"turn\" broadsheet publishers as part of a larger plot to control the flow of information in the city-a critical element of {@creature Manshoon|WDH}'s takeover." — `sources/adventure-wdh.json:9750`

**G2. Self-preservation, but not at Agorn's price** (the amulet):
> "Every lieutenant carries a pass-amulet to Kolat Towers and will try to destroy it if capture seems certain, except Agorn, who trades his to save himself."
> — `campaign/guides/factions/10-manshoons-zhentarim.md:7`
> "Avareen carries a pass-amulet to Kolat Towers; her first instinct if captured is to destroy it."
> — `campaign/structure/arc-e-faction-outposts.md:205`

**G3. Satisfaction in a job done properly** (voice):
> "Satisfaction in a job done correctly shows as a small \"Thank you.\""
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:108`

**G4. Contrast with Agorn** (Agorn's page, the other amulet holder): "To those who capture him, he offers his pass-amulet, Amath Sercent's address, Manshoon's general operational structure, and whatever else occurs to him" — `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:21`

**G5. Nights out, blood on the armour** (habits, seen by a neighbour):
> "They come and go at strange hours, sometimes returning from a night's sojourn with blood on their leather armor."
> — `sources/adventure-wdh.json:7193`

**G6. The house as her home**:
> "Front Room. Avareen and Zorbog's quarters."
> — `campaign/guides/factions/10-manshoons-zhentarim.md:23`
> "Front Room: Avareen and Zorbog live here." — `sources/5. Faction Outposts.pdf` printed p.45 (image)

**G7. Manshoon's approach to her work** (the page's own line; keep verbatim):
> "**Motivations.** Avareen wants to run the Brindul Alley operation to Manshoon's specifications, maintain the pass-amulet's security, and deliver outcomes with minimum exposure."
> — `campaign/setting/notable-figures/manshoons-zhentarim/06-avareen-windrivver.md:15`

**G8. Her own morale** (page): "In a fight, Avareen fights with a spy's discipline: efficient, targeted, and oriented toward extraction rather than victory. She does not sacrifice herself for the building." — `06-avareen-windrivver.md:23`

**G9. Her cruelty and politeness, as a voice trait** (voice): "Her politeness is the menace." — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:107`

**G10. The Splinter's wider loyalty climate**: "Loyalty to him runs from devotion to calculation." — `campaign/setting/organizations/09-manshoons-zhentarim.md:43` (the belief "One True Manshoon"; the sentence continues with Havia and Mookie, not Avareen). Avareen is not named in that belief.

---

## H. Consistency between this page and Zorbog Jyarkoth's page

The two pages must agree on these points. Zorbog's page is `campaign/setting/notable-figures/manshoons-zhentarim/07-zorbog-jyarkoth.md`.

1. **Species, alignment, pronouns, stat block.** Avareen: "*Illuskan human spy (Zhentarim interrogator), lawful evil, she/her*. Stat block: **Spy**." (`06:5`). Zorbog: "*Turami human thug (Zhentarim), neutral evil, he/him*. Stat block: **Thug**." (`07:5`). The adventure gives "LE female Illuskan human spy" and "NE male Turami human thug" (`sources/adventure-wdh.json:7202`).
2. **They live and work in the same house.** Avareen: "A quiet woman who lives in a windowless house in Brindul Alley" (`06:29`). Zorbog: "A large man who occupies the windowless house at Brindul Alley alongside Avareen Windrivver." (`07:29`). Factions Guide: "Avareen and Zorbog's quarters." (`guides/factions/10-manshoons-zhentarim.md:23`). Keep "windowless" and "Brindul Alley" on both.
3. **Operational partnership.** Avareen: "Zorbog Jyarkoth's operational partner" (`06:25`). Zorbog: "Zorbog is Avareen Windrivver's operational partner at the Interrogation House" (`07:25`). Keep the same phrase on both.
4. **Direction.** Zorbog: "he takes direction from Avareen without comment, question, or visible opinion on the subject" (`07:21`). Avareen's voice: "She says \"Zorbog\" as a complete instruction." (`voices/manshoons-zhentarim.md:109`). Zorbog's voice: "He waits for Avareen's instruction before answering." (`voices/manshoons-zhentarim.md:127`). Consistent. Do not give Avareen's page a "takes direction from" line that contradicts this.
5. **Morale.** Avareen: "She does not sacrifice herself for the building." (`06:23`). Zorbog: "In a fight, Zorbog protects Avareen and the building, in that order. He does not retreat while Avareen is still inside." (`07:23`). Both lines stand. Neither page may say that Avareen protects Zorbog.
6. **The pass-amulet belongs to Avareen only** on these pages and in the sources (`guides/factions/10-manshoons-zhentarim.md:23`; Alexandrian p.45). Zorbog's page must not give him one.
7. **Ott Steeltoes.** Avareen's page carries the captive line (C16), which must come out. Zorbog's page does not mention Ott at all. The Zorbog page names Fenerus only if it is quest-time; keep it out of day-one text.
8. **Interrogation.** Avareen: "Zhentarim interrogation operative at the Brindul Alley Interrogation House" (`06:25`). Zorbog: "Deep down, he does not interrogate things." (`07:21`). These read as a tension. The Zorbog drafter must decide what "does not interrogate things" means before both pages go out (D4).
9. **Featured in.** Both pages: "**Featured in:** **Faction Outposts**" (`06:7`, `07:7`). Keep identical.
10. **Organization label.** Both: "**Affiliation:** Manshoon's Zhentarim" (`06:6`, `07:6`). The Factions Guide organization page names them under Key Members (`organizations/09-manshoons-zhentarim.md:101`-`:102`), with the same words "maintains the Interrogation House alongside Zorbog" and "Avareen's partner at the Interrogation House".
11. **Stat blocks.** Spy and Thug, as above. The Factions Guide roster: "Avareen Windrivver (**spy**) + Zorbog Jyarkoth (**thug**)" (`guides/factions/10-manshoons-zhentarim.md:29`).
12. **Ward.** Neither page names the ward. If the Avareen page names one, it must match Zorbog's page (D1).

---

## Not found

- **Wiki.** `scratchpad/wiki-manshoons-zhentarim/06-avareen-windrivver.txt` and `07-zorbog-jyarkoth.txt`: each reads `NOT FOUND`. Grep over `sources/research/*/wiki.txt` for `Avareen|Zorbog|Windrivver|Jyarkoth|Brindul Alley|Interrogation House`: no file. The only wiki hit near the name is the Guild figure Avaereene (D6).
- **Appendix B** (`sources/Appendix_B_-_Player_Factions.md`): no match for `Avareen|Zorbog|Windrivver|Jyarkoth|Brindul|interrogation`.
- **Appendix C** (`sources/Appendix_C_-_Player_Faction_Missions.md`): no match for `Avareen|Zorbog|Windrivver|Jyarkoth|Brindul`. Zhentarim mentions there are unrelated (Esloon Bezant, Field Ward thugs, Skeemo's safe houses).
- **SOURCE_GUIDE** (`sources/SOURCE_GUIDE.md`): no match for `Avareen|Zorbog|Windrivver|Jyarkoth|Brindul|interrogation`. The Faction Outposts summary says "Safe house near Trades Ward with coded correspondence" (`:215`).
- **Adventure** (`sources/adventure-wdh.json`): names appear at `:77-78` and `:405-406` (the Pronunciation Guide), `:7193`, `:7198`-`:7204` (the house scene). Not named in the lieutenants list (`:26763`). Not in Appendix B. "Brindul Alley" appears once more, as an unrelated alley (`:31299`).
- **Campaign** (all folders searched with Grep for `Avareen|Zorbog|Windrivver|Jyarkoth|interrogation house|Brindul`): gazetteer (north-ward, southern-ward, trades-ward, field-ward), guides (factions 08, 09, 10; gm-guide running-the-villains), organizations (09), villains (manshoon), structure (arc-d, arc-e, arc-i), history (04, 08), quests (doom-raiders m05 ev-01), notable-figures (manshoons-zhentarim 05, 06, 07; xanathars-guild 02, 06). Other Zhentarim pages (Vevette, Sidra, Urstul, Agorn, Amath, Vira, Manafret, Kaevja, Havia, Mookie, Yorn) do not name either figure in the house, except Agorn's amulet.
- **Notable Figures folder** (`manshoons-zhentarim/`, Grep for `interrogat|brindul|zorbog|avareen|pass-amulet|trades ward`): hits only on 03, 04, 05, 06, 07, 08, 10 (none names Avareen or Zorbog as a person except 06 and 07).
- **Alexandrian PDFs**: Grep cannot search PDF bodies. Read: `sources/5. Faction Outposts.pdf` printed p.45 (PDF p.10) and `sources/17. Outpost and Lair Revelation Lists.pdf` printed pp.121-123 (PDF pp.1-3). Not read for these two names: `sources/11. Lair  Xanathar’s Lair.pdf`, `sources/12. Lair  Zhentarim – Kolat Towers.pdf` (the most likely place for more of the pass-amulet and Kolat material), `sources/1. The Villains.pdf`, `sources/6. Faction Response Teams.pdf`. Those need a `pdftotext` pass.
- **Brief**: `docs/plans/setting-compendium-pass6-brief.md` names no Avareen or Zorbog ruling beyond Ott (line 69).
- **Voice doc** `.claude/skills/character-voices/voices/manshoons-zhentarim.md`: both profiles present (`:101-115`, `:119-133`). Nothing contradicts the page.

## Not readable

- `sources/Other remix files/*.docx`: not searched. The SOURCE_GUIDE does not list one for Avareen or Zorbog.
- PDFs listed above: not text-searched. The two read PDF pages are image transcriptions.

## Not run

- `voicecheck.py`: not run (research only).
- The page was not written. No file was edited except this notes file.
