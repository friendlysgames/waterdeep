# Deities Pass 2, Batch I: Amaunator, Sune, Leira, Milil, Tempus

## Method and conventions

- **Bundles read in full:** the five `5etools.md`, five `wiki.txt` (each under 300 lines, so one chunk each), and the `campaign-hits.txt` and `adventure-hits.txt` files. Bundle folder: `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/<power>/`. Brief read at `/home/user/waterdeep/docs/plans/setting-compendium-pass2-brief.md` (lines 84-94). Model page read at `/home/user/waterdeep/campaign/setting/deities/asmodeus.md`.
- **Own targeted Grep:** all of `/home/user/waterdeep/campaign/`, `/home/user/waterdeep/sources/adventure-wdh.json` and `/home/user/waterdeep/sources/adventure-wdmm.json`, for every alias listed in the Not found sections.
- **Not consulted, as instructed:** the Alexandrian PDFs, `sources/SOURCE_GUIDE.md`, the `.docx` files, and the `docs/` research notes.
- **Wiki markup:** the only change to wiki text is that `[[ ]]` link brackets are removed, which the brief allows. Piped labels (for example `deity|god`), `{{ }}` templates and `<ref>` tags are kept as written. Annotations sit outside the quotes, on the citation line.
- **Line numbers:** bundle and wiki lines are line numbers in the bundle file. Campaign lines are in the named file. `sources/adventure-wdh.json` lines are the JSON line numbers. JSON indentation is removed. The strings are otherwise exact; JSON escapes such as `—` are shown as written in the source.
- **Edition tags:** the wiki infobox suffix shows the edition. `5eR` fields cite *Heroes of Faerûn* (HoF). Plain `5e` fields cite SCAG or PHB. `4e`, `3e`, `2e` and `1e` fields cite the books their `refs` lines name. Inline wiki citations are reported as the wiki gives them.
- **Gaps in the bundles:** my Grep found these lines that the bundles did not list.
  - Amaunator: both bundle hit files are empty. My Grep agrees: no hits.
  - Sune: `adventure-hits.txt` lacks `sources/adventure-wdh.json:30974` (the Temple of Beauty row) and `:31363` (the Grand Revel name line).
  - Leira: `campaign-hits.txt` is empty, but `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:83` and `:111` name her festivals.
  - Milil: `adventure-hits.txt` is empty. The Grand Revel lines `sources/adventure-wdh.json:31363` and `:31367` use the name of the holiday that the bundle's FRHoF entry gives to Milil, but they name Sune, Sharess and Lliira as its clergy.
  - Tempus: `adventure-hits.txt` lacks `sources/adventure-wdh.json:30979`, `:31229` and `:31414` (House of Heroes).
- **Not readable:** none. Every bundle file and every named campaign file opened.

---

## 1. Amaunator

### Answers

- **Q1 (temples or shrines in Waterdeep):** None found. No file places an Amaunator temple or shrine in Waterdeep. The "Major Temples of Waterdeep" table has no Amaunator row (see Field 6).
- **Q2 (campaign NPC, faction or quest):** None found.
- **Q3 (wiki lines that mention Waterdeep):** One line, and it is only a citation:
> "* {{Cite book/City of Splendors: Waterdeep}}"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/wiki.txt:231`

### Field 1: Identity

> "## Amaunator | source FRHoF p.100 | pantheon Faerûnian
> - altNames: ['The Keeper of the Eternal Sun', 'The Light of Law', 'The Yellow God']
> - title: God of the sun
> - worshipers: Farmers, lawmakers, travelers
> - plane: Mechanus"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/5etools.md:1-5` (FRHoF p.100)

> "## Amaunator | source SCAG p.21 | pantheon Faerûnian
> - altNames: ['The Keeper of the Eternal Sun', 'The Light of Law', 'The Yellow God']
> - title: God of the sun
> - alignment: ['L', 'N']
> - domains: ['Life', 'Light']
> - symbol: Golden sun"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/5etools.md:14-19` (SCAG p.21; the bundle's only source for alignment, domains and symbol)

> "| alignment5e         = Lawful neutral
> | symbol5e            = Golden sun"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/wiki.txt:37-38` (5e)

> "| domains5e           = Life domain|Life, Light domain|Light"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/wiki.txt:44` (5e)

> "| alignment4e         = Lawful good"
> "| domains4e           = Civilization domain|Civilization, Justice domain|Justice, Sun domain|Sun"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/wiki.txt:51` and `:58` (4e; see Field 7)

### Field 2: Edict or core tenet

No file lists an edict. The closest statements:

> "His priests teach that Amaunator has died and been reborn time and again. Like the sun, he might pass into the realm of darkness, but inevitably his bright gaze will fall on the world once again. Amaunator is seen as a stern and unforgiving deity, not unlike Silvanus in comportment, but his concern isn't for the balance of life - he cares that things proceed according to the celestial order, that promises are kept, and that the rule of law persists."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/5etools.md:22` (SCAG p.21)

> "Amaunator preached that people needed to follow the law to the letter. The reason for this was the belief that laws were the foundations on which any society was built and disrespecting the law would inevitably cause the collapse of any society.<ref name="F&A-28">{{Cite book/Faiths & Avatars|28}}</ref> The same adherence was also extended to traditions.<ref name="FRPG-150">{{Cite book/Forgotten Realms Player's Guide|150}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/wiki.txt:169` (cites Faiths & Avatars 28, which the infobox lists under `refs2e` at line 93)

### Field 3: Portfolio and Areas of Concern

> "The rule of law and the glory of the sun both fall in Amaunator's dominion. He is a stern and unforgiving god, concerned with keeping promises and maintaining order."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/5etools.md:7` (FRHoF p.100)

> "| portfolio5eR        = Law, the sun"
> "| portfolio5e         = Law, the sun"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/wiki.txt:28` and `:43` (5eR and 5e)

> "| portfolio2e         = Bureaucracy, contracts, law, order, rulership, the sun"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/wiki.txt:87` (2e)

Areas of Concern: no bundle file has the field. Not found.

### Field 4: Worship (clergy, holy days, temples, omens, messengers)

> "Amaunator's priests help establish bureaucracies and order in communities. They witness contracts and signed agreements, signifying these documents' validity by stamping them with the god's sun symbol. Temples to Amaunator feature courtyards and skylights to invite the god's bright gaze. In underground settlements or places plagued by cloud cover, his temples mount a torch with a {@spell Continual Flame|XPHB} spell cast on it over their doorway to symbolize the sun. Amaunator's temples keep extensive records of their surrounding community's laws and legal proceedings. Most temples make these records available to the public for transparency. In places where corruption has spread even to Amaunator's temples, access to these records cost a hefty sum."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/5etools.md:11` (FRHoF p.100; clergy and temples)

> "Priests of Amaunator encouraged the establishment of lawful order and bureaucracy in the world at large. They were called on to witness contracts and apply a signatory stamp with the symbol of Amaunator to verify its validity.<ref name="SCAG5e-p21,24" />"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/wiki.txt:189` (SCAG p.21, 24)

> "| holy days2e         = Third full moon of the year, summer solstice"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/wiki.txt:91` (2e only; the 5eR, 5e and 4e holy-day fields are blank at lines 32, 47 and 62)

> "When Amaunator sends a messenger, its presence is unmistakable: a {@creature Couatl|XMM} or a seemingly ordinary bird with gleaming eyes like miniature suns descends from the heavens in a shaft of bright light. Amaunator also communicates with his followers via dreams in which the darkness of night is suddenly vanquished by the broad daylight."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/5etools.md:9` (FRHoF p.100; messengers)

> "The Chosen of Amaunator master magic that dispels darkness and unveils hidden truths. Some work to enforce the law across the land; others become magistrates in Faerûn's highest courts."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/5etools.md:12` (FRHoF p.100)

> "Another manifestation of his were thirteen giant hyenas. These were sent by the Yellow God to punish people who deserved such or to avenge people who did not have the ability to do it themselves. When these hyenas appeared the offender was killed by them and the body was ripped apart to cover 1 acre (4047 square meters).<ref name="F&A-27"/>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/wiki.txt:154` (omen-type manifestation; cites Faiths & Avatars 27)

### Field 5: Relations with other powers and origin (edition as tagged)

> "| servedby4e          = Siamorphe"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/wiki.txt:56` (4e infobox; the 4e refs at line 64 cite Forgotten Realms Campaign Guide 63, 80)

> "After returning, he was served by Siamorphe as his exarch and lived with Waukeen on his astral domain Eternal Sun.<ref name="FRCG-63"/>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/wiki.txt:178` (cites Forgotten Realms Campaign Guide 63)

> "It was eventually claimed, following the Spellplague, that Lathander, the Faerûnian deity|god of the sun, was an aspect of the long-dormant Amaunator.<ref name="FRCG-72">{{Cite book/Forgotten Realms Campaign Guide|72}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/wiki.txt:118` (cites Forgotten Realms Campaign Guide 72)

> "He dropped from greater deity-status to lesser deity-status and from there to dead power-status over a millennium."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/wiki.txt:196` (sentence; the paragraph cites Faiths & Avatars 27 and sets the fall around 661 DR; origin after Karsus's Folly)

> "Once he came back to life, he created the astral dominion Eternal Sun and lived there with Siamorphe and Waukeen.<ref name="FRCG-63">{{Cite book/Forgotten Realms Campaign Guide|63}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/wiki.txt:166` (cites Forgotten Realms Campaign Guide 63)

> "Apparently, he found Sune attractive.<ref name="FRCG-77">{{Cite book/Forgotten Realms Campaign Guide|77}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/amaunator/wiki.txt:180` (cites Forgotten Realms Campaign Guide 77)

### Field 6: Campaign and published-adventure mentions

- **Campaign:** none. The bundle `campaign-hits.txt` is empty. My Grep of `campaign/` for "Amaunator", "Keeper of the Eternal Sun", "Yellow God", "Eternal Sun" and "Light of (the) Law" returned no lines.
- **Published adventure:** none. The bundle `adventure-hits.txt` is empty. My Grep of `sources/adventure-wdh.json` and `sources/adventure-wdmm.json` for the same terms returned no lines.
- **Table row:** the "Major Temples of Waterdeep" table (caption at `/home/user/waterdeep/sources/adventure-wdh.json:30910`) has no Amaunator row.

### Field 7: Conflicts and what was not found

