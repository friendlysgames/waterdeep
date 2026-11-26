# Pass 6 research notes: Renaer Neverember

Page: `campaign/setting/notable-figures/independents-allies/02-renaer-neverember.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 19; ruling 19 on GM-facing pages)
Ruling used: Ches 1, 1492 DR. Quest-time = any capture, rescue, mission, reward, hire or "once the party" wording. The night-before kidnapping of Renaer and Floon is a capture, so it is quest-time.
Organization page: `campaign/setting/organizations/01-harpers.md` (the page says Renaer is "Harper-adjacent", not a member; the published adventure says he is a Harper; see D1). Factions Guide: none.
Voice profile: `.claude/skills/character-voices/voices/independents-allies.md` lines 48 to 62 ("### Renaer Neverember").
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/trollskull-community/01-talisolvanar-fellbranch.md`

## Method and caveats

- Campaign files: Grep and Read. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`. JSON escapes shown as plain quotes; `{@creature ...}` tags left as written. Line numbers are JSON line numbers.
- Alexandrian markdown: `sources/Appendix_D_-_Running_the_Tavern.md`, `sources/Act_III_Arc_D.md`, `sources/Appendix_B_-_Player_Factions.md`, read by Grep and Read.
- Alexandrian PDFs read with the Read tool's `pages` parameter: `sources/2. Other Factions.pdf` (3 pages, printed pp. 20 to 22), `sources/14. Finding Floon.pdf` (5 pages, printed pp. 102 to 106), `sources/26. Addendum Other Collaborators.pdf` (5 pages, printed pp. 173 to 177). Transcriptions are flagged `[PDF: check with pdftotext -layout]`. No shell was available.
- Wiki: `wiki-independents-allies/02-renaer-neverember.txt` (extract, 115 lines; line numbers below are extract lines). The extract is the Forgotten Realms Wiki page. Its infobox cites `WDH5e-p215-216` (Waterdeep: Dragon Heist, 5e) and `BST` (Blackstaff Tower, the novel). The wiki prints no edition on most lines; where a citation key is shown it is given.
- `sources/research/pass3-bundles/open-lord-and-masked-lords/wiki.txt` (Dagult's wiki page) was read by Grep for Renaer's mother and inheritance.
- `docs/plans/setting-compendium-research-notes/pass1-era4-era6.md:22` records a Patreon Renaer guide (1479 DR rescue). That guide is a `.docx` (see Not readable).
- `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **"Harper-adjacent" is contradicted by the published adventure, which says Renaer is a Harper.** The page L25 says "a Harper-adjacent ally of Mirt and Remi Haventree". The adventure says "As a Harper, he spends a lot of time defending Waterdavians" (`sources/adventure-wdh.json:32547`). The wiki says "By 1492 DR, Renaer had joined the Harpers." (extract line 86). The organization page follows the page, and the consistency note calls it a USER decision (`docs/plans/setting-compendium-research-notes/consistency-notable-figures.md:14`). Section D1.
2. **The page says the Blackstaff rescue of 1479 is "permanently in his debt". Only the Patreon guide (unreadable) and the force-grey page support the rescue, and the year is tagged `[research]`.** Section D8.
3. **Renaer carries an Eye of the Stone of Golorr in a locket, and does not know it.** This is day-one (the locket was given before Ches 1). The campaign's history and lore say so (`campaign/setting/history/06-the-open-lords-fall.md:85`; `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:34`). It is a hidden fact (ruling 19 Secret callout) and not on the page.
4. **The stat block is a Swashbuckler (adventure), but the Trollskull guide and Appendix D say "Noble stat block".** Section D2.

---

## A. Background facts by theme

### A1. Origin, parents and early life (published adventure, wiki and campaign)

> "Renaer is the estranged son of Dagult Neverember, the former Open Lord of Waterdeep and the current Lord of Neverwinter. Father and son detest one another, and Renaer is least happy when he finds himself forced to deal with some mess his father left behind. Qualities that both share include striking good looks, a love of drink, and a flair for diplomacy. What Renaer lacks is his father's belligerence, ill temper, and bad judgment."
> — `sources/adventure-wdh.json:32546` (Appendix B, page 215)

> "Renaer was born to Dagult Neverember, who served as the Open Lord of Waterdeep. Renaer's mother died in his youth. Renaer began managing his family's extensive property holdings while his father spent time at the palace."
> — extract line 66 (`History`; refs removed; the Blackstaff Tower novel is the cited source, `{{Cite book/Blackstaff Tower}}`, no page). Edition: the novel is not an edition.

> "His mother was a member of the Brandarth family."
> — extract line 82 (`Relationships`; ref `BST-p272`). Edition: novel.

> "Renaer's father was the Open Lord Dagult Neverember. His mother was a member of the Brandarth family. Renaer had a rocky relationship with his father. In contrast, he had a good relationship with his mother, who left everything to Renaer rather than Dagult."
> — extract line 82 (refs removed: `BST-p22`, `BST-p272`, `BST-p122`, `BST-p223`).

> "She bore him a son, Renaer, before dying when the boy was still in his youth and leaving everything to him instead of to Dagult."
> — `sources/research/pass3-bundles/open-lord-and-masked-lords/wiki.txt:361` (Dagult's wiki page; refs `BST-p22`, `BST-p223`; the line is "In Waterdeep, he married into the noble Brandarth family, adding his wife's broad property holdings and wealth to his own." before it).

> "Renaer is the estranged son ..." (page L25 and the adventure) — see A1 above.

Campaign, the mother's name (a conflict in the campaign's own notes, D5):
> "- Renaer Neverember is Dagult's son by Lady Alethea Brandath. His mother died when Renaer was still in his youth and left her property to Renaer and nothing to Dagult (Forgotten Realms Wiki, Dagult Neverember and Renaer Neverember; Blackstaff Tower)."
> — `campaign/setting/history/06-the-open-lords-fall.md:73`. The rest of the line: "The published adventure gives only the inheritance (`adventure-wdh.json` lines 32546-32547), which is the minimum this page relies on. Renaer now owns more property than anyone else in Waterdeep, all of it inherited from her."

Relatives in the wiki (edition not tagged; the BST citations are the Blackstaff Tower novel):
> "Renaer's great-great-granduncle was Kulzar Brandarth, a pirate. Another one of his ancestors was Varad Brandarth, one of the last students of Khelben \"Blackstaff\" Arunsun."
> — extract line 84 (refs `BST-p65`, `BST-p117-118`, `BST-p122`).

