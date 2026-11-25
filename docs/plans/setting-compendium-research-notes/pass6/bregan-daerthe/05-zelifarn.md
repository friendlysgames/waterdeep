# Pass 6 research notes: Zelifarn

Page: `campaign/setting/notable-figures/bregan-daerthe/05-zelifarn.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Model format: `docs/plans/setting-compendium-research-notes/pass6/cassalanters/04-osvaldo-cassalanter.md`
Rulings used: Ches 1, 1492 DR (day one). Campaign-start rule (ruling 1). User ruling on Key Members (Brief, "Key Members labels"): keep Zelifarn on `campaign/setting/organizations/07-bregan-daerthe.md` under Key Members, keep the page's own "None (friendly to Bregan D'aerthe; not an operative)" label, and note the looser tie. User ruling: the crystal ball moral thread belongs to **Sea Maidens Faire** (routed in section E).

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines. Where a quote is a paragraph inside a quest journal, the line number is the line the sentence starts on.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes (`\"`) are shown as plain quotes. Tags such as `{@creature ...}` and `{@i ...}` are left as written.
- Alexandrian PDF: `sources/9. Lair – Sea Maidens Faire.pdf` was read with the Read tool's `pages` parameter, PDF pages 1 to 7 (printed pp.68 to 74). Zelifarn's section is PDF p.4 (printed p.71). Area U4 is PDF p.6 (printed p.73). This session has no shell, so `pdftotext` could not run. The PDF quotes are transcriptions from rendered page images and must be checked with `pdftotext -layout` before any quote goes into prose. PDF pages 8 onward were not read.
- Alexandrian markdown: `sources/Appendix_C_-_Player_Faction_Missions.md` (lines 1728 to 1781) and `sources/Appendix_B_-_Player_Factions.md` (line 937).
- Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-bregan-daerthe/05-zelifarn.txt`. Quoted as "wiki line N" (that file's lines). Citation key: `WDH5e-p91` (*Waterdeep: Dragon Heist*, 5e) and `MM5e-p108` (*Monster Manual*, 5e). The wiki's own infobox gives 5e values only.
- Pass 4 and pass 5 research bundles were searched. `sources/research/pass4-bundles/jarlaxle/campaign-hits.txt` is out of date (it quotes older lines of `bahamut.md` and `trades-ward.md`). It is not used here. No bundle holds a Zelifarn fact that is not already quoted below.
- Not opened: `sources/Vajra Safahr, Zelifarn, and Deepwater Harbor quests.docx` (listed at `sources/SOURCE_GUIDE.md:696`). See section F and the report's Not readable list.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **Zelifarn's tenure in the harbor has four values and no day-one date.** Force Grey says he has lived there "about three tendays" (`campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:18`). The Force Grey design notes list "Zelifarn's three tendays in the harbor" as **Invented** (`.../m02-the-dragon-in-the-harbor/design-notes.md:19`). `campaign/structure/arc-h-sea-maidens-faire.md:19` says he took up residence "within days of the Sea Maidens Faire's arrival on Ches 21", which is after day one. The published adventure says "recently moved into Deepwater Harbor" and "the past several months" (`sources/adventure-wdh.json:26604`). The wiki says he "had moved to the harbor in the late 15th century DR" (wiki line 70). The Background needs one value, and the drafter must decide it with the orchestrator.
2. **The campaign's own sources disagree on whether Zelifarn knows who killed his mother.** `arc-h-sea-maidens-faire.md:19` says the killers were "agents whose employers Zelifarn had not yet identified". `arc-h-sea-maidens-faire.md:117` says "Zelifarn does not know this when the party first engages him for assistance on this quest." `arc-h-sea-maidens-faire.md:394` says "killed by Jarlaxle's agents". The Alexandrian PDF (p.71) says "Jarlaxle and his agents killed his mother, Asphosis" and "Zelifarn knows that Jarlaxle keeps it in the *Scarlet Marpenoth*". The mother's death and the crystal ball are routed to **Sea Maidens Faire** (section E). Only the pre-campaign fact of the death belongs on the page, and the campaign files do not date it.
3. **The crystal ball's room is in dispute.** `arc-h-sea-maidens-faire.md:19`, `:117` and `:394` say U4. The Alexandrian PDF (p.73) says "Area U4 – Jarlaxle's Stateroom ... a crystal ball sits upon a plush cushion". The campaign location file says the bronze crystal ball is in U7a: "U7a contains Jarlaxle's fallback position chair, a bronze periscope, and a bronze crystal ball on a teak stand" (`campaign/locations/sea-maidens-faire/05-scarlet-marpenoth.md:19`). Route to Sea Maidens Faire.
4. **"Friendly terms with the crew" conflicts with the Force Grey mission.** The page says he is "on friendly terms with the *Eyecatcher*'s crew" (line 25). `ev-01-the-dragon-in-the-harbor.md:22` says "The Faire's deck watch has fired crossbows near him to drive him off." The published adventure says "His attempts to treat with the crew have met with no success" (`sources/adventure-wdh.json:26604`). The campaign file wins, but the page and the mission need the same wording.
5. **Two voice lines conflict with the page.** Line 106 of the voice doc says "He waves with a flipper". The adventure says "raises a claw in a small wave" (`sources/adventure-wdh.json:26601`), and Force Grey says "he claps his claws together" (`ev-01-the-dragon-in-the-harbor.md:272`). Line 112 says "I'm telling the captain!" The page says "he does not report to Jarlaxle or anyone else" (line 21). Who "the captain" is in that line is not stated.
6. **The affiliation label** follows the user's ruling on Key Members (Brief, "Key Members labels"). The page's own line 6 reads "None (friendly to Bregan D'aerthe; not an operative)". The organization page lists him under Key Members (`campaign/setting/organizations/07-bregan-daerthe.md:103`) and notes the looser tie (`:184`). `campaign/setting/deities/bahamut.md:129` cites the affiliation at `05-zelifarn.md:7`, which is the Featured-in line. The correct line is 6 (stale citation, not edited).
7. **Overview length.** The Overview (line 29) is one sentence of 34 words, counted by hand. The brief limit is 21 words per sentence.

---

## A. Background facts by theme

### A1. Origin, birth and kind (no birth, hatching or birthplace in any source)

Species and kind, the wiki's infobox and lead:

> `| race           = [[Bronze dragon]]`
> — wiki line 14 (`WDH5e-p91`)

> `'''Zelifarn''' was a friendly [[bronze dragon]] who lived in [[Deepwater Harbor]] in [[Waterdeep]] in the late 15{{th}} century [[DR]].<ref name="WDH5e-p91" /><ref name="WDH5e-p36">{{Cite book/Waterdeep: Dragon Heist|36}}</ref><ref name="WDH5e-p145">{{Cite book/Waterdeep: Dragon Heist|145}}</ref>`
> — wiki line 64 (5e)

Age class, wiki infobox:

> `| age            = [[Dragon aging|Young]] in {{Yearlink|1492}}{{Waterdeep-time}}`
> — wiki line 17 (5e)

Age in years, campaign (quest structure, present tense, used as a day-one age):

> "Zelifarn was twenty-two years old, enthusiastic about ships, curious about everything, and growing suspicious that the Eyecatcher had a second hull."
> — `campaign/structure/arc-h-sea-maidens-faire.md:19`

Published adventure, the dragon's look and speech (no age given):

> "In the water ahead, a large shape speeds toward you. As it gets closer, you recognize it as a dragon with bronze-colored scales. Slewing to a stop, the creature gives a toothy grin, then raises a claw in a small wave. \"Well met!\" it chirps."
> — `sources/adventure-wdh.json:26601` (insetReadaloud, "The Friendly Dragon", page 145)

### A2. Arrival and tenure in Deepwater Harbor (conflicting; see Findings 1 and D2)

Published adventure:

> "Zelifarn, a {@creature young bronze dragon}, recently moved into Deepwater Harbor. He has spent the past several months scouring wrecks at the bottom of the harbor for treasure and stashing precious baubles in a hidden underwater cave. Recently, he noticed a strange craft mounted on the underside of the {@i Eyecatcher}. His attempts to treat with the crew have met with no success, but he's curious to know more. Since the characters appear to be headed toward a rendezvous with the {@i Eyecatcher}, Zelifarn would like them to find out all they can about the underwater vessel without raising suspicion. The dragon promises to meet them again after they have completed their mission. In exchange for information, he offers to give the party a barnacle-covered chest that he found recently. He hasn't opened it yet, so its contents are unknown to him, but he can smell gold inside."
> — `sources/adventure-wdh.json:26604` (page 145, "Special Events")

Wiki:

> "Zelifarn had moved to the harbor in the late 15{{th}} century DR. As of the {{YearlinkName|1492}},{{Waterdeep-time}} he spent most of his time searching shipwrecks at the bottom of the harbor in search for treasure. He stashed all his findings in a secret underwater cave."
> — wiki line 70 (5e, `WDH5e-p145`)

Campaign, Force Grey mission (quest journal; the duration is listed as Invented in the design notes):

> "Zelifarn is a Young Bronze Dragon who has lived in Deepwater Harbor for about three tendays. He scours the wrecks on the harbor floor and keeps what he finds in a cave beneath the elvish wreck."
> — `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:18`

> "Zelifarn is a young bronze dragon who has lived in Deepwater Harbor for about three tendays, scouring the wrecks on the harbor floor and keeping what he finds in a cave beneath an elvish wreck forty feet down. Captains and churches leave offerings for Umberlee at the deep moorings, and Zelifarn took them because nobody was guarding them and he believed they were abandoned."
> — `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/overview.md:21`

> "- Invented: the offerings (fourteen cups, three casks, six candle jars and a bell, about 400 gp), the cave under the wreck's bow, Zelifarn's three tendays in the harbor, and his rowboat measures for the vessel. The 80-foot, 20-foot size comes from the Sea Maidens Faire location notes."
> — `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/design-notes.md:19`

Campaign, a message in the mission (the speaker is not named in the excerpt):

> "> > Vajra has had sailors reporting a bronze dragon outside the Dragonward for a tenday now, and I'd say it's worth asking whether that dragon is your thief."
> — `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:73`

> "> > Renaer sent word ahead that the Queenspire has lost its offerings. A bronze dragon has sat outside the Dragonward for a tenday, and I think those are one problem. Find out whether the dragon is your thief and what else it has seen."
> — `.../ev-01-the-dragon-in-the-harbor.md:95`

Campaign, Sea Maidens Faire (quest structure; the arrival is dated after Ches 21):

> "The young bronze dragon had taken up residence near an old elvish wreck in Deepwater Harbor within days of the Sea Maidens Faire's arrival on Ches 21."
> — `campaign/structure/arc-h-sea-maidens-faire.md:19`

Ward: the Dock Ward gazetteer places the harbor:

> "The ward lies on Deepwater Harbor."
> — `campaign/gazetteer/waterdeep/dock-ward.md:22`

### A3. Family: his mother Asphosis and her hoard (pre-campaign death; the date is not given)

Campaign, Sea Maidens Faire (quest structure):

> "His mother Asphosis had been killed four years earlier by agents whose employers Zelifarn had not yet identified. Her crystal ball — a family heirloom, a masterwork scrying device — had disappeared with her hoard."
> — `campaign/structure/arc-h-sea-maidens-faire.md:19`

> "Zelifarn had no way to know that the crystal ball now sat in U4 controlling nine clairvoyance crystals across Waterdeep. He only knew that something about the Eyecatcher's underside was wrong, and that it scraped against the grief he had been carrying for four years without a name."
> — `campaign/structure/arc-h-sea-maidens-faire.md:19`

Campaign, Sea Maidens Faire, the discovery (routed; see E):

> "Zelifarn also introduces this quest's moral dimension. The crystal ball in U4 — the Nimblewright Crystal Ball that controls Jarlaxle's surveillance network — belonged to Zelifarn's mother Asphosis. Jarlaxle's agents killed Asphosis and took it. Zelifarn does not know this when the party first engages him for assistance on this quest. He discovers it only if the party brings him to U4 or tells him what they found there. His reaction is grief, then cold fury, then a request: \"That was hers. Bring it to me.\""
> — `campaign/structure/arc-h-sea-maidens-faire.md:117`

Alexandrian PDF (transcription; check before quoting):

> "Zelifarn's mother was, in addition to being a dragon, a master crystalmancer. Jarlaxle and his agents killed his mother, Asphosis, and stole from her the special crystal ball that he uses to spy through the nimblewrights. Zelifarn doesn't know exactly what the crystal ball does, but he wants it back so that he can restore his mother's horde. Zelifarn knows that Jarlaxle keeps it in the Scarlet Marpenoth, but hasn't been able to figure out a way to get it by himself."
> — `sources/9. Lair – Sea Maidens Faire.pdf`, PDF p.4 (printed p.71), "The Dragon Zelifarn" section. Transcribed from a rendered page image.

Campaign, Sea Maidens Faire, the moral thread (routed; see E):

> "This quest's moral dimension is smaller in scope but personal — the Nimblewright Crystal Ball in U4 belonged to Zelifarn's mother, killed by Jarlaxle's agents."
> — `campaign/structure/arc-h-sea-maidens-faire.md:394`

> "Zelifarn's reaction to learning the truth should be played for genuine emotion. He is a young dragon — enthusiastic, curious, not yet cynical. Learning that the interesting ship with the funny name was operated by the people who killed his mother is a formative moment."
> — `campaign/structure/arc-h-sea-maidens-faire.md:398`

Search: a `grep` for "Asphosis" over `campaign/`, `sources/*.md`, `sources/*.json` and `.claude/` returned only `campaign/structure/arc-h-sea-maidens-faire.md:19` and `:117`. The Alexandrian PDF (p.4) is the third source. No source gives the mother's family name, any sibling or a mate. The wiki's infobox fields for `parents`, `spouses`, `siblings` and `children` are blank (wiki lines 31 to 35 in that file).

### A4. Character and manner (day-one habits)

Campaign, the Zelifarn page (Emotions):

> "**Emotions.** Zelifarn most often feels bright curiosity, uncomplicated friendliness, genuine interest in surface-world affairs, delight when someone tells him something he did not know, and possessive pride in his stretch of Deepwater Harbor."
> — `campaign/setting/notable-figures/bregan-daerthe/05-zelifarn.md:13`

Wiki (5e, past tense):

> "Zelifarn was very friendly towards strangers, as well as curious and inquisitive. He was eager to add treasure to his hoard, but did not hesitate to offer some of his treasure in exchange for information about his surroundings."
> — wiki line 67 (`WDH5e-p36`, `WDH5e-p145`)

Campaign, Force Grey (a checkable trait):

> "Any character who watches Zelifarn for a few minutes and makes a successful DC 13 Wisdom (Insight) check determines that he is curious, has no wish to hurt anyone and does not understand why people are afraid of him."
> — `.../m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:200`

Alexandrian appendix (Arc FG-2, Scene 1, transcribed in markdown):

> "A young bronze dragon has taken up residence in Deepwater Harbor. It startled some sailors — it surfaced near a fishing boat and one of the crew apparently fainted — but it hasn't hurt anyone."
> — `sources/Appendix_C_-_Player_Faction_Missions.md:1744` (quoted inside the `<p>` tags in the file; the quote marks are the in-world narration)

### A5. The cave and his hoard

> "Zelifarn never lies, does not understand secrets and submerges if he is attacked."
> — `.../m02-the-dragon-in-the-harbor/overview.md:27`

Wiki:

> "He stashed all his findings in a secret underwater cave."
> — wiki line 70

Campaign:

> "...keeping what he finds in a cave beneath an elvish wreck forty feet down."
> — `.../m02-the-dragon-in-the-harbor/overview.md:21` (the sentence in full is quoted under A2)

Adventure (the chest):

> "In exchange for information, he offers to give the party a barnacle-covered chest that he found recently. He hasn't opened it yet, so its contents are unknown to him, but he can smell gold inside."
> — `sources/adventure-wdh.json:26604`

### A6. Relationships (the crew, Jarlaxle, Vajra)

Campaign, the Zelifarn page (Motivations and Persona):

> "**Motivations.** Zelifarn wants to learn about the surface world and the strange ships that pass through his harbor, stay on good terms with the *Eyecatcher*'s crew, whom he finds interesting, and collect specific information in exchange for specific rewards."
> — `campaign/setting/notable-figures/bregan-daerthe/05-zelifarn.md:15`

> "Deep down, he does not report to Jarlaxle or anyone else. He knows the *Eyecatcher* has something under her hull and that her crew discouraged him from looking, but he does not know whose the vessel is."
> — `campaign/setting/notable-figures/bregan-daerthe/05-zelifarn.md:21`

Campaign, Force Grey design notes (the session ruling behind line 21):

> "- The Notable Figures page for Zelifarn and the Bregan D'aerthe organization page now agree with this Event: he is a young bronze dragon in Deepwater Harbor who does not report to Jarlaxle and is not stationed aboard the *Scarlet Marpenoth* (Session 51 ruling)."
> — `.../m02-the-dragon-in-the-harbor/design-notes.md:21`

Campaign, the organization page:

> "- **Zelifarn** — Young bronze dragon, lawful good. Lives in Deepwater Harbor and is on friendly terms with the *Eyecatcher*'s crew. He is not an operative and does not know whose vessel hangs under the *Eyecatcher*. See the **Zelifarn** page in Notable Figures."
> — `campaign/setting/organizations/07-bregan-daerthe.md:103`

Campaign, Force Grey (conflicts with line 25; see D1):

> "The vessel under the *Eyecatcher* is the *Scarlet Marpenoth*, a Bregan D'aerthe submersible about 80 feet long and 20 feet across. Zelifarn does not know whose it is. The Faire's deck watch has fired crossbows near him to drive him off."
> — `.../m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:22`

Wiki, the Gray Hands (wiki only; the campaign does not use this):

> "The dragon's presence did not go unnoticed by sailors traveling through the harbor. In the interest of keeping the harbor safe, a group of [[Gray Hands]] was dispatched by [[Vajra Safahr]] to learn about Zelifarn's true intentions and make sure that he did not represent a threat to the city."
> — wiki line 72 (`WDH5e-p36`)

Campaign, Force Grey's knowledge of him:

> "Vajra knows only that sailors have reported a dragon. She does not know that something is fixed to the keel of the *Eyecatcher*, which Zelifarn has watched since the ship arrived."
> — `.../m02-the-dragon-in-the-harbor/overview.md:23`

Campaign, Lolth check (no tie found):

> "**No tie found:** Zelifarn is a lawful good bronze dragon with no affiliation to Bregan D'aerthe (`05-zelifarn.md:6`), and neither his page nor the Umberlee mission mentions Lolth."
> — `campaign/setting/deities/lolth.md:143`

### A7. Faith and offerings

> "Captains and churches leave offerings for Umberlee at the deep moorings, and Zelifarn took them because nobody was guarding them and he believed they were abandoned."
> — `.../m02-the-dragon-in-the-harbor/overview.md:21`

Note for the drafter: the theft of the offerings is what the party discovers in the Force Grey mission. It is not on the page now, and this section records only the campaign's description of it. See F7.

### A8. Signature belongings

Campaign, the reward chest (the same chest as in adventure 26604; the reward is a trade outcome):

> "**Relationships.** Zelifarn is the young bronze dragon of Deepwater Harbor, on friendly terms with the *Eyecatcher*'s crew but answerable to none of them, and the source of a genuine reward (300 sp, a golden octopus amulet, and a *scroll of revivify*) for parties willing to trade information about the Scarlet Marpenoth's contents."
> — `campaign/setting/notable-figures/bregan-daerthe/05-zelifarn.md:25`

Adventure, the reward as given:

> "It contains 300 sp plus a golden amulet shaped like an octopus with amethyst eyes (worth 250 gp)."
> — `sources/adventure-wdh.json:26611`

### A9. How long in post

Not applicable. Zelifarn is not an employee and has no post. Section A2 covers his time in the harbor.

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, the page: "*Young bronze dragon, lawful good, he/him*. Stat block: **Young Bronze Dragon**." — `campaign/setting/notable-figures/bregan-daerthe/05-zelifarn.md:5`
- Campaign, the organization page: "- **Zelifarn** — Young bronze dragon, lawful good." — `campaign/setting/organizations/07-bregan-daerthe.md:103`
- Campaign, Force Grey: "> Zelifarn (Lawful Good, Bronze Dragon, he/him) :: a bright, bouncy young dragon who trades facts the way sailors trade rumors, and who never lies." — `.../m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:227`
- Wiki: `| alignment5e    = [[Lawful good]]` — wiki line 59 (5e). Consistent.
- Adventure: no alignment given. The adventure says only "{@creature young bronze dragon}" (`sources/adventure-wdh.json:26604`).

**Species**
- Campaign, the page: "*Young bronze dragon ...*" (`05-zelifarn.md:5`).
- Wiki: `| race           = [[Bronze dragon]]` — wiki line 14. Consistent.
- Adventure: "Zelifarn, a {@creature young bronze dragon}" (`sources/adventure-wdh.json:26604`).

**Pronouns**
- Campaign, the page: "he/him" (`05-zelifarn.md:5`).
- Campaign, Force Grey: "(Lawful Good, Bronze Dragon, he/him)" (`.../ev-01-the-dragon-in-the-harbor.md:227`).
- Wiki: `| sex            = Male` — wiki line 12. Consistent.
- Campaign, Sea Maidens structure, a sibling-level kinship word: "belonged to Zelifarn's mother" (`arc-h-sea-maidens-faire.md:394`); "honors a grieving son's claim" (`arc-h-sea-maidens-faire.md:117`). Consistent.

**Stat block**
- Campaign, the page: "Stat block: **Young Bronze Dragon**." (`05-zelifarn.md:5`).
- Campaign, Force Grey: "> Zelifarn uses the **Young Bronze Dragon** stat block (CR 8), and the **Force Grey Mechanics Reference** covers him." — `.../ev-01-the-dragon-in-the-harbor.md:207`
- Campaign, Force Grey overview: "Zelifarn uses the 2024 **Young Bronze Dragon** stat block (CR 8) and does not fight." — `.../m02-the-dragon-in-the-harbor/overview.md:10`
- Alexandrian appendix: "**Zelifarn** (**Young Bronze Dragon**, 2024 *Monster Manual*)." — `sources/Appendix_C_-_Player_Faction_Missions.md:1759`
- Wiki: `| challenge5e    = 8` (wiki line 60) and `refs5e         = <ref name="WDH5e-p91" /><ref name="MM5e-p108">{{Cite book/Monster Manual 5th edition|108}}</ref>` (wiki line 62). The wiki's stat is 5e.

**Combat facts (campaign, for the Morale line)**
> "At the start of combat, Zelifarn uses his Repulsion Breath, a 30-foot cone. Each creature in it makes a DC 15 Strength saving throw or is pushed 40 feet and knocked Prone. Then he swims for deeper water."
> — `.../m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:210`

---

## C. Sentences on the current page that narrate quest-time or depend on a discovery

Current page: `campaign/setting/notable-figures/bregan-daerthe/05-zelifarn.md`. The page has no Background, Personality or Connections section yet.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Young bronze dragon, lawful good, he/him*. Stat block: **Young Bronze Dragon**." | Day-one. Stat block sourced in section B | `05-zelifarn.md:5`; B |
| 2 | L6 | "**Affiliation:** None (friendly to Bregan D'aerthe; not an operative)" | Day-one. User ruling (Key Members) | `campaign/setting/organizations/07-bregan-daerthe.md:103`, `:184` |
| 3 | L7 | "**Featured in:** **Sea Maidens Faire**, **Kolat Towers**, **Vault of Dragons**, **The Dragon in the Harbor**" | Quest references. Trollskull Alley is also a source for him (D9) | `campaign/structure/arc-h-sea-maidens-faire.md:115`; `arc-i-kolat-towers.md:369`; `arc-j-vault-of-dragons.md:117`; `.../m02-the-dragon-in-the-harbor/overview.md` |
| 4 | L11 | "**Resonance.** Zelifarn should inspire immediate delight with his chirping enthusiasm; pleasant surprise when his requested intelligence is specific and his offered reward is genuine; and amusement at a dragon who waves." | "when his requested intelligence is specific and his offered reward is genuine" is trade-time. The rest is day-one (wave: `sources/adventure-wdh.json:26601`) | Trade: `.../ev-01-the-dragon-in-the-harbor.md:223`-`:242` ("Zelifarn's Trade"); reward: `sources/adventure-wdh.json:26611` |
| 5 | L13 | "**Emotions.** Zelifarn most often feels bright curiosity, uncomplicated friendliness, genuine interest in surface-world affairs, delight when someone tells him something he did not know, and possessive pride in his stretch of Deepwater Harbor." | Day-one | Wiki line 67; `ev-01-the-dragon-in-the-harbor.md:200` |
| 6 | L15 | "**Motivations.** Zelifarn wants to learn about the surface world and the strange ships that pass through his harbor, stay on good terms with the *Eyecatcher*'s crew, whom he finds interesting, and collect specific information in exchange for specific rewards." | "stay on good terms" conflicts with the crossbows (D1). "collect specific information in exchange for specific rewards" is the trade mechanic. Kept verbatim per ruling 3 | `ev-01-the-dragon-in-the-harbor.md:22`; `ev-01-the-dragon-in-the-harbor.md:223`-`:242` |
| 7 | L17 | "**Inspirations.** When playing Zelifarn, channel Toothless (*How to Train Your Dragon*), Nemo (*Finding Nemo*), and Mushu (*Mulan*)." | Not a fact | n/a |
| 8 | L21 | "**Persona.** To the world, Zelifarn is a young bronze dragon who surfaces near ships in Deepwater Harbor with bronze-scaled curiosity and a cheerful wave. To those who engage with him honestly, he will trade specific information about the Eyecatcher for specific information about the surface world, and the reward he offers is genuine and already prepared. Deep down, he does not report to Jarlaxle or anyone else. He knows the *Eyecatcher* has something under her hull and that her crew discouraged him from looking, but he does not know whose the vessel is. He never lies, and he trades facts for facts." | The public part is day-one (A4). "he will trade specific information ... already prepared" is a trade (C4). "her crew discouraged him from looking" is softer than the mission's crossbows (D1). "He knows the *Eyecatcher* has something under her hull" is day-one (`overview.md:23`, "has watched since the ship arrived") | `sources/adventure-wdh.json:26604`; `.../overview.md:23`; `.../ev-01-the-dragon-in-the-harbor.md:22` |
| 9 | L23 | "**Morale.** Zelifarn does not fight at the surface. If threatened, he submerges and does not resurface near the threat. He remembers, though, and the sea is large." | "submerges" is a day-one habit (`overview.md:27`). "He remembers, though" echoes a mission consequence: "he remembers how the party treated him" (`overview.md:69`). Decide whether it is day-one | `.../overview.md:27`; `.../overview.md:69` |
| 10 | L25 | "**Relationships.** Zelifarn is the young bronze dragon of Deepwater Harbor, on friendly terms with the *Eyecatcher*'s crew but answerable to none of them, and the source of a genuine reward (300 sp, a golden octopus amulet, and a *scroll of revivify*) for parties willing to trade information about the Scarlet Marpenoth's contents." | "on friendly terms" conflicts with the crossbows (D1). "the source of a genuine reward ... for parties willing to trade information" is quest-time (the trade happens in the mission). A day-one version would state only that he holds a chest | `sources/adventure-wdh.json:26604`, `:26611`; `.../ev-01-the-dragon-in-the-harbor.md:223`-`:242` |
| 11 | L29 | "A young bronze dragon who surfaces near ships in Deepwater Harbor with a cheerful wave — genuinely curious about the surface world, and willing to trade specific, accurate information for equally specific information in return." | Day-one public face. 34 words (brief limit 21). "willing to trade" is the mission mechanic in public terms | `sources/adventure-wdh.json:26601`; Finding 7 |

**Voice profile (`.claude/skills/character-voices/voices/bregan-daerthe.md`, "### Zelifarn" at lines 98 to 112)**

Tagline, line 99: "*A bright, bouncy young bronze dragon who chirps, waves and trades facts like a delighted child.*" (day-one)

> "- **Sound:** A high, chirping, echoing voice with the sound of water in it. It warbles when he's excited." — line 101 (day-one)

> "- **Sentence shape:** Excited, rapid questions about the surface world, and short, precise bargains (\"You tell me three things, I tell you one big thing!\")." — line 102 (day-one; the bargain is the trade mechanic, see C4)

> "- **Word choice:** Harbour words and wonder: ships, shiny things, \"surface folk\", \"the captain\". He calls ships by their names and people by what they're wearing." — line 103 (day-one; "the captain" needs a referent, see D4)

> "- **Swearing:** *Never · Plain · n/a.* None. He picks up rude sailor words and uses them wrong and innocently (\"Is that a fucking? What's a fucking?\")." — line 104 (day-one; keep as written, adult table)

> "- **Personality in speech:** Bright curiosity and friendliness. He's delighted by new information. He's proud of his harbour and says \"my harbour\" often." — line 105 (day-one)

> "- **Quirks:** He waves with a flipper. He repeats new words to learn them. He splashes when happy." — line 106 (day-one; "flipper" conflicts with "claw", see D5)

> "- **Signature phrases:** \"Tell me something I don't know!\" / \"My harbour!\" / \"Trade? Trade!\"" — line 107 (day-one)

> "- **Never:** He never lies, never breaks a trade, and never understands why people keep secrets." — line 108 (day-one; "breaks a trade" is the trade mechanic)

> "  - *Greeting:* \"Hello! Hello, boat people! You're new! Tell me something I don't know!\"" — line 110 (day-one)

> "  - *Business:* \"Three things about the city, and I'll tell you where the fancy ship keeps its guards at night. Fair trade!\"" — line 111 (**quest-time clause**: the Eyecatcher's guards, offered as a trade. Restate as a day-one offer or remove under ruling 3)

> "  - *Under pressure:* \"Bad people! Bad! I'm telling the captain!\" (and he dives)" — line 112 (**quest-time-like clause**: "I'm telling the captain" conflicts with "does not report to Jarlaxle or anyone else" at page line 21; see D4)

Quest-time clauses in the Zelifarn profile for the rule-16 restatement: line 111 (Business, the Eyecatcher's guards) and line 112 (Under pressure, "the captain"). No profile line narrates the mother or the crystal ball. No profile line has been changed yet; the drafter will report changes.

---

## D. Conflicts

**D1. Does he have friendly terms with the crew?**
- Campaign, the page: "on friendly terms with the *Eyecatcher*'s crew" — `campaign/setting/notable-figures/bregan-daerthe/05-zelifarn.md:25`
- Campaign, the organization page: "is on friendly terms with the *Eyecatcher*'s crew" — `campaign/setting/organizations/07-bregan-daerthe.md:103`
- Campaign, Force Grey: "The Faire's deck watch has fired crossbows near him to drive him off." — `.../m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:22`
- Campaign, Force Grey overview: "Zelifarn describes a second hull fixed to the keel of the *Eyecatcher*, which comes out at night and goes back. The party can swim to the keel to look, though the Faire's deck watch fires crossbows at divers who are seen." — `.../m02-the-dragon-in-the-harbor/overview.md:57`
- Adventure: "His attempts to treat with the crew have met with no success" — `sources/adventure-wdh.json:26604`
- Rank: campaign over adventure. The campaign is internally split (the page and the organization page against the mission). Flag for the orchestrator.

**D2. How long he has lived in the harbor** (see Finding 1)
- Force Grey: "has lived in Deepwater Harbor for about three tendays" — `ev-01-the-dragon-in-the-harbor.md:18`, `overview.md:21`.
- Force Grey, in-world messages: "for a tenday now" — `ev-01-the-dragon-in-the-harbor.md:73`; "has sat outside the Dragonward for a tenday" — `ev-01-the-dragon-in-the-harbor.md:95`.
- Force Grey design notes: "Invented: ... Zelifarn's three tendays in the harbor" — `design-notes.md:19`.
- Sea Maidens Faire: "within days of the Sea Maidens Faire's arrival on Ches 21" — `arc-h-sea-maidens-faire.md:19`.
- Adventure: "recently moved into Deepwater Harbor ... the past several months" — `sources/adventure-wdh.json:26604`.
- Wiki: "had moved to the harbor in the late 15th century DR" — wiki line 70.
- Rank: campaign over adventure and wiki. Within the campaign, the Force Grey journal and the Sea Maidens structure doc disagree with each other, and the mission's own "a tenday" lines disagree with its "three tendays" line.

**D3. Does he know who killed his mother, and does he know the vessel?**
- Campaign, Sea Maidens structure: "agents whose employers Zelifarn had not yet identified" — `arc-h-sea-maidens-faire.md:19`
- Campaign, Sea Maidens structure: "Zelifarn does not know this when the party first engages him for assistance on this quest." — `arc-h-sea-maidens-faire.md:117`
- Campaign, Sea Maidens structure: "killed by Jarlaxle's agents" — `arc-h-sea-maidens-faire.md:394`
- Alexandrian PDF (transcription): "Jarlaxle and his agents killed his mother, Asphosis" and "Zelifarn knows that Jarlaxle keeps it in the Scarlet Marpenoth" — `sources/9. Lair – Sea Maidens Faire.pdf` PDF p.4 (printed p.71).
- Campaign, the page and Force Grey: "he does not know whose the vessel is" (`05-zelifarn.md:21`); "Zelifarn does not know whose it is." (`ev-01-the-dragon-in-the-harbor.md:22`).
- Rank: campaign over Alexandrian. The Sea Maidens structure doc is internally consistent on "does not know this" (line 117) and "not yet identified" (line 19), but line 394 states the killers without the qualifier. Routed to Sea Maidens Faire.

**D4. Which "captain"? And does he report to anyone?**
- Campaign, the page: "Deep down, he does not report to Jarlaxle or anyone else." — `05-zelifarn.md:21`
- Voice doc: "I'm telling the captain!" — `.claude/skills/character-voices/voices/bregan-daerthe.md:112`
- Voice doc, word choice: "\"the captain\"" — line 103
- Voice doc, Fel'rekt's profile, for comparison: "The captain trusts us." — line 71 (there "the captain" is Jarlaxle)
- Rank: campaign. The page says he does not report to Jarlaxle. The voice line does not say whom it means. Drafter to decide.

**D5. The dragon's wave: a flipper or a claw**
- Voice doc: "He waves with a flipper." — `bregan-daerthe.md:106`
- Adventure: "raises a claw in a small wave" — `sources/adventure-wdh.json:26601`
- Force Grey: "he claps his claws together" — `.../ev-01-the-dragon-in-the-harbor.md:272`
- Rank: adventure and campaign (Force Grey) both say claw. The voice doc is a profile file, not a fact file. Flag.

**D6. Mother's crystal ball room**
- Campaign, Sea Maidens structure: "the Nimblewright Crystal Ball in U4" — `arc-h-sea-maidens-faire.md:394`; "The crystal ball in U4" — `:117`; "the crystal ball now sat in U4" — `:19`
- Campaign, locations: "U7a contains Jarlaxle's fallback position chair, a bronze periscope, and a bronze crystal ball on a teak stand." — `campaign/locations/sea-maidens-faire/05-scarlet-marpenoth.md:19`
- Campaign, locations, U4 entry: "**U4 — Jarlaxle's Stateroom:** Locked (DC 18 Thieves' Tools). Harp, harpsichord, and a magic one-way window showing the sea outside." — `campaign/locations/sea-maidens-faire/05-scarlet-marpenoth.md:42` (no crystal ball in the U4 entry)
- Alexandrian PDF (transcription): "Area U4 – Jarlaxle's Stateroom: In addition to the normal entry for this area, a crystal ball sits upon a plush cushion of black velvet on a pedestal at the foot of the bed." — PDF p.6 (printed p.73).
- Rank: the campaign's locations file and the Sea Maidens structure doc disagree. Route to Sea Maidens Faire. Not for the page.

**D7. Alignment, species, pronouns, stat block, ward**: no conflict among the page, the organization page, the wiki, Force Grey and the Appendix. The adventure gives no alignment.

**D8. Affiliation label**: the page says "None (friendly to Bregan D'aerthe; not an operative)" (`05-zelifarn.md:6`). The organization page lists him under Key Members (`07-bregan-daerthe.md:103`), and its note says "Zelifarn stays in the list as the brief directs, although his page gives his affiliation as None." (`07-bregan-daerthe.md:184`). This is the user's ruling. Both are kept.

**D9. Featured in**: the page lists four quests (line 7). Trollskull Alley is absent. `campaign/quests/act-i/trollskull-alley/design-notes.md:47` ("## Force Grey / Zelifarn") and `campaign/structure/arc-b-trollskull-alley.md:365` ("## Force Grey / Zelifarn") give a section on him. Whether to add it is for the orchestrator.

---

## E. Stale lines in other files (not edited) and routed quest references

**Stale lines in other files**
- `campaign/setting/deities/bahamut.md:129` cites the affiliation as "(`campaign/setting/notable-figures/bregan-daerthe/05-zelifarn.md:7`)". The affiliation is at line 6 (`05-zelifarn.md:6`). Line 7 is Featured in.
- `sources/research/pass4-bundles/jarlaxle/campaign-hits.txt:1148` quotes the same note at `bahamut.md:133`. The bundle is out of date; the current line is 129.
- `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/design-notes.md:21` says the page and the organization page "now agree" with the mission. The page's Relationships line (25) still says "friendly terms" (D1).
- `campaign/structure/arc-h-sea-maidens-faire.md:19` and `:394` (the killers, and U4) conflict with `campaign/structure/arc-h-sea-maidens-faire.md:117` (he does not know) and with `campaign/locations/sea-maidens-faire/05-scarlet-marpenoth.md:19` (U7a). These are all campaign files (D3, D6).
- `sources/9. Lair – Sea Maidens Faire.pdf`, PDF p.4, says Zelifarn "knows that Jarlaxle keeps it in the Scarlet Marpenoth". Campaign (`arc-h-sea-maidens-faire.md:117`) says he does not know this when the party first engages him (D3).
- `.claude/skills/character-voices/voices/bregan-daerthe.md:106` ("flipper") conflicts with `sources/adventure-wdh.json:26601` ("claw") (D5).

**Routed to Sea Maidens Faire (the crystal ball moral thread, per the user ruling)**
- `campaign/structure/arc-h-sea-maidens-faire.md:392` "## Zelifarn's Crystal Ball as Moral Thread"
- `campaign/structure/arc-h-sea-maidens-faire.md:394` "Every lair heist has a moral dimension ... the Nimblewright Crystal Ball in U4 belonged to Zelifarn's mother, killed by Jarlaxle's agents."
- `campaign/structure/arc-h-sea-maidens-faire.md:396` "The choice is whether to return the crystal ball to Zelifarn (honoring a grieving dragon's claim, destroying Jarlaxle's surveillance network) or keep it (gaining a city-wide intelligence tool)."
- `campaign/structure/arc-h-sea-maidens-faire.md:398` (quoted under A3).
- `campaign/structure/arc-h-sea-maidens-faire.md:117` (quoted under A3): the discovery, the grief, the "cold fury" and the request.
- `campaign/structure/arc-h-sea-maidens-faire.md:13`-`:19`: the Eye and Zelifarn's arrival and backstory (quoted under A2 and A3).
- `campaign/structure/arc-h-sea-maidens-faire.md:115` "**Zelifarn (young bronze dragon).** If the party befriended Zelifarn in Force Grey Mission 2, he is the arc's most significant ally."
- `campaign/structure/arc-h-sea-maidens-faire.md:233` "**Zelifarn underwater extraction (if allied).** Zelifarn surfaces alongside the Eyecatcher's hull."
- `campaign/structure/arc-h-sea-maidens-faire.md:288`, `:290`, `:292` (NPC reactions to the crystal ball and to Zelifarn's fate)
- `campaign/structure/arc-h-sea-maidens-faire.md:336` "**Force Grey Mission 2 — The Dragon in the Harbor** — Zelifarn's introduction, submarine observation, Vajra's threat assessment filing."
- `campaign/structure/arc-h-sea-maidens-faire.md:344` "**Undermountain (future)** — Zelifarn's grief and potential alliance seeds his future role if the party descends."
- `campaign/locations/sea-maidens-faire/05-scarlet-marpenoth.md:19` and `:36` ("What Jarlaxle does if the crystal ball is accessed")

**Routed to Force Grey (Mission 2, "The Dragon in the Harbor")**
- `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/overview.md:21` (the offerings), `:23` (Meritide's deadline), `:27` (never lies), `:53` (the cave), `:57` (the keel), `:69` ("Zelifarn stays at the wreck and keeps watching the *Eyecatcher*, and he remembers how the party treated him.")
- `.../ev-01-the-dragon-in-the-harbor.md:18`, `:223`-`:242` (Zelifarn's Trade), `:272`, `:284`-`:289` (the three routes), `:311`, `:313`, `:337`, `:464`-`:465` (the Zelifarn Contacted and Zelifarn Befriended Event Outcomes)
- `campaign/guides/factions/06-force-grey.md:71` "| Renown 3, 3rd level | **The Dragon in the Harbor** | Zelifarn, a Young Bronze Dragon, has taken Umberlee's offerings from the harbor moorings."

**Routed to the Vault of Dragons (scale)**
- `campaign/structure/arc-j-vault-of-dragons.md:117` "The party may also recall specific sources encountered earlier in the campaign — Zelifarn's collection, Jarlaxle's private quarters, the Cassalanters' study — any of which could yield one for the asking, a favor, or a theft, depending on the party's standing with that source."
- `campaign/setting/lore/vault-of-dragons.md:56` "the party may also take one from Zelifarn's collection, Jarlaxle's private quarters or the Cassalanters' study."

**Routed to Kolat Towers**
- `campaign/structure/arc-i-kolat-towers.md:369` "Each lair heist has a moment that asks the party to weigh a consequence against a tactical advantage: smokepowder demolition in **Xanathar's Lair**, the children's sacrifice in **Cassalanter Villa**, Zelifarn's crystal ball in **Sea Maidens Faire**."

**Adventure (quest-time; not on the page)**
- `sources/adventure-wdh.json:26586`-`:26614`, "Special Events" → "The Friendly Dragon" (page 145). Quoted in A2, A8 and C.
- `sources/adventure-wdh.json:3802`: "\"A young bronze dragon has taken up residence in Deepwater Harbor. It startled a few sailors recently but hasn't hurt anyone. Confront the dragon and learn its intentions.\"" (Force Grey renown row, 3rd level)

**Alexandrian appendices (quest-time)**
- `sources/Appendix_B_-_Player_Factions.md:937`: "| 3rd | **The Dragon in the Harbor** | A young bronze dragon named Zelifarn has taken up residence in Deepwater Harbor. Determine its intentions. Vajra provides *potions of water breathing* for the dive. | +1 |"
- `sources/Appendix_C_-_Player_Faction_Missions.md:1728`-`:1781` (Arc FG-2, "The Dragon in the Harbor"). "Zelifarn is now an occasional source of harbor intelligence — he notices everything that moves below the surface and will share it in exchange for something interesting." is at line 1780.

**Other campaign files that name him**
- `campaign/setting/villains/jarlaxle.md:184` (draft notes): "Left out: ... Fenerus Stormcastle beyond the Manshoon note, Zelifarn, and the Alexandrian PDF 8 Eye-holder list."
- `campaign/setting/organizations/07-bregan-daerthe.md:184` (draft notes): "Zelifarn stays in the list as the brief directs, although his page gives his affiliation as None." (D8)
- `campaign/guides/factions/08-bregan-daerthe.md:152` (Notable Figures list)
- `campaign/setting/geography/dragonward-and-walking-statues.md:171` "> - **Research:** `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/` uses the dragonward in play. Vajra reports a bronze dragon \"just outside the Dragonward\" (`ev-01-the-dragon-in-the-harbor.md:81`), and the dragon is Zelifarn."
- `campaign/setting/deities/umberlee.md:89` "The Dragon in the Harbor links the two through Zelifarn and the vessel under the *Eyecatcher*, but no file ties Umberlee or the Queenspire to the Faire."
- `campaign/setting/deities/bahamut.md:111` "- **Aurinax**, **Zelifarn**, **Hlam** (Notable Figures): the gold dragon at the vault, the bronze dragon of the harbor and the monk who helps the party at the vault."
- `campaign/setting/deities/tiamat.md:116` "- **Aurinax**, **Zelifarn** (Notable Figures): the campaign's gold and bronze dragons, with no tie to her."

---

## F. Gaps a Background would need that no source gives

For each gap: the sourced facts the drafter must stay consistent with.

1. **Birth, hatching, birthplace, early life.** No source. Wiki infobox `dob` and `dobnotes` are blank (wiki lines 22 and 23). Constraints: he is young (wiki line 17: "Young in 1492"; `arc-h-sea-maidens-faire.md:19`: "twenty-two years old"). He is a bronze dragon (wiki line 14). His mother was a dragon and "a master crystalmancer" (Alexandrian PDF p.4).
2. **His mother's date of death and how it happened.** Name: "Asphosis" (`arc-h-sea-maidens-faire.md:19`, `:117`; PDF p.4). Date: "four years earlier" than the campaign's present, relative to "the grief he had been carrying for four years" (`arc-h-sea-maidens-faire.md:19`). The killers: "agents whose employers Zelifarn had not yet identified" (`:19`), "Zelifarn does not know this" (`:117`), and "Zelifarn knows that Jarlaxle keeps it in the Scarlet Marpenoth" (PDF p.4). Any Background must choose, and must not contradict the routed Sea Maidens Faire thread.
3. **The mother's hoard and heirloom.** "Her crystal ball — a family heirloom, a masterwork scrying device — had disappeared with her hoard." (`arc-h-sea-maidens-faire.md:19`). "he wants it back so that he can restore his mother's horde" (PDF p.4, transcription).
4. **How and when he came to Deepwater Harbor.** Four values (Finding 1, D2). No source gives a route, a reason or a companion.
5. **Whether he knows Jarlaxle's name or role.** The page says he does not report to Jarlaxle (`05-zelifarn.md:21`). The mission says he does not know whose the vessel is (`ev-01-the-dragon-in-the-harbor.md:22`). The Sea Maidens structure says he does not know who killed his mother when the party first engages him (`arc-h-sea-maidens-faire.md:117`). The Alexandrian says he knows Jarlaxle keeps the ball in the *Scarlet Marpenoth* (PDF p.4). Conflict (D3).
6. **His relationship to the crew, and to Vajra and Force Grey.** The page says friendly terms (`05-zelifarn.md:25`). The mission says crossbows (`ev-01-the-dragon-in-the-harbor.md:22`). The wiki says Vajra dispatched Gray Hands to learn his intentions (wiki line 72). The campaign's Force Grey overview says "Vajra knows only that sailors have reported a dragon" (`overview.md:23`). No source gives Zelifarn a line to Vajra.
7. **The offerings to Umberlee.** The campaign says he took them (`overview.md:21`). Whether the Background mentions them is a judgment for the orchestrator: the discovery is a mission event (`ev-01-the-dragon-in-the-harbor.md:18`, `:19`).
8. **Any other kin.** None. The wiki's `siblings`, `children` and `spouses` fields are blank (wiki lines 32 to 34 in that file).
9. **Personal goals.** No source gives Zelifarn a goal beyond the page's Motivations (line 15: "learn about the surface world ... stay on good terms ... collect specific information"). The Alexandrian gives one: "he wants it back so that he can restore his mother's horde" (PDF p.4). That goal is tied to the crystal ball, which is routed to Sea Maidens Faire. The drafter must not use it as a day-one goal without the orchestrator's decision.
10. **Name meaning, title, alias.** None. The wiki gives no title and no alias (wiki lines 5 to 9 are blank).

---

## G. Inner-life hints (exact quotes; for the Background and the personal goals, brief ruling 17)

- Mother, and the grief he carries: "...and that it scraped against the grief he had been carrying for four years without a name." — `campaign/structure/arc-h-sea-maidens-faire.md:19`
- Mother's horde: "he wants it back so that he can restore his mother's horde." — PDF p.4 (transcription)
- Grief and fury at the discovery: "His reaction is grief, then cold fury, then a request: \"That was hers. Bring it to me.\"" — `campaign/structure/arc-h-sea-maidens-faire.md:117`
- A grieving claim: "honoring a grieving dragon's claim" — `campaign/structure/arc-h-sea-maidens-faire.md:396`
- Nature at his age: "He is a young dragon — enthusiastic, curious, not yet cynical." — `campaign/structure/arc-h-sea-maidens-faire.md:398`
- Pride in his place: "possessive pride in his stretch of Deepwater Harbor" — `campaign/setting/notable-figures/bregan-daerthe/05-zelifarn.md:13`; "He's proud of his harbour and says \"my harbour\" often." — `.claude/skills/character-voices/voices/bregan-daerthe.md:105`
- Delight and wonder: "delight when someone tells him something he did not know" — `05-zelifarn.md:13`; "Tell me something I don't know!" — voice line 107
- Memory (mission consequence; check against F7): "He remembers, though, and the sea is large." — `05-zelifarn.md:23`; "he remembers how the party treated him" — `.../m02-the-dragon-in-the-harbor/overview.md:69`
- Cannot keep a secret: "Zelifarn cannot keep a secret or lie" — `.../m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:311`
- Does not understand fear: "does not understand why people are afraid of him." — `.../ev-01-the-dragon-in-the-harbor.md:200`
- Does not understand secrets: "I don't know how to do that. I'll just not say it unless someone asks." — `.../ev-01-the-dragon-in-the-harbor.md:313` (his answer when asked to say nothing)
- Has watched the ship: "which Zelifarn has watched since the ship arrived." — `.../m02-the-dragon-in-the-harbor/overview.md:23`
- Attention to the Eyecatcher: "I've been watching it for a week. It comes out sometimes, at night, and goes back." — `sources/Appendix_C_-_Player_Faction_Missions.md:1770` (Arc FG-2, Scene 3; a quest line, but the watching is also in `overview.md:23`)
- Restraint about the crew: "I considered offering to help them with security and decided they would say no." — `sources/Appendix_C_-_Player_Faction_Missions.md:1771`
- Acquisitive, wants shiny things: "He wants shiny things, interesting things, things that have a story." — `sources/Appendix_C_-_Player_Faction_Missions.md:1759`; "Zelifarn's whole body wiggles when you mention the deep moorings, and he claps his claws together before he answers." — `.../ev-01-the-dragon-in-the-harbor.md:272`
- Wants his treasure to grow: "He was eager to add treasure to his hoard" — wiki line 67.
- Says he will not hurt anyone: "has no wish to hurt anyone" — `.../ev-01-the-dragon-in-the-harbor.md:200`; "He never lies, and he trades facts for facts." — `05-zelifarn.md:21`
- Does not fight at the surface: "Zelifarn does not fight at the surface." — `05-zelifarn.md:23`

---

## Report completeness

- Every fact on the page's Summary, Roleplaying Information, Character Information and Overview is quoted or listed in C.
- The voice profile is quoted for every line that changes (C, voice block).
- Searched and found nothing about Zelifarn: `campaign/setting/history/` (no Zelifarn), `campaign/setting/governance-and-guilds/` (none), `campaign/setting/lore/` (only the scale line, `vault-of-dragons.md:56`), `sources/Act_III_Arc_D.md` and `sources/Act_III_Arc_E.md` (none; the Arc E hit is for Fenerus only).
- Not read: `sources/Vajra Safahr, Zelifarn, and Deepwater Harbor quests.docx` (`sources/SOURCE_GUIDE.md:696`); `sources/9. Lair – Sea Maidens Faire.pdf` PDF pages 8 onward; `sources/1. The Villains.pdf` and `sources/3. Player Character Factions.pdf` (not checked for Zelifarn; the Force Grey mission is covered by Appendix B and C).
