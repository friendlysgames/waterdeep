# Pass 6 research notes: Soluun Xibrindas

Page: `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR. Campaign-start lore only. Quest-time sentences are listed in section C and routed.
Model format: `docs/plans/setting-compendium-research-notes/pass6/cassalanters/04-osvaldo-cassalanter.md`
Voice profile: `.claude/skills/character-voices/voices/bregan-daerthe.md`, "### Soluun Xibrindas" (heading line 44; tagline line 45; sample lines to line 58).
Companion notes: `docs/plans/setting-compendium-research-notes/pass6/bregan-daerthe/01-jarlaxle-baenre.md`

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes are shown as plain quotes. Tags such as `{@creature ...}` are left as written.
- Wiki: the scratchpad extract `wiki-bregan-daerthe/02-soluun-xibrindas.txt` was read in full (96 lines). Cited as "wiki extract line N" (that file's lines). The citation keys are *Waterdeep: Dragon Heist* 5e (WDH5e-p15, p.34, p.40, p.141-142, p.202, p.211); the extract gives no other edition.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. `sources/9. Lair – Sea Maidens Faire.pdf` was read as page images (printed pp.73-75). Those quotes are transcriptions. Check with `pdftotext -layout` before any quote goes into prose. `sources/1. The Villains.pdf` and `sources/5. Faction Outposts.pdf` were read and do not name Soluun.
- The Appendix C Dock Ward mission and the Appendix B Bregan entry are markdown and were read directly.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **The stat block conflicts.** The page (line 5) says "Stat block: **Drow Gunslinger**." The Doom Raiders mission and its design notes use the 2024 **Scout** for Soluun (`campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/overview.md:60`). The Alexandrian appendix uses "**Drow Gunslinger**" (Appendix C line 1213). The published adventure gives a drow gunslinger "with these changes" (`sources/adventure-wdh.json:32048`). Decide which block the page names (D1).
2. **The Lolth shrine is dropped by the campaign.** The adventure puts Soluun "worshiping before a shrine of Lolth" (`sources/adventure-wdh.json:26345`) and the wiki says he "prayed to Lolth" (wiki extract line 65). The campaign's U3 entry has no shrine (`campaign/locations/sea-maidens-faire/05-scarlet-marpenoth.md:40`) and the Lolth page drops it (`campaign/setting/deities/lolth.md:68`). Keep the campaign's rule (D2).
3. **The disownment has three wordings and a forged item has three names.** The page says "disowned for unsanctioned Dock Ward murders" (line 21). The Dock Ward gazetteer says "killing without orders" (`dock-ward.md:38`). The Killer's Fate event says the disownment was "Jarlaxle's invention" (`s05-the-killers-fate/ev-01-the-killers-fate.md:18`). The forged item is a "token" (`dock-ward.md:38`, `07-bregan-daerthe.md:127`), "identification" (page line 25 and Overview), and a "silver disc" that is "a forgery" (`s05 ev-01:18`). Pick one wording for the day-one cover (D3).
4. **The Nar'l page has unreviewed design text about Soluun.** The Nar'l page (`campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md`) adds `[design]` lines that make Soluun carry Nar'l out of a burning house (lines 43, 154, 157) and give Soluun a role in the raiding parties (line 153). These are not sourced beyond "wiped out long ago" (`sources/adventure-wdh.json:32323`). The Soluun Background must match them or flag the difference (section A2 and D5).
5. **Morale (line 23) and the Draft Notes of the Killer's Fate are quest-time.** The Morale line's "the next" and "hasn't yet decided" clauses are day-one. The Killer's Fate event (`s05`) says Jarlaxle "has decided to make the cover story true" (line 20), which is not day-one. Route it (C).

---

## A. Background facts by theme

### A1. Origin and the family that was lost

**Adventure, the family and the surviving brothers (Nar'l's entry, appendix B page 211)**
> "{@creature Xanathar|WDH}'s advisor is a nervous and conniving male drow named {@creature Nar'l Xibrindas|wdh}. Nar'l's house was wiped out long ago, but he and his elder brother Soluun survived and joined Bregan D'aerthe. A year ago, Nar'l was given the difficult task of infiltrating the Xanathar Guild and getting as close to the beholder as possible."
> — `sources/adventure-wdh.json:32323` (rest of the passage covers Nar'l's Guild work, the grell and the bargain with Xanathar)

**Wiki extract, the family house (5e, cited WDH p.211)**
> "The family's house was destroyed and only Soluun and his younger brother [[Nar'l Xibrindas|Nar'l]] survived. They decided to join [[Bregan D'aerthe]].<ref name=\"WDH5e-p211\">{{Cite book/Waterdeep: Dragon Heist|211}}</ref>"
> — wiki extract line 68

**Wiki extract, the lead (5e, cited WDH p.15)**
> "'''Soluun Xibrindas''' ({{Pronounce|soh|LOON|_|zeh|BRIN|das|refs=<ref name=\"WDH5e-p4\">{{Cite book/Waterdeep: Dragon Heist|4}}</ref>}}) was one of the top agents of [[Bregan D'aerthe]] in [[Waterdeep]] during the early 1490s [[DR]].<ref name=\"WDH5e-p15\">{{Cite book/Waterdeep: Dragon Heist|15}}</ref>"
> — wiki extract line 62

**History page, the house and the brothers (Founding)**
> "- Nar'l Xibrindas is an example. His house was wiped out long ago, and he and his elder brother Soluun survived and joined the company."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:43`

**Nar'l page, the house (Session 51 draft, `[design]` tag on the Soluun clause; `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md`)**
> "- **Bregan D'aerthe:** The company he joined with Soluun after his house fell. It keeps an asset inside every rival, and Nar'l is the one inside Xanathar's Guild (**Bregan D'aerthe** in Organizations)."
> — `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:42`

> "- **Soluun Xibrindas:** His elder brother and a lieutenant of Jarlaxle. Soluun considers him a weakling and despises him, though he once carried Nar'l out of their burning house `[design]`."
> — `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:43`

**Nar'l page, the Design list (Session 51 draft, unreviewed)**
> "  - Background, early life: a house whose sons were trained to fight and a childhood among the retainers who kept the records; Soluun sent out with the raiding parties as soon as he could carry a blade; Nar'l judged too slight and given to the house archivist, who taught him to read, keep accounts and copy spells; the worn primer of cantrips as the source of his first spells; Soluun reading the arrangement as proof that Nar'l could not fight."
> — `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:153`

> "  - Background, the fall and the years after: a rival house attacking while the raiding parties were away; Soluun coming back, going into the burning hall and carrying Nar'l out through a service passage while the archivist and household died; the primer as the only book saved; the brothers hiring out in Underdark cities (Soluun fighting, Nar'l keeping accounts and casting); neither mentioning the night since and Nar'l never thanking him; Soluun giving Jarlaxle the devotion owed his house, and Nar'l joining as a mage and clerk who copied reports and kept ciphers."
> — `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:154`

> "  - Connections: Soluun carried him out of their burning house."
> — `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:157`

### A2. Training as a killer, from a young age

