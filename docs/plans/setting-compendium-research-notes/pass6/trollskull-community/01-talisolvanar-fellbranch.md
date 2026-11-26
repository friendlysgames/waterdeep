# Pass 6 research notes: Talisolvanar "Tally" Fellbranch

Page: `campaign/setting/notable-figures/trollskull-community/01-talisolvanar-fellbranch.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Ruling 2 names "the Trollskull staff" as major. No source puts Tally on the staff roll (`campaign/guides/trollskull-manor/` has no staff entry for him), so he is a neighbor. The size call (major or minor) is the orchestrator's.
Organization page: none. The trollskull-community group has no `campaign/setting/organizations/` page. The affiliation check is in section D6.
Factions Guide: none. Tally has no `campaign/guides/factions/` page.
Voice profile: `.claude/skills/character-voices/voices/trollskull-community.md` lines 7 to 21 ("### Talisolvanar "Tally" Fellbranch").
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`

## Method and caveats

- Campaign files: Grep and Read. Quotes are copied from tool output. Line numbers are file lines. Where a line was too long for Grep, I re-read it with Read or a narrower Grep (noted where it applies).
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes are shown as plain quotes. `{@creature ...}` tags are left as written.
- Alexandrian Appendix D: `sources/Appendix_D_-_Running_the_Tavern.md`, markdown transcription.
- Alexandrian PDF: `sources/27. Addendum A Night in Trollskull Manor.pdf` was read with the Read tool's `pages` parameter. PDF pages 1 to 11 (printed pages 178 to 188) were read as images. PDF page 7 is printed 184 (patron table). PDF page 9 is printed 186 (topics and agendas). The PDF quotes are transcriptions from the image. Each one must be checked with `pdftotext -layout` before it goes into prose. No shell was available. Printed pages after 188 were not read.
- Wiki: the scratchpad extract `wiki-trollskull-community/01-talisolvanar-fellbranch.txt` is the stub `NOT FOUND`. The full Forgotten Realms Wiki dump in the scratchpad does have the page: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/fandom-dump/forgottenrealms_pages_current.xml`, page title "Talisolvanar Fellbranch", XML lines 4008161 to 4008272. Quotes from it are cited as "dump line N" and the XML entities are decoded. Its infobox cites `WDH5e-p32`. The Relationships section cites a 2018 D&D Beyond article, edition not tagged.
- `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **The campaign settles Tally as "he". The Alexandrian PDF transcription says "she".** The adventure says "male" (`adventure-wdh.json:3372`). The North Ward gazetteer records the user's ruling (`north-ward.md:276`). The PDF transcription on printed p.186 says "She's been commissioned" (PDF page 9). This is a transcription to check, and it is listed under D1.
2. **The Featured-in list names four quests, and three of them carry no Tally line.** The Undercliff Scarecrows design notes say he does not appear (`m01-the-undercliff-scarecrows/design-notes.md:29`). The Doppelganger Auditions, The Archer Above and The Dragon in the Harbor have no line naming Tally (checked by Grep). The drafter should not carry these as appearances. See D2.
3. **The sibling link is not in the adventure.** `adventure-wdh.json` names Tally at lines 313, 3372, 3376 and 3384, and no line in the Melannor entry (3696 to 3717) names a brother. The sibling link is in Appendix D (`:1244`), the Alexandrian PDF (printed p.186), the Emerald Enclave first-meeting event (`ev-01-first-meeting.md:68`), and the wiki dump (line 4008246, a D&D Beyond article). The Melannor page marks the sibling detail `[design]` (`emerald-enclave/01-melannor-fellbranch.md:37`). See A1 and D4.
4. **The Background has to match the Melannor page's [design] sentences about Tally.** The Melannor page says Tally left "first to learn joinery" and that the brothers "never agreeing" about jokes (`emerald-enclave/01-melannor-fellbranch.md:137` and `:138`). These are campaign-side design claims. They are not sources. See G.

---

## A. Background facts by theme

### A1. Origin, family and the brother

**Adventure, T2 entry (page 32)**
> "{@creature Talisolvanar \"Tally\" Fellbranch|wdh}, the owner and chief artisan of the Bent Nail, is a male half-elf carpenter and woodcarver. He is a {@creature commoner}, with these changes:"
> — `sources/adventure-wdh.json:3372`

**Adventure, pronunciation key**
> "Talisolvanar Fellbranch",
> — `sources/adventure-wdh.json:313` (the next line, 314, reads "tal-iss-AWL-van-ar")

**Adventure, racial traits and languages**
> "He has these racial traits: He has advantage on saving throws against being {@condition charmed}, and magic can't put him to sleep. He has darkvision out to a range of 60 feet. He speaks Common and Elvish."
> — `sources/adventure-wdh.json:3377`

