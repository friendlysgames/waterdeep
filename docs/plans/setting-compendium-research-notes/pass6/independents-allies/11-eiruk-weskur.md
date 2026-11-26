# Pass 6 research notes: Eiruk Weskur

Page: `campaign/setting/notable-figures/independents-allies/11-eiruk-weskur.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 19, user rulings Session 53)
Day one: Ches 1, 1492 DR.
Organization page: none. No `campaign/setting/organizations/` page covers Oghma's clergy or the Black Tears. Affiliation label is on the page at line 6 (see D4).
Factions Guide: none names Eiruk.
Deity page (campaign, the faith link): `campaign/setting/deities/oghma.md`. It names Eiruk as a priest (see D1).
Voice profile: `.claude/skills/character-voices/voices/independents-allies.md` lines 210 to 224.
Model format: `docs/plans/setting-compendium-research-notes/pass6/trollskull-community/01-talisolvanar-fellbranch.md`

## Method and caveats

- Campaign files: Grep and Read. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json` has no line naming Eiruk or Weskur (grep). Undermountain (`sources/adventure-wdmm.json`): no match.
- Alexandrian: `sources/Appendix_D_-_Running_the_Tavern.md:1139` (markdown table row only; no profile). `sources/27. Addendum A Night in Trollskull Manor.pdf` PDF page 8 (printed p.185): "15 Eiruk Weskur". Transcription: check with `pdftotext -layout`. `sources/26. Addendum Other Collaborators.pdf` and `sources/2. Other Factions.pdf` read in full: no match.
- Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-independents-allies/11-eiruk-weskur.txt` is a real page. Its only citation is the novel *Blackstaff Tower* (the page links `Blackstaff Tower (novel)`, wiki line 76). Edition is not tagged. Cited as "wiki line N".
- `voicecheck.py` was not run. No shell. No file was edited except this notes file.

## Findings that change how the page is written

1. **The wiki makes Eiruk a Watchful Order mage; the campaign makes him a priest of Oghma.** The campaign's priesthood is in the summary (line 5), the Persona and Relationships (lines 21 and 25), the Overview (line 29), the deity page and the voice profile. The wiki says "occupation = Wizard" (wiki line 16), "class = [[Mage]]" (wiki line 35) and that he joined the Watchful Order "around [[1473 DR]]" (wiki line 62). No campaign file explains a mage becoming a priest. This is the largest open conflict on the page (D1).
2. **The campaign gives the faith no act.** `campaign/setting/deities/oghma.md:71` says "No quest or event has Oghma act". Keep the priesthood as the page's day-one fact, not an event.
3. **The wiki adds a 1479 DR story with a backup heir to the Blackstaff.** No campaign file contradicts it directly, but the campaign's Vajra page says her heir choice is secret (`campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md:155`). The force-grey organization page marks "the Blackstaff's heir" as wiki-only `[research]` (`campaign/setting/organizations/05-force-grey.md:151`). See D2.

---

## A. Background facts by theme

### A1. Origin, kin and the 1479 DR story (wiki, Blackstaff Tower novel)

> "'''Eiruk Weskur''' was a young [[human]] [[wizard]] of [[Waterdeep]].<ref name="BST-p105-106">{{Cite book/Blackstaff Tower|105-106}}</ref>"
> — wiki line 56

> "Eiruk had black hair that he often worn shorn short in a [[skullcap (cap)|skullcap]].<ref name="BST-p105-106" />"
> — wiki line 59 (section "Description")

> "Eiruk's mother was named [[Ainla]].<ref name="BST-p195">{{Cite book/Blackstaff Tower|195}}</ref>"
> — wiki line 71 (section "Relationships")

> "Eiruk joined the [[Watchful Order of Magists and Protectors]] around [[1473 DR]].<ref name="BST-p110">{{Cite book/Blackstaff Tower|110}}</ref>"
> — wiki line 62 (section "History")

> "In [[1479 DR]], Eiruk was recruited by [[Khondar "Ten-Rings" Naomal|Khondar "Ten-Rings" Naomal]] to aid the [[Blackstaff]], [[Samark Dhanzscul]], in retrieving an item from the tomb of [[Sarael Arunsun]]."
> — wiki line 64

> "Only an honest and just person (in this case Eiruk) could receive the item; that person also received an invisible, magical mark."
> — wiki line 64

> "Because he had the mark, Eiruk was made the backup heir to the [[Blackstaff]]."
> — wiki line 64

> "When Laraelra, [[Renaer Neverember]], [[Meloon Wardragon]], and others were accused by Khondar of murdering Vajra, Eiruk initially joined other wizards in his guild in an attempt to capture them."
> — wiki line 66

> "Eiruk switched sides after witnessing a battle between mages from the Watchful Order and Laraelra's friends and he helped return Vajra to [[Blackstaff Tower]] because he had a crush on her. The crush made her feel uncomfortable, so she decided to make [[Laraelra Harsard]] her heir instead of him.<ref name="Blackstaff Tower"/>"
> — wiki line 66

> "Eiruk was later made one of the founding members of the group organized by Renaer to replace the [[Moonstars]].<ref name="BST-p305">{{Cite book/Blackstaff Tower|305}}</ref>"
> — wiki line 68

Campaign counterpart (day one, no date): "Deep down, he stays with the Black Tears because he believes Renaer is going to need a priest before this is over, and he would rather be there than hear about it later." — `campaign/setting/notable-figures/independents-allies/11-eiruk-weskur.md:21`

On the Black Tears as the Moonstars replacement: the campaign never says it. Renaer's page: "Renaer is the estranged son of Dagult Neverember (former Open Lord, current Lord of Neverwinter), the devoted friend of Floon Blagmaar, the closest living friend of Meloon Wardragon (whose changed behavior has him alarmed), a man who rescued Vajra Safahr from Khondar Naomal's agents and left the Blackstaff permanently in his debt, a Harper-adjacent ally of Mirt and Remi Haventree, and the leader of the Black Tears (his personal circle of trusted companions)." — `campaign/setting/notable-figures/independents-allies/02-renaer-neverember.md:25`. On the Moonstars: "The campaign has no Moonstars page, and Khelben is dead in the campaign." — `campaign/setting/organizations/01-harpers.md:187`

### A2. The faith (campaign)

- "Eiruk Weskur is a priest of Oghma and a member of Renaer Neverember's Black Tears, steady and patient, the one the group looks to when their decisions carry weight." — `11-eiruk-weskur.md:29`
- "His faith teaches that knowledge includes knowing when to swing a mace." — `11-eiruk-weskur.md:23`
- Deity page, the campaign's own account: "Oghma never appears in person. His faith reaches the campaign through Eiruk Weskur, a priest in Renaer Neverember's Black Tears, and through the Font of Knowledge, whose archivist appears in a Harper mission." — `campaign/setting/deities/oghma.md:8`
- Deity page, campaign ties: "**Campaign ties:** A priest of Oghma in Renaer's circle, an archivist at the Font, and the Font itself." — `campaign/setting/deities/oghma.md:71`
- Deity page, epithet: "Eiruk's voice profile has him call Oghma "the Binder" (`.claude/skills/character-voices/voices/independents-allies.md:215`), and no campaign file shows which name the city uses." — `campaign/setting/deities/oghma.md:115`

### A3. Temperament and habits (campaign and voice)

- "Eiruk most often feels patient curiosity, bone-deep conviction, steady loyalty, scholarly absorption, gentle stubbornness about theological points, and a calm that deepens rather than breaks under pressure." — `11-eiruk-weskur.md:13`
- Voice: "**Quirks:** He writes down what people say. He quotes a text, then admits he may be misremembering it. He waits a beat before answering." — `.claude/skills/character-voices/voices/independents-allies.md:218`
- Voice: "**Word choice:** Scholarly and gentle: knowledge, record, "it's written that…". He calls Oghma "the Binder". He calls friends by name, gently." — `independents-allies.md:215` (the profile's own ellipsis)

### A4. Time in post and location

- No source gives Eiruk's age (wiki: "young", wiki line 56), birthplace, an Oghma house, or when he joined the Black Tears. The wiki's "around [[1473 DR]]" (wiki line 62) is the only date for the Order.

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Summary: "> - *Chondathan human priest of Oghma, neutral good, he/him*. Stat block: **Priest**." — `campaign/setting/notable-figures/independents-allies/11-eiruk-weskur.md:5`
- Campaign-assigned: "All six (Elra, Osco, Torlyn, Eiruk, Harug, Parlek) lacked alignment in their stat lines. Alignments assigned and committed (`c0c6bde`)." — `session 5 handoff.md:73`
- Wiki: "| alignment5e    = " (blank) — wiki line 52
- Appendix D: "| 15 | Eiruk Weskur |" (`sources/Appendix_D_-_Running_the_Tavern.md:1139`). No alignment.

**Species**
- Summary: "Chondathan human" (`11-eiruk-weskur.md:5`). "Chondathan" is campaign-only. Ruling 5 accepts it as a Faerûn ethnicity.
- Wiki: "| race           = [[Human]]" — wiki line 14. Wiki line 56: "was a young [[human]] [[wizard]]".

**Pronouns**
- Summary: "he/him" (`11-eiruk-weskur.md:5`)
- Wiki: "| sex            = Male" — wiki line 13

**Stat block**
- Summary: "Stat block: **Priest**." (`11-eiruk-weskur.md:5`)
- Wiki: "| occupation     = Wizard" — wiki line 16. "| class          = [[Mage]]<ref name="BST-p110">{{Cite book/Blackstaff Tower|110}}</ref>" — wiki line 35.
- Conflict: D1.

---

## C. Sentences on the current page that narrate a quest-time event or a day-one conflict

The page has no quest event and no Background section yet. Every sentence on the page was checked.

| Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|
| L7 | "> - **Featured in:** Background figure; no scripted appearance." | Campaign label. Not an event. | Renaer's Friends row: `campaign/guides/trollskull-manor/06-tavern-time.md:93` |
| L11 | "**Resonance.** Eiruk should inspire trust with his steadiness, gratitude when he offers counsel without being asked, and warmth with his genuine belief that knowledge shared is knowledge doubled." | Day one. Keep. | none needed |
| L13 | "**Emotions.** Eiruk most often feels patient curiosity, bone-deep conviction, steady loyalty, scholarly absorption, gentle stubbornness about theological points, and a calm that deepens rather than breaks under pressure." | Day one. Keep. | none needed |
| L15 | "**Motivations.** Eiruk wants to serve Oghma by gathering and sharing knowledge, keep his friends grounded when ambition or anger pulls them off course, and understand the deeper history behind the events unfolding in Waterdeep." | Framing. "the events unfolding in Waterdeep" points at the campaign's events and names none. Drafter's call (C2). | none needed |
| L21 | "**Persona.** To the world, Eiruk is a priest of Oghma who keeps company with a noble's drinking circle. To those he trusts, he is the one who listens, remembers, and offers his opinion only when asked. Deep down, he stays with the Black Tears because he believes Renaer is going to need a priest before this is over, and he would rather be there than hear about it later." | Framing. "before this is over" points at the campaign's end and names no event. Drafter's call (C2). | none needed |
| L23 | "**Morale.** In a fight, Eiruk would heal first, fight second, and put himself between danger and whoever is most vulnerable. His faith teaches that knowledge includes knowing when to swing a mace." | Day one. Keep. | none needed |
| L25 | "**Relationships.** Eiruk is a priest of Oghma and a member of Renaer's Black Tears. When the group's decisions carry moral weight, they look at Eiruk whether they mean to or not." | Day one. "the group's decisions" names no decision. Keep. | none needed |
| L29 | "Eiruk Weskur is a priest of Oghma and a member of Renaer Neverember's Black Tears, steady and patient, the one the group looks to when their decisions carry weight." | Day one. Keep. | none needed |

### C2. Framing lines (not quest events; drafter's call)

- L15 "the events unfolding in Waterdeep" and L21 "before this is over" both point at the campaign's arc. Neither names an event, a faction move or an outcome. Keep, or restate as a day-one concern under ruling 1.

### C3. Renaer's Friends table and the Oghma page (routed; tavern-time)

- Campaign: "| 15 | Eiruk Weskur |" — `campaign/guides/trollskull-manor/06-tavern-time.md:93` (heading "## Renaer's Friends Table (d20)" at line 84)
- Campaign: "Use this four-step procedure for each significant night the characters spend at the tavern." — `campaign/guides/trollskull-manor/06-tavern-time.md:5`
- Campaign, deity page: "**Featured in:** **A Friend's House** (Harpers Mission 4), where the Font's archivist offers a record that mentions the Vault of Dragons, and **Tavern Time** in the Trollskull Manor guide, where Eiruk can arrive as one of Renaer's friends." — `campaign/setting/deities/oghma.md:9`
- Appendix D: "| 15 | Eiruk Weskur |" — `sources/Appendix_D_-_Running_the_Tavern.md:1139`
- Addendum PDF page 8 (printed p.185), transcription: "15 Eiruk Weskur". Check with pdftotext.
- Tavern status: "A long-closed tavern, Trollskull Manor, stands at the end of Trollskull Alley among old residences and shops." — `campaign/gazetteer/waterdeep/north-ward.md:203`
- Ownership by the party: "The deed is real. **Trollskull Manor** is real, non-operational, and now the party's property." — `campaign/quests/act-i/finding-floon/ev-04-xanathar-sewer-hideout.md:100`

### C4. Voice profile quest-time clauses (`.claude/skills/character-voices/voices/independents-allies.md`, lines 210 to 224)

- Line 211 (tagline): "*A steady, patient priest of Oghma who listens first, remembers everything, and speaks when asked.*" — no quest event.
- Line 222 (Greeting): "*Greeting:* "Welcome. Sit, please. Tell me what brought you here, and take your time."" — assumes a first meeting. Drafter's call.
- Line 223 (Business): "*Business:* "There's an older account of that family in the Oghmanyte archive. I'll look tonight."" — "that family" names no family. No quest event.
- Line 224 (Under pressure): "*Under pressure:* "Breathe. We'll do this carefully, and then we'll do the next thing."" — no quest event.
- No profile change is needed for a quest-time clause.

---

## D. Conflicts

**D1. Class and occupation (campaign priest vs wiki mage)**
- Campaign summary: "> - *Chondathan human priest of Oghma, neutral good, he/him*. Stat block: **Priest**." — `campaign/setting/notable-figures/independents-allies/11-eiruk-weskur.md:5`
- Campaign Overview: "Eiruk Weskur is a priest of Oghma and a member of Renaer Neverember's Black Tears, steady and patient, the one the group looks to when their decisions carry weight." — `11-eiruk-weskur.md:29`
- Campaign deity page: "**Campaign ties:** A priest of Oghma in Renaer's circle, an archivist at the Font, and the Font itself." — `campaign/setting/deities/oghma.md:71`
- Wiki: "| occupation     = Wizard" — wiki line 16
- Wiki: "| class          = [[Mage]]<ref name="BST-p110">{{Cite book/Blackstaff Tower|110}}</ref>" — wiki line 35
- Wiki: "'''Eiruk Weskur''' was a young [[human]] [[wizard]] of [[Waterdeep]].<ref name="BST-p105-106">{{Cite book/Blackstaff Tower|105-106}}</ref>" — wiki line 56
- Higher ranked: the campaign. The priesthood is in the summary, Persona, Relationships, Overview, deity page and voice profile. The wiki's "Mage" is not adopted, and the stat block stays "Priest". No file bridges a Watchful Order mage and an Oghma priest. Any Background that uses the wiki's Order years must say how he became a priest (as `[design]`), or leave those years out (ruling 15).

**D2. Blackstaff heir (wiki vs campaign secrecy)**
- Wiki: "Because he had the mark, Eiruk was made the backup heir to the [[Blackstaff]]." — wiki line 64
- Wiki: "The crush made her feel uncomfortable, so she decided to make [[Laraelra Harsard]] her heir instead of him." — wiki line 66
- Campaign, Vajra's personal goals: "choosing an heir and giving that student a few more years as a student, which she has told no one." — `campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md:155`
- Campaign, organization research note: "- **Research:** Wiki-only items tagged `[research]` in the body: the Khelben, Tsarra and Kyriani line, Jardwim, Piergeiron and Harshnag, the Blackstaff's heir, and the head count." — `campaign/setting/organizations/05-force-grey.md:151`
- Not a direct contradiction. The campaign says Vajra has chosen an heir and told no one. The wiki says Eiruk was the backup heir in 1479 DR and that Laraelra became the heir. The campaign does not name Laraelra as heir. Higher ranked: the campaign's secrecy line. Keep the heir claim as `[research]`. Do not state it as fact on Eiruk's page.

**D3. Renaer's group and the Moonstars (wiki vs campaign)**
- Wiki: "Eiruk was later made one of the founding members of the group organized by Renaer to replace the [[Moonstars]]." — wiki line 68
- Campaign: "and the leader of the Black Tears (his personal circle of trusted companions)." — `campaign/setting/notable-figures/independents-allies/02-renaer-neverember.md:25`
- The campaign does not connect the two. Do not link them without a ruling.

**D4. Affiliation label**
- Summary: "> - **Affiliation:** Independent (ally)" — `11-eiruk-weskur.md:6`
- Relationships: "**Relationships.** Eiruk is a priest of Oghma and a member of Renaer's Black Tears. When the group's decisions carry moral weight, they look at Eiruk whether they mean to or not." — `11-eiruk-weskur.md:25`
- Deity page cross-reference: "- **Eiruk Weskur**, **Renaer Neverember** (Notable Figures): the priest and his circle, the Black Tears." — `campaign/setting/deities/oghma.md:105`
- No organization page for Oghma's clergy in the campaign. The Oghma deity page is a deity page, not a faction. The drafter keeps "Independent (ally)" and states the priesthood and the membership in Connections.

**D5. Ethnicity (no conflict)**: The wiki says "[[Human]]" (wiki line 14) with no ethnicity. "Chondathan" is campaign-only.

---

## E. Stale lines in other files (not edited), and routed references

**E1. Lines that depend on the priesthood**
- `campaign/setting/deities/oghma.md:8`, `:71`, `:94`, `:105` and `:109`: all name Eiruk as a priest. If D1 is decided the other way, these change.
- `campaign/setting/deities/oghma.md:17`: "- **Other Names:** The Binder of What Is Known, the Lord of Knowledge (FRHoF); the Binder (SCAG, 2014); the Wise God and Patron of Bards (wiki, 2e)" — the voice's "the Binder" is an existing name (`oghma.md:115`).
- `.claude/skills/character-voices/SKILL.md:23`: lists Eiruk with the Black Tears. Matches.

**E2. Routed quest references (quest-time)**
- `campaign/guides/trollskull-manor/06-tavern-time.md:93`, `:84` and `:5`; `sources/Appendix_D_-_Running_the_Tavern.md:1139`; Addendum PDF page 8 (printed p.185).
- `campaign/setting/deities/oghma.md:9` (Tavern Time, "where Eiruk can arrive as one of Renaer's friends").

**E3. Name in another note**
- `campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md:155` names "Samark's ward". The wiki names Samark Dhanzscul as the Blackstaff's agent in the 1479 DR tomb story (wiki line 64). No campaign file explains who Samark is. Do not link Samark to Eiruk without a ruling.

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]`.

