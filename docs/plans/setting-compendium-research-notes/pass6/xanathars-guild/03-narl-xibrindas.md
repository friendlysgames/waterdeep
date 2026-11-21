# Pass 6 research notes: Nar'l Xibrindas

Page: `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Repo paths below are relative to `/home/user/waterdeep`. Scratchpad paths are absolute.
Ruling used: Nar'l is Xanathar's only advisor and a Bregan D'aerthe plant placed in the Guild in 1491 DR, a year before Ches 1, 1492 DR (`campaign/setting/organizations/08-xanathars-guild.md:23`). His secret allegiance is GM-only. The Overview shows only the advisor.

Method and caveats:
- Campaign files: Read and Grep, quoted from the file. Line numbers are from tool output.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. Tags such as `{@creature ...}` are left as written. JSON escapes are shown as plain quotes.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. The PDFs were read as rendered page images with the Read tool. Every PDF quote is marked **[img]** and is a transcription. Check it against `pdftotext -layout` before any quote goes into prose. Printed page numbers come first, PDF page in brackets.
- The Alexandrian spelling is "N'arl" in the PDFs and Appendix D, and "Nar'l" in the campaign and adventure. Quotes keep each source's spelling.
- Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-xg/Nar_l_Xibrindas.txt` (read, lines 1 to 104), cited below as `Nar_l_Xibrindas.txt`. `.../wiki-xg/Narl_Xibrindas.txt` returned NOT FOUND. Bundle copies: `sources/research/pass5-bundles/xanathars-guild/wiki.txt` and `sources/research/pass5-bundles/bregan-daerthe/wiki.txt`. Most wiki lines print no edition. Editions come from the citation key and are marked inferred where so.
- House Xorlarrin and Soluun Xibrindas were searched only in `sources/SOURCE_GUIDE.md`, the adventure, the Alexandrian PDFs and appendices, the campaign, and the `sources/research/` bundles, as the caller set. The scratchpad `fandom-dump` folder is outside that set and was not searched.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written. Nothing was committed.
- `voicecheck.py` was not run (research only).

---

## A. Background facts by theme

### A1. Family, house and origin

**Campaign, the house and the brother (day-one)**
> "- Nar'l Xibrindas is an example. His house was wiped out long ago, and he and his elder brother Soluun survived and joined the company."
> — `campaign/setting/history/03-bregan-daerthes-long-road.md:43`

**Adventure, the house and the brother (5e, day-one background)**
> "{@creature Xanathar|WDH}'s advisor is a nervous and conniving male drow named {@creature Nar'l Xibrindas|wdh}. Nar'l's house was wiped out long ago, but he and his elder brother Soluun survived and joined Bregan D'aerthe. A year ago, Nar'l was given the difficult task of infiltrating the Xanathar Guild and getting as close to the beholder as possible. Not only did he succeed, but in the course of gaining {@creature Xanathar|WDH}'s trust, he managed to convince the beholder to eliminate its other advisors. The beholder's paranoia will eventually cause {@creature Xanathar|WDH} to question the drow's loyalty, though, and Nar'l has become increasingly worried about his future. If forced to decide between himself and Bregan D'aerthe, he'll choose the former and betray his drow allies to save his own skin."
> — `sources/adventure-wdh.json:32323` (entry "Nar'l Xibrindas", `"page": 211` at `:32310`)

**Wiki, the house (wiki only; the paragraph carries no citation, the nearby History paragraph cites WDH5e-p211)**
> "The family's house was destroyed and only Nar'l and his elder brother [[Soluun Xibrindas|Soluun]] survived. They decided to join [[Bregan D'aerthe]]."
> — `Nar_l_Xibrindas.txt:68` (History; edition 5e inferred from the citation at `:70`)

**Adventure, the pronunciation (5e)**
> "{@creature Nar'l Xibrindas|WDH}" with the pronunciation "NAR-ul zeh-BRIN-das" on the next line
> — `sources/adventure-wdh.json:249`-`:250`

**Wiki infobox, race and home (wiki only; edition inferred 5e from `refs5e`)**
> "| home           = [[Waterdeep]], [[Sword Coast North]]"
> — `Nar_l_Xibrindas.txt:11`
> "| race           = [[Drow]]"
> — `Nar_l_Xibrindas.txt:14`

**Soluun's view of Nar'l (adventure, 5e; the brothers' ages)**
> "His younger brother, Nar'l, has infiltrated the Xanathar Guild. Soluun considers Nar'l a weakling who turned to arcane magic by way of compensation, and he has never had much faith in his brother or his abilities."
> — `sources/adventure-wdh.json:32040` (Soluun Xibrindas entry, which begins at `:32036`)

**Age (Alexandrian, quest-scene description, not a campaign or adventure fact)**
> "He is approximately sixty by drow standards, thin-faced, with the composed expression of someone who has been expecting visitors and has had time to decide what to say to them."
> — `sources/Appendix_C_-_Player_Faction_Missions.md:1627` (Arc BD-4, Scene 3, Area X35)

### A2. Joining Bregan D'aerthe

**Campaign, placed by Jarlaxle before the campaign (day-one)**
> "- Jarlaxle placed Nar'l Xibrindas inside the Xanathar's Guild before the campaign. Nar'l convinced the current Xanathar, a beholder named Zushaxx (it/its), to eliminate its other advisors, and he reports to Jarlaxle by *Sending*."
> — `campaign/setting/history/08-the-players-arrive.md:47`

**Campaign, the 1491 date (day-one, sourced)**
> "1491 DR (sourced): Nar'l Xibrindas is assigned to the Xanathar's Guild, one year before the campaign. The wiki also has Jarlaxle acquire the *Scarlet Marpenoth* this year."
> — `campaign/setting/history/08-the-players-arrive.md:81`

**Adventure, the Bregan D'aerthe faction entry (5e)**
> "Bregan D'aerthe is skilled at infiltrating criminal organizations. {@creature Xanathar|WDH}'s drow advisor, {@creature Nar'l Xibrindas|wdh} (see {@adventure appendix B|WDH|12}), is actually a Bregan D'aerthe spy. Bregan D'aerthe support comes in these ways:"
> — `sources/adventure-wdh.json:1301`

**Adventure, Jarlaxle's spy and the route (5e; a sentence in the lair chapter, not in a Nar'l entry)**
> "Jarlaxle has a spy in the Xanathar Guild: the advisor {@creature Nar'l Xibrindas|wdh}, who uses {@spell sending} spells to transmit intelligence to his drow brethren. Bregan D'aerthe knows that the safest route to the beholder's lair is a secret staircase in the sewers of the Castle Ward. Any character who belongs to this faction can get this information from Jarlaxle or another source."
> — `sources/adventure-wdh.json:15149`

**Wiki, the 1491 assignment (wiki only; 5e)**
> "In [[1491 DR]], Nar'l was assigned a mission to infiltrate the [[Xanathar's Thieves' Guild]] and get closer to the [[beholder]] crime lord. Nar'l was so successful that he became the only advisor of the Xanathar.<ref name="WDH5e-p211" />"
> — `Nar_l_Xibrindas.txt:70`

**Bregan D'aerthe wiki page, the same (wiki only; WDH5e-p211)**
> "*[[Nar'l Xibrindas]], Soluun's younger brother on a mission to infiltrate the [[Xanathar's Thieves' Guild]] becoming [[Xanathar]]'s only wizard advisor in [[1491 DR]].<ref name="WDH5e-p211">{{Cite book/Waterdeep: Dragon Heist|211}}</ref>"
> — `sources/research/pass5-bundles/bregan-daerthe/wiki.txt:135`

No source gives a date for the recruitment, a place, or the person who recruited him beyond Jarlaxle (see F4).

### A3. Placement in the Guild and tenure

**Campaign, Guild history (day-one; the one-year tenure)**
> "- **1491 DR, Nar'l Xibrindas.** Bregan D'aerthe placed Nar'l in the Guild a year before the campaign. He won Xanathar's trust and persuaded it to eliminate its other advisors, and he has been its only advisor since (*Dragon Heist*, 5e; Forgotten Realms Wiki, *Xanathar's Thieves' Guild*, 5e)."
> — `campaign/setting/organizations/08-xanathars-guild.md:23`

**Campaign, the page's own Persona (day-one)**
> "To Jarlaxle, he is Bregan D'aerthe's best intelligence source on Guild movements, reporting via Sending spell after one year in place, placed in 1491 DR."
> — `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:21`

**Campaign, Settled ruling (Session 47)**
> "- **Settled by the user (Session 47):** Nar'l's tenure is one year, placed in 1491 DR (`adventure-wdh.json` line 32323; the wiki dates it 1491 DR)."
> — `campaign/setting/history/02-the-long-shadow.md:156`

