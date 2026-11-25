# Pass 6 research notes: Terenzio Cassalanter

Page: `campaign/setting/notable-figures/cassalanters/05-terenzio-cassalanter.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Model format: `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md`
Companion: `docs/plans/setting-compendium-research-notes/pass6/cassalanters/06-elzerina-cassalanter.md` (the shared household facts are repeated in both files so each drafter has them in one place)
Ruling used: Ches 1, 1492 DR. Terenzio is eight, is not in the cult and does not know the bargain. His first appearance is the Trollskull Alley Grand Opening (`campaign/setting/villains/cassalanters.md:76`). The Grand Opening sentence on the page is quest-time (section C).

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. Tags such as `{@creature ...}` are left as written. JSON escapes are shown as plain quotes. Each line number was checked by a one-line Read or by a grep that printed it.
- Alexandrian PDFs: no shell, so `pdftotext` could not run. `1. The Villains.pdf` (PDF pp.6-7, printed pp.18-19) and `10. Lair  Cassalanter Villa.pdf` (PDF pp.1-6, printed pp.77-82) were read as page images. Those quotes are transcriptions. Check them with `pdftotext -layout` before prose use.
- Correction to the Ammalia notes (`docs/plans/setting-compendium-research-notes/pass6/cassalanters/02-ammalia-cassalanter.md`): the line "The Cassalanter twins aren't members of their parents' cult" is at `sources/adventure-wdh.json:18418`, not `:18417`. Line 18417 is the opening `"entries": [` of that block.
- Wiki: no Terenzio page exists (section A9).
- Source rank: campaign, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- Not run: `voicecheck.py`. The page was not written. This notes file is the only file written.

---

## Findings that change how the page is written

1. **Age and birthday.** "Eight" is derived from the campaign's Flamerule 11 birthday. The adventure gives no current age; it says the twins "turn nine years old a mere ten days after Founders' Day" (`sources/adventure-wdh.json:18294`). The campaign quest text states the age: "The twins are eight years old and turn nine on Flamerule 11." (`campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:66`).
2. **Pronouns.** "he/him" is sourced in campaign files only (`ev-06-the-grand-opening.md:79`; `campaign/locations/cassalanter-villa/area-overview.md:48`). The adventure's only hint is a possessive, "his sister", which refers to Terenzio (`sources/adventure-wdh.json:20497`).
3. **Unsourced labels.** "lawful good" and the stat block "Commoner (child)" have no adventure, wiki or Alexandrian source. "Tethyrian human" is campaign-only.
4. **Quest-time text on the page.** The Grand Opening sentence (L27) is quest-time and should be routed to **Trollskull Alley**. The Resonance clause "as you understand his parents' bargain" (L11) depends on the party learning the truth and needs a day-one restatement.
5. **The chase location conflicts.** The page puts the chase "around the library" (L21). The adventure's chase is in C18, the Twins' Bedroom (`sources/adventure-wdh.json:20497`, under the C18 header at `:20484`). C3 is the library, where the twins ride the sliding ladders (`:20042`, under the C3 header at `:20028`).
6. **Overview length.** The Overview (L31) is one sentence of 30 words. The brief limit is 21 words per sentence.

---

## A. Background facts by theme

### A1. Birth and age (derived; no source gives a birth date)

> "- **1480 and 1483 DR, the children are born (derived):** Osvaldo was born in 1480 DR, and the twins, Terenzio and Elzerina, were born on Flamerule 11, 1483 DR. No source states either year. Osvaldo's comes from his ninth year in 1489 DR, and the twins' comes from their ninth birthday on Flamerule 11, 1492 DR (**A Debt in Blood**)."
> — `campaign/setting/organizations/10-cassalanters.md:23`

> "- 1483 DR: Terenzio and Elzerina are born on Flamerule 11. This is derived from their ninth birthday on Flamerule 11, 1492 DR and is stated by no source."
> — `campaign/setting/history/05-a-debt-in-blood.md:125`

> "The twins are eight years old and turn nine on Flamerule 11. They know nothing of the pact, and nothing in this scene points to it. Ammalia is as warm with them as she is with the party, and she keeps a hand on one twin or the other whenever they stand still. Play it as a mother's care in a busy room."
> — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:66` (quest journal)

> "Terenzio and Elzerina are eight years old and turn nine on Flamerule 11."
> — `campaign/locations/cassalanter-villa/area-overview.md:67` (the paragraph goes on: "The twins know nothing of the contract, the temple, or the feast, and nothing in the villa tells them they are in danger." See A3 and A5.)

> "**Derived:** The twins are eight years old (the published text gives no age)."
> — `campaign/setting/villains/cassalanters.md:134`

The adventure gives no age and no birth date for either child. Its nearest line is "The souls of the younger twins, Terenzio and Elzerina, will be taken when they turn nine years old." (`sources/adventure-wdh.json:31715`, Appendix B, Ammalia).

### A2. Parents and family

> "Victoro and Ammalia head the house, and Victoro leads the cult as its priest. Their twins, Terenzio and Elzerina, are eight years old. The twins are tutored privately, rarely leave the estate and belong to no cult. Their eldest brother Osvaldo is the chain devil in the attic (*Dragon Heist*, 5e; **Osvaldo Cassalanter**)."
> — `campaign/setting/organizations/10-cassalanters.md:47` (Structure, "The family")

> "Victoro and Ammalia's eldest son disappeared three years ago when the family was on the verge of bankruptcy. They have two surviving children, young twins named Terenzio and Elzerina."
> — `sources/adventure-wdh.json:18403` (Ch. 6 lore)

> "Ammalia sitting with baby Terenzio and Elzerina in her lap while Victoro reads them a fairy tale"
> — `sources/adventure-wdh.json:20331` (Portraits, family portrait caption)

> "| children       = [[Elzerina Cassalanter]]<br /> [[Osvaldo Cassalanter]]<br /> [[Terenzio Cassalanter]]"
> — `sources/research/pass4-bundles/cassalanters/wiki.txt:38` (Victoro infobox; the same line is at `:151`, Ammalia infobox). The line prints no edition.

### A3. Brother Osvaldo and the cover story

> "If asked about their older brother, Osvaldo, Terenzio and Elzerina repeat what their parents have told them: he's attending school in a faraway city (they don't recall which one). Neither knows the cruel fate that has befallen Osvaldo (see {@area C24|325}) or suspects that a similar fate awaits them."
> — `sources/adventure-wdh.json:18456`

> "- Terenzio and Elzerina are eight years old and have not been taken. They do not know about the bargain. They have been told that Osvaldo attends school in a faraway city."
> — `campaign/setting/history/05-a-debt-in-blood.md:51`

> "- **The Family Comes First:** The love for the twins is real and drives every decision. Victoro and Ammalia would do anything to save Terenzio and Elzerina. Neither twin belongs to the cult, and both have been told that Osvaldo attends school in a faraway city (*Dragon Heist*, 5e). The published adventure adds that Victoro's plan to win back the twins is meant to ease his guilt over Osvaldo (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/10-cassalanters.md:35`

> "To everyone but his parents, Osvaldo was studying in a faraway city."
> — `sources/research/pass4-bundles/cassalanters/wiki.txt:512` (Osvaldo wiki page, Activities; the key is `WDH5e-p116`, so 5e by the key)

> "Terenzio says his father is looking for missing dragons and that something howls in the attic sometimes, which he thinks is a dragon."
> — `campaign/locations/cassalanter-villa/area-overview.md:104` (the paragraph "What they know")

### A4. The pact and the children's place in it

> "Victoro and {@creature Ammalia Cassalanter|WDH} struck a deal with Asmodeus, Lord of the Nine Hells. Three years ago, they traded away the souls of their children to escape financial ruin. The soul of their eldest son, Osvaldo, was taken immediately. What was left behind was transformed into a chain devil, which the Cassalanters confined to their attic. Their two youngest children, Terenzio and Elzerina, are doomed to lose their souls when they turn nine years old a mere ten days after Founders' Day, a midsummer festival that celebrates Waterdeep's founding."
> — `sources/adventure-wdh.json:18294`

> "Reneging on a contract with Asmodeus is a luxury no mortal can afford, but there is a way for Lord and Lady Cassalanter to save the souls of Terenzio and Elzerina. A clause in the contract allows them to preserve their remaining (and future) children's lives by instead paying \"one shy of a million gold coins, and the sacrifice of one shy of one hundred unfortunate souls.\" The Cassalanters have most of the coin they need, but they require the gold from the Vault of Dragons to buy their children's salvation without bankrupting themselves."
> — `sources/adventure-wdh.json:18296`

> "The soul of Victoro's eldest son, Osvaldo, is forever lost and can't be saved. To allay his guilt, Victoro has forged a plan to win back the souls of his young twins, Terenzio and Elzerina. Under the terms of the contract, their souls will be forfeit on their ninth birthdays, and that day is fast approaching. But Victoro can buy his way out of the obligation by providing, as the contract states, \"one shy of a million gold coins and the sacrifice of one shy of a hundred unfortunate souls.\""
> — `sources/adventure-wdh.json:32693` (Appendix B, Victoro entry)

> "- **The pact:** Victoro and Ammalia traded the souls of their children to Asmodeus for wealth compressed from three generations into one and for political access that normally takes a family centuries to build. They discussed it, understood what they were signing, and signed, three years ago. The pact covers three children: Osvaldo, already taken, and the twins."
> — `campaign/setting/organizations/10-cassalanters.md:128` (GM Secret callout)

> "- **The deadline:** The pact comes due on Flamerule 11, the twins' ninth birthday. Founders' Day on Flamerule 1 is the feast and Ammalia's real deadline. It is her operational window, chosen for the civic cover and for the time left to verify the terms, and it does not appear in the contract."
> — `campaign/setting/organizations/10-cassalanters.md:131`

> "- The goal is to reclaim the claims on Terenzio and Elzerina. The price is 999,999 gp and ninety-nine souls, both. The souls are the ninety-nine guests poisoned at the Founders' Day feast."
> — `campaign/setting/history/05-a-debt-in-blood.md:64`

> "- Osvaldo is the proof of the bargain, and Terenzio and Elzerina know nothing about it."
> — `campaign/setting/history/05-a-debt-in-blood.md:85`

> "- The contract claimed the children one at a time. Osvaldo, the eldest, was taken first and is now a chain devil. Terenzio and Elzerina are still claimed but not yet taken."
> — `campaign/setting/history/05-a-debt-in-blood.md:23`

> "The contract claims each child at nine. Osvaldo was nine when he was taken and is twelve now, a chain devil held in the soundproofed attic of the villa. The twins' souls are forfeit on their ninth birthday, Flamerule 11, ten days after Founders' Day."
> — `campaign/setting/villains/cassalanters.md:25`

> "Victoro and Ammalia Cassalanter are loving parents and secret diabolists, the heads of a Waterdhavian noble house who traded their three children's souls to Asmodeus three years ago. Their core motive is to free the twins before their ninth birthday on Flamerule 11. That means raising 999,999 gp from their own coffers and the Vault of Dragons, and poisoning ninety-nine guests at the Founders' Day feast."
> — `campaign/setting/villains/cassalanters.md:16`

> "- **Settled:** The pact covers three children (Osvaldo, taken, and the twins), per **A Debt in Blood**. The inline tag is dropped."
> — `campaign/setting/organizations/10-cassalanters.md:181`

The wiki gives the same bargain, with its markup left as written:

> "In [[1489 DR]],<ref name=\"WDH5e-p116\" />{{Waterdeep-time}} the couple signed a contract with Asmodeus, in which they agreed to give up the souls of their children in exchange for power, good health, and long life. Their eldest son, Osvaldo, was taken immediately and transformed into a [[chain devil]]. [[Terenzio Cassalanter|Terenzio]] and [[Elzerina Cassalnter|Elzerina]], their youngest twins, were also scheduled to be taken by the [[archdevil]] when they turned nine years old in [[1492 DR]],{{Waterdeep-time}} to be transformed into [[lemure]]s."
> — `sources/research/pass4-bundles/cassalanters/wiki.txt:189` (Ammalia page, History; the first sentence's key is `WDH5e-p116`, and the paragraph's second key is `WDH5e-p193-194`; 5e by the keys). "Cassalnter" is the wiki's own link spelling.

### A5. Household and cult status

> "The Cassalanter twins aren't members of their parents' cult and have no other friends, since they are privately tutored and rarely allowed to leave the estate. Around strangers, Terenzio becomes suspicious and meek, while Elzerina seems brash and outgoing. Both children are incredibly excited to meet friendly strangers and treat their \"new friends\" to a trip around the house. They help the characters sneak through the villa, since the children know they aren't supposed to have guests."
> — `sources/adventure-wdh.json:18418`

> "Terenzio and Elzerina have places in the house that their parents have forbade them from visiting-and that they are excited to explore, now that they have friends to accompany them. These locations are as follows:"
> — `sources/adventure-wdh.json:18446` (the list of rooms follows and is not reproduced)

> "**Terenzio and Elzerina Cassalanter** (Tethyrian human children, he/him and she/her; eight, turning nine on Flamerule 11) and **Laiba \"Nana\" Rosse** (tiefling cult fanatic, she/her): The twins follow the schedule under **The Cassalanter Twins** below and are with Nana Rosse at all times except from 4 to 5 on a day with no event. They are never in C22, C23, C24, the basement, or the temple."
> — `campaign/locations/cassalanter-villa/area-overview.md:48`

> "**The Twins (Terenzio and Elzerina).** Eight years old, bright, restless, and oblivious to their parents' secret. They love exploring the villa and know every room that is not locked — and several that are. Terenzio has found a way to peek into C6 through a gap in the door's lower hinge (\"Father gets very cross\"). Elzerina knows the wine cellar has \"a funny door behind a sun\" — the Siamorphe symbol concealing the passage to C29. Neither child has been to the attic or the temple."
> — `campaign/structure/arc-g-cassalanter-villa.md:129`

> "The children do not know this. They think they are showing their new friends a secret."
> — `campaign/structure/arc-g-cassalanter-villa.md:131` (the sentence before it reads "The cost is moral: the party is exploiting children whose souls are forfeit.")

> "Neither twin belongs to the cult, and both have been told that Osvaldo attends school in a faraway city (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/10-cassalanters.md:35` (the full bullet is in A3)

Nana Rosse, the twins' caretaker and tutor:

> "Laiba \"Nana\" Rosse is the twins' tiefling caretaker and tutor, a cult fanatic whose devotion to the children and devotion to the cult are inseparable in her own understanding, and the person who knows the twins' daily movements better than anyone else in the villa."
> — `campaign/setting/notable-figures/cassalanters/08-laiba-nana-rosse.md:25`

> "{@creature Laiba \"Nana\" Rosse|wdh|Laiba Rosse}, better known as \"Nana,\" is the caretaker and private tutor for Terenzio and Elzerina, and she does her best to keep track of their every move. Even so, the two often sneak away from her watchful eye."
> — `sources/adventure-wdh.json:18501` (the tag is left as written)

> "- **Laiba \"Nana\" Rosse** (cult fanatic, the twins' caretaker) — loves Terenzio and Elzerina fiercely. Joined the cult to stay close to the children when the Cassalanters began restricting household access. She knows the gatherings happen, has seen the robes. She does not know about Osvaldo or the Founders' Day plan. If she learns the children are in danger — from any source — she turns immediately. No check required. She provides: the twins' daily routine, which rooms they frequent, which doors are always locked, and that \"something terrible\" lives in the attic."
> — `campaign/structure/arc-g-cassalanter-villa.md:97`

> "Laiba \"Nana\" Rosse (Tutor/Caretaker) – tiefling cult fanatic, MM p. 345 (DH p. 117)"
> — `sources/10. Lair  Cassalanter Villa.pdf`, printed p.82 [PDF p.6] (page image transcription)

> "She reports where the twins have been and who they met to the household every evening, and she does not think of that as spying."
> — `campaign/locations/cassalanter-villa/area-overview.md:67`

> "| From 9, every night | C18 | Asleep. Nana Rosse sleeps in C17 next door and does not attend cult gatherings. |"
> — `campaign/locations/cassalanter-villa/area-overview.md:83` (table row)

### A6. Daily routine and the villa rooms

> "C3 (library), C16 (piano room), C17 (playroom), and C18 (the twins' bedroom) have no page in this journal. The table gives everything the party needs from them. From the end of the piano lesson until supper, Terenzio wears his dragon costume and Elzerina wears a knight's helm and carries her wooden sword."
> — `campaign/locations/cassalanter-villa/area-overview.md:69`

The day-schedule table is `area-overview.md:73`-`:83`. The rows that name the twins:

> "| Dawn to 10 | C16 | At a piano lesson. Elzerina plays and Terenzio roars along. Nana Rosse sits beside the piano with her crochet. |"
> "| 10 to noon | C3 | Riding the sliding ladders along the shelves. Nana Rosse sits in an armchair and counts them aloud. |"
> "| Noon to 2 | C25, reached through C2 | Chasing butterflies on the lawn. Nana Rosse sits on a wrought-iron bench. |"
> "| 2 to 4 | C17 | Playing with toys on the floor while Nana Rosse crochets a doll. |"
> "| 4 to 5 | Apart | Terenzio on the third floor outside C6. Elzerina in the kitchen corridor outside C10. Nana Rosse searches the second floor, calling for them. |"
> "| 5 to 6 | C18 | Playing make-believe in costume. |"
> "| 6 to 7 | C9 | At supper with Victoro and Ammalia. Nana Rosse stands at the sideboard. |"
> "| 7 to 9 | C17 | Playing quietly and listening to a story. |"
> "| From 9, every night | C18 | Asleep. Nana Rosse sleeps in C17 next door and does not attend cult gatherings. |"
> — `campaign/locations/cassalanter-villa/area-overview.md:75`-`:83`

> "- **Social event (Goldenight, Waukeentide Charity Ball):** C1 for the first fifteen minutes after the doors open, with Ammalia and Nana Rosse, in their best clothes. Then C18 until morning."
> — `campaign/locations/cassalanter-villa/area-overview.md:87`

> "- **Caravance (Tarsakh 1):** With Victoro, Ammalia, and Nana Rosse all day, hunting hidden presents. Dawn to 10 in C17, 10 to noon in C1, noon to 2 in C13, 2 to 5 in C25, 5 to 8 at supper in C9 and then C17, and from 8 asleep in C18. Victoro and Ammalia are not in C4, C6, or C22 that day."
> — `campaign/locations/cassalanter-villa/area-overview.md:88`

> "- **Founders' Day (Flamerule 1):** In C17 with Nana Rosse all day."
> — `campaign/locations/cassalanter-villa/area-overview.md:90`

Adventure room entries for the children:

> "If Terenzio and Elzerina are here, they're playing on the sliding ladders."
> — `sources/adventure-wdh.json:20042` (C3 Library; header `"name": "C3. Library"` at `:20028`)

> "If Terenzio and Elzerina are here. Terenzio is dressed in a crude dragon costume and is being chased around the room by his sister, who is wearing a knight's helm and swinging a wooden sword."
> — `sources/adventure-wdh.json:20497` (C18 Twins' Bedroom; header `"name": "C18. Twins' Bedroom"` at `:20484`)

> "Terenzio and Elzerina have heard howling coming from the attic two or three times in their lives and are curious about what lurks there."
> — `sources/adventure-wdh.json:20634` (C23 Attic Landing)

> "If Terenzio and Elzerina are here, they are frolicking in the garden."
> — `sources/adventure-wdh.json:20684` (C25 Butterfly Garden; the same entry then covers the six raven imps)

Alexandrian children's-location roll, printed p.81 [PDF p.5] (page image transcription):

> "Roll 1d6 to determine where Terenzio and Elzerina are. (They are generally accompanied by Nana Rosse, unless she is determined to be in Area C17 on the roster above.)"
> — `sources/10. Lair  Cassalanter Villa.pdf`, printed p.81

> "1 | Area C3, playing on the sliding ladders."
> "4 | Area C18, playing make-believe in costumes (see area description)."
> — same file, printed p.81 (the table headed "D6 / CHILDREN'S LOCATION")

Location pages (habits; the rooms are part of the day-one layout):

> "On a day with no event, Terenzio lies on the floor of the third-floor corridor from 4 to 5, looking through the gap under the door's lower hinge. His father gets very cross when he finds him there. A party member who reaches the door in that hour finds him, and he greets them as described in **The Cassalanter Twins** in the **Cassalanter Villa Area Overview**. Then he whispers: \"There's a knight in there. It never moves. I think it's asleep.\""
> — `campaign/locations/cassalanter-villa/04-victoros-office.md:33`

> "Terenzio tells Nana Rosse about any stranger he saw at the door, and she reports it to the household that evening."
> — `campaign/locations/cassalanter-villa/04-victoros-office.md:35`

> "Terenzio holds up a butterfly on his finger and tells anyone who stops: \"Mama's butterflies came on a ship. This one's a Monarch.\" Elzerina asks the first armed party member about their weapon: \"Is that a real sword? Mine's only wood, so it's a shit sword.\" Nana Rosse answers: \"Bother and buttons, Elzerina. Language.\" If anyone asks about the ravens, the twins say their mother rescued the birds from the docks."
> — `campaign/locations/cassalanter-villa/09-butterfly-garden.md:29`

> "Lissette the upstairs maid mentions hearing Ammalia crying after she visits \"the top floor.\" The twins' caretaker Nana Rosse knows \"something terrible\" lives in the attic. Neither has been inside."
> — `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:35`

> "Knows the children's schedule, favorite hiding places in the villa, and that Terenzio has nightmares about \"the thing upstairs.\" If told the truth: panics, then steadies — the children come first."
> — `campaign/structure/arc-g-cassalanter-villa.md:113` (Bressa, nursemaid, human female, 20s; the entry opens "assists Nana Rosse with the twins during daytime hours.")

### A7. The Trollskull Alley Grand Opening (first appearance; quest-time event)

Campaign placement, in a setting page (see E1 for the quest text it carries):

> "Terenzio and Elzerina must appear before **Cassalanter Villa**. They first appear at the **Trollskull Alley** Grand Opening, where Ammalia brings them with their nanny, Nana Rosse, and the party meets them again in the villa. The Grand Opening marks the Event Outcome **Cassalanter Twins Met** when any character speaks with either twin. Once the PCs have met the children, the Founders' Day deadline becomes personal rather than abstract."
> — `campaign/setting/villains/cassalanters.md:76`

> "| Terenzio and Elzerina | Surviving children | Twins, eight years old; don't know about the bargain; first appear at the **Trollskull Alley** Grand Opening, before PCs investigate the villa |"
> — `campaign/setting/villains/cassalanters.md:58`

> "**Settled by the user (Session 51):** The key design note needed the twins in **Trollskull Alley**, and no file in `campaign/quests/` named Terenzio or Elzerina. ... The twins now first appear at the Grand Opening, with their nanny Nana Rosse, in a fixed scene, and the party meets them again in the villa."
> — `campaign/setting/villains/cassalanters.md:132` (Draft Notes; the omitted middle sentences are about the Ammalia scene and the zero-prep rule, and are quoted in full at that line)

The Grand Opening scene (quest journal, quoted for routing):

> "Ammalia arrives without Lord Cassalanter. She brings her twins, Terenzio and Elzerina, and their tiefling nanny, Nana Rosse. She is warm, generous, and interested in the party as people. She stays two hours, learns everyone's name, and leaves with the social grace that makes a room feel larger after she's gone. She is a diabolist counting the days to Founders' Day. Play none of it."
> — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:54`

> "Terenzio and Elzerina Cassalanter (Lawful Good, Tethyrian Human, he/him and she/her) :: eight-year-old twins in a dragon costume and a knight's helm, who want to see every corner of the tavern."
> — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:79`

> "Terenzio is curious and trusting, and he roars at people as a greeting. Elzerina is blunt and competitive, and she pokes people with her wooden sword when she wants an answer. He calls her Elzi, and she calls him Ter. They go first to the character standing nearest the door."
> — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:81`

> "Terenzio roars, swishes his felt tail, and waits for your answer."
> — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:95`

> "Terenzio's dragon has a long neck and a great many teeth, and Elzerina is adding a knight with a very large sword."
> — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:114`

> "Terenzio accepts either answer cheerfully. If the party says yes, the drawing stays in the corner of the slate until someone wipes it. Near the end of the evening, Ammalia tells the twins to thank the owners, takes a child's hand in each of hers and leaves, with Nana Rosse a step behind."
> — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:118`

> "Mark **Cassalanter Twins Met** when any character speaks with Terenzio or Elzerina."
> — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:120`

> "After twelve days of renovation, six guilds, seven factions, and a gladiatorial tournament, the party opened Trollskull Manor. Full house on opening night. Ammalia Cassalanter attended, stayed two hours, learned everyone's name, and was exactly as warm as the wine she sent. She brought her eight-year-old twins and their nanny, and the twins spent the evening drawing on the specials slate. Durnan sent a message through Threestrings. A merchant from the harbor bottom came and went without giving his name."
> — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:151` (quest journal; quest-time)

The Fireball dinner (quest-time; the children are kept away):

> "The children are \"not well enough for company\" — a detail offered once by the butler and not returned to. If **Cassalanter Twins Met** is marked, a party that asks after the twins hears the butler say they are with their nanny and at their lessons, and nothing more, because the household keeps the children away from guests."
> — `campaign/quests/act-ii/fireball/ev-05-the-cassalanter-dinner.md:25`

### A8. Nicknames and the bond between the twins

> "He calls her Elzi, and she calls him Ter."
> — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:81`

> "**Word choice:** Child's adventure vocabulary: dragons, missing dragons, \"my brother's at school\", \"Nana\". He calls his sister \"Elzi\"."
> — `.claude/skills/character-voices/voices/cassalanters.md:90`

> "Elzerina is Terenzio's twin and the bolder of the two, forfeit to Asmodeus alongside her brother on their ninth birthday, Flamerule 11, 1492 DR (she is eight now), and a child who suspects something is wrong in this house without knowing what."
> — `campaign/setting/notable-figures/cassalanters/06-elzerina-cassalanter.md:25` (her page; the bond is shared)

### A9. Wiki and research bundles (no Terenzio page)

- `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-cassalanters/05-terenzio-cassalanter.txt` reads "NOT FOUND".
- `sources/research/pass4-bundles/cassalanters/wiki.txt`: the page headers are Victoro (`:5`), Ammalia (`:118`), Caladorn (`:350`), Osvaldo (`:438`) and the family page (`:536`). No Terenzio or Elzerina header exists. The twins appear only inside those pages, at `:38`, `:76`, `:151`, `:189`, `:193`, `:470`, `:504`, `:580`.
- `sources/research/pass4-bundles/cassalanters/wiki.txt:580` (the family page, History; key `WDH5e-p115-116`): "the younger twins Elzerina and Terenzio were scheduled to be taken on the occasion of their 9{{th}} birthday, one [[tenday]] after [[Founders' Day]] of {{Yearlink|1492}}."
- `sources/research/pass3-bundles/north-ward/wiki.txt:1028`: the same sentence, with the same markup.

---

## B. Alignment, species, pronouns, stat block

**Page (current, the Summary line)**
> "- *Tethyrian human child, lawful good, he/him*. Stat block: **Commoner (child)**."
> — `campaign/setting/notable-figures/cassalanters/05-terenzio-cassalanter.md:5`

**Campaign, quest journal (the only source for alignment and pronouns)**
> "Terenzio and Elzerina Cassalanter (Lawful Good, Tethyrian Human, he/him and she/her) :: eight-year-old twins in a dragon costume and a knight's helm, who want to see every corner of the tavern."
> — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:79`

**Campaign, Organizations page**
> "- **Terenzio Cassalanter** — Tethyrian human child, lawful good. See the **Terenzio Cassalanter** page in Notable Figures."
> — `campaign/setting/organizations/10-cassalanters.md:97`

**Campaign, Locations (area overview)**
> "**Terenzio and Elzerina Cassalanter** (Tethyrian human children, he/him and she/her; eight, turning nine on Flamerule 11)"
> — `campaign/locations/cassalanter-villa/area-overview.md:48`

**Adventure (pronoun clue only; no alignment, species or stat block for the twins)**
> "Terenzio is dressed in a crude dragon costume and is being chased around the room by his sister, who is wearing a knight's helm and swinging a wooden sword."
> — `sources/adventure-wdh.json:20497` (the possessive "his sister" refers to Terenzio)
> "Around strangers, Terenzio becomes suspicious and meek, while Elzerina seems brash and outgoing."
> — `sources/adventure-wdh.json:18418` (no pronoun, no race)

**Adventure, Appendix B:** no entry for either child. The Ammalia entry is at `sources/adventure-wdh.json:31711`-`:31719`, and the Osvaldo index entry is at `:32470`. A search for "Terenzio" and "Elzerina" in the adventure found no Appendix entry.

**Wiki:** no page. No race, alignment or stat block for either child.

**Alexandrian stat reference**, printed p.82 [PDF p.6] (page image transcription; the whole list was read): "Cooks – commoners, MM p. 345", "Cultists – MM p. 345", "Guard – MM p. 347", "Servants – commoners, MM p. 345", "Imps – MM p. 76", "Oslando Cassalanter – chain devil, MM p. 72", "Jandar Chergoba (Head Chef) – tiefling cult fanatic, MM p. 345 (DH p. 117)", "Laiba \"Nana\" Rosse (Tutor/Caretaker) – tiefling cult fanatic, MM p. 345 (DH p. 117)". No entry for Terenzio or Elzerina. The "Commoner (child)" label on the page has no source.

---

## C. Sentences on the current page that narrate quest-time or depend on a discovery

Page lines: L5 summary, L11 Resonance, L13 Emotions, L15 Motivations, L17 Inspirations, L21 Persona, L23 Morale, L25 Relationships, L27 Trollskull paragraph, L31 Overview.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Tethyrian human child, lawful good, he/him*. Stat block: **Commoner (child)**." | Day-one label. "lawful good" and "Commoner (child)" are unsourced (B) | `ev-06-the-grand-opening.md:79` (alignment, pronouns); no stat source |
| 2 | L6 | "**Affiliation:** The Cassalanters (non-cultist)" | Day-one | `campaign/setting/organizations/10-cassalanters.md:35` |
| 3 | L7 | "**Featured in:** Trollskull Alley, Cassalanter Villa, Cassalanter Villa (location)" | Quest references in the summary; kept per brief | `ev-06-the-grand-opening.md:54`; `area-overview.md:48` |
| 4 | L11 | "**Resonance.** Terenzio should inspire immediate protectiveness; delight at his dragon-costume earnestness; and creeping dread as you understand his parents' bargain makes him forfeit on his ninth birthday, Flamerule 11. He is eight now." | "as you understand his parents' bargain" depends on the party's discovery (campaign-start rule). Restate as a day-one dread or route. The forfeit itself is day-one | `campaign/setting/villains/cassalanters.md:25` |
| 5 | L13 | "**Emotions.** Terenzio most often feels uncomplicated curiosity, physical joy in play, trust in the adults he knows, the particular bravery of a child who has never had reason to doubt that he is loved, and restless impatience to grow up enough to have adventures." | Day-one temperament. "trust in the adults he knows" fits `sources/adventure-wdh.json:18456` | `:18456` |
| 6 | L15 | "**Motivations.** Terenzio wants to play with his sister, explore the parts of the villa his parents told him not to explore, and eventually become someone who could go in the attic." | Day-one. "parts of the villa his parents told him not to explore" matches `sources/adventure-wdh.json:18446` | `:18446` |
| 7 | L17 | "**Inspirations.** When playing Terenzio, channel Simba (*The Lion King*), Hiccup (*How to Train Your Dragon*, before he found the dragon), and Bastian (*The Neverending Story*)." | Not a fact | n/a |
| 8 | L21 | "**Persona.** To the world, Terenzio is a boy in a dragon costume being chased around the library by his sister with a wooden sword. To those who speak with him, he knows his parents are looking for \"missing dragons,\" he has heard howling from the attic two or three times, and he thinks his brother Osvaldo must be doing very well at school by now. Deep down, he has decided that whatever is in the attic is probably a dragon, and he considers this exciting rather than frightening." | Day-one. "library" conflicts with the adventure's C18 (D1). "missing dragons" `:18455`; "howling" `:20634`; "school" `:18456` | `sources/adventure-wdh.json:18455`, `:18456`, `:20497`, `:20634` |
| 9 | L23 | "**Morale.** Terenzio runs to Nana Rosse if frightened by anything he cannot interpret as a game." | Borderline. A fright-and-escape rule in a Morale block, with no source for Terenzio. Nana's protective role is day-one (`area-overview.md:106`). The running is a combat-type reaction. Decision for the orchestrator (H1) | `area-overview.md:106`; `arc-g-cassalanter-villa.md:305` |
| 10 | L25 | "**Relationships.** Terenzio is one of the twins (alongside Elzerina), forfeit to Asmodeus on his ninth birthday, Flamerule 11, 1492 DR (he is eight now), a child who trusts his parents completely, and a boy who is curious about the attic for entirely innocent reasons." | Day-one. "a child who trusts his parents completely" has no direct source; the trust is the page's own (see L13) | `villains/cassalanters.md:25`; `sources/adventure-wdh.json:18418` |
| 11 | L27 | "At the **Trollskull Alley** Grand Opening, Terenzio arrives in his dragon costume with Ammalia and Nana Rosse, roars at the party, and draws a dragon on the tavern's specials slate." | **Quest-time** (a named quest event). Route to **Trollskull Alley**, ev-06 | `ev-06-the-grand-opening.md:54`, `:79`, `:95`, `:114`, `:118` |
| 12 | L31 | "Terenzio Cassalanter is one of the family's young twins, currently best known for wearing a dragon costume around the villa while being chased by his sister with a wooden sword." | Day-one. **30 words** in one sentence (brief limit 21) | `area-overview.md:65`-`:69`; `ev-06-the-grand-opening.md:79` |

**Voice profile** (`.claude/skills/character-voices/voices/cassalanters.md`, Terenzio at lines 85-99). The file's secrecy header (line 3) says "Some profiles also have an **after discovery** register, used only once the party has found the truth". Terenzio's profile has none. The clauses that need a decision under ruling 16:
- Line 99, sample "Under pressure": "Elzi! Elzi, run! I'll be the dragon!" This is a danger line, so it is combat-time. Decision for the orchestrator.
- Line 92, Personality in speech: "Curious and trusting. He happily repeats what he's heard about \"missing dragons\" and the howling. His bravery shows as wanting to see the attic." Day-one.
- Line 98, sample "Business": "Father's looking for missing dragons. And there's howling in the attic, sometimes. I think it's a dragon too." Day-one (`sources/adventure-wdh.json:18455`, `:20634`).

**Children's fates** (quest-time resolutions; route them, do not write them as day-one):

> "And the ninety-nine — the Cassalanters will still attempt the feast unless the party explicitly addresses this. The sacrifice clause is separate from the gold clause."
> — `campaign/structure/arc-g-cassalanter-villa.md:147` (the paragraph headed "**Path 1 — Help the Cassalanters Find the Gold (Cooperative).**")

> "The children's souls are freed without the gold payment or the ninety-nine sacrifices. Osvaldo's chain devil form dissolves — he dies, but his soul is freed."
> — `campaign/structure/arc-g-cassalanter-villa.md:149` (the paragraph headed "**Path 2 — Destroy the Infernal Contract (Mace of Disruption).**")

> "The party does not intervene before Founders' Day. Ninety-nine die. The children's souls are saved by the completed ritual."
> — `campaign/structure/arc-g-cassalanter-villa.md:155` (the paragraph headed "**Path 3 — Let the Sacrifice Happen.**")

> "The children's souls are forfeit — Asmodeus claims them on their birthday. They become lemures. Cost: the children die."
> — `campaign/structure/arc-g-cassalanter-villa.md:157` (the paragraph headed "**Path 4 — Expose the Cassalanters.**")

> "If the Cassalanters fail to obtain the {@item Stone of Golorr|WDH}, the following events don't come to pass. As a consequence, Terenzio and Elzerina are transformed into {@creature lemure||lemures} as their souls are forfeit ten days after Founders' Day."
> — `sources/adventure-wdh.json:22888` (see D4)

> "The Cassalanters' ritual to save Terenzio and Elzerina plays out here (see \"Special Events\")."
> — `sources/adventure-wdh.json:22811`

> "Standing before the statue of Asmodeus in the temple, Victoro summons a {@creature barbed devil} and informs it that payment has been made in full."
> — `sources/adventure-wdh.json:22918` (Day of the Damned)

> "The devil declares (in Infernal) that the payment is \"satisfactory\" and informs Victoro that the souls of Terenzio and Elzerina will not be taken to the Nine Hells."
> — `sources/adventure-wdh.json:22918` (the same entry)

> "The Cassalanters don't fear being arrested, since they have faith that their wealth, reputations, and contacts will keep them out of prison. They do fear the ticking clock of Founders' Day. They plead for the characters to allow them to carry out their plan, if only to save Terenzio's and Elzerina's lives."
> — `sources/adventure-wdh.json:18528`

> "- **The forfeit.** The contract falls due on Flamerule 11, the twins' ninth birthday and ten days after Founders' Day. The soul half of the buy-out fails if the feast is stopped, whatever happens with the gold. If the feast proceeds, ninety-nine people are dead whether or not the party later destroys the contract."
> — `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:91`

> "TARSAKH 11th – THE TWINS' BIRTHDAY: The twins' ninth birthday, on which Asmodeus will claim their souls."
> — `sources/10. Lair  Cassalanter Villa.pdf`, printed p.79 [PDF p.3] (image transcription)

Confrontation (quest-time; not Background):

> "The confrontation should feel tragic. These are desperate parents who chose a monstrous path. Ammalia reading to her chain-devil son. Victoro unable to visit the attic. Elzerina stepping between Terenzio and anything that frightens him. These details humanize without excusing."
> — `campaign/structure/arc-g-cassalanter-villa.md:305`

---

## D. Conflicts

**D1. Where the chase happens: the library against C18**
- Page, L21: "being chased around the library by his sister with a wooden sword" (`campaign/setting/notable-figures/cassalanters/05-terenzio-cassalanter.md:21`).
- Adventure, C18 Twins' Bedroom: "Terenzio is dressed in a crude dragon costume and is being chased around the room by his sister, who is wearing a knight's helm and swinging a wooden sword." (`sources/adventure-wdh.json:20497`; header at `:20484`).
- Campaign area overview: "C3 (library), C16 (piano room), C17 (playroom), and C18 (the twins' bedroom) have no page in this journal." (`campaign/locations/cassalanter-villa/area-overview.md:69`); "| 5 to 6 | C18 | Playing make-believe in costume. |" (`:80`); "| 10 to noon | C3 | Riding the sliding ladders along the shelves. Nana Rosse sits in an armchair and counts them aloud. |" (`:76`).
- Higher source: the adventure and the area overview both put the costume chase in C18. The page's "library" is the outlier.

**D2. Cursed at birth against the parents' contract**
- Alexandrian, printed p.19 [PDF p.7] (image transcription): "Lady Cassalanter introduces her husband and they tell the PCs a modified version of their plight: The twins were cursed at their birth by Asmodean cultists to lose their souls on their ninth birthday." (`sources/1. The Villains.pdf`)
- Adventure: "Three years ago, they traded away the souls of their children to escape financial ruin." (`sources/adventure-wdh.json:18294`)
- Campaign: "Victoro and Ammalia Cassalanter are loving parents and secret diabolists, the heads of a Waterdhavian noble house who traded their three children's souls to Asmodeus three years ago." (`campaign/setting/villains/cassalanters.md:16`)
- Higher source: the campaign and the adventure. The "cursed at birth" version is recorded as left out at `campaign/setting/villains/cassalanters.md:135`: "The Alexandrian claim that the twins were cursed at birth (`1. The Villains.pdf` p.19, from a page image)."

**D3. Where the children first meet the party**
- Alexandrian, printed p.19 (image transcription): "They are given an opportunity to \"accidentally\" meet the Cassalanters' children, who come running into the Entrance Hall (C1) while the PCs are waiting." (`sources/1. The Villains.pdf` PDF p.7)
- Campaign, the Session 51 user ruling: "The twins now first appear at the Grand Opening, with their nanny Nana Rosse, in a fixed scene, and the party meets them again in the villa." (`campaign/setting/villains/cassalanters.md:132`)
- Higher source: the campaign (user ruling). The Alexandrian meeting in the Entrance Hall is not used.

**D4. What triggers the children's transformation**
- Adventure: "If the Cassalanters fail to obtain the {@item Stone of Golorr|WDH}, the following events don't come to pass. As a consequence, Terenzio and Elzerina are transformed into {@creature lemure||lemures} as their souls are forfeit ten days after Founders' Day." (`sources/adventure-wdh.json:22888`)
- Campaign: "The soul half of the buy-out fails if the feast is stopped, whatever happens with the gold." (`campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:91`)
- Campaign, the Secret block: "Had the contract run its course, the twins were to become lemures (Forgotten Realms Wiki, Victoro Cassalanter, from *Dragon Heist*, 5e)." (`campaign/setting/organizations/10-cassalanters.md:129`, inside the Osvaldo bullet; the parenthesis is the wiki citation)
- Campaign: "The children's souls are forfeit — Asmodeus claims them on their birthday. They become lemures." (`campaign/structure/arc-g-cassalanter-villa.md:157`)
- The adventure ties the fate to the Stone; the campaign ties it to the buy-out and the birthday. Higher source: the campaign. Route the trigger to **Cassalanter Villa**.

**D5. Feast and birthday dates**
- Alexandrian Lair, printed p.79 [PDF p.3] (image transcription): "TARSAKH 9th – LEIRUIN FEAST: This is the feast at which the Cassalanters poison 99 guests and perform the ritual necessary to save their children's souls (assuming they've managed to secure the gold from the Vault)." and "TARSAKH 11th – THE TWINS' BIRTHDAY: The twins' ninth birthday, on which Asmodeus will claim their souls."
- Campaign: "| Flamerule 1 | Founders' Day | **Cassalanter Villa** | The Cassalanter feast. This is the party's real deadline |" and "| Flamerule 11 | The Cassalanter twins' ninth birthday | **Cassalanter Villa** | The contract falls due |" (`campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:68`-`:69`).
- Higher source: the campaign calendar and the adventure's "ten days after Founders' Day" (`sources/adventure-wdh.json:18294`). The Lair dates are overruled (see `campaign/setting/organizations/10-cassalanters.md:184` and `campaign/setting/villains/cassalanters.md:133`).

**D6. Age: "nine and seven" in a retired file**
- Retired file, `campaign/structure/ch2-city-of-splendors.md:285`: "| Terenzio and Elzerina | Surviving children | Nine and seven years old; don't know about the bargain; should appear in Arc B before PCs investigate the villa |"
- Campaign: "Terenzio and Elzerina are eight years old and turn nine on Flamerule 11." (`campaign/locations/cassalanter-villa/area-overview.md:67`)
- Higher source: the campaign. The retired file is not to be used (CLAUDE.md, retired chapter files).

**D7. Osvaldo's age in the adventure's captions (sibling context)**
- `sources/adventure-wdh.json:20039`: "Hanging on the north wall between two bookshelves is a 7-foot-tall portrait of Lord and Lady Cassalanter holding two infant children and standing beside their teenage son, Osvaldo. (This portrait conceals a secret door.)"
- `sources/adventure-wdh.json:20330`: "Twelve-year-old Osvaldo holding a ceremonial rapier"
- Campaign: "Osvaldo was nine when he was taken and is twelve now" (`campaign/setting/villains/cassalanters.md:25`). The captions conflict with each other; the campaign is higher.

**D8. Who grabs the children in a fight (across pages; see H1)**
- Terenzio page, L23: "Terenzio runs to Nana Rosse if frightened by anything he cannot interpret as a game."
- Elzerina page, L23: "Elzerina does not run when frightened. She interposes herself between Terenzio and the threat and looks for a weapon."
- Nana page, L23: "In a fight, Nana Rosse grabs the twins and places herself between them and the threat."
- Ammalia page, L24: "In a fight, Ammalia grabs the twins and runs."
- Area overview, `:106`: "If a fight starts in a room with the twins, she takes both by the hand and leaves by the nearest door, placing herself between them and the party."
- Structure doc, `:305` and `:485`: "Elzerina stepping between Terenzio and anything that frightens him."
- Four sources describe the household's response to a fight with the children. The drafter must pick one or route the scene.

**D9. Consistent items (checked, no conflict)**
- Appendix C (`sources/Appendix_C_-_Player_Faction_Missions.md:1017`): "The Cassalanters have two children. There was no twin. Gaxly's source invented this story." Consistent with two living children (the twins). The scene is the Black Viper rumour (Ammalia notes, D6).
- Lair, printed p.82 [PDF p.6] (servant questioning, a rumour): "Ammalia is worried sick about her children, although they seem in perfect health." Consistent.

---

## E. Stale lines in other files (not edited) and routed references

**E1. Setting pages carrying quest text (for the orchestrator; not edited)**
- `campaign/setting/villains/cassalanters.md:58`: "first appear at the **Trollskull Alley** Grand Opening, before PCs investigate the villa" (a quest placement in a relationships row).
- `campaign/setting/villains/cassalanters.md:76`: "The Grand Opening marks the Event Outcome **Cassalanter Twins Met** when any character speaks with either twin. Once the PCs have met the children, the Founders' Day deadline becomes personal rather than abstract." (an Event Outcome and an "once the PCs" clause on a setting page; ruling 1 bars both)
- `campaign/gazetteer/waterdeep/sea-ward.md:113`: "Osvaldo is a chain devil now, and the twins are told he is at school." (day-one; consistent)

**E2. Retired and source-guide lines**
- `campaign/structure/ch2-city-of-splendors.md:285` ("Nine and seven years old"): retired (D6).
- `campaign/structure/ch2-city-of-splendors.md:296`: "**Key design note:** Terenzio and Elzerina must appear before Arc G. The DM should identify during Arc B when the children will first be visible." Superseded by `campaign/setting/villains/cassalanters.md:132`.
- `sources/SOURCE_GUIDE.md:136`: "- **Cassalanters:** Victoro and Ammalia as desperate, sympathetic parents who bargained away their children's souls. Their agenda: recover the gold to buy back the children's souls before Founders' Day." (the contract falls due after Founders' Day; see D5)
- `sources/SOURCE_GUIDE.md:326`: "- Five resolution paths for the children's pact (from the plan's Critical Design Decisions)" (the campaign's Cassalanter Villa text has four paths: `campaign/structure/arc-g-cassalanter-villa.md:147`, `:149`, `:155`, `:157`)

**E3. Quest-time references that already live in the quest files (route, do not write as day-one)**
- Trollskull Alley: `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:54`, `:66`, `:79`, `:81`, `:87` ("- Monsters: Elzerina asks whether the party fights them and whether she can come."), `:91`, `:95`, `:101`, `:107`, `:109`, `:114`, `:116`, `:118`, `:120`, `:138`, `:151`, `:159`; `campaign/quests/act-i/trollskull-alley/overview.md:43`, `:63`; `flowchart.md:91`.
- Fireball!: `campaign/quests/act-ii/fireball/ev-05-the-cassalanter-dinner.md:25`.
- Cassalanter Villa structure: `campaign/structure/arc-g-cassalanter-villa.md:21`, `:97`, `:113`, `:129`, `:131`, `:147`, `:149`, `:155`, `:157`, `:305`, `:485`.
- Cassalanter Villa location: `campaign/locations/cassalanter-villa/area-overview.md:65`-`:110`; `01-entrance-hall.md:27`, `:29`; `02-garden-mudroom.md:31`; `04-victoros-office.md:33`, `:35`; `07-ammalias-study.md:17`; `08-osvaldos-prison.md:35`; `09-butterfly-garden.md:27`, `:29`; `10-false-vault.md:17`; `11-wine-cellar.md:13`; `15-family-crypt.md:31`.
- Bregan D'aerthe, the Vessa thought-reading: `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/design-notes.md:7` ("...because it points at the children's pact and the twins are eight.") and `:11` ("She reads thoughts, which is how he learned of the Asmodean pact and the children's contract.").

**E4. Wiki (not edited)**
- Wiki, Osvaldo page `:504` and family page `:580`: the twins were "scheduled to be taken" at nine (see A4 and A9 for the exact text). The Victoro page `:76` carries the same sentence with `{{WDH-time}}` as its date template.

---

## F. Gaps (what a Background would need that no source gives)

1. **Birth date and place.** No source. The derived year 1483 DR is "stated by no source" (`campaign/setting/history/05-a-debt-in-blood.md:125`).
2. **Race "human" and ethnicity "Tethyrian".** Campaign only (`ev-06-the-grand-opening.md:79`; `area-overview.md:48`). The adventure's "Tethyrian" hits belong to other NPCs and families (for example `sources/adventure-wdh.json:1060`, the Amcathras family, and `:13211`, Arn and Seffia). None is for a Cassalanter child. The wiki has no page.
3. **Alignment.** "lawful good" is campaign only (`ev-06-the-grand-opening.md:79`). The adventure gives no alignment for either child (`sources/adventure-wdh.json:18403`-`:18456`).
4. **Stat block.** None. The Alexandrian stat reference has no entry (B).
5. **Schooling.** Adventure: "privately tutored" (`sources/adventure-wdh.json:18418`); Nana is "the caretaker and private tutor" (`:18501`). The subjects are not given beyond "At a piano lesson" (`area-overview.md:75`) and the sliding ladders and playroom.
6. **Friends.** "have no other friends" (`sources/adventure-wdh.json:18418`), against "now that they have friends to accompany them" (`:18446`, the party). No source gives a child friend.
7. **The dragon costume and the belief in dragons.** The adventure gives "missing dragons" and "howling" (`:18455`, `:20634`); no source gives the costume's origin.
8. **The children's lives after the resolution.** The campaign gives the children's status for each path (`arc-g-cassalanter-villa.md:149`, `:155`, `:157`) and nothing about their lives afterward.
9. **Relationship with Osvaldo beyond the cover story.** No source says Terenzio ever met Osvaldo. The adventure says the twins "don't recall" which school (`sources/adventure-wdh.json:18456`).
10. **Caladorn (grandfather).** No child-specific source. Caladorn is Victoro's father ("**Caladorn Cassalanter:** Victoro's father.", `campaign/setting/organizations/10-cassalanters.md:123`), so the twins' grandfather is an inference `[research]`. Caladorn says the names once: "His voice does: \"Elzerina and Terenzio.\" He says the names once." (`campaign/locations/cassalanter-villa/15-family-crypt.md:31`).
11. **Terenzio's own goals.** None sourced. The page's own Motivations (L15) give "play with his sister" and "eventually become someone who could go in the attic". Any `[design]` goal must not reveal the pact to him, must not put him in the attic or the temple ("They are never in C22, C23, C24, the basement, or the temple.", `area-overview.md:48`), and must not change an Event Outcome.
12. **Whether he has seen his brother.** No source.
13. **Fear.** The adventure says the twins are "too scared to ask" about the missing dragons (`sources/adventure-wdh.json:18455`). No source says he fears the attic. The page says he finds it "exciting rather than frightening" (L21, page-own).

---

## G. Inner-life hints (exact quotes; the Background and personal goals must not contradict them)

- **Curiosity about the attic.** "Terenzio and Elzerina have heard howling coming from the attic two or three times in their lives and are curious about what lurks there." — `sources/adventure-wdh.json:20634`
- **Fear he does not voice.** "(What their parents plan to do with a bunch of scary, winged reptiles is beyond them, and Terenzio and Elzerina are too scared to ask.)" — `sources/adventure-wdh.json:18455`
- **Nightmares.** "Terenzio has nightmares about \"the thing upstairs.\"" — `campaign/structure/arc-g-cassalanter-villa.md:113`
- **Shy with strangers.** "Around strangers, Terenzio becomes suspicious and meek, while Elzerina seems brash and outgoing." — `sources/adventure-wdh.json:18418`. "If the party did not mark it, both are shy and polite. Terenzio stays half behind Nana Rosse, and Elzerina steps forward." — `campaign/locations/cassalanter-villa/area-overview.md:98`
- **Peeking at forbidden rooms.** "On a day with no event, Terenzio lies on the floor of the third-floor corridor from 4 to 5, looking through the gap under the door's lower hinge. His father gets very cross when he finds him there." — `campaign/locations/cassalanter-villa/04-victoros-office.md:33`
- **Mother's butterflies.** "Mama's butterflies came on a ship. This one's a Monarch." — `campaign/locations/cassalanter-villa/09-butterfly-garden.md:29`. Ammalia's voice: "The Monarch is my favourite; it travels so far." — `.claude/skills/character-voices/voices/cassalanters.md:40`
- **Dragon play with his sister.** "Terenzio is dressed in a crude dragon costume and is being chased around the room by his sister, who is wearing a knight's helm and swinging a wooden sword." — `sources/adventure-wdh.json:20497`
- **Bravery and trust (page-own, L13).** "the particular bravery of a child who has never had reason to doubt that he is loved". The adventure's "repeat what their parents have told them" (`sources/adventure-wdh.json:18456`) is the only sourced trust.
- **Joy in play.** "Terenzio roars, swishes his felt tail, and waits for your answer." — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:95`
- **Under pressure (voice).** "Elzi! Elzi, run! I'll be the dragon!" — `.claude/skills/character-voices/voices/cassalanters.md:99`. Combat-time (C).
- **The family's warmth.** "The family's warmth toward the twins is real. Victoro and Ammalia carry the decision together, Ammalia makes the final calls, and Victoro has stopped questioning them." — `campaign/setting/history/05-a-debt-in-blood.md:73`
- **Victoro's guilt.** "To allay his guilt, Victoro has forged a plan to win back the souls of his young twins, Terenzio and Elzerina." — `sources/adventure-wdh.json:32692`
- **Ammalia's supervision.** "She allows her youngest children to play in the garden under her supervision." — `sources/adventure-wdh.json:31717` (Appendix B, Ammalia; verified by a one-line Read)
- **Nana's devotion, with a line she would cross.** "Laiba \"Nana\" Rosse, the twins' caretaker, is a cult fanatic who joined the cult to remain close to the children — she would betray the Cassalanters to save Terenzio and Elzerina." — `campaign/structure/arc-g-cassalanter-villa.md:21`
- **Family memory.** "Ammalia sitting with baby Terenzio and Elzerina in her lap while Victoro reads them a fairy tale" — `sources/adventure-wdh.json:20331`
- **The brother he misses (Osvaldo's page).** "the specific anguish of knowing his siblings are scheduled for the same fate" — `campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md:13`. "make contact with the siblings he cannot see" — same file, `:15`.

---

## H. Consistency with the household pages

**H1. Fight responses (must agree across pages, or the scene is routed).**
- Ammalia page L24: "In a fight, Ammalia grabs the twins and runs. She will spend Victoro's life to buy that retreat without hesitating, and her arcane magic is precise enough to cover an exit while collapsing a hallway behind her."
- Nana page L23: "In a fight, Nana Rosse grabs the twins and places herself between them and the threat. She is more dangerous than she looks."
- Elzerina page L23: "Elzerina does not run when frightened. She interposes herself between Terenzio and the threat and looks for a weapon."
- Terenzio page L23: "Terenzio runs to Nana Rosse if frightened by anything he cannot interpret as a game."
- Adventure, the joint-defence rule (`sources/adventure-wdh.json:18525`): "Lord and Lady Cassalanter are formidable spellcasters and devoted to one another. If one is assailed within Cassalanter Villa, the other arrives as quickly as possible." The rule names the parents, not the children.
- The Ammalia notes (D3) record that her Morale conflicts with this rule and route it. The four children's fight responses cannot all be true at one fight.

**H2. Consistent items (checked against the household pages)**
- Victoro page L16 (Motivations): "Victoro wants to save his younger twins from the Asmodean pact before their ninth birthday, acquire 999,999 gold pieces to fund the buy-out clause, and sacrifice 99 souls at the Founders' Day feast while maintaining his philanthropist reputation." Consistent.
- Victoro page L22 (Persona): "a genuine warmth toward his younger children that makes the rest of what he is harder to see". Consistent.
- Victoro page L26 (Relationships): "Terenzio and Elzerina (the twins, forfeit on their ninth birthday)". Consistent.
- Ammalia page L16 (Motivations): "Ammalia wants to save the twins by any means necessary (including poisoning 99 people)". Consistent.
- Ammalia page L26 (Relationships): "the mother of Osvaldo, Terenzio, and Elzerina". Consistent.
- Osvaldo page L13 (Emotions): "the specific anguish of knowing his siblings are scheduled for the same fate". Consistent.
- Osvaldo page L21 (Persona): "\"attending school in a faraway city,\" Terenzio and Elzerina were told". Consistent with `sources/adventure-wdh.json:18456`.
- Osvaldo page L25 (Relationships): "the reason Terenzio and Elzerina are forfeit on their ninth birthday, Flamerule 11, 1492 DR (the pact requires both 999,999 gp and ninety-nine souls)". Consistent.
- Nana page L21 (Persona): "she reports the children's movements to the household every evening, without considering it a betrayal". Consistent with `area-overview.md:67`.
- Organization page, Structure (`:47`): "Their twins, Terenzio and Elzerina, are eight years old." Consistent.
- Affiliation: "(non-cultist)" is consistent with `organizations/10-cassalanters.md:35` and `sources/adventure-wdh.json:18418`.

**H3. Within the twins' pages**
- Both pages give "Tethyrian human child, lawful good" (campaign only).
- Both pages carry the Grand Opening sentence at L27 (quest-time).
- Both Overviews are one sentence (Terenzio 30 words; Elzerina 36 words, counted by hand).
- The Elzerina page's L25 says she "suspects something is wrong in this house without knowing what". The adventure says "Neither knows the cruel fate that has befallen Osvaldo ... or suspects that a similar fate awaits them" (`sources/adventure-wdh.json:18456`). The two do not conflict, because a child may sense that something is wrong without suspecting her own fate. Keep the same line for both twins.

---

## Cross-references (every other file:line where the topic appears)

- `campaign/setting/organizations/10-cassalanters.md`: `:7`, `:23`, `:35`, `:36`, `:47`, `:97`, `:98`, `:118`, `:123`, `:128`, `:129`, `:131`, `:181`, `:184`, `:198`
- `campaign/setting/villains/cassalanters.md`: `:16`, `:25`, `:58`, `:76`, `:80`, `:132`, `:134`, `:135`
- `campaign/setting/history/05-a-debt-in-blood.md`: `:9`, `:14`, `:23`, `:25`, `:42`, `:43`, `:51`, `:58`, `:64`, `:67`, `:73`, `:77`, `:85`, `:86`, `:96`, `:97`, `:114`, `:125`, `:128`, `:133`
- `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md`: `:16`, `:24`, `:68`, `:69`, `:91`
- `campaign/setting/deities/asmodeus.md`: `:74`, `:75`, `:109`
- `campaign/setting/deities/lliira.md`: `:8`, `:81`
- `campaign/setting/deities/waukeen.md`: `:72`
- `campaign/gazetteer/waterdeep/sea-ward.md`: `:37`, `:113`
- `campaign/guides/factions/11-cassalanters.md`: `:7`, `:107`
- `campaign/guides/gm-guide/design-notes-running-the-campaign.md`: `:67`
- `campaign/guides/gm-guide/structural-rules.md`: `:52`, `:65`
- `campaign/guides/trollskull-manor/01-overview.md`: `:15`
- `campaign/locations/cassalanter-villa/area-overview.md`: `:48`, `:52`, `:65`-`:110`
- `campaign/locations/cassalanter-villa/01-entrance-hall.md`: `:27`, `:29`
- `campaign/locations/cassalanter-villa/02-garden-mudroom.md`: `:31`
- `campaign/locations/cassalanter-villa/04-victoros-office.md`: `:33`, `:35`
- `campaign/locations/cassalanter-villa/07-ammalias-study.md`: `:17`
- `campaign/locations/cassalanter-villa/08-osvaldos-prison.md`: `:35`
- `campaign/locations/cassalanter-villa/09-butterfly-garden.md`: `:27`, `:29`
- `campaign/locations/cassalanter-villa/10-false-vault.md`: `:17`
- `campaign/locations/cassalanter-villa/11-wine-cellar.md`: `:13`
- `campaign/locations/cassalanter-villa/15-family-crypt.md`: `:31`
- `campaign/structure/arc-g-cassalanter-villa.md`: `:9`, `:11`, `:13`, `:17`, `:19`, `:21`, `:75`, `:97`, `:113`, `:129`, `:131`, `:147`, `:149`, `:155`, `:157`, `:305`, `:433`, `:485`
- `campaign/structure/ch2-city-of-splendors.md` (retired): `:117`, `:285`, `:296`, `:375`, `:402`
- `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md`: `:10`, `:54`, `:62`, `:66`, `:73`, `:79`, `:81`, `:83`, `:87`, `:91`, `:95`, `:101`, `:107`, `:109`, `:114`, `:116`, `:118`, `:120`, `:138`, `:151`, `:159`
- `campaign/quests/act-i/trollskull-alley/overview.md`: `:43`, `:63`
- `campaign/quests/act-i/trollskull-alley/flowchart.md`: `:91`
- `campaign/quests/act-ii/fireball/ev-05-the-cassalanter-dinner.md`: `:25`
- `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/design-notes.md`: `:7`, `:11`
- `campaign/setting/notable-figures/cassalanters/02-ammalia-cassalanter.md`: `:12`, `:16`, `:24`, `:26`, `:30`
- `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md`: `:16`, `:22`, `:26`, `:30`
- `campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md`: `:13`, `:15`, `:21`, `:25`
- `campaign/setting/notable-figures/cassalanters/08-laiba-nana-rosse.md`: `:11`, `:13`, `:15`, `:21`, `:23`, `:25`, `:27`, `:31`
- `campaign/setting/notable-figures/cassalanters/14-caladorn-cassalanter.md`: `:15`, `:25`
- `sources/adventure-wdh.json`: `:18294`, `:18296`, `:18403`, `:18405`, `:18414`, `:18418`, `:18446`, `:18455`, `:18456`, `:18501`, `:18525`, `:18528`, `:20028`, `:20039`, `:20042`, `:20330`, `:20331`, `:20484`, `:20497`, `:20634`, `:20684`, `:22811`, `:22888`, `:22918`, `:31715`, `:31717`, `:32692`, `:32693`
- `sources/1. The Villains.pdf`: PDF p.6 (printed p.18), PDF p.7 (printed p.19)
- `sources/10. Lair  Cassalanter Villa.pdf`: PDF p.1 (printed p.77, the children in the garden picture); PDF p.3 (printed p.79, event schedule); PDF p.5 (printed p.81, children's location roll); PDF p.6 (printed p.82, stat reference and servant questioning)
- `sources/SOURCE_GUIDE.md`: `:31`, `:136`, `:323`, `:326`, `:687`
- `sources/Appendix_C_-_Player_Faction_Missions.md`: `:1017`
- `sources/research/pass4-bundles/cassalanters/wiki.txt`: `:38`, `:76`, `:151`, `:189`, `:193`, `:470`, `:504`, `:512`, `:580`
- `sources/research/pass3-bundles/north-ward/wiki.txt`: `:1028`

---

## Not found

Terms searched, and where:
- "Terenzio", "Elzerina", "Elzi", "twins": `campaign/setting/`, `campaign/quests/`, `campaign/locations/`, `campaign/structure/`, `campaign/guides/`, `campaign/gazetteer/` (all). Found only the lines in the cross-references.
- "Terenzio" or "Elzerina" in `sources/research/*/wiki.txt`: only `pass4-bundles/cassalanters/wiki.txt` and `pass3-bundles/north-ward/wiki.txt`.
- "Terenzio", "Elzerina", "twins", "Osvaldo", "children" in `sources/*.md` (Act III Arc E, Appendix B, C, D, SOURCE_GUIDE): only Appendix C `:1017` and SOURCE_GUIDE `:31`, `:136`, `:323`-`:326`, `:687`. The Appendix D "Vayle Twins" and the Act III Arc E Gralhund children are unrelated.
- "Commoner" and "lawful good" for the twins in `campaign/` and `sources/`: only `ev-06-the-grand-opening.md:79` and the page itself.
- "Tethyrian" for the twins in `sources/adventure-wdh.json`: none.
- The Vault of Dragons quest (`campaign/structure/arc-j-vault-of-dragons.md`) and `arc-c-fireball.md`: no twin line found by grep.
- A stat block for either child: none in the Alexandrian Lair stat reference, the adventure, the wiki or the campaign.

Gaps (no source): birth date and place, race and ethnicity beyond the campaign's label, alignment, stat block, schooling subjects, the costume's origin, the children's friends, their life after the pact resolves, and any Terenzio-Osvaldo contact beyond the cover story. See F.

---

## Not readable

- `sources/Other remix files/Cassalanters, their tragic backtstory, and Endgame setup.docx` (listed in `sources/SOURCE_GUIDE.md:687` as "Victoro & Ammalia backstory, the soul-pact timeline, the children's situation, endgame resolution paths"). The file exists (Glob confirmed) and cannot be opened with these tools. It is the most likely source for the children's situation and may settle F1, F8 and F9. Name it for the caller to extract.
- `sources/Other remix files/*.docx` (others): not searched. `SOURCE_GUIDE.md` lists no other Cassalanter docx.
- PDFs read as page images, not `pdftotext`: `sources/1. The Villains.pdf` (PDF pp.6-7) and `sources/10. Lair  Cassalanter Villa.pdf` (PDF pp.1-6). Every PDF quote needs a `pdftotext -layout` check before prose use.

## Not run

- `voicecheck.py` was not run (research only).
- The page was not written. The only file written is this notes file.
