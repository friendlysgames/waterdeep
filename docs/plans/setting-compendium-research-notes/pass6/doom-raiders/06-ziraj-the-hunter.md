# Pass 6 research notes: Ziraj the Hunter

Page: `campaign/setting/notable-figures/doom-raiders/06-ziraj-the-hunter.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Ziraj is a major NPC (brief ruling 2): full Personality and Connections apply.
Organization page: `campaign/setting/organizations/06-doom-raiders.md` (heading "The Zhentarim (Doom Raiders)")
Factions Guide: `campaign/guides/factions/07-doom-raiders.md`
Voice profile: `.claude/skills/character-voices/voices/doom-raiders.md` (### Ziraj the Hunter, lines 98-113)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`
Wiki extract: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-doom-raiders/06-ziraj-the-hunter.txt` contains only "NOT FOUND". No wiki page for Ziraj was found in that extract or in `sources/research/pass5-bundles/doom-raiders/wiki.txt` (Grep: no hit).

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes are shown as plain quotes. `{@creature ...}` tags are left as written.
- Alexandrian PDF: `sources/3. Player Character Factions.pdf` (PDF p.3, printed p.25) has no Ziraj text. PDF p.2 has none either.
- Alexandrian markdown: `sources/Appendix_B_-_Player_Factions.md`, `sources/Appendix_C_-_Player_Faction_Missions.md` (the Rooftop Assassin mission is a Lords' Alliance mission in that file, Arc LA-4, lines 616-683), `sources/Appendix_D_-_Running_the_Tavern.md`.
- No shell was available and no edit tool was available, so this file was written whole. `voicecheck.py` was not run. No other file was edited.
- Quest-file hits are Grep output. The `Ziraj` hits total 254 lines in 44 files under `campaign/` (count run). Cross-references lists each file with its count; quest lines are routed.

## Findings that change how the page is written

1. **Two campaign-day facts come from the Alexandrian Rooftop Assassin mission, and they conflict with the adventure.** The adventure says he kills only because a friend asked (`sources/adventure-wdh.json:31965`). Appendix C calls his kills "unsanctioned" and says "He did not tell Davil because Davil would have told him to stop." (`sources/Appendix_C_-_Player_Faction_Missions.md:623`, `:656`). The page follows the adventure. Both are quoted in D1.
2. **Species and weapon conflict with other campaign files.** The page and the adventure say half-orc and oversized longbow. The Trollskull guide and Appendix D say "Calishite"; Appendix C says "hand crossbow" (D2 and D3).
3. **Stat block label is not settled.** The page says "Assassin (with modifications)" (`:5`). Appendix C says "treat as **Veteran** with assassin modifications" (`Appendix_C:654`). The quest files use the Assassin block (D4).
4. **The page's Morale and Relationships contain quest-time clauses.** "If wounded" and "a colleague Yagra will run across the city to save" are quest-time (C rows 2 and 3).

---

## A. Background facts by theme

### A1. Origin, family, early life

**Adventure, Ziraj entry (page 201)**
> "{@creature Ziraj the Hunter|wdh|Ziraj} is a half-orc hunter who wields an oversized bow that shoots correspondingly large arrows. He is the Master of Assassination for the Black Network. If Ziraj sets out to kill someone, it's because one of his friends (Davil, Istrid, Skeemo, or Tashlyn) asked him to. The characters might become Ziraj's prey, or Ziraj might come to their aid to eliminate a common enemy. He's the strong, silent type."
> — `sources/adventure-wdh.json:31965` (entry "Ziraj the Hunter", page 201)

> "The City Watch has received reports of a figure who haunts the rooftops of Waterdeep-a hulking shadow that glares from its perch, rains down death in the form of long black arrows, and slinks off without so much as a whisper. Where he comes from-if he even has a home-remains a mystery, as does the question of where he might show up next."
> — `sources/adventure-wdh.json:31966`

No source gives a birth year, a name before "Ziraj", a family, a home, or an age. The adventure says "Where he comes from-if he even has a home-remains a mystery" (`:31966`). The wiki has no page for him (see Not found).

### A2. Joining the cell and his rank

**Adventure, the five leaders (the Zhentarim section)**
> "The Doom Raiders (described in appendix B) consider themselves the true Zhentarim of Waterdeep. The group's leaders are {@creature Davil Starsong|WDH} (Master of Opportunities and Negotiations), {@creature Istrid Horn|WDH} (Master of Trade and Coin), {@creature Skeemo Weirdbottle|WDH} (Master of Magic), {@creature Tashlyn Yafeera|WDH} (Master of Arms and Mercenaries), and {@creature Ziraj the Hunter|WDH} (Master of Assassination)."
> — `sources/adventure-wdh.json:1447`

**Adventure, what he offers the party**
> "Adventurers can hire {@creature Ziraj the Hunter|wdh|Ziraj} to assassinate someone, in return for some undisclosed favor to be called in later."
> — `sources/adventure-wdh.json:1456`

**Adventure, Davil's introduction of him**
> "Davil can put the characters in contact with other leaders of the Black Network's Waterdeep division, namely {@creature Istrid Horn|WDH} (if they need a loan), {@creature Skeemo Weirdbottle|WDH} (if they need magic), {@creature Tashlyn Yafeera|WDH} (if they need weapons or mercenaries), and {@creature Ziraj the Hunter|WDH} (if they need a highly skilled assassin)."
> — `sources/adventure-wdh.json:31925`

**Campaign, Organization page, Structure (the Master's title and post)**
> "  - **Ziraj the Hunter, Master of Assassination:** He kills from the rooftops with an oversized bow and keeps a back table at Corellon's Crown."
> — `campaign/setting/organizations/06-doom-raiders.md:61`

**Campaign, Organization page, Ranks and titles**
> "- **Ranks and titles:** The Masters' titles are the cell's only sourced ranks. Davil is the leader, as the wiki infobox and the published adventure agree (Forgotten Realms Wiki, *Doom Raiders*, 5e), and Tashlyn speaks for the cell when he is away. The ranks that members earn are a game rule and live in the Factions Guide."
> — `campaign/setting/organizations/06-doom-raiders.md:63`

**Campaign, Organization page, Key Members**
> "- **Ziraj the Hunter** — Master of Assassination; operates from the rooftops and Corellon's Crown. See the **Ziraj the Hunter** page in Notable Figures."
> — `campaign/setting/organizations/06-doom-raiders.md:101`

**Campaign, Factions Guide, Ardragon rank (a day-one service the cell offers)**
> "- Ziraj the Hunter can be requested for a single operation per quest, to be taken alive or quietly eliminated. He won't take suicidal assignments and doesn't argue about it."
> — `campaign/guides/factions/07-doom-raiders.md:16` (Ziraj's Ardragon favor is at line 59 in the same file)

**Campaign, Doom Raiders History (the cell's leaders and the trade)**
> "- Their leaders are Davil Starsong, Master of Opportunities and Negotiations; Istrid Horn, Master of Trade and Coin; Skeemo Weirdbottle, Master of Magic; Tashlyn Yafeera, Master of Arms and Mercenaries; and Ziraj the Hunter, Master of Assassination."
> — `campaign/setting/history/04-the-founding-of-chains.md:54`

### A3. Where he stays and his friendships

**Campaign, Organization page, Structure (the back table)**
> "Ziraj takes the back table at Corellon's Crown, where Fala Lefaliir shelters him. Tarrow's is a chandler's shop at 22 Sail Street run by Wenna Tarrow, and Corellon's Crown is a greenhouse in the North Ward (**Dock Ward**; **North Ward**)."
> — `campaign/setting/organizations/06-doom-raiders.md:64` (the sentence is part of a longer line; the complete line continues with the Black Network safe house on Sail Street)

**Adventure, Fala entry (page not read; the same entry is in the Trollskull community folder)**
> "{@creature Fala Lefaliir|WDH} is an outgoing wood elf with long, braided hair. Like the elven god Corellon Larethian, Fala is neither male nor female. If referred to as \"he\" or \"she,\" Fala gently requests to be addressed by name or as \"they.\" Fala is friends with a member of the Zhentarim named Ziraj, who saved Fala's life. He visits Fala from time to time, and Fala has set aside a room for him on the second floor."
> — `sources/adventure-wdh.json:3432`

**Campaign, Fala's page**
> "**Persona.** To the world, Fala is an outgoing wood elf herbalist with long braided hair who speaks without small talk and has strong opinions about tea. To those they trust, Fala is the person who shelters a Zhentarim assassin because he once saved their life, no questions asked. Deep down, Fala's curiosity runs deeper than their caution, and they know it."
> — `campaign/setting/notable-figures/trollskull-community/04-fala-lefaliir.md:21`

**Campaign, Fala's page, Relationships**
> "**Relationships.** Fala is a close friend of Ziraj the Hunter (Doom Raiders assassin, who keeps a room on Fala's second floor), a neighbor and confidant of Tally Fellbranch, and a member of the Guild of Apothecaries and Physicians. Fala uses they/them pronouns, reflecting Corellon Larethian's genderless nature."
> — `campaign/setting/notable-figures/trollskull-community/04-fala-lefaliir.md:25`

**Alexandrian, Appendix D, Fala's entry (the back table)**
> "2. Introduces the characters to Ziraj the Hunter, a large Calishite member of the Zhentarim Doom Raiders, who wants a quiet table in the back."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1271`