- **Alignment.** Wiki 4e says "Lawful good" (`wiki.txt:51`). The SCAG entry says `alignment: ['L', 'N']` (`5etools.md:17`), and the wiki 5e field says "Lawful neutral" (`wiki.txt:37`). The brief makes SCAG the only alignment source, so use Lawful neutral. The 4e value is a superseded edition.
- **Domains.** Wiki 4e gives Civilization, Justice and Sun (`wiki.txt:58`). SCAG gives `domains: ['Life', 'Light']` (`5etools.md:18`). The wiki 5e field (`wiki.txt:44`) agrees with SCAG.
- **Plane.** FRHoF says "- plane: Mechanus" (`5etools.md:5`). The wiki says "Once he came back to life, he created the astral dominion Eternal Sun and lived there with Siamorphe and Waukeen." (`wiki.txt:166`). FRHoF is the higher-ranked source for the plane field. The two statements describe different places of residence.
- **Lathander.** FRHoF says "They quarrel with followers of Lathander over whether Lathander is an aspect of Amaunator or is a separate deity." (`5etools.md:8`). The wiki says "It is unknown if they were actually separate beings by this time or one was the aspect of the other." (`wiki.txt:217`, cites SCAG 13, 21, 24, 32). Both sources leave this open, so this is not a conflict.
- **Not found:** Areas of Concern; an edict list; any Waterdeep temple or shrine; any campaign or published-adventure mention; any Chosen named in the campaign; any holy day in FRHoF or SCAG.

---

## 2. Sune

### Answers

- **Q1 (temples or shrines in Waterdeep):** The Temple of Beauty, in the Sea Ward. The table row at `/home/user/waterdeep/sources/adventure-wdh.json:30973-30975` (see Field 6 for the lines). The Sea Ward text at `/home/user/waterdeep/sources/adventure-wdh.json:30883` names the same temple. No campaign file names it.
- **Q2 (campaign NPC, faction or quest):** None in `campaign/`. The only Sune-linked event is the published adventure's Grand Revel, led by "the clergy of Sune, Sharess, and Lliira" (`/home/user/waterdeep/sources/adventure-wdh.json:31367`). It is not a campaign NPC, faction or quest.
- **Q3 (wiki lines that mention Waterdeep):** None. Grep of all five `wiki.txt` files found no Waterdeep line.

### Field 1: Identity

> "## Sune | source FRHoF p.122 | pantheon Faerûnian
> - altNames: ['Lady Firehair', 'The Lady of Love', 'The Princess of Passion']
> - title: God of love and beauty
> - worshipers: Artists, hedonists, lovers
> - plane: Arborea (Arvandor)"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/sune/5etools.md:1-5` (FRHoF p.122)

> "## Sune | source SCAG p.21 | pantheon Faerûnian
> - altNames: ['Lady Firehair', 'The Lady of Love', 'The Princess of Passion']
> - title: Goddess of love and beauty
> - alignment: ['C', 'G']
> - domains: ['Life', 'Light']
> - symbol: Face of a beautiful red-haired woman"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/sune/5etools.md:27-32` (SCAG p.21; the PHB p.294 entry at lines 19-23 gives the same alignment, domains and symbol)

> "| alignment5e         = Chaotic good
> | symbol5e            = Face of a beautiful red-haired woman"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/sune/wiki.txt:37-38` (5e)

> "| gender              = Feminine"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/sune/wiki.txt:16`

### Field 2: Edict or core tenet

> "But beauty is more than skin deep, say Sune's followers; it issues from the core of one's being and shows one's true face to the world. The followers of Sune believe in romance, true love winning over all, and following the heart to its true destination. Fated matches, impossible loves, and embracing beauty beyond the physical are the purview of Sune."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/sune/5etools.md:10` (FRHoF p.122)

> "{{quote|Beauty is more than skin deep; it issues from the core of one's being and shows one's fair (or foul) face to the world.|A Sunite saying.<ref name="SCAG5e-p21,37-38" /><ref name="FA-150">{{Cite book/Faiths & Avatars|150}}</ref>}}"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/sune/wiki.txt:129` (a Sunite saying; cites SCAG 21, 37-38)

> "Sune was a benevolent goddess<ref name="FaP-65-67"/> who abhorred the destruction of beauty.<ref name="FA-149-151" />"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/sune/wiki.txt:136` (sentence)

### Field 3: Portfolio and Areas of Concern

> "Sune Firehair is a deity of passion and the delights of the senses. She is the god of beauty in all its forms—not just pleasing sights, but also enchanting sounds, luxurious tastes and scents, and exquisite sensual pleasures, from a lover's caress to the whispering brush of silk on the skin. Her worshipers seek out these pleasures in life, not out of mere decadence, but because the experience of pleasure is an act of worship."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/sune/5etools.md:7` (FRHoF p.122)

> "| portfolio5eR        = Love, beauty, passion"
> "| portfolio5e         = Love, beauty, passion"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/sune/wiki.txt:28` and `:43`

> "| portfolio2e         = Beauty, love, passion"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/sune/wiki.txt:89` (2e)

Areas of Concern: no bundle file has the field. Not found.

### Field 4: Worship (clergy, holy days, temples, omens, messengers)

> "When she doesn't speak in dreams or visions, she sends a {@creature Couatl|XMM} or {@creature Deva|XMM} to act as muse on her behalf."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/sune/5etools.md:8` (FRHoF p.122; messengers)

> "Temples dedicated to Sune serve as public baths and places of relaxation. A temple features a mirrored and well-lit salon where individuals can enhance their appearance, as well as see others and be seen. In remote locales or in parts of sprawling cities far from a temple, small, roofed shrines to Sune provide her followers convenient access to beautification resources. Each shrine bears a mirror and is stocked with free perfumes and cosmetics."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/sune/5etools.md:11` (FRHoF p.122)

> "Temples dedicated to Sune are common in human lands, and they frequently serve as public baths and places of relaxation. A temple usually features a mirrored and well-lit salon where folks can primp, as well as see others and be seen. Where a temple doesn't exist, or in a large city where the nearest temple might be too far to walk to, a small shrine to Sune often stands near a street corner. These sites consist of a mirror hung beneath a small roof where one can say a prayer while checking one's appearance. The spot might feature a shelf or a cupboard holding various perfumes and cosmetics so that those without the funds to purchase such items can still make themselves feel beautiful."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/sune/5etools.md:38` (SCAG p.21, 37-38)

> "Her temples usually held social salons and displayed mirrors for use by lay parishioners. Some of them even had public baths for the local populace.<ref name="SCAG-p37">{{Cite book/Sword Coast Adventurer's Guide|37}}</ref> Her shrines often stood on the corner of busy city streets. They would have a small ornate overhanging roof with a mirror underneath. They were used to check one's appearance while honoring Sune with prayer. Some shrines even held perfume and cosmetic items for those who could not afford such luxuries themselves.<ref name="SCAG-p38">{{Cite book/Sword Coast Adventurer's Guide|38}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/sune/wiki.txt:172` (cites SCAG 37, 38)

> "| holy days3e         = Greengrass, Midsummer night"
> "| holy days2e         = Greengrass, Midsummer night"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/sune/wiki.txt:79` and `:93` (3e and 2e; the 5e holy-day field at line 48 is blank)

> "Sodality of the Ruby Rose: The Sodality of the Ruby Rose is a knightly order dedicated to Lady Firehair and tasked with guarding Sune's temples and holy sites."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/sune/5etools.md:13` (FRHoF p.122)

Chosen: "Sune's Chosen exemplify some aspect of beauty." (`5etools.md:12`, FRHoF p.122). Omitted from the quote list because of the six-quote limit.

### Field 5: Relations with other powers and origin (edition as tagged)

> "Sune was served by both Lliira and Sharess and was allies with Milil, Lathander, and Selûne, the latter of which was also a servant of Lady Firehair in the past before going her own way,<ref name="FaP-65-67" /> though they were still extremely friendly and cooperative.<ref name="FA-135">{{Cite book/Faiths & Avatars|135}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/sune/wiki.txt:161` (cites Faiths and Pantheons 65-67 and Faiths & Avatars 135; the 4e servedby line at 57 reads "| servedby4e          = Lliira, Sharess")

> "She also had no love for Talona, goddess of disease, or Tempus, god of battle, on similar grounds, although the latter considered her too flighty and irrelevant to be worth the conflict or even dislike.<ref name="FaP-65-67" />"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/sune/wiki.txt:163` (sentence; cites Faiths and Pantheons 65-67)

> "Sune had been romantically linked with many members of the Faerunian pantheon in the many myths of the realms; for example she was said to have been smitten with Torm for his actions during the Time of Troubles,<ref name="FaP-65-67" /> and many deities, including Torm himself as well as Amaunator, had become smitten with her in turn. In regards to such matters, the Lady of Love was simultaneously distant and flirtatious.<ref name="FRCG4e-63,77,80" />"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/sune/wiki.txt:159` (cites Forgotten Realms Campaign Guide 63, 77, 80, the 4e refs at line 65)

> "During the Spellplague, Sune moved Brightwater to Selûne's realm, the Gates of the Moon. Most of the other goddesses joined her in her romantic city, though Tymora had her own area within the Gates known as the Tymora#Divine_Realm|Great Wheel, and Waukeen's Marketplace Eternal moved to Amaunator's realm.<ref name="FRCG4e-63,77,80" />"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/sune/wiki.txt:156` (cites Forgotten Realms Campaign Guide 63, 77, 80; pipe label kept as written)

> "During the Time of Troubles, Sune rescued Sharess from death at the hands of Shar and restored the corrupted deity to her original state before Shar's influence affected her.<ref>{{Cite book/Powers & Pantheons|52}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/sune/wiki.txt:187` (cites Powers & Pantheons 52)