**Wiki, lead (dump line 4008239; the ref names are as printed; entities decoded)**
> "'''Talisovanar "Tally" Fellbranch''' ({{Pronounce|tal|iss|AWL|van|ar|refs=<ref name="WDH5e-p4"><nowiki>{{Cite book/Waterdeep: Dragon Heist|4}}</nowiki></ref>}}) was a [[half-elf]] carpenter and woodcarver in [[Waterdeep]] in the late 15{{th}} century [[DR]].<ref name="WDH5e-p32" />"
> — dump line 4008239 (the wiki's spelling is "Talisovanar", see D3)

**Wiki, infobox (dump lines 4008190 to 4008208)**
> "| sex            = Male" (dump line 4008190)
> "| race           = [[Half-elf]] " (dump line 4008191)
> "| occupation     = Carpenter, woodcarver<ref name="WDH5e-p32" />" (dump line 4008193)
> "| languages      = [[Common]] and [[Elvish]]" (dump line 4008196)
> "| siblings       = " (dump line 4008208, blank)

**Wiki, Relationships (dump line 4008246; the ref is a D&D Beyond article, 2018, edition not tagged)**
> "Tally was brother to [[Melannor Fellbranch]]."
> — dump line 4008246

**Alexandrian Appendix D, Topics & Agendas (1244)**
> "1. Introduces the characters to his brother, Melannor Fellbranch (Emerald Enclave contact), framing it as a casual visit that is clearly calculated."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1244`

**Alexandrian PDF, printed p.186 (PDF page 9; transcription)**
> "Introduces PCs to his brother, Melannor Fellbranch (representative of the Emerald Enclave)."
> — `sources/27. Addendum A Night in Trollskull Manor.pdf`, PDF page 9

**Emerald Enclave first meeting, Melannor's line**
> "Good morning, and welcome to Phaulkonmere. I am Melannor Fellbranch, and I would like to know whether Talisolvanar is well. He is my brother, and he works as a carpenter in your alley."
> — `campaign/quests/faction-events/emerald-enclave/00-first-meeting/ev-01-first-meeting.md:68`

**Melannor page, family (the sibling and parents are `[design]`)**
> "Melannor grew up in a village at the edge of a forest in the North, the older of two sons of a human orchardist and an elven forester `[design]`. His mother taught him to graft a branch and to tell a sick tree from a dry one, and his father, who was often away in the forest, taught him to read soil and tracks `[design]`. His younger brother, Talisolvanar, followed him down the rows and made a joke about every tree `[design]`."
> — `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md:18`

**Melannor page, Connections**
> "- **Talisolvanar "Tally" Fellbranch:** His younger brother, a carpenter and woodcarver at the Bent Nail in Trollskull Alley `[design]`. Each has told the other to visit, and Talisolvanar wants Melannor to come more often than he does."
> — `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md:37`

**Melannor page, Draft Notes, Background (ALL `[design]`, not a source)**
> "  - Background, Waterdeep: Talisolvanar leaving first to learn joinery; Melannor staying until the replanted trees took; the gardener's-hand job at Phaulkonmere for its old oak; the Enclave druid who held the post, taught him druid craft and *Animal Messenger*, and brought him in; the families asking him to take the post; the Enclave as his one company besides his brother."
> — `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md:138` (the callout line is `> ` prefixed in the file)

**Tally page, current Relationships (the sibling clause)**
> "**Relationships.** Tally is the brother of Melannor Fellbranch (Emerald Enclave contact at Phaulkonmere), and a longtime neighbor of Fala Lefaliir and Embric."
> — `campaign/setting/notable-figures/trollskull-community/01-talisolvanar-fellbranch.md:25`

### A2. The shop, its trade and its rank

**Adventure, T2 entry heading and sign (page 32)**
> "T2. The Bent Nail"
> — `sources/adventure-wdh.json:3367`
> "A small wooden sign above this shop's main door is bare except for a large, bent nail sticking out of it. The front room contains displays of ornate wooden furniture, as well as a selection of bows and crossbows. The wall behind the counter is lined with rows of finely carved wooden canes, {@item quarterstaff|PHB|quarterstaffs}, and {@item shield|PHB|shields}."
> — `sources/adventure-wdh.json:3370`

**Adventure, Services (page 32)**
> "Tally sells wooden weapons and shields at normal cost. He also crafts and sells furniture and wood sculptures."
> — `sources/adventure-wdh.json:3384`

**Wiki, Bent Nail page (dump line 5111317; refs WDH5e-p33 and CSW3E-p94,97)**
> "The building was located on a corner next to the northeast entry to the alley from [[Saerdoun Street]], in front of a ground entrance to the [[Waterdeep/Sewers|Waterdhavian sewer system]]."
> — dump line 5111317

**Wiki, Bent Nail page, Inhabitants (dump line 5111333; ref WDH5e-p32)**
> "By {{Yearlink|1492}},{{Waterdeep-time}} the shop was owned by the [[half-elf]] [[Talisolvanar Fellbranch]], who was also its chief artisan."
> — dump line 5111333

**Wiki, Bent Nail page, earlier tenant (mid-14th century DR; not day one)**
> "By the mid‒14{{th}} century [[DR]], the [[wizard]] [[Avaereene]] rented rooms above the shop."
> — dump line 5111331

**Wiki, Trollskull Alley page (dump lines 5103805 and 5103808; refs WDH5e-ch2, WDH5e-map, VGW2e-p103)**
> "'''Trollskull Alley''' was an alley located in the [[Waterdeep/North Ward|North Ward]] of [[Waterdeep]]."
> — dump line 5103805
> "The alley was a narrow passage that wound through the interior of the city block surrounded in the North and South by [[Saerdoun Street]] and [[Delzorin Street]] and in the East and West by [[Whaelgond Way]] and [[Windborne Way]], respectively."
> — dump line 5103808

**North Ward gazetteer, Trollskull Alley entry**
> "- The party's tavern stands at its north end. The Bent Nail is a woodshop run by **Tally Fellbranch**, Steam and Steel is a forge run by **Embric** and **Avi**, and Corellon's Crown is a greenhouse kept by **Fala Lefaliir**."
> — `campaign/gazetteer/waterdeep/north-ward.md:57`

**Appendix D, Patron table (1106)**
> "| 1 | Tally Fellbranch *(The Bent Nail)* |"
> — `sources/Appendix_D_-_Running_the_Tavern.md:1106`

**Trollskull Manor guide, Patron table (06-tavern-time.md:58)**
> "| 1 | Tally Fellbranch *(The Bent Nail)* |"
> — `campaign/guides/trollskull-manor/06-tavern-time.md:58`

### A3. Temperament, habits and manner (Appendix D, the patron profile; the guide)

**Appendix D, Appearance (1239)**
> "**Appearance:** Short brown hair in a bowl cut; large blue eyes; leather vest with tool pockets. Rubs the tops of his ears as a nervous habit."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1239`

**Appendix D, Roleplaying Keys (1241)**
> "**Roleplaying Keys:** Strong handshake. Very sarcastic — not meanly, but reflexively. Genuinely proud of his work."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1241`

**Appendix D, Topics & Agendas 2 to 4 (1245 to 1247)**
> "2. Offers to sculpt a wooden troll's skull to mount above the bar — "something actually imposing, not whatever you're planning.""
> "3. Has received a commission to craft 8-foot-tall chess pieces for the Cragsmere Estate. He buys a round for the whole tavern to celebrate. He looks sheepish about it."
> "4. Mentions that the oak tree outside the manor is "acting strange" — the roots are reaching toward the foundation. He thinks it's the ghost. He's wrong."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1245` to `:1247`

**Trollskull Manor guide, Notable Patrons (08-notable-patrons.md:13 to 17)**
> "**Tally Fellbranch** *(The Bent Nail, CG half-elf, Commoner)*"
> "Strong handshake; reflexively sarcastic; proud of his work."
> "- Has been commissioned for 8-foot chess pieces for Cragsmere Estate; buys a round"
> — `campaign/guides/trollskull-manor/08-notable-patrons.md:13`, `:14`, `:17`

**Voice profile (character-voices skill; the profile's own bullets)**
> "*A dry, sarcastic carpenter who talks about wood grain more easily than feelings and helps before he's asked.*"
> "- **Personality in speech:** Wry amusement covers real care. He offers help as a complaint ("Fine, I'll fix it, it's an eyesore"). Pride in good work shows in understatement ("It'll hold."). He complains that his brother Melannor never visits in a way that's clearly about missing him."
> "- **Quirks:** He judges furniture out loud. He knocks on wood to test it while he talks. He answers compliments with "It's just wood.""
> "- **Never:** He never gushes, never lies about a bad job, and never charges a neighbour full price."
> — `.claude/skills/character-voices/voices/trollskull-community.md:8`, `:14`, `:15`, `:17`

### A4. Neighbors

**Alexandrian PDF, printed p.186 (PDF page 9, transcription)**
> "Offers his services to sculpt a wooden troll's skull that could be displayed on the wall."
> — PDF page 9 (Appendix D 1245 has "to mount above the bar" instead)

**Fala Lefaliir page, Relationships (other page, read only)**
> "**Relationships.** Fala is a close friend of Ziraj the Hunter (Doom Raiders assassin, who keeps a room on Fala's second floor), a neighbor and confidant of Tally Fellbranch, and a member of the Guild of Apothecaries and Physicians. Fala uses they/them pronouns, reflecting Corellon Larethian's genderless nature."
> — `campaign/setting/notable-figures/trollskull-community/04-fala-lefaliir.md:25`

**Emmek Frewn page, Relationships (other page, read only)**
> "**Relationships.** Emmek is a debtor of Istrid Horn (150 gp loan with interest, enforced by Zhentarim thugs), a client of the Shard Shunners (halfling wererat gang he pays to sabotage the party), and a reluctant neighbor of Tally Fellbranch (who thinks Emmek's pub sign is "an insult to joinery")."
> — `campaign/setting/notable-figures/trollskull-community/10-emmek-frewn.md:25`

**Embric page, Relationships (other page, read only)**
> "**Relationships.** Embric is the husband of Avi (co-owner of Steam and Steel), a neighbor of Tally Fellbranch (whose wooden shields he considers inferior to metal), and a member of the Most Careful Order of Skilled Smiths and Metalforgers."
> — `campaign/setting/notable-figures/trollskull-community/02-embric.md:25`

### A5. Time in post

- The wiki's day-one owner line is quoted above (dump line 5111333): "By 1492 DR the shop was owned by ... Talisolvanar Fellbranch, who was also its chief artisan." The wiki's exact words are "By {{Yearlink|1492}},{{Waterdeep-time}} the shop was owned by the [[half-elf]] [[Talisolvanar Fellbranch]], who was also its chief artisan."
- No source gives the year he took the shop, his age, his birthplace, or when he came to Waterdeep. See F.

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Summary: "> - *Half-elf carpenter, chaotic good, he/him*. Stat block: **Commoner**." — `campaign/setting/notable-figures/trollskull-community/01-talisolvanar-fellbranch.md:5`
- Adventure: "Tally is chaotic good." — `sources/adventure-wdh.json:3376`
- Appendix D: "*The Bent Nail — CG, Commoner with half-elf traits*" — `sources/Appendix_D_-_Running_the_Tavern.md:1237`
- Wiki: "| alignment5e    = [[Chaotic good]]" — dump line 4008234
- Trollskull Manor guide: "**Tally Fellbranch** *(The Bent Nail, CG half-elf, Commoner)*" — `campaign/guides/trollskull-manor/08-notable-patrons.md:13`
- All sources agree: chaotic good.

**Species**
- Summary: "*Half-elf carpenter, chaotic good, he/him*" (`01-talisolvanar-fellbranch.md:5`)
- Adventure: "is a male half-elf carpenter and woodcarver" (`sources/adventure-wdh.json:3372`)
- Wiki: "| race           = [[Half-elf]] " (dump line 4008191)
- Appendix D: "Commoner with half-elf traits" (`:1237`)
- All sources agree.

**Pronouns**
- Summary: "he/him" (`01-talisolvanar-fellbranch.md:5`)
- Adventure: "is a male half-elf" (`sources/adventure-wdh.json:3372`)
- Wiki: "| sex            = Male" (dump line 4008190)
- North Ward gazetteer, Draft Notes: "> - **Settled by the user (Session 51):** Tally Fellbranch is male (Dragon Heist `adventure-wdh.json:3372`), and `ev-01-the-fireball.md` now says "he"." — `campaign/gazetteer/waterdeep/north-ward.md:276`
- Fireball! ev-01: "Substitute **Tally Fellbranch** as this witness — he watched the blast from the Bent Nail's doorway and provides the same account of the burned man limping north." — `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:125`
- Conflicts: see D1 (the PDF transcription says "She's").

**Stat block**
- Summary: "Stat block: **Commoner**." (`01-talisolvanar-fellbranch.md:5`)
- Adventure: "He is a {@creature commoner}, with these changes:" (`sources/adventure-wdh.json:3372`)
- Wiki: "| class5e        = [[Commoner]]" (dump line 4008236)
- Appendix D: "Commoner with half-elf traits" (`:1237`)
- The adventure's changes are alignment (3376), racial traits (3377) and Services (3384).

---

## C. Sentences on the current page that narrate a quest-time event or a day-one conflict

Current page: `campaign/setting/notable-figures/trollskull-community/01-talisolvanar-fellbranch.md`. The page has no Background section yet. Its sections are Gamemaster's Summary, Roleplaying Information, Character Information and Overview.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L6 | "> - **Affiliation:** Trollskull Alley community" | Label, not a quest event. See D6 | No organization page. See D6 |
| 2 | L7 | "> - **Featured in:** **Trollskull Alley**, **Fireball!**, **The Doppelganger Auditions**, **The Undercliff Scarecrows**, **The Archer Above**, **The Dragon in the Harbor**, **Trollskull Manor**" | Quest list. Brief ruling 1: route. Four of the seven entries are not confirmed (D2) | Trollskull Alley: `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:19`; Fireball!: `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:163` and `:165`; Trollskull Manor: `campaign/guides/trollskull-manor/06-tavern-time.md:27`. Undercliff: `campaign/quests/faction-events/emerald-enclave/m01-the-undercliff-scarecrows/design-notes.md:29` says he does not appear |
| 3 | L15 | "**Motivations.** Tally wants to run the best woodworking shop in the North Ward, keep the alley a decent place to live, and make sure his brother Melannor actually visits once in a while." | Day-one. Keep verbatim (ruling 3). Sibling clause is design, see A1 | `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md:37` |
| 4 | L23 | "**Morale.** In a fight, Tally would grab whatever sharp tool is nearest and stand between the threat and his shop. He has no combat training but will not abandon the Bent Nail." | Day-one. Keep. "his shop" is his trade, not a quest fact | Bent Nail: `sources/adventure-wdh.json:3367` |
| 5 | L25 | "**Relationships.** Tally is the brother of Melannor Fellbranch (Emerald Enclave contact at Phaulkonmere), and a longtime neighbor of Fala Lefaliir and Embric." | Day-one in form. The parenthesis labels Melannor, not Tally. "longtime" has no source | Sibling: A1. "Longtime" is `[research]` |
| 6 | L29 | "Tally runs the Bent Nail woodworking shop in Trollskull Alley and is one of the party's most reliable neighbors — dry-humored, plainspoken, and quietly generous with tools and labor when something in the alley needs fixing." | Day-one in content. "the party's" presumes the party. Drafter restates as the alley's neighbor (ruling 1) | Shop: `sources/adventure-wdh.json:3372`; neighbor role: `campaign/gazetteer/waterdeep/north-ward.md:57` |

**Voice profile, quest-time clauses (`.claude/skills/character-voices/voices/trollskull-community.md`, lines 8 to 21)**

- Line 19, Greeting sample: "*Greeting:* "You're the new owners. Your front door's hung like shit. I'll bring tools."" — **quest-time clause**. "the new owners" means the party owns the tavern, which the adventure gives after Volo's quest: "Following the completion of Volo's quest, the characters gain a home base with an address in Trollskull Alley, in Waterdeep's North Ward." (`sources/adventure-wdh.json:1595`). Restate as a day-one line (for example, a neighbor greeting whoever holds the manor). The profile change is for the drafter (ruling 16).
- Line 20, Business sample: "*Business:* "Oak for the bar. Pine'll warp by spring and you'll blame me."" — minor. "the bar" is the tavern's. Not an event. Drafter's call.
- Line 21, Under pressure: "Get behind the counter. Nobody's coming into the Bent Nail tonight." — day-one. Keep.
- Lines 10 to 17 (Sound, Sentence shape, Word choice, Swearing, Personality in speech, Quirks, Signature phrases, Never) have no quest-time clause. Line 14 "He complains that his brother Melannor never visits" is day-one.

### C2. Where Tally's quest-time events already live (routed; do not restate on the day-one page)

- **Trollskull Alley, ev-01**: "**Bent Nail** (Tally Fellbranch) — a woodshop with sawdust on the threshold and a handmade sign. The door is open." — `campaign/quests/act-i/trollskull-alley/ev-01-welcome-to-trollskull-alley.md:21`
- **Trollskull Alley, ev-03 (The Neighbors)**: "**Tally Fellbranch (Bent Nail).** Knocks on the open door holding a small carved wooden owl, saying "for the bar; last owners never had one." Offers to fix the warped door frames at cost. Wry and unpretentious. Tally is Melannor Fellbranch's brother; the party will not make the connection until Emerald Enclave recruitment arrives in ev-04. Cross-ref the **Tally Fellbranch** page in Notable Figures." — `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:19`
- **Trollskull Alley, ev-06 (The Grand Opening)**: "**Neighbors** — Tally, Embric and Avi, Fala, Rishaal (all four attend). Vincent Trench sends regrets via a note and a gift of expensive pipe tobacco. Ulkoria arrives late, drinks one ale, says "Acceptable," and leaves." — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:40`
- **Trollskull Alley, ev-07 (The Twin Parades), victim table**: "| Tally Fellbranch | ev-03 | Connected to Renaer and Melannor; his death damages two faction relationships |" — `campaign/quests/act-i/trollskull-alley/ev-07-the-twin-parades.md:65`
- **Trollskull Alley overview**: "- **Tally Fellbranch** (independent) — woodworker at the Bent Nail; Melannor's brother; potential fireball victim" — `campaign/quests/act-i/trollskull-alley/overview.md:31` (label conflict, see D6)
- **Trollskull Alley flowchart**: "**The Factions Come Calling overlaps the renovation period.** Faction invitations arrive while the renovation runs; the party may be meeting Tally on the same day a Harper paper bird lands on their window." — `campaign/quests/act-i/trollskull-alley/flowchart.md:33`
- **Fireball!, ev-01, Fala fallback**: "> If Fala was the Trollskull Alley victim, she is dead in the alley. Substitute **Tally Fellbranch** as this witness — he watched the blast from the Bent Nail's doorway and provides the same account of the burned man limping north. The information is identical; the NPC differs." — `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:125`
- **Fireball!, ev-01, witness entry**: "#### Tally Fellbranch / Embric and Avi" then "Supporting witnesses. Tally saw the flash and the smoke from the Bent Nail's doorway. Embric noticed a glint of silver moving east across the rooftops a moment before the blast. Avi confirms the timing." — `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:163` and `:165`
- **Fireball!, overview**: "- **Tally Fellbranch / Embric / Avi** (Trollskull Alley) — supporting witnesses; Tally substitutes for Fala if Fala is the victim" — `campaign/quests/act-ii/fireball/overview.md:33`
- **Fireball!, design notes**: "***The Fala Fallback.*** If Fala Lefaliir was the designated victim, Tally Fellbranch substitutes as the witness who saw Floxin flee north. The information is identical; the delivery changes. Do not use Fala for both roles — the GM's selection from Trollskull Alley is binding." — `campaign/quests/act-ii/fireball/design-notes.md:15`
- **North Ward gazetteer, Hook**: "- Hook: the **Fireball!** blast hits the alley at first light on Ches 22. It kills twelve in a 20-foot radius, including three North Ward servants out on early errands, and it may kill Fala or Tally." — `campaign/gazetteer/waterdeep/north-ward.md:59`
- **Structural rules, victim table**: "| Tally Fellbranch (he/him) | ev-03 | Connected to Renaer and Melannor; his death damages two faction relationships |" — `campaign/guides/gm-guide/structural-rules.md:103`
- **Trollskull Manor guide, Operating costs**: "- **Emerald Enclave (Jeryth Phaulkon + Melannor Fellbranch):** Two Enclave druids use *Mold Earth*, *Shape Water*, *Plant Growth* and *Stone Shape* to dig out the cellar, drain the courtyard and reseat the foundation stones in a single day. The Enclave donates seasoned timber, and Tally Fellbranch lays it at no charge. Renovation cost drops by 250 gp, once. Ask: leave the oak tree undisturbed; allow silverbark growth on it." — `campaign/guides/trollskull-manor/02-operating-costs.md:82`
- **Trollskull Manor guide, Tavern time (calendar rows)**: "| Ches 21–30, after the fireball | Tally Fellbranch, Embric & Avi, Fala Lefaliir | 6: a City Watch patrol arrests a patron | The alley counts its dead. The Watch is sweeping the North Ward for fireball witnesses, and the arrest shows the party how hard the city is leaning on the neighborhood. |" — `campaign/guides/trollskull-manor/06-tavern-time.md:27`
- **Tavern time, Kythorn row**: "| Kythorn 1–10 | Broxley Fairkettle, Tally Fellbranch, Laraelra "Elra" Harsard with Lord Torlyn Wands (Renaer's Friends) | 14: a Masked Lord visits (at Fame 81+); otherwise 17: a socialite demands the best table | Guild season. The night measures where the tavern stands with the city's upper floors. |" — `campaign/guides/trollskull-manor/06-tavern-time.md:32`
- **Tavern time, first tenday after Vault row**: "| First tenday after **Vault of Dragons** (Fame 15+) | Renaer Neverember, Floon Blagmaar, Tally Fellbranch | Halaster's stranger (see **Trollskull Manor**, The Tavern and Undermountain) | Undermountain notices the party. |" — `campaign/guides/trollskull-manor/06-tavern-time.md:35`
- **Tavern time, Trollskull Manor location**: "**Operational state.** Furnished and staffed. Bar tools in place (laid out by Lif before anyone asks). Hearth lit when weather turns. Tables and chairs from Tally Fellbranch's repair work. The chalk slate has the current specials in handwriting that isn't anyone's." — `campaign/locations/trollskull-manor/tm01-taproom.md:7`
- **Emerald Enclave first meeting, ev-01**: "Meet Melannor Fellbranch inside the gate, where he asks after his brother Talisolvanar, and walk the garden with him." — `campaign/quests/faction-events/emerald-enclave/00-first-meeting/ev-01-first-meeting.md:8`; the timber line "- **The timber:** The Enclave donates seasoned timber for the frames and floors, and Tally Fellbranch lays it at no charge to the party." — `:274`; "Good, I am glad to hear it. Talisolvanar should visit when his work in the alley allows it." — `:74` (the file's line is blockquoted)
- **Order of the Gauntlet, first meeting, ev-01**: "When nobody is at the manor, she leaves a note with Tally Fellbranch, who works on the door frames. Tally hands it to the first resident he sees. The note is one short paragraph, written in a left-slanting hand on paper with the Halls of Justice seal, folded once and signed "S.B." Read the following aloud when someone answers the door." — `campaign/quests/faction-events/order-of-the-gauntlet/00-first-meeting/ev-01-first-meeting.md:36`
- **Order of the Gauntlet, Factions Guide**: "Savra knocks once at Trollskull Manor and waits to be asked in. If nobody is home, she leaves a note with Tally Fellbranch. She names two targets: a beholder said to run the Guild beneath the city, and a Sea Ward family she will not name. She states the cost of the work plainly, including a quarter of what a member earns on big jobs. A character who asks sincerely about her past learns she spent three years in the Howling Hatred cult, and nothing about what she did there." — `campaign/guides/factions/05-order-of-the-gauntlet.md:37`
- **Appendix C, faction mission "Asking the Right People"**: "**Asking the Right People.** The party's Trollskull Alley neighbors are a useful shortcut. **Tally Fellbranch** of the Bent Nail saw a hire-dray with no visible driver pulled up outside the Silvermoon Institute three days ago — he mentioned it because he thought the dray's owner was napping inside." (rest of the passage covers: Fala Lefaliir's hire-drays and the two neighbors' DC reduction) — `sources/Appendix_C_-_Player_Faction_Missions.md:57`
- **Adventure, Fala's eyewitness account (quest time)**: "He was headed toward the Bent Nail." — `sources/adventure-wdh.json:4477`; "Fala saw {@creature Urstul Floxin|wdh} fleeing the scene with the {@item Stone of Golorr|WDH} in his clutches. He circled around the Bent Nail (see chapter 2, {@area T2|09b}) on his way out of Trollskull Alley." — `sources/adventure-wdh.json:4480`
- **Alexandrian Act III, Fala's account**: "He was limping north toward the Bent Nail." — `sources/Act_III_Arc_D.md:158`
- **Structure docs (superseded or pending, do not use for content)**: `campaign/structure/arc-b-trollskull-alley.md:95` ("- **Tally Fellbranch (Bent Nail):** Knocks on the open door holding a small carved wooden owl ...") and `:268`; `campaign/structure/arc-c-fireball.md:82`.

---

## D. Conflicts

**D1. Pronoun (he or she)**
- Adventure: "is a male half-elf carpenter and woodcarver" (`sources/adventure-wdh.json:3372`)
- North Ward gazetteer: "Tally Fellbranch is male" (`campaign/gazetteer/waterdeep/north-ward.md:276`, "Settled by the user (Session 51)")
- Fireball! ev-01: "he watched the blast" (`campaign/quests/act-ii/fireball/ev-01-the-fireball.md:125`)
- Appendix D: "He buys a round for the whole tavern to celebrate. He looks sheepish about it." (`sources/Appendix_D_-_Running_the_Tavern.md:1246`)
- Alexandrian PDF, printed p.186 (transcription, check with pdftotext): "She's been commissioned to craft 8-foot-tall chess pieces for the Cragsmere Estate. It's a major commission and she buys a round of drinks for everyone in the tavern to celebrate." (PDF page 9)
- Trollskull Manor guide: "buys a round" with no pronoun (`campaign/guides/trollskull-manor/08-notable-patrons.md:17`)
- Higher ranked: the adventure, and the user's Session 51 ruling in the campaign. The PDF's "she" is an open transcription question. The brief says the page is "he".
- Stale: `north-ward.md:286` says "`ev-01-the-fireball.md:128` calls Tally "she" against the Notable Figures page." The current file has no such line at 128 (line 128 is the heading "#### Jezrynne Hornraven"), and line 125 says "he". This is a stale note, not a live conflict (see E1).

**D2. Featured-in list (quest appearances)**
- Page L7 lists **The Doppelganger Auditions**, **The Undercliff Scarecrows**, **The Archer Above**, **The Dragon in the Harbor**.
- `campaign/quests/faction-events/emerald-enclave/m01-the-undercliff-scarecrows/design-notes.md:29`: "- `campaign/setting/notable-figures/trollskull-community/01-talisolvanar-fellbranch.md:8` lists this mission under Tally's appearances, but he does not appear in it." (the reference is to line 8 of the page; the Featured-in line is at page line 7 in the current file)
- Grep of `campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/ev-01-the-doppelganger-auditions.md` for Tally, Talisolvanar, Embric, Avi, Bent Nail, Steam and Steel and Trollskull Alley: no matches.
- Grep of `campaign/quests/faction-events/lords-alliance/m04-the-archer-above/ev-01-the-archer-above.md`: no Tally line. Only rooftop and feed-store lines name the alley's neighborhood, for example: "The party needs the feed store on Pell Street, one block north of Trollskull Alley, before the fourth evening."
- Grep of `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md`: no matches.
- Higher ranked: the quest files. The Featured-in list is not supported for three entries and is contradicted for one.

**D3. Name spelling**
- Adventure: "Talisolvanar Fellbranch" (`sources/adventure-wdh.json:313`)
- Wiki page title and lead: "Talisovanar "Tally" Fellbranch" (dump lines 4008162, 4008182, 4008239).
- Campaign: "Talisolvanar" throughout (page L1, Relationships L25; Melannor page). The campaign spelling follows the adventure's key. Drafter uses the campaign spelling. The wiki's "Talisovanar" is a spelling variant only.

**D4. The sibling link: source weight**
- Adventure: no line calls the two brothers. The Tally lines are `:313`, `:3372`, `:3376` and `:3384`. The Melannor lines are `:233`, `:1327`, `:3696`, `:3700` and `:3701`, and none names a brother.
- Appendix D `:1244`, Alexandrian PDF printed p.186, and the wiki dump line 4008246 all state the sibling link.
- Melannor page marks it `[design]` (`campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md:37`).
- Higher ranked: the campaign uses the link (Melannor page and Enclave first meeting), with the Melannor page's `[design]` tag. The link rests on Appendix D and the PDF. The adventure is silent.

**D5. The Cragsmere commission and the place**
- Appendix D `:1246`, PDF page 9, and `08-notable-patrons.md:17` all give the commission. No campaign file defines "Cragsmere Estate". The wiki lists "Cragsmere" only as landowners and a "Cragsmere Villa" in a ward list: `sources/research/pass3-bundles/north-ward/wiki.txt:551` ("* [[Cragsmere Villa]]") and `:645` ("* [[Cragsmere]]&mdash;Noted landowners who increased their wealth through money-lending."). Not used by the campaign. Gap (F).

**D6. Affiliation label**
- Page Summary: "> - **Affiliation:** Trollskull Alley community" (`01-talisolvanar-fellbranch.md:6`).
- Trollskull Alley overview: "- **Tally Fellbranch** (independent) — woodworker at the Bent Nail; Melannor's brother; potential fireball victim" (`campaign/quests/act-i/trollskull-alley/overview.md:31`).
- Emerald Enclave organization page: "- **Talisolvanar "Tally" Fellbranch** (Notable Figures): Melannor's brother, a Trollskull Alley carpenter outside the Enclave" (`campaign/setting/organizations/03-emerald-enclave.md:141`).
- No organization page covers the Trollskull community. The page's label is "Trollskull Alley community", and the Enclave page puts Tally "outside the Enclave". The quest overview's "(independent)" is a quest summary, so it does not govern (brief ruling 6). The drafter keeps "Trollskull Alley community" and does not write "Emerald Enclave" for Tally.
- Page L25 "Emerald Enclave contact at Phaulkonmere" describes Melannor, not Tally. Melannor's labels: `campaign/setting/organizations/03-emerald-enclave.md:8` ("**Contacts:** **Melannor Fellbranch** (primary)") and `:55` ("- **Primary Contact:** Melannor Fellbranch, groundskeeper of Phaulkonmere and a Half-Elf druid.").

**D7. Renaer**
- Structural rules and Trollskull Alley ev-07 say Tally is "Connected to Renaer and Melannor" (`campaign/guides/gm-guide/structural-rules.md:103`; `campaign/quests/act-i/trollskull-alley/ev-07-the-twin-parades.md:65`).
- No line in the adventure or the Alexandrian sources links Tally and Renaer. Renaer appears with Tally only in the tavern-time rows (`06-tavern-time.md:32` and `:35`), which are calendar rows. Not a biography fact (F).

---

## E. Stale lines in other files (not edited) and routed quest references

**E1. Stale or conflicting lines**
- `campaign/gazetteer/waterdeep/north-ward.md:286`: "`ev-01-the-fireball.md:128` calls Tally "she" against the Notable Figures page." Stale. The current file has no pronoun for Tally at line 128 (see D1).
- `campaign/quests/faction-events/emerald-enclave/m01-the-undercliff-scarecrows/design-notes.md:29`: lists Tally's appearance in a mission where he does not appear (see D2).
- `campaign/quests/faction-events/harpers/m01-the-talking-mare/design-notes.md:17`: "The Tally Fellbranch and Fala Lefaliir shortcut is dropped, since Orvel, the stablehands and the Wagonworks drivers already give three routes." (rest of the line covers: Hessa Dorn's stable on Brondar's Way and the Candle Lane warehouse). Routed to the Harpers quest. The Talking Mare does not list Tally on the page.
- `campaign/structure/arc-b-trollskull-alley.md:95` and `:268`: superseded by the quest journal. The arc's line 268 reads "| Tally Fellbranch | Scene 3 | Connected to Renaer and Melannor; his death damages two faction relationships |".
- `campaign/quests/faction-events/doom-raiders/r25-ardragon/ev-01-ardragon.md:191` (and `design-notes.md:21`): a **different character** named "Tally", the Doom Raiders informant Bastian Quill. Quote: "> - **Tally**, Bastian Quill: a junior clerk in a Trades Ward counting-house that keeps the cell's accounts." The drafter must not link them to Talisolvanar Fellbranch.
- `campaign/setting/deities/eldath.md:77`, `:80` and `:92`, and `campaign/setting/deities/istishia.md:81`: cite the Avi page at line numbers that are one off from the current file (for example, Avi's Priest stat block is at `03-avi.md:5`; eldath.md:77 cites `:6`). Not a Tally line; listed because the Trollskull lines are cited there.
- Melannor page Draft Notes at `01-melannor-fellbranch.md:141`: "a brother who is a carpenter and wants him to visit (`01-talisolvanar-fellbranch.md:15`, `:25`)". Lines 15 and 25 of this page are the current Motivations and Relationships lines, so they are right today. Any change to those lines must be checked against that note.

**E2. Routed quest references (quest-time facts)**
- See section C2 for the full list. In short: Trollskull Alley ev-01, ev-03, ev-06, ev-07, overview and flowchart; Fireball! ev-01 (witness, fallback), overview, design notes; Emerald Enclave first meeting ev-01; Order of the Gauntlet first meeting ev-01 and the Factions Guide; Appendix C "Asking the Right People" (`:57`); adventure `:4477` and `:4480`; Act III `:158` and `:239`; the tavern-time rows (`06-tavern-time.md:27`, `:32`, `:35`); the Trollskull Manor renovation (`02-operating-costs.md:82`, `tm01-taproom.md:7`).
- Alexandrian Act III, line 239 (Arc D file, not a quest file): "If the characters mention Fala's sighting of the burned man fleeing toward the Bent Nail, Renaer reaches out to his Harper contacts. Within a day, he returns with the following:" — `sources/Act_III_Arc_D.md:239`.

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

1. **Birth, age, and when he came to Waterdeep.** No source. The wiki infobox leaves age, dob and parents blank (dump lines 4008194, 4008198, 4008206). The Melannor page says Tally is the younger of two sons, and gives the parents as a human orchardist and an elven forester (`01-melannor-fellbranch.md:18`, all `[design]`). Tally is a half-elf, so the parents fit. Must stay consistent with: the parents as Melannor's page states them, the younger-brother order, and the wiki's "siblings" being blank.
2. **Where he learned joinery and how he got the shop.** No source gives a teacher or a route. The wiki says only that by 1492 DR he owned the shop and was its chief artisan (dump line 5111333). The Melannor page says "Talisolvanar leaving first to learn joinery" (`01-melannor-fellbranch.md:138`, `[design]`). Must stay consistent with: Tally left first and the shop is his. The year he bought or leased the shop is open.
3. **The Bent Nail's earlier history.** The wiki says the wizard Avaereene rented rooms above the shop in the mid-14th century DR (dump line 5111331). That is a 14th-century fact and must not appear as day one. The campaign does not use it.
4. **His faith, if any.** No source. Do not give him a deity.
5. **Friends and neighbors.** Sources give Fala ("a neighbor and confidant of Tally Fellbranch", `04-fala-lefaliir.md:25`), Embric ("a neighbor of Tally Fellbranch", `02-embric.md:25`), and Emmek as a "reluctant neighbor" (`10-emmek-frewn.md:25`). Nothing else.
6. **The Cragsmere chess commission.** Appendix D and the guide give it (see D5). The Cragsmere Estate is not defined. A Background can mention the commission only as a patron topic, with `[research]` on the estate.
7. **The owl he gives the party.** Quest-time (ev-03, see C2). Do not put it on the day-one page.
8. **The shop's sign, stock and sewer entrance.** The sign and stock are in the adventure (`:3370`). The sewer entrance is in the wiki (dump line 5111317). The adventure's Trollskull Alley map is an image and is not in the text.

---

## G. Inner-life hints in the sources (exact quotes)

These are the sourced hints a Background or the personal goals may use. They must not be contradicted.

- **Nervous habit.** "Rubs the tops of his ears as a nervous habit." — `sources/Appendix_D_-_Running_the_Tavern.md:1239`
- **Pride in work.** "Genuinely proud of his work." — `sources/Appendix_D_-_Running_the_Tavern.md:1241`; "Pride in good work shows in understatement ("It'll hold.")." — `.claude/skills/character-voices/voices/trollskull-community.md:14`
- **Brother and visits.** "He complains that his brother Melannor never visits in a way that's clearly about missing him." — voice profile line 14. Melannor page: "Each has told the other to visit, and Talisolvanar wants Melannor to come more often than he does." (`01-melannor-fellbranch.md:37`, `[design]`). Melannor's first-meeting line: "Talisolvanar should visit when his work in the alley allows it." (`ev-01-first-meeting.md:74`).
- **Measures his worth by the alley.** "Deep down, he measures his worth by whether the alley is better for his being in it." — current page line 21 (day-one, Persona; no source; the drafter keeps it).
- **Will not leave the shop.** "He has no combat training but will not abandon the Bent Nail." — current page line 23.
- **The ghost.** "He thinks it's the ghost. He's wrong." — `sources/Appendix_D_-_Running_the_Tavern.md:1247` (patron topic, not a fact about his life).
- **Fair dealing.** "He never gushes, never lies about a bad job, and never charges a neighbour full price." — voice profile line 17.
- **Melannor's Background (design, the other page).** "Talisolvanar answering with more jokes, and the brothers never agreeing about it." — `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md:137` (`[design]`). "one afternoon in his brother's shop with no report" — `:139` (`[design]`). Tally's Background must not contradict these.
