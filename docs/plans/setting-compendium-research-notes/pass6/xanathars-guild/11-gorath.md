# Pass 6 research notes: Gorath

Page: `campaign/setting/notable-figures/xanathars-guild/11-gorath.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Instructions: `scratchpad/pass6-researcher-instructions.md`
Ruling used: Ches 1, 1492 DR is the day-one state. Quest-time sentences are listed in section C with the file where they already live.

Method and caveats:
- Campaign files: Read and Grep, quoted from the file. Line numbers are from tool output.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes (`\"`) are shown as plain quotes. `{@creature ...}` tags are left as written.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. Every PDF quote below was transcribed from the rendered page image. Each is marked **[PDF image]** and needs a `pdftotext -layout` check before any prose use. Cite as printed page with PDF page in brackets.
- Appendices: `sources/Appendix_C_-_Player_Faction_Missions.md` and `sources/Appendix_D_-_Running_the_Tavern.md` are markdown and were read as text.
- Wiki: `scratchpad/wiki-xg/Gorath.txt`. **This is a different figure** (a Kara-Tur spirit). It is quoted in section D only so the drafter does not import it. `Gorathil.txt` is not in the `wiki-xg/` folder, so it was not searched.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written.

---

## Summary

1. **Gorath is named only in campaign files and the Alexandrian remix.** He does not appear in `sources/adventure-wdh.json` at all, and the adventure's list of the Guild's "important underlings" leaves him out (see A3).
2. **Who he is (day one):** the first of the Guild's three response-team leaders. The Factions Guide says "Gorath leads four **duergar**" (`campaign/guides/factions/09-xanathars-guild.md:9`). The Alexandrian remix says "Gorath is the leader of a small team of duergar" (**[PDF image]** `sources/6. Faction Response Teams.pdf`, printed p.54 [PDF p.6]).
3. **What he commands (day one):** a team of four duergar, sent "when someone needs to be taught a lesson" (same two sources). Korgstrod Uxgulm's team is second and Noska Ur'gray's is third.
4. **No Gorath-specific source** gives his species, his stat block, his alignment, his birth, his background, his faith, his belongings or his time in post. The campaign states "Duergar, lawful evil" for him on the Guild page and on his own page, with no source behind it (see B).
5. **Quest state, to route:** the party-triggered tavern visits (Trollskull Manor guide and Appendix D), the escalation paragraphs (Factions Guide and `arc-e`), the structure-doc Notable Figures list (`arc-f`), and the Guild's Terasse escalation. See C and E.
6. **Conflicts to decide:** the Factions Guide escalation paragraph and the Factions Guide tier table disagree on which tier sends Gorath (D5). The voice profile says he "never threatens directly" while the sourced ultimatum is an ultimatum (D7). The Guild page cites *Dragon Heist* for Gorath, and the adventure does not name him (D6).

---

## A. Background facts by theme

### A1. Origin, family, former life
No source gives any. Searched: the target page, the Guild organization page, all `campaign/setting/notable-figures/xanathars-guild/` pages, `campaign/setting/history/`, `campaign/setting/lore/`, `sources/adventure-wdh.json` (no hits for Gorath), `Appendix_B`, `Appendix_C`, `Act_III_Arc_D.md`, `Act_III_Arc_E.md`, the wiki pages in `wiki-xg/` (only `Gorath.txt` names Gorath, and it is the other figure). See F1.

### A2. How he joined and rose in the Guild
Team role, the only rise-related statement for him:
> "**First Team — Gorath's Team.** Gorath leads four **duergar**. He is sent when someone needs to be taught a lesson."
> — `campaign/guides/factions/09-xanathars-guild.md:9`

> "GORATH: Gorath is the leader of a small team of duergar. His team is sent in one when someone needs to be taught a lesson."
> — **[PDF image]** `sources/6. Faction Response Teams.pdf`, printed p.54 [PDF p.6], "Xanathar Response Teams"

The general entry test, which the page does not apply to Gorath. The campaign says nothing Gorath-specific:
> "- **Crime Is the Entry Fee:** Anyone can join, but an applicant must first pass a test that always involves a serious crime. The crime might be murdering a member who failed Xanathar, kidnapping a Waterdhavian, collecting a ransom or looting a warehouse. After that, advancement depends on wiles and on the ability to dispose of rivals, and the competition is fierce and often deadly."
> — `campaign/setting/organizations/08-xanathars-guild.md:32`

### A3. Rank and place among the Guild's figures
The ladder is in the Guild page. Gorath is not placed on it:
> "The published ranks for members, from lowest to highest, are Eyestalker, Agent of the Eye, Eye Ray, Guild Boss and Hand of the Eye (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/08-xanathars-guild.md:45`

The Guild page places the response teams, not ranks:
> "Ott Steeltoes keeps Sylgar, and Gorath and Korgstrod Uxgulm lead duergar in the field (*Dragon Heist*, 5e; Notable Figures)."
> — `campaign/setting/organizations/08-xanathars-guild.md:43` (see D6 on the citation)

The published adventure's list of the Guild's important underlings does not include him (the list is the full set of underlings the adventure names):
> "{@creature Xanathar|WDH} relies on underlings for advice, information, and day-to-day oversight of the Xanathar Guild. The following important underlings are described in appendix B:"
> — `sources/adventure-wdh.json:15066`

> "{@creature Ahmaergo|WDH}, dwarf majordomo",
> "{@creature Nar'l Xibrindas|wdh}, drow advisor",
> "{@creature Nihiloor|WDH}, {@creature mind flayer}",
> "{@creature Noska Ur'gray|wdh}, dwarf enforcer",
> "{@creature Ott Steeltoes|wdh}, dwarf fishkeeper",
> "{@creature Thorvin Twinbeard|wdh}, dwarf engineer"
> — `sources/adventure-wdh.json:15071`-`:15076`

