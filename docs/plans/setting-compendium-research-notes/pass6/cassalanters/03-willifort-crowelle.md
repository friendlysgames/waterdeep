# Pass 6 research notes: Willifort Crowelle

Page: `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Faction page: `campaign/setting/organizations/10-cassalanters.md`
Villains page: `campaign/setting/villains/cassalanters.md`
Voice profile: `.claude/skills/character-voices/voices/cassalanters.md` (heading `### Willifort Crowelle`, lines 49-63)
Model: `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md`

Ruling used: Ches 1, 1492 DR. Willifort is the Cassalanters' chief butler, Victoro's personal attendant and a full cult member, present in the villa. Everything that happens to him in a heist, a chase, a hostile-mode attempt, combat or an Event Outcome is quest time (section C).

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output.
- Published adventure: `sources/adventure-wdh.json`. Tags such as `{@creature ...}` are left as written. JSON escapes (`\"`) are shown as plain quotes. Lines that Grep returned as "[Omitted long matching line]" were re-read by line offset, so each adventure quote is the full line.
- Wiki: the scratchpad extraction at `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-cassalanters/03-willifort-crowelle.txt`. Citations below write it as `wiki:NN`. The wiki prints no edition on most lines. Editions are marked inferred where the citation key shows one.
- Cassalanter wiki copy in the repo: `sources/research/pass4-bundles/cassalanters/wiki.txt`.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. Every PDF quote below is a transcription from the rendered page image and must be checked with `pdftotext -layout` before any prose use. Each is cited as the printed page with the PDF page in brackets.
- Appendix B and Appendix C: no match for `Willifort`, `Crowelle` or `butler` (Grep over `sources/*.md`). Appendix D has a Willifort section (quest time, section C).
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written.

---

## A. Background facts by theme

### A1. Origin, kind and birth

No source gives Willifort's birth, origin, home before the villa, or how he came to be a doppelganger. The sources give only the kind and the guise.

**Kind and guise (adventure, 5e):**
> "Willifort dresses in a sharp black suit and wears thin-rimmed spectacles. He's a {@creature doppelganger} that usually takes the form of an aging male tiefling, and he greets all guests in the entrance hall ({@area C1|2ee})."
> — `sources/adventure-wdh.json:18481` (Head Servants, "Willifort Crowelle", page 116, id `2dd`; the name entry is at `:18476`-`:18477`)

**Kind and guise (Alexandrian, printed p.53 [PDF p.5]; image transcription):**
> "WILLIFORT CROWELLE: “Willifort” is supposedly the elderly tiefling valet of the Cassalanters. In truth he is a doppelganger and their most trusted lieutenant."
> — `sources/6. Faction Response Teams.pdf`, printed p.53 [PDF p.5]

**Kind and guise (wiki, lead line; citation key "WDH5e-p122", 5e):**
> "'''Willifort Crowelle''' was the [[doppelganger]] butler of the [[Cassalanter|Cassalanter family]] in the late–15{{th}} century [[DR]].<ref name="WDH5e-p122" />"
> — `wiki:62`

**Kind and guise (campaign, NF page, Persona):**
> "To those he trusts, he is a doppelganger who has served the Cassalanters long enough that the role has become his identity."
> — `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:21`

### A2. Household role, rank and standing

**Chief butler and personal attendant (adventure, 5e; page 116):**
> "As the Cassalanters' chief butler and Lord Victoro's personal attendant, {@creature Willifort Crowelle|WDH} makes a point of knowing everything that transpires within the villa. If the Cassalanters have guests, he escorts them during their entire visit, using stealth if necessary. He ushers nosy guests away from areas or objects that might link the Cassalanters with the Asmodeus-worshiping cult."
> — `sources/adventure-wdh.json:18482`

**Keys (adventure, 5e):**
> "Doors are made of exotic hardwood. If a door is locked, the lock can be picked by a character who makes a successful {@dc 15} Dexterity check using thieves' tools, or the door can be forced open by a character who makes a successful {@dc 20} Strength (Athletics) check. Victoro, Ammalia, and the head butler, Willifort, hold keys to every room in the house."
> — `sources/adventure-wdh.json:18614`

**Personal attendants are kept on (adventure, 5e):**
> "Cassalanter Villa is home to no one but Lord and Lady Cassalanter, their children, their personal attendants, and their guards. All the other servants who work at the villa live in dingy homes in the Dock Ward or the Field Ward and travel across the city in the wee hours of the morning to arrive before the Cassalanters awake."
> — `sources/adventure-wdh.json:18597`
>
> "With the exception of their personal attendants, the Cassalanters replenish their servants regularly. Most move on to other jobs, but occasionally a servant discovers the secret vault ({@area C29|330}), visits the forbidden attic ({@area C24|325}), or otherwise learns too much. Such folk are fated to become sacrifices to Asmodeus."
> — `sources/adventure-wdh.json:18598`