**Wiki, Xanathar's Thieves' Guild page, the 1491 entry (wiki only; the page cites WDH-p211, 5e inferred)**
> "By {{Yearlink|1491}}, Zushaxx had taken [[Nar'l Xibrindas]], a [[Bregan D'aerthe]] spy, as its only advisor, choosing to eliminate all others.<ref name="WDH-p211"/>"
> — `sources/research/pass5-bundles/xanathars-guild/wiki.txt:155`

**Campaign, the beholder of 1491 is named Zushaxx (history page; the campaign uses "Xanathar" for the title)**
> "- 1491 DR: Zushaxx takes Nar'l as its only advisor."
> — `campaign/setting/history/02-the-long-shadow.md:136` (the line is a bullet inside a block quote)

### A4. Rank and role in the Guild

**Campaign, the Guild's structure (day-one)**
> "Ahmaergo, a shield dwarf, is the most influential member after the beholder, and Nar'l Xibrindas is its only advisor."
> — `campaign/setting/organizations/08-xanathars-guild.md:43` (the sentence sits in the Structure paragraph that begins "Xanathar rules the Guild from a lair below Skullport")

**Campaign, the Guild's Key Members entry (day-one)**
> "- **Nar'l Xibrindas** (DH p. 213) — Drow mage, neutral evil. Xanathar's advisor and secret Bregan D'aerthe asset. Nar'l reports to Jarlaxle by *Sending* spell and has been operating in place for one year, placed in 1491 DR. See the **Nar'l Xibrindas** page in Notable Figures."
> — `campaign/setting/organizations/08-xanathars-guild.md:102` (page citation conflict, see D3)

**Adventure, the underlings list (5e)**
> "{@creature Xanathar|WDH} relies on underlings for advice, information, and day-to-day oversight of the Xanathar Guild. The following important underlings are described in appendix B:"
> — `sources/adventure-wdh.json:15066` (list item at `:15072`: "{@creature Nar'l Xibrindas|wdh}, drow advisor,")

**Adventure, the Guild's Nar'l entry, the sending spell (5e)**
> "{@creature Nar'l Xibrindas|wdh} is a {@creature drow mage}. He prepares and casts the {@spell sending} spell whenever he needs to communicate with his brother."
> — `sources/adventure-wdh.json:32331` (the receiver in this line is his brother; `:15149` says "his drow brethren", see D11)

**Adventure, the lair's day-one staging (5e)**
> "{@creature Nar'l Xibrindas|wdh} has smuggled smokepowder into the lair (see {@area X36|2cb}) and, with {@creature Thorvin Twinbeard|wdh}'s help, identified areas that are structurally unstable."
> — `sources/adventure-wdh.json:15091` (the sentence sits in "Destroy the Lair", `:15087`, page 100)

**Campaign, the one drow in the lair (structure doc; rests on the Alexandrian Lair)**
> "*Inside Ally: Nar'l Xibrindas (X35).* The only drow in the lair, which Xanathar considers proof of its own cosmopolitan generosity. Nar'l's grell bodyguard carries a kill-on-disloyalty order from Xanathar, an instruction the grell will carry out without hesitation. Nar'l cannot dismiss it. He can only avoid triggering it."
> — `campaign/structure/arc-f-xanathars-lair.md:99`

**Alexandrian, Lair p.86 [img], the agent**
> **[img]** "Nar'l Xibrindas: N'arl is an agent of Bregan D'Aerthe, but his ability to directly assist Jarlaxle during the heist is limited due to the presence of the grell bodyguard Xanathar has placed on him. Jarlaxle would also prefer to keep him in situ as a valuable source of intel until the Grand Game has concluded."
> — `sources/11. Lair  Xanathar’s Lair.pdf`, printed p.86 [PDF p.4]

**Alexandrian, Lair p.87 [img], subtler help**
> **[img]** "However, once the distractions start causing turmoil, Nar'l might contribute to Jarlaxle's plan in subtler ways. (For example, by ordering key guards out of the way on plausible pretexts at the right moment.)"
> — `sources/11. Lair  Xanathar’s Lair.pdf`, printed p.87 [PDF p.5]

**Alexandrian, Appendix B, the Bregan D'aerthe renown (Alexandrian, not day-one)**
> "- **Protect Nar'l Xibrindas's cover within Xanathar's Guild (+1).** Jarlaxle's spy inside Xanathar's council is his most valuable single asset in Waterdeep."
> — `sources/Appendix_B_-_Player_Factions.md:781`

**Wiki, the Guild's Notable Members (wiki only; WDH-p211, 5e inferred)**
> "* [[Nar'l Xibrindas]]: [[drow]] [[wizard]] advisor<ref name="WDH-p211">{{Cite book/Waterdeep: Dragon Heist|211}}</ref>"
> — `sources/research/pass5-bundles/xanathars-guild/wiki.txt:114`

### A5. Relationship to Xanathar and the grell

**Adventure, the grell and the suspicion (5e)**
> "{@creature Xanathar|WDH} is aware that something is off with Nar'l, and recently assigned him a {@creature grell} bodyguard. The grell has instructions to dispose of Nar'l at the first sign of disloyalty."
> — `sources/adventure-wdh.json:32324`

**Campaign, Xanathar's suspicion (day-one)**
> "- Xanathar suspects Nar'l of disloyalty and has set a grell to kill him at the first proof. It does not know he reports to Bregan D'aerthe or to Jarlaxle."
> — `campaign/setting/villains/xanathar.md:56`

**Campaign, Persona (day-one)**
> "Deep down, Xanathar suspects a mole and has assigned Nar'l a grell bodyguard with orders to kill him at the first sign of disloyalty."
> — `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:21`

**Wiki, the 1492 worry (wiki only; WDH5e-p211)**
> "In [[1492 DR]],{{WDH-time}} however, Nar'l was worried about the growing paranoia of the beholder, who'd started to suspect something about the drow.<ref name="WDH5e-p211" />"
> — `Nar_l_Xibrindas.txt:72`

**Alexandrian, Lair p.91 [img], the crypt and the double-agent fear**
> **[img]** "N'arl Xibrindas knows more than most. He's even snuck into the Crypt of Xanathars Past (X33). But he'll also suspect that anyone questioning him is actually an agent of Xanathar trying to reveal him as a double agent."
> — `sources/11. Lair  Xanathar’s Lair.pdf`, printed p.91 [PDF p.9]

**Campaign, the Guild's "Knowledge Is Removed" belief (day-one)**
> "Nar'l's advice that Xanathar should eliminate its other advisors fits this habit (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/08-xanathars-guild.md:31`

### A6. Temperament and manner

**Adventure (5e)**
> "The beholder's paranoia will eventually cause {@creature Xanathar|WDH} to question the drow's loyalty, though, and Nar'l has become increasingly worried about his future."
> — `sources/adventure-wdh.json:32323`

**Wiki (wiki only; WDH5e-p211)**
> "Nar'l was a nervous individual. He always chose his personal safety over that of his allies. He had with him a secret poison to blind the Xanathar.<ref name="WDH5e-p211" />"
> — `Nar_l_Xibrindas.txt:75`

**Campaign, the loyalty line (day-one)**
> "- **Nar'l Xibrindas** is Xanathar's trusted drow advisor and secretly Jarlaxle's best intelligence source on the Guild. He reports by *Sending* spell, and if forced to choose between himself and Bregan D'aerthe, he will choose himself (the **Nar'l Xibrindas** page)."
> — `campaign/setting/villains/jarlaxle.md:58`

**Adventure, the eyescratch vial (5e)**
> "In addition to his other gear, Nar'l carries a vial containing three doses of {@item eyescratch|WDH}, a contact poison. A creature that comes into contact with the poison must succeed on a {@dc 14} Constitution saving throw or be {@condition poisoned} for 1 hour and {@condition blinded} while {@condition poisoned} in this way. A lesser restoration spell or similar magic ends the effect."
> — `sources/adventure-wdh.json:32332`

### A7. Belongings, office and the smokepowder cache

**Adventure, the office (5e; the room is inside the lair)**
> "X35. Nar'l Xibrindas's Office"
> — `sources/adventure-wdh.json:18096` (page 113)

**Adventure, the drawers (5e)**
> "The first drawer holds Nar'l's spellbook, a sturdy tome bound in black leather and wrapped in webbing. It contains all the spells that Nar'l has prepared, plus the {@spell sending} spell."
> — `sources/adventure-wdh.json:18125`

> "The second drawer contains a {@item bag of holding} that belongs to {@creature Jarlaxle Baenre|WDH}. Nar'l borrowed this magic item and used it to smuggle kegs of {@item smokepowder|WDH} into {@creature Xanathar|WDH}'s lair (see {@area X36|2cb})."
> — `sources/adventure-wdh.json:18126`

