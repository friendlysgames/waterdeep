# Pass 6 research notes: Lord Torlyn Wands

Page: `campaign/setting/notable-figures/independents-allies/10-lord-torlyn-wands.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 19, user rulings Session 53)
Day one: Ches 1, 1492 DR.
Organization page: none. No `campaign/setting/organizations/` page covers House Wands. Affiliation label is on the page at line 6 (see D5).
Factions Guide: `campaign/guides/factions/03-lords-alliance.md:68` names him (Stingblade rank benefit; routed in E2).
Governance pages checked: `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md`, `code-legal-and-magisters.md`, `city-watch.md`, `guilds.md`. None names Torlyn or any Wands.
Voice profile: `.claude/skills/character-voices/voices/independents-allies.md` lines 192 to 206.
Model format: `docs/plans/setting-compendium-research-notes/pass6/trollskull-community/01-talisolvanar-fellbranch.md`

## Method and caveats

- Campaign files: Grep and Read. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json` has no line naming Torlyn, Wands or House Wands (grep). Undermountain (`sources/adventure-wdmm.json`): no match.
- Alexandrian: `sources/Appendix_D_-_Running_the_Tavern.md:1138` (markdown table row only). `sources/27. Addendum A Night in Trollskull Manor.pdf` PDF page 8 (printed p.185) read with the Read tool's `pages` parameter: "13-14 Lord Torlyn Wands". Transcription: check with `pdftotext -layout`. `sources/26. Addendum Other Collaborators.pdf` and `sources/2. Other Factions.pdf` read in full: no match.
- Wiki: `scratchpad/wiki-independents-allies/10-lord-torlyn-wands.txt` is `NOT FOUND`. No wiki page for Torlyn is in the extract. The only wiki text is a family list in `sources/research/pass3-bundles/code-legal-and-magisters/wiki.txt` (the Wands page, lines 1024 to 1073; the Eldrus Wands page, lines 947 to 1020). The list citation is *Blackstaff Tower* (novel). Edition is not tagged for the lines quoted. Cited as "wiki line N" (file `wiki.txt`).
- `voicecheck.py` was not run. No shell. No file was edited except this notes file.

## Findings that change how the page is written

1. **No source makes Torlyn a Masked Lord.** The "Lord" in his name is the title his house gives him, as the quest file uses it: "Lord Torlyn Wands, a wizard of House Wands" (`campaign/quests/faction-events/lords-alliance/r10-stingblade/ev-01-stingblade.md:123`). He is not on any list of Masked Lords in the campaign, and the governance page says Laeral will not name one (D2).
2. **The page puts him in a tavern that is closed on day one.** The Persona (line 21), the voice tagline (line 193) and the voice "Never" line (line 202) all put him at Trollskull. The gazetteer says the tavern has been closed for years on day one (`campaign/gazetteer/waterdeep/north-ward.md:63`). See D1.
3. **The only wiki material is a family list.** There is no wiki page for Torlyn. The house has a North Ward villa and a documented history (wiki lines 1052 to 1073). The father is not named in any source.

---

## A. Background facts by theme

### A1. Family and house (campaign)

- "Torlyn is a member of the Wands noble family, a member of Renaer's Black Tears, and a wizard whose family connections give the group social access they would not otherwise have." — `campaign/setting/notable-figures/independents-allies/10-lord-torlyn-wands.md:25`
- "Lord Torlyn Wands is a wizard from Waterdeep's notable Wands family who prefers Trollskull Alley to galas and keeps company with Renaer Neverember's Black Tears." — `10-lord-torlyn-wands.md:29`
- "Torlyn wants to be Renaer's friend rather than Lord Wands's son, practice his magic without political entanglement, and keep the Wands family's reputation intact without becoming its servant." — `10-lord-torlyn-wands.md:15`
- Quest-time (routed, E2): "**Lord Torlyn Wands**, a wizard of House Wands, receives the member at his rooms. He writes a letter of standing in the Wands name, and it opens one noble door: a dinner, a servants' entrance or a steward's ear." — `campaign/quests/faction-events/lords-alliance/r10-stingblade/ev-01-stingblade.md:123`

### A2. The house (wiki, family pages, not a Torlyn page)

