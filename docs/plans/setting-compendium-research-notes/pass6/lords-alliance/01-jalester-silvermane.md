# Pass 6 research notes: Jalester Silvermane

Page: `campaign/setting/notable-figures/lords-alliance/01-jalester-silvermane.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Jalester is a major NPC (brief ruling 2): full Personality and Connections apply.
Organization page: `campaign/setting/organizations/02-lords-alliance.md`
Factions Guide: `campaign/guides/factions/03-lords-alliance.md`
Voice profile: `.claude/skills/character-voices/voices/lords-alliance.md` (### Jalester Silvermane, lines 5-19)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes are shown as plain quotes. `{@creature ...}` tags are left as written. The `page` field is given where the entry has one.
- Wiki: the scratchpad extract `wiki-lords-alliance/01-jalester-silvermane.txt` is the Jalester page. It is cited as "wiki line N" (that file's lines). The wiki prints no edition on most sentences; the `ref` names are quoted where they appear.
- Wiki, Watch captain claim: `sources/research/pass5-bundles/city-watch/wiki.txt` line 101 (the same line is in `sources/research/pass3-bundles/city-watch/wiki.txt:101`).
- Alexandrian PDF: `sources/3. Player Character Factions.pdf` was read as a rendered page image (PDF p.3 = printed p.25). The quote is a transcription from the image. Check with `pdftotext -layout` before any quote goes into prose.
- Alexandrian Appendices B and D are markdown and quoted from the file.
- No shell was available. `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **Faerrel's death has three versions in the sources.** The published adventure says he was "killed in a street fight last year" (`adventure-wdh.json:1537`) and "killed while helping bring the perpetrators to justice" (`:32160`). The page's Persona says he "died exposing a plot against the government." The organization page settled on the Persona version and on "last year" (see D1).
2. **The stat block label "Spy" has no source except the campaign.** The page says "Stat block: **Spy**." The Alexandrian Appendix D says "Veteran", the published adventure says "fighter", and the wiki says Fighter 11 with CR 4 (see B and D2).
3. **The voice profile has a quest-time greeting.** Sample line 17 says "You were at the Gralhund villa on the night in question, weren't you?" It must be restated or removed (C, row V-1).
4. **The Watch rank conflicts.** The Dungeon of the Mad Mage text and the wiki call Jalester a captain of the City Watch. Dragon Heist calls him an agent. `city-watch.md:128` follows Dragon Heist and the Notable Figures page (see D6).
5. **"cannot bear to delegate" (page line 29) has no source in any file searched** (see C, row P-11).

---

## A. Background facts by theme

### A1. Origin, birthplace, age

**Adventure, Jalester Silvermane entry (page 205)**
> "An earnest man in his mid-twenties, {@creature Jalester Silvermane|wdh|Jalester} hails from the distant land of Cormyr, where he earned his spurs working for a mercenary company called the Steel Shadows. A few years ago, Jalester left the Dales and traveled to Waterdeep with several other members of the company, one of whom-Faerrel Dunblade-would become his best friend and lover."
> — `sources/adventure-wdh.json:32159` (entry "Jalester Silvermane", page 205)

**Wiki, History (ref `DM`, the novel *Death Masks*; no edition)**
> "Jalester was born in [[Cormyr]] and for a time he worked for the [[Steel Shadows]] mercenary company until some years before he and several members of the group left the [[Dales]] and settled in Waterdeep. There, he fell in love with his fellow mercenary Faerrel.<ref name="DM">{{Cite book/Death Masks}}</ref>"
> — wiki line 77

**Wiki, infobox age (ref `WDH5e-p205`, 5e)**
> "| age            = Mid‒20s in [[1492 DR]]<ref name="WDH5e-p205" />{{Waterdeep-time}}"
> — wiki line 17

No source gives a birth year, parents, siblings, children or a home town. The wiki infobox fields `dob` (line 21), `parents` (line 29) and `siblings` (line 31) are blank.

### A2. The Steel Shadows, Faerrel, and recruitment by Laeral

**Adventure, Jalester entry (page 205)**
> "The wizard Elminster befriended the two young men and brought them to the attention of {@creature Laeral Silverhand|WDH}, who put them to work as deputies and spies. Jalester and Faerrel helped the Open Lord expose a plot to overthrow the government, but Faerrel was killed while helping bring the perpetrators to justice. Jalester remained in Waterdeep afterward, becoming one of Laeral's field operatives in the service of Waterdeep and the Lords' Alliance. He has been romantically unattached ever since Faerrel's death but longs again for love."
> — `sources/adventure-wdh.json:32160` (entry "Jalester Silvermane", page 205)

