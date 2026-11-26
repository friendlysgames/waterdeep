# Pass 6 research notes: Vajra Safahr, the Blackstaff

Page: `campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Vajra is a major NPC (brief ruling 2): full Personality and Connections apply.
Organization page: `campaign/setting/organizations/05-force-grey.md`
Factions Guide: `campaign/guides/factions/06-force-grey.md`
Voice profile: `.claude/skills/character-voices/voices/force-grey.md` (### Vajra Safahr, the Blackstaff, lines 5-19)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. `{@creature ...}` tags are left as written. The `page` field is given where the entry has one. Note that the Vajra entry is `page: 216` in the JSON (`:32667`), while the wiki's `WDH5e-p217` cites p.217.
- Wiki, the scratchpad extract `wiki-force-grey/01-vajra-safahr-the-blackstaff.txt` is **NOT FOUND** (the stub says so). The Vajra page was found in `sources/research/pass5-bundles/force-grey/wiki.txt`, "LINKED WIKI PAGE (first 5000 chars): Vajra Safahr" at lines 745 to 826. That extract is cut at 5000 characters: line 826 ends "She was kno". Cited below as "wiki line N" (that bundle's lines). The Force Grey page of the same bundle is cited as "wiki line N" too.
- Alexandrian Appendices B and D are markdown and quoted from the file. The Alexandrian PDF has no Force Grey page read for this note.
- Mechanics: `docs/plans/harpers-mechanics-reference.md` rows are quoted by line.
- No shell was available. `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **The page's "Stat block: **Archmage**" conflicts with the campaign's own mechanics record.** The mechanics reference lists "Vajra Safahr (WDH record)" at CR 13 (`harpers-mechanics-reference.md:587`), and the wiki gives CR 13 (wiki line 805). Only the Archmage reference block is CR 12 (`:586`). See B and D4.
2. **The alignment is settled as Lawful Neutral, but three Watch pages still say Neutral.** `castle-ward.md:259` records the user's Session 51 ruling. `city-watch.md:63`, `code-legal-and-magisters.md:45` and `guilds.md:48` still say "Neutral" (D1).
3. **Species and age conflict in the Alexandrian Appendix D.** It says "NG Calishite human" and "Late thirties" (`Appendix_D_-_Running_the_Tavern.md:1313`, `:1315`). The adventure says "mid-thirties" (`adventure-wdh.json:32679`). The wiki's birth year 1455 gives 37 in 1492 DR (wiki line 768) (D2, D3).
4. **The page's Relationships line (line 25) carries two quest-time items**: "The Splinter tried to kill me through a junior arcanist" (Smoke in the Tower) and the **Manshoon Named** gate on how she says the Splinter's name (C, row P-9 and P-10).
5. **The organization page's Draft Notes are stale about the page.** `05-force-grey.md:153` says the Notable Figures page "still reads 'how tired three years in the post have made her'." The current page reads "how young she is and how tired the post has made her" (`01-vajra-safahr-the-blackstaff.md:11`). The "three years" line is gone (D5).
6. **Voice sample line 17 is quest-like.** "Blackstaff here. Rogue construct, Castle Ward, two hours ago..." Its phrasing is not found in any quest file (C, row V-1).

---

## A. Background facts by theme

### A1. Origin, birth, family (wiki only; no campaign or adventure source)

**Wiki, infobox (ref `BST-p4`, Blackstaff Tower; no edition printed)**
> "| home           = [[Waterdeep]], [[Sword Coast North]]<ref name="Blackstaff Tower">{{Cite book/Blackstaff Tower}}</ref>
> | formerhomes    = [[Tethyr]], [[west Faerûn]]<ref name="BST-p247-251" />
> | sex            = Female
> | race           = [[Human]]
> | ethnicity      = [[Tethyrian]]<ref name="BST-p4">{{Cite book/Blackstaff Tower|4}}</ref>"
> — wiki line 758 to 762 (the `formerhomes` line is 759)

> "| dob            = 1455"
> — wiki line 768

> "| parents        = [[Tamik al Safahr]] and [[Parama yr Manshaka]]"
> — wiki line 776

The infobox `familyrefs` cite `BST-p247-251` (line 780). No sibling, spouse or child is named.

**Wiki, lead (refs `Blackstaff Tower`, `BST-p4`, `BST-p1`, `WoW`; no edition)**
> "'''Vajra Safahr''' ({{Pronounce|VAJ|rah|_|sah|FAR|refs=<ref name="WDH5e-p4">{{Cite book/Waterdeep: Dragon Heist|4}}</ref>}}) was the seventh [[Blackstaff]] of [[Waterdeep]], a title she ascended to in [[1479 DR]] when her mentor and lover, [[Samark Dhanzscul]], was killed.<ref name="Blackstaff Tower">{{Cite book/Blackstaff Tower}}</ref> She was quite young when she became the Blackstaff,<ref name="BST-p4">{{Cite book/Blackstaff Tower|4}}</ref><ref name="BST-p1">{{Cite book/Blackstaff Tower|1}}</ref> and was the youngest Blackstaff in Waterdeep's history.<ref name="WoW">{{Cite game/Warriors of Waterdeep}}</ref>"
> — wiki line 809

**Wiki, Description (refs `BST-p4`, `BST-p1`)**
> "Vajra was diminutive, standing under {{SI|5|ft|c|long=yes}},<ref name="Schend-tweet">...</ref> with olive skin, short black hair, and brown eyes.<ref name="BST-p4" /><ref name="BST-p1" /> However, for a time, she had the ability to change her eye color, and the color switched depending on which of the six previous Blackstaffs controlled her body at any given time.<ref name="Schend-tweet" />"
> — wiki line 812 (the tweet reference is a web source; the quote is cut at its ref name and the body is otherwise complete)

**Wiki, Personality (ref `WoW`, `DM-ch1`)**
> "Vajra loved an intriguing [[arcane]] challenge. She was patient and known to pursue multiple plans at once, often requiring her to get her rivals to act in her best interests instead of their own.<ref name="WoW" /> Although she was prone to self-doubt when she first assumed the role of the Blackstaff,<ref name="DM-ch1">{{Cite book/Death Masks||1}}</ref> she soon learned to ignore those doubts and to dismiss the envies of those who were skeptical of her role.<ref name="WoW" />"
> — wiki line 815

**Wiki, Activities (ref `WoW`)**
> "She was focused on turning Waterdeep, and specifically her [[Blackstaff Academy]], into the center of [[magical]] study in [[Faerûn]]. She would wander the libraries and laboratories of [[Blackstaff Tower]] under magical silence so as not to disturb the other wizards, save for when she made a sudden appearance to aid them in their studies. She allowed her best students access to her own personal [[spellbook]], and was said to even allow some of them to add their own creations to it.<ref name="WoW" />"
> — wiki line 818

**Wiki, Abilities (ref `Blackstaff Tower`)**
> "Though having become the Blackstaff at a young age, Vajra was a skilled wizard, even capable of casting a lone spell while entirely [[paralyze|paralyzed]], and thus incapable of performing verbal incantations or hand-gestures. The effect of this spell was to fire forth a few rays of amber-colored energy from her eyes.<ref name="Blackstaff Tower">{{Cite book/Blackstaff Tower}}</ref>"
> — wiki line 821

