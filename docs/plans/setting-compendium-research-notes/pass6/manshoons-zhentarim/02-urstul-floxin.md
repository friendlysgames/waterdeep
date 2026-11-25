# Pass 6 research notes: Urstul Floxin

Target page: `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md`
Group folder: `manshoons-zhentarim`. Faction page: `campaign/setting/organizations/09-manshoons-zhentarim.md`. Villains page: `campaign/setting/villains/manshoon.md`. Voice doc: `.claude/skills/character-voices/voices/manshoons-zhentarim.md`.

Method and limits:
- Read: the brief (`docs/plans/setting-compendium-pass6-brief.md`, rulings 1, 3, 15 to 17 and the user rulings), the target page, the organization page, the voice profile, the Villains page, the extracted wiki page (`/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-manshoons-zhentarim/02-urstul-floxin.txt`), and the Gralhund Villa, Fireball!, Finding Floon and Doom Raiders quest journals where Floxin appears.
- The file `docs/plans/setting-compendium-research-notes/pass6/manshoons-zhentarim/06-ott-steeltoes.md` does not exist at the path the generic instructions give. The Ott notes that do exist are at `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md`. The sections A to G below follow the generic instructions.
- Model pages `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md` and `11-gorath.md` were not opened. They are format inputs for the drafter and hold no Floxin facts that this report needs.
- `sources/adventure-wdh.json` line numbers come from Grep and Read output. Wiki line numbers come from the extracted text file. PDF quotes were transcribed from page images and are flagged for a `pdftotext` check.
- Edition: the published adventure is 5e *Waterdeep: Dragon Heist*. The wiki cites WDH 5e p. 216 for the infobox.

## Summary of the day-one state (Ches 1, 1492 DR)

- Who he is: an Illuskan human assassin, lawful evil, male, in his forties, the chief field operative of Manshoon's Zhentarim, who will not name his master (sources in A, B and D).
- Where he lives on Ches 1 is **in conflict** between sources (D1). Do not write a residence until the orchestrator chooses.
- Day one, the cell tracks Dalakhar and the Stone (A9). The Stone's path is quest-time (C and E).
- The night before Ches 1, his cell took Renaer and Floon. That night is pre-campaign and is told on the setting page `history/08-the-players-arrive.md` (A10). The rescue and the warehouse raid are Finding Floon events.
- Gralhund Villa, the raid, his outcome (**Floxin Alive**, **Floxin Captured**, or the **Floxin Status** values in the Doom Raiders text) and the Kolat Towers appearance are all routed (C, E).

---

## A. Background facts by theme

### Origin and identity

> "{@creature Urstul Floxin|wdh} is an Illuskan human {@creature assassin}, with these changes:"
> — `sources/adventure-wdh.json:32652` (Appendix B entry, p. 216 per the JSON `"page": 216` at line 32641)

> "| home           = [[Waterdeep]], [[Sword Coast North]]"
> — `.../wiki/02-urstul-floxin.txt:11` (wiki infobox; 5e infobox edition)

> "| race           = [[Human]]"
> "| ethnicity      = [[Illuskan]]"
> — `.../wiki/02-urstul-floxin.txt:14` and `:15`

> "| occupation     = Assassin<ref name="WDH5e-p216" />"
> — `.../wiki/02-urstul-floxin.txt:16`

> "| languages      = [[Common]], [[Orc language|Orc]]"
> — `.../wiki/02-urstul-floxin.txt:19`

> "He speaks Common and Orc and knows thieves' cant."
> — `sources/adventure-wdh.json:32657` (list item under Game Statistics)

> "{@creature Urstul Floxin|WDH}", "UR-stool FLOX-in"
> — `sources/adventure-wdh.json:341-342` (pronunciation key entry; the two items are separate array strings)

> "Illuskan human assassin, lawful evil, he/him"
> — `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:5` (Gamemaster's Summary; the page's own line, italic)

### Appearance and age

> "{@creature Urstul Floxin|wdh} works for {@creature Manshoon|WDH}, and he is the highest-ranking member of the Zhentarim squad stationed at House Gralhund. Urstul is a glorified thug with all the charm and breeding of a snake, but the Gralhunds tolerate him because he feeds them useful information culled from his spies throughout the city. Urstul takes his orders from {@creature Manshoon|WDH}'s current simulacrum, which comes and goes from House Gralhund by way of a teleportation circle (connected to the circle in Kolat Towers)."
> — `sources/adventure-wdh.json:32644` (rest of the passage: the appendix entry continues below; see B and D)

> "Urstul is a large, heavyset man in his forties. He storms about House Gralhund like he owns the place. He has a collection of black {@creature flying snake||flying snakes} that he uses as couriers to deliver messages to underlings throughout the city."
> — `sources/adventure-wdh.json:32645`

> "A large, heavyset man in his forties who carries himself as though every room belongs to him. He works for the Zhentarim and makes no effort to hide it, though he will not name who gives him orders."
> — `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:29` (Overview; "the Zhentarim" here is not qualified, see D8)

