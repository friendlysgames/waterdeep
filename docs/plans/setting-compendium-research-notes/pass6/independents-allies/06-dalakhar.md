# Pass 6 research notes: Dalakhar

Page: `campaign/setting/notable-figures/independents-allies/06-dalakhar.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 19). Ruling used: Ches 1, 1492 DR is day one. Dalakhar is alive on Ches 1 and dies at the fireball on Ches 22 (quest time).
Organization page: `campaign/setting/organizations/12-house-gralhund.md` (names him as Dagult Neverember's agent). No organization page exists for the Neverember family.
Factions Guide: `campaign/guides/factions/13-house-gralhund.md:19` and `:119`.
Voice profile: `.claude/skills/character-voices/voices/independents-allies.md` lines 120 to 134.
Wiki: `scratchpad/wiki-independents-allies/06-dalakhar.txt` (full page, not a stub). Editions: the wiki cites *Waterdeep: Dragon Heist* 5e (WDH5e) by ref name.

## Method and caveats

- No shell. Alexandrian PDFs read with the Read tool as images; the transcriptions must be checked with `pdftotext -layout` before prose use: `sources/13. Clues and Timelines.pdf` PDF page 2 (printed p.98) and PDF page 3 (printed p.99); `sources/16. Backtracking Dalakhar  Kalain.pdf` PDF page 1 (printed p.117), PDF page 2 (p.118) and PDF page 4 (p.120); `sources/15. The Nimblewright Investigation.pdf` PDF page 3 (printed p.109); `sources/29. Addendum Timelines  Starting the Campaign.pdf` PDF page 1 (printed p.225, no Dalakhar).
- `voicecheck.py` was not run. No file was edited except these notes.

## Findings that change how the page is written

1. **The Stone's theft date is the largest conflict.** The GM Guide says Dalakhar "steals it on Ches 20" (`running-the-villains.md:19`). The Players Arrive Lore Summary says he "has the Stone and is carrying it toward Trollskull Manor" with no date (`history/08-the-players-arrive.md:24`). A day-one page must not give him the Stone. The theft is quest time.
2. **On Ches 1 he is alive and no longer on Renaer's watch.** The Gralhund house page and the Alexandrian both have him moved from watching Renaer to infiltrating Xanathar's Guild before the campaign. The exact timing is open (D2).
3. **The Alexandrian letter places a Red Magic assignment four years earlier.** No campaign file uses it (D3).
4. **Dalakhar is the fireball's intended target, not the Trollskull Alley victim.** The GM Guide designates the victim from a candidate list that does not include him (`campaign/guides/gm-guide/structural-rules.md:100` to `:107`).

---

## A. Background facts by theme

### A1. Origin and the Neverember service

Wiki (edition WDH5e, ref names as printed):

> "'''Dalakhar''' was a [[thief]] and spy in [[Waterdeep]] working for Lord [[Dagult Neverember]] in the late 15{{th}} century [[DR]].<ref name="WDH5e-p11">{{Cite book/Waterdeep: Dragon Heist|11}}</ref>"
> — `scratchpad/wiki-independents-allies/06-dalakhar.txt` line 61

> "| race           = [[Rock gnome]]" (line 13); "| occupation     = [[Thief]] and spy<ref name="WDH5e-p11" />" (line 15); "| home           = [[Waterdeep]], [[Sword Coast North]]" (line 10); "| sex            = Male" (line 12)
> — same file

> "In [[1492 DR]],{{WDH-time}} Dalakhar was spying upon [[Renaer Neverember]], the estranged son of his master.<ref name="WDH5e-p49">{{Cite book/Waterdeep: Dragon Heist|49}}</ref> At one point, however, Lord Dagult ordered many of his agents, including Dalakhar, to obtain the ''[[stone of Golorr]]'' from the lair of the [[Xanathar]]. The rock gnome managed to steal the stone, ruining a meeting between Xanathar and the [[Zhentarim]].<ref name="WDH5e-p5">{{Cite book/Waterdeep: Dragon Heist|5}}</ref>"
> — same file, line 64 (the wiki gives no date for the theft)

> "Dalakhar was very loyal to his master, believing Dagult to be the rightful [[Open Lord]] of Waterdeep.<ref name="WDH5e-p46">{{Cite book/Waterdeep: Dragon Heist|46}}</ref>"
> — same file, line 69

Published adventure:

> "Who actually stole the {@item Stone of Golorr|WDH}? The answer: a rock gnome named Dalakhar. After Lord Neverember used magic to discern the gemstone's location, he sent forth a succession of spies to infiltrate {@creature Xanathar|WDH}'s lair and obtain it. Dalakhar succeeded where many others before him had failed, but his success turns out to be short-lived."
> — `sources/adventure-wdh.json:474` (undated)

> "\"House Gralhund has been bankrolling Black Network operations in Waterdeep, including the plot to kidnap {@creature Renaer Neverember|wdh} and the plot to steal the {@item Stone of Golorr|WDH} from his father's gnome spy, Dalakhar.\""
> — `sources/adventure-wdh.json:5967` (a line in the Gralhund Villa chapter; the speaker is not named in the text read)

### A2. Pre-campaign history (campaign pages, Alexandrian)

> "Dalakhar, a rock gnome spy, serves Dagult Neverember. He had questioned Kalain about Neverember's vault years before the campaign."
> — `campaign/setting/history/08-the-players-arrive.md:55`

> "Neverember's agents did not know the full picture. Dalakhar was told to watch Renaer and not told why, because Neverember's chief concern was keeping the hidden Eye safe until he could regain the Stone."
> — `campaign/setting/history/06-the-open-lords-fall.md:88`

> "Months before Ches 1, 1492 DR: The house embedded agents in Renaer Neverember's household. They spotted Dalakhar watching Renaer, identified him as an agent of Lord Neverember, and followed him when he was pulled off that assignment to Xanathar's Guild."
> — `campaign/setting/organizations/12-house-gralhund.md:24`

> "- **Embed and observe:** The house plants agents inside other households and watches who watches them. Renaer is estranged from his father, so the house knew the placement was a long shot, and it paid off: the agents in his household caught Dalakhar's surveillance and traced him to Xanathar's Guild. Orond's journal gives the two informants the code names \"Eagle\" and \"Catoblepas.\""
> — `campaign/setting/organizations/12-house-gralhund.md:56`

> "- **Xanathar's Guild** (neutral, watched): The house traced Dalakhar into the Guild and did not know the Guild held the Stone."
> — `campaign/setting/organizations/12-house-gralhund.md:68`

The Alexandrian timeline (`13. Clues and Timelines.pdf`, PDF page 2, printed p.98; transcribed from image):
> "Lord Neverember sends a network of agents into Waterdeep. Many of these agents are attempting to locate the *Stone*. One of them, Dalakhar, is assigned to keep a watchful eye on Dagult's son, Renaer. (Dalakhar isn't told this, but Lord Neverember's primary concern is that the Eye unwittingly carried by Renaer is kept safe until he can regain the *Stone*.)"

PDF page 3, printed p.99 (transcribed from image):
> "Lord Neverember discovers that Xanathar stole the *Stone*. Dalakhar is sent to infiltrate Xanathar's organization and steal the *Stone* back. (At this point Lord Neverember believes that Xanathar has the *Stone* and that the Zhentarim still have the Eye they stole from him. To maintain the original siloing of information, Dalakhar is not told about the Eyes and doesn't know to look for the one Xanathar now holds.)"

Same PDF page, under DRAGON HEIST BEGINS (1492 DR), quest time:
> "With Dalakhar's network removed from watching over Renaer, he's exposed."

PDF 16, printed p.120 (transcribed from image; see D3):
> "A letter from Dalakhar also dating to four years ago, reporting on his unsuccessful efforts to infiltrate Red Magic in the Castle Ward. (GM Note: This is literally a red herring. Dalakhar's assignment four years ago has nothing to do with present events. The Red Wizards of Thay use the Thayan embassy as a cover for their local operations; it's connected to the Thayan enclave in Skullport via a portal.)"

### A3. Work, method and manner

Act III, the Trades Ward trace (quest time; the Ches 22 departure):
> "Characters who want to understand why Dalakhar was in Trollskull Alley may trace his recent movements. A successful DC 15 Charisma (Investigation) check, made over a day's inquiry through inns and lodging houses in the Trades Ward, reveals he rented a room for one night at the **Inn of the Dripping Dagger** in the Trades Ward and then departed."
> — `sources/Act_III_Arc_D.md:483`

Renaer's account of the watch (`sources/adventure-wdh.json:4781`; quest time, given after the fireball):
> "\"When the Lords of Waterdeep ousted my father, I thought his long, dark shadow was finally gone for good. The truth is, I want nothing to do with him. But his spies hound me. One of them, a gnome named Dalakhar, had been watching me for months. Then, about two tendays ago, the spy was suddenly nowhere to be seen. My father didn't trust many people, but he trusted that gnome.\""
> — conflict with the campaign timing, D2

Renaer's account in the Act III file (`sources/Act_III_Arc_D.md:236`):
> "\"I know who he is. Dalakhar. He's one of my father's — one of my <em>estranged</em> father's — operatives. A spy. The man has followed me off and on for years, watching me on my father's behalf. I want nothing to do with any of it. But I spoke to some of Dalakhar's acquaintances once, when I was curious. Apparently he had been on some special mission to recover something called the <em>Stone of Golorr</em>. He thought the Zhentarim and the Xanathar Guild were about to catch him. When he heard what you had done for me — rescuing me from the Zhentarim — I think he decided you were trustworthy enough to hold it for him temporarily while he lost his pursuers. He was running to <em>you</em>.\""
> — quest time (the Stone and the rescue)

Dalakhar's own room, Ches 22 (quest time):
> "She remembers Dalakhar clearly — he was small, alone, paid in coin, asked for an upper-floor room with a window visible from the street, and left before breakfast though he had prepaid through the evening."
> — `campaign/quests/act-ii/fireball/ev-06-the-death-mark.md:21`

### A4. Kalain and the letter

Kalain's letter, Act III file (`sources/Act_III_Arc_D.md:565`; PDF 16 page 2, printed p.118, transcription agrees):
> "*I had to give considerable thought to your request. But you were always kind to me even when your demonic master was not. If you are still in need of my aid, you may claim whatever sanctuary I can offer.*"
The source does not name the "demonic master". Dagult is the only master the sources name for him (D5).

Act III, the Kalain entry (`sources/Act_III_Arc_D.md:569`; quest time):
> "Before he was killed, Dalakhar had been casting about desperately for any safe harbor he could find. He even contacted Kalain — a former mistress of Lord Dagult Neverember, now largely estranged from polite society — on the slim hope that her old affection for him might translate into shelter. Her reply arrived too late."

Kalain's affair is Neverember's, not Dalakhar's:
> "- In 1475 DR he commissioned a portrait from the painter Kalain, and the two had an affair that lasted more than a year. He later used his influence to ruin her reputation and her work."
> — `campaign/setting/history/06-the-open-lords-fall.md:36`

### A5. Temperament, loyalty and habits (page and voice profile)

Voice profile (day-one parts):
> "- **Personality in speech:** Cautious determination and operative pride. His fear shows as constant glances and half-finished instructions. Loyalty to Neverember is absolute, even dead." — `.claude/skills/character-voices/voices/independents-allies.md:127` (the clause "even dead" is quest time, C14)
> "- **Quirks:** He checks behind himself mid-sentence. He calls the Stone \"the package\" and never by name." — same file, line 128
> "- **Never:** He never betrays Neverember, never gives his real plans to strangers, and never relaxes." — same file, line 130

Sewer habit, quest time (a body detail, not a day-one fact):
> "The dead gnome has dry waste on his boots and cloak, suggesting he has spent time in the sewers recently. He also has a pouch containing five 100 gp gemstones." — `sources/adventure-wdh.json:4415`

---

## B. Alignment, species, pronouns, stat block

- Page summary: "> - *Rock gnome spy, neutral, he/him*. Stat block: **Spy**." — `06-dalakhar.md:5`
- Adventure: "One male gnome (Dalakhar) wearing a burned cloak and clutching a dagger" — `sources/adventure-wdh.json:4406`
- Wiki: "| race           = [[Rock gnome]]" (line 13); "| sex            = Male" (line 12). "| alignment5e    = " is blank (line 56).
- Alignment "neutral": page summary only. No adventure or wiki line gives an alignment.
- Stat block "Spy": page summary only. No adventure or wiki line gives a stat block for Dalakhar. The Zhentarim sellswords are described at `sources/adventure-wdh.json:4404`, not him. Wiki occupation: "[[Thief]] and spy" (line 15).

---

## C. Quest-time sentences on the current page and the voice profile

Ruling 1: restate as a day-one fact, or remove and route. The file where each already lives is given.

| # | Where | Sentence (exact) | Where it already lives |
|---|---|---|---|
| C1 | Summary L6 | "> - **Affiliation:** Agent of Dagult Neverember" | Day one. Keep (`12-house-gralhund.md:24`). |
| C2 | Summary L7 | "**Featured in:** **Fireball!**, **Gralhund Villa**, **Vault of Dragons**, **House of Inspired Hands**, **Sea Maidens Faire**" | Backed: Fireball! (`campaign/quests/act-ii/fireball/ev-01-the-fireball.md:25`); Gralhund Villa (`campaign/quests/act-ii/gralhund-villa/ev-03-daytime-infiltration.md:66`); Sea Maidens (`campaign/locations/sea-maidens-faire/05-scarlet-marpenoth.md:23`: "A small figure (Dalakhar) running through Trollskull Alley toward the harbor."). Vault: `campaign/quests/act-ii/fireball/ev-07-kalainsalley-tower.md:77` ("The Dalakhar Papers ... are read at Vault of Dragons, not before."). House of Inspired Hands: no hit in `campaign/locations/house-of-inspired-hands/`. |
| C3 | Resonance L11 | "Dalakhar should inspire respect for his competence (he stole the Stone where many before him failed), sympathy for his doomed loyalty, and curiosity through the fragments the party pieces together after his death." | The theft: `running-the-villains.md:19` ("steals it on Ches 20"). The death: `ev-01-the-fireball.md:8`. |
| C4 | Emotions L13 | "Dalakhar most often felt cautious determination, operative's pride, growing fear of pursuit, unshakable loyalty to Dagult Neverember, and exhaustion from days living in the sewers." | "growing fear of pursuit": the fear is day one (`history/08-the-players-arrive.md:57`), the pursuit's outcome is quest time. "exhaustion from days living in the sewers": `ev-01-the-fireball.md:48` ("Sewer silt dried on Dalakhar's boots and cloak hem — he came up through the sewers recently."). `history/08:127` quotes "weeks living in the sewers" (E). |
| C5 | Motivations L15 | "Dalakhar wanted to deliver the Stone of Golorr to the party (planning to reclaim it later for Neverember), avoid the Zhentarim and Xanathar agents closing in, and serve the man he believed was Waterdeep's rightful Open Lord." | Delivery plan: `ev-01-the-fireball.md:180` ("Dalakhar's letter states the Stone is in his hands and he was on his way to Trollskull Manor."); adventure `:4536` ("He was on his way to deliver it to them, planning to come back and reclaim it after he had eluded his pursuers."). Keep the loyalty half (wiki line 69). |
| C6 | Persona L21 | "To the world, Dalakhar was a small gnome with dry waste on his boots and sewer-stink on his cloak. To those he trusted, he was Neverember's most reliable agent, the one who succeeded where many others had failed. Deep down, he was afraid that the Zhentarim and Xanathar's Guild were close to catching him, and he was right." | "dry waste on his boots and cloak": `adventure-wdh.json:4415` (quest time, a body detail). "the one who succeeded where many others had failed": `:474` (undated). "and he was right": the Ches 22 outcome (`ev-01-the-fireball.md:8`). The fear is day one (`history/08:57`). |
| C7 | Morale L23 | "Dalakhar is dead when the party encounters him. Via Speak with Dead, he answers questions with the clipped precision of a trained spy who remains loyal to his employer even in death." | `ev-01-the-fireball.md:92` ("**Dalakhar** (up to 5 questions): ..."); `sources/adventure-wdh.json:4529` ("A {@spell speak with dead} spell can pry some or all of the following information from Dalakhar's corpse if the right questions are asked:") |
| C8 | Relationships L25 | "Dalakhar was an agent of Dagult Neverember, known to Renaer (\"My father didn't trust many people, but he trusted that gnome\"), and the last person to hold the Stone of Golorr before it entered the Grand Game." | Renaer's line is quest time: `sources/adventure-wdh.json:4781`. "the last person to hold the Stone": conflict, D4. The agent clause is day one (C1). |
| C9 | Overview L29 | "Dalakhar was a quiet rock gnome who died in the fireball that tore through Trollskull Alley. Whatever brought him to the North Ward that morning died with him, unless someone goes looking." | `ev-01-the-fireball.md:8` ("The fireball kills twelve: Dalakhar, two Zhentarim, eight bystanders, and the Trollskull Alley victim."); `ev-01-the-fireball.md:243`. Quest time. |
| C10 | Voice L121 (tagline) | "*A sewer-worn gnome spy, heard only in flashback or through Speak with Dead: terse, hunted and loyal to the end.*" | The profile is built on the death. "Speak with Dead" and "flashback" are quest-time forms. |
| C11 | Voice L123 (Sound) | "... Through Speak with Dead, flat and faraway." | Quest time (the corpse). `ev-01-the-fireball.md:92` |
| C12 | Voice L124 (Sentence shape) | "Speak with Dead answers are five words or fewer, and literal." | Quest time. `ev-01-the-fireball.md:92` |
| C13 | Voice L126 (Swearing) | "... Tired and bitter (\"Fucking Zhents, fucking Xanathar, fucking sewers.\") when alive and hunted. None through Speak with Dead." | "when alive and hunted" is day one (`history/08:57`). "None through Speak with Dead" is quest time. |
| C14 | Voice L127 (Personality) | "... Loyalty to Neverember is absolute, even dead." | "even dead" is quest time. |
| C15 | Voice L132 (Sample, flashback) | "*Greeting (flashback):* \"You. Don't look at me. Keep walking. Take this.\"" | Quest-time flashback; it implies the Stone handover, which the page places after Ches 1 (`ev-01-the-fireball.md:180`). |
| C16 | Voice L133 (Sample, Speak with Dead) | "*Speak with Dead:* \"The package. For the Open Lord.\"" | Quest time. |
| C17 | Voice L134 (Sample, under pressure) | "*Under pressure:* \"They're close. Shit. Go, go, go.\"" | Day one if it means the Renaer watch; quest time if it means the Ches 22 chase. Drafter's call. |

Quest-time items the page does not carry, routed:
- The fireball and the Stone's removal: `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:32` ("The nimblewright threw the bead from the cooperage rooftop to the east, dropped to the street, rifled Dalakhar's body, took the Stone of Golorr, and fled east across the rooftops.")
- The paper bird: `ev-01-the-fireball.md:171` ("He carries Dalakhar's paper bird, sent that morning before the blast ...").
- Speak with Dead answers: `ev-01-the-fireball.md:92` and `sources/adventure-wdh.json:4533` to `:4536`.
- The Trades Ward inn and the death mark: `ev-06-the-death-mark.md:15`, `:21`, `:40`.
- Vajra's dossier: `ev-06-the-death-mark.md:68` ("She has a partial dossier on Dalakhar: confirmed his role as Neverember's agent, notes he infiltrated Xanathar's organization before going dark.")
- Cassalanter knowledge: `ev-05-the-cassalanter-dinner.md:45` ("Victoro knows Dalakhar worked for Neverember, the Stone is the key to a concealed vault, ...").
- The Kalain letter, four days after: `ev-06-the-death-mark.md:76`.
- The Gralhund seizure of Renaer "to recover the Stone from Dalakhar": `campaign/quests/act-ii/gralhund-villa/ev-05-the-guest-suite.md:49` and `organizations/12-house-gralhund.md:26` ("The night before Ches 1, 1492 DR: Zhentarim agents seized Renaer Neverember on the night Floon Blagmaar was taken. The house paid for the operation, and Yalah arranged it to gain leverage over Dalakhar.").
- The Stone's chain: `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:52` ("**Ches 22:** The fireball kills Dalakhar. The Gralhund nimblewright takes the Stone from his body and carries it to **Gralhund Villa** ...").

---

## D. Conflicts

**D1. When he took the Stone**
- `campaign/guides/gm-guide/running-the-villains.md:19`: "Xanathar holds it in its lair until Dalakhar, a rock gnome spy in Neverember's employ, steals it on Ches 20; he was carrying it to Trollskull Manor when the fireball killed him on Ches 22."
- Alexandrian, PDF 13 printed p.99 (transcribed): "Ches 20th: Dalakhar successfully steals the *Stone* from Xanathar."
- Same campaign page, conflicting: `campaign/setting/history/08-the-players-arrive.md:24`: "Dalakhar, the agent of Dagult Neverember, has the Stone and is carrying it toward Trollskull Manor. Urstul Floxin's Zhentarim cell is tracking him." and `:56`: "By the morning of Ches 22 Dalakhar has the Stone of Golorr and is carrying it to Trollskull Manor, where he means to deliver it to the party. Which keeper he took it from is unsettled. See Draft Notes."
- Routed: `campaign/setting/history/06-the-open-lords-fall.md:162`: "Dalakhar's 1492 DR mission, the Ches 20 theft and his death on Ches 22 belong on **The Players Arrive**."
- Higher ranked: `running-the-villains.md:19` (GM Guide) and the Stone page (`stone-of-golorr-and-the-eyes.md:51`). `history/08:24` is a Lore Summary line that contradicts the same page's `:56` and `:127`.

**D2. Still on the Renaer watch on Ches 1?**
- Renaer, quest time (`adventure-wdh.json:4781`): "Then, about two tendays ago, the spy was suddenly nowhere to be seen."
- Alexandrian, PDF 15 printed p.109 (transcribed): "A few weeks ago, though, he abruptly disappeared and Renaer doesn't know where he's been. (If the PCs ask, it happened just before Renaer was kidnapped by the Zhentarim.)"
- Campaign: `history/06-the-open-lords-fall.md:88` ("Dalakhar was told to watch Renaer"); `organizations/12-house-gralhund.md:24` ("when he was pulled off that assignment to Xanathar's Guild").
- Higher ranked: campaign. The campaign says the surveillance ended with the pull-off to the Guild, before Ches 1. The adventure and the Alexandrian give "two tendays" and "a few weeks". The drafter should check this against `history/08`.

**D3. Red Magic assignment**
- Alexandrian, PDF 16 printed p.120 (transcribed; A2). A Grep of `campaign/` for "Red Magic" found no match.
- Higher ranked: campaign (silence). The drafter decides; the fact is not in any campaign file.

**D4. "The last person to hold the Stone"**
- Page L25: "the last person to hold the Stone of Golorr before it entered the Grand Game."
- `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:186`: "Which keeper Dalakhar took it from is unsettled in `history/08-the-players-arrive.md:58`, and the page follows his speak with dead answer in `ev-01:94` (a beholder called Xanathar)."
- Higher ranked: campaign. Xanathar is the named prior holder.

**D5. "Demonic master"**
- `sources/Act_III_Arc_D.md:565` (and the PDF 16 transcription): "your demonic master". No source names the master. Cassalanter secrecy applies: nobody outside the household and the cult knows about the pact. Do not link Dalakhar to the infernal pact on this phrase alone.

**D6. Undated theft in the adventure**
- `sources/adventure-wdh.json:474` ("succeeded where many others before him had failed") and `:854` ("Dalakhar, a gnome thief working for Dagult, tries to smuggle the Stone of Golorr out of Waterdeep.") are undated. Campaign: Ches 20 (D1).

---

## E. Stale lines in other files (not edited), and routed references

- `campaign/setting/history/08-the-players-arrive.md:127` (Draft Notes): "... and \"weeks living in the sewers\" in the Dalakhar page does not fit a Ches 20 theft." The current page says "exhaustion from days living in the sewers" (page L13). The note quotes earlier wording.
- `campaign/setting/history/08-the-players-arrive.md:24`: "has the Stone and is carrying it toward Trollskull Manor" (Lore Summary; conflicts with `:56`, D1).
- `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:51`: "- **Ches 20:** Dalakhar steals it from Xanathar's lair on Neverember's orders." and `:52` (the Ches 22 fireball). A lore page narrating quest time, against the campaign-start rule.
- `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:8`: "The table holds on the morning of Ches 22, when **Fireball!** opens, because the Xanathar and Manshoon cells assume Dalakhar has already taken the Stone from Xanathar's lair." A day-one table set on Ches 22.
- `campaign/setting/organizations/08-xanathars-guild.md:189`: "**Routed to quests (ruling 28):** The theft of the Stone. \"Xanathar held the Stone of Golorr until Dalakhar stole it\" happens on Ches 20, after campaign start."
- `campaign/setting/organizations/12-house-gralhund.md:155` and `:162`: the seizure motive (`ev-05-the-guest-suite.md:49` against `running-the-villains.md:19`).
- `campaign/setting/organizations/12-house-gralhund.md:171`: "when it was stolen they were among the first to suspect (and then know) that Dalakhar was responsible" (cites `2. Other Factions.pdf` p. 20; PDF 2 not re-read). The theft is on Ches 20 and belongs to **Fireball!**.
- `campaign/guides/factions/13-house-gralhund.md:19`: "On Ches 22, Yalah sends the nimblewright to Trollskull Alley, and Dalakhar dies in the fireball." (quest time)
- `campaign/guides/trollskull-manor/08-notable-patrons.md:50`: "Quiet update on the investigation into Dalakhar's murder — sits with his back to the wall" (quest time; Renaer's patron entry).
- `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:73`: "Do you know a man named Dalakhar? Small, gnomish build?" (quest time)
- `sources/Appendix_D_-_Running_the_Tavern.md:1307`: "Requests a quiet update on the investigation into Dalakhar's murder — what the characters have found, what they suspect." (quest time)
- `campaign/gazetteer/waterdeep/trades-ward.md:69`: "Hook: in **The Death Mark** Myl lets the party into Dalakhar's room for an honest request, a Watch badge or 5 gp. The room was scrubbed before he left." (quest time)
- `campaign/quests/act-ii/fireball/overview.md:43`: "- **Dalakhar** (deceased) — rock gnome spy; Neverember's agent; can answer five questions via *Speak with Dead* for five days after the blast" (quest time)
- Not readable: none for Dalakhar.

---

## F. Gaps a Background needs, and the sourced facts to stay consistent with

1. **Birthplace, age, family, how he became a spy.** No source. Wiki infobox blank: "| dob            = " (line 20), "| age            = " (line 16), "| parents        = " (line 28).
2. **His handler and tasks.** Neverember ordered him to watch Renaer (`history/06:88`) and, later, to "infiltrate Xanathar's organization and steal the *Stone* back" (PDF 13, printed p.99, transcribed).
3. **Where he lodged.** A Trades Ward inn, one night before the Ches 22 blast (`Act_III_Arc_D.md:483`). The room is quest time.
4. **Kalain.** "He had questioned Kalain about Neverember's vault years before the campaign." (`history/08:55`). See A4 for the affair, which is Neverember's.
5. **Renaer.** Dalakhar's pre-campaign watch on Renaer: `history/06:88` (D2). Renaer's own words on the watch are quest time (`adventure-wdh.json:4781`).
6. **Red Magic (Alexandrian only).** D3.

---

## G. Inner-life hints in the sources (exact quotes)

- "unshakable loyalty to Dagult Neverember" (page L13)
- "Dalakhar was very loyal to his master, believing Dagult to be the rightful [[Open Lord]] of Waterdeep." (`06-dalakhar.txt` line 69)
- "He calls the Stone \"the package\" and never by name." (voice L128)
- "Dalakhar was spying upon [[Renaer Neverember]], the estranged son of his master." (wiki line 64; the watch)
- "He was on his way to deliver it to them, planning to come back and reclaim it after he had eluded his pursuers." (`adventure-wdh.json:4536`; quest time)
- Kalain's letter: "you were always kind to me even when your demonic master was not." (`Act_III_Arc_D.md:565`; see D5)
- "Before he was killed, Dalakhar had been casting about desperately for any safe harbor he could find." (`Act_III_Arc_D.md:569`; quest time)
- "The dead gnome has dry waste on his boots and cloak" (`adventure-wdh.json:4415`; quest time)
