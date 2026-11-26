# Pass 6 research notes: Hammond Kraddoc

Page: `campaign/setting/notable-figures/trollskull-community/07-hammond-kraddoc.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 19; user rulings Session 53)
Method: Grep and Read only. Quotes are copied from tool output. Line numbers are file lines unless marked "dump line" (wiki XML) or "extract line" (scratchpad wiki extract). For the Hammond wiki page, dump line = extract line + 4020583 (checked at extract lines 57, 65, 68 and 71 = dump lines 4020640, 4020648, 4020651 and 4020654). JSON escapes are shown as plain quotes. `{@creature ...}` tags are left as written.
Organization page: none. The Vintners', Distillers', and Brewers' Guild has no organization page. Its governance entry is in `campaign/setting/governance-and-guilds/guilds.md` (see D1).
Factions Guide: none. Villains page: none.
Voice profile: `.claude/skills/character-voices/voices/trollskull-community.md` lines 115 to 129 ("### Hammond Kraddoc").
Wiki: the extract `scratchpad/wiki-trollskull-community/07-hammond-kraddoc.txt` is the full page (not a stub). The same page is in the full dump at XML lines 4020566 to 4020660 (title "Hammond Kraddoc", line 4020568).
PDF: `sources/27. Addendum A Night in Trollskull Manor.pdf` was read with the Read tool's `pages` parameter. PDF page 10 is printed p.187. The **HAMMOND KRADDOC (Vintners')** bullets are on PDF page 10. These PDF quotes are transcriptions from the image. Check each with `pdftotext -layout` before it goes into prose. No shell was available.

## Findings that change how the page is written

1. **The father is sourced only by the Alexandrian PDF.** "Discovers that Lif knew his father, Barbaros Kraddoc." (PDF page 10, printed p.187). No campaign or adventure file names him (grep of the whole repo and `sources/` found no other "Barbaros"). This is the only family fact in any source.
2. **The adventure gives the day-one character and the Jinny relationship.** "Hammond (N male Illuskan human commoner) doesn't like adventurers, but he likes their coin." and "always seen in the company of a young scribe, Jinny (NG female tiefling commoner)" (`sources/adventure-wdh.json:4113`).
3. **The Kraddoc correspondence in Kalain's Tower has two directions.** Fireball! ev-07 says letters "to Hammond Kraddoc ... confirming large bribes paid" (no payer named). Act III Arc D says "confirming that Kraddoc paid Lord Dagult large bribes" (see D2). The page does not use either; both are quest-time.
4. **The affiliation label conflicts with the governance page.** The page says "Trollskull Alley community" (line 6). `guilds.md:46` says he "represents the Vintners', Distillers', and Brewers' Guild" (see D1).

---

## A. Background facts by theme

### A1. Origin, ethnicity and family

**Adventure, Vintners' Guild entry (page 41; heading at `sources/adventure-wdh.json:4108`)**
> "{@i Vintners', Distillers', and Brewers' Guild}"
> "Hammond (N male Illuskan human {@creature commoner}) doesn't like adventurers, but he likes their coin. This effete, well-dressed man is always seen in the company of a young scribe, Jinny (NG female tiefling commoner), who wears spectacles and silently records notes and conversations in a small book as Hammond speaks."
> — `sources/adventure-wdh.json:4112` and `:4113`

**Adventure, the guild's visits (the trigger is the reopening)**
> "Once it becomes known around the city that the tavern in Trollskull Alley is planning to reopen its doors to the public, the adventurers receive visits from guild representatives interested in the tavern's welfare. This section describes a handful of these representatives."
> — `sources/adventure-wdh.json:4094` (heading "Sample Guild Representatives", `:4090`, page 41)

**Adventure, the guild's supply role**
> "Meat must come from the Guild of Butchers; ale and wine from the Vintners', Distillers', and Brewers' Guild; and bread and pastries from the Bakers' Guild. The list goes on."
> — `sources/adventure-wdh.json:4086`

**Wiki, "Hammond Kraddoc" (extract lines 5 to 16; dump lines 4020588 to 4020599 for the infobox, same offset)**
> "| home           = [[Waterdeep]], [[Sword Coast North]]" (extract line 11)
> "| sex            = Male" (extract line 13)
> "| race           = [[Human]]" (extract line 14)
> "| ethnicity      = [[Illuskan]]" (extract line 15)
> "| occupation     = Brewer<ref name="WDH5e-p41" />" (extract line 16)

**Wiki, lead (extract line 62; dump line 4020645; `WDH5e-p41`)**
> "'''Hammond Kraddoc''' was a representative of the [[Vintners', Distillers', & Brewers' Guild|Vintners', Distillers' and Brewers' Guild]] in [[Waterdeep]] in the early 1490s [[DR]].<ref name="WDH5e-p41" />"

**Wiki, History (extract line 65; dump line 4020648; `WDH5e-p41`)**
> "In [[1492 DR]],{{WDH-time}} Hammond possibly went into business with the new owners of the [[Trollskull Manor]].<ref name="WDH5e-p41">{{Cite book/Waterdeep: Dragon Heist|41}}</ref>"
(Edition: 5e, Dragon Heist p.41. The line describes a 1492 DR business with "new owners" of the manor. That is a quest-time relationship; see C7 and D3.)

**Wiki, Personality (extract line 68; dump line 4020651)**
> "Hammond disliked adventurers but liked their coin. He liked arriving in the middle of the month to talk about all the new spirits produced by the guild. He also chastised tavern owners for their current selection of beverages, even if he'd previously sold them those goods, in order to test their willingness to cooperate."

**Wiki, Relationship (extract line 71; dump line 4020654)**
> "Hammond had always at his side [[Jinny]], a [[tiefling]] scribe who silently recorded notes and conversations."

**PDF, HAMMOND KRADDOC (Vintners'), printed p.187 (PDF page 10; transcription, check with pdftotext)**
> "Discovers that Lif knew his father, Barbaros Kraddoc. Barbaros would actually stay at Trollskull Manor when he would come into Waterdeep to sell wines from the Elysium Fields. (Lif is saddened to learn that the Elysium Fields were destroyed.)"
> — `sources/27. Addendum A Night in Trollskull Manor.pdf`, PDF page 10
(The first clause is a patron topic and is tavern-time. The fact of the father is not dated. Lif's solitary minding is dated "since 1479 DR" (`campaign/gazetteer/waterdeep/north-ward.md:63`); the PDF does not date Barbaros's stays. See F.)

**Gazetteer, Lif (the tavern's last barkeeper)**
> "- The tavern has been closed for years, and the poltergeist **Lif** haunts it. He is the spirit of the last barkeeper, a dwarf, and has minded the building alone since 1479 DR."
> — `campaign/gazetteer/waterdeep/north-ward.md:63`

### A2. Trade, the guild and its role

**Governance page, The Guilds (`campaign/setting/governance-and-guilds/guilds.md:46`)**
> "**Hammond Kraddoc** (Neutral, Illuskan Human, he/him) represents the Vintners', Distillers', and Brewers' Guild and wants to keep its hold on the North Ward's spirit trade. He arrives with his scribe Jinny, a young tiefling, to inspect the party's tavern, and he keeps visiting after the inspections end because he has nobody else to drink with."

**Governance page, Jinny has no page (`guilds.md:121`)**
> "Names with no page: Mareva Coile, Berna, Herath, Delvon Harsk, Pirn, Piers Hobb, Sembra Vashir, Pynt Oomtrowl, Jarbokken Frostbeard, Justyn Rassk, Morana Huldark, Esvele Rosznar and Jinny are plain text and appear only in event pages or the adventure."

**Adventure, the beverage visit (4114)**
> "Hammond likes to stop by in the middle of the month to inform the characters of new spirits that the guild has to offer, and to give them a list of which ones to push hard. To test the extent of their willingness to cooperate, he chastises them for their current selection of beverages, even if he previously sold them those goods."
> — `sources/adventure-wdh.json:4114`

**Appendix D, Hammond's featured spirit (Fashionable tier, `sources/Appendix_D_-_Running_the_Tavern.md:741`)**
> "| Fashionable | 81–150 | 35–40 | 62–80 gp | At or near capacity most nights; Hammond Kraddoc's featured spirits worth stocking |"

**Trollskull Manor cellar (location, tavern stock; `campaign/locations/trollskull-manor/tm03-cellar.md:13`)**
> "**Storage function.** After opening, the cellar holds tavern stock: wine casks, ale casks (Hammond Kraddoc's guild-recommended selections in pride of place), preserved goods from the Guild of Butchers and Bakers' Guild suppliers."

### A3. Temperament, habits and manner

**Appendix D, Appearance and Roleplaying Keys (1392, 1394)**
> "**Appearance:** Always dressed as if attending a formal dinner, at all hours. His scribe Jinny (NG female tiefling, Commoner) is always with him, always recording, never introduced."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1392`
> "**Roleplaying Keys:** Sighs at ale. Brightens at good spirits. Measures the quality of a room by what the bar stocks. Does not make small talk; makes assessments."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1394`

**Trollskull Manor guide, Guild Figures (`08-notable-patrons.md:82` to `:83`)**
> "**Hammond Kraddoc** *(Vintners' Guild, N male Illuskan human, Commoner)*"
> "Always dressed for a formal dinner; his scribe Jinny (always present, always recording, never introduced) sighs at ale, brightens at good spirits."

**Voice profile (`trollskull-community.md`)**
> "*A fussy, self-important guild inspector who condescends about your spirits and is secretly lonely for company.*" (line 116)
> "- **Personality in speech:** Self-importance over loneliness. His criticism is really an attempt to be part of the conversation. The rare social visit is framed as an \"unscheduled inspection\". When he genuinely approves, he gives it grudgingly, in a single sentence." (line 122)
> "- **Never:** He never admits he visits for company, never praises lavishly, and never risks his skin for anyone." (line 125)

### A4. Relationships to other named figures

**Emmek Frewn (the rival pub; no source ties Hammond to Emmek beyond the inspections in ev-02)**
> "**Hammond Kraddoc** appears at the Vintners' Guild inspection, chastises the party's current beverage selection, and suggests two specific guild products "the guild is emphasizing this tenday." Buying both reduces the first month's supply rate by 5 gp. He will never acknowledge this as a social visit." — `campaign/quests/act-i/trollskull-alley/ev-02-the-guild-gauntlet.md:62`
> "Broxley Fairkettle and Hammond Kraddoc arrived on the same morning with two different checklists and the same expectation: that the party would visit six guilds, pass six inspections, and pay the associated fees before a single drink could be legally served. Emmek Frewn had already spoken to two of those inspectors." — `campaign/quests/act-i/trollskull-alley/ev-02-the-guild-gauntlet.md:78`

**Broxley Fairkettle (the other guild representative)**
> "**Broxley Fairkettle** (Fellowship of Innkeepers) arrives within a day of the party's arrival, permit checklist in hand and apologetic expression already deployed. **Hammond Kraddoc** (Vintners' Guild) appears uninvited alongside him, with his scribe Jinny and a second list. Between them, the party has the full picture:" — `campaign/quests/act-i/trollskull-alley/ev-02-the-guild-gauntlet.md:18`

**Neverember (Kalain's Tower; Fireball! ev-07; quest-time; routed)**
> "**2. Kraddoc correspondence.** Letters to Hammond Kraddoc of the Vintners', Distillers', and Brewers' Guild confirming large bribes paid to cover a contaminated-liquor scandal in the Dock Ward. Neverember's private leverage over the Guild. Not directly relevant to the Stone but potentially useful for a party building political assets." — `campaign/quests/act-ii/fireball/ev-07-kalainsalley-tower.md:55`
> "- **Neverember and the Vintners':** In Kalain's Tower the party finds letters to Hammond Kraddoc that confirm large bribes paid to cover a contaminated-liquor scandal in the Dock Ward. They are Neverember's private leverage over the Vintners', Distillers', and Brewers' Guild (campaign-only)." — `campaign/setting/governance-and-guilds/guilds.md:66`

### A5. Time in post

- The wiki gives "in the early 1490s DR" for the representative post (extract line 62; dump line 4020645). No start year.
- No source gives when Hammond took the guild post, his age, or where he was before Waterdeep. See F.

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Summary (page line 5): "> - *Illuskan human guild representative, neutral, he/him*. Stat block: **Commoner**." — `campaign/setting/notable-figures/trollskull-community/07-hammond-kraddoc.md:5`
- Adventure: "Hammond (N male Illuskan human {@creature commoner})" (`sources/adventure-wdh.json:4113`).
- Appendix D: "*Vintners', Distillers', and Brewers' Guild — N male Illuskan human, Commoner*" (`sources/Appendix_D_-_Running_the_Tavern.md:1390`).
- Governance page: "(Neutral, Illuskan Human, he/him)" (`guilds.md:46`).
- Wiki: "| alignment5e    = [[Neutral]]" (extract line 57; dump line 4020640).
- All sources agree: neutral.

**Species and ethnicity**
- Summary: "Illuskan human" (page line 5).
- Adventure: "N male Illuskan human" (`sources/adventure-wdh.json:4113`).
- Wiki: "| race           = [[Human]]" (extract line 14); "| ethnicity      = [[Illuskan]]" (extract line 15).
- Governance page: "Illuskan Human" (`guilds.md:46`).
- All sources agree: Illuskan human.

**Pronouns**
- Summary (page line 5): "he/him".
- Adventure: "N male Illuskan human" (`sources/adventure-wdh.json:4113`); "This effete, well-dressed man" (same line).
- Appendix D: "N male Illuskan human" (`:1390`).
- Governance page: "he/him" (`guilds.md:46`).
- Wiki: "| sex            = Male" (extract line 13).
- All sources agree: he/him.

**Stat block**
- Summary: "Stat block: **Commoner**." (page line 5).
- Adventure: "{@creature commoner}" (`sources/adventure-wdh.json:4113`).
- Appendix D: "Commoner" (`:1390`).
- Wiki: "| class5e        = [[Commoner]]" (extract line 59).
- All sources agree: Commoner.

**Occupation (wiki conflict within the wiki; see D1)**
- Wiki infobox: "| occupation     = Brewer<ref name="WDH5e-p41" />" (extract line 16).
- Wiki lead: "was a representative of the [[Vintners', Distillers', & Brewers' Guild|...]]" (extract line 62).
- Adventure: "representative" is not used; the adventure gives "(Vintners' Guild)" (`sources/adventure-wdh.json:4112`).

---

## C. Sentences on the current page (and the voice profile) that narrate a quest-time event or a day-one conflict

Current page: `campaign/setting/notable-figures/trollskull-community/07-hammond-kraddoc.md`. Sections: Gamemaster's Summary, Roleplaying Information, Character Information, Overview. No Background yet.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| C1 | 7 | "> - **Featured in:** **Trollskull Alley**, **Fireball!**, **Trollskull Manor**" | Quest list. Route (ruling 1) | Trollskull Alley: `campaign/quests/act-i/trollskull-alley/ev-02-the-guild-gauntlet.md:18` and `:62`. Fireball!: `campaign/quests/act-ii/fireball/ev-07-kalainsalley-tower.md:55`. Trollskull Manor: `campaign/guides/trollskull-manor/06-tavern-time.md:30` and `:67` |
| C2 | 15 (Motivations) | "**Motivations.** Kraddoc wants to maintain the Vintners', Distillers', and Brewers' Guild's grip on the North Ward spirit trade, prove that he knows more about drink than anyone the party employs, and visit socially without admitting that is what he is doing." | "than anyone the party employs" presumes the party runs a staffed tavern, which is tavern-time (the manor is closed on Ches 1, `north-ward.md:63`; it opens on Ches 20, `campaign/guides/gm-guide/structural-rules.md:43`). Flag for the orchestrator (ruling 3) | `campaign/guides/gm-guide/structural-rules.md:43`; `campaign/setting/governance-and-guilds/guilds.md:46` ("to inspect the party's tavern") |
| C3 | 25 (Relationships) | "**Relationships.** Kraddoc is accompanied everywhere by his scribe Jinny (a young tiefling who records everything), a recurring antagonist of Emmek Frewn (whose establishment he also inspects, with less patience), and a representative of the Vintners', Distillers', and Brewers' Guild." | "recurring antagonist of Emmek Frewn" and "whose establishment he also inspects, with less patience" have **no source**. The closest quest-time line is ev-02:78 ("Emmek Frewn had already spoken to two of those inspectors."), which does not name Hammond as Emmek's inspector. Flag (F) | `campaign/quests/act-i/trollskull-alley/ev-02-the-guild-gauntlet.md:78`; `sources/adventure-wdh.json:4113` (Jinny) |
| C4 | 29 (Overview) | "Kraddoc visits the tavern as the Vintners', Distillers', and Brewers' Guild representative, arriving with clipboard, scribe, and opinions about the party's spirits selection — and staying, when no inspection is needed, simply because he has nowhere better to be." | "the party's spirits selection" and "when no inspection is needed" are tavern-time (the inspections are ev-02; the spirit selection is adventure `:4114`, which describes a tavern that has reopened). Restate as a day-one description | `sources/adventure-wdh.json:4114`; `campaign/quests/act-i/trollskull-alley/ev-02-the-guild-gauntlet.md:62` |
| C5 | Voice 120 (Word choice) | "*Word choice:* Guild jargon and connoisseur vocabulary: \"vintage\", \"finish\", \"unacceptable\", \"in accordance with\". He calls the party \"proprietors\", pointedly." | **Quest-time clause.** "the party" as "proprietors" presumes the party owns the tavern. The adventure gives that after Volo's quest: "Following the completion of Volo's quest, the characters gain a home base with an address in Trollskull Alley, in Waterdeep's North Ward." (`sources/adventure-wdh.json:1595`). Drafter restates (ruling 16) | `sources/adventure-wdh.json:1595` |
| C6 | Voice 127 (Greeting) | "*Greeting:* \"Hammond Kraddoc, Vintners', Distillers', and Brewers' Guild. I trust your paperwork is in order. Note that down.\"" | **Quest-time clause.** "your paperwork" is the permit checklist the party receives in ev-02 ("The permit checklist has seven items.", `ev-02-the-guild-gauntlet.md:82`). Drafter restates as a day-one greeting | `campaign/quests/act-i/trollskull-alley/ev-02-the-guild-gauntlet.md:16` and `:82` |
| C7 | Voice 128 (Business) | "*Business:* \"Your house spirit is harsh, overpriced, and served at the wrong temperature. I will have another, for thoroughness.\"" | **Quest-time clause.** "Your house spirit" presumes the party's tavern is open. Day-one restatement needed | `campaign/guides/trollskull-manor/06-tavern-time.md:30` (the visit row) |
| C8 | Voice 129 (Under pressure) | "*Under pressure:* \"I am leaving. The guild will hear of this. Everyone will hear of this!\"" | Not quest-time. Keep | none needed |
| C9 | 23 (Morale) | "In a fight, Kraddoc would leave immediately and file a formal complaint with the guild, the Watch, and any other authority he can reach before the blood dries. He will never risk his life for the tavern." | Day-one. "for the tavern" presumes the tavern. The phrase is a Morale line, keep verbatim (ruling 3). No source for the complaint behaviour (design) | none needed (G) |
| C10 | Voice 121 (Swearing) | "*Swearing:* *Never · Euphemist · n/a.* Never; he's prim. Deeply offended by anyone else's." | Not quest-time. Keep | none needed |

### C2. Where Hammond's quest-time events already live (routed; do not restate on the day-one page)

- **Trollskull Alley, ev-02 (The Permit Checklist)**: "**Hammond Kraddoc** (Vintners' Guild) appears uninvited alongside him, with his scribe Jinny and a second list." — `campaign/quests/act-i/trollskull-alley/ev-02-the-guild-gauntlet.md:18`
- **Trollskull Alley, ev-02 (Other Guild Beats)**: "**Hammond Kraddoc** appears at the Vintners' Guild inspection, chastises the party's current beverage selection, and suggests two specific guild products "the guild is emphasizing this tenday." Buying both reduces the first month's supply rate by 5 gp. He will never acknowledge this as a social visit." — `campaign/quests/act-i/trollskull-alley/ev-02-the-guild-gauntlet.md:62`
- **Trollskull Alley, ev-02 (the checklist's narration)**: "The permit checklist has seven items. The guild fees are due on inspection, not on completion. ... Broxley Fairkettle keeps apologizing. Hammond Kraddoc keeps making notes." — `campaign/quests/act-i/trollskull-alley/ev-02-the-guild-gauntlet.md:82`
- **Trollskull Alley, ev-02 (the same-morning arrival)**: "Broxley Fairkettle and Hammond Kraddoc arrived on the same morning with two different checklists and the same expectation: that the party would visit six guilds, pass six inspections, and pay the associated fees before a single drink could be legally served. Emmek Frewn had already spoken to two of those inspectors." — `campaign/quests/act-i/trollskull-alley/ev-02-the-guild-gauntlet.md:78`
- **Trollskull Alley overview**: "- **Hammond Kraddoc** (Vintners', Distillers', and Brewers' Guild) — arrives uninvited; his scribe Jinny takes notes on everything" — `campaign/quests/act-i/trollskull-alley/overview.md:28`
- **Fireball!, ev-07 (Kalain's Tower letters)**: see A4 (`ev-07-kalainsalley-tower.md:55`).
- **Fireball!, arc-c structure (superseded)**: "- Correspondence with Hammond Kraddoc of the Vintners', Distillers', and Brewers' Guild confirming large bribes paid to cover a contaminated-liquor scandal in the Dock Ward." — `campaign/structure/arc-c-fireball.md:275`
- **Act III Arc D (Lord Dagult's papers)**: "- Correspondence with Hammond Kraddoc of the Vintners', Distillers', and Brewers' Guild confirming that Kraddoc paid Lord Dagult large bribes to cover up a contaminated-liquor scandal in the Dock Ward." — `sources/Act_III_Arc_D.md:596` (see D2)
- **Trollskull Manor guide, Tavern time (first tenday after the party's first lair heist)**: "| First tenday after the party's first lair heist | Faction Contact (slot 17), Jalester Silvermane, Hammond Kraddoc | 8: the Response Team of the faction whose lair was robbed | The robbed faction comes to look at the people who robbed it. |" — `campaign/guides/trollskull-manor/06-tavern-time.md:30`
- **Trollskull Manor guide, Patron table**: "| 11 | Hammond Kraddoc *(Vintners' Guild)* |" — `campaign/guides/trollskull-manor/06-tavern-time.md:67`
- **Trollskull Manor guide, Notable Patrons (Guild Figures, `08-notable-patrons.md:84` to `:87`)**: "- New featured spirit to promote (roll 1d4: blackberry seawine, Berg Brew, Entsap, \"Storm Giant Ale\")" / "- Wants an exclusive supply arrangement; the catch is a reporting obligation on sales figures and regular customers" / "- Competitor sourcing spirits outside guild channels — has not yet reported this; wondering if the party has information" / "- Here purely socially (unusual; Jinny is recording it); orders one good thing, tips exactly the right amount, leaves"
- **Appendix D, Topics & Agendas (1397 to 1400; tavern-time)**: "1. Has a new featured spirit to promote. Roll 1d4: (1) blackberry seawine from Mount Sar; (2) Berg Brew — an alchemically frozen slurry, extremely potent; (3) Entsap, brewed from treant sap, earthy and bitter; (4) \"Storm Giant Ale\" — no giants involved, but it tingles. He pushes for a trial order and will negotiate a good first-delivery rate." (`sources/Appendix_D_-_Running_the_Tavern.md:1397`)
- **Appendix D, Patron table**: "| 11 | Hammond Kraddoc *(Vintners' Guild)* |" — `sources/Appendix_D_-_Running_the_Tavern.md:1115`
- **Appendix D, Lif's ordering (Ulkoria, not Hammond; not used)**: none.
- **Trollskull Manor location, cellar (`tm03-cellar.md:13`)**: quoted in A2.
- **Adventure, the guild's "Sample Guild Representatives" (quest-time visits; `sources/adventure-wdh.json:4094`)**: quoted in A1.
- **PDF, HAMMOND KRADDOC (Vintners'), printed p.187 (transcription)**: "Dropping by to let the owners know about new spirits his guild has to offer: Blackberry seawine from the Nasaqh Estates on Mount Sar. Berg Brew, an alchemically frozen slurry that has ten times the alcoholic content of other beers. Entsap, brewed from the sap of treants. Storm Giant Ale, which is not actually bewed by storm giants but does have an electrical \"tingle.\"" / "Chastises the owners for their current selection of beverages (even if he was the one who sold them)." / "Discovers that Lif knew his father, Barbaros Kraddoc. ..." (see A1). — `sources/27. Addendum A Night in Trollskull Manor.pdf`, PDF page 10
- **Governance page, Guild Gauntlet (`guilds.md:40`)**: "- **The Guild Gauntlet (campaign-only):** In **Trollskull Alley**, Broxley Fairkettle and Hammond Kraddoc give the party a checklist, which reads "Required guilds: ..." Each needs a site inspection and a fee."
- **Governance page, Featured in (`guilds.md:9`)**: "**Fireball!** (Kalain's Tower, where Neverember's letters to Hammond Kraddoc are found)".

---

## D. Conflicts

**D1. Affiliation label and the guild**
- Page (line 6): "> - **Affiliation:** Trollskull Alley community"
- Governance page (`campaign/setting/governance-and-guilds/guilds.md:46`): "**Hammond Kraddoc** (Neutral, Illuskan Human, he/him) represents the Vintners', Distillers', and Brewers' Guild ..."
- Adventure (`sources/adventure-wdh.json:4112`): "{@i Vintners', Distillers', and Brewers' Guild}"
- Higher ranked: the governance page and the adventure name the guild. The page's "Trollskull Alley community" is a neighborhood label, not an organization. No Vintners' organization page exists. Flag for the orchestrator: the label needs a decision (brief ruling 6).
- Occupation: the wiki infobox says "Brewer" (extract line 16), its lead says "representative" (extract line 62). Lower ranked; the page and the adventure say guild representative. Not a campaign conflict.

**D2. Who paid the bribes (Kalain's Tower letters)**
- Fireball! ev-07: "Letters to Hammond Kraddoc of the Vintners', Distillers', and Brewers' Guild confirming large bribes paid to cover a contaminated-liquor scandal in the Dock Ward." (`campaign/quests/act-ii/fireball/ev-07-kalainsalley-tower.md:55`). The payer is not named.
- Governance page: "letters to Hammond Kraddoc that confirm large bribes paid to cover a contaminated-liquor scandal in the Dock Ward." (`campaign/setting/governance-and-guilds/guilds.md:66`). The payer is not named.
- Alexandrian Act III Arc D: "Correspondence with Hammond Kraddoc of the Vintners', Distillers', and Brewers' Guild confirming that Kraddoc paid Lord Dagult large bribes to cover up a contaminated-liquor scandal in the Dock Ward." (`sources/Act_III_Arc_D.md:596`).
- Higher ranked: the campaign quest file (`ev-07:55`) names no payer. The Alexandrian line says Kraddoc is the payer. The campaign does not adopt the Alexandrian direction. The drafter must not put any of this on the day-one page (quest-time).

**D3. "Went into business with the new owners" (wiki) against the campaign's day-one state**
- Wiki (extract line 65; dump line 4020648): "In [[1492 DR]],{{WDH-time}} Hammond possibly went into business with the new owners of the [[Trollskull Manor]]."
- Campaign: the manor is closed on Ches 1 ("The tavern has been closed for years", `campaign/gazetteer/waterdeep/north-ward.md:63`) and the party gets it after Volo's quest (`sources/adventure-wdh.json:1595`).
- Adventure: "even if he previously sold them those goods" (`sources/adventure-wdh.json:4114`) (a sale to the tavern's owners, after the reopening).
- Higher ranked: the campaign and the adventure. The wiki's "new owners" is the party, which is quest-time. The wiki says "possibly". Do not put this on the day-one page.

**D4. The father's stays and Lif's solitary minding (PDF against gazetteer, timing only)**
- PDF (printed p.187, transcription): "Discovers that Lif knew his father, Barbaros Kraddoc. Barbaros would actually stay at Trollskull Manor when he would come into Waterdeep to sell wines from the Elysium Fields."
- Gazetteer (`campaign/gazetteer/waterdeep/north-ward.md:63`): "has minded the building alone since 1479 DR."
- No source dates Barbaros's stays. A day-one Background that has Barbaros staying at the manor must place the stays before the tavern closed (the gazetteer dates the solitary haunting from 1479 DR). This is a consistency constraint, not a conflict. Flag.

**D5. Ethnicity or species (none)**
- All sources say Illuskan human (see B). No conflict.

---

## E. Stale lines in other files (not edited) and routed quest references

- `campaign/structure/arc-c-fireball.md:275`: "- Correspondence with Hammond Kraddoc of the Vintners', Distillers', and Brewers' Guild confirming large bribes paid to cover a contaminated-liquor scandal in the Dock Ward." — superseded by `ev-07-kalainsalley-tower.md:55`. Stale on the payer question (D2).
- `campaign/structure/arc-c-fireball.md:357`: "Lord Dagult's papers (Scene 5, optional): vault-opening method, Kraddoc correspondence, unsigned Eyes letter confirming all three were in Neverember's hands four years ago." — superseded. Quest-time.
- `campaign/quests/act-i/trollskull-alley/ev-02-the-guild-gauntlet.md:62` names Hammond as a "chastises" visitor during the Vintners' Guild inspection. Routed to ev-02.
- `campaign/gazetteer/waterdeep/north-ward.md`: no Hammond line (grep).
- `campaign/guides/gm-guide/design-notes-running-the-campaign.md:120`: "- Madrak, Jinny (Kraddoc's scribe), Justyn Rassk — too peripheral" — the design note treats Jinny as peripheral. Not a Notable Figures fact.
- `campaign/setting/notable-figures/trollskull-community/07-hammond-kraddoc.md:25`: "a recurring antagonist of Emmek Frewn" — no source (C3).
- `sources/Appendix_D_-_Running_the_Tavern.md:741` and `:748`: Hammond's featured spirits as the tavern's stock (tavern-time economy). Not a biography fact.

**E-routed (quest-time references and where each already lives):** `ev-02-the-guild-gauntlet.md:16`, `:18`, `:62`, `:78`, `:82`; `overview.md:28`; `fireball/ev-07-kalainsalley-tower.md:55`; `guides/trollskull-manor/06-tavern-time.md:30`, `:67`; `08-notable-patrons.md:82` to `:87`; `locations/trollskull-manor/tm03-cellar.md:13`; `sources/Act_III_Arc_D.md:596`; `sources/adventure-wdh.json:4094`, `:4114`; Appendix D `:741`, `:748`, `:1115`, `:1389` to `:1400`; PDF printed p.187; `campaign/setting/governance-and-guilds/guilds.md:9`, `:40`, `:66`.

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with.

1. **Origin, birth and arrival in Waterdeep.** No source. The wiki gives the home as "[[Waterdeep]], [[Sword Coast North]]" (extract line 11) and "ethnicity = Illuskan" (extract line 15). The age is blank (extract line 17). Stay consistent with: Illuskan, living in Waterdeep.
2. **How he got the guild post, and when.** No source. The wiki says "in the early 1490s DR" (extract line 62). Stay consistent with: a representative of the Vintners', Distillers', and Brewers' Guild in the North Ward spirit trade (`guilds.md:46`).
3. **The father, Barbaros Kraddoc.** PDF only (printed p.187, transcription). No other source. The PDF's stays at the manor, the wines from the Elysium Fields, and the Elysium Fields' destruction are PDF-only. Stay consistent with: Barbaros is a wine seller who came into Waterdeep; Lif knew him (PDF). The wine trade is not otherwise in the campaign. "Elysium Fields" is not in any campaign file (grep found none).
4. **Mother and other family.** No source. The wiki leaves parents, spouses and siblings blank (extract lines 29 to 31).
5. **His faith, if any.** No source. Do not give him a deity.
6. **Why he visits socially.** The sources say only that he "is here purely socially, which is unusual enough that Jinny is recording it" (Appendix D `:1400`, tavern-time) and "he has nobody else to drink with" (`guilds.md:46`). Stay consistent with: the social visits and the loneliness.
7. **Jinny's background.** Sourced as "NG female tiefling commoner" (`sources/adventure-wdh.json:4113`); "a young scribe" (same line); no name for her family or origin. Jinny has no Notable Figures page (`guilds.md:121`).
8. **His personal goals beyond the guild.** No source. Campaign motives (`page line 15`) are the guild's spirit trade and visits. Any personal goal is a `[design]` addition (ruling 17).

---

## G. Inner-life hints in the sources (exact quotes)

These are the sourced hints a Background or the personal goals may use. They must not be contradicted.

- **Dislike of adventurers, love of coin.** "doesn't like adventurers, but he likes their coin." — `sources/adventure-wdh.json:4113`
- **Enjoys the good spirits.** "Brightens at good spirits." — `sources/Appendix_D_-_Running_the_Tavern.md:1394`; "Sighs at ale." (same line)
- **Measures a room by its bar.** "Measures the quality of a room by what the bar stocks." — `:1394`
- **Social visits, unusual.** "Is here purely socially, which is unusual enough that Jinny is recording it." — `:1400`
- **Loneliness and drinking company.** "he keeps visiting after the inspections end because he has nobody else to drink with." — `campaign/setting/governance-and-guilds/guilds.md:46`; "a man who loves fine spirits and has no one else to drink them with" — page line 21 (day-one persona, design-adjacent).
- **Pride in the guild's trade.** "wants to keep its hold on the North Ward's spirit trade" — `guilds.md:46`.
- **Fear of exposure, hidden.** "Hammond Kraddoc ... He has not reported this yet. He mentions it in a way that suggests he is deciding whether to." — Appendix D `:1399` (topic 3, tavern-time).
- **Father (PDF only).** "Discovers that Lif knew his father, Barbaros Kraddoc." — PDF printed p.187 (transcription).
- **Scribe always present.** "always present, always recording, never introduced" — `campaign/guides/trollskull-manor/08-notable-patrons.md:83`.
- **Voice sample on loneliness.** "secretly lonely for company" — voice profile line 116 (tagline); "Self-importance over loneliness." — line 122.
