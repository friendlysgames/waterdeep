# Pass 6 research notes: Variel Duskwhisper

Page: `campaign/setting/notable-figures/harpers/06-variel-duskwhisper.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Model: `docs/plans/setting-compendium-research-notes/pass6/bregan-daerthe/03-felrekt-lafeen.md`
Ruling used: Ches 1, 1492 DR. Variel is a Harper courier under touring-musician cover and a Trollskull house-bard candidate. The High Harper scene that features him is quest time and is routed to **High Harper** (`campaign/quests/faction-events/harpers/r50-high-harper/`). Cassalanter secrecy and the Lolth rule do not touch this page.
Organization page: `campaign/setting/organizations/01-harpers.md` (Key Members, `:103`).
Factions Guide: `campaign/guides/factions/02-harpers.md` (`:82`, a cross-reference line only; no Variel mission row).
Voice profile: `.claude/skills/character-voices/voices/harpers.md`, "### Variel Duskwhisper", lines 101-115.
Wiki: NOT FOUND. `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-harpers/06-variel-duskwhisper.txt` reads "NOT FOUND". No wiki infobox, no citation key, no edition. The pass5 Harpers bundle has no Variel line (see Not found). One general wiki line on Harper bards is quoted in A7.

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines (Grep `-n`, or Read offsets).
- Published adventure: `sources/adventure-wdh.json` has no match for Variel or Duskwhisper (count 0). `sources/adventure-wdmm.json` also count 0.
- Alexandrian: Variel appears in `sources/Appendix_D_-_Running_the_Tavern.md` (the candidate block at `:708`-`:723` and a patron line at `:1349`). He does not appear in `Appendix_B` or `Appendix_C`, or in `Act_III_Arc_D.md` / `Act_III_Arc_E.md` (Grep).
- Alexandrian PDFs: Grep cannot search PDFs. `sources/3. Player Character Factions.pdf` was read (3 pages, printed pp.23-25) and names no Variel. Other PDFs were not read (see Not readable).
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **The page's alignment and stat block are supported by the campaign, but the Alexandrian appendix disagrees on both.** The page says "*Wood elf bard (Harper courier), neutral good, he/him*. Stat block: **Performer**." (`06-variel-duskwhisper.md:5`). The Alexandrian candidate block says "*N male wood elf, Commoner. A Harper courier. The music is secondary.*" (`Appendix_D_-_Running_the_Tavern.md:709`). The staff table agrees with the page: "| 5 | **Variel Duskwhisper** | NG wood elf |" (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:88`). See D1 and E1.
2. **"Featured in: Background figure; no scripted appearance." is contradicted by the High Harper event.** `campaign/quests/faction-events/harpers/r50-high-harper/ev-01-high-harper.md:5` names him as "courier witness". The scene is quest time and is routed. See D3.
3. **"Eight years" is sourced only on this page.** Two lines (`:13`, `:21`) carry it. The Alexandrian appendix says he is "based in Waterdeep for the next two months while waiting for a contact to arrive from Baldur's Gate" (`Appendix_D_-_Running_the_Tavern.md:715`). No file places the eight years. See D5.
4. **His instrument conflicts.** The Alexandrian candidate block says "His lute is old" (`Appendix_D_-_Running_the_Tavern.md:712`). The campaign quest says "with a fiddle across his knee" (`r50-high-harper/ev-01-high-harper.md:40`). Campaign outranks Alexandrian. See D4.
5. **The Overview is 38 words** (brief limit 21). The Morale line's "Uncanny Dodge" appears in no other file. See C rows 7 and 9.

---

## A. Background facts by theme

### A1. Origin, birth, home, family

No source gives Variel's birth, home, family or origin. The only location facts are the touring circuit and the Waterdeep posting in the Alexandrian candidate block.