**Adventure, the secret room (5e; the room Nar'l found)**
> "Neither {@creature Xanathar|WDH} nor its loyal underlings know this room exists. When Nar'l found it, he asked to have the adjoining room ({@area X35|2c7}) turned into his office so that he could keep this room secret. The only other individual who knows about this room is {@creature Thorvin Twinbeard|wdh}, {@creature Xanathar|WDH}'s chief engineer, but he's not inclined to tell the beholder about it."
> — `sources/adventure-wdh.json:18165` (room "X36. Secret Room", header at `:18143`; the kegs are at `:18162`: "Twenty kegs of smokepowder are neatly stacked in the middle of the room.")

**Campaign, the office (Lair key; day-one room, quest-scene use)**
> "**X35 — Nar'l's Office.** Sparse and organized by a mind that trusts nothing to memory when paper will do. The desk holds Guild operational reports and a coded communication log in Jarlaxle's cipher (DC 16 Intelligence to decode without the key)."
> — `campaign/structure/arc-f-xanathars-lair.md:169` (the same entry continues with the Seven Masks report and "Nar'l has kept this from Xanathar for eleven months.", see D4)

**Alexandrian, Lair p.88 [img], the office desk**
> **[img]** "X35 – Nar'l Xibrindas' Office: In addition the normal entry for this room, the desk contains a *Report on the Seven Masks Theater*."
> — `sources/11. Lair  Xanathar’s Lair.pdf`, printed p.88 [PDF p.6]

**Campaign, the smokepowder cache (day-one; "eight kegs, four months" conflicts with the adventure, see D8)**
> "*The Smokepowder Option.* Nar'l smuggled eight smokepowder kegs into a concealed cache in Area X36 over four months. Thorvin's structural schematic identifies five load-bearing junctions that, struck simultaneously, trigger a controlled collapse of the lair's central chambers within one hour."
> — `campaign/structure/arc-f-xanathars-lair.md:107`

**Campaign, Thorvin's knowledge of the cache (day-one)**
> "To those who earn his trust, he has been a Harper informant for three years, knows exactly where Nar'l Xibrindas hid the smokepowder, and will tell the party where to place it for maximum effect before he flees up the cellar stairs."
> — `campaign/setting/notable-figures/xanathars-guild/07-thorvin-twinbeard.md:21`

### A8. Faith

No source gives Nar'l a deity, a shrine or a rite. The page has no Lolth line and the voice profile has none. The Lolth lines near the Nar'l material are the adventure's Soluun entry (D16) and Jarlaxle's letter in Appendix C (D17).

### A9. Affiliation and allegiance (GM-only fact)

**Campaign, Bregan D'aerthe's side (day-one)**
> "- **Xanathar's Guild (rival):** Nar'l Xibrindas advises the beholder and reports to Jarlaxle, and Jarlaxle prefers a manageable Xanathar to a dead one (**Jarlaxle Baenre**; **The Grand Game in Play**)."
> — `campaign/setting/organizations/07-bregan-daerthe.md:90`

**Campaign, the Bregan D'aerthe list (day-one)**
> "- **Keep an Asset Inside Every Rival:** The company is skilled at infiltrating criminal organizations, and Nar'l Xibrindas advises Xanathar while he reports to Jarlaxle by *Sending* spell."
> — `campaign/setting/organizations/07-bregan-daerthe.md:38`

**Campaign, the Villains page (day-one)**
> "| Nar'l Xibrindas | Advisor | Trusted as a drow voice on Guild matters; actually a Bregan D'aerthe spy; discovery ends Nar'l immediately |"
> — `campaign/setting/villains/xanathar.md:48`

**Campaign, Jarlaxle's view (day-one)**
> "- He reached Waterdeep already knowing of the Stone, the three Eyes and the vault, and Nar'l's reports keep him current. The nimblewright ledger puts him in the city no later than Marpenoth 3, 1491 DR (**Bregan D'aerthe's Long Road**)."
> — `campaign/setting/villains/jarlaxle.md:55`

**Campaign, Jarlaxle's hidden contingency (research tag in the source)**
> "| Nar'l Xibrindas | Embedded spy | Inside Xanathar's Guild; Jarlaxle's most valuable asset; Jarlaxle has a contingency if Nar'l is discovered (has not shared it with Nar'l) `[research]` |"
> — `campaign/setting/villains/jarlaxle.md:105`

**Campaign, the Guild's view of Jarlaxle (day-one)**
> "- **Bregan D'aerthe** (rival, unaware): Nar'l Xibrindas advises Xanathar and reports to Jarlaxle by *Sending* spell, and Bregan D'aerthe buys equipment through Grinda Garloth. Xanathar suspects a mole and is hunting in the wrong direction (**Running the Villains**; **Nar'l Xibrindas**)."
> — `campaign/setting/organizations/08-xanathars-guild.md:91`

### A10. Renown and rank

No day-one rank for Nar'l. Campaign: "- At Renown 3+: Nar'l Xibrindas's intelligence on Xanathar's movement patterns is available once per tenday — response timing and surface contacts, not the lair layout. The distinction is deliberate."
> — `campaign/guides/factions/08-bregan-daerthe.md:15`

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Page, Gamemaster's Summary: "- *Drow mage, neutral evil, he/him*. Stat block: **Mage**." — `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:5`
- Guild page: "- **Nar'l Xibrindas** (DH p. 213) — Drow mage, neutral evil." — `campaign/setting/organizations/08-xanathars-guild.md:102`
- Wiki infobox: "| alignment5e    = " (blank) — `Nar_l_Xibrindas.txt:57`
- Adventure entry `sources/adventure-wdh.json:32309`-`:32335`: the entry gives no alignment (checked by reading the whole entry).
- Alexandrian: no alignment line for Nar'l found in Lair pp.83-91 or Outposts pp.36-48.
- Result: "neutral evil" is sourced in the campaign only (Guild page, line 102). The page's line 5 matches it.

**Species**
- Page: "Drow mage" (`03-narl-xibrindas.md:5`).
- Adventure: "a nervous and conniving male drow named" (`sources/adventure-wdh.json:32323`).
- Wiki: "| race           = [[Drow]]" (`Nar_l_Xibrindas.txt:14`).
- Guild page: "Drow mage" (`08-xanathars-guild.md:102`).

**Pronouns**
- Page: "he/him" (`03-narl-xibrindas.md:5`).
- Adventure: "a nervous and conniving male drow" (`sources/adventure-wdh.json:32323`); the entry uses "his" and "he" (`:32323`, `:32324`, `:32331`).
- Wiki: "| sex            = Male" (`Nar_l_Xibrindas.txt:13`).
- Appendix C: "He sets down his stylus." (`sources/Appendix_C_-_Player_Faction_Missions.md:1628`).
- Alexandrian Lair p.91 [img]: "He's even snuck into the Crypt of Xanathars Past (X33)." (`sources/11. Lair  Xanathar’s Lair.pdf`, printed p.91 [PDF p.9]).

**Stat block label (conflict, see D2)**
- Page: "Stat block: **Mage**." (`03-narl-xibrindas.md:5`)
- Adventure: "{@creature Nar'l Xibrindas|wdh} is a {@creature drow mage}." (`sources/adventure-wdh.json:32331`)
- Alexandrian Lair p.91 [img]: "N'arl Xibrindas – drow mage, MM p. 129 (DH p. 211)" (`sources/11. Lair  Xanathar’s Lair.pdf`, printed p.91 [PDF p.9])
- Alexandrian Appendix C: "**Nar'l Xibrindas** (**Drow Mage**, *Dragon Heist* appendix B)." (`sources/Appendix_C_-_Player_Faction_Missions.md:1632`)
- Wiki: "| class5e        = [[Mage]]" (`Nar_l_Xibrindas.txt:59`), citation "WDH5e-p211" at `:60`.
- Docs note, not campaign (see E2): "the 2024 Mage has no Sending (swapped in by M4)" (`docs/plans/harpers-out-of-scope-notes.md:497`).

**Page citation (conflict, see D3)**
- Guild page: "(DH p. 213)" (`08-xanathars-guild.md:102`).
- Adventure: `"page": 211` (`sources/adventure-wdh.json:32310`).
- Wiki: "{{Cite book/Waterdeep: Dragon Heist|211}}" (`sources/research/pass5-bundles/xanathars-guild/wiki.txt:114`).
- Alexandrian Lair p.91 [img]: "DH p. 211" (`sources/11. Lair  Xanathar’s Lair.pdf`, printed p.91).

**Pronunciation (adventure, 5e)**: "NAR-ul zeh-BRIN-das" (`sources/adventure-wdh.json:250`).

**Lolth check**
- Page: no mention of Lolth or any deity (`03-narl-xibrindas.md`, whole file).
- Voice profile: no mention of Lolth (`.claude/skills/character-voices/voices/xanathars-guild.md:47`-`:61`).
- Lolth page: "Nar'l Xibrindas, the drow advisor in Xanathar's Guild, has no Lolth line either." (`campaign/setting/deities/lolth.md:143`).
- No Lolth-devotion line for Nar'l. Two Lolth lines in the Nar'l-adjacent material are flagged for the orchestrator (D16, D17).

---

## C. Quest-time sentences on the current page, and voice-profile quest-time clauses

The page body (lines 11 to 29) narrates no quest event. All of it is day-one (see the table). The only quest-time material on the page is the Featured-in list (line 7).

| Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|
| L5 | "- *Drow mage, neutral evil, he/him*. Stat block: **Mage**." | Day-one; the label conflicts (B, D2) | `08-xanathars-guild.md:102`; `sources/adventure-wdh.json:32331` |
| L6 | "- **Affiliation:** Xanathar's Guild (secretly Bregan D'aerthe)" | Day-one GM-only secret (Gamemaster's Summary) | `08-xanathars-guild.md:102`; `07-bregan-daerthe.md:90` |
| L7 | "**Featured in:** **Faction Outposts**, **Xanathar's Lair**, **Sea Maidens Faire**, **The Wazoo Affair**, **The Betrayal Pitch**, **The Compromised Eye**, **The Dive**, **Doom Raiders Mission 1 — The Dockside Killer**, **Force Grey Mission 4 — Destroy the Intellect Factory**" | Quest references. Four entries are stale or not Nar'l's (see the list below) | See the Featured-in list below |
| L11 | "**Resonance.** Nar'l should inspire sympathy with his escalating fear of discovery, fascination with the impossible position he occupies between two hostile factions, and contempt from his own brother Soluun." | Day-one | `sources/adventure-wdh.json:32040` (Soluun's contempt); `:32324` (the grell and the suspicion) |
| L13 | "**Emotions.** Nar'l most often feels nervous calculation, growing paranoia, practiced competence masking terror, contempt for Xanathar's delusions, desperate self-preservation, and bitter awareness that Jarlaxle would sacrifice him without hesitation if the cost were right." | Day-one state for the fear and self-preservation. The Jarlaxle clause has a quest-scene source: "Jarlaxle decided it was simpler to eliminate him than to extract him." | `sources/adventure-wdh.json:32323`; `sources/Appendix_C_-_Player_Faction_Missions.md:1634` (quest-time) |
| L15 | "**Motivations.** Nar'l wants to survive his assignment as Jarlaxle's intelligence asset inside Xanathar's Guild, avoid Xanathar's suspicion (which is growing), and keep his options open in case he needs to betray Bregan D'aerthe to save himself." | Day-one | `campaign/setting/history/02-the-long-shadow.md:72`; `sources/adventure-wdh.json:32323` |
| L17 | "**Inspirations.** When playing Nar'l, channel Severus Snape (*Harry Potter*), Gus Fring (*Breaking Bad*), and Donnie Brasco (*Donnie Brasco*)." | Not a fact | n/a |
| L21 | "**Persona.** To the world, Nar'l is Xanathar's trusted drow advisor who convinced the beholder to eliminate its other counselors. To Jarlaxle, he is Bregan D'aerthe's best intelligence source on Guild movements, reporting via Sending spell after one year in place, placed in 1491 DR. Deep down, Xanathar suspects a mole and has assigned Nar'l a grell bodyguard with orders to kill him at the first sign of disloyalty. If forced to choose between himself and Bregan D'aerthe, he will choose himself." | Day-one | `sources/adventure-wdh.json:32323`, `:32324`; `campaign/setting/organizations/08-xanathars-guild.md:23` |
| L23 | "**Morale.** In a fight, Nar'l would use magic to misdirect and escape. He carries three doses of contact poison (eyescratch, DC 14 Con or blinded/poisoned) and will use it on anyone, including allies, if it means survival." | Day-one for the vial and the DC. No source says "including allies"; the adventure says the vial goes to Bregan D'aerthe members who are recognised (quest-time) | `sources/adventure-wdh.json:32332`; `:17585` (quest-time, see E4) |
| L25 | "**Relationships.** Nar'l is the younger brother of Soluun Xibrindas (who considers him a weakling), Jarlaxle's intelligence asset inside Xanathar's Guild, and Xanathar's only advisor, who has a grell bodyguard assigned to execute him at the first sign of treachery." | Day-one | `sources/adventure-wdh.json:32040`, `:32323`, `:32324`; `campaign/setting/organizations/08-xanathars-guild.md:43` |
| L29 | "Nar'l Xibrindas is a drow mage serving as Xanathar's only advisor, presenting himself as a trusted counselor who has the beholder's ear. He is precise, controlled, and carefully unremarkable." | Day-one; public face. No secret allegiance shown | `sources/adventure-wdh.json:32323` |

**Featured-in list (line 7), item by item**
- **Faction Outposts**: supported. `campaign/structure/arc-e-faction-outposts.md:185`: "*Intel Yield.* Nar'l's correspondence is the primary entry path to Xanathar's Lair via the guildsign trail." Also `:165`, `:183`, `:351`, `:491`.
- **Xanathar's Lair**: supported. `campaign/structure/arc-f-xanathars-lair.md:17`, `:43`, `:107`, `:169`, `:184`, `:198`.
- **Sea Maidens Faire**: supported. `campaign/structure/arc-h-sea-maidens-faire.md:15`: "...the same network that had placed Nar'l Xibrindas inside Xanathar's Guild a year earlier, in 1491." (the sentence begins "The Eye had reached him the night before Ches 1, through Bregan D'aerthe intelligence work — ")
- **The Wazoo Affair**: stale. `campaign/quests/faction-events/bregan-daerthe/m02-the-wazoo-affair/design-notes.md:35`: "`campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md` line 8 lists **The Wazoo Affair** under Nar'l's \"Featured in\". Nar'l no longer appears here."
- **The Betrayal Pitch**: the mission is cut. `m02-the-wazoo-affair/design-notes.md:39`: "- **Kreb Drops the Cover** and **Contact Severed** no longer read the cut Betrayal Pitch, and **Kreb Drops the Cover** reads **Wazoo Exposé Published**." And `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/design-notes.md:40`: "still lists **The Betrayal Pitch** under \"Featured in\", although the mission is cut."
- **The Compromised Eye**: supported. `campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/overview.md:17`.
- **The Dive**: supported. `campaign/quests/faction-events/bregan-daerthe/m06-the-dive/overview.md:26`: "- Otherwise, if **Nar'l Active** or **Nar'l Cleared** is marked and **Soluun Killed** is marked, Nar'l Xibrindas leaked it in grief. He wanted standing with Ahmaergo and wanted to hurt the captain who didn't avenge his brother."
- **Doom Raiders Mission 1 — The Dockside Killer**: no Nar'l. The mission names Soluun only. `campaign/quests/faction-events/doom-raiders/m01-the-dockside-killer/overview.md:53`: "- **Soluun Xibrindas** (Bregan D'aerthe): the killer, a drow gunslinger who hunts elf and half-elf sailors."
- **Force Grey Mission 4 — Destroy the Intellect Factory**: no Nar'l. `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/overview.md:27`: "The default captive is Zaibon Kyszalt, a drow of House Auvryndar. If **Soluun Expelled** is marked, Soluun Xibrindas sits in the chair instead." (the rest of the line covers the Guild's seizure of Soluun and the Force Grey agent inside the Guild)

**Voice profile quest-time clauses** (`.claude/skills/character-voices/voices/xanathars-guild.md`, Nar'l section lines 47 to 61; the profile has no Lolth line)
- Line 53, Swearing: "*Stingy · Plain · Clipped.* Only alone, or with someone he's bargaining for his life with: a tight, frightened \"fuck\"." The phrase "bargaining for his life" matches the Compromised Eye trade (see below). The Swearing line stays (ruling 16).
- Line 60, Sample (Business, privately): "\"I can tell you where the smokepowder is. What I need is a way out of this city that no one is watching. What would you offer?\"" The offer and the extraction ask match the Compromised Eye trade. Compare `sources/Appendix_C_-_Player_Faction_Missions.md:1632` ("He is offering to trade: the location of Xanathar's Eye (Area X19, in Sylgar's fishbowl) and the specific bypass through Area X18 that allows access without triggering the Panopticus network, in exchange for his life and extraction from the lair.") and `campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/overview.md:40`.
- Line 61, Sample (Under pressure): "\"Wait. Wait. I'm more useful alive, to you and to anyone else. Let's be sensible.\"" A captured-state line. Day-one only if read as a general pressure line. Judgment for the drafter.
- Lines 52 and 54 use "the Xanathar" (Word choice; Personality in speech). Rule 9 says Xanathar is "it" in narration. These lines are profile narration, not speech tags. Flagged, not changed.

**Quest-time material in other sources that the page must not restate** (routed; see E4)
- Compromised Eye (`campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/overview.md:17`, `:40`, `:58`, `:73`, `:79`, `:84`; `ev-01-the-compromised-eye.md:46`, `:47`; `ev-02-twelve-minutes.md:274`, `:413`-`:415`).
- Alexandrian Arc BD-4 (`sources/Appendix_C_-_Player_Faction_Missions.md:1600`, `:1632`, `:1634`, `:1638`).
- Jarlaxle's compromise order (`sources/Appendix_B_-_Player_Factions.md:815`).
- Adventure's traitor mission (`sources/adventure-wdh.json:3634`) and the Jarlaxle suspicion (`:7153`).

---

## D. Conflicts

**D1. Sponsor: House Xorlarrin against Bregan D'aerthe (the orchestrator's main call)**
- Index: "- Internal politics the PCs can exploit: Nar'l Xibrindas (drow spy working against Xanathar for House Xorlarrin), Noska vs. Ahmaergo rivalry, the Sylgar distraction (Xanathar's goldfish — stealing or threatening it causes Xanathar to abandon tactical thinking)" — `sources/SOURCE_GUIDE.md:343` (entry header "### `11. Lair  Xanathar's Lair.pdf`" at `:335`).
- The Lair PDF that the index describes: **[img]** "N'arl is an agent of Bregan D'Aerthe" (printed p.86 [PDF p.4]). None of the nine pages read names House Xorlarrin.
- Adventure: "is actually a Bregan D'aerthe spy" (`sources/adventure-wdh.json:1301`) and "Jarlaxle has a spy in the Xanathar Guild" (`:15149`). The adventure has no "Xorlarrin" anywhere.
- Campaign: "Nar'l Xibrindas is Xanathar's trusted drow advisor and secretly Jarlaxle's best intelligence source on the Guild." (`campaign/setting/villains/jarlaxle.md:58`).
- The only "Xorlarrin" line in the searched sources links House Xorlarrin to Bregan D'aerthe in 1360 DR, with nothing about Nar'l: "Circa [[1360 DR]], [[House Xorlarrin]] hired Bregan D'aerthe to help protect the [[Lustrum]] mines.<ref name="DDGttU-p67-68">{{Cite book/Drizzt Do'Urden's Guide to the Underdark|67-68}}</ref>" (`sources/research/pass5-bundles/bregan-daerthe/wiki.txt:82`; the same line at `sources/research/pass4-bundles/jarlaxle/wiki.txt:381`). The citation is to *Drizzt Do'Urden's Guide to the Underdark*, whose edition is not printed on the line (older edition, inferred `[research]`).
- Higher source: the adventure, the Alexandrian Lair PDF and the campaign all say Bregan D'aerthe. The SOURCE_GUIDE line is a summary and does not match the PDF it describes. No searched source supports House Xorlarrin.

**D2. Stat block label: "Mage" against "drow mage"**
- Page: "Stat block: **Mage**." (`03-narl-xibrindas.md:5`)
- Adventure: "is a {@creature drow mage}" (`sources/adventure-wdh.json:32331`)
- Alexandrian Lair p.91 [img]: "N'arl Xibrindas – drow mage, MM p. 129 (DH p. 211)"
- Appendix C: "**Drow Mage**" (`sources/Appendix_C_-_Player_Faction_Missions.md:1632`)
- Wiki: "| class5e        = [[Mage]]" (`Nar_l_Xibrindas.txt:59`)
- Higher source: the adventure ("drow mage", 5e). No searched source gives the 2024 stat-block name for Nar'l. The orchestrator decides.

**D3. Page citation: "DH p. 213" against "page 211"**
- Guild page: "- **Nar'l Xibrindas** (DH p. 213) — Drow mage, neutral evil." (`campaign/setting/organizations/08-xanathars-guild.md:102`). The same page cites DH p. 213 for Nihiloor (line 103) and Noska (line 104).
- Adventure: `"page": 211` at `sources/adventure-wdh.json:32310`.
- Wiki: WDH-p211 (`sources/research/pass5-bundles/xanathars-guild/wiki.txt:114`).
- Alexandrian Lair p.91 [img]: "(DH p. 211)".
- Higher source: the adventure and the Alexandrian Lair both give 211.

**D4. Tenure: one year against "eleven months"**
- Current: "reporting via Sending spell after one year in place, placed in 1491 DR." (`03-narl-xibrindas.md:21`). The Lair structure doc (`campaign/structure/arc-f-xanathars-lair.md:17`): "Jarlaxle placed Nar'l Xibrindas in the Guild in 1491 and has relied on him as a double agent for the year since."
- Adventure: "A year ago, Nar'l was given the difficult task" (`sources/adventure-wdh.json:32323`).
- Conflict: "Nar'l has kept this from Xanathar for eleven months." (`campaign/structure/arc-f-xanathars-lair.md:169`). This is still in the Lair structure doc and is not fixed.
- The campaign's own note: "Nar'l's tenure also differed by source: one year in the published adventure, now also in `03-narl.md` line 21 and the Guild organization page (line 23), placed in 1491 DR, and eleven years or months in `arc-f` lines 17 and 169." (`campaign/setting/villains/xanathar.md:106`). Line 17 of `arc-f` has since been corrected (see above).
- Higher source: the adventure, the wiki and the Settled ruling (`campaign/setting/history/02-the-long-shadow.md:156`) all give one year, placed 1491 DR. `arc-f:169` is the outlier.

**D5. Jarlaxle's view of Nar'l's loyalty (quest-time suspicion in the adventure against the campaign's day-one reliance)**
- Adventure, traitor mission (quest-time): "Jarlaxle identifies the traitor as a drow mage named {@creature Nar'l Xibrindas|wdh} (see {@adventure appendix B|WDH|12}) and furnishes the characters with a route to {@creature Xanathar|WDH}'s lair through underground passageways." (`sources/adventure-wdh.json:3634`)
- Adventure, quest-time: "Jarlaxle suspects that {@creature Nar'l Xibrindas|wdh}, his spy in the Xanathar Guild, has betrayed him and is now using the resources of Bregan D'aerthe to help the beholder retrieve the stone." (`sources/adventure-wdh.json:7153`)
- Wiki, the 1492 state (wiki only; WDH5e-p64): "[[Jarlaxle]] too believed that Nar'l was double-crossing Bregan D'aerthe and was willingly working with the beholder." (`Nar_l_Xibrindas.txt:72`)
- Campaign, day-one: "Nar'l reports to Jarlaxle by *Sending* spell." (`campaign/setting/organizations/08-xanathars-guild.md:102`) and "Nar'l's reports keep him current." (`campaign/setting/villains/jarlaxle.md:55`). The campaign's Jarlaxle page does not say he doubts Nar'l on Ches 1.
- Campaign, quest-time: the Compromised Eye (`campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/overview.md:17`).
- Higher source: the campaign. The adventure's suspicion sits in quest-time mission text (`:3634`, `:7153`).