### A4. Relationships to named figures

**Korgstrod Uxgulm (the second team, sent after Gorath).**
> "**Second Team — Korgstrod's Team.** Korgstrod Uxgulm leads three **duergar**, a **half-ogre**, and a **gazer**. The half-ogre carries the *Orb Confectioners' Note*: the passphrase to the sewer hideout ("Eight small eyes." / "Around an ocular cake.")."
> — `campaign/guides/factions/09-xanathars-guild.md:11`

> "KORGSTROD UXGULM: If Gorath is taken out, Korgstrod is sent out from the Xanathar Sewer Hideout (see Outposts) to send a stronger message."
> — **[PDF image]** `sources/6. Faction Response Teams.pdf`, printed p.54 [PDF p.6]

> "The first two teams, led by Gorath and Korgstrod Uxgulm, are sent before his (**Xanathar's Guild**, Factions Guide)."
> — `campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md:22`

> "- **Gorath** and **Korgstrod Uxgulm:** The leaders of the first and second response teams. The Guild sends them before it sends Noska."
> — `campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md:35`

> "**Relationships.** Korgstrod is the duergar leader of the Orb Confectioners sewer hideout, the second response team leader of Xanathar's Guild, and the commander of a kobold retinue whose continued employment is contingent on not being in his field of vision when things go wrong."
> — `campaign/setting/notable-figures/xanathars-guild/10-korgstrod-uxgulm.md:25`

**Noska Ur'gray (the third team, sent after Korgstrod).**
> "**Third Team — Noska's Team.** Noska Ur'gray leads six **bugbears** and a **gazer**. He is sent when Xanathar is done sending messages and wants the problem gone."
> — `campaign/guides/factions/09-xanathars-guild.md:13`

> "Xanathar charms and bullies its minions and puts its symbol on doors, tattoos and chalk marks so that no one forgets whose ground they stand on (*Dragon Heist*, 5e; **Dock Ward**). The Guild warns before it kills. Gorath delivers a message once and leaves, and Noska is sent when Xanathar is done sending messages (**Gorath**; **Noska Ur'gray**)."
> — `campaign/setting/organizations/08-xanathars-guild.md:77`

> "NOSKA UR'GRAY: Noska, a shield dwarf, is another of Xanathar's enforcers."
> — **[PDF image]** `sources/6. Faction Response Teams.pdf`, printed p.54 [PDF p.6]

**Nar'l Xibrindas (the directive the first or second team carries; not a personal tie).**
> "The first or second team the party encounters carries *A Directive from Nar'l Xibrindas*, instructing the team leader to resupply at Grinda Garloth's."
> — `campaign/guides/factions/09-xanathars-guild.md:7`

> "A DIRECTIVE FROM N'ARL XIBRINDAS: The first or second Xanathar response team the PCs encounter should carry A Directive From N'arl Xibrindas, instructing the leader of the response team to get "properly outfitted" by Grinda Garloth."
> — **[PDF image]** `sources/6. Faction Response Teams.pdf`, printed p.54 [PDF p.6] (the same PDF page continues with the potion and +1 weapon line; see A6)

**Grinda Garloth (the team is outfitted by her).**
> "This team has a potion of healing, potion of greater healing, and a +1 weapon. (They were, in fact, outfitted by Grinda.)"
> — **[PDF image]** `sources/6. Faction Response Teams.pdf`, printed p.54 [PDF p.6]

**Ahmaergo, Xanathar, Nihiloor.** No source names a personal tie between Gorath and any of them. Searched: all Guild Notable Figures pages (`campaign/setting/notable-figures/xanathars-guild/`), `Appendix_B`, `Appendix_C`, the adventure. The Guild page names Ahmaergo's role without Gorath (`campaign/setting/organizations/08-xanathars-guild.md:101`).

### A5. Faith
None for Gorath. The Guild page gives the Guild no creed: "The sources give the Guild no creed, and the membership test is its only rite." (`campaign/setting/organizations/08-xanathars-guild.md:39`, quoted in part; see F5).

### A6. Signature belongings and the team's kit
Gorath has no personal item in any source. The team's kit, per the Factions Guide, applies to the first or second team the party meets:
> "That team also carries a *potion of healing*, a *potion of greater healing*, and a *+1 weapon*."
> — `campaign/guides/factions/09-xanathars-guild.md:7`

The team's look in the tavern visit (describes the team, not Gorath alone):
> "**Who comes:** Gorath (four duergar in unremarkable clothes). If Gorath is neutralized: Korgstrod Uxgulm's team (half-ogre + cloaked gazer). Noska Ur'gray does not visit — he arrives with intent."
> — `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:19`

### A7. How long in post
None. The Factions Guide gives the team order, not a start date. The only time reference is the Trollskull tenday table, which is quest timing (C, row 9).

### A8. Conduct as the sources describe it (party-triggered visits; these are quest-time, see C)
Appendix D, the early visit:
> "Four dwarves come in at the same time, which is unusual enough to notice. They don't look at you directly. They order ale by pointing at the nearest tap. They sit at two tables without rearranging the chairs — which means they sat exactly where they could watch the door and the stair. One of them, the broadest, has a filed-tooth smile he uses once, when your eyes meet his. He does not look away first."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1527`

> "They drink one round each and leave exact coin on the table. No tip. No trouble. They do not come back that night."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1528`

