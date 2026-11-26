# Pass 6 research notes: Ulkoria Stonemarrow

Page: `campaign/setting/notable-figures/trollskull-community/09-ulkoria-stonemarrow.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR.
Organization page: none for the Watchful Order of Magists and Protectors. The Force Grey page (`campaign/setting/organizations/05-force-grey.md:92`) names the Order as the body Vajra heads (see D3). Guilds page: `campaign/setting/governance-and-guilds/guilds.md:48`.
Voice profile: `.claude/skills/character-voices/voices/trollskull-community.md` lines 151 to 165.
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/trollskull-community/01-talisolvanar-fellbranch.md`

## Method and caveats

- Campaign files: Grep and Read. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string (escapes shown as plain quotes).
- Appendix D: `sources/Appendix_D_-_Running_the_Tavern.md`.
- Alexandrian PDF: `sources/27. Addendum A Night in Trollskull Manor.pdf`, read with the Read tool's `pages` parameter (38 pages, printed 178 to 215). Every PDF quote is a transcription from the page image. **Check each with `pdftotext -layout` before it goes into prose.** No shell was available.
- Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-trollskull-community/09-ulkoria-stonemarrow.txt`. Citation key `WDH5e-p42`. The description and some relationships cite a video game, `idle` (Idle Champions of the Forgotten Realms), which is not a tabletop edition.
- `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **The "at cost" glyph price conflicts with every source.** The page (Persona) and the voice profile say "at cost". The adventure says "for which she charges 300 gp apiece" (`sources/adventure-wdh.json:4136`). Appendix D says the 300 gp is "below her usual rate" (`sources/Appendix_D_-_Running_the_Tavern.md:1428`). See D1.
2. **The Masked Lord claim is campaign-only, and the page does not say so.** No source names Ulkoria as a Masked Lord. The page's line 25 states it flat, with only "(never confirmed in her presence)". The gazetteer (`north-ward.md:281`) says the page tags it "campaign only in its own GM Notes", but this page has no GM Notes block. See D2.
3. **The Watchful Order label is inconsistent across files.** Page line 6 says "Trollskull Alley community"; the guilds page says "Order members in Trollskull Alley"; the Force Grey page says "a senior member of the Watchful Order that Vajra heads". See D3.
4. **The Alexandrian PDF makes her a friendly archmage.** The PDF (printed p.200) says "But incredibly friendly and personable; like everyone's favorite grandmother." The adventure, Appendix D and the campaign voice all give a blunt, unfriendly archmage. See D5.
5. **The PDF names the orphanage owner "Arissa Mirthkettle"; the adventure does not.** The campaign uses neither name. See A2.

---

## A. Background facts by theme

### A1. Origin, rank and the Order

**Adventure, Sample Guild Representatives, Ulkoria (page 42)**
> "{@i Watchful Order of Magists and Protectors}"
> — `sources/adventure-wdh.json:4133`

**Adventure, page 42, first paragraph**
> "Ulkoria (NG female shield dwarf {@creature archmage}) has defended Waterdeep with her magic more times than she can recall. She's known as \"the Gargoyle\" because her face is frozen in a scowl that frightens adults and children alike. No one knows where she lives, but it's believed to be underground, possibly a cellar or dungeon under one of the city's oldest estates. She uses {@spell teleport} spells to enter and leave her home, and she's never seen without her {@creature shield guardian} close by."
> — `sources/adventure-wdh.json:4134`

**Appendix D, Ulkoria (page 42), heading**
> "*Watchful Order of Magists and Protectors — NG female shield dwarf, Archmage*"
> — `sources/Appendix_D_-_Running_the_Tavern.md:1420`

