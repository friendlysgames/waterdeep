# Pass 6 research notes: Jandar Chergoba

Page: `campaign/setting/notable-figures/cassalanters/09-jandar-chergoba.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR. Jandar is a cult fanatic and the head chef of Cassalanter Villa. He is alive, in the kitchen, and preparing for Founders' Day. The pact is a GM fact. Cassalanter secrecy applies (nobody outside the household and the cult knows the pact).
Model format: `docs/plans/setting-compendium-research-notes/pass6/cassalanters/04-osvaldo-cassalanter.md`
Companion notes: `docs/plans/setting-compendium-research-notes/pass6/cassalanters/10-seffia-naelryke.md`

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes (`\"`) are shown as plain quotes. Tags such as `{@creature ...}` are left as written.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. Pages were read as rendered images, and their quotes are transcriptions. Check exact wording with `pdftotext -layout` before any quote goes into prose:
  - `sources/10. Lair  Cassalanter Villa.pdf` (printed pp.77-82 = PDF pp.1-6). Read: PDF pp.1-6.
  - `sources/5. Faction Outposts.pdf` (printed p.41 = PDF p.6). Read: PDF pp.5-6 (printed pp.40-41).
- Alexandrian appendices B, C and D: `sources/Appendix_C_-_Player_Faction_Missions.md` and `sources/Appendix_D_-_Running_the_Tavern.md` were searched by name. Quotes from them are exact.
- Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-cassalanters/09-jandar-chergoba.txt`. Quoted as "wiki line N" (that file's lines). Citation key is `Waterdeep: Dragon Heist` (5e), as the wiki prints it on each `Cite book` line. No other wiki bundle names Jandar (see Not found).
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **Two campaign files give Jandar a debt, and the page says only "the craft that brought him to the Cassalanters' attention".** The structure doc gives a specific debt and a specific date (`campaign/structure/arc-g-cassalanter-villa.md:98`). The page's Motivations (line 15) uses the craft wording. Both are kept by the Organization page's Draft Notes (`campaign/setting/organizations/10-cassalanters.md:195`). The Background can state the debt, because it is day-one (a debt that already exists on Ches 1).
2. **The stat block name is "Cult Fanatic" on this page and "Cultist Fanatic" on the Seffia page** in the same folder. The adventure and the Alexandrian PDF both say "cult fanatic". One folder file calls the name the 2014 name (see D1).
3. **The kitchen knives are "ten" in the adventure and the campaign, and "a dozen" in the wiki** (see D2). The page's Resonance (line 11) and Morale (line 23) use the campaign number.
4. **Founders' Day is Flamerule 1 in the campaign and the adventure, and "TARSAKH 9th" in the Alexandrian Lair** (see D5). Jandar's feast date is the campaign date.
5. **The Morale line's "retreats to a defensible position" and the Resonance line's "shock when ten knives rise" are encounter behaviour.** The adventure's only fight line for Jandar is the "For'zaal" shout (`sources/adventure-wdh.json:20256`). "Retreats to a defensible position" has no source (F7).

---

## A. Background facts by theme

### A1. Origin, birth and early life (no source gives any)

**Wiki, the lead line (no birth, birthplace or childhood given)**
> "'''Jandar Chergoba''' was the Head Chef of the [[Cassalanter]] family in [[Waterdeep]], who worked in [[Cassalanter Villa]] in the [[Waterdeep/Sea Ward|Sea Ward]] ''circa'' the late 15{{th}} century [[DR]].<ref name="tr" />"
> — wiki line 65 (edition: 5e, `Waterdeep: Dragon Heist`, p.117 per the ref `tr` on wiki line 21)

**Wiki, the infobox (blank for origin, age and family)**
> "| ethnicity      = " (wiki line 16, blank)
> "| age            = " (wiki line 18, blank)
> "| dob            = " (wiki line 23, blank)
> "| parents        = " (wiki line 32, blank)

**Adventure: no origin, no age, no family**
The adventure gives him one paragraph (`sources/adventure-wdh.json:18507`-`:18512`), quoted in A2.

**Campaign: the page has no origin and no childhood**
No campaign file gives a birthplace, age, family or pre-cult life for Jandar. The search terms are in Not found.

### A2. Post, duties and rank in the household

**Adventure, head chef and menu**
> "As the head chef of Cassalanter Villa, {@creature Jandar Chergoba|wdh|Jandar} determines each day's menu and oversees all activity in the kitchen."
> — `sources/adventure-wdh.json:18511` (Head Servants, page 117)

> "Jandar is a male tiefling {@creature cult fanatic}. He is often in the kitchen ({@area C10|303})."
> — `sources/adventure-wdh.json:18512` (Head Servants, page 117)

**Adventure, the head servants are cult members**
> "The head servants of Cassalanter Villa are members of the cult. These four servants are described below. All appear to be tieflings, though one is not. The following changes apply to the tieflings' stat blocks:"
> — `sources/adventure-wdh.json:18467` (Head Servants, page 116)

> "The tieflings are lawful evil."
> — `sources/adventure-wdh.json:18471` (list item under the same heading)

**Adventure, the kitchen staff under him**
> "The head chef, {@creature Jandar Chergoba|wdh} (see \"Head Servants,\"), oversees six chefs (human {@creature commoner||commoners}). If Jandar believes the characters are a threat, he shouts \"For'zaal,\" causing ten knives to magically rise from the counters and attack. These knives are {@creature flying sword||flying swords} that deal 4 ({@dice 1d6 + 1}) piercing damage on a hit."
> — `sources/adventure-wdh.json:20256` (C10, Kitchen, page 121)

**Campaign, the chain of command (Organization)**
> "- **Chain of command:** Ammalia makes the final calls for the family and the cult, and Victoro, who leads the worship, has stopped questioning her. Willifort Crowelle links the family to everyone who works for it. He runs household security, reports to Ammalia and directs the spy and the poisoner. Seffia Naelryke commands the field team and answers to Victoro, and the head servants keep order at the rites."
> — `campaign/setting/organizations/10-cassalanters.md:51`

**Campaign, the household staff roster (Organization)**
> "- **Household staff:** The villa employs sixteen named staff, and ten of them know nothing about the temple (`arc-g-cassalanter-villa.md` line 91). The six cult members are Willifort the butler, Tissina Khyret the attendant, Nana Rosse the twins' caretaker, Jandar Chergoba the head chef, and the field pair Seffia Naelryke and Arn Xalrondar. The other ten are Corvo (footman), Pela (laundress), Marchello (gardener), Fiorella (cook's assistant), Doro (stable hand), Lissette (upstairs maid), Rennet (scullion), Maesta (housekeeper), Tomas (night watchman) and Bressa (nursemaid). Maesta manages the non-cult staff and is loyal to the household's reputation, not to the Cassalanters themselves."
> — `campaign/setting/organizations/10-cassalanters.md:52`

**Campaign, the cult's rites (Organization)**
> "- **The cult:** Victoro leads it, and the whole cult gathers in the temple at midnight on the first day of every tenday. About thirty members attend when it meets in force, roughly half of them nobles and the rest Waterdhavian commoners (*Dragon Heist*, 5e). Willifort, Tissina Khyret, Nana Rosse and Jandar Chergoba keep order at the rites while Ammalia pours the wine. The cult reaches beyond the household. Yalah Gralhund keeps Asmodean symbols and robes with Cassalanter embroidery in a trunk, and her groundskeeper Hurv Taldred wears a Cassalanter devotional mark (**House Gralhund**)."
> — `campaign/setting/organizations/10-cassalanters.md:50`

**Adventure, the Cult Gathering (his post at the rites)**
> "If the cult is here in force, thirty human {@creature cultists||cultists} stand in neat rows before the statue, chanting to Asmodeus with wooden goblets in hand while their leader, {@creature Victoro Cassalanter|WDH} (see {@adventure appendix B|WDH|12}), tosses offerings into the bowl. Roughly half of the cultists are members of the nobility; the rest are Waterdavian rabble brought into the cult to fill out the ranks. Standing around the perimeter are {@creature Willifort Crowelle|WDH}, {@creature Tissina Khyret|wdh}, {@creature Laiba \"Nana\" Rosse|wdh|Laiba Rosse}, and {@creature Jandar Chergoba|wdh} (see \"Head Servants\"). Their job is to make sure the other cultists behave themselves while {@creature Ammalia Cassalanter|WDH} (see {@adventure appendix B|WDH|12}) walks gracefully through the crowd with a golden decanter, ceremonially pouring wine into the cultists' goblets for toasting to the Lord of the Nine Hells. Lady Cassalanter's six {@creature imp||imps} (see {@area C25|328}) are perched invisibly on the statue."
> — `sources/adventure-wdh.json:22818` (Cult Gathering, page 129)

**Campaign, the cult and household knowledge (Willifort page)**
> "- **Laiba \"Nana\" Rosse** and **Jandar Chergoba:** Fellow cult members, who keep order at the rites beside Willifort and Tissina."
> — `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:39`

**Campaign, Asmodeus page (cult fanatic list)**
> "- **Who is tied to him:** The Cassalanters. Victoro Cassalanter is a half-elf banker and secret priest of Asmodeus. Ammalia Cassalanter is a Tethyrian human wizard and secret worshipper. Tissina Khyret, Laiba \"Nana\" Rosse, Jandar Chergoba, Seffia Naelryke and Arn Xalrondar are cult fanatics. Willifort Crowelle, the doppelganger butler, is their trusted operative."
> — `campaign/setting/deities/asmodeus.md:72`

**Campaign, the kitchen (room text; quest-time location, routed)**
> "**C10 — Kitchen.** Ground floor, west wing. Jandar Chergoba commands the kitchen with six commoner assistants and a rack of knives he can animate on command (\"For'zaal\" — ten flying swords). The cellar key ring hangs on a hook in the pantry. During Founders' Day: Jandar is outside on the lawn, preparing the feast. The kitchen is empty except for Fiorella, who has been told to stay inside."
> — `campaign/structure/arc-g-cassalanter-villa.md:199`

**Campaign, the kitchen room note (location journal)**
> "Jandar Chergoba commands this kitchen with quiet authority. He speaks to his staff in clipped instructions, rarely looks up from whatever he is preparing, and does not welcome guests in this part of the house. If the party enters during kitchen hours, he pauses, sets down a knife, and says simply: \"This is a working kitchen. Guests aren't received here.\""
> — `campaign/locations/cassalanter-villa/05-kitchen.md:9`

**Campaign, the area overview**
> "**Jandar Chergoba** (chef): C10 during kitchen hours. Can animate ten flying swords (command word \"For'zaal\"; deactivation word \"Basta\")."
> — `campaign/locations/cassalanter-villa/area-overview.md:40`

**Wiki, his post (5e, cited p.117 and p.121)**
> "During his tenure as a head chef in the {{YearlinkName|1492}}, Jandar oversaw the manse's kitchens and determined the family's daily menus.<ref name=\"tr\" /> He supervised six [[human]] cooks.<ref name=\"tr-p121\">{{Cite book/Waterdeep: Dragon Heist|121}}</ref>"
> — wiki line 74 (History)

### A3. The debt, and how the cult service began (day-one; the structure doc is the only source)

**Campaign, the debt and the date (structure doc, Cassalanter Villa cult roster)**
> "- **Jandar Chergoba** (cult fanatic, head chef) — bound by debt. Victoro holds a 3,000 gp obligation over him from a failed restaurant venture. The debt converted into cult service three years ago. Jandar attends gatherings, prepares ritual meals, and commands the kitchen's ten animated knives (flying sword statistics). He hates what he does. DC 12 Charisma (Persuasion) with an offer of protection — or DC 10 if the party can resolve the debt — turns him. He provides: kitchen schedules, which deliveries access the cellar, and the location of the wine cellar's false wall."
> — `campaign/structure/arc-g-cassalanter-villa.md:98` (The debt, "three years ago", and "He hates what he does" are day-one facts or inner-life hints, see A3 and G. The DC clauses and "He provides" are quest-time, see C.)

**Campaign, the same debt (structure doc, Villa intro)**
> "The household holds six souls who know what lies beneath. Willifort Crowelle, doppelganger, serves Asmodeus with genuine devotion — the family is secondary. Tissina Khyret, Ammalia's attendant, is a cult fanatic who joined out of loyalty to Ammalia personally — she does not know the contract's full terms. Laiba \"Nana\" Rosse, the twins' caretaker, is a cult fanatic who joined the cult to remain close to the children — she would betray the Cassalanters to save Terenzio and Elzerina. Jandar Chergoba, head chef, is a cult fanatic bound by debt — Victoro holds a financial obligation over him that converted into cult service. Seffia Naelryke commands the external operations team and knows the cult's military posture. Arn Xalrondar, her lieutenant, handles field security for the outposts and has never set foot in the temple."
> — `campaign/structure/arc-g-cassalanter-villa.md:21`

**Campaign, the recruiting pattern (Organization, Beliefs)**
> "- **Service Is Worship:** The cult's members fold devotion into the work they do for the family. Tissina Khyret attends Ammalia, Nana Rosse minds the twins, Jandar Chergoba cooks and Seffia Naelryke runs field operations, and none of them sees a conflict between the job and the god. They came to the faith by different roads: Tissina out of loyalty to Ammalia, Nana Rosse to stay close to the twins, and Jandar through a debt to Victoro that became cult service (`arc-g-cassalanter-villa.md` lines 96-98)."
> — `campaign/setting/organizations/10-cassalanters.md:40`

**Campaign, the recruiting pattern (Organization, Methods)**
> "- **Recruiting:** The cult draws nobles and commoners with the promise of wealth and status (*Dragon Heist*, 5e). It also binds people through debt, as with Jandar, through loyalty, as with Tissina, and through closeness to the twins, as with Nana Rosse (`arc-g-cassalanter-villa.md` lines 96-98). The **Asmodeus** page says his priests exploit greed and impatience, and the wiki says his cult works as a mutual-aid society for merchants and nobles who raise one another in rank (Forgotten Realms Wiki, *Asmodeus*, 3e) `[research]`."
> — `campaign/setting/organizations/10-cassalanters.md:69`

**Campaign, the timing of his service (Organization, History)**
> "- **Before Ches 1, 1492 DR, undated, the temple and the cult:** The temple of Siamorphe that lay beneath the estate was desecrated by the family's devil-worship and given to Asmodeus, and its thirty-foot statue was carved from an image of Siamorphe (*Dragon Heist*, 5e; **The Cassalanters** in Villains). Jandar Chergoba's debt to Victoro turned into cult service three years ago, which places some of the cult's household recruiting at the time of the bargain (`arc-g-cassalanter-villa.md` line 98). No source dates the temple's conversion, the cult's founding or the arrival of its other members `[research]`."
> — `campaign/setting/organizations/10-cassalanters.md:27`

**Campaign, the bargain's year (History; the year is derived)**
> "- **About 1489 DR, the bargain:** Victoro and Ammalia Cassalanter are Waterdeep aristocrats who made a devil's bargain. The details vary depending on who is speaking. Three years ago, they forged a pact with Asmodeus, trading their children's souls for power and prosperity. Ammalia found the way through infernal research, and a pit fiend carried the contract to the family. Victoro and Ammalia signed it together in the temple beneath their villa, after they had read the terms, and the deal also bought good health and long life (**A Debt in Blood**; `arc-g-cassalanter-villa.md` line 11)."
> — `campaign/setting/organizations/10-cassalanters.md:25`
>
> The Jandar debt is "three years ago" in the structure doc (line 98). The bargain is "Three years ago" in the Organization page (line 25). The two are the same year by the campaign's count. The Organization page's Draft Notes (line 195) keep the two phrases, and the page should use "three years ago" only with the 1489 DR date from **A Debt in Blood**.

**Campaign, the bargain's year (Villains)**
> "The bargain was made in 1489 DR, counted back from the published \"three years ago\". Ammalia found the way through infernal research. A pit fiend carried the contract to them, and they signed it together in the temple beneath their own villa."
> — `campaign/setting/villains/cassalanters.md:24`

### A4. Founders' Day and his part in the feast (day-one plan; the feast is a future event)

**Adventure, the feast (Founders' Day party and the poison)**
> "{@creature Jandar Chergoba|wdh|Jandar} isn't here. Instead, he's preparing Ammalia's {@condition poisoned} feast in a cooking pavilion out on the estate's sprawling lawn."
> — `sources/adventure-wdh.json:20263` (C10, Founders' Day subsection, page 121)

**Adventure, the feast itself (Day of the Damned; quest-time event, see C)**
> "{@creature Ammalia Cassalanter|WDH} hosts a grand party on Founders' Day that begins in the early afternoon and ends at midnight. Wealthy guests begin to arrive in the late afternoon and gather inside the villa, away from the sun and heat, while one hundred of Waterdeep's poorest residents-most brought from the Field Ward-gather under pavilions set up on the lawn. Hired actors dressed as Waterdeep's founders parade around, and bards play lively tunes. No one suspects that the food in the pavilion tents has been laced with midnight tears-a poison that will slay the impoverished guests at the stroke of midnight. Ammalia is immune to poison and thus partakes freely of the delicious food. Wealthy guests who remain holed up in Cassalanter Villa eat and drink at separate tables and are spared a grisly end."
> — `sources/adventure-wdh.json:22916` (Day of the Damned, page 130; rest of the passage covers: the rest of the feast, the gold convoy and the barbed devil, the aftermath, in `:22917`-`:22919`)

**Campaign, the Founders' Day date (Organization, GM Secret)**
> "- **The feast:** On Founders' Day, Flamerule 1, the family plans to poison 99 guests at a feast to collect the ninety-nine souls. Ammalia is the architect of the feast and Jandar Chergoba, the villa's head chef, is the person who sees that the poison is distributed correctly."
> — `campaign/setting/organizations/10-cassalanters.md:130`

**Campaign, the poison and his role (Organization, Methods)**
> "- **Poison:** Ammalia keeps ten vials of the poison called midnight tears in her private study, and she is immune to poison (*Dragon Heist*, 5e). She means to serve ninety-nine of the one hundred guests wine laced with it, so that they die within a day and nothing connects them to the house (**The Cassalanters** in Villains). Jandar Chergoba sees that the poison is distributed correctly. Rella Asp is a poisoner under a cook's cover (**Rella Asp**)."
> — `campaign/setting/organizations/10-cassalanters.md:67`

**Campaign, Ammalia's page (his role in one line)**
> "- **Jandar Chergoba:** The head chef, who sees that the poison at the feast is distributed correctly."
> — `campaign/setting/notable-figures/cassalanters/02-ammalia-cassalanter.md:47`

**Campaign, the feast's date (structure doc, quest opener)**
> "Founders' Day falls on the first of Flamerule. Ammalia has prepared ten vials of midnight tears poison, stored in her study beside the grimoire that contains the commune ritual. The plan: invite one hundred of Waterdeep's poorest to a charitable feast on the villa's lawn pavilions. The food is genuine. The poison is administered through the wine — ninety-nine cups, one untouched, satisfying the contract's \"one shy of a hundred\" requirement. The gold from the Vault of Dragons — all five hundred thousand pieces — provides the financial component. Together, gold and souls buy the twins' freedom before their birthday."
> — `campaign/structure/arc-g-cassalanter-villa.md:19`

**Campaign, the date in the history page (Timeline)**
> "- Flamerule 1, 1492 DR: Founders' Day, the feast and Ammalia's operational window. The day is in the published adventure and the year is in the Alexandrian timeline."
> — `campaign/setting/history/05-a-debt-in-blood.md:127`

### A5. The kitchen's knives, the command word and the deactivation word (routed; encounter tools)

**Adventure, the command word (the adventure gives the phrase, not the deactivation word)**
> "The head chef, {@creature Jandar Chergoba|wdh} (see \"Head Servants,\"), oversees six chefs (human {@creature commoner||commoners}). If Jandar believes the characters are a threat, he shouts \"For'zaal,\" causing ten knives to magically rise from the counters and attack."
> — `sources/adventure-wdh.json:20256` (repeated from A2; the trigger is his own judgement of the party)

**Adventure, the golden key and the regalia box (day-one object; a quest-time opening route)**
> "{@creature Jandar Chergoba|wdh}, the head chef, keeps his golden sacrificial dagger, golden mask, and crimson robes (see \"Cult of Asmodeus,\") in a locked iron box underneath a sack of potatoes. The box can be unlocked with Jandar's golden key, or by a character who makes a successful {@dc 15} Dexterity check using thieves' tools. A character can also pry it open with a successful {@dc 25} Strength (Athletics) check."
> — `sources/adventure-wdh.json:20289` (C11, Pantry, Locked Iron Box, page 121)

**Campaign, the "Basta" word and its source (structure doc, encounter mechanics)**
> "Jandar's animated knives (10 flying swords) activate on his command word \"For'zaal.\" They fight until destroyed or until Jandar speaks \"Basta\" (the deactivation word, obtainable from Fiorella or a DC 14 Charisma (Intimidation) check on Jandar)."
> — `campaign/structure/arc-g-cassalanter-villa.md:251` (encounter mechanics; see C)

**Campaign, the carving knives (location journal)**
> "**The Carving Knives.** If Jandar speaks the command word \"For'zaal,\" ten flying swords animate from the knife rack and attack on his direction. Deactivation word: \"Basta\" — obtainable from Fiorella (she overheard it once and doesn't know what it means) or by succeeding on a DC 14 Charisma (Intimidation) check directed at Jandar mid-combat."
> — `campaign/locations/cassalanter-villa/05-kitchen.md:19`

**Wiki, the knives (5e, cited p.121)**
> "Jandar possessed spellcasting abilities, appropriate for being a cultist of [[Asmodeus]].<ref name=\"tr\" /> With the use of a single [[command word]], \"For'zaal,\" he could animate a dozen of kitchen [[knives]] to become animated akin to ''[[flying sword]]s''.<ref name=\"tr-p121\" />"
> — wiki line 68 (Abilities). Conflicts with "ten" (D2).

### A6. Possessions and the locked box

**Wiki, the regalia (5e, cited p.121)**
> "Jandar owned a regalia of [[Asmodeus]], his cultist uniform, which included a [[gold]]en sacrificial [[dagger]], a golden [[Mask (object)|mask]], and crimson [[robe]]s. He kept it hidden in a lockbox, hidden underneath sacks of [[potato]]es in Cassalanter Villa kitchens.<ref name=\"tr-p121\" />"
> — wiki line 71 (Possessions)

**Campaign, the cult's regalia on the Willifort page (a possible overlap with the lockbox, see D7)**
> "- **The cult:** Willifort is a full member of the Asmodean cult beneath the villa. He keeps order at the rites beside Tissina Khyret, Nana Rosse and Jandar Chergoba, and his regalia lies in the lockbox that he shares with Tissina."
> — `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:88`

**Campaign, the Organization page (no regalia)**
The Organization page does not name Jandar's regalia. The regalia is adventure and wiki material only.

### A7. Current state on Ches 1, 1492 DR (what he is doing and what he knows)

**Campaign, his page's Persona (day-one habit and role)**
> "**Persona.** To the world, Jandar runs the Cassalanter kitchen with the efficiency of a general who has never had to reconsider a campaign. To those who threaten the kitchen, a single word raises every knife in the room. Deep down, the Founders' Day feast is the most important project of his career, and he has approached it with the same precision he brings to everything else."
> — `campaign/setting/notable-figures/cassalanters/09-jandar-chergoba.md:21` (the public half is day-one; "a single word raises every knife" is encounter, see C)

**Campaign, his page's Relationships**
> "**Relationships.** Jandar is the Cassalanter Villa's head chef, a cult fanatic, the keeper of golden sacrificial implements hidden under a sack of potatoes, and the person who determines whether the Founders' Day poison is distributed correctly."
> — `campaign/setting/notable-figures/cassalanters/09-jandar-chergoba.md:25`

**Campaign, his knowledge of the attic (who knows what is behind the door)**
> "The household staff knows the attic is forbidden. Only Willifort Crowelle — the doppelganger butler who serves Asmodeus directly — knows what is behind the door."
> — `campaign/structure/arc-g-cassalanter-villa.md:13`
>
> Jandar is household staff. He is not named among those who know what is behind the door. The page must not say he does (see F4).

**Campaign, the staff who notice him (Fiorella, non-cult, day-one)**
> "- **Fiorella** (cook's assistant, human female, 20s) — works under Jandar. Has noticed Jandar's anxiety before specific nights and that he prepares food for \"private events\" she is never invited to attend. Knows where the cellar keys are kept (C10 pantry hook). If told the truth: frightened but resolute — wants the children safe."
> — `campaign/structure/arc-g-cassalanter-villa.md:107`

**Campaign, the cult members' motivations (structure doc, Cult section)**
> "The cult members are individually motivated — true belief (Willifort), personal loyalty (Tissina), love for the children (Nana Rosse), debt-bound service (Jandar). They are not interchangeable. A party that turns Tissina gets different information than one that turns Jandar. A party that turns Nana Rosse gets the most emotionally charged cooperation: a woman who loves the children more than she fears the cult."
> — `campaign/structure/arc-g-cassalanter-villa.md:519`

**Campaign, the Relationships preface (who knows the pact)**
> "Each entry gives the stance on Ches 1, 1492 DR. Outside the household and the cult, nobody knows about the pact, so every faction below only suspects the family, and Jarlaxle is the one exception."
> — `campaign/setting/organizations/10-cassalanters.md:76`

**Campaign, Nana Rosse's line (the only source line that limits a cult member's knowledge)**
> "**Laiba \"Nana\" Rosse** (cult fanatic, the twins' caretaker) — loves Terenzio and Elzerina fiercely. Joined the cult to stay close to the children when the Cassalanters began restricting household access. She knows the gatherings happen, has seen the robes. She does not know about Osvaldo or the Founders' Day plan."
> — `campaign/structure/arc-g-cassalanter-villa.md:97` (Jandar's line in the same file, line 98, is silent on what he knows; see F4 and F5.)

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, the Jandar page: "- *Tiefling cult fanatic (Asmodeus), lawful evil, he/him*. Stat block: **Cult Fanatic**." — `campaign/setting/notable-figures/cassalanters/09-jandar-chergoba.md:5`
- Campaign, the Organization page: "- **Jandar Chergoba** — Tiefling cult fanatic (Asmodeus), lawful evil. See the **Jandar Chergoba** page in Notable Figures." — `campaign/setting/organizations/10-cassalanters.md:101`
- Adventure, the head servants: "The tieflings are lawful evil." — `sources/adventure-wdh.json:18471` (applies to the four head servants as a group; Jandar is one of the four by the heading at 18467)
- Wiki: the alignment fields are blank (wiki lines 43-63; for example "| alignment5e    = " at wiki line 60).
- Alexandrian Lair: no alignment for Jandar in the stat reference (printed p.82, transcription).

**Species**
- Campaign, the Jandar page: "*Tiefling cult fanatic (Asmodeus), lawful evil, he/him*" (`campaign/setting/notable-figures/cassalanters/09-jandar-chergoba.md:5`)
- Adventure: "Jandar is a male tiefling {@creature cult fanatic}." — `sources/adventure-wdh.json:18512`
- Wiki: "| race           = [[Tiefling]]" (wiki line 15)
- Alexandrian Lair, stat reference, printed p.82 [PDF p.6] (transcription): "Jandar Chergoba (Head Chef) – tiefling cult fanatic, MM p. 345 (DH p. 117)"

**Pronouns**
- Campaign, the Jandar page: "he/him" (`campaign/setting/notable-figures/cassalanters/09-jandar-chergoba.md:5`)
- Adventure: "He is often in the kitchen" (`sources/adventure-wdh.json:18512`); "Jandar is a male tiefling" (same line).
- Wiki: "| sex            = Male" (wiki line 13); "| gender         = Masculine" (wiki line 14).
- Result: "he/him" is sourced by the adventure and the page. No `[research]` is needed for pronouns.

**Stat block**
- Campaign, the Jandar page: "Stat block: **Cult Fanatic**." (`campaign/setting/notable-figures/cassalanters/09-jandar-chergoba.md:5`)
- Adventure: "Jandar is a male tiefling {@creature cult fanatic}." (`sources/adventure-wdh.json:18512`)
- Alexandrian Lair, printed p.82 [PDF p.6] (transcription): "Jandar Chergoba (Head Chef) – tiefling cult fanatic, MM p. 345 (DH p. 117)"
- Campaign, the Factions Guide (Seffia's team, the name used for a cult fanatic in this folder): "**Seffia's Team.** Seffia Naelryke (**Cultist Fanatic**) + 2 **Spies** + 1 **Veteran** + 1 invisible **Imp**." — `campaign/guides/factions/11-cassalanters.md:17` (see D1)

**Wiki infobox fields (5e, `Waterdeep: Dragon Heist`, p.117)**
- wiki line 7: "| titles         = Head Chef"
- wiki line 11: "| home           = [[Cassalanter Villa]], [[Waterdeep]]"
- wiki line 17: "| occupation     = Chef, cultist"
- wiki line 19: "| patron deity   = [[Asmodeus]]"
- wiki line 21: "| basicrefs      = <ref name=\"tr\">{{Cite book/Waterdeep: Dragon Heist|117}}</ref>"

---

## C. Sentences on the current page that narrate quest-time or depend on a discovery

Current page: `campaign/setting/notable-figures/cassalanters/09-jandar-chergoba.md`. The page has no Background, Personality or Connections section yet and no Draft Notes. Each row says whether the sentence is day-one, and where its fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L5 | "*Tiefling cult fanatic (Asmodeus), lawful evil, he/him*. Stat block: **Cult Fanatic**." | Day-one. Stat block name conflicts within the folder (D1) | Section B |
| 2 | L6 | "- **Affiliation:** The Cassalanters (cult)" | Day-one. Matches the Organization page's cult roster (`10-cassalanters.md:52`) | A2 |
| 3 | L7 | "- **Featured in:** Cassalanter Villa, Cassalanter Villa (location)" | Quest references only. No quest journal names Jandar (Not found) | `campaign/structure/arc-g-cassalanter-villa.md:199`; `campaign/locations/cassalanter-villa/05-kitchen.md:9` |
| 4 | L11 | "**Resonance.** Jandar should inspire the professional respect any accomplished chef earns; shock when ten knives rise from the counters; and cold realization that the Founders' Day menu is already planned." | Three clauses. "professional respect" is a character trait with no event. "shock when ten knives rise from the counters" is encounter time (`sources/adventure-wdh.json:20256`). "the Founders' Day menu is already planned" is day-one (`campaign/setting/organizations/10-cassalanters.md:130`) | `sources/adventure-wdh.json:20256`; `campaign/locations/cassalanter-villa/05-kitchen.md:19` |
| 5 | L13 | "**Emotions.** Jandar most often feels rigorous professional pride in the kitchen's standards, theological certainty carried without drama, the specific pleasure of a plan executed flawlessly, controlled urgency on the days that matter, and contempt for anyone who asks about the menu without understanding what the menu serves." | Day-one habits. "controlled urgency on the days that matter" is tied to the feast days, whose date is a day-one plan (`campaign/setting/organizations/10-cassalanters.md:130`). "theological certainty" is a day-one trait with no Jandar-specific source (the cult's faith is sourced at `campaign/setting/organizations/10-cassalanters.md:40`) | `campaign/setting/organizations/10-cassalanters.md:40`; `campaign/setting/organizations/10-cassalanters.md:130` |
| 6 | L15 | "**Motivations.** Jandar wants to run the kitchen to his exacting standards, prepare the Founders' Day feast exactly as planned, and serve Asmodeus through the craft that brought him to the Cassalanters' attention." | Day-one plan. "the craft that brought him to the Cassalanters' attention" conflicts with the structure doc's debt (`arc-g-cassalanter-villa.md:98`). Kept verbatim per ruling 3; the Background explains the debt (D3) | `campaign/structure/arc-g-cassalanter-villa.md:98`; `campaign/setting/organizations/10-cassalanters.md:195` |
| 7 | L17 | "**Inspirations.** When playing Jandar, channel Gordon Ramsay (*Hell's Kitchen*, precision without warmth), Anthony Bourdain (the seriousness of craft), and Hannibal Lecter (*Hannibal*, the disconcerting chef in a domestic context)." | Not a fact about the campaign. Real-person references, kept verbatim | n/a |
| 8 | L21 | "**Persona.** To the world, Jandar runs the Cassalanter kitchen with the efficiency of a general who has never had to reconsider a campaign. To those who threaten the kitchen, a single word raises every knife in the room. Deep down, the Founders' Day feast is the most important project of his career, and he has approached it with the same precision he brings to everything else." | Public half is day-one. "To those who threaten the kitchen, a single word raises every knife in the room" is encounter time (the "For'zaal" shout, `sources/adventure-wdh.json:20256`). "Deep down ... feast" is day-one and matches the Organization page (`10-cassalanters.md:130`) | `sources/adventure-wdh.json:20256`; `campaign/setting/organizations/10-cassalanters.md:130` |
| 9 | L23 | "**Morale.** In a fight, Jandar speaks the word \"For'zaal\" (raising ten flying swords) and retreats to a defensible position. He does not abandon the kitchen before Founders' Day." | Encounter behaviour. "speaks the word 'For'zaal'" is sourced (`sources/adventure-wdh.json:20256`). "retreats to a defensible position" has no source (F7). "He does not abandon the kitchen before Founders' Day" is day-one as the page's own habit; the feast is his task (`campaign/structure/arc-g-cassalanter-villa.md:199`) | `sources/adventure-wdh.json:20256`; `campaign/locations/cassalanter-villa/05-kitchen.md:19` |
| 10 | L25 | "**Relationships.** Jandar is the Cassalanter Villa's head chef, a cult fanatic, the keeper of golden sacrificial implements hidden under a sack of potatoes, and the person who determines whether the Founders' Day poison is distributed correctly." | Day-one. "the keeper of golden sacrificial implements hidden under a sack of potatoes" is sourced (`sources/adventure-wdh.json:20289`). "determines whether the Founders' Day poison is distributed correctly" is close to the Organization's wording, which says he "sees that the poison is distributed correctly" (`10-cassalanters.md:130`) | `sources/adventure-wdh.json:18511`, `:20289`; `campaign/setting/organizations/10-cassalanters.md:130` |
| 11 | L29 | "Jandar Chergoba is the Cassalanter Villa's head chef, a tiefling who runs his kitchen with the efficiency of a general and produces food that guests remember long after they leave." | Day-one public face. Count: 30 words. The Pass 6 brief sets the Overview at 21 words or fewer per sentence (ruling 7 in its list), so this sentence is over the limit and the drafter rewrites it | `sources/adventure-wdh.json:18511`; `campaign/setting/notable-figures/cassalanters/09-jandar-chergoba.md:21` |

**Voice profile (`.claude/skills/character-voices/voices/cassalanters.md`, "### Jandar Chergoba" at lines 155-169)**

The file's secrecy header says the "after discovery" register is "used only once the party has found the truth (villain Phase 2 onward, or when the character is confronted in the temple)" (`.claude/skills/character-voices/voices/cassalanters.md:3`). The Jandar profile has an "After discovery" line. That line is quest-time under the header's own rule.

> "- **Sound:** A sharp, clipped, commanding voice pitched to carry over a kitchen." — `.claude/skills/character-voices/voices/cassalanters.md:158` (day-one)

> "- **Sentence shape:** Terse kitchen commands and precise culinary judgements. After discovery: calm, cold certainty." — line 159. "After discovery: calm, cold certainty" is the quest-time register (the drafter reports the change under rule 16).

> "- **Word choice:** Kitchen military: \"service\", \"stations\", \"mise en place\", \"the menu\". He calls intruders \"pests\"." — line 160 (day-one habit; "intruders" names the party, which is a quest-time role, so the drafter keeps "pests" as a habit only)

> "- **Swearing:** *Punctuation · Colourful · Tirade.* Kitchen-grade filth at his staff (\"Who plated this? A blind fucking goat?\"). Never in front of guests. Tirade: \"Who plated this? You under-seasoned, over-reduced, lumpy-sauced, cold-plated, knife-dropping, onion-weeping, pan-scorching cunt of a commis, get out of my kitchen and take your shame with you!\"" — line 161 (day-one; the swearing stays, adult table)

> "- **Personality in speech:** Professional pride and contempt. Anyone who asks about the menu without understanding it gets a withering answer. Publicly, the Founders' Day feast is simply his masterpiece." — line 162 (day-one)

> "- **Quirks:** He tastes everything before answering. One word from him and every knife rises." — line 163 ("every knife rises" is encounter; the day-one habit is "He tastes everything before answering")

> "- **Signature phrases:** \"Service!\" / \"The menu is not your concern.\" / \"Pests.\"" — line 164 (day-one; "Pests" is a habit)

> "- **Never:** He never serves a flawed dish, never discusses the feast's purpose, and never lets anyone in the kitchen uninvited." — line 165 (day-one)

> "- **Sample lines:**" — lines 166-169:
>   - *Greeting:* "Out of my kitchen. Guests eat in the hall." — line 167 (day-one)
>   - *Business:* "The Founders' Day menu is the finest work of my life. It is not your concern." — line 168 (day-one)
>   - *Under pressure:* "Pests." (every knife rises) — line 169 (encounter time)

Quest-time or encounter clauses in the profile, for the rule-16 restatement (none changed yet; the drafter will report changes): line 159 ("After discovery: calm, cold certainty"), line 163 ("every knife rises"), line 169 (*Under pressure* sample, "every knife rises").

---

## D. Conflicts

**D1. Stat block name: "Cult Fanatic" or "Cultist Fanatic"**
- Jandar page: "Stat block: **Cult Fanatic**." — `campaign/setting/notable-figures/cassalanters/09-jandar-chergoba.md:5`
- Seffia page: "Stat block: **Cultist Fanatic**." — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:7`
- Factions Guide: "**Seffia's Team.** Seffia Naelryke (**Cultist Fanatic**) + 2 **Spies** + 1 **Veteran** + 1 invisible **Imp**." — `campaign/guides/factions/11-cassalanters.md:17`
- Factions Guide, the Asmodean Shrine roster: "**Roster:** 1 **Cultist Fanatic** + 2 **Imps** (Area 1) | 1 **Apprentice Wizard** + 2 **Imps** (Area 2) | 2 **Cultist Fanatics** (Area 4)." — `campaign/guides/factions/11-cassalanters.md:45`
- Adventure: "Jandar is a male tiefling {@creature cult fanatic}." — `sources/adventure-wdh.json:18512`
- Alexandrian Lair, printed p.82 [PDF p.6] (transcription): "Jandar Chergoba (Head Chef) – tiefling cult fanatic, MM p. 345 (DH p. 117)"
- Order of the Gauntlet design notes (a stale line in another file, about Seffia): "- Seffia's page still lists this mission and gives her \"Cult Fanatic,\" the 2014 name." — `campaign/quests/faction-events/order-of-the-gauntlet/m02-the-black-viper-investigation/design-notes.md:27`
- Higher source: no campaign file settles the name for both figures. `CLAUDE.md` requires 2024 terminology. The Order note calls "Cult Fanatic" the 2014 name, and the Seffia page and the Factions Guide use "Cultist Fanatic". The drafter must choose one name for both pages.