> "Renaer was talented at impressions, particularly with his voice. He collected books and was very well read in history and local lore."
> — extract line 79 (refs `BST-p63`, `BST-p270`). The page's Persona has "a collector of rare tomes" (`campaign/gazetteer/waterdeep/sea-ward.md:124`).

Dagult's line on his son (wiki, Blackstaff Tower 1479):
> "My son has become a man, and worse yet, a hero. Something this city has not seen in some time."
> — extract line 63 (Dagult, 1479 DR; ref `Blackstaff Tower-ch23`).

### A2. The Blackstaff years and the 1479 DR founding group (wiki; the rescue date is `[research]` in the campaign)

> "In Nightal of 1479 DR, Renaer was confronted by Laraelra Harsard about suspicious happenings at a property owned by the Neverember family. When he entered the house with Laraelra and her bodyguard Meloon Wardragon to investigate, they were kicked out by Khondar Naomal, who was using the house with the permission of Dagult Neverember. Renaer and friends returned at night and found the Blackstaff's Heir Vajra Safahr, who had been imprisoned and tortured by Khondar beneath the house in a plot to seize control of the city."
> — extract line 68 (markup removed; ref `Blackstaff Tower-ch`, novel).

> "The group rescued Vajra and they fled with his companions through a portal in Neverember Manor to Varadras, disused estate outside Waterdeep. Khondar publicly accused Renaer of murdering Vajra."
> — extract line 68 (the same paragraph).

> "As Laraelra, Meloon, and Osco Salibuck tried to head Khondar off, Renaer met with his father, the Open Lord, and threatened to reveal Dagult's involvement in Khondar's actions unless Dagult rescinded the charges against Renaer and his friends and allowed Renaer additional autonomy in the Neverember household, including restoring Neverember Manor to its original name Brandarthall."
> — extract line 70 (markup removed; the same paragraph continues: "Renaer and Dagult returned to Blackstaff Tower in time to witness Khondar be killed by spectral hounds of the Black Hunt.")

> "With Vajra's approval, a tenday later Renaer founded a group similar to the Moonstars to serve as heroes of the city. The first members of this group included Renaer, Vajra, Laraelra, Meloon, and Eiruk Weskur."
> — extract line 72 (ref `BST-p305`). This is the wiki's founding group. The campaign's Black Tears is not named in the wiki (see G and Not found).

Campaign, the rescue and its date:
> "1479 DR, the rescue: Renaer Neverember and Meloon Wardragon rescued Vajra from agents of Khondar Naomal. Meloon's page places the rescue more than a decade ago, and Renaer's page says it left the Blackstaff permanently in his debt (**Meloon Wardragon**; **Renaer Neverember**). The year itself is `[research]`."
> — `campaign/setting/organizations/05-force-grey.md:28`.

> "Meloon Wardragon is an active member who reports to Vajra, whose life he saved more than a decade ago alongside Renaer. His page is in the Independents and Allies group."
> — `campaign/setting/organizations/05-force-grey.md:109`.

Campaign, the 1479 date as a research tag (the Patreon source is unreadable):
> "The 1479 DR date of the rescue comes only from a Patreon Renaer guide recorded in `pass1-era4-era6.md:22` and `history/06-the-open-lords-fall.md:164`, and it is tagged `[research]`."
> — `campaign/setting/organizations/05-force-grey.md:150`.

### A3. Dagult's ouster and the estrangement (day-one; published adventure and campaign history)

> "In 1489 DR the Masked Lords voted him out while he was in Neverwinter, and Laeral Silverhand took the office at their request. His agents took the Stone from the palace and lost it on the way out of the city."
> — `campaign/setting/history/06-the-open-lords-fall.md:24`.

> "Dagult leaves Waterdeep to rebuild Neverwinter and is ousted as Open Lord of Waterdeep."
> — `sources/adventure-wdh.json:822`. The date is not given there.

