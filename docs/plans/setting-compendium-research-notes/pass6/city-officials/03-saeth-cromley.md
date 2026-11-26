# Pass 6 research notes: Saeth Cromley

Page: `campaign/setting/notable-figures/city-officials/03-saeth-cromley.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Brief ruling 2 sizes a page by role; no source names Saeth as a head, villain or lieutenant, so the size class is left to the orchestrator. Ruling 2 gives minor NPCs "two or three sentences" of Personality and "one line" of Connections; ruling 15 gives them "at least two" Background paragraphs.
Organization page: `campaign/setting/organizations/11-open-lords-watch.md` (The Open Lord's Watch)
Factions Guide: `campaign/guides/factions/12-open-lords-watch.md` (The Open Lord's Watch; Saeth appears only as a cross-reference and in Draft Notes)
Governance: `campaign/setting/governance-and-guilds/city-watch.md`, `code-legal-and-magisters.md`
Voice profile: `.claude/skills/character-voices/voices/city-officials.md` (`### Saeth Cromley`, lines 43-57)
Wiki extract: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-city-officials/03-saeth-cromley.txt` (quoted as "wiki line N" = that file's lines; infobox refs name `WDH5e-p215` = Dragon Heist 5e p.215)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines. Where a Grep line was too long to print, I re-read it or used a bounded `-o` match; the quote says so.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes are shown as plain text. `{@creature ...}` tags are left as written. Page numbers are the `page` field of the entry.
- Alexandrian: `sources/Act_III_Arc_D.md` (markdown, read by Grep). `sources/7. Other Response Teams.pdf` (5 PDF pages = printed pp. 57-61) was read as rendered images. It has no mention of Saeth Cromley. Appendix B, C and D markdown have no mention of Saeth (Grep). No PDF text was extracted; no PDF quote is used in this note.
- The `.docx` in `sources/Other remix files/` named under Not readable may hold NPC material for this figure.
- No shell was available. `voicecheck.py` was not run. No file was edited except this notes file.
- Lolth and Cassalanter secrecy: no Cassalanter or Lolth line touches this page (checked in section F).

## Findings that change how the page is written

1. **Retired on day one; "Sergeant" is the fireball scene.** The adventure's Saeth entry says he is retired and "occasionally comes out of retirement" (`adventure-wdh.json:32573`). The fireball scene calls him "a City Watch sergeant" (`adventure-wdh.json:4444`). The Watch organization page and the Factions Guide both record him as retired (conflict D1).
2. **Three Persona and Relationships phrases have no source:** "now that no one checks" (Persona), "keep wearing the badge" (Persona) and "Charisma enough to coax information from anyone" (Relationships). "only friend" is Barnibus's page wording, not the adventure's (section B and D8).
3. **The Summary's "buys him a drink" clause is the quest mechanic.** The sergeants'-room habit is day-one (`castle-ward.md:134`, `11-open-lords-watch.md:79`). The drink rule is written in three quest events (section C, row 1).
4. **Overview is 29 words**, over the brief's 21-word limit (`page line 31`).
5. **The voice profile calls Barnibus "the magistrate"**, and one Business sample line describes the gnome blast (quest-time). The adventure gives Barnibus no magistrate's title (conflict D3).

---

## A. Background facts by theme

### A1. Origin, home, family

**Wiki, infobox (WDH5e-p215)**
> "| home           = [[Waterdeep]], [[Sword Coast North]]"
> — wiki line 11

> "| ethnicity      = [[Illuskan]]<ref name="WDH5e-p215" />"
> — wiki line 15

Blank infobox fields, with no birth, family or age: "| age            = " (wiki line 17), "| dob            = " (line 21), "| parents        = " (line 29), "| spouses        = " (line 30), "| siblings       = " (line 31), "| children       = " (line 32). All are empty.

**Adventure, Saeth Cromley entry (page 215)**
> "{@creature Saeth Cromley|wdh} is a retired {@creature sergeant|WDH} of the City Watch, a likable fellow with a sharp, sarcastic wit. He occasionally comes out of retirement at the request of {@creature Barnibus Blastwind|WDH}, and he assists the mage in investigating unusual crimes in the city. Cromley helps Barnibus relate to the common folk, and he is good at coaxing information out of them. Though Cromley was once a strict proponent of Watch regulations and dress codes, he has grown a bit lax in both matters now that he's officially retired."
> — `sources/adventure-wdh.json:32573` (entry "Saeth Cromley", page 215)

**Adventure, Game Statistics (page 215)**
> "{@creature Saeth Cromley|WDH} is an Illuskan human {@creature veteran}, with these changes:"
> — `sources/adventure-wdh.json:32580`

**Voice profile, Sound**
> "- **Sound:** A gravelly, easygoing voice with a laugh in it, a Dock Ward edge he never lost."
> — `.claude/skills/character-voices/voices/city-officials.md:46` (the only source that places him in the Dock Ward; it is a speech-profile line, not a history)

No source gives his birth, parentage, hometown, faith, age or how he came to Waterdeep. The wiki's home field is the city, not a ward.

### A2. Watch career, rank, retirement

**Wiki, lead (WDH5e-p215)**
> "was a retired [[City Watch (Waterdeep)|City Watch]] [[Generic City Guard sergeant (Waterdeep)|sergeant]] in [[Waterdeep]] in the early 1490s [[DR]]."
> — wiki line 62 (the lead sentence; the only retirement date in any source, and it is a range, not a year)

**Wiki, occupation and titles**
> "| titles         = [[Generic City Guard sergeant (Waterdeep)|Sergeant]]" — wiki line 7
> "| occupation     = Retired City Watch sergeant<ref name="WDH5e-p215" />" — wiki line 16

**Wiki, History (WDH5e-p215)**
> "Saeth was once an officer in the City Watch until he decided to retire. Sometimes, however, he helped Barnibus in difficult cases."
> — wiki line 71

**Wiki, Personality (WDH5e-p215)**
> "Saeth was a likable fellow with a sharp, sarcastic wit. He was very capable of collecting information from common folk. Once he was very strict about the City Watch's dress code but after his retirement he wore more practical dress."
> — wiki line 65

**Organization page, Key Members (The Open Lord's Watch)**
> "- **Saeth Cromley** — Illuskan human retired sergeant, lawful good, he/him. A retired sergeant of the Watch who helps Barnibus Blastwind with investigations and sits in the sergeants' room at the Halls of Justice in the afternoons. See the **Saeth Cromley** page in Notable Figures."
> — `campaign/setting/organizations/11-open-lords-watch.md:79`

**Governance, City Watch, Key figures**
> "**Saeth Cromley** (Lawful Good, Illuskan Human, he/him) is a retired sergeant of the Watch who assists Barnibus Blastwind in many of his investigations. In the fireball scene he escorts Barnibus to the crime scene and sends twenty constables door to door. Between cases he sits in the sergeants' room at the Halls of Justice in the afternoons, and a visitor who buys him a drink finds him easy to talk to."
> — `campaign/setting/governance-and-guilds/city-watch.md:59` (the fireball clause is quest-time; see C)

**Adventure, Barnibus entry (page 195): Saeth's role for Barnibus**
> "{@creature Barnibus Blastwind|wdh|Barnibus} works for the Watchful Order of Magists and  Protectors, investigating crimes that involve the use of  magic. He comes across as prickly and secretive, confiding only in {@creature Saeth Cromley|wdh}, a retired {@creature sergeant|WDH} of the City  Watch who assists in many of his investigations."
> — `sources/adventure-wdh.json:31774` (entry "Barnibus Blastwind", page 195)

**Wiki, Watch list (pass5 bundle copy of the wiki)**
> "* Sergeant [[Saeth Cromley]]: was retired, but sometimes helped with investigations<ref name="WDH5e-p215">{{Cite book/Waterdeep: Dragon Heist|215}}</ref>"
> — `sources/research/pass5-bundles/city-watch/wiki.txt:104`

**Settled note on the organization page (rank only)**
> "> - **Settled:** Cromley is a retired sergeant, per his Notable Figures page (`03-saeth-cromley.md:5`). The fireball scene's "Sergeant Cromley" is a quest matter and stays off this page."
> — `campaign/setting/organizations/11-open-lords-watch.md:155`

### A3. Partnership with Barnibus

**Wiki, Relationships (WDH5e-p215)**
> "Saeth had a working partnership with Barnibus."
> — wiki line 68

> "Saeth, like his friend [[Barnibus Blastwind]] of the [[Watchful Order of Magists and Protectors]], wanted solid evidence and testimonies before ordering arrests. He preferred to not have unauthorized people inside the crime scene.<ref name="WDH5e-p44-45" />"
> — wiki line 65 (the wiki cites WDH p.44-45, the fireball scene; see F and C)

**Barnibus Notable Figures page, Relationships**
> "**Relationships.** Barnibus is an investigator for the Watchful Order of Magists and Protectors, the exclusive professional partner of Saeth Cromley (his only real friend), and the **Fireball!** investigator who examines the fireball scene."
> — `campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md:25`

**Governance, Barnibus entry**
> "He is prickly and secretive, confides only in Cromley and finds violence appalling."
> — `campaign/setting/governance-and-guilds/city-watch.md:61`

**Adventure 31774**: quoted in A2 (the "confiding only in" wording; the adventure does not say "friend").

### A4. Places he is found

**Gazetteer, Castle Ward, Saeth entry**
> "**Saeth Cromley (Lawful Good, Illuskan Human, he/him)**
> - Retired City Watch sergeant. He sits in the Halls of Justice sergeants' room in the afternoons, and a visitor who buys him a drink finds him easy to talk to.
> - He helps Barnibus Blastwind with unusual crimes by translating between the investigator and the common folk."
> — `campaign/gazetteer/waterdeep/castle-ward.md:133-135`

**Gazetteer, Castle Ward, ward note**
> "Barnibus Blastwind and Saeth Cromley work out of the ward."
> — `campaign/gazetteer/waterdeep/castle-ward.md:9` (the Castle Ward is the ward where he works; no home ward is given)

**Gazetteer, Castle Ward, temple clerk's office**
> "- The Order keeps a clerk's office in the east annex, and Brother Haldric Wence there arranges *Speak with Dead* on bodies the Watch holds. Saeth Cromley drinks in the sergeants' room most afternoons."
> — `campaign/gazetteer/waterdeep/castle-ward.md:66` (verb "drinks", not "sits"; see D2)

**Faith link (not a faith)**
> "- **Savra Belabranta**, **Sister Valdra**, **Hlam**, **Lady Gondafrey**, **Saeth Cromley**, **Vajra Safahr, the Blackstaff** (Notable Figures): the people tied to the Halls and the faith."
> — `campaign/setting/deities/tyr.md:114` (the Tyr page groups him with the Halls; it gives no faith, rite or devotion to him)

### A5. Personal habits, looks and traits (day-one register)

**Voice profile, Personality in speech, Quirks, Never**
> "- **Personality in speech:** Wry amusement and patience. He gets witnesses talking by being unimpressive. He misses the Watch, and it comes out as nostalgia disguised as complaint."
> — `.claude/skills/character-voices/voices/city-officials.md:50`
> "- **Quirks:** He scratches his chin before the killer question. He adjusts a badge he isn't technically supposed to wear anymore."
> — `.claude/skills/character-voices/voices/city-officials.md:51`
> "- **Never:** He never takes a bribe, never talks down to common folk, and never admits he misses the job."
> — `.claude/skills/character-voices/voices/city-officials.md:53`

**Stat-level traits, adventure**
> "He has a Charisma of 14 and Intimidation +4."
> — `sources/adventure-wdh.json:32585` (list item under "Game Statistics")

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Summary: "> - *Illuskan human retired sergeant, lawful good, he/him*. Stat block: **Warrior Veteran**." — `campaign/setting/notable-figures/city-officials/03-saeth-cromley.md:5`
- Adventure: "Saeth is lawful good." — `sources/adventure-wdh.json:32584`
- Wiki: "| alignment5e    = [[Lawful good]]" — wiki line 57 (5e)
- Governance: "**Saeth Cromley** (Lawful Good, Illuskan Human, he/him) is a retired sergeant of the Watch" — `campaign/setting/governance-and-guilds/city-watch.md:59`
- Gazetteer: "**Saeth Cromley (Lawful Good, Illuskan Human, he/him)**" — `campaign/gazetteer/waterdeep/castle-ward.md:133`
- Organization page: "Illuskan human retired sergeant, lawful good, he/him" — `campaign/setting/organizations/11-open-lords-watch.md:79`

**Species and ethnicity**
- Summary: "Illuskan human" — `03-saeth-cromley.md:5`
- Adventure: "{@creature Saeth Cromley|WDH} is an Illuskan human {@creature veteran}" — `sources/adventure-wdh.json:32580`
- Wiki: "| race           = [[Human]]<ref name="WDH5e-p215" />" — wiki line 14; "| ethnicity      = [[Illuskan]]<ref name="WDH5e-p215" />" — wiki line 15
- "Illuskan" is the same in all five sources above. Brief ruling 5 (Faerûn ethnicity) is met by "Illuskan".

**Pronouns**
- Summary: "he/him" — `03-saeth-cromley.md:5`
- Adventure: "he has grown a bit lax in both matters now that he's officially retired." — `sources/adventure-wdh.json:32573`
- Wiki: "| sex            = Male<ref name="WDH5e-p215">{{Cite book/Waterdeep: Dragon Heist|215}}</ref>" — wiki line 13
- Page prose: "To those he trusts, he is Barnibus's translator" (Persona, `03-saeth-cromley.md:23`). Pronouns are not inferred, and all sources agree on he/him.

**Stat block**
- Summary: "Stat block: **Warrior Veteran**." — `03-saeth-cromley.md:5`
- Adventure: "{@creature Saeth Cromley|WDH} is an Illuskan human {@creature veteran}, with these changes:" followed by "Saeth is lawful good.", "He has a Charisma of 14 and Intimidation +4.", "He speaks Common." — `sources/adventure-wdh.json:32580-32586`. The adventure names no 2024 stat block and no CR.
- Wiki: "| challenge5e    = 3" — wiki line 58; "| class5e        = [[Veteran]]" — wiki line 59; "| refs5e         = <ref name="WDH5e-p215" /><ref name="MM5e-p350">{{Cite book/Monster Manual 5th edition|350}}</ref>" — wiki line 60.
- Mechanics reference: "| Veteran (Mirt NF, Saeth NF) | **Warrior Veteran** | 3 | XMM p.320. Mirt uses the WDH CR 9 record instead. |" — `docs/plans/harpers-mechanics-reference.md:571`
- Stale 2014 label, Harpers notes: "- **Saeth Cromley's page** (`city-officials/03-saeth-cromley.md`) carries the 2014 "Veteran" block." — `docs/plans/harpers-out-of-scope-notes.md:838`
- Stale 2014 label, quest design note: "- Saeth Cromley's Notable Figures page lists the old **Veteran** stat block and should read **Warrior Veteran**." — `campaign/quests/faction-events/lords-alliance/m04-the-archer-above/design-notes.md:28`. The page now reads "Warrior Veteran" (line 5), so both notes are stale.

**Pronunciation**
> "{@creature Saeth Cromley|WDH}",
> "SAYTH KROM-lee"
> — `sources/adventure-wdh.json:285-286` (pronunciation table entry)

**Affiliation label**
- Summary: "> - **Affiliation:** City of Waterdeep" — `03-saeth-cromley.md:6`
- Organization page, for Laeral (the only Watch-page affiliation sentence): "**Laeral Silverhand** — Moon elf archmage, chaotic good, she/her. The Open Lord, to whom the Commander of the Watch reports. Her Notable Figures page lists her affiliation as the City of Waterdeep." — `campaign/setting/organizations/11-open-lords-watch.md:78`
- Barnibus Notable Figures page: "> - **Affiliation:** City of Waterdeep (Watchful Order of Magists and Protectors)" — `campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md:6`
- Quest journals use "(City of Waterdeep)": "- **Saeth Cromley** (City of Waterdeep): a retired Watch sergeant with a missing officer on his mind." — `campaign/quests/faction-events/harpers/m04-a-friends-house/overview.md:52`; "- **Saeth Cromley** (City of Waterdeep): a retired Watch sergeant who recognises the shooter's walk and knows the roofs." — `campaign/quests/faction-events/lords-alliance/m04-the-archer-above/overview.md:84`
- The organization page's own label for him is "retired sergeant" (`11-open-lords-watch.md:8` and `:79`), not a faction. The Watch is "The Open Lord's Watch" (`11-open-lords-watch.md:1`). "City of Waterdeep" matches the other city-officials pages. Whether to add "(retired City Watch)" is the orchestrator's call.

---

## C. Sentences on the current page (and related text) that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/city-officials/03-saeth-cromley.md`. The page has no Background, Personality or Connections section yet. Each row says where the fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L9 | "Saeth sits in the sergeants' room at the Halls of Justice in the afternoons, and a visitor who buys him a drink finds him easy to talk to." | Habit is day-one. "a visitor who buys him a drink finds him easy to talk to" is the quest gate in three events. Restate as the habit only. | Habit: `campaign/gazetteer/waterdeep/castle-ward.md:134`; `campaign/setting/organizations/11-open-lords-watch.md:79`; `campaign/setting/governance-and-guilds/city-watch.md:59`. Drink gate: `campaign/quests/faction-events/lords-alliance/m04-the-archer-above/ev-01-the-archer-above.md:103` ("Any character who buys him a drink for 2 gp and describes the shooter gets the answers below"); `campaign/quests/faction-events/order-of-the-gauntlet/s02-savras-past/ev-01-savras-past.md:64` ("Any member who buys him a drink and asks about the Howling Hatred gets the account below"). Receive-the-member rule: `campaign/quests/faction-events/lords-alliance/r10-stingblade/ev-01-stingblade.md:124` |
| 2 | L7 | "**Featured in:** **Fireball!**, **Gralhund Villa**, **A Friend's House**, **The Archer Above**, **Stingblade**, **Savra's Past**" | Quest-name list. Routed. | Quest folders named in E2; Factions Guide cross-reference `campaign/guides/factions/12-open-lords-watch.md:154` |
| 3 | L23 | "Deep down, he misses the Watch but will not admit it, and Barnibus's cases give him an excuse to keep wearing the badge." | "misses the Watch" is day-one (see G). "keep wearing the badge" has no day-one source. | Misses the Watch: `.claude/skills/character-voices/voices/city-officials.md:50` ("He misses the Watch"); `campaign/quests/faction-events/lords-alliance/m04-the-archer-above/ev-01-the-archer-above.md:109` ("he misses the Watch more than he admits"). Badge: the only badge line for him is a quest reward: `campaign/quests/act-ii/fireball/ev-06-the-death-mark.md:27` ("a Watch badge obtained at the crime scene (from Cromley or Barnibus), grants automatic entry") |
| 4 | L23 | "a bit lax in dress code now that no one checks" | "a bit lax" is day-one (adventure). "now that no one checks" is not in any source. | `sources/adventure-wdh.json:32573` ("he has grown a bit lax in both matters now that he's officially retired") |
| 5 | L25 | "In a fight, Cromley would draw his sword and position himself to protect Barnibus." | "protect Barnibus" is a fireball-scene role (bodyguard). "draw his sword" is in no source. | `sources/adventure-wdh.json:4454` ("with {@creature Sergeant|WDH} Cromley by his side as a witness and bodyguard"); wiki line 73 ("He acted as bodyguard and assistant to Barnibus.", 1492 DR, quest-time) |
| 6 | L27 | "Cromley is the retired partner and only friend of Barnibus Blastwind, a former sergeant of the City Watch (confirmed rank; not Watch Commander despite some in-text references)" | "retired partner" is day-one (wiki line 68; Barnibus page L25). "only friend" is Barnibus's page's wording. The parenthesis is a Draft Note inside the body. "not Watch Commander despite some in-text references": no source found that names him Commander (see D7). | `campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md:25`; `sources/adventure-wdh.json:31774` ("confiding only in") |
| 7 | L27 | "and an Illuskan veteran with Charisma enough to coax information from anyone." | "Charisma 14" is the stat line. "from anyone" is an overreach. | `sources/adventure-wdh.json:32585`; `sources/adventure-wdh.json:32573` ("he is good at coaxing information out of them") |
| 8 | L31 | "Saeth Cromley is a retired City Watch sergeant who works alongside Barnibus Blastwind on investigations, translating between the investigator's forensic reasoning and the common folk they need to interview." | Day-one in substance. 29 words (brief limit 21). | `sources/adventure-wdh.json:32573` ("Cromley helps Barnibus relate to the common folk") |
| 9 | Voice L56 | "What the magistrate means is, somebody blew up a gnome in your street, and we'd like to know who." | Quest-time: the gnome blast. | `sources/adventure-wdh.json:4444` ("a City Watch {@creature sergeant|WDH} named {@creature Saeth Cromley|wdh}"); `sources/adventure-wdh.json:4454` ("Specifically, Barnibus wants to find out the gnome's identity and whether he was known to anyone."); wiki line 73 ("In [[1492 DR]],{{WDH-time}} Saeth, together with Barnibus, was called in to investigate the blast that killed ten people in [[North Ward of Waterdeep|North Ward]], including the [[gnome]] [[Dalakhar]].") |
| 10 | Voice L57 | "Get down, sunshine. That's not a firework." | Reads as a scene line during an attack or blast. The drafter decides. | Same as row 9 (blast scene); `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:36` ("and **Sergeant Saeth Cromley** appear with twenty constables and formally take charge.") |
| 11 | Voice L51 | "He adjusts a badge he isn't technically supposed to wear anymore." | No day-one badge source (see row 3). | As row 3 |
| 12 | Voice L48, L55, L56, L57 | "the magistrate" (Barnibus) | Title conflict, not quest-time (see D3). | `sources/adventure-wdh.json:31774` (no magistrate); `campaign/setting/governance-and-guilds/city-watch.md:61` ("The published adventure gives him no magistrate's office.") |

