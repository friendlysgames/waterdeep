# Batch L research report: Mephistopheles, Mammon, Orcus, Demogorgon, Graz'zt

Researcher report for the Pass 2 Deities patron pages (Setting Compendium). Brief: `docs/plans/setting-compendium-pass2-brief.md`. Model page: `campaign/setting/deities/asmodeus.md`.

## Conventions

- Quote format: the quote sits on a `>` line, and the file and line follow on the next line after an em dash. Wiki quotes drop the `[[ ]]` link markup only (piped links keep their `target|label` text). Everything else is verbatim, including `<ref>` and `{{Cite ...}}` markup, so the citation keys stay visible. Each power section lists the keys it uses and the book each key names.
- Wiki paths are in full: `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/<slug>/wiki.txt`. Line numbers come from tool output (Read or Grep).
- Campaign and adventure paths are in full (`/home/user/waterdeep/...`).
- Edition tags are the book the wiki cites, as the wiki names it. The wiki template also gives an edition in some fields (`power5e`, `challenge3e`, and so on), and those are quoted as they stand.
- Not read, per the job scope: the Alexandrian PDFs and `sources/SOURCE_GUIDE.md`.

## Bundle files and aliases (all five)

**5etools.md.** Each of the five files says the same thing. Quote from `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/5etools.md:1`:

> "No 5etools deities.json entry for this name."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/5etools.md:1`

The same line (line 1, identical text) appears in `mammon/5etools.md`, `orcus/5etools.md`, `demogorgon/5etools.md` and `graz-zt/5etools.md`, all under the same scratchpad folder.

**adventure-hits.txt.** Empty for all five. Confirmed by searching the two JSON files (see Not found).

**campaign-hits.txt.** Empty for Orcus, Demogorgon and Graz'zt. For Mephistopheles and Mammon it holds one line, the Asmodeus page (quoted below).

Aliases searched in `sources/adventure-wdh.json` and `sources/adventure-wdmm.json`: Mephisto, Molikroth, Cold Lord, Lord of Hellfire, Lord of the Eighth, hellfire, Mammon, Minauros, Orcus, Demogorgon, Graz'zt (and Grazzt, and Graz'zt with a curly apostrophe), Prince of Demons, Prince of Undeath, Wand of Orcus, Tenebrous, Azzagrat, Dark Prince, Prince of Pleasure, Imprisoned One, Lord of the Third, Viscount, Lord of Undeath, Blood Lord, Deep Father, Aameul, Hethradiah, Prince of the Undead, demon lord.

- `adventure-wdh.json`: no line matches any alias.
- `adventure-wdmm.json`: the only matches are generic "demon lord" or "Tenebrous" lines. They are quoted under Cross-references.

## Required quote: the Asmodeus page

These lines are the ones the brief asks for, so the patron pages can agree with them.

> "Mephistopheles is his greatest ally and chief rival. Dispater is loyal, Mammon fawns, Baalzebul and Levistus resent him, and Belial and Fierna rule Phlegethos together by his ruling. Every archdevil would take his throne and none moves openly against him."
— `/home/user/waterdeep/campaign/setting/deities/asmodeus.md:51`
Context: bullet under "Relations with other archdevils and the planar court" (line 48). The bullet's leading "  - " is not part of the quote.

No other line in `campaign/` names any of the five. A search for Mephisto, Molikroth, Cold Lord, Lord of Hellfire, Lord of the Eighth, hellfire, Mammon, Minauros, Orcus, Demogorgon, Graz'zt, Prince of Demons, Prince of Undeath, Wand of Orcus, Tenebrous, Azzagrat, Dark Prince, Prince of Pleasure, Imprisoned One, Lord of the Third and Viscount returned only that line. A second search for demon prince, demon lord, archdevil, Fiend patron, warlock patron, Mammon, Orcus, Graz, Demogorgon and Mephisto returned only asmodeus.md lines 8, 31, 44, 45, 47, 48, 51, 52, 62, 69, 104 and 120. Those lines concern Asmodeus and name none of the five except line 51.

---

# 1. Mephistopheles

Wiki page: `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt`. Wiki keys (book as the wiki names it): FCII = Fiendish Codex II: Tyrants of the Nine Hells (line 12). FCAII = Fiendish Codex II Fiendish Aspects, a web article dated 2007-02-16 (line 120). MTOF = Mordenkainen's Tome of Foes, pp. 16-17, 20, 23, 174, cited as 5e (line 41). DMG5e-p65-66 = Dungeon Master's Guide 5th edition (line 41). Motp4e-p104-105 = Manual of the Planes 4th edition (line 56). Motp3-pp122-123 = Manual of the Planes 3rd edition (line 120). BoVD = Book of Vile Darkness (line 120). GTH = Guide to Hell (line 120). TNH26-31 = Dragon 76, The Nine Hells Part II (line 12). HoHM = Dungeon 140, Heart of Hellfire Mountain (line 12). SS = Shadowstorm, novel (line 116). NWNHoTU = Neverwinter Nights: Hordes of the Underdark, video game (line 283). PoLB = Planes of Law: Baator (line 157). Dragon-223-p17.18 = Dragon 223, The Lords of the Nine (line 112). MMII = Monster Manual II, 1st edition (line 13). FCIIp5.28.41 = Fiendish Codex II pp. 5, 28, 41 (line 72). TG = The Godborn, hardcover novel (line 294). D135 = Dungeon 135, Age of Worms: Dawn of a New Age (line 222). TPA-67 = The Plane Above, p. 67 (line 237).

## Answers

**(1) Waterdeep cult, shrine or temple.** None in any source. The wiki names Waterdeep only as a target of the Valsharess and in a picture caption (Q3). The campaign files name no cult of Mephistopheles. The published adventure's "Major Temples of Waterdeep" table has no Mephistopheles row (Cross-references).

**(2) Campaign NPC, faction or quest using the power.** None. The only campaign line is `asmodeus.md:51`, which names him as Asmodeus's ally and rival. It describes no cult and no NPC.

**(3) Wiki lines that mention Waterdeep.** Lines 283, 285, 286 and 288 (quoted in Field 6 below).

## Field 1: Identity

- Titles, line 12:
> "| titles              = Lord of the Eighth<ref name ="FCII">{{Cite book/Fiendish Codex II: Tyrants of the Nine Hells|69-72,84,153-155}}</ref><br /> Lord of the Citadel<ref name="Motp3-pp122-123">{{Cite book/Manual of the Planes 3rd edition|122-123}}</ref><br/> Lord of No Mercy<ref name="TNH26-31">{{Cite dragon/76/The Nine Hells, Part II|26-31}}</ref><br /> Lord of Hellfire<ref name="BoVD-pp62-63.161-165">{{Cite book/Book of Vile Darkness|62-63,161-165}}</ref><br /> The Cold Lord<ref name="TNH26-31"/><br /> Duke of Brimstone<ref name="BoVD-pp62-63.161-165"/><br /> Archduke of Cania<ref name ="FCII"/><br /> Baron of Cania<ref name="FoETF-p32">{{Cite book/Faces of Evil: The Fiends|32}}</ref><br /> The Archdevil of Contradictions<ref name ="HoHM">{{Cite dungeon/140/Heart of Hellfire Mountain}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:12`

- Aspects and true name, line 13:
> "| aspects             = Mephisto<ref name="MMII">{{Cite book/Monster Manual II 1st edition|47-48}}</ref><br/>Molikroth<ref name="FoETF-p32"/><br/> Thra'axfyl the Ambitious (True name)<ref name="NWN">{{Cite game/Neverwinter Nights: Hordes of the Underdark}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:13`

- Introduction, line 112 (rank, other names):
> "'''Mephistopheles''' ({{Pronounce|me|fiz|TAF|e|leez|refs=<ref name="D93-APG-p28">{{Cite dragon/93/Ay pronunseeAYshun gyd|28}}</ref>}}), sometimes shortened to '''Mephisto'''<ref name="MMII"/> and once under the name of '''Molikroth''',<ref name="Dragon-223-p17.18"/> was the lord of [[Cania]] and most powerful [[archdevil]] next to [[Asmodeus]] himself. [[Hell]]'s greatest [[wizard]] was a walking contradiction, on the surface the cool and calculating '''Cold Lord''' and beneath that the grandiose and hot-headed '''Lord of Hellfire'''.<ref name ="FCII"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:112`

- Plane and realm, 5e fields:
> "| homeplane5e         = [[Nine Hells]]"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:30`
> "| realm5e             = [[Cania]]"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:31`

- Pantheon (line 16), portfolio5e (line 34), portfolio3e (line 64): all empty.

- Alignment, 4e line 43 and 3e line 58:
> "| alignment4e         = [[Evil]]"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:43`
> "| alignment3e         = [[Lawful evil]]"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:58`
The `alignment5e` field (line 28) is empty.

- Domains, 3e, line 65:
> "| domains3e           = [[Diabolic domain|Diabolic]], [[Evil domain|Evil]], [[Fire domain|Fire]]"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:65`

- Symbol, 3e, line 59:
> "| symbol3e            = A flame rendered in copper and gold<br /> A red hand with black nails shrouded in dark flame<br />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:59`

- Typical followers, 5e, line 36:
> "| worshipers5e        = [[Oni]], [[storm giant]]s, [[wizard]]s"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:36`
The 3e line 66 adds: `| worshipers3e        = Disaffected [[devil]]-worshipers, fire worshipers`.

- 5e statistics: `power5e` (line 27) is `[[Archdevil]]`. The wiki gives no 5e challenge rating (no `challenge5e` field). The 5e refs (line 41) are DMG5e-p65-66 and MTOF. The 3e challenge rating is 29: `| challenge3e         = 29` (line 70).

## Field 2: What he wants from a warlock, and what a pact costs

> "Still, even before his recent discoveries, Mephistopheles had some distinct brand of corruption, existing as a patron of magic and the source of many [[warlock]] pacts.<ref name="FCII"/><ref name="Motp4e-p104-105"/> He had the advantage of having the lowest quotas of the archdevils but with the limitation of the highest standards. He and his harvesters specialized in luring skilled wizards and cunning sages into making deals by playing on their curiosity and ambition, the offer of magical might by itself often seen as proof of that mortal's greatness. Most of these types of cultists also sought to crush their rivals with said magical power, and gained the ability to deflect and absorb magic through the deal.<ref name="MTOF"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:249`

> "While skilled, the mortals being lured into Mephistopheles's traps were targeted due to gullibility or ego, and while the arrangement offered them magic it also ensured them misery. Mephistopheles's façade of charm only needed to last until the aspiring caster signed away their soul, and after death they would face decades of tedious routine, deep regret, and isolation to prevent dissent. The agents of Mephisto carefully avoided statements about their lord's behavior and actions, and the clever clauses in the signed soul contracts allowed him to destroy the tricked sages with a word. Sometimes entire wizard guilds and sage conclaves fell under Mephistopheles's sway, as did magic-using beings like [[storm giant]]s or [[oni]].<ref name="MTOF"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:251`

> "Mephistopheles's recent insights into hellfire gave him a new way to appeal to mortals, even despite the fact that it's diabolical nature typically required a sacrifice of the user's own vitality to be called upon.<ref name ="FCIIp89-91"/> The beauty of offering hellfire laid in its accessibility; most types of magic required the user to slowly refine their skills and/or progress along a path of understanding on how to use it, a dangerous road of adventure being a frequently used method. Mephistopheles's cultists could offer the dark energy to even the most inept persons of influence, granting them an easy, painless, path to power, prestige, and dominion.<ref name ="FCII"/> Because this plan was as much a method of gaining souls as it was of increasing Mephistopheles's influence on the Material Plane, being [[lawful evil]] wasn't a barrier of entry to join the cult.<ref name ="FCIIp5.28.41"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:258`

Hellfire is the power he sold. The wiki names the cost as a sacrifice of the user's own vitality, and the soul contract is the cost of the warlock pact. The cited books are FCII, Motp4e, MTOF, FCIIp89-91 and FCIIp5.28.41, so the sources mix editions.

## Field 3: Portfolio and sphere

Portfolio fields (portfolio5e line 34, portfolio3e line 64, portfolio2e line 80, portfolio1e line 94) and sphere fields (spheres2e line 81) are empty. The wiki's description of his area of concern is magic and arcane research:
> "From the wizard's tower that was Mephistar, Mephistopheles performed many tests, to discover more about arcane magic and the nature of the planes,<ref name="MTOF"/> his most recent pet project being his hellfire obsession."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:204`

> "Mephistopheles's great intelligence often ended up mixing with his obsessiveness, as in his pursuit of knowledge he became fascinated with the most minor details."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:140`

## Field 4: Cults, clergy, worship, temples, holy days, messengers

- Cult size, line 247:
> "Mephistopheles was in something of an irritating situation when it came to cults, as despite being second only to Asmodeus, he had one of, if not the, smallest cults out of all the archdevils. Mephistopheles had been so effective in making himself the image of the devil that he had become generic in the eyes of many mortals, frequently confused with and believed to be the same as Asmodeus to the point where the Overlord of Hell left it to him to operate many of his cults.<ref name ="FCIIp5.28.41"/><ref name="FCII"/> Not only that, but further blurring any sense of identity was his symbol, or rather symbols, since he constantly adopted new icons to represent himself.<ref name="BoVD-pp62-63.161-165"/> As someone who adored worship as a god, this mistaken identity was frustrating to no end.<ref name="FCII"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:247`

