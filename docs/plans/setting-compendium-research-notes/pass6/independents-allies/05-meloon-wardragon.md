# Pass 6 research notes: Meloon Wardragon

Page: `campaign/setting/notable-figures/independents-allies/05-meloon-wardragon.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 19). Ruling used: Ches 1, 1492 DR is day one. No prose drafted here.
Organization page: `campaign/setting/organizations/05-force-grey.md`. Factions Guide: `campaign/guides/factions/06-force-grey.md`.
Voice profile: `.claude/skills/character-voices/voices/independents-allies.md` lines 102 to 116.
Wiki: `scratchpad/wiki-independents-allies/05-meloon-wardragon.txt` (full page, not a stub). Editions: the wiki cites *Blackstaff Tower* (BST) and *Waterdeep: Dragon Heist* 5e (WDH5e) by ref name; no edition on most lines.

## Method and caveats

- No shell. Alexandrian PDF `sources/27. Addendum A Night in Trollskull Manor.pdf` read with the Read tool, PDF page 7 (printed p.184). The transcription is from the image. Check with `pdftotext -layout` before prose use.
- `sources/Appendix_B`, `Appendix_C` and `Appendix_D` quotes are from the markdown files.
- Campaign gazetteer and history pages read by Grep and Read.
- `Meloon Wardragon NPC Guide.docx` (SOURCE_GUIDE.md:692) cannot be opened.
- `voicecheck.py` was not run. No file was edited except these notes.

## Findings that change how the page is written

1. **The published adventure and the Blackstaff Tower wiki both put the occupation earlier than the campaign.** The campaign moves it to after the Field of Triumph (`history/08-the-players-arrive.md:138`). The wiki also dates his death to 1491 (line 25). The page must show him alive and genuine on Ches 1.
2. **The sources disagree on alignment, ethnicity and class.** The page says "neutral good (when himself)", "Chondathan" and "Warrior Veteran". The Trollskull Manor guide and Appendix D say "Champion Fighter", and Appendix D says "Illuskan". See D1 to D3.
3. **The Force Grey status is "active" by campaign decision.** The published adventure says "Until recently, he was a member of Force Grey" (`adventure-wdh.json:32255`). The org page records the settled departure (`05-force-grey.md:164`).
4. **The Force Grey quest files name Laraelra Harsard as a third rescuer of Vajra.** The Meloon page names only Renaer. Both are day-one history.

---

## A. Background facts by theme

### A1. Origin and arrival (wiki, Blackstaff Tower)

> "Meloon traveled to Waterdeep around [[1477 DR]]. He may have previously lived in [[Loudwater]]."
> — `scratchpad/wiki-independents-allies/05-meloon-wardragon.txt` line 62 (ref BST-p170)

> "| home           = [[Waterdeep]], [[Sword Coast North]]<ref name="BST-p170">{{Cite book/Blackstaff Tower|170}}</ref>" and "| formerhomes    = [[Loudwater]], [[Savage Frontier]]<ref name="BST-p170"/>"
> — same file, lines 11 and 12

> "Meloon was a member of the [[Clan Wardragon|Wardragon]] clan, which had been some of the early settlers of Waterdeep. Meloon was a descent of [[Laroun]], one of the early warlords of Waterdeep."
> — same file, line 82 (ref BST-p170-171)

> "At the [[Mysticslake]] tavern in Waterdeep, he was once pickpocketed but won the fight that resulted."
> — same file, line 62 (ref BST-p61)

### A2. The 1479 DR years (wiki, Blackstaff Tower; campaign confirmation)

> "In [[Nightal]] [[1479 DR]], Meloon was working as a hired blade in [[Waterdeep]] when [[Laraelra Harsard]] hired him as a bodyguard to accompany her into the sewers to rescue a trapped [[dwarf|dwarven]] worker."
> — `scratchpad/wiki-independents-allies/05-meloon-wardragon.txt` line 64

> "They eventually rescued the future [[Blackstaff]], [[Vajra Safahr]], from imprisonment and torture by [[Khondar Naomal|Khondar "Ten-Rings" Naomal]], who desired to have the power of the Blackstaff for himself."
> — same file, line 64

> "Meloon had a vision in which he spoke with his ancestor [[Laroun]] and pledged himself to the defense of Waterdeep."
> — same file, line 66 (the Nameless Haunt's lair; the Azuredge pull)

> "After Vajra assumed the role of the seventh Blackstaff and killed Khondar, Meloon became one of the members of Renaer's organization intended to replace the [[Moonstars]] as defenders of Waterdeep and the Blackstaff."
> — same file, line 70 (ref BST-p305)

> "In [[1479 DR]], Meloon obtained the fabled axe ''[[Azuredge]],'' a powerful relic forged by [[Ahghairon]] himself for Waterdeep's defense.<ref name="BST-p168">{{Cite book/Blackstaff Tower|168}}</ref> Meloon was able to communicate telepathically with the sentient axe."
> — same file, line 79 (refs BST-p168 and BST-p228-229)

> "- **1479 DR, the rescue:** Renaer Neverember and Meloon Wardragon rescued Vajra from agents of Khondar Naomal. Meloon's page places the rescue more than a decade ago, and Renaer's page says it left the Blackstaff permanently in his debt (**Meloon Wardragon**; **Renaer Neverember**). The year itself is `[research]`."
> — `campaign/setting/organizations/05-force-grey.md:28`

> "In 1479 DR `[research]` agents of Khondar Naomal took Vajra, and Renaer Neverember and Meloon Wardragon got her away from them (**Renaer Neverember**; **Meloon Wardragon**). Meloon has never mentioned it since, and Renaer's page says that it left the Blackstaff permanently in his debt (same pages)."
> — `campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md:20`

> "Vajra decided before the *Sending* went out. Renaer vouched for the party, and she trusts his word because he, Laraelra Harsard and Meloon Wardragon pulled her out of Khondar Naomal's cells. She never tells the party, and no speaker mentions it."
> — `campaign/quests/faction-events/force-grey/00-first-meeting/ev-01-first-meeting.md:21`

### A3. Force Grey and Vajra (campaign)

> "- **Meloon Wardragon:** Meloon is an active member who reports to Vajra, whose life he saved more than a decade ago alongside Renaer. His page is in the Independents and Allies group."
> — `campaign/setting/organizations/05-force-grey.md:109`

> "- **Losses Are Expected:** Force Grey takes the jobs that kill people, and its ranks turn over. The wiki says the older cadre took in new members steadily because so many died (Forgotten Realms Wiki, *Force Grey*, citing *City of Splendors: Waterdeep*, 3e). Meloon carries grief for colleagues he has outlived (**Meloon Wardragon**)."
> — `campaign/setting/organizations/05-force-grey.md:43`

> "- **Settled (ruling 17):** Meloon is an active member, per his Notable Figures page (`05-meloon-wardragon.md:26`). This is a deliberate departure from the published "Until recently, he was a member of Force Grey" (`adventure-wdh.json:32255`)."
> — `campaign/setting/organizations/05-force-grey.md:164`

### A4. Character, from the page and the sources (day one)

Page Persona, the day-one clause only (the quest clauses are in section C):

> "To the world, Meloon Wardragon is a barrel-chested warrior who enters every room at full volume — laugh, handshake, Azuredge at his hip and demonstrated on request. He fills taverns with warmth and expects nothing back for it. To those he trusts, he is the friend who shows up unprompted, who rescued Vajra alongside Renaer without being asked and never mentioned it again, who carries quiet grief for colleagues he has outlived."
> — `campaign/setting/notable-figures/independents-allies/05-meloon-wardragon.md:22`

> "{@creature Meloon Wardragon|wdh|Meloon} is a handsome, formidable warrior in his prime, who serves the goddess Tymora and loves a good fight. His friends-among them {@creature Renaer Neverember|wdh} and {@creature Vajra Safahr|WDH}-describe him as honest, optimistic, and extraordinarily lucky. Until recently, he was a member of Force Grey and reported directly to the Blackstaff. In recent months, Meloon has spent much of his time at the Yawning Portal."
> — `sources/adventure-wdh.json:32255` (the "Until recently" sentence is the conflict in D6)

> "{@creature Meloon Wardragon|WDH} (see {@adventure appendix B|WDH|12}) comes across as a cheery, optimistic, warm-hearted man eager to fight alongside those he considers his friends. The Yawning Portal staff and many of the regular guests know that Meloon is a skilled fighter with ties to Force Grey."
> — `sources/adventure-wdh.json:1547`

> "Endlessly optimistic. Buys rounds without being asked. Tells stories about dead people he loved with complete emotional openness. Sees himself in young adventurers and says so, directly. Is entirely who he appears to be — which is itself slightly unnerving after long enough in Waterdeep."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1359` (Roleplaying Keys; the profile begins at line 1354)