**Adventure, Vajra entry (page 216)**
> "{@creature Vajra Safahr|wdh|Vajra} is a capable wizard in her mid-thirties, the youngest person ever to hold the position of Blackstaff. As the High Wizard of Waterdeep, she is charged with using all the magic and resources at her disposal to defend the city against threats. She was handpicked for the job by Khelben Arunsun, and wields the Blackstaff from which Khelben derived his name and the title of the office. Vajra isn't the city's most powerful wizard, but she can hold her own. Despite her many gifts, she still questions her ability to meet the demands of her role, and she rarely makes a decision without first soliciting the advice of the Blackstaff, which contains Khelben Arunsun's spirit as well as the spirits of all the other Blackstaffs who preceded her. She also gets intelligence from many other sources, both through her own network of spies and from Harper agents."
> — `sources/adventure-wdh.json:32679` (entry "Vajra Safahr", page 216)

**Campaign, Force Grey organization page, History (the 1479 DR succession)**
> "- **1479 DR, Vajra takes the Blackstaff:** Vajra Safahr became the seventh Blackstaff when her mentor and lover, Samark Dhanzscul, was killed, and she is the youngest person ever to hold the title (Forgotten Realms Wiki, *Vajra Safahr*, edition not stated). `[research]` The published adventure puts her in her mid-thirties in 1492 DR, which makes her in her early twenties at the succession, and says Khelben Arunsun handpicked her (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/05-force-grey.md:27`

**Campaign, Castle Ward gazetteer (the 1479 DR date is tagged `[research]`)**
> "- The Blackstaff of Waterdeep, head of the Watchful Order, and the youngest Blackstaff ever, in the post since 1479 DR `[research]`. She sends orders by Sending, often in exactly 25 words."
> — `campaign/gazetteer/waterdeep/castle-ward.md:126`

### A2. Training and the staff

**Adventure (Laeral entry, page 205): the staff holds Khelben's soul**
> "Laeral's relationship with {@creature Vajra Safahr|WDH}, the current Blackstaff, has its challenges. For one thing, Laeral is much older, much wiser, and much more powerful than Vajra, whom she views as an insecure child. In addition, Vajra wields the Blackstaff, which has Khelben Arunsun's soul and the souls of all the other Blackstaffs bound inside it. Laeral covets the staff, because it contains all that's left of her husband. Not surprisingly, the two mages avoid each other as much as possible."
> — `sources/adventure-wdh.json:32205`

**Adventure, Laeral entry: marriage and Khelben**
> "Long ago, Laeral ruled a kingdom called Stornanter and held the title of Witch-Queen of the North. After that, she led a band of adventurers called the Nine. She met and married Khelben Arunsun, who would later become the Blackstaff, the Lord Mage of Waterdeep. After Khelben died, Laeral retired from public life. She resurfaced after the Spellplague and the Sundering, weakened by Mystra's death, rebirth, and withdrawal from the world."
> — `sources/adventure-wdh.json:32202`

**Wiki, the Blackstaffs list (ref `Blackstaff337-342`)**
> "The seventh Blackstaff was [[Vajra Safahr]]. The following were the Blackstaffs in order from earliest to latest:"
> — wiki line 255
> "A [[Chosen of Mystra]] and the original Blackstaff who created Blackstaff Tower, Khelben was almost a thousand years old when he sacrificed his life to raise Rhymanthiin, the Hidden City of Hope, on the [[Feast of the Moon]], [[1374 DR]].<ref name="Blackstaff337-342">{{Cite book/Blackstaff/MMP|337–342}}</ref> He was considered the greatest of the Blackstaffs.<ref>{{Cite book/Blackstaff Tower|?|22}}</ref>"
> — wiki line 257

**Wiki, heir custom**
> "Over time, it became customary for the Blackstaff to choose an heir,<ref>{{Cite book/Blackstaff Tower|?|22}}</ref><ref>{{Cite book/Blackstaff Tower|?|24}}</ref> called the '''Blackstaff's Heir'''.<ref>{{Cite book/Blackstaff Tower|?|Prologue}}</ref>"
> — wiki line 249

**Campaign, Force Grey organization page, Structure (The Blackstaff)**
> "**The Blackstaff:** \"Blackstaff\" began as a nickname for Khelben Arunsun because of his staff, and after his death it became the title of the master of Blackstaff Tower and of Waterdeep's archmage. Vajra is the seventh holder (Forgotten Realms Wiki, *Blackstaff*, edition not stated). The published adventure calls her the High Wizard of Waterdeep and says she rarely makes a decision without consulting the staff, which holds Khelben's spirit (*Dragon Heist*, 5e). The wiki says it became customary for each Blackstaff to choose an heir, and no campaign file names Vajra's. `[research]`"
> — `campaign/setting/organizations/05-force-grey.md:53`

### A3. The 1479 DR rescue and the Renaer and Meloon friendships

**Campaign, Force Grey organization page, History**
> "- **1479 DR, the rescue:** Renaer Neverember and Meloon Wardragon rescued Vajra from agents of Khondar Naomal. Meloon's page places the rescue more than a decade ago, and Renaer's page says it left the Blackstaff permanently in his debt (**Meloon Wardragon**; **Renaer Neverember**). The year itself is `[research]`."
> — `campaign/setting/organizations/05-force-grey.md:28`

**Campaign, Renaer Neverember page, Relationships**
> "**Relationships.** Renaer is the estranged son of Dagult Neverember (former Open Lord, current Lord of Neverwinter), the devoted friend of Floon Blagmaar, the closest living friend of Meloon Wardragon (whose changed behavior has him alarmed), a man who rescued Vajra Safahr from Khondar Naomal's agents and left the Blackstaff permanently in his debt, a Harper-adjacent ally of Mirt and Remi Haventree, and the leader of the Black Tears (his personal circle of trusted companions)."
> — `campaign/setting/notable-figures/independents-allies/02-renaer-neverember.md:25`

**Campaign, Meloon Wardragon page, Persona**
> "To those he trusts, he is the friend who shows up unprompted, who rescued Vajra alongside Renaer without being asked and never mentioned it again, who carries quiet grief for colleagues he has outlived."
> — `campaign/setting/notable-figures/independents-allies/05-meloon-wardragon.md:22`

**Campaign, Meloon Wardragon page, Relationships**
> "**Relationships.** Meloon is an active member of Force Grey (reporting to Vajra Safahr, whose life he saved more than a decade ago alongside Renaer), the closest friend of Renaer Neverember (whose growing unease, without knowing why, becomes alarm once the occupation takes hold),"
> — `campaign/setting/notable-figures/independents-allies/05-meloon-wardragon.md:26` (the sentence continues; the rest covers Bonnie, the devourer and the courier)

**Source of the 1479 DR rescue date (Patreon, per the findings note; `[research]`)**
> "Patreon Renaer guide: 1479 for the Blackstaff Tower rescue of Vajra (13 years before)."
> — `docs/plans/setting-compendium-research-notes/pass1-era4-era6.md:22`
> "- **Routed facts:** Renaer's 1479 DR rescue of Vajra at Blackstaff Tower (Patreon, per the findings note) belongs on **Renaer Neverember**."
> — `campaign/setting/history/06-the-open-lords-fall.md:164`

**Adventure, Force Grey entry (page 36)**: the rescue the adventure names is Renaer's, not Vajra's.
> "The Blackstaff, {@creature Vajra Safahr|WDH} (see {@adventure appendix B|WDH|12}), is friends with {@creature Renaer Neverember|wdh}, and word of his rescue quickly reaches her ears. She uses a {@spell sending} spell to deliver the following short message to one of the characters:"
> — `sources/adventure-wdh.json:3764`

### A4. Headquarters and the Watchful Order

