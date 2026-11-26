# Pass 6 research notes: Laeral Silverhand

Page: `campaign/setting/notable-figures/city-officials/01-laeral-silverhand.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Laeral is a major NPC (brief ruling 2): full Personality and Connections apply.
Organization page: `campaign/setting/organizations/11-open-lords-watch.md`. Laeral is not a Watch member; the page lists her as the Open Lord to whom the Commander reports (line 78).
Institution entry: `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md` (the Open Lord's office; her Key Members entry is line 38).
Factions Guide: `campaign/guides/factions/12-open-lords-watch.md` (the Watch's rules). Laeral's Grand Game stance is in `campaign/guides/factions/03-lords-alliance.md:7-9`.
Voice profile: `.claude/skills/character-voices/voices/city-officials.md`, "### Laeral Silverhand", lines 7-21.
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`.
Wiki extract: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-city-officials/01-laeral-silverhand.txt` (199 lines; quoted as "wiki line N"). The wiki's infobox fields carry edition tags where it gives them; most body sentences print no edition.

## Method and caveats

- Campaign files: Read and Grep. Every quote is copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes are shown as plain quotes. `{@creature ...}` tags are left as written. Where Grep showed "[Omitted long matching line]", the line was re-read with Read before quoting.
- Alexandrian PDF: `sources/2. Other Factions.pdf` was read as rendered page images (PDF p.2, printed p.21). The quote is a transcription from the image and is flagged for a `pdftotext -layout` check before any quote reaches prose.
- No shell was available. `voicecheck.py` was not run. No file was edited except this notes file.
- The "not fully, but yes" wording is the user's Sundering ruling. It is quoted from the standing rule in CLAUDE.md ("Sundering canon and 5e source precedence") and from `docs/plans/setting-compendium-research-notes/sundering-resolutions.md:997`.
- The Alexandrian Arc D, Appendix B, C and D markdown files were searched for Laeral (see Not found).

## Findings that change how the page is written

1. **The voice profile contradicts the day-one rule that she does not know the Stone has resurfaced.** The Greeting opens "You're the ones who found the Stone." (`.claude/skills/character-voices/voices/city-officials.md:19`). Every day-one source says she does not know (`campaign/setting/history/07-a-city-watching-itself.md:24`, `campaign/guides/factions/12-open-lords-watch.md:26`, `campaign/guides/factions/03-lords-alliance.md:9`). The drafter must restate or remove that Greeting (brief ruling 3, and the profile change under ruling 16). See D3.
2. **Species is contested, and one campaign file misstates the adventure.** The page and the Open Lord entry say moon elf (`01-laeral-silverhand.md:5`; `open-lord-and-masked-lords.md:38`). `campaign/setting/history/07-a-city-watching-itself.md:35` reads: "The campaign makes Laeral a moon elf. The published adventure and the wiki both call her human, and the wiki's alignment, chaotic good, matches the campaign's, so only the species differs (Forgotten Realms Wiki, Laeral Silverhand, infobox race and 5e alignment)." The adventure's Laeral entry (lines 32187 to 32206) contains no species word. The wiki's race field says Human (wiki line 18). See B2 and D1.
3. **The stat block line has no CR on the page, and the sources give two different CRs.** The Summary says "Stat block: **Archmage**." The wiki's 5e infobox gives challenge 17 (wiki line 62). The Lords' Alliance mechanics reference gives CR 12 and marks it unverified (`docs/plans/lords-alliance-mechanics-reference.md:304`). The adventure gives no stat block. See B4 and D4.
4. **Marriage to Khelben is contested.** The adventure says "She met and married Khelben Arunsun" (`sources/adventure-wdh.json:32202`). The wiki says "though they were never married" (wiki line 133). The campaign calls her Khelben's widow (`01-laeral-silverhand.md:25`). See D2.
5. **Several setting pages narrate quest events, against the campaign-start rule.** Lines 23, 46, 52 and 62 of `history/07-a-city-watching-itself.md`, and lines 62 and 68 of `open-lord-and-masked-lords.md`, name **Lioncrown**, **Fentree's Ledger** and **An Audience with the Open Lord** as events. They are listed under E2 and not edited.

---

## A. Background facts by theme

### A1. Origin, family, early life

**Adventure, Laeral entry (page 207)**
> "Anamanué {@creature Laeral Silverhand|wdh} was born in the Year of the Cowl (765 DR), the fifth of seven daughters of the goddess Mystra. Each of the Seven Sisters is a powerful and ageless beauty with a penchant for arcane magic."
> — `sources/adventure-wdh.json:32201` (entry "Laeral Silverhand", page 207)

**Campaign, history 07 (Laeral Takes the Seat)**
> "- Laeral Silverhand is the fifth of the goddess Mystra's seven daughters, born in 765 DR. She was once the Witch-Queen of the North and led the adventuring company called the Nine."
> — `campaign/setting/history/07-a-city-watching-itself.md:30`

**Campaign, open-lord page (Key Members)**
> "**Laeral Silverhand** (Chaotic Good, Moon Elf, she/her) is the Open Lord. She is the fifth of the Seven Sisters, the daughters of Mystra, and was born in 765 DR. She uses her magic sparingly, relies on trusted advisors and deputies, and likes to leave the Palace in disguise to visit old friends and check on enemies. The published adventure gives her no species, and the moon elf reading is the campaign's own (campaign-only)."
> — `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:38`

**Wiki, parents (edition not printed; cites *The Seven Sisters* pp. 6-8)**
> "Laeral was one of seven female spellcasters born to the [[ranger]] [[Dornal Silverhand]] and his wife [[Elué]] (with the exception of [[Qilué Veladorn]] who, due to divine intervention, was [[drow]]). Collectively, they were known as the [[Seven Sisters]]."
> — wiki line 106 (ref `SS-p6-8`). Wiki-only as to the parents' names.

**Wiki, childhood (cites *The Seven Sisters* p. 8)**
> "After their mother died, Laeral, [[Dove Falconhand|Dove]], and [[Storm Silverhand|Storm]] were placed into the care of [[Elminster]] until they came of age. When her sisters left the Old Sage, Laeral elected to stay with him as his apprentice. When she had finished her studies, she left to join the [[Harpers]]."
> — wiki line 119. Wiki-only. The campaign and the adventure say nothing of her childhood or training.

### A2. Former life: Witch-Queen, Stornanter and the Nine

**Adventure, Laeral entry (page 207)**
> "Long ago, Laeral ruled a kingdom called Stornanter and held the title of Witch-Queen of the North. After that, she led a band of adventurers called the Nine. She met and married Khelben Arunsun, who would later become the Blackstaff, the Lord Mage of Waterdeep. After Khelben died, Laeral retired from public life. She resurfaced after the Spellplague and the Sundering, weakened by Mystra's death, rebirth, and withdrawal from the world."
> — `sources/adventure-wdh.json:32202` (see D2 for the wiki's "never married")

**Adventure, a Bregan D'aerthe letter prop (a title; the letter is quest-time)**
> "To Her Ageless Majesty, {@creature Laeral Silverhand|WDH}, the Witch-Queen of Stornanter, Lady of the North, She of the Seven Sisters, Chosen of Mystra, and Open Lord of Waterdeep:"
> — `sources/adventure-wdh.json:26646`

**Wiki, Stornanter (cites *The Grand History of the Realms* p. 103)**
> "Laeral left the Harpers early and, in the {{YearlinkName|806}}, at age 41, she was a self-styled queen, ruling the realm of [[Stornanter]] from [[Port Llast]]."
> — wiki line 121 (ref `GHotR-103`). The dates are wiki-only; the realm and the title are in the adventure (`:32202`).

**Wiki, Malek and Khelben (cites *Blackstaff/MMP*; wiki-only)**
> "Barely ten years into her reign, Laeral's court mage, [[Khelben Arunsun|Malek Aldhanek]], with whom she had worked very closely, was apparently assassinated in a plot involving other nobles. Realizing too late that she was in love with Malek, Laeral quit her court and spent twenty five years wandering Stornanter. In truth, Malek was not dead—he'd never even existed—and was actually Khelben Arunsun in disguise."
> — wiki line 123 (ref `BS-?`). Wiki-only. Do not use without a `[research]` tag. The campaign has no Malek.

**Wiki, the Crown of Horns (cites *Champions of Ruin* p. 126)**
> "In the {{YearlinkName|1337}}, Laeral and the Nine discovered the ancient [[Netherese]] [[artifact]] known as the ''[[Crown of Horns]]'' in [[Yûlash]]. The ''Crown'' was actually planted for her to find by the Netherese [[lich]] [[Aumvor The Undying]], who wished to use the ''Crown'' to influence her to marry him. The plot failed when Laeral donned the headpiece and the ''Crown's'' powers conflicted with Laeral's [[spellfire]] and drove her into madness."
> — wiki line 131 (ref `CoR-p126`). Wiki-only. The campaign's Myrkul page says the Crown "held what was left of his mind for a decade, then reformed and passed from host to host across Faerûn" only in part: its exact wording is "It held what was left of his mind for a decade, then reformed and passed from host to host across Faerûn" (`campaign/setting/deities/myrkul.md:54`), and it says the Khelben's-tower vault for the Crown "appear[s] only in the wiki" (`campaign/setting/deities/myrkul.md:114`).

**Wiki, Khelben frees her (edition not printed)**
> "Twenty years later, in the {{YearlinkName|1357}}, Khelben Arunsun traveled to the [[Stronghold of the Nine]] in the [[High Forest]], freed Laerel Silverhand from the ''Crown of Horns'', the malign intelligence contained within' and her madness. Laeral returned with him to Waterdeep for more healing, and after that, they were inseparable. She was referred to as Lady Arunsun,<ref>{{Cite book/City of Splendors: Waterdeep|24}}</ref> though they were never married."
> — wiki line 133. The last clause conflicts with the adventure (D2).

**Wiki, Khelben's death (ref `WDH5e-p207`)**
> "When Khelben died in the {{YearlinkName|1374}}, Laeral returned from life in the public eye for some time.<ref name="WDH5e-p207" />"
> — wiki line 146. No campaign file gives a date for his death (F3).

**Wiki, Moonstars (edition not printed; cites *The Forgotten Realms Campaign Setting* 3e p. 280)**
> "Together with her partner [[Khelben \"Blackstaff\" Arunsun]], they led the [[Moonstars]], a dissident faction of the [[Harpers]], which sought to guide the cities and countries of the [[North]] toward a shared destiny."
> — wiki line 66 (ref `FRCS3e-280`). The campaign has no Moonstars page (D10).

### A3. The Spellplague, the Sundering and her magic

**Adventure, Laeral entry (page 207)**
> "Laeral's magic isn't as great as it once was, though she does her utmost to hide this fact. Only Elminster, her trusted friend and advisor, knows the extent of her decline. Despite her diminished abilities, Laeral remains a formidable, clear-headed wizard with plenty of magic at her disposal."
> — `sources/adventure-wdh.json:32203`

**Campaign, history 07 (Lore Summary)**
> "- She governs with deputies and uses her own magic sparingly, because it waned with Mystra's death and the Spellplague. It has come back since the Weave returned in 1487, though not fully. Only Elminster knows how far, and she admits it to one Lioncrown of the Lords' Alliance."
> — `campaign/setting/history/07-a-city-watching-itself.md:23`. The last clause names a quest event (C2).

**Campaign, history 07 (Laeral Takes the Seat)**
> "- She came back after the Spellplague and the Sundering, weakened by Mystra's death and rebirth."
> — `campaign/setting/history/07-a-city-watching-itself.md:33`

**The user ruling behind the magic line**
> "- **Laeral:** her magic waned with the Spellplague and has recovered since the Weave returned in 1487, "not fully, but yes"."
> — `docs/plans/setting-compendium-research-notes/sundering-resolutions.md:997`
> Same ruling in CLAUDE.md, section "Sundering canon and 5e source precedence": "Two campaign rulings follow from it: Laeral's magic waned with the Spellplague and has recovered since the Weave returned in 1487, "not fully, but yes"; ..."

**Wiki, powers and the Second Sundering (cites *Death Masks*, a novel per the wiki's own Appearances list at line 162)**
> "As a centuries-old wizard, Laeral was one of the most accomplished spellcasters in [[Faerûn]], though her powers steadily declined as she had to increasingly devote her energies to maintaining her aging body.<ref name="DM" /> Like all Chosen, Laeral's divine blessings were much reduced in the wake of the [[Second Sundering]], as all gods took a more distant approach to interfering in mortal affairs.<ref name="DM" />"
> — wiki line 80 (ref `DM`)

**Wiki, 1487 DR (cites *The Herald*)**
> "In the {{YearlinkName|1487}}, [[Larloch]] foiled Laeral and Alustriel's plans and absorbed the wards of Candlekeep.<ref name="TH-p-238">{{Cite book/The Herald/Hardcover|238|13}}</ref> Shortly thereafter, Laeral, Alustriel, Elminster, and the [[Srinshee]] prevented Larloch's ascension to godhood.<ref name="TH-p-348-350">{{Cite book/The Herald/Hardcover|348-350|19}}</ref> Laeral remained a Chosen of the restored Mystra.<ref name="DM-p?1">{{Cite book/Death Masks|?}}</ref>"
> — wiki line 149 (wiki-only detail)

### A4. Khelben, the Blackstaff and Vajra

**Adventure, Laeral entry (page 207)**
> "Laeral's relationship with {@creature Vajra Safahr|WDH}, the current Blackstaff, has its challenges. For one thing, Laeral is much older, much wiser, and much more powerful than Vajra, whom she views as an insecure child. In addition, Vajra wields the Blackstaff, which has Khelben Arunsun's soul and the souls of all the other Blackstaffs bound inside it. Laeral covets the staff, because it contains all that's left of her husband. Not surprisingly, the two mages avoid each other as much as possible."
> — `sources/adventure-wdh.json:32205`

**Campaign, history 07 (How Laeral Governs)**
> "- Laeral explains her inaction as a test of Vajra's competence. She also covets the Blackstaff, which holds Khelben's soul, and she thinks of Vajra as an insecure child. The two avoid each other."
> — `campaign/setting/history/07-a-city-watching-itself.md:45`

**Campaign, Vajra's Notable Figures page**
> "- **Khelben Arunsun:** The original Blackstaff and Laeral's late husband, who handpicked Vajra. His spirit is in the staff, and Vajra will not discuss what is in it."
> — `campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md:39`

**Wiki, Blackstaff Tower (cites `CoS:W-p24`)**
> "Laerel soon came to be the caretaker of Blackstaff Tower and Blackstaff Academy, which was founded as apprentices flocked to the Tower to learn from Khelben and herself."
> — wiki line 135. Wiki-only. The spelling "Laerel" is the wiki's.

### A5. Return to public life and the Open Lord's office

**Adventure, Laeral entry (page 207)**
> "A few years ago, Dagult Neverember was ousted as Open Lord of Waterdeep. Laeral reluctantly stepped into the vacancy at the request of the Masked Lords, and has served as Waterdeep's Open Lord ever since. Initially overwhelmed by the demands of the nobles and guildmasters, she has settled nicely into her new role. She uses her magic sparingly and relies on trusted advisors and deputies. As time allows, she likes to venture outside the Palace of Waterdeep in disguise, just to clear her head or check up on old friends (and enemies)."
> — `sources/adventure-wdh.json:32204`

**Campaign, history 07 (Laeral Takes the Seat)**
> "- The Masked Lords voted Dagult Neverember out while he was rebuilding Neverwinter. They asked Laeral to fill the vacancy, and she took it reluctantly."
> — `campaign/setting/history/07-a-city-watching-itself.md:32`

**Campaign, history 07 (Overview)**
> "Laeral Silverhand is the Open Lord of Waterdeep, and she has held the office since about 1489 DR. In that year the Masked Lords voted Dagult Neverember out and asked her to take his place. She is the fifth of the goddess Mystra's seven daughters, an archmage of great age and renown who was once the Witch-Queen of the North and the wife of the wizard Khelben Arunsun. She governs from the Palace with the help of trusted deputies and advisors, among them Mirt, and the city has been quiet under her."
> — `campaign/setting/history/07-a-city-watching-itself.md:76`

**Campaign, open-lord page (the office)**
> "The Open Lord and the Masked Lords are the ruling council of Waterdeep, made up of one lord who sits in public and a body of other lords whose names are kept secret. Ahghairon founded the arrangement in 1032 DR, after he turned the warlord Raurlor's own sword into a serpent that killed him. Ahghairon then seated himself on the warlord's throne in the audience chamber, in front of the leaders of the city's armies and powerful families. From that seat he decreed that he would sit openly as lord while a council of other lords of nearly equal power ruled with him. The Open Lord still sits on that throne. Laeral Silverhand has held the office since the other Lords voted Dagult Neverember out a few years ago."
> — `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:16`

**Campaign, open-lord page (Operations)**
> "- **How the office changes hands:** The only recorded removal is Dagult Neverember, whom the other Lords voted out while he was in Neverwinter. Laeral stepped into the vacancy reluctantly, at the request of the Masked Lords. The published adventure gives no procedure for choosing or removing a Lord."
> — `open-lord-and-masked-lords.md:31`

**Wiki, Mystra's request (cites *Death Masks*, a novel, and *Sword Coast Adventurer's Guide*)**
> "After the fall of [[Myth Drannor]], Mystra herself appeared to Laeral. With the end of [[Luruar]], stability was once again needed in the [[Sword Coast North|northern Sword Coast]], and Mystra tasked Laeral with maintaining it by becoming Open Lord of Waterdeep. ... Following Mystra's request, Laeral returned to Waterdeep, and swiftly managed to gain the support of the Masked Lords of the city, supplanting [[Dagult Neverember]] as Open Lord<ref name="DM-p?2">..."
> — wiki line 151. (The ellipsis skips the wiki's account of why Mystra wanted her there. Rest of the passage covers: that her presence would restrain abuse of magic.) Wiki-only; `campaign/setting/history/07-a-city-watching-itself.md:34` tags it `[research: wiki only]`. The campaign uses the Masked Lords' support and the office, not Mystra's request, as fact.

**Wiki, the Open Lord date (same line 151)**
> "... supplanting [[Dagult Neverember]] as Open Lord<ref name="DM-p?2">{{Cite book/Death Masks|?}}</ref><ref name="SCAG">{{Cite book/Sword Coast Adventurer's Guide}}</ref>{{Page needed}} ''circa'' the {{YearlinkName|1489}}.{{LaeralOpenLord}}"
> — wiki line 151 (cites *Death Masks* and SCAG; the 1489 DR date is derived on the campaign side, see D7)

### A6. How she governs (day-one habits and position)

**Campaign, history 07 (How Laeral Governs)**
> "- She uses her magic sparingly and relies on trusted advisors and deputies. When time allows she slips out of the Palace in disguise to clear her head and visit old friends."
> — `campaign/setting/history/07-a-city-watching-itself.md:41`
> "- Mirt, a Masked Lord and a senior Harper, is her closest advisor. Elminster, the Warden of Waterdeep, answers to her. The Commander of the Watch reports to her."
> — `campaign/setting/history/07-a-city-watching-itself.md:42`
> "- Her spies keep watch on the adventurers in the city, and she rewards those who put Waterdeep ahead of themselves. Jalester Silvermane is her field operative and reports to her directly, and the Lords' Alliance is her instrument for acting outside the Palace."
> — `campaign/setting/history/07-a-city-watching-itself.md:43`
> "- Vajra Safahr, the Blackstaff, commands Force Grey. Laeral can order Vajra to unleash it in great need. Vajra has secretly sent its members on unauthorized missions, and Laeral has not confronted her."
> — `campaign/setting/history/07-a-city-watching-itself.md:44`

**Adventure, Lords' Alliance entry (page number not read)**
> "Waterdeep is one of the most influential and invested members of the Lords' Alliance. Waterdeep's Open Lord, {@creature Laeral Silverhand|WDH}, uses spies to keep tabs on adventurers in the city, rewarding those who place Waterdeep's interests above their own. Laeral employs adventurers as agents of the Lords' Alliance, among them {@creature Jalester Silvermane|WDH}. See {@adventure appendix B|WDH|12} for more information on these NPCs."
> — `sources/adventure-wdh.json:1384`
> "Laeral spends most of her time in the Palace of Waterdeep. Within walking distance of the palace are well-maintained government residences set aside for the use of representatives of other Lords' Alliance cities and towns."
> — `sources/adventure-wdh.json:1385`

**Adventure, Warden and Commander (the Watch's chain)**
> "The current Warden of Waterdeep is Elminster, who answers to the Open Lord, {@creature Laeral Silverhand|WDH}."
> — `sources/adventure-wdh.json:31836`
> "The Watch also includes a Senior Armsmaster, who reports to the Commander of the Watch and is in charge of supplies. The Commander of the Watch reports to the Open Lord, {@creature Laeral Silverhand|WDH}."
> — `sources/adventure-wdh.json:31886`

**Campaign, open-lord page (how she answers questions; the first sentence is day-one, the second is a quest event, see E2)**
> "- **How Laeral answers questions about the Lords:** She will not name a Masked Lord to anyone and says "That is not mine to give." In **An Audience with the Open Lord** she signs the Masked Lord's Writ for the vault district and discloses the Splinter's offer of an account of every Masked Lord it has confirmed, for a fifth of the vault's contents. She asks the party's opinion and has not decided."
> — `open-lord-and-masked-lords.md:68`

**Adventure, Force Grey command (day-one standing order)**
> "In times of great need, Laeral can command Vajra to unleash Force Grey. Until that order is given, Force Grey isn't allowed to conduct operations in Waterdeep, though Laeral's spies tell her that Vajra has secretly activated members of the elite order and sent them on a number of unauthorized missions. Laeral is reluctant to confront Vajra on the matter, and rationalizes her inaction by framing it as a test of Vajra's competence."
> — `sources/adventure-wdh.json:32206`

**Adventure, the strip-title power**
> "Several of the older and more seasoned wizards in Waterdeep consider Vajra an upstart, but they are smart enough not to challenge her. Only the Open Lord, currently {@creature Laeral Silverhand|WDH}, can strip Vajra of her title."
> — `sources/adventure-wdh.json:32682`

### A7. Mirt, Elminster and the Lords

**Adventure, Mirt entry (page 210)** (the sentence sits in the full paragraph at `:32293`, which begins "Once known as {@creature Mirt|WDH} the Merciless and the Old Wolf" and ends "he is the least concerned with concealing his identity.")
> "Today, an older and wiser {@creature Mirt|WDH} serves as one of the Masked Lords, a Harper, and a close advisor to {@creature Laeral Silverhand|WDH}."
> — `sources/adventure-wdh.json:32293`

**Campaign, open-lord page (GM Notes)**
> "- **Mirt's reveal:** The published adventure says Mirt is the least concerned of the Lords with hiding his identity. The campaign overrides that on purpose. He mentions neither office at the **Harpers First Meeting**, and at the **High Harper** rank he tells the member that he is a Masked Lord and can be asked to act in that capacity once. Laeral knows it."
> — `open-lord-and-masked-lords.md:61`

**Campaign, open-lord page (Key Members, Mirt)**
> "**Mirt** (Chaotic Good, Tethyrian Human, he/him) is a moneylender known as the Old Wolf, and Laeral's closest advisor. The published adventure names him as one of the Masked Lords and says he is the least concerned of them with hiding his identity. The campaign keeps his office from the party until the High Harper rank (see GM Notes). His mansion stands in the Castle Ward, and **Castle Ward** describes it."
> — `open-lord-and-masked-lords.md:40`

### A8. The vault and her day-one belief

**Campaign, history 07 (What Laeral Knows About the Vault)**
> "- Laeral was told for years that the vault lay in Neverwinter, and she believed it. Jalester's field reports and the Watch's contacts have placed it there too."
> — `campaign/setting/history/07-a-city-watching-itself.md:51`
> "- She wants the gold in the treasury. In her framing the money was taxed from Waterdhavian citizens and merchants, and Neverember's exile does not change who owns it."
> — `campaign/setting/history/07-a-city-watching-itself.md:53`

**Campaign, Factions Guide (the Watch's Grand Game stance)**
> "Laeral Silverhand wants the 500,000 gold dragons back in the city treasury. In her view the money was taxed from Waterdhavian citizens and merchants, and Neverember's removal does not change who owns it. She wants it recovered without a public scandal. She does not play the Grand Game herself, because the Lords' Alliance acts for her outside the Palace. The Watch is the part of her government that stands in the street, and its job is order in the wards, not the vault."
> — `campaign/guides/factions/12-open-lords-watch.md:15`

**Campaign, Lords' Alliance Factions Guide (Grand Game Stance)**
> "At campaign start, Laeral is three moves behind. Jalester's field reports and the Watch's contacts have placed the vault somewhere in Neverwinter. She doesn't know that the Stone of Golorr has resurfaced in Waterdeep or that all four villain factions are circling it. The one route by which she can learn of it early is House Gralhund: Yalah can approach the Open Lord with the Stone as collateral (**House Gralhund** in this guide). Characters who share intelligence early change the shape of her involvement. Those who keep her in the dark find her arriving at **Vault of Dragons** as an uncertain variable rather than an ally."
> — `campaign/guides/factions/03-lords-alliance.md:9`

**Alexandrian remix, "Other Minor Factions", Open Lord (PDF p.2, printed p.21; transcribed from the page image, flagged for pdftotext)**
> "OPEN LORD: The Open Lord of Waterdeep isn't exactly a "minor" faction, but Laeral Silverhand is considerably behind the curve in the current Grand Game. She knows that Lord Neverember embezzled 500,000 dragons from the city, but as Dragon Heist begins she is under the belief that he already has the money in Neverwinter. She has agents working to recover it there, but little hope of succeeding (as she believes it has likely already been laundered into Neverember's expansive plans for rebuilding and expanding Neverwinter). She has heard rumors of Neverember's Enigma, but has yet to connect that with the missing dragons, and is also unaware of the Stone of Golorr (although she knows that a powerful artifact was stolen from the palace during the confused time period when Neverember was being ousted from power)."
> — `sources/2. Other Factions.pdf`, PDF p.2 (printed p.21). Transcription; check with `pdftotext -layout` before use.

### A9. Motivations (the only personal-goal line on the page)

**Campaign, Roleplaying Information (Motivations; page text)**
> "**Motivations.** Laeral wants to keep Waterdeep stable after Neverember's ouster, conceal the extent of her diminished power, and resist the urge to reclaim the Blackstaff (which holds Khelben Arunsun's soul)."
> — `campaign/setting/notable-figures/city-officials/01-laeral-silverhand.md:15`

No source gives a personal goal beyond this line. See F8 for what the drafter must stay consistent with.

---

## B. Alignment, species, pronouns, stat block

**B1. Alignment**
- Campaign, Summary: "> - *Moon elf archmage, chaotic good, she/her*. Stat block: **Archmage**." — `campaign/setting/notable-figures/city-officials/01-laeral-silverhand.md:5`
- Campaign, open-lord page: "**Laeral Silverhand** (Chaotic Good, Moon Elf, she/her) is the Open Lord." — `open-lord-and-masked-lords.md:38`
- Campaign, Castle Ward: "**Laeral Silverhand (Chaotic Good, Moon Elf, she/her)** (the moon elf reading is campaign-only)" — `campaign/gazetteer/waterdeep/castle-ward.md:117`
- Campaign, Watch Key Members: "- **Laeral Silverhand** — Moon elf archmage, chaotic good, she/her. The Open Lord, to whom the Commander of the Watch reports. Her Notable Figures page lists her affiliation as the City of Waterdeep. See the **Laeral Silverhand** page in Notable Figures." — `campaign/setting/organizations/11-open-lords-watch.md:78`
- Campaign, quest tag (Lioncrown; the other quest tags agree): "> Laeral Silverhand (Chaotic Good, Moon Elf, she/her) :: the Open Lord of Waterdeep, a silver-haired elf who works at this table whenever the city allows." — `campaign/quests/faction-events/lords-alliance/r50-lioncrown/ev-01-lioncrown.md:76`
- Wiki, 5e infobox: "| alignment5e    = [[Chaotic good]]" — wiki line 61. Also "| alignment35    = [[Chaotic good]]" (wiki line 54, 3e).
- Adventure: no alignment in the Laeral entry (`sources/adventure-wdh.json:32187` to `:32206`).

**B2. Species**
- Campaign, Summary: "*Moon elf archmage, chaotic good, she/her*" — `01-laeral-silverhand.md:5`
- Campaign, history 07: "The campaign makes Laeral a moon elf. The published adventure and the wiki both call her human, and the wiki's alignment, chaotic good, matches the campaign's, so only the species differs (Forgotten Realms Wiki, Laeral Silverhand, infobox race and 5e alignment)." — `campaign/setting/history/07-a-city-watching-itself.md:35`. The first claim about the adventure is wrong (D1).
- Adventure: no species word in the Laeral entry, `sources/adventure-wdh.json:32187` to `:32206` (read in full). Its only identity sentence is "Anamanué {@creature Laeral Silverhand|wdh} was born in the Year of the Cowl (765 DR), the fifth of seven daughters of the goddess Mystra." (`:32201`).
- Wiki, infobox: "| race           = [[Human]]" — wiki line 18. The field has no `<ref>`.
- Wiki, categories: "[[Category:Humans]]" (wiki line 180); "[[Category:Illuskans]]" (wiki line 179). The wiki gives no ethnicity (wiki line 19 is blank).

**B3. Pronouns**
- Campaign: "she/her" — `01-laeral-silverhand.md:5`; `open-lord-and-masked-lords.md:38`.
- Adventure: "She met and married Khelben Arunsun" (`sources/adventure-wdh.json:32202`); "As time allows, she likes to venture outside the Palace" (`:32204`).
- Wiki: "| sex            = Female" — wiki line 17.

**B4. Stat block**
- Campaign, Summary: "Stat block: **Archmage**." — `01-laeral-silverhand.md:5`. The page gives no CR, AC or HP.
- Wiki, 5e infobox: "| challenge5e    = 17" with "| refs5e         = <ref name="WDH5e-p207" />" — wiki lines 62 and 64. The cited printed page 207 is the adventure's Laeral entry, which has no stat block in the JSON (D4).
- Wiki, 3e infobox: "| challenge35    = 34" — wiki line 55.
- Mechanics reference: "Her Archmage stats (CR 12, Wis 15, no Insight proficiency) were read by report 04 and are **not re-verified here.** The roster-free design depends on that rule, not on a block." — `docs/plans/lords-alliance-mechanics-reference.md:304`
- Mechanics reference table: "| Archmage (Laeral) stats | Rep 04 section 7 | **Unverified here** | Not used in any math |" — `docs/plans/lords-alliance-mechanics-reference.md:418`

**B5. Ethnicity.** Not applicable to an elf. Brief ruling 5 applies to humans.

---

## C. Sentences on the current page that narrate a quest event or depend on a discovery

Current page: `campaign/setting/notable-figures/city-officials/01-laeral-silverhand.md`. The page has no Background, Personality or Connections section yet. Each row says where the fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| C1 | L7 | "- **Featured in:** **Fireball!**, **Sea Maidens Faire**, **Kolat Towers**, **Vault of Dragons**, **The Red Wizard's Price**, **Fentree's Ledger**, **An Audience with the Open Lord**, **Escalation to the Open Lord**, **Warduke**, **Lioncrown**, **Force Grey Mission 2 — The Dragon in the Harbor**, **Force Grey Mission 6 — Smoke in the Tower**" | Quest-name list. Route under "Routed to quests" | The quest folders named in the list; `open-lord-and-masked-lords.md:9` and `:10` |
| C2 | L21 | "**Persona.** ... The one exception is a Lioncrown of the Lords' Alliance, to whom she admits it in private during **Lioncrown**." | Quest-time. The admission is the **Lioncrown** event. Restate as a trait or remove | `campaign/quests/faction-events/lords-alliance/r50-lioncrown/ev-01-lioncrown.md` (the event; `history/07-a-city-watching-itself.md:99` cites its "lines 33-38 and 243-261"); `history/07-a-city-watching-itself.md:46` ("She tells one Lioncrown of the Lords' Alliance in **Lioncrown**, and she hopes that a fragment of Halaster's crystal will halt the decline."); `open-lord-and-masked-lords.md:62` |
| C3 | L21 | "**Persona.** ... Deep down, only Elminster knows the extent of her decline since the Spellplague." | Day-one. Keep | `sources/adventure-wdh.json:32203` |
| C4 | L21 | "**Persona.** ... The Blackstaff on Vajra's hip holds the soul of the man she loved." | Day-one. Keep | `sources/adventure-wdh.json:32205` |
| C5 | L25 | "**Relationships.** Laeral is the widow of Khelben Arunsun (the original Blackstaff), the Open Lord who counts Mirt as her closest advisor, ..." | Day-one. "widow" is the campaign's reading (D2) | `history/07-a-city-watching-itself.md:31` and `:42`; `sources/adventure-wdh.json:32202` |
| C6 | L13 | "**Emotions.** ... fleeting joy when she sneaks out in disguise." | Day-one habit. Keep | `sources/adventure-wdh.json:32204` |
| C7 | L11, L15, L23 | Resonance, Motivations, Morale | Day-one. Keep (ruling 3) | `history/07-a-city-watching-itself.md:41`, `:46`; `sources/adventure-wdh.json:32203`, `:32205` |
| C8 | L29 | "Laeral Silverhand is the Open Lord of Waterdeep and fifth of the Seven Sisters — her centuries as an archmage and her political authority make her the most formidable official the party is likely to address directly." | Day-one. 36 words (brief limit 21). Draft a shorter Overview | `sources/adventure-wdh.json:32201`; `history/07-a-city-watching-itself.md:76` |
| C9 | Voice L17 (Never) | "**Never:** She never admits her power is diminished, never begs, and never discusses the Blackstaff's contents. The one exception is **Lioncrown**: alone with the new Lioncrown, after Jalester and Sevel have left the room, she answers honestly that her power is less than her enemies assume and more than her staff knows. She says it once, plainly, and never again." | Quest-time in the second sentence (the Lioncrown annex). The first sentence is day-one | `campaign/quests/faction-events/lords-alliance/r50-lioncrown/ev-01-lioncrown.md:419` and `:423` (the annex: "Laeral Silverhand names a Lords' Alliance member a Lioncrown in a working annex at Piergeiron's Palace."); `history/07-a-city-watching-itself.md:23` |
| C10 | Voice L19 (Greeting) | "*Greeting:* \"You're the ones who found the Stone. Sit. I have perhaps ten minutes, and I'd like all of them to be useful.\"" | Quest-time, and contrary to day one (D3). The party's discovery of the Stone is a quest event | The Stone's quest-time route: `sources/adventure-wdh.json:7152` ("\"Laeral\" tells the characters that Fenerus had a sentient magic item in his possession called the {@item Stone of Golorr|WDH}, which knows the location of a large cache of gold..."). Day-one denial: `history/07-a-city-watching-itself.md:52`; `factions/12-open-lords-watch.md:26`; `factions/03-lords-alliance.md:9` |
| C11 | Voice L20 (Business) | "Whoever holds that gold holds the city's future. I would prefer it be no one." | Day-one (she knows the vault exists). Keep | `history/07-a-city-watching-itself.md:51` |
| C12 | Voice L21 (Under pressure) | "Everyone behind me. Now. I'll explain later, if there is a later." | Day-one generic. Keep | n/a |

**Voice profile, quest-time clauses (`.claude/skills/character-voices/voices/city-officials.md`, "### Laeral Silverhand", lines 7-21)**
- Line 8 (tagline) — day-one.
- Lines 10 to 12 (Sound, Sentence shape, Word choice) — day-one.
- Line 13 (Swearing) "*Stingy · Plain · Clipped.* Never in office. In disguise, out on the town, she enjoys a casual "shit" and a laugh no one would believe." — day-one; keep (adult table).
- Line 14 (Personality in speech) "Her grief for Khelben comes out as silence." — day-one.
- Line 15 (Quirks) — day-one.
- Line 16 (Signature phrases) — day-one.
- Line 17 (Never) — the second sentence is quest-time (C9).
- Line 19 (Greeting) — quest-time (C10).
- Lines 20 and 21 — day-one (C11, C12).

**Quest-time clauses in the profile: line 17 (second sentence) and line 19.**

---

## D. Conflicts

**D1. Species (moon elf or human), and the claim about the adventure**
- Campaign, Summary: "*Moon elf archmage, chaotic good, she/her*" — `01-laeral-silverhand.md:5`
- Campaign, open-lord page: "The published adventure gives her no species, and the moon elf reading is the campaign's own (campaign-only)." — `open-lord-and-masked-lords.md:38`
- Campaign, history 07: "The published adventure and the wiki both call her human, and the wiki's alignment, chaotic good, matches the campaign's, so only the species differs" — `campaign/setting/history/07-a-city-watching-itself.md:35`
- Adventure: no species word in the Laeral entry (`sources/adventure-wdh.json:32187-32206`). The history 07 sentence is wrong about the adventure, and the open-lord page is right.
- Wiki: "| race           = [[Human]]" — wiki line 18.
- Open-lord draft notes: "**Conflicts, Laeral:** the wiki gives her species as human (`wiki.txt` line 29). The adventure gives none, and the campaign says moon elf (`01-laeral-silverhand.md` line 5). The page keeps the campaign reading with the tag." — `open-lord-and-masked-lords.md:106`
- Higher rank: the campaign's decision (moon elf) outranks the wiki (human). The adventure is silent. Keep the campaign's tag; do not write "human" from the wiki.

**D2. Married or never married to Khelben**
- Adventure: "She met and married Khelben Arunsun, who would later become the Blackstaff, the Lord Mage of Waterdeep." — `sources/adventure-wdh.json:32202`
- Wiki: "She was referred to as Lady Arunsun,<ref>...</ref> though they were never married." — wiki line 133
- Campaign: "Laeral is the widow of Khelben Arunsun" — `01-laeral-silverhand.md:25`. "The published adventure says she married Khelben Arunsun, who became the Blackstaff, and retired from public life after he died. The campaign keeps her a widow." — `campaign/setting/history/07-a-city-watching-itself.md:31`
- Campaign, history 07 Draft Notes: "The wiki's Laeral page says she never did (City of Splendors: Waterdeep, 3e; Seven Sisters, 2e), but its Khelben Arunsun page calls her his lady love and speaks of his wife, so the wiki contradicts itself." — `history/07-a-city-watching-itself.md:126`
- Higher rank: the adventure, then the campaign, which follows it. The wiki's "never married" is lower-ranked and self-contradictory.

**D3. Does Laeral know the Stone has resurfaced on day one?**
- Campaign, history 07: "She does not know the Stone of Golorr has resurfaced, and she does not know four villain factions are moving on the city." — `history/07-a-city-watching-itself.md:24`
- Campaign, Factions Guide: "She doesn't know that the Stone of Golorr has resurfaced in Waterdeep or that all four villain factions are circling it." — `factions/03-lords-alliance.md:9`
- Campaign, Watch Factions Guide: "She does not know that the Stone of Golorr has resurfaced in Waterdeep." — `campaign/guides/factions/12-open-lords-watch.md:26`
- Campaign, Watch org page: "She does not know that the Stone of Golorr has resurfaced in Waterdeep or that four villain factions are circling it (**A City Watching Itself**)." — `campaign/setting/organizations/11-open-lords-watch.md:93`
- Voice profile: "*Greeting:* "You're the ones who found the Stone. Sit. I have perhaps ten minutes, and I'd like all of them to be useful."" — `.claude/skills/character-voices/voices/city-officials.md:19`
- Alexandrian PDF, printed p.21: "is also unaware of the Stone of Golorr" (`sources/2. Other Factions.pdf`, PDF p.2). It agrees on day one and adds the artifact line (E3).
- Higher rank: the campaign. The Greeting is the conflict. Brief ruling 16 requires the profile to change to match.

**D4. Stat block (CR)**
- Campaign, Summary: "Stat block: **Archmage**." — `01-laeral-silverhand.md:5`. No CR on the page.
- Wiki, 5e: "| challenge5e    = 17" — wiki line 62 (refs `WDH5e-p207`).
- Wiki, 3e: "| challenge35    = 34" — wiki line 55.
- Mechanics reference: "(CR 12, Wis 15, no Insight proficiency)" — `docs/plans/lords-alliance-mechanics-reference.md:304`; "Unverified here" at `:418`.
- Adventure: no CR (`sources/adventure-wdh.json:32187-32206`).
- Higher rank: none verified. Left open for the stat-block pass.

**D5. Masked Lords: does Laeral know each other's identities?**
- Open-lord page: "**Hidden from each other:** The published adventure says the Lords' identities are hidden even from each other, and it wins over the wiki, which says they were known to each other." — `open-lord-and-masked-lords.md:62`. The adventure's line is `sources/adventure-wdh.json:30477` (cited at `open-lord-and-masked-lords.md:103`).
- Open-lord page, the same bullet: "Laeral tells a Lioncrown "I know them, and I will not name one", and the campaign reads this as one of the Open Lord's reserved powers, which is a ruling for the user to confirm. `[research]`" — `open-lord-and-masked-lords.md:62` (quest-time quote in a setting page; see E2).
- Open-lord page, GM Notes: "Laeral knows it." (Mirt's office) — `open-lord-and-masked-lords.md:61`.
- Higher rank: the adventure. The `[research]` tag stays. The page should not say whether she knows the other Lords' identities.

**D6. Mirt's office: public or hidden (affects what Laeral says, not what she knows)**
- Open-lord page: "Laeral knows it." — `open-lord-and-masked-lords.md:61`
- Harpers Mirt notes (`docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`, D1) list the open conflict on whether the office is public. Laeral's knowledge is not in dispute. The Laeral page should not say whether Mirt's office is public to the party.

**D7. The Open Lord's date**
- Adventure: "A few years ago, Dagult Neverember was ousted as Open Lord of Waterdeep." — `sources/adventure-wdh.json:32204`
- Campaign: "she has held the office since about 1489 DR" — `history/07-a-city-watching-itself.md:76`. "The start year is therefore derived." — `history/07-a-city-watching-itself.md:16`
- Wiki: "circa the {{YearlinkName|1489}}" — wiki line 151.
- Not a true conflict. The 1489 DR date is derived on the campaign side (`history/07:16`). The page may say "since about 1489 DR" or follow the adventure's "a few years ago".

**D8. Bregan D'aerthe and Laeral**
- Adventure: "Harper spies in Luskan recently warned Laeral that Jarlaxle might be in Waterdeep. She reached out to him with a {@spell sending} spell to arrange this meeting, in the hope of finding out his plans." — `sources/adventure-wdh.json:26633` (the meeting itself is at `:26632`: "These Bregan D'aerthe spies are on their way to a secret meeting with {@creature Laeral Silverhand|WDH} (see {@adventure appendix B|WDH|12}).").
- Campaign: the meeting is omitted. "Conflicts: Bregan D'aerthe. `adventure-wdh.json` lines 26632-26633 have Laeral arranging a meeting ... This page follows the campaign and omits the meeting." — `history/07-a-city-watching-itself.md:125`. Also: "The campaign has nobody name Jarlaxle to her before **Jarlaxle Unmasked** (`r50-lioncrown/ev-01-lioncrown.md` line 38)." — same line.
- Jarlaxle's page: "- **Laeral Silverhand:** The Open Lord, whose debt he wants more than any sum of gold. She regards Luskan as a greedy pirate state that cannot be trusted." — `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:58`. Consistent with `campaign/setting/organizations/07-bregan-daerthe.md:77`: "He wants Laeral Silverhand in his debt more than he wants any sum of gold, and he wants one Eye of the Stone as a chip to trade for it."
- Higher rank: the campaign. Laeral does not know Jarlaxle's face before **Jarlaxle Unmasked**. The page must not connect her to the Bregan spies in the Dock Ward alley.

**D9. Residence**
- Wiki, the griffin story (edition not printed; cites a gamebook): "Both baby griffin and its trainer were staying inside Laeral's mansion in Waterdeep." — wiki line 155 (ref `tCaT-p4`). Wiki-only.
- Adventure: "Laeral spends most of her time in the Palace of Waterdeep." — `sources/adventure-wdh.json:1385`
- Campaign: no mansion for Laeral. The Palace is her working residence (`open-lord-and-masked-lords.md:29`: "The Open Lord governs from the Palace of Waterdeep").
- Not a conflict as such. The wiki's mansion is outside the campaign.

**D10. Harpers and the Moonstars**
- Wiki: "Together with her partner [[Khelben \"Blackstaff\" Arunsun]], they led the [[Moonstars]], a dissident faction of the [[Harpers]]" — wiki line 66 (ref `FRCS3e-280`).
- Campaign: "the 1370 DR Moonstars schism with Laeral's departure, the Wailing Years, the Harpers of Luruar, the double agent of about 1479 DR and the Tiamat years are wiki parallels. The campaign has no Moonstars page, and Khelben is dead in the campaign." — `campaign/setting/organizations/01-harpers.md:187`
- Not a conflict with the page. The Moonstars is not in the campaign; do not write it as day-one.

---

## E. Stale lines in other files (not edited), and routed quest references

**E1. The species sentence in `history/07` (see D1)**
- `campaign/setting/history/07-a-city-watching-itself.md:35`: "The published adventure and the wiki both call her human" — the adventure does not (`sources/adventure-wdh.json:32187-32206`).

**E2. Quest events narrated in setting pages (campaign-start rule, brief ruling 1)**
- `campaign/setting/history/07-a-city-watching-itself.md:23`: "She governs with deputies ... and she admits it to one Lioncrown of the Lords' Alliance." (the full bullet is quoted in A3; the last clause is quest-time).
- `campaign/setting/history/07-a-city-watching-itself.md:46`: "- Only Elminster knows the full extent of her decline. She tells one Lioncrown of the Lords' Alliance in **Lioncrown**, and she hopes that a fragment of Halaster's crystal will halt the decline."
- `campaign/setting/history/07-a-city-watching-itself.md:52`: "- She does not know that the Stone of Golorr has resurfaced in Waterdeep or that the four villain factions are circling it. **Fentree's Ledger** corrects her intelligence." (the first clause is day-one; the last sentence is quest-time.)
- `campaign/setting/history/07-a-city-watching-itself.md:60`: "- Members who bring the Grand Game to Jalester draw her interest. Once she is fully informed she makes the recovery a political priority and gives the party real resources."
- `campaign/setting/history/07-a-city-watching-itself.md:61`: "- If the party holds the gold and she learns of it, she makes one polite offer to take it back in exchange for a 10 percent finder's fee, which is 50,000 gp. She asks once and accepts the answer."
- `campaign/setting/history/07-a-city-watching-itself.md:62`: "- In **An Audience with the Open Lord** she issues a Masked Lord's Writ for the vault district whatever answers the party gives. She also discloses a Splinter offer: a complete account of the Masked Lords it has confirmed, for a fifth of the vault's contents before the treasury sees them. She has not decided, and she asks the party's opinion."
- `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:62`: "- **Hidden from each other:** ... Laeral tells a Lioncrown "I know them, and I will not name one", ..." (quest-time quote; see D5).
- `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:68`: "- **How Laeral answers questions about the Lords:** ... In **An Audience with the Open Lord** she signs the Masked Lord's Writ for the vault district ..." (see A6).

**E3. The Alexandrian artifact line**
- `sources/2. Other Factions.pdf`, PDF p.2 (printed p.21): "(although she knows that a powerful artifact was stolen from the palace during the confused time period when Neverember was being ousted from power)". No campaign file carries the artifact line. The Watch's Draft Notes say so ("Conflicts: The stolen artifact", `campaign/setting/organizations/11-open-lords-watch.md`, Draft Notes; the notes cite `history/07-a-city-watching-itself.md:124`).

**E4. Routed quest references (quest-time; the day-one page must not restate them)**
- `campaign/quests/faction-events/lords-alliance/r50-lioncrown/ev-01-lioncrown.md`: the annex scene at lines 46, 419 and 423 (Grep), and the source lines 33-38 and 243-261 (per `history/07` Source References at `:99`).
- `campaign/quests/faction-events/lords-alliance/r25-warduke/ev-01-warduke.md:39`: "- The Masked Lord is a Lord of Waterdeep who owes Laeral a favor and acts through her office. The Lord is never named, and it is neither Mirt nor Jelenn Urmbrusk."
- `campaign/quests/faction-events/lords-alliance/r25-warduke/ev-01-warduke.md:336` (her tag and scene).
- `campaign/quests/faction-events/lords-alliance/m06-an-audience-with-the-open-lord/ev-01-an-audience-with-the-open-lord.md:126` (her tag and scene).
- `campaign/quests/faction-events/force-grey/r50-force-grey-commander/ev-01-force-grey-commander.md:251` (her tag and scene).
- `campaign/quests/faction-events/harpers/r50-high-harper/ev-01-high-harper.md:54` (her tag; cited by the Mirt notes).
- `campaign/guides/factions/12-open-lords-watch.md:168` (cites `campaign/quests/faction-events/lords-alliance/s02-escalation-to-the-open-lord/ev-01-escalation-to-the-open-lord.md:254` to `:256`, the LA Grand Game Escalated rule).
- Adventure, quest-time: `sources/adventure-wdh.json:7144` (Jarlaxle disguised as "Laeral" offers a quest); `:7152` (the Stone and the fake-Laeral request); `:10629` ("A character who has at least 4 renown in the Lords' Alliance can arrange a meeting with {@creature Laeral Silverhand|WDH} (see {@adventure appendix B|WDH|12}) at Piergeiron's Palace"); `:14888` ("{@creature Laeral Silverhand|WDH} is prepared to let the characters keep one-tenth of the treasure (50,000 gp) for themselves."); `:22949` (Jarlaxle returns the gold to Laeral); `:26632` and `:26633` (the Bregan meeting); `:26657` ("cautions them to mind the City Watch and the City Guard"); `:26666` ("Conversation with Laeral"); `:26740` ("{@creature Laeral Silverhand|WDH} summons them to the Palace of Waterdeep to thank them officially"); `:26764` (the ledger).

**E5. Other files that name Laeral, checked for stale lines**
- `campaign/setting/notable-figures/harpers/01-mirt.md:36` (the Mirt page, being redrafted): "- **Laeral Silverhand:** The Open Lord, who counts Mirt as her closest advisor and knows him as a Masked Lord." Consistent with `open-lord-and-masked-lords.md:61`.
- `campaign/setting/notable-figures/lords-alliance/01-jalester-silvermane.md:40`: "- **Laeral Silverhand:** The Open Lord, to whom he reports directly. She put him and Faerrel to work as deputies and spies, and his badge of the Watch returns to her if he loses it." Consistent with `sources/adventure-wdh.json:32167` ("If the badge is lost or taken from him, it returns to {@creature Laeral Silverhand|WDH}.").
- `campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md:38`: "- **Laeral Silverhand:** The Open Lord and Vajra's superior, who views her as an insecure child wielding her late husband's staff." Consistent.
- `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:58` (see D8).
- `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:100`: the table has no Laeral row; not stale.

**E6. Resolved, no action**
- `docs/plans/setting-compendium-research-notes/consistency-notable-figures.md:5` said the old line 25 inverted Mirt and Laeral ("Laeral NF city-officials/01:25 calls Laeral 'a close advisor to Mirt': inverted"). The current line 25 reads "the Open Lord who counts Mirt as her closest advisor" and is correct.

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` (brief ruling 17) and is listed in the Draft Notes.

