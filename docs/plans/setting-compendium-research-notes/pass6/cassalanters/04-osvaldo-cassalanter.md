# Pass 6 research notes: Osvaldo Cassalanter

Page: `campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR. Osvaldo is in the attic (room C24) as a chain devil. The pact is a GM fact. The public story is that he is at school. Cassalanter secrecy applies (nobody outside the household and the cult knows the pact).
Model format: `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md`
Companion notes: `docs/plans/setting-compendium-research-notes/pass6/cassalanters/02-ammalia-cassalanter.md`, `docs/plans/setting-compendium-research-notes/pass6/cassalanters/01-victoro-cassalanter.md`

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes (`\"`) are shown as plain quotes. Tags such as `{@creature ...}` are left as written.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. Two PDFs were read as rendered page images and their quotes are transcriptions. Check exact wording with `pdftotext -layout` before any quote goes into prose:
  - `sources/10. Lair  Cassalanter Villa.pdf` (six pages in the PDF; printed pp.77-82 = PDF pp.1-6). Read: PDF pp.1-6.
  - `sources/1. The Villains.pdf` (printed pp.18-19 = PDF pp.6-7). Read: PDF pp.6-7.
- Alexandrian appendices B, C, D and `Act_III_Arc_E.md` contain no Osvaldo text (see Not found).
- Wiki: the extracted page `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-cassalanters/04-osvaldo-cassalanter.txt`. Quoted as "wiki line N" (that file's lines). Citation keys are as printed (5e, *Waterdeep: Dragon Heist*).
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **The brief's premise needs one correction.** The Osvaldo page (line 23), the Ammalia page (line 22) and the Sea Ward gazetteer (line 113) do not disagree with each other on the term. All three say "shielding circle". The disagreement is between that term and two other campaign readings: `arc-g-cassalanter-villa.md` line 13 ("through the warded door") and the Villains, Organization and History pages, which say "pentagram". The published adventure says "pentagram" and never says "shielding circle" (D1).
2. **The Osvaldo page's Morale (line 23) and Persona (line 21) describe encounter behaviour and conflict with the published text.** The adventure says Ammalia's visit makes him curse her, not calm down. The adventure ties his attacks to the pentagram, and the Osvaldo page says he attacks anything that enters the attic (D2, D3).
3. **Soul status conflicts across sources.** The adventure says Osvaldo's soul "is forever lost and can't be saved" (`sources/adventure-wdh.json:32693`). The campaign's Path 2 and the C24 room notes say his soul "is freed" if the contract is destroyed (`campaign/structure/arc-g-cassalanter-villa.md:149`, `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:31`). The campaign outranks the adventure, but a day-one page cannot state either outcome (D5).
4. **Cult status is unsourced for him.** No roster names Osvaldo as a cult member. The published text says the twins are not members (`sources/adventure-wdh.json:18418`). Nothing says whether he was a member before 1489 DR (F2).
5. **Several details have no source at all:** "15-foot reach" (`campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md:21`), "brass-tinted eyes" (only `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:27`), "Tethyrian" (the wiki says only "Human"), and the claim that he knows his siblings' fate (`04-osvaldo-cassalanter.md:13`). Each is listed in F or D.
6. **The Alexandrian Lair spells his name "Oslando"** in two places (printed p.82). Every other source says "Osvaldo" (D9).

---

## A. Background facts by theme

### A1. Origin, birth and early life (no campaign or adventure source for birth or childhood)

**Campaign, the birth year (derived, not sourced)**
> "1480 DR: Osvaldo is born. This is derived from his ninth year in 1489 DR and is stated by no source."
> — `campaign/setting/history/05-a-debt-in-blood.md:124` (Timeline, GM)

> "- **1480 and 1483 DR, the children are born (derived):** Osvaldo was born in 1480 DR, and the twins, Terenzio and Elzerina, were born on Flamerule 11, 1483 DR. No source states either year. Osvaldo's comes from his ninth year in 1489 DR, and the twins' comes from their ninth birthday on Flamerule 11, 1492 DR (**A Debt in Blood**)."
> — `campaign/setting/organizations/10-cassalanters.md:23` (History)

**Wiki, the lead line (no birth, birthplace or childhood given)**
> '''Osvaldo Cassalanter''' was the heir apparent of the [[Cassalanter]] family of [[Waterdeep]] in the late 15{{th}} century [[DR]].<ref name="WDH5e-p124" />
> — wiki line 62 (edition: 5e, `WDH5e-p124`)

The wiki's infobox leaves `dob` (wiki line 21), `age` (wiki line 17) and `ethnicity` (wiki line 15) blank.

**Adventure, the childhood image (the only pre-1489 picture of him)**
> "Twelve-year-old Osvaldo holding a ceremonial rapier",
> — `sources/adventure-wdh.json:20330` (Portraits list for the villa; the entry is listed with the wedding portrait at 20329)

> "Hanging on the north wall between two bookshelves is a 7-foot-tall portrait of Lord and Lady Cassalanter holding two infant children and standing beside their teenage son, Osvaldo. (This portrait conceals a secret door.)"
> — `sources/adventure-wdh.json:20039` (the library portrait; see D7 for the age conflict)

### A2. Family, heir status and household

**Adventure, eldest child and heir**
> "Ammalia and {@creature Victoro Cassalanter|WDH} traded the soul of their eldest child for power. Stripped of his humanity, Osvaldo was chained up in Cassalanter Villa and slowly transformed into a devil (and an insane one at that). Now a creature of pure evil and hate, he has no hope of regaining what was taken from him."
> — `sources/adventure-wdh.json:32474` (Appendix B, "Osvaldo Cassalanter", page 214)

> "After the deal was struck, the Cassalanters enjoyed a miraculous comeback. Their banking and money-lending business thrived while their competition suffered. The disappearance of their eldest son (and heir apparent) earned them sympathy. Their philanthropic endeavors bought them legitimacy and new friends. They became the envy of Waterdavian nobility in short order. Seemingly blessed, the Cassalanters attracted new followers to their cult of devil worship, which was Asmodeus's plan all along."
> — `sources/adventure-wdh.json:18295` (Ch.6 intro; see D6)

**Campaign, the relationship to the parents and siblings**
> "**Relationships.** Osvaldo is the eldest child of Victoro and Ammalia (taken at nine, twelve now, his soul surrendered to Asmodeus three years ago during the family's financial crisis), the reason Terenzio and Elzerina are forfeit on their ninth birthday, Flamerule 11, 1492 DR (the pact requires both 999,999 gp and ninety-nine souls), and the tragedy that both explains and indicts everything his parents are doing."
> — `campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md:25`

> "- **The family:** Victoro and Ammalia head the house, and Victoro leads the cult as its priest. Their twins, Terenzio and Elzerina, are eight years old. The twins are tutored privately, rarely leave the estate and belong to no cult. Their eldest brother Osvaldo is the chain devil in the attic (*Dragon Heist*, 5e; **Osvaldo Cassalanter**)."
> — `campaign/setting/organizations/10-cassalanters.md:47`

**Adventure, the pact covers all three children**
> "The {@creature Victoro Cassalanter|wdh|lord of House Cassalanter} is a devilishly handsome half-elf who likes coin and power. He and his wife gained both by cutting a deal with Asmodeus-which involved trading away the souls of their three children."
> — `sources/adventure-wdh.json:32691` (Appendix B, "Victoro Cassalanter"; the next line, 32692, gives his public face: "Most Waterdavians know him as a successful banker, philanthropist, and worshiper of Lathander.")

**Campaign, the household: who lives in the house**
> "- **The villa:** Cassalanter Villa stands in the Sea Ward, where the wiki puts it on the southwest corner of Delzorin Street and Diamond Street (Forgotten Realms Wiki, *Cassalanter*, 3e). White walls and a crimson roof with turrets rise behind a wrought-iron gate, and the campaign journal gives the house four stories above ground, a basement and a sub-basement (**Cassalanter Villa**, location). Hired guards in house livery hold the front gate and the garden gate. Only the family, its personal attendants and its guards live in the house, and the other servants arrive before dawn from homes in the Dock Ward and the Field Ward (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/10-cassalanters.md:48`

### A3. The taking, 1489 DR, and the transformation (pre-campaign)

**Adventure, the taking (no age given; "three years ago" is the anchor)**
> "Victoro and {@creature Ammalia Cassalanter|WDH} struck a deal with Asmodeus, Lord of the Nine Hells. Three years ago, they traded away the souls of their children to escape financial ruin. The soul of their eldest son, Osvaldo, was taken immediately. What was left behind was transformed into a chain devil, which the Cassalanters confined to their attic. Their two youngest children, Terenzio and Elzerina, are doomed to lose their souls when they turn nine years old a mere ten days after Founders' Day, a midsummer festival that celebrates Waterdeep's founding."
> — `sources/adventure-wdh.json:18294` (Ch.6 intro)

**Adventure, the conflicting signing phrase (see D7)**
> "When they were young, Ammalia and Victoro signed a contract with the archdevil, trading the souls of their children for power, good health, and long life. The soul of Osvaldo, their eldest son, was taken immediately, and he was transformed into a chain devil. The souls of the younger twins, Terenzio and Elzerina, will be taken when they turn nine years old."
> — `sources/adventure-wdh.json:31715` (Appendix B, "Ammalia Cassalanter", page 193)

**Campaign, the age at the taking (user ruling, Session 47)**
> "> - **Conflicts:** The user ruled in Session 47 that every child is taken at nine. Osvaldo was nine when taken and is twelve now, matching the published adventure's portrait of \"twelve-year-old Osvaldo\" (`adventure-wdh.json` line 20330) and the Alexandrian author's \"already 9\"."
> — `campaign/setting/history/05-a-debt-in-blood.md:137` (Draft Notes)

> "> - The contract claimed the children one at a time. Osvaldo, the eldest, was taken first and is now a chain devil. Terenzio and Elzerina are still claimed but not yet taken."
> — `campaign/setting/history/05-a-debt-in-blood.md:23` (lead)

**Campaign, the transformation (quest opener, backstory; pre-campaign event)**
> "Osvaldo's transformation was immediate. The boy screamed for three hours before the change completed. Victoro sealed the attic with abjuration wards, soundproofed the floor, and has not entered the room since. Ammalia reads to her son weekly through the warded door — children's stories he loved before the contract, spoken to a chain devil who weeps black ichor and claws at the walls. Two imps in spider form watch the corridor. The household staff knows the attic is forbidden. Only Willifort Crowelle — the doppelganger butler who serves Asmodeus directly — knows what is behind the door."
> — `campaign/structure/arc-g-cassalanter-villa.md:13` (Quest Opener. The "has not entered the room since" clause conflicts with the "in months" clauses, see D4; the "warded door" clause conflicts with "shielding circle", see D1)

**Campaign, the signing and the pact's year (derived)**
> "The bargain was made in 1489 DR, counted back from the published \"three years ago\". Ammalia found the way through infernal research. A pit fiend carried the contract to them, and they signed it together in the temple beneath their own villa."
> — `campaign/setting/villains/cassalanters.md:24`

> "The contract claims each child at nine. Osvaldo was nine when he was taken and is twelve now, a chain devil held in the soundproofed attic of the villa. The twins' souls are forfeit on their ninth birthday, Flamerule 11, ten days after Founders' Day."
> — `campaign/setting/villains/cassalanters.md:25`

> "- **About 1489 DR, Osvaldo:** The contract claims each child at nine, and Osvaldo, who was nine, was taken at once. His soul went to Asmodeus and his body became a chain devil, which the family keeps in the soundproofed attic of the villa, room C24, under the watch of two imps in spider form. Ammalia visits weekly and sits in the room outside the pentagram, and Victoro has not entered in months. The city hears that Osvaldo studies in a faraway city, and the twins have been told the same (**A Debt in Blood**; **Osvaldo Cassalanter**; *Dragon Heist*, 5e). Campaign change: every child is taken at nine (user ruling, Session 47)."
> — `campaign/setting/organizations/10-cassalanters.md:26`

**Campaign, the Proof of Contract (History, GM)**
> "### The Proof of Contract"
>
> "- Souls were claimed one at a time."
> "- Osvaldo, the eldest, was nine when he was taken, and is now twelve."
> "- Osvaldo is a chain devil held in the soundproofed attic of the villa, room C24, never the basement or the temple. Ammalia visits weekly and sits in the room outside the pentagram. Victoro has not entered in months. Willifort knows. Two imps are always present."
> "- Terenzio and Elzerina are eight years old and have not been taken. They do not know about the bargain. They have been told that Osvaldo attends school in a faraway city."
> — `campaign/setting/history/05-a-debt-in-blood.md:46-51`

### A4. Confinement: the attic (room C24), the guards and the wards

**Adventure, the room (C24, "Osvaldo's Prison", page 124)**
> "{@creature Osvaldo Cassalanter|WDH} (see {@adventure appendix B|WDH|12}) shrieks and moans at all hours of the day. He is trying desperately to get someone to hear him and come to his rescue. If one or both of his parents are here, he spits curses at them as they weep before him."
> — `sources/adventure-wdh.json:20661`

> "Guarding the room are two {@creature imp||imps} in spider form. They answer to Lord Cassalanter, and their job is to kill birds, {@creature rat||rats}, and other vermin that find their way into the attic. They attack anyone who tries to free Osvaldo or threatens other family members present."
> — `sources/adventure-wdh.json:20662`

> "The Cassalanter heir apparent is a soulless abomination thanks to his parents' thoughtless greed. His empty shell of a body has been transformed into a {@creature chain devil} that his parents have imprisoned using his own chains. A 10-foot-diameter pentagram has been burned into the floor around him. A {@spell detect magic} spell reveals a powerful aura of abjuration magic emanating from the symbol."
> — `sources/adventure-wdh.json:20663`

> "Osvaldo's chains are wrapped around the beams and timbers that frame the room. He can't damage the house, nor can he break his own chains. He can only howl impotently at the misery being inflicted on him. He is thoroughly insane and can't be reasoned with."
> — `sources/adventure-wdh.json:20664`

> "A successful {@dc 15} Intelligence (Arcana) check reveals that the pentagram prevents Osvaldo from manipulating his chains, and that the effect ends if another creature enters the area encompassed by the pentagram. The magic of the pentagram can also be dispelled ({@dc 15}). If he is freed, Osvaldo regains control of his chains and attacks indiscriminately. If he is reduced to 0 hit points, the chain devil cries out for his mother before melting into a pool of sickening black ichor."
> — `sources/adventure-wdh.json:20665`

> "You are greeted with a wave of incoherent howling, as if opening the door broke down a dam that had been holding back a madman's screams."
> — `sources/adventure-wdh.json:20658` (insetReadaloud at the door)

> "If {@creature Ammalia Cassalanter|WDH} or {@creature Victoro Cassalanter|WDH} (see {@adventure appendix B|WDH|12}) or both are present, the door to this room is unlocked but closed. Otherwise, it's locked shut, and Victoro and Ammalia carry the only keys. When the characters first open the door, read:"
> — `sources/adventure-wdh.json:20653`

> "This attic is soundproof as long as no doors are open. Osvaldo's howling can be heard outside the attic only if the trapdoor between this room and {@area C22|31f} and the door between this room and {@area C24|325} are both open at the same time. Additionally, creatures that have telepathy can't communicate telepathically with creatures outside the attic unless the doors are open."
> — `sources/adventure-wdh.json:20633` (C23, "Attic Landing")

**Campaign, the room (C24, Cassalanter Villa heist text; quest-time location, routed)**
> "**C24 — Osvaldo's Prison.** The attic. Soundproofed. Accessible via C23 from C22, or via a locked exterior door on the attic level (DC 19 Dexterity (Thieves' Tools)). Inside: a burned pentagram on the floor, abjuration wards glowing faintly, and Osvaldo — a chain devil who was taken at nine and is now twelve. He is chained to an iron ring in the floor. Two imps in spider form cling to the rafters."
> — `campaign/structure/arc-g-cassalanter-villa.md:205`

> "At the end of the chains: Osvaldo."
> — `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:19`

> "**Two imps in spider form** cling to the rafters above the ring. They are passive observers during normal attic operations, reporting to Ammalia through a one-way telepathic bond. They attack if Osvaldo is directly threatened or if the party attempts to dispel the containment wards."
> — `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:23` (imps report to Ammalia here; the adventure says they "answer to Lord Cassalanter", see D11)

**Wiki, the confinement (5e, cited p.124)**
> "Osvaldo was chained and locked in the attic of [[Cassalanter Villa]] where he was held in place by a magical pentagram and guarded by two [[imp]]s working for Victoro. He desperately tried to free himself by asking for someone to rescue him.<ref name=\"WDH5e-p124\">{{Cite book/Waterdeep: Dragon Heist|124}}</ref>"
> — wiki line 73 (Activities)

### A5. Public cover (the school story; suspicion only)

**Adventure, what the twins were told**
> "If asked about their older brother, Osvaldo, Terenzio and Elzerina repeat what their parents have told them: he's attending school in a faraway city (they don't recall which one). Neither knows the cruel fate that has befallen Osvaldo (see {@area C24|325}) or suspects that a similar fate awaits them."
> — `sources/adventure-wdh.json:18456` (Terenzio and Elzerina, page 116)

**Adventure, the public disappearance (see D6)**
> "Victoro and Ammalia's eldest son disappeared three years ago when the family was on the verge of bankruptcy. They have two surviving children, young twins named Terenzio and Elzerina."
> — `sources/adventure-wdh.json:18403` (the Cassalanters' public overview, page 116)

**Campaign, the cover (Osvaldo page, Persona)**
> "**Persona.** To the world, Osvaldo Cassalanter is a name the family does not mention — \"attending school in a faraway city,\" Terenzio and Elzerina were told. To those who open the attic door, he is a chain devil in a soundproofed attic who attacks immediately, and whose chains have a 15-foot reach. Deep down, some fragment of Osvaldo is still there, and it hears his mother's voice when she comes to read, and it is very much aware of what was done to it."
> — `campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md:21` (the public part is day-one; the encounter clause is in C)

**Campaign, the cover (Organization page, Overview)**
> "The Cassalanters are a noble family of Waterdeep and among the city's most prominent philanthropists. ... Their eldest son is said to be at school in a faraway city, and more than one Waterdhavian has wondered aloud how a family can be so gracious, so prosperous and so fortunate all at once."
> — `campaign/setting/organizations/10-cassalanters.md:110` (the Overview paragraph; the ellipsis skips the family's charity and galas, and the full paragraph is the Overview at line 110)

**Campaign, the cover (Organization page, GM Secret callout)**
> "- **Osvaldo:** The eldest son's soul was claimed first, when he was nine, the age at which the contract claims each child, and he is now twelve and a chain devil held in the soundproofed attic of the villa, room C24, never the basement or the temple. Ammalia visits weekly, sitting in the room outside the pentagram to read to him while he curses her and weeps. Victoro has not visited in months. Willifort knows. Two imps are always present. Terenzio and Elzerina have been told Osvaldo is at school. Had the contract run its course, the twins were to become lemures (Forgotten Realms Wiki, Victoro Cassalanter, from *Dragon Heist*, 5e)."
> — `campaign/setting/organizations/10-cassalanters.md:129` (GM Secret callout; the callout's header is at line 126)

> "- **The Family Comes First:** The love for the twins is real and drives every decision. Victoro and Ammalia would do anything to save Terenzio and Elzerina. Neither twin belongs to the cult, and both have been told that Osvaldo attends school in a faraway city (*Dragon Heist*, 5e). The published adventure adds that Victoro's plan to win back the twins is meant to ease his guilt over Osvaldo (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/10-cassalanters.md:35`

**Campaign, the cover (History page, GM)**
> "- Terenzio and Elzerina are eight years old and have not been taken. They do not know about the bargain. They have been told that Osvaldo attends school in a faraway city."
> — `campaign/setting/history/05-a-debt-in-blood.md:51`

**Campaign, the Overview (Villains page)**
> "Their eldest son is said to be studying in a faraway city, and the family does not often speak of him."
> — `campaign/setting/villains/cassalanters.md:80`

**Campaign, the sibling's view (Terenzio page, Persona)**
> "**Persona.** To the world, Terenzio is a boy in a dragon costume being chased around the library by his sister with a wooden sword. To those who speak with him, he knows his parents are looking for \"missing dragons,\" he has heard howling from the attic two or three times, and he thinks his brother Osvaldo must be doing very well at school by now. Deep down, he has decided that whatever is in the attic is probably a dragon, and he considers this exciting rather than frightening."
> — `campaign/setting/notable-figures/cassalanters/05-terenzio-cassalanter.md:21`

**Adventure, the twins' howling (5e)**
> "Terenzio and Elzerina have heard howling coming from the attic two or three times in their lives and are curious about what lurks there."
> — `sources/adventure-wdh.json:20634`

### A6. Household and cult status

**Cult status (no roster names him)**
> "- **Rank Is Kept:** The cult runs on a strict order. Victoro leads the worship and Ammalia pours the wine, the head servants keep the other members in line, and Seffia is a true believer in the cult's hierarchy (*Dragon Heist*, 5e; **Seffia Naelryke**). The **Asmodeus** page says his priests obey his Chosen as lesser devils obey greater ones, and no file names a Chosen in the campaign."
> — `campaign/setting/organizations/10-cassalanters.md:41`

> "- **Household staff:** The villa employs sixteen named staff, and ten of them know nothing about the temple (`arc-g-cassalanter-villa.md` line 91). The six cult members are Willifort the butler, Tissina Khyret the attendant, Nana Rosse the twins' caretaker, Jandar Chergoba the head chef, and the field pair Seffia Naelryke and Arn Xalrondar. The other ten are Corvo (footman), Pela (laundress), Marchello (gardener), Fiorella (cook's assistant), Doro (stable hand), Lissette (upstairs maid), Rennet (scullion), Maesta (housekeeper), Tomas (night watchman) and Bressa (nursemaid). Maesta manages the non-cult staff and is loyal to the household's reputation, not to the Cassalanters themselves."
> — `campaign/setting/organizations/10-cassalanters.md:52` (Osvaldo is not on either list)

> "- **Who suspects:** Everybody is suspicious of the Cassalanters because they are too nice to be this rich and this purebred, and nobody outside the household and the cult knows they are infernalists."
> — `campaign/setting/organizations/10-cassalanters.md:118`

**Campaign, the twins are not in the cult (organization page)**
> "Neither twin belongs to the cult, and both have been told that Osvaldo attends school in a faraway city (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/10-cassalanters.md:35`

**Adventure, the twins are not in the cult**
> "The Cassalanter twins aren't members of their parents' cult and have no other friends, since they are privately tutored and rarely allowed to leave the estate. Around strangers, Terenzio becomes suspicious and meek, while Elzerina seems brash and outgoing. Both children are incredibly excited to meet friendly strangers and treat their \"new friends\" to a trip around the house. They help the characters sneak through the villa, since the children know they aren't supposed to have guests."
> — `sources/adventure-wdh.json:18418` (Terenzio and Elzerina, page 116; the Ammalia notes cite 18417, which is the "entries" key line)

**Adventure, household knowledge of the attic (servants)**
> "With the exception of their personal attendants, the Cassalanters replenish their servants regularly. Most move on to other jobs, but occasionally a servant discovers the secret vault ({@area C29|330}), visits the forbidden attic ({@area C24|325}), or otherwise learns too much. Such folk are fated to become sacrifices to Asmodeus."
> — `sources/adventure-wdh.json:18598`

**Campaign, who knows what is in the attic (quest opener and room notes)**
> "The household staff knows the attic is forbidden. Only Willifort Crowelle — the doppelganger butler who serves Asmodeus directly — knows what is behind the door."
> — `campaign/structure/arc-g-cassalanter-villa.md:13`

> "Lissette the upstairs maid mentions hearing Ammalia crying after she visits \"the top floor.\" The twins' caretaker Nana Rosse knows \"something terrible\" lives in the attic. Neither has been inside."
> — `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:35`

**Campaign, who runs the household**
> "- **Chain of command:** Ammalia makes the final calls for the family and the cult, and Victoro, who leads the worship, has stopped questioning her. Willifort Crowelle links the family to everyone who works for it. He runs household security, reports to Ammalia and directs the spy and the poisoner. Seffia Naelryke commands the field team and answers to Victoro, and the head servants keep order at the rites."
> — `campaign/setting/organizations/10-cassalanters.md:51`

### A7. Parental contact (Ammalia weekly; Victoro not in months)

**Campaign, Ammalia's visits (Osvaldo page, Morale; the conflict is D2)**
> "**Morale.** Osvaldo attacks anything that enters the attic except Ammalia. Her presence calms him enough for her to read from outside the shielding circle, but she does not go into the room."
> — `campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md:23`

**Campaign, Ammalia's visits (Ammalia page, Persona)**
> "She also goes to the attic where Osvaldo is bound, and reads him his favorite stories from a chair placed just outside the shielding circle while he curses her name and pleads with her to save him."
> — `campaign/setting/notable-figures/cassalanters/02-ammalia-cassalanter.md:22` (the sentence sits in the Persona line, which opens "**Persona.** To the world, Ammalia is well-mannered, well-read, well-traveled, and known for driving a hard bargain.")

**Campaign, Victoro's absence (Victoro page, Persona)**
> "He has not entered the attic where Osvaldo is in months and cannot bring himself to go; that vigil belongs to Ammalia."
> — `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:22` (the sentence sits in the Persona line)

**Campaign, Victoro's absence (History, GM)**
> "- Osvaldo is a chain devil held in the soundproofed attic of the villa, room C24, never the basement or the temple. Ammalia visits weekly and sits in the room outside the pentagram. Victoro has not entered in months. Willifort knows. Two imps are always present."
> — `campaign/setting/history/05-a-debt-in-blood.md:50`

**Campaign, Victoro's absence (Villains, Relationships row)**
> "| Osvaldo | Eldest child (transformed) | Chain devil imprisoned in C24 (the soundproofed villa attic); Ammalia visits weekly, sitting outside the pentagram to read aloud while Osvaldo spits curses at her and weeps; Victoro has not visited in months |"
> — `campaign/setting/villains/cassalanters.md:57`

**Adventure, Victoro's guilt**
> "The soul of Victoro's eldest son, Osvaldo, is forever lost and can't be saved. To allay his guilt, Victoro has forged a plan to win back the souls of his young twins, Terenzio and Elzerina. Under the terms of the contract, their souls will be forfeit on their ninth birthdays, and that day is fast approaching. But Victoro can buy his way out of the obligation by providing, as the contract states, \"one shy of a million gold coins and the sacrifice of one shy of a hundred unfortunate souls.\""
> — `sources/adventure-wdh.json:32693` (Appendix B, "Victoro Cassalanter"; the soul line is D5)

### A8. Osvaldo's own life in the attic (campaign persona; the inner life is also in G)

**Campaign, the Persona (Osvaldo page)**
> "**Persona.** To the world, Osvaldo Cassalanter is a name the family does not mention — \"attending school in a faraway city,\" Terenzio and Elzerina were told. To those who open the attic door, he is a chain devil in a soundproofed attic who attacks immediately, and whose chains have a 15-foot reach. Deep down, some fragment of Osvaldo is still there, and it hears his mother's voice when she comes to read, and it is very much aware of what was done to it."
> — `campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md:21` ("15-foot reach" has no source, see F6; "attacks immediately" conflicts with the room notes, see D3)

**Campaign, the Motivations (Osvaldo page)**
> "**Motivations.** The chain devil wants to escape, attack, and destroy anything that enters the attic. The fragmented self wants to understand what happened to him and make contact with the siblings he cannot see."
> — `campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md:15`

### A9. Soul status (the contract; campaign and adventure disagree, see D5)

**Adventure, "forever lost" and "no hope"**
> "The soul of Victoro's eldest son, Osvaldo, is forever lost and can't be saved." — `sources/adventure-wdh.json:32693`
> "Now a creature of pure evil and hate, he has no hope of regaining what was taken from him." — `sources/adventure-wdh.json:32474`

**Campaign, the contract-destruction path (quest-time; freed soul)**
> "**Path 2 — Destroy the Infernal Contract (Mace of Disruption).** ... Osvaldo's chain devil form dissolves — he dies, but his soul is freed."
> — `campaign/structure/arc-g-cassalanter-villa.md:149` (the full paragraph is in section C)

> "If the infernal contract is later destroyed (see A7 — mace of disruption), Osvaldo's death is retroactively a mercy: his soul, no longer contracted, is freed. If the contract is not destroyed, his soul belongs to Asmodeus."
> — `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:31`

### A10. Dates and ages (derived unless noted)

- Age at taking: nine (`campaign/setting/history/05-a-debt-in-blood.md:137`; `campaign/structure/arc-g-cassalanter-villa.md:9`: "Osvaldo, their eldest, already nine, the age at which the contract claims each child").
- Present age: twelve (`campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md:25`: "twelve now"; `campaign/setting/history/05-a-debt-in-blood.md:49`: "Osvaldo, the eldest, was nine when he was taken, and is now twelve.").
- Wiki: "| age            = " (blank, wiki line 17).
- Wiki: "| dob            = " (blank, wiki line 21).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, the Osvaldo page: "- *Tethyrian human (chain devil), lawful evil, he/him*. Stat block: **Chain Devil**." — `campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md:5`
- Campaign, the Organization page: "- **Osvaldo Cassalanter** — Tethyrian human (chain devil), lawful evil. The Cassalanters' eldest son, now a **chain devil**, chained in the soundproofed attic of the Villa (room C24). The pact's first cost. Victoro and Ammalia have told no one. See the **Osvaldo Cassalanter** page in Notable Figures." — `campaign/setting/organizations/10-cassalanters.md:96`
- Campaign, the Session 51 ruling (Draft Notes): "> - **Settled by the user (Session 51):** Osvaldo's alignment. *Dragon Heist* gives only \"chain devil\", and a standard chain devil is lawful evil. The page and his Notable Figures page now say lawful evil, and \"formerly lawful good\" is dropped." — `campaign/setting/organizations/10-cassalanters.md:183`
- Adventure: no alignment in Appendix B (`sources/adventure-wdh.json:32470`-`:32481`). The only type line is "Osvaldo is a {@creature chain devil}." (`:32481`).
- Wiki: "| alignment5e    = " (blank), and the other alignment fields are blank (wiki lines 40-57).

**Species**
- Campaign: "Tethyrian human (chain devil)" (`campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md:5`; `campaign/setting/organizations/10-cassalanters.md:96`). "Tethyrian" is not in any source for him (see D8).
- Adventure: "Stripped of his humanity, Osvaldo was chained up in Cassalanter Villa and slowly transformed into a devil" (`sources/adventure-wdh.json:32474`). The adventure calls him "a {@creature chain devil}" (`:20663`, `:32481`).
- Wiki: "| race           = [[Human]]" (wiki line 14); "[[Category:Humans]]" (wiki line 86); "[[Category:Kytons]]" (wiki line 85).

**Pronouns**
- Campaign: "he/him" (`campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md:5`).
- Adventure: "He is trying desperately to get someone to hear him and come to his rescue." (`sources/adventure-wdh.json:20661`); "His empty shell of a body has been transformed" (`:20663`).
- Wiki: "| sex            = Male" (wiki line 13).

**Stat block**
- Campaign, the Osvaldo page: "Stat block: **Chain Devil**." (`campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md:5`)
- Campaign, the room: "He has the statistics of a chain devil." (`campaign/locations/cassalanter-villa/08-osvaldos-prison.md:21`)
- Campaign, the structure doc: "Chain devil (Osvaldo) per MM." (`campaign/structure/arc-g-cassalanter-villa.md:434`; the Bestiary is not drafted)
- Adventure: "Osvaldo is a {@creature chain devil}." (`sources/adventure-wdh.json:32481`, "Game Statistics", page 214)
- Alexandrian Lair, stat reference, printed p.82 [PDF p.6] (transcription): "Oslando Cassalanter – chain devil, MM p. 72" (the name is misspelt in the source; see D9)

**Wiki infobox fields (5e, cited `WDH5e-p116`, `WDH5e-p124`, `WDH5e-p193-194`)**
- wiki line 11: "| home           = [[Sea Ward of Waterdeep|Sea Ward]], [[Waterdeep]]"
- wiki line 21: "| dob            = " (blank)
- wiki line 25: "| death          = 1489"
- wiki line 26: "| deathnotes     = (soul claimed by [[Asmodeus]]; body turned into a [[chain devil]])<ref name=\"WDH5e-p116\">{{Cite book/Waterdeep: Dragon Heist|116}}</ref>{{Waterdeep-time}}"
- wiki line 29: "| parents        = [[Ammalia Cassalanter]]<br />[[Victoro Cassalanter]]"
- wiki line 31: "| siblings       = [[Elzerina Cassalanter]]<br /> [[Terenzio Cassalanter]]"

---

## C. Sentences on the current page that narrate quest-time or depend on a discovery

Current page: `campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md`. The page has no Background, Personality or Connections section yet. Each row says whether the sentence is day-one, and where its fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L5 | "*Tethyrian human (chain devil), lawful evil, he/him*. Stat block: **Chain Devil**." | Day-one. "Tethyrian" `[research]` (D8) | Section B |
| 2 | L6 | "- **Affiliation:** The Cassalanters" | Day-one. The organization page gives no affiliation label for him. "cult" is not sourced (A6) | `campaign/setting/organizations/10-cassalanters.md:96`; A6 |
| 3 | L7 | "- **Featured in:** Cassalanter Villa, Cassalanter Villa (location)" | Quest references. No quest journal names Osvaldo (see Not found) | `campaign/structure/arc-g-cassalanter-villa.md:433`; `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:1` |
| 4 | L11 | "**Resonance.** Osvaldo should inspire horror when the party realizes what the howling is; genuine sorrow for the boy in the portrait with the ceremonial rapier; and cold terror when the chain devil is encountered in the flesh." | Two clauses are discovery or encounter time: "when the party realizes" (the same pattern as Ammalia's "when they learn", Ammalia notes row 4; no source gives the discovery) and "when the chain devil is encountered in the flesh". The portrait clause is day-one (`sources/adventure-wdh.json:20330`) | Encounter: `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:21`-`:29`; discovery: `campaign/structure/arc-g-cassalanter-villa.md:159` ("The Cooperative Discovery Path") |
| 5 | L13 | "**Emotions.** Osvaldo most often feels the chain devil's rage against confinement, fragmented grief for a life that ended at nine, desperate pleading when Ammalia visits, a hatred of his own condition that sometimes expresses as hatred of everything, and the specific anguish of knowing his siblings are scheduled for the same fate." | Day-one habits, except "the specific anguish of knowing his siblings are scheduled for the same fate": no source says Osvaldo knows the twins' fate (see F5 and D12) | "ended at nine": `campaign/setting/history/05-a-debt-in-blood.md:49`; "desperate pleading when Ammalia visits": `sources/adventure-wdh.json:20661` ("trying desperately to get someone to hear him"), with the visits in `campaign/setting/organizations/10-cassalanters.md:129`; "knowing": none |
| 6 | L15 | "**Motivations.** The chain devil wants to escape, attack, and destroy anything that enters the attic. The fragmented self wants to understand what happened to him and make contact with the siblings he cannot see." | Day-one for the sibling clause. "attack, and destroy anything that enters the attic" is the encounter behaviour (D3). Motivations are kept verbatim per ruling 3 | `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:23`; A8 |
| 7 | L17 | "**Inspirations.** When playing Osvaldo, channel the Beast (*Beauty and the Beast*, before the transformation reversed), Bertha Mason (*Jane Eyre*), and the Hulk (*Marvel*, the monster who remembers being someone else)." | Not a fact | n/a |
| 8 | L21 | "**Persona.** To the world, Osvaldo Cassalanter is a name the family does not mention — \"attending school in a faraway city,\" Terenzio and Elzerina were told. To those who open the attic door, he is a chain devil in a soundproofed attic who attacks immediately, and whose chains have a 15-foot reach. Deep down, some fragment of Osvaldo is still there, and it hears his mother's voice when she comes to read, and it is very much aware of what was done to it." | The public part is day-one (A5). "To those who open the attic door ... attacks immediately" is encounter time (room notes at `08-osvaldos-prison.md:27`, D3). "15-foot reach" has no source (F6). "hears his mother's voice when she comes to read" is a day-one habit ("Mama?" at `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:21`) | `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:27`; `sources/adventure-wdh.json:20661`; "Mama?" at `08-osvaldos-prison.md:21` |
| 9 | L23 | "**Morale.** Osvaldo attacks anything that enters the attic except Ammalia. Her presence calms him enough for her to read from outside the shielding circle, but she does not go into the room." | Encounter behaviour and a conflict. "calms him enough" conflicts with the adventure and the Villains page (D2). "attacks anything that enters the attic" conflicts with the pentagram rule and the room notes (D3). The "does not go into the room" clause is day-one (`sources/adventure-wdh.json:20653`) | `sources/adventure-wdh.json:20661`, `:20665`; `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:27`; `campaign/setting/villains/cassalanters.md:57` |
| 10 | L25 | "**Relationships.** Osvaldo is the eldest child of Victoro and Ammalia (taken at nine, twelve now, his soul surrendered to Asmodeus three years ago during the family's financial crisis), the reason Terenzio and Elzerina are forfeit on their ninth birthday, Flamerule 11, 1492 DR (the pact requires both 999,999 gp and ninety-nine souls), and the tragedy that both explains and indicts everything his parents are doing." | Day-one. "forfeit on their ninth birthday, Flamerule 11" is a calendar fact (`campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:69`); the adventure says "ten days after Founders' Day" (`sources/adventure-wdh.json:18294`). The soul half of the buy-out is a day-one term; its resolution is quest-time (row 14 of routing, Section E) | `campaign/setting/organizations/10-cassalanters.md:47`; `campaign/setting/villains/cassalanters.md:25` |
| 11 | L29 | "Osvaldo Cassalanter is the family's eldest son — absent from public life, said to be attending school in a faraway city, and not a subject his parents discuss with guests." | Day-one public face. **29 words** (brief limit 21). Conflicts with the adventure's public "disappearance" wording (D6) | `campaign/setting/villains/cassalanters.md:80`; `campaign/setting/organizations/10-cassalanters.md:110` |

**Voice profile (`.claude/skills/character-voices/voices/cassalanters.md`, "### Osvaldo Cassalanter" at lines 67-81)**

The file's secrecy header says the "after discovery" register is "used only once the party has found the truth (villain Phase 2 onward, or when the character is confronted in the temple)" (`.claude/skills/character-voices/voices/cassalanters.md:3`). The Osvaldo profile has no "after discovery" register. Its lines, with status:

> "- **Sentence shape:** The devil: snarls and fragments. The boy: broken pleading, half-sentences, names." — line 71 (day-one)

> "- **Swearing:** *Punctuation · Colourful · Tirade.* The devil is a torrent of filth at anyone who enters (\"Come closer, you soft little cunt, let me wrap you in iron!\"). The boy never swears. Tirade (the devil): \"Come closer, you soft, bleating, chain-dodging, gutless, fucking meat, come closer so I can wrap you in iron and listen to you break!\"" — line 73. The swearing stays (adult table). "at anyone who enters" is encounter time (D3).

> "- **Sound:** A metallic, grinding roar. Now and then a twelve-year-old boy's cracked voice breaks through, and then it's gone." — line 70 (day-one)

> "*Greeting:* A roar, and chains striking the door." — line 79. Encounter time (the greeting to someone at the door).

> "*The boy:* \"Is that — please. Are Terenzio and Elzi safe? Tell me they're not coming here.\"" — line 80. The line presupposes someone at the door. The sibling worry is day-one (`campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md:13`); the knowledge behind it is a gap (F5).

> "*Under pressure:* \"Closer! Closer, and I'll show you what she made me!\"" — line 81. Encounter time. "what she made me" is a grievance against Ammalia (day-one; see G).

> "- **Personality in speech:** Rage against confinement, with fragments of grief. The boy is desperate for contact with the twins." — line 74 (day-one)

> "- **Quirks:** Chains rattle in time with the words. The boy's voice only breaks through at the name \"Osvaldo\"." — line 75 (day-one)

> "- **Signature phrases:** Devil: \"Closer.\" / Boy: \"Mother, please.\" / \"Are they safe?\"" — line 76 (day-one; "Closer" is an encounter word)

> "- **Never:** The devil never shows mercy. The boy never wants to hurt anyone." — line 77 (day-one)

Quest-time or encounter clauses in the profile, for the rule-16 restatement (none changed yet; the drafter will report changes): lines 73 ("at anyone who enters"), 79 (Greeting), 80 (sample line presupposing a visitor), 81 (Under pressure). Line 76 ("Closer") is the devil's encounter word.

**Routing for the quest-time text (Cassalanter Villa heist; no quest journal exists)**
- `campaign/structure/arc-g-cassalanter-villa.md:75`: "**Caravance (Tarsakh 1).** Gift-giving holiday. The Cassalanters give most staff the night off to celebrate privately with their children. A skeleton crew remains: perimeter guards, Willifort, imp watchers on Osvaldo's door. The primary heist window: minimal staff, the Cassalanters emotionally focused on the twins. After the children sleep, cultists arrive for a midnight gathering in the temple — the Cult Gathering adversary roster applies from midnight to dawn."
- `campaign/structure/arc-g-cassalanter-villa.md:161`: "- **Osvaldo in C24** — seeing a chain devil imprisoned in a warded attic room, weeping and clawing walls, establishes that the Cassalanters have an infernal connection that cost them a child."
- `campaign/structure/arc-g-cassalanter-villa.md:205` and `:207`: the C24 room and the dispel-death (A4; G).
- `campaign/structure/arc-g-cassalanter-villa.md:315`: "**Tone.** The complications carry moral weight. Confronting Osvaldo is horror. Confronting the Cassalanters is tragedy. ..."
- `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:11`-`:35`: the whole "Heist — Cassalanter Villa Only" room (dispel, death, the interaction options; see G).
- `campaign/locations/cassalanter-villa/16-ceremonial-hall.md:35`: "- The children's souls are freed. Osvaldo's chain devil form, if still alive, dissolves — he dies, but his soul is freed"
- `campaign/structure/arc-g-cassalanter-villa.md:157`: "**Path 4 — Expose the Cassalanters.** ... The children's souls are forfeit — Asmodeus claims them on their birthday. They become lemures. ..."
- `campaign/structure/arc-g-cassalanter-villa.md:351`: "*Exposed.* Evidence delivered to the Masked Lords. Cassalanters arrested or fled. Cult disbanded. Children's souls forfeit on their birthday — Asmodeus claims them. They become lemures. Victoro and Ammalia vow to destroy those who thwarted them (from prison or exile). Banking operations disrupted, affecting guild debts across the city."
- `campaign/structure/arc-g-cassalanter-villa.md:439`: "- **Undermountain (future)** — Asmodean retribution from Path 2 (contract destruction) seeds Vanrakdoom, Level 18. The Stone's 2-Eye upgrade intensifies the Mad Mage seed from **Xanathar's Lair**. Osvaldo's freed soul may appear in the afterlife mechanics."
- Adventure: `sources/adventure-wdh.json:22888`: "If the Cassalanters fail to obtain the {@item Stone of Golorr|WDH}, the following events don't come to pass. As a consequence, Terenzio and Elzerina are transformed into {@creature lemure||lemures} as their souls are forfeit ten days after Founders' Day. Shattered by their failure and their loss, Victoro and {@creature Ammalia Cassalanter|WDH} vow to destroy those who thwarted them." (Special Events, page 130; the condition is the Stone, see D10)
- Adventure: `sources/adventure-wdh.json:22918`: "While Ammalia plays host, Victoro instructs his cultists to remove the sacks of gold from House Cassalanter's vault ({@area C29|330}) and hurl them into the sacrificial bowl ({@area A7|345}). They finish shortly before midnight. At the stroke of midnight, as the poison does its work, Ammalia keeps an eye on her wealthy guests and orders Tessina Khyret to notify Victoro that the deed is done. Standing before the statue of Asmodeus in the temple, Victoro summons a {@creature barbed devil} and informs it that payment has been made in full. The devil declares (in Infernal) that the payment is \"satisfactory\" and informs Victoro that the souls of Terenzio and Elzerina will not be taken to the Nine Hells. It then disappears whence it came, leaving the Cassalanters to bask in their triumph." (the feast's resolution; the gold and the souls are quest-time)
- Lair PDF, printed p.79 [PDF p.3] (transcription): "The only people left in the Villa during this time, beyond the Cassalanters themselves, are: • The guards • Willifort Crowell • The imps guarding Osvaldo Cassalanter" (Tarsakh 1, Caravance)
- Lair PDF, printed p.81 [PDF p.5] (transcription; roster): "2 imps + Osvaldo Cassalanter", listed against the rooms, with "Area C24 – Osvaldo's Prison"

**Trollskull Alley (twins' timing, quest-time; see E4)**
- `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:54`: "Ammalia arrives without Lord Cassalanter. She brings her twins, Terenzio and Elzerina, and their tiefling nanny, Nana Rosse."
- `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:120`: "Mark **Cassalanter Twins Met** when any character speaks with Terenzio or Elzerina."

---

## D. Conflicts

Rank used: campaign files first, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.

**D1. How she reads to Osvaldo: "shielding circle", "warded door" or "pentagram"**
- Osvaldo page: "Her presence calms him enough for her to read from outside the shielding circle, but she does not go into the room." — `campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md:23`
- Ammalia page: "a chair placed just outside the shielding circle" — `campaign/setting/notable-figures/cassalanters/02-ammalia-cassalanter.md:22`
- Gazetteer: "from a chair outside his shielding circle" — `campaign/gazetteer/waterdeep/sea-ward.md:113`
- Structure doc: "Ammalia reads to her son weekly through the warded door" — `campaign/structure/arc-g-cassalanter-villa.md:13`
- Villains: "sitting outside the pentagram" — `campaign/setting/villains/cassalanters.md:57`
- Organization: "Ammalia visits weekly, sitting in the room outside the pentagram to read to him while he curses her and weeps." — `campaign/setting/organizations/10-cassalanters.md:129`
- History: "Ammalia visits weekly and sits in the room outside the pentagram." — `campaign/setting/history/05-a-debt-in-blood.md:50`
- Location: "Observe without entering the pentagram" — `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:27`
- Adventure: "A 10-foot-diameter pentagram has been burned into the floor around him." — `sources/adventure-wdh.json:20663`; "the effect ends if another creature enters the area encompassed by the pentagram" — `:20665`. The adventure never says "shielding circle" (the only "shielding" in the file is "ring of mind shielding", `:32768`).
- Result: "shielding circle" is in three campaign files (the Osvaldo page, the Ammalia page and the gazetteer), and those three agree with each other. "warded door" is in the structure doc only. "pentagram" is in the Villains, Organization, History and location files and in the adventure. The published text is the higher source for the physical object (a pentagram with abjuration magic). The Notable Figures pages are higher than the structure doc. The page keeps "shielding circle" per the Ammalia notes (D2 there), and the drafter should note the adventure's word.

**D2. Does Ammalia's visit calm him, or does he curse her?**
- Osvaldo page: "Her presence calms him enough for her to read from outside the shielding circle, but she does not go into the room." — `campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md:23`
- Adventure: "If one or both of his parents are here, he spits curses at them as they weep before him." — `sources/adventure-wdh.json:20661`
- Villains: "Ammalia visits weekly, sitting outside the pentagram to read aloud while Osvaldo spits curses at her and weeps" — `campaign/setting/villains/cassalanters.md:57`
- Organization: "Ammalia visits weekly, sitting in the room outside the pentagram to read to him while he curses her and weeps." — `campaign/setting/organizations/10-cassalanters.md:129`
- Ammalia page: "while he curses her name and pleads with her to save him" — `campaign/setting/notable-figures/cassalanters/02-ammalia-cassalanter.md:22`
- Higher source: the campaign files (Villains, Organization, Ammalia page) and the adventure all say he curses her. The Osvaldo page's "calms him" is the outlier.

**D3. Who he attacks, and when**
- Osvaldo page: "To those who open the attic door, he is a chain devil in a soundproofed attic who attacks immediately" (line 21); "Osvaldo attacks anything that enters the attic except Ammalia." (line 23)
- Pentagram rule (adventure): "A successful {@dc 15} Intelligence (Arcana) check reveals that the pentagram prevents Osvaldo from manipulating his chains, and that the effect ends if another creature enters the area encompassed by the pentagram." — `sources/adventure-wdh.json:20665`
- Imps (adventure): "They attack anyone who tries to free Osvaldo or threatens other family members present." — `:20662`
- Room notes (campaign, heist): "*Observe without entering the pentagram:* The party can watch. Osvaldo is aware of them — his brass-tinted eyes track movement. He does not attack at range." — `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:27`
- Room notes: "They attack if Osvaldo is directly threatened or if the party attempts to dispel the containment wards." — `08-osvaldos-prison.md:23`
- Higher source: no file settles it. The campaign room notes govern heist behaviour, and they say he "does not attack at range". The Osvaldo page's "anything that enters the attic" is wider than the adventure's pentagram rule and the room notes. The drafter must choose one wording.

**D4. Has Victoro entered the room since the transformation?**
- Structure doc: "Victoro sealed the attic with abjuration wards, soundproofed the floor, and has not entered the room since." — `campaign/structure/arc-g-cassalanter-villa.md:13`
- Victoro page: "He has not entered the attic where Osvaldo is in months and cannot bring himself to go; that vigil belongs to Ammalia." — `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:22`
- Organization: "Victoro has not visited in months." — `campaign/setting/organizations/10-cassalanters.md:129`
- Villains: "Victoro has not visited in months" — `campaign/setting/villains/cassalanters.md:57`
- History: "Victoro has not entered in months." — `campaign/setting/history/05-a-debt-in-blood.md:50`
- Higher source: the campaign's Notable Figures and history pages ("in months"). The structure doc says "since". The page uses "in months".

**D5. Soul status: forever lost, or freed on contract destruction**
- Adventure: "The soul of Victoro's eldest son, Osvaldo, is forever lost and can't be saved." — `sources/adventure-wdh.json:32693`
- Adventure: "Now a creature of pure evil and hate, he has no hope of regaining what was taken from him." — `:32474`
- Structure doc (Path 2): "Osvaldo's chain devil form dissolves — he dies, but his soul is freed." — `campaign/structure/arc-g-cassalanter-villa.md:149`
- Room notes: "If the infernal contract is later destroyed (see A7 — mace of disruption), Osvaldo's death is retroactively a mercy: his soul, no longer contracted, is freed. If the contract is not destroyed, his soul belongs to Asmodeus." — `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:31`
- Higher source: the campaign (the freed soul is a Path 2 outcome). The adventure's "can't be saved" is the adventure's day-one view. A day-one page must not say either outcome as fact. The Osvaldo page says nothing about his soul's future.

**D6. Public story: a disappearance, or a school**
- Adventure: "The disappearance of their eldest son (and heir apparent) earned them sympathy." — `sources/adventure-wdh.json:18295`; "Victoro and Ammalia's eldest son disappeared three years ago when the family was on the verge of bankruptcy." — `:18403`
- Campaign, Osvaldo page: "a name the family does not mention" (line 21); "not a subject his parents discuss with guests" (line 29)
- Campaign, Organization: "The city hears that Osvaldo studies in a faraway city" (line 26); "Their eldest son is said to be at school in a faraway city" (line 110)
- Campaign, Villains: "said to be studying in a faraway city, and the family does not often speak of him" (line 80)
- Higher source: the campaign (the public story is school). The adventure's word "disappeared" is in its public overview. The campaign does not say the public knows he disappeared. The drafter should not say the public knows of a disappearance.

**D7. Osvaldo's age in the family portrait, and the signing phrase**
- Adventure: "a 7-foot-tall portrait of Lord and Lady Cassalanter holding two infant children and standing beside their teenage son, Osvaldo." — `sources/adventure-wdh.json:20039`
- Campaign derived birth: "1480 DR: Osvaldo is born. This is derived from his ninth year in 1489 DR and is stated by no source." — `campaign/setting/history/05-a-debt-in-blood.md:124`; the twins are born "1483 DR" (`:125`). If Osvaldo is three years older than the infant twins, he is not a teenager beside them. The adventure's "teenage son" and "two infant children" cannot both be squared with the derived birth years. Not resolved.
- Adventure: "When they were young, Ammalia and Victoro signed a contract with the archdevil" (`:31715`) against "Three years ago, they traded away the souls of their children" (`:18294`). The history page follows "three years ago" (`campaign/setting/history/05-a-debt-in-blood.md:139`).

**D8. Species and ethnicity**
- Campaign: "Tethyrian human (chain devil)" — `campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md:5`
- Wiki: "| race           = [[Human]]" (wiki line 14); "[[Category:Humans]]" (line 86)
- Adventure: no ethnicity for him. "chain devil" (`:32481`).
- Wiki: "[[Category:Kytons]]" (line 85). A kyton is not a chain devil. The wiki category is not a campaign claim.
- Result: "human" is wiki-sourced, and the adventure's "humanity" (`:32474`) implies it. "Tethyrian" is `[research]`. "chain devil" is the adventure's type.

**D9. The name "Oslando" in the Alexandrian Lair**
- Lair PDF, printed p.82 [PDF p.6] (transcription): "Oslando Cassalanter – chain devil, MM p. 72", and "(*GM Note*: That was Oslando on a particularly bad day.)"
- Adventure: "{@creature Osvaldo Cassalanter|WDH}" (`:20661`); "Osvaldo" (`:32470`).
- Higher source: the adventure and campaign. Check the PDF's text layer before any citation.

**D10. Which condition decides the twins' fate: the Stone, or the gold? (the adventure's own conflict)**
- Adventure: "If the Cassalanters fail to obtain the {@item Stone of Golorr|WDH}, the following events don't come to pass. As a consequence, Terenzio and Elzerina are transformed into {@creature lemure||lemures} as their souls are forfeit ten days after Founders' Day." — `sources/adventure-wdh.json:22888`
- Adventure: "This event occurs only if the Cassalanters obtain the gold from the Vault of Dragons." — `:22915`
- Adventure: "The Cassalanters have most of the coin they need, but they require the gold from the Vault of Dragons to buy their children's salvation without bankrupting themselves." — `:18296`
- Campaign: the gold is the condition (Structure, Path 1: "They need the Vault of Dragons' 500,000 GP to complete the financial component." — `campaign/structure/arc-g-cassalanter-villa.md:147`).
- Higher source: the campaign (gold). The adventure's line 22888 names the Stone. The campaign files do not settle it.

**D11. Who the imps answer to**
- Adventure: "They answer to Lord Cassalanter" — `sources/adventure-wdh.json:20662`
- Room notes: "reporting to Ammalia through a one-way telepathic bond." — `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:23`
- Higher source: the campaign (Ammalia). The Organization page (`campaign/setting/organizations/10-cassalanters.md:129`: "Two imps are always present.") and the History page (`campaign/setting/history/05-a-debt-in-blood.md:50`: "Two imps are always present.") do not name the imps' master.

**D12. Who knows about Osvaldo in the house**
- Organization: "Victoro and Ammalia have told no one." — `campaign/setting/organizations/10-cassalanters.md:96`
- Structure doc: "The household staff knows the attic is forbidden. Only Willifort Crowelle — the doppelganger butler who serves Asmodeus directly — knows what is behind the door." — `campaign/structure/arc-g-cassalanter-villa.md:13`
- Room notes: "The twins' caretaker Nana Rosse knows \"something terrible\" lives in the attic." — `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:35`
- Organization: "Willifort knows." — `campaign/setting/organizations/10-cassalanters.md:129`
- Lair PDF p.82 [PDF p.6] (transcription): "When working on the third floor once, they heard horrible screams coming from above them on the roof."
- Result: "told no one" is an organization-level simplification. The structure doc and room notes say staff, Nana Rosse and Willifort know of the attic. The page should say what the family told the twins and the public.

**D13. The attic door: locked, or unlocked from the corridor?**
- Adventure: "Otherwise, it's locked shut, and Victoro and Ammalia carry the only keys." — `sources/adventure-wdh.json:20653`
- Room notes: "The attic door is not locked from the corridor side." — `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:9`
- Room notes, the exterior door: "**Exterior attic door lock:** DC 19 Dexterity (Thieves' Tools)." — `08-osvaldos-prison.md:5`
- Higher source: the campaign (location journal, heist). Drafter note only.

**D14. Calendar: the twins' birthday (Flamerule 11, or Tarsakh 11)**
- Campaign: "Flamerule 11, 1492 DR: the twins' ninth birthday and the contract's due date, \"ten days after Founders' Day\" in the published adventure." — `campaign/setting/history/05-a-debt-in-blood.md:128`
- Campaign (Trollskull ev-06): "either twin tells anyone who asks their age that they turn nine on the eleventh of Flamerule." — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:89`
- Alexandrian Lair, printed p.79 [PDF p.3] (transcription): "TARSAKH 11th – THE TWINS' BIRTHDAY: The twins' ninth birthday, on which Asmodeus will claim their souls."
- Higher source: the campaign and the adventure (Flamerule 1 and 11; `sources/adventure-wdh.json:31447`: "Flamerule 1: Founders' Day"). The history page records the Lair's Tarsakh dates as overruled (`campaign/setting/history/05-a-debt-in-blood.md:138`).

---

## E. Stale lines in other files (not to be edited), and routed references

### E1. Stale or retired files

- `campaign/structure/ch2-city-of-splendors.md:115` (retired file, do not use): "The proof of contract: souls claimed one at a time; Osvaldo, the eldest, was seventeen; he is now in his early thirties and is a chain devil living in the temple beneath his parents' villa; they visit him"
- `campaign/structure/ch2-city-of-splendors.md:284`: "| Osvaldo | Eldest child (transformed) | Chain devil; the Cassalanters know where he is; they visit; the DM decides what these visits look like |"
  (The retired file gives age 17 at the taking and "the temple" as his place. Both are contradicted by the current files, which say nine and room C24 in the attic.)
- `sources/research/pass4-bundles/cassalanters/campaign-hits.txt:86` (a snapshot copy of `campaign/guides/gm-guide/about-this-campaign.md:78`): "> - Osvaldo Cassalanter was a person before he was a chain devil. He was nine when he was taken. His mother still visits him." The current GM Guide line reads "Osvaldo Cassalanter was a person before he was a chain devil. He was nine when he was taken and is twelve now. His mother still visits him each week." (`campaign/guides/gm-guide/about-this-campaign.md:78`)
- `campaign/setting/history/05-a-debt-in-blood.md:140`: "`04-osvaldo-cassalanter.md` line 26 (\"or\" for \"and\")". The current page's line 25 has no such "or". The history note is out of date.

### E2. Setting pages that touch him

- `campaign/gazetteer/waterdeep/sea-ward.md:113`: "from a chair outside his shielding circle" (see D1; the gazetteer is a setting page, so the term matters).
- `campaign/setting/deities/asmodeus.md:64`: "- **Never reveal:** That the Cassalanters worship him, the pact and the soul contract, the ninety-nine poisoned guests, Osvaldo's fate, or that Jarlaxle knows through Vessa."
- `campaign/setting/deities/asmodeus.md:74`: "- **What was already paid:** Osvaldo, the eldest, was taken at nine, the age at which the contract claims each child. He is now twelve and a chain devil. The twins, Terenzio and Elzerina, are eight and unaware of the bargain." (consistent with the Osvaldo page)

### E3. Routed quest references (where the quest-time facts already live)

- Cassalanter Villa structure doc: `campaign/structure/arc-g-cassalanter-villa.md:75`, `:149`, `:157`, `:161`, `:205`, `:207`, `:315`, `:351`, `:434`, `:439`
- C24 location journal: `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:11`-`:35` (the "Heist — Cassalanter Villa Only" room)
- Ceremonial hall (destruction): `campaign/locations/cassalanter-villa/16-ceremonial-hall.md:35`
- Area overview: `campaign/locations/cassalanter-villa/area-overview.md:23` ("- **Attic**: C24 (Osvaldo's prison)") and `:46` ("**Two imps in spider form** (C24, Osvaldo's prison): Passive observers. Attack if Osvaldo is threatened or freed.")
- Ammalia's study: `campaign/locations/cassalanter-villa/07-ammalias-study.md:7` ("A trapdoor in the floor, beneath a woven rug, opens to C23 — a short corridor leading to the attic stair (C24, Osvaldo's prison).")
- Trollskull Alley Grand Opening (the twins' first appearance; Event Outcome **Cassalanter Twins Met**): `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:54`, `:66`, `:89`, `:120`, `:137`-`:138`
- Adventure, Special Events and feast: `sources/adventure-wdh.json:22888`, `:22915`-`:22918`
- Adventure, C24 room: `sources/adventure-wdh.json:20649`-`:20665`
- Factions Guide list of Notable Figures (no quest text): `campaign/guides/factions/11-cassalanters.md:107`
- Alexandrian Lair: `sources/10. Lair  Cassalanter Villa.pdf` printed pp.79, 81, 82 (see C and D9)

### E4. Children timing note (the brief's request, org and villains pages)

- Villains, Relationships table: "| Terenzio and Elzerina | Surviving children | Twins, eight years old; don't know about the bargain; first appear at the **Trollskull Alley** Grand Opening, before PCs investigate the villa |" — `campaign/setting/villains/cassalanters.md:58`
- Villains, Key Design Note: "Terenzio and Elzerina must appear before **Cassalanter Villa**. They first appear at the **Trollskull Alley** Grand Opening, where Ammalia brings them with their nanny, Nana Rosse, and the party meets them again in the villa. The Grand Opening marks the Event Outcome **Cassalanter Twins Met** when any character speaks with either twin. Once the PCs have met the children, the Founders' Day deadline becomes personal rather than abstract." — `campaign/setting/villains/cassalanters.md:76`
- Villains, Draft Notes: "The twins now first appear at the Grand Opening, with their nanny Nana Rosse, in a fixed scene, and the party meets them again in the villa." — `campaign/setting/villains/cassalanters.md:132`
- Organization page: no Grand Opening note (a search of `10-cassalanters.md` for "grand opening" returned nothing). The organization page gives the twins' age ("are eight years old", `:47`) and their cult status ("belong to no cult", `:47`; `:35`), not their timing.
- Trollskull quest (current): `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:54` (twins present), `:120` (outcome). Consistent with the villains note.

---

## F. Gaps (what a Background would need that no source gives)

Each gap lists the sourced facts the drafter must stay consistent with.

1. **Birth, family of origin, childhood, schooling, early personality.** No campaign file and no adventure line. The only source facts: "heir apparent" (`sources/adventure-wdh.json:18295`; wiki line 62), the derived birth year 1480 DR (`campaign/setting/history/05-a-debt-in-blood.md:124`, "stated by no source"), and the childhood portrait "Twelve-year-old Osvaldo holding a ceremonial rapier" (`:20330`, a picture of his present age, not a date). Stay consistent with: "eldest child of Victoro and Ammalia" (`04-osvaldo-cassalanter.md:25`); "heir apparent of the Cassalanter family" (wiki line 62).
2. **Cult membership before 1489 DR, or ever.** No source. The cult roster (`campaign/setting/organizations/10-cassalanters.md:52`) gives six members, not him. The twins are not members (`sources/adventure-wdh.json:18418`). Stay consistent with: "Victoro and Ammalia have told no one." (`10-cassalanters.md:96`) and "The pact's first cost." (`10-cassalanters.md:96`).
3. **How he was taken, beyond "three years ago", "immediately", "nine", "1489 DR".** The adventure: "The soul of their eldest son, Osvaldo, was taken immediately." (`sources/adventure-wdh.json:18294`). The campaign: "The contract claims each child at nine, and Osvaldo, who was nine, was taken at once." (`10-cassalanters.md:26`). The date 1489 DR is derived: `campaign/setting/history/05-a-debt-in-blood.md:16`, `:133`.
4. **The first hours of the transformation.** The quest opener says he "screamed for three hours before the change completed" (`arc-g-cassalanter-villa.md:13`). That is the only source. It is a pre-campaign event and may be used as backstory.
5. **Whether he knows the twins' fate or the feast.** No source says he knows. The adventure says of the twins: "Neither knows the cruel fate that has befallen Osvaldo" (`:18456`), which is about them, not him. The page's "the specific anguish of knowing his siblings are scheduled for the same fate" (`04-osvaldo-cassalanter.md:13`) and the voice line "Tell me they're not coming here." (`.claude/skills/character-voices/voices/cassalanters.md:80`) are unsourced knowledge claims. Mark `[research]` or restate as his fear.
6. **"15-foot reach".** No source. Only `04-osvaldo-cassalanter.md:21` has it. The room notes give no reach. Stay consistent with: "He can't damage the house, nor can he break his own chains." (`sources/adventure-wdh.json:20664`).
7. **"Brass-tinted eyes".** Only `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:27` ("his brass-tinted eyes track movement"). No adventure or wiki line gives an eye colour. Stay consistent with the room notes.
8. **Whether he can ever be saved, and what he would feel about it.** The adventure says "forever lost and can't be saved" (`:32693`) and "no hope of regaining" (`:32474`). The campaign's Path 2 frees the soul (`arc-g-cassalanter-villa.md:149`). See D5. A day-one page can say what he wants and fears, not whether either outcome is true.
9. **Ammalia's stories.** "children's stories he loved before the contract" (`arc-g-cassalanter-villa.md:13`). No story is named in any file.
10. **Which imps guard him, and who they report to.** See D11.
11. **The twins' names for him, and his for them.** The voice file uses "Terenzio and Elzi" (`voices/cassalanters.md:80`). The adventure gives him no nickname. The twins' nicknames for each other are in the Trollskull entry (`campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:81`: "He calls her Elzi, and she calls him Ter."), which is a quest event file, not day-one lore.
12. **His personal wants.** No source gives a personal want beyond "trying desperately to get someone to hear him and come to his rescue" (`sources/adventure-wdh.json:20661`) and "make contact with the siblings he cannot see" (`04-osvaldo-cassalanter.md:15`). The rescue want is a quest-time hope (the room notes say he dies if the ward is dispelled, `08-osvaldos-prison.md:29`). Constraints for any `[design]` goal (brief ruling 17): no change to the contract outcome, no new Event Outcome, and nothing that makes his rescue a day-one fact.
13. **Chain devil appearance.** No source describes his face or body beyond "His empty shell of a body has been transformed into a chain devil that his parents have imprisoned using his own chains." (`sources/adventure-wdh.json:20663`) and "Osvaldo is a {@creature chain devil}." (`:32481`). The images on Lair PDF p.77 and Villains PDF p.18 show two children in front of two adults; they are not labelled Osvaldo.
14. **Pronouns.** Sourced (he/him). No gap.
15. **Species label "Tethyrian".** Unsourced; `[research]` (D8).

---

## G. Inner-life hints (exact quotes; for the Background and personal goals, brief ruling 17)

Each entry says whether the fact is day-one or quest-time. Quest-time facts are the heist's room text and the death or contract-destruction text, and they must not be stated as day-one fact.

**Loves and bonds**
> "Ammalia reads to her son weekly through the warded door — children's stories he loved before the contract, spoken to a chain devil who weeps black ichor and claws at the walls." — `campaign/structure/arc-g-cassalanter-villa.md:13` (day-one habit; the stories are ones "he loved before the contract")
> "Deep down, some fragment of Osvaldo is still there, and it hears his mother's voice when she comes to read, and it is very much aware of what was done to it." — `campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md:21` (day-one)
> "The fragmented self wants to understand what happened to him and make contact with the siblings he cannot see." — `04-osvaldo-cassalanter.md:15` (day-one)
> "The boy is desperate for contact with the twins." — `.claude/skills/character-voices/voices/cassalanters.md:74` (day-one)
> "He alternates between states — the chain devil's combat readiness, then a sudden stillness, then a child's voice: \"Mama?\" Then the chains lash again." — `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:21` (quest-time room text)
> "If he is reduced to 0 hit points, the chain devil cries out for his mother before melting into a pool of sickening black ichor." — `sources/adventure-wdh.json:20665` (quest-time: the combat death)

**Grudges and anger**
> "If one or both of his parents are here, he spits curses at them as they weep before him." — `sources/adventure-wdh.json:20661` (day-one)
> "Ammalia visits weekly, sitting in the room outside the pentagram to read to him while he curses her and weeps." — `campaign/setting/organizations/10-cassalanters.md:129` (day-one)
> "a hatred of his own condition that sometimes expresses as hatred of everything" — `04-osvaldo-cassalanter.md:13` (the page's own Emotions; no source line gives this)
> "Closer! Closer, and I'll show you what she made me!" — `.claude/skills/character-voices/voices/cassalanters.md:81` (encounter line; "what she made me" is a grievance against Ammalia; not restated)

**Fears and losses**
> "The Cassalanter heir apparent is a soulless abomination thanks to his parents' thoughtless greed." — `sources/adventure-wdh.json:20663` (day-one)
> "Stripped of his humanity, Osvaldo was chained up in Cassalanter Villa and slowly transformed into a devil (and an insane one at that)." — `sources/adventure-wdh.json:32474` (day-one)
> "He can only howl impotently at the misery being inflicted on him." — `sources/adventure-wdh.json:20664` (day-one)
> "The boy screamed for three hours before the change completed." — `campaign/structure/arc-g-cassalanter-villa.md:13` (pre-campaign)
> "fragmented grief for a life that ended at nine" — `04-osvaldo-cassalanter.md:13` (the page's own Emotions)
> "He can't damage the house, nor can he break his own chains." — `sources/adventure-wdh.json:20664` (day-one)

**Place and the people who visit**
> "He is trying desperately to get someone to hear him and come to his rescue." — `sources/adventure-wdh.json:20661` (day-one; the rescue is a quest outcome, see F12)
> "Lissette the upstairs maid mentions hearing Ammalia crying after she visits \"the top floor.\"" — `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:35` (day-one, staff gossip)
> "She's weeping before Osvaldo in the attic  ({@area C24|325})." — `sources/adventure-wdh.json:18352` (day-one table row, for the "91-00" range)
> "During an average day, she normally tended to her garden, smoked on the balcony, dismally watching the ocean, or wept at a transformed [[Osvaldo Cassalanter|Osvaldo]]'s feet in her [[House Cassalanter|mansion]]'s attic." — wiki line 67 (wiki, 5e)
> "Ammalia often wept at her transformed son's feet in the mansion's attic.<ref name=\"WDH5e-p116,125\">{{Cite book/Waterdeep: Dragon Heist|116,125}}</ref>" — wiki line 73 (wiki, 5e, cited pp.116, 125)

**Voice and manner (day-one)**
> "- **Personality in speech:** Rage against confinement, with fragments of grief. The boy is desperate for contact with the twins." — `voices/cassalanters.md:74`
> "- **Never:** The devil never shows mercy. The boy never wants to hurt anyone." — `voices/cassalanters.md:77`
> "*The boy:* \"Is that — please. Are Terenzio and Elzi safe? Tell me they're not coming here.\"" — `voices/cassalanters.md:80` (the boy's worry for the twins; the source for the knowledge is missing, see F5)

**Quest-time inner-life lines (do not use as day-one facts)**
> "**C24 — Osvaldo's Prison.** ... Osvaldo is insane. He alternates between the chain devil's combat instincts and fragments of the child he was — calling for his mother, asking why it hurts, then lashing with his chains at anything that moves." — `campaign/structure/arc-g-cassalanter-villa.md:207`
> "*Observe without entering the pentagram:* The party can watch. Osvaldo is aware of them — his brass-tinted eyes track movement. He does not attack at range. After twenty seconds, the child's voice says, distinctly: \"Please don't let them know I talked to you.\" Then the chain devil's instincts resurface and he attacks his own chains." — `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:27`
> "The voice says: \"I'm sorry.\" He dies." — `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:29` (quest-time: the dispel and death)

**Family's view of him (day-one)**
> "The soul of Victoro's eldest son, Osvaldo, is forever lost and can't be saved. To allay his guilt, Victoro has forged a plan to win back the souls of his young twins, Terenzio and Elzerina..." — `sources/adventure-wdh.json:32693` (Victoro's guilt; see D5)
> "He has not entered the attic where Osvaldo is in months and cannot bring himself to go; that vigil belongs to Ammalia." — `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:22`
> "- **Osvaldo:** ... Terenzio and Elzerina have been told Osvaldo is at school." — `campaign/setting/organizations/10-cassalanters.md:129`
> "he thinks his brother Osvaldo must be doing very well at school by now" — `campaign/setting/notable-figures/cassalanters/05-terenzio-cassalanter.md:21`

**Binding limits from sources (facts a `[design]` goal must not contradict; these are facts, not design advice)**
- "he has no hope of regaining what was taken from him" (`sources/adventure-wdh.json:32474`)
- "is forever lost and can't be saved" (`:32693`); the campaign's Path 2 says his soul "is freed" (`campaign/structure/arc-g-cassalanter-villa.md:149`), a quest outcome.
- "If the infernal contract is later destroyed ... his soul, no longer contracted, is freed." (`campaign/locations/cassalanter-villa/08-osvaldos-prison.md:31`)
- "Victoro and Ammalia have told no one." (`campaign/setting/organizations/10-cassalanters.md:96`)
- "Only Willifort Crowelle ... knows what is behind the door." (`campaign/structure/arc-g-cassalanter-villa.md:13`)

---

## Not found

Terms and places searched:
- "Osvaldo" and "Oslando": all of `/home/user/waterdeep` (Grep, content and file mode). Hits in `campaign/` are listed above. **No hit under `campaign/quests/`** for Osvaldo (the twins do appear there, in `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md`). Hits in `sources/`: `adventure-wdh.json`, `SOURCE_GUIDE.md` (lines 31 and 324), and the research bundles. Hits in the Alexandrian PDFs: `10. Lair  Cassalanter Villa.pdf` (printed pp.79, 81, 82; "Oslando" at p.82). `1. The Villains.pdf` has no Osvaldo on printed pp.18-19; the twins line is on p.19.
- "Osvaldo" in `sources/Appendix_B_-_Player_Factions.md`, `Appendix_C_-_Player_Faction_Missions.md`, `Appendix_D_-_Running_the_Tavern.md`, `sources/Act_III_Arc_D.md`, `sources/Act_III_Arc_E.md`: no hit in the file-mode search. Not read in full.
- "shielding" in the adventure: only `sources/adventure-wdh.json:32768` ("ring of mind shielding"). No "shielding circle" in any adventure line.
- "15-foot" in the Cassalanter files: only `04-osvaldo-cassalanter.md:21`. No source.
- "brass" for Osvaldo: only `08-osvaldos-prison.md:27`.
- "lemure" in the adventure: `sources/adventure-wdh.json:22888` only (the twins). Campaign: `campaign/structure/arc-g-cassalanter-villa.md:157`, `:351`; `campaign/setting/organizations/10-cassalanters.md:160` (the wiki's Victoro line).
- A cult roster that names Osvaldo: none (see F2).
- An age for him in the wiki: none (`| age            = ` blank, wiki line 17).
- The Stone of Golorr is not linked to him in any file.
- The wiki's Cassalanter family page and the research bundles (`sources/research/pass4-bundles/cassalanters/wiki.txt`) were not re-read for Osvaldo beyond the grep above.

## Not readable

- `sources/Other remix files/Cassalanters, their tragic backtstory, and Endgame setup.docx` (SOURCE_GUIDE line 687 says it covers "Victoro & Ammalia backstory, the soul-pact timeline, the children's situation, endgame resolution paths"). Not opened (`.docx`, no tool). It may hold the Osvaldo backstory that the Villains draft notes mention (`campaign/setting/villains/cassalanters.md:135`). Name it for the orchestrator to extract.
- `sources/10. Lair  Cassalanter Villa.pdf` and `sources/1. The Villains.pdf`: read as images (no `pdftotext`). Transcriptions above; check before prose use.
- `sources/research/pass4-bundles/cassalanters/wiki.txt`: not re-read.

## Not run

- `voicecheck.py` was not run (research only).
- The page was not written. No file was edited except this notes file.
- Ammalia notes citation check: section A10 of `docs/plans/setting-compendium-research-notes/pass6/cassalanters/02-ammalia-cassalanter.md` quotes `sources/adventure-wdh.json:18417` for the twins' cult status. The text is at `:18418` (verified here). Note for the Ammalia notes owner; not edited.
