# Pass 6 research notes: Thorvin Twinbeard

Page: `campaign/setting/notable-figures/xanathars-guild/07-thorvin-twinbeard.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 16)
Caller's specifics: Thorvin is the Guild's chief engineer and trapsmith and a Harper informant. The Harper tie is a hidden loyalty. The Overview shows only the engineer. The Harper contact goes in Character Information and a Secret callout. Check the Harpers organization page and the Harper voice and figure pages, and quote the day-one state of the tie against quest-time recruitment text.

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Where a line was too long for a plain quote, the sentence is quoted whole and the rest of the line is named.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string with escapes removed. `{@creature ...}` and similar tags are left as written. Line numbers come from Read or Grep output.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. Every PDF quote below was transcribed from the rendered page image and is marked **[PDF transcription]**. Check each one with `pdftotext -layout` before any quote goes into prose. Pages read in full: `sources/11. Lair  Xanathar’s Lair.pdf` (PDF pp.1 to 9, printed pp.83 to 91), `sources/17. Outpost and Lair Revelation Lists.pdf` (PDF pp.1 to 4, printed pp.121 to 124), `sources/5. Faction Outposts.pdf` (PDF pp.1 to 13, printed pp.36 to 48), `sources/3. Player Character Factions.pdf` (PDF pp.1 to 3, printed pp.23 to 25). Grep cannot read these PDFs (compressed streams), so the "not found" results for them come from the page reads.
- Wiki: the extracted page `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-xg/Thorvin_Twinbeard.txt` (cited "wiki-xg :N"), and the pass-5 bundle copies. The infobox citation keys are `WDH5e-p216`, `WDH5e-p105` and `WDH5e-p86`, which name *Waterdeep: Dragon Heist* 5e. Editions are otherwise not printed on the lines.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written.

Ruling used throughout: Ches 1, 1492 DR is day one. Thorvin is free, in post as the Guild's engineer, and a Harper informant whose tie is hidden. Lair events (the gazer's destruction, the smokepowder plan, the collapse, the rescue or flight) are quest time.

---

## A. Background facts by theme

### A1. Origin, family, upbringing

No source gives Thorvin's birth, clan, home town, parents or training. The only family fact in the sources is in the Lair structure doc. It is a quest-scene sentence, so it is listed here and again in section C.

> "Thorvin will not evacuate himself. He has a family in the Trades Ward, and he intends to survive this. He will delay alarm responses to mechanical failures by "taking unusually long to diagnose the problem." A DC 12 Dexterity (Thieves' Tools) check creates a failure he can credibly explain."
> — `campaign/structure/arc-f-xanathars-lair.md:97` (Scene 3, "Inside Ally: Thorvin Twinbeard (X13)")

Race and ethnicity (wiki, edition from key `WDH5e-p216`):

> "| race           = [[Dwarf]]"
> — wiki-xg :14

> "| ethnicity      = [[Shield dwarf]]"
> — wiki-xg :15

Adventure, subrace:

> "Thorvin is a shield dwarf {@creature commoner}, with these changes:"
> — `sources/adventure-wdh.json:32625`

Campaign, species (day-one page label):

> "*Dwarf engineer (secret Harper), neutral good, he/him*. Stat block: **Spy**."
> — `campaign/setting/notable-figures/xanathars-guild/07-thorvin-twinbeard.md:5`

### A2. Trade, training and tools

Adventure, the post and the tools:

> "{@creature Thorvin Twinbeard|wdh|Thorvin} serves as {@creature Xanathar|WDH}'s chief engineer and trapsmith. He also serves the Harpers as a paid informant, keeping that faction apprised of {@creature Xanathar|WDH}'s plans as well as he can. Thorvin uses the ruse of maintenance inspections to cover up secret meetings he holds with Harper spies in Skullport and elsewhere."
> — `sources/adventure-wdh.json:32617`

> "Thorvin wears iron-rimmed spectacles and carries a large, heavy wrench that doubles as a club. He also carries mason's tools, {@item smith's tools|PHB}, and {@item thieves' tools|PHB}, and has proficiency with all three."
> — `sources/adventure-wdh.json:32618`

Wiki occupation (edition key `WDH5e-p216`):

> "| occupation     = Engineer<ref name="WDH5e-p216" />"
> — wiki-xg :16

Campaign, the Guild page (the quote begins mid-paragraph; the omitted opening covers Xanathar's lair below Skullport and its lieutenants):

> "Ahmaergo, a shield dwarf, is the most influential member after the beholder, and Nar'l Xibrindas is its only advisor. Nihiloor has carved out a lair of its own inside the beholder's lair, Noska Ur'gray is the chief enforcer and Thorvin Twinbeard is the chief engineer and trapsmith. Ott Steeltoes keeps Sylgar, and Gorath and Korgstrod Uxgulm lead duergar in the field (*Dragon Heist*, 5e; Notable Figures)."
> — `campaign/setting/organizations/08-xanathars-guild.md:43` (the Structure paragraph)

Campaign, the Lair structure doc (tenure as engineer; see D3 for the Harper duration):

> "*Inside Ally: Thorvin Twinbeard (X13).* Thorvin is a dwarf engineer who has maintained the lair's mechanical infrastructure for nine years and served as a Harper informant for six. He is watched by a gazer at all times — a tiny beholder-kin that floats near the workshop ceiling and observes everything. He knows it is there. He communicates in short, technical-seeming statements that encode information in their structure."
> — `campaign/structure/arc-f-xanathars-lair.md:91`

Derived, not sourced: "nine years" before Ches 1, 1492 DR points to about 1483 DR. The campaign gives no date. Mark any use `[research]`.

### A3. How he joined the Guild, and his rank

No source says how or when Thorvin was hired. Two sources place him among the Guild's officers, and the wiki's one dated line is undated in itself.

Adventure, the "important underlings" list:

> "{@creature Xanathar|WDH} relies on underlings for advice, information, and day-to-day oversight of the Xanathar Guild. The following important underlings are described in appendix B:"
> — `sources/adventure-wdh.json:15066`

> "{@creature Thorvin Twinbeard|wdh}, dwarf engineer"
> — `sources/adventure-wdh.json:15076`

Wiki, the appointment (edition key `WDH-p100`; the paragraph before it is dated 1492 DR):

> "By {{Yearlink|1492}}, Zushaxx had fully taken over Skullport, forcing the businesses within to pay it for protection."
> — `sources/research/pass5-bundles/xanathars-guild/wiki.txt:159`

> "By this time, Zushaxx had also appointed [[Thorvin Twinbeard]], a Harper informant, [[Nihiloor]], a mind flayer, and [[Noska Ur'gray]] to important positions. It had also come to own [[Sylgar]], a goldfish."
> — `sources/research/pass5-bundles/xanathars-guild/wiki.txt:161` (the "By this time" is not dated; it follows the 1492 DR paragraph)

Campaign, the rank ladder (Thorvin is not placed on it):

> "The published ranks for members, from lowest to highest, are Eyestalker, Agent of the Eye, Eye Ray, Guild Boss and Hand of the Eye (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/08-xanathars-guild.md:45`

### A4. The Harper tie: day-one state, quest-time text, and its duration

