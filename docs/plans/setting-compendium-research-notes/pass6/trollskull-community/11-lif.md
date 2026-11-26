# Pass 6 research notes: Lif

Page: `campaign/setting/notable-figures/trollskull-community/11-lif.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 19; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Lif is a building spirit, not a person in the Trollskull staff roll. Day-one location: Trollskull Manor, North Ward, Trollskull Alley (see Ches 1 placement below).
Organization page: none. The trollskull-community group has no `campaign/setting/organizations/` page. Factions Guide: none. Villains page: none.
Voice profile: `.claude/skills/character-voices/voices/trollskull-community.md` lines 187 to 201 ("### Lif").
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/trollskull-community/01-talisolvanar-fellbranch.md`
Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-trollskull-community/11-lif.txt` (infobox and History; wiki prints no edition on most lines; citation key WDH5e-p31 is printed in the text). The Trollskull Manor wiki page is in the full dump `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/fandom-dump/forgottenrealms_pages_current.xml` (dump lines cited below).

## Method and caveats

- Campaign files: Grep and Read. Quotes copied from tool output. Lines marked "(Grep)" were quoted from a Grep result.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string with escapes removed. `{@creature ...}` tags left as written.
- Alexandrian Appendix D: `sources/Appendix_D_-_Running_the_Tavern.md` (markdown). Appendix C: `sources/Appendix_C_-_Player_Faction_Missions.md`.
- Alexandrian PDF: `sources/27. Addendum A Night in Trollskull Manor.pdf` read with the Read tool's `pages` parameter: PDF pages 1 to 3 (printed 178 to 180), 10 to 13 (printed 187 to 190), 15 to 18 (printed 192 to 195). The Lif quotes below come from PDF page 10 (printed 187) and are transcriptions from the image. **Each one must be checked with `pdftotext -layout` before it goes into prose.** Not read: PDF pages 4 to 9 (printed 181 to 186), page 14 (printed 191) and printed pages 196 onward. The Appendix D markdown has no Lif patron profile, so the PDF's Lif topics are not in the markdown.
- Not read: the two `.docx` files in `sources/Other remix files/` (see Not readable).
- `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **Species conflict inside the campaign.** The page says "Half-elf" (line 5). The adventure says "a half-elf named Lif" (`sources/adventure-wdh.json:3341`). The North Ward gazetteer says "a dwarf" (`campaign/gazetteer/waterdeep/north-ward.md:63`) and the Trollskull area overview says "a dwarf" (`campaign/locations/trollskull-manor/area-overview.md:41`). The m03 design notes already flag this (`campaign/quests/faction-events/bregan-daerthe/m03-three-nights/design-notes.md:44`). See D1.
2. **The stat block tag and the alignment do not match the wiki.** The page says "Stat block: **Specter**" and "unaligned" (line 5). The adventure tags the poltergeist as `{@creature specter}` (`sources/adventure-wdh.json:3341`) and gives no alignment. The wiki says "Chaotic evil" and "Poltergeist" (wiki line 57 and line 13). See D2 and D3.
3. **The death in the Persona is unsourced.** "he died holding a hag at bay on the last night of Fleetswake" (line 21) has no source. The adventure says only that he "couldn't abandon the place in death" (`sources/adventure-wdh.json:3341`). The hag in the sources belongs to a later owner's story (`sources/adventure-wdh.json:4135`). See D4 and F1.
4. **Several inner-life lines are campaign invention.** The cellar fixation, the portrait of a love interest and the urchins' kitchen arrangement have no source (see F and G). The only sourced inner-life hints are in the adventure (`:3341`), Appendix D (`:105`) and the PDF (printed 187, unverified).

---

## A. Background facts by theme

### A1. Who he was in life (origin, trade, death)

**Adventure, Spirit on Tap (page 31)**
> "The former tavern is haunted by the poltergeist ({@creature specter}) of the tavern's previous barkeeper, a half-elf named Lif. Maintaining the tavern was his life's work, and he couldn't abandon the place in death."
> — `sources/adventure-wdh.json:3341`

**Wiki, infobox (WDH5e-p31)**
> "| occupation     = Barkeeper (in life)" — wiki line 15
> "| race           = [[Poltergeist]]<br />{{Former}} [[Half-elf]]" — wiki line 13
> "| languages      = [[Common]], [[Elvish]] (couldn't speak)" — wiki line 18
> "| sex            = Male" — wiki line 12

**Wiki, History (WDH5e-p31)**
> "Lif was a [[half-elf]] barkeeper who even after his death couldn't abandon his old tavern on [[Trollskull Alley]] and tried to scare away all new owners." — wiki line 65
> "In {{Yearlink|1492}},{{Waterdeep-time}} [[Volothamp Geddarm]] acquired the place at a low price and later formally gave it to some adventurers whom he had hired to save [[Floon Blagmaar]]." — wiki line 65 (the same line)

**Wiki, Personality (WDH5e-p31)**
> "Lif's life was his work. If a new owner opened another tavern inside [[Trollskull Manor]], he could gradually become quite accommodating to them." — wiki line 68

