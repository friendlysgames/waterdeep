# Pass 6 research notes: Korgstrod Uxgulm

Page: `campaign/setting/notable-figures/xanathars-guild/10-korgstrod-uxgulm.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 16 and the Session 53 user rulings)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md`
Task extras (from the orchestrator): check the duergar's day-one posture against quest-time events (Faction Outposts, Xanathar's Lair), and the Xanathar's Guild outposts in `campaign/guides/factions/09-xanathars-guild.md`. Added as section G.

Method and caveats:
- **No wiki page exists for Korgstrod.** Checked three ways: (1) `scratchpad/wiki-xg/Korgstrod_Uxgulm.txt` reads `NOT FOUND`; (2) a Grep of `sources/research/` for `Korgstrod|Uxgulm` returns hits only in `campaign-hits.txt` and `adventure-hits.txt` bundles, never in a `wiki.txt`; (3) the Forgotten Realms dump (`scratchpad/fandom-dump/forgottenrealms_pages_current.xml`) has one hit, an index entry for "Clan Uxgulm" (section A1). The wiki therefore contributes only the Skullport infobox and the Thorvin page (sections A and G), both marked wiki-only.
- Campaign files: Read and Grep, quoted from the file.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. Tags such as `{@creature ...}` are left as written. JSON escapes (`\"`) are shown as plain quotes.
- Alexandrian PDFs: no shell in this session, so `pdftotext` could not run. I read the rendered page images with the Read tool's `pages` parameter. Every PDF quote is a transcription and needs a `pdftotext -layout` check before prose use. Read in full: `sources/11. Lair  Xanathar’s Lair.pdf` (all 9 pages), `sources/5. Faction Outposts.pdf` (PDF pp. 7 to 10, printed pp. 42 to 45), `sources/17. Outpost and Lair Revelation Lists.pdf` (PDF pp. 1 to 4, printed pp. 121 to 124). Appendix B and C were searched with Grep and have no Korgstrod hit.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written.

---

## A. Background facts by theme

The page has no published history. Almost every Background fact below comes from the campaign's own Guild pages or from the adventure's keyed area B8 and its "Stone of Deception" sidebar. Items the brief would need for a history are in section F.

### A1. Origin, family and clan

**No origin, birth, family or former life in any source.** One index hit only:

> "{{P|[[Clan Uxgulm]]|86}}"
> — `scratchpad/fandom-dump/forgottenrealms_pages_current.xml:3744432` (inside the Forgotten Realms Wiki page whose nearest `<title>` line is "Waterdeep: Dragon Heist" at line 3744214; the numbers are book page references, so `86` is Dragon Heist p.86, the Cellar Complex; wiki-only, 5e page reference inferred)

Context of the same index line: `;Clans: {{P|[[Clan Frostbeard|...` lists "Clan Steeltoes|34" (Ott's clan, see the Ott notes) and "Clan Ur'gray|66" (Noska's clan). The surname `Uxgulm` is therefore a clan name in the book index, but no text ties Korgstrod to the clan by name. `[research]`

### A2. Joining the Guild

**The campaign's general entry test (not Korgstrod-specific):**

> "- **Crime Is the Entry Fee:** Anyone can join, but an applicant must first pass a test that always involves a serious crime. The crime might be murdering a member who failed Xanathar, kidnapping a Waterdhavian, collecting a ransom or looting a warehouse. After that, advancement depends on wiles and on the ability to dispose of rivals, and the competition is fierce and often deadly."
> — `campaign/setting/organizations/08-xanathars-guild.md:32`

No source says when, how or why Korgstrod joined.

### A3. Rank and role

**Second response team leader (campaign, the Factions Guide mechanic):**

> "**Second Team — Korgstrod's Team.** Korgstrod Uxgulm leads three **duergar**, a **half-ogre**, and a **gazer**. The half-ogre carries the *Orb Confectioners' Note*: the passphrase to the sewer hideout ("Eight small eyes." / "Around an ocular cake.")."
> — `campaign/guides/factions/09-xanathars-guild.md:11`

> "Ott Steeltoes keeps Sylgar, and Gorath and Korgstrod Uxgulm lead duergar in the field (*Dragon Heist*, 5e; Notable Figures)."
> — `campaign/setting/organizations/08-xanathars-guild.md:43` (last sentence of the Structure paragraph; see section D5, the cited source does not say this)

> "- **Gorath** and **Korgstrod Uxgulm:** The leaders of the first and second response teams. The Guild sends them before it sends Noska."
> — `campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md:35`

**Not an "important underling" in the published adventure:**

> "{@creature Xanathar|WDH} relies on underlings for advice, information, and day-to-day oversight of the Xanathar Guild. The following important underlings are described in appendix B:"
> — `sources/adventure-wdh.json:15066`

The list that follows at `:15071`-`:15076` names Ahmaergo, Nar'l Xibrindas, Nihiloor, Noska Ur'gray, Ott Steeltoes and Thorvin Twinbeard. Korgstrod is not on it, and Gorath appears nowhere in the adventure.

**Rank ladder (Korgstrod not placed on it):**

> "The published ranks for members, from lowest to highest, are Eyestalker, Agent of the Eye, Eye Ray, Guild Boss and Hand of the Eye (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/08-xanathars-guild.md:45`

### A4. The post: Orb Confectioners cellar (Southern Ward)

**Adventure, the hideout and his seat (5e, Cellar Complex: Autumn, page 86):**

> "The characters have been encouraged to explore a Xanathar Guild hideout under the Southern Ward. They enter the location through {@area B1|1e2}. The Xanathar Guild Roster table provides a summary of the forces stationed throughout the complex. The sections that follow describe some of the hideout's features."
> — `sources/adventure-wdh.json:11960`

> "Korgstrod Uxgulm, the {@creature duergar} leader (40 hit points), seated in a stone chair and attended by 3 {@creature kobold||kobolds} (see \"Stone of Deception\" below)"
> — `sources/adventure-wdh.json:11987` (Xanathar Guild Roster table, Area B8; the table caption is at `:11963`)

**Campaign, the outpost:**

> "- **Orb Confectioners.** A sweets shop on Rising Ride in the Southern Ward that sells eye-shaped treats. Korgstrod Uxgulm runs a duergar operation in the cellar below it (**Southern Ward**; **Korgstrod Uxgulm**)."
> — `campaign/setting/organizations/08-xanathars-guild.md:57`

> "Orb Confectioners is a sweets shop specializing in eye-shaped treats: smallcakes, sweetmeats, sugar plates, candied nuts. Its cellar connects to a duergar operation run by Korgstrod Uxgulm. Use the Autumn version of the Cellar Complex (DH p. 86) for the layout."
> — `campaign/guides/factions/09-xanathars-guild.md:53`

> "A sweets shop that sells eye-shaped treats: smallcakes, sweetmeats, sugar plates and candied nuts. The Rising Ride is one of the streets that meet Caravan Court (wiki)."
> — `campaign/gazetteer/waterdeep/southern-ward.md:72`-`:73` (line 72 is the first sentence of the entry; the second sentence is at `:73`)

> "- **Korgstrod Uxgulm**, a duergar, runs the cellar operation beneath it for Xanathar's Guild and leads its second response team. A customer who asks for \"eight small eyes\" and answers \"Around an ocular cake\" earns an escort to the basement stairs."
> — `campaign/gazetteer/waterdeep/southern-ward.md:73`

**Alexandrian, the same outpost (printed p.44, PDF p.9; image transcription, check with pdftotext):**

> "XANATHAR SEWER HIDEOUT, TAKE 2: The Xanathar Guild maintains a number of sewer hideouts throughout Waterdeep. This one is a duergar operation run by Korgstrod Uxgulm. Use the Autumn version of the Cellar Complex (see Dragon Heist, p. 86)."
> — `sources/5. Faction Outposts.pdf`, printed p.44 [PDF p.9]

### A5. Relationships

**Ahmaergo (logistics; the outpost orders come from him):**

> "Ahmaergo handles logistics: gladiatorial procurement, outpost resupply, discipline. Most orders that bear Xanathar's name are written by Ahmaergo."
> — `campaign/setting/organizations/08-xanathars-guild.md:101`

> "**Area B7 – Mechanical Beholder**: Mixed in with the other material in this room is a letter." / "*On the Delivery of a Mechanical Beholder*: \"X is outraged that you bungling incompetents couldn't get his *piece de triomphe* working for the Shipwrights' Ball! ... See that it's delivered to Terasse's house of healing on Elsambul's Lane by the ninth of Tarsakh or be prepared to pay for it with your heads! - Ahmaergo\""
> — `sources/5. Faction Outposts.pdf`, printed p.44 [PDF p.9] (image transcription; the ellipsis is in the source transcript's own text and is not mine; check with pdftotext)

**Nar'l Xibrindas (a letter addressed to Korgstrod; quest-time discovery, but the letter's sender is a day-one relationship only if the drafter so decides):**

> "**Area B9b – Korgstrod's Room**: The chest at the foot of his bed is a **mimic**. The coffer in a secret compartment under the bed (DC 13 to find) contains 500 gp and *Correspondence with N'arl Xibrindas*."
> — `sources/5. Faction Outposts.pdf`, printed p.45 [PDF p.10] (image transcription)

> "\"Korgstrod—It is very important that this be kept in stricted confidence. Only you, me, and X know of the smokepowder. It must be brought to the Staircase of Eyes on the night of the 1st at precisely the stroke of eleven. Use disposable muscle. I will mark the sewer tunnels west of your hideout with a red eye to guide your men. – N'arl Xibrindas.\""
> — `sources/5. Faction Outposts.pdf`, printed p.45 [PDF p.10] (image transcription; "stricted" may be a transcription error for "strict"; no month is printed with "the 1st")

> "The smokepowder delivery referenced in the Korgstrod correspondence was his operation."
> — `campaign/setting/organizations/08-xanathars-guild.md:192` (Draft Notes, routed to the Factions Guide at `09-xanathars-guild.md:59`)

**Gorath (first team; campaign only):**

> "**First Team — Gorath's Team.** Gorath leads four **duergar**. He is sent when someone needs to be taught a lesson."
> — `campaign/guides/factions/09-xanathars-guild.md:9`

**Noska Ur'gray (third team; the Guild sends Korgstrod's team before Noska):**