> "Tousled blond hair, a body built for cold and violence, wearing it easily at nearly forty. He squints with one eye when he smiles. A magnificent silver-and-electrum battleaxe is strapped to his side as if it were a hat. He looks like exactly the kind of man people write songs about. The songs are accurate."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1357` (Appearance)

> "Tells a story about a previous Force Grey operation — one that went wrong, involving a crypt in the City of the Dead that turned out to be occupied. He names people who died. He is not morbid about this; he is fond of them."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1368` (Topic 2)

> "Endlessly optimistic; buys rounds; tells stories about dead people he loved with complete emotional openness; sees himself in young adventurers and says so."
> — `campaign/guides/trollskull-manor/08-notable-patrons.md:62`

Voice profile, day-one parts (the quest clauses are in section C):

> "- **Personality in speech:** Optimism and iron loyalty. His grief for fallen friends is open and brief. Possessed, the emotions are performed: correct words, wrong timing, too much interest in Undermountain directions."
> — `.claude/skills/character-voices/voices/independents-allies.md:109` (the last sentence is C20)

> "- **Quirks:** Bone-crushing handshakes. He shows off Azuredge on request. He toasts Tymora before every drink. Possessed, he gives implausible excuses for why Azuredge stays sheathed."
> — same file, line 110 (the last sentence is C21)