Appendix D, the active visit (Gorath himself):
> "Gorath sits at the bar — which is a choice, because it means his back is to the room. He orders something good, pays for it, and says, when there is a lull: "You cost us something." He doesn't specify what. "We want it back. Or we want something worth the same. You have until the new moon." He drinks the rest of his ale, sets the mug down precisely, and leaves. His team is outside. They walk east, together, without looking back."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1536`

The same visit in the Trollskull guide:
> "**Active campaign (Acts II–IV, once the Guild marks the party as a threat):** Gorath sits at the bar with his back to the room, orders something good, and says: "You cost us something. We want it back. Or we want something worth the same. You have until the new moon." Then leaves. His team is outside."
> — `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:28`

Appendix D, the trigger list and the meaning of the visit:
> "**What triggers a visit:**
> - The party has discovered, looted, or interfered with a Xanathar Guild outpost or operation.
> - A Guild spy planted as staff (Tobrin Ashvale, Grevik Nass, or any similar candidate) has been exposed.
> - The party has the Stone of Golorr or an Eye in their possession and the Guild knows it."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1519`-`:1522`

> "**What this means:** The Guild knows where you live. They are not threatened yet. This visit is a receipt — confirmation that their files on the party now include this address."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1531`

Appendix D's design note on when teams come:
> "Teams show up at the tavern in proportion to how much the party has gotten in their way — or how useful they might be."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1506`

Motto of the Guild's visits (Appendix D heading line):
> "*The Xanathar Guild does not negotiate. It sends lessons.*"
> — `sources/Appendix_D_-_Running_the_Tavern.md:1515`

Trollskull guide's version of the same motto: "*The Guild does not negotiate. It sends lessons.*" (`campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:17`).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, Guild page: "- **Gorath** — Duergar, lawful evil. See the **Gorath** page in Notable Figures." — `campaign/setting/organizations/08-xanathars-guild.md:110`
- Campaign, current page: "*Duergar (first response team leader), lawful evil, he/him*. Stat block: **Duergar**." — `campaign/setting/notable-figures/xanathars-guild/11-gorath.md:5`
- No adventure, Alexandrian or appendix source gives Gorath an alignment. Searched.

**Species (Gorath as an individual)**
- Campaign, Guild page: "- **Gorath** — Duergar, lawful evil." (`campaign/setting/organizations/08-xanathars-guild.md:110`)
- Campaign, Notable page: "*Duergar (first response team leader), lawful evil, he/him*." (`11-gorath.md:5`)
- Campaign, Factions Guide: "Gorath leads four **duergar**." (`campaign/guides/factions/09-xanathars-guild.md:9`) — this says the team is duergar. It does not say Gorath is.
- **[PDF image]** Alexandrian: "GORATH: Gorath is the leader of a small team of duergar." (`sources/6. Faction Response Teams.pdf`, printed p.54 [PDF p.6]) — team level.
- Appendix D: "### Xanathar Guild — Gorath's Duergar" (`sources/Appendix_D_-_Running_the_Tavern.md:1513`) — the team's name.
- Appendix D describes the team as "Four dwarves" (`:1527`, quoted in A8).
- Adventure: no Gorath entry.
- Result: no source says in so many words that Gorath is a duergar. [research] if the drafter keeps "duergar".

**Species (comparison, Korgstrod, for the drafter)**
- Adventure: "Korgstrod Uxgulm, the {@creature duergar} leader (40 hit points), seated in a stone chair and attended by 3 {@creature kobold||kobolds} (see \"Stone of Deception\" below)" — `sources/adventure-wdh.json:11987`
- Notable, Korgstrod: "- *Duergar (second response team leader), lawful evil, he/him*. Stat block: **Duergar**." — `campaign/setting/notable-figures/xanathars-guild/10-korgstrod-uxgulm.md:5`

**Pronouns**
- Campaign, current page: "he/him" (`campaign/setting/notable-figures/xanathars-guild/11-gorath.md:5`)
- Appendix D, independent of the page: "Gorath himself takes a seat facing the door." (`sources/Appendix_D_-_Running_the_Tavern.md:1517`)
- Appendix D: "He orders something good, pays for it, and says..." and "his back is to the room" (`sources/Appendix_D_-_Running_the_Tavern.md:1536`, quoted in A8)
- Trollskull guide: "Gorath sits at the bar with his back to the room, orders something good, and says:" (`campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:28`)
- Pronouns table: "| Gorath | xanathars-guild/11-gorath.md:5 | he/him | prose ("a man who is himself the warning", "he delivers it once") | High |" (`docs/plans/npc-pronouns-table-group-c.md:36`). **This table's evidence is the page's own prose**, so it is not an independent source. Appendix D and the trollskull guide are the independent ones.

**Stat block**
- Campaign, current page: "Stat block: **Duergar**." (`11-gorath.md:5`)
- Alexandrian, team: "4 **duergar** (MM p. 122)" — **[PDF image]** `sources/6. Faction Response Teams.pdf`, printed p.54 [PDF p.6], under "GORATH". This is the team's block.
- Alexandrian, stat reference: "Duergar – MM p. 122" — **[PDF image]** `sources/11. Lair  Xanathar’s Lair.pdf`, printed p.91 [PDF p.9], "STAT REFERENCE".
- No source gives a separate stat block for Gorath.

---

## C. Every sentence on the current page that narrates a quest-time event or a day-one conflict