- Clergy, the hellfire masters and stewards, and the granter, line 264:
> "The Lord of Hellfire offered magical power at unrivaled speed,<ref name ="FCIIp5.28.41"/> for even though other archdevils learnt how to bestow hellfire to their minions, despite his efforts to keep it for himself,<ref name="BoVD4e-pp57"/><ref name="BoVD4e-pp16">{{Cite book/The Book of Vile Darkness/Player's Book|16}}</ref> on top of some warlocks discovering how to tap into Hell's essence while just experimenting with [[eldritch blast]]s,<ref name ="FCIIp89-91"/> Mephistopheles was its original inventor and greatest master, giving him a unique edge.<ref name ="FCII"/> Other [[hellfire warlock]]s had to have a fair amount of magical and extraplanar knowledge to call upon it,<ref name ="FCIIp89-91"/> but the disciples of Mephistopheles, known as hellfire masters and hellfire stewards, had no such obligation. Depending on what the whims of the granter, typically a higher-ranking [[cleric]], even a favored initiate of incredibly low ability could gain access to power surpassing that of many accomplished magic-users.<ref name="BoVD-pp62-63.161-165"/><ref name ="FCIIp5.28.41"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:264`

- Initiation, temples and the Book of Brimstone, line 267:
> "Initiation into Mephistopheles's cult first required a show of cruelty, the sacrifice of an intelligent being in magical flame, typically while the victim was still alive so as to provide screaming chorus to the silent prayers. Temples to Mephistopheles were strange, hidden, distant places often filled with great fire pits in which to conduct a sacrifice, rigged to suddenly flare at the appropriate times and on top of which were slabs of blackened stone to serve as altars for the ritual.<ref name ="FCII"/><ref name ="FCIIp5.28.41"/><ref name="BoVD-pp62-63.161-165"/> A potential aid in this process would be the Book of Brimstone, a tome written in [[Infernal language|Infernal]] by a Mephistopheles worshiping [[monk]], who shortly after writing it went mad and was lost in the Canian wastes. It was rumored that only four copies of the book existed, the first half consisting of the proper ways to worship, adore, sacrifice, and become a disciple of Mephistopheles, among other rites, and the latter a small collection of vile arcane spells.<ref name ="HoHM"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:267`

- Membership and followers, line 269:
> "Hellfire masters were much like Mephistopheles himself; obsessed with fire, donning red and black garb, wielding ranseurs and hiding great anger. On occasions where speech was required, they yelled rather than spoke, infected with their lord's same unpredictable anger.<ref name="BoVD-pp62-63.161-165"/><ref name="BoVD4e-pp57"/> They were capable of independent action and working in groups equally well, whether their partners were wicked schemers, violent megalomaniacs, devils, or other wicked fire creatures like [[hell hound]]s or [[salamander]]s. Apart from those looking for easy power, Mephistopheles promoted himself as a "god of hellfire" to those who revered flame, as well as devil worshipers that had become dissatisfied with their current archdevil patrons. [[Fire giant]]s were known for their attempts to become hellfire masters,<ref name="BoVD-pp62-63.161-165"/> and Mephistopheles was known to try to appeal to [[frost giant]]s as well.<ref name= "FCAII"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:269`