> "Goblins and bugbears work for the Guild as muscle. Noska leads the third of its response teams, six bugbears and a gazer, and Xanathar sends him when it is done sending messages and wants the problem gone. The first two teams, led by Gorath and Korgstrod Uxgulm, are sent before his (**Xanathar's Guild**, Factions Guide)."
> — `campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md:22`

**Thorvin Twinbeard (the B7 guards and the B8 stairs; no source says Korgstrod commands the B7 guard):**

> "3 {@creature duergar} and 1 {@creature gazer|vgm} (see {@adventure appendix B|WDH|12}) standing guard while {@creature Thorvin Twinbeard|wdh} (see {@adventure appendix B|WDH|12}) works on a mechanical beholder (see \"Mechanical Beholder\" below)"
> — `sources/adventure-wdh.json:11983` (Xanathar Guild Roster table, Area B7)

> "In [[1492 DR]],{{WDH-time}} he was working on a mechanical [[beholder]] while three [[duergar]] and one [[gazer]] protected him.<ref name=\"WDH5e-p86\">{{Cite book/Waterdeep: Dragon Heist|86}}</ref> In truth, the gazer was spying on Thorvin under orders of the Xanathar, who suspected the dwarf.<ref name=\"WDH5e-p105\" />"
> — `scratchpad/wiki-xg/Thorvin_Twinbeard.txt:67` (wiki, cites Dragon Heist p.86, 5e; it names no duergar leader)

**Zhentarim envoys, Xanathar, the Guild as a whole:** no Korgstrod-specific line. The Guild page's general "Doubt Is Answered With Force" belief is in `campaign/setting/organizations/08-xanathars-guild.md:36` (not quoted here; it is not about him).

### A6. Faith

None. No source gives Korgstrod a deity, shrine or rite. The Guild page has no creed (`campaign/setting/organizations/08-xanathars-guild.md:39`, "Doctrine and Rites").

### A7. Signature belongings and posture

**The whip (adventure, 5e):**

> "Korgstrod plans to deliver the stone to {@creature Xanathar|WDH} in due time and won't willingly part with it before then. He uses a whip to flog his kobold lackeys and keep them in line. The cowardly kobolds flee into the sewers if Korgstrod is attacked and cower in his presence otherwise."
> — `sources/adventure-wdh.json:12016`

**The stone chair and the kobolds:** see A4 (`:11987`). The adventure gives three kobolds, not a retinue named by number elsewhere.

**The "Stone of Deception" sidebar (5e, page 86; the heading is at `sources/adventure-wdh.json:12011`).** Cut from the current page by user ruling (see D1):

> "Korgstrod Uxgulm, the duergar leader, has what he believes to be the {@item Stone of Golorr|WDH}. He found it during a search of Fenerus's house in the Trades Ward. This stone is a clever imitation. It's gray and ovoid with streaks of black, but has no magical powers. Korgstrod has been unable to attune to it and assumes he's unworthy of it, not that the stone is fake."
> — `sources/adventure-wdh.json:12015`

### A8. How long in post, and when he began

