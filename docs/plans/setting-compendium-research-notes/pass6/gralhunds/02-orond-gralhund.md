# Pass 6 research notes: Orond Gralhund

Page: `campaign/setting/notable-figures/gralhunds/02-orond-gralhund.md`
Companion notes: `docs/plans/setting-compendium-research-notes/pass6/gralhunds/01-yalah-gralhund.md` (same house, same sources; Yalah's notes hold the shared quotes in full, and this file repeats only what Orond needs)
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Orond is a major NPC (brief ruling 2): full Personality and Connections apply.
Organization page: `campaign/setting/organizations/12-house-gralhund.md`
Factions Guide: `campaign/guides/factions/13-house-gralhund.md`
Voice profile: `.claude/skills/character-voices/voices/gralhunds.md` (`### Orond Gralhund`, lines 25-39)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes (`\"`) are shown as plain quotes. `{@creature ...}` and similar tags are left as written. The `page` field is given where the entry has one.
- Wiki: the scratchpad extract `wiki-gralhunds/02-orond-gralhund.txt` is cited as "wiki extract line N". The same page is in `sources/research/pass5-bundles/gralhunds/wiki.txt` at lines 91 to 180 (cited as "wiki bundle line N"). The wiki prints no edition on most sentences. The infobox refs (`WDH5e-p213-214`, 5e) give the edition; inferred.
- Alexandrian PDFs were read as page images (no shell, no `pdftotext`): `sources/4. Gralhund Villa.pdf` (10 PDF pages = printed pp. 26 to 35) and `sources/2. Other Factions.pdf` (3 PDF pages = printed pp. 20 to 22). Every PDF quote is a transcription from the image and is marked **PDF transcription**. Each needs a `pdftotext -layout` check before it goes into prose.
- Alexandrian markdown: `sources/Act_III_Arc_E.md` (HTML `<p>` text is quoted without the tags; the number is the markdown line).
- Quest journal and location lines are cited by file and line as Grep returned them. Quest-time lines are routed, not reproduced in full.
- `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **The Morale line is a quest scene with a dice rule.** `02-orond-gralhund.md:23` gives "He breaks under a DC 10 Intimidation check" and "He throws himself at the mercy of the first person to bust through his barricade." Both come from the Guest Suite scene (`sources/adventure-wdh.json:5961` to `:5962`; `campaign/quests/act-ii/gralhund-villa/ev-05-the-guest-suite.md:41`). The habit ("barricades himself behind furniture and cowers") is day-one (`campaign/setting/organizations/12-house-gralhund.md:34`). Restate the habit; route the check (section C, row O9).
2. **The Resonance line depends on a discovery.** `02-orond-gralhund.md:11` says "when the party discovers the secret he carries literally on his body". The tail is a day-one fact (`sources/adventure-wdh.json:32448`). No campaign line says the party discovers it. Restate the Resonance as a day-one image (section C, row O4).
3. **Orond's stat label is "Noble", and the adventure says "with these changes".** `02-orond-gralhund.md:5` says "Stat block: **Noble**." `sources/adventure-wdh.json:32455` says "is a Tethyrian human noble, with these changes:". Yalah's page says "Noble (with modifications)". See D1.
4. **Cult membership is open for Orond.** The adventure says "Lord and Lady Gralhund are both secret members" (`sources/adventure-wdh.json:6010`). The campaign's Secret says Orond "does not know the cult's name or its leader" (`campaign/setting/organizations/12-house-gralhund.md:110`), and the Villa journal has him say the same (`ev-05-the-guest-suite.md:47`, quest-time). The Background must pick a side or leave the choice to the orchestrator (D3).
5. **The Overview and the Persona are day-one and within limit.** The Overview's first sentence is 21 words (`02-orond-gralhund.md:29`); the second is 17. Nothing in the Overview is quest-time.

---

## A. Background facts by theme

### A1. Origin, the tail, and the family's tiefling line

**Adventure, Orond Gralhund (page 213)**
> "Although he is human, Orond was born with a tiefling's tail. The tail was amputated when he was a young boy, but the scar on his backside remains."
> — `sources/adventure-wdh.json:32448`

**Wiki extract, Description (5e, citing WDH5e-p213-214)**
> "Orond was short with a stocky build, but he was good-looking and well-dressed. He was born with a [[tiefling]]'s tail but it was removed when he was a boy."
> — wiki extract line 65

**Organization page, Secret (campaign; a GM Secret callout)**
> "- **The devil-blood:** The family chronicle records an ancestor's pact with a devil and the Infernal bloodline behind Orond's tail. Orond is human, born with a tiefling's tail that was amputated when he was a boy, and the scar remains. Opening the chronicle's lock without Yalah's brass key releases three specters."
> — `campaign/setting/organizations/12-house-gralhund.md:109`

**Adventure, Gralhund Villa chronicle (page 53)**
> "Of particular note is the little-known fact that the Gralhunds forged pacts with devils in years past, giving rise to a strain of tieflings. All such members of the house were sent to live on a Gralhund estate in Yartar, a city far to the north (or so the book claims in its epilogue), and there are passing references to some Waterdavian family members having been born with tails."
> — `sources/adventure-wdh.json:5877`

**Campaign, Gralhund Villa location (the chronicle in G12)**
> "The tome is the **Gralhund family chronicle**: tiefling lineage, an ancestor's pact with a devil, an amputated tail, the Infernal bloodline that produced Orond's scar. This is lore rather than leverage, but it contextualizes the Asmodean compartment in G16."
> — `campaign/locations/gralhund-villa/g12-family-library.md:5`

The chronicle's date range and the 1260 DR founding are the same as the Yalah notes (A1; D14 there).

### A2. Patriarch, title and role in the house

**Adventure, Orond Gralhund (page 213)**
> "Orond is the patriarch, but he's not a quick-thinking or cultured sort-and deep down, he knows it. He leaves most of the plotting and socializing to his wife, {@creature Yalah Gralhund|wdh|Yalah}, to whom he is devoted."
> — `sources/adventure-wdh.json:32443`

**Adventure, Orond Gralhund (page 213), the title in the published text**
> "When several of the Masked Lords were assassinated in quick succession some years ago, Lord Gralhund had expected his wife to fill one of the vacancies."
> — `sources/adventure-wdh.json:32444` (the same entry calls him "Lord Gralhund"; the Gralhund Villa scene uses "Lord Gralhund" throughout, `:5962`)

**Organization page, Key Members (campaign)**
> "- **Orond Gralhund** — Tethyrian human noble, neutral evil, he/him. Patriarch of the house, a short, stocky man who dresses well and shows a boorish side whenever he believes himself unobserved. See the **Orond Gralhund** page in Notable Figures."
> — `campaign/setting/organizations/12-house-gralhund.md:85`

**Organization page, Beliefs (campaign)**
> "- **The Wife Runs the House:** Orond is the patriarch and the face of the family. He leaves the plotting and socializing to Yalah, to whom he is devoted and of whom he is afraid, and Yalah manages him more than she loves him."
> — `campaign/setting/organizations/12-house-gralhund.md:35`

**Debts of the City, GM Guide (the public face)**
> "Her husband Orond manages appearances; she manages the house."
> — `campaign/guides/gm-guide/debts-of-the-city.md:76`

**Alexandrian, Act III Arc E (markdown; the visitor rule in the villa text; not adopted as a day-one fact)**
> "Which of them comes depends on the stated purpose of the visit; Yalah handles anything political or financial, Orond handles anything related to the household's physical operations or legal matters."
> — `sources/Act_III_Arc_E.md:209` (inside the paragraph headed "**Meeting the Gralhunds:**")

### A3. The grievance over the seat

**Adventure, Orond Gralhund (page 213)**
> "After she was passed over, Orond became insanely angry, and he has remained that way ever since."
> — `sources/adventure-wdh.json:32444`

**Wiki extract, History (5e, citing WDH5e-p213-214)**
> "When in [[1491 DR]] many members of the [[Lords of Waterdeep]] were killed in a [[Death Masks|nefarious plot]], Orond expected that his wife would fill one of the vacancies but that never happened, despite all the bribes and promises. Orond became deeply angry about this."
> — wiki extract line 71

**Organization page, Beliefs (campaign)**
> "- **A Slight Is Remembered:** Yalah's earlier bids for a seat were thwarted, and she feels banked fury at the Lords who passed her over. The vault's gold is her last best chance. Orond shares the anger and also hopes that her appointment will raise him."
> — `campaign/setting/organizations/12-house-gralhund.md:33`

**Campaign, History 07 (the Lords' murders, Orond's anger)**
> "- The published adventure says several Masked Lords were assassinated in quick succession some years ago. Yalah Gralhund had expected a vacancy and was passed over, and Orond has been angry ever since."
> — `campaign/setting/history/07-a-city-watching-itself.md:69`

The date of the killings is settled to keep both dates (`campaign/setting/history/07-a-city-watching-itself.md:128`; see the Yalah notes D13).

### A4. The Zhentarim alliance and what Orond knew

**Adventure, Orond Gralhund (page 213)**
> "Orond doesn't fully grasp how entwined the Black Network and his family have become-it is now next to impossible to separate one from the other. It's no secret in Waterdeep that the Black Network has firmly rooted itself in House Gralhund. But what's not generally known is that the Zhents in House Gralhund are agents of {@creature Manshoon|WDH}. Neither Orond nor any other member of his family knows about the wizard's clone. As far as Orond and his wife are concerned, the local leaders of the Black Network (with {@creature Urstul Floxin|wdh} chief among them) reside with them in the family villa."
> — `sources/adventure-wdh.json:32446`

**Wiki extract, History (5e, citing WDH5e-p213-214)**
> "Orond was approached by some [[Zhentarim]] loyal to [[Manshoon]] and they formed an alliance. The Zhent gained the coin and the resources of the Gralhunds for their operations in the city and in exchange granted to Orond all the information about the Masked Lords they could find."
> — wiki extract line 73 (the wiki says the approach was to Orond; see D7)

**Organization page, GM Notes (campaign)**
> "- **What the house does not know:** Neither Yalah nor Orond knows that Manshoon is the Zhentarim's true master, and Orond does not fully grasp how entangled his family has become with the Black Network."
> — `campaign/setting/organizations/12-house-gralhund.md:101`

**Organization page, Timeline (campaign)**
> "- **The year before Ches 1, 1492 DR:** Agents of Manshoon's Zhentarim approached the Gralhunds, and the two sides formed an alliance. The house gives the Zhentarim coin and the use of the villa as a refuge, and it receives the Black Network's intelligence in return, including what the Zhentarim learn about the Masked Lords. The wiki places the alliance in 1492 DR (Forgotten Realms Wiki, *Gralhund*, 5e)."
> — `campaign/setting/organizations/12-house-gralhund.md:23`

### A5. The household's day, and the rooms he uses

**Adventure, Orond Gralhund (page 213)**
> "Orond relies on Yalah to manage the Zhentarim. He spends his days watching mercenaries train, paying bills, and ranting about the cost of doing business in the city."
> — `sources/adventure-wdh.json:32448`

**Organization page, Structure (campaign)**
> "- **Arms and Hired Swords Are the Trade:** The house contracts mercenaries and manufactures weapons. Orond spends his days watching mercenaries train, paying bills and complaining about the cost of doing business in Waterdeep."
> — `campaign/setting/organizations/12-house-gralhund.md:37`

**Wiki extract, Activities (5e, citing WDH5e-p213-214)**
> "Orond seemed to spend most of his time watching mercenaries as they trained, paying bills,  and complaining about the cost of doing business in Waterdeep."
> — wiki extract line 68 (the double space after "bills," is in the source)

**Campaign, Gralhund Villa location G10 (the den)**
> "**Unoccupied in both states.** The den is used for after-dinner smoking and Orond's occasional conversation with his business partners, but neither is scheduled during this quest."
> — `campaign/locations/gralhund-villa/g10-den.md:9` (the partners are not named in any source)

**Campaign, Gralhund Villa location G11 (the study)**
> "Locked (DC 15 thieves' tools or ring of keys). A working office, not a reading room — Orond reads in G12. The study holds a 10-foot wrestling mat against the south wall (Orond's morning exercise, apparently), two velvet armchairs, and mahogany bookshelves covering the east wall floor-to-ceiling."
> — `campaign/locations/gralhund-villa/g11-oronds-study.md:3`

**Campaign, Gralhund Villa location G12 (the library, day state)**
> "**Day state only — Lord Orond Gralhund:** Orond is in this room during the day, reading in the wolf-skin chair, a glass of amber spirits on the side table beside him. For his social encounter behavior, refer to the **Daytime Infiltration** Event (ev-03)."
> — `campaign/locations/gralhund-villa/g12-family-library.md:19`

**Alexandrian, Act III Arc E (markdown, the G11 room description)**
> "Orond reads here most mornings."
> — `sources/Act_III_Arc_E.md:272` (the same markdown calls the room "Orond's Study"; see D5 for the conflict with `g11-oronds-study.md:3`)

**Alexandrian, 4. Gralhund Villa.pdf, printed p.30 (G12, PDF transcription)**
> "Area G12 – Library: Orond was studding A Missive from Castle Ward. He leaves it laying on the arm of one of the library's chairs if disturbed (by, for example, a Zhentarim strike team breaking into this house)."
> — `sources/4. Gralhund Villa.pdf` PDF p.5 (printed p.30). **PDF transcription.** The Alexandrian's word is "studding"; it reads as a typo for "studying".

**Campaign, Gralhund Villa location G08 (the family portrait)**
> "**Family portrait (south wall):** Oil on canvas, three feet by five feet. Lord Orond and Lady Yalah seated, three children standing (Zartan in front, Greth and Tomassin behind). A black-and-tan hound sits at Orond's feet. The hound died two years ago. No one has commissioned a replacement portrait."
> — `campaign/locations/gralhund-villa/g08-great-hall.md:7`

### A6. The journal of the Grand Game (the one private thing he keeps)

**Organization page, Methods (campaign)**
> "- **Hide the private papers:** Orond keeps a private journal of about 200 pages in a false-book compartment in his study, holding his own analysis of the Grand Game's faction leaders and their agents. Yalah wears the key to the chronicle's lock on a chain at her throat."
> — `campaign/setting/organizations/12-house-gralhund.md:61`

**Campaign, Gralhund Villa location G11 (the journal)**
> "**The False-Book Compartment (DC 15 Investigation):** On the main run of shelving, one section of false-book spines conceals a fitted compartment with a magnetic latch. The latch does not resist; it simply is not visible unless the party is looking for it. Inside: a leather-bound private journal, roughly 200 pages, in Orond's cramped hand."
> — `campaign/locations/gralhund-villa/g11-oronds-study.md:7`

**Campaign, Gralhund Villa location G11 (what the journal shows)**
> "This is the **Gralhund Study of the Grand Game** — Orond's personal running analysis of the six Grand Game faction leaders, their embedded agents, his deduction of the Three Eyes and the Stone, and his designation of code names for two informants inside Renaer Neverember's household (\"Eagle\" and \"Catoblepas\"). This is characterization rather than tactical intelligence; the party cannot weaponize it directly, but it confirms that Orond has been more active in the Grand Game than his frightened-library-reader persona suggests."
> — `campaign/locations/gralhund-villa/g11-oronds-study.md:9`

The "Three Eyes" deduction is part of the journal's content that the Factions Guide routes to **Gralhund Villa** (`campaign/guides/factions/13-house-gralhund.md:83` and `:89`; Yalah notes E3).

### A7. Hrabbaz, the bodyguard he keeps close

**Adventure, Orond Gralhund (page 213)**
> "When he must speak to strangers, he keeps his half-orc bodyguard {@creature Hrabbaz|WDH} close by, for fear that others might attack and rob him at any moment. While in Yalah's presence, Orond becomes an altogether different person: quiet, almost timid, and happy to let his wife have the spotlight."
> — `sources/adventure-wdh.json:32447`

**Organization page, Retainers (campaign)**
> "- **Retainers:** Hrabbaz guards both Gralhunds and is more loyal to Yalah. Hurv Taldred keeps the yard with two mastiffs, and the Gralhunds paid a necromancer to ritually change the three of them into shadows from sundown to dawn. Chirada works as an intelligence operative in the city."
> — `campaign/setting/organizations/12-house-gralhund.md:47`

(Hrabbaz's shared service is D2.)

### A8. The Renaer seizure (the day-one fact; the confession is quest-time)

**Organization page, Timeline (campaign)**
> "- **The night before Ches 1, 1492 DR:** Zhentarim agents seized Renaer Neverember on the night Floon Blagmaar was taken. The house paid for the operation, and Yalah arranged it to gain leverage over Dalakhar."
> — `campaign/setting/organizations/12-house-gralhund.md:26` (the bullet does not name Orond; the house is the subject)

**History 08 (the day-one fact, with a quest source)**
> "- The Gralhunds funded the Zhentarim seizure of Renaer Neverember to gain leverage over Dalakhar, according to Orond Gralhund, who says Yalah Gralhund arranged it. Source: **Gralhund Villa**, the guest suite."
> — `campaign/setting/history/08-the-players-arrive.md:58` (quest-time source; see E1)

**Adventure, Gralhund Villa, Orond's account (the content is the day-one fact; the telling is quest-time)**
> "\"House Gralhund has been bankrolling Black Network operations in Waterdeep, including the plot to kidnap {@creature Renaer Neverember|wdh} and the plot to steal the {@item Stone of Golorr|WDH} from his father's gnome spy, Dalakhar.\""
> — `sources/adventure-wdh.json:5967` (the Guest Suite, `:5962` and `:5966` to `:5968`)

### A9. The nimblewright in his study

**Organization page, Structure (campaign)**
> "- **The nimblewright:** The household nimblewright is NW-02 in Jarlaxle's ledger, which names the buyer as O. Gralhund of Saerdoun Street. It was built as a household model with combat programming. It stands dormant against the northeast corner of Orond's study and activates on any Alarm trigger or when Yalah speaks its command word from her bedroom."
> — `campaign/setting/organizations/12-house-gralhund.md:48`

**Organization page, History (campaign; the ledger's summary)**
> "- **Marpenoth 7, 1491 DR (year derived):** Jarlaxle's sale ledger records nimblewright NW-02 as sold to \"O. Gralhund of Saerdoun Street.\""
> — `campaign/setting/organizations/12-house-gralhund.md:22` (the ledger's own line is at `campaign/setting/history/08-the-players-arrive.md:40`; Yalah notes D6)

### A10. The Stone on Ches 1

**Organization page, Grand Game Agenda (campaign)**
> "On Ches 1 the Stone of Golorr sits in Xanathar's Guild's lair, and the Alexandrian text says the Gralhunds do not know that."
> — `campaign/setting/organizations/12-house-gralhund.md:92`

Orond has no day-one Stone fact beyond this. The Guest Suite's account of the Stone ("some kind of ancient creature transformed into an artifact") is quest-time (`sources/adventure-wdh.json:5966`).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, Summary: "> - *Tethyrian human noble, neutral evil, he/him*. Stat block: **Noble**." — `campaign/setting/notable-figures/gralhunds/02-orond-gralhund.md:5`
- Adventure: "Orond is neutral evil." — `sources/adventure-wdh.json:32459` (page 214, Game Statistics)
- Wiki extract: "| alignment5e    = [[Neutral evil]]" — wiki extract line 57 (5e)
- Agreement: all sources that give one say neutral evil.

**Species and ethnicity**
- Campaign, Summary: "*Tethyrian human noble*" (`02-orond-gralhund.md:5`). Campaign, key member list: "Tethyrian human noble, neutral evil, he/him" (`campaign/setting/organizations/12-house-gralhund.md:85`).
- Adventure: "{@creature Orond Gralhund|wdh} is a Tethyrian human noble, with these changes:" — `sources/adventure-wdh.json:32455`
- Adventure, human: "Although he is human, Orond was born with a tiefling's tail." — `sources/adventure-wdh.json:32448`
- Wiki: "| race           = [[Human]]" (wiki extract line 14) and "| ethnicity      = [[Tethyrian]]" (wiki extract line 15, no ref on the line)
- Agreement: human, Tethyrian. The tail is a human's trait from a tiefling line, not a tiefling's body.

**Pronouns**
- Campaign, Summary: "he/him" (`02-orond-gralhund.md:5`).
- Adventure: "Orond is the patriarch, but he's not a quick-thinking or cultured sort-and deep down, he knows it." (`sources/adventure-wdh.json:32443`) and "Orond relies on Yalah to manage the Zhentarim." (`:32448`).
- Wiki: "| sex            = Male" (wiki extract line 13).

**Stat block**
- Campaign, Summary: "Stat block: **Noble**." (`02-orond-gralhund.md:5`). This does not match the adventure (D1).
- Adventure, Game Statistics (page 214): "{@creature Orond Gralhund|wdh} is a Tethyrian human noble, with these changes:" followed by the list: "Orond is neutral evil." / "He has an Intelligence of 9 (-1)." / "Never one to bother learning other languages, he speaks only Common." — `sources/adventure-wdh.json:32455`, `:32459`, `:32460`, `:32461`. No CR, AC or HP is given in the adventure.
- Alexandrian, Stat Reference (PDF p.5, printed p.30): "Orond Gralhund – DH p. 213-4; noble, MM p. 348" — **PDF transcription**. No CR.
- Wiki infobox: "| occupation     = Noble<ref name="WDH5e-p213-214" />" (wiki extract line 16), "| challenge5e    = {{Frac|1|8}}" (line 58), "| class5e        = [[Noble]]" (line 59), "| refs5e         = <ref name="WDH5e-p213-214" /><ref name="MM5e-p348">{{Cite book/Monster Manual 5th edition|358}}</ref>" (line 60). The wiki's Monster Manual ref is named p348 but prints page 358 (see the Yalah notes D7).
- Intelligence and languages (for the drafter's consistency): "He has an Intelligence of 9 (-1)." (`sources/adventure-wdh.json:32460`); "Never one to bother learning other languages, he speaks only Common." (`:32461`); wiki: "| languages      = [[Common]]" (wiki extract line 19).

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/gralhunds/02-orond-gralhund.md`. The page has no Background, no Personality, no Connections and no Voice block yet.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| O1 | L5 | "> - *Tethyrian human noble, neutral evil, he/him*. Stat block: **Noble**." | Day-one name tag. Stat label conflicts with the adventure (D1) | Section B (`sources/adventure-wdh.json:32455`) |
| O2 | L6 | "> - **Affiliation:** House Gralhund" | Day-one. Matches the org page (`12-house-gralhund.md:85`, "Patriarch of the house") | `campaign/setting/organizations/12-house-gralhund.md:85` |
| O3 | L7 | "> - **Featured in:** **Gralhund Villa**, **Cassalanter Villa**" | Quest list. "Gralhund Villa" is the Villa journal. "Cassalanter Villa" has no Orond line in the Cassalanter folder (Grep: no match) | Route to quests. Verify the Cassalanter entry (D6) |
| O4 | L11 | "**Resonance.** Orond should inspire contempt with his boorish posturing, pity for the man who hides behind his wife and his bodyguard, and dark amusement when the party discovers the secret he carries literally on his body." | Day-one character, but "when the party discovers" is a quest discovery. The tail is day-one (`sources/adventure-wdh.json:32448`); the party's discovery of it is not written in any campaign journal (Grep found none) | Keep the tail as a day-one fact (A1). Restate the clause as a day-one image (ruling 3) |
| O5 | L13 | "**Emotions.** Orond most often feels inflated self-importance, impotent rage, fearful dependence on Yalah, paranoid suspicion of servants and visitors, petulant frustration at being passed over, and brief pathetic dignity when he attempts to assert authority." | Day-one. Keep | `sources/adventure-wdh.json:32447`; `12-house-gralhund.md:35`; wiki extract line 84 ("He was a little paranoid, always fearing attacks from strangers") |
| O6 | L15 | "**Motivations.** Orond wants to be the patriarch his title says he is, see Yalah appointed as a Masked Lord (which he believes will elevate him), and stop feeling afraid in his own home." | Day-one. Keep | `12-house-gralhund.md:33` ("Orond shares the anger and also hopes that her appointment will raise him.") |
| O7 | L17 | "**Inspirations.** When playing Orond, channel Joffrey Baratheon (*Game of Thrones*), Tobias Funke (*Arrested Development*), and Percy Wetmore (*The Green Mile*)." | Not a fact. Keep | n/a |
| O8 | L21 | "**Persona.** To the world, Orond is the patriarch of House Gralhund, a short, stocky man who dresses well and is easy on the eyes. To those who deal with him, his boorish nature, inflated ego, and despicable opinions about \"the common rabble\" emerge whenever Yalah is not present to quiet him. Deep down, he was born with a tiefling's tail (amputated as a boy; the scar remains), does not understand how entangled his family has become with the Black Network, and keeps Hrabbaz close for fear that others might attack and rob him at any moment." | Day-one. Keep. "short, stocky" conflicts with `sources/Act_III_Arc_E.md:216` (D4) | `sources/adventure-wdh.json:32447` ("his boorish nature, inflated sense of self-importance, fragile ego, and despicable opinions about \"the common rabble\" come to the fore"), `:32448` (tail), `:32446` (the Black Network) |
| O9 | L23 | "**Morale.** In a confrontation, Orond barricades himself behind furniture and cowers. He breaks under a DC 10 Intimidation check (with disadvantage if he fears Yalah is watching). He throws himself at the mercy of the first person to bust through his barricade." | **QUEST-TIME in the second and third sentences.** The first sentence is the day-one habit (org page). The DC 10 check and the mercy line are the Guest Suite scene. Restate the habit; route the check | Habit: `campaign/setting/organizations/12-house-gralhund.md:34` ("Orond barricades himself behind furniture and cowers."), `:103` ("He barricades himself behind furniture in a confrontation."). Scene: `sources/adventure-wdh.json:5961` (the barricade, p.54) and `:5962` (DC 10 Intimidation, disadvantage if Yalah can overhear). Villa journal: `campaign/quests/act-ii/gralhund-villa/ev-05-the-guest-suite.md:37` to `:41`. Location: `campaign/locations/gralhund-villa/g15-guest-suite.md:25` |
| O10 | L25 | "**Relationships.** Orond is the husband of Yalah Gralhund (devoted to her and terrified of her in equal measure), the employer of Hrabbaz (whom he barely controls), and a nobleman whose excessive boasting and temper tantrums vanish the moment his wife enters the room." | Day-one. "the employer of Hrabbaz" conflicts with the shared bodyguard (D2) | `12-house-gralhund.md:35` ("to whom he is devoted and of whom he is afraid"), `:47`; `sources/adventure-wdh.json:32447`; `campaign/setting/notable-figures/gralhunds/03-hrabbaz.md:25` |
| O11 | L29 | "Orond Gralhund is the patriarch of House Gralhund — a short, stocky man who dresses well and is easy on the eyes. His boorish nature and inflated opinions about the common rabble emerge readily when he believes himself unobserved." | Day-one. First sentence is 21 words (within the limit). "short, stocky" against Arc E:216 (D4) | `12-house-gralhund.md:85`; `sources/adventure-wdh.json:32447` |

**Voice profile, lines (`.claude/skills/character-voices/voices/gralhunds.md`, `### Orond Gralhund`, lines 25-39)**

- Line 26 (tagline): "*A pompous, frightened lord who blusters about \"the rabble\" when his wife isn't there to stop him.*" Day-one.
- Line 28 (Sound): "A loud, blustering voice that goes shrill when frightened and sulky when corrected." Day-one.
- Line 29 (Sentence shape): "Self-important declarations and complaints, and petulant questions (\"Do you know who I am?\"). With Yalah present, abrupt silence." Day-one.
- Line 30 (Word choice): "Snobbish and bigoted: \"the common rabble\", \"my house\", \"outrageous\". He calls servants \"you there\"." Day-one.
- Line 31 (Swearing): "*Casual · Colourful · Rant.* Petty, spiteful insults at the lower classes (\"filthy gutter-born rabble\"). They get shrill when he's frightened." Day-one. Swearing stays (adult table).
- Line 32 (Personality in speech): "Inflated importance over fear. He boasts until threatened, then hides behind Hrabbaz. His brief attempts at dignity collapse fast." Day-one as a habit. "hides behind Hrabbaz" matches the barricade habit; keep it as a habit, not as the Guest Suite scene.
- Line 33 (Quirks): "He checks where Hrabbaz is before speaking. He touches the small of his back, near the scar, when nervous." Day-one.
- Line 34 (Signature phrases): "\"Do you know who I am?\" / \"Rabble!\" / \"Hrabbaz!\"" Day-one.
- Line 35 (Never): "He never admits to fear, never mentions his tail, and never contradicts Yalah to her face." Day-one.
- Lines 37 to 39 (Sample lines): "Who let you in? This is House Gralhund, not a public tavern, you rabble." / "My wife handles the, ah, particulars. I'm the lord. Obviously." / "Hrabbaz! Hrabbaz, do something! I'm the lord of this house!" Day-one as habits. The third is said under threat; the drafter should use it as a general "under pressure" line, not as the Guest Suite's line.

No quest-time clause is in the Orond voice profile. The tail and the scar appear there as day-one facts.

---

## D. Conflicts

**D1. Stat block label**
- Campaign Summary (Orond): "> - *Tethyrian human noble, neutral evil, he/him*. Stat block: **Noble**." (`02-orond-gralhund.md:5`)
- Campaign Summary (Yalah): "> - *Tethyrian human noble, neutral evil, she/her*. Stat block: **Noble (with modifications)**." (`01-yalah-gralhund.md:5`)
- Adventure: "{@creature Orond Gralhund|wdh} is a Tethyrian human noble, with these changes:" (`sources/adventure-wdh.json:32455`)
- Higher rank: the adventure. Orond's Summary should read "Noble (with modifications)" like Yalah's, or the difference must be a deliberate choice for the orchestrator.

**D2. Hrabbaz: shared or the employer's bodyguard**
- Orond Relationships: "the employer of Hrabbaz (whom he barely controls)" (`02-orond-gralhund.md:25`)
- Yalah Relationships: "the commander of Hrabbaz (her bodyguard, more loyal to her than to Orond)" (`01-yalah-gralhund.md:25`)
- Adventure: "Yalah shares the services of a half-orc bodyguard with her husband, although {@creature Hrabbaz|WDH} (see \"{@creature Hrabbaz|WDH}\") is more loyal to her than to him." (`sources/adventure-wdh.json:32782`)
- Adventure, Hrabbaz entry: "{@creature Hrabbaz|wdh} is a muscle-bound half-orc with a cleft palate who serves the lord and lady of House Gralhund as a bodyguard." (`sources/adventure-wdh.json:32140`)
- Hrabbaz page: "**Relationships.** Hrabbaz is the bodyguard of both Gralhunds (shared, though more loyal to Yalah), and a half-orc whose impeccable manners and wardrobe make him the most unsettling presence in a villa full of Zhentarim." (`campaign/setting/notable-figures/gralhunds/03-hrabbaz.md:25`)
- Higher rank: the adventure and the Hrabbaz page (shared service). Write "the bodyguard of both Gralhunds" on Orond's page.

**D3. Cult membership: is Orond a member?**
- Adventure: "Lord and Lady Gralhund are both secret members of a cult of Asmodeus worshipers popular among select nobles in Waterdeep. The cult is led by Lord {@creature Victoro Cassalanter|WDH} (see {@adventure appendix B|WDH|12}), though the Gralhunds won't divulge this information willingly." (`sources/adventure-wdh.json:6010`)
- Alexandrian, Act III Arc E (markdown): "Only Orond, under significant pressure and with genuine belief that Yalah cannot hear him, will confirm there is a cult. He does not know who leads it. Yalah has never told him, and he has been wise enough not to ask." (`sources/Act_III_Arc_E.md:34`). The same section names Yalah as a member (`:32`) and Hurv Taldred (`:35`). Orond is not named as a member.
- Alexandrian, villa roster text (markdown, not adopted): "There is a religious cult involved — he does not know its name, does not know its leaders. Yalah has never told him and he has been wise enough not to ask." (`sources/Act_III_Arc_E.md:649`)
- Villa journal (quest-time, the confession): "**3. A religious affiliation.** He does not know its name, does not know who leads it. There are symbols in a trunk in the master bedroom. He has never opened it. \"I have been wise enough not to ask.\"" (`campaign/quests/act-ii/gralhund-villa/ev-05-the-guest-suite.md:47`)
- Campaign, org Secret: "Orond knows that the trunk holds symbols and has never opened it, and he does not know the cult's name or its leader." (`campaign/setting/organizations/12-house-gralhund.md:110`). The same callout's first sentence: "The Gralhunds therefore belong to the same Asmodean cult as the Cassalanter household."
- Campaign, Victoro page: "- **Yalah Gralhund** and **Hurv Taldred:** Members of the cult from House Gralhund." (`campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:57`). Orond is not named.
- Campaign, G16: "This is the first physical evidence that the Gralhunds and the Cassalanters are members of the same Asmodean cult." (`campaign/locations/gralhund-villa/g16-master-bedroom.md:14`)
- Higher rank: the campaign (org Secret and Victoro page) for what Orond knows: symbols in a trunk, no name, no leader. Whether he is a member is not settled by any campaign file. The adventure says he is. The Background must not state membership until the orchestrator decides. Any version obeys the Cassalanter secrecy rule.

**D4. Physical description**
- Campaign Overview and Persona: "a short, stocky man who dresses well and is easy on the eyes" (`02-orond-gralhund.md:21`, `:29`); adventure: "Orond is a short, stocky man who dresses well and is easy on the eyes." (`sources/adventure-wdh.json:32447`); wiki: "Orond was short with a stocky build" (wiki extract line 65).
- Alexandrian, Act III Arc E (markdown, Orond's arrival in the front room): "A broad-shouldered man in a well-cut coat enters with the careful confidence of someone who has decided in advance not to be surprised by anything today." (`sources/Act_III_Arc_E.md:216`, inner text of a `<p>`)
- Higher rank: the campaign and the adventure (short, stocky). The Alexandrian's "broad-shouldered" is a physical conflict to flag for the user.

**D5. Where he reads**
- Campaign, G11 location: "A working office, not a reading room — Orond reads in G12." (`campaign/locations/gralhund-villa/g11-oronds-study.md:3`)
- Campaign, G12 location: "Orond is in this room during the day, reading in the wolf-skin chair" (`campaign/locations/gralhund-villa/g12-family-library.md:19`)
- Alexandrian, Act III Arc E (markdown): "Orond reads here most mornings." (`sources/Act_III_Arc_E.md:272`, in the G11 room description, which calls the room "Orond's Study")
- Higher rank: the campaign location journal (G11 is a study; G12 is the reading room). The Background should say "the library" for reading and "the study" for the journal and the wrestling mat. The Alexandrian's "here" conflicts.

**D6. "Featured in: Cassalanter Villa"**
- Summary: "> - **Featured in:** **Gralhund Villa**, **Cassalanter Villa**" (`02-orond-gralhund.md:7`).
- Grep of `campaign/locations/cassalanter-villa/` for Orond: no match. Grep of `campaign/structure/arc-g-cassalanter-villa.md` for Orond: no match. The one Cassalanter line that names the house is "Inform Y.G." (`campaign/locations/cassalanter-villa/03-reading-room.md:14`), which is Yalah's initials only.
- Higher rank: no source. Route or remove the Cassalanter entry on the Summary. The orchestrator decides.

**D7. Who was approached by the Zhentarim**
- Wiki extract line 73: "Orond was approached by some [[Zhentarim]] loyal to [[Manshoon]] and they formed an alliance."
- Adventure: "Less than a year ago, the Gralhunds were approached by agents of the Zhentarim loyal to {@creature Manshoon|WDH}, and the nobles formed an alliance with them." (`sources/adventure-wdh.json:32445`)
- Organization page: "- **The year before Ches 1, 1492 DR:** Agents of Manshoon's Zhentarim approached the Gralhunds, and the two sides formed an alliance." (`campaign/setting/organizations/12-house-gralhund.md:23`)
- Higher rank: the adventure and the org page (the house, not Orond alone). The wiki's "approached ... Orond" is the wiki's version and ranks last.

**D8. Intelligence (the persona against the act)**
- Wiki extract line 84: "Orond was not smart or intelligent and deep down he knew this."
- Adventure: "He has an Intelligence of 9 (-1)." (`sources/adventure-wdh.json:32460`)
- Adventure: "he's not a quick-thinking or cultured sort-and deep down, he knows it." (`sources/adventure-wdh.json:32443`)
- Campaign G11: "it confirms that Orond has been more active in the Grand Game than his frightened-library-reader persona suggests." (`campaign/locations/gralhund-villa/g11-oronds-study.md:9`)
- Higher rank: all agree he is not clever by his own measure. The journal is not a source conflict; it is the persona against the act. Keep both: he knows he is not clever and he keeps a journal anyway. Do not make him clever.

---

## E. Stale lines in other files (not to be edited) and routed quest references

**E1. Quest-time or stale lines in setting and guide pages (report only)**
- `campaign/setting/history/08-the-players-arrive.md:58`: "- The Gralhunds funded the Zhentarim seizure of Renaer Neverember to gain leverage over Dalakhar, according to Orond Gralhund, who says Yalah Gralhund arranged it. Source: **Gralhund Villa**, the guest suite." (a setting page whose source is a quest scene)
- `campaign/gazetteer/waterdeep/north-ward.md:68` gives "their two children" for the couple (the org page and the adventure give three; see the Yalah notes D15).
- `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:52` (quest-time, see the Yalah notes E1).
- `docs/plans/setting-compendium-pass6-drafter-instructions.md:24` lists the Gralhund pages with quest-time risk ("Chirada and Hurv Taldred (`gralhunds`), Yalah (`01-yalah-gralhund.md:21`)"). Orond is not named there; O4 and O9 are the Orond rows.

**E2. Event Outcomes that Orond's page must not use before Ches 24**
- "**Orond Confession Heard**" (`campaign/quests/act-ii/gralhund-villa/ev-03-daytime-infiltration.md:106`; `ev-05-the-guest-suite.md:57`). Factions Guide: "Orond's confession (**Gralhund Villa**, Daytime Infiltration, The Front Door or The Guest Suite; marks **Orond Confession Heard**)." (`campaign/guides/factions/13-house-gralhund.md:88`)
- "**Yalah Missing**" and "**Yalah In Custody**" (`campaign/guides/factions/13-house-gralhund.md:23`), which change Orond's state: "Orond is in shock and makes no move." (`13-house-gralhund.md:26`)

**E3. Orond's quest-time lines (routed to Gralhund Villa; the day-one page must not restate them)**
- `campaign/quests/act-ii/gralhund-villa/ev-03-daytime-infiltration.md:128`: "The party entered Gralhund Villa during the day. The estate was guarded and operational, Lady Yalah upstairs with the Stone. Lord Orond was in the library."
- `ev-05-the-guest-suite.md:37`: "The wardrobe has been pushed against the door from inside. Behind it: overturned furniture, Orond's evening coat torn at the shoulder, and Lord Orond Gralhund himself backed against the far wall with a fireplace poker in both hands and the whites of his eyes showing. When the door opens and the party is not Floxin, the grip goes slack."
- `ev-05-the-guest-suite.md:39`: "He will not fight. The kind of coward who has decided money means he doesn't have to be brave, and tonight has thoroughly tested that theory."
- `ev-05-the-guest-suite.md:41`: "Under **DC 10 Intimidation** (Disadvantage if he has any reason to believe Yalah can hear him through the wall), he confirms:"
- `ev-05-the-guest-suite.md:43`: "**1. The Stone of Golorr.** An ancient creature transformed into an artifact; it holds the location of a hidden vault somewhere beneath Waterdeep containing half a million gold dragons. He does not know how to open it, and knows nothing of the Eyes."
- `ev-05-the-guest-suite.md:45` and `:49` (the fireball and the Renaer funding): quoted in the Yalah notes E3.
- `ev-05-the-guest-suite.md:51`: "**Orond as leverage in G16.** If the party brings Orond upstairs when they approach Lady Yalah, she will surrender the Stone without a Charisma check; no negotiation required. Hrabbaz will stand down if she looks at him first. This is the fastest resolution path in this quest."
- `ev-06-the-gralhund-confrontation-day.md:37`: "**Family.** Yalah is first and last a mother. If the party has Orond in custody, or makes it credibly clear that Zartan or Greth are in immediate danger" (the Yalah notes E3 has the full sentence).
- `ev-07-the-gralhund-confrontation-night.md:39`: "**Family.** Yalah is first and last a mother. If the party has Orond in custody, she recognizes him the moment she sees him."
- `campaign/locations/gralhund-villa/g15-guest-suite.md:25`: "**Night state:** **Lord Orond Gralhund** is barricaded inside (wardrobe + desk + chair pressed against the door from the inside). He's backed against the far wall with a fireplace poker in both hands and the whites of his eyes showing. For his behavior and the four revelations he will confirm under pressure, refer to the **The Guest Suite** Event (ev-05)."
- `campaign/locations/gralhund-villa/area-overview.md:68` ("| G12 (Family Library) | Lord Orond Gralhund |") and `:81` ("| G15b | Lord Orond Gralhund (barricaded) | Behind wardrobe + desk + chair |").
- `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:44`: "Lord Gralhund is in shock." (the full sentence is in the Yalah notes E3).
- Alexandrian (`sources/Act_III_Arc_E.md`, quest-time, not adopted): "Lord Orond, reading late in G12, hears the noise, opens the library door, locks eyes with Floxin in the hall below, and runs for the stairs." (`:397`); "The study door stands ajar. Inside, the wrestling mat and the mahogany desk and the ornamental bookshelves are exactly as they should be, except that one of the armchairs has been knocked over — Orond, in his hurry to flee when the fighting began below, overturned it getting to the door." (`:544`, inner text of a `<p>`); "The library is exactly as Orond left it in his hurry — a reading chair overturned, the evening's tea cold in its cup beside the hearth." (`:556`)
- Alexandrian PDF, printed p.33 (quest-time): "Lord Orond emerges from the Library (G12), where he's been studying late." (**PDF transcription**, `sources/4. Gralhund Villa.pdf` PDF p.8). Printed p.34: "Lord Orond is dragged into G16 and Fel'rekt negotiates with Lady Yalah through the door." (**PDF transcription**, PDF p.9). Printed p.31: "If a peaceful approach is being taken, successful Charisma checks may allow PCs to meet with Lord Orond." (**PDF transcription**, PDF p.6)

**E4. Orond's Morale and the confrontation (routed)**
- `sources/adventure-wdh.json:5961`, `:5962`, `:5966` to `:5968` (quest-time mechanics and the confession text).
- `campaign/quests/act-ii/gralhund-villa/ev-05-the-guest-suite.md:41` (the DC 10 check, quoted at E3).

**E5. Routed to the Factions Guide (mechanics)**
- `campaign/guides/factions/13-house-gralhund.md:26`: "- **Yalah In Custody, or dead.** Nobody gives orders. Orond is in shock and makes no move. Chirada works alone as a team of one, tracking whoever holds the Stone and the Eye she believes the Zhentarim took."
- `campaign/guides/factions/13-house-gralhund.md:88`: "- Orond's confession (**Gralhund Villa**, Daytime Infiltration, The Front Door or The Guest Suite; marks **Orond Confession Heard**). He confirms what the Stone is, that Yalah sent the nimblewright on Ches 22, that symbols of a religious affiliation lie in a trunk in the master bedroom, and that the house funded the Zhentarim agents who seized Renaer."

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

**F1. Birth year, age, home town, parents, childhood.** No source gives any of these. The wiki's infobox fields `age`, `dob`, `parents` and `siblings` are blank (wiki extract lines 17, 21, 29 and 31). The only age cue is that he has adult children (`campaign/setting/organizations/12-house-gralhund.md:45`; `sources/adventure-wdh.json:6038`). Do not give a birth year. He is a Tethyrian human; no birthplace is given.

**F2. The tail's amputation.** The adventure says "The tail was amputated when he was a young boy" (`sources/adventure-wdh.json:32448`). No source gives the surgeon, the place, the reason or the family's reaction. The chronicle says there are "passing references to some Waterdavian family members having been born with tails" (`:5877`). Any account of the operation is `[design]`, and it must not tie the amputation to the cult or the Stone (the cult is a Secret).

**F3. How he became the patriarch, and why the title is his.** The sources say he "is the patriarch" (`sources/adventure-wdh.json:32443`) and "Orond is the patriarch and the face of the family" (`12-house-gralhund.md:35`). No source says whether he inherited the title, from whom, or when.

**F4. How he met Yalah and why he is devoted to her.** No source. "He leaves most of the plotting and socializing to his wife ... to whom he is devoted." (`:32443`) and "to whom he is devoted and of whom he is afraid" (`12-house-gralhund.md:35`). Any history is `[design]`.

**F5. The source of his fear of strangers and his paranoia.** The sources state the fear and the habit (`:32447`, "for fear that others might attack and rob him at any moment"; wiki extract line 84, "He was a little paranoid, always fearing attacks from strangers"). No source gives a cause. A cause is `[design]` and must not add a plot fact (an attack, a robbery) that needs a new quest event.

**F6. The hound.** "A black-and-tan hound sits at Orond's feet. The hound died two years ago." (`campaign/locations/gralhund-villa/g08-great-hound.md:7`; the file is `g08-great-hall.md`). No name, breed history or death is given. A name is `[design]`; it must not name a new Notable Figure.

**F7. Orond's business, his partners and his mercenaries.** "his business partners" (`campaign/locations/gralhund-villa/g10-den.md:9`) and "watching mercenaries train, paying bills" (`sources/adventure-wdh.json:32448`). No partner is named. Do not name one (ruling 17: no new Notable Figure).

**F8. The journal's author.** The journal is "in Orond's cramped hand" (`campaign/locations/gralhund-villa/g11-oronds-study.md:7`) and holds "Orond's personal running analysis of the six Grand Game faction leaders" (`:9`). His intelligence is 9 (`sources/adventure-wdh.json:32460`), and the wiki and the adventure say he knows he is not clever (D8). How he learned the analysis is not given. The drafter must not make him the cleverest person in the house.

**F9. His own grief.** The only sourced loss to Orond is the hound (F6) and the passing over of his wife for a seat: "After she was passed over, Orond became insanely angry, and he has remained that way ever since." (`:32444`). No death, no child's death, no friend. Any further loss is `[design]`.

**F10. What he wants for himself apart from the house.** Motivations (`02-orond-gralhund.md:15`) give "stop feeling afraid in his own home" and "be the patriarch his title says he is". The personal goal must be `[design]` (brief ruling 17). It must not reveal the cult's name or the Stone.

**F11. Hrabbaz's history with Orond.** "Orond relies on Yalah to manage the Zhentarim" (`:32448`) and Hrabbaz is shared (D2). No source says when Hrabbaz came into service.

**F12. The Zhentarim's approach.** The sources differ on who was approached (D7). The Background must say which version it uses.

---

## G. Source facts that hint at the figure's inner life (for the backstory; do not contradict)

Each quote is a fact about Orond. Quest-time quotes are marked and must not be copied onto the page.

- "He leaves most of the plotting and socializing to his wife, {@creature Yalah Gralhund|wdh|Yalah}, to whom he is devoted." — `sources/adventure-wdh.json:32443`. (Devotion to Yalah.)
- "Orond is the patriarch, but he's not a quick-thinking or cultured sort-and deep down, he knows it." — `sources/adventure-wdh.json:32443`. (Self-knowledge; a private shame.)
- "After she was passed over, Orond became insanely angry, and he has remained that way ever since." — `sources/adventure-wdh.json:32444`. (A lasting grudge.)
- "While in Yalah's presence, Orond becomes an altogether different person: quiet, almost timid, and happy to let his wife have the spotlight." — `sources/adventure-wdh.json:32447`. (Fear of Yalah; relief at being let off.)
- "When he must speak to strangers, he keeps his half-orc bodyguard {@creature Hrabbaz|WDH} close by, for fear that others might attack and rob him at any moment." — `sources/adventure-wdh.json:32447`. (Fear of strangers.)
- "He spends his days watching mercenaries train, paying bills, and ranting about the cost of doing business in the city." — `sources/adventure-wdh.json:32448`. (His daily round.)
- "Orond was not smart or intelligent and deep down he knew this. He disliked common people and had a fragile ego." — wiki extract line 84. (Self-knowledge; contempt for commoners.)
- "Orond adored his wife. He trusted his bodyguard [[Hrabbaz]]." — wiki extract line 87. (Affection; the one person he trusts.)
- "Her husband Orond manages appearances; she manages the house." — `campaign/guides/gm-guide/debts-of-the-city.md:76`. (He is the face; he knows his role.)
- "A black-and-tan hound sits at Orond's feet. The hound died two years ago. No one has commissioned a replacement portrait." — `campaign/locations/gralhund-villa/g08-great-hall.md:7`. (A dead dog he still shows in the family portrait.)
- "Orond's morning exercise, apparently" — `campaign/locations/gralhund-villa/g11-oronds-study.md:3` (the wrestling mat in the study; a physical habit the sources do not explain). Full sentence at A5.
- "Orond is in this room during the day, reading in the wolf-skin chair, a glass of amber spirits on the side table beside him." — `campaign/locations/gralhund-villa/g12-family-library.md:19`. (His daytime habit.)
- "**Hide the private papers:** Orond keeps a private journal of about 200 pages in a false-book compartment in his study, holding his own analysis of the Grand Game's faction leaders and their agents." — `campaign/setting/organizations/12-house-gralhund.md:61`. (A private self; the journal is his.)
- "This is characterization rather than tactical intelligence; the party cannot weaponize it directly, but it confirms that Orond has been more active in the Grand Game than his frightened-library-reader persona suggests." — `campaign/locations/gralhund-villa/g11-oronds-study.md:9`. (The persona hides a working mind.)
- "Orond reads here most mornings." — `sources/Act_III_Arc_E.md:272`. (A morning habit; conflicts on the room, D5.)
- Voice: "He touches the small of his back, near the scar, when nervous." — `.claude/skills/character-voices/voices/gralhunds.md:33`. (The scar is a nervous habit.)
- Voice: "He never admits to fear, never mentions his tail, and never contradicts Yalah to her face." — `.claude/skills/character-voices/voices/gralhunds.md:35`. (The tail is a wound he does not speak of.)
- Voice: "He boasts until threatened, then hides behind Hrabbaz. His brief attempts at dignity collapse fast." — `.claude/skills/character-voices/voices/gralhunds.md:32`. (The bluster is armour.)
- Org page: "**Orond's weakness:** Orond is a coward in his wife's absence and a bully when he believes himself unobserved." — `campaign/setting/organizations/12-house-gralhund.md:103`. (The bluster-and-fear pattern.)
- Quest-time, do not copy: "The kind of coward who has decided money means he doesn't have to be brave, and tonight has thoroughly tested that theory." (`campaign/quests/act-ii/gralhund-villa/ev-05-the-guest-suite.md:39`). "I have been wise enough not to ask." (`ev-05-the-guest-suite.md:47`, the confession). "It was careless," (`ev-05-the-guest-suite.md:45`).

---

## Cross-references (the Orond topic in other files)

Grep for `Orond` across `campaign/` falls within the 405 occurrences of `Yalah|Orond` in 56 files (the Yalah notes list the files). The list below names the files with Orond lines that are day-one or routed. Quest-time lines are quoted in sections C and E.

| File | Lines naming Orond | Relevance |
|---|---|---|
| `campaign/setting/organizations/12-house-gralhund.md` | `:8`, `:21`, `:33`, `:34`, `:35`, `:37`, `:44`, `:45`, `:48`, `:61`, `:85`, `:101`, `:103`, `:109`, `:110`, `:154` | Day-one; quoted in A and D |
| `campaign/guides/factions/13-house-gralhund.md` | `:26`, `:88`, `:119` (Orond in the Stone conflict note), `:125` | Mechanics; quoted in E2 and E5 |
| `campaign/setting/notable-figures/gralhunds/01-yalah-gralhund.md` | `:5`, `:21`, `:25` | Companion page |
| `campaign/setting/notable-figures/gralhunds/03-hrabbaz.md` | `:25` (and `:6`, `:11`, `:13`, `:21`, `:29` for Hrabbaz's view of Orond) | D2 |
| `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md` | Orond not named (`:57` names Yalah and Hurv) | D3 |
| `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md` | Orond not named (`:65` names Yalah) | n/a |
| `campaign/setting/history/07-a-city-watching-itself.md` | `:69` ("Orond has been angry ever since.") | A3 |
| `campaign/setting/history/08-the-players-arrive.md` | `:58` (quest-time source, E1) | A8 |
| `campaign/gazetteer/waterdeep/north-ward.md` | `:68` (the couple's household); `:122` (Yalah's entry: "her husband Orond cowers behind her") | E1 and the Yalah notes D15 |
| `campaign/guides/gm-guide/debts-of-the-city.md` | `:76` ("Her husband Orond manages appearances; she manages the house.") | G |
| `campaign/locations/gralhund-villa/` | `area-overview.md:68`, `:81`; `g08-great-hall.md:7`; `g10-den.md:9`; `g11-oronds-study.md:1`, `:3`, `:7`, `:9`; `g12-family-library.md:5`, `:19`; `g15-guest-suite.md:25`; `g16-master-bedroom.md:12`, `:14` | A5, A6, C, G |
| `campaign/locations/cassalanter-villa/` | none for Orond | D6 |
| `campaign/quests/act-ii/gralhund-villa/` | Orond lines in `ev-03-daytime-infiltration.md:106`, `:128`; `ev-05-the-guest-suite.md:37` to `:57`; `ev-09-aftermath.md:44`; others not read line by line | E3 |
| `campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md` | `:237` (a Dunfell passage naming "Orond's account") | not read in full |
| `campaign/structure/arc-d-gralhund-villa.md` | superseded; not read line by line | n/a |
| `sources/adventure-wdh.json` | `:32139` to `:32140` (Hrabbaz entry), `:32439` to `:32466` (Orond entry), `:5955` to `:5972` (the Orond scene), `:5961` to `:5962`, `:5966` to `:5968`, `:6010`, `:6038`, `:4377`, `:4378`, `:4804`, `:4809`, `:4812`, `:20107` | A, B, C, D, E |
| `sources/Act_III_Arc_E.md` | `:31` to `:35` (cult), `:98`, `:99` (rosters), `:209`, `:216`, `:239`, `:262`, `:272`, `:378`, `:397`, `:544`, `:549`, `:556`, `:640` to `:649`; `:652` to `:653` omitted by the tool and not read | A2, A5, C, D, E3 |
| `sources/4. Gralhund Villa.pdf` | PDF pp.5, 6, 8, 9 (printed pp. 30, 31, 33, 34) | Read as images; quoted in A5, E3 (**PDF transcription**) |
| `sources/2. Other Factions.pdf` | printed p.20 (Gralhunds, "they embedded agents in Renaer Neverember's household") | Quoted in the Yalah notes A2 |
| `sources/SOURCE_GUIDE.md:155` | 1 | "Orond wants political leverage" (a guide summary; not in any source) |
| `docs/plans/npc-pronouns-table-group-c.md:80` | 1 | Row for Orond: `gralhunds/02-orond-gralhund.md:5`, he/him |

---

## Not found

- Searched for: birth year, age, parents, childhood, the amputation's account, how he became patriarch, how he met Yalah, the hound's name, the partners' names, the cause of his fears, his personal wants. Searched `sources/adventure-wdh.json` (Grep for `Orond`; hits read), `sources/Act_III_Arc_E.md` (Grep), `sources/Act_III_Arc_D.md` (Grep for `Orond`: lines `:37` and `:666`), `sources/2. Other Factions.pdf` (3 pages read), `sources/4. Gralhund Villa.pdf` (10 pages read), `sources/Appendix_B_-_Player_Factions.md` (no Gralhund or Orond line), `sources/research/` (pass5 gralhunds bundle read at lines 91 to 180; pass3 and pass4 bundles not opened), `campaign/` (Grep `Orond`).
- Searched for "Orond" in `campaign/locations/cassalanter-villa/` and `campaign/structure/arc-g-cassalanter-villa.md`: no match (D6).
- Searched for "Orond" in `campaign/setting/villains/` and `campaign/setting/the-grand-game/`: no match.
- Searched for "Orond" in `campaign/setting/lore/`: no match.
- Searched for "broad-shouldered" and "stocky" in `campaign/`: the Alexandrian Arc E line (`:216`) and the campaign lines (D4).
- Searched for a day-one account of the amputation in `campaign/` and `sources/`: none beyond "amputated when he was a young boy" (`sources/adventure-wdh.json:32448`) and "removed when he was a boy" (wiki extract line 65).
- Searched for the Orond cult claim in `sources/` (Grep `cult`): the adventure (`:6010`) and the Alexandrian (`:32`, `:34`, `:35`, `:649`).

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. No Gralhund `.docx` is named in `SOURCE_GUIDE.md`.
- `sources/research/pass3-bundles/` and `pass4-bundles/`: Grep lists the files; the lines were not opened.
- `campaign/structure/arc-d-gralhund-villa.md`: superseded; not read line by line.
- `sources/Act_III_Arc_E.md`: `:652` to `:653` (the "Playing Orond Gralhund" box) were omitted by the tool and were not read.
- `campaign/quests/act-ii/gralhund-villa/ev-06-the-gralhund-confrontation-day.md` and `ev-07-the-gralhund-confrontation-night.md`: Orond lines read from Grep output only.
