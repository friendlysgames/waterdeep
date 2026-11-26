# Pass 6 research notes: Remallia "Remi" Haventree

Page: `campaign/setting/notable-figures/harpers/02-remallia-haventree.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Remi is a major NPC (brief ruling 2): full Personality and Connections apply.
Organization page: `campaign/setting/organizations/01-harpers.md` (Secondary Contact line 54; Key Members line 99)
Factions Guide: `campaign/guides/factions/02-harpers.md`
Voice profile: `.claude/skills/character-voices/voices/harpers.md` (### Remallia "Remi" Haventree, lines 29-43)
Companion notes: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md` (Mirt; Remi appears in its Connections)

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes are shown as plain quotes. `{@creature ...}` tags are left as written. Page fields are given where they exist.
- **Wiki:** the scratchpad extract `wiki-harpers/02-remallia-haventree.txt` reads `NOT FOUND`. The Remallia Haventree wiki page was found in `sources/research/pass5-bundles/harpers/wiki.txt` at lines 862 to 990. Those lines are the wiki source used here, quoted as "wiki line N" of that file. Wiki `<ref>` tags and `{{templates}}` are removed from quotes; the words are otherwise as printed. Edition tags come from the infobox (`alignment5e`, `challenge5e`, `class5e`, `refs5e`) and from each `ref name`. Most sentences print no edition.
- Alexandrian PDF `sources/3. Player Character Factions.pdf` does not name Remi (the Harpers paragraph on PDF p.2 names only the Harpers in general).
- No shell was available. `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **The cause of Arthagast's death conflicts across sources.** The published adventure says "assassins killed her husband" (`sources/adventure-wdh.json:32527`). The wiki says the Cult of the Dragon "killed Lord Arthagast" (wiki line 958). The campaign page uses the adventure's version (`01-mirt.md` is not the source here; see the Persona and Resonance quotes in section A). Adventure wins. The wiki version is listed in D1.
2. **Her stat block does not verify.** The page's Summary says "Mage (with modifications)". The wiki gives CR 9 and "Wizard 13" (wiki lines 922-923). The mechanics reference calls the WDH record "CR 9, no *Remove Curse*" (`docs/plans/harpers-mechanics-reference.md:598`). The adventure's Remi entry (`:32523-32530`) has no stat block. See B3 and D4.
3. **Her Overview is 36 words** (page line 29). The brief limit is 21.
4. **The safe-house keeper and her hidden identity differ between files.** The Harpers Factions Guide says the safe house is "kept by an intermediary" (`02-harpers.md:58`); Appendix B says "maintained by Remallia Haventree" (`sources/Appendix_B_-_Player_Factions.md:144`). The Trollskull tavern event names her as a Harper referral (`campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:90`), which conflicts with the hidden-identity rule (D2).
5. **Two campaign facts come from the wiki, not the adventure:** that she "founded" or "called together" the Council of Waterdeep (wiki line 926; the campaign says "the wiki lists Remallia Haventree among those who called the Council together", `01-harpers.md:29`), and her "Harper councilor" title (wiki line 879). Keep them as wiki-sourced if used.

---

## A. Background facts by theme

### A1. Origin, family, marriage and the death of her husband

**Adventure, Remallia Haventree entry (page 215)**
> "{@creature Remallia Haventree|wdh|Remallia} (Remi to her friends) is the lady of House Ulbrinter and a guiding light for the Harpers in Waterdeep. She became an active force for good in the city after assassins killed her husband, Arthagast Ulbrinter, and destroyed his remains. A sun elf, she has two adult children (a half-elf son named Arthius, who is studying music in Silverymoon, and a half-elf daughter named Serenore, who lives on the Moonshae island of Alaron with her husband and daughter). Lady Haventree retains a handful of loyal servants and spies."
> — `sources/adventure-wdh.json:32527`

**Adventure, the Harper membership list (page 16)**
> "The elf lady of the house, {@creature Remallia Haventree|WDH} (\"Remi\" to her friends), the widow of Lord Arthagast Ulbrinter, is a high-ranking member of the faction."
> — `sources/adventure-wdh.json:1363` (the passage continues with Renaer and Mirt; the list of Harper support is at `:1365`-`:1371`)

**Appendix B (Alexandrian, page-level transcription of the same facts)**
> "**Secondary Contact: Remallia \"Remi\" Haventree.** A precise, guarded elf widow who manages Harper intelligence operations in the North Ward. She lost her husband to political violence and responded by becoming very good at preventing more of it. Harder to read than Mirt, but ultimately more reliable."
> — `sources/Appendix_B_-_Player_Factions.md:64`

**Wiki, Relationships (edition: 5e; `WDH5e-p214-215`)**
> "Lady Remallia was married [[Arthagast Ulbrinter]] of the noble [[Ulbrinter]] family. Together they had two children: [[Arhtius|Arthius]], their son that lived in [[Silverymoon]], and [[Serenore]], their daughter that lived with her family on the island of [[Alaron]] in the [[Moonshaes]]."
> — wiki line 949 (edition 5e, ref `WDH5e-p214-215`)

**Wiki, History (edition: 5e; `WDH5e-p37,215` and `TRoT-p20`)**
> "Remallia was a noble sun elf living in [[Waterdeep]] in [[Ulbrinter Villa]], once the home of her husband Arthagast. At some point she joined the Harpers."
> — wiki line 955 (5e; the ref names are `WDH5e-p37,215` and `TRoT-p20`)

**Wiki, Tyranny of Dragons (edition: 5e; `ToD`, `RoT-p21`, `TRoT-p20`)**
> "During the 1480s DR, the Cult of the Dragon raided Ulbrinter Villa in search of a [[White Dragon Mask|draconic artifact]] stolen by a [[Zhentarim]] agent, and killed Lord Arthagast. Lady Remallia took decisive action in response, methodically and purposefully dismantling the cult's operations with all the resources at her disposal."
> — wiki line 958 (5e; the Council sentences of the same paragraph are in A4)

**Wiki, Personality (edition: 5e; `TRoT-p20`)**
> "The untimely death of her husband at the Dragon Cult's hand served only to increase Remallia's willingness to fight against the forces of evil."
> — wiki line 936 (5e). This is the wiki's cause of death (see D1).

**Wiki, Possessions (edition: 5e; `Upr-p5`)**
> "Among her possessions was a large oil painting of her family, created before her husband's death some time during the mid—to—late 15th century."
> — wiki line 941 (5e; Adventurers League *Uprising* p.5)

**Campaign, Persona (day-one; the cause of death is the adventure's)**
> "**Persona.** To the world, Remi is the lady of House Ulbrinter, a gracious hostess who remembers details about everyone's life. To those she trusts, she runs the Harper operation in Waterdeep from a warded villa, using a silver raven figurine to send messages to her spies. Deep down, assassins killed her husband and destroyed his remains, and every protective measure she takes serves the memory of what it cost her to be careless once."
> — `campaign/setting/notable-figures/harpers/02-remallia-haventree.md:21`

**Campaign, Resonance and Emotions (day-one)**
> "**Resonance.** Remi should inspire trust with her warm attentiveness, admiration for the strength she rebuilt after her husband's murder, and curiosity about the intelligence network she runs from a villa full of loyal servants and protective wards."
> — `02-remallia-haventree.md:11`
> "**Emotions.** Remi most often feels gracious warmth, sharp analytical focus, held grief for Arthagast that surfaces only in private, maternal pride in her children's independence, measured caution toward new operatives, and calm authority that never needs to raise its voice."
> — `02-remallia-haventree.md:13`

**Campaign, north-ward gazetteer (day-one; the "assassins" version)**
> "- The lady of House Ulbrinter and the widow of Lord Arthagast Ulbrinter. She is a gracious hostess who remembers details about everyone's life, and her villa is full of loyal servants and protective wards."
> — `campaign/gazetteer/waterdeep/north-ward.md:108`
> "> - Remi is the de facto Harper leader in Waterdeep and runs the faction's intelligence from the villa, sending messages to her spies by a silver raven figurine. Assassins killed her husband and destroyed his remains, and every precaution she takes comes from that loss."
> — `campaign/gazetteer/waterdeep/north-ward.md:113`

### A2. Her villa and household

**Adventure, Harper support (page 16)**
> "The Harpers have several secret gathering places in Waterdeep, among them Ulbrinter Villa, an estate located on Delzorin Street between Vhezoar Street and Brondar's Way, in the North Ward (just south of Trollskull Alley)."
> — `sources/adventure-wdh.json:1363` (the same paragraph gives Renaer and Mirt; the passage quoted is the first sentence group)

**Adventure, Remi entry (page 215)**
> "Remi holds secret Harper meetings in her villa, which is warded by all manner of spells. She uses a silver raven {@i figurine of wondrous power} to deliver messages to Harper spies scattered throughout the city."
> — `sources/adventure-wdh.json:32528`

**Campaign, north-ward (Ulbrinter Villa; day-one)**
> "An estate on Delzorin Street between Vhezoar Street and Brondar's Way, just south of Trollskull Alley (Dragon Heist). **Remallia Haventree** keeps it as the lady of House Ulbrinter, and her salons are famous for their guest lists."
> — `campaign/gazetteer/waterdeep/north-ward.md:77`

**Campaign, Harpers organization page (day-one; the house and the lodging)**
> "**Headquarters:** Ulbrinter Villa on Delzorin Street in the North Ward is Remi's warded villa and one of the Harpers' secret gathering places. The Harpers also use a rented house at 12 Delzorin Street with five bunks, which an intermediary keeps and which has no link to the villa."
> — `campaign/setting/organizations/01-harpers.md:60` (the paragraph continues with the Skullport hideout and the Harpers' Waterdeep headquarters note)

**Adventure, household (page 215)**: "Lady Haventree retains a handful of loyal servants and spies." (`sources/adventure-wdh.json:32527`, quoted in A1)

### A3. Her role in the Harpers (rank, leadership, reach)

**Campaign, Secondary Contact (day-one; her Harper role is hidden)**
> "**Secondary Contact:** Remallia \"Remi\" Haventree — a precise, guarded elf widow who manages Harper intelligence operations in the North Ward. Harder to read than Mirt but ultimately more reliable. Her faction identity is kept hidden from outsiders, and few in Waterdeep know her as a Harper."
> — `campaign/setting/organizations/01-harpers.md:54`

**Campaign, Key Members (day-one)**
> "- **Remallia \"Remi\" Haventree** — Sun elf noblewoman; de facto Harper leader in Waterdeep, manages intelligence from House Ulbrinter. See the **Remallia \"Remi\" Haventree** page in Notable Figures."
> — `01-harpers.md:99`

**Adventure, Harper support (page 16)**
> "{@creature Remallia Haventree|wdh} (see {@adventure appendix B|WDH|12}) feeds useful bits of information to the adventurers and might also offer them temporary shelter."
> — `sources/adventure-wdh.json:1370`

**Appendix B, the Harper safe house (the keeper differs; see D3)**
> "| 1 | **Watcher** | Recognized Harper. Other members are Friendly by default. Access to the Harper safe house in the North Ward, maintained by Remallia Haventree. New members receive a silver harp-and-crescent pin. |"
> — `sources/Appendix_B_-_Player_Factions.md:144`

**Campaign, Harpers Factions Guide, rank 1 (intermediary keeps the house)**
> "| 1 | **Watcher** | Recognized Harper. Other members are Friendly by default. Silver harp-and-crescent pin. Access to the Harper safe house in the North Ward, kept by an intermediary. |"
> — `campaign/guides/factions/02-harpers.md:58`

**Campaign, Secondary Contact and the Harpers' Draft Notes (the reveal is quest time; the identity is day-one)**
> "> - **Conflicts:** Remi's identity. `trollskull-alley/ev-04-the-factions-come-calling.md:90` has **Remallia Haventree** (Harpers) name a Dock Ward informant by faction referral, while `north-ward.md:83` describes her Harper identity as hidden from the party until she reveals it herself. This page follows the North Ward gazetteer."
> — `01-harpers.md:176`

**Campaign, North Ward, the reveal rule (day-one)**
> "> - The villa is one of the Harpers' secret gathering places, and Remallia's Harper identity stays hidden from the party until she chooses to reveal it. The lodging at 12 Delzorin Street is kept by an intermediary and has no link to the villa."
> — `campaign/gazetteer/waterdeep/north-ward.md:83`

**Campaign, North Ward GM note (day-one)**
> "> - Remi is the de facto Harper leader in Waterdeep and runs the faction's intelligence from the villa, sending messages to her spies by a silver raven figurine. Assassins killed her husband and destroyed his remains, and every precaution she takes comes from that loss."
> "> - She decides whether a party can be trusted with real responsibility, and she reveals herself as a Harper only when she chooses to."
> — `campaign/gazetteer/waterdeep/north-ward.md:113` and `:114`

**Campaign, Harpers Factions Guide, Fronts (day-one)**
> "**Fronts and covers:** Most Harper agents live a double life (Forgotten Realms Wiki, *Harpers*, edition not stated). Remi is the gracious lady of House Ulbrinter, Mirt is a moneylender, Mattrim Mereg is a middling bard at the Yawning Portal, Variel Duskwhisper is a touring musician, and Corvin and Nessa Vayle are servers who come as a pair."
> — `campaign/setting/organizations/01-harpers.md:62`

### A4. The Council of Waterdeep and the Red Wizards (wiki only; the campaign mentions the Council)

**Wiki, lead paragraph (edition: 5e; `TRoT-p12`, `ToD.9`)**
> "Lady '''Remallia Haventree''' ({{Pronounce|reh|MAW|lee|ah|...}}) was [[Waterdhavian]] [[Nobility of Waterdeep|noblewoman]] and an agent of the [[Harpers]] during the late 15th century [[DR]]. She famously founded the [[Council of Waterdeep]], a conciliary body that united the [[Five Factions]] of the [[Sword Coast]] against the emergent threat of the [[Cult of the Dragon]] during the 1480s DR."
> — wiki line 926 (5e; the pronunciation template is cut and the rest of the paragraph is not quoted)

**Wiki, Tyranny of Dragons, the Council sentence (edition: 5e; `TRoT-p20`)**
> "She was the decisive force in uniting the Five Factions in the Council of Waterdeep, founded to combat the menace of the Cult of the Dragon. For her efforts she was chosen as the Harpers' representative on the Council."
> — wiki line 958

**Wiki, Against the Red Wizards (edition: Adventurers League organized play, 5e; not canon for day one)**
> "She worked with her fellow Harpers and a group of adventurers to investigate a Red Wizard safehouse in Waterdeep's [[Waterdeep/Dock Ward|Dock Ward]], then directed them to take information they recovered to [[Candlekeep]] for interpretation."
> — wiki line 961 (refs `UH-p3`, `SS-p3`; organized play, 5e)

**Wiki, illness (edition: Adventurers League, organized play; out of the day-one page; see F7)**
> "During her stay in the city, Remallia became afflicted with some unknown malady. She began to unknowingly harm herself, leaving wounds that created ichor-filled boils upon her skin."
> — wiki line 965 (refs `FW-p9-10`, `FW-p11`; Abeir/Xorvintroth setting; Adventurers League)

**Campaign, Harpers organization page (day-one; the council is in the timeline)**
> "- **The 1480s DR, the Tiamat years:** The Harpers tracked the revived Cult of the Dragon along the Sword Coast, helped gather the free cities' leaders in the Council of Waterdeep and fought at the Well of Dragons (Forgotten Realms Wiki, *Harpers*, edition not stated). The wiki lists Remallia Haventree among those who called the Council together, and the campaign has the Order of the Gauntlet tracking the cult's shipments beside the Harpers in the same years."
> — `campaign/setting/organizations/01-harpers.md:29` (the paragraph continues with the rebuild after 1487 DR)

### A5. Later life: the Eilistraee temple (novel; not day one; see F5)

**Wiki (edition: none printed for the ref; `DM` = *Death Masks*, a novel; `SCAG` ref at the same line)**
> "In the {{YearlinkName|1491}}, the goddess [[Eilistraee]] returned to the Realms near the walls of Waterdeep. In turn, many of the goddess' [[drow]] followers traveled to the City of Splendors ''en masse''. Some of their numbers approached Remallia and requested aid in constructing a temple of Eilistraee in the city. Lady Remallia agreed to provide her support to their cause."
> — wiki line 968 (refs `SCAG` and `DM`, `{{Page needed}}`)

Campaign: no mention of Remi with Eilistraee was found (see Not found).

### A6. Harper work she does (day-one from the campaign; quest-time routed)

**Campaign, Harpers Factions Guide, Gathering information (day-one habit)**
> "- **Gathering information:** Remi sends messages to her spies by a silver raven figurine, Variel's stories carry reports, Corvin passes folded notes, Maxeene listens at hitching posts and Mattrim watches the Zhentarim agents who drink at the Yawning Portal."
> — `campaign/setting/organizations/01-harpers.md:74`

**Campaign, Harpers organization page, Fighting (day-one)**
> "- **Fighting:** The Harpers prefer to send one agent where an army could not go, and the wiki says they take decisive action against cults, thieves' guilds and other forces that terrorize ordinary people (Forgotten Realms Wiki, *Harpers*, edition not stated). Mirt moves with surprising speed and carries hidden weapons. Remi wards her doors and sends her agents, and she fights in person only when the wards fail."
> — `01-harpers.md:75`

**Adventure, the Remi salon (quest-time; the Harpers' Renown 5 mission)**
> "Lady {@creature Remallia Haventree|WDH} is hosting a party at House Ulbrinter, her villa on Delzorin Street, located between Vhezoar Street and Brondar's Way in the North Ward. We have reason to suspect that drow spies have infiltrated the guest list. Attend the party and root out the disguised drow. Dress sharply."
> — `sources/adventure-wdh.json:3873` (the mission row; the next paragraph says "{@creature Remallia Haventree|WDH} (see {@adventure appendix B|WDH|12}) knows of the mission, but it's not revealed to the characters that she's a Harper.")

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, Summary: "> - *Sun elf noblewoman, chaotic good, she/her*. Stat block: **Mage (with modifications)**." — `campaign/setting/notable-figures/harpers/02-remallia-haventree.md:5`
- Campaign, North Ward: "**Remallia \"Remi\" Haventree (Chaotic Good, Sun Elf, she/her)**" — `campaign/gazetteer/waterdeep/north-ward.md:107`
- Campaign, quest tag: "> Remallia Haventree (Chaotic Good, Sun Elf, she/her) :: a gracious noblewoman who remembers every detail of her guests' lives and gives away nothing of her own." — `campaign/quests/faction-events/harpers/m04-a-friends-house/ev-01-the-salon.md:110`
- Wiki: "| alignment5e    = [[Chaotic good]]" (line 921; edition 5e; ref `TRoT-p12`, `WDH5e-p214-215`)
- Adventure: no alignment line in the Remi entry (`sources/adventure-wdh.json:32523-32530`) or in Appendix B line 64.

**Species**
- Campaign: "Sun elf" (Summary line 5; North Ward line 107).
- Adventure: "A sun elf, she has two adult children" (`sources/adventure-wdh.json:32527`).
- Adventure, the pronunciation key: "{@creature Remallia Haventree|WDH}" and "reh-MAW-lee-ah" (`sources/adventure-wdh.json:269` and `:270`).
- Wiki: "| race           = [[Sun elf]]<ref group="note">Remallia is described as a [[moon elf]] in ''[[The Rise of Tiamat]]''.</ref>" (line 877). The wiki's own note says moon elf in *Rise of Tiamat*. The campaign and the adventure say sun elf (D5).

**Pronouns**
- Campaign: "she/her" (Summary line 5).
- Adventure: "Remi holds secret Harper meetings in her villa" (`sources/adventure-wdh.json:32528`); "She uses a silver raven" (same line, "She" after the first sentence). 
- Wiki: "| sex            = Female" (line 876).

**Stat block**
- Campaign, Summary: "Stat block: **Mage (with modifications)**." (`02-remallia-haventree.md:5`)
- Campaign, mechanics reference table: "| Mage with modifications (Remallia) | **Remallia Haventree (WDH record)** | 9 | 13th-level wizard; has *Dispel Magic* and *Banishment*; no *Remove Curse*. |" (`docs/plans/harpers-mechanics-reference.md:579`)
- Campaign, mechanics reference: "*Remallia's list* (WDH): she has *Dispel Magic* and *Banishment* but no *Remove Curse* and no *Greater Restoration*. If Mirt calls her in, she can supply *Dispel Magic* (an automatic Break at 4th level). Cap her at one Break so the party still does the work." (`:347`)
- Campaign, mechanics reference: "| Mirt, Remallia, Vajra | Verified (WDH records) | Mirt CR 9, AC 16, 153 Hit Points; Remallia CR 9, no *Remove Curse*; Vajra CR 13. |" (`:598`)
- Adventure: the Remi entry (`sources/adventure-wdh.json:32523` to `:32530`, page 215) has no CR, class, HP or spells. The wiki's spells and "Dispel Magic" are not in the JSON.
- Wiki, 5e: "| challenge5e    = 9" (line 922) and "| class5e        = {{Class table|edition=5e|[[Wizard]]|13}}" (line 923); ref `TRoT-p12` and `WDH5e-p214-215` (line 924).

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/harpers/02-remallia-haventree.md`. The page has no Background, Personality or Connections section yet.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L5 | "*Sun elf noblewoman, chaotic good, she/her*. Stat block: **Mage (with modifications)**." | Day-one name tag. Stat block source does not verify (B, D4) | section B |
| 2 | L6 | "- **Affiliation:** Harpers" | Day-one. Her Harper role is hidden from outsiders (org page `01-harpers.md:54`), so the label is the cell's, not public | `01-harpers.md:54` |
| 3 | L7 | "- **Featured in:** **Trollskull Alley**, **Fireball!**, **A Friend's House**" | Quest-name list. Omits the Harpers' other events that feature her (`campaign/quests/faction-events/harpers/00-first-meeting/ev-01-first-meeting.md:24`: "Remallia Haventree pays for the lodging on the address card through an intermediary.") | `campaign/quests/faction-events/harpers/` folders |
| 4 | L11 | "**Resonance.** Remi should inspire trust with her warm attentiveness, admiration for the strength she rebuilt after her husband's murder, and curiosity about the intelligence network she runs from a villa full of loyal servants and protective wards." | Day-one. Keep (ruling 3) | `sources/adventure-wdh.json:32527`; `north-ward.md:108` |
| 5 | L13 | "**Emotions.** Remi most often feels gracious warmth, sharp analytical focus, held grief for Arthagast that surfaces only in private, maternal pride in her children's independence, measured caution toward new operatives, and calm authority that never needs to raise its voice." | Day-one. Keep | `sources/adventure-wdh.json:32527` (children, grief) |
| 6 | L15 | "**Motivations.** Remi wants to guide the Harpers effectively in Waterdeep, protect her household and her network from the threats that killed her husband, and determine whether the party can be trusted with real responsibility." | Day-one for the first two clauses. "determine whether the party can be trusted" refers to the PCs. The gazetteer says the same (`north-ward.md:114`). Judgment for the drafter: it is a standing aim, not a quest event | `north-ward.md:114` |
| 7 | L17 | "**Inspirations.** When playing Remi, channel Violet Crawley (*Downton Abbey*), Minerva McGonagall (*Harry Potter*), and Mrs. S (*Orphan Black*)." | Not a fact. Keep | n/a |
| 8 | L21 | "**Persona.** To the world, Remi is the lady of House Ulbrinter, a gracious hostess who remembers details about everyone's life. To those she trusts, she runs the Harper operation in Waterdeep from a warded villa, using a silver raven figurine to send messages to her spies. Deep down, assassins killed her husband and destroyed his remains, and every protective measure she takes serves the memory of what it cost her to be careless once." | Day-one. The cause of death is the adventure's (D1) | `sources/adventure-wdh.json:32527`; `north-ward.md:113` |
| 9 | L23 | "**Morale.** In a fight, Remi would ward the doors and send her agents to handle it. She fights in person only if the wards fail, and by then she has already cast three spells the attackers have not noticed yet." | Encounter register, not a quest event. Keep (ruling 3) | `01-harpers.md:75` ("she fights in person only when the wards fail") |
| 10 | L25 | "**Relationships.** Remi is the widow of Arthagast Ulbrinter, the mother of Arthius and Serenore (both grown and living elsewhere), the de facto Harper leader in Waterdeep, and a colleague of Mirt whose operational styles complement each other." | Day-one. The children's places are the adventure's (`:32527`) | `sources/adventure-wdh.json:32527`; `01-harpers.md:99` |
| 11 | L29 | "The gracious lady of House Ulbrinter, a sun elf noblewoman whose warded villa and precise memory for personal details make her a formidable host and a careful judge of who can be trusted with real responsibility." | Day-one. **36 words** (brief limit 21). Draft a shorter Overview | `sources/adventure-wdh.json:32527`; `north-ward.md:108` |