**Wiki, History (ref `DM`, novel; the year is the wiki's)**
> "In [[1491 DR]], Elminster met and befriended the two young mercenaries and presented them to the Open Lord Laeral. Under the Lord's orders, Jalester and Faerrel unveiled a [[Death Masks|sinister plot]] but Faerrel was killed.<ref name="DM"/>"
> — wiki line 79

**Wiki, Watch and Laeral (ref `WDH5e-p205`)**
> "In [[1492 DR]], Jalester was one of Laeral's main field operatives.<ref name="WDH5e-p205" />"
> — wiki line 81

**Campaign, Lords' Alliance organization page, Draft Notes (the settled date)**
> "**Last year, about 1491 DR, Faerrel Dunblade.** Faerrel was a former mercenary of the Steel Shadows whom Laeral had put to work beside Jalester as deputies and spies, and he died while exposing a plot against the government. Jalester stayed in Waterdeep as one of the Open Lord's field operatives (**Jalester Silvermane**; *Dragon Heist*, 5e, for the recruitment and the plot; the Trollskull Manor guide for "last year"). Design: the published adventure gives no date for the death, and the campaign places it last year."
> — `campaign/setting/organizations/02-lords-alliance.md:28`

### A3. The badge of the Watch and the Open Lord

**Adventure, Treasure subentry (page 205)**
> "Jalester carries a {@item badge of the Watch|WDH} (+2 bonus to AC if not using a shield). If the badge is lost or taken from him, it returns to {@creature Laeral Silverhand|WDH}."
> — `sources/adventure-wdh.json:32167`

**Campaign, City Watch, Badge of the Watch (wiki and adventure)**
> "- **Badge of the Watch (wiki):** The wiki, citing Dragon Heist, says an officer who reaches captain may be given a badge of the Watch. The badge adds protection against attacks and tells the Open Lord where the wearer is, and only the Open Lord can award one. The published adventure gives a badge to Jalester Silvermane and says it returns to Laeral if he loses it."
> — `campaign/setting/governance-and-guilds/city-watch.md:38`

**Campaign, Lords' Alliance organization page, GM Notes**
> "- **Jalester:** He carries a badge of the City Watch and reads the Watch's file ledger each tenday. He is grieving his partner, Faerrel Dunblade, who died last year exposing a plot against the government, and he fills the silence with work."
> — `campaign/setting/organizations/02-lords-alliance.md:118`

**Appendix B, the First Meeting readaloud (Alexandrian)**
> "There is a City Watch badge on his belt, worn casually enough that you might miss it."
> — `sources/Appendix_B_-_Player_Factions.md:213`

### A4. Daily life and the corner table

**Adventure, Yawning Portal NPC list (page 20)**
> "{@creature Jalester Silvermane|WDH} (see {@adventure appendix B|WDH|12}) is an agent of the Lords' Alliance who reports directly to {@creature Laeral Silverhand|WDH}. The Open Lord of Waterdeep has asked him to spy on adventurers who might, through their actions, aid or imperil the city and its citizens. Since the Yawning Portal attracts adventurers of all sorts, Jalester spends a lot of time here, usually seated by himself in a quiet corner. {@creature Durnan|WDH} knows that Jalester works for Laeral and leaves the young man alone."
> — `sources/adventure-wdh.json:1536` (entry "Jalester Silvermane", page 20)

**Adventure, Lords' Alliance faction entry (page 38)**
> "The characters' primary contact is {@creature Jalester Silvermane|WDH} (see {@adventure appendix B|WDH|12}), a field agent who reports to Open Lord {@creature Laeral Silverhand|WDH}. Jalester spends much of his time in the Yawning Portal and other taverns that adventurers are known to frequent."
> — `sources/adventure-wdh.json:3895`

**Campaign, Lords' Alliance organization page, Structure**
> "Its members are contacted in person, at the corner table beside the well at the Yawning Portal. Jalester takes that table most evenings, and anyone at the Portal's bar can point to it."
> — `campaign/setting/organizations/02-lords-alliance.md:55`

**Wiki, Activities (ref `WDH5e-p37`)**
> "Jalester spent much of his time in the [[Yawning Portal]] and other taverns that adventurers were known to frequent.<ref name="WDH5e-p37">{{Cite book/Waterdeep: Dragon Heist|37}}</ref>"
> — wiki line 71

### A5. Relationships to named figures

**Laeral Silverhand (direct orders), Durnan, Elminster and Mirt**
> "Jalester was an agent under the direct orders of [[Open Lord]] [[Laeral Silverhand]], who ordered him to monitor the adventurers of the city. [[Durnan]] knew about his master and left Jalester alone.<ref name="WDH5e-p20">{{Cite book/Waterdeep: Dragon Heist|20}}</ref> He was also friends with [[Elminster]]<ref name="WDH5e-p205" /> and [[Mirt]].<ref name="WDMM5e-p9" />"
> — wiki line 74

**Sevel Dastar (campaign only; no Notable Figures page)**
> "- **Sevel Dastar** — A middle-aged Chondathan human in a plain brown coat who works for the Alliance as a spy."
> — `campaign/setting/organizations/02-lords-alliance.md:103`

**Davil Starsong's cell (the Splinter line)**
> "Alliance speakers say \"the Splinter\" or \"the other cell\" until **Manshoon Named** is marked for the listener. Jalester also separates the Splinter from Davil Starsong's cell, with the words \"not Davil's people\". They say \"the carnival fleet\" until **Jarlaxle Unmasked** is marked."
> — `campaign/guides/factions/03-lords-alliance.md:13`

**Xanathar's lair (Jalester does not know where it is)**
> "Characters who are members of the Lords' Alliance can reach out to {@creature Jalester Silvermane|WDH} (see {@adventure appendix B|WDH|12}). Jalester doesn't know the location of {@creature Xanathar|WDH}'s lair but can get the details from {@creature Laeral Silverhand|WDH}."
> — `sources/adventure-wdh.json:15170` (quest-time context; the campaign's day-one reading is at `02-lords-alliance.md:91`)

**Campaign, Organization page, Relationships (Xanathar's Guild)**
> "- **Xanathar's Guild** (enemy): The Guild is the largest criminal organization in Waterdeep and rules from a lair below the city, and the Alliance exists to watch for threats to the city's stability (**Xanathar's Guild**). Jalester does not know where the lair is and would have to ask Laeral (*Dragon Heist*, 5e). No source states an Alliance policy toward the Guild, so the stance follows from the Alliance's remit. `[research]`"
> — `campaign/setting/organizations/02-lords-alliance.md:91`

**Durnan (Yawning Portal)**: the adventure line at `:1536` (A4) is the only source for the Durnan tie.

**Darvish and Bram (Trollskull Manor staff)**
> "**Faction Note:** Formally retired City Watch. Lords' Alliance characters who know Jalester Silvermane will find that Darvish and Jalester have a professional acquaintance; Jalester will speak well of him if asked directly."
> — `sources/Appendix_D_-_Running_the_Tavern.md:279`

> "**Faction Note:** Retired Watch, informal Lords' Alliance adjacent. Characters with Lords' Alliance affiliation find that Jalester Silvermane knows Bram — not well, but respectfully. Jalester will say only that Bram is \"reliable in the narrow sense.\""
> — `sources/Appendix_D_-_Running_the_Tavern.md:569`

### A6. Information work and the Watch ledger

> "**Information.** Its intelligence comes from Jalester's field reports and the Watch's contacts, and it runs about three moves behind the factions (**A City Watching Itself**). Laeral's own spies keep watch on the adventurers in the city, and she rewards those who put Waterdeep ahead of themselves (*Dragon Heist*, 5e). Jalester reads the Watch's file ledger each tenday (**The City Watch**)."
> — `campaign/setting/organizations/02-lords-alliance.md:69`

> "**Jalester Silvermane** (Lawful Good, Chondathan Human, he/him) is a Lords' Alliance field agent who reports to Laeral and carries a badge of the Watch. He reads the Watch's file ledger each tenday, and his briefings in the **Cassalanter Villa** and **Kolat Towers** structure documents cover Watch patrol schedules and Watch coverage."
> — `campaign/setting/governance-and-guilds/city-watch.md:65`

### A7. Faith

No source gives Jalester a faith. The wiki infobox field `patron deity` is blank (wiki line 18). The adventure entry, the Appendix B and D entries, the Notable Figures page and the Trollskull guide say nothing about a god. `[research]` (a gap; the drafter should leave it blank or invent with a `[design]` tag).

### A8. Current post (how long in post)

> "Jalester remained in Waterdeep afterward, becoming one of Laeral's field operatives in the service of Waterdeep and the Lords' Alliance."
> — `sources/adventure-wdh.json:32160`

> "In [[1492 DR]], Jalester was one of Laeral's main field operatives.<ref name="WDH5e-p205" />"
> — wiki line 81

No source gives the year he took the post. The organization page's Draft Notes say the death was "last year" (`02-lords-alliance.md:28`).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Notable Figures page, Summary: "> - *Chondathan human spy, lawful good, he/him*. Stat block: **Spy**." — `campaign/setting/notable-figures/lords-alliance/01-jalester-silvermane.md:5`
- Adventure: "{@i LG male Chondathan human fighter}" — `sources/adventure-wdh.json:1535` (Yawning Portal NPC list, page 20)
- City Watch page: "**Jalester Silvermane** (Lawful Good, Chondathan Human, he/him)" — `campaign/setting/governance-and-guilds/city-watch.md:65`
- Trollskull guide: "**Jalester Silvermane** *(Lords' Alliance, LG male Chondathan Human, Spy; see **The Lords' Alliance** organization page)*" — `campaign/guides/trollskull-manor/08-notable-patrons.md:107`
- Wiki: "| alignment5e    = [[Lawful good]]" — wiki line 57
- Alexandrian Appendix D (conflict, see D3): "*Lords' Alliance — N male Cormyrean human, Veteran*" — `sources/Appendix_D_-_Running_the_Tavern.md:1435`
- Appendix B: no alignment line in the Contact entry (`sources/Appendix_B_-_Player_Factions.md:185`).

**Species and ethnicity**
- Notable Figures page: "*Chondathan human spy, lawful good, he/him*" — line 5.
- Adventure: "{@i LG male Chondathan human fighter}" — `sources/adventure-wdh.json:1535`. Appendix B gives only "A no-nonsense human field agent" (`sources/Appendix_B_-_Player_Factions.md:185`).
- Wiki: "| race           = [[Human]]<ref name="WDH5e-p20" />" (line 14) and "| ethnicity      = [[Chondathan]]<ref name="WDH5e-p20" />" (line 15).
- Alexandrian Appendix D: "*Lords' Alliance — N male Cormyrean human, Veteran*" (`sources/Appendix_D_-_Running_the_Tavern.md:1435`). "Cormyrean" names the homeland, not the ethnicity (brief ruling 5).

**Pronouns**
- Notable Figures page: "he/him" (line 5).
- Adventure: "Jalester is often distracted by thoughts of Faerrel Dunblade, his boyfriend" — `sources/adventure-wdh.json:1537`.
- Wiki: "| sex            = Male<ref name="WDH5e-p20" />" (line 13).
- Campaign: "**Jalester Silvermane** (Lawful Good, Chondathan Human, he/him)" (`city-watch.md:65`).

**Stat block**
- Notable Figures page: "Stat block: **Spy**." (line 5). The Trollskull guide says "Spy" (`08-notable-patrons.md:107`). No stat-block source for Spy was found: the adventure gives no stat block for Jalester (the Jalester entry is `sources/adventure-wdh.json:32155` to `:32171`; its only mechanical line is the badge at `:32167`).
- Alexandrian Appendix D: "Veteran" (`sources/Appendix_D_-_Running_the_Tavern.md:1435`).
- Wiki: "| challenge5e    = 4" (line 58) and "| class5e        = {{Class table|edition=5e|[[Fighter]]|11}}" (line 59); refs `WDH5e-p205`, `WDH5e-p20`, `PHB5e-p72` (line 60). The wiki gives a class level and a CR, not a stat block.
- `docs/plans/lords-alliance-mechanics-reference.md` names Jalester at lines 39, 127, 136, 310, 382 and 424 but gives no stat line.

**Age**
- Adventure: "An earnest man in his mid-twenties" (`sources/adventure-wdh.json:32159`). Wiki: "Mid‒20s in [[1492 DR]]" (line 17). Appendix B (conflict D5): "A middle-aged man in a plain dark doublet sits alone at a corner table with a tankard he has not touched." (`sources/Appendix_B_-_Player_Factions.md:210`)

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/lords-alliance/01-jalester-silvermane.md`. The page has no Background, Personality or Connections section yet. Each row says where the fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| P-1 | L5 | "> - *Chondathan human spy, lawful good, he/him*. Stat block: **Spy**." | Day-one name tag; the stat label is unsourced (B) | section B |
| P-2 | L6 | "> - **Affiliation:** Lords' Alliance" | Day-one; matches the organization page | `campaign/setting/organizations/02-lords-alliance.md:101` |
| P-3 | L7 | "> - **Featured in:** **Trollskull Alley**, **Fireball!**, **Gralhund Villa**, **Faction Outposts**, **Xanathar's Lair**, **Cassalanter Villa**, **Sea Maidens Faire**, **Kolat Towers**, **Vault of Dragons**, **Lords' Alliance First Meeting**, **The Long Watch**, **The Exile's Return**, **The Red Wizard's Price**, **The Archer Above**, **Fentree's Ledger**, **An Audience with the Open Lord**, **Suspension and Dismissal**, **Escalation to the Open Lord**, **Redknife**, **Stingblade**, **Warduke**, **Lioncrown**, **The Sleeping Asset**, **The Stone's Other Master**, **The Doppelganger Problem**, **Force Grey Mission 5 — The Legate's Eyes**" | Quest-name list, not narrative (ruling 1: list under "Routed to quests") | `campaign/quests/faction-events/lords-alliance/` folders; `02-lords-alliance.md:10` |
| P-4 | L11 | "**Resonance.** Jalester should inspire sympathy with his loneliness and unresolved grief, respect for his understated competence, and protectiveness when the party realizes how much of his life he has sacrificed to a job that will not love him back." | Day-one. Keep (ruling 3) | `adventure-wdh.json:1537`; `:32160` |
| P-5 | L13 | "**Emotions.** Jalester most often feels dutiful focus, private grief for Faerrel, the reward of a job done well, chronic loneliness he fills with work, guarded warmth toward competent people, and a longing for connection he does not know how to pursue." | Day-one. Keep | `adventure-wdh.json:32160`; `:1537` |
| P-6 | L15 | "**Motivations.** Jalester wants to serve Laeral Silverhand and the Lords' Alliance faithfully, find someone who makes the loneliness bearable, and prove that Faerrel's death was not meaningless." | Day-one. Keep verbatim | `01-jalester-silvermane.md:15`; `adventure-wdh.json:1537` |
| P-7 | L17 | "**Inspirations.** When playing Jalester, channel Steve Rogers (*Captain America*), Brienne of Tarth (*Game of Thrones*), and Will Graham (*Hannibal*)." | Not a fact. Keep | n/a |
| P-8 | L21 | "**Persona.** To the world, Jalester is a lean, thinning-haired Cormyte field agent in a dark doublet who asks questions more specific than casual conversation warrants. To those he trusts, he is direct, disciplined, and quietly grieving a lover named Faerrel Dunblade who died exposing a plot against the government. Deep down, he is lonely and looking for love, but he does not know how to stop working long enough to find it." | Day-one. "died exposing a plot" is one of the three versions weighed in D1 | `adventure-wdh.json:32160`; `:1537` |
| P-9 | L23 | "**Morale.** In a fight, Jalester would fight with spy's precision: controlled, efficient, no wasted movement. He notes competence gaps privately and does not discipline anyone informally. A member who fails him is dealt with through **Suspension and Dismissal**." | The first two sentences are day-one habit (the competence-gap habit is shown in one quest scene). The last sentence is a mechanic | Mechanic: `campaign/guides/factions/03-lords-alliance.md:74`. Competence-gap habit: `sources/Appendix_C_-_Player_Faction_Missions.md:538` ("...but he notes the competence gap.") |
| P-10 | L25-27 | "> [!gamemaster]**Desk Duty**" / "> If Laeral is told that Jalester has been compromised, she may put him on desk duty. Sevel Dastar then takes Jalester's place as the member's handler, as **Escalation to the Open Lord** sets out." | **Quest-time gate** (the "Laeral Told of Jalester" Event Outcome). Route it, or restate as a day-one contingency with no gate | `campaign/quests/faction-events/lords-alliance/m06-an-audience-with-the-open-lord/overview.md:58` ("Telling her puts Jalester on desk duty and sends Sevel Dastar to the Portal."); `.../m06-an-audience-with-the-open-lord/design-notes.md:13` ("**Laeral Told of Jalester** puts him on desk duty, and Sevel Dastar takes over every later contact."); `campaign/guides/factions/03-lords-alliance.md:62` |
| P-11 | L29 | "**Relationships.** Jalester is a field operative for Laeral Silverhand, a former member of the Steel Shadows mercenary company (Cormyr), the surviving partner of Faerrel Dunblade, and the Lords' Alliance faction contact who delivers missions in person because he cannot bear to delegate." | Day-one clauses, except the reason. "delivers missions in person" is sourced at `02-lords-alliance.md:55` and `03-lords-alliance.md:39`. "because he cannot bear to delegate" has **no source** in any file searched | `campaign/setting/organizations/02-lords-alliance.md:55`; `campaign/guides/factions/03-lords-alliance.md:39` |
| P-12 | L33 | "A lean field agent in a dark doublet whose questions are more specific than casual conversation warrants, and whose precise attention suggests he is always on assignment rather than simply passing through." | Day-one. Overview is 32 words (brief limit 21; re-draft) | Questions line: `sources/Appendix_D_-_Running_the_Tavern.md:1439` ("Asks questions that are more specific than casual conversation usually warrants."); `campaign/guides/trollskull-manor/08-notable-patrons.md:108` |

**Voice profile, quest-time clauses (`.claude/skills/character-voices/voices/lords-alliance.md`, "### Jalester Silvermane", lines 5-19)**

- V-1 (line 17, Greeting): "Jalester Silvermane. I'm with the Alliance. You were at the Gralhund villa on the night in question, weren't you?" — **quest-time**. It refers to the Gralhund Villa events. It lives in `campaign/guides/factions/03-lords-alliance.md:30` ("Gralhund Villa | Xanathar's Guild activity around Gralhund Villa coincided with three Watch officers being moved off that beat the tenday before. Jalester wants to know what the party saw in the villa.") and `campaign/quests/act-ii/gralhund-villa/ev-01-what-the-factions-say.md:30` (section "### Jalester Silvermane (Lords' Alliance)"). Restate as a day-one greeting or remove.
- V-2 (line 18, Business): "The Open Lord wants this handled without noise. I want it handled without anyone dying. Can you do both?" — generic. No quest file found with this sentence.
- V-3 (line 19, Under pressure): "Get the witness out. I'll hold them. That's an order, not a request." — "the witness" points to an event. No file found with "Get the witness out" (search of `campaign/` and `sources/`). Restate as generic or flag.
- V-4 (line 12, Personality in speech): "He gives competent people warm, awkward praise. His grief for Faerrel shows only as a stop mid-sentence. When he wants connection, he asks a personal question and then retreats from it." — day-one.
- V-5 (line 15, Never): "He never breaks cover carelessly, never disobeys Laeral, and never talks about Faerrel unless asked twice." — day-one.
- V-6 (line 14, Signature phrases): "\"Understood.\" / \"One more detail, if you don't mind.\" / \"Discreetly, please.\"" — day-one.
- V-7 (line 9, Sentence shape): "When he tries small talk, it comes out as a debrief." — day-one.
- V-8 (line 10, Word choice): "Agent's terminology: asset, assignment, \"the Open Lord's interests\"." — day-one.

**Quest-time items found in the wiki, not on the current page (do not use on day one)**

- Runestone errand: "Some time later Jalester was instructed by Laeral to recover from [[Undermountain]] a [[runestone]] magic crystal for her. So, telling to all he needed the crystal for himself, Jalester hired adventurers to accomplish the mission." — wiki line 83 (ref `DotMM-9`). Campaign home: `campaign/quests/faction-events/lords-alliance/r50-lioncrown/ev-01-lioncrown.md:375` ("> [!gamemaster]**The Runestone Errand**") and `:388` ("> - The Runestone and its fragments lie on Level 20, and Jalester hires adventurers of the 12th level or higher to bring him one."). The Mad Mage text has the same errand: `sources/adventure-wdmm.json:457` to `:461`.

**Quest-time lines in Alexandrian Appendix C (routed, not on the page)**

- `sources/Appendix_C_-_Player_Faction_Missions.md:512`: "\"Alliance,\" he says. Not a question. \"Jalester's still sending children, I see.\""
- `sources/Appendix_C_-_Player_Faction_Missions.md:538`: "Jalester receives the report, sighs, and says: \"I said quietly.\""
- `sources/Appendix_C_-_Player_Faction_Missions.md:557`: "Jalester assigns the party to prevent Manshoon's Zhentarim from recruiting a Red Wizard of Thay named Esloon Bezant."
- `sources/Appendix_C_-_Player_Faction_Missions.md:623`: "A rooftop assassin has been picking off targets in the North Ward. Jalester wants him found and delivered to the Watch alive."

---

## D. Conflicts

**D1. Faerrel Dunblade's death (cause, date, and the Persona version)**
- Adventure, Jalester entry: "Jalester and Faerrel helped the Open Lord expose a plot to overthrow the government, but Faerrel was killed while helping bring the perpetrators to justice." — `sources/adventure-wdh.json:32160`
- Adventure, NPC list (page 20): "Jalester is often distracted by thoughts of Faerrel Dunblade, his boyfriend, who was killed in a street fight last year." — `sources/adventure-wdh.json:1537`
- Alexandrian Appendix D, Roleplaying Keys: "**Roleplaying Keys:** Lonely — his partner Faerrel Dunblade was killed in a street fight last year — but not sorry for himself. Direct about practical matters. Asks questions that are more specific than casual conversation usually warrants. Is professional about this to the point of being slightly strange." — `sources/Appendix_D_-_Running_the_Tavern.md:1439`
- Trollskull guide: "Thinning hair, lean frame, dark doublet; lonely (partner Faerrel Dunblade killed last year) but not sorry for himself; direct; asks questions more specific than casual conversation warrants." — `campaign/guides/trollskull-manor/08-notable-patrons.md:108`
- Notable Figures page, Persona: "quietly grieving a lover named Faerrel Dunblade who died exposing a plot against the government." — `campaign/setting/notable-figures/lords-alliance/01-jalester-silvermane.md:21`
- Wiki, full line: "In [[1491 DR]], Elminster met and befriended the two young mercenaries and presented them to the Open Lord Laeral. Under the Lord's orders, Jalester and Faerrel unveiled a [[Death Masks|sinister plot]] but Faerrel was killed.<ref name="DM"/>" — wiki line 79 (novel)
- Higher rank: the brief and the organization page settle on the Notable Figures wording and "last year" (`02-lords-alliance.md:28`, `:168`). The adventure is the source for "last year" and for the "street fight" cause, and line `:32160` for "helping bring the perpetrators to justice". The drafter must pick one cause and keep "last year". Left to the user if the cause matters.

**D2. Stat block and class**
- Notable Figures page: "Stat block: **Spy**." — `campaign/setting/notable-figures/lords-alliance/01-jalester-silvermane.md:5`
- Trollskull guide: "LG male Chondathan Human, Spy" — `campaign/guides/trollskull-manor/08-notable-patrons.md:107`
- Alexandrian Appendix D: "*Lords' Alliance — N male Cormyrean human, Veteran*" — `sources/Appendix_D_-_Running_the_Tavern.md:1435`
- Adventure: "{@i LG male Chondathan human fighter}" — `sources/adventure-wdh.json:1535`
- Wiki: "| class5e        = {{Class table|edition=5e|[[Fighter]]|11}}" — wiki line 59; "| challenge5e    = 4" — wiki line 58.
- Higher rank: the adventure's class (fighter) and the wiki agree on a fighter. The Notable Figures "Spy" is a campaign label. The Appendix D "Veteran" is an Alexandrian monster name. No source gives a stat block. The drafter should not write a stat line.

**D3. Alignment**
- Notable Figures: "*Chondathan human spy, lawful good, he/him*" — `campaign/setting/notable-figures/lords-alliance/01-jalester-silvermane.md:5`
- Adventure: "{@i LG male Chondathan human fighter}" — `sources/adventure-wdh.json:1535`
- Alexandrian Appendix D: "*Lords' Alliance — N male Cormyrean human, Veteran*" — `sources/Appendix_D_-_Running_the_Tavern.md:1435`
- Higher rank: the adventure (LG) outranks the Alexandrian appendix. The campaign agrees with the adventure.

**D4. Species wording**
- Notable Figures and adventure: "Chondathan human" (`campaign/setting/notable-figures/lords-alliance/01-jalester-silvermane.md:5`; `sources/adventure-wdh.json:1535`).
- Appendix D: "Cormyrean human" (`sources/Appendix_D_-_Running_the_Tavern.md:1435`).
- Higher rank: ruling 5 (Faerûn ethnicity). "Chondathan" is the ethnicity. "Cormyrean" is not an ethnicity; the adventure's "hails from the distant land of Cormyr" (`sources/adventure-wdh.json:32159`) gives the homeland.

**D5. Age**
- Adventure: "An earnest man in his mid-twenties" (`sources/adventure-wdh.json:32159`). Wiki: "Mid‒20s in [[1492 DR]]" (line 17).
- Appendix B: "A middle-aged man in a plain dark doublet sits alone at a corner table with a tankard he has not touched." — `sources/Appendix_B_-_Player_Factions.md:210`
- Higher rank: the adventure. The Appendix B text is a readaloud description and is stale on age.

**D6. Watch rank (captain or agent)**
- Dungeon of the Mad Mage: "Volothamp Geddarm introduces the characters to a friend of his: a young captain of the City Watch named Jalester Silvermane. If the characters played through {@adventure Waterdeep: Dragon Heist|WDH}, they probably know him already. Jalester is a secret agent of the {@adventure Lords' Alliance|WDH|1|Lords' Alliance} who reports to Lady Laeral Silverhand, the Open Lord of Waterdeep." — `sources/adventure-wdmm.json:457`
- Wiki lead, full line: "'''Jalester Silvermane''' ({{Pronounce|JAH|less|ter|refs=<ref name="WDH5e-p4">{{Cite book/Waterdeep: Dragon Heist|4}}</ref>}}) was a [[Generic City Watch captain (Waterdeep)|captain]] of the [[City Watch (Waterdeep)|City Watch]] of [[Waterdeep]] and the city's main [[Lords' Alliance]] agent in [[1492 DR]].<ref name="WDH5e-p37" /><ref name="WDMM5e-p9">{{Cite book/Waterdeep: Dungeon of the Mad Mage|9}}</ref>{{Waterdeep-time}}" — wiki line 62
- Wiki, city watch list, full line: "* Captain [[Jalester Silvermane]]<ref name="WDMM5e-p10">{{Cite book/Waterdeep: Dungeon of the Mad Mage|10}}</ref> ''circa ''[[1492 DR]]" — `sources/research/pass5-bundles/city-watch/wiki.txt:101`
- Adventure (Dragon Heist, Yawning Portal NPC list): "{@creature Jalester Silvermane|WDH} (see {@adventure appendix B|WDH|12}) is an agent of the Lords' Alliance who reports directly to {@creature Laeral Silverhand|WDH}." — `sources/adventure-wdh.json:1536`
- Campaign: "**Conflicts, Jalester:** The Dungeon of the Mad Mage text (`adventure-wdmm.json` line 457) and the wiki (`wiki.txt` line 101) call him a young captain of the City Watch. Dragon Heist (`adventure-wdh.json` line 1536) and his Notable Figures page make him a Lords' Alliance agent, and this page follows them." — `campaign/setting/governance-and-guilds/city-watch.md:128`
- Higher rank: Dragon Heist and the Notable Figures page (as city-watch.md:128 says). The Watch badge (adventure `:32167`) does not make him a captain. Drafter: no Watch rank on the page.

**D7. Runestone errand (who wants the fragment)**
- Wiki: "So, telling to all he needed the crystal for himself, Jalester hired adventurers to accomplish the mission." — wiki line 83
- Dungeon of the Mad Mage: "Jalester tells the characters that he wants the fragment for himself and won't disclose its purpose, except to say that its recovery will help to ensure Waterdeep's security (a true statement)." — `sources/adventure-wdmm.json:459`
- Campaign Lioncrown: "The Runestone is Laeral's own research, and she hopes a fragment of Halaster's crystal will halt her decline. She has told Jalester only that the errand protects the city." — `campaign/quests/faction-events/lords-alliance/r50-lioncrown/ev-01-lioncrown.md:36`
- Higher rank: the campaign's Lioncrown journal. The page should not mention the errand on day one (C).

**D8. Laeral's knowledge of the Stone (day-one pages must say she does not know)**
- Factions Guide: "At campaign start, Laeral is three moves behind. Jalester's field reports and the Watch's contacts have placed the vault somewhere in Neverwinter. She doesn't know that the Stone of Golorr has resurfaced in Waterdeep or that all four villain factions are circling it. The one route by which she can learn of it early is House Gralhund: Yalah can approach the Open Lord with the Stone as collateral (**House Gralhund** in this guide)." — `campaign/guides/factions/03-lords-alliance.md:9`
- Ruling (brief, Session 53): Laeral learns of the Stone early only through Yalah Gralhund. Day-one pages still say Laeral does not know. The Jalester page does not mention the Stone, so no change is needed.

**D9. Relationships to Mirt and Elminster** — no conflict. The wiki line 74 says Jalester was friends with both; the campaign Persona and Relationships do not name them. Add only if the drafter wants them (the wiki cites `WDH5e-p205` and `WDMM5e-p9`).

---

## E. Stale lines in other files (not to be edited) and routed quest references

**E1. Stale or conflicting lines in other files**
- `sources/Appendix_D_-_Running_the_Tavern.md:1435`: "*Lords' Alliance — N male Cormyrean human, Veteran*" (conflicts with the page and the adventure on alignment, species and stat; see D2 to D4).
- `sources/Appendix_B_-_Player_Factions.md:210`: "A middle-aged man in a plain dark doublet sits alone at a corner table" (conflicts with mid-twenties; see D5).
- `sources/adventure-wdmm.json:457`: "a young captain of the City Watch" (see D6).
- `docs/plans/setting-compendium-research-notes/consistency-notable-figures.md:31`: "Jalester NF lords-alliance/01:5 \"Cormyrean human spy\"" (a research note that quotes an older label; the page now says "Chondathan human spy").
- `docs/plans/setting-compendium-research-notes/pass5/lords-alliance.md:282`: "His partner Faerrel Dunblade was killed in a street fight a year ago" (a research note that quotes an old organization-page sentence; the organization page now says "died exposing a plot against the government", see `02-lords-alliance.md:168`).

**E2. Routed quest references (quest-time facts; the day-one page must not restate them)**
- `campaign/quests/faction-events/lords-alliance/m06-an-audience-with-the-open-lord/overview.md:58`: "This scene runs only if a character present learned from Mirt that Jalester is compromised. Laeral asks what the party is not telling her, and the knowing character decides whether to answer. Telling her puts Jalester on desk duty and sends Sevel Dastar to the Portal."
- `campaign/quests/faction-events/lords-alliance/m06-an-audience-with-the-open-lord/design-notes.md:13`: "**Laeral Told of Jalester** puts him on desk duty, and Sevel Dastar takes over every later contact."
- `campaign/quests/faction-events/lords-alliance/r50-lioncrown/ev-01-lioncrown.md:161`: "He will not discuss the Open Lord's private business, the Runestone or why Jalester was moved. He answers each with \"Not mine to say.\""
- `campaign/quests/faction-events/lords-alliance/r50-lioncrown/ev-01-lioncrown.md:375` to `:388`: the Runestone Errand.
- `campaign/quests/act-ii/gralhund-villa/ev-01-what-the-factions-say.md:30`: "### Jalester Silvermane (Lords' Alliance)"; `:34`: "Jalester does not acknowledge that forty-eight hours means the Stone will be gone before any legal process concludes. He does not know. The party does."
- `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:108`: "**Lords' Alliance (Jalester).** His debrief request arrives within twenty-four hours."
- `campaign/quests/faction-events/lords-alliance/m04-the-archer-above/ev-01-the-archer-above.md:328`: "If a member names the scrap as the Cassalanter villa's side gate and gives Jalester the paper, mark **Villa Address Identified** and read or paraphrase the following:"
- `campaign/guides/factions/03-lords-alliance.md:74`: "Briefs from **The Long Watch** to **Fentree's Ledger** each state a deadline in Jalester's own words. A member who refuses a Brief, or who lets the stated deadline pass without taking any step, is suspended at a visit at the well table."
- `campaign/quests/faction-events/lords-alliance/s01-suspension-and-dismissal/ev-01-suspension-and-dismissal.md` and `campaign/quests/faction-events/lords-alliance/s02-escalation-to-the-open-lord/ev-01-escalation-to-the-open-lord.md` (quest events for the suspension and the Escalation; see `03-lords-alliance.md:74` and `:55`).
- Appendix C lines 512, 538, 557, 623 (section C above).

---

## F. Gaps a Background would need that no source gives

For each gap: the sourced facts the drafter must stay consistent with. Invented material carries `[design]` and must be listed in Draft Notes.

**F1. Birth year and early childhood.** No source gives a birth year, a childhood or a family. Sourced: "mid-twenties" in 1492 DR (`sources/adventure-wdh.json:32159`; wiki line 17); born in Cormyr (wiki line 77, `DM`); "hails from the distant land of Cormyr" (`:32159`). The drafter must keep him in his mid-twenties in 1492 DR. An invented family must be a nameless relative or place (brief ruling 17); no parents are named in any source (wiki line 29 is blank).

**F2. Mercenary years and the move to Waterdeep.** Sourced: "earned his spurs working for a mercenary company called the Steel Shadows" (`:32159`); "A few years ago, Jalester left the Dales and traveled to Waterdeep" with the company (`:32159`); wiki: "until some years before he and several members of the group left the [[Dales]] and settled in Waterdeep" (line 77). No campaign file gives the company's history in Cormyr or the Dales.

**F3. Meeting Faerrel and the work for Laeral.** Sourced: met as fellow mercenaries and became "best friend and lover" (`:32159`); wiki: "There, he fell in love with his fellow mercenary Faerrel." (line 77). Elminster "befriended the two young men" and Laeral put them "to work as deputies and spies" (`:32160`). The wiki's year is 1491 DR (line 79, novel).

**F4. Faerrel's death.** See D1. The drafter must pick the cause from the versions or write the death without a cause, with a `[research]` tag. Sourced: "last year" (`sources/adventure-wdh.json:1537`; `02-lords-alliance.md:28`); "died exposing a plot against the government" (page line 21); "helping bring the perpetrators to justice" (`:32160`).

**F5. Where he lives.** No source gives a home. Sourced: he sits at the corner table at the Yawning Portal most evenings (`02-lords-alliance.md:55`; `sources/adventure-wdh.json:1536`: "usually seated by himself in a quiet corner"). The Alliance's safe house at "14 Ironwick Lane in the Trades Ward" is the Alliance's, not his (`02-lords-alliance.md:53`).

**F6. Watch career before the Alliance.** Only the wiki and the Mad Mage text give one, and they call him a captain (D6). The drafter should not use a Watch rank. The badge (`:32167`) is the only Watch fact in Dragon Heist.

**F7. Faith.** No source gives one (A7). Leave blank or use `[design]`.

**F8. Personal goals.** The page's Motivations (line 15) already give "find someone who makes the loneliness bearable, and prove that Faerrel's death was not meaningless." Sources: "longs again for love" (`:32160`); "is lonely and looking for love" (`:1537`). A `**Personal goals.**` paragraph may build on these; anything beyond them is `[design]`.

**F9. Physical details.** Sourced: "Thinning brown hair, a lean angular frame, dark silver-grey doublet" (Appendix D, `sources/Appendix_D_-_Running_the_Tavern.md:1437`); "a lean man, thinning dark hair" (Appendix B, `sources/Appendix_B_-_Player_Factions.md:213`). The hair colour conflicts (brown or dark); use "thinning" only.

---

## G. Source facts that hint at the figure's inner life (exact quotes)

- Adventure, page 20: "Jalester is often distracted by thoughts of Faerrel Dunblade, his boyfriend, who was killed in a street fight last year. When not engaged in alliance business, Jalester is lonely and looking for love." — `sources/adventure-wdh.json:1537`
- Adventure, page 205: "He has been romantically unattached ever since Faerrel's death but longs again for love." — `sources/adventure-wdh.json:32160`
- Adventure, page 205: "one of whom-Faerrel Dunblade-would become his best friend and lover." — `sources/adventure-wdh.json:32159`
- Wiki, line 65: "He often thought about his dead boyfriend [[Faerrel Dunblade]]. He was lonely and in search of love." (ref `WDH5e-p20`)
- Appendix B, readaloud: "He stands as you approach — a lean man, thinning dark hair, the composed stillness of someone who has either spent a long time in professional service or a long time grieving, and has let them become the same thing." — `sources/Appendix_B_-_Player_Factions.md:213`
- Appendix B, readaloud: "\"Jalester Silvermane.\" His handshake is firm and brief. He does not smile, but he is not cold — he is simply economical." — `sources/Appendix_B_-_Player_Factions.md:214`
- Appendix D, Roleplaying Keys: "Lonely — his partner Faerrel Dunblade was killed in a street fight last year — but not sorry for himself. Direct about practical matters." — `sources/Appendix_D_-_Running_the_Tavern.md:1439`
- Organization page, GM Notes: "He is grieving his partner, Faerrel Dunblade, who died last year exposing a plot against the government, and he fills the silence with work." — `campaign/setting/organizations/02-lords-alliance.md:118`
- Notable Figures, Emotions (line 13): "private grief for Faerrel, the reward of a job done well, chronic loneliness he fills with work, guarded warmth toward competent people, and a longing for connection he does not know how to pursue."
- Notable Figures, Motivations (line 15): "find someone who makes the loneliness bearable, and prove that Faerrel's death was not meaningless."
- Voice profile, line 12: "His grief for Faerrel shows only as a stop mid-sentence. When he wants connection, he asks a personal question and then retreats from it."
- Voice profile, line 15: "He never breaks cover carelessly, never disobeys Laeral, and never talks about Faerrel unless asked twice."
- Adventure, badge (`:32167`): "If the badge is lost or taken from him, it returns to Laeral Silverhand." (a tie to Laeral)
- Adventure, page 20 (`:1536`): "Durnan knows that Jalester works for Laeral and leaves the young man alone." — this sentence is the end of the full paragraph quoted in A4 (`:1536`).

**Cassalanter secrecy and the Alliance (Connections)**
- Organization page: "- **The Cassalanters** (neutral, suspicious): The Alliance has no proof against the family and knows nothing of a pact. Its speakers think the family too rich and too pleasant, and the Watch has closed three complaints against the house (**The Cassalanters**; **Lords' Alliance** in the Factions Guide)." — `campaign/setting/organizations/02-lords-alliance.md:93`
- Factions Guide: "They never say more of the Cassalanters than that the family is too rich and too pleasant, and nobody in the Alliance has proof of anything." — `campaign/guides/factions/03-lords-alliance.md:13`
- Conflict: `campaign/setting/villains/cassalanters.md:71` and `:117` ("Lords' Alliance contacts"); see the organization page Draft Notes at `02-lords-alliance.md:177`.

**Lolth and Xanathar**: no Lolth line in either Lords' Alliance file. Xanathar appears as "Xanathar's Guild" in `02-lords-alliance.md:91` and as "Xanathar" in the adventure at `:15170`.

---

## Cross-references (every other file:line where the topic appears, with its line)

- `campaign/setting/organizations/02-lords-alliance.md:28` (Faerrel, last year), `:53` (safe house), `:55` (corner table), `:57` (primary contact), `:69` (information), `:91` (Xanathar's Guild), `:93` (Cassalanters), `:101` and `:103` (Key Members and Sevel Dastar), `:118` (GM Notes), `:168` (the settled Faerrel wording)
- `campaign/guides/factions/03-lords-alliance.md:9`, `:13`, `:23`, `:30`, `:39`, `:41`, `:62`, `:74`
- `campaign/setting/governance-and-guilds/city-watch.md:38`, `:65`, `:128`
- `campaign/guides/trollskull-manor/08-notable-patrons.md:107`, `:108`, `:109`
- `campaign/setting/history/07-a-city-watching-itself.md:43` ("Jalester Silvermane is her field operative and reports to her directly, and the Lords' Alliance is her instrument for acting outside the Palace.")
- `campaign/setting/history/07-a-city-watching-itself.md:26` ("- Her intelligence comes from Jalester Silvermane and the Watch, and it is about three moves behind." — see the line 26 text in that file before quoting)
- `campaign/setting/governance-and-guilds/guilds.md:104` (Jalester in the list of named people)
- `sources/adventure-wdh.json`: `:153` and `:154` (pronunciation "JAH-less-ter"), `:1384` ("Laeral employs adventurers as agents of the Lords' Alliance, among them {@creature Jalester Silvermane|WDH}."), `:1536`, `:1537`, `:3891` to `:3896`, `:15170` to `:15172`, `:32155` to `:32171`
- `sources/Appendix_B_-_Player_Factions.md:183`, `:185`, `:204`, `:210`, `:213`, `:214`, `:215` to `:229`
- `sources/Appendix_C_-_Player_Faction_Missions.md:512`, `:538`, `:557`, `:590`, `:606`, `:623`, `:681`
- `sources/Appendix_D_-_Running_the_Tavern.md:56`, `:279`, `:569`, `:795`, `:1119`, `:1435` to `:1443`
- `sources/adventure-wdmm.json:457` to `:461`, `:54522`, `:54726`
- `sources/3. Player Character Factions.pdf` PDF p.3 (printed p.25): "The Lords' Alliance actually works directly for the Open Lord. If Jalester Silvermane becomes aware of what the PCs have gotten themselves tangled up in, he'll arrange a discreet meeting with Laeral Silverhand as quickly as possible." (transcribed from the image; check with pdftotext)

---

## Not found

- Searched for Jalester's birth year, parents, siblings, children, faith and home: nothing in the campaign, the adventure, Appendix B, C, D, the Factions Guide, the Trollskull guide, the Notable Figures pages or the wiki extract. Gaps listed in F.
- Searched for a stat block for Jalester ("Jalester", "Silvermane", "Spy", "Veteran") in `docs/plans/lords-alliance-mechanics-reference.md`, `docs/plans/harpers-mechanics-reference.md` and `campaign/`: no stat line for him.
- Searched for "cannot bear to delegate" and "delegat" in `campaign/setting/notable-figures/lords-alliance/`: only the page's line 29. No other source.
- Searched for "Get the witness out" and "I'll hold them" in `campaign/` and `sources/`: no match outside the voice profile (`.claude/skills/character-voices/voices/lords-alliance.md:19`).
- Searched for the Laeral magic ruling ("not fully"). The campaign line is `campaign/setting/history/07-a-city-watching-itself.md:23`: "- She governs with deputies and uses her own magic sparingly, because it waned with Mystra's death and the Spellplague. It has come back since the Weave returned in 1487, though not fully. Only Elminster knows how far, and she admits it to one Lioncrown of the Lords' Alliance." It is not on this page.
- Searched `sources/research/pass5-bundles/lords-alliance/` for a Lords' Alliance wiki file: the folder holds only `campaign-hits.txt` and `adventure-hits.txt`. The only Jalester wiki text is the scratchpad extract.

## Not readable

- `sources/Other remix files/*.docx`: not opened (no shell). `sources/SOURCE_GUIDE.md` lists no `.docx` for Jalester in the lines searched (`:172`, `:600`); the `.docx` at `:696` is for Vajra (see the Force Grey notes).
- The Alexandrian PDF `sources/3. Player Character Factions.pdf` was read only at PDF p.3 (printed p.25). PDF p.2 (printed p.24) was not read for this page.
