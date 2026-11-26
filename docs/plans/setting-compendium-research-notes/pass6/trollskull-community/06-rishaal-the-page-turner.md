# Pass 6 research notes: Rishaal the Page-Turner

Page: `campaign/setting/notable-figures/trollskull-community/06-rishaal-the-page-turner.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 19; user rulings Session 53)
Method: Grep and Read only. Quotes are copied from tool output. Line numbers are file lines unless marked "dump line" (wiki XML) or "extract line". JSON escapes are shown as plain quotes. `{@creature ...}` tags are left as written.
Organization page: none for Rishaal. The Watchful Order of Magists and Protectors has no organization page; it has an institution entry in `campaign/setting/governance-and-guilds/city-watch.md` (see D2).
Factions Guide: none. Villains page: none.
Voice profile: `.claude/skills/character-voices/voices/trollskull-community.md` lines 97 to 111 ("### Rishaal the Page-Turner").
Wiki: the extract `scratchpad/wiki-trollskull-community/06-rishaal-the-page-turner.txt` is the stub `NOT FOUND`. The full Forgotten Realms Wiki dump (`/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/fandom-dump/forgottenrealms_pages_current.xml`) has the page **"Rishaal"** (XML lines 4005566 to 4005650). Its cites are `WDH5e-p33` and `MM5e-p347`.
PDF: `sources/27. Addendum A Night in Trollskull Manor.pdf` was read with the Read tool's `pages` parameter. PDF page 10 is printed p.187. The **RISHAAL THE PAGE-TURNER** bullets are on PDF page 10. These PDF quotes are transcriptions from the image and must be checked with `pdftotext -layout` before they go into prose. No shell was available.

## Findings that change how the page is written

1. **The adventure gives Rishaal's day-one residence and shop.** "who lives on the third floor" (`sources/adventure-wdh.json:3511`). The shop is "Book Wyrm's Treasure", a bookshop on Trollskull Alley (wiki, dump line 4005646). The Watchful Order membership is in the adventure too (`:3511`).
2. **The affiliation label conflicts with the Watchful Order membership.** The page says "Trollskull Alley community" (line 6). The adventure, the wiki, the governance page and his own Relationships line say he is a Watchful Order member (see D2).
3. **Species and alignment have source conflicts.** The campaign and the adventure say gold dragonborn and neutral. Appendix D and the Trollskull Manor guide say "bronze dragonborn" and "NG" (see D1 and D3). The adventure outranks Appendix D.
4. **Several of the page's lines are tavern-time, not Ches 1.** The "book whose words rearrange themselves", the planar-binding purchases by Vincent, the "increasingly suspicious" line, and the Variel messages are all in Appendix D patron topics and the guide (see C). The page's "across from the tavern" has no source (see D4).

---

## A. Background facts by theme

### A1. Identity, origin and the shop

**Adventure, T6 Book Wyrm's Treasure (page 33; heading at `sources/adventure-wdh.json:3507`)**
> "The front of this bookstore is adorned with a charming sign of a gold dragon curled around a treasure hoard of books and scrolls. Inside, the shop is decorated with beautiful hardwood, and the earthy scent of old books permeates the air. The library fills two floors of this three-story building, and it somehow seems to contain more shelves than the building should be able to hold."
> — `sources/adventure-wdh.json:3511`

> "The shop is managed by a short dragonborn of gold dragon ancestry named {@creature Rishaal the Page-Turner|wdh|Rishaal} the Page-Turner, who lives on the third floor. Rishaal, a member of the Watchful Order of Magists and Protectors, is a {@creature mage}, with these changes:"
> — `sources/adventure-wdh.json:3512`

**Wiki, "Rishaal" page (infobox and lead, dump lines 4005582 to 4005646; entities decoded)**
> "| nicknames      = The Page-Turner" (dump line 4005589)
> "| sex            = Male" (dump line 4005593)
> "| race           = [[Gold dragon|Gold]] [[dragonborn]]" (dump line 4005594)
> "| occupation     = Shopkeeper" (dump line 4005596)
> "| languages      = [[Common]], [[Draconic_language|Draconic]], [[Dwarvish]], and [[Elvish]]" (dump line 4005599)
> "'''Rishaal the Page-Turner''' ({{Pronounce|ree|SHAWL|refs=...}}) was a [[dragonborn]] shopkeeper and [[wizard]] in [[Waterdeep]] in the late 15{{th}} century [[DR]]." (dump line 4005643; `WDH5e-p33`)
> "Rishaal, a dragonborn of [[gold dragon]] ancestry, managed the [[Book Wyrm's Treasure]], a bookshop on [[Trollskull Alley]] in the [[North Ward of Waterdeep|North Ward]]. He was also a member of the [[Watchful Order of Magists and Protectors]]." (dump line 4005646; `WDH5e-p33`)

**Wiki, North Ward "Shops & Businesses" (`sources/research/pass3-bundles/north-ward/wiki.txt:154`, cites WDH5e-p33)**
> "* [[Book Wyrm's Treasure]]<ref name="WDH5e-p33">{{Cite book/Waterdeep: Dragon Heist|33}}</ref>"

**Gazetteer, Trollskull Alley entry**
> "- The Tiger's Eye is a detective agency run by **Vincent Trench**, Book Wyrm's Treasure is a bookshop run by **Rishaal the Page-Turner**, and a few doors down is Frewn's Brews, a rival pub owned by **Emmek Frewn**."
> — `campaign/gazetteer/waterdeep/north-ward.md:58`

**Gazetteer, Organizations (Watchful Order, Ulkoria and Rishaal in the alley)**
> "- **Organizations:** House Gralhund and the Black Network resources in its villa, the Harpers (Ulbrinter Villa), Manshoon's Zhentarim (the Interrogation House), the Fellowship of Innkeepers (represented by Broxley Fairkettle), the City Watch (the station and Endcliff Tower), the Watchful Order (Ulkoria Stonemarrow and Rishaal the Page-Turner in Trollskull Alley) and the Guild of Glassblowers, Glaziers and Spectacle-makers (the House of Crystal)."
> — `campaign/gazetteer/waterdeep/north-ward.md:34`

**Gazetteer, Defense**
> "- Ulkoria Stonemarrow and Rishaal the Page-Turner are both Watchful Order members in good standing, and either can sign the written attestation that the Order's inspector asks for about the tavern's poltergeist."
> — `campaign/gazetteer/waterdeep/north-ward.md:178`

**Trollskull Manor location, turret (the view toward the shop)**
> "The turret occupies the northeast corner of the building, rising half a floor above the fourth-floor roofline. A tight spiral stair connects it to the fourth floor. One small room, low ceiling, single window facing north over the alley and east toward Book Wyrm's Treasure. Empty weather vane mounting bracket on the roof peak; the weather vane itself is gone."
> — `campaign/locations/trollskull-manor/tm06-turret.md:3`

### A2. Trade, stock and the shop's services

**Adventure, Services (page 33)**
> "The shop contains books of all sorts. In addition, {@creature Rishaal the Page-Turner|wdh|Rishaal} has a small collection of spellbooks and allows wizards to copy spells from them at the cost listed in the Spells for Sale table. He can scribe any of these spells as a spell scroll but charges twice the listed cost for this service."
> — `sources/adventure-wdh.json:3526`

**Adventure, racial traits (his combat and language, which is a fact about the figure)**
> "He has these racial traits: He can use his action to exhale a 15-foot cone of fire (but can't do this again until he finishes a short or long rest); each creature in the cone must make a {@dc 10} Dexterity saving throw, taking {@dice 2d6} fire damage on a failed save, or half as much damage on a successful one. He has resistance to fire damage. He speaks Common, Draconic, Dwarvish, and Elvish."
> — `sources/adventure-wdh.json:3517`

**Window sign (Fireball! ev-01 and the alley, quest-time; see C2)**
> "**Book Wyrm's Treasure** (Rishaal the Page-Turner) — earthy paper smell from the propped-open door, handwritten sign in the window: *Spells for sale. Inquire within.*"
> — `campaign/quests/act-i/trollskull-alley/ev-01-welcome-to-trollskull-alley.md:29`

### A3. Temperament, habits and manner

**Appendix D, Appearance and Roleplaying Keys (1342, 1344)**
> "**Appearance:** Burnished amber-bronze scales that catch candlelight. He is thin for a dragonborn, bookish in posture, and always has ink somewhere on his hands. His shop is two doors down; he appears to have walked here mid-thought and hasn't quite caught up with himself yet."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1342`
> "**Roleplaying Keys:** Enthusiastic about obscure things. Will interrupt himself to clarify a reference. Genuinely delighted by people who ask follow-up questions. Has a complicated relationship with the concept of closing time."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1344`

**Trollskull Manor guide, Notable Patrons (`08-notable-patrons.md:122` to `:123`)**
> "**Rishaal the Page-Turner** *(Book Wyrm's Treasure, NG male bronze dragonborn, Mage)*"
> "Burnished amber-bronze scales; bookish in posture; ink on hands; appears mid-thought."
> — `campaign/guides/trollskull-manor/08-notable-patrons.md:122` and `:123`

**Voice profile (`trollskull-community.md`)**
> "*A distracted, ink-stained dragonborn scholar who answers the question you didn't ask and misses the one you did.*" (line 98)
> "- **Personality in speech:** Absorbed and befuddled, but sharper than he sounds. He sometimes drops a pointed observation about who bought what in the middle of a ramble, then goes back to his book. Protective anxiety about his inventory makes him fussy." (line 104)
> "- **Quirks:** He blinks up from a page and says \"Hm? Oh.\" He corrects the edition. He wipes ink onto his scales and doesn't notice." (line 105)
> "- **Never:** He never hurries, never sells a dangerous book without a warning, and never names his suspicions of a neighbour outright." (line 107)

### A4. Membership, rank and relations to other named figures

**Adventure, membership (3512, quoted in A1). Wiki (dump line 4005646, quoted in A1).**
- Rank or post in the Order is not given by any source. See F.

**Adventure, the Order's registration rule (general, not Rishaal-specific)**
> "Arcane spellcasters living in the city are required by law to register with the Watchful Order of Magists and Protectors, so that they can be called on to defend the city with their magic in times of need."
> — `sources/adventure-wdh.json:1101`

**Watchful Order, city-watch institution entry (`campaign/setting/governance-and-guilds/city-watch.md:51`, first two sentences)**
> "**The Watchful Order of Magists and Protectors.** Waterdeep requires arcane spellcasters who plan to stay to register with the city, and it strongly encourages them to join the Watchful Order, which the published adventure says the Blackstaff heads. Members are expected to serve as temporary members of the Watch or the Guard when called. (rest of the passage covers: their expertise, the Order watching its own members, the wiki's guild and mage-academy description, and the cross-reference to The Guilds.)"

**Ulkoria Stonemarrow, Relationships (colleague; `campaign/setting/notable-figures/trollskull-community/09-ulkoria-stonemarrow.md:25`)**
> "**Relationships.** Ulkoria is a senior member of the Watchful Order of Magists and Protectors, the tavern's former owner, a colleague of Rishaal the Page-Turner, and a Masked Lord of Waterdeep (never confirmed in her presence)."

**Vincent Trench, Relationships (see the Vincent notes): his page calls Vincent a neighbor. The adventure has no Rishaal and Vincent link other than Appendix D `:1350`.**

**Ulkoria's label (Notable Figures page line 6, the same label as Rishaal's page)**
> "> - **Affiliation:** Trollskull Alley community" — `campaign/setting/notable-figures/trollskull-community/09-ulkoria-stonemarrow.md:6`

### A5. Time in post

- The wiki says "managed the [[Book Wyrm's Treasure]]" in the late 15th century DR (dump lines 4005643 and 4005646). No year is given for when he took the shop. No source gives the year he came to Waterdeep or his age. See F.

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Summary (page line 5): "> - *Gold dragonborn mage, neutral, he/him*. Stat block: **Mage**." — `campaign/setting/notable-figures/trollskull-community/06-rishaal-the-page-turner.md:5`
- Adventure: "Rishaal is neutral." (`sources/adventure-wdh.json:3516`)
- Appendix D: "*Book Wyrm's Treasure — NG male bronze dragonborn, Mage*" (`sources/Appendix_D_-_Running_the_Tavern.md:1340`)
- Guide: "NG male bronze dragonborn, Mage" (`08-notable-patrons.md:122`)
- Wiki: "| alignment5e    = [[Neutral]]" (dump line 4005638)
- Conflict: NG (Appendix D, guide) against neutral (adventure, wiki, page). See D3.

**Species**
- Summary: "Gold dragonborn" (page line 5).
- Adventure: "a short dragonborn of gold dragon ancestry" (`sources/adventure-wdh.json:3512`)
- Wiki: "| race           = [[Gold dragon|Gold]] [[dragonborn]]" (dump line 4005594)
- Appendix D and guide: "bronze dragonborn" (`:1340`; `08-notable-patrons.md:122`). See D1.

**Pronouns**
- Summary (page line 5): "he/him".
- Adventure: "He has these racial traits" (`sources/adventure-wdh.json:3517`); "He can scribe any of these spells" (`:3526`). The adventure's pronoun is "He".
- Appendix D: "NG male bronze dragonborn" (`:1340`) gives "male".
- Wiki: "| sex            = Male" (dump line 4005593).
- All sources agree: he/him.

**Stat block**
- Summary: "Stat block: **Mage**." (page line 5).
- Adventure: "is a {@creature mage}, with these changes:" (`sources/adventure-wdh.json:3512`).
- Appendix D: "Mage" (`:1340`).
- Wiki: "| challenge5e    = 6" and "| class5e        = {{Class table|edition=5e|[[Wizard]]|9}}" (dump lines 4005639 and 4005640); refs "MM5e-p347" (dump line 4005641).

---

## C. Sentences on the current page (and the voice profile) that narrate a quest-time event or a day-one conflict

Current page: `campaign/setting/notable-figures/trollskull-community/06-rishaal-the-page-turner.md`. Sections: Gamemaster's Summary, Roleplaying Information, Character Information, Overview. No Background yet.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| C1 | 7 | "> - **Featured in:** **Trollskull Alley**, **Fireball!**" | Quest list. Route (ruling 1) | Trollskull Alley: `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:27`; Fireball!: `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:155` to `:161`; `campaign/quests/act-ii/fireball/overview.md:32` |
| C2 | 15 (Motivations) | "**Motivations.** Rishaal wants to maintain the finest arcane bookshop in the North Ward, understand the book whose words rearrange themselves when observed, and determine why Vincent Trench keeps buying texts on planar binding." | Two clauses are tavern-time. "understand the book whose words rearrange themselves when observed" is an Appendix D patron topic (`:1347`) and guide `08-notable-patrons.md:124`. "determine why Vincent Trench keeps buying texts on planar binding" is an Appendix D patron topic (`:1350`) and guide `:127`. Flag for the orchestrator (ruling 3 keeps Motivations verbatim unless a line is quest-time) | `sources/Appendix_D_-_Running_the_Tavern.md:1347`, `:1350`; `campaign/guides/trollskull-manor/08-notable-patrons.md:124`, `:127` |
| C3 | 25 (Relationships) | "**Relationships.** Rishaal is a member of the Watchful Order of Magists and Protectors, a professional acquaintance of Ulkoria Stonemarrow (whose arcane purchases he respects), and an increasingly suspicious neighbor of Vincent Trench." | Membership: day-one (`sources/adventure-wdh.json:3512`). "increasingly suspicious neighbor of Vincent Trench" is quest-time phrasing from ev-03, which says the suspicion is shared "if the party shows interest". "(whose arcane purchases he respects)" has no source | `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:27`; `campaign/gazetteer/waterdeep/north-ward.md:153` |
| C4 | 29 (Overview) | "Rishaal runs Book Wyrm's Treasure, the arcane bookshop across from the tavern, and keeps the alley's best selection of magical texts and arcane lore — if you can get his attention long enough to ask." | "across from the tavern" has no source (see D4). "the tavern" is the Trollskull Manor, which is closed on Ches 1 (gazetteer `:63`) and given to the party after Volo's quest (`sources/adventure-wdh.json:1595`). Restate the placement from the sources | `campaign/gazetteer/waterdeep/north-ward.md:58` ("a bookshop"); `sources/Appendix_D_-_Running_the_Tavern.md:1342` ("two doors down") |
| C5 | 21 (Persona) | "Deep down, he suspects at least one of his neighbors is not what they appear, and he is not sure he wants to confirm it." | Day-one inner life, no source. Keep. The "suspects" is not the quest-time "increasingly" | none (G) |
| C6 | 23 (Morale) | "In a fight, Rishaal would exhaust his spells defending Book Wyrm's Treasure before retreating. He will not abandon his inventory to save himself, and his breath weapon is a last resort he considers undignified." | Day-one. "breath weapon" is sourced (`:3517`). "considers undignified" has no source | `sources/adventure-wdh.json:3517` |
| C7 | Voice 110 (Business) | "*Business:* \"Planar binding? That's the third request this month, and the other two were the same man. Anyway. Aisle four.\"" | **Tavern-time clause.** Planar-binding purchases are Appendix D `:1350` (tavern night, Vincent's two visits "this tenday"). Drafter decides whether to keep the sample line (ruling 16) | `sources/Appendix_D_-_Running_the_Tavern.md:1350`; `campaign/guides/trollskull-manor/08-notable-patrons.md:127` |
| C8 | Voice 109 (Greeting) | "*Greeting:* \"Hm? Oh, customers. Welcome to Book Wyrm's, mind the stack, it's load-bearing.\"" | Day-one. Keep | none needed |
| C9 | Voice 111 (Under pressure) | "*Under pressure:* \"Get out from between me and the shelves, please. I'd rather not breathe on the first editions.\"" | Day-one. Keep. "breathe" refers to the breath weapon (`:3517`) | none needed |

### C2. Where Rishaal's quest-time events already live (routed; do not restate on the day-one page)

- **Trollskull Alley, ev-01 (the shop sign)**: "**Book Wyrm's Treasure** (Rishaal the Page-Turner) — earthy paper smell from the propped-open door, handwritten sign in the window: *Spells for sale. Inquire within.*" — `campaign/quests/act-i/trollskull-alley/ev-01-welcome-to-trollskull-alley.md:29`
- **Trollskull Alley, ev-02 (the poltergeist notice)**: "The Order's inspector was dispatched because Rishaal filed a poltergeist notice during his own guild duties. He notices Lif within thirty seconds of entering the taproom. His report notation: "Haunting: active. Benign or hostile: TBD."" — `campaign/quests/act-i/trollskull-alley/ev-02-the-guild-gauntlet.md:48`
- **Trollskull Alley, ev-02 (the attestation)**: "The Order requires written attestation that the haunting poses no public safety risk. Two qualified signatories in the alley: Rishaal the Page-Turner or Ulkoria Stonemarrow (both Watchful Order members in good standing)." — `campaign/quests/act-i/trollskull-alley/ev-02-the-guild-gauntlet.md:50`
- **Trollskull Alley, ev-03 (The Alley Tour)**: "**Rishaal the Page-Turner (Book Wyrm's Treasure).** Arrives with a slim leather-bound history of the North Ward and hands it over: "There's a chapter on the building. Thought you'd want to know what you own." Has questions about the cellar, delivered via a footnote on a subsequent visit. Increasingly suspicious of Vincent Trench and will share that suspicion if the party shows interest. Cross-ref the **Rishaal the Page-Turner** page in Notable Figures." — `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:27`
- **Trollskull Alley, ev-06 (The Grand Opening)**: "**Neighbors** — Tally, Embric and Avi, Fala, Rishaal (all four attend)." — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:40`
- **Trollskull Alley overview, Involved Characters**: "- **Rishaal the Page-Turner** (Watchful Order) — bookseller at Book Wyrm's Treasure; filed the poltergeist notice; suspicious of Vincent Trench" — `campaign/quests/act-i/trollskull-alley/overview.md:35`
- **Fireball!, ev-01 (Rishaal and the Lantanese text)**: "Book Wyrm's Treasure. No visual evidence of the blast — he was in the back of the shop with the morning delivery. Within an hour of being asked about mechanical constructs and the explosion, he produces a Lantanese engineering text from his stock: *Gond's Artifice: Mechanical Life in the Lantanese Tradition*, specifically the chapter on nimblewrights." — `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:157`; "The text names the House of Inspired Hands (corner of Seawatch and Shark Streets, Sea Ward) as Waterdeep's only active temple of Gond and the foremost authority on Lantanese mechanical constructs in the city." — `:159`
- **Fireball!, ev-02**: "1. **Rishaal's text.** Lantanese engineering book directly names the House of Inspired Hands." — `campaign/quests/act-ii/fireball/ev-02-the-house-of-inspired-hands.md:92`
- **Fireball!, overview**: "- **Rishaal the Page-Turner** (Book Wyrm's Treasure) — produces a Lantanese engineering text naming the House of Inspired Hands within an hour of being asked" — `campaign/quests/act-ii/fireball/overview.md:32`
- **Trollskull Manor guide, Tavern time (Tarsakh 11 to 20 row)**: "| Tarsakh 11–20 | Jarlaxle Baenre (in disguise), Mattrim "Threestrings" Mereg, Rishaal the Page-Turner | 19: a courier arrives with an urgent message for a patron who just left | The patron who just left was Jarlaxle. The message, from Krebbyg, reads "The tide turns on the twentieth." It's the party's last clear warning before the Faire sails. |" — `campaign/guides/trollskull-manor/06-tavern-time.md:29`
- **Trollskull Manor guide, Tavern time (Mirtul 1 to 10 row)**: "| Mirtul 1–10 | Rishaal the Page-Turner, Ulkoria Stonemarrow, Vincent Trench | 9: Kyser Tameno's first visit | Arcane gossip night. An archmage of the Watchful Order drinks two tables from a rakshasa in disguise, and a wizard walks out of the wall. |" — `campaign/guides/trollskull-manor/06-tavern-time.md:31`
- **Trollskull Manor guide, Patron table**: "| 5 | Rishaal the Page-Turner *(Book Wyrm's Treasure)* |" — `campaign/guides/trollskull-manor/06-tavern-time.md:62`
- **Trollskull Manor guide, Harpers dead-drop**: "- **Harpers** may use it as a casual dead-drop point (rotating books via Rishaal)." — `campaign/guides/trollskull-manor/01-overview.md:25`
- **Appendix D, Harpers dead-drop**: "- **The Harpers** may use the tavern as a casual dead-drop point, with notes left inside specific books that Rishaal provides on a rotating basis." — `sources/Appendix_D_-_Running_the_Tavern.md:1650`
- **Variel Duskwhisper messages (tavern-time)**: "Asks if the characters have used his shop to leave a message for Variel Duskwhisper (Harper courier), and if so, which one — because he has received two messages for that name and is not sure which is which." — `sources/Appendix_D_-_Running_the_Tavern.md:1349`. Guide: "Asks if the party left a message at the shop for Variel Duskwhisper — he received two messages for that name and isn't sure which is which" — `campaign/guides/trollskull-manor/08-notable-patrons.md:126`. Routed by `campaign/setting/notable-figures/harpers/06-variel-duskwhisper.md:112`.
- **Trollskull Manor guide, Notable Patrons (Rishaal block, `08-notable-patrons.md:122` to `:127`)**: "- Acquired a book whose words rearrange when directly observed. Is thrilled. Wonders if the party would like to look at it while he watches their faces." (`:124`); "- A customer has been asking for pre-Spellplague accounts of Undermountain's upper levels. He didn't sell them anything." (`:125`)
- **Appendix D, Topics & Agendas (1347 to 1350; tavern-time)**: "1. Has acquired a book that he cannot read — not because of a language barrier, but because the words rearrange themselves when observed directly. He is thrilled about this. He wonders if the characters might look at it while he watches their faces." (`sources/Appendix_D_-_Running_the_Tavern.md:1347`); "2. A customer has been asking for a very specific type of text: pre-Spellplague accounts of Undermountain's upper levels. He did not sell them anything. He is mentioning this because it seemed like the sort of thing someone in their position should know." (`:1348`)
- **PDF, RISHAAL THE PAGE-TURNER (printed p.187; PDF page 10; transcription, check with pdftotext)**: "Sits quietly in one corner, sipping tea and reading an oddly titled book: Duke Avanice's Vile Poems, Cults of Ancient Netheril, Umbral Reflections on the Kingdom of Man, The Journal of Captain Arienthil's Journeys in the Moonshae Isles, Memories of Kara-Tur, The Seventh Codex of the Numinous Ascendants of Kaal, The Atlas of Forgotten Cartographies." / "If Lif has been pacified and is now part of the tavern's culture, Rishaal will stop by with a copy of Richelle's Poems, a book of elvish poetry which was once one of Lif's favorites." / "His hands are bandaged. He came into possession of a cursed book that, when he touched it, caused his hands to burst out into boils." — `sources/27. Addendum A Night in Trollskull Manor.pdf`, PDF page 10
- **Structure docs (superseded; do not use for content)**: `campaign/structure/arc-b-trollskull-alley.md:99` ("- **Rishaal the Page-Turner (Book Wyrm's Treasure):** Arrives with a slim leather-bound history of the North Ward ...") and `:215`; `campaign/structure/arc-c-fireball.md:81` ("- **Rishaal the Page-Turner.** Book Wyrm's Treasure. No visual evidence.").