> "'''Wands''' ({{Pronounce|WANDS|refs=<ref name="CS-WW2e-p28"><nowiki>{{Cite book/City of Splendors (boxed set)/Who's Who in Waterdeep|28}}</nowiki></ref>}}) was a distinguished [[Waterdhavian]] noble house that had a strong history of magic within the city.<ref name="CSW p.63">{{Cite book/City of Splendors: Waterdeep|63}}</ref>"
> — `sources/research/pass3-bundles/code-legal-and-magisters/wiki.txt:1052`

> "The family owned [[Wands Villa|a villa]] in the [[Waterdeep/North Ward|North Ward]], at the corner of [[Shando Street]] and the [[Magecourt]].<ref name="CSW3e-p94,101">{{Cite book/City of Splendors: Waterdeep|94,101}}</ref><ref name="WDH5e-map">{{Cite book/Waterdeep: Dragon Heist/Map}}</ref>"
> — `wiki.txt:1055`

> "From his many children, Eldrus was the founder of what would become House Wands of Waterdeep.<ref name="CoS.W-p63"/><ref name="SotM-p41" />"
> — `wiki.txt:1014` (Eldrus Wands page)

> "* [[Eldrus Wands]] ([[409 DR]] – [[516 DR]]). Infamous Patriarch of the Waterdeep [[Wands]] Family."
> — `wiki.txt:116`

> "* [[Torlyn Wands]] ([[1479 DR]])<ref name="BST-p11-12">{{Cite book/Blackstaff Tower|11-12}}</ref>"
> — `wiki.txt:1069` (members list)

> "* [[Nharaen Wands]] ([[1479 DR]])<ref name="BST-p300-301">{{Cite book/Blackstaff Tower|300-301}}</ref>"
> — `wiki.txt:1064` (another member in 1479 DR; no relation is stated)

> "In [[1370 DR]], the Wands family suffered a public embarrassment when Marcus Wands stole the family heirloom of [[Mulhorand]]i origins, the ''[[golden scarab beetle]]'', that was said to bring magic luck to any Wands family member possessing it. The ''scarab'' was lost in [[Undermountain]] and Maskar Wands, the family [[wizard]] patriarch, requested [[Khelben Arunsun]]'s aid in the matter. The heirloom was subsequently retrieved from the [[Tomb of Ankh-Kephra]] and returned to the Wands family.<ref name="Dec">{{Cite game/Descent to Undermountain}}</ref>"
> — `wiki.txt:1073`

### A3. Training, craft and manner (campaign)

- "In a fight, Torlyn would cast with disciplined precision. He has been trained since childhood and fights like it, but he would rather talk his way out." — `10-lord-torlyn-wands.md:23`
- Voice: "A mix of courtly and tavern: he knows the right fork and doesn't care. He calls his family "the Wands" as if they were an institution." — `.claude/skills/character-voices/voices/independents-allies.md:197`

### A4. Friends and the circle (campaign)

- "Deep down, he carries the Wands name like luggage he cannot put down, and Renaer's circle is the one place no one asks him to open it." — `10-lord-torlyn-wands.md:21`
- Renaer's page: "Renaer is the estranged son of Dagult Neverember (former Open Lord, current Lord of Neverwinter), the devoted friend of Floon Blagmaar, the closest living friend of Meloon Wardragon (whose changed behavior has him alarmed), a man who rescued Vajra Safahr from Khondar Naomal's agents and left the Blackstaff permanently in his debt, a Harper-adjacent ally of Mirt and Remi Haventree, and the leader of the Black Tears (his personal circle of trusted companions)." — `campaign/setting/notable-figures/independents-allies/02-renaer-neverember.md:25`

### A5. Time in post and dates

- No source gives Torlyn's age, birthplace, training school or when he joined Renaer's circle. The only date is the family-list entry "([[1479 DR]])" (wiki line 1069).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Summary: "> - *Illuskan human wizard, chaotic good, he/him*. Stat block: **Mage**." — `campaign/setting/notable-figures/independents-allies/10-lord-torlyn-wands.md:5`
- Campaign-assigned: "All six (Elra, Osco, Torlyn, Eiruk, Harug, Parlek) lacked alignment in their stat lines. Alignments assigned and committed (`c0c6bde`)." — `session 5 handoff.md:73`
- Adventure and wiki: no alignment for Torlyn. Appendix D row: "| 13–14 | Lord Torlyn Wands |" (`sources/Appendix_D_-_Running_the_Tavern.md:1138`). No alignment.