> "- **Signature phrases:** "Tymora's luck!" / "Friend!" / "Want to see the axe?""
> — same file, line 111

### A5. Yawning Portal and tavern presence (day one)

> "| 9 | Meloon Wardragon *(reroll if a Force Grey contact the party has already met)* |"
> — `campaign/guides/trollskull-manor/06-tavern-time.md:65`

> "| 18 | Meloon Wardragon |"
> — `campaign/guides/trollskull-manor/06-tavern-time.md:96` (the same row is `sources/Appendix_D_-_Running_the_Tavern.md:1142`)

### A6. Other day-one anchors

> "Meloon as member of the new [[Force Grey]] helped adventurers in tough situations."
> — wiki line 72 (ref WDH5e-p16)

> "{@creature Meloon Wardragon|WDH} (see {@adventure appendix B|WDH|12}) or some other respected member of Force Grey helps the adventurers out of a tough situation."
> — `sources/adventure-wdh.json:1350`

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Page summary: "> - *Chondathan human fighter, neutral good (when himself) / neutral evil (while occupied), he/him*. Stat block: **Warrior Veteran**." — `05-meloon-wardragon.md:5`
- Adventure, occupied state: "{@i NE male Chondathan human adventurer under the control of an intellect devourer}" — `sources/adventure-wdh.json:1546`
- Adventure, restored state: "Meloon is neutral good." — `sources/adventure-wdh.json:32268`
- Wiki: "| alignment5e    = [[Neutral good]]" — `05-meloon-wardragon.txt` line 52
- Trollskull Manor guide: "**Meloon Wardragon** *(Champion Fighter, NG Chondathan human)*" — `campaign/guides/trollskull-manor/08-notable-patrons.md:61`
- Appendix D: "*Force Grey — NG Illuskan human, Champion Fighter*" — `sources/Appendix_D_-_Running_the_Tavern.md:1355`
- Force Grey event, occupied: "> Meloon Wardragon (Neutral Evil, Chondathan Human, he/him) :: a Force Grey veteran with an Occupying Devourer behind his eyes, warm on the surface and curious in the wrong direction." — `campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/ev-01-the-tenday-watch.md:196`

