# Pass 6 research notes: Vincent Trench

Page: `campaign/setting/notable-figures/trollskull-community/05-vincent-trench.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 19; user rulings Session 53)
Method: Grep and Read only. Quotes are copied from tool output. Line numbers are file lines unless marked "dump line" (wiki XML) or "extract line" (scratchpad wiki extract). JSON escapes are shown as plain quotes. `{@creature ...}` and `{@spell ...}` tags are left as written.
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/trollskull-community/01-talisolvanar-fellbranch.md`
Organization page: none. The trollskull-community group has no `campaign/setting/organizations/` page. There is no Watchful Order or Vintners' Guild organization page either (see D4 and D5).
Factions Guide: none for Vincent. Villains page: none.
Voice profile: `.claude/skills/character-voices/voices/trollskull-community.md` lines 79 to 93 ("### Vincent Trench").
Wiki: the extract `scratchpad/wiki-trollskull-community/05-vincent-trench.txt` is the stub `NOT FOUND`. The full Forgotten Realms Wiki dump (`/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/fandom-dump/forgottenrealms_pages_current.xml`) has no page titled "Vincent Trench". It has the page **"Valantajar"** (XML lines 4008754 to 4008844), whose infobox gives `aliases = Vincent Trench`. That page is quoted below as the wiki source for Vincent. Its edition is tagged by its cite, `WDH5e-p32-33` (Waterdeep: Dragon Heist, 5e).
PDF: `sources/27. Addendum A Night in Trollskull Manor.pdf` was read with the Read tool's `pages` parameter. PDF page 9 is printed p.186 and PDF page 10 is printed p.187. The **VINCENT TRENCH** bullets are on PDF page 9 (printed p.186). These PDF quotes are transcriptions from the image. Each one must be checked with `pdftotext -layout` before it goes into prose. No shell was available.

## Findings that change how the page is written

1. **The day-one identity is sourced.** The adventure says Vincent is "in fact a rakshasa named Valantajar" (`sources/adventure-wdh.json:3493`). The wiki dates the alias: "By the {{YearlinkName|1492}}... Valantajar went by the name Vincent Trench and managed the Tiger's Eye" (dump line 4008833). Both support a day-one page.
2. **The pronoun has a source conflict to keep in view.** The page says he/him (page line 5). The adventure uses "he" for the disguise and "it" for the rakshasa beneath it (`sources/adventure-wdh.json:3493`, see D1). The page keeps he/him because the page and the gazetteer say so.
3. **The quest-time facts are the Fireball! scene and the alley introduction.** Vincent's Fireball! witness account is at `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:147` to `:153`. His alley visit is at `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:25`. The page's Relationships line (page line 25) says "for the Trollskull party", a phrase that presumes the party owns the tavern (see C2).
4. **The patron topics are tavern-time.** Vincent's client, the Adric Thongolir job, and the Thundercross Alley theft are in Appendix D (`sources/Appendix_D_-_Running_the_Tavern.md:1293` to `:1297`) and the PDF (printed p.186). None is dated before the tavern opens. Only the PDF has "half-steel dragon" (see D6).

---

## A. Background facts by theme

### A1. Identity, origin and the alias

**Adventure, T5 Tiger's Eye (page 32)**
> "This private detective's business is unremarkable on the outside, its only distinguishing mark an orange-and-black sign featuring a cat's eyes. Inside is a regal apartment dimly lit by flickering oil lamps. The door is locked, and visitors must knock or ring the bell before being let in."
> — `sources/adventure-wdh.json:3492`

> "They are met by {@creature Vincent Trench|WDH}, a human detective and the owner of the Tiger's Eye. He speaks concisely, dresses in a sharp suit, and smokes a slim pipe. Vincent is in fact a {@creature rakshasa} named Valantajar that always casts {@spell disguise self} on itself before seeing visitors. The rakshasa has lived in Waterdeep for years, switching identities as often as needed to keep its true nature hidden. It has grown accustomed to living among mortals and, much to its own astonishment, is rather fond of Waterdeep and its citizens."
> — `sources/adventure-wdh.json:3493`

**Wiki, "Valantajar" page (infobox, dump lines 4008769 to 4008828)**
> "| aliases        = Vincent Trench" (dump line 4008775)
> "| race           = [[Rakshasa]] disguised as [[human]]" (dump line 4008781)
> "| occupation     = Private detective" (dump line 4008783)
> "| alignment5e    = [[Lawful evil]]" (dump line 4008825)
> "| challenge5e    = 13" (dump line 4008826)

