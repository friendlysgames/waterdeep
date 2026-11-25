# Pass 6 research notes: Krebbyg Masq'il'yr

Page: `campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR. Krebbyg is a named lieutenant of Jarlaxle and runs the Seven Masks Theater under the human cover "Kreb Sorrush" on day one. The cover's exposure, the members' missions and the Gralhund and Sea Maidens events are quest time. Cassalanter secrecy and the Lolth rule apply. Brief ruling 2 makes him a major NPC, so the full Personality and Connections apply.
Organization page: `campaign/setting/organizations/07-bregan-daerthe.md`
Voice profile: `.claude/skills/character-voices/voices/bregan-daerthe.md` ("### Krebbyg Masq'il'yr ("Kreb Sorrush")", lines 80-94)
Wiki extract: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-bregan-daerthe/04-krebbyg-masqilyr.txt` (quoted as "wiki line N", that file's lines; citation key `WDH5e`, *Waterdeep: Dragon Heist*, 5e)

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes are shown as plain quotes. `{@creature ...}` tags are left as written. The `page` field of an entry is given where one exists.
- Alexandrian PDFs: no shell, so `pdftotext` could not run. Three PDFs were read as rendered page images and their quotes are transcriptions. Check exact wording with `pdftotext -layout` before any quote goes into prose:
  - `sources/5. Faction Outposts.pdf` (printed pp.36-37 = PDF pp.1-2). Read: PDF pp.1-2.
  - `sources/17. Outpost and Lair Revelation Lists.pdf` (printed p.122 = PDF p.2). Read: PDF p.2.
  - `sources/9. Lair – Sea Maidens Faire.pdf` (printed pp.68-70 = PDF pp.1-3). Read: PDF pp.1-3.
- Alexandrian text files read: `sources/Appendix_B_-_Player_Factions.md`, `sources/Appendix_D_-_Running_the_Tavern.md`, `sources/Act_III_Arc_D.md`, `sources/Act_III_Arc_E.md`.
- The Grep tool cannot search the PDFs. The PDFs not read were not checked for his name (see Not found).
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **"Logistics lieutenant" is his label on the org page and his own page, and it is also Fel'rekt's label in two quest events.** The org page's Draft Notes flag it (`campaign/setting/organizations/07-bregan-daerthe.md:189`). His page's Relationships line uses it (L25). Details in D1.
2. **The message pickup is dated nowhere in the campaign, and the Alexandrian text dates it to the Faire's arrival.** The Relationships line (L25) gives the pickup as a day-one role. The PDF says "Since the Sea Maidens Faire arrived in Waterdeep, Fenerus has also been acting as a message drop" (PDF p.1, printed p.36, transcription). The campaign's fleet arrives on Ches 21 (`campaign/setting/villains/jarlaxle.md:52`), but the Scarlet Marpenoth "has been moored in the harbor all year" (`campaign/setting/history/03-bregan-daerthes-long-road.md:153`). The drafter should not date the pickup. See D3.
3. **The Overview is 34 words, over the 21-word limit** (L29). See C row 11.
4. **His pickup frequency: "every two days" in the campaign, "once every 1d3 days" in the Alexandrian PDF.** See D2.
5. **His human cover is public; the exposure is quest time.** The Persona says "To the world, Krebbyg operates as "Kreb Sorrush," the booking manager of the Seven Masks Theater" (L21). The cover's details and its exposure (the wig, the greasepaint, the members' Kreb Unmasked outcome) live in `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md`. See E2.
6. **No source gives his birth, home, house name, age or date of joining.** Section F lists what the drafter must invent. Invented material is tagged `[design]`.

---

## A. Background facts by theme

### A1. Origin, birth and early life (sourced only for the destroyed house)

**Adventure, the entry (page 202)**
> "Krebbyg's house was destroyed long ago, leaving him with no connection to his old life in the Underdark. He is young and rash."
> — `sources/adventure-wdh.json:32021` (entry "Krebbyg Masq'il'yr", page 202)

**Wiki, History (edition 5e, WDH5e-p202)**
> "After the destruction of his house, Krebbyg had no more connections in the [[underdark]] and so he joined [[Bregan D'aerthe]]."
> — wiki line 68 (History)

**Wiki, lead (edition 5e, WDH5e-p15)**
> "was one of the top agents of the [[Bregan D'aerthe]] in [[Waterdeep]] during the early 1490s [[DR]]."
> — wiki line 62 (lead; the sentence opens "'''Krebbyg Masq'il'yr''' (" with a pronunciation template before this clause)

**Adventure, pronunciation key**
> "{@creature Krebbyg Masq'il'yr|WDH}"
> "KREH-big MASK-il-eer"
> — `sources/adventure-wdh.json:193`-`:194`