**Species and ethnicity**
- Page: "Chondathan human" (`05-meloon-wardragon.md:5`); adventure: "NE male Chondathan human" (`adventure-wdh.json:1546`)
- Wiki: "| race           = [[Human]]" and "| ethnicity      = [[Chondathan]]<ref name="WDH5e-p20"/>" (`05-meloon-wardragon.txt` lines 14 and 15)
- Appendix D: "NG Illuskan human" (`Appendix_D_-_Running_the_Tavern.md:1355`). Conflict, see D2.

**Pronouns**
- Page: "he/him" (`05-meloon-wardragon.md:5`)
- Adventure: "NE male Chondathan human" (`adventure-wdh.json:1546`)
- Wiki: "| sex            = Male" (`05-meloon-wardragon.txt` line 13)

**Stat block**
- Page: "Stat block: **Warrior Veteran**." (`05-meloon-wardragon.md:5`)
- Force Grey overview: "> The only fights are the hosted Meloon, who uses the **Warrior Veteran** stat block with the custom **Occupying Devourer** riding him, and the expelled devourer alone." — `campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/overview.md:10`
- Trollskull guide and Appendix D: "Champion Fighter" (see above). The adventure text read (`adventure-wdh.json:1540` to `:1550`, `:32251` to `:32275`) gives no stat block name.
- Wiki: "| class5e        = " (blank, `05-meloon-wardragon.txt` line 53)

**Age**
- Appendix D: "wearing it easily at nearly forty" (`Appendix_D_-_Running_the_Tavern.md:1357`). Wiki: "| age            = " (blank, line 17). Wiki description, 1479 DR: "Meloon was a very tall young man with broad shoulders, blond hair, and pale blond scruff on his face." (line 59, refs BST-p26-27)

---

## C. Quest-time sentences on the current page and the voice profile

Each sentence narrates a quest event, or a state that begins during the quest. The file where it already lives is given. Ruling 1: restate as a day-one fact or remove.