**Wiki, Trollskull Manor page, History (refs WDH5e-p30-31; dump lines 5104660 and 5104662)**
> "The historic building was originally a tavern kept by the [[half-elf]] [[Lif]]." — dump line 5104660
> "Following Lif's death, Trollskull Manor fell into abandon. It was bought by [[Volothamp Geddarm]] sometime in the early 1490s [[DR]]. Volo intended to investigate the manor as part of research for his book ''[[Volo's Guide to Spirits and Specters]]''." — dump line 5104662

**Wiki, a list entry (dump line 4049607; the page title is not checked, edition not tagged)**
> "'''[[Lif]]''' was the [[half-elf]] bartender of [[Trollskull Manor]]. After his death, he became a [[specter]] and haunted his old tavern." — dump line 4049607

**Appendix D, Lif's Signature Drink (line 105)**
> "Lif invented this drink in life and has continued refining it in death." — `sources/Appendix_D_-_Running_the_Tavern.md:105`

**Appendix D, intro (since 1479 DR)**
> "Trollskull Tavern is more than a base of operations. It is the characters' home in Waterdeep — a place they have rebuilt with their own coin, their own labor, and (if they were wise) the reluctant blessing of a poltergeist bartender who has been waiting for new owners since 1479 DR. The systems in this appendix give that investment mechanical and narrative weight." — `sources/Appendix_D_-_Running_the_Tavern.md:10`

**North Ward gazetteer (campaign, the date and the "dwarf")**
> "- The tavern has been closed for years, and the poltergeist **Lif** haunts it. He is the spirit of the last barkeeper, a dwarf, and has minded the building alone since 1479 DR." — `campaign/gazetteer/waterdeep/north-ward.md:63`
> "- The poltergeist Lif has minded the building alone since 1479 DR." — `campaign/gazetteer/waterdeep/north-ward.md:199`

**Trollskull Manor location overview (campaign, the "dwarf")**
> "Lif is the poltergeist of the building's last barkeeper — a dwarf who tended the taproom from its last year of operation in 1479 DR until the current owners arrived. He manifests as moving objects, handwriting on dusty surfaces, and the occasional flung piece of glassware. He does not leave the building." — `campaign/locations/trollskull-manor/area-overview.md:41`

**Trollskull Manor guide (campaign, the date)**
> "Trollskull Tavern is the party's home in Waterdeep — rebuilt with their own coin, their own labor, and the uneasy blessing of a poltergeist bartender who has been waiting for new owners since 1479 DR. This guide gives that investment mechanical and narrative weight." — `campaign/guides/trollskull-manor/01-overview.md:5`

### A2. The building (the day-one owner and the place)

**Adventure, Volo's reward (page 31 and page 30)**
> "As a reward for rescuing Floon, Volo gives adventurers the deed to a building in the North Ward that looks out onto a wide cul-de-sac hemmed in by old residences and shops. The property used to be a tavern with a residence on the upper floors. The tavern has been closed for years, and the residence is haunted by a poltergeist that the characters can lay to rest." — `sources/adventure-wdh.json:485`
> "The tube contains a deed to Trollskull Manor, a historic building in the North Ward that the characters can claim as a home base. The deed has been notarized and appears legitimate (because it is). Volo recently bought the property because it is rumored to be haunted, and he was hoping that investigating it might yield a chapter for his next book, {@i Volo's Guide to Spirits and Specters}." — `sources/adventure-wdh.json:2962`

**Adventure, Tavern Rooms (page 31)**
> "When the characters first arrive, the tavern's taproom is filled with broken furniture, tarnished silverware, casks of wine that have turned to vinegar, and worthless detritus. The tavern's other rooms are all empty, except for cobwebs, dust, and harmless rats." — `sources/adventure-wdh.json:3332`

**North Ward gazetteer, Trollskull Alley and the Manor (campaign)**
> "- Trollskull Manor has had a string of owners. Ulkoria once owned the tavern and sold it to a family of shield dwarves, who fell on hard times and sold it to a woman who ran it as an orphanage. She turned out to be a hag who cooked and ate the children. Volo bought the building recently, hoping its haunting would give him a chapter for his next book." — `campaign/gazetteer/waterdeep/north-ward.md:198`

**Wiki, Trollskull Alley page (dump line 5103826; refs WDH5e-p31)**
> "* [[Trollskull Manor]], the largest building in the alley, had once been a tavern. By 1492 DR, it was abandoned and haunted by the [[poltergeist]] of [[Lif]], its former owner." — dump line 5103826

### A3. Habits, temperament and manner (adventure, wiki, Appendix D, PDF)

**Adventure, what Lif does (page 31)**
> "The poltergeist understands Common and Elvish, but it can't speak. It invisibly causes mischief at the expense of the new owners by smashing plates, breaking beer barrels, and so forth. If the characters don't take the hint, it writes not-so-subtle warnings (such as \"Closing time!\" and \"Last call!\") on dusty floors and grimy windows. To truly claim the tavern as their own, the characters must either appease the poltergeist or destroy it." — `sources/adventure-wdh.json:3342`