---

## D. Conflicts

**D1. Species and ancestry: gold or bronze**
- Adventure: "a short dragonborn of gold dragon ancestry" (`sources/adventure-wdh.json:3512`).
- Wiki: "[[Gold dragon|Gold]] [[dragonborn]]" (dump line 4005594); "a dragonborn of [[gold dragon]] ancestry" (dump line 4005646).
- Appendix D: "NG male bronze dragonborn, Mage" (`sources/Appendix_D_-_Running_the_Tavern.md:1340`); "Burnished amber-bronze scales that catch candlelight." (`:1342`).
- Guide: "NG male bronze dragonborn, Mage" (`campaign/guides/trollskull-manor/08-notable-patrons.md:122`).
- Page (line 5): "Gold dragonborn mage".
- Higher ranked: the adventure (gold). The page follows it. "Burnished amber-bronze scales" in Appendix D and the guide is a scale description and does not settle the ancestry. Flag the Appendix D and guide "bronze" as stale.

**D2. Affiliation: "Trollskull Alley community" against the Watchful Order**
- Page (line 6): "> - **Affiliation:** Trollskull Alley community"
- Page (line 25): "Rishaal is a member of the Watchful Order of Magists and Protectors ..."
- Adventure: "Rishaal, a member of the Watchful Order of Magists and Protectors, is a {@creature mage}, with these changes:" (`sources/adventure-wdh.json:3512`)
- Wiki: "He was also a member of the [[Watchful Order of Magists and Protectors]]." (dump line 4005646)
- Governance page (`campaign/setting/governance-and-guilds/guilds.md:48`): "**Rishaal the Page-Turner** (Neutral, Gold Dragonborn, he/him) and **Ulkoria Stonemarrow** (Neutral Good, Shield Dwarf, she/her) are Order members in Trollskull Alley, and in The Guild Gauntlet either of them can sign the written statement that the poltergeist Lif poses no public danger."
- Organization page (`campaign/setting/organizations/04-order-of-the-gauntlet.md:158`): "> - **Conflicts:** Rishaal the Page-Turner and Ulkoria Stonemarrow. `campaign/setting/governance-and-guilds/guilds.md:48` calls them Order members, and their Notable Figures pages (`trollskull-community/06` and `09`, line 6) label them Trollskull Alley community. The page follows the Notable Figures pages, so neither is in Key Members."
- Higher ranked: the adventure and the campaign's own page body say Watchful Order membership. The line-6 label is a neighborhood label, not an organization. The Order has no organization page (see `campaign/setting/governance-and-guilds/city-watch.md:51`). Flag for the orchestrator: the affiliation label needs a decision. Brief ruling 6 says labels are checked against organization pages, and the Order's page does not exist.