**D6. Compromise: "forbids killing" against "eliminate"**
- Factions Guide, Compromised Eye row: "| 5th | **The Compromised Eye** | Extract or protect Nar'l Xibrindas, the BD mole embedded in Xanathar's Guild. Jarlaxle forbids killing him — Nar'l is more valuable alive and in position. Three approaches: feed him a false report, extract him from the city, or confront Ahmaergo's counterintelligence source. | +3 |" (`campaign/guides/factions/08-bregan-daerthe.md:69`)
- Alexandrian Appendix B: "| 5th | **The Compromised Spy** | Nar'l Xibrindas — Jarlaxle's agent embedded in Xanathar's council — has been compromised. Eliminate him before Xanathar does, to prevent him from being tortured into revealing D'aerthe's operations. Jarlaxle furnishes a route directly into the beholder's lair. | +2 |" (`sources/Appendix_B_-_Player_Factions.md:815`)
- Alexandrian Appendix C: "Jarlaxle sends the party to eliminate Nar'l Xibrindas, his own agent inside Xanathar's Guild." (`sources/Appendix_C_-_Player_Faction_Missions.md:1600`)
- Campaign quest journal: "A party that surrenders Nar'l has marked **Nar'l Eliminated**, because the grell kills him in front of it." (`campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/ev-02-twelve-minutes.md:274`) and "Mark **Nar'l Eliminated** and use the debrief scene in **Twelve Minutes**." (`ev-01-the-compromised-eye.md:47`)
- Higher source: the campaign. The Factions Guide row says Jarlaxle forbids killing him, and the campaign quest journal has a Nar'l Eliminated outcome. These conflict inside the campaign. The orchestrator decides.