**Adventure, Force Grey entry (page 37)**
> "Blackstaff Tower is a fortress and a wizard training academy all in one. From here, {@creature Vajra Safahr|WDH} watches over the city and asserts herself as Blackstaff. {@spell Sending} spells are her preferred way of communicating with her operatives."
> — `sources/adventure-wdh.json:3779`

**Adventure, Watch section (the Watchful Order)**
> "Arcane spellcasters who intend to stay in Waterdeep for any length of time are required to register with the city, and will be strongly encouraged to join the Watchful Order of Magists and Protectors, headed by the Blackstaff."
> — `sources/adventure-wdh.json:30578` (the text begins "Expect to be questioned at the gate..."; the sentence quoted is the last one of the entry)

**Adventure, Blackstaff Tower description (page 213 area)**
> "Blackstaff Tower is a squat black blot in the otherwise pretty ward. Humble though the edifice might be, looking at the place for too long can give you a queasy feeling and the sense that you are being watched-almost as if the tower itself has turned an unseen and wrathful eye upon you. Perhaps you think this fanciful. Well, go and try it yourself!"
> — `sources/adventure-wdh.json:31012`

**Campaign, Castle Ward gazetteer, Blackstaff Tower**
> "**Blackstaff Tower** — Wizard academy and fortress"
> — `campaign/gazetteer/waterdeep/castle-ward.md:60`
> "- Vajra Safahr, the Blackstaff, trains wizards here and heads the Watchful Order. Staring at the tower for long gives a queasy sense of being watched."
> — `campaign/gazetteer/waterdeep/castle-ward.md:61`

**Campaign, Force Grey organization page, Structure (Headquarters)**
> "**Headquarters:** Force Grey works out of Blackstaff Tower in the Castle Ward. Vajra also runs Blackstaff Academy there and heads the Watchful Order. The published adventure calls the Tower a fortress and a wizard training academy in one, and the Castle Ward gazetteer says that staring at it for long gives a queasy sense of being watched (*Dragon Heist*, 5e; **Castle Ward**). The wiki describes a black stone tower of three visible stories with at least a dozen more levels inside, some reachable only by magic (Forgotten Realms Wiki, *Blackstaff Tower*, citing the *Forgotten Realms Campaign Guide*, 4e)."
> — `campaign/setting/organizations/05-force-grey.md:57`

### A5. Tenure and the Force Grey timeline

**Campaign, Force Grey organization page, History (about 1489 DR)**
> "- **About 1489 DR, Laeral takes the seat:** The Masked Lords voted Dagult Neverember out and Laeral Silverhand became Open Lord, which made her the authority over Force Grey (**A City Watching Itself**). Her spies tell her that Vajra has secretly activated members and sent them on a number of unauthorized missions. Laeral has not confronted Vajra and excuses her silence as a test of Vajra's competence (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/05-force-grey.md:29`

**Campaign, Force Grey organization page, History (Ches 1, 1492 DR)**
> "- **Ches 1, 1492 DR, Force Grey today:** Vajra runs Blackstaff Academy and commands Force Grey from Blackstaff Tower, and the published adventure says she is always looking for new adventurers who bring unusual skills, abilities or spells (*Dragon Heist*, 5e). She knows that magical coercion is spreading among Waterdhavians in positions of influence and suspects a link to the gang war. She also knows that the Black Network has split, and she does not know that the Stone of Golorr has resurfaced or that four factions are competing for the vault (**Force Grey** in the Factions Guide)."
> — `campaign/setting/organizations/05-force-grey.md:31`

**Settled ruling (Session 51), Castle Ward gazetteer**
> "- **Settled by the user (Session 51):** Alignments follow canon. Savra Belabranta is Neutral Good (Dragon Heist `adventure-wdh.json:3949` and the wiki) and Vajra Safahr is Lawful Neutral (wiki, 5e). Saeth, Durnan and Mirt match the wiki."
> — `campaign/gazetteer/waterdeep/castle-ward.md:259`

**Settled ruling (Session 51), History 07**
> "> - **Settled by the user (Session 51):** Vajra's tenure. The campaign's \"three years in the post\" had no source and is dropped. The wiki has her take the Blackstaff's power at Samark Dhanzscul's death in 1479 DR (Blackstaff Tower, 4e) and gives no later date for her formal assumption, so the pages say \"since 1479 DR\" `[research]`. This page still gives no tenure."
> — `campaign/setting/history/07-a-city-watching-itself.md:132`

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Notable Figures page: "> - *Tethyrian human archmage, lawful neutral, she/her*. Stat block: **Archmage**." — `campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md:5`
- Castle Ward gazetteer: "**Vajra Safahr (Lawful Neutral, Tethyrian Human, she/her)**" — `campaign/gazetteer/waterdeep/castle-ward.md:125`
- Wiki: "| alignment5e    = [[Lawful neutral]]" — wiki line 804. Class and CR: "| challenge5e    = 13" (line 805) and "| class5e        = {{Class table|edition=5e|[[Wizard]]|18}}" (line 806); `refs5e` cites `WDH5e-p217` (line 807).
- Adventure: no alignment line in the Vajra entry (`sources/adventure-wdh.json:32666` to `:32684`).
- Alexandrian Appendix D (conflict, D1): "*Archmage — NG Calishite human; see Dragon Heist appendix B*" — `sources/Appendix_D_-_Running_the_Tavern.md:1313`
- Watch and Code pages (conflict, D1): "**Vajra Safahr** (Neutral, Tethyrian Human, she/her)" — `campaign/setting/governance-and-guilds/city-watch.md:63`

**Species and ethnicity**
- Notable Figures page and castle-ward: "Tethyrian Human" (`castle-ward.md:125`); Notable Figures page line 5 "Tethyrian human archmage".
- Wiki: "| race           = [[Human]]" (line 761); "| ethnicity      = [[Tethyrian]]<ref name="BST-p4">" (line 762).
- Adventure: no species line. Appendix D says "Calishite human" (`:1313`, D2).

**Pronouns**
- Notable Figures page: "she/her" (line 5). Adventure: "She was handpicked for the job by Khelben Arunsun" (`sources/adventure-wdh.json:32679`). Wiki: "| sex            = Female" (line 760).
- Campaign: "Vajra Safahr (Neutral, Tethyrian Human, she/her)" (`city-watch.md:63`).
- `docs/plans/npc-pronouns-table-group-b.md:16` gives "she/her" with the same reasoning.

**Stat block**
- Notable Figures page: "Stat block: **Archmage**." (line 5).
- Mechanics reference, Archmage row: "| Archmage (reference) | **Archmage** | 12 | XMM. Not used. |" (`docs/plans/harpers-mechanics-reference.md:586`)
- Mechanics reference, Vajra row: "| Vajra Safahr | **Vajra Safahr (WDH record)** | 13 | WDH p.217. Not used in a Harper fight. |" (`docs/plans/harpers-mechanics-reference.md:587`)
- Mechanics reference, verified list: "| Mirt, Remallia, Vajra | Verified (WDH records) | Mirt CR 9, AC 16, 153 HP; Remallia CR 9, no *Remove Curse*; Vajra CR 13. |" (`docs/plans/harpers-mechanics-reference.md:598`)
- Wiki: CR 13 and "Wizard 18" (wiki lines 805 and 806).
- Adventure: no CR, AC or HP in the Vajra entry. The mechanics reference's "WDH p.217" is not in the JSON (the JSON gives `page: 216`).

