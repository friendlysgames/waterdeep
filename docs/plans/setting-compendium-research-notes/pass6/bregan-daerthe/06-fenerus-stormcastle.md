# Pass 6 research notes: Fenerus Stormcastle

Page: `campaign/setting/notable-figures/bregan-daerthe/06-fenerus-stormcastle.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Model format: `docs/plans/setting-compendium-research-notes/pass6/cassalanters/04-osvaldo-cassalanter.md`
Rulings used: Ches 1, 1492 DR (day one). Campaign-start rule (ruling 1). Settled by the user, Session 51 (`campaign/gazetteer/waterdeep/trades-ward.md:249`-`:250`): Fenerus knows the destination of the messages, has not worked out that the drow are Bregan D'aerthe, is not a Watch prisoner, and did not hide the Stone before an arrest. The campaign's Stone routing: `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:184` and the Gralhund Villa journal govern where the Stone is.

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines. Where a quote is a fragment of a longer sentence, the fragment is copied exactly and the line number is given.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes (`\"`) are shown as plain quotes. Tags such as `{@creature ...}` and `{@item ...}` are left as written. Section titles are given as the adventure prints them, with the page number.
- Alexandrian markdown: `sources/Act_III_Arc_E.md` (line 74 is the only Fenerus line; the file has no Quill Alley, Trades Ward, Seven Masks or lamplighter text). `sources/Appendix_B_-_Player_Factions.md` and `sources/Appendix_C_-_Player_Faction_Missions.md`: no Fenerus line.
- Alexandrian PDFs: not read for Fenerus. `sources/5. Faction Outposts.pdf` and `sources/17. Outpost and Lair Revelation Lists.pdf` are the PDFs the source guide lists for Bregan D'aerthe outposts and letters. `sources/SOURCE_GUIDE.md:222`-`:225` lists three Bregan D'aerthe outposts (Seven Masks Theater, a hidden safehouse at the docks, and a disguise workshop in the North Ward) and does not list a Trades Ward house. This session has no shell, so `pdftotext` could not run, and the PDFs were not paged through. Check `5. Faction Outposts.pdf` for a Fenerus house before any outpost detail is used.
- Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-bregan-daerthe/06-fenerus-stormcastle.txt`. Quoted as "wiki line N" (that file's lines). Citation keys: `WDH5e-p83` (*Waterdeep: Dragon Heist*, 5e, p.83), `WDH5e-p63` (p.63), `WDH5e-p57` (p.57) and `WDH5e-p4`. The wiki gives 5e values only.
- Pass 4 and pass 5 research bundles were searched. `sources/research/pass4-bundles/jarlaxle/campaign-hits.txt` is out of date: at its line 54 it quotes an older `trades-ward.md:40` ("Fenerus believes his contacts are Luskan agents"), and at its line 59 an older `trades-ward.md:261` ("His Notable Figures page says he hid the Stone before his arrest"). Neither is used here.
- No `.docx` in `sources/SOURCE_GUIDE.md` names Fenerus. See the report's Not readable list for the docx files that could hold Bregan D'aerthe detail.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **The arrest and the hidden Stone are not day-one facts.** The published adventure says Fenerus was arrested and had hidden the Stone: "Agents of the Lords' Alliance recently labeled Fenerus as a wanted brigand and notified the Lords of Waterdeep, who sent the City Watch to arrest him. Fenerus had the good sense to hide the {@item Stone of Golorr|WDH} elsewhere and hopes to use it as leverage to gain his freedom as well as forgiveness for past crimes." (`sources/adventure-wdh.json:7125`). The wiki says the same (wiki lines 70 and 72). The campaign has settled otherwise: "He is not a Watch prisoner and did not hide the Stone before an arrest." (`campaign/gazetteer/waterdeep/trades-ward.md:250`). The campaign wins. The page must not mention an arrest or a hidden Stone.
2. **Where the Stone is, is conditional.** The campaign's Gralhund Villa journal puts the Stone in his house only on one branch: "### If the Chase Fails" and then "The Stone reaches its destination:" with "- **BD team:** The Stone reaches Fenerus Stormcastle. Jarlaxle holds it." (`campaign/quests/act-ii/gralhund-villa/ev-08-the-rooftop-chase.md:62`-`:67`). The adventure states it outright (`sources/adventure-wdh.json:6171`). The page cannot state the Stone's location on day one.
3. **Knowledge of the drow is settled.** The published adventure says "He has no clue that his contacts are drow members of Bregan D'aerthe" (`sources/adventure-wdh.json:7124`). The campaign says he "knows where the messages go, but he has not worked out that the cloaked drow belong to Bregan D'aerthe" (`campaign/gazetteer/waterdeep/trades-ward.md:38`). The page's Affiliation line (line 6) says he "has worked out where the messages go". This matches the campaign. He believes he spies for Luskan (`trades-ward.md:38`; `sources/adventure-wdh.json:7124`), while the Factions Guide and the organization page list him as a Bregan D'aerthe asset.
4. **The pickup interval is two days.** Campaign: "Krebbyg Masq'il'yr collects them every two days" (`campaign/gazetteer/waterdeep/trades-ward.md:37`). The Alexandrian markdown says "with updates transmitted twice daily to Fenerus Stormcastle via message drop" (`sources/Act_III_Arc_E.md:74`), which is about the Gralhund team's updates and not Krebbyg's pickups. The campaign wins.
5. **Overview length.** The page's Overview (line 29) is one sentence of 26 words, counted by hand. The brief limit is 21.
6. **The Manshoon kidnap is a quest event.** The organization page says Manshoon "has marked Fenerus Stormcastle ... as a soft target" (`campaign/setting/organizations/09-manshoons-zhentarim.md:87`), a day-one state. The directive that orders the kidnap arrives while the party explores (`campaign/guides/factions/10-manshoons-zhentarim.md:23`). The Villains page, the GM Guide and the Running the Villains table state the directive as present fact (`campaign/setting/villains/jarlaxle.md:114`; `campaign/guides/gm-guide/running-the-villains.md:75`). Route those to Faction Outposts.

---

## A. Background facts by theme

### A1. Origin and birth (no birthplace, birth year or family in any source)

Species, ethnicity and sex, the wiki's infobox:

> `| race           = [[Human]]`
> — wiki line 14 (5e)

> `| ethnicity      = [[Tethyrian]]`
> — wiki line 15 (5e)

> `| sex            = Male`
> — wiki line 13

Campaign, the gazetteer's line on his name and kind:

> "**Fenerus Stormcastle (Neutral, Tethyrian Human, he/him)**"
> — `campaign/gazetteer/waterdeep/trades-ward.md:120`

The pronunciation, from the adventure's list of names:

> "Fenerus Stormcastle", "FEN-er-us"
> — `sources/adventure-wdh.json:117`-`:118`

Age: the wiki's `age` field is blank (wiki line 17). The wiki's `dob` and `dobnotes` are blank (wiki lines 21 and 22). The page says nothing about age. The page's Emotions line refers to "a decade of brigandage" (line 13), which is the only time span in the sources.

### A2. The Blood Hawk Posse: founding, the raid, and the fall

Adventure, the whole story (section "Fenerus's Story", page 63):

> "Fenerus Stormcastle was the founder of the Blood Hawk Posse, a gang of horse-riding brigands that, to this day, harries travelers on the road to Amphail. When he was drummed out of the gang after a botched raid, Fenerus \"retired\" to Waterdeep and joined the Guild of Chandlers and Lamplighters."
> — `sources/adventure-wdh.json:7123`

Wiki (5e, same facts, no date):

> "Fenerus was the founder of the infamous mounted bandit group known as the [[Blood Hawk Posse]]. He was ousted as the head of the gang after a failed raid and decided to retire in Waterdeep, where he unknowingly became the primary spy of Bregan D'aerthe.<ref name=\"WDH5e-p63\" />"
> — wiki line 68 (`WDH5e-p63`)

Campaign, the organization page (the same facts in brief):

> "**Fenerus Stormcastle** — Tethyrian human cut-out and message-drop, neutral. Guild of Chandlers and Lamplighters lamplighter by day; intelligence asset by night. Supposed to be a cut-out, but once followed Krebbyg after a pickup and knows the messages go to the Sea Maidens Faire. See the **Fenerus Stormcastle** page in Notable Figures."
> — `campaign/setting/organizations/07-bregan-daerthe.md:104`

Campaign, the Guilds page (the same facts, in the Guilds entry):

> "**Fenerus Stormcastle** (Neutral, Tethyrian Human, he/him) founded the Blood Hawk Posse, was drummed out of the gang after a botched raid, and then joined the Guild of Chandlers and Lamplighters in Waterdeep."
> — `campaign/setting/governance-and-guilds/guilds.md:54`

Campaign, the page's Relationships line (current; the Posse is still active):

> "**Relationships.** Fenerus is the former founder of the Blood Hawk Posse (current brigands on the Amphail road), a Bregan D'aerthe cut-out and message-drop on Quill Alley, and the target of Manshoon's kidnap directive in **Faction Outposts**."
> — `campaign/setting/notable-figures/bregan-daerthe/06-fenerus-stormcastle.md:25` (the kidnap clause is quest-time; see C10)

### A3. Joining the Guild of Chandlers and Lamplighters, and the lamplighter's post

Campaign, the Trades Ward gazetteer entry:

> "A big, scar-faced lamplighter with gray hair, who lights lamps in the ward and minds his own business. He is a retired brigand who spies for Luskan."
> — `campaign/gazetteer/waterdeep/trades-ward.md:121`

Adventure, a resident's view (the children of the alley, section "Fenerus's Story" neighbourhood, page 63):

> "If they are asked about Fenerus, the children know who he is. They describe him as a big man with graying hair who looks like he has been in many fights, based on \"the scars he wears on his face.\" They know nothing more about him, other than that he lives alone."
> — `sources/adventure-wdh.json:7104`

No source dates his joining the Guild.

### A4. Spying for Luskan, and the drow he serves without knowing

Wiki:

> "Beyond his work as a lamplighter, Fenerus spied on Waterdeep for agents of [[Luskan]], who were in fact secret [[drow]] operatives of [[Bregan D'aerthe]]. He provided information about current political decisions made in Waterdeep to his contacts in the City of Sails.<ref name=\"WDH5e-p63\">{{Cite book/Waterdeep: Dragon Heist|63}}</ref>"
> — wiki line 65 (`WDH5e-p63`)

Adventure:

> "Until recently, Fenerus supplemented his income by spying for the city of Luskan and providing his contacts with information on the political climate in Waterdeep, as well as juicy bits of news overheard on his nightly rounds through the Trades Ward. He has no clue that his contacts are drow members of Bregan D'aerthe, since they wear cloaks and keep to the shadows."
> — `sources/adventure-wdh.json:7124`

Campaign, the Trades Ward gazetteer:

> "- Fenerus spies for Luskan. He followed Krebbyg once and knows where the messages go, but he has not worked out that the cloaked drow belong to Bregan D'aerthe."
> — `campaign/gazetteer/waterdeep/trades-ward.md:38`

Campaign, the settled note (Session 51):

> "- **Settled by the user (Session 51):** Whether Fenerus knows who his contacts are. The published text says he has no idea (`sources/adventure-wdh.json:7124`), and the Factions Guide says he followed Krebbyg once and knows where the messages go (`campaign/guides/factions/08-bregan-daerthe.md:85`). He knows the destination and spies for Luskan, and his Notable Figures page now says so. He has not worked out that the cloaked drow belong to Bregan D'aerthe."
> — `campaign/gazetteer/waterdeep/trades-ward.md:249`

Campaign, the Factions Guide:

> "Use the description from DH p. 63. Fenerus collects messages from dead drops throughout the Trades Ward and stores them at the house; Krebbyg picks them up every two days. Fenerus isn't supposed to know where the messages go, but he followed Krebbyg once and does."
> — `campaign/guides/factions/08-bregan-daerthe.md:85`

### A5. The house on Quill Alley (a message drop; rented; alone)

Adventure, the house:

> "The characters' quest for the {@item Stone of Golorr|WDH} first leads them to Fenerus Stormcastle, a lamplighter who rents a small house in the Trades Ward ({@area L1|140})."
> — `sources/adventure-wdh.json:7087`

Campaign, the gazetteer:

> "**Fenerus Stormcastle's House** — Small house and message drop, Quill Alley"
> — `campaign/gazetteer/waterdeep/trades-ward.md:61`

> "- A small house that the lamplighter Fenerus rents in an alley. Residents of the ward know him, and a map marks the alley with his name."
> — `campaign/gazetteer/waterdeep/trades-ward.md:62`

> "- Fenerus Stormcastle's house on Quill Alley is a Bregan D'aerthe message drop. Fenerus gathers messages from dead drops across the ward and stores them at the house, and Krebbyg Masq'il'yr collects them every two days. The messages are coded in Drow, and they point the party to the **Sea Maidens Faire**."
> — `campaign/gazetteer/waterdeep/trades-ward.md:37`

Adventure, the map (the Jarlaxle variant, page 63):

> "If Jarlaxle is the villain, \"Fenerus Stormcastle\" is written by the X on a map of the Trades Ward. (Residents of the Trades Ward know Fenerus. He's a lamplighter with an alley dwelling. The X marks the alley.)"
> — `sources/adventure-wdh.json:6203`

### A6. Personal ties (day-one)

Campaign, the Trollskull community entry (the acquaintance):

> "**Relationships.** Jenks is Nat's steadiest companion, Squiddly's reluctant foil, and an acquaintance of Fenerus Stormcastle (the lamplighter they see on their rounds)."
> — `campaign/setting/notable-figures/trollskull-community/13-jenks.md:25`

Campaign, Krebbyg (the courier who collects from Fenerus):

> "**Relationships.** Krebbyg is the close friend and operational partner of Fel'rekt Lafeen, Jarlaxle's logistics lieutenant (collecting messages from Fenerus Stormcastle for the Scarlet Marpenoth), and the operating cover manager of the Seven Masks Theater."
> — `campaign/setting/notable-figures/bregan-daerthe/04-krebbyg-masqilyr.md:25`

Campaign, the Manshoon note (day-one: he is a soft target; present tense):

> "- **Bregan D'aerthe (wary rival):** Manshoon treats Jarlaxle as the only Grand Game player he takes seriously, and the two keep a fragile non-interference arrangement (**Manshoon**). `[research]` The Villains page tags the arrangement and the rating as unsourced. Manshoon has marked Fenerus Stormcastle, whom he has identified as a Bregan D'aerthe cut-out, as a soft target (**Trades Ward**; **Running the Villains**)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:87`