**F1. Childhood, parents and training.** The adventure gives only "the fifth of seven daughters of the goddess Mystra" (`:32201`). The wiki gives parents Dornal Silverhand and Elué (wiki line 106) and Elminster as guardian and teacher (wiki line 119). Both are wiki-only and tagged. The campaign says nothing. Do not contradict "fifth of seven daughters of the goddess Mystra".

**F2. Marriage, how she met Khelben, and children.** The adventure says she married him (`:32202`). The wiki gives a 1357 DR rescue from the Crown of Horns (wiki line 133) and says "never married". The wiki gives three children (wiki line 110: "She had three children, a girl named Maura of Evermeet ... Laeral also had twins, a boy named Krehlan Arunsun ... and a girl named Kamaulra"). No campaign file names any child. Do not give children, and do not describe the meeting, without a `[research]` tag and the D2 caveat.

**F3. Khelben's death.** The adventure says "After Khelben died, Laeral retired from public life." (`:32202`). The wiki dates it 1374 DR (wiki line 146). The campaign gives no date. `campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md:141` says: "The page states the handpicking and gives no date for his death." Give no year, or tag the wiki.

**F4. Why she came back to Waterdeep.** The campaign: her magic "waned with Mystra's death and the Spellplague" (`history/07:23`). The adventure: she "resurfaced after the Spellplague and the Sundering, weakened by Mystra's death, rebirth, and withdrawal from the world." (`:32202`). The wiki says Mystra asked her to become Open Lord (wiki line 151), which the campaign tags `[research: wiki only]` (`history/07:34`). Keep the campaign's and the adventure's accounts; the Mystra request is wiki-only.

