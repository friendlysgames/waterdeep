# Batch D research report: Mielikki, Silvanus, Chauntea, Eldath, Malar

## Conventions

- **Bundle root (absolute):** `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/`. Citations such as `mielikki/wiki.txt:207` are relative to this root.
- **Repo root (absolute):** `/home/user/waterdeep/`. Citations such as `sources/adventure-wdh.json:1320` and `campaign/...` are relative to it.
- **Wiki markup:** The wiki's `[[ ]]` link brackets are removed in every wiki quote. A piped link shows its display text. Where a quote also drops `<ref>` citation tags or `''` italic markup, the citation for that quote is given after it. Nothing else is changed. Where a wiki line has several sentences and I skip some, each quoted sentence is its own quote with the same line number. No ellipsis appears inside any quote.
- **Wiki edition tags:** taken from the infobox row that holds the fact (`power1e`/`2e`/`3e`/`4e` rows, or the `5e`/`5eR` rows), or from the book named in the citation. Where neither gives an edition, the tag says "edition not stated". The wiki's own note at `mielikki/wiki.txt:192` says *Faiths & Avatars* is 2nd edition and *Faiths and Pantheons* is 3rd edition.
- **5etools:** FRHoF is the current canon. SCAG (2014) is used only for alignment, domains and symbol, per the brief. PHB 2014 entries are shown where they conflict.
- **Searched:** all `campaign/**/*.md` and both adventure JSON files, by name and alias (aliases are listed under each power's Not found). Bundle hit lists were checked against my own Grep.
- **Not searched (out of scope for this job):** the Alexandrian PDFs, `SOURCE_GUIDE.md`, the Appendix markdown files, and session handoffs. `sources/Appendix_B_-_Player_Factions.md` names Mielikki at lines 297 and 341 and was not read.
- **Deviation from the brief:** campaign lines that name Jeryth or Phaulkon but not Mielikki are summarised by file and count, not copied one by one. Grep found 543 such occurrences in 59 files. Every campaign line that names Mielikki is copied.

## Summary of hits

- **Waterdeep worship, by the files:** Mielikki and Silvanus share the "Shrines of Nature" in the Sea Ward (published adventure). Mielikki also has Phaulkonmere in the Southern Ward, with Jeryth Phaulkon as Chosen. Malar has the Howldown festival (published adventure) and a Level 5 cult complex in Undermountain. Eldath has one campaign NPC, Avi, and no shrine. Chauntea has nothing.
- **Campaign files:** name Mielikki only through Jeryth and the Enclave, and name Eldath only through Avi. They do not name Silvanus, Chauntea or Malar.
- **Premise check:** No campaign file calls Mielikki the Emerald Enclave's patron. Campaign files call Jeryth the "patron of Phaulkonmere" and "Chosen of Mielikki". See Mielikki, Field 7.

---

# 1. MIELIKKI

## Field 1. Identity

**5etools, FRHoF p.115 (current canon, 2024-era)**
> "## Mielikki | source FRHoF p.115 | pantheon Faerûnian"
> "- altNames: ['Our Lady of the Forest', 'The Forest Queen']"
> "- title: God of forests"
> "- worshipers: Fey, foresters, Rangers"
> "- plane: The Beastlands (Krigala)"
> — `mielikki/5etools.md:1-5`

**5etools, SCAG p.21 (2014; fallback for alignment, domains, symbol)**
> "## Mielikki | source SCAG p.21 | pantheon Faerûnian"
> "- altNames: ['Our Lady of the Forest', 'The Forest Queen']"
> "- title: Goddess of forests"
> "- alignment: ['N', 'G']"
> "- domains: ['Nature']"
> "- symbol: Unicorn's head"
> — `mielikki/5etools.md:22-27`

**5etools, PHB p.294 (2014; same values as SCAG)**
> "## Mielikki | source PHB p.294 | pantheon Forgotten Realms"
> "- title: Goddess of forests"
> "- alignment: ['N', 'G']"
> "- domains: ['Nature']"
> "- symbol: Unicorn's head"
> — `mielikki/5etools.md:14-18`

**Wiki title row** (editions by ref group: 1e and 2e refs on "Lady of the Forest"; 3e and 5e refs on "The Forest Queen" and "Our Lady of the Forest")
> "| title               = Mistress of the Forest<ref name="D&D1e-p60" /><ref name="OHG-p104" /><br/>Lady of the Forest<ref name="FRCS1e-p12" /><ref name="Dragon54" /><ref name="FRA-p26" /><ref name="FRCS2e-RTR-p52" /><ref name="FRCS2e-Cards" /><br/>The Forest Queen<ref name="FRCS3e-p246" /><ref name="FaP-p48" /><ref name="EGPEFR-p154" /><ref name="SCAG5e-p21,34" /><ref name="HoF-p115" /><br />Our Lady of the Forest<ref name="F&A-p112" /><ref name="FRCS3e-p246" /><ref name="FaP-p48" /><ref name="SCAG5e-p21,34" /><ref name="HoF-p115" /><br />The Supreme Ranger<ref name="F&A-p112" /><br/>Daughter to Silvanus<ref name="FRCS2e-RTR-p52" /><ref name="F&A-p112" />"
> — `mielikki/wiki.txt:6`

**Wiki 5e and pantheon rows** (brackets removed)
> "| pantheon            = Faerûnian pantheon, Finnish pantheon, Seldarine" — `mielikki/wiki.txt:11`
> "| alignment5e         = Neutral good" — `mielikki/wiki.txt:38`
> "| symbol5e            = Unicorn's head" — `mielikki/wiki.txt:39`
> "| homeplane5eR        = The Beastlands (Krigala)" — `mielikki/wiki.txt:25`

Areas of Concern: no field in any Mielikki entry, 5etools or wiki.

## Field 2. Edict or core tenet

No edict or dogma appears in any of the five source sets. The closest lines follow.

> "People rarely speak of Mielikki except in quiet forest spaces. Woodlands that evoke wonder are where she reigns supreme, but she is said to keep watch over good folk in any forest, not matter how dark or cruel. When children are lost in the woods, people beseech Mielikki to protect them until they are found."
> — `mielikki/5etools.md:29` (SCAG 2014)

> "Mielikki also watched over rangers, druids, dryads and other forest beings,<ref name="D&D1e-p60" /><ref name="OHG-p104" /> as well as good people and lost children in any woodland, regardless of how evil the threats against them."
> — `mielikki/wiki.txt:184` (first sentence; refs 1e D&D p.60, 2e On Hallowed Ground p.104)

> "While she knew that death was a part of life and some must die so that others may live, she could not just accept injuries and deaths of both animals and friends."
> — `mielikki/wiki.txt:133` (personality, not a tenet)

## Field 3. Portfolio and Areas of Concern

> "Good natured, confident, and fiercely loyal to her allies, Mielikki is a god of the woods and the creatures who live within them."
> — `mielikki/5etools.md:7` (FRHoF)

> "Mielikki is the goddess of the forest and the creatures that live within it. She is seen as a remote and spiritual deity - less human-like than many other gods. She's not unmindful of people, but her attention and favor are difficult to attract. She is the patron of rangers in the same way that Milil is the patron of bards, but even rangers rarely pray to her directly. They instead pray to Gwaeron Windstrom, who they believe will carry their words to the goddess by tracking her to whichever forest she hides in."
> — `mielikki/5etools.md:30` (SCAG 2014)

> "| portfolio5e         = Forests" — `mielikki/wiki.txt:44` (5e)

> "| portfolio3e         = Autumn, dryads, forest creatures, forests, rangers" — `mielikki/wiki.txt:73` (3e; brackets removed)

> "| portfolio2e         = Forests, forest creatures, rangers, dryads, autumn, nature (Finnish pantheon only)" — `mielikki/wiki.txt:90` (2e; brackets removed)

> "In the chaos of the aftermath, Mielikki claimed the portfolio of autumn from the deceased god Myrkul.<ref name="FRCS2e-RTR-p52" /><ref name="F&A-p112" />"
> — `mielikki/wiki.txt:274` (refs 2e: FRCS2e-RTR p.52; F&A, which the wiki's line 192 calls 2nd edition)

## Field 4. Worship (Waterdeep first: see Q1)

> "Mielikki's followers don't organize into official temples. Instead, they assemble in peaceful wooded glades to worship her or create shrines in her honor. A typical shrine to Mielikki is a dead tree trunk into which has been carved the likeness of her holy symbol: a unicorn or unicorn's head. Such a shrine marks a point in the forest beyond which locals know not to cut timber or hunt; in this way, followers thank Mielikki for the forest's bounty."
> — `mielikki/5etools.md:8` (FRHoF)

> "When she makes her will known on the Material Plane, Mielikki manifests as a confident voice in a forest glade. Alternatively, she sends a {@creature Dryad|XMM}, {@creature Hawk|XMM}, or {@creature Unicorn|XMM} as a messenger."
> — `mielikki/5etools.md:7` (FRHoF; messengers)

> "On {@book Greengrass|FRHoF|2|Greengrass} and {@book Midsummer|FRHoF|2|Midsummer}, Mielikki blesses her followers with an event called the Wild Ride."
> — `mielikki/5etools.md:11` (FRHoF; holy days)

> "| holy days2e         = Four Feasts: summer solstice, winter solstice, spring equinox, autumn equinox; Greengrass; Midsummer; Shieldmeet"
> — `mielikki/wiki.txt:98` (2e row; brackets removed)

> "The majority of rangers revered Mielikki, as their leader, their watchful mother, and the supreme ranger.<ref name="F&A-p113" />"
> — `mielikki/wiki.txt:221` (2e; F&A p.113; brackets removed)

> "| misc manifestations = Confident voice in a forest glade" — `mielikki/wiki.txt:119` (omen row; manifestation ref HoF p.115, 5e-era book)

Also in the bundle, not quoted above: "The faithful, however, believed her most common manifestation was her whispering voice, echoing forever through all the forests of the world via the rustling of leaves." (`mielikki/wiki.txt:146`, refs CDM p.65 and F&A pp.113-114).

## Field 5. Relations with other powers, and origin (edition tagged)

> "Mielikki is allied with Silvanus but she takes pity on hurt creatures Silvanus ignores. Mielikki has a close bond with Lurue, god of unicorns, and Lurue serves as her mount when Mielikki goes hunting in the Beastlands. Rangers of Mielikki serve as a line of defense against marauders and followers of the god Malar."
> — `mielikki/5etools.md:10` (FRHoF)

> "Mielikki was a servant of Silvanus, the Oak-Father, together with Chauntea, the Grain Goddess, and Eldath, the Goddess of Singing Water.<ref name="FRCS1e-p12" /><ref name="FRA-p26" /><ref name="F&A-p112" /><ref name="FRCS3e-p246" /><ref name="FaP-p48" /><ref name="FRCS1e-p17">{{Cite book/Forgotten Realms Campaign Set/Cyclopedia of the Realms|17}}</ref><ref>{{Cite book/Forgotten Realms Campaign Setting 2nd edition (revised)/Running the Realms|46,48,54}}</ref><ref name="FRCS2e-Cards" /><ref>{{Cite book/Faiths & Avatars|3,47,57,145}}</ref> Mielikki, Eldath, and Silvanus counted each other as allies, worked in harmony, and held true trust and affection for one another, and these relationships were mirrored in the alliances of their churches and priests.<ref name="F&A-p112" /><ref name="SCAG5e-p21,34" /><ref name="F&A-p57">{{Cite book/Faiths & Avatars|57,145}}</ref>"
> — `mielikki/wiki.txt:190` (brackets removed; refs 1e Cyclopedia; 2e FRA, F&A; 3e FRCS and Faiths and Pantheons)

> "Although her followers sometimes referred to her with the honorific '''Daughter to Silvanus''', Mielikki was not actually the daughter of Silvanus; rather, she considered him a father figure."
> — `mielikki/wiki.txt:192` (first sentence)

> "3{{rd}}-edition's ''Faiths and Pantheons'' explicitly calls Silvanus her father and Eldath her sister, but the earlier 2{{nd}}-edition sourcebook ''Faiths & Avatars'' makes it clear that these were mortal misunderstandings."
> — `mielikki/wiki.txt:192` (the wiki's own `<ref group="note">`)

> "While she served Silvanus, she in turn was served by Gwaeron Windstrom, Lurue, and Shiallia.<ref name="FRCS1e-p17" /><ref name="FRA-p26" /><ref name="F&A-p112" /><ref name="FRCS3e-p246" /><ref name="FaP-p48" /><ref>{{Cite book/Powers & Pantheons|26,36,55}}</ref>" (brackets removed)
> — `mielikki/wiki.txt:194` (refs 1e, 2e, 3e)

> "After the Spellplague, Shiallia was counted as Mielikki's exarch.<ref name="FRCG4e-p63" />" (brackets removed)
> — `mielikki/wiki.txt:194` (4e, FRCG4e p.63)

> "Mielikki was also allies with Shaundakul, Lathander, and Nobanion, and was of course an enemy of Malar, Moander, Myrkul, Talona, and Talos." (brackets removed; refs as written in the file are not reproduced)
> — `mielikki/wiki.txt:196` (refs F&A, FRCS3e, FaP, Powers & Pantheons)

> "Mielikki hailed from the Finnish pantheon.<ref name="FRCS1e-p12" /><ref>{{Cite book/Faiths & Avatars|14}}</ref>" (brackets removed)
> — `mielikki/wiki.txt:230` (origin; 1e Cyclopedia p.12; 2e F&A p.14)

## Field 6. Campaign and published-adventure mentions

> "Members of the Emerald Enclave can be found in Phaulkonmere, a noble villa in the Southern Ward, and at the Snobeedle Orchard and Meadery in Undercliff. The walls of Phaulkonmere enclose fabulous gardens, and the buildings are covered with moss and ivy. The place is owned by descendants of two wealthy families-the Tarms (longtime Waterdavians) and the Phaulkons (who are of Cormyrean descent). They spend most of the year traveling abroad and entrust the estate to a half-elf groundskeeper named {@creature Melannor Fellbranch|wdh}. He is joined by Jeryth Phaulkon, a noblewoman turned demigod who serves Mielikki, divine lady of the forest."
> — `sources/adventure-wdh.json:1320`

> "When the characters arrive at Phaulkonmere for the first time, {@creature Melannor Fellbranch|wdh|Melannor} introduces them to the lady of the estate: a noblewoman-turned-demigod and Chosen of Mielikki named Jeryth Phaulkon."
> — `sources/adventure-wdh.json:3717` (first sentence; the rest of the passage covers the Enclave charm and the offer of Phaulkonmere as a haven)

> "The Shrines to Nature, just a block away from the Tower of Luck, are resplendent gardens dedicated to nature gods like Mielikki and Silvanus. The park is closed to all except residents of the Sea Ward. Yet from beyond the iron fence that surrounds it, you can catch glimpses of the superb shrines, statues, and fountains within."
> — `sources/adventure-wdh.json:30884` (first three sentences; the rest covers the Heroes' Garden)

> `"Mielikki, Silvanus",` — `sources/adventure-wdh.json:30953` (Major Temples row; see Q1 for the full row)

> "- **Jeryth Phaulkon** — Disembodied presence, Chosen of Mielikki; patron of Phaulkonmere; highest Enclave authority in Waterdeep. See the **Jeryth Phaulkon** page in Notable Figures."
> — `campaign/setting/organizations/03-emerald-enclave.md:29`

> "**Relationships.** Jeryth is the Chosen of Mielikki, the patron of Phaulkonmere, and the Emerald Enclave's highest authority in Waterdeep. Her relationship with the party runs through Melannor, who relays her words as she speaks them. Her direct interventions carry the weight of divine mandate."
> — `campaign/setting/notable-figures/emerald-enclave/02-jeryth-phaulkon.md:29`

> "She calls Mielikki "the Lady of the Forest". She has lived in the gardens of Phaulkonmere for several years." — `campaign/setting/notable-figures/emerald-enclave/02-jeryth-phaulkon.md:9` (the rest of the paragraph covers her manner of speech)

## Field 7. Conflicts between sources, and what was not found

**Conflicts**

1. **Title and gender.** FRHoF: "- title: God of forests" (`mielikki/5etools.md:3`). PHB and SCAG: "- title: Goddess of forests" (`mielikki/5etools.md:15`, `:24`). Wiki gender row: "| gender              = Feminine<ref name="FRCG4e-p80" />" (`mielikki/wiki.txt:14`). The FRHoF text uses "she" ("When she makes her will known", `mielikki/5etools.md:7`). FRHoF is the higher-ranked source. The drafter must choose the title.
2. **Relation to Silvanus.** FRHoF: "Mielikki is allied with Silvanus" (`mielikki/5etools.md:10`). Wiki: "Mielikki was a servant of Silvanus" (`mielikki/wiki.txt:190`). SCAG: "Silvanus is sometimes thought of as her father" (`mielikki/5etools.md:31`). Wiki: "Mielikki was not actually the daughter of Silvanus" (`mielikki/wiki.txt:192`).
3. **Divine home.** The 2e-cited divine realm: "She only established a divine realm in the Outer Planes in the 1369." (`mielikki/wiki.txt:166`; brackets removed; refs F&A pp.57, 112 omitted). The 4e-cited home: "Following the Spellplague, by the late 15th century DR, Mielikki resided with Silvanus in his domain in the Deep Wilds in the World Axis cosmology." (`mielikki/wiki.txt:170`; brackets removed; refs FRPG p.154 and FRCG4e p.63 omitted). FRHoF plane: "The Beastlands (Krigala)" (`mielikki/5etools.md:5`). Edition-tagged; not identical.
4. **Shrine name and location.** The table says "Shrines of Nature" (`sources/adventure-wdh.json:30954`). The prose says "The Shrines to Nature, just a block away from the Tower of Luck" (`sources/adventure-wdh.json:30884`). The table places Tymora's Tower of Luck in the Castle Ward (`sources/adventure-wdh.json:30985`). The campaign gazetteer notes the conflict: "Tymora's Tower of Luck is placed in the Castle Ward by the Dragon Heist temple table and in the Sea Ward by its Sea Ward text and by the campaign's own Waterdeep outline, so it is not a Castle Ward temple here." (`campaign/gazetteer/waterdeep/castle-ward.md:165`)
5. **Jeryth's origin.** FRHoF: "a woman from Cormyr who now inhabits an expansive garden estate in Waterdeep as a disembodied spirit" (`mielikki/5etools.md:12`; the book tags are removed). WDH: "the Phaulkons (who are of Cormyrean descent)" (`sources/adventure-wdh.json:1320`). The wording differs: one says Jeryth is from Cormyr, the other says her family is of Cormyrean descent.
6. **Premise: "Mielikki is the Emerald Enclave's patron."** No campaign file says this. The campaign files say Jeryth is "patron of Phaulkonmere" (`campaign/setting/organizations/03-emerald-enclave.md:29`). The only source that ties Mielikki to the Enclave as a body is the wiki: "Many Harpers also followed Mielikki,<ref name="F&A-p113" /> as did most members of the Emerald Enclave.<ref>{{Cite book/Forgotten Realms Campaign Setting 3rd edition|273}}</ref>" (`mielikki/wiki.txt:221`; the citation is 3e, FRCS p.273).

**Not found**

- Areas of Concern: none.
- Edict or dogma: none (see Field 2).
- Waterdeep temples or shrines to Mielikki other than the Shrines of Nature and Phaulkonmere: none.
- Campaign holy days (Wild Ride, Greengrass, Midsummer) for Mielikki: none in campaign files.
- Other Chosen named in the campaign: none. Jeryth is the only one.
- Searched terms, campaign and both adventure JSON files: Mielikki; Lady of the Forest; Forest Queen; Our Lady; Jeryth; Phaulkon; Shrines of Nature; Shrines to Nature; unicorn; Lurue; Khalreshaar; Green Regent; Hornblade; Hartsong; Wild Ride; Feast of the Stags.

## Answers

**Q1. Which temples or shrines do the adventure or campaign files place in Waterdeep, and in which ward?**

- **Shrines of Nature, Sea Ward** (published adventure, Major Temples table; caption "Major Temples of Waterdeep" at `sources/adventure-wdh.json:30910`). Row cells:
  > `"Mielikki, Silvanus",` — `sources/adventure-wdh.json:30953`
  > `"Shrines of Nature",` — `sources/adventure-wdh.json:30954`
  > `"Sea Ward"` — `sources/adventure-wdh.json:30955`
  The prose places the shrines in the Sea Ward: "Two parks in the Sea Ward might also be worth your time." (`sources/adventure-wdh.json:30884`). See Field 7, conflict 4.
- **Phaulkonmere, Southern Ward** (a sanctuary and garden; no file calls it a temple or shrine): "Its Waterdeep presence centers on Phaulkonmere, an old estate and garden in the Southern Ward." (`campaign/setting/organizations/03-emerald-enclave.md:20`). Also: "Members of the Emerald Enclave can be found in Phaulkonmere, a noble villa in the Southern Ward" (`sources/adventure-wdh.json:1320`).
- **Current canon on Waterdeep:** "who now inhabits an expansive garden estate in Waterdeep as a disembodied spirit" (`mielikki/5etools.md:12`, FRHoF; the book tags are removed).
- Wiki: no Waterdeep shrine or temple (see Q3).

**Q2. Which campaign NPC, faction or quest uses this power?**

- **Jeryth Phaulkon** (Chosen of Mielikki; NPC). "**Featured in:** **Fireball!**, **Gralhund Villa**, **Faction Outposts**, **Xanathar's Lair**, **Cassalanter Villa**, **Sea Maidens Faire**, **Kolat Towers**, **Vault of Dragons**, **Emerald Enclave First Meeting**, **A Seat at Phaulkonmere**, **The Water Table Stirs**, **Summerstrider**, **Ten Nights in the City of the Dead**, **The Doppelganger Problem**, **The Grells in the Dock Ward**, **Autumnreaver**, **The Fouled Channel**, **Winterstalker**, **The Dreamer's Reach**, **Master of the Wild**" (`campaign/setting/notable-figures/emerald-enclave/02-jeryth-phaulkon.md:7`)
- **Emerald Enclave** (faction, which Jeryth leads): "**Featured in:** **Fireball!**, **Gralhund Villa**, **Xanathar's Lair**, **Cassalanter Villa**, **Vault of Dragons**" (`campaign/setting/organizations/03-emerald-enclave.md:8`)
- The Enclave's faction-event folders under `campaign/quests/faction-events/emerald-enclave/` name Jeryth. Their Mielikki-naming lines are listed under Cross-references.

**Q3. Which lines in wiki.txt mention Waterdeep?**

- `mielikki/wiki.txt:175`, citation only (Waterdeep and the North, p.10; the page does not otherwise discuss Waterdeep here): "Harpers held this to be obviously true and even made hazardous pilgrimages up the river." (citation: Waterdeep and the North p.10, then The Savage Frontier p.51)
- `mielikki/wiki.txt:207` (Jeryth; cites City of Splendors (boxed set), pp.9-10, by ref CoS-SotC-p9; the wiki does not state an edition): "One, in the late 14th century DR, was Lady Jeryth Phaulkon of Waterdeep, titled the Chosen Star of Mielikki, Our Lady's Champion, and even the Granddaughter of Silvanus." (brackets removed)
- `mielikki/wiki.txt:272` (citation only; Waterdeep (adventure) p.7): "During the ensuing Time of Troubles, Mielikki adapted well to avatar form and did not abandon her responsibilities, and since she already resided on the Prime Material plane, she suffered little." (the citation Waterdeep (adventure) p.7 sits between "responsibilities," and "and since"; brackets removed)
- `mielikki/wiki.txt:278` (Jeryth; cites CoS-SotC-p9; edition not stated): "In the 1367, Mielikki appeared in a dream to Jeryth Phaulkon, a noble of Waterdeep, and offered to make her her chosen."

## Cross-references (Mielikki)

Campaign lines naming Mielikki, not yet quoted above:

> "Jeryth speaks when the party reaches the oldest oak at the center of the garden. She is a Chosen of Mielikki who has lived as a disembodied presence in the gardens for several years, and she cannot be harmed. Her voice comes from the leaves, the gravel and the air together, and the branches move when she speaks, even on a windless day."
> — `campaign/quests/faction-events/emerald-enclave/00-first-meeting/ev-01-first-meeting.md:161`

> "Jeryth Phaulkon (Neutral Good, Chosen of Mielikki, disembodied presence, she/her) :: the patron of Phaulkonmere, who speaks rarely and means every word."
> — `campaign/quests/faction-events/emerald-enclave/00-first-meeting/ev-01-first-meeting.md:175`

> "Jeryth is Friendly toward the candidates, and she shows it through the garden. A warm breeze moves through the branches, flowers open along the path, and the grass lies flat where a candidate walks. She calls Mielikki "the Lady of the Forest" and never swears. If a player asks about the vault gold, she answers once with "That question is for the Lords to settle." and says nothing more on the subject."
> — `campaign/quests/faction-events/emerald-enclave/00-first-meeting/ev-01-first-meeting.md:177`

> "Jeryth Phaulkon (Neutral Good, Chosen of Mielikki, disembodied presence, she/her) :: the patron of Phaulkonmere, who speaks in two short sentences and lets the garden answer."
> — `campaign/quests/faction-events/emerald-enclave/m04-the-grells-in-the-dock-ward/ev-02-the-nest.md:150`

> "Jeryth is Friendly toward the party. A warm breeze moves through the branches, and the grass lies flat where a character who fought walks. She calls Mielikki "the Lady of the Forest" and never swears. She speaks only to those she has reason to address, and she does not repeat herself."
> — `campaign/quests/faction-events/emerald-enclave/m04-the-grells-in-the-dock-ward/ev-02-the-nest.md:152`

> "Jeryth Phaulkon (Neutral Good, Chosen of Mielikki, disembodied presence, she/her) :: the voice that speaks from the gardens of Phaulkonmere."
> — `campaign/quests/faction-events/emerald-enclave/r03-summerstrider/ev-01-summerstrider.md:126`

> "She speaks one or two short sentences at a time and never repeats them. Jeryth is Friendly and distant. The leaves move when she speaks, and the garden answers her with flowers and breezes. She never swears and takes no side in mortal politics. She calls Mielikki "the Lady of the Forest"."
> — `campaign/quests/faction-events/emerald-enclave/r03-summerstrider/ev-01-summerstrider.md:128`

> "Jeryth Phaulkon (Neutral Good, Chosen of Mielikki, disembodied presence, she/her) :: a disembodied presence in the gardens of Phaulkonmere, who casts through a sprig because she cannot leave them."
> — `campaign/quests/faction-events/emerald-enclave/r10-autumnreaver/ev-01-autumnreaver.md:97`

> "She speaks one or two short sentences at a time and never repeats them. Jeryth is Friendly and distant. The leaves move when she speaks, and the garden answers with a warm breeze. She never swears and takes no side in mortal politics. She calls Mielikki "the Lady of the Forest"."
> — `campaign/quests/faction-events/emerald-enclave/r10-autumnreaver/ev-01-autumnreaver.md:99`

> "Jeryth Phaulkon (Neutral Good, Chosen of Mielikki, disembodied presence, she/her) :: a disembodied presence in the gardens of Phaulkonmere, who casts through a sprig because she cannot leave them."
> — `campaign/quests/faction-events/emerald-enclave/r25-winterstalker/ev-01-winterstalker.md:159`

> "She speaks one or two short sentences at a time and never repeats them. Jeryth is Friendly and distant. The leaves move when she speaks, and the garden answers with a warm breeze. She never swears and takes no side in mortal politics. She calls Mielikki "the Lady of the Forest"."
> — `campaign/quests/faction-events/emerald-enclave/r25-winterstalker/ev-01-winterstalker.md:161`

> "Jeryth Phaulkon (Neutral Good, Chosen of Mielikki, disembodied presence, she/her) :: a disembodied presence in the gardens of Phaulkonmere, who has chosen to name the member before the whole Enclave."
> — `campaign/quests/faction-events/emerald-enclave/r50-master-of-the-wild/ev-01-master-of-the-wild.md:102`

> "She speaks one or two short sentences at a time and never repeats herself. Jeryth is Friendly and distant, and the garden answers with her through turning leaves, opening flowers and a warm breeze. She never swears and takes no side in mortal politics. She calls Mielikki "the Lady of the Forest"."
> — `campaign/quests/faction-events/emerald-enclave/r50-master-of-the-wild/ev-01-master-of-the-wild.md:104`

> "Jeryth Phaulkon (Neutral Good, Chosen of Mielikki, disembodied presence, she/her) :: the patron of Phaulkonmere, who has said what she meant to say and answers little more."
> — `campaign/quests/faction-events/emerald-enclave/s01-a-seat-at-phaulkonmere/ev-01-a-seat-at-phaulkonmere.md:135`

> "Jeryth is Friendly toward the member, and she shows it through the garden. Flowers open along the path, the grass lies flat where the member walks, and the leaves move when she speaks. She does not say "well done" or "you are welcome", because either one would suggest the member owes her something. She calls Mielikki "the Lady of the Forest" and never swears."
> — `campaign/quests/faction-events/emerald-enclave/s01-a-seat-at-phaulkonmere/ev-01-a-seat-at-phaulkonmere.md:137`

> "Jeryth Phaulkon (Neutral Good, Chosen of Mielikki, disembodied presence, she/her) :: the patron of Phaulkonmere. She speaks only to those she has reason to address, and she answers in one or two sentences."
> — `campaign/quests/faction-events/emerald-enclave/s02-the-water-table-stirs/ev-01-the-water-table-stirs.md:168`

> "Jeryth leaves long silences between her answers, and the garden answers with her. Leaves turn, and a cool wind crosses the path when she is troubled. She calls Mielikki "the Lady of the Forest", never swears and never repeats herself."
> — `campaign/quests/faction-events/emerald-enclave/s02-the-water-table-stirs/ev-01-the-water-table-stirs.md:170`

> "- *Disembodied presence, Neutral Good, Chosen of Mielikki, she/her*. Stat block: none (a disembodied presence, not a combatant)."
> — `campaign/setting/notable-figures/emerald-enclave/02-jeryth-phaulkon.md:5`

> "- **Affiliation:** Emerald Enclave (Chosen of Mielikki)"
> — `campaign/setting/notable-figures/emerald-enclave/02-jeryth-phaulkon.md:6`

> "**Persona.** To the world, Jeryth is a disembodied female voice heard by anyone in the Phaulkonmere gardens. Her voice comes from the leaves, the gravel and the air together, and the branches move when she speaks. To those she trusts, she is a noblewoman who became a Chosen of Mielikki and grants sanctuary, spells, and charms. Her approval shows in the garden, where flowers open and a warm breeze moves along the path. Deep down, she is disinterested in the dragon hoard. When asked about the gold, she answers once, "That question is for the Lords to settle," and says nothing more. Her real concern is something old and patient that she senses dreaming beneath the city, and she does not know its name."
> — `campaign/setting/notable-figures/emerald-enclave/02-jeryth-phaulkon.md:25`

> "**Secondary Contact:** Jeryth Phaulkon, the lady of the Phaulkonmere estate. She was a noblewoman before she became a Chosen of Mielikki, and for several years she has lived as a disembodied voice in the gardens. She cannot be harmed in this state, and she can cast any druid spell. She sends no one on missions, and the animals carry only Melannor's words."
> — `campaign/setting/organizations/03-emerald-enclave.md:24`

Published-adventure Jeryth and Phaulkon lines that do not name Mielikki:

> "Jeryth Phaulkon sends three {@creature swarm of rats||swarms of rats} to assist the characters. Once the characters are no longer in peril, the rats disperse throughout the vault."
> — `sources/adventure-wdh.json:14819`

> "Characters who are members of the Emerald Enclave can learn the location of {@creature Xanathar|WDH}'s lair by speaking with Jeryth Phaulkon at Phaulkonmere. Jeryth tells them that she has been sending {@creature awakened rat|wdh|awakened rats} into the sewers to find the beholder's lair, and that they recently discovered a secret staircase in the Castle Ward sewers leading down to it ({@area X1|271}). She has one of the awakened rats lead them there. This {@creature rat} has an Intelligence score of 10 and can speak Common."
> — `sources/adventure-wdh.json:15181`

Other Jeryth and Phaulkon lines in the published adventure (no Mielikki): `sources/adventure-wdh.json:165`, `:1327`, `:1328`, `:3690`, `:3700`, `:3713`, `:3718`, `:3750`.

Campaign lines naming Jeryth or Phaulkon but not Mielikki: 543 occurrences in 59 files. The largest are `campaign/quests/faction-events/emerald-enclave/s02-the-water-table-stirs/ev-01-the-water-table-stirs.md` (50), `00-first-meeting/ev-01-first-meeting.md` (42), `r50-master-of-the-wild/ev-01-master-of-the-wild.md` (36), `r10-autumnreaver/ev-01-autumnreaver.md` (34), `m05-the-fouled-channel/ev-01-the-fouled-channel.md` (29), `r25-winterstalker/ev-01-winterstalker.md` (28), `r03-summerstrider/ev-01-summerstrider.md` (27), `m06-the-dreamers-reach/ev-01-the-descent.md` (26), `campaign/guides/factions/04-emerald-enclave.md` (22), `campaign/setting/organizations/03-emerald-enclave.md` (14), and `campaign/setting/notable-figures/emerald-enclave/02-jeryth-phaulkon.md` (12). The full list is not copied, per the deviation in Conventions.

Unicorn and Lurue lines in campaign files (name Lurue, not Mielikki):

> "Floon's necklace, a holy symbol of Lurue worked as a unicorn bas-relief on a blue pearl chain, shed beads during the struggle outside Xoblob's shop. The beads are pale blue against dark stone; DC 13 Wisdom (Perception) to spot the trail on the cobblestones."
> — `campaign/quests/act-i/finding-floon/ev-02-dock-ward-investigation.md:73`

> "- **Floon's bead trail.** Floon's necklace — a holy symbol of Lurue, a unicorn bas-relief on a blue pearl chain — shed beads during the struggle outside Xoblob's. A DC 13 Wisdom (Perception) check spots the trail on the cobblestones; the beads are pale blue against dark stone and easy to miss in shadow. Following the trail leads directly to the mouth of Candle Lane and ends at the warehouse gate. If the party already knows about Candle Lane from another path, the trail still confirms which building."
> — `campaign/structure/arc-a-finding-floon.md:105` (structure doc; the quest journal line above supersedes it for content)

Published-adventure unicorn hits name the unicorn creature, the Sea Maidens Faire float, or a stuffed unicorn, not Mielikki. Counted as noise: `sources/adventure-wdh.json:13531`, `:13697`, `:13701`, `:20494`, `:20500`, `:20504`, `:25165`; `sources/adventure-wdmm.json:7128`, `:12575`, `:12580`, `:16197`.

Mielikki-relevant wiki lines for reference: `mielikki/wiki.txt:166`, `:168`, `:170`, `:186`, `:190`, `:192`, `:194`, `:196`, `:207`, `:221`, `:230`, `:274`, `:278`.

Mielikki-relevant bundle line (SCAG 2014): "Silvanus is sometimes thought of as her father and Eldath is considered her sister, but Mielikki walks her own path through the wilds." (`mielikki/5etools.md:31`)

## Not readable

None for Mielikki. Every file was readable.

---

# 2. SILVANUS

## Field 1. Identity

**5etools, FRHoF p.121**
> "## Silvanus | source FRHoF p.121 | pantheon Faerûnian"
> "- altNames: ['Oak Father', 'The Old Oak', 'Old Father Tree']"
> "- title: God of wild nature"
> "- worshipers: Barbarians, Druids, Rangers, wood elves"
> "- plane: The Outlands"
> — `silvanus/5etools.md:1-5`

**5etools, SCAG p.21 (2014; fallback)**
> "## Silvanus | source SCAG p.21 | pantheon Faerûnian"
> "- altNames: ['Oak Father', 'The Old Oak', 'Old Father Tree']"
> "- title: God of wild nature"
> "- alignment: ['N']"
> "- domains: ['Nature']"
> "- symbol: Oak leaf"
> — `silvanus/5etools.md:30-35`

**5etools, PHB p.298 (2014, Celtic pantheon entry; conflicts on symbol)**
> "## Silvanus | source PHB p.298 | pantheon Celtic"
> "- title: God of nature and forests"
> "- alignment: ['N']"
> "- domains: ['Nature']"
> "- symbol: Summer oak tree"
> — `silvanus/5etools.md:14-18`

**Wiki title row**
> "| title               = Oak Father<ref name="HoF-p121">{{Cite book/Forgotten Realms: Heroes of Faerûn|121}}</ref><ref name="SCAG5e-p21,37" /><ref name="FRCS-235" /><br />The Old Oak<ref name="HoF-p121"/><ref name="SCAG5e-p21,37" /><br />Old Father Tree<ref name="HoF-p121"/><ref name="SCAG5e-p21,37" /><br />The Forest Father<ref name="FRCS-235" /><ref name="FRCG4e-p76" /><ref name="FRPG-p153" /><br />Treefather<ref name="FRCS-235" /><br/>God of Wild Nature<ref name="cru-p30">{{Cite book/Crucible|30}}</ref><br />Green Father<ref name="PrayersFTF-p49">{{Cite book/Prayers from the Faithful|49}}</ref><ref name="TBK-p18">{{Cite book/The Border Kingdoms|18}}</ref>"
> — `silvanus/wiki.txt:12` (5e: HoF, SCAG; 3e: FRCS; 4e: FRCG4e)

**Wiki rows** (brackets removed)
> "| pantheon            = Celtic pantheon<br />Faerûnian pantheon" — `silvanus/wiki.txt:17`
> "| alignment5e         = Neutral" — `silvanus/wiki.txt:45`
> "| symbol5e            = Oak leaf" — `silvanus/wiki.txt:46`
> "| homeplane5eR        = The Outlands" — `silvanus/wiki.txt:32`

Areas of Concern: no field in any Silvanus entry.

## Field 2. Edict or core tenet (the creed)

> "Druids make up most of Silvanus's following. His creed dictates that nature's glory must be preserved not merely because nature is beautiful, but because wild nature is the true state of the world. {@skill Nature|XPHB} refreshes and revitalizes the mortal soul, giving breath to the world. His faithful oppose the expansion of settlements into wild places and consider the excessive consumption of natural resources to be not only wasteful but blasphemous."
> — `silvanus/5etools.md:10` (FRHoF)

> "Nature and its impartial fairness is central to the dogma of Silvanus's faith. His priests seek to know the total situation, to view the macrocosm; their viewpoint isn't confined to one person's or one nation's idea of what is best. The loss of a farming community to goblin raids is a tragedy for some, but the event provides an opportunity for the wilderness to grow up and make the land fertile again, which in turn provides new challenges for those who would return to tame it."
> — `silvanus/5etools.md:38` (SCAG 2014)

> "The creed of Silvanus dictates that nature's glory must be preserved not merely because nature is beautiful, but because wild nature is the true state of the world. Its expanses refresh and revitalize the mortal soul, and give breath to all the world. Many of his faithful oppose the expansion of settlements into wild places, and consider excessive consumption of natural resources to be not only wasteful but blasphemous."
> — `silvanus/5etools.md:39` (SCAG 2014)

> "When it came to nature itself, he cared greatly for maintaining a balance between growth and decay,<ref name="FRCG4e-p76">{{Cite book/Forgotten Realms Campaign Guide|76}}</ref><ref name="FRPG-p153">{{Cite book/Forgotten Realms Player's Guide|153}}</ref><ref name="FRCS-p251" /><ref name="FRCS.2e-p48" /><ref name="drag412-p23" /> water and drought, fire and ice<ref name="FRCS-p251" /><ref name="FRCS.2e-p48" /><ref name="drag412-p23" /> &mdash; the natural cycle of life.<ref name="FRCS-p251" /><ref name="FRCS.2e-p48" /><ref name="EGPEFR-p165">{{Cite book/Ed Greenwood Presents Elminster's Forgotten Realms|165}}</ref> This was considered to be his dogma<ref name="FRCS-p251" /><ref name="FRCS.2e-p48" /> and he was emotionally distant in regards to its necessity.<ref name="FRCS-p251" /> This led some to view him as heartless, though in reality he valued all life.<ref name="drag412-p23" />"
> — `silvanus/wiki.txt:144` (refs: 4e FRCG4e p.76 and FRPG p.153; 1e FRCS p.251; 2e FRCS.2e p.48; Dragon 412)

> "He had a special hatred for those who used fire carelessly or with deliberate intention to cause destruction.<ref name="drag412-p24">{{Cite dragon/412/Channel Divinity: Chauntea and Silvanus|24}}</ref><ref name="F&A-p146" />" (brackets removed)
> — `silvanus/wiki.txt:146`

## Field 3. Portfolio and Areas of Concern

> "Silvanus, god of wild nature, is closely associated with forests, mountains, and plains. In truth, Silvanus represents the entirety of nature: deserts as well as forests, sharks as much as deer. In legends he commands other nature deities, dealing out rewards and punishments to them as he sees fit."
> — `silvanus/5etools.md:7` (FRHoF)

> "Silvanus represents the entirety of nature, deserts as well as forests, sharks as much as deer. But folk in the North, who contend with the dangers of forests, mountains, and plains, see Silvanus more as a god of those places. Silvanus is thought of as a grim and severe father figure who metes out flood and drought, fire and ice, and life and death in the wilderness. In legends he often commands other nature deities, dealing out rewards and punishments to them as is fitting."
> — `silvanus/5etools.md:37` (SCAG 2014)

> "| portfolio5e         = Wild nature" — `silvanus/wiki.txt:51` (5e)

> "| portfolio3e         = Wild nature, Druids" — `silvanus/wiki.txt:81` (3e; brackets removed)

> "| portfolio2e         = Untamed nature, forests, druids" — `silvanus/wiki.txt:97` (2e; brackets removed)

## Field 4. Worship (Waterdeep first: see Q1)

> "The oak leaf is Silvanus's symbol, and villagers might dedicate a grove of oaks nearby as a shrine to him. In places where oak trees don't grow, an oak leaf etched into the bark of another kind of tree signifies a sacred site. Official temples to Silvanus are few and far between and likely to be hidden away in the depths of a forest rather than in a bustling urban center."
> — `silvanus/5etools.md:11` (FRHoF)

> "Silvanus tasks his Chosen with presiding over a forest, a desert, a lake, or another natural region. Some develop spiritual relationships with their assigned domain, not unlike a dryad's link to its sanctuary. When their domain flourishes, these Chosen become invigorated; when it suffers or comes under attack, they feel the pain."
> — `silvanus/5etools.md:12` (FRHoF)

> "When he needs to communicate directly with his followers, he sends a {@creature Dryad|XMM}, {@creature Treant|XMM}, or {@creature Twig Blight|XMM} as a divine messenger."
> — `silvanus/5etools.md:9` (FRHoF; messenger)

> "| holy days4e         = Greengrass<br />Midsummer<br />Highharvestide" — `silvanus/wiki.txt:71` (4e; brackets removed)

> "| holy days3e         = Greengrass, Midsummer night, Highharvestide, Night the Forest Walks" — `silvanus/wiki.txt:87` (3e; brackets removed)

> "| misc manifestations = An oak leaf blown out of nowhere<br />A fire-quenching, eerie green glow that's always accompanied by the sounds of faint whistling wind and running or dripping water" — `silvanus/wiki.txt:122` (omens; manifestation ref F&A p.146, 2e)

> "His clergy often worked together with the clergy of his allies, Mielikki and Eldath, towards common goals.<ref name="FRCS-p17">{{Cite book/Forgotten Realms Campaign Set/Cyclopedia of the Realms|17}}</ref><ref name="drag54-p55" /><ref name="EGPEFR-p145,154">{{Cite book/Ed Greenwood Presents Elminster's Forgotten Realms|145,154}}</ref> With the latter two being instructed to support, protect, and (if the need arose) obey the clergy of Silvanus.<ref name="EGPEFR-p145,154" />" (brackets removed)
> — `silvanus/wiki.txt:177` (refs 1e Cyclopedia p.17; Dragon 54; Elminster's Forgotten Realms)

## Field 5. Relations with other powers, and origin (edition tagged)

> "In the Faerûnian pantheon he was allied with and served by fellow non-evil deities of animals and nature.<ref name="FRCS-p251" /> Such as Eldath, Mielikki,<ref name="FRCS-p17" /><ref name="drag54-p55" /> and Shiallia.<ref>{{Cite book/Forgotten Realms Campaign Setting 2nd edition (revised)/Running the Realms|59}}</ref> The first viewed him as a father figure, but often found his robustness intimidating,<ref name="F&A-p57">{{Cite book/Faiths & Avatars|57}}</ref> while the second had crafted the banish blight spell partially as a gift to him.<ref name="F&A-p115">{{Cite book/Faiths & Avatars|115}}</ref>" (italic markup removed; the citations are as listed)
> — `silvanus/wiki.txt:167` (refs 1e Cyclopedia p.17; 2e Running the Realms p.59; F&A 2e)

> "| servedby2e          = Eldath and Mielikki" — `silvanus/wiki.txt:96` (2e row; brackets removed)

> "| servedby1e          = Eldath and Mielikki<ref name="FRCS-p17" />" — `silvanus/wiki.txt:110` (1e row; brackets removed)

> "| servedby4e          = Malar (exarch)" — `silvanus/wiki.txt:65` (4e row; brackets removed)

> "Other allies of Silvanus included Chauntea and Lathander<ref name="F&A-p47,90">{{Cite book/Faiths & Avatars|47,90}}</ref> &mdash; who he at times he would work with in their efforts against the Gods of Fury.<ref name="FRCS-p17" /><ref name="drag54-p55">{{Cite dragon/54/Down-to-earth divinity|55}}</ref> As well as Ki, nature goddess of the Untheric pantheon.<ref name="OHGp62">{{Cite book/On Hallowed Ground|62}}</ref>"
> — `silvanus/wiki.txt:169` (brackets removed; the text reads "who he at times he would work with" as written)

> "He was considered an enemy by Moander, Malar, Talona, and Talos.<ref name="F&A-p105,119,152,155">{{Cite book/Faiths & Avatars|105,119,152,155}}</ref> He actively opposed the latter three, as their love for destruction often upset the balance of nature.<ref name="FRCS-p251" /> After the events of the Spellplague, Malar became subject to Silvanus' rule as a resident of the Deep Wilds. Despite this, Silvanus did not rein in Malar.<ref name="AtRDT-p4">{{cite web |url=http://secretsofthearchmages.net/Threads/Wotc/2015/ForgottenRealms/1514971.htm|title=The one and only "Ask the Realms authors/designers thread" 4|accessmonthday=January 29th|accessyear=2017|author=[[Richard Baker]]|date=August 12th, 2008}}</ref>"
> — `silvanus/wiki.txt:171` (brackets removed; the web citation is kept as written)

> "Silvanus originated as a member of the Celtic pantheon.<ref name="OHG-p168">{{Cite book/On Hallowed Ground|168}}</ref><ref name="F&A-p105" />"
> — `silvanus/wiki.txt:182` (origin; On Hallowed Ground p.168, edition not stated; F&A p.105, 2e)

> "Around the time of the rise of Netheril,<ref name="P&P">{{Cite book/Powers & Pantheons|2,94}}</ref> a wave of planar immigrants came from another world<ref name="F&A-p105" /> and settled on Toril. One of these groups of people came from a rugged land with a culture tied to nature, the sea, and the warrior history of its dozen-king greater god." (brackets removed, display text used for piped links; the citations are as listed)
> — `silvanus/wiki.txt:184` (origin; refs Powers & Pantheons pp.2, 94; F&A p.105)

## Field 6. Campaign and published-adventure mentions

> "Two parks in the Sea Ward might also be worth your time. The Shrines to Nature, just a block away from the Tower of Luck, are resplendent gardens dedicated to nature gods like Mielikki and Silvanus. The park is closed to all except residents of the Sea Ward. Yet from beyond the iron fence that surrounds it, you can catch glimpses of the superb shrines, statues, and fountains within. The Heroes' Garden is the only green space in the city that is open to the public besides the City of the Dead, but it is tucked away so far to the north in the Sea Ward that it gets few visitors-which is a pity, since the fine statuary in this lush garden portrays many of the figures important to the city's history."
> — `sources/adventure-wdh.json:30884`

> `"Mielikki, Silvanus",` — `sources/adventure-wdh.json:30953` (Major Temples row; see Q1 for the rest of the row)

No campaign file names Silvanus. Searches are listed under Not found.

## Field 7. Conflicts between sources, and what was not found

**Conflicts**

1. **Symbol.** PHB p.298 gives "Summer oak tree" (`silvanus/5etools.md:18`). SCAG gives "Oak leaf" (`silvanus/5etools.md:35`). The wiki 5e row gives "Oak leaf" (`silvanus/wiki.txt:46`). The wiki 2e row gives "Green living oak leave<br/>Oak tree in summer<br/>Wooden staff sprouting buds and tiny green leaves" (`silvanus/wiki.txt:92`). The FRHoF entry has no symbol field.
2. **Pantheon.** FRHoF: "pantheon Faerûnian" (`silvanus/5etools.md:1`). PHB p.298: "pantheon Celtic" (`silvanus/5etools.md:14`). Wiki: "Celtic pantheon<br />Faerûnian pantheon" (`silvanus/wiki.txt:17`). These are different editions' placements, not one conflict.
3. **Plane.** FRHoF: "The Outlands" (`silvanus/5etools.md:5`). Wiki 3e row: "The House of Nature" (`silvanus/wiki.txt:77`). Wiki 1e row: "Concordant Opposition" (`silvanus/wiki.txt:107`). Edition-tagged.
4. **Alignment.** Wiki 4e row: "Unaligned" (`silvanus/wiki.txt:60`). Wiki 5e row: "Neutral" (`silvanus/wiki.txt:45`). SCAG: N (`silvanus/5etools.md:33`). Edition-tagged.

**Not found**

- Areas of Concern: none.
- Named Chosen: none in any source.
- Campaign files: no mention of Silvanus.
- Waterdeep temples or shrines other than the Shrines of Nature (Sea Ward): none.
- Searched terms, campaign and both adventure JSON files: Silvanus; Oak Father; Old Father; Forest Father; Old Oak; oak leaf; Shrines of Nature; Shrines to Nature. Only the two adventure lines above matched.

## Answers

**Q1. Waterdeep temples or shrines.**
- Shrines of Nature, Sea Ward: `sources/adventure-wdh.json:30953` ("Mielikki, Silvanus"), `:30954` ("Shrines of Nature"), `:30955` ("Sea Ward"). Prose: "The Shrines to Nature, just a block away from the Tower of Luck, are resplendent gardens dedicated to nature gods like Mielikki and Silvanus." (`sources/adventure-wdh.json:30884`).
- No campaign file places a Silvanus temple or shrine in any ward.

**Q2. Campaign NPC, faction or quest.** No campaign file uses this power.

**Q3. Waterdeep lines in wiki.txt.** None. No line of `silvanus/wiki.txt` mentions Waterdeep.

## Cross-references (Silvanus)

> "Official temples to Silvanus are few and far between and likely to be hidden away in the depths of a forest rather than in a bustling urban center." — `silvanus/5etools.md:11` (quoted in Field 4)

> "His worship was widespread across the east and south of Tethyr, especially in the Forest of Tethir,<ref>{{Cite book/Empires of the Sands|24}}</ref> in the Dalelands,<ref>{{Cite book/Forgotten Realms Campaign Setting 2nd edition (revised)/A Grand Tour of the Realms|31}}</ref> the Moonshae Isles, the Chondalwood of the Vilhon Reach, and the Yuirwood in Aglarond.<ref name="drag412-p23" />" (brackets removed) — `silvanus/wiki.txt:179` (worship geography; no Waterdeep)

Other Silvanus lines in the wiki: `silvanus/wiki.txt:12`, `:65`, `:71`, `:87`, `:96`, `:110`, `:122`, `:136`, `:140`.

## Not readable

None.

---

# 3. CHAUNTEA

## Field 1. Identity

**5etools, FRHoF p.104**
> "## Chauntea | source FRHoF p.104 | pantheon Faerûnian"
> "- altNames: ['The Grain Goddess', 'The Great Mother']"
> "- title: God of agriculture"
> "- worshipers: Farmers, gardeners, homesteaders"
> "- plane: Elysium (Eronia)"
> — `chauntea/5etools.md:1-5`

**5etools, PHB p.294 (2014)**
> "## Chauntea | source PHB p.294 | pantheon Forgotten Realms"
> "- title: Goddess of agriculture"
> "- alignment: ['N', 'G']"
> "- domains: ['Life']"
> "- symbol: Sheaf of grain or a blooming rose over grain"
> — `chauntea/5etools.md:18-22`

**5etools, SCAG p.21 (2014)**
> "## Chauntea | source SCAG p.21 | pantheon Faerûnian"
> "- altNames: ['The Great Mother', 'The Grain Goddess']"
> "- title: Goddess of agriculture"
> "- alignment: ['N', 'G']"
> "- domains: ['Life']"
> "- symbol: Sheaf of grain or a blooming rose over grain"
> — `chauntea/5etools.md:26-31`

**Wiki title row**
> "| title               = The Great Mother<ref name="HoF-p104">{{Cite book/Forgotten Realms: Heroes of Faerûn|104}}</ref><ref name="SCAG5e-p21,27" /><ref name="FRCS.CotR-p10">{{Cite book/Forgotten Realms Campaign Set/Cyclopedia of the Realms|10}}</ref><br /> The Grain Goddess<ref name="HoF-p104"/><ref name="SCAG5e-p21,27" /><ref name="FA-p47"/><br /> The Golden Goddess<ref name="Ne-TWoN-p37"/><br/>Goddess of Agriculture<ref name="NWNAOL">{{Cite game/Neverwinter Nights (AOL game)}}</ref><br /> Earthmother<ref name="Ne-TWoN-p37"/><br /> The Forest Mother<ref name="Ne-TWoN-p37"/><br /> She Who Shapes All<ref name="FA-p47">{{Cite book/Faiths & Avatars|47-48}}</ref><br /> Guardian of the Wilds and Deeps<ref name="Ne-TWoN-p37"/><br /> Keeper of the Wild<ref name="Ne-TWoN-p37" /><br/>Goddess of Bountiful Nature<ref name="cru-p30">{{Cite book/Crucible|30}}</ref><br/>The Mother of All Flowers<ref name="VGtD-p18">{{Cite book/Volo's Guide to the Dalelands|18}}</ref><br/>The Lady of the Harvest<ref name="UI-p8">{{Cite book/Under Illefarn|8}}</ref><br/>Grandmother ([[Uthgardt]])<ref name="TSF-pp11,21">{{Cite book/The Savage Frontier|11,21}}</ref>"
> — `chauntea/wiki.txt:8` (brackets removed)

**Wiki rows** (brackets removed)
> "| alignment5e         = Neutral good" — `chauntea/wiki.txt:40`
> "| alignment4e         = Lawful good" — `chauntea/wiki.txt:54` (4e; ref FRCG p.80)
> "| alignment3e         = Neutral good" — `chauntea/wiki.txt:69` (3e)
> "| symbol5e            = Sheaf of grain or a blooming rose over grain" — `chauntea/wiki.txt:41`
> "| domains5e           = Life" — `chauntea/wiki.txt:47`
> "| pantheon            = Faerûnian pantheon<br/>Netherese pantheon<br/>The First Circle" — `chauntea/wiki.txt:13`

Areas of Concern: none in any source.

## Field 2. Edict or core tenet

> "Chauntea's faith is one of nurturing and growth. Agricultural aphorisms and farming parables dot her teachings. Growing and reaping, the eternal cycle, is a common theme in the faith. Destruction for its own sake, or leveling without rebuilding, is anathema to her."
> — `chauntea/5etools.md:34` (SCAG 2014)

> "Chauntea's teachings are full of agricultural aphorisms and farming parables. Her faith teaches folk to nurture, tend, and plant wherever possible; anything torn down must have something new planted in its place. Temples of Chauntea are repositories of practical lore concerning farming and cultivation. Chauntea's priests work closely with rural communities to ensure plentiful harvests and are happy to roll up their sleeves and dig their hands into the dirt. They dress humbly, wearing shades of beige and muted green."
> — `chauntea/5etools.md:10` (FRHoF)

> "This relationship was not one-way however, for Chauntea also preached reverence towards nature. She urged the people of civilized lands to repair that which they damage,<ref name="FP-p18" /> calling her followers to perform small acts of devotion.<ref name="FA-p48" /> Furthermore, while she would prefer diplomacy to open conflict, to bring blight to the natural world would surely evoke the fury of the Earthmother.<ref name="FP-p18" />"
> — `chauntea/wiki.txt:136` (refs 3e Faiths and Pantheons p.18; 2e F&A p.48)

## Field 3. Portfolio and Areas of Concern

> "Chauntea is goddess of agriculture: sowing and reaping, seeding and harvest, breeding and butchery, shearing and weaving. In this aspect she is a rural deity rarely prayed to behind the walls of a city except by kitchen gardeners. But Chauntea is also the Great Mother, a goddess of crib, hearth, and home. And as such she is welcomed into all homes at mealtimes and at the birth of children, and folk give her thanks whenever they experience the pleasure of settling by a fire and feeling safe and loved."
> — `chauntea/5etools.md:33` (SCAG 2014)

> "| portfolio5e         = Agriculture" — `chauntea/wiki.txt:31` (5e)

> "| portfolio3e         = Agriculture <br /> Crops <br /> Farmers <br /> Gardeners <br /> Summer" — `chauntea/wiki.txt:75` (3e)

> "| portfolio2e         = Agriculture <br /> Crops <br /> Farmers <br /> Gardeners <br /> Summer" — `chauntea/wiki.txt:91` (2e)

## Field 4. Worship (Waterdeep first: see Q1)

> "Chauntea is the most widely worshiped god among Faerûn's common folk. As a god of agriculture, she is especially popular among farmers and rural communities. The hearth and home also fall under her purview, and as such, people in cities pray to her at mealtimes or before the birth of a child. Some say Chauntea blessed the world with life when it was first formed."
> — `chauntea/5etools.md:7` (FRHoF)

> "Some worshipers of Chauntea celebrate fertility festivals each {@book Greengrass|FRHoF|2|Greengrass}, wherein they arrange freshly cut flowers in beautiful arrangements as offerings for the god in exchange for a speedy growing season. Later in the year, folk across Faerûn express gratitude to Chauntea on the holiday of {@book Highharvestide|FRHoF|2|Highharvestide}, thanking her at sunset for the past year's plentiful bounty as winter approaches."
> — `chauntea/5etools.md:9` (FRHoF; holy days)

> "Grand spectacles and displays of power hold no interest to Chauntea. She prefers quiet and small acts of devotion. The Grain Goddess seldom appears directly to mortals, nor does she send divine messengers. On the rare occasions when she communicates with her followers, she does so through words scrawled on freshly tilled soil or the rustling sound of wind through crops, sounding faintly like whispered speech."
> — `chauntea/5etools.md:8` (FRHoF; messengers)

> "It's rare for Chauntea to select a Chosen, and it's even rarer to spot one. They usually dress and comport themselves no differently than any other member of her following."
> — `chauntea/5etools.md:11` (FRHoF; Chosen)

> "Seeds of Cultivation: The Seeds of Cultivation is a nomadic order of Chauntea dedicated to easing the pain of communities experiencing blight or famine. These worshipers travel wherever they are needed."
> — `chauntea/5etools.md:12` (FRHoF; the rest of the passage covers the crop spells, the recruiting rule and the brooch)

> "Her clergy were known for ministering in rural communities, and for their willingness to work in the community's fields next to the local farmers."
> — `chauntea/wiki.txt:154` (SCAG 2014 p.27; the same paragraph covers the wider worshipers, peasants and druids)

> "| misc manifestations = Unexpected flowers growing with great speed<br />Light motes" — `chauntea/wiki.txt:116` (omens; manifestation ref DD&D p.10)

## Field 5. Relations with other powers, and origin (edition tagged)

> "She had strong ties with other deities concerned with nature, such as Shiallia and Mielikki, and she shared a close relationship with Silvanus, but that diminished over time. She was also known to have romantic affiliations with Lathander.<ref name="FP-p18">{{Cite book/Faiths and Pantheons|18}}</ref><ref name="tymore5-6">{{Cite book/Tymora's Luck|5-6|1}}</ref>"
> — `chauntea/wiki.txt:145` (3e Faiths and Pantheons p.18; novel Tymora's Luck)

> "Her most despised enemy was Talona, the Lady of Pestilence, whose disposition to wreak suffering, disease and decay upon the natural world led her to oppose her with utmost vehemence. She was always in conflict with Talos. Chauntea battled deities who sought to desecrate and expunge nature; she opposed evil deities such as Malar and Bane, and viewed the latter's resurgence as portentous.<ref name="FP-p18" />"
> — `chauntea/wiki.txt:147` (3e Faiths and Pantheons p.18)

> "Chauntea was believed to be one of the eldest gods in Faerûn&mdash;she was born when Toril was created by the primeval battles between Shar and Selûne. Selûne favored her and nurtured her with her light, with the help of Mystryl.<ref name="FP-p17" />"
> — `chauntea/wiki.txt:170` (origin; 3e Faiths and Pantheons p.17; brackets removed)

> "Before her days as the Great Mother, she was known as Jannath, the Earthmother and in her early days, she frequented places of overgrown nature, wilderness, and packs of animals. In the Moonshae Isles, Chauntea was still worshiped as Jannath.<ref name="FP-p17" />"
> — `chauntea/wiki.txt:161` (origin; 3e Faiths and Pantheons p.17)

> "Following Malar's apparent death after the Spellplague, Chauntea leant her blessing to an effort by Argon Bael to revive the Beastlord in the late 15th century DR. Her motivations for willing his return remained unclear, but she indicated that her reasons were far beyond mortal conceptions of good or evil.<ref name="RoS-ch3">{{Cite digital book/The Rose of Sarifal/Kindle||3,6,9}}</ref>"
> — `chauntea/wiki.txt:172` (novel The Rose of Sarifal; brackets removed)

> "| servedby4e          = Sheela Peryroyl" — `chauntea/wiki.txt:59` (4e row; brackets removed)

> "| realm2e             = Great Mother's Garden" — `chauntea/wiki.txt:88` (2e row; brackets removed)

> "| realm4e             = Green Fields" — `chauntea/wiki.txt:57` (4e row; brackets removed)

## Field 6. Campaign and published-adventure mentions

No campaign file and no published-adventure line names Chauntea. The searches are listed under Not found.

## Field 7. Conflicts between sources, and what was not found

**Conflicts**

1. **Title and gender.** FRHoF: "- title: God of agriculture" (`chauntea/5etools.md:3`). PHB and SCAG: "- title: Goddess of agriculture" (`chauntea/5etools.md:19`, `:28`). Wiki gender row: "| gender              = Feminine" (`chauntea/wiki.txt:16`).
2. **Alignment.** Wiki 4e row: "Lawful good" (`chauntea/wiki.txt:54`). Wiki 5e row: "Neutral good" (`chauntea/wiki.txt:40`). SCAG: N, G (`chauntea/5etools.md:29`). Edition-tagged.
3. **Divine realm.** 2e: "Great Mother's Garden" (`chauntea/wiki.txt:88`). 4e: "Green Fields" (`chauntea/wiki.txt:57`). The wiki's Great Wheel passage places the 2e realm on Elysium's second layer of Eronia (`chauntea/wiki.txt:139`).

**Not found**

- Areas of Concern: none.
- Waterdeep: no Chauntea temple or shrine in the Major Temples table (`sources/adventure-wdh.json:30922-30996`). No campaign file places one.
- Campaign and published-adventure mentions: none.
- Searched terms, campaign and both adventure JSON files: Chauntea; Grain Goddess; Great Mother; Earthmother; Earth Mother; Seeds of Cultivation; Mother of All Flowers; Lady of the Harvest; Bhalla; Jannath. No hits.
- Wiki Waterdeep: none.

## Answers

**Q1.** No Chauntea temple or shrine in Waterdeep is named by any file. The Major Temples table has an "All deities" row that names no deity: `sources/adventure-wdh.json:30923` ("All deities"), `:30924` ("Holyhands House"), `:30925` ("North Ward"). The row is generic and does not name Chauntea.

**Q2.** No campaign file uses this power.

**Q3.** None. No line of `chauntea/wiki.txt` mentions Waterdeep.

## Cross-references (Chauntea)

- The wiki's Silvanus and Mielikki relation is at `chauntea/wiki.txt:145` (quoted in Field 5).
- Wiki line 154 cites "Sword Coast Adventurer's Guide|27". No other cross-reference.

## Not readable

None.

---

# 4. ELDATH

## Field 1. Identity

**5etools, FRHoF p.106**
> "## Eldath | source FRHoF p.106 | pantheon Faerûnian"
> "- altNames: ['The Guardian of Groves', 'The Quiet One', 'The Mother of the Waters']"
> "- title: God of peace"
> "- worshipers: Druids, pacifists, the dying"
> "- plane: Elysium (Eronia)"
> — `eldath/5etools.md:1-5`

**5etools, PHB p.294 (2014)**
> "## Eldath | source PHB p.294 | pantheon Forgotten Realms"
> "- title: Goddess of peace"
> "- alignment: ['N', 'G']"
> "- domains: ['Life', 'Nature', 'Peace']"
> "- symbol: Waterfall plunging into still pool"
> — `eldath/5etools.md:12-16`

**5etools, SCAG p.21 (2014)**
> "## Eldath | source SCAG p.21 | pantheon Faerûnian"
> "- altNames: ['The Quiet One', 'The Guardian of Groves', 'The Mother of the Waters']"
> "- title: Goddess of peace"
> "- alignment: ['N', 'G']"
> "- domains: ['Life', 'Nature', 'Peace']"
> "- symbol: Waterfall plunging into a still pool"
> — `eldath/5etools.md:20-25`

**Wiki title row**
> "| title               = Mother Guardian of Groves<ref name="SCAG5e-p21,28" /><ref name="F&P"/><br/>Mother of the Waters<ref name="HoF-p106">{{Cite book/Forgotten Realms: Heroes of Faerûn|106}}</ref><ref name="SCAG5e-p21,28" /><br />Goddess of Shining Waters<ref name="VR-PG-P7">{{Cite book/The Vilhon Reach/Player's Guide|7}}</ref><br />Goddess of Singing Waters<ref name="F&P"/><br/>The Green Goddess<ref name="F&P"/><br />The Quiet One<ref name="HoF-p106"/><ref name="SCAG5e-p21,28" /><br />Lady of Summer<ref name="GoS">{{Cite web/theedverse/2023-04-08 - Gods of summer}}</ref>"
> — `eldath/wiki.txt:7`

**Wiki rows**
> "| gender              = Feminine" — `eldath/wiki.txt:13`
> "| alignment5e         = Neutral good" — `eldath/wiki.txt:30`
> "| alignment3e         = Neutral good" — `eldath/wiki.txt:60`
> "| alignment1e         = Neutral" — `eldath/wiki.txt:89`
> "| pantheon            = Faerûnian pantheon" — `eldath/wiki.txt:11`

Areas of Concern: none in any source.

## Field 2. Edict or core tenet

> "Eldath's dogma was pacifistic, and her followers only resorted to violence in defense of themselves, of their friends and loved ones, and of pools and groves.<ref name="F&A-57" /> Worshipers of Eldath could be of any alignment, but priests were always non-evil.<ref name="F&A-57" /> Druids that followed the Mother of the Waters remained neutral, while her specialty priests sometimes leaned toward good.<ref name="F&A-59">{{Cite book/Faiths & Avatars|59}}</ref>"
> — `eldath/wiki.txt:144` (2e F&A pp.57, 59; the wiki's note at `mielikki/wiki.txt:192` calls F&A 2nd edition)

> "Most rural settlements have a pond or a glade that locals ascribe to Eldath. Tradition dictates that the site remain a place of quiet reflection. The body of water serves as a repository of offerings. Within a glade, people tie offerings to a bush or tree. Offerings are broken weapons or items associated with arguments, which the faithful discard while praying for peace. Many who favor Eldath are pacifists or people troubled by violence they have witnessed or experienced."
> — `eldath/5etools.md:8` (FRHoF)

> "Those who serve Eldath are happy to preside over peaceful negotiations and to certify treaties, but they can't force others to engage in harmony."
> — `eldath/5etools.md:29` (SCAG 2014; the rest of the passage covers the protection afforded by the taboo)

## Field 3. Portfolio and Areas of Concern

> "Eldath is a god of comfort, healing, stillness, and peaceful waters. She is thought to be present at waterfalls, springs, pools, and glades, particularly those visited by druids. Her blessed waters heal the sick, ease troubled minds, and comfort the dying. When she speaks to her followers, Eldath appears as a serene humanlike face formed from flowing water in a pool or waterfall, or she sends a {@creature Centaur Warden|XMM} or a {@creature Merfolk Wavebender|XMM} to deliver her instructions."
> — `eldath/5etools.md:7` (FRHoF)

> "Eldath is the goddess of waterfalls, springs, pools, stillness, peace, and quiet glades. She is thought to be present at many such places, particularly those that serve as druid groves. Eldath is a goddess of comfort, healing, and calm. Her blessed waters heal the sick, cure madness, and comfort the dying."
> — `eldath/5etools.md:27` (SCAG 2014)

> "| portfolio5eR        = Comfort, healing, stillness, peaceful waters" — `eldath/wiki.txt:21`

> "| portfolio5e         = Peace, waterfalls, springs, pools, stillness, quiet glades, summer" — `eldath/wiki.txt:36`

> "| portfolio1e         = Druid-groves, peace, pools, springs, stillness, streams, waterfalls" — `eldath/wiki.txt:95` (1e)

## Field 4. Worship (Waterdeep first: see Q1)

> "Eldath's priests don't organize into large sects. Instead they wander between holy sites and shrines, ensuring locations are cared for and that they remain places of sweet serenity. The faithful of Eldath are close to nature and allied to druids. It is taboo to strike a priest of Eldath, and killing one is said to bring great misfortune. Despite this protection, some priests of Eldath avoid conflict entirely, while others quickly step in to soothe strife and disharmony. Those who serve Eldath preside over peaceful negotiations and certify treaties. Eldath is served by the Yielding Way, an order of monks devoted to peace and protection, and by the Tall Trees, a circle of druids operating in the High Forest."
> — `eldath/5etools.md:9` (FRHoF)

> "Eldath's Chosen are known as Lotuses and wear a lotus blossom blessed never to wilt as long as they have Eldath's favor. Lotuses serve as ambassadors and mediators whose mere presence can extinguish violence and rage."
> — `eldath/5etools.md:10` (FRHoF)

> "Druids of Eldath prayed for their evocations once per day at a time selected after great personal reflection. The only calendar-related holy day of the church was the Greening, a gathering and festival celebrated at Greengrass. It was preceded by Firstflow, a festival held at varying times when the ice broke up and began to flow at the conclusion of winter.<ref name="F&A-58" />"
> — `eldath/wiki.txt:147` (2e F&A p.58)

> "| holy days3e         = The Greening (Greengrass)" — `eldath/wiki.txt:71` (3e; brackets removed)

> "| misc manifestations = Whispering winds<br />Green healing aura" — `eldath/wiki.txt:106` (omens; manifestation ref DD&D p.11)

> "Offerings to Eldath were typically weapons broken so they could never be used again, or an item that caused an argument and so had to be discarded to promote peace.<ref name="SCAG-p28" />"
> — `eldath/wiki.txt:149` (SCAG 2014 p.28)

> "Eldathyns were organized into a simplistic hierarchy, where priests reported to a local high priest responsible for a realm or larger region." — `eldath/wiki.txt:137` (F&A p.58; the rest of the passage covers the open-air shrines and the followers' location)

> "Her clergy often followed migratory patterns traveling from holy site to holy site in a local area." — `eldath/wiki.txt:139` (the rest of the passage covers the taboo on violence against priests and the allied local druids)

> "Many rural communities had a designated pond or glade which served as a holy site for local parishioners. These places were traditionally used as places to reflect and meditate." — `eldath/wiki.txt:154` (Temples; the rest of the passage covers the water repository)

## Field 5. Relations with other powers, and origin (edition tagged)

> "Eldath considered Mielikki a sister and together with her she served Silvanus loyally, even if she did find him at times intimidating. She had close relationships with Chauntea, Selûne, and Lathander, as they shared some common interests.<ref name="F&P" /> Eldath and Mielikki were said to directly bring retribution down on any who deliberately set fires in the High Forest.<ref name="SM-p27" />"
> — `eldath/wiki.txt:130` (brackets removed; refs Faiths and Pantheons (3e); Silver Marches)

> "Although Eldath was diametrically opposed to Tempus, the Lord of Battles, they were not enemies.<ref name="F&A-57" /> He thought she was naïve, but appreciated her convictions and punished any of his followers that harmed Eldath's faithful or desecrated her shrines and temples.<ref name="F&A-158">{{Cite book/Faiths & Avatars|158}}</ref>"
> — `eldath/wiki.txt:132` (brackets removed; 2e F&A pp.57, 158)

> "| serves2e            = Silvanus" — `eldath/wiki.txt:79` (2e row; brackets removed)

> "| serves1e            = Silvanus" — `eldath/wiki.txt:93` (1e row; brackets removed)

> "'''Eldath''' ({{Pronounce|EL|dæth|audio=Eldath.ogg|refs=<ref name="F&P">{{Cite book/Faiths and Pantheons|93}}</ref>}}), also known as the '''Mother of the Waters''' among the Bedine people,<ref name="Ana-p49">{{Cite book/Anauroch|49}}</ref>was a lake spirit<ref name="DR376-p65">{{Cite dragon/376/Realmslore: Sarifal|65}}</ref> who was often worshiped as a goddess of peace and calm waters.<ref name="F&P" /> The '''Mother Guardian of Groves''' was a mysterious deity that acted as a protector of copses and watersheds. The voice of the '''Green Goddess''' was heard in every babbling brook, her presence felt wherever there was calm.<ref name="F&A-57" />"
> — `eldath/wiki.txt:110` (origin; 3e Faiths and Pantheons p.93; Anauroch p.49; Dragon 376; F&A p.57)

> "Eldath's divine realm was called True Grove. In the Great Wheel cosmology, it was located in Eronia, in the second layer of Elysium.<ref name="PGF159">{{Cite book/Player's Guide to Faerûn|159}}</ref>" (brackets removed) — `eldath/wiki.txt:123` (Player's Guide to Faerûn p.159; the wiki's 3e rows cite the same book)

> "According to Bedine legend, the sun goddess At'ar was jealous of Eldath's beauty and imprisoned her at the oasis of Elah'zad in the Anauroch desert.<ref name="Ana-p49" /><ref name="F&A-58" /><ref name="PS-p224">{{Cite book/The Parched Sea|224}}</ref>" (brackets removed) — `eldath/wiki.txt:157` (Bedine legend; Anauroch p.49, edition not stated)

> "| homeplane3e         = House of Nature" — `eldath/wiki.txt:62` (3e row; see Field 7)

## Field 6. Campaign and published-adventure mentions

> "{@creature Avi|WDH} worships Eldath, god of peace, and uses his magic to quench hot steel. He is an expert armorsmith. {@creature Avi|WDH} is laid back and speaks plainly. He has the statistics of a {@creature priest}, with these changes:"
> — `sources/adventure-wdh.json:3406` (Avi, in the published adventure's Trollskull Alley text; Embric is at `sources/adventure-wdh.json:3398`)

> "Resonance. Avi should inspire comfort with her calm directness, endearment with the way she balances Embric's moods, and admiration with her quiet devotion to Eldath." — `campaign/setting/notable-figures/trollskull-community/03-avi.md:12` (bold label removed)

> "Motivations. Avi wants to craft armor that protects without encouraging violence, maintain peace in her marriage and her neighborhood, and honor Eldath through the discipline of her trade." — `campaign/setting/notable-figures/trollskull-community/03-avi.md:16` (bold label removed)

> "Relationships. Avi is the wife of Embric, a fellow member of the Splendid Order of Armorers, Locksmiths, and Finesmiths, and a worshipper of Eldath whose pacifism occasionally puts her at odds with adventuring customers." — `campaign/setting/notable-figures/trollskull-community/03-avi.md:26` (bold label removed)

> "**Featured in:** **Trollskull Alley**, **Fireball!**" — `campaign/setting/notable-figures/trollskull-community/03-avi.md:8`

> "**Steam and Steel** (Embric and Avi) — a forge, smoke rising from the chimney stack, hammer sounds inside. The back gate opens onto the same shared courtyard as the manor." — `campaign/quests/act-i/trollskull-alley/ev-01-welcome-to-trollskull-alley.md:24`

## Field 7. Conflicts between sources, and what was not found

**Conflicts**

1. **Title and gender.** FRHoF: "- title: God of peace" (`eldath/5etools.md:3`). PHB and SCAG: "- title: Goddess of peace" (`eldath/5etools.md:13`, `:22`). Wiki gender row: "| gender              = Feminine" (`eldath/wiki.txt:13`).
2. **Alignment.** Wiki 1e row: "Neutral" (`eldath/wiki.txt:89`). Wiki 3e and 5e rows: "Neutral good" (`eldath/wiki.txt:60`, `:30`). SCAG: N, G (`eldath/5etools.md:23`). Edition-tagged.
3. **Plane.** Wiki 3e row: "House of Nature" (`eldath/wiki.txt:62`). Wiki 5e row: "Elysium (Eronia)" (`eldath/wiki.txt:17`). FRHoF: "Elysium (Eronia)" (`eldath/5etools.md:5`). Edition-tagged.
4. **Symbol wording.** PHB: "Waterfall plunging into still pool" (`eldath/5etools.md:16`). SCAG: "Waterfall plunging into a still pool" (`eldath/5etools.md:25`). The wording differs by the article only.

**Not found**

- Areas of Concern: none.
- Waterdeep temple or shrine to Eldath: none. The Major Temples table has no Eldath row (`sources/adventure-wdh.json:30922-30996`), and no campaign file names one.
- Searched terms, campaign and both adventure JSON files: Eldath; Quiet One; Mother of the Waters; Guardian of Groves; Green Goddess; Lotus; Lotuses; Yielding Way; Tall Trees; Greening. Only the Avi lines above matched.
- Wiki Waterdeep: none.

## Answers

**Q1.** No Eldath temple or shrine in Waterdeep is named by any file. The Major Temples table has no Eldath row (`sources/adventure-wdh.json:30922-30996`).

**Q2.** Avi, a Trollskull community NPC who worships Eldath and works at Steam and Steel. "**Relationships.** Avi is the wife of Embric, a fellow member of the Splendid Order of Armorers, Locksmiths, and Finesmiths, and a worshipper of Eldath whose pacifism occasionally puts her at odds with adventuring customers." (`campaign/setting/notable-figures/trollskull-community/03-avi.md:26`). Also "**Featured in:** **Trollskull Alley**, **Fireball!**" (`campaign/setting/notable-figures/trollskull-community/03-avi.md:8`). No quest uses Eldath as a power.

**Q3.** None. No line of `eldath/wiki.txt` mentions Waterdeep.

## Cross-references (Eldath)

> "Avi wants to craft armor that protects without encouraging violence, maintain peace in her marriage and her neighborhood, and honor Eldath through the discipline of her trade." — `campaign/setting/notable-figures/trollskull-community/03-avi.md:16` (quoted in Field 6)

> "Avi crafts armor at Steam and Steel alongside her husband Embric; calm and precise where he is loud and impulsive, she is the neighbor who will listen without judgment and answer plainly." — `campaign/setting/notable-figures/trollskull-community/03-avi.md:30` (no Eldath mention; cited for Avi's location at Steam and Steel)

## Not readable

None.

---

# 5. MALAR

## Field 1. Identity

**5etools, FRHoF p.114**
> "## Malar | source FRHoF p.114 | pantheon Faerûnian"
> "- altNames: ['The Beastlord', 'The Bloodgod', 'The Wild Hunter']"
> "- title: God of the hunt"
> "- worshipers: Barbarians, hunters, lycanthropes"
> "- plane: Carceri (Colothys)"
> — `malar/5etools.md:1-5`

**5etools, PHB p.294 (2014)**
> "## Malar | source PHB p.294 | pantheon Forgotten Realms"
> "- title: God of the hunt"
> "- alignment: ['C', 'E']"
> "- domains: ['Nature']"
> "- symbol: Clawed paw"
> — `malar/5etools.md:13-17`

**5etools, SCAG p.21 (2014)**
> "## Malar | source SCAG p.21 | pantheon Faerûnian"
> "- altNames: ['The Beastlord', 'The Black-Blooded One']"
> "- title: God of the hunt"
> "- alignment: ['C', 'E']"
> "- domains: ['Nature']"
> "- symbol: Clawed paw"
> — `malar/5etools.md:21-26`

**Wiki title row**
> "| title               = The Beastlord<ref name="HoF-p114">{{Cite book/Forgotten Realms: Heroes of Faerûn|114}}</ref><ref name="SCAG5e-p21,33" /><br /> The Great Beast<ref name="FA3e-p113">{{Cite book/Faiths and Pantheons|113}}</ref><br /> The Beast of Beasts<ref name="FA3e-p113" /><br /> The Bloodgod<ref name="HoF-p114"/><ref name="FA3e-p113" /><br /> The Black-Blooded One<ref name="SCAG5e-p21,33" /><br /> The Wild Hunter<ref name="HoF-p114"/><ref name="F&A"/><br /> Master of the Hunt<ref name="EIotE">{{Cite book/Evermeet: Island of Elves}}</ref>"
> — `malar/wiki.txt:7`

**Wiki rows** (brackets removed)
> "| pantheon            = Faerûnian pantheon<br/>Gods of Fury" — `malar/wiki.txt:11`
> "| alignment5e         = Chaotic evil" — `malar/wiki.txt:34`
> "| alignment4e         = Evil" — `malar/wiki.txt:49` (4e)
> "| alignment2e         = Chaotic evil" — `malar/wiki.txt:80` (2e)
> "| homeplane5eR        = Carceri (Colothys)" — `malar/wiki.txt:21`

Areas of Concern: none in any source.

## Field 2. Edict or core tenet

> "Malarites believed that it was an honor to Malar to make one's killing bloody and long. His followers sometimes formed in bands, called "Hunts". While forbidden to slay the young or the pregnant, Hunts typically followed his dogma and evoked wanton slaughter in Malar's name.<ref name="FaA-106"/><ref name="FP3e-p43" /> They were opposed to the druidic concept of Balance, which they perceived as a threat to the savage rights of predators and hunters.<ref name="F&A" />"
> — `malar/wiki.txt:147` (under "Dogma"; refs F&A p.106 (2e), Faiths and Pantheons p.43 (3e))

> "Foolish mortals attempt to propitiate Malar with offerings or prayers, hoping to avoid attacks by wild animals. These efforts are in vain, for Malar shows no mercy. Those who worship him instead attempt to embody his peerless hunting skill. Berserkers scream prayers to Malar as they rage, and hunters whisper a prayer before closing in for the kill. Lycanthropes see themselves in Malar's uncontrollable savagery. Malar's followers wear or carry trinkets from the fearsome creatures they've slain. Teeth, pelts, wings, claws—the more ferocious, the better."
> — `malar/5etools.md:9` (FRHoF)

> "People believe that Malar can't be propitiated and knows no mercy, so he receives prayers only from those engaging in a hunt. Such supplicants pray to Malar for two reasons: to beg the aid of his peerless skill as a hunter, or to adopt his fearsome mantle and thus ward off other predators."
> — `malar/5etools.md:28` (SCAG 2014; the rest of the passage covers the hunt as the centre point between life and death)

## Field 3. Portfolio and Areas of Concern

> "Malar inspires the thrill of adrenaline experienced by a predator chasing its next meal. He epitomizes the bloody, sadistic side of nature, the world that is red in tooth and claw. He is the god of those who delight in the hunt, don't shy from bloodshed, and savor the fear of their prey."
> — `malar/5etools.md:7` (FRHoF)

> "| portfolio5e         = Hunt" — `malar/wiki.txt:40` (5e)

> "| portfolio3e         = Bloodlust <br /> Evil lycanthropes <br /> Hunters <br /> Marauding beasts and monsters <br /> Stalking" — `malar/wiki.txt:70` (3e; brackets removed)

> "| portfolio2e         = Hunters, marauding beasts and monsters, blood, bloodlust, evil lycanthropes, stalking" — `malar/wiki.txt:86` (2e; brackets removed)

> "| sphere4e            = Beasts" — `malar/wiki.txt:55` (4e)

## Field 4. Worship (Waterdeep first: see Q1)

> "Priests of Malar believe in the survival of the fittest, and none are allowed to enter the priesthood without first demonstrating prowess in hunting and combat. Malar has no temples in Faerûn's major cities, but villages on the edges of the wilderness might house a temple. During the tenday leading up to {@book Highharvestide|FRHoF|2|Highharvestide}, priests of Malar hunt tirelessly for as much game as they can find. They then invite members of the community to join them at a great feast on Highharvestide called the Feast of the Stags. They keep quiet the dreaded High Hunt ritual, in which priests of Malar choose someone to become their prey for a day and a night. If the prey survives, they gain a favor from the priests of Malar, but death is a far more likely outcome."
> — `malar/5etools.md:10` (FRHoF)

> "Malar's Chosen are gifted trackers, sometimes blessed with lycanthropy. It is said that the Chosen of Malar can smell their quarry from miles away."
> — `malar/5etools.md:11` (FRHoF)

> "When he needs to make his will known on the Material Plane, he sends a ferocious predator drenched in blood, such as a {@creature Displacer Beast|XMM}, an {@creature Owlbear|XMM}, or a {@creature Peryton|XMM}."
> — `malar/5etools.md:8` (FRHoF; messengers)

> "The "church" of Malar had no formal hierarchy. Instead, it revolved around the primal concept of the hunt. The most dominant figure within any group was known as the huntmaster, who held authority over the rest." — `malar/wiki.txt:142` (display text of the piped link is kept; the rest of the passage covers who may fill the huntmaster role)

> "The High Hunt ritual was a vicious hunt in which a captured humanoid was released, and for the next day and night attempted to escape the prowling worshipers of the Beastlord. If they managed to survive, they won their freedom as well as, perhaps, other things.<ref name="FaA-106">{{Cite book/Faiths & Avatars|106}}</ref>" (brackets removed) — `malar/wiki.txt:151` (2e F&A p.106)

> "The Feast of the Stags day made Malar's worship more tolerable in certain areas. For this event, all people were invited to partake of the bounty of the hunt, regardless of faith. At this time, priests of Malar chose some widows, orphans, elderly, or infirm citizens and promised to provide meat for their tables for the winter.<ref name="FP3e-p43" /><ref name="FaA-106" />" (brackets removed) — `malar/wiki.txt:153` (3e Faiths and Pantheons p.43; 2e F&A p.106)

> "Malarites were generally frowned upon by civilization, as they tended to wreak havoc in their wake." — `malar/wiki.txt:140` (the rest of the passage covers Cormyr, the wild-beast invocation and the roaming bands)

> "| misc manifestations = " — `malar/wiki.txt:111` (blank: the omens field is empty; the manifestation ref is HoF p.114, `malar/wiki.txt:112`)

## Field 5. Relations with other powers, and origin (edition tagged)

> "He was a member of the Gods of Fury led by Talos.<ref name="HoF-p123">{{Cite book/Forgotten Realms: Heroes of Faerûn|123}}</ref><ref name="F&A" /> Following the Spellplague, he was briefly believed to be dead<ref name="TRoS-ch2">{{Cite digital book/The Rose of Sarifal/Kindle||2}}</ref> and then served as an exarch of Silvanus<ref name="FRCG-p63">{{Cite book/Forgotten Realms Campaign Guide|63}}</ref> until after the Second Sundering, when he was once again a fully fledged deity and one of the gods of the First Circle.<ref name="SCAG5e-p126" />" (brackets removed)
> — `malar/wiki.txt:118` (HoF p.123 for the Talos link; Forgotten Realms Campaign Guide p.63 for exarch; SCAG 2014 p.126)

> "Malar was one of the Deities of Fury, led by Talos. He held a long-standing alliance with Lolth against the Seldarine, and is allied with other dark deities like Bane and Loviatar. He fought against deities of peace, civilization, and nature, but held particular hate for Nobanion for defeating him in a battle during the Time of Troubles." (brackets removed; no refs in the paragraph)
> — `malar/wiki.txt:129`

> "After the events of the Spellplague, Malar became subject to Silvanus' rule as a resident of the Deep Wilds. Despite this, Silvanus did not rein in Malar." (brackets removed; the web citation is kept as written in the file)
> — `malar/wiki.txt:136`

> "Following the Spellplague, Malar was much reduced,<ref name="FRCG-p63" /> and it was said that he had in fact been slain after being hunted down by his own beasts. This rendered him unable to affect anything but his followers' dreams, and to visit them in their nightmares." — `malar/wiki.txt:182` (Forgotten Realms Campaign Guide p.63; the rest of the paragraph covers Argon Bael and the revival)

> "It was not until the late 1470s DR that Bael successfully revived Malar, having arranged for the god's spirit and mind to return within the body of a cat-shifter named Kip with the approval of Malar's longtime enemy, Chauntea.<ref name="TRoS-ch9">{{Cite digital book/The Rose of Sarifal/Kindle||9}}</ref>{{TRoS-time}}" (brackets removed) — `malar/wiki.txt:182` (novel The Rose of Sarifal)

> "Malar was first created by Ed Greenwood, mentioned in the "Down-to-earth divinity" article of Dragon magazine #54 (October 1981, pg 52)." (brackets removed) — `malar/wiki.txt:187` (origin; the article date is 1981)

> "Malar was a minor deity not unique to Toril, a divine scavenger who foraged for worshipers among perhaps a hundred predatory races across an equally vast number of worlds.<ref name="EIotE"/>" — `malar/wiki.txt:140` (origin; Evermeet novel citation)

> "| servedby4e          = Malar (exarch)" — `silvanus/wiki.txt:65` (cross-entry: the 4e row on Silvanus; see Silvanus Field 5)

## Field 6. Campaign and published-adventure mentions

> "Nightal 11: Howldown" — `sources/adventure-wdh.json:31573` (the day's heading, in JSON field "name")

> "In honor of Malar, members of the City Guard leave the city in groups on this day to hunt down known threats to farmers and travelers, including brigands, {@creature wolf||wolves}, {@creature owlbear||owlbears}, {@creature ogre||ogres}, and trolls that haunt the roads and wilderness. These hunts typically last no longer than a tenday. During the same span of time, the City Watch engages in its own rigorous hunt for malefactors within the city walls. If you've any reason to doubt your standing in the eyes of the law, avoid Waterdeep for at least a tenday after Howldown."
> — `sources/adventure-wdh.json:31577`

> "With no real hunting to do of their own, the children of Waterdeep spend Howldown engaging in mock hunts of adults dressed up as monsters, and play at the killing of these predators."
> — `sources/adventure-wdh.json:31578`

> "South of {@creature Wyllow|WDMM}'s tower stands a large complex of ornate stone buildings that used to be home to a cult of Malar, the Beast Lord. {@creature Wyllow|WDMM} allowed these evil humans to hunt in her forest, but they abused the privilege—so the archdruid and her green dragon ally eradicated the cultists."
> — `sources/adventure-wdmm.json:13252` (inside "Level 5: Wyllowwood", `sources/adventure-wdmm.json:13173`)

> "20. Malar's Tabernacle" — `sources/adventure-wdmm.json:16019`

> "The cult of Malar would gather to worship here. The building's stone doors are fitted with locks, though they are unlocked at present. The building consists of one large, opulent room with the following features:"
> — `sources/adventure-wdmm.json:16024`

> "Whoever drops the chimera to 0 hit points gains inspiration—a minor blessing from the god Malar."
> — `sources/adventure-wdmm.json:16041`

> "Level 5: Wyllowwood" — `sources/adventure-wdmm.json:13173` (the level heading; "Level 6: Lost Level" begins at `sources/adventure-wdmm.json:16282`, so the tabernacle at line 16019 is in Level 5)

No campaign file names Malar.

## Field 7. Conflicts between sources, and what was not found

**Conflicts**

1. **Epithets.** FRHoF lists "The Bloodgod" (`malar/5etools.md:2`). SCAG lists "The Black-Blooded One" (`malar/5etools.md:22`). The wiki lists both (`malar/wiki.txt:7`). Not a factual conflict; both are epithets.
2. **Alignment.** FRHoF has no alignment field. PHB and SCAG give C, E (`malar/5etools.md:15`, `:24`). Wiki 5e row: "Chaotic evil" (`malar/wiki.txt:34`). Wiki 4e row: "Evil" (`malar/wiki.txt:49`). Edition-tagged.
3. **Rank.** Wiki 2e row: "Lesser deity" (`malar/wiki.txt:79`). Wiki 4e row: "Exarch" (`malar/wiki.txt:48`). Wiki: "served as an exarch of Silvanus" (`malar/wiki.txt:118`). Edition-tagged.
4. **Patron.** Wiki 5e row: "serves5eR = Talos" (`malar/wiki.txt:23`). Silvanus wiki 4e row: "Malar (exarch)" (`silvanus/wiki.txt:65`). Edition-tagged; not identical.
5. **Temples.** FRHoF: "Malar has no temples in Faerûn's major cities" (`malar/5etools.md:10`). The Undermountain tabernacle (`sources/adventure-wdmm.json:16019`) is not in a Faerûn city. Not a conflict, but the orchestrator should note it.
6. **Feast days.** FRHoF puts the Feast of the Stags at Highharvestide (`malar/5etools.md:10`). The published adventure puts Howldown on Nightal 11 (`sources/adventure-wdh.json:31573`). These are two different Malar days. The campaign calendar does not list Howldown: "Festival days. Five days fall between months and belong to neither. They are Midwinter, Greengrass, Midsummer, Highharvestide and the Feast of the Moon." (`campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:33`)

**Not found**

- Areas of Concern: none.
- Campaign files: no mention of Malar, the Beastlord, the Black-Blooded One, the High Hunt, the Feast of the Stags, or Howldown.
- Waterdeep temples or shrines to Malar: none. The Major Temples table has no Malar row (`sources/adventure-wdh.json:30922-30996`).
- Searched terms, campaign and both adventure JSON files: Malar; Beastlord; Beast Lord; Bloodgod; Wild Hunter; Black-Blooded; Feast of the Stags; High Hunt; Howldown. Campaign hits: none. Adventure hits: the lines above.

## Answers

**Q1. Waterdeep temples or shrines.** None in a ward. The Undermountain cult complex is on Level 5 of the dungeon beneath the city: "20. Malar's Tabernacle" (`sources/adventure-wdmm.json:16019`), inside "Level 5: Wyllowwood" (`sources/adventure-wdmm.json:13173`). The file does not give it a ward.

**Q2. Campaign NPC, faction or quest.** No campaign file uses this power. The published adventure's Howldown festival (`sources/adventure-wdh.json:31573`, `:31577`) is not in the campaign calendar.

**Q3. Waterdeep lines in wiki.txt.** One citation only: "* {{Cite dungeon/126/Vampires of Waterdeep: Blood of Malar}}" (`malar/wiki.txt:217`, under "===Further Reading===" at line 216). The wiki gives no Waterdeep fact for Malar.

## Cross-references (Malar)

Other WDMM lines that name Malar (all in Level 5, Wyllowwood, lines 13173 to 16282):

> "Four deep alcoves, each roughly 10 feet wide and 15 feet tall, line the cavern wall south of {@creature Wyllow|WDMM}'s tower. Strewn about in them are the skeletal remains of sixty humans clad in rotting clothes and furs—the remains of Malar worshipers killed by the green dragon's poison breath. {@creature Wyllow|WDMM} dragged the corpses here and left them to rot, as a dire warning to others who would betray her. A search of the bones reveals nothing of value." — `sources/adventure-wdmm.json:15514`

> "{@creature Mobar|WDMM}'s cave is unfurnished except for a moldy old wooden chest sitting on a natural shelf 10 feet off the floor in the room's southwest corner. The chest is unlocked and contains 60 gp in a leather pouch, three wooden holy symbols of Malar, a {@item Potion of Greater Healing||potion of greater healing } in a varnished gourd, a pair of dainty slippers, six bleached human skulls, a beautifully carved ivory figurine of {@creature Wyllow|WDMM} (25 gp), and a chalice hewn from blue quartz (250 gp). Hanging from a hook on the inside lid of the chest is an iron master key that fits all the doors in {@area areas 18|2f6|x}–{@area 24|31e}. The head of the key is shaped like a dwarf's stern visage." — `sources/adventure-wdmm.json:15749`

> "The chest at the east end of the cave contains a beaten copper tankard (10 gp), a crowbar, a set of manacles, a bar of soap, five wooden holy symbols of Malar, a shoddy cloak made from a brown bear's pelt, and ten bleached human skulls." — `sources/adventure-wdmm.json:15838`

> "This long, windowless stone building contains several apartments formerly occupied by high-ranking priests of Malar, god of the hunt. Stone doors throughout are fitted with locks, though they're unlocked at present. The building has various amenities (see the \"Lighting and Plumbing\"sidebar)." — `sources/adventure-wdmm.json:15871`

> "Heaped around the building are broken swords, dented helms, and torn metal armor. After the green dragon killed the cultists of Malar, {@creature Wyllow|WDMM} stripped the corpses of their metal gear, piled the offensive material here as a warning of sorts, and dragged the bodies to {@area area 7|2d2|x} to rot." — `sources/adventure-wdmm.json:15872`

> "The goblin werebats have thoroughly ransacked this room, where priests of Malar once displayed trophies of their hunts and meted out punishment to those who had failed them. The room contains the following:" — `sources/adventure-wdmm.json:15888`

> "Once the lodgings of the high priest of the cult of Malar, this apartment consists of a spacious bedroom and an equally impressive bathroom accessible from within." — `sources/adventure-wdmm.json:15922`

> "This windowless stone building contains apartments formerly used by rank-and-file Malar cultists. Stone doors throughout are fitted with locks, though the doors are unlocked at present. The building also has the features detailed in the \"Lighting and Plumbing\" sidebar." — `sources/adventure-wdmm.json:15978`

> "The cultists of Malar kept various beasts here under lock and key. None of the building's stone doors is currently locked, however. The building has lighting and plumbing (see the \"{@area Lighting and Plumbing|2f6|x}\" sidebar)." — `sources/adventure-wdmm.json:16227`

Other Malar lines in the wiki: `malar/wiki.txt:116`, `:118`, `:126`, `:129`, `:136`, `:140`, `:142`, `:147`, `:151`, `:153`, `:161`, `:173`, `:182`, `:187`, `:217`.

## Not readable

None.

---

# Files used

- Bundle (absolute root in Conventions): `mielikki/`, `silvanus/`, `chauntea/`, `eldath/`, `malar/` (`5etools.md`, `wiki.txt`, `campaign-hits.txt`, `adventure-hits.txt`).
- Repo, relative to `/home/user/waterdeep/`: `sources/adventure-wdh.json`, `sources/adventure-wdmm.json`, `campaign/setting/notable-figures/emerald-enclave/02-jeryth-phaulkon.md`, `campaign/setting/organizations/03-emerald-enclave.md`, `campaign/setting/notable-figures/trollskull-community/03-avi.md`, `campaign/quests/act-i/trollskull-alley/ev-01-welcome-to-trollskull-alley.md`, `campaign/quests/act-i/finding-floon/ev-02-dock-ward-investigation.md`, `campaign/structure/arc-a-finding-floon.md`, `campaign/gazetteer/waterdeep/castle-ward.md`, `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md`, `campaign/guides/factions/04-emerald-enclave.md`, and the folders under `campaign/quests/faction-events/emerald-enclave/`.