Summary for the drafter. Day one (campaign): Thorvin is a secret Harper informant inside the Guild and a paid one. He holds secret meetings with Harper spies in Skullport (`campaign/setting/organizations/01-harpers.md:64`; `campaign/setting/organizations/08-xanathars-guild.md:85`; `campaign/setting/geography/undermountain-and-skullport.md:93`). Xanathar has begun to question his loyalty and a gazer watches him (`campaign/setting/organizations/08-xanathars-guild.md:85`). Quest time: how the party reaches the Harper channel (the renown gate and the recognition code in the Lair's Scene 1, `campaign/structure/arc-f-xanathars-lair.md:31`, and `sources/adventure-wdh.json:15161`) and the reveal (`campaign/structure/arc-f-xanathars-lair.md:95`). No Harper mission in `campaign/quests/faction-events/harpers/` names him (A4b).

Day-one (campaign), the Harpers organization page:

> "**Informants inside rival groups:** Thorvin Twinbeard is a secret Harper informant inside Xanathar's Guild, and Corene Wyldath works in its Dock Ward operation under the name Halla Ironstave. Mara Coppersail works as a ticket clerk at the Sea Maidens Faire and passes what she sees to the Harpers."
> — `campaign/setting/organizations/01-harpers.md:64`

> "- **Xanathar's Guild** (enemy): The Harpers keep Thorvin inside the lair and Corene in the Dock Ward operation, and the wiki says they move against thieves' guilds. An intellect devourer rides Corene, and she is one of three Harpers Nihiloor has taken."
> — `campaign/setting/organizations/01-harpers.md:89`

Day-one (campaign), the Guild organization page ("These stances hold on Ches 1, 1492 DR."):

> "- **The Harpers** (enemy): The Harpers keep Thorvin Twinbeard inside the lair as a paid informant, and Corene Wyldath works in the Guild's Dock Ward operation under a false name (**The Harpers**; **Corene Wyldath**). Xanathar has begun to question Thorvin's loyalty and has set a gazer to watch him (*Dragon Heist*, 5e). One of Nihiloor's intellect devourers rides Corene, and she is one of three Harpers it has taken."
> — `campaign/setting/organizations/08-xanathars-guild.md:85`

Day-one (campaign), the Skullport meetings:

> "- **The Harpers:** Dalagor's Fortress, a Harper hideout, stands on the uppermost level of Skullport, guarded by a dragonborn mage named Felrax. **Thorvin Twinbeard** serves the Harpers as a paid informant and holds secret meetings with Harper spies in Skullport."
> — `campaign/setting/geography/undermountain-and-skullport.md:93`

Day-one (adventure), the same tie, from the paragraph quoted in full at A2:

> "He also serves the Harpers as a paid informant, keeping that faction apprised of {@creature Xanathar|WDH}'s plans as well as he can."
> — `sources/adventure-wdh.json:32617`

Wiki, the tie (edition key `WDH5e-p216`):

> "Thorvin was the chief engineer and trapsmith for the [[Xanathar]]. He was also a paid informant of the [[Harpers]] and informed them of the Xanathar's plots under the cover of his maintenance inspections in [[Skullport]].<ref name="WDH5e-p216" />"
> — wiki-xg :65

The duration, as the campaign states it (the conflict is in D3):

> "To those who earn his trust, he has been a Harper informant for three years, knows exactly where Nar'l Xibrindas hid the smokepowder, and will tell the party where to place it for maximum effect before he flees up the cellar stairs."
> — `campaign/setting/notable-figures/xanathars-guild/07-thorvin-twinbeard.md:21` (the sentence before this one is also in section C)

**A4a. The quest-time recruitment text (Scene 1 of the Lair)**

This is the one place the campaign states how the party reaches the Harper channel. It is a quest mechanic, not day-one lore.

> "*Mirt (Harpers — renown 1+).* Thorvin Twinbeard is inside the lair — a Harper asset embedded in the lair's engineering staff for six years, Mirt's most carefully kept secret. Mirt provides Thorvin's location (X13, the workshop) and a recognition code: ask him what he thinks of the new pulley design. His response — "It'll hold if the load is distributed right" — confirms the channel. If Xanathar outposts were hit in **Faction Outposts**, Mirt warns that Thorvin's cover may be compromised: a gazer has been assigned to watch him, and Thorvin knows it. At renown 10+, Mirt arranges a Harper field agent — use the spy stat block — to stage a timed surface distraction above the guildsign entrance: a staged brawl that occupies Guild topside watchers for 20 minutes at a prearranged signal."
> — `campaign/structure/arc-f-xanathars-lair.md:31` (Scene 1, "The Lair Intelligence Briefing"; the gate is "renown 1+")

Adventure, the same channel, gated at a different renown (see D4):

> "{@creature Mirt|WDH} won't accompany the adventurers, but he knows a secret that could be helpful: {@creature Thorvin Twinbeard|wdh}, {@creature Xanathar|WDH}'s chief engineer, is a Harper informant. {@creature Mirt|WDH} shares this secret with any character who has renown of 4 or higher in the Harper faction."
> — `sources/adventure-wdh.json:15161` (the "Harpers" entry at `:15155`, page 101)

Wiki, the Harper roster line (edition key `WDH-p216`):

> "* [[Thorvin Twinbeard]], a Harper informant who held a notable position within [[Xanathar's Thieves' Guild]].<ref name="WDH-p216">{{Cite book/Waterdeep: Dragon Heist|216}}</ref>"
> — `sources/research/pass5-bundles/harpers/wiki.txt:473`

**A4b. Harper missions and the Harper quest folder**

No file under `campaign/quests/faction-events/harpers/` names Thorvin (see Not found). The two Guild-side informants the Harper missions do name are different people:

> "> - **Lantern**, Dena Holt: a courier for a Guild warehouse on the Dock Ward waterfront. She can report which crates go where, who carries them and when the guards change on her round. She never enters the lair and hears nothing said in a back room."
> — `campaign/quests/faction-events/harpers/r25-wise-owl/ev-01-wise-owl.md:153`

> "> - Learn how to send one request per quest to each of three informants inside the Guild, the Faire and the Splinter."
> — `campaign/quests/faction-events/harpers/r25-wise-owl/ev-01-wise-owl.md:8`

The Harper Factions Guide page names no Guild informant. Its Xanathar's Lair row covers Nihiloor, not Thorvin:

> "| **Xanathar's Lair** | Mirt wants Nihiloor dead — the mind flayer's intellect devourers have touched three Harper assets. He offers tactical support for the Xanathar lair heist if the party commits to eliminating Nihiloor. Nihiloor always escapes, so the support rests on a real attempt, not a kill. |"
> — `campaign/guides/factions/02-harpers.md:31`

The Harper Factions Guide page has no "Thorvin" and no "informant inside the Guild" (grep of `campaign/guides/factions/02-harpers.md`). The Guild's Factions Guide page, `campaign/guides/factions/09-xanathars-guild.md`, has no "Harper" at all.

Harper leak context (day-one; not Thorvin-specific, but it bears on whether a Harper's reports are safe):

> "**The Waterdeep cell is compromised.** Agents of the Splinter have infiltrated the Harpers' local network. Information shared with Harper contacts has a meaningful chance of reaching them. The Harpers do not know who leads the Splinter or where it is based."
> — `campaign/setting/organizations/01-harpers.md:56`

> "Mirt is hunting the leak in his own cell, because the Splinter has acted on information that moved only through Harper channels."
> — `campaign/setting/organizations/01-harpers.md:38` (rest of the bullet covers the Code)

Harper ("Ches 1, 1492 DR, the Harpers today"):

> "- **Ches 1, 1492 DR, the Harpers today:** Their primary concern in the current moment is the rivalry inside the Black Network and the ruthless newcomers they call the Splinter, which seems to act on Harper information. They are also alert to the Stone of Golorr — they believe it contains intelligence of strategic importance and want it in their hands."
> — `campaign/setting/organizations/01-harpers.md:31`

### A5. Work, pay and the pulverizer

Adventure, the workshop (keyed area X13, "X13. Thorvin's Workshop", header at `:17415`):

> "{@creature Thorvin Twinbeard|wdh} (see {@adventure appendix B|WDH|12}), {@creature Xanathar|WDH}'s engineer, is building a large contraption in the middle of the room. Floating nearby is an albino {@creature gazer|VGM} (see {@adventure appendix B|WDH|12})."
> — `sources/adventure-wdh.json:17423`

> "Other furnishings include a cot and a stack of wooden casks filled with Wyrmwizz Ale (a Skullport brew)."
> — `sources/adventure-wdh.json:17425`

> "When it is finished, Thorvin's contraption will enable {@creature Xanathar|WDH} to pulverize creatures that it petrifies, turning them into a fine powder that can be used to make plaster. The pulverizer consists mainly of a tall stone bin with grinding gears at the bottom, and a chute where the powdered stone pours out."
> — `sources/adventure-wdh.json:17443`

> "The pulverizer is a pet project of Thorvin's that allows him to hang around {@creature Xanathar|WDH}'s lair and gather information, which he sells to the Harpers. (Thorvin puts the coin he earns from the faction in a bank, far from the beholder's prying eyes.) If one or more characters approach him and claim to be Harpers, Thorvin is upset that they would risk exposing him as a spy, pointing to the albino gazer. If the characters befriend the gazer and promise to go away, Thorvin truthfully answers as many as three questions. He's never seen {@creature Ahmaergo|WDH}'s chambers (areas X11 and X12) but knows the rest of the lair well."
> — `sources/adventure-wdh.json:17444` (the sentences from "If one or more characters" onward are quest time; see C)

Wiki (edition key `WDH5e-p105`):

> "He lived inside the [[beholder]]'s lair. His pet project was a pulverizer to destroy for good the [[petrified]] victims of his master but he used it as cover to gather information to sell to the Harpers.<ref name="WDH5e-p105">{{Cite book/Waterdeep: Dragon Heist|105}}</ref>"
> — wiki-xg :69 (conflicts with the adventure on the pulverizer's purpose; see D6)

Campaign, the Lair doc (X13, daylight hours):

> "**X13 — Thorvin's Workshop.** Cluttered with mechanical components and active engineering projects. Thorvin works here during daylight hours. A gazer floats near the ceiling and watches him constantly. Thorvin communicates via encoded technical-sounding statements — "the third pulley from the north has a load problem" means the third guard station north of X1 is on elevated alert. The party extracts intelligence by asking about specific "mechanical issues." If the gazer is destroyed, Thorvin speaks openly, confirms Nihiloor's projects, and tells the party that the entity running the Guild is not the one making its decisions."
> — `campaign/structure/arc-f-xanathars-lair.md:151` (Scene 4 keyed areas; the last two sentences are quest time)

### A6. Where he lives and works

> "Thorvin works here during daylight hours." — `campaign/structure/arc-f-xanathars-lair.md:151` (quoted in full at A5)

> "He lived inside the [[beholder]]'s lair." — wiki-xg :69 (quoted in full at A5; wiki only)

> "Other furnishings include a cot and a stack of wooden casks filled with Wyrmwizz Ale (a Skullport brew)." — `sources/adventure-wdh.json:17425`

> "Thorvin will not evacuate himself. He has a family in the Trades Ward, and he intends to survive this." — `campaign/structure/arc-f-xanathars-lair.md:97` (quoted in full at A1)

Skullport meetings (campaign and adventure, both at A4).

### A7. Relationships to named figures

**Xanathar (the gazer, the question of loyalty).**

> "{@creature Xanathar|WDH} dreamed this gazer into existence and sent it to spy on Thorvin, whose loyalty the beholder is beginning to question. The gazer is itself disloyal. A wizard character can befriend it with a successful {@dc 11} Charisma (Persuasion) check and turn it into their familiar with a {@spell find familiar} ritual. When the gazer becomes a familiar, its alignment changes to match that of its new master."
> — `sources/adventure-wdh.json:17434` (keyed area X13, "Albino Gazer")

Campaign day-one, quoted at A4 (`campaign/setting/organizations/08-xanathars-guild.md:85`): "Xanathar has begun to question Thorvin's loyalty and has set a gazer to watch him (*Dragon Heist*, 5e)."

Wiki (edition key `WDH5e-p105`):

> "In truth, the gazer was spying on Thorvin under orders of the Xanathar, who suspected the dwarf.<ref name="WDH5e-p105" />"
> — wiki-xg :67

The Lair doc says the watcher is in place (`campaign/structure/arc-f-xanathars-lair.md:31`, quoted at A4a: "a gazer has been assigned to watch him, and Thorvin knows it.") and gives the gazer's quest-time reaction at `campaign/structure/arc-f-xanathars-lair.md:95` (see C).

**Nar'l Xibrindas (the secret room, the smokepowder).**

> "Neither {@creature Xanathar|WDH} nor its loyal underlings know this room exists. When Nar'l found it, he asked to have the adjoining room ({@area X35|2c7}) turned into his office so that he could keep this room secret. The only other individual who knows about this room is {@creature Thorvin Twinbeard|wdh}, {@creature Xanathar|WDH}'s chief engineer, but he's not inclined to tell the beholder about it."
> — `sources/adventure-wdh.json:18165` (keyed area X36, "X36. Secret Room", header at `:18143`)

> "{@creature Nar'l Xibrindas|wdh} has smuggled smokepowder into the lair (see {@area X36|2cb}) and, with {@creature Thorvin Twinbeard|wdh}'s help, identified areas that are structurally unstable. If these areas all suffer catastrophic damage, the lair collapses over the course of 1 hour. Characters can learn this information by speaking to Thorvin in {@area X13|28d}. The unstable areas are as follows:"
> — `sources/adventure-wdh.json:15091` (the "Destroy the Lair" entry, page 100)

Campaign, the Nar'l Notable Figures page:

> "With the help of **Thorvin Twinbeard**, the Guild's chief engineer, he has identified the structurally unstable parts of the lair (*Dragon Heist*, 5e)."
> — `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:20` (the sentence before it reads "...a secret room that neither Xanathar nor its underlings know exists.")

> "- **Thorvin Twinbeard:** The Guild's chief engineer. He is the only other person who knows about the secret room, and he helped Nar'l identify the unstable parts of the lair."
> — `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:37`

**Mirt (the Harper channel).** See A4 and A4a: `campaign/structure/arc-f-xanathars-lair.md:31` ("Mirt's most carefully kept secret") and `sources/adventure-wdh.json:15161`.

**Ahmaergo, Noska Ur'gray, Nihiloor, Ott Steeltoes.** No source gives Thorvin a stated relationship with any of them. The adventure says he has "never seen Ahmaergo's chambers (areas X11 and X12) but knows the rest of the lair well" (`sources/adventure-wdh.json:17444`). The Ott notes record that no source links Ott to Thorvin (`docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md`, F17). The Nihiloor link is quest time (`campaign/structure/arc-f-xanathars-lair.md:95`).

### A8. Signature belongings

> "Thorvin wears iron-rimmed spectacles and carries a large, heavy wrench that doubles as a club. He also carries mason's tools, {@item smith's tools|PHB}, and {@item thieves' tools|PHB}, and has proficiency with all three."
> — `sources/adventure-wdh.json:32618`

> "When it is finished, Thorvin's contraption will enable {@creature Xanathar|WDH} to pulverize creatures that it petrifies ..." — `sources/adventure-wdh.json:17443` (quoted in full at A5)

The voice profile gives him the phrase "the damned things" for his creations (`.claude/skills/character-voices/voices/xanathars-guild.md:124`, quoted in C).

### A9. Faith

None found. No source gives Thorvin a deity, a shrine or a rite. (Searched: the adventure entry at `:32604` to `:32636`, the campaign Notable Figures page, the voice profile, the wiki page.)

### A10. How long in post

See A2 (campaign: "nine years", `campaign/structure/arc-f-xanathars-lair.md:91`; derived about 1483 DR, not sourced) and A3 (wiki: "By this time", undated, `sources/research/pass5-bundles/xanathars-guild/wiki.txt:161`). The campaign's Notable Figures page does not state tenure as engineer.

### A11. Loyalty and flight in a fight (adventure, day one)

> "If combat breaks out in the cellar complex, {@creature Thorvin Twinbeard|wdh} flees up the stairs in {@area B8|1ea} and uses a key to unlock the door leading outside. He has no loyalty to the other creatures stationed here."
> — `sources/adventure-wdh.json:12006` (the "Mechanical Beholder" entry, page 86; the cellar complex is the Dragon Heist Spring event, see D7)

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, NF page: "*Dwarf engineer (secret Harper), neutral good, he/him*. Stat block: **Spy**." — `campaign/setting/notable-figures/xanathars-guild/07-thorvin-twinbeard.md:5`
- Campaign, Guild page: "- **Thorvin Twinbeard** — Dwarf engineer (secret Harper), neutral good. See the **Thorvin Twinbeard** page in Notable Figures." — `campaign/setting/organizations/08-xanathars-guild.md:106`
- Adventure: "Thorvin is lawful neutral." — `sources/adventure-wdh.json:32629` (inside the Game Statistics list, page 216)
- Wiki: "| alignment5e    = [[Lawful neutral]]" — wiki-xg :57 (key `WDH5e-p216`)

**Species**
- Campaign: "Dwarf engineer" (NF `:5`, Guild `:106`)
- Adventure: "Thorvin is a shield dwarf {@creature commoner}, with these changes:" — `sources/adventure-wdh.json:32625`
- Wiki: "| race           = [[Dwarf]]" (wiki-xg :14); "| ethnicity      = [[Shield dwarf]]" (wiki-xg :15)
- Alexandrian stat reference **[PDF transcription]**: "Thorvin Twinbeard – dwarven commoner, MM p. 345 (DH p. 216)" — `sources/11. Lair  Xanathar’s Lair.pdf`, printed p.91 [PDF p.9]

**Pronouns**
- Campaign, NF page: "he/him" (`campaign/setting/notable-figures/xanathars-guild/07-thorvin-twinbeard.md:5`)
- Campaign, Lair doc: "Thorvin will not evacuate himself. He has a family in the Trades Ward, and he intends to survive this." — `campaign/structure/arc-f-xanathars-lair.md:97`
- Adventure: "He has no loyalty to the other creatures stationed here." — `sources/adventure-wdh.json:12006`; "but he's not inclined to tell the beholder about it." — `sources/adventure-wdh.json:18165`
- Wiki: "| sex            = Male" — wiki-xg :13

**Stat block**
- Campaign, NF page: "Stat block: **Spy**." — `campaign/setting/notable-figures/xanathars-guild/07-thorvin-twinbeard.md:5`. No source gives Thorvin a Spy stat block (see D2).
- Adventure: "Thorvin is a shield dwarf {@creature commoner}, with these changes:" — `sources/adventure-wdh.json:32625`
- Alexandrian: "Thorvin Twinbeard – dwarven commoner, MM p. 345 (DH p. 216)" **[PDF transcription]**, `sources/11. Lair  Xanathar’s Lair.pdf` printed p.91 [PDF p.9]
- Wiki: "| class5e        = [[Commoner]]" — wiki-xg :59

**Racial traits and ability (adventure)**
> "He has these racial traits: His walking speed is 25 feet. He has advantage on saving throws against poison and resistance to poison damage. He has darkvision out to a range of 60 feet. He speaks Common and Dwarvish."
> — `sources/adventure-wdh.json:32630`

> "He has an Intelligence of 16 (+3)."
> — `sources/adventure-wdh.json:32631`

Wiki languages: "| languages      = [[Common]], [[Dwarvish]]" (wiki-xg :19).

**Index entries**: "82. Thorvin Twinbeard" — `sources/adventure-wdh.json:32981`. The entry opens with `"name": "Thorvin Twinbeard"` and `"page": 216` at `:32604` to `:32605`.

**Harper label (the NF page's Affiliation)**
- "- **Affiliation:** Xanathar's Guild (secretly Harpers)" — `campaign/setting/notable-figures/xanathars-guild/07-thorvin-twinbeard.md:6`
- Harpers organization: "a secret Harper informant" (`campaign/setting/organizations/01-harpers.md:64`), the singular form.

**Voice profile**: the profile has no pronoun line. Its tagline carries the duration conflict in D3: "*An irritable dwarf engineer who hates his work and has been waiting three years for someone to tell.*" — `.claude/skills/character-voices/voices/xanathars-guild.md:120`.

---

## C. Sentences on the current page that narrate quest time, or a day-one conflict

"Day-one" means the sentence can stand on Ches 1, 1492 DR with its source. "Quest time" means it narrates a Lair or other quest event (a gazer's death, a smokepowder plan, a rescue, a flight during a fight, a reveal). Where a sentence is partly one and partly the other, both are listed.

**Summary and header (`07-thorvin-twinbeard.md`)**

| Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|
| L5 | "*Dwarf engineer (secret Harper), neutral good, he/him*. Stat block: **Spy**." | Day-one; alignment and stat block conflict (D1, D2) | Guild `:106`; adventure `:32629`, `:32625`; wiki-xg :57, :59 |
| L6 | "- **Affiliation:** Xanathar's Guild (secretly Harpers)" | Day-one. "secretly Harpers" (plural) is a label; the source says "a secret Harper informant" (`01-harpers.md:64`) | Guild `:106` |
| L7 | "- **Featured in:** **Faction Outposts**, **Xanathar's Lair**" | "Xanathar's Lair": supported (`arc-f-xanathars-lair.md:31`, `:91`). "Faction Outposts": **no support found** (see E1) | Lair: `arc-f-xanathars-lair.md:31`. Faction Outposts: none |

**Roleplaying Information**

| Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|
| L11 | "**Resonance.** Thorvin should inspire initial wariness with his mechanical work for Xanathar; growing sympathy when his reluctance becomes visible; and genuine trust when he turns out to be the inside man." | The first clause is day-one. "genuine trust when he turns out to be the inside man" is a quest-time reveal | Reveal: `campaign/structure/arc-f-xanathars-lair.md:95` ("If the gazer is destroyed (13 HP, AC 13), Thorvin speaks openly for the first time.") |
| L13 | "**Emotions.** Thorvin most often feels the specific stress of doing terrible work because the alternative is worse, genuine engineering pride he wishes he could direct at anything else, cautious hope when the party appears, and relief at finally having someone useful to tell about the smokepowder." | "stress of doing terrible work" and "engineering pride" are day-one (the pulverizer, `sources/adventure-wdh.json:17443`). "cautious hope when the party appears" and "relief at finally having someone useful to tell about the smokepowder" are quest time. The adventure's reaction to a party that claims Harper ties is "upset" (`sources/adventure-wdh.json:17444`). The Lair doc gives the relief: "His relief is immediate and genuine." (`arc-f-xanathars-lair.md:95`) | `arc-f-xanathars-lair.md:95`; `sources/adventure-wdh.json:17444` |
| L15 | "**Motivations.** Thorvin wants to survive long enough for someone to take down the Lair, pass intelligence through Harper channels, and never finish the pulverizer if he can help it." | "pass intelligence through Harper channels" and "never finish the pulverizer" are day-one (`sources/adventure-wdh.json:17444`, `:17443`). "someone to take down the Lair" is a quest-outcome motive (`arc-f-xanathars-lair.md:111`: "Nar'l and Thorvin must be evacuated or they die."); "he intends to survive this" is at `arc-f-xanathars-lair.md:97` | `arc-f-xanathars-lair.md:97`, `:111` |
| L17 | "**Inspirations.** When playing Thorvin, channel Geppetto (*Pinocchio*), Scotty (*Star Trek*), and Hank Schrader (*Breaking Bad*, the reluctant insider)." | Not a fact | n/a |

**Character Information**

| Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|
| L21 (a) | "**Persona.** To the world, Thorvin is an irritable dwarf engineer building mechanical horrors for Xanathar and taking no questions about his methods." | Day-one | `sources/adventure-wdh.json:17423` ("building a large contraption"), `:32617` |
| L21 (b) | "To those who earn his trust, he has been a Harper informant for three years," | Day-one tie; duration conflicts (D3) | `arc-f-xanathars-lair.md:31`, `:91` (six years) |
| L21 (c) | "knows exactly where Nar'l Xibrindas hid the smokepowder," | Day-one knowledge. The cache is pre-campaign: "Nar'l smuggled eight smokepowder kegs into a concealed cache in Area X36 over four months." (`arc-f-xanathars-lair.md:107`); the adventure says "Twenty kegs of smokepowder" (`sources/adventure-wdh.json:18162`; D5) | `arc-f-xanathars-lair.md:107`; `sources/adventure-wdh.json:15091`, `:18165`; `03-narl-xibrindas.md:20` |
| L21 (d) | "and will tell the party where to place it for maximum effect before he flees up the cellar stairs." | **Quest time.** The telling is a Lair action ("Thorvin also tells them where to plant the smokepowder to cause the most damage (see "Destroy the Lair")."). The flight is the Spring cellar event (B8), not the Lair | `sources/adventure-wdh.json:17445`; `arc-f-xanathars-lair.md:93`, `:109`; flight `sources/adventure-wdh.json:12006` |
| L21 (e) | "Deep down, Xanathar has sent a gazer to watch him, and Thorvin knows it, and the gazer knows Thorvin knows it." | First half is day-one (`sources/adventure-wdh.json:17434`; `arc-f-xanathars-lair.md:91`: "He knows it is there."). "and the gazer knows Thorvin knows it" has **no source** (gap F9) | `sources/adventure-wdh.json:17434` |
| L23 | "**Morale.** In a fight, Thorvin flees immediately through whichever stairs lead outside. He does not die for his employer." | Day-one trait, sourced from the cellar entry (`sources/adventure-wdh.json:12006`), which is the Spring cellar event (D7). The Lair doc has no flight line for him | `sources/adventure-wdh.json:12006` |
| L25 | "**Relationships.** Thorvin is an engineer of Xanathar's Guild, a secret Harper informant, the man who maintains the Lair's mechanical constructs and traps (and knows every failure condition), and the reason the smokepowder demolition option is viable." | "engineer of Xanathar's Guild" and "maintains the Lair's mechanical constructs and traps" are day-one (`sources/adventure-wdh.json:32617`; `arc-f-xanathars-lair.md:91`). "(and knows every failure condition)" has **no source**; the nearest is "a hand-drawn schematic of every mechanical trap in the service corridors" (`arc-f-xanathars-lair.md:93`, quest time). "the reason the smokepowder demolition option is viable" is **quest time** | `arc-f-xanathars-lair.md:93`, `:107`, `:109`, `:171` |
| L29 | "Thorvin Twinbeard is an irritable dwarf engineer employed by Xanathar's Guild to maintain its mechanical constructs and devices. He takes no questions about his methods or his employers." | Day-one; fits the public face | `sources/adventure-wdh.json:32617`; `08-xanathars-guild.md:43` |

**Voice profile (`.claude/skills/character-voices/voices/xanathars-guild.md`, lines 119 to 133)**

> "*An irritable dwarf engineer who hates his work and has been waiting three years for someone to tell.*" — `:120`
> Quest time: "for someone to tell" (the reveal, `arc-f-xanathars-lair.md:95`). Duration conflicts with D3 ("three years" against "six").

> "**Sound:** A gruff, grumbling dwarven voice that drops to a hurried whisper around the gazer." — `:122`
> Day-one (the gazer, `sources/adventure-wdh.json:17434`).

> "**Sentence shape:** Short, irritable brush-offs in public. In private, rushed technical instructions, precise and grateful." — `:123`
> "In private, rushed technical instructions" is quest time (the instructions are the Lair advice, `sources/adventure-wdh.json:17445`). The rest is day-one.

> "**Word choice:** Engineering: tolerances, pressure, "load", "smokepowder". Harper code words when safe. He calls his creations "the damned things"." — `:124`
> Day-one. The Lair recognition code (`arc-f-xanathars-lair.md:31`) is not in the profile.

> "**Swearing:** *Casual · Pearls · Phrase.* Mostly dwarven grumbling, then a gem: "I've built things for gods-cursed madmen before, but never one who'd wear the result as a hat."" — `:125`
> Day-one speech. "the result as a hat" is a reference to Ott's eyestalk hat (`campaign/setting/notable-figures/xanathars-guild/06-ott-steeltoes.md:29`, "a hat fashioned from a beholder's dried eyestalks"; see the Ott notes D7 for the "dried" versus "fake" conflict). Flag for the drafter.

> "**Personality in speech:** Stressed and reluctant. His engineering pride sneaks through even about terrible machines. Hope makes him talk fast." — `:126`
> Day-one.

> "**Quirks:** He glances at the gazer and changes the subject mid-sentence. He calls the pulverizer "unfinished", pointedly." — `:127`
> Day-one (gazer; the pulverizer, `sources/adventure-wdh.json:17443`).

> "**Signature phrases:** "No questions." / "Unfinished. Deliberately." / "Place it there, and run."" — `:128`
> "No questions." and "Unfinished. Deliberately." are day-one. **"Place it there, and run." is quest time** (the placement is a Lair plan, `arc-f-xanathars-lair.md:107`, `:109`).

> "**Never:** He never finishes the pulverizer, never talks openly with the gazer present, and never stays for the explosion." — `:129`
> The first two are day-one (`sources/adventure-wdh.json:17443`, `:17434`). "never stays for the explosion" is quest time (the smokepowder plan, `arc-f-xanathars-lair.md:111`).

> "*Greeting:* "No questions. I don't answer questions. Go away."" — `:131`
> Day-one.

> "*Business (privately):* "Nar'l hid the smokepowder behind the third cistern. Put it against the north pillar, and you'll bring the whole damned hall down."" — `:132`
> **Quest time** (advice on placement). "behind the third cistern" and "the north pillar" have **no source** anywhere in the repo (grep for "third cistern" and "north pillar" finds only this voice line). "Nar'l hid the smokepowder" is supported (`sources/adventure-wdh.json:15091`).

> "*Under pressure:* "That's my cue. Good luck, and fuck this place."" — `:133`
> **Quest time** (a parting line to the party in a fight). The flight is supported (`sources/adventure-wdh.json:12006`); the speech is not.

---

## D. Conflicts (both sides quoted, higher-ranked source named)

**D1. Alignment: "neutral good" against "lawful neutral"**
- Campaign NF page: "*Dwarf engineer (secret Harper), neutral good, he/him*. Stat block: **Spy**." — `campaign/setting/notable-figures/xanathars-guild/07-thorvin-twinbeard.md:5`
- Campaign Guild page: "- **Thorvin Twinbeard** — Dwarf engineer (secret Harper), neutral good." — `campaign/setting/organizations/08-xanathars-guild.md:106`
- Adventure: "Thorvin is lawful neutral." — `sources/adventure-wdh.json:32629`
- Wiki: "| alignment5e    = [[Lawful neutral]]" — wiki-xg :57
- Higher source: the campaign (neutral good, on both campaign pages). The adventure and the wiki say lawful neutral. No campaign file explains the change. Orchestrator's call.

**D2. Stat block: "Spy" against "commoner"**
- Campaign NF page: "Stat block: **Spy**." — `campaign/setting/notable-figures/xanathars-guild/07-thorvin-twinbeard.md:5`
- Adventure: "Thorvin is a shield dwarf {@creature commoner}, with these changes:" — `sources/adventure-wdh.json:32625`
- Alexandrian **[PDF transcription]**: "Thorvin Twinbeard – dwarven commoner, MM p. 345 (DH p. 216)" — `sources/11. Lair  Xanathar’s Lair.pdf` printed p.91 [PDF p.9]
- Wiki: "| class5e        = [[Commoner]]" — wiki-xg :59
- Campaign context: Spy is used for other figures. "Corene uses the **Spy** stat block while the custom **Occupying Devourer** rides her." (`campaign/quests/faction-events/harpers/m05-the-sleeping-asset/overview.md:10`) and "use the spy stat block" for a Harper field agent (`campaign/structure/arc-f-xanathars-lair.md:31`).
- Higher source: the campaign label is the only "Spy" in the record. No file gives Thorvin the Spy block. The adventure, the Alexandrian stat reference and the wiki agree on commoner. Orchestrator's call.

**D3. Years as a Harper informant: "three" against "six"**
- Campaign NF page: "To those who earn his trust, he has been a Harper informant for three years," — `campaign/setting/notable-figures/xanathars-guild/07-thorvin-twinbeard.md:21`
- Campaign NF voice tagline: "has been waiting three years for someone to tell." — `.claude/skills/character-voices/voices/xanathars-guild.md:120`
- Campaign Lair structure doc: "served as a Harper informant for six." — `campaign/structure/arc-f-xanathars-lair.md:91`
- Campaign Lair structure doc: "a Harper asset embedded in the lair's engineering staff for six years" — `campaign/structure/arc-f-xanathars-lair.md:31`
- Harpers organization page, already flagged: "> - **Conflicts:** Thorvin's service. `campaign/structure/arc-f-xanathars-lair.md:91` says six years as a Harper informant and his Notable Figures page (`:21`) says three. The page gives no figure." — `campaign/setting/organizations/01-harpers.md:182`
- Higher source: the Lair structure doc is authoritative for the Lair until the Lair journal exists (`CLAUDE.md`, Workspace Structure). The NF page is the day-one figure page. Both are campaign files. Orchestrator's call. The adventure and the wiki give no duration.

**D4. The Harper gate: "renown 1+" against "renown of 4 or higher"**
- Campaign Lair doc: "*Mirt (Harpers — renown 1+).*" — `campaign/structure/arc-f-xanathars-lair.md:31`
- Adventure: "{@creature Mirt|WDH} shares this secret with any character who has renown of 4 or higher in the Harper faction." — `sources/adventure-wdh.json:15161`
- Higher source: the campaign. The gate is a quest-time mechanic and is routed (section E).

**D5. Smokepowder kegs in X36: "eight" against "Twenty"**
- Campaign Lair doc: "*The Smokepowder Option.* Nar'l smuggled eight smokepowder kegs into a concealed cache in Area X36 over four months." — `campaign/structure/arc-f-xanathars-lair.md:107`
- Campaign Lair doc: "**X36 — Smokepowder Cache.** A sealed maintenance alcove marked on Thorvin's schematic as "decommissioned drainage junction." Eight smokepowder kegs wrapped in Guild-color cloth." — `campaign/structure/arc-f-xanathars-lair.md:171`
- Adventure, the "Secret Room" (header at `sources/adventure-wdh.json:18143`): "Twenty kegs of smokepowder are neatly stacked in the middle of the room." — `sources/adventure-wdh.json:18162`
- Higher source: the campaign (eight). The adventure's room is "X36. Secret Room" and the campaign's is "Smokepowder Cache", a different description. Orchestrator's call on whether the NF page names a count (it does not).

**D6. The pulverizer's purpose: "petrified victims" against "make plaster"**
- Wiki: "His pet project was a pulverizer to destroy for good the [[petrified]] victims of his master" — wiki-xg :69 (edition key `WDH5e-p105`)
- Adventure: "to pulverize creatures that it petrifies, turning them into a fine powder that can be used to make plaster." — `sources/adventure-wdh.json:17443`
- Higher source: the adventure (wiki is last). The campaign page gives no purpose.

**D7. Where Thorvin works on the mechanical beholder**
- Adventure, cellar entry: "3 {@creature duergar} and 1 {@creature gazer|vgm} (see {@adventure appendix B|WDH|12}) standing guard while {@creature Thorvin Twinbeard|wdh} (see {@adventure appendix B|WDH|12}) works on a mechanical beholder (see "Mechanical Beholder" below)" — `sources/adventure-wdh.json:11983` (row "B7")
- Adventure, the cellar's place: "Cellars and sewer tunnels intersect to create small dungeons under Waterdeep." (`sources/adventure-wdh.json:10691`), and "The characters have learned that a halfling necromancer named {@creature Losser Mirklav|wdh} took the {@item Stone of Golorr|WDH}. He lives in a cellar complex under a powdered wig shop in the Trades Ward. The shop, Dandymops, is closed and locked with an iron gate." — `sources/adventure-wdh.json:11837` (the "Cellar Complex: Spring" event, page 85)
- Campaign, the sewer hideout's B7: "Area B7 – Mechanical Beholder: Mixed in with the other material in this room is a letter." **[PDF transcription]** — `sources/5. Faction Outposts.pdf` printed p.44 [PDF p.8]. The campaign key `arc-e-faction-outposts.md:183` says: "Area B7: *On the Delivery of a Mechanical Beholder* from Ahmaergo, setting a delivery deadline of Tarsakh 9th for a mechanical beholder to Terasse Estate".
- Campaign, Thorvin's day-one workshop: "**X13 — Thorvin's Workshop.**" — `campaign/structure/arc-f-xanathars-lair.md:151`; the adventure's is "X13. Thorvin's Workshop" (`sources/adventure-wdh.json:17415`). These agree.
- Wiki: "In [[1492 DR]],{{WDH-time}} he was working on a mechanical [[beholder]] while three [[duergar]] and one [[gazer]] protected him." — wiki-xg :67
- Conflict: the adventure puts Thorvin's mechanical beholder in cellar B7, which is a Dragon Heist Spring event under a Trades Ward shop. The campaign's B7 is a room in the Xanathar Sewer Hideout, and the campaign gives Thorvin no role in it. Not resolved. The campaign also leaves the Spring cellar out on purpose: "> - **Left out:** Cuttle's Meat Pies, Dandymops, Elaspra Ulmarr's lock shop, Losser Mirklav and Bepis Honeymaker are published sites and NPCs for Stone-trail variants that no campaign file uses." — `campaign/gazetteer/waterdeep/trades-ward.md:260` (the bullet continues past that sentence). The campaign page should not place the build anywhere it does not state.

**D8. Appointment date (not a flat conflict)**
- Wiki: "By this time, Zushaxx had also appointed [[Thorvin Twinbeard]]..." — `sources/research/pass5-bundles/xanathars-guild/wiki.txt:161`, undated.
- Campaign: "maintained the lair's mechanical infrastructure for nine years" — `campaign/structure/arc-f-xanathars-lair.md:91`. Derived, not sourced: about 1483 DR.
- Not a conflict unless the drafter dates the hire. The wiki is last-ranked.

**D9. Entry route (SOURCE_GUIDE against the Alexandrian)**
- Source guide: "- Entry approaches: gladiatorial tournament (undercover as fighters), sewer infiltration, slave rescue mission (buying/freeing captives gives access), Thorvin Twinbeard's Harper informant route" — `sources/SOURCE_GUIDE.md:341` (under "### `11. Lair  Xanathar's Lair.pdf`", `:335`)
- Alexandrian Lair **[PDF transcription]**, printed p.86 [PDF p.4]: "Generally speaking, there are three methods of entry to Xanathar's Lair. You can come in the secret entrance (X1), you can try to sneak in from Skullport (X4), or you can be brought in as part of the audience for the gladiatorial games (also via X4, but almost certainly arriving in X6 before you'll have a chance to slip away)."
- No Thorvin route is in the three methods or anywhere else in the nine PDF pages. The SOURCE_GUIDE line has no PDF support. The adventure gives Thorvin a route as a Mirt tip (`sources/adventure-wdh.json:15161`).

**D10. Arena percentages (within the Alexandrian, transcription)**
- Printed p.90 [PDF p.8], "THE ARENA CROWD:" list **[PDF transcription]**: "Thorvin Twinbeard (01-50%)"
- Printed p.90 [PDF p.8], adventure roster **[PDF transcription]**: "Thorvin Twinbeard (51-00%)", next to "Area X13 – Thorvin's Workshop"
- Not resolved; likely two rolls in one table. Check with pdftotext before any use.

**D11. Harper ties in the Lair doc against the Factions Guide**
- The Harper Factions Guide Xanathar's Lair row names no Thorvin (`campaign/guides/factions/02-harpers.md:31`), while the Lair doc's Scene 1 names him as Mirt's channel (`arc-f-xanathars-lair.md:31`). This is an omission, not a conflict. Noted for the drafter.

---

## E. Stale lines in other files (not to be edited), and routed quest references

### E1. Lines on this page with no source
- `campaign/setting/notable-figures/xanathars-guild/07-thorvin-twinbeard.md:7`: "- **Featured in:** **Faction Outposts**, **Xanathar's Lair**". Searched `campaign/structure/arc-e-faction-outposts.md` (Thorvin, Twinbeard, engineer, informant: the hits at `:183`, "engineering operations", and `:495`, "Harper informants", name no Thorvin), `sources/5. Faction Outposts.pdf` (PDF pp.1 to 13, read in full: no Thorvin; the Xanathar outposts are printed pp.42 to 45), and all `campaign/quests/` files (no Thorvin). The Faction Outposts quest journal does not exist yet.
- `campaign/structure/arc-e-faction-outposts.md:183` (for context, the Guild's engineering link): "Area B7: *On the Delivery of a Mechanical Beholder* from Ahmaergo, setting a delivery deadline of Tarsakh 9th for a mechanical beholder to Terasse Estate — confirms the gladiatorial supply chain and ties Ahmaergo to Xanathar's engineering operations."
- `campaign/structure/arc-e-faction-outposts.md:495` (the Harper hook; informants unnamed): "Once the party reaches Renown 30+, Mirt can direct embedded Harper informants to provide advance intelligence against Xanathar and Manshoon outposts — shift rotations, guard counts, unusual personnel — delivered before each operation rather than discovered during it."

### E2. Quest-time text that already lives in quest-side files
- Lair Scene 1, the Harper channel: `campaign/structure/arc-f-xanathars-lair.md:31` (quoted at A4a).
- Lair Scene 3, "Inside Ally: Thorvin Twinbeard (X13)": `campaign/structure/arc-f-xanathars-lair.md:91`, `:93`, `:95`, `:97` (quoted in A1, A2, C).
- Lair, the smokepowder plan: `campaign/structure/arc-f-xanathars-lair.md:107`, `:109`, `:111` (quoted in C and D5).
- Lair Scene 6 (Mirt's aftermath line): `campaign/structure/arc-f-xanathars-lair.md:294`: "- **Mirt:** "Is Thorvin alive?" Genuine concern. Then: "What did you find in the beholder's private rooms?" He suspects Nihiloor. He does not say so directly."
- Lair design note, the dream nullifier through Thorvin's guidance: `campaign/structure/arc-f-xanathars-lair.md:372`: "A party that found the dream nullifier through Thorvin's guidance or onsite reconnaissance has a tool: destroy it, wait three minutes, follow Xanathar out of the room, and extract the Eye with four minutes of silence."
- Lair Scene 2, the dream nullifier: `campaign/structure/arc-f-xanathars-lair.md:77`: "A party that found X20 through reconnaissance or Thorvin's guidance has a clean extraction opportunity."
- Lair design note, the loss if the lair is destroyed: `campaign/structure/arc-f-xanathars-lair.md:400` (the sentence names "Nar'l and Thorvin killed unless the party explicitly evacuates them").
- Lair, the Notable Figures list: `campaign/structure/arc-f-xanathars-lair.md:339`: "- **Notable Figures** — Full NPC profiles for Xanathar, Ahmaergo, Nar'l Xibrindas, Nihiloor, Noska Ur'gray, Ott Steeltoes, Thorvin Twinbeard, Keln Trigos, Grinda Garloth, Korgstrod Uxgulm, Gorath."
- Adventure, the Mirt channel (renown gate): `sources/adventure-wdh.json:15161` (D4).
- Adventure, the Harper approach at the workshop: `sources/adventure-wdh.json:17444` (sentences from "If one or more characters approach him..." onward).
- Adventure, the placement advice: `sources/adventure-wdh.json:17445`: "If the characters are looking for a way to mess with {@creature Xanathar|WDH}'s operation, Thorvin suggests they coerce {@creature Nar'l Xibrindas|wdh}, the beholder's advisor (see {@area X18|29a}), into giving them the large supply of {@item smokepowder|WDH} that he smuggled into the dungeon. Thorvin also tells them where to plant the {@item smokepowder|WDH} to cause the most damage (see "Destroy the Lair")."
- Adventure, the collapse entry: `sources/adventure-wdh.json:15087` ("Destroy the Lair", page 100).
- Adventure, the Spring cellar event (Losser Mirklav, Trades Ward): `sources/adventure-wdh.json:11837`, `:11983`, `:12006`.

### E3. Stale or conflicting lines in other files
- `campaign/structure/arc-f-xanathars-lair.md:31`: "for six years" and "renown 1+" (the Lair doc disagrees with the NF page's "three years" and with the adventure's "renown of 4 or higher"; D3, D4).
- `campaign/structure/arc-f-xanathars-lair.md:171`: "Eight smokepowder kegs" against the adventure's "Twenty kegs" (`sources/adventure-wdh.json:18162`; D5).
- `campaign/setting/organizations/01-harpers.md:182`: already flags the "three" against "six" conflict and gives no figure.
- `docs/plans/setting-compendium-research-notes/pass5/harpers.md:547` and `:565` carry "six" and "three" as research notes (not sources; not edited).
- `campaign/setting/organizations/08-xanathars-guild.md:161`: the Guild page's Cross-References list for the principal members omits Thorvin ("**Xanathar**, **Ahmaergo**, **Nar'l Xibrindas**, **Nihiloor**, **Noska Ur'gray**, **Ott Steeltoes**, **Keln Trigos**, **Grinda Garloth**, **Korgstrod Uxgulm**, **Gorath** (Notable Figures): the principal members"). Thorvin is named in the Structure paragraph (`:43`) and the Key Members list (`:106`) but not here.
- `sources/SOURCE_GUIDE.md:341`: the Harper route (D9).
- `sources/SOURCE_GUIDE.md:29`: "Thorvin Twinbeard (Harper informant)" under Chapter 5. This is consistent with the adventure.
- `.claude/skills/character-voices/voices/xanathars-guild.md:120`: "three years" (D3); `:128`, `:129`, `:132`, `:133` quest-time clauses (section C).
- `campaign/setting/organizations/08-xanathars-guild.md:85`: the Guild page says "Xanathar has begun to question Thorvin's loyalty", which is day-one and consistent with the adventure (`sources/adventure-wdh.json:17434`).

### E4. Other facts that a drafter might pick up by mistake
- `campaign/setting/geography/undermountain-and-skullport.md:140`: "- **Durnan**, **Ryvarra**, **Xanathar**, **Nihiloor**, **Thorvin Twinbeard**, **Meloon Wardragon**, **Jeryth Phaulkon**, **Manshoon**, **Laeral Silverhand**, **Vajra Safahr** and **Mattrim Mereg**: the people named above." This is a cross-reference list, not a fact.
- Alexandrian Lair printed p.83 [PDF p.1] (not Thorvin-specific; a Guild conflict for the Guild drafter): "Xanathar stole the *Stone of Golorr* from Lord Neverember and he stole one of the three Eyes from the Zhentarim. Then he lost the *Stone* when Dalakhar took it from him." **[PDF transcription]** The campaign's Stone sequence is routed to quests (`campaign/setting/organizations/08-xanathars-guild.md:176`).

---

## F. Gaps (what a Background would need that no source gives)

For each gap, the suggested inference is for the drafter, tagged `[research]`. None is an invented plot fact. Where the sources already give a choice, the choice goes to the orchestrator.

1. **Birth, family name, home town, upbringing, training.** No source. The only family fact is "He has a family in the Trades Ward" (`campaign/structure/arc-f-xanathars-lair.md:97`). Suggested inference: none beyond that line, or a `[research]` note that the family is in the Trades Ward without names.
2. **Clan and trade training.** The adventure gives "shield dwarf" and the tools (`sources/adventure-wdh.json:32618`). Suggested inference: the tools (mason's, smith's, thieves') fit a trained craftsman; `[research]`.
3. **How and when he was hired by the Guild.** Wiki only: "appointed" under Zushaxx (`sources/research/pass5-bundles/xanathars-guild/wiki.txt:161`). Campaign: "nine years" as engineer (`arc-f-xanathars-lair.md:91`, derived about 1483 DR). Suggested inference: hired in the Zushaxx era, when the campaign already has Zushaxx as the beholder (`campaign/setting/organizations/08-xanathars-guild.md:21`); `[research]`.
4. **How and when he became a Harper informant, and who recruited him.** No source names a recruiter. The duration conflicts (D3). The campaign does name who holds the channel: Mirt ("Mirt's most carefully kept secret", `campaign/structure/arc-f-xanathars-lair.md:31`; "Mirt ... knows a secret", `sources/adventure-wdh.json:15161`). Suggested inference: Mirt is his handler; `[research]`. The orchestrator picks the duration.
5. **Why he informs.** The adventure gives pay: "Thorvin puts the coin he earns from the faction in a bank, far from the beholder's prying eyes." (`sources/adventure-wdh.json:17444`). The NF page's "the alternative is worse" (`campaign/setting/notable-figures/xanathars-guild/07-thorvin-twinbeard.md:13`) names no alternative. Suggested inference: money plus the family in the Trades Ward; `[research]`. Do not name a threat.
6. **When Xanathar's suspicion began.** Only "beginning to question" (`sources/adventure-wdh.json:17434`). Suggested inference: none needed; keep the sources' wording.
7. **Whether Xanathar knows Thorvin is a Harper.** Not stated. The sources give suspicion and a gazer. Suggested inference: suspicion only, matching `campaign/setting/organizations/08-xanathars-guild.md:85`.
8. **Relationship with Ahmaergo, Noska Ur'gray, Nihiloor.** No source gives one, except "never seen Ahmaergo's chambers" (`sources/adventure-wdh.json:17444`). Suggested inference: none; leave the Connections list to the sources.
9. **"Knows every failure condition" and "the gazer knows Thorvin knows it".** No source. The campaign's schematic is "of every mechanical trap in the service corridors" (`arc-f-xanathars-lair.md:93`, quest time). Suggested inference: drop the "every failure condition" wording, or mark `[research]`.
10. **Faith.** None (A9). Suggested inference: none; the adventure gives no deity for him.
11. **Age and lifespan.** None.
12. **Where he lives.** "He lived inside the beholder's lair" (wiki, `wiki-xg :69`) and the cot in X13 (`sources/adventure-wdh.json:17425`). The family is in the Trades Ward (`arc-f-xanathars-lair.md:97`). Suggested inference: lives in the lair with a cot; family elsewhere; `[research]` for the "lived" wording, which is wiki only.
13. **The Skullport meeting place.** The campaign says he "holds secret meetings with Harper spies in Skullport" (`campaign/setting/geography/undermountain-and-skullport.md:93`), and the same line names Dalagor's Fortress as a Harper hideout. No source ties the meetings to the fortress. Suggested inference: `[research]` only, if at all.
14. **The 1492 DR mechanical beholder.** Wiki (`wiki-xg :67`) and the adventure's cellar B7 (`sources/adventure-wdh.json:11983`) agree he works on one. The campaign has no Thorvin role in it (D7). Suggested inference: omit from the day-one page, or say he is "building a large contraption" (`sources/adventure-wdh.json:17423`) in X13, which the campaign's Lair doc also supports (`arc-f-xanathars-lair.md:151`).
15. **Pulverizer purpose.** The adventure (plaster) and the wiki (destroy petrified victims) differ (D6). Suggested inference: use the adventure.
16. **The Harper code words.** The voice profile says "Harper code words when safe" (`voices/xanathars-guild.md:124`). The one code in the sources is the Lair's recognition exchange, a quest mechanic (`arc-f-xanathars-lair.md:31`). Suggested inference: keep the generic phrase; do not use the quest code on the day-one page.
17. **Stat block for Thorvin.** No file gives a Spy block (D2). Suggested inference: `commoner` from the adventure, with the `Spy` label routed to the orchestrator.

---

## Not found

Searches and reads, with the terms and files tried:

- Grep for `Thorvin|Twinbeard` across the whole repository (`/home/user/waterdeep`, all file types): 168 hits in 46 files. Campaign files with hits: `campaign/setting/notable-figures/xanathars-guild/07-thorvin-twinbeard.md` (9), `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md` (2, found with a case-insensitive search), `campaign/setting/organizations/01-harpers.md` (4), `campaign/setting/organizations/08-xanathars-guild.md` (3), `campaign/setting/geography/undermountain-and-skullport.md` (3), `campaign/structure/arc-f-xanathars-lair.md` (15). No hits in `campaign/quests/`, `campaign/guides/`, `campaign/gazetteer/`, `campaign/setting/villains/`, `campaign/setting/history/`, `campaign/setting/lore/`, `campaign/structure/arc-e-faction-outposts.md`, or `campaign/setting/notable-figures/harpers/`.
- Grep for `Harper` in `campaign/guides/factions/09-xanathars-guild.md`: no match.
- Grep for `Xanathar|Lair|informant|Thorvin|Guild` in `campaign/guides/factions/02-harpers.md`: only the Lair row (`:31`), the Guild rival lines and the Mirt rows. No Thorvin.
- Grep for `Harper` in `campaign/setting/villains/xanathar.md`, `campaign/setting/the-grand-game/*.md`, `campaign/setting/history/02-the-long-shadow.md`, `campaign/guides/gm-guide/running-the-villains.md`, `campaign/setting/lore/*.md`, `campaign/gazetteer/waterdeep/dock-ward.md`, `trades-ward.md` and `castle-ward.md`: no Thorvin and no Harper-informant line about him.
- Grep for `Xanathar|Guild|informant|lair|Lair` in `.claude/skills/character-voices/voices/harpers*.md`: no match. The Harper voice profiles say nothing about the Guild.
- Grep for `Xanathar|lair|Lair` in `campaign/setting/notable-figures/harpers/`: only Mirt's Featured-in list (`01-mirt.md:7`) and Corene's Relationships (`05-corene-wyldath.md:25`).
- Grep for `thorvin|Thorvin|Twinbeard` in `campaign/setting/notable-figures/` (folder-wide): only `03-narl-xibrindas.md` and `07-thorvin-twinbeard.md`.
- Grep for `third cistern|north pillar` across the repo: only `.claude/skills/character-voices/voices/xanathars-guild.md:132`.
- Grep for `Dandymops|Mirklav` in `campaign/`: two hits, `campaign/gazetteer/waterdeep/trades-ward.md:260` ("Left out", quoted at D7) and `campaign/guides/factions/12-open-lords-watch.md:177` ("Not used"). The Spring cellar is not used in the campaign.
- Grep for `engineer|trapsmith` across `sources/*.md` (Appendix B, Appendix C, Act_III_Arc_E, Appendix D): only `sources/SOURCE_GUIDE.md` and an unrelated Gond file. No Thorvin in the appendices.
- Grep for `Thorvin|Twinbeard` in `sources/Act_III_Arc_E.md`: none.
- Alexandrian PDFs: Grep returns zero hits, but the PDFs are compressed, so the zero is not evidence. Read in full: `sources/11. Lair  Xanathar’s Lair.pdf` (9 pages; Thorvin on printed pp.89, 90, 91 only), `sources/17. Outpost and Lair Revelation Lists.pdf` (4 pages, pp.121 to 124; the Lair list at p.123 has no Thorvin entry), `sources/5. Faction Outposts.pdf` (13 pages; no Thorvin), `sources/3. Player Character Factions.pdf` (3 pages; no Thorvin; p.24 names the Harpers' Waterdeep double-agent problem without a name).
- The Harper Wise Owl informant "Lantern" is Dena Holt at a Guild warehouse, and "She never enters the lair" (`campaign/quests/faction-events/harpers/r25-wise-owl/ev-01-wise-owl.md:153`). The Sea Maidens and Dock Ward informants (Mara Coppersail, Joss Marrin) are not Thorvin.

## Not readable

- None of the sources failed to open.
- The Alexandrian PDFs were read as rendered images (no shell, so no `pdftotext`). Every PDF quote is marked **[PDF transcription]** and needs a `pdftotext -layout` check.
- `sources/Other remix files/*.docx` were not searched. `sources/SOURCE_GUIDE.md` lists no `.docx` for the Guild.

## Not run

- `voicecheck.py` was not run (research only).
- The page was not written. No file was edited except this notes file.