1. **How a Watchful Order mage became a priest of Oghma.** No source. Wiki: "Eiruk joined the [[Watchful Order of Magists and Protectors]] around [[1473 DR]]." (wiki line 62). Campaign: "priest of Oghma" (line 5). The drafter must decide the path (`[design]`), or keep the wiki's Order years as `[research]` and the priesthood as the campaign's day-one fact, and say which is which (ruling 15, D1).
2. **Age.** Wiki: "young" (wiki line 56). No number. Day-one age is open.
3. **Birthplace and kin.** Wiki gives the mother "Ainla" (wiki line 71). No birthplace and no father. The "Chondathan" ethnicity (summary, line 5) is campaign-only.
4. **An Oghma house.** No source. The Oghmanyte church appears only as a wiki name on the deity page (`campaign/setting/deities/oghma.md:39`), not as Eiruk's house.
5. **The crush on Vajra and the heir story.** Wiki: "because he had a crush on her" (wiki line 66). It depends on the wiki's Blackstaff plot (D2). Use only as `[research]`.
6. **Why he stays with the Black Tears.** Campaign: "he believes Renaer is going to need a priest before this is over" (`11-eiruk-weskur.md:21`). No event. Keep the belief, not a timeline.
7. **Any history with Laraelra.** Wiki gives the rivalry-by-heir line (wiki line 66). The campaign's Laraelra page (`campaign/setting/notable-figures/independents-allies/08-laraelra-elra-harsard.md:25`) says only that she is "a member of Renaer's Black Tears".