> "During the Spellplague, Sune's plane of Brightwater was destroyed, but Selûne invited Sune and her exarchs to join her in the Gates of the Moon."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/sune/wiki.txt:189` (sentence; the paragraph continues with the claim that Hanali Celanil and other love powers were aspects of Sune)

### Field 6: Campaign and published-adventure mentions

- **Campaign:** none. The bundle `campaign-hits.txt` is empty. My Grep of `campaign/` for `Sune`, `Sunite`, `Lady Firehair`, `Lady of Love`, `Princess of Passion`, `Temple of Beauty`, `Ruby Rose`, `Sodality` and `Brightwater` returned no Sune reference. The only hit was "Tessaly Brightwater", a Factor's name in `campaign/quests/faction-events/lords-alliance/r10-stingblade/ev-01-stingblade.md:126`, which is not the deity.
- **Published adventure, Sea Ward:**
> "If you need to refresh yourself during your travels, or perhaps to primp before an important meeting or a night out, visit Sune's faithful at the Temple of Beauty. Its marbled public baths and mirrored salons are open from before dawn to after dusk. There's no fee for these services, or for the advice and aid of the temple's many pleasant attendants, but donations are encouraged."
> — `/home/user/waterdeep/sources/adventure-wdh.json:30883`

- **Published adventure, "Major Temples of Waterdeep" table** (caption `/home/user/waterdeep/sources/adventure-wdh.json:30910`, "caption": "Major Temples of Waterdeep"). Copied as JSON lines; the row's bracket lines at 30972 and 30976 are omitted:
> "Sune",
> "Temple of Beauty",
> "Sea Ward"
> — `/home/user/waterdeep/sources/adventure-wdh.json:30973-30975`

- **Published adventure, Grand Revel:**
> "name": "Alturiak 14: The Grand Revel",
> — `/home/user/waterdeep/sources/adventure-wdh.json:31363`

> "Led by the clergy of Sune, Sharess, and Lliira, the Grand Revel is a day of dancing, music, and the consumption of sweet treats of all kinds, from chocolate to red firemint candies."
> — `/home/user/waterdeep/sources/adventure-wdh.json:31367` (sentence; the rest of the paragraph covers the street ring dances, the "love feasts" at dusk, and blessed rings)

### Field 7: Conflicts and what was not found

- **Title and gender.** FRHoF says "- title: God of love and beauty" (`5etools.md:3`). SCAG and PHB say "- title: Goddess of love and beauty" (`5etools.md:20` and `:29`). FRHoF is the higher-ranked source for the title.
- **Worshipers.** The wiki's 5eR field says "| worshipers5eR       = Artists, hedonists, lovers" (`wiki.txt:30`). Its 5e field says "| worshipers5e        = Hedonists, promoters of art" (`wiki.txt:45`). FRHoF (`5etools.md:4`) is the higher-ranked source.
- **Grand Revel.** The published adventure gives the Grand Revel to Sune, Sharess and Lliira on Alturiak 14 (`sources/adventure-wdh.json:31367`). The bundle's Milil entry gives a Grand Revel to Milil at Midsummer. See Milil, Field 7.
- **Not found:** a Sune NPC, faction or quest in `campaign/`; any Sunite NPC named in the wiki (Adon of Sune, Histra, Taegan Nightwind, Joelle Emmeline, `wiki.txt:178-181`) in `campaign/`; any Sodality or Ruby Rose member in `campaign/`; any Sune shrine in Waterdeep other than the Temple of Beauty; any Sune line in `sources/adventure-wdmm.json`.

---

## 3. Leira

### Answers

- **Q1 (temples or shrines in Waterdeep):** None. The published adventure and the campaign place no Leira temple in Waterdeep. The SCAG entry says: "Only in Nimbral do temples to Leira exist, and shrines dedicated to her found across the continent are usually disguised as other kinds of sites, marked with signs that only the faithful would recognize." (`/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/5etools.md:31`)
- **Q2 (campaign NPC, faction or quest):** None. The campaign names two of her festivals and no NPC, faction or quest. See Field 6.
- **Q3 (wiki lines that mention Waterdeep):** None.

### Field 1: Identity

> "## Leira | source FRHoF p.112 | pantheon Faerûnian
> - altNames: ['The Lady of Deception', 'The Lady of the Mists', 'Mistshadow']
> - title: God of illusion
> - worshipers: Actors, con artists, Illusionists, Rogues
> - plane: Limbo"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/5etools.md:1-5` (FRHoF p.112)

> "## Leira | source SCAG p.21 | pantheon Faerûnian
> - altNames: ['The Lady of the Mists', 'Mistshadow', 'The Lady of Deception']
> - title: Goddess of illusion
> - alignment: ['C', 'N']
> - domains: ['Trickery']
> - symbol: Point-down triangle containing a swirl of mist"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/5etools.md:21-26` (SCAG p.21)

> "| alignment5e         = Chaotic neutral"
> "| domains5e           = Trickery domain|Trickery"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/wiki.txt:37` and `:44` (5e)

> "| died                = 1358 DR (apparently)"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/wiki.txt:14`

> "| power2e             = Lesser deity, presumed dead"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/wiki.txt:81` (2e)

### Field 2: Edict or core tenet

> "Rogues, con artists, illusionist mages, and actors hold Leira in high regard, though none can identify specifics about the god or her intentions. She is an enigmatic deity of illusions, disguises, and deception."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/5etools.md:7` (FRHoF p.112)

> "Leira isn't viewed as malicious or as a trickster but is seen as enigmatic, quiet, and retiring."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/5etools.md:29` (SCAG p.21)

> "She was an enigma, never telling the truth when falsehood would do. Everything she did and said was shrouded in layers of illusion and lies.<ref name="FA-93-96" />"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/wiki.txt:117` (cites Faiths and Avatars 93-96)

> "Some folk perform a swirling motion with a finger behind their backs when telling a lie as a way of beseeching Leira for aid.Her faithful keep their secrets close and refrain from telling the truth when falsehoods or half-truths would serve them better. Only among fellow worshipers of Leira do they feel comfortable enough to speak plainly."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/5etools.md:9` (FRHoF p.112; "aid.Her" is the source's spelling)

### Field 3: Portfolio and Areas of Concern

> "| portfolio5eR        = Illusions, disguises, deception"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/wiki.txt:28` (5eR; brackets removed from `[[Illusion]]s`)

> "| portfolio5e         = Illusion, deception"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/wiki.txt:43`

> "| portfolio2e         = Deception, illusion"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/wiki.txt:88` (2e)

Areas of Concern: no bundle file has the field. Not found.

### Field 4: Worship (clergy, holy days, temples, omens, messengers)

> "No images or statues of Leira grace her temples, since her priests know it is useless to presume the true appearance of a god of illusion. Her temples are disguised as other sites, marked with signs that only the faithful recognize. Leira's temples are filled with a white mist that normally remains low but can rise to fill the room and thicken to obscure vision if the temple's high priest desires. Her priests wear vestments of white and mist gray, and their faces are covered by smooth, featureless masks. They are loath to reveal their faces to the unfaithful and sometimes wield sleep-inducing poisons."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/5etools.md:10` (FRHoF p.112)

> "Her priests wear vestments of white and mist-gray, and their faces are covered by smooth, featureless masks. Only in Nimbral do temples to Leira exist, and shrines dedicated to her found across the continent are usually disguised as other kinds of sites, marked with signs that only the faithful would recognize."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/5etools.md:31` (SCAG p.21)

> "The faithful of Leira seem to be scarce, although it is difficult to know this for certain, because those who favor her rarely make their inclinations known. Leira is the patron of illusionists and liars. She receives little regular worship except from illusionists, who pray to the Mistshadow for potency in their magic, and con artists, for whom she is a kind of champion. Most people pray to her when they hope to keep something secret, or placate her with a prayer before making an important decision when they fear being deceived. Some folk perform a swirling motion with a finger behind their backs when telling a lie as a way of beseeching her for aid."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/5etools.md:30` (SCAG p.21)

> "Leira had quite a small following. Her priests, known as Leirans, or Worshipers of the Mistshadow, wore silver mask (object)|masks and often disguised themselves to deceive those around them. Leirans would speak the truth only to other Leirans. High-level clerics of the Leiran faith were called Mistcallers.<ref name="FA-94-95">{{Cite book/Faiths & Avatars|94-95}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/wiki.txt:123` (the whole paragraph; pipe label kept as written)

> "Nevertheless, {@creature Displacer Beast|XMM|Displacer Beasts} are sometimes seen as omens of her will, especially when encountered in places beyond the ordinary reach of fey influence."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/5etools.md:8` (FRHoF p.112; omens, sentence)

Holy days: the wiki's holy-day fields are blank in every edition that has one (`wiki.txt:32` 5eR, `:48` 5e, `:92` 2e). The published adventure's holy day is in Field 6.

### Field 5: Relations with other powers and origin (edition as tagged)

> "Leira's allies were Mask, who betrayed her, and Azuth. Though she had no enemies,<ref name="FaA-93" /> she was opposed by Oghma, as her lies were a hindrance to knowledge.<ref name ="FAP54">{{Cite book/Faiths and Pantheons|54}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/wiki.txt:139`

> "Months after the Time of Troubles|Avatar Crisis,<ref name="TGHotR-144">{{Cite book/The Grand History of the Realms|144}}</ref> Leira was slain by the new deity of death, Cyric,<ref name="LEoF-p42"/> at the village Blackfeather Bridge,<ref name="FRCS-130">{{Cite book/Forgotten Realms Campaign Setting 3rd edition|130}}</ref> wielding the sword Godsbane, which was in fact an avatar of Mask.<ref name="LEoF-p42"/> Her portfolios were subsequently absorbed by the mad god.<ref name="FaA-93" />"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/wiki.txt:142` (pipe label kept as written; cites Lost Empires of Faerûn 42 and Faiths & Avatars 93)

> "By the late 15{{th}} century DR, it became known that Leira was in fact alive and delighted in the confusion created by rumors of her demise and return. At this time, the faithful of Cyric also considered her to be his daughter.<ref name="SCAG5e-p21,32" />"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/wiki.txt:148` (cites SCAG 21, 32)

> "In the ''Player's Handbook 5th edition'', Leira is listed in the "Deities of the Forgotten Realms" table, suggesting she is officially considered alive once more in the 5{{th}} edition of the setting."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/wiki.txt:152` (wiki's own note on 5e)

> "Leira maintained a divine realm called the Courts of Illusion on the chaotic plane of Limbo. After her apparent demise, her body was thought to be adrift on the Astral Plane, like those of other dead powers.<ref name="FaA-93"/>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/wiki.txt:120` (cites Faiths & Avatars 93)