| # | Where | Sentence (exact) | Where it already lives |
|---|---|---|---|
| C1 | Summary L6 | "> - **Affiliation:** Force Grey (occupied by a Xanathar's Guild intellect devourer after the Field of Triumph, about three tendays before the first day of the watch)" | `m03-the-trouble-with-meloon/overview.md:21` ("After the Field of Triumph, an Occupying Devourer from Nihiloor's brood took his skull, about three tendays before the watch begins."); `trollskull-alley/design-notes.md:35` |
| C2 | Summary L7 | "**Featured in:** ... **The Dragon in the Harbor**, **The Trouble with Meloon**, **Destroy the Intellect Factory**, **The Legate's Eyes**" | Quest pages. "The Dragon in the Harbor" does not name Meloon in its body. The only hit is the unlock gate: "**The Trouble with Meloon** becomes available when an individual Force Grey member reaches Renown 5 and 4th level." (`force-grey/m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:472`) |
| C3 | Summary L8 | "> - **Timing:** The published adventure has the devourer take him "several months ago". The campaign moves it to after the Field of Triumph so the party meets him as himself first, as the Meloon section of the **Trollskull Alley** design notes explains." | `history/08-the-players-arrive.md:138` (Settled by the user). Draft Notes only; drop from the page. |
| C4 | Resonance L12 | "**Resonance.** ... horror when the party discovers that a devourer has been riding their friend. His brain is alive under it, and the party can force the devourer out in **The Trouble with Meloon**." | `m03/ev-02-the-extraction.md:9` ("Hold him and force the devourer out with a ward, with Azuredge as an anchor, or with both.") |
| C5 | Emotions L14 | "The occupied Meloon performs these emotions with slight miscalibrations: he orders something new, asks with too much specificity, misremembers small details." | `sources/Appendix_D_-_Running_the_Tavern.md:1370` (Act III only); `campaign/guides/trollskull-manor/08-notable-patrons.md:69` |
| C6 | Motivations L16 | "The intellect devourer wants to steer adventurers away from Undermountain, serve Xanathar's interests, and avoid detection." | `sources/adventure-wdh.json:32257` ("The intellect devourer's primary goals are to steer adventurers away from Undermountain and get them to undertake quests that further the aims of {@creature Xanathar|WDH}.") |
| C7 | Persona L22 | "The devourer occupies him after the Field of Triumph, about three tendays before the first day of the watch, and it keeps his brain alive and reads it. It has taken him into the lair twice by then. The wrongness is harder to name than to describe: the third person, the implausible Azuredge excuses, the drinks he never used to order, the directions through the sewers that lead straight into Xanathar patrols." | `m03/overview.md:21` (lair twice; telepathy); `m03/ev-01-the-tenday-watch.md:208` and `:218` (Azuredge excuses) |
| C8 | Persona L22 | "Deep down, Nihiloor's intellect devourer has marked him as a target precisely because he is trusted, well-connected, and constitutionally unable to believe that a friend's body could be used against him." | Quest-time secret. No quest file quotes this sentence. The devourer is Nihiloor's (`m03/overview.md:21`). Secret callout or cut. |
| C9 | Morale L24 | "While the intellect devourer rides him, he fights competently as a Warrior Veteran but steers outcomes to serve Xanathar's interests. He never draws Azuredge and never swears." | `m03/overview.md:85` ("he never draws Azuredge"); `m03/ev-02-the-extraction.md:165` ("Meloon swears constantly" after the extraction) |
| C10 | Morale L24 | "Each dawn the devourer must succeed on a DC 15 Charisma save to touch the axe, and the axe is Meloon's anchor when the party forces the devourer out." | `m03/overview.md:23` (DC 15 Charisma saving throw); `m03/ev-01-the-tenday-watch.md:154` ("Every dawn the devourer must succeed on a DC 15 Charisma saving throw to touch Azuredge.") |
| C11 | Morale L24 | "Once it is out, the real Meloon wakes with 1 level of Exhaustion and speaks only in fragments until a Long Rest. Then he remembers the whole occupation as a long dream, and he never knows what the devourer passed on." | `m03/ev-02-the-extraction.md:42` ("He takes 1 level of Exhaustion and speaks in fragments until a Long Rest."); `:165` ("He remembers the occupation as a long dream..."); `m03/overview.md:55` ("After a Long Rest he tells the party about the long dream...") |
| C12 | Relationships L26 | "... the closest friend of Renaer Neverember (whose growing unease, without knowing why, becomes alarm once the occupation takes hold), a Yawning Portal regular whose surface thoughts Bonnie reads as comprehensibly normal until the occupation, and, after the Field of Triumph, a host for Nihiloor's intellect devourer, which reports to the Guild through a courier because telepathy reaches only 60 feet." | Renaer's alarm: `notable-figures/independents-allies/02-renaer-neverember.md:25`. Bonnie: `m03/ev-01-the-tenday-watch.md:265` ("Bonnie (Neutral, Doppelganger, she/her) :: the Portal's barmaid, who read Meloon's surface thoughts once and has not tried again."). Courier and 60 feet: `m03/overview.md:21`. The "Meloon is an active member of Force Grey (reporting to Vajra Safahr...)" clause is day one (`05-force-grey.md:109`). |
| C13 | Overview L30 | "He fills taverns with warmth and will fight alongside anyone he calls a friend, until a devourer takes him over." | The "until" clause is quest-time (`m03/overview.md:21`). The Overview is GM text (ruling 19), so the clause is allowed only as a GM truth. |
| C14 | Inspirations L18 | "When playing Meloon, channel Thor (*Marvel*, early films); once occupied, shift to the T-1000 (*Terminator 2*)." | The "once occupied" clause is quest-time. Keep the first half. |
| C15 | Voice L103 (tagline) | "*A booming, warm-hearted warrior who fills every room. Once possessed, the warmth is note-perfect and slightly wrong.*" | The "Once possessed" clause restates the occupation (`m03/ev-01-the-tenday-watch.md:196`). |
| C16 | Voice L105 (Sound) | "Possessed, the volume stays but the laugh lands a beat late." | Quest-time (occupied). `m03/ev-01:196` |
| C17 | Voice L106 (Sentence shape) | "Possessed, he's over-specific: exact questions about routes, times and who knows what. He also slips into the third person." | `Appendix_D:1370`; `guides/trollskull-manor/08-notable-patrons.md:69` |
| C18 | Voice L107 (Word choice) | "Possessed, he orders new drinks and misremembers small shared details." | `Appendix_D:1370` |
| C19 | Voice L108 (Swearing) | "Possessed, the swearing stops, because the intellect devourer doesn't think to do it. That absence is a tell players can catch." | `m03/ev-02-the-extraction.md:165` (after the occupation he "swears constantly") |
| C20 | Voice L109 (Personality) | "Possessed, the emotions are performed: correct words, wrong timing, too much interest in Undermountain directions." | `Appendix_D:1370` |
| C21 | Voice L110 (Quirks) | "Possessed, he gives implausible excuses for why Azuredge stays sheathed." | `m03/ev-01-the-tenday-watch.md:208` ("Azuredge, which he says is lent to a friend.") and `:218` |
| C22 | Voice L112 (Never) | "Never: As himself: never cruel, never dishonest, never quiet. Possessed: never swears, never draws Azuredge." | `m03/overview.md:85` |
| C23 | Voice L116 (Sample) | "*Possessed:* "Meloon is glad to see you. Which way will you be going down? The sewers? Which entrance, exactly?"" | Voice profile only. Quest-time sample (the occupied speech). |