**Appendix D, Appearance (page 42)**
> "**Appearance:** Permanent scowl that is not, the characters will eventually learn, the same as disapproval. Silver hair braided back with utilitarian precision. Her Shield Guardian — a massive animated suit of plate — waits outside. It blocks the alley view. No one mentions this to her."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1422`

**Appendix D, roster**
> "| 13 | Ulkoria Stonemarrow |"
> — `sources/Appendix_D_-_Running_the_Tavern.md:1117`

**Gazetteer, North Ward, Organizations**
> "the Watchful Order (Ulkoria Stonemarrow and Rishaal the Page-Turner in Trollskull Alley)"
> — `campaign/gazetteer/waterdeep/north-ward.md:34`

**Gazetteer, North Ward, Ulkoria entry**
> "**Ulkoria Stonemarrow (Neutral Good, Shield Dwarf, she/her)**"
> "- Known as \"the Gargoyle\", an archmage of the Watchful Order whose face is frozen in a scowl that frightens adults and children alike. Nobody knows where she lives, and she is never seen without her shield guardian."
> — `campaign/gazetteer/waterdeep/north-ward.md:138` and `:139`

**Wiki, lead and occupation (edition WDH5e-p42)**
> "'''Ulkoria Stonemarrow''' was an [[archmage]] representative of the [[Watchful Order of Magists and Protectors]] in [[Waterdeep]] in the early 1490s [[DR]].<ref name=\"WDH5e-p42\" />"
> — `scratchpad/wiki-trollskull-community/09-ulkoria-stonemarrow.txt:63`

**Wiki, Description (cites `idle`, a video game)**
> "Ulkoria was a small but stout [[Shield dwarven]] woman. By the age of 377 winters, Ulkoria had a light-colored, wrinkled skin and a mostly gray head of hair, with some strands still retaining their chestnut-brown color. Many nicknamed her \"the Gargoyle\" as her face was frozen in a scowl. She was known for her withering stares that left very few unaffected."
> — `scratchpad/wiki-trollskull-community/09-ulkoria-stonemarrow.txt:66`

**Alexandrian PDF, printed p.200 (PDF page 23), Background, bullet 2**
> "No one knows where she lives, but it's believed to be underground, possibly a cellar or a dungeon under one of the city's oldest estates. (She uses teleport spells to enter and leave her home.)"
> — `sources/27. Addendum A Night in Trollskull Manor.pdf`, PDF page 23. **Check with pdftotext.**

**Alexandrian PDF, printed p.200, Stats**
> "NG female shield dwarf **archmage** (MM p. 342)"
> — PDF page 23.

### A2. The tavern she owned, and who came after her

**Adventure, page 42**
> "A little-known fact is that Ulkoria once owned the tavern in Trollskull Alley. She sold it to a family of shield dwarves, who fell on hard times and sold it to a woman who made it into an orphanage. \"Turned out to be a hag who was cooking and eating the children,\" Ulkoria recalls. The estate passed through several more hands in the years that followed. Ulkoria hopes the new owners make something good of it."
> — `sources/adventure-wdh.json:4135`

**Alexandrian PDF, printed p.181 (PDF page 4), history list**
> "Owned by Ulkoria Stonemarrow. She sold the tavern to go adventuring."
> "Sold to a family of shield dwarves. They fell on hard times and sold it to a woman named Arissa Mirthkettle."
> — PDF page 4 (printed p.181). **Check with pdftotext.** "Arissa Mirthkettle" is PDF-only. The adventure leaves the orphanage owner unnamed. The campaign uses neither name.

**Alexandrian PDF, printed p.200 (PDF page 23), Background, bullet 3**
> "Once owned Trollskull Manor. She sold it to a family of shield dwarves who fell on hard times and sold it to a woman who made it into an orphanage. The woman, Arissa Mirthkettle, turned out to be a hag who was cooking and eating the children. It was then abandoned for many years before being acquired by a half-elf named Lif."
> — PDF page 23. **Check with pdftotext.**

**Wiki, History (edition WDH5e-p42)**
> "By the age of 377, Ulkoria had defended the City of Splendors more times than she could even recount.<ref name=\"idle\" /> Ulkoria once owned the tavern in [[Trollskull Manor]] and had followed all the different owners of the place.<ref name=\"WDH5e-p42\" />"
> — `scratchpad/wiki-trollskull-community/09-ulkoria-stonemarrow.txt:75`

**Gazetteer, North Ward, Lore**
> "- Trollskull Manor has had a string of owners. Ulkoria once owned the tavern and sold it to a family of shield dwarves, who fell on hard times and sold it to a woman who ran it as an orphanage. She turned out to be a hag who cooked and ate the children. Volo bought the building recently, hoping its haunting would give him a chapter for his next book."
> — `campaign/gazetteer/waterdeep/north-ward.md:198`

### A3. Her visits to the tavern and her glyph service

**Adventure, page 42 (visits)**
> "Anytime she passes through the North Ward, Ulkoria stops by the tavern for a drink and to check out the place while her shield guardian waits outside. If she doesn't like what the characters have done with the establishment, she keeps her criticisms to herself. The characters can hire her to cast {@spell glyph of warding||glyphs of warding} on the place, for which she charges 300 gp apiece."
> — `sources/adventure-wdh.json:4136`

**Appendix D, Topics & Agendas (page 42)**
> "2. Offers to add a *Glyph of Warding* to the cellar access for 300 gp — below her usual rate, which she does not explain. She will say only that the previous tenant of this property made enemies she considers unresolved. She means the hag. She will not elaborate on the hag."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1428`

**Alexandrian PDF, printed p.200, Key Info**
> "Used to own Trollskull Manor. Hopes the new owners make something good of it."
> "Charges 300 gp for castings of *glyphs of warding*."
> — PDF page 23. **Check with pdftotext.**

### A4. Personal habits, manner and what she keeps to herself

**Appendix D, Roleplaying Keys (page 42)**
> "**Roleplaying Keys:** Delivers criticism inside compliments so compressed the compliment is nearly invisible. Examines rooms the way archivists examine manuscripts. Has opinions about the placement of every piece of furniture in the tavern and will share three of them if given any opening."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1424`

**Appendix D, Topics & Agendas (page 42)**
> "1. Has come to say the place is holding together better than she expected. She does not say this. She says the eastern wall is showing acceptable settling. This is the same thing."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1427`

**Appendix D, Topics & Agendas (page 42)**
> "3. Has heard something through the Order that she believes the characters should be aware of: a specific type of arcane signature has been detected in the North Ward three times in the past tenday. She does not know what it is. She is here because the Trollskull is on the same block. She will share the signature's description if asked; it is consistent with either Xanathar Guild gazer activity or something older. She does not know which."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1429`

**Appendix D, Topics & Agendas (page 42)**
> "4. Examines Lif. Watches him work for ten minutes without ordering anything. Then orders a single measure of whatever Lif considers his best and drinks it in silence. Leaves a large tip on the bar. This is, in Ulkoria's emotional vocabulary, an extraordinary endorsement."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1430`

