# Pass 6 research notes: Volothamp "Volo" Geddarm

Page: `campaign/setting/notable-figures/independents-allies/01-volothamp-volo-geddarm.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 19; ruling 19 on GM-facing pages)
Ruling used: Ches 1, 1492 DR. Quest-time = any capture, rescue, mission, reward, hire or "once the party" wording.
Organization page: none. Volo is "Independent (ally)" (page L6). The independents-allies group has no `campaign/setting/organizations/` page and no `campaign/guides/factions/` page.
Voice profile: `.claude/skills/character-voices/voices/independents-allies.md` lines 7 to 44 ("### Volothamp "Volo" Geddarm" and "#### Volo's written voice").
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/trollskull-community/01-talisolvanar-fellbranch.md`

## Method and caveats

- Campaign files: Grep and Read. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`. Quoted as the JSON string. JSON escapes are shown as plain quotes. `{@creature ...}` and `{@i ...}` tags are left as written. Line numbers are JSON line numbers.
- Alexandrian markdown: `sources/Appendix_D_-_Running_the_Tavern.md` and `sources/Appendix_B_-_Player_Factions.md`, read by Grep and Read.
- Alexandrian PDFs read with the Read tool's `pages` parameter: `sources/14. Finding Floon.pdf` (5 pages, printed pp. 102 to 106) and `sources/26. Addendum Other Collaborators.pdf` (5 pages, printed pp. 173 to 177). Transcriptions from the page images are flagged `[PDF: check with pdftotext -layout]` below. No shell was available.
- Wiki: `wiki-independents-allies/01-volothamp-volo-geddarm.txt` is the stub `NOT FOUND`. The full Forgotten Realms Wiki dump in the scratchpad does have the page: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/fandom-dump/forgottenrealms_pages_current.xml`, page title "Volothamp Geddarm" (XML lines 52017 to about 52345). Quotes from it are cited as "dump line N". Entities are decoded. Wiki markup (`[[ ]]`, `{{ }}`, `''`) and `<ref>` tags are removed from quotes, and each quote that needed this says so. The wiki prints no edition on most lines; where a citation key is shown it is given, and otherwise the edition is "not tagged".
- Other wiki: the pass5 and pass3 bundles were searched for Volo (`sources/research/`) and returned no Volo page text.
- `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **The page says Renaer outbid Emmek for the Trollskull deed. Every other source says Volo did.** Page L25 reads "Renaer Neverember, the man who outbid Emmek Frewn for the Trollskull Manor deed". The adventure (`sources/adventure-wdh.json:4237`) says Emmek "was outbid by Volothamp Geddarm". Section D1.
2. **The page narrates the quest.** Page L29 "He hires the party to find his missing friend Floon Blagmaar." and L25 "(which he gives to the party)" are quest-time (brief ruling 1). Section C.
3. **The stat block and ethnicity on L5 have no published source.** The adventure gives no stat block or ethnicity for Volo. The wiki gives Wizard level 1 and CR 1/4 (dump lines 52100 to 52101) and leaves ethnicity blank (dump line 52053). Sections B and D2.
4. **How Volo knows things is written in the sources.** Elminster describes Volo's method as gossip, notes and "spying" (dump line 52160), and Volo's own revised guide says he uses "secondhand sources" (dump line 52225). Section H (ruling 19).

---

## A. Background facts by theme

Nothing here is quest-time unless marked.

### A1. Origin and early life (wiki only)

> "According to Elminster, at least, Volo was born in a bog somewhere. He was named for the city of Volothamp in Calimshan, apparently because he had been conceived there, and he spent some of his early childhood there. From such an inauspicious start, he would travel far and wide."
> — dump line 52180 (`### Volo's Early Life`; refs removed: `VGtW-p232-233`, `EGP-WiViD&D`). Edition: not tagged.

> "Volothamp Geddarm first came to prominence when he published the infamous first version of ''Volo's Guide to All Things Magical'' early in the 1358, and in doing so angered many of Faerûn's mages."
> — dump line 52195 (markup removed; refs `FRA-p44`, `PftM-p4`, `NwN2:SoZ`). The year is 1358 DR, not day one. Use only as backstory with the date.

### A2. Family (wiki only; edition not tagged)

> "From a tenday-long affair with Ravithara Silmerhelve, of the Silmerhelve noble family of Waterdeep, Volo had one son, Emmeros Silmerhelve. Volo and Ravithara were unmarried and Emmeros was still an infant in 1372 DR."
> — dump line 52141 (markup removed; refs `NHoW`, `Dr250-p80`).

> "children       = [[Emmeros Silmerhelve]] (son)"
> — dump line 52071.

The campaign has no file that names Emmeros or Silmerhelve in a Volo context. Grep of `campaign/` for "Emmeros" and "Silmerhelve" returned only `campaign/quests/faction-events/lords-alliance/m02-the-exiles-return/` (Kylynne Silmerhelve, a magister, a different figure).

### A3. Reputation and manner (wiki and campaign)

> "What is known of Volo comes via [[Elminster]], who edited, annotated, provided prefaces for, and indeed criticized Volo's guides."
> — dump line 52108 (markup and refs removed). Elminster's descriptions follow in the same paragraph.