**D2. How many knives Jandar animates**
- Adventure: "causing ten knives to magically rise from the counters and attack" — `sources/adventure-wdh.json:20256`
- Campaign structure doc: "a rack of knives he can animate on command (\"For'zaal\" — ten flying swords)" — `campaign/structure/arc-g-cassalanter-villa.md:199`
- Campaign location: "ten flying swords animate from the knife rack and attack on his direction" — `campaign/locations/cassalanter-villa/05-kitchen.md:19`
- Wiki (5e): "he could animate a dozen of kitchen [[knives]]" — wiki line 68
- Higher source: the campaign and the adventure (ten). The wiki's "a dozen" is the lowest-ranked source.

**D3. Why Jandar serves the cult: the debt, or "the craft that brought him to the Cassalanters' attention"**
- Jandar page: "and serve Asmodeus through the craft that brought him to the Cassalanters' attention." — `campaign/setting/notable-figures/cassalanters/09-jandar-chergoba.md:15`
- Structure doc: "Victoro holds a 3,000 gp obligation over him from a failed restaurant venture. The debt converted into cult service three years ago." — `campaign/structure/arc-g-cassalanter-villa.md:98`
- Organization page, Draft Notes: "**Conflicts:** Jandar's road to the cult. `arc-g-cassalanter-villa.md:98` says his debt \"converted into cult service three years ago\", and `09-jandar-chergoba.md:15` says he serves Asmodeus \"through the craft that brought him to the Cassalanters' attention\". Both are kept, since neither contradicts the other." — `campaign/setting/organizations/10-cassalanters.md:195`
- Higher source: the structure doc gives the debt; the page's line 15 is kept verbatim (ruling 3). Both can be true if the failed restaurant venture is the craft. The sources do not say so; a Background that joins them is `[research]`.