> "Shortly after the Time of Troubles, Cyric slew Leira and became the god of lies in her stead. On her return, Leira reclaimed most of her portfolio, but not all of it."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/leira/5etools.md:8` (FRHoF p.112)

### Field 6: Campaign and published-adventure mentions

- **Campaign, festival table:** the Waukeentide row names "Leiruin on Tarsakh 10" (`/home/user/waterdeep/campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:83`):
> "| Tarsakh 1 to 10 | Waukeentide | A tenday of commerce honoring Waukeen. Caravance on Tarsakh 1 (gift-giving), Goldenight on Tarsakh 5 (shops open all night), Guildsmeet on Tarsakh 7 (a guild gala from dusk to dawn) and Leiruin on Tarsakh 10 (guild dues paid and charters renewed with the Lords). | Trade festival. Cassalanter social events peak. Cover for Cassalanter Villa surveillance. |"

- **Campaign, after-window calendar** (`/home/user/waterdeep/campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:111`):
> "After the window, the calendar continues with Midsummer and Shieldmeet, Ahghairon's Day (Eleasis 1), Brightswords (Eleint 21), Stoneshar (Marpenoth 7), the Reign of Misrule (Marpenoth 10), Gods' Day (Marpenoth 15) and Liar's Night (Marpenoth 30). These matter only if play runs past Flamerule 11."

- **Published adventure, Leiruin** (`/home/user/waterdeep/sources/adventure-wdh.json:31405`; the paragraph's earlier entries cover Caravance, Goldenight and Guildsmeet):
> "{@b Leiruin (Tarsahk 10}). In times long past, Waukeen caught Leira, the goddess of illusions and deception, attempting to cheat her in a deal, and buried her under a mountain of molten gold as punishment. A commemoration of that event, Leiruin is the day for guild members to pay their annual dues and for guildmasters to meet with the Lords of Waterdeep and renew their charters for another year."

- **Published adventure, Liar's Night:**
> "name": "Marpenoth 30: Liar's Night",
> — `/home/user/waterdeep/sources/adventure-wdh.json:31541`

> "This holy day pays tribute to Leira and Mask. To placate those deities and ward away their attention, folk of all walks of life don masks and costumes (magical or mundane) to disguise themselves and play at being other than what they are. Commonly seen mask styles include the black mask symbol of Mask and the mirror face of the priests of Leira. But there are no bounds on the disguise you don, and the more elaborate and outlandish it is, the more celebrated the wearer."
> — `/home/user/waterdeep/sources/adventure-wdh.json:31545`

Campaign NPC, faction or quest: none. The calendar names Leiruin and Liar's Night only. Neither entry links to Leira as a character or to a faction.

### Field 7: Conflicts and what was not found

- **Title and gender.** FRHoF says "- title: God of illusion" (`5etools.md:3`). SCAG says "- title: Goddess of illusion" (`5etools.md:23`). FRHoF is the higher-ranked source.
- **Status.** FRHoF says Leira returned (`5etools.md:8`, quoted in Field 5). The wiki's 2e field says "presumed dead" (`wiki.txt:81`), and its 3e field says "Dead power" (`wiki.txt:66`). The wiki's 5e note says she is alive (`wiki.txt:152`). FRHoF and the 5e entries agree on alive.
- **Death story.** The wiki says Cyric killed her at Blackfeather Bridge (`wiki.txt:142`, quoted in Field 5). The published adventure says "In times long past, Waukeen caught Leira, the goddess of illusions and deception, attempting to cheat her in a deal, and buried her under a mountain of molten gold as punishment." (`sources/adventure-wdh.json:31405`). The adventure's version is festival lore. The two accounts do not match.
- **Not found:** a Leira temple in Waterdeep; a Leiran or Mistcaller NPC in `campaign/`; a Leira Chosen; any holy day for Leira in the wiki's own holy-day fields (blank); any Leira reference in `sources/adventure-wdmm.json`.

---

## 4. Milil

### Answers

- **Q1 (temples or shrines in Waterdeep):** The campaign names a "Temple of Milil" but gives no ward or address. The line is in `/home/user/waterdeep/campaign/guides/trollskull-manor/03-staff-and-hiring.md:85`, quoted in Field 6. The published adventure has no Milil temple. The wiki's temple is in Athkatla, not Waterdeep (`wiki.txt:148`, quoted in Field 5).
- **Q2 (campaign NPC, faction or quest):** One campaign NPC. Lysa of the White Lute, a Trollskull Manor staff candidate, has "played twelve years at guild functions and the Temple of Milil" (`03-staff-and-hiring.md:85`). No faction or quest names Milil.
- **Q3 (wiki lines that mention Waterdeep):** None.

### Field 1: Identity

> "## Milil | source FRHoF p.116 | pantheon Faerûnian
> - altNames: ['The Lord of All Songs', 'The First Poet', 'The Bard of Oghma']
> - title: God of poetry and song
> - worshipers: Bards, orators, poets, singers
> - plane: Elysium (Amoria)"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/5etools.md:1-5` (FRHoF p.116)

> "## Milil | source SCAG p.21 | pantheon Faerûnian
> - altNames: ['The Lord of Song', 'The One True Hand of All-Wise Oghma']
> - title: God of poetry and song
> - alignment: ['N', 'G']
> - domains: ['Light']
> - symbol: Five-stringed harp made of leaves"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/5etools.md:21-26` (SCAG p.21)

> "| alignment5e         = Neutral good
> | symbol5e            = Five-stringed harp made of leaves"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/wiki.txt:30-31` (5e)

> "| homeplane5eR        = Elysium (Amoria)"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/wiki.txt:17` (5eR; brackets removed)

> "| serves5e            = Oghma"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/wiki.txt:34` (5e)

### Field 2: Edict or core tenet

No edict. Core statements:

> "Milil is the ideal to which performers aspire: poised and confident, winningly charismatic, and a source of inspiration. Songbirds are heralds of Milil. He manifests to mortals as a beautiful, haunting voice echoing through open spaces or through visions that appear to entertainers during performances."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/5etools.md:8` (FRHoF p.116; the same line begins "Like Deneir, Milil defers to Oghma's will, and he is sometimes thought of as Oghma's left hand.")

> "He represents the finished thought, the result of the process that takes an idea from conception to realization."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/5etools.md:28` (SCAG p.21)

### Field 3: Portfolio and Areas of Concern

> "Milil is a god of poetry, eloquence, and song. He is also a god of creativity and inspiration, of the essence of song beyond the lyrics or the music."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/5etools.md:7` (FRHoF p.116)

> "| portfolio5eR        = Poetry, eloquence, song, creativity, inspiration"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/wiki.txt:21` (5eR)

> "| portfolio2e         = Eloquence, poetry, song"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/wiki.txt:81` (2e)

> "| sphere4e            = Song"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/wiki.txt:51` (4e)

Areas of Concern: no bundle file has the field. Not found.

### Field 4: Worship (clergy, holy days, temples, omens, messengers)

> "Worshipers dedicate holy sites to Milil in performance venues and music schools. Whether the site is a vast concert hall or a small choral chamber, it must have excellent acoustic qualities. Milil's priests are patrons of the arts, performers, and tutors. Each year on {@book Midsummer|FRHoF|2|Midsummer}, priests of Milil hold a holiday called the Grand Revel. In this ceremony, clergy and other followers of Milil dance, feast, act out parodies, and join in wickedly satirical song. Though it isn't an expressly political event, those in power are the revel's biggest targets. For this reason, tyrannical rulers outlaw the Grand Revel—though priests of Milil still conduct it in small, private ceremonies."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/5etools.md:10` (FRHoF p.116; temples, holy sites, holy day)

> "Milil's Chosen have angelic voices that resonate far beyond those of most mortals. Their passionate words can crack the hardest of hearts, whether through song or oration."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/5etools.md:11` (FRHoF p.116)

> "He was predominantly worshiped by human, elf, and half-elf bards but attracted other musically inclined individuals such as troubadours and poets.<ref name="F&A-116">{{Cite book/Faiths & Avatars|116}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/wiki.txt:140` (sentence; cites Faiths & Avatars 116)

> "*Harmonious Order: This group of personable and swaggering paladins encouraged bards to accompany them to create ballads based on their exploits taken in Milil's name.<ref name="F&A-118">{{Cite book/Faiths & Avatars|118}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/wiki.txt:143` (the wiki's list marker is a leading asterisk)

> "To signify his approval of artistic work, whether it be a song, epic poem, theatrical performance or the like, Milil would conjure a golden-lined image of two dancing hollyphants."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/wiki.txt:119` (sentence; cites Faiths & Avatars 116; the omen-type sign of approval)

Messengers: the bundle's FRHoF says "Songbirds are heralds of Milil." (`5etools.md:8`, quoted in Field 2). Holy days: the wiki's holy-day fields are blank (`wiki.txt:25` 5eR, `:41` 5e, `:56` 4e, `:71` 3e, `:85` 2e, `:98` 1e). The FRHoF holy day is in the Field 4 quote from `5etools.md:10`.

### Field 5: Relations with other powers and origin (edition as tagged)

> "As a deity, Milil, along with Deneir and Gond, served the greater power of Oghma. Despite this shared service, Milil had little in common with Gond, and they had a slightly strained relationship.<ref name="F&A-116"/><ref name="FaP-102"/>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/wiki.txt:131` (cites Faiths & Avatars 116; Faiths and Pantheons 102)

> "Milil maintained very good relations with a number of powerful gods, including Mystra, Sune, and Lliira, as well as with the gods of the Seldarine|elven pantheon. He felt that Finder Wyvernspur showed some promise, but Finder did not feel the same about Milil.<ref name="F&A-116"/><ref name="FaP-102"/>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/wiki.txt:133` (pipe label kept as written)

> "After Milil made a mocking ballad about Cyric and his insanity, the Prince of Lies became an enemy of the Lord of Song.<ref name="FaP-102"/>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/wiki.txt:135`

> "During the Era of Upheaval, Milil was simply an exarch of Oghma.<ref name="FRCG4e-p81" />"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/wiki.txt:152` (cites Forgotten Realms Campaign Guide 81, the 4e refs at line 58)

> "Soon after making a mocking ballad about Cyric, Milil was ejected from the pantheon and banished to the Fugue Plane. As a result, musical prayers went out of fashion among bards. Some time before the late {{YearlinkName|1400}}, Lord of Song was rescued by a mysterious being called Withers, who pulled him out of the Fugue Plane. However, as payment, Milil had to "honor the worthy", whenever Withers asked him to, a favour he was eternally invoking.<ref name="FaP-102"/><ref name="BGIII">{{Cite game/Baldur's Gate III}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/wiki.txt:154`

