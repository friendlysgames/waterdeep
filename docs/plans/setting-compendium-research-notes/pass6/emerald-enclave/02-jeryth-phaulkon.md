# Pass 6 research notes: Jeryth Phaulkon

Page: `campaign/setting/notable-figures/emerald-enclave/02-jeryth-phaulkon.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Jeryth is the Enclave's highest authority in Waterdeep (`campaign/setting/organizations/03-emerald-enclave.md:52`), so the full Personality and Connections apply.
Organization page: `campaign/setting/organizations/03-emerald-enclave.md` ("# The Emerald Enclave"; "Campaign role: Player faction.", line 7)
Factions Guide: `campaign/guides/factions/04-emerald-enclave.md`
Voice profile: `.claude/skills/character-voices/voices/emerald-enclave.md` (`### Jeryth Phaulkon`, lines 23-37)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`
Companion notes: `docs/plans/setting-compendium-research-notes/pass6/emerald-enclave/01-melannor-fellbranch.md`

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output; line numbers are file lines. Where the Grep tool omitted a long line, it was read with Read at its offset.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. `{@creature ...}` tags are left as written.
- Alexandrian PDF: `sources/3. Player Character Factions.pdf`, rendered page 2 (printed page 24). The Enclave sentence there is a transcription from the image and must be checked with `pdftotext -layout` before prose. Jeryth is not named on that page.
- Alexandrian Appendices B, C and D are markdown and were read directly.
- Wiki: the scratchpad extract `wiki-emerald-enclave/02-jeryth-phaulkon.txt`, quoted as "wiki line N". Most wiki sentences carry no edition. The citations name *City of Splendors* (boxed set; the wiki's own *Mielikki* page tags it 2e, `sources/research/pass2-bundles/mielikki/wiki.txt:278`), *Forgotten Realms Campaign Setting* (3e, `FRCS3e-p42`), *The North: Guide to the Savage Frontier* (edition not printed) and *Waterdeep: Dragon Heist* (5e). Editions are tagged where cited.
- Wiki and Appendix quotes that run on are closed after the last sentence used, with a "(rest of the passage covers: ...)" note. The file and line of the full passage are given.
- No shell and no edit tool were available, so this file was written whole. `voicecheck.py` was not run. No other file was edited.

## Findings that change how the page is written

1. **Species is open.** The campaign page gives no species (`02-jeryth-phaulkon.md:5` reads "Disembodied presence"). The adventure says "a noblewoman-turned-demigod and Chosen of Mielikki" (`sources/adventure-wdh.json:3717`), Appendix B says "a noblewoman who has become a demigod" (`sources/Appendix_B_-_Player_Factions.md:297`), and the wiki says "[[Human]], [[Demigod]]" (wiki line 14). The Enclave Draft Notes say the campaign "drops demigod" (`03-emerald-enclave.md:158`). The orchestrator must decide the species line. Conflict D1.
2. **The calling has three dates in the sources.** The wiki's *Mielikki* page says 1367 DR (`wiki.txt:278`). Appendix B says "several years ago" (`sources/Appendix_B_-_Player_Factions.md:341`). The campaign says "for several years" for the garden residence (`02-jeryth-phaulkon.md:9`). Conflict D2.
3. **"Old, patient and hungry" appears in two campaign files with different timing.** The Factions Guide puts it before the campaign (`campaign/guides/factions/04-emerald-enclave.md:9`). This page makes it a **The Water Table Stirs** line only (`02-jeryth-phaulkon.md:34`). Conflict D5.
4. **The page's Motivations and Relationships use quest-time words.** "watch the party's handling of the Stone of Golorr with particular attention" (`:19`) and "Her relationship with the party runs through Melannor" (`:29`). The GM callout's gates are at `:34` and `:35`.
5. **The voice profile's Sentence shape line carries a production note.** It ends "This is a deliberate break from `ember-voice` speech." (`.claude/skills/character-voices/voices/emerald-enclave.md:27`). It is not a speech rule and must not reach the page's `### Voice` block.

---

## A. Background facts by theme

### A1. Origin

**Adventure, the Phaulkons' origin (page 15)**
> "The place is owned by descendants of two wealthy families-the Tarms (longtime Waterdavians) and the Phaulkons (who are of Cormyrean descent)."
> — `sources/adventure-wdh.json:1320`

**Wiki, lead sentence (infobox refs `WDH5e-p4`, `TN.TW-52`, `FRCS3e-p42`)**
> "[[Jeryth Phaulkon]] ({{Pronounce|JAIR|ith|_|FAWL|kon|refs=<ref name="WDH5e-p4">{{Cite book/Waterdeep: Dragon Heist|4}}</ref>}}) was a [[human]] [[noble|noblewoman]] of the [[Cormyr]]-native [[Phaulkon]] family, who served as a powerful [[ranger]] of the [[High Forest]],<ref name="TN.TW-52">{{Cite book/The North: Guide to the Savage Frontier/The Wilderness|52}}</ref> as well as a [[divine champion]] and [[Chosen]] of [[Mielikki]].<ref name="FRCS3e-p42">{{Cite book/Forgotten Realms Campaign Setting 3rd edition|42}}</ref>"
> — wiki line 62 (`TN.TW` edition not printed; `FRCS3e-p42` is 3e)

**Wiki, infobox home and former homes**
> "| home           = [[Phaulkonmere]], [[Waterdeep]]" — wiki line 11
> "| formerhomes    = [[High Forest]], [[Cormyr]]" — wiki line 12

**Campaign, the Cormyr origin (day one, deity page)**
> "- **Chosen:** She gives each Chosen an undying unicorn as a mount and companion. Some Chosen transcend their bodies and become disembodied manifestations of natural places, and FRHoF names Jeryth Phaulkon as one, a woman from Cormyr who now inhabits a garden estate in Waterdeep."
> — `campaign/setting/deities/mielikki.md:39`
> Source line in the 5etools Heroes of Faerûn file: "Mielikki gifts her Chosen with an undying unicorn that serves them as a mount and companion. Some Chosen transcend their physical forms to become disembodied manifestations of natural spaces—such as Jeryth Phaulkon, a woman from {@book Cormyr|FRHoF|2|Cormyr} who now inhabits an expansive garden estate in {@book Waterdeep|FRHoF|2|Waterdeep} as a disembodied spirit."
> — `sources/5etools/deities.json:9279` (Heroes of Faerûn, as carried in the file)

**Campaign, the estate's owners (day one)**
> "- **Phaulkonmere:** The Tarm and Phaulkon families own the estate and spend most of the year abroad, and only Jeryth lives there now. *Dragon Heist* (5e) calls the Phaulkons of Cormyrean descent and the Tarms longtime Waterdhavians."
> — `campaign/setting/organizations/03-emerald-enclave.md:101`

### A2. Family (wiki only; the campaign and the adventure name none of these people)

**Wiki, parents and siblings**
> "|parents         = [[Bronson Phaulkon]] (father), [[Cera Phaulkon]] (mother), [[Silvanus]] (grandfather), [[Mielikki]] (possible mother)" — wiki line 29
> "| siblings       = [[Marie Phaulkon]] (older sister)" — wiki line 31
> "| familyrefs     = <ref group="note">The description of Silvanus as Jeryth's grandfather, along with the comparison made between Jeryth and [[Alustriel]] by [[Tathshandra Tyrar]] suggests that Mielikki may have birthed Jeryth in a process similar to that used by [[Mystra]] when giving birth to the [[Seven Sisters]].</ref>" — wiki line 33 (the wiki's own speculation)

**Wiki, Bronson (CoS, 2e)**
> "* [[Bronson Phaulkon]]: The lord of the Phaulkon family and Jeryth's father was an up-and-coming merchant and caravan organizer who owned properties within Waterdeep's [[Southern Ward of Waterdeep|Southern Ward]], where he built his villa.<ref name="CoS.AGttC-45-46">{{Cite book/City of Splendors (boxed set)/Adventurer's Guide to the City|45-46}}</ref>"
> — wiki line 78 (2e)

**Wiki, Cera (CoS, 2e)**
> "* [[Cera Phaulkon]]: The deceased lady of the Phaulkon family and Jeryth's mother was killed during a raid on one of the Phaulkon caravans in [[1367 DR]].<ref name="CoS.SotC-9">{{Cite book/City of Splendors (boxed set)/Secrets of the City|9}}</ref>"
> — wiki line 79 (2e)

**Wiki, Marie (CoS, 2e)**
> "* [[Marie Phaulkon]]: Jeryth's wild and rebellious older sister.<ref name="CoS.AGttC-59">{{Cite book/City of Splendors (boxed set)/Adventurer's Guide to the City|59}}</ref><ref name="CoS.SotC-14">{{Cite book/City of Splendors (boxed set)/Secrets of the City|14}}</ref>"
> — wiki line 80 (2e)

**Wiki, the betrothal (no citation)**
> "* [[Arum Tarm]]: Prior to her disappearance, Jeryth was betrothed to a son of the Tarm noble family of Waterdeep."
> — wiki line 82

**Negative check.** A Grep over `campaign/` for "Arum", "Bronson", "Cera Phaulkon" and "Marie Phaulkon" returned no match. The adventure (`sources/adventure-wdh.json`) names none of the four.

### A3. Looks and manner before and after the calling (wiki, 2e)

> "Jeryth had green eyes and long blond hair that she wore in elaborate coiffures. Being known as someone at the height of fashion, prior to her disappearance, she favored wearing green and golden outfits to match her physical features. Jeryth was however also known to use cosmetics to an excessive degree." — wiki line 67 (CoS.AGttC-54)
> "Prior to her disappearance, Jeryth was known as a rather typical [[Waterdhavian]] noblewoman; arrogant, and utterly frivolous in her interests. Despite this, she was beloved and respected for her forthrightness and honesty." — wiki line 69 (CoS.AGttC-54)
> "Jeryth had a habit of playing with her hair, twisting it around her fingers." — wiki line 71 (CoS.AGttC-54)
> "After her disappearance and rise as a Chosen, Jeryth's blond hair received the addition of a streak of ivory to it, resembling the horn of a [[unicorn]]. Along with her physical change, Jeryth's personality additionally altered itself to far more represent the ways of her goddess, becoming carefree like a bird." — wiki line 73 (CoS.SotC-9)
> "Jeryth has however also grown strict in the face of those who would misuse nature, following the most conservative credos of rangers." — wiki line 75 (CoS.SotC-9)
> Campaign: no physical description. Adventure: "manifests as a disembodied female voice" (`sources/adventure-wdh.json:3717`) only.

### A4. The calling, the 1367 DR events and the High Forest years (wiki only)

**Wiki, 1367 DR, "believed missing or killed" (CoS, 2e)**
> "By [[1367 DR]], Jeryth was believed missing or killed near [[Luskan]] as a result of the same caravan raid that took the life of her mother.<ref name="CoS.CG-33">{{Cite book/City of Splendors (boxed set)/Campaign Guide|33}}</ref> This massacre was performed by the [[Hoar Fang]] tribe of [[gnolls]] due to the schemes of a [[doppelganger]] member of the [[Unseen]] seeking to gain information about the noble family.<ref name="CoS.WWiW-87">{{Cite book/City of Splendors (boxed set)/Who's Who in Waterdeep|87}}</ref>"
> — wiki line 89

**Wiki, the calling and the captivity (wiki's *Mielikki* page, 2e)**
> "In the {{YearlinkName|1367}}, Mielikki appeared in a dream to Jeryth Phaulkon, a noble of Waterdeep, and offered to make her her chosen. Her reasons were more practical than mystical: initially, she wanted her new champion to stop the [[Hoar Fang]] [[gnoll]]s from laying waste to the [[Lurkwood]], and Jeryth happened to be their captive at the time. Imbued with the goddess's powers, Jeryth freed herself and her companions, met the Harper [[Bran Skorlsun]], and defeated the gnolls. Similarly, Mielikki appeared in a dream to [[Briosar Helmsing]], one of her priests, and gave him a quest to meet up with Jeryth.<ref name="CoS-SotC-p9" />"
> — `sources/research/pass2-bundles/mielikki/wiki.txt:278`

**Wiki, the High Forest years (*The North*, edition not printed)**
> "The truth was however that as of [[1370 DR]], Jeryth lived within and roamed the High Forest as a ranger, tasked with the mission of serving as Mielikki's foremost defender of the woods. Jeryth's interference in troubles of the forest was however rarely necessary as the native [[elves]] often were capable enough to handle such matters on their own.<ref>{{Cite book/The North: Guide to the Savage Frontier/The Wilderness|58}}</ref>"
> — wiki line 91

**Wiki, Everlund and Tyrar (*The North*, edition not printed)**
> "Around the same time, Jeryth was known to have spent time in [[Everlund]] in the company of her fellow faithful of Mielikki, [[Tathshandra Tyrar]] of [[Silverymoon]]. The encounter with the Chosen of Mielikki left Tyrar feeling lighthearted, bolstered in her faith, and as though young again. Tyrar felt that Lady Phaulkon's relationship with Mielikki was comparable to Lady [[Alustriel Silverhand|Alustriel]] of Silverymoon's relationship with the [[goddess]] [[Mystra]].<ref>{{Cite book/The North: Guide to the Savage Frontier/Cities & Civilization|53}}</ref>"
> — wiki line 93

**Wiki, Alustriel (*The North*, edition not printed)**
> "Not long thereafter, it was rumoured that Lady Alustriel sought out an alliance with Lady Phaulkon to address expansionist actions of [[Turlang]] [[Treant|the Treant]].<ref name="TN.CC-54">{{Cite book/The North: Guide to the Savage Frontier/Cities & Civilization|54}}</ref>"
> — wiki line 95
> "- [[Alustriel Silverhand]]: The ruler of Silverymoon considered Jeryth her ally.<ref name="TN.CC-54" />" — wiki line 83

**Wiki, Silvanus as grandfather (*The North*, edition not printed)**
> "* [[Silvanus]]: Jeryth was known to be the divine granddaughter of the Oak Father.<ref name="TN.TW-58">{{Cite book/The North: Guide to the Savage Frontier/The Wilderness|58}}</ref>" — wiki line 81

### A5. The garden, the Enclave and her position (day one)

**Campaign, her role (Enclave page, Structure)**
> "- **Secondary Contact:** Jeryth Phaulkon, the lady of the Phaulkonmere estate. She was a noblewoman before she became a Chosen of Mielikki, and for several years she has lived as a disembodied voice in the gardens. She cannot be harmed in this state, and she can cast any druid spell. She sends no one out on tasks, and the animals carry only Melannor's words."
> — `campaign/setting/organizations/03-emerald-enclave.md:56`

**Campaign, leadership (Enclave page, Structure)**
> "- **Leadership:** Jeryth is the highest Enclave authority in Waterdeep, and Melannor serves her and carries her words to the Enclave's members. No file names anyone above her or says whether the Waterdeep presence answers to a council elsewhere. [research] The Vilhon order was governed by an Elder Circle of three over seven circles of members (Forgotten Realms Wiki, *Emerald Enclave*, edition not stated), and the campaign gives the Waterdeep presence nothing like it."
> — `campaign/setting/organizations/03-emerald-enclave.md:52`

**Campaign, the Key Members entry (Enclave page)**
> "- **Jeryth Phaulkon** — Disembodied presence, Chosen of Mielikki; patron of Phaulkonmere; highest Enclave authority in Waterdeep. See the **Jeryth Phaulkon** page in Notable Figures."
> — `campaign/setting/organizations/03-emerald-enclave.md:89`

**Campaign, the garden (Enclave page, Structure)**
> "- **Phaulkonmere:** Its Waterdeep presence centers on Phaulkonmere, an old estate and garden in the Southern Ward. The gate stands open to anyone the Enclave has invited, and the garden is older than the street around it. No faction has ever openly violated the sanctuary. A walled villa stands among old oaks, its buildings covered with moss and ivy, and the manor has gathered wings and rooms over many generations (*Dragon Heist*, 5e; Alexandrian remix, Appendix B). The oldest oak stands at the center, and every path in the garden bends back to it."
> — `campaign/setting/organizations/03-emerald-enclave.md:54`

**Campaign, the garden and the gardeners (Southern Ward gazetteer)**
> "- The Tarm and Phaulkon families own it and spend most of the year abroad. **Melannor Fellbranch** keeps the grounds, and **Jeryth Phaulkon** speaks from the leaves as a disembodied voice. The gate stands open before an invited visitor arrives, and response teams may watch the street but never enter." — `campaign/gazetteer/waterdeep/southern-ward.md:43`
> "- A noblewoman who became a Chosen of Mielikki and now lives in the gardens of Phaulkonmere as a voice. She speaks one or two short sentences at a time, and the branches move when she speaks." — `campaign/gazetteer/waterdeep/southern-ward.md:116`

**Adventure, her introduction (page 36, entry "Jeryth Phaulkon")**
> "When the characters arrive at Phaulkonmere for the first time, {@creature Melannor Fellbranch|wdh|Melannor} introduces them to the lady of the estate: a noblewoman-turned-demigod and Chosen of Mielikki named Jeryth Phaulkon. Jeryth, the only member of her family who currently resides at Phaulkonmere, manifests as a disembodied female voice that can be heard by anyone in the villa gardens. She offers membership in the enclave and bestows on each new member a {@reward charm of restoration} (see \"Supernatural Gifts\" in chapter 7 of the {@book Dungeon Master's Guide|dmg}). Jeryth also offers Phaulkonmere as a safe haven for enclave members and their friends."
> — `sources/adventure-wdh.json:3717`
> "In her disembodied state, Jeryth can't be harmed. If the need arises, Jeryth can cast any spell on the {@filter druid|spells|class=druid} spell list. She uses her spells in defense of her estate and its beautiful gardens. A member of the Emerald Enclave can petition Jeryth to cast a spell, which she is happy to do if that character's renown in the enclave equals or exceeds the spell's level."
> — `sources/adventure-wdh.json:3718`

**Wiki, the 1492 DR status (no edition printed; the ref is 5e p. 36)**
> "As of [[1492 DR]], Lady Phaulkon's powers had grown so great that she had ascended to the status of a [[demipower]], having shed her physical form to become a disembodied voice and presence within the villa gardens of her family home, [[Phaulkonmere Villa]]. In this state, Jeryth served as a leader of the [[Emerald Enclave]], offering [[magic|magical]] aid to any of its members.<ref name="WDH5e-p36" />"
> — wiki line 97 (Conflicts D1 and D3)

**Wiki, the Enclave line (ref 5e p. 36)**
> "* [[Emerald Enclave]]: Jeryth served as one of the Enclave's leaders.<ref name="WDH5e-p36" />" — wiki line 84 (D3)

### A6. Her words and attitudes (Alexandrian, Appendix B)

> "\"I am Jeryth Phaulkon. This was my family's estate. In some sense it still is, though I occupy it differently now. Mielikki asked something of me several years ago, and I said yes, and here we are.\" There is no bitterness in the voice; it is simply a report. \"I watch over the garden. I watch over the city when I can. And I watch over those who do honest work in the world.\""
> — `sources/Appendix_B_-_Player_Factions.md:341`
> "\"Welcome to Phaulkonmere. I am sorry I cannot greet you more visibly. It has been some time since I could manage that.\""
> — `sources/Appendix_B_-_Player_Factions.md:339`
> "\"If you join us, this place is yours as a refuge. No questions asked, no favors owed for it — that is not how we work. What we ask instead is that you pay attention to what is being disrupted, and that you act on what you see. That is the whole of it.\""
> — `sources/Appendix_B_-_Player_Factions.md:343`
> "**Contact: Jeryth Phaulkon.** The lady of the estate, a noblewoman who has become a demigod and Chosen of Mielikki. She manifests as a disembodied voice heard throughout the villa's gardens. She cannot be harmed in this state, has access to the full druid spell list, and will cast spells for Enclave members whose renown equals or exceeds the spell's level."
> — `sources/Appendix_B_-_Player_Factions.md:297`
> "Phaulkonmere sits behind an iron gate in the Southern Ward, worked with reliefs of leaves and birds, standing open in the morning air. Beyond it is a garden of conspicuous wildness — not neglected, but deliberately allowed to grow in the directions nature would choose rather than those a gardener would impose. Stone paths run through it, worn smooth with long use. Old oak trees spread their branches overhead, and there are birds in them — actual birds, apparently unconcerned with being watched."
> — `sources/Appendix_B_-_Player_Factions.md:317` (rest of the passage covers: the manor house, which "has accumulated wings and rooms without any obvious architectural plan", and "The whole compound smells of turned earth and something green and quietly alive.")

### A7. The dreaming presence (day one, campaign)

**Campaign, Castle Ward (day one)**
> "- Jeryth Phaulkon has felt a dreaming presence below the Castle Ward for months. It is Illuun, an aboleth on Undermountain Level 4, and the Stone of Golorr woke it. It stirs the ward's water table and the cisterns. Enclave speakers say only that something dreams below, and no one in the ward knows its name." — `campaign/gazetteer/waterdeep/castle-ward.md:39`

**Campaign, Stone lore (day one; the gates are on lines 88 and 118)**
> "- **Who else senses it:** Jeryth Phaulkon of the Emerald Enclave has felt a dreaming presence below the Castle Ward for months and does not know its name. The Stone woke it, and **The Water Table Stirs** and **The Dreamer's Reach** carry the Enclave's side. Hlam felt an abolethic resonance for tendays in Force Grey's first mission, and a Harper seer felt something answer the Stone from below the city." — `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:87`
> "- **Who learns the name:** An Enclave member learns it when **Anchor Destroyed** is marked, or from the Stone at the Full Awakening. Otherwise nobody outside the GM knows it." — `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:88`

**Campaign, Mielikki page (day one)**
> "- **The Southern Ward and the Castle Ward:** Jeryth senses an infernal influence in the Southern Ward, and the Enclave knows it is there. Nobody in the Enclave knows whose it is. The Shrines of Nature stand in the Sea Ward, and no file connects them to it. Jeryth has also felt a presence dreaming below the Castle Ward for months, and her page says what a member can learn about it." — `campaign/setting/deities/mielikki.md:80`

### A8. Her Enclave concerns (day one)

**Campaign, Hold the Line Below (Enclave page, Beliefs)**
> "- **Hold the Line Below:** Jeryth's concern is something old and patient that she senses dreaming beneath the city, and she holds it back from the Castle Ward's water table. She wants whatever wakes below handled before it reaches the surface. Melannor feels the same unease in the earth beneath the Castle Ward and cannot say what it is." — `campaign/setting/organizations/03-emerald-enclave.md:44`

**Campaign, the Sanctuary (Enclave page, Beliefs)**
> "- **The Sanctuary Holds:** Phaulkonmere is a sacred space under Jeryth's protection and the one place in its ward that the Enclave defends, and she guards it with spells from the druid list (*Dragon Heist*, 5e). No faction has ever openly violated it." — `campaign/setting/organizations/03-emerald-enclave.md:41`

**Campaign, Grand Game Agenda (Enclave page)**
> "Its one stake lies below the city, and Jeryth wants whatever dreams beneath the Castle Ward held back from the surface." — `campaign/setting/organizations/03-emerald-enclave.md:93`

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, Summary: "> - *Disembodied presence, Neutral Good, Chosen of Mielikki, she/her*. Stat block: none (a disembodied presence, not a combatant)." — `02-jeryth-phaulkon.md:5`
- Campaign, gazetteer: "**Jeryth Phaulkon (Neutral Good, Disembodied Presence, she/her)**" — `campaign/gazetteer/waterdeep/southern-ward.md:115`
- Adventure: no alignment in the entry (`sources/adventure-wdh.json:3713` to `:3718`).
- Wiki: every alignment field is blank (wiki lines 40, 43, 46, 50, 54, 57).
- So only the campaign gives an alignment. The Mielikki page's "a neutral good god" (`campaign/setting/deities/mielikki.md:73`) describes the deity, not Jeryth.

**Species**
- Campaign: no species line. The Summary's first item reads "*Disembodied presence, Neutral Good, Chosen of Mielikki, she/her*" (`02-jeryth-phaulkon.md:5`). The Southern Ward gazetteer says: "Jeryth's page states no species, so the heading uses its \"disembodied presence\" line." (`campaign/gazetteer/waterdeep/southern-ward.md:252`)
- Adventure: "a noblewoman-turned-demigod and Chosen of Mielikki named Jeryth Phaulkon" (`sources/adventure-wdh.json:3717`); "a noblewoman turned demigod who serves Mielikki" (`:1320`)
- Appendix B: "a noblewoman who has become a demigod and Chosen of Mielikki" (`sources/Appendix_B_-_Player_Factions.md:297`)
- Wiki: "| race           = [[Human]], [[Demigod]]<ref name="WDH5e-p">{{Cite book/Waterdeep: Dragon Heist|217}}</ref>" — wiki line 14 (5e, p. 217)
- Wiki, class: "| class3e        = [[Divine champion]], [[Ranger]]<ref name="FRCS3e-p42"/>" — wiki line 48 (3e)
- Enclave Draft Notes: "The page keeps Chosen and drops demigod, and says so in History." (`campaign/setting/organizations/03-emerald-enclave.md:158`). The page as it stands does not say demigod and has no History section. Conflict D1.

**Pronouns and sex**
- Campaign: "she/her" — `02-jeryth-phaulkon.md:5`; "she/her" — `southern-ward.md:115`
- Adventure: "manifests as a disembodied female voice" — `sources/adventure-wdh.json:3717`
- Wiki: "| sex            = Female" — wiki line 13

**Stat block**
- Campaign, Summary: "Stat block: none (a disembodied presence, not a combatant)." — `02-jeryth-phaulkon.md:5`
- Adventure: no creature stat block. "In her disembodied state, Jeryth can't be harmed." — `sources/adventure-wdh.json:3718`
- Wiki: no stat block. Only 3e class fields are filled (wiki line 48). `class5e` is blank (wiki line 59).
- Page Morale: "Jeryth cannot be harmed in her disembodied state. She can cast any druid spell to defend the estate." — `02-jeryth-phaulkon.md:27`

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/emerald-enclave/02-jeryth-phaulkon.md`. It has no Background, Personality, Connections or `### Voice` section yet. Its GM callout is headed "What Is Actually True", not the **Secret** callout that brief ruling 8 asks for.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "- *Disembodied presence, Neutral Good, Chosen of Mielikki, she/her*. Stat block: none (a disembodied presence, not a combatant)." | Day one. Species gap (B, D1) | section B |
| 2 | L6 | "- **Affiliation:** Emerald Enclave (Chosen of Mielikki)" | Day one. Organization label: "# The Emerald Enclave" (`03-emerald-enclave.md:1`) | `03-emerald-enclave.md:89` |
| 3 | L7 | "- **Featured in:** **Fireball!**, **Gralhund Villa**, **Faction Outposts**, **Xanathar's Lair**, **Cassalanter Villa**, **Sea Maidens Faire**, **Kolat Towers**, **Vault of Dragons**, **Emerald Enclave First Meeting**, **A Seat at Phaulkonmere**, **The Water Table Stirs**, **Summerstrider**, **Ten Nights in the City of the Dead**, **The Doppelganger Problem**, **The Grells in the Dock Ward**, **Autumnreaver**, **The Fouled Channel**, **Winterstalker**, **The Dreamer's Reach**, **Master of the Wild**" | Quest names. Routed (brief ruling 1) | `campaign/quests/faction-events/emerald-enclave/` (folders `00-first-meeting`, `s01`, `s02`, `r03`, `r10`, `r25`, `r50`, `m01` to `m06`); `campaign/quests/act-ii/fireball/`; `campaign/quests/act-ii/gralhund-villa/`; `campaign/structure/arc-e-faction-outposts.md:85`, `:249`, `:373`; `campaign/structure/arc-f-xanathars-lair.md:428` |
| 4 | L9 | "Jeryth speaks one or two short sentences at a time, with long gaps between them. She never repeats or explains herself, never swears, and names no mortal politics. She calls Mielikki \"the Lady of the Forest\". She has lived in the gardens of Phaulkonmere for several years." | Day one. Keep | voice `emerald-enclave.md:27` to `:29`; `03-emerald-enclave.md:56` ("for several years") |
| 5 | L11 | "She does not dispatch missions. Melannor's animals carry the Enclave's requests, and the urgency in them is his." | Day one. Keep | `03-emerald-enclave.md:56` ("She sends no one out on tasks, and the animals carry only Melannor's words.") |
| 6 | L15 | "**Resonance.** Jeryth should inspire awe with her divine authority, comfort with the sanctuary she offers, and unease with the weight of a Chosen's rare, deliberate words." | Day one. Keep | `03-emerald-enclave.md:41` |
| 7 | L17 | "**Emotions.** Jeryth most often feels ancient patience, pressing urgency when something stirs below, warm approval expressed through the garden itself, and a focused intensity that makes her few words feel like verdicts." | Day one. Keep | voice `emerald-enclave.md:30` |
| 8 | L19 | "**Motivations.** Jeryth wants to protect the natural order from whatever is dreaming beneath the Castle Ward, offer Phaulkonmere as a sanctuary for those who serve the balance, and watch the party's handling of the Stone of Golorr with particular attention." | **Quest-time clause: "and watch the party's handling of the Stone of Golorr with particular attention."** The Stone reaches the party as a quest object: "the party has it by **Faction Outposts** (`campaign/structure/arc-e-faction-outposts.md:45`)" (`campaign/setting/deities/bane.md:130`). Restate the rest as day one. A standing Enclave ask exists: "That the Stone of Golorr not stay in one place longer than it must, because Jeryth believes the pressure below follows it." (`campaign/guides/factions/04-emerald-enclave.md:22`). Drafter's call | `campaign/guides/factions/04-emerald-enclave.md:22`; `campaign/setting/deities/bane.md:130` |
| 9 | L21 | "**Inspirations.** When playing Jeryth, channel the Oracle (*The Matrix*), the Great Deku Tree (*The Legend of Zelda*), and Galadriel (*The Lord of the Rings*, mirror scene)." | Not a fact. Keep | n/a |
| 10 | L25 | "**Persona.** To the world, Jeryth is a disembodied female voice heard by anyone in the Phaulkonmere gardens. Her voice comes from the leaves, the gravel and the air together, and the branches move when she speaks. To those she trusts, she is a noblewoman who became a Chosen of Mielikki and grants sanctuary, spells, and charms. Her approval shows in the garden, where flowers open and a warm breeze moves along the path. Deep down, she is disinterested in the dragon hoard. When asked about the gold, she answers once, \"That question is for the Lords to settle,\" and says nothing more. Her real concern is something old and patient that she senses dreaming beneath the city, and she does not know its name." | Day one throughout. The charm and spells have sources (`sources/adventure-wdh.json:3717`, `:3718`). "Her voice comes from the leaves, the gravel and the air together" is the page's own; no source names the gravel | `sources/adventure-wdh.json:3717`, `:3718`; `03-emerald-enclave.md:56`; `southern-ward.md:43` and `:116` |
| 11 | L27 | "**Morale.** Jeryth cannot be harmed in her disembodied state. She can cast any druid spell to defend the estate. She does not fight; she protects. When she says \"Enough,\" every vine in the garden tightens." | Day one. Keep | `sources/adventure-wdh.json:3718`; `03-emerald-enclave.md:67` ("**Fighting:** Jeryth does not fight and protects the garden instead, and when she says \"Enough\", every vine in it tightens.") |
| 12 | L29 | "**Relationships.** Jeryth is the Chosen of Mielikki, the patron of Phaulkonmere, and the Emerald Enclave's highest authority in Waterdeep. Her relationship with the party runs through Melannor, who relays her words as she speaks them. Her direct interventions carry the weight of divine mandate." | **Quest-time phrasing: "Her relationship with the party runs through Melannor".** Day-one version: "the animals carry only Melannor's words" (`03-emerald-enclave.md:56`). "Her direct interventions carry the weight of divine mandate" has no source sentence. The phrase "divine mandate" appears on the Mielikki page: "The Jeryth page treats her direct interventions as backed by divine mandate." (`campaign/setting/deities/mielikki.md:77`) | `03-emerald-enclave.md:52` and `:56`; `campaign/gazetteer/waterdeep/southern-ward.md:117` |
| 13 | L33 | "- Jeryth has held the dreaming presence back from the Castle Ward water table for months. It is Illuun, an aboleth on Undermountain Level 4, and the Stone of Golorr woke it." | Day one, a GM truth. Keep, in the GM callout | `campaign/gazetteer/waterdeep/castle-ward.md:39`; `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:87` |
| 14 | L34 | "- She never names it. Her words are \"Something dreams below,\" and in **The Water Table Stirs** alone she adds \"old, patient and hungry\". A member learns the name only through **Anchor Destroyed**, when she learns it as the anchor breaks and tells them, or from the Stone at Full Awakening. **Illuun Contact** alone gives the presence, not the name." | **Quest gates and a quest name.** "in **The Water Table Stirs** alone she adds" conflicts with the Factions Guide (D5). "A member learns the name only through **Anchor Destroyed**" and "**Illuun Contact** alone gives the presence" are gates. Day-one part: "She never names it. Her words are \"Something dreams below.\"" | `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:88` and `:118`; `campaign/quests/faction-events/emerald-enclave/m06-the-dreamers-reach/ev-02-the-anchor.md:89` and `:203` to `:204` (both cited by `03-emerald-enclave.md:181`); `ev-02-the-anchor.md:163` ("I do not know what it is called, and Jeryth has not said. It reached up from a long way below, and it stopped when the anchor broke."); `campaign/quests/faction-events/emerald-enclave/r50-master-of-the-wild/ev-01-master-of-the-wild.md:41`; `campaign/quests/faction-events/emerald-enclave/s02-the-water-table-stirs/ev-01-the-water-table-stirs.md:18` and `:164` |
| 15 | L35 | "- In **The Dreamer's Reach** she falls silent for three days. She wakes when the anchor breaks and speaks twice at the oak." | **Quest event.** Route | `campaign/quests/faction-events/emerald-enclave/m06-the-dreamers-reach/overview.md:85` ("Jeryth Phaulkon has fallen silent, and her garden has lost its sense of direction.") |
| 16 | L37-39 | "A disembodied female voice heard throughout the Phaulkonmere gardens, who addresses only those she has reason to speak to, and does so with few words and complete precision." | Day one. Keep | voice `emerald-enclave.md:31` ("She speaks only to those she has reason to address.") |

**Voice profile, quest-time clauses (`.claude/skills/character-voices/voices/emerald-enclave.md`, `### Jeryth Phaulkon`, lines 23-37)**

Ruling 16: a quest-time clause gets the day-one restatement, and the profile is changed to match. Each line:

- Line 24 (tagline): "*A disembodied voice in the gardens: few words, each one a verdict.*" — day one.
- Line 26 (Sound): "A clear, calm woman's voice that comes from everywhere in the garden at once, with leaves moving when she speaks." — day one.
- Line 27 (Sentence shape): "One or two short sentences, spaced far apart. Every sentence is complete and final. This is a deliberate break from `ember-voice` speech." — the first two sentences are the speech rule. **The last sentence is a production note for writers. It must not appear on the page.**
- Line 28 (Word choice): "Nature and time: seasons, roots, dreaming, balance. Mielikki is \"the Lady of the Forest\". She names no mortal politics." — day one.
- Line 29 (Swearing): "*Never · Plain · n/a.* Never." — day one. Keep (adult table).
- Line 30 (Personality in speech): "Ancient patience and urgency. Her approval comes through the garden itself: flowers opening, a warm breeze. Her disinterest in the gold is a single dismissal." — day one.
- Line 31 (Quirks): "She speaks only to those she has reason to address. The garden answers along with her." — day one.
- Line 32 (Signature phrases): "\"Something dreams below.\" / \"That question is for the Lords to settle.\" / \"Rest here.\"" — day one.
- Line 33 (Never): "She never chatters, never explains herself twice, and never takes a side in the Grand Game." — day one.
- Line 35 (Sample, Greeting): "\"You carry something heavy. Rest here.\"" — day one.
- Line 36 (Sample, Business): "\"The gold is for the Lords to settle. Watch what dreams beneath the Castle Ward.\"" — day one (a standing watch; no event named).
- Line 37 (Sample, Under pressure): "\"Enough.\" (every vine in the garden tightens)" — day one. The fighting rule is `03-emerald-enclave.md:67`.

No speech line in the profile is a quest-time clause. The one editorial problem is the production note on line 27.

---

## D. Conflicts

**D1. Species and "demigod" (campaign silent; published, Alexandrian and wiki say demigod)**
- Enclave Draft Notes: "> - **Conflicts, Jeryth's nature:** *Dragon Heist* says \"a noblewoman-turned-demigod and Chosen of Mielikki named Jeryth Phaulkon\" (`sources/adventure-wdh.json:3717`) and \"a noblewoman turned demigod who serves Mielikki\" (`:1320`). Appendix B says \"a noblewoman who has become a demigod and Chosen of Mielikki\" (`Appendix_B_-_Player_Factions.md:297`). Her Notable Figures page says \"Chosen of Mielikki\" (`02-jeryth-phaulkon.md:5`) and calls her no demigod. The page keeps Chosen and drops demigod, and says so in History. This corrects the earlier note, which implied that the published text never says Chosen." — `campaign/setting/organizations/03-emerald-enclave.md:158`
- Wiki: "| race           = [[Human]], [[Demigod]]" — wiki line 14; "As of [[1492 DR]], Lady Phaulkon's powers had grown so great that she had ascended to the status of a [[demipower]]..." — wiki line 97 (full line in A5)
- Higher-ranked source: the campaign for the name "Chosen" and for the absence of "demigod" on her page. The campaign records no species decision. Not settled.

**D2. The calling date (wiki, Appendix B, and the campaign's "several years")**
- Wiki (*Mielikki* page): "In the {{YearlinkName|1367}}, Mielikki appeared in a dream to Jeryth Phaulkon, a noble of Waterdeep, and offered to make her her chosen." — `sources/research/pass2-bundles/mielikki/wiki.txt:278`
- Wiki (Jeryth page): "By [[1367 DR]], Jeryth was believed missing or killed near [[Luskan]]..." — wiki line 89 (full line in A4)
- Wiki (Jeryth page): "The truth was however that as of [[1370 DR]], Jeryth lived within and roamed the High Forest as a ranger..." — wiki line 91 (full line in A4)
- Appendix B: "Mielikki asked something of me several years ago, and I said yes, and here we are." — `sources/Appendix_B_-_Player_Factions.md:341`
- Campaign: "She has lived in the gardens of Phaulkonmere for several years." — `02-jeryth-phaulkon.md:9`; "Several years before 1492 DR, the voice in the garden: Mielikki asks something of Jeryth, and she agrees and takes up her place as a disembodied voice in the gardens of Phaulkonmere (Alexandrian remix, Appendix B)." — `03-emerald-enclave.md:24`
- Enclave Draft Notes: "The page keeps both as separate entries and does not reconcile them." — `03-emerald-enclave.md:157`
- Higher-ranked source: the campaign for "several years" in the garden. The campaign does not date the calling. Not settled.

**D3. "One of the Enclave's leaders" (wiki) against "highest authority" (campaign)**
- Wiki: "* [[Emerald Enclave]]: Jeryth served as one of the Enclave's leaders." — wiki line 84
- Campaign: "the Emerald Enclave's highest authority in Waterdeep" — `02-jeryth-phaulkon.md:29`; "Jeryth is the highest Enclave authority in Waterdeep" — `03-emerald-enclave.md:52`
- Higher-ranked source: the campaign.

**D4. The wiki disagrees with itself about 1367 DR**
- Wiki line 89 says she was "believed missing or killed" and that the Hoar Fang massacre was "due to the schemes of a [[doppelganger]] member of the [[Unseen]]".
- The wiki's *Mielikki* page (`wiki.txt:278`) says "Jeryth happened to be their captive at the time. Imbued with the goddess's powers, Jeryth freed herself and her companions".
- Neither version is in the campaign. The Enclave Draft Notes use only the *Mielikki* version (`03-emerald-enclave.md:22`).

**D5. "Old, patient and hungry" (Factions Guide against this page)**
- Factions Guide: "Jeryth has felt a dreaming presence in the earth beneath the Castle Ward since before the campaign begins. She calls it old, patient and hungry, and she does not know its name." — `campaign/guides/factions/04-emerald-enclave.md:9`
- This page: "and in **The Water Table Stirs** alone she adds \"old, patient and hungry\"." — `02-jeryth-phaulkon.md:34`
- Both are campaign files. The Enclave Draft Notes flag it (`03-emerald-enclave.md:182`). Not settled.

**D6. Where the infernal influence is (Factions Guide against the rest)**
- Factions Guide: "Enclave druids feel an infernal influence in the Sea Ward." — `campaign/guides/factions/04-emerald-enclave.md:32`
- Sea Ward gazetteer: "Nobody in the ward knows. Every faction suspects the family because it is too nice to be this rich, and none knows about the pact. Savra Belabranta of the Order of the Gauntlet hunts for proof, and Jeryth Phaulkon feels an infernal influence in the Southern Ward that the Emerald Enclave cannot trace to a house. The one exception is Jarlaxle, who knows through **Vessa**, his doppelganger spy in the Cassalanter social circle, and tells Bregan D'aerthe members nothing unless they work it out." — `campaign/gazetteer/waterdeep/sea-ward.md:38`
- Mielikki page: "Jeryth senses an infernal influence in the Southern Ward" — `campaign/setting/deities/mielikki.md:80`
- Higher-ranked source: the campaign (Southern Ward). The Factions Guide line is stale (`03-emerald-enclave.md:159`).

**D7. Where the dreaming presence is (Appendix B against the campaign)**
- Appendix B: "something wrong in the earth beneath the Southern Ward" — `sources/Appendix_B_-_Player_Factions.md:367` (in the renown bullet "Assist Jeryth Phaulkon with a magical or druidic task at her request (+2).")
- Castle Ward: "Jeryth Phaulkon has felt a dreaming presence below the Castle Ward for months." — `campaign/gazetteer/waterdeep/castle-ward.md:39`
- Factions Guide: "in the earth beneath the Castle Ward" — `campaign/guides/factions/04-emerald-enclave.md:9`
- Higher-ranked source: the campaign (Castle Ward). The Enclave Draft Notes settle it (`03-emerald-enclave.md:160`).

**D8. Spells (Appendix D against the adventure and Appendix B)**
- Adventure: "If the need arises, Jeryth can cast any spell on the {@filter druid|spells|class=druid} spell list." — `sources/adventure-wdh.json:3718`
- Appendix B: "has access to the full druid spell list" — `sources/Appendix_B_-_Player_Factions.md:297`
- Appendix D: "Jeryth Phaulkon can cast *Fabricate* to transform the manor's own salvaged materials into finished repair stock, effectively <strong>reducing renovation cost by 250 gp</strong>." — `sources/Appendix_D_-_Running_the_Tavern.md:806` (a Trollskull Manor advice box)
- Whether *Fabricate* is on the druid list was not checked in this pass. Flag for the orchestrator.

**D9. How long the wound has lasted (quest-linked)**
- `campaign/structure/arc-e-faction-outposts.md:85`: "Jeryth Phaulkon has been monitoring a disturbance in the Southern Ward for two weeks."
- `campaign/gazetteer/waterdeep/southern-ward.md:121`: "Jeryth's Southern Ward report in **Summerstrider** is that she has felt a wound in the ley lines near Coachlamp Lane for a tenday and a half, and she senses infernal influence there."
- Enclave Draft Notes: "The page gives no figure and tags the onset `[research]`." — `03-emerald-enclave.md:164`

**D10. Rats (adventure against the campaign's Xanathar's Lair)**
- Adventure: "Jeryth tells them that she has been sending {@creature awakened rat|wdh|awakened rats} into the sewers to find the beholder's lair, and that they recently discovered a secret staircase in the Castle Ward sewers leading down to it ({@area X1|271})." — `sources/adventure-wdh.json:15181`
- Campaign: "- **Melannor:** \"Did anything unusual happen to the underground water systems near the collapse point?\"" — `campaign/structure/arc-f-xanathars-lair.md:296` (Melannor's sewer scouting stands in for the rats). The Enclave Draft Notes leave the rats out (`03-emerald-enclave.md:168`).

---

## E. Stale lines in other files (not to be edited) and routed quest references

**E1. Stale or conflicting lines in other files**
- `campaign/guides/factions/04-emerald-enclave.md:32`: "Enclave druids feel an infernal influence in the Sea Ward." — stale (D6).
- `campaign/guides/factions/04-emerald-enclave.md:9`: "old, patient and hungry" before the campaign (D5).
- `campaign/setting/deities/mielikki.md:81`, `campaign/gazetteer/waterdeep/southern-ward.md:48` and `campaign/setting/notable-figures/emerald-enclave/02-jeryth-phaulkon.md:34` still carry "Until **Manshoon Named** is marked" or **Anchor Destroyed** gates. Ruling 28 asks setting pages to restate them as day-one facts (listed at `03-emerald-enclave.md:187`). `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:88` and `:118` carry the **Anchor Destroyed** gate.
- `campaign/gazetteer/waterdeep/southern-ward.md:121` places Jeryth's report in **Summerstrider**, a quest event (D9).
- `campaign/setting/deities/eldath.md:104` says the campaign Enclave names Mielikki as its patron through Jeryth. `campaign/setting/deities/mielikki.md:67` says: "No campaign file calls Mielikki the Enclave's patron." (`03-emerald-enclave.md:187` flags the Eldath line too.)
- `sources/Appendix_D_-_Running_the_Tavern.md:806` (*Fabricate*, D8).
- `sources/3. Player Character Factions.pdf`, printed page 24 (transcription, check with `pdftotext`): "The **Harpers** know that the Cassalanters are actually demon-worshippers and, if they realize the PCs have gotten tangled up with them, will quickly warn them of the fact." The Cassalanter secrecy rule overrules it. Not a Jeryth line; listed because it sits on the same page as the Enclave sentence.

**E2. Routed quest references (quest time; the day-one page does not restate them)**
- `s02-the-water-table-stirs/ev-01-the-water-table-stirs.md:18` and `:164` ("old, patient and hungry"; the Enclave Draft Notes say "Jeryth says 'old, patient and hungry' in **The Water Table Stirs** and nowhere else." at `03-emerald-enclave.md:182`).
- `m06-the-dreamers-reach/ev-02-the-anchor.md:89` and `:203` to `:204`; `r50-master-of-the-wild/ev-01-master-of-the-wild.md:41` (the name and the gates; per `03-emerald-enclave.md:181`).
- `m06-the-dreamers-reach/overview.md:85` ("Jeryth Phaulkon has fallen silent, and her garden has lost its sense of direction.").
- `m06-the-dreamers-reach/ev-01-the-descent.md:17` (the anchor); `m05-the-fouled-channel/overview.md:21` to `:30` and `ev-01-the-fouled-channel.md:23` (the water-table route; per `03-emerald-enclave.md:183`).
- `campaign/structure/arc-e-faction-outposts.md:249`: "Mirt can connect the party with an Enclave contact who has been narrowing the Southern Ward infernal resonance to a North Ward secondary signature." An unidentified Enclave contact. Enclave Draft Notes leave it open (`03-emerald-enclave.md:161`).
- `campaign/structure/arc-e-faction-outposts.md:373`: "If the windmill was not cleared: Jeryth's garden is showing symptoms — herbs dying, birds leaving the grounds, a persistent wrongness spreading rather than shrinking." — quest time (rest of the passage covers the Founders' Day pressure).
- `campaign/structure/arc-f-xanathars-lair.md:428`: "Before the party enters Xanathar's lair, Jeryth Phaulkon provides an enchanted herb sprig that functions as a mild psychic shield." — quest time.
- `campaign/structure/arc-i-kolat-towers.md:37` (the renown 10+ spell "Jeryth Phaulkon casts pass without trace on the entire party").
- `r03-summerstrider/ev-01-summerstrider.md:189` (the Southern Ward wound report, per `southern-ward.md:251`).
- `r10-autumnreaver/ev-01-autumnreaver.md:35` (the twelve years of maintenance, per `03-emerald-enclave.md:174`) and `:134` (the sprig does not work underground, per `campaign/setting/geography/undermountain-and-skullport.md:112`).
- `r25-winterstalker/ev-01-winterstalker.md:37` (the four years, per `03-emerald-enclave.md:174`).
- `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:110` (the minor ley line the Enclave monitors, per `03-emerald-enclave.md:82`).
- `campaign/gazetteer/waterdeep/castle-ward.md:38`: "Mirt, Jalester Silvermane, Yagra Stonefist and Jeryth's awakened rats each lead a party to it" — quest route to the Xanathar stair.
- `campaign/guides/factions/04-emerald-enclave.md:23`: "She is ready without notice if **Anchor Destroyed** is marked, and she needs notice from the party if it is not." — gate; route.
- `campaign/guides/factions/04-emerald-enclave.md:33`: "If **The Dreamer's Reach** has run and **Anchor Destroyed** is marked, Jeryth is awake and needs no notice." — gate; route.
- `sources/adventure-wdh.json:14819`: "Jeryth Phaulkon sends three {@creature swarm of rats||swarms of rats} to assist the characters. Once the characters are no longer in peril, the rats disperse throughout the vault." — quest time (Vault of Dragons).
- `sources/adventure-wdh.json:15181` (the rats to the Xanathar lair; D10).
- `sources/Appendix_C_-_Player_Faction_Missions.md:921` ("Jeryth Phaulkon bestows a *charm of heroism* (supernatural gift, 2024 *DMG*) on every party member who helped ...") — quest time (Master of the Wild). The quote is cut where the Appendix's passage goes on to the walk back.
- `sources/Appendix_D_-_Running_the_Tavern.md:805` to `:806` (Trollskull Manor renovation, *Fabricate*).

---

## F. Gaps a Background would need that no source gives

Invented material carries `[design]` and is listed in Draft Notes (brief ruling 17).

1. **Species.** Open (D1). The campaign has no species line. Do not write one without the orchestrator's decision.
2. **Birth date, age, and her look before 1367.** The wiki gives looks (wiki lines 67 to 75) but no birth date or age. The campaign has no physical description.
3. **Her mother's death and her own disappearance.** Cera died in a 1367 DR caravan raid (wiki line 79). Jeryth was "believed missing or killed" (wiki line 89), or a captive who freed herself (`wiki.txt:278`). No campaign file says which. D2 and D4.
4. **The calling.** The date and the form are open (D2). Consistent with "Mielikki asked something of me several years ago, and I said yes" (`sources/Appendix_B_-_Player_Factions.md:341`).
5. **The years between the calling and the garden.** The wiki has the High Forest ranger years (wiki line 91) and Everlund and Tyrar (wiki line 93). No campaign source. The campaign has "for several years" in the garden (`02-jeryth-phaulkon.md:9`).
6. **How she became a disembodied voice.** The wiki says she "shed her physical form to become a disembodied voice and presence" (wiki line 97). The campaign does not say how.
7. **Her family after 1367.** Bronson, Cera and Marie are wiki only (wiki lines 78 to 80). The Tarms co-own the estate (`03-emerald-enclave.md:101`). No campaign source names a Tarm.
8. **The betrothal to Arum Tarm.** Wiki only (wiki line 82). Consistent with "Phaulkonmere is owned by the Tarm and Phaulkon noble families" (`sources/adventure-wdh.json:3700`).
9. **Her personal goals.** None sourced. The page's Motivations (`02-jeryth-phaulkon.md:19`) are the Enclave's and the estate's. Consistent with "protect the natural order", "offer Phaulkonmere as a sanctuary", and her standing concern for "something old and patient" (`02-jeryth-phaulkon.md:25`).
10. **Her feelings about her body.** Sourced hints only (G). No source states them.
11. **Alustriel and Tyrar.** Wiki only (wiki lines 83, 93, 95). No campaign source.
12. **When she first knew of the Stone.** The campaign says she has felt the presence "for months" (`castle-ward.md:39`) and that the Stone "woke it" (`stone-of-golorr-and-the-eyes.md:87`). No file says when she learned of the Stone.

---

## G. Source facts that hint at inner life (quotes; the Background must not contradict them)

- **Her manner.** "There is no bitterness in the voice; it is simply a report." — `sources/Appendix_B_-_Player_Factions.md:341`
- **Regret at what she cannot do.** "I am sorry I cannot greet you more visibly. It has been some time since I could manage that." — `sources/Appendix_B_-_Player_Factions.md:339`
- **Her duty, in her words.** "I watch over the garden. I watch over the city when I can. And I watch over those who do honest work in the world." — `sources/Appendix_B_-_Player_Factions.md:341`
- **Her family's house.** "This was my family's estate. In some sense it still is, though I occupy it differently now." — `sources/Appendix_B_-_Player_Factions.md:341`
- **What she asks in return.** "What we ask instead is that you pay attention to what is being disrupted, and that you act on what you see. That is the whole of it." — `sources/Appendix_B_-_Player_Factions.md:343`
- **Her habit before her disappearance.** "Jeryth had a habit of playing with her hair, twisting it around her fingers." — wiki line 71
- **Her reputation before her disappearance.** "Despite this, she was beloved and respected for her forthrightness and honesty." — wiki line 69
- **The change after the calling.** "Jeryth's personality additionally altered itself to far more represent the ways of her goddess, becoming carefree like a bird." — wiki line 73
- **Her strictness.** "Jeryth has however also grown strict in the face of those who would misuse nature, following the most conservative credos of rangers." — wiki line 75
- **Her interest in the gold.** "Deep down, she is disinterested in the dragon hoard." — `02-jeryth-phaulkon.md:25`
- **Her concern.** "Her real concern is something old and patient that she senses dreaming beneath the city, and she does not know its name." — `02-jeryth-phaulkon.md:25`
- **Her concern about what wakes.** "She wants whatever wakes below handled before it reaches the surface." — `campaign/setting/organizations/03-emerald-enclave.md:44`
- **Her delight in the garden.** "Her approval shows in the garden, where flowers open and a warm breeze moves along the path." — `02-jeryth-phaulkon.md:25`
- **Her silence.** "She never chatters, never explains herself twice, and never takes a side in the Grand Game." — voice `emerald-enclave.md:33`
- **Her view of the gold.** "That question is for the Lords to settle." — `02-jeryth-phaulkon.md:25`; "Jeryth gives the same answer to anyone who asks: \"That question is for the Lords to settle.\"" — `campaign/setting/organizations/03-emerald-enclave.md:93`
- **Her garden under strain (quest time; route).** "Jeryth's garden is showing symptoms — herbs dying, birds leaving the grounds, a persistent wrongness spreading rather than shrinking." — `campaign/structure/arc-e-faction-outposts.md:373`

---

## Draft Notes material for the drafter (short)

- Settled for day one: the Cormyr origin (A1); the Tarms co-own the estate (A1); "for several years" in the garden (A5); Chosen of Mielikki and the disembodied state (A5, B); she/her (B); the Southern Ward garden and the Castle Ward presence (A7, D7); Illuun named in the Castle Ward gazetteer and Stone lore (A7).
- Open for the orchestrator: species and demigod (D1); the calling date (D2); "old, patient and hungry" (D5); the *Fabricate* line (D8); whether the Stone wish in Motivations stays (row 8).
- Open for the drafter: strip the production note on voice line 27; restate the quest-time phrases in Motivations (row 8), Relationships (row 12) and the GM callout's gates (rows 14 and 15); rename "What Is Actually True" to the Secret callout form the brief asks for, or justify keeping it.
- Not run: `voicecheck.py`.
