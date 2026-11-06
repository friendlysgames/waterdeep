# Batch G research: Mask, Bhaal, Loviatar, Talona, Talos (Deities Pass 2)

Brief: `docs/plans/setting-compendium-pass2-brief.md` ("Researcher report (per power)"). Model page: `campaign/setting/deities/asmodeus.md`.
Bundles: `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/{mask,bhaal,loviatar,talona,talos}/` (`5etools.md`, `wiki.txt`, `campaign-hits.txt`, `adventure-hits.txt`).
Targeted Grep: `campaign/`, `sources/adventure-wdh.json`, `sources/adventure-wdmm.json`, with aliases. The Alexandrian PDFs and `sources/SOURCE_GUIDE.md` were not read, per instruction. `docs/` was not used.

## Conventions

- **Wiki quotes.** `[[ ]]` link markup is dropped. Piped links show only the text after the pipe. All other wiki markup (`{{ }}` templates, `<ref>` tags, `<br />`) is kept as written. Line numbers are `wiki.txt` lines.
- **Editions.** FRHoF is Forgotten Realms: Heroes of Faerûn (current canon). PHB and SCAG entries are 2014 sources. Wiki facts are tagged with the book that the wiki's own `<ref>` cites.
- **Quote format.** Each quote is a whole line or paragraph, copied exactly. Consecutive lines from one block are grouped under one heading, and each line keeps its own number.
- **Bundle gaps.** The Mask `campaign-hits.txt` misses the two "Shadowmasters" rows. The Talos `adventure-hits.txt` is empty, but a targeted Grep found the Malyk line at `sources/adventure-wdmm.json:30762`.

## Major Temples of Waterdeep (`sources/adventure-wdh.json`)

Caption:
> "caption": "Major Temples of Waterdeep", — `sources/adventure-wdh.json:30910`

The rows run from line 30921 to line 30996. None of the five powers has a row. The only generic row is "All deities" / "Holyhands House" / "North Ward" (lines 30922–30926), which names none of them.

---

## 1. Mask

### Field 1: Identity

FRHoF entry (`5etools.md`, lines 1–5):
> "## Mask | source FRHoF p.115 | pantheon Faerûnian" — `5etools.md:1`
> "- altNames: ['The Lord of Shadows', 'The Master of All Thieves']" — `5etools.md:2`
> "- title: God of thieves" — `5etools.md:3`
> "- worshipers: Assassins, Rogues, thieves, tricksters" — `5etools.md:4`
> "- plane: Hades (Niflheim)" — `5etools.md:5`

PHB entry (`5etools.md`, lines 14–18):
> "## Mask | source PHB p.294 | pantheon Forgotten Realms" — `5etools.md:14`
> "- title: God of thieves" — `5etools.md:15`
> "- alignment: ['C', 'N']" — `5etools.md:16`
> "- domains: ['Trickery']" — `5etools.md:17`
> "- symbol: Black mask" — `5etools.md:18`

SCAG entry (`5etools.md`, lines 22–27):
> "## Mask | source SCAG p.21 | pantheon Faerûnian" — `5etools.md:22`
> "- altNames: ['The Lord of Shadows', 'The Master of All Thieves']" — `5etools.md:23`
> "- title: God of thieves" — `5etools.md:24`
> "- alignment: ['C', 'N']" — `5etools.md:25`
> "- domains: ['Trickery']" — `5etools.md:26`
> "- symbol: Black mask" — `5etools.md:27`

Wiki, 5e fields (the wiki cites SCAG p.21,33 and PHB5e p.62–63):
> "| power5e             = God" — `wiki.txt:34`
> "| alignment5e         = Chaotic Neutral" — `wiki.txt:35`
> "| symbol5e            = Black mask" — `wiki.txt:36`
> "| portfolio5e         = Thieves" — `wiki.txt:41`
> "| domains5e           = Trickery" — `wiki.txt:42`
> "| worshipers5e        = Spies, thieves" — `wiki.txt:43`

Wiki, adjective and aspects:
> "| adjective           = Maskarran<ref name="F&A-p111">{{Cite book/Faiths & Avatars|111}}</ref>" — `wiki.txt:9`
> "| aspects             = Veldraeos<ref name="PftF-p54">{{Cite book/Prayers from the Faithful|54}}</ref><br />Ondoum<ref name="PftF-p54"/>" — `wiki.txt:10`

Wiki, lead paragraph (the lead cites Faiths & Avatars pp.109–112; the rank by edition is in the infobox: 2e at `wiki.txt:80`, 1e at `wiki.txt:94`):
> "'''Mask''' ({{Pronounce|MASK|audio=Mask.ogg|refs=<ref>{{Cite book/FRCS|246}}</ref><ref name="FP-p45-47" />}}) was the intermediate god of shadows, thievery, and formerly intrigue in the Faerûnian pantheon, a loner god most often associated with those of ill-repute. The '''Lord of Shadows'''  was a chaotic neutral or neutral evil deity symbolized with a velvet black mask tainted with red.<ref name="F&A-p109-112" />" — `wiki.txt:109`

The wiki title list on line 8 also gives "The Shadowlord", "God of Thieves", "Blackheart", and the derogatory "Shadowflea" and "Shadowcrab". Those names are at `wiki.txt:8`.

### Field 2: Edict or core tenet

No edict appears in 5etools or in the wiki infobox.

> "The church of Mask stated that wealth rightfully belonged to those who could acquire it. Honesty was for fools but apparent honesty was a very valuable thing, and subtlety was everything.<ref name="F&P-p110">{{Cite book/Faiths & Avatars|110}}</ref>" — `wiki.txt:141` (wiki cites Faiths & Avatars p.110)

> "Mask's faithful were led to believe that the god saw everything that happens in the dark and to trust it, as one would be made an easy target by walking into plain light. The abilities to deceive, as truth was a foolish virtue and manipulation was better than brute force, and to be dextrous were also appreciated. Whilst the faith advocated for accumulating riches, it also said to only steal what was necessary. They also believed that owning something simply required being in possession of it.<ref name="FRA-26" />" — `wiki.txt:158` (wiki cites Forgotten Realms Adventures p.26)

> "Those who favor Mask practice thievery and try to acquire what belongs to others, engaging in pickpocketing, burglary, mugging, and con games. Ordinary folk pray to him so he'll avert his eyes from their valuables, but cautious individuals employ "Mask's purse," a small, cheap cloth pouch worn in plain sight containing a small offering of coin. By convention, a pickpocket pilfers Mask's purse when encountering another person wearing one and considers it a gift from the god, while the one who lost the purse is grateful to Mask for accepting this respectful sacrifice. Of course, nothing prevents another pickpocket from targeting someone who has lost Mask's purse, and anyone with the ill luck to attract multiple pickpockets in a single outing has probably earned Mask's ire anyway." — `5etools.md:9` (FRHoF)

### Field 3: Portfolio and areas of concern

> "Mask is a trickster god, the patron of ne'er-do-wells, spies, and thieves. All that occurs within shadow is in the purview of Mask. People whisper a prayer to Mask whenever stealth is required or intrigue is afoot. Courtiers and diplomats invoke Mask's name in hope of a smooth negotiation." — `5etools.md:7` (FRHoF)

> "| portfolio3e         = Shadows, thievery, thieves" — `wiki.txt:71` (3e)
> "| portfolio2e         = Thieves, thievery, shadows" — `wiki.txt:87` (2e)
> "| portfolio1e         = Thieves, intrigue" — `wiki.txt:101` (1e)

> "Known for his constant scheming, cool head, and oft-reserved mocking comment, Mask lost a significant portion of his power, the intrigue portfolio, to Cyric. This, of course, led to two things: an enduring hatred of Cyric, and the Lord of Shadows training himself to be more direct than he was in his prior, elaborate plots.<ref name="FRCS3e-p246" />" — `wiki.txt:118` (wiki cites Forgotten Realms Campaign Setting 3e p.246)

### Field 4: Worship (clergy, holy days, temples, omens, messengers)

**Waterdeep first.** The published Waterdeep adventure has one Mask observance: a holiday in the city's celebrations. It is not a temple.

> "At many times of year, hardly a tenday can pass in Waterdeep without the staging of some rite, race, or rousing ceremony of civic pride. Here I briefly summarize the most widely celebrated events on the calendar, from the first of Hammer to the last of Nightal." — `sources/adventure-wdh.json:31350` (the section is "City Celebrations", line 31346)

> "name": "Marpenoth 30: Liar's Night", — `sources/adventure-wdh.json:31541`
> "This holy day pays tribute to Leira and Mask. To placate those deities and ward away their attention, folk of all walks of life don masks and costumes (magical or mundane) to disguise themselves and play at being other than what they are. Commonly seen mask styles include the black mask symbol of Mask and the mirror face of the priests of Leira. But there are no bounds on the disguise you don, and the more elaborate and outlandish it is, the more celebrated the wearer." — `sources/adventure-wdh.json:31545`

Clergy (FRHoF):
> "Priests of Mask are thieves by profession and serve as higher-ups in the local underworld or a criminal syndicate. They go by the title of demarche and wear veil-masks when acting in their priestly capacity." — `5etools.md:10`