Adventure, Mirt's grudge against the Posse (page 83, quest context; the grudge is a fact about Mirt):

> "{@creature Mirt|WDH} has personally lost coin to the Blood Hawk Posse, so helping Fenerus squirm out of jail stings him deeply."
> — `sources/adventure-wdh.json:10628`

### A7. Faith, belongings, and a sign of the trade

No source gives Fenerus a faith. No source gives him a signature belonging. The message drop has no object tied to him except the coded messages (`campaign/gazetteer/waterdeep/trades-ward.md:37`, quoted under A5).

### A8. How long in post

Not dated. The Factions Guide says he followed Krebbyg "once" (`campaign/guides/factions/08-bregan-daerthe.md:85`). The wiki says he was the company's "primary spy" without a date (wiki line 68). The page says "a decade of brigandage and a quiet retirement" (`06-fenerus-stormcastle.md:13`), which is the only span given.

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, the page: "*Tethyrian human bandit captain (retired brigand), neutral, he/him*. Stat block: **Bandit Captain**." — `campaign/setting/notable-figures/bregan-daerthe/06-fenerus-stormcastle.md:5`
- Campaign, the gazetteer: "**Fenerus Stormcastle (Neutral, Tethyrian Human, he/him)**" — `campaign/gazetteer/waterdeep/trades-ward.md:120`
- Campaign, the organization page: "Tethyrian human cut-out and message-drop, neutral." — `campaign/setting/organizations/07-bregan-daerthe.md:104`
- Wiki: `| alignment5e    = [[Neutral]]` — wiki line 57 (5e). Consistent.
- Adventure: no alignment given.