**Adventure, taught to kill (appendix B page 202)**
> "Soluun has a burning hatred of surface elves and half-elves, having been taught from a young age to kill them as opportunity permits. When not engaged in a Bregan D'aerthe operation, Soluun spends his nights haunting the darkened streets and alleys of Waterdeep, looking for solitary elves or half-elves to pick off. He conceals his nighttime escapades as well as he can, but Jarlaxle, Fel'rekt, and Krebbyg know what he's up to."
> — `sources/adventure-wdh.json:32041`

**Wiki extract, from the earliest days (5e, cited WDH p.202)**
> "Soluun was a fanatical bully totally loyal to Bregan D'aerthe and Jarlaxle. He considered his brother weak for his decision to study [[magic]]. From his earliest days, he hated surface elves and half-elves and when he had free time outside his missions Soluun always tried to kill some solitary elvish individuals.<ref name=\"WDH5e-p202\" />"
> — wiki extract line 71

**Campaign, the Persona (the page, line 21; the day-one habit)**
> "**Persona.** To the world, Soluun is a drow gunslinger of Bregan D'aerthe, disowned for unsanctioned Dock Ward murders. To those he trusts, he is fiercely loyal to Jarlaxle and Bregan D'aerthe, and he considers his brother Nar'l a weakling who turned to arcane magic by way of compensation. Deep down, he was taught from a young age to kill surface elves as opportunity permits, and the habit has become his identity. He despises Lolth and the matron houses that serve her, as the whole band does, and the devotion a drow of the houses would give the Spider Queen he gives to Jarlaxle instead."
> — `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:21`

**Campaign, the Killer's Fate "What Is Actually True" (GM text, day-one truths only)**
> "He kills surface elves and half-elves because he was raised to. For some weeks he hunted them along the Dock Ward waterfront, choosing victims from the audiences of the Seven Masks Theater. Jarlaxle knew and hadn't decided what to do."
> — `campaign/quests/faction-events/bregan-daerthe/s05-the-killers-fate/ev-01-the-killers-fate.md:18` (the first sentence of the same paragraph names him as Nar'l's elder brother and a devoted drow gunslinger; the rest of the paragraph covers the cover story, which is in D3)

**Campaign, the Dock Ward gazetteer (day-one habit)**
> "- A drow gunslinger who has hunted the waterfront for some weeks. He picks an elf or half-elf sailor out of a Seven Masks audience, follows him home for two nights and strikes on the third with a hand crossbow bolt and a curved shortsword. He takes the head and the bolt."
> — `campaign/gazetteer/waterdeep/dock-ward.md:152`

### A3. Service to Jarlaxle and the company

**Campaign, the Overview of Key Members (Organization)**
> "- **Soluun Xibrindas** — Drow gunslinger, neutral evil. Stalks and murders elven and half-elven audience members after shows at the Seven Masks Theater. Jarlaxle is aware and hasn't yet decided what to do. See the **Soluun Xibrindas** page in Notable Figures."
> — `campaign/setting/organizations/07-bregan-daerthe.md:100`

**Campaign, the Dock Ward gazetteer (who he is)**
> "- Soluun hates surface elves and serves Jarlaxle with a zealot's devotion. He is the elder brother of Nar'l Xibrindas, whom he despises. See the Secret for the disownment."
> — `campaign/gazetteer/waterdeep/dock-ward.md:157`

**Campaign, the Factions Guide Lockdown row**
> "| Lockdown | Fel'rekt, Krebbyg, and Soluun deployed together. Jarlaxle intervenes personally, always with an offer rather than a fight. |"
> — `campaign/guides/factions/08-bregan-daerthe.md:122`

**Adventure, the lieutenant (Bregan entry, faction box)**
> "When one or more characters are drow, Jarlaxle has three lieutenants — **Fel'rekt Lafeen**, **Krebbyg Masq'il'yr**, and **Soluun Xibrindas** — shadow the party at a careful distance for several days."
> — `sources/Appendix_B_-_Player_Factions.md:717`

**Adventure, the lieutenants and their guns**
> "\"Zord has drow spies in Waterdeep-{@creature Fel'rekt Lafeen|WDH}, {@creature Krebbyg Masq'il'yr|WDH}, and {@creature Soluun Xibrindas|wdh}. All carry Lantanese firearms.\""
> — `sources/adventure-wdh.json:23035`

**Adventure, the faction box (the drow gunslingers and Zord)**
> "In the magical guise of a flamboyant Illuskan captain named Zardoz Zord, Jarlaxle oversees things from the {@i Eyecatcher}, his flagship, and the {@i Scarlet Marpenoth}, a submarine mounted underneath it. He relies on three {@creature Drow Gunslinger|wdh|drow gunslingers}—{@creature Fel'rekt Lafeen|WDH}, {@creature Krebbyg Masq'il'yr|WDH}, and {@creature Soluun Xibrindas|wdh}—to do most of his dirty work in the city."
> — `sources/adventure-wdh.json:1300`