> "\"When the Lords of Waterdeep ousted my father, I thought his long, dark shadow was finally gone for good. The truth is, I want nothing to do with him. But his spies hound me. One of them, a gnome named Dalakhar, had been watching me for months.\""
> — `sources/adventure-wdh.json:4781` (Renaer's speech in "What Renaer Knows", Chapter 3). The rest of the same speech is quest-time: "Then, about two tendays ago, the spy was suddenly nowhere to be seen. My father didn't trust many people, but he trusted that gnome."

> "\"The Zhentarim thinks that my father embezzled a large amount of gold while he was Open Lord, and that he hid the dragons somewhere in the city. ... My father and I haven't spoken in years.\""
> — `sources/adventure-wdh.json:2121`. The ellipsis skips the Stone-of-Golorr sentences. Quest-time (the warehouse interview); the estrangement is day-one. Exact text of the skipped sentences: "They think they can find it by using an artifact called the Stone of Golorr, which was in the hands of the Xanathar Guild until recently. Apparently, someone stole it. The Zhents thought I knew something about all of this, but I don't."

> "Renaer's estrangement from his father is nothing but an act" — not in the sources. The adventure says: "Some believe that Renaer's estrangement from his father is nothing but an act, and that anyone who bears the Neverember name is an enemy of Waterdeep. Renaer just shakes his head at such accusations and gets on with his life. He has many powerful friends to watch his back."
> — `sources/adventure-wdh.json:32548`.

### A4. His house, his money and his way of life (published adventure, wiki and campaign)

> "Renaer lives off a sizable inheritance left to him by his mother. Approaching middle age, he has given up adventuring and settled down somewhat. As a Harper, he spends a lot of time defending Waterdavians against those who, like his father, would deprive them of their coin and rights. He owns Neverember House, a four-story residence in the Sea Ward. Renaer spends as little time there as possible, however, since it's constantly under surveillance by spies loyal to his father. His friends have an open invitation to use the house as they please, while Renaer spends most of his free time in taverns and festhalls."
> — `sources/adventure-wdh.json:32547` (Appendix B, page 215). The "As a Harper" clause is the conflict in D1.

> "- A four-story house owned by Renaer Neverember. He spends as little time here as he can, because spies loyal to his father, Dagult Neverember, watch it constantly. His friends have an open invitation to use it as they please."
> — `campaign/gazetteer/waterdeep/sea-ward.md:85`.

> "- The estranged son of Dagult Neverember, a well-read collector of rare tomes who knows the city's factions, geography and politics. He owns considerable property in Waterdeep, all of it inherited from his mother."
> — `campaign/gazetteer/waterdeep/sea-ward.md:124`.

> "Renaer Neverember is the estranged son of Dagult Neverember — sharp, well-read, and knowledgeable about every faction operating in the city. He owns considerable property in Waterdeep and fights alongside those he trusts."
> — `campaign/setting/notable-figures/independents-allies/02-renaer-neverember.md:29` (the page's Overview).

> "- Renaer's loan is the one the party will forget about and feel guilty about later."  — NOT USED (party-side). Instead: "Renaer Neverember | Up to 200 gp | Coin, no interest, \"when convenient\" | Party's choice; Renaer will never ask | Technically indefinite; morally, they should pay it" — `sources/Appendix_D_-_Running_the_Tavern.md:869` (Alexandrian; a tavern-finance loan, quest-time once the tavern is owned).

### A5. Friends, the Black Tears and the circle (campaign only; not in the wiki or adventure)

Campaign statements (day-one-style, but the Black Tears is a campaign invention):
> "- **Renaer Neverember** ... " — none. The page L25 says: "the leader of the Black Tears (his personal circle of trusted companions)".
> — page L25 (`campaign/setting/notable-figures/independents-allies/02-renaer-neverember.md:25`).

> "Eiruk is a priest of Oghma and a member of Renaer Neverember's Black Tears, steady and patient, the one the group looks to when their decisions carry weight."
> — `campaign/setting/notable-figures/independents-allies/11-eiruk-weskur.md:29`.

> "Laraelra Harsard is a half-elf mage and a member of Renaer Neverember's trusted circle, the Black Tears, known for checking exits and keeping wards on her companions."
> — `campaign/setting/notable-figures/independents-allies/08-laraelra-elra-harsard.md:29`.

The source check: `sources/adventure-wdh.json` (no hit for "Black Tears"), the wiki extracts (no hit), the Alexandrian Markdown (no hit). The name first appears in campaign files; `session 5 handoff.md:18` names "Black Tears members" in `campaign/structure/appendix-a-npc-roster.md` (a file no longer at that path).

Friends in the adventure and wiki (day-one):
> "Renaer ... the devoted friend of Floon Blagmaar" — page L25; the source is "Floon was a friend to both Renaer and Volothamp." (extract line 81 of the Floon page, `wiki-independents-allies/04-floon-blagmaar.txt`; ref `WDH5e-p5-6`).

> "Meloon Wardragon ... serves the goddess Tymora and loves a good fight. His friends-among them {@creature Renaer Neverember|wdh} and {@creature Vajra Safahr|WDH}-describe him as honest, optimistic, and extraordinarily lucky."
> — `sources/adventure-wdh.json:32255` (Meloon's Appendix B entry; the line continues: "Until recently, he was a member of Force Grey and reported directly to the Blackstaff. In recent months, Meloon has spent much of his time at the Yawning Portal."). The source does not say "closest living friend" (D6).

> "An intellect devourer in league with {@creature Xanathar|WDH} ate Meloon's brain several months ago."
> — `sources/adventure-wdh.json:1548` (Familiar Faces; day-one, before Ches 1). This supports the page's "whose changed behavior has him alarmed".

### A6. Harpers (day-one membership, as the published adventure and wiki give it)

> "By [[1492 DR]], Renaer had joined the [[Harpers]]."
> — extract line 86 (ref `WDH5e-p215`).

> "* [[Renaer Neverember]], valiant Harper and son of the famous [[Dagult Neverember]] of Neverwinter."
> — `sources/research/pass5-bundles/harpers/wiki.txt:464` (the wiki's Harpers list; ref `WDH5e-p215`).

> "Renaer Neverember is a Harper-adjacent ally of Mirt and Remi, and this page does not list him as a member."
> — `campaign/setting/organizations/01-harpers.md:58` (the campaign's view; see D1).

### A7. Eye of the Stone of Golorr in a mourning locket (day-one; hidden)

> "- Neverember placed the three Eyes in three places before the vote. He kept one with him in Neverwinter, he gave one to Renaer inside an ivory mourning locket in honor of his mother, and he hid one in the Brandath Crypts near Alethea's tomb. The Renaer and Brandath placements are in the Alexandrian account, and the Crypts and the tomb are in the Vault of Dragons quest opener."
> — `campaign/setting/history/06-the-open-lords-fall.md:85`.

> "- **Where Neverember put them:** He kept one with him in Neverwinter. He gave one to his son Renaer inside an ivory mourning locket made in honor of Renaer's mother, and Renaer never knew what it held. He hid one in the Brandath Crypts near Alethea Brandath's tomb."
> — `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:34`.

> "- Renaer refused to help his father hide the gold. He knows nothing about the vault, the Stone's part in it or what his locket held, and his ignorance is genuine."
> — `campaign/setting/history/06-the-open-lords-fall.md:75`.

Alexandrian PDF, printed p.105 `[PDF: check with pdftotext -layout]`:
> "His father had given him an elaborate, ivory mourning locket in honor of his mother. The Eye was hidden inside it."
> — `sources/14. Finding Floon.pdf`, printed p.105 (PDF page 4).

> "- Neverember's agents did not know the full picture. Dalakhar was told to watch Renaer and not told why, because Neverember's chief concern was keeping the hidden Eye safe until he could regain the Stone."
> — `campaign/setting/history/06-the-open-lords-fall.md:88`.

> "- Renaer Neverember ... " — the locket is taken at the warehouse on the night before Ches 1 (quest-time; see C).

### A8. Personal relationships and voice (campaign, day-one)

> "Renaer lives off a sizable inheritance" — see A4.
> "Renaer's trust is easily gained but impossible to restore once broken." — page L23 (`campaign/setting/notable-figures/independents-allies/02-renaer-neverember.md:23`). The phrase matches the adventure's warehouse scene (`sources/adventure-wdh.json:2113`: "His trust is easily gained but impossible to restore once broken.") (quest-time scene, but the trait is day-one).

Voice profile (`.claude/skills/character-voices/voices/independents-allies.md`):
> "Relaxed, articulate, medium-to-long sentences, a knowledgeable friend explaining the city. He deflects sincerity with a joke, then follows with one short, dead-serious line."
> — line 52.
> "Sorry. The name." / "Ask me anything about this city, I'll probably know." / "That's my father's work, isn't it." — line 57 (signature phrases).

---

## B. Alignment, species, pronouns, stat block

**Summary line (page L5):** "- *Illuskan human noble, chaotic good, he/him*. Stat block: **Swashbuckler**." — `campaign/setting/notable-figures/independents-allies/02-renaer-neverember.md:5`

**Alignment**
- Adventure: "Renaer is chaotic good." — `sources/adventure-wdh.json:32559`.
- Wiki: "| alignment5e    = [[Chaotic good]]" — extract line 57. "| challenge5e    = 3" — line 58.
- Agreement: chaotic good in both.

**Species and ethnicity**
- Adventure: "{@creature Renaer Neverember|wdh} is an Illuskan human who has the statistics of a {@creature swashbuckler|VGM}, with these changes:" — `sources/adventure-wdh.json:32555`.
- Wiki: "| race           = [[Human]]<ref name=\"WDH5e-p215-216\" />" (extract line 14); "| ethnicity      = [[Illuskan]]<ref name=\"WDH5e-p215-216\" />" (extract line 15).
- Agreement: Illuskan human.

**Pronouns**
- Wiki: "| sex            = Male" — extract line 13.
- Adventure: "Renaer is chaotic good." (no pronoun); the adventure's Renaer uses "he" in `:32547` ("Approaching middle age, he has given up adventuring").
- Page: "he/him" (L5). Consistent with the sources.

**Stat block**
- Adventure: "statistics of a {@creature swashbuckler|VGM}" — `sources/adventure-wdh.json:32555`.
- Wiki: "| class5e        = [[Swashbuckler]]" (extract line 59).
- Trollskull guide: "**Renaer Neverember** *(Noble stat block, CG Illuskan human)*" — `campaign/guides/trollskull-manor/08-notable-patrons.md:48`. Conflict, D2.
- Appendix D: "*Waterdeep Noble — CG Illuskan human, Noble stat block*" — `sources/Appendix_D_-_Running_the_Tavern.md:1300`. Conflict, D2.

**Name and titles**
- Wiki: "| nicknames      = Ren<ref name=\"BST-p13 \">{{Cite book/Blackstaff Tower|13}}</ref>" (extract line 9).
- Wiki: "| titles         = " (blank, extract line 7).
- Adventure: "Renaer is the estranged son of Dagult Neverember, the former Open Lord of Waterdeep and the current Lord of Neverwinter." (`:32546`).

---

## C. Quest-time sentences on the current page (and the voice profile)

Brief ruling 1: restate as day-one, or remove and route. Each row gives the page line, the sentence, and where the quest fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L7 | "- **Featured in:** **Finding Floon**, **Trollskull Alley**, **Fireball!**, **Gralhund Villa**, **Cassalanter Villa**, **Vault of Dragons**, **The Stone's Other Master**, **The Dragon in the Harbor**, **Gralhund Villa (location)**, **Zhentarim Warehouse**, **Xanathar Sewer Hideout**" | Route. Each name is checked in D9 | Finding Floon: `campaign/quests/act-i/finding-floon/overview.md`; Trollskull Alley: `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md`; Fireball!: `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:173`; Gralhund Villa: `campaign/quests/act-ii/gralhund-villa/ev-05-the-guest-suite.md:49`; Vault of Dragons: `campaign/setting/lore/vault-of-dragons.md:118`; The Stone's Other Master: `campaign/quests/faction-events/harpers/m06-the-stones-other-master/ev-01-the-stones-other-master.md`; The Dragon in the Harbor: `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/overview.md:17`; Zhentarim Warehouse: `campaign/locations/zhentarim-warehouse/z05-offices.md:11`; Xanathar Sewer Hideout: `campaign/locations/xanathar-sewer-hideout/area-overview.md:75` |
| 2 | L13 | "Renaer most often feels steady determination, self-deprecating humor, fierce loyalty, suppressed anger toward his father, open warmth toward friends, guilt about the dangers his name attracts, and a growing, private alarm at what Meloon has become." | Day-one (Meloon's change predates Ches 1, `sources/adventure-wdh.json:1548`). Keep | A1 and A5 |
| 3 | L21 | "He owns more property than anyone in the city, all of it inherited from his mother (Dagult received nothing)." | Day-one in content. The claim "more than anyone" has no source outside the campaign's history (D4) | `campaign/setting/history/06-the-open-lords-fall.md:73`; wiki extract line 82 |
| 4 | L21 | "To those he trusts, he is self-deprecating about his name, deflects sincerity with humor, and becomes completely serious when the Vault or Floon comes up." | Day-one character trait. Keep | `sources/Appendix_D_-_Running_the_Tavern.md:1304` (Alexandrian) |
| 5 | L23 | "His trust is easily gained but impossible to restore once broken." | Trait taken from the warehouse scene. Keep as a trait | `sources/adventure-wdh.json:2113` (quest scene; the sentence is a trait) |
| 6 | L25 | "Renaer is the estranged son of Dagult Neverember (former Open Lord, current Lord of Neverwinter), the devoted friend of Floon Blagmaar, the closest living friend of Meloon Wardragon (whose changed behavior has him alarmed), a man who rescued Vajra Safahr from Khondar Naomal's agents and left the Blackstaff permanently in his debt, a Harper-adjacent ally of Mirt and Remi Haventree, and the leader of the Black Tears (his personal circle of trusted companions)." | Mixed. "the closest living friend" is unsourced in the adventure and wiki (F4). "left the Blackstaff permanently in his debt" is `[research]` (A2). "Harper-adjacent" conflicts (D1). "the leader of the Black Tears" is campaign-only (A5) | See A1, A2, A5, A6 |
| 7 | L29 | "Renaer Neverember is the estranged son of Dagult Neverember — sharp, well-read, and knowledgeable about every faction operating in the city. He owns considerable property in Waterdeep and fights alongside those he trusts." | Day-one. Keep | `campaign/gazetteer/waterdeep/sea-ward.md:124` |

**Voice profile quest-time clauses (`.claude/skills/character-voices/voices/independents-allies.md`):**

- Line 54, Swearing: "Casual among the Black Tears and the party (\"Shit, that's my father's handiwork.\")." — "the party" is a quest-time reference. Restate as "casual among friends", or keep as a day-one habit. Drafter's call (ruling 16 change is for the orchestrator).
- Line 60, Sample line, Greeting: "You're the ones who dragged Floon out of that warehouse. I owe you more than a drink, but let's start with the drink." — quest-time (the rescue at the warehouse). Route to Finding Floon.
- Line 61, Sample line, Business: "The Zhentarim splinter runs out of the Dock Ward, the Xanathar's people are under it, and my father's money is somewhere in the middle. That's the short version." — day-one knowledge. Keep.
- Line 62, Sample line, Under pressure: "No. Not like him. I won't do it like him. Give me a minute." — day-one. Keep.
- Lines 51 to 53, 55 to 58 (Sound, Sentence shape, Word choice, Personality in speech, Quirks, Signature phrases, Never) have no quest-time clause. Line 55 ("Private alarm about Meloon shows as uncharacteristically hesitant questions.") is day-one (A5).

**Quest-time facts already in other files (route; do not restate on the day-one page):**
- The night-before kidnapping and the warehouse: `campaign/setting/history/08-the-players-arrive.md:25` ("- Floon Blagmaar is taken on the night before Ches 1, and the party's arrival at the Yawning Portal the next evening begins the campaign.") and `campaign/guides/gm-guide/structural-rules.md:38` ("Floon was kidnapped the night before."). Renaer's seizure: `campaign/setting/organizations/09-manshoons-zhentarim.md:33` ("- **The night before Ches 1, 1492 DR, Renaer Neverember:** Five Zhentarim thugs working for Urstul Floxin seized Renaer Neverember to learn what he knew about his father's hidden gold, and they took Floon Blagmaar in the same attack. House Gralhund paid for the operation (*Dragon Heist*, 5e; **House Gralhund**). Xanathar's Guild raided the Candle Lane warehouse where the thugs held both men and killed the cell's agents there (*Dragon Heist*, 5e).").
- The published adventure's kidnapping scene: `sources/adventure-wdh.json:2114` ("On the night of the abduction, Renaer was concerned that Floon was too intoxicated to find his way home by himself and offered to escort him. The two were jumped by five thugs as they left Fillet Lane and headed north on Zastrow Street.") and `:2115` ("Renaer feels guilty that Floon was taken, since he believes (correctly) that they mistook Floon for him.").
- Locket taken: `campaign/setting/history/06-the-open-lords-fall.md:136` ("- Ches 1, 1492 DR: the campaign opens. Manshoon's cell took Renaer's locket the night before."); `campaign/quests/act-i/finding-floon/ev-03-zhentarim-warehouse.md:53` ("- The Zhentarim took his mourning locket, which he believed held a keepsake from his mother; he didn't know there was a hidden compartment").
- Gralhund funding of the seizure: `campaign/setting/history/08-the-players-arrive.md:58` ("- The Gralhunds funded the Zhentarim seizure of Renaer Neverember to gain leverage over Dalakhar, according to Orond Gralhund, who says Yalah Gralhund arranged it. Source: **Gralhund Villa**, the guest suite.") and `campaign/quests/act-ii/gralhund-villa/ev-05-the-guest-suite.md:49`.
- Volo's party and the rescue: `sources/adventure-wdh.json:3582` ("Word begins to spread throughout Waterdeep that a group of adventurers helped Volothamp Geddarm and rescued {@creature Renaer Neverember|wdh}."); `campaign/quests/act-i/trollskull-alley/ev-01-welcome-to-trollskull-alley.md` (the Renaer welcome; not read in this pass).
- Fireball knowledge (Renaer's Harper contact): `sources/adventure-wdh.json:4776` ("At some point during their investigation, the characters might want to speak to {@creature Renaer Neverember|wdh} about the fireball, given his own recent brush with the Zhentarim.") and `sources/Act_III_Arc_D.md:239` ("If the characters mention Fala's sighting of the burned man fleeing toward the Bent Nail, Renaer reaches out to his Harper contacts. Within a day, he returns with the following:").
- Floon's warehouse exchange (quest-time): `sources/adventure-wdh.json:2972` ("Volo, Floon, and Renaer all express their gratitude through camaraderie.").
- Renaer's Zhentarim seizure motive and Dalakhar: `campaign/quests/act-ii/gralhund-villa/ev-05-the-guest-suite.md:49` ("**4. The Neverember abduction.** The house funded Zhentarim agents who seized Renaer Neverember the night Floon Blagmaar was taken, before the fireball, before the Stone. Yalah arranged it. The point was leverage to recover the Stone from Dalakhar, the gnome who stole it from Lord Neverember's people.").

---

## D. Conflicts

**D1. Harper status**
- Page L25: "a Harper-adjacent ally of Mirt and Remi Haventree" — `campaign/setting/notable-figures/independents-allies/02-renaer-neverember.md:25`.
- Adventure: "As a Harper, he spends a lot of time defending Waterdavians against those who, like his father, would deprive them of their coin and rights." — `sources/adventure-wdh.json:32547`.
- Wiki: "By [[1492 DR]], Renaer had joined the [[Harpers]]." — extract line 86.
- Wiki list: "valiant Harper and son of the famous" — `sources/research/pass5-bundles/harpers/wiki.txt:464`.
- Campaign organization page: "Renaer Neverember is a Harper-adjacent ally of Mirt and Remi, and this page does not list him as a member." — `campaign/setting/organizations/01-harpers.md:58`; and the conflict note "**Conflicts:** Renaer. The wiki lists Renaer Neverember as a \"valiant Harper\" (`wiki.txt:464`) and the published adventure says \"As a Harper, he spends a lot of time defending Waterdavians\" (`sources/adventure-wdh.json:32547`), while his Notable Figures page (`02-renaer-neverember.md:25`) calls him \"a Harper-adjacent ally of Mirt and Remi Haventree\". The page follows the Notable Figures page and does not list him under Key Members." — `campaign/setting/organizations/01-harpers.md:185`.
- Mirt's page: "- **Renaer Neverember:** A Harper-adjacent ally of Mirt and Remi." — `campaign/setting/notable-figures/harpers/01-mirt.md:40`.
- Consistency note: "Renaer NF independents-allies/02:7,26: \"Independent (ally)\", \"Harper-adjacent\" vs WDH:32547 \"As a Harper\" and wiki Renaer:88 (joined the Harpers by 1492). USER decision." — `docs/plans/setting-compendium-research-notes/consistency-notable-figures.md:14`.
- Higher ranked: the published adventure (over the campaign's Notable Figures page; the adventure is the source, and the page is a draft). Brief ruling 6 says to check the group folder and organization page, and the organization page follows the page. Open conflict for the user.

**D2. Stat block (Swashbuckler vs Noble)**
- Adventure: "Renaer Neverember|wdh} is an Illuskan human who has the statistics of a {@creature swashbuckler|VGM}" — `sources/adventure-wdh.json:32555`.
- Wiki: "| class5e        = [[Swashbuckler]]" — extract line 59.
- Trollskull guide: "**Renaer Neverember** *(Noble stat block, CG Illuskan human)*" — `campaign/guides/trollskull-manor/08-notable-patrons.md:48`.
- Appendix D: "*Waterdeep Noble — CG Illuskan human, Noble stat block*" — `sources/Appendix_D_-_Running_the_Tavern.md:1300`.
- Higher ranked: the adventure and wiki (Swashbuckler). The page is right. The two guides are stale (Alexandrian and campaign).

**D3. Age**
- Adventure: "Approaching middle age, he has given up adventuring and settled down somewhat." — `sources/adventure-wdh.json:32547`.
- Appendix D: "Tall, sandy-haired, looks younger than his years in a way that has always made the older noble families slightly mistrustful of him." — `sources/Appendix_D_-_Running_the_Tavern.md:1302`. This is appearance, not age; it does not contradict. No age is on the page.

**D4. Property**
- Page L21: "He owns more property than anyone in the city, all of it inherited from his mother (Dagult received nothing)."
- Campaign history: "Renaer now owns more property than anyone else in Waterdeep, all of it inherited from her." — `campaign/setting/history/06-the-open-lords-fall.md:73`.
- Adventure: "He owns Neverember House, a four-story residence in the Sea Ward." — `sources/adventure-wdh.json:32547`. The adventure says nothing about "more than anyone".
- Wiki: "In Waterdeep, he married into the noble Brandarth family, adding his wife's broad property holdings and wealth to his own." — `sources/research/pass3-bundles/open-lord-and-masked-lords/wiki.txt:361`. "Leaving everything to him instead of to Dagult" is in the same line. The wiki says the holdings were the Brandarths' and went to Renaer, not that he owns "more than anyone".
- Higher ranked: the adventure and wiki for the inheritance; "more than anyone" is campaign-only. Drafter: keep "all of it inherited from his mother" and tag "more than anyone" `[research]`.

**D5. Mother's name**
- Campaign history: "Renaer Neverember is Dagult's son by Lady Alethea Brandath." — `campaign/setting/history/06-the-open-lords-fall.md:73`.
- Campaign history note: "**Conflicts:** The name of Renaer's mother. The Alexandrian and `arc-j` say Alethea Brandath, the Patreon material says Alathea, and the wiki says Brandarth. This page follows the campaign." — `campaign/setting/history/06-the-open-lords-fall.md:158`.
- Wiki: "His mother was a member of the Brandarth family." — extract line 82. The wiki does not name her.
- Higher ranked: the campaign's own history (the page follows it). The name is a family name in the wiki and a given name in the campaign.

**D6. "Closest living friend" of Meloon**
- Page L25: "the closest living friend of Meloon Wardragon".
- Adventure: "His friends-among them {@creature Renaer Neverember|wdh} and {@creature Vajra Safahr|WDH}-describe him as honest, optimistic, and extraordinarily lucky." — `sources/adventure-wdh.json:32255`.
- Force Grey (quest files): "Renaer Neverember (independent): Meloon's closest friend, an anchor if the party sends for him." — `campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/overview.md:80`. This is a quest file.
- Higher ranked: the adventure says "friends" (plural). "Closest" is a campaign quest-file phrase. Drafter: keep "a close friend" or tag `[research]`.

**D7. Black Tears**
- Page L25 and the voice profile name the Black Tears. No published or wiki source. The campaign's other pages (`11-eiruk-weskur.md:29`, `08-laraelra-elra-harsard.md:29`) use the same name. Not a conflict with a source; flagged as campaign-only (A5).

**D8. The Blackstaff rescue**
- Page L25: "a man who rescued Vajra Safahr from Khondar Naomal's agents and left the Blackstaff permanently in his debt".
- Wiki: "Renaer and friends returned at night and found the Blackstaff's Heir Vajra Safahr ..." and "The group rescued Vajra" (extract line 68). The wiki's account has the group, not Renaer alone; the wiki does not say "in his debt".
- Force Grey page: "Renaer's page says it left the Blackstaff permanently in his debt" and the year is `[research]` (`campaign/setting/organizations/05-force-grey.md:28`, `:150`).
- Higher ranked: the wiki for the events; the year `[research]`. "In his debt" has no source. Drafter: tag it.

**D9. Featured-in list**
- Page L7 lists "**Cassalanter Villa**" and "**Vault of Dragons**". The quest journals for those are not yet drafted. `campaign/structure/arc-g-cassalanter-villa.md:15` and `campaign/structure/arc-j-vault-of-dragons.md:355` ("## Dagult Neverember and the NeverSword") are the structure docs that name Renaer, and `campaign/setting/lore/vault-of-dragons.md:118` says "The Scene 5 duel with Renaer is optional and player-driven." The Vault option is a Renaer duel (brief note). The Cassalanter appearance is the structure doc only. Not a conflict; routed to the structure docs.
- Page L7 lists "**Gralhund Villa (location)**", "**Zhentarim Warehouse**" and "**Xanathar Sewer Hideout**" (locations). The Renaer mentions are in `campaign/locations/zhentarim-warehouse/z05-offices.md:11` and `campaign/locations/xanathar-sewer-hideout/area-overview.md:75`.

---

## E. Stale lines in other files (not edited) and routed quest references

**E1. Stale or conflicting campaign lines**
- `campaign/setting/organizations/01-harpers.md:58` and `:185`: follow the page's "Harper-adjacent" (D1). Stale against the adventure.
- `campaign/guides/trollskull-manor/08-notable-patrons.md:48` and `sources/Appendix_D_-_Running_the_Tavern.md:1300`: "Noble stat block" (D2). Stale against the adventure.
- `campaign/setting/history/06-the-open-lords-fall.md:73`: "Renaer now owns more property than anyone else in Waterdeep" (D4). Campaign-only.
- `campaign/setting/history/08-the-players-arrive.md:136` says the Gralhund Villa events "now say the night Floon Blagmaar was taken". Current, not stale.
- `campaign/quests/act-ii/gralhund-villa/ev-05-the-guest-suite.md:49` names Dalakhar as "the gnome who stole it" (motive for the seizure). The Gralhund page notes the conflict with `running-the-villains.md:19` (`campaign/setting/organizations/12-house-gralhund.md:162`). Not a Renaer page fact; listed because it touches the seizure.
- `campaign/setting/organizations/12-house-gralhund.md:24` ("- **Months before Ches 1, 1492 DR:** The house embedded agents in Renaer Neverember's household. They spotted Dalakhar watching Renaer, identified him as an agent of Lord Neverember, and followed him when he was pulled off that assignment to Xanathar's Guild."). Day-one, and it matches the Alexandrian p.20.

**E2. Routed quest references**
- Finding Floon overview: `campaign/quests/act-i/finding-floon/overview.md:48` (see the Volo notes) and the Renaer lines at `:51` to `:53` (the history note says "`finding-floon/overview.md` lines 51-53 call Renaer \"the Open Lord's estranged son\". He is the former Open Lord's son." — `campaign/setting/history/06-the-open-lords-fall.md:157`).
- Finding Floon warehouse: `campaign/quests/act-i/finding-floon/ev-03-zhentarim-warehouse.md:53` to `:58` (the locket and "What Renaer doesn't know").
- Fireball!: `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:173` ("Renaer knows the *Stone of Golorr* is \"the key to everything\" but not about the Eyes or the vault's location. He carries guilt for not acting on the message immediately — he read it and set it aside for an hour.").
- Force Grey m03: `campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/ev-02-the-extraction.md:76` ("- **Renaer.** If the party sends for Renaer Neverember, he arrives within the hour. As Meloon's closest friend he is an anchor who knows him, so his checks have Advantage.").
- Xanathar Sewer Hideout: `campaign/locations/xanathar-sewer-hideout/area-overview.md:75` ("> - The Q03 strongbox has been forced open and emptied. A thin brass chain with a snapped clasp lies in the bottom. Renaer Neverember recognizes it as his locket's chain if he is with the party or sees it later.").
- Trollskull Manor guide: `campaign/guides/trollskull-manor/06-tavern-time.md:28`, `:33`, `:34`, `:35`, `:63`, `:64`, `:88` (the Renaer rows and the Renaer's Friends table); `campaign/guides/trollskull-manor/02-operating-costs.md:87` ("- **Renaer Neverember (not a faction):** Covers estate transfer tax plus up to 200 gp, framed as a loan with no interest and no actual expectation of repayment. He will be embarrassed by profuse thanks.").
- Structure doc (Vault): `campaign/structure/arc-j-vault-of-dragons.md:355` to the section "Dagult Neverember and the NeverSword".

**E3. Stale wiki and Alexandrian line on the rescue**
- `docs/plans/setting-compendium-research-notes/consistency-history-vs-wiki.md:39`: "W:Renaer_Neverember:68 \"in his youth\"" (the mother's death; the wiki's line 66 is the phrase, line 68 is the rescue). Not a campaign line.

---

## F. Gaps a Background would need that no source gives

1. **Age and birth year.** No source. The wiki's infobox has "| age            = " and "| dob            = " blank (extract lines 17, 21). The adventure says "Approaching middle age" (`:32547`). Stay consistent with: middle-aged, and a mother who died while he was "still in his youth" (extract line 66).
2. **His mother's name.** Conflict D5. The campaign says Alethea Brandath (`history/06:73`). The wiki says only "Brandarth family" (extract line 82). Tag `[research]` if used.
3. **How he came to the Harpers.** The wiki says only "By 1492 DR, Renaer had joined the Harpers" (extract line 86). No source gives a teacher or date. Stay consistent with the 1492 date and D1.
4. **His faith.** The campaign's `campaign/setting/deities/mielikki.md:68` says "a locket in the Zhentarim warehouse offices bears a horse head that suggests Renaer Neverember's mother was a devotee" (a campaign inference; the locket is in `campaign/locations/zhentarim-warehouse/z05-offices.md:9`, which says "suggesting Renaer's mother was a devotee"). No source names a deity for Renaer or his mother. Do not give him a deity.
5. **The Black Tears' origin.** Campaign-only. The wiki's 1479 DR founding group is "Renaer, Vajra, Laraelra, Meloon, and Eiruk Weskur" (extract line 72). A Background can use the wiki's group under its own name, or leave the Black Tears to the campaign files.
6. **His own friends who are not named by a source.** The sources name Floon (`sources/adventure-wdh.json:32547`? no: the friendship is at `:2972`), Meloon (`:32255`), Vajra (`:32255`), Laraelra and Eiruk (wiki extract line 72), Volo (`:2972`), Mirt (`:1391`, "a Masked Lord who serves as {@creature Laeral Silverhand|wdh}'s advisor").
7. **His Dalakhar relationship before Ches 1.** Renaer's own words (`sources/adventure-wdh.json:4781`) and the Alexandrian account (`sources/2. Other Factions.pdf`, printed p.20: "Thinking outside of the box, they embedded agents in Renaer Neverember's household months ago."). The campaign's own date: `campaign/setting/organizations/12-house-gralhund.md:24` ("Months before Ches 1, 1492 DR"). Stay consistent with: Dalakhar watched Renaer for months before the kidnapping (day-one), and the house's agents caught him.
8. **Whether he knew of the locket.** Renaer "never knew what it held" (`campaign/setting/lore/stone-of-golorr-and-the-eyes.md:34`) and "He knows nothing about the vault, the Stone's part in it or what his locket held" (`campaign/setting/history/06-the-open-lords-fall.md:75`). Stay consistent with: he did not know the compartment existed (`sources/14. Finding Floon.pdf`, printed p.106, "If they find the locket and see the (now empty) secret compartment inside it, Renaer can also tell them that he had no idea that the compartment existed or what was stored inside it.").
9. **His personal goals.** The campaign's own Motivations line: "Renaer wants to live on his own terms without his father's shadow, protect the people who get hurt because of the Neverember name, and prove that estrangement from Dagult is conviction rather than cowardice." (page L15). The Alexandrian p.? "Renaer Neverember ... Invites the characters to a party at Brandarthall" (`sources/Appendix_D_-_Running_the_Tavern.md:1308`) is a patron topic, not a goal.

**Searched, not found (Renaer, day one):** "Black Tears" (`sources/adventure-wdh.json`, the wiki extracts, `sources/` Markdown: no hit); "closest friend" of Renaer or Meloon (adventure: no hit; quest file only); his age (adventure: "Approaching middle age" only); his deity (campaign: inference only); "debt" to the Blackstaff in any published source (no hit).

---

## G. Inner-life hints in the sources (exact quotes)

These are the sourced hints a Background or the personal goals may use. They must not be contradicted.

- **Dislikes his father, and it shows as bitter jokes.** "The suppressed anger at his father comes out in clipped, bitter jokes." — voice profile, `.claude/skills/character-voices/voices/independents-allies.md:55`.
- **Fears being like Dagult.** "Deep down, he shares his father's charm and intelligence but lives in fear that he also shares the belligerence, ill temper, and bad judgment." — page L21. Source: "What Renaer lacks is his father's belligerence, ill temper, and bad judgment." — `sources/adventure-wdh.json:32546`.
- **"I want nothing to do with him."** — `sources/adventure-wdh.json:4781` (Renaer's speech; the quest-time sentence after it is not used).
- **Refuses to be the Neverember name's shadow.** "Renaer just shakes his head at such accusations and gets on with his life." — `sources/adventure-wdh.json:32548`.
- **Guilt over Floon.** "Renaer feels guilty that Floon was taken, since he believes (correctly) that they mistook Floon for him." — `sources/adventure-wdh.json:2115` (quest-time event, but the guilt is a trait).
- **Mother's locket and the mother.** "He gave one to his son Renaer inside an ivory mourning locket made in honor of Renaer's mother, and Renaer never knew what it held." — `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:34`. "In contrast, he had a good relationship with his mother, who left everything to Renaer rather than Dagult." — extract line 82.
- **The mother's keepsake.** "They took his mourning locket; he believed it held a keepsake from his mother; he didn't know there was a compartment inside" — `campaign/locations/zhentarim-warehouse/z02-storage-closet.md:16` (quest-time; the belief is a day-one trait).
- **Honesty about his own life.** "This is not self-pity. It is honest." — `sources/Appendix_D_-_Running_the_Tavern.md:1309` (on his father's legacy).
- **Trust.** "His trust is easily gained but impossible to restore once broken." — page L23 and `sources/adventure-wdh.json:2113`.
- **Loyalty to Floon.** "the devoted friend of Floon Blagmaar" — page L25. "Renaer's own words: 'Renaer ... ' — `sources/Appendix_D_-_Running_the_Tavern.md:1379` (Floon's keys: "Talks about Renaer with the devotion of someone who knows they are in the orbit of a more significant person and has made peace with this.")
- **His estate.** "Renaer spends as little time there as possible, however, since it's constantly under surveillance by spies loyal to his father." — `sources/adventure-wdh.json:32547`.
- **Harpers and fights for the city.** "As a Harper, he spends a lot of time defending Waterdavians against those who, like his father, would deprive them of their coin and rights." — `sources/adventure-wdh.json:32547` (see D1).
- **Renaer's own favourite topics.** "He collected books and was very well read in history and local lore." — extract line 79.
- **The Vault and Floon.** "Becomes completely serious when either the Vault of Dragons or Floon Blagmaar is mentioned." — `sources/Appendix_D_-_Running_the_Tavern.md:1304`.
- **Fear of the Watch and the wrong crowd (Alexandrian Appendix D, GM keys).** "Introduces a friend — roll on Renaer's Friends table to determine who, and let their agenda drive the rest of the scene." — `sources/Appendix_D_-_Running_the_Tavern.md:1310` (a scene keys line; not a fact about Renaer).

---

## Not readable

- `Renaer Neverember Guide, his backstory and family secrets.docx` (listed in `sources/SOURCE_GUIDE.md:693` as "Renaer's history, his father's crimes, what he knows vs. what he suspects, roleplaying guidance"). It could not be opened. It is the most direct source for a Renaer Background. Extract it.
- `Meloon Wardragon NPC Guide.docx` (`sources/SOURCE_GUIDE.md:692`): Meloon's mind-control situation and "morale"; it may bear on Renaer's alarm. Extract it.
- `The Waterdavian's Guide to Waterdeep NPCs ... .docx` (`sources/SOURCE_GUIDE.md:695`): a broad NPC reference; it may name Renaer.
- The Patreon Renaer guide cited for the 1479 DR rescue (`docs/plans/setting-compendium-research-notes/pass1-era4-era6.md:22`; `campaign/setting/organizations/05-force-grey.md:150`) is one of these `.docx` files, by the look of the citation. Not confirmed.

## Cross-references (other `file:line` where Renaer appears, selected)

- `campaign/gazetteer/waterdeep/sea-ward.md:9`: "Renaer offers his Sea Ward townhouse in **The Neighbors**, the tavern's financing passes through the Cassalanter Counting House in **The Grand Opening**, and one procession in **The Twin Parades** comes from this ward."
- `campaign/gazetteer/waterdeep/sea-ward.md:86`: "- Hook: in **The Neighbors**, Renaer offers the party his Sea Ward townhouse as a workspace for anything sensitive, and means it."
- `campaign/gazetteer/waterdeep/sea-ward.md:125`: "- Hook: he appears as an ally in **Finding Floon** and **Trollskull Alley**, and the party can ask him about any faction in the city."
- `campaign/gazetteer/waterdeep/castle-ward.md:45`: "- Durnan owns it and charges standard prices. ..." — not Renaer. Skip.
- `campaign/gazetteer/waterdeep/dock-ward.md:45`: "- Hook: in **Finding Floon**, Volo says Floon was last seen here. A regular remembers Floon leaving with Renaer Neverember around midnight, with five men following them out."
- `campaign/gazetteer/waterdeep/dock-ward.md:86`: "- Hook: in **Finding Floon**, the party arrives to find twelve corpses, four kenku searching the wreckage and Renaer Neverember hidden in a back room."
- `campaign/setting/notable-figures/independents-adversaries/01-dagult-neverember.md:21` (named in the Gralhund notes; not read in full in this pass).
- `campaign/setting/notable-figures/harpers/01-mirt.md:40`: "- **Renaer Neverember:** A Harper-adjacent ally of Mirt and Remi." (D1)
- `campaign/setting/notable-figures/doom-raiders/01-davil-starsong.md` and `02-yagra-stonefist.md` name Renaer (not read in this pass).
- `campaign/guides/factions/03-lords-alliance.md:9` (Yalah as the route by which Laeral learns of the Stone; `docs/plans/...` ruling; not read in this pass).
- `campaign/guides/factions/13-house-gralhund.md:47` ("- The house has agents inside Renaer's household, and Orond's journal calls them Eagle and Catoblepas. When any party member tells Renaer where the Stone or an Eye is, or what the party plans to do with it, the house has the news within two days. A party that tells Renaer nothing closes this channel, and the house then knows only what Chirada sees.").

## Not found (search terms and files)

- "Black Tears": `sources/adventure-wdh.json` (no hit), `sources/research/**/wiki.txt` (no hit), `sources/*.md` (no hit). Campaign-only (A5).
- "Lurue" + Renaer: campaign only (`campaign/locations/zhentarim-warehouse/z05-offices.md:9`; `campaign/setting/deities/mielikki.md:68`); `sources/adventure-wdh.json` (no hit).
- "closest" + Renaer + Meloon: `sources/adventure-wdh.json` (no hit); quest files only.
- Renaer's age: `sources/adventure-wdh.json` ("Approaching middle age"), wiki (blank infobox).
- "in his debt" + Blackstaff: no published source (D8).
- Renaer + "more property than" or "most property": campaign only (D4).
- Renaer's teacher or Harper initiation: no source.