**D7. Featured-in list (line 7) against the quest files**
- Stale: The Wazoo Affair (`m02-the-wazoo-affair/design-notes.md:35`). Cut: The Betrayal Pitch (`m02-the-wazoo-affair/design-notes.md:39`; `s02-kreb-drops-the-cover/design-notes.md:40`). Soluun only: The Dockside Killer (`doom-raiders/m01-the-dockside-killer/overview.md:53`) and Force Grey M4 (`force-grey/m04-destroy-the-intellect-factory/overview.md:27`, `:69`).
- Higher source: the quest files and their design notes. Four of the nine Featured-in entries are not supported for Nar'l.

**D8. Smokepowder: "twenty kegs" against "eight kegs over four months"**
- Adventure: "Twenty kegs of smokepowder are neatly stacked in the middle of the room." (`sources/adventure-wdh.json:18162`, the room is X36)
- Campaign: "Nar'l smuggled eight smokepowder kegs into a concealed cache in Area X36 over four months." (`campaign/structure/arc-f-xanathars-lair.md:107`)
- Alexandrian: the Lair PDF (all nine pages read) gives no keg count. The Outposts letter says "the smokepowder" only (**[img]** `sources/5. Faction Outposts.pdf`, printed p.45 [PDF p.10]).
- Higher source: the campaign (`arc-f:107`) is the Lair structure doc and the authority until the Lair journal exists. The adventure is the published count. The orchestrator decides.

