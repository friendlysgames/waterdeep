# Pass 6 research notes: Manafret Cherryport

Page: `campaign/setting/notable-figures/manshoons-zhentarim/10-manafret-cherryport.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 17)
Model: `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md`
Sister page: `campaign/setting/notable-figures/manshoons-zhentarim/09-vira-solkan.md` (not related in any source)
Read only: `campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md` (merged; not edited, see H)

Method and caveats:
- Campaign files: Read and Grep, quoted from the file.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. Tags such as `{@creature ...}` are left as written. JSON escapes (`\"`) are shown as plain quotes.
- Alexandrian PDF: `sources/12. Lair  Zhentarim – Kolat Towers.pdf` (5 pages, printed pp. 92 to 96). No shell, so `pdftotext` could not run. Quotes were transcribed from the rendered page images. Cite as printed page with PDF page in brackets. Check exact wording with `pdftotext -layout` before any quote goes into prose. The Alexandrian Kolat PDF is the only Alexandrian source for Manafret.
- Wiki: `sources/research/**/wiki.txt`, Grep for `Manafret|Cherryport` returned zero matches. The scratchpad extract `scratchpad/wiki-manshoons-zhentarim/10-manafret-cherryport.txt` reads exactly `NOT FOUND`. No wiki edition applies.
- Source rank used: campaign files first, then the published adventure, then the Alexandrian PDF, then the wiki. Quest-time structure documents (the Kolat Towers structure doc, `arc-i`, authoritative until the Kolat journal exists) are campaign files and rank with the campaign.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

---

## A. Background facts by theme

The Manafret page has no Background. Each fact below carries a status: **DAY-ONE** (may stay on the day-one page), **QUEST-TIME** (route, do not state on the day-one page), or **UNDATED** (no date in any source; do not place it on Ches 1 without a `[research]` tag).

### A0. Identity, species, alignment, stat block, pronouns (DAY-ONE)

**Adventure: the entry for the kitchen (published, the strongest identity source)**
> "The halfling, {@creature Manafret Cherryport|wdh}, is one of {@creature Manshoon|WDH}'s lieutenants. He loves to cook, and uses his mage hand cantrip to cut vegetables. He assumes the characters are intruders unless convinced otherwise. Any ability check to do so is made with disadvantage, since Manafret knows that {@creature Manshoon|WDH} would have informed him if guests were expected. If the mage suspects the characters are intruders, he surreptitiously pours a vial of assassin's blood ({@dc 10} Constitution save, on a failure 10 ({@dice 3d6}) poison damage and {@condition poisoned} for 24 hours, half damage on a success and not {@condition poisoned}) into the stew before asking them to taste it and give him an honest critique. He then cries out to the guards in {@area K2|3db} and attacks. Combat in this area draws the attention of the Zhents in areas K2 and K7, who investigate."
> — `sources/adventure-wdh.json:28191` (entry "Zhent Cook", id `3df`, under "K3. Kitchen", `:28172`, page 149)

**Adventure: species, class, alignment and hit points (published)**
> "{@creature Manafret Cherryport|wdh|Manafret} is a lightfoot halfling {@creature mage}, with these changes:"
> — `sources/adventure-wdh.json:28192`

> "Manafret is neutral evil and has 31 ({@dice 9d6}) hit points."
> — `sources/adventure-wdh.json:28196`

> "He has these racial traits: He is Small, and his walking speed is 25 feet. He can move through the space of a Medium or larger creature. He has advantage on saving throws against being {@condition frightened}. He speaks Common and Halfling."
> — `sources/adventure-wdh.json:28197`

**Adventure: the ring (published)**
> "Manafret wears a teleporter ring (see \"Teleporter Rings\")."
> — `sources/adventure-wdh.json:28200`

**Alexandrian: the roster, the kitchen and the ring (printed p.94 [PDF p.3]; transcribed from image)**
> "Manafret Cherryport*" (roster column)
> "Area K3 – Kitchen" (roster column)
> "* Has a teleporter signet ring."
> — `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p.94 [PDF p.3]

**Alexandrian: the stat reference (printed p.95 [PDF p.4]; transcribed from image)**
> "Manafret Cherryport – lightfoot halfling mage, MM p. 347; see DH p. 149"
> — `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p.95 [PDF p.4]

**Campaign: summary line, alignment, species, stat block, pronouns (DAY-ONE)**
> "- *Lightfoot halfling mage (Kolat Towers cook), neutral evil, he/him*. Stat block: **Mage**."
> — `campaign/setting/notable-figures/manshoons-zhentarim/10-manafret-cherryport.md:5`

> "- **Manafret Cherryport** — Lightfoot halfling mage (Kolat Towers cook), neutral evil; see the **Manafret Cherryport** page in Notable Figures."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:105`

**Pronouns, sourced**
- Published: "He loves to cook" (`sources/adventure-wdh.json:28191`); "He then cries out to the guards" (`:28191`).
- Campaign page: "*Lightfoot halfling mage (Kolat Towers cook), neutral evil, he/him*." (`10-manafret-cherryport.md:5`)
- Pronoun table: "| Manafret Cherryport | manshoons-zhentarim/10-manafret-cherryport.md:5 | he/him | prose ("his halfling hospitality", "a man whose hospitality toward intruders") | High |" — `docs/plans/npc-pronouns-table-group-c.md:54`. Note: the table's evidence is the page's own prose, and the published line at `:28191` is the stronger source.

### A1. The kitchen and the household (DAY-ONE)

**Campaign: the Kolat Towers household (structure of the cell)**
> "- **Kolat Towers:** A dilapidated pair of towers stands one block north of Phaulkonmere, the Emerald Enclave's estate, behind a force field with the properties of a wall of force. Light from *continual flame* spells shows in the windows, and most neighbors believe the place is abandoned or haunted by the Kolat brothers (*Dragon Heist*, 5e; **Southern Ward**). Sidra Romeir runs the ground floor like a barracks, Manafret Cherryport cooks for the household, and Manshoon's three apprentices, Ered Payno, Havi Termock and Savara Firethorn, sleep in the old apprentices' quarters and wear teleporter rings (**Sidra Romeir**; **Manafret Cherryport**; *Dragon Heist*, 5e). Lady Gondafrey is still a prisoner inside (**Southern Ward**)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:54`