> "During the Time of Troubles, Milil appeared in Athkatla, where he founded a singing circle in Arbalest's House, a temple dedicated to his own glorification. He tasked the Patriarch of Song to oversee continued development of the temple, and to expand the ranks of the faithful.<ref name="F&A-117" />"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/wiki.txt:148` (Athkatla, not Waterdeep; cites Faiths & Avatars 117)

### Field 6: Campaign and published-adventure mentions

- **Campaign, Trollskull Manor staff table** (`/home/user/waterdeep/campaign/guides/trollskull-manor/03-staff-and-hiring.md:85`, whole table row):
> "| 2 | **Lysa of the White Lute** | NG half-elf | Carries her lute case like something fragile. Sits straight. "I haven't performed professionally. I want to be transparent about that." Has played twelve years at guild functions and the Temple of Milil. "I would like to find out if I'm good in front of people who don't already like me." More talented than she knows. | None. Father's Carpenters' Guild connections occasionally useful. | 6 gp (rises to 8 gp if she succeeds) | First tenday: DC 13 Performance roll — success: +1 Fame, +2 Revenue; failure: −1 Fame. Needs encouragement (DC 12 Persuasion or sincere support) to return after a failure. From second tenday: +1 Fame, +3 Revenue. |"

- **Published adventure, Grand Revel name** (`/home/user/waterdeep/sources/adventure-wdh.json:31363`):
> "name": "Alturiak 14: The Grand Revel",

- **Published adventure, Grand Revel** (`/home/user/waterdeep/sources/adventure-wdh.json:31367`, first sentence; the paragraph names Sune, Sharess and Lliira, and Milil nowhere):
> "Led by the clergy of Sune, Sharess, and Lliira, the Grand Revel is a day of dancing, music, and the consumption of sweet treats of all kinds, from chocolate to red firemint candies."

- **Campaign calendar, Midsummer:** `/home/user/waterdeep/campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:46` names Midsummer in the festival-day row for Flamerule ("| Flamerule | Summertide | Midsummer (between Flamerule 30 and Eleasis 1), then Shieldmeet in leap years | |"). It does not name Milil or the Grand Revel.

- **Campaign, Grand Revel:** none. My Grep of `campaign/` for "Grand Revel" and "Milil" returned only the staff row above.

### Field 7: Conflicts and what was not found

- **Grand Revel.** FRHoF says "Each year on {@book Midsummer|FRHoF|2|Midsummer}, priests of Milil hold a holiday called the Grand Revel." (`/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/milil/5etools.md:10`). The published adventure says "Led by the clergy of Sune, Sharess, and Lliira, the Grand Revel is a day of dancing" and dates it Alturiak 14 (`/home/user/waterdeep/sources/adventure-wdh.json:31363` and `:31367`). FRHoF is the higher-ranked source for Milil's holiday. The adventure's festival names no Milil, so no file reconciles the two.
- **Worshipers.** FRHoF says "- worshipers: Bards, orators, poets, singers" (`5etools.md:4`). The wiki's 5e field says "| worshipers5e        = Bards, troubadours, entertainers" (`wiki.txt:38`). FRHoF is the higher-ranked source.
- **Not found:** a ward, street or address for the Temple of Milil in Waterdeep; any Milil Chosen, Harmonious Order, Sharptongue or tuneservant in `campaign/`; any Milil line in `sources/adventure-wdh.json` (the Grand Revel lines name Sune, not Milil); any Milil line in `sources/adventure-wdmm.json`.

---

## 5. Tempus

### Answers

- **Q1 (temples or shrines in Waterdeep):** The House of Heroes, in the Sea Ward, "the largest temple in the city". The Sea Ward text is `/home/user/waterdeep/sources/adventure-wdh.json:30879` (quoted in Field 6). The table rows are `:30977-30981`. The campaign does not name it.
- **Q2 (campaign NPC, faction or quest):** None named. The only campaign line that names Tempus is a gazetteer note listing the wiki's city-wide faiths (`/home/user/waterdeep/campaign/gazetteer/waterdeep/castle-ward.md:31`, quoted in Field 6). It is not an NPC, faction or quest. No Stormknife, Red Knight or Tempus faction appears in `campaign/` (Grep).
- **Q3 (wiki lines that mention Waterdeep):** None. The Tempus wiki page has no Waterdeep line. This matters for castle-ward.md:31 (see Field 7).

### Field 1: Identity

> "## Tempus | source FRHoF p.124 | pantheon Faerûnian
> - altNames: ['The Foehammer', 'The Lord of Battles']
> - title: God of war
> - worshipers: Fighters, mercenaries, warriors
> - plane: Limbo"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/5etools.md:1-5` (FRHoF p.124)

> "## Tempus | source SCAG p.21 | pantheon Faerûnian
> - altNames: ['The Foehammer', 'The Lord of Battles']
> - title: God of war
> - alignment: ['N']
> - domains: ['War']
> - symbol: Upright flaming sword"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/5etools.md:28-33` (SCAG p.21)

> "| alignment5e         = Neutral"
> "| domains5e           = War domain|War"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/wiki.txt:35` and `:42` (5e; brackets removed)

> "| alignment3e         = Chaotic neutral"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/wiki.txt:65` (3e; the 2e field at line 82 says the same)

> "| homeplane5eR        = Limbo"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/wiki.txt:22` (5eR)

### Field 2: Edict or core tenet

> "Over the centuries, Tempus's priests have spread and enforced a common code that encourages rules of war, respect for reputation, and professional behavior on the battlefield. This code, called Tempus's Honor, encourages conflicts to be brief, decisive, and as safe as possible for bystanders. The rules in the code include the following: arm anyone who has need of a weapon, disparage no foe, acquit yourself with bravery, train all for battle, and don't engage in feuds. Those who poison wells, taint fields, kill noncombatants, or engage in torture in the name of war are considered enemies."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/5etools.md:10` (FRHoF p.124)

> "This god of war is random in his favors, meaning his chaotic nature favors all sides equally. Tempus might be an army's ally one day and its enemy the next. When he manifests before a battle, he can appear to either side in the conflict. If he rides Veiros, his white mare, the army will succeed. If he rides Deiros, his black stallion, defeat is certain. Most often, he rides with one foot in each mount's stirrup, signifying the unpredictable nature of battle."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/5etools.md:8` (FRHoF p.124)

> "Tempus's favor might be randomly distributed, but over the centuries his priests have made an effort to spread and enforce a common code of warfare - to make war a thing of rules, respect for reputations, and professional behavior. This code, called Tempus's Honor, has the purpose of making conflicts brief, decisive, and as safe as possible for those not directly involved. The rules in the code include the following: arm anyone who has need of a weapon; disparage no foe; acquit oneself with bravery; train all for battle; and don't engage in feuds. Those who poison wells, taint fields, kill noncombatants, or engage in torture in the name of war are all considered sinners."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/5etools.md:36` (SCAG p.21)

> "Tempus' orders to all combatants were simple and direct:
> # Be fearless
> # Never turn away from a fight.
> # Obey the rules of war.<ref name="FRPG">{{Cite book/Forgotten Realms Player's Guide|153}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/wiki.txt:176-179` (the wiki's Dogma list; cites Forgotten Realms Player's Guide 153, which the wiki gives with no edition label on this section)

### Field 3: Portfolio and Areas of Concern

> "Tempus is a war god concerned with brave conduct, using force to settle disputes, and encouraging bloodshed. The Foehammer is friendly with Gond for his war machines and was once Beshaba's lover. Tempus sponsored the Red Knight's ascension to divinity."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/5etools.md:7` (FRHoF p.124)

> "| portfolio5eR        = War"
> "| portfolio5e         = War"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/wiki.txt:26` and `:41`

> "| portfolio3e         = Battle, War, Warriors"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/wiki.txt:71` (3e; brackets removed)

> "| portfolio2e         = Battle, war, warriors"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/wiki.txt:88` (2e)

Areas of Concern: no bundle file has the field. Not found.

### Field 4: Worship (clergy, holy days, temples, omens, messengers)

> "Worshipers of Tempus are a legion, and soldiers carry his name in their hearts. His priests are tacticians skilled in the art of war. Many of his priests serve as battlefield chaplains with armies and mercenary companies, encouraging fellow soldiers with word and blade. Priests of Tempus teach that war conducted properly is fair because it impacts all sides equally, with each soldier poised for both death and glory. Mortals shouldn't fear war but should see it as a natural force—the storm that civilization brings about by its existence."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/5etools.md:11` (FRHoF p.124; clergy)

> "Temples to the Lord of Battle looked more like military fortresses than the archetypal temple. They featured barracks, mess halls, armories, and training grounds.<ref name="FPp71" />"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/wiki.txt:153` (cites Faiths and Pantheons 71)

> ";Order of the Broken Blade: The Order of the Broken Blade honored those warriors and clergy who could no longer fight at their best. They continued to serve Tempus by working at shrines and temples.<ref name="FPp71" />"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/wiki.txt:162` (the next line, 163, gives the Order of the Steel Fang; both cite Faiths and Pantheons 71)

> "The Chosen of Tempus are masterful tacticians, fearsome warriors, and powerful leaders. They find their way to battlefields with such certainty that many suspect the Chosen's presence causes battles to break out."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/5etools.md:12` (FRHoF p.124)

> "In such visions, Tempus is a powerfully built warrior dressed for battle in the style of those who see him. When he speaks to mortals directly, his voice reverberates in a clash of weapons, or he sends a Celestial {@creature Berserker|XMM} to carry his will."
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/5etools.md:9` (FRHoF p.124; messengers)

Holy days: the wiki's holy-day fields are blank (`wiki.txt:31` 5eR, `:45` 5e, `:61` 4e, `:77` 3e, `:92` 2e, `:105` 1e). Mounts (Veiros, Deiros) are in Field 2.

### Field 5: Relations with other powers and origin (edition as tagged)

> "| servedby4e          = Beshaba (intermediate deity|god)<br/>Garagos (exarch)<br/>Red Knight|The Red Knight (exarch)<br/>Uthgar (exarch)<br/>Valkur (exarch)"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/wiki.txt:55` (4e; brackets removed; the refs at line 63 cite Dragon 378 p.32 and Forgotten Realms Campaign Guide 80-81)

> "The Foehammer did have a friendly relationship with Gond for his war machines<ref name="FRCS3e-p242">{{Cite book/Forgotten Realms Campaign Setting 3rd edition|242}}</ref> a casual friendship with Nobanion,<ref name="FRCS3e-p252" /> and had a lover in Beshaba.<ref name="FRCG-p65">{{Cite book/Forgotten Realms Campaign Guide|65}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/wiki.txt:135` (the same line opens with "Tempus was quiet and solitary towards the other gods of the Faerunian pantheon.")

> "It was Tempus who sponsored the ascension of the Red Knight, he who encouraged her worship, and only he who knew her true name. She looked to him as a father figure<ref name="PP-44">{{Cite book/Powers & Pantheons|44}}</ref> and their relationship was akin to that of a fond and protective father with a brilliant daughter that worked hard and successfully in the family business, namely war.<ref name="F&A-p158" /> The two spent a great amount of time together, mostly looking into the battles of Faerun past and present, but they also simply hunted or shared stories in his feasting hall.<ref name="PP-44" />"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/wiki.txt:137`

> "Sune considered him a foe for his destruction of beautiful things, but besides her very nature making it hard for others to stay mad at her for long, he considered her flighty and irrelevant, not worth getting into active conflict with or even harboring a mutual dislike.<ref name="FRCS3e-p251">{{Cite book/Forgotten Realms Campaign Setting 3rd edition|251}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/wiki.txt:142` (sentence; the paragraph opens "Strangely for a god of war, Tempus had very few actual enemies," and the Eldath and Garagos paragraphs follow in the same section)