> "Variel is a Harper information courier — not a field agent, but a messenger who uses musician's travel as cover. He is based in Waterdeep for the next two months while waiting for a contact to arrive from Baldur's Gate. He wants the house bard position because it gives him a legitimate reason to be seen in the North Ward regularly. He will tell Mirt about the tavern; Mirt already knows, but will appreciate the confirmation."
> — `sources/Appendix_D_-_Running_the_Tavern.md:715` (Alexandrian; the campaign files do not repeat the Baldur's Gate contact)

> "| 5 | **Variel Duskwhisper** | NG wood elf | Quiet, long-limbed. Plays a brief audition piece — something modal and winding, composed for a specific forest that no longer exists. Stops. \"I'm good. Not extraordinary. I'll fill a room comfortably.\" Then, without being asked: \"I travel a great deal — perhaps six nights out of ten, but not which six in advance.\" DC 15 Insight detects his schedule is structured, not random — he is managing a courier route. | Harper courier using musician work as cover. In Waterdeep for two months, waiting on a Baldur's Gate contact. Mirt's network accounts for his placement. | 7 gp | No Revenue bonus. One piece of actionable Harper-network intelligence/tenday, passed to the party incidentally. |"
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:88` (the House Bard candidate table; the header "**House Bard Candidates (wages vary)**" is at `:80`)

### A2. How he presents and works (cover)

> "**Information Is the Currency:** The Harpers hoard information the way other organizations hoard gold, and they collect it from ordinary people in ordinary places. Variel Duskwhisper tells one story per set that doubles as an intelligence report, Mattrim Mereg plays a mediocre bard at the Yawning Portal, Corvin Vayle passes folded notes between orders and Maxeene the draft horse listens at the hitching posts. The wiki records the same habit of informants living under aliases as traveling performers (Forgotten Realms Wiki, *Harpers*, edition not stated). It also records a Harper maxim that knowledge gained is half the battle won against any foe, and says that a changed chord or a substituted phrase in a familiar folk song can carry a warning to allies (Forgotten Realms Wiki, *Harpers*, edition not stated)."
> — `campaign/setting/organizations/01-harpers.md:36`

> "**Fronts and covers:** Most Harper agents live a double life (Forgotten Realms Wiki, *Harpers*, edition not stated). Remi is the gracious lady of House Ulbrinter, Mirt is a moneylender, Mattrim Mereg is a middling bard at the Yawning Portal, Variel Duskwhisper is a touring musician, and Corvin and Nessa Vayle are servers who come as a pair. Maxeene is hired out by the day from a stand off Fillet Lane. The published adventure says the Harpers like to do business in busy inns such as the Yawning Portal, or in quiet places such as the City of the Dead."
> — `campaign/setting/organizations/01-harpers.md:62`

> "- **Gathering information:** Remi sends messages to her spies by a silver raven figurine, Variel's stories carry reports, Corvin passes folded notes, Maxeene listens at hitching posts and Mattrim watches the Zhentarim agents who drink at the Yawning Portal. The wiki says the Harpers keep drop boxes, hidden caches and safe houses, with at least thirty drop-offs in Waterdeep alone, and that they use a sign language, a system of marked runes and spoken code words (Forgotten Realms Wiki, *Harpers*, edition not stated)."
> — `campaign/setting/organizations/01-harpers.md:74`

### A3. The courier role and the one-per-tenday mechanic

> "- **Variel Duskwhisper** — Wood elf bard; Harper courier operating under touring musician cover; passes one piece of network intelligence per tenday. See the **Variel Duskwhisper** page in Notable Figures."
> — `campaign/setting/organizations/01-harpers.md:103` (Key Members)

> "**Faction Note:** Harper courier. Harper party members will find Mirt has already accounted for Variel in his calculations — the man's presence at the Trollskull is, from Mirt's perspective, an organizational convenience. Occasional courier packages arrive at the kitchen entrance for him. These are not the party's business. Mostly."
> — `sources/Appendix_D_-_Running_the_Tavern.md:719`

> "**Mechanical Effect:** Music quality provides no Revenue Roll bonus (he is honest about being merely competent). Once per tenday, Variel delivers one piece of actionable street intelligence from the Harper network as an incidental — a name, a meeting, a rumor that bears investigation."
> — `sources/Appendix_D_-_Running_the_Tavern.md:723`

> "> - **Routed facts:** The \"Mission delivery\" bullet was deleted from the Summary. Its paper-bird method is in `02-harpers.md:37` and `01-overview.md:21`. The \"offers a substantial favor in return\" line and Variel's \"one piece of network intelligence per tenday\" stay as lore, and the Factions Guide (`02-harpers.md:51`) and the Trollskull Manor guide (`03-staff-and-hiring.md:88`) carry the mechanics."
> — `campaign/setting/organizations/01-harpers.md:188` (the Draft Notes callout)

### A4. The Trollskull house-bard candidacy (tavern procedure)

> "| House Bard | +8 gp standard | +1 Fame (good) or −1 Fame (bad)/tenday | Must be auditioned; DC 13 Performance (GM reads it) |"
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:95` (the staff upgrade table; the candidate table is at `:80`-`:88`)

> "**Wage:** 7 gp/tenday. He asked for 6 gp; the characters should offer 7 gp. He is underbidding because he wants the position."
> — `sources/Appendix_D_-_Running_the_Tavern.md:721`

### A5. His audition and his manner (Alexandrian)

> "He is quiet and long-limbed, with the particular stillness that elves achieve when they are paying close attention. His lute is old and has been repaired in several places with visible care. He plays a brief audition piece when asked — something modal and winding, clearly composed for a specific forest that no longer exists — and stops. \"I'm good,\" he says. \"Not extraordinary. I'll fill a room comfortably. I travel a great deal, so my availability is irregular — I can commit to perhaps six nights out of every ten, but not which six in advance.\" He waits. \"That's a problem for most places. I'm aware.\""
> — `sources/Appendix_D_-_Running_the_Tavern.md:712` (the paragraph is inside an HTML `<div>` and `<p>`; the tags are omitted here)

> "**Hidden Quality:** He will tell the characters he is a Harper contact if they are already Harper-affiliated; otherwise, DC 15 Insight detects that his irregular schedule is structured rather than genuinely variable. He is more useful as an intelligence asset than as a bard — his network connections can provide the characters with advance notice of Harpers-adjacent events in the city."
> — `sources/Appendix_D_-_Running_the_Tavern.md:717`

### A6. The High Harper event (quest time; routed)

> "This Social Event occurs when an individual Harper member first reaches Renown 50, which usually happens during **Dungeon of the Mad Mage**. Mirt receives the member in his library at 20:00, with Variel Duskwhisper as courier witness and Remallia Haventree at the table if her Harper role is known. In this Event, the member can:"
> — `campaign/quests/faction-events/harpers/r50-high-harper/ev-01-high-harper.md:5`

> "> Variel Duskwhisper (Neutral Good, Wood Elf, he/him) :: a slow-talking wood elf bard who carries Harper papers across the city under the cover of a touring musician."
> — `campaign/quests/faction-events/harpers/r50-high-harper/ev-01-high-harper.md:80` (the heading is "The Courier Witness" at `:78`)

> "> Variel is Friendly and says as little as the evening allows. He sips his one drink between sentences and tunes the same string while he listens. He never names a person outside a song, and he never raises his voice."
> — `campaign/quests/faction-events/harpers/r50-high-harper/ev-01-high-harper.md:82`

> "- Variel Duskwhisper never repeats what he hears. He leaves the library before the reveal."
> — `campaign/quests/faction-events/harpers/r50-high-harper/ev-01-high-harper.md:30`

> "Mirt's library is a long room lined with maps, and a fire has been burning in the hearth since the afternoon. Variel Duskwhisper sits on a stool by the far window with a fiddle across his knee, tuning one string. Mirt pushes a chair out with his foot and refills the glass in front of it before you sit."
> — `campaign/quests/faction-events/harpers/r50-high-harper/ev-01-high-harper.md:40`

> "> Variel will not discuss what Mirt says in the library, or anyone's business but his own."
> — `campaign/quests/faction-events/harpers/r50-high-harper/ev-01-high-harper.md:89`

Further quest-time lines in the same event (routed; he delivers the copies and the receipt):
> "- **Delivery:** At 10:00 the next day, Variel brings the copies to Mirt's library. The member reads them there, and Variel takes them away again." — `r50-high-harper/ev-01-high-harper.md:112`
> "- **Receipt:** At 10:00 three days later, Variel brings a receipt from the office to Mirt's library. It lists the submitted claims, the facts that are corroborated and the gaps that remain." — `r50-high-harper/ev-01-high-harper.md:281`
> "> Variel sets a sealed receipt on the library table beside Mirt's copy of your dossier. He slides both toward you and goes back to tuning his string." — `r50-high-harper/ev-01-high-harper.md:288`

### A7. The Harper bard tradition (wiki and org page; general, not Variel)

> "True bards are another matter entirely. Part of a bard's training is memorizing the traditions and lore, which are passed down, precise and immutable, for generations. That's why so many Harpers are bards: to preserve a knowledge of our past."
> — `sources/research/pass5-bundles/harpers/wiki.txt:95` (a wiki quote attributed to Khelben Arunsun, citing *Elfsong* (1994) p.17, `ES-p17`; the wiki's ref tags are omitted; the wiki gives no edition on the line)

> "- **Keep the Record:** `[research]` The wiki says the Harpers hold that current events can be understood only through the history that came before them, which is why so many Harpers are bards. They share lore with ordinary people through music and stories, and they do not change a performance to please those in power (Forgotten Realms Wiki, *Harpers*, edition not stated). The campaign shows the habit in Variel's story-reports and in the Harpers' scholarly and artistic ties, and no campaign file states the belief."
> — `campaign/setting/organizations/01-harpers.md:42` (Beliefs; tagged `[research]` on the page)

Recruiting and the adventure's bard lines:
> "Any smart, non-evil character can join the Harpers of Waterdeep. Bards and wizards are especially welcome." — `sources/adventure-wdh.json:1361`
> "If the adventurers are accosted and overwhelmed, one or more Harpers come to their rescue. A Harper rescue team usually consists of a {@creature bard|vgm} (see {@adventure appendix B|WDH|12}) or a {@creature mage}, plus {@dice 1d4 + 3} {@creature spy||spies} or {@creature veteran||veterans}." — `sources/adventure-wdh.json:1371`
> "- **Recruiting:** The published adventure says any smart, non-evil character can join the Harpers of Waterdeep, and that bards and wizards are especially welcome (`sources/adventure-wdh.json`). The wiki says the group usually picks its own recruits, that a member in good standing must sponsor them and the High Harpers must approve, and that a senior member watches the recruit's first mission without being seen (Forgotten Realms Wiki, *Harpers*, edition not stated)." — `campaign/setting/organizations/01-harpers.md:72`

### A8. The Trollskull patron who holds his messages

> "- Asks if the party left a message at the shop for Variel Duskwhisper — he received two messages for that name and isn't sure which is which" — `campaign/guides/trollskull-manor/08-notable-patrons.md:126` (the patron is Rishaal the Page-Turner, header at `:122`). The Alexandrian version: "3. Asks if the characters have used his shop to leave a message for Variel Duskwhisper (Harper courier), and if so, which one — because he has received two messages for that name and is not sure which is which." — `sources/Appendix_D_-_Running_the_Tavern.md:1349`

### A9. The page's own life facts (sourced only as far as noted)

- "Deep down, he has been doing this for eight years and finds the work sufficient." — `campaign/setting/notable-figures/harpers/06-variel-duskwhisper.md:21`. No other file gives eight years (see D5).
- "the quiet satisfaction of work that has proven sufficient over eight years" — `06-variel-duskwhisper.md:13`.
- "a Trollskull Manor bard candidate whose audition is genuine" — `06-variel-duskwhisper.md:25`. "Genuine" is the page's word; see C row 8.

### A10. Relation to Mirt and to the Trollskull

- "Mirt's network accounts for his placement." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:88` (the table's last-but-one column).
- "Mirt already knows, but will appreciate the confirmation." — `sources/Appendix_D_-_Running_the_Tavern.md:715`.
- The campaign has no line that gives Variel and Mirt a relationship before the High Harper event (F8).

### A11. Faith

No Variel-specific faith line. `campaign/setting/deities/milil.md:116`: "> - **Bards checked:** No Notable Figures page for Mattrim \"Threestrings\" Mereg, Variel Duskwhisper, Davil Starsong, Margo Verida or Agorn Fuoco names Milil (Grep for \"Milil\" over `campaign/` returns only the staff table, the Deities pages and the research notes), so the page names no worshiper beyond Lysa's history."

`campaign/setting/deities/corellon-larethian.md:70`: "- The campaign's other elves are Davil Starsong (sun elf, Zhentarim, Doom Raiders), Remallia Haventree (sun elf, Harpers), Variel Duskwhisper (wood elf, Harpers) and Laeral Silverhand (moon elf, Open Lord). None of their pages names a god of the Seldarine."

---

## B. Alignment, species, pronouns, stat block

**Alignment**
> "- *Wood elf bard (Harper courier), neutral good, he/him*. Stat block: **Performer**." — `campaign/setting/notable-figures/harpers/06-variel-duskwhisper.md:5`
> "| 5 | **Variel Duskwhisper** | NG wood elf |" — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:88` (campaign; agrees with the page)
> "Variel Duskwhisper (Neutral Good, Wood Elf, he/him) :: a slow-talking wood elf bard who carries Harper papers across the city under the cover of a touring musician." — `campaign/quests/faction-events/harpers/r50-high-harper/ev-01-high-harper.md:80` (campaign; agrees)
> "*N male wood elf, Commoner. A Harper courier. The music is secondary.*" — `sources/Appendix_D_-_Running_the_Tavern.md:709` (Alexandrian; says N, not NG)
> "The staff table lists Variel as \"N wood elf\" (`03-staff-and-hiring.md:88`) while his page says neutral good (`campaign/setting/notable-figures/harpers/06-variel-duskwhisper.md:6`). I did not edit either." — `campaign/setting/deities/milil.md:117`. The staff table now reads "NG wood elf" (`03-staff-and-hiring.md:88`), so this milil note is out of date.

**Species**
- "Wood elf bard (Harper courier)" — `06-variel-duskwhisper.md:5`.
- "Wood Elf" — `ev-01-high-harper.md:80`.
- "NG wood elf" — `03-staff-and-hiring.md:88`.
- "*N male wood elf, Commoner. ...*" — `Appendix_D_-_Running_the_Tavern.md:709`.
- "Variel Duskwhisper (wood elf, Harpers)" — `campaign/setting/deities/corellon-larethian.md:70`.

**Pronouns**
- "he/him" — `06-variel-duskwhisper.md:5`; `ev-01-high-harper.md:80`.
- "male" — `Appendix_D_-_Running_the_Tavern.md:709`.

**Stat block**
- "Stat block: **Performer**." — `06-variel-duskwhisper.md:5`.
- "Commoner" — `Appendix_D_-_Running_the_Tavern.md:709` (Alexandrian stat label; conflicts; see D2).
- The planning doc's Bard row names Mattrim and Agorn, not Variel: "| Bard (Mattrim, Agorn) | **Performer** (CR 1/2) or **Performer Maestro** (CR 6) | 1/2 or 6 | XMM pp.236-237. Mattrim is not a combatant in the Harper pages. |" — `docs/plans/harpers-mechanics-reference.md:572` (planning, not campaign). No planning row for Variel.
- The Mattrim page uses the same label: "*Illuskan human bard (Harper spy), lawful good, he/him*. Stat block: **Performer**." — `campaign/setting/notable-figures/harpers/03-mattrim-mereg.md:5`.
- No file defines "Performer" or lists its numbers.

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/harpers/06-variel-duskwhisper.md`. Each row gives the status and where the fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L5 | "- *Wood elf bard (Harper courier), neutral good, he/him*. Stat block: **Performer**." | Day-one for species, pronouns, alignment and courier role (B). The stat label is a campaign choice; the Alexandrian says Commoner (D2). | B |
| 2 | L7 | "- **Featured in:** Background figure; no scripted appearance." | Contradicted by the High Harper event, a quest scene (D3). | `r50-high-harper/ev-01-high-harper.md:5`, `:78`-`:89` |
| 3 | L11 | "**Resonance.** Variel should inspire warmth with his unhurried folk musician manner; trust when his intelligence turns out to be precise; and pleasant surprise when a man who plays three-hour sets turns out to have been watching the entire time." | Day-one in content. "turns out" is reveal wording; restate as a trait, not a discovery. | `ev-01-high-harper.md:82` (manner); `Appendix_D_-_Running_the_Tavern.md:717` (structured schedule, DC 15 Insight) |
| 4 | L13 | "**Emotions.** Variel most often feels meditative patience, the quiet satisfaction of work that has proven sufficient over eight years, genuine pleasure in a good performance, mild boredom that reads as serenity, and professional satisfaction when the information moves correctly." | "eight years" is sourced only on this page (D5). Rest is the page's own. | none beyond the page |
| 5 | L15 | "**Motivations.** Variel wants to pass Harper-network intelligence without drawing attention, maintain the touring musician cover that lets him move freely, and play sets good enough that no one remembers them as anything else." | Day-one. Matches the courier role in `01-harpers.md:62` and `:74`. | `01-harpers.md:62`; `01-harpers.md:74` |
| 6 | L21 | "**Persona.** To the world, Variel Duskwhisper is a wandering elf bard who plays folk ballads at the same establishments on a slow circuit and drinks his one drink slowly. To those who know where to listen, he tells one story per set that is also an intelligence report, delivered in the structure of the tale and audible only to someone who knows what they are hearing. Deep down, he has been doing this for eight years and finds the work sufficient." | Day-one in content. "eight years" is unsourced beyond this page (D5). "one story per set" matches `01-harpers.md:36`. | `01-harpers.md:36`; voice `harpers.md:108` |
| 7 | L23 | "**Morale.** In a fight, Variel relies on Uncanny Dodge to protect himself and exits. He does not put the courier network at risk for a fight." | Encounter behaviour. "Uncanny Dodge" appears in no other file (Not found). | none |
| 8 | L25 | "**Relationships.** Variel is a Harper courier operating under touring musician cover, a Trollskull Manor bard candidate whose audition is genuine, a member of the Harper intelligence relay who passes one piece of network intelligence per tenday, and a man who has watched the same taverns long enough to notice when something changes." | "a Trollskull Manor bard candidate" is a tavern-hire state; no file dates it (F1). "whose audition is genuine" has no source; the Alexandrian says "I'm good. Not extraordinary." and "he is honest about being merely competent" (`Appendix_D_-_Running_the_Tavern.md:712`, `:723`). "passes one piece of network intelligence per tenday" is a mechanic (A3). | `Appendix_D:715`, `:723`; `03-staff-and-hiring.md:88`; `01-harpers.md:103` |
| 9 | L27-29 | "## Overview" / "A wood elf bard on a slow touring circuit who plays folk ballads at the same establishments and nurses a single drink over the course of an evening, watching the room more carefully than the unhurried manner suggests." | Day-one in content. **38 words** by whitespace count (brief limit 21). Draft a shorter Overview. | `ev-01-high-harper.md:82`; `harpers.md:101`-`:111` |

Voice profile lines (`.claude/skills/character-voices/voices/harpers.md`, "### Variel Duskwhisper", lines 101-115):
- Line 108: "- **Personality in speech:** Patience is his whole manner. He answers in his own time, and nothing hurries him. His professionalism shows in what he leaves out. When information needs passing, it arrives inside a tale (\"There's a song they sing in Rassalantar about a miller who…\"), and he never says it plainly." The Rassalantar name is a place with no page: "**Names with no page:** Ahghairon, Raurlor, Zundbridge, Rassalantar, the Cynosure, Amendsfarm and Peaktop Aerie are plain text." (`campaign/setting/geography/waterdeep.md:161`). This is a voice line, not a quest event.
- Line 114: "  - *Business:* \"Listen to the third song tonight. The one about the ferryman. Listen to what he carries.\"" The delivery manner is a standing practice. "ferryman" appears in no campaign file linked to Variel (Grep finds only `campaign/quests/faction-events/bregan-daerthe/m06-the-dive/ev-01-the-dive.md:29`, a paid ferryman in a Bregan D'aerthe event). Flag as unsourced phrase.
- Lines 113 and 115: no quest-time clause.

Quest-time facts on the page (routed to **High Harper**, `campaign/quests/faction-events/harpers/r50-high-harper/`):
- `ev-01-high-harper.md:5` (courier witness), `:30` (never repeats), `:40` (library scene), `:80` (tag), `:82` (manner), `:89` (will not discuss), `:112` (copies), `:281` (receipt), `:288` (sealed receipt), `:253` (the Laeral dossier, quoted below), `:331` (he leaves), `:438` (the player-facing account).
- "> > \"If you want a faction exposed, bring me its name and the evidence you really have. I'll send it to Laeral's office tonight. Variel will bring the answer back.\"" — `r50-high-harper/ev-01-high-harper.md:253`.
- "We became High Harpers at Mirt's table, with Variel playing in the corner." — `r50-high-harper/ev-01-high-harper.md:438`.

---

## D. Conflicts

**D1. Alignment (campaign against Alexandrian).**
- Page: "*Wood elf bard (Harper courier), neutral good, he/him*." (`06-variel-duskwhisper.md:5`)
- Staff table: "| 5 | **Variel Duskwhisper** | NG wood elf |" (`03-staff-and-hiring.md:88`)
- Quest tag: "Variel Duskwhisper (Neutral Good, Wood Elf, he/him)" (`ev-01-high-harper.md:80`)
- Alexandrian candidate block: "*N male wood elf, Commoner. A Harper courier. The music is secondary.*" (`Appendix_D_-_Running_the_Tavern.md:709`)
Higher rank: campaign. The Alexandrian line says N and Commoner.

**D2. Stat block.** Page: "Stat block: **Performer**." (`06-variel-duskwhisper.md:5`). Alexandrian: "Commoner" (`Appendix_D_-_Running_the_Tavern.md:709`). Campaign outranks Alexandrian. The Mattrim page also uses Performer (`03-mattrim-mereg.md:5`).

**D3. "Featured in".**
> "- **Featured in:** Background figure; no scripted appearance." — `campaign/setting/notable-figures/harpers/06-variel-duskwhisper.md:7`
> "Mirt receives the member in his library at 20:00, with Variel Duskwhisper as courier witness and Remallia Haventree at the table if her Harper role is known." — `campaign/quests/faction-events/harpers/r50-high-harper/ev-01-high-harper.md:5`
The page says "no scripted appearance"; the High Harper event scripts him in a scene (`:78`-`:89`) and in the copies and receipt deliveries (`:112`, `:281`, `:288`).

**D4. Instrument.**
> "His lute is old and has been repaired in several places with visible care." — `sources/Appendix_D_-_Running_the_Tavern.md:712` (Alexandrian)
> "Variel Duskwhisper sits on a stool by the far window with a fiddle across his knee, tuning one string." — `campaign/quests/faction-events/harpers/r50-high-harper/ev-01-high-harper.md:40` (campaign)
Campaign outranks Alexandrian. The page does not name an instrument.

**D5. Time in the post.**
> "Deep down, he has been doing this for eight years and finds the work sufficient." — `campaign/setting/notable-figures/harpers/06-variel-duskwhisper.md:21`
> "He is based in Waterdeep for the next two months while waiting for a contact to arrive from Baldur's Gate." — `sources/Appendix_D_-_Running_the_Tavern.md:715`
These do not contradict in terms (the eight years could be elsewhere), but no file says where the eight years were spent. The Alexandrian gives a Waterdeep posting of two months.

**D6. "Audition is genuine".** The page says "a Trollskull Manor bard candidate whose audition is genuine" (`:25`). The Alexandrian says "*I'm good. Not extraordinary.*" and "he is honest about being merely competent" (`Appendix_D_-_Running_the_Tavern.md:712`, `:723`). The Alexandrian's hidden quality is that "his irregular schedule is structured rather than genuinely variable" (`:717`). The word "genuine" on the page is not in any source.

**D7. The intelligence rule.** "passes one piece of network intelligence per tenday" (`:25`) and the mechanic at `Appendix_D:723` agree. No conflict.

---

## E. Stale lines in other files (not to be edited) and routed quest references

**E1. Stale lines**
- `campaign/setting/deities/milil.md:117` (quoted in B): the staff table now reads "NG wood elf" (`03-staff-and-hiring.md:88`), so the milil note is stale.
- `campaign/setting/organizations/01-harpers.md:188` (quoted in A3) routes the mechanic to the Factions Guide at `02-harpers.md:51`. Grep finds no Variel at `02-harpers.md:51`; the Factions Guide mentions Variel only at `:82`. The mechanic's campaign source is `03-staff-and-hiring.md:88`.
- `sources/Appendix_D_-_Running_the_Tavern.md:709` (N, Commoner) conflicts with the campaign (D1, D2).

**E2. Routed quest references (the High Harper event; quest time)**
- `campaign/quests/faction-events/harpers/r50-high-harper/ev-01-high-harper.md:5`, `:30`, `:40`, `:78`-`:89`, `:112`, `:253`, `:281`, `:288`, `:327`, `:331`, `:438`.
- `campaign/quests/faction-events/harpers/r50-high-harper/design-notes.md:9` (Grep returned this line with Variel's name; the line was omitted from the Grep display, so its text is unread).

**E3. Cross-references (not Variel-specific claims)**
- `campaign/guides/factions/02-harpers.md:82`: "- Notable Figures: **Mirt**, **Remallia \"Remi\" Haventree**, **Mattrim \"Threestrings\" Mereg**, **Bonnie**, **Corene Wyldath**, **Variel Duskwhisper**, **Corvin Vayle**, **Nessa Vayle**, **Maxeene**"
- `campaign/setting/organizations/01-harpers.md:161`: "- **Mirt**, **Remallia \"Remi\" Haventree**, **Mattrim \"Threestrings\" Mereg**, **Corene Wyldath**, **Variel Duskwhisper**, **Maxeene** (Notable Figures): the principal Harpers"
- `campaign/guides/trollskull-manor/08-notable-patrons.md:126` (A8).
- `campaign/setting/organizations/01-harpers.md:36`, `:62`, `:74` (A2).

---

## F. Gaps a Background needs that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]`.

**F1. Origin, birth, home, family, age.** No source gives any of these. The Alexandrian gives a two-month Waterdeep posting and a Baldur's Gate contact (`Appendix_D:715`). The page gives "eight years" (`:13`, `:21`). Do not name a new Notable Figure (brief ruling 17). The Baldur's Gate contact is unnamed in every file; a nameless contact is allowed.

**F2. How and when he became a Harper courier.** None in any source. The Harper recruitment rule is the group's (A7). Mirt's network "accounts for his placement" (`03-staff-and-hiring.md:88`); no line says who recruited him.

**F3. Musical training and instrument.** None. The campaign's instrument is a fiddle (`ev-01-high-harper.md:40`); the Alexandrian's is a lute (`Appendix_D:712`). Campaign ranks higher (D4).

**F4. Where the eight years were spent.** None (D5).

**F5. Personal goals beyond the post.** None in any source. The page's Motivations give the courier and performance wants (`:15`). Any `[design]` goal must not reveal the network's structure, an Event Outcome or the Grand Game balance (brief ruling 17), and must sit with his manner: "He never rushes" (`harpers.md:111`).

**F6. Losses, grudges, fears, loves.** None in any source. The only sourced inner habit is the voice's "He never rushes, never gossips about named people outside a story, and never raises his voice." (`harpers.md:111`).

**F7. Physical appearance.** Only the Alexandrian gives one: "He is quiet and long-limbed, with the particular stillness that elves achieve when they are paying close attention." (`Appendix_D:712`). The voice gives "A soft, unhurried wood-elf voice, warm and slightly husky." (`harpers.md:104`). No fixed description of his look is in the campaign.

**F8. His relation to Mirt before the High Harper event.** None. The sources say Mirt "already knows" about the tavern (`Appendix_D:715`) and that he "will tell Mirt" (same line). The quest puts him in Mirt's library (`ev-01-high-harper.md:40`). The campaign gives nothing earlier.

**F9. Faith.** None. The Milil and Corellon notes name no worship (A11).

---

## G. Source facts that hint at the figure's inner life (for the backstory; do not contradict)

- "Deep down, he has been doing this for eight years and finds the work sufficient." — `campaign/setting/notable-figures/harpers/06-variel-duskwhisper.md:21`
- "the quiet satisfaction of work that has proven sufficient over eight years, genuine pleasure in a good performance, mild boredom that reads as serenity, and professional satisfaction when the information moves correctly." — `06-variel-duskwhisper.md:13`
- "Variel wants to pass Harper-network intelligence without drawing attention, maintain the touring musician cover that lets him move freely, and play sets good enough that no one remembers them as anything else." — `06-variel-duskwhisper.md:15`
- "He does not put the courier network at risk for a fight." — `06-variel-duskwhisper.md:23`
- "Patience is his whole manner. He answers in his own time, and nothing hurries him. His professionalism shows in what he leaves out." — `.claude/skills/character-voices/voices/harpers.md:108`
- "He sings far more than he speaks." — `harpers.md:104`
- "He names songs and places, never people." — `harpers.md:106`
- "He sips his one drink between sentences. He tunes the same string while he thinks. He ends conversations by starting to play." — `harpers.md:109`
- "He never rushes, never gossips about named people outside a story, and never raises his voice." — `harpers.md:111`
- "\"I'm good,\" he says. \"Not extraordinary. I'll fill a room comfortably.\"" — `Appendix_D_-_Running_the_Tavern.md:712` (the same paragraph ends: "\"That's a problem for most places. I'm aware.\"")
- "He is underbidding because he wants the position." — `Appendix_D_-_Running_the_Tavern.md:721`
- "He wants the house bard position because it gives him a legitimate reason to be seen in the North Ward regularly." — `Appendix_D_-_Running_the_Tavern.md:715`
- "Occasional courier packages arrive at the kitchen entrance for him. These are not the party's business. Mostly." — `Appendix_D_-_Running_the_Tavern.md:719`
- "Variel Duskwhisper never repeats what he hears. He leaves the library before the reveal." — `campaign/quests/faction-events/harpers/r50-high-harper/ev-01-high-harper.md:30` (quest-time; a trait)
- "Variel is Friendly and says as little as the evening allows." — `r50-high-harper/ev-01-high-harper.md:82` (quest-time)

---

## Not found

- Origin, birth, home, family, age, training, instrument (beyond D4), recruitment, sponsor, handler, personal goals, losses, faith and appearance (beyond the Alexandrian paragraph). Searched: `campaign/` (Grep for "Variel|Duskwhisper"), `sources/*.md` (Grep), `sources/adventure-wdh.json` (count 0), `sources/adventure-wdmm.json` (count 0), `sources/research/` (Grep).
- "eight years" in any file other than the Variel page: Grep over `campaign/` returns this page's two lines only as they concern Variel. Other "eight years" hits concern other figures.
- "Uncanny Dodge" in any file other than this page: Grep over the repository returns only `06-variel-duskwhisper.md:23`.
- Numbers for the "Performer" stat block: no file defines the block, and the planning Bard row (`docs/plans/harpers-mechanics-reference.md:572`) does not name Variel.
- The name of the Baldur's Gate contact (`Appendix_D:715`). No file names the contact.
- A wiki page for Variel (scratchpad extract is NOT FOUND). `sources/research/pass5-bundles/harpers/wiki.txt`: Grep for Variel and Duskwhisper returns nothing. The pass3 and pass4 bundles hold campaign-hits only.
- Variel in `Appendix_B_-_Player_Factions.md` and `Appendix_C_-_Player_Faction_Missions.md`: none (Grep).
- Variel in `Act_III_Arc_D.md` and `Act_III_Arc_E.md`: none (Grep).
- Variel in `sources/SOURCE_GUIDE.md`: none. The `.docx` list (`SOURCE_GUIDE.md:683`-`:698`) has no Harper NPC guide.
- Variel in the Dock Ward, Trades Ward and Field Ward gazetteers: none (Grep).

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. `SOURCE_GUIDE.md:683`-`:698` lists NPC guides for Cassalanters, Davil, Gale, Jarlaxle, Lif, Meloon, Renaer, the urchins, Vajra, Xoblob and Zardoz. None covers Variel.
- Alexandrian PDFs not read: `sources/11. Lair – Xanathar's Lair.pdf`, `sources/1. The Villains.pdf` and the others. Grep cannot search PDFs. No PDF other than `3. Player Character Factions.pdf` was checked for Variel's name.
- `sources/3. Player Character Factions.pdf` was read in full (pp.1-3). It names neither Variel nor Corene. Transcription from images; check with `pdftotext -layout` before quoting.