**Alexandrian PDF, printed p.200, Roleplaying Notes**
> "A permanent scowl inflicted by some unknown cause."
> "But incredibly friendly and personable; like everyone's favorite grandmother."
> "Occasionally gets a distant look in her eyes, waggles her fingers, and will murmur something like, \"That's better.\" under her breath. (It's unclear if she's pulling people's legs with this routine.)"
> — PDF page 23. **Check with pdftotext.** The "friendly" line conflicts with the campaign's Persona and voice (D5).

### A5. Her shield guardian and her dealings with Jarlaxle (wiki only)

**Wiki, Relationships (edition WDH5e-p42 and `idle`)**
> "Ulkoria had always at her side her [[shield guardian]]. She did command several animated [[gargoyle]]s that were used to keep her tavern always clean. At some point before the late 15{{th}} century DR, Ulkoria became acquainted with [[Jarlaxle]]. The [[drow]] man often tried to convince Ulkoria to sponsor mass production of [[stuffed toy]]s in his image."
> — `scratchpad/wiki-trollskull-community/09-ulkoria-stonemarrow.txt:69`

**Wiki, Possessions (edition `idle`)**
> "Ulkoria wielded an [[enchanted]] ''[[Watchful Order staff]]'' and wore a pin, adorned with the symbol of the magical school of [[Transmutation]]."
> — `scratchpad/wiki-trollskull-community/09-ulkoria-stonemarrow.txt:72`

Campaign check: `campaign/setting/notable-figures/trollskull-community/09-ulkoria-stonemarrow.md` has no Jarlaxle line. A grep of `campaign/` for "Ulkoria" returns no villains file. The adventure's Ulkoria entry (`sources/adventure-wdh.json:4129` to `:4136`) does not mention Jarlaxle. The Jarlaxle link is **wiki only**.

**Wiki, 1492 DR (edition WDH5e-p42 and `idle`; quest-time as written)**
> "In the {{YearlinkName|1492}},{{WDH-time}} Ulkoria went to check on the new owners of the place.<ref name=\"WDH5e-p42\" /> During the same period of time, Ulkoria was asked to write a review of [[Volothamp Geddarm]]'s new [[book]], ''[[Volo's Guide to the Weave]]'' for the ''[[Sentinel (chapbook)|Sentinel]]'' [[chapbook]].<ref name=\"idle\" />"
> — `scratchpad/wiki-trollskull-community/09-ulkoria-stonemarrow.txt:77`

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Summary: "> - *Shield dwarf archmage, neutral good, she/her*. Stat block: **Archmage**." — `campaign/setting/notable-figures/trollskull-community/09-ulkoria-stonemarrow.md:5`
- Adventure: "NG female shield dwarf {@creature archmage}" (`sources/adventure-wdh.json:4134`)
- Appendix D: "*Watchful Order of Magists and Protectors — NG female shield dwarf, Archmage*" (`sources/Appendix_D_-_Running_the_Tavern.md:1420`)
- PDF: "NG female shield dwarf **archmage** (MM p. 342)" (PDF page 23, printed p.200)
- Wiki: "| alignment5e    = [[Neutral good]]" (`scratchpad/wiki-trollskull-community/09-ulkoria-stonemarrow.txt:58`)
- Trollskull Manor guide: "**Ulkoria Stonemarrow** *(Watchful Order of Magists and Protectors, NG female shield dwarf, Archmage)*" (`campaign/guides/trollskull-manor/08-notable-patrons.md:96`)
- All sources agree: neutral good.

**Species**
- Summary: "*Shield dwarf archmage, neutral good, she/her*" (`09-ulkoria-stonemarrow.md:5`)
- Adventure: "NG female shield dwarf" (`sources/adventure-wdh.json:4134`)
- Wiki: "| race           = [[Dwarf]]" (line 15) and "| ethnicity      = [[Shield dwarf]]" (line 16)
- All sources agree: shield dwarf.

**Pronouns**
- Summary: "she/her" (`09-ulkoria-stonemarrow.md:5`)
- Adventure: "NG female shield dwarf" (`sources/adventure-wdh.json:4134`)
- Appendix D: "NG female shield dwarf" (`sources/Appendix_D_-_Running_the_Tavern.md:1420`)
- Wiki: "| sex            = Female" (line 13) and "| gender         = Feminine" (line 14)
- PDF: "A female dwarf whose face has been frozen..." (PDF page 23)
- All sources agree: she/her.

**Stat block**
- Summary: "Stat block: **Archmage**." (`09-ulkoria-stonemarrow.md:5`)
- Adventure: "{@creature archmage}" (`sources/adventure-wdh.json:4134`)
- PDF: "NG female shield dwarf **archmage** (MM p. 342)" (PDF page 23)
- Wiki: "| class5e        = [[Archmage]]" (line 60)

---

## C. Sentences on the current page that narrate a quest-time event or a day-one conflict

