# Pass 6 research notes: Fel'rekt Lafeen

Page: `campaign/setting/notable-figures/bregan-daerthe/03-felrekt-lafeen.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR. Fel'rekt is a named lieutenant of Jarlaxle and is in Waterdeep on day one. His Gralhund Villa role is quest time and is routed to **Gralhund Villa**. Cassalanter secrecy and the Lolth rule apply. Brief ruling 2 makes him a major NPC, so the full Personality and Connections apply.
Organization page: `campaign/setting/organizations/07-bregan-daerthe.md`
Voice profile: `.claude/skills/character-voices/voices/bregan-daerthe.md` ("### Fel'rekt Lafeen", lines 62-76)
Wiki extract: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-bregan-daerthe/03-felrekt-lafeen.txt` (quoted as "wiki line N", that file's lines; citation key `WDH5e`, *Waterdeep: Dragon Heist*, 5e)

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes are shown as plain quotes. `{@creature ...}` tags are left as written. The `page` field of an entry is given where one exists.
- Where a source sentence runs on past the quoted part, the quote ends at a sentence boundary and the rest of the passage is named in brackets. No quote is cut mid-sentence.
- Alexandrian PDFs: no shell, so `pdftotext` could not run. Four PDFs were read as rendered page images and their quotes are transcriptions. Check exact wording with `pdftotext -layout` before any quote goes into prose:
  - `sources/5. Faction Outposts.pdf` (printed pp.36-37 = PDF pp.1-2). Read: PDF pp.1-2.
  - `sources/17. Outpost and Lair Revelation Lists.pdf` (printed p.122 = PDF p.2). Read: PDF p.2.
  - `sources/9. Lair – Sea Maidens Faire.pdf` (printed pp.68-70 = PDF pp.1-3). Read: PDF pp.1-3.
  - `sources/1. The Villains.pdf` (printed p.17 = PDF p.5). Read: PDF p.5.
- Alexandrian text files read: `sources/Appendix_B_-_Player_Factions.md`, `sources/Appendix_D_-_Running_the_Tavern.md`, `sources/Act_III_Arc_D.md`, `sources/Act_III_Arc_E.md`.
- The Grep tool cannot search the PDFs (no match for "Lafeen" in any `sources/*.pdf` file). The PDFs not read were not checked for names (see Not found).
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **One Gralhund clause sits in the Relationships line.** L25 ends with "and the Bregan D'aerthe operative who led the team at Gralhund Villa." That is quest time. Its day-one form depends on **Jarlaxle Informed**, a Fireball! outcome (`campaign/quests/act-ii/gralhund-villa/ev-02-saerdoun-street.md:53`). Route it (section C, row 10).
2. **The Persona's account of his origin goes beyond the sources.** The page says "in a society that punishes male drow" (L21). The published adventure says "Unhappy with the treatment of males in his society" (`sources/adventure-wdh.json:32002`). The wiki says "disgusted with the treatment of males in drow society" (wiki line 70). See D4.
3. **"Logistics lieutenant" is used for Fel'rekt in two quest events, and for Krebbyg on the org page and his own page.** The org page calls Fel'rekt "BD lieutenant" (`campaign/setting/organizations/07-bregan-daerthe.md:101`). The org page's own Draft Notes flag the label (`:189`). See D1.
4. **The Overview is 25 words, over the 21-word limit** (L29). See C row 11.
5. **The public face of his cover conflicts across files.** The org page says he "keeps his heritage to himself" (`campaign/setting/organizations/07-bregan-daerthe.md:101`). The Trollskull appendix says "Fel'rekt does not disguise his heritage" (`sources/Appendix_D_-_Running_the_Tavern.md:1626`). The Persona says "To the world, Fel'rekt is a drow gunslinger" (L21). See D2.
6. **No source gives a birth year, home, family, age, or date of joining.** Section F lists what the drafter must invent and what it must stay consistent with. Invented material is tagged `[design]`.

---

## A. Background facts by theme

### A1. Origin, birth and the change of sex (sourced for the change and the reason for it only)

**Adventure, the entry (page 201)**
> "Fel'rekt is a male drow who was born female. Unhappy with the treatment of males in his society, he petitioned to join Bregan D'aerthe. Jarlaxle took a shine to Fel'rekt almost immediately, and the young drow has since become one of Jarlaxle's most loyal lieutenants. Eager to prove himself, Fel'rekt is quick to volunteer for tasks and hurls himself into combat with verve."
> — `sources/adventure-wdh.json:32002` (entry "Fel'rekt Lafeen", page 201)

**Wiki, History (edition 5e, WDH5e-p201-202)**
> "Fel'rekt was born female but at some point changed to being male. However, disgusted with the treatment of males in [[drow]] society, he joined [[Bregan D'aerthe]]. Almost immediately, Jarlaxle was impressed with Fel'rekt, who volunteered for all the most dangerous missions."
> — wiki line 70 (History)

**Wiki, lead (edition 5e, WDH5e-p15)**
> "was one of the top agents of the [[Bregan D'aerthe]] in [[Waterdeep]] during the early 1490s [[DR]]."
> — wiki line 64 (the lead sentence opens with the name and a pronunciation template, which is not quoted)

**Adventure, pronunciation key**
> "{@creature Fel'rekt Lafeen|WDH}"
> "FEL-rekt lah-FEEN"
> — `sources/adventure-wdh.json:113`-`:114`

**Campaign, Persona (the page's own account; see D4)**
> "**Persona.** To the world, Fel'rekt is a drow gunslinger, one of Jarlaxle's most trusted lieutenants. To those he trusts, he was born female in a society that punishes male drow; he petitioned to join Bregan D'aerthe and Jarlaxle took an immediate shine to him. Deep down, he lacks the cruelty common to most drow and will not kill an adversary unless left with no other choice."
> — `campaign/setting/notable-figures/bregan-daerthe/03-felrekt-lafeen.md:21`

**Campaign, the organization page**
> "Fel'rekt Lafeen petitioned to join because he was unhappy with the treatment of males in drow society, and Jarlaxle took to him almost at once (*Waterdeep: Dragon Heist*, 5e)."
> — `campaign/setting/organizations/07-bregan-daerthe.md:42` (Stand Outside the System)

**Campaign, the company's founding rule (history, GM-facing)**
> "- The company was built from rogue males of destroyed houses in Menzoberranzan and Ched Nasad. The published adventure calls its first members the much-derided and dishonorable castaways of destroyed drow houses. Almost all of them are male, because female drow rarely take orders from a male."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:41`

**Campaign, the same rule (villains page, Background)**
> "- He left his house and name, though not his connections, and founded the company from the rogue males of destroyed and disgraced houses (Forgotten Realms Wiki, novel *Homeland*; published adventure). Almost all members are male, because female drow rarely take orders from a male, and a female drow can earn a place by decrying the matriarchy and convincing him she would be an asset (**Bregan D'aerthe's Long Road**)."
> — `campaign/setting/villains/jarlaxle.md:46`

No source gives his birth year, birth name, home district, house, parents, or an age beyond "the young drow" (see F1).

### A2. How he joined and how he rose

**Adventure (see A1, `sources/adventure-wdh.json:32002`)**: "Jarlaxle took a shine to Fel'rekt almost immediately, and the young drow has since become one of Jarlaxle's most loyal lieutenants."

**Wiki (wiki line 70)**: "Almost immediately, Jarlaxle was impressed with Fel'rekt, who volunteered for all the most dangerous missions."

**Alexandrian Appendix B, the lieutenants (the joining section)**
> "When one or more characters are drow, Jarlaxle has three lieutenants — **Fel'rekt Lafeen**, **Krebbyg Masq'il'yr**, and **Soluun Xibrindas** — shadow the party at a careful distance for several days."
> — `sources/Appendix_B_-_Player_Factions.md:717`

**Adventure, the recruitment watch (quest-time use; routed in E2)**
> "If one or more characters are drow, {@creature Jarlaxle Baenre|WDH} has his lieutenants, three {@creature drow gunslinger|WDH|drow gunslingers}, shadow these potential new recruits while keeping a safe distance. {@creature Fel'rekt Lafeen|WDH} and {@creature Krebbyg Masq'il'yr|WDH} watch the characters at night, and {@creature Soluun Xibrindas|wdh} watches them during the day (doing his best to stay out of the sunlight)."
> — `sources/adventure-wdh.json:3592` (chapter not checked; the passage concerns new recruits)

**Campaign, the rank in the Villains page (the quest-time membership run)**
> "- **Membership.** Membership runs during **Trollskull Alley**, like any other faction. Three drow lieutenants shadow the party for several days. J.B. Nevercott, who is Jarlaxle in a *hat of disguise* posing as a haberdasher, then visits Trollskull Manor and offers enrollment to any interested PC."
> — `campaign/setting/villains/jarlaxle.md:16`

**Campaign, the Initiate benefit (Factions Guide, mechanics)**
> "| 1 | **Initiate** | Recognized D'aerthe operative. Safe house access aboard the *Heartbreaker* or *Hellraiser*. Access to drow-made equipment at cost — hand crossbows, *+1 bolts*, darkvision-enhancing gear — through Fel'rekt Lafeen. All D'aerthe members extend professional courtesy: will not act against the character without direct orders from Jarlaxle."
> — `campaign/guides/factions/08-bregan-daerthe.md:56` (Renown table, rank 1)

**Campaign, the organization page label**
> "- **Fel'rekt Lafeen** — Drow gunslinger, neutral good, and BD lieutenant. One of Jarlaxle's most trusted men, he is the close friend and operational partner of Krebbyg Masq'il'yr and keeps his heritage to himself. See the **Fel'rekt Lafeen** page in Notable Figures."
> — `campaign/setting/organizations/07-bregan-daerthe.md:101` (Key Members)

**Adventure, the Scarlet Marpenoth stateroom (page 143)**
> "If he has not been encountered and defeated elsewhere, a {@creature drow gunslinger|WDH} named {@creature Fel'rekt Lafeen|WDH} (see {@adventure appendix B|WDH|12}) is here, cleaning his pistol. His stateroom contains a net hammock and a steel footlocker."
> — `sources/adventure-wdh.json:26433` ("U5. Fel'rekt's Stateroom", page 143)

**Campaign, the Sea Maidens Faire structure doc (the room is a day-one residence in the campaign; see D8)**
> "**U5 (Fel'rekt's Stateroom).** Fel'rekt Lafeen is present unless ashore with Krebbyg (they move together). Less dangerous than Soluun — Fel'rekt will not kill unless cornered. He can be negotiated with (DC 14 Persuasion) if the party demonstrates they are not there to harm BD personnel. He values Krebbyg's safety above his own."
> — `campaign/structure/arc-h-sea-maidens-faire.md:172`

**Campaign, the Scarlet Marpenoth room file**
> "**U3 — Soluun's Stateroom:** Drow gunslinger Soluun Xibrindas, cleaning his weapons."
> — `campaign/locations/sea-maidens-faire/05-scarlet-marpenoth.md:40`
> "The three drow gunslingers are at combat readiness in their staterooms."
> — `campaign/locations/sea-maidens-faire/05-scarlet-marpenoth.md:48`

**Wiki (day-one residence, wiki line 67; WDH5e-p143)**
> "Fel'rekt resided at the ''[[Scarlet Marpenoth]]'' ship, where he cleaned his firearm."
> — wiki line 67

### A3. Former life

No source gives one. The only sourced statements about where he came from are A1 and "Unhappy with the treatment of males in his society" (`sources/adventure-wdh.json:32002`). The Persona line ("a society that punishes male drow") is the only other statement and is not in any source (D4).

### A4. Faith

Fel'rekt's own faith is not stated in any source.

**Campaign, the Lolth rule (history, GM-facing)**
> "- This is where the campaign rule starts. Jarlaxle rejected Lolth, Bregan D'aerthe rejects her, and its members speak of her as the goddess they walked away from. Soluun gives Jarlaxle the devotion that a drow of the houses would give the Spider Queen."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:34`

**Campaign, Fel'rekt under the rule (Lolth page)**
> "- **The Killer's Fate and Kreb Drops the Cover:** Soluun never says her name \"with anything but disgust\" (`campaign/quests/faction-events/bregan-daerthe/s05-the-killers-fate/ev-01-the-killers-fate.md:242`). Fel'rekt Lafeen \"never mentions Lolth\" (`s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:136`)."
> — `campaign/setting/deities/lolth.md:89`

**Campaign, the quest file it cites (quest time; the trait is sourced)**
> "He is warm toward the members and firm about discretion, because he knows what happens to drow the Watch catches. He never threatens anyone and never mentions Lolth."
> — `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:136`

### A5. Signature belongings

**Adventure, the gunslinger sidebar (before the entry)**
> "Firearms aren't widely available in the North, but some members of Bregan D'aerthe are equipped with Lantanese pistols, bullets, and packets of smokepowder. These {@creature drow gunslinger|wdh|drow gunslingers} are expert pistoleers, as skilled with their guns as the best archers are with their bows."
> — `sources/adventure-wdh.json:31995`

**Adventure, Game Statistics (page 202)**
> "{@creature Fel'rekt Lafeen|WDH} is a neutral good {@creature drow gunslinger|WDH}. In addition to his weapons, he carries four packets of {@item smokepowder|WDH} (see {@adventure appendix A|WDH|11}) and a pouch containing twenty pistol bullets."
> — `sources/adventure-wdh.json:32010`

**Wiki (WDH5e-p132)**
> "Like his fellow Soluun Xibrindas and Krebbyg Masq'il'yr, Fel'rekt was equipped with Lantanese [[firearm]]s."
> — wiki line 81

**Adventure, the footlocker (page 143)**
> "Fel'rekt's footlocker contains 65 gp in a pouch, a comb carved from dragon bone (worth 5 gp), and a pair of obsidian dice (worth 25 gp)."
> — `sources/adventure-wdh.json:26440`

**Villains page, the arming of lieutenants**
> "- He has an alliance with Lantan, arms his lieutenants with Lantanese firearms that run on smokepowder, and keeps the Lantanese submarine *Scarlet Marpenoth*. He plans to flee Waterdeep in it if his scheme unravels (`sources/adventure-wdh.json` line 32181)."
> — `campaign/setting/villains/jarlaxle.md:53`

### A6. Relationships (named figures)

**Krebbyg (closest friend and partner)**
> "Fel'rekt and {@creature Krebbyg Masq'il'yr|WDH} are close friends and work as a team, trading banter and jokes at their enemies' expense. Fel'rekt lacks the cruelty common to most drow, and he won't kill an adversary unless he is left with no other choice."
> — `sources/adventure-wdh.json:32003`
> "Fel'rekt and Krebbyg were a working team."
> — wiki line 78 (Relationship)
> "Fel'rekt is one of Jarlaxle's most loyal lieutenants, the close friend and operational partner of Krebbyg Masq'il'yr, and the Bregan D'aerthe operative who led the team at Gralhund Villa." — the page's own line, `campaign/setting/notable-figures/bregan-daerthe/03-felrekt-lafeen.md:25` (see C row 10)

**Soluun (sibling lieutenant; the three know his night habits)**
> "He conceals his nighttime escapades as well as he can, but Jarlaxle, Fel'rekt, and Krebbyg know what he's up to."
> — `sources/adventure-wdh.json:32041` (Soluun Xibrindas entry, page 202)

**Jarlaxle (the employer)**
> "Jarlaxle took a shine to Fel'rekt almost immediately, and the young drow has since become one of Jarlaxle's most loyal lieutenants."
> — `sources/adventure-wdh.json:32002`
> "A drow gunslinger and Jarlaxle's trusted lieutenant" — the page's Overview, `campaign/setting/notable-figures/bregan-daerthe/03-felrekt-lafeen.md:29` (C row 11)

**Fenerus's house (a Faction Outposts item, quest time)**
> "- A surveillance report from Fel'rekt Lafeen on the Gralhund Villa observation post, noting Zhentarim presence and gazer activity nearby."
> — `campaign/guides/factions/08-bregan-daerthe.md:90` (in the list of what the party finds at Fenerus Stormcastle's house)

**The pier stall (quest time; the Ches 21 date is the Faire's, see D9)**
> "The Faire fleet ties up at the Dock Ward pier on the morning of Ches 21. From then on Fel'rekt Lafeen (Neutral Good, Drow, he/him), the young lieutenant who works the stall for the company's members, is there whenever the ramps are open."
> — `campaign/quests/faction-events/bregan-daerthe/s04-contact-severed/ev-01-contact-severed.md:75` (the passage continues with the scene's trigger; the stall as a service is the Factions Guide's "through Fel'rekt Lafeen", A2)

### A7. Rank, post and time in post

- "one of Jarlaxle's most loyal lieutenants" (`sources/adventure-wdh.json:32002`).
- "was one of the top agents of the [[Bregan D'aerthe]] in [[Waterdeep]] during the early 1490s [[DR]]." (wiki line 64)
- "BD lieutenant" (`campaign/setting/organizations/07-bregan-daerthe.md:101`); "the captain's logistics lieutenant" (`campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:134` and `m06-the-dive/ev-01-the-dive.md:63`). See D1.
- Alexandrian Faction Outposts PDF, a report signed by him (transcription, PDF p.2, printed p.37): "A report from the Gralhund Villa observation team: 'Watchpost established in the manor south of the Gralhund Villa. ... – Fel'rekt Lafeen'" (the report is about the Gralhund observation post; see A6).

### A8. Habits

**Wiki (wiki line 67; WDH5e-p34)**
> "Fel'rekt and Krebbyg preferred to act during the night."

**Adventure, the recruitment watch (A2, `sources/adventure-wdh.json:3592`)**: the two watch the characters at night.

**Adventure, the Scarlet Marpenoth (page 143)**: "cleaning his pistol" (`sources/adventure-wdh.json:26433`).

**Wiki, the lieutenants' tasks (wiki line 67)**
> "Fel'rekt, together with [[Soluun Xibrindas]] and [[Krebbyg Masq'il'yr]], was tasked by [[Jarlaxle]] with doing dirty deeds in the city."

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, the page: "*Drow gunslinger, neutral good, he/him*. Stat block: **Drow Gunslinger**." — `campaign/setting/notable-figures/bregan-daerthe/03-felrekt-lafeen.md:5`
- Campaign, the org page: "- **Fel'rekt Lafeen** — Drow gunslinger, neutral good, and BD lieutenant." — `campaign/setting/organizations/07-bregan-daerthe.md:101`
- Campaign, the quest event tag: "Fel'rekt Lafeen (Neutral Good, Drow, he/him) :: a bright young drow gunslinger and the captain's logistics lieutenant, who would rather disarm anyone than hurt them and is never far from Krebbyg." — `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:134` (the same tag format is at `m06-the-dive/ev-01-the-dive.md:63`)
- Adventure: "{@creature Fel'rekt Lafeen|WDH} is a neutral good {@creature drow gunslinger|WDH}." — `sources/adventure-wdh.json:32010`
- Wiki: "| alignment5e    = [[Neutral good]]" — wiki line 59

**Species**
- Campaign: "*Drow gunslinger*" (`campaign/setting/notable-figures/bregan-daerthe/03-felrekt-lafeen.md:5`).
- Wiki: "| race           = [[Drow]]" — wiki line 15.
- Adventure: "a neutral good {@creature drow gunslinger|WDH}" — `sources/adventure-wdh.json:32010`.

**Pronouns**
- Campaign: "he/him" (`campaign/setting/notable-figures/bregan-daerthe/03-felrekt-lafeen.md:5`).
- Adventure: "Fel'rekt is a male drow who was born female." (`sources/adventure-wdh.json:32002`).
- Wiki: "| sex            = Male <br />{{Former}} Female" — wiki line 13.
- Campaign, the quest tags: "(Neutral Good, Drow, he/him)" (`campaign/quests/faction-events/bregan-daerthe/s04-contact-severed/ev-01-contact-severed.md:75`) and the same string at `s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:134`.

**Stat block**
- Campaign: "Stat block: **Drow Gunslinger**." — `campaign/setting/notable-figures/bregan-daerthe/03-felrekt-lafeen.md:5`
- Adventure: "{@creature Fel'rekt Lafeen|WDH} is a neutral good {@creature drow gunslinger|WDH}." — `sources/adventure-wdh.json:32010` (Game Statistics, page 202)
- Wiki: "| class5e        = [[Gunslinger]]" and "| refs5e         = <ref name=\"WDH5e-p201-202\">" — wiki lines 61-62.
- No numeric stat block (CR, HP, AC) for the drow gunslinger appears in the sources read. The Bestiary is not drafted (`campaign/structure/arc-h-sea-maidens-faire.md:338`: "Stat blocks for Soluun, Fel'rekt, Krebbyg (drow gunslingers).").

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/bregan-daerthe/03-felrekt-lafeen.md`. The page has no Background, Personality or Connections section yet. Each row gives the status and where the fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L5 | "*Drow gunslinger, neutral good, he/him*. Stat block: **Drow Gunslinger**." | Day-one (B) | section B |
| 2 | L6 | "- **Affiliation:** Bregan D'aerthe" | Day-one | `campaign/setting/organizations/07-bregan-daerthe.md:101` |
| 3 | L7 | "- **Featured in:** **Gralhund Villa**, **Faction Outposts**, **Sea Maidens Faire**" | Quest-name list (not narrative). It omits **Trollskull Alley** and **Bregan D'aerthe First Meeting**, which feature him (E2) | `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:26` |
| 4 | L11 | "**Resonance.** Fel'rekt should inspire admiration for his courage in leaving a society that rejected him, endearment with his eager-to-prove-himself energy, and trust with his refusal to kill when any other option exists." | Day-one. Keep (ruling 3) | `sources/adventure-wdh.json:32002`, `:32003` |
| 5 | L13 | "**Emotions.** Fel'rekt most often feels determined optimism, competitive enthusiasm, easy camaraderie with Krebbyg, genuine gratitude toward Jarlaxle, restless eagerness, and a stubborn refusal to let cruelty define him." | Day-one. Keep | `sources/adventure-wdh.json:32003`; voice profile line 69 |
| 6 | L15 | "**Motivations.** Fel'rekt wants to prove himself worthy of Jarlaxle's confidence, protect Krebbyg (his closest friend), and demonstrate that leaving drow society made him stronger rather than weaker." | Day-one. Keep | A1, A6 |
| 7 | L17 | "**Inspirations.** When playing Fel'rekt, channel Samwise Gamgee (*The Lord of the Rings*), Finn (*Star Wars*), and Sokka (*Avatar: The Last Airbender*)." | Not a fact. Keep | n/a |
| 8 | L21 | "**Persona.** To the world, Fel'rekt is a drow gunslinger, one of Jarlaxle's most trusted lieutenants. To those he trusts, he was born female in a society that punishes male drow; he petitioned to join Bregan D'aerthe and Jarlaxle took an immediate shine to him. Deep down, he lacks the cruelty common to most drow and will not kill an adversary unless left with no other choice." | Day-one, except "a society that punishes male drow", which goes beyond the adventure (D4). "Jarlaxle took an immediate shine" follows the adventure's "took a shine ... almost immediately" | `sources/adventure-wdh.json:32002`; `campaign/setting/organizations/07-bregan-daerthe.md:42` |
| 9 | L23 | "**Morale.** In a fight, Fel'rekt hurls himself into combat with verve, trading banter with Krebbyg at the enemies' expense. He volunteers for dangerous tasks first and disengages last." | Encounter behaviour, not a quest event. Brief ruling 3 keeps Morale verbatim; the drafter should know it is encounter-register | `sources/adventure-wdh.json:32002`, `:32003` |
| 10 | L25 | "**Relationships.** Fel'rekt is one of Jarlaxle's most loyal lieutenants, the close friend and operational partner of Krebbyg Masq'il'yr, and the Bregan D'aerthe operative who led the team at Gralhund Villa." | The first two clauses are day-one. **"who led the team at Gralhund Villa" is quest time.** Restate without it, or remove it and route to **Gralhund Villa** (list below) | see the Gralhund list below |
| 11 | L27-29 | "## Overview" / "A drow gunslinger and Jarlaxle's trusted lieutenant — eager to prove himself, reluctant to kill when any other option remains, and almost always accompanied by Krebbyg." | Day-one. **25 words** (brief limit 21). Draft a shorter Overview | `sources/adventure-wdh.json:32002`, `:32003` |

Row 10, the Gralhund facts the drafter routes (all quest time):
- `campaign/quests/act-ii/gralhund-villa/ev-02-saerdoun-street.md:53`: "If the party marked **Jarlaxle Informed** in **Fireball!**, Fel'rekt Lafeen's team occupies the empty Artheyn Manor directly across Saerdoun Street. The owner has relocated to the Moonshae Isles and the building is dark."
- `campaign/structure/arc-d-gralhund-villa.md:245`: "*Jarlaxle's Team in Motion (Conditional).* If Bregan D'aerthe is present in Artheyn Manor, this sequence plays out concurrent with beats 8–10 above, once the raid is fully committed:"
- `campaign/quests/act-ii/gralhund-villa/ev-06-the-gralhund-confrontation-day.md:49`: "The gunslingers take positions at G13's exterior windows and fire through the glass — two guards at the stairhead, neutralized. Fel'rekt Lafeen drops to the balcony (G17) with four drow."
- `campaign/quests/act-ii/gralhund-villa/overview.md:29`: "- **Fel'rekt Lafeen** (Bregan D'aerthe — conditional on **Jarlaxle Informed**) — the drow negotiator across the street; arrives through the balcony during the raid; his offer to Yalah is the cleanest sentence in the building: *\"The Stone, Lady Gralhund. That is all I am here for.\"*"

**Voice profile, the quest-time clauses (`.claude/skills/character-voices/voices/bregan-daerthe.md`, "### Fel'rekt Lafeen", lines 62-76)**

Lines with status:
- Line 65, "- **Sound:** A bright, earnest young drow voice that speeds up when he's excited." — day-one.
- Line 66, "- **Sentence shape:** Enthusiastic, medium sentences, plans and encouragement. When a fight looks likely, he offers alternatives aloud." — day-one habit; "When a fight looks likely" is an encounter cue.
- Line 67, "- **Word choice:** Loyal and hopeful: \"we can do this\", \"the captain trusts us\", \"there's another way\". He calls Krebbyg \"Kreb\" and Jarlaxle \"the captain\"." — day-one.
- Line 68, "- **Swearing:** *Casual · Plain · Phrase.* Occasional and excited (\"Oh, shit, that worked!\")." — day-one. The swearing stays (adult table).
- Line 69, "- **Personality in speech:** Determined optimism and competitiveness. His refusal to be cruel shows in how he keeps offering surrender. His gratitude to Jarlaxle is open and sincere." — day-one.
- Line 70, "- **Quirks:** He counts off options on his fingers. He checks on Kreb mid-sentence. He grins when a plan goes right." — day-one.
- Line 71, "- **Signature phrases:** \"There's another way.\" / \"Kreb, behind me.\" / \"The captain trusts us.\"" — "Kreb, behind me." is an encounter cue (the register of Ott's "Closer"). Flag for the drafter.
- Line 72, "- **Never:** He never kills when there's another option, never abandons Kreb, and never mocks surface folk." — day-one.
- Line 74, sample *Greeting*: "Hi! Fel'rekt. That's Kreb. We're with the captain, sort of. Mostly. It's complicated." — day-one.
- Line 75, sample *Business*: "We go in quiet, we take the ledger, nobody has to die. That's the plan. I like that plan." — **quest time**: "the ledger" is the nimblewright ledger, a Sea Maidens Faire item (`sources/Act_III_Arc_D.md:394`: "the ledger is a significant intelligence find"; `campaign/setting/villains/jarlaxle.md:56`). Flag; drop the ledger or reword.
- Line 76, sample *Under pressure*: "Drop it! Please drop it, I really don't want to shoot you!" — **encounter time**. Flag.

---

## D. Conflicts

**D1. "Logistics lieutenant" versus "BD lieutenant"**
- Org page, Fel'rekt: "- **Fel'rekt Lafeen** — Drow gunslinger, neutral good, and BD lieutenant." — `campaign/setting/organizations/07-bregan-daerthe.md:101`
- Org page, Krebbyg: "- **Krebbyg Masq'il'yr** — Drow gunslinger, chaotic neutral, and logistics lieutenant." — `campaign/setting/organizations/07-bregan-daerthe.md:102`
- Quest event, Fel'rekt (s02): "Fel'rekt Lafeen (Neutral Good, Drow, he/him) :: a bright young drow gunslinger and the captain's logistics lieutenant, who would rather disarm anyone than hurt them and is never far from Krebbyg." — `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:134`
- Quest event, Fel'rekt (m06): "Fel'rekt Lafeen (Neutral Good, Drow, he/him) :: a bright young drow gunslinger and the captain's logistics lieutenant, who counts his options off on his fingers and would rather disarm anyone than hurt them." — `campaign/quests/faction-events/bregan-daerthe/m06-the-dive/ev-01-the-dive.md:63`
- Krebbyg's page: "Krebbyg is the close friend and operational partner of Fel'rekt Lafeen, Jarlaxle's logistics lieutenant (collecting messages from Fenerus Stormcastle for the Scarlet Marpenoth), and the operating cover manager of the Seven Masks Theater." — `campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:25`
- The org page's own Draft Notes: "**Conflicts:** Krebbyg's role. This page's Key Members line, kept verbatim, calls him \"logistics lieutenant\". `m06-the-dive/ev-01-the-dive.md:63` and `s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:134` call Fel'rekt \"the captain's logistics lieutenant\", and `04-krebbyg-masqilyr.md:25` is ambiguous about which of the two it means. The page says \"BD lieutenant\" for Fel'rekt, as before." — `campaign/setting/organizations/07-bregan-daerthe.md:189`
- Not decided in the sources. The brief's ruling "Keep and note the tie" covers Zelifarn, Bonnie and Nessa Vayle only.

**D2. Whether his heritage is visible to the public**
- Campaign, the org page: "...and keeps his heritage to himself." — `campaign/setting/organizations/07-bregan-daerthe.md:101` (the full sentence is in A2)
- Campaign, the page's Persona: "To the world, Fel'rekt is a drow gunslinger, one of Jarlaxle's most trusted lieutenants." — `campaign/setting/notable-figures/bregan-daerthe/03-felrekt-lafeen.md:21`
- Alexandrian Trollskull appendix: "Fel'rekt does not disguise his heritage. He sits at the bar in the open, surface-dressed but with his coloring making no claim to anything it is not." — `sources/Appendix_D_-_Running_the_Tavern.md:1626`
- The sources do not say what "heritage" covers. The drafter has to choose one line for the Overview and Persona.

**D3. Krebbyg's message pickup frequency (this file's Fel'rekt cross-reference)**
- Campaign, the org page: "Collects messages from Fenerus Stormcastle's house every two days and carries them to the *Scarlet Marpenoth*." — `campaign/setting/organizations/07-bregan-daerthe.md:102`
- Campaign, Factions Guide: "Fenerus collects messages from dead drops throughout the Trades Ward and stores them at the house; Krebbyg picks them up every two days." — `campaign/guides/factions/08-bregan-daerthe.md:85`
- Campaign, Trades Ward gazetteer: "Fenerus gathers messages from dead drops across the ward and stores them at the house, and Krebbyg Masq'il'yr collects them every two days." — `campaign/gazetteer/waterdeep/trades-ward.md:39`
- Campaign, Faction Outposts structure doc: "Staking out the house and following Krebbyg Masq'il'yr (he visits every two days to drop or collect messages) leads directly to the Faire." — `campaign/structure/arc-e-faction-outposts.md:313`
- Alexandrian PDF (transcription): "Following Krebbyg: Krebbyg comes to collect messages from Fenerus once every 1d3 days." — `sources/5. Faction Outposts.pdf` PDF p.2 (printed p.37).
- Higher rank: campaign ("every two days"). The Alexandrian "every 1d3 days" is the older source. Krebbyg notes, D2.

**D4. How the page describes his origin**
- Page Persona (L21): "he was born female in a society that punishes male drow" — `campaign/setting/notable-figures/bregan-daerthe/03-felrekt-lafeen.md:21`
- Adventure: "Unhappy with the treatment of males in his society" — `sources/adventure-wdh.json:32002`
- Wiki: "disgusted with the treatment of males in [[drow]] society" — wiki line 70
- Campaign org page: "unhappy with the treatment of males in drow society" — `campaign/setting/organizations/07-bregan-daerthe.md:42`
- Higher rank: the adventure (published, above the wiki). "Punishes" is a stronger claim that no source makes.

**D5. Where Artheyn Manor is in relation to the villa**
- Gralhund quest journal: "If the party marked **Jarlaxle Informed** in **Fireball!**, Fel'rekt Lafeen's team occupies the empty Artheyn Manor directly across Saerdoun Street." — `campaign/quests/act-ii/gralhund-villa/ev-02-saerdoun-street.md:53`
- Gralhund design notes: "He does not mention that Fel'rekt Lafeen's team is already in Artheyn Manor, directly across the street." — `campaign/quests/act-ii/gralhund-villa/design-notes.md:31`
- Campaign, the Villains page: "where Fel'rekt Lafeen's team takes the empty Artheyn Manor across Saerdoun Street" — `campaign/setting/villains/jarlaxle.md:25`
- Alexandrian Gralhund file (older): "Jarlaxle already has Fel'rekt Lafeen's team in position at Artheyn Manor, directly north of Gralhund Villa." — `sources/Act_III_Arc_D.md:648`
- Alexandrian Gralhund file (older): "**Jarlaxle's Team** is billeted in **Artheyn Manor**, the vacant townhouse immediately north of the villa." — `sources/Act_III_Arc_E.md:74`
- Higher rank: the quest journal. The two Alexandrian lines say "north".

**D6. Whether Bregan D'aerthe takes the Stone**
- Alexandrian PDF (transcription): "The Bregan D'Aerthe team at Gralhund Villa (Part 2) successfully take possession of the *Stone of Golorr*." — `sources/9. Lair – Sea Maidens Faire.pdf` PDF p.1 (printed p.68).
- Campaign, the Gralhund journal: "| BD takes the Stone (Fel'rekt, conditional) | Bregan D'aerthe | ev-08 or ev-09 |" — `campaign/quests/act-ii/gralhund-villa/ev-06-the-gralhund-confrontation-day.md:96`
- Campaign, Gralhund structure doc: "*Jarlaxle's Team in Motion (Conditional).*" — `campaign/structure/arc-d-gralhund-villa.md:245`
- Higher rank: campaign (conditional). Do not state it as day-one.

**D7. Jarlaxle's knowledge at the start**
- Alexandrian PDF (transcription): "As *Dragon Heist* begins, Jarlaxle is unaware of the *Stone of Golorr* or the Grand Game which is being played." — `sources/1. The Villains.pdf` PDF p.5 (printed p.17)
- Campaign history: "- **Settled by the user (Session 47):** When Jarlaxle learned of the vault. \"He's known about it since getting to Waterdeep, whenever that was.\"" — `campaign/setting/history/03-bregan-daerthes-long-road.md:151`. The same Draft Note says "Overruled: the Alexandrian line that he is unaware of the Stone and the Grand Game at the start".
- Higher rank: campaign (the Session 47 ruling).

**D8. The stateroom numbers aboard the Scarlet Marpenoth**
- Campaign, Sea Maidens Faire area overview: "**Scarlet Marpenoth:** Three gnome pilots (U7b), Breena Bafflestone (gnome engineer, U2), three drow gunslingers (U3, U4, U5), four off-duty gnome engineers (U8)." — `campaign/locations/sea-maidens-faire/area-overview.md:34`
- Campaign, the room file: "**U4 — Jarlaxle's Stateroom:** Locked (DC 18 Thieves' Tools)." — `campaign/locations/sea-maidens-faire/05-scarlet-marpenoth.md:42`
- Campaign, the structure doc: "**U5 (Fel'rekt's Stateroom).**" (`campaign/structure/arc-h-sea-maidens-faire.md:172`) and "**U6 (Krebbyg's Stateroom).**" (`:174`)
- Adventure: "U5. Fel'rekt's Stateroom" (`sources/adventure-wdh.json:26429`) and "U6. Krebbyg's Stateroom" (`:26447`)
- Higher rank: the room file, the structure doc and the adventure agree on U5 and U6. The area overview lists U3, U4 and U5 as the gunslingers' rooms, which puts Jarlaxle's stateroom among the gunslingers' and omits U6. Fix in E1.

**D9. Sea Maidens Faire arrival date**
- Alexandrian PDF (transcription): "Ches 10th, announcing its arrival" — `sources/9. Lair – Sea Maidens Faire.pdf` PDF p.2 (printed p.69, EVENT SCHEDULE, carnival parades).
- Campaign: "The Faire fleet ties up at the Dock Ward pier on the morning of Ches 21." — `campaign/quests/faction-events/bregan-daerthe/s04-contact-severed/ev-01-contact-severed.md:75`; "The fleet reaches Deepwater Harbor on Ches 21, the opening day of Fleetswake, and leaves at dawn on Tarsakh 20" — `campaign/setting/villains/jarlaxle.md:52`
- Higher rank: campaign. The Alexandrian line is a parade date, which may not be the fleet's arrival.

**D10. Team size at Artheyn Manor (minor)**
- Quest journal: "Ground floor: Fel'rekt and two drow at a front-room watch post. Top floor: two drow gunslingers and six additional drow with a direct sightline to the villa's upper windows." — `campaign/quests/act-ii/gralhund-villa/ev-02-saerdoun-street.md:55`
- Alexandrian Gralhund file: "Fel'Rekt Lafeen, two additional Drow Gunslingers, and six Drow occupy a ground-floor watching post facing the villa's gate and an upper-floor observation room with sightlines to the balcony." — `sources/Act_III_Arc_E.md:74`
- Higher rank: the quest journal. The two versions differ on which rooms the gunslingers hold; the total is similar.

**D11. Trollskull tavern visitor (not a conflict in substance)**
- Alexandrian appendix: "Fel'rekt Lafeen most often in the early campaign" — `sources/Appendix_D_-_Running_the_Tavern.md:1610`
- Trollskull guide: "Fel'rekt Lafeen most often in the early campaign (Acts II–III)" — `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:87`. The two differ on the act range only.

---

## E. Stale lines in other files (do not edit) and routed quest references

**E1. Stale or conflicting lines in other files**
- `campaign/gazetteer/waterdeep/dock-ward.md:320`: "Fel'rekt Lafeen has a Notable Figures page, but the page names him once in passing and does not link him." Stale: the page exists and is a full Notable page.
- `campaign/gazetteer/waterdeep/trades-ward.md:38`: "Fenerus spies for Luskan. He followed Krebbyg once and knows where the messages go, but he has not worked out that the cloaked drow belong to Bregan D'aerthe." Also `:40`: "Fenerus believes his contacts are Luskan agents. He followed Krebbyg once and knows where the messages go, but he has not worked out that the cloaked drow belong to Bregan D'aerthe." These conflict with `campaign/setting/organizations/07-bregan-daerthe.md:104`: "Supposed to be a cut-out, but once followed Krebbyg after a pickup and knows the messages go to the Sea Maidens Faire." The Alexandrian PDF says "Fenerus once followed Krebbyg after Jarlaxle's lieutenant picked up the messages and knows that they're being taken to the Sea Maidens Faire." (PDF p.1, printed p.36, transcription). The Session 51 ruling at `campaign/setting/governance-and-guilds/guilds.md:122` settles Fenerus's knowledge in favour of the org page. That ruling cites the org page as line 103; the line is 104.
- `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:194`: "Hlam, Fel'rekt Lafeen and Kalain are named in passing and I did not open their pages (`bregan-daerthe/03-felrekt-lafeen.md` and `independents-allies/20-kalain.md` exist)." Stale: a research note that predates the page.
- `sources/Appendix_B_-_Player_Factions.md:792`: "Safe house access aboard the *Hellraiser* or *Hellbreaker*." The campaign files spell the ship "Heartbreaker" (`campaign/guides/factions/08-bregan-daerthe.md:56`). Not Fel'rekt's line, but it names his pier.
- `campaign/locations/sea-maidens-faire/area-overview.md:34`: "three drow gunslingers (U3, U4, U5)" — see D8.

**E2. Routed quest references (the quest-time facts on the page)**

Gralhund Villa (the quest that puts Fel'rekt's team on the page):
- `campaign/quests/act-ii/gralhund-villa/ev-02-saerdoun-street.md:53-55` (Artheyn Manor team; **Jarlaxle Informed**; quoted in C and D5)
- `campaign/quests/act-ii/gralhund-villa/ev-04-the-zhentarim-raid.md:76`: "2. Fel'rekt Lafeen and four drow drop to the Balcony (G17) and enter the upper floor." (the raid beats run to `:81`; `:83`: "**BD-affiliated PCs:** If any party member belongs to Bregan D'aerthe, Jarlaxle's gunslingers extend their covering fire to include that character during the raid, sniping threats the PC is engaged with through the upper-floor windows. Fel'rekt acknowledges the PC with a nod when their paths cross.")
- `campaign/quests/act-ii/gralhund-villa/ev-06-the-gralhund-confrontation-day.md:55`: "Fel'rekt enters through the glass doors to G16. Yalah reads this immediately: she retreats into G18 — the children's room — and locks the door from inside. Hrabbaz holds G16 against Fel'rekt, buying her the seconds she needs."
- `campaign/quests/act-ii/gralhund-villa/ev-06-the-gralhund-confrontation-day.md:57`: "Before Fel'rekt moves toward the G18 door, he turns to the party. His voice is level and carries no threat: *\"Jarlaxle sends his regards. You have been following the same trail we have — which means you already know what is in that room and what it is worth. I am not here to fight you. What I am here for is behind that door.\"*"
- `campaign/quests/act-ii/gralhund-villa/ev-07-the-gralhund-confrontation-night.md:59`, `:65` and `:67` (the night version of the same beats; `:67` is the same speech as ev-06:57)
- `campaign/quests/act-ii/gralhund-villa/ev-08-the-rooftop-chase.md:21`: "**Bregan D'aerthe.** Fel'rekt's team exits via the rooftops. They move fast and know where they are going: a BD outpost in the Trades Ward (Fenerus Stormcastle)."
- `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:44`: "By the morning of Ches 25th, the City Watch has sealed Gralhund Villa and begun processing twenty-three bodies. Lord Gralhund is in shock. Hrabbaz is dead if he held G16 against Fel'rekt, and alive if he stood down. No Stone, no nimblewright, no Floxin."
- `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:118`: "**Bregan D'aerthe — BD Operative in Party (conditional — **Jarlaxle Informed**).** No back-room invitation. Fel'rekt's debrief arrives through the operative's established channel — a direct, brief message, not an open offer to the group."
- `campaign/structure/arc-d-gralhund-villa.md:248`-`:253` (the raid timeline, beats 2 to 7) and `:255` ("**BD-Affiliated PCs:** If any party member belongs to Bregan D'aerthe, Jarlaxle's gunslingers extend their covering fire..." — the `:255` text differs from ev-04:83 in wording; both are quest time)
- `campaign/locations/gralhund-villa/g17-balcony.md:9`: "**BD assault route:** During the BD assault sequence (*Jarlaxle Informed*), Fel'rekt Lafeen and four drow use this balcony as their entry point — dropping from the rooftops and coming through the glass doors into G16. If the party is on the balcony when this happens, Fel'rekt acknowledges them with a glance and continues without breaking stride."
- `sources/Act_III_Arc_E.md:14` (the HTML bullet: "<li><strong>Bregan D'Aerthe:</strong> Fel'Rekt Lafeen and a team of drow in the neighboring Artheyn Manor. They will act when the moment is right.</li>"); also `:701` ("A DC 13 Wisdom (Perception) check spots Fel'Rekt Lafeen's team on the Artheyn roofline.") and `:729` ("Fel'Rekt Lafeen's team will make their move regardless of whether the characters are present. The only question is when.")

Sea Maidens Faire (the ship and the stateroom):
- `campaign/structure/arc-h-sea-maidens-faire.md:275`: "- **Jarlaxle Hostile** (combat, casualties among BD lieutenants): If the party killed Soluun, Fel'rekt, or Krebbyg, Jarlaxle's response escalates from professional to personal. He reaches for leverage before force, but he reaches harder. BD response teams become more aggressive in future encounters."
- `sources/adventure-wdh.json:14782`: "If {@creature Jarlaxle Baenre|WDH} (see {@adventure appendix B|WDH|12}) is the villain, he arrives with three {@creature drow gunslinger|WDH|drow gunslingers} (see {@adventure appendix B|WDH|12}). Replace no-name drow gunslingers with {@creature Fel'rekt Lafeen|WDH}, {@creature Krebbyg Masq'il'yr|WDH}, and {@creature Soluun Xibrindas|wdh} if they are alive and free."
- `sources/adventure-wdh.json:25120` (the armory safe; the three lieutenants know the combination)

Faction events (the day-one page must not restate these):
- `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:26`: "The watchers are Jarlaxle's three lieutenants. Fel'rekt Lafeen and Krebbyg Masq'il'yr shadow the party from dusk until dawn, and Soluun Xibrindas takes the day from shade and doorways." (the passage continues: "After dark Soluun also hunts elf and half-elf sailors in the Dock Ward on his own account, the subject of the Doom Raiders mission **The Dockside Killer**." and two more sentences)
- `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:403`: "A young man named Fel'rekt Lafeen will keep a stall on the pier once the carnival ships tie up on the morning of the twenty-first, and he'll see you properly equipped." (the passage continues: the box office and the mate)
- `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:134` and `:136` (see A4 and D1)
- `campaign/quests/faction-events/bregan-daerthe/m06-the-dive/ev-01-the-dive.md:5`: "This Combat and Exploration Event occurs after **Kolat Towers**, in the last hour of darkness. Fel'rekt Lafeen's watchers see a Xanathar's Guild dive team slip into the water beneath the old Faire pier at Smugglers' Dock." (the passage continues with the Event's end state); `:56` and `:63`
- `campaign/quests/faction-events/bregan-daerthe/s04-contact-severed/ev-01-contact-severed.md:83`: "Hi, I'm Fel'rekt. You've probably seen me around Trollskull Alley without knowing who I was. I'm not allowed to sell you anything, or really to talk to you, because the captain says so, and I don't argue with the captain. Nobody's going to hurt you, I promise. We just don't deal with you any more."
- `campaign/quests/faction-events/bregan-daerthe/s05-the-killers-fate/ev-01-the-killers-fate.md:503`: "Fel'rekt rows the members back to the south quay and leaves them on the steps."
- `campaign/quests/faction-events/bregan-daerthe/m03-three-nights/overview.md:23`: "Fel'rekt Lafeen watches from the roof of the Bent Nail each night and counts what comes through the doors. He does not interfere." (the passage opens with Jarlaxle learning of the guest)
- `campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/ev-02-twelve-minutes.md:186`: "Fel'rekt waits in the street above with a covered cart. He helps Nar'l under a tarpaulin, shakes everyone's hand in turn and drives the cart to the Faire's pier in the Dock Ward. He puts Nar'l aboard the *Heartbreaker*, and Nar'l says only that he is grateful."
- `campaign/quests/faction-events/bregan-daerthe/r50-houseless-noble/ev-01-houseless-noble.md:55`: "Two Scouts in stagehands' aprons open the dressing room door. Fel'rekt waits inside, and a closed cart takes the member and him down to the Dock Ward waterfront, where a skiff lies at the south quay steps."
- `campaign/quests/faction-events/bregan-daerthe/s01-coin-pouches/ev-01-coin-pouches.md:63`: "On the day of the Twin Parades, Dunstan followed the Beat 1 recipient into the Dock Ward and came within a street of the crate at Net and Dock before he lost them. Fel'rekt, who was watching the member for Bregan D'aerthe, saw him."

Trollskull guide and appendix (the tavern visitor; not day-one):
- `sources/Appendix_D_-_Running_the_Tavern.md:1610` (see D11)
- `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:83` (heading "## Bregan D'aerthe — Fel'rekt Lafeen (or Another Lieutenant)")

Factions Guide:
- `campaign/guides/factions/08-bregan-daerthe.md:90` (see A6)
- `campaign/guides/factions/08-bregan-daerthe.md:122`: "| Lockdown | Fel'rekt, Krebbyg, and Soluun deployed together. Jarlaxle intervenes personally, always with an offer rather than a fight. |"

Lore:
- `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:53`: "- **At Gralhund Villa:** The party takes the Stone from Yalah, or, if she surrenders it to Fel'rekt Lafeen, from the carrier in the rooftop chase. Holding it when the aftermath opens earns 1 Milestone Point and brings the party to Level 4."

Wiki (quest time, not day-one):
- wiki line 72: "In [[1492 DR]],{{WDH-time}} if Jarlaxle managed to obtain the ''[[Stone of Golorr]]'', then Fel'rekt and Krebbyg confronted some adventurers first in [[Mistshore]], where they had the support of the [[Lantanese]] mechanical [[dragon turtle]] [[Big Belchy]],<ref name=\"WDH5e-p67\">{{Cite book/Waterdeep: Dragon Heist|67}}</ref> and again in the [[Dock Ward]].<ref name=\"WDH5e-p72\">{{Cite book/Waterdeep: Dragon Heist|72}}</ref>"

Adventure (quest time, not day-one):
- `sources/adventure-wdh.json:8513`: "{@creature Fel'rekt Lafeen|WDH} and {@creature Krebbyg Masq'il'yr|WDH} start out 40 feet ahead of their pursuers. They do nothing but move on their turns, trying to put as much distance between themselves and the characters as possible. Fel'rekt has the {@item Stone of Golorr|WDH} at the start of the chase, but one drow gunslinger can pass the stone to the other as a reaction as long as the two drow are within 10 feet of each other."
- `sources/adventure-wdh.json:7568`: "At the end of their pursuit, the characters corner {@creature Fel'rekt Lafeen|WDH} and {@creature Krebbyg Masq'il'yr|WDH} in Mistshore."

---

## F. Gaps a Background needs that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

**F1. Birth year, birth name, home district, family, age.** No source gives any of these. The only age term is "the young drow" (`sources/adventure-wdh.json:32002`) and the wiki's "early 1490s DR" (wiki line 64). No source names a parent, sibling or house for him. Do not name a new Notable Figure (brief ruling 17). A nameless relative or place is allowed.

**F2. Former life before Bregan D'aerthe.** Only "Unhappy with the treatment of males in his society" (`sources/adventure-wdh.json:32002`). Constraint: the company's founding rule (`campaign/setting/history/03-bregan-daerthes-long-road.md:41`) and the Lolth rule (`:34`) bind any origin.

**F3. The change of sex and when it happened.** The wiki says "at some point changed to being male" (wiki line 70). The adventure says "a male drow who was born female" (`sources/adventure-wdh.json:32002`). The page uses he/him throughout. No source gives a date or a reason beyond "the treatment of males". The company's rule that "Almost all of them are male, because female drow rarely take orders from a male" (`campaign/setting/history/03-bregan-daerthes-long-road.md:41`) is the frame the drafter must keep.

**F4. How and when he petitioned, and how old he was.** Only "he petitioned to join Bregan D'aerthe" (`sources/adventure-wdh.json:32002`). No date.

**F5. Training with firearms.** Sourced only as "expert pistoleers, as skilled with their guns as the best archers are with their bows" (`sources/adventure-wdh.json:31995`) and "Lantanese pistols, bullets, and packets of smokepowder" (same line). The company's lieutenants are armed with Lantanese firearms that run on smokepowder (`campaign/setting/history/03-bregan-daerthes-long-road.md:69`). Where he learned to shoot is not sourced.

**F6. Relationship with his employer before he joined.** None. The sourced facts are "Jarlaxle took a shine to Fel'rekt almost immediately" (`sources/adventure-wdh.json:32002`) and "Almost immediately, Jarlaxle was impressed with Fel'rekt, who volunteered for all the most dangerous missions." (wiki line 70).

**F7. Losses, grudges, anyone he left behind.** None in any source.

**F8. Personal goals beyond the company.** None in any source. The page's Motivations give his wants toward Jarlaxle and Krebbyg (`campaign/setting/notable-figures/bregan-daerthe/03-felrekt-lafeen.md:15`). The Background explains where those come from. Brief ruling 17: the goals may not reveal a secret, an Event Outcome, a quest result or the Grand Game balance, and may not add a quest event. A goal about a place, a craft or a person he wants to keep is allowed as `[design]`.

**F9. Gralhund Villa role before the campaign.** None. The Gralhund team is conditional on **Jarlaxle Informed** (`campaign/quests/act-ii/gralhund-villa/ev-02-saerdoun-street.md:53`). The Alexandrian line is that the team "will act when the moment is right" (`sources/Act_III_Arc_E.md:14`). Keep it off day one.

**F10. Physical appearance.** None as a day-one fact. A quest scene describes him: "He is out of breath and his white hair has come loose from its tie" (`campaign/quests/faction-events/bregan-daerthe/m06-the-dive/ev-01-the-dive.md:54`). That is one scene, not a fixed description.

**F11. His cover in public.** See D2.

---

## G. Source facts that hint at the figure's inner life (for the backstory; do not contradict)

- "Eager to prove himself, Fel'rekt is quick to volunteer for tasks and hurls himself into combat with verve." — `sources/adventure-wdh.json:32002`
- "Fel'rekt lacks the cruelty common to most drow, and he won't kill an adversary unless he is left with no other choice." — `sources/adventure-wdh.json:32003`
- "Unhappy with the treatment of males in his society, he petitioned to join Bregan D'aerthe." — `sources/adventure-wdh.json:32002`
- "disgusted with the treatment of males in [[drow]] society" — wiki line 70 (see D4 for the wording)
- "who volunteered for all the most dangerous missions." — wiki line 70
- "Fel'rekt's footlocker contains 65 gp in a pouch, a comb carved from dragon bone (worth 5 gp), and a pair of obsidian dice (worth 25 gp)." — `sources/adventure-wdh.json:26440` (the footlocker in U5)
- "He values Krebbyg's safety above his own." — `campaign/structure/arc-h-sea-maidens-faire.md:172`
- "Fel'rekt argued that a contact who must wear a mask while taking messages will eventually slip, so members who have delivered two jobs have earned the face." — `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:17` (quest time; shows a trait: caution about cover)
- "He is warm toward the members and firm about discretion, because he knows what happens to drow the Watch catches." — `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:136` (quest time; the trait is sourced)
- "Deep down, he lacks the cruelty common to most drow and will not kill an adversary unless left with no other choice." — `campaign/setting/notable-figures/bregan-daerthe/03-felrekt-lafeen.md:21`
- "Fel'rekt wants to prove himself worthy of Jarlaxle's confidence, protect Krebbyg (his closest friend), and demonstrate that leaving drow society made him stronger rather than weaker." — `campaign/setting/notable-figures/bregan-daerthe/03-felrekt-lafeen.md:15`
- Voice, day-one: "His gratitude to Jarlaxle is open and sincere." (`.claude/skills/character-voices/voices/bregan-daerthe.md:69`); "He grins when a plan goes right." (line 70); "He never kills when there's another option, never abandons Kreb, and never mocks surface folk." (line 72)
- The closest person: "Fel'rekt and {@creature Krebbyg Masq'il'yr|WDH} are close friends" (`sources/adventure-wdh.json:32003`).

---

## Not found

- Birth year, birth name, home district, house, parents, family, age, date of joining, date of the sex change. Searched: `campaign/` (Grep for "Fel.?rekt" and "Lafeen"), `sources/adventure-wdh.json` (Grep for "Fel'rekt" and "Lafeen"), `sources/*.md` (Grep), `sources/research/` (Grep). No match gives any of these.
- Former life and faith beyond the Lolth rule: the same search. Only `campaign/setting/history/03-bregan-daerthes-long-road.md:34` and `ev-01-kreb-drops-the-cover.md:136`.
- Alexandrian PDFs for Fel'rekt. Read: `sources/5. Faction Outposts.pdf` (pp.1-2), `sources/17. Outpost and Lair Revelation Lists.pdf` (p.2), `sources/9. Lair – Sea Maidens Faire.pdf` (pp.1-3), `sources/1. The Villains.pdf` (p.5). Not read: `sources/4. Gralhund Villa.pdf`, `sources/3. Player Character Factions.pdf`, `sources/26. Addendum Other Collaborators.pdf`. Those may hold more BD text and were not checked for his name.
- Wiki: no line on his birth, parentage, home or age. The infobox fields `age` (wiki line 18), `dob` (line 23), `parents` (line 31) and `siblings` (line 33) are blank.

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. `sources/SOURCE_GUIDE.md:690` lists `Jarlaxle Baenre NPC Guide.docx` as the Jarlaxle persona source. Its lines are cited in `campaign/setting/history/03-bregan-daerthes-long-road.md:140` (the "third son" note). Not checked for Fel'rekt.
- The `campaign/quests/faction-events/bregan-daerthe/` event files and the Gralhund journal were read through Grep (the full files are too large to read whole). Quotes are exact Grep output.