**D9. Where he stands: X35 office against X18 audience chamber**
- Campaign: "Nar'l is in X35 unless pre-arranged otherwise, with grell bodyguard." (`campaign/structure/arc-f-xanathars-lair.md:184`).
- Alexandrian Lair p.89 [img], standard roster: "Area X35 – Nar'l's Office" (`sources/11. Lair  Xanathar’s Lair.pdf`, printed p.89 [PDF p.7]). Random encounter, printed p.89: "3 N'arl Xibrindas + Grell bodyguard". Tournament crowd, printed p.90 [PDF p.8]: "Nar'l Xibrindas (01-50%)".
- Adventure, during the speech: "{@creature Xanathar|WDH}'s treacherous {@creature drow mage} advisor, {@creature Nar'l Xibrindas|wdh} (see {@adventure appendix B|WDH|12}), stands in front of the open door to {@area X19|29c}, clapping weakly at the speech." (`sources/adventure-wdh.json:17583`, room "X18. Audience Chamber" at `:17568`). Then `:17584`: "If {@creature Xanathar|WDH} is elsewhere, this room contains only Nar'l and the grell."; he "retreats to {@area X35|2c7}".
- Wiki: "Usually Nar'l was in the audience chamber inside the Xanathar's lair." (`Nar_l_Xibrindas.txt:65`)
- Not a flat conflict: the adventure places him in X18 during the speech and in X35 when retreating. The wiki gives X18 as his usual post. The campaign gives X35.

**D10. Crypt and cache knowledge: who knows which room**
- Campaign: "Nar'l Xibrindas is the only current Guild member who knows this room exists." (`campaign/structure/arc-f-xanathars-lair.md:167`, room X33)
- Campaign, the crypt line: "The crypt of previous Xanathars (area X33 of **Xanathar's Lair**) shows that the title is claimed through murder. Of the Guild's own people, only Nar'l knows the room exists." (`campaign/setting/history/02-the-long-shadow.md:82`); "Settled by the user (Session 47): Who knows the crypt." (`history/02-the-long-shadow.md:157`)
- Adventure, a different room (X36, the cache): "The only other individual who knows about this room is {@creature Thorvin Twinbeard|wdh}" (`sources/adventure-wdh.json:18165`).
- Adventure, the crypt X33: "{@creature Xanathar|WDH} (see {@adventure appendix B|WDH|12}), if present, is gazing somberly at the tombs of past Xanathars." (`sources/adventure-wdh.json:18027`); X33 header at `:18014`.
- Alexandrian Lair p.91 [img]: "Xanathar doesn't allow anyone to enter the Area X33 and most don't even know what's in there, but some know that there's a secret door connecting the Arena (X6) and \"whatever Xanathar has hidden down there\"."
- Higher source: the user's Session 47 ruling (`history/02-the-long-shadow.md:157`) and the remix's Xanathar note (`campaign/setting/villains/xanathar.md:102`) override the published X33 entry.

**D11. Whom he reports to: Jarlaxle against Soluun and "drow brethren"**
- Adventure, the Nar'l entry: "He prepares and casts the {@spell sending} spell whenever he needs to communicate with his brother." (`sources/adventure-wdh.json:32331`)
- Adventure, the lair-chapter sentence: "uses {@spell sending} spells to transmit intelligence to his drow brethren" (`:15149`)
- Campaign: "Nar'l reports to Jarlaxle by *Sending* spell." (`campaign/setting/organizations/08-xanathars-guild.md:102`)
- Higher source: the campaign (Jarlaxle). The adventure's two lines do not name Jarlaxle as the receiver in the Nar'l entry.

**D12. Spell list: "Sending" against the Mage stat block**
- Adventure: the spellbook "contains all the spells that Nar'l has prepared, plus the {@spell sending} spell." (`sources/adventure-wdh.json:18125`)
- Docs note: "the 2024 Mage has no Sending (swapped in by M4)" (`docs/plans/harpers-out-of-scope-notes.md:497`).
- Quest: "Nar'l fights only when cornered or attacked, and then he uses *Shield*, *Misty Step*, *Invisibility* and the eyescratch in his vial." (`campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/ev-02-twelve-minutes.md:84`)
- Not settled by any source searched. The 2024 Mage list is not in the sources. The orchestrator decides.

**D13. Spelling of the name**
- "N'arl" appears in the Alexandrian PDFs (`sources/11. Lair  Xanathar’s Lair.pdf`, printed pp.86, 91 [img]; `sources/5. Faction Outposts.pdf` printed p.45 [PDF p.10] [img]; `sources/17. Outpost and Lair Revelation Lists.pdf` printed p.123 [PDF p.3] [img]) and in `sources/Appendix_D_-_Running_the_Tavern.md:205`. The campaign and adventure use "Nar'l". Spelling only.

**D14. Appendix D names him as the dispatcher of a replacement**
- "If the characters discover his affiliation and dismiss him, N'arl Xibrindas dispatches a replacement within three tendays — this time not applying for a bar position." (`sources/Appendix_D_-_Running_the_Tavern.md:205`; the candidate is "Candidate 5 — Tobrin Ashvale" at `:190`).
- The campaign names Tobrin as a Guild plant with no Nar'l link: "Grevik Nass and Tobrin Ashvale are the Guild's two plants among the staff of Trollskull Manor." (`campaign/setting/organizations/08-xanathars-guild.md:196`, Draft Notes, routed).

**D15. The Guild's ranks and Nar'l**
- Campaign: "The published ranks for members, from lowest to highest, are Eyestalker, Agent of the Eye, Eye Ray, Guild Boss and Hand of the Eye (*Dragon Heist*, 5e)." (`campaign/setting/organizations/08-xanathars-guild.md:45`). Nar'l is not placed on it. Alexandrian Appendix B: "Jarlaxle's spy inside Xanathar's council" (`sources/Appendix_B_-_Player_Factions.md:781`). No rank is given for Nar'l in any source.

**D16. Soluun's shrine to Lolth in the adventure (flagged under the Lolth rule; Soluun, not Nar'l)**
- Adventure: "If he has not been encountered and disposed of elsewhere, a {@creature drow gunslinger|WDH} named {@creature Soluun Xibrindas|wdh} (see {@adventure appendix B|WDH|12}) is here, worshiping before a shrine of Lolth. His stateroom has the following features:" (`sources/adventure-wdh.json:26345`).
- Campaign: "He despises Lolth and the matron houses that serve her, as the whole band does" (`campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:21`, quoted in `campaign/setting/deities/lolth.md:76`).
- Brief ruling 8: "Bregan D'aerthe rejects Lolth. No member worships her or invokes her with devotion."

**D17. Lolth in the Nar'l-adjacent quest text (flagged, not in the page or the profile)**
- Alexandrian Arc BD-4, Jarlaxle's letter: "We have a spy deep within Xanathar's organization, but I fear he has been compromised. It breaks my heart to do this, but I am sending you to eliminate him. Make it quick and painless, and for Lolth's sake, be discreet. I will give you a route." (`sources/Appendix_C_-_Player_Faction_Missions.md:1610`). "for Lolth's sake" is a phrase in the faction leader's letter. The orchestrator decides whether it breaks the rule.

**D18. The sewer route and the red eyes**
- Alexandrian: "...through a passage marked with red eyes at the junctions (Nar'l's old guildsign, still partially intact), and surfaces in Area X1" (`sources/Appendix_C_-_Player_Faction_Missions.md:1618`).
- Campaign: "Nar'l's guildsigns lead toward Area X1 of Xanathar's Lair; the trail requires DC 15 checks, rising to DC 17 near the lair itself." (`campaign/guides/factions/09-xanathars-guild.md:59`). Consistent. Quest-time, routed.

---

## E. Stale lines in other files (not edited), and routed references