**F5. Her health and magic as a daily fact.** The campaign: "Only Elminster knows how far, and she admits it to one Lioncrown of the Lords' Alliance." (`history/07:23`). The second clause is quest-time (C9). Day-one: only Elminster knows the extent (`:32203`). Do not write what she can still cast.

**F6. Home and daily life.** The adventure makes the Palace her place of work and, in practice, her residence ("Laeral spends most of her time in the Palace of Waterdeep." `:1385`). The adventure gives no private house. The wiki's mansion (wiki line 155) is in a gamebook and is not campaign canon.

**F7. Appearance.** The adventure has an image and no text (`:32195` to `:32199`, the title "{@creature Laeral Silverhand|WDH}"). The only text descriptions are quest tags: "a silver-haired elf who works at this table" (`r50-lioncrown/ev-01-lioncrown.md:76`) and "a tall silver-haired elf in a plain grey gown" (`m06-an-audience-with-the-open-lord/ev-01-an-audience-with-the-open-lord.md:126`). Quest-time tags; do not use them as day-one description without a `[design]` tag.

**F8. Personal goals beyond the office.** The only source line is Motivations: "Laeral wants to keep Waterdeep stable after Neverember's ouster, conceal the extent of her diminished power, and resist the urge to reclaim the Blackstaff (which holds Khelben Arunsun's soul)." (`01-laeral-silverhand.md:15`). The adventure adds "Laeral covets the staff, because it contains all that's left of her husband." (`:32205`). The wiki's goal is in the past tense: "Her ultimate goal however, was to unite all thinking races, be they [[dwarves]], [[elves]], [[human]]s, or [[orc]]s in a goodly purpose." (wiki line 99, cites *The Seven Sisters* pp. 31-32; wiki-only). Any `[design]` goal must not reveal the Blackstaff's contents, the vault, the Stone, the Writ or the Splinter offer, the Lioncrown admission, or any Event Outcome (brief ruling 17). A goal about the staff must not give her a plan to take it: the adventure has her reluctant to confront Vajra (`:32206`).

