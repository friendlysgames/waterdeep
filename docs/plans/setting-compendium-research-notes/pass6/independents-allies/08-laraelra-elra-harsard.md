# Pass 6 research notes: Laraelra "Elra" Harsard

Page: `campaign/setting/notable-figures/independents-allies/08-laraelra-elra-harsard.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 19). Ruling used: Ches 1, 1492 DR is day one. Elra has no scripted quest appearance. The quest files name her only as a past rescuer.
Organization page: none. The Black Tears are Renaer Neverember's personal circle (`campaign/setting/notable-figures/independents-allies/02-renaer-neverember.md:25`). Force Grey page: `campaign/setting/organizations/05-force-grey.md`.
Factions Guide: none for Elra.
Voice profile: `.claude/skills/character-voices/voices/independents-allies.md` lines 156 to 170.
Wiki: `scratchpad/wiki-independents-allies/08-laraelra-elra-harsard.txt` is the NOT FOUND stub. The full Forgotten Realms Wiki dump has the page: `scratchpad/fandom-dump/forgottenrealms_pages_current.xml`, page title "Laraelra Harsard", XML lines 1201561 to 1201660. Cited as "dump line N" with entities decoded. Its only source is *Blackstaff Tower* (BST), cited by ref name.

## Method and caveats

- No shell. The Alexandrian PDF `sources/27. Addendum A Night in Trollskull Manor.pdf` PDF page 7 (printed p.184) was read as an image: rows 7 and 8 read "Renaer's Friends" and do not name her. Check with `pdftotext -layout` before prose use.
- No Alexandrian PDF or markdown names Elra. The published adventure has no Elra text (Grep for "Laraelra", "Elra" and "Harsard" in `sources/adventure-wdh.json`: no match).
- `voicecheck.py` was not run. No file was edited except these notes.

## Findings that change how the page is written

1. **The wiki gives Elra a different species, class and office.** The dump says she was a "human sorceress" and "the Blackstaff's Heir under Vajra Safahr" as of 1479 DR (dump lines 1201590, 1201632). The page says "Half-elf mage" and mentions no heir post (D1 to D3).
2. **The campaign's only source for her history is the Force Grey quest files.** Both name her as one of Vajra's three rescuers in 1479 DR (`ev-01-first-meeting.md:21`; `m03/ev-01-the-tenday-watch.md:23`). The Meloon page names only Renaer.
3. **The Force Grey org page says she "has no Notable Figures page"** (`05-force-grey.md:165`). That line is stale now that this page exists (E1).
4. **Her Trollskull role is a d20 Renaer's Friends row** (`sources/Appendix_D_-_Running_the_Tavern.md:1136`; `campaign/guides/trollskull-manor/06-tavern-time.md:90`). Day one.

---

## A. Background facts by theme

### A1. Origin and family (wiki only, BST; the campaign is silent)

> "| sex            = Female" (dump line 1201589); "| race           = [[Human]]" (line 1201590); "| nicknames      = Elra<ref name="BST-p29">{{Cite book/Blackstaff Tower|29}}</ref>" (line 1201586); "| aliases        = Ararna<ref name="BST-p51">{{Cite book/Blackstaff Tower|51}}</ref>" (line 1201585)
> — `scratchpad/fandom-dump/forgottenrealms_pages_current.xml` lines 1201585, 1201586, 1201589, 1201590

> "'''Laraelra Harsard''' was a [[human]] [[sorceress]] with minor [[magic]]al powers.<ref name="BST-p31-32">{{Cite book/Blackstaff Tower|31-32}}</ref> As of [[1479 DR]], she was the [[Blackstaff]]'s Heir under [[Vajra Safahr]].<ref name="BST-p260">{{Cite book/Blackstaff Tower|260}}</ref>"
> — dump line 1201632

> "Laraelra was very thin, pale, and had long black hair."
> — dump line 1201635 (ref "Blackstaff Tower", no page)

> "Laraelra was an idealist who cared deeply for Waterdeep and its inhabitants. She championed the causes of underdogs, including [[dwarf|dwarves]] in the Cellarers' and Plumbers' guild who were discriminated against.<ref name="BST-p46">{{Cite book/Blackstaff Tower|46}}</ref> Despite her independence, however, she was insecure and feared her father's disapproval.<ref name="BST-p243">{{Cite book/Blackstaff Tower|243}}</ref>"
> — dump line 1201638

> "Laraelra was the daughter of the guildmaster of the [[Cellarers' &amp; Plumbers' Guild]], [[Malaerigo Harsard]].<ref name="BST-p239">{{Cite book/Blackstaff Tower|239}}</ref> As such, she had detailed knowledge of the sewers and tunnels underneath [[Waterdeep]].<ref name="Blackstaff Tower"/>"
> — dump line 1201644 (the file reads "&amp;"; decoded here)

### A2. The 1479 DR rescue (wiki, then campaign)

> "In [[1479 DR]], while exploring [[Waterdeep/Sewers|the sewers]] with her hired bodyguard [[Meloon Wardragon]], Laraelra heard a woman's screams. She was able to track the source to a house owned by [[Renaer Neverember]]. Laraelra, Meloon, Renaer, and two of his friends rescued the woman, who turned out to be the Blackstaff's Heir, [[Vajra Safahr]], who had been kidnapped after the secret murder of Blackstaff [[Samark Dhanzscul]]."
> — dump line 1201641 (the paragraph continues: "Laraelra and friends were forced to leave Waterdeep for a short time after Khondar "Ten-Rings" Naomal framed the group for Vajra's supposed murder. They returned to Waterdeep and Blackstaff Tower, where Vajra officially assumed the title of Blackstaff.")

> "Laraelra was accepted by the tower and made Blackstaff's Heir (chosen by Vajra over [[Eiruk Weskur]]), allowing her to carry and wield a [[Blackstaff (staff)|Blackstaff]] and channel Vajra's power through it."
> — dump line 1201641 (the heir clause; see D3)

> "- Vajra suspects a devourer and has no proof. Renaer, Laraelra Harsard and Meloon once pulled her out of Khondar Naomal's cells, and she never tells the party so."
> — `campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/ev-01-the-tenday-watch.md:23` (a GM bullet in the event's opening notes)

> "Vajra decided before the *Sending* went out. Renaer vouched for the party, and she trusts his word because he, Laraelra Harsard and Meloon Wardragon pulled her out of Khondar Naomal's cells. She never tells the party, and no speaker mentions it."
> — `campaign/quests/faction-events/force-grey/00-first-meeting/ev-01-first-meeting.md:21` (a GM bullet)

> "- **Settled (ruling 17):** ... Laraelra Harsard, who appears in the Force Grey quest files as one of Vajra's rescuers, has no Notable Figures page and is also left out."
> — `campaign/setting/organizations/05-force-grey.md:165` (stale; E1)

### A3. Renaer's circle and the Black Tears (campaign)

> "**Relationships.** Renaer is the estranged son of Dagult Neverember (former Open Lord, current Lord of Neverwinter), the devoted friend of Floon Blagmaar, the closest living friend of Meloon Wardragon (whose changed behavior has him alarmed), a man who rescued Vajra Safahr from Khondar Naomal's agents and left the Blackstaff permanently in his debt, a Harper-adjacent ally of Mirt and Remi Haventree, and the leader of the Black Tears (his personal circle of trusted companions)."
> — `campaign/setting/notable-figures/independents-allies/02-renaer-neverember.md:25`

> "**Relationships.** Osco is a member of Renaer's Black Tears. Elra handles the threats they can see; Osco handles the ones they cannot."
> — `campaign/setting/notable-figures/independents-allies/09-osco-salibuck.md:25`

> "**Relationships.** Torlyn is a member of the Wands noble family, a member of Renaer's Black Tears, and a wizard whose family connections give the group social access they would not otherwise have."
> — `campaign/setting/notable-figures/independents-allies/10-lord-torlyn-wands.md:25`

> "**Relationships.** Eiruk is a priest of Oghma and a member of Renaer's Black Tears. When the group's decisions carry moral weight, they look at Eiruk whether they mean to or not."
> — `campaign/setting/notable-figures/independents-allies/11-eiruk-weskur.md:25`

Renaer's Friends (d20 table; Elra is rows 9 to 10):
> "| 9–10 | Laraelra \"Elra\" Harsard |"
> — `sources/Appendix_D_-_Running_the_Tavern.md:1136` (the table heading is at `:1130`, "### Renaer's Friends Table")
> — `campaign/guides/trollskull-manor/06-tavern-time.md:90` (same row; table at `:84`)

> "| Kythorn 1–10 | Broxley Fairkettle, Tally Fellbranch, Laraelra \"Elra\" Harsard with Lord Torlyn Wands (Renaer's Friends) | 14: a Masked Lord visits (at Fame 81+); otherwise 17: a socialite demands the best table | Guild season. The night measures where the tavern stands with the city's upper floors. |"
> — `campaign/guides/trollskull-manor/06-tavern-time.md:32`

### A4. Character and voice (page and voice profile; day one)

Page Persona:
> "To the world, Elra is one of Renaer's drinking companions. To those she trusts, she is the one who checks the exits and knows the wards. Deep down, she stays close to Renaer because she believes his father's enemies will come for him eventually, and she intends to be there when they do."
> — `campaign/setting/notable-figures/independents-allies/08-laraelra-elra-harsard.md:21`

Page Morale:
> "In a fight, Elra would throw a Shield spell before her first thought finished forming. She casts defensively, layers wards on whoever is closest, and starts attacking only after everyone she cares about has cover."
> — same file, line 23

Voice profile:
> "*The Black Tears' sharp-eyed mage: confident, dry and always watching the exits.*" (line 157)
> "- **Sound:** A cool, composed half-elf voice, a little amused, never flustered." (line 159)
> "- **Personality in speech:** Settled confidence and assessment. She asks new people pointed questions. She's protective of Renaer, and it shows as irritation when he takes risks." (line 163)
> "- **Quirks:** She names the exits on arrival. She sets wards mid-conversation, and mentions it only if asked." (line 164)
> "- **Signature phrases:** \"Two exits, one window.\" / \"Ren, no.\" / \"Warded. You're welcome.\"" (line 165)
> "- **Never:** She never trusts quickly, never wastes a spell showing off, and never leaves Renaer exposed." (line 166)
> "*Business:* \"The ward on that door is Thayan work. Somebody paid for that. Find out who.\"" (line 169; a sample line)

---

## B. Alignment, species, pronouns, stat block

**Species**
- Page summary: "> - *Half-elf mage, neutral good, she/her*. Stat block: **Mage**." (`08-laraelra-elra-harsard.md:5`)
- Page Resonance and Overview: "curiosity about what a half-elf mage sees in a group of drinking buddies" (L11); "Laraelra Harsard is a half-elf mage" (L29)
- Voice profile: "A cool, composed half-elf voice" (line 159)
- Wiki: "| race           = [[Human]]" (dump line 1201590); "was a [[human]] [[sorceress]]" (line 1201632). Conflict, D1.

**Alignment**
- Page summary only: "neutral good" (`:5`). The wiki's "| alignment5e    = " is blank (dump line 1201628).

**Pronouns**
- Page summary: "she/her" (`:5`). Wiki: "| sex            = Female" (dump line 1201589).

**Stat block**
- Page summary: "Stat block: **Mage**." (`:5`). Wiki: "| class4e        =[[Sorcerer]] " (dump line 1201626); "[[Category:Sorcerers]]" (line 1201652). Conflict, D2.

**Languages**
- Wiki: "| languages      = [[Dwarvish]]<ref name="BST-p86">" (dump line 1201595). Campaign: none.

**Age, birth, parents**
- Wiki: "| age            = " (blank, dump line 1201593); "| parents        = " (blank, line 1201605); "| siblings       = " (blank, line 1201607). Campaign: none.

---

## C. Quest-time sentences on the current page and the voice profile

The page has no scripted quest sentence. The items below are the clauses that a quest outcome presumes. Ruling 1: restate or remove.

| # | Where | Sentence (exact) | Where it already lives |
|---|---|---|---|
| C1 | Summary L6 | "> - **Affiliation:** Independent (ally)" | Day one. Keep. |
| C2 | Summary L7 | "> - **Featured in:** Background figure; no scripted appearance." | Accurate for scripted scenes. The quest files name her as a past rescuer (A2), both day-one memories. |
| C3 | Resonance L11 | "Elra should inspire admiration with her arcane competence, endearment with her loyalty to Renaer's circle, and curiosity about what a half-elf mage sees in a group of drinking buddies." | Day one. No quest clause. |
| C4 | Emotions L13 | "Elra most often feels settled confidence, sharp-eyed assessment of new people, relaxed warmth among the Black Tears, intellectual restlessness, and protective alertness that surfaces when Renaer takes risks." | Day one. |
| C5 | Motivations L15 | "Elra wants to keep Renaer's circle safe, pursue her own arcane studies, and ensure that the Neverember name does not drag her friends into something they cannot handle." | Day one. |
| C6 | Persona L21 | "Deep down, she stays close to Renaer because she believes his father's enemies will come for him eventually, and she intends to be there when they do." | Day one, as her belief. It is not an event. |
| C7 | Relationships L25 | "Elra is a member of Renaer's Black Tears and the only reason the group has a real combat edge. The others fight well enough; Elra is the one who keeps them alive." | Day one. |
| C8 | Overview L29 | "Laraelra Harsard is a half-elf mage and a member of Renaer Neverember's trusted circle, the Black Tears, known for checking exits and keeping wards on her companions." | Day one. |
| C9 | Voice L168 (Greeting) | "\"Harsard. You're the ones Ren won't stop talking about. Sit where I can see you.\"" | Presumes a quest outcome: "the ones Ren won't stop talking about" presumes the party has already dealt with Renaer. The Renaer kidnap and the rescue fall on the night before Ches 1 and in Finding Floon (`campaign/guides/gm-guide/structural-rules.md:38`). Drafter's call. |
| C10 | Voice L170 (Under pressure) | "\"Ren, behind me. Everyone else, shut up and move.\"" | Day one. |

The Trollskull Alley and Fireball! files do not name Elra. The Force Grey files name her in the past tense only (A2).

---

## D. Conflicts

**D1. Species**
- Page: "Half-elf mage" (`08-laraelra-elra-harsard.md:5`, `:11`, `:29`); voice: "A cool, composed half-elf voice" (line 159).
- Wiki: "| race           = [[Human]]" (dump line 1201590); "was a [[human]] [[sorceress]]" (line 1201632).
- No Alexandrian or adventure source names her species. Higher ranked: the campaign (the page and its voice profile agree). The wiki is the only source for "human", and it cites BST.

**D2. Class**
- Page: "Stat block: **Mage**." (`:5`).
- Wiki: "| class4e        =[[Sorcerer]] " (dump line 1201626); "was a [[human]] [[sorceress]] with minor [[magic]]al powers." (line 1201632).
- Higher ranked: campaign. The wiki gives a sorcerer.

**D3. Heir to the Blackstaff**
- Wiki: "As of [[1479 DR]], she was the [[Blackstaff]]'s Heir under [[Vajra Safahr]]." (dump line 1201632); "made Blackstaff's Heir (chosen by Vajra over [[Eiruk Weskur]])" (line 1201641).
- Campaign: no line gives Elra an heir post. A Grep of `campaign/` for "Heir" and "Malaerigo" gave no Elra or Harsard line. The Vajra page (`campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md`) names no heir.
- Higher ranked: campaign (silent). The heir post is a wiki-only fact. Ruling 15 lets a wiki-only fact be used with `[research]`.

**D4. Who the rescuers were**
- Quest files: "Renaer, Laraelra Harsard and Meloon" (`m03/ev-01:23`); Meloon page L22: "who rescued Vajra alongside Renaer" (Renaer only); Renaer page L25: "a man who rescued Vajra Safahr from Khondar Naomal's agents" (no other names).
- Wiki: "Laraelra, Meloon, Renaer, and two of his friends rescued the woman" (dump line 1201641).
- Higher ranked: the quest files and the wiki agree on three rescuers. The Meloon and Renaer pages do not name her.

**D5. The Force Grey org page's note**
- `campaign/setting/organizations/05-force-grey.md:165`: "Laraelra Harsard ... has no Notable Figures page and is also left out." Stale (E1).

**D6. Her father**
- Wiki: "the daughter of the guildmaster of the [[Cellarers' &amp; Plumbers' Guild]], [[Malaerigo Harsard]]" (dump line 1201644). The campaign's Cellarers' guild is in `campaign/setting/governance-and-guilds/guilds.md:24`; no Harsard appears there.

---

## E. Stale lines in other files (not edited), and routed references

- E1. `campaign/setting/organizations/05-force-grey.md:165`: "Laraelra Harsard, who appears in the Force Grey quest files as one of Vajra's rescuers, has no Notable Figures page and is also left out." This page now exists.
- E2. `campaign/setting/organizations/05-force-grey.md:28`: "- **1479 DR, the rescue:** Renaer Neverember and Meloon Wardragon rescued Vajra from agents of Khondar Naomal." (names two rescuers; the quest files name three)
- E3. `campaign/guides/trollskull-manor/06-tavern-time.md:32`, `:90` and `sources/Appendix_D_-_Running_the_Tavern.md:1136`: roster rows (not stale; listed for the drafter).
- E4. `campaign/setting/deities/oghma.md:8`: "His faith reaches the campaign through Eiruk Weskur, a priest in Renaer Neverember's Black Tears" (names the Black Tears; not Elra).
- Not readable: none for Elra.

---

## F. Gaps a Background needs, and the sourced facts to stay consistent with

1. **Birth, age, childhood.** No source. The campaign calls her a half-elf mage (page L5). The wiki gives none (blank fields, D-list above).
2. **Family.** Wiki only: father "Malaerigo Harsard", guildmaster of the Cellarers' and Plumbers' Guild (dump line 1201644), and "feared her father's disapproval" (line 1201638). Use with `[research]`; the name is a wiki name, so ruling 17 allows it only with that tag.
3. **How she trained.** Wiki: "a [[human]] [[sorceress]] with minor [[magic]]al powers" (line 1201632). Campaign: "knows the wards" (page L21); "The ward on that door is Thayan work" (voice L169, a sample line).
4. **How she met Renaer and joined the Black Tears.** No source beyond the 1479 rescue (A2) and the Renaer's Friends rows (A3).
5. **Her dealings with Meloon.** The 1479 sewer errand: "with her hired bodyguard [[Meloon Wardragon]]" (dump line 1201641). The Meloon page says only "rescued Vajra alongside Renaer" (D4).
6. **The sewers.** Wiki: "she had detailed knowledge of the sewers and tunnels underneath [[Waterdeep]]" (dump line 1201644).
7. **Her goals.** Campaign: "pursue her own arcane studies" (L15). No source gives a specific study.
8. **Heir status.** D3: wiki only.

---

## G. Inner-life hints in the sources (exact quotes)

- "Laraelra was an idealist who cared deeply for Waterdeep and its inhabitants. She championed the causes of underdogs, including dwarves in the Cellarers' and Plumbers' guild who were discriminated against." (dump line 1201638)
- "Despite her independence, however, she was insecure and feared her father's disapproval." (dump line 1201638)
- "Deep down, she stays close to Renaer because she believes his father's enemies will come for him eventually, and she intends to be there when they do." (`08-laraelra-elra-harsard.md:21`)
- "Elra is the one who keeps them alive." (`08-laraelra-elra-harsard.md:25`)
- "Elra handles the threats they can see; Osco handles the ones they cannot." (`09-osco-salibuck.md:25`)
- "Ren, behind me. Everyone else, shut up and move." (voice L170; a sample line, not a fact)
