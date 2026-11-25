# Pass 6 research notes: Ammalia Cassalanter

Page: `campaign/setting/notable-figures/cassalanters/02-ammalia-cassalanter.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR. The pact is a GM fact (Character Information and a Secret callout may state it). The player-safe Overview and the Background's public face must not. The cult and the household know it. Everyone else only suspects the family. Jarlaxle is the one outsider who knows, through Vessa.
Model format: `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md`

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are the file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes are shown as plain quotes. Tags such as `{@creature ...}` are left as written.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. Quotes from `1. The Villains.pdf` (printed pp.18-19) and `10. Lair  Cassalanter Villa.pdf` (printed pp.77-82) were transcribed from rendered page images. Check exact wording with `pdftotext -layout` before any quote goes into prose.
- Alexandrian appendices and Act III Arc E: Grep line numbers.
- Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-cassalanters/02-ammalia-cassalanter.txt` (the extracted Ammalia page). Line numbers below are that file's lines. The infobox cites `WDH5e-p193-194` (*Waterdeep: Dragon Heist*, 5e). Editions are as the citation key states them. The wiki's Cassalanter family page (`sources/research/pass4-bundles/cassalanters/wiki.txt` lines 544-572) was not re-read here.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

---

## Summary of findings that change how the page is written

1. **No source gives Ammalia a birth, family of origin, age, or early life.** The Background needs `[design]` material for all of it (ruling 17). The only fixed facts are the marriage, the children, the 1489 DR pact (derived), and the posts and plans of 1492 DR.
2. **The page's Morale line (L24) and Resonance clause "when they learn" (L12) are quest-time.** The other lines are day-one plans or habits. See section C.
3. **The page's Overview is 33 words** (brief limit: 21).
4. **"Tethyrian" is unsourced for Ammalia.** Every Cassalanter page and the campaign pages say "Tethyrian human", but the adventure and the wiki give no ethnicity for her. The drafter should keep the label and list it as `[research]`.
5. **Osvaldo's shielding circle is in conflict with the structure doc.** `arc-g-cassalanter-villa.md` line 13 says she reads "through the warded door"; the Notable Figures pages and the gazetteer say "outside the shielding circle" or "outside the pentagram". The published adventure does not say how she reads.

---

## A. Background facts by theme

### A1. Origin, birth, early life (no campaign source; wiki and adventure only)

**Wiki, schooling (5e, WDH5e-p55 cited)**
> "Ammalia was schooled in the [[arcane]] arts. Like her husband, she was the leader of a Cult of [[Asmodeus]] that involved certain nobles in [[Waterdeep]].<ref name="WDH5e-p55">{{Cite book/Waterdeep: Dragon Heist|55}}</ref>"
> — `scratchpad/wiki-cassalanters/02-ammalia-cassalanter.txt` line 65 (Activities)

**Adventure, schooling (5e)**
> "The vainglorious {@creature Ammalia Cassalanter|wdh|lady of House Cassalanter} is schooled in the arcane arts. Like her husband Victoro, she worships Asmodeus. When they were young, Ammalia and Victoro signed a contract with the archdevil, trading the souls of their children for power, good health, and long life. The soul of Osvaldo, their eldest son, was taken immediately, and he was transformed into a chain devil. The souls of the younger twins, Terenzio and Elzerina, will be taken when they turn nine years old."
> — `sources/adventure-wdh.json:31715` (Appendix B, "Ammalia Cassalanter", page 193)

No source gives her birthplace, parents, age, or how she came to Waterdeep's noble registry. The wiki infobox has `age = ` and `ethnicity = ` blank (`scratchpad/.../02-ammalia-cassalanter.txt` lines 15 and 17).

### A2. Marriage and the family

**Wiki infobox (cited WDH5e-p193-194)**
> "| spouses        = [[Victoro Cassalanter]]"
> — wiki line 30

> "| children       = [[Elzerina Cassalanter]]<br /> [[Osvaldo Cassalanter]]<br /> [[Terenzio Cassalanter]]"
> — wiki line 32

**Adventure, the wedding portrait (5e, page 121, Portraits)**
> "A wedding portrait, showing Victoro and Ammalia smiling and carefree"
> — `sources/adventure-wdh.json:20329`

> "Ammalia sitting with baby Terenzio and Elzerina in her lap while Victoro reads them a fairy tale"
> — `sources/adventure-wdh.json:20331`

**Adventure, the family portrait in the library (5e)**
> "Hanging on the north wall between two bookshelves is a 7-foot-tall portrait of Lord and Lady Cassalanter holding two infant children and standing beside their teenage son, Osvaldo. (This portrait conceals a secret door.)"
> — `sources/adventure-wdh.json:20039`

**Campaign, the marriage (GM summary of the Ammalia page)**
> "**Relationships.** Ammalia is the wife of Victoro Cassalanter, the mother of Osvaldo, Terenzio, and Elzerina, and the operational architect of the Founders' Day feast. Her lepidopterology hobby gives her an excuse to spend hours in the garden with her children, which is both genuine and calculated."
> — `campaign/setting/notable-figures/cassalanters/02-ammalia-cassalanter.md:26`

### A3. The pact: how and when she signed (GM fact; the year is derived)

**Adventure, the bargain (5e, page 115, Ch.6 intro)**
> "Victoro and {@creature Ammalia Cassalanter|WDH} struck a deal with Asmodeus, Lord of the Nine Hells. Three years ago, they traded away the souls of their children to escape financial ruin. The soul of their eldest son, Osvaldo, was taken immediately. What was left behind was transformed into a chain devil, which the Cassalanters confined to their attic. Their two youngest children, Terenzio and Elzerina, are doomed to lose their souls when they turn nine years old a mere ten days after Founders' Day, a midsummer festival that celebrates Waterdeep's founding."
> — `sources/adventure-wdh.json:18294`

**Adventure, the conflicting date**
> "When they were young, Ammalia and Victoro signed a contract with the archdevil, trading the souls of their children for power, good health, and long life."
> — `sources/adventure-wdh.json:31715` (conflict, see D1)

**Campaign, the infernal research (structure doc, the Villa quest opener)**
> "Ammalia found the path through infernal research: a patron who could restore their fortune and guarantee their children's futures. The contract arrived through a pit fiend intermediary. They signed it together, in the temple beneath their own villa, on a night when Osvaldo was sleeping two floors above."
> — `campaign/structure/arc-g-cassalanter-villa.md:11`

**Campaign, the Villains page (GM bullet)**
> "The bargain was made in 1489 DR, counted back from the published \"three years ago\". Ammalia found the way through infernal research. A pit fiend carried the contract to them, and they signed it together in the temple beneath their own villa."
> — `campaign/setting/villains/cassalanters.md:24`

**Campaign, the history page (Lore Summary; the year is derived from "three years ago")**
> "- Victoro and Ammalia discussed the bargain, understood what they were signing and signed together."
> — `campaign/setting/history/05-a-debt-in-blood.md:35`

> "- Financial ruin was the trigger. The family's banking was near bankruptcy when the bargain was made."
> — `campaign/setting/history/05-a-debt-in-blood.md:33`

**Campaign, the Secret callout on the organization page (GM only)**
> "- **The pact:** Victoro and Ammalia traded the souls of their children to Asmodeus for wealth compressed from three generations into one and for political access that normally takes a family centuries to build. They discussed it, understood what they were signing, and signed, three years ago. The pact covers three children: Osvaldo, already taken, and the twins."
> — `campaign/setting/organizations/10-cassalanters.md:128`

### A4. The ruin and Dagult Neverember (a grudge)

**Campaign, the structure doc**
> "The desperation began with Dagult Neverember. His embezzlement from the city treasury gutted the Cassalanter banking operations — loans underwritten against civic funds that no longer existed. Victoro's investments collapsed in sequence. The family's reputation held because reputation lags reality, but the ledgers told a different story."
> — `campaign/structure/arc-g-cassalanter-villa.md:11`

**Adventure, the gold and Victoro's hunt**
> "While Victoro hunts for Dagult Neverember's lost cache of gold, Ammalia makes plans to host a {@condition poisoned} feast in celebration of Founders' Day."
> — `sources/adventure-wdh.json:31716`

### A5. Cult leadership and role in the cult

**Adventure, the heads of the cult (5e, page 115)**
> "Lord and Lady Cassalanter are the heads of a secretive cult of Asmodeus. The cult convenes at midnight once every tenday in the temple of Asmodeus beneath Cassalanter Villa."
> — `sources/adventure-wdh.json:18304`

**Campaign, the cult's order (organization page, Beliefs)**
> "- **Rank Is Kept:** The cult runs on a strict order. Victoro leads the worship and Ammalia pours the wine, the head servants keep the other members in line, and Seffia is a true believer in the cult's hierarchy (*Dragon Heist*, 5e; **Seffia Naelryke**)."
> — `campaign/setting/organizations/10-cassalanters.md:41`