None in any source. The adventure gives no date. The wiki gives none. `[research]` for any tenure line.

### A9. Name and pronunciation

> "\"Korgstrod Uxgulm\", \"KORG-strawd UX-gulm\""
> — `sources/adventure-wdh.json:189`-`:190` (the pronunciation table row for Korgstrod, with `[` and `]` array brackets around the pair in the source)

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, current page: "*Duergar (second response team leader), lawful evil, he/him*. Stat block: **Duergar**." — `campaign/setting/notable-figures/xanathars-guild/10-korgstrod-uxgulm.md:5`
- Campaign, Guild page: "- **Korgstrod Uxgulm** — Duergar, lawful evil. Duergar leader of the sewer hideout beneath Orb Confectioners. See the **Korgstrod Uxgulm** page in Notable Figures." — `campaign/setting/organizations/08-xanathars-guild.md:109`
- Campaign, Guild Key Members (the 09 Factions Guide gives none): `campaign/setting/organizations/08-xanathars-guild.md:109` above is the only alignment line.
- Adventure: no alignment for Korgstrod. The adventure gives only "the {@creature duergar} leader" (`:11987`) and "the duergar leader" (`:12015`).
- Wiki: none.

**Species**
- Adventure: "Korgstrod Uxgulm, the {@creature duergar} leader (40 hit points)" — `sources/adventure-wdh.json:11987`; "Korgstrod Uxgulm, the duergar leader, has what he believes to be" — `sources/adventure-wdh.json:12015`
- Campaign: "Korgstrod Uxgulm — Duergar, lawful evil." — `campaign/setting/organizations/08-xanathars-guild.md:109`; "Korgstrod Uxgulm (**duergar**) + 4 **duergar**." — `campaign/guides/factions/09-xanathars-guild.md:61`
- Alexandrian: "This one is a duergar operation run by Korgstrod Uxgulm." — `sources/5. Faction Outposts.pdf`, printed p.44 [PDF p.9]
- No source says "shield dwarf" or "dwarf" for him. (Ott, Ahmaergo and Noska are "shield dwarf" in the adventure.)

**Pronouns**
- Adventure: "He found it during a search of Fenerus's house in the Trades Ward." — `sources/adventure-wdh.json:12015`; "He uses a whip to flog his kobold lackeys" — `sources/adventure-wdh.json:12016`. The "He" refers to Korgstrod.
- Campaign: "*Duergar (second response team leader), lawful evil, he/him*." — `campaign/setting/notable-figures/xanathars-guild/10-korgstrod-uxgulm.md:5`
- Pronoun table: "| Korgstrod Uxgulm | xanathars-guild/10-korgstrod-uxgulm.md:5 | he/him | prose (\"his brute authority\", \"he is the officer who runs\") | High |" — `docs/plans/npc-pronouns-table-group-c.md:35`

**Stat block**
- Campaign, current page: "Stat block: **Duergar**." — `campaign/setting/notable-figures/xanathars-guild/10-korgstrod-uxgulm.md:5`
- Campaign, Factions Guide: "Korgstrod Uxgulm (**duergar**) + 4 **duergar**." — `campaign/guides/factions/09-xanathars-guild.md:61`
- Alexandrian Lair, stat reference, printed p.91 [PDF p.9]: "Duergar – MM p. 122"
- Adventure: "40 hit points" — `sources/adventure-wdh.json:11987`. No source gives a duergar hit point total to compare against, and no source gives Korgstrod a separate stat block. `[research]`

---

## C. Every sentence on the current page that narrates a quest event, or a day-one claim that needs a check

Current page: `campaign/setting/notable-figures/xanathars-guild/10-korgstrod-uxgulm.md`. "Day-one OK" means no quest gate is needed. "Quest-time" means the sentence narrates or depends on a quest event. "Check" means no source is found.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Duergar (second response team leader), lawful evil, he/him*. Stat block: **Duergar**." | Day-one. The "second response team leader" role is a Factions Guide mechanic that deploys in quest time (see G) | `organizations/08-xanathars-guild.md:109`; `guides/factions/09-xanathars-guild.md:11` |
| 2 | L6 | "**Affiliation:** Xanathar's Guild" | Day-one OK | `organizations/08-xanathars-guild.md:109` |
| 3 | L7 | "**Featured in:** **Faction Outposts**, **Xanathar's Lair**" | Quest references. Faction Outposts: yes (`campaign/structure/arc-e-faction-outposts.md:179`, `:183`, `:187`). Xanathar's Lair: the Lair roster does not name Korgstrod (`sources/11. Lair  Xanathar’s Lair.pdf`, PDF pp. 7 and 8, printed pp. 89 and 90; see G3). Only the Notable Figures list names him (`campaign/structure/arc-f-xanathars-lair.md:339`) | `campaign/structure/arc-e-faction-outposts.md:179`; `campaign/structure/arc-f-xanathars-lair.md:339` |
| 4 | L11 | "**Resonance.** Korgstrod should inspire wariness with his brute authority, and dark humor with the way he treats his kobold lackeys." | Day-one OK. "the way he treats his kobold lackeys" matches the whip line | `sources/adventure-wdh.json:12016` |
| 5 | L13 | "**Emotions.** Korgstrod most often feels the duergar's characteristic contempt for weakness, frustrated pride in a subordinate operation that should have been simple, and physical pleasure in discipline." | Day-one reads as a standing mood. "a subordinate operation that should have been simple" implies a setback that no source gives. Check | none. "physical pleasure in discipline" has no source |
| 6 | L15 | "**Motivations.** Korgstrod wants to maintain discipline in the sewer hideout and earn Xanathar's favor by running the Orb Confectioners operation without trouble." | Day-one OK in intent. "earn Xanathar's favor" has no source. "without trouble" has no source | `sources/adventure-wdh.json:12016` (the whip and the kobolds); `organizations/08-xanathars-guild.md:57` (the operation) |
| 7 | L17 | "**Inspirations.** When playing Korgstrod, channel Vernon Dursley (*Harry Potter*, the authoritarian who does not understand what he controls), General Grievous (*Star Wars*, the brutal officer who treats his own troops as expendable), and any petty overseer who is certain that harsher discipline will fix whatever has gone wrong in the hideout." | Not a fact | n/a |
| 8 | L21 | "**Persona.** To the world, Korgstrod Uxgulm is a duergar in a stone chair attended by kobold lackeys who keep asking about a whip." | Stone chair and kobolds: day-one (`:11987`). "keep asking about a whip": no source. The adventure says the kobolds "flee" or "cower" (`:12016`) | `sources/adventure-wdh.json:11987`, `:12016` |
| 9 | L21 | "To those who deal with him, he is the officer who runs Xanathar's Orb Confectioners hideout and expects obedience." | Day-one OK. "expects obedience" has no source beyond the whip line | `organizations/08-xanathars-guild.md:57`; `guides/factions/09-xanathars-guild.md:53` |
| 10 | L23 | "**Morale.** In a fight, Korgstrod enlarges himself, presses forward, and uses his whip to position the kobolds he expects to die first. He does not retreat from his own hideout." | **Quest-time clause:** "enlarges himself" comes from the Faction Outposts response (`arc-e-faction-outposts.md:187`: "invisibility, enlargement, and four duergar fighting to the death"). "position the kobolds he expects to die first" and "does not retreat" have no source. The whip flogging is at `:12016` | `campaign/structure/arc-e-faction-outposts.md:187` |
| 11 | L25 | "**Relationships.** Korgstrod is the duergar leader of the Orb Confectioners sewer hideout, the second response team leader of Xanathar's Guild, and the commander of a kobold retinue whose continued employment is contingent on not being in his field of vision when things go wrong." | Hideout leader: day-one. "second response team leader": Factions Guide mechanic. "kobold retinue whose continued employment is contingent on not being in his field of vision when things go wrong": no source. The adventure says only that the kobolds "cower in his presence" (`:12016`) | `organizations/08-xanathars-guild.md:57`; `guides/factions/09-xanathars-guild.md:11`; `sources/adventure-wdh.json:12016` |
| 12 | L29 | "Korgstrod Uxgulm is a duergar who holds court in a stone chair attended by kobold lackeys, plainly expecting obedience and receiving it. He handles Guild business with blunt authority." | Stone chair and kobolds: day-one (`:11987`). "handles Guild business with blunt authority": no source beyond the Factions Guide role | `sources/adventure-wdh.json:11987` |