> "Urstul Floxin ... a large, heavyset man in his forties" (the same description in the Doom Raiders briefing):
> "Urstul Floxin is a big, heavy man in his forties who has killed for the Black Network for years. Rumour says he leads the renegade cell, the other Zhentarim in this city, but I can't prove it and I don't like guessing."
> — `campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:130` (quest-time event text; a Doom Raiders NPC's opinion; see C)

> "> - *Illuskan human assassin, lawful evil, he/him*."
> "... "Urstul is lawful evil." ..." (see B)

### Rank and post

> "'''Urstul Floxin''' ({{Pronounce|UR|stool|_|FLOX|in|refs=<ref name="WDH5e-p4">{{Cite book/Waterdeep: Dragon Heist|4}}</ref>}}) was a high-ranking member of the [[Zhentarim]] in [[Waterdeep]] in the early 1490s [[DR]].<ref name="WDH5e-p216" />"
> — `.../wiki/02-urstul-floxin.txt:62` (wiki; WDH 5e p. 216)

> "In {{Yearlink|1492}},{{WDH-time}} Urstul Floxin was the leader of the Zhents headquartered in the villa of the [[Gralhund]] family. From there, he directed the search for the ''[[Stone of Golorr]]'', which was in possession of the [[gnome]] [[Dalakhar]].<ref name="WDH5e-p44">{{Cite book/Waterdeep: Dragon Heist|44}}</ref>"
> — `.../wiki/02-urstul-floxin.txt:65` (wiki; WDH 5e p. 44; the 1492 wording is the wiki's, and it conflicts with the campaign, see D2)

> "> - **Manshoon's Zhentarim** (ally of convenience)..." (not used; see D1)

> "- **Lieutenants and field teams:** Urstul Floxin is the chief field operative and leads the thugs who work the streets. Vevette Blackwater coordinates strike teams from Kolat Towers and leads the forces that fight Xanathar's Guild, and in the published adventure Agorn Fuoco leads those that fight the Zhents who are not loyal to Manshoon (**Vevette Blackwater**; *Dragon Heist*, 5e). Vira Solkan is a plant inside Blackstaff Tower (**Castle Ward**)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:58`

> "- **Urstul Floxin** — Illuskan human assassin, lawful evil, and Manshoon's chief field operative. He is the thuggish leader of the cell's field teams, and his team is tracking Dalakhar, the gnome moving the Stone of Golorr. See the **Urstul Floxin** page in Notable Figures."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:100`

> "Urstul Floxin is Manshoon's chief field operative, a temporary occupant of Gralhund Villa (where he treats Yalah as an underling), and the antagonist who drives **Fireball!** and **Gralhund Villa** before the party can identify his master."
> — `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:25` (Relationships; the "temporary occupant" and "drives" clauses are D1 and C)

> "Urstul Floxin ... a Zhent field commander" (Fireball! overview, quest-time; the quest-time reading is routed in C):
> "- **Urstul Floxin** (Manshoon's Zhentarim) — Zhent field commander; survived the blast; gives his real name; wants the party to track the Stone so his cell can follow"
> — `campaign/quests/act-ii/fireball/overview.md:27`

### Inner life and standing with Manshoon (day one)

> "Urstul works for Manshoon, and he" (see the full passage at `sources/adventure-wdh.json:32644` above)

> "**Relationships.** Manshoon is the leader of the Zhentarim splinter cell, the employer of Urstul Floxin, Sidra Romeir, and Vevette Blackwater, a blackmailer of Masked Lords Jelenn Urmbrusk and Corylus Thann, and a clone-wizard whose response teams are deliberately the weakest in muscle because drawing attention is the one mistake he will not make twice."
> — `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:26`

> "> Urstul is Manshoon's chief field operative..." (see the Relationships quote above)

> "Urstul was truly loyal to Manshoon, even after being punished.<ref name="WDH5e-p159" /> He was a charming and dangerous individual.<ref name="WDH5e-p216" />"
> — `.../wiki/02-urstul-floxin.txt:78` (wiki; "even after being punished" is quest-time, see C and G)

> "| Urstul Floxin | Field lieutenant | Most effective operative; trusted with the Stone recovery at Gralhund Villa; his failure there is the first crack |"
> — `campaign/setting/villains/manshoon.md:61` (the row's "trusted with the Stone recovery ... his failure there" clause is quest-time, see C)

> "- Urstul Floxin ran the Dalakhar capture attempt and the **Gralhund Villa** operation. In the published adventure he takes his orders from Manshoon's simulacrum, and in the campaign he cannot name Manshoon, because he knows only a code and a chain of dead drops."
> — `campaign/setting/villains/manshoon.md:69`

> "Urstul received his orders directly from a [[simulacrum]] of Manshoon. He had a collection of black [[flying snake]]s that he used as couriers.<ref name="WDH5e-p216" />"
> — `.../wiki/02-urstul-floxin.txt:81`

### Gralhund alliance and household (day one, pre-raid)

> "Less than a year ago, the Gralhunds were approached by agents of the Zhentarim loyal to {@creature Manshoon|WDH}, and the nobles formed an alliance with them. House Gralhund gives the Zhents coin and allows them to use the family's noble villa as a refuge. In exchange, the house reaps all the benefits that the Black Network offers, including intelligence that its spies have gathered. So while the Zhents use House Gralhund as a shield, the Gralhunds are using the Zhents to ascertain the identities and weaknesses of the Masked Lords."
> — `sources/adventure-wdh.json:32445`

> "The heads of the Gralhund noble family, {@creature Yalah Gralhund|wdh} and her husband, {@creature Orond Gralhund|wdh|Orond}, are providing coin and shelter to Urstul and his fellow Zhents in exchange for the promise of getting their fair share of the hidden cache of gold. But the Gralhunds aren't willing to put their trust entirely in the Black Network; they sent out their own agent to shadow the Zhents, eliminate Dalakhar, and obtain the {@item Stone of Golorr|WDH} on their behalf. Yalah gave the would-be assassin a {@item necklace of fireballs} with instructions on how and when to use it. When it seemed as though Dalakhar might give {@creature Urstul Floxin|wdh} the slip, this agent hurled one of the beads from the necklace to stop the gnome in his tracks."
> — `sources/adventure-wdh.json:4377` (the nimblewright passage follows at line 4378; the fireball part is quest-time, see C)

> "Orond doesn't fully grasp how entwined the Black Network and his family have become-it is now next to impossible to separate one from the other. It's no secret in Waterdeep that the Black Network has firmly rooted itself in House Gralhund. But what's not generally known is that the Zhents in House Gralhund are agents of {@creature Manshoon|WDH}. Neither Orond nor any other member of his family knows about the wizard's clone. As far as Orond and his wife are concerned, the local leaders of the Black Network (with {@creature Urstul Floxin|wdh} chief among them) reside with them in the family villa."
> — `sources/adventure-wdh.json:32446` (the whole paragraph; see D1 for the residence conflict)

> "A squad of Manshoon's Zhentarim lives at the villa under Urstul Floxin, the highest-ranking among them. Yalah treats them as her own spy network."
> — `campaign/setting/organizations/12-house-gralhund.md:49` (day-one residence claim, see D1)

> "- **House Gralhund (ally of convenience):** The Zhentarim use the villa as a shield and refuge, and the house uses them to learn the Masked Lords' identities and weaknesses (**House Gralhund**). Yalah Gralhund treats Urstul Floxin as a sub-employee..." (see the actual text below)
> — the actual text is: "- **House Gralhund (ally of convenience):** The Zhentarim use the villa as a shield and refuge, and the house uses them to learn the Masked Lords' identities and weaknesses (**House Gralhund**). Yalah Gralhund treats Urstul Floxin as an underling and does not know that Manshoon is the cell's master (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:90`

> "Before Gralhund Villa" / "- The house pays for the Zhentarim cell that shelters at its villa. Yalah treats the cell's leader, Urstul Floxin, as an employee and doesn't know that Manshoon is its master."
> — `campaign/guides/factions/13-house-gralhund.md:17` (D1)

> "Yalah shares the services of a half-orc bodyguard with her husband ... Most of her dealings are with the Zhent master assassin {@creature Urstul Floxin|wdh} (see \"{@creature Urstul Floxin|WDH}\"), whom she treats as an underling."
> — `sources/adventure-wdh.json:32782` (full paragraph quoted in D6)

> "Until recently, this suite was set aside for the use of {@creature Urstul Floxin|wdh}. Lord Gralhund has barricaded himself in area G15b, using heavy furniture to block the door. Forcing it open requires a successful {@dc 18} Strength (Athletics) check."
> — `sources/adventure-wdh.json:5951` (the first sentence is the residence claim; the rest is quest-time, see C)

### Relationship to the cell's Dalakhar hunt (day one)

> "Dalakhar, the agent of Dagult Neverember, has the Stone and is carrying it toward Trollskull Manor. Urstul Floxin's Zhentarim cell is tracking him."
> — `campaign/setting/history/08-the-players-arrive.md:24`

> "- Xanathar's Guild knows Dalakhar was moving the Stone, though it does not know what the Eyes are. Urstul Floxin's Zhentarim cell was tracking him."
> — `campaign/setting/history/08-the-players-arrive.md:57`

> "| Manshoon's Zhentarim | The Stone exists and unlocks great wealth; Urstul Floxin's team was tracking Dalakhar; does not yet know the Stone reached the Gralhunds | Nothing | Stone + all three Eyes |"
> — `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:25` (the same row: `campaign/guides/gm-guide/running-the-villains.md:39`)

> "- **Lieutenants and field teams:** ..." (see above)

> "The Gralhunds' assassin is a {@creature nimblewright|wdh} ..." (quest-time; see C)

> "- **Manshoon's Zhentarim:** By the night of Ches 24, when Floxin's strike team hits **Gralhund Villa**, Manshoon's cell knows the Gralhunds hold the Stone."
> — `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:39` (quest-time sentence on a setting page, see E)

> "Three members of the Black Network, including the Zhent assassin {@creature Urstul Floxin|wdh} (see {@adventure appendix B|WDH|12}), were close to nabbing Dalakhar when they were caught in the blast."
> — `sources/adventure-wdh.json:4368` (quest-time, see C)

> "Dalakhar, a rock gnome spy, serves Dagult Neverember. He had questioned Kalain about Neverember's vault years before the campaign." — not about Floxin; not quoted.

> "The Stone's day-one holder: 'By the morning of Ches 22 Dalakhar has the Stone of Golorr and is carrying it to Trollskull Manor'" — `campaign/setting/history/08-the-players-arrive.md:56` (Ches 22 is quest-time, see C)

### Renaer and Floon (the night before Ches 1, pre-campaign)

> "Five Zhentarim thugs working for {@creature Urstul Floxin|wdh} (see {@adventure appendix B|WDH|12}) jumped both Floon and Renaer. They took them to a warehouse in the Dock Ward, so they could question Renaer-the son of Lord Dagult Neverember-about the whereabouts of the Stone of Golorr and his father's hidden cache of dragons. Before the interrogation could begin, members of the Xanathar Guild ambushed and killed the Zhent guards in the warehouse. The new arrivals mistook Floon for Renaer, knocked Floon {@condition unconscious}, and dragged him away while Renaer hid and escaped their notice."
> — `sources/adventure-wdh.json:1687` (the paragraph begins: "Unbeknownst to Volo, not long after he departed, a drunken Floon met another acquaintance, Lord {@creature Renaer Neverember|wdh}, at the tavern. ...")

> "- **The night before Ches 1, 1492 DR, Renaer Neverember:** Five Zhentarim thugs working for Urstul Floxin seized Renaer Neverember to learn what he knew about his father's hidden gold, and they took Floon Blagmaar in the same attack. House Gralhund paid for the operation (*Dragon Heist*, 5e; **House Gralhund**). Xanathar's Guild raided the Candle Lane warehouse where the thugs held both men and killed the cell's agents there (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:33`

> "Floon Blagmaar is taken on the night before Ches 1. The published adventure says "two nights"; the campaign settled on "last night"."
> — `campaign/setting/history/08-the-players-arrive.md:64`

> "- Urstul Floxin's cell led the kidnapping and fled to Kolat Towers before the quest begins. The City Watch has Splinter thugs under arrest at the Dock Ward scene."
> — `campaign/setting/history/08-the-players-arrive.md:65` (see D1)

> "- The cell seized Renaer's mourning locket and pried it open at the Candle Lane warehouse. Xanathar's Guild raided the warehouse the same night and carried off what it found in the back office, the Eye included, without knowing what the Eye was."
> — `campaign/setting/history/08-the-players-arrive.md:66` (the Eye part is not Floxin's, see E)

> "Volo met {@creature Floon Blagmaar|WDH} for drinks at the Skewered Dragon two nights ago." — `sources/adventure-wdh.json:1686` (the published "two nights" wording, see D12)

### Watch and Dock Ward (day one)

> "By the spring of 1492 DR brawls between Xanathar's Guild and the Zhentarim have become common in the Dock Ward, and the Watch is called to them often (**The Players Arrive**). The Dock Ward captain, Hyustus Staget, pulled a surveillance detail off a Zhent instigator named Urstul Floxin to strengthen street patrols, and he regrets it (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/11-open-lords-watch.md:25`

> "Staget once had the warehouse under surveillance, but elected to pull the detail to bolster patrols throughout the Dock Ward-a decision he now regrets. That surveillance was part of an attempt to catch a known Zhent instigator named {@creature Urstul Floxin|wdh}, a \"big fish\" rumored to be responsible for much of the recent strife. Staget doesn't share this information with strangers."
> — `sources/adventure-wdh.json:2185`

### Doom Raiders belief (day one)

> "- **Zhentarim (Doom Raiders) (enemy):** ... Davil, Yagra and the others believe Urstul Floxin leads the rival cell, so they do not know whom it serves (see GM Notes)."
> — the actual text: "`[research]` Davil, Yagra and the others believe Urstul Floxin leads the rival cell, so they do not know whom it serves (see GM Notes)."
> — `campaign/setting/organizations/06-doom-raiders.md:88`

> "- **What the Doom Raiders call the rival cell:** Manshoon directs the rival cell through Urstul Floxin, but no Doom Raider has heard his name connected to it. Davil, Yagra and the others believe that Floxin leads it, and they call it \"the other cell\", \"Floxin's cell\" or \"the Splinter\". The History above states the truth for the GM."
> — `campaign/setting/organizations/06-doom-raiders.md:115` (GM note; see D2)

> "The cell believes Urstul Floxin leads its rival and does not know whom he serves (see GM Notes)." — `campaign/setting/organizations/06-doom-raiders.md:39` (the leading clause is the belief)

### Habits, belongings and couriers (day one)

> "Persona... he keeps a collection of black flying snakes as couriers because he trusts animals more than people." — `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:21`

> "He has a collection of black {@creature flying snake||flying snakes} that he uses as couriers to deliver messages to underlings throughout the city." — `sources/adventure-wdh.json:32645`

> "- **Messengers:** Black flying snakes carry the cell's orders between its sites, and three of them nest at the Interrogation House while Urstul keeps a collection of his own (**North Ward**; **Urstul Floxin**)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:64`

> "- **Nobody Names the Master:** The street crews will not say who gives the orders, and few in the cell know their master's name. Urstul Floxin will not divulge it unless magically compelled, and he sends messages by black flying snake because he trusts animals more than people. Outsiders call the cell the Splinter."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:42`

> "Urstul Floxin's team tracks..." (none)

### Public standing and the Watch (day one)

> "Floxin is the name that keeps coming up, a large man in his forties who makes no effort to hide what he is." — this is a Doom Raiders briefing answer in `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:258`. Quest-time event text; the belief it reports is day-one (see C).

> "A warrant has been issued for Urstul's arrest, but his current whereabouts are unknown." — `sources/adventure-wdh.json:4034` (quest-time, see D8)

---

## B. Alignment, species, pronouns, stat block

| Field | Value | Quote and line |
|---|---|---|
| Alignment | Lawful evil | `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:5`: "*Illuskan human assassin, lawful evil, he/him*. Stat block: **Assassin**." |
| Alignment (published) | Lawful evil | `sources/adventure-wdh.json:32656`: "Urstul is lawful evil." |
| Alignment (wiki) | Lawful evil | `.../wiki/02-urstul-floxin.txt:57`: "| alignment5e    = [[Lawful evil]]" |
| Alignment (organization page) | Lawful evil | `campaign/setting/organizations/09-manshoons-zhentarim.md:100`: "Illuskan human assassin, lawful evil, and Manshoon's chief field operative." |
| Species | Human | `sources/adventure-wdh.json:32652`: "is an Illuskan human {@creature assassin}"; wiki line 14: "| race           = [[Human]]" |
| Ethnicity | Illuskan | `.../wiki/02-urstul-floxin.txt:15`: "| ethnicity      = [[Illuskan]]"; Notable Figures line 5 and published line 32652 agree |
| Pronouns | he/him | `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:5`: "he/him"; published `sources/adventure-wdh.json:32645`: "He storms about House Gralhund like he owns the place."; wiki line 13: "| sex            = Male" |
| Affiliation | Manshoon's Zhentarim | `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:6`: "> - **Affiliation:** Manshoon's Zhentarim" |
| Stat block | Assassin (MM p. 343 per the wiki) | `sources/adventure-wdh.json:32652`: "is an Illuskan human {@creature assassin}, with these changes:"; wiki line 59: "| class5e        = [[Assassin]]" and the MM citation in wiki line 60 |
| Challenge rating (wiki) | 8 | `.../wiki/02-urstul-floxin.txt:58`: "| challenge5e    = 8" |
| Challenge rating (published, wounded at G15) | 3 (700 XP) | `sources/adventure-wdh.json:5952`: "Urstul is wounded with 50 hit points remaining and has no poison coating his weapons, reducing his challenge rating to 3 (700 XP)." (quest-time, see C; see D11) |
| Languages | Common and Orc, thieves' cant | `sources/adventure-wdh.json:32657`: "He speaks Common and Orc and knows thieves' cant." |
| Age | "in his forties" | `sources/adventure-wdh.json:32645`: "Urstul is a large, heavyset man in his forties." |
| Build | large, heavyset | same line 32645 |
| Featured in | Finding Floon; Fireball!; Gralhund Villa; Faction Outposts; Sea Maidens Faire; Kolat Towers; Gralhund Villa (location) | `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:7` |

Notes for the Summary block:
- The organization page's Key Members entry (`campaign/setting/organizations/09-manshoons-zhentarim.md:100`) gives "Illuskan human assassin, lawful evil". It matches the page.
- The Factions Guide response-team entry is "**Urstul Floxin** (**assassin**) + 3–4 **thugs** (available only if he survived the Gralhund Villa)." (`campaign/guides/factions/10-manshoons-zhentarim.md:13`). This is the Factions Guide bullet the brief asks the Summary to add. It is conditional on a quest result.

---

## C. Quest-time sentences on the current page (and where each already lives)

Each sentence below narrates a quest event or a quest-time state. Under ruling 1 it is restated as a day-one fact or removed. The rows give the file where the event already lives.

| Page line | Sentence (exact) | Where the event already lives | Day-one restatement available? |
|---|---|---|---|
| `02-urstul-floxin.md:11` (Resonance) | "frustration with his slipperiness across multiple arcs" | No quest event. "arcs" is retired vocabulary (E) | Not an event; the word "arcs" must go |
| `02-urstul-floxin.md:21` (Persona) | "he is Manshoon's chief field operative who runs both the Dalakhar capture attempt and the Gralhund Villa operation" | Dalakhar ambush: `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:94` ("Worked for Urstul Floxin. Assigned to intercept a rock gnome named Dalakhar."), and `sources/adventure-wdh.json:4368`. Gralhund raid: `campaign/quests/act-ii/gralhund-villa/overview.md:46` and `ev-04-the-zhentarim-raid.md:20`. | Day one: he is "chief field operative" and his cell tracks Dalakhar (`history/08-the-players-arrive.md:24`). The "runs ... capture attempt" and "operation" clauses are quest-time. |
| `02-urstul-floxin.md:23` (Morale) | "If wounded or desperate, he kicks open the nearest door to grab a hostage." | The G15 door and hostage beat: `campaign/quests/act-ii/gralhund-villa/ev-04-the-zhentarim-raid.md:42` ("He begins trying to kick the door down.") and `ev-05-the-guest-suite.md:18`; the hostage plan for G16 is in `sources/Act_III_Arc_E.md:689` | Behaviour, not an event; the drafter decides |
| `02-urstul-floxin.md:23` (Morale) | "If confronted with overwhelming force, he uses surviving Zhents as cover and runs." | `sources/Act_III_Arc_E.md:596` ("Floxin is not a martyr...") | Behaviour; no event |
| `02-urstul-floxin.md:25` (Relationships) | "a temporary occupant of Gralhund Villa" | Residence conflict (D1) | Conflict, not a fact |
| `02-urstul-floxin.md:25` (Relationships) | "the antagonist who drives **Fireball!** and **Gralhund Villa** before the party can identify his master" | `campaign/quests/act-ii/fireball/overview.md:27`; `campaign/quests/act-ii/gralhund-villa/overview.md:28` | Remove; restate as "he works for Manshoon and will not name him" |
| `02-urstul-floxin.md:13` (Emotions) | "(he storms about Gralhund Villa like he owns it)" | Published `sources/adventure-wdh.json:32645` says "He storms about House Gralhund like he owns the place." | Day one if the residence is settled (D1) |
| `02-urstul-floxin.md:15` (Motivations) | "Urstul wants to recover the Stone of Golorr for Manshoon" | Stone's path: `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:32` (nimblewright takes it); `sources/adventure-wdh.json:4379` ("is refusing to hand over the Stone ... until he speaks to his secret master") | Motivation is day-one (he tracks the Stone, `history/08:24`); the recovery is quest-time |
| `02-urstul-floxin.md:29` (Overview) | "He works for the Zhentarim" | Two Zhentarims rule (E) | Restate as "Manshoon's Zhentarim" or "a Zhentarim cell" |
| Voice `manshoons-zhentarim.md:38` | "Cornered, he turns cunning and grabs a hostage, still never naming his master." | Behaviour (see Morale above) | Behaviour |
| Voice `manshoons-zhentarim.md:37` | "Get that fucking gnome, you slack-jawed pisspots!" | Dalakhar hunt: `history/08:24` (day one) | Day one (the hunt, not the capture) |
| Voice `manshoons-zhentarim.md:41` | "He never names Manshoon unless magically compelled" | Conflict with `campaign/quests/act-ii/gralhund-villa/ev-05-the-guest-suite.md:33` (D3) | Conflict |
| Voice `manshoons-zhentarim.md:44` | "The stone comes to me. Who I give it to is not your business." | Stone's path (Fireball, Gralhund) | Sample line; the drafter decides whether it reads as a day-one line |
| Voice `manshoons-zhentarim.md:45` | "Back off, or the pretty one gets a new smile. Back. Off." | "the pretty one" is not identified in any source | Sample line; no event named |
| `campaign/setting/organizations/09-manshoons-zhentarim.md:100` | "his team is tracking Dalakhar, the gnome moving the Stone of Golorr" | Day-one hunt (`history/08:24`) | Day one |

Quest-time facts that the page does **not** currently state, but which the Background must not contradict:
- Fireball!: the burned man "gives his real name when asked", is "north of the blast radius — badly burned, conscious", and "wants the Stone tracked so the Zhentarim can follow" (`campaign/quests/act-ii/fireball/ev-01-the-fireball.md:32, 64, 66`).
- Gralhund Villa: he "arrived on the night of Ches 24th with eight agents and lost most of them" (`campaign/quests/act-ii/gralhund-villa/overview.md:28`).
- Gralhund Villa: he is "trapped in the guest suite corridor" and "still will not name his master" (same line).
- Gralhund Villa: the raid and the G15b door (`ev-04-the-zhentarim-raid.md:42`; `ev-05-the-guest-suite.md:18`).
- Gralhund Villa aftermath: "No Stone, no nimblewright, no Floxin." (`campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:44`).
- Kolat Towers: "If he survived earlier encounters with the characters" he is in the towers, punished for the lost Stone (`sources/adventure-wdh.json:30041`).

---

## D. Conflicts

**D1. Where he lives on Ches 1, 1492 DR (residence).** Not settled in any file.

Day-one residence at Gralhund Villa:
> "{@creature Urstul Floxin|wdh} works for {@creature Manshoon|WDH}, and he is the highest-ranking member of the Zhentarim squad stationed at House Gralhund." — `sources/adventure-wdh.json:32644`
> "Until recently, this suite was set aside for the use of {@creature Urstul Floxin|wdh}." — `sources/adventure-wdh.json:5951`
> "A squad of Manshoon's Zhentarim lives at the villa under Urstul Floxin, the highest-ranking among them. Yalah treats them as her own spy network." — `campaign/setting/organizations/12-house-gralhund.md:49`
> "a temporary occupant of Gralhund Villa (where he treats Yalah as an underling)" — `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:25`
> "The house pays for the Zhentarim cell that shelters at its villa." — `campaign/guides/factions/13-house-gralhund.md:17`

Day-one residence elsewhere (Kolat Towers):
> "- Urstul Floxin's cell led the kidnapping and fled to Kolat Towers before the quest begins. The City Watch has Splinter thugs under arrest at the Dock Ward scene." — `campaign/setting/history/08-the-players-arrive.md:65`
> "- **Urstul Floxin** (Manshoon's Zhentarim) — offscreen; led the kidnapping cell; already fled to Kolat Towers before the quest begins" — `campaign/quests/act-i/finding-floon/overview.md:31`

Arrival at the villa on Ches 24 (quest journal):
> "- **Urstul Floxin** (Manshoon's Zhentarim) — led the strike team; arrived on the night of Ches 24th with eight agents and lost most of them; trapped in the guest suite corridor by the time the party arrives; still armed; still operational; still will not name his master" — `campaign/quests/act-ii/gralhund-villa/overview.md:28`

Villa stay before the raid (quest-time, Ches 22–24):
> "Two house guards are dead in this room. Floxin killed them in the small hours of Ches 24th, while the household slept. He was still a prisoner then; the raid had not yet begun." — `campaign/locations/gralhund-villa/g09-parlor.md:7`
> "{@creature Urstul Floxin|wdh} was confined here when he returned to the villa, but shortly thereafter he killed his guards and escaped." — `sources/adventure-wdh.json:5797`

Retreat after the fireball (Alexandrian, quest-time):
> "He did not stay confined. Within hours, Floxin killed his guards and escaped — without the Stone, which Gralhund refused to yield. He retreated to his Black Network safe house, assembled his full strike team, and began planning a return." — `sources/Act_III_Arc_D.md:39` (inside a `<p>` element)

The Harper note (Fireball! overview, quest-time) and the Yellowspire lead (see D10).

Ranking note for the orchestrator: `history/08` is a setting page and `finding-floon/overview.md` is a quest journal. Both are campaign files and both say "before the quest begins" for the Kolat Towers flight. The Gralhund-residence claims are in an organization page and a guide, both written as day-one lore. No rule in the brief settles this.

**D2. Rank and position.** The sources describe him in different terms.
> "- **Lieutenants and field teams:** Urstul Floxin is the chief field operative and leads the thugs who work the streets." — `campaign/setting/organizations/09-manshoons-zhentarim.md:58`
> "- **Urstul Floxin** — ... and Manshoon's chief field operative. He is the thuggish leader of the cell's field teams, ..." — `campaign/setting/organizations/09-manshoons-zhentarim.md:100`
> "{@creature Urstul Floxin|wdh} ... the highest-ranking member of the Zhentarim squad" — `sources/adventure-wdh.json:32644`
> "The rumored leader of the renegade Zhent faction is {@creature Urstul Floxin|wdh}, a known Black Network assassin." — `sources/adventure-wdh.json:4033`
> "In {{Yearlink|1492}},{{WDH-time}} Urstul Floxin was the leader of the Zhents headquartered in the villa of the [[Gralhund]] family." — `.../wiki/02-urstul-floxin.txt:65`
> "Floxin is Manshoon's chief field agent and the face of the cell in the streets, but he is not its leader." — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:21` (GM-only truth)
> "- The rival cell of the Black Network in Waterdeep and its leader, Urstul Floxin." — `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:195` (Davil's topics list, the Doom Raiders' belief)
Note: `sources/research`'s pass5 notes say "Campaign governs; the Doom Raiders text must not use line 4033" (`docs/plans/setting-compendium-research-notes/pass5/zhentarim.md:283`).

**D3. Whether he can be made to name Manshoon.**
> "Deep down, he will not divulge his master's name unless magically compelled" — `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:21`
> "He never names Manshoon unless magically compelled" — `.../voices/manshoons-zhentarim.md:41`
> "won't divulge it or the name of his master, {@creature Manshoon|WDH}, unless he's magically compelled to do so." — `sources/adventure-wdh.json:5952`
> "Floxin will not name Manshoon. Not under Intimidation, not under magical compulsion, not with a blade at his throat. He does not know the name — he knows a code and a set of dead-drop locations." — `campaign/quests/act-ii/gralhund-villa/ev-05-the-guest-suite.md:33`
> "Floxin does not name his master. ... DC 14 Insight during any interrogation of Floxin confirms this genuinely: he knows a dead-drop chain and a code, not a name or a face." — `campaign/quests/act-ii/gralhund-villa/design-notes.md:37`
> "he cannot name Manshoon, because he knows only a code and a chain of dead drops." — `campaign/setting/villains/manshoon.md:69`
The page and the voice profile follow the published adventure on compulsion. The Gralhund quest journal removes the compulsion exception.

**D4. How he takes orders.**
> "Urstul takes his orders from {@creature Manshoon|WDH}'s current simulacrum, which comes and goes from House Gralhund by way of a teleportation circle (connected to the circle in Kolat Towers)." — `sources/adventure-wdh.json:32644`
> "Urstul received his orders directly from a [[simulacrum]] of Manshoon." — `.../wiki/02-urstul-floxin.txt:81`
> "the chain of command stopped at a contact he never saw face to face. Manshoon stays invisible." — `campaign/quests/act-ii/gralhund-villa/ev-05-the-guest-suite.md:33`
> "In the published adventure he takes his orders from Manshoon's simulacrum, and in the campaign he cannot name Manshoon" — `campaign/setting/villains/manshoon.md:69`

**D5. The teleportation circle and flying snakes in G15b.**
> "The birdcage contains three {@creature flying snake||flying snakes} that Urstul uses to deliver messages to his spies throughout the city. The circle is used by {@creature Manshoon|WDH} to meet secretly with {@creature Urstul Floxin|WDH} and to teleport Zhents to and from Kolat Towers (see chapter 8)." — `sources/adventure-wdh.json:5954`
> "The Alexandrian Remix explicitly removes both. G15b is an ordinary guest room." — `campaign/quests/act-ii/gralhund-villa/ev-05-the-guest-suite.md:12`
> "G15b is an ordinary guest room with no magical infrastructure." — `campaign/structure/arc-d-gralhund-villa.md:162` (superseded file)

**D6. Who holds the Stone during the Dalakhar fight (quest-time).**
> "Dalakhar is killed by a fireball spell. Urstul Floxin steals the Stone of Golorr from Dalakhar's corpse." — `sources/adventure-wdh.json:862`
> "Though he was wounded, he was able to pluck the {@item Stone of Golorr|WDH} from Dalakhar's pocket before fleeing the scene." — `sources/adventure-wdh.json:4368`
> "The nimblewright threw the bead from the cooperage rooftop to the east, dropped to the street, rifled Dalakhar's body, took the Stone of Golorr, and fled east across the rooftops. Floxin was north of the blast radius — badly burned, conscious." — `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:32`
> "The nimblewright uses a necklace of fireballs to launch a fireball which kills Dalakhar and most of the Zhentarim agents, with the exception of Urstul Floxin (who barely survives, but is incapacitated)." — Alexandrian `sources/4. Gralhund Villa.pdf` p. 26 (transcribed from the page image; flag for pdftotext)
Campaign outranks the published adventure (the quest journal is authoritative for Fireball!).

**D7. Outcome names for Floxin's fate.**
> "- **Floxin Alive** — mark when Floxin survives the raid; read by **Kolat Towers**, where he becomes available as a Manshoon response team leader." — `campaign/quests/act-ii/gralhund-villa/ev-04-the-zhentarim-raid.md:98`
> "- **Floxin Captured** — mark when the party takes Floxin into custody, only when **Floxin Alive** is also marked; a captured Floxin provides nothing useful about his master." — `campaign/quests/act-ii/gralhund-villa/ev-04-the-zhentarim-raid.md:99`
> "- **Floxin Status.** If the **Gralhund Villa** outcome **Floxin Status** is Dead or Captured, no Doom Raider says "Floxin's cell". They say "the other cell" instead, ..." — `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:28`
> "- **Alive:** Floxin filed the tip himself. ..." and "- **Dead or Captured:** another member of the cell filed the tip, ..." — `campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:26-27`
The Gralhund quest journal has no "Dead" outcome in its Event Outcomes list, and the Doom Raiders files read a single **Floxin Status** outcome with three values. The naming does not match. Route to Gralhund Villa.

**D8. Warrant and whereabouts after the raid.**
> "A warrant has been issued for Urstul's arrest, but his current whereabouts are unknown. Even magical scrying has failed to reveal his location." — `sources/adventure-wdh.json:4034`
> "The Zhent leader, {@creature Urstul Floxin|wdh}, was among those who got away. He's still at large. The Watch plans to step up its search for him." — `sources/adventure-wdh.json:4837`
> "**Alive:** ... The warrant and the failed scrying are real, because Floxin is hiding." — `campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:26`
> "**Warrant.** Only if Floxin is Alive: the Watch has issued a warrant for him, his whereabouts are unknown, and scrying has failed to find him." — `campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:115`
> "No Stone, no nimblewright, no Floxin." — `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:44`

**D9. Harper identification.**
> "- **Conflicts:** Floxin. `fireball/ev-01-the-fireball.md:175` has Renaer's Harper contacts identify the burned man as "Manshoon's chief field agent in Waterdeep", while `02-harpers.md:22` and `history/04-the-founding-of-chains.md:93` say no Harper contact names Manshoon. The body no longer mentions Floxin, so the conflict is for the quest files to settle." — `campaign/setting/organizations/01-harpers.md:177`
> "Renaer ... the burned man is **Urstul Floxin**, Manshoon's chief field agent in Waterdeep." — `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:175`

**D10. Safe house.**
> "| 1+ days | Briefed on Dalakhar's death; knows Floxin was following him | Inadvertently confirms Floxin as a pursuer; can mention Floxin staying at the Yellowspire safe house (Castle Ward) → leads to Gralhund Villa if the party hasn't found it yet |" — `campaign/quests/act-ii/fireball/ev-06-the-death-mark.md:52`
> "- Tracking Urstul Floxin before the Gralhund Villa operation (Response Team: Urstul Floxin)" — `campaign/guides/factions/10-manshoons-zhentarim.md:68` (Yellowspire revelation list)
> "Parties that searched Urstul Floxin's effects at Gralhund Villa have documents pointing to Brindul Alley." — `campaign/guides/factions/10-manshoons-zhentarim.md:19`
Conflict with `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:175` ("A North Ward resident saw Floxin ... enter Gralhund Villa on Saerdoun Street within hours of the blast.").

**D11. Challenge rating.**
> "| challenge5e    = 8" — `.../wiki/02-urstul-floxin.txt:58`
> "reducing his challenge rating to 3 (700 XP)" — `sources/adventure-wdh.json:5952` (wounded, no poison; quest-time)
> "(50 hp, no poison, CR 3)" — `campaign/quests/act-ii/gralhund-villa/overview.md:40` (quest-time)
Not a conflict on the base stat; the page does not give a CR and must not give CR 3 as his base.

**D12. Timing of the kidnapping.**
> "Volo met {@creature Floon Blagmaar|WDH} for drinks at the Skewered Dragon two nights ago." — `sources/adventure-wdh.json:1686`
> "Floon Blagmaar is taken on the night before Ches 1. The published adventure says "two nights"; the campaign settled on "last night"." — `campaign/setting/history/08-the-players-arrive.md:64`
Campaign uses "last night" (CLAUDE.md; history/08 line 64).

**D13. Who is the Zhentarim squad at the villa.**
> "the local leaders of the Black Network (with {@creature Urstul Floxin|wdh} chief among them) reside with them in the family villa." — `sources/adventure-wdh.json:32446`
> "A squad of Manshoon's Zhentarim lives at the villa under Urstul Floxin" — `campaign/setting/organizations/12-house-gralhund.md:49`
> "The Zhentarim squad ... the Zhents in House Gralhund" — `campaign/setting/organizations/12-house-gralhund.md:158`: "- **Conflicts:** Urstul and Yalah, who is the underling. ..." (organization page's own conflict note)

**D14. Floxin's Yalah relationship (not a conflict; for the record).** `campaign/setting/notable-figures/gralhunds/01-yalah-gralhund.md:15` says "without Manshoon discovering she considers Urstul an underling" and `:21` says "Deep down, she pried the Stone from Floxin at sword-point and holds it herself". The `:21` clause is quest-time (E).

---

## E. Stale lines in other files (not edited) and routed quest references

Stale under ruling 1 (quest-time or conflicting with a day-one restatement):
- `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:11` "across multiple arcs" (retired vocabulary, "Quests, not arcs").
- `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:21` "runs both the Dalakhar capture attempt and the Gralhund Villa operation" (quest-time, C).
- `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:25` "drives **Fireball!** and **Gralhund Villa** before the party can identify his master" (quest-time, C).
- `campaign/setting/notable-figures/gralhunds/01-yalah-gralhund.md:21` "Deep down, she pried the Stone from Floxin at sword-point and holds it herself" (quest-time).
- `campaign/setting/villains/manshoon.md:61` "trusted with the Stone recovery at Gralhund Villa; his failure there is the first crack" (quest-time).
- `campaign/setting/villains/manshoon.md:69` "Urstul Floxin ran the Dalakhar capture attempt and the **Gralhund Villa** operation." (quest-time).
- `campaign/gazetteer/waterdeep/north-ward.md:73` "Yalah holds the Stone of Golorr, which she took from Urstul Floxin at sword-point." (setting page, quest-time).
- `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:39` "By the night of Ches 24, when Floxin's strike team hits **Gralhund Villa**, Manshoon's cell knows the Gralhunds hold the Stone." (setting page, quest-time).
- `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:63` "| Ches 24 | Urstul Floxin strikes Gralhund Villa at nightfall | **Gralhund Villa** | The quest opens |" (setting page timeline).
- `campaign/guides/gm-guide/structural-rules.md:47` "| Ches 24 | Urstul Floxin strikes Gralhund Villa | **Gralhund Villa** opens |".
- `campaign/setting/organizations/12-house-gralhund.md:172` "Routed to quests: Yalah taking the Stone from Urstul Floxin at sword-point" (the organization page itself routes this; no edit needed).
- `campaign/guides/factions/10-manshoons-zhentarim.md:19` "parties that searched Urstul Floxin's effects at Gralhund Villa have documents pointing to Brindul Alley" (quest-time).
- `campaign/setting/history/08-the-players-arrive.md:65` "fled to Kolat Towers before the quest begins" (pre-campaign; conflicts with `organizations/12-house-gralhund.md:49`; see D1).

Routed quest references (the page should not narrate; these live in the quest files):
- Gralhund Villa: `campaign/quests/act-ii/gralhund-villa/overview.md:28, 40, 46`; `ev-02-saerdoun-street.md:41, 43, 47, 72-74`; `ev-03c-night-infiltration.md:68`; `ev-04-the-zhentarim-raid.md:16, 20, 42, 64, 98-99, 113, 121`; `ev-05-the-guest-suite.md:8, 12, 16-33, 79`; `ev-09-aftermath.md:40, 44, 57`.
- Fireball!: `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:32, 62-68, 94, 104, 116, 120, 175, 219`; `overview.md:27, 34, 60`; `ev-04-the-sea-maidens-faire.md:134`; `ev-06-the-death-mark.md:52, 58`.
- Finding Floon: `campaign/quests/act-i/finding-floon/overview.md:31`; `design-notes.md:9` ("The Candle Lane warehouse belongs to Manshoon's cell, Urstul Floxin's people, operating separately from Davil.").
- Doom Raiders quests: `s01-davils-arrest/ev-01-davils-arrest.md:24-27, 114-115, 130, 134`; `m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:28`; `m04-silencing-skeemo/design-notes.md:15`; `r25-ardragon/ev-01-ardragon.md:23`; `s02-davils-return/design-notes.md:17`.
- Faction Outposts: `campaign/structure/arc-e-faction-outposts.md:117` (superseded); the Factions Guide response-team entry (`10-manshoons-zhentarim.md:13`); "Directive to Urstul Floxin" (`10-manshoons-zhentarim.md:63`).
- Kolat Towers: `campaign/structure/arc-i-kolat-towers.md:152` ("**E5 — Laboratory.** Urstul Floxin is here if he survived **Gralhund Villa**.") and `sources/adventure-wdh.json:26763` (Urstul at area E5 as a lieutenant to be captured).
- Sea Maidens Faire: `campaign/structure/arc-h-sea-maidens-faire.md:204` ("**The Strike Team.** Urstul Floxin (if alive from **Gralhund Villa**; if dead, replaced by Vevette Blackwater) ...").
- Lords' Alliance: `campaign/quests/faction-events/lords-alliance/r25-warduke/ev-01-warduke.md:203` ("The third Splinter crew appears only if Urstul Floxin survived **Gralhund Villa**.").
- Dalakhar Speak with Dead (quest-time): `ev-01-the-fireball.md:92-96`.
- Faction mission: `sources/Appendix_B_-_Player_Factions.md:658` ("Neutralize a named Manshoon operative (+2). Eliminate or capture one of Manshoon's lieutenants — Urstul Floxin, Vevette Blackwater, Agorn Fuoco, or any other named agent.").
- Tavern: `sources/Appendix_D_-_Running_the_Tavern.md:1549` ("Urstul Floxin does not visit the tavern unless he is specifically hunting the characters for the Gralhund Villa incident.").
- Responses: `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:40` (same idea, same routing).
- Warrant: `campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:115`.

Outcome-name routing: "Floxin Alive" and "Floxin Captured" (`ev-04:98-99`), "Floxin Status" (Doom Raiders, `m05 ev-01:28`, `s01 ev-01:24-27`), and "Gralhund Villa Named" (`fireball/ev-01-the-fireball.md:219`). The Gralhund quest journal's Event Outcomes are the source; the drafter must not write any of them into the page.

Route the Villains page's relationship row and notes (`manshoon.md:61`, `:69`) to Gralhund Villa and Kolat Towers. Do not edit.

---

## F. Gaps a Background would need that no source gives

For each gap, the sourced facts the drafter must stay consistent with.

1. **Birthplace, upbringing and family.** No source gives a birthplace. Sourced: "Illuskan" ethnicity (wiki line 15; `sources/adventure-wdh.json:32652`) and "home = Waterdeep, Sword Coast North" (wiki line 11). Parents, siblings, children, spouse: wiki infobox lines 29-32 are blank (`parents`, `spouses`, `siblings`, `children` are empty). Consistency: nothing may say he is from another culture or city than Illuskan/Waterdeep; "Illuskan" is the ethnicity only.
2. **How he became an assassin and came into the Black Network.** No source. Sourced: "Assassin" (wiki line 16; `sources/adventure-wdh.json:32652`); "high-ranking member of the [[Zhentarim]] in [[Waterdeep]] in the early 1490s [[DR]]" (wiki line 62). Consistency: the wiki's "early 1490s" and the campaign's Manshoon cell (2 years building, `history/08` lines 31-32) must both hold.
3. **How he met Manshoon and came under his command.** No source. Sourced: "works for Manshoon" (`sources/adventure-wdh.json:32644`), "employer" (`manshoon.md`/01 line 26), and "cannot name Manshoon" (`villains/manshoon.md:69`). Consistency: he has never seen his master face to face (`ev-05-the-guest-suite.md:33`), so any origin story must not include a meeting.
4. **Rise and rank history.** No source. Sourced: "highest-ranking member of the Zhentarim squad stationed at House Gralhund" (`32644`), "chief field operative" (`org 09:58`, Notable 02:21). Consistency: D2 (leader vs. not leader).
5. **Former punishment.** `sources/adventure-wdh.json:30041`: "He is being punished for allowing the {@item Stone of Golorr|WDH} to slip through his fingers (during the events of chapter 3)." Quest-time, Kolat Towers; not day-one.
6. **Faith or god.** No source gives him a deity or rites. Sourced: nothing; the organization's Beliefs section says the cell has no campaign creed (`organizations/09:46` research note). Consistency: none of the sources gives him an oath.
7. **Friends, lovers, companions.** No source. Sourced: none for Floxin. The only named personal bonds are with his underlings in quest files (Bashekk Ortallis and Wern Malkrave, `ev-01-the-fireball.md:94`, `Act_III_Arc_D.md:224`). Consistency: those two died in the blast (Fireball!), so a backstory may not make them alive.
8. **Fears.** No source names a fear. Sourced: "desperate cunning when cornered" (Notable 02:13); "he kicks open the nearest door to grab a hostage" (Notable 02:23). Consistency: "Floxin is not a martyr" (quest-time, `Act_III_Arc_E.md:596`).
9. **Personal goals beyond the Stone.** No source. Sourced faction goal: "Urstul wants to recover the Stone of Golorr for Manshoon, maintain operational control of the field team, and survive encounters with the party by any means necessary, including hostage-taking." (Notable 02:15). Consistency: Motivations and Emotions stay verbatim (ruling 3); the personal goal must not reveal or change the Stone, the Eyes, Manshoon's name, any Event Outcome or the Grand Game balance (ruling 17). Note: the Gralhund quest and the Doom Raiders files make Floxin's fate depend on the Gralhund Villa outcome, so a personal goal should not require him to be alive on Ches 1 for later quests (ruling 17 limit). [design] for any invention.
10. **Where he sleeps on Ches 1.** Conflict (D1). Sourced candidates in D1 only; no tie-breaker in the sources.
11. **His connection to the flying snakes.** Sourced: `32645` ("a collection of black flying snakes that he uses as couriers"); `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:21` ("he keeps a collection of black flying snakes as couriers because he trusts animals more than people"). No source says when or from whom he got them.
12. **His time in Waterdeep before Ches 1.** No source. Sourced: Dock Ward surveillance by Staget ("pulled a surveillance detail off a Zhent instigator named Urstul Floxin", `organizations/11-open-lords-watch.md:25`); "Renaer ... Floxin" (`1687`). Consistency: the Watch was watching him before Ches 1.
13. **Pre-campaign history with Dalakhar, the Stone and the Eyes.** Sourced: "Urstul Floxin's Zhentarim cell is tracking him" (`history/08:24`). The Stone's history before Dalakhar is in `history/08` and `Act_III_Arc_D.md` and is not Floxin's.
14. **Languages and training.** Sourced: Common, Orc and thieves' cant (`32657`). No training source.
15. **Physical appearance beyond build.** Sourced: "large, heavyset", "in his forties" (`32645`). No hair, eyes, scars, clothing before the quest. Quest-time: "badly burned" (`fireball/ev-01:32`), "wounded" (`ev-05:18`). Do not write the burns as a day-one feature.
16. **Pronunciation.** Sourced: "UR-stool FLOX-in" (`sources/adventure-wdh.json:342`).

---

## G. Inner-life hints (exact quotes)

These are the source facts that hint at fears, habits, loves, grudges, losses or a place or person he cares about. They are for ruling 17. Each line is quoted in full; the note says whether it is day-one or quest-time.

- Habit with animals (day one): "Deep down, he will not divulge his master's name unless magically compelled, and he keeps a collection of black flying snakes as couriers because he trusts animals more than people." — `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:21`
- Habit with animals (day one): "He talks to his flying snakes more gently than to people." — `.../character-voices/voices/manshoons-zhentarim.md:39` (voice doc Quirks)
- Loyalty (quest-time, Kolat Towers): "Urstul was truly loyal to Manshoon, even after being punished." — `.../wiki/02-urstul-floxin.txt:78`
- Loyalty (quest-time): "Nevertheless, he remains loyal to {@creature Manshoon|WDH}." — `sources/adventure-wdh.json:30041`
- Pride and contempt (day one, published): "{@creature Urstul Floxin|wdh} works for {@creature Manshoon|WDH}..." — `sources/adventure-wdh.json:32644` ("Urstul is a glorified thug with all the charm and breeding of a snake")
- Possessiveness (day one): "territorial possessiveness (he storms about Gralhund Villa like he owns it)" — `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:13`
- Refusal to name his master (day one): "absolute refusal to name his master." — `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md:13`
- Grudge and bitterness (published, Doom Raiders briefing, day one): "The botched kidnapping of {@creature Renaer Neverember|wdh} won't sit well with Urstul. He might try again. (Tashlyn doesn't actually believe this, but she knows that Renaer has ties to the Harpers and might share information of interest with the characters.)" — `sources/adventure-wdh.json:4035`
- Grudge (quest-time, Alexandrian, aftermath): "Floxin does not forget and does not forgive. He will be looking for them." — `sources/Act_III_Arc_E.md:892`
- Motive (quest-time, Gralhund secret): "Believing that {@creature Urstul Floxin|WDH} is after the gold for himself, Yalah plans to cut Urstul out of the deal and deliver the {@item Stone of Golorr|WDH} to {@creature Manshoon|WDH} herself." — `sources/adventure-wdh.json:4812` (this is Lady Gralhund's view, a Gralhund Villa secret; do not reveal)
- Self-preservation, quest-time: "He would rather live and plan than die heroically over a Stone he no longer has any certainty about." — `sources/Act_III_Arc_E.md:596` (rest of the passage covers his fall-back behaviour)
- Watchfulness, quest-time: "Floxin is at the G15b door, shoulder into the wood, boot following, reading each impact for where the barricade is weakest. He is focused." — `campaign/quests/act-ii/gralhund-villa/ev-05-the-guest-suite.md:18`
- Possession of luggage and a map (quest-time, Gralhund Villa, G15): "Floxin's luggage occupies the wardrobe — traveling clothes, a locked case (DC 14 thieves' tools) that holds a set of thieves' tools, a hand-drawn map of the North Ward with three properties marked (none of them Gralhund Villa), and a folded document in cipher." — `campaign/locations/gralhund-villa/g15-guest-suite.md:21`
- Coat left behind (quest-time): "Floxin's traveling coat is on the rack — it has been there since Ches 22nd; he wasn't permitted to take it when Yalah had him disarmed." — `campaign/locations/gralhund-villa/g15-guest-suite.md:11`
- Plans to recover his position (quest-time, Alexandrian): "He retreated to his Black Network safe house, assembled his full strike team, and began planning a return." — `sources/Act_III_Arc_D.md:39`
- Yalah's view of him (day one): "without Manshoon discovering she considers Urstul an underling" — `campaign/setting/notable-figures/gralhunds/01-yalah-gralhund.md:15`

No source gives him a place or person he cares about, a lost love, a child, a debt he is still paying, or a childhood fear. Those are for the drafter's [design] tag under ruling 17.

---

## Cross-references (file:line, with the line copied)

Campaign setting and guides:
- `campaign/setting/organizations/09-manshoons-zhentarim.md:33` "- **The night before Ches 1, 1492 DR, Renaer Neverember:** Five Zhentarim thugs working for Urstul Floxin seized Renaer Neverember to learn what he knew about his father's hidden gold, and they took Floon Blagmaar in the same attack. House Gralhund paid for the operation (*Dragon Heist*, 5e; **House Gralhund**). Xanathar's Guild raided the Candle Lane warehouse where the thugs held both men and killed the cell's agents there (*Dragon Heist*, 5e)."
- `campaign/setting/organizations/09-manshoons-zhentarim.md:42` "- **Nobody Names the Master:** The street crews will not say who gives the orders, and few in the cell know their master's name. Urstul Floxin will not divulge it unless magically compelled, and he sends messages by black flying snake because he trusts animals more than people. Outsiders call the cell the Splinter."
- `campaign/setting/organizations/09-manshoons-zhentarim.md:58`, `:90`, `:100` (quoted in A and B).
- `campaign/setting/organizations/09-manshoons-zhentarim.md:169` "- **Conflicts:** Urstul and his master's name. `02-urstul-floxin.md` line 21 has him refusing to divulge it unless magically compelled, and `villains/manshoon.md` line 69 has him unable to name Manshoon because he knows only a code and a chain of dead drops. The Nobody Names the Master belief follows the Notable Figures page."
- `campaign/setting/organizations/12-house-gralhund.md:49`, `:66`, `:158`, `:172` (quoted in D1, D13, E).
- `campaign/setting/organizations/11-open-lords-watch.md:25` (quoted in A).
- `campaign/setting/organizations/06-doom-raiders.md:39`, `:88`, `:115` (quoted in A).
- `campaign/setting/organizations/01-harpers.md:177` (quoted in D9).
- `campaign/setting/villains/manshoon.md:9` "The party gets his name at the Interrogation House in **Faction Outposts**, which is where the **Manshoon Named** Event Outcome is marked." (the Manshoon name is not Floxin's to give; see G and F3)
- `campaign/setting/villains/manshoon.md:61`, `:69` (quoted).
- `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:26` (quoted in A).
- `campaign/setting/notable-figures/gralhunds/01-yalah-gralhund.md:15`, `:21`, `:25` (quoted in D14, E). `:25`: "Yalah is the wife of Orond Gralhund (whom she manages more than loves), the commander of Hrabbaz (her bodyguard, more loyal to her than to Orond), and the de facto handler of the Zhentarim forces at her villa, not realizing their true master is Manshoon."
- `campaign/setting/history/08-the-players-arrive.md:24`, `:25`, `:56`, `:57`, `:64`, `:65`, `:66` (quoted in A, D1, D12, E).
- `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:63` (quoted in E).
- `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:25`, `:39`, `:85` (quoted in A and E). `:85`: "- **Changed column, Manshoon's Zhentarim:** \"Urstul Floxin redirected to Gralhund Villa\" (`grand-game.md:33`) is no longer a table cell. It is the substance of the procedure line. \"Stone + all three Eyes\" (`running-the-villains.md:39`) is kept verbatim."
- `campaign/setting/deities/bane.md:73` "Until the party marks **Manshoon Named**, even the Doom Raiders say \"Floxin's cell\" or \"the other cell\" and call Kolat Towers \"the towers in the Southern Ward\"." (quest-time gate; not Floxin's)
- `campaign/gazetteer/waterdeep/north-ward.md:39`, `:73`, `:254` (quoted in E; `:39`: "- A party that searched Urstul Floxin's effects at Gralhund Villa holds documents that name the alley. Any other party can find the house by canvassing the ward for a day (DC 14 Investigation, no faction membership needed), and Zhentarim response teams carry orders to take their prisoners here."; `:254`: "- **Avareen Windrivver**, **Urstul Floxin**: the Zhentarim operatives tied to the Interrogation House and the villa.")
- `campaign/locations/gralhund-villa/area-overview.md:18` and `:80` (quest-time; `:80`: "| G15a | Urstul Floxin (50 hp, no poison), 1 Zhent thug | Trying to breach G15b |").
- `campaign/locations/gralhund-villa/g05-kitchen.md:7`, `g06-pantry.md:9`, `g09-parlor.md:7`, `:13`, `:15`, `g15-guest-suite.md:11`, `:15`, `:21`, `:23` (quest-time; quoted in D1, G).
- `campaign/guides/factions/10-manshoons-zhentarim.md:13`, `:19`, `:52`, `:54`, `:63`, `:68` (quoted in B, C, E).
- `campaign/guides/factions/13-house-gralhund.md:17`, `:75`, `:118`, `:119`. `:118`: "- **Conflicts:** The Stone after the quest. `ev-09-aftermath.md:44` says there is no Stone, nimblewright or Floxin left, while `ev-09-aftermath.md:142` says the Stone may be with \"Yalah, who kept it\"." `:119`: "- **Conflicts:** How Yalah got the Stone. `campaign/setting/notable-figures/gralhunds/01-yalah-gralhund.md:21` says \"she pried the Stone from Floxin at sword-point and holds it herself\"..." (the rest of the line covers the Alexandrian `2. Other Factions.pdf` p. 21, not checked).
- `campaign/guides/factions/12-open-lords-watch.md:100` "- **A witness.** The Watch releases a witness it holds, such as Urstul Floxin, within 24 hours, because it has no grounds to keep him."
- `campaign/guides/gm-guide/running-the-villains.md:39` (quoted in A), `:50` (escalation row; "Urstul Floxin's team if the others fail").
- `campaign/guides/gm-guide/structural-rules.md:47` (quoted in E).
- `campaign/guides/gm-guide/debts-of-the-city.md:55`: "Urstul Floxin is Manshoon's chief field operative in Waterdeep: a large, heavyset Illuskan man in his forties who moves through rooms as though he owns them and reserves his anger for moments when it will accomplish something." `:62`: "Floxin works for Manshoon, not the Doom Raiders. A character whose Debt is held by Floxin is already entangled with the campaign's primary villain faction, whether they know it or not."
- `campaign/guides/players-guide/debts-of-the-city.md:41` (the Debt, "a name you obtained with difficulty afterward").
- `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:40` (quoted in E).

Campaign quests:
- `campaign/quests/act-i/finding-floon/overview.md:31`; `design-notes.md:9` (quoted in C, D1, E).
- `campaign/quests/act-ii/fireball/overview.md:27`, `:34`, `:42`, `:60`; `ev-01-the-fireball.md:32`, `:60`, `:62-68`, `:94`, `:104`, `:116`, `:120`, `:175`, `:184`, `:198`, `:200`, `:219`; `ev-04-the-sea-maidens-faire.md:134`; `ev-06-the-death-mark.md:52`, `:58`; `design-notes.md:15`, `:21`.
- `campaign/quests/act-ii/gralhund-villa/overview.md:28`, `:40`, `:46`; `ev-02-saerdoun-street.md:41`, `:43`, `:47`, `:72`, `:74`; `ev-03-daytime-infiltration.md:28`, `:97`; `ev-03c-night-infiltration.md:56`, `:68`, `:70`, `:79`; `ev-04-the-zhentarim-raid.md:6`, `:9`, `:12`, `:16`, `:20`, `:28`, `:36`, `:38`, `:42`, `:46`, `:57`, `:64`, `:87`, `:89`, `:91`, `:98-99`, `:103`, `:113`, `:121`; `ev-05-the-guest-suite.md:8`, `:12`, `:16`, `:18`, `:20`, `:24`, `:26`, `:28`, `:30`, `:33`, `:37`, `:69`, `:79`; `ev-06-the-gralhund-confrontation-day.md:19`, `:28`, `:65`; `ev-07-the-gralhund-confrontation-night.md:23`, `:30`, `:51`, `:75`; `ev-09-aftermath.md:40`, `:44`, `:57`; `flowchart.md:106-107`; `design-notes.md:23`, `:37`.
- `campaign/quests/faction-events/doom-raiders/00-first-meeting/ev-01-first-meeting.md:21`, `:23`, `:195`, `:258`, `:262`, `:268`, `:432`; `design-notes.md:11`, `:13`.
- `campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/ev-01-the-dockside-killer.md:76` ("Floxin has no use for sailors, ...").
- `campaign/quests/faction-events/doom-raiders/m04-silencing-skeemo/design-notes.md:15`; `ev-02-the-chase.md:155`; `ev-03-the-reckoning.md:176`; `overview.md:25`.
- `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:27`, `:28`, `:50`, `:56`, `:106`, `:110`, `:112`, `:116`, `:122`; `ev-02-the-debrief.md:25`; `overview.md:10`, `:28`, `:32`.
- `campaign/quests/faction-events/doom-raiders/m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md:26`.
- `campaign/quests/faction-events/doom-raiders/r03-wolf/design-notes.md:7`; `r25-ardragon/ev-01-ardragon.md:23`, `:170`; `r50-dread-lord/ev-01-dread-lord.md:82`.
- `campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:8`, `:24`, `:26`, `:27`, `:114`, `:115`, `:124`, `:130`, `:134`, `:154`, `:224`, `:291`; `design-notes.md:5`, `:11`, `:13`.
- `campaign/quests/faction-events/doom-raiders/s02-davils-return/design-notes.md:17`; `ev-01-davils-return.md:102`.
- `campaign/quests/faction-events/lords-alliance/r25-warduke/ev-01-warduke.md:198`, `:203`.

Structure docs (superseded by quest journals; cross-reference only):
- `campaign/structure/arc-a-finding-floon.md:45`, `:235`.
- `campaign/structure/arc-c-fireball.md:57`, `:86`, `:255`, `:307`, `:321`, `:358`.
- `campaign/structure/arc-d-gralhund-villa.md:29`, `:162`, `:227`, `:351`, `:400`, `:420`, `:463`.
- `campaign/structure/arc-e-faction-outposts.md:117`.
- `campaign/structure/arc-h-sea-maidens-faire.md:204`.
- `campaign/structure/arc-i-kolat-towers.md:152`, `:320`.
- `campaign/structure/ch1-beginning.md:182` (retired chapter file).

Alexandrian markdown:
- `sources/Act_III_Arc_D.md:26`, `:36`, `:39`, `:59`, `:161`, `:165`, `:224-226`, `:241-242`, `:251`, `:477`, `:634`, `:665-667`.
- `sources/Act_III_Arc_E.md:13`, `:72`, `:262`, `:377`, `:393-405`, `:407-409`, `:512-515`, `:594-596`, `:612-631`, `:648`, `:685-689`, `:892`.
- `sources/Appendix_B_-_Player_Factions.md:658`; `sources/Appendix_D_-_Running_the_Tavern.md:1549`.
- `sources/SOURCE_GUIDE.md:35` ("Contains: Manshoon, his simulacrum, Sidra Romeir, Manafret Cherryport, Vevette Blackwater, Agorn Fuoco, Urstul Floxin.") and `:190`.

Published adventure (`sources/adventure-wdh.json`): lines 341-342, 862, 1686-1687, 1715, 2183-2185, 4032-4035, 4368-4380, 4480, 4543-4545, 4791-4792, 4803-4816, 4836-4837, 5796-5797, 5882, 5951-5954, 26762-26763, 30033-30042, 32445-32446, 32640-32657, 32782.
Key lines: 1686 "Volo met {@creature Floon Blagmaar|WDH} for drinks at the Skewered Dragon two nights ago. They drank and gambled for a few hours, and then Volo left. That's the last he saw of Floon."; 4480 "Fala saw {@creature Urstul Floxin|wdh} fleeing the scene with the {@item Stone of Golorr|WDH} in his clutches. He circled around the Bent Nail (see chapter 2, {@area T2|09b}) on his way out of Trollskull Alley."; 4804 (quoted in D1); 4815 "Having gravely misjudged and underestimated Lady Gralhund once, Urstul isn't about to do so again. Rallying despite his injuries, he manages to kill the two inattentive Gralhund guards who were watching over him and alert the other Zhents on the estate, who begin dispatching the other guards and servants. Urstul's goal is to capture Lord or Lady Gralhund, force the surrender of the {@item Stone of Golorr|WDH}, and deliver it to his master {@creature Manshoon|WDH} in Kolat Towers (described in chapter 8)."; 4836 "Apparently, the Gralhunds had been held hostage for more than a tenday by agents of the Black Network. Most of the Zhents were killed during a bloody revolt led by Lord Gralhund himself."; 4837 (quoted in D8); 4791 "The man Fala saw matches the description of {@creature Urstul Floxin|wdh}, a suspected member of the Black Network."; 4792 "Another North Ward resident claims he saw Urstul enter Gralhund Villa, in the North Ward, shortly after the fireball incident. The resident reported him to the City Watch because Urstul looked suspicious."; 4033-4035 (D2, D8). 5952 (quoted). 26763 (quoted in E). 30041 (quoted in F5/G). 

Wiki (`scratchpad/wiki-manshoons-zhentarim/02-urstul-floxin.txt`): lines 11-19, 57-65, 75, 78, 81 (quoted in A, B, D).

## Not found

Searched for `Urstul`, `Floxin` and `Urstul Floxin` across: `campaign/` (all subfolders, including setting, guides, gazetteer, locations, quests, structure), `sources/adventure-wdh.json`, `sources/SOURCE_GUIDE.md`, `sources/Act_III_Arc_D.md`, `sources/Act_III_Arc_E.md`, `sources/Appendix_B/C/D`. Results:

Not found (the drafter would have to invent these, or mark them [design] under ruling 17):
- Birthplace, parents, siblings, children, spouse (wiki infobox blank; no other source).
- Former employment or career before the Zhentarim.
- Date or year he joined the Black Network, date he took his current post, length of service.
- How he met or was recruited by Manshoon.
- Faith, deity, oath, rite (no campaign source; the organization page's Beliefs section has none).
- Friends or lovers (outside the dead underlings Bashekk Ortallis and Wern Malkrave).
- Named fears, losses or grudges before the campaign (the published "Renaer" grudge at line 4035 is the only pre-campaign one).
- Hair, eyes, scars, clothing, voice before the quest (only build and age).
- Any source naming Floxin in `campaign/setting/lore/`, `campaign/setting/governance-and-guilds/`, `campaign/setting/deities/` (except `bane.md:73`, which names only "Floxin's cell"), or `campaign/setting/notable-figures/` outside the Manshoon and Gralhund folders (no hits; the Gralhund and Manshoon folders hit).
- Appendix C (Player Faction Missions): no match for Urstul or Floxin. (Appendix B has one entry at line 658; Appendix D one at line 1549.)
- A residence on Ches 1 that the sources agree on (see D1).

Searched but outside this report (matched in the file list, not opened): `sources/research/pass3-bundles/stone-of-golorr-and-the-eyes/wiki.txt`, `sources/research/pass3-bundles/vault-of-dragons/wiki.txt`, `sources/research/pass5-bundles/gralhunds/wiki.txt`, `sources/research/pass5-bundles/doom-raiders/wiki.txt`, and the `campaign-hits.txt` and `adventure-hits.txt` files in pass3, pass4 and pass5 bundles. These are bundle grep output. They were not opened for this report.

## Not readable

- `.docx` files (cannot be opened with these tools). The SOURCE_GUIDE (`sources/SOURCE_GUIDE.md:683-698`) lists these as NPC or faction sources in `sources/Other remix files/`. These may mention Floxin:
  - `Renaer Neverember Guide, his backstory and family secrets.docx` (`SOURCE_GUIDE.md:693`; "Finding Floon, Gralhund Villa").
  - `Davil and the Doom Raider Zhents + Elf Killer mission and more.docx` (`SOURCE_GUIDE.md:688`; "the Zhentarim (Doom Raiders)" page).
  - `The Waterdavian's Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx` (`SOURCE_GUIDE.md:695`; "Secondary reference only").
  - `Cassalanters, their tragic backtstory, and Endgame setup.docx` (`SOURCE_GUIDE.md:687`; Floxin not expected).
- Alexandrian PDFs read: `sources/4. Gralhund Villa.pdf` (PDF pages 1-4, printed pp. 26-29; transcribed from page images, flag for `pdftotext`); `sources/1. The Villains.pdf` (all 7 PDF pages, printed pp. 13-19; no mention of Floxin; the Zhentarim section is printed p. 16, PDF page 4).
- Alexandrian PDFs not read for this report: `sources/2. Other Factions.pdf` (p. 21 is cited at `campaign/guides/factions/13-house-gralhund.md:119` and not checked), `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, `sources/13. Clues and Timelines.pdf`, `sources/14. Finding Floon.pdf`, `sources/15. The Nimblewright Investigation.pdf`, `sources/16. Backtracking Dalakhar  Kalain.pdf`, `sources/17. Outpost and Lair Revelation Lists.pdf`. The `.md` remixes of Arc D and Arc E were used in place of the Gralhund PDF text. The PDFs for Kolat Towers and Finding Floon may hold Floxin material and should be checked by the orchestrator.
- The extracted wiki is read in full (`scratchpad/wiki-manshoons-zhentarim/02-urstul-floxin.txt`, 108 lines).
- Model pages `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md` and `11-gorath.md` were not opened (format inputs; no Floxin facts expected).
- The Ott notes file named in the generic instructions does not exist at that path (see Method).
- Not run: `voicecheck.py` (research only; no prose written).