**Campaign, the final calls (organization page, Chain of command)**
> "- **Chain of command:** Ammalia makes the final calls for the family and the cult, and Victoro, who leads the worship, has stopped questioning her."
> — `campaign/setting/organizations/10-cassalanters.md:51`

**Campaign, the cult's founding and her joining (undated; the organization page flags this)**
> "- **Research:** Doctrine and Rites (Beliefs). The creed, the cult's other sacraments and how it recruits remain unsourced beyond the published rites and the Asmodeus page's candidate doctrine. The cult's founding, the temple's conversion and when each member joined are undated in every campaign file, so the History entry for them carries `[research]`."
> — `campaign/setting/organizations/10-cassalanters.md:178`

No source dates when Ammalia joined the cult, or who founded it.

### A6. Public life, charity and manner

**Adventure, her manner and hobby (5e, page 193)**
> "Ammalia is well mannered, well read, well traveled, and exceptionally shrewd. She is known for driving a hard bargain. Her hobby is lepidopterology, and her estate has the most beautiful butterfly garden. She allows her youngest children to play in the garden under her supervision."
> — `sources/adventure-wdh.json:31717`

**Adventure, her goodwill (5e, page 116)**
> "Ammalia has a lot of goodwill banked in Waterdeep-enough to curry favor with a magistrate."
> — `sources/adventure-wdh.json:18328` (within the paragraph that begins "Lady Cassalanter reacts with surprise to the sight of uninvited guests")

**Campaign, the charity (structure doc)**
> "The villa above is Waterdeep's most admired household. Ammalia's charity in the Field Ward feeds hundreds. Victoro's banking operations underwrite half the guilds in the city."
> — `campaign/structure/arc-g-cassalanter-villa.md:17`

**Campaign, the Field Ward (gazetteer, Secret callout)**
> "- The Cassalanters use the Field Ward as a source of victims and a cover for their cult. Ammalia's charity picks the one hundred poor guests for the Founders' Day feast on Flamerule 1, where ninety-nine cups of wine carry midnight tears, and the guests die within 24 hours, scattered across the city."
> — `campaign/gazetteer/waterdeep/field-ward.md:38`

**Campaign, the Sea Ward entry for her (gazetteer, "Ammalia Cassalanter (Lawful Evil, Tethyrian Human, she/her)")**
> "- A wizard known for driving a hard bargain, and keeper of the most beautiful butterfly garden in Waterdeep, where she can often be found supervising her youngest children at play. She runs a charity booth for the Cassalanter Foundation's orphan fund during the festival in **The Twin Parades**."
> — `campaign/gazetteer/waterdeep/sea-ward.md:108`

### A7. The butterfly garden and the imps

**Adventure, the garden (5e, page 125, C25)**
> "In the spring, {@creature Ammalia Cassalanter|WDH}'s gardens attract caterpillars, which transform into butterflies come summer. Lady Cassalanter's butterfly garden is the envy of her peers. The sweet scent of flowers and herbs filters up from the planters and rose bushes."
> — `sources/adventure-wdh.json:20683`

**Adventure, the six raven imps as her spies (5e)**
> "Six {@creature imp||imps} in raven form hang around the butterfly garden and occasionally prey on Ammalia's prized pets when their mistress isn't looking. Despite their insolence, Ammalia uses these imps as spies. She sends them on missions throughout the city."
> — `sources/adventure-wdh.json:20684`

**Campaign, the garden location (C25)**
> "The Cassalanters maintain this garden as a social amenity. Nobles duel here for entertainment, under the shade of flowering trees, while other guests place wagers. Ammalia presents it as a conservation project — birds rescued from the docks, butterflies bred from imported specimens."
> — `campaign/locations/cassalanter-villa/09-butterfly-garden.md:5`

### A8. Her daily pattern (adventure, 5e)

**Adventure, the location table (page 116)**
> "During an average day, she normally tended to her garden, smoked on the balcony, dismally watching the ocean, or wept at a transformed [[Osvaldo Cassalanter|Osvaldo]]'s feet in her [[House Cassalanter|mansion]]'s attic."
> — wiki line 67 (wiki quoting WDH5e-p116,125)

> "| 1-70 | She's tending to her butterfly garden ({@area C25|328}). |" (the table rows are at `sources/adventure-wdh.json:18342`-`:18353`; quoted row by row: `"1-70",` / `"She's tending to her butterfly garden ({@area C25|328})."` at 18343-18344; `"71-90",` / `"She's smoking on the balcony ({@area C25a|32a})."` at 18347-18348; `"91-00",` / `"She's weeping before Osvaldo in the attic  ({@area C24|325})."` at 18351-18352)
> — `sources/adventure-wdh.json:18343`-`:18352`

**Adventure, the balcony (C25a, page 125)**
> "If {@creature Ammalia Cassalanter|WDH} (see {@adventure appendix B|WDH|12}) is here, she's smoking and either staring dismally out toward the ocean or watching her children in the garden below ({@area C25|328})."
> — `sources/adventure-wdh.json:20703`

**Campaign, the Osvaldo visits (history page, GM)**
> "- Osvaldo is a chain devil held in the soundproofed attic of the villa, room C24, never the basement or the temple. Ammalia visits weekly and sits in the room outside the pentagram. Victoro has not entered in months. Willifort knows. Two imps are always present."
> — `campaign/setting/history/05-a-debt-in-blood.md:50`

**Campaign, the same visits (structure doc; conflicts, see D2)**
> "Ammalia reads to her son weekly through the warded door — children's stories he loved before the contract, spoken to a chain devil who weeps black ichor and claws at the walls."
> — `campaign/structure/arc-g-cassalanter-villa.md:13`

**Campaign, the Osvaldo location (C24, shielding circle)**
> "Ammalia is in the room outside the shielding circle" is not written; the location says: "Observe without entering the pentagram: The party can watch. Osvaldo is aware of them — his brass-tinted eyes track movement." — `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:27` (no Ammalia visit line here; her visit is in 08 line 35 only through Lissette and Nana Rosse, quoted in section C)

**Campaign, the study (C22; the grimoire and her notes)**
> "- Marginal notes added over three years, escalating in desperation: *\"There must be another way.\"* *\"Nana cannot know.\"* *\"V. still cannot enter the attic. He tries.\"* *\"There must be another way.\"* The phrase appears eleven times, in different inks."
> — `campaign/locations/cassalanter-villa/07-ammalias-study.md:18`

**Campaign, the study's key (C22)**
> "**Lock:** DC 18 Dexterity (Thieves' Tools), or Ammalia's key. The key never leaves her person."
> — `campaign/locations/cassalanter-villa/07-ammalias-study.md:5`

### A9. The feast, the poison and the deadline (scheduled and planned; the events are quest-time, see C and section 'Founders' Day')

**Adventure, the plan (5e, page 115)**
> "Ammalia, for her part, plans to sacrifice ninety-nine souls in one fell swoop by throwing a feast on Founders' Day featuring {@condition poisoned} food. Both the souls and the gold must be paid to Asmodeus at the same time. Foiling either one of these schemes spells doom for the Cassalanters' plot and their youngest children."
> — `sources/adventure-wdh.json:18297`

**Adventure, the poison stash (C22, page 123)**
> "Aside from the grimoire (described below), the desk holds an ornate golden candlestick (worth 125 gp), a golden inkwell (worth 25 gp), and a feathered quill pen (worth 15 gp). The desk drawer contains a wax seal bearing the Cassalanter crest, {@creature Ammalia Cassalanter|WDH}'s spellbook (which contains all the spells she has prepared), and ten vials of jet-black poison known as midnight tears (see \"Poisons\" in chapter 8 of the {@book Dungeon Master's Guide|dmg}). Ammalia plans to taint the Founders' Day feast with the poison (see \"Special Events\")."
> — `sources/adventure-wdh.json:20602`

**Adventure, her immunity (page 130, the Day of the Damned event)**
> "Ammalia is immune to poison and thus partakes freely of the delicious food."
> — `sources/adventure-wdh.json:22916`

**Campaign, the Motivations line (GM)**
> "**Motivations.** Ammalia wants to save the twins by any means necessary (including poisoning 99 people), maintain the family's social position, and ensure that the Founders' Day feast goes exactly as planned."
> — `campaign/setting/notable-figures/cassalanters/02-ammalia-cassalanter.md:16`

**Campaign, the operational window (history page)**
> "- Founders' Day, Flamerule 1, is the feast and Ammalia's real deadline. It is her operational window, chosen for the civic cover and for the time left to verify the terms. The contract falls due on Flamerule 11, the twins' ninth birthday, and does not name Founders' Day."
> — `campaign/setting/history/05-a-debt-in-blood.md:67`

### A10. Children

**Adventure, the twins (5e, page 116)**
> "Victoro and Ammalia's eldest son disappeared three years ago when the family was on the verge of bankruptcy. They have two surviving children, young twins named Terenzio and Elzerina."
> — `sources/adventure-wdh.json:18403`