> "Volo certainly had a reputation for embellishing the truth and for bragging and he had an overly high opinion of himself and his place in the world."
> — dump line 52108 (refs removed; the source's sentence runs on with "and he had an overly high opinion").

> "Despite his flaws, however, Volo was soft at heart and he cared for his friends most of all, at least those friends he had. He would do anything he could to aid them."
> — dump lines 52112 and 52112's next sentence (refs removed; both sentences are in the same paragraph at line 52112 and 52113 respectively, as printed in the dump).

> "Although a notorious rogue in his own right, Volo's reputation and the rumors about him meant he was often blamed and scapegoated for many more scandals than he'd actually had a hand in."
> — dump line 52156 (refs removed).

Campaign and adventure:
> "Volothamp Geddarm is known to most Waterdavians as a braggart and a notorious embellisher of facts. For all his faults, though, Volo is a soft-hearted sort who cares for nothing as much as his friends. At present, he is grievously concerned for the well-being of one of them. He begins his request with an air of charm and mystery, but it quickly devolves into tearful sincerity."
> — `sources/adventure-wdh.json:1667` (the first two sentences are the day-one reputation; the last two are the quest opener, see section C)

### A4. Career and books up to Ches 1, 1492 DR (wiki and campaign)

> "Sometime in the late 1480s or early 1490s DR, Volo journeyed to Port Nyanzaru in Chult in order to promote his new book, Volo's Guide to Monsters. He arranged audiences with the seven merchant princes of the city to deliver autographed hardcover copies to them, and of course visited inns and taverns to share stories and sell books for 50 gp each."
> — dump line 52269 (markup removed; refs `ToA5e-p235-236`, `ToA5e-p18`; Tomb of Annihilation, 5e).

> "Following his successful promotional tour, he returned to Waterdeep to take a break and to start working on his next book, Volo's Guide to Spirits and Specters, while he waited for royalty payments for his previous book, Volo's Guide to Monsters, which left him short on coin. However, he struggled on Spirits and Specters, not least because his knowledge of the ghostly variety of spirit was far surpassed by his knowledge of the alcoholic. While pondering it, he passed many of his free hours in the taproom of the Yawning Portal and catching up with friends and old friends."
> — dump line 52272 (refs removed; `WDH-p21-22`, `WDH-p218`; Waterdeep: Dragon Heist, 5e).

> "* ''[[Volo's Guide to Monsters (in-universe)|Volo's Guide to Monsters]]'': a treatise on monster lore, with annotations and comments by Elminster, published sometime in the late 1480s or early 1490s DR."
> — dump line 52316 (bibliography).

> "* ''[[Volo's Guide to Spirits and Specters]]'': an unfinished book that lacked substantial information about insubstantial supernatural beings."
> — dump line 52324 (bibliography; ref `WDH-p21-22`).

> "| The tavern gains a write-up in *Volo's Guide to Spirits and Specters* | +3 |"
> — `sources/Appendix_D_-_Running_the_Tavern.md:960` (Alexandrian fame table; a game effect, not day one).

Alexandrian PDF, `sources/14. Finding Floon.pdf`, printed p.103 (PDF page 2) `[PDF: check with pdftotext -layout]`:
> "DC 10 Wisdom (Insight): Volo is stretching the truth about how much he can pay immediately. (Currently low on cash, Volo is awaiting royalty payments from Volo's Guide to Monsters and he's currently endeavoring to finish Volo's Guide to Spirits and Specters, for which he is certain receive a handsome advance.)"

The campaign has the same state, in a quest file:
> "**DC 10 Wisdom (Insight):** Volo is honest but the 100 gp is a stretch; he is waiting on royalties from *Volo's Guide to Monsters* while his current project (*Volo's Guide to Spirits and Specters*) goes poorly. He does not know Renaer Neverember met Floon after Volo left the Skewered Dragon."
> — `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:100`. The "100 gp" clause and the last sentence are quest-time. The royalty state is day-one.

### A5. The Portal and the house he bought (day-one ownership; the handover is quest-time)

> "Reputed to be haunted, Volo had purchased the property for research material. Much later, Volo may have come cap in hand to the successful adventurers to ask for funding for his next expedition."
> — dump line 52274 (refs removed). The first sentence is the day-one purchase. The sentences before it in the same paragraph (the 1492 disappearance and the hire) are quest-time (section C). The "Much later" sentence is after Ches 1 and is not day-one.

> "Volo recently bought the property because it is rumored to be haunted, and he was hoping that investigating it might yield a chapter for his next book, {@i Volo's Guide to Spirits and Specters}."
> — `sources/adventure-wdh.json:2962` (reward text; the purchase is day-one, the handover is quest-time)

> "Trollskull Manor has had a string of owners. Ulkoria once owned the tavern and sold it to a family of shield dwarves, who fell on hard times and sold it to a woman who ran it as an orphanage. She turned out to be a hag who cooked and ate the children. Volo bought the building recently, hoping its haunting would give him a chapter for his next book."
> — `campaign/gazetteer/waterdeep/north-ward.md:198` (North Ward gazetteer, "Lore"; the building's owners are day-one lore)

> "{@creature Emmek Frewn|WDH}, a salty northerner (NE male Illuskan {@creature commoner}), recently tried to buy the tavern in Trollskull Alley but was outbid by Volothamp Geddarm. Stung by the loss, he bought a smaller, less impressive building in the same alley and turned it into a pub, which he calls Frewn's Brews."
> — `sources/adventure-wdh.json:4237` (section "Business Rival: Emmek Frewn", line 4233)

> "The bombastic world traveler {@creature Volothamp \"Volo\" Geddarm|ToA|Volothamp Geddarm} is enjoying some downtime in Waterdeep following a successful book tour promoting his latest work, {@book Volo's Guide to Monsters|vgm}. He spends most of his free time in the taproom of the Yawning Portal, reuniting with old friends and mulling over his next book project."
> — `sources/adventure-wdh.json:32703` (Appendix B, page 218)

### A6. Appearance

> "Volo was considered handsome and in his own estimation even extraordinarily handsome. He had a moustache and a beard he kept neatly trimmed. He habitually wore a floppy velvet beret that was considered stylish but which had become tatty. It was sometimes adorned with a feather that would droop and look more sad than dashing."
> — dump lines 52119 (markup and refs removed). The beret and feather are the wiki's description from the 1360s and 1480s DR.

> "He also often wore a once-white loose shirt, leather vest, and breeches and sometimes added a scarf."
> — dump line 52119 (markup removed; same paragraph).

Adventure, the quest opener (the look is day-one, the speech is quest-time):
> "The figure who approached you strokes his mustache, adjusts his floppy hat, and tightens his scarf."
> — `sources/adventure-wdh.json:1672`

### A7. Magic and skills

> "Beginning again as a wizard in the late 1480s DR and early 1490s DR, he prepared only comprehend languages, detect magic, disguise self, friends, mending, and prestidigitation."
> — dump line 52122 (spell-name link markup removed; refs `ToA5e-p235-236`, `WDH-p218`). This is the only Ches-1-era spell list in the sources.

> "As of the late 1480s DR, Volo fought with a dagger."
> — dump line 52176 (refs `ToA5e-p235-236`, `WDH-p218`).

> "As of the early 1360s DR, Volo was a wizard of only modest ability."
> — dump line 52122 (the 1360s date; not day one).

### A8. Imprisonment and the Spellplague (wiki; cites WDH p167, not verified in the adventure)

> "For whatever reason, Elminster eventually made good on this threat and trapped Volo in an imprisonment spell, in a state of stasis, as punishment for whatever he'd done this time."
> — dump line 52258 (markup and refs removed; refs `TEV-2021-02-23`, `WDH-p167`).

> "Conveniently, Volo was still caught like this when the Spellplague struck in the 1385. With him being one of Mystra's Weave anchors, the magic fortunately did not go awry, injure him, or end prematurely. Unfortunately, he remained trapped in this state for decades, unageing and unaware of the world that moved far beyond what he'd written of in his guides."
> — dump line 52260 (refs removed).

> "Following his release, he was later informed by Elminster about the events of the Spellplague and the transference of parts of Abeir and Toril, though Volo scarcely understood the explanations."
> — dump line 52262 (ref `WDH-p167`).

Checks: Grep of `sources/adventure-wdh.json` for "stasis", "imprison", "frog" and "toad" found no Volo line. No campaign file mentions Volo's stasis (grep). Unverified: see F8.

### A9. Weave anchor (wiki; a hidden fact)

> "Unbeknownst to Volo, he was in fact a Weave anchor, being imbued by Mystra with her divine fire as a way to prevent the Weave from collapsing should anything happen to the goddess of magic, again."
> — dump line 52134 (refs removed).

> "For security, this was a secret known only to Mystra and Elminster, and kept secret from Volo himself, lest he boast and blab about it. This had no effect on his person, thoughts, habits, or any other aspect of his life."
> — dump line 52134 (refs removed). The wiki's "goddess of magic" is Mystra; the campaign uses "god of magic" for titles (brief ruling 11).

Campaign grep for "Weave anchor" returned no Volo line. This is a secret that would change play if used, so the Background must not state it without a GM decision (brief ruling 17).

### A10. Brotherhood of the Cloak (wiki; minor)

> "Volo was an honorary member of the Brotherhood of the Cloak of Mulmaster. The membership was granted to him by the Senior Cloak Thurndan Tallwand personally, in exchange for Volo's silence on his sources used in writing the infamous and legendarily suppressed work, Volo's Guide to All Things Magical."
> — dump line 52152 (markup removed; ref `IM-p28`).

---

## B. Alignment, species, pronouns, stat block

**Summary line (page L5):** "- *Illuskan human chronicler, chaotic good, he/him*. Stat block: **Mage (with modifications)**." — `campaign/setting/notable-figures/independents-allies/01-volothamp-volo-geddarm.md:5`

**Alignment**
- Wiki 5e: "| alignment5e    = [[Chaotic good]]" — dump line 52099. Wiki 2e: "| alignment2e    = [[Chaotic good]]" — dump line 52085.
- Adventure: no alignment is given for Volo. `sources/adventure-wdh.json:32699` to `:32706` (Appendix B) gives none.
- Chaotic good is wiki-only (5e and 2e). Not conflicting. Tag `[research]` if the drafter keeps it.

**Species**
- Wiki: "| race           = [[Human]]" — dump line 52052.
- Wiki prose: "was a widely traveled [[human]] [[wizard]] and sage of [[Faerûn]]" — dump line 52104 (markup removed).
- Adventure: "The bombastic world traveler {@creature Volothamp \"Volo\" Geddarm|ToA|Volothamp Geddarm} is enjoying some downtime in Waterdeep" — `sources/adventure-wdh.json:32703` (no species word).

**Ethnicity (the page says "Illuskan")**
- Wiki: "| ethnicity      = " (blank) — dump line 52053.
- Adventure: no ethnicity for Volo. The page label "Illuskan" has no source. Brief ruling 5 says Faerûn ethnicity. See D2.

**Pronouns**
- Wiki: "| sex            = Male" — dump line 52051.
- Adventure: "He spends most of his free time in the taproom of the Yawning Portal" — `sources/adventure-wdh.json:32703`.
- Page: "he/him" (L5). Consistent.

**Stat block (the page says "Mage (with modifications)")**
- Wiki: "| challenge5e    = {{Frac|1|4}}" — dump line 52100. "| class5e        = {{Class table|edition=5e|[[Wizard]]|1}}" — dump line 52101 (refs `ToA5e-p235-236`, `WDH-p218`).
- Adventure: the Appendix B entry has no stat block (`sources/adventure-wdh.json:32699` to `:32706`). The quest opener and the Enchiridion give none.
- No source says "Mage". Grep of `sources/` for "Mage (with" returned nothing. See D3.

**Title and occupation**
- Wiki: "| occupation     = Writer, sage, traveler" — dump line 52054.
- Adventure, quest opener (quest-time speech, but the title is day-one): "Volothamp Geddarm, chronicler, wizard, and celebrity, at your service." — `sources/adventure-wdh.json:1672`.

---

## C. Quest-time sentences on the current page (and the voice profile)

Brief ruling 1: restate as day-one, or remove and route. Each row gives the page line, the sentence, and where the quest fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L7 | "- **Featured in:** **Finding Floon**, **Trollskull Alley**" | Route. Both quests name Volo | `campaign/quests/act-i/finding-floon/overview.md:48`; `campaign/quests/act-i/trollskull-alley/overview.md:6` |
| 2 | L11 | "Volo should inspire amusement with his inflated self-importance, endearment with his tearful concern for Floon, and exasperation when his generosity turns out to be a tavern deed instead of gold." | The "tavern deed instead of gold" clause is quest-time (the reward). Restate as a habit: "his generosity is often a grand gesture that turns out smaller than promised" | Deed: `campaign/quests/act-i/finding-floon/ev-04-xanathar-sewer-hideout.md:130` (see E4) |
| 3 | L13 | "Volo most often feels bombastic self-assurance, open affection for friends, theatrical distress, cheerful obliviousness to his own reputation, wounded dignity, and impulsive generosity he cannot afford." | Day-one. Keep (ruling 3) | Soft heart: `sources/adventure-wdh.json:1667` |
| 4 | L15 | "Volo wants to promote his latest book, protect his friends at any cost (especially Floon and Renaer), and find the next subject worthy of a Volo's Guide." | Day-one. Keep | Book: dump line 52272 (A4). Friends: dump line 52112 (A3) |
| 5 | L21 | "To the world, Volo is a bombastic chronicler, wizard, and celebrity who trusts you have noted the violence in our fair city." | Day-one in form. The phrase echoes the hiring speech | Quote is the opener: `sources/adventure-wdh.json:1672` ("I trust you've noted the violence in our fair city these past tendays.") |
| 6 | L25 | "Volo is a close friend of Floon Blagmaar and Renaer Neverember, the man who outbid Emmek Frewn for the Trollskull Manor deed (which he gives to the party), and a regular at the Yawning Portal who has worn out his welcome with Durnan at least twice." | Mixed. "(which he gives to the party)" is quest-time. "the man who outbid Emmek" is a conflict (D1). "worn out his welcome with Durnan at least twice" has no source (F6) | Gift: `campaign/quests/act-i/finding-floon/ev-04-xanathar-sewer-hideout.md:130`; `sources/adventure-wdh.json:2962`. Outbid: `sources/adventure-wdh.json:4237` |
| 7 | L29 | "He hires the party to find his missing friend Floon Blagmaar." | Quest-time (the hire). Restate as a standing habit or cut | Hire: `campaign/quests/act-i/finding-floon/overview.md:48`; `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:96` |
| 8 | L29 | "Volothamp Geddarm is a bombastic chronicler, celebrity wizard, and self-promoter who drinks at the Yawning Portal and occasionally writes guidebooks to places he may not have visited." | Day-one habits and books. Keep. The page's Overview is GM text (ruling 19) | Books: dump line 52316 (A4); Portal: dump line 52272 (A4) |

**Voice profile quest-time clauses (`.claude/skills/character-voices/voices/independents-allies.md`):**

- Line 14, Personality in speech: "His generosity arrives as a grand gesture that turns out to be smaller, or stranger, than promised (a deed, not gold)." — quest-time clause (the deed). The rest of line 14 is day-one. Drafter: restate as a habit (ruling 16 change is for the orchestrator).
- Line 19, Sample line, Greeting: "Ah! Adventurers! You'll have heard of me, of course; Volothamp Geddarm, author, wizard, and, I'm told, something of a legend. Sit, sit!" — said to the party at the Portal, so it is the quest opener. The greeting is usable as a day-one habit for any adventurers.
- Line 20, Sample line, Business: "My dear friend Floon has vanished, and I fear the very worst, and I will pay you handsomely, well, handsomely-adjacent, to find him." — quest-time (Floon vanishes; the hire). Route to Finding Floon.
- Line 21, Sample line, Under pressure: "Floon? Floon! Oh gods, is he — tell me he's breathing. Tell me!" — quest-time (Floon found hurt). Route.
- Lines 8 to 17 (Sound, Sentence shape, Word choice, Swearing, Personality in speech apart from line 14's deed clause, Quirks, Signature phrases, Never) have no quest-time clause.

**Where the quest-time facts already live:**
- Hire and reward: `campaign/quests/act-i/finding-floon/overview.md:48`, `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:96`, `campaign/quests/act-i/finding-floon/ev-04-xanathar-sewer-hideout.md:130`.
- Dock Ward last sighting: `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:116`.
- Deed in the North Ward: `campaign/gazetteer/waterdeep/north-ward.md:64` ("- Hook: Volo gives the party the deed for finding Floon, and the building becomes their home base.").

---

## D. Conflicts

**D1. The Trollskull deed: who outbid Emmek and who bought the building**
- Page L25: "Renaer Neverember, the man who outbid Emmek Frewn for the Trollskull Manor deed (which he gives to the party)".
- Adventure: "{@creature Emmek Frewn|WDH}, a salty northerner (NE male Illuskan {@creature commoner}), recently tried to buy the tavern in Trollskull Alley but was outbid by Volothamp Geddarm." — `sources/adventure-wdh.json:4237`.
- Adventure: "Volo recently bought the property because it is rumored to be haunted" — `sources/adventure-wdh.json:2962`.
- Wiki: "Reputed to be haunted, Volo had purchased the property for research material." — dump line 52274.
- Campaign: "Volo bought the building recently, hoping its haunting would give him a chapter for his next book." — `campaign/gazetteer/waterdeep/north-ward.md:198`.
- Higher ranked: the published adventure, which the campaign's own gazetteer agrees with. The page is wrong on the buyer. Drafter: Volo bought the building.

**D2. Ethnicity**
- Page L5: "Illuskan human chronicler". Wiki: "| ethnicity      = " (blank) — dump line 52053. Adventure: no ethnicity.
- Wiki birth detail: "He was named for the city of Volothamp in Calimshan" — dump line 52180. Not a conflict, but Calimshan is where he was named and spent early childhood. Brief ruling 5 says use a Faerûn ethnicity. The sources give none; the drafter needs a decision.

**D3. Stat block**
- Page L5: "Stat block: **Mage (with modifications)**."
- Wiki: "| challenge5e    = {{Frac|1|4}}" and "| class5e        = {{Class table|edition=5e|[[Wizard]]|1}}" — dump lines 52100 to 52101.
- Adventure: no stat block (`sources/adventure-wdh.json:32699` to `:32706`).
- Conflict: the wiki gives a Wizard level 1 at CR 1/4. The page says Mage. No source in the set gives a Mage stat block. Unresolved.

**D4. A 1492 DR event that puts Volo outside Waterdeep (wiki, Baldur's Gate 3 canon)**
- Wiki: "In the 1492, Volo traveled to the Emerald Grove in the Western Heartlands in order to study the unique behavior of a certain group of goblins. He was subsequently captured by these goblins, who were members of the Cult of the Absolute, and taken to their headquarters at a nearby temple of Selûne, which at least gave him a closer look at his subjects." — dump line 52281 (ref `BG3`). Same line: "Volo's fate is as yet unconfirmed; he may have been rescued by adventurers, or else left in the goblins' clutches."
- Campaign: Volo is in Waterdeep on Ches 1, 1492 DR (`campaign/quests/act-i/finding-floon/overview.md:48`; `campaign/gazetteer/waterdeep/castle-ward.md:46`, "Volo's job offer").
- Conflict: the wiki's BG3 timeline puts Volo's capture in 1492 outside the city. The campaign wins (brief ruling 12). The drafter should not use the goblin capture.

**D5. Floon's disappearance: "two nights ago" in the adventure, "last night" in the campaign**
- Adventure: "Beset by writer's block, Volo met {@creature Floon Blagmaar|WDH} for drinks at the Skewered Dragon two nights ago. They drank and gambled for a few hours, and then Volo left. That's the last he saw of Floon." — `sources/adventure-wdh.json:1686`.
- Adventure: "My friend's name is {@creature Floon Blagmaar|WDH}. ... I worry he took a bad way home a couple nights ago and was kidnapped-or worse." — `sources/adventure-wdh.json:1674` (the ellipsis is a skipped sentence, "He's got more beauty than brains, and I worry he took..." is the quote; read the line for the rest).
- Campaign: "A writer named Volo Geddarm hired the party to find his missing companion, Floon Blagmaar, last seen at a Dock Ward tavern last night." — `campaign/quests/act-i/finding-floon/overview.md:48`.
- Campaign: "He describes Floon Blagmaar: wavy red-blond hair, early thirties, more charming than sensible, last seen at the Skewered Dragon last night wearing princely garb." — `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:96`.
- Campaign: "Floon was kidnapped the night before." — `campaign/guides/gm-guide/structural-rules.md:38`.
- Alexandrian PDF, printed p.103: "Last night he accompanied me to the Skewered Dragon, a dark, bawdy tavern in the Dock Ward." — `sources/14. Finding Floon.pdf`, printed p.103 `[PDF: check with pdftotext -layout]`.
- Higher ranked: the campaign's "last night" (CLAUDE.md, Finding Floon timeline). The page has no "two nights" wording. Stale campaign line: E1.

**D6. Volo's Relationships line on Durnan**
- Page L25: "a regular at the Yawning Portal who has worn out his welcome with Durnan at least twice."
- Durnan page L25: "a reluctant acquaintance of Volo (whom he tolerates)". Neither has a source. Not a conflict, but both are unsourced (F6).

---

## E. Stale lines in other files (not edited) and routed quest references

**E1. Stale line on Floon's timing**
- `campaign/setting/history/08-the-players-arrive.md:128`: "`finding-floon/overview.md` line 49 still says \"two nights before\", as does the published adventure, and both are stale for the remix."
- Actual file: `campaign/quests/act-i/finding-floon/overview.md:48` reads "last seen at a Dock Ward tavern last night." The line-49 claim is stale. Drafter: take "last night" from line 48.

**E2. Campaign-hits index line numbers are off by one**
- `sources/research/pass3-bundles/dock-ward/campaign-hits.txt:59` gives `finding-floon/overview.md:49` for "last night". The current file has it at line 48. Do not cite the index.

**E3. The Emmek fact**
- `campaign/gazetteer/waterdeep/north-ward.md:198` agrees with the adventure (Volo bought the building). It is not stale. The Volo page is the wrong one (D1).

**E4. Routed quest and guide references**
- Finding Floon: `campaign/quests/act-i/finding-floon/overview.md:24` ("- **Volo Geddarm** (independent) — the quest-giver; offers 10 gp upfront and a deed to Trollskull Manor as payment"), `:48`; `ev-01-yawning-portal.md:96`, `:100`, `:116`; `ev-04-xanathar-sewer-hideout.md:112` ("The party holds the deed to Trollskull Manor."), `:130` ("Volo paid with a deed to a derelict tavern called Trollskull Manor in the North Ward.").
- Trollskull Alley: `campaign/quests/act-i/trollskull-alley/overview.md:6` ("> Finding Floon complete. The party holds the deed to Trollskull Manor, received from Volo Geddarm as payment for Floon Blagmaar's rescue. They arrive in the North Ward as 2nd-level characters with no established community and not enough gold.") and `:45` ("- **Volo Geddarm** (independent) — attends the Grand Opening; attempts a review; spills ink on two pages").
- Trollskull Manor guide: `campaign/guides/trollskull-manor/06-tavern-time.md:43` ("| **Finding Floon** or **Trollskull Alley** | Volothamp "Volo" Geddarm |"), `campaign/guides/trollskull-manor/07-events.md:25` ("| 7 †| Volo arrives and wants to arrange a book signing. He has questions about the haunting. | Roleplay. Reroll on second occurrence. |"), `campaign/guides/trollskull-manor/04-fame.md:67` ("| Volo's write-up obtained | +3 |").
- Alexandrian Appendix D: `sources/Appendix_D_-_Running_the_Tavern.md:1173` ("| 7 | Volo arrives and would like to arrange a book signing here. He has questions about the haunting for a new project. ★ † | Roleplay. | Reroll on second occurrence — the signing either happened or it didn't; Volo does not ask twice. |").
- Adventure: `sources/adventure-wdh.json:2940` to `:2973` (the reward scene, "Completing Volo's Quest"); `:1594` to `:1595` (the quest summary).

**E5. The deed as a quest reward**
- `campaign/gazetteer/waterdeep/north-ward.md:64`: "- Hook: Volo gives the party the deed for finding Floon, and the building becomes their home base. The **Trollskull Manor** location journal maps it, and the Trollskull Manor guide runs the tavern."

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

1. **Age, birth year, and when he came to Waterdeep.** No source gives an age or birth year. The wiki birth account has no date (dump line 52180). The campaign never states his arrival. The wiki's only Waterdeep date for him is the caption "A sighting of Volo in Waterdeep in the early 1360s DR." (dump line 52201). Stay consistent with: a Calimshan naming and early childhood (dump line 52180), a son born by 1372 DR (dump line 52141), and a Waterdeep base by the 1490s (dump line 52272).
2. **Where he lives on Ches 1.** No source gives an address. The Yawning Portal taproom is his habit (dump line 52272; `sources/adventure-wdh.json:32703`).
3. **Ethnicity and home region.** See D2.
4. **His faith.** No source. Do not give him a deity.
5. **The stat block.** See D3.
6. **His relationship with Durnan.** Only the page's "worn out his welcome" (L25) and the Durnan page's "whom he tolerates" have no source. The adventure gives no Volo–Durnan exchange. The Enchiridion quotes Durnan (section H4). Stay consistent with: Durnan runs the Portal and tolerates the regulars.
7. **The Spirits and Specters book and its money.** The book is real in the sources (A4). Royalty trouble is in the Alexandrian p.103 and the campaign ev-01 line 100. No source gives an amount.
8. **Elminster and the imprisonment.** Wiki only (dump lines 52258 to 52262). The adventure does not confirm the stasis (A8). The campaign has Elminster as the Warden of Waterdeep: "The current Warden of Waterdeep is Elminster, who answers to the Open Lord, {@creature Laeral Silverhand|WDH}." (`sources/adventure-wdh.json:31836`). No campaign file links Volo and Elminster in a 1492 DR scene.
9. **His son, Emmeros.** Wiki only (dump lines 52071 and 52141). Not in any campaign file (A2). The wiki's citation is Dragon magazine 250. If the drafter names him, tag `[research]`.
10. **Romances: Sa'Sani, Nanthé Ryddorn, Ravithara Silmerhelve.** Wiki only (dump lines 52141 to 52147). None appears in a campaign file as a Volo contact. Ruling 17 allows a named figure only when a source already names them, so these may be named only with `[research]`, and never as a new Notable Figure.
11. **The 14th-century Guide to All Things Magical.** Wiki only (dump lines 52186 to 52227). Campaign mentions of the book are in deity pages as sources for those gods (`campaign/setting/deities/azuth.md:54`, `ilmater.md:53`, `myrkul.md:54`, `mystra.md:47`, `selune.md:37`). No campaign file treats Volo's book as Volo's history. Tag any use `[research]`.

**Searched, not found (Volo, 1492 DR, day one):** his "worn out his welcome" with Durnan (adventure grep for "welcome", "tolerat", and Volo with Durnan: no Volo–Durnan exchange); a "Mage" stat block (adventure, wiki, Alexandrian); an "Illuskan" ethnicity (adventure, wiki); his faith; his home address; his age.

---

## G. Inner-life hints in the sources (exact quotes)

These are the sourced hints a Background or the personal goals may use. They must not be contradicted.

- **Soft heart.** "Despite his flaws, however, Volo was soft at heart and he cared for his friends most of all, at least those friends he had." — dump line 52112 (refs removed). Also `sources/adventure-wdh.json:1667`: "For all his faults, though, Volo is a soft-hearted sort who cares for nothing as much as his friends."
- **Fear of not being believed (campaign, day one).** "Deep down, he knows his reputation as an embellisher is earned, and it terrifies him that someday no one will believe him when it matters." — `campaign/setting/notable-figures/independents-allies/01-volothamp-volo-geddarm.md:21`. Voice: "His fear of not being believed shows as over-insistence." — `.claude/skills/character-voices/voices/independents-allies.md:14`.
- **Restless feet and a love of the tavern.** "Volo himself claimed to have restless feet and a love of travel, of seeing new things and living life to the full, though his may just have been an excuse for his forced journeys. He considered anything outside the towns and cities to be boring and hazardous." and "He much preferred the setting of a pleasant tavern or festhall to trekking through a jungle, ruins, or dungeon, and he tended to indulge himself." — dump line 52114 (refs removed).
- **Hides his drinking ability.** "Less professionally, Volo could drink incredible quantities of alcohol without getting drunk. Instead, he would pretend to be inebriated so as to hide the ability and let rivals and foes underestimate him or act overconfident." — dump line 52128 (refs removed).
- **Fear of wizards.** "Having earned the ire of various wizards following All Things Magical, Volo had to take efforts to hide his identity from them, lest he lose his head—or worse!" — dump line 52168 (refs removed).
- **Vow to be careful.** "He would not speak of these, but vowed he would be \"a very good boy where dealings with wizards are concerned for a long time to come.\"" — dump line 52202 (refs removed).
- **Money trouble.** "Currently low on cash, Volo is awaiting royalty payments" — `sources/14. Finding Floon.pdf`, printed p.103 `[PDF: check with pdftotext -layout]`. Also dump line 52272 ("which left him short on coin").
- **Self-image.** "Volo has an inflated opinion of himself and his importance in the world, but he's not without his charm. There is nothing he won't do to help a friend in need." — `sources/adventure-wdh.json:32704`.
- **The house he bought for a book.** "he was hoping that investigating it might yield a chapter for his next book" — `sources/adventure-wdh.json:2962`.
- **Concern for Floon.** "At present, he is grievously concerned for the well-being of one of them." — `sources/adventure-wdh.json:1667`. The page's Motivations: "protect his friends at any cost (especially Floon and Renaer)" — page L15.
- **Voice's sample aside (style only).** "I have laid violets beneath Ahghairon's tower on his day, among a great many commoners (a charming custom, and a cheap one, which matters to a man on my budget) who all kept a careful distance from the cage. I kept it too. The bones of the last fellow who tried the door hang beyond the barrier still, and one look settled my choice." — `.claude/skills/character-voices/voices/independents-allies.md:44` (whole aside quoted). The voice doc marks the asides "style only" (line 41: "*Sample asides (style only):*"). Do not treat as campaign fact. The consistency note says the four asides are not on the page (`docs/plans/setting-compendium-research-notes/consistency-notable-figures.md:18`).

---

## H. How Volo knows things (ruling 19: anecdotes, hearsay, rumors, where a source gives them)

**H1. Elminster's account of Volo's method (wiki; the only source that describes how Volo gathers facts)**
> "Volo's research methods on All Things Magical were, according to Elminster, assorted notes, gossip, and stolen glances at other mages' spellbooks, with things hastily and secretly scribbled down when he had the chance or else hazily remembered when he did not."
> — dump line 52160 (markup and refs removed). The same line: "he described Volo's best skill as \"spying and then reporting everything folk would fain keep secret for good reason.\""

**H2. Volo's own account of his sources (wiki; the revised 1367 DR guide)**
> "This time, he claimed to use only secondhand sources: interviews, legends, and stories, all documented, verifiable, and publicly available, with no stolen secrets (not that he admitted to having used any the first time around)"
> — dump line 52225 (ref `RoM-p4`). Dated 1367 DR, not day one.

**H3. Rumors overheard in taverns (wiki; Chult, not Waterdeep)**
> "He gladly shared the latest rumors, advice, and information he'd overheard since arriving in town to any travelers and adventurers he met, and some of it was even true."
> — dump line 52269 (refs removed).

**H4. Volo quotes Durnan in his own Enchiridion (adventure; the speaker is Volo's book)**
> "\"The only mortals that Waterdavians fear are a few unstable wizards and the Lords,\" {@creature Durnan|WDH} often says to those who are surprised by the nonchalance of the Yawning Portal's regulars concerning the open entrance to Undermountain in their midst. \"And only when they've incurred the wrath of said persons themselves.\""
> — `sources/adventure-wdh.json:30712` (Chapter 9, "Volo's Waterdeep Enchiridion", which starts at `:30419`; the Castle Ward section starts at `:31003`). This is the only Volo-voice passage in the sources that quotes Durnan. It implies Volo heard Durnan speak at the Portal. It does not say so.

**H5. Volo's own account of Floon's last sighting (quest opener; quest-time)**
> "Beset by writer's block, Volo met {@creature Floon Blagmaar|WDH} for drinks at the Skewered Dragon two nights ago. They drank and gambled for a few hours, and then Volo left. That's the last he saw of Floon."
> — `sources/adventure-wdh.json:1686`. Quest-time (route to Finding Floon). See D5 for the timing.

**H6. Volo's knowledge of Renaer and Durnan**
- No source says how Volo knows Renaer or Durnan.
- The campaign says what Volo does not know: "He does not know Renaer Neverember met Floon after Volo left the Skewered Dragon." — `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:100` (quest file).
- The voice profile on how Volo reports: "He knows because he went, asked, and was thrown out, fined, followed or fed." — `.claude/skills/character-voices/voices/independents-allies.md:33`. "Hearsay is marked as hearsay." — line 34. These are voice rules, not facts about the campaign.

**H7. Campaign citation pattern (how the campaign already cites Volo's book)**
> "Volo and Elminster wrote that, by report, her hut had appeared near Rashemen in north-eastern Faerûn in the 14th century DR (*Volo's Guide to All Things Magical*)."
> — `campaign/setting/deities/baba-yaga.md:38`. The campaign tags Volo-sourced facts "by report". This is a pattern for citing Volo's books, not a fact about his life.

---

## Not readable

- `sources/SOURCE_GUIDE.md` lists `The Waterdavian's Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx` as a broad NPC reference. It may name Volo. It could not be opened with the tools. Extract it and check for Volo.
- No individual Volo NPC guide is listed in `SOURCE_GUIDE.md`.

## Cross-references (other `file:line` where Volo appears)

- `campaign/gazetteer/waterdeep/dock-ward.md:8`: "> - **Finding Floon** is set here from start to finish. Volo sends the party to the Skewered Dragon, the Dock Ward investigation leads to the Candle Lane warehouse, and the sewers below the ward lead to the Guild hideout where Floon is held."
- `campaign/gazetteer/waterdeep/castle-ward.md:46`: "- Hook: the campaign opens here with a brawl, a troll out of the well and Volo's job offer. Patrons sing a bawdy song when someone goes down, and a faction contact is usually at a table."
- `campaign/gazetteer/waterdeep/north-ward.md:64` and `:198`: see E5 and D1.
- `campaign/setting/history/08-the-players-arrive.md:67`: "- Volothamp Geddarm hires the party at the Yawning Portal on the evening of Ches 1. The era ends with the party walking into a room where every thread above is already moving."
- `campaign/setting/history/08-the-players-arrive.md:118`: lists "**Volothamp "Volo" Geddarm**" among the people named.
- `campaign/guides/trollskull-manor/08-notable-patrons.md:94`: "- News: Volo's Guide is being updated; there's a researcher asking about notable establishments; Broxley suggested the Trollskull".
- `sources/Appendix_D_-_Running_the_Tavern.md:1415`: "4. Has news: *Volo's Guide to Waterdeep* is being updated. There is a researcher asking around about notable establishments. Broxley has suggested the Trollskull. This is not something he had to do. He has done it." (a Broxley entry; Volo is not the speaker).
- `docs/plans/setting-compendium-research-notes/consistency-notable-figures.md:14` and `:18`: earlier notes on this page (Renaer's Harper status; the four asides).

## Not found (search terms and files)

- Volo + "welcome", "tolerat", "Durnan": `sources/adventure-wdh.json` (no hit), `campaign/` (only the page's L25 and the Durnan page's L25).
- "Mage (with", and Volo + "Mage": `sources/` and `campaign/` (no source).
- "Illuskan" + Volo: `sources/adventure-wdh.json` (no hit); wiki dump (ethnicity blank).
- "Emmeros", "Silmerhelve" + Volo: `campaign/` (no Volo file).
- "stasis", "imprison", "frog", "toad" + Volo: `sources/adventure-wdh.json` (no Volo hit).
- "Weave anchor": `campaign/` (no Volo hit).
- "Sa'Sani", "Spirits and Specters": `campaign/` (only `ev-01-yawning-portal.md:100` and the Appendix D fame row).
- `sources/Appendix_B_-_Player_Factions.md`: no Volo line (Grep "Volo" returned none).