**F9. Her patron.** The wiki gives "patron deity = [[Mystra]]" (wiki line 22). The adventure names Mystra as her mother (`:32201`). Write "a Chosen of Mystra" only with the adventure's letter wording (`:26646`) or the wiki (line 149).

**F10. Who she trusts and dislikes.** The adventure gives her relationship with Vajra (`:32205`), Elminster as "her trusted friend and advisor" (`:32203`), Mirt as "a close advisor" (`:32293`), and Xanathar's fear of her: "{@creature Xanathar|WDH} has a healthy fear of {@creature Laeral Silverhand|WDH} and is inclined to spare those in her employ, to avoid provoking a conflict with Waterdeep's Open Lord." (`sources/adventure-wdh.json:528`; the Xanathar rule is that it is "it"). The wiki says "She disliked [[doppelganger]]s and slave-owners." (wiki line 73; cites *The Seven Sisters* p. 31; wiki-only). Do not use the doppelganger line without a tag: the campaign's doppelganger threads (Vessa, Bonnie) are quest-time.

**F11. Khelben's apprentices.** Wiki line 92: "She also kept constant watch on any of Khelben's apprentices who left Blackstaff Tower to ensure that no treachery was afoot." (wiki-only; cites *The Seven Sisters* pp. 32 and 117-118).