Status key: **Day-one OK** (state on Ches 1, 1492 DR); **Routed** (quest-time, with the file where it already lives); **Unsourced** (no source; the drafter must tag `[research]` or cut it).

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Duergar (first response team leader), lawful evil, he/him*. Stat block: **Duergar**." | Day-one role OK. Species, alignment and stat block: see B (team-level only) | `organizations/08-xanathars-guild.md:110`; `factions/09-xanathars-guild.md:9` |
| 2 | L6 | "**Affiliation:** Xanathar's Guild" | Day-one OK | `organizations/08-xanathars-guild.md:110` |
| 3 | L7 | "**Featured in:** **Faction Outposts**, **Xanathar's Lair**" | Routed. Quest references | `campaign/structure/arc-e-faction-outposts.md:155` (the team deploys in the Getaway step); `campaign/structure/arc-f-xanathars-lair.md:339` (Notable Figures list only). The Lair PDF (pp.1–9) does not name Gorath, in the roster or elsewhere |
| 4 | L11 | "**Resonance.** Gorath should inspire slow dread as the message lands; unexpected respect for a man who delivers bad news without threatening and still makes you feel threatened; and the particular unease of a warning delivered with total professionalism." | Style, not a fact. "without threatening" conflicts with the sourced ultimatum (D7) | `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:28`; `sources/Appendix_D_-_Running_the_Tavern.md:1536` |
| 5 | L13 | "**Emotions.** Gorath most often feels professional calm, the satisfaction of a message delivered precisely, contempt for situations that require raised voices, deliberate patience, and the focused restraint of a man who is himself the warning." | Mostly voice-profile material. "professional calm" and "raised voices" are in the profile (see the Voice table below). "satisfaction" and "deliberate patience" are unsourced | `.claude/skills/character-voices/voices/xanathars-guild.md:198`, `:197` |
| 6 | L15 | "**Motivations.** Gorath wants to deliver the message exactly as instructed, leave without escalating, and ensure the recipient understood." | Unsourced in part. The team's purpose is a lesson (`factions/09:9`). "exactly as instructed" and "ensure the recipient understood" have no source | `campaign/guides/factions/09-xanathars-guild.md:9` |
| 7 | L17 | "**Inspirations.** When playing Gorath, channel Mike Ehrmantraut (*Breaking Bad*), Anton Chigurh (*No Country for Old Men*, the message-before-consequence aspect), and Winston Wolf (*Pulp Fiction*)." | Not a fact | n/a |
| 8 | L21 (a) | "To the world, Gorath is a stocky duergar who walks into the tavern in unremarkable clothes, sits at the bar, orders something good, and leaves exact coin." | **Routed** for "the tavern" (Trollskull Manor, party-triggered). "stocky" is **Unsourced**. "unremarkable clothes" is the team's (A6). "sits at the bar, orders something good" is the active visit. "leaves exact coin" is the early visit (A8) | `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:19`, `:26`, `:28`; `sources/Appendix_D_-_Running_the_Tavern.md:1528`, `:1536` |
| 9 | L21 (b) | "To those who receive his message, he delivers it once, clearly, and does not repeat himself." | Day-one OK (trait). "delivers it once" and "does not repeat himself" are in the profile; "clearly" is unsourced | `.claude/skills/character-voices/voices/xanathars-guild.md:195`; `sources/Appendix_D_-_Running_the_Tavern.md:1536` |
| 10 | L21 (c) | "Deep down, Gorath is the announcement. The consequence comes after. He finds the distinction important." | "is the announcement... the consequence comes after" is in the profile. "He finds the distinction important" is **Unsourced** | `.claude/skills/character-voices/voices/xanathars-guild.md:198`; `campaign/setting/organizations/08-xanathars-guild.md:77` |
| 11 | L23 | "In a fight, Gorath fights without aggression and without mercy, in that order. He does not pursue. His job is to survive and report." | **Unsourced** (no combat, pursuit or reporting statement exists for Gorath or for the team) | none. Searched: Factions Guide, Trollskull guide, Appendix D, PDF 6 p.54, Lair PDF |
| 12 | L25 (a) | "**Relationships.** Gorath is the first response team leader of Xanathar's Guild (four duergar, sent when the Guild wants a lesson taught rather than a person killed)" | First half, **Day-one OK**: `factions/09-xanathars-guild.md:9`. "a lesson" is sourced (`:9`). "rather than a person killed" is **Unsourced** (the closest is `organizations/08-xanathars-guild.md:77`, "The Guild warns before it kills.") | `campaign/guides/factions/09-xanathars-guild.md:9`; `sources/Appendix_D_-_Running_the_Tavern.md:1515` |
| 13 | L25 (b) | "the formal notice that Xanathar knows what the party did" | **Routed** (quest-time: a party action). The trigger is a party action (A8). The notice's meaning is stated for the early visit only | `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:21`-`:24`; `sources/Appendix_D_-_Running_the_Tavern.md:1519`-`:1522`, `:1531` |
| 14 | L25 (c) | "and the first escalation before Korgstrod's team and then Noska's arrive." | Team order is **Day-one OK** (`factions/09:9`, `:11`, `:13`). "escalation" is a quest-state mechanic and **Routed** | `campaign/guides/factions/09-xanathars-guild.md:35` (quest escalation), `:72`-`:74` (tier table); `campaign/structure/arc-e-faction-outposts.md:155`; `campaign/guides/gm-guide/running-the-villains.md:49` |
| 15 | L29 | "Gorath is a stocky duergar who arrives without warning, sits at the bar, orders something good, delivers a message once, and leaves. He does not repeat himself." | Overview. "stocky" and "arrives without warning" are **Unsourced**. "sits at the bar, orders something good, delivers a message once, and leaves" is the **Routed** active visit (quest-time) | `sources/Appendix_D_-_Running_the_Tavern.md:1536`; `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:28` |

**Voice profile, quest-time clauses and other items** (`.claude/skills/character-voices/voices/xanathars-guild.md:191`-`:205`):