**Adventure, Appeasing Lif (page 31; this is an appeasement mechanic, so it is a quest-time behavior)**
> "If the characters work to repair and renovate the tavern with the goal of opening it to the public again, the poltergeist begins to accept them as the new owners and gradually becomes quite accommodating: pulling out a chair when a character wants to sit down, pouring a beer and delivering it to a character, taking coats when folks come in from the rain, and so forth. Once the business is up and running, Lif can also perform other helpful functions, such as locking doors, sweeping floors, and so forth." — `sources/adventure-wdh.json:3349`

**Adventure, Destroying Lif (page 31)**
> "Lif's poltergeist is destroyed if its hit points are reduced to 0. If attacked, it flees to the uppermost level of the turret when reduced to half its hit points. From there it fights to the bitter end." — `sources/adventure-wdh.json:3358`

**Appendix D, Lif the Bartender (line 101)**
> "If Lif (see Act II) has been appeased, he becomes the tavern's de facto bartender at no cost. He pours drinks with unsettling precision, keeps the bar spotless without instruction, and has memorized every regular's order after a single visit. He communicates through gesture, chalk on a small slate, and occasional atmospheric emphasis. He does not require wages, a bed, or meals — though he will occasionally leave a fresh drink at a specific table for a specific guest, with no explanation offered." — `sources/Appendix_D_-_Running_the_Tavern.md:101`

**Appendix D, Ulkoria's topic (line 1430; the patron is Ulkoria Stonemarrow, section at line 1419)**
> "4. Examines Lif. Watches him work for ten minutes without ordering anything. Then orders a single measure of whatever Lif considers his best and drinks it in silence. Leaves a large tip on the bar. This is, in Ulkoria's emotional vocabulary, an extraordinary endorsement." — `sources/Appendix_D_-_Running_the_Tavern.md:1430`

**Alexandrian PDF, Rishaal the Page-Turner topic (printed p.187, PDF page 10; transcription, check with pdftotext)**
> "If Lif has been pacified and is now part of the tavern's culture, Rishaal will stop by with a copy of *Richelle's Poems*, a book of elvish poetry which was once one of Lif's favorites." — `sources/27. Addendum A Night in Trollskull Manor.pdf`, PDF page 10 (printed 187)

**Alexandrian PDF, Hammond Kraddoc topic (printed p.187, PDF page 10; transcription, check with pdftotext)**
> "Discovers that Lif knew his father, Barbaros Kraddoc. Barbaros would actually stay at Trollskull Manor when he would come into Waterdeep to sell wines from the Elysium Fields. (Lif is saddened to learn that the Elysium Fields were destroyed.)" — `sources/27. Addendum A Night in Trollskull Manor.pdf`, PDF page 10 (printed 187)

**Voice profile (character-voices skill, lines 190 to 195)**
> "- **Sound:** He has no voice. He communicates in soot-written words on mirrors and windows, in thrown objects, and later in helpful gestures (a chair pulled out, a drink sliding across the bar)." — `.claude/skills/character-voices/voices/trollskull-community.md:190`
> "- **Personality in speech:** Territorial pride and loyalty. What he approves of goes neatly on the mirror. Anger is crockery. Grief is wordless: a cold draft, a portrait that stops smiling. His portrait behind the bar shows his judgement (flat, skeptical, a small smile)." — `.claude/skills/character-voices/voices/trollskull-community.md:194`
> "- **Quirks:** He underlines words he means. He straightens a crooked chair while the party is talking about him. A cup rattles when someone lies in the tavern." — `.claude/skills/character-voices/voices/trollskull-community.md:195`

### A4. Relationships to other named figures