---

## G. Source facts that hint at the figure's inner life (for the backstory; do not contradict)

- "Laeral's magic isn't as great as it once was, though she does her utmost to hide this fact." — `sources/adventure-wdh.json:32203`. (Pride and fear of exposure.)
- "Laeral covets the staff, because it contains all that's left of her husband." — `sources/adventure-wdh.json:32205`. (Grief.)
- "After Khelben died, Laeral retired from public life." — `sources/adventure-wdh.json:32202`. (Withdrawal.)
- "As time allows, she likes to venture outside the Palace of Waterdeep in disguise, just to clear her head or check up on old friends (and enemies)." — `sources/adventure-wdh.json:32204`. (Old friends; a private restlessness.)
- "Laeral is reluctant to confront Vajra on the matter, and rationalizes her inaction by framing it as a test of Vajra's competence." — `sources/adventure-wdh.json:32206`. (Avoidance.)
- "Initially overwhelmed by the demands of the nobles and guildmasters, she has settled nicely into her new role." — `sources/adventure-wdh.json:32204`. (The office was a burden she accepted.)
- "She accepted the role because the city needed her, and she holds it with weary precision." — `01-laeral-silverhand.md:29` (the page's Overview).
- "She avoids direct confrontation when possible because every expenditure of power reveals how much she has lost." — `01-laeral-silverhand.md:23` (Morale; a fear of visible decline).
- "restless grief for Khelben" — `01-laeral-silverhand.md:13` (Emotions).
- "Her grief for Khelben comes out as silence." — `.claude/skills/character-voices/voices/city-officials.md:14`.
- "She lets a silence run until the other person fills it." — `city-officials.md:15` (Quirks).
- "She never admits her power is diminished, never begs, and never discusses the Blackstaff's contents." — `city-officials.md:17` (first sentence only; the second is quest-time, C9).
- "much older, much wiser, and much more powerful than Vajra, whom she views as an insecure child" — `sources/adventure-wdh.json:32205`.
- "Having been in thrall to the ''Crown of Horns'' and forced to commit heinous acts by it, she felt that she understood the nature of evil better than most" — wiki line 71 (cites *The Seven Sisters* p. 32; wiki-only). (A past wound.)
- "Realizing too late that she was in love with Malek, Laeral quit her court and spent twenty five years wandering Stornanter." — wiki line 123 (wiki-only; see A2).
- "Laeral never denied this, instead preferring to let those who wished Khelben harm seek her out as an ally against him." — wiki line 133 (wiki-only; cites *The Seven Sisters* pp. 28-29). Conflicts with D2 on the marriage.
- "She was also proactive in her defense of the city, to the extent that certain Waterdhavians would stage calamitous events so that she would keep tabs on persons of interest for them without their needing to ask for her help or involve themselves directly." — wiki line 69 (wiki-only).
- Do not use: the wiki's Malek story is wiki-only; the campaign has no Malek. Do not use "She hopes that a fragment of Halaster's crystal will halt the decline" (`history/07:46`), which is quest-time.

---

## Cross-references (Laeral topic in other files)

- `campaign/setting/notable-figures/city-officials/01-laeral-silverhand.md:5`, `:7`, `:11`, `:13`, `:15`, `:17`, `:21`, `:23`, `:25`, `:29`.
- `campaign/setting/organizations/11-open-lords-watch.md:61` ("The Open Lord (superior): The Commander reports to Laeral, and her closest advisor, Mirt, is a Masked Lord (*Dragon Heist*, 5e; **A City Watching Itself**).")
- `campaign/setting/organizations/11-open-lords-watch.md:78` (her Key Members entry), `:92` ("- **What Laeral believes on day one:** She believes the vault, and so the gold, lies in Neverwinter."), `:93` (the Stone line, quoted in D3).
- `campaign/guides/factions/12-open-lords-watch.md:15` (Grand Game Stance), `:25`, `:26`.
- `campaign/guides/factions/03-lords-alliance.md:7`, `:9`.
- `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:16`, `:29`, `:30`, `:31`, `:38`, `:61`, `:62`, `:63`, `:66`, `:68`, `:103`, `:106`, `:112`, `:113`.
- `campaign/setting/history/07-a-city-watching-itself.md:16`, `:23`, `:24`, `:26`, `:30`, `:31`, `:32`, `:33`, `:34`, `:35`, `:36`, `:37`, `:41` to `:46`, `:50` to `:53`, `:59` to `:65`, `:76`, `:99`, `:124`, `:125`, `:126`.
- `campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md:38`, `:39`, `:95`, `:141`.
- `campaign/setting/notable-figures/lords-alliance/01-jalester-silvermane.md:40`.
- `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:58`.
- `campaign/setting/notable-figures/harpers/01-mirt.md:36`, `:50`, `:85`, `:89` (the Mirt page's Laeral lines).
- `campaign/setting/organizations/07-bregan-daerthe.md:77` (Jarlaxle wants her in his debt).
- `campaign/setting/organizations/01-harpers.md:187` (the Moonstars is not in the campaign; Khelben is dead in the campaign).
- `campaign/setting/villains/jarlaxle.md:49`, `:108`, `:171` (Laeral as Jarlaxle's target for Luskan and the Renaer link).
- `campaign/setting/villains/manshoon.md:38` ("He wants to oust Laeral Silverhand as Open Lord by bribing and blackmailing the Masked Lords ...").
- `campaign/setting/deities/myrkul.md:54`, `:90`, `:114` (the Crown of Horns, wiki-only).
- `campaign/gazetteer/waterdeep/castle-ward.md:117`.
- `sources/Act_III_Arc_D.md:215` ("He worked for the rightful Open Lord — by which he means Lord Dagult Neverember, not Laeral Silverhand."; about Dalakhar, a Fireball! victim; quest-time).
- `sources/Appendix_B_-_Player_Factions.md:255`, `:256`, `:920` (Warduke, Lioncrown and Force Grey Commander rank benefits naming Laeral; quest-time).
- `sources/Appendix_D_-_Running_the_Tavern.md:1445` ("He has thoughts. Some of them are Laeral's.").
- `sources/SOURCE_GUIDE.md:265`, `:498`, `:633` (what the guide says about Laeral in the Watch, Vault and Stone entries).

## Not found

- **Searched for:** a species, race or ethnicity for Laeral in the published adventure. Method: Read of the full Laeral entry, `sources/adventure-wdh.json:32187-32206`, and every Grep hit for `Laeral|Barnibus` in the JSON. Result: no species, race, alignment or stat block.
- **Searched for:** a CR or stat block for Laeral: the adventure (none, as above); `docs/` (only `lords-alliance-mechanics-reference.md:304` and `:418`).
- **Searched for:** a campaign date for Khelben's death: `campaign/setting` (Grep for `1374|Khelben[^.]{0,60}(died|death|killed|dead)`). None for Khelben's death in the campaign (`01-vajra-safahr-the-blackstaff.md:141` gives none).
- **Searched for:** children, parents, siblings, a childhood, a training, Stornanter, the Nine, the Crown of Horns, Malek, Gelda, Irusyl and the Moonstars in the campaign (Grep for `Stornanter|Crown of Horns|Gelda|Irusyl|Malek Aldhanek|Blackstaff Academy|Moonstars`): only `iggwilv.md:73` (the adventure's Stornanter title), `myrkul.md:54`, `:90`, `:114`, `01-harpers.md:187`, and the Vajra page's Blackstaff Academy line (`:53`). None describes Laeral's own childhood or training.
- **Searched for:** Laeral's personal mansion or home other than the Palace: `campaign/` (Grep for "Laeral" with home terms). Only the Palace references above.
- **Searched for:** the 1487 DR Weave return as a campaign fact: `1487` under `campaign/`. Only `history/07-a-city-watching-itself.md:23` names Laeral's recovery; the deity pages date other events to 1487.
- **Searched for:** Laeral's appearance in text (not tags): the adventure has an image only (`:32195` to `:32199`); the campaign's only description is in quest tags.
- **Searched for:** whether Laeral knows each Masked Lord's identity: `open-lord-and-masked-lords.md:62`. A `[research]` ruling, not settled.
- **Searched for:** Laeral's alias ("Gelda", "Irusyl"): not in the campaign. Wiki-only (wiki lines 12, 71, 144).
- **Searched in:** Alexandrian Appendices B, C and D (`sources/Appendix_B_-_Player_Factions.md`, `Appendix_C_-_Player_Faction_Missions.md`, `Appendix_D_-_Running_the_Tavern.md`) and `sources/Act_III_Arc_D.md` (Grep for `Laeral`). Hits at Arc D line 215; Appendix B lines 255, 256, 920; Appendix D lines 1384 and 1445. No Alexandrian source gives Laeral a day-one personal fact beyond the Open Lord paragraph in `2. Other Factions.pdf` (PDF p.2).
- **Not searched:** `sources/20. The Vault.pdf` (SOURCE_GUIDE line 498: "Laeral Silverhand's involvement: when and how the Open Lord appears"). It is Vault of Dragons material, which is quest-time, and was not read in this pass. `sources/7. Other Response Teams.pdf` (the Open Lord team, printed p.58; cited in the Watch Draft Notes) was not read here.
- **Not searched:** `sources/research/pass3-bundles/open-lord-and-masked-lords/wiki.txt` beyond the lines the Open Lord page quotes (wiki.txt lines 29, 588, 740, 747, 752, as cited at `open-lord-and-masked-lords.md:103` to `:113`). The scratchpad extract is the wiki page used here.

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. `sources/SOURCE_GUIDE.md` names no `.docx` for Laeral (its Laeral lines are at `:265`, `:498` and `:633`, none naming a `.docx`). Not checked for Laeral.
- `sources/2. Other Factions.pdf`: read as rendered page images (PDF p.2, printed p.21), not `pdftotext`. The OPEN LORD quote in A8 is a transcription.
- `sources/20. The Vault.pdf` and `sources/7. Other Response Teams.pdf`: not read in this pass (see Not found).
