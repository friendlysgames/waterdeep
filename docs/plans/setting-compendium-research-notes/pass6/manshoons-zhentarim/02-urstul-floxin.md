# Pass 6 research notes: Urstul Floxin

Target page: `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md`
Group folder: `manshoons-zhentarim`. Faction page: `campaign/setting/organizations/09-manshoons-zhentarim.md`. Villains page: `campaign/setting/villains/manshoon.md`. Voice doc: `.claude/skills/character-voices/voices/manshoons-zhentarim.md`.

Method and limits:
- Read: the brief (`docs/plans/setting-compendium-pass6-brief.md`, rulings 1, 3, 15 to 17 and the user rulings), the target page, the organization page, the voice profile, the Villains page, the extracted wiki page (`/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-manshoons-zhentarim/02-urstul-floxin.txt`), and the Gralhund Villa, Fireball!, Finding Floon and Doom Raiders quest journals where Floxin appears.
- The file `docs/plans/setting-compendium-research-notes/pass6/manshoons-zhentarim/06-ott-steeltoes.md` does not exist at the path the generic instructions give. The Ott notes that do exist are at `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md`. Sections A to G below follow the generic instructions.
- Model pages `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md` and `11-gorath.md` were not opened. They are format inputs for the drafter.
- `sources/adventure-wdh.json` line numbers come from Grep and Read output. Wiki line numbers come from the extracted text file. PDF quotes were transcribed from page images and are flagged for a `pdftotext` check.
- Cross-reference lists in the last sections are locators. Every line quoted in A to G was checked against tool output; the locator lines were located with Grep or Read but are not all copied out.
- Edition: the published adventure is 5e *Waterdeep: Dragon Heist*. The wiki cites WDH 5e p. 216 for the infobox.

## Summary of the day-one state (Ches 1, 1492 DR)

- Who he is: an Illuskan human assassin, lawful evil, male, in his forties, Manshoon's chief field operative in Waterdeep, who will not name his master (sources in A, B and D).
- Where he lives on Ches 1 is **in conflict** between the sources (D1). No tie-breaker is given.
- Day one, the cell tracks Dalakhar and the Stone (A, "Dalakhar hunt"). The Stone's path is quest-time (C and E).
- The night before Ches 1, his cell took Renaer and Floon. That night is pre-campaign and is told on the setting page `campaign/setting/history/08-the-players-arrive.md` (A, "Renaer and Floon"). The rescue and the warehouse raid are Finding Floon events.
- The Gralhund Villa raid, his outcome (**Floxin Alive**, **Floxin Captured**, or the **Floxin Status** values in the Doom Raiders text) and his Kolat Towers appearance are quest-time and routed (C, E).

---

## A. Background facts by theme

### Origin and identity