**Age**
- Adventure: "a capable wizard in her mid-thirties" (`sources/adventure-wdh.json:32679`).
- Appendix D: "**Appearance:** Late thirties. The Blackstaff (the actual staff) is always with her, and it is always watching." (`sources/Appendix_D_-_Running_the_Tavern.md:1315`)
- Wiki: "| dob            = 1455" (line 768); no age field is filled (line 764 is blank).

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md`. The page has no Background, Personality or Connections section yet.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| P-1 | L5 | "> - *Tethyrian human archmage, lawful neutral, she/her*. Stat block: **Archmage**." | Day-one name tag; stat block conflicts (B, D4) | section B |
| P-2 | L6 | "> - **Affiliation:** Force Grey (Blackstaff of Waterdeep)" | Day-one. Force Grey is the organization; the Blackstaff is public (see the status section) | `campaign/setting/organizations/05-force-grey.md:6`? (not in that file; the org summary is line 7: "Campaign role: Player faction." ) |
| P-3 | L7 | "> - **Featured in:** **Trollskull Alley**, **Fireball!**, **Gralhund Villa**, **Faction Outposts**, **Xanathar's Lair**, **Cassalanter Villa**, **Sea Maidens Faire**, **Kolat Towers**, **Vault of Dragons**, **Consulting Hlam**, **The Dragon in the Harbor**, **The Trouble with Meloon**, **Destroy the Intellect Factory**, **The Legate's Eyes**, **Smoke in the Tower**, **The Sleeping Asset**" | Quest-name list, not narrative (ruling 1) | `campaign/quests/faction-events/force-grey/`; `05-force-grey.md:10` |
| P-4 | L11 | "**Resonance.** Vajra should inspire respect for the weight she carries, discomfort with her refusal to perform warmth she does not feel, and sympathy when the party realizes how young she is and how tired the post has made her." | Day-one. Keep | `05-force-grey.md:12` |
| P-5 | L13 | "**Emotions.** Vajra most often feels burdened determination, impatient competence, defensive pride, controlled anger at threats to Waterdeep, dry humor that surfaces at unexpected moments, and private exhaustion she will not show." | Day-one. Keep | `adventure-wdh.json:32679` ("she still questions her ability"); wiki line 815 ("prone to self-doubt") |
| P-6 | L15 | "**Motivations.** Vajra wants to defend Waterdeep using Force Grey, prove that she earned the Blackstaff rather than inherited it, and outlast the senior wizards who consider her an upstart." | Day-one. Keep verbatim | `adventure-wdh.json:32681`? (no: the "upstart" line is `:32682`: "Several of the older and more seasoned wizards in Waterdeep consider Vajra an upstart, but they are smart enough not to challenge her.") |
| P-7 | L17 | "**Inspirations.** When playing Vajra, channel Ahsoka Tano (*Star Wars*), Jessica Pearson (*Suits*), and Satsuki Kiryuin (*Kill la Kill*)." | Not a fact. Keep | n/a |
| P-8 | L21 | "**Persona.** To the world, Vajra is the Blackstaff, commander of Force Grey, who communicates by Sending (often exactly 25 words) and does not perform warmth. To those she trusts, she cares about Waterdeep and the people in it, and her years as the youngest Blackstaff ever have worn her down. Deep down, she wields a staff containing Khelben Arunsun's soul, and Laeral Silverhand views her as an insecure child holding her dead husband's weapon. She does not find observations about her youth interesting." | Day-one. "her years as the youngest Blackstaff ever have worn her down" is a state, not an event | `05-force-grey.md:12`; `adventure-wdh.json:32205` |
| P-9 | L23 | "**Morale.** In a fight, Vajra would open with something large enough to end the conversation. She explains herself afterward to exactly no one." | Day-one trait. The fight-opening habit is also in `06-force-grey.md:73` | `campaign/guides/factions/06-force-grey.md:73` |
| P-10 | L25 | "**Relationships.** Vajra is the Blackstaff of Waterdeep, the commander of Force Grey, the wielder of a staff containing Khelben Arunsun's soul, and a strained subordinate of Laeral Silverhand. She has rare, dry humor, which she delivers flat: \"The Splinter tried to kill me through a junior arcanist. That's either an insult or a compliment. I haven't decided.\" She says \"the Splinter\" until **Manshoon Named** is marked for the party member she is speaking to, and only then says his name." | **Quest-time** in two places: (a) the junior-arcanist attack is the **Smoke in the Tower** attack; (b) the **Manshoon Named** Event Outcome gate. The first clause (Blackstaff, commander, staff, subordinate) is day-one | (a) `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/overview.md:21` ("Six weeks ago the Splinter placed Vira Solkan in Blackstaff Tower as a junior arcanist ... She hid a resonance disruptor in a hollowed book..."); `m06-smoke-in-the-tower/ev-01-smoke-in-the-tower.md:17`. (b) `campaign/guides/factions/06-force-grey.md:11`; `m06-.../ev-01-smoke-in-the-tower.md:22` ("Until then Vajra says \"the Splinter\" and \"the other cell\"."); `00-first-meeting/ev-01-first-meeting.md:25` |
| P-11 | L27-29 | "## Overview" / "The Blackstaff of Waterdeep and commander of Force Grey, who communicates by *Sending* and manages the city's arcane defense with impatient competence, declining to perform warmth she does not feel." | Day-one. 26 words (within the 21-word limit? No: 26 words, re-draft) | `05-force-grey.md:16` |

**Quest-time clauses in the voice profile (`.claude/skills/character-voices/voices/force-grey.md`, "### Vajra Safahr, the Blackstaff", lines 5-19)**

- V-1 (line 17, Greeting, Sending): "Blackstaff here. Rogue construct, Castle Ward, two hours ago. You are closest. Contain it, do not destroy it. Report to Blackstaff Tower by dusk tonight." — **quest-time-like**. The exact phrase "Rogue construct" is not in any quest file (case-insensitive search of `campaign/`). Closest quest sendings: `campaign/quests/faction-events/force-grey/s01-the-full-picture/ev-01-the-full-picture.md:36` ("Blackstaff here. The Tower holds Watch reports of unexplained trouble in three wards. Come at dusk. Bring everything you know, and anyone who helped you.") and `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:81` ("Blackstaff here. Bronze dragon, Deepwater Harbor, outside the Dragonward. Intentions unknown. Come to the Tower now. Bring your people. Assess it, do not provoke it."). Restate as generic or as a day-one sending.
- V-2 (line 11, Swearing): "I have not slept in two days, and some shit-brained cultist just opened a portal." — a sample line. The phrase "just opened a portal" is in no quest file. The swearing register is the point; the event is a sample. Consider a day-one version.
- V-3 (line 18, Business): "I need it done quietly and I need it done tonight. Can you do that, or do I send someone who can?" — generic.
- V-4 (line 19, Under pressure): "Down! Stay down. I've got it. I said I've got it." — generic.
- V-5 (line 12, Personality in speech): "Burdened determination and defensive pride. Comments about her youth earn a cold stare and a subject change. Her dry humour surfaces unexpectedly, delivered deadpan. Exhaustion shows in shortened sentences, never in complaint." — day-one.
- V-6 (line 13, Quirks): "She counts Sending words on her fingers. She answers \"Are you alright?\" with \"Irrelevant.\"" — day-one.
- V-7 (line 14, Signature phrases): "\"Irrelevant.\" / \"Force Grey will handle it.\" / \"Next.\"" — day-one.
- V-8 (line 15, Never): "She never discusses what's in the Blackstaff, never asks for sympathy, and never lets anyone see her doubt herself." — day-one.
- V-9 (line 10, Word choice): "She calls Laeral \"the Open Lord\", precisely, and never mentions Khelben. She calls wizards who doubt her by their surnames." — day-one. (The "never mentions Khelben" rule is a habit, not an event.)

---

## D. Conflicts

**D1. Alignment (Lawful Neutral, Neutral, or Neutral Good)**
- Notable Figures page: "> - *Tethyrian human archmage, lawful neutral, she/her*. Stat block: **Archmage**." — `campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md:5`
- Castle Ward, settled: "- **Settled by the user (Session 51):** Alignments follow canon. ... Vajra Safahr is Lawful Neutral (wiki, 5e)." — `campaign/gazetteer/waterdeep/castle-ward.md:259`
- Castle Ward, Vajra entry: "**Vajra Safahr (Lawful Neutral, Tethyrian Human, she/her)**" — `castle-ward.md:125`
- Wiki: "| alignment5e    = [[Lawful neutral]]" — wiki line 804.
- Watch page: "**Vajra Safahr** (Neutral, Tethyrian Human, she/her) is the Blackstaff and, by the published adventure, the head of the Watchful Order." — `campaign/setting/governance-and-guilds/city-watch.md:63` (stale against the settled ruling).
- Code and Legal page: "**Vajra Safahr** (Neutral, Tethyrian Human, she/her) is the Blackstaff, and the published adventure says the Watchful Order is headed by the Blackstaff." — `campaign/setting/governance-and-guilds/code-legal-and-magisters.md:45` (stale).
- Guilds page: "**Vajra Safahr** (Neutral, Tethyrian Human, she/her) is the Blackstaff, and the published adventure says the Watchful Order is headed by the Blackstaff." — `campaign/setting/governance-and-guilds/guilds.md:48` (stale).
- Appendix D: "*Archmage — NG Calishite human; see Dragon Heist appendix B*" — `sources/Appendix_D_-_Running_the_Tavern.md:1313` (the Alexandrian text is an outlier on both alignment and species).
- Higher rank: the Session 51 user ruling (`castle-ward.md:259`) and the wiki (line 804). The three Watch and Guild pages are stale and are not edited here.

**D2. Species and birthplace (Calishite or Tethyrian)**
- Appendix D: "*Archmage — NG Calishite human; see Dragon Heist appendix B*" — `sources/Appendix_D_-_Running_the_Tavern.md:1313`
- Notable Figures page and castle-ward, wiki: "Tethyrian" (`01-vajra-safahr-the-blackstaff.md:5`; `castle-ward.md:125`; wiki line 762 "| ethnicity      = [[Tethyrian]]").
- Higher rank: ruling 5 (Faerûn ethnicity, Tethyrian). The Alexandrian "Calishite" is an outlier. Drafter: Tethyrian human.

**D3. Age (mid-thirties, late thirties, or dob 1455)**
- Adventure: "a capable wizard in her mid-thirties" (`sources/adventure-wdh.json:32679`)
- Appendix D: "**Appearance:** Late thirties." (`sources/Appendix_D_-_Running_the_Tavern.md:1315`)
- Wiki: "| dob            = 1455" (line 768). In 1492 DR that is 37, which is "late thirties" in the Appendix D's sense and past the adventure's "mid-thirties" (the adventure's phrase is the wording the campaign uses).
- Force Grey org page: "The published adventure puts her in her mid-thirties in 1492 DR, which makes her in her early twenties at the succession" (`05-force-grey.md:27`). The wiki's 1455 DR birth year puts her at 24 at the 1479 DR succession, which is "early twenties" only loosely.
- Higher rank: the adventure (mid-thirties) for the page's wording; the wiki's birth year is `[research]`. Do not state an exact age.

**D4. Stat block (Archmage or WDH record CR 13)**
- Notable Figures page: "Stat block: **Archmage**." — `01-vajra-safahr-the-blackstaff.md:5`
- Mechanics reference: "| Vajra Safahr | **Vajra Safahr (WDH record)** | 13 | WDH p.217. Not used in a Harper fight. |" — `docs/plans/harpers-mechanics-reference.md:587`; "| Archmage (reference) | **Archmage** | 12 | XMM. Not used. |" — `:586`
- Wiki: "| challenge5e    = 13" — wiki line 805.
- Higher rank: the mechanics reference and the wiki agree on CR 13 for the WDH record. The Notable Figures "Archmage" is a label (the XMM Archmage is CR 12). The drafter should not put a stat line on the page without the orchestrator's decision.

**D5. Tenure (the "three years" line)**
- Organization page: "Her Notable Figures page (`01-vajra-safahr-the-blackstaff.md:11`) still reads \"how tired three years in the post have made her\"" — quoted in `campaign/setting/organizations/05-force-grey.md:153`.
- Current Notable Figures page, line 11: "**Resonance.** Vajra should inspire respect for the weight she carries, discomfort with her refusal to perform warmth she does not feel, and sympathy when the party realizes how young she is and how tired the post has made her." — `campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md:11`. The phrase "three years" is no longer on the page (a search for "three years" in the page returned no match).
- Higher rank: the current page (line 11) has already dropped "three years", per the Session 51 ruling (`history/07-a-city-watching-itself.md:132`). The organization page's Draft Notes at `05-force-grey.md:153` are stale.

**D6. Khelben's death and the handpicking**
- Wiki: "Khelben was almost a thousand years old when he sacrificed his life to raise Rhymanthiin, the Hidden City of Hope, on the [[Feast of the Moon]], [[1374 DR]]." — wiki line 257
- Adventure: "She was handpicked for the job by Khelben Arunsun" — `sources/adventure-wdh.json:32679`
- Wiki: Vajra "became the Blackstaff" in 1479 DR (wiki line 809).
- Conflict: Khelben's death in 1374 DR (wiki) cannot be the same man who handpicked a woman who took the title in 1479 DR (wiki) unless the handpicking came before 1374 DR. The campaign's Force Grey organization page says so in Draft Notes: "The wiki also dates Khelben's death to 1374 DR, while the published adventure says Khelben handpicked Vajra (`adventure-wdh.json:32679`) for a title she took in 1479 DR. The page states both and does not reconcile them." — `campaign/setting/organizations/05-force-grey.md:162`
- Higher rank: the adventure's "handpicked" line is the published statement, and the wiki's death date is wiki-only. The campaign's Notable Figures page does not give a death date for Khelben. Drafter: say Khelben is dead and his soul is in the staff; do not give a date.

**D7. Staff contents: Khelben's soul, or green-tinged facsimiles**
- Notable Figures page: "Deep down, she wields a staff containing Khelben Arunsun's soul" — `01-vajra-safahr-the-blackstaff.md:21`
- Adventure: "which has Khelben Arunsun's soul and the souls of all the other Blackstaffs bound inside it" — `sources/adventure-wdh.json:32205`
- Wiki: the wiki says the tower's spirits are "green-tinged facsimiles" (per `05-force-grey.md:162`'s note at `wiki.txt:251`). That line is in the Force Grey bundle at `sources/research/pass5-bundles/force-grey/wiki.txt:251`; quote it there before use.
- Higher rank: the adventure and the campaign agree (soul). The wiki line is not used.

**D8. Force Grey dismantled (1491 DR) or continuously active**
- Wiki: "By the {{YearlinkName|1491}}, Force Grey had been dismantled for some time. [[Mirt|Mirt the Moneylender]] and Lady Lord [[Laeral Silverhand]] contemplated reestablishing the organization to aid her leadership of the City of Splendors." — wiki line 87
- Campaign, Meloon: "Meloon is an active member of Force Grey (reporting to Vajra Safahr, whose life he saved more than a decade ago alongside Renaer)" — `05-meloon-wardragon.md:26`
- Higher rank: the campaign (`05-force-grey.md:30` says "no campaign file records a dismantling"; the org page treats Force Grey as one continuous body). Drafter: no dismantling.

**D9. The Gray Hands: the entry tier or the whole cadre**
- Wiki: "Force Grey, otherwise known as the Gray Hands" (quoted in `05-force-grey.md:158`; `wiki.txt:51`).
- Adventure: "To join Force Grey, one must first become a member of the Gray Hands." — `sources/adventure-wdh.json:1339`
- Campaign: "**The Gray Hands:** The Gray Hands is the entry tier of Force Grey." — `05-force-grey.md:55`
- Higher rank: the adventure and the campaign (entry tier). The wiki's "whole cadre" is not used.

**D10. Public or discreet: "not a public organization" against the adventure's public profile**
- Alexandrian Appendix B: "Force Grey is not a public organization. Its operations are deniable, its membership discreet, and its mandate broad" — `sources/Appendix_B_-_Player_Factions.md:823`
- Adventure: "Vajra offers the characters membership in the Gray Hands, a private security force under her command." — `sources/adventure-wdh.json:3780`
- Adventure (public profile): "She is also in charge of Force Grey, an order of highly skilled adventurers who are called upon to defend the city in times of need." — `sources/adventure-wdh.json:32680`
- Higher rank: the campaign rules the organization discreet (`05-force-grey.md:35`, "Deniable and Discreet"). The title "Blackstaff" and the Watchful Order are public (see the status section). The orchestrator should confirm whether Force Grey's existence is public.

**D11. "The city's most powerful individual wizard" against "isn't the city's most powerful wizard"**
- Alexandrian Appendix B: "the city's most powerful individual wizard and its designated guardian against arcane threats" — `sources/Appendix_B_-_Player_Factions.md:823`
- Adventure: "Vajra isn't the city's most powerful wizard, but she can hold her own." — `sources/adventure-wdh.json:32679`
- Campaign: the organization page keeps the Appendix B sentence "verbatim under ruling 29" (`05-force-grey.md:160`). Left to the user.

**D12. Renaer's rescue of Vajra (campaign) against the adventure's "rescue"**
- Adventure: "The Blackstaff, {@creature Vajra Safahr|WDH} (see {@adventure appendix B|WDH|12}), is friends with {@creature Renaer Neverember|wdh}, and word of his rescue quickly reaches her ears." — `sources/adventure-wdh.json:3764`. The rescue here is Renaer's own (his "rescue").
- Campaign, Renaer and Meloon pages: a rescue of Vajra in 1479 DR by Renaer and Meloon. No conflict in fact; the adventure is silent on Vajra's rescue. The year is `[research]` (`05-force-grey.md:28`).

**D13. Blackstaff Tower in the Castle Ward; the Watch's formal review**
- No conflict. Both the adventure (`:32680`) and the gazetteer (`castle-ward.md:61`) place the tower in the Castle Ward.

---

## E. Stale lines in other files (not to be edited) and routed quest references

**E1. Stale or conflicting lines in other files**
- `campaign/setting/governance-and-guilds/city-watch.md:63`, `code-legal-and-magisters.md:45`, `guilds.md:48`: "Neutral" (stale against `castle-ward.md:259`).
- `campaign/setting/organizations/05-force-grey.md:153`: "three years" (stale; see D5).
- `campaign/setting/notable-figures/independents-allies/05-meloon-wardragon.md:26`: "more than a decade ago" (agrees with the 1479 DR rescue only loosely; the campaign's own `[research]` tag is 1479).
- `docs/plans/setting-compendium-research-notes/consistency-notable-figures.md:16`: "Vajra NF force-grey/01:12,22 \"three years in the post\"" (a research note; the current page has no such line).
- `docs/plans/setting-compendium-research-notes/consistency-notable-figures.md:28`: "Vajra alignment \"neutral\" (NF:6) vs wiki lawful neutral." (a research note; the NF page now says lawful neutral).
- `campaign/setting/history/07-a-city-watching-itself.md:126` (Khelben's wife) and the wiki's Khelben Arunsun page (not in any bundle here): see D6.

**E2. Routed quest references (quest-time facts; the day-one page must not restate them)**
- `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/overview.md:21` (Vira Solkan, the disruptor, the Splinter attack on the Tower; the "junior arcanist" line).
- `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/ev-01-smoke-in-the-tower.md:22`: "Nobody in this Event says Manshoon's name, or calls Kolat Towers his home, unless **Manshoon Named** is marked for the member being addressed. Until then Vajra says \"the Splinter\" and \"the other cell\"."
- `campaign/quests/faction-events/force-grey/00-first-meeting/ev-01-first-meeting.md:25`: "The other Black Network cell is led by Manshoon. Vajra does not know that, and no Force Grey speaker names him until **Manshoon Named** is marked for the listener."
- `campaign/quests/faction-events/force-grey/s01-the-full-picture/ev-01-the-full-picture.md:22` and `:167`: the Cassalanter scrying residue, quest text.
- `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:81`: "Blackstaff here. Bronze dragon, Deepwater Harbor, outside the Dragonward. Intentions unknown. Come to the Tower now. Bring your people. Assess it, do not provoke it."
- `campaign/quests/faction-events/force-grey/m05-the-legates-eyes/ev-01-the-legates-eyes.md:70`: quest text about a devourer in a clerk.
- `campaign/quests/act-ii/gralhund-villa/ev-01-what-the-factions-say.md:38`: "Vajra admits as much at **Gralhund Villa**, where she says she cannot authorize an entry legally and promises only to speak to the Open Lord afterward." (per `05-force-grey.md:171`).
- `campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/overview.md:21` (the devourer occupation of Meloon; per `05-force-grey.md:172`).
- `campaign/quests/faction-events/force-grey/r25-force-grey/ev-01-force-grey.md:40`: "Vajra knows only that something lies under the Cassalanter villa, and she will not discuss it. Nobody in this Event knows more than she does."
- `campaign/quests/faction-events/force-grey/r03-junior-griffon/ev-01-junior-griffon.md:92` (per `campaign/setting/deities/umberlee.md:88`): the Queenspire letter and the harbor matter.
- `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/ev-01-the-brief.md:22` ("Until **Manshoon Named** is marked, nobody in this Event names Manshoon, and no Force Grey speaker names Jarlaxle or Bregan D'aerthe.").
- `campaign/guides/factions/06-force-grey.md:9` ("Mission 2 brings a report of a vessel fixed under the *Eyecatcher*'s hull, which is the Bregan D'aerthe submersible, and she never learns whose it is.").
- `campaign/guides/factions/06-force-grey.md:11` (Event Outcome gate **Manshoon Named**).
- Adventure, quest-time: `sources/adventure-wdh.json:14828` ("{@creature Vajra Safahr|WDH} sends {@creature Meloon Wardragon|WDH} (see {@adventure appendix B|WDH|12}) to help the characters secure the vault, unaware that Meloon has fallen under {@creature Xanathar|WDH}'s sway."); `:26740` (Vajra's invitation after Manshoon's death); `:26764` (the Kolat Towers ledger); `:30326` (Vajra's offer for Manshoon's spellbook).
- Appendix B, quest-time missions: `sources/Appendix_B_-_Player_Factions.md:839` to `:847` (the first Sending and the candidate invitation); `:872` to `:884` (the meeting at the standing desk).

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in Draft Notes.

**F1. Birth, family and early life.** The wiki gives a birth year (1455, line 768), a Tethyr origin (line 759, `formerhomes`), olive skin, short black hair and brown eyes (line 812), parents "Tamik al Safahr and Parama yr Manshaka" (line 776) and an infobox `familyrefs` citation to `BST-p247-251` (line 780). No campaign or adventure source gives any of these. The drafter must keep to "mid-thirties" or "late thirties" (`sources/adventure-wdh.json:32679`; `Appendix_D:1315`) and must not state a birth year. A parent's name is wiki-only and should carry `[research]` if used.

**F2. Training.** Wiki line 821 ("a skilled wizard"); adventure `:32680` ("Vajra runs Blackstaff Academy, a school for mages, out of Blackstaff Tower in the Castle Ward."). No source names a teacher other than Samark Dhanzscul in the wiki (line 809).

**F3. Samark Dhanzscul and the 1479 DR succession.** Wiki line 809: "her mentor and lover, [[Samark Dhanzscul]], was killed." Campaign: `05-force-grey.md:27` (the same, tagged as the wiki). No campaign page names Samark. A drafter who uses Samark must tag `[research]`.

**F4. How she came to the staff and the handpicking.** Adventure `:32679`: "She was handpicked for the job by Khelben Arunsun". Wiki: Khelben's death 1374 DR (line 257). See D6.

**F5. Where she lives.** No source gives a private residence. Sourced: Blackstaff Tower in the Castle Ward (`sources/adventure-wdh.json:32680`; `castle-ward.md:61`). The Gray Hands may enter the Tower "at any hour without appointment" (`06-force-grey.md:58`).

**F6. Faith.** No source gives Vajra a deity. Tyr and Hlam (`campaign/setting/deities/tyr.md:78`) concern Hlam, not Vajra. Leave blank or `[design]`.

**F7. Relationship to Khelben.** Sourced: Khelben is Laeral's husband (`sources/adventure-wdh.json:32202`), his soul is in the staff (`:32205`), and Vajra "rarely makes a decision without first soliciting the advice of the Blackstaff" (`:32679`). Laeral "covets the staff" (`:32205`). Wiki: "Khelben 'Blackstaff' Arunsun" as "the original Blackstaff who created Blackstaff Tower" (line 257). The drafter may not give Vajra a personal link to Khelben beyond the staff and the handpicking.

**F8. Relationship to Laeral.** Sourced: "Laeral's relationship with Vajra ... has its challenges" (`:32205`); "an uneasy superior to Vajra Safahr (whom she views as an insecure child wielding her husband's staff)" (Laeral page, `city-officials/01-laeral-silverhand.md:25`). Vajra's Notable Figures page says "a strained subordinate of Laeral Silverhand" (line 25).

**F9. Personal goals.** The page's Motivations (line 15): "Vajra wants to defend Waterdeep using Force Grey, prove that she earned the Blackstaff rather than inherited it, and outlast the senior wizards who consider her an upstart." The adventure's "she still questions her ability to meet the demands of her role" (`:32679`) and the wiki's "prone to self-doubt" (line 815) support a goal about self-proof. Anything beyond these is `[design]`.

**F10. Friends and staff.** Sourced: Renaer (`:3764`, "is friends with"), Meloon (`:32255`: "His friends-among them {@creature Renaer Neverember|wdh} and {@creature Vajra Safahr|WDH}-describe him as honest, optimistic, and extraordinarily lucky."), the Tower's quartermaster Merris and the Tower mage Ysmay Halvane (`06-force-grey.md:59`, `:62`). The Tower's mages are not named in the adventure.

---

## G. Source facts that hint at the figure's inner life (exact quotes)

- Adventure, page 216: "Despite her many gifts, she still questions her ability to meet the demands of her role, and she rarely makes a decision without first soliciting the advice of the Blackstaff, which contains Khelben Arunsun's spirit as well as the spirits of all the other Blackstaffs who preceded her." — `sources/adventure-wdh.json:32679`
- Adventure, page 216: "Several of the older and more seasoned wizards in Waterdeep consider Vajra an upstart, but they are smart enough not to challenge her." — `sources/adventure-wdh.json:32682`
- Wiki, line 815: "Although she was prone to self-doubt when she first assumed the role of the Blackstaff, she soon learned to ignore those doubts and to dismiss the envies of those who were skeptical of her role."
- Wiki, line 818: "She was focused on turning Waterdeep, and specifically her [[Blackstaff Academy]], into the center of [[magical]] study in [[Faerûn]]."
- Notable Figures, Persona (line 21): "her years as the youngest Blackstaff ever have worn her down. Deep down, she wields a staff containing Khelben Arunsun's soul, and Laeral Silverhand views her as an insecure child holding her dead husband's weapon. She does not find observations about her youth interesting."
- Notable Figures, Emotions (line 13): "private exhaustion she will not show."
- Notable Figures, Motivations (line 15): "prove that she earned the Blackstaff rather than inherited it".
- Force Grey organization page, Overview GM Notes (line 108): "**The staff:** The Blackstaff holds Khelben Arunsun's soul, and Vajra rarely decides without consulting it (*Dragon Heist*, 5e). Laeral wants it back, which is part of why the two avoid each other."
- Voice profile, line 12: "Comments about her youth earn a cold stare and a subject change." and line 15: "She never discusses what's in the Blackstaff, never asks for sympathy, and never lets anyone see her doubt herself."
- Force Grey organization page, History (about 1489 DR): "Her spies tell her that Vajra has secretly activated members and sent them on a number of unauthorized missions." — `05-force-grey.md:29`
- Castle Ward gazetteer (Laeral entry, line 123): "She considers Vajra an insecure child holding her husband's soul in the Blackstaff." — `campaign/gazetteer/waterdeep/castle-ward.md:123`

**Cassalanter secrecy (Connections)**
- Force Grey organization page: "- **The Cassalanters (neutral, suspicious):** Scrying from Blackstaff Tower has found conjuration and abjuration residue beneath the Cassalanter villa. Vajra cannot say what makes it and does not guess, and nobody in Force Grey knows about the pact (**The Cassalanters** in Villains; **Force Grey** in the Factions Guide)." — `campaign/setting/organizations/05-force-grey.md:89`
- Factions Guide: "This is suspicion only, and nobody in Force Grey knows more than she does." — `campaign/guides/factions/06-force-grey.md:32`
- Quest, r25: "Vajra knows only that something lies under the Cassalanter villa, and she will not discuss it. Nobody in this Event knows more than she does." — `campaign/quests/faction-events/force-grey/r25-force-grey/ev-01-force-grey.md:40`

**Lolth and Xanathar**: no Lolth line in either Force Grey file. Xanathar appears in the Factions Guide as "Xanathar's mind-control operations" (`06-force-grey.md:47`, "countering Xanathar's mind-control operations is Force Grey's most urgent Grand Game priority"). The Notable Figures page does not name Xanathar.

---

## Public or discreet: Vajra's status

- Adventure (public profile): "Vajra runs Blackstaff Academy, a school for mages, out of Blackstaff Tower in the Castle Ward. She is also in charge of Force Grey, an order of highly skilled adventurers who are called upon to defend the city in times of need." — `sources/adventure-wdh.json:32680`
- Adventure, the sending to the party: "\"I am {@creature Vajra Safahr|WDH}, the Blackstaff. Come to Blackstaff Tower in the Castle Ward at once. Bring your friends.\"" — `sources/adventure-wdh.json:3769`
- Adventure, the Watchful Order: "encouraged to join the Watchful Order of Magists and Protectors, headed by the Blackstaff." — `sources/adventure-wdh.json:30578`
- Campaign, Open Lord page: "Only the Open Lord can strip **Vajra Safahr** of her title as Blackstaff." — `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:30`
- Campaign, Castle Ward (public-facing): "- Vajra Safahr, the Blackstaff, trains wizards here and heads the Watchful Order." — `castle-ward.md:61`
- Campaign, Force Grey organization page: "- **Deniable and Discreet:** Force Grey's operations are deniable and its membership is discreet." — `05-force-grey.md:35`
- Appendix B: "Force Grey is not a public organization. Its operations are deniable, its membership discreet, and its mandate broad" — `sources/Appendix_B_-_Player_Factions.md:823`
- Masked Lord status: Vajra is not a Masked Lord in any campaign file. The Open Lord page's Key Members lists Mirt, Jelenn, Durnan, Ulkoria and Caladorn, not Vajra (`open-lord-and-masked-lords.md:38` to `:50`). The Masked Lords "rule beside the Open Lord" (`open-lord-and-masked-lords.md:16`). The Force Grey org page says: "Ulkoria Stonemarrow, a senior member of the Watchful Order that Vajra heads, is also a Masked Lord in the campaign (**North Ward**)." — `05-force-grey.md:92`. Ulkoria's Masked Lord status is campaign-only (`open-lord-and-masked-lords.md:46`: "The campaign makes her a Masked Lord, which is never confirmed in her presence (campaign-only).").

---

## Cross-references (every other file:line where the topic appears, with its line)

- `campaign/setting/organizations/05-force-grey.md:7` to `:31` (Summary, History), `:35` (Beliefs), `:49` to `:61` (Structure), `:88` to `:92` (Relationships), `:96` (Key Members), `:108` (GM Notes), `:153` (stale three-years note), `:155` to `:162` (conflicts)
- `campaign/guides/factions/06-force-grey.md:7`, `:9`, `:11`, `:23`, `:30`, `:32`, `:37`, `:58`, `:59`, `:67`, `:73`, `:75`
- `campaign/gazetteer/waterdeep/castle-ward.md:60`, `:61`, `:123`, `:125`, `:126`, `:131`, `:170`, `:259`
- `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:16`, `:30`, `:46`
- `campaign/setting/governance-and-guilds/city-watch.md:63`; `code-legal-and-magisters.md:45`; `guilds.md:48`
- `campaign/setting/notable-figures/city-officials/01-laeral-silverhand.md:15`, `:21`, `:25`
- `campaign/setting/notable-figures/independents-allies/02-renaer-neverember.md:25`; `05-meloon-wardragon.md:22`, `:26`
- `campaign/setting/history/07-a-city-watching-itself.md:31` to `:32`, `:43` to `:45`, `:76`, `:132`
- `campaign/setting/history/06-the-open-lords-fall.md:164`
- `campaign/setting/geography/dragonward-and-walking-statues.md:38` ("**The Blackstaff:** Only the wielder of the Blackstaff can animate the seven statues that are still whole. **Vajra Safahr** holds the Blackstaff now.")
- `campaign/setting/geography/city-of-the-dead.md:48` (Vajra's written permit to enter at night)
- `campaign/setting/geography/waterdeep.md:73` ("The Watchful Order and Force Grey")
- `campaign/setting/deities/mystra.md:85` ("**Khelben and the Blackstaff:** The campaign calls Khelben Arunsun the original Blackstaff and Laeral's late husband. His soul is in the staff that Vajra Safahr carries.")
- `campaign/setting/deities/tyr.md:78` (Hlam and Force Grey Mission 1)
- `campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:30` ("| **Force Grey** | Vajra Safahr sends a *Sending* spell to one party member | Renaer's rescue brought the party to Vajra's attention |")
- `docs/plans/harpers-mechanics-reference.md:586`, `:587`, `:598`
- `docs/plans/npc-pronouns-table-group-b.md:16` ("| Vajra Safahr | force-grey/01-vajra-safahr-the-blackstaff.md:5 | she/her |")
- `sources/adventure-wdh.json` `:349` and `:350` (pronunciation "VOJ-rah sah-FAR"), `:1339`, `:1342`, `:1343`, `:1348`, `:3764`, `:3769`, `:3772`, `:3779`, `:3780`, `:10593`, `:13575`, `:13701`, `:14753`, `:14828`, `:26740`, `:26764`, `:30326`, `:30578`, `:31012`, `:31620`, `:32202`, `:32205`, `:32206`, `:32219` ("kill the Blackstaff"), `:32255`, `:32666` to `:32684`, `:32723`
- `sources/Appendix_B_-_Player_Factions.md:821` to `:847`, `:872` to `:884`, `:901` to `:908`
- `sources/Appendix_C_-_Player_Faction_Missions.md:937` to `:939` (the Force Grey mission table entries)
- `sources/Appendix_D_-_Running_the_Tavern.md:845` to `:848` (Vajra's offer), `:1312` to `:1321` (Vajra's NPC entry), `:1135` (roll table)
- `sources/SOURCE_GUIDE.md:172` (Vajra as a faction contact), `:600` (Force Grey conditions), `:696` (the .docx, see Not readable)
- `sources/research/pass5-bundles/force-grey/wiki.txt:58`, `:73`, `:87`, `:249`, `:251`, `:255`, `:257`, `:745` to `:826`
- `docs/plans/setting-compendium-research-notes/pass1-era4-era6.md:22` (the Patreon rescue date)

---

## Not found

- Searched for Vajra's faith, residence, a teacher other than Samark Dhanzscul, siblings, children, and a personal artefact besides the staff: nothing in the campaign files, the adventure, Appendix B, C or D, or the wiki extract. Gaps listed in F.
- Searched `campaign/` for "Rogue construct" (case-insensitive) and "two hours ago": no match in the quest files. Voice sample only (`.claude/skills/character-voices/voices/force-grey.md:17`).
- Searched `campaign/` for "shit-brained cultist" and "just opened a portal": only the voice profile's line 11 uses "shit-brained"; the Legate's Eyes quest line 70 says "some shit-brained Guild breeder" (`campaign/quests/faction-events/force-grey/m05-the-legates-eyes/ev-01-the-legates-eyes.md:70`); "just opened a portal" is in no quest file.
- Searched `campaign/` for "three years" in the Notable Figures page: none (D5).
- Searched the Force Grey wiki bundle for "Vajra Safahr" to find the scratchpad stub's page: found at `sources/research/pass5-bundles/force-grey/wiki.txt:745`; the scratchpad stub `wiki-force-grey/01-vajra-safahr-the-blackstaff.txt` reads NOT FOUND.
- Searched the Force Grey wiki bundle for "Khelben" and "Samark" to confirm the mentor line: "Samark" appears only at line 809 of that bundle in the Vajra page, and in the campaign only at `05-force-grey.md:27` and `:59`.
- Searched for a Force Grey Alexandrian PDF page: not read for this note.

## Not readable

- `sources/Other remix files/` `.docx` at `sources/SOURCE_GUIDE.md:696`: "`Vajra Safahr, Zelifarn, and Deepwater Harbor quests.docx`" (covers "Vajra as Force Grey Blackstaff, Zelifarn the sea dragon, Deepwater Harbor quest hooks"). It was not opened (no shell). Extract it before any Vajra draft that touches the Deepwater Harbor or Zelifarn.
- `sources/3. Player Character Factions.pdf`: read only at PDF p.3 for the Lords' Alliance (see the Jalester notes). No Force Grey page was read from it.
- Scratchpad stub `wiki-force-grey/01-vajra-safahr-the-blackstaff.txt` is `NOT FOUND`. The wiki page was taken from the bundle instead (Method).