**Species**
- Campaign, the page: "Tethyrian human" (`06-fenerus-stormcastle.md:5`).
- Wiki: `| race           = [[Human]]` (wiki line 14) and `| ethnicity      = [[Tethyrian]]` (wiki line 15). Consistent.
- Adventure: no species given beyond "a lamplighter" (`sources/adventure-wdh.json:7087`).

**Pronouns**
- Campaign, the page: "he/him" (`06-fenerus-stormcastle.md:5`).
- Campaign, the gazetteer: "he/him" (`trades-ward.md:120`).
- Campaign, the Guilds page: "he/him" (`guilds.md:54`).
- Wiki: `| sex            = Male` (wiki line 13). Consistent.
- Stale: `campaign/gazetteer/waterdeep/trades-ward.md:252` says "His Notable Figures page has no pronoun tag, and its prose uses 'he' and 'man'". The page now has "he/him" at line 5. This note is stale.

**Stat block**
- Campaign, the page: "Stat block: **Bandit Captain**." (`06-fenerus-stormcastle.md:5`).
- Campaign, the Factions Guide: "**Roster:** Fenerus Stormcastle (**Bandit Captain**) with no permanent guards." — `campaign/guides/factions/08-bregan-daerthe.md:97`
- Wiki: `| class5e        = [[Bandit]]` (wiki line 59) and `refs5e         = <ref name="WDH5e-p83">{{Cite book/Waterdeep: Dragon Heist|83}}</ref>` (wiki line 60). The wiki gives the class "Bandit", not a stat block name. Not a conflict.
- Adventure: no stat block for Fenerus is given.

---

## C. Sentences on the current page that narrate quest-time or depend on a discovery