**D4. Whether his debt began the cult or came with the bargain**
- Structure doc: "The debt converted into cult service three years ago." — `campaign/structure/arc-g-cassalanter-villa.md:98`
- Organization page: "Jandar Chergoba's debt to Victoro turned into cult service three years ago, which places some of the cult's household recruiting at the time of the bargain" — `campaign/setting/organizations/10-cassalanters.md:27`
- Organization page, Draft Notes: "The cult's founding, the temple's conversion and when each member joined are undated in every campaign file, so the History entry for them carries `[research]`." — `campaign/setting/organizations/10-cassalanters.md:178`
- Adventure: no date for Jandar's cult service. "The head servants of Cassalanter Villa are members of the cult." — `sources/adventure-wdh.json:18467`
- Higher source: the structure doc. "three years ago" is the bargain year, 1489 DR by the campaign's count: "1489 DR: Neverember is deposed, the family is on the verge of bankruptcy, the pact is signed and Osvaldo is taken." — `campaign/setting/history/05-a-debt-in-blood.md:123`. The Background can state "three years ago" as day-one. A month or a join date is `[research]`.

**D5. The feast's date: Flamerule 1, or Tarsakh 9**
- Campaign, Organization: "On Founders' Day, Flamerule 1, the family plans to poison 99 guests at a feast" — `campaign/setting/organizations/10-cassalanters.md:130`
- Adventure: "{@creature Ammalia Cassalanter|WDH} hosts a grand party on Founders' Day" (`sources/adventure-wdh.json:22916`); the calendar line "Flamerule 1: Founders' Day" (`sources/adventure-wdh.json:31447`)
- Alexandrian Lair, printed p.79 [PDF p.3] (transcription): "**TARSAKH 9th – LEIRUIN FEAST**: This is the feast at which the Cassalanters poison 99 guests and perform the ritual necessary to save their children's souls (assuming they've managed to secure the gold from the Vault)."
- History page, Draft Notes: "- **Conflicts:** The Alexandrian files put the poisoning feast on Tarsakh 9 or 10 and the forfeit on Tarsakh 11 (`10. Lair Cassalanter Villa.pdf` p.79, `29. Addendum` p.225). The published adventure and this campaign use Flamerule 1 and Flamerule 11, and these win." — `campaign/setting/history/05-a-debt-in-blood.md:138`
- Higher source: the campaign and the adventure (Flamerule 1).