| Line | Profile text (exact) | Status | Note |
|---|---|---|---|
| 192 | "*A duergar messenger who delivers the warning once, calmly, and leaves the threat in the air.*" | Day-one OK | Tagline |
| 194 | "- **Sound:** A low, calm, unhurried voice with no inflection at all." | Day-one OK (unsourced style) | |
| 195 | "- **Sentence shape:** A short, complete message delivered once, deliberately (a break from `ember-voice` speech). He doesn't repeat himself or answer follow-up questions." | Day-one OK | |
| 196 | "- **Word choice:** Plain and exact. He orders something good at the bar by name. He calls the recipient by name, which is itself the threat." | Day-one OK | Source for "orders something good": `:1536` |
| 197 | "- **Swearing:** *Never · Plain · n/a.* He finds raised voices and curses equally unprofessional." | Keep (ruling: Swearing line stays) | |
| 198 | "- **Personality in speech:** Professional calm. He is the announcement, and he knows the consequence comes after. His contempt for escalation shows in how softly he speaks." | Day-one OK | |
| 199 | "- **Quirks:** He leaves exact coin. He says the message, finishes his drink, and goes." | Day-one OK | Sources: `:1528`, `:1536` |
| 200 | "- **Signature phrases:** "I'll say this once." / "That's the message." / "Good ale."" | Day-one OK | |
| 201 | "- **Never:** He never threatens directly, never repeats himself, and never starts the fight." | Conflicts with the sourced ultimatum (D7) | Drafter decision |
| 203 | "  - *Greeting:* "The dark ale, please. Good ale."" | Day-one OK (profile sample) | No source |
| 204 | "  - *Business:* "I'll say this once. The Xanathar knows what you took from the sewers. Return it by the new moon. That's the message."" | **Quest-time clauses: "what you took from the sewers" and "Return it by the new moon"** (the restatement in the brief, ruling 16). "The Xanathar" is in speech, not a speech tag (see D8) | Day-one restatement needed. The sourced ultimatum is `:1536` and `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:28` |
| 205 | "  - *Under pressure:* "I'm leaving now. I'd let me."" | Printed as shown. The sentence is unclear ("I'd let me"); not a quest clause | Flag for the voice pass |

---

## D. Conflicts

Rank used: campaign files first, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.

**D1. Alignment.** No conflict. One source family (campaign). "Duergar, lawful evil" appears in `campaign/setting/organizations/08-xanathars-guild.md:110` and `campaign/setting/notable-figures/xanathars-guild/11-gorath.md:5`. Nothing else gives an alignment. Both are campaign pages and neither cites a source.

**D2. Species of Gorath himself.** Not a flat conflict. The campaign says "Duergar" for him (`08:110`, `11:5`). The Factions Guide says his team is duergar (`factions/09:9`). The Alexandrian says "a small team of duergar" (**[PDF image]** printed p.54 [PDF p.6]). Korgstrod's species is in the adventure (`adventure-wdh.json:11987`) and Gorath's is not. Campaign outranks Alexandrian, so "Duergar" stands for the campaign, but the drafter should know no source states it for Gorath personally. [research]

**D3. Stat block.** Not a flat conflict. The Notable page's "Stat block: **Duergar**." (`11:5`) matches the team block "4 **duergar** (MM p. 122)" (**[PDF image]** printed p.54 [PDF p.6]). Gorath himself has no block of his own in any source.

**D4. Venue of the "tavern" (day-one setting vs party-triggered visits).** The Persona says Gorath "walks into the tavern" (`11:21`). Every source places the tavern visits in Trollskull Manor and ties them to party action (`campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:21`-`:24`; `sources/Appendix_D_-_Running_the_Tavern.md:1519`-`:1522`). On Ches 1 the manor is not yet the party's (`sources/Appendix_D_-_Running_the_Tavern.md:1506` is the design note; the Trollskull Alley and Trollskull Manor quests are the source of the deed). The Persona line does not name the manor. The drafter must decide whether the setting page names a tavern.

**D5. Which escalation tier sends Gorath.** Two campaign statements disagree.
- Gorath at Suspicious: "| Suspicious | Gazer scouts; Nihiloor processes captured intelligence. First team (Gorath's duergar) deployed as a warning |" (`campaign/guides/factions/09-xanathars-guild.md:72`) and "| **Xanathar's Guild** | Normal operations | Gazer scouts; Nihiloor processes captured intelligence. First team: Gorath's duergar, deployed as a warning | Second team: Korgstrod Uxgulm's squad (half-ogre + gazer) | Third team: Noska Ur'gray's bugbear squad with orders to eliminate. Xanathar takes personal interest; lair incursions trigger Eye-ray responses |" (`campaign/guides/gm-guide/running-the-villains.md:49`; header at `:47`: "| Faction | Unaware | Suspicious | Alert | Lockdown |").
- Gorath at Alert, after a second hit: "***Escalation.*** Xanathar moves to Suspicious (Tier 2). If a second Xanathar outpost has already been hit, it moves directly to Alert (Tier 3), and Gorath's team deploys within 2 days to the last known party location. **Founders' Day Clock: 2–4 days.**" (`campaign/guides/factions/09-xanathars-guild.md:35`) and "Xanathar moves directly to Alert (Tier 3) and Gorath's response team deploys to the last known party location within 2 days." (`campaign/structure/arc-e-faction-outposts.md:155`, the full sentence ending "...within 2 days.").
- Both are campaign files. The two tables and the two escalation paragraphs cannot both be right. The orchestrator decides.

**D6. The *Dragon Heist* citation.** The Guild page cites the adventure for Gorath: "Ott Steeltoes keeps Sylgar, and Gorath and Korgstrod Uxgulm lead duergar in the field (*Dragon Heist*, 5e; Notable Figures)." (`campaign/setting/organizations/08-xanathars-guild.md:43`). The adventure has no Gorath (no hit for `Gorath` in `sources/adventure-wdh.json`), and its list of important underlings omits him (`:15066`-`:15076`). The adventure names Korgstrod as "the duergar leader" (`:11987`). The citation for Gorath is unsupported. The Guild page's "Dragon Heist" citation is therefore stale for Gorath.

**D7. "Never threatens directly" against the sourced ultimatum.** The profile says "He never threatens directly, never repeats himself, and never starts the fight." (`.claude/skills/character-voices/voices/xanathars-guild.md:201`). The sourced visit ends with "You have until the new moon." (`sources/Appendix_D_-_Running_the_Tavern.md:1536`; `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:28`). The Resonance also says "without threatening" (`11:11`). The drafter decides whether "threatens" means a direct threat. The ultimatum is quoted above.