**Appendix D, staff entry (line 588; the staff entry is not Lif's)**
> "**Wage:** 7 gp/tenday. He negotiated this himself, which took a while, because he was distracted by Lif halfway through." — `sources/Appendix_D_-_Running_the_Tavern.md:588`

**Appendix D, Perella Dunwhistle (line 129; staff relationship, applies only if appeased)**
> "**Mechanical Effect:** +3 to Revenue Roll per tenday. If Lif is also present, they develop a strange working rapport — Lif handles the ale side, Perella handles spirits, and the efficiency of this arrangement adds an additional +1 (total +4 with both)." — `sources/Appendix_D_-_Running_the_Tavern.md:129`

**Wiki, Nat, Jenks, Squiddly**: the three urchin wiki extracts do not name Lif (checked).

### A5. Time in post

- "since 1479 DR" appears in `campaign/gazetteer/waterdeep/north-ward.md:63`, `:199`, `campaign/locations/trollskull-manor/area-overview.md:41`, `campaign/guides/trollskull-manor/01-overview.md:5` and `sources/Appendix_D_-_Running_the_Tavern.md:10`. Only the Appendix D line and the campaign files give the year. The adventure gives no year. The wiki gives no year for Lif's death.
- Lif's death date is not in any source. The page's "last night of Fleetswake" is unsourced (see D4 and F1).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Page summary: "> - *Half-elf poltergeist, unaligned, he/him*. Stat block: **Specter**." — `campaign/setting/notable-figures/trollskull-community/11-lif.md:5`
- Adventure: no alignment is given for Lif. (Checked: `sources/adventure-wdh.json:3338` to `:3361`.)
- Appendix D: no alignment is given. (Checked: `sources/Appendix_D_-_Running_the_Tavern.md:99` to `:108`.)
- Wiki: "| alignment5e    = [[Chaotic evil]]" — wiki line 57.
- Result: the page's "unaligned" is campaign-only. The wiki says Chaotic evil. See D2.

**Species**
- Page summary: "*Half-elf poltergeist*" (`11-lif.md:5`).
- Adventure: "a half-elf named Lif" (`sources/adventure-wdh.json:3341`).
- Wiki: "| race           = [[Poltergeist]]<br />{{Former}} [[Half-elf]]" — wiki line 13.
- Campaign: "a dwarf" (`campaign/gazetteer/waterdeep/north-ward.md:63`; `campaign/locations/trollskull-manor/area-overview.md:41`). See D1.

**Pronouns**
- Page summary: "he/him" (`11-lif.md:5`).
- Adventure: "his life's work" (`sources/adventure-wdh.json:3341`).
- Wiki: "| sex            = Male" (wiki line 12).

**Stat block**
- Page summary: "Stat block: **Specter**." (`11-lif.md:5`).
- Adventure: "the poltergeist ({@creature specter})" (`sources/adventure-wdh.json:3341`). The adventure names the poltergeist with the specter tag, and never calls Lif a specter.
- Wiki: "| challenge5e    = 2" (wiki line 58); "| refs5e         = <ref name="WDH5e-p31" /><ref name="MM5e-p279">{{Cite book/Monster Manual 5th edition|279}}</ref>" (wiki line 60); class5e blank (wiki line 59).
- Wiki list entry: "After his death, he became a [[specter]]" (dump line 4049607).
- Voice profile: "*A poltergeist who speaks in soot on mirrors and flying crockery, possessive of the tavern and terrified for the cellar.*" (`.claude/skills/character-voices/voices/trollskull-community.md:188`).

---

## C. Quest-time sentences on the current page (routed; not day-one)

Current page: `campaign/setting/notable-figures/trollskull-community/11-lif.md`. Sections: Gamemaster's Summary, Roleplaying Information (Resonance, Emotions, Motivations, Inspirations), Character Information (Persona, Morale, Relationships), Overview.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L7 | "> - **Featured in:** **Trollskull Alley**, **Trollskull Manor**" | Quest list. Route. Misses the Bregan D'aerthe mission in which Lif is an ally | `campaign/quests/act-i/trollskull-alley/overview.md:26`; `campaign/quests/faction-events/bregan-daerthe/m03-three-nights/ev-01-three-nights.md:173` (heading "> [!gamemaster]**Lif's Help**") and `:119`; `sources/Appendix_C_-_Player_Faction_Missions.md:1538` |
| 2 | L11 | "**Resonance.** Lif should inspire sympathy ... and dread when the party realizes why he has been warning them away from the cellar this whole time." | The clause "when the party realizes" is quest-time phrasing. The rest is day-one roleplay text. Drafter restates or keeps it per ruling 3 | Warnings: `sources/adventure-wdh.json:3342` |
| 3 | L15 | "**Motivations.** Lif wants to see the tavern reopened, maintained to his standards, and protected ... He wants no one near the cellar, especially children, for reasons that predate anything he can still put into words." | "reopened" is a quest state. The cellar fixation has no source (see F4) | "reopened": `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:136` ("Lif Appeased"). Cellar: none (F4) |
| 4 | L21 | "His portrait behind the bar shifts with the party's standing: flat disapproval when they arrive, skeptical assessment as they work, a small smile once they have earned it." | Quest-time: the party's standing is the appeasement track. The portrait is not in any source (the voice profile and m03 mention a portrait) | Appeasement: `sources/adventure-wdh.json:3349`; `campaign/quests/act-i/trollskull-alley/ev-01-welcome-to-trollskull-alley.md:67`. Portrait: `campaign/quests/faction-events/bregan-daerthe/m03-three-nights/ev-01-three-nights.md:252` ("the portrait behind it has a small smile") |
| 5 | L21 | "To those who appease him, he pulls out chairs, delivers drinks, and locks up at night." | Quest-time (appeasement). Restate as a behavior, not as a state of the party | `sources/adventure-wdh.json:3349` |
| 6 | L21 | "Deep down, he died holding a hag at bay on the last night of Fleetswake, long enough for the patrons to escape." | Day-one history, but no source gives the death, the hag or the date. See D4 and F1 | Hag: `sources/adventure-wdh.json:4135`; `sources/Appendix_D_-_Running_the_Tavern.md:1428`. Death: `sources/adventure-wdh.json:3341` (no cause) |
| 7 | L25 | "**Relationships.** Lif is the permanent resident of Trollskull Manor, a spectral colleague of whatever bartender the party hires (his signature drink \"The Half-Elf\" adds +2 to Revenue Rolls)" | "the party hires" is tavern-time (after the opening). The drink line is Appendix D | Bartender: `sources/Appendix_D_-_Running_the_Tavern.md:101`; drink: `:105`; `campaign/guides/trollskull-manor/03-staff-and-hiring.md:26` |
| 8 | L25 | "... the silent guarantor of the urchins' kitchen arrangement in exchange for their staying away from the cellar hatch ..." | Tavern-time (after the opening) and unsourced in its terms ("guarantor", "in exchange"). The urchins' kitchen stay is a random event | `sources/Appendix_D_-_Running_the_Tavern.md:1184` (Event 18); `campaign/guides/trollskull-manor/07-events.md:36` |
| 9 | L25 | "A portrait of his love interest stands on an easel in the turret peak; no one living knows her name." | No source. Invented. Must be `[design]` if kept (F5) | none |
| 10 | L29 | "Lif is the poltergeist who has haunted Trollskull Manor since long before the party arrived" | Day-one in form ("since 1479 DR" is the sourced year). "the party arrived" is quest-time phrasing | `campaign/gazetteer/waterdeep/north-ward.md:199`; `sources/Appendix_D_-_Running_the_Tavern.md:10` |
| 11 | L29 | "... approachable to the right owners, but fixed on the cellar. ... and will work alongside the party if they earn his approval." | "the party ... earn his approval" is quest-time (appeasement). "fixed on the cellar" unsourced | `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:50` ("Lif (if appeased) — Mark **Lif Appeased** here.") |
| 12 | L23 | "**Morale.** In a fight, Lif hurls whatever is bolted down at anyone threatening the tavern or its patrons. At half hit points, he retreats to the turret." | Day-one behavior in form. "At half hit points ... turret" is sourced | `sources/adventure-wdh.json:3358` |
| 13 | L23 | "He cannot be reasoned with when someone is heading for the cellar." | Unsourced (cellar) | none (F4) |

### C2. Where Lif's quest-time facts already live (routed; do not restate on the day-one page)

- **Trollskull Alley, ev-01, the Lif section**: "The poltergeist of the building's last barkeeper makes himself known within ten minutes of the party's arrival. His escalation runs in three stages based on party behavior:" — `campaign/quests/act-i/trollskull-alley/ev-01-welcome-to-trollskull-alley.md:43`
- **ev-01, the acceptance track**: "If the party engages respectfully — cleaning up, asking questions aloud, demonstrating intent to restore the tavern as a public house — Lif de-escalates toward acceptance. The acceptance accumulates gradually across Scenes 1–5 as the renovation proceeds." — `ev-01-welcome-to-trollskull-alley.md:55`
- **ev-01, the destroy path**: "Destroying Lif requires reducing him to 0 hit points. Mark **Lif Destroyed**. His +2 Revenue bonus and the "free bartender" line in the **Trollskull Manor** guide's operating cost calculation are forfeited permanently." — `ev-01-welcome-to-trollskull-alley.md:63`
- **ev-01, the appeasement marker**: "**Lif Appeased** is marked at the Grand Opening (ev-06), not in this Event." — `ev-01-welcome-to-trollskull-alley.md:88`
- **ev-01, the day-one line (renovation) and the 1479 date**: "The party arrived at Trollskull Manor, assessed the building's state and the renovation cost, and made first contact with Lif — the poltergeist of its former bartender, who has been minding the place alone since 1479 DR and has opinions about what should happen next." — `ev-01-welcome-to-trollskull-alley.md:104`
- **ev-02, the inspector**: "The Order's inspector was dispatched because Rishaal filed a poltergeist notice during his own guild duties. He notices Lif within thirty seconds of entering the taproom." — `campaign/quests/act-i/trollskull-alley/ev-02-the-guild-gauntlet.md:48`
- **ev-06, the Grand Opening**: "**Lif** (if appeased) — Mark **Lif Appeased** here. He is behind the bar before anyone asks. Bar tools laid out. Chalk slate updated. He has decided." — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:50`
- **ev-06, outcome note**: "**Lif Appeased** — mark when Lif is behind the bar on opening night. He has extended professional courtesy to the new owners and has no intention of leaving. Read by the **Trollskull Manor** guide, whose full bartender mechanics apply from this point forward, and by **Fireball!** (Spirit Haunting)." — `ev-06-the-grand-opening.md:136`
- **ev-07, victim-style row (the "second death")**: "| Lif | ev-01 (if appeased) | His second death is the tavern's spirit dying with its neighborhood |" — `campaign/quests/act-i/trollskull-alley/ev-07-the-twin-parades.md:67`
- **Structural rules, the same row**: "| Lif | ev-01 (if appeased) | His second death is the manor's spirit going with the neighborhood |" — `campaign/guides/gm-guide/structural-rules.md:105`
- **Bregan D'aerthe, Three Nights, Lif's Help**: "If the party marked **Lif Appeased** in **Trollskull Alley**, Lif helps on the ground floor and the upper floors. At the start of each round, before any character acts, he produces the next effect from the list below, and the party spends no action on it." — `campaign/quests/faction-events/bregan-daerthe/m03-three-nights/ev-01-three-nights.md:119`. Its design note: "Lif does not manifest in the cellar, so this is the one fight where the party cannot lean on him" — `campaign/quests/faction-events/bregan-daerthe/m03-three-nights/design-notes.md:30`
- **Appendix C, Guarding Ott (quest-time, the faction mission)**: "The mission is a three-night siege of the party's home, using Trollskull Manor itself as the defensive terrain, with Lif as an involuntary ally." — `sources/Appendix_C_-_Player_Faction_Missions.md:1538`. Night Three: "Lif wakes you — if you are sleeping — by the simple method of making every glass in the building ring simultaneously at exactly the same pitch." — `sources/Appendix_C_-_Player_Faction_Missions.md:1578`. Aftermath: "Lif has done something he has never done before: he polished the bar while the party slept between the second and third nights." — `sources/Appendix_C_-_Player_Faction_Missions.md:1589`
- **Alexandrian Act III, Arc D (quest-time)**: "Act II ended with a mood: the characters had a home, a neighborhood, and people worth protecting. Lif poured drinks. The urchins knew their names. The guilds sent holiday greetings." — `sources/Act_III_Arc_D.md:13`
- **Trollskull Manor locations (the renovation state, campaign)**: "**Operational state.** Furnished and staffed. Bar tools in place (laid out by Lif before anyone asks)." — `campaign/locations/trollskull-manor/tm01-taproom.md:7`
- **Trollskull Manor, Lif's stage 3 retreat (quest)**: "**Resolution window.** When Lif retreats to the turret and the party follows without weapons drawn, appeasement becomes possible again" — `campaign/locations/trollskull-manor/tm06-turret.md:9`
- **Trollskull Manor guide, the bartender line (after opening)**: "If appeased during Act I, Lif tends bar for free." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:26`
- **Trollskull Manor guide, the Fame lines**: "| Lif caused a violent scene (unappeased) | −2 |" — `campaign/guides/trollskull-manor/04-fame.md:25`
- **Trollskull Alley overview, Lif's role**: "- **Lif** (Trollskull Manor) — the building's poltergeist bartender; resident obstacle turned cooperative staff member if appeased" — `campaign/quests/act-i/trollskull-alley/overview.md:26`
- **Fireball!**: the Lif Appeased outcome is read by Fireball! (ev-06:136 above). The flowchart says "Lif Appeased | ev-06 | the **Trollskull Manor** guide (bartender mechanics); Fireball (Spirit Haunting)" — `campaign/quests/act-i/trollskull-alley/flowchart.md:76`. Not checked: the Fireball! quest files for a Lif scene (see Not found).

---

## D. Conflicts

**D1. Species (half-elf or dwarf)**
- Adventure: "a half-elf named Lif" (`sources/adventure-wdh.json:3341`)
- Wiki: "The historic building was originally a tavern kept by the [[half-elf]] [[Lif]]." (dump line 5104660); "| race           = [[Poltergeist]]<br />{{Former}} [[Half-elf]]" (wiki line 13)
- Page: "*Half-elf poltergeist, unaligned, he/him*" (`11-lif.md:5`)
- Campaign, gazetteer: "He is the spirit of the last barkeeper, a dwarf, and has minded the building alone since 1479 DR." (`campaign/gazetteer/waterdeep/north-ward.md:63`)
- Campaign, location overview: "Lif is the poltergeist of the building's last barkeeper — a dwarf who tended the taproom ..." (`campaign/locations/trollskull-manor/area-overview.md:41`)
- The campaign's own note: "The Trollskull Manor area overview (`area-overview.md`, around line 41) says Lif was a dwarf, and his Notable Figures page says half-elf." (`campaign/quests/faction-events/bregan-daerthe/m03-three-nights/design-notes.md:44`)
- Higher ranked: the published adventure, and the wiki agrees with it. The gazetteer and the area overview are campaign files and rank above the adventure in the project order, but they conflict with the page and with each other's history. The choice is the orchestrator's. Drafter writes nothing about ancestry until the choice is made.

**D2. Alignment**
- Page: "unaligned" (`11-lif.md:5`)
- Wiki: "| alignment5e    = [[Chaotic evil]]" (wiki line 57)
- Adventure: silent. Appendix D: silent.
- Result: only the wiki (lowest rank) gives an alignment. The page's "unaligned" is a campaign decision, not a conflict with a higher source. Flagged for the orchestrator.

**D3. Stat block tag**
- Page: "Stat block: **Specter**." (`11-lif.md:5`)
- Adventure: "the poltergeist ({@creature specter})" (`sources/adventure-wdh.json:3341`) and "Lif's poltergeist is destroyed if its hit points are reduced to 0." (`:3358`)
- Wiki: "| challenge5e    = 2" (wiki line 58) and the MM5e-p279 cite (wiki line 60)
- Wiki list entry: "After his death, he became a [[specter]]" (dump line 4049607)
- Higher ranked: the adventure. Its tag is a specter stat block, so the page's "Specter" matches the adventure's tag. The wiki's CR 2 and its MM cite do not name a stat block.

**D4. The death and the hag**
- Page: "Deep down, he died holding a hag at bay on the last night of Fleetswake, long enough for the patrons to escape." (`11-lif.md:21`)
- Adventure: "Maintaining the tavern was his life's work, and he couldn't abandon the place in death." (`sources/adventure-wdh.json:3341`) — no cause, no date, no hag.
- Adventure hag: "\"Turned out to be a hag who was cooking and eating the children,\" Ulkoria recalls." (`sources/adventure-wdh.json:4135`) — the orphanage owner, reached after the shield dwarves sold the building.
- Appendix D: "She means the hag. She will not elaborate on the hag." (`sources/Appendix_D_-_Running_the_Tavern.md:1428`)
- Result: the page's death is unsourced, and the hag is the campaign's. The sources do not connect Lif's death to the hag.

**D5. Ownership before the party**
- Adventure: "Volo recently bought the property because it is rumored to be haunted" (`sources/adventure-wdh.json:2962`)
- Wiki: "Following Lif's death, Trollskull Manor fell into abandon. It was bought by [[Volothamp Geddarm]] sometime in the early 1490s [[DR]]." (dump line 5104662); and wiki line 65 "In {{Yearlink|1492}},... [[Volothamp Geddarm]] acquired the place at a low price"
- Campaign: "Volo bought the building recently, hoping its haunting would give him a chapter for his next book." (`campaign/gazetteer/waterdeep/north-ward.md:198`)
- Not a conflict with Lif's page, but the wiki's date for Volo's purchase differs: 1492 (wiki line 65) and "early 1490s" (dump line 5104662). The adventure gives no date.

**D6. Featured-in list**
- Page: "**Featured in:** **Trollskull Alley**, **Trollskull Manor**" (`11-lif.md:7`).
- Also featured, per Grep: `campaign/quests/faction-events/bregan-daerthe/m03-three-nights/` and `sources/Appendix_C_-_Player_Faction_Missions.md:1538`. Not a conflict; a list that omits a quest.

---

## E. Stale lines in other files (not edited) and routed quest references

- `campaign/setting/deities/baba-yaga.md:154`: "The campaign repeats the hag in `campaign/guides/trollskull-manor/08-notable-patrons.md:99`, `campaign/setting/notable-figures/trollskull-community/08-broxley-fairkettle.md:26` and `campaign/setting/notable-figures/trollskull-community/11-lif.md:22`." **Stale line numbers.** On the current files, the Broxley hag line is at `08-broxley-fairkettle.md:25`, and the Lif page has no hag line at line 22 (line 21 is Persona, which carries the hag). Not edited.
- `campaign/quests/faction-events/bregan-daerthe/m03-three-nights/design-notes.md:44`: correct on today's files.
- `campaign/quests/faction-events/bregan-daerthe/m03-three-nights/overview.md:52`: "**Lif** (Trollskull Alley community): the poltergeist of the manor, who helps on every floor above the cellar if the party has treated the building well." Routed.
- `campaign/guides/gm-guide/structural-rules.md:105` and `ev-07-the-twin-parades.md:67`: "His second death" (see C2). Implies a first death that no source dates. Routed; not edited.
- `campaign/gazetteer/waterdeep/north-ward.md:226`: cross-reference only.
- `campaign/guides/trollskull-manor/03-staff-and-hiring.md:24`: "### Lif the Poltergeist Bartender" (guide heading, post-opening).

**Routed quest references**: Trollskull Alley ev-01, ev-02, ev-06, ev-07, overview, flowchart (`campaign/quests/act-i/trollskull-alley/`); Bregan D'aerthe m03 Three Nights ev-01 and design notes (`campaign/quests/faction-events/bregan-daerthe/m03-three-nights/`); Appendix C `:1538`, `:1569`, `:1578`, `:1589`; Act III Arc D `:13`.

---

## F. Gaps a Background would need that no source gives

1. **Death.** No source gives the cause, the date or the place of Lif's death. Sourced: "he couldn't abandon the place in death" (`sources/adventure-wdh.json:3341`); "After his death, he became a [[specter]] and haunted his old tavern." (dump line 4049607). The page's "last night of Fleetswake" and "a hag at bay" must be `[design]` if kept.
2. **Birth, family, age, and how he got the tavern.** No source. The wiki gives no age, dob, parents or siblings (wiki lines 16, 21, 29, 31). Sourced only: "the tavern's previous barkeeper, a half-elf named Lif" (`sources/adventure-wdh.json:3341`).
3. **The 1479 DR start.** The year "1479 DR" for the last year of tavern operation is in Appendix D (`:10`) and the campaign files (see A5). No source gives the start of his time as barkeeper. The area overview says "from its last year of operation in 1479 DR until the current owners arrived" (`campaign/locations/trollskull-manor/area-overview.md:41`).
4. **The cellar.** No source gives a cellar fixation. The adventure says only: "it writes not-so-subtle warnings (such as \"Closing time!\" and \"Last call!\") on dusty floors and grimy windows" (`sources/adventure-wdh.json:3342`). The cellar is in the campaign only: "Lif does not manifest here. The cellar is below Lif's area of effect." (`campaign/locations/trollskull-manor/tm03-cellar.md:11`). The page's Motivations line about the cellar is campaign-invented; list as `[design]` if kept.
5. **A love interest.** No source. The page's "A portrait of his love interest ... no one living knows her name" (line 25) is invented. Must be `[design]` if kept, and the drafter may not name her (ruling 17: a named new figure is not allowed).
6. **The urchins' kitchen arrangement.** No source. Only the random event: "The Three Urchins (Nat, Jenks, and Squiddly) have somehow gotten into the tavern after hours and are sleeping in the kitchen." (`sources/Appendix_D_-_Running_the_Tavern.md:1184`). The "silent guarantor" line is invented.
7. **Faith.** No source. Do not give him a deity.
8. **Surviving relationships.** Sourced only through the PDF (see G): Rishaal's *Richelle's Poems* (printed 187) and Kraddoc's father Barbaros (printed 187). Both need pdftotext before use.

---

## G. Inner-life hints in the sources (exact quotes)

These are the sourced hints a Background and the personal goals may use. They must not be contradicted.

- **Work as a calling.** "Maintaining the tavern was his life's work, and he couldn't abandon the place in death." — `sources/adventure-wdh.json:3341`; wiki: "Lif's life was his work." (wiki line 68).
- **Pride in a signature drink.** "Lif invented this drink in life and has continued refining it in death." — `sources/Appendix_D_-_Running_the_Tavern.md:105`.
- **A favorite book.** "a book of elvish poetry which was once one of Lif's favorites" — PDF printed 187 (transcription, check with pdftotext).
- **A lost friend or family.** "Lif knew his father, Barbaros Kraddoc ... (Lif is saddened to learn that the Elysium Fields were destroyed.)" — PDF printed 187 (transcription, check with pdftotext).
- **Attention from a regular.** "Examines Lif. Watches him work for ten minutes without ordering anything." — `sources/Appendix_D_-_Running_the_Tavern.md:1430`.
- **Grief in the voice profile.** "Grief is wordless: a cold draft, a portrait that stops smiling." — `.claude/skills/character-voices/voices/trollskull-community.md:194`. (Voice, not source.)
- **Not leaving.** "He has decided." (`campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:50`) and "has no intention of leaving" (`ev-06-the-grand-opening.md:136`). Both are campaign quest text.
- **Territory.** "The taproom is Lif's primary area of manifestation." (`campaign/locations/trollskull-manor/tm01-taproom.md:9`) (campaign).
- **Warnings.** "it writes not-so-subtle warnings (such as \"Closing time!\" and \"Last call!\")" (`sources/adventure-wdh.json:3342`).
- **Hag history.** The hag story is told by Ulkoria, not by Lif (`sources/adventure-wdh.json:4135`). Do not attach it to Lif without a `[design]` tag.

---

## Ches 1 placement (what the campaign places, day one)

- **Building**: Trollskull Manor, "a building in the North Ward that looks out onto a wide cul-de-sac" (`sources/adventure-wdh.json:485`).
- **Street**: Trollskull Alley. "* [[Trollskull Manor]], the largest building in the alley, had once been a tavern. By 1492 DR, it was abandoned and haunted by the [[poltergeist]] of [[Lif]], its former owner." (dump line 5103826, wiki)
- **Ward**: North Ward. "The tavern has been closed for years, and the poltergeist **Lif** haunts it." (`campaign/gazetteer/waterdeep/north-ward.md:63`)
- **Room**: the taproom is his "primary area of manifestation" (`campaign/locations/trollskull-manor/tm01-taproom.md:9`), and the turret is his retreat (`tm06-turret.md:5`). Both are campaign room placements; the adventure gives the turret only (`sources/adventure-wdh.json:3358`).
- **Owner on Ches 1**: no owner is named on Ches 1. Volo "recently bought the property" (`sources/adventure-wdh.json:2962`). The Volo deed is a Floon-quest reward (`sources/adventure-wdh.json:485`).

---

## Not found

- **Lif's alignment** in the adventure, Appendix D, the PDF pages read, Appendix B and C, and the guides. Searched for "alignment", "Lif" and "unaligned".
- **Lif's death, cause and date** in the adventure (searched for "died", "death", "Lif.{0,80}(die|death)"), the wiki extracts, the Appendix D markdown and the PDF pages read.
- **The cellar fixation** in the adventure (searched for "cellar" across the file; the Trollskull passages around `:3300` to `:3420` name no cellar for Lif) and Appendix D (searched for "cellar"). Only the campaign mentions it.
- **A love interest or a portrait of her** in the adventure, Appendix D, Appendix C and the PDF pages read (searched for "portrait", "love", "easel").
- **The urchins' kitchen arrangement** beyond Event 18 (see G and F6).
- **Appendix B** (Player Factions): grep for "Lif", "poltergeist" and "urchin" returned no match in `sources/Appendix_B_-_Player_Factions.md`.
- **Fireball! quest files**: not searched for a Lif scene. Only the flowchart and the ev-06 outcome note name Lif for Fireball!.

## Not readable

- `sources/Other remix files/Lif and the Haunting of Trollskull Manor.docx`: named by `sources/SOURCE_GUIDE.md:691` as "Lif the poltergeist — history, personality, appeasement mechanics, tavern integration". Not readable with the tools. The docx is likely the most complete source for Lif's history and must be extracted before the Background is final.
- `sources/Other remix files/The 3 Urchins NPC Guide.docx`: named by `sources/SOURCE_GUIDE.md:694` (for Nat, Squiddly and Jenks). Not readable. See the three urchin notes.
- PDF `sources/27. Addendum A Night in Trollskull Manor.pdf`: printed pages 181 to 186, 191 and 196 onward were not read. Lif's Event entries (Appendix D `:1176` onward) were not checked against the PDF's event table.