**D6. Jandar's location on Founders' Day**
- Adventure: "{@creature Jandar Chergoba|wdh|Jandar} isn't here. Instead, he's preparing Ammalia's {@condition poisoned} feast in a cooking pavilion out on the estate's sprawling lawn." — `sources/adventure-wdh.json:20263`
- Structure doc: "During Founders' Day: Jandar is outside on the lawn, preparing the feast." — `campaign/structure/arc-g-cassalanter-villa.md:199`
- Location: "**Founders' Day:** Jandar is outside on the lawn pavilion, preparing the charitable feast." — `campaign/locations/cassalanter-villa/05-kitchen.md:21`
- Alexandrian Lair, printed p.79 [PDF p.3] (transcription): "The only people left in the Villa during this time, beyond the Cassalanters themselves, are:" followed by "The guards", "Willifort Crowell" and "The imps guarding Osvaldo Cassalanter". Jandar is not on the list.
- No conflict among these. Recorded so the drafter knows the sources agree on the feast.

**D7. Whether his regalia and the Willifort regalia share the lockbox**
- Adventure, Jandar's box: "{@creature Jandar Chergoba|wdh}, the head chef, keeps his golden sacrificial dagger, golden mask, and crimson robes (see \"Cult of Asmodeus,\") in a locked iron box underneath a sack of potatoes." — `sources/adventure-wdh.json:20289`
- Willifort page: "and his regalia lies in the lockbox that he shares with Tissina." — `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:88`
- Wiki: "He kept it hidden in a lockbox, hidden underneath sacks of [[potato]]es in Cassalanter Villa kitchens." — wiki line 71
- Higher source: the adventure (Jandar's own iron box, under potatoes). The Willifort page's lockbox is a separate box shared with Tissina. No source says the two boxes are the same. The page must not put Jandar's regalia in Willifort's box.

**D8. Who knows what is behind the attic door**
- Structure doc: "The household staff knows the attic is forbidden. Only Willifort Crowelle — the doppelganger butler who serves Asmodeus directly — knows what is behind the door." — `campaign/structure/arc-g-cassalanter-villa.md:13`
- Organization: "Willifort knows." — `campaign/setting/organizations/10-cassalanters.md:129` (the GM Secret, part of the Osvaldo bullet)
- Jandar is household staff and a cult member. No source says whether he has seen the attic. The Organization page's family-level statement is "Victoro and Ammalia have told no one." — `campaign/setting/organizations/10-cassalanters.md:96`
- Result: no conflict on the page's facts. Recorded because a Background that mentions the attic must follow the structure doc's sentence.

---

## E. Stale lines in other files (not to be edited), and routed references

### E1. Stale or wrong lines in other files
- `campaign/setting/organizations/10-cassalanters.md:101`: "- **Jandar Chergoba** — Tiefling cult fanatic (Asmodeus), lawful evil. See the **Jandar Chergoba** page in Notable Figures." Not stale; the name used is the one in D1.
- `campaign/quests/faction-events/order-of-the-gauntlet/m02-the-black-viper-investigation/design-notes.md:27` calls the Seffia page's "Cult Fanatic" the 2014 name, which the Seffia page no longer uses. It concerns Seffia, not Jandar, and is listed for D1.
- `campaign/structure/arc-g-cassalanter-villa.md:199` says "(\"For'zaal\" — ten flying swords)". Consistent with the adventure.
- Wiki (5e) "a dozen" of knives: see D2. The wiki is the lowest rank.

### E2. Setting pages that touch him
- `campaign/setting/deities/asmodeus.md:72` (see A2).
- `campaign/setting/notable-figures/cassalanters/02-ammalia-cassalanter.md:47` (see A4).
- `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:39` and `:88` (see A2 and D7).
- `campaign/guides/factions/11-cassalanters.md:107`: "- Notable Figures: **Victoro Cassalanter**, **Ammalia Cassalanter**, **Willifort Crowelle**, **Seffia Naelryke**, **Arn Xalrondar**, **Tissina Khyret**, **Laiba \"Nana\" Rosse**, **Jandar Chergoba**, **Rella Asp**, **Ivrala Sorn**, **Osvaldo Cassalanter**, **Caladorn Cassalanter**"

### E3. Routed quest references (where the quest-time facts already live)
- Cassalanter Villa structure doc: `campaign/structure/arc-g-cassalanter-villa.md:98` (the DC and the "He provides" clause), `:199` (C10 room text, the Founders' Day state), `:251` (the knives' deactivation), `:107` (Fiorella), `:519` (the cult's motivations).
- C10 kitchen location journal: `campaign/locations/cassalanter-villa/05-kitchen.md:9`, `:17`, `:19`, `:21`.
- Area overview: `campaign/locations/cassalanter-villa/area-overview.md:40`.
- Adventure, C10 and the Founders' Day subsection: `sources/adventure-wdh.json:20243`-`:20265`, and the regalia box at `:20289`. The Cult Gathering: `sources/adventure-wdh.json:22818`. Day of the Damned (the feast): `sources/adventure-wdh.json:22916`-`:22918`.
- Alexandrian Lair, printed p.81 [PDF p.5] (transcription; roster): "Jandar Chergoba + 6 chefs" and "Area C10 – Kitchen". The roster's columns are read as images, so the rows are not aligned in the transcription.
- Alexandrian Lair, printed p.82 [PDF p.6] (transcription; stat reference): "Jandar Chergoba (Head Chef) – tiefling cult fanatic, MM p. 345 (DH p. 117)".
- Alexandrian Lair, printed p.79 [PDF p.3] (transcription; feast): "**TARSAKH 9th – LEIRUIN FEAST**" (see D5).

---

## F. Gaps (what a Background would need that no source gives)

Each gap lists the sourced facts the drafter must stay consistent with.

1. **Birth, family of origin, childhood, age and early life.** No campaign file, adventure line, Alexandrian PDF or wiki line gives any of them. The wiki's infobox leaves `ethnicity`, `age` and `dob` blank (wiki lines 16, 18, 23). Stay consistent with: "a male tiefling" (`sources/adventure-wdh.json:18512`); "He is often in the kitchen" (same line); "tiefling" (wiki line 15).
2. **The restaurant venture.** The only source is "a 3,000 gp obligation over him from a failed restaurant venture" (`campaign/structure/arc-g-cassalanter-villa.md:98`). No name, city, date or cause of failure is given. Stay consistent with: the debt is a 3,000 gp obligation, held by Victoro (same line); the debt "converted into cult service three years ago" (same line). Any name for the venture is `[research]` or `[design]` (brief ruling 17).
3. **How he met the Cassalanters, and when he first served them.** The structure doc says the debt is what brought him in (`arc-g-cassalanter-villa.md:98`), and the page says "the craft that brought him to the Cassalanters' attention" (`09-jandar-chergoba.md:15`). No source gives the first meeting. Stay consistent with: "three years ago" (same structure line).
4. **What he knows of the attic and of Osvaldo.** The structure doc says "Only Willifort Crowelle — the doppelganger butler who serves Asmodeus directly — knows what is behind the door." (`arc-g-cassalanter-villa.md:13`). Jandar is not named among those who know. The sources do not state whether he knows of the pact. Stay consistent with: "Victoro and Ammalia have told no one." (`campaign/setting/organizations/10-cassalanters.md:96`). Any statement that he knows of Osvaldo is `[research]` and contradicts the structure doc's "only Willifort" line.
5. **Whether he knows the twins' bargain or the poison's purpose.** The Organization page says Jandar "is the person who sees that the poison is distributed correctly" (`campaign/setting/organizations/10-cassalanters.md:130`). That is a day-one fact about his task. The only source line that limits a cult member's knowledge is about Nana Rosse: "She does not know about Osvaldo or the Founders' Day plan." (`campaign/structure/arc-g-cassalanter-villa.md:97`). For Jandar the sources are silent on what he understands of the poison's purpose. Mark any statement `[research]`.
6. **His feelings about the feast and the cult.** The structure doc says "He hates what he does." (`arc-g-cassalanter-villa.md:98`). The page's Emotions line says "controlled urgency on the days that matter" (`09-jandar-chergoba.md:13`). Stay consistent with both.
7. **"Retreats to a defensible position" (Morale).** No source gives it. The adventure's only fight line for Jandar is the "For'zaal" shout (`sources/adventure-wdh.json:20256`). The Morale line is kept verbatim (ruling 3) and tagged `[research]` by the drafter if it stays.
8. **Personal goals (brief ruling 17).** No source gives a personal want. The page's Motivations (`09-jandar-chergoba.md:15`) are faction-bound ("prepare the Founders' Day feast exactly as planned"). The structure doc gives one inner line: "He hates what he does." Constraints for any `[design]` goal (brief ruling 17): no change to the feast, the poison, the contract or any Event Outcome; no new named figure; no rescue, escape or betrayal plot that needs a new quest event. The "DC 12 Charisma (Persuasion)" turn at `arc-g-cassalanter-villa.md:98` is a quest mechanic, not a day-one fact.
9. **Religion before the cult.** No source says whether he was devout before the debt. Stay consistent with: "theological certainty" in his Emotions (`09-jandar-chergoba.md:13`). The structure doc's "true belief" is given for Willifort only (`arc-g-cassalanter-villa.md:519`).
10. **His skill with the knives and the rites.** The "For'zaal" command and the knives are sourced (`sources/adventure-wdh.json:20256`). The wiki says "Jandar possessed spellcasting abilities, appropriate for being a cultist of [[Asmodeus]]." (wiki line 68). The adventure gives him a stat block (cult fanatic), so any spellcasting follows the stat block. Stay consistent with the stat block name (D1).
11. **Family, friends or a place he cares about.** None in any source. The only named people near him are Fiorella (under him, `arc-g-cassalanter-villa.md:107`), Willifort and Tissina (co-keepers of order, `10-cassalanters.md:50`). Any named relative or place is `[design]` and must not name a new figure (brief ruling 17).

---

## G. Inner-life hints (exact quotes; for the Background and personal goals, brief ruling 17)

Each entry says whether the fact is day-one or quest-time. Quest-time facts are the heist's room text and the encounter text, and they must not be stated as day-one fact.

**Debt, grudge and what he wants to be free of**
> "bound by debt. Victoro holds a 3,000 gp obligation over him from a failed restaurant venture. The debt converted into cult service three years ago." — `campaign/structure/arc-g-cassalanter-villa.md:98` (day-one; the debt is the thing that holds him)
> "He hates what he does." — `campaign/structure/arc-g-cassalanter-villa.md:98` (day-one inner life; the same line gives the DC clauses, which are quest-time)

**Pride, the craft and the menu**
> "Deep down, the Founders' Day feast is the most important project of his career, and he has approached it with the same precision he brings to everything else." — `campaign/setting/notable-figures/cassalanters/09-jandar-chergoba.md:21` (day-one)
> "- **Personality in speech:** Professional pride and contempt. Anyone who asks about the menu without understanding it gets a withering answer. Publicly, the Founders' Day feast is simply his masterpiece." — `.claude/skills/character-voices/voices/cassalanters.md:162` (day-one)
> "*Business:* \"The Founders' Day menu is the finest work of my life. It is not your concern.\"" — `.claude/skills/character-voices/voices/cassalanters.md:168` (day-one; a sample line)

**Anxiety noticed by others**
> "- **Fiorella** (cook's assistant, human female, 20s) — works under Jandar. Has noticed Jandar's anxiety before specific nights and that he prepares food for \"private events\" she is never invited to attend." — `campaign/structure/arc-g-cassalanter-villa.md:107` (day-one; Fiorella's observation, non-cult)

**Contempt and standards**
> "**Emotions.** Jandar most often feels rigorous professional pride in the kitchen's standards, theological certainty carried without drama, the specific pleasure of a plan executed flawlessly, controlled urgency on the days that matter, and contempt for anyone who asks about the menu without understanding what the menu serves." — `campaign/setting/notable-figures/cassalanters/09-jandar-chergoba.md:13` (the page's own Emotions; no source line gives this wording)

**Loyalty to the cult's order**
> "- **Service Is Worship:** The cult's members fold devotion into the work they do for the family. Tissina Khyret attends Ammalia, Nana Rosse minds the twins, Jandar Chergoba cooks and Seffia Naelryke runs field operations, and none of them sees a conflict between the job and the god." — `campaign/setting/organizations/10-cassalanters.md:40` (day-one; the full bullet is quoted in A3)

**The kitchen as his place**
> "He speaks to his staff in clipped instructions, rarely looks up from whatever he is preparing, and does not welcome guests in this part of the house." — `campaign/locations/cassalanter-villa/05-kitchen.md:9` (room text; the day-one habit is this first part)
> "He does not abandon the kitchen before Founders' Day." — `campaign/setting/notable-figures/cassalanters/09-jandar-chergoba.md:23` (day-one; the page's own line)

**The poison he carries**
> "Jandar Chergoba, the villa's head chef, is the person who sees that the poison is distributed correctly." — `campaign/setting/organizations/10-cassalanters.md:130` (day-one, GM Secret)

**Quest-time inner-life lines (do not use as day-one facts)**
> "Jandar's animated knives (10 flying swords) activate on his command word \"For'zaal.\"" — `campaign/structure/arc-g-cassalanter-villa.md:251` (encounter)
> "If Jandar believes the characters are a threat, he shouts \"For'zaal,\" causing ten knives to magically rise from the counters and attack." — `sources/adventure-wdh.json:20256` (encounter; the trigger is the party)
> "If the party enters during kitchen hours, he pauses, sets down a knife, and says simply:" — `campaign/locations/cassalanter-villa/05-kitchen.md:9` (quest-time: the party in the kitchen)

**Binding limits from sources (facts a `[design]` goal must not contradict; these are facts, not design advice)**
- "Victoro holds a 3,000 gp obligation over him from a failed restaurant venture." (`campaign/structure/arc-g-cassalanter-villa.md:98`)
- "Jandar is the Cassalanter Villa's head chef, a cult fanatic, the keeper of golden sacrificial implements hidden under a sack of potatoes" (`campaign/setting/notable-figures/cassalanters/09-jandar-chergoba.md:25`) (the sentence continues: "and the person who determines whether the Founders' Day poison is distributed correctly.")
- "Jandar is a male tiefling {@creature cult fanatic}." (`sources/adventure-wdh.json:18512`)
- "Only Willifort Crowelle — the doppelganger butler who serves Asmodeus directly — knows what is behind the door." (`campaign/structure/arc-g-cassalanter-villa.md:13`)
- "Victoro and Ammalia have told no one." (`campaign/setting/organizations/10-cassalanters.md:96`)

---

## Not found

Terms and places searched:
- "Jandar", "Chergoba", "For'zaal", "Basta" across `/home/user/waterdeep` (Grep, content mode). Hits in `campaign/`, `sources/adventure-wdh.json` and `sources/research/` are listed above.
- The Alexandrian appendices `sources/Appendix_B_-_Player_Factions.md`, `sources/Appendix_C_-_Player_Faction_Missions.md` and `sources/Appendix_D_-_Running_the_Tavern.md`: no hit for "Jandar" or "Chergoba" in any of them (a search of all `sources/*.md` files for the names returned Seffia hits in Appendix C and D only).
- "Jandar" in `campaign/quests/` (no hits), `campaign/setting/history/` (no hits), `campaign/setting/villains/cassalanters.md` (no hits), `campaign/guides/trollskull-manor/` (no hits), `campaign/guides/gm-guide/running-the-villains.md` (no hits).
- "Jandar" in the wiki bundles `sources/research/pass4-bundles/cassalanters/wiki.txt` and `sources/research/pass5-bundles/` (no hits in any wiki file; hits only in the campaign-hits and adventure-hits files of the bundles).
- The wiki page for Jandar: only the scratchpad extract. It is quoted above.
- Jandar's birth, age, family, origin and the restaurant venture's name: none in any file read (see F1 and F2).
- "Jandar" in `sources/SOURCE_GUIDE.md`: not seen in the Grep output (the search was for Cassalanter, Seffia, Jandar, Windmill and the Stone terms, capped at 60 lines). The Cassalanter Villa chapter line (SOURCE_GUIDE line 31) names "Willifort Crowelle (doppelganger butler)" and not the head chef.
- The Alexandrian Lair text on the kitchen beyond the roster and stat reference (printed pp.79-82): none beyond the entries quoted.

## Not readable

- `sources/Other remix files/Cassalanters, their tragic backtstory, and Endgame setup.docx` (SOURCE_GUIDE line 687: "Victoro & Ammalia backstory, the soul-pact timeline, the children's situation, endgame resolution paths"). Not opened (`.docx`, no tool). It is not known to name Jandar. Name it for the orchestrator to extract and search for "Jandar".
- `sources/Other remix files/The Waterdavian's Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx` (SOURCE_GUIDE line 695: "Broad NPC reference — use as a secondary source"). Not opened. It may hold NPC notes for the cast. Name it for extraction.
- `sources/10. Lair  Cassalanter Villa.pdf` and `sources/5. Faction Outposts.pdf`: read as images (no `pdftotext`). Transcriptions above; check before prose use.

## Not run

- `voicecheck.py` was not run (research only).
- The page was not written. No file was edited except this notes file.