**D8. "The Xanathar" in speech against "Xanathar is 'it'."** The profile's Business line reads "The Xanathar knows what you took from the sewers." (`.claude/skills/character-voices/voices/xanathars-guild.md:204`). The brief's ruling 9 says the guild is "Xanathar's Guild" and Xanathar is "it" in narration; ruling 16 says "Xanathar is 'it' in narration, never in a figure's speech tag." The line is speech, not a tag. Flagged for the drafter. The sourced ultimatum has no "The Xanathar" (`:1536`).

**D9. Ahmaergo labelled duergar in Appendix C (not Gorath; label drift).** "2 = Ahmaergo (duergar; inspection; DC 15 Deception to pass as authorized)" (`sources/Appendix_C_-_Player_Faction_Missions.md:1887`). The Guild page says "- **Ahmaergo** (DH p. 195) — Shield dwarf majordomo, lawful evil." (`campaign/setting/organizations/08-xanathars-guild.md:101`). The adventure says "{@creature Ahmaergo|WDH}, dwarf majordomo" (`sources/adventure-wdh.json:15071`). Shown because the label "duergar" is used loosely across the Guild.

**D10. The wiki's Gorath is a different figure.** Not a conflict to resolve. The wiki page is the Kara-Tur spirit (see section E, wiki). Its infobox and lead line are quoted there so the drafter can see the collision.

**D11. Early visit called "dwarves" and "duergar" in two sources.** "Four dwarves come in at the same time" (`sources/Appendix_D_-_Running_the_Tavern.md:1527`) and "Four duergar, same time, sit at two tables covering door and stair." (`campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:26`). Same visit, two words. No real conflict.

---

## E. Stale lines in other files (not to be edited), and routed quest references

### E1. Stale or unsupported lines in other files
- `campaign/setting/organizations/08-xanathars-guild.md:43`: "Ott Steeltoes keeps Sylgar, and Gorath and Korgstrod Uxgulm lead duergar in the field (*Dragon Heist*, 5e; Notable Figures)." — the *Dragon Heist* citation does not support Gorath (D6).
- `campaign/guides/factions/09-xanathars-guild.md:35` and `campaign/structure/arc-e-faction-outposts.md:155` — the Alert-path deployment of Gorath (D5).
- `campaign/guides/gm-guide/running-the-villains.md:49` — Gorath at Suspicious (D5).
- `docs/plans/npc-pronouns-table-group-c.md:36` — the pronoun evidence is the page's own prose, so it is circular (B).
- `docs/plans/setting-compendium-research-notes/pass5/xanathars-guild.md:113` — prior note reads "- **Gorath** — org `:30`: "- **Gorath** — Duergar (first response team leader), lawful evil. See the **Gorath** page in Notable Figures."" and says "Result: matches." That note predates the current org page (now `:110`).
- `docs/plans/lords-alliance-mechanics-reference.md:367` — a table row in a mechanics reference: "| Xanathar's Guild | First | A leader and four fighters from underground stock; sent to teach a lesson | Gorath's team |". No separate source.
- `sources/Appendix_C_-_Player_Faction_Missions.md:1887` — Ahmaergo as duergar (D9).