Current page: `campaign/setting/notable-figures/bregan-daerthe/06-fenerus-stormcastle.md`. The page has no Background, Personality or Connections section yet.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Tethyrian human bandit captain (retired brigand), neutral, he/him*. Stat block: **Bandit Captain**." | Day-one. Stat block sourced (B) | `06-fenerus-stormcastle.md:5`; `08-bregan-daerthe.md:97` |
| 2 | L6 | "**Affiliation:** Bregan D'aerthe (cut-out who spies for Luskan and has worked out where the messages go)" | Day-one. Knows the destination, not the drow's identity (A4). The affiliation follows the organization page's Key Members line (`07-bregan-daerthe.md:104`) | `trades-ward.md:38`, `:249` |
| 3 | L7 | "**Featured in:** **Gralhund Villa**, **Faction Outposts**, **Sea Maidens Faire**" | Quest references | `campaign/quests/act-ii/gralhund-villa/ev-08-the-rooftop-chase.md:21`; `campaign/structure/arc-e-faction-outposts.md:299`; `campaign/structure/arc-h-sea-maidens-faire.md:335` |
| 4 | L11 | "**Resonance.** Fenerus should inspire wariness with a man who has a long criminal record and no reason to be honest; grudging respect when what he knows about the messages proves real; and sympathy for the impossible position that placed him at the intersection of every faction's interest simultaneously." | "grudging respect when what he knows about the messages proves real" is a discovery-time clause (the party verifies the messages). The "impossible position" clause is day-one: four factions want him (`09-manshoons-zhentarim.md:87`; `08-bregan-daerthe.md:85`) | Verification: `campaign/structure/arc-e-faction-outposts.md:315` ("Fenerus's testimony — if he is present and cooperative — confirms that messages travel to a contact at the Faire"). Position: `09-manshoons-zhentarim.md:87` |
| 5 | L13 | "**Emotions.** Fenerus most often feels calculating watchfulness, practiced evasion, a criminal's patience honed over a decade of brigandage and a quiet retirement, contempt for anyone who thinks threats work faster than deals, and an exhaustion he has worn so long it looks like indifference." | Day-one habits | `trades-ward.md:122` ("He wants immunity and a quiet life, and he survives by saying little.") |
| 6 | L15 | "**Motivations.** Fenerus wants to trade what he knows about the messages for immunity and nothing less, survive the overlapping interest of the Zhentarim, Xanathar's Guild, and Bregan D'aerthe, and live long enough to see the arrangement concluded cleanly." | "for immunity" is the bargain he makes once questioned: "Fenerus refuses to divulge the stone's location until he is released and granted immunity for his past crimes." (`sources/adventure-wdh.json:10657`, quest-time). Day-one intent: "He wants immunity and a quiet life" (`trades-ward.md:122`). "the overlapping interest of the Zhentarim" is day-one (`09-manshoons-zhentarim.md:87`). "Xanathar's Guild" is quest-time (the duergar search, `sources/adventure-wdh.json:7126`) | `trades-ward.md:122`; `sources/adventure-wdh.json:10657` |
| 7 | L17 | "**Inspirations.** When playing Fenerus, channel Walter White (*Breaking Bad*, early seasons), Jimmy McGill (*Better Call Saul*), and Red Reddington (*The Blacklist*)." | Not a fact | n/a |
| 8 | L21 | "**Persona.** To the world, Fenerus Stormcastle is a big, scar-faced man with gray hair who lights lamps in the Trades Ward and minds his own business. To those who question him, he is a practiced liar who has long since decided what his silence is worth and what he will give up first. Deep down, he knows where the messages he gathers are taken, because he once followed the drow who collects them, and he has been wondering what that knowledge is worth." | All day-one: appearance (`sources/adventure-wdh.json:7104`), the lamps (`trades-ward.md:121`), the following of Krebbyg (`trades-ward.md:38`). "To those who question him" is general, not a discovery | `trades-ward.md:121`; `08-bregan-daerthe.md:85` |
| 9 | L23 | "**Morale.** In a fight, Fenerus disengages immediately. He has survived too many of the wrong kinds of fights to start one he did not choose." | Day-one habit. No campaign file names an encounter for him | n/a |
| 10 | L25 | "**Relationships.** Fenerus is the former founder of the Blood Hawk Posse (current brigands on the Amphail road), a Bregan D'aerthe cut-out and message-drop on Quill Alley, and the target of Manshoon's kidnap directive in **Faction Outposts**." | "the target of Manshoon's kidnap directive in Faction Outposts" is quest-time. The day-one version is "Manshoon has marked Fenerus Stormcastle, whom he has identified as a Bregan D'aerthe cut-out, as a soft target" (`09-manshoons-zhentarim.md:87`). The Posse clause is day-one (`sources/adventure-wdh.json:7123`) | Directive: `campaign/guides/factions/10-manshoons-zhentarim.md:23`; `campaign/structure/arc-e-faction-outposts.md:305` |
| 11 | L29 | "A big, scar-faced lamplighter in the Trades Ward who minds his own business and has been wondering what he knows about the message drop is worth." | Day-one public face. 26 words (brief limit 21). "the message drop" is a day-one fact but a secret one (`trades-ward.md:37`); keep it out of the public Overview if the drafter agrees | `trades-ward.md:121`; `trades-ward.md:37` |

**Voice profile (`.claude/skills/character-voices/voices/bregan-daerthe.md`, "### Fenerus Stormcastle" at lines 116 to 130)**

Tagline, line 117: "*A scarred ex-brigand who talks in careful deals and says nothing for free.*" (day-one)

> "- **Sound:** A deep, gravelly, tired voice, slow and deliberate." — line 119 (day-one)

> "- **Sentence shape:** Measured sentences that circle the point, and conditional offers (\"If I had something, and I'm not saying I do…\")." — line 120 (day-one)

> "- **Word choice:** Lawyer-ish criminal caution: immunity, \"in writing\", \"a signed release\". He calls interrogators \"friend\" with heavy irony." — line 121 (day-one; "a signed release" is the bargain for an arrest, see C10 and D1)

> "- **Swearing:** *Casual · Plain · Phrase.* Worn and casual (\"I've had ten years of shit. Yours is small.\")." — line 122 (day-one; keep as written, adult table)

> "- **Personality in speech:** Calculating, evasive and exhausted. He's contemptuous of threats and says so calmly. He gives a little to show he has more." — line 123 (day-one)