**D3. Alignment: neutral or NG**
- Adventure: "Rishaal is neutral." (`sources/adventure-wdh.json:3516`)
- Wiki: "| alignment5e    = [[Neutral]]" (dump line 4005638)
- Page (line 5): "neutral"
- Appendix D: "NG male bronze dragonborn, Mage" (`sources/Appendix_D_-_Running_the_Tavern.md:1340`)
- Guide: "NG male bronze dragonborn, Mage" (`campaign/guides/trollskull-manor/08-notable-patrons.md:122`)
- Higher ranked: the adventure (neutral). Appendix D and the guide say NG. The guide copies Appendix D.

**D4. Shop placement: "across from the tavern" or "two doors down"**
- Page (line 29): "the arcane bookshop across from the tavern"
- Gazetteer (`north-ward.md:58`): "a few doors down is Frewn's Brews" (after "Book Wyrm's Treasure is a bookshop run by **Rishaal the Page-Turner**")
- Appendix D (`:1342`): "His shop is two doors down; he appears to have walked here mid-thought and hasn't quite caught up with himself yet."
- Trollskull Manor turret (`tm06-turret.md:3`): "single window facing north over the alley and east toward Book Wyrm's Treasure."
- No source says "across from the tavern". The adventure gives the shop's keyed place as T6 (`sources/adventure-wdh.json:3507`) and the map is an image. Higher ranked: the gazetteer (campaign) says only "a bookshop". Flag: the page's placement has no source.