**Species**
- Summary: "Illuskan human" (`10-lord-torlyn-wands.md:5`). Campaign-only. No source gives an ethnicity for Torlyn. Ruling 5 accepts "Illuskan", which is a Faerûn ethnicity.

**Pronouns**
- Summary: "he/him" (`10-lord-torlyn-wands.md:5`)
- Persona: "To those he trusts, he is a wizard who would rather drink at Trollskull than attend a gala." (`10-lord-torlyn-wands.md:21`)
- Pronoun table: `docs/plans/npc-pronouns-table-group-a.md:27` ("Lord Torlyn Wands | independents-allies/10-lord-torlyn-wands.md:5 | he/him | from page prose, line 21")
- Wiki: no pronoun (no page).

**Stat block**
- Summary: "Stat block: **Mage**." (`10-lord-torlyn-wands.md:5`)
- Wiki: no class for Torlyn. The house's "strong history of magic" (`wiki.txt:1052`) supports the wizard label but names no class.
- Voice: "A relaxed noble wizard who'd rather be at Trollskull than a gala, and says so." (`independents-allies.md:193`)

---

## C. Sentences on the current page that narrate a quest-time event or a day-one conflict

The page has no quest event and no Background section yet. Every sentence on the page was checked.

| Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|
| L6 | "> - **Affiliation:** Independent (ally)" | Label. See D5. | Stingblade (E2) |
| L7 | "> - **Featured in:** Background figure; no scripted appearance." | Campaign label. Not an event. | Tavern row `campaign/guides/trollskull-manor/06-tavern-time.md:32` (E2) |
| L11 | "**Resonance.** Torlyn should inspire respect for his family's legacy, endearment with his refusal to act like a noble, and amusement when his casual manner clashes with the Wands name." | Day one. Keep. | none needed |
| L13 | "**Emotions.** Torlyn most often feels relaxed confidence, dry amusement, protective pride in the Wands legacy, private stubbornness about living on his own terms, and honest pleasure in low-stakes company." | Day one. Keep. | none needed |
| L15 | "**Motivations.** Torlyn wants to be Renaer's friend rather than Lord Wands's son, practice his magic without political entanglement, and keep the Wands family's reputation intact without becoming its servant." | Day one. Keep. The father is unnamed (F2). | none needed |
| L21 | "**Persona.** To the world, Torlyn is a Wands noble, which means something in Waterdeep's magical circles. To those he trusts, he is a wizard who would rather drink at Trollskull than attend a gala. Deep down, he carries the Wands name like luggage he cannot put down, and Renaer's circle is the one place no one asks him to open it." | Day-one conflict on "drink at Trollskull": the tavern is closed on day one (D1). The rest is day one. | D1; `campaign/gazetteer/waterdeep/north-ward.md:63` |
| L23 | "**Morale.** In a fight, Torlyn would cast with disciplined precision. He has been trained since childhood and fights like it, but he would rather talk his way out." | Day one. Keep. | none needed |
| L25 | "**Relationships.** Torlyn is a member of the Wands noble family, a member of Renaer's Black Tears, and a wizard whose family connections give the group social access they would not otherwise have." | Day one. Keep. | A1 |
| L29 | "Lord Torlyn Wands is a wizard from Waterdeep's notable Wands family who prefers Trollskull Alley to galas and keeps company with Renaer Neverember's Black Tears." | Day one. "Trollskull Alley" is the street (open). The tavern is closed (D1). | D1 |

### C2. Voice profile (`.claude/skills/character-voices/voices/independents-allies.md`, lines 192 to 206)

- Line 193 (tagline): "*A relaxed noble wizard who'd rather be at Trollskull than a gala, and says so.*" — the day-one conflict (D1). A drafter who keeps the preference must name a place open on day one, or change "at Trollskull" to a day-one place. Profile change is the drafter's call (ruling 16).
- Line 201 (Signature): "**Signature phrases:** "Just Torlyn." / "The Wands can manage without me." / "Another round?"" — "Another round?" is at Trollskull by implication (D1).
- Line 202 (Never): "**Never:** He never pulls rank, never discusses family business, and never misses a round at Trollskull." — same conflict (D1).
- Line 204 (Greeting): "*Greeting:* "Torlyn. Just Torlyn. The Lord part stays at home with the silverware."" — no quest event. Assumes a first meeting. Drafter's call.
- Line 205 (Business): "*Business:* "I can get you into the Wands archive. I'd rather not, but I can."" — no quest event.
- Line 206 (Under pressure): "*Under pressure:* "Well. That's inconvenient. Shield up, everyone."" — no quest event.