**Quest-time items on the Watch and Gralhund pages that touch Saeth (routed, not day-one)**
- `campaign/setting/governance-and-guilds/city-watch.md:59`: "In the fireball scene he escorts Barnibus to the crime scene and sends twenty constables door to door." (fireball, quest-time)
- `campaign/guides/factions/12-open-lords-watch.md:80`: "Barnibus Blastwind, Saeth Cromley and 20 constables take charge." (fireball, quest-time, in the response-clock table). The organization page's Routed to quests list at `11-open-lords-watch.md:162` names the same arrival.
- `campaign/guides/factions/12-open-lords-watch.md:95`: "and he offers a conversation with Cromley, who will look away for 48 hours if the party commits to sharing its intelligence in that time." (Gralhund Villa, quest-time)
- `campaign/guides/factions/12-open-lords-watch.md:110`: "(**Fireball!**, through a faction channel, a 25 gp temple donation or a DC 13 Charisma (Persuasion) check on Barnibus or Cromley)." (fireball, quest-time)

---

## D. Conflicts (quoted both sides, file:line)

**D1. Retired or serving at the fireball (Watch rank and status)**
- Day-one status, retired: "He occasionally comes out of retirement at the request of {@creature Barnibus Blastwind|WDH}" — `sources/adventure-wdh.json:32573` (page 215); "now that he's officially retired" — `:32573`; wiki "was a retired [[City Watch (Waterdeep)|City Watch]] [[Generic City Guard sergeant (Waterdeep)|sergeant]] in [[Waterdeep]] in the early 1490s [[DR]]." — wiki line 62.
- Fireball, serving: "Twenty minutes after the explosion, a City Watch {@creature sergeant|WDH} named {@creature Saeth Cromley|wdh} (see {@adventure appendix B|WDH|12}) escorts a member of the Watchful Order of Magists and Protectors named {@creature Barnibus Blastwind|WDH} (see {@adventure appendix B|WDH|12}) to the crime scene. Barnibus quietly takes charge of the investigation at that point, while {@creature Sergeant|WDH} Cromley directs a force of twenty constables ({@creature veteran||veterans}) to knock on doors and question locals." — `sources/adventure-wdh.json:4444` (page 44, "The Watch Arrives")
- Fireball, serving (Alexandrian): "Twenty minutes after the explosion, Sergeant **Saeth Cromley** escorts **Barnibus Blastwind** of the Watchful Order of Magists and Protectors to the crime scene." — `sources/Act_III_Arc_D.md:137`
- Fireball, serving (quest): "Twenty minutes before **Barnibus Blastwind** (meticulous Illuskan human mage, Watchful Order) and **Sergeant Saeth Cromley** appear with twenty constables and formally take charge." — `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:36`
- Wiki, Watch list: "* Sergeant [[Saeth Cromley]]: was retired, but sometimes helped with investigations" — `sources/research/pass5-bundles/city-watch/wiki.txt:104`
- The governance page records the same conflict: "This page calls him retired and shows him escorting Barnibus and directing the constables, which is what line 4444 says. The user should confirm." — `campaign/setting/governance-and-guilds/city-watch.md:127`
- Factions Guide Draft Notes: "> - **Conflicts, Cromley:** `fireball/ev-01-the-fireball.md:36` calls him \"Sergeant Saeth Cromley\". `notable-figures/city-officials/03-saeth-cromley.md:5` says \"retired sergeant\". This page follows the Notable Figures page and names no rank." — `campaign/guides/factions/12-open-lords-watch.md:173`
- Higher-ranked source for the day-one page: the adventure's Saeth entry (`:32573`, retired and occasionally recalled) and the organization page (`11-open-lords-watch.md:79`). The fireball "Sergeant" is quest-time. Not settled by the user (`city-watch.md:127`).