**Campaign: the Manshoon page's household line**
> "- **Kaevja Cynavern**, **Havia Quickknife**, **Mookie Plush**, **Manafret Cherryport** and **Yorn the Terror:** His household in Kolat Towers and the sanctum behind it. Kaevja watches the entrance, Havia and Mookie keep his audience chamber, Manafret cooks, and Yorn keeps the household afraid of its master."
> — `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:60`

**Adventure: the kitchen room (published, room K3)**
> "Mouthwatering scents fill this room, which contains the following features:"
> — `sources/adventure-wdh.json:28176`

> "If he hasn't already been drawn elsewhere, a portly halfling stands atop a stool and cooks at an iron stove."
> — `sources/adventure-wdh.json:28180`

> "A green, ghostly hand floats above a trellis table, holding a knife and cutting carrots and celery."
> — `sources/adventure-wdh.json:28181`

> "A staircase curves up one wall, leading to {@area K7|3ea}."
> — `sources/adventure-wdh.json:28182`

**Alexandrian: the kitchen in the roster (printed p.94 [PDF p.3])**
> "Area K3 – Kitchen" (roster, next to "Manafret Cherryport*")

### A2. The ring and the sanctum (DAY-ONE for holding a ring; the ring's use is QUEST-TIME)

**Campaign: the ring system's sources (structure doc, authoritative until the Kolat journal exists; DAY-ONE)**
> "*The Teleporter Ring System.* Reaching the sanctum from K22 requires a teleporter ring keyed to the K22 circle. Without a ring, the circle is inert. Sources for rings: Sidra Romeir (K2, carries two spares in addition to her own); Manafret Cherryport (K3, wears one on his right hand); any named lieutenant in the towers or sanctum. The party should identify how they plan to acquire a ring during Scene 3 — whether by defeating or bypassing a ring-holder in the towers. If the party enters via Yellowspire, they arrive at K22 but still need a ring to activate the circle in reverse for exit."
> — `campaign/structure/arc-i-kolat-towers.md:95`

**Campaign: the K3 entry (structure doc; the "kitchen" statement is DAY-ONE, the Alert poisoning is QUEST-TIME)**
> "**K3 — Kitchen.** Manafret Cherryport (mage) + 1 kitchen worker (commoner, non-combatant). Manafret is one of the longest-serving Splinter members — formerly of the Acquisitions division, recruited because he can operate a teleportation circle with mechanical precision under fire. He wears a teleporter ring on his right hand and will not give it up voluntarily. At Alert and Lockdown tiers, he has poisoned all food in the kitchen with midnight tears (DC 17 Constitution saving throw, 31 (9d6) poison damage on a failed save, or half on success; onset 1 minute; DC 13 Perception or DC 12 Nature to detect before consumption). He is efficient and loyal but not suicidal — if reduced below 15 HP, he attempts to flee to E3 via the K22 circle."
> — `campaign/structure/arc-i-kolat-towers.md:126`

**Campaign: the escalation row (QUEST-TIME; Kolat Towers escalation tiers)**
> "| Alert | Gaps shifted 30 min; amulets require DC 14 Arcana to recalibrate | Posts doubled; K22 adds 2 thugs to standard spectator/snake garrison; Manafret poisons all kitchen food | Manshoon in E12, staff in hand; simulacrum activated in E1 as decoy | 20 min |"
> — `campaign/structure/arc-i-kolat-towers.md:103`

**Campaign: the critical path (structure doc; QUEST-TIME as a route)**
> "*Running This Scene.* The critical path runs K1/K22 (entry) → K2/K3 (Sidra, Manafret, teleporter ring) → K22 (circle to sanctum) → E1/E2/E3 (sanctum foyer) → deeper sanctum → E12 or E13 (Manshoon). Everything else is optional."
> — `campaign/structure/arc-i-kolat-towers.md:116` (rest of the paragraph covers the timer and the garrison)

**Adventure: the ring as an object (published)**
> "To access {@creature Manshoon|WDH}'s extraplanar sanctum, one needs a {@item teleporter ring|WDH}: a brass signet ring bearing a stylized M, and which emanates an aura of conjuration magic when targeted by a {@spell detect magic} spell or similar magic. {@creature Manshoon|WDH} gives these rings to his most trusted servants."
> — `sources/adventure-wdh.json:28822` (header "Teleporter Rings", `:28818`, page 157)

> "As an action, a creature wearing a teleporter ring can activate the teleportation circle either in {@area K22|40b} or {@area E1|413}, teleporting itself and up to six other willing creatures from one circle to the other."
> — `sources/adventure-wdh.json:28823`