> "The one being that deemed Tempus an enemy that he actually acknowledged was Garagos. Once the primary war god of West Faerûn, the young demigod Tempus managed to defeat him, purportedly winning a century long battle by using his own berserker fury against him, and taking the position of the god of war as the spoils from their duel. The Blood-Reaver's loss to Tempus had only shortened his fuse, and his new incarnation possessed none of his former craftiness or mercy. While Garagos still harbored deep resentment towards Tempus unless his destructive abilities could someday surpass his tactical weakness, he would suffer if they someday met on the battlefield.<ref name="PP-44">{{Cite book/Powers & Pantheons|44}}</ref><ref name="FAP-p95">{{Cite book/Faiths and Pantheons|95}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/wiki.txt:144` (cites Powers & Pantheons 44 and Faiths and Pantheons 95)

> "Tempus was originally one of many potential war gods who emerged from the primordial clashes between Selûne and Shar. These gods fought constantly with each other, the victors absorbing the essence and power of the defeated. This continued until Tempus stood as the sole god of war in the Faerûnian pantheon, having defeated and absorbed all of his competitors (with the notable exception of Garagos, whom he defeated but spared).<ref name="FPp71" /> The barbarians of Icewind Dale claimed that Tempus' original name was "Tempos".<ref>{{Cite game/Icewind Dale}}</ref>"
> — `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/tempus/wiki.txt:186` (cites Faiths and Pantheons 71)

Note: the 4e servedby line (`wiki.txt:55`) gives five names, one of them the Red Knight, and "Uthgar" and "Valkur" as exarchs. The Uthgar and Valkur allied-gods paragraph at `wiki.txt:139` also names both as allies. The line is `> "Tempus was the only ally of Uthgar, deity of the Uthgardt barbarians of the Sword Coast North and had sponsored his divinity as well, having admired his fighting spirit."` (not in the six-quote list).

### Field 6: Campaign and published-adventure mentions

- **Campaign (gazetteer, Castle Ward):**
> "- **Religion:** Temple of the Seldarine (all elven gods), Spires of the Morning (Lathander), Font of Knowledge (Oghma), Halls of Justice (Tyr). The wiki also lists the House of Two Hands, which no campaign page uses. Tymora's Tower of Luck is listed here by one Waterdeep Dragon Heist table and placed in the Sea Ward elsewhere, and the wiki's Castle Ward list names neither it nor a Temple of Helm. The wiki's city-wide faiths are Deneir, Mystra, Oghma and Tempus. See the temples bullets under Culture in Life in the Ward. No dominant faith is sourced for the ward. [research]"
> — `/home/user/waterdeep/campaign/gazetteer/waterdeep/castle-ward.md:31`

- **Campaign, Plowing and Running** (the Field of Triumph line; it names the arena, not a temple):
> "- Plowing and Running (Mirtul 6 to 9) sends ward races through the Castle Ward streets before the finals at the Field of Triumph."
> — `/home/user/waterdeep/campaign/gazetteer/waterdeep/castle-ward.md:196`

- **Published adventure, Sea Ward text** (`/home/user/waterdeep/sources/adventure-wdh.json:30879`):
> "Must-see locations in the Sea Ward begin, of course, with the Field of Triumph, but just across the street is the no less remarkable House of Heroes-the largest temple in the city. Dedicated to Tempus, its many grand halls celebrate the city's champions of both battle and sport. The winners of ward competitions are paraded here after their victories, often carried on shoulders or passed from hand to hand over the heads of a crowd. It is a sight you shouldn't miss."