**Wiki, lead (dump line 4008830; `WDH5e-p32-33`)**
> "'''Valantajar''' was a [[rakshasa]] who worked as a private investigator in [[Waterdeep]] in the late 15{{th}} century [[DR]].&lt;ref name="WDH5e-p32-33" /&gt;"
> — dump line 4008830 (entities decoded)

**Wiki, Activities (dump line 4008833; `WDH5e-p32-33`)**
> "By the {{YearlinkName|1492}},{{Waterdeep-time}} Valantajar went by the name '''Vincent Trench''' and managed the [[Tiger's Eye]], a detective business on [[Trollskull Alley]] in the [[Waterdeep/North Ward|North Ward]]. He could discover any secret in the city in exchange for [[gold]] or a service to him."
> — dump line 4008833

**Wiki, Personality (dump line 4008836; `WDH5e-p32-33`)**
> "Valantajar had lived for many years in Waterdeep, changing identities as necessary. He had grown accustomed to living among mortals and&mdash;to his own astonishment&mdash;was rather fond of the city and its inhabitants."
> — dump line 4008836 (entities decoded)

**Appendix D, Vincent Trench (1275 to 1276)**
> "### Vincent Trench"
> "*Tiger's Eye — LE rakshasa disguised as a Calishite human, Rakshasa stat block*"
> — `sources/Appendix_D_-_Running_the_Tavern.md:1275` and `:1276`

**North Ward gazetteer, Vincent (day-one GM note; the gazetteer is Campaign rank)**
> "- Vincent is Valantajar, a rakshasa who has lived in Waterdeep for years under a string of identities and has grown fond of the city. His interest in the party serves himself and is not hostile at first."
> — `campaign/gazetteer/waterdeep/north-ward.md:152`

### A2. The shop, its trade and its place

**Adventure, Tiger's Eye services (page 32)**
> "Trench can discover any secret in Waterdeep, for a fee. Use your judgment when pricing its services; 50 gp is sufficient for most investigations, but if the characters want to learn secrets relating to the major antagonists of this adventure, the rakshasa might require a service in payment, such as slaying enemies that are hunting it, posting advertisements for its business in their tavern, or keeping tabs on someone Vincent has been hired to spy on."
> — `sources/adventure-wdh.json:3500`

**Adventure, Trollskull Alley intro (the keyed map)**
> "Trollskull Alley is filled with people who can shape the characters' day-to-day lives in Waterdeep. The characters will likely return to Trollskull Alley many times during the adventure and get to know their neighbors as time passes."
> — `sources/adventure-wdh.json:3008`
> "The locations described below are keyed to the map of Trollskull Alley. Buildings not specifically identified on the map are row-houses that serve as private residences for upper-middle class Waterdavians who can afford housekeepers, groundskeepers, and nannies."
> — `sources/adventure-wdh.json:3009`

**North Ward gazetteer, Trollskull Alley entry**
> "- The Tiger's Eye is a detective agency run by **Vincent Trench**, Book Wyrm's Treasure is a bookshop run by **Rishaal the Page-Turner**, and a few doors down is Frewn's Brews, a rival pub owned by **Emmek Frewn**."
> — `campaign/gazetteer/waterdeep/north-ward.md:58`

**Gazetteer, Vincent entry (Characters of Interest, Life in the Ward)**
> "**Vincent Trench (Lawful Evil, Rakshasa disguised as a Human, he/him)**"
> "- A sharp-dressed, pipe-smoking private detective who runs the Tiger's Eye across the alley. He speaks concisely, charges fairly and calls on new neighbors with a rate card."
> — `campaign/gazetteer/waterdeep/north-ward.md:146` and `:147`

**Gazetteer, Read Aloud anchor**
> "- Trollskull Alley: sawdust at the door of the Bent Nail, hammer sounds and chimney smoke at Steam and Steel, a greenhouse with glass walls full of blossoms, and the orange-and-black sign of the Tiger's Eye."
> — `campaign/gazetteer/waterdeep/north-ward.md:212`

**Wiki, North Ward "Shops & Businesses" list (`sources/research/pass3-bundles/north-ward/wiki.txt:169`, cites WDH5e-p32)**
> "* [[Tiger's Eye]]<ref name="WDH5e-p32" />"
> — `sources/research/pass3-bundles/north-ward/wiki.txt:169`

**Trollskull Manor guide, Operating State (the tavern is not yet open on Ches 1; see C2)**
> "- The tavern has been closed for years, and the poltergeist **Lif** haunts it. He is the spirit of the last barkeeper, a dwarf, and has minded the building alone since 1479 DR."
> — `campaign/gazetteer/waterdeep/north-ward.md:63`

