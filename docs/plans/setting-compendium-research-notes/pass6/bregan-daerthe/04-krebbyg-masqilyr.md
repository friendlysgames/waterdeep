# Pass 6 research notes: Krebbyg Masq'il'yr

Page: `campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR. Krebbyg is a named lieutenant of Jarlaxle and runs the Seven Masks Theater under the human cover "Kreb Sorrush" on day one. The exposure of the cover, the members' missions and the Gralhund and Sea Maidens events are quest time. Cassalanter secrecy and the Lolth rule apply. Brief ruling 2 makes him a major NPC, so the full Personality and Connections apply.
Organization page: `campaign/setting/organizations/07-bregan-daerthe.md`
Voice profile: `.claude/skills/character-voices/voices/bregan-daerthe.md` ("### Krebbyg Masq'il'yr ("Kreb Sorrush")", lines 80-94)
Wiki extract: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-bregan-daerthe/04-krebbyg-masqilyr.txt` (quoted as "wiki line N", that file's lines; citation key `WDH5e`, *Waterdeep: Dragon Heist*, 5e)

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes are shown as plain quotes. `{@creature ...}` tags are left as written. The `page` field of an entry is given where one exists.
- Where a source sentence runs on past the quoted part, the quote ends at a sentence boundary and the rest of the passage is named in brackets. No quote is cut mid-sentence.
- Alexandrian PDFs: no shell, so `pdftotext` could not run. Three PDFs were read as rendered page images and their quotes are transcriptions. Check exact wording with `pdftotext -layout` before any quote goes into prose:
  - `sources/5. Faction Outposts.pdf` (printed pp.36-37 = PDF pp.1-2). Read: PDF pp.1-2.
  - `sources/17. Outpost and Lair Revelation Lists.pdf` (printed p.122 = PDF p.2). Read: PDF p.2.
  - `sources/9. Lair – Sea Maidens Faire.pdf` (printed pp.68-70 = PDF pp.1-3). Read: PDF pp.1-3.
- Alexandrian text files read: `sources/Appendix_B_-_Player_Factions.md`, `sources/Appendix_D_-_Running_the_Tavern.md`, `sources/Act_III_Arc_D.md`, `sources/Act_III_Arc_E.md`.
- The Grep tool cannot search the PDFs. The PDFs not read were not checked for his name (see Not found).
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **"Logistics lieutenant" is his label on the org page and his own page, and it is also Fel'rekt's label in two quest events.** The org page's Draft Notes flag it (`campaign/setting/organizations/07-bregan-daerthe.md:189`). His page's Relationships line uses it (L25). See D1.
2. **The message pickup is dated nowhere in the campaign, and the Alexandrian text ties it to the Faire's arrival.** The Relationships line (L25) gives the pickup as a day-one role. The PDF says "Since the Sea Maidens Faire arrived in Waterdeep, Fenerus has also been acting as a message drop for Bregan D'Aerthe" (PDF p.1, printed p.36, transcription). The campaign's fleet arrives on Ches 21 (`campaign/setting/villains/jarlaxle.md:52`), but the Scarlet Marpenoth "has been moored in the harbor all year" (`campaign/setting/history/03-bregan-daerthes-long-road.md:153`). The drafter should not date the pickup. See D3.
3. **The Overview is 34 words, over the 21-word limit** (L29). See C row 11.
4. **His pickup frequency: "every two days" in the campaign, "once every 1d3 days" in the Alexandrian PDF.** See D2.
5. **His human cover is public; its exposure is quest time.** The Persona says "To the world, Krebbyg operates as "Kreb Sorrush," the booking manager of the Seven Masks Theater" (L21). The cover's details and its exposure (the wig, the greasepaint, the members' Kreb Unmasked outcome) live in `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md`. See E2.
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
> — wiki line 62 (the lead sentence opens with the name and a pronunciation template, which is not quoted)

**Adventure, pronunciation key**
> "{@creature Krebbyg Masq'il'yr|WDH}"
> "KREH-big MASK-il-eer"
> — `sources/adventure-wdh.json:193`-`:194`