**D2. Where he sits and whether he drinks**
- "Saeth Cromley drinks in the sergeants' room most afternoons." — `campaign/gazetteer/waterdeep/castle-ward.md:66`
- "- Retired City Watch sergeant. He sits in the Halls of Justice sergeants' room in the afternoons, and a visitor who buys him a drink finds him easy to talk to." — `campaign/gazetteer/waterdeep/castle-ward.md:134`
- "Between cases he sits in the sergeants' room at the Halls of Justice in the afternoons" — `campaign/setting/governance-and-guilds/city-watch.md:59`
- "who sits in the sergeants' room at the Halls of Justice in the afternoons" — `campaign/setting/organizations/11-open-lords-watch.md:79`
- "Saeth sits in the Watch sergeants' room at the Halls of Justice most afternoons." — `campaign/quests/faction-events/order-of-the-gauntlet/s02-savras-past/ev-01-savras-past.md:64`
- The verb differs ("drinks" versus "sits") in the gazetteer's two lines (66 and 134). The other sources say "sits". The Halls of Justice is a court and temple: "the Halls of Justice as temple and courts" (`campaign/setting/deities/tyr.md:92`, which cites castle-ward).
- Higher-ranked: the gazetteer's Castle Ward entry (`castle-ward.md:134`) and the organization page agree on "sits". Line 66 is a ward-life line. The drafter's choice.

