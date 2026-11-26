# Pass 6 research notes: Broxley Fairkettle

Page: `campaign/setting/notable-figures/trollskull-community/08-broxley-fairkettle.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR.
Organization page: none. The trollskull-community group has no `campaign/setting/organizations/` page. The Fellowship of Innkeepers is a guild, covered on `campaign/setting/governance-and-guilds/guilds.md` (Broxley's entry at line 44). No Factions Guide page exists for him.
Voice profile: `.claude/skills/character-voices/voices/trollskull-community.md` lines 133 to 147.
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/trollskull-community/01-talisolvanar-fellbranch.md`

## Method and caveats

- Campaign files: Grep and Read. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string (escapes shown as plain quotes). `{@creature ...}` tags are left as written.
- Appendix D: `sources/Appendix_D_-_Running_the_Tavern.md`, markdown.
- Alexandrian PDF: `sources/27. Addendum A Night in Trollskull Manor.pdf` was read with the Read tool's `pages` parameter (the PDF has 38 pages, printed 178 to 215). Every PDF quote below is a transcription from the page image. Each one must be checked with `pdftotext -layout` before it goes into prose. No shell was available. The PDF page and printed page are both given.
- Wiki: the scratchpad extracts `wiki-trollskull-community/08-broxley-fairkettle.txt` and the bundle `sources/research/pass3-bundles/north-ward/wiki.txt`. The extract's citation key is `WDH5e-p41` (Dragon Heist 5e, page 41). The wiki prints no edition on most lines; the `WDH5e` key is the only edition marker.
- `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **The Alexandrian PDF gives Broxley a full origin, and the adventure and Appendix D do not.** The PDF (printed p.199, PDF page 22) says he came to Waterdeep as a refugee, that he worked up from scuttle-boy to owner of a tavern, and that he was elected North Ward representative. The wiki and the campaign say none of this. Quoted in A1 to A3. The PDF is transcribed and needs the pdftotext check.
2. **The feast name conflicts.** The adventure calls it the Deadwinter Day feast (`sources/adventure-wdh.json:30387`). The PDF (printed p.187) says "Leiruin Feast" and marks it "Extrapolate event from DH p. 162." The campaign's `guilds.md:44` follows the adventure. See D2.
3. **Most of the page's quest-time material is in the Trollskull Alley quest and the manor guide, not on the page.** The page's only quest-time wording sits in Overview (L29) and in Relationships (L25 "the hag incident"). See C and E.
4. **The "neighbor who remembers the hag" claim has no source.** No source ties Broxley to the hag or to the tavern's worst days. Relationships line L25 says it. See D5 and F.

---

## A. Background facts by theme

### A1. Origin, arrival in Waterdeep and early life (PDF transcription; not in the adventure or Appendix D)

**Alexandrian PDF, printed p.199 (PDF page 22), Background, bullet 1**
> "Broxley came to Waterdeep as a refugee when he was just a wee young hin. His father and mother had fled Secomber when it was overrun by the Ursahni hobgoblins in the 1470's."
> — `sources/27. Addendum A Night in Trollskull Manor.pdf`, PDF page 22 (printed p.199). "Ursahni" and "Secomber" are as read from the image: **check with pdftotext**.

**Alexandrian PDF, printed p.199, Background, bullet 2**
> "Broxley started as a scuttle-boy for the local taverns. He eventually worked his way up through the kitchens until he finally came to own a tavern of his own, the Barefoot Boards (which is scaled for and caters almost exclusively to halflings)."
> — PDF page 22 (printed p.199). **Check with pdftotext.**

Campaign check: a grep of `campaign/` for "Barefoot Boards", "Secomber" and "Ursahni" returned no match. No campaign file uses these names.

### A2. Trade, rank and how he rose in the Fellowship

**Alexandrian PDF, printed p.199, Background, bullet 3**
> "Broxley often supported other tavern owners in the area (many of whom he had worked with or for over the years), and he was elected as the new North Ward representative of the Fellowship of Innkeepers' a few years back."
> — PDF page 22 (printed p.199). **Check with pdftotext.**

**Alexandrian PDF, printed p.199, Key Info**
> "North Ward representative of the Fellowship of Innkeepers'. (Inns and taverns are few and far between in the North Ward, so he makes frequent visits.)"
> — PDF page 22 (printed p.199).

**Adventure, Sample Guild Representatives (page 41)**
> "Broxley (LG male strongheart halfling {@creature commoner}) is a laid-back, law-abiding halfling with mutton chops and bushy eyebrows. Inns and taverns are few and far between in the North Ward, so he makes frequent visits to the characters' place to see how it's doing and to offer his well-wishes. If none of the characters are members of the guild, he strongly urges them to join \"to avoid further harassment.\" The cost of membership in the Fellowship of Innkeepers is included in the regular expenses outlined in the \"Tavern Keeping Expenses\" sidebar."
> — `sources/adventure-wdh.json:4102`

**Adventure, heading and guild**
> "{@i Fellowship of Innkeepers}"
> — `sources/adventure-wdh.json:4101`

**Appendix D, Broxley (heading and key line)**
> "*Fellowship of Innkeepers — LG male strongheart halfling, Commoner*"
> — `sources/Appendix_D_-_Running_the_Tavern.md:1405`

**Appendix D, roster**
> "| 12 | Broxley Fairkettle *(Fellowship of Innkeepers)* |"
> — `sources/Appendix_D_-_Running_the_Tavern.md:1116`

**Gazetteer, North Ward (Organizations and Characters of Interest)**
> "- **Organizations:** House Gralhund and the Black Network resources in its villa, the Harpers (Ulbrinter Villa), Manshoon's Zhentarim (the Interrogation House), the Fellowship of Innkeepers (represented by Broxley Fairkettle), the City Watch (the station and Endcliff Tower), the Watchful Order (Ulkoria Stonemarrow and Rishaal the Page-Turner in Trollskull Alley) and the Guild of Glassblowers, Glaziers and Spectacle-makers (the House of Crystal)."
> — `campaign/gazetteer/waterdeep/north-ward.md:34`

**Gazetteer, Broxley entry**
> "**Broxley Fairkettle (Lawful Good, Strongheart Halfling, he/him)**"
> "- The Fellowship of Innkeepers representative for the North Ward, a laid-back, law-abiding halfling with mutton chops and bushy eyebrows. He is the father of nine and visits the party's tavern often to wish it well."
> — `campaign/gazetteer/waterdeep/north-ward.md:125` and `:126`

**Wiki, lead and occupation (edition WDH5e-p41)**
> "'''Broxley Fairkettle''' was a [[strongheart halfling]] representative of the [[Fellowship of Innkeepers]] in [[Waterdeep]] in the early 1490s [[DR]].<ref name=\"WDH5e-p41\" />"
> — `scratchpad/wiki-trollskull-community/08-broxley-fairkettle.txt:62`
> "| occupation     = Innkeeper<ref name=\"WDH5e-p41\" />"
> — same file, line 16

### A3. Family

**Adventure, Sample Guild Representatives (page 41)**
> "While lamenting the burdens of being a father of nine, he is quick to point out that the characters' continued compliance with guild rules and regulations makes his rather difficult life \"just a bitty bit easier.\""
> — `sources/adventure-wdh.json:4103`

**Wiki infobox (edition WDH5e-p41)**
> "| children       = nine"
> — `scratchpad/wiki-trollskull-community/08-broxley-fairkettle.txt:32`
> "| spouses        = " (blank) — same file, line 30. "| parents        = " (blank) — line 29. "| siblings       = " (blank) — line 31.

**Appendix D, Roleplaying Keys (page 41)**
> "**Roleplaying Keys:** Rubs his belly when anxious. Names all nine children in order of birth whenever they come up. Genuinely fond of the characters if they treat him with basic decency. Exhausted in a way that is not unfriendly."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1409`