**Adventure, the twins' cult status (5e, page 116)**
> "The Cassalanter twins aren't members of their parents' cult and have no other friends, since they are privately tutored and rarely allowed to leave the estate."
> — `sources/adventure-wdh.json:18417`

**Campaign, the ages (organization page)**
> "- **The family:** Victoro and Ammalia head the house, and Victoro leads the cult as its priest. Their twins, Terenzio and Elzerina, are eight years old. The twins are tutored privately, rarely leave the estate and belong to no cult. Their eldest brother Osvaldo is the chain devil in the attic (*Dragon Heist*, 5e; **Osvaldo Cassalanter**)."
> — `campaign/setting/organizations/10-cassalanters.md:47`

**Campaign, the age derivation (history page)**
> "- 1483 DR: Terenzio and Elzerina are born on Flamerule 11. This is derived from their ninth birthday on Flamerule 11, 1492 DR and is stated by no source."
> — `campaign/setting/history/05-a-debt-in-blood.md:125`

**Campaign, Osvaldo's age (structure doc)**
> "The terms were specific: Osvaldo, their eldest, already nine, the age at which the contract claims each child — taken immediately, transformed into a chain devil, bound."
> — `campaign/structure/arc-g-cassalanter-villa.md:9`

**Campaign, the twins' timing note (villains page, Key Design Note)**
> "Terenzio and Elzerina must appear before **Cassalanter Villa**. They first appear at the **Trollskull Alley** Grand Opening, where Ammalia brings them with their nanny, Nana Rosse, and the party meets them again in the villa. The Grand Opening marks the Event Outcome **Cassalanter Twins Met** when any character speaks with either twin. Once the PCs have met the children, the Founders' Day deadline becomes personal rather than abstract."
> — `campaign/setting/villains/cassalanters.md:76` (the twins' timing is a quest placement; see section C)

### A11. Osvaldo (the pact's first cost; her grief)

**Campaign, the Secret (organization page, the attic)**
> "- **Osvaldo:** The eldest son's soul was claimed first, when he was nine, the age at which the contract claims each child, and he is now twelve and a chain devil held in the soundproofed attic of the villa, room C24, never the basement or the temple. Ammalia visits weekly, sitting in the room outside the pentagram to read to him while he curses her and weeps. Victoro has not visited in months. Willifort knows. Two imps are always present. Terenzio and Elzerina have been told Osvaldo is at school."
> — `campaign/setting/organizations/10-cassalanters.md:129` (the GM Secret callout; the line itself is `campaign/setting/organizations/10-cassalanters.md:129`)

**Campaign, the Osvaldo page (Persona; shielding circle)**
> "**Morale.** Osvaldo attacks anything that enters the attic except Ammalia. Her presence calms him enough for her to read from outside the shielding circle, but she does not go into the room."
> — `campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md:23`

**Campaign, Osvaldo's view of his mother (Osvaldo page, Persona)**
> "Deep down, some fragment of Osvaldo is still there, and it hears his mother's voice when she comes to read, and it is very much aware of what was done to it."
> — `campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md:21`

**Campaign, the cover story (Terenzio's page)**
> "To those who speak with him, he knows his parents are looking for \"missing dragons,\" he has heard howling from the attic two or three times, and he thinks his brother Osvaldo must be doing very well at school by now."
> — `campaign/setting/notable-figures/cassalanters/05-terenzio-cassalanter.md:21`

### A12. Harpers and the public face (suspicion only)

**Campaign, the Harpers (organization page; the Ammalia knowledge is `[research]`)**
> "- **The Harpers (neutral, watching):** The Harpers have watched the family's charitable work for years and found nothing, which they find suspicious, and Ammalia knows they watch (**A Debt in Blood**; **The Cassalanters** in Villains, `[research]`)."
> — `campaign/setting/organizations/10-cassalanters.md:78`

**Campaign, the secrecy rule (organization page, Who suspects)**
> "- **Who suspects:** Everybody is suspicious of the Cassalanters because they are too nice to be this rich and this purebred, and nobody outside the household and the cult knows they are infernalists."
> — `campaign/setting/organizations/10-cassalanters.md:118`

**Campaign, the one outsider who knows (organization page, the exception)**
> "- **The one exception:** Jarlaxle knows about the pact through **Vessa**, his doppelganger spy in the Cassalanter social circle. He never tells Bregan D'aerthe members unless they work it out themselves."
> — `campaign/setting/organizations/10-cassalanters.md:122`

**Adventure, the public worship (Lathander and Siamorphe)**
> "Over the years, the Cassalanters have founded a number of philanthropic societies and made generous donations to temples dedicated to good-aligned deities. They are known to worship Siamorphe, a demigod whose ethos is the nobility's right and responsibility to rule."
> — `sources/adventure-wdh.json:18405`

**Campaign, the public devotion (organization Overview, GM Notes)**
> "> - **Origins:** The Cassalanter name has stood in Waterdeep's noble registry for several generations. The Lords of Waterdeep ennobled the house in 1248 DR, about 244 years before the campaign, when they granted titles to several merchant houses (Forgotten Realms Wiki, *City of Splendors: Waterdeep*, 3e). The wiki lists Waukeen, Siamorphe and Asmodeus as the house's favored deities. Financial ruin was the trigger for the bargain, which was made three years ago, about 1489 DR. The deal also bought power, good health and long life."
> — `campaign/setting/organizations/10-cassalanters.md:114`

### A13. The Eye and the household (only as context for her knowledge)

**Campaign, what the family knows of the Stone (what-each-faction table, Day one)**
> "| The Cassalanters | The vault's entrance lies in the Brandath family crypts; does not yet know the Stone is in play or in circulation | Eye #2 | Stone + Eyes #1 and #3 |"
> — `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:26`

**Campaign, the Stone's knowledge change (quest-time)**
> "- **The Cassalanters:** The row has changed by Ches 23, when Ammalia's dinner invitation reaches the party in **Fireball!**, because the family now knows the Stone is in play."
> — `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:40`

---

## B. Alignment, species, pronouns, stat block

**Pronouns**
- Campaign: "*Tethyrian human wizard and secret Asmodeus worshipper, lawful evil, she/her*. Stat block: **Mage (with modifications)**." — `campaign/setting/notable-figures/cassalanters/02-ammalia-cassalanter.md:5`
- Wiki: "| sex            = Female<ref name=\"WDH5e-p193-194\">{{Cite book/Waterdeep: Dragon Heist|193-194}}</ref>" — wiki line 13
- Adventure: "Her hobby is lepidopterology" (`sources/adventure-wdh.json:31717`); no pronoun on the line. The Sea Ward gazetteer uses "she/her" (`campaign/gazetteer/waterdeep/sea-ward.md:107`).

**Alignment**
- Campaign: "lawful evil" (`campaign/setting/notable-figures/cassalanters/02-ammalia-cassalanter.md:5`; `campaign/setting/organizations/10-cassalanters.md:94`: "Tethyrian human wizard and secret Asmodeus worshipper, lawful evil."; `campaign/gazetteer/waterdeep/sea-ward.md:107`: "Ammalia Cassalanter (Lawful Evil, Tethyrian Human, she/her)")
- Wiki (5e): "| alignment5e    = [[Lawful evil]]" — wiki line 57
- Adventure: no alignment on Ammalia's Appendix B entry (`sources/adventure-wdh.json:31711`-`:31717`).

**Species**
- Campaign: "Tethyrian human" on five pages (see `campaign/setting/notable-figures/cassalanters/02-ammalia-cassalanter.md:5`, `campaign/setting/organizations/10-cassalanters.md:94`, `campaign/setting/villains/cassalanters.md:80`, `campaign/gazetteer/waterdeep/sea-ward.md:107`, `campaign/setting/history/05-a-debt-in-blood.md:77`: "and Lady Ammalia, a Tethyrian human wizard"). No source in the adventure or wiki gives "Tethyrian" for her.
- Wiki: "| race           = [[Human]]<ref name=\"WDH5e-p193-194\" />" — wiki line 14
- Adventure: no race on Ammalia's entry.
- Result: "human" is sourced; "Tethyrian" is `[research]`.

**Titles and occupation**
- Wiki: "| titles         = Lady" (wiki line 7); "| occupation     = [[Noble]]" (wiki line 16)
- Adventure: "Lady Ammalia Cassalanter" (`sources/adventure-wdh.json:18324`); "lady of House Cassalanter" (`sources/adventure-wdh.json:31715`)

**Patron deity**
- Wiki: "| patron deity   = [[Asmodeus]]<ref name=\"WDH5e-p193-194\" />" — wiki line 18
- Adventure: "Like her husband Victoro, she worships Asmodeus." (`sources/adventure-wdh.json:31715`)

**Stat block**
- Campaign, page: "Stat block: **Mage (with modifications)**." — `campaign/setting/notable-figures/cassalanters/02-ammalia-cassalanter.md:5`. The label is a house convention (other pages use "(with modifications)" labels). The Bestiary is not drafted. No file names "Mage" for her.
- Campaign, structure doc: "Ammalia (9th-level spellcaster, see the **Bestiary** (not yet drafted))" — `campaign/structure/arc-g-cassalanter-villa.md:245`
- Campaign, location overview: "**Ammalia Cassalanter** (9th-level spellcaster): Occupies C22 or second-floor family rooms." — `campaign/locations/cassalanter-villa/area-overview.md:38`
- Wiki (5e): "| challenge5e    = 5" (wiki line 58); "| class5e        = {{Class table|edition=5e|[[Wizard]]|9}}" (wiki line 59)
- Alexandrian Lair, stat reference, printed p.82 [PDF p.6] (transcription): "Ammalia Cassalanter – DH p. 193"
- Adventure: no game statistics under her Appendix B entry (`sources/adventure-wdh.json:31711`-`:31719`).

**Age**
- No source. Wiki `age =` blank (wiki line 17). The adventure gives no age.

---

## C. Sentences on the current page that narrate quest-time, or depend on a discovery

The page does not contain a Background, Personality or Connections section. The GM block is `## Roleplaying Information` and `## Character Information`. Quest-time items are listed for routing.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L5 | "*Tethyrian human wizard and secret Asmodeus worshipper, lawful evil, she/her*. Stat block: **Mage (with modifications)**." | Day-one. "Tethyrian" `[research]`; stat label unsourced (section B) | Section B |
| 2 | L6 | "**Affiliation:** The Cassalanters (cult leadership)" | Day-one | `campaign/setting/organizations/10-cassalanters.md:94` (no affiliation line on the org page; cult leadership at `:41`, `:51`) |
| 3 | L8 | "**Featured in:** Trollskull Alley, Fireball!, Cassalanter Villa, Vault of Dragons, The Theater's Back Room, Cassalanter Villa (location)" | Quest references in the GM summary. Keep per brief (Featured in) | `campaign/quests/act-i/trollskull-alley/overview.md:43`; `campaign/quests/act-ii/fireball/overview.md:40`; `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/overview.md:81`; `campaign/structure/arc-j-vault-of-dragons.md:200` |
| 4 | L12 | "**Resonance.** Ammalia should inspire wariness with her exquisite manners and probing intelligence, sympathy when the party sees her with the twins in the butterfly garden, and cold dread when they learn she is the one planning the poisoned feast." | Mostly day-one. "when they learn" presupposes party discovery: quest-time clause. Replace with a day-one restatement (e.g. "cold dread once the party understands the feast") or route | Feast plan: `sources/adventure-wdh.json:18297`; `campaign/setting/villains/cassalanters.md:28` |
| 5 | L14 | "**Emotions.** Ammalia most often feels shrewd calculation, maternal protectiveness twisted by desperation, vainglorious self-assurance, careful control over every social interaction, intellectual pleasure in negotiation, and a private grief about Osvaldo that she channels into ruthless action." | Day-one. "vainglorious" from `sources/adventure-wdh.json:31715` | section A |
| 6 | L16 | "**Motivations.** Ammalia wants to save the twins by any means necessary (including poisoning 99 people), maintain the family's social position, and ensure that the Founders' Day feast goes exactly as planned." | Day-one plan (the feast is planned, not held). Keep | `campaign/setting/villains/cassalanters.md:70` |
| 7 | L18 | "**Inspirations.** When playing Ammalia, channel Lady Macbeth (*Macbeth*), Mama Imelda (*Coco*), and Catherine de Medici (*The Serpent Queen*)." | Not a fact | n/a |
| 8 | L22 | "**Persona.** To the world, Ammalia is well-mannered, well-read, well-traveled, and known for driving a hard bargain. Her butterfly garden is the most beautiful in Waterdeep, and she supervises her youngest children at play there. To those she trusts, she worships Asmodeus alongside Victoro and shares the same pact and the same desperation. Deep down, while Victoro hunts Neverember's gold, Ammalia makes the plans: the feast, the poison, the 99 souls. She also goes to the attic where Osvaldo is bound, and reads him his favorite stories from a chair placed just outside the shielding circle while he curses her name and pleads with her to save him." | Day-one habits and plans. The shielding-circle detail conflicts with the structure doc (D2). "shares the same pact" is GM-only (fine in Character Information). No quest-time clause | `sources/adventure-wdh.json:31717`; `campaign/gazetteer/waterdeep/sea-ward.md:113`; `campaign/setting/organizations/10-cassalanters.md:122` |
| 9 | L24 | "**Morale.** In a fight, Ammalia grabs the twins and runs. She will spend Victoro's life to buy that retreat without hesitating, and her arcane magic is precise enough to cover an exit while collapsing a hallway behind her." | Quest-time (a fight). The org draft notes route the same sentence (`campaign/setting/organizations/10-cassalanters.md:198`). The combat behaviour is at `campaign/structure/arc-g-cassalanter-villa.md:245`. Conflicts with `sources/adventure-wdh.json:18525`, see D3 | Route to Cassalanter Villa; day-one restatement needed if the Morale stays |
| 10 | L26 | "**Relationships.** Ammalia is the wife of Victoro Cassalanter, the mother of Osvaldo, Terenzio, and Elzerina, and the operational architect of the Founders' Day feast. Her lepidopterology hobby gives her an excuse to spend hours in the garden with her children, which is both genuine and calculated." | Day-one. Keep | section A2, A6 |
| 11 | L30 | "Ammalia Cassalanter is a noblewoman known for driving a hard bargain and for keeping the most beautiful butterfly garden in Waterdeep, where she can often be found supervising her youngest children at play." | Day-one. **33 words** (brief limit 21). The Overview must be cut or split | `sources/adventure-wdh.json:31717` |

**Voice profile (`.claude/skills/character-voices/voices/cassalanters.md`, Ammalia Cassalanter at lines 31-45)**

The file's secrecy header says the "after discovery" register is "used only once the party has found the truth (villain Phase 2 onward, or when the character is confronted in the temple)" (`.claude/skills/character-voices/voices/cassalanters.md:3`). Quest-time clauses in her profile:

> "- **Sentence shape:** Poised, precise sentences and probing questions. She sets terms before others know they're negotiating. After discovery: steady, cold and entirely in control." — voices file line 35

> "- **Word choice:** Public: gardens, butterflies, society, charity, \"a fair arrangement\". After discovery: planning language (\"the feast\", \"the timetable\", \"what must be done\")." — voices file line 36

> "  - *After discovery:* \"You think I'm a monster. I'm a mother with a deadline. Offer me something better, and I'll take it this instant.\"" — voices file line 45

Each needs a day-one restatement or removal under ruling 16 (the voice profile is changed to match, and the change is reported). The public register lines (voices file lines 34, 36 public part, 39-44) are day-one.

**Routing for the quest-time text (Ammalia's appearances)**
- `campaign/structure/arc-g-cassalanter-villa.md:13`: "Ammalia reads to her son weekly through the warded door".
- `campaign/structure/arc-g-cassalanter-villa.md:245`: "Ammalia (9th-level spellcaster ...) ... Her combat behavior: charm person ... dominate person on the most dangerous combatant ... She arrives to aid Victoro within 2 rounds of hearing combat."
- `campaign/structure/arc-g-cassalanter-villa.md:147`: "Victoro drops the social mask. Ammalia weeps."
- `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:54` (the Grand Opening; "She is a diabolist counting the days to Founders' Day. Play none of it.")
- `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:58`: "Mark **Ammalia Cassalanter Met**."
- `campaign/quests/act-i/trollskull-alley/ev-07-the-twin-parades.md:52`: "She is not collecting for any orphan."
- `campaign/quests/act-ii/fireball/ev-05-the-cassalanter-dinner.md:8`: "Ammalia is warm, attentive, and genuine; she is not performing."
- `campaign/quests/act-ii/fireball/ev-05-the-cassalanter-dinner.md:15`: "**Event Outcome read:** **Ammalia Cassalanter Met** and **Cassalanter Twins Met** (from Trollskull Alley ev-06)."
- `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:358` (rumour: "Madam Ammalia goes out alone twice a month in a hired cab with the curtains drawn.")
- `campaign/quests/faction-events/order-of-the-gauntlet/m02-the-black-viper-investigation/overview.md:17` (the false twin story, see D6)
- `campaign/structure/arc-c-fireball.md:208`-`:222` (the dinner, "Ammalia at the Table" at line 216)
- Cassalanter Villa location pages: `campaign/locations/cassalanter-villa/07-ammalias-study.md:28` (heist configuration), `campaign/locations/cassalanter-villa/09-butterfly-garden.md:19` (social-event rotation), `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:29` ("Ammalia moves toward C24 in the following round.").
- Adventure: `sources/adventure-wdh.json:18527` ("If the characters reduce Ammalia to 30 hit points or fewer and Victoro is with her, he banishes her to safety ..."), `sources/adventure-wdh.json:22916`-`:22919` (the feast, Day of the Damned: "This event occurs only if the Cassalanters obtain the gold from the Vault of Dragons.").

---

## Founders' Day: scheduled fact versus quest-time events

**Scheduled (day-one calendar fact)**
> "| Flamerule 1 | Founders' Day | **Cassalanter Villa** | The Cassalanter feast. This is the party's real deadline |"
> — `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:68`

> "| Flamerule 11 | The Cassalanter twins' ninth birthday | **Cassalanter Villa** | The contract falls due |"
> — `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:69`

> "- **Founders' Day versus the birthday.** The feast is the deadline the party must beat. The birthday is the date on which the contract comes due. Do not tell the players either meaning. Calendar awareness is a player resource, and the connection to the Cassalanters is a discovery they earn."
> — `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:74`

> "- Founders' Day, Flamerule 1, is the feast and Ammalia's real deadline. It is her operational window, chosen for the civic cover and for the time left to verify the terms." — `campaign/setting/history/05-a-debt-in-blood.md:67` (Recovery Plan, GM)

**Quest-time (the events on the day; keep out of the Background)**
> "This event occurs only if the Cassalanters obtain the gold from the Vault of Dragons." — `sources/adventure-wdh.json:22915` (Day of the Damned)
> "{@creature Ammalia Cassalanter|WDH} hosts a grand party on Founders' Day that begins in the early afternoon and ends at midnight." — `sources/adventure-wdh.json:22916`
> "- **Quest-time, the feast itself:** `campaign/structure/arc-g-cassalanter-villa.md:19` ("ninety-nine cups, one untouched") and `campaign/guides/gm-guide/structural-rules.md:51` (the feast and the poison, "guests die within 24 hours")."

The Founders' Day date (Flamerule 1) and the birthday (Flamerule 11) are day-one. The poisoning, the sacrifice, the gold delivery, the soul-contract resolution paths and the Event Outcomes are quest-time.

---

## D. Conflicts

**D1. Pact date: "three years ago" against "When they were young"**
- Adventure: "Three years ago, they traded away the souls of their children to escape financial ruin." — `sources/adventure-wdh.json:18294`
- Adventure, Appendix B: "When they were young, Ammalia and Victoro signed a contract with the archdevil" — `sources/adventure-wdh.json:31715`
- Campaign: "The bargain was made in 1489 DR, counted back from the published \"three years ago\"." — `campaign/setting/villains/cassalanters.md:24`
- Higher source: the adventure line 18294 ("three years ago"). The campaign follows it, and history 05 line 139 records the conflict. Both adventure lines are above the wiki's 1489 DR (wiki line 70).

**D2. Where she reads to Osvaldo: warded door against shielding circle**
- Structure doc: "Ammalia reads to her son weekly through the warded door" — `campaign/structure/arc-g-cassalanter-villa.md:13`
- Ammalia page: "from a chair placed just outside the shielding circle" — `campaign/setting/notable-figures/cassalanters/02-ammalia-cassalanter.md:22`
- Osvaldo page: "Her presence calms him enough for her to read from outside the shielding circle, but she does not go into the room." — `campaign/setting/notable-figures/cassalanters/04-osvaldo-cassalanter.md:23`
- History and organization: "sits in the room outside the pentagram" — `campaign/setting/history/05-a-debt-in-blood.md:50`; `campaign/setting/organizations/10-cassalanters.md:129`
- Gazetteer: "from a chair outside his shielding circle" — `campaign/gazetteer/waterdeep/sea-ward.md:113`
- Location: "Observe without entering the pentagram" — `campaign/locations/cassalanter-villa/08-osvaldos-prison.md:27`
- Higher source: the campaign's Notable Figures and gazetteer agree on "outside the shielding circle". The structure doc (`arc-g` line 13) is the outlier, and it is a quest doc. The published adventure says nothing on the method. The page keeps the shielding circle.

**D3. Ammalia in a fight: "spend Victoro's life" against the adventure's joint-defence rule**
- Ammalia page: "She will spend Victoro's life to buy that retreat without hesitating" — `campaign/setting/notable-figures/cassalanters/02-ammalia-cassalanter.md:24`
- Adventure: "Lord and Lady Cassalanter are formidable spellcasters and devoted to one another. If one is assailed within Cassalanter Villa, the other arrives as quickly as possible." — `sources/adventure-wdh.json:18525`
- Adventure: "If the characters reduce Ammalia to 30 hit points or fewer and Victoro is with her, he banishes her to safety for a few brief moments while he continues fighting." — `sources/adventure-wdh.json:18527`
- Structure doc: "She does not fight to kill unless the children are directly threatened." — `campaign/structure/arc-g-cassalanter-villa.md:245`
- Higher source: the adventure (18525-18527). Ammalia's Morale is quest-time and is routed (section C).

**D4. Feast food against feast wine**
- Adventure: "No one suspects that the food in the pavilion tents has been laced with midnight tears-a poison that will slay the impoverished guests at the stroke of midnight." — `sources/adventure-wdh.json:22916`
- Structure doc: "The poison is administered through the wine — ninety-nine cups, one untouched, satisfying the contract's \"one shy of a hundred\" requirement." — `campaign/structure/arc-g-cassalanter-villa.md:19`
- Alexandrian villains PDF (p.19, transcription): "Ammalia poisons 99 guests in the garden pavilion" — `sources/1. The Villains.pdf` printed p.19 [PDF p.7]
- Campaign GM bullet: "serves ninety-nine of them wine laced with midnight tears" — `campaign/setting/villains/cassalanters.md:28`
- Higher source: the adventure (food). The campaign has wine. The page does not state the method; the Motivations line says "poisoning 99 people".

**D5. Feast timing: Flamerule 1 against Tarsakh 9**
- Campaign: "Founders' Day, Flamerule 1" (`campaign/setting/history/05-a-debt-in-blood.md:67`)
- Alexandrian Lair, printed p.79 [PDF p.3] (transcription): "TARSAKH 9th – LEIRUIN FEAST: This is the feast at which the Cassalanters poison 99 guests and perform the ritual necessary to save their children's souls"
- Alexandrian Lair, printed p.79: "TARSAKH 11th – THE TWINS' BIRTHDAY: The twins' ninth birthday, on which Asmodeus will claim their souls."
- Higher source: the adventure (Flamerule 1 and 11, `sources/adventure-wdh.json:22888`: "ten days after Founders' Day"), and the campaign calendar. The Lair PDF date is overruled (already recorded at `campaign/setting/history/05-a-debt-in-blood.md:138`).

**D6. Is the Black Viper the twin of Ammalia?**
- Appendix C, printed scene (Alexandrian): "\"The Black Viper,\" he says, ... \"my source tells me she is the secret twin sister of Lady Ammalia Cassalanter. A twin kept hidden from society since birth because of a disfigurement. The mask isn't vanity. It's concealment.\"" — `sources/Appendix_C_-_Player_Faction_Missions.md:1013`
- Order m02 ev-01: "\"Black Viper, twin sister of Lady Ammalia C.? Source: anonymous, Tethyrian, well-dressed. Verify before print. Will she come back?\"" — `campaign/quests/faction-events/order-of-the-gauntlet/m02-the-black-viper-investigation/ev-01-the-black-viper-investigation.md:206`
- Order m02 overview: "The story is false. The Black Viper is not Lady Ammalia's twin, and nobody in this mission knows who she is." — `campaign/quests/faction-events/order-of-the-gauntlet/m02-the-black-viper-investigation/overview.md:26`
- Sea Ward gazetteer: "Lady Esvele Rosznar is the Black Viper" — `campaign/gazetteer/waterdeep/sea-ward.md:82`
- Higher source: the campaign (false story, Esvele Rosznar is the Black Viper). Do not put a twin on the Ammalia page.

**D7. The household: a retainer investigator against the 16-staff list**
- Structure doc: "The household staff..." lists sixteen named staff (`campaign/structure/arc-g-cassalanter-villa.md:91`: "The Cassalanter household employs sixteen named staff"; the organization page line 52 gives the list). Florette Cressyn is not on either list.
- m05: "Florette Cressyn is a household investigator on Ammalia Cassalanter's retainer, not a servant, and she reports to Ammalia directly." — `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:22`
- m02: "She is a household secretary hired for the work, and Brisenne is an alias. She is not household staff" — `campaign/quests/faction-events/order-of-the-gauntlet/m02-the-black-viper-investigation/overview.md:25`
- Higher source: the campaign's staff lists. Both quest names are quest-time routes, and the page does not name them.

**D8. The household staff: "replenish" against "discharged"**
- Adventure: "With the exception of their personal attendants, the Cassalanters replenish their servants regularly. Most move on to other jobs, but occasionally a servant discovers the secret vault" — `sources/adventure-wdh.json:18598`
- Appendix D, Hadra Stonebread (Alexandrian cook candidate, printed as Appendix D text, line 319): "Hadra was the head cook at a prominent noble household in the Sea Ward for twelve years until the family fell into debt and discharged their staff." — `sources/Appendix_D_-_Running_the_Tavern.md:319`
- Higher source: the adventure. The Appendix D candidate is a separate Alexandrian hire. Note the claim for the drafter; it is not in the Ammalia page.

**D9. Ammalia's stat label**
- Page: "Mage (with modifications)" (`campaign/setting/notable-figures/cassalanters/02-ammalia-cassalanter.md:5`)
- Structure doc and location overview: "9th-level spellcaster" (`campaign/structure/arc-g-cassalanter-villa.md:245`; `campaign/locations/cassalanter-villa/area-overview.md:38`)
- Wiki: "Wizard 9", challenge 5 (wiki lines 58-59)
- Higher source: none sourced for "Mage". The wiki and the structure doc agree on a 9th-level wizard. The page's label is a house label, and it is not a source fact.

**D10. The Ammalia Osvaldo "teenage son" and "Twelve-year-old Osvaldo" (adventure, portrait captions)**
- Adventure: "a 7-foot-tall portrait of Lord and Lady Cassalanter holding two infant children and standing beside their teenage son, Osvaldo." — `sources/adventure-wdh.json:20039`
- Adventure: "Twelve-year-old Osvaldo holding a ceremonial rapier" — `sources/adventure-wdh.json:20330`
- Campaign: "Osvaldo was nine when he was taken and is twelve now" (`campaign/setting/villains/cassalanters.md:25`)
- Higher source: the campaign (twelve now). The adventure's two captions differ, as the villains page's Draft Notes record (`campaign/setting/villains/cassalanters.md:122`).

**D11. "Tethyrian" (no source for her ethnicity)**
- Campaign: "Tethyrian human wizard" (`campaign/setting/notable-figures/cassalanters/02-ammalia-cassalanter.md:5`)
- Wiki: "| race           = [[Human]]" with no ethnicity (wiki line 14, ethnicity blank at line 15)
- Adventure, other NPCs: "Tethyrian human" for Vaelle Lurval (`sources/adventure-wdh.json:8317`) and Seffia (`sources/adventure-wdh.json:13211`). Not for Ammalia.
- Higher source: none. Report as `[research]`.

**D12. Public cover: Lathander and Siamorphe against the wiki's favored deities**
- Campaign: "The wiki lists Waukeen, Siamorphe and Asmodeus as the house's favored deities." (`campaign/setting/organizations/10-cassalanters.md:114`)
- Adventure: "Victoro ... worshipper of Lathander" is public (`sources/adventure-wdh.json:32692`, the Victoro entry; quoted in the organization Draft Notes at `campaign/setting/organizations/10-cassalanters.md:128`)
- Higher source: the adventure and the campaign's public cover. The page does not state either deity for Ammalia.

---

## E. Stale lines in other files (not edited), and routed references

**E1. Setting pages that name quest events or invented items**
- `campaign/gazetteer/waterdeep/southern-ward.md:68`: "Ammalia Cassalanter visits twice a month, alone, in a hired cab with the curtains drawn. The family pays the upper floor's rent in the name of Marra Selby." The lease name is quest-invented: `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/design-notes.md:52` ("Invented: Marra Selby (the lease name)"). A setting page carries a quest-linked item.
- `campaign/gazetteer/waterdeep/sea-ward.md:108`: "She runs a charity booth for the Cassalanter Foundation's orphan fund during the festival in **The Twin Parades**." The quest reference is on a setting page. The quest line is `campaign/quests/act-i/trollskull-alley/ev-07-the-twin-parades.md:52`.
- `campaign/gazetteer/waterdeep/sea-ward.md:113` ("Ammalia plans the Founders' Day feast and reads to her eldest son ... from a chair outside his shielding circle") is a day-one habit. It is consistent with the Notable Figures page.

**E2. Structure doc**
- `campaign/structure/arc-g-cassalanter-villa.md:13` ("through the warded door"): conflicts with the Notable Figures page (D2). Quest doc, not day-one.

**E3. Alexandrian stale or outlier lines**
- `sources/Act_III_Arc_E.md:32` (transcribed from the HTML line): "Lady Yalah Gralhund is a devoted member of the Asmodeus cult led by Victoro and Ammalia Cassalanter."
- `sources/Act_III_Arc_E.md:895`: "- **The Cassalanters** know the Gralhund connection has been compromised. Lady Ammalia will quietly distance herself from the Gralhunds and accelerate her own timeline."
- `sources/Appendix_D_-_Running_the_Tavern.md:254`: "If the Cassalanters determine the party is an asset, Ivrala's reports shape how Lady Ammalia approaches them in Act IV."
- `sources/10. Lair  Cassalanter Villa.pdf`, printed p.82 [PDF p.6] (transcription): "Ammalia is worried sick about her children, although they seem in perfect health." (a servant rumour, given as a questioning result)
- `sources/10. Lair  Cassalanter Villa.pdf`, printed p.82 [PDF p.6]: "Oslando Cassalanter – chain devil, MM p. 72" (spelling "Oslando" for Osvaldo; stale)

**E4. The Villa structure and the Gazetteer disagree on the feast's start**
- `campaign/locations/cassalanter-villa/...` (the Structure's feast time, `arc-g-cassalanter-villa.md:81`) and `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:89` ("In the campaign the feast begins at noon.") and the published adventure `sources/adventure-wdh.json:22916` ("begins in the early afternoon and ends at midnight"). Quest-time; route.

**E5. Routed to quests (where the quest-time facts already live)**
- Eye #2 and the family: `campaign/structure/arc-g-cassalanter-villa.md:15`.
- Dinner invitation and the Cassalanter Dinner: `campaign/quests/act-ii/fireball/ev-05-the-cassalanter-dinner.md:6` ("This Optional Social Event occurs when Ammalia Cassalanter's dinner invitation is accepted."), `campaign/quests/act-ii/fireball/ev-05-the-cassalanter-dinner.md:93`, `campaign/structure/arc-c-fireball.md:212` (The Invitation).
- Grand Opening: `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:52`-`:54` and `:66`.
- Florette Cressyn and Brimel: `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:22`, `:160`, `:162`.
- Corisande Brisenne: `campaign/quests/faction-events/order-of-the-gauntlet/m02-the-black-viper-investigation/ev-01-the-black-viper-investigation.md:231`.
- Black Viper rumour: see D6.
- Trollskull Manor and Ammalia's warm visit: `campaign/structure/arc-b-trollskull-alley.md:286`, `:347`-`:349` ("Ammalia Cassalanter's Introduction"; "Her Warmth Must Be Genuine.")

---

## F. Gaps (what a Background would need that no source gives)

For each gap, the sourced facts the drafter must stay consistent with are given after the gap.

1. **Birth, age, birthplace, family of origin.** No source. Consistent with: "Ammalia was schooled in the [[arcane]] arts" (wiki line 65) and "is schooled in the arcane arts" (`sources/adventure-wdh.json:31715`). Age is not stated. The wiki gives `age =` blank (line 17).
2. **Ethnicity "Tethyrian".** No source (D11). Keep the label as `[research]`.
3. **How she met and married Victoro, and when.** No source. The wedding portrait (`sources/adventure-wdh.json:20329`) is the only trace. Wedding date: none.
4. **Her schooling and the arcane training.** Only "schooled in the arcane arts" (`sources/adventure-wdh.json:31715`). Where, under whom: none.
5. **Her first contact with Asmodeus.** The grimoire records the ritual: "The tome on the desk, bound in crimson leather, details a diabolical ritual that Ammalia and Victoro enacted to first contact the archdevil Asmodeus." (`sources/adventure-wdh.json:20611`). The date and the first contact's circumstances are not given.
6. **The pact year and the age of the children.** 1489 DR is derived from "three years ago" (D1). Osvaldo's age at the pact is nine (`campaign/structure/arc-g-cassalanter-villa.md:9`).
7. **Her charity: when it started and why.** No source. The Field Ward charity is in `campaign/structure/arc-g-cassalanter-villa.md:17`.
8. **Her cult role's start, and how she recruited Tissina, Nana Rosse and Jandar.** Tissina "Joined because Ammalia asked her to" (`campaign/structure/arc-g-cassalanter-villa.md:96`). Nana Rosse joined "to stay close to the children" (`campaign/structure/arc-g-cassalanter-villa.md:97`). Jandar "bound by debt" (`:98`). Ammalia's own recruiting: none.
9. **Her friendship or rivalry with anyone outside the family.** None. The Lair PDF's servant rumour gives "Ammalia is worried sick about her children" (E3). The Order's Black Viper story is false (D6).
10. **Her relationship to Caladorn (her father-in-law).** No source gives her view of him. The ghost's line: "I do not ask for vengeance on Victoro and — on Ammalia. Only that it ends." (`campaign/setting/notable-figures/cassalanters/../voices/cassalanters.md:260`, the voices file, Caladorn's "Business" sample). Caladorn's own page gives the family tie: "Caladorn is the ghost of Victoro Cassalanter's father" (`campaign/setting/notable-figures/cassalanters/14-caladorn-cassalanter.md:25`).
11. **Her fears and losses beyond Osvaldo.** None sourced except Osvaldo (section G).
12. **Stat block.** "Mage" unsourced (B, D9).
13. **Her personal goals apart from the feast and the twins.** None sourced. Brief ruling 17 requires `[design]` material. Available hooks are in section G (lepidopterology, the butterflies, the garden).
14. **Her public devotion.** Siamorphe is the house's public devotion (`sources/adventure-wdh.json:18405`). Her own public worship is not stated; she "worships Asmodeus" only to those she trusts (page L22).
15. **Her knowledge of the Stone and the Eyes.** The campaign says the family knows the vault's entrance (`campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:26`). The adventure: "Victoro is in charge of locating the Vault of Dragons and securing the gold within it." (`sources/adventure-wdh.json:18297`). Her part in the Stone search is not separately stated.
16. **What the family does with the cult's Eye and the feast's gold.** Quest-time, not Background.

---

## G. Inner-life hints (exact quotes, for the Background and personal goals; must not be contradicted)

- **Grief for Osvaldo.** "a private grief about Osvaldo that she channels into ruthless action" — `campaign/setting/notable-figures/cassalanters/02-ammalia-cassalanter.md:14`. "She also goes to the attic where Osvaldo is bound, and reads him his favorite stories from a chair placed just outside the shielding circle while he curses her name and pleads with her to save him." — same file, line 22.
- **Children's stories.** "children's stories he loved before the contract, spoken to a chain devil who weeps black ichor and claws at the walls." — `campaign/structure/arc-g-cassalanter-villa.md:13`.
- **Crying after the top floor.** "Knows that Ammalia cries after visiting the top floor — she has heard her through the door." — `campaign/structure/arc-g-cassalanter-villa.md:109` (Lissette, a staff member's knowledge).
- **Smoking and watching the ocean.** "she's smoking and either staring dismally out toward the ocean or watching her children in the garden below" — `sources/adventure-wdh.json:20703`. "During an average day, she normally tended to her garden, smoked on the balcony, dismally watching the ocean, or wept at a transformed [[Osvaldo Cassalanter|Osvaldo]]'s feet in her [[House Cassalanter|mansion]]'s attic." — wiki line 67.
- **The garden as her joy.** "Her hobby is lepidopterology, and her estate has the most beautiful butterfly garden." — `sources/adventure-wdh.json:31717`. "Lady Cassalanter's butterfly garden is the envy of her peers." — `sources/adventure-wdh.json:20683`. The voice doc: "The Monarch is my favourite; it travels so far." (`.claude/skills/character-voices/voices/cassalanters.md:40`).
- **The twins.** "maternal protectiveness twisted by desperation" (page L14). "She allows her youngest children to play in the garden under her supervision." (`sources/adventure-wdh.json:31717`). "The family's warmth toward the twins is real. Victoro and Ammalia carry the decision together, Ammalia makes the final calls, and Victoro has stopped questioning them." — `campaign/setting/history/05-a-debt-in-blood.md:73`.
- **Her guilt and her wording.** "There must be another way." (repeated eleven times) and "Nana cannot know." — `campaign/locations/cassalanter-villa/07-ammalias-study.md:18`. The study's notes also say "V. still cannot enter the attic. He tries." (same line).
- **Wedding and family portraits.** "A wedding portrait, showing Victoro and Ammalia smiling and carefree" — `sources/adventure-wdh.json:20329`. "Ammalia sitting with baby Terenzio and Elzerina in her lap while Victoro reads them a fairy tale" — `sources/adventure-wdh.json:20331`.
- **Grudge against Neverember.** "His embezzlement from the city treasury gutted the Cassalanter banking operations" — `campaign/structure/arc-g-cassalanter-villa.md:11`. "While Victoro hunts for Dagult Neverember's lost cache of gold" — `sources/adventure-wdh.json:31716`.
- **Pride and manner.** "vainglorious self-assurance" (page L14); "Ammalia is well mannered, well read, well traveled, and exceptionally shrewd." (`sources/adventure-wdh.json:31717`); "Ammalia has a lot of goodwill banked in Waterdeep" (`sources/adventure-wdh.json:18328`).
- **Immune to poison.** "Ammalia is immune to poison and thus partakes freely of the delicious food." — `sources/adventure-wdh.json:22916`.
- **Her attendant.** "Madame Khyret is the personal attendant to Ammalia Cassalanter and is the family's chief housemaid." — `sources/adventure-wdh.json:18491`. Tissina "Joined because Ammalia asked her to." — `campaign/structure/arc-g-cassalanter-villa.md:96`.
- **Staff who notice her.** "Marchello ... Ammalia told him they were rescue birds from the docks." — `campaign/locations/cassalanter-villa/09-butterfly-garden.md:15`.
- **Harpers watch her.** "Ammalia knows they watch" — `campaign/setting/organizations/10-cassalanters.md:78` (`[research]`).

---

## Cross-references (every other file:line where the topic appears)

- `campaign/setting/villains/cassalanters.md:16`, `:24`, `:25`, `:26`, `:28`, `:29`, `:35`, `:43`, `:44`, `:56`, `:57`, `:60`, `:64`, `:70`, `:76`, `:80`, `:94`, `:106`, `:122`, `:131`, `:132`
- `campaign/setting/organizations/10-cassalanters.md:8`, `:28`, `:35`, `:36`, `:37`, `:40`, `:41`, `:47`, `:50`, `:51`, `:52`, `:54`, `:58`, `:64`, `:65`, `:66`, `:67`, `:71`, `:78`, `:94`, `:96`, `:110`, `:114`, `:117`, `:122`, `:128`, `:129`, `:130`, `:131`, `:169`, `:191`, `:198`
- `campaign/setting/history/05-a-debt-in-blood.md:8`, `:9`, `:14`, `:16`, `:22`, `:25`, `:33`, `:35`, `:42`, `:50`, `:51`, `:57`, `:58`, `:64`, `:67`, `:72`, `:73`, `:77`, `:81`, `:83`, `:97`, `:104`, `:114`, `:125`, `:127`, `:128`, `:134`, `:138`, `:139`, `:142`
- `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:29`, `:68`, `:69`, `:74`, `:82`, `:89`, `:90`, `:149`
- `campaign/setting/deities/asmodeus.md:72`, `:73`, `:75`, `:109`
- `campaign/setting/deities/siamorphe.md:58`
- `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:26`, `:40`
- `campaign/gazetteer/waterdeep/sea-ward.md:37`, `:68`, `:69`, `:82`, `:107`, `:108`, `:113`
- `campaign/gazetteer/waterdeep/southern-ward.md:68`
- `campaign/gazetteer/waterdeep/field-ward.md:38`, `:161`
- `campaign/gazetteer/waterdeep/castle-ward.md:73`
- `campaign/guides/factions/05-order-of-the-gauntlet.md:77`
- `campaign/guides/factions/11-cassalanters.md:9`, `:107`
- `campaign/guides/gm-guide/design-notes-running-the-campaign.md:67`, `:73`
- `campaign/guides/gm-guide/structural-rules.md:51`, `:52`, `:60`, `:65`
- `campaign/locations/cassalanter-villa/01-entrance-hall.md:9`, `:27`; `04-victoros-office.md:7`, `:29`; `06-ballroom.md:17`; `07-ammalias-study.md:1`-`:28`; `08-osvaldos-prison.md:3`, `:17`, `:23`, `:29`, `:35`; `09-butterfly-garden.md:5`-`:27`; `12-secret-vault.md:17`; `16-ceremonial-hall.md:15`; `area-overview.md:36`, `:38`, `:81`, `:87`, `:88`
- `campaign/structure/arc-g-cassalanter-villa.md:9`, `:11`, `:13`, `:15`, `:17`, `:19`, `:21`, `:96`-`:98`, `:109`, `:147`, `:162`, `:245`, `:277`, `:351`
- `campaign/structure/arc-b-trollskull-alley.md:243`, `:286`, `:290`, `:347`, `:349`
- `campaign/structure/arc-c-fireball.md:208`, `:212`, `:216`, `:222`, `:228`, `:230`, `:305`, `:334`
- `campaign/structure/arc-j-vault-of-dragons.md:200`, `:248`
- `campaign/quests/act-i/trollskull-alley/overview.md:43`, `:63`; `ev-06-the-grand-opening.md:10`, `:52`, `:54`, `:58`, `:66`, `:91`, `:118`, `:137`, `:155`, `:159`; `ev-07-the-twin-parades.md:12`, `:52`, `:99`
- `campaign/quests/act-ii/fireball/overview.md:40`; `ev-01-the-fireball.md:211`; `ev-05-the-cassalanter-dinner.md:6`, `:8`, `:13`, `:15`, `:27`, `:53`, `:71`, `:93`, `:97`; `design-notes.md:51`; `flowchart.md:54`
- `campaign/quests/faction-events/bregan-daerthe/m02-the-wazoo-affair/ev-01-the-wazoo-affair.md:27`, `:206` (the Gaxly note; check Notable Figures), `:386`
- `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:22`, `:160`, `:162`, `:348`, `:358`; `overview.md:81`; `design-notes.md:52`, `:57`
- `campaign/quests/faction-events/order-of-the-gauntlet/m02-the-black-viper-investigation/overview.md:17`, `:25`, `:26`; `ev-01-the-black-viper-investigation.md:20`, `:206`, `:231`
- `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:22`, `:26`; `03-willifort-crowelle.md:25`; `04-osvaldo-cassalanter.md:13`, `:21`, `:23`, `:25`; `05-terenzio-cassalanter.md:21`, `:27`; `06-elzerina-cassalanter.md:27`; `07-tissina-khyret.md:13`, `:15`, `:21`, `:23`, `:25`, `:29`; `08-laiba-nana-rosse.md:21`, `:27`; `14-caladorn-cassalanter.md:15`, `:25`
- `campaign/setting/notable-figures/bregan-daerthe/12-vessa.md:15`, `:25`
- `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:25`
- `campaign/setting/notable-figures/doom-raiders/`: none found
- `sources/adventure-wdh.json`: `:65` (pronunciation index), `:538`, `:539` (Ch.6 summary), `:18294`, `:18297`, `:18304`, `:18324`, `:18328`, `:18343`-`:18352` (location table), `:18388`, `:18403`, `:18405`, `:18417`, `:18491`, `:18525`-`:18528`, `:18535`, `:18544`, `:18560`, `:18563`, `:18597`, `:18598`, `:20039`, `:20263`, `:20329`, `:20331`, `:20574`, `:20602`, `:20611`, `:20653`, `:20683`, `:20684`, `:20703`, `:22888`, `:22916`-`:22919`, `:31711`-`:31717`, `:32474`, `:32901`
- `sources/adventure-wdh.json:3982` (Gysheer Omfreys is "an overzealous member of a devil-worshiping cult led by {@creature Victoro Cassalanter|WDH}"; Savra "has no grounds to stir up trouble with the Cassalanters")
- `sources/1. The Villains.pdf` printed pp.18-19 [PDF pp.6-7]: "They discovered that Neverember had hidden one of the Eyes in the crypt of Lady Alethea Brandath, Renaer's mother." (p.18); "Lady Cassalanter comes out personally to gather the PCs from the Entrance Hall and shoos the children away." (p.19); "THE FEAST: If the PCs agree to help and succeed in delivering the gold to the Cassalanters, they receive invitations to the feast where Ammalia poisons 99 guests in the garden pavilion and the final ritual is performed." (p.19)
- `sources/10. Lair  Cassalanter Villa.pdf` printed pp.77-82 [PDF pp.1-6]: "As Dragon Heist begins, the Cassalanters control one of the Eyes. (They stole it from the crypt of Lady Alethea Brandath, Renaer's mother.)" (p.77); "Area C22 – Ammalia's Private Study: In addition to the normal entry for this room, the desk contains the Cassalanter Report on the Grand Game (see Part 6D)." (p.80); "Ammalia Cassalanter (26-65%)" and "Ammalia Cassalanter (66-90%)" in the roster (p.81); "Ammalia Cassalanter – DH p. 193" (p.82)
- `sources/Appendix_B_-_Player_Factions.md:137`, `:406`, `:464` (the Harpers "are aware" and the Order "suspects"; against the secrecy rule)
- `sources/Appendix_C_-_Player_Faction_Missions.md:1013` (the twin claim, D6)
- `sources/Appendix_D_-_Running_the_Tavern.md:246`, `:252`, `:254`, `:319`, `:321` (Ivrala's household role and Hadra's past; see D8)
- `sources/Act_III_Arc_E.md:32`, `:895`
- `sources/SOURCE_GUIDE.md:31`, `:136`, `:649`-`:650`, `:656`, `:687` (the backstory file), `:716`

---

## Consistency with Victoro's page (`campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md`, written by the other researcher)

These must stay consistent with the Ammalia page and the Background:
1. **Stat label.** Victoro's page: "Stat block: **Noble (with modifications)**." (`01-victoro-cassalanter.md:5`). Ammalia's page: "Mage (with modifications)" (`02:5`). Neither is sourced (D9).
2. **The vigil.** Victoro's page: "He has not entered the attic where Osvaldo is in months and cannot bring himself to go; that vigil belongs to Ammalia." (`01:22`). Ammalia's page: "She also goes to the attic where Osvaldo is bound" (`02:22`). Consistent.
3. **Motivations.** Victoro's: "sacrifice 99 souls at the Founders' Day feast while maintaining his philanthropist reputation" (`01:16`). Ammalia's: "ensure that the Founders' Day feast goes exactly as planned" (`02:16`). Consistent; neither says who poisons.
4. **Who leads the cult.** Victoro's Persona: "he is a secret priest of Asmodeus" (`01:22`). Organization: "Victoro leads the worship and Ammalia pours the wine" (`10-cassalanters.md:41`). Ammalia's Persona shares the pact (`02:22`).
5. **Morale in a fight.** Victoro's: "he fights to protect his family and his secret" (`01:24`). Ammalia's: "She will spend Victoro's life to buy that retreat without hesitating" (`02:24`). These conflict in tone and with the adventure (D3). The Victoro page's line is the one that matches `sources/adventure-wdh.json:18527` (Victoro banishes her). Route Ammalia's line.
6. **Who Willifort reports to.** Victoro's: "the employer of Willifort Crowelle (doppelganger butler who knows everything that happens in the villa)" (`01:26`). Willifort's page: "reports to Ammalia on everything that transpires within the villa" (`03:25`). Organization: "Willifort Crowelle reports to Ammalia on everything that happens in the villa." (`10-cassalanters.md:117`). Victoro's page does not name Ammalia here; consistent.
7. **The children.** Victoro's: "Terenzio and Elzerina (the twins, forfeit on their ninth birthday)" (`01:26`). Consistent with Ammalia's list.
8. **The 500,000 gp.** Victoro's: "The family already holds about 500,000 gp of its own" (`01:16`). Consistent with the organization and history pages.
9. **Osvaldo visits.** Victoro: "He has not entered the attic ... in months" (`01:22`); the villains page: "Victoro has not visited in months" (`villains/cassalanters.md:57`). Consistent.
10. **Victoro's dates.** Victoro's Relationships give the pact's children; no date. Consistent with the 1489 DR derivation.

---

## Not found

Terms searched:
- "Ammalia" and "Lady Cassalanter" / "Lady Ammalia" across `campaign/` (62 files), `sources/` (38 files) and the research bundles `sources/research/pass4-bundles/cassalanters/` (bundle files read by grep only).
- "Tethyr" across `sources/adventure-wdh.json` and `campaign/*cassalanter*`.
- "Mage (with" and "Noble (with" across `campaign/setting/notable-figures/`.
- "timing" across `campaign/setting/`, "Founders' Day" and "Flamerule 1" across the calendar, structural-rules and history pages.
- "Vessa" across `campaign/setting/`.
- "Florette", "Corisande", "Brisenne", "Black Viper", "twin sister" across `campaign/`.

Gaps (no source):
- Ammalia's birth, age, birthplace, parents, schooling details, wedding date, first arrival in Waterdeep, her ethnicity (see F1-F4).
- The date and circumstances of her joining the cult, and of the cult's founding (organization page Draft Notes line 178 says so).
- Who founded the charity and when.
- Her stat block (no Bestiary).
- Her own public worship (only Siamorphe for the house).
- Her relationship with Caladorn beyond the family tie.
- Her friends and enemies outside the cult and family.
- Any Ammalia entry in the wiki's Cassalanter family page (`sources/research/pass4-bundles/cassalanters/wiki.txt`), beyond what the Cassalanter page cites. Not re-read.
- The Harpers' and Lords' Alliance knowledge of her by name (organization pages not read beyond the Harpers line).
- The Factions Guide's `campaign/guides/factions/11-cassalanters.md` for her personal entries (only lines 9 and 107 mention her).

---

## Not readable

- `Cassalanters, their tragic backtstory, and Endgame setup.docx` (listed in `sources/SOURCE_GUIDE.md:687` as "Victoro & Ammalia backstory, the soul-pact timeline, the children's situation, endgame resolution paths"). This is the most relevant source for her Background and cannot be opened with these tools. Name it for the caller to extract. Its contents are not represented in any campaign file that was read here, and it may settle gap F1 and F3 above.
- `sources/Other remix files/*.docx`: not searched. `SOURCE_GUIDE.md` lists no other `.docx` for Ammalia (line 687 is the only Cassalanter entry found).
- PDFs read as page images (no `pdftotext`): `1. The Villains.pdf` (printed pp.18-19) and `10. Lair  Cassalanter Villa.pdf` (printed pp.77-82). All PDF quotes need checking against `pdftotext -layout` before any prose use.

## Not run
- `voicecheck.py` was not run (research only).
- The page was not written. No file was edited except this notes file.