Clergy (wiki):
> "The Clergy of Mask were called Maskarrans, with elite specialty priests referred to as demarchesses ({{pronounce|deh|mar|KESS|es}}) if female, and demarchs ({{pronounce|deh|MARKS}}) if male.<ref name="F&P-p110" /> Maskarrans addressed each other as "Brother/Sister Shadow", no matter their rank. Clergy that completed an especially dangerous heist or complex act of manipulation were often admitted to the Circle of the Gray Ribbon.<ref name="F&P-p110" />" — `wiki.txt:143`

Temples (FRHoF; the House of Shadow is in Telflamm, Thesk, not Waterdeep):
> "The foremost organization serving Mask is the Shadowmasters of Telflamm, a criminal syndicate in the land of {@book Thesk|FRHoF|2|Thesk}. The Shadowmasters are based at Mask's largest temple, the House of Shadow, in Telflamm, but they also maintain safe houses throughout Thesk." — `5etools.md:11`

Temples (wiki, general; names no city):
> "Mask's priesthood had operated independently across cities and regions. This decentralization had served to protect temples and guilds from collective retaliation—ensuring that actions taken against one enclave did not endanger others. In regions dominated by a single thieves' guild, temples or shrines dedicated to Mask had often been linked to the guild hall via hidden underground tunnels. In larger cities with rival guilds, Mask's temple had typically been located in a subterranean space, recognized by all factions as neutral ground.<ref name="FRA-26" />" — `wiki.txt:153`

Messengers (FRHoF):
> "Mask takes the form of a quick masculine being wielding two shadowy blades, his identity hidden by a mask. Sometimes he takes the form of masks that others might wear. When he speaks to his followers, he does so by claiming a mask as his temporary face, or he sends a living shadow (Neutral Evil {@creature Shadow Demon|XMM})." — `5etools.md:8`

Chosen (FRHoF): "Chosen of Mask are master thieves, manipulative spies, and assassins who rarely walk in the light." — `5etools.md:12`

Holy days beyond Liar's Night, and omens: none sourced (Field 7).

### Field 5: Relations with other powers, and origin or rise

Wiki, edition tags as cited by the wiki's refs.

> "Simply put, Mask was a loner and unlike other deities he enjoyed his own company greatly.<ref name="FRCS3e-p246" /><ref name="TEV" /> However, before this, he had frequent alliances with Bane. If nothing else, their sizable hatred of Cyric gave them common ground in addition to their history of working together. Mask was also at direct odds with Waukeen, the goddess of merchants and honest trade. All guardians of light, knowledge, and duty were opposed to him. This included Selûne, whose light tended to reveal his own faithful whilst they worked.<ref name="FRCS3e-p246" />" — `wiki.txt:129` (wiki cites Forgotten Realms Campaign Setting 3e p.246)

> "He was allied with the drow god of thievery Vhaeraun.<ref name="DD-36">{{Cite book/Demihuman Deities|36}}</ref> The relationship itself was businesslike.<ref name="FaP-114">{{Cite book/Faiths and Pantheons|114}}</ref> However, Mask planned to compensate what he lost to Cyric with Vhaeraun's divinity,<ref name="LoD-29">{{Cite book/Lords of Darkness|29}}</ref> while Vhaeraun used the similarity between their symbols to recruit half-elves and humans into his church of Vhaeraun.<ref name="DD-38">{{Cite book/Demihuman Deities|38}}</ref> The two were often confused with one another among non-drow on the surface.<ref name="DD-37">{{Cite book/Demihuman Deities|37}}</ref> They also shared one very similar title, Mask's "Lord of Shadows"<ref name="FaP-45">{{Cite book/Faiths and Pantheons|45}}</ref> and Vhaeraun's "Lord of Shadow".<ref name="DDG-93">{{Cite book/Drizzt Do'Urden's Guide to the Underdark|93}}</ref>" — `wiki.txt:137` (wiki cites Demihuman Deities, Faiths and Pantheons, Lords of Darkness, and Drizzt Do'Urden's Guide to the Underdark)

> "During the Time of Troubles of 1358 DR, Mask took the shape of a powerful blade called Godsbane.<ref name="F&A-p109-112" /> He eventually came to be wielded by the then-mortal Cyric; he acquired the sword by stealing it from a halfling named Sneakabout,<ref name="FRE3-p10">{{Cite book/Waterdeep (adventure)|8,10}}</ref><ref name="Wd-c3">{{Cite book/Waterdeep|52-52|3}}</ref> who in turn had killed the former wielder of the sword.<ref name="Wd-c14">{{Cite book/Waterdeep|257-263|14}}</ref>" — `wiki.txt:162` (the three Waterdeep references are book citations, not text about the city; see Answers 3)

> "In the {{YearlinkName|1374}}, Mask relinquished his divinity and his life over to Shar to repay a millennia-old debt to the goddess, who was revealed to be his "mother" as well as the person he served as a herald. Just before his death, Shar revealed Mask's true name as Lessinor, though its origin (either as a mortal name or a birth name) was not explained. A portion of Mask's divinity—the portion stolen by Kesson Rel—was absorbed in equal portions by Erevis Cale, Drasek Riven, and Prince Rivalen of the Shade enclave. Erevis then sacrificed himself to Mephistopheles, the archdevil Lord of Cania, in payment for releasing the half of the soul of Magadon that he ate; Mephistopheles in turn absorbed the portion of Mask's divinity held by Cale.<ref name="Shadowrealm" />" — `wiki.txt:167` (wiki cites the Shadowrealm source)

### Field 6: Campaign and published-adventure mentions

The bundle's `campaign-hits.txt` lists three lines: `campaign/setting/villains/cassalanters.md:16`, `campaign/structure/ch2-city-of-splendors.md:270`, and `campaign/setting/notable-figures/manshoons-zhentarim/11-kaevja-cynavern.md:22`. None names the god. My targeted Grep agrees on those three and adds two "Shadowmasters" rows that the bundle does not list.

Campaign, "Mask" used for something else (noise):
> "| 2 | The Desperate Parents | Acts II–III | Mask off; they did it and they've lived with it; Ammalia holds steady, Victoro is starting to fracture |" — `campaign/setting/villains/cassalanters.md:16` (identical text at `campaign/structure/ch2-city-of-splendors.md:270`, a retired file)

> "**Persona.** To the world — specifically to anyone who has breached E2 and triggered the Mask discharge — Kaevja is the mage at E3, already reaching for her component pouch. To Manshoon, she is the sanctum's most reliable early-warning mechanism, valued more for the sending she can cast than for the spells she throws in combat. Deep down, she serves Manshoon because he is the most capable operator she has encountered, and working for the most capable operator available is, in her estimation, the rational choice until demonstrated otherwise." — `campaign/setting/notable-figures/manshoons-zhentarim/11-kaevja-cynavern.md:22` ("Mask discharge" is a device, not the god)

Campaign, the Shadowmasters (a different name, which the campaign does not link to Mask):
> "| Shadowmasters Exile | Strong | Your old underworld connections still have reach into Waterdeep's black market. |" — `campaign/guides/players-guide/character-creation.md:62`

> "| Shadowmasters Exile | Strong | Criminal underworld connections; the Shadowmasters have reach into Waterdeep's black market |" — `campaign/structure/ch1-beginning.md:122` (retired file)

Published adventure, Waterdeep: the holiday quoted in full in Field 4 (`sources/adventure-wdh.json:31545`).

Published adventure, Undermountain (names Mask as the god):
> "Yoastal can be both friend and foe to an adventuring party. The ghost claims to have once been a cleric of Mask, cursed to remain in Slitherswamp until the nagas are destroyed. She provides characters with the layout of the level in exchange for promises to free her. But her information is always slanted toward leading the characters into situations that might further escalate the war between the Ssethian Scourges and the Blacktongues." — `sources/adventure-wdmm.json:23786`

Published adventure, noise (the word is not the god):
> "name": "Tyrant's Mask", — `sources/adventure-wdh.json:30260` (an item name)

> "Lady Alathene appeared in open court and asked the Lords of Waterdeep to strip her brother of his title and banish him from the city. She also presented evidence of her brother's numerous crimes, including slavery, arson, theft, and murder. The Lords ordered the immediate capture of the Dark Ranger, but by the time the City Watch had breached the gates of his villa, Vanrak and his followers had already fled through a secret portal into Undermountain. He and his followers remained there until, in the Year of the Dark Mask (1171 DR), they conquered the level of Undermountain that came to be known as Vanrakdoom." — `sources/adventure-wdmm.json:48609` (a year name)

Count: campaign, 5 lines use "Mask". Three use it in another sense (`cassalanters.md:16`, `ch2:270`, `11-kaevja-cynavern.md:22`), and two name the Shadowmasters. Adventures, 4 lines use "Mask". Two name the god (`wdh:31545`, `wdmm:23786`), and two do not (`wdh:30260`, `wdmm:48609`).

The line at `sources/adventure-wdmm.json:30762` (Talos Field 6) also names "Vhaeraun (god of thieves)" as a fountain statue. Vhaeraun is the wiki's drow thieves' god, allied with Mask (`wiki.txt:137`).