**Alexandrian: the two items (printed p.92 [PDF p.1]; transcribed from image)**
> "You need to obtain a **pass-amulet** in order to pass through the force field surrounding Kolat Tower."
> "You need to obtain a **teleporter signet ring** in order to reach the inner sanctum., as described on page 157 of *Dragon Heist*. These brass signet rings have a stylized M. written upon them."
> — `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p.92 [PDF p.1]. The printed text reads "inner sanctum.," with the stray punctuation as shown.

**Alexandrian: what lieutenants know (printed p.96 [PDF p.5]; transcribed from image; see D7)**
> "Manshoon's lieutenants know what the apprentice wizards know, but also:"
> "The layout of the extradimensional sanctum, including the location of the astral vault."
> — `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p.96 [PDF p.5]

**Alexandrian: what thugs and apprentices know (printed p.95 [PDF p.4]; transcribed from image)**
> "Manshoon's lieutenants wear special rings that let them access Manshoon's sanctuary atop the Outer Tower (although they don't know that this is actually an extradimensional space; they think he just lives up there)."
> — `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed p.95 [PDF p.4] (the bullet sits under "Thugs know the general layout of the tower:")
> "That Manshoon lives in an extradimensional sanctum."
> — same file, printed p.95 [PDF p.4] (apprentice wizards' bullet)

**Adventure: the sanctum from the thug Yorn (published, for contrast)**
> "He has never visited {@creature Manshoon|WDH}'s extraplanar sanctum, but he does know that the teleportation circle in {@area K22|40b} is the way to get there."
> — `sources/adventure-wdh.json:28348`

**Campaign: the sanctum's entry (DAY-ONE)**
> "- **The sanctum:** Behind the towers lies an extradimensional sanctum in a finite demiplane, which the original Manshoon created and his clones all know. A teleporter ring and the circle in the towers are the way in (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:55` (rest of the bullet covers Kaevja, Havia, Mookie and Yorn)

### A3. Service history and recruitment (UNDATED; one structure-doc sentence)

Only one source gives any past for Manafret:
> "Manafret is one of the longest-serving Splinter members — formerly of the Acquisitions division, recruited because he can operate a teleportation circle with mechanical precision under fire."
> — `campaign/structure/arc-i-kolat-towers.md:126`

No other file names the Acquisitions division (Grep `Acquisitions` across `campaign/`, `sources/` and `docs/`: only this line). No date, employer, or place is given for the recruitment.

**Splinter's founding (campaign; the earliest Manafret could have joined a Splinter unit)**
> "- **About 1490 DR, the clone takes the towers:** ... He then spent about two years building the Splinter, and in that time he peeled off a large part of the local network that the Doom Raiders had built (**The Founding of Chains**)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:30` (the bullet's quoted sentences are the whole of the Splinter clause; the ellipsis covers the clone's arm and the Undermountain history, which are quoted in full at `:30`)