**Adventure, the lieutenants if Jarlaxle is the villain (Xanathar's Lair chapter, the replacement list)**
> "If {@creature Jarlaxle Baenre|WDH} (see {@adventure appendix B|WDH|12}) is the villain, he arrives with three {@creature drow gunslinger|WDH|drow gunslingers} (see {@adventure appendix B|WDH|12}). Replace no-name drow gunslingers with {@creature Fel'rekt Lafeen|WDH}, {@creature Krebbyg Masq'il'yr|WDH}, and {@creature Soluun Xibrindas|wdh} if they are alive and free."
> — `sources/adventure-wdh.json:14782`

**Alexandrian, the Dock Ward "Joining" section (faction appendix, markdown)**
> "When one or more characters are drow, Jarlaxle has three lieutenants — **Fel'rekt Lafeen**, **Krebbyg Masq'il'yr**, and **Soluun Xibrindas** — shadow the party at a careful distance for several days. Characters with a passive Perception of 18 or higher catch glimpses of the surveillance; a DC 15 Wisdom (Insight) check confirms the watchers have a particular interest in drow party members."
> — `sources/Appendix_B_-_Player_Factions.md:717` (the second sentence is the recruitment shadowing and is quoted for the lieutenants' habit; the first is Appendix B's)

### A4. Day and night habits (sourced)

**Wiki extract, the day and night (5e, cited WDH p.34 and p.40)**
> "Soluun, together with [[Fel'rekt Lafeen]] and [[Krebbyg Masq'il'yr]], was tasked by [[Jarlaxle]] with carrying out dirty deeds in the city.<ref name=\"WDH5e-p15\" /> Soluun preferred to act during the day.<ref name=\"WDH5e-p34\">{{Cite book/Waterdeep: Dragon Heist|34}}</ref> At night, Soluun's hobby was killing solitary [[elves]] and [[half-elves]] in the [[Dock Ward of Waterdeep|Dock Ward]].<ref name=\"WDH5e-p40\">{{Cite book/Waterdeep: Dragon Heist|40}}</ref><ref name=\"WDH5e-p202\" />"
> — wiki extract line 65

**Campaign, the first-meeting watch (day shift)**
> "The watchers are Jarlaxle's three lieutenants. Fel'rekt Lafeen and Krebbyg Masq'il'yr shadow the party from dusk until dawn, and Soluun Xibrindas takes the day from shade and doorways. After dark Soluun also hunts elf and half-elf sailors in the Dock Ward on his own account, the subject of the Doom Raiders mission **The Dockside Killer**. Jarlaxle knows and has not decided what to do. Nothing in this Event lets the party connect the two, and Soluun never speaks to anyone."
> — `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:26`

**Campaign, the first-meeting watch (position)**
> "Fel'rekt and Krebbyg work the night in turns, so one of them is always at the mouth of Trollskull Alley or on a roof across from the manor. Soluun takes the day from doorways and awnings on the shaded side of the street."
> — `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:42`

**Campaign, the first-meeting design notes (the day shift)**
> "The lieutenants keep a fixed shift: the pair by night, Soluun by day. Soluun's day watch and his Dock Ward killings are the same man on two schedules, which fits WDH's note that he stays out of the sun."
> — `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/design-notes.md:15`

### A5. The Dock Ward killings and the cover (day-one, with the mark that the event sets)

**Campaign, the Dock Ward gazetteer (Secret, day-one)**
> "- The man killing elf and half-elf sailors off Ship Street is Soluun Xibrindas, a drow gunslinger of Bregan D'aerthe. Jarlaxle's public story is that he disowned Soluun for killing without orders, and the story is a cover. Jarlaxle knows about the murders and has not decided what to do, and Soluun carries a forged Bregan D'aerthe token so that the band can deny him. Nothing in **The Dockside Killer** lets the party learn this."
> — `campaign/gazetteer/waterdeep/dock-ward.md:38`

**Campaign, the Villains page (GM Notes)**
> "- Soluun Xibrindas carries forged Bregan D'aerthe identification, and his public disownment is a cover story. Jarlaxle knows about the Dock Ward murders and has not decided what to do about them."
> — `campaign/setting/villains/jarlaxle.md:116`

**Campaign, the Organization page (GM Notes)**
> "- **Soluun's cover story:** Jarlaxle's public story is that he disowned Soluun for killing without orders. The story is a cover, and Soluun carries a forged Bregan D'aerthe token so that the company can deny him."
> — `campaign/setting/organizations/07-bregan-daerthe.md:127`

**Adventure, the killer's appearance in the published text**
> "\"Zord has drow spies in Waterdeep" — see A3 (the adventure gives no disownment and no forgery for Soluun; the published text has him loyal and killing on his own, `sources/adventure-wdh.json:32040`-`:32041`).

**Campaign, the Operation (the Morale and the playbill; the day-one item)**
> "**Morale.** In a fight, Soluun attacks without hesitation or mercy. He carries a bloodstained Seven Masks Theater playbill for Blood Wedding; he stalks and murders elven and half-elven audience members after shows. Jarlaxle is aware and hasn't yet decided what to do about it."
> — `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:23` (the first sentence is the encounter line; see C)

**Campaign, the Dock Ward gazetteer (the playbill as a clue)**
> "- Hook: the Doom Raiders hunt him in **The Dockside Killer**, and a bloodstained Seven Masks playbill is the clue that points to the theater."
> — `campaign/gazetteer/waterdeep/dock-ward.md:153`

**Appendix C, the playbill (the Dockside Killer mission; Alexandrian, markdown)**
> "**What He Carries.** A bloodstained playbill from the Seven Masks Theater — a performance of *Blood Wedding* that took place several nights ago. A DC 12 Intelligence check connects the Seven Masks Theater to Bregan D'aerthe (the connection is available to characters who have interacted with Jarlaxle or conducted any research on the organization)."
> — `sources/Appendix_C_-_Player_Faction_Missions.md:1217`

### A6. Devotion, and the rejection of Lolth

**Campaign, the Persona (line 21; the same sentence as A2)**
> "He despises Lolth and the matron houses that serve her, as the whole band does, and the devotion a drow of the houses would give the Spider Queen he gives to Jarlaxle instead."
> — `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:21`

**Campaign, the Emotions (line 13)**
> "a zealot's fervor for the band (which, like every member of Bregan D'aerthe, rejects Lolth)"
> — `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:13`

**Campaign, the Lolth page, the standing rule (`deities/lolth.md`)**
> "> - **Soluun Xibrindas:** He \"despises Lolth and the matron houses that serve her, as the whole band does\", and gives Jarlaxle the devotion a drow of the houses would give the Spider Queen (`campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:22`)."
> — `campaign/setting/deities/lolth.md:76` (the page's line 22 cite is the Persona line; the quote in the page is line 21 of the file)

**Campaign, the Dockside Killer (the event's Lolth answer)**
> "If a character has Soluun in hand and asks him about the god of his people, he answers with open contempt for Lolth, since Bregan D'aerthe rejects her."
> — `campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/ev-01-the-dockside-killer.md:343` (quest-time: the event's scene; the rule is day-one)

**Campaign, the Killer's Fate (the captive's disgust)**
> "He never apologizes, never says Lolth's name with anything but disgust, and mentions his brother only as \"the weak one\"."
> — `campaign/quests/faction-events/bregan-daerthe/s05-the-killers-fate/ev-01-the-killers-fate.md:242` (the quest-time half of the paragraph is cut; see C)

**Campaign, the Lolth page's cited faith line (the Dockside first-meeting contempt)**
> "Gods, no. My colleagues left the Spider Queen behind on purpose, and most of them left in a hurry and in a bad temper. You won't find anyone among us with a kind word for her, and I'd advise you not to ask them about her at dinner."
> — `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:379` (Nevercott, not Soluun; the same rule)

**Adventure, the shrine (contradicts the campaign; see D2)**
> "If he has not been encountered and disposed of elsewhere, a {@creature drow gunslinger|WDH} named {@creature Soluun Xibrindas|wdh} (see {@adventure appendix B|WDH|12}) is here, worshiping before a shrine of Lolth. His stateroom has the following features:"
> — `sources/adventure-wdh.json:26345`

**Wiki extract, the prayer (5e, cited WDH p.141-142; conflicts with the campaign; see D2)**
> "Soluun resided on the ''[[Scarlet Marpenoth]]'' ship, where he prayed to [[Lolth]].<ref name=\"WDH5e-p141-142\">{{Cite book/Waterdeep: Dragon Heist|141-142}}</ref>"
> — wiki extract line 65

### A7. Brother and the rivalry with Nar'l

**Adventure, the view of Nar'l (appendix B page 202)**
> "Soluun is a sadistic, fanatical bully who is fiercely loyal to Bregan D'aerthe, and to Jarlaxle in particular. His younger brother, Nar'l, has infiltrated the Xanathar Guild. Soluun considers Nar'l a weakling who turned to arcane magic by way of compensation, and he has never had much faith in his brother or his abilities."
> — `sources/adventure-wdh.json:32040`

**Wiki extract, the contempt for magic (5e, cited WDH p.202)**
> "He considered his brother weak for his decision to study [[magic]]."
> — wiki extract line 71

**Campaign, the Relationships (line 25)**
> "**Relationships.** Soluun is the elder brother of Nar'l Xibrindas (whom he despises), a lieutenant of Jarlaxle (whom he worships), and a serial killer whose disownment by Bregan D'aerthe is a cover story: he carries forged BD identification."
> — `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:25`

**Campaign, the Nar'l page (the brother's view of Soluun; the Nar'l page keeps it)**
> "**Relationships.** Nar'l is the younger brother of Soluun Xibrindas (who considers him a weakling), Jarlaxle's intelligence asset inside Xanathar's Guild, and Xanathar's only advisor, who has a grell bodyguard assigned to execute him at the first sign of treachery."
> — `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:85`

**Adventure, the sending (the brother link)**
> "{@creature Nar'l Xibrindas|wdh} is a {@creature drow mage}. He prepares and casts the {@spell sending} spell whenever he needs to communicate with his brother."
> — `sources/adventure-wdh.json:32331` (the sending is to Jarlaxle in the campaign, see D6)

**Campaign, the Motivations (line 15)**
> "**Motivations.** Soluun wants to kill every surface elf and half-elf he can find without consequences, serve Jarlaxle with absolute loyalty, and prove that his brother Nar'l is the weak one."
> — `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:15`

### A8. Belongings

**Adventure, the kit (appendix B page 202, Game Statistics)**
> "He wears a pair of drow-made {@item boots of elvenkind}. In addition to his weapons, he carries four packets of {@item smokepowder|WDH} (see {@adventure appendix A|WDH|11}) and a pouch containing twenty pistol bullets."
> — `sources/adventure-wdh.json:32053`

**Adventure, the weapon (page 202)**
> "Soluun wields a scimitar instead of a shortsword (it deals slashing damage instead of piercing damage)."
> — `sources/adventure-wdh.json:32052` (conflicts with the gazetteer's "curved shortsword"; see D4)

**Wiki extract, the firearms (5e)**
> "Like his fellows Fel'rekt and Krebbyg, Soluun was equipped with [[Lantanese]] [[firearm]]s.<ref name=\"WDH5e-p132\">{{Cite book/Waterdeep: Dragon Heist|132}}</ref>"
> — wiki extract line 74

**Campaign, the Morale (the playbill; the signature item)**
> "He carries a bloodstained Seven Masks Theater playbill for Blood Wedding" — `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:23`

**Campaign, the silver disc (the Killer's Fate scene; not day-one, see C)**
> "a silver disc on a cord hangs at the open collar of his shirt." — `campaign/quests/faction-events/bregan-daerthe/s05-the-killers-fate/ev-01-the-killers-fate.md:190`

**Campaign, the Dock Ward and the playbill (the Seven Masks Theater)**
> "- Soluun Xibrindas picks his victims from the audience here. See the Secret." — `campaign/gazetteer/waterdeep/dock-ward.md:77`

**Campaign, the Factions Guide Response Team**
> "- *Playbill for the Seven Masks Theater* (Response Team: Soluun Xibrindas)" — `campaign/guides/factions/08-bregan-daerthe.md:137`

**Alexandrian, the stateroom footlocker (PDF transcription, printed p.73 = `sources/9. Lair – Sea Maidens Faire.pdf` PDF p.6)**
> "Area U3 – Soluun's Stateroom: The footlocker contains A Letter from N'arl."
> — `sources/9. Lair – Sea Maidens Faire.pdf` printed p.73 (transcription; the letter is Nar'l's, not Soluun's)

**Alexandrian, the letter's words about Soluun's killing (transcription, printed p.73)**
> "Thank you for the evening at the Seven Masks last tenday. A delightfully bloody affair."
> — `sources/9. Lair – Sea Maidens Faire.pdf` printed p.73 (transcription; Nar'l's letter, see C routing)

### A9. Where he lives and works

**Campaign, the Scarlet Marpenoth stateroom (location journal)**
> "**U3 — Soluun's Stateroom:** Drow gunslinger Soluun Xibrindas, cleaning his weapons. Footlocker: Lantanese diving suit (functions as a *cap of water breathing*; allows underwater breathing for 24 hours, reusable). The suit is the only diving gear aboard."
> — `campaign/locations/sea-maidens-faire/05-scarlet-marpenoth.md:40`

**Alexandrian, the crew roster (transcription, printed p.74)**
> "Soluun Xibrindas (50%)" with "Area U3 – Soluun's Stateroom" in the same table (`sources/9. Lair – Sea Maidens Faire.pdf` printed p.74).

**Wiki extract, the residence (5e, cited WDH p.141-142; see D2)**
> "Soluun resided on the ''[[Scarlet Marpenoth]]'' ship, where he prayed to [[Lolth]]."
> — wiki extract line 65

**Adventure, the stateroom (the page's shrine; see D2)**
> "U3. Soluun's Stateroom" — `sources/adventure-wdh.json:26341` (the entry is the keyed room; the shrine is in the entry text at line 26345)

**Campaign, the Dock Ward gazetteer (the Faire's pier)**
> "- The Seven Masks Theater stands ..." — not quoted; the Seven Masks is Jarlaxle's theater (`campaign/gazetteer/waterdeep/dock-ward.md:75`: "The theater is a Bregan D'aerthe front. Rongquan Mystere is a disguise of Jarlaxle's, and Kreb Sorrush is Krebbyg.")

### A10. Voice (the profile's lines, verbatim source)

The drafter copies the profile into the page. Quest-time and encounter clauses are in section C. Profile lines:
- Tagline, line 45: "*A fanatical drow killer: cold, contemptuous and zealous for the captain, with every word soaked in hatred for surface elves.*"
- Sound, line 47: "- **Sound:** A low, flat, cold voice. It rises into fervour when he speaks of Jarlaxle or of Nar'l's weakness."
- Sentence shape, line 48, and Word choice, line 49, Swearing, line 50, Personality in speech, line 51, Quirks, line 52, Signature phrases, line 53, Never, line 54, Sample lines, lines 55-58.

### A11. How long in post

- Wiki extract line 62: "was one of the top agents of [[Bregan D'aerthe]] in [[Waterdeep]] during the early 1490s [[DR]]."
- Adventure, page 211 (Nar'l's entry): "A year ago, Nar'l was given the difficult task..." (about Nar'l, not Soluun). No source gives Soluun's start date in Waterdeep.
- Campaign, the first-meeting event (day-one watch): see A4. No tenure is given.

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, the page (line 5): "- *Drow gunslinger, neutral evil, he/him*. Stat block: **Drow Gunslinger**."
- Campaign, the Organization page Key Members (line 100): "- **Soluun Xibrindas** — Drow gunslinger, neutral evil." (see A3)
- Campaign, the gazetteer (line 151): "**Soluun Xibrindas (Neutral Evil, Drow, he/him)**"
- Adventure, appendix B page 202: "{@creature Soluun Xibrindas|wdh} is a neutral evil {@creature drow gunslinger|WDH}, with these changes:" — `sources/adventure-wdh.json:32048`
- Wiki extract line 57: "| alignment5e    = [[Neutral evil]]"

**Species**
- Campaign, the page (line 5): "Drow gunslinger".
- Adventure: "{@creature Soluun Xibrindas|wdh} is a neutral evil {@creature drow gunslinger|WDH}" (`sources/adventure-wdh.json:32048`).
- Wiki extract line 14: "| race           = [[Drow]]".

**Pronouns**
- Campaign, the page (line 5): "he/him". Gazetteer line 151: "he/him".
- Adventure: "He conceals his nighttime escapades as well as he can" (`sources/adventure-wdh.json:32041`).
- Wiki extract line 13: "| sex            = Male".

**Stat block**
- Campaign, the page (line 5): "Stat block: **Drow Gunslinger**."
- Campaign, the Doom Raiders overview (`campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/overview.md:60`): "Soluun Xibrindas uses the **Scout** from the 2024 *Monster Manual*, with a hand crossbow in place of the longbow, Darkvision 120 feet and Advantage on Stealth checks in dim light or darkness."
- Campaign, the first-meeting design notes (`campaign/quests/faction-events/bregan-daerthe/00-first-meeting/design-notes.md:33`): "The events use it for Krebbyg and Fel'rekt, and use the 2024 **Scout** for Soluun, as **The Dockside Killer** does."
- Alexandrian, Appendix C, the Dockside Killer scene 3 (`sources/Appendix_C_-_Player_Faction_Missions.md:1213`): "**Soluun Xibrindas** (**Drow Gunslinger**, *Dragon Heist* appendix B)."
- Adventure: "with these changes" (`sources/adventure-wdh.json:32048`); the changes are a scimitar and the kit at `:32052`-`:32053`.
- Alexandrian, the roster (`sources/9. Lair – Sea Maidens Faire.pdf` printed p.74): "Soluun Xibrindas (50%)" (no stat-block name).

**Affiliation**
- Campaign, the page (line 6): "- **Affiliation:** Bregan D'aerthe"
- Campaign, the Organization page (line 100): "Drow gunslinger, neutral evil." (affiliation is the company page)
- Campaign, the gazetteer (line 38): "a drow gunslinger of Bregan D'aerthe"

---

## C. Sentences on the current page that narrate quest-time or depend on a discovery

Current page: `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md`. The page has no Background, Personality or Connections section yet. Each row says whether the sentence is day-one, and where its fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L5 | "- *Drow gunslinger, neutral evil, he/him*. Stat block: **Drow Gunslinger**." | Day-one for the alignment and species. The stat-block name conflicts (D1) | Section B |
| 2 | L6 | "- **Affiliation:** Bregan D'aerthe" | Day-one | `campaign/setting/organizations/07-bregan-daerthe.md:100` |
| 3 | L7 | "- **Featured in:** **Faction Outposts**, **Sea Maidens Faire**, **Doom Raiders Mission 1 — The Dockside Killer**, **The Compromised Eye**, **Force Grey Mission 4 — Destroy the Intellect Factory**" | Quest references. The list omits the Trollskull First Meeting (`ev-01-first-meeting.md:26`), The Killer's Fate (`s05`) and The Dive (`m06`), where he appears | `campaign/quests/faction-events/bregan-daerthe/s05-the-killers-fate/ev-01-the-killers-fate.md`; `m06-the-dive/ev-01-the-dive.md` |
| 4 | L11 | "**Resonance.** Soluun should inspire revulsion with his methodical murder of surface elves, discomfort with his fanatical loyalty to Jarlaxle, and pity for the hatred that defines his entire existence." | Day-one. "methodical murder" is the day-one habit (A2) | `sources/adventure-wdh.json:32041`; `dock-ward.md:152` |
| 5 | L13 | "**Emotions.** Soluun most often feels cold hatred of surface elves, fanatical devotion to Bregan D'aerthe, contemptuous superiority, a zealot's fervor for the band (which, like every member of Bregan D'aerthe, rejects Lolth), hunting focus, and bitter disdain for his brother Nar'l." | Day-one. Keep verbatim | A2, A6, A7 |
| 6 | L15 | "**Motivations.** Soluun wants to kill every surface elf and half-elf he can find without consequences, serve Jarlaxle with absolute loyalty, and prove that his brother Nar'l is the weak one." | Day-one. Keep verbatim. "without consequences" is a motive, not a fact (the disownment is a cover; D3) | `sources/adventure-wdh.json:32040`-`:32041` |
| 7 | L17 | "**Inspirations.** When playing Soluun, channel the Punisher (*Marvel*), Colonel Kurtz (*Apocalypse Now*), and Kylo Ren (*Star Wars*)." | Not a fact | n/a |
| 8 | L21 | "**Persona.** To the world, Soluun is a drow gunslinger of Bregan D'aerthe, disowned for unsanctioned Dock Ward murders. ..." | "disowned for unsanctioned Dock Ward murders" is the public cover. The wording differs from `dock-ward.md:38` ("killing without orders") (D3). The rest is day-one | A2, A5, A6 |
| 9 | L23 | "**Morale.** In a fight, Soluun attacks without hesitation or mercy. He carries a bloodstained Seven Masks Theater playbill for Blood Wedding; he stalks and murders elven and half-elven audience members after shows. Jarlaxle is aware and hasn't yet decided what to do about it." | Sentence 1 is encounter behaviour; its day-one counterpart is "Soluun attacks without hesitation" in the adventure's style, but the adventure has no combat line for Soluun, so cite `campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/overview.md:60` (Scout, flees at half hit points) and Appendix C line 1215 ("He fights with professional efficiency and flees at half hit points"). Sentences 2 and 3 are day-one (A5) | `sources/Appendix_C_-_Player_Faction_Missions.md:1215`; `dock-ward.md:38` |
| 10 | L25 | "**Relationships.** Soluun is the elder brother of Nar'l Xibrindas (whom he despises), a lieutenant of Jarlaxle (whom he worships), and a serial killer whose disownment by Bregan D'aerthe is a cover story: he carries forged BD identification." | Day-one (the cover; D3). "forged BD identification" uses a different item name from `dock-ward.md:38` ("forged Bregan D'aerthe token") | `villains/jarlaxle.md:116`; `dock-ward.md:38` |
| 11 | L29 | "A drow gunslinger carrying a bloodstained Seven Masks Theater playbill — publicly disowned by his organization, though his forged identification tells a different story." | Day-one as the public face. 21 words or fewer is the brief's limit; the sentence is 24 words | `dock-ward.md:38` |

**Voice profile (`.claude/skills/character-voices/voices/bregan-daerthe.md`), quest-time or encounter clauses for the rule-16 restatement**
- Line 51, Personality in speech: "- **Personality in speech:** Cold hatred, fanatical loyalty and superiority. Once captured, he shows no remorse, only disgust. He claims Jarlaxle's authority even though he was disowned." The clause "Once captured" is encounter-time. "even though he was disowned" states the cover as fact (D3). Restate as the public story.
- Line 56, Greeting: "  - *Greeting:* \"You're not elves. Stay out of my way and you might live.\"" Encounter-time (a confrontation at a door or in an alley).
- Line 57, Business: "  - *Business:* \"I serve the captain. Whatever they told you about me is a lie told for the humans.\"" Presupposes that the party has heard the public story. Quest-time: restate or cut.
- Line 58, Under pressure: "  - *Under pressure:* \"Kill me, then. No goddess is coming for me, and I never wanted one. The captain remembers his own. You'll all be prey one day.\"" Encounter-time. The line "The captain remembers his own." is an inner-life hint (G).
- Line 52, Quirks: "He touches his forged token when he names Bregan D'aerthe." Day-one.
- Line 54, Never: "He never apologises, never shows mercy to an elf, never admits Jarlaxle disowned him, and never speaks of Lolth as anything but the spider-bitch he walked away from." "never admits Jarlaxle disowned him" keeps the cover (day-one).

**Campaign, the Killer's Fate text (quest-time; routed to `s05-the-killers-fate/ev-01-the-killers-fate.md`)**
- Line 9 (the event's card): "- Watch the ruling delivered and Soluun stripped of the silver disc he wears at his neck."
- Line 20: "Then Soluun was seen. The Doom Raiders stood in the alley, the Harbor Watch has his description, and the hired Luskan sailors who guarded the street end are talking in the quay taverns. An agent who kills openly in Waterdeep is a liability to every other agent, so Jarlaxle has decided to make the cover story true. Soluun is expelled tonight and leaves with nothing but his clothes, unless a member pleads for more." — quest-time (the event). Restated as day-one: Jarlaxle has not yet decided; `s05` line 18 says so.
- Line 22: "Soluun believes this is a test, or a mistake the captain will mend, and that belief is all that keeps him from spitting in Nevercott's face. It won't last." — quest-time (the event's belief and the Dive).
- Line 242: "He doesn't believe the captain means it until Fel'rekt lifts the disc from his neck." — quest-time.
- Line 259: "Soluun touches the silver disc at his throat, a spider in its web crossed by a blade." — event scene; whether the disc exists on Ches 1 is not stated (D3).

**Campaign, the Dockside Killer (quest-time; routed to `doom-raiders/m01-the-dockside-killer/`)**
- `overview.md:60` (the Scout and the hired hands), `ev-01-the-dockside-killer.md:343` (the Lolth answer, quoted in A6), `design-notes.md:13` ("***The disownment.*** The restored draft treated Soluun's disownment as real. ... This version keeps that in GM text only, and Soluun never mentions being disowned."). The design note says the Notable Figures page treats the disownment as a cover story; it matches the page.

**Campaign, the Compromised Eye (quest-time; routed to `m04-the-compromised-eye/ev-01-the-compromised-eye.md`)**
- Line 21: "> - Nar'l held the reports back to protect his elder brother, because the Dock Ward killings were Soluun's work. He has told nobody in the company." — quest-time (Nar'l's reports; `m04` event).
- Lines 30-32: "**Soluun Expelled** (marked by **The Killer's Fate**)", "**Soluun Killed** (marked by **The Dockside Killer**, a Doom Raiders mission)", "**Neither is marked:** Soluun is alive and still carries forged company papers." Outcome-gated.

**Campaign, The Dive (quest-time; routed to `m06-the-dive/`)**
- `m06-the-dive/ev-01-the-dive.md:11`: "> - Learn from the team's papers, or from Soluun, who sold the Guild the berth." — quest-time (the Dive mission).
- `m06-the-dive/design-notes.md:17`: "- **Soluun's sale**, if **Soluun Expelled** is marked. Soluun is in the launch and his hand is on Orlo's sketch."

**Campaign, the arc-h structure (quest routing for the letter)**
- `campaign/structure/arc-h-sea-maidens-faire.md:424`: "**To Xanathar's Lair (if not yet completed).** The Letter from Nar'l Xibrindas (U3) confirms the BD mole in Xanathar's organization and mentions the Seven Masks Theater purchase." — routed to Xanathar's Lair and Sea Maidens Faire.

**Alexandrian (transcription), the letter in U3 (routed; Nar'l's letter)**
- `sources/9. Lair – Sea Maidens Faire.pdf` printed p.73: "Brother—I hope this letter finds you in good spirits." Routed to Sea Maidens Faire.

---

## D. Conflicts

Rank used: campaign files first, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.

**D1. Stat block**
- Campaign, the page: "Stat block: **Drow Gunslinger**." (`campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:5`)
- Campaign, the Doom Raiders overview: "Soluun Xibrindas uses the **Scout** from the 2024 *Monster Manual*" (`campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/overview.md:60`)
- Campaign, the first-meeting design notes: "use the 2024 **Scout** for Soluun, as **The Dockside Killer** does." (`campaign/quests/faction-events/bregan-daerthe/00-first-meeting/design-notes.md:33`)
- Alexandrian, Appendix C: "**Soluun Xibrindas** (**Drow Gunslinger**, *Dragon Heist* appendix B)." (`sources/Appendix_C_-_Player_Faction_Missions.md:1213`)
- Adventure: "is a neutral evil {@creature drow gunslinger|WDH}, with these changes:" (`sources/adventure-wdh.json:32048`)
- Unresolved. The page names the block the drafter writes, and the Draft Notes must say which.

**D2. The Lolth shrine and the prayer**
- Adventure: "is here, worshiping before a shrine of Lolth." (`sources/adventure-wdh.json:26345`)
- Wiki extract: "where he prayed to [[Lolth]]." (wiki extract line 65)
- Campaign, the location: "**U3 — Soluun's Stateroom:** Drow gunslinger Soluun Xibrindas, cleaning his weapons." (`campaign/locations/sea-maidens-faire/05-scarlet-marpenoth.md:40`)
- Campaign, the Lolth page: "The campaign's U3 entry has Soluun cleaning his weapons and no shrine (`campaign/locations/sea-maidens-faire/05-scarlet-marpenoth.md:40`), so the shrine is dropped." (`campaign/setting/deities/lolth.md:68`)
- Campaign rule: "Bregan D'aerthe has rejected Lolth as its goddess. No member worships her, keeps a shrine to her or invokes the Spider Queen with devotion" (`campaign/setting/organizations/07-bregan-daerthe.md:46`)
- Alexandrian, the U3 entry (transcription): "Area U3 – Soluun's Stateroom: The footlocker contains A Letter from N'arl." No shrine (`sources/9. Lair – Sea Maidens Faire.pdf` printed p.73).
- Resolved in favour of the campaign. The page states no shrine and no prayer. The wiki's infobox also gives "| patron deity   = [[Lolth]]" (wiki extract line 18), which the campaign does not accept.

**D3. The disownment and the forged item**
- Page, line 21: "disowned for unsanctioned Dock Ward murders" (`campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:21`)
- Gazetteer: "Jarlaxle's public story is that he disowned Soluun for killing without orders, and the story is a cover." (`campaign/gazetteer/waterdeep/dock-ward.md:38`)
- Organization page: "Soluun carries a forged Bregan D'aerthe token so that the company can deny him." (`campaign/setting/organizations/07-bregan-daerthe.md:127`)
- Killer's Fate, the cover: "The public story that Soluun was disowned for killing without orders was Jarlaxle's invention, put about so nobody could trace the killings to him. The silver disc at Soluun's neck is a forgery the company struck on purpose so it could deny him." (`campaign/quests/faction-events/bregan-daerthe/s05-the-killers-fate/ev-01-the-killers-fate.md:18`)
- Killer's Fate, the state of the disownment: "until tonight the company's public disownment of him has been a cover story." (`s05 ev-01:5`) and "Soluun is expelled tonight" (`s05 ev-01:20`). These are event-time; the disownment becomes true only at the event (`m04-the-compromised-eye/ev-01-the-compromised-eye.md:30`).
- Voice: "He claims Jarlaxle's authority even though he was disowned." (`.claude/skills/character-voices/voices/bregan-daerthe.md:51`)
- Three wordings of the item: "forged Bregan D'aerthe token" (gazetteer and Organization), "forged BD identification" (page line 25), "a forgery" for the "silver disc" (Killer's Fate). The Killer's Fate event says the disc is struck by the company. The page should use the campaign's day-one wording ("cover story" and "forged"), not the disc.

**D4. The weapon**
- Gazetteer: "a hand crossbow bolt and a curved shortsword" (`campaign/gazetteer/waterdeep/dock-ward.md:152`)
- Adventure: "Soluun wields a scimitar instead of a shortsword (it deals slashing damage instead of piercing damage)." (`sources/adventure-wdh.json:32052`)
- Campaign, the Dockside Killer: "with a hand crossbow in place of the longbow" (`campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/overview.md:60`)
- Adventure, the kit: "a pouch containing twenty pistol bullets" (`sources/adventure-wdh.json:32053`) and the Lantanese firearms (`sources/adventure-wdh.json:23035`). Firearms and crossbow are both in the sources; the page does not name a weapon.

**D5. The Nar'l page and the burning house**
- Adventure, the house: "Nar'l's house was wiped out long ago, but he and his elder brother Soluun survived and joined Bregan D'aerthe." (`sources/adventure-wdh.json:32323`)
- Wiki extract: "The family's house was destroyed and only Soluun and his younger brother [[Nar'l Xibrindas|Nar'l]] survived." (wiki extract line 68)
- Nar'l page, unreviewed `[design]` text: "though he once carried Nar'l out of their burning house `[design]`." (`campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:43`)
- Nar'l page, Design list: "Soluun coming back, going into the burning hall and carrying Nar'l out through a service passage while the archivist and household died" (`campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:154`)
- Not a contradiction of the sources (the house was destroyed, and both survived). But the burning-house story is only on the Nar'l page as `[design]`. The Soluun Background must either repeat it as `[design]` or leave it out. The Nar'l page's own check (line 158) says the text "stays consistent with these sourced facts."

**D6. Who receives Soluun's brother's sending**
- Adventure, Nar'l: "He prepares and casts the {@spell sending} spell whenever he needs to communicate with his brother." (`sources/adventure-wdh.json:32331`)
- Adventure, Xanathar's Lair: "who uses {@spell sending} spells to transmit intelligence to his drow brethren" (`sources/adventure-wdh.json:15149`)
- Campaign, the Villains and Organization pages: Nar'l reports to Jarlaxle by *Sending* (`campaign/setting/villains/jarlaxle.md:113`: "Nar'l reports to Jarlaxle by *Sending*. Xanathar suspects him of disloyalty and has set a grell to kill him at the first proof, and it does not know he reports to Bregan D'aerthe or to Jarlaxle.")
- Not a Soluun fact. Listed because the adventure ties the brothers and the sending.

**D7. Dock Ward victims**
- Gazetteer: "He picks an elf or half-elf sailor out of a Seven Masks audience" (`dock-ward.md:152`) and "Soluun Xibrindas picks his victims from the audience here." (`dock-ward.md:77`)
- Page, Morale: "he stalks and murders elven and half-elven audience members after shows" (`campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:23`)
- Appendix C: "Three elf and half-elf sailors have been decapitated in the Dock Ward at night." (`sources/Appendix_C_-_Player_Faction_Missions.md:1180`)
- Adventure: "looking for solitary elves or half-elves to pick off" (`sources/adventure-wdh.json:32041`)
- Not a conflict. The victims are sailors in the gazetteer and Appendix C, and audience members in the page's Morale. The drafter should state both.

---

## E. Stale lines in other files (not edited) and routed quest references

**Stale, not edited**
- `campaign/setting/villains/jarlaxle.md:116` and the Organization page (`:127`) both say Soluun carries a "forged" item. Those agree with the gazetteer. The Killer's Fate disc is a separate item (D3).
- `campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/design-notes.md:13` says the Notable Figures page treats the disownment as a cover story and that Jarlaxle "hasn't decided what to do". Current and consistent.
- `campaign/setting/deities/lolth.md:76` quotes the Persona as "02-soluun-xibrindas.md:22". The Persona is at line 21 of the file. Stale cite (not edited).
- `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:158` says `02-soluun-xibrindas.md` Persona has "was taught from a young age to kill surface elves", which matches line 21 (correct).
- `campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/design-notes.md:17` ("If Soluun was expelled, the cover story is real and nobody calls it one.") is quest-time and consistent with the Killer's Fate.

**Routed to quests (quest-time facts the page cannot state as day-one)**
- Dockside Killer (Doom Raiders Mission 1): `campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/ev-01-the-dockside-killer.md` (the ambush, the playbill clue, the Scout, the Soluun Killed outcome). Appendix C: `sources/Appendix_C_-_Player_Faction_Missions.md:1176`-`:1223` (the three-night stakeout and the alley).
- The Killer's Fate (Bregan D'aerthe, s05): `campaign/quests/faction-events/bregan-daerthe/s05-the-killers-fate/ev-01-the-killers-fate.md` (the ruling, the disc, Soluun Expelled, Soluun Killed).
- The Compromised Eye (m04): `campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/ev-01-the-compromised-eye.md` (the Soluun outcomes and Nar'l's reports).
- The Dive (m06): `campaign/quests/faction-events/bregan-daerthe/m06-the-dive/ev-01-the-dive.md:11` and `:28`; `design-notes.md:17`-`:28` (Soluun's sale of the berth).
- Nar'l's letter in U3 (Sea Maidens Faire): `campaign/structure/arc-h-sea-maidens-faire.md:424`.
- First-meeting watch (day-one as a habit, quest as an event): `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:26`, `:42`, `:159`.
- Doom Raiders response team (the Factions Guide): `campaign/guides/factions/08-bregan-daerthe.md:122` and `:137`.

---

## F. Gaps a Background would need that no source gives

1. **Birth year, birthplace, age and the house's name.** No source gives any. The wiki infobox leaves `age`, `dob`, `ethnicity` and `home` detail blank (wiki extract lines 17, 21, 15 and 11; line 11 gives only "[[Waterdeep]], [[Sword Coast North]]"). The house is unnamed in every source (`sources/adventure-wdh.json:32323`: "Nar'l's house was wiped out long ago").
2. **How the house fell and when.** The adventure says only "wiped out long ago" (`sources/adventure-wdh.json:32323`). The wiki says "The family's house was destroyed" (wiki extract line 68). The Nar'l page's `[design]` burning house is the only detail (D5).
3. **The raiding parties and his training.** The Nar'l page's `[design]` text has Soluun "sent out with the raiding parties as soon as he could carry a blade" (`campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:153`). The adventure says only "taught from a young age" (`sources/adventure-wdh.json:32041`).
4. **How he met Jarlaxle and joined.** The sources give only the joining with Nar'l: "They decided to join [[Bregan D'aerthe]]." (wiki extract line 68) and "he and his elder brother Soluun survived and joined Bregan D'aerthe" (`sources/adventure-wdh.json:32323`). No source gives the recruitment scene.
5. **Years in the company and the rank.** The wiki gives "one of the top agents ... during the early 1490s [[DR]]" (wiki extract line 62). No rank is given beyond "lieutenant" (`campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:25`: "a lieutenant of Jarlaxle").
6. **Current home.** No campaign source gives a home. The wiki says "The wiki" home line "[[Waterdeep]], [[Sword Coast North]]" (wiki extract line 11). The Scarlet Marpenoth stateroom U3 is the room the Alexandrian and the campaign name (`campaign/locations/sea-maidens-faire/05-scarlet-marpenoth.md:40`). The wiki places him on the sub (wiki extract line 65).
7. **Personal goals.** No source gives a personal want beyond "kill every surface elf and half-elf he can find without consequences, serve Jarlaxle with absolute loyalty, and prove that his brother Nar'l is the weak one" (`campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:15`, verbatim Motivations). Any other goal is `[design]`.
8. **A relationship or loss that still matters.** The brother is the only named relation: the adventure says "His younger brother, Nar'l, has infiltrated the Xanathar Guild" (`sources/adventure-wdh.json:32040`). The wiki says his brother Nar'l "decision to study magic" (wiki extract line 71). The Nar'l page's `[design]` text adds the burning house and Soluun's later love for his brother ("his love for the brother who came back for him" is in the Nar'l page's Personal goals at `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:156`, which is Nar'l's goal, not Soluun's).
9. **The Lolth question.** No devotion to Lolth is allowed (D2). A Background must give him "the devotion a drow of the houses would give the Spider Queen he gives to Jarlaxle instead" (`campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:21`).
10. **The age at Ches 1.** Not sourced. Wiki infobox blank (wiki extract line 17).

---

## G. Source facts that hint at the inner life (habits, loves, grudges, losses, places, people)

The drafter uses these for the backstory and personal goals (brief ruling 17). Nothing invented may contradict them.

**Hatred and grudges (sourced)**
> "Soluun has a burning hatred of surface elves and half-elves, having been taught from a young age to kill them as opportunity permits." — `sources/adventure-wdh.json:32041`
> "Soluun considers Nar'l a weakling who turned to arcane magic by way of compensation, and he has never had much faith in his brother or his abilities." — `sources/adventure-wdh.json:32040`
> "He considered his brother weak for his decision to study [[magic]]." — wiki extract line 71
> "- Soluun hates surface elves and serves Jarlaxle with a zealot's devotion. He is the elder brother of Nar'l Xibrindas, whom he despises." — `campaign/gazetteer/waterdeep/dock-ward.md:157`

**Loyalty and what he is afraid of losing (campaign and voice)**
> "To those he trusts, he is fiercely loyal to Jarlaxle and Bregan D'aerthe" — `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:21`
> "- **Quirks:** He spits at the mention of surface elves. He touches his forged token when he names Bregan D'aerthe." — `.claude/skills/character-voices/voices/bregan-daerthe.md:52`
> "Kill me, then. No goddess is coming for me, and I never wanted one. The captain remembers his own. You'll all be prey one day." — `.claude/skills/character-voices/voices/bregan-daerthe.md:58`
> "- **Never:** He never apologises, never shows mercy to an elf, never admits Jarlaxle disowned him, and never speaks of Lolth as anything but the spider-bitch he walked away from." — `.claude/skills/character-voices/voices/bregan-daerthe.md:54`

**Routine and the night (sourced)**
> "He conceals his nighttime escapades as well as he can, but Jarlaxle, Fel'rekt, and Krebbyg know what he's up to." — `sources/adventure-wdh.json:32041`
> "Soluun preferred to act during the day." — wiki extract line 65
> "Soluun takes the day from doorways and awnings on the shaded side of the street." — `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:42`

**The trophy and the thrill (campaign)**
> "He carries a bloodstained Seven Masks Theater playbill for Blood Wedding" — `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:23`
> "Soluun touches the silver disc at his throat, a spider in its web crossed by a blade." — `campaign/quests/faction-events/bregan-daerthe/s05-the-killers-fate/ev-01-the-killers-fate.md:259` (the event's scene, not day-one)

**The Nar'l page's `[design]` lines about Soluun (not sourced; do not contradict)**
> "Soluun giving Jarlaxle the devotion owed his house" — `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:154`
> "Soluun reading the arrangement as proof that Nar'l could not fight." — `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:153`

**The Alexandrian letter (Nar'l's view; transcription)**
> "A delightfully bloody affair." — `sources/9. Lair – Sea Maidens Faire.pdf` printed p.73 (transcription; Nar'l to Soluun)

**Surface elves in general (sourced)**
> "Filthy fucking surface-blood. You all smell of sunlight." — `.claude/skills/character-voices/voices/bregan-daerthe.md:50` (sample swearing line; the profile's Swearing line)

---

## Not found

- **Soluun's birth, childhood home, age, and the house name:** searched "Soluun" and "Xibrindas" across `campaign/` (39 files named Soluun). Only the Nar'l page's `[design]` text adds any childhood detail. No source gives a birth year.
- **Soluun's recruitment scene and start date:** searched the Bregan faction events, the Factions Guide and the Organization page. None give a joining scene or a date.
- **Soluun's rank title:** searched "lieutenant" and the Factions Guide ranks (`campaign/guides/factions/08-bregan-daerthe.md:56`-`:60`). The ranks are for player characters; no Soluun rank is given.
- **Soluun's personal goals beyond the Motivations line:** none.
- **Soluun's stat block name in the adventure:** the adventure gives "with these changes" (`sources/adventure-wdh.json:32048`) but no name beyond "drow gunslinger".
- **Soluun in the Alexandrian Faction Outposts PDF:** `sources/5. Faction Outposts.pdf` printed pp.36-38 (PDF pp.1-3) do not name Soluun. The outposts text after p.38 was not read.
- **Soluun in the Alexandrian Revelation Lists PDF:** `sources/17. Outpost and Lair Revelation Lists.pdf` was not read this session. The campaign's Factions Guide Response Team lines are at `campaign/guides/factions/08-bregan-daerthe.md:122`-`:137`.
- **Soluun in `sources/1. The Villains.pdf`:** the Villains PDF (PDF pp.2-5 read) does not name Soluun.
- **Soluun's wiki extract beyond the 96 lines:** the file has 96 lines and was read in full.
- **Soluun in the pass5 wiki bundle** (`sources/research/pass5-bundles/bregan-daerthe/wiki.txt`): not searched for Soluun in this pass. The extract has the 5e page.

## Not readable

- `Jarlaxle Baenre NPC Guide.docx` and `Zardoz Zord (and extra side quest hook).docx` (`sources/SOURCE_GUIDE.md:690`, `:698`): the tools cannot open `.docx`. They may hold Soluun material; not checked.
- `sources/17. Outpost and Lair Revelation Lists.pdf`: not read.
- `sources/9. Lair – Sea Maidens Faire.pdf` printed pp.73-75: read as page images; the quotes are transcriptions and need `pdftotext -layout`.
- `sources/5. Faction Outposts.pdf`: read as page images; the first three PDF pages do not name Soluun.