### Field 7: Conflicts and not found

Conflicts:
- Status. The wiki's 5e rank is "God" (`wiki.txt:34`). Its 4e rank is:
> "| power4e             = Dead power" — `wiki.txt:49`
- The history says he gave up his divinity in 1374 DR (`wiki.txt:167`). FRHoF lists him as a current god (`5etools.md:1`, `5etools.md:3`).
- The Shadowmasters. FRHoF says the Shadowmasters of Telflamm are Mask's syndicate in Thesk (`5etools.md:11`). The campaign's "Shadowmasters" are in Waterdeep (Field 6). The campaign does not link them to Mask, and the two should not be linked without a source.

Not found:
- No Mask temple, shrine, or holy place in Waterdeep, in the Major Temples table, or in the campaign.
- No omens sourced for Mask.
- No campaign NPC, faction, or quest that names the god.
- No wiki text about Waterdeep. The only Waterdeep lines are citation markup (`wiki.txt:162`).

### Answers (1)–(3)

1. **Waterdeep temples or shrines, and ward.** None. The Major Temples table has no Mask row (`sources/adventure-wdh.json:30910`). The one Waterdeep observance is the holiday (`sources/adventure-wdh.json:31545`), which has no ward or temple.
2. **Campaign use.** No campaign file uses this power. The Shadowmasters rows are a background feature, not Mask.
3. **Wiki lines that mention Waterdeep.** `wiki.txt:162` only, and only in citation markup ("Waterdeep (adventure)" and "Waterdeep" book cites). On the thieves' guilds, the wiki says only in general terms that Mask's temples were linked to guild halls or sat in neutral subterranean space (`wiki.txt:153`). It does not name Waterdeep or its guilds.

---

## 2. Bhaal

### Field 1: Identity

FRHoF (`5etools.md`, lines 1–5):
> "## Bhaal | source FRHoF p.103 | pantheon Faerûnian" — `5etools.md:1`
> "- altNames: ['The Lord of Murder']" — `5etools.md:2`
> "- title: God of murder" — `5etools.md:3`
> "- worshipers: Assassins, murderers" — `5etools.md:4`
> "- plane: Gehenna (Khalas)" — `5etools.md:5`

PHB (`5etools.md`, lines 13–17):
> "## Bhaal | source PHB p.294 | pantheon Forgotten Realms" — `5etools.md:13`
> "- title: God of murder" — `5etools.md:14`
> "- alignment: ['N', 'E']" — `5etools.md:15`
> "- domains: ['Death']" — `5etools.md:16`
> "- symbol: Skull surrounded by a ring of blood droplets" — `5etools.md:17`

SCAG (`5etools.md`, lines 21–26):
> "## Bhaal | source SCAG p.21 | pantheon Faerûnian" — `5etools.md:21`
> "- altNames: ['The Lord of Murder']" — `5etools.md:22`
> "- title: God of murder" — `5etools.md:23`
> "- alignment: ['N', 'E']" — `5etools.md:24`
> "- domains: ['Death']" — `5etools.md:25`
> "- symbol: Skull surrounded by ring of bloody droplets" — `5etools.md:26`

Wiki, title and aspects:
> "| title               = Lord of Murder<ref name="HoF-p103">{{Cite book/Forgotten Realms: Heroes of Faerûn|103}}</ref><ref name="SCAG5e-p21,27" /><ref name="FRCS.CotR-p10">{{Cite book/Forgotten Realms Campaign Set/Cyclopedia of the Realms|10}}</ref><br/>Dread Lord<ref name="dod">{{Cite game/Neverwinter Nights: Darkness over Daggerford}}</ref>" — `wiki.txt:10`
> "| aspects             = Bale<ref name="EE:CM-p23">{{Cite book/Elminster's Ecologies/The Cormyrean Marshes|23}}</ref><br /> Niynjushigampo<ref name="TH-p57">{{Cite book/The Horde/Volume I|57}}</ref><br/>" — `wiki.txt:12`

Wiki, 5e status:
> "| power5e             = Quasi-deity<ref name="BG.DiA-p231">{{Cite book/Baldur's Gate: Descent into Avernus|231}}</ref><br/>{{Former}} Deity<ref name="scag-p21,23,27">{{Cite book/Sword Coast Adventurer's Guide|21,23,27}}</ref>" — `wiki.txt:43`

Wiki, 5e stats:
> "| portfolio5e         = Murder" — `wiki.txt:50`
> "| domains5e           = Death" — `wiki.txt:51`
> "| worshipers5e        = Assassins, compulsive killers" — `wiki.txt:52`

Wiki, lead paragraph:
> "'''Bhaal''' ({{Pronounce|BAWL|refs=<ref name="BG.DiA-p4">{{Cite book/Baldur's Gate: Descent into Avernus|4}}</ref>}} {{Pronounce|BAHL|alt=yes|refs=<ref name="F&A-pp44-45">{{Cite book/Faiths & Avatars|44-45}}</ref>}} {{Pronounce|beh|HAHL|alt=yes|audio=Bhaal.ogg|refs=<ref name="FRCS.CotR-p10" />}}), known as '''Niynjushigampo''' among his Gugari worshipers,<ref name="TH-p57" /> was the widely feared '''Lord of Murder''', the Faerûnian god of violence and ritualistic killing.<ref name="F&A-pp44-45" />" — `wiki.txt:125`

### Field 2: Edict or core tenet

> "Bhaal is a god of murder who revels in violence and ritualistic killing. He lends power to those whose slaughters invoke fear and dread. The act of murder is only half the equation. The second half is the suspicion, paranoia, and fear that a seemingly unstoppable killer can evoke. Bhaal inspires fear by slaying those seemingly beyond the reach of death. He is a member of a trio of deities known as the Dead Three alongside Bane and Myrkul." — `5etools.md:7` (FRHoF)

> "The clergy of Bhaal in Faerûn were known as Bhaalists or Bhaalyn, the latter being used more commonly in the lands east of the Dragon Reach. Together they were a disorderly network of local hierarchies,<ref name="F&A-pp44-45" /> with the urban and rural branches maintaining distant relations from one another. Collectively, they believed that murder was both a duty to their god and a game for their enjoyment. Each cleric of Bhaal was expected to perform at least one murder every tenday, in the darkest moment in the dead of night.<ref name="F&A-p46">{{Cite book/Faiths & Avatars|46}}</ref>" — `wiki.txt:153` (wiki cites Faiths & Avatars p.46)

> "The folk of Faerûn don't normally pray to or acknowledge Bhaal. He is seen as a deeply evil and destructive deity who hungers for death - meaning the death of any sentient beings through unlawful means." — `5etools.md:28` (SCAG)

### Field 3: Portfolio and areas of concern

> "| portfolio3e         = Assassination, murder, violence, death (especially violent or ritual death)" — `wiki.txt:79` (3e)
> "| portfolio2e         = Death, murder, ritual death" — `wiki.txt:94` (2e)

> "Upon Jergal's suggestion, the three divided his power, deciding how to divide it based on the outcome of a game. The three played a game of knucklebones, and Bane emerged as the victor. He claimed the domains of hatred, strife and tyranny as his own. Myrkul, coming second, chose rule over the dead, the ultimate fate for all of Bane's minions. Finally, Bhaal chose the divine province of death.<ref name="F&A-p37" />" — `wiki.txt:163` (wiki cites Faiths & Avatars p.37)

### Field 4: Worship (clergy, holy days, temples, omens, messengers)

Waterdeep: none (Answers 1).