### C3. Quest-time facts already in the files (routed, not for the day-one page)

- **Stingblade introduction (quest event).** "- **Lord Torlyn Wands**, a wizard of House Wands, receives the member at his rooms. He writes a letter of standing in the Wands name, and it opens one noble door: a dinner, a servants' entrance or a steward's ear." — `campaign/quests/faction-events/lords-alliance/r10-stingblade/ev-01-stingblade.md:123`
- **Stingblade, the member's line.** "> > "Then you don't need me for the door, but the introduction still carries what the list says. Lord Torlyn writes a letter for you only if I ask him, and it costs the same use. Is that the one you want?"" — `ev-01-stingblade.md:139`
- **Stingblade design notes.** "- The Fentree report lists the copper button stamped with a coiled dragon as unclaimed property, as **Fentree's Ledger** does, and that points to the Green Dragon Inn as a free lead beside the mission's own three. Barnibus, Torlyn, Saeth and Valetta are not voiced here, since the Event ends at the table." — `campaign/quests/faction-events/lords-alliance/r10-stingblade/design-notes.md:25`
- **Rank benefit (Factions Guide).** "| 10 | **Stingblade** | Once per quest, Jalester arranges an introduction to one of eight named Waterdhavians: Barnibus Blastwind of the Watchful Order, Lord Torlyn Wands, Saeth Cromley, Valetta, Factor Tessaly Brightwater, Guildmaster Piers Hobb, Clerk Maelith Dray or Lady Perrine Ostler. Once per quest, the Alliance's solicitor pays up to 500 gp of bail, fines and damages for one genuine incident. The member reads the Watch's files at the central records office. Standard files take one hour, and classified files take four hours and a **DC 12 Charisma (Persuasion)** check with the file officer. |" — `campaign/guides/factions/03-lords-alliance.md:68`
- **Tavern-time row (post-acquisition).** "| Kythorn 1–10 | Broxley Fairkettle, Tally Fellbranch, Laraelra "Elra" Harsard with Lord Torlyn Wands (Renaer's Friends) | 14: a Masked Lord visits (at Fame 81+); otherwise 17: a socialite demands the best table | Guild season. The night measures where the tavern stands with the city's upper floors. |" — `campaign/guides/trollskull-manor/06-tavern-time.md:32`
- **Renaer's Friends table.** "| 13–14 | Lord Torlyn Wands |" — `campaign/guides/trollskull-manor/06-tavern-time.md:92` (table heading "## Renaer's Friends Table (d20)" at line 84). Appendix D: "| 13–14 | Lord Torlyn Wands |" — `sources/Appendix_D_-_Running_the_Tavern.md:1138`. Addendum PDF page 8 (printed p.185), transcription: "13-14 Lord Torlyn Wands". Check with pdftotext.
- **Tavern premise.** "Use this four-step procedure for each significant night the characters spend at the tavern." — `campaign/guides/trollskull-manor/06-tavern-time.md:5`

---

## D. Conflicts

**D1. The tavern (page and voice vs gazetteer and quest)**
- Page: "To those he trusts, he is a wizard who would rather drink at Trollskull than attend a gala." — `10-lord-torlyn-wands.md:21`
- Voice: "A relaxed noble wizard who'd rather be at Trollskull than a gala, and says so." — `independents-allies.md:193`
- Gazetteer: "The tavern has been closed for years, and the poltergeist **Lif** haunts it. He is the spirit of the last barkeeper, a dwarf, and has minded the building alone since 1479 DR." — `campaign/gazetteer/waterdeep/north-ward.md:63`
- Gazetteer: "A long-closed tavern, Trollskull Manor, stands at the end of Trollskull Alley among old residences and shops." — `campaign/gazetteer/waterdeep/north-ward.md:203`
- Quest: "The deed is real. **Trollskull Manor** is real, non-operational, and now the party's property." — `campaign/quests/act-i/finding-floon/ev-04-xanathar-sewer-hideout.md:100`
- Higher ranked: the gazetteer and the quest (both campaign). The page's "Trollskull" as a drinking place is a post-quest state. The drafter must choose a day-one drinking place for Torlyn, or keep the preference with a place that is open on Ches 1. No file names one.