**Voice profile, quest-time and Stone clauses** (`.claude/skills/character-voices/voices/xanathars-guild.md:173`-`:187`). The profile's Stone lines describe the fake Stone that the user cut (D1). The drafter must restate or remove them (ruling 16):

> "*A pompous duergar boss convinced his own unworthiness is why the Stone won't work.*"
> — `.claude/skills/character-voices/voices/xanathars-guild.md:174`

> "- **Sentence shape:** Barked orders and self-important statements. There's a brooding, self-critical muttering whenever the Stone comes up."
> — `.claude/skills/character-voices/voices/xanathars-guild.md:177`

> "- **Word choice:** Military authority and duergar contempt: \"discipline\", \"unworthy\", \"weaklings\". He calls the kobolds \"vermin\" and the Stone \"the prize\"."
> — `.claude/skills/character-voices/voices/xanathars-guild.md:178`

> "- **Personality in speech:** Brute authority and thwarted ambition. The fake Stone's failure is his personal spiritual crisis, which he discusses earnestly."
> — `.claude/skills/character-voices/voices/xanathars-guild.md:180`

> "- **Quirks:** The kobolds keep asking about a whip, and he keeps shouting at them. He holds the Stone and concentrates visibly."
> — `.claude/skills/character-voices/voices/xanathars-guild.md:181`

> "- **Never:** He never suspects the Stone is fake, never shows weakness to subordinates, and never finds the whip."
> — `.claude/skills/character-voices/voices/xanathars-guild.md:183`

> "  - *Greeting:* \"Kneel before the keeper of the prize, surface-worms.\""
> — `.claude/skills/character-voices/voices/xanathars-guild.md:185`

> "  - *Business:* \"When I am worthy, the Stone will speak. Until then, it goes nowhere.\""
> — `.claude/skills/character-voices/voices/xanathars-guild.md:186`

Other voice lines with no source: "The kobolds keep asking about a whip" (`:181`), and the signature phrases "Discipline!" / "I am not yet worthy." / "Where is the whip?" (`:182`). The adventure has the whip (`:12016`) but no line about the kobolds asking for it.

---

## D. Conflicts

Rank used: campaign files first, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.

**D1. Does Korgstrod hold a Stone of Golorr? A fake one (adventure) against the campaign's Stone path (campaign ruling)**
- Adventure: "Korgstrod Uxgulm, the duergar leader, has what he believes to be the {@item Stone of Golorr|WDH}. He found it during a search of Fenerus's house in the Trades Ward. This stone is a clever imitation." — `sources/adventure-wdh.json:12015`
- Campaign, the Stone's path: "- **Ches 20:** Dalakhar steals it from Xanathar's lair on Neverember's orders." — `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:51` (and `:50`: "- **After the vote:** Neverember's spies take the Stone from the Palace and are killed leaving the city. It passes from hand to hand until it reaches Xanathar.")
- Campaign, Stone lore, the cut: "- **Settled, Korgstrod:** `notable-figures/xanathars-guild/10-korgstrod-uxgulm.md` had him holding a fake Stone (lines 12, 14, 16, 22 and 26), and no quest journal uses it. The user ruled that the Gralhund Villa journal governs the Stone, so the fake Stone is cut from his page." — `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:185`
- Campaign, the ruling: "18. **Korgstrod.** Cut the fake Stone from 10-korgstrod-uxgulm.md lines 16, 22, 26; the Gralhund Villa journal governs the Stone. Settle the Conflicts note in lore/stone-of-golorr-and-the-eyes.md." — `docs/plans/deities-user-rulings-brief.md:22`
- Session 51 handoff: "Korgstrod's fake Stone cut" — `session 51 handoff.md:24`
- Higher source: the campaign (user ruling). The current page has no Stone. The voice profile still carries Stone lines (section C). The Lair roster's Samara line says Xanathar holds the Stone on the Alexandrian's own timeline: "she believes that Xanathar holds the Stone of Golorr" (`sources/11. Lair  Xanathar’s Lair.pdf`, printed p.88 [PDF p.6]).

**D2. Where the fake came from: the adventure's Fenerus search (duergar in the Trades Ward) against the campaign's Fenerus and Trades Ward pages**
- Adventure, the duergar and the search: "Shortly after Fenerus's arrest, drow agents of Bregan D'aerthe showed up to collect the stone and were waylaid by {@condition invisible} duergar hiding in the alley. The duergar were members of the Xanathar Guild that had been sent by {@creature Nar'l Xibrindas|wdh} (see {@adventure appendix B|WDH|12}) to retrieve the stone. After searching Fenerus's home and finding nothing, they were waiting for Fenerus to return when the drow showed up. The drow barely got away with their lives." — `sources/adventure-wdh.json:7126`
- Adventure, the stone hidden: "Fenerus had the good sense to hide the {@item Stone of Golorr|WDH} elsewhere and hopes to use it as leverage to gain his freedom as well as forgiveness for past crimes." — `sources/adventure-wdh.json:7125`
- Campaign: "Settled by the user (Session 51): The Stone and Fenerus. He is not a Watch prisoner and did not hide the Stone before an arrest. `campaign/quests/act-ii/gralhund-villa/ev-08-the-rooftop-chase.md:67-68` has the Stone delivered to his house for Bregan D'aerthe, and that governs. His Notable Figures page now agrees." — `campaign/gazetteer/waterdeep/trades-ward.md:250`
- Campaign, the stone's route: "- **BD team:** The Stone reaches Fenerus Stormcastle. Jarlaxle holds it." — `campaign/quests/act-ii/gralhund-villa/ev-08-the-rooftop-chase.md:67`
- Higher source: the campaign. No campaign file has Guild duergar searching Fenerus's house, and the Trades Ward gazetteer has no "duergar" at all.