**D3. "Magistrate" (Barnibus's title)**
- Voice profile: "Don't mind the magistrate, he's friendlier than he sounds." — `.claude/skills/character-voices/voices/city-officials.md:55`; the same title appears at `:48`, `:56` and `:57`.
- Adventure: "{@creature Barnibus Blastwind|wdh|Barnibus} works for the Watchful Order of Magists and  Protectors, investigating crimes that involve the use of  magic." — `sources/adventure-wdh.json:31774` (no title)
- Governance: "The published adventure gives him no magistrate's office." — `campaign/setting/governance-and-guilds/city-watch.md:61`
- Governance, Code Legal: "His Notable Figures page and the **Stingblade** event call him a magistrate, but the published adventure gives him no magistrate's title (campaign-only; see GM Notes)." — `campaign/setting/governance-and-guilds/code-legal-and-magisters.md:41`
- The current Barnibus Notable Figures page does not say "magistrate" (a Grep of `02-barnibus-blastwind.md` returns no match; line 25 is quoted in A3).
- Higher-ranked: the adventure (no title). The voice doc is the outlier. Not settled.

**D4. Barnibus's species (affects Connections; not a Saeth fact)**
- "Illuskan human" in the Barnibus page: `campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md:6`
- Alexandrian: "Barnibus — a soft-spoken, meticulous dwarf mage in an ink-stained coat" — `sources/Act_III_Arc_D.md:137`
- Fireball journal: "meticulous Illuskan human mage" — `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:36`
- Higher-ranked: the campaign's Barnibus page and the quest journal (Illuskan). The Alexandrian line is remix text. Not Saeth's page to settle.

**D5. Stat block label**
- Summary, current: "Stat block: **Warrior Veteran**." — `03-saeth-cromley.md:5`
- Stale, quest design note: "Saeth Cromley's Notable Figures page lists the old **Veteran** stat block" — `campaign/quests/faction-events/lords-alliance/m04-the-archer-above/design-notes.md:28`
- Stale, Harpers notes file: "carries the 2014 "Veteran" block" — `docs/plans/harpers-out-of-scope-notes.md:838`
- Adventure has "veteran" with changes and no CR (`sources/adventure-wdh.json:32580`). Wiki CR 3 (wiki line 58).
- Higher-ranked for the label: the mechanics reference (`docs/plans/harpers-mechanics-reference.md:571`) gives "Warrior Veteran | 3". The current page matches it.

**D6. Retirement date**
- Wiki: "in the early 1490s [[DR]]" — wiki line 62.
- No other source dates the retirement. The adventure gives no date.

**D7. "Commander" (parenthesis on the page)**
- Page, Relationships: "(confirmed rank; not Watch Commander despite some in-text references)" — `03-saeth-cromley.md:27`
- Organization page: "**The Commander and the Open Lord:** The Commander of the Watch reports to the Open Lord (*Dragon Heist*, 5e), and no source names the Commander in 1492 DR." — `campaign/setting/organizations/11-open-lords-watch.md:42`
- No source found calls Cromley "Commander." The "in-text references" the page mentions are not identified in any file searched.

**D8. "Partner" versus "friend"**
- Wiki: "Saeth had a working partnership with Barnibus." — wiki line 68
- Barnibus page: "the exclusive professional partner of Saeth Cromley (his only real friend)" — `campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md:25`
- Adventure: "confiding only in {@creature Saeth Cromley|wdh}" — `sources/adventure-wdh.json:31774`
- Not a conflict in facts. The adventure does not say "friend" or "only friend".

---

## E. Stale lines in other files (not edited) and routed quest references

**E1. Stale or conflicting lines in other files**
- `campaign/quests/faction-events/lords-alliance/m04-the-archer-above/design-notes.md:28`: "Saeth Cromley's Notable Figures page lists the old **Veteran** stat block and should read **Warrior Veteran**." (page now reads Warrior Veteran)
- `docs/plans/harpers-out-of-scope-notes.md:838`: "Saeth Cromley's page (`city-officials/03-saeth-cromley.md`) carries the 2014 "Veteran" block." (stale)
- `docs/plans/harpers-out-of-scope-notes.md:607`: "Fireball ev-01:37 has Saeth Cromley as an active Watch sergeant; his Notable Figures page and Harper M4/M5 have him retired." (the quest line is now line 36)
- `campaign/gazetteer/waterdeep/castle-ward.md:66`: "Saeth Cromley drinks in the sergeants' room most afternoons." (verb; D2)
- `docs/plans/setting-compendium-pass3-closeout.md:84`: "Cromley is retired on his page and in the adventure appendix but "Sergeant Cromley" arrives with twenty constables in `fireball/ev-01-the-fireball.md:37`" (line now 36; unresolved in the user list)
- `campaign/quests/act-ii/fireball/overview.md:26`: "- **Saeth Cromley** (City Watch) — sergeant directing constable canvass; has nothing to share and does not try" (labels him City Watch, not retired; quest file)

**E2. Routed quest references (quest-time; the day-one page must not restate them)**
- `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:36` (arrival with twenty constables; see D1); `:79` ("**Sergeant Cromley** directs the constable canvass. He has nothing useful to share and does not try."); `:88` ("A character who knows *Speak with Dead* can attempt entry to the Watch station or mortuary with DC 13 Persuasion (Barnibus or Cromley).")
- `campaign/quests/act-ii/fireball/ev-06-the-death-mark.md:27` ("a Watch badge obtained at the crime scene (from Cromley or Barnibus), grants automatic entry")
- `campaign/quests/act-ii/fireball/overview.md:26`
- `campaign/quests/act-ii/gralhund-villa/ev-01-what-the-factions-say.md:32` ("He offers what he calls the cleanest legal path: a conversation with Sergeant Cromley, who will look the other way for forty-eight hours if the party signs a statement committing to share their intelligence within that window.")
- `campaign/quests/act-ii/gralhund-villa/ev-02-saerdoun-street.md:33` ("Jalester, Cromley, or any city-wise contact can supply the same information without the wait.")
- `campaign/quests/act-ii/gralhund-villa/ev-03b-the-front-door.md:32` ("A Watch credential (available if the party took Jalester's Cromley path in ev-01)")
- `campaign/quests/faction-events/harpers/m04-a-friends-house/ev-01-the-salon.md:130`, `:204` ("Saeth Cromley (Lawful Good, Illuskan Human, he/him) :: a retired Watch sergeant who is bad at parties and good at making strangers talk."), `:206` ("His missing officer is Dalen Voss, who was Corene Wyldath's contact in the Watch. Saeth does not know that, and the party cannot learn it here."), `:343`
- `campaign/quests/faction-events/harpers/m04-a-friends-house/overview.md:52`
- `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-01-the-sleeping-asset.md:9`, `:101` ("He has pulled the file on Dalen Voss, a Watch officer who vanished two months ago.")
- `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-02-the-extraction.md:93`
- `campaign/quests/faction-events/lords-alliance/m04-the-archer-above/ev-01-the-archer-above.md:23`, `:101`-`:121` (the "Saeth Cromley" exploration block), `:223`, `:237`, `:308`; `overview.md:38` and `:84`; `design-notes.md:9`
- `campaign/quests/faction-events/lords-alliance/r10-stingblade/ev-01-stingblade.md:124` ("**Saeth Cromley**, a retired Watch sergeant with a network in the Dock Ward, sits in the Halls of Justice sergeants' room in the afternoons and receives the member there."), `:131`; `design-notes.md:25`
- `campaign/quests/faction-events/order-of-the-gauntlet/s02-savras-past/ev-01-savras-past.md:8`, `:64`-`:98` (including "**The Limit on Saeth**"); `design-notes.md:21`, `:24`
- `campaign/structure/arc-c-fireball.md:45`, `:358`; `campaign/structure/arc-d-gralhund-villa.md:94`
- `sources/Act_III_Arc_D.md:90`, `:129` ("Barnibus Blastwind is not stupid, and Sergeant Cromley has been doing this a long time."), `:137`, `:208`, `:667` ("Cromley visits the characters with this summary.")
- Adventure, quest-time: `sources/adventure-wdh.json:4453`-`4455` (the tavern questioning: "with {@creature Sergeant|WDH} Cromley by his side as a witness and bodyguard" at `:4454`); `:4829`-`4831` ("Sometime afterward, Cromley visits the characters by himself and, as a courtesy, tells them what happened:"); `:6064` ("Barnibus instructs {@creature Sergeant|WDH} Cromley to arrest them for the crime of murdering a noble, which carries a death sentence if they're found guilty.")
- Wiki, quest-time: "In [[1492 DR]],{{WDH-time}} Saeth, together with Barnibus, was called in to investigate the blast that killed ten people in [[North Ward of Waterdeep|North Ward]], including the [[gnome]] [[Dalakhar]]." — wiki line 73. "Later, Saeth accompanied Barnibus when he was called in to investigate the [[Gralhund Villa Bloodbath]]." — wiki line 75.

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes (brief ruling 17).

1. **Origin and birth.** No source gives a birth year, birthplace (beyond the city), parents or age. Wiki age, dob and parents fields are blank (wiki lines 17, 21, 29). Stay consistent with "Illuskan human" (adventure 32580) and "Dock Ward edge he never lost" (voice L46).
2. **How he joined the Watch and how long he served.** No source. Stay consistent with "a retired sergeant of the City Watch" (32573) and the "early 1490s DR" retirement (wiki line 62). Do not give a rank progression.
3. **The retirement: when and why.** Only "until he decided to retire" (wiki line 71) and "now that he's officially retired" (32573). The reason is not given. Stay consistent with "Deep down, he misses the Watch" (page L23) and "nostalgic fondness for the Watch he left behind" (page L15).
4. **How the partnership with Barnibus began.** Only "a working partnership" (wiki line 68) and "confiding only in" (31774). No origin. Stay consistent with "a retired sergeant of the City Watch who assists in many of his investigations" (31774).
5. **Home, residence, family, friends.** No source gives a residence. The Castle Ward line says he and Barnibus "work out of the ward" (`castle-ward.md:9`). The Barnibus page says "his only real friend" (`02-barnibus-blastwind.md:25`). No family is named.
6. **Faith.** None. The Tyr page only groups him with the Halls (`campaign/setting/deities/tyr.md:114`). Do not assign a deity.
7. **Belongings.** The only badge in any source is a quest item (`fireball/ev-06-the-death-mark.md:27`). The adventure gives him no possessions. The Persona's badge line is unsourced.
8. **Personal goals.** The page's Motivations (L17): "Cromley wants to help Barnibus solve cases the investigator cannot handle alone, keep retired life interesting, and coax information from common folk who would never talk to a mage in a tower." No other goal is sourced. Brief ruling 17 needs one to three personal wants: `[design]`.
9. **Losses or grudges.** None sourced. The archer quest says he "misses the Watch more than he admits" (`ev-01-the-archer-above.md:109`). Do not name a dead partner or officer. Dalen Voss belongs to the Harpers' M5 quest and is not a Saeth backstory fact in any source; a Saeth Background should not name him (see E2).
10. **Places he loves.** None sourced beyond the sergeants' room (castle-ward.md:134) and the Dock Ward voice line (L46).

---

## G. Source facts that hint at the figure's inner life (quote exactly; do not contradict)

- Emotions, page L15: "**Emotions.** Cromley most often feels wry amusement, easygoing patience, gruff affection for Barnibus, the old thrill at cracking a case, mild distaste for bureaucracy, and nostalgic fondness for the Watch he left behind." — `03-saeth-cromley.md:15`
- Motivations, page L17: "**Motivations.** Cromley wants to help Barnibus solve cases the investigator cannot handle alone, keep retired life interesting, and coax information from common folk who would never talk to a mage in a tower." — `03-saeth-cromley.md:17`
- Persona, page L23: "Deep down, he misses the Watch but will not admit it, and Barnibus's cases give him an excuse to keep wearing the badge." — `03-saeth-cromley.md:23`
- Adventure: "Though Cromley was once a strict proponent of Watch regulations and dress codes, he has grown a bit lax in both matters now that he's officially retired." — `sources/adventure-wdh.json:32573`
- Archer quest: "He swears cheerfully, and he misses the Watch more than he admits." — `campaign/quests/faction-events/lords-alliance/m04-the-archer-above/ev-01-the-archer-above.md:109`
- Voice, Never: "He never takes a bribe, never talks down to common folk, and never admits he misses the job." — `.claude/skills/character-voices/voices/city-officials.md:53`
- Voice, Sound: "a Dock Ward edge he never lost." — `.claude/skills/character-voices/voices/city-officials.md:46`
- Wiki, Personality: "Once he was very strict about the City Watch's dress code but after his retirement he wore more practical dress." — wiki line 65
- Voice, Quirk: "He scratches his chin before the killer question." — `city-officials.md:51` (the Archer quest uses the same habit at `ev-01-the-archer-above.md:121`: "Saeth scratches his chin and looks at the ceiling for a moment before he answers.")
- Savra quest, trait: "He keeps to what he saw himself, because he has no patience with rumour." — `campaign/quests/faction-events/order-of-the-gauntlet/s02-savras-past/ev-01-savras-past.md:70` (quest-time character trait; the drafter may use the trait, not the scene)

---

## Cross-references (every other file:line where the topic appears)

- `campaign/setting/organizations/11-open-lords-watch.md:8`, `:79`, `:80`, `:139`, `:155`, `:162`
- `campaign/guides/factions/12-open-lords-watch.md:80`, `:95`, `:110`, `:117`, `:135`, `:154`, `:173`
- `campaign/setting/governance-and-guilds/city-watch.md:8`, `:59`, `:61`, `:118`, `:127`
- `campaign/setting/governance-and-guilds/code-legal-and-magisters.md:41`, `:43`, `:90`
- `campaign/setting/the-grand-game/the-grand-game.md:41`, `:57`, `:62`, `:74`
- `campaign/setting/deities/tyr.md:92`, `:114`
- `campaign/gazetteer/waterdeep/castle-ward.md:9`, `:66`, `:133`-`:135`, `:216`, `:233`, `:234`, `:259`
- `campaign/gazetteer/waterdeep/north-ward.md:103`, `:253`
- `campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md:21`, `:25`
- `campaign/setting/notable-figures/city-officials/01-laeral-silverhand.md:6` (affiliation "City of Waterdeep")
- `docs/plans/npc-pronouns-table-group-a.md:14` ("Saeth Cromley | city-officials/03-saeth-cromley.md:5 | he/him")
- `docs/plans/faerun-ethnicities-research.md:347` ("Saeth Cromley | 32580 | `is an Illuskan human {@creature veteran}, with these changes:`")
- Factions and quests listed in E2
- `sources/research/pass3-bundles/city-watch/campaign-hits.txt:172`-`:174` (an earlier copy of the page; superseded)
- `sources/research/pass5-bundles/city-watch/wiki.txt:104`
- `sources/research/pass5-bundles/gralhunds/wiki.txt:427` and `sources/research/pass5-bundles/doom-raiders/wiki.txt:363` contain "Cromley" on a long line that the tool omits. Not quoted; both are Gralhund and Doom Raider aftermath lines and are quest-time.

---

## Not found

- **Birth, family, hometown, age, faith, ward of residence, date of joining the Watch, length of service, date of retirement (beyond "early 1490s DR"), reason for retirement, pets, possessions beyond the badge quest item.** Searched: wiki extract (all fields), adventure entry page 215 and the Barnibus entry page 195, campaign `notable-figures/city-officials/`, governance pages, Castle Ward, Watch org page, Watch Factions Guide, Tyr page, quest folders `harpers/`, `lords-alliance/`, `order-of-the-gauntlet/`, `act-ii/`, `structure/arc-c`, `arc-d`, `sources/Act_III_Arc_D.md`, `sources/research/pass3` and `pass5` city-watch and gralhunds bundles.
- **Saeth's own speech about the Watch or Watch slang sourced to the adventure.** The slang list is in the voice doc and `city-watch.md`; no adventure line.
- **A badge he owns.** Searched "badge" in the Cromley-related files: only `ev-06-the-death-mark.md:27` and the Watch's Jalester badge (`11-open-lords-watch.md:42`, "The adventure's one example is Jalester Silvermane's badge").
- **A "Commander" reference to Saeth** (D7). Searched the campaign and the adventure lines listed above.
- **Any Dalen Voss fact as Saeth backstory.** Only quest files name him (E2).
- **A sword, a fighting style or a weapon for Saeth in a source.** Only the stat-block "veteran" and the bodyguard line (`adventure-wdh.json:4454`).
- **Pronoun or species conflict.** None found.
- **Alexandrian PDFs.** Not text-searched. `sources/7. Other Response Teams.pdf` pp. 57-61 read as images: no Saeth Cromley. The Watch and faction PDFs (`2. Other Factions.pdf`, per `sources/SOURCE_GUIDE.md:254-271`) were not opened for this figure.

## Not readable

- `sources/Other remix files/` `.docx` files cannot be opened. The one that may hold an NPC overview for this figure is `The Waterdavian's Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx` (`sources/SOURCE_GUIDE.md:695`, "Broad NPC reference — use as a secondary source"). It may cover Saeth and was not read.
- Alexandrian PDFs: text not extracted (see Not found).

## Housekeeping

- A stray file, `docs/plans/setting-compendium-research-notes/pass6/city-officials/03-saeth-cromley.md.tmp`, was created by mistake during this run. It contains the single word "placeholder". No delete tool was available. It should be removed before commit.