### A3. Temperament, habits and manner

**Appendix D, Roleplaying Keys and Appearance (1278, 1280)**
> "**Appearance:** Always impeccably dressed. His hands are backwards. Most people don't notice this. Players who look carefully may."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1278`
> "**Roleplaying Keys:** Asks questions more than he offers information. Very good at seeming interested in whoever he is speaking to. Never drinks the ale — always spirits, always neat."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1280`

**Appendix D, Slow Burn note (1287 to 1289; the note is a GM aside on 2024 Truesight)**
> "<p>As a rakshasa, Vincent is immune to spells of 6th level or lower and resists Bludgeoning, Piercing, and Slashing damage from nonmagical attacks. He will not be caught in a tavern fight. He will, however, remember everything that happens in his vicinity.</p>"
> — `sources/Appendix_D_-_Running_the_Tavern.md:1289`

**Trollskull Manor guide, City Figures (`08-notable-patrons.md:38` to `:41`)**
> "**Vincent Trench** *(Tiger's Eye, LE rakshasa in Calishite human disguise, Rakshasa stat block)*"
> "Asks questions; seems interested in whoever he's speaking to; always spirits, always neat; his hands are backwards."
> "**2024 note:** Truesight no longer auto-reveals shapeshifters — Vincent's rakshasa nature requires *True Seeing* or specific magical investigation, not casual divine scrutiny. Play him as the best-connected, most unsettling man in the North Ward until Act II when the reveal matters most."
> — `campaign/guides/trollskull-manor/08-notable-patrons.md:38`, `:39`, `:41`

**Voice profile (`.claude/skills/character-voices/voices/trollskull-community.md`)**
> "*A sharp-dressed, pipe-smoking detective whose attention is flattering and whose manner is very slightly wrong.*" (line 80)
> "- **Personality in speech:** Predatory amusement and real curiosity. He's genuinely interested in whoever he's talking to, and it's flattering and unnerving. The subtle wrongness is in what he notices (things he shouldn't know yet) and in odd phrasing about time and people ("in my experience of your kind of trouble"). His fondness for the city surfaces unexpectedly." (line 86)
> "- **Quirks:** He tamps his pipe before a hard question. He compliments one precise detail about the listener. Very occasionally he refers to Waterdeep with the distance of someone much older than he looks." (line 87)
> "- **Never:** He never loses composure in public, never reveals his nature, and never takes a case that would draw powerful attention." (line 89)

### A4. Neighbors and the alley