**Campaign, Persona (the page's own account)**
> "**Persona.** To the world, Krebbyg operates as \"Kreb Sorrush,\" the booking manager of the Seven Masks Theater. To those he trusts, he is young, rash, and happy to let Fel'rekt do the thinking and talking. Deep down, his house was destroyed long ago, leaving him with no connection to his old life in the Underdark. The theater is the closest thing he has to a home outside Bregan D'aerthe."
> — `campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:21`

**Campaign, the organization page (the "Luskan accent" line)**
> "**Street Contact:** Krebbyg Masq'il'yr is usually at the Seven Masks Theater in the Dock Ward, where he operates as \"Kreb Sorrush,\" the theater's booking manager. He is a drow gunslinger with a relaxed professional manner and a slight Luskan accent that he makes no effort to conceal. He handles casting inquiries, performance schedules and faction intelligence requests with equal efficiency, switching between them mid-sentence. He does not explain who he works for."
> — `campaign/setting/organizations/07-bregan-daerthe.md:59`

**Campaign, the Dock Ward gazetteer (the Krebbyg block)**
> "- A young drow gunslinger who runs the Seven Masks Theater's bookings as Kreb Sorrush. He is rash and cheerful, and he leaves the thinking to Fel'rekt Lafeen."
> — `campaign/gazetteer/waterdeep/dock-ward.md:144`

No source gives his birth year, birth name, home district, house name, parents, family, or an age beyond "young" (see F1).

### A2. How he joined and how he rose

**Wiki (wiki line 68)**: "After the destruction of his house, Krebbyg had no more connections in the underdark and so he joined Bregan D'aerthe."

**Campaign, the Motivations (the company took him in)**
> "**Motivations.** Krebbyg wants to follow Fel'rekt into whatever comes next, run the Seven Masks Theater without Malkolm Brizzenbright's ghost interfering, and prove useful enough that Jarlaxle never regrets taking him in."
> — `campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:15`

**Campaign, the Dock Ward block (the theater's role and his hook; quest-name references)**
> "- Hook: he sends the theater invitation after **Fireball!**, and he is the contact for many Bregan D'aerthe missions, including **The Theater's Back Room** and **Kreb Drops the Cover**."
> — `campaign/gazetteer/waterdeep/dock-ward.md:145` (quest-time hook; see E2)

**Campaign, the organization page label**
> "- **Krebbyg Masq'il'yr** — Drow gunslinger, chaotic neutral, and logistics lieutenant. Operates as \"Kreb Sorrush\" at the Seven Masks Theater. Collects messages from Fenerus Stormcastle's house every two days and carries them to the *Scarlet Marpenoth*. See the **Krebbyg Masq'il'yr** page in Notable Figures."
> — `campaign/setting/organizations/07-bregan-daerthe.md:102` (Key Members)

**Campaign, the Factions Guide (the theater as a Bregan D'aerthe front)**
> "The theater is a Bregan D'aerthe front. Rongquan Mystere is a disguise of Jarlaxle's, and Kreb Sorrush is Krebbyg. One dressing room is kept empty as a safe house, with two drow guards inside whenever it is in use."
> — `campaign/gazetteer/waterdeep/dock-ward.md:75` (GM Notes)

**Campaign, the Factions Guide, the message pickup**
> "Fenerus collects messages from dead drops throughout the Trades Ward and stores them at the house; Krebbyg picks them up every two days."
> — `campaign/guides/factions/08-bregan-daerthe.md:85` (Fenerus Stormcastle, Use the description from DH p. 63)

**Campaign, the Dock Ward GM notes (the errand)**
> "- Krebbyg works for Bregan D'aerthe and reports to Jarlaxle. His errand outside the ward is the message pickup at Fenerus Stormcastle's house in the Trades Ward."
> — `campaign/gazetteer/waterdeep/dock-ward.md:149`

**Wiki, the lieutenants' tasks (wiki line 65; WDH5e-p15)**
> "Krebbyg, together with [[Soluun Xibrindas]] and [[Fel'rekt Lafeen]], was tasked by [[Jarlaxle]] with doing dirty deeds in the city."

**Adventure, the lieutenants' work (the Dock Ward watch; quest-time use, routed in E2)**
> "{@creature Fel'rekt Lafeen|WDH} and {@creature Krebbyg Masq'il'yr|WDH} watch the characters at night, and {@creature Soluun Xibrindas|wdh} watches them during the day (doing his best to stay out of the sunlight)."
> — `sources/adventure-wdh.json:3592` (chapter not checked; the passage concerns new recruits)

### A3. Former life and the Underdark

The only source fact is the destroyed house (A1). The wiki says "no more connections in the underdark" (wiki line 68). The page's Persona says "no connection to his old life in the Underdark" (L21), which repeats the adventure's wording at `sources/adventure-wdh.json:32021`. No house name, city or rank is given.

### A4. Faith

Krebbyg's own faith is not stated in any source.

**Campaign, the Lolth rule (history, GM-facing)**
> "- This is where the campaign rule starts. Jarlaxle rejected Lolth, Bregan D'aerthe rejects her, and its members speak of her as the goddess they walked away from. Soluun gives Jarlaxle the devotion that a drow of the houses would give the Spider Queen."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:34`

**Campaign, the Lolth page (the events where the rule applies; Krebbyg's own speeches)**
> "- **Houseless Noble, The Dockside Killer, Kreb Drops the Cover, The Killer's Fate, The Compromised Eye:** Each repeats the rule or applies it to a speech. The lines are in the GM Notes."
> — `campaign/setting/deities/lolth.md:77`

**Campaign, the Kreb Drops the Cover voice line (quest time; the rule is sourced)**
> "Krebbyg and Fel'rekt both say \"the captain\" and never Jarlaxle's name."
> — `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:24`

### A5. Signature belongings and skill

**Adventure, the gunslinger sidebar (before the entries)**
> "Firearms aren't widely available in the North, but some members of Bregan D'aerthe are equipped with Lantanese pistols, bullets, and packets of smokepowder. These {@creature drow gunslinger|wdh|drow gunslingers} are expert pistoleers, as skilled with their guns as the best archers are with their bows."
> — `sources/adventure-wdh.json:31995`

**Adventure, Game Statistics (page 202)**
> "{@creature Krebbyg Masq'il'yr|WDH} is a chaotic neutral {@creature drow gunslinger|WDH}. In addition to his weapons, he carries four packets of {@item smokepowder|WDH} (see {@adventure appendix A|WDH|11}) and a pouch containing twenty pistol bullets."
> — `sources/adventure-wdh.json:32029`

**Wiki (WDH5e-p132)**
> "Like his fellows Soluun Xibrindas and Fel'rekt Lafeen, Krebbyg was equipped with Lantanese [[firearm]]s."
> — wiki line 79

**Adventure, the stateroom (page 143)**
> "If he has not been encountered and defeated elsewhere, a {@creature drow gunslinger|WDH} named {@creature Krebbyg Masq'il'yr|WDH} (see {@adventure appendix B|WDH|12}) is here, sharpening his sword. His stateroom contains a net hammock and nothing else."
> — `sources/adventure-wdh.json:26451` ("U6. Krebbyg's Stateroom", page 143)

**Wiki, the same room (WDH5e-p143)**
> "Krebbyg resided on the ''[[Scarlet Marpenoth]]'' ship where he sharpened his sword."
> — wiki line 65

**Campaign, the Voice profile's cover (theatre skill)**
> "- **Word choice:** Theatre jargon (bookings, blocking, the house, the ghost), laid over gang talk. As Kreb Sorrush he calls everyone \"darling\"."
> — `.claude/skills/character-voices/voices/bregan-daerthe.md:85`

### A6. Relationships (named figures)

**Fel'rekt (closest friend and partner)**
> "Krebbyg works closely with {@creature Fel'rekt Lafeen|WDH}, and the two collaborate well despite their disparate alignments. Krebbyg prefers to follow Fel'rekt's lead, letting him do most of the thinking and talking."
> — `sources/adventure-wdh.json:32022`
> "Fel'rekt and Krebbyg were a working team." — wiki line 76 (Relationship)
> "Krebbyg is the close friend and operational partner of Fel'rekt Lafeen, Jarlaxle's logistics lieutenant (collecting messages from Fenerus Stormcastle for the Scarlet Marpenoth), and the operating cover manager of the Seven Masks Theater." — the page's own line, `campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:25` (C row 8)

**Soluun (the sibling lieutenant; the three know his nights)**
> "He conceals his nighttime escapades as well as he can, but Jarlaxle, Fel'rekt, and Krebbyg know what he's up to."
> — `sources/adventure-wdh.json:32041` (Soluun Xibrindas entry, page 202)

**Malkolm Brizzenbright (the ghost of the theater's founder)**
> "The ghost is Malkolm Brizzenbright, the theater's founder. He is not hostile, and he will tell a respectful visitor that \"Rongquan\" is a false identity and that drow come and go at irregular hours."
> — `campaign/gazetteer/waterdeep/dock-ward.md:76`
> The page's own line: "run the Seven Masks Theater without Malkolm Brizzenbright's ghost interfering" (`campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:15`). The Malkolm page (`campaign/setting/notable-figures/bregan-daerthe/07-malkolm-brizzenbright.md`) does not mention Krebbyg (Grep, no match).

**Jarlaxle (the employer; his disguise is the theater's owner)**
> "Playbills name the owner as Rongquan Mystere, and a booking manager who calls himself Kreb Sorrush handles casting inquiries and schedules." — `campaign/gazetteer/waterdeep/dock-ward.md:70`

**Fenerus Stormcastle (the message drop he collects from)**
> "Fenerus collects messages from dead drops throughout the Trades Ward and stores them at the house; Krebbyg picks them up every two days." — `campaign/guides/factions/08-bregan-daerthe.md:85`
> "Krebbyg Masq'il'yr collects them every two days." — `campaign/gazetteer/waterdeep/trades-ward.md:39`
> "Fenerus Stormcastle's house on Quill Alley is a Bregan D'aerthe message drop." — `campaign/gazetteer/waterdeep/trades-ward.md:37`

### A7. Rank, post and the theater

- "logistics lieutenant" (`campaign/setting/organizations/07-bregan-daerthe.md:102`; see D1).
- "operating cover manager of the Seven Masks Theater" (`campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:25`).
- "the contact for many Bregan D'aerthe missions" (`campaign/gazetteer/waterdeep/dock-ward.md:145`).
- "The theater is a Bregan D'aerthe front" (`campaign/gazetteer/waterdeep/dock-ward.md:75`).
- The Alexandrian Dock Ward file: "One of the dressing rooms is kept empty as a safe house for D'Aerthe agents in trouble." (PDF p.2, printed p.37, transcription; `sources/5. Faction Outposts.pdf`).
- Time in post: "during the early 1490s [[DR]]" (wiki line 62). No date for when he took the booking post.

### A8. Habits and temperament (day-one sources)

**Wiki (wiki line 65; WDH5e-p34)**
> "Krebbyg and Fel'rekt preferred to act during the night."

**Wiki (wiki line 73; WDH5e-p202)**
> "Krebbyg was young and rash. He preferred to follow Fel'rekt's leadership."

**Adventure (see A6, `sources/adventure-wdh.json:32022`)**: "Krebbyg prefers to follow Fel'rekt's lead, letting him do most of the thinking and talking."

**Voice profile, day-one habits (`.claude/skills/character-voices/voices/bregan-daerthe.md`, lines 83-90)**
> "- **Personality in speech:** Reckless confidence and deference. He defers to Fel'rekt immediately on anything serious (\"Ask Fel.\"). He gets bored with anything routine, and it's obvious. His pleasure in the theatre is real."
> "- **Never:** He never plans, never argues with Fel'rekt, and never lets anyone insult the theatre."

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, the page: "*Drow gunslinger, chaotic neutral, he/him*. Stat block: **Drow Gunslinger**." — `campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:5`
- Campaign, the org page: "- **Krebbyg Masq'il'yr** — Drow gunslinger, chaotic neutral, and logistics lieutenant." — `campaign/setting/organizations/07-bregan-daerthe.md:102`
- Campaign, the Dock Ward block: "**Krebbyg Masq'il'yr (Chaotic Neutral, Drow, he/him)**" — `campaign/gazetteer/waterdeep/dock-ward.md:143`
- Campaign, the quest tag: "Krebbyg Masq'il'yr (Chaotic Neutral, Drow, he/him) :: a young drow gunslinger who has run the Seven Masks' bookings as the human Kreb Sorrush" — `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:85`
- Adventure: "{@creature Krebbyg Masq'il'yr|WDH} is a chaotic neutral {@creature drow gunslinger|WDH}." — `sources/adventure-wdh.json:32029`
- Wiki: "| alignment5e    = [[Chaotic neutral]]" — wiki line 57.

**Species**
- Campaign: "*Drow gunslinger*" (`campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:5`).
- Wiki: "| race           = [[Drow]]" — wiki line 14.
- Adventure: "a chaotic neutral {@creature drow gunslinger|WDH}" — `sources/adventure-wdh.json:32029`.

**Pronouns**
- Campaign: "he/him" (`campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:5`); the Dock Ward block "(Chaotic Neutral, Drow, he/him)" (`campaign/gazetteer/waterdeep/dock-ward.md:143`).
- Adventure: "He is young and rash." (`sources/adventure-wdh.json:32021`).
- Wiki: "| sex            = Male " — wiki line 13.

**Stat block**
- Campaign: "Stat block: **Drow Gunslinger**." — `campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:5`
- Adventure: "{@creature Krebbyg Masq'il'yr|WDH} is a chaotic neutral {@creature drow gunslinger|WDH}." — `sources/adventure-wdh.json:32029` (Game Statistics, page 202)
- Wiki: "| class5e        = [[Gunslinger]]" and "| refs5e         = <ref name=\"WDH5e-p202\">" — wiki lines 59-60.
- No numeric stat block (CR, HP, AC) appears in the sources read. The Bestiary is not drafted (`campaign/structure/arc-h-sea-maidens-faire.md:338`: "Stat blocks for Soluun, Fel'rekt, Krebbyg (drow gunslingers).").

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md`. The page has no Background, Personality or Connections section yet.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L5 | "*Drow gunslinger, chaotic neutral, he/him*. Stat block: **Drow Gunslinger**." | Day-one (B) | section B |
| 2 | L6 | "- **Affiliation:** Bregan D'aerthe" | Day-one | `campaign/setting/organizations/07-bregan-daerthe.md:102` |
| 3 | L7 | "- **Featured in:** **Faction Outposts**, **Sea Maidens Faire**, **The Handkerchief and the Girl**, **The Wazoo Affair**, **The Betrayal Pitch**, **Three Nights**, **The Compromised Eye**, **The Theater's Back Room**, **The Dive**" | Quest-name list. Keep as a list of quest names (not narrative). It omits **Bregan D'aerthe First Meeting**, **Kreb Drops the Cover** and **Coin Pouches**, which feature him (E2) | `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:7` |
| 4 | L11 | "**Resonance.** Krebbyg should inspire amusement with his rash energy, endearment with his deference to Fel'rekt, and curiosity about what an Underdark exile makes of a career managing a Waterdeep theater." | Day-one. Keep (ruling 3) | `sources/adventure-wdh.json:32021` |
| 5 | L13 | "**Emotions.** Krebbyg most often feels reckless confidence, cheerful deference to Fel'rekt's judgment, restless boredom with routine, creative pleasure in his theater cover identity, mischievous humor, and an eagerness that substitutes for planning." | Day-one. Keep | voice profile lines 87 and 90 |
| 6 | L15 | "**Motivations.** Krebbyg wants to follow Fel'rekt into whatever comes next, run the Seven Masks Theater without Malkolm Brizzenbright's ghost interfering, and prove useful enough that Jarlaxle never regrets taking him in." | Day-one. Keep. "taking him in" is the company's recruitment, which the wiki dates to after the house fell (wiki line 68) | A2; `campaign/gazetteer/waterdeep/dock-ward.md:76` |
| 7 | L17 | "**Inspirations.** When playing Krebbyg, channel Rocket Raccoon (*Guardians of the Galaxy*), Jesse Pinkman (*Breaking Bad*), and Mushu (*Mulan*)." | Not a fact. Keep | n/a |
| 8 | L21 | "**Persona.** To the world, Krebbyg operates as \"Kreb Sorrush,\" the booking manager of the Seven Masks Theater. To those he trusts, he is young, rash, and happy to let Fel'rekt do the thinking and talking. Deep down, his house was destroyed long ago, leaving him with no connection to his old life in the Underdark. The theater is the closest thing he has to a home outside Bregan D'aerthe." | Day-one. The "To the world" cover is public (the Dock Ward block says the same). The exposure is quest time (E2) | `sources/adventure-wdh.json:32021`; `campaign/gazetteer/waterdeep/dock-ward.md:70` |
| 9 | L23 | "**Morale.** In a fight, Krebbyg follows Fel'rekt's lead, trading banter and covering flanks. He acts before thinking and relies on Fel'rekt to tell him when to stop." | Encounter behaviour, not a quest event. Brief ruling 3 keeps Morale verbatim; the drafter should know it is encounter-register | `sources/adventure-wdh.json:32022` |
| 10 | L25 | "**Relationships.** Krebbyg is the close friend and operational partner of Fel'rekt Lafeen, Jarlaxle's logistics lieutenant (collecting messages from Fenerus Stormcastle for the Scarlet Marpenoth), and the operating cover manager of the Seven Masks Theater." | The friendship and the cover manager role are day-one. "logistics lieutenant" is the disputed label (D1). "collecting messages from Fenerus Stormcastle" is a day-one role in the org page (`:102`) but its start date is not sourced (D3) | `campaign/setting/organizations/07-bregan-daerthe.md:102`; `campaign/guides/factions/08-bregan-daerthe.md:85` |
| 11 | L27-29 | "## Overview" / "A drow gunslinger who operates as \"Kreb Sorrush,\" booking manager of the Seven Masks Theater in the Dock Ward — handles casting inquiries, performance schedules, and other requests with equal efficiency, switching between them mid-sentence." | Day-one. **34 words** (brief limit 21). Draft a shorter Overview | `campaign/gazetteer/waterdeep/dock-ward.md:70`; voice line 85 |

**Voice profile, the quest-time clauses (`.claude/skills/character-voices/voices/bregan-daerthe.md`, lines 80-94)**

Lines with status:
- Line 83, "- **Sound:** A quick, cheerful, slightly frantic voice, a stage manager's patter." — day-one.
- Line 84, "- **Sentence shape:** Rapid run-on sentences that switch topics mid-flow (\"the Tuesday matinee's full, did you bring the package, no, not you, the soprano\")." — day-one.
- Line 85, "- **Word choice:** Theatre jargon (bookings, blocking, the house, the ghost), laid over gang talk. As Kreb Sorrush he calls everyone \"darling\"." — day-one.
- Line 86, "- **Swearing:** *Punctuation · Colourful · Phrase.* Casual and constant backstage (\"Where's the fucking soprano?\")." — day-one. The swearing stays (adult table).
- Line 87, "- **Personality in speech:** Reckless confidence and deference. He defers to Fel'rekt immediately on anything serious (\"Ask Fel.\"). He gets bored with anything routine, and it's obvious. His pleasure in the theatre is real." — day-one.
- Line 88, "- **Quirks:** He checks a schedule while talking. He complains about the ghost moving his props. He answers \"What's the plan?\" with \"Fel?\"" — day-one.
- Line 89, "- **Signature phrases:** \"Ask Fel.\" / \"The ghost moved it again.\" / \"Darling.\"" — day-one.
- Line 90, "- **Never:** He never plans, never argues with Fel'rekt, and never lets anyone insult the theatre." — day-one.
- Line 92, sample *Greeting*: "Kreb Sorrush, bookings, how can I help, casting's on Tuesdays, sorry, darling, who sent you?" — day-one.
- Line 93, sample *Business*: "You want in the basement? Ha, no. Ask Fel. Also the ghost hates you already, don't take it personally." — **Flag.** "the basement" has no source for the Seven Masks Theater. A search of `campaign/` for "basement" returns the Cassalanter and Xanathar files and no Seven Masks entry (see F8). The business register is the drafter's call.
- Line 94, sample *Under pressure*: "Fel! Fel, it's happening! What do we do?" — **encounter time**. Flag.

Also: Malkolm's voice profile (line 147, "There is a machine in my basement, Lantanese, hideous, and a door I never built") is the only other "basement" reference in the voices. Flag for the Malkolm page.

---

## D. Conflicts

**D1. "Logistics lieutenant" versus "BD lieutenant"**
- Org page, Krebbyg: "- **Krebbyg Masq'il'yr** — Drow gunslinger, chaotic neutral, and logistics lieutenant." — `campaign/setting/organizations/07-bregan-daerthe.md:102`
- Org page, Fel'rekt: "- **Fel'rekt Lafeen** — Drow gunslinger, neutral good, and BD lieutenant." — `campaign/setting/organizations/07-bregan-daerthe.md:101`
- Quest events, Fel'rekt: "a bright young drow gunslinger and the captain's logistics lieutenant, who would rather disarm anyone than hurt them and is never far from Krebbyg." — `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:134`; and "...the captain's logistics lieutenant, who counts his options off on his fingers..." — `campaign/quests/faction-events/bregan-daerthe/m06-the-dive/ev-01-the-dive.md:63`
- The org page's Draft Notes: "**Conflicts:** Krebbyg's role. This page's Key Members line, kept verbatim, calls him \"logistics lieutenant\". `m06-the-dive/ev-01-the-dive.md:63` and `s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:134` call Fel'rekt \"the captain's logistics lieutenant\", and `04-krebbyg-masqilyr.md:25` is ambiguous about which of the two it means. The page says \"BD lieutenant\" for Fel'rekt, as before." — `campaign/setting/organizations/07-bregan-daerthe.md:189`
- Not decided in the sources.

**D2. Pickup frequency**
- Campaign, the org page: "Collects messages from Fenerus Stormcastle's house every two days and carries them to the *Scarlet Marpenoth*." — `campaign/setting/organizations/07-bregan-daerthe.md:102`
- Campaign, the Factions Guide: "Krebbyg picks them up every two days." — `campaign/guides/factions/08-bregan-daerthe.md:85`
- Campaign, the Trades Ward gazetteer: "Krebbyg Masq'il'yr collects them every two days." — `campaign/gazetteer/waterdeep/trades-ward.md:39`
- Campaign, the Faction Outposts structure doc: "Staking out the house and following Krebbyg Masq'il'yr (he visits every two days to drop or collect messages) leads directly to the Faire." — `campaign/structure/arc-e-faction-outposts.md:313`
- Campaign, the Faction Outposts structure doc, the Operation step: "Krebbyg writing to Jarlaxle" — `campaign/structure/arc-e-faction-outposts.md:333` (no frequency)
- Alexandrian PDF (transcription): "Following Krebbyg: Krebbyg comes to collect messages from Fenerus once every 1d3 days." — `sources/5. Faction Outposts.pdf` PDF p.2 (printed p.37).
- Higher rank: campaign ("every two days"). The Alexandrian "every 1d3 days" is the older source.

**D3. When the message drop began**
- Alexandrian PDF (transcription): "Since the Sea Maidens Faire arrived in Waterdeep, Fenerus has also been acting as a message drop for Bregan D'Aerthe." — `sources/5. Faction Outposts.pdf` PDF p.1 (printed p.36).
- Campaign, the fleet's arrival: "The fleet reaches Deepwater Harbor on Ches 21, the opening day of Fleetswake, and leaves at dawn on Tarsakh 20" — `campaign/setting/villains/jarlaxle.md:52`
- Campaign, the Scarlet Marpenoth: "In the campaign it has been moored in Deepwater Harbor since he reached the city, and the carnival fleet joins it for Fleetswake." — `campaign/setting/history/03-bregan-daerthes-long-road.md:69`
- Campaign, the message role itself is undated (no source gives a start date for the pickup).
- Higher rank: none. The drafter should not date the pickup. The page's L25 gives it as a current role.

**D4. Whether Fenerus knows the drow are Bregan D'aerthe**
- Trades Ward gazetteer: "Fenerus spies for Luskan. He followed Krebbyg once and knows where the messages go, but he has not worked out that the cloaked drow belong to Bregan D'aerthe." — `campaign/gazetteer/waterdeep/trades-ward.md:38` and "Fenerus believes his contacts are Luskan agents." — `:40`
- Org page: "Supposed to be a cut-out, but once followed Krebbyg after a pickup and knows the messages go to the Sea Maidens Faire." — `campaign/setting/organizations/07-bregan-daerthe.md:104`
- Alexandrian PDF (transcription): "Questioning Fenerus: Although he's supposed to be a cut-out, Fenerus once followed Krebbyg after Jarlaxle's lieutenant picked up the messages and knows that they're being taken to the Sea Maidens Faire." — `sources/5. Faction Outposts.pdf` PDF p.1 (printed p.36).
- The Session 51 ruling at `campaign/setting/governance-and-guilds/guilds.md:122` settles Fenerus's knowledge in favour of the org page. That ruling cites the org page as line 103; the line is 104.
- Higher rank: the org page (the Session 51 ruling). The Trades Ward gazetteer is stale on what Fenerus has worked out.

**D5. His human cover: "human" or "drow" in the public record**
- Campaign, the Persona: "To the world, Krebbyg operates as \"Kreb Sorrush,\" the booking manager of the Seven Masks Theater." (`campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:21`)
- Campaign, the Dock Ward block: "Playbills name the owner as Rongquan Mystere, and a booking manager who calls himself Kreb Sorrush handles casting inquiries and schedules." (`campaign/gazetteer/waterdeep/dock-ward.md:70`)
- The campaign does not say the public knows Kreb Sorrush is a drow. The Dock Ward GM notes say "Kreb Sorrush is Krebbyg" (`campaign/gazetteer/waterdeep/dock-ward.md:75`), and the Kreb Drops the Cover event says the cover is "a human stage manager with a brown wig" (`campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:15`). Not a conflict, but the drafter should say "human cover" and not "a human".
- Higher rank: the campaign files agree. The phrase "to the world" in the Persona is the only public statement.

**D6. Luskan accent**
- Org page: "a slight Luskan accent that he makes no effort to conceal" (`campaign/setting/organizations/07-bregan-daerthe.md:59`).
- Adventure: no accent given (`sources/adventure-wdh.json:32017`-`:32032`).
- Voice profile: no accent given (`.claude/skills/character-voices/voices/bregan-daerthe.md:83`-`:90`).
- Not a conflict. Only the org page gives an accent, and it is the day-one source.

**D7. Quest-time text that calls Krebbyg "a drow lieutenant" (cover details)**
- "Kreb Sorrush is a drow lieutenant who passes as a human stage manager with a brown wig, pale greasepaint and gloves he never takes off." — `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:15` (quest time). The wig, the greasepaint and the gloves are in this event only.

**D8. Stateroom**
- Adventure: "U6. Krebbyg's Stateroom" (`sources/adventure-wdh.json:26447`); "His stateroom contains a net hammock and nothing else." (`:26451`)
- Campaign, the structure doc: "**U6 (Krebbyg's Stateroom).** Krebbyg Masq'il'yr is present unless ashore with Fel'rekt (they move together). Reckless, follows Fel'rekt's lead. If Fel'rekt has been neutralized or agreed to stand down, Krebbyg follows suit. If Fel'rekt is in danger, Krebbyg fights without thinking." — `campaign/structure/arc-h-sea-maidens-faire.md:174`
- Campaign, the Scarlet Marpenoth area overview: "three drow gunslingers (U3, U4, U5)" (`campaign/locations/sea-maidens-faire/area-overview.md:34`) omits U6. See Fel'rekt notes D8.

---

## E. Stale lines in other files (do not edit) and routed quest references

**E1. Stale or conflicting lines in other files**
- `campaign/gazetteer/waterdeep/trades-ward.md:38` and `:40`: see D4.
- `campaign/gazetteer/waterdeep/dock-ward.md:320`: "Names with no page: ... Rongquan Mystere and Kreb Sorrush (aliases of Jarlaxle and Krebbyg) ... appear as plain text." Stale: Krebbyg has a Notable Figures page (`campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md`).
- `campaign/gazetteer/waterdeep/dock-ward.md:254`: "**Krebbyg Masq'il'yr**, **Soluun Xibrindas**..." (the characters of interest). Not stale.
- `campaign/setting/organizations/07-bregan-daerthe.md:189`: "Krebbyg's role" note — see D1.
- `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:134` labels Fel'rekt "the captain's logistics lieutenant" (see D1).
- `campaign/structure/arc-e-faction-outposts.md:446` lists "Krebbyg Masq'il'yr" as a Notable Figure "to profile" (a pending-conversion structure doc, so not stale in the sense of a conflict).
- The Alexandrian Appendix B line 792 spells the ship "Hellbreaker" (`sources/Appendix_B_-_Player_Factions.md:792`); the campaign spells it "Heartbreaker". Not Krebbyg's line.

**E2. Routed quest references (the quest-time facts about Krebbyg)**

The cover and its exposure (routed to **Kreb Drops the Cover**):
- `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:1`-`:19` (the event's header and the cover's exposure; line 15: "What drops is Krebbyg's own cover.")
- `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:17` ("The cover costs him half an hour before every matinee and forces him to hold the act through every conversation with a member.")
- `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:24` (see A4)
- `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:275` ("Krebbyg is the same person the members met in **Coin Pouches** or in the Seven Masks lobby, with the greasepaint off whenever the door is locked.")
- `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:289` ("**Kreb Unmasked** — mark for each member who hears Krebbyg's arrangements in the booking office.")
- `campaign/setting/villains/jarlaxle.md:17` ("...or by exposing a Bregan D'aerthe drow in **Kreb Drops the Cover**.")

The member contact and the messages (quest time, routed to **Kreb Drops the Cover**, **Coin Pouches**, **The Wazoo Affair** and the rank events):
- `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:19` ("From this Event on, Krebbyg is the members' day-to-day contact at the theater for drops, messages and word of rank events.")
- `campaign/quests/faction-events/bregan-daerthe/r03-soldier/ev-01-soldier.md:137` ("The first part tells the member how alarmed Xanathar's Guild is about their party. Krebbyg writes it in these words:")
- `campaign/quests/faction-events/bregan-daerthe/r03-soldier/ev-01-soldier.md:151` ("A member who asks Krebbyg for any of those is told \"our friend doesn't draw maps, darling\", and nothing is spent.")

The Gralhund Villa and the Trades Ward (routed to **Gralhund Villa** and **Faction Outposts**):
- `campaign/guides/factions/08-bregan-daerthe.md:30` ("Word comes through Krebbyg: \"We saw what happened at Gralhund. We know who left with what. If the party is interested in what we saw, the theater has a back room.\"")
- `campaign/guides/factions/08-bregan-daerthe.md:29` (the **Fireball!** invitation: "Krebbyg, watching the post-fireball investigation, sends a theater invitation to any drow party members")
- `campaign/guides/factions/08-bregan-daerthe.md:31` ("At Renown 3+, Krebbyg has briefed the door staff: party members walk in without questions.")
- `campaign/guides/factions/08-bregan-daerthe.md:107` (the **Faction Outposts** Area P6 letter from "K" to "J": "Krebbyg warns Jarlaxle that strange eyes have been watching Fenerus's house and black snakes have been spotted over the Trades Ward...")
- `campaign/guides/factions/08-bregan-daerthe.md:122` ("| Lockdown | Fel'rekt, Krebbyg, and Soluun deployed together. Jarlaxle intervenes personally, always with an offer rather than a fight. |")
- `campaign/structure/arc-e-faction-outposts.md:303` ("a captured BD response team member's *Sealed Letter from Krebbyg*, naming Fenerus as a message recipient.")
- `campaign/structure/arc-e-faction-outposts.md:313` (see D2)
- `campaign/structure/arc-e-faction-outposts.md:333` ("*Step 4 — The Operation.* ... Stage Manager's Office (P6): *A Letter from K to J* — Krebbyg writing to Jarlaxle...")
- `campaign/structure/arc-d-gralhund-villa.md:344` ("- **Bregan D'aerthe (conditional on Arc C ev-04: Jarlaxle Informed):** Word reaches the party through whatever channel Krebbyg established during Arc C...")
- `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:142` (the Stone's carrier list; Krebbyg not named)
- Alexandrian PDF 17 (transcription, printed p.122): "Sealed Letter to Fenerus Stormcastle (Response Team: Krebbyg Masq'il'yr)" — `sources/17. Outpost and Lair Revelation Lists.pdf` PDF p.2.

The Sea Maidens Faire (routed to **Sea Maidens Faire**):
- `campaign/structure/arc-h-sea-maidens-faire.md:174` (U6, see D8)
- `campaign/structure/arc-h-sea-maidens-faire.md:275` ("**Jarlaxle Hostile**... If the party killed Soluun, Fel'rekt, or Krebbyg...")
- `campaign/guides/factions/08-bregan-daerthe.md:71` ("The Dive... Xanathar's Guild divers have located the Scarlet Marpenoth submarine...") — Krebbyg not named in the row; the event is in `campaign/quests/faction-events/bregan-daerthe/m06-the-dive/ev-01-the-dive.md:7` ("Take the brief from Krebbyg Masq'il'yr and Fel'rekt...")
- `sources/adventure-wdh.json:14782` ("Replace no-name drow gunslingers with {@creature Fel'rekt Lafeen|WDH}, {@creature Krebbyg Masq'il'yr|WDH}, and {@creature Soluun Xibrindas|wdh} if they are alive and free.")
- `sources/adventure-wdh.json:25120` (the armory safe, known to the three lieutenants)

Faction events (the day-one page must not restate these):
- `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:26` ("The watchers are Jarlaxle's three lieutenants. Fel'rekt Lafeen and Krebbyg Masq'il'yr shadow the party from dusk until dawn...")
- `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:42` ("Fel'rekt and Krebbyg work the night in turns, so one of them is always at the mouth of Trollskull Alley or on a roof across from the manor.")
- `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:7` ("Take Krebbyg's brief and learn that a frightened Cassalanter steward is selling a floor plan of a windmill, and that the family has a watcher on him.")
- `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:30` ("Krebbyg says \"the captain\" or \"J.\"")
- `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/design-notes.md:24` ("...Krebbyg carries the mission alone.")
- `campaign/quests/faction-events/bregan-daerthe/m03-three-nights/ev-01-three-nights.md:118` ("Kreb tells the member what the people behind the card are doing, and his answer depends on what the member learned about him in **The Wazoo Affair**.")
- `campaign/quests/faction-events/bregan-daerthe/m03-three-nights/ev-01-three-nights.md:397` ("The Event concludes when the bands take Ott, or when the Guild gets him first... and Krebbyg does not come for Ott.")
- `campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/ev-02-twelve-minutes.md:387` ("**+1 Renown:** return the captain's *bag of holding* to Arannis or Krebbyg, and keep the *Report on the Seven Masks Theater* out of the Guild's reach.")
- `campaign/quests/faction-events/bregan-daerthe/m06-the-dive/ev-02-before-dawn.md:265` ("Krebbyg and Fel'rekt wait on the pier and hold the line.")
- `campaign/quests/faction-events/bregan-daerthe/m06-the-dive/ev-01-the-dive.md:43` ("**Surface line:** A rope tied to the pier's outermost pile and held by Krebbyg.")
- `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/design-notes.md:13` ("Constable Pimm tests discretion... nobody in the company planned his visit, which suits Krebbyg, who never plans.")

Trollskull guide (not day-one):
- `campaign/guides/trollskull-manor/06-tavern-time.md:29` ("| Tarsakh 11–20 | Jarlaxle Baenre (in disguise), Mattrim \"Threestrings\" Mereg, Rishaal the Page-Turner | 19: a courier arrives with an urgent message for a patron who just left | The patron who just left was Jarlaxle. The message, from Krebbyg, reads \"The tide turns on the twentieth.\" It's the party's last clear warning before the Faire sails. |")

Gazetteer, Dock Ward (the Fireball! hook and the stall):
- `campaign/gazetteer/waterdeep/dock-ward.md:71` ("Hook: after **Fireball!**, two theater tickets on Faire stationery reach the party.") — this line is the theater hook.

Wiki (quest time, not day-one):
- wiki line 70: "In [[1492 DR]],{{WDH-time}} if Jarlaxle managed to obtain the ''[[Stone of Golorr]]'', then Fel'rekt and Krebbyg confronted some adventurers first in [[Mistshore]], where they had the support of the [[Lantanese]] mechanical [[dragon turtle]] [[Big Belchy]]..." (see the Fel'rekt notes E2 for the full text).

---

## F. Gaps a Background needs that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

**F1. Birth year, birth name, home, house name, parents, family, age.** No source gives any of these. The only age term is "He is young and rash." (`sources/adventure-wdh.json:32021`). The house is not named. Do not name a new Notable Figure (brief ruling 17). A nameless relative or place is allowed.

**F2. The destroyed house and how it fell.** Only "Krebbyg's house was destroyed long ago" (`sources/adventure-wdh.json:32021`) and "After the destruction of his house" (wiki line 68). Constraint: the company's founding rule that its members are "the rogue males of destroyed and disgraced houses" (`campaign/setting/villains/jarlaxle.md:46`) and the Underdark setting of the company (`campaign/setting/history/03-bregan-daerthes-long-road.md:41`) both apply. Nar'l and Soluun Xibrindas had a house "wiped out long ago" (`campaign/setting/history/03-bregan-daerthes-long-road.md:43`); the drafter must not give Krebbyg the same house without `[design]` and a reason, because no source links the two.

**F3. How he joined and when.** Only "he joined Bregan D'aerthe" after the house fell (wiki line 68) and "Jarlaxle never regrets taking him in" (`campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:15`). No date.

**F4. How he came to run the theater, and when.** No source. The Dock Ward block gives the cover: "a booking manager who calls himself Kreb Sorrush handles casting inquiries and schedules" (`campaign/gazetteer/waterdeep/dock-ward.md:70`). The Persona says "The theater is the closest thing he has to a home outside Bregan D'aerthe" (L21). Any origin in theater work is `[design]`. The voice profile is the only source for his theatre skill ("Theatre jargon (bookings, blocking, the house, the ghost)", line 85).

**F5. Where the Luskan accent comes from.** Only the org page: "a slight Luskan accent that he makes no effort to conceal" (`campaign/setting/organizations/07-bregan-daerthe.md:59`). Constraint: the company's Luskan base is in `campaign/setting/history/03-bregan-daerthes-long-road.md:60` ("After 1485 DR the High Captains trade legally across the Sword Coast and are secretly under the sway of Jarlaxle and the company."). The drafter may tie the accent to Luskan only as `[design]`.

**F6. Relationship with Malkolm Brizzenbright's ghost.** Only the Motivations line (L15) and the gazetteer ("He is not hostile", `campaign/gazetteer/waterdeep/dock-ward.md:76`). Constraint: the ghost is "the theater's founder" and "not hostile" (`campaign/gazetteer/waterdeep/dock-ward.md:76`); the Malkolm voice profile is hostile in tone ("Proprietary outrage and anxiety", `.claude/skills/character-voices/voices/bregan-daerthe.md:141`), which is a voice, not a relationship. The Malkolm page does not mention Krebbyg.

**F7. Personal goals beyond the company.** None in any source. The page's Motivations give his wants toward Fel'rekt, the theater and Jarlaxle (L15). Brief ruling 17: the goals may not reveal a secret, an Event Outcome, a quest result or the Grand Game balance. A goal about the theater, a craft or a person is allowed as `[design]`.

**F8. The "basement".** The voice profile has Krebbyg's sample line "You want in the basement? Ha, no. Ask Fel." (`.claude/skills/character-voices/voices/bregan-daerthe.md:93`) and Malkolm's "There is a machine in my basement, Lantanese, hideous, and a door I never built" (line 147). No file in `campaign/` gives the Seven Masks Theater a basement. The gazetteer's Seven Masks block lists the dressing room as the safe house (`campaign/gazetteer/waterdeep/dock-ward.md:75`) and no basement. The Alexandrian Dock Ward text puts the safe house in "One of the dressing rooms" (PDF p.2, printed p.37). The drafter must not write a basement as a fact.

**F9. Faith.** None. Constraint: the Lolth rule (`campaign/setting/history/03-bregan-daerthes-long-road.md:34`). Krebbyg's own speech about the goddess is not in any file read. Do not invent a shrine or an invocation.

**F10. Physical appearance.** Only the cover ("a brown wig, pale greasepaint and gloves he never takes off", `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:15`), which is quest-time and is the disguise. The drow appearance is not described in any source.

**F11. Where he goes off duty, and what he does for fun outside the theatre.** None. The sources say he "gets bored with anything routine" (voice line 87) and that his "pleasure in the theatre is real" (line 87).

---

## G. Source facts that hint at the figure's inner life (for the backstory; do not contradict)

- "Krebbyg's house was destroyed long ago, leaving him with no connection to his old life in the Underdark." — `sources/adventure-wdh.json:32021`
- "The theater is the closest thing he has to a home outside Bregan D'aerthe." — `campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:21`
- "Krebbyg prefers to follow Fel'rekt's lead, letting him do most of the thinking and talking." — `sources/adventure-wdh.json:32022`
- "Krebbyg was young and rash. He preferred to follow Fel'rekt's leadership." — wiki line 73
- "His pleasure in the theatre is real." — `.claude/skills/character-voices/voices/bregan-daerthe.md:87`
- "He gets bored with anything routine, and it's obvious." — same line
- "He never lets anyone insult the theatre." — `.claude/skills/character-voices/voices/bregan-daerthe.md:90`
- "creative pleasure in his theater cover identity" — `campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:13`
- "nobody in the company planned his visit, which suits Krebbyg, who never plans." — `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/design-notes.md:13` (design note; shows the trait)
- "Krebbyg is the close friend and operational partner of Fel'rekt Lafeen" — `campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:25`
- "He is warm toward..." is Fel'rekt's line, not Krebbyg's. Not used here.
- "Kreb tried to sit in it once, and Pelsha moved him." — `sources/research/pass3-bundles/dock-ward/campaign-hits.txt:114` (the quote is from `campaign/quests/faction-events/bregan-daerthe/r50-houseless-noble/ev-01-houseless-noble.md:167`; the chair is Soluun's) — quest time; not for the backstory.
- "Krebbyg resided on the Scarlet Marpenoth ship where he sharpened his sword." — wiki line 65
- "sharpening his sword. His stateroom contains a net hammock and nothing else." — `sources/adventure-wdh.json:26451`

---

## Not found

- Birth year, birth name, home, house name, parents, family, age, date of joining, the date he took the theater post: searched `campaign/` (Grep for "Krebbyg|Kreb\b|Kreb Sorrush|Masq.il"), `sources/adventure-wdh.json` (Grep for "Krebbyg"), `sources/*.md`, `sources/research/`. No match gives any of these.
- Faith and any shrine or prayer: the same search. Only the Lolth rule (`campaign/setting/history/03-bregan-daerthes-long-road.md:34`).
- Seven Masks basement: Grep for "basement" across `campaign/` gives no Seven Masks entry (see F8).
- Malkolm's page and Krebbyg: no mention (Grep of `campaign/setting/notable-figures/bregan-daerthe/07-malkolm-brizzenbright.md`).
- Alexandrian PDFs for Krebbyg. Read: `sources/5. Faction Outposts.pdf` (pp.1-2), `sources/17. Outpost and Lair Revelation Lists.pdf` (p.2), `sources/9. Lair – Sea Maidens Faire.pdf` (pp.1-3), `sources/1. The Villains.pdf` (p.5). Not read: `sources/4. Gralhund Villa.pdf`, `sources/3. Player Character Factions.pdf`, `sources/26. Addendum Other Collaborators.pdf`, `sources/11. Lair Xanathar's Lair.pdf`. Those may hold more BD text and were not checked for his name.
- Wiki: no line on his birth, parentage, home, age or house name. The infobox fields `dob`, `age`, `parents` and `siblings` are blank (wiki lines 17-17, 21, 29-33). The home field is blank. Wiki line 11 is Fel'rekt's; Krebbyg's home line is at wiki line 11 as "| home           = [[Waterdeep]], [[Sword Coast North]]".

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. `sources/SOURCE_GUIDE.md:690` lists `Jarlaxle Baenre NPC Guide.docx` as the Jarlaxle persona source. Its lines are cited in `campaign/setting/history/03-bregan-daerthes-long-road.md:140`. Not checked for Krebbyg.
- The `campaign/quests/faction-events/bregan-daerthe/` event files were read through Grep (the full files are too large to read whole). Quotes are exact Grep output.