**D5. Hands: ink or bandages**
- Page (line 21): "ink-stained hands"; voice profile line 98: "ink-stained dragonborn scholar".
- Appendix D (`:1342`): "always has ink somewhere on his hands."
- PDF page 10 (printed p.187, transcription): "His hands are bandaged. He came into possession of a cursed book that, when he touched it, caused his hands to burst out into boils."
- Higher ranked: the campaign's ink (day-one) against the PDF's bandages (tavern-time topic). The bandage is a tavern-time condition and is not day-one.

**D6. "Colleague" or "professional acquaintance" (Ulkoria)**
- Page (line 25): "a professional acquaintance of Ulkoria Stonemarrow (whose arcane purchases he respects)"
- Ulkoria page (line 25): "a colleague of Rishaal the Page-Turner" (`09-ulkoria-stonemarrow.md:25`)
- Campaign-internal. The Ulkoria page is Notable Figures; the Rishaal page is also Notable Figures. Flag only.

---

## E. Stale lines in other files (not edited) and routed quest references

- `campaign/setting/deities/bahamut.md:114`: "- **Valetta**, **Rishaal the Page-Turner** (Notable Figures): the campaign's dragonborn, with no tie to him." — a cross-reference. Consistent with the page; it states no tie to Bahamut.
- `campaign/setting/deities/gond.md:114`: "- **Remallia Haventree**, **Vajra Safahr, the Blackstaff**, **Barnibus Blastwind**, **Rishaal the Page-Turner** (Notable Figures): the contacts who point the party to the House in **Fireball!**." — a cross-reference to a quest-time event.
- `campaign/guides/trollskull-manor/08-notable-patrons.md:122`: "NG male bronze dragonborn" — stale against the adventure (D1, D3).
- `sources/Appendix_D_-_Running_the_Tavern.md:1340`: "NG male bronze dragonborn" — stale against the adventure (D1, D3).
- `campaign/structure/arc-b-trollskull-alley.md:99`: "Cross-ref **Appendix A** (Rishaal profile)." No file named Appendix A exists in `sources/`.
- `campaign/setting/notable-figures/harpers/06-variel-duskwhisper.md:112`: "Rishaal the Page-Turner holding two messages for Variel lives in `campaign/guides/trollskull-manor/08-notable-patrons.md:126`." — routed, consistent.
- `campaign/quests/act-i/trollskull-alley/overview.md:35`: "(Watchful Order)" — a quest summary label; does not govern (D2).
- `campaign/quests/act-ii/fireball/design-notes.md` and `ev-07-kalainsalley-tower.md`: no Rishaal line found by grep (not checked line by line).