**Gazetteer, Trollskull Alley entry (the alley's frame)**
> "**Trollskull Alley** — Street of shops and the party's neighbors"
> — `campaign/gazetteer/waterdeep/north-ward.md:56`

**Wiki, Trollskull Alley (ward; dump lines 5103805 and 5103808, refs WDH5e-ch2, WDH5e-map, VGW2e-p103)**
> "'''Trollskull Alley''' was an alley located in the [[Waterdeep/North Ward|North Ward]] of [[Waterdeep]]."
> — dump line 5103805 (the wiki's Trollskull Alley page is not quoted further here; it is the same as the Rishaal and Hammond notes)

### A5. Time in post

- Wiki, dump line 4008833 (quoted in A1): the Tiger's Eye name and management are dated "By the 1492 DR". The wiki gives no start year for Valantajar in Waterdeep. The wiki's lead says only "in the late 15th century DR" (dump line 4008830).
- No source gives the year Valantajar took the name Vincent Trench before 1492 DR, his arrival in Waterdeep, or the age of the rakshasa. See F.

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Summary (page line 5): "> - *Rakshasa (disguised as human detective), lawful evil, he/him*. Stat block: **Rakshasa (as Valantajar)**." — `campaign/setting/notable-figures/trollskull-community/05-vincent-trench.md:5`
- Gazetteer (`north-ward.md:146`): "**Vincent Trench (Lawful Evil, Rakshasa disguised as a Human, he/him)**"
- Appendix D (`1276`): "*Tiger's Eye — LE rakshasa disguised as a Calishite human, Rakshasa stat block*"
- Guide (`08-notable-patrons.md:38`): "LE rakshasa in Calishite human disguise, Rakshasa stat block"
- Wiki (dump line 4008825): "| alignment5e    = [[Lawful evil]]"
- Adventure: no alignment line for Vincent in T5 (`sources/adventure-wdh.json:3493`).
- All sources agree: lawful evil.

**Species**
- Summary: "*Rakshasa (disguised as human detective)*" (page line 5).
- Adventure: "Vincent is in fact a {@creature rakshasa} named Valantajar" (`sources/adventure-wdh.json:3493`); "a human detective" (same line).
- Appendix D: "disguised as a Calishite human" (`:1276`). Guide: "Calishite human disguise" (`08-notable-patrons.md:38`).
- Wiki: "| race           = [[Rakshasa]] disguised as [[human]]" (dump line 4008781).
- Conflict on the disguise ethnicity: see D2 and D3.

**Pronouns**
- Summary (page line 5): "he/him". Gazetteer (`north-ward.md:146`): "he/him".
- Adventure: "He speaks concisely, dresses in a sharp suit, and smokes a slim pipe." (`sources/adventure-wdh.json:3493`). The same line uses "it" for the rakshasa: "always casts {@spell disguise self} on itself" and "to keep its true nature hidden" (same line).
- Appendix D: "His hands are backwards." (`:1278`). No pronoun conflict.
- Wiki: "| sex            = Male" (dump line 4008780).
- Conflict: see D1.

**Stat block**
- Summary (page line 5): "Stat block: **Rakshasa (as Valantajar)**."
- Adventure: "Vincent is in fact a {@creature rakshasa} named Valantajar" (`sources/adventure-wdh.json:3493`).
- Appendix D: "Rakshasa stat block" (`:1276`). Wiki: "| challenge5e    = 13" (dump line 4008826) and "MM5e-p257" in refs (dump line 4008828).

---

## C. Sentences on the current page (and the voice profile) that narrate a quest-time event or a day-one conflict

Current page: `campaign/setting/notable-figures/trollskull-community/05-vincent-trench.md`. Sections: Gamemaster's Summary, Roleplaying Information, Character Information, Overview. No Background yet.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| C1 | 7 | "> - **Featured in:** **Trollskull Alley**, **Fireball!**" | Quest list. Route (brief ruling 1) | Trollskull Alley: `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:25`. Fireball!: `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:147` to `:153`; `campaign/quests/act-ii/fireball/overview.md:31` |
| C2 | 25 | "**Relationships.** Vincent is a neighbor and occasional information broker for the Trollskull party, an object of growing suspicion for Rishaal (who has noticed his unusual book purchases), and a creature whose true identity is known to no one in the alley." | Mixed. "for the Trollskull party" presumes the party owns the tavern, which the adventure gives after Volo's quest: "Following the completion of Volo's quest, the characters gain a home base with an address in Trollskull Alley, in Waterdeep's North Ward." (`sources/adventure-wdh.json:1595`). "growing suspicion ... (who has noticed his unusual book purchases)" is tavern-time (see C3). "a creature whose true identity is known to no one in the alley" has no source (F) | Party as owners: `sources/adventure-wdh.json:1595`; Trollskull Alley intro, `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:25` ("His interest in the party is self-serving but not immediately hostile.") |
| C3 | 25 | "(who has noticed his unusual book purchases)" | Tavern-time. Appendix D and the guide date Rishaal's noticing to a tavern-night topic, not to Ches 1 | `sources/Appendix_D_-_Running_the_Tavern.md:1350` ("4. Mentions, as if it were unremarkable, that Vincent Trench has been in the shop twice this tenday. Both times he bought books on planar binding. Rishaal is not worried. He is, however, mentioning it."); `campaign/guides/trollskull-manor/08-notable-patrons.md:127`; `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:27` ("Increasingly suspicious of Vincent Trench and will share that suspicion if the party shows interest.") |
| C4 | 15 (Motivations) | "**Motivations.** Vincent wants to maintain his comfortable life in Waterdeep indefinitely, learn every secret worth knowing in the city, and avoid drawing the attention of anyone powerful enough to see through his disguise." | No quest event. Day-one. Keep (ruling 3). Not a source fact for "comfortable life" (design; see G) | none needed |
| C5 | 21 (Persona) | "**Persona.** To the world, Vincent Trench is a sharp-dressed, pipe-smoking private detective who speaks concisely and charges fairly. To those he trusts, he is Valantajar, a rakshasa who has lived in Waterdeep for years, cycling through identities. Deep down, he has grown genuinely fond of the city and its people, and this horrifies some part of him that remembers what he is." | Day-one. Sourced in `sources/adventure-wdh.json:3493` and dump line 4008836. "horrifies some part of him" is design | `sources/adventure-wdh.json:3493` |
| C6 | 23 (Morale) | "**Morale.** In a fight, Vincent would use his innate magic to deflect or escape rather than reveal his true nature. If cornered and unmasked, he fights with a rakshasa's full cunning and cruelty. He will flee Waterdeep before he will die in it." | Day-one. "He will flee Waterdeep before he will die in it" has no source (F) | Partial: `sources/Appendix_D_-_Running_the_Tavern.md:1289` ("He will not be caught in a tavern fight.") |
| C7 | 29 (Overview) | "Vincent Trench is the private detective across the alley — pipe-smoking, precise, willing to find almost anything for the right price, and subtly wrong in ways his customers cannot quite name." | Day-one. Fine | `sources/adventure-wdh.json:3500` ("Trench can discover any secret in Waterdeep, for a fee.") |
| C8 | Voice 91 (Greeting) | "*Greeting:* \"You're the tavern people. Sit down. You've a nice way of standing in a doorway, like you expect it to bite.\"" | **Quest-time clause.** "the tavern people" presumes the party owns the tavern. Drafter restates as a day-one line (ruling 16) | `sources/adventure-wdh.json:1595` |
| C9 | Voice 92 (Business) | "*Business:* \"Five gold a day and expenses. I'll have a name within the tenday. Interesting.\"" | Not quest-time. A rate conflict with the adventure's price (see D5) | `sources/adventure-wdh.json:3500` ("50 gp is sufficient for most investigations") |
| C10 | Voice 93 (Under pressure) | "*Under pressure:* \"Now, let's not be hasty. Nobody here wants to see what I look like when I'm hasty.\"" | Not quest-time. Keep | none needed |

### C2. Where Vincent's quest-time events already live (routed; do not restate on the day-one page)

- **Trollskull Alley, ev-01 (Tiger's Eye sign and the locked door)**: "**Tiger's Eye** (Vincent Trench) — locked. Orange-and-black sign promising investigations handled discreetly." — `campaign/quests/act-i/trollskull-alley/ev-01-welcome-to-trollskull-alley.md:27`
- **Trollskull Alley, ev-03 (The Alley Tour)**: "**Vincent Trench (Tiger's Eye).** Knocks formally, presents his rate card, and offers his services for investigations. "Most new businesses in the North Ward find they have enemies they didn't know about. I'm useful for that." He is a rakshasa named Valantajar who has lived in Waterdeep long enough to genuinely like it. His interest in the party is self-serving but not immediately hostile. Cross-ref the **Vincent Trench** page in Notable Figures." — `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:25`
- **Trollskull Alley, ev-06 (The Grand Opening)**: "**Neighbors** — Tally, Embric and Avi, Fala, Rishaal (all four attend). Vincent Trench sends regrets via a note and a gift of expensive pipe tobacco. Ulkoria arrives late, drinks one ale, says "Acceptable," and leaves." — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:40`
- **Trollskull Alley overview, Involved Characters**: "- **Vincent Trench / Valantajar** (independent) — rakshasa detective at the Tiger's Eye; self-serving interest in the party" — `campaign/quests/act-i/trollskull-alley/overview.md:34` (the "(independent)" label is a quest summary; it does not govern, see D4)
- **Fireball!, ev-01 (Vincent Trench / "The Rake")**: "The Tiger's Eye detective agency, across from the cooperage. Arrived after the explosion. DC 15 Insight: he knows more than he's saying — his affect is too calm, his eyes slightly too still." — `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:149`; and "DC 16 Persuasion: confirms he saw the construct from his window — "a construct of Lantanese manufacture, moving with purpose, heading for the harbor." He is a rakshasa. What he shares is accurate. What he withholds is that he recognized the nimblewright immediately and already knows who builds them and for whom." — `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:151`
- **Fireball!, ev-01 (Jezrynne Hornraven, who had just left the Tiger's Eye)**: "Noblewoman. Had just left the Tiger's Eye detective office when the blast hit." — `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:129`
- **Fireball!, overview**: "- **Vincent Trench / "The Rake"** (Tiger's Eye) — private investigator; is a rakshasa; shares limited accurate intelligence; withholds that he recognized the construct immediately" — `campaign/quests/act-ii/fireball/overview.md:31`
- **Adventure, Jezrynne (the Fireball witness, quest time)**: "A Waterdavian born of wealth and privilege, Jezrynne was leaving the Tiger's Eye (see chapter 2, {@area T5|0a1}), having just hired {@creature Vincent Trench|WDH} to spy on her philandering husband, when she witnessed the following:" — `sources/adventure-wdh.json:4489`
- **Act III Arc D, Jezrynne**: "A Waterdavian noblewoman born of wealth and little patience, Jezrynne had just departed the Tiger's Eye — Vincent Trench's detective office — when the blast hit." — `sources/Act_III_Arc_D.md:171`
- **Trollskull Manor guide, Tavern time (Mirtul 1 to 10 row)**: "| Mirtul 1–10 | Rishaal the Page-Turner, Ulkoria Stonemarrow, Vincent Trench | 9: Kyser Tameno's first visit | Arcane gossip night. An archmage of the Watchful Order drinks two tables from a rakshasa in disguise, and a wizard walks out of the wall. |" — `campaign/guides/trollskull-manor/06-tavern-time.md:31`
- **Trollskull Manor guide, Patron table**: "| 4 | Vincent Trench *(Tiger's Eye)* |" — `campaign/guides/trollskull-manor/06-tavern-time.md:61`
- **Appendix D, Patron table**: "| 4 | Vincent Trench *(Tiger's Eye)* |" — `sources/Appendix_D_-_Running_the_Tavern.md:1109`
- **Appendix D, Topics & Agendas (patron topics, tavern-time)**:
  > "1. Meeting a client at a back table — a nervous merchant from the Dock Ward who keeps looking at the door. The nature of the case is not offered, but the client is clearly frightened." (`sources/Appendix_D_-_Running_the_Tavern.md:1294`)
  > "2. Wants to hire the characters to follow a young noble: Adric Thongolir, youngest son of Lady Adiira Thongolir, believed to be meeting with someone he shouldn't." (`:1295`)
  > "3. Has been hired to investigate petty thefts in Thundercross Alley. A valuable grey jade statuette of a stone giant has been taken from a collector named Irbyth Authamaun. The culprit is a small, floating magical skull that has developed a fondness for stone likenesses. (This is a miniature campaign sandbox hook requiring no further preparation.)" (`:1296`)
  > "4. Tells the characters, apparently idly, that he has recently taken on a very large client — someone interested in several simultaneous investigations. He does not say who. He watches their reaction." (`:1297`)
- **Trollskull Manor guide, Notable Patrons (City Figures, `08-notable-patrons.md:43` to `:46`)**: "- Client meeting in back — nervous Dock Ward merchant who keeps looking at the door" / "- Wants to hire the party to follow young noble Adric Thongolir (meeting someone he shouldn't)" / "- Investigating petty theft in Thundercross Alley: a grey jade stone giant statuette, taken by a small floating magical skull fond of stone likenesses (self-contained sandbox hook)" / "- Mentions he's taken on a notable new client — someone with enough coin to commission several simultaneous investigations. Watches the party's reaction."
- **PDF, VINCENT TRENCH (printed p.186; PDF page 9; transcription, check with pdftotext)**: "Meeting a client. (Either a simple member of the public, or possibly one of the other notable patrons in the tavern.)" / "Looking to hire the PCs to contribute to one of his investigations: He needs a foppish young noble (Adric Thongolir, a half-steel dragon and youngest son of Lady Adiira Thongolir) followed." / "Vincent has been hired to investigate a series of petty thefts in Thundercross Alley (running perpendicular to Thunderstaff Way just north of Sashtar Street)." — `sources/27. Addendum A Night in Trollskull Manor.pdf`, PDF page 9
- **Trollskull Alley, flowchart and Grand Opening**: see `ev-06` above.
- **Structure docs (superseded or pending; do not use for content)**: `campaign/structure/arc-b-trollskull-alley.md:98` ("- **Vincent Trench (Tiger's Eye):** Knocks formally, presents his rate card, and offers his services for investigations.") and `:215`; `campaign/structure/arc-c-fireball.md:80` ("- **Vincent Trench.** The Tiger's Eye detective agency, across the alley. Arrived after the explosion.").

---

## D. Conflicts

**D1. Pronoun (he, or it for the rakshasa)**
- Page (line 5): "he/him". Gazetteer (`north-ward.md:146`): "he/him".
- Adventure, the disguise: "He speaks concisely, dresses in a sharp suit, and smokes a slim pipe." (`sources/adventure-wdh.json:3493`)
- Adventure, the rakshasa: "Vincent is in fact a {@creature rakshasa} named Valantajar that always casts {@spell disguise self} on itself before seeing visitors. The rakshasa has lived in Waterdeep for years, switching identities as often as needed to keep its true nature hidden." (`sources/adventure-wdh.json:3493`)
- Higher ranked: the campaign (page and gazetteer) says he/him for both names. The adventure uses "he" for the persona and "it" for the true rakshasa. The page's Persona line 21 ("To those he trusts, he is Valantajar") keeps he. The drafter keeps he/him for the whole figure, per ruling 4 (existing page). Flag for the user; the adventure's "it" is not a campaign ruling.

**D2. Disguise ethnicity ("human" or "Calishite")**
- Page (line 5): "Rakshasa (disguised as human detective)" (no ethnicity).
- Adventure: "a human detective" (`sources/adventure-wdh.json:3493`).
- Appendix D: "disguised as a Calishite human" (`sources/Appendix_D_-_Running_the_Tavern.md:1276`).
- Guide: "in Calishite human disguise" (`08-notable-patrons.md:38`).
- Higher ranked: the adventure, for "human". Appendix D and the guide add "Calishite" (ruling 5 allows a Faerûn ethnicity). Not settled; the page can take either.

**D3. Wiki ethnicity**
- Wiki: "| race           = [[Rakshasa]] disguised as [[human]]" (dump line 4008781). No ethnicity field is filled (`| ethnicity      = ` at dump line 4008782).
- Campaign and Appendix D say "Calishite". Lower ranked; the wiki leaves ethnicity blank.

**D4. Affiliation label**
- Page (line 6): "> - **Affiliation:** Trollskull Alley community"
- Quest overview (`campaign/quests/act-i/trollskull-alley/overview.md:34`): "- **Vincent Trench / Valantajar** (independent) — rakshasa detective at the Tiger's Eye; self-serving interest in the party"
- No organization page covers Vincent. Brief ruling 6 says a quest summary does not govern. The page label stays "Trollskull Alley community". Flag only: "(independent)" appears in a quest summary, and the page label is a neighborhood label, not a faction.

**D5. Price for services**
- Adventure: "50 gp is sufficient for most investigations" (`sources/adventure-wdh.json:3500`).
- Voice profile, Business sample: "Five gold a day and expenses." (`.claude/skills/character-voices/voices/trollskull-community.md:92`).
- Higher ranked: the adventure. The voice line is a sample line and is a day rate, a different unit. Drafter decides whether to keep the sample line; the profile is the figure's voice (ruling 16).

**D6. Half-steel dragon (PDF only)**
- PDF page 9 (printed p.186), transcription: "(Adric Thongolir, a half-steel dragon and youngest son of Lady Adiira Thongolir)"
- Appendix D: "Wants to hire the characters to follow a young noble: Adric Thongolir, youngest son of Lady Adiira Thongolir, believed to be meeting with someone he shouldn't." (`sources/Appendix_D_-_Running_the_Tavern.md:1295`). No "half-steel dragon" in Appendix D or the guide.
- Only the PDF gives the species. The PDF is transcribed from the image. Flag for pdftotext.

**D7. Thundercross Alley location (PDF only)**
- PDF page 9 (printed p.186), transcription: "(running perpendicular to Thunderstaff Way just north of Sashtar Street)".
- Appendix D and the guide give no location for Thundercross Alley (`sources/Appendix_D_-_Running_the_Tavern.md:1296`; `08-notable-patrons.md:45`). The PDF's location has no other campaign file (grep found none).

---

## E. Stale lines in other files (not edited) and routed quest references

- `campaign/structure/arc-b-trollskull-alley.md:98`: "Cross-ref **Appendix A** (Vincent Trench / Valantajar profile)." No file named Appendix A exists in `sources/` (Glob `sources/**/Appendix*` returns only Appendix B, C and D). Stale; the structure doc is superseded.
- `campaign/structure/arc-c-fireball.md:80`: "What he withholds is that he recognized it immediately and already knows who builds them." Superseded by `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:151`.
- `campaign/gazetteer/waterdeep/north-ward.md:148`: "Hook: after the **Fireball!** blast he arrives at the scene and knows more than he says, and he is the party's best-connected neighbor for information." — quest-time hook in the gazetteer's Characters of Interest. Routed to `ev-01-the-fireball.md:147` to `:153`.
- `campaign/gazetteer/waterdeep/north-ward.md:153`: "- Rishaal the Page-Turner has noticed that Vincent buys books on planar binding, and he shares his suspicion with a party that shows interest." — quest-time (shares with the party). Routed to `ev-03-the-neighbors.md:27`.
- `campaign/guides/trollskull-manor/08-notable-patrons.md:41`: "**2024 note:** ... Play him as the best-connected, most unsettling man in the North Ward until Act II when the reveal matters most." — the reveal timing ("Act II") is a quest-time plan, not a day-one fact.
- `campaign/guides/gm-guide/design-notes-running-the-campaign.md`: no Vincent line (not checked against Vincent; Jinny only at `:120`).
- `docs/plans/setting-compendium-research-notes/pass6/trollskull-community/01-talisolvanar-fellbranch.md`: no Vincent line.

**E-routed (quest-time references, the file where each already lives):** `ev-01-welcome-to-trollskull-alley.md:27`; `ev-03-the-neighbors.md:25`; `ev-06-the-grand-opening.md:40`; `overview.md:34` (Trollskull Alley); `fireball/ev-01-the-fireball.md:129`, `:147` to `:153`; `fireball/overview.md:31`; `sources/adventure-wdh.json:4489` (Jezrynne hired Vincent); `sources/Act_III_Arc_D.md:171`; `guides/trollskull-manor/06-tavern-time.md:31`, `:61`; `08-notable-patrons.md:38` to `:46`; Appendix D `:1109` and `:1275` to `:1297`; PDF printed p.186.

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with.

1. **Origin, birth and arrival in Waterdeep.** No source. The adventure says "The rakshasa has lived in Waterdeep for years" (`sources/adventure-wdh.json:3493`). The wiki says "Valantajar had lived for many years in Waterdeep" (dump line 4008836). Stay consistent with: years in the city, not a recent arrival; many identities; the city "has grown accustomed". No source gives a year.
2. **The identities before Vincent Trench.** The adventure says "switching identities as often as needed to keep its true nature hidden" (`:3493`). No names. Do not invent names; a nameless past identity is allowed by ruling 17.
3. **When Valantajar took the name Vincent Trench.** The wiki says the name and the Tiger's Eye are dated "By the 1492 DR" (dump line 4008833). No earlier date. Stay consistent with: the name is in use on Ches 1.
4. **How he came to run the Tiger's Eye.** No source. The wiki's "managed the Tiger's Eye, a detective business on Trollskull Alley" (dump line 4008833) is the only fact. The sign is "orange-and-black ... featuring a cat's eyes" (`:3492`).
5. **His faith, if any.** No source. Do not give a deity.
6. **His family, if any.** No source. The wiki leaves parents, spouses and children blank (dump lines 4008797 to 4008799).
7. **The rakshasa's own past (what he was before Waterdeep, why he stays).** No source beyond "fond" of the city (`:3493`; dump line 4008836). The "Morale" line says "He will flee Waterdeep before he will die in it." (page line 23), unsourced.
8. **His clients and the people he hires.** Tavern-time only (A2, C2). Do not put them in the Background.
9. **The Thundercross Alley theft and Adric Thongolir.** Tavern-time (Appendix D `:1295` to `:1296`; PDF printed p.186 only for the species and the location). Do not put them in the Background.
10. **The rate.** The adventure gives "50 gp is sufficient for most investigations" (`:3500`). The voice's "Five gold a day and expenses" is a sample line (D5).

---

## G. Inner-life hints in the sources (exact quotes)

These are the sourced hints a Background or the personal goals may use. They must not be contradicted.

- **Fondness for the city.** "is rather fond of Waterdeep and its citizens." — `sources/adventure-wdh.json:3493`; "was rather fond of the city and its inhabitants." — dump line 4008836 (`WDH5e-p32-33`). Page line 21 keeps "Deep down, he has grown genuinely fond of the city and its people". Consistent.
- **Surprise at the fondness.** "much to its own astonishment" — `sources/adventure-wdh.json:3493`; "to his own astonishment" — dump line 4008836.
- **Remembers everything.** "He will, however, remember everything that happens in his vicinity." — `sources/Appendix_D_-_Running_the_Tavern.md:1289`.
- **Never drinks the ale.** "Never drinks the ale — always spirits, always neat." — `sources/Appendix_D_-_Running_the_Tavern.md:1280`; `08-notable-patrons.md:39` ("always spirits, always neat").
- **Hands.** "His hands are backwards. Most people don't notice this." — `sources/Appendix_D_-_Running_the_Tavern.md:1278`. The page does not use this. It is a physical hint (drafter decides).
- **Voice sample on a past life (voice profile, not a source fact).** "Men like him are why I stopped eating people. The taste doesn't improve." — `.claude/skills/character-voices/voices/trollskull-community.md:85` (Swearing line, a sample). It implies a past. It is a voice sample; the drafter may use it only as a voice line and must not turn it into a backstory fact without a `[design]` tag.
- **Distance from the city.** "Very occasionally he refers to Waterdeep with the distance of someone much older than he looks." — voice profile line 87.
- **Never loses composure.** "He never loses composure in public, never reveals his nature" — voice profile line 89.
- **Comfortable life (page).** "Vincent wants to maintain his comfortable life in Waterdeep indefinitely" — page line 15 (day-one Motivations; keep verbatim).
- **Fear of the powerful (page).** "avoid drawing the attention of anyone powerful enough to see through his disguise" — page line 15.