### E1. Stale in campaign files
- `campaign/setting/villains/xanathar.md:106`: "> - **Conflicts:** The table calls Nar'l \"Trusted\" and the notes say Xanathar suspects him and has set a grell to kill him at the first proof. Nar'l's tenure also differed by source: one year in the published adventure, now also in `03-narl.md` line 21 and the Guild organization page (line 23), placed in 1491 DR, and eleven years or months in `arc-f` lines 17 and 169." (rest of the line covers: "Stale text remains in `grand-game-in-play.md` line 63, `running-the-villains.md` lines 71 and 73, and `01-xanathar.md` line 27.") Stale: `arc-f:17` is now one year (see D4); `arc-f:169` still says eleven months.
- `campaign/structure/arc-f-xanathars-lair.md:169`: "Nar'l has kept this from Xanathar for eleven months." Conflicts with one year (D4).
- `campaign/setting/the-grand-game/the-grand-game.md:91`: "> - **Left open (brief ruling 14), none settled here:** Nihiloor's domination of Xanathar, Nar'l's tenure, Ott Steeltoes, the \"something vast and dreaming\" seed and the Doom Raiders and Enclave Trades Ward lines are not touched." (rest of the line covers: "The page says only that Nar'l reports to Jarlaxle by *sending* spell.") Stale on the tenure, which is settled at `history/02:156`.
- `campaign/setting/villains/jarlaxle.md:179`: "> - **Calls applied:** Left open per ruling 13: Nar'l's tenure (the page gives none), Nihiloor's domination of Xanathar, Ott Steeltoes and the Doom Raiders and Enclave Trades Ward lines." Stale: the Nar'l page gives one year, placed 1491 DR.
- `campaign/setting/villains/manshoon.md:139`: "> - **Left open (brief call 13):** Nihiloor's domination of Xanathar, Nar'l Xibrindas's tenure, Ott Steeltoes, the \"something vast and dreaming\" seed, and the Doom Raiders and Enclave Trades Ward lines. None is stated on this page." Stale on the tenure.
- `campaign/gazetteer/waterdeep/southern-ward.md:260`: "> - **Names with no page:** Brimel Crestfall, Marra Selby, Vaelle Lurval, Volkarr Kibbens, Urlaster Ghann, Pippa Underbough, Tolliver Greenbottle, Marda Goodbarrel, Blossom and Dasher Snobeedle, Tessaly Brightwater, Dessa Voll, Ruid, Duhlark and Alcedor Kolat, Nar'l Xibrindas (his page was not opened) and Istrid Horn's courier cache." (rest of the line covers: "Brimel, Vaelle and the Kolat brothers appear as plain text.") Stale: the Nar'l page exists.
- `campaign/gazetteer/waterdeep/dock-ward.md:310`: "> - **Names with no page:** Xoblob, Gorra, Ilsa Dalloway, Harl Pimm, Captain Staget, Heldar, Rongquan Mystere and Kreb Sorrush (aliases of Jarlaxle and Krebbyg), Wenna Tarrow, Nella Fen, Ostrin Brindle, Tarn Hobble, Piers Hobb, Mirsa, Garrit Moll, Tobiah Ashby, Sarna, the Peabody family and Nar'l Xibrindas appear as plain text." Stale: the Nar'l page exists.
- `campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/design-notes.md:16`: "- Nar'l's tenure is a year, as WDH says, and not the three years in the Notable Figures page or the eleven in **Xanathar's Lair**." The Notable Figures page says one year now (`03-narl-xibrindas.md:21`), so "three years" is stale wording. The "eleven" is stale as in D4.
- `campaign/quests/faction-events/bregan-daerthe/m02-the-wazoo-affair/design-notes.md:35` (the Featured-in line; see D7).
- `campaign/guides/factions/08-bregan-daerthe.md:69` against the m04 outcome (see D6).

### E2. Stale lines in `docs/` (not campaign; not edited)
- `docs/plans/setting-compendium-research-notes/consistency-notable-figures.md:15`: "Nar'l tenure: WDH:32323 \"a year ago\"; wiki 1491 DR; NF xanathars-guild/03:22 three years; organizations/08-xanathars-guild.md:23 three years" (rest of the line covers the other notes). The current page has no "three years" line. Stale.
- `docs/plans/harpers-out-of-scope-notes.md:468`: "His page (:8, :22) says \"three years\"." Stale.
- `docs/plans/setting-compendium-research-notes/pass5/xanathars-guild.md:272` quotes the same stale claim: "The NF now says one year. Stale." Stale.
- `docs/plans/harpers-out-of-scope-notes.md:497`: "the 2024 Mage has no Sending (swapped in by M4)" — an unsourced claim (see D12).

### E3. Sources outside the campaign that are stale or unsupported
- `sources/SOURCE_GUIDE.md:343`: "Nar'l Xibrindas (drow spy working against Xanathar for House Xorlarrin)" — not supported by any searched source (D1).
- `sources/SOURCE_GUIDE.md:514`: "- The documents reveal inter-faction tensions (e.g., Nar'l Xibrindas's loyalties are subtly undermined in Xanathar's report — he's praised too much, which in Xanathar's paranoid world is suspicious)". **Not found.** All 13 pages of `sources/21. Faction Reports of the Grand Game.pdf` were read (printed pp.142-154 [PDF pp.1-13] [img]). "A Briefing for Xanathar Concerning the Grand Game" (printed pp.151-152 [PDF pp.10-11] [img]) does not name Nar'l. The Gralhund study, Jarlaxle's report, the Cassalanter report, the vault notes, the Eyes notes and Manshoon's report name no Nar'l either.
- `sources/Appendix_D_-_Running_the_Tavern.md:205`: "N'arl" spelling (D13) and the replacement line (D14).