**D2. "Lord" and the Masked Lords (not a conflict; a confusion risk)**
- Governance overview: "Waterdeep is governed by the Open Lord, who rules in public, and by a council of secret Masked Lords. Ahghairon founded the system in 1032 DR and kept the Masked Lords anonymous so that nobody could bribe or threaten them. Laeral Silverhand is the Open Lord today, and invited petitioners meet the Lords in the Palace audience chamber. Any Masked Lord can overturn a magister's ruling, though one is rarely at hand when a petitioner needs it." — `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:56`
- Laeral's refusal: "> - **How Laeral answers questions about the Lords:** She will not name a Masked Lord to anyone and says "That is not mine to give." In **An Audience with the Open Lord** she signs the Masked Lord's Writ for the vault district and discloses the Splinter's offer of an account of every Masked Lord it has confirmed, for a fifth of the vault's contents. She asks the party's opinion and has not decided." — `open-lord-and-masked-lords.md:68`
- Manshoon's list: "> - **What anonymity does not protect:** The masks stop a stranger's bribe and do nothing against blackmail by someone who has learned a name. Manshoon keeps a list of five Masked Lords whose identities he knows. They are Mirt, Corylus Thann, Thardouk Starbuckler, Jelenn Urmbrusk and Dorgar Adarbrent, and he has checked off Corylus and Jelenn as the two he is blackmailing." — `open-lord-and-masked-lords.md:63`
- Named Lords in the campaign text: Mirt (`:40`), Jelenn Urmbrusk (`:42`), Durnan (`:44`), Ulkoria Stonemarrow (`:46`), Caladorn Cassalanter (`:50`). Torlyn is not among them, and no Wands is named anywhere on that page. The governance page says the identities are hidden, so the files cannot rule out a hidden seat. Nothing in the files gives him one.
- The same Fame-table row (`campaign/guides/trollskull-manor/06-tavern-time.md:32`) names Torlyn and "a Masked Lord visits". The drafter must not read Torlyn as the visitor. The governance page: "> - **At Trollskull Manor:** From Fame 81 a Masked Lord may stop by for a drink and a generous tip. At Fame 351 a Masked Lord has a reserved table." — `open-lord-and-masked-lords.md:69`

**D3. Father (not a conflict)**
- Campaign: "Torlyn wants to be Renaer's friend rather than Lord Wands's son" (`10-lord-torlyn-wands.md:15`). No father is named. The wiki's 1370 DR patriarch is "Maskar Wands, the family [[wizard]] patriarch" (`wiki.txt:1073`). The campaign does not say Maskar is Torlyn's father or grandfather. Do not assume it.

**D4. Class (no conflict).** The summary's "Mage" (line 5) has no wiki counterpart.

**D5. Affiliation label**
- Summary: "> - **Affiliation:** Independent (ally)" — `10-lord-torlyn-wands.md:6`
- Relationships: "Torlyn is a member of the Wands noble family, a member of Renaer's Black Tears, ..." — `10-lord-torlyn-wands.md:25`
- No organization page for House Wands or the Black Tears. The labels do not clash in the campaign, but the drafter should state both: independent, and of a noble house.

---

## E. Stale lines in other files (not edited), and routed references

**E1. Stale or sensitive lines**
- `campaign/gazetteer/waterdeep/north-ward.md:63` and `:203` (D1): the tavern is closed on day one. The Renaer's Friends table (`06-tavern-time.md:84` to `:98`) and the Torlyn row presume an open tavern.
- `campaign/guides/trollskull-manor/06-tavern-time.md:32`: a Masked Lord visit in the same row as Torlyn (D2).
- `campaign/gazetteer/waterdeep/north-ward.md:183`: "- Lesser noble houses keep villas among the rowhouses. The wiki lists Adarbrent, Agundar, Anteos, Gost, Gralhund, Hothemer, Hawkwinter, Kothont, Phull, Roaringhorn, Ulbrinter and Wands, and Dragon Heist adds Amcathra on the High Road, Margaster between Stabbed Sailor Alley and Shattercrock Alley, and Phylund on Copper Street." Lists Wands from the wiki only. No campaign villa is placed.
- `docs/plans/lords-alliance-mechanics-reference.md:315`: "| 2 | Lord Torlyn Wands | House Wands, wizard and heir's circle | A letter of standing from the Wands name: one noble door opens (a dinner, a servants' entrance or a steward's ear) | Notable Figures page |" — "heir's circle" has no source in the files. Check before any Background uses it.
- `.claude/skills/character-voices/SKILL.md:23`: lists Torlyn with the Black Tears. Matches.