**Alexandrian PDF, printed p.199, Roleplaying Notes**
> "Relates everything back to the lamentable burdens of being a father of nine."
> — PDF page 22 (printed p.199). Check with pdftotext.

No source names his wife, his children or his parents by name. The PDF gives the parents only as "His father and mother" (A1).

### A4. Inner life and the haunted tavern

**Adventure, page 41**
> "Broxley has long believed the tavern to be haunted and is glad to see living souls in it once more."
> — `sources/adventure-wdh.json:4103`

**Alexandrian PDF, printed p.199, Key Info**
> "Has long believed Trollskull Manor to be haunted."
> — PDF page 22 (printed p.199).

### A5. Signature belongings and look

**Appendix D, Appearance (page 41)**
> "**Appearance:** Extravagant mutton chops. Fellowship sash over a waistcoat that has seen better decades. Perpetually slightly damp, as if recently arrived from somewhere inconvenient."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1407`

**Alexandrian PDF, printed p.199, Roleplaying Notes**
> "Scratches his cheek thoughtfully."
> — PDF page 22 (printed p.199). Check with pdftotext.

### A6. Time in post

- Adventure: no date for his election or the start of his term.
- PDF: "a few years back" (A2). No year.
- Wiki: "in the early 1490s [[DR]]" (`scratchpad/wiki-trollskull-community/08-broxley-fairkettle.txt:62`).
- Campaign: no date.

### A7. Other named links on the page or in sources

- No source gives him a god. `campaign/setting/deities/yondalla.md:65` says "none of their pages gives a god, so this page makes none of them a worshiper."
- Fellowship sash (A5).
- Dues and licence money, from the guides and PDF (agenda material, not his life): `campaign/guides/trollskull-manor/02-operating-costs.md:17`: "| Fellowship of Innkeepers | Operating license | 3 gp |".

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Summary: "> - *Strongheart halfling innkeeper, lawful good, he/him*. Stat block: **Commoner**." — `campaign/setting/notable-figures/trollskull-community/08-broxley-fairkettle.md:5`
- Adventure: "Broxley (LG male strongheart halfling {@creature commoner})" — `sources/adventure-wdh.json:4102`
- Appendix D: "*Fellowship of Innkeepers — LG male strongheart halfling, Commoner*" — `sources/Appendix_D_-_Running_the_Tavern.md:1405`
- PDF: "LG male strongheart halfling **commoner** (MM p. 345)" — PDF page 22 (printed p.199), Stats line.
- Wiki: "| alignment5e    = [[Lawful good]]" — `scratchpad/wiki-trollskull-community/08-broxley-fairkettle.txt:57`
- Trollskull Manor guide: "**Broxley Fairkettle** *(Fellowship of Innkeepers, LG male strongheart halfling, Commoner)*" — `campaign/guides/trollskull-manor/08-notable-patrons.md:89`
- All sources agree: lawful good.

**Species**
- Summary: "*Strongheart halfling innkeeper, lawful good, he/him*" (`01` line 5 above, i.e. `08-broxley-fairkettle.md:5`)
- Adventure: "LG male strongheart halfling" (`sources/adventure-wdh.json:4102`)
- Wiki: "| race           = [[Halfling]]" (line 14) and "| ethnicity      = [[Strongheart halfling]]" (line 15) — `scratchpad/wiki-trollskull-community/08-broxley-fairkettle.txt`
- All sources agree: strongheart halfling.

**Pronouns**
- Summary: "he/him" (`08-broxley-fairkettle.md:5`)
- Adventure: "LG male strongheart halfling" (`sources/adventure-wdh.json:4102`)
- Appendix D: "LG male strongheart halfling" (`sources/Appendix_D_-_Running_the_Tavern.md:1405`)
- Wiki: "| sex            = Male" (line 13)
- PDF: "LG male" (PDF page 22, printed p.199)
- North Ward gazetteer Draft Notes: "and `dragon heist` `:4102`, "male" for Broxley" — `campaign/gazetteer/waterdeep/north-ward.md:280`: "The Notable Figures pages for Remallia, Yalah, Broxley, Emmek, Ulkoria and Vincent give alignment and species in the summary line (line 6) but state no pronouns." (That line says the Broxley page states no pronouns; the page's own summary line 5 does say "he/him". See D6.)

**Stat block**
- Summary: "Stat block: **Commoner**." (`08-broxley-fairkettle.md:5`)
- Adventure: "{@creature commoner}" (`sources/adventure-wdh.json:4102`)
- Appendix D: "Commoner" (`sources/Appendix_D_-_Running_the_Tavern.md:1405`)
- PDF: "**commoner** (MM p. 345)" (PDF page 22)
- Wiki: "| class5e        = [[Commoner]]" (line 59)

---

## C. Sentences on the current page that narrate a quest-time event or a day-one conflict

Current page: `campaign/setting/notable-figures/trollskull-community/08-broxley-fairkettle.md`. The page has sections Gamemaster's Summary, Roleplaying Information (Resonance, Emotions, Motivations, Inspirations), Character Information (Persona, Morale, Relationships) and Overview. No Background yet.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L6 | "> - **Affiliation:** Trollskull Alley community" | Label. See D6 | No organization page. See D6 |
| 2 | L7 | "> - **Featured in:** **Trollskull Alley**" | Quest list. Brief ruling 1 | Trollskull Alley: `campaign/quests/act-i/trollskull-alley/ev-01-welcome-to-trollskull-alley.md:92`; `ev-02-the-guild-gauntlet.md:18`; Trollskull Manor guide `campaign/guides/trollskull-manor/06-tavern-time.md:68`. The list is short: see E3 |
| 3 | L11 | "**Resonance.** Broxley should inspire endearment with his fatherly fussing, sympathy with his nine-child domestic chaos, and mild exasperation with his relentless guild membership pitch." | Habit, not an event. Keep (ruling 3). "guild membership pitch" is the same habit as the adventure's "he strongly urges them to join" | `sources/adventure-wdh.json:4102` |
| 4 | L13 | "**Emotions.** Broxley most often feels cheerful resignation, paternal concern, mild anxiety about inspections, uncomplicated happiness at seeing the tavern occupied, earnest civic duty, and exhaustion he insists is contentment." | Borderline. "seeing the tavern occupied" presumes the party's tavern is open. "inspections" is the renovation's guild inspections (ev-02). Drafter decides wording | `campaign/quests/act-i/trollskull-alley/ev-02-the-guild-gauntlet.md:82` (inspections) |
| 5 | L15 | "**Motivations.** Broxley wants to get the tavern into the Fellowship of Innkeepers before anyone else causes trouble with the guild, keep the North Ward hospitable, and survive raising nine children on a halfling's budget." | A goal, not an event. Keep verbatim (ruling 3). "the tavern" is the party's tavern: the Background or restatement can say "the Trollskull" | `campaign/quests/act-i/trollskull-alley/ev-02-the-guild-gauntlet.md:18` |
| 6 | L21 | "**Persona.** To the world, Broxley is a laid-back, law-abiding halfling with mutton chops and bushy eyebrows who visits too often and talks too much about guild membership. ..." | Day-one habit. The adventure line is the same (`sources/adventure-wdh.json:4102`) | — |
| 7 | L21 | "... Deep down, he is terrified that the haunted tavern will bring trouble to the alley, and guild oversight is how he manages that fear." | Day-one belief. "terrified" is campaign wording; the adventure says only "has long believed the tavern to be haunted" (`sources/adventure-wdh.json:4103`) | `sources/adventure-wdh.json:4103` |
| 8 | L23 | "**Morale.** In a fight, Broxley would gather children, lock doors, and send someone for the Watch. He would put himself between a threat and any child present without hesitation." | Day-one. Keep | Voice line 147 corroborates "Somebody fetch the Watch" |
| 9 | L25 | "**Relationships.** Broxley is a representative of the Fellowship of Innkeepers, a father of nine, and a neighbor who remembers the tavern's worst days (the hag incident, the hauntings) and wants to believe its best are ahead." | Day-one in form. "the hag incident" and Broxley's memory of it have **no source** (see D5). "wants to believe its best are ahead" is campaign | Hag: `sources/adventure-wdh.json:4135` (Ulkoria recalls the hag, not Broxley). Hauntings: `sources/adventure-wdh.json:4103` |
| 10 | L29 | "Broxley is the Fellowship of Innkeepers representative for the North Ward — cheerful, civic-minded, and persistent about getting the party's establishment properly registered before something goes wrong with it again." | Quest-time framing ("the party's establishment", "registered"). Route to Trollskull Alley | `campaign/quests/act-i/trollskull-alley/ev-02-the-guild-gauntlet.md:18` and `:64` |

**Voice profile, quest-time clauses (`.claude/skills/character-voices/voices/trollskull-community.md`, lines 133 to 147)**

- Line 145 "*Greeting:* "Oh, hello, hello! Broxley Fairkettle, Fellowship of Innkeepers, and I've brought a wee form, just a small one."" — day-one habit. Keep.
- Line 146 "*Business:* "Membership makes everything just a bitty bit easier, you see, especially with inspections, and with the, well, the ghost."" — borderline: "inspections" refers to the renovation's guild inspections (ev-02). Drafter's call (ruling 16).
- Line 147 "*Under pressure:* "Children, inside, now! Somebody fetch the Watch, please, quickly!"" — day-one. Keep.
- Line 138 "He uses little diminutives: "a bitty bit", "just a wee form"." — day-one.
- Line 139 "*Swearing:* *Never · Euphemist · n/a.* Never, because there are children present, and there are always children present. "Oh, fiddlesticks."" — day-one.

### C2. Where Broxley's quest-time events already live (routed; do not restate on the day-one page)

- **Trollskull Alley, ev-01**: "The party has established what they own and what it will cost them. Broxley Fairkettle contacts them within the day to deliver the permit checklist. Proceed to **The Guild Gauntlet** Event." — `campaign/quests/act-i/trollskull-alley/ev-01-welcome-to-trollskull-alley.md:92` (blockquote)
- **Trollskull Alley, ev-02 (The Guild Gauntlet)**: "**Broxley Fairkettle** (Fellowship of Innkeepers) arrives within a day of the party's arrival, permit checklist in hand and apologetic expression already deployed. **Hammond Kraddoc** (Vintners', Distillers', and Brewers' Guild) appears uninvited alongside him, with his scribe Jinny and a second list." — `campaign/quests/act-i/trollskull-alley/ev-02-the-guild-gauntlet.md:18`
- **Trollskull Alley, ev-02**: "Cross-ref the **Broxley Fairkettle** and **Hammond Kraddoc** pages in Notable Figures." — `ev-02-the-guild-gauntlet.md:64`
- **Trollskull Alley, ev-02**: "Broxley Fairkettle and Hammond Kraddoc arrived on the same morning with two different checklists and the same expectation: that the party would visit six guilds, pass six inspections, and pay the associated fees before a single drink could be legally served." — `ev-02-the-guild-gauntlet.md:78`
- **Trollskull Alley, ev-02, checklist**: "The permit checklist has seven items. The guild fees are due on inspection, not on completion. The Carpenters' foreman wants eighteen days and an extra twenty gold. The butcher wants a tip he is not owed. The Watchful Order's inspector wants to know if your poltergeist has a safety certification. Broxley Fairkettle keeps apologizing. Hammond Kraddoc keeps making notes." — `ev-02-the-guild-gauntlet.md:82`
- **Trollskull Alley overview**: "- **Broxley Fairkettle** (Fellowship of Innkeepers) — delivers the permit checklist; first city bureaucrat the party navigates" — `campaign/quests/act-i/trollskull-alley/overview.md:27`
- **Trollskull Alley design notes, ev-02 guild entries**: "`ev-02-the-guild-gauntlet.md` lines 19-37 and 41-57: the checklist, Emmek's penalty and the Watchful Order inspection." — `campaign/setting/governance-and-guilds/guilds.md:84` (a source line that points to ev-02)
- **Gazetteer, North Ward, Politics**: "- The Fellowship of Innkeepers presses the party for membership through Broxley Fairkettle." — `campaign/gazetteer/waterdeep/north-ward.md:185`
- **Gazetteer, North Ward, Draft Notes (Left out / Conflicts)**: "- **Conflicts:** Inns and taverns. Dragon Heist has Broxley say they are "few and far between in the North Ward" (`:4102`), while the wiki lists ten inns and taverns plus the Gentle Mermaid and two more gambling dens (`north-ward/wiki.txt:112-130`). The page records both." — `campaign/gazetteer/waterdeep/north-ward.md:275`
- **Trollskull Manor guide, Patron table**: "| 12 | Broxley Fairkettle *(Fellowship of Innkeepers)* |" — `campaign/guides/trollskull-manor/06-tavern-time.md:68`
- **Trollskull Manor guide, Tavern time, Kythorn row**: "| Kythorn 1–10 | Broxley Fairkettle, Tally Fellbranch, Laraelra "Elra" Harsard with Lord Torlyn Wands (Renaer's Friends) | 14: a Masked Lord visits (at Fame 81+); otherwise 17: a socialite demands the best table | Guild season. The night measures where the tavern stands with the city's upper floors. |" — `campaign/guides/trollskull-manor/06-tavern-time.md:32`
- **Trollskull Manor guide, Notable Patrons**: "- News: Volo's Guide is being updated; there's a researcher asking about notable establishments; Broxley suggested the Trollskull" — `campaign/guides/trollskull-manor/08-notable-patrons.md:94`
- **Trollskull Manor guide, Notable Patrons**: "- Invites the party to the Fellowship's annual member dinner; the food will be mediocre; he likes them and doesn't invite everyone" — `campaign/guides/trollskull-manor/08-notable-patrons.md:93`
- **Trollskull Manor guide, Notable Patrons**: "- One of his other member establishments is being pressured by someone unidentified — strange guild filings, a permit application that shouldn't exist" — `campaign/guides/trollskull-manor/08-notable-patrons.md:92`
- **Trollskull Manor guide, Operating costs**: "| Fellowship of Innkeepers | Operating license | 3 gp |" — `campaign/guides/trollskull-manor/02-operating-costs.md:17`
- **Lords' Alliance ev-01 (the licence cut)**: "- **The licence cut:** the manor guide lowers the Fellowship of Innkeepers line from 3 gp to 1 gp a tenday while the party holds Alliance standing. This is passive and needs no scene, and any Watch citation against the manor resets it." — `campaign/quests/faction-events/lords-alliance/00-first-meeting/ev-01-first-meeting.md:260`
- **Trollskull Manor guide, Tavern time, Tenday row**: "| 12 | Broxley Fairkettle *(Fellowship of Innkeepers)* |" (row 12 of the patron table, `06-tavern-time.md:68`, as above).
- **Guilds page, Broxley entry**: "The published adventure has him ask the party to host the Deadwinter Day feast, which the Fellowship arranges with the Bakers', Butchers' and Vintners' guilds." — `campaign/setting/governance-and-guilds/guilds.md:44`. This is a campaign statement, but the adventure supports it (D2).
- **Adventure, Deadwinter Day Feast (page 162)**: "The Fellowship of Innkeepers—in conjunction with the Bakers' Guild, the Guild of Butchers, and the Vintners', Distillers', and Brewers' Guild—decides to hold a Deadwinter Day feast for the residents of Trollskull Alley. Broxley Fairkettle (see \"Sample Guild Representatives\"), asks the characters if they would be willing to host the feast in their tavern." — `sources/adventure-wdh.json:30387`
- **Alexandrian PDF, printed p.187 (PDF page 10), topics**: "Asks the PCs to host the guild's Leiruin Feast. (Extrapolate event from DH p. 162.)" — PDF page 10 (**check with pdftotext**; see D2).
- **Alexandrian PDF, printed p.187, topics**: "Offers to sell them a signatory license to the Fellowship of Innkeepers' indemnification insurance for 20 gp per month: It covers the costs of any lawsuits held against them or their tavern due to injuries incurred during a stay. (He relates how the previous year a spice merchant nearly bankrupted an inn who didn't have insurance when a magister held them liable for not only the magical healing of his injuries, but also for his lost wages during a period of physical and emotional recovery.)" — PDF page 10. **Check with pdftotext.**
- **Alexandrian PDF, printed p.187, topics**: "Dues for the Fellowship of Innkeepers are increasing by 5 gp per month starting on the first of next month." — PDF page 10.
- **Alexandrian PDF, printed p.182 (PDF page 5), Guild visits**: "SUPPLIERS (BRIBES): Fellowship of Innkeepers (Broxley Fairkettle, p. 41) 25-100 gp" — PDF page 5. **Check with pdftotext.**
- **Appendix D, Broxley topics (page 41)**: "1. Stops by with an inspection form that is completely in order, which he knows and they know, and he simply wanted an excuse to see how the place is doing. He is pleased. He does not say this. He says: "It's adequate." He tips generously." / "2. Has a problem: one of his other member establishments is being pressured by someone he can't identify — strange guild filings, a permit application that shouldn't exist. He wants to know if the characters know anything about unusual pressure campaigns in the North Ward. He is fishing, but he is also genuinely worried." / "3. Is here to invite the characters to the Fellowship's annual member dinner. It is a dull event. The food will be mediocre (the catering contract is a legacy arrangement). He is inviting them because he likes them and he doesn't invite everyone." / "4. Has news: *Volo's Guide to Waterdeep* is being updated. There is a researcher asking around about notable establishments. Broxley has suggested the Trollskull. This is not something he had to do. He has done it." — `sources/Appendix_D_-_Running_the_Tavern.md:1412` to `:1415`

---

## D. Conflicts

**D1. Pronoun: none.** Every source says male: `sources/adventure-wdh.json:4102` ("LG male strongheart halfling"); `sources/Appendix_D_-_Running_the_Tavern.md:1405` ("LG male strongheart halfling"); wiki line 13 ("| sex            = Male"); PDF page 22 ("LG male"). Summary line 5 says "he/him".

**D2. Feast name and feast host.**
- Adventure: "The Fellowship of Innkeepers—in conjunction with the Bakers' Guild, the Guild of Butchers, and the Vintners', Distillers', and Brewers' Guild—decides to hold a Deadwinter Day feast for the residents of Trollskull Alley." — `sources/adventure-wdh.json:30387`
- Alexandrian PDF (printed p.187, PDF page 10; **check with pdftotext**): "Asks the PCs to host the guild's Leiruin Feast. (Extrapolate event from DH p. 162.)"
- Campaign: "The published adventure has him ask the party to host the Deadwinter Day feast, which the Fellowship arranges with the Bakers', Butchers' and Vintners' guilds." — `campaign/setting/governance-and-guilds/guilds.md:44`
- Higher ranked: the adventure (Deadwinter Day, `:30387`). The PDF's "Leiruin" is an Alexandrian extrapolation that names a different festival; Leiruin falls on Tarsakh 10 (`campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:81`). Quote: "| Tarsakh 1 to 10 | Waukeentide | ... Leiruin on Tarsakh 10 (guild dues paid and charters renewed with the Lords). |". The drafter should name Deadwinter Day.

**D3. The North Ward has few inns (Broxley's line) versus the wiki's list.**
- Adventure: "Inns and taverns are few and far between in the North Ward" — `sources/adventure-wdh.json:4102`
- Campaign, already recorded: "Dragon Heist has Broxley say they are "few and far between in the North Ward" (`:4102`), while the wiki lists ten inns and taverns plus the Gentle Mermaid and two more gambling dens (`north-ward/wiki.txt:112-130`)." — `campaign/gazetteer/waterdeep/north-ward.md:275`
- Higher ranked: the adventure. The gazetteer records both.

**D4. "Frequent visits" versus "often" in the campaign.** No conflict. Adventure: "he makes frequent visits" (`sources/adventure-wdh.json:4102`); PDF: "so he makes frequent visits" (printed p.199); campaign: "visits too often" (`08-broxley-fairkettle.md:21`).

**D5. The hag and Broxley.**
- Campaign: "a neighbor who remembers the tavern's worst days (the hag incident, the hauntings)" — `08-broxley-fairkettle.md:25`
- Adventure: the hag is recalled only by Ulkoria: "\"Turned out to be a hag who was cooking and eating the children,\" Ulkoria recalls." — `sources/adventure-wdh.json:4135`
- Alexandrian PDF: "The woman, Arissa Mirthkettle, turned out to be a hag who was cooking and eating the children." (printed p.200, Ulkoria's profile; not Broxley's.)
- No source links Broxley to the hag. **Unsourced.** The drafter must not write it as a fact without `[research]` or a `[design]` tag under ruling 17.
- Also, `campaign/setting/deities/baba-yaga.md:63` says "The campaign repeats the hag in `campaign/guides/trollskull-manor/08-notable-patrons.md:99`, `campaign/setting/notable-figures/trollskull-community/08-broxley-fairkettle.md:26` and `campaign/setting/notable-figures/trollskull-community/11-lif.md:22`." Line 26 of this page is blank. The hag line is at line 25. See E2.

**D6. Affiliation label.**
- Page summary: "> - **Affiliation:** Trollskull Alley community" — `08-broxley-fairkettle.md:6`
- Trollskull Alley overview: "- **Broxley Fairkettle** (Fellowship of Innkeepers) — delivers the permit checklist" — `campaign/quests/act-i/trollskull-alley/overview.md:27` (quest summary; brief ruling 6 says it does not govern)
- Guilds page: "**Broxley Fairkettle** (Lawful Good, Strongheart Halfling, he/him) is the Fellowship of Innkeepers representative for the North Ward and a father of nine." — `campaign/setting/governance-and-guilds/guilds.md:44`
- No organization page covers the Fellowship. The page's label "Trollskull Alley community" is the group label used on all five of the trollskull-community pages. Drafter's call under ruling 6; report only.

**D7. Pronoun statement on the gazetteer.** `campaign/gazetteer/waterdeep/north-ward.md:280` says the Notable Figures pages "state no pronouns." The Broxley page does state "he/him" in its summary line (`08-broxley-fairkettle.md:5`). The gazetteer line is stale for this page.

**D8. Voice tagline and alignment.** No conflict.

**D9. PDF "wee young hin".** The PDF's "hin" (a halfling's word for a child) is as read. Check with pdftotext.

---

## E. Stale lines in other files (not edited) and routed quest references

**E1. Stale or conflicting lines**
- `campaign/baba-yaga` line: `campaign/setting/deities/baba-yaga.md:63` cites `campaign/setting/notable-figures/trollskull-community/08-broxley-fairkettle.md:26` for the hag. Line 26 of the page is blank. The hag text is at line 25. Stale citation.
- `campaign/gazetteer/waterdeep/north-ward.md:280`: "The Notable Figures pages for Remallia, Yalah, Broxley, Emmek, Ulkoria and Vincent give alignment and species in the summary line (line 6) but state no pronouns." — stale for Broxley (the summary is line 5 and carries "he/him"). Quote and location exact.
- `campaign/setting/governance-and-guilds/guilds.md:44`: "The published adventure has him ask the party to host the Deadwinter Day feast" — supported by `sources/adventure-wdh.json:30387`. Not stale.

**E2. Routed quest references (quest-time facts)**: see C2 for the full list. In short: Trollskull Alley ev-01 (line 92), ev-02 (lines 18, 64, 78, 82), overview (line 27), guild rows in the manor guide (06-tavern-time lines 32 and 68; 08-notable-patrons lines 89 to 94; 02-operating-costs line 17), Lords' Alliance ev-01 line 260.

**E3. Featured-in list is incomplete.** The page lists only **Trollskull Alley**. Broxley also appears in the Trollskull Manor guide (`06-tavern-time.md:32` and `:68`, `08-notable-patrons.md:89`) and in the gazetteer (`north-ward.md:125`). This is for the drafter's call.

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in Draft Notes.

1. **Birth and age.** No source. Wiki `age` and `dob` are blank (`scratchpad/wiki-trollskull-community/08-broxley-fairkettle.txt:17`, `:21`). Must stay consistent with: he is a grown father of nine (`sources/adventure-wdh.json:4103`).
2. **Where he was born.** The PDF says he came to Waterdeep as a refugee (A1). The birthplace is not given. Must stay consistent with: a refugee child from Secomber (PDF, `[check]`).
3. **Secomber and the Ursahni hobgoblins.** PDF only (printed p.199). No campaign file uses them. Use with `[research]` tag or check the PDF first.
4. **The Barefoot Boards.** PDF only. The campaign never names it. The PDF says it "is scaled for and caters almost exclusively to halflings." Use with `[research]`.
5. **When he was elected North Ward representative.** The PDF says "a few years back" (A2). No year. Campaign: no date.
6. **Wife and children's names.** No source. Adventure and Appendix D give "nine" and Appendix D says "Names all nine children in order of birth whenever they come up." — but names no child (`sources/Appendix_D_-_Running_the_Tavern.md:1409`). Must stay consistent with: nine children, named in birth order by him (a habit, not a list).
7. **Faith.** No source. `campaign/setting/deities/yondalla.md:65` says none of the halfling Notable Figures gives a god. Do not give him a deity.
8. **Friends and neighbors.** Sources name none, except the Fellowship's other representatives and the tavern owners he supported (PDF, printed p.199: "many of whom he had worked with or for over the years"). Unnamed.
9. **Whether he owns a tavern in Waterdeep today.** PDF: "until he finally came to own a tavern of his own, the Barefoot Boards" — past tense, not stated as current. Open.
10. **The hag and his memory of the tavern's worst days.** No source (D5).

---

## G. Inner-life hints in the sources (exact quotes)

These are the sourced hints a Background or the personal goals may use. They must not be contradicted.

- **Nine children, named in birth order.** "Names all nine children in order of birth whenever they come up." — `sources/Appendix_D_-_Running_the_Tavern.md:1409`
- **Nine children, a burden he says he wants eased.** "While lamenting the burdens of being a father of nine, he is quick to point out that the characters' continued compliance with guild rules and regulations makes his rather difficult life \"just a bitty bit easier.\"" — `sources/adventure-wdh.json:4103`
- **Refugee origin (PDF, check).** "Broxley came to Waterdeep as a refugee when he was just a wee young hin." — PDF page 22 (printed p.199).
- **Haunted tavern.** "Broxley has long believed the tavern to be haunted and is glad to see living souls in it once more." — `sources/adventure-wdh.json:4103`
- **Rubs his belly when anxious.** "Rubs his belly when anxious." — `sources/Appendix_D_-_Running_the_Tavern.md:1409`
- **Fond of those who treat him decently.** "Genuinely fond of the characters if they treat him with basic decency." — `sources/Appendix_D_-_Running_the_Tavern.md:1409`
- **Likes the people he invites.** "He is inviting them because he likes them and he doesn't invite everyone." — `sources/Appendix_D_-_Running_the_Tavern.md:1414`
- **Pleased and does not say so.** "He is pleased. He does not say this. He says: "It's adequate."" — `sources/Appendix_D_-_Running_the_Tavern.md:1412`
- **Worried about pressure on a member establishment.** "He is fishing, but he is also genuinely worried." — `sources/Appendix_D_-_Running_the_Tavern.md:1413`
- **Fear of the haunting (campaign).** "Deep down, he is terrified that the haunted tavern will bring trouble to the alley, and guild oversight is how he manages that fear." — `campaign/setting/notable-figures/trollskull-community/08-broxley-fairkettle.md:21`
- **Exhaustion he calls contentment (campaign).** "exhaustion he insists is contentment." — `campaign/setting/notable-figures/trollskull-community/08-broxley-fairkettle.md:13`
- **Fellowship sash and a tired look.** "Fellowship sash over a waistcoat that has seen better decades. Perpetually slightly damp, as if recently arrived from somewhere inconvenient." — `sources/Appendix_D_-_Running_the_Tavern.md:1407`
- **Exhausted, not unfriendly.** "Exhausted in a way that is not unfriendly." — `sources/Appendix_D_-_Running_the_Tavern.md:1409`
- **Voice.** "*A cheerful, fussing halfling father of nine who cannot stop pitching guild membership.*" — `.claude/skills/character-voices/voices/trollskull-community.md:134`
- **Voice, fatherly protection.** "*Under pressure:* "Children, inside, now! Somebody fetch the Watch, please, quickly!"" — `.claude/skills/character-voices/voices/trollskull-community.md:147`
- **Voice, never threatens or leaves a child in danger.** "*Never:* He never threatens, never breaks a rule, and never leaves a child in danger." — `.claude/skills/character-voices/voices/trollskull-community.md:143`

---

## Section list for the drafter (per the pass 6 brief)

- Summary: keep. Add one Fellowship bullet if the drafter wants a Factions/Guilds line (none exists for him).
- Background: A1 to A3 (PDF origin, rank) with `[check]`; the nine children (A3); the haunting belief (A4). Personal goals: must come from G or `[design]` (ruling 17).
- Voice: lines 133 to 147 of the profile. Line 146 "inspections" is borderline (C, voice).
- Quest-time sentences to restate or route: C rows 4, 5, 9 (hag), 10; voice line 146.
