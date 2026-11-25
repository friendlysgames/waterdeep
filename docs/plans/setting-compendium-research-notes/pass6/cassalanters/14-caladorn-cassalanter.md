# Pass 6 research notes: Caladorn Cassalanter

Page: `campaign/setting/notable-figures/cassalanters/14-caladorn-cassalanter.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR. Caladorn is dead. His ghost is bound to the family crypt (A4a). Quest-time ghost behaviour (the trigger, the lucid state, the vow, the mace hand-over) is routed, not day-one. Cassalanter secrecy applies: no source says the public knows of the ghost.
Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-cassalanters/14-caladorn-cassalanter.txt`. Quoted as "wiki line N" (that file's lines). Citation keys are as printed (CoSW-p54, CoSCG-p69, BST-p198, WDH5e-p128, WatN-p16, Tangled Webs, Elfsong, Windwalker). The wiki prints no edition on the page; the edition is inferred from the key and from the campaign's tags.
Method: Read and Grep only. Quotes are copied from tool output. Line numbers are file lines. JSON escapes are shown as plain quotes.
PDFs: `sources/10. Lair  Cassalanter Villa.pdf` (PDF pp.1-6, printed pp.77-82) and `sources/1. The Villains.pdf` (PDF pp.6-7, printed pp.18-19) were read as page images. Neither names Caladorn. No PDF text is quoted. Run `pdftotext -layout` before any PDF quote enters prose.
Not run: `voicecheck.py`. No file was edited except this notes file.

## Findings that change how the page is written

1. **The ghost's trigger conflicts across sources.** The campaign's crypt file says the ghost attacks anyone who "has participated in Asmodean worship, carries an infernal mark, or is a cult member" (`campaign/locations/cassalanter-villa/15-family-crypt.md:21`). The published adventure says the undead "attack any living creatures but can't leave the crypt or approach within 5 feet of any creature that wears a holy symbol of Asmodeus" (`sources/adventure-wdh.json:22712`). Both agree the Siamorphe symbol halts him (D1).
2. **The vow has three wordings.** `arc-g-cassalanter-villa.md:139` and `15-family-crypt.md:29` differ from each other and from `sources/adventure-wdh.json:22729` (D2).
3. **Office conflicts.** The wiki says "Open Lord" by 1399 DR (wiki line 90). The campaign and the adventure keep "former Masked Lord" (D3).
4. **Alignment conflicts.** The campaign says lawful good (page line 5). The wiki's 2e and 3e fields say neutral good (wiki lines 46 and 53). No campaign or adventure source gives lawful good (D4).
5. **Hair conflicts with the wiki.** The wiki gives living hair as "short dark red or brown" (wiki line 68). The campaign gives "silver-haired" for the portrait and the ghost (D5).
6. **The portrait location.** The page says "the entrance hall upstairs" (line 21). The entrance-hall file says a two-story foyer with a grand staircase, with Caladorn "near the stair" (D6).
7. **"Three years" has one source, and it is a structure document.** `campaign/structure/arc-g-cassalanter-villa.md:135` says "His ghost has been raging in silence for three years". `arc-g-cassalanter-villa.md:491` repeats it. No setting or adventure source gives the date (F2).
8. **"Twelve feet away" has no source.** It appears only in the page (line 21) (F3).
9. **Death date, cause and wife's name: none.** The wiki says "After his death" with no date (wiki line 92). The adventure says "the late" (`sources/adventure-wdh.json:18404`). The wife is unnamed in every file (F1).
10. **Victoro's page invents Caladorn's past.** `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:21` ([design]) says "Caladorn spent long seasons in the North" and that he repaid a failed loan out of the house's plate and warehouses. The Caladorn Background must not contradict this (G3).
11. **Quest-time text sits on setting pages (not to be edited).** `campaign/setting/villains/cassalanters.md:36` and `campaign/setting/deities/siamorphe.md:62`, `:63` and `:70` describe the ghost's hand-over and the party's quest. See E.
12. **The Organization page's history is the fullest campaign statement.** `campaign/setting/organizations/10-cassalanters.md:22` gives Caladorn's name-shedding, Masked Lord service and fatherhood in one paragraph, with edition tags 1e, 3e and 5e (A1, A3).

---

## A. Background facts by theme

### A1. Origin, the noble house and the name he set aside (campaign, wiki)

> "- **The 14th and 15th centuries DR, a banking fortune and a Masked Lord:** The wiki says the house made its fortune in banking, money-lending and rumor-mongering for the highest payer, and names Ohrl Cassalanter as its patriarch (Forgotten Realms Wiki, *Cassalanter*, 1e) `[research: wiki only]`. Ohrl's son Caladorn set the family name aside until he had done something worthy of it (Forgotten Realms Wiki, *Caladorn Cassalanter*, 1e and 3e). He served as a Masked Lord, earned the title of hero of the North and fathered Victoro (*Dragon Heist*, 5e). His ghost now waits in the family crypt below the villa, where it attacks anything with a fiendish taint (**Caladorn Cassalanter**). Campaign change: the wiki also makes him an Open Lord, and the campaign keeps him a Masked Lord only (**The Open Lord and the Masked Lords**)."
> — `campaign/setting/organizations/10-cassalanters.md:22` (Historical entry; the paragraph is the Organization's History bullet)

> "- **Origins:** The Cassalanter name has stood in Waterdeep's noble registry for several generations. The Lords of Waterdeep ennobled the house in 1248 DR, about 244 years before the campaign, when they granted titles to several merchant houses (Forgotten Realms Wiki, *City of Splendors: Waterdeep*, 3e)."
> — `campaign/setting/organizations/10-cassalanters.md:114` (GM Notes)

> "A member of the noble family of [[Cassalanter]], one of the richest families in Waterdeep, <ref name=\"TW-p23\"/> Caladorn ceased using his family's name until he had done \"something worthy of it.\"<ref name=\"WatN-p16\"/> His father, Lord [[Ohrl Cassalanter]], believed that Caladorn would never deem himself worthy, and so he was left with the benefits of his birthright but none of the responsibilities.<ref name=\"CoSW-p54\"/>"
> — wiki line 78 (Early Life; keys TW-p23, WatN-p16, CoSW-p54; the edition is not printed; the campaign tags the CoSW key 3e at `campaign/setting/history/05-a-debt-in-blood.md:32`)

Context: the wiki's "something worthy of it" is the source for the name-shedding. The Organization page carries it at line 22 and tags it 1e and 3e (Forgotten Realms Wiki, *Caladorn Cassalanter*). Edition tags for the same wiki page differ across campaign files (E9).

### A2. Parents and siblings (wiki; the wife is unnamed)

> "Caladorn was the third son of [[Ohrl Cassalanter|Lord Ohrl]],<ref name=\"CoSW-p54\"/> and [[Sylull Cassalanter|Lady Sylull Cassalanter]].<ref name=\"CoS.NHoW-p2\">{{Cite web enhancement/Noble Houses of Waterdeep|2}}</ref>"
> — wiki line 95 (Relationships)

> "| parents        = [[Ohrl Cassalanter]] (father)"
> — wiki line 32 (infobox). Mother: none in the infobox.

> "| children       = [[Victoro Cassalanter]]"
> — wiki line 35 (infobox)

> "Lord {@creature Victoro Cassalanter|WDH} is the only living heir of the late Caladorn Cassalanter, a former Masked Lord and a hero of the North."
> — `sources/adventure-wdh.json:18404` (Ch.6 public overview, page 116)

> "- **Caladorn Cassalanter:** Victoro's father. The wiki has him a Masked Lord and later Open Lord of Waterdeep, by 1399 DR (*Blackstaff Tower*, 2e and 3e)."
> — `campaign/setting/organizations/10-cassalanters.md:123` (GM Notes)

Context: "Ohrl Cassalanter appears only in the wiki (`sources/research/pass4-bundles/cassalanters/wiki.txt` lines 383 and 544-545), and no campaign file names him" — `campaign/setting/organizations/10-cassalanters.md:179` (Research note). The History page tags him `[research: wiki only]` (`campaign/setting/history/07-a-city-watching-itself.md:36`). Sylull is named only by the wiki.

### A3. Early life and service as a Masked Lord (campaign and wiki)

> "Caladorn Cassalanter ... was a young and gallant secret [[Masked Lord]] and later [[Open Lord]] of [[Waterdeep]], who served during the 14{{th}} and 15{{th}} centuries [[DR]]."
> — wiki line 65 (lead; the copy at `sources/research/pass4-bundles/cassalanters/wiki.txt:416` carries the same line). The Organization page quotes it as "was a young and gallant secret Masked Lord and later Open Lord of Waterdeep" (`campaign/setting/organizations/10-cassalanters.md:188`).

> "Caladorn was quite perceptive and intelligent. He acted with purpose,<ref name=\"TW-p23\"/> and had a cynical outlook,<ref name=\"CoSCG-p69\" /> but he loved to have fun in private, when the occasion called for it.<ref name=\"CoSW-p54\"/> He was considered to be the epitome of the \"Knight Bachelor\".<ref name=\"WatN-p16\"/>"
> — wiki line 71 (Personality)

> "As lord, was very interested in the city's navy and understood the challenges they had in maintaining order around the [[Sea of Swords]].<ref name=\"CoSW-p54\"/> Those who were unaware of his position with the Lords of Waterdeep thought him a simple fighting instructor at the Fields of Triumph.<ref name=\"CoSWW-p12\">..."
> — wiki line 74 (Activities; key CoSWW-p12 is "City of Splendors (boxed set)/Who's Who in Waterdeep")

> "Caladorn was a fighter through and through – broad-shouldered, and {{SI|6|ft}} tall.<ref name=\"CoSW-p54\"/> He had short dark red or brown hair and was clean-shaven<ref name=\"CoSW-p54\"/>, with a prominent cleft chin.<ref name=\"CoSCG-p69\" /> He was somewhat older than his friend [[Danilo Thann]].<ref name=\"ESo-p28\">{{Cite book/Elfsong|28}}</ref>"
> — wiki line 68 (Description)

> "- **Affiliation:** The Cassalanters (deceased; ancestral ghost)"
> — `campaign/setting/notable-figures/cassalanters/14-caladorn-cassalanter.md:6` (Summary)

Context for "Masked Lord" status: `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:50` says "**Caladorn Cassalanter** (Lawful Good, Tethyrian Human Ghost, he/him) was a Masked Lord and a hero of the North, and he is Victoro Cassalanter's father." (D3).

### A4. Adventuring years (wiki only; novels and Lords' lore)

> "In the {{YearlinkName|1361}}, Caladorn was traveling on the ship ''[[Cutter (ship)|Cutter]]'', a [[seal]]-hunting ship captained by [[Farlow]] in the [[Sea of Moving Ice]].<ref name=\"TW-24\">...</ref> While he was on the ship, the crew discovered an abandoned ship full of pickled [[sea elf|sea elves]] packed in [[barrel]]s bearing the mark of [[Ruathym]]. It was later discovered to be part of a plot to provoke the [[Lords' Alliance]] into war on Ruathym."
> — wiki line 81 (Adventuring Years; key TW-24 is the *Tangled Webs* novel)

> "Caladorn intended to bring the barrels back to Waterdeep to begin an investigation, but his ship was intercepted by the ''[[Elfmaid (ship)|Elfmaid]]'', which scuttled their ship and marooned the crew. With the help of [[Xzorsh]], Caladorn was eventually able to make it to safety on Ruathym and explain his story."
> — wiki line 83 (key TW, *Tangled Webs*)

> "In the {{YearlinkName|1364}}, Caladorn was courting [[Lucia Thione-Hhune|Lucia Thione]] and planning to marry her. However, Lucia, a high-ranking member of the [[Knights of the Shield]], discovered that he was a Lord of Waterdeep and attempted to poison him in order to keep her true allegiances secret.<ref name=\"ESo-p271-272\">{{Cite book/Elfsong|271-272}}</ref> Heartbroken, Caladorn quit the Lords and his city for two years, traveling the [[Sword Coast]].<ref name=\"CoSCG-p69\" /> After returning to Waterdeep, Caladorn involved himself with the Waterdhavian navy.<ref name=\"CoSW-p54\"/>"
> — wiki line 87 (key ESo = *Elfsong* novel)

> "Caladorn had a servant named [[Anthony]], who was killed by Lucia Thione in [[1364 DR]].<ref name=\"ESo-p271-272\" />"
> — wiki line 99 (Relationships)

Context: these are novel-sourced (Tangled Webs, Windwalker, Elfsong) and wiki-tagged. The brief allows them as the wiki tier, with the edition tagged. Lucia Thione and Anthony are named only by the wiki; neither has a Notable Figures page. Do not create them as figures (brief ruling 17).

### A5. Friends and rivals named by the wiki (wiki only)

> "Caladorn and [[Danilo Thann]] were well-acquainted. It was postulated that Caladorn ran off to join the ''Cutter'' after Danilo chased him away from pursuing his sister [[Judith Thann]].<ref name=\"WW-p??\">..."
> — wiki line 97 (key WW-p?? is unresolved in the wiki)

> "Soon afterwards, Caladorn traveled back to Waterdeep with [[Liriel Baenre]] and [[Fyodor]], helping them to contact [[Danilo Thann]] in order to secure safe passage to the [[Promenade of the Dark Maiden]] near [[Skullport]]."
> — wiki line 85 (key WW = *Windwalker*)

> "He thought highly of the charming [[Randulaith]] who hailed from [[Mirabar]].<ref name=\"CoSW-p65\">..."
> — wiki line 97

### A6. Death, interment and the crypt (wiki and adventure; no date)

> "After his death, Caladorn's body was interned in the family crypt under [[Cassalanter Villa]] in Waterdeep with his plate armor and [[Mace of disruption]]. His [[ghost]] continued to dwell within the crypt, sympathetic to those bore the [[holy symbol]] of [[Siamorphe]].<ref name=\"WDH5e-p128\">{{Cite book/Waterdeep: Dragon Heist|128}}</ref>"
> — wiki line 92 (Later Years and Death; key WDH5e-p128, 5e)

> "The spirits of several dead members of the Cassalanter family are bound to this crypt. They manifest as three dark, vaporous {@creature specter||specters} plus a {@creature ghost} that looks like the insubstantial image of a handsome, clean-shaven man of knightly bearing clad in plate armor."
> — `sources/adventure-wdh.json:22712` (A4 crypt; the rest of the paragraph is in D1)

> "The ghost is all that remains of Caladorn Cassalanter, a former Masked Lord and hero of Waterdeep. The ghost halts its attack and calls off the specters if a character wears or presents a holy symbol of Siamorphe. After it is shown such a symbol, the ghost guides characters to its personal crypt ({@area A4a|33e})."
> — `sources/adventure-wdh.json:22713`

> "Caladorn's bones have turned to dust, but his suit of {@item +1 plate armor} remains. Also lying in the dust is a {@item mace of disruption}."
> — `sources/adventure-wdh.json:22729` (Treasure, A4a, page 128; the next sentences give the vow, see D2)

> "Years after his death, Lord Caladorn was still considered to be a hero of [[the North]].<ref name=\"WDH5e-p198\">{{Cite book/Waterdeep: Dragon Heist|116}}</ref>"
> — wiki line 101 (the key says p198, the cite says 116; the campaign does not use this line)

> "A dusty stone sarcophagus occupies this crypt, its plaster lid carved in the likeness of a handsome, clean-shaven nobleman clutching a chalice engraved with the symbol of the sun. The likeness resembles the ghost of Caladorn Cassalanter (see above)."
> — `sources/adventure-wdh.json:22722` (A4a)

> "CALADORN CASSALANTER — MASKED LORD OF WATERDEEP — SERVANT OF SIAMORPHE IN HIS TIME"
> — `campaign/locations/cassalanter-villa/15-family-crypt.md:9` (plaque, A4a)

> "One sarcophagus here, distinguished from the others by its size and its effigy: an armored figure, silver-haired, with the Cassalanter features and the bearing of someone who carried a weapon all his life."
> — `campaign/locations/cassalanter-villa/15-family-crypt.md:9`

> "**Caladorn's Ghost (A4a).** The ghost manifests when approached. An armored figure, solid-seeming until the eye finds the places where it fails to meet the edges of things — the wall behind him is not quite hidden. The voice is steady. The face is recognizable from the portrait in C1."
> — `campaign/locations/cassalanter-villa/15-family-crypt.md:19`

> "**A4 / A4a — Family Crypt / Caladorn's Crypt.** Twelve sarcophagi in a vaulted chamber. Three specters rise from the floor when a living creature enters — they attack unless shown a Siamorphe holy symbol, at which point they retreat into their sarcophagi and become inert. Beyond A4, a smaller chamber (A4a) holds Caladorn Cassalanter's sarcophagus and his ghost."
> — `campaign/structure/arc-g-cassalanter-villa.md:229`

> "The family crypt opens off the temple's entry. Twelve stone sarcophagi bear the family crest, a sun over a scale in the Siamorphe heraldic tradition, and Caladorn's ghost holds the crypt (**Cassalanter Villa**, location)."
> — `campaign/setting/organizations/10-cassalanters.md:49` (The temple and the crypt)

Context: the Organization's "The family crypt opens off the temple's entry" and the crypt file's "A4 is a vaulted chamber adjacent to the anterior vestibule, reached through a side passage off A3" (`15-family-crypt.md:7`) agree in substance.

### A7. The ghost's standing in the house (campaign, day-one posture)

> "Caladorn's ghost has been raging in silence for three years, unable to leave A4a, unable to stop what his family has done to his legacy."
> — `campaign/structure/arc-g-cassalanter-villa.md:135` (the only source for "three years"; see F2)

> "The Cassalanters have tried to reach the crypt twice and retreated both times."
> — `campaign/structure/arc-g-cassalanter-villa.md:151` (the source for the page's "retreat from A4a twice"; the Victoro page says the same at line 56)

> "The Cassalanters cannot access this path. Caladorn's ghost attacks devil-worshippers on sight — anyone who has participated in Asmodean rituals triggers his hostility."
> — `campaign/structure/arc-g-cassalanter-villa.md:151`

> "- **Caladorn Cassalanter:** His father, whose ghost holds the family crypt and has driven the family out of it twice."
> — `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:56`

### A8. Siamorphe devotion and the public face

> "They are known to worship Siamorphe, a demigod whose ethos is the nobility's right and responsibility to rule."
> — `sources/adventure-wdh.json:18405` (the family's public worship, page 116; not Caladorn's by name)

> "- **Caladorn Cassalanter:** The ghost of Victoro's father was a Masked Lord and hero of the North who devoted his life to Siamorphe. He is bound in the family crypt, off the temple's anterior vestibule, with three specters. His plaque reads \"Servant of Siamorphe in his time,\" and he knows the statue was his wife's image of the goddess before the family defaced it."
> — `campaign/setting/deities/siamorphe.md:61` (Siamorphe page, GM notes; the quest-time lines at 62, 63 and 70 are E2 to E4)

> "- **The Open Lord and the Masked Lords (neutral):** The Lords of Waterdeep ennobled the house in 1248 DR, and Caladorn sat among the Masked Lords, so the family still shows his portrait as a sign of civic virtue (**The Open Lord and the Masked Lords**)."
> — `campaign/setting/organizations/10-cassalanters.md:89`

> "> - **Featured in:** **Trollskull Alley** (Ulkoria Stonemarrow in **The Neighbors**), **Gralhund Villa** (Yalah Gralhund's bid for a seat), **Cassalanter Villa** (Caladorn Cassalanter's portrait), **Kolat Towers** (the list of Masked Lords in Manshoon's drawer), and **Vault of Dragons** (Laeral's one legal intervention and the Masked Lord's Writ)."
> — `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:9`

### A9. The portrait in the house (public)

> "The walls are hung with Cassalanter ancestor portraits — Caladorn Cassalanter is prominently placed near the stair, silver-haired and armored in the heraldic style of the North."
> — `campaign/locations/cassalanter-villa/01-entrance-hall.md:3`

> "Portraits carry information for observant players. A DC 14 Intelligence (History) check on Caladorn's portrait identifies him as a former Masked Lord and Siamorphe devotee."
> — `campaign/locations/cassalanter-villa/01-entrance-hall.md:17`

> "C1 — Entrance Hall. Two-story foyer with marble floors and a grand staircase. Portraits of Cassalanter ancestors line the walls — Caladorn is prominently placed, silver-haired and armored."
> — `campaign/structure/arc-g-cassalanter-villa.md:191`

### A10. Personal goals and the ghost's motives (campaign)

> "**Motivations.** Caladorn wants to see the infernal corruption of his house ended, the effigy in A7 destroyed, and some portion of the honor his family carried for generations restored to the name he left behind. He does not want revenge on Victoro and Ammalia. He wants the bargain broken."
> — `campaign/setting/notable-figures/cassalanters/14-caladorn-cassalanter.md:15`

## B. Alignment, species, pronouns, stat block

**Alignment**
- Page: "*Tethyrian human ghost of a Cassalanter noble, lawful good, he/him*. Stat block: **Ghost**." — `campaign/setting/notable-figures/cassalanters/14-caladorn-cassalanter.md:5`
- Organization: "- **Caladorn Cassalanter** — Tethyrian human ghost of a Cassalanter noble, lawful good. See the **Caladorn Cassalanter** page in Notable Figures." — `campaign/setting/organizations/10-cassalanters.md:106`
- Governance: "**Caladorn Cassalanter** (Lawful Good, Tethyrian Human Ghost, he/him) was a Masked Lord and a hero of the North, and he is Victoro Cassalanter's father." — `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:50`
- Wiki 2e: "| alignment2e    = [[Neutral good]]" — wiki line 46 (key CoSCG-p69, line 48)
- Wiki 3e: "| alignment35    = [[Neutral good]]" — wiki line 53 (key CoSW-p54, line 56)
- Wiki 5e: "| alignment5e    = " — wiki line 60 (blank)
- Adventure: no alignment for Caladorn (`sources/adventure-wdh.json:22712`-`:22729` gives none).
- Conflict: D4.

**Species**
- "Tethyrian human ghost" — page line 5; organization line 106; governance line 50.
- Wiki: "| race           = [[Human]]" (wiki line 15); "| ethnicity      = [[Tethyrian]]" (wiki line 16).
- Adventure: "a {@creature ghost}" (`sources/adventure-wdh.json:22712`).

**Pronouns**
- "he/him" — page line 5; governance line 50.
- Wiki: "| sex            = Male" (wiki line 14).
- Adventure: no pronoun for Caladorn. The ghost is "its" in the adventure: "After it is shown such a symbol, the ghost guides characters to its personal crypt" (`sources/adventure-wdh.json:22713`).
- Campaign narration: "He looks at the symbol for a long moment." (`campaign/locations/cassalanter-villa/15-family-crypt.md:23`).

**Stat block**
- Page: "Stat block: **Ghost**." — `campaign/setting/notable-figures/cassalanters/14-caladorn-cassalanter.md:5`
- Crypt file: "Multiattack, Withering Touch, CR 4 ghost statistics." — `campaign/locations/cassalanter-villa/15-family-crypt.md:21`
- Structure: "If the approaching creature bears fiendish taint (participated in Asmodean worship, bears an infernal mark), Caladorn attacks — Multiattack, Withering Touch, CR 4." — `campaign/structure/arc-g-cassalanter-villa.md:231`
- Adventure: "a {@creature ghost}" (`sources/adventure-wdh.json:22712`); no ghost stat-block text was found in the adventure lines read.

**Wiki infobox (5e, no alignment, no stat block)**
- "| death          = " (blank, wiki line 25) and "| deathnotes     = " (blank, wiki line 26). Death date: none.

## C. Sentences on the current page that narrate quest-time or depend on a discovery

Page: `campaign/setting/notable-figures/cassalanters/14-caladorn-cassalanter.md`. The page has no Background, Personality or Connections section yet.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L5 | "*Tethyrian human ghost of a Cassalanter noble, lawful good, he/him*. Stat block: **Ghost**." | Day-one. "lawful good" conflicts with the wiki (D4) | Section B |
| 2 | L6 | "- **Affiliation:** The Cassalanters (deceased; ancestral ghost)" | Day-one | `organizations/10-cassalanters.md:106` |
| 3 | L7 | "- **Featured in:** Cassalanter Villa, Cassalanter Villa (location)" | Quest references only. No quest journal names Caladorn | `campaign/structure/arc-g-cassalanter-villa.md:489` (Caladorn's Ghost heading) |
| 4 | L11 | "**Resonance.** Caladorn should inspire immediate pity when the party understands what he has been watching from A4a for three years, admiration when his dignity holds despite everything his family has become, and a specific grief when his voice breaks speaking their names." | "when the party understands" is discovery time. "watching ... for three years" (F2). "when his voice breaks speaking their names" is the lucid-state voice of quest-time (see row 8) | `arc-g-cassalanter-villa.md:135`; `15-family-crypt.md:23`; `arc-g-cassalanter-villa.md:137` |
| 5 | L13 | "**Emotions.** Caladorn most often feels steadfast conviction in a duty that has outlasted death, grief that has had three years to deepen undisturbed, controlled anguish when his family is mentioned or visible evidence of their corruption surrounds him, and a warmth — readable as relief rather than welcome — when the Siamorphe holy symbol is presented." | "three years" (F2). "when the Siamorphe holy symbol is presented" is encounter time (`arc-g-cassalanter-villa.md:137`) | as listed |
| 6 | L15 | "**Motivations.** Caladorn wants to see the infernal corruption of his house ended, the effigy in A7 destroyed, and some portion of the honor his family carried for generations restored to the name he left behind. He does not want revenge on Victoro and Ammalia. He wants the bargain broken." | Day-one. Keep verbatim (ruling 3). No quest-time clause | A10 |
| 7 | L17 | "**Inspirations.** When playing Caladorn, channel King Hamlet (*Hamlet*), Ned Stark (*Game of Thrones*), and Jacob Marley (*A Christmas Carol*)." | Not a fact | n/a |
| 8 | L21 | "**Persona.** To the world — specifically to anyone who enters A4a bearing a Siamorphe holy symbol — Caladorn is an armored figure with silver hair and the Cassalanter features, carrying the family sword, voice steady until it is not. His portrait hangs prominently in the entrance hall upstairs, silver-haired and armored; the family uses his image as civic virtue while remaining unable to reach him. To those who present the symbol and wait, he is lucid, measured, and specific about what he is asking and what he is giving in return. Deep down, they turned his wife's goddess into that thing, and he has been twelve feet away from it for three years." | Split. The portrait sentence is day-one (A9) but says "upstairs" (D6). "To anyone who enters A4a bearing ..." and "To those who present the symbol and wait ..." are encounter time (`15-family-crypt.md:23`). "voice steady until it is not" is encounter time (`arc-g:137`). "twelve feet away" (F3). "for three years" (F2). "his wife's goddess" is day-one (A8) | `01-entrance-hall.md:3`; `15-family-crypt.md:23`; `arc-g:137`; `siamorphe.md:61` |
| 9 | L23 | "**Morale.** Caladorn attacks any creature bearing fiendish taint on sight — a restriction that has forced the Cassalanters to retreat from A4a twice. Against creatures who present the Siamorphe holy symbol, he manifests peacefully and provides the +1 plate armor and mace of disruption from his sarcophagus. He does not waver when told the full terms of the pact." | Encounter behaviour. "attacks ... on sight" is trigger text (D1). "retreat ... twice" is day-one history (`arc-g:151`). "provides ... mace" is the lucid state (`arc-g:139`). "He does not waver when told the full terms" is a discovery trigger; he does not know the full terms (`arc-g:141`) | `arc-g:139`, `:141`, `:151`; `15-family-crypt.md:21`, `:25`-`:27`, `:31` |
| 10 | L25 | "**Relationships.** Caladorn is the ghost of Victoro Cassalanter's father, a former Masked Lord and hero of the North who devoted his life to Siamorphe, the former owner of two items critical to the contract-destruction path (the +1 plate armor and the mace of disruption), and the reason the solution to the Cassalanter pact has been beneath the villa the entire time — accessible only to people not corrupted by it." | The father, office and devotion clauses are day-one. "critical to the contract-destruction path" and "the reason the solution ... has been beneath the villa" are quest-time routing (`arc-g:489`-`:493`; Organization line 202 routes it). Keep only the day-one part | `campaign/setting/organizations/10-cassalanters.md:202` (routed) |
| 11 | L29 | "Caladorn Cassalanter's portrait hangs prominently in the villa's entrance hall — silver-haired and armored, a former Masked Lord and hero of the North whose image the family still invokes as civic virtue." | Day-one public face. **31 words** by count (brief limit 21). Sentence has an em-dash | A9; A8 |

**Voice profile (`.claude/skills/character-voices/voices/cassalanters.md`, "### Caladorn Cassalanter" at lines 243 to 257)**

The file's secrecy header says the "after discovery" register is "used only once the party has found the truth (villain Phase 2 onward, or when the character is confronted in the temple)" (`.claude/skills/character-voices/voices/cassalanters.md:3`). The Caladorn profile has no "after discovery" register; its lines are:

> "- **Sound:** A deep, measured, noble voice, hollow with death. It breaks when he names his family." — line 246 (day-one)
> "- **Word choice:** Chivalric and grave: honour, duty, \"my house\", \"the bargain\". Siamorphe is \"my wife's goddess\". He never says the names Victoro and Ammalia without a pause." — line 248 (day-one for the wife; "the bargain" is a discovery term; the pause is encounter)
> "- **Swearing:** *Never · Plain · n/a.* His grief is heavier than any curse." — line 249 (day-one)
> "- **Personality in speech:** Steadfast conviction and deep grief. He wants the bargain broken, not revenge, and says so. Relief at the Siamorphe symbol shows as warmth." — line 250 (the Siamorphe symbol is encounter)
> "- **Quirks:** He rests a hand on the family sword as he speaks. He falls silent mid-sentence facing the effigy's direction." — line 251 (day-one habit with the sword; the effigy direction is encounter)
> "- **Signature phrases:** \"Break the bargain.\" / \"My house has fallen far.\" / \"I do not ask for vengeance.\"" — line 252 (the bargain is a discovery term)
> "- **Never:** He never asks for revenge, never lies, and never leaves A4a." — line 253 (day-one; "never leaves A4a" follows from `arc-g:135`)
> "*Greeting:* \"You carry her symbol. Then I may speak. Hear me, for I have waited three years for someone to.\"" — line 255 (encounter; "three years" is F2)
> "*Business:* \"Destroy the effigy below. Break the bargain. I do not ask for vengeance on Victoro and — on Ammalia. Only that it ends.\"" — line 256 (encounter; the vow)
> "*Under pressure:* \"Go, now. This house devours what it touches.\"" — line 257 (encounter)

Quest-time or conditional clauses for the rule-16 restatement: line 246 "It breaks when he names his family" (the lucid-state voice, `arc-g:137`), line 250 "Relief at the Siamorphe symbol", line 251 "falls silent mid-sentence facing the effigy's direction", line 252 "Break the bargain" (a discovery term), line 255 "waited three years", line 256 the vow, line 257 the pressure line.

**Routing for the quest-time text (Cassalanter Villa; no quest journal exists)**
- `campaign/structure/arc-g-cassalanter-villa.md:137`: "If a character presents a Siamorphe holy symbol (from the Order's chaplain at the end of Order of the Gauntlet Mission 5, or from Savra at Order of the Gauntlet r10), the specters in A4 stand down. Caladorn's ghost manifests in A4a — an armored figure with the Cassalanter features, silver-haired, carrying the family sword. He is lucid — steady voice, measured words, until he mentions his family. Then the voice cracks."
- `campaign/structure/arc-g-cassalanter-villa.md:139`: "Caladorn provides: a +1 plate armor (his own, stored in his sarcophagus) and a mace of disruption (consecrated to Siamorphe, the weapon he carried as a Masked Lord). He asks for a vow: \"Use the mace to destroy the effigy of evil incarnate. End the corruption of my house. Restore my family's honor.\" The mace is the key to destroying the Asmodeus statue in A7."
- `campaign/structure/arc-g-cassalanter-villa.md:141`: "Caladorn does not know the contract's specific terms. He knows his family has turned to Asmodeus. He knows the statue in A7 was his wife's image of Siamorphe before they defaced it. He does not know about the children's souls or the Founders' Day plan. If told, his anguish deepens — but he does not waver. The mace is the answer. The statue must fall."
- `campaign/structure/arc-g-cassalanter-villa.md:149` (Path 2): the paragraph begins "**Path 2 — Destroy the Infernal Contract (Mace of Disruption).** The Cassalanters want this — they have searched for years and found nothing." and names Caladorn's ghost in A4a with the mace.
- `campaign/structure/arc-g-cassalanter-villa.md:231`: quoted in B.
- `campaign/structure/arc-g-cassalanter-villa.md:489` ("## Caladorn's Ghost and the Mace of Disruption") and `:493`: "Only outsiders — the PCs, bearing a Siamorphe holy symbol from the Order of the Gauntlet — can speak to Caladorn and receive the mace."
- `campaign/locations/cassalanter-villa/15-family-crypt.md:23`: "**Lucid state trigger:** If the approaching creature presents a Siamorphe holy symbol, Caladorn holds. ... \"My son could not send an outside. He sent people he doesn't know. That tells me something.\""
- `campaign/locations/cassalanter-villa/15-family-crypt.md:31`: "If told — his expression does not change. His voice does: \"Elzerina and Terenzio.\" He says the names once. Then: \"The mace. End it.\""
- `campaign/structure/arc-g-cassalanter-villa.md:168`: "We can never speak to Caladorn's spirit — he attacks us on sight." (the Cassalanters' own dialogue in the Stage 4 confrontation)
- `campaign/structure/arc-g-cassalanter-villa.md:370`: "*Savra (Order of the Gauntlet).* Exultant. Caladorn Cassalanter was a hero of the North — his ghost's holy weapon destroyed an infernal altar."
- `campaign/setting/organizations/10-cassalanters.md:202` (Draft Notes, routed-facts note for the contract path).
- `campaign/setting/villains/cassalanters.md:36`: E1.

## D. Conflicts

**D1. The ghost's trigger**
- Crypt file: "If the approaching creature has participated in Asmodean worship, carries an infernal mark, or is a cult member, Caladorn attacks immediately — Multiattack, Withering Touch, CR 4 ghost statistics." — `campaign/locations/cassalanter-villa/15-family-crypt.md:21`
- Structure: "If the approaching creature bears fiendish taint (participated in Asmodean worship, bears an infernal mark), Caladorn attacks" — `campaign/structure/arc-g-cassalanter-villa.md:231`
- Victoro page: "His ghost waits in the family crypt below the villa, where it attacks anything with a fiendish taint and helps anyone who shows a holy symbol of Siamorphe." — `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:17`
- Adventure: "These undead attack any living creatures but can't leave the crypt or approach within 5 feet of any creature that wears a holy symbol of Asmodeus." — `sources/adventure-wdh.json:22712`
- Higher-ranked: the campaign (crypt file, structure, Victoro page, page). The campaign's "fiendish taint" applies to the ghost; the adventure's undead are the ones kept at five feet from the Asmodeus symbol, and the adventure gives no taint rule for the ghost. Both sides agree the Siamorphe symbol halts the ghost (`sources/adventure-wdh.json:22713`). The campaign's "cult member" trigger is not in the adventure.

**D2. The vow wording**
- Adventure: "Before vanishing for good, it says, \"Use the mace to destroy the effigy of evil incarnate. End the corruption to restore my family's honor.\"" — `sources/adventure-wdh.json:22729`
- Structure: "Use the mace to destroy the effigy of evil incarnate. End the corruption of my house. Restore my family's honor." — `campaign/structure/arc-g-cassalanter-villa.md:139`
- Crypt file: "Use the mace to destroy the effigy of evil in the ceremonial hall. End the corruption of my house. Restore my family's honor." — `campaign/locations/cassalanter-villa/15-family-crypt.md:29`
- Adventure also has the ghost ask first: "If Caladorn's ghost is present when one or both magic items are removed from the sarcophagus, it asks, \"Do you vow to use these items to defeat the forces of darkness?\"" — `sources/adventure-wdh.json:22729`
- Higher-ranked: the two campaign files differ from each other ("in the ceremonial hall" versus "incarnate"). Both outrank the adventure. The orchestrator picks the wording; the page should not quote a vow on day one (routed).

**D3. Office: Masked Lord or Open Lord**
- Wiki: "By the {{YearlinkName|1399}}, Caladorn had been named [[Open Lord]] of Waterdeep." — wiki line 90 (key BST-p198, "Blackstaff Tower")
- Organization, History: "Ohrl's son Caladorn set the family name aside until he had done something worthy of it ... He served as a Masked Lord, earned the title of hero of the North and fathered Victoro (*Dragon Heist*, 5e). ... Campaign change: the wiki also makes him an Open Lord, and the campaign keeps him a Masked Lord only" — `campaign/setting/organizations/10-cassalanters.md:22`
- Organization, GM Notes: "The wiki has him a Masked Lord and later Open Lord of Waterdeep, by 1399 DR (*Blackstaff Tower*, 2e and 3e)." — `campaign/setting/organizations/10-cassalanters.md:123`
- Governance: "Conflicts, Caladorn: `wiki.txt` line 747 lists him as an Open Lord. `adventure-wdh.json` lines 18404 and 22713 call him a former Masked Lord, and this page follows the adventure." — `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:105`
- History: "The wiki also lists him as the fifth Open Lord, which the published adventure and the campaign do not" — `campaign/setting/history/05-a-debt-in-blood.md:32`
- History: "- The wiki lists seven Open Lords to 1489 DR: Ahghairon, Baeron Silmaeril, Lhestyn, Piergeiron the Paladinson, Caladorn Cassalanter, Dagult Neverember and Laeral Silverhand (...). `[research: wiki only]`" — `campaign/setting/history/07-a-city-watching-itself.md:36`
- Higher-ranked: the adventure and the campaign (Masked Lord only). The wiki's Open Lord claim is wiki-only.

**D4. Alignment**
- Page: "lawful good" — `campaign/setting/notable-figures/cassalanters/14-caladorn-cassalanter.md:5`
- Wiki 2e: "| alignment2e    = [[Neutral good]]" — wiki line 46
- Wiki 3e: "| alignment35    = [[Neutral good]]" — wiki line 53
- Higher-ranked: the campaign says lawful good in three files (page, organization line 106, governance line 50). No source gives lawful good. The campaign's value stands; the wiki's neutral good is the only other source and is wiki-tier.

**D5. Hair**
- Wiki (life): "He had short dark red or brown hair and was clean-shaven" — wiki line 68.
- Campaign (portrait and ghost): "silver-haired and armored" — `campaign/locations/cassalanter-villa/01-entrance-hall.md:3`; page line 21 "an armored figure with silver hair".
- Higher-ranked: the campaign for the ghost's and the portrait's look. Living hair colour is wiki-only and is not contradicted by the portrait (age and the portrait's conventions are not sourced).

**D6. Portrait location**
- Page: "His portrait hangs prominently in the entrance hall upstairs, silver-haired and armored" — `campaign/setting/notable-figures/cassalanters/14-caladorn-cassalanter.md:21`
- Entrance hall: "A two-story foyer with marble floors and a grand staircase curving to the second floor. The walls are hung with Cassalanter ancestor portraits — Caladorn Cassalanter is prominently placed near the stair, silver-haired and armored in the heraldic style of the North." — `campaign/locations/cassalanter-villa/01-entrance-hall.md:3`
- Higher-ranked: the location file. "Upstairs" is not in it. Drop "upstairs" or say "near the stair".

**D7. Ghost's knowledge**
- Crypt file: "He knows his family has turned to Asmodeus; he knows the statue in A7 was his wife's image of Siamorphe before they defaced it." — `campaign/locations/cassalanter-villa/15-family-crypt.md:31`
- Siamorphe page: "he knows the statue was his wife's image of the goddess before the family defaced it" — `campaign/setting/deities/siamorphe.md:61`
- These agree. The page's Persona ("Deep down, they turned his wife's goddess into that thing") agrees with them.

**D8. Victoro's mother**
- Victoro page: "Caladorn was human and Victoro is a half-elf, so his mother was an elf `[research]`. No file gives her name." — `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:17`
- Not a conflict with Caladorn's wife. The wife is unnamed; whether she is Victoro's mother is not stated (F1).

## E. Stale lines in other files (not to be edited) and routed quest references

- E1. `campaign/setting/villains/cassalanters.md:36` (a setting page; the campaign-start rule applies): "In the contract path the mace of disruption from Caladorn's ghost strikes the Asmodeus statue in A7 and severs the contract, which frees the children and brings Asmodean retribution within days."
- E2. `campaign/setting/deities/siamorphe.md:62`: "The mace: Caladorn carried a mace of disruption as a Masked Lord, and it was consecrated in Siamorphe's name. He tells the party that she is still in it." — "He tells the party" is quest-time on a setting page.
- E3. `campaign/setting/deities/siamorphe.md:63`: "The holy symbol: A Siamorphe holy symbol, worn or presented, halts the specters and calms the ghost. Caladorn then becomes lucid and hands over his +1 plate armor and the mace. A party without one must fight the specters, which cannot follow into his chamber." — quest-time on a setting page.
- E4. `campaign/setting/deities/siamorphe.md:70`: "A party that has met Caladorn and heard him ask to \"restore my family's honor\" reads this as deliberate desecration of the whole temple." — quest-time on a setting page.
- E5. `campaign/setting/organizations/10-cassalanters.md:202` (Draft Notes) routes the clause "and is the reason the way to break the contract lies beneath it" out of the body, correctly. The current body at line 123 has no such clause. The older Organization text still carries it in `sources/research/pass4-bundles/cassalanters/campaign-hits.txt:865`, so that bundle copy is stale.
- E6. `campaign/guides/gm-guide/grand-game-in-play.md:84`: "In the contract path, the mace of disruption, recovered from Caladorn Cassalanter's ghost in the villa's family crypt, strikes the Asmodeus statue in A7, severs the infernal contract..." — GM guide, quest-time text; routed to Cassalanter Villa.
- E7. `campaign/locations/cassalanter-villa/14-anterior-vestibule.md:23`: "Any party member who has been told about or found Caladorn's ghost (A4a) and his demand to \"restore my family's honor\" receives the context immediately" — location file; quest-time.
- E8. `campaign/setting/history/05-a-debt-in-blood.md:32`: "His ghost haunts the family crypt beneath the villa." — day-one; fine. Its "fifth Open Lord" clause is D3.
- E9. Edition tags for the same Lords listing differ across campaign files. `campaign/setting/history/07-a-city-watching-itself.md:36` gives "5e" for the boxed set Campaign Guide and SCAG; `campaign/setting/history/07-a-city-watching-itself.md:131` gives "City of Splendors: Waterdeep, 3e"; `campaign/setting/organizations/10-cassalanters.md:123` gives "2e and 3e" for Blackstaff Tower; `campaign/setting/organizations/10-cassalanters.md:22` gives "1e and 3e" for the Caladorn entry.
- E10. `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:21` ([design]) makes claims about Caladorn's past: "Caladorn spent long seasons in the North", "his father repaid a failed loan out of the house's plate and two of its warehouses", "Caladorn was proud of it". See G3.

## F. Gaps a Background would need that no source gives

- **F1. Wife.** Unnamed in every file. "his wife's goddess" (`14-caladorn-cassalanter.md:21`); "his wife's image of Siamorphe" (`arc-g-cassalanter-villa.md:141`). Whether she is Victoro's mother is not stated (`campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:146`: "Caladorn's wife (`deities/siamorphe.md:61` and the voice profile for Caladorn) is unnamed, and no file says whether she is Victoro's mother. The page does not say."). Whether she is buried in the crypt: no source. Her death, if any: no source.
- **F2. Death date and "three years."** No death date in any source (wiki line 92; adventure "the late", `sources/adventure-wdh.json:18404`). The "three years" comes from `arc-g-cassalanter-villa.md:135` and `:491` only. No file ties Caladorn's ghost to 1489 DR. Mark the death date `[research]` if the drafter gives one.
- **F3. "Twelve feet away."** Only the page (line 21) has it. The crypt file gives no distance: "the wall behind him is not quite hidden" (`15-family-crypt.md:19`).
- **F4. Early life.** Birthplace, birth year and childhood are not sourced. Wiki line 78 covers only the name and the father's view. Sylull's name is wiki-only (wiki line 95).
- **F5. Cause of death and when he entered the crypt.** Not sourced.
- **F6. Lucia Thione.** The wiki names her as the poisoner (wiki line 87). She is not a Notable Figure. She is named only by a wiki source, which ranks last. Flag before use.
- **F7. Fields of Triumph.** The cover ("a simple fighting instructor at the Fields of Triumph", wiki line 74) is in no campaign file. A grep of `campaign/` for "Fields of Triumph" found no match.
- **F8. Masked Lord service dates.** No source gives when he was a Masked Lord or who recruited him. The wiki says "secret" (wiki line 65).
- **F9. Caladorn's knowledge of the pact.** Partly sourced: `arc-g-cassalanter-villa.md:141` gives what he knows (the family turned to Asmodeus; the statue). Whether he knows the pact's terms is not day-one; the sources say he does not (`15-family-crypt.md:31`).
- **F10. Grandchildren.** Victoro is the only named child (wiki line 35; adventure 18404). The twins are grandchildren, but Caladorn is not named as their grandfather in any file (`campaign/setting/notable-figures/cassalanters/06-elzerina-cassalanter.md:134`: "The Background does not name Caladorn as the twins' grandfather. No file gives a child-specific fact about him, and the grandfather link is an inference `[research]`.").
- **F11. Personal goals.** The Motivations line (A10) is the only goal source. Others must be drafted under ruling 17 and tagged `[design]`, and must not contradict Victoro's `[design]` claims (E10).
- **F12. Ghost's mobility.** The page says "never leaves A4a" (voice line 253). Sources agree the ghost cannot leave A4a (`arc-g-cassalanter-villa.md:135`: "unable to leave A4a").

## G. Source facts that hint at the figure's inner life (exact quotes)

- G1. "He does not want revenge on Victoro and Ammalia. He wants the bargain broken." — `campaign/setting/notable-figures/cassalanters/14-caladorn-cassalanter.md:15`
- G2. "grief that has had three years to deepen undisturbed" — `campaign/setting/notable-figures/cassalanters/14-caladorn-cassalanter.md:13` (the "three years" is F2)
- G3. Victoro's page [design] lines about Caladorn: "Caladorn spent long seasons in the North, and the boy was left with the counting house and its ledgers `[design]`. While Victoro was still young, his father repaid a failed loan out of the house's plate and two of its warehouses, so that no creditor could say that a Masked Lord had defaulted `[design]`. Caladorn was proud of it, and Victoro carried the ledgers that showed what it had cost `[design]`. He came away believing that his father's honor was real and that the house had barely been able to afford it `[design]`." — `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:21`. Constraint: the Caladorn Background may build on these or leave them alone; it must not contradict "long seasons in the North" or the loan.
- G4. "Caladorn ceased using his family's name until he had done \"something worthy of it.\"" — wiki line 78; also `campaign/setting/organizations/10-cassalanters.md:22`
- G5. "he loved to have fun in private, when the occasion called for it." — wiki line 71
- G6. "Heartbroken, Caladorn quit the Lords and his city for two years, traveling the [[Sword Coast]]." — wiki line 87
- G7. "was very interested in the city's navy" — wiki line 74
- G8. "Caladorn was courting [[Lucia Thione-Hhune|Lucia Thione]] and planning to marry her." — wiki line 87
- G9. "his wife's goddess" and "he has been twelve feet away from it for three years" — `14-caladorn-cassalanter.md:21`
- G10. "He never asks for revenge, never lies, and never leaves A4a." — `.claude/skills/character-voices/voices/cassalanters.md:253`
- G11. "Siamorphe is \"my wife's goddess\"." — `.claude/skills/character-voices/voices/cassalanters.md:248`
- G12. "I do not ask for vengeance." — `.claude/skills/character-voices/voices/cassalanters.md:252`
- G13. "He knows the statue in A7 was his wife's image of Siamorphe before they defaced it." — `campaign/structure/arc-g-cassalanter-villa.md:141`
- G14. "Caladorn's bones have turned to dust, but his suit of {@item +1 plate armor} remains." — `sources/adventure-wdh.json:22729`
- G15. "Caladorn's ghost has been raging in silence for three years, unable to leave A4a, unable to stop what his family has done to his legacy." — `campaign/structure/arc-g-cassalanter-villa.md:135`
</content>