**Alexandrian, Appendix D, Yagra's entry (a past relationship)**
> "She and Ziraj the Hunter dated briefly; this is not a comfortable topic and she will change the subject with finality if it comes up."
> — `sources/Appendix_D_-_Running_the_Tavern.md:550` (the sentence is in Yagra's entry; it is a fact about Yagra and Ziraj, not Ziraj alone)

**Campaign, Organization page, Beliefs (the trail marks; the group sentence)**
> "- **The Network Looks After Its Own:** A member of the cell is one of theirs. When something goes wrong the faction does what it can, and it expects the same loyalty in return. Anyone who betrays or harms Istrid Horn finds her former adventuring companions using every resource they have to ruin them. The loyalty is personal as well as institutional. Yagra will reach a threatened friend's door at 2 AM in full armor, and Ziraj taught her the trail marks he leaves when he is wounded (**Yagra Stonefist**; **Ziraj the Hunter**)."
> — `campaign/setting/organizations/06-doom-raiders.md:37`

**Campaign, Quest, the trail code (routed quest text that states the backstory)**
> "Ziraj killed three or four of them on a warehouse roof off Sail Street before two crossbow bolts brought him down. He has been working toward Corellon's Crown ever since, marking the eaves with a code he taught Yagra years ago."
> — `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/overview.md:23`

### A4. Killing, his reason, and the cell's view of it

**Campaign, Organization page, Beliefs (Killing Is a Favor)**
> "- **Killing Is a Favor:** If Ziraj the Hunter sets out to kill someone, a friend in the cell asked him to, and if no one asked he would stop. He does not hunt for his own profit. The published adventure names the friends whose word counts as Davil, Istrid, Skeemo and Tashlyn (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/06-doom-raiders.md:42`

**Alexandrian, Appendix C, the Rooftop Assassin mission (Scene 3, the cell's backstory for him)**
> "He is a Doom Raider. His kills have been Xanathar Guild members who murdered a woman he was paid to protect six months ago. He tracked each of them for weeks before acting. He did not tell Davil because Davil would have told him to stop."
> — `sources/Appendix_C_-_Player_Faction_Missions.md:656` (conflicts with `sources/adventure-wdh.json:31965`; see D1)

### A5. Time in post

No source gives Ziraj's time in post. The adventure gives none (`sources/adventure-wdh.json:31965`). The Appendix C text gives "six months ago" for the woman he was paid to protect (`Appendix_C:656`). That is a kill history, not a post date.

### A6. Faith, signature belongings, appearance

**Adventure, Treasure (the weapon and the armor)**
> "Ziraj wears {@item +2 leather armor} and carries an {@item oversized longbow|wdh}. This unique weapon can be used only by a Medium or larger creature that has a Strength of 18 or higher. The bow shoots oversized arrows that deal piercing damage equal to {@dice 2d6} + the wielder's Strength modifier. Its range is the same as an ordinary {@item longbow|phb}."
> — `sources/adventure-wdh.json:31973` (Treasure subentry, page 201)

**Alexandrian, Appendix C, the first sight of him**
> "He is enormous — a half-orc of unusual even by half-orc standards, broad across the shoulders, with a face that has been in a number of fights and remembers all of them."
> — `sources/Appendix_C_-_Player_Faction_Missions.md:650` (a quest-scene read-aloud; the physical fact is usable, the scene is not)

No source gives a faith or a deity for Ziraj. The cell's rites are Istrid's (`campaign/setting/organizations/06-doom-raiders.md:43`).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, Summary: "> - *Half-orc assassin, lawful evil, he/him*. Stat block: **Assassin (with modifications)**." — `campaign/setting/notable-figures/doom-raiders/06-ziraj-the-hunter.md:5`
- Campaign, quest tags (all say the same): "> Ziraj the Hunter (Lawful Evil, Half-Orc, he/him) :: the Doom Raiders' Master of Assassination, who speaks in two to five words and reports in counts." — `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:348` (the same tag is at `ev-02-the-debrief.md:159`).
- Wiki: no page (NOT FOUND).
- Adventure: no alignment line in the Ziraj entry (`sources/adventure-wdh.json:31961-31977`).

**Species**
- Campaign: "Half-orc" (Summary, `06-ziraj-the-hunter.md:5`; quest tags above).
- Adventure: "is a half-orc hunter" (`sources/adventure-wdh.json:31965`).
- Appendix C: "a half-orc of unusual even by half-orc standards" (`Appendix_C:650`).
- Conflict: "a large Calishite member of the Zhentarim Doom Raiders" (`sources/Appendix_D_-_Running_the_Tavern.md:1271`) and "large Calishite Zhentarim" (`campaign/guides/trollskull-manor/08-notable-patrons.md:30`). See D2.

**Pronouns**
- Campaign: "he/him" (Summary, `06-ziraj-the-hunter.md:5`; quest tags above).
- Adventure: "He is the Master of Assassination for the Black Network." (`sources/adventure-wdh.json:31965`). Also "if he even has a home" (`:31966`).
- Appendix C: "He is enormous and quiet in the way that very large, very capable people sometimes are" (`Appendix_C:654`).

**Stat block**
- Campaign, Summary: "Stat block: **Assassin (with modifications)**." (`06-ziraj-the-hunter.md:5`).
- Adventure: no CR, AC, HP or block name. The Treasure subentry names the weapon and armor only (`sources/adventure-wdh.json:31973`).
- Appendix C: "**Ziraj the Hunter** (**Assassin**, *Dragon Heist* appendix B; treat as **Veteran** with assassin modifications for the 2024 rules)." — `sources/Appendix_C_-_Player_Faction_Missions.md:654`
- Quest, Lords' Alliance folder: "Ziraj uses the 2024 Assassin with an oversized longbow swap from his Notable Figures page." — `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/design-notes.md:11`
- Quest, the kill team: "Ziraj uses the **Assassin** block with an oversized longbow, starts at 38 Hit Points, and isn't counted as a combatant." — `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/overview.md:69`
- Wiki: NOT FOUND.

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/doom-raiders/06-ziraj-the-hunter.md`. The page has no Background section yet. Each row gives the exact sentence, the reason it is quest-time, and where the fact already lives.

| # | Line | Sentence (exact) | Why quest-time | Where it already lives |
|---|---|---|---|---|
| 1 | L7 | "**Featured in:** **Trollskull Alley**, **Kolat Towers**, **Vault of Dragons**, **Doom Raiders Mission 5 — The Yellowspire Job**, **Doom Raiders Mission 6 — Ziraj's Last Hunt**" | Quest names only (routed) | `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/`, `m06-zirajis-last-hunt/`; `campaign/guides/factions/07-doom-raiders.md:59` (the Ardragon favor) |
| 2 | L23 | "**Morale.** In a fight, Ziraj fires from elevation with his oversized longbow (requires Strength 18, deals 2d6 + modifier), repositions silently, and never engages in melee unless cornered. If wounded, he leaves intentional trail marks that he taught Yagra years ago." | "If wounded" is the state of the Ziraj's Last Hunt scene. The trail code is a backstory fact that the quest file states. The bow and the melee habit are day-one | `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/overview.md:17` ("Yagra Stonefist reaches Trollskull Manor at 02:10, armor on and breathing evenly despite the run from Sail Street. A Splinter kill team is hunting Ziraj the Hunter across the rooftops, and he is wounded somewhere east of where she lost his trail marks."); `m06-zirajis-last-hunt/overview.md:23` (A3, the taught code) |
| 3 | L25 | "**Relationships.** Ziraj is the Doom Raiders' Master of Assassination, a close friend of Fala Lefaliir (who shelters him at Corellon's Crown), a colleague Yagra will run across the city to save, and a presence on the Trollskull Alley rooftops that the party may not notice for weeks." | "a colleague Yagra will run across the city to save" is the rescue in Ziraj's Last Hunt | `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/overview.md:17` (Yagra's run from Sail Street); `m06-zirajis-last-hunt/overview.md:60` ("- **Yagra Stonefist** (Doom Raiders): brings the news, guides the party to the trail marks and carries Ziraj.") |
| 4 | L21 | "**Persona.** ... Deep down, he kills because someone he cares about asked him to, and if no one asked, he would stop." | Day-one wording, but conflicts with the Rooftop Assassin source (D1) | `sources/adventure-wdh.json:31965`; `campaign/setting/organizations/06-doom-raiders.md:42`; conflict at `sources/Appendix_C_-_Player_Faction_Missions.md:623` and `:656` |
| 5 | L21 | "... To those he trusts, he uses the quiet back table at Corellon's Crown and says \"Three left\" when asked for a report." | Day-one habit; the back table is in the Appendix D entry for Fala | `sources/Appendix_D_-_Running_the_Tavern.md:1271`; `06-doom-raiders.md:61` |
| 6 | L29 | "A half-orc of conspicuous size who keeps to Trollskull Alley's rooftops and rarely speaks — when he does appear at street level, it is at Corellon's Crown, at the back table, and only briefly." | "keeps to Trollskull Alley's rooftops" narrows the adventure's city-wide watch; the Trollskull Alley hunt is the Rooftop Assassin mission | `sources/adventure-wdh.json:31966` ("haunts the rooftops of Waterdeep"); `sources/Appendix_C_-_Player_Faction_Missions.md:623` ("My sources say he goes to ground somewhere near Trollskull Alley." is at Appendix C:632, quoted in D3) |

Quest-time clauses in the voice profile: none found. The profile's lines 99 to 113 are day-one. The sample "Business: \"Two on the roof. One in the alley. Mine.\"" is a sample line. Ruling 16 applies only to clauses that narrate a quest event.

Quest-time sentences in the source texts that the page does not use (for awareness):
- "Rishaal the Page-Turner at the Book Wyrm noticed a very large, very quiet individual buy a candle, three strips of dried meat, and a thin blanket \"for cold nights\" at a market stall near the alley about a week ago." — `sources/Appendix_C_-_Player_Faction_Missions.md:642`
- "He has been sleeping in my greenhouse for a week," Fala says quietly, to no one in particular. — `sources/Appendix_C_-_Player_Faction_Missions.md:670`

---

## D. Conflicts

**D1. Why he kills (adventure versus Alexandrian Rooftop Assassin mission)**
- Adventure: "If Ziraj sets out to kill someone, it's because one of his friends (Davil, Istrid, Skeemo, or Tashlyn) asked him to." — `sources/adventure-wdh.json:31965`
- Organization page: "If Ziraj the Hunter sets out to kill someone, a friend in the cell asked him to, and if no one asked he would stop." — `campaign/setting/organizations/06-doom-raiders.md:42`
- Alexandrian, mission overview: "a Doom Raiders operative conducting unsanctioned kills on personal motivation." — `sources/Appendix_C_-_Player_Faction_Missions.md:623`
- Alexandrian, mission scene: "He did not tell Davil because Davil would have told him to stop." — `sources/Appendix_C_-_Player_Faction_Missions.md:656`
- Higher rank: the published adventure (the source for the page's line, `06-ziraj-the-hunter.md:21`). The Alexandrian text is a mission and is in the "Lords' Alliance" file. The campaign uses the adventure's version (org page and page). The Alexandrian line is not settled here. The drafter should not state both as fact in a Background.

**D2. Species (half-orc versus Calishite)**
- Page, Summary: "*Half-orc assassin, lawful evil, he/him*." — `campaign/setting/notable-figures/doom-raiders/06-ziraj-the-hunter.md:5`
- Adventure: "is a half-orc hunter" — `sources/adventure-wdh.json:31965`
- Appendix D: "a large Calishite member of the Zhentarim Doom Raiders" — `sources/Appendix_D_-_Running_the_Tavern.md:1271`
- Trollskull guide: "- Introduces Ziraj the Hunter (large Calishite Zhentarim, wants a quiet table in the back)" — `campaign/guides/trollskull-manor/08-notable-patrons.md:30`
- Higher rank: the adventure and the page (half-orc). Appendix D and the patron guide are campaign-side and say "Calishite"; the conflict is not settled here.

**D3. Weapon (oversized longbow versus crossbow)**
- Adventure: "carries an {@item oversized longbow|wdh}" — `sources/adventure-wdh.json:31973`
- Quest, the kill team: "Ziraj uses the **Assassin** block with an oversized longbow" — `m06-zirajis-last-hunt/overview.md:69`
- Appendix C, the briefing: "We have reports of an assassin prowling the rooftops near the North Ward, picking off targets with a hand crossbow." — `sources/Appendix_C_-_Player_Faction_Missions.md:632`
- Appendix C, the scene: "A hand crossbow lies disassembled on a cloth in front of him" — `sources/Appendix_C_-_Player_Faction_Missions.md:650`
- Lords' Alliance design notes: "Appendix C's fourth Lords' Alliance mission, \"The Rooftop Assassin\", sends the party after Ziraj the Hunter, who has killed three people with a crossbow in the North Ward." — `campaign/quests/faction-events/lords-alliance/m04-the-archer-above/design-notes.md:5`
- Higher rank: the adventure and the page (longbow). The crossbow is in the Alexandrian mission only, and the Lords' folder notes that it is a different source.

**D4. Stat block label (page versus Appendix C versus quest files)**
- Page: "Stat block: **Assassin (with modifications)**." — `06-ziraj-the-hunter.md:5`
- Appendix C: "treat as **Veteran** with assassin modifications for the 2024 rules" — `sources/Appendix_C_-_Player_Faction_Missions.md:654`
- Quest, kill team: "Ziraj uses the **Assassin** block with an oversized longbow, starts at 38 Hit Points" — `m06-zirajis-last-hunt/overview.md:69`
- Quest, design: "Ziraj uses the 2024 Assassin with an oversized longbow swap from his Notable Figures page." — `m06-zirajis-last-hunt/design-notes.md:11`
- Higher rank: the quest files agree with the page (Assassin). The Appendix says Veteran. Not settled here.

**D5. Where he is seen (city-wide versus Trollskull Alley)**
- Adventure: "a figure who haunts the rooftops of Waterdeep" — `sources/adventure-wdh.json:31966`
- Page: "keeps to Trollskull Alley's rooftops" — `06-ziraj-the-hunter.md:29`
- Appendix C: "A rooftop assassin has been picking off targets in the North Ward." — `sources/Appendix_C_-_Player_Faction_Missions.md:623`
- Higher rank: the adventure (city-wide). The page narrows it to Trollskull Alley. Not a flat contradiction.

**D6. Where he sleeps at Fala's**
- Adventure: "Fala has set aside a room for him on the second floor." — `sources/adventure-wdh.json:3432`
- Fala's page: "who keeps a room on Fala's second floor" — `campaign/setting/notable-figures/trollskull-community/04-fala-lefaliir.md:25`
- Appendix C, the scene: "The greenhouse on the third floor of Corellon's Crown is a glass-and-iron structure" — `sources/Appendix_C_-_Player_Faction_Missions.md:649`
- Not a contradiction: the room is on the second floor, and the greenhouse is on the third. The Alexandrian line places him in the greenhouse during a quest scene.

**D7. Relationship to Yagra (romantic past)**
- Appendix D: "She and Ziraj the Hunter dated briefly; this is not a comfortable topic and she will change the subject with finality if it comes up." — `sources/Appendix_D_-_Running_the_Tavern.md:550`
- Organization page: "Yagra will reach a threatened friend's door at 2 AM in full armor, and Ziraj taught her the trail marks he leaves when he is wounded" — `campaign/setting/organizations/06-doom-raiders.md:37`
- Page: "a colleague Yagra will run across the city to save" — `06-ziraj-the-hunter.md:25`. The page calls Yagra a colleague and says nothing of a past romance.
- Higher rank: none conflicts. The romance is in the Yagra entry only. The drafter should not put it on Ziraj's page as a settled fact unless the Yagra page carries it.

**D8. The wiki (no page)**
- No wiki page exists in the scratchpad extract (`/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-doom-raiders/06-ziraj-the-hunter.txt`: "NOT FOUND"). No conflict can be drawn from the wiki.

---

## E. Stale lines in other files (do not edit) and routed quest references

**E1. Stale or conflicting lines in other files**
- `sources/Appendix_C_-_Player_Faction_Missions.md:623`: "...a man named Ziraj the Hunter, a Doom Raiders operative conducting unsanctioned kills on personal motivation." Conflicts with the adventure (D1).
- `sources/Appendix_C_-_Player_Faction_Missions.md:632`: "picking off targets with a hand crossbow" (D3).
- `sources/Appendix_D_-_Running_the_Tavern.md:1271`: "a large Calishite member of the Zhentarim Doom Raiders" (D2).
- `campaign/guides/trollskull-manor/08-notable-patrons.md:30`: "large Calishite Zhentarim" (D2).
- `campaign/quests/faction-events/lords-alliance/m04-the-archer-above/design-notes.md:5`: "who has killed three people with a crossbow in the North Ward" (D3).
- `campaign/gazetteer/waterdeep/north-ward.md:1` (count 1): not read in full.
- `campaign/setting/deities/gruumsh.md:111`: "- **Sister Valdra**, **Yagra Stonefist**, **Ziraj the Hunter**, **Hrabbaz**, **Grevik Nass**, **Yorn the Terror** (Notable Figures): the half-orcs in the files." Consistent with half-orc.
- `campaign/setting/history/04-the-founding-of-chains.md:54`: "and Ziraj the Hunter, Master of Assassination." Consistent.

**E2. Routed quest references (quest-time facts; the day-one page must not restate them)**

Ziraj's own quest appearances, by file (count of lines naming him):
- `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md` (66 lines). Sample: "> - Find Ziraj by following his trail marks, by reading the kill team's search pattern or by asking Fala Lefaliir, all before the sweep reaches him at 02:35."
- `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/overview.md` (20). Samples at lines 17, 23, 31 and 60 (quoted in C and A3).
- `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/design-notes.md` (6). Line 11 (quoted in B).
- `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md` (14) (line 348, the tag, quoted in B); `ev-02-the-debrief.md` (14) (line 159); `overview.md` (7). Samples: "Davil asks Ziraj to hand his surveillance notes on the Kolat Towers force field to whoever went into Yellowspire. Ziraj and Fala Lefaliir give them to Doom Raiders members at Corellon's Crown, in either version." — `m05-the-yellowspire-job/overview.md:56`; "**Ziraj's Last Hunt** becomes available at Renown 13 and 7th level, and it runs after **Kolat Towers**." — `m05-the-yellowspire-job/overview.md:70`
- `campaign/quests/faction-events/doom-raiders/r25-ardragon/ev-01-ardragon.md` (28), `design-notes.md` (4). The Ardragon crew favor: "Ziraj the Hunter extends Davil's friends a favor..." is in the Factions Guide (`campaign/guides/factions/07-doom-raiders.md:59`).
- `campaign/quests/faction-events/doom-raiders/r50-dread-lord/ev-01-dread-lord.md` (8)
- `campaign/quests/faction-events/doom-raiders/r10-viper/ev-01-viper.md` (1); `r10-viper/design-notes.md` (1)
- `campaign/quests/faction-events/doom-raiders/m04-silencing-skeemo/ev-02-the-chase.md` (1)
- `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md` (4); `00-first-meeting/design-notes.md` (1)
- `campaign/quests/faction-events/doom-raiders/s02-davils-return/design-notes.md` (1)
- `campaign/quests/faction-events/lords-alliance/m04-the-archer-above/design-notes.md` (3): Appendix C's Rooftop Assassin mission is a Lords' Alliance folder. The folder replaced Ziraj with a shooter in earlier drafts (its line 5).
- `campaign/quests/act-i/trollskull-alley/` (ev-03-the-neighbors.md 3; ev-04-the-factions-come-calling.md 1; ev-07-the-twin-parades.md 1; overview.md 1)
- `campaign/quests/faction-events/harpers/s01-the-cell-is-compromised/`: none found for Ziraj (the count list shows none).

Routed Appendix C mission, Rooftop Assassin (Lords' Alliance, LA-4), quest-time and not for this page: "Jalester wants him found and delivered to the Watch alive." (`sources/Appendix_C_-_Player_Faction_Missions.md:623`); "Each character who aids in Ziraj's capture receives 50 gp from Jalester." (`:681`).

Routed Appendix B table row: "| 5th | **The Rooftop Assassin** | Locate Ziraj the Hunter — a Zhentarim assassin picking off targets from the rooftops — and deliver him to the City Watch alive. He is reportedly hiding near Trollskull Alley. | +2 |" — `sources/Appendix_B_-_Player_Factions.md:275`.

Routed adventure line 401 (a creature tag in a list; context not read) and index line 32972 ("73. Ziraj the Hunter") are cross-references only.

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

**F1. Origin and birth.** No source gives a birth place, birth year, age, parents, a childhood name or a home. The adventure says "if he even has a home" (`sources/adventure-wdh.json:31966`). The page says "Where he comes from remains a mystery." (`06-ziraj-the-hunter.md:21`). A Background origin is `[design]` and must keep the adventure's mystery of where he comes from for players. The drafter may give the origin to the GM only.

**F2. Race and culture.** Conflict in D2. The adventure and the page say half-orc. The Calishite label in Appendix D is a conflict to be settled before a Background names a home.

**F3. How he came to the cell and the rank.** The sources say he is a Doom Raider and "Master of Assassination" (`sources/adventure-wdh.json:1447`). They do not say how he joined. The Factions Guide says he "won't take suicidal assignments and doesn't argue about it" (`campaign/guides/factions/07-doom-raiders.md:16`). A join story is `[design]`.

**F4. The woman he was paid to protect.** Sources: "His kills have been Xanathar Guild members who murdered a woman he was paid to protect six months ago." (`sources/Appendix_C_-_Player_Faction_Missions.md:656`). She is not named. Any name for her is `[design]` and must not be a named Notable Figure (brief ruling 17). The Appendix C text is a conflict with the adventure's reason (D1); a Background must choose the adventure's reason or state both as the cell's and his views.

**F5. Fala and the life he saved.** Sources: "Fala is friends with a member of the Zhentarim named Ziraj, who saved Fala's life." (`sources/adventure-wdh.json:3432`); Fala's page: "shelters a Zhentarim assassin because he once saved their life, no questions asked" (`campaign/setting/notable-figures/trollskull-community/04-fala-lefaliir.md:21`). The rescue itself is not described. The drafter must not state how or when the rescue happened; that is a `[design]` detail and must not contradict Fala's page.

**F6. Yagra and the trail code.** Sources: "marking the eaves with a code he taught Yagra years ago" (`m06-zirajis-last-hunt/overview.md:23`, quest file, the backstory clause); "Ziraj taught her the trail marks he leaves when he is wounded" (`06-doom-raiders.md:37`). The romance (D7) is in Appendix D's Yagra entry only. A Background may say he taught Yagra the code, and it must not state the romance as fact unless the Yagra page carries it.

**F7. Personal goals beyond the cell and Fala.** The sourced wants are in the Motivations line (`06-ziraj-the-hunter.md:15`): "keep Fala Lefaliir safe, and remain unseen by the rest of the world." Any further goal is `[design]`. Limits: no quest result, no Event Outcome, no Grand Game balance, no new Notable Figure.

**F8. The fact that he has no home.** The adventure says "if he even has a home" (`sources/adventure-wdh.json:31966`). Fala's page says he "keeps a room" at Fala's (`04-fala-lefaliir.md:25`). The room is a sourced place; a home elsewhere is not. A Background must not give him a home other than Fala's room and the back table.

**F9. Physical appearance.** The adventure has none beyond "hulking shadow" (`sources/adventure-wdh.json:31966`) and "half-orc". The Appendix C scene gives "enormous ... broad across the shoulders, with a face that has been in a number of fights and remembers all of them" (`sources/Appendix_C_-_Player_Faction_Missions.md:650`). Usable as a read-aloud description; the scene itself is quest content.

**F10. Why he kills only when asked (his reason).** The adventure gives it (`sources/adventure-wdh.json:31965`). The reason's deeper cause is not given. A cause is `[design]`, and it must agree with the adventure's rule that a friend asks.

---

## G. Source facts that hint at the figure's inner life (for the backstory; do not contradict)

- "If Ziraj sets out to kill someone, it's because one of his friends (Davil, Istrid, Skeemo, or Tashlyn) asked him to." — `sources/adventure-wdh.json:31965`. (Loyalty to the cell's Masters.)
- "Where he comes from-if he even has a home-remains a mystery, as does the question of where he might show up next." — `sources/adventure-wdh.json:31966`. (He keeps no home in public.)
- "Fala is friends with a member of the Zhentarim named Ziraj, who saved Fala's life. He visits Fala from time to time, and Fala has set aside a room for him on the second floor." — `sources/adventure-wdh.json:3432`. (A debt, and the one place he rests.)
- "Ziraj taught her the trail marks he leaves when he is wounded" — `campaign/setting/organizations/06-doom-raiders.md:37`. (Care for Yagra in a practical form.)
- "She and Ziraj the Hunter dated briefly" — `sources/Appendix_D_-_Running_the_Tavern.md:550` (Yagra's entry; the sentence is about her and him; see D7).
- "He did not tell Davil because Davil would have told him to stop." — `sources/Appendix_C_-_Player_Faction_Missions.md:656`. (A secret kill history, and a conflict with the adventure; do not state as fact without choosing the adventure's version.)
- "keep Fala Lefaliir safe, and remain unseen by the rest of the world" — `campaign/setting/notable-figures/doom-raiders/06-ziraj-the-hunter.md:15`. (His page's own wants.)
- "Killing Is a Favor: If Ziraj the Hunter sets out to kill someone, a friend in the cell asked him to, and if no one asked he would stop. He does not hunt for his own profit." — `campaign/setting/organizations/06-doom-raiders.md:42`. (A stated limit: no killing for profit.)
- "Ziraj will not kill for his own profit." — not in the sources as written; the org page's line 42 is the source ("He does not hunt for his own profit.").
- "He's the strong, silent type." — `sources/adventure-wdh.json:31965`. (Voice of the adventure; the profile's "Never" line also says "He never boasts, never explains a kill, and never raises his voice." — `.claude/skills/character-voices/voices/doom-raiders.md:108`.)
- "Rishaal the Page-Turner at the Book Wyrm noticed a very large, very quiet individual buy a candle, three strips of dried meat, and a thin blanket \"for cold nights\"" — `sources/Appendix_C_-_Player_Faction_Missions.md:642`. QUEST-TIME. Listed only as a warning: it shows a bare, careful life, but it is a clue in a mission.

---

## Cross-references (every other file where the topic appears)

Counts from Grep over `campaign/` (44 files, 254 lines). Non-quest lines are quoted or named. Quest-file lines are routed and given as counts above (E2).

Non-quest files and key lines:
- `campaign/setting/organizations/06-doom-raiders.md` (11 lines): lines 37, 42, 61, 64, 101 (quoted in A and B; line 64 is the back table and the Corellon's Crown sentence).
- `campaign/guides/factions/07-doom-raiders.md` (6): lines 16 and 59 (the Ardragon favor, "Ziraj the Hunter extends Davil's friends a favor: each Ardragon member can request it once per campaign, and one member's use does not spend another's. Ziraj neutralizes one named target, captured alive or quietly eliminated, and won't take assignments he considers suicidal."); lines 42, 45, 46 (Doom Raiders Renown, not Ziraj-specific). Factions Guide line 16 is quoted in A2.
- `campaign/setting/notable-figures/doom-raiders/01-davil-starsong.md` (2): not read in full.
- `campaign/setting/notable-figures/doom-raiders/02-yagra-stonefist.md` (2): not read in full. Yagra's page should be checked for the romance (D7).
- `campaign/setting/notable-figures/doom-raiders/04-skeemo-weirdbottle.md` (1): not read in full.
- `campaign/setting/notable-figures/trollskull-community/04-fala-lefaliir.md` (3): lines 21, 23, 25 (quoted in A3 and F5). Line 23: "They would die before betraying Ziraj's location to the Watch."
- `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md` (1): not read in full.
- `campaign/setting/history/04-the-founding-of-chains.md` (2): line 54 (quoted in A2).
- `campaign/setting/deities/corellon-larethian.md` (8), `campaign/setting/deities/gruumsh.md` (5; line 111 quoted in E1), `campaign/setting/deities/bhaal.md` (1), `campaign/setting/geography/city-of-the-dead.md` (2): not read in full.
- `campaign/setting/notable-figures/xanathars-guild/08-keln-trigos.md` (2), `campaign/setting/organizations/02-lords-alliance.md` (1): not read in full.
- `campaign/guides/trollskull-manor/08-notable-patrons.md` (1; line 30 quoted in D2).
- `campaign/guides/gm-guide/structural-rules.md` (1): not read in full.
- `campaign/gazetteer/waterdeep/north-ward.md` (1): not read in full.
- `campaign/structure/arc-b-trollskull-alley.md` (3), `arc-i-kolat-towers.md` (3), `arc-j-vault-of-dragons.md` (1): not read in full. Superseded or pending; routed.
- `sources/adventure-wdh.json`: lines 401 (list item, context not read), 1447, 1456, 3432 (Fala), 31925, 31961-31977 (Ziraj entry, page 201; quoted in A and B), 32972 (index).
- `sources/Appendix_B_-_Player_Factions.md`: line 275 (Lords' Alliance table row; quoted in E2).
- `sources/Appendix_C_-_Player_Faction_Missions.md`: lines 616-683 (the Rooftop Assassin mission; quoted in A4, A6, B, C, D1 and D3). Routed.
- `sources/Appendix_D_-_Running_the_Tavern.md`: lines 550 and 1271 (quoted in A3 and D2).
- `sources/research/pass5-bundles/doom-raiders/wiki.txt`: no hit (Grep).

Name collisions:
- "Ziraj" is unique. The Vayle and Thorne names do not collide with it.
- "Nessa Thorne" (Doom Raiders assassin, r25) and "Nessa Vayle" (Harper, twin of Corvin, Trollskull server candidate): `campaign/quests/faction-events/doom-raiders/r25-ardragon/ev-01-ardragon.md:137` ("Crew Two is the assassin Nessa Thorne (she/her) and the spies Garrick Pell and Bree Ostler."); `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58` ("| 5 | **Nessa & Corvin Vayle** | CN Illuskan human twins |"). The first name is shared; the surnames differ. The r25 Ardragon crew uses Nessa Thorne as a leader of a crew the cell deploys, not as a Harper.
- "Vael" stem: "Vaelle Lurval" (`sources/adventure-wdh.json:8317`, Cassalanter cult florist) and "Senna Vael" (Trollskull server candidate). Not a collision with Ziraj.

---

## Not found

- Searched for: Ziraj, "Ziraj the Hunter", "Master of Assassination" in `campaign/` (Grep, 254 lines in 44 files), `sources/adventure-wdh.json` (Grep), `sources/Appendix_B/C/D` (Grep), `sources/research/` (Grep; the pass5 doom-raiders wiki.txt has no Ziraj hit), and the wiki extract (NOT FOUND).
- Birth year, age, parents, origin, childhood name, home: no match in any source (F1).
- Faith or deity: no match (A6).
- Time in post: no match (A5).
- Wiki page: none (scratchpad extract "NOT FOUND"; `sources/research/pass5-bundles/doom-raiders/wiki.txt` no hit).
- Named woman he was paid to protect: no name in any source (F4).
- Name of the friend who asked for kills: the adventure names only the four Masters; no further name (`sources/adventure-wdh.json:31965`).
- How he joined the cell: no match (F3).
- How he rescued Fala: no match (F5).
- Stat block with a CR, AC or HP for Ziraj in the adventure: no match (`sources/adventure-wdh.json:31961-31977`). The stat block label is in D4.
- Alignment in the adventure: no match in `:31961-31977`.
- Appearance beyond half-orc and "hulking": no adventure match (F9).

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. `campaign/setting/organizations/06-doom-raiders.md:193` names "Davil and the Doom Raider Zhents + Elf Killer mission and more.docx" (not read; it may hold Ziraj material).
- `sources/3. Player Character Factions.pdf`: read as images (PDF pp.2-3). No Ziraj text on those pages.
- `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md` (66 Grep lines): Grep only; the file was not read in full. Its quotes here are Grep output.