> "{@creature Urstul Floxin|wdh} is an Illuskan human {@creature assassin}, with these changes:"
> — `sources/adventure-wdh.json:32652` (Appendix B entry; the entry's JSON `"page": 216` is at line 32641)

> "| home           = [[Waterdeep]], [[Sword Coast North]]"
> — `scratchpad/wiki-manshoons-zhentarim/02-urstul-floxin.txt:11` (wiki infobox)

> "| race           = [[Human]]"
> — `scratchpad/wiki-manshoons-zhentarim/02-urstul-floxin.txt:14`

> "| ethnicity      = [[Illuskan]]"
> — `scratchpad/wiki-manshoons-zhentarim/02-urstul-floxin.txt:15`

> "| occupation     = Assassin<ref name="WDH5e-p216" />"
> — `scratchpad/wiki-manshoons-zhentarim/02-urstul-floxin.txt:16`

> "| languages      = [[Common]], [[Orc language|Orc]]"
> — `scratchpad/wiki-manshoons-zhentarim/02-urstul-floxin.txt:19`

> "He speaks Common and Orc and knows thieves' cant."
> — `sources/adventure-wdh.json:32657` (list item under Game Statistics)

> "UR-stool FLOX-in"
> — `sources/adventure-wdh.json:342` (pronunciation key; the name is at line 341)

> "*Illuskan human assassin, lawful evil, he/him*. Stat block: **Assassin**."
> — `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:5` (the page's Gamemaster's Summary, first bullet)

### Appearance, age and manner

> "{@creature Urstul Floxin|wdh} works for {@creature Manshoon|WDH}, and he is the highest-ranking member of the Zhentarim squad stationed at House Gralhund. Urstul is a glorified thug with all the charm and breeding of a snake, but the Gralhunds tolerate him because he feeds them useful information culled from his spies throughout the city. Urstul takes his orders from {@creature Manshoon|WDH}'s current simulacrum, which comes and goes from House Gralhund by way of a teleportation circle (connected to the circle in Kolat Towers)."
> — `sources/adventure-wdh.json:32644` (the whole paragraph; the taking-orders sentence is contested, see D4)

> "Urstul is a large, heavyset man in his forties. He storms about House Gralhund like he owns the place. He has a collection of black {@creature flying snake||flying snakes} that he uses as couriers to deliver messages to underlings throughout the city."
> — `sources/adventure-wdh.json:32645`

> "A large, heavyset man in his forties who carries himself as though every room belongs to him. He works for the Zhentarim and makes no effort to hide it, though he will not name who gives him orders."
> — `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:29` (Overview; "the Zhentarim" is not qualified, see E)

> "Urstul Floxin is a big, heavy man in his forties who has killed for the Black Network for years. Rumour says he leads the renegade cell, the other Zhentarim in this city, but I can't prove it and I don't like guessing."
> — `campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:130` (quest-time event; a Doom Raiders NPC's public opinion, see C and D2)

> "Floxin is the name that keeps coming up, a large man in his forties who makes no effort to hide what he is."
> — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:258` (a Doom Raiders briefing answer; the belief it reports is day one, see C)

### Rank and post

> "'''Urstul Floxin''' ({{Pronounce|UR|stool|_|FLOX|in|refs=<ref name="WDH5e-p4">{{Cite book/Waterdeep: Dragon Heist|4}}</ref>}}) was a high-ranking member of the [[Zhentarim]] in [[Waterdeep]] in the early 1490s [[DR]].<ref name="WDH5e-p216" />"
> — `scratchpad/wiki-manshoons-zhentarim/02-urstul-floxin.txt:62` (wiki; WDH 5e p. 216)

> "In {{Yearlink|1492}},{{WDH-time}} Urstul Floxin was the leader of the Zhents headquartered in the villa of the [[Gralhund]] family. From there, he directed the search for the ''[[Stone of Golorr]]'', which was in possession of the [[gnome]] [[Dalakhar]].<ref name="WDH5e-p44">{{Cite book/Waterdeep: Dragon Heist|44}}</ref>"
> — `scratchpad/wiki-manshoons-zhentarim/02-urstul-floxin.txt:65` (wiki; WDH 5e p. 44; conflicts with the campaign, see D2 and D1)

> "- **Lieutenants and field teams:** Urstul Floxin is the chief field operative and leads the thugs who work the streets. Vevette Blackwater coordinates strike teams from Kolat Towers and leads the forces that fight Xanathar's Guild, and in the published adventure Agorn Fuoco leads those that fight the Zhents who are not loyal to Manshoon (**Vevette Blackwater**; *Dragon Heist*, 5e). Vira Solkan is a plant inside Blackstaff Tower (**Castle Ward**)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:58`

> "- **Urstul Floxin** — Illuskan human assassin, lawful evil, and Manshoon's chief field operative. He is the thuggish leader of the cell's field teams, and his team is tracking Dalakhar, the gnome moving the Stone of Golorr. See the **Urstul Floxin** page in Notable Figures."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:100`

> "**Relationships.** Urstul is Manshoon's chief field operative, a temporary occupant of Gralhund Villa (where he treats Yalah as an underling), and the antagonist who drives **Fireball!** and **Gralhund Villa** before the party can identify his master."
> — `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:25` (the "temporary occupant" clause is D1; the "drives" clause is C)

> "- **Urstul Floxin** (Manshoon's Zhentarim) — Zhent field commander; survived the blast; gives his real name; wants the party to track the Stone so his cell can follow"
> — `campaign/quests/act-ii/fireball/overview.md:27` (quest-time; Fireball! overview)

### Standing with Manshoon (day one)

> "**Relationships.** Manshoon is the leader of the Zhentarim splinter cell, the employer of Urstul Floxin, Sidra Romeir, and Vevette Blackwater, a blackmailer of Masked Lords Jelenn Urmbrusk and Corylus Thann, and a clone-wizard whose response teams are deliberately the weakest in muscle because drawing attention is the one mistake he will not make twice."
> — `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:26`

> "- Urstul Floxin ran the Dalakhar capture attempt and the **Gralhund Villa** operation. In the published adventure he takes his orders from Manshoon's simulacrum, and in the campaign he cannot name Manshoon, because he knows only a code and a chain of dead drops."
> — `campaign/setting/villains/manshoon.md:69` (the first sentence is quest-time, see C)

> "| Urstul Floxin | Field lieutenant | Most effective operative; trusted with the Stone recovery at Gralhund Villa; his failure there is the first crack |"
> — `campaign/setting/villains/manshoon.md:61` (the "trusted with the Stone recovery" and "his failure there" clauses are quest-time, see C)

> "Urstul received his orders directly from a [[simulacrum]] of Manshoon. He had a collection of black [[flying snake]]s that he used as couriers.<ref name="WDH5e-p216" />"
> — `scratchpad/wiki-manshoons-zhentarim/02-urstul-floxin.txt:81`

> "Urstul was truly loyal to Manshoon, even after being punished.<ref name="WDH5e-p159" /> He was a charming and dangerous individual.<ref name="WDH5e-p216" />"
> — `scratchpad/wiki-manshoons-zhentarim/02-urstul-floxin.txt:78` (wiki; "even after being punished" is quest-time, see C and G)

> "Yalah is the wife of Orond Gralhund (whom she manages more than loves), the commander of Hrabbaz (her bodyguard, more loyal to her than to Orond), and the de facto handler of the Zhentarim forces at her villa, not realizing their true master is Manshoon."
> — `campaign/setting/notable-figures/gralhunds/01-yalah-gralhund.md:25` (the Yalah page; Urstul is not named on this line)

### Gralhund alliance and household (day one, before the raid)

> "Less than a year ago, the Gralhunds were approached by agents of the Zhentarim loyal to {@creature Manshoon|WDH}, and the nobles formed an alliance with them. House Gralhund gives the Zhents coin and allows them to use the family's noble villa as a refuge. In exchange, the house reaps all the benefits that the Black Network offers, including intelligence that its spies have gathered. So while the Zhents use House Gralhund as a shield, the Gralhunds are using the Zhents to ascertain the identities and weaknesses of the Masked Lords."
> — `sources/adventure-wdh.json:32445`

> "The heads of the Gralhund noble family, {@creature Yalah Gralhund|wdh} and her husband, {@creature Orond Gralhund|wdh|Orond}, are providing coin and shelter to Urstul and his fellow Zhents in exchange for the promise of getting their fair share of the hidden cache of gold. But the Gralhunds aren't willing to put their trust entirely in the Black Network; they sent out their own agent to shadow the Zhents, eliminate Dalakhar, and obtain the {@item Stone of Golorr|WDH} on their behalf. Yalah gave the would-be assassin a {@item necklace of fireballs} with instructions on how and when to use it. When it seemed as though Dalakhar might give {@creature Urstul Floxin|wdh} the slip, this agent hurled one of the beads from the necklace to stop the gnome in his tracks."
> — `sources/adventure-wdh.json:4377` (the nimblewright sentence in the next line, 4378, is quest-time; the fireball clause is C)

> "Orond doesn't fully grasp how entwined the Black Network and his family have become-it is now next to impossible to separate one from the other. It's no secret in Waterdeep that the Black Network has firmly rooted itself in House Gralhund. But what's not generally known is that the Zhents in House Gralhund are agents of {@creature Manshoon|WDH}. Neither Orond nor any other member of his family knows about the wizard's clone. As far as Orond and his wife are concerned, the local leaders of the Black Network (with {@creature Urstul Floxin|wdh} chief among them) reside with them in the family villa."
> — `sources/adventure-wdh.json:32446` (the whole paragraph; the residence sentence is contested, see D1)

> "- **The Zhentarim squad:** A squad of Manshoon's Zhentarim lives at the villa under Urstul Floxin, the highest-ranking among them. Yalah treats them as her own spy network."
> — `campaign/setting/organizations/12-house-gralhund.md:49` (day-one residence claim, see D1)

> "- **House Gralhund (ally of convenience):** The Zhentarim use the villa as a shield and refuge, and the house uses them to learn the Masked Lords' identities and weaknesses (**House Gralhund**). Yalah Gralhund treats Urstul Floxin as an underling and does not know that Manshoon is the cell's master (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:90`

> "- The house pays for the Zhentarim cell that shelters at its villa. Yalah treats the cell's leader, Urstul Floxin, as an employee and doesn't know that Manshoon is its master."
> — `campaign/guides/factions/13-house-gralhund.md:17` (D1)

> "Yalah shares the services of a half-orc bodyguard with her husband, although {@creature Hrabbaz|WDH} (see \"{@creature Hrabbaz|WDH}\") is more loyal to her than to him. She also uses the Zhentarim who are based in House Gralhund as her personal spy network, not realizing that the Zhents' true master is {@creature Manshoon|WDH}. Most of her dealings are with the Zhent master assassin {@creature Urstul Floxin|wdh} (see \"{@creature Urstul Floxin|WDH}\"), whom she treats as an underling."
> — `sources/adventure-wdh.json:32782`

> "Until recently, this suite was set aside for the use of {@creature Urstul Floxin|wdh}. Lord Gralhund has barricaded himself in area G15b, using heavy furniture to block the door. Forcing it open requires a successful {@dc 18} Strength (Athletics) check."
> — `sources/adventure-wdh.json:5951` (the first sentence is the residence claim; the rest is quest-time)

### Dalakhar hunt (day one)

> "Dalakhar, the agent of Dagult Neverember, has the Stone and is carrying it toward Trollskull Manor. Urstul Floxin's Zhentarim cell is tracking him."
> — `campaign/setting/history/08-the-players-arrive.md:24`

> "- Xanathar's Guild knows Dalakhar was moving the Stone, though it does not know what the Eyes are. Urstul Floxin's Zhentarim cell was tracking him."
> — `campaign/setting/history/08-the-players-arrive.md:57`

> "| Manshoon's Zhentarim | The Stone exists and unlocks great wealth; Urstul Floxin's team was tracking Dalakhar; does not yet know the Stone reached the Gralhunds | Nothing | Stone + all three Eyes |"
> — `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:25` (the same row, verbatim, at `campaign/guides/gm-guide/running-the-villains.md:39`)

> "- **Manshoon's Zhentarim:** By the night of Ches 24, when Floxin's strike team hits **Gralhund Villa**, Manshoon's cell knows the Gralhunds hold the Stone."
> — `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:39` (quest-time sentence on a setting page, see E)

> "By the morning of Ches 22 Dalakhar has the Stone of Golorr and is carrying it to Trollskull Manor, where he means to deliver it to the party. Which keeper he took it from is unsettled. See Draft Notes."
> — `campaign/setting/history/08-the-players-arrive.md:56` (Ches 22 is quest-time; quoted here for the Dalakhar timeline only)

> "Three members of the Black Network, including the Zhent assassin {@creature Urstul Floxin|wdh} (see {@adventure appendix B|WDH|12}), were close to nabbing Dalakhar when they were caught in the blast."
> — `sources/adventure-wdh.json:4368` (quest-time; see C)

### Renaer and Floon (the night before Ches 1, pre-campaign)

> "Unbeknownst to Volo, not long after he departed, a drunken Floon met another acquaintance, Lord {@creature Renaer Neverember|wdh}, at the tavern. The two left together, with Renaer offering to walk Floon home. Five Zhentarim thugs working for {@creature Urstul Floxin|wdh} (see {@adventure appendix B|WDH|12}) jumped both Floon and Renaer. They took them to a warehouse in the Dock Ward, so they could question Renaer-the son of Lord Dagult Neverember-about the whereabouts of the Stone of Golorr and his father's hidden cache of dragons. Before the interrogation could begin, members of the Xanathar Guild ambushed and killed the Zhent guards in the warehouse. The new arrivals mistook Floon for Renaer, knocked Floon {@condition unconscious}, and dragged him away while Renaer hid and escaped their notice."
> — `sources/adventure-wdh.json:1687` (the whole paragraph; the published adventure's "two nights ago" wording is at line 1686)

> "- **The night before Ches 1, 1492 DR, Renaer Neverember:** Five Zhentarim thugs working for Urstul Floxin seized Renaer Neverember to learn what he knew about his father's hidden gold, and they took Floon Blagmaar in the same attack. House Gralhund paid for the operation (*Dragon Heist*, 5e; **House Gralhund**). Xanathar's Guild raided the Candle Lane warehouse where the thugs held both men and killed the cell's agents there (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:33`

> "Floon Blagmaar is taken on the night before Ches 1. The published adventure says "two nights"; the campaign settled on "last night"."
> — `campaign/setting/history/08-the-players-arrive.md:64`

> "- Urstul Floxin's cell led the kidnapping and fled to Kolat Towers before the quest begins. The City Watch has Splinter thugs under arrest at the Dock Ward scene."
> — `campaign/setting/history/08-the-players-arrive.md:65` (see D1)

> "- The cell seized Renaer's mourning locket and pried it open at the Candle Lane warehouse. Xanathar's Guild raided the warehouse the same night and carried off what it found in the back office, the Eye included, without knowing what the Eye was. Bregan D'aerthe agents already inside Xanathar's hideout lifted it that night, and it reached Jarlaxle aboard the *Scarlet Marpenoth* before the party reached the hideout. Manshoon himself never held it. This route is the main session's reading of the user's Session 47 ruling "Jarlaxle has men in Xanathar's hideout"."
> — `campaign/setting/history/08-the-players-arrive.md:66` (the Eye part is not Floxin's, see E)

### Watch and Dock Ward (day one)

> "By the spring of 1492 DR brawls between Xanathar's Guild and the Zhentarim have become common in the Dock Ward, and the Watch is called to them often (**The Players Arrive**). The Dock Ward captain, Hyustus Staget, pulled a surveillance detail off a Zhent instigator named Urstul Floxin to strengthen street patrols, and he regrets it (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/11-open-lords-watch.md:25`

> "Staget once had the warehouse under surveillance, but elected to pull the detail to bolster patrols throughout the Dock Ward-a decision he now regrets. That surveillance was part of an attempt to catch a known Zhent instigator named {@creature Urstul Floxin|wdh}, a \"big fish\" rumored to be responsible for much of the recent strife. Staget doesn't share this information with strangers."
> — `sources/adventure-wdh.json:2185`

### Doom Raiders belief (day one)

> "- **Manshoon's Zhentarim (enemy):** The Splinter peeled off a large part of the Doom Raiders' network, and the two cells despise each other and will not cooperate (**The Founding of Chains**). Manshoon regards the Doom Raiders as deserters who stole his name (**Manshoon**). `[research]` Davil, Yagra and the others believe Urstul Floxin leads the rival cell, so they do not know whom it serves (see GM Notes)."
> — `campaign/setting/organizations/06-doom-raiders.md:88`

> "- **The War at Home Comes First:** The fight with the rival cell is the Doom Raiders' defining preoccupation, and the Grand Game is secondary to it. Information given to the Doom Raiders will not reach the rival cell. The published adventure adds that Manshoon's war on Xanathar's Guild threw the cell's plans into upheaval (*Dragon Heist*, 5e). The cell believes Urstul Floxin leads its rival and does not know whom he serves (see GM Notes)."
> — `campaign/setting/organizations/06-doom-raiders.md:39`

> "- **What the Doom Raiders call the rival cell:** Manshoon directs the rival cell through Urstul Floxin, but no Doom Raider has heard his name connected to it. Davil, Yagra and the others believe that Floxin leads it, and they call it \"the other cell\", \"Floxin's cell\" or \"the Splinter\". The History above states the truth for the GM."
> — `campaign/setting/organizations/06-doom-raiders.md:115` (GM note; see D2)

> "- The rival cell of the Black Network in Waterdeep and its leader, Urstul Floxin."
> — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:195` (a topic Davil is "happy to discuss", so it is his belief; see D2)

### Habits, belongings and couriers (day one)

> "**Persona.** To the world, Urstul is a large, heavyset man in his forties who treats every room as his own. To those he works with, he is Manshoon's chief field operative who runs both the Dalakhar capture attempt and the Gralhund Villa operation. Deep down, he will not divulge his master's name unless magically compelled, and he keeps a collection of black flying snakes as couriers because he trusts animals more than people."
> — `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:21` (the "runs both" clause is quest-time, see C)

> "- **Messengers:** Black flying snakes carry the cell's orders between its sites, and three of them nest at the Interrogation House while Urstul keeps a collection of his own (**North Ward**; **Urstul Floxin**)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:64`

> "- **Nobody Names the Master:** The street crews will not say who gives the orders, and few in the cell know their master's name. Urstul Floxin will not divulge it unless magically compelled, and he sends messages by black flying snake because he trusts animals more than people. Outsiders call the cell the Splinter."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:42`

> "He talks to his flying snakes more gently than to people. He jabs a finger at whoever he's talking to."
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:39` (voice doc, Quirks)

---

## B. Alignment, species, pronouns, stat block

| Field | Value | Quote and line |
|---|---|---|
| Alignment (page) | Lawful evil | `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:5`: "*Illuskan human assassin, lawful evil, he/him*. Stat block: **Assassin**." |
| Alignment (published) | Lawful evil | `sources/adventure-wdh.json:32656`: "Urstul is lawful evil." |
| Alignment (wiki) | Lawful evil | `scratchpad/wiki-manshoons-zhentarim/02-urstul-floxin.txt:57`: "| alignment5e    = [[Lawful evil]]" |
| Alignment (organization page) | Lawful evil | `campaign/setting/organizations/09-manshoons-zhentarim.md:100`: "Illuskan human assassin, lawful evil, and Manshoon's chief field operative." |
| Species | Human | `sources/adventure-wdh.json:32652`: "is an Illuskan human {@creature assassin}, with these changes:"; wiki line 14: "| race           = [[Human]]" |
| Ethnicity | Illuskan | wiki line 15: "| ethnicity      = [[Illuskan]]"; the page's line 5 and `sources/adventure-wdh.json:32652` agree |
| Pronouns | he/him | page line 5: "he/him"; `sources/adventure-wdh.json:32645`: "He storms about House Gralhund like he owns the place."; wiki line 13: "| sex            = Male" |
| Affiliation | Manshoon's Zhentarim | `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:6`: "> - **Affiliation:** Manshoon's Zhentarim" |
| Stat block | Assassin | `sources/adventure-wdh.json:32652` (above); wiki line 59: "| class5e        = [[Assassin]]"; wiki line 60 cites MM 5e p. 343 |
| Challenge rating (wiki, base) | 8 | wiki line 58: "| challenge5e    = 8" |
| Challenge rating (published, wounded at G15) | 3 (700 XP) | `sources/adventure-wdh.json:5952`: "Urstul is wounded with 50 hit points remaining and has no poison coating his weapons, reducing his challenge rating to 3 (700 XP)." (quest-time, see C and D11) |
| Languages | Common, Orc, thieves' cant | `sources/adventure-wdh.json:32657` (above); wiki line 19 (above) |
| Age | "in his forties" | `sources/adventure-wdh.json:32645`: "Urstul is a large, heavyset man in his forties." |
| Build | large, heavyset | same line 32645 |
| Featured in | Finding Floon; Fireball!; Gralhund Villa; Faction Outposts; Sea Maidens Faire; Kolat Towers; Gralhund Villa (location) | `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:7` |

Notes for the Summary block:
- The organization page's Key Members entry (`campaign/setting/organizations/09-manshoons-zhentarim.md:100`) matches the page on species, alignment and role.
- The Factions Guide response-team entry is "**Urstul Floxin** (**assassin**) + 3–4 **thugs** (available only if he survived the Gralhund Villa)." (`campaign/guides/factions/10-manshoons-zhentarim.md:13`). It is conditional on a quest result. The brief asks the Summary to add a bullet for the Factions Guide or Villains page; that bullet can cite the Villains page (`campaign/setting/villains/manshoon.md:61`).

---

## C. Quest-time sentences on the current page (and where each already lives)

Each sentence below narrates a quest event or a quest-time state. Under ruling 1 it is restated as a day-one fact or removed. The rows give the file where the event already lives.

| Page line | Sentence (exact) | Where the event already lives | Day-one restatement available? |
|---|---|---|---|
| `02-urstul-floxin.md:11` (Resonance) | "frustration with his slipperiness across multiple arcs" | No quest event. "arcs" is retired vocabulary (E) | Not an event; the word "arcs" must go |
| `02-urstul-floxin.md:21` (Persona) | "To those he works with, he is Manshoon's chief field operative who runs both the Dalakhar capture attempt and the Gralhund Villa operation." | Dalakhar ambush: `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:94` ("Worked for Urstul Floxin. Assigned to intercept a rock gnome named Dalakhar."); `sources/adventure-wdh.json:4368`. Gralhund raid: `campaign/quests/act-ii/gralhund-villa/overview.md:46`; `ev-04-the-zhentarim-raid.md:20`. | Day one: "chief field operative" (`09-manshoons-zhentarim.md:58`) and the cell is tracking Dalakhar (`history/08:24`). The "runs both ..." clause is quest-time. |
| `02-urstul-floxin.md:23` (Morale) | "If wounded or desperate, he kicks open the nearest door to grab a hostage." | G15 door: `campaign/quests/act-ii/gralhund-villa/ev-04-the-zhentarim-raid.md:42` ("He begins trying to kick the door down."); `ev-05-the-guest-suite.md:18`. G16 hostage plan: `sources/Act_III_Arc_E.md:689`. | Behaviour, not an event; the drafter decides |
| `02-urstul-floxin.md:23` (Morale) | "If confronted with overwhelming force, he uses surviving Zhents as cover and runs." | `sources/Act_III_Arc_E.md:596` | Behaviour; no event |
| `02-urstul-floxin.md:25` (Relationships) | "a temporary occupant of Gralhund Villa" | Residence conflict (D1) | Conflict, not a fact |
| `02-urstul-floxin.md:25` (Relationships) | "the antagonist who drives **Fireball!** and **Gralhund Villa** before the party can identify his master" | `campaign/quests/act-ii/fireball/overview.md:27`; `campaign/quests/act-ii/gralhund-villa/overview.md:28` | Remove; restate as "he works for Manshoon and will not name him" |
| `02-urstul-floxin.md:13` (Emotions) | "(he storms about Gralhund Villa like he owns it)" | Published `sources/adventure-wdh.json:32645`: "He storms about House Gralhund like he owns the place." | Day one, if the residence is settled (D1) |
| `02-urstul-floxin.md:15` (Motivations) | "Urstul wants to recover the Stone of Golorr for Manshoon" | Stone's path: `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:32` (the nimblewright takes it); `sources/adventure-wdh.json:4379` ("Urstul Floxin is refusing to hand over the Stone of Golorr until he speaks to his secret master") | Motivation is day one (`history/08:24`); the recovery is quest-time |
| `02-urstul-floxin.md:29` (Overview) | "He works for the Zhentarim" | Two Zhentarims rule (E) | Restate as "Manshoon's Zhentarim" or "a Zhentarim cell" |
| Voice `manshoons-zhentarim.md:38` | "Cornered, he turns cunning and grabs a hostage, still never naming his master." | Behaviour (see Morale above) | Behaviour |
| Voice `manshoons-zhentarim.md:37` | "Get that fucking gnome, you slack-jawed pisspots!" | Dalakhar hunt: `history/08:24` (day one) | Day one (the hunt, not the capture) |
| Voice `manshoons-zhentarim.md:41` | "He never names Manshoon unless magically compelled" | Conflict with `campaign/quests/act-ii/gralhund-villa/ev-05-the-guest-suite.md:33` (D3) | Conflict |
| Voice `manshoons-zhentarim.md:44` | "The stone comes to me. Who I give it to is not your business." | Stone's path (Fireball, Gralhund) | Sample line; the drafter decides |
| Voice `manshoons-zhentarim.md:45` | "Back off, or the pretty one gets a new smile. Back. Off." | "the pretty one" is not identified in any source | Sample line; no event named |
| `campaign/setting/organizations/09-manshoons-zhentarim.md:100` | "his team is tracking Dalakhar, the gnome moving the Stone of Golorr" | Day-one hunt (`history/08:24`) | Day one |

Quest-time facts the page does not currently state, which the Background must not contradict:
- Fireball!: the burned man "gives his real name when asked", is "north of the blast radius — badly burned, conscious", and "wants the Stone tracked so the Zhentarim can follow" (`campaign/quests/act-ii/fireball/ev-01-the-fireball.md:32, 64, 66`).
- Gralhund Villa: "led the strike team; arrived on the night of Ches 24th with eight agents and lost most of them; trapped in the guest suite corridor by the time the party arrives; still armed; still operational; still will not name his master" (`campaign/quests/act-ii/gralhund-villa/overview.md:28`).
- Gralhund Villa: "He was still a prisoner then; the raid had not yet begun." (`campaign/locations/gralhund-villa/g09-parlor.md:7`, which places him in the villa on Ches 22 to 24).
- Gralhund Villa aftermath: "No Stone, no nimblewright, no Floxin." (`campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:44`).
- Kolat Towers: "If he survived earlier encounters with the characters" he is in the towers, "being punished for allowing the Stone of Golorr to slip through his fingers" (`sources/adventure-wdh.json:30041`).

---

## D. Conflicts

**D1. Where he lives on Ches 1, 1492 DR (residence).** No file settles it.

Day-one residence at Gralhund Villa:
> "{@creature Urstul Floxin|wdh} works for {@creature Manshoon|WDH}, and he is the highest-ranking member of the Zhentarim squad stationed at House Gralhund." — `sources/adventure-wdh.json:32644`
> "Until recently, this suite was set aside for the use of {@creature Urstul Floxin|wdh}." — `sources/adventure-wdh.json:5951`
> "- **The Zhentarim squad:** A squad of Manshoon's Zhentarim lives at the villa under Urstul Floxin, the highest-ranking among them. Yalah treats them as her own spy network." — `campaign/setting/organizations/12-house-gralhund.md:49`
> "a temporary occupant of Gralhund Villa (where he treats Yalah as an underling)" — `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:25`
> "- The house pays for the Zhentarim cell that shelters at its villa. Yalah treats the cell's leader, Urstul Floxin, as an employee and doesn't know that Manshoon is its master." — `campaign/guides/factions/13-house-gralhund.md:17`

Day-one residence elsewhere (Kolat Towers):
> "- Urstul Floxin's cell led the kidnapping and fled to Kolat Towers before the quest begins. The City Watch has Splinter thugs under arrest at the Dock Ward scene." — `campaign/setting/history/08-the-players-arrive.md:65`
> "- **Urstul Floxin** (Manshoon's Zhentarim) — offscreen; led the kidnapping cell; already fled to Kolat Towers before the quest begins" — `campaign/quests/act-i/finding-floon/overview.md:31`

Arrival at the villa on Ches 24 (quest journal):
> "- **Urstul Floxin** (Manshoon's Zhentarim) — led the strike team; arrived on the night of Ches 24th with eight agents and lost most of them; trapped in the guest suite corridor by the time the party arrives; still armed; still operational; still will not name his master" — `campaign/quests/act-ii/gralhund-villa/overview.md:28`

Villa stay on Ches 22 to 24 (quest-time):
> "Two house guards are dead in this room. Floxin killed them in the small hours of Ches 24th, while the household slept. He was still a prisoner then; the raid had not yet begun." — `campaign/locations/gralhund-villa/g09-parlor.md:7`
> "{@creature Urstul Floxin|wdh} was confined here when he returned to the villa, but shortly thereafter he killed his guards and escaped." — `sources/adventure-wdh.json:5797`

Retreat after the fireball (Alexandrian, quest-time):
> "He did not stay confined. Within hours, Floxin killed his guards and escaped — without the Stone, which Gralhund refused to yield. He retreated to his Black Network safe house, assembled his full strike team, and began planning a return." — `sources/Act_III_Arc_D.md:39` (inside a `<p>` element; "safe house" is not located)

Ranking note for the orchestrator: `history/08` is a setting page and `finding-floon/overview.md` is a quest journal. Both are campaign files, and both place him at Kolat Towers "before the quest begins". The Gralhund-residence claims are in an organization page and a guide, both written as day-one lore. The brief's rules do not settle which to follow. The Yellowspire safe house is a third location (D10).

**D2. Rank and position.** The sources describe him in different terms.
> "- **Lieutenants and field teams:** Urstul Floxin is the chief field operative and leads the thugs who work the streets." — `campaign/setting/organizations/09-manshoons-zhentarim.md:58`
> "- **Urstul Floxin** — Illuskan human assassin, lawful evil, and Manshoon's chief field operative. He is the thuggish leader of the cell's field teams, and his team is tracking Dalakhar, the gnome moving the Stone of Golorr. See the **Urstul Floxin** page in Notable Figures." — `campaign/setting/organizations/09-manshoons-zhentarim.md:100`
> "{@creature Urstul Floxin|wdh} works for {@creature Manshoon|WDH}, and he is the highest-ranking member of the Zhentarim squad stationed at House Gralhund." — `sources/adventure-wdh.json:32644`
> "The rumored leader of the renegade Zhent faction is {@creature Urstul Floxin|wdh}, a known Black Network assassin." — `sources/adventure-wdh.json:4033`
> "In {{Yearlink|1492}},{{WDH-time}} Urstul Floxin was the leader of the Zhents headquartered in the villa of the [[Gralhund]] family." — `scratchpad/wiki-manshoons-zhentarim/02-urstul-floxin.txt:65`
> "Floxin is Manshoon's chief field agent and the face of the cell in the streets, but he is not its leader." — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:21` (GM-only truth)
> "- The rival cell of the Black Network in Waterdeep and its leader, Urstul Floxin." — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:195` (Davil's topic list, the Doom Raiders' belief)
Note: the pass 5 notes say "Campaign governs; the Doom Raiders text must not use line 4033" (`docs/plans/setting-compendium-research-notes/pass5/zhentarim.md:283`).

**D3. Whether he can be made to name Manshoon.**
> "Deep down, he will not divulge his master's name unless magically compelled" — `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:21`
> "He never names Manshoon unless magically compelled, never backs down in public, and never trusts a person over a snake." — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:41`
> "won't divulge it or the name of his master, {@creature Manshoon|WDH}, unless he's magically compelled to do so." — `sources/adventure-wdh.json:5952`
> "Floxin will not name Manshoon. Not under Intimidation, not under magical compulsion, not with a blade at his throat. He does not know the name — he knows a code and a set of dead-drop locations." — `campaign/quests/act-ii/gralhund-villa/ev-05-the-guest-suite.md:33`
> "DC 14 Insight during any interrogation of Floxin confirms this genuinely: he knows a dead-drop chain and a code, not a name or a face." — `campaign/quests/act-ii/gralhund-villa/design-notes.md:37` (the sentence before it reads "Floxin does not name his master.")
> "he cannot name Manshoon, because he knows only a code and a chain of dead drops." — `campaign/setting/villains/manshoon.md:69`
The page and the voice profile follow the published adventure on compulsion. The Gralhund quest journal removes the compulsion exception.

**D4. How he takes orders.**
> "Urstul takes his orders from {@creature Manshoon|WDH}'s current simulacrum, which comes and goes from House Gralhund by way of a teleportation circle (connected to the circle in Kolat Towers)." — `sources/adventure-wdh.json:32644`
> "Urstul received his orders directly from a [[simulacrum]] of Manshoon." — `scratchpad/wiki-manshoons-zhentarim/02-urstul-floxin.txt:81`
> "He knows the shape of the operation and the chain of command stopped at a contact he never saw face to face. Manshoon stays invisible." — `campaign/quests/act-ii/gralhund-villa/ev-05-the-guest-suite.md:33`
> "In the published adventure he takes his orders from Manshoon's simulacrum, and in the campaign he cannot name Manshoon" — `campaign/setting/villains/manshoon.md:69`

**D5. The teleportation circle and flying snakes in G15b.**
> "Area G15b is a wood-paneled bedchamber with a birdcage on a table and a permanent teleportation circle inscribed on the floor. The birdcage contains three {@creature flying snake||flying snakes} that Urstul uses to deliver messages to his spies throughout the city. The circle is used by {@creature Manshoon|WDH} to meet secretly with {@creature Urstul Floxin|WDH} and to teleport Zhents to and from Kolat Towers (see chapter 8). See the {@spell teleportation circle} spell description in the {@book Player's Handbook|phb} for more information on how the circle functions." — `sources/adventure-wdh.json:5954`
> "- Note: The published module places a teleportation circle and flying snakes in G15b. The Alexandrian Remix explicitly removes both. G15b is an ordinary guest room." — `campaign/quests/act-ii/gralhund-villa/ev-05-the-guest-suite.md:12`
> "G15b is an ordinary guest room with no magical infrastructure." — `campaign/structure/arc-d-gralhund-villa.md:162` (superseded file)

**D6. Who holds the Stone during the Dalakhar fight (quest-time).**
> "Dalakhar is killed by a fireball spell. Urstul Floxin steals the Stone of Golorr from Dalakhar's corpse." — `sources/adventure-wdh.json:862`
> "Though he was wounded, he was able to pluck the {@item Stone of Golorr|WDH} from Dalakhar's pocket before fleeing the scene." — `sources/adventure-wdh.json:4368`
> "The nimblewright threw the bead from the cooperage rooftop to the east, dropped to the street, rifled Dalakhar's body, took the Stone of Golorr, and fled east across the rooftops. Floxin was north of the blast radius — badly burned, conscious." — `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:32`
> "The nimblewright uses a necklace of fireballs to launch a fireball which kills Dalakhar and most of the Zhentarim agents, with the exception of Urstul Floxin (who barely survives, but is incapacitated)." — `sources/4. Gralhund Villa.pdf` p. 26 (transcribed from the page image; flag for `pdftotext`)
The Fireball! quest journal is authoritative for the quest.

**D7. Outcome names for Floxin's fate.**
> "- **Floxin Alive** — mark when Floxin survives the raid; read by **Kolat Towers**, where he becomes available as a Manshoon response team leader." — `campaign/quests/act-ii/gralhund-villa/ev-04-the-zhentarim-raid.md:98`
> "- **Floxin Captured** — mark when the party takes Floxin into custody, only when **Floxin Alive** is also marked; a captured Floxin provides nothing useful about his master. Read by **Dungeon of the Mad Mage** (reserved; that journal is not yet written)." — `campaign/quests/act-ii/gralhund-villa/ev-04-the-zhentarim-raid.md:99`
> "- **Floxin Status.** If the **Gralhund Villa** outcome **Floxin Status** is Dead or Captured, no Doom Raider says \"Floxin's cell\". They say \"the other cell\" instead, and Davil uses the Dead or Captured answer in **Who runs the other cell?**" — `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:28`
> "> - **Alive:** Floxin filed the tip himself. On the dawn of Ches 26, hooded and with his left hand wrapped in a bandage from the burns he took in the fireball, he pushed a folded note through the gatehouse window at Castle Waterdeep. The warrant and the failed scrying are real, because Floxin is hiding." — `campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:26`
> "> - **Dead or Captured:** another member of the cell filed the tip, a lean hooded human who pushed the note through the same window at the same hour, on orders from Manshoon. Floxin never sent it, and there is no bandaged man to find. The warrant in Tashlyn's information is moot, and she has nothing to scry." — `campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:27`
The Gralhund quest journal's Event Outcomes list "Floxin Alive" and "Floxin Captured" and no "Dead" outcome. The Doom Raiders files read one **Floxin Status** outcome with three values. The names do not match. Route to Gralhund Villa.

**D8. Warrant and whereabouts after the raid.**
> "A warrant has been issued for Urstul's arrest, but his current whereabouts are unknown. Even magical scrying has failed to reveal his location." — `sources/adventure-wdh.json:4034`
> "The Zhent leader, {@creature Urstul Floxin|wdh}, was among those who got away. He's still at large. The Watch plans to step up its search for him." — `sources/adventure-wdh.json:4837`
> "> - **The warrant.** Only if Floxin is Alive: the Watch has issued a warrant for him, his whereabouts are unknown, and scrying has failed to find him." — `campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:115`
> "No Stone, no nimblewright, no Floxin." — `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:44`

**D9. Harper identification.**
> "- **Conflicts:** Floxin. `fireball/ev-01-the-fireball.md:175` has Renaer's Harper contacts identify the burned man as \"Manshoon's chief field agent in Waterdeep\", while `02-harpers.md:22` and `history/04-the-founding-of-chains.md:93` say no Harper contact names Manshoon. The body no longer mentions Floxin, so the conflict is for the quest files to settle." — `campaign/setting/organizations/01-harpers.md:177`
> "When the party mentions Fala's (or Tally's) account of the burned man fleeing north, Renaer reaches out to Harper contacts at once. Within one day (the morning of Ches 23rd at the latest), he returns: the burned man is **Urstul Floxin**, Manshoon's chief field agent in Waterdeep. A North Ward resident saw Floxin — visibly burned and limping — enter Gralhund Villa on Saerdoun Street within hours of the blast. The City Watch sent two constables who were told everything was fine. No warrant was issued." — `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:175`

**D10. Safe house.**
> "| 1+ days | Briefed on Dalakhar's death; knows Floxin was following him | Inadvertently confirms Floxin as a pursuer; can mention Floxin staying at the Yellowspire safe house (Castle Ward) → leads to Gralhund Villa if the party hasn't found it yet |" — `campaign/quests/act-ii/fireball/ev-06-the-death-mark.md:52`
> "- Tracking Urstul Floxin before the Gralhund Villa operation (Response Team: Urstul Floxin)" — `campaign/guides/factions/10-manshoons-zhentarim.md:68` (Yellowspire revelation list)
> "Parties that searched Urstul Floxin's effects at Gralhund Villa have documents pointing to Brindul Alley." — `campaign/guides/factions/10-manshoons-zhentarim.md:19`
The Yellowspire lead (`ev-06:52`) and the Gralhund residence (D1) are in conflict. Fireball! `ev-01:175` places him in the villa "within hours of the blast" (see D9 quote).

**D11. Challenge rating.**
> "| challenge5e    = 8" — `scratchpad/wiki-manshoons-zhentarim/02-urstul-floxin.txt:58`
> "reducing his challenge rating to 3 (700 XP)" — `sources/adventure-wdh.json:5952` (wounded, no poison; quest-time)
> "Night state:** Urstul Floxin (50 hp, no poison, CR 3) in the guest suite corridor; Hurv Taldred as shadow + 2 mastiff-shadows in the yard; 1–2 surviving Zhent thugs in the great hall and upstairs foyer; Hrabbaz; Yalah; the household nimblewright." — `campaign/quests/act-ii/gralhund-villa/overview.md:40` (quest-time)
Not a conflict on the base stat. The page gives no CR. Do not give CR 3 as his base.

**D12. Timing of the kidnapping.**
> "Volo met {@creature Floon Blagmaar|WDH} for drinks at the Skewered Dragon two nights ago. They drank and gambled for a few hours, and then Volo left. That's the last he saw of Floon." — `sources/adventure-wdh.json:1686`
> "Floon Blagmaar is taken on the night before Ches 1. The published adventure says \"two nights\"; the campaign settled on \"last night\"." — `campaign/setting/history/08-the-players-arrive.md:64`
The campaign uses "last night" (`history/08` line 64).

**D13. Who is the Zhentarim squad at the villa.** Covered by D1 and D2. The published adventure has "the local leaders of the Black Network (with Urstul Floxin chief among them) reside with them in the family villa" (`sources/adventure-wdh.json:32446`). The organization page says "A squad of Manshoon's Zhentarim lives at the villa under Urstul Floxin" (`campaign/setting/organizations/12-house-gralhund.md:49`). The Gralhund quest journal says he "arrived on the night of Ches 24th" (`campaign/quests/act-ii/gralhund-villa/overview.md:28`).

**D14. Not a conflict, for the record.** `campaign/setting/notable-figures/gralhunds/01-yalah-gralhund.md:15` says "without Manshoon discovering she considers Urstul an underling." Its line 21 says "Deep down, she pried the Stone from Floxin at sword-point and holds it herself." The line 21 clause is quest-time (E).

---

## E. Stale lines in other files (not edited) and routed quest references

Stale under ruling 1 (quest-time, or conflicting with a day-one restatement):
- `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:11`: "frustration with his slipperiness across multiple arcs" (retired vocabulary, "Quests, not arcs").
- `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:21`: "runs both the Dalakhar capture attempt and the Gralhund Villa operation" (quest-time, C).
- `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:25`: "the antagonist who drives **Fireball!** and **Gralhund Villa** before the party can identify his master" (quest-time, C).
- `campaign/setting/notable-figures/gralhunds/01-yalah-gralhund.md:21`: "Deep down, she pried the Stone from Floxin at sword-point and holds it herself" (quest-time).
- `campaign/setting/villains/manshoon.md:61`: "trusted with the Stone recovery at Gralhund Villa; his failure there is the first crack" (quest-time).
- `campaign/setting/villains/manshoon.md:69`: "Urstul Floxin ran the Dalakhar capture attempt and the **Gralhund Villa** operation." (quest-time).
- `campaign/gazetteer/waterdeep/north-ward.md:73`: "Yalah holds the Stone of Golorr, which she took from Urstul Floxin at sword-point." (setting page, quest-time).
- `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:39`: "By the night of Ches 24, when Floxin's strike team hits **Gralhund Villa**, Manshoon's cell knows the Gralhunds hold the Stone." (setting page, quest-time).
- `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:63`: "| Ches 24 | Urstul Floxin strikes Gralhund Villa at nightfall | **Gralhund Villa** | The quest opens |" (setting page timeline).
- `campaign/guides/gm-guide/structural-rules.md:47`: "| Ches 24 | Urstul Floxin strikes Gralhund Villa | **Gralhund Villa** opens |" (guide timeline).
- `campaign/guides/factions/10-manshoons-zhentarim.md:19`: "Parties that searched Urstul Floxin's effects at Gralhund Villa have documents pointing to Brindul Alley." (quest-time).
- `campaign/setting/history/08-the-players-arrive.md:65`: "Urstul Floxin's cell led the kidnapping and fled to Kolat Towers before the quest begins." (pre-campaign; conflicts with `campaign/setting/organizations/12-house-gralhund.md:49`, D1).
- `campaign/setting/organizations/12-house-gralhund.md:172` already routes "Yalah taking the Stone from Urstul Floxin at sword-point" to **Gralhund Villa**. No edit needed.

Routed quest references (the page should not narrate these; they live in the quest files):
- Gralhund Villa: `campaign/quests/act-ii/gralhund-villa/overview.md:28, 40, 46`; `ev-02-saerdoun-street.md:41, 43, 47, 72-74`; `ev-03c-night-infiltration.md:68`; `ev-04-the-zhentarim-raid.md:16, 20, 42, 64, 98-99, 113, 121`; `ev-05-the-guest-suite.md:8, 12, 16-33, 79`; `ev-09-aftermath.md:40, 44, 57`.
- Fireball!: `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:32, 62-68, 94, 104, 116, 120, 175, 219`; `overview.md:27, 34, 60`; `ev-04-the-sea-maidens-faire.md:134`; `ev-06-the-death-mark.md:52, 58`.
- Finding Floon: `campaign/quests/act-i/finding-floon/overview.md:31`; `design-notes.md:9`.
- Doom Raiders quests: `s01-davils-arrest/ev-01-davils-arrest.md:24-27, 114-115, 130, 134`; `m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:28`; `m04-silencing-skeemo/design-notes.md:15`; `r25-ardragon/ev-01-ardragon.md:23`; `s02-davils-return/design-notes.md:17`.
- Faction Outposts: the Factions Guide response-team entry (`campaign/guides/factions/10-manshoons-zhentarim.md:13`) and the Directive (`10-manshoons-zhentarim.md:63`: "- *Directive to Urstul Floxin* (Response Team: Urstul Floxin — names Avareen in Brindul Alley)").
- Kolat Towers: `campaign/structure/arc-i-kolat-towers.md:152` ("**E5 — Laboratory.** Urstul Floxin is here if he survived **Gralhund Villa**.") and `sources/adventure-wdh.json:26763` (Urstul at area E5 as a lieutenant to be captured).
- Sea Maidens Faire: `campaign/structure/arc-h-sea-maidens-faire.md:204` ("**The Strike Team.** Urstul Floxin (if alive from **Gralhund Villa**; if dead, replaced by Vevette Blackwater) + 1 lieutenant + 4 thugs.").
- Lords' Alliance: `campaign/quests/faction-events/lords-alliance/r25-warduke/ev-01-warduke.md:203` ("The third Splinter crew appears only if Urstul Floxin survived **Gralhund Villa**.").
- Faction mission: `sources/Appendix_B_-_Player_Factions.md:658` ("Neutralize a named Manshoon operative (+2). Eliminate or capture one of Manshoon's lieutenants — Urstul Floxin, Vevette Blackwater, Agorn Fuoco, or any other named agent.").
- Tavern: `sources/Appendix_D_-_Running_the_Tavern.md:1549` ("Urstul Floxin does not visit the tavern unless he is specifically hunting the characters for the Gralhund Villa incident.").
- Trollskull response teams: `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:40` ("Urstul Floxin only visits if specifically hunting the party for the Gralhund Villa incident.").
- Warrant: `campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:115` (D8).

Outcome names to route, not to write: "Floxin Alive" and "Floxin Captured" (`campaign/quests/act-ii/gralhund-villa/ev-04-the-zhentarim-raid.md:98-99`); "Floxin Status" (`campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:28`; `s01-davils-arrest/ev-01-davils-arrest.md:24-27`); "Gralhund Villa Named" (`campaign/quests/act-ii/fireball/ev-01-the-fireball.md:219`).

---

## F. Gaps a Background would need that no source gives

For each gap, the sourced facts the drafter must stay consistent with.

1. **Birthplace, upbringing and family.** No source gives a birthplace or family. Sourced: "Illuskan" ethnicity (wiki line 15) and "home = Waterdeep, Sword Coast North" (wiki line 11). Wiki infobox lines for parents, spouses, siblings and children are blank. Consistency: nothing may give him a different ethnicity or home city.
2. **How he became an assassin and joined the Black Network.** No source. Sourced: "Assassin" (wiki line 16; `sources/adventure-wdh.json:32652`); "high-ranking member of the [[Zhentarim]] in [[Waterdeep]] in the early 1490s [[DR]]" (wiki line 62). Consistency: the cell was built over about two years (`campaign/setting/history/08-the-players-arrive.md:32`: "The clone then spent two years building the Splinter cell, which is about 1490 DR counted back from Ches 1, 1492 DR.").
3. **How he met Manshoon and came under his command.** No source. Sourced: "works for Manshoon" (`sources/adventure-wdh.json:32644`), "the employer of Urstul Floxin" (`campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:26`), and "cannot name Manshoon" (`campaign/setting/villains/manshoon.md:69`). Consistency: he has never seen his master face to face (`ev-05-the-guest-suite.md:33`), so an origin story must not include a meeting.
4. **Rise and rank history.** No source. Sourced: "highest-ranking member of the Zhentarim squad stationed at House Gralhund" (`sources/adventure-wdh.json:32644`) and "chief field operative" (`campaign/setting/organizations/09-manshoons-zhentarim.md:58`). Consistency: D2 (leader versus not leader).
5. **Former punishment.** `sources/adventure-wdh.json:30041`: "He is being punished for allowing the {@item Stone of Golorr|WDH} to slip through his fingers (during the events of chapter 3)." Quest-time, Kolat Towers. Not day one.
6. **Faith or god.** No source gives him a deity or rites. The organization page's Beliefs section says "The campaign files give the cell no creed, oath or rites." (`campaign/setting/organizations/09-manshoons-zhentarim.md:46`). Consistency: none.
7. **Friends, lovers, companions.** No source for Floxin. Named underlings are Bashekk Ortallis and Wern Malkrave (`campaign/quests/act-ii/fireball/ev-01-the-fireball.md:94`), who are listed as "(deceased)" in `campaign/quests/act-ii/fireball/overview.md:44`. Consistency: a backstory may not make them alive.
8. **Fears.** No source names a fear. Sourced: "desperate cunning when cornered" (`02-urstul-floxin.md:13`). Quest-time: "Floxin is not a martyr" (`sources/Act_III_Arc_E.md:596`).
9. **Personal goals beyond the Stone.** No source. Sourced faction goal: "Urstul wants to recover the Stone of Golorr for Manshoon, maintain operational control of the field team, and survive encounters with the party by any means necessary, including hostage-taking." (`02-urstul-floxin.md:15`). Consistency: Motivations and Emotions stay verbatim (ruling 3). A personal goal must not reveal or change the Stone, the Eyes, Manshoon's name, any Event Outcome or the Grand Game balance (ruling 17). The Gralhund and Doom Raiders files make his fate depend on the raid, so a goal should not depend on his survival past Ches 1. Anything invented carries `[design]`.
10. **Where he sleeps on Ches 1.** Conflict (D1). No tie-breaker in the sources.
11. **The flying snakes.** Sourced: "He has a collection of black {@creature flying snake||flying snakes} that he uses as couriers" (`sources/adventure-wdh.json:32645`). No source says when or from whom he got them.
12. **His time in Waterdeep before Ches 1.** Sourced: the Dock Ward surveillance by Staget (`campaign/setting/organizations/11-open-lords-watch.md:25`), and the Dock Ward warehouse as the cell's place (`sources/adventure-wdh.json:1687`).
13. **Pre-campaign history with Dalakhar, the Stone and the Eyes.** Sourced: "Urstul Floxin's Zhentarim cell is tracking him." (`campaign/setting/history/08-the-players-arrive.md:24`). The Stone's history before Dalakhar is in `history/08` and is not Floxin's.
14. **Training.** Sourced: Common, Orc and thieves' cant (`sources/adventure-wdh.json:32657`). No training source.
15. **Appearance beyond build.** Sourced: "large, heavyset", "in his forties" (`sources/adventure-wdh.json:32645`). No hair, eyes, scars or clothing before the quest. Quest-time: "badly burned" (`campaign/quests/act-ii/fireball/ev-01-the-fireball.md:32`) and "50 hit points remaining" (`sources/adventure-wdh.json:5952`). Do not write the burns as a day-one feature.
16. **Pronunciation.** Sourced: "UR-stool FLOX-in" (`sources/adventure-wdh.json:342`).

---

## G. Inner-life hints (exact quotes)

These are the source facts that hint at habits, loyalty, grudges or a person he cares about. Each is quoted in full or as an exact fragment. The note says whether it is day one or quest-time.

- Habit with animals (day one): "he keeps a collection of black flying snakes as couriers because he trusts animals more than people." — `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:21`
- Habit with animals (day one, voice): "He talks to his flying snakes more gently than to people." — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:39`
- Pride and contempt (day one, published): "Urstul is a glorified thug with all the charm and breeding of a snake" — `sources/adventure-wdh.json:32644`
- Possessiveness (day one): "territorial possessiveness (he storms about Gralhund Villa like he owns it)" — `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:13`
- Refusal to name his master (day one): "absolute refusal to name his master." — `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:13`
- Grudge (day one, published, Doom Raiders briefing): "The botched kidnapping of {@creature Renaer Neverember|wdh} won't sit well with Urstul. He might try again. (Tashlyn doesn't actually believe this, but she knows that Renaer has ties to the Harpers and might share information of interest with the characters.)" — `sources/adventure-wdh.json:4035`
- Loyalty (quest-time, Kolat Towers): "Nevertheless, he remains loyal to {@creature Manshoon|WDH}." — `sources/adventure-wdh.json:30041`
- Loyalty (day one, wiki, with a quest-time clause): "Urstul was truly loyal to Manshoon, even after being punished." — `scratchpad/wiki-manshoons-zhentarim/02-urstul-floxin.txt:78`
- Grudge (quest-time, Alexandrian aftermath): "Floxin does not forget and does not forgive. He will be looking for them." — `sources/Act_III_Arc_E.md:892`
- Self-preservation (quest-time, Alexandrian): "He would rather live and plan than die heroically over a Stone he no longer has any certainty about." — `sources/Act_III_Arc_E.md:596`
- Watchfulness (quest-time): "Floxin is at the G15b door, shoulder into the wood, boot following, reading each impact for where the barricade is weakest. He is focused." — `campaign/quests/act-ii/gralhund-villa/ev-05-the-guest-suite.md:18`
- Luggage (quest-time, Gralhund Villa G15): "Floxin's luggage occupies the wardrobe — traveling clothes, a locked case (DC 14 thieves' tools) that holds a set of thieves' tools, a hand-drawn map of the North Ward with three properties marked (none of them Gralhund Villa), and a folded document in cipher." — `campaign/locations/gralhund-villa/g15-guest-suite.md:21`
- Coat (quest-time): "Floxin's traveling coat is on the rack — it has been there since Ches 22nd; he wasn't permitted to take it when Yalah had him disarmed." — `campaign/locations/gralhund-villa/g15-guest-suite.md:11`
- Yalah's view of him (day one): "without Manshoon discovering she considers Urstul an underling" — `campaign/setting/notable-figures/gralhunds/01-yalah-gralhund.md:15`
- Lady Gralhund's secret view of him (quest-time; a Gralhund Villa secret; do not reveal): "Believing that {@creature Urstul Floxin|WDH} is after the gold for himself, Yalah plans to cut Urstul out of the deal and deliver the {@item Stone of Golorr|WDH} to {@creature Manshoon|WDH} herself." — `sources/adventure-wdh.json:4812`

No source gives him a place or person he cares about, a lost love, a child, a debt he is still paying, or a childhood fear. Those are for the drafter's `[design]` tag under ruling 17.

---

## Cross-references (file:line)

Campaign setting and guides:
- `campaign/setting/organizations/09-manshoons-zhentarim.md:33`, `:42`, `:58`, `:64`, `:90`, `:100`, `:169` (quoted in A, B, D).
- `campaign/setting/organizations/12-house-gralhund.md:49`, `:66`, `:158`, `:172`. `:158`: "- **Conflicts:** Urstul and Yalah, who is the underling." `:172`: "- **Routed to quests:** Yalah taking the Stone from Urstul Floxin at sword-point (`01-yalah-gralhund.md:21`, `north-ward.md:73`, `adventure-wdh.json:4804`). It belongs to **Gralhund Villa**, and the two day-one notes should be reworded."
- `campaign/setting/organizations/11-open-lords-watch.md:25` (quoted in A).
- `campaign/setting/organizations/06-doom-raiders.md:39`, `:88`, `:115` (quoted in A).
- `campaign/setting/organizations/01-harpers.md:177` (quoted in D9).
- `campaign/setting/villains/manshoon.md:9` (the Manshoon name is given at the Interrogation House; not Floxin's), `:61`, `:69` (quoted).
- `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:26` (quoted in A).
- `campaign/setting/notable-figures/gralhunds/01-yalah-gralhund.md:15`, `:21`, `:25` (quoted in A, D14, E).
- `campaign/setting/history/08-the-players-arrive.md:24`, `:32`, `:56`, `:57`, `:64`, `:65`, `:66` (quoted in A, D1, D12, E).
- `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:63` (quoted in E).
- `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:25`, `:39` (quoted in A, E).
- `campaign/setting/deities/bane.md:73`: "Until the party marks **Manshoon Named**, even the Doom Raiders say \"Floxin's cell\" or \"the other cell\" and call Kolat Towers \"the towers in the Southern Ward\"." (a quest-time gate; not Floxin's)
- `campaign/gazetteer/waterdeep/north-ward.md:39`, `:73`, `:254`: `:39` "- A party that searched Urstul Floxin's effects at Gralhund Villa holds documents that name the alley. Any other party can find the house by canvassing the ward for a day (DC 14 Investigation, no faction membership needed), and Zhentarim response teams carry orders to take their prisoners here."; `:254` "- **Avareen Windrivver**, **Urstul Floxin**: the Zhentarim operatives tied to the Interrogation House and the villa."
- `campaign/locations/gralhund-villa/area-overview.md:18`, `:80` (quest-time; `:80`: "| G15a | Urstul Floxin (50 hp, no poison), 1 Zhent thug | Trying to breach G15b |").
- `campaign/locations/gralhund-villa/g05-kitchen.md:7`, `g06-pantry.md:9`, `g09-parlor.md:7`, `:13`, `:15`, `g15-guest-suite.md:11`, `:15`, `:21`, `:23` (quest-time; quoted in D1, G).
- `campaign/guides/factions/10-manshoons-zhentarim.md:13`, `:19`, `:52`, `:54`, `:63`, `:68` (quoted in B, C, E).
- `campaign/guides/factions/13-house-gralhund.md:17`, `:75`, `:118`, `:119` (`:118` and `:119` cite `ev-09-aftermath.md:44`, `ev-09-aftermath.md:142`, and the Alexandrian `2. Other Factions.pdf` p. 21, which was not checked).
- `campaign/guides/factions/12-open-lords-watch.md:100`: "- **A witness.** The Watch releases a witness it holds, such as Urstul Floxin, within 24 hours, because it has no grounds to keep him."
- `campaign/guides/gm-guide/running-the-villains.md:39`, `:50`.
- `campaign/guides/gm-guide/structural-rules.md:47` (quoted in E).
- `campaign/guides/gm-guide/debts-of-the-city.md:55`: "Urstul Floxin is Manshoon's chief field operative in Waterdeep: a large, heavyset Illuskan man in his forties who moves through rooms as though he owns them and reserves his anger for moments when it will accomplish something." `:62`: "Floxin works for Manshoon, not the Doom Raiders. A character whose Debt is held by Floxin is already entangled with the campaign's primary villain faction, whether they know it or not."
- `campaign/guides/players-guide/debts-of-the-city.md:41` (the Debt text).
- `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:40` (quoted in E).

Campaign quests:
- `campaign/quests/act-i/finding-floon/overview.md:31`; `design-notes.md:9` ("The Candle Lane warehouse belongs to Manshoon's cell, Urstul Floxin's people, operating separately from Davil.").
- `campaign/quests/act-ii/fireball/overview.md:27`, `:34`, `:44`, `:60`; `ev-01-the-fireball.md:32`, `:60`, `:62-68`, `:94`, `:104`, `:116`, `:120`, `:175`, `:184`, `:219`; `ev-04-the-sea-maidens-faire.md:134`; `ev-06-the-death-mark.md:52`, `:58`; `design-notes.md:15`, `:21`.
- `campaign/quests/act-ii/gralhund-villa/overview.md:28`, `:40`, `:46`; `ev-02-saerdoun-street.md:41`, `:43`, `:47`, `:72`, `:74`; `ev-03-daytime-infiltration.md:28`, `:97`; `ev-03c-night-infiltration.md:56`, `:68`, `:70`, `:79`; `ev-04-the-zhentarim-raid.md:6`, `:9`, `:12`, `:16`, `:20`, `:28`, `:36`, `:38`, `:42`, `:46`, `:57`, `:64`, `:87`, `:89`, `:91`, `:98-99`, `:103`, `:113`, `:121`; `ev-05-the-guest-suite.md:8`, `:12`, `:16`, `:18`, `:20`, `:24`, `:26`, `:28`, `:30`, `:33`, `:37`, `:69`, `:79`; `ev-06-the-gralhund-confrontation-day.md:19`, `:28`, `:65`; `ev-07-the-gralhund-confrontation-night.md:23`, `:30`, `:51`, `:75`; `ev-09-aftermath.md:40`, `:44`, `:57`; `design-notes.md:23`, `:37`.
- `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:21`, `:23`, `:195`, `:258`, `:262`, `:268`, `:432`; `design-notes.md:11`, `:13`.
- `campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/ev-01-the-dockside-killer.md:76`.
- `campaign/quests/faction-events/doom-raiders/m04-silencing-skeemo/design-notes.md:15`; `ev-02-the-chase.md:155`; `ev-03-the-reckoning.md:176`; `overview.md:25`.
- `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:27`, `:28`, `:50`, `:56`, `:106`, `:110`, `:112`, `:116`, `:122`; `ev-02-the-debrief.md:25`; `overview.md:10`, `:28`, `:32`.
- `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md:26`.
- `campaign/quests/faction-events/doom-raiders/r03-wolf/design-notes.md:7`; `r25-ardragon/ev-01-ardragon.md:23`, `:170`; `r50-dread-lord/ev-01-dread-lord.md:82`.
- `campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:8`, `:24`, `:26`, `:27`, `:114`, `:115`, `:124`, `:130`, `:134`, `:154`, `:224`, `:291`; `design-notes.md:5`, `:11`, `:13`.
- `campaign/quests/faction-events/doom-raiders/s02-davils-return/design-notes.md:17`; `ev-01-davils-return.md:102`.
- `campaign/quests/faction-events/lords-alliance/r25-warduke/ev-01-warduke.md:198`, `:203`.

Structure docs (superseded by quest journals; cross-reference only):
- `campaign/structure/arc-a-finding-floon.md:45`, `:235`; `arc-c-fireball.md:57`, `:86`, `:255`, `:307`, `:321`, `:358`; `arc-d-gralhund-villa.md:29`, `:162`, `:227`, `:351`, `:400`, `:420`, `:463`; `arc-e-faction-outposts.md:117`; `arc-h-sea-maidens-faire.md:204`; `arc-i-kolat-towers.md:152`, `:320`; `ch1-beginning.md:182` (retired).

Alexandrian markdown:
- `sources/Act_III_Arc_D.md:26`, `:36`, `:39`, `:59`, `:165`, `:224-226`, `:241-242`, `:251`, `:477`, `:634`, `:665-667`.
- `sources/Act_III_Arc_E.md:13`, `:72`, `:262`, `:393-405`, `:512-515`, `:594-596`, `:612-631`, `:648`, `:685-689`, `:892`.
- `sources/Appendix_B_-_Player_Factions.md:658`; `sources/Appendix_D_-_Running_the_Tavern.md:1549`.
- `sources/SOURCE_GUIDE.md:35` (Chapter 8 lists Urstul Floxin among the Kolat Towers cast) and `:190`.

Published adventure (`sources/adventure-wdh.json`): 341-342, 862, 1686-1687, 2183-2185, 4032-4035, 4368-4380, 4480, 4543-4545, 4791-4792, 4803-4816, 4836-4837, 5796-5797, 5951-5954, 26762-26763, 30033-30042, 32445-32446, 32640-32657, 32782.

Wiki (`scratchpad/wiki-manshoons-zhentarim/02-urstul-floxin.txt`): lines 11-19, 57-65, 75, 78, 81 (quoted above).

---

## Not found

Searched `Urstul`, `Floxin` and `Urstul Floxin` across `campaign/` (all subfolders), `sources/adventure-wdh.json`, `sources/SOURCE_GUIDE.md`, `sources/Act_III_Arc_D.md`, `sources/Act_III_Arc_E.md` and `sources/Appendix_B/C/D`. Gaps, which the drafter would have to invent or tag `[design]`:
- Birthplace, parents, siblings, children, spouse (wiki infobox blank; no other source).
- Any career or employer before the Black Network.
- The year he joined the Black Network, the year he took his post, length of service.
- How he met or was recruited by Manshoon.
- Faith, deity, oath, rite (no source).
- Friends or lovers (only the dead underlings Bashekk Ortallis and Wern Malkrave).
- Named fears, losses or grudges before the campaign (the Renaer grudge at `sources/adventure-wdh.json:4035` is the only one).
- Hair, eyes, scars, clothing before the quest (only build and age).
- Floxin in `campaign/setting/lore/`, `governance-and-guilds/`, or `notable-figures/` outside the Manshoon and Gralhund folders (no hits). `deities/bane.md:73` names only "Floxin's cell".
- Appendix C (Player Faction Missions): no match. Appendix B has one entry (line 658). Appendix D has one entry (line 1549).
- A residence on Ches 1 that all sources agree on (D1).

Matched in file lists but not opened for this report: `sources/research/pass3-bundles/stone-of-golorr-and-the-eyes/wiki.txt`, `pass3-bundles/vault-of-dragons/wiki.txt`, `pass5-bundles/gralhunds/wiki.txt`, `pass5-bundles/doom-raiders/wiki.txt`, and the `campaign-hits.txt` and `adventure-hits.txt` files in the pass 3, 4 and 5 bundles.

## Not readable

- `.docx` files cannot be opened with these tools. These are in `sources/Other remix files/` (listed at `sources/SOURCE_GUIDE.md:683-698`). They may mention Floxin:
  - `Renaer Neverember Guide, his backstory and family secrets.docx` (`SOURCE_GUIDE.md:693`; "Finding Floon, Gralhund Villa").
  - `Davil and the Doom Raider Zhents + Elf Killer mission and more.docx` (`SOURCE_GUIDE.md:688`; the Zhentarim (Doom Raiders) page).
  - `The Waterdavian's Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx` (`SOURCE_GUIDE.md:695`; "Secondary reference only").
- Alexandrian PDFs read: `sources/4. Gralhund Villa.pdf` (PDF pages 1-4, printed pp. 26-29; transcribed from page images, flag for `pdftotext`); `sources/1. The Villains.pdf` (all 7 PDF pages, printed pp. 13-19; no mention of Floxin).
- Alexandrian PDFs not read: `sources/2. Other Factions.pdf` (p. 21 is cited at `campaign/guides/factions/13-house-gralhund.md:119`), `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, `sources/13. Clues and Timelines.pdf`, `sources/14. Finding Floon.pdf`, `sources/15. The Nimblewright Investigation.pdf`, `sources/16. Backtracking Dalakhar  Kalain.pdf`, `sources/17. Outpost and Lair Revelation Lists.pdf`. The Kolat Towers and Finding Floon PDFs may hold Floxin material and should be checked.
- Model pages `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md` and `11-gorath.md` were not opened (format inputs).
- The Ott notes file named in the generic instructions is not at the path given (see Method).
- Not run: `voicecheck.py` (research only; no prose written).