**E-routed (quest-time references and where each already lives):** `ev-01-welcome-to-trollskull-alley.md:29`; `ev-02-the-guild-gauntlet.md:48`, `:50`; `ev-03-the-neighbors.md:27`; `ev-06-the-grand-opening.md:40`; `overview.md:35`; `fireball/ev-01-the-fireball.md:155` to `:161`; `fireball/ev-02-the-house-of-inspired-hands.md:92`; `fireball/overview.md:32`; `guides/trollskull-manor/06-tavern-time.md:29`, `:31`, `:62`; `01-overview.md:25`; `08-notable-patrons.md:122` to `:127`; Appendix D `:1347` to `:1350` and `:1650`; PDF printed p.187.

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with.

1. **Origin, birth and arrival in Waterdeep.** No source. The wiki's home is "[[Waterdeep]], [[Sword Coast North]]" (dump line 4005591). The age is blank (dump line 4005597). Stay consistent with: a gold dragonborn who is a Waterdeep resident; a Watchful Order member (`sources/adventure-wdh.json:3512`).
2. **Family.** No source. The wiki leaves parents, spouses and siblings blank (dump lines 4005610 to 4005612). Do not give a family without a `[design]` tag.
3. **How he came to Book Wyrm's Treasure.** No source. The wiki gives only that he "managed" it (dump line 4005646). The adventure says "The shop is managed by" him (`sources/adventure-wdh.json:3512`). Stay consistent with: he manages, and "lives on the third floor" (`:3512`).
4. **His training and Order rank.** No source gives a teacher, a school or a rank. The adventure gives only "a member of the Watchful Order of Magists and Protectors" (`:3512`). Registration is required for arcane casters (`sources/adventure-wdh.json:1101`).
5. **His faith, if any.** No source. Do not give him a deity. The Bahamut page's "no tie" line (E) is the only faith-related line.
6. **The book whose words rearrange.** Tavern-time (Appendix D `:1347`). Not a day-one fact.
7. **His relationship to Vincent beyond suspicion.** Appendix D `:1350` gives Vincent's planar-binding purchases (tavern-time). No day-one link.
8. **The third-floor living space.** Sourced ("who lives on the third floor", `:3512`), but no detail of the rooms.