> "Murder cults of Bhaal have arisen in the past, each led by a charismatic, self-styled priest of Bhaal, but organized worship of the Lord of Murder is extremely uncommon. Temples and shrines are similarly rare. Those who erect a shrine to Bhaal usually do so to thank him for a successful murder. Such shrines feature a skull or a severed head surrounded by drops of blood (both from the murdered victim). As with the other members of the Dead Three, Bhaal's cult has infiltrated {@book Baldur's Gate|FRHoF|2|Baldur's Gate} on the {@book Sword Coast|FRHoF|2|Sword Coast}, where a vast temple to the Lord of Murder is said to brood in the tunnels beneath the city." — `5etools.md:10` (FRHoF; the only city this line names for a temple is Baldur's Gate)

> "While the folk of Faerûn don't normally pray to Bhaal, some propitiate him when they want to commit murder. A person might have an understandable reason to resort to murder, such as when they're unable to redress an injustice through lawful means, but it's far more common for prayers to Bhaal to be uttered by murderers motivated by jealousy, greed, or wrath. It's rare for anyone but assassins or compulsive killers to take Bhaal as a patron." — `5etools.md:9` (FRHoF)

> "Bhaal always carries a red handkerchief somewhere on his manifested form. He can take on an alternate appearance regardless of his current form: a hulking figure armed with a long, curved dagger that drips blood. In this hairless form, he wears only a tattered loincloth and is covered with bleeding wounds caused by a blade. His face is a skull flayed of its flesh and surrounded by a halo of blood. When he sends emissaries to carry his word, he usually tasks a {@creature Doppelganger|XMM} in the guise of someone the recipient later learns was dead during the conversation, or he sends a vicious {@creature Mezzoloth|XMM}." — `5etools.md:8` (messengers, FRHoF)

> "Chosen of Bhaal are blood-soaked terrors with little or no capacity for empathy. Their divine gifts hone their killing skills to a razor's edge." — `5etools.md:11` (FRHoF)

> "| holy days2e         = Feast of the Moon" — `wiki.txt:98` (2e; wiki cites Faiths & Avatars pp.44–45)

> "During the time that he was dead, Bhaal had many scattered cultist groups, the most infamous being the Deathstalkers of Bhaal,<ref name="F&A-p47">{{Cite book/Faiths & Avatars|47}}</ref> who attempted to bring him back to life. For a while after the Bhaalspawn crisis, it was believed his essence had been locked away on the Upper Planes, preventing his resurrection permanently. However, this proved to be incorrect. Bhaal's essence had been preserved in his half-mortal children, the Bhaalspawn, and after the death of the last two Bhaalspawn,<ref name="MiBG-CG-p3" /> Bhaal was revived.<ref name="SCAG5e-p17" />" — `wiki.txt:156`

Omens: none sourced.

### Field 5: Relations with other powers, and origin or rise

> "A wholly evil, debased and sadistic god, Bhaal was reviled by a majority of the pantheon; his divine foes included Chauntea, Helm, Ilmater, Lathander, Lliira and Tyr. Bhaal was served by the goddesses Talona and Loviatar,<ref name="F&A-pp44-45" /> and he in turn served Bane.<ref name="F&A-p36">{{Cite book/Faiths & Avatars|36}}</ref>" — `wiki.txt:144` (wiki cites Faiths & Avatars pp.44–45 and p.36)

> "Before his ascension to godhood, Bhaal was a power-hungry adventurer on Toril. Along with his companions Bane and Myrkul Bey al-Kursi, he sought to attain the portfolio of the God of the Dead Jergal. After defeating one of the Seven Lost Gods, the three were able to travel to Jergal's domain, the Castle of Bone in the Gray Waste. Upon their arrival, Jergal willingly offered his realm to the Dark Three, though they couldn't decide amongst themselves who would rule.<ref name="F&A-p37" /><ref name="LEoF-p41" />" — `wiki.txt:161` (wiki cites Faiths & Avatars p.37 and Lost Empires of Faerûn p.41)

> "On Eleint 16, in the {{YearlinkName|1358}}, having lost his powers and being forced to walk Faerûn like the rest of the gods, Bhaal was slain by the upstart mortal Cyric using the avatar of Mask, a sword named ''Godsbane.'' In doing this, Cyric stole Bhaal's divinity and portfolio elements.<ref name="LEoF-p42" /> However, much like Myrkul—who invested his divine essence in the artifact known as the ''Crown of Horns''—Bhaal was not utterly removed from Faerûn. Part of his divinity remained in the Winding Water, around Boareskyr Bridge where he was slain, his blood having flowed into the river.<ref name="F&A-pp44-45" /> More importantly, Bhaal foresaw his death and impregnated many mortal women, creating his heirs, the Bhaalspawn.<ref name="LEoF-p42" /> The Bhaalspawn were involved in a series of conflicts along the Sword Coast, with one standing above the others and ultimately foiling Bhaal's plan to return through his children.<ref name="BGII.ToB" />" — `wiki.txt:170` (wiki cites Lost Empires of Faerûn p.42, Faiths & Avatars pp.44–45, and Baldur's Gate II: Throne of Bhaal). The Mask link is in this line: Cyric used Mask's avatar.

> "With all of his children dead, all of Bhaal's essence was freed, allowing for his resurrection. Bhaal was revived, and reclaimed the murder domain from Cyric.<ref name="SCAG5e-p17">{{Cite book/Sword Coast Adventurer's Guide|17}}</ref> However, the Lord of Murder was no longer a true deity, and was instead a being of quasi-divine status. As with Bane and Myrkul, he was effectively a mortal.<ref name="BG.DiA-p231" /> In 1492 DR, the city of Baldur's Gate saw a spate of murders by cultists of the Dead Three.<ref name="BG.DiA-p11">{{Cite book/Baldur's Gate: Descent into Avernus|11}}</ref>" — `wiki.txt:178` (wiki cites SCAG 5e p.17, Descent into Avernus p.231, and Descent into Avernus p.11)

### Field 6: Campaign and published-adventure mentions

Campaign: none. The Grep for "Bhaal", "Bhaalist", "Bhaalspawn", "Lord of Murder", "Dead Three", and "murder cult" found no campaign line, and `campaign-hits.txt` is empty.

Published adventure, Waterdeep (the only Bhaal line in the Waterdeep adventure, in a history passage, not a temple):
> "When the gods walked among mortals during the Time of Troubles, they were cast down to the world by the mysterious Overgod Ao in 1358 DR. Until then, none but the gods had known of Ao's existence, and since then, we have learned little more. As all know, the crisis began with the theft of the Tablets of Fate by the vile and ambitious gods Bane and Myrkul, later joined by Bhaal. These mystic artifacts supposedly determine the extent of the gods' power, and dictate how they use that power. As punishment for this affront, Ao cast down the gods (or the ones that humans worshiped, at any rate) and then demanded that they return the tablets to him." — `sources/adventure-wdh.json:30482` (the paragraph is in the city's history section; the paragraph at line 30481 states that "During the Time of Troubles, Waterdeep stood at the center of events.")

Published adventure, Undermountain: none in `sources/adventure-wdmm.json`.

### Field 7: Conflicts and not found

Conflicts:
- Status. FRHoF calls him a god: "Bhaal is a god of murder who revels in violence and ritualistic killing." (`5etools.md:7`). The wiki says "the Lord of Murder was no longer a true deity, and was instead a being of quasi-divine status." (`wiki.txt:178`). The wiki's "Former Deity" (`wiki.txt:43`) cites SCAG pp.21, 23, 27. The 5etools SCAG entry (`5etools.md:21–26`) does not state a status, so that wiki citation cannot be checked against it.
- Symbol wording. PHB: "- symbol: Skull surrounded by a ring of blood droplets" (`5etools.md:17`). SCAG: "- symbol: Skull surrounded by ring of bloody droplets" (`5etools.md:26`). Same symbol, different wording.
- "Dread Lord" appears in the wiki title (`wiki.txt:10`) and in the Appendix B table, where it is a rank in the Black Network. That row reads: "| 50 | **Dread Lord** | The Doom Raiders invest fully in the character as a Network leader. Eight Black Network operatives are available for one major operation. Davil proposes the character for a seat on the reforming Zhentarim Council — a position of genuine continental influence within the Black Network. |" — `sources/Appendix_B_-_Player_Factions.md:672` (not Bhaal; outside this batch's scope, noted only)

Not found:
- No Bhaal temple, shrine, or priest in Waterdeep, in the Major Temples table, or in the campaign.
- No campaign NPC, faction, or quest that names Bhaal.
- No Bhaal holy day in the Waterdeep calendar.

### Answers (1)–(3)

1. **Waterdeep temples or shrines, and ward.** None. The published adventure and the campaign place no Bhaal temple or shrine in Waterdeep. The only temple location the FRHoF names is in Baldur's Gate (`5etools.md:10`).
2. **Campaign use.** No campaign file uses this power.
3. **Wiki lines that mention Waterdeep.** `wiki.txt:196` and `wiki.txt:198`, both in the Appearances table:
> "| adventures          = ''Waterdeep''" — `wiki.txt:196`
> "| novels              = ''Tantras''; ''Waterdeep''; ''Black Wizards'' • ''Darkwell''" — `wiki.txt:198`

These are appearances in the Waterdeep adventure and the Waterdeep novel. They place no temple in the city.

---

## 3. Loviatar

### Field 1: Identity

FRHoF (`5etools.md`, lines 1–5):
> "## Loviatar | source FRHoF p.114 | pantheon Faerûnian" — `5etools.md:1`
> "- altNames: ['The Maiden of Pain', 'The Scourge Mistress', 'The Willing Whip']" — `5etools.md:2`
> "- title: God of pain" — `5etools.md:3`
> "- worshipers: Those suffering from pain or betrayal" — `5etools.md:4`
> "- plane: Gehenna (Mungoth)" — `5etools.md:5`

PHB (`5etools.md`, lines 14–18):
> "## Loviatar | source PHB p.294 | pantheon Forgotten Realms" — `5etools.md:14`
> "- title: Goddess of pain" — `5etools.md:15`
> "- alignment: ['L', 'E']" — `5etools.md:16`
> "- domains: ['Death']" — `5etools.md:17`
> "- symbol: Nine-tailed barbed scourge" — `5etools.md:18`

SCAG (`5etools.md`, lines 22–27):
> "## Loviatar | source SCAG p.21 | pantheon Faerûnian" — `5etools.md:22`
> "- altNames: ['The Maiden of Pain', 'The Scourge Mistress', 'The Willing Whip']" — `5etools.md:23`
> "- title: Goddess of pain" — `5etools.md:24`
> "- alignment: ['L', 'E']" — `5etools.md:25`
> "- domains: ['Death']" — `5etools.md:26`
> "- symbol: Nine-tailed barbed scourge" — `5etools.md:27`

Wiki, title:
> "| title               = The Maiden of Pain<ref name="HoF-p114"/><ref name="SCAG5e-p21,33" /><br /> The Willing Whip<ref name="HoF-p114"/><ref name="SCAG5e-p21,33" /><br />The Scourge Mistress<ref name="HoF-p114"/><ref name="SCAG5e-p21,33" /><br /> Patroness of Torturers<ref name="F&A-p100" />" — `wiki.txt:7`

Wiki, 5e alignment and symbol:
> "| alignment5e         = Lawful evil" — `wiki.txt:55`
> "| symbol5e            = Nine-tailed barbed scourge" — `wiki.txt:56`

Wiki, lead paragraph:
> "'''Loviatar''' ({{Pronounce|loh|VEE|a|tar|refs=<ref name="F&P100"/>}} {{Pronounce|loh|vee|A|tar|alt=yes|audio=Loviatar.ogg|refs=<ref name="FRCS1e-CotR-p12">{{Cite book/Forgotten Realms Campaign Set/Cyclopedia of the Realms|12}}</ref>}}) was the evil goddess of agony and was both queen and servant to the greater god Bane.<ref name="FRCG-pg80">{{Cite book/Forgotten Realms Campaign Guide|80}}</ref> '''The Maiden of Pain''' was the master of inflicting physical and psychological suffering, her portfolio encompassing hurt and torture.<ref name="F&P100"/>" — `wiki.txt:134`

### Field 2: Edict or core tenet

> "To the followers of Loviatar, nothing is as transcendent as suffering. All pain is holy, from the crudest brutality to the emotional suffering of the heartbroken or the betrayed, and is proof of Loviatar's attention. Pain—the ability both to inflict it and to endure it—is a path to power. Loviatar's followers consider a cold, cruel demeanor ideal because that best emulates Loviatar herself, and for the same reason her faithful appreciate beauty, cultural refinement, and skill at manipulation." — `5etools.md:9` (FRHoF)

> "The Maiden of Pain, Loviatar, teaches us that pain is a most powerful and sacred sensation. And should our pain delight her—should we ''embrace'' such a gift—she will grant her most sacred of blessings." — `wiki.txt:137` (a worshiper's quote, Abdirak, citing Baldur's Gate III)

### Field 3: Portfolio and areas of concern

> "Loviatar is a god of agony, the mistress of physical and psychological suffering. Coldhearted and calculatingly cruel, Loviatar is an aggressive and domineering despot, and she deeply enjoys her divine remit. Pain isn't a means to an end for Loviatar, but an end unto itself. That quality endears her to the tyrant god Bane." — `5etools.md:7` (FRHoF)

> "| portfolio5eR        = Pain" — `wiki.txt:46` (5eR)
> "| portfolio5e         = Pain" — `wiki.txt:61` (5e; wiki cites SCAG p.21,33)
> "| portfolio3e         = Agony, hurt, suffering, torment, torture" — `wiki.txt:90` (3e)
> "| portfolio2e         = Pain, hurt, agony, suffering, torment, torture" — `wiki.txt:105` (2e)

### Field 4: Worship (clergy, holy days, temples, omens, messengers)

Waterdeep: none (Answers 1). Undermountain: Field 6.

Temples, as the wiki lists them under the heading "Temples Dedicated to Loviatar" (`wiki.txt:199`):
> "* House of Nine Blessings, in Calimport.<ref name="C-p31">{{Cite book/Calimport|31}}</ref>" — `wiki.txt:200`
> "* House of Scarlet Hooks in Calaunt.<ref name="FRAp80">{{Cite book/Forgotten Realms Adventures|80–81}}</ref>" — `wiki.txt:201`
> "* Lady's Hand Monastery, in Ladypeak.<ref name="SM-p12">{{Cite book/Silver Marches|12-13}}</ref>" — `wiki.txt:202`
> "* Resting Place of the Whip in Melvaunt.<ref name="MotM p.12">{{Cite book/Mysteries of the Moonsea|12}}</ref>" — `wiki.txt:203`
> "* Tower of Pain Exalted in Zhentil Keep.<ref name="FRA-p120">{{Cite book/Forgotten Realms Adventures|120}}</ref>" — `wiki.txt:204`
> "* House of Pain in Undermountain.<ref name="CoS.W-p41">{{Cite book/City of Splendors: Waterdeep|41}}</ref>" — `wiki.txt:205`

Clergy and faith (FRHoF):
> "Though temples to Loviatar are rare, her faithful are numerous. Loviatar is a preferred deity of those who inflict pain as a matter of course, including torturers and others who need to break the will of their victims. Her followers form cells of secret adherents led by someone who takes pleasure in administering pain and dominating others, supported and bolstered by submissive sycophants." — `5etools.md:10`

> "Worshipers of Loviatar rarely gather in numbers except in the more populous cities. When small cadres of faithful operate quietly in such places, few citizens take notice or raise a fuss if they do witness cult activity. The sufferers who endure the lash, however, aren't always willing participants, and Lovatar's cults sometimes operate secret slavery rings, which can draw the attention of the authorities. The open worship of Loviatar and temples clearly dedicated to her are rarely seen except in lands where slavery is an accepted practice." — `5etools.md:32` (SCAG; "Lovatar" is the source's misspelling)

Clergy ranks and specialty priests (wiki):
> "Specialty priests, called pains, operate as a separate arm of the faith. They travel from place to place carrying out the goddess's will as envoys, agents, or inquisitors rather than being permanently stationed at a temple. Ordinary clerics of Loviatar hold the pains in high regard. A temple mainly consists of clerics, but one to three pains can be called upon if needed. Mystics often are assigned to groups of pains and monk, while living only with monks and monasteries. They usually swear fealty to the temple that their abbey is a part of in the hierarchy. <ref name="FaA-101"/>" — `wiki.txt:195`

Rites and holy days (wiki):
> "Loviatans often engaged in self-flagellation, often in the morning when praying for spells. They celebrated each season with the Rite of Pain and Purity, a ritual that involved followers dancing on glass, thorns, or barbed-wire while being whipped by higher-level Loviatans. A smaller ritual occurring every twelve days involved followers passing their bodies through the flames of candles.<ref name="F&P100" />" — `wiki.txt:173` (wiki cites Faiths and Pantheons p.100)

Messengers (FRHoF):
> "Loviatar takes the form of a slender woman, like a whip in her movement and aspect. She speaks to her followers during extended sessions of enduring or inflicting pain, intruding on their perceptions in the delirium of agony or ecstasy. When she dispatches an emissary, she usually sends a {@creature Chain Devil|XMM}, an {@creature Incubus|XMM}, or a {@creature Succubus|XMM}." — `5etools.md:8`

Chosen (FRHoF): "The Chosen of Loviatar are paragons of inflicting and receiving pain. They delight in insinuating themselves into the fabric of society and then tearing through it like a barbed whip." — `5etools.md:12`

Omens: none sourced.

### Field 5: Relations with other powers, and origin or rise

> "Prior to the Time of Troubles, Loviatar was a servant of Bhaal and had a heated rivalry with her fellow servant Talona.<ref name="F&A-p45">{{Cite book/Faiths & Avatars|45}}</ref> In the {{YearlinkName|-33}},<ref name="N.EoM-p12">{{Cite book/Netheril: Empire of Magic/The Winds of Netheril|12}}</ref> demigoddess Kiputytto, Loviatar's sister, was slain by Talona. This made Loviatar and Talona heated rivals, leaving the Lady of Pain to torment Talona in revenge.<ref name="TEV">{{Cite web/theedverse/2022-11-07 - Loviatar & Talona}}</ref> Loviatar thought that Talona should and would eventually serve her.<ref name="F&A-p101">{{Cite book/Faiths & Avatars|101}}</ref> During that time she was also affiliated with Malar.<ref name="F&P100" />" — `wiki.txt:156` (wiki cites Faiths & Avatars p.45, Netheril: Empire of Magic p.12, and Faiths & Avatars p.101)

> "For a time she fell under the sway of Shar, though the return of Bane changed this, as she once again served as his consort. Loviatar's portfolio conflicted most with that of Ilmater, because Loviatar despised those who helped others. She also hated Eldath and Lliira for offering rewards without any suffering to achieve them.<ref name="F&P100" />" — `wiki.txt:158` (wiki cites Faiths and Pantheons p.100)

Origin (wiki):
> "Loviatar is named for Loviatar, a Finnish goddess of death and pestilence of the same name, originally appearing in the 1{{st}}-edition ''Deities & Demigods''.<ref name="Dragon 54">{{Cite dragon/54/Down-to-earth divinity|52}}</ref>" — `wiki.txt:214` (the wiki's Background section; cite is Dragon 54)

### Field 6: Campaign and published-adventure mentions

Campaign: none. The Grep for "Loviatar", "Lovatar", "Loviatan", "Maiden of Pain", "Scourge Mistress", and "Willing Whip" found no campaign line, and `campaign-hits.txt` is empty.

Published adventure, Undermountain. The Tower of the Seven Woes entry (`sources/adventure-wdmm.json:62692`, page 304) names worshipers of Loviatar using a tower as a prison, not as a temple:
> "9. Tower of the Seven Woes" — `sources/adventure-wdmm.json:62692`

> "Carved into the column is a seven-story prison composed of windowless torture chambers connected to one another by rough-hewn stairways. Worshipers of Loviatar used this tower to imprison and torture slaves. The walls throughout are lined with manacles; rusted shackles lie strewn amid torture racks, spiked cages, and other contraptions that have fallen into disrepair." — `sources/adventure-wdmm.json:62705`

Published adventure, Waterdeep: none in `sources/adventure-wdh.json`.

### Field 7: Conflicts and not found

Conflicts:
- Gender of title. FRHoF: "- title: God of pain" (`5etools.md:3`). PHB and SCAG: "- title: Goddess of pain" (`5etools.md:15`, `5etools.md:24`). The wiki's infobox: "| gender              = Feminine" (`wiki.txt:34`). FRHoF's prose uses "she" ("she deeply enjoys her divine remit", `5etools.md:7`).
- Rank by edition (wiki infobox): 5e "Deity" (`wiki.txt:39`), 4e "Intermediate deity" (`wiki.txt:68`), 3e "Lesser deity" (`wiki.txt:83`), 1e "Demigoddess" (`wiki.txt:112`).
- Spelling. "Lovatar's cults" (`5etools.md:32`) is a misspelling in the source. No other line uses it.

Not found:
- No campaign NPC, faction, quest, or Waterdeep temple. No Loviatar row in the Major Temples table.
- No Loviatar holy day in the Waterdeep calendar. No omen source.

### Answers (1)–(3)

1. **Waterdeep temples or shrines, and ward.** None in Waterdeep. The wiki lists a "House of Pain" temple "in Undermountain" and cites City of Splendors: Waterdeep p.41 (`wiki.txt:205`). It gives no ward. The Undermountain tower (`sources/adventure-wdmm.json:62705`) is a prison that its worshipers used, not a temple.
2. **Campaign use.** No campaign file uses this power.
3. **Wiki lines that mention Waterdeep.** `wiki.txt:205`, in the citation only ("City of Splendors: Waterdeep").

---

## 4. Talona

### Field 1: Identity

FRHoF (`5etools.md`, lines 1–5):
> "## Talona | source FRHoF p.123 | pantheon Faerûnian" — `5etools.md:1`
> "- altNames: ['Lady of Poison', 'Mistress of Disease', 'The Plague Crone']" — `5etools.md:2`
> "- title: God of poison and disease" — `5etools.md:3`
> "- worshipers: Those suffering from plague" — `5etools.md:4`
> "- plane: Carceri (Cathrys)" — `5etools.md:5`

PHB (`5etools.md`, lines 14–18):
> "## Talona | source PHB p.294 | pantheon Forgotten Realms" — `5etools.md:14`
> "- title: Goddess of disease and poison" — `5etools.md:15`
> "- alignment: ['C', 'E']" — `5etools.md:16`
> "- domains: ['Death']" — `5etools.md:17`
> "- symbol: Three teardrops on a triangle" — `5etools.md:18`

SCAG (`5etools.md`, lines 22–27):
> "## Talona | source SCAG p.21 | pantheon Faerûnian" — `5etools.md:22`
> "- altNames: ['Lady of Poison', 'Mistress of Disease', 'The Plague-crone']" — `5etools.md:23`
> "- title: Goddess of poison and disease" — `5etools.md:24`
> "- alignment: ['C', 'E']" — `5etools.md:25`
> "- domains: ['Death']" — `5etools.md:26`
> "- symbol: Three teardrops in a triangle" — `5etools.md:27`

Wiki, 5e alignment and symbol (the wiki cites SCAG p.21,38):
> "| alignment5e         = Chaotic evil" — `wiki.txt:53`
> "| symbol5e            = Three teardrops in a triangle" — `wiki.txt:54`

Wiki, lead paragraph:
> "'''Talona''' ({{Pronounce|tah|LO|nah|refs=<ref name="F&P-p107" />}}) was the goddess of poison and disease in the Faerûnian pantheon.<ref name="F&P-p107">{{Cite book/Faiths and Pantheons|107-108}}</ref><ref name="HoF-pp99,123">{{Cite book/Forgotten Realms: Heroes of Faerûn|99,123}}</ref> Where the '''Lady of Poison''' walked, death and disaster followed, and she was blamed for all manner of ailments, ranging from common sicknesses and devastating diseases to brackish wells and failing crops,<ref name="SCAG5e-p21,38" /> Worship of the '''Mother of All Plagues''' waxed and waned in an unending cycle; the '''Mistress of Disease''' would unleash waves of death-bringing blights, after which came mass entreaties for respite before that cycle's great plagues went into remission, her power slowly declined, and spurred by feelings of vulnerability, she began the cycle anew.<ref name="F&P-p107" />" — `wiki.txt:133`

### Field 2: Edict or core tenet

No edict in the sources. The core tenet is propitiation.

> "One of Faerûn's most feared deities, Talona is a god of plague and poison, blamed for everything from common illnesses to crop failure, from brackish wells to plague. She craves propitiation from mortals and pursues it by any means necessary." — `5etools.md:7` (FRHoF)

> "Talona was a strange goddess in terms of personality. She had been compared by sages to a greedy and petulant child, switching between the juvenile desire for attention at any cost to the aloofness of a discarded paramour. Curiously for a deity so closely tied to death, she had no personal taste for violence.<ref name="F&A-p152"/>" — `wiki.txt:141` (wiki cites Faiths & Avatars p.152)

### Field 3: Portfolio and areas of concern

> "| portfolio5eR        = Poison, disease" — `wiki.txt:44` (5eR; the source line is `[[Poison]], [[disease]]`, rendered here with link markup dropped)
> "| portfolio5e         = Poison, disease" — `wiki.txt:59` (5e; wiki cites SCAG p.21,38)
> "| portfolio3e         = Disease<br />Poison" — `wiki.txt:89` (3e)
> "| portfolio2e         = Disease, poison" — `wiki.txt:104` (2e)

### Field 4: Worship (clergy, holy days, temples, omens, messengers)

Waterdeep: none (Answers 1).

> "Talona is a fickle god. She is more petulant than conniving, more reactive than active. Though she receives many prayers, Talona has almost no temples or cults dedicated to her, and she resents the neglect. When she lashes out with plagues, blights, and magical contagions, victims desperately pray to her for respite, placating her for a time. But once the contagion ends, prayers dwindle, and it isn't long before the neglected god lashes out again." — `5etools.md:8` (FRHoF)

> "When Talona communicates with mortals—usually to demand some sort of propitiation—she sends a {@creature Vulture|XMM}, a {@creature Giant Rat|XMM}, or the corpse of a creature infested by insects. Whatever method she chooses, her messenger is shrouded in a sickly yellow-brown glow." — `5etools.md:9` (messengers, FRHoF)

> "Rituals to placate Talona involve three drops of blood or three tears dropped into a well that has gone bad, dripped into the handkerchief of someone beset by coughing, dropped into a fire made by burning a withered crop, dripped into the mouth of a plague sufferer, and so on. It's common practice to mark a container of poison with her holy symbol, three droplets in a triangle. During epidemics, this image is painted on the homes of the infected." — `5etools.md:10` (FRHoF)

> "Talona's priests rarely enter into her service willingly. Some are forced into the role by their communities, while other individuals simply have nothing else to live for. This latter category includes the sole survivors of harrowing magical contagions, or people who have lost loved ones to Talona's whims. They dedicate their lives to the priesthood to make sure the same fate doesn't befall others. A priest of Talona maintains a small shrine instead of a temple. Despite the priest's best efforts, people often lavish these shrines with offerings during tough times while neglecting them in times of health and abundance." — `5etools.md:11` (FRHoF)

> "Though she is often the recipient of prayers, Talona has almost no temples and few cults dedicated to her. A cult or a shrine to her might arise in an area after it suffers from pestilence, when some of those who survived decide to revere her or even become priests." — `5etools.md:30` (SCAG)

Temple (wiki, the only named temple; in Tashluta, not Waterdeep):
> "The House of Night's Embrace was Talona's largest church in Faerun and was located in Tashluta.<ref name="SK-p126">{{Cite book/Serpent Kingdoms|126}}</ref>" — `wiki.txt:168` (heading "Temples" at `wiki.txt:167`)

Chosen (FRHoF): "Among these fanatics, her Chosen are gifted with immunity to poisons and magical maladies." — `5etools.md:12`

Holy days: none sourced. Omens: none sourced.

### Field 5: Relations with other powers, and origin or rise

> "Prior to the Time of Troubles, Talona was a servant of Bhaal and had a heated rivalry with her fellow servant Loviatar.<ref name="F&A-p45">{{Cite book/Faiths & Avatars|45}}</ref> During that time she was often teased and tormented by her. Mocked for her appearance, the size of her portfolio, and her small number of followers.<ref name="F&A-p101, 152">{{Cite book/Faiths & Avatars|101, 152}}</ref> She would occasionally provide aid to adventurers of good alignments if she viewed their goals as something that would damage Loviatar's reputation.<ref name="F&A-p152" />" — `wiki.txt:149` (wiki cites Faiths & Avatars pp.45, 101, and 152)

> "''Circa'' 1369 DR, she developed an alliance with the deity Shar.<ref name="F&A-p152" />" — `wiki.txt:151` (wiki cites Faiths & Avatars p.152)

> "She despised Chauntea, Mielikki, Kelemvor, and Tyr.<ref name="F&A-p152" /><ref name="F&P-p107" />" — `wiki.txt:153` (wiki cites Faiths & Avatars p.152 and Faiths and Pantheons p.107)

> "In {{Yearlink|-33}},<ref name="NEoM-p117">{{Cite book/Netheril: Empire of Magic/The Winds of Netheril|117}}</ref> a demipower named Kiputytto, sister of Loviatar,<ref name="TEV">{{Cite web/theedverse/2022-11-07 - Loviatar & Talona}}</ref> tried to challenge Talona for her portfolio. The conflict that ensued devastated the nation of Asram with terrible plagues, forcing its citizens to provide Talona devotional power in hopes that she would lessen the plague's effects.<ref name="F&A-p152">{{Cite book/Faiths & Avatars|152}}</ref><ref name="N.EoM-p12">{{Cite book/Netheril: Empire of Magic/The Winds of Netheril|12}}</ref> Talona ultimately won the conflict and shortly afterwards murdered Kiputytto. In the years that followed, texts would be written that referred to the latter deity as an alias of hers, further cementing Kiputytto's defeat.<ref name="F&A-p152" />" — `wiki.txt:171` (wiki cites Netheril: Empire of Magic p.117 for the date, Faiths & Avatars p.152, and Netheril: Empire of Magic p.12)

### Field 6: Campaign and published-adventure mentions

None. The Grep for "Talona", "Talontar", "Talonite", "Lady of Poison", "Mistress of Disease", "Plague Crone", "Plague-crone", "Mother of All Plagues", "Plague Rats", "Palace of Poison Tears", and "House of Night" found no line in `campaign/`, `sources/adventure-wdh.json`, or `sources/adventure-wdmm.json`. Both bundle files are empty.

### Field 7: Conflicts and not found

Conflicts:
- Worshipers. FRHoF: "- worshipers: Those suffering from plague" (`5etools.md:4`). Wiki, 5e, citing SCAG p.21,38: "| worshipers5e        = Survivors from pestilence" (`wiki.txt:61`). These are two source lists. They do not contradict each other.
- Symbol wording. PHB: "- symbol: Three teardrops on a triangle" (`5etools.md:18`). SCAG: "- symbol: Three teardrops in a triangle" (`5etools.md:27`). Same symbol.

Not found:
- No Waterdeep temple, shrine, or holy day for Talona.
- No campaign NPC, faction, or quest that names her.
- No published-adventure line names her.

### Answers (1)–(3)

1. **Waterdeep temples or shrines, and ward.** None. The only temple the wiki names is the House of Night's Embrace in Tashluta (`wiki.txt:168`). The Major Temples table has no Talona row.
2. **Campaign use.** No campaign file uses this power.
3. **Wiki lines that mention Waterdeep.** None.

---

## 5. Talos

### Field 1: Identity

FRHoF (`5etools.md`, lines 1–5):
> "## Talos | source FRHoF p.123 | pantheon Faerûnian" — `5etools.md:1`
> "- altNames: ['The Destroyer', 'Storm Lord', 'The Raging One']" — `5etools.md:2`
> "- title: God of storms" — `5etools.md:3`
> "- worshipers: Barbarians, Druids, raiders" — `5etools.md:4`
> "- plane: Pandemonium (Pandesmos)" — `5etools.md:5`

PHB (`5etools.md`, lines 13–17):
> "## Talos | source PHB p.294 | pantheon Forgotten Realms" — `5etools.md:13`
> "- title: God of storms" — `5etools.md:14`
> "- alignment: ['C', 'E']" — `5etools.md:15`
> "- domains: ['Tempest']" — `5etools.md:16`
> "- symbol: Three lightning bolts radiating from a central point" — `5etools.md:17`

SCAG (`5etools.md`, lines 21–26):
> "## Talos | source SCAG p.21 | pantheon Faerûnian" — `5etools.md:21`
> "- altNames: ['Stormlord', 'The Destroyer']" — `5etools.md:22`
> "- title: God of storms" — `5etools.md:23`
> "- alignment: ['C', 'E']" — `5etools.md:24`
> "- domains: ['Tempest']" — `5etools.md:25`
> "- symbol: Three lightning bolts radiating from a point" — `5etools.md:26`

Wiki, aspects:
> "| aspects             = Bhaelros (Calimshan)<ref name="HoF-p123"/><ref name="F&A"/><br/>Kozah (Netheril, Bedine)<ref name="F&A"/><ref name="nem-wn-42-45">{{Cite book/Netheril: Empire of Magic/The Winds of Netheril|42-45}}</ref><br/>Malyk (Underdark)<ref name="F&A"/>" — `wiki.txt:10`

Wiki, 5e portfolio, domains, worshipers (the wiki cites SCAG p.21,38):
> "| portfolio5e         = Storms, forest fires, earthquakes, tornadoes, destruction" — `wiki.txt:36`
> "| domains5e           = Tempest" — `wiki.txt:37`
> "| worshipers5e        = Ravagers, raiders, looters, brigands" — `wiki.txt:38`

Wiki, lead paragraph:
> "'''Talos''' ({{Pronounce|TAHL|os|refs=<ref>{{Cite book/Forgotten Realms Campaign Setting 3rd edition|252}}</ref><ref name="FaP-p68"/>}}), known long ago as '''Kozah''', was the Faerûnian greater deity of storms and destruction. The '''Storm Lord''' was the destructive force of nature and leader of the Gods of Fury whose self-serving dogma demanded utter obedience from his priests, instructing them to spread destruction where they might.<ref name="FaP-p68" /><ref name="F&A" />" — `wiki.txt:110`

### Field 2: Edict or core tenet

> "Day-to-day worship of the Storm Lord is outlawed in most of Faerûn, though folk make desperate offerings to save themselves from natural disasters. Talos's faithful love destruction, and they call storms on towns and cities in the name of their deity. Many become brigands, wandering from place to place demanding loot and threatening destruction. Sometimes Talos's faithful forgo any ultimatum, causing wanton destruction for destruction's sake. They are taught that life is chaos and that each person should seize what they can when they can—after all, who can say when Talos will strike and bring them to the afterlife?" — `5etools.md:9` (FRHoF)

> "Talos is the dark side of nature, the uncaring and destructive force that might strike at any time. He is the god of storms, forest fires, earthquakes, tornadoes, and general destruction. He counts the ravager, the raider, the looter, and the brigand among his followers. Those who favor him see life as a succession of random effects in a sea of chaos, so the devout should grab what they can, when they can - for who can say when Talos will strike and send them into the afterlife?" — `5etools.md:28` (SCAG)

> "Talos can see nothing but a world that must be destroyed." — `wiki.txt:115`
> "Mystra.<ref name="PoL7">{{Cite book/Prince of Lies|chapter=7}}</ref>" — `wiki.txt:116` (the attribution; lines 115 and 116 form one block quote)

### Field 3: Portfolio and areas of concern

> "Talos personifies the destructive aspects of nature. He is best known as a god of storms, but he is also associated with forest fires, earthquakes, tornadoes, and general destruction. Raiders, looters, and brigands flock to his worship." — `5etools.md:7` (FRHoF)

> "| portfolio3e         = Conflagration <br /> Destruction <br /> Earthquakes <br /> Rebellion <br /> Storms <br /> Vortices" — `wiki.txt:65` (3e)

### Field 4: Worship (clergy, holy days, temples, omens, messengers)

Waterdeep: none (Answers 1).

> "Priests of Talos have few temples, instead traveling like a wayward storm.They wear ragged robes and cloaks shot through with jagged lines of gold and silver. Many wear an eye patch in deference to their god. Priests and other devout worshipers of Talos make pilgrimages to a canyon called the Gulf of Storms in eastern {@book Amn|FRHoF|2|Amn}. The peculiar iron ore in the canyon's walls attracts electrical charges, making the chasm prone to spectacular, deadly arrays of crisscrossing, leaping lightning bolts. This energy develops into storms that race down the valley to lash across Amn and {@book Tethyr|FRHoF|2|Tethyr}." — `5etools.md:10` (FRHoF)

> "Although Talos is a popular deity, his name is invoked more often out of fear than out of reverence. He does have priests, mostly traveling doomsayers, who warn of disasters to come and accept charity in exchange for blessings of protection. Many of his faithful wear a black eyepatch, even if both eyes are intact." — `5etools.md:30` (SCAG)

Omens and messengers (FRHoF; the manifestations are the last sentence):
> "The Storm Lord's actions seem petty and vengeful, motivated by rage, anger, and the need to posture among other gods. Talos is an ancient god who sprang up from the wreckage of the first battle between Selûne and Shar. Religious art often depicts him as a broad-shouldered, bearded man with an eye patch, but the folk of {@book Calimshan|FRHoF|2|Calimshan} know him by the name Bhaelros and depict him with a genie-like appearance. Talos rules over the gods of fury—Auril, Malar, and Umberlee—though it's said Malar would kill him if he could. The Raging One manifests to mortals as bellowing laughter in the heart of strong winds or as red lightning strikes in a storm." — `5etools.md:8`

Worship restrictions and holy sites (wiki):
> "Worship of Talos was outlawed in many countries. Most Talossan holy sites were secret because of the church's reputation. Public churches often took the form of castles or fortified strongholds that lay on earthquake fault lines or in the path of storms or lava; Talos ensured they remain unscathed.<ref>{{cite book/Faiths & Avatars|156}}</ref>" — `wiki.txt:162`

Festivals (wiki; no dates given):
> "Clerics of Talos celebrated Talossan festivals with ceremonies that summoned lightning and storms.<ref name="FA-p157" /><ref name="FaP-p68" />" — `wiki.txt:165` (wiki cites Faiths & Avatars p.157 and Faiths and Pantheons p.68)

Chosen (FRHoF):
> "Talos's Chosen bring terror to Faerûn. They wield incredibly powerful destructive spells such as {@spell Storm of Vengeance|XPHB}, {@spell Earthquake|XPHB}, and {@spell Meteor Swarm|XPHB}, unleashing annihilation on cities and villages that don't bend to the Storm Lord's will." — `5etools.md:11`

Holy days beyond the festival line: none sourced.

### Field 5: Relations with other powers, and origin or rise

> "Talos was the leader of the Gods of Fury, a collection of deities including Auril, Umberlee, Malar, and himself, that he brought together through sheer force and which he kept together under his tight control.<ref name="OHG-171" />" — `wiki.txt:131` (wiki cites On Hallowed Ground p.171)

> "Talos's relationship with Umberlee was simultaneously flirtatious and competitive.<ref name="F&A" /> Like with Auril, he had been encroaching upon her portfolio, trying to pick up violent nature in all its forms as his own. Though she might flirt with him on occasion, Umberlee would gladly kill him and become the sole deity of destruction herself if she could. Given her inability to directly affect the land and relative weakness however, she simply bided her time trying to distract him with romantic intrigues and instructing her priests to kill those who would ascribe the storms of the sea and shore to him.<ref name="FA-p173">{{Cite book/Faiths & Avatars|173}}</ref><ref name="FRCS-254">{{Cite book/Forgotten Realms Campaign Setting 3rd edition|254}}</ref>" — `wiki.txt:135` (wiki cites Faiths & Avatars p.173 and Forgotten Realms Campaign Setting 3e p.254)

> "Of the Gods of Fury, Talos's worst relationship was with Malar. They cooperated only grudgingly and the Beastlord would happily kill him if he had the power to.<ref name="F&A" /> Unfortunately for him, Talos's growing strength had left him weakened after the Time of Troubles.<ref name="FA-p105">{{Cite book/Faiths & Avatars|105}}</ref>" — `wiki.txt:137` (wiki cites Faiths & Avatars p.105)

> "The Stormlord was said to have formed from the first battle between Selûne and Shar, near the dawn of the world. The people of ancient Netheril worshiped him as Kozah, and called him The Destroyer and The Raging One, among other titles.<ref name="N.EoM-p42">{{Cite book/Netheril: Empire of Magic/The Winds of Netheril|42}}</ref>" — `wiki.txt:175` (wiki cites Netheril: Empire of Magic p.42)

> "Talos was restored to the pantheon following the Second Sundering,<ref name="SCAG5e-p21,38" /> and subsequently interceded in a conflict between Auril and Umberlee by siding with the latter, thus forcing Auril to retreat to Icewind Dale in the late 1480s DR.<ref name="RotF-p275">{{Cite book/Icewind Dale: Rime of the Frostmaiden|275}}</ref> After the Battle of Leilon in the late 15{{th}} century DR, Talos was furious with Fheralai Stormsworn for failing him, and his avatar appeared in a rage to punish her Cult of Talos.<ref>{{Cite web/D&D Beyond/Divine Contention}}</ref>" — `wiki.txt:181` (wiki cites SCAG 5e p.21,38 for the restoration)

Origin and the Gruumsh identity: Field 7 (`wiki.txt:112`, `wiki.txt:179`).

### Field 6: Campaign and published-adventure mentions

Campaign: none. The Grep for "Talos", "Storm Lord", "Stormlord", "Raging One", "Bhaelros", "Gulf of Storms", "Destroyer", "Malyk", "Kozah", and "Gods of Fury" found no campaign line. `campaign-hits.txt` is empty.

Published adventure, Undermountain. The one hit names an alias of Talos. The adventure does not link the two:
> "The fountain is fed by a natural spring and provides the drow with a virtually endless supply of fresh water. The statues stand atop stone plinths above the water, facing outward. Starting with the northernmost one and moving clockwise, the statues represent Eilistraee (god of beauty, dance, and the hunt), Malyk (god of wild magic), Kiaransalee (god of undeath), Ghaunadaur (god of oozes, slimes, and all things subterranean), Zinzerena (god of assassins), Vhaeraun (god of thieves), Lolth (the Demon Queen of Spiders and mother of the Dark Seldarine) in her drow form, and Selvetarm (god of war and warriors)." — `sources/adventure-wdmm.json:30762`

The wiki gives Malyk as Talos's Underdark aspect (`wiki.txt:10`, "Malyk (Underdark)"). Published adventure, Waterdeep: none.

### Field 7: Conflicts and not found

Conflicts:
- Gruumsh. The wiki's history line says:
> "Among the Bedine of Anauroch, who descended from the citizens of Netheril, Talos was still known as Kozah by the 14{{th}} century DR.<ref name="FaP-p68">{{Cite book/Faiths and Pantheons|68-71}}</ref> In Calimshan and Airspur (Chessenta), he was worshiped as '''Bhaelros'''<ref name="F&A" /><ref name="OE58">{{Cite book/Old Empires|58}}</ref> and in the Underdark, he had an aspect with a small following as '''Malyk''', a god of wild magic.<ref name="F&A" />  After the Spellplague, many came to believe that Talos was, in fact, an aspect of the orcish god Gruumsh,<ref name="DFR">{{Cite dragon/378/Domains in Eberron and the Forgotten Realms|36-37}}</ref> but after the Second Sundering the two deities seemed more distinct.<ref name="SCAG-21,24,38,118">{{Cite book/Sword Coast Adventurer's Guide|21, 24, 38, 118}}</ref>" — `wiki.txt:112`
  FRHoF and SCAG (`5etools.md:8`, `5etools.md:28`–`30`) do not mention Gruumsh.
- The wiki's Stormstar Requiem line says Talos was said to reveal himself as Gruumsh:
> "Following the events of the Spellplague, Talos was believed to be one of several gods who was severely weakened,<ref name="RoS-ch3">{{Cite digital book/The Rose of Sarifal/Kindle||3}}</ref> and in an event known as the Stormstar Requiem, he was said to have revealed himself to be the orcish god Gruumsh, which led to his expulsion from the ranks of the Gods of Fury.<ref name="Drag367">{{Cite dragon/367/Hall of the Frostmaiden|61}}</ref> Even so, Talos continued to be feared through the late 15{{th}} century DR alongside the likes of Bane or Asmodeus,<ref name="RoS-ch9">{{Cite digital book/The Rose of Sarifal/Kindle||9}}</ref> even as it was believed that he could do little more than visit his faithful in their dreams and nightmares.<ref name="RoS-ch3" />" — `wiki.txt:179`
- Spelling. FRHoF writes "Storm Lord" (`5etools.md:2`, `5etools.md:8`). SCAG writes "Stormlord" (`5etools.md:22`).

Not found:
- No Talos temple, shrine, or festival in Waterdeep. No Talos row in the Major Temples table.
- No campaign NPC, faction, or quest that names Talos or an alias.

### Answers (1)–(3)

1. **Waterdeep temples or shrines, and ward.** None. FRHoF says "Priests of Talos have few temples" (`5etools.md:10`), and the wiki's public churches are "castles or fortified strongholds" with no city named (`wiki.txt:162`).
2. **Campaign use.** No campaign file uses this power.
3. **Wiki lines that mention Waterdeep.** None.

---

## Not searched or not used

- `sources/Appendix_B_-_Player_Factions.md:672` (Dread Lord, quoted under Bhaal Field 7) is noted only.
- `docs/plans/setting-compendium-research-notes/pass2/` (other batches) was not used.
- The Alexandrian PDFs and `sources/SOURCE_GUIDE.md` were not read, per the instruction.

## Not readable

None. Every bundle file opened. Empty bundle files: `talona/campaign-hits.txt`, `talona/adventure-hits.txt`, `bhaal/campaign-hits.txt`, `loviatar/campaign-hits.txt`, `talos/campaign-hits.txt`, `talos/adventure-hits.txt`.