Current page: `campaign/setting/notable-figures/trollskull-community/09-ulkoria-stonemarrow.md`. Sections: Gamemaster's Summary, Roleplaying Information, Character Information (Persona, Morale, Relationships), Overview. No Background yet.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L6 | "> - **Affiliation:** Trollskull Alley community" | Label. See D3 | No organization page. See D3 |
| 2 | L7 | "> - **Featured in:** **Trollskull Alley**, **Trollskull Manor**" | Quest list. Incomplete (E3) | `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:29`; `ev-06-the-grand-opening.md:155`; `campaign/guides/trollskull-manor/06-tavern-time.md:31` |
| 3 | L11 | "**Resonance.** Ulkoria should inspire intimidation with her permanent scowl and blunt manner, gratitude when her rare approval lands like a benediction, and sympathy for the loneliness beneath the Gargoyle's reputation." | Day-one character. Keep | Appendix D `:1422` (scowl); voice line 158 |
| 4 | L13 | "**Emotions.** Ulkoria most often feels grim satisfaction, protective vigilance, impatient disdain for small talk, buried nostalgia for the tavern she once owned, reluctant approval, and carefully buried grief." | Day-one (she owned it earlier). Keep | `sources/adventure-wdh.json:4135` ("Ulkoria hopes the new owners make something good of it.") |
| 5 | L15 | "**Motivations.** Ulkoria wants to ensure the tavern does not fall into dangerous hands again, defend Waterdeep from arcane threats (as she has done more times than she can count), and determine whether the party is worthy of the building she once called hers." | A goal, not an event. "the party" presumes the party. Keep verbatim except the party reference (ruling 3). Drafter restates as "the new owners" | `sources/adventure-wdh.json:4135` (new owners) |
| 6 | L17 | "**Inspirations.** When playing Ulkoria, channel Professor McGonagall (*Harry Potter*), Olenna Tyrell (*Game of Thrones*), and Izumi Curtis (*Fullmetal Alchemist*)." | Not an event. Keep | — |
| 7 | L21 | "**Persona.** To the world, Ulkoria is \"the Gargoyle,\" a shield dwarf archmage whose permanent scowl frightens adults and children alike." | Day-one. Matches `sources/adventure-wdh.json:4134` | — |
| 8 | L21 | "To those she trusts, she offers her shield guardian's protection and glyph of warding at cost." | Day-one habit, but "at cost" conflicts with the sources (D1). "shield guardian's protection" has no source | `sources/adventure-wdh.json:4136` (300 gp apiece) |
| 9 | L21 | "Deep down, she sold the tavern and has watched every subsequent owner fail, one of them catastrophically." | Day-one backstory. "watched every subsequent owner fail" is campaign wording; the adventure says "Ulkoria hopes the new owners make something good of it." (`:4135`) | `sources/adventure-wdh.json:4135` |
| 10 | L21 | "She visits not to inspect but to see whether this time will be different." | Day-one habit. The adventure says she visits: "Anytime she passes through the North Ward, Ulkoria stops by the tavern..." (`:4136`). "whether this time will be different" is campaign wording | `sources/adventure-wdh.json:4136` |
| 11 | L23 | "**Morale.** In a fight, Ulkoria would unleash archmage-level spells without hesitation or warning. She has defended Waterdeep more times than she can recall and does not require permission to do it again." | Day-one. Keep | `sources/adventure-wdh.json:4134` ("defended Waterdeep with her magic more times than she can recall") |
| 12 | L25 | "**Relationships.** Ulkoria is a senior member of the Watchful Order of Magists and Protectors, the tavern's former owner, a colleague of Rishaal the Page-Turner, and a Masked Lord of Waterdeep (never confirmed in her presence)." | Day-one, except the Masked Lord clause (campaign-only; D2) and "a colleague" (D4) | Order: `sources/adventure-wdh.json:4133`. Former owner: `sources/adventure-wdh.json:4135`. Rishaal: `campaign/setting/notable-figures/trollskull-community/06-rishaal-the-page-turner.md:25` |
| 13 | L29 | "Ulkoria Stonemarrow — \"the Gargoyle\" to the North Ward — is a shield dwarf archmage who sold Trollskull Manor years ago and has watched it suffer under every owner since." | Day-one backstory. "years ago" has no source date. "watched it suffer" is campaign wording | `campaign/gazetteer/waterdeep/north-ward.md:139` (the Gargoyle) |
| 14 | L29 | "She calls on the party without warning and with few words of welcome." | Quest-time framing ("the party"). The habit is sourced: "Appears without knocking." Route | `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:29` |

**Voice profile, quest-time clauses (`.claude/skills/character-voices/voices/trollskull-community.md`, lines 151 to 165)**

- Line 156 "She calls the party "you lot" and the tavern "my old house"." — "the party" is the quest's party; "my old house" is a day-one fact (she owned it). Drafter's call (ruling 16).
- Line 163 "*Greeting:* "You're the new owners. Hm."" — **quest-time clause.** "the new owners" means the party holds the tavern, which the adventure gives after Volo's quest: "Following the completion of Volo's quest, the characters gain a home base with an address in Trollskull Alley, in Waterdeep's North Ward." (`sources/adventure-wdh.json:1595`). The drafter must restate as a day-one line (for example, the owner of the building a stranger has just bought). Profile change is for the drafter (ruling 16).
- Line 164 "*Business:* "Glyph of warding on the cellar, at cost. Don't argue."" — **conflicts with the 300 gp price** (D1). "at cost" must be changed or flagged.
- Line 165 "*Under pressure:* "Get behind me."" — day-one. Keep.
- Line 158 "She's guarding a nostalgia she won't admit, and it shows when she corrects details of the building ("That was a window.")." — day-one. Keep.

### C2. Where Ulkoria's quest-time events already live (routed; do not restate on the day-one page)