---

## G. Inner-life hints in the sources (exact quotes)

- **Belief.** "Deep down, he stays with the Black Tears because he believes Renaer is going to need a priest before this is over, and he would rather be there than hear about it later." — `11-eiruk-weskur.md:21`
- **Conviction.** "Eiruk most often feels patient curiosity, bone-deep conviction, steady loyalty, scholarly absorption, gentle stubbornness about theological points, and a calm that deepens rather than breaks under pressure." — `11-eiruk-weskur.md:13`
- **Faith in action.** "His faith teaches that knowledge includes knowing when to swing a mace." — `11-eiruk-weskur.md:23`
- **Goal.** "Eiruk wants to serve Oghma by gathering and sharing knowledge, keep his friends grounded when ambition or anger pulls them off course, and understand the deeper history behind the events unfolding in Waterdeep." — `11-eiruk-weskur.md:15`
- **Voice, under pressure.** "**Personality in speech:** Patient curiosity and deep conviction. He's stubborn on theological points and says so softly. Under pressure he gets calmer, and his sentences slow down." — `independents-allies.md:217`
- **Voice, signature.** "**Signature phrases:** "What do you think?" / "Knowledge shared is knowledge doubled." / "Let me write that down."" — `independents-allies.md:219`
- **Voice, never.** "**Never:** He never gossips, never rushes, and never withholds knowledge that would help." — `independents-allies.md:220`
- **Wiki, the crush (`[research]`).** "The crush made her feel uncomfortable, so she decided to make [[Laraelra Harsard]] her heir instead of him." — wiki line 66
- **Wiki, the backup heir (`[research]`).** "Because he had the mark, Eiruk was made the backup heir to the [[Blackstaff]]." — wiki line 64