**D3. Who is Korgstrod's team and how many duergar: three or four (campaign, internal)**
- "**Second Team — Korgstrod's Team.** Korgstrod Uxgulm leads three **duergar**, a **half-ogre**, and a **gazer**." — `campaign/guides/factions/09-xanathars-guild.md:11`
- "***Roster.*** Korgstrod Uxgulm (**duergar**) + 4 **duergar**." — `campaign/guides/factions/09-xanathars-guild.md:61`
- The Alexandrian Outposts: "Korgstrod's response — invisibility, enlargement, and four duergar fighting to the death — signals this location is more important than the others." — `campaign/structure/arc-e-faction-outposts.md:187`
- Adventure, the B7 guards (not named as Korgstrod's): "3 {@creature duergar} and 1 {@creature gazer|vgm} ... standing guard" — `sources/adventure-wdh.json:11983`
- Notes file already flags it: "`guides/factions/09-xanathars-guild.md` gives Korgstrod's crew as three duergar in one place and four in another." — `docs/plans/harpers-out-of-scope-notes.md:301`
- Higher source: the Factions Guide governs the team (three duergar, half-ogre, gazer; the escalation "+ 4 duergar" is the outpost roster). The orchestrator decides the count. This is a count question, not a page fact.

**D4. Which team carries the passphrase note**
- Factions Guide: "The half-ogre carries the *Orb Confectioners' Note*: the passphrase to the sewer hideout" — `campaign/guides/factions/09-xanathars-guild.md:11`
- Alexandrian revelation list: "Orb Confectioners' Note (Response Team: Korgstrod Uxgulm)" — `sources/17. Outpost and Lair Revelation Lists.pdf`, printed p.123 [PDF p.3]
- Higher source: the campaign says the half-ogre carries it; the Alexandrian says the response team. Both are compatible with Korgstrod's team. The orchestrator decides which to write.

**D5. "Lead duergar in the field" against the adventure's underling list**
- Campaign, cited to Dragon Heist: "Ott Steeltoes keeps Sylgar, and Gorath and Korgstrod Uxgulm lead duergar in the field (*Dragon Heist*, 5e; Notable Figures)." — `campaign/setting/organizations/08-xanathars-guild.md:43`
- Adventure, the Dragon Heist list of important underlings: "{@creature Xanathar|WDH} relies on underlings for advice, information, and day-to-day oversight of the Xanathar Guild. The following important underlings are described in appendix B:" — `sources/adventure-wdh.json:15066`; the list at `:15071`-`:15076` omits Korgstrod and Gorath.
- Higher source: the adventure has no field-lead role for Korgstrod. The campaign's "lead duergar in the field" is a campaign inference cited to Dragon Heist. Treat as `[research]`, not as a Dragon Heist fact.

**D6. "Enlarges himself" in Morale (campaign, quest-time) against the adventure (no enlargement)**
- Current page: "In a fight, Korgstrod enlarges himself, presses forward, and uses his whip to position the kobolds he expects to die first." — `campaign/setting/notable-figures/xanathars-guild/10-korgstrod-uxgulm.md:23`
- The only source for enlargement is the Outposts response: "Korgstrod's response — invisibility, enlargement, and four duergar fighting to the death" — `campaign/structure/arc-e-faction-outposts.md:187`
- Adventure: the roster gives only "(40 hit points), seated in a stone chair" (`sources/adventure-wdh.json:11987`). No ability is given.
- Higher source: the adventure has no ability; the Outposts doc has the response. Quest-time (see G).

**D7. The B8 seat against the Alexandrian's B8 (stairs removed)**
- Adventure, B8 is Korgstrod's seat and has stairs: "Korgstrod Uxgulm, the {@creature duergar} leader (40 hit points), seated in a stone chair ..." (`sources/adventure-wdh.json:11987`); "If combat breaks out in the cellar complex, {@creature Thorvin Twinbeard|wdh} flees up the stairs in {@area B8|1ea} and uses a key to unlock the door leading outside." (`sources/adventure-wdh.json:12006`)
- Alexandrian: "Area B8: Remove the stairs up." — `sources/5. Faction Outposts.pdf`, printed p.44 [PDF p.9]
- Appendix C, the quest route: "through Area B8 which has been cleared of its staircase — the party must find another way through." — `sources/Appendix_C_-_Player_Faction_Missions.md:1875`
- Higher source: the adventure gives the seat and the stairs; the Alexandrian and Appendix C remove the stairs (a quest-time layout change). The campaign's Factions Guide does not mention B8 for Korgstrod. Not resolved in the campaign.

**D8. Where the sewer hideout lies: Southern Ward (Korgstrod) against the Dock Ward (Finding Floon)**
- Campaign, Southern Ward: "- **Orb Confectioners.** A sweets shop on Rising Ride in the Southern Ward ..." — `campaign/setting/organizations/08-xanathars-guild.md:57`
- Campaign, Dock Ward: "The sewers beneath the Dock Ward lead to a Xanathar's Guild hideout carved into a decommissioned vault." — `campaign/quests/act-i/finding-floon/ev-04-xanathar-sewer-hideout.md:122`
- Campaign, the Dock Ward gazetteer: "**Xanathar Sewer Hideout** — Guild hideout beneath the ward" — `campaign/gazetteer/waterdeep/dock-ward.md:107`
- Campaign, the Guild page's own conflict note, citing `finding-floon/ev-04-xanathar-sewer-hideout.md:133` (that line number is stale; the sentence is at `:122`): "`dock-ward.md:107-108` and `finding-floon/ev-04-xanathar-sewer-hideout.md:133` put the mapped hideout below the Dock Ward, and *Dragon Heist* puts a Guild hideout below the Southern Ward (`adventure-wdh.json:11960`; `dock-ward.md:296` logs it as unresolved)." — `campaign/setting/organizations/08-xanathars-guild.md:185`
- Adventure: "The characters have been encouraged to explore a Xanathar Guild hideout under the Southern Ward." — `sources/adventure-wdh.json:11960`
- Gazetteer log: "`finding-floon/ev-04-xanathar-sewer-hideout.md:133` and `overview.md:55` put the hideout beneath the Dock Ward, and Dragon Heist's Cellar Complex text puts a Guild hideout under the Southern Ward (`:11960`). Unresolved." — `docs/plans/...` (see `campaign/gazetteer/waterdeep/...`; the log is `dock-ward.md:296`, which the Guild page cites)
- Higher source: the campaign page keeps Korgstrod in the Southern Ward and the Dock Ward hideout for the Finding Floon quest. Unresolved: whether the Orb cellar and the Dock Ward hideout are one complex.

**D9. Pronunciation and spelling**
- Alexandrian: "Korgstrod" throughout; adventure pronunciation: "KORG-strawd UX-gulm" (`sources/adventure-wdh.json:190`). No conflict.

**D10. Ahmaergo's species in an appendix (not Korgstrod; cross-reference only)**
- "2 = Ahmaergo (duergar; inspection; DC 15 Deception to pass as authorized)" — `sources/Appendix_C_-_Player_Faction_Missions.md:1887`
- Adventure: Ahmaergo is a shield dwarf; the Ahmaergo research notes record this (`campaign/setting/notable-figures/xanathars-guild/02-ahmaergo.md:124`).

**D11. Which Guild agent carries the Report to Agorn Fuoco (cross-reference on the Orb outpost)**
- Factions Guide: "- *Report to Agorn Fuoco* (Response Team: Agorn Fuoco — names Orb Confectioners on Rising Ride)" — `campaign/guides/factions/09-xanathars-guild.md:95`
- Alexandrian revelation list: "Report to Agorn Fuoco (Response Team: Vevette Blackwater)" — `sources/17. Outpost and Lair Revelation Lists.pdf`, printed p.123 [PDF p.3]
- Higher source: the campaign's Factions Guide is the mechanic. This is not a Korgstrod fact; listed because the Orb Confectioners outpost depends on it.

---

## E. Stale lines in other files (not edited), and routed references

### E1. Setting pages that name quest events (routing only; do not edit)
- `campaign/gazetteer/waterdeep/southern-ward.md:74`: "- Hook: **Faction Outposts** treats it as an encounter-plus outpost. A letter there threatens the mechanical beholder's delivery to Terasse Estate, and correspondence with Nar'l Xibrindas gives guildsigns that lead toward **Xanathar's Lair**." (a quest reference on a setting page; the setting rule bars it)
- `campaign/setting/organizations/08-xanathars-guild.md:43`: "Korgstrod Uxgulm lead duergar in the field (*Dragon Heist*, 5e; Notable Figures)." (cited to Dragon Heist; see D5)
- `campaign/setting/organizations/08-xanathars-guild.md:192`: "- **Routed to quests (ruling 28):** Key Members, Nar'l: \"The smokepowder delivery referenced in the Korgstrod correspondence was his operation.\" Lives in the Factions Guide (`09-xanathars-guild.md:59`, Area B9b)."
- `campaign/setting/history/02-the-long-shadow.md:161` (Draft Notes): "The response teams (Gorath, Korgstrod Uxgulm, Noska Ur'gray) belong on the **Xanathar's Guild** page in the Factions Guide, where they already sit."

### E2. Bundle copies (snapshots; not edited)
- `sources/research/pass3-bundles/stone-of-golorr-and-the-eyes/campaign-hits.txt:167`: "Motivations. Korgstrod wants to deliver the Stone of Golorr to Xanathar and receive the credit, maintain discipline in the sewer hideout, and figure out why he cannot attune to the stone (the answer is that it is a fake, but this has not occurred to him)." (the old page; current L15 has no Stone)
- `sources/research/pass3-bundles/stone-of-golorr-and-the-eyes/campaign-hits.txt:169`: "**Relationships.** Korgstrod is the duergar leader of the Orb Confectioners sewer hideout, the second response team leader of Xanathar's Guild, the holder of a convincing fake Stone of Golorr, and the commander of a kobold retinue ..." (the old page, before the cut)

### E3. Routed to quests (where the quest-time facts already live)
- Terasse Estate and Orb Confectioners escalation: "If a second Xanathar outpost has already been hit, it moves directly to Alert (Tier 3), and Gorath's team deploys within 2 days to the last known party location." — `campaign/guides/factions/09-xanathars-guild.md:35` (Terasse); the Orb outpost: "***Escalation.*** Xanathar moves to Alert (Tier 3). Korgstrod's response team deploys within 3 days of the operation. **Founders' Day Clock: 1–3 days.**" — `campaign/guides/factions/09-xanathars-guild.md:63`
- Faction Outposts, the Orb outpost: `campaign/structure/arc-e-faction-outposts.md:175`-`:187` (Scene 4C); Escalation at `:187`, Area B9b at `:183`.
- Lords' Alliance Warduke (Korgstrod's team in a rank event): "| Xanathar's Guild | Second | A leader, three fighters from underground stock, a half-ogre and a floating one-eyed creature | Korgstrod Uxgulm's team |" — `campaign/quests/faction-events/lords-alliance/r25-warduke/ev-01-warduke.md:194`
- Doom Raiders r03 Wolf: "> - **Xanathar's Guild:** Gorath with four duergar, then Korgstrod Uxgulm with a half-ogre and a gazer, then Noska Ur'gray with six bugbears and a gazer." — `campaign/quests/faction-events/doom-raiders/r03-wolf/ev-01-wolf.md:125`
- Bregan D'aerthe r03 Soldier: "> - **Korgstrod's team:** \"Next up is Korgstrod Uxgulm with three duergar, a half-ogre and a gazer, and they hit a lot harder than Gorath's lot.\"" — `campaign/quests/faction-events/bregan-daerthe/r03-soldier/ev-01-soldier.md:147`
- Trollskull Manor response teams (guide, Acts I to II; quest-time visits): "**Who comes:** Gorath (four duergar in unremarkable clothes). If Gorath is neutralized: Korgstrod Uxgulm's team (half-ogre + cloaked gazer). Noska Ur'gray does not visit — he arrives with intent." — `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:19`; "**What the party can do:** Negotiate, return goods (if goods rather than information), or prepare for Korgstrod's team." — `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:30`
- Appendix D (Running the Tavern), the same visit: "If Gorath has already been neutralized, Korgstrod Uxgulm's team is next — with a half-ogre who takes up too much space and a gazer floating at belt height under a heavy cloak." — `sources/Appendix_D_-_Running_the_Tavern.md:1517`
- Alexandrian revelation list, the Orb outpost: "XANATHAR SEWER HIDEOUT, TAKE 2 / Orb Confectioners' Note (Response Team: Korgstrod Uxgulm)" — `sources/17. Outpost and Lair Revelation Lists.pdf`, printed p.123 [PDF p.3]
- Smokepowder, Nar'l's letter: the correspondence's guildsign trail "requires DC 15 checks to follow" — `sources/5. Faction Outposts.pdf`, printed p.45 [PDF p.10] (GM Note)