- Messenger word, line 187 (the gelugons' role in Cania, not a cult messenger):
> "Only the gelugons, the primary residents and second in authority only to the pit fiends, although they were mainly guards, servants, and messengers, could comfortably exist in Cania.<ref name="GTH"/><ref name="PoLB"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:187`

- Holy days: the fields `holy days5e` (line 39), `holy days4e` (line 54) and `holy days3e` (line 69) are empty. The wiki gives no omen for him.

## Field 5: Relations and origin

**Asmodeus (relations).** Line 237:
> "Perhaps Mephistopheles's strangest relationship was with his master Asmodeus, for he was the Prince of Evil's most dangerous enemy and most capable ally. Despite Mephistopheles making it abundantly clear that he dreamt of the day when he could depose his lord, Asmodeus still seemed to trust the counsel of his boundlessly jealous companion when offered. The relationship was further clouded by the existence of [[Glasya]], to whom Mephistopheles was something of a godfather.<ref name="FCII"/><ref name="DMG5e-p65-66"/><ref name="Motp4e-p104-105"/><ref name="TPA-67">{{Cite book/The Plane Above|67}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:237`

> "Several reasons behind this relationship, (Mephisto's rivalry with Baalzebul and the usefulness of Baalphegor), had been presented, but a more simple and underlying possibility also existed.<ref name="FCII"/><ref name="Motp4e-p104-105"/><ref name="TNH26-31"/> Mephistopheles was potentially the only individual archdevil that Asmodeus feared, whose mastery of hellfire, knowledge of ancient secrets, and duty as guard of his realm made him a deadly and great enough asset to tolerate his threats. Though Mephisto couldn't yet oppose Asmodeus, both watched to see if circumstances changed the nature of the situation, the Lord of Hellfire waiting until his adversary made a big enough miscalculation for him to make his move.<ref name="FCII"/><ref name="DMG5e-p65-66"/><ref name="Motp4e-p104-105"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:239`

**Other archdevils.** Line 229 (Baalzebul, the rival):
> "Among the archdevils, Mephistopheles wasn't looked upon with particular favor, the result of his blatant arrogance and unstable personality.<ref name="FCII"/> His greatest and most obvious rival was Baalzebul, each regarding the other with bitter hate and seeing one another as their biggest obstacle to taking the throne of Hell, although their hatred did have other roots. Like Dispater, the ancient Archduke of Cania saw Baalzebul's rapid promotion as worthy of enmity, while Baalzebul had come to see everyone else as responsible for his transformation into a slug, especially Mephistopheles. Each conspired against each other, the hatching of plans taking up a great amount of time and their more open antagonism towards each other being part of the reason Asmodeus left them in charge.<ref name="FCII"/><ref name="BoVD-pp62-63.161-165"/><ref name="GTH"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:229`

> "Among Mephistopheles's actual allies, at least nominally, was the Iron Duke Dispater, the two of which shared seniority and a desire for knowledge.<ref name="MTOF"/><ref name="GTH"/> Dispater was drawn to Mephistopheles's power and respected him as a true member of the baatezu race, unlike the relative upstart Baalzebul, although recently, Dispater tried to present himself as a friend to all and enemy of none, distancing himself from allies and trying to make peace with rivals in a futile attempt to assuage his paranoia.<ref name="FCII"/><ref name="GTH"/><ref name ="FCIIp5.28.41"/> On top of that, Mephistopheles's court had to be on constant alert for Dispater's agents, as the secret-loving archdevil was pained by the idea that Mephistopheles knew something he didn't.<ref name="MTOF"/> Once the two of them were allies with the greedy [[Mammon]], but the speed with which the spineless serpent sold them out at the end of the Reckoning marked him as undesirable to all archdevils.<ref name="BOVD149-159"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:235`

> "Also on the Cold Lord's mental radar was the Frozen Prince Levistus, who he carefully kept an eye on.<ref name="GTH"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:233`

**Origin and rise, edition as cited.** Line 277 (cites FCIIp5.28.41 and others):
> "Mephistopheles was an ancient entity, a being rivaling even Asmodeus in terms of age, and during his time as an archdevil he had been responsible for many infernal innovations aside from hellfire.<ref name ="FCIIp5.28.41"/> Millenia ago, he had entrapped a race of mercenary fiends similar to the [[mezzoloth]]s in Hell, keeping them in a state of perpetual servitude and giving rise to the gelugon baatezu.<ref name="Motp4e-p104-105"/> The fiendish surgeons within his palace augmented a breed of [[hell hound]]s, the fearsome Nessian warhounds, with even greater abilities, making Mephisto's pit hounds even stronger, bigger, crueler and fiery than Asmodeus's.<ref name ="HoHM"/> He captured the blood and tears of Baalphegor in a vial to create a powerful artifact known as Baalphegor's Grace, allowing the user to summon a group of [[erinyes]] known as the ''Blessed Angels'' that were ultimately loyal to him, although he originally intended to loan it to favored cultists before he lost track of it.<ref name="D135"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:277`

Line 279 (Molikroth and the Reckoning, citing Motp3 and BoVD):
> "One of his infamous schemes was before the [[Reckoning]], when he donned a secret identity as the archdevil Baron Molikroth. He "deposed" himself using this alter ego and ruled for a great amount of time before finally revealing his true identity. The traitors who co-conspired with Molikroth to overthrow Mephistopheles were ended along with the deception.<ref name="Motp3-pp122-123"/><ref name="BoVD-pp62-63.161-165"/> When the Reckoning actually occurred and Mephistopheles's faction of Dispater, Mammon, and [[Geryon]], went up against Baalzebul's faction of [[Zariel]], Belial and [[Moloch]], his entire plan was undermined by a spy in his ranks; Geryon. Geryon was secretly siding with Asmodeus, and with a blow of his horn, the pit fiend generals of both armies turned against them. Despite the blatancy of his rebellion against Asmodeus, he was perhaps the archdevil that suffered the least, not cursed like Mammon or Baalzebul, cast down like Zariel, Belial, Geryon or Moloch nor left to stew in his own paranoia like Dispater.<ref name="GTH" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:279`

Line 292 (the Spellplague ascension, citing SS and TG):
> "Mephistopheles's plans to become a god finally came to some form of fruition during the [[Spellplague]]. Mephistopheles had persuaded his half-breed son, [[Magadon]], to release the devil inside of him and therefore bring himself and his fellow companions [[Erevis Cale]] and [[Drasek Riven]] to Cania through some manipulation of Cale's ability to travel through shadows. Mephistopheles then proceeded to kill his half-breed son after Erevis promised Mephistopheles a portion of the god [[Mask]]'s divinity. He did this as part of the agreement, not that he discussed it with Cale, saying that he would kept half of Magadon's soul with him as collateral until the delivery. Erevis later returned to Cania and sacrificed his life for the return of Magadon's soul, giving Mephistopheles the divinity he so desired, although with an unexpected cost.<ref name="SS"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:292`

Line 181 (his realm, Cania):
> "Mephistopheles's realm was the gloomy, frigid wasteland of Cania<ref name ="FCII"/> a realm of cold indescribable with words<ref name="GTH"/> so bitter that it was practically alive.<ref name="Motp3-pp122-123"/><ref name="Motp1pp109-111"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:181`

## Field 6: Campaign and published-adventure mentions

- Campaign: `asmodeus.md:51` (quoted at the top of this report). No other campaign line.
- Published adventure: no hit in `sources/adventure-wdh.json` or `sources/adventure-wdmm.json` for any alias.
- Wiki Waterdeep lines (Q3). Line 283:
> "Not too long after [[1372 DR]], a [[drow]] matron known to history only as the [[Valsharess]] managed to bind Mephistopheles into her service on the material plane, in [[Toril]]. Aided by his powers, she proceeded to conquer much of the [[Underdark]], and even went on to try to expand her influence on the surface, attacking [[Waterdeep]] through [[Undermountain]].<ref name="NWNHoTU">{{Cite game/Neverwinter Nights: Hordes of the Underdark}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:283`

Line 285 (caption of the image; file-link brackets dropped):
> "File:Meph_waterdeep.jpg|thumb|330px|Mephistopheles arrives in Waterdeep."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:285`

Line 286:
> "Previously, an [[Drogan Droganson's pupil|adventurer]] fleeing the briefly re-activated, but once again falling, [[Netheril|Netherese]] city of [[Undrentide]] into the [[Plane of Shadow]] had come across a strange relic that they had used occasionally to access the small plane of a strange creature known as the [[Reaper (Neverwinter Nights)|Reaper]]. This item was in fact meant for the leader of a cult of Mephistopheles, and contained a piece of the devil's own flesh. Later the adventurer, by then quite famous and powerful, came to Waterdeep to aid the city in its struggle against the Valsharess's forces. Mephistopheles manipulated the Valsharess to eventually bring the adventurer into her inner sanctum, where she ordered him to kill them. At this point, her control over Mephistopheles was loosened, since the relic carried by the adventurer bound them to the archdevil, and by ordering him to kill the adventurer she broke the pact which she used to bind him.<ref name="NWNHoTU"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:286`

Line 288:
> "Instead of complying, Mephistopheles left the adventurer and his party free to duel and kill the Valsharess. He then sent them to Cania in his stead and set out to conquer Toril, intending to turn it into a new layer of Hell that would go down below the Ninth and make him the new supreme ruler of the plane. He raised the dead souls he had gained from the recent battles between the Valsharess and her enemies as a special form of spiritual army and began to follow a similar course of conquest to hers, advancing from the Underdark to Waterdeep. However, the adventurer, who had by this point grown in power far beyond that of most other mortals, was able to escape Cania by learning the Reaper's [[true name]], ''Hecugoth the Abandoned''. They returned to Toril and banished Mephistopheles back to his old domain before he could destroy the City of Splendors. It could be deduced that since Mephistopheles remained a threat to the planes as nobody's slave, the adventurer either did not learn ''his'' true name or simply chose not use it to its full potential for whatever reason.<ref name="NWNHoTU"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:288`

Line 274 (an aspect "rumored" to be trapped in Undermountain; not a cult or temple):
> "Mephistopheles used aspects in many situations, and they weren't afraid of death knowing that they'd be recreated if destroyed. On the rare occasion when they left the Nine Hells to create new converts, they would mix with almost any society, devil or mortal, and sometimes even venture into the battlefield of the [[Blood War]]. They irregularly appeared in the [[Faerun|Realms]], normally bringing several other devils with them when they did, and it was rumored that an aspect of him was trapped in [[Undermountain]].<ref name= "FCAII"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mephistopheles/wiki.txt:274`

## Field 7: Conflicts and not found

- **Conflict (edition):** the wiki gives a 3e and 4e account of the Reckoning (line 279) and a 5e MTOF account of his character (lines 153 and 249 cite MTOF for the pact text). The wiki does not choose between them. The wiki has no 5e challenge rating for him (Field 1).
- **Conflict (Asmodeus relation, wording):** asmodeus.md:51 calls Mephistopheles "his greatest ally and chief rival". The wiki (line 237) calls him "the Prince of Evil's most dangerous enemy and most capable ally". The substance agrees; the wording differs.
- **Not found:** holy days (fields empty, lines 39, 54, 69), omens, a messenger of the cult (line 187 is a devil role), a cult shrine or temple in any Waterdeep source, any campaign NPC, faction or quest that uses him.

---

# 2. Mammon

Wiki page: `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt`. Wiki keys (book as the wiki names it): FC2 = Fiendish Codex II: Tyrants of the Nine Hells (line 12, for example FC2-p145). MToF = Mordenkainen's Tome of Foes, cited as 5e (line 39). BoVD = Book of Vile Darkness (line 70). Motp4e-p100-101 = Manual of the Planes 4th edition (line 12). Dragon-223-pp14-15 = Dragon 223, The Lords of the Nine (line 13). Dragon-75-pp24-26 = Dragon 75, The Nine Hells (line 148). GTH-31.40-41.46 = Guide to Hell (line 108). FAII = Fiendish Codex II Fiendish Aspects, a web article dated 2007-02-16 (line 117). DMG64 = Dungeon Master's Guide 5th edition, p. 64 (line 119). NHR = Dragon 91, Nine Hells Revisited (line 138). Dun197-2-5 = Dungeon 197, Codex of Betrayal: Glasya (line 128). TPA = The Plane Above (line 173). ApiH-p28 = A Paladin in Hell, p. 28 (line 207). TBOVD55 = The Book of Vile Darkness, Dungeon Master's Book, p. 55 (line 124). MMII-p47 = Monster Manual II, 1st edition (line 97).

## Answers

**(1) Waterdeep cult, shrine or temple.** None. The wiki places Mammon's aspects in the alleys of Waterdeep (line 204, quoted below). That is an aspect's presence, not a cult, shrine or temple. No campaign file or published-adventure line names a Mammon temple in Waterdeep. The WDH temple table has no Mammon row.

**(2) Campaign NPC, faction or quest.** None. asmodeus.md:51 is the only campaign line ("Mammon fawns").

**(3) Wiki lines that mention Waterdeep.** Line 204 only.

## Field 1: Identity

- Titles, line 12:
> "| title               = Lord of the Third<ref name="FC2-p145">{{Cite book/Fiendish Codex II: Tyrants of the Nine Hells|145-146}}</ref><br/>Lord of Avarice<ref name="Dragon-75-pp24-26">{{Cite dragon/75/The Nine Hells|24-26}}</ref><br/> Lord of Lust<ref name="BoVD-pp60-61">{{Cite book/Book of Vile Darkness|60-61}}</ref><br/> King of Greed<ref name="Motp4e-p100-101">{{Cite book/Manual of the Planes 4th edition|100-101}}</ref><br/> King of Covetousness<ref name="BoVD-pp60-61"/><br/> Archduke of Minauros<ref name="DMG64">{{Cite book/Dungeon Master's Guide 5th edition|64}}</ref><br/>Viscount of Minauros<ref name="Dragon-223-pp14-15">{{Cite dragon/223/The Lords of the Nine|14-15}}</ref><br/>The Serpent<ref name="Dragon-223-pp14-15"/><br/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:12`

- Aspects, line 13:
> "| aspects             = Minauros<ref name="Dragon-223-pp14-15"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:13`

- Opening, line 108:
> "'''Mammon''', sometimes referred to as '''Minauros''', was the lord of the identically named [[Minauros]],<ref name="Dragon-223-pp14-15"/> and potentially the richest being in existence.<ref name="MToF-pp12.20, 170-171"/> Both literally and figuratively two-faced, the [[archdevil]] viscount was a feckless miser whose only loyalty was to coin.<ref name="MToF-pp12.20, 170-171"/><ref name="GTH-31.40-41.46"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:108`

- Plane and realm (5e):
> "| homeplane5e         = [[Nine Hells]]"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:27`
> "| realm5e             = [[Minauros]]"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:28`

- Alignment: `| alignment4e         = [[Evil]]` (line 41); `| alignment3e         = [[Lawful evil]]` (line 56). `alignment5e` (line 25) is empty.

- Domains, 3e, line 63:
> "| domains3e           = [[Diabolic domain|Diabolic]], [[Evil domain|Evil]], [[Greed domain|Greed]], [[Trickery domain|Trickery]]"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:63`

- Symbol, 3e, line 57:
> "| symbol3e            = An open pair of scaled, red hands looming above a diamond-shaped black gem.<br/> A medallion-sized coin emblazoned with Mammon's serpentine form."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:57`

- Worshipers, 5e, line 33:
> "| worshipers5e        = [[Dragon]]s, [[duergar]]"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:33`
The 3e row (line 64) reads: `| worshipers3e        = [[Beholder]]s, [[dragon|evil dragon]]s, [[mind flayer]]s`.

- 5e statistics: `power5e` (line 24) is `[[Archdevil]]`. The 5e challenge rating field (line 37) is blank, so the wiki gives no 5e challenge rating for Mammon. The 3e challenge rating is 25: `| challenge3e         = 25` (line 68). The 5e refs (line 39) are `MToF-pp12.20, 170-171`.

## Field 2: What he wants from a warlock, and what a pact costs

> "If you must make a deal with a devil, Mammon might be your best option. Unfortunately, you need the wealth of a dozen kingdoms to close the deal if you don't want to offer your soul."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:186`
(The text sits in the quote box whose source is Mordenkainen, citing MToF.)

> "Mammon's area of expertise was not diplomacy but the soul trade, and after realizing his inability to form new relationships with the major figures of Hell, he devoted himself to it further. Of all the archdevils, his efforts to reap souls always proved the most bountiful, and he did so, as one might expect, with his raw affluence. As patron of the greedy and lustful, Mammon drew in the materialistic mortals that not only desired the pleasures of wealth but the pleasure of denying it to others, spreading their avarice like a virulent plague.<ref name="MToF-pp12.20, 170-171"/><ref name="FC2-p145"/> He also, based on the principle that "money is the root of all evil", incited the rich and powerful into abandoning acts of charity, sabotaged industries, and bankrupted once prosperous nations. In his mission to cause economic collapse, he had sent a vast number of his devils to mortal realms, each desperate to sow desperation and send the millions in destabilized regions to Minauros.<ref name="FC2-p45-50"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:188`

> "The King of Avarice was one of the few archdevils willing to barter in gold as opposed to souls and any surplus petitioners were appropriated and sold for money.<ref name="MToF-pp12.20, 170-171"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:154`

The wiki gives no Fiend-patron pact text for Mammon. His cult initiation is a betrayal, quoted in Field 4.

## Field 3: Portfolio and sphere

The portfolio fields are blank (`portfolio5e` line 31, `portfolio3e` line 62, `portfolio2e` line 78). The wiki names his area of expertise in line 188 (the soul trade, quoted above) and his greed in line 108 (quoted above). Line 122 gives the personality:
> "Mammon was an utterly selfish entity that practically personified greed with his insatiable desire."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:122`

## Field 4: Cults, clergy, worship, temples, holy days, messengers

- Cults in high society and merchant guilds, line 192:
> "Mammon's influence on the Material Plane wasn't limited to lone scammers, for he also had widespread cults. Having gained exorbitant wealth from dirty dealings, coercion, and extortion, such cultists could be found at the peak of high society<ref name="BoVD-pp148-149" /><ref name="FC2-p145"/> and in merchant or trade guilds. The powers offered by Mammon allowed his followers to thieve and deceive with almost supernatural skill, grasping unkept items from several feet away and manipulating the idea of value and where it laid in the minds of others. Races typically found underneath Mammon included [[duergar]]<ref name="MToF-pp12.20, 170-171"/> and [[goblinoid]]s, along with several less conventional worshipers like [[beholder]]s. [[Illithid]]s were also in his ranks to the point where he had a special team of information gatherers comprised of them, as well as the more interactive of evil dragons,<ref name="BoVD-pp60-61"/><ref name="BoVD-pp148-149" /> them being his most favored followers.<ref name="FC2-p145"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:192`

- Temples, line 201 (cites FC2 and BoVD):
> "Mammon's temple were obscenely ornate and ungodly gaudy, showcasing so much treasure that the raw garishness bordered on ridiculous. True to Mammon's nature, the lairs and implements within weren't so much tools to protect their wealth but wealth that also performed a function. From the altars, to the sacrificial daggers, to the temples themselves, almost everything was made of gold and adorned with gemstones. Cultists prospered by using temples as locations for back-alley deals, conspiring together and making commercial pacts within that would carry out into the wider world.<ref name="FC2-p19-20.26-27"/> Temples were chocked full of wards, traps and guardians appropriate for defending such riches, often the types of non-[[humanoid]] monsters that served as Mammon's cultists.<ref name="FC2-p19-20.26-27"/><ref name="BoVD-pp148-149" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:201`

- Initiation and the covetors (clergy), line 199:
> "Mammonian cult initiation required the neophyte to betray their closest friend for personal gain and perform a perverse ritual as demeaning as it was disgusting.<ref name="BoVD-pp60-61"/> Such behavior was in line with the gross service provenly loyal cultists could have to endure if invited to Mammon's court. While horrendous, attending his court could curry wealth beyond the imagination of mortals.<ref name="FC2-p145"/> One such regular attendee was the former [[cleric]] of [[Hextor]], [[Zbavra]], and other notable cultists included the [[dwarf]] [[Dorban Smokestone]] and the illithid [[Ruulam]]. Mammonian clerics, also known as covetors, wore gold-trimmed red robes and golden ornamentation.<ref name="BoVD-pp148-149" /> [[Rogue]]s and [[bard]]s, typically those interested in money rather than murder, could occasionally be found as his disciples.<ref name="BoVD-pp60-61"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:199`

- Rite, line 196 (source: Zbavra, BoVD):
> "Almighty Mammon, lord of lust and king of covetousness, I call upon your great might to get what I want. I prostrate myself before you and your relentless power. Bring me my heart’s desire."
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:196`

- Holy days: the holy-day fields (lines 36, 52, 67, 82, 95) are blank. The wiki gives no omen and no messenger. The word "herald" (line 159) appears only in an image caption about Titivilus, herald of Dispater, and is not a Mammon messenger.

## Field 5: Relations and origin

- Tiamat, Dispater, Mephistopheles and Asmodeus, line 160:
> "Despite being one of the Lords of the Nine, Mammon was considered a lesser archdevil in Hell's political sphere. He was hopelessly lacking in allies among the other Lords of the Nine, and even [[Tiamat]] despised him for stealing her [[dragon]] worshipers by appealing to their greed.<ref name="FC2-p145"/> Though he was once in an alliance with [[Dispater]], and by extension [[Mephistopheles]], he likely never trusted the Iron Duke in the first place.<ref name="MMII-p47"/> He almost instantly began groveling before Asmodeus the moment the Overlord proved victorious, betraying both his partners without a second thought, thus earning him the suspicion and scorn of every other archdevil.<ref name="BoVD-pp148-149"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:160`

- Glasya, line 162:
> "Mammon had a particularly complex relationship with the relatively new archdevil and his former consort, [[Glasya]]. It was said that her position as Mammon's concubine wasn't something she had set out to claim, but a form of punishment placed upon her by Asmodeus. The spoilt Princess of Hell, accustomed to the comforts of [[Nessus]], was forced to endure the disgusting advances of the Serpent and the backwater slum that was his layer.<ref name="Dun197-2-5"/> Still, others posited that she came to Minauros willingly, possibly out of some form of genuine affection or merely as a way to annoy the other archdevils, particularly her father, before the Lord of Nessus broke off their relationship.<ref name="BoVD-pp167">{{Cite book/Book of Vile Darkness|167}}</ref><ref name="FC2-p61-62">{{Cite book/Fiendish Codex II: Tyrants of the Nine Hells|61-62}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:162`

- Seneschal and dukes, line 167:
> "While Mammon was the master of Minauros in name, he often neglected it, leaving such matters to his seneschal [[Focalor]]. Respectful but silent, Focalar handled the administration, diplomacy, and security of Minauros in his master's absence, as well as the protection of Glasya during her time as his consort. Despite appearing completely loyal, having resisted the constant temptations by rival archdevils to win him over to their side, Focalar hated his master for his incompetence and irresponsibility. He willingly worked with Glasya when he was her bodyguard, using his actual awareness of the political sphere to undermine Mammon with intent to destroy him.<ref name="Dragon-75-pp24-26"/><ref name="Dun197-2-5"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:167`

- Daughter, line 173:
> "Mammon also had a daughter, [[List of Archdevils#Baelzra|Baelzra]], born of neither Glasya nor Glwa but an affair had with the bloated archdevil [[List of Archevils#Sagirsa|Sagirsa]], queen of [[Jangling Hiter]]. The Chain Princess lacked the unsightliness one would expect from the child of Mammon and a former paeliryon, but only because her inner grotesquery surpassed even that of her father. Her illegal soul-harvesting operation on Avernus secretly netted the King of Greed some soul-profit, and he still doted on her despite her exile.<ref name="Motp4e-p100-101" /><ref name="TPA">{{Cite book/The Plane Above|70-75}}</ref><ref name="FCII-p51">{{Cite book/Fiendish Codex II: Tyrants of the Nine Hells|48}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:173`

- Origin and rise, line 207 (cites A Paladin in Hell and BoVD):
> "As the first to retreat before and submit beneath Asmodeus after the disaster that was the [[Reckoning]], Mammon was left disgraced and, despite his kowtowing, punished. His relationship with Glasya was ended,<ref name="GTH-31.40-41.46"/> but his real punishment began once he changed his name to Minauros.<ref name="ApiH-p28">{{Cite book/A Paladin in Hell|28}}</ref> Asmodeus changed Mammon's natural form, possibly for his own reasons and possibly because Mammon asked him to as a sign that he was a "new devil" that wouldn't betray him,<ref name="BoVD-pp148-149" /><ref name="GTH-31.40-41.46"/> into one resembling [[Geryon]], the only archdevil that had stayed loyal to Asmodeus during the Reckoning.<ref name="ApiH-p28"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:207`

## Field 6: Campaign and published-adventure mentions

- Campaign: `campaign/setting/deities/asmodeus.md:51` ("Mammon fawns"; quoted at the top of this report).
- Published adventure: none in `sources/adventure-wdh.json` or `sources/adventure-wdmm.json`.
- Wiki Waterdeep line (Q3), line 204:
> "Mammon's aspects were abundant in [[Faerun]], often under the guise of a [[yuan-ti]], spreading and encouraging avarice in order to more easily manipulate mortals. They found sunny climates unpleasant, being used to the polluted dampness of Minauros, and were rarely found in natural settings. Instead they lurked in urban areas, anywhere from behind the walls of the [[Zhentil Keep]], to the streets of [[Sembia]], to the alleys of [[Waterdeep]]. Even in terms of fighting, they were greedy creatures with a "me first" attitude that impeded their ability to work in concert with their servants. Part of the reason for their rapaciousness, outside of it being in their nature, was that they had no possessions outside of special gear given for their assignment; all other acquired goods were sent to Mammon, leaving them with nothing but unfulfilled desire.<ref name= "FAII"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:204`

## Field 7: Conflicts and not found

- **Conflict (form):** line 117 says Mammon's natural form "was eventually changed into one resembling certain [[yuan-ti halfblood]]s":
> "Mammon's original form was traditionally infernal, a {{SI|12|ft}} tall creature that resembled a flabby [[pit fiend]] with scaly, red-gold skin and wings that were as lustrous as rubies.<ref name="MMII-p47"/> Although still able to assume his old form, Mammon's natural appearance was eventually changed into one resembling certain [[yuan-ti halfblood]]s, albeit {{SI|30|ft}} long.<ref name="GTH-31.40-41.46">{{Cite book/Guide to Hell|31.40-41.46}}</ref><ref name= "FAII">{{Cite web|url=http://archive.wizards.com/default.asp?x=dnd/we/20070216a|title=Fiendish Codex II Fiendish Aspects|accessdate=2020-04-029|author=[[Robert Wiese]]|publisher=[[Wizards of the Coast]]|date=2007-02-16}}</ref> His lower half was that of an enormous, spotted serpent with yellow-brown skin comparable to swirled vomit, while his upper half sported a muscular humanoid torso with bony spines protruding across his shoulders and along his large arms.<ref name= "FAII"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/mammon/wiki.txt:117`
Line 207 (quoted under Field 5) says Asmodeus changed him "into one resembling Geryon". The two lines name different forms (yuan-ti halfblood, citing GTH and FAII; Geryon, citing ApiH and BoVD). The wiki gives no ruling.

- **Conflict (titles):** the title row (line 12) gives "Archduke of Minauros" (DMG 5e, p. 64) and "Viscount of Minauros" (Dragon 223). The body (line 108) calls him "the archdevil viscount". Both are quoted.
- **Not found:** holy days, omens, messengers, a Mammon temple or cult in Waterdeep, and any campaign NPC, faction or quest that uses him.

---

# 3. Orcus

Wiki page: `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt`. Wiki keys (book as the wiki names it): OotA-p244-245 = Out of the Abyss, 5e (line 42). MM5e-p52 = Monster Manual 5th edition (line 42). FCI-p73-74 = Fiendish Codex I: Hordes of the Abyss, 3e (line 73). FCI-127-128 = Fiendish Codex I pp. 127-128 (line 243). MToF-p26-29 = Mordenkainen's Tome of Foes, 5e (line 117). MM4e-p206 = Monster Manual 4th edition (line 113). MotM-p203-204 = Mordenkainen Presents: Monsters of the Multiverse (line 57). ToB-p75-77 = The Throne of Bloodstone (line 123). ToM-p48 = Tome of Magic 3.5 (line 13). DD-p23-25 = Demihuman Deities (line 18). LM-p18 = Libris Mortis (line 113). DrM359.MWV-p62 = Dragon 359, 1d20 Villains (line 113). DrM417.STW-p12-14 = Dragon 417, History Check: The Shadow that Was (line 113). Dead Gods-p6-9 = Dead Gods (line 143). GEP-p47 = A Guide to the Ethereal Plane (line 270). Demonomicon-p8 = Demonomicon of Iggwilv (line 113). FP-p113 = Faiths and Pantheons (line 192). BL-p6 = The Bloodstone Lands (line 227).

## Answers

**(1) Waterdeep cult, shrine or temple.** None. The wiki has no Waterdeep mention (grep for Waterdeep, Waterdhav, Dock Ward, Undermountain, Sea Ward, North Ward, Trollskull and Yawning Portal returned no matches). The only Orcus temple location quoted is Deepearth (line 222), which is not Waterdeep. The WDH table has no Orcus row.

**(2) Campaign NPC, faction or quest.** None.

**(3) Wiki lines that mention Waterdeep.** None.

## Field 1: Identity

- Titles, line 13:
> "| titles         = Lord of the Undead<br /> Lord of Undeath<ref name="DuM149-p52">{{Cite dungeon/149/Enemies of My Enemy|52}}</ref><br /> Prince of the Undead<ref name="BW-p4">{{Cite book/The Bloodstone Wars|4}}</ref><br /> Prince of Undeath<br /> Blood Lord<br /> Lord of Specters<br /> Master of Vampires<br /> The Goat-Horned Demon<ref name="MoB-p22">{{Cite book/The Mines of Bloodstone|22}}</ref><br /> Sovereign of Thanatos<ref name="DuM149-p52" /><br /> Keeper of Everlost<ref name="DuM149-p52" /><br /> Master of the Last Word<ref name="DuM149-p52" /><br /> Mighty Orcus<ref name="DuM149-p52" /><br /> The Shadow That Was<ref name="ToM-p48">{{Cite book/Tome of Magic 3.5|48}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:13`

- Aspects, line 14:
> "| aspects             = Tenebrous<ref name="Dead Gods-p36">{{Cite book/Dead Gods|36}}</ref><ref name="wnw">{{Cite game/Neverwinter Nights: Tyrants of the Moonsea}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:14`

- Introduction, line 113:
> "'''Orcus''', also known as '''Tenebrous'''<ref name="ToM-p48" /><ref name="DD-p23-25" /><ref name="DrM359.MWV-p62" /> was a [[demon lord|demon prince]] and purported [[primordial]]<ref name="MM4e-p52">{{Cite book/Monster Manual 4th edition|52}}</ref> that served as master of the [[undead]] from the depths of the [[Abyss]].<ref name="OotA-p244-245" /><ref name="Demonomicon-p8">{{Cite book/Demonomicon|8}}</ref> Returned from undeath but not technically alive, the '''Demon Lord of Undeath''' was the multiverse's staunchest advocate for stagnation, seeking to exterminate all life, to darken and desolate all worlds, until all that remained in his static reality were undead moved only by his will.<ref name="OotA-p244-245" /><ref name="FCI-p73-74" /><ref name="MM5e-p52" /><ref name="MToF-p26-29" /> The '''Blood Lord'''<ref name="OotA-p244-245" /> was believed to be one of the mightiest demon lords, one that inspired dread in the hearts of [[god]]s.<ref name="MM4e-p206">{{Cite book/Monster Manual 4th edition|206}}</ref> '''The Shadow That Was'''<ref name="DrM417.STW-p12-14" /> was among the powers of the Abyss most often worshiped as deity by the mortals of the [[Prime Material plane]] and, even more than the [[Demogorgon|Prince of Demons]] himself, was close to obtaining true divinity.<ref name="FCI-p73-74" /><ref name="LM-p18" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:113`

- Home and layer note, line 18:
> "| home                = [[Thanatos (layer)|Thanatos]]<ref name ="DD-p23-25" /><ref name="ToB-p46">{{Cite book/The Throne of Bloodstone|46}}</ref><ref name="OHG-p180">{{Cite book/On Hallowed Ground|180}}</ref><ref group="note" name="Layers">In ''[[The Throne of Bloodstone]]'', Orcus's realm is the 333{{rd}} layer of the Abyss. In the [[Dungeons & Dragons]] sourcebook ''[[Fiendish Codex I: Hordes of the Abyss]]'' and Planescape sourcebook ''[[On Hallowed Ground]]'', his realm is the 113{{th}} layer. The 333{{rd}} was attributed to the deity [http://dragonlancenexus.com/lexicon/index.php?title=Hiddukel Hiddukel] of [[Krynn]] and called [[Broken Scale]].</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:18`

- Plane and realm, 5e: `| homeplane5e         = [[Abyss]]` (line 32); `| realm5e             = [[Thanatos (layer)|Thanatos]]` (line 33).

- Alignment: `alignment5e` (line 30) `[[Chaotic evil]]`; `alignment3e` (line 59) `[[Chaotic evil]]`.

- Domains, 3e, line 66:
> "| domains3e           = [[Chaos domain|Chaos]], [[Death domain|Death]], [[Demonic domain|Demonic]], [[Evil domain|Evil]]"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:66`

- Domains and undeath, line 136:
> "The Prince of the Undead held dominion over the [[portfolio]] of [[undeath]], and held influence over the [[divine domain|domains]] of [[chaos domain|chaos]], [[death domain|death]], [[evil domain|evil]], [[darkness domain|darkness]],<ref name="LM-p18" /> and [[undeath domain|undeath]].<ref name="F&P-p221">{{Cite book/Faiths and Pantheons|221}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:136`

- Symbol, 3e, line 60:
> "| symbol3e            = A black, skull-topped [[mace]]"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:60`

- Symbol, described in the worship section, line 227:
> "Orcus' holy symbol was described as the horned head of a [[goat]],<ref name="BL-p6">{{Cite book/The Bloodstone Lands|6}}</ref><ref name="LM-p18">{{Cite book/Libris Mortis|18}}</ref> sometimes set over a skull-topped mace.<ref name="AM-p45">{{Cite adventurers league/Assault on Maerimydra|45}}</ref> This symbol was not universally used throughout his cult however. Some cells adopted similar, but distinctly different iconography.<ref name="MM4e-p210">{{Cite book/Monster Manual 4th edition|210}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:227`

- Challenge rating: the template closes on line 112 with `|challenge5e=26}}`, so the wiki gives a 5e challenge rating of 26. That field has no citation of its own. The 5e refs (line 42) are OotA-p244-245 and MM5e-p52. The 3e challenge (line 71) is 28: `| challenge3e         = 28`.

- Power: `power5e` (line 29) `[[Demon lord]]`; `power4e` (line 43) is empty; `alignment4e` (line 44) `[[Chaotic evil]]`.

- Worshipers, 5e (line 38): empty.

## Field 2: What he wants from a warlock, and what a pact costs

> "Orcus did grant limited powers to the meager mortals that slew others in his name, transforming them into mindless [[zombie]]s or [[ghoul]]s.<ref name="OotA-p244-245" /> He was said to have made a [[bonegouge assassin|unique form of undead]] from among the members of a single guild of [[assassin]]s.<ref name="Demonomicon-p106">{{Cite book/Demonomicon|106}}</ref> Orcus would also bless some demons with transformation into undeath,<ref name="MM5e-p52">{{Cite book/Monster Manual 5th edition|52}}</ref> the most revered example of which involved the creation of a [[devourer]].<ref name="MotM-p93">{{Cite book/Mordenkainen Presents: Monsters of the Multiverse|93}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:138`

> "Leaders within the various cults of Orcus were known as Skull Lords. To attain this title, Orcus' followers were tasked with taking control of a horde of undead from the [[Plains of Hunger]] and setting them loose in an invasion upon the prime material plane. Those that failed were slain and raised as liches, doomed to dwell within Thanatos for eternity.<ref name="FCI-127-128" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:217`

The warlock link (the only warlock wording for Orcus in the wiki), line 270:
> "The lost divinity of Tenebrous existed as a wandering essence of the planes, a vestige that could be called upon by [[warlock]]s.<ref name="ToM-p48" /><ref name="GEP-p47">{{Cite book/A Guide to the Ethereal Plane|47}}</ref> Orcus came to fear the possibility that if this vestige were restored to power, the personality of Tenebrous might subsume him, thus when the activities of a [[githyanki]] rebel known as [[Kastya Zurith-Movya]] threatened to create a conduit for Tenebrous to revive, Orcus forged a pact with the Lich-Queen [[Vlaakith CLVII]] to oppose him.<ref name="EE-p130">{{Cite book/Exemplars of Evil|130}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:270`

## Field 3: Portfolio and sphere

Line 136 (quoted in Field 1) gives the portfolio: "the portfolio of undeath". `portfolio5e` (line 36) is empty. The wiki's personality paragraph, line 128, is the area of concern:
> "Orcus was wholly misanthropic and self-absorbed with his hatred of all things,<ref name="LM-p18" /> a nihilistic and brooding being<ref name="MM5e-p52" /> who sought to put an end to all hope.<ref name="MToF-p26-29" /> He cared for nothing save himself—not even his devotees and undead servants—and focused only on spreading the evil and agony that resided within him. Despite his all-consuming hatred towards existence itself,<ref name="LM-p18" /> Orcus was not an aimless force of chaotic destruction. Rather he was an exceedingly brilliant strategist,<ref name="ToB-p75-77" /><ref name="FCI-p73-74" /> wholly consumed with inflicting agony upon those he despised.<ref name="MM5e-p52">{{Cite book/Monster Manual 5th edition|52}}</ref> Interestingly enough, Orcus did appear to find some modicum of joy and appreciation in the misery he caused.<ref name="MM4e-p206" /><ref name="MToF-p152-153" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:128`

## Field 4: Cults, clergy, worship, temples, holy days, messengers

- Cult structure, line 206:
> "Worship of Orcus was spread across numerous isolated cults that operated independently of one another. They operated within the shadows of society, often congregating in locales linked to the dead, including graveyards and secluded tombs.<ref name="MM4e-p210">{{Cite book/Monster Manual 4th edition|210}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:206`

- Followers, line 215:
> "His worship often attracted malevolent [[human]]s, [[orc]]s, [[ogre]]s, [[giant]]s, and [[goblinoid]]s,<ref name="FCI-127-128" /><ref name="BL-p23">{{Cite book/The Bloodstone Lands|23}}</ref><ref name="LM-p18" /> along with at least one line of [[red dragon]]s .<ref name="ToB-p49">{{Cite book/The Throne of Bloodstone|49}}</ref> His cults also attracted twisted creatures with a morbid fascination for undeath. Notable among these followers were [[necromancer]]s<ref name="HOH-p87">{{Cite book/Heroes of Horror|87}}</ref> and others deliberately seeking the path to unlife via [[lichdom]] or [[vampirism]].<ref name="FCI-p73-74" /><ref name="MM4e-p259">{{Cite book/Monster Manual 4th edition|259}}</ref> Among the undead that dwelled within [[Palace of Orcus|Orcus' palace]] or otherwise joined his armies  were zombies, [[wight]]s,<ref name="MM5e-p300">{{Cite book/Monster Manual 5th edition|300}}</ref> [[shadow]]s, [[huecuva]]e, [[nightwalker]]s, [[sheet phantom]]s, and [[death knight]]s.<ref name="ToB-p46" /><ref name="MoP4e-p55">{{Cite book/Manual of the Planes 4th edition|55}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:215`

- Regions and the Cult of the Goat's Head, line 220:
> "Orcus had cults dedicated to his worship all across [[Faerûn]], including the realms of Vaasa and [[Damara]].<ref name="RoF-p91">{{Cite book/Races of Faerûn|91}}</ref><ref name="PGtF-p15">{{Cite book/Player's Guide to Faerûn|15}}</ref> In the [[Bloodstone Lands]], Orcus' worship was coordinated by the [[Cult of the Goat's Head]],<ref name="DD-p23-25">{{Cite book/Demihuman Deities|23-25}}</ref><ref name="BL-p17">{{Cite book/The Bloodstone Lands|17}}</ref> and in the [[Neverwinter Wood]], by the [[Hunt Lords]].<ref name="SKT-p101">{{Cite book/Storm King's Thunder|101}}</ref> Despite its transformation into a realm of undeath, Orcus viewed [[Thay]] under the [[Szass Tam]] as a mere petty fiefdom.<ref name="SC-p44">{{Cite adventurers league/Streams of Crimson|44}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:220`

- Temples, line 222:
> "Temples of Orcus could be found throughout the many planes of existence,<ref name="LM-p18" /> including at least one on Toril in the [[Temple of Orcus (Deepearth)|caverns of Deepearth]].<ref name="MoB-p22-26">{{Cite book/The Mines of Bloodstone|22-26}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:222`

- Shadowfell cults and the Raven Queen, line 224:
> "His influence was not limited to the Abyss and the Prime Material Plane. Many of Orcus' dark servants spread out across the [[Shadowfell]], determined to commit horrific deeds in his name.<ref name="FRCG-p69">{{Cite book/Forgotten Realms Campaign Guide|69}}</ref> In the Shadowfell, Orcus' cultists took over the dark settlements of [[Moil]],<ref name="EE-p129">{{Cite book/Exemplars of Evil|129}}</ref><ref name="BVD.DMB-p52">{{Cite book/The Book of Vile Darkness/Dungeon Master's Book|52}}</ref><ref name="MoP4e-p60">{{Cite book/Manual of the Planes 4th edition|60}}</ref> and [[Evernight]], the dark echo of [[Neverwinter]] in Faerûn.<ref name="NCS-p202">{{Cite book/Neverwinter Campaign Setting|202}}</ref> Several Shadowfell cults even banded together for a time to raise up Orcus as a new God of Death, to take the place of the [[Raven Queen]],<ref name="DR-p6">{{Cite book/Death's Reach|6}}</ref> going so far as to scour the [[Plane of Dreams]] for clues to their quest.<ref name="MoP4e-p31">{{Cite book/Manual of the Planes 4th edition|31}}</ref><ref name="MoP4e-p53">{{Cite book/Manual of the Planes 4th edition|53}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:224`

- Clergy: the deathpriests and the aspect ritual, line 146:
> "Orcus could not be harmed by non-[[item enchantment|magical]] weapons, was highly resistant to the elements,<ref name="OotA-p244-245" /> nearly impervious to [[magic]],<ref name="ToB-p75-77" /> and wholly immune to any [[magic]]al or mundane [[charm]] or [[fear]].<ref name="OotA-p244-245" /> He could appear as an aspect of himself to any of his deathpriests that performed the appropriate [[ritual]].<ref name="MM4e-p208">{{Cite book/Monster Manual 4th edition|208}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:146`

- Notable worshipers, line 231 (one of the bullet list on lines 231 to 239; none is in Waterdeep):
> "* [[Banak]], high priest of Orcus in the [[Bloodstone Lands]]<ref name="BP-p29">{{Cite book/Bloodstone Pass|29}}</ref><ref name="BL-p44">{{Cite book/The Bloodstone Lands|44}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:231`

- Holy days: the holy-day fields (lines 40, 55, 70, 85, 98) are empty. The wiki gives no omen and no messenger in the worship text.

## Field 5: Relations and origin

- Enemies and allies, line 188 (the triad with Graz'zt and Demogorgon):
> "Orcus was one third of the triad―including Graz'zt and Demogorgon―that engaged in ongoing war with one another.<ref name="CoR-p131"/><ref name="FCI-p73-74" /><ref group="note" name="Rivals">While ''[[Champions of Ruin]]'' state [[Eltab]] was among the three demon lords in constant battle with one another, nearly every other source includes Demogorgon among the trio.</ref> He viewed Graz'zt as a self-aggrandized narcissist,<ref name="SC-p44" /> and was believed to have warred with Demogorgon for hundreds of thousands of years.<ref name="FCI-63">{{Cite book/Fiendish Codex I: Hordes of the Abyss|63}}</ref> Their conflict predated the [[Days of Thunder]] if not the formation of [[Toril]] itself.<ref name="ToB-p34">{{Cite book/The Throne of Bloodstone|34}}</ref>{{Speculation}}"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:188`

- Raven Queen, line 190:
> "The Prince of the Undead developed strong enmity with the [[Raven Queen]], the goddess of death that dwelled within the [[Shadowfell]].<ref name="SGB-p8" /> Followers of the Raven Queen vehemently opposed those that venerated Orcus due to their conflicting views on undeath.<ref name="DrM397.FH-p4">{{Cite dragon/397/Faith & Heresy|4}}</ref> At one point, Orcus and his minions carried out a series of schemes in an ongoing effort to strip her of her divine powers.<ref name="SGB-p8">{{Cite book/The Shadowfell: Gloomwrought and Beyond|8}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:190`

- Kiaransalee and the Cult of the Goat's Head, line 192:
> "After Kiaransalee took control of Orcus's ream of Thanatos in the mid&ndash;14{{th}} century DR, the drow goddess became obsessed with destroying all traces of Orcus.<ref name="FP-p113">{{Cite book/Faiths and Pantheons|113}}</ref> Her followers accordingly wiped out his [[Cult of the Goat's Head]] in [[Vaasa]].<ref name="DD-p25">{{Cite book/Demihuman Deities|25}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:192`

- Yeenoghu and Iggwilv, line 194:
> "For a brief time, he forged a tenuous alliance with [[Yeenoghu]] the Lord of Savagery,<ref name="ToB-p64">{{Cite book/The Throne of Bloodstone|64}}</ref> and [[Iggwilv]], the mortal daughter of [[Baba Yaga]]. Orcus and Iggwilv became involved in an elaborate scheme to overthrow Demogorgon as Prince of Demons.<ref name="DrM359.MWV-p62" /><ref name="DuM150-p62">{{Cite dungeon/150/Prince of Demons|62}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:194`

- Vecna and Acererak, line 196:
> "Orcus was a patron of sorts to the [[Oerth]]ian mage [[Vecna]], and was said to have offered him the ritual by which he became the first lich.<ref name="DMG5e-p224">{{Cite book/Dungeon Master's Guide 5th edition|224}}</ref> He was even pleased with the work of Vecna's one-time follower [[Acererak]], who traveled the planes in search of new and horrific ways to slay innocents.<ref name="SC-p44">{{Cite adventurers league/Streams of Crimson|44}}</ref> Acererak even turned to the worship of Orcus for a time.<ref name="ToH4e-p4-5">{{Cite book/Tomb of Horrors (4th edition)|4-5}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:196`

**Origin and rise, two accounts that the wiki gives as alternatives.** Line 243 (the mortal account, citing FCI-127-128):
> "Like many of the most powerful demon lords who struggled for power in the Abyss, Orcus started his existence as a mortal on the [[Prime Material Plane|Prime Plane]]. He was apparently a wicked spellcaster of some sort, most probably a priest to some dark deity. After his death, his soul journeyed to [[Pazunia]]<ref name="DrM359.MWV-p62" /> in the Abyss and Orcus began his [[afterlife]] as a lowly [[larva]].Orcus proceeded to climb through the demonic ranks over the next several thousand years, going from [[larva]] to [[mane]], from mane to [[dretch]], from dretch to [[rutterkin]], from rutterkin to [[vrock]], from vrock to [[glabrezu]], from glabrezu to [[nalfeshnee]], and eventually in the form of a balor.<ref name="FCI-127-128">{{Cite book/Fiendish Codex I: Hordes of the Abyss|127-128}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:243`

Line 245 (the primordial account, citing Demonomicon p. 8):
> "There existed for Orcus a different origin, stating he was one of the primordials present during the [[Dawn War]] and was older than the Abyss itself. Along with fellow primordials Baphomet and Demogorgon, Orcus was said to have brought down the then-current [[Prince of Demons]], [[Obox-ob]]. Obox-Ob had attained the shard of pure evil ventured out to the [[Astral Plane]], to gain ultimate power over the entire multiverse. While in the midst of attaining their demonic forms, the trio cast the Prince of Demons down into the point form which the Abyss first formed. They then rode along the [[Blood Rift]] and ascended to the ranks of full-fledged demon lords.<ref name="Demonomicon-p8">{{Cite book/Demonomicon|8}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:245`

Line 247 (the transition to Prince of the Undead):
> "However it began, Orcus became the Prince of the Undead and took dominion over Thanatos, the Belly of Death.<ref name="FCI-127-128" /> Ever hungry for more power, Orcus sought to dethrone Demogorgon as the 'Prince of Demons', a title also coveted by Graz'zt.<ref name="DrM359.MWV-p62" /><ref name="DuM150-p62" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:247`

The later history, line 261 (the full paragraph, including the Kiaransalee account):
> "By this time in his existence, Orcus achieved some form of actual divinity.<ref name="DrM359.MWV-p62" /> He also however had grown indolent and no longer concerned himself with the eternal conflict between himself, Demogorgon and Graz'zt.<ref name="FCI-p73-74" /><ref name="DrM417.STW-p12-14" /> His realm became a hushed desolation of idle undeath, considered a humorous oddity among [[planewalker]]s of the multiverse. Orcus' sloth and carelessness made him vulnerable within his Abyssal palace, and he was slain by the [[drow]] [[demi-goddess]] [[Kiaransalee]].<ref name="Dead Gods-p6-9">{{Cite book/Dead Gods|6-9}}</ref><ref name="PGtF-p87">{{Cite book/Player's Guide to Faerûn|187}}</ref><ref name="CSQ-p5">{{Cite book/City of the Spider Queen|5}}</ref> She then took over rulership of Orcus' realm of Thanatos in the Abyss and reshaped it in her own image. Despite its apparent recent destruction,<ref name="DoF-p9" /><ref name="GHotR-144" /> Kiaransalee decreed that the ''Wand of Orcus'' be hidden away in [[Pandemonium]] and Orcus' name be erased from all recorded existence.<ref name="DD-p23-25" /><ref name="Dead Gods-p6-9" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:261`

Line 264 (rebirth as Tenebrous):
> "Despite the drow demi-goddess' efforts, Orcus was restored as a burst of [[negative energy]] named Tenebrous<ref name="ToM-p48" /><ref name="DD-p23-25" /> and struck out to reclaim power in opportune moments.<ref name="FCI-p73-74" /> Upon his return, Tenebrous discovered the [[Last Word]], one of the [[words of power]].<ref name="FCI-127-128" /> This utterance so powerful that it could destroy deities, including the being that uttered it, unless they were themselves a true deity. Tenebrous sought out the lost ''Wand of Orcus'' to attain this divinity and restore himself to power.<ref name="Dead Gods-p6-9" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/orcus/wiki.txt:264`

## Field 6: Campaign and published-adventure mentions

- Campaign: none (`campaign-hits.txt` is empty; the campaign grep found no Orcus line).
- Published adventure: none (`adventure-hits.txt` is empty; the JSON grep found no match for Orcus, Wand of Orcus, Prince of Undeath, Tenebrous or Prince of the Undead). The WDMM "Tenebrous" line 58833 is a book title (see Cross-references).
- Wiki appearances, line 294 (adventure titles, none placed in Waterdeep): "The Mines of Bloodstone • The Throne of Bloodstone • The Great Modron March • Dead Gods • Prince of Undeath • Out of the Abyss".

## Field 7: Conflicts and not found

- **Conflict (origin):** line 243 (mortal origin, citing FCI-127-128) and line 245 (primordial origin, citing Demonomicon p. 8). The wiki presents them as alternatives ("There existed for Orcus a different origin").
- **Conflict (primordial status):** line 113 says "purported primordial" (citing MM4e-p52). The Rise section (line 243) gives a mortal origin.
- **Conflict (rivalry):** the note on line 188 says *Champions of Ruin* names Eltab, not Demogorgon, among the three demon lords. The wiki says "nearly every other source includes Demogorgon among the trio."
- **Edition difference (challenge):** `challenge5e=26` (line 112) and `challenge3e` 28 (line 71).
- **Not found:** holy days, omens, messengers, a Waterdeep cult or temple, any Waterdeep mention, any campaign NPC, faction or quest that uses him.

---

# 4. Demogorgon

Wiki page: `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/demogorgon/wiki.txt`. Wiki keys (book as the wiki names it): MM1e-pp16-17 = Monster Manual 1st edition (line 100). MToF-pp144-145 = Mordenkainen's Tome of Foes, 5e (line 42). OotA-pp236-237 = Out of the Abyss (line 42). MM24e-pp42-50 = Monster Manual 2, 4th edition (line 57). DN4e-pp7-8 = Demonomicon, 4e (line 191). FCI-p63 = Fiendish Codex I: Hordes of the Abyss, 3e (line 73). BoVD-p125 = Book of Vile Darkness (line 71). Dr357-PoD = Dragon 357, Demonomicon of Iggwilv: Demogorgon: Prince of Demons (line 113). PHB5e-p109 = Player's Handbook 5th edition (line 171). VGM5e-p219 = Volo's Guide to Monsters (line 171). MM-p88 = Monster Mythology (line 167). BGII.ToB = Baldur's Gate II: Throne of Bhaal, video game (line 14). Archmage-p357 = Archmage, 2015 hardcover (line 212).

## Answers

**(1) Waterdeep cult, shrine or temple.** None. The wiki has no Waterdeep mention (grep returned no match). The "Lost Temple of Demogorgon" in the Further Reading list (line 274) is a Dungeon issue title that places no temple in any city. The WDH table has no Demogorgon row.

**(2) Campaign NPC, faction or quest.** None.

**(3) Wiki lines that mention Waterdeep.** None.

## Field 1: Identity

- Titles, line 13:
> "| title               = Prince of Demons<ref name="MM1e-pp16-17">{{Cite book/Monster Manual 1st edition|16-17}}</ref><br />The Deep Father<ref name="OotA5e-pp45,47-48" /><br />The Sibilant Beast<ref name="MToF-pp144-145">{{Cite book/Mordenkainen's Tome of Foes|144-145}}</ref><br />Master of the Spiraling Depths<ref name="MToF-pp144-145" /><br />  Master of the Mysterious<ref name="BoVD-p67">{{Cite book/Book of Vile Darkness|67}}</ref><br />King of the Deviants<ref name="BoVD-p67"/><br />Tanar'ri Prince and Lord of All that Swims in Darkness<ref name="TGP-p105">{{Cite book/The Glass Prison|105|7}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/demogorgon/wiki.txt:13`

- Aspects, line 14:
> "| aspects             = Ahmon-Ibor<ref name="FCI-p63">{{Cite book/Fiendish Codex I: Hordes of the Abyss|63}}</ref><br /> Siosivash<ref name="FCI-p63" /><br />Leemooggoogoon<ref name="OotA5e-pp45,47-48">{{Cite book/Out of the Abyss|45,47-48}}</ref><br /> The Imprisoned One<ref name="BGII.ToB">{{Cite game/Baldur's Gate II: Throne of Bhaal}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/demogorgon/wiki.txt:14`

- Introduction, line 113:
> "'''Demogorgon''' ({{Pronounce|DEE|mo|gor|gun|refs=<ref name="Dr93-Apg-p26">{{Cite dragon/93/Ay pronunseeAYshun gyd|26}}</ref>|audio=Demogorgon.ogg}}) referred to as the '''Imprisoned One''' by some followers of [[Helm]],<ref name="BGII.ToB" /> was the [[demon lord]] and [[lesser deity]] of domination and the draining of energy,<ref name="MM-p88" /> an embodiment of madness and destruction that sought to drag all down into the infinite depths of the [[Abyss]].<ref name="MToF-pp144-145" /> He was known by many names, called '''Siosivash''' by the [[yuan-ti]],<ref name="FCI-p63" /> '''Leemooggoogoon the Deep Father''' by the [[kuo-toa]],<ref name="OotA5e-pp45,47-48" /> and '''Ahmon-Ibor the Sibilant Beast''' by the [[troglodyte]]s.<ref name="FCI-p63" /> The first [[tanar'ri]], formed from mortals' ancient fears,<ref name="Dr357-PoD-p21">{{Cite dragon/357/Demonomicon of Iggwilv: Demogorgon: Prince of Demons|21}}</ref> even his chosen race, the [[ixitxachitl]], dared not speak his name aloud;<ref name="FCI-p63"/> it alone could inspire a primal terror.<ref name="FCI-p62">{{Cite book/Fiendish Codex I: Hordes of the Abyss|62}}</ref> Inspiring fear in even other demon lords, his self-proclaimed title of '''Prince of Demons''' was won by virtue of power and influence; many demons challenged it, but none could defeat Demogorgon and claim it.<ref name="MM24e-pp42-50" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/demogorgon/wiki.txt:113`

- Realm and plane: `homeplane5e` (line 31) "The [[Abyss]]"; `realm5e` (line 32) "[[Gaping Maw]]". The 3e home (line 61) is "The [[Abyss]]/[[Layers of the Abyss#Layer 88: Gaping Maw|88{{th}} layer]]".

- Alignment, line 29: `| alignment5e         = [[Chaotic evil]]`.

- Domains, 3e, line 66:
> "| domains3e           = [[Chaos domain|Chaos]], [[Demonic domain|Demonic]], [[Corruption domain|Corruption]], [[Evil domain|Evil]]"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/demogorgon/wiki.txt:66`

- Symbol, 3e, line 60: `| symbol3e            = Forked tail`.

- Challenge rating: `| challenge5e         = 26` (line 40) and `| challenge3e         = 23<ref group="note">In the [[Book of Vile Darkness (sourcebook)|Book of Vile Darkness]] his challenge rating is given as 30.</ref>` (line 71). The 5e value has no field citation. The 5e refs (line 42) are MToF-pp144-145 and OotA-pp236-237.

- Power: `power5e` (line 28) "[[Demon lord]]"; `power4e` (line 43) "[[Primordial]]"; `power2e` (line 74) "[[Lesser deity]]"; `power3e` (line 58) "[[Demon lord]]".

- Worshipers, 2e, line 83: `| worshipers2e        = [[Ixitxachitl]], [[kraken]]s`.

## Field 2: What he wants from a warlock, and what a pact costs

> "Demogorgon was sufficiently powerful to offer patronage pacts with [[warlock]]s,<ref name="PHB5e-p109">{{Cite book/Player's Handbook 5th edition|109}}</ref> who usually kept [[quasit]]s as familiars.<ref name="VGM5e-p219">{{Cite book/Volo's Guide to Monsters|219}}</ref> His most devout followers were granted magic boons, such as an aspect of his dual minds that conferred resistance to mind-affecting effects. Their signature spells mimicked Demogorgon's own abilities, such as ''[[charm person]]'', ''[[enlarge or reduce person|enlarge/reduce]]'', and ''[[vampiric touch]]''.<ref name="MToF-p30">{{Cite book/Mordenkainen's Tome of Foes|30}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/demogorgon/wiki.txt:171`

The wiki gives no pact cost for Demogorgon (see Field 7).

## Field 3: Portfolio and sphere

> "| portfolio3e         = Demonkind<ref name="FCI-p155">{{Cite book/Fiendish Codex I: Hordes of the Abyss|155}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/demogorgon/wiki.txt:65`

The 3e portfolio is Demonkind. The domains (line 66) are quoted under Field 1. The area of concern is the line 113 phrase "domination and the draining of energy" (quoted under Field 1).

## Field 4: Cults, clergy, worship, temples, holy days, messengers

- Cult size, line 167:
> "Demogorgon's cult was relatively small compared to "true" deities, but much larger than those of most fiends. He was worshiped by the intelligent manta ray race known as [[ixitxachitl]]s, who drew power from the Abyss itself in order to become more powerful spellcasters. In turn, vital energy drained by [[vampiric ixitxachitl]]s was transferred directly to Demogorgon via an unknown Abyssal mechanism.<ref name="MM-p88" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/demogorgon/wiki.txt:167`

- Other worshipers, temples and domains, line 169:
> "Demogorgon's other worshipers included [[troglodyte]]s, [[kuo-toa]], and other [[humanoid]]s, particularly evil [[human]]s. His cult prospered in times of chaos and caused great destruction wherever it was found. Temples to Demogorgon were split in half, with one side representing Aameul and the other representing Hethradiah.<ref name="MM24e-pp42-50" /> Demogorgon's domains were [[Chaos domain|Chaos]], [[Corruption domain|Corruption]], [[Demonic domain|Demonic]], and [[Evil domain|Evil]].<ref name="FCI-p63" /> His symbol was that of a forked tail, often wrapped around a skull or sword.<ref name="BoVD-pp125-127" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/demogorgon/wiki.txt:169`

- Warlock and boon text, quoted under Field 2 (line 171).

- Aspects, line 174:
> "Mortals could not summon Demogorgon himself, but the most pious could use sacrifice to summon a temporary [[aspect]] of Demogorgon. The aspect was smaller and not as powerful as Demogorgon. An aspect of Demogorgon was always unbalanced, taking after one head more than the other.<ref name="MM24e-pp42-50" /><ref name="FCII.FA-pp1-4">{{Cite web enhancement/Fiendish Aspects II|1-4}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/demogorgon/wiki.txt:174`

- Kuo-toa cult, line 220:
> "In the late 15{{th}} century [[DR]], as a result of a vision of the demon lord in the [[Darklake]], a faction of the kuo-toa of [[Sloobludop]] started a cult of Demogorgon.<ref name="OotA5e-pp45,47-48" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/demogorgon/wiki.txt:220`

- Worshipper's invocation, line 164 (the quotation of Qill, cultist, BoVD p. 67):
> "The dual-lived, dual-willed prince of the Abyss, master of the mysterious and king of the deviants, Demogorgon, you are my lord!"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/demogorgon/wiki.txt:164`

- Temples: the body's only temple sentence is line 169 (quoted). Line 274 is a Further Reading title (quoted under Field 6).
- Holy days: the holy-day fields (lines 39, 55, 70, 85, 98) are empty. The wiki gives no omen and no messenger.

## Field 5: Relations and origin

- Orcus and Graz'zt, line 178:
> "The hatred between [[Orcus]] and Demogorgon was legendary.<ref name="MM24e-pp42-50" /><ref name="MM1e-pp16-17" /> He was also a dedicated foe of [[Graz'zt]]<ref name="MM24e-pp42-50" /> and had unsuccessfully attempted to conquer [[Fraz-Urb'luu]]'s realm.<ref name="Dr357-pp20-32" /> He hated [[Sekolah]] and encouraged his followers to kill [[sahuagin]].<ref name="MM-p88" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/demogorgon/wiki.txt:178`

- Allies, line 180:
> "Demogorgon was allied with the [[obyrith]] lord [[Dagon]],<ref name="FCI-p61" /> who often advised the heads of Aameul and Hethradiah separately. Dagon provided intellect, while Demogorgon provided brute strength.<ref name="MM24e-pp42-50" /> He was also frequently visited by [[Zuggtmoy]], who exchanged fungi at Gaping Maw and engaged with Demogorgon in several discussions. He was also allied with [[Ilsidahur]], lord of [[bar-lgura]]s.<ref name="Dr357-pp20-32" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/demogorgon/wiki.txt:180`

- Romance and kin, line 182:
> "Demogorgon's romantic interests included the [[succubus]] [[Shami-Amourae]] and the Succubus Queen [[Malcanthet]], both of whom had manipulated him for their own benefits. Shami-Amourae, however, was imprisoned in the [[Layers of the Abyss#Layer 73: The Wells of Darkness|Wells of Darkness]] for her manipulations.<ref name="Du148">{{Cite dungeon/148/Wells of Darkness}}</ref><ref name="Dr357-pp20-32" /> He was the brother of another demon lord called [[Mandrillagon]].<ref name="DoD">{{Cite book/Dance of Demons}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/demogorgon/wiki.txt:182`

- Balor servant, line 184:
> "The [[balor]] [[Belaphoss]] considered himself to be the most powerful of Demogorgon's servants.<ref name="SCAG-p139">{{Cite book/Sword Coast Adventurer's Guide|139}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/demogorgon/wiki.txt:184`

**Origin, two conflicting accounts.** Line 189 (first tanar'ri, citing Dragon 357). The line opens "There were conflicting legends about the origin of Demogorgon."
> "There were conflicting legends about the origin of Demogorgon. One account claimed that he was the first of the [[tanar'ri]], who originated out of the consolidated fear of mortal souls, shortly after the [[obyrith]] [[Obox-ob]] was defeated by the [[Queen of Chaos]]. Cast aside as a deformity with his boneless arms and twin heads, Demogorgon lay hidden while the Queen of Chaos used [[sibriex]]es to better shape other primal mortal emotions into more refined tanar'ri.<ref name="Dr357-pp20-32" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/demogorgon/wiki.txt:189`

Line 191 (primordial account, citing DN4e-pp7-8):
> "Another legend claimed that Demogorgon was originally a [[primordial]] and the first of his kind to set foot in the Abyss shortly after the formation of the plane, followed closely by Dagon, who challenged him for control of the plane. As he and Demogorgon fought, Obox-ob seized the opportunity to become the first Prince of Demons. A temporary alliance between Demogorgon, Orcus, and [[Baphomet]] was formed to defeat Obox-ob.<ref name="DN4e-pp7-8" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/demogorgon/wiki.txt:191`

- Ascension, line 197 (the whole paragraph):
> "Following the defeat of the Queen of Chaos at the hands of the tanar'ri, the leading demon lords Graz'zt and Orcus then competed for the title of Prince of Demons. At that moment, Demogorgon, who had grown stronger during his exile, launched a massive assault throughout the plane to crush his rivals' forces. After he slew a dozen demon lords, draining their life forces with his tentacles, even Graz'zt and Orcus were forced to kneel. Thus, Demogorgon asserted his position as Prince of Demons.<ref name="DN4e-p9">{{Cite book/Demonomicon|9}}</ref><ref name="Dr357-pp20-32">{{Cite dragon/357/Demonomicon of Iggwilv: Demogorgon: Prince of Demons|20-32}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/demogorgon/wiki.txt:197`

- Recorded history, line 214 (1486 DR):
> "On [[Nightal 15]], [[1486 DR]],<ref name="Archmage-p356">{{Cite book/Archmage/Hardcover (2015)|356}}</ref> [[Archmage of Menzoberranzan|Archmage]] [[Gromph Baenre]] weakened the barriers of ''[[faerzress]]'', inadvertently "summoning" Demogorgon and allowing him to pass from the Abyss to the [[Prime Material Plane]]. He arrived at the tower of [[Sorcere]] in [[Menzoberranzan]] and cut a swath of destruction as he exited the cavern.<ref name="Archmage-p357">{{Cite book/Archmage/Hardcover (2015)|357}}</ref> Gromph was able to weaken the ''faerzress'' because of his study of [[psionics]] and the psychic conveyance of a plan devised by the goddess [[Lolth]].<ref name="Archmage-p82">{{Cite book/Archmage/Hardcover (2015)|82}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/demogorgon/wiki.txt:214`

- Realm, line 152 (the divine realm):
> "Demogorgon lived on the [[Layers of the Abyss#Layer 88: Gaping Maw|88{{th}} layer]] of the [[Abyss]], known as the [[Gaping Maw]]. This was a layer consisting of a great sea of briny water broken by tall, sharp, ugly, rocky promontories. Demogorgon's palace, called [[Abysm]], consisted of two twin towers roughly shaped like tightly coiled serpents, crowned at the top with skull-shaped minarets. The two towers were linked by a bridge near the top. Most of the fortress lay underwater beneath the towers.<ref name="BoVD-pp125-127" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/demogorgon/wiki.txt:152`

## Field 6: Campaign and published-adventure mentions

- Campaign: none (`campaign-hits.txt` is empty; the campaign grep found no Demogorgon line).
- Published adventure: none (`adventure-hits.txt` is empty; the JSON grep found no match for Demogorgon, Prince of Demons, Imprisoned One, Aameul or Hethradiah).
- Further Reading, line 274 (a Dungeon issue title, not a Waterdeep place):
> "* {{Cite dungeon/120/Lost Temple of Demogorgon}}"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/demogorgon/wiki.txt:274`

## Field 7: Conflicts and not found

- **Conflict (origin):** line 189 (first tanar'ri, citing Dragon 357) and line 191 (originally a primordial, citing Demonomicon 4e). Line 189 itself opens "There were conflicting legends about the origin of Demogorgon."
- **Conflict (rank):** line 74 (`power2e` "Lesser deity") against line 58 (`power3e` "Demon lord") and line 28 (`power5e` "Demon lord"). Line 43 gives 4e as "Primordial".
- **Conflict (challenge):** line 71 gives the 3e challenge as 23, with a note that the Book of Vile Darkness gives 30.
- **Not found:** pact costs, holy days, omens, messengers, any Waterdeep cult or temple, any campaign NPC, faction or quest.

---

# 5. Graz'zt

Wiki page: `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/graz-zt/wiki.txt`. Wiki keys (book as the wiki names it): OotA5e-p240-241 = Out of the Abyss, 5e (line 39). MTF5e-p148-149 = Mordenkainen's Tome of Foes, 5e (line 39). FC13e = Fiendish Codex I: Hordes of the Abyss, 3e (line 70). BoVD = Book of Vile Darkness (lines 13, 70). D360 = Dragon 360, Demonomicon of Iggwilv: Graz'zt, the Dark Prince (line 70). MotP4e-p131 = Manual of the Planes 4th edition, pp. 130-131 (line 54). MToF-28 = Mordenkainen's Tome of Foes (line 186). HotA-p65 = Fiendish Codex I: Hordes of the Abyss, p. 65 (line 177). HotA-p118-121 = Fiendish Codex I, pp. 118-121 (line 155). FDaD-4 = For Duty & Deity (line 175). D355-p71 = Dragon 355, Volo's Guide: Demon Cults of the Realms (line 175). D414 = Dragon 414, History Check: The Iggwilv-Graz'zt Affair (line 180). GHotR-81 = The Grand History of the Realms (line 157). MM5 = Monster Manual 5th edition, p. 52 (line 109). VGtM-199 = Volo's Guide to Monsters (line 171).

## Answers

**(1) Waterdeep cult, shrine or temple.** None. The wiki has no Waterdeep mention. Its `church` and `temples` fields (lines 106–107) are empty. The WDH table has no Graz'zt row. The Waukeen heresy at line 175 is placed in the church of Waukeen, not in a city.

**(2) Campaign NPC, faction or quest.** None.

**(3) Wiki lines that mention Waterdeep.** None.

## Field 1: Identity

- Titles, line 13:
> "| title               = The Dark Prince<ref name="FC13e-p65-66" /><br />The Dark Man<ref name="BoVD-pp68">{{Cite book/Book of Vile Darkness|68}}</ref><br />The Shadow King<ref name="BoVD-pp68"/><br />The Prince of Pleasure<ref name="OotA5e-p240-241">{{Cite book/Out of the Abyss|240-241}}</ref>The Lord of Forbidden Pleasures<ref name="MTF5e-p30">{{Cite book/Mordenkainen's Tome of Foes|30}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/graz-zt/wiki.txt:13`

- Introduction, line 109:
> "'''Graz'zt''' was the [[demon lord|demon prince]] of pleasure, decadence, and unlimited self-indulgence, as well as the patron of corrupt authorities and tyrants who would rule by force. He ruled the 45{{th}}, 46{{th}}, and 47{{th}} layers of the [[Abyss]], known as [[Azzagrat]] or the Triple Realm.<ref name="FC13e-p65-66" /><ref name="MToF-28" /> The appearance of '''the Dark Prince''' belied the true depths of his wickedness,<ref name="MM5">{{Cite book/Monster Manual 5th edition|52}}</ref> his existence a warning that not all that was beautiful was also good.<ref name="MTF5e-p148-149" /> All things were but playthings in the eyes of the '''Prince of Pleasure'''; he simply hadn't claimed them yet.<ref name="MToF-28" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/graz-zt/wiki.txt:109`

- Realm and plane: `homeplane3e` (line 58) "The [[Abyss]]"; `realm3e` (line 59) "[[Azzagrat]]". The 5e home and realm fields (lines 28–29) are empty.

- Alignment: `alignment5e` (line 26) and `alignment3e` (line 56) are both "[[Chaotic evil]]".

- Domains, 3e, line 63:
> "| domains3e           = [[Chaos domain|Chaos]], [[Demonic domain|Demonic]], [[Evil domain|Evil]], [[Temptation domain|Temptation]]"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/graz-zt/wiki.txt:63`

- Symbol, 3e, line 57: `| symbol3e            = A black, six-fingered hand`.
- Favored weapon, 3e, line 66: `| favored weapon3e    = [[Bastard sword]]`.
- Portfolio, 3e, line 62: `| portfolio3e         = Tyrants, despot, guile, debauchery`.

- Challenge rating: `| challenge5e         = 24` (line 37), with refs5e (line 39) OotA5e-p240-241 and MTF5e-p148-149. The 3e challenge (line 68) is 32, with a note that *Fiendish Codex I* gives 22 and the *Book of Vile Darkness* gives 24.

- Power: `power5e` (line 25) "[[Demon lord]]"; `power4e` (line 40) "[[Demon lord]]"; `power3e` (line 55) "[[Demon lord]]".

- Worshipers, 3e (line 64) and 5e (line 34): empty. The worship text is at line 153 (quoted under Field 4).

## Field 2: What he wants from a warlock, and what a pact costs

The cost of a bargain is in the wiki's line 125:
> "Unlike his kin, he paid a great deal of attention to the [[Prime Material plane]] through his spies and he was known to have interacted with mortals quite often, trading favors, aid, or information with them only to then demand a service later on.<ref name=":0" /><ref>{{Cite book/Fiendish Codex I: Hordes of the Abyss|66}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/graz-zt/wiki.txt:125`

His appetites and the pact-making of his followers, line 129 (cites HotA-p65, BoVD, MToF, MM5, D360):
> "As the Prince of Pleasure, the only sin as far as he was concerned was moderation. He was fond of procreating with humanoids who had made pacts with fiends and was one of the most notorious sources of [[cambion]]s within the [[Lower Planes]]. He enjoyed contrasts and mismatches that others considered grotesque, while he despised kindness or restrictions. Due to his insatiable appetites, the Dark Prince never went anywhere without a retinue of female monsters such as [[lamia]]s, [[Succubus|succubi]], or [[marilith]]s.<ref name="HotA-p65" /><ref name="BoVD-p130" /><ref name="MToF-p148" /><ref name="MM5" /><ref name="D360-p10-11" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/graz-zt/wiki.txt:129`

The wiki has no Fiend-patron pact text for Graz'zt. The word "warlock" does not appear in the file.

## Field 3: Portfolio and sphere

The 3e portfolio (line 62) is quoted under Field 1. The wiki's account of his goal, line 131:
> "In contrast to his hedonism, he kept his mind clear of distractions so as to focus on claiming more land and minions, all while defeating his enemies one at a time. His endless schemes led to his ultimate goal, which was the complete subjugation and unification of the Abyss and from there the whole of the Lower Planes in an attempt to then command a terrible army of [[fiend|fiends]] to raze all other planes within the multiverse to the ground.<ref name="HotA-p65" /><ref name="BoVD-p130">{{Cite book/Book of Vile Darkness|130}}</ref><ref name="MToF-p148">{{Cite book/Mordenkainen's Tome of Foes|148}}</ref><ref name="MM5" /><ref name="D360-p10-11" />"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/graz-zt/wiki.txt:131`

## Field 4: Cults, clergy, worship, temples, holy days, messengers

- Worship and the Chosen, line 153 (cites BoVD-pp130-132 and FC13e-p65-66):
> "Although he had not yet achieved divine status, Graz'zt was worshiped on the [[Material Plane]] by many monstrous races, most notably the [[lamia]]s. Many of his high priests, known as the Chosen, were female, and the rituals they performed were violent and involved themes of darkness and betrayal.<ref name="BoVD-pp130-132" /><ref name="FC13e-p65-66"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/graz-zt/wiki.txt:153`

- Cultist's invocation, line 151 (the text before the pipe is the quotation; after it, the speaker, Besmal, human cultist, BoVD pp. 68):
> "The dark man, the shadow king, the ebony skinned master of all things that revel in the night, oh master Graz'zt, spare me your wrath and grant me your favor!|[[Besmal]], human cultist of Graz'zt.<ref name="BoVD-pp68"/>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/graz-zt/wiki.txt:151`

- The Waukeen heresy, line 175 (cites FDaD-4 and D355-p71; the heresy sits in the church of Waukeen, not in a city):
> "Through his own schemings and mischief, Graz'zt became the chief enemy of [[Waukeen]], a goddess of wealth and merchantry. During the [[Time of Troubles]], the deity bargained for safe passage across Zelatar with information regarding a secret horde of treasure. Graz'zt readily accepted the offer, but betrayed Waukeen as soon as she arrived in the Abyss. Imprisoned in the Argent Palace, the goddess was forced to witness profane celebrations held in her honor.<ref name="FDaD-4">{{Cite book/For Duty & Deity|4}}</ref><ref name="D360-p12-13" /> A sinister group known as the [[League of the Six-Fingered Gentlemen]] (sometimes the League of Six Rings) wormed its way into the hierarchy of the [[church of Waukeen]] during the time that Graz'zt had imprisoned the goddess in the Abyss. Once there, they were not rooted out, and busily spread the Harlot's Coin Heresy among Waukeen's faithful. This heretical schism of Waukeen's faith taught that Waukeen had been gradually selling off pieces of her divinity and virtue to Graz'zt in order to finance her church and it was for failing to pay her debts that the demon lord imprisoned her. These heretics claimed that Waukeen became free because she finally paid her debt to the demon, resulting in Graz'zt owning the majority of Waukeen's godhood. The heretics thus believed that all who worshiped Waukeen were really worshiping Graz'zt instead, and they're just fine with that.<ref name="D355-p71">{{Cite dragon/355/Volo's Guide: Demon Cults of the Realms|71}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/graz-zt/wiki.txt:175`

- Vasharans, line 162 (the wiki's own ellipsis is inside the quote, as printed):
> "Some sources claimed that Graz'zt was the creator of the Vasharans, a breed of vilely evil [[human]]s. Deemed cruel and soulless by the gods who created him, the Vasharans' ancestor was destroyed... but Graz'zt breathed new life into the corpse, long before he attained his present status. It was a terrifying legacy, for the Vasharans were obsessed with deicide, and destroying all gods became the reason for their existence.<ref name="BoVD-pp12">{{Cite book/Book of Vile Darkness|12}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/graz-zt/wiki.txt:162`

- Temples, shrines and holy days: the `church` and `temples` fields (lines 106–107) are empty. The holy-day fields (lines 36, 52, 67, 82, 95) are empty. The wiki gives no omen and no messenger.

## Field 5: Relations and origin

- Enemies, line 177 (Baphomet, Yeenoghu, Adimarchus):
> "Graz'zt warred with many other lords of the Abyss as well, including [[Baphomet]] and [[Yeenoghu]]. Thanks to the efforts of his son Athux, he overthrew the demon prince [[Adimarchus]], who ruled [[Layers of the Abyss#Layer 507: Occipitus|Occipitus]], the 507{{th}} layer of the Abyss.<ref name="HotA-p65">{{Cite book/Fiendish Codex I: Hordes of the Abyss|65}}</ref><ref name="DN4e-p58">{{Cite book/Demonomicon|58}}</ref><ref name="DunM116-p61-62">{{Cite dungeon/116/Asylum|61-62}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/graz-zt/wiki.txt:177`

- Iggwilv, line 180 (the raw line, in full):
> "One of Graz'zt's most confusing enemies was the witch queen [[Iggwilv|Iggwilv (a.k.a. Tasha)]]. The two had been both lovers and bitter enemies over many years.<ref name="D414">{{Cite dragon/414/History Check: The Iggwilv-Graz'zt Affair}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/graz-zt/wiki.txt:180`

- Enemies, line 182 (Malcanthet, Gwynharwyf, Kostchtchie):
> "Two of Graz'zt's other greatest enemies were [[Malcanthet]], Queen of the [[Succubi]], and [[Gwynharwyf]], champion of the [[Celestial eladrin|eladrin]].<ref name="D149-ST-EoME-p42">{{Cite dungeon/149/Enemies of My Enemy|42}}</ref> His conflict with the former ended up involving [[Kostchtchie]], the Prince of Wrath, who swore revenge against Graz'zt for humiliating him, although Graz'zt himself did not consider the upstart demon lord as much of a threat.<ref name="D345-DoI-K-PoW-pp25">{{Cite dragon/345/Demonomicon of Iggwilv: Kostchtchie: Prince of Wrath|25}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/graz-zt/wiki.txt:182`

- Servants and Raxivort, line 171:
> "The god [[Raxivort]] was once a servant of the Dark Prince.<ref name="HotA-p118-121" /><ref name="D360-p12-13" /> He stole powerful artifacts from Graz'zt and escaped to the howling chasms of [[Pandemonium]], where he became the divine patron of rodents and bats. Raxivort even has his own chosen race, a goblinoid horde known as the [[xvart]]s.<ref name="VGtM-199">{{Cite book/Volo's Guide to Monsters|199}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/graz-zt/wiki.txt:171`

- Sons, line 157 (cites GHotR-81):
> "In the {{YearlinkName|-666}}, Graz'zt and [[Ayanna Orgolath]] had twin half-fiendish sons, named [[Ulthas Orgolath|Ulthas]] and [[Ulthar Orgolath|Ulthar]]. They would overthrow the [[lich]]-king of [[Narfell]], [[Belevan Crell|Belevan the Unliving]], and give rise to the [[Orgolath Dynasty]].<ref name="GHotR-81">{{Cite book/The Grand History of the Realms|81}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/graz-zt/wiki.txt:157`

**Origin, several competing theories.** Line 186 (the first theory, an archdevil who served Asmodeus; the wiki's own lead describes "several competing, often contradictory theories"):
> "There were several competing, often contradictory theories as to Graz'zt's origin, some of which claimed that he was not a native to the Abyss, but was once an [[archdevil]] who served [[Asmodeus]]. In one of these theories, Graz'zt was chosen to lead an invasion of the Abyss as part of the [[Blood War]]&mdash;and conquered three layers of the Abyss&mdash;but became corrupted by the chaotic forces he had been sent to destroy and renounced his allegiance to the devils.<ref name="MotP4e-p131" /> Another theory claimed that Graz'zt became disillusioned with his place in [[Baator]] when he realized that the hierarchy of Hell ultimately benefited only one creature—Asmodeus—and felt that pledging his allegiance to the Abyss was the only way to place himself beyond Asmodeus's clutches.<ref name="MToF-28">{{Cite book/Mordenkainen's Tome of Foes|28}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/graz-zt/wiki.txt:186`

Line 188 (the third theory, a child of Pale Night, citing Dragon 360):
> "Yet another theory suggested that Graz'zt was one of several demonic children of [[Pale Night]], sired after the fall of the [[obyrith]]s; this would make him the brother of several other demons, including [[Lupercio]], [[Vucarik]], [[Rhyxali]], and [[Zivorgian]]. Those who subscribed to this theory believed that Pale Night must have drawn some great evil entity to herself to father her children; suggestions for what this entity could have been included an evil god such as [[Set]], a [[baernoloth]], the patriarch of a race of immortal warriors from another reality, an Outer God of Crawling Chaos, and even a sentient portion of the Abyss itself. Some maintained that Asmodeus was drawn from the Nine Hells to mate with Pale Night, implying that there may be truth in both theories.<ref name="D360-p10-11">{{Cite dragon/360/Demonomicon of Iggwilv: Graz'zt, the Dark Prince|10-11}}</ref>"
— `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/graz-zt/wiki.txt:188`

- Asmodeus link: lines 186 and 188 name Asmodeus. The Asmodeus page (asmodeus.md) does not name Graz'zt (the campaign grep returned no Graz'zt line).

## Field 6: Campaign and published-adventure mentions

- Campaign: none (`campaign-hits.txt` is empty; the campaign grep found no Graz'zt line).
- Published adventure: none (`adventure-hits.txt` is empty; the JSON grep for Graz'zt, Grazzt, Dark Prince, Prince of Pleasure and Azzagrat matched no line).

## Field 7: Conflicts and not found

- **Conflict (origin):** line 186 gives an archdevil-turned-demon origin and line 188 gives Pale Night's child. The wiki calls them "competing, often contradictory theories".
- **Conflict (challenge):** `challenge5e` 24 (line 37) and `challenge3e` 32 (line 68), with the note at line 68 giving 22 (FC I) and 24 (BoVD).
- **Not found:** holy days, omens, messengers, pact cost (beyond the bargain at line 125), any Waterdeep cult or temple, any campaign NPC, faction or quest, any Graz'zt entry in `deities.json`.

---

# Cross-references

- Asmodeus page: `/home/user/waterdeep/campaign/setting/deities/asmodeus.md:51` (quoted at the top).
- WDMM, "demon lord" lines (none names the five powers):
  - `/home/user/waterdeep/sources/adventure-wdmm.json:54849`:
> "If the characters destroy the Runestone, Halaster sets out to destroy all the gargoyles and Stonecloaks on this level for failing him. He then begins luring and binding demons to the Runestone Caverns—nalfeshnees, glabrezus, hezrous, and vrocks, for a start. Eventually, he might get around to trapping a demon lord here as well."
  - `/home/user/waterdeep/sources/adventure-wdmm.json:6341` is a Juiblex line ("The wall carvings represent the all-consuming demon lord Juiblex"). Other "demon lord" lines name Baphomet: `:33297`, `:33317`, `:35233`, `:35252`.
- WDMM "Tenebrous" (a book title in a chest, not the demon lord): `/home/user/waterdeep/sources/adventure-wdmm.json:58833`:
> "The case holds texts on various arcane subjects, focusing on evocation magic and planar travel. Three of the texts are valuable (100 gp each). They are titled {@i Tenebrous and the True Path to Lichdom}, {@i Musings of a Planar Traveler}, and {@i Touched by the Far Realm: A Wizard's Lamentable Descent into Lunacy}. Tucked among these mundane tomes is Melissara's spellbook, which bears the (right side up) Shadowdusk family crest on the cover and contains the spells Melissara has prepared, plus {@spell arcane lock} and {@spell glyph of warding}."
- WDH "Major Temples of Waterdeep" table: `/home/user/waterdeep/sources/adventure-wdh.json:30910` (caption). The 15 rows (lines 30922–30996) name "All deities", "All elven deities", Gond, Helm, Ilmater, Lathander, "Mielikki, Silvanus", Mystra, Oghma, Selûne, Sune, Tempus, Tymora, Tyr and Umberlee. None of the five.
- WDH Asmodeus line outside the five (not quoted): `/home/user/waterdeep/sources/adventure-wdh.json:31715`, about Ammalia Cassalanter's worship of Asmodeus.

# Not found

Searches and files tried:

- `/home/user/waterdeep/campaign/` (all subfolders), first pass: the aliases listed at the top. Result: asmodeus.md:51 only.
- `/home/user/waterdeep/campaign/`, second pass: demon prince, demon lord, archdevil, Fiend patron, warlock patron, Mammon, Orcus, Graz, Demogorgon, Mephisto. Result: asmodeus.md lines 8, 31, 44, 45, 47, 48, 51, 52, 62, 69, 104 and 120 (all Asmodeus-only, apart from 51).
- `/home/user/waterdeep/sources/adventure-wdh.json`: all aliases. Result: no match. The temple table caption (line 30910) and its 15 rows name no patron.
- `/home/user/waterdeep/sources/adventure-wdmm.json`: all aliases. Result: only the lines listed in Cross-references.
- Wiki (all five): Waterdeep, Waterdhav, Dock Ward, Undermountain, Sea Ward, North Ward, Trollskull, Yawning Portal. Result: Mephistopheles lines 274, 283, 285, 286, 288; Mammon line 204.
- Wiki (all five): omen, messenger, herald, holy day, shrine, temple, church, Chosen, clergy, priest, sacrifice. Result: the body text is quoted under Field 4 for each power; no omen, no shrine, no holy day. The one "omen" hit in Graz'zt is inside the word "moment".
- Wiki (Orcus, Demogorgon, Graz'zt): Asmodeus, Mephisto, Mammon, Orcus, Demogorgon, Graz, Minauros, Thanatos, Cania, Azzagrat. Result: no cross-reference between the five except as quoted.
- Not searched: the Alexandrian PDFs and `sources/SOURCE_GUIDE.md` (outside this job's scope).

# Not readable

None. All bundle files were opened (5etools.md, campaign-hits.txt, adventure-hits.txt and wiki.txt for each of the five powers). The adventure-hits.txt files were empty.