### E4. Routed quest references (where the quest-time facts live)
- **Faction Outposts** (`campaign/structure/arc-e-faction-outposts.md`): `:165` ("a captured Xanathar response team member's *Directive from Nar'l* names her as a supplier"); `:183` ("*Correspondence with Nar'l Xibrindas*: Nar'l's letter references smokepowder and provides guildsign directions toward Area X1 of Xanathar's Lair."); `:185` (Intel Yield); `:351` ("Xanathar teams carry operational correspondence from Nar'l or Ahmaergo"); `:491` ("Xanathar's Lair — Nar'l's guildsign trail, gladiatorial transport via Terasse, Ott Steeltoes as guide (three paths)").
- **Factions Guide, Xanathar's Guild** (`campaign/guides/factions/09-xanathars-guild.md`): `:7` ("The first or second team the party encounters carries *A Directive from Nar'l Xibrindas*, instructing the team leader to resupply at Grinda Garloth's."), `:59` (Area B9b, the Korgstrod letter), `:86` ("- *A Directive from Nar'l Xibrindas* (Any Xanathar Response Team)"), `:103` ("- *Correspondence with Nar'l Xibrindas* (Xanathar Sewer Hideout 2 — guildsigns lead to Area X1)").
- **Alexandrian Outposts, printed p.45 [PDF p.10] [img]** (`sources/5. Faction Outposts.pdf`): "Area B9b – Korgstrud's Room: The chest at the foot of his bed is a **mimic**. The coffer in a secret compartment under the bed (DC 13 to find) contains 500 gp and *Correspondence with N'arl Xibrindas*." The letter: "Korgstrod—It is very important that this be kept in strict confidence. Only you, me, and X know of the smokepowder. It must be brought to the Staircase of Eyes on the night of the 1st at precisely the stroke of eleven. Use disposable muscle. I will mark the sewer tunnels west of your hideout with a red eye to guide your men. – N'arl Xibrindas."
- **Alexandrian Revelation Lists** (`sources/17. Outpost and Lair Revelation Lists.pdf`): printed p.122 [PDF p.2] [img], under SEVEN MASKS THEATER: "Letter from N'arl (Sea Maidens Faire)". Printed p.123 [PDF p.3] [img], under GRINDA GARLOTH: "A Directive from N'arl Xibrindas (Any Xanathar Response Team)"; under LAIR: XANATHAR'S LAIR: "Correspondence with N'arl Xibrindas (Xanathar Sewer Hideout 2)".
- **Xanathar's Lair** (unconverted), `campaign/structure/arc-f-xanathars-lair.md`: `:17`, `:43` ("...Nar'l Xibrindas's name and position inside the lair — framed as proof of trust."), `:59` ("**The Guildsign Trail (via Orb Confectioners correspondence).** N'arl Xibrindas's letter from the **Faction Outposts** sewer hideout contains guildsign directions to Area X1..."), `:93`, `:99`, `:101`, `:103`, `:107`, `:111` ("Nar'l and Thorvin must be evacuated or they die. Thorvin will not leave the lair's surviving workers; Nar'l will leave without hesitation."), `:167`, `:169`, `:184`, `:198` ("Trigger: a named NPC (Ahmaergo, Nar'l, Noska) confirms combat with intruders."), `:216`, `:222`, `:339`, `:340` ("Custom stat blocks for Ahmaergo (minotaur veteran), Nar'l (drow mage + grell bodyguard), Nihiloor (mind flayer arcanist)."), `:400`.
- **Sea Maidens Faire** (`campaign/structure/arc-h-sea-maidens-faire.md:15`, `:424`): "The Letter from Nar'l Xibrindas (U3) confirms the BD mole in Xanathar's organization and mentions the Seven Masks Theater purchase."
- **Compromised Eye** (`campaign/quests/faction-events/bregan-daerthe/m04-the-compromised-eye/`): `overview.md:17` (quoted in D5), `:40`, `:73` ("- **Nar'l Xibrindas** (Bregan D'aerthe, secretly, and Xanathar's Guild): the compromised advisor, who trades his information for his life."), `:79` ("- **Ahmaergo** (Xanathar's Guild): holds the case against Nar'l, and does not appear."), `ev-01-the-compromised-eye.md:46`-`:47` (outcomes), `ev-02-twelve-minutes.md:109`-`:112` (outcomes), `:274`, `:413`-`:415` (outcome definitions), `design-notes.md:14`, `:16`, `:21`, `:23`, `:29`.
- **Dinner with Zardoz** (`campaign/quests/faction-events/bregan-daerthe/s03-dinner-with-zardoz/ev-01-dinner-with-zardoz.md`): `:17`, `:41`, `:200` ("Read the one that matches the Nar'l outcome the member marked in **The Compromised Eye**. Zardoz never names Nar'l in any of them."), `:202`, `:210`, `:218`, `:226`, `:400`.
- **Dockside Killer** — Soluun only (D7).
- **Soldier rank event** (`campaign/quests/faction-events/bregan-daerthe/r03-soldier/`, 9 hits in `ev-01-soldier.md`, 4 in `design-notes.md`) — not read line by line in this pass. Referenced at `m04-the-compromised-eye/ev-02-twelve-minutes.md:413`: "the **Soldier** rank event (where Nar'l's intelligence channel is open but thin)".
- **Houseless Noble** (`r50-houseless-noble/ev-01-houseless-noble.md`, 13 hits) — not read in this pass.
- **Trollskull** — `sources/Appendix_D_-_Running_the_Tavern.md:205` (D14).

### E5. Cross-check of other Notable Figures and voice files (not edited)
- `campaign/setting/notable-figures/xanathars-guild/01-xanathar.md:26`: "**Relationships.** Xanathar is the beholder crime lord of Xanathar's Guild, the employer of Ahmaergo (its majordomo), Nihiloor (its mind flayer, which has psionically dominated Xanathar for the last four months without Xanathar knowing), and Nar'l Xibrindas (its drow advisor, whom it does not yet know is Jarlaxle's spy)." Consistent with the page.
- `campaign/setting/notable-figures/xanathars-guild/07-thorvin-twinbeard.md:21` (quoted in A7). Consistent.
- `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:13`: "...and bitter disdain for his brother Nar'l." Consistent.
- `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:25`: "**Relationships.** Soluun is the elder brother of Nar'l Xibrindas (whom he despises), a lieutenant of Jarlaxle (whom he worships), and a serial killer whose disownment by Bregan D'aerthe is a cover story: he carries forged BD identification." Consistent on age.
- `.claude/skills/character-voices/voices/bregan-daerthe.md:47` (Soluun section): "Sound: A low, flat, cold voice. It rises into fervour when he speaks of Jarlaxle or of Nar'l's weakness." Consistent.
- `.claude/skills/character-voices/voices/xanathars-guild.md:132`, in the Thorvin section (heading at `:119`): "- *Business (privately):* \"Nar'l hid the smokepowder behind the third cistern. Put it against the north pillar, and you'll bring the whole damned hall down.\"" Consistent with the cache.

---

## F. Gaps (what a Background would need that no source gives)

1. **Birth, parents, the house name, where he grew up.** No source names the house or the place. The adventure (`:32323`), the wiki (`Nar_l_Xibrindas.txt:68`) and the history (`history/03:43`) say only that the house was wiped out long ago. Suggested: keep the one-line source and tag any extra with `[research]`.
2. **How he came to magic.** No source gives training or a teacher. Soluun's view is the only line: "Soluun considers Nar'l a weakling who turned to arcane magic by way of compensation" (`sources/adventure-wdh.json:32040`). Suggested: stop at "drow mage" (see D2).
3. **Age.** Only Appendix C gives one, as a quest-scene description: "approximately sixty by drow standards" (`sources/Appendix_C_-_Player_Faction_Missions.md:1627`). Not a campaign or adventure fact. Suggested: omit, or tag `[research]` if used.
4. **The date and manner of Jarlaxle's recruitment.** "joined Bregan D'aerthe" has no date and no scene (`sources/adventure-wdh.json:32323`). Suggested: "Jarlaxle placed Nar'l in the Guild in 1491 DR" (`campaign/setting/history/08-the-players-arrive.md:47`, `:81`), with nothing on how.
5. **How he won Xanathar's trust.** The only source says he "managed to convince the beholder to eliminate its other advisors" (`:32323`). No method is given. Suggested: none beyond that sentence.
6. **Names of the advisors he removed.** No source names them. Suggested: do not name anyone.
7. **Name of the grell bodyguard.** None. "a grell" only (`:32324`).
8. **Faith.** None (see A8). Suggested: say nothing. Do not give Lolth.
9. **What Nar'l does for Xanathar day to day.** Only "advisor" and "advice" (`:15066`, `:32323`). Suggested: the Guild page's "Xanathar's advisor and secret Bregan D'aerthe asset" (`08-xanathars-guild.md:102`).
10. **Whom Nar'l's Sending reaches.** The Nar'l entry says "his brother" (`:32331`); the lair-chapter sentence says "his drow brethren" (`:15149`); the campaign says Jarlaxle. Suggested: the campaign's Jarlaxle reading, as day-one, with the D11 conflict noted.
11. **Smokepowder count and date.** Eight kegs over four months (`arc-f:107`) against twenty kegs with no date (`:18162`). Suggested: state that the cache exists and leave the count to the Lair journal (D8).
12. **Whether Jarlaxle holds a contingency.** "Jarlaxle has a contingency if Nar'l is discovered (has not shared it with Nar'l) `[research]`" (`campaign/setting/villains/jarlaxle.md:105`). Tagged research in the source. Suggested: leave out of the Background.
13. **Relationship to Ahmaergo before the campaign.** None on day one. The only Ahmaergo link is quest-time (`m04/overview.md:79`).
14. **Relationship to Thorvin.** Day-one knowledge only (`:18165`; `07-thorvin-twinbeard.md:21`). Nothing about trust.
15. **Death or fate.** None on day one. The quest outcomes are routed (E4).
16. **Alignment.** Single source, the Guild page (`08-xanathars-guild.md:102`). The adventure and the wiki give none. Suggested: keep the line 5 wording.
17. **The Zushaxx name.** `history/08:47` and wiki `:155` name the 1491 beholder Zushaxx; the campaign rule is that Xanathar is "it" (brief ruling 9). Suggested: "Xanathar" throughout.

---

## Not readable

- `Narl_Xibrindas.txt` in the scratchpad `wiki-xg` folder: NOT FOUND (the tool returned a one-line NOT FOUND).
- `sources/Other remix files/*.docx`: not opened (the tools cannot read .docx). `SOURCE_GUIDE.md` names no Nar'l-specific entry for them, but the Jarlaxle guide (`SOURCE_GUIDE.md:690`: "Jarlaxle's personality, tactics, goals, and the Bregan D'aerthe operation") and "The Waterdavian's Guide to Waterdeep NPCs" (`SOURCE_GUIDE.md:695`: "Broad NPC reference") could mention Nar'l. Name them to the orchestrator for extraction.
- Alexandrian PDFs read in this pass, all pages: `11. Lair  Xanathar’s Lair.pdf` (9 pages), `5. Faction Outposts.pdf` (13 pages), `17. Outpost and Lair Revelation Lists.pdf` (4 pages), `1. The Villains.pdf` (7 pages; no Nar'l), `21. Faction Reports of the Grand Game.pdf` (13 pages; no Nar'l). Not opened: the rest of the PDF set (for example `6. Faction Response Teams.pdf`, which carries the response-team Directive documents; `SOURCE_GUIDE.md:350`). The rest were not searched by content.
- All PDF quotes are **[img]** transcriptions. Check each against `pdftotext -layout` before prose use.
- `sources/research/pass3-bundles/` and `pass4-bundles/`: searched by grep for "Nar'l|Xibrindas|Xorlarrin". The `guilds/campaign-hits.txt` (pass3, 92 hits) and the pass5 campaign-hits are older snapshots and were not quoted. Current files were checked directly.

## Not run

- `voicecheck.py` was not run (research only).
- The page was not written. No file was edited except this notes file. Nothing committed.