### E4. Day-one and cross-reference lines (keep them)
- Eye placement and the Stone on Ches 1 (Xanathar holds the Stone): "- **The Eye in the bowl:**" lines are about Xanathar, not Korgstrod; see `campaign/setting/organizations/08-xanathars-guild.md:125`. For the Stone's day-one holder: "- **Ches 20:** Dalakhar steals it from Xanathar's lair on Neverember's orders." — `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:51`.
- Zemk, the duergar in the Finding Floon hideout (Q05; Dock Ward): "Q05: Zemk (duergar, CR 1). Hostile to the party." — `campaign/locations/xanathar-sewer-hideout/area-overview.md:51` (the full line is "**Q05:** Zemk (duergar, CR 1). Hostile to the party. Krentz (bandit, CR 1/8) present if he survived ev-01; his reaction depends on how the party treated him at the Yawning Portal."). Adventure: "a hostile member of the Xanathar Guild, a {@creature duergar} named Zemk." — `sources/adventure-wdh.json:2784`
- Alexandrian Lair, the stone's owner on the title page: "Xanathar stole the *Stone of Golorr* from Lord Neverember and he stole one of the three Eyes from the Zhentarim. Then he lost the *Stone* when Dalakhar took it from him." — `sources/11. Lair  Xanathar’s Lair.pdf`, printed p.83 [PDF p.1] (title page; italics as in the transcription)