**Campaign, Persona (the page's own account)**
> "**Persona.** To the world, Krebbyg operates as \"Kreb Sorrush,\" the booking manager of the Seven Masks Theater. To those he trusts, he is young, rash, and happy to let Fel'rekt do the thinking and talking. Deep down, his house was destroyed long ago, leaving him with no connection to his old life in the Underdark. The theater is the closest thing he has to a home outside Bregan D'aerthe."
> — `campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:21`

**Campaign, the organization page (the accent line)**
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

**Campaign, the Dock Ward block (the hook; quest-name references)**
> "- Hook: he sends the theater invitation after **Fireball!**, and he is the contact for many Bregan D'aerthe missions, including **The Theater's Back Room** and **Kreb Drops the Cover**."
> — `campaign/gazetteer/waterdeep/dock-ward.md:145` (quest-time hook; see E2)

**Campaign, the organization page label**
> "- **Krebbyg Masq'il'yr** — Drow gunslinger, chaotic neutral, and logistics lieutenant. Operates as \"Kreb Sorrush\" at the Seven Masks Theater. Collects messages from Fenerus Stormcastle's house every two days and carries them to the *Scarlet Marpenoth*. See the **Krebbyg Masq'il'yr** page in Notable Figures."
> — `campaign/setting/organizations/07-bregan-daerthe.md:102` (Key Members)

**Campaign, the Dock Ward GM notes (the theater as a Bregan D'aerthe front)**
> "- The theater is a Bregan D'aerthe front. Rongquan Mystere is a disguise of Jarlaxle's, and Kreb Sorrush is Krebbyg. One dressing room is kept empty as a safe house, with two drow guards inside whenever it is in use."
> — `campaign/gazetteer/waterdeep/dock-ward.md:75`

**Campaign, the Factions Guide, the message pickup**
> "Fenerus collects messages from dead drops throughout the Trades Ward and stores them at the house; Krebbyg picks them up every two days."
> — `campaign/guides/factions/08-bregan-daerthe.md:85` (Fenerus Stormcastle; the passage begins "Use the description from DH p. 63.")

**Campaign, the Dock Ward GM notes (the errand)**
> "- Krebbyg works for Bregan D'aerthe and reports to Jarlaxle. His errand outside the ward is the message pickup at Fenerus Stormcastle's house in the Trades Ward."
> — `campaign/gazetteer/waterdeep/dock-ward.md:149`

**Wiki, the lieutenants' tasks (wiki line 65; WDH5e-p15)**
> "Krebbyg, together with [[Soluun Xibrindas]] and [[Fel'rekt Lafeen]], was tasked by [[Jarlaxle]] with doing dirty deeds in the city."

**Adventure, the lieutenants' watch (quest-time use in the adventure; the passage concerns new recruits)**
> "{@creature Fel'rekt Lafeen|WDH} and {@creature Krebbyg Masq'il'yr|WDH} watch the characters at night, and {@creature Soluun Xibrindas|wdh} watches them during the day (doing his best to stay out of the sunlight)."
> — `sources/adventure-wdh.json:3592` (chapter not checked)

### A3. Former life and the Underdark

The only source fact is the destroyed house (A1). The wiki says "no more connections in the underdark" (wiki line 68). The page's Persona says "no connection to his old life in the Underdark" (L21), which repeats the adventure's wording at `sources/adventure-wdh.json:32021`. No house name, city or rank is given.

### A4. Faith

Krebbyg's own faith is not stated in any source.

**Campaign, the Lolth rule (history, GM-facing)**
> "- This is where the campaign rule starts. Jarlaxle rejected Lolth, Bregan D'aerthe rejects her, and its members speak of her as the goddess they walked away from. Soluun gives Jarlaxle the devotion that a drow of the houses would give the Spider Queen."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:34`

**Campaign, the Lolth page (the events where the rule applies)**
> ">   - **Houseless Noble, The Dockside Killer, Kreb Drops the Cover, The Killer's Fate, The Compromised Eye:** Each repeats the rule or applies it to a speech. The lines are in the GM Notes."
> — `campaign/setting/deities/lolth.md:77`

**Campaign, the Kreb Drops the Cover event (quest time; the rule is sourced)**
> "Krebbyg and Fel'rekt both say \"the captain\" and never Jarlaxle's name."
> — `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:24` (the passage continues with Nevercott's disguise)

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

**Voice profile, the theatre skill**
> "- **Word choice:** Theatre jargon (bookings, blocking, the house, the ghost), laid over gang talk. As Kreb Sorrush he calls everyone \"darling\"."
> — `.claude/skills/character-voices/voices/bregan-daerthe.md:85`

### A6. Relationships (named figures)

**Fel'rekt (closest friend and partner)**
> "Krebbyg works closely with {@creature Fel'rekt Lafeen|WDH}, and the two collaborate well despite their disparate alignments. Krebbyg prefers to follow Fel'rekt's lead, letting him do most of the thinking and talking."
> — `sources/adventure-wdh.json:32022`
> "Fel'rekt and Krebbyg were a working team." — wiki line 76 (Relationship)
> "Krebbyg is the close friend and operational partner of Fel'rekt Lafeen, Jarlaxle's logistics lieutenant (collecting messages from Fenerus Stormcastle for the Scarlet Marpenoth), and the operating cover manager of the Seven Masks Theater." — the page's own line, `campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:25` (C row 10)

**Soluun (the sibling lieutenant; the three know his nights)**
> "He conceals his nighttime escapades as well as he can, but Jarlaxle, Fel'rekt, and Krebbyg know what he's up to."
> — `sources/adventure-wdh.json:32041` (Soluun Xibrindas entry, page 202)

**Malkolm Brizzenbright (the ghost of the theater's founder)**
> "The ghost is Malkolm Brizzenbright, the theater's founder. He is not hostile, and he will tell a respectful visitor that \"Rongquan\" is a false identity and that drow come and go at irregular hours."
> — `campaign/gazetteer/waterdeep/dock-ward.md:76`
> The page's own line: "run the Seven Masks Theater without Malkolm Brizzenbright's ghost interfering" (`campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:15`). The Malkolm page (`campaign/setting/notable-figures/bregan-daerthe/07-malkolm-brizzenbright.md`) does not mention Krebbyg (Grep, no match).

**Jarlaxle (the employer; the theater's owner is his disguise)**
> "Playbills name the owner as Rongquan Mystere, and a booking manager who calls himself Kreb Sorrush handles casting inquiries and schedules."
> — `campaign/gazetteer/waterdeep/dock-ward.md:70`

**Fenerus Stormcastle (the message drop he collects from)**
> "Fenerus collects messages from dead drops throughout the Trades Ward and stores them at the house; Krebbyg picks them up every two days." — `campaign/guides/factions/08-bregan-daerthe.md:85`
> "Fenerus Stormcastle's house on Quill Alley is a Bregan D'aerthe message drop." — `campaign/gazetteer/waterdeep/trades-ward.md:37`

### A7. Rank, post and the theater

- "logistics lieutenant" (`campaign/setting/organizations/07-bregan-daerthe.md:102`; see D1).
- "operating cover manager of the Seven Masks Theater" (`campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:25`).
- "he is the contact for many Bregan D'aerthe missions" (`campaign/gazetteer/waterdeep/dock-ward.md:145`).
- "The theater is a Bregan D'aerthe front" (`campaign/gazetteer/waterdeep/dock-ward.md:75`).
- Alexandrian Dock Ward text (transcription, PDF p.2, printed p.37, `sources/5. Faction Outposts.pdf`): "One of the dressing rooms is kept empty as a safe house for D'Aerthe agents in trouble."
- Time in post: "during the early 1490s [[DR]]" (wiki line 62). No date for when he took the booking post.

### A8. Habits and temperament (day-one sources)

**Wiki (wiki line 65; WDH5e-p34)**
> "Krebbyg and Fel'rekt preferred to act during the night."

**Wiki (wiki line 73; WDH5e-p202)**
> "Krebbyg was young and rash. He preferred to follow Fel'rekt's leadership."

**Adventure (see A6, `sources/adventure-wdh.json:32022`)**: "Krebbyg prefers to follow Fel'rekt's lead, letting him do most of the thinking and talking."

**Voice profile, day-one habits (`.claude/skills/character-voices/voices/bregan-daerthe.md`, lines 87 and 90)**
> "- **Personality in speech:** Reckless confidence and deference. He defers to Fel'rekt immediately on anything serious (\"Ask Fel.\"). He gets bored with anything routine, and it's obvious. His pleasure in the theatre is real."
> "- **Never:** He never plans, never argues with Fel'rekt, and never lets anyone insult the theatre."

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, the page: "*Drow gunslinger, chaotic neutral, he/him*. Stat block: **Drow Gunslinger**." — `campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:5`
- Campaign, the org page: "- **Krebbyg Masq'il'yr** — Drow gunslinger, chaotic neutral, and logistics lieutenant." — `campaign/setting/organizations/07-bregan-daerthe.md:102`
- Campaign, the Dock Ward block: "**Krebbyg Masq'il'yr (Chaotic Neutral, Drow, he/him)**" — `campaign/gazetteer/waterdeep/dock-ward.md:143`
- Campaign, the quest tag: "Krebbyg Masq'il'yr (Chaotic Neutral, Drow, he/him) :: a young drow gunslinger who has run the Seven Masks' bookings as the human Kreb Sorrush, and who is more relieved than anyone that the greasepaint is off." — `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:85`
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
| 3 | L7 | "- **Featured in:** **Faction Outposts**, **Sea Maidens Faire**, **The Handkerchief and the Girl**, **The Wazoo Affair**, **The Betrayal Pitch**, **Three Nights**, **The Compromised Eye**, **The Theater's Back Room**, **The Dive**" | Quest-name list (not narrative). It omits **Bregan D'aerthe First Meeting**, **Kreb Drops the Cover** and **Coin Pouches**, which feature him (E2) | `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:7` |
| 4 | L11 | "**Resonance.** Krebbyg should inspire amusement with his rash energy, endearment with his deference to Fel'rekt, and curiosity about what an Underdark exile makes of a career managing a Waterdeep theater." | Day-one. Keep (ruling 3) | `sources/adventure-wdh.json:32021`; `:32022` |
| 5 | L13 | "**Emotions.** Krebbyg most often feels reckless confidence, cheerful deference to Fel'rekt's judgment, restless boredom with routine, creative pleasure in his theater cover identity, mischievous humor, and an eagerness that substitutes for planning." | Day-one. Keep | voice profile lines 87 and 90 |
| 6 | L15 | "**Motivations.** Krebbyg wants to follow Fel'rekt into whatever comes next, run the Seven Masks Theater without Malkolm Brizzenbright's ghost interfering, and prove useful enough that Jarlaxle never regrets taking him in." | Day-one. Keep. "taking him in" is the company's recruitment, which the wiki dates to after the house fell (wiki line 68) | A2; `campaign/gazetteer/waterdeep/dock-ward.md:76` |
| 7 | L17 | "**Inspirations.** When playing Krebbyg, channel Rocket Raccoon (*Guardians of the Galaxy*), Jesse Pinkman (*Breaking Bad*), and Mushu (*Mulan*)." | Not a fact. Keep | n/a |
| 8 | L21 | "**Persona.** To the world, Krebbyg operates as \"Kreb Sorrush,\" the booking manager of the Seven Masks Theater. To those he trusts, he is young, rash, and happy to let Fel'rekt do the thinking and talking. Deep down, his house was destroyed long ago, leaving him with no connection to his old life in the Underdark. The theater is the closest thing he has to a home outside Bregan D'aerthe." | Day-one. The "To the world" cover is public (the Dock Ward block says the same). Its exposure to members is quest time (E2) | `sources/adventure-wdh.json:32021`; `campaign/gazetteer/waterdeep/dock-ward.md:70` |
| 9 | L23 | "**Morale.** In a fight, Krebbyg follows Fel'rekt's lead, trading banter and covering flanks. He acts before thinking and relies on Fel'rekt to tell him when to stop." | Encounter behaviour, not a quest event. Brief ruling 3 keeps Morale verbatim; the drafter should know it is encounter-register | `sources/adventure-wdh.json:32022` |
| 10 | L25 | "**Relationships.** Krebbyg is the close friend and operational partner of Fel'rekt Lafeen, Jarlaxle's logistics lieutenant (collecting messages from Fenerus Stormcastle for the Scarlet Marpenoth), and the operating cover manager of the Seven Masks Theater." | The friendship and the cover-manager role are day-one. "logistics lieutenant" is the disputed label (D1). "collecting messages from Fenerus Stormcastle" is a day-one role in the org page (`:102`), but its start date is not sourced (D3) | `campaign/setting/organizations/07-bregan-daerthe.md:102`; `campaign/guides/factions/08-bregan-daerthe.md:85` |
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
- Line 93, sample *Business*: "You want in the basement? Ha, no. Ask Fel. Also the ghost hates you already, don't take it personally." — **Flag.** "the basement" has no source for the Seven Masks Theater (see F8). The business register is the drafter's call.
- Line 94, sample *Under pressure*: "Fel! Fel, it's happening! What do we do?" — **encounter time**. Flag.

Malkolm's voice profile (line 147) has a second "basement" reference: "There is a machine in my basement, Lantanese, hideous, and a door I never built, and a man whose handwriting is no more Tethyrian than I am alive." (`.claude/skills/character-voices/voices/bregan-daerthe.md:147`). Flag for the Malkolm page.

---

## D. Conflicts

**D1. "Logistics lieutenant" versus "BD lieutenant"**
- Org page, Krebbyg: "- **Krebbyg Masq'il'yr** — Drow gunslinger, chaotic neutral, and logistics lieutenant." — `campaign/setting/organizations/07-bregan-daerthe.md:102`
- Org page, Fel'rekt: "- **Fel'rekt Lafeen** — Drow gunslinger, neutral good, and BD lieutenant." — `campaign/setting/organizations/07-bregan-daerthe.md:101`
- Quest event, Fel'rekt (s02): "Fel'rekt Lafeen (Neutral Good, Drow, he/him) :: a bright young drow gunslinger and the captain's logistics lieutenant, who would rather disarm anyone than hurt them and is never far from Krebbyg." — `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:134`
- Quest event, Fel'rekt (m06): "Fel'rekt Lafeen (Neutral Good, Drow, he/him) :: a bright young drow gunslinger and the captain's logistics lieutenant, who counts his options off on his fingers and would rather disarm anyone than hurt them." — `campaign/quests/faction-events/bregan-daerthe/m06-the-dive/ev-01-the-dive.md:63`
- The org page's own Draft Notes: "**Conflicts:** Krebbyg's role. This page's Key Members line, kept verbatim, calls him \"logistics lieutenant\". `m06-the-dive/ev-01-the-dive.md:63` and `s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:134` call Fel'rekt \"the captain's logistics lieutenant\", and `04-krebbyg-masqilyr.md:25` is ambiguous about which of the two it means. The page says \"BD lieutenant\" for Fel'rekt, as before." — `campaign/setting/organizations/07-bregan-daerthe.md:189`
- Not decided in the sources.

**D2. Pickup frequency**
- Campaign, the org page: "Collects messages from Fenerus Stormcastle's house every two days and carries them to the *Scarlet Marpenoth*." — `campaign/setting/organizations/07-bregan-daerthe.md:102`
- Campaign, the Factions Guide: "Krebbyg picks them up every two days." — `campaign/guides/factions/08-bregan-daerthe.md:85`
- Campaign, the Trades Ward gazetteer: "Fenerus gathers messages from dead drops across the ward and stores them at the house, and Krebbyg Masq'il'yr collects them every two days." — `campaign/gazetteer/waterdeep/trades-ward.md:39`
- Campaign, the Faction Outposts structure doc: "Staking out the house and following Krebbyg Masq'il'yr (he visits every two days to drop or collect messages) leads directly to the Faire." — `campaign/structure/arc-e-faction-outposts.md:313`
- Alexandrian PDF (transcription): "Following Krebbyg: Krebbyg comes to collect messages from Fenerus once every 1d3 days." — `sources/5. Faction Outposts.pdf` PDF p.2 (printed p.37).
- Higher rank: campaign ("every two days"). The Alexandrian "every 1d3 days" is the older source.

**D3. When the message drop began**
- Alexandrian PDF (transcription): "Since the Sea Maidens Faire arrived in Waterdeep, Fenerus has also been acting as a message drop for Bregan D'Aerthe." — `sources/5. Faction Outposts.pdf` PDF p.1 (printed p.36).
- Campaign, the fleet's arrival: "The fleet reaches Deepwater Harbor on Ches 21, the opening day of Fleetswake, and leaves at dawn on Tarsakh 20" — `campaign/setting/villains/jarlaxle.md:52`
- Campaign, the Scarlet Marpenoth: "In the campaign it has been moored in Deepwater Harbor since he reached the city, and the carnival fleet joins it for Fleetswake." — `campaign/setting/history/03-bregan-daerthes-long-road.md:69`
- Campaign, the message role itself: undated. No source gives a start date for the pickup.
- Higher rank: none. The drafter should not date the pickup. The page's L25 gives it as a current role.

**D4. Whether Fenerus knows the drow are Bregan D'aerthe**
- Trades Ward gazetteer: "Fenerus spies for Luskan. He followed Krebbyg once and knows where the messages go, but he has not worked out that the cloaked drow belong to Bregan D'aerthe." — `campaign/gazetteer/waterdeep/trades-ward.md:38`; also `:40`: "Fenerus believes his contacts are Luskan agents. He followed Krebbyg once and knows where the messages go, but he has not worked out that the cloaked drow belong to Bregan D'aerthe."
- Org page: "Supposed to be a cut-out, but once followed Krebbyg after a pickup and knows the messages go to the Sea Maidens Faire." — `campaign/setting/organizations/07-bregan-daerthe.md:104`
- Alexandrian PDF (transcription): "Questioning Fenerus: Although he's supposed to be a cut-out, Fenerus once followed Krebbyg after Jarlaxle's lieutenant picked up the messages and knows that they're being taken to the Sea Maidens Faire." — `sources/5. Faction Outposts.pdf` PDF p.1 (printed p.36).
- The Session 51 ruling at `campaign/setting/governance-and-guilds/guilds.md:122` settles Fenerus's knowledge in favour of the org page. That ruling cites the org page as line 103; the line is 104.
- Higher rank: the org page (the Session 51 ruling). The Trades Ward gazetteer is stale on what Fenerus has worked out.

**D5. His human cover: public record**
- Campaign, the Persona: "To the world, Krebbyg operates as \"Kreb Sorrush,\" the booking manager of the Seven Masks Theater." (`campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:21`)
- Campaign, the Dock Ward block: "Playbills name the owner as Rongquan Mystere, and a booking manager who calls himself Kreb Sorrush handles casting inquiries and schedules." (`campaign/gazetteer/waterdeep/dock-ward.md:70`)
- The campaign does not say the public knows Kreb Sorrush is a drow. The Dock Ward GM notes say "Kreb Sorrush is Krebbyg" (`campaign/gazetteer/waterdeep/dock-ward.md:75`). The Kreb Drops the Cover event describes the cover: "Kreb Sorrush is a drow lieutenant who passes as a human stage manager with a brown wig, pale greasepaint and gloves he never takes off." (`campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:15`; quest time).
- Not a conflict. The drafter should say "human cover" and not state that the public knows he is a drow.

**D6. Luskan accent**
- Org page: "a slight Luskan accent that he makes no effort to conceal" (`campaign/setting/organizations/07-bregan-daerthe.md:59`).
- Adventure: no accent given (`sources/adventure-wdh.json:32017`-`:32033`).
- Voice profile: no accent given (`.claude/skills/character-voices/voices/bregan-daerthe.md:83`-`:90`).
- Not a conflict. Only the org page gives an accent.

**D7. Stateroom**
- Adventure: "U6. Krebbyg's Stateroom" (`sources/adventure-wdh.json:26447`); "His stateroom contains a net hammock and nothing else." (`:26451`)
- Campaign, the structure doc: "**U6 (Krebbyg's Stateroom).** Krebbyg Masq'il'yr is present unless ashore with Fel'rekt (they move together). Reckless, follows Fel'rekt's lead. If Fel'rekt has been neutralized or agreed to stand down, Krebbyg follows suit. If Fel'rekt is in danger, Krebbyg fights without thinking." — `campaign/structure/arc-h-sea-maidens-faire.md:174`
- Campaign, the Scarlet Marpenoth area overview: "three drow gunslingers (U3, U4, U5)" (`campaign/locations/sea-maidens-faire/area-overview.md:34`) omits U6. See the Fel'rekt notes, D8.

---

## E. Stale lines in other files (do not edit) and routed quest references

**E1. Stale or conflicting lines in other files**
- `campaign/gazetteer/waterdeep/trades-ward.md:38` and `:40`: see D4.
- `campaign/gazetteer/waterdeep/dock-ward.md:320`: "- **Names with no page:** Xoblob, Gorra, Ilsa Dalloway, Harl Pimm, Captain Staget, Heldar, Rongquan Mystere and Kreb Sorrush (aliases of Jarlaxle and Krebbyg), Wenna Tarrow, Nella Fen, Ostrin Brindle, Tarn Hobble, Piers Hobb, Mirsa, Garrit Moll, Tobiah Ashby, Sarna, the Peabody family and Nar'l Xibrindas appear as plain text." Stale for Krebbyg: he has a Notable Figures page (`campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md`).
- `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:134` labels Fel'rekt "the captain's logistics lieutenant" (see D1).
- `campaign/structure/arc-e-faction-outposts.md:446` lists "Krebbyg Masq'il'yr" among the Notable Figures to profile (a pending-conversion structure doc).
- `sources/Appendix_B_-_Player_Factions.md:792` spells the ship "Hellbreaker"; the campaign files spell it "Heartbreaker" (`campaign/guides/factions/08-bregan-daerthe.md:56`). Not Krebbyg's line.

**E2. Routed quest references (the quest-time facts about Krebbyg)**

The cover and its exposure (routed to **Kreb Drops the Cover**):
- `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:15`: "What drops is Krebbyg's own cover. Kreb Sorrush is a drow lieutenant who passes as a human stage manager with a brown wig, pale greasepaint and gloves he never takes off." (the passage continues: "It is an ordinary theater trade secret, and it fools almost everybody in the Dock Ward.")
- `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:17`: "The cover costs him half an hour before every matinee and forces him to hold the act through every conversation with a member." (rest of the passage covers Fel'rekt's argument about the mask)
- `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:19`: "From this Event on, Krebbyg is the members' day-to-day contact at the theater for drops, messages and word of rank events."
- `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:275`: "Krebbyg is the same person the members met in **Coin Pouches** or in the Seven Masks lobby, with the greasepaint off whenever the door is locked." (rest of the passage covers the member's arrangements)
- `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:289`: "- **Kreb Unmasked** — mark for each member who hears Krebbyg's arrangements in the booking office." (the outcome's readers follow)
- `campaign/setting/villains/jarlaxle.md:17`: "A character is marked by giving Sergeant Marek Dunmere their name in the **Bregan D'aerthe First Meeting**, by attacking Nevercott, or by exposing a Bregan D'aerthe drow in **Kreb Drops the Cover**."

The member contact and the messages (routed to **Kreb Drops the Cover**, **Coin Pouches**, **The Wazoo Affair** and the rank events):
- `campaign/quests/faction-events/bregan-daerthe/r03-soldier/ev-01-soldier.md:137`: "The first part tells the member how alarmed Xanathar's Guild is about their party. Krebbyg writes it in these words:"
- `campaign/quests/faction-events/bregan-daerthe/r03-soldier/ev-01-soldier.md:151`: "A member who asks Krebbyg for any of those is told \"our friend doesn't draw maps, darling\", and nothing is spent."
- `campaign/quests/faction-events/bregan-daerthe/m03-three-nights/ev-01-three-nights.md:118`: "Kreb tells the member what the people behind the card are doing, and his answer depends on what the member learned about him in **The Wazoo Affair**."
- `campaign/quests/faction-events/bregan-daerthe/m03-three-nights/ev-01-three-nights.md:397`: "The Event concludes when the bands take Ott, or when the Guild gets him first. The second black pouch arrives that afternoon in **Coin Pouches**, and Krebbyg does not come for Ott."

The Gralhund Villa and the Trades Ward (routed to **Gralhund Villa**, **Faction Outposts**, **Fireball!**):
- `campaign/guides/factions/08-bregan-daerthe.md:29`: "Krebbyg, watching the post-fireball investigation, sends a theater invitation to any drow party members" (rest of the row: "— or, if none are present, to "the group investigating the explosion on Trollskull." The note is on Faire stationery and includes two tickets to a Seven Masks Theater performance. It is not a mission. It is reconnaissance.")
- `campaign/guides/factions/08-bregan-daerthe.md:30`: "Word comes through Krebbyg: \"We saw what happened at Gralhund. We know who left with what. If the party is interested in what we saw, the theater has a back room.\"" (rest of the row: the price of the meeting)
- `campaign/guides/factions/08-bregan-daerthe.md:31`: "At Renown 3+, Krebbyg has briefed the door staff: party members walk in without questions."
- `campaign/guides/factions/08-bregan-daerthe.md:107`: "Krebbyg warns Jarlaxle that strange eyes have been watching Fenerus's house and black snakes have been spotted over the Trades Ward; he recommends caution and possibly finding a replacement asset." (the Area P6 letter from "K" to "J")
- `campaign/guides/factions/08-bregan-daerthe.md:122`: "| Lockdown | Fel'rekt, Krebbyg, and Soluun deployed together. Jarlaxle intervenes personally, always with an offer rather than a fight. |"
- `campaign/structure/arc-e-faction-outposts.md:303`: "...a captured BD response team member's *Sealed Letter from Krebbyg*, naming Fenerus as a message recipient." (the approach paragraph's first two options are the Seven Masks archive and the Directive to Zorbog)
- `campaign/structure/arc-e-faction-outposts.md:333`: "*Step 4 — The Operation.* Primary objective: the BD safehouse dressing room and its stored intelligence. Stage Manager's Office (P6): *A Letter from K to J* — Krebbyg writing to Jarlaxle — warning that Fenerus's address has become known to a third party and recommending a new message drop."
- `campaign/structure/arc-d-gralhund-villa.md:344`: "- **Bregan D'aerthe (conditional on Arc C ev-04: Jarlaxle Informed):** Word reaches the party through whatever channel Krebbyg established during Arc C: *\"We saw what happened at Gralhund. We know which factions were there. We know who left with what. If the party is interested in a full account — faction by faction — the theater has a back room. Price is one conversation. Not a mission. A meeting.\"* Jarlaxle was on the rooftops. He watched every entrance and exit."
- Alexandrian PDF 17 (transcription, printed p.122): "Sealed Letter to Fenerus Stormcastle (Response Team: Krebbyg Masq'il'yr)" — `sources/17. Outpost and Lair Revelation Lists.pdf` PDF p.2.

The Sea Maidens Faire and the Dive (routed to **Sea Maidens Faire**, **The Dive**, **Jarlaxle Hostile**):
- `campaign/structure/arc-h-sea-maidens-faire.md:174` (U6; see D7)
- `campaign/structure/arc-h-sea-maidens-faire.md:275`: "- **Jarlaxle Hostile** (combat, casualties among BD lieutenants): If the party killed Soluun, Fel'rekt, or Krebbyg, Jarlaxle's response escalates from professional to personal. He reaches for leverage before force, but he reaches harder. BD response teams become more aggressive in future encounters."
- `campaign/quests/faction-events/bregan-daerthe/m06-the-dive/ev-01-the-dive.md:7`: "Take the brief from Krebbyg Masq'il'yr and Fel'rekt, and collect potions of water breathing, spears and lamps from the armory crate." (the list of the party's options)
- `campaign/quests/faction-events/bregan-daerthe/m06-the-dive/ev-01-the-dive.md:43`: "**Surface line:** A rope tied to the pier's outermost pile and held by Krebbyg."
- `campaign/quests/faction-events/bregan-daerthe/m06-the-dive/ev-02-before-dawn.md:265`: "Krebbyg and Fel'rekt wait on the pier and hold the line."
- `sources/adventure-wdh.json:14782`: "If {@creature Jarlaxle Baenre|WDH} (see {@adventure appendix B|WDH|12}) is the villain, he arrives with three {@creature drow gunslinger|WDH|drow gunslingers} (see {@adventure appendix B|WDH|12}). Replace no-name drow gunslingers with {@creature Fel'rekt Lafeen|WDH}, {@creature Krebbyg Masq'il'yr|WDH}, and {@creature Soluun Xibrindas|wdh} if they are alive and free."

Faction events (the day-one page must not restate these):
- `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:26`: "The watchers are Jarlaxle's three lieutenants. Fel'rekt Lafeen and Krebbyg Masq'il'yr shadow the party from dusk until dawn, and Soluun Xibrindas takes the day from shade and doorways." (rest of the passage covers Soluun's killings and the Dockside Killer)
- `campaign/quests/faction-events/bregan-daerthe/00-first-meeting/ev-01-first-meeting.md:42`: "Fel'rekt and Krebbyg work the night in turns, so one of them is always at the mouth of Trollskull Alley or on a roof across from the manor."
- `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:7`: "Take Krebbyg's brief and learn that a frightened Cassalanter steward is selling a floor plan of a windmill, and that the family has a watcher on him."
- `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:30`: "No Bregan D'aerthe speaker says \"Jarlaxle\" in this Event. Krebbyg says \"the captain\" or \"J.\"" (rest of the passage covers Zardoz and the Cassalanter watcher)
- `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/design-notes.md:24`: "If **Zardoz Introduced** is not marked, the box is empty and the hat sits on the rail, and Krebbyg carries the mission alone."
- `campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/ev-02-twelve-minutes.md:387`: "+1 Renown: return the captain's *bag of holding* to Arannis or Krebbyg, and keep the *Report on the Seven Masks Theater* out of the Guild's reach."
- `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/design-notes.md:13`: "He is an ordinary Dock Ward Watchman with no link to Bregan D'aerthe, and nobody in the company planned his visit, which suits Krebbyg, who never plans." (design note on Constable Pimm)

Trollskull guide (not day-one):
- `campaign/guides/trollskull-manor/06-tavern-time.md:29`: "| Tarsakh 11–20 | Jarlaxle Baenre (in disguise), Mattrim \"Threestrings\" Mereg, Rishaal the Page-Turner | 19: a courier arrives with an urgent message for a patron who just left | The patron who just left was Jarlaxle. The message, from Krebbyg, reads \"The tide turns on the twentieth.\" It's the party's last clear warning before the Faire sails. |"

Wiki (quest time, not day-one):
- wiki line 70: "In [[1492 DR]],{{WDH-time}} if Jarlaxle managed to obtain the ''[[Stone of Golorr]]'', then Fel'rekt and Krebbyg confronted some adventurers first in [[Mistshore]] where they had the support of the [[Lantanese]] mechanical [[dragon turtle]] [[Big Belchy]]<ref name=\"WDH5e-p67\">{{Cite book/Waterdeep: Dragon Heist|67}}</ref> and again in the [[Dock Ward]].<ref name=\"WDH5e-p72\">{{Cite book/Waterdeep: Dragon Heist|72}}</ref>"

---

## F. Gaps a Background needs that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

**F1. Birth, birth name, home, house name, parents, family, age.** No source gives any of these. The only age term is "He is young and rash." (`sources/adventure-wdh.json:32021`). The house is not named. Do not name a new Notable Figure (brief ruling 17). A nameless relative or place is allowed.

**F2. The destroyed house and how it fell.** Only "Krebbyg's house was destroyed long ago" (`sources/adventure-wdh.json:32021`) and "After the destruction of his house" (wiki line 68). Constraint: the company's founding rule that its members are "the rogue males of destroyed and disgraced houses" (`campaign/setting/villains/jarlaxle.md:46`) applies. Nar'l and Soluun Xibrindas had a house "wiped out long ago" (`campaign/setting/history/03-bregan-daerthes-long-road.md:43`). No source links Krebbyg's house to theirs, so the drafter must not give him the same house without `[design]`.

**F3. How he joined and when.** Only "he joined Bregan D'aerthe" after the house fell (wiki line 68) and "prove useful enough that Jarlaxle never regrets taking him in" (`campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:15`). No date.

**F4. How he came to run the theater, and when.** No source. The Dock Ward block gives the cover: "a booking manager who calls himself Kreb Sorrush handles casting inquiries and schedules" (`campaign/gazetteer/waterdeep/dock-ward.md:70`). The Persona says "The theater is the closest thing he has to a home outside Bregan D'aerthe" (L21). Any origin in theater work is `[design]`. The voice profile is the only source for his theatre skill ("Theatre jargon (bookings, blocking, the house, the ghost)", line 85).

**F5. Where the Luskan accent comes from.** Only the org page: "a slight Luskan accent that he makes no effort to conceal" (`campaign/setting/organizations/07-bregan-daerthe.md:59`). The company's Luskan connection: "After 1485 DR the High Captains trade legally across the Sword Coast and are secretly under the sway of Jarlaxle and the company." (`campaign/setting/history/03-bregan-daerthes-long-road.md:60`). The drafter may tie the accent to Luskan only as `[design]`.

**F6. Relationship with Malkolm Brizzenbright's ghost.** Only the Motivations line (L15) and the gazetteer: "He is not hostile" (`campaign/gazetteer/waterdeep/dock-ward.md:76`). The Malkolm voice profile gives his register as "Proprietary outrage and anxiety" (`.claude/skills/character-voices/voices/bregan-daerthe.md:141`). That is a voice, not a relationship. The Malkolm page does not mention Krebbyg.

**F7. Personal goals beyond the company.** None in any source. The page's Motivations give his wants toward Fel'rekt, the theater and Jarlaxle (L15). Brief ruling 17: the goals may not reveal a secret, an Event Outcome, a quest result or the Grand Game balance. A goal about the theater, a craft or a person is allowed as `[design]`.

**F8. The "basement".** The voice profile has Krebbyg's sample line "You want in the basement? Ha, no. Ask Fel." (`.claude/skills/character-voices/voices/bregan-daerthe.md:93`) and Malkolm's "There is a machine in my basement" (line 147). No file in `campaign/` gives the Seven Masks Theater a basement. The gazetteer's Seven Masks block lists "One dressing room is kept empty as a safe house" (`campaign/gazetteer/waterdeep/dock-ward.md:75`) and no basement. The Alexandrian Dock Ward text puts the safe house in "One of the dressing rooms" (PDF p.2, printed p.37). The drafter must not write a basement as a fact.

**F9. Faith.** None. Constraint: the Lolth rule (`campaign/setting/history/03-bregan-daerthes-long-road.md:34`). Krebbyg's own speech about the goddess is not in any file read. Do not invent a shrine or an invocation.

**F10. Physical appearance.** Only the cover ("a brown wig, pale greasepaint and gloves he never takes off", `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:15`), which is the disguise and is quest-time in its detail. The drow appearance is not described in any source.

**F11. Off-duty life outside the theatre.** None. The voice profile says he "gets bored with anything routine" and that "His pleasure in the theatre is real." (`.claude/skills/character-voices/voices/bregan-daerthe.md:87`).

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
- "He is an ordinary Dock Ward Watchman with no link to Bregan D'aerthe, and nobody in the company planned his visit, which suits Krebbyg, who never plans." — `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/design-notes.md:13` (design note on Constable Pimm; shows the trait)
- "Krebbyg is the close friend and operational partner of Fel'rekt Lafeen" — `campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:25`
- "Krebbyg resided on the Scarlet Marpenoth ship where he sharpened his sword." — wiki line 65
- "is here, sharpening his sword. His stateroom contains a net hammock and nothing else." — `sources/adventure-wdh.json:26451`

---

## Not found

- Birth, birth name, home, house name, parents, family, age, date of joining, the date he took the theater post: searched `campaign/` (Grep for "Krebbyg|Kreb\b|Kreb Sorrush|Masq.il"), `sources/adventure-wdh.json` (Grep for "Krebbyg"), `sources/*.md` (Grep), `sources/research/` (Grep). No match gives any of these.
- Faith and any shrine or prayer: the same search. Only the Lolth rule (`campaign/setting/history/03-bregan-daerthes-long-road.md:34`).
- Seven Masks basement: Grep for "basement" across `campaign/` gives no Seven Masks entry (see F8).
- Malkolm's page and Krebbyg: no mention (Grep of `campaign/setting/notable-figures/bregan-daerthe/07-malkolm-brizzenbright.md`).
- Alexandrian PDFs for Krebbyg. Read: `sources/5. Faction Outposts.pdf` (pp.1-2), `sources/17. Outpost and Lair Revelation Lists.pdf` (p.2), `sources/9. Lair – Sea Maidens Faire.pdf` (pp.1-3), `sources/1. The Villains.pdf` (p.5). Not read: `sources/4. Gralhund Villa.pdf`, `sources/3. Player Character Factions.pdf`, `sources/26. Addendum Other Collaborators.pdf`, `sources/11. Lair Xanathar's Lair.pdf`. Those may hold more BD text and were not checked for his name.
- Wiki: no line on his birth, parentage, home, age or house name. The infobox fields `age` (wiki line 17), `dob` (line 21), `parents` (line 29) and `siblings` (line 31) are blank. The `home` field (line 11) gives only "[[Waterdeep]], [[Sword Coast North]]".

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. `sources/SOURCE_GUIDE.md:690` lists `Jarlaxle Baenre NPC Guide.docx` as the Jarlaxle persona source. Its lines are cited in `campaign/setting/history/03-bregan-daerthes-long-road.md:140`. Not checked for Krebbyg.
- The `campaign/quests/faction-events/bregan-daerthe/` event files and the Gralhund journal were read through Grep (the full files are too large to read whole). Quotes are exact Grep output.
