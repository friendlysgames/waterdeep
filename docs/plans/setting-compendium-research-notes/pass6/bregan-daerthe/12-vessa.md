# Pass 6 research notes: Vessa

Page: `campaign/setting/notable-figures/bregan-daerthe/12-vessa.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR. Vessa is already embedded in the Cassalanter social circle on day one, and she already knows the pact. Her Cassalanter Villa role (the operation, the Eye #3 adjustment) is quest time and is routed to **Cassalanter Villa**. Cassalanter secrecy applies in full: Vessa is the one route by which Jarlaxle knows about the pact, and no one outside the household and the cult knows it. The Lolth rule applies to the company. Brief ruling 2 makes her a major NPC, so the full Personality and Connections apply.
Organization page: `campaign/setting/organizations/07-bregan-daerthe.md`
Villains pages: `campaign/setting/villains/jarlaxle.md`, `campaign/setting/villains/cassalanters.md`
Factions Guide: `campaign/guides/factions/08-bregan-daerthe.md`. Vessa, Lymeria and Khafeyta are not named in it (searched).
Voice profile: `.claude/skills/character-voices/voices/bregan-daerthe.md` ("### Vessa", lines 222-236)
Wiki: NOT FOUND. `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-bregan-daerthe/12-vessa.txt` contains only the line `NOT FOUND`. A search of `sources/research/**/wiki.txt` for "Vessa", "Lymeria" and "Lhaurilstar" found no Vessa line; the one "Lhaurilstar" hit is a Castle Ward residence (D1 below).

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. `{@creature ...}` tags are left as written. The name Vessa does not appear in `sources/adventure-wdh.json` at all (a search of the file for "Vessa", "Lymeria" and "doppelganger" returned only the Bonnie passages below).
- Alexandrian: `sources/*.md` searched for "Vessa", "doppelganger", "spy" and "Lymeria": no Vessa line. The Alexandrian PDFs cannot be searched; `sources/10. Lair  Cassalanter Villa.pdf` and `sources/1. The Villains.pdf` were not checked for her.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDF and appendices, then the wiki (none).
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **The name "Lymeria Lhaurilstar" is the published adventure's alias for Bonnie, a different doppelganger.** The campaign page gives it to Vessa as her "full name" (`campaign/setting/notable-figures/bregan-daerthe/12-vessa.md:25`). The adventure says of Bonnie: "poses as a minor noblewoman going by the name Lymeria Lhaurilstar" (`sources/adventure-wdh.json:20414`). The campaign's session 18 decision made the switch on purpose (`session 18 handoff.md:54`). The drafter must know this (D1).
2. **Vessa is the only outsider who knows the pact, and every campaign file that names her says so.** The rule is consistent across the Villains, Organization, Gazetteer, History and Cassalanter pages (B and C). The one contradiction is in the voice profile, which says she "reports only to the captain" (`bregan-daerthe.md:229`). That is consistent, not in conflict.
3. **Her Relationships line is mostly quest time.** Its second half names the Cassalanter Villa operation and the Eye #3 adjustment (C, row 10). The day-one parts are her cover and her role as Jarlaxle's source.
4. **Her "Featured in: Sea Maidens Faire" has one weak line.** The only line in the Sea Maidens structure doc that names Vessa is a cross-reference (`campaign/structure/arc-h-sea-maidens-faire.md:341`), and it says her operation "previews" Jarlaxle's work (D2).
5. **No source gives her origin, age, or how she came to Jarlaxle.** Her Emotions and Persona give hints about her age and her face (G). Section F lists what the drafter must invent.

---

## A. Background facts by theme

### A1. Origin, birth, home, family, true form
No source gives any of these. The Persona gives her an unspecified long career in Waterdeep society:

> "**Persona.** To the world, \"Vessa\" is a noblewoman circulating through the Cassalanter banquet hall with the ease of someone who has been attending these events for months, which she has."
> — `campaign/setting/notable-figures/bregan-daerthe/12-vessa.md:21`

The campaign files give her doppelganger form and her cover as a human noblewoman:

> "- **Vessa**, a doppelganger, sits in the Cassalanter social circle under a permanent human cover. She is how Jarlaxle alone outside the household and the cult knows about the family's pact, and he does not tell Bregan D'aerthe members unless they work it out themselves (**A Debt in Blood**; the **Vessa** page)."
> — `campaign/setting/villains/jarlaxle.md:59`

### A2. How she joined and rose
No source gives how she joined the company or when. The Villains page's Background names her among the spies:

> "- **Vessa**, **Ryvarra** and **Quilm:** His operatives in the Cassalanter social circle, at the Yawning Portal and across the city, who send him intelligence."
> — `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:54`

The Organization page's Key Members line gives her rank as operative:

> "- **Vessa** — Doppelganger operative, neutral. Embedded in the Cassalanter social scene under a permanent human cover; Jarlaxle's primary intelligence source on the Cassalanters. See the **Vessa** page in Notable Figures."
> — `campaign/setting/organizations/07-bregan-daerthe.md:110`

### A3. Former life
No source gives one.

### A4. Faith
Not stated for Vessa. The campaign's rule for the company: "- **The Company Rejects Lolth:** Bregan D'aerthe has rejected Lolth as its goddess. No member worships her, keeps a shrine to her or invokes the Spider Queen with devotion, and members speak of her with contempt, as the goddess they walked away from. Soluun gives Jarlaxle the devotion that a drow of the houses would give her." — `campaign/setting/organizations/07-bregan-daerthe.md:46`

### A5. Signature belongings and skills
The voice profile gives her cover manner and signature lines (B and G). Her magical use is in the Morale line:

> "**Morale.** Vessa does not fight in the villa under any circumstances — her cover is the asset and she will not burn it. Exposed or cornered, she uses her read thoughts ability to identify what to say to exit the situation, and then says it. She will not enter the temple below the villa under any circumstances."
> — `campaign/setting/notable-figures/bregan-daerthe/12-vessa.md:23`

### A6. Relationships (named figures)

**Jarlaxle (her principal).** The Villains page:

> "- Jarlaxle knows about the Cassalanters' pact through Vessa and tells no Bregan D'aerthe member unless they work it out. Cassalanter imps watch the Sea Maidens Faire, and his counter-intelligence has not detected them."
> — `campaign/setting/villains/jarlaxle.md:115` (Relationship notes)

The Notable Figures page for Jarlaxle:

> "**Relationships.** Jarlaxle is the leader of Bregan D'aerthe, the secret lord of Luskan, the employer of Soluun, Fel'rekt, and Krebbyg, and a rival who may become an ally when offered something worth more than the gold. He has known of the Stone, the Eyes, and the vault since reaching Waterdeep, no later than Marpenoth 3, 1491 DR. He alone outside the household and the cult knows of the Cassalanter pact, through his doppelganger spy Vessa. Eye #3 is aboard the *Scarlet Marpenoth*."
> — `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:98`

The Organization page on the company's network, one full paragraph:

> "**The Waterdeep network:** Ryvarra watches the well at the Yawning Portal from the balcony, and Quilm files a weekly intelligence report for Jarlaxle. Fenerus Stormcastle's house on Quill Alley in the Trades Ward is a message drop, and a calligraphy shop in the same ward belongs to the company too. A grain factor's tallyman in the Field Ward is a company spy, and the merfolk broker Filthy Meg sells harbor intelligence to Jarlaxle for a ring of *true sight* she keeps as a retainer. Grinda Garloth, the Mistshore armorer, contracts to the company and to Xanathar's Guild alike. Vessa sits in the Cassalanter social circle, and Nar'l Xibrindas sits at Xanathar's side."
> — `campaign/setting/organizations/07-bregan-daerthe.md:67`

**The Cassalanters (the family she watches).** Vessa's role in the family's household: none is sourced. Her standing with them is "the social circle" only. The Cassalanter Notable Figures page for Caladorn:

> "- **Who knows the pact:** Nobody outside the household and the cult. Everyone else suspects the family because it is too nice to be this rich, and Jarlaxle alone knows more, through **Vessa**."
> — `campaign/setting/notable-figures/cassalanters/14-caladorn-cassalanter.md:88`

**Bonnie (a different doppelganger; same alias).** See D1. No relationship between Vessa and Bonnie is sourced.

**Featured in.** Her page's Summary:

> "- **Featured in:** **Cassalanter Villa**, **Sea Maidens Faire**"
> — `campaign/setting/notable-figures/bregan-daerthe/12-vessa.md:7` (see D2 for the Sea Maidens line)

### A7. Rank, post, time in post, stat
- Time in the Cassalanter circle: "has moved in Cassalanter society for months" (`campaign/quests/faction-events/bregan-daerthe/m02-the-wazoo-affair/ev-01-the-wazoo-affair.md:20`).
- Stat block: "Stat block: **Doppelganger**." (`campaign/setting/notable-figures/bregan-daerthe/12-vessa.md:5`). No numeric stat block is sourced.

### A8. Habits and temperament
Campaign voice and Persona lines (B and G).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, the page: "*Doppelganger, neutral, she/her*. Stat block: **Doppelganger**." — `campaign/setting/notable-figures/bregan-daerthe/12-vessa.md:5`
- Campaign, the org page: "- **Vessa** — Doppelganger operative, neutral. Embedded in the Cassalanter social scene under a permanent human cover; Jarlaxle's primary intelligence source on the Cassalanters. See the **Vessa** page in Notable Figures." — `campaign/setting/organizations/07-bregan-daerthe.md:110`
- Adventure: none (Vessa is not in the published adventure).
- Wiki: none (NOT FOUND stub).

**Species**
- Campaign, the page: "*Doppelganger, neutral, she/her*." — `12-vessa.md:5`
- Campaign, the Villains page: "- **Vessa**, a doppelganger, sits in the Cassalanter social circle under a permanent human cover." — `campaign/setting/villains/jarlaxle.md:59`
- Campaign, the org page: "Doppelganger operative" — `campaign/setting/organizations/07-bregan-daerthe.md:110`
- Voice profile: "*A doppelganger noblewoman fluent in every face at the banquet, and bored of her own.*" — `.claude/skills/character-voices/voices/bregan-daerthe.md:223`

**Pronouns**
- Campaign, the page: "she/her" (`12-vessa.md:5`). The Notable Figures page uses "she" in the Resonance, Emotions and Persona lines.
- No source gives a pronoun for Vessa beyond the campaign page. The voice profile uses "she" ("In truth she has read their thoughts and knows about the pact", `bregan-daerthe.md:229`). The pronoun table (`docs/plans/npc-pronouns-table-group-c.md`) was not searched for Vessa; searched only for Khafeyta.

**Name**
- Campaign, the page: "Vessa (full name Lymeria Lhaurilstar)" (`12-vessa.md:25`). "Vessa" is an operational alias in the campaign's own usage ("\"Vessa\" the BD operative", `campaign/structure/arc-g-cassalanter-villa.md:436`).
- Adventure: "Lymeria Lhaurilstar" appears once, for Bonnie (D1).

**Stat block**
- Campaign: "Stat block: **Doppelganger**." (`12-vessa.md:5`). No numeric stat block is sourced.

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/bregan-daerthe/12-vessa.md`. The page has no Background, no Personality and no Connections section yet. Each row gives the status and where the fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L5 | "*Doppelganger, neutral, she/her*. Stat block: **Doppelganger**." | Day-one (B). Keep | section B |
| 2 | L6 | "- **Affiliation:** Bregan D'aerthe" | Day-one. Keep | `campaign/setting/organizations/07-bregan-daerthe.md:110` |
| 3 | L7 | "- **Featured in:** **Cassalanter Villa**, **Sea Maidens Faire**" | Quest-name list. The Sea Maidens entry is weak (D2) | `campaign/structure/arc-g-cassalanter-villa.md:359` (Cassalanter Villa); `arc-h-sea-maidens-faire.md:341` (Sea Maidens, cross-reference only) |
| 4 | L11 | "**Resonance.** Vessa should inspire discomfort at the moment she briefly shows her true face to a BD-affiliated party member — a flash of gray, a knowing look, the implication that she has been watching longer than they have been looking — and then calibrated trust, because she is useful and she knows it." | Mixed. "a BD-affiliated party member" is a party-member framing (a quest register). The day-one part is the reveal to a BD member, which the voice profile permits (`bregan-daerthe.md:232`). Restate as a day-one trait, without "party" | `.claude/skills/character-voices/voices/bregan-daerthe.md:232` ("never shows her true face to anyone outside Bregan D'aerthe") |
| 5 | L13 | "**Emotions.** Vessa most often feels patient professional detachment, cold satisfaction in the quality of her cover, operational curiosity about how the party's infiltration is proceeding, and a very old, very contained disinterest in her own face." | Mixed. "how the party's infiltration is proceeding" is a Cassalanter Villa quest-time clause. Restate as curiosity about the infiltration in general | `campaign/structure/arc-g-cassalanter-villa.md:359` (the "reports the outcome" beat) |
| 6 | L15 | "**Motivations.** Vessa wants to maintain her cover in the Cassalanter social scene, observe the outcome of the **Cassalanter Villa** operation, and report accurate intelligence to Jarlaxle. She does not want to enter the temple." | "observe the outcome of the Cassalanter Villa operation" is quest time. Route it. The rest is day-one | `campaign/structure/arc-g-cassalanter-villa.md:359` |
| 7 | L17 | "**Inspirations.** When playing Vessa, channel Tatiana Maslany (*Orphan Black*), Mystique (*X-Men: First Class*), and Gus Fring (*Breaking Bad*)." | Not a fact. Keep | n/a |
| 8 | L21 | "**Persona.** To the world, \"Vessa\" is a noblewoman circulating through the Cassalanter banquet hall with the ease of someone who has been attending these events for months, which she has. To BD-affiliated party members who approach her, she provides a brief unambiguous signal — a flash of gray features, a knowing look — before returning to the social performance; to everyone else, she is a mysterious woman who seems to know too much. Deep down, she has been doing this long enough that she has to think before remembering what her own face looks like, and has decided this is probably fine." | Day-one, except "To BD-affiliated party members who approach her" (party framing, as row 4). Keep the rest | `campaign/quests/faction-events/bregan-daerthe/m02-the-wazoo-affair/ev-01-the-wazoo-affair.md:20` ("for months") |
| 9 | L23 | "**Morale.** Vessa does not fight in the villa under any circumstances — her cover is the asset and she will not burn it. Exposed or cornered, she uses her read thoughts ability to identify what to say to exit the situation, and then says it. She will not enter the temple below the villa under any circumstances." | Encounter register ("Exposed or cornered"). "does not fight in the villa" and "will not enter the temple" are day-one traits | `campaign/structure/arc-g-cassalanter-villa.md:247` (Willifort's combat line, a parallel) is not Vessa's; no source covers Vessa's combat. Flag |
| 10 | L25 | "**Relationships.** Vessa (full name Lymeria Lhaurilstar) is a Bregan D'aerthe doppelganger operative embedded in the Cassalanter social scene under a permanent human cover, Jarlaxle's primary intelligence source on the Cassalanter operation throughout **Cassalanter Villa**, a useful ally to BD-affiliated party members (distraction, cover stories, social-exposure suppression), and the source of the intelligence adjustment Jarlaxle makes to his Eye #3 strategy once **Cassalanter Villa** resolves." | First clause day-one (with the name in D1). "throughout Cassalanter Villa", "a useful ally to BD-affiliated party members" and "the source of the intelligence adjustment ... once Cassalanter Villa resolves" are quest time | `campaign/structure/arc-g-cassalanter-villa.md:359` ("\"Vessa\" reports the outcome to Jarlaxle. If the party recovered the Eye, Jarlaxle adjusts his plan for Eye #3 — he knows they are two-thirds of the way to the Vault.") |
| 11 | L29 | "A noblewoman who has been attending Waterdeep's high social events for months, fluent with every face in the room, who knows too much about too many people and never goes near the exits." | Day-one. 34 words (brief limit 21). Draft a shorter Overview | `campaign/quests/faction-events/bregan-daerthe/m02-the-wazoo-affair/ev-01-the-wazoo-affair.md:20` |

Voice profile, the lines with a quest-time or encounter clause (`.claude/skills/character-voices/voices/bregan-daerthe.md`, "### Vessa", lines 222-236):
- Line 235, sample *Business (to a BD member, quietly)*: "The captain says hello. The service stair is unguarded at midnight." — operational clue for the Cassalanter Villa heist. No campaign file states a service stair that is unguarded at midnight. The closest campaign line is the service wing in `campaign/structure/arc-g-cassalanter-villa.md:247` ("attempts to flee through the service wing"). Quest time; route to **Cassalanter Villa** or drop it.
- Line 236, sample *Under pressure*: "Well, this party has taken a turn. I'll be leaving by the front door, like a lady." — encounter cue. Flag.
- Line 230, Quirks: "She pauses a beat before answering to her own name. She knows every guest's name and never needs reminding." — day-one.
- Line 231, Signature phrases: "\"Darling.\" / \"Too perfect, aren't they?\" / \"I'm not going near the chapel.\"" — day-one. The chapel line is the Cassalanter temple, which she will not enter (`:232`).
- Line 232, Never: "She never enters the temple, never breaks cover publicly, and never shows her true face to anyone outside Bregan D'aerthe." — day-one.
- Line 229, Personality in speech: "Patient detachment and satisfaction in her cover. Her curiosity about the party's infiltration shows in precise questions. Around the Cassalanters she talks pure society suspicion and calls them \"too perfect\". In truth she has read their thoughts and knows about the pact, which she reports only to the captain and never says aloud to anyone else." — day-one, except "the party's infiltration" (quest time, row 5).

---

## D. Conflicts

**D1. The name Lymeria Lhaurilstar (campaign against the published adventure).**
- Campaign, the page: "Vessa (full name Lymeria Lhaurilstar) is a Bregan D'aerthe doppelganger operative..." — `campaign/setting/notable-figures/bregan-daerthe/12-vessa.md:25`
- Adventure, the Cassalanter party (Founders' Day): "Four doppelgangers from the Yawning Portal have slipped into the party disguised as nobles. Their leader, {@creature Bonnie|WDH} (see \"Familiar Faces\"), poses as a minor noblewoman going by the name Lymeria Lhaurilstar; she was hoping to have a fun night at the party, but she's willing to help the characters if they need aid." — `sources/adventure-wdh.json:20414` (entry "C15. Banquet Hall", page 122; the heading is at `:20394`)
- Adventure, Bonnie's own entry: "\"Bonnie\"", "{@i N doppelganger disguised as Tethyrian human barmaid}", "This doppelganger posing as a friendly barmaid is the leader of a gang of five doppelgangers that arrived in Waterdeep over a year ago." — `sources/adventure-wdh.json:1511`-`:1516` (page 20)
- Campaign, the Harper Bonnie (not the Vessa figure): "**Bonnie** — barmaid. Knows every face in the room; shares tavern gossip freely. Nothing she says is untrue; she controls what she reveals." — `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:24`
- Campaign, the Harpers guide: "| 4th | **The Doppelganger Auditions** | Harper agent Mattrim Mereg wants to recruit a crew of five doppelgangers. Interview them and report which you would trust. One of them is selling the Harpers out, and only their leader Bonnie is recruited. | +3 |" — `campaign/guides/factions/02-harpers.md:70`
- Session 18 decision: "**Decision:** The Arc G doppelganger BD operative (previously \"Bonnie\") was renamed \"Vessa\" (true identity: Lymeria Lhaurilstar) throughout Arc G and given a new Appendix A profile. The Yawning Portal Bonnie in App A/C/D is a completely different character and was not touched." — `session 18 handoff.md:54`
- Session 18 open item: "- **Vessa's true name:** The Arc G BD operative's true name (Lymeria Lhaurilstar) is preserved in the Appendix A profile. The Arc G file uses \"Vessa\" as the operational alias throughout. Confirm during prose-polish pass that Arc G refers to her as Vessa in all scenes." — `session 18 handoff.md:117`
- Higher rank: the campaign decided the name in session 18 (`session 18 handoff.md:54`), and the page's name is a campaign decision. The published adventure gives the same name to a different character (Bonnie), so the two are in conflict on the name. The drafter should keep the campaign's name and state the collision if the page mentions it, or drop the name.
- Related campaign name: the wiki's Castle Ward residence list has "Lady Naneatha Lhaurilstar" (`campaign/gazetteer/waterdeep/castle-ward.md:253`: "The wiki's Castle Ward residence list names Mirt (a Masked Lord), Leone and Lady Naneatha Lhaurilstar, and no other Masked Lord."). The surname is shared with a Masked Lord household, not with Vessa.

**D2. "Featured in: Sea Maidens Faire" (weakly sourced).**
- Campaign, the page: "- **Featured in:** **Cassalanter Villa**, **Sea Maidens Faire**" — `campaign/setting/notable-figures/bregan-daerthe/12-vessa.md:7`
- Campaign, the only Sea Maidens line naming her: "- **Cassalanter Villa** — Report on Cultists of Asmodeus (J30) provides Three Clue Rule path to **Cassalanter Villa**. \"Vessa\" the BD operative in **Cassalanter Villa** previews Jarlaxle's surveillance operations." — `campaign/structure/arc-h-sea-maidens-faire.md:341` (a cross-reference list; no Sea Maidens event)
- Campaign, the Sea Maidens structure doc line 436 is in the Cassalanter structure doc, not the Sea Maidens one: "- **Sea Maidens Faire** — Stone 2-Eye impressions (ship in harbor, Scarlet Marpenoth, bald elf) point toward **Sea Maidens Faire**. \"Vessa\" the BD operative in this quest is a preview of Jarlaxle's intelligence operations." — `campaign/structure/arc-g-cassalanter-villa.md:436`
- Not settled. The page's "Sea Maidens Faire" entry rests on a cross-reference only. Route or drop.

**D3. "Reports the outcome" (Cassalanter Villa) against the day-one role.** Not a conflict: the Cassalanter Villa structure doc (`arc-g-cassalanter-villa.md:359`) and the Relationships line (`12-vessa.md:25`) agree. The day-one role and the quest-time reporting are different facts. The reporting belongs to the quest.

**D4. Her knowledge of the pact against the voice's "she never says aloud".** Not a conflict. The voice profile (`bregan-daerthe.md:229`) and the Villains rule ("He does not tell Bregan D'aerthe members unless they work it out") are the same rule.

**D5. Which companies she may show her face to.** The Resonance and Persona say she shows her face "to a BD-affiliated party member" (`12-vessa.md:11`, `:21`). The voice says "never shows her true face to anyone outside Bregan D'aerthe" (`bregan-daerthe.md:232`). Consistent if the party member is a BD member. Route the party framing.

---

## E. Stale lines in other files (do not edit) and routed quest references

**E1. Stale or related lines in other files.**
- `campaign/setting/organizations/10-cassalanters.md:84`: "- **Bregan D'aerthe (neutral, informed):** Jarlaxle knows about the pact through Vessa, who sits in the family's social circle under a permanent human cover, and he is the only outsider who does. He has no wish to act unless he sees a strategic gain, and he tells no member of the company unless the member works it out (**The Cassalanters** in Villains; **Jarlaxle Baenre**; **Vessa**)." Consistent with the Vessa page.
- `campaign/setting/organizations/10-cassalanters.md:122`: "> - **The one exception:** Jarlaxle knows about the pact through **Vessa**, his doppelganger spy in the Cassalanter social circle. He never tells Bregan D'aerthe members unless they work it out themselves." Consistent.
- `campaign/setting/villains/cassalanters.md:66`: "- Jarlaxle is the one exception. He knows about the pact through **Vessa**, his doppelganger spy in the Cassalanter social circle, and he tells no Bregan D'aerthe member unless the member works it out." Consistent.
- `campaign/setting/villains/jarlaxle.md:109` (Relationships table): "| The Cassalanters | Aware but uninvested | Knows about their infernal bargain through intelligence; not interested in getting involved unless strategic upside appears |" — the row names no Vessa. Consistent.
- `campaign/setting/history/05-a-debt-in-blood.md:83`: "> - The one exception is Jarlaxle, who learned it through Vessa, his doppelganger spy in the Cassalanter social circle. He does not tell Bregan D'aerthe members unless they work it out themselves." Consistent.
- `campaign/gazetteer/waterdeep/sea-ward.md:38`: "> - Nobody in the ward knows. Every faction suspects the family because it is too nice to be this rich, and none knows about the pact. Savra Belabranta of the Order of the Gauntlet hunts for proof, and Jeryth Phaulkon feels an infernal influence in the Southern Ward that the Emerald Enclave cannot trace to a house. The one exception is Jarlaxle, who knows through **Vessa**, his doppelganger spy in the Cassalanter social circle, and tells Bregan D'aerthe members nothing unless they work it out." Consistent.
- `campaign/gazetteer/waterdeep/sea-ward.md:221`: "- **Vessa**: Jarlaxle's spy in the Cassalanter circle (see Secret)." Consistent.
- `campaign/gazetteer/waterdeep/north-ward.md:42`: "> - Nobody outside the household and the cult knows the family worships Asmodeus, apart from Jarlaxle, whose spy Vessa moves in its social circle. The party reaches the shrine through **Faction Outposts** or the Order of the Gauntlet's **The Shrine on Aveen Street**. It is a separate site from the temple beneath **Cassalanter Villa**." Consistent.
- `campaign/gazetteer/waterdeep/southern-ward.md:37`: "> - Nobody outside the household and the cult knows the family worships Asmodeus. The one exception is Jarlaxle, whose spy **Vessa** moves in the family's social circle and who tells Bregan D'aerthe members nothing unless they work it out. The footmen's rumor in **The Wazoo Affair** names the windmill only as a place where lanterns burn on moonless nights, and the Enclave has felt a wound in the ley lines near Coachlamp Lane without finding a cause." Consistent.
- `campaign/gazetteer/waterdeep/southern-ward.md:228`: "- **Tally Fellbranch**, **Korgstrod Uxgulm**, **Kelso Fiddlewick**, **Tashlyn Yafeera**, **Lady Gondafrey**, **Vessa**: Melannor's brother, the Orb Confectioners duergar, the wererat gang's leader, the Doom Raiders' lieutenant, the prisoner in Kolat Towers and Jarlaxle's spy." The six names and six roles are listed in order, so Vessa is read as "Jarlaxle's spy". Consistent by order; the list is not explicit.
- `campaign/setting/deities/asmodeus.md:64`: "> - **Never reveal:** That the Cassalanters worship him, the pact and the soul contract, the ninety-nine poisoned guests, Osvaldo's fate, or that Jarlaxle knows through Vessa. A player who asks about Asmodeus gets the Overview, and the party's own evidence is the only thing that adds to it." Consistent.
- `campaign/setting/history/05-a-debt-in-blood.md:116`: "- **Jarlaxle Baenre** (Villains) and **Vessa**: the one outsider who knows." Consistent.
- `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:104`: "- **The pact:** Nobody outside the household and the cult knows what the Cassalanters have done, and everyone else only suspects the family. Jarlaxle is the one exception, through **Vessa**, and he tells no member of Bregan D'aerthe who has not worked it out." Consistent.
- `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:106` through `14-caladorn-cassalanter.md:88`: each Cassalanter page repeats the rule and names Vessa. Consistent.
- `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:133`: "- **Soluun Xibrindas**, **Fel'rekt Lafeen**, **Krebbyg Masq'il'yr**, **Nar'l Xibrindas**, **Vessa**, **Ryvarra**, **Quilm**, **Margo Verida** and **Khafeyta Murzan** (Notable Figures): his lieutenants, spies and companions" — the list calls Vessa a "spy" in the cross-reference. Consistent.

**E2. Routed quest references (the quest-time facts on the page).**

Cassalanter Villa (the quest that puts Vessa on the page):
- `campaign/structure/arc-g-cassalanter-villa.md:359`: "**Bregan D'aerthe.** \"Vessa\" reports the outcome to Jarlaxle. If the party recovered the Eye, Jarlaxle adjusts his plan for Eye #3 — he knows they are two-thirds of the way to the Vault." (the reporting beat; Relationships row 10 and Motivations row 6)
- `campaign/structure/arc-g-cassalanter-villa.md:436`: see D2.

Faction events (the day-one page must not restate the quest mechanics):
- `campaign/quests/faction-events/bregan-daerthe/m02-the-wazoo-affair/ev-01-the-wazoo-affair.md:20`: "> - Jarlaxle knows the Cassalanters are bound to Asmodeus and have pledged their children in a contract. His doppelganger agent Vessa, who has moved in Cassalanter society for months, read it in their thoughts. No other faction or NPC in this Event knows." (day-one fact stated in a quest event; use the day-one part)
- `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/overview.md:30`: "Jarlaxle wants the plan because he knows what the Cassalanters are. His doppelganger agent Vessa has moved in their social circle for months and read the Asmodean pact and the children's contract in their thoughts, and the Wazoo piece was meant to make the family flinch. Vessa's cover has never reached the windmill, so the plan is the company's first look at it. Zardoz and Krebbyg never confirm any of this to a member. The exception is a member who works out the truth and says so." (quest event)
- `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-02-the-debrief.md:28`: "> Zardoz Zord is Jarlaxle, and Jarlaxle knows that the Cassalanters are bound to Asmodeus and have pledged their children in a contract. His doppelganger agent Vessa has moved in their social circle for months and reads thoughts, which is how he learned it. Krebbyg and Fel'rekt may or may not know. The company wants the member's account because Vessa's cover has never reached the windmill. No speaker tells a member the truth unless the member has worked it out. See **Figuring It Out**." (quest event)
- `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:444`: "In **Cassalanter Villa** (unconverted), Vessa then helps that member openly with a cover story and a distraction at the banquet, and the member can speak with her about the family's plans." (quest event; the outcome **Cassalanter Pact Shared with BD** is the gate)
- `campaign/quests/faction-events/bregan-daerthe/r25-commander/ev-01-commander.md:45`: "Jarlaxle knows the Cassalanters are bound to Asmodeus and have pledged their children in a contract, because his doppelganger agent Vessa, who has moved in their social circle for months, reads thoughts." (quest event)
- `campaign/quests/faction-events/bregan-daerthe/r10-officer/ev-01-officer.md:283`: "> - **What it never says:** the company knows the truth about the Cassalanters through Vessa. An assessment never states the Asmodean pact or the children's contract to a member who hasn't worked it out. For that member, a page on the Cassalanters covers the house, staff, holdings and social calendar, and leaves the pact out." (quest event)
- `campaign/quests/faction-events/bregan-daerthe/r50-houseless-noble/ev-01-houseless-noble.md:27`: "> Bregan D'aerthe rejects Lolth. The spider on the coin is the goddess the company walked away from, caught in her own web with a blade through her, and every speaker mentions her with contempt. The company knows the truth about the Cassalanters, because Jarlaxle's doppelganger agent Vessa reads their thoughts. No speaker tells a member who hasn't worked it out." (quest event)
- `campaign/quests/faction-events/bregan-daerthe/s03-dinner-with-zardoz/ev-01-dinner-with-zardoz.md:34`: "> Jarlaxle knows that the Cassalanters are bound to Asmodeus and have pledged their children in a contract, because his doppelganger agent Vessa, who has moved in their social circle for months, reads thoughts. No speaker at this table tells a member who has not worked it out." (quest event)

Sea Maidens Faire (cross-reference only): `campaign/structure/arc-h-sea-maidens-faire.md:341`, quoted in D2.

Factions Guide: no Vessa line (searched `campaign/guides/`).

---

## F. Gaps a Background needs that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

**F1. Origin, birth, age, home, family.** No source gives any of these. The only age hint is "a very old, very contained disinterest in her own face" (`campaign/setting/notable-figures/bregan-daerthe/12-vessa.md:13`). The Persona gives "for months" in the social circle (`:21`) and "has been doing this long enough" (`:21`). Do not name a new Notable Figure. A nameless relative or place is allowed.

**F2. How she came to Jarlaxle and to the company.** No source. The company's recruiting rule is in the org page: "Watch Before You Approach: The company recruits with care. Its spies shadow a candidate for several days before anyone makes contact." (`campaign/setting/organizations/07-bregan-daerthe.md:40`). Constraint: the company's rule that "Almost all members are male" (`:41`) does not apply to a doppelganger (no sourced member count applies to non-drow operatives: "In this campaign Jarlaxle collects capable people whatever their species." `:41`).

**F3. How she came to a human cover.** No source. The cover is "a permanent human cover" (`campaign/setting/villains/jarlaxle.md:59`). Constraint: she must keep the cover in the Cassalanter circle, per the Motivations line (`12-vessa.md:15`).

**F4. Her doppelganger true form and her "true face".** The Persona says she has "to think before remembering what her own face looks like" (`:21`). No source gives the true form. Do not describe it as a fixed face; the voice gives "a flash of gray features" (`:21`).

**F5. Relationship with the Cassalanters.** None beyond the rule that she sits in their social circle and reads their thoughts. The campaign gives no personal contact with Victoro, Ammalia or the children.

**F6. Losses, grudges, a fear, a place she cares about.** None in any source.

**F7. Personal goals beyond the company.** None in any source. The page's Motivations (`:15`) give wants toward Jarlaxle and the cover. Brief ruling 17 allows a `[design]` goal about a place, a craft or a person, provided it does not reveal the pact to a member, does not contradict "She does not want to enter the temple" (`:15`), and does not change the Cassalanter Villa outcome.

**F8. The name.** "Lymeria Lhaurilstar" is the campaign's name (D1). The Background must use it consistently with the page, or use "Vessa" alone.

---

## G. Source facts that hint at the figure's inner life (for the backstory; do not contradict)

- "a very old, very contained disinterest in her own face." — `campaign/setting/notable-figures/bregan-daerthe/12-vessa.md:13`
- "Deep down, she has been doing this long enough that she has to think before remembering what her own face looks like, and has decided this is probably fine." — `12-vessa.md:21`
- "Patient detachment and satisfaction in her cover." (voice) — `.claude/skills/character-voices/voices/bregan-daerthe.md:229`
- "She pauses a beat before answering to her own name." (voice) — `bregan-daerthe.md:230`
- "Her own name is used a little too carefully." (voice) — `bregan-daerthe.md:227`
- "She knows every guest's name and never needs reminding." (voice) — `bregan-daerthe.md:230`
- "Vessa does not fight in the villa under any circumstances — her cover is the asset and she will not burn it." — `12-vessa.md:23`
- "She will not enter the temple below the villa under any circumstances." — `12-vessa.md:23`
- "\"I'm not going near the chapel.\"" (voice signature) — `bregan-daerthe.md:231`
- "Around the Cassalanters she talks pure society suspicion and calls them \"too perfect\"." — `bregan-daerthe.md:229`
- "She does not want to enter the temple." — `12-vessa.md:15`
- "She is how Jarlaxle alone outside the household and the cult knows about the family's pact" — `campaign/setting/villains/jarlaxle.md:59` (her one fact that the drafter must not reveal to a member; see the Cassalanter secrecy rule)

---

## Not found

- Origin, birth, age, home, family, former life, faith, how she came to Jarlaxle, when she joined, her true form, a loss, a grudge, a fear, a personal goal beyond the cover. Searched: `campaign/` (Grep for "Vessa|Lymeria|Lhaurilstar|doppelganger"), `sources/adventure-wdh.json` (Grep for "Vessa|Lymeria|doppelganger": the only hits are the Bonnie passages at `:1515`, `:3745`, `:6672`, `:7694`-`:7702`, `:10572`-`:10603`, `:13674`, `:14781`, `:18481`, `:20414`, none about Vessa), `sources/*.md` (Grep for "Vessa|doppelganger|spy|Lymeria": no Vessa line), `sources/SOURCE_GUIDE.md` (Cassalanter entries name Willifort Crowelle only, lines `:31`, `:322`).
- Vessa in the Factions Guide: none (`campaign/guides/factions/`).
- Vessa in the Cassalanter Villa location journal: none (`campaign/locations/cassalanter-villa/`, searched for "Vessa").
- The "service stair is unguarded at midnight" clue (voice line 235): no campaign match for "service stair" or "unguarded at midnight". The campaign's service references are the garden service gate (`campaign/locations/cassalanter-villa/09-butterfly-garden.md:21`) and the service wing (`campaign/structure/arc-g-cassalanter-villa.md:247`).
- Alexandrian PDFs: not searched for Vessa (not greppable). `sources/10. Lair  Cassalanter Villa.pdf` and `sources/1. The Villains.pdf` are the likeliest to name a BD spy and remain unchecked. `sources/SOURCE_GUIDE.md:315`-`:329` describes the Cassalanter PDF's adversary rosters: "household staff, hired guards, Willifort Crowelle (doppelganger butler), chain devil, and the Cassalanters themselves" (`:322`). That list has no BD operative.
- Wiki: NOT FOUND stub for Vessa (scratchpad `wiki-bregan-daerthe/12-vessa.txt`, line 1).

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. `sources/SOURCE_GUIDE.md:687` lists `Cassalanters, their tragic backtstory, and Endgame setup.docx`; `sources/SOURCE_GUIDE.md:690` lists `Jarlaxle Baenre NPC Guide.docx`. Neither was checked for Vessa. Route to the caller for extraction.
- PDFs: text cannot be extracted without `pdftotext`. The Cassalanter and Villains PDFs were not checked for Vessa.