Quest and event clauses that the page does not carry (routed):
- Field of Triumph meeting: `campaign/quests/act-i/trollskull-alley/ev-05-the-field-of-triumph.md:50` ("a Force Grey fighter who competes here because he enjoys it") and `:54` ("Mark **Meloon Met**.").
- The Trouble with Meloon: `campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/ev-01-the-tenday-watch.md:45` ("Meloon Wardragon is one of mine, and he hasn't filed a report in three tendays.").
- Factions Guide mission: `campaign/guides/factions/06-force-grey.md:72` ("Force Grey veteran Meloon Wardragon is behaving oddly at the Yawning Portal. Watch him for a tenday, confirm what rides him and get it out of him before the courier's report on Day 10.")
- Published-adventure task: `sources/adventure-wdh.json:3806` ("A member of Force Grey has been acting strangely of late. His name is {@creature Meloon Wardragon|WDH}, and his happy-go-lucky demeanor has soured. He's been hanging around the Yawning Portal more than usual. Observe him for a tenday, then report back to me.")
- Appendix C mission: `sources/Appendix_C_-_Player_Faction_Missions.md:1784` (section "Arc FG-3 — The Trouble with Meloon") and `:1791`.
- Appendix B: `sources/Appendix_B_-_Player_Factions.md:938` ("| 4th | **The Trouble with Meloon** | Force Grey operative Meloon Wardragon has been behaving erratically. ...").
- Vault: `sources/adventure-wdh.json:14828` ("Vajra Safahr sends Meloon Wardragon (see Appendix B) to help the characters secure the vault, unaware that Meloon has fallen under Xanathar's sway.").

---

## D. Conflicts

**D1. Alignment**
- Page L5: "neutral good (when himself) / neutral evil (while occupied)" (`05-meloon-wardragon.md:5`)
- Trollskull guide: "NG Chondathan human" (`campaign/guides/trollskull-manor/08-notable-patrons.md:61`)
- Appendix D: "NG Illuskan human" (`sources/Appendix_D_-_Running_the_Tavern.md:1355`)
- Wiki: "Neutral good" (`05-meloon-wardragon.txt` line 52)
- Adventure (occupied) "NE" (`adventure-wdh.json:1546`); (restored) "neutral good" (`:32268`)
- Higher ranked: the campaign page and the m03 event. The Trollskull guide and Appendix D are older campaign-adjacent sources.

**D2. Ethnicity**
- Page and adventure: "Chondathan" (`05-meloon-wardragon.md:5`; `adventure-wdh.json:1546`); wiki "[[Chondathan]]" (line 15)
- Appendix D: "NG Illuskan human" (`Appendix_D_-_Running_the_Tavern.md:1355`). Higher ranked: adventure.