### E2. Routed quest references (quest-time, with the files where they already live)
- Trollskull Manor guide, active-visit and triggers: `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:15`-`:30` (the whole Gorath section). Quote for the trigger list, line 21-24: "**Triggers:** - Party has discovered, looted, or interfered with a Xanathar outpost or operation - A Guild plant as staff (Tobrin Ashvale, Grevik Nass) has been exposed - Party has the Stone of Golorr or an Eye and the Guild knows it" — `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:21`-`:24`.
- Trollskull patron table, Slot for the tenday after Gralhund Villa: "| First tenday after **Gralhund Villa** | Renaer Neverember, Floon Blagmaar, Yagra Stonefist (at the bar, or on the door if she is the Bouncer) | 8: Xanathar's Guild (Gorath's Duergar) | The Stone has changed hands. The first villain visit tells the party they're now players in the Grand Game. |" — `campaign/guides/trollskull-manor/06-tavern-time.md:28`
- Appendix D, the whole profile: `sources/Appendix_D_-_Running_the_Tavern.md:1513`-`:1541`.
- Appendix D, design note: `sources/Appendix_D_-_Running_the_Tavern.md:1506`.
- Factions Guide, the kit and first-encounter rule: `campaign/guides/factions/09-xanathars-guild.md:7` (quoted in A6).
- Factions Guide, escalation and tier table: `campaign/guides/factions/09-xanathars-guild.md:35`, `:72`-`:74`.
- Factions Guide, the Terasse outpost is the only Guild outpost that names Gorath. Quote: "***Escalation.*** Xanathar moves to Suspicious (Tier 2). If a second Xanathar outpost has already been hit, it moves directly to Alert (Tier 3), and Gorath's team deploys within 2 days to the last known party location. **Founders' Day Clock: 2–4 days.**" (`campaign/guides/factions/09-xanathars-guild.md:35`, under "### Terasse Estate — Mini-Heist (Castle Ward, Elsambul's Lane)" at `:17`). The Grinda outpost (`:37`-`:49`) and the Orb Confectioners outpost (`:51`-`:63`) do not name Gorath. The Orb Confectioners outpost's escalation names Korgstrod: "***Escalation.*** Xanathar moves to Alert (Tier 3). Korgstrod's response team deploys within 3 days of the operation. **Founders' Day Clock: 1–3 days.**" (`campaign/guides/factions/09-xanathars-guild.md:63`).
- Factions Guide, the Grinda escalation: "***Escalation.*** Xanathar moves to Suspicious (Tier 2) if the location is raided; no tier change if the party engages as customers without taking documents. **Founders' Day Clock: 1–2 days.**" (`campaign/guides/factions/09-xanathars-guild.md:49`).
- Structure doc, Faction Outposts Getaway step (quest-state): `campaign/structure/arc-e-faction-outposts.md:155`.
- Structure doc, Xanathar's Lair Notable Figures list: `campaign/structure/arc-f-xanathars-lair.md:339`: "- **Notable Figures** — Full NPC profiles for Xanathar, Ahmaergo, Nar'l Xibrindas, Nihiloor, Noska Ur'gray, Ott Steeltoes, Thorvin Twinbeard, Keln Trigos, Grinda Garloth, Korgstrod Uxgulm, Gorath." (no scene names him).
- Quest events, Gorath's team as a response (quest-time): `campaign/quests/faction-events/bregan-daerthe/r03-soldier/ev-01-soldier.md:146`: "> - **Gorath's team:** "Watch for Gorath's crew next, four duergar who enjoy hurting people. They're who the Guild sends first when somebody needs a lesson."" — `campaign/quests/faction-events/doom-raiders/r03-wolf/ev-01-wolf.md:125`: "> - **Xanathar's Guild:** Gorath with four duergar, then Korgstrod Uxgulm with a half-ogre and a gazer, then Noska Ur'gray with six bugbears and a gazer. When all three have been beaten, the answer says the guild has no crew left to send on the street and that the next move will be Xanathar's own." — `campaign/quests/faction-events/lords-alliance/r25-warduke/ev-01-warduke.md:193`: "> | Xanathar's Guild | First | A leader and four fighters from underground stock, sent to teach a lesson | Gorath's team |"
- Alexandrian GM tip, a timed visit in an example schedule: **[PDF image]** "First, take 5 minutes between sessions to think about what each faction is going to do next. Some of those things won't affect the PCs; some will. Make a list of those and when they'll happen: Gorath will come to Trollskull Manor at 5pm on the 10th. Souun Xibrindas will target one of the PCs for assassination with a sniper team at 10am on the 11th. And so forth." — `sources/6. Faction Response Teams.pdf`, printed p.50 [PDF p.2] (a GM example, not a date for the campaign; the month is not given).
- Alexandrian, the first or second team's directive: **[PDF image]** as quoted in A4 — `sources/6. Faction Response Teams.pdf`, printed p.54 [PDF p.6]. Its routing: `campaign/guides/factions/09-xanathars-guild.md:7`.
- Alexandrian, Noska's notes on the team order: `campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md:22`, `:35`, `:98`.
- Notable, Korgstrod (parallel page): `campaign/setting/notable-figures/xanathars-guild/10-korgstrod-uxgulm.md:5`, `:25`.
- Notable, Noska (parallel page): `campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md:76`: "**Relationships.** Noska is an enforcer of Xanathar's Guild, the third response team leader, and a shield dwarf whose crossbow-arm, rust monster pet, and bathtub bed constitute a complete portrait of his priorities."

### E3. Wiki, the other Gorath (not this figure)
Source: `scratchpad/wiki-xg/Gorath.txt`. The wiki's own infobox:
> "| name           = Gorath"
> — `Gorath.txt:4`

> "| home           = [[Kuo Te' Lung]], [[Shou Lung]]"
> — `Gorath.txt:10`

> "| sex            = Male"
> — `Gorath.txt:12`

> "| race           = Greater [[spirit]]"
> — `Gorath.txt:13`

> "| ref1e          = <ref name="KTI-p23">{{Cite book/Kara-Tur: The Eastern Realms/Volume I|23}}</ref>"
> — `Gorath.txt:35`

The lead:
> "The '''Gorath''' was the hidden leader of the [[Royal Vagabonds]] of [[Shou Lung]] around [[1357 DR]].<ref name="KTI-p23" />"
> — `Gorath.txt:37`

> "The Gorath secretly assisted [[the Old Man]] in managing the activities of the Royal Vagabonds against enemies of Shou Lung. In truth, Gorath was for centuries in the service of the [[Chin dynasty]], a task assigned to him by the [[Undersecretary of the Minister of War]] in the [[Celestial Bureaucracy]] and he did not always work for the good of the Empire.<ref name="KTI-p23" />"
> — `Gorath.txt:40`

> "The Gorath had encountered [[Lui-hsia Chih]] of the [[Many-Hued Peacock Society]] several times in the past and they were mortal enemies.<ref name="BotY-p1">{{Cite book/Blood of the Yakuza/Encounter Construction Booklet|1}}</ref>"
> — `Gorath.txt:43`

Edition: none printed on these lines. The citation keys are *Kara-Tur: The Eastern Realms* (KTI, p.23) and *Blood of the Yakuza* (BotY, pp.1 and 23). The book titles are AD&D-era (inferred, [research]). Do not import: the wiki's Gorath is a spirit and a Royal Vagabonds leader in Shou Lung, not a duergar. The wiki's Xanathar pages (`wiki-xg/`) do not name Gorath.

---

## F. Gaps (what a Background would need that no source gives)