- **Published adventure, "Major Temples of Waterdeep" table** (`/home/user/waterdeep/sources/adventure-wdh.json:30978-30980`; the row's bracket lines are 30977 and 30981):
> "Tempus",
> "House of Heroes",
> "Sea Ward"

- **Published adventure, statue** (`/home/user/waterdeep/sources/adventure-wdh.json:31229`):
> "It now bows low toward the House of Heroes on bended knee-a gesture of obeisance to the city, and an acknowledgment of the sacrifice of all who fought for the city in that war."
> (rest of the paragraph covers the walking statue's history and its reshaping by Khelben Blackstaff after the 1370 DR sahuagin invasion)

- **Published adventure, Mirtul 6–9: The Plowing and Running** (`/home/user/waterdeep/sources/adventure-wdh.json:31410` gives the entry name "Mirtul 6–9: The Plowing and Running"; the quote is from the entry's first paragraph at `:31414`):
> "Who knows? Your name or visage might soon have a place in the House of Heroes."
> (sentence; the paragraph describes ward races whose winners compete at the Field of Triumph)

- **Campaign, House of Heroes:** none. My Grep of `campaign/` for "House of Heroes" and "Heroes' Garden" returned no line.
- **Campaign, Tempus named anywhere else:** none. My Grep of `campaign/` for "Tempus", "Foehammer", "Lord of Battles", "Tempos", "Stormknife", "Tempuran" and "Warrior's Rest" returned only `castle-ward.md:31`.

**Campaign lines about the Field of Triumph (requested in full).** The brief asks for every campaign line about the House of Heroes or the Field of Triumph. The House of Heroes has no campaign line. Below is every campaign line that names the Field of Triumph, grouped by file, with its line number. Each quote is either the whole line or the sentence that names the arena, copied from tool output.

*Trollskull Alley and related:*

- `/home/user/waterdeep/campaign/quests/act-i/trollskull-alley/overview.md:13`: "> Combat is limited; the quest's friction is social, economic, and bureaucratic. Lif's Stage 3 is the only mandatory fight, and it resolves short of a kill. The Field of Triumph (ev-05) is a gladiatorial set-piece under nonlethal rules."
- `overview.md:20`: "> - **The Field of Triumph** Event (ev-05): 1 Milestone Point — tournament completed; renovation nearly funded"
- `overview.md:43`: "- **Meloon Wardragon** (Force Grey) — leads the opposing team in the Field of Triumph final round; met as himself here; load-bearing for Force Grey Mission 3"
- `overview.md:56`: "**Field of Triumph:** Nonlethal gladiatorial combat across four rounds. Final round opponent is Meloon Wardragon's Force Grey team. No permanent consequences; the combat rules the arena enforces make this safe by design."
- `overview.md:64`: "A carnival captain named Zardoz Zord invited them to fight in his sponsored gladiatorial slots at the Field of Triumph. They met Meloon Wardragon in the final round, who shook their hands afterward and asked their names. The Grand Opening filled the house — and Ammalia Cassalanter stayed two hours, learned everyone's name, and left with the social grace that makes a room feel larger after she's gone."
- `/home/user/waterdeep/campaign/quests/act-i/trollskull-alley/ev-01-welcome-to-trollskull-alley.md:12`: "> - Lif's appeasement condition is behavioral: it runs through **The Field of Triumph** Event before resolving at the Grand Opening"
- `/home/user/waterdeep/campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:128`: "> The renovation is still running. Faction missions are now available. The Field of Triumph invitation arrives from the Sea Maidens Faire. Proceed to **The Field of Triumph** Event."
- `/home/user/waterdeep/campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:97`: "> Completing this Event awards 1 Milestone Point. This is likely to advance the party to Level 3 if they have completed Finding Floon, **The Factions Come Calling** Event, and **The Field of Triumph** Event."
- `/home/user/waterdeep/campaign/quests/act-i/trollskull-alley/ev-05-the-field-of-triumph.md:1`: "# The Field of Triumph"
- `ev-05-the-field-of-triumph.md:19`: "An invitation arrives from the Sea Maidens Faire, a carnival flotilla docked in Waterdeep Harbor. **Zardoz Zord**, the Faire's flamboyant Illuskan captain, has reserved gladiatorial entry slots at the Field of Triumph. Entry is free; Zord's sponsorship fee pays out regardless of outcome; prize purses are awarded per round. The invitation is addressed to the party by name."
- `ev-05-the-field-of-triumph.md:23`: "The Field of Triumph's standard gladiatorial format: a free-for-all qualification round, then a four-team bracket. Nonlethal rules throughout; participants yield, they do not die. The party competes as a team."
- `ev-05-the-field-of-triumph.md:55`: "Award **Meloon Met (Field of Triumph)** attunement."
- `ev-05-the-field-of-triumph.md:103`: "> The renovation continues. The tournament winnings have closed most of the financing gap. The party is now known at the Field of Triumph, which means they are known across the Sea Ward and by every faction with Noble connections. Proceed to **The Grand Opening** Event."
- `ev-05-the-field-of-triumph.md:105`: "> #### Milestone: The Field of Triumph"
- `ev-05-the-field-of-triumph.md:111`: "Zardoz Zord invited the party to fight in his sponsored gladiatorial slots at the Field of Triumph. Four rounds of nonlethal combat. The final round put them across the sand from Meloon Wardragon, who shook their hands afterward and asked their names. Xanathar's Guild was watching."
- `ev-05-the-field-of-triumph.md:115`: "> The Field of Triumph holds three thousand people when it's full. The sand is raked between bouts. A man in an extraordinary hat watches from the Faire's reserved box and claps after every exchange — not the crowd's rhythm, his own. The team across the sand from you in the final round is led by a man who smiles when the fight is hardest. He learns your names before you leave."
- `ev-05-the-field-of-triumph.md:119`: "The party competed in Zardoz Zord's sponsored gladiatorial slots at the Field of Triumph, met Meloon Wardragon in the final round, and received an unsolicited contact from Xanathar's Guild. The prize purses helped close the renovation gap. The tournament is done; the Grand Opening is next."
- `/home/user/waterdeep/campaign/quests/act-i/trollskull-alley/flowchart.md:16`: "[ev-05] The Field of Triumph        ←── Occurs during renovation; before opening"
- `flowchart.md:35`: "**The Field of Triumph occurs during the renovation period, before opening.** The invitation arrives after faction enrollment, while the party still has time before opening. Zord's timing is deliberate — he wants to see them before the tavern is successful."
- `flowchart.md:84`: "| Meloon Met (Field of Triumph) | ev-05 | Force Grey Mission 3 |"
- `/home/user/waterdeep/campaign/quests/act-i/trollskull-alley/design-notes.md:5`: " **The Field of Triumph** slots into the renovation period: the party is recruited, fighting in the city's arena, and hiring staff all in the same stretch of time."
- `design-notes.md:33`: "## The Field of Triumph and Meloon Wardragon"
- `design-notes.md:35` (two sentences from one line):
  - "The Field of Triumph places Meloon Wardragon in front of the party as himself: direct, skilled, warm, genuinely likeable."
  - "Parties who fight Meloon at the Field of Triumph and then encounter him again in Mission 3 will remember him as the man who shook their hands and asked their names."

*Structure documents (superseded or retired; quoted for completeness):*

- `/home/user/waterdeep/campaign/structure/arc-b-trollskull-alley.md:27`: "Between the renovation costs, the guild fees, and the neighbor who keeps filing complaints about rats, the city shows the party exactly what it costs to put down roots. Before the tavern opens, an invitation from the Sea Maidens Faire draws them to the Field of Triumph, where a carnival master named Zardoz Zord watches from a private box and Meloon Wardragon leads the opposing team in the final round. The arc's emotional high point is the Grand Opening — a full house, a poltergeist who has extended professional courtesy to the new owners, and an Ammalia Cassalanter attending as a generous patron, curious and charming and already counting the days to Founders' Day. The Twin Parades follow not long after, where something mechanical walks in one of the processions without explanation."
- `arc-b-trollskull-alley.md:155`: "### Scene 5: The Field of Triumph"
- `arc-b-trollskull-alley.md:161`: "*The Tournament Invitation.* An invitation arrives from the Sea Maidens Faire, a carnival flotilla docked in Waterdeep Harbor. Zardoz Zord, the Faire's flamboyant Illuskan captain, has reserved gladiatorial entry slots at the Field of Triumph and wants sponsored combatants. Entry is free; the prize is 50 gp per combatant plus whatever reputation accrues from public performance. The invitation is addressed to the party by name."
- `arc-b-trollskull-alley.md:163`: "*Tournament Structure.* The Field of Triumph's standard gladiatorial format: a free-for-all qualification round, then a four-team bracket. Nonlethal rules throughout — participants yield, they do not die. The party competes as a team; Zord's sponsorship fee covers their entry and pays out regardless of outcome. Arena purses are awarded per round for winning teams:"
- `arc-b-trollskull-alley.md:282`: "1. **Seven scenes confirmed.** Four core (Arrival, Guild Gauntlet, Neighbors, Factions) plus Field of Triumph before the Grand Opening, then Grand Opening as culmination, then Twin Parades as coda. Justified by 3–5 session runtime and the broader content scope of this arc."
- `arc-b-trollskull-alley.md:288`: "4. **Field of Triumph as Scene 5, placed before the Grand Opening.** The party fights in the city before they have a tavern to be proud of — the tournament win (or close loss) is part of what makes opening night feel earned. Meloon is met as himself here; Force Grey Mission 3 brings him back changed."
- `arc-b-trollskull-alley.md:298`: "9. **Sandbox scene ordering.** Scenes 1–3 are sequential (the party must arrive, deal with guilds, and meet neighbors before factions can recruit them). Scene 4 overlaps the renovation period (faction invitations arrive while the renovation runs; so does the Field of Triumph invitation). Scene 5 (Field of Triumph) occurs during the renovation period, before opening. Scene 6 (Grand Opening) is the renovation's culmination. Scene 7 (Twin Parades) is a scheduled city event following the opening."
- `arc-b-trollskull-alley.md:327`: "***Seven Scenes for an Episodic Arc.*** Arc A has four scenes because Arc A is a linear investigation — it flows from clue to clue, from the surface to the sewers, and ends when Floon is found. Arc B is structurally different: the party has a home base, multiple concurrent obligations, and no investigation to follow. The seven-scene structure imposes narrative progression on open-ended content without prescribing player choices. Scenes 1–3 run sequentially because the party cannot receive faction invitations before they have somewhere to receive them. Scene 4 overlaps the renovation period with faction recruitment running parallel to neighbor introductions. Scene 5 (Field of Triumph) slots into the renovation period — the party is recruited, fighting in the city's arena, and hiring staff all in the same stretch of time. Scene 6 (Grand Opening) is the renovation's endpoint and the arc's emotional culmination. Scene 7 (Twin Parades) is the city's calendar, not the party's — it falls when it falls. The DM runs Arc B as weeks of parallel activity, with these scenes as waypoints rather than a script."
- `arc-b-trollskull-alley.md:355`: "## The Field of Triumph and Meloon Wardragon"
- `arc-b-trollskull-alley.md:357`: "***Meeting Meloon Before He's Gone.*** The Field of Triumph places Meloon Wardragon in front of the party as himself: direct, skilled, warm, genuinely likeable. He leads the opposing team in the final round, gives them a real fight, and congratulates them afterward regardless of outcome. This is the party's only opportunity to know Meloon before Force Grey Mission 3 reveals what happened to him — the intellect devourer takes hold after Arc C, not before. The design depends on the sequence: the encounter works as foreshadowing only because it comes before the corruption. Parties who fight Meloon at the Field of Triumph and then encounter him again in Mission 3 will remember him as the man who shook their hands and asked their names — and that memory is what makes Mission 3 matter."
- `/home/user/waterdeep/campaign/structure/arc-g-cassalanter-villa.md:395`: "*Founders' Day Clock.* This quest consumes 1–2 tendays total: several days of intelligence gathering and casing (Scenes 1–3), 1–3 days for the operation and escape (Scenes 4–5), and 2–4 days of recovery and debrief (Scene 6). Update the campaign calendar. The GM communicates the advancing deadline through environmental detail: Founders' Day preparations visible across the city, Cassalanter-funded pavilions being erected in the Field of Triumph, festival decorations going up in every ward, and — if the party has Cassalanter contacts — increasingly strained behavior from Ammalia."
- `/home/user/waterdeep/campaign/structure/arc-c-fireball.md:168`: "A party that attended the Field of Triumph (Arc B Scene 5) recognizes him from the private box." (sentence)
- `/home/user/waterdeep/campaign/structure/ch2-city-of-splendors.md:35`: "- **Sea Ward** (wealthy northwest): noble estates, major temples, the Field of Triumph; Cassalanter Villa is here" (retired file)
- `/home/user/waterdeep/campaign/setting/waterdeep-lore.md:15`: "- **Sea Ward** (wealthy northwest): noble estates, major temples, the Field of Triumph; Cassalanter Villa is here"

*Quests (faction events and other):*

- `/home/user/waterdeep/campaign/quests/act-ii/fireball/ev-04-the-sea-maidens-faire.md:34`: "A party that attended the Field of Triumph (Trollskull Alley) recognizes the private-box figure."
- `/home/user/waterdeep/campaign/quests/faction-events/emerald-enclave/r03-summerstrider/ev-01-summerstrider.md:33`: "> - The network is made of ordinary people: gardeners in the City of the Dead, park wardens near the Field of Triumph and two fisherfolk on the south quay. They do not know they report to a druid, and they tell Melannor what they notice."
- `ev-01-summerstrider.md:197`: "> > "They are gardeners in the City of the Dead, park wardens near the Field of Triumph and two fisherfolk on the south quay. They send me what they notice, and I pass it to you."
- `/home/user/waterdeep/campaign/quests/faction-events/bregan-daerthe/s03-dinner-with-zardoz/design-notes.md:5`: " That was wrong, because the party has seen him at the Twin Parades, may have sat in his box at the Field of Triumph, and may have stood in his office during **Fireball!**."
- `/home/user/waterdeep/campaign/quests/faction-events/bregan-daerthe/s03-dinner-with-zardoz/ev-01-dinner-with-zardoz.md:8`: "> - Dine in the captain's dining cabin with Zardoz, who has already met the party at the Twin Parades and possibly at the Field of Triumph or in his office."
- `ev-01-dinner-with-zardoz.md:28`: "> - The party has seen him before. Most of them saw him wave from the lead float at the Twin Parades, and many met him at the Field of Triumph in **Trollskull Alley** or in his office during **Fireball!**. Nothing in this Event treats the dinner as a first meeting."
- `ev-01-dinner-with-zardoz.md:145`: "If the party competed at the Field of Triumph during **Trollskull Alley**, and did not visit the ship during **Fireball!**, read or paraphrase the following instead:"
- `ev-01-dinner-with-zardoz.md:151`: "> > You're the ones from the Field of Triumph! I watched all four rounds from my box with a bucket of fried fish, and I haven't been so happy since I won back my second-best hat. I sent you sealed notes between bouts, remember, and you were far too polite to ask who was paying."
- `/home/user/waterdeep/campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/design-notes.md:22`: "- The Twin Parades text says the fleet docks on Ches 21, but the Field of Triumph text says it is already docked, so this Event runs from whenever the fleet docks until Tarsakh 20."
- `/home/user/waterdeep/campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/overview.md:21`: "After the Field of Triumph, an Occupying Devourer from Nihiloor's brood took his skull, about three tendays before the watch begins." (sentence)
- `overview.md:35`: "On Day 5 the party can sit with the hosted Meloon. He asks twice as many questions as he answers, never touches his ale, never swears, and gives sewer directions that end at a Guild post. A character who met him at the Field of Triumph hears the difference at once."
- `/home/user/waterdeep/campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/ev-01-the-tenday-watch.md:18`: "> - An Occupying Devourer took Meloon's skull after the Field of Triumph, about three tendays before Day 1. It keeps his brain alive. Meloon is aware and cannot act, speak or cast."
- `/home/user/waterdeep/campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/design-notes.md:15`: "The guide's CR 10 stat block, its 120-foot telepathy, its Wish cure and its Field of Triumph possession were all rejected." (sentence)
- `/home/user/waterdeep/campaign/guides/gm-guide/running-the-villains.md:25`: "Nevercott in Trollskull Alley and Zardoz Zord at the Field of Triumph — and his villain escalation keys off the **Jarlaxle Informed** flag set during **Fireball!**, which records only that the party made contact with him." (sentence fragment; the line begins earlier and the start is not quoted)

*Setting and history:*

- `/home/user/waterdeep/campaign/setting/notable-figures/independents-allies/05-meloon-wardragon.md:7`: "> - **Affiliation:** Force Grey (occupied by a Xanathar's Guild intellect devourer after the Field of Triumph, about three tendays before the first day of the watch)"
- `05-meloon-wardragon.md:22`: "**Persona.** To the world, Meloon Wardragon is a barrel-chested warrior who enters every room at full volume — laugh, handshake, Azuredge at his hip and demonstrated on request. He fills taverns with warmth and expects nothing back for it. To those he trusts, he is the friend who shows up unprompted, who rescued Vajra alongside Renaer without being asked and never mentioned it again, who carries quiet grief for colleagues he has outlived. Deep down, Nihiloor's intellect devourer has marked him as a target precisely because he is trusted, well-connected, and constitutionally unable to believe that a friend's body could be used against him. The devourer occupies him after the Field of Triumph, about three tendays before the first day of the watch, and it keeps his brain alive and reads it. It has taken him into the lair twice by then. The wrongness is harder to name than to describe: the third person, the implausible Azuredge excuses, the drinks he never used to order, the directions through the sewers that lead straight into Xanathar patrols."
- `05-meloon-wardragon.md:26`: "**Relationships.** Meloon is an active member of Force Grey (reporting to Vajra Safahr, whose life he saved more than a decade ago alongside Renaer), the closest friend of Renaer Neverember (whose growing unease, without knowing why, becomes alarm once the occupation takes hold), a Yawning Portal regular whose surface thoughts Bonnie reads as comprehensibly normal until the occupation, and, after the Field of Triumph, a host for Nihiloor's intellect devourer, which reports to the Guild through a courier because telepathy reaches only 60 feet."
- `/home/user/waterdeep/campaign/setting/history/08-the-players-arrive.md:133`: "> - **Settled by the user (Session 47):** Faire arrival. The carnival fleet and parades arrive on Ches 21 (`trollskull-alley/ev-07-the-twin-parades.md` lines 11 and 26; `waterdeep-lore.md` line 44), and the *Scarlet Marpenoth* has been moored in the harbor all year. `ev-05-the-field-of-triumph.md` line 19 (Zord sponsoring Field of Triumph slots before Ches 20) and the ledger (Jarlaxle selling from Marpenoth 1491) show Jarlaxle's own presence, not the fleet's. The Alexandrian file `9.` (p.69), with an arrival parade on Ches 10, is overruled."
- `08-the-players-arrive.md:143`: "> - **Conflicts:** Meloon Wardragon's meeting "after the Field of Triumph" against the published adventure's "several months ago" (line 1548). Taken from the findings note and not rechecked."
- `/home/user/waterdeep/campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:90`: "- **Customs.** The Field of Triumph hosts illusory displays that chronicle Waterdeep's history, and the City Guard gives martial exhibitions. Festhalls hold costume contests for the best recreation of a historical figure. Several mages veil Castle Waterdeep as Nimoar's ancient log fortress from midday to sunset. The veiling was once banned as frivolous and has been reinstated."
- `09-timekeeping-and-the-festival-calendar.md:104`: "| Mirtul 6 to 9 | The Plowing and Running | Races are run in each ward and the ward winners meet at the Field of Triumph. |"
- `09-timekeeping-and-the-festival-calendar.md:117`: "- **Waukeentide.** Goldenight and Guildsmeet put crowds in the Cynosure and the Field of Triumph, and the Cassalanters host their own events. Any surveillance of the villa during these days has cover."
- `09-timekeeping-and-the-festival-calendar.md:126`: "Fleetswake honors the sea in the last tenday of Ches, Waukeentide fills the first tenday of Tarsakh with trade and galas, and on Founders' Day, the first of Flamerule, the Field of Triumph stages illusory histories of the city while Castle Waterdeep is veiled as the log fortress of Nimoar." (sentence from the Overview paragraph)

Grep of `campaign/` for "Field of Triumph" lists 25 files; every file is quoted above.

### Field 7: Conflicts and what was not found

- **Worshipers.** FRHoF says "- worshipers: Fighters, mercenaries, warriors" (`5etools.md:4`). The wiki's 5eR field says "| worshipers5eR       = Fighters, mercenaries, warriors" (`wiki.txt:28`), and its 5e field says "| worshipers5e        = Soldiers" (`wiki.txt:43`). FRHoF is the higher-ranked source.
- **Alignment.** SCAG says "- alignment: ['N']" (`5etools.md:31`). The same SCAG entry says: "The god of war is random in his favors, meaning that his chaotic nature favors all sides equally." (`5etools.md:35`). The bundle does not resolve this. The wiki's 3e and 2e fields say Chaotic neutral (`wiki.txt:65` and `:82`).
- **Waterdeep faiths.** The campaign says "The wiki's city-wide faiths are Deneir, Mystra, Oghma and Tempus." (`castle-ward.md:31`). The Tempus wiki page in this bundle has no Waterdeep line (Grep of `wiki.txt`). The source of that list is not in this bundle.
- **Not found:** a Tempus NPC, faction or quest in `campaign/`; a Stormknife or Tempus's Honor reference in `campaign/`; a Tempus holy day in any edition (blank in `wiki.txt:31`, `:45`, `:61`, `:77`, `:92`, `:105`); any Tempus line in `sources/adventure-wdmm.json`; any House of Heroes line in `campaign/`.

---

## Cross-references (other file:line hits on these topics)

- `/home/user/waterdeep/campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:43` — "| Tarsakh | The Claw of Storms | Greengrass (between Tarsakh 30 and Mirtul 1) | |" (Greengrass; the wiki gives Greengrass as a Sune holy day at `wiki.txt:79` and `:93`; the calendar does not name Sune)
- `09-timekeeping-and-the-festival-calendar.md:45` — "| Kythorn | The Time of Flowers | | Summer solstice, Kythorn 20 |" (summer solstice; the wiki gives Amaunator's 2e holy day as "Third full moon of the year, summer solstice" at `wiki.txt:91`; the calendar does not name Amaunator)
- `09-timekeeping-and-the-festival-calendar.md:46` — "| Flamerule | Summertide | Midsummer (between Flamerule 30 and Eleasis 1), then Shieldmeet in leap years | |" (Midsummer; the FRHoF Milil holy day is at `5etools.md:10`; the calendar does not name Milil)
- `09-timekeeping-and-the-festival-calendar.md:103` — "| Tarsakh 30 and Mirtul 1 | Greengrass | The festival day that marks the official start of spring. Wealthier people give flowers to the less wealthy. |" (Greengrass, see line 43)
- `/home/user/waterdeep/sources/adventure-wdh.json:30910` — "caption": "Major Temples of Waterdeep" (table caption; the Sune and Tempus rows are quoted in Sune Field 6 and Tempus Field 6)
- `/home/user/waterdeep/sources/adventure-wdh.json:30692` — "The City of the Dead lies opposite the northern ridge of Mount Waterdeep, which descends down to the Field of Triumph, the city's great coliseum." (sentence)
- `/home/user/waterdeep/sources/adventure-wdh.json:30722` — "Be warned that when the demand for drays is high-during rain or snow, or to get to or from an event at the Field of Triumph-conditions become crowded and perfect for pickpockets." (sentence)
- `/home/user/waterdeep/sources/adventure-wdh.json:30798` — "They spend coin to fund celebrations, contests at the Field of Triumph, upkeep at the city's temples and shrines, civic projects, guild events, and charitable actions such as burial of the unknown dead." (sentence)
- `/home/user/waterdeep/sources/adventure-wdh.json:30878` — "There's a persistent but patently false legend that the famous Lion Gate at the Field of Triumph is the gaping maw of a sea lion." (sentence)
- `/home/user/waterdeep/sources/adventure-wdh.json:31158` — "Public facilities for those out and about can be found all around the Market and the Field of Triumph, and near the largest city squares." (sentence)
- `/home/user/waterdeep/sources/adventure-wdh.json:31414` — "Foot, horse, and chariot races are run through courses in each ward, and the winners from each ward compete at the Field of Triumph." (sentence; the entry is "Mirtul 6–9: The Plowing and Running", line 31410)
- `/home/user/waterdeep/sources/adventure-wdh.json:31451` — "The Field of Triumph is the site of illusory displays that chronicle the history of Waterdeep, as well as martial exhibitions by the Guard and other worthies." (sentence)
- `/home/user/waterdeep/sources/adventure-wdh.json:31488` — "The most anticipated part of the day is when horses are cleared from the Field of Triumph and the surrounding streets so that the Griffon Cavalry can perform aerial displays over the crowds in the stadium." (sentence)
- `/home/user/waterdeep/sources/adventure-wdh.json:31405` — "These gatherings culminate in a gala festival and dance sponsored by several guilds, which lasts from dusk till dawn and overruns the Market, the Cynosure, the Field of Triumph, and all areas in between." (sentence from the Waukeentide paragraph; the Leiruin entry is quoted in Leira Field 6)
- `/home/user/waterdeep/campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:111` — quoted in Leira Field 6 (Liar's Night)

## Not found (summary)

- **Amaunator:** Waterdeep temple or shrine; campaign NPC, faction or quest (terms searched in `campaign/`: "Amaunator", "Keeper of the Eternal Sun", "Yellow God", "Eternal Sun", "Light of the Law", "Keeper of Law"); any published-adventure line (terms searched in `sources/adventure-wdh.json` and `sources/adventure-wdmm.json`, the same terms); Areas of Concern; edict list; 5e holy days.
- **Sune:** campaign mention (terms searched in `campaign/`: "Sune", "Sunite", "Lady Firehair", "Lady of Love", "Princess of Passion", "Temple of Beauty", "Ruby Rose", "Sodality", "Hopeful"); any Sunite NPC from the wiki (`wiki.txt:178-181`) in `campaign/`; Areas of Concern; Sune line in `sources/adventure-wdmm.json`.
- **Leira:** Waterdeep temple; campaign NPC, faction or quest (terms searched in `campaign/`: "Leira", "Leiran", "Lady of Mists", "Mistshadow", "Lady of Deception", "Mistcaller", "Mistwalker", "Courts of Illusion"); Leira Chosen; Leira line in `sources/adventure-wdmm.json`; Areas of Concern.
- **Milil:** ward or address of the Temple of Milil; Milil Chosen; Harmonious Order; Sharptongue; Milil line in `sources/adventure-wdh.json` (terms searched: "Milil", "Lord of Song", "Lord of All Songs", "Grand Revel", "tuneservant", "Sharptongue", "Harmonious Order") and in `sources/adventure-wdmm.json`; Areas of Concern.
- **Tempus:** House of Heroes line in `campaign/` (terms searched: "House of Heroes", "Heroes' Garden"); Tempus NPC, faction or quest in `campaign/` (terms searched: "Tempus", "Foehammer", "Lord of Battles", "Tempos", "Stormknife", "Tempuran", "Warrior's Rest", "Red Knight", "Garagos", "Valkur", "Uthgar", "Blood-Reaver"); Tempus holy day; Tempus line in `sources/adventure-wdmm.json`; Areas of Concern.

## Not readable

None. All bundle files and every campaign file named above were opened. Not opened by instruction: the Alexandrian PDFs, `sources/SOURCE_GUIDE.md`, the `.docx` files and the `docs/` research notes.