**D3. Class and stat block**
- Page: "Warrior Veteran" (`05-meloon-wardragon.md:5`); m03 overview: "**Warrior Veteran**" (`overview.md:10`)
- Trollskull guide: "Champion Fighter" (`08-notable-patrons.md:61`); Appendix D: "Champion Fighter" (`:1355`)
- Higher ranked: campaign (page and m03 overview).

**D4. Timing of the occupation**
- Adventure: "Meloon ... several months ago" (`adventure-wdh.json:1548`); "Three months ago, out of boredom, Meloon accompanied a fledgling band of adventurers on an expedition to Undermountain." (`adventure-wdh.json:32256`)
- Campaign: after the Field of Triumph, about three tendays before Mission 3 (`history/08-the-players-arrive.md:138`; `m03/overview.md:21`).
- Wiki: "However, around [[1491 DR]], during an expedition to [[Undermountain]] with an adventuring party, they were attacked by the [[Xanthar]]'s minions and an [[intellect devourer]] ate Meloon's brain." (`05-meloon-wardragon.txt` line 74)
- Higher ranked: campaign (settled by the user, `history/08:138`). The adventure's Undermountain expedition is not carried by any campaign file.

**D5. Death (wiki)**
- Wiki infobox: "| death          = 1491" and "| deathnotes     = (brain eaten by an [[intellect devourer]])" (`05-meloon-wardragon.txt` lines 25 and 26)
- Campaign: alive on Ches 1. Higher ranked: campaign.

**D6. Force Grey status**
- Adventure: "Until recently, he was a member of Force Grey and reported directly to the Blackstaff." (`adventure-wdh.json:32255`)
- Campaign: "Meloon is an active member who reports to Vajra" (`05-force-grey.md:109`; settled at `:164`). Higher ranked: campaign.

**D7. Who rescued Vajra**
- Meloon page L22: "rescued Vajra alongside Renaer" (Renaer only).
- Force Grey first meeting `ev-01-first-meeting.md:21` and m03 `ev-01-the-tenday-watch.md:23` name Laraelra Harsard as a third rescuer. Renaer page L25: "a man who rescued Vajra Safahr from Khondar Naomal's agents". Force Grey org page `05-force-grey.md:165` says Laraelra "has no Notable Figures page" (stale; see E).

**D8. When the devourer is active**
- Trollskull guide 08:64: "By Act II, Meloon has been compromised by a Xanathar's Guild intellect devourer." (`campaign/guides/trollskull-manor/08-notable-patrons.md:64`)
- Appendix D: "By Act III, Meloon Wardragon has been compromised by an intellect devourer planted by the Xanathar Guild" (`sources/Appendix_D_-_Running_the_Tavern.md:1363`)
- Campaign: after the Field of Triumph, Act I (`history/08:138`). Higher ranked: campaign.

**D9. Featured-in claim**
- Page L7 lists "The Dragon in the Harbor"; the m02 quest does not name Meloon in its body (C2). Unsupported.

---

## E. Stale lines in other files (not edited), and routed references

