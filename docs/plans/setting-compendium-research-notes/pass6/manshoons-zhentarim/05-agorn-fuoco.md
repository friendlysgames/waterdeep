# Pass 6 research notes: Agorn Fuoco

Page: `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Group folder: `manshoons-zhentarim` (Villain factions, Stage 1)
Faction organization page: `campaign/setting/organizations/09-manshoons-zhentarim.md`
Villains page: `campaign/setting/villains/manshoon.md` (names Agorn only at line 116; no background)
Voice profile: `.claude/skills/character-voices/voices/manshoons-zhentarim.md` (`### Agorn Fuoco`, lines 85-99)
Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-manshoons-zhentarim/05-agorn-fuoco.txt` (cited as `wiki05:N`, the line numbers of that file)
Model notes: `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md`

Method and caveats:
- Campaign files: Read and Grep, quoted from the tool output.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. Tags such as `{@creature ...}` are left as written. JSON escapes are shown as plain quotes.
- Alexandrian PDF: `sources/6. Faction Response Teams.pdf`, printed p.55 [PDF p.7]. This session has no shell, so `pdftotext` could not run. The quote was transcribed from the rendered page image. Check it with `pdftotext -layout` before any quote goes into prose. The Kolat Towers PDF (`sources/12. Lair  Zhentarim – Kolat Towers.pdf`, pp.94-95) and the revelation list (`sources/17. Outpost and Lair Revelation Lists.pdf`, p.123) are cited only from earlier pass 6 notes, not re-read here.
- Wiki: most lines print no edition. Editions come from the citation keys and the infobox, and are marked inferred where so.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written.

---

## A. Background facts by theme

### A1. Origin, home and family

**Race, sex, ethnicity, home (wiki only; infobox, 5e citation key `WDH5e-p76`)**
> "| home           = [[Waterdeep]], [[Sword Coast North]]" — `wiki05:11`
> "| sex            = Male" — `wiki05:13`
> "| race           = [[Human]]" — `wiki05:14`
> "| ethnicity      = [[Turami]]" — `wiki05:15`
> "| occupation     = Bard" — `wiki05:16`

**Parents (wiki only)**
> "| parents        = [[Marta Fuoco]]" — `wiki05:29`

**Pronunciation (wiki, 5e key; the adventure index also gives it)**
> "'''Agorn Fuoco''' ({{Pronounce|AY|gorn|_|foo|OH|koh|refs=<ref name="WDH5e-p4">{{Cite book/Waterdeep: Dragon Heist|4}}</ref>}}) was a high-ranking member of [[Manshoon]]'s [[Zhentarim]] in [[Waterdeep]] during the early 1490s [[DR]].<ref name="WDH5e-p76" />" — `wiki05:62`
> adventure index row: `["Agorn Fuoco", "AY-gorn foo-OH-koh"]` — `sources/adventure-wdh.json:41-42`

**Mistshore, the music, the mother (adventure, 5e; page 67)**
> "Agorn made such a good impression on {@creature Manshoon|WDH} that he was elevated quickly through the ranks of the organization, but his life is full of disappointment otherwise. He has not achieved the fame he craved nor earned the wealth he felt he was entitled to. He has adopted the Zhentarim credo that power comes to those who deserve it and has come to see the Black Network as a new family of sorts. Agorn has come to Mistshore to visit a member of his actual family-his mother, who is gravely ill and lives in abject poverty." — `sources/adventure-wdh.json:7599`

> "The children know who Agorn Fuoco is because he used to live and play music in Mistshore. They offer to lead characters to his mother's residence." — `sources/adventure-wdh.json:7625`

> "Agorn lived and played music in [[Mistshore]].<ref name="WDH5e-p68">{{Cite book/Waterdeep: Dragon Heist|68}}</ref> Later, he settled in [[Kolat Tower]] with his master Manshoon.<ref name="WDH5e-p158">{{Cite book/Waterdeep: Dragon Heist|158}}</ref>" — `wiki05:65` (5e key)

**The mother's name and state (adventure; quest-time scene, see C and D1)**
> "Agorn Fuoco (NE male Turami {@creature bard|VGM}; see {@adventure appendix B|WDH|12}) is inside, trying to smother his bedridden mother, Marta (N female Turami human {@creature commoner} with 1 hit point), with a sack she uses as a pillowcase. With tears born of joy and sadness streaming down his face, Agorn is cutting loose his old family ties and embracing his new family: the Zhentarim. The characters can stop him from committing matricide by pulling him away from his mother before she suffocates." — `sources/adventure-wdh.json:7634` (the entry is "Mother and Son", page 68)

**The mother (campaign, day-one, the page as it stands)**
> "**Relationships.** Agorn is a Manshoon lieutenant and bard, the partner of Amath Sercent, whom he visits at Yellowspire in the evenings, a pass-amulet holder for Kolat Towers, and a man whose mother lives in Mistshore and knows nothing about any of this." — `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:25`

**The mother (wiki, 5e key; the attempt, see C and D1)**
> "Afterward, Agorn went to meet his mother and, inspired by the theater's play and by Amath, he tried to kill the woman in order to cut all his ties to his old family.<ref name="WDH5e-p67-68">{{Cite book/Waterdeep: Dragon Heist|67-68}}</ref>" — `wiki05:72`

**The mother (Alexandrian, printed p.55 [PDF p.7]; image transcription)**
> "He has adopted the Zhentarim credo that power comes to those who deserve it. In fact, he believed it so much that he murdered his own mother in order to "escape" her poverty. He has come to see the Black Network as a new family of sorts." — `sources/6. Faction Response Teams.pdf`, printed p.55 [PDF p.7] **[image transcription]**

**Mother in the campaign voice profile**
> "- **Word choice:** Artistic and social: performances, "delightful company", "a small favour". He calls his mother "Mama", and becomes briefly comprehensible when she's present." — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:90` (no source for "Mama"; see F12)

### A2. Early ambition and joining the Zhentarim

**Wiki (5e key, `WDH5e-p67`)**
> "Agorn dreamed of becoming a famous bard but he had no success so he decided to devote himself to the Zhentarim, quickly advancing through the ranks.<ref name="WDH5e-p67">{{Cite book/Waterdeep: Dragon Heist|67}}</ref>" — `wiki05:68`

**Adventure (5e)** — the same passage as A1, `sources/adventure-wdh.json:7599`: "He has not achieved the fame he craved nor earned the wealth he felt he was entitled to."

**Alexandrian, same sense (printed p.55 [PDF p.7]; image transcription)**
> "AGORN FUOCO: Agorn made such a good impression on Manshoon that he was elevated quickly through the ranks of the organization, but his life was full of disappointment otherwise. He has not achieved the fame he craved nor earned the wealth he felt he was entitled to." — `sources/6. Faction Response Teams.pdf`, printed p.55 [PDF p.7] **[image transcription]**