1. **Birth, origin, clan, home.** No source. Suggested inference, modest and sourced: "He came up through the Guild's membership test, the same entry path as every member" (`campaign/setting/organizations/08-xanathars-guild.md:32`). Tag `[research]`.
2. **How he rose to team leader.** No Gorath-specific source. The general advancement rule is `campaign/setting/organizations/08-xanathars-guild.md:32` ("advancement depends on wiles and on the ability to dispose of rivals"). Suggested inference: "Xanathar gave him the first team." Tag `[research]`.
3. **Former life.** No source.
4. **Rank on the ladder.** `08:45` gives the ladder, not his place. The team order (`factions/09:9`, `:11`, `:13`) is the only ranking. A Background can state the order without assigning a rank.
5. **Faith.** No source. Do not invent.
6. **Signature belongings.** No source for Gorath. The team kit is in `factions/09:7`. Do not assign it to Gorath personally.
7. **Time in post.** No source. The team order implies he has been in post since the Guild had response teams, but no date is given.
8. **Relations to Ahmaergo, Nar'l, Nihiloor, Xanathar, Ott, Grinda.** No source gives a personal tie. Grinda outfits the team (A4, PDF p.54 [PDF p.6]). The team carries Nar'l's directive (A4). Those are team facts, not personal ones.
9. **Species, alignment, stat block as Gorath personally.** See B and D2-D3.
10. **Motivations and Morale.** Unsourced (C rows 6 and 11).
11. **"Stocky."** Unsourced. The word appears only on the Notable page (`11:21`, `:29`).
12. **"Arrives without warning."** Unsourced (`11:29`).
13. **"Rather than a person killed."** Unsourced (C row 12).
14. **Where he lives or holds court.** No source. The adventure places Korgstrod in a stone chair (`:11987`), and no source places Gorath anywhere.
15. **Why Xanathar trusts him.** No source.

---

## Not found

Searched for "Gorath" (and "duergar" where the team is meant) in:
- `sources/adventure-wdh.json`: no hit for `Gorath`. "duergar" hits at lines 2784, 2786, 7126, 8288, 11983, 11987, 12015 (Zemk, the Guild duergar at the Nar'l retrieval, Korgstrod, Thorvin's workshop guard). None names Gorath. The "important underlings" list (`:15066`-`:15076`) omits him.
- `sources/SOURCE_GUIDE.md`: no hit for `Gorath`. Lines `:29`, `:83`, `:88`, `:343` name Xanathar, duergar in the dungeon level, and the Guild's internal politics, but not Gorath.
- `sources/Appendix_B_-_Player_Factions.md`: no hit.
- `sources/Appendix_C_-_Player_Faction_Missions.md`: no Gorath. The only "duergar" line is `:1887` (Ahmaergo, D9).
- `sources/Appendix_D_-_Running_the_Tavern.md`: Gorath at `:1513`-`:1541`.
- `sources/Act_III_Arc_D.md`, `sources/Act_III_Arc_E.md`: no hit.
- `sources/research/` (all bundles): hits only in copies of the campaign files listed in E. No new Gorath facts.
- `campaign/` (all folders, incl. `setting/`, `guides/`, `structure/`, `quests/`, `locations/`, `gazetteer/`): Gorath in the files listed in C and E. No hit in `campaign/locations/xanathar-sewer-hideout/` or `campaign/quests/act-i/finding-floon/`.
- `docs/`: Gorath appears only in research notes and the pronouns table (E1) and in `docs/index.html` (generated; not read).
- `.claude/skills/character-voices/voices/xanathars-guild.md`: `### Gorath` at `:191`-`:205`.
- `scratchpad/wiki-xg/`: only `Gorath.txt` names Gorath.
- Alexandrian PDFs read: `5. Faction Outposts.pdf` (pp.36–48, all 13 pages; Gorath not named), `6. Faction Response Teams.pdf` (pp.49–56; Gorath at p.54 [PDF p.6] and the GM tip at p.50 [PDF p.2]), `7. Other Response Teams.pdf` (pp.57–61, all 5 pages; not named), `11. Lair  Xanathar’s Lair.pdf` (pp.83–91, all 9 pages; not named; the duergar appear only as "2 duergar" at p.89 [PDF p.7] and as the stat reference "Duergar – MM p. 122" at p.91 [PDF p.9]), `17. Outpost and Lair Revelation Lists.pdf` (pp.121–124; not named), `27. Addendum A Night in Trollskull Manor.pdf` (pp.178–189; not named, the response-team section at p.188 [PDF p.11] is generic), `29. Addendum Timelines  Starting the Campaign.pdf` (pp.225–226, both pages; not named), `21. Faction Reports of the Grand Game.pdf` (pp.142–154, all 13 pages; handwritten reports; not named), `1. The Villains.pdf` (pp.13–16 of 4 read; the Xanathar section at p.15 [PDF p.3] is about Xanathar, Gorath not named).
- **Not read page by page:** `2. Other Factions.pdf`, `3. Player Character Factions.pdf`, `4. Gralhund Villa.pdf`, `8. The Eyes of the Stone.pdf`, `9. Lair – Sea Maidens Faire.pdf`, `10. Lair  Cassalanter Villa.pdf`, `12. Lair  Zhentarim – Kolat Towers.pdf`, `13. Clues and Timelines.pdf`, `14. Finding Floon.pdf`, `15`, `16`, `18`, `19`, `20`, `22`–`26`, `28`, `30`. None of the campaign files derived from them names Gorath. Check with `pdftotext` before drawing a negative conclusion from these.
- `sources/Other remix files/`: see Not readable.

---

## Not readable

- `sources/Other remix files/*.docx` were not opened (no tool for .docx). `sources/SOURCE_GUIDE.md` lists an NPC guide for the Waterdavian's notes that may name Gorath: "The Waterdavian's Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx" (`sources/SOURCE_GUIDE.md:695`). It is a "Broad NPC reference", so it might hold Gorath. The drafter should extract it and check it for "Gorath" before writing the Background. No other .docx in the guide names Xanathar's Guild.
- **[PDF image] quotes:** every PDF quote above was read from the rendered page image (no text layer). Run `pdftotext -layout` on `5. Faction Outposts.pdf`, `6. Faction Response Teams.pdf`, `11. Lair  Xanathar’s Lair.pdf`, `17. Outpost and Lair Revelation Lists.pdf` and `27. Addendum A Night in Trollskull Manor.pdf` before any quote goes into prose.
- `Gorathil` (the other wiki page the caller named) is not in `scratchpad/wiki-xg/`, so it was not read.

## Not run
- `voicecheck.py` was not run (research only).
- The page was not written. No file was edited except this notes file.