- `campaign/setting/notable-figures/independents-allies/02-renaer-neverember.md:13`: "... and a growing, private alarm at what Meloon has become." (quest-time)
- `campaign/setting/notable-figures/independents-allies/02-renaer-neverember.md:25`: "... the closest living friend of Meloon Wardragon (whose changed behavior has him alarmed) ..." (quest-time)
- `campaign/setting/organizations/05-force-grey.md:165`: "Laraelra Harsard, who appears in the Force Grey quest files as one of Vajra's rescuers, has no Notable Figures page and is also left out." (stale: `campaign/setting/notable-figures/independents-allies/08-laraelra-elra-harsard.md` now exists)
- `campaign/setting/organizations/06-doom-raiders.md:183`: "Meloon watching Davil. `notable-figures/doom-raiders/01-davil-starsong.md` line 25 and `adventure-wdh.json` line 1548 have Meloon watching Davil for Xanathar. `history/08-the-players-arrive.md` line 138 puts the intellect devourer's occupation after the Field of Triumph, so Meloon is himself on Ches 1." (consistent with the page)
- `campaign/setting/organizations/08-xanathars-guild.md:186`: "His Notable Figures page says the devourer took him "about three tendays before the first day of the watch" (`05-meloon-wardragon.md:6`), and the adventure says three months ago (`adventure-wdh.json:32256`)."
- `campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:128`: "Settled (user ruling recorded at `history/08-the-players-arrive.md:138`): Meloon Wardragon's occupation is dated after the Field of Triumph ..."
- `campaign/guides/trollskull-manor/08-notable-patrons.md:61` and `:64`: stat, alignment and timing conflicts (D1, D3, D8).
- `campaign/guides/trollskull-manor/06-tavern-time.md:34`: "Meloon may not be Meloon (see **Notable Patrons**)." (quest-time)
- `sources/Appendix_D_-_Running_the_Tavern.md:1370`: "He has no Topics and Agendas of his own anymore. He has his controller's." (quest-time)
- `campaign/setting/notable-figures/doom-raiders/01-davil-starsong.md:142`: "Meloon watching him belongs to **The Trouble with Meloon** and **Trollskull Alley**." (routed)
- `campaign/quests/act-i/trollskull-alley/ev-05-the-field-of-triumph.md:56`: "Force Grey Mission 3 brings him back changed."
- Wiki line 25 (death 1491) and line 74 (Undermountain expedition): not used (D4, D5).
- Not readable: `sources/SOURCE_GUIDE.md:692` lists `Meloon Wardragon NPC Guide.docx`.

---

## F. Gaps a Background needs, and the sourced facts to stay consistent with

1. **Birth, parents, childhood.** No source. Wiki: "| parents        = " (blank, line 29); "| dob            = " (blank, line 21). The only origin given: "traveled to Waterdeep around [[1477 DR]]. He may have previously lived in [[Loudwater]]" (line 62).
2. **How he became a hired blade.** Wiki: "Meloon was working as a hired blade in Waterdeep when Laraelra Harsard hired him as a bodyguard" (line 64). This is 1479 DR, thirteen years before the campaign.
3. **Why he joined Force Grey.** Wiki: "Meloon became one of the members of Renaer's organization intended to replace the Moonstars as defenders of Waterdeep and the Blackstaff." (line 70). The 1479 rescue is in A2.
4. **His faith.** Tymora: wiki line 18 ("| patron deity   = [[Tymora]]"); adventure `:32255` ("serves the goddess Tymora"); page Motivations ("honor Tymora through brave action"). The gods-in-prose rule sets the title form; check `campaign/setting/deities/tymora.md` before writing it.
5. **Azuredge.** Acquired 1479 DR, "forged by Ahghairon himself" (wiki line 79); telepathic bond (line 79). The adventure's Appendix A entry: "He can attune to {@item Azuredge|wdh} (see {@adventure appendix A|WDH|11})." (`adventure-wdh.json:32270`). The campaign gives the axe's day-one state only in Persona L22 and Overview L30.
6. **Laroun.** Ancestor: wiki lines 66 and 82. No campaign page mentions Laroun.
7. **Brother, sister, family.** None sourced.
8. **Date of the Field of Triumph.** `history/08` gives no date. Use "after the Field of Triumph" only.

---

## G. Inner-life hints in the sources (exact quotes)

- "who carries quiet grief for colleagues he has outlived" (`05-meloon-wardragon.md:22`)
- "Meloon carries grief for colleagues he has outlived (**Meloon Wardragon**)." (`05-force-grey.md:43`)
- "Tells stories about dead people he loved with complete emotional openness." (`Appendix_D_-_Running_the_Tavern.md:1359`)
- "He names people who died. He is not morbid about this; he is fond of them." (`Appendix_D:1368`)
- "Optimism and iron loyalty. His grief for fallen friends is open and brief." (voice L109)
- "He toasts Tymora before every drink." (voice L110)
- "pledged himself to the defense of Waterdeep" (wiki line 66)
- "honest, optimistic, and extraordinarily lucky" (`adventure-wdh.json:32255`)
- "the closest living friend of Meloon Wardragon" (`02-renaer-neverember.md:25`, Renaer's page)
- Do not use as day-one inner life: "constitutionally unable to believe that a friend's body could be used against him" (C8).