**Valet to Victoro (wiki, citation key "WDH5e-p116", 5e):**
> "As butler and personal valet of Lord [[Victoro Cassalanter]], Willifort was usually at the side of his master. He always want knew all that happened inside the mansion and survey all the guests in order to hide connection with Asmodeus' cult.<ref name="WDH5e-p116">{{Cite book/Waterdeep: Dragon Heist|116}}</ref>"
> — `wiki:65` (the wiki's own typo "always want knew" is kept here; do not copy it into prose)

**Tenure (campaign, arc-g structure doc; the only tenure figure in any source; tagged by the author):**
> "*Willifort's Surveillance.* The villa's defining social challenge. Willifort Crowelle is a doppelganger who has served the Cassalanter household for eight years [research]. He greets every visitor at C1, offers drinks, positions himself outside doors, and uses detect thoughts continuously on anyone inside the villa."
> — `campaign/structure/arc-g-cassalanter-villa.md:83`

**Command line (campaign, org page; Structure, "Chain of command"):**
> "- **Chain of command:** Ammalia makes the final calls for the family and the cult, and Victoro, who leads the worship, has stopped questioning her. Willifort Crowelle links the family to everyone who works for it. He runs household security, reports to Ammalia and directs the spy and the poisoner. Seffia Naelryke commands the field team and answers to Victoro, and the head servants keep order at the rites."
> — `campaign/setting/organizations/10-cassalanters.md:51`

> "> - **Chain of command:** Ammalia makes the final calls and Victoro has stopped questioning this. Willifort Crowelle reports to Ammalia on everything that happens in the villa. Seffia Naelryke's response team answers to Lord Cassalanter, and Rella Asp and Ivrala Sorn report to Willifort."
> — `campaign/setting/organizations/10-cassalanters.md:117` (GM Notes)

> "- **Keep the Temple Hidden:** An illegal temple to Asmodeus lies beneath the villa, and discovery of it is a capital offense under the Code Legal once a magistrate has ruled it unlawful, and it ruins the plan. Willifort Crowelle manages household security. Devil worship alone is not illegal in Waterdeep, so what the family guards is the temple and what is done in it (*Dragon Heist*, 5e; **Asmodeus** in Deities). ..."
> — `campaign/setting/organizations/10-cassalanters.md:39` (rest of the bullet covers the published adventure's protection line and the City Watch)

> "- **Intelligence:** Willifort makes a point of knowing everything that happens in the villa, and he escorts every guest for the whole visit and steers nosy ones away from anything that could link the family to the cult (*Dragon Heist*, 5e). ..."
> — `campaign/setting/organizations/10-cassalanters.md:66` (rest of the bullet covers Ammalia's ravens, Rella and Ivrala, and the wiki's rumor-mongering line)

> "- **Pressure before force:** The published adventure says the family tries to misdirect and discredit its opponents and not to murder them (*Dragon Heist*, 5e). The family uses the city's own leverage first, in the form of Watch complaints, noble pressure and guild sanctions, and infernal force comes last (**The Cassalanters** in Villains). Willifort is the exception to that restraint, and he burns bridges, gathers intelligence and, when necessary, solves problems permanently (**Willifort Crowelle**)."
> — `campaign/setting/organizations/10-cassalanters.md:68`

**Staff and the villain page:**
> "- Willifort Crowelle, the doppelganger butler, knows everything that happens in the villa and reports to Ammalia. He runs household security and is the family's most dangerous weapon."
> — `campaign/setting/villains/cassalanters.md:64`

**Who he reports to (NF Relationships, day-one):**
> "**Relationships.** Willifort is the chief butler and Lord Victoro's personal attendant, a doppelganger who holds keys to every room alongside Victoro and Ammalia, and the Cassalanters' intelligence operative who reports to Ammalia on everything that transpires within the villa."
> — `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:25`

**Reports from Rella and Ivrala (campaign, Trollskull staff guide; the drop location is in conflict, see D8):**
> "| 3 | **Ivrala Sorn** | NE Chondathan human | ... | Cassalanter social operative. Reports floor-level patron intelligence monthly to Willifort Crowelle via Dock Ward tobacconist drop. ..."
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:56` (rest of the row covers her hiring, pay and Fame)

**Other staff who know him (arc-g, structure doc; Maesta, non-cult housekeeper):**
> "- **Maesta** (housekeeper, human female, 50s) — manages the non-cult staff. Professional, discreet, loyal to the household's reputation rather than to the Cassalanters personally. Knows the staff schedules, which rooms are restricted, and that Willifort is \"more than he appears\" — she has seen him change the shape of his hands when he thought no one was looking. If told the truth: her first concern is the staff's safety, her second is the children, her third is whether the party can keep this quiet."
> — `campaign/structure/arc-g-cassalanter-villa.md:111`

### A3. Cult membership and faith

**Full member (wiki, citation key "WDH5e-p122", 5e):**
> "He was a full member of the cult of [[Asmodeus]].<ref name="WDH5e-p122">{{Cite book/Waterdeep: Dragon Heist|122}}</ref>"
> — `wiki:67`

**Patron deity (wiki infobox, 5e p.122):**
> "| patron deity   = [[Asmodeus]]<ref name="WDH5e-p122" />"
> — `wiki:18`

**Head servants are cult members (adventure, 5e; page 116):**
> "The head servants of Cassalanter Villa are members of the cult. These four servants are described below. All appear to be tieflings, though one is not. The following changes apply to the tieflings' stat blocks:"
> — `sources/adventure-wdh.json:18467`

**Cult regalia (adventure, 5e; page 122):**
> "{@creature Willifort Crowelle|WDH} and {@creature Tissina Khyret|wdh} keep their cult regalia (see \"Cult of Asmodeus\"), in a gold-embellished lockbox hidden under a stack of quilts bearing images of flying devils. The box can be unlocked with either Willifort's or Tissina's golden key, or by a character who succeeds on a {@dc 14} Dexterity check using thieves' tools. It can also be pried open with a successful {@dc 16} Strength (Athletics) check."
> — `sources/adventure-wdh.json:20540` (room entry "Lockbox", page 122; the header is at `:20536`-`:20537`)

**Cult gathering stations (adventure, 5e; page 129):**
> "If the cult is here in force, thirty human {@creature cultist||cultists} stand in neat rows before the statue, chanting to Asmodeus with wooden goblets in hand while their leader, {@creature Victoro Cassalanter|WDH} (see {@adventure appendix B|WDH|12}), tosses offerings into the bowl. Roughly half of the cultists are members of the nobility; the rest are Waterdavian rabble brought into the cult to fill out the ranks. Standing around the perimeter are {@creature Willifort Crowelle|WDH}, {@creature Tissina Khyret|wdh}, {@creature Laiba \"Nana\" Rosse|wdh|Laiba Rosse}, and {@creature Jandar Chergoba|wdh} (see \"Head Servants\"). Their job is to make sure the other cultists behave themselves while {@creature Ammalia Cassalanter|WDH} (see {@adventure appendix B|WDH|12}) walks gracefully through the crowd with a golden decanter, ceremonially pouring wine into the cultists' goblets for toasting to the Lord of the Nine Hells."
> — `sources/adventure-wdh.json:22818` (Special Events, "Cult Gathering", page 129, id `346`)

**Campaign, cult roster (org page; "The cult"):**
> "- **The cult:** Victoro leads it, and the whole cult gathers in the temple at midnight on the first day of every tenday. About thirty members attend when it meets in force, roughly half of them nobles and the rest Waterdhavian commoners (*Dragon Heist*, 5e). Willifort, Tissina Khyret, Nana Rosse and Jandar Chergoba keep order at the rites while Ammalia pours the wine. ..."
> — `campaign/setting/organizations/10-cassalanters.md:50` (rest of the bullet covers the cult's reach into House Gralhund)

> "- **Household staff:** The villa employs sixteen named staff, and ten of them know nothing about the temple (`arc-g-cassalanter-villa.md` line 91). The six cult members are Willifort the butler, Tissina Khyret the attendant, Nana Rosse the twins' caretaker, Jandar Chergoba the head chef, and the field pair Seffia Naelryke and Arn Xalrondar. ..."
> — `campaign/setting/organizations/10-cassalanters.md:52` (rest of the bullet covers the non-cult staff)

**Campaign, the Cassalanter structure doc (cult role and devotion):**
> "The household holds six souls who know what lies beneath. Willifort Crowelle, doppelganger, serves Asmodeus with genuine devotion — the family is secondary. Tissina Khyret, Ammalia's attendant, is a cult fanatic who joined out of loyalty to Ammalia personally — she does not know the contract's full terms. ..."
> — `campaign/structure/arc-g-cassalanter-villa.md:21` (rest of the paragraph covers the other five cult staff)

> "- **Willifort Crowelle** (doppelganger, butler) — serves Asmodeus directly. True believer. Will not break under any social pressure; he would die before revealing the temple. If the Cassalanters are exposed as cultists, Willifort drops his tiefling disguise and fights."
> — `campaign/structure/arc-g-cassalanter-villa.md:95` (Cult Staff list, in "Questioning Staff")

**Who keeps the secret (campaign, org page; GM Notes):**
> "> - **Who suspects:** Everybody is suspicious of the Cassalanters because they are too nice to be this rich and this purebred, and nobody outside the household and the cult knows they are infernalists."
> — `campaign/setting/organizations/10-cassalanters.md:118`

**Not in the faith-road list (campaign, org page "Service Is Worship"; Willifort is absent from it):**
> "- **Service Is Worship:** The cult's members fold devotion into the work they do for the family. Tissina Khyret attends Ammalia, Nana Rosse minds the twins, Jandar Chergoba cooks and Seffia Naelryke runs field operations, and none of them sees a conflict between the job and the god. They came to the faith by different roads: Tissina out of loyalty to Ammalia, Nana Rosse to stay close to the twins, and Jandar through a debt to Victoro that became cult service (`arc-g-cassalanter-villa.md` lines 96-98)."
> — `campaign/setting/organizations/10-cassalanters.md:40`

### A4. Ties to named figures

**Victoro (campaign, Victoro NF page, Relationships):**
> "**Relationships.** Victoro is the husband of Ammalia Cassalanter (co-conspirator), the father of Osvaldo (eldest, soul lost, transformed into a chain devil), Terenzio and Elzerina (the twins, forfeit on their ninth birthday), and the employer of Willifort Crowelle (doppelganger butler who knows everything that happens in the villa)."
> — `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:26`

**Osvaldo (campaign, org Secret callout):**
> "> - **Osvaldo:** The eldest son's soul was claimed first, when he was nine, the age at which the contract claims each child, and he is now twelve and a chain devil held in the soundproofed attic of the villa, room C24, never the basement or the temple. Ammalia visits weekly, sitting in the room outside the pentagram to read to him while he curses her and weeps. Victoro has not visited in months. Willifort knows. Two imps are always present. Terenzio and Elzerina have been told Osvaldo is at school. ..."
> — `campaign/setting/organizations/10-cassalanters.md:129` (rest of the bullet covers the twins' fate and the wiki source)

> "Osvaldo's transformation was immediate. ... Only Willifort Crowelle — the doppelganger butler who serves Asmodeus directly — knows what is behind the door."
> — `campaign/structure/arc-g-cassalanter-villa.md:13` (the paragraph's middle sentences cover the transformation, the wards and the imps)

**Ammalia:** the reporting line is quoted in A2 (`campaign/setting/organizations/10-cassalanters.md:51`, `:117`). No separate personal tie is sourced.

**Tissina, shared lockbox (campaign, Tissina NF page, Relationships):**
> "**Relationships.** Tissina is Ammalia Cassalanter's personal tiefling attendant, a cult fanatic whose regalia is stored alongside Willifort Crowelle's in a shared lockbox, and the first cultist in the villa to notice an infiltration."
> — `campaign/setting/notable-figures/cassalanters/07-tissina-khyret.md:25`

**Seffia (campaign, Seffia NF page):**
> "- **Willifort Crowelle:** The family's other field operative. His methods are blunt where hers are precise, and the two combine in hostile mode. Unresolved: nothing says who leads when they work together."
> — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:35`

**Rella Asp and Ivrala Sorn (campaign, NF pages):**
> "**Relationships.** Rella Asp is a Cassalanter operative placed as a Trollskull Manor Master Cook candidate, a poisoner whose commission to poison a bonded NPC activates in Act III, an intelligence collector reporting to Willifort Crowelle, and a staff candidate in the **Trollskull Manor** guide."
> — `campaign/setting/notable-figures/cassalanters/12-rella-asp.md:25`

> "**Relationships.** Ivrala is a Cassalanter intelligence operative placed as a Trollskull Manor server candidate, a person reporting to Willifort Crowelle on patron activity, recognizable to Sister Valdra on a DC 13 Perception check when both are present, and a staff candidate in the **Trollskull Manor** guide."
> — `campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md:25`

**Hadra Stonebread, the former household employee (campaign, NF page; Hadra is an independent ally):**
> "**Relationships.** Hadra is a former household employee of the Cassalanters (twelve years), a woman who knows Willifort Crowelle on sight and avoids his sight in return, and a Trollskull Manor staff candidate whose interview reveals the cost of working for wealthy people with secrets."
> — `campaign/setting/notable-figures/independents-allies/15-hadra-stonebread.md:25`

> "Deep down, she knows Willifort Crowelle noticed the day she left, and she does not know how long the Cassalanters will allow a witness to walk free."
> — `campaign/setting/notable-figures/independents-allies/15-hadra-stonebread.md:21`

**Jarlaxle and Vessa (campaign, org page; the one outsider who knows the pact; no Willifort tie in the file):**
> "> - **The one exception:** Jarlaxle knows about the pact through **Vessa**, his doppelganger spy in the Cassalanter social circle. He never tells Bregan D'aerthe members unless they work it out themselves."
> — `campaign/setting/organizations/10-cassalanters.md:122`

**Caladorn:** no Willifort tie in any file.

### A5. Signature belongings, habits and manner

- Sharp black suit and thin-rimmed spectacles: `sources/adventure-wdh.json:18481`; NF page `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:29` ("an aging tiefling in a sharp black suit and thin-rimmed spectacles").
- Golden key to the cult lockbox: `sources/adventure-wdh.json:20540` (A3).
- Keys to every room: `sources/adventure-wdh.json:18614` (A2).
- Detect thoughts, active from the moment a guest crosses the threshold: `campaign/locations/cassalanter-villa/01-entrance-hall.md:7` ("His *Detect Thoughts* is active from the moment a guest crosses the threshold, reading surface thoughts automatically without requiring concentration."). This is a normal-operations description (see C3).
- Spectacles and redirection (voice profile, Quirks): `.claude/skills/character-voices/voices/cassalanters.md:57` ("He anticipates requests before they're made. He adjusts his spectacles before a redirection.").
- Hand habit: `campaign/structure/arc-g-cassalanter-villa.md:111` (A2).

### A6. Time in post and age

- Tenure: "for eight years [research]" (`campaign/structure/arc-g-cassalanter-villa.md:83`, A2). The `[research]` tag is the author's. The published adventure gives no tenure. The bundle copy at `sources/research/pass4-bundles/cassalanters/campaign-hits.txt:1005` shows the same sentence **without** the tag (section E1).
- Age: none. The adventure says "aging male tiefling" (`sources/adventure-wdh.json:18481`). The org page says "Presents as an elderly tiefling" (`campaign/setting/organizations/10-cassalanters.md:95`). The wiki gives no age. The NF Overview calls him "an aging tiefling" (`campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:29`).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, current page: "*Doppelganger butler, neutral, he/him*. Stat block: **Doppelganger**." — `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:5`
- Campaign, org page: "- **Willifort Crowelle** — Doppelganger butler, neutral. The Cassalanters' doppelganger valet. Presents as an elderly tiefling. Their most trusted operative and most dangerous weapon. Uses disguise to burn bridges, gather intelligence, and when necessary, solve problems permanently. See the **Willifort Crowelle** page in Notable Figures." — `campaign/setting/organizations/10-cassalanters.md:95`
- Campaign, Factions Guide: no alignment. "\"Willifort Crowelle\" (**Doppelganger**) + 1 **Bearded Devil** (or 2 **Cultist Fanatics**) + 3 **Cultists**. Deployed for operations requiring deception, assassination, or escalation." — `campaign/guides/factions/11-cassalanters.md:19`
- Adventure: no alignment is given for Willifort. The only alignment line in the Head Servants passage is "The tieflings are lawful evil." (`sources/adventure-wdh.json:18471`). See D1.
- Wiki: the alignment fields are empty. `wiki:54` reads `| alignment4e    = ` and `wiki:57` reads `| alignment5e    = `.
- Alexandrian: no alignment for Willifort in the Response Teams, Lair or Outposts PDFs read.

**Species**
- Campaign, current page: "Doppelganger butler" (`campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:5`), with the tiefling guise in Persona (`:21`: "To the world, Willifort is an aging male tiefling").
- Campaign, org page: "Doppelganger butler" (`campaign/setting/organizations/10-cassalanters.md:95`).
- Adventure: "He's a {@creature doppelganger} that usually takes the form of an aging male tiefling" (`sources/adventure-wdh.json:18481`).
- Wiki: "| race           = [[Doppelganger]] posing as [[tiefling]]<ref name="WDH5e-p122" />" — `wiki:14`.
- Alexandrian, printed p.53 [PDF p.5]: "In truth he is a doppelganger" (A1).
- Consistent across sources: the true species is doppelganger; tiefling is the guise.

**Pronouns**
- Campaign, current page: "he/him" (`campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:5`).
- Adventure: "He's a {@creature doppelganger}" and "he escorts them during their entire visit" (`sources/adventure-wdh.json:18481`, `:18482`).
- Wiki: "| sex            = Male" — `wiki:13`.

**Stat block**
- Campaign, current page: "Stat block: **Doppelganger**." (`campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:5`).
- Campaign, Factions Guide: "\"Willifort Crowelle\" (**Doppelganger**)" (`campaign/guides/factions/11-cassalanters.md:19`).
- Adventure: "He's a {@creature doppelganger}" (`sources/adventure-wdh.json:18481`). The Head Servants changes apply to the tieflings' stat blocks only (`:18471`).
- Alexandrian Lair, printed p.82 [PDF p.6]; image transcription: "Willifort Crowelle (Head Butler/Agent) – doppelganger, MM p. 82 (DH p. 116)" — `sources/10. Lair  Cassalanter Villa.pdf`.
- Alexandrian Response Teams, printed p.53 [PDF p.5]; image transcription: "“Willifort Crowelle” (doppelganger, MM p. 82)".
- Wiki: no stat block line in the infobox.

**Location and ward**
- Campaign, org page: "- **The villa:** Cassalanter Villa stands in the Sea Ward, where the wiki puts it on the southwest corner of Delzorin Street and Diamond Street (Forgotten Realms Wiki, *Cassalanter*, 3e)." — `campaign/setting/organizations/10-cassalanters.md:48` (the bullet's later sentences cover the building)
- Wiki: "| home           = [[Sea Ward of Waterdeep|Sea Ward]], [[Waterdeep]]" — `wiki:11`.
- Wiki occupation: "| occupation     = Butler" — `wiki:16`.

---

## C. Every sentence on the current page that narrates a quest-time event, a combat state or a day-one conflict

Current page: `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md`. "Day-one OK" means no quest gate is needed. Quest-time means the sentence describes a heist, a chase, a hostile-mode attempt, combat or an outcome.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Doppelganger butler, neutral, he/him*. Stat block: **Doppelganger**." | Day-one OK | org `:95`; adventure `:18481` |
| 2 | L6 | "**Affiliation:** The Cassalanters (household operative)" | Day-one OK | org `:95` ("The Cassalanters' doppelganger valet.") |
| 3 | L7 | "**Featured in:** Faction Outposts, Cassalanter Villa, Vault of Dragons, Cassalanter Villa (location)" | Reference list; "Cassalanter Villa" is listed twice. Quest refs: Faction Outposts `campaign/structure/arc-e-faction-outposts.md:355`; Cassalanter Villa `campaign/structure/arc-g-cassalanter-villa.md:83-95`; Vault of Dragons `campaign/structure/arc-j-vault-of-dragons.md:198-199`; location `campaign/locations/cassalanter-villa/01-entrance-hall.md:7` |
| 4 | L11 | "**Resonance.** Willifort should inspire surface comfort with his impeccable butler's manner, growing unease as the party realizes he knows too much, and visceral shock when his true nature is revealed." | Mixed. "impeccable butler's manner" is day-one (adventure `:18481`; org `:29`). "growing unease as the party realizes he knows too much" describes the party's discovery, which is quest time. "visceral shock when his true nature is revealed" is a reveal. The reveal is quest time: `campaign/structure/arc-g-cassalanter-villa.md:277` ("Willifort drops the tiefling disguise.") and `:95` ("If the Cassalanters are exposed as cultists, Willifort drops his tiefling disguise and fights."). Decide under ruling 3 (RP text verbatim, quest-time lines removed) |
| 5 | L13 | "**Emotions.** Willifort most often feels clinical detachment, possessive loyalty to the Cassalanters, controlled satisfaction in maintaining perfect cover, cold contempt for guests who are easy to deceive, and the alien patience of a creature that has been someone else for so long it has forgotten what it was." | Day-one RP text. "possessive loyalty to the Cassalanters" conflicts with the structure doc (D4). "controlled satisfaction in maintaining perfect cover" has no source beyond the disguise (adventure `:18481`) |
| 6 | L15 | "**Motivations.** Willifort wants to protect the Cassalanter family and their secrets, maintain his cover as an aging tiefling butler, and handle problems permanently when discretion fails." | Day-one RP text. "protect the Cassalanter family" conflicts with `arc-g:21` (D4). "handle problems permanently when discretion fails" matches org `:68` and Factions Guide `:15` |
| 7 | L17 | "**Inspirations.** When playing Willifort, channel Alfred Pennyworth (*Batman*), Mystique (*X-Men*), and Kato (*The Green Hornet*)." | Not a fact |
| 8 | L21 | "**Persona.** To the world, Willifort is an aging male tiefling in a sharp black suit and thin-rimmed spectacles who greets all guests and steers nosy ones away from cult business. To those he trusts, he is a doppelganger who has served the Cassalanters long enough that the role has become his identity. Deep down, he is the family's most trusted operative and most dangerous weapon, using disguise to burn bridges, gather intelligence, and solve problems permanently." | Day-one. Sources: adventure `:18481`, `:18482`; org `:68` ("burns bridges, gathers intelligence and, when necessary, solves problems permanently"). "most trusted operative" matches org `:95` |
| 9 | L23 (a) | "In a fight, Willifort orders imps and spined devils to attack while he secures the family's retreat." | Quest-time (combat). Adventure hire-coach encounter (ch. 6): `sources/adventure-wdh.json:7065` ("When he sees the characters, Willifort orders the imps and the spined devils to attack.") and `:7067` ("Willifort flees on foot if the hirecoach is destroyed or its horses are unable to move."). Spined devils conflict with org `:54` (D3) |
| 10 | L23 (b) | "If the party confronts him directly, he fights with a doppelganger's deceptive shapeshifting." | Quest-time (combat). Structure doc: `campaign/structure/arc-g-cassalanter-villa.md:247` ("In combat: drops the tiefling disguise, uses Multiattack, and attempts to flee through the service wing if reduced below 15 HP.") |
| 11 | L23 (c) | "His hostile-mode escalation: he attempts to assassinate Jarlaxle, fails, then targets the PCs in a follow-up." | Quest-time (hostile mode, gated by the party's refusal or threat). Routed: `campaign/guides/factions/11-cassalanters.md:11`; `campaign/guides/gm-guide/running-the-villains.md:76`; Alexandrian `6. Faction Response Teams.pdf` printed p.52; `campaign/structure/arc-e-faction-outposts.md:355`. Villains gate: `campaign/setting/villains/cassalanters.md:34` |
| 12 | L25 | "**Relationships.** Willifort is the chief butler and Lord Victoro's personal attendant, a doppelganger who holds keys to every room alongside Victoro and Ammalia, and the Cassalanters' intelligence operative who reports to Ammalia on everything that transpires within the villa." | Day-one OK. Sources: adventure `:18482`, `:18614`; org `:51`, `:117` |
| 13 | L29 | "Willifort Crowelle is the Cassalanter family's chief butler — an aging tiefling in a sharp black suit and thin-rimmed spectacles who greets every guest with impeccable courtesy and seems to know exactly what is needed before anyone asks." | Day-one OK. One sentence of 37 words (the brief's Overview limit is 21 words per sentence). Sources: adventure `:18481`, `:18482` |

### C2. Quest-time clauses in the voice profile

Profile: `.claude/skills/character-voices/voices/cassalanters.md` lines 49-63. Ruling 16 copies it into the NF page.

> "- **Sound:** A dry, precise, elderly voice, perfectly correct. Unmasked, flat and alien."
> — `.claude/skills/character-voices/voices/cassalanters.md:52` ("Unmasked" describes the cover broken. That is the Stage 4 state, `campaign/structure/arc-g-cassalanter-villa.md:277`.)

> "- **Word choice:** Service formality: \"sir\", \"madam\", \"if you would follow me\", \"the family\". Unmasked, cold and brief."
> — `.claude/skills/character-voices/voices/cassalanters.md:54`

> "- **Swearing:** *Never · Plain · n/a.* Not even unmasked. The creature underneath has no use for it."
> — `.claude/skills/character-voices/voices/cassalanters.md:55`

> "  - *Under pressure (unmasked):* \"You should not have come down here.\""
> — `.claude/skills/character-voices/voices/cassalanters.md:63` (the cover is broken only at Stage 4 or in combat, `arc-g:247` and `:277`)

Other profile lines carry no quest-time clause. The Never line ("He never breaks cover in public, never hurries, and never reveals the family's business.", line 59) is day-one. Ruling 16 requires the same day-one restatement as ruling 3 for lines 52, 54, 55 and 63, and the skill file's profile changes must be reported.

### C3. Quest-time clauses in other campaign files that touch Willifort

- Villa, the cover-breaking state: `campaign/structure/arc-g-cassalanter-villa.md:95`; `:247`; `:277` ("**Stage 4 — Exposed.** The party's true intentions are known. Guards mobilize. Willifort drops the tiefling disguise. ...").
- Social Exposure System, Stage 2: `:269` ("**Stage 2 — Noticed.** Willifort begins actively scanning the party — he positions himself within 30 feet and uses his action to probe deeper thoughts (DC 15 Wisdom saving throw).").
- Surveillance options: `:85` ("The party must address Willifort or accept that their surface thoughts are being monitored. Options: ... (b) identify Willifort as a threat and neutralize him — risky, because his absence triggers an immediate household response; Ammalia checks on him within 15 minutes; ...").
- Staff questioning trigger: `:115` ("... word reaches Maesta, who mentions it to Willifort as a professional concern (\"Guests are asking unusual questions about the household\"), advancing the Social Exposure System by one stage.").
- Heist windows: `:75` ("**Caravance (Tarsakh 1).** ... A skeleton crew remains: perimeter guards, Willifort, imp watchers on Osvaldo's door. ...") and `:259` ("40–60 civilian guests fill C1, C5 lower, C9, C13, C15, and C25. ... Willifort circulates with a tray. ...").
- Stage 1: `:265` ("Willifort monitors via detect thoughts but has not flagged anything.").
- Escalation table: `:174` ("| Unaware | No Cassalanter outposts hit | Standard roster. Staff relaxed. Willifort uses detect thoughts casually. Social entry straightforward. |") and `:175` ("| Suspicious | Converted Windmill hit | Imp surveillance doubled (12 imps, not 6). Willifort scans every visitor aggressively. ...").
- Outcome states (structure doc, not yet Event Outcome names): `:345` ("*Redeemed (contract destroyed).* ... Willifort: if he served Asmodeus directly (he did), he flees. He has no loyalty to a family that no longer serves his master.") and `:349` ("*Active / Adversarial.* ... Willifort's network may attempt to recover Eye #2. ..."). `:347` (Cooperative) and `:351` (Exposed) do not name him.
- Location journal: `campaign/locations/cassalanter-villa/01-entrance-hall.md:9` ("During Fireball (ev-06), the party arrives here by Ammalia's invitation. Willifort takes coats, offers wine, and escorts the party to C9 (dining room). He reads the party during this transit. The Social Exposure System begins at Stage 1."); `:15` ("During the Charity Ball or Goldenight gala, the entrance hall is filled with 40–60 guests. ... Willifort circulates with a tray, angling to position himself within 30 feet of the party. ..."); `:21` ("Doppelganger, tiefling disguise. Combat behavior: Multiattack in his natural form; flees through the service corridor if reduced below 15 HP. His absence triggers an immediate household response — Ammalia checks on him within 15 minutes of any gap in his presence."); `:23` ("During normal operations, Willifort reads surface thoughts passively. ...").
- Location overview: `campaign/locations/cassalanter-villa/area-overview.md:34` ("**Willifort Crowelle** (doppelganger, tiefling disguise): Circulates C1, C5 lower, and service corridors. *Detect Thoughts* active at all times within 30 feet. Does not engage combat unless cornered."); `:60`-`:63` (stage table: "| 3 | Suspected | Guards escort the party to Willifort; Victoro notified | Not possible |" and "| 4 | Exposed | Active confrontation; guards and Willifort converge | Not possible |"); `:89` ("- **Fireball dinner:** In C17 all evening and not seen. If the party asks, Willifort says what **The Cassalanter Dinner** gives him to say: ...").
- Reading room: `campaign/locations/cassalanter-villa/03-reading-room.md:9` ("During ev-06, if the party arrives early or is left briefly in a waiting area, they may be placed in the reading room. Willifort is not present; a servant offers wine and excuses himself.").
- Factions Guide: `campaign/guides/factions/11-cassalanters.md:9` ("Willifort keeps tabs on the characters from a distance, reporting to Ammalia, and the family's response apparatus holds."); `:11` ("Willifort attempts to assassinate Jarlaxle, fails, then targets the characters in a follow-up attempt. This may push Jarlaxle to propose an alliance against the Cassalanters."); `:71` ("| Suspicious | Imp surveillance from the Asmodean Shrine; Willifort tracks in disguise. Willifort gathers close intelligence on party identities and contacts. |"); `:72` ("| Alert | Seffia's team in passive mode; Seffia and Willifort combined in hostile mode. |"); `:73` ("| Lockdown | Bearded devil called up; Willifort targets a party ally to create leverage. ..."); `:75` ("Hostile mode skips directly to Willifort's full operation.").
- GM guide: `campaign/guides/gm-guide/running-the-villains.md:51` ("| **The Cassalanters** | Normal operations | Imp surveillance from the Asmodean Shrine; Willifort Crowelle tracks in disguise. ..."); `:61` ("**Cassalanters.** The Cassalanters operate in two modes. In passive mode they barely react; in hostile mode they skip straight to Willifort's full operation. The switch fires when the PCs refuse to help or are identified as a threat to the soul-pact plan."); `:76` ("| **Cassalanters vs. Bregan D'aerthe** | Surveillance — not yet conflict | ... If the Cassalanters turn hostile, Willifort attempts to assassinate Jarlaxle, fails, and that failure likely pushes Jarlaxle toward a PC alliance against the Cassalanters. | *Instructions from Lord Cassalanter* (Asmodean Shrine) |").
- Grand-game guide: `campaign/guides/gm-guide/grand-game-in-play.md:53` ("**The Cassalanters** are largely binary. ... The switch to hostile mode happens when the PCs are identified as a threat to the soul-pact plan, and they move directly to Willifort Crowelle's full operation. ...").
- Design notes: `campaign/guides/gm-guide/design-notes-running-the-campaign.md:25` ("... A party that does careful surveillance of Cassalanter Villa gets better entry options and intelligence on Willifort's detect thoughts range. ...").
- Lords' Alliance: `campaign/quests/faction-events/lords-alliance/r25-warduke/ev-01-warduke.md:200` ("| The Cassalanter household (unconfirmed, credible) | Second | A man who gives the name Willifort Crowelle, three hired hands in plain robes and one heavy escort | Willifort's crew |").
- Bregan D'aerthe, The Theater's Back Room: `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:337` ("> > \"Lathander keep me, is it done? You have it, don't you? Nobody followed? I've got to be back at the villa by eleven bells. Mr. Crowelle counts the household at the door. I couldn't explain myself if I were late.\"") and `:362` ("> > \"Because I'm frightened, sir. Since the piece in the newspaper, Mr. Crowelle has asked every servant who they speak to. The family dismisses whoever it can blame, and I'm the one who carries the baskets. If I'm to be blamed anyway, I'd like the three hundred gold, and a ship.\""). The quest's narrator also says (`:20`): "Brimel is not a man of conscience. After *The Waterdeep Wazoo* printed its piece and two \"solicitors\" called on the publisher, Lord Victoro's butler, Mr. Crowelle, began asking every servant who they speak to." (Brimel's narration in a quest file.)
- Trollskull calendar: `campaign/guides/trollskull-manor/06-tavern-time.md:33` ("| Kythorn 21–30, if **Cassalanter Villa** is not complete | Faction Contact (slot 17), Floon Blagmaar, Fala Lefaliir | 8: the Cassalanters (\"Willifort Crowelle\") | Ten days before Founders' Day, the Cassalanters check whether the party is still a threat. |").
- Open Lord's Watch: `campaign/guides/factions/12-open-lords-watch.md:96` ("- **A well-connected house.** The Watch cannot touch the Cassalanters without evidence. Willifort Crowelle can also arrange for a Cassalanter-connected Watch lieutenant to take a new interest in the party's tavern, and a Watch investigation there lowers Fame.").
- Vault of Dragons: `campaign/structure/arc-j-vault-of-dragons.md:198` ("| Cassalanters | Active-Adversarial | Willifort Crowelle (doppelganger, tiefling guise) leading cult fanatics and cultists | Seize the vault gold by force for the Asmodeus buy-out |") and `:199` ("| Cassalanters | Cooperative (Gold Delivered) | Willifort and a dozen carts of trusted servants, unarmed for combat | Collect the gold owed per the **Cassalanter Villa** agreement |").
- Faction Outposts: `campaign/structure/arc-e-faction-outposts.md:355` (C2 row 11 and E2).

### C4. Quest-time clauses in the published adventure (ch. 6 Stone-theft sequence and the house)

These describe a Stone-of-Golorr chase that no campaign file carries. Grep for `hire-coach`, `Street Chase` and `Cellar Complex` in `campaign/` returns only generic gazetteer or Gralhund hits. Read them as adventure-only quest material.

- Summary: "The spined devils deliver the stone to a hire-coach parked in an alley (encounter 1, \"Alley\"). Inside the coach is {@creature Victoro Cassalanter|WDH}'s valet, {@creature Willifort Crowelle|WDH}, a doppelganger in tiefling form. As the hire-coach flees, a street chase ensues (encounter 3, \"Street Chase\"). When a crowd cuts off his escape route, Willifort leaps out of the hire-coach and tries to lose himself in the crowd. In the confusion, street urchins snatch the stone. The characters catch up to the children in their cellar hideout (encounter 9, \"Cellar Complex\")." — `sources/adventure-wdh.json:6671`
- Hire-coach: "Lord Cassalanter's {@creature doppelganger} valet, in the guise of an elderly tiefling named {@creature Willifort Crowelle|WDH}, sits in the passenger cab, which grants {@quickref Cover||3||half cover}. Standing next to the hire-coach is a {@creature bearded devil} disguised as a cloaked human bodyguard wearing a wide-brimmed hat, and perched on the coach are three {@condition invisible} {@creature imp||imps}. Any {@creature spined devil||spined devils} that survived the previous encounter are also present, having just delivered the {@item Stone of Golorr|WDH} to Willifort." — `sources/adventure-wdh.json:7064`
- "When he sees the characters, Willifort orders the imps and the spined devils to attack. The bearded devil stays close to Willifort and engages any character who tries to reach the hire-coach." — `sources/adventure-wdh.json:7065`
- "If there's any chance that the characters might obtain the {@item Stone of Golorr|WDH} as the encounter progresses, Willifort orders the driver to move the hire-coach out of the alley as quickly as possible. If the driver is {@condition incapacitated} or killed, the bearded devil climbs into the driver's seat on the back of the coach and steers the vehicle. If the bearded devil is unable to replace the driver, the doppelganger takes the reins. Willifort flees on foot if the hirecoach is destroyed or its horses are unable to move." — `sources/adventure-wdh.json:7067`
- Escape: "If Willifort escapes and the characters pursue him, proceed with encounter 3, \"Street Chase.\"" — `sources/adventure-wdh.json:7076`
- Street chase: "The characters are pursuing Lord Cassalanter's doppelganger valet, Willifort, as he flees in a hire-coach or on foot. The chase takes place on crowded streets, in front of agog spectators." — `sources/adventure-wdh.json:7694`
- Crowd: "If Willifort flees in a hire-coach, his getaway is thwarted on the third round of the chase when a large crowd blocks the road, forcing the hire-coach to stop. (If the chase occurs on Founders' Day, the crowd is part of the holiday celebration.) The doppelganger jumps out of the hire-coach on his next turn and makes his way through the crowd on foot." — `sources/adventure-wdh.json:7702`
- Raven: "If Willifort is {@condition incapacitated}, a raven abruptly swoops down, acting next in the initiative count. It snatches the stone and flees with it. This raven is a shapechanged {@creature imp} that works for Lady Cassalanter." — `sources/adventure-wdh.json:7704`
- Intruders: "{@creature Victoro Cassalanter|WDH} reacts with fiery rage to the sight of uninvited guests. He demands to know their names and calls for the butler, {@creature Willifort Crowelle|WDH}, to show them out." — `sources/adventure-wdh.json:18364` (quest time; the intruders are the party)
- Conditional: "If the characters are expected guests, {@creature Willifort Crowelle|WDH} (see \"Head Servants,\") awaits them here and guides them to the smoking room ({@area C12|308}) to meet with Lord Cassalanter. He allows them to explore the house while they wait but follows them doggedly." — `sources/adventure-wdh.json:19988`
- Conditional: "If Lord Cassalanter has invited the characters to his home for any reason, he meets them here. If the conversation turns to business, he has Willifort bring his guests glasses of fine brandy and pipes filled with pipeweed." — `sources/adventure-wdh.json:20317`
- Villains' stance in the adventure: "If the Cassalanters are the villains, they send three {@creature cult fanatic||cult fanatics} and three {@creature cultist||cultists}. Victoro's {@creature doppelganger} manservant, {@creature Willifort Crowelle|WDH}, leads the group in his tiefling guise unless the characters killed him or otherwise disposed of him earlier in this chapter or in chapter 6." — `sources/adventure-wdh.json:14781`

### C5. Quest-time clauses in the Alexandrian PDFs and appendix (all image transcriptions)

- Lair, Event Schedule, printed p.79 [PDF p.3]: "The only people left in the Villa during this time, beyond the Cassalanters themselves, are:" then the bullet "Willifort Crowell" (the PDF spells it "Crowell" here; D7). `sources/10. Lair  Cassalanter Villa.pdf`.
- Lair, Adversary Rosters, printed p.81 [PDF p.5]: "Willifort Crowelle (75%) or Servant" (first line of the Cassalanter Villa roster).
- Lair, Questioning Staff, printed p.82 [PDF p.6]: "They once saw a number of people go down into the wine cellar. They waited around for twenty minutes before Willifort shoed them away, but nobody came back up."
- Outposts, Questioning Cultists, printed p.40 [PDF p.5]: "The fanatics will report that their contact there is Willifort Crowelle (which might lead the PCs to believe that the Cassalanters are unaware of what’s happening in their own home); the wizard knows better and may be made to reveal as much." — `sources/5. Faction Outposts.pdf`.
- Outposts, Instructions from Lord Cassalanter, printed p.40 [PDF p.5]: "(The note might mention the PCs by name here if they were the source of this intelligence; otherwise he names Willifort Crowelle.)" and the note itself: "“The imps should report back to me directly at the villa.”"
- Response Teams, printed p.52 [PDF p.4]: "If the PCs turn down the Cassalanters, then the whole shape of the campaign will shift:" followed by "Willifort Crowelle will attempt to assassinate Jarlaxle. He’ll fail, but a few days later he’ll target the PCs in a similar attempt. This may prompt Jarlaxle to reach out to the PCs and propose an alliance against the Cassalanters." — `sources/6. Faction Response Teams.pdf`.
- Appendix D (Running the Tavern), quest time: `sources/Appendix_D_-_Running_the_Tavern.md:1580` ("**Who comes:** \"Willifort Crowelle\" — in truth a doppelganger, the Cassalanters' most trusted lieutenant. He arrives in whatever identity is most useful: a friendly rival tavern-owner, a minor city functionary checking compliance paperwork, a Harper contact the characters haven't met before. He will not arrive as himself, because \"himself\" does not exist."); `:1588` ("A Cassalanter household operative placed as staff has been exposed — ... Either way, \"Willifort\" arrives to assess the damage."); `:1600` ("... Once that threshold is crossed, Willifort shifts from information-gathering to active interference: impersonating party members to damage faction relationships, or arranging for a Cassalanter-connected Watch lieutenant to take a new interest in the tavern's compliance record."); `:1602` ("**Fame Impact:** Willifort's visit causes no public Fame impact. ...").
- Appendix D, Ivrala's reporting, `:252`: "She reports in writing, monthly, to Willifort Crowelle, through a drop at a tobacconist on the High Road." (conflict, D8); `:256` ("Willifort Crowelle appears on this thread if the party is already investigating the Cassalanters.").

### C6. Founders' Day deadline: scheduled (day-one) against quest time

**Scheduled facts (campaign-start knowledge):**
- Org, Campaign role: "- **Campaign role:** Villain faction; racing to acquire the vault's gold before the twins' ninth birthday, Flamerule 11, when their soul pact with Asmodeus comes due; Founders' Day (Flamerule 1) is the date the family has chosen for its feast." — `campaign/setting/organizations/10-cassalanters.md:7`
- Org, Ches 1 bullet: "**Ches 1, 1492 DR, the campaign opens:** Osvaldo is in the attic, and the family holds Eye #2 and about 500,000 gp. ... On their ninth birthday, Flamerule 11, the pact comes due. Founders' Day falls ten days before, on Flamerule 1; that is when the Cassalanters plan to collect the ninety-nine souls." — `campaign/setting/organizations/10-cassalanters.md:30` (the middle sentences cover the Stone's placement and the Eyes)
- Org, Secret callout: "> - **The deadline:** The pact comes due on Flamerule 11, the twins' ninth birthday. Founders' Day on Flamerule 1 is the feast and Ammalia's real deadline. It is her operational window, chosen for the civic cover and for the time left to verify the terms, and it does not appear in the contract." — `campaign/setting/organizations/10-cassalanters.md:131`
- Villains, Core motive: "Victoro and Ammalia Cassalanter are loving parents and secret diabolists, ..." — `campaign/setting/villains/cassalanters.md:16` (the sentence that carries the date: "Their core motive is to free the twins before their ninth birthday on Flamerule 11. That means raising 999,999 gp from their own coffers and the Vault of Dragons, and poisoning ninety-nine guests at the Founders' Day feast.")
- Villains, operational window: "Founders' Day (Flamerule 1) is Ammalia's operational window, chosen for the civic cover and for the time left to verify the terms. The contract falls due on Flamerule 11, ten days after Founders' Day, and its terms do not mention the feast." — `campaign/setting/villains/cassalanters.md:29`
- Structure doc, quest opener: "The twins, Terenzio and Elzerina — souls forfeit on their ninth birthday, one tenday after Founders' Day." — `campaign/structure/arc-g-cassalanter-villa.md:9`
- Adventure (published, 5e): "Their two youngest children, Terenzio and Elzerina, are doomed to lose their souls when they turn nine years old a mere ten days after Founders' Day, a midsummer festival that celebrates Waterdeep's founding." — `sources/adventure-wdh.json:18294`
- Adventure, lemure outcome (conditional on the Stone): "If the Cassalanters fail to obtain the {@item Stone of Golorr|WDH}, the following events don't come to pass. As a consequence, Terenzio and Elzerina are transformed into {@creature lemure||lemures} as their souls are forfeit ten days after Founders' Day." — `sources/adventure-wdh.json:22888`

**Quest-time (the heist windows, the deadline gate and the schedule of the cult):**
- Caravance, skeleton crew including Willifort: `campaign/structure/arc-g-cassalanter-villa.md:75` (C3).
- Founders' Day as deadline: `campaign/structure/arc-g-cassalanter-villa.md:81` ("**Founders' Day (Flamerule 1).** Not a heist window. This is the deadline. The poisoning feast occupies the villa's lawn pavilions. ... If the party has not acted by this date, the sacrifice occurs.").
- Accelerated plan: `campaign/structure/arc-g-cassalanter-villa.md:349` ("The Founders' Day plan accelerates.").
- Trollskull, ten days before: `campaign/guides/trollskull-manor/06-tavern-time.md:33` (C3).

**Alexandrian dates that conflict with the campaign calendar (D6):**
- Lair, printed p.79 [PDF p.3] (image transcription): "TARSAHK 1st – CARAVANCE" (Caravance on Tarsakh 1); "TARSAHK 9th – LEIRUIN FEAST: This is the feast at which the Cassalanters poison 99 guests and perform the ritual necessary to save their children’s souls (assuming they’ve managed to secure the gold from the Vault)."; "TARSAKH 11th – THE TWINS’ BIRTHDAY: The twins’ ninth birthday, on which Asmodeus will claim their souls."
- Timelines addendum, printed p.225 [PDF p.1] (image transcription): "Cassalanter kids get their souls sucked to Hell on Tarsakh 11th." and "(with the sacrificial feast thrown by the Cassalanters being a Feast of Leiruin on Tarsakh 10th)" — `sources/29. Addendum Timelines  Starting the Campaign.pdf`.

**Gap for the drafter:** no source gives Willifort a role on Founders' Day itself. The adventure's Founders' Day entry (`sources/adventure-wdh.json:19991`, page 118) does not name him, and the campaign files give him no feast task. The feast is run by Ammalia and Jandar (Villains page; org `:131`).

---

## D. Conflicts

**D1. Alignment: neutral (campaign) against "lawful evil" (adventure, Head Servants)**
- Campaign, NF page: "*Doppelganger butler, neutral, he/him*." (`campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:5`)
- Campaign, org page: "- **Willifort Crowelle** — Doppelganger butler, neutral." (`campaign/setting/organizations/10-cassalanters.md:95`)
- Adventure: "All appear to be tieflings, though one is not. The following changes apply to the tieflings' stat blocks:" (`sources/adventure-wdh.json:18467`) and "The tieflings are lawful evil." (`:18471`). The adventure does not say which of the four head servants is not a tiefling. Willifort's own stat block is the doppelganger's, so the line may not reach him.
- Higher source: the campaign (neutral). The adventure line is about tieflings and may not apply.

**D2. Stone of Golorr against Eye #2 (the object Willifort recovers)**
- Wiki: "In [[1492 DR]],{{WDH-time}} the [[Cassalanter]] family may have managed to acquire the ''[[Stone of Golorr]]''. If so, Willifort, supported by some [[devil]]s, tried to stop some adventurers that wanted retrieve the stone from the Cassalanter mausoleum inside the [[City of the Dead (Waterdeep)|City of the Dead]]<ref name="WDH5e-p60">{{Cite book/Waterdeep: Dragon Heist|60}}</ref>. He later went back with the stone to the Cassalanter villa.<ref name="WDH5e-p62">{{Cite book/Waterdeep: Dragon Heist|62}}</ref>" — `wiki:70`
- The wiki's Cassalanter page says the same: "Later, Victoro sent his [[doppelganger]] valet [[Willifort Crowelle]] to recover the Stone and return with it to the Cassalanter villa.<ref name="WDH5e-p60-62">{{Cite book/Waterdeep: Dragon Heist|60-62}}</ref>" — `sources/research/pass4-bundles/cassalanters/wiki.txt:84`
- Adventure: "The spined devils deliver the stone to a hire-coach parked in an alley (encounter 1, \"Alley\"). Inside the coach is {@creature Victoro Cassalanter|WDH}'s valet, {@creature Willifort Crowelle|WDH}, a doppelganger in tiefling form." (`sources/adventure-wdh.json:6671`)
- Campaign: "Victoro sent Seffia Naelryke and Arn Xalrondar to take it and to silence three cult members who knew too much." and "Campaign change: the published adventure sends the pair after the Stone itself, and the campaign changes the object to Eye #2." — `campaign/setting/organizations/10-cassalanters.md:29`. Villains: "Eye #2 came to the Cassalanters through infernal divination, which found it in the Brandath Crypts, and their agents took it from Neverember's magical wards." (`campaign/setting/villains/cassalanters.md:32`).
- Alexandrian, printed p.77 [PDF p.1] (image transcription): "As Dragon Heist begins, the Cassalanters control one of the Eyes. (They stole it from the crypt of Lady Alethea Brandath, Renaer’s mother.)" — `sources/10. Lair  Cassalanter Villa.pdf`.
- Higher source: the campaign (Eye #2). The wiki's Stone line and the adventure's Stone chase are not used. The chase has no campaign carrier (C4).
- Location, same ruling: the wiki's "mausoleum inside the City of the Dead" matches the Brandath Mausoleum where the Eye was found (`campaign/structure/arc-g-cassalanter-villa.md:15`: "the crypt of Lady Alethea Brandath, Renaer's mother ... interred in the Brandath Mausoleum in the City of the Dead" is in the quest opener's Eye paragraph). The family crypt is beneath the villa (org `:49`, "The temple and the crypt: The temple lies below the wine cellar, ...").

**D3. Who commands spined devils: Willifort (NF Morale; adventure) against Seffia (campaign)**
- NF Morale: "In a fight, Willifort orders imps and spined devils to attack while he secures the family's retreat." (`campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:23`)
- Adventure: "When he sees the characters, Willifort orders the imps and the spined devils to attack." (`sources/adventure-wdh.json:7065`)
- Campaign, org page: "The cult also calls devils to its work. Seffia's team calls spined devils, and Willifort's team can call a bearded devil (**Seffia Naelryke**; **The Cassalanters** in the Factions Guide)." (`campaign/setting/organizations/10-cassalanters.md:54`)
- Campaign, Factions Guide: "**Seffia's Team.** Seffia Naelryke (**Cultist Fanatic**) + 2 **Spies** + 1 **Veteran** + 1 invisible **Imp**." (`campaign/guides/factions/11-cassalanters.md:17`, no spined devil) and "**Willifort's Team.** \"Willifort Crowelle\" (**Doppelganger**) + 1 **Bearded Devil** (or 2 **Cultist Fanatics**) + 3 **Cultists**." (`:19`)
- Higher source: the campaign (bearded devil for Willifort; spined devils for Seffia). The NF Morale line copies the quest-time adventure encounter.

**D4. Loyalty: the family (NF Emotions and Motivations) against Asmodeus first (structure doc)**
- NF Emotions: "Willifort most often feels clinical detachment, possessive loyalty to the Cassalanters, ..." (`campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:13`)
- NF Motivations: "Willifort wants to protect the Cassalanter family and their secrets, maintain his cover as an aging tiefling butler, and handle problems permanently when discretion fails." (`:15`)
- Structure doc: "Willifort Crowelle, doppelganger, serves Asmodeus with genuine devotion — the family is secondary." (`campaign/structure/arc-g-cassalanter-villa.md:21`); "serves Asmodeus directly. True believer." (`:95`); and, in the Redeemed outcome, "He has no loyalty to a family that no longer serves his master." (`:345`)
- Both sides are campaign files. The structure doc is authoritative only until its Cassalanter Villa journal exists, and none does (Glob `campaign/quests/**/*cassalanter*/**` returned nothing). The orchestrator must choose. The NF Motivations and Emotions are day-one RP text (ruling 3); the structure doc is quest-design text.

**D5. Who he answers to (two masters; the text states both)**
- Adventure: "Lord Victoro's personal attendant" (`sources/adventure-wdh.json:18482`); "Lord Cassalanter's doppelganger valet" (`:7064`, `:7694`).
- Campaign: "reports to Ammalia" (`campaign/setting/organizations/10-cassalanters.md:51`; `:117`; `campaign/setting/villains/cassalanters.md:64`; NF `:25`).
- Alexandrian: "The imps should report back to me directly at the villa." (Lord Cassalanter's note, `5. Faction Outposts.pdf` printed p.40 [PDF p.5]). The imps, not Willifort.
- Adventure, raven: "This raven is a shapechanged {@creature imp} that works for Lady Cassalanter." (`:7704`).
- The drafter needs both: he is Victoro's personal attendant and reports to Ammalia.

**D6. Founders' Day and the twins' birthday: Flamerule (campaign) against Tarsakh (Alexandrian and timeline addendum)**
- Campaign: "Flamerule 11" and "Flamerule 1" (org `:7`, `:30`, `:131`; villains `:16`, `:29`).
- Alexandrian Lair, printed p.79 [PDF p.3]: "TARSAHK 9th – LEIRUIN FEAST" and "TARSAKH 11th – THE TWINS’ BIRTHDAY" (image transcription).
- Addendum, printed p.225 [PDF p.1]: "Cassalanter kids get their souls sucked to Hell on Tarsakh 11th." (image transcription).
- Adventure: "a mere ten days after Founders' Day" (`sources/adventure-wdh.json:18294`), no month.
- Higher source: the campaign (Flamerule 1 and 11). The villains draft note (`campaign/setting/villains/cassalanters.md:133`) already records that the Alexandrian files put the feast on Tarsakh 9 or 10.

**D7. Name spelling: "Crowell" (Alexandrian Lair, printed p.79 [PDF p.3]) against "Crowelle" everywhere else**
- Lair: "Willifort Crowell" (image transcription).
- Campaign, adventure, Response Teams and Outposts: "Willifort Crowelle".
- Higher source: the campaign ("Crowelle"). Use "Crowelle".

**D8. Where the reports are dropped: "Dock Ward tobacconist" (campaign) against "tobacconist on the High Road" (Appendix D)**
- Campaign: "Reports floor-level patron intelligence monthly to Willifort Crowelle via Dock Ward tobacconist drop." (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:56`)
- Appendix D: "She reports in writing, monthly, to Willifort Crowelle, through a drop at a tobacconist on the High Road." (`sources/Appendix_D_-_Running_the_Tavern.md:252`)
- Higher source: the campaign (Dock Ward). The Appendix is an Alexandrian source and ranks lower.

**D9. Name clash: the courthouse doppelganger**
- Adventure: "If the doppelganger obtains the {@item Stone of Golorr|WDH}, it promptly delivers it to {@creature Victoro Cassalanter|WDH}. If the characters extricate themselves from the mess they're in, they can retrieve the stone from Cassalanter Villa (see chapter 6)." (`sources/adventure-wdh.json:10573`) sits in the courthouse section, where a doppelganger impersonates Captain Staget. The line before it names the impostor: "...whom \"Hyustus\" accuses of beating the cell block guards to death." (`:10572`). That is a different doppelganger, not Willifort. Do not attribute `:10573` to him.

**D10. "Head butler" in other sources (not Willifort)**
- Adventure: "The Zhents have killed two servants, an older male human (the head butler) and a younger male halfling (a cook), and left their bodies on the floor." (`sources/adventure-wdh.json:5731`, page 52, before the Cassalanter entries at page 60). The house is not named in the line, and it was not identified in this pass.
- Alexandrian: "Corpses present: Head butler and cook (G6), head maid (back stairs to G19), 8 guards and 2 Zhents (G8), 2 guards (G9), 6 guards and 2 Zhents (G13)." (`sources/Act_III_Arc_E.md:383`). Not Willifort.

**D11. Overview length (not a source conflict)**
- The NF Overview is one sentence of 37 words (`campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:29`). The brief's limit is 21 words per sentence.

---

## E. Stale lines in other files (not edited), and routed quest references

### E1. Stale or inconsistent in other files

- `campaign/setting/governance-and-guilds/city-watch.md:134` (a setting page): "- **Names with no page:** Elminster, Hyustus Staget, Cressa Galavarco, Jonn Bannock, Ysa Terrow, Captain Rulathon, Ezender Drayth, Corylus Thann, Bowgentra Summertaen, Willifort Crowelle, Brenna, Orvyn, Gosta Ironhelm, Duhlark Kolat, and the Belabranta family. ..." Stale now that the NF page exists.
- `sources/research/pass4-bundles/cassalanters/campaign-hits.txt:1005` (copy of `arc-g-cassalanter-villa.md:83`): "Willifort Crowelle is a doppelganger who has served the Cassalanter household for eight years." The bundle copy drops the `[research]` tag that the current file carries.
- `campaign/structure/ch2-city-of-splendors.md:294` (retired chapter file; CLAUDE.md says do not use): "method: Willifort Crowelle (doppelganger butler) manages household security".
- `campaign/setting/organizations/10-cassalanters.md:95` ("Presents as an elderly tiefling") against `sources/adventure-wdh.json:18481` ("an aging male tiefling"). Wording only.
- `campaign/setting/deities/bhaal.md:100`: "The campaign's doppelgangers (Willifort Crowelle, Vessa) have no tie to him in any file, and the page draws none." Consistent; not stale.

### E2. Routed to quests (quest-time facts and where they already live)

- Jarlaxle assassination, hostile mode: `campaign/guides/factions/11-cassalanters.md:11`; `campaign/guides/gm-guide/running-the-villains.md:76`; `sources/6. Faction Response Teams.pdf` printed p.52 [PDF p.4]; `campaign/structure/arc-e-faction-outposts.md:355` ("Opposing or refusing them: imps maintain constant surveillance, Seffia's team competes at **Xanathar's Lair** operations, and Willifort Crowelle makes social approaches that escalate to assassination attempts if the party actively works against the family.").
- Villa heist (social exposure, cover breaking, combat): `campaign/structure/arc-g-cassalanter-villa.md:85`, `:95`, `:111`, `:115`, `:247`, `:259`, `:265`, `:269`, `:277`; `campaign/locations/cassalanter-villa/01-entrance-hall.md:9`, `:15`, `:21`, `:23`; `campaign/locations/cassalanter-villa/area-overview.md:34`, `:52`, `:60`-`:63`.
- Caravance skeleton crew: `campaign/structure/arc-g-cassalanter-villa.md:75`.
- Outcome states naming him: `campaign/structure/arc-g-cassalanter-villa.md:345` (Redeemed: he flees) and `:349` (Active: his network may try to recover Eye #2). No Event Outcome name is used yet.
- Trollskull Manor response team: `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:63` ("**Who comes:** \"Willifort Crowelle\" — a doppelganger, the Cassalanters' most trusted lieutenant. Always arrives as a different identity: friendly rival tavern owner, minor city functionary checking compliance paperwork, Harper contact the party hasn't met. Never arrives as himself, because himself does not exist."); `:73` ("**\"Willifort\" as compliance officer:** Has a real Fellowship of Innkeepers badge (he had it made). Polite, thorough, two degrees more specific than required. How often deliveries? Regular overnight guests? Cellar access? At the door on the way out: \"Do you know a man named Dalakhar? Small, gnomish build?\" Watches the party's face."); `:77` ("**Escalation:** Once the party is in direct competition for the Gold, Willifort shifts from information-gathering to interference: impersonating party members to damage faction relationships, or arranging for a Cassalanter-connected Watch lieutenant to take a new interest in the tavern's compliance record."); `:79` ("**Fame impact:** Willifort's visit: 0. Seffia's team detected during busy service: −1 (patrons notice something wrong, can't say what).").
- Appendix D, Trollskull response (Alexandrian): `sources/Appendix_D_-_Running_the_Tavern.md:1576`-`:1602` (C5).
- Lords' Alliance Warduke: `campaign/quests/faction-events/lords-alliance/r25-warduke/ev-01-warduke.md:200`.
- Bregan D'aerthe, The Theater's Back Room: `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:20`, `:337`, `:362`.
- Vault of Dragons: `campaign/structure/arc-j-vault-of-dragons.md:198`-`:199`.
- Stone-theft chase and hire-coach (adventure ch. 6): `sources/adventure-wdh.json:6670`-`:7716`. No campaign file carries it.

---

## F. Gaps (what a Background would need that no source gives)

For each gap, the sourced facts the drafter must stay consistent with are listed.

1. **Birth, origin and first form.** No source. Consistent with "a doppelganger who has served the Cassalanters long enough that the role has become his identity" (`campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:21`).
2. **How he came to the Cassalanters.** No source gives a hiring or a first meeting. Consistent with "With the exception of their personal attendants, the Cassalanters replenish their servants regularly." (`sources/adventure-wdh.json:18598`) and the tenure figure "eight years [research]" (`campaign/structure/arc-g-cassalanter-villa.md:83`). The eight years is the only number.
3. **When and how he began to serve Asmodeus.** No source. The wiki says "full member of the cult" (`wiki:67`). The org page gives the others' roads to faith and omits him (`campaign/setting/organizations/10-cassalanters.md:40`). Consistent with "serves Asmodeus with genuine devotion" (`arc-g-cassalanter-villa.md:21`).
4. **Tiefling guise: whom he copies.** No source names the person. Consistent with "an aging male tiefling" (`sources/adventure-wdh.json:18481`) and "an elderly tiefling" (`:7064`). Do not give the guise a name.
5. **Real name and true form.** No source. The wiki's true-name field is blank (`wiki:10`). Consistent with "Never arrives as himself, because himself does not exist." (`campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:63`).
6. **Age and birth year.** No source gives a number. Consistent with "aging" (`campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:15`, `:29`).
7. **Relationship with Victoro.** The sourced relation is "personal attendant" and "personal valet" (`sources/adventure-wdh.json:18482`; `wiki:65`). No personal history. See D4 (loyalty).
8. **Relationship with Ammalia.** The sourced relation is the reporting line (`campaign/setting/organizations/10-cassalanters.md:51`). No personal history.
9. **Relationship with Osvaldo.** The sourced fact is "Willifort knows." (`campaign/setting/organizations/10-cassalanters.md:129`). No other tie. The NF page does not mention Osvaldo.
10. **Relationship with Tissina and the cult staff.** The sourced ties are the shared lockbox (`sources/adventure-wdh.json:20540`) and the perimeter duty at gatherings (`:22818`). No personal history.
11. **Relationship with Maesta (non-cult housekeeper).** The sourced fact is that she has seen him "change the shape of his hands when he thought no one was looking" (`campaign/structure/arc-g-cassalanter-villa.md:111`). Consistent with the habit only.
12. **The Asmodean faith in detail: rites, rank, what he prays for.** No source. The creed and sacraments are open: "The creed, the cult's other sacraments and how it recruits remain unsourced" (`campaign/setting/organizations/10-cassalanters.md:178`, Draft Notes). Consistent with "True believer" (`arc-g-cassalanter-villa.md:95`).
13. **Fears.** No source. Consistent with "cold contempt for guests who are easy to deceive" (NF `:13`) and "he would die before revealing the temple" (`arc-g:95`).
14. **Loved ones, places, a craft, a debt.** No source. The only held object is the cult lockbox key (`sources/adventure-wdh.json:20540`). No place of his own is named.
15. **Fate after the campaign.** Quest outcomes only: he flees in the Redeemed outcome (`arc-g:345`), and his network may recover Eye #2 in the Active outcome (`arc-g:349`). These are quest states, not Background.
16. **Hadra and the day she left.** The sourced fact is that "Willifort Crowelle noticed the day she left" (`campaign/setting/notable-figures/independents-allies/15-hadra-stonebread.md:21`). Whether he acted on it is not given.
17. **Founders' Day role.** No source (C6).
18. **Past deaths and the two cultists Seffia's team lost.** No source names a Willifort kill. The NF page names none.

---

## G. Source facts that hint at the figure's inner life

Each quote is exact. The drafter uses these for Personal goals (ruling 17) and must not contradict them. Quest-time sources are marked (QT). Quest-time sources give habit or trait only, not plot.

**G1. Devotion and the limit of his loyalty**
> "Willifort Crowelle, doppelganger, serves Asmodeus with genuine devotion — the family is secondary."
> — `campaign/structure/arc-g-cassalanter-villa.md:21`

> "- **Willifort Crowelle** (doppelganger, butler) — serves Asmodeus directly. True believer. Will not break under any social pressure; he would die before revealing the temple. If the Cassalanters are exposed as cultists, Willifort drops his tiefling disguise and fights."
> — `campaign/structure/arc-g-cassalanter-villa.md:95`

> "Willifort: if he served Asmodeus directly (he did), he flees. He has no loyalty to a family that no longer serves his master." (QT: outcome)
> — `campaign/structure/arc-g-cassalanter-villa.md:345`

**G2. Inner state (Emotions, verbatim RP text)**
> "Willifort most often feels clinical detachment, possessive loyalty to the Cassalanters, controlled satisfaction in maintaining perfect cover, cold contempt for guests who are easy to deceive, and the alien patience of a creature that has been someone else for so long it has forgotten what it was."
> — `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:13`

**G3. Identity and self**
> "To those he trusts, he is a doppelganger who has served the Cassalanters long enough that the role has become his identity."
> — `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:21`

> "Never arrives as himself, because himself does not exist." (QT: Trollskull guide, the tavern visit; the full sentence is at `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:63`, quoted in E2)

> "Willifort is \"more than he appears\" — she has seen him change the shape of his hands when he thought no one was looking." (QT: structure doc; Maesta's knowledge; the full sentence is quoted in A2)
> — `campaign/structure/arc-g-cassalanter-villa.md:111`

**G4. Habit and watching (trait)**
> "He always want knew all that happened inside the mansion and survey all the guests in order to hide connection with Asmodeus' cult." (wiki, typo as printed)
> — `wiki:65`

> "He ushers nosy guests away from areas or objects that might link the Cassalanters with the Asmodeus-worshiping cult."
> — `sources/adventure-wdh.json:18482`

> "Mr. Crowelle counts the household at the door." (QT: Bregan D'aerthe quest file, a line spoken by a servant)
> — `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:337`

**G5. Trust and standing**
> "Victoro, Ammalia, and the head butler, Willifort, hold keys to every room in the house."
> — `sources/adventure-wdh.json:18614`

> "In truth he is a doppelganger and their most trusted lieutenant."
> — `sources/6. Faction Response Teams.pdf` printed p.53 [PDF p.5] (image transcription)

> "With the exception of their personal attendants, the Cassalanters replenish their servants regularly."
> — `sources/adventure-wdh.json:18598` (the attendants are kept; no reason given)

**G6. Self-preservation in combat (QT)**
> "Willifort flees on foot if the hirecoach is destroyed or its horses are unable to move."
> — `sources/adventure-wdh.json:7067`

> "In combat: drops the tiefling disguise, uses Multiattack, and attempts to flee through the service wing if reduced below 15 HP."
> — `campaign/structure/arc-g-cassalanter-villa.md:247`

**G7. Fear and grudges**
- None in any source. The only grudge-like line is about Jarlaxle (hostile mode, `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:23`). It is quest time, and the NF page already holds it.

**G8. Contempt**
> "Contempt for easily deceived guests never reaches his words, only his eyes."
> — `.claude/skills/character-voices/voices/cassalanters.md:56` (Personality in speech)

---

## Voice profile (for ruling 16)

Lines 49-63 of `.claude/skills/character-voices/voices/cassalanters.md` are the Willifort profile. The drafter copies them verbatim except for the quest-time clauses (C2: lines 52, 54, 55 and 63). Every other sample line and field is day-one. The sample line at line 63 ("Under pressure (unmasked)") describes the cover broken (Stage 4, `arc-g:277`).

---

## Not found

Terms and files searched:
- `Willifort`, `Crowelle`, `Crowell`, `butler`, `doppelganger`: `sources/adventure-wdh.json` (whole file); `campaign/` (whole folder, including notable-figures, organizations, villains, guides, locations, quests, structure, setting, gazetteer); `sources/*.md` (Grep with glob `*.md`); `sources/SOURCE_GUIDE.md`; `sources/research/pass4-bundles/cassalanters/` (wiki, campaign-hits, adventure-hits). `sources/research/pass3-bundles/` and `pass5-bundles/` returned hits, all copies of campaign or adventure lines.
- `campaign/quests/**/*cassalanter*/**`: no Cassalanter Villa quest journal exists. The villa is still a structure doc (`campaign/structure/arc-g-cassalanter-villa.md`).
- `hire-coach`, `Street Chase`, `Cellar Complex`, `Rooftop Chase` in `campaign/`: no Cassalanter stone-chase carrier.
- Alexandrian PDFs read for Willifort: `1. The Villains.pdf` (7 pages, printed pp.13-19; the Cassalanter section at printed pp.18-19 does not name him); `5. Faction Outposts.pdf` (13 pages; Willifort on printed p.40 [PDF p.5]; Cassalanter outposts printed pp.38-41); `6. Faction Response Teams.pdf` (8 pages; Willifort on printed pp.52-53 [PDF pp.4-5]); `10. Lair  Cassalanter Villa.pdf` (6 pages, printed pp.77-82); `13. Clues and Timelines.pdf` (5 pages, printed pp.97-101; no Willifort); `17. Outpost and Lair Revelation Lists.pdf` (4 pages, printed pp.121-124; no Willifort); `21. Faction Reports of the Grand Game.pdf` (13 pages, printed pp.142-154; handwriting-font reports; no Willifort in the Cassalanter report, pp.146-147); `29. Addendum Timelines  Starting the Campaign.pdf` (2 pages, printed pp.225-226; Tarsakh dates only).
- Alexandrian PDFs not read in this pass (so an absence there is not a finding): `2. Other Factions.pdf`, `3. Player Character Factions.pdf`, `4. Gralhund Villa.pdf`, `7. Other Response Teams.pdf`, `8. The Eyes of the Stone.pdf`, `9. Lair – Sea Maidens Faire.pdf`, `11. Lair  Xanathar’s Lair.pdf`, `12. Lair  Zhentarim – Kolat Towers.pdf`, `14`, `15`, `16`, `18. Golorr Artifacts.pdf`, `19. The Brandath Crypts.pdf`, `20. The Vault.pdf`, `22`-`28`, `30`. `19. The Brandath Crypts.pdf` and `26. Addendum Other Collaborators.pdf` may hold Cassalanter material and should be read.
- Appendix B (`sources/Appendix_B_-_Player_Factions.md`) and Appendix C (`sources/Appendix_C_-_Player_Faction_Missions.md`): no match.
- Wiki: the whole scratchpad page was read. No edition is printed on the lines beyond the citation keys (WDH5e-p116, WDH5e-p122, WDH5e-p60, WDH5e-p62).
- Founders' Day role for Willifort: none (C6).
- Cult creed and his place in the rites: none (F12).

## Not readable

- `sources/Other remix files/Cassalanters, their tragic backtstory, and Endgame setup.docx` (listed at `sources/SOURCE_GUIDE.md:687`: "Victoro & Ammalia backstory, the soul-pact timeline, the children's situation, endgame resolution paths"). This is the most likely campaign source for Willifort's backstory and must be extracted by the user. The `.docx` cannot be opened with the tools here.
- `sources/Other remix files/The Waterdavian's Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx` (`sources/SOURCE_GUIDE.md:695`, a broad NPC reference that may hold Willifort). Not readable here.
- The PDFs were read as rendered images only (no `pdftotext` in this session). Every PDF quote here is a transcription (see Method).