---

## G. Inner-life hints in the sources (exact quotes)

These are the sourced hints a Background or the personal goals may use. They must not be contradicted.

- **Delight in others' questions.** "Genuinely delighted by people who ask follow-up questions." — `sources/Appendix_D_-_Running_the_Tavern.md:1344`
- **Closing time.** "Has a complicated relationship with the concept of closing time." — `:1344`
- **Mid-thought.** "he appears to have walked here mid-thought and hasn't quite caught up with himself yet." — `:1342`
- **Protective of the inventory.** "Protective anxiety about his inventory makes him fussy." — voice profile line 104; "He will not abandon his inventory to save himself" — page line 23 (day-one, design).
- **Never sells a dangerous book without a warning.** "never sells a dangerous book without a warning" — voice profile line 107.
- **Dislikes being told what to think.** No source. Do not invent without a tag.
- **Fondness for Lif (PDF, tavern-time).** "If Lif has been pacified and is now part of the tavern's culture, Rishaal will stop by with a copy of *Richelle's Poems*, a book of elvish poetry which was once one of Lif's favorites." — PDF page 10 (printed p.187; transcription). Tavern-time; the drafter may use the father-like care as a hint only.
- **Suspicion he keeps.** "Deep down, he suspects at least one of his neighbors is not what they appear, and he is not sure he wants to confirm it." — page line 21 (no source).
- **Suspicion he does not voice.** "never names his suspicions of a neighbour outright." — voice profile line 107.
- **Scholarly absorption.** "Rishaal most often feels scholarly absorption, mild befuddlement at interruptions, private delight at a rare find ..." — page line 13 (day-one, design).