**E2. Routed quest references (quest-time)**
- `campaign/quests/faction-events/lords-alliance/r10-stingblade/ev-01-stingblade.md:123` and `:139`; `design-notes.md:25`
- `campaign/guides/factions/03-lords-alliance.md:68` (Stingblade rank benefit)
- `campaign/guides/trollskull-manor/06-tavern-time.md:32` (Kythorn row) and `:92` (Renaer's Friends)
- `sources/Appendix_D_-_Running_the_Tavern.md:1138`; Addendum PDF printed p.185

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]`.

1. **Birth, age, upbringing.** No source. Stay consistent with: a noble-house child, "trained since childhood" (`10-lord-torlyn-wands.md:23`), and no date in any file.
2. **His father.** Campaign: "Lord Wands's son" (`10-lord-torlyn-wands.md:15`). No name. A father can be a nameless `[design]` figure. Do not name a new Notable Figure. Do not identify the father with Maskar Wands (`wiki.txt:1073`) without a ruling.
3. **Training.** Campaign: "trained since childhood" and "disciplined precision" (`10-lord-torlyn-wands.md:23`). No school, master or city institution is named. The house's "strong history of magic within the city" (`wiki.txt:1052`) is the only background for it.
4. **How he came to Renaer's circle.** No day-one source. Campaign: "Renaer's circle is the one place no one asks him to open it" (`10-lord-torlyn-wands.md:21`). The Stingblade introduction is quest-time (E2).
5. **A home or villa.** Wiki gives a Wands villa in the North Ward "at the corner of [[Shando Street]] and the [[Magecourt]]" (`wiki.txt:1055`). The campaign's North Ward gazetteer does not place it (`north-ward.md:183`). Use only as `[research]`.
6. **Family history.** The 1370 DR scarab embarrassment (`wiki.txt:1073`) and the founder Eldrus, who was a Magister from 409 to 516 DR (`wiki.txt:116`). Wiki only. Use as `[research]` if used at all.
7. **Ethnicity.** "Illuskan human" (page L5) has no source. Keep as the page states it.
8. **Personal goals.** The only goals in any file: "Torlyn wants to be Renaer's friend rather than Lord Wands's son, practice his magic without political entanglement, and keep the Wands family's reputation intact without becoming its servant." (`10-lord-torlyn-wands.md:15`).

---

## G. Inner-life hints in the sources (exact quotes)

- **The name.** "Deep down, he carries the Wands name like luggage he cannot put down, and Renaer's circle is the one place no one asks him to open it." — `10-lord-torlyn-wands.md:21`
- **Stubbornness.** "Torlyn most often feels relaxed confidence, dry amusement, protective pride in the Wands legacy, private stubbornness about living on his own terms, and honest pleasure in low-stakes company." — `10-lord-torlyn-wands.md:13`
- **Goals.** "Torlyn wants to be Renaer's friend rather than Lord Wands's son, practice his magic without political entanglement, and keep the Wands family's reputation intact without becoming its servant." — `10-lord-torlyn-wands.md:15`
- **Voice, personality.** "**Personality in speech:** Dry amusement and stubbornness about living on his own terms. He's proud of his family's legacy but won't serve it, and the tension shows in short answers." — `independents-allies.md:199`
- **Voice, quirk.** "**Quirks:** He lights pipes with cantrips. He changes the subject when "Lord Wands" is used." — `independents-allies.md:200`
- **Voice, signature.** "**Signature phrases:** "Just Torlyn." / "The Wands can manage without me." / "Another round?"" — `independents-allies.md:201`
- **Voice, never.** "**Never:** He never pulls rank, never discusses family business, and never misses a round at Trollskull." — `independents-allies.md:202`
- **Voice, swearing sample.** "Casual and dry among friends ("Galas are shit, and I've been to all of them."). Polished at court." — `independents-allies.md:198`
- **Morale.** "He has been trained since childhood and fights like it, but he would rather talk his way out." — `10-lord-torlyn-wands.md:23`
- **Wiki, the house's grief.** "In [[1370 DR]], the Wands family suffered a public embarrassment when Marcus Wands stole the family heirloom ..." — `wiki.txt:1073` (`[research]` only; the full sentence is in A2)