No source gives the year, the place or the recruiter of his joining.

### A3. Rise and rank

**Campaign, the Zhentarim rule of promotion (org page)**
> "- **Recruiting:** The Black Network has an open recruitment policy that prizes tenacity and loyalty without requiring either, but the published adventure says adventurers cannot join Manshoon's cause (*Dragon Heist*, 5e). His lieutenants rise by impressing him, and Agorn Fuoco was raised quickly after he made a good impression on the wizard (*Dragon Heist*, 5e). Kaevja Cynavern was a Red Wizard of Thay who gave up her Thayan head tattoos and red robes to study under him (*Dragon Heist*, 5e)." — `campaign/setting/organizations/09-manshoons-zhentarim.md:71`

**Wiki, lieutenant and impression (5e key; the wiki cites p.148 and p.67)**
> "Agorn was one of the lieutenants of Manshoon<ref name="WDH5e-p148">{{Cite book/Waterdeep: Dragon Heist|148}}</ref> who was very impressed by him.<ref name="WDH5e-p67" />" — `wiki05:75`

**Campaign, the title**
> "- **Agorn Fuoco** — Turami human bard (Manshoon lieutenant), neutral evil, and a hollow coward who sends his thugs into danger while hanging back; see the **Agorn Fuoco** page in Notable Figures." — `campaign/setting/organizations/09-manshoons-zhentarim.md:99`

> "- *Turami human bard (Manshoon lieutenant), neutral evil, he/him*. Stat block: **Performer**." — `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:5`

**Campaign, the cell's ranks (no rank titles beyond "lieutenant")**
> "- **Size and ranks:** `[research]` No source counts the cell's members or gives it rank titles beyond "lieutenant". The wiki's ranks, from Fang to Dread Lord, belong to the Doom Raiders in the campaign." — `campaign/setting/organizations/09-manshoons-zhentarim.md:60`

**Adventure, the two "most trusted" lines (5e)**
> "Vevette and Agorn are two of {@creature Manshoon|WDH}'s most trusted followers. Vevette commands the wizard's forces against the Xanathar Guild, while Agorn commands those who oppose the Zhents that aren't loyal to {@creature Manshoon|WDH}. At the moment, they are resting in the sanctum while awaiting orders from {@creature Manshoon|WDH}." — `sources/adventure-wdh.json:30130` (Kolat Towers, the "Zhents" entry, page 159)

**Campaign, the command role is not given (org page draft note)**
> "> - **Conflicts:** Agorn's command. The published adventure has Agorn lead the forces that oppose the Zhents not loyal to Manshoon (`adventure-wdh.json` line 30130), and the campaign gives Agorn no such role (`05-agorn-fuoco.md`). Structure keeps the line with a "published adventure" tag." — `campaign/setting/organizations/09-manshoons-zhentarim.md:181`

**Campaign, the field-team role (Factions Guide)**
> "All three Zhentarim response teams consist of a lieutenant plus 3–4 **thugs**. Every lieutenant carries a pass-amulet to Kolat Towers and will try to destroy it if capture seems certain, except Agorn, who trades his to save himself." — `campaign/guides/factions/10-manshoons-zhentarim.md:7`

> "**Agorn Fuoco** — bard + 3–4 **thugs**." — `campaign/guides/factions/10-manshoons-zhentarim.md:12`

**Alexandrian, the response-team lieutenant (printed p.55 [PDF p.7]; image transcription)**
> "Manshoon's response teams consist of:" / "1 lieutenant (Vevette, Urstul, or Agorn)" / "3-4 thugs" — `sources/6. Faction Response Teams.pdf`, printed p.55 [PDF p.7] **[image transcription]**

**Time in post**: no source gives it. The wiki's "Later, he settled in Kolat Tower" (`wiki05:65`) has no date.

### A4. Relationships

**Amath Sercent (campaign, settled)**
> "- **Amath Sercent** — Mulan human priest of Bane, lawful evil, who occupies Yellowspire in the Castle Ward as a Banite priestess allied with Manshoon. Agorn Fuoco is her romantic partner and visits her there in the evenings. See the **Amath Sercent** page in Notable Figures." — `campaign/setting/organizations/09-manshoons-zhentarim.md:103`

> "Amath is the Banite priestess occupying Yellowspire (Castle Ward), the keeper of a teleportation circle providing a back-route into Kolat Towers (bypassing the pass-amulet requirement), Agorn Fuoco's romantic partner, and a Manshoon-adjacent religious operative whose devotion to Bane predates and outlasts any particular Zhentarim arrangement." — `campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md:25`

> "- Amath is a priest of Bane allied with Manshoon's Zhentarim, and she keeps the teleportation circle to Kolat Towers. She is the partner of Agorn Fuoco." — `campaign/gazetteer/waterdeep/castle-ward.md:82`

> "Amath Sercent is Agorn Fuoco's romantic partner, per `05-agorn-fuoco.md` line 25, `08-amath-sercent.md` line 25 and `castle-ward.md` line 82, which replaces the old "Friends with Agorn Fuoco, who visits when he wants company"." — `campaign/setting/organizations/09-manshoons-zhentarim.md:160` (Draft Notes, "Settled (ruling 23)")

**Amath (adventure, quest-time scene; the lady friend)**
> "Agorn was moved to perpetrate this act by the play he saw at the theater and by his lady friend, Amath Sercent, to whom he entrusted the Stone of Golorr." — `sources/adventure-wdh.json:7635`

**Amath (wiki, 5e key)**
> "However, Agorn entrusted the ''Stone'' to his girlfriend [[Amath Sercent]].<ref name="WDH5e-p68">{{Cite book/Waterdeep: Dragon Heist|68}}</ref>" — `wiki05:70` (same paragraph; see D3)

**Vevette Blackwater (adventure, shared duty only)**
> "Vevette takes a seat behind them and surreptitiously passes the {@item Stone of Golorr|WDH} to Agorn." — `sources/adventure-wdh.json:9133` (Theater, page 76; quest-time, see D3)

> "{@creature Kaevja Cynavern|wdh}, Vevette Blackwater, Agorn Fuoco, {@creature Zhent Martial Arts Adept|wdh|Havia Quickknife}, and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush} all sleep here." — `sources/adventure-wdh.json:30212` (Kolat Towers sleeping quarters; the room ID is not read here)

No source gives a friendship or a rivalry with Vevette beyond shared duty.

**Remallia Haventree (Harper surveillance, adventure)**
> "Looking on from the back row is {@creature Remallia Haventree|WDH} (see {@adventure appendix B|WDH|12}), a member of the Harpers who suspects Agorn of being a high-ranking Zhent. She has been watching him for a while now, hoping to identify other Zhentarim leaders in Waterdeep." — `sources/adventure-wdh.json:9133`