- **Trollskull Alley, ev-02, Watchful Order attestation**: "The Order requires written attestation that the haunting poses no public safety risk. Two qualified signatories in the alley: Rishaal the Page-Turner or Ulkoria Stonemarrow (both Watchful Order members in good standing)." — `campaign/quests/act-i/trollskull-alley/ev-02-the-guild-gauntlet.md:50`
- **Trollskull Alley, ev-02, checklist**: "The Watchful Order's inspector wants to know if your poltergeist has a safety certification." — `ev-02-the-guild-gauntlet.md:82`
- **Trollskull Alley, ev-03 (The Neighbors)**: "**Ulkoria Stonemarrow (Watchful Order).** Appears without knocking. Inspects the courtyard oak tree — circles it, lays one hand on the bark, says nothing. Examines the cellar door. Leaves a pre-filled invoice for two glyphs of warding: 600 gp for both (300 gp each), take it or leave it. When departing: \"The building has had bad luck with owners. Don't contribute to the pattern.\" She is a Masked Lord of Waterdeep. The party will not learn this in this quest. Her inspection is protective. Cross-ref the **Ulkoria Stonemarrow** page in Notable Figures." — `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:29`
- **Trollskull Alley, ev-06 (The Grand Opening), neighbors**: "**Neighbors** — Tally, Embric and Avi, Fala, Rishaal (all four attend). Vincent Trench sends regrets via a note and a gift of expensive pipe tobacco. Ulkoria arrives late, drinks one ale, says \"Acceptable,\" and leaves." — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:40`
- **Trollskull Alley, ev-06, readaloud**: "> The taproom fills before the hour mark. The bar is covered in tools you didn't lay out. The chalk slate has the night's specials in handwriting that isn't yours. Ulkoria Stonemarrow drinks one ale, says \"Acceptable,\" and leaves. Ammalia Cassalanter stays two hours and knows everyone's name when she goes. By the end of the night you realize the building feels different. Like it has decided something." — `ev-06-the-grand-opening.md:155`
- **Trollskull Alley overview**: "- **Ulkoria Stonemarrow** (Watchful Order / Masked Lords) — mage neighbor; glyph offer; inspects the courtyard oak without explanation" — `campaign/quests/act-i/trollskull-alley/overview.md:36` (quest summary; label conflict, D3)
- **Trollskull Manor area overview, Courtyard**: "Ulkoria Stonemarrow inspects this tree during her **The Neighbors** Event visit without explaining why." — `campaign/locations/trollskull-manor/area-overview.md:15`
- **Trollskull Manor guide, Tavern time, Mirtul row**: "| Mirtul 1–10 | Rishaal the Page-Turner, Ulkoria Stonemarrow, Vincent Trench | 9: Kyser Tameno's first visit | Arcane gossip night. An archmage of the Watchful Order drinks two tables from a rakshasa in disguise, and a wizard walks out of the wall. |" — `campaign/guides/trollskull-manor/06-tavern-time.md:31`
- **Trollskull Manor guide, Patron table**: "| 13 | Ulkoria Stonemarrow |" — `campaign/guides/trollskull-manor/06-tavern-time.md:69`
- **Trollskull Manor guide, Notable Patrons**: "- Offers to add a *Glyph of Warding* to the cellar access for 300 gp; says the previous tenant made enemies she considers unresolved. Means the hag. Will not elaborate on the hag." — `campaign/guides/trollskull-manor/08-notable-patrons.md:99`
- **Trollskull Manor guide, Notable Patrons**: "- An arcane signature detected in the North Ward three times this tenday — consistent with either Xanathar gazer activity or something older. Tells the party because the Trollskull is on the same block." — `campaign/guides/trollskull-manor/08-notable-patrons.md:100`
- **Trollskull Manor guide, Notable Patrons**: "- Examines Lif for ten minutes without ordering. Then orders his best, drinks it in silence, leaves a large tip. This is, in Ulkoria's vocabulary, an extraordinary endorsement." — `campaign/guides/trollskull-manor/08-notable-patrons.md:101`
- **Gazetteer, North Ward, Defense**: "- Ulkoria Stonemarrow and Rishaal the Page-Turner are both Watchful Order members in good standing, and either can sign the written attestation that the Order's inspector asks for about the tavern's poltergeist." — `campaign/gazetteer/waterdeep/north-ward.md:178`
- **Bregan D'aerthe, Commander, ev-01 (audience with a Lord)**: "| Ulkoria Stonemarrow, or the Watchful Order | Ulkoria Stonemarrow | A reading room in the Castle Ward, an hour before noon |" — `campaign/quests/faction-events/bregan-daerthe/r25-commander/ev-01-commander.md:160`
- **Bregan D'aerthe, Commander, ev-01, reward**: "- **A Lord the company can reach (Mirt, Durnan, Ulkoria Stonemarrow or Jelenn Urmbrusk):** record that Lord's name against the member as the **Seat**. Zardoz toasts the choice. The first audience favour the member asks for in the campaign cannot be refused for that Lord, and the meeting lasts half an hour instead of ten minutes." — `campaign/quests/faction-events/bregan-daerthe/r25-commander/ev-01-commander.md:326`
- **Bregan D'aerthe, Commander, design notes**: "The four reachable Lords are Mirt, Durnan, Ulkoria Stonemarrow and Jelenn Urmbrusk, each confirmed as a Masked Lord on their Notable Figures pages (Ulkoria's is \"never confirmed in her presence\", and Durnan's is \"secret\"). Zardoz never confirms any of them aloud." — `campaign/quests/faction-events/bregan-daerthe/r25-commander/design-notes.md:37`
- **Adventure, Sample Guild Representatives intro (quest-time framing)**: "Once it becomes known around the city that the tavern in Trollskull Alley is planning to reopen its doors to the public, the adventurers receive visits from guild representatives interested in the tavern's welfare. This section describes a handful of these representatives." — `sources/adventure-wdh.json:4094`
- **Structure doc (superseded, do not use for content)**: `campaign/structure/arc-b-trollskull-alley.md:215` ("Ulkoria arrives late, drinks one ale, says "Acceptable," and leaves.").

---

## D. Conflicts

**D1. The glyph of warding price.**
- Page Persona: "To those she trusts, she offers her shield guardian's protection and glyph of warding at cost." — `campaign/setting/notable-figures/trollskull-community/09-ulkoria-stonemarrow.md:21`
- Voice profile: "*Business:* "Glyph of warding on the cellar, at cost. Don't argue."" — `.claude/skills/character-voices/voices/trollskull-community.md:164`
- Adventure: "The characters can hire her to cast {@spell glyph of warding||glyphs of warding} on the place, for which she charges 300 gp apiece." — `sources/adventure-wdh.json:4136`
- Appendix D: "Offers to add a *Glyph of Warding* to the cellar access for 300 gp — below her usual rate, which she does not explain." — `sources/Appendix_D_-_Running_the_Tavern.md:1428`
- PDF (printed p.200): "Charges 300 gp for castings of *glyphs of warding*." — PDF page 23.
- Quest: "Leaves a pre-filled invoice for two glyphs of warding: 600 gp for both (300 gp each), take it or leave it." — `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:29`
- Higher ranked: the adventure, which Appendix D and the PDF confirm. "at cost" conflicts with "charges 300 gp" and with Appendix D's "below her usual rate". The drafter should not write "at cost" as a fact.

**D2. The Masked Lord claim, and what each file says.**
- Page: "a Masked Lord of Waterdeep (never confirmed in her presence)" — `09-ulkoria-stonemarrow.md:25`. The page has no GM Notes block and no "campaign only" tag.
- Governance page: "The campaign makes her a Masked Lord, which is never confirmed in her presence (campaign-only)." — `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:46`
- Governance page GM Notes: "**Campaign-only facts:** Durnan as a secret Masked Lord and the founder of the Red Sashes, Ulkoria as a Masked Lord and Laeral as a moon elf come from the campaign, and the published adventure names only Mirt among the Lords. ... Ulkoria's office is stated in **The Neighbors**, and the party does not learn it in that quest." — `open-lord-and-masked-lords.md:60`
- Quest: "She is a Masked Lord of Waterdeep. The party will not learn this in this quest." — `ev-03-the-neighbors.md:29` (stated flat, not "campaign-only")
- North Ward gazetteer: "**Conflicts:** Ulkoria as a Masked Lord. This is a campaign-only claim on her Notable Figures page (line 25), and the page tags it as campaign only in its own GM Notes. Dragon Heist names only Mirt as the Masked Lord among the Castle Ward residents." — `campaign/gazetteer/waterdeep/north-ward.md:281`. **Stale:** the page has no GM Notes tag.
- Adventure: the Ulkoria entry (`sources/adventure-wdh.json:4129` to `:4136`) does **not** call her a Masked Lord. Appendix D (`sources/Appendix_D_-_Running_the_Tavern.md:1419` to `:1430`) does not either. The PDF (printed p.200) does not either. Source status: **none.**
- Adventure Masked Lords, for context: "Jelenn Urmbrusk, a Masked Lord in debt to {@creature Manshoon|WDH}, requests an interest-free loan of 10,000 gp" — `sources/adventure-wdh.json:14896`. Manshoon's ledger list is introduced at "Slipped into the ledger is a piece of paper with a list of names in {@creature Manshoon|WDH}'s handwriting. {@creature Manshoon|WDH} keeps this list of Masked Lords whose identities he knows, with check marks indicating the ones he's blackmailing:" — `sources/adventure-wdh.json:30299`. The governance page reads the list as Mirt, Corylus Thann, Thardouk Starbuckler, Jelenn Urmbrusk and Dorgar Adarbrent (`open-lord-and-masked-lords.md:63`).
- The governance page says "the published adventure names only Mirt among the Lords" (`open-lord-and-masked-lords.md:60`). This is **contradicted** by `sources/adventure-wdh.json:14896` (Jelenn) and `:30299` (the list). Higher ranked: the adventure. The gazetteer's "names only Mirt" (`north-ward.md:281`) repeats the same error.
- The Bregan D'aerthe design notes say each Lord is "confirmed as a Masked Lord on their Notable Figures pages (Ulkoria's is "never confirmed in her presence")" (`campaign/quests/faction-events/bregan-daerthe/r25-commander/design-notes.md:37`). The Ulkoria page does not confirm it, and its own wording is "never confirmed".

**D3. Watchful Order label and Ulkoria's place in it.**
- Page summary: "> - **Affiliation:** Trollskull Alley community" — `09-ulkoria-stonemarrow.md:6`
- Page Relationships: "Ulkoria is a senior member of the Watchful Order of Magists and Protectors" — `09-ulkoria-stonemarrow.md:25`
- Guilds page: "**Rishaal the Page-Turner** (Neutral, Gold Dragonborn, he/him) and **Ulkoria Stonemarrow** (Neutral Good, Shield Dwarf, she/her) are Order members in Trollskull Alley, and in The Guild Gauntlet either of them can sign the written statement that the poltergeist Lif poses no public danger." — `campaign/setting/governance-and-guilds/guilds.md:48`
- Force Grey organization page: "Ulkoria Stonemarrow, a senior member of the Watchful Order that Vajra heads, is also a Masked Lord in the campaign (**North Ward**)." — `campaign/setting/organizations/05-force-grey.md:92`
- Force Grey Notable Figure: "- **Ulkoria Stonemarrow:** A senior member of the Watchful Order that Vajra heads. The campaign makes her a Masked Lord, and no source says that Vajra knows." — `campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md:43`
- Order of the Gauntlet organization page: "**Conflicts:** Rishaal the Page-Turner and Ulkoria Stonemarrow. `campaign/setting/governance-and-guilds/guilds.md:48` calls them Order members, and their Notable Figures pages (`trollskull-community/06` and `09`, line 6) label them Trollskull Alley community. The page follows the Notable Figures pages, so neither is in Key Members." — `campaign/setting/organizations/04-order-of-the-gauntlet.md:158`
- Trollskull Alley overview: "- **Ulkoria Stonemarrow** (Watchful Order / Masked Lords) — mage neighbor" — `overview.md:36` (quest summary; does not govern, brief ruling 6).
- Adventure: the Order is "headed by the Blackstaff" (`sources/adventure-wdh.json:30578`: "...will be strongly encouraged to join the Watchful Order of Magists and Protectors, headed by the Blackstaff."). The adventure gives Ulkoria no role in the Order.
- Higher ranked for the label: the Notable Figures page (it governs the drafter's label under ruling 6), with the guilds and Force Grey pages recording the Order membership. **Open:** the page label "Trollskull Alley community" and the Order membership are both in the campaign; the drafter must choose one label. Report only.

**D4. Rishaal relationship.**
- Ulkoria page: "a colleague of Rishaal the Page-Turner" — `09-ulkoria-stonemarrow.md:25`
- Rishaal page: "Rishaal is a member of the Watchful Order of Magists and Protectors, a professional acquaintance of Ulkoria Stonemarrow (whose arcane purchases he respects), and an increasingly suspicious neighbor of Vincent Trench." — `campaign/setting/notable-figures/trollskull-community/06-rishaal-the-page-turner.md:25`
- Adventure: none. "colleague" and "professional acquaintance" are campaign wording. Conflict between two campaign pages.

**D5. Her personality in the PDF versus the campaign.**
- PDF (printed p.200): "But incredibly friendly and personable; like everyone's favorite grandmother." — PDF page 23. **Check with pdftotext.**
- Adventure: "a scowl that frightens adults and children alike" (`sources/adventure-wdh.json:4134`); "If she doesn't like what the characters have done with the establishment, she keeps her criticisms to herself." (`:4136`)
- Voice profile: "She never makes small talk" (line 161), "Impatient with small talk" (line 158).
- Higher ranked: the adventure and the campaign voice. The PDF line is an Alexandrian addition. Drafter's call, but the Persona and voice contradict the PDF.

**D6. Stat block and the "archmage" line.** No conflict. The wiki gives the "archmage" class (line 60), as does the adventure (`:4134`).

**D7. The sale of the tavern: a reason.** PDF (printed p.181): "She sold the tavern to go adventuring." No other source gives a reason. Not a conflict; a PDF-only motive.

---

## E. Stale lines in other files (not edited) and routed quest references

**E1. Stale or conflicting lines**
- `campaign/gazetteer/waterdeep/north-ward.md:281`: "This is a campaign-only claim on her Notable Figures page (line 25), and the page tags it as campaign only in its own GM Notes." **Stale:** the page has no GM Notes block (`09-ulkoria-stonemarrow.md` lines 1 to 30).
- `campaign/gazetteer/waterdeep/north-ward.md:281`: "Dragon Heist names only Mirt as the Masked Lord among the Castle Ward residents." — the adventure names Jelenn as a Masked Lord too (`sources/adventure-wdh.json:14896`).
- `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:60`: "the published adventure names only Mirt among the Lords" — contradicted by `sources/adventure-wdh.json:14896` and `:30299`.
- `campaign/quests/faction-events/bregan-daerthe/r25-commander/design-notes.md:37`: "each confirmed as a Masked Lord on their Notable Figures pages" — the Ulkoria page says "never confirmed in her presence".
- `campaign/quests/act-i/trollskull-alley/overview.md:36`: "(Watchful Order / Masked Lords)" — quest summary; the Masked Lord claim is campaign-only.
- `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:29`: "She is a Masked Lord of Waterdeep." (stated flat; the page says "never confirmed in her presence").
- `campaign/setting/deities/baba-yaga.md:82` and `:89` cite the Ulkoria page without a line for the hag story. No conflict; no line to correct. (`baba-yaga.md:63` cites the Broxley page for the hag at line 26; see the Broxley notes.)

**E2. Routed quest references (quest-time facts)**: see C2. In short: Trollskull Alley ev-02 (lines 50, 82), ev-03 (line 29), ev-06 (lines 40, 155), overview (line 36); Trollskull Manor guide (06-tavern-time lines 31, 69; 08-notable-patrons lines 96 to 101); Bregan D'aerthe Commander ev-01 (lines 160, 326) and design notes (line 37).

**E3. Featured-in list is incomplete.** The page lists **Trollskull Alley** and **Trollskull Manor**. The Bregan D'aerthe Commander mission names her as a reachable Lord (`ev-01-commander.md:160` and `:326`), and the governance page lists the Lords the company can reach (`open-lord-and-masked-lords.md:67`). For the drafter's call.

---

## F. Gaps a Background would need that no source gives

1. **Birth and age.** The wiki's "By the age of 377 winters" (`scratchpad/wiki-trollskull-community/09-ulkoria-stonemarrow.txt:66`) cites the video game `idle`, and no campaign file uses it. Must stay consistent with: she has defended Waterdeep "more times than she can recall" (`sources/adventure-wdh.json:4134`).
2. **Origin, family and clan.** No source. The wiki's "shield dwarven" line (`:66`) gives the ethnicity only. Do not give her a clan or parents without `[research]` or `[design]`.
3. **When she sold the tavern.** No source gives a date. PDF says only "She sold the tavern to go adventuring." (printed p.181). Campaign: "years ago" (page line 29).
4. **Who she sold to, and the Mirthkettle name.** The adventure: "a family of shield dwarves" then "a woman" (`sources/adventure-wdh.json:4135`). The PDF names "Arissa Mirthkettle" (printed p.181 and p.200; check). The campaign does not name her. A Background that names the woman must mark it `[research]`.
5. **Where she lives.** "No one knows where she lives" (`:4134`). The PDF says "believed to be underground" (printed p.200). Must stay consistent with: no one knows her home; she teleports in and out (`:4134`).
6. **Faith.** No source.
7. **The Jarlaxle link (stuffed toys).** Wiki only (`scratchpad/wiki-trollskull-community/09-ulkoria-stonemarrow.txt:69`). The campaign does not use it. Use only with `[research]`.
8. **The 1492 DR visit to the new owners and the Volo review.** Wiki only (`:77`), citing `WDH5e-p42` and the video game `idle`. The new-owner visit is quest-time (the party). The Volo review is not used anywhere in the campaign. Do not put either on a day-one page.
9. **Her Watchful Order rank and status.** The campaign says "senior member" (page line 25; `05-force-grey.md:92`). No source gives a rank title. The wiki says "representative of the Watchful Order" (`:63`).
10. **Her Masked Lord status** (D2). Campaign only; no source.
11. **Her gargoyles and shield guardian.** The wiki says "She did command several animated gargoyles that were used to keep her tavern always clean" (`:69`). The campaign does not use it.

---

## G. Inner-life hints in the sources (exact quotes)

- **Nostalgia for the tavern (voice).** "She's guarding a nostalgia she won't admit, and it shows when she corrects details of the building ("That was a window.")." — `.claude/skills/character-voices/voices/trollskull-community.md:158`
- **Hopes the new owners do well.** "Ulkoria hopes the new owners make something good of it." — `sources/adventure-wdh.json:4135`
- **The hag she will not discuss.** "She will say only that the previous tenant of this property made enemies she considers unresolved. She means the hag. She will not elaborate on the hag." — `sources/Appendix_D_-_Running_the_Tavern.md:1428`
- **The hag, in her own words.** "\"Turned out to be a hag who was cooking and eating the children,\" Ulkoria recalls." — `sources/adventure-wdh.json:4135`
- **Visits and watches.** "Anytime she passes through the North Ward, Ulkoria stops by the tavern for a drink and to check out the place while her shield guardian waits outside." — `sources/adventure-wdh.json:4136`
- **The scowl is not disapproval.** "Permanent scowl that is not, the characters will eventually learn, the same as disapproval." — `sources/Appendix_D_-_Running_the_Tavern.md:1422`
- **Compliments that are criticism.** "Delivers criticism inside compliments so compressed the compliment is nearly invisible." — `sources/Appendix_D_-_Running_the_Tavern.md:1424`
- **Extraordinary endorsement for Lif (Appendix D).** "This is, in Ulkoria's emotional vocabulary, an extraordinary endorsement." — `sources/Appendix_D_-_Running_the_Tavern.md:1430`
- **Grief (campaign).** "and carefully buried grief." — `campaign/setting/notable-figures/trollskull-community/09-ulkoria-stonemarrow.md:13`
- **Never sad in front of others (voice).** "*Never:* She never makes small talk, never apologises, and never lets anyone else see her sad about the tavern." — `.claude/skills/character-voices/voices/trollskull-community.md:161`
- **Approval as absence of criticism (voice).** "Her approval arrives as the absence of criticism, or a single "Good."" — `.claude/skills/character-voices/voices/trollskull-community.md:158`
- **Defends the city without asking (campaign).** "She has defended Waterdeep more times than she can recall and does not require permission to do it again." — `campaign/setting/notable-figures/trollskull-community/09-ulkoria-stonemarrow.md:23`
- **PDF, "like everyone's favorite grandmother"** (conflicts with the voice; D5). "But incredibly friendly and personable; like everyone's favorite grandmother." — PDF page 23, printed p.200. **Check with pdftotext.**
- **Arcane signature worry.** "She is here because the Trollskull is on the same block." — `sources/Appendix_D_-_Running_the_Tavern.md:1429`

---

## Section list for the drafter (per the pass 6 brief)

- Summary: keep. Affiliation label needs a ruling (D3).
- Background: A1 to A4 (origin, the Order, the tavern's sale and its later owners, habits). A5 is wiki-only and needs `[research]`.
- Personal goals: must come from G or be `[design]` (ruling 17). Do not contradict "Ulkoria hopes the new owners make something good of it." (`:4135`).
- Voice: lines 151 to 165. Lines 156, 163 and 164 are quest-time or conflicting (C voice; D1).
- Quest-time sentences to restate or route: C rows 5, 8, 14; voice lines 156, 163, 164; the Masked Lord clause in row 12 (D2).
- Masked Lord: campaign only. The page must keep "never confirmed in her presence" and should carry a flag, since no source gives it (D2).