### E5. Source guide
- `sources/SOURCE_GUIDE.md:83` lists the dungeon level: "| 1 | Dungeon Level | Goblins, duergar, connections to the city above | Secondary — physical connection to Xanathar lair |" (a general reference; not Korgstrod).

---

## F. Gaps (what a Background would need that no source gives), with suggested modest inferences

Every suggestion below is a `[research]` inference. None is an invented plot fact. The drafter must tag each one.

1. **Birth, family, early life, former life.** No source. The only hit is the index entry "Clan Uxgulm" (`scratchpad/fandom-dump/forgottenrealms_pages_current.xml:3744432`). *Suggested inference:* "[research] Korgstrod's family name is Uxgulm, a clan the Dragon Heist index lists on the Cellar Complex page." The index does not say that Korgstrod is a member of the clan.
2. **When and how he joined the Guild, and how he came to run the cellar.** No source. *Suggested inference:* "[research] Korgstrod passed the Guild's general entry test (`organizations/08-xanathars-guild.md:32`) and was given the Orb Confectioners cellar as his post." The test is general and not dated.
3. **Length of service in the post.** No source. *Suggested inference:* none beyond "he has run the cellar for some time". Do not give a year.
4. **Who gives him orders.** Ahmaergo handles outpost resupply (`organizations/08-xanathars-guild.md:101`), and the B7 letter is from Ahmaergo (Alexandrian p.44). Nar'l's letter is addressed to him (Alexandrian p.45). *Suggested inference:* "[research] Korgstrod takes logistics orders from Ahmaergo and smokepowder orders from Nar'l Xibrindas." Both facts exist; the link is the inference.
5. **Relationship to Gorath.** Only "Gorath and Korgstrod Uxgulm lead duergar in the field" (`organizations/08-xanathars-guild.md:43`), and the response order (`05-noska-urgray.md:35`). *Suggested inference:* "[research] Two duergar leaders serve under Xanathar's Guild in separate teams; no source records a rivalry or a friendship."
6. **Relationship to Noska and Xanathar.** Noska's team comes third (`05-noska-urgray.md:22`). No source records a Korgstrod–Noska tie. *Suggested inference:* none. Say only the response order.
7. **The Stone.** No campaign source gives Korgstrod any Stone. The adventure's fake Stone is cut (D1). Do not write a Stone for him.
8. **How the Guild's duergar got into Fenerus's house.** Adventure only (`sources/adventure-wdh.json:7126`), and the campaign contradicts the search (D2). Do not use.
9. **The smokepowder letter's date.** The letter says "on the night of the 1st" with no month (Alexandrian p.45). The Factions Guide gives no date. *Suggested inference:* none; leave the date out of the Background.
10. **Stat block and abilities.** Only "40 hit points" (`:11987`) and "duergar" (campaign). The enlargement and invisibility in the Outposts response (`arc-e-faction-outposts.md:187`) are quest-time, not day-one. *Suggested inference:* keep "Duergar" as the stat block label; give no ability on day one.
11. **Whip and kobolds.** The whip and the cowering kobolds are in the adventure (`:12016`). "The kobolds keep asking about a whip" (voice profile, `:181`) has no source. *Suggested inference:* keep the whip and the cowering kobolds; mark the "asking about a whip" line `[research]` or cut it.
12. **Kobold retinue size and terms of service.** The adventure gives three kobolds (`:11987`). "Continued employment ... contingent on not being in his field of vision" has no source. *Suggested inference:* keep "three kobolds"; cut the employment clause or tag it `[research]`.
13. **Faith.** No deity or rite for Korgstrod in any source. The Guild has no creed (`organizations/08-xanathars-guild.md:39`). Leave blank.
14. **Appearance.** Only "a stone chair" (`:11987`). No other physical description. Leave blank.
15. **Age.** None.
16. **Whether B7's duergar are his men.** The adventure has "3 duergar and 1 gazer standing guard while Thorvin ... works on a mechanical beholder" (`:11983`) with no leader named. The Factions Guide gives his team three duergar (`09-xanathars-guild.md:11`). *Suggested inference:* "[research] The B7 duergar are Guild guards; the source does not say they answer to Korgstrod."
17. **Whether the Orb cellar and the Dock Ward hideout are one complex.** Unresolved (D8). Do not merge them on the page.
18. **Whether he is among the "Dwarves (mostly duergar)" in Skullport.** The wiki's Skullport infobox gives "{{Numeric table|...|[[Dwarves]] (mostly [[duergar]])|68|...}}" (`sources/research/pass5-bundles/xanathars-guild/wiki.txt:256`, Skullport page, wiki-only, no edition printed). No line ties him to it. Do not use.
19. **Pronouns.** Sourced (he/him). No gap.
20. **Pronunciation.** Sourced (`sources/adventure-wdh.json:190`).

---

## G. Duergar posture: day one against quest time

The caller asked for this. Each line states whether it is day-one (Ches 1, 1492 DR) or quest-time, with the file.