> "- **Quirks:** He taps the table for \"in writing\". He answers every question with the price of answering." — line 124 (day-one)

> "- **Signature phrases:** \"In writing.\" / \"I'm not saying I do.\" / \"Threats are slow, friend. Deals are fast.\"" — line 125 (day-one)

> "- **Never:** He never reveals the Stone's location without immunity, never raises his voice, and never trusts a promise that isn't signed." — line 126 (**quest-time clause**: "the Stone's location" is a discovery-time fact; see D2 and Finding 2. Restate or remove under ruling 3)

> "  - *Greeting:* \"Lamplighter. Retired from the other thing. What do you want, friend?\"" — line 128 (day-one)

> "  - *Business:* \"Signed release from a magister or a Lord, in writing, and I'll draw you a map. Not before.\"" — line 129 (**quest-time clause**: a magister's release is the arrest bargain (`sources/adventure-wdh.json:10645`, "A character tells the magister about the hidden cache of dragons and Fenerus's role in finding it."); the map is the Stone. See D1 and D2)

> "  - *Under pressure:* \"Go ahead. Then nobody gets it. Threats are slow, friend.\"" — line 130 (**quest-time clause**: "Then nobody gets it" refers to the Stone; see D2)

Quest-time clauses in the Fenerus profile for the rule-16 restatement: line 126 ("the Stone's location"), line 129 ("Signed release from a magister" and "I'll draw you a map") and line 130 ("nobody gets it"). No profile line narrates an arrest in words; the arrest is implied by "a signed release" and "magister". No profile line has been changed yet; the drafter will report changes.

---

## D. Conflicts

**D1. Was Fenerus arrested?**
- Wiki: "In [[1492 DR]],{{WDH-time}} while under pressure from the [[Lords' Alliance]], the [[Lords of Waterdeep]] ordered the [[City Watch (Waterdeep)|City Watch]] to arrest Fenerus for his past crimes." — wiki line 70 (`WDH5e-p63`)
- Adventure: "Agents of the Lords' Alliance recently labeled Fenerus as a wanted brigand and notified the Lords of Waterdeep, who sent the City Watch to arrest him." — `sources/adventure-wdh.json:7125`
- Adventure, Jarlaxle's account: "I've learned that Fenerus Stormcastle was arrested by the City Watch for theft and taken to a courthouse in the Castle Ward to face the judgment of a magister." — `sources/adventure-wdh.json:9090`
- Adventure, the Dock Ward variant: "Fenerus has a criminal history and is currently in trouble with the law." — `sources/adventure-wdh.json:6171`
- Campaign, settled (Session 51): "He is not a Watch prisoner and did not hide the Stone before an arrest." — `campaign/gazetteer/waterdeep/trades-ward.md:250`
- Rank: campaign over adventure and wiki. The page must not mention an arrest, a courthouse or a magister's release as a fact. The Motivations and Voice lines that depend on a release are routed (C6 and the voice block).

**D2. Did he hide the Stone?**
- Wiki: "He hid the artifact before being arrested but to reveal the location Fenerus wanted to be released and have immunity for his past crimes." — wiki line 72 (`WDH5e-p83`)
- Adventure, the house: "Fenerus had the good sense to hide the {@item Stone of Golorr|WDH} elsewhere and hopes to use it as leverage to gain his freedom as well as forgiveness for past crimes." — `sources/adventure-wdh.json:7125`
- Adventure, the cauldron: "Fenerus hid the {@item Stone of Golorr|WDH} in the cauldron that hangs in the fireplace on the upper level ({@area O3|1ac}). But it's not there anymore." — `sources/adventure-wdh.json:9719`
- Adventure, the tower: "Fenerus hid the {@item Stone of Golorr|WDH} on the top floor of an old tower in the Dock Ward-a tower warded against all forms of magic." — `sources/adventure-wdh.json:10667`
- Campaign, settled (Session 51): "He is not a Watch prisoner and did not hide the Stone before an arrest." — `trades-ward.md:250`
- Campaign, the lore file: "- **Settled:** Files that put the Stone in the wrong hands." and, in the same entry, "`notable-figures/bregan-daerthe/06-fenerus-stormcastle.md` no longer say that Amath holds the Stone, that Agorn entrusted it to her, or that Fenerus hid it." — `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:184`
- Rank: campaign over adventure and wiki. The page must not say he hid the Stone.

**D3. Where the Stone goes after the chase**
- Adventure, the Dock Ward variant: "If Jarlaxle is the villain, the stone is delivered to Fenerus Stormcastle, a lamplighter in the Trades Ward." — `sources/adventure-wdh.json:6171`
- Campaign, Gralhund Villa, the conditional heading: "### If the Chase Fails" (`campaign/quests/act-ii/gralhund-villa/ev-08-the-rooftop-chase.md:62`)
- Campaign, Gralhund Villa, the branch: "The Stone reaches its destination:" (`ev-08-the-rooftop-chase.md:64`)
- Campaign, Gralhund Villa, the branch: "- **BD team:** The Stone reaches Fenerus Stormcastle. Jarlaxle holds it." (`ev-08-the-rooftop-chase.md:67`)
- Campaign, Gralhund Villa, the chase: "They move fast and know where they are going: a BD outpost in the Trades Ward (Fenerus Stormcastle)." — `ev-08-the-rooftop-chase.md:21`
- Campaign, Gralhund Villa, the aftermath: "(**Stone Secured** and **Stone Recovered** are both unmarked, and Fel'rekt took it in ev-06 or ev-07 or it reached Fenerus Stormcastle when the ev-08 chase failed)" — `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:85`
- Rank: campaign. The Stone reaches his house only if the chase fails. Routed to Gralhund Villa.

**D4. Did Xanathar's men take the Stone from his house?**
- Adventure: "Korgstrod Uxgulm, the duergar leader, has what he believes to be the {@item Stone of Golorr|WDH}. He found it during a search of Fenerus's house in the Trades Ward." — `sources/adventure-wdh.json:12015`
- Campaign, settled: "**Settled (user ruling, Session 51):** The fake Stone of Golorr is cut from this page." — `campaign/setting/notable-figures/xanathars-guild/10-korgstrod-uxgulm.md:119`; the same entry says the adventure's "Stone of Deception" sidebar "is not used, and neither is its Fenerus search." (`:119`)
- Rank: campaign. The Korgstrod search is cut. The house ransacking (D7) is also adventure-only.

**D5. What he knows of the drow**
- Adventure: "He has no clue that his contacts are drow members of Bregan D'aerthe" — `sources/adventure-wdh.json:7124`
- Campaign (settled): "He knows the destination and spies for Luskan, and his Notable Figures page now says so. He has not worked out that the cloaked drow belong to Bregan D'aerthe." — `trades-ward.md:249`
- Campaign, the Factions Guide: "Fenerus isn't supposed to know where the messages go, but he followed Krebbyg once and does." — `08-bregan-daerthe.md:85`
- Campaign, the organization page: "once followed Krebbyg after a pickup and knows the messages go to the Sea Maidens Faire" — `07-bregan-daerthe.md:104`
- Rank: campaign. The page's line 6 and Persona (line 21) follow the campaign. No conflict remains on the page.

**D6. How often the messages are collected**
- Campaign: "Krebbyg Masq'il'yr collects them every two days" — `trades-ward.md:37`; "Krebbyg picks them up every two days" — `08-bregan-daerthe.md:85`; "for Krebbyg to collect every two days" — `campaign/setting/organizations/07-bregan-daerthe.md:75`
- Alexandrian markdown: "with updates transmitted twice daily to Fenerus Stormcastle via message drop" — `sources/Act_III_Arc_E.md:74`
- Rank: campaign. The Alexandrian line is about the Gralhund team's updates, not Krebbyg's pickups. Flag for the orchestrator only if the Background mentions frequency.

**D7. Was his house ransacked?**
- Adventure: "The door to Fenerus's house stands open, and the place has been ransacked. Painted in blood on the kitchen wall is a circle with ten equidistant lines radiating outward from its circumference: the sign of {@creature Xanathar|WDH}." — `sources/adventure-wdh.json:7114`
- Campaign: no line found. A search of `campaign/` for "ransack" returned only unrelated hits (`campaign/quests/faction-events/doom-raiders/m04-silencing-skeemo/ev-03-the-reckoning.md:110`). The Trades Ward gazetteer and the Factions Guide describe the house without this scene.
- Rank: campaign has no counterpart. Adventure-only, quest-time. Not for the page.

**D8. Affiliation label and what he believes**
- Page, line 6: "**Affiliation:** Bregan D'aerthe (cut-out who spies for Luskan and has worked out where the messages go)" — `06-fenerus-stormcastle.md:6`
- Organization page, Key Members: "Tethyrian human cut-out and message-drop, neutral." — `07-bregan-daerthe.md:104`
- Adventure: "spying for the city of Luskan" and "He has no clue that his contacts are drow members of Bregan D'aerthe" — `sources/adventure-wdh.json:7124`
- Rank: the page and the organization page agree. The adventure gives him the Luskan belief. Both are kept, and the conflict is in what he believes, not in the label.

**D9. Featured in**: the page lists three quests (line 7). `ev-08-the-rooftop-chase.md:21` (Gralhund Villa), `arc-e-faction-outposts.md:299` (Faction Outposts, 7A) and `arc-h-sea-maidens-faire.md:335` (Sea Maidens Faire, Scene 4) all name him. Consistent.

**D10. Stat block name**: the page and the Factions Guide say "Bandit Captain" (`06-fenerus-stormcastle.md:5`; `08-bregan-daerthe.md:97`). The wiki says class "Bandit" (wiki line 59). Not a conflict.

**D11. Ward and address**: consistent. "Trades Ward" and "Quill Alley" are in `trades-ward.md:37`, `:61`, `:120`, and on the page at lines 21 and 25. The adventure places him in the Trades Ward at `sources/adventure-wdh.json:7087`.

---

## E. Stale lines in other files (not edited) and routed quest references

**Stale lines in other files**
- `campaign/gazetteer/waterdeep/trades-ward.md:252` ("Fenerus's pronouns. His Notable Figures page has no pronoun tag"). The page now has "he/him" (line 5). Stale.
- `campaign/setting/governance-and-guilds/guilds.md:122` says "`06-fenerus-stormcastle.md` line 7 says he spies for Luskan and has worked out where the messages go". The line is 6 now. Line 7 is Featured in. Stale citation.
- `sources/research/pass4-bundles/jarlaxle/campaign-hits.txt:54` (quotes `trades-ward.md:40`: "Fenerus believes his contacts are Luskan agents") and `:59` (quotes `trades-ward.md:261`: "His Notable Figures page says he hid the Stone before his arrest"). Older text. Stale; the bundle is out of date.
- `sources/Act_III_Arc_E.md:74` ("updates transmitted twice daily to Fenerus Stormcastle via message drop"). Conflicts with the campaign (D6). Alexandrian rank.
- `campaign/setting/villains/jarlaxle.md:114` ("Manshoon has identified Fenerus Stormcastle as a Bregan D'aerthe cut-out and ordered his abduction, and Jarlaxle will act unilaterally if the abduction proceeds.") The directive is quest-time (`campaign/guides/factions/10-manshoons-zhentarim.md:23`). Stated as present fact on the Villains page.
- `campaign/guides/gm-guide/running-the-villains.md:75` ("Manshoon has identified Fenerus Stormcastle as a D'aerthe cut-out and ordered his abduction.") Same issue.
- `campaign/guides/gm-guide/grand-game-in-play.md:65` ("Manshoon has identified Fenerus Stormcastle as a Bregan D'aerthe cut-out and ordered his abduction.") Same issue.
- `campaign/setting/notable-figures/manshoons-zhentarim/07-zorbog-jyarkoth.md:122` and `06-avareen-windrivver.md:125` cite the directive as a routed item. They are consistent with routing.
- `campaign/structure/arc-d-gralhund-villa.md:302` ("The Stone reaches a Bregan D'aerthe outpost (Fenerus Stormcastle in the Trades Ward)"). The arc-d doc is superseded by the Gralhund Villa journal; the journal's conditional version governs (D3).
- `campaign/quests/act-ii/gralhund-villa/design-notes.md:5` critiques the published adventure's Fenerus or Grinda variant. No change to Fenerus's facts.
- `campaign/setting/notable-figures/xanathars-guild/10-korgstrod-uxgulm.md:119` cuts the Fenerus search (D4). Correct as settled.

**Routed to Faction Outposts (the house as an outpost; the kidnap)**
- `campaign/structure/arc-e-faction-outposts.md:211` "*Intel Yield.* ... The *Directive to Zorbog* naming Fenerus Stormcastle — a cross-faction thread pointing toward Bregan D'aerthe (Fenerus is a BD lamplighter; Manshoon has identified him as a soft target)." (the ellipsis skips "Manshoon's name (first use in the campaign). The pass-amulet from Avareen (route to Kolat Towers). Ott Steeltoes as a potential **Xanathar's Lair** contact.")
- `campaign/structure/arc-e-faction-outposts.md:299` "#### 7A: Fenerus Stormcastle's House (Encounter-Plus)"
- `campaign/structure/arc-e-faction-outposts.md:303` "*Approach.* Three paths to Fenerus: the Seven Masks Theater intelligence archive (a letter from \"K\" to \"J\" referencing Fenerus as a BD field contact and his address at Quill Alley); the *Directive to Zorbog* from the Interrogation House (Manshoon is targeting Fenerus — his address is in the directive); or a captured BD response team member's *Sealed Letter from Krebbyg*, naming Fenerus as a message recipient."
- `campaign/structure/arc-e-faction-outposts.md:305` "*The Kidnap Complication.* The *Directive to Zorbog* orders Fenerus captured within four days of issuance. This complication is live — it fires 1d6+2 days after the directive is issued, regardless of whether the party acts. Three possible states when the party arrives at Quill Alley:"
- `campaign/structure/arc-e-faction-outposts.md:307`, `:309`, `:311` (the three states: warned, arrives during the kidnap, arrives after the kidnap)
- `campaign/structure/arc-e-faction-outposts.md:315` "*Intel Yield.* ... Fenerus's testimony — if he is present and cooperative — confirms that messages travel to a contact at the Faire and that \"Rongquan Mystere\" is not the theater owner's real identity." (the ellipsis skips "Decoded messages provide multiple independent paths to the Sea Maidens Faire as the next target.")
- `campaign/structure/arc-e-faction-outposts.md:317` (escalation and the kidnap clock)
- `campaign/structure/arc-e-faction-outposts.md:333` (the letter from K to J: "warning that Fenerus's address has become known to a third party and recommending a new message drop")
- `campaign/structure/arc-e-faction-outposts.md:419` "8. **Fenerus kidnap timing.** Directive arrives live at the Interrogation House. Kidnap fires 1d6+2 days later."
- `campaign/guides/factions/10-manshoons-zhentarim.md:23` "While the party explores, a flying snake arrives with *A Directive to Zorbog* signed by \"Manshoon,\" ordering Zorbog to kidnap Fenerus Stormcastle of Quill Alley, a \"known associate of these new meddlers in the Grand Game.\""
- `campaign/guides/factions/08-bregan-daerthe.md:83` "### Fenerus Stormcastle's House — Encounter-Plus (Trades Ward, Quill Alley)"; `:97` roster; `:99` escalation ("If Fenerus has already been kidnapped before the party arrives, no escalation triggers"); `:107` (the letter from K to J); `:128`-`:131` (revelation list); `:135`, `:141`, `:142` (message contents)
- `campaign/guides/gm-guide/running-the-villains.md:75` (Manshoon vs. Bregan D'aerthe escalation)

**Routed to Gralhund Villa (the Stone's route; the rooftop chase)**
- `campaign/quests/act-ii/gralhund-villa/ev-08-the-rooftop-chase.md:21` (the BD team exits to "a BD outpost in the Trades Ward (Fenerus Stormcastle)")
- `campaign/quests/act-ii/gralhund-villa/ev-08-the-rooftop-chase.md:62`-`:67` ("If the Chase Fails"; quoted under D3)
- `campaign/gazetteer/waterdeep/trades-ward.md:10` "**Gralhund Villa** sends a Bregan D'aerthe team across the rooftops to Fenerus Stormcastle's house if the Stone leaves the villa in **The Rooftop Chase**."
- `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:85` (the package at Trollskull Manor if BD holds the Stone; quoted under D3)
- `campaign/quests/act-ii/gralhund-villa/design-notes.md:5` (the published adventure's variant)

**Routed to Sea Maidens Faire**
- `campaign/structure/arc-h-sea-maidens-faire.md:335` "- **Faction Outposts, Scene 4 (BD Outposts)** — Fenerus Stormcastle's house, Seven Masks Theater. Escalation tier entering this quest. Decoded messages confirming intelligence flows to the Faire. Malkolm Brizzenbright's ghost testimony about \"Rongquan Mystere.\""
- `campaign/structure/arc-h-sea-maidens-faire.md:337` "- **Notable Figures** — Full NPC profiles for Jarlaxle, Soluun, Fel'rekt, Krebbyg, Zelifarn, Margo Verida, Khafeyta Murzan, Fenerus Stormcastle, Malkolm Brizzenbright."
- `campaign/gazetteer/waterdeep/trades-ward.md:37` ("they point the party to the **Sea Maidens Faire**") — day-one as a fact about the messages; the party's discovery is quest-time.

**Other campaign files that name him (no action)**
- `campaign/gazetteer/waterdeep/dock-ward.md:149` (Krebbyg's errand), `:266` (Trades Ward list)
- `campaign/gazetteer/waterdeep/trades-ward.md:33`, `:34`, `:227`, `:234`, `:235` (ward lists)
- `campaign/setting/geography/waterdeep.md:42`, `:100` (ward lists; "Faction Outposts" list)
- `campaign/setting/governance-and-guilds/code-legal-and-magisters.md:105` (Barch hears Fenerus's visitors in the Castle Ward courthouse, derived from `sources/adventure-wdh.json:9090`; quest-time)
- `campaign/guides/trollskull-manor/06-tavern-time.md:45` (Faction Outposts list)
- `campaign/setting/notable-figures/trollskull-community/13-jenks.md:25` (acquaintance; quoted under A6)

---

## F. Gaps a Background would need that no source gives

For each gap: the sourced facts the drafter must stay consistent with.

1. **Birthplace, birth year, childhood, parents.** No source. Wiki `parents`, `spouses`, `siblings`, `children` are blank (wiki lines 29 to 32 in that file). `dob` and `age` are blank (wiki lines 17, 21, 22). The page's Persona line gives no childhood.
2. **Date he joined the Guild of Chandlers and Lamplighters.** No source. The Guild is named (`sources/adventure-wdh.json:7123`; `guilds.md:54`). The lamplighter post is in the Trades Ward (`trades-ward.md:121`).
3. **The Blood Hawk Posse: the date he founded it, the raid, and the year he was ousted.** No date in any source. The botched raid is unspecified (`sources/adventure-wdh.json:7123`; wiki line 68: "after a failed raid"). The Posse harries "travelers on the road to Amphail" (`sources/adventure-wdh.json:7123`) and is "current brigands on the Amphail road" (page line 25).
4. **How he came to Luskan's notice, and when his spying began.** No source gives a date or a first contact. The spying is "Until recently" (`sources/adventure-wdh.json:7124`). The wiki says he "unknowingly became the primary spy of Bregan D'aerthe" (wiki line 68), with no date.
5. **His "decade of brigandage."** The page says "a criminal's patience honed over a decade of brigandage and a quiet retirement" (line 13). No other source gives the decade. It sits with the Blood Hawk story and the ousting, which are undated.
6. **How he met Krebbyg or the rest of the drow.** "he followed Krebbyg once" (`trades-ward.md:38`). No date, no place, and no contact beyond the message drop.
7. **Any romance, child, friend or pet.** None. "they know nothing more about him, other than that he lives alone" (`sources/adventure-wdh.json:7104`). The only named acquaintance is Jenks, "an acquaintance of Fenerus Stormcastle (the lamplighter they see on their rounds)" (`13-jenks.md:25`).
8. **His faith, his home before Waterdeep, and his real name.** None. The name is given as "Fenerus Stormcastle" (`sources/adventure-wdh.json:117`); no alias is given.
9. **Personal goals.** The page's Motivations: "live long enough to see the arrangement concluded cleanly" (line 15). The campaign's gazetteer: "He wants immunity and a quiet life, and he survives by saying little." (`trades-ward.md:122`). No source gives a personal goal outside the bargain. A goal must not contradict the Stone's routing (D2, D3) or the arrest's absence (D1).
10. **His own view of the Blood Hawk Posse now.** None. The page says it is "current brigands on the Amphail road" (line 25). No source gives his feelings about the gang he founded.

---

## G. Inner-life hints (exact quotes; for the Background and the personal goals, brief ruling 17)

- The bargain he wants: "He wants immunity and a quiet life, and he survives by saying little." — `campaign/gazetteer/waterdeep/trades-ward.md:122`
- Exhaustion: "an exhaustion he has worn so long it looks like indifference." — `06-fenerus-stormcastle.md:13`
- Long patience: "a criminal's patience honed over a decade of brigandage and a quiet retirement" — `06-fenerus-stormcastle.md:13`
- Wondering what he knows is worth: "and he has been wondering what that knowledge is worth." — `06-fenerus-stormcastle.md:21`; "has been wondering what he knows about the message drop is worth" — `06-fenerus-stormcastle.md:29`
- Survival: "live long enough to see the arrangement concluded cleanly." — `06-fenerus-stormcastle.md:15`
- Lives alone, with scars: "other than that he lives alone." — `sources/adventure-wdh.json:7104`; "the scars he wears on his face" — `sources/adventure-wdh.json:7104`
- The gang that bears his name still raids: "a gang of horse-riding brigands that, to this day, harries travelers on the road to Amphail." — `sources/adventure-wdh.json:7123`
- Ousted from his own gang: "When he was drummed out of the gang after a botched raid" — `sources/adventure-wdh.json:7123`
- A grudge against the Posse held by someone else: "{@creature Mirt|WDH} has personally lost coin to the Blood Hawk Posse" — `sources/adventure-wdh.json:10628` (quest context: jail)
- Contempt for threats: "contempt for anyone who thinks threats work faster than deals" — `06-fenerus-stormcastle.md:13`; "Threats are slow, friend. Deals are fast." — voice line 125
- Wry toughness: "I've had ten years of shit. Yours is small." — voice line 122 (`ten years` echoes "a decade" on page line 13)
- A greeting that names his past: "Lamplighter. Retired from the other thing." — voice line 128
- Wants things in writing: "In writing." — voice line 125; "He taps the table for \"in writing\"." — voice line 124
- Scarred and grey: "A big, scar-faced lamplighter with gray hair" — `trades-ward.md:121`
- Irony toward interrogators: "He calls interrogators \"friend\" with heavy irony." — voice line 121
- Calm when threatened: "In a fight, Fenerus disengages immediately. He has survived too many of the wrong kinds of fights to start one he did not choose." — `06-fenerus-stormcastle.md:23`

---

## Report completeness

- Every fact on the page's Summary, Roleplaying Information, Character Information and Overview is quoted or listed in C.
- The voice profile is quoted for every line that changes (C, voice block).
- Searched and found nothing about Fenerus: `campaign/setting/history/` (no Fenerus), `campaign/setting/lore/` (only the Stone settlement, `stone-of-golorr-and-the-eyes.md:184`), `sources/Act_III_Arc_D.md` (the Stone's fate, not a Fenerus fact), `sources/Appendix_B_-_Player_Factions.md` and `sources/Appendix_C_-_Player_Faction_Missions.md` (no Fenerus line).
- Not read: `sources/5. Faction Outposts.pdf` (no Fenerus house in the source guide's summary; page-by-page read not done); `sources/17. Outpost and Lair Revelation Lists.pdf` (the Krebbyg letter; the campaign's `guides/factions/08-bregan-daerthe.md:131` cites it); `sources/3. Player Character Factions.pdf` (Bregan D'aerthe membership, not checked for Fenerus).