**Sidra's page on the Splinter's start (the other pages' date, [research])**
> "She came to his service no earlier than the founding of the Splinter, about two years before Ches 1, 1492 DR `[research]`."
> — `campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md:17`

### A4. Personal goals and inner life (no source for goals)

No source gives Manafret a personal want beyond his job. The page's Motivations are verbatim roleplay (ruling 3):
> "**Motivations.** Manafret wants to cook well, keep the kitchen orderly, be useful to Manshoon, and welcome whoever the teleporter ring brings through the sanctum."
> — `campaign/setting/notable-figures/manshoons-zhentarim/10-manafret-cherryport.md:15`

The sourced habit and love are in A0 and G: "He loves to cook" (`sources/adventure-wdh.json:28191`).

### A5. Faith (UNDATED; the campaign says none is known)

> "No Notable Figure names Yondalla. The halflings among them are **Broxley Fairkettle**, **Osco Salibuck**, **Kelso Fiddlewick**, **Corene Wyldath**, **Manafret Cherryport**, **Havia Quickknife** and **Mookie Plush**, and none of their pages gives a god, so this page makes none of them a worshiper."
> — `campaign/setting/deities/yondalla.md:65`

> "- **Broxley Fairkettle**, **Osco Salibuck**, **Corene Wyldath**, **Manafret Cherryport**, **Havia Quickknife**, **Mookie Plush** (Notable Figures): the other halflings in the files, none with a stated god."
> — `campaign/setting/deities/yondalla.md:105`

---

## B. Alignment, species, pronouns, stat block

- **Alignment**: "neutral evil" — `10-manafret-cherryport.md:5`; `09-manshoons-zhentarim.md:105`; `sources/adventure-wdh.json:28196` ("Manafret is neutral evil and has 31 ({@dice 9d6}) hit points."). Consistent.
- **Species**: "Lightfoot halfling" — `10-manafret-cherryport.md:5`; `09-manshoons-zhentarim.md:105`; `sources/adventure-wdh.json:28192` ("...is a lightfoot halfling {@creature mage}, with these changes:"); Alexandrian printed p.95 ("lightfoot halfling mage, MM p. 347"). Consistent.
- **Stat block**: "Mage" — `10-manafret-cherryport.md:5` ("Stat block: **Mage**."); the adventure's "{@creature mage}" at `:28192`; Alexandrian printed p.95 "mage, MM p. 347; see DH p. 149". Consistent.
- **Pronouns**: he/him — `10-manafret-cherryport.md:5`; `sources/adventure-wdh.json:28191` ("He loves to cook"); pronoun table `docs/plans/npc-pronouns-table-group-c.md:54`. Consistent.
- **Role**: "lieutenant" — `sources/adventure-wdh.json:28191` ("is one of {@creature Manshoon|WDH}'s lieutenants"); `10-manafret-cherryport.md:25` ("a lieutenant whose threat is contextual"); `arc-i-kolat-towers.md:126` ("one of the longest-serving Splinter members"). Consistent. The organization page's "Kolat Towers cook" (`:105`) is a title, not a rank.
- **Ring**: "wears a teleporter ring" — `sources/adventure-wdh.json:28200`; "wears one on his right hand" — `arc-i-kolat-towers.md:95`; "He wears a teleporter ring on his right hand and will not give it up voluntarily." — `arc-i-kolat-towers.md:126`.

Ruling 4 is met: the pronouns are sourced, nothing is inferred.

---

## C. Every sentence on the current page

Current page: `campaign/setting/notable-figures/manshoons-zhentarim/10-manafret-cherryport.md`. Status: **DAY-ONE** (keep, restated if needed), **QUEST-TIME** (remove from the day-one page and route), **CONFLICT** (sourced elsewhere to the contrary; see D).

**L1** `# Manafret Cherryport` — title.

**L5** "*Lightfoot halfling mage (Kolat Towers cook), neutral evil, he/him*. Stat block: **Mage**." — DAY-ONE. Sources: B.

**L6** "- **Affiliation:** Manshoon's Zhentarim" — DAY-ONE. `campaign/setting/organizations/09-manshoons-zhentarim.md:19` (Two Zhentarims callout) and `:105`.

**L7** "- **Featured in:** **Kolat Towers**" — routed label. `campaign/structure/arc-i-kolat-towers.md` (the pending quest's structure doc; the quest is not yet a journal).

**L11 (Resonance)**
- Sentence 1: "Manafret should inspire endearment with his halfling hospitality" — DAY-ONE in substance (the kitchen, `sources/adventure-wdh.json:28191`).
- Sentence 2: "a specific kind of unsettling confusion when he does not register that you are intruders" — **CONFLICT** (D1): `sources/adventure-wdh.json:28191` says "He assumes the characters are intruders unless convinced otherwise."
- Sentence 3: "and the disquieting experience of being offered dinner by someone who works for a wizard who kills people." — DAY-ONE in substance; "a wizard who kills people" has no Manafret-specific source (the cell's violence is in the Manshoon page; not re-checked).

**L13 (Emotions)**
- "Manafret most often feels genuine domestic pride, the uncomplicated satisfaction of a well-run kitchen, pleasant curiosity about visitors who have not introduced themselves, loyal warmth toward Manshoon expressed through excellent food, and mild concern when guests seem confused." — DAY-ONE as roleplay; no source for the feelings. The "loyal" trait is echoed by `arc-i-kolat-towers.md:126` ("He is efficient and loyal"). "Pleasant curiosity about visitors who have not introduced themselves" sits oddly with the published "assumes the characters are intruders" (D1).

**L15 (Motivations)** "Manafret wants to cook well, keep the kitchen orderly, be useful to Manshoon, and welcome whoever the teleporter ring brings through the sanctum." — DAY-ONE as a want. "the teleporter ring brings through the sanctum" describes the sanctum's entry (`09-manshoons-zhentarim.md:55`); the ring's role is in A2.

**L17 (Inspirations)** "When playing Manafret, channel Bilbo Baggins (*The Hobbit*), Samwise Gamgee (*The Lord of the Rings*, domestic competence), and Hannibal Lecter (*Hannibal*, the disconcerting chef who welcomes you warmly)." — not a fact.

**L21 (Persona)**
- Sentence 1: "To the world, Manafret is the Kolat Towers cook who sets an extra place at the table for visitors who may arrive unexpectedly from the sanctum." — DAY-ONE as a habit. The "extra place" habit has no published source; it is voice-profile material (`manshoons-zhentarim.md:181`, "He sets an extra place mid-conversation.") and campaign-only.
- Sentence 2: "To those who enter the kitchen through the wrong door, he asks whether they have eaten, what they would prefer, and whether he should let Lord Manshoon know they have arrived." — **CONFLICT** (D1). The published entry has him assume intruders and check them with disadvantage (`:28191`). The "have you eaten" habit is the voice profile's (`manshoons-zhentarim.md:182`).
- Sentence 3: "Deep down, he wears the teleporter ring because Manshoon trusts him" — DAY-ONE. The ring is sourced (`sources/adventure-wdh.json:28200`); the reason "because Manshoon trusts him" fits "{@creature Manshoon|WDH} gives these rings to his most trusted servants" (`:28822`). Not a direct source for the cause.
- Sentence 4: "and the intruders always seem to respond well to the food." — QUEST-TIME in part. "always" implies a record of intruder encounters, and the published entry has him poison the stew of intruders he suspects (`:28191`). Restate or remove.

**L23 (Morale)**
- "In a fight, Manafret retreats to a defensible position, calls for help through whatever means are available, and uses his halfling size to make himself a difficult target." — QUEST-TIME (combat). **CONFLICT** (D2): `:28191` ("He then cries out to the guards in {@area K2|3db} and attacks.") and `arc-i-kolat-towers.md:126` ("if reduced below 15 HP, he attempts to flee to E3 via the K22 circle"). The "small size" clause is the published racial trait ("He is Small", `:28197`).
- "He does not use the teleporter ring except on Manshoon's orders." — DAY-ONE in intent, UNSOURCED. No source gives a rule about when Manafret may use his ring. `arc-i-kolat-towers.md:126` says only "will not give it up voluntarily". Tag `[research]` or route.

**L25 (Relationships)**
- "Manafret is Manshoon's Kolat Towers cook and a teleporter ring holder" — DAY-ONE (`:28191`, `:28200`; `arc-i:126`).
- "a lieutenant whose threat is contextual (his ring bypasses the pass-amulet system)" — **UNSOURCED** (D5). No source says a teleporter ring bypasses a pass-amulet. The Alexandrian gives pass-amulets for the force field and rings for the inner sanctum (printed p.92). The parenthesis must be cut or tagged `[research]`.
- "and a man whose hospitality toward intruders has probably prevented more deaths than his employer would prefer." — **CONFLICT** (D1, D3) and QUEST-TIME in part ("prevented more deaths" is a record of past encounters). The published entry has poison for intruders (`:28191`) and the structure doc has poison at Alert (`arc-i:103`, `:126`).

**L29 (Overview)** "The halfling cook of Kolat Towers who sets an extra place at the table for unexpected visitors. He asks whether they have eaten, what they would prefer, and whether he should let the tower's master know they have arrived." — DAY-ONE as the public face; the "extra place" and the questions are the voice profile's (`manshoons-zhentarim.md:181`, `:182`). The Overview sentence "He asks whether they have eaten" is not contradicted by the published entry, which leaves the greeting out.

**Voice block (not on the page yet; the drafter copies it from the profile, ruling 16).** Profile: `.claude/skills/character-voices/voices/manshoons-zhentarim.md:173`-`:187`. Quotes, exact:
> "*A delightful halfling cook who welcomes intruders to supper as if they were expected guests.*" (`:174`)
> "- **Sound:** A warm, merry, grandfatherly halfling voice." (`:176`)
> "- **Sentence shape:** Hospitable, rambling kitchen talk: menus, questions about appetite, fussing." (`:177`)
> "- **Word choice:** Food and hospitality: "have you eaten?", dishes by name, "Lord Manshoon". He calls everyone "dear"." (`:178`)
> "- **Swearing:** *Never · Euphemist · n/a.* "Oh, burnt biscuits!"" (`:179`)
> "- **Personality in speech:** Genuine domestic pride. He doesn't register intruders as threats. His loyalty to Manshoon comes out as fussing over the master's preferences. He's mildly concerned when guests seem confused." (`:180`)
> "- **Quirks:** He sets an extra place mid-conversation. He offers to let Lord Manshoon know they've arrived, which is a real threat he doesn't know he's making." (`:181`)
> "- **Signature phrases:** "Have you eaten, dear?" / "Shall I tell Lord Manshoon you've arrived?" / "Oh, burnt biscuits!"" (`:182`)
> "- **Never:** He never thinks the worst of a guest, never serves a bad meal, and never understands why people are frightened." (`:183`)
> "  - *Greeting:* "Oh! Visitors! Have you eaten, dear? Sit, sit, there's lamb and a lovely pudding."" (`:185`)
> "  - *Business:* "Shall I tell Lord Manshoon you've arrived? He does like to know."" (`:186`)
> "  - *Under pressure:* "Oh, burnt biscuits, you're not guests at all, are you?"" (`:187`)

Voice clauses that conflict or are quest-time (ruling 16 says restate and report):
- `:174` "welcomes intruders to supper as if they were expected guests" — **CONFLICT** with `:28191` ("He assumes the characters are intruders unless convinced otherwise.").
- `:180` "He doesn't register intruders as threats." — **CONFLICT** (D1).
- `:183` "He never thinks the worst of a guest, never serves a bad meal" — **CONFLICT** (D1, D3): `:28191` (poison in the stew of suspected intruders) and `arc-i:103`, `:126` (poison at Alert and Lockdown).
- `:187` "Under pressure: 'Oh, burnt biscuits, you're not guests at all, are you?'" — QUEST-TIME (a discovery line; the situation is combat or discovery).
- `:181` "which is a real threat he doesn't know he's making" — day-one characterization, not a quest event.

---

## D. Conflicts

Rank used: campaign files first, then the published adventure, then the Alexandrian PDF, then the wiki (none used). The campaign itself disagrees on several points, so each conflict says which file is which.

**D1. Does Manafret assume intruders, or does he not register them?**
- Page, L11: "a specific kind of unsettling confusion when he does not register that you are intruders" — `10-manafret-cherryport.md:11`
- Page, L21: "To those who enter the kitchen through the wrong door, he asks whether they have eaten" — `10-manafret-cherryport.md:21`
- Voice profile, `:180`: "He doesn't register intruders as threats." — `manshoons-zhentarim.md:180`
- Voice profile, `:183`: "He never thinks the worst of a guest, never serves a bad meal, and never understands why people are frightened." — `manshoons-zhentarim.md:183`
- Published adventure, `:28191`: "He assumes the characters are intruders unless convinced otherwise. Any ability check to do so is made with disadvantage, since Manafret knows that {@creature Manshoon|WDH} would have informed him if guests were expected."
- Structure doc, `arc-i-kolat-towers.md:103`: "Manafret poisons all kitchen food" (Alert).
- Higher source: the rule ranks campaign above published, and both the page and the voice profile are campaign files, but the structure doc (also campaign) and the published entry both say the opposite. The conflict is inside the campaign and the drafter cannot settle it from the files. Not resolved here.

**D2. Combat behaviour**
- Page, L23: "Manafret retreats to a defensible position, calls for help through whatever means are available" — `10-manafret-cherryport.md:23`
- Published, `:28191`: "He then cries out to the guards in {@area K2|3db} and attacks."
- Structure doc, `arc-i-kolat-towers.md:126`: "if reduced below 15 HP, he attempts to flee to E3 via the K22 circle."
- Higher source: the structure doc (campaign, authoritative until the journal). Route the combat tactics. The Morale line is roleplay and the day-one page should keep only the temperament.

**D3. Poison**
- Published, `:28191`: "he surreptitiously pours a vial of assassin's blood ... into the stew before asking them to taste it" (poison type: assassin's blood).
- Structure doc, `arc-i-kolat-towers.md:126`: "he has poisoned all food in the kitchen with midnight tears".
- Page, L25: "a man whose hospitality toward intruders has probably prevented more deaths" and voice `:183` "never serves a bad meal".
- Higher source: the campaign structure doc for the Alert and Lockdown mechanic; the published entry for the poison's identity (the campaign has no poison name for Manafret other than the structure doc). Both are quest-time. Not resolved; the day-one page should state neither.

**D4. Seniority**
- Structure doc, `arc-i-kolat-towers.md:126`: "Manafret is one of the longest-serving Splinter members"
- Sidra's page, `04-sidra-romeir.md:25`: "On Ches 1, 1492 DR she is the lieutenant who has served longest, and she runs the ground floor as she has for the whole of her time there `[research]`."
- Higher source: the structure doc (campaign). Both can be true ("one of" and "the longest"? no: they cannot both be exact). Sidra's claim is `[research]` on her page. Flag for the orchestrator; the Manafret page must not say he served longest.

**D5. The ring and the pass-amulet**
- Page, L25: "his ring bypasses the pass-amulet system"
- Alexandrian, printed p.92: "You need to obtain a **pass-amulet** in order to pass through the force field surrounding Kolat Tower." and "You need to obtain a **teleporter signet ring** in order to reach the inner sanctum."
- Published, `:28822`: "{@creature Manshoon|WDH} gives these rings to his most trusted servants." (no mention of the force field or the amulet)
- Structure doc, `arc-i-kolat-towers.md:128`: "They activate on any living creature entering without a pass-amulet or without Sidra present to vouch for them." (the gargoyles, K4; no ring)
- No source says a ring bypasses the amulet. Higher source: none supports the claim. Cut or tag `[research]`.

**D6. Ring use and control**
- Page, L23: "He does not use the teleporter ring except on Manshoon's orders." — `10-manafret-cherryport.md:23`
- Structure doc, `arc-i-kolat-towers.md:126`: "He wears a teleporter ring on his right hand and will not give it up voluntarily."
- Not contradictory (use versus surrender). The use rule is unsourced. Tag `[research]` or route.

**D7. What lieutenants know about the sanctum (Alexandrian, internal)**
- Alexandrian, printed p.95 [PDF p.4]: thugs "don't know that this is actually an extradimensional space" (the bullet is about thugs' knowledge).
- Alexandrian, printed p.96 [PDF p.5]: "Manshoon's lieutenants know what the apprentice wizards know, but also: The layout of the extradimensional sanctum".
- Published, `:28348`: "He has never visited {@creature Manshoon|WDH}'s extraplanar sanctum, but he does know that the teleportation circle in {@area K22|40b} is the way to get there." (Yorn, a thug)
- Page, L15 and L21: "welcome whoever the teleporter ring brings through the sanctum"; "visitors who may arrive unexpectedly from the sanctum".
- Higher source: the Alexandrian p.96 applies to lieutenants (Manafret is one, `:28191`). The page's sanctum lines are consistent with p.96. Not a conflict for Manafret.

**D8. Lieutenant rank (consistent)**
- Published: "is one of {@creature Manshoon|WDH}'s lieutenants" (`:28191`). Page L25: "a lieutenant whose threat is contextual". Consistent.

---

## E. Stale lines in other files (not edited), and routed references

### E1. Current files that narrate Manafret's quest-time behaviour

- `campaign/structure/arc-i-kolat-towers.md:103`: the Alert row, "Manafret poisons all kitchen food" (QUEST-TIME; authoritative structure doc).
- `campaign/structure/arc-i-kolat-towers.md:126`: the K3 entry's Alert and Lockdown poisoning and the flight at 15 HP (QUEST-TIME).
- `campaign/structure/arc-i-kolat-towers.md:116`: the critical path through K2/K3 (QUEST-TIME route).
- `campaign/setting/organizations/09-manshoons-zhentarim.md:54` is day-one; no quest-time text.

### E2. Routed to quests (where the quest-time facts already live)

- The kitchen fight and the alarm: `sources/adventure-wdh.json:28155` ("Combat in this area draws the attention of {@creature Manafret Cherryport|wdh} in {@area K3|3de}, who investigates."), `:28349` ("Combat in this area draws the attention of {@creature Manafret Cherryport|wdh} in {@area K3|3de}, who investigates.") and `:28191` (the poison and the attack). Structure doc: `arc-i-kolat-towers.md:116`, `:126`.
- The stew and the disadvantage check: `:28191` ("Any ability check to do so is made with disadvantage").
- The Alert and Lockdown tiers: `arc-i-kolat-towers.md:103` (Alert), `:126` (Alert and Lockdown).
- The Kolat Towers quest itself: Kolat Towers structure doc `campaign/structure/arc-i-kolat-towers.md` (the journal does not exist; Glob `campaign/quests/**/*kolat*` returned nothing).

### E3. Other stale or partial references (not edited)

- `campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md:39` and `:81` (Sidra's Connections and Morale): "The halfling cook of Kolat Towers, who feeds the household while Sidra keeps the ground floor. She calls for him when a fight begins." and "Once she draws, she calls for Manafret Cherryport, picks a defensible position, and does not leave it." Consistent with the day-one role; not a Manafret-page fact.
- `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:60`: "Manafret cooks" — consistent.
- `docs/plans/npc-pronouns-table-group-c.md:54`: he/him, row cites the page's prose, not the published line.
- `campaign/setting/organizations/09-manshoons-zhentarim.md:105`: "Lightfoot halfling mage (Kolat Towers cook)".
- `sources/SOURCE_GUIDE.md:35`: "Contains: Manshoon, his simulacrum, Sidra Romeir, Manafret Cherryport, Vevette Blackwater, Agorn Fuoco, Urstul Floxin." — the guide's Chapter 8 lists him as a principal NPC.

### E4. Day-one lines in other files (keep them)

- `campaign/setting/organizations/09-manshoons-zhentarim.md:54`, `:55`, `:105` (A1, A2, B).
- `campaign/setting/deities/yondalla.md:65`, `:105` (A5).
- `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:147`: "**Manafret Cherryport**" in the cell's lieutenants, household and sites list.

---

## F. Gaps (what a Background would need that no source gives)

For each gap: the sourced facts the drafter must stay consistent with.

1. **Birth, family, home, early life.** No source. Sourced: lightfoot halfling (`:28192`), Small (`:28197`), 31 hit points (`:28196`). Do not name a homeland or family.
2. **Career before the Splinter.** Only "formerly of the Acquisitions division" (`arc-i-kolat-towers.md:126`). No source names that division, its employer, its city or its date. Any Background must keep the phrase as given and tag the rest `[design]` or `[research]`.
3. **How and when he joined the cell.** Only "recruited because he can operate a teleportation circle with mechanical precision under fire" (`arc-i:126`), with no date. The Splinter's start is "About 1490 DR" (`09-manshoons-zhentarim.md:30`) and "two years" of building; Sidra's page dates her own arrival "no earlier than the founding of the Splinter" (`04-sidra-romeir.md:17`, `[research]`). Manafret's joining date must not contradict D4.
4. **Cooking.** "He loves to cook" (`:28191`) is the only sourced fact. No training, no dishes beyond the voice samples (`manshoons-zhentarim.md:185`, "lamb and a lovely pudding"), no kitchen history. The voice samples are voice text, not facts.
5. **Ring history.** No source gives when he got the ring or who gave it. `:28822` gives the rule that Manshoon gives rings to "his most trusted servants". The structure doc gives the hand ("right hand", `arc-i:95`, `:126`).
6. **Faith.** None stated. `campaign/setting/deities/yondalla.md:65` says "none of their pages gives a god". Do not give him a god.
7. **Relationships with the household.** Sourced only as roles: Sidra "calls for him when a fight begins" (`04-sidra-romeir.md:81`); the kitchen with the "1 kitchen worker" (`arc-i:126`); Kaevja, Havia, Mookie, Yorn (`09-manshoons-zhentarim.md:55`). No source links Manafret to Havia or Mookie (both lightfoot halflings, Alexandrian printed p.95: "Havia Quickknife / Mookie Plush (LE lightfoot halfling) – martial arts adepts, DH p. 209"). Do not invent a family tie without `[design]`.
8. **Manshoon.** "Manafret knows that {@creature Manshoon|WDH} would have informed him if guests were expected." (`:28191`) is the only sourced fact about the two men's exchange. The page's "loyal warmth toward Manshoon" (L13) is the page's own.
9. **Age, appearance beyond halfling.** No source. Do not write an age.
10. **Personal goals.** No source beyond Motivations (`10-manafret-cherryport.md:15`). Ruling 17 requires `[design]` goals.
11. **Fears and losses.** No source. The page's Emotions (`:13`) are campaign text.

---

## G. Inner-life hints in the sources (for the Background and goals)

Quoted exactly. Each marked DAY-ONE (habit, love, trait) or QT (quest-time).

- "He loves to cook, and uses his mage hand cantrip to cut vegetables." — `sources/adventure-wdh.json:28191` (DAY-ONE; the strongest personal fact in any source)
- "Manafret knows that {@creature Manshoon|WDH} would have informed him if guests were expected." — `sources/adventure-wdh.json:28191` (DAY-ONE; trusts Manshoon's word)
- "If he hasn't already been drawn elsewhere, a portly halfling stands atop a stool and cooks at an iron stove." — `sources/adventure-wdh.json:28180` (DAY-ONE; a habit of standing on a stool)
- "A green, ghostly hand floats above a trellis table, holding a knife and cutting carrots and celery." — `sources/adventure-wdh.json:28181` (DAY-ONE; his mage hand at work)
- "He is efficient and loyal but not suicidal — if reduced below 15 HP, he attempts to flee to E3 via the K22 circle." — `arc-i-kolat-towers.md:126` (DAY-ONE trait "efficient and loyal"; the flight is QT)
- "Manafret is one of the longest-serving Splinter members — formerly of the Acquisitions division, recruited because he can operate a teleportation circle with mechanical precision under fire." — `arc-i-kolat-towers.md:126` (DAY-ONE as a past; "mechanical precision" is a skill)
- "He sets an extra place mid-conversation." — `manshoons-zhentarim.md:181` (DAY-ONE habit; voice)
- "Oh! Visitors! Have you eaten, dear? Sit, sit, there's lamb and a lovely pudding." — `manshoons-zhentarim.md:185` (voice sample; DAY-ONE)
- "Genuine domestic pride. ... His loyalty to Manshoon comes out as fussing over the master's preferences." — `manshoons-zhentarim.md:180` (voice; DAY-ONE)
- "Emotions. Manafret most often feels genuine domestic pride, the uncomplicated satisfaction of a well-run kitchen" — `10-manafret-cherryport.md:13` (page's own; DAY-ONE)
- "Oh, burnt biscuits, you're not guests at all, are you?" — `manshoons-zhentarim.md:187` (QT: a discovery line)

---

## H. Consistency with Sidra Romeir's merged page, and the Two Zhentarims rule

H1. **Two Zhentarims.** Manafret is in Manshoon's cell, not the Doom Raiders' (`campaign/setting/organizations/09-manshoons-zhentarim.md:19`): "Anyone who deals with the Zhentarim through Davil is dealing with the Doom Raiders and not with Manshoon. The villains on this page answer only to Manshoon." Manafret's page L6 says "Manshoon's Zhentarim". No conflict.

H2. **Sidra's page names Manafret in three places, all day-one or routing:**
- `04-sidra-romeir.md:39`: "**Manafret Cherryport:** The halfling cook of Kolat Towers, who feeds the household while Sidra keeps the ground floor. She calls for him when a fight begins."
- `04-sidra-romeir.md:81`: "**Morale.** In a fight, Sidra waits for the intruders to commit before she draws. Once she draws, she calls for Manafret Cherryport, picks a defensible position, and does not leave it."
- `04-sidra-romeir.md:106`: "- **Manshoon**, **Urstul Floxin**, **Vevette Blackwater**, **Agorn Fuoco**, **Manafret Cherryport**, **Kaevja Cynavern**, **Davil Starsong** (Notable Figures): her master, the other lieutenants, the cook, the sanctum's watch and the leader of the other Zhentarim cell"
The Manafret page must keep: a cook; feeds the household (org `:54`); called to fights by Sidra (her page `:81`) and drawn by combat (`:28155`, `:28349`). The Manafret page's Morale must not say he answers to Sidra, and must not say he retreats from her call.

H3. **Seniority conflict with Sidra's page.** `04-sidra-romeir.md:25`: "On Ches 1, 1492 DR she is the lieutenant who has served longest" (`[research]`) against `arc-i-kolat-towers.md:126`: "Manafret is one of the longest-serving Splinter members". Sidra's Persona (`04-sidra-romeir.md:79`) says "she has outlasted every other lieutenant Manshoon has employed." Manafret's Background must not claim he served longer than Sidra. Not resolved in the files; the orchestrator decides.

H4. **Ring keeping.** Sidra's page: `04-sidra-romeir.md:38`: "Sidra holds the teleporter rings when a lieutenant leaves the Towers, and she hands a ring to the replacement when its holder does not come back." Sidra's Background (`04-sidra-romeir.md:25`, `[design]`): "In her first week she asked who held every teleporter ring, and Manshoon gave her the keeping of the ring system because of it." Manafret's ring: "He wears a teleporter ring on his right hand and will not give it up voluntarily." (`arc-i-kolat-towers.md:126`). Consistent only if Manafret keeps his own ring while he is at the Towers. The Manafret page must not say Sidra holds his ring, and must not say he has handed his ring to anyone. The campaign's "Sidra holds the rings" line (`09-manshoons-zhentarim.md:41`) and the structure doc's "Sidra Romeir (K2, carries two spares in addition to her own)" (`arc-i:95`) do not name Manafret.

H5. **Arrival.** Sidra's page places her in the Towers from "no earlier than the founding of the Splinter" (`04-sidra-romeir.md:17`, `[research]`). Manafret's Background must not place him earlier than the Splinter's founding (`09-manshoons-zhentarim.md:30`, "About 1490 DR") unless it is tagged `[design]` and the H3 conflict is decided. If it is placed later, Sidra's "longest" claim (`:25`) is unaffected.

H6. **Overview and Sidra's Overview.** Both pages describe the household's public face: Sidra "treats unexpected visitors with professional courtesy. She offers water, watches their hands and asks their business." (`04-sidra-romeir.md:48`). Manafret's Overview (`10-manafret-cherryport.md:29`) asks whether visitors have eaten. The two do not conflict; the Sidra page says she offers water and the Manafret page says he offers supper. Note only.

H7. **Featured in.** Sidra: "**Faction Outposts**, **Kolat Towers**" (`04-sidra-romeir.md:11`). Manafret: "**Kolat Towers**" (`10-manafret-cherryport.md:7`). No conflict.

---

## Not found

Searched, with the terms and files:
- `Manafret`, `Cherryport`: `sources/adventure-wdh.json` (K2, K3, K22, E1, Teleporter Rings, Yorn, Ered Payno entries), every non-research `sources/*.md`, `sources/SOURCE_GUIDE.md`, `sources/research/**/wiki.txt` (zero matches), `campaign/**`, `docs/**`.
- `Acquisitions` (the division): Grep across `campaign/`, `sources/`, `docs/`: only `arc-i-kolat-towers.md:126`.
- Manafret's birth, family, home, early career, recruiter, date of recruitment, personal goals, fears, faith, ring history: searched in the files above. Only the items in A and F were found.
- Manafret's own hit points beyond 31 and his age: no source for age.
- The wiki: `scratchpad/wiki-manshoons-zhentarim/10-manafret-cherryport.txt` reads exactly "NOT FOUND".
- The Force Grey pages (`campaign/quests/faction-events/force-grey/`) do not name Manafret (Grep, no match).
- The Factions Guide `campaign/guides/factions/10-manshoons-zhentarim.md`: no Manafret (Grep, no match).
- `campaign/setting/villains/manshoon.md`: no Manafret (Grep, no match).
- `campaign/gazetteer/waterdeep/` (all wards): no Manafret (Grep, no match).

---

## Not readable

- The Alexandrian Kolat PDF was read as page images. Its quotes are transcriptions and carry the `pdftotext` check note in the caveats. `pdftotext` is not available in this session.
- `sources/Other remix files/*.docx`: not opened. `sources/SOURCE_GUIDE.md` lists "The Waterdavian's Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place ...).docx" as a "Secondary reference only" source (`SOURCE_GUIDE.md:695`); it may name Manafret and could not be read. Ask the user to extract it if a Manafret Background needs it.

## Not run

- `voicecheck.py` was not run (research only).
- The page was not written. No file was edited except this notes file.