**Voice profile, quest-time clauses (`harpers.md`, "### Remallia "Remi" Haventree", lines 29-43)**

- Line 30 (tagline): "*A gracious, unhurried hostess whose warmth never slips and whose questions never stop.*" — day-one.
- Line 32 (Sound): "A clear, cultured elven voice, measured and never raised. When she's displeased she becomes quieter and more precise." — day-one.
- Line 33 (Sentence shape): "Complete, well-formed sentences with the occasional subordinate clause. She asks a great many questions, framed as courtesies." — day-one.
- Line 34 (Word choice): "...She addresses the party by name as soon as she has heard it once, and calls her agents \"my dears\" only in private." — day-one. "addresses the party by name as soon as she has heard it once" is a habit, not an event.
- Line 35 (Swearing): "*Never · Plain · n/a.* Never. A single \"damn\" from Remi would stop a room." — day-one.
- Line 36 (Personality in speech): "Warmth is her method. Every kindness is also an assessment. Grief for Arthagast never enters her speech in front of others; if it's mentioned, she thanks the speaker and changes the subject gracefully. Authority comes through in how she makes requests: she never commands, and nobody refuses." — day-one.
- Line 37 (Quirks): "She pours the tea herself. She pauses before answering a question she has decided not to answer, then answers a different one. She touches the silver raven figurine when she's thinking of her network." — day-one.
- Line 38 (Signature phrases): "\"Tell me about yourself; I like to know whom I'm feeding.\" / \"How is your [person they mentioned]?\" / \"We'll speak again when you've had time to think.\"" — day-one.
- Line 39 (Never): "She never swears, never raises her voice, and never admits fear in front of an operative." — day-one.
- Lines 40 to 43 (Sample lines):
  - Greeting (line 41): "You must be the ones Mirt mentioned. Do sit down; the tea is fresh and I've been looking forward to meeting you." — **possible quest-time**. "the ones Mirt mentioned" implies a Mirt referral that happens in a faction mission (Harpers Recruitment or A Friend's House). Flag for the drafter.
  - **Business (line 42): "I'd like you to deliver something for me, and I'd like you not to open it. I'm telling you that so you know I'll know."** — **possible quest-time**: a delivery brief. No day-one source gives a delivery. Flag.
  - **Under pressure (line 43): "The wards will hold for a few minutes yet. Please take the children's door and go now, and don't argue with me."** — **encounter register** (a raid on the villa). Not a quest event as such, but it presumes an attack. Flag.

**Quest-time clauses in the profile:** lines 41, 42 and 43 are flagged. Lines 30 to 39 are day-one.

**Quest-time clauses in the page's Roleplaying Information:** none beyond L15 (see C row 6).

---

## D. Conflicts

**D1. What killed Arthagast (cult or assassins)**
- Adventure: "She became an active force for good in the city after assassins killed her husband, Arthagast Ulbrinter, and destroyed his remains." — `sources/adventure-wdh.json:32527`
- Wiki: "During the 1480s DR, the Cult of the Dragon raided Ulbrinter Villa in search of a [[White Dragon Mask|draconic artifact]] stolen by a [[Zhentarim]] agent, and killed Lord Arthagast." — wiki line 958 (5e)
- Wiki: "The untimely death of her husband at the Dragon Cult's hand served only to increase Remallia's willingness to fight against the forces of evil." — wiki line 936 (5e)
- Campaign (the page and gazetteer): "Assassins killed her husband and destroyed his remains" — `campaign/setting/notable-figures/harpers/02-remallia-haventree.md:21`; `campaign/gazetteer/waterdeep/north-ward.md:113`
- Higher rank: the adventure (published; above the wiki). The campaign agrees with the adventure. The wiki's Cult version is listed here for the orchestrator. Note the campaign also says the Cult was revived in the 1480s (org page `01-harpers.md:29`), so the two can both hold in the campaign if the Cult killed the husband and the assassins were hired by it; no file says so. Leave to the user.

**D2. Whether her Harper identity is visible to the party**
- Campaign, North Ward: "> - The villa is one of the Harpers' secret gathering places, and Remallia's Harper identity stays hidden from the party until she chooses to reveal it." — `campaign/gazetteer/waterdeep/north-ward.md:83`
- Campaign, Harpers organization page: "Her faction identity is kept hidden from outsiders, and few in Waterdeep know her as a Harper." — `campaign/setting/organizations/01-harpers.md:54`
- Campaign, Trollskull Alley event: "The Mistshore information broker is available through faction referral: **Remallia Haventree** (Harpers) or **Yagra Stonefist** (Doom Raiders) name her as a reliable Dock Ward source." — `campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:90`
- Campaign, Trollskull structure doc: "*Filthy Meg.* The Mistshore information broker is introduced during Arc B through faction referral: Remallia Haventree (Harpers) or Yagra (Doom Raiders) names Meg as a reliable Dock Ward source." — `campaign/structure/arc-b-trollskull-alley.md:149` (superseded by the journal)
- Campaign, GM Guide, player-facing table: "| Harpers | **Mirt** (primary); **Remallia \"Remi\" Haventree** (secondary — identity withheld until Mission 4) | Intelligence on faction activity; protection of vulnerable NPCs; exposure of corruption |" — `campaign/guides/gm-guide/player-factions-overview.md:158`
- Adventure: "{@creature Remallia Haventree|WDH} (see {@adventure appendix B|WDH|12}) knows of the mission, but it's not revealed to the characters that she's a Harper." — `sources/adventure-wdh.json:3874` (quest-time; the Harper identity is hidden in the adventure too)
- Higher rank: the gazetteer and the organization page (the campaign) agree. The Trollskull event's referral is the outlier and the Harpers org page calls it a conflict (`01-harpers.md:176`). The page must not say she is a Harper in public.

**D3. Who keeps the Harper safe house in the North Ward**
- Appendix B: "Access to the Harper safe house in the North Ward, maintained by Remallia Haventree." — `sources/Appendix_B_-_Player_Factions.md:144`
- Factions Guide: "Access to the Harper safe house in the North Ward, kept by an intermediary." — `campaign/guides/factions/02-harpers.md:58`
- Campaign, Harpers org page Draft Notes: "> - **Conflicts:** Safe-house keeper. `sources/Appendix_B_-_Player_Factions.md:144` says Remi maintains the North Ward safe house, and `02-harpers.md:58` and `north-ward.md:83` say an intermediary keeps it. The page follows the Factions Guide and the gazetteer." — `campaign/setting/organizations/01-harpers.md:180`
- Higher rank: the Factions Guide and the gazetteer (campaign). The page should say an intermediary keeps the lodging, not the villa.

**D4. Stat block**
- Summary: "Stat block: **Mage (with modifications)**." — `02-remallia-haventree.md:5`
- Wiki: "| challenge5e    = 9" and "| class5e        = {{Class table|edition=5e|[[Wizard]]|13}}" — wiki lines 922-923 (5e)
- Mechanics reference: "| Mage with modifications (Remallia) | **Remallia Haventree (WDH record)** | 9 | 13th-level wizard; has *Dispel Magic* and *Banishment*; no *Remove Curse*. |" — `docs/plans/harpers-mechanics-reference.md:579`
- The adventure has no stat block for her (`sources/adventure-wdh.json:32523-32530`). The "WDH record" the reference cites is not in the JSON.
- Higher rank: none; the three sources agree on CR 9 and a 13th-level wizard in substance. The label "Mage (with modifications)" is the campaign's; "Wizard 13" is the wiki's. Check the printed page 215 before a stat line is quoted.

**D5. Sun elf or moon elf**
- Adventure: "A sun elf, she has two adult children" (`sources/adventure-wdh.json:32527`)
- Wiki: "| race           = [[Sun elf]]<ref group="note">Remallia is described as a [[moon elf]] in ''[[The Rise of Tiamat]]''.</ref>" (line 877)
- Higher rank: the adventure. The campaign uses sun elf.

**D6. Her leadership and the Council (wiki and campaign)**
- Wiki, occupation: "| occupation     = [[Harper]] councilor" (line 879; 5e)
- Wiki, lead: "She famously founded the [[Council of Waterdeep]], ..." (line 926)
- Campaign, Harpers org page: "The wiki lists Remallia Haventree among those who called the Council together" (`01-harpers.md:29`)
- Campaign, the NF Relationships and the Harpers Key Members: "de facto Harper leader in Waterdeep" (`02-remallia-haventree.md:25`; `01-harpers.md:99`)
- Campaign, org page Structure: "It names no High Harper above the city cell" (`01-harpers.md:48`, quoted from the org page's Structure paragraph: "The campaign keeps that looseness. It names no High Harper above the city cell, refers to the High Harpers only as a body to which a senior member can appeal (`campaign/guides/factions/02-harpers.md`), and gives the local lead to two people.")
- Higher rank: the campaign (the local lead is given to two people, Mirt and Remi). The wiki's "councilor" and "founded" are not used as day-one facts without a wiki tag.

**D7. Harper rank: "high-ranking" (adventure) and "agent" (wiki)**
- Adventure: "is a high-ranking member of the faction." (`sources/adventure-wdh.json:1363`)
- Wiki: "and an agent of the [[Harpers]] during the late 15th century [[DR]]." (line 926)
- Higher rank: the adventure. The campaign says "de facto Harper leader".

**D8. Her husband's remains and the villa's owner**
- Wiki: "Remallia was a noble sun elf living in [[Waterdeep]] in [[Ulbrinter Villa]], once the home of her husband Arthagast." (line 955). The wiki's "once" suggests the villa was not hers at the time it was written. The adventure and the campaign call the villa hers and call her "lady of House Ulbrinter" (`sources/adventure-wdh.json:32527`; `north-ward.md:77`). Campaign wins.

**D9. Eilistraee temple (wiki novel line; not in campaign)**
- Wiki line 968 (A5). The campaign does not mention it. Not a conflict; flagged as unused.

---

## E. Stale lines in other files (do not edit) and routed quest references

**E1. Stale or conflicting lines in other files**
- `campaign/gazetteer/waterdeep/north-ward.md:83` and `campaign/setting/organizations/01-harpers.md:54` agree with the campaign's hidden identity. The Trollskull event at `ev-04-the-factions-come-calling.md:90` and the structure doc `arc-b-trollskull-alley.md:149` and `:294` conflict (D2).
- `campaign/guides/gm-guide/player-factions-overview.md:158` names "identity withheld until Mission 4". The Harpers Factions Guide puts **A Friend's House** at the 5th-level mission row (`02-harpers.md:71`). Mission 4 in the quest folders is `m04-a-friends-house`. Consistent by folder number; the GM Guide's "Mission 4" means the folder.
- `campaign/quests/faction-events/harpers/00-first-meeting/design-notes.md:23`: "...names Remallia Haventree as a Harper referral for Filthy Meg, which breaks the hidden-Remi rule." (the Harpers' own note on the Trollskull event; agrees with D2)
- `sources/Appendix_B_-_Player_Factions.md:144` (D3).
- `campaign/structure/arc-b-trollskull-alley.md:149` (D2).

**E2. Routed quest references (quest-time facts; the day-one page must not restate them)**

The Remi-facing quest events and their line counts (from Grep for `Remallia|Remi\b|Haventree` in each folder):
- `campaign/quests/faction-events/harpers/m04-a-friends-house/ev-01-the-salon.md` (44 lines; the salon, the guest list, Erystian Demarne, the "Is Remallia one of us?" box at `:70`)
- `campaign/quests/faction-events/harpers/m04-a-friends-house/ev-03-the-confrontation.md` (41 lines; "Report to Mirt and Remallia at 09:00 and learn what Remallia is." at `:10`; "Remallia has known from the start who the guest was, and Mirt asked her to wait until the morning to say what she is." at `:21`)
- `campaign/quests/faction-events/harpers/m04-a-friends-house/overview.md` (13 lines); `ev-02-the-tail.md` (6)
- `campaign/quests/faction-events/harpers/00-first-meeting/ev-01-first-meeting.md:24`: "> - Remallia Haventree pays for the lodging on the address card through an intermediary. Nobody in this Event names her as a Harper."
- `campaign/quests/faction-events/harpers/00-first-meeting/design-notes.md:13`: "The lodging at 12 Delzorin Street is kept by an intermediary, because the organization page hides Remallia's Harper role until **A Friend's House**."
- `campaign/quests/faction-events/harpers/m04-a-friends-house/design-notes.md:11`: "Remallia's role is revealed in the study at nine, not in the middle of the dinner."
- `campaign/quests/faction-events/harpers/m04-a-friends-house/ev-03-the-confrontation.md:25`: "Remallia opens her study on request and keeps the other guests in the salon, while on the bridge and on Swords Street there is no one else about."
- `campaign/quests/act-ii/fireball/ev-02-the-house-of-inspired-hands.md:93`: "2. **Faction intelligence.** Any faction contact can identify \"nimblewright\" from witness descriptions and direct the party to the Gond temple. Harpers fastest (Remallia knows the high priest personally)."
- `campaign/quests/act-ii/fireball/ev-01-the-fireball.md` (1 line; Mirt-led; Remi not named by the Grep count), `campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:90` (D2)
- `campaign/structure/arc-c-fireball.md:121`: "- **Faction Intelligence.** Any faction contact can identify \"nimblewright\" from the witness descriptions and direct the party to the Gond temple. Harpers are fastest — Remallia Haventree knows the high priest personally."
- `campaign/structure/arc-b-trollskull-alley.md:149` and `:294` (D2)
- Harpers mission and rank events (routed; counts from Grep): `r03-harpshadow`, `r10-brightcandle`, `r25-wise-owl`, `r50-high-harper`, `s01-the-cell-is-compromised`, `m05-the-sleeping-asset`, `m06-the-stones-other-master` (the Remi lines in each are quest-time).
- Adventure, quest-time (not day-one): `sources/adventure-wdh.json:1370` (day-one support; see A3), `:2974` ("Renaer can set up meetings with {@creature Mirt|WDH}, {@creature Remallia Haventree|WDH} (see {@adventure appendix B|WDH|12} for both)..."; a Renaer scene, not a fixed event), `:7646` ("Two Harper {@creature spy||spies} sent by {@creature Remallia Haventree|WDH} (see {@adventure appendix B|WDH|12}) appear on the scene."), `:7742` and `:7743` ("If the characters return to the theater, {@creature Remallia Haventree|WDH} ... waves them over"), `:9028` (the Pink Flumph actress reports to Remi; "If Remallia learns the location of the Vault of Dragons, she sees that the information reaches the Lords of Waterdeep by conveying it to {@creature Mirt|WDH}."), `:9133` and `:9143` (the Blood Wedding theater; "Looking on from the back row is {@creature Remallia Haventree|WDH} ..., a member of the Harpers who suspects Agorn of being a high-ranking Zhent.")
- Appendix C (Alexandrian, quest-time): `sources/Appendix_C_-_Player_Faction_Missions.md:328` ("Lady Remallia Haventree is hosting a party at House Ulbrinter, her villa on Delzorin Street between Vhezoar and Brondar's Way in the North Ward."), `:341` ("Remallia Haventree stands near the window — a precise, composed elven woman in grey and silver, hair swept back, watching the room with the patient attention of someone who knows exactly where all the pieces are."), `:344`, `:376`, `:385` ("Every party member who attended receives 200 gp from Remallia after the event — delivered the following morning by paper bird with a note that says simply: *Well done.*").
- Appendix D (Alexandrian): `sources/Appendix_D_-_Running_the_Tavern.md:647`: "**Faction Note:** Harper-adjacent. Mattrim is not a formal Harper agent but he feeds Remallia Haventree information through Mirt's network."
- Trollskull guide: `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md` (not read; Grep matched Mirt only)

---

## F. Gaps a Background needs that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

**F1. Birth year, age, home before marriage, parents, her own family.** No source gives any of these. The wiki's `age` (line 880), `dob` (line 885), `parents` (line 893) and `siblings` (line 895) are blank. She is a "noble sun elf" (wiki line 955) and "A sun elf" (adventure `:32527`). The wiki says she has "aged considerably during a few short decades in her life" (line 931; ref `Upr-p5`). Do not give her a birth year.

**F2. How she came to the Harpers.** Only "At some point she joined the Harpers." (wiki line 955, ref `TRoT-p20`). Do not give a date or a sponsor.

**F3. When and how Arthagast died.** The adventure says "assassins killed her husband" (`sources/adventure-wdh.json:32527`). The wiki says the Cult killed him "during the 1480s DR" (line 958). The campaign has no date. The Cult's revival in the 1480s is in the campaign's timeline (`01-harpers.md:29`). Any date must be `[research]` and must sit inside the 1480s.

**F4. Her marriage and the two children's lives.** The adventure gives the children's places: Arthius "is studying music in Silverymoon" and Serenore "lives on the Moonshae island of Alaron with her husband and daughter" (`sources/adventure-wdh.json:32527`). Names of the husband and daughter are not given; do not name them (brief ruling 17: a nameless relative is fine). The wiki's Arthius and Serenore lines (line 949) match.

**F5. Her later religious involvement.** The wiki says she supported a temple of Eilistraee in 1491 DR (wiki line 968, ref `DM`, a novel). The campaign does not mention it. Edition and novel-only status must be tagged. The campaign's Eilistraee page is not checked (not in Grep results for Remi). Do not put it on the day-one page without `[research]`.

**F6. Faith and magic.** The wiki says "She was at the very least proficient in [[divination]] magic." (wiki line 946, ref `Upr-p5`). The mechanics reference gives her "Dispel Magic" and "Banishment" (`docs/plans/harpers-mechanics-reference.md:347`, WDH record). No faith is given in any source. The campaign's Morale line (`02-remallia-haventree.md:23`) describes her spells in a fight.

**F7. The illness and the Xorvintroth lookout (organized play).** The wiki says "During her stay in the city, Remallia became afflicted with some unknown malady." (wiki line 965; Adventurers League *Frozen Whispers*). The stay was in Icewind Dale (Abeir-era necropolis, `wiki line 963`). Not a campaign fact; do not use on day one.

**F8. Her house, her servants and the household staff.** The adventure: "Lady Haventree retains a handful of loyal servants and spies." (`:32527`). The Appendix C: "Remallia's household has no guards beyond two Guards" is in the mechanics reference (`docs/plans/harpers-mechanics-reference.md:237`). Names of servants: none. Do not name a steward.

**F9. Her reasons for the work beyond Arthagast.** The campaign's Motivations (`02-remallia-haventree.md:15`) and the wiki's "The untimely death of her husband at the Dragon Cult's hand served only to increase Remallia's willingness to fight against the forces of evil." (wiki line 936). The wiki also says "She understood the threats that faced the Realms, but understood the caution of her fellow Harpers." (line 936). Any personal goal beyond these is `[design]` (ruling 17) and may not reveal a secret or change the Grand Game.

**F10. Her appearance.** The wiki: "Remallia had distinctly bronze-colored skin." (line 931; ref `UH-p16`, Adventurers League). Adventure: no description. Campaign: none (the NF page has none). The skin tone is wiki-only and organized-play; use `[research]` if used.

**F11. The painting, the tea and the kettle.** Wiki: "Among her possessions was a large oil painting of her family, created before her husband's death..." (line 941) and "She was rather fond of ticklemint tea, which she served in silver kettle with porcelain teacups." (line 943). The campaign voice profile says "She pours the tea herself." (`harpers.md:37`). The painting and the ticklemint tea are wiki-only.

**F12. Her children's pride and her grief.** The campaign: "maternal pride in her children's independence" (`02-remallia-haventree.md:13`) and "held grief for Arthagast that surfaces only in private" (`:13`). The adventure's children-living-elsewhere (`:32527`). No source gives a memory or a place for the grief; any is `[design]`.

**F13. The party's testing.** The adventure's A Friend's House mission has her wait for the morning: campaign `ev-03-the-confrontation.md:21` ("Remallia has known from the start who the guest was, and Mirt asked her to wait until the morning to say what she is.") and `design-notes.md:17` (Appendix C says Remallia does not know why the party is invited. She does, and she waits for the morning.). This is quest time (see E2).

---

## G. Source facts that hint at the figure's inner life (for the backstory; do not contradict)

- "She became an active force for good in the city after assassins killed her husband, Arthagast Ulbrinter, and destroyed his remains." — `sources/adventure-wdh.json:32527`. (Her public work began after the loss.)
- "Deep down, assassins killed her husband and destroyed his remains, and every protective measure she takes serves the memory of what it cost her to be careless once." — `campaign/setting/notable-figures/harpers/02-remallia-haventree.md:21`. (The guilt about carelessness.)
- "She lost her husband to political violence and responded by becoming very good at preventing more of it." — `sources/Appendix_B_-_Player_Factions.md:64`.
- "The untimely death of her husband at the Dragon Cult's hand served only to increase Remallia's willingness to fight against the forces of evil." — wiki line 936 (5e). (The wiki's version of the same loss; see D1.)
- "Among her possessions was a large oil painting of her family, created before her husband's death..." — wiki line 941 (5e; `Upr-p5`).
- "She was rather fond of ticklemint tea, which she served in silver kettle with porcelain teacups." — wiki line 943 (5e; `Upr-p4`, `Upr-p5`).
- "Not one to open dialogue, Remi let others speak first before saying her piece." — wiki line 938 (5e; `UH-p16`, `SS-p18`).
- "Lady Remallia was honest and friendly. She understood the threats that faced the Realms, but understood the caution of her fellow Harpers." — wiki line 936 (5e; `TRoT-p12`).
- "Remi holds secret Harper meetings in her villa, which is warded by all manner of spells." — `sources/adventure-wdh.json:32528`.
- "Remi is the de facto Harper leader in Waterdeep and runs the faction's intelligence from the villa, sending messages to her spies by a silver raven figurine." — `campaign/gazetteer/waterdeep/north-ward.md:113`.
- "Grief for Arthagast never enters her speech in front of others; if it's mentioned, she thanks the speaker and changes the subject gracefully." — `.claude/skills/character-voices/voices/harpers.md:36`.
- "She touches the silver raven figurine when she's thinking of her network." — `harpers.md:37`.
- Quest-time (not day-one; shows a trait): "...a member of the Harpers who suspects Agorn of being a high-ranking Zhent. She has been watching him for a while now, hoping to identify other Zhentarim leaders in Waterdeep." — `sources/adventure-wdh.json:9133`. Routed to the Blood Wedding/Stone sequence.
- Quest-time (shows a trait): "Remallia steps between the party and the guests before a second attack lands. She does not fight a guest in her own house." — `docs/plans/harpers-mechanics-reference.md:221`.

---

## Cross-references (the Remi topic in other files)

The Grep for `Remallia|Remi\b|Haventree|Ulbrinter|Arthagast|Arthius|Serenore|Alaron` across `campaign/` returns about 70 lines. Day-one lines are quoted above. The quest-time lines are listed in E2 by file.

| File | Lines (approx.) | Relevance |
|---|---|---|
| `campaign/setting/organizations/01-harpers.md` | 9 Remi lines (`:23`, `:29`, `:54`, `:60`, `:62`, `:74`, `:75`, `:99`, `:176`, `:180`) | Day-one; quoted above |
| `campaign/guides/factions/02-harpers.md` | 4 (`:58`, `:71`, `:82`) | Quoted above |
| `campaign/gazetteer/waterdeep/north-ward.md` | 19 (Remi and Ulbrinter) | `:76`-`:83` and `:107`-`:114` quoted above |
| `campaign/setting/notable-figures/independents-allies/02-renaer-neverember.md:25` | 1 | "...a Harper-adjacent ally of Mirt and Remi Haventree, ..." |
| `campaign/setting/notable-figures/city-officials/01-laeral-silverhand.md` | 0 Remi lines | (Laeral's page names Mirt only) |
| `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md` | 0 Remi lines | (Remi not named) |
| `campaign/setting/history/` | 0 Remi lines | |
| `campaign/structure/arc-b-trollskull-alley.md:149`, `:294` | 2 | D2 |
| `campaign/structure/arc-c-fireball.md:121` | 1 | E2 |
| `campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:90` | 1 | D2 |
| `campaign/quests/act-ii/fireball/ev-02-the-house-of-inspired-hands.md:93` | 1 | E2 |
| `campaign/quests/faction-events/harpers/` (m04, 00-first-meeting, r-events, s01) | about 60 | Quest-time; E2 |
| `campaign/guides/gm-guide/player-factions-overview.md:158` | 1 | D2 |
| `campaign/guides/trollskull-manor/` | 0 Remi lines (Mirt only) | |
| `docs/plans/harpers-mechanics-reference.md` | 7 Remi lines (`:11`, `:221`, `:237`, `:347`, `:579`, `:598`) | D4, F8 |
| `sources/adventure-wdh.json` | 14 Remi lines (`:269`, `:270`, `:1363`, `:1370`, `:2974`, `:3873`, `:3874`, `:7646`, `:7742`, `:7743`, `:9028`, `:9133`, `:9143`, `:32523`, `:32527`, `:32528`) | A, B, E2 |
| `sources/Appendix_B_-_Player_Factions.md` | 4 (`:64`, `:144`, `:147`, `:167`) | D3; quoted above |
| `sources/Appendix_C_-_Player_Faction_Missions.md` | 9 | E2 (quest-time) |
| `sources/Appendix_D_-_Running_the_Tavern.md:647` | 1 | E2 |
| `sources/research/pass5-bundles/harpers/wiki.txt:459`, `:463`, `:862-990` | 3 | `:463` is the wiki's "Remallia Haventree, a Waterdhavian noblewoman who help call together the Council of Waterdeep and led numerous missions for the Harpers in the late 15th century." (5e, refs `RoT-p20`, `WDH5e-p215`) — the wiki list of Harper members. `:862-990` is the page quoted in A and D. |

---

## Not found

- Searched for: Remi's birth year, age, parents, siblings, home before marriage, the date of Arthagast's death, her date of joining the Harpers, her sponsor, her faith, her appearance in the campaign: `campaign/` (Grep for `Remallia|Remi\b|Haventree|Ulbrinter|Arthagast|Arthius|Serenore|Alaron`), `sources/adventure-wdh.json` (Grep for the same terms), `sources/*.md` (Grep), `sources/research/` (Grep for `Remallia|Haventree|Ulbrinter`). No match gives any of these except the wiki lines quoted above.
- Searched for an Eilistraee link to Remi in the campaign: `campaign/setting/deities/` Grep for `Remallia|Remi\b|Haventree` returned no Eilistraee page. The only Eilistraee link is wiki line 968.
- The Remi wiki scratchpad `wiki-harpers/02-remallia-haventree.txt`: NOT FOUND (the scratchpad file contains `NOT FOUND`). The wiki page used is `sources/research/pass5-bundles/harpers/wiki.txt:862-990`.
- Stat block in the adventure: none (`sources/adventure-wdh.json:32523-32530`). The mechanics reference's "WDH record" is not in the JSON; the printed page 215 was not checked.
- Remi's pronouns in the adventure as a direct tag: none; the pronouns come from "her villa" and "She uses" in `:32528` and the NF page's `she/her`.
- Remi's alignment in the adventure: none.
- The Alexandrian PDF `sources/3. Player Character Factions.pdf` names no Remallia (read at PDF pp.1-3, printed pp.23-25).
- The Trollskull guide `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md` was not checked for Remi (the Grep for Mirt matched it; the Remi Grep was not run on it).

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. `sources/SOURCE_GUIDE.md` returned no Remi line with a `.docx` name (the Grep for `Harper|Haventree|Mirt` returned lines 29, 167, 172, 598, none naming a `.docx`).
- `sources/3. Player Character Factions.pdf`: read as images, not `pdftotext`. The Remi search of that PDF is a visual check of printed pp.23-25 only.
- `campaign/quests/faction-events/harpers/` files were read through Grep only; quotes from them are exact Grep output.