**G1. Day-one posture of the duergar in the Guild (campaign and adventure)**
- Duergar run the Southern Ward cellar under Orb Confectioners, under Korgstrod: "Korgstrod Uxgulm runs a duergar operation in the cellar below it" (`campaign/setting/organizations/08-xanathars-guild.md:57`); "- **Korgstrod Uxgulm**, a duergar, runs the cellar operation beneath it for Xanathar's Guild" (`campaign/gazetteer/waterdeep/southern-ward.md:73`). Adventure, the cellar complex (5e): "The characters have been encouraged to explore a Xanathar Guild hideout under the Southern Ward." (`sources/adventure-wdh.json:11960`)
- Duergar guard the B7 mechanical beholder with Thorvin (adventure, day-one state): "3 {@creature duergar} and 1 {@creature gazer|vgm} ... standing guard while ... Thorvin Twinbeard ... works on a mechanical beholder" (`sources/adventure-wdh.json:11983`). Wiki says "In [[1492 DR]]," (`scratchpad/wiki-xg/Thorvin_Twinbeard.txt:67`, wiki-only).
- A Guild duergar in the Dock Ward hideout (Finding Floon; the hideout is a day-one location and the party meets him there in the quest): "Q05: Zemk (duergar, CR 1). Hostile to the party." (`campaign/locations/xanathar-sewer-hideout/area-overview.md:51`); adventure: "a hostile member of the Xanathar Guild, a {@creature duergar} named Zemk." (`sources/adventure-wdh.json:2784`).
- The Guild's duergar in the Trades Ward (the adventure's Fenerus search): quest-time-only in the adventure's timeline ("Shortly after Fenerus's arrest"), contradicted by the campaign (D2).

**G2. Quest-time posture: the response teams (campaign mechanics, deploy when the Guild reaches Alert or Suspicious)**
- Gorath's first team (four duergar, Suspicious and above): "Suspicious | Gazer scouts; Nihiloor processes captured intelligence. First team (Gorath's duergar) deployed as a warning" (`campaign/guides/factions/09-xanathars-guild.md:72`).
- Korgstrod's second team (Alert): "| Alert | Second team (Korgstrod's heavy team: half-ogre + gazer) deployed |" (`campaign/guides/factions/09-xanathars-guild.md:73`). The Guild's own escalation table (campaign, GM Guide): "| **Xanathar's Guild** | Normal operations | ... | Second team: Korgstrod Uxgulm's squad (half-ogre + gazer) | Third team: Noska Ur'gray's bugbear squad with orders to eliminate. ..." (`campaign/guides/gm-guide/running-the-villains.md:49`)
- Korgstrod's team in the outpost (Faction Outposts, Scene 4C, quest-time): "Escalation: Xanathar moves to Alert (Tier 3) if this outpost is cleared. Korgstrod's response — invisibility, enlargement, and four duergar fighting to the death — signals this location is more important than the others. Response teams deploy within 1d4 days of the operation." (`campaign/structure/arc-e-faction-outposts.md:187`). Factions Guide version: "Korgstrod's response team deploys within 3 days of the operation." (`campaign/guides/factions/09-xanathars-guild.md:63`). The two disagree on timing (1d4 days against 3 days). Campaign state: the Factions Guide mechanic is the written one, and the Outposts doc is the structuring draft. The orchestrator decides.
- Terasse Estate (Faction Outposts, Scene 4A, quest-time): "If a second Xanathar outpost has already been hit, it moves directly to Alert (Tier 3), and Gorath's team deploys within 2 days to the last known party location." (`campaign/guides/factions/09-xanathars-guild.md:35`)

**G3. Quest-time posture: Xanathar's Lair (Alexandrian, not the campaign page)**
- Korgstrod is not in the Lair roster. The Lair's Standard Adventure Roster, public area list and Tournament roster name no Korgstrod (`sources/11. Lair  Xanathar’s Lair.pdf`, printed pp. 89 and 90 [PDF pp. 7 and 8]).
- Duergar in the Lair appear only as "2 duergar" in the public audience (printed p.89, PDF p.7): "- 10 bandits • 2 duergar" (the public audience list; the transcription lists them as bullets, "10 bandits" and "2 duergar").
- Duergar stat reference: "Duergar – MM p. 122" (printed p.91, PDF p.9).
- Campaign: the Lair structure doc names Korgstrod only in its Notable Figures list (`campaign/structure/arc-f-xanathars-lair.md:339`). It has no "duergar" line and no Korgstrod roster line.
- Campaign's Lair entry route through the Orb cellar, quest-time: "Use the Autumn Cellar Complex layout (DH p. 86)." (`campaign/structure/arc-e-faction-outposts.md:181`); the Lair route depends on the Orb documents: "Melannor's environmental intelligence from Scene 1 can substitute for the guildsign trail if the Orb Confectioners documents weren't recovered." (`campaign/structure/arc-f-xanathars-lair.md:65`)

**G4. Quest-time posture: Korgstrod's team in other quest events**
- Lords' Alliance Warduke: `campaign/quests/faction-events/lords-alliance/r25-warduke/ev-01-warduke.md:194` (Second team, Korgstrod's team).
- Doom Raiders Wolf: `campaign/quests/faction-events/doom-raiders/r03-wolf/ev-01-wolf.md:125` (Korgstrod with a half-ogre and a gazer, after Gorath).
- Bregan D'aerthe Soldier: `campaign/quests/faction-events/bregan-daerthe/r03-soldier/ev-01-soldier.md:147` (Korgstrod's team as the next visit).

**G5. Day-one against quest time, for the page's own lines**
- Day-one: the cellar (`:57`), the stone chair and kobolds (`:11987`), the whip (`:12016`), the Southern Ward (`:73`).
- Quest-time or quest-derived: "enlarges himself" (arc-e `:187`), the response team (`09-xanathars-guild.md:11`, `:63`), "Korgstrod's team" in rank events (G4), the Factions Guide Escalation (G2), and the Morale's "position the kobolds he expects to die first" (no source at all).

---

## Not readable

- None of the sources failed to open. The three PDFs with Korgstrod content were read as rendered images (no `pdftotext` in this session). Their quotes are transcriptions, marked "image transcription" above. Check each with `pdftotext -layout` before any prose use. The transcription of "stricted" in the Nar'l letter (printed p.45) is the one most in doubt.
- `sources/Other remix files/*.docx` were not searched. `SOURCE_GUIDE.md` does not list one for Korgstrod.
- The Forgotten Realms dump was searched by Grep only; the one Korgstrod hit is the index line in section A1. The dump has no Korgstrod page.

## Not run

- `voicecheck.py` was not run (research only).
- The page was not written. No file was edited except this notes file.