**Manshoon (campaign)**
> "- **Manshoon** — Vaasan human wizard (clone), lawful evil; see the **Manshoon** page in Notable Figures." — `campaign/setting/organizations/09-manshoons-zhentarim.md:96`

Manshoon's view of him is given only as "very impressed" (`wiki05:75`) and "most trusted followers" (`sources/adventure-wdh.json:30130`).

**Urstul Floxin and Avareen (campaign, field reports, Factions Guide)**
> "| Suspicious | Flying snake courier network; Agorn and Avareen's field reports. Avareen identifies the threat; Urstul reviews field reports |" — `campaign/guides/factions/10-manshoons-zhentarim.md:52`

> "| Alert | Agorn or Vevette's team; orders are to capture, not kill |" — `campaign/guides/factions/10-manshoons-zhentarim.md:53`

**Xanathar's Guild (campaign, Factions Guide)**
> "- *Report to Agorn Fuoco* (Response Team: Agorn Fuoco — names Orb Confectioners on Rising Ride)" — `campaign/guides/factions/09-xanathars-guild.md:95` (conflict D7)

### A5. Belongings

**Pass-amulet (campaign; the page's own mention)**
> "a pass-amulet holder for Kolat Towers" — `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:25`

> "Every lieutenant carries a pass-amulet to Kolat Towers and will try to destroy it if capture seems certain, except Agorn, who trades his to save himself." — `campaign/guides/factions/10-manshoons-zhentarim.md:7` (quest-time use, see C)

**Lyre and lute (adventure and quest)**
> "Unless they've been drawn elsewhere, two of {@creature Manshoon|WDH}'s lieutenants are here: Vevette Blackwater (CE female Tethyrian human {@creature swashbuckler|VGM}; see {@adventure appendix B|WDH|12}) and Agorn Fuoco (NE male Turami human {@creature bard|VGM}; see {@adventure appendix B|WDH|12}). Vevette is relaxing in a chair, while Agorn strums a lyre." — `sources/adventure-wdh.json:30120`

> "He visits on those evenings to see Amath." — `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:159` (the same entry says he "sits by the ground-level fire and tunes a lute")

**Green flame brazier (adventure, combat knowledge)**
> "Agorn knows this feature of the brazier, and he uses it in combat if the situation is desperate." — `sources/adventure-wdh.json:30139`

**Love letters (adventure, the chest)**
> "Agorn's chest contains a bundle of love letters from someone named Tamzyn. Hidden in one of the envelopes is an elegant platinum necklace (worth 250 gp), featuring a tiny cameo containing a sketched portrait of a beautiful Turami woman." — `sources/adventure-wdh.json:30222` (Tamzyn is not described further in any source)

### A6. Faith

No source gives Agorn a deity or a rite. The Milil page says he names no worship:
> "**Bards checked:** No Notable Figures page for Mattrim "Threestrings" Mereg, Variel Duskwhisper, Davil Starsong, Margo Verida or Agorn Fuoco names Milil (Grep for "Milil" over `campaign/` returns only the staff table, the Deities pages and the research notes), so the page names no worshiper beyond Lysa's history." — `campaign/setting/deities/milil.md:116`

The Bane page names him as a visitor only:
> "Agorn Fuoco (Neutral Evil, Turami Human, he/him) visits in the evenings for company and is Amath's partner. He flees at the first sign of a fight." — `campaign/setting/deities/bane.md:84`

The adventure gives the Zhentarim credo, not a faith (`sources/adventure-wdh.json:7599`, quoted in A1).

### A7. The Stone of Golorr and the cell (quest-time, see D3)

The hand-off of the Stone to Agorn (`sources/adventure-wdh.json:9133`) and to Amath (`:7635`) are in the adventure's Dragon Heist chain. The campaign timeline does not give the Stone to the Zhentarim before Ches 22 (see D3).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, the page: "*Turami human bard (Manshoon lieutenant), neutral evil, he/him*. Stat block: **Performer**." — `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:5`
- Campaign, the org page: "Turami human bard (Manshoon lieutenant), neutral evil" — `campaign/setting/organizations/09-manshoons-zhentarim.md:99`
- Campaign, the quest file: "Agorn Fuoco (Neutral Evil, Turami Human, he/him) is in the tower only if the party enters during working hours after dusk" — `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:159`
- Campaign, the Bane page: "Agorn Fuoco (Neutral Evil, Turami Human, he/him)" — `campaign/setting/deities/bane.md:84`
- Adventure: "Agorn Fuoco (NE male Turami {@creature bard|VGM}; see {@adventure appendix B|WDH|12})" — `sources/adventure-wdh.json:7634`; "a Zhentarim spy named Agorn Fuoco (NE male Turami {@creature bard|VGM}; see {@adventure appendix B|WDH|12})" — `:9133`; "Agorn Fuoco (NE male Turami human {@creature bard|VGM}; ...)" — `:30120`, `:14783`
- Alexandrian, printed p.55 [PDF p.7]: "Stats: NE male Turami bard (DH p. 195)" **[image transcription]**
- Wiki: "| alignment5e    = [[Neutral evil]]" — `wiki05:57`
- Wiki, the 5e class: "| class5e        = [[Bard]]" — `wiki05:59`; "| refs5e         = <ref name="WDH5e-p76">..." — `wiki05:60`

Alignment agrees across all sources. No conflict.

**Species and ethnicity**
- Campaign: "Turami human" — `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:5` (ruling 5: a Faerûn ethnicity; Turami is one)
- Adventure: "NE male Turami human" — `sources/adventure-wdh.json:30120`
- Wiki: "| race           = [[Human]]" — `wiki05:14`; "| ethnicity      = [[Turami]]" — `wiki05:15`

**Pronouns**
- Campaign: "he/him" — `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:5`
- Adventure: "NE male" (`sources/adventure-wdh.json:9133`) and "his mother" (`:7634`)
- Wiki: "| sex            = Male" — `wiki05:13`
- `docs/plans/npc-pronouns-table-group-c.md:49` gives "he/him" with the same sources.

**Stat block (conflicts, see D4)**
- Campaign, the page: "Stat block: **Performer**." — `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:5`
- Campaign, the quest file: "He never fights and has no stat block, and he flees the moment a fight starts." — `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:159`
- Campaign, the session record: "Kalain, Mattrim, Variel, Agorn and Margo on Performer stat blocks" — `session 51 handoff.md:24`
- Campaign, the session record: "There is no 2024 Bard, so Agorn Fuoco is a non-combatant." — `session 38 handoff.md:136`
- Adventure: bard, 2014 name, "{@creature bard|VGM}" (`sources/adventure-wdh.json:9133`)
- Alexandrian: "Stats: NE male Turami bard (DH p. 195)" (printed p.55 [PDF p.7]) **[image transcription]**
- Wiki: "| class5e        = [[Bard]]" — `wiki05:59`
- Doom Raiders mechanics reference (planning note, not a source): "| Agorn Fuoco "Bard" | **Unverified** | No Bard record found in XMM; Mage Apprentice (CR 2) offered as a named swap. He does not fight. |" — `docs/plans/doom-raiders-mechanics-reference.md:263`
- Harpers mechanics reference (planning note): "| Bard (Mattrim, Agorn) | **Performer** (CR 1/2) or **Performer Maestro** (CR 6) | 1/2 or 6 | XMM pp.236-237. Mattrim is not a combatant in the Harper pages. |" — `docs/plans/harpers-mechanics-reference.md:572`

---

## C. Every sentence on the current page

Current page: `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md`. "Day-one OK" means no quest gate is needed. "Quest-time" means the sentence narrates a capture, a rescue, a scene or a quest event. "Conditional" means it describes what he does if captured or in a fight.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Turami human bard (Manshoon lieutenant), neutral evil, he/him*. Stat block: **Performer**." | Day-one. Stat label conflicts with the quest file (D4) | Org `09-manshoons-zhentarim.md:99`; quest `ev-01-the-yellowspire-job.md:159` |
| 2 | L6 | "**Affiliation:** Manshoon's Zhentarim" | Day-one OK | Org page title, `09-manshoons-zhentarim.md:1` ("# Manshoon's Zhentarim") |
| 3 | L7 | "**Featured in:** **Faction Outposts**, **Kolat Towers**; **The Yellowspire Job**" | Cross-reference only. The Yellowspire Job is a Doom Raiders faction mission (quest) | `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/overview.md` (exists); Faction Outposts `campaign/structure/arc-e-faction-outposts.md:223`, `:231`; Kolat `arc-i-kolat-towers.md:156` |
| 4 | L11 | "**Resonance.** Agorn should inspire pity when you realize he is genuinely out of his depth; contempt when he starts trading people to buy his own escape; and wry surprise when his mother appears and he becomes, briefly, comprehensible." | Mixed. "out of his depth" day-one. "starts trading people to buy his own escape" is capture behaviour (Conditional). "when his mother appears" describes the Mistshore scene, which is quest-time | Trading: `campaign/guides/factions/10-manshoons-zhentarim.md:7`, `:77`; Mother scene: `sources/adventure-wdh.json:7634`; Alexandrian `6. Faction Response Teams.pdf` p.55 |
| 5 | L13 | "**Emotions.** Agorn most often feels artistic self-absorption, the particular anxiety of someone who has made too many decisions based on mood, passive compliance with whoever is most immediately persuasive, genuine love of music that sits embarrassingly alongside everything else, and deep filial attachment to his mother." | Day-one (feelings). "deep filial attachment to his mother" needs the mother's day-one state (F7) | Music: `sources/adventure-wdh.json:7625`; mother: `:7599`; wiki `wiki05:65` |
| 6 | L15 | "**Motivations.** Agorn wants to avoid consequences for his Zhentarim work, use whatever he knows (Amath's identity, his pass-amulet, Manshoon's operational structure) to buy his freedom, and eventually retire somewhere quieter." | Day-one as a want. The "buy his freedom" wording is a capture plan | Pass-amulet and capture: `10-manshoons-zhentarim.md:7`, `:77`; Amath: `08-amath-sercent.md:25` |
| 7 | L17 | "**Inspirations.** When playing Agorn, channel Pete Campbell (*Mad Men*), Zaphod Beeblebrox (*The Hitchhiker's Guide to the Galaxy*), and Tom Ripley (*The Talented Mr. Ripley*, the man always one step behind the situation)." | Not a fact | n/a |
| 8 | L21 (a) | "**Persona.** To the world, Agorn Fuoco is a bard who attends the theater, keeps excellent company, and does occasional work for the Zhentarim that he does not ask about too carefully." | Day-one | "attends the theater": `sources/adventure-wdh.json:9133` (the theater scene, quest-time, shows him there); "keeps excellent company": no source (the page's own phrase) |
| 9 | L21 (b) | "To those who capture him, he offers his pass-amulet, Amath Sercent's address, Manshoon's general operational structure, and whatever else occurs to him — starting immediately and working outward from least to most useful, in the order most likely to buy another minute." | Conditional. Describes behaviour under capture, which is quest-time | Pass-amulet barter: `campaign/guides/factions/10-manshoons-zhentarim.md:77` ("Capturing Agorn Fuoco: he barters his pass-amulet"); Alexandrian p.55; Yellowspire: `ev-01-the-yellowspire-job.md:159` |
| 10 | L21 (c) | "Deep down, he would rather be playing music." | Day-one (inner life) | Music: `sources/adventure-wdh.json:7625`; wiki `wiki05:65` |
| 11 | L23 (a) | "**Morale.** In a fight, Agorn attempts to flee immediately." | Day-one OK (combat behaviour) | `sources/adventure-wdh.json:7644` ("while Agorn tries to escape"); `ev-01-the-yellowspire-job.md:159` ("he flees the moment a fight starts"); `sources/6. Faction Response Teams.pdf` p.55 |
| 12 | L23 (b) | "If capture is certain, he begins trading information before anyone asks." | Conditional. Describes capture | `ev-01-the-yellowspire-job.md:159` ("he offers his pass-amulet and Amath's schedule for his life before anyone asks"); `10-manshoons-zhentarim.md:7` |
| 13 | L25 | "**Relationships.** Agorn is a Manshoon lieutenant and bard, the partner of Amath Sercent, whom he visits at Yellowspire in the evenings, a pass-amulet holder for Kolat Towers, and a man whose mother lives in Mistshore and knows nothing about any of this." | Day-one, except "knows nothing about any of this" reads as a quest-time state (D1). "whom he visits at Yellowspire in the evenings" is backed by the quest file | Partner: `org 09:103`, `08-amath:25`, `castle-ward.md:82`; mother: `adventure-wdh.json:7599`; visits: `ev-01-the-yellowspire-job.md:159` |
| 14 | L29 | "A bard who attends the theater, keeps excellent company, and does occasional work he does not discuss. He carries himself as though the situation is never quite as bad as others seem to think." | Day-one OK | Theater: `sources/adventure-wdh.json:9133`; the rest is the page's own |

**Routing for the quest-time sentences (rows 4, 9, 12, 13)**
- `campaign/guides/factions/10-manshoons-zhentarim.md:7`: "Every lieutenant carries a pass-amulet to Kolat Towers and will try to destroy it if capture seems certain, except Agorn, who trades his to save himself."
- `campaign/guides/factions/10-manshoons-zhentarim.md:45`: "**Escalation:** Manshoon moves to Suspicious (Tier 2) if the Interrogation House has not yet been hit; moves to Lockdown (Tier 4) if it has. Agorn carries word to surviving Zhentarim contacts if he escapes; response teams redeploy within 3 days. **Founders' Day Clock: 3–5 days.**"
- `campaign/guides/factions/10-manshoons-zhentarim.md:69`: "- Threatening Agorn Fuoco: he sells out Amath Sercent to save himself (Response Team: Agorn Fuoco)"
- `campaign/guides/factions/10-manshoons-zhentarim.md:77`: "- Capturing Agorn Fuoco: he barters his pass-amulet (Response Team: Agorn Fuoco)"
- `campaign/guides/factions/10-manshoons-zhentarim.md:43`: "**Roster:** Amath Sercent (**priest**) + 4 **acolytes**. Agorn Fuoco is present from dusk to midnight, when he reports to Amath; casing the tower for one evening reveals the pattern."
- `campaign/structure/arc-e-faction-outposts.md:223`: "*Step 2 — Case the Target.* Use the Winter Old Tower layout (DH p. 79). Amath Sercent (priest) occupies the tower with four acolytes. Agorn Fuoco is present on a one-in-three chance." (quoted in part; the sentence is complete)
- `campaign/structure/arc-e-faction-outposts.md:231`: "*Step 5 — Getaway.* Amath fights with conviction; acolytes are less committed. Agorn flees. **Escalation: Manshoon moves to Suspicious (Tier 2) if the Interrogation House has not been hit; moves to Lockdown (Tier 4) if it has.** Agorn carries word to surviving Zhentarim contacts if he escapes. Response teams redeploy within 1d4 days."
- `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:157-159`: the Agorn entry (quoted in B). Line 265: "The ledger lists every carrier of a pass-amulet by name, the day each amulet was last refreshed and where each carrier hands it on. It names three carriers: Avareen Windrivver, who works from a house in Brindul Alley; Agorn Fuoco, who visits Yellowspire on some evenings; and the field crews that Vevette Blackwater sends out from Kolat Towers." Line 334: "A clean exit means that neither the circle pulse nor Amath's coin fired, no acolyte saw the intruders, and Agorn Fuoco did not escape." Line 419: "**Yellowspire Alarm Sounded** — mark when the circle pulse fired, Amath dropped a coin, Agorn escaped, or Amath or an acolyte survived and reported; read by **Kolat Towers** Scene 3 (Manshoon's escalation tier is at least Suspicious) and by the **Manshoon's Zhentarim** Factions Guide page."
- `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/overview.md:79`: "- **Agorn Fuoco** (Manshoon's Zhentarim): a bard who visits some evenings and trades his pass-amulet for his life."
- `campaign/guides/gm-guide/running-the-villains.md:50`: "| **Manshoon's Zhentarim** | Normal operations | Flying snake courier network active; Agorn Fuoco and Avareen Windrivver file field reports. Urstul Floxin reviews them | Agorn Fuoco or Vevette Blackwater's team; orders are to capture, not kill | Urstul Floxin's team if the others fail; Manshoon issues personal directives by flying snake. Manshoon's simulacrum engages; Sidra Romeir locks down Kolat Towers |"
- Mother scene and Stone hand-off: `sources/adventure-wdh.json:7598-7655` (Mistshore, the "Mother and Son" entry, page 68) and `:9115-9152` (Theater, page 76). No campaign quest file holds these scenes. The campaign's Stone chain is not yet a quest (see D3).
- Kolat Towers E8: `sources/adventure-wdh.json:30120`, `:30130`, `:30139` (quoted in A1, A5 and B), `campaign/structure/arc-i-kolat-towers.md:156` (via `docs/plans/setting-compendium-research-notes/pass6/manshoons-zhentarim/03-vevette-blackwater.md:337`; not re-read here)

---

## D. Conflicts

Rank used: campaign files first, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.

**D1. The mother: alive in Mistshore (campaign) against "murdered his own mother" (Alexandrian) and "trying to smother his bedridden mother" (adventure)**
- Campaign, higher: "a man whose mother lives in Mistshore and knows nothing about any of this." — `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:25`
- Adventure: "Agorn has come to Mistshore to visit a member of his actual family-his mother, who is gravely ill and lives in abject poverty." — `sources/adventure-wdh.json:7599`; "trying to smother his bedridden mother, Marta" — `:7634`
- Alexandrian: "In fact, he believed it so much that he murdered his own mother in order to "escape" her poverty." — `sources/6. Faction Response Teams.pdf`, printed p.55 [PDF p.7] **[image transcription]**
- Wiki: "he tried to kill the woman in order to cut all his ties to his old family." — `wiki05:72`
- Higher source: the campaign (mother alive, living in Mistshore). The attempt and the death are quest-time or past-tense claims that no campaign file adopts. The page keeps the campaign line. The mother's name "Marta" comes from the adventure only.

**D2. "Partner" (campaign) against "friends" (Alexandrian and an old campaign copy)**
- Campaign, higher: "Agorn is a Manshoon lieutenant and bard, the partner of Amath Sercent" — `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:25`
- Alexandrian: "Agorn is friends with Amath Seccent (see Yellowspire in Part 3B: Faction Outposts), but he will gladly sell her out, too, revealing the existence of the teleportation circle in Yellowspire." — `sources/6. Faction Response Teams.pdf`, printed p.55 [PDF p.7] **[image transcription; the Alexandrian spells the name "Seccent"]**
- Old campaign copy: "Friends with Agorn Fuoco, who visits when he wants company." — `docs/plans/setting-compendium-research-notes/pass2/batch-f-kelemvor-myrkul-jergal-bane-cyric.md:542` (quoting a retired version of `09-manshoons-zhentarim.md`); the org page's draft note says it was replaced (`organizations/09-manshoons-zhentarim.md:160`).
- Higher source: the campaign ("partner"). The Alexandrian "friends" and the spelling "Seccent" are the outlier.

**D3. The Stone of Golorr: with Agorn and Amath (adventure, wiki) against with Dalakhar until Ches 22 (campaign)**
- Adventure: "Vevette takes a seat behind them and surreptitiously passes the {@item Stone of Golorr|WDH} to Agorn." — `sources/adventure-wdh.json:9133`; "to whom he entrusted the Stone of Golorr" (Amath) — `:7635`
- Wiki: "However, Agorn entrusted the ''Stone'' to his girlfriend [[Amath Sercent]]." — `wiki05:70`
- Campaign, higher: "Dalakhar, the agent of Dagult Neverember, has the Stone and is carrying it toward Trollskull Manor. Urstul Floxin's Zhentarim cell is tracking him." — `campaign/setting/history/08-the-players-arrive.md:24`; "By the morning of Ches 22 Dalakhar has the Stone of Golorr and is carrying it to Trollskull Manor, where he means to deliver it to the party." — `campaign/setting/history/08-the-players-arrive.md:56`
- Higher source: the campaign. No day-one Agorn or Amath text may give them the Stone. The page does not mention the Stone, which is correct. An older pass 2 copy of the Amath page said "holds the Stone of Golorr" (`docs/plans/setting-compendium-research-notes/pass2/batch-f-kelemvor-myrkul-jergal-bane-cyric.md:505`); the current `castle-ward.md:82` does not.

**D4. Stat block: "Performer" (campaign page) against "has no stat block" (quest file), "bard" (Alexandrian, adventure, wiki)**
- Campaign page: "Stat block: **Performer**." — `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:5`
- Quest file: "He never fights and has no stat block, and he flees the moment a fight starts." — `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:159`
- Alexandrian: "Stats: NE male Turami bard (DH p. 195)" — `sources/6. Faction Response Teams.pdf`, printed p.55 [PDF p.7] **[image transcription]**
- Adventure: "{@creature bard|VGM}" — `sources/adventure-wdh.json:9133`
- Wiki: "| class5e        = [[Bard]]" — `wiki05:59`
- Session record: "Kalain, Mattrim, Variel, Agorn and Margo on Performer stat blocks" — `session 51 handoff.md:24`
- Not a fact conflict in the campaign's own terms: the page says Performer and the quest says no stat block. The orchestrator decides which label stays. The Performer label is the campaign's 2024 choice (session 51), and no source gives a Performer stat block for Agorn.

**D5. Pass-amulet (campaign, Alexandrian) against ring (structure doc)**
- Campaign, higher: "Every lieutenant carries a pass-amulet to Kolat Towers" — `campaign/guides/factions/10-manshoons-zhentarim.md:7`
- Alexandrian: "All of Manshoon's lieutenants carry pass-amulets to Kolat Towers (see Part 4), but will attempt to destroy them if it looks as if they are being captured. (Except Agorn, that feckless weasel, who will attempt to barter it for his own life.)" — `sources/6. Faction Response Teams.pdf`, printed p.55 [PDF p.7] **[image transcription]**
- Structure doc (quoted through `03-vevette-blackwater.md:337`, not re-read here): "he offers his ring (he carries one)" — `campaign/structure/arc-i-kolat-towers.md:156`
- Higher source: the campaign (pass-amulet). The structure doc's "ring" is the outlier.

**D6. Presence at Yellowspire (quest file, Factions Guide) against "one-in-three" (structure doc)**
- Quest file, higher: "He visits on those evenings to see Amath." and "is in the tower only if the party enters during working hours after dusk" — `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:159`
- Factions Guide: "Agorn Fuoco is present from dusk to midnight, when he reports to Amath" — `campaign/guides/factions/10-manshoons-zhentarim.md:43`
- Structure doc: "Agorn Fuoco is present on a one-in-three chance." — `campaign/structure/arc-e-faction-outposts.md:223`
- Higher source: the quest file and the Factions Guide. The structure doc is stale (the session 28 handoff already flagged the dice: "Agorn's "one-in-three chance"", `session 28 handoff.md:172`).

**D7. Who carries the *Report to Agorn Fuoco* (campaign against Alexandrian)**
- Campaign, higher: "- *Report to Agorn Fuoco* (Response Team: Agorn Fuoco — names Orb Confectioners on Rising Ride)" — `campaign/guides/factions/09-xanathars-guild.md:95`
- Alexandrian revelation list: "Report to Agorn Fuoco (Response Team: Vevette Blackwater)" — `sources/17. Outpost and Lair Revelation Lists.pdf`, printed p.123 [PDF p.3] (quoted through `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/10-korgstrod-uxgulm.md:309`; not re-read here)
- Higher source: the campaign. The Alexandrian is the outlier on which team carries it.

**D8. Agorn's command (adventure) against the campaign's field-team roles**
- Adventure: "while Agorn commands those who oppose the Zhents that aren't loyal to {@creature Manshoon|WDH}." — `sources/adventure-wdh.json:30130`
- Campaign: "in the published adventure Agorn Fuoco leads those that fight the Zhents who are not loyal to Manshoon (**Vevette Blackwater**; *Dragon Heist*, 5e)." — `campaign/setting/organizations/09-manshoons-zhentarim.md:58`; the Factions Guide gives the Alert role as "Agorn or Vevette's team; orders are to capture, not kill" (`campaign/guides/factions/10-manshoons-zhentarim.md:53`)
- Higher source: the campaign page keeps the adventure line with a tag (`09-manshoons-zhentarim.md:181`). The NF page does not say he commands anything. This is not a conflict for the Notable Figures page, but the drafter must not give him a command role as a day-one fact.

**D9. Coward, flight and self-preservation (no conflict; all three agree)**
- "hollow coward" — `campaign/setting/organizations/09-manshoons-zhentarim.md:99`
- "feckless weasel" — `sources/6. Faction Response Teams.pdf`, printed p.55 **[image transcription]**
- "flees the moment a fight starts" — `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:159`

---

## E. Stale lines in other files (not to be edited) and routed references

### E1. Old copies and pass 2 notes (not campaign files)
- `docs/plans/setting-compendium-research-notes/pass2/batch-f-kelemvor-myrkul-jergal-bane-cyric.md:505`: "> "> - Amath is a priest of Bane allied with Manshoon's Zhentarim, and she keeps the teleportation circle to Kolat Towers. She is the partner of Agorn Fuoco and holds the Stone of Golorr."" (the current `castle-ward.md:82` does not say "holds the Stone of Golorr")
- `docs/plans/setting-compendium-research-notes/pass2/batch-f-kelemvor-myrkul-jergal-bane-cyric.md:542`: "Friends with Agorn Fuoco, who visits when he wants company." (a retired org-page line)
- `docs/plans/setting-compendium-research-notes/pass2/batch-f-kelemvor-myrkul-jergal-bane-cyric.md:623`: "6. Campaign (`campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:26`): "**Relationships.** Agorn is a Manshoon lieutenant and bard, the man who entrusted the Stone of Golorr to Amath Seccent, a pass-amulet holder for Kolat Towers, and a man whose mother lives in Mistshore and knows nothing about any of this."" (a retired version of the page's Relationships, with the Stone; the current line 25 does not have the Stone)
- `docs/plans/setting-compendium-research-notes/pass5/zhentarim.md:136`: "Urstul, Sidra and Agorn carry the revelation-list items named in the Factions Guide (Section 5)." (the pass 6 Sidra note says the claim is not supported; not an NF fact)

### E2. Campaign files that show Agorn in the wrong place or with the wrong status
- `campaign/structure/arc-e-faction-outposts.md:223` (one-in-three, D6) and `:231` (Agorn flees; carries word). Structure doc, quest content.
- `campaign/structure/arc-i-kolat-towers.md:156` (ring, D5; the E8 Reading Room). Not re-read here.
- `campaign/structure/arc-i-kolat-towers.md:180`: "External reinforcements — Agorn's team or replacement spy + 4 thugs — arrive at the perimeter with fresh pass-amulets. The party is fighting the entire remaining Splinter cell." Quest content.
- `campaign/structure/arc-i-kolat-towers.md:320`: "- **Notable Figures** — Existing profiles: Manshoon, Sidra Romeir, Manafret Cherryport, Vevette Blackwater, Agorn Fuoco, Urstul Floxin, Lady Gondafrey, Skeemo Weirdbottle. New profiles needed: Kaevja Cynavern, Havia Quickknife, Mookie Plush, Yorn the Terror." (the profile exists; the structure note is out of date)
- `campaign/guides/gm-guide/running-the-villains.md:71`: "Agorn Fuoco monitors Orb Confectioners. Xanathar suspects a mole; it's hunting in the wrong direction." (a campaign escalation row, quest-era state)
- `campaign/quests/faction-events/lords-alliance/r25-warduke/ev-01-warduke.md:197`: "| The Splinter | Second | A lieutenant who talks and three or four hired hands, with orders to take prisoners | Agorn Fuoco's crew |" (a quest file)
- `campaign/quests/faction-events/doom-raiders/r03-wolf/ev-01-wolf.md:126` (quoted through `03-vevette-blackwater.md:353`, not re-read here): "Once either outcome is marked, the swashbuckler is Vevette Blackwater, the bard is Agorn Fuoco and the assassin is Urstul Floxin, and the answer names them."
- `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:419` and `ev-02-the-debrief.md:23` (quoted in C): the Yellowspire outcomes (quest state).

### E3. Routed to quests (where the quest-time facts already live)
- Capture and pass-amulet barter: `campaign/guides/factions/10-manshoons-zhentarim.md:7`, `:69`, `:77`; `campaign/structure/arc-e-faction-outposts.md:231`; Alexandrian `sources/6. Faction Response Teams.pdf` printed p.55 **[image transcription]**.
- Yellowspire raid and the Doom Raiders mission "The Yellowspire Job": `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:157-159`, `:265`, `:334`, `:392`, `:419`; `ev-02-the-debrief.md:23`; `overview.md:64`, `:79`.
- Mistshore and the Fuoco residence, the theater hand-off: `sources/adventure-wdh.json:7598`-`:7655` and `:9132`-`:9152`. No campaign file routes these. Flag for the Dragon Heist-chain conversion.
- Kolat Towers E8, the Reading Room: `sources/adventure-wdh.json:30120`, `:30130`, `:30139`; `campaign/structure/arc-i-kolat-towers.md:156`.
- Appendix mentions (not facts for the page): `sources/Appendix_B_-_Player_Factions.md:658` ("**Neutralize a named Manshoon operative (+2).** Eliminate or capture one of Manshoon's lieutenants — Urstul Floxin, Vevette Blackwater, Agorn Fuoco, or any other named agent."); `sources/Appendix_D_-_Running_the_Tavern.md:1549` ("Agorn Fuoco may arrive as a secondary contact, especially if Vevette has already been neutralized.")
- Adventure Kolat Towers encounter odds: `sources/adventure-wdh.json:13479` ("There's a {@chance 50|50 percent chance} that these Zhents are led by one of {@creature Manshoon|WDH}'s lieutenants, either Vevette Blackwater or Agorn Fuoco, if they're still alive (see chapter 8, {@area E8|425}).")

### E4. Other day-one and cross-reference lines (keep them)
- `campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md:25` (quoted in A4).
- `campaign/gazetteer/waterdeep/castle-ward.md:77`: "- Amath Sercent (Lawful Evil, Mulan Human, she/her), a well-mannered woman in common clothes, keeps the tower with four followers, and visitors find them at ease with the handprints."
- `campaign/gazetteer/waterdeep/castle-ward.md:82` (quoted in A4).
- `campaign/setting/deities/bane.md:84` (quoted in A6).
- `campaign/setting/deities/bane.md:119`: "- **Amath Sercent**, **Agorn Fuoco**, **Manshoon**, **Davil Starsong**, **Tashlyn Yafeera** (Notable Figures): the people tied to Yellowspire."
- `campaign/setting/deities/milil.md:116` (quoted in A6).
- `campaign/setting/villains/manshoon.md:116`: "- **Manshoon**, **Urstul Floxin**, **Sidra Romeir**, **Vevette Blackwater**, **Agorn Fuoco**, **Avareen Windrivver**, **Jelenn Urmbrusk** and **Davil Starsong** (Notable Figures): profiles for the Relationships table and the notes"
- `campaign/setting/organizations/09-manshoons-zhentarim.md:8`: "> - **Contacts:** **Avareen Windrivver**, **Agorn Fuoco**, **Vevette Blackwater** (field operatives); **Sidra Romeir** (Kolat Towers)"
- `campaign/setting/organizations/09-manshoons-zhentarim.md:152` (cross-reference list): "- **Manshoon**, **Urstul Floxin**, **Sidra Romeir**, **Vevette Blackwater**, **Agorn Fuoco**, **Avareen Windrivver**, **Amath Sercent** (Notable Figures): the principal members"

### E5. Source guide
- `sources/SOURCE_GUIDE.md:35`: "- **Chapter 8 — Face of the Enemy (Manshoon/Zhentarim):** Kolat Towers keyed location (22 areas, force field mechanics, pass-amulet system, teleporter signet rings) and the Extradimensional Sanctum (13 areas, Manshoon's personal stronghold). Contains: Manshoon, his simulacrum, Sidra Romeir, Manafret Cherryport, Vevette Blackwater, Agorn Fuoco, Urstul Floxin."

---

## F. Gaps (what a Background would need that no source gives)

1. **Birth and childhood.** No source gives a birthplace or a childhood. The wiki gives "home" as "Waterdeep, Sword Coast North" (`wiki05:11`). The adventure says only that he "used to live and play music in Mistshore" (`sources/adventure-wdh.json:7625`), and the wiki says "Agorn lived and played music in Mistshore" (`wiki05:65`).
2. **Age.** No source gives an age. The adventure index, the wiki infobox (the `age` field is blank in `wiki05`, lines 17-18 of the Read output) and the Alexandrian give none.
3. **Father.** No source names him. The wiki gives the mother only: "| parents        = [[Marta Fuoco]]" (`wiki05:29`).
4. **How he joined the Zhentarim.** The wiki says he "decided to devote himself to the Zhentarim" (`wiki05:68`), with no date, place or recruiter.
5. **The rise.** "Quickly" is the only word (`sources/adventure-wdh.json:7599`; `campaign/setting/organizations/09-manshoons-zhentarim.md:71`). No rung, year or sponsor.
6. **Time in post.** No source.
7. **The mother's state on Ches 1.** The campaign says she "lives in Mistshore" (`campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:25`). The adventure says "gravely ill" and "bedridden" (`sources/adventure-wdh.json:7599`, `:7634`). No source dates either state. The Alexandrian says he killed her (D1). The Background must not say she is dead, and must not give her a date of illness.
8. **Music training and career.** The adventure says only that he "used to live and play music in Mistshore" (`:7625`) and that he "strums a lyre" (`:30120`). The quest file gives a lute (`ev-01-the-yellowspire-job.md:159`). No training, teacher, troupe or performance date is given.
9. **The Tamzyn letters.** "Tamzyn" appears only in the chest entry (`sources/adventure-wdh.json:30222`). No source says who Tamzyn is. Do not name her as a Notable Figure (brief ruling 17). A nameless admirer is allowed.
10. **Amath's history with him.** "lady friend" (`:7635`), "girlfriend" (`wiki05:70`), "partner" (`campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:25`). No source gives how they met or how long they have been together.
11. **Faith.** None. The Milil page names no worship (`campaign/setting/deities/milil.md:116`).
12. **"Mama".** The voice profile gives "He calls his mother "Mama"" (`.claude/skills/character-voices/voices/manshoons-zhentarim.md:90`) and the signature line "Mama will be so upset." (`:94`). No source names the mother's pet name. The drafter keeps it as the voice profile's own (a voice choice, not a fact), and lists it as unsourced.
13. **Where he sleeps.** "all sleep here" (`sources/adventure-wdh.json:30212`), in a Kolat Towers room whose area ID is not read here.
14. **Pass-amulet acquisition.** No source gives how or when he got it.
15. **Why Manshoon trusts him.** The campaign says only "His lieutenants rise by impressing him" (`organizations/09-manshoons-zhentarim.md:71`). No specific act is given.
16. **Stat label.** Performer (campaign page) against no stat block (quest file) (D4).
17. **Relationship with Vevette.** Shared duty only (`sources/adventure-wdh.json:30130`). No friendship or rivalry given.
18. **Pronunciation.** Given: "AY-gorn foo-OH-koh" (`sources/adventure-wdh.json:41-42`).

---

## G. Inner-life hints (exact quotes; do not contradict)

**Mother, the one person he visits and cares for**
> "Agorn has come to Mistshore to visit a member of his actual family-his mother, who is gravely ill and lives in abject poverty." — `sources/adventure-wdh.json:7599`
> "deep filial attachment to his mother." — `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:13`
> "wry surprise when his mother appears and he becomes, briefly, comprehensible." — `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:11`
> "a man whose mother lives in Mistshore and knows nothing about any of this." — `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:25`

**The break with the family (quest-time; the Background may note the tension, not the attempt)**
> "With tears born of joy and sadness streaming down his face, Agorn is cutting loose his old family ties and embracing his new family: the Zhentarim." — `sources/adventure-wdh.json:7634`
> "Afterward, Agorn went to meet his mother and, inspired by the theater's play and by Amath, he tried to kill the woman in order to cut all his ties to his old family." — `wiki05:72`

**Ambition, not fulfilled**
> "Agorn dreamed of becoming a famous bard but he had no success so he decided to devote himself to the Zhentarim, quickly advancing through the ranks." — `wiki05:68`
> "He has not achieved the fame he craved nor earned the wealth he felt he was entitled to." — `sources/adventure-wdh.json:7599`
> "genuine love of music that sits embarrassingly alongside everything else" — `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:13`
> "Deep down, he would rather be playing music." — `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:21`
> "eventually retire somewhere quieter." — `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:15` (a day-one personal goal already on the page)

**The Zhentarim as family and creed**
> "He has adopted the Zhentarim credo that power comes to those who deserve it and has come to see the Black Network as a new family of sorts." — `sources/adventure-wdh.json:7599`
> "Agorn was one of the lieutenants of Manshoon" and "who was very impressed by him." — `wiki05:75` (the wiki's sentence is one line; split only at the citation tags)
> "Vevette and Agorn are two of {@creature Manshoon|WDH}'s most trusted followers." — `sources/adventure-wdh.json:30130`

**Amath (the one partner)**
> "Agorn Fuoco is her romantic partner and visits her there in the evenings." — `campaign/setting/organizations/09-manshoons-zhentarim.md:103`
> "Agorn was moved to perpetrate this act by the play he saw at the theater and by his lady friend, Amath Sercent" — `sources/adventure-wdh.json:7635` (quest-time)

**Music and the theater**
> "Agorn lived and played music in [[Mistshore]]." — `wiki05:65`
> "The children know who Agorn Fuoco is because he used to live and play music in Mistshore." — `sources/adventure-wdh.json:7625`
> "Agorn strums a lyre." — `sources/adventure-wdh.json:30120`

**Self-preservation and fear (day-one attitude; the acts are quest-time)**
> "Agorn Fuoco would trade whatever he knows to save himself." — `campaign/setting/organizations/09-manshoons-zhentarim.md:43`
> "Deep down, he would rather be playing music." (see above)
> "In a fight, Agorn attempts to flee immediately." — `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:23`
> "He carries himself as though the situation is never quite as bad as others seem to think." — `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:29`

**Wants**
> "use whatever he knows (Amath's identity, his pass-amulet, Manshoon's operational structure) to buy his freedom, and eventually retire somewhere quieter." — `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:15`

**Must not contradict**
- Alive mother in Mistshore on Ches 1 (campaign, D1).
- Partner of Amath Sercent (campaign, D2).
- Not holding the Stone on Ches 1 (campaign, D3).
- Neutral evil, Turami human, he/him (B).
- Not a combatant; flees (campaign, quest file, D4).
- Names no deity (`campaign/setting/deities/milil.md:116`).

---

## Not readable

- `sources/6. Faction Response Teams.pdf` p.55 (printed p.55, PDF p.7) was read as a rendered page image. Its quotes are transcriptions. Check them with `pdftotext -layout` before prose use.
- `sources/12. Lair  Zhentarim – Kolat Towers.pdf` pp.94-95 and `sources/17. Outpost and Lair Revelation Lists.pdf` p.123 were not re-read here. Their lines are cited through earlier pass 6 notes and marked "not re-read here".
- `sources/Other remix files/*.docx` were not searched. `SOURCE_GUIDE.md` does not list one for Agorn.

## Not run
- `voicecheck.py` was not run (research only).
- The page was not written. No file was edited except this notes file.
