# Pass 6 research notes: Malkolm Brizzenbright

Page: `campaign/setting/notable-figures/bregan-daerthe/07-malkolm-brizzenbright.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Group folder: `bregan-daerthe`. Faction organization page: `campaign/setting/organizations/07-bregan-daerthe.md`. Villains page: none; `campaign/setting/villains/jarlaxle.md` names Malkolm only as left out (line 184).
Ruling used: Ches 1, 1492 DR. Malkolm is the non-hostile ghost of the Seven Masks Theater in the Dock Ward. He is an unknowing asset of Bregan D'aerthe and a witness to the theater's drow, not a combatant.
Voice profile: `.claude/skills/character-voices/voices/bregan-daerthe.md`, heading `### Malkolm Brizzenbright` (line 134).

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure `sources/adventure-wdh.json`: quoted as the JSON string. JSON escapes (`\"`) are shown as plain quotes, `—` is shown as an em dash, and tags such as `{@creature ...}` are left as written.
- Alexandrian PDF `sources/5. Faction Outposts.pdf`: no shell, so `pdftotext` could not run. Read as page images with the Read tool. Printed p.36 = PDF p.1. Printed p.37 = PDF p.2. The Bregan section ends on printed p.37 (PDF p.3 opens the Cassalanter Outposts at printed p.38). Every PDF quote below is a transcription. Check exact wording with `pdftotext -layout` before any wording goes into prose.
- Alexandrian appendices (`sources/Appendix_B/C/D`) and `sources/Act_III_Arc_E.md`: Grep only. Act_III_Arc_E.md has no Malkolm text.
- Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-bregan-daerthe/07-malkolm-brizzenbright.txt` reads `NOT FOUND`. There is no wiki page for Malkolm. Grep of `sources/research/pass5-bundles/bregan-daerthe/wiki.txt` and `adventure.txt` found no line naming Malkolm, Malcolm, Brizzenbright, Seven Masks or Rongquan.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDF and appendices, then the wiki (none).
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **The ghost haunts the Dock Ward, not the Trades Ward.** The published adventure places the Seven Masks in the Dock Ward: "Jarlaxle is waiting for them at the Seven Masks Theater in the Dock Ward." (`sources/adventure-wdh.json:9066`). It puts a different theater, "the Brizzenbright", in the Trades Ward (`sources/adventure-wdh.json:9115`). The campaign's own settlement reads: "The Seven Masks Theater is published in the Dock Ward (`:9066`, `:12034`); the Brizzenbright is a separate Trades Ward theater in Dragon Heist's winter version. The Alexandrian *Faction Outposts* (the Seven Masks Theater entry) transplants his ghost into the Seven Masks as its founder, so the merge is the remix's." (`campaign/gazetteer/waterdeep/dock-ward.md:306`, "Settled (Session 51)"). The Alexandrian PDF supports the move (`sources/5. Faction Outposts.pdf`, printed p.37).
2. **Death and species have thin sourcing.** "Dead for over thirty years" is sourced only to the Alexandrian PDF (printed p.37). No source gives a death year, cause, birthplace or ethnicity. "Chondathan" (page line 5) has no source at all and needs `[research]`. The page's "human" is also unsourced.
3. **Two voice-profile clauses are removed claims that the skill still carries.** The gazetteer's Session 51 note reads: "The "secret door to the Vault of Dragons", the "Lantanese machinery" and the handwriting claim were invented in an earlier session and are removed." (`campaign/gazetteer/waterdeep/dock-ward.md:306`). The voice profile still has "the machinery in the basement, the secret door he didn't build" (`.claude/skills/character-voices/voices/bregan-daerthe.md:141`) and "There is a machine in my basement, Lantanese, hideous, and a door I never built" (`:147`). The "handwriting that isn't Tethyrian" clause (`:141`, `:147`) is the third removed claim. Drop these clauses from the profile and report the change (ruling 16). The page does not carry them.
4. **Spelling is mixed across sources.** The campaign page, the voice heading and the adventure use "Malkolm". The Alexandrian PDF (printed p.37) and `campaign/structure/arc-e-faction-outposts.md:446` use "Malcolm". Use "Malkolm" (the campaign and the adventure agree).

---

## A. Background facts by theme

### A1. Origin, birth, birthplace and family (no source)

No source gives Malkolm's birth, origin, birthplace, age or family. The only physical description is the adventure's:

> "Malkolm Brizzenbright, a {@creature ghost}, greets all visitors in the lobby ({@area P1|191}). Dressed in a suit, his hair unkempt, he floats in plain sight most of the time, waving his hands about in gestures of greeting and salutation. Locals are accustomed to his spectral form and his stock introduction: \"Let not this harried visage diminish you, gentlesirs and beautiful ladies, for I am but your friendly host. What fine art have we wrought for you this day? Buy your tickets and behold! You shan't be disappointed!\""
> — `sources/adventure-wdh.json:9122` (Theater: Winter, "Brizzenbright's Ghost", page 76)

### A2. The theater: founder, owner and the name Rongquan

**Campaign, founder (Dock Ward gazetteer, GM Notes)**
> "- The ghost is Malkolm Brizzenbright, the theater's founder. He is not hostile, and he will tell a respectful visitor that \"Rongquan\" is a false identity and that drow come and go at irregular hours. Jarlaxle also uses the theater for neutral-ground meetings with other factions."
> — `campaign/gazetteer/waterdeep/dock-ward.md:76` (the GM Notes block is headed at line 73)

**Campaign, founder and ownership (organization page, Structure)**
> "**The Seven Masks Theater:** The theater stands in the Dock Ward, and its playbills name the owner as Rongquan Mystere. Jarlaxle owns it under that false name, and he uses it for neutral-ground meetings with other factions. The theater's founder, the ghost Malkolm Brizzenbright, still haunts it. One dressing room is kept empty as a safe house, and two drow guard it whenever it is in use."
> — `campaign/setting/organizations/07-bregan-daerthe.md:57`

**Campaign, the GM Notes on the false name (organization page)**
> "- **Other names:** Jarlaxle also owns the Seven Masks Theater as Rongquan Mystere, its Shou owner. Malkolm Brizzenbright's ghost knows \"Rongquan\" is a false identity."
> — `campaign/setting/organizations/07-bregan-daerthe.md:124`

**Alexandrian, founder and death (PDF transcription, printed p.37)**
> "Malcolm Brizzenbright: We'll also transplant Brizzenbright's Ghost from the Winter version of the Theater (see Dragon Heist, p. 76). He's the founder of the Seven Masks Theater, but has been dead for over thirty years."
> — `sources/5. Faction Outposts.pdf`, printed p.37 (PDF p.2). Transcription; check with pdftotext.

**Alexandrian, the owner under the Rongquan name (PDF transcription, printed p.37)**
> "SEVEN MASKS THEATER (Dragon Heist, p. 75): Use the description of the Autumn version of the theater from the original campaign. Jarlaxle owns this theater under the false identity of Rongquan Mystere. One of the dressing rooms is kept empty as a safe house for D'Aerthe agents in trouble. Jarlaxle will also use the theater as a \"neutral\" meeting place with other factions (including the PCs)."
> — `sources/5. Faction Outposts.pdf`, printed p.37 (PDF p.2). Transcription.

**Adventure, the owner of the Autumn theater (Rongquan is Jarlaxle)**
> "The owner of the theater is a burly and jovial Shou man with a braided goatee named Rongquan Mystere—another of Jarlaxle's many disguises. When Jarlaxle is away, he entrusts his stage managers to look after things."
> — `sources/adventure-wdh.json:9066` (Theater: Autumn, page 75)

**Adventure, the dead owner of the Winter theater (a different theater, see D1)**
> "As this encounter opens, the characters follow a fleeing Zhent swashbuckler into a theater in the Trades Ward called the Brizzenbright. Named after Malkolm Brizzenbright, its dead owner, the establishment has struggled in recent years. It stays open in the winter for its own survival, but the theater is wickedly cold this time of year."
> — `sources/adventure-wdh.json:9115` (Theater: Winter, page 76)

### A3. Death and the ghost's binding (pre-campaign; no death date in any source)

**Adventure, why the ghost stays (Winter theater)**
> "The ghost can engage in light conversation. It is bound to the theater because Malkolm Brizzenbright's soul couldn't bear to leave the place. If the theater were to close down, the ghost would haunt it still, perhaps becoming more deranged over time. Only razing or burning the theater to the ground can force his spirit to depart forever."
> — `sources/adventure-wdh.json:9123` (Brizzenbright's Ghost, page 76)

**Campaign, the ghost's state on Ches 1 (Overview of the page; the page gives no death date)**
> "The founding ghost of the Seven Masks Theater, dead for over thirty years — anxious about the new management, specific in his grievances, and waiting for someone worth telling."
> — `campaign/setting/notable-figures/bregan-daerthe/07-malkolm-brizzenbright.md:29`

Derived, not sourced: "over thirty years" before Ches 1, 1492 DR puts the death before about 1462 DR. No source states a year.

### A4. Dealings with Jarlaxle's company (day-one knowledge)

**Campaign, the false name and the lobby sighting (Factions Guide, Seven Masks outpost)**
> "Malkolm Brizzenbright haunts the building. He shares his knowledge with characters who treat him with respect, including the detail about \"Rongquan\" meeting with drow who mentioned the Sea Maidens Faire."
> — `campaign/guides/factions/08-bregan-daerthe.md:109`

**Alexandrian, what he knows (PDF transcription, printed p.37)**
> "He knows that \"Rongquan Mystere\" is a fake identity, and he's anxious that his theater not be used for nefarious purposes."
> "He can identify the dressing room being used as a safe house."
> "He once saw \"Rongquan\" speaking with drow in the lobby during a performance of The Mad Mage's Seven Riddles. They mentioned something called the \"Sea Maidens Faire\"."
> — `sources/5. Faction Outposts.pdf`, printed p.37 (PDF p.2), bullets under "Malcolm Brizzenbright". Transcription. "The Mad Mage's Seven Riddles" appears in no adventure file (Grep of `sources/adventure-wdh.json` for "Seven Riddles": no match).

**Campaign, the safe house and the ghost's roster (Factions Guide)**
> "**Roster:** Two **Drow** serving as safe house guards, present only when the dressing room is occupied. Malkolm Brizzenbright (**Ghost**, non-hostile)."
> — `campaign/guides/factions/08-bregan-daerthe.md:111`

**Campaign, the company's view (organization page, Key Members)**
> "- **Malkolm Brizzenbright** — Ghost, neutral. Founder of the Seven Masks Theater, dead for over thirty years. Anxious about what Jarlaxle is using his theater for. Knows \"Rongquan Mystere\" is a false identity, can identify the drow safe house dressing room, and once overheard \"Rongquan\" speaking with drow who mentioned the Sea Maidens Faire. See the **Malkolm Brizzenbright** page in Notable Figures."
> — `campaign/setting/organizations/07-bregan-daerthe.md:105`

**Campaign, the new management (voice profile, Word choice)**
> "- **Word choice:** Old theatre vocabulary: \"the house\", \"blocking\", \"my stage\", \"philistines\". He calls the drow \"the new management\" with disdain."
> — `.claude/skills/character-voices/voices/bregan-daerthe.md:139`

**Campaign, the pre-campaign lobby sighting (page Relationships)**
> "**Relationships.** Malkolm Brizzenbright is the founding ghost of the Seven Masks Theater, the one who knows \"Rongquan Mystere\" is a fake identity, the witness who can identify the dressing room Bregan D'aerthe keeps as a safe house, and the man who once saw \"Rongquan\" speaking with drow in the lobby during a performance of *The Mad Mage's Seven Riddles*, when they mentioned something called the Sea Maidens Faire."
> — `campaign/setting/notable-figures/bregan-daerthe/07-malkolm-brizzenbright.md:25`

**Campaign, how long the Rongquan transformation has run (structure doc; the only "two years" source)**
> "He has watched \"Rongquan Mystere\" transform his theater over the past two years and does not approve."
> — `campaign/structure/arc-e-faction-outposts.md:335` (Seven Masks outpost, Malkolm paragraph)

### A5. The theater's life (day-one habits)

> "- A public theater for a lower-class audience, where ship captains and sailors get in free (Dragon Heist). Playbills name the owner as Rongquan Mystere, and a booking manager who calls himself Kreb Sorrush handles casting inquiries and schedules. The theater has a ghost that moves props during rehearsals."
> — `campaign/gazetteer/waterdeep/dock-ward.md:70`

> "The Seven Masks Theater: playbills, a box office and a crowd of sailors admitted for free."
> — `campaign/gazetteer/waterdeep/dock-ward.md:239`

Adventure, the theater's struggles (Winter):
> "Named after Malkolm Brizzenbright, its dead owner, the establishment has struggled in recent years."
> — `sources/adventure-wdh.json:9115`

### A6. Soluun's murders (the ghost witnessed them; structure doc)

> "*Soluun's Murders.* A pattern emerges if the party investigates the *Bloodstained Playbill* further: seat numbers corresponding to elves and half-elves who attended the theater and subsequently disappeared. Soluun Xibrindas is stalking victims from the audience after performances. The pattern is discoverable through theater records (DC 14 Investigation) or through asking Malkolm, who witnessed it. This is not required for the main intelligence pipeline — but it is leverage. Jarlaxle is aware of Soluun's behavior and has not acted on it. \"He's useful\" is his entire position on the matter."
> — `campaign/structure/arc-e-faction-outposts.md:337` (Step 4 paragraph; the Malkolm paragraph is at line 335)

Campaign, the murderer's habit at the theater (the page this is built from is Soluun's, not Malkolm's):
> "**Morale.** In a fight, Soluun attacks without hesitation or mercy. He carries a bloodstained Seven Masks Theater playbill for Blood Wedding; he stalks and murders elven and half-elven audience members after shows. Jarlaxle is aware and hasn't yet decided what to do about it."
> — `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:23`

### A7. The ghost's standing at the theater (structure doc, Seven Masks outpost)

> "Malkolm Brizzenbright, the theater's ghost, is non-hostile. He appears in the backstage corridors as a translucent figure in a director's coat, carrying a script that was never performed. He is not a haunting — he is an anxious witness. He has watched \"Rongquan Mystere\" transform his theater over the past two years and does not approve. A party that treats him with respect earns his testimony: \"Rongquan\" is a false identity, drow use the dressing room at irregular hours, and he overheard a conversation about \"the Faire\" and \"cargo that must not be examined.\" See the **Malkolm Brizzenbright** page in Notable Figures."
> — `campaign/structure/arc-e-faction-outposts.md:335` (the testimony sentence is quest-time; see C and E5)

---

## B. Alignment, species, pronouns, stat block

**Alignment: neutral (campaign only)**
- Page: "> - *Chondathan human ghost, neutral, he/him*. Stat block: **Ghost**." — `campaign/setting/notable-figures/bregan-daerthe/07-malkolm-brizzenbright.md:5`
- Organization page: "- **Malkolm Brizzenbright** — Ghost, neutral." (quoted in full at `campaign/setting/organizations/07-bregan-daerthe.md:105`, see A4)
- Adventure: no alignment. `sources/adventure-wdh.json:9122` gives only "a {@creature ghost}".
- Alexandrian PDF: no alignment on printed p.37.
- Wiki: none.

**Species: "Chondathan human" (unsourced, needs `[research]`)**
- Page: "*Chondathan human ghost, neutral, he/him*." (`07-malkolm-brizzenbright.md:5`)
- No file in `campaign/`, `sources/` or the wiki gives a species or ethnicity for Malkolm. Grep of `campaign/setting` for "Chondathan" returned other NPC pages only; none names Malkolm.
- The gazetteer's Dock Ward entry gives the ghost no species: "The theater has a ghost that moves props during rehearsals." (`campaign/gazetteer/waterdeep/dock-ward.md:70`).

**Pronouns: he/him**
- Page: "*Chondathan human ghost, neutral, he/him*." (`07-malkolm-brizzenbright.md:5`)
- Adventure: "Dressed in a suit, his hair unkempt, he floats in plain sight most of the time" (`sources/adventure-wdh.json:9122`).
- Alexandrian PDF (printed p.37): "He's the founder of the Seven Masks Theater" (transcription).

**Stat block: Ghost**
- Page: "Stat block: **Ghost**." (`07-malkolm-brizzenbright.md:5`)
- Factions Guide: "Malkolm Brizzenbright (**Ghost**, non-hostile)." (`campaign/guides/factions/08-bregan-daerthe.md:111`)
- Adventure: "Malkolm Brizzenbright, a {@creature ghost}" (`sources/adventure-wdh.json:9122`). No stat numbers are given anywhere.

**Affiliation: Bregan D'aerthe (unknowing asset)**
- Page: "> - **Affiliation:** Bregan D'aerthe (unknowing asset; ghost of the Seven Masks Theater)" (`07-malkolm-brizzenbright.md:6`)
- Organization page, Key Members: listed under the company (`campaign/setting/organizations/07-bregan-daerthe.md:105`, quoted in A4).
- Quest label: "- **Malkolm Brizzenbright** (Bregan D'aerthe, unknowing asset): the theater's ghost, who knows the house better than its management." (`campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/overview.md:83`)

**Location: Dock Ward (campaign and adventure, Seven Masks), Trades Ward (adventure, Winter theater; see D1)**
- `campaign/gazetteer/waterdeep/dock-ward.md:69`: "**Seven Masks Theater** — Theater"
- `campaign/setting/organizations/07-bregan-daerthe.md:57` (quoted in A2).

---

## C. Sentences on the current page that narrate quest-time or depend on a discovery

Current page: `campaign/setting/notable-figures/bregan-daerthe/07-malkolm-brizzenbright.md`. The page has no Background, Personality or Connections yet.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Chondathan human ghost, neutral, he/him*. Stat block: **Ghost**." | Day-one label. "Chondathan" unsourced (B). | Section B |
| 2 | L6 | "**Affiliation:** Bregan D'aerthe (unknowing asset; ghost of the Seven Masks Theater)" | Day-one label. Matches `07-bregan-daerthe.md:105`. | Section A4 |
| 3 | L7 | "**Featured in:** **Faction Outposts**, **Sea Maidens Faire**" | Quest references, not lore. Malkolm also appears in the faction event `m05-the-theaters-back-room` (overview line 83; ev-01 lines 133 to 142). | `campaign/structure/arc-e-faction-outposts.md:321` (7B); `arc-h-sea-maidens-faire.md:335` and `:337` |
| 4 | L11 | "**Resonance.** Malkolm should inspire pity for a man who loved his theater enough to haunt it; endearment with his fussy pride in the building's artistic integrity; and useful surprise when his grievance against Jarlaxle turns out to be the intelligence the party needed." | Final clause is quest-time: the intelligence is paid off when the party gets his testimony. "loved his theater enough to haunt it" is a day-one inference with no source (the adventure gives "couldn't bear to leave the place", `sources/adventure-wdh.json:9123`). | Testimony: `campaign/structure/arc-e-faction-outposts.md:335`; `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:142` |
| 5 | L13 | "**Emotions.** Malkolm most often feels proprietary outrage at the drow who use his dressing room, anxious concern about the theater's reputation, a director's eye that notices everything that has changed, and the specific unhappiness of a ghost who died too early to see what his theater would become." | Day-one habits. "died too early" rests on the unsourced death date (A3, F1). "a director's eye" and "director's coat" are in the structure doc (`arc-e-faction-outposts.md:335`). | A3; A7 |
| 6 | L15 | "**Motivations.** Malkolm wants to protect the Seven Masks Theater's reputation, convince someone worth convincing that \"Rongquan Mystere\" is not who he claims, and move props in a way that communicates his displeasure without being dismissed as a poltergeist." | Day-one. "move props" is sourced (`dock-ward.md:70`). The "convince someone worth convincing" wish is a day-one wish, not a quest event. | A4, A5 |
| 7 | L17 | "**Inspirations.** When playing Malkolm, channel Nearly Headless Nick (*Harry Potter*), Casper (*Casper*), and Albert Brooks (*any comedy where he plays a man who is right about everything and cannot make anyone listen*)." | Not a fact. | n/a |
| 8 | L21 | "**Persona.** To the world, the Seven Masks Theater has a ghost that moves props during rehearsals and occasionally hisses at actors who project poorly. To those who speak with him, Malkolm Brizzenbright is the theater's founder — anxious that his theater not be used for nefarious purposes, certain that \"Rongquan Mystere\" is a false name, and able to point to the empty dressing room where drow agents in trouble hide. Deep down, he has been waiting for someone to tell, and the only question is whether they are worth telling." | Day-one. "hisses at actors" has no source beyond the voice profile (`bregan-daerthe.md:137`). The safe-house sentence is day-one (`08-bregan-daerthe.md:105`; Alexandrian p.37). | A2, A4 |
| 9 | L23 | "**Morale.** Malkolm is a ghost. He passes through walls, can terrify intruders, and moves props. He avoids combat because the theater cannot afford the damage." | Encounter behaviour. "passes through walls" and "terrify intruders" have no source. "moves props" is day-one (`dock-ward.md:70`). "He avoids combat because the theater cannot afford the damage" has no source. | F3 |
| 10 | L25 | "**Relationships.** Malkolm Brizzenbright is the founding ghost of the Seven Masks Theater, the one who knows \"Rongquan Mystere\" is a fake identity, the witness who can identify the dressing room Bregan D'aerthe keeps as a safe house, and the man who once saw \"Rongquan\" speaking with drow in the lobby during a performance of *The Mad Mage's Seven Riddles*, when they mentioned something called the Sea Maidens Faire." | Day-one. The lobby sighting happened before Ches 1 (past tense). Source for the sighting: Alexandrian p.37 only (PDF check). | A4 |
| 11 | L27 | "## Overview" heading | Not a fact. | n/a |
| 12 | L29 | "The founding ghost of the Seven Masks Theater, dead for over thirty years — anxious about the new management, specific in his grievances, and waiting for someone worth telling." | Day-one. "dead for over thirty years" sourced only to the Alexandrian p.37 (PDF check). One sentence, 28 words, over the brief's 21-word limit. | A3 |

**Voice profile (`.claude/skills/character-voices/voices/bregan-daerthe.md`, "### Malkolm Brizzenbright", lines 134 to 148)**

The Malkolm profile has no "after discovery" register. Its lines, with status:

> "- **Sound:** A reedy, theatrical, hollow voice with an actor-manager's diction, and a hiss when someone projects poorly." — line 137 (day-one; the "hiss" is also in the page's Persona, L21)

> "- **Sentence shape:** Long, aggrieved, theatrical complaints full of stage terminology. When someone finally listens, he gets eager and specific." — line 138 (day-one)

> "- **Word choice:** Old theatre vocabulary: \"the house\", \"blocking\", \"my stage\", \"philistines\". He calls the drow \"the new management\" with disdain." — line 139 (day-one; the same phrase appears in quest-time event text, `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:130`, see E3)

> "- **Swearing:** *Stingy · Euphemist · Clipped.* Old-fashioned and prim (\"Blasted\", \"confounded\"), then one real \"damn them\" he's proud of." — line 140 (day-one; the swearing stays, adult table)

> "- **Personality in speech:** Proprietary outrage and anxiety. He's specific about grievances: the machinery in the basement, the secret door he didn't build, the handwriting that isn't Tethyrian. He's thrilled when anyone takes him seriously." — line 141. **Removed claims, still in the profile.** "the machinery in the basement" and "the secret door he didn't build" are the claims that `campaign/gazetteer/waterdeep/dock-ward.md:306` says were "invented in an earlier session and are removed". "the handwriting that isn't Tethyrian" is the third removed claim. Drop these; keep "He's thrilled when anyone takes him seriously."

> "- **Quirks:** He critiques the party's diction. He moves props to make a point. He sighs dramatically." — line 142 (day-one; "critiques the party's diction" is an encounter habit with no source)

> "- **Signature phrases:** \"My stage!\" / \"Project, for pity's sake!\" / \"Finally, someone who listens.\"" — line 143 (day-one)

> "- **Never:** He never lets bad acting pass, never leaves the theatre, and never believes \"Rongquan Mystere\"." — line 144 (day-one; "never leaves the theatre" matches the adventure's Winter ghost, `sources/adventure-wdh.json:9123`, which says the ghost is bound to the theater)

> "  - *Greeting:* \"You there! Project! I can't hear you from the gallery, and I've no body, so that's saying something.\"" — line 146 (encounter greeting; no quest-time clause)

> "  - *Business:* \"There is a machine in my basement, Lantanese, hideous, and a door I never built, and a man whose handwriting is no more Tethyrian than I am alive.\"" — line 147. **Removed claims, still in the profile**, as line 141. The Business line is the only one in the profile that presupposes an item; no current Seven Masks source supports a handwriting item at the theater (`dock-ward.md:306` removes the handwriting claim).

> "  - *Under pressure:* \"Not my stage! Not my blasted stage!\"" — line 148 (day-one)

---

## D. Conflicts

**D1. Where the ghost haunts: Dock Ward or Trades Ward**
- Campaign, the Dock Ward: "The ghost is Malkolm Brizzenbright, the theater's founder." — `campaign/gazetteer/waterdeep/dock-ward.md:76`
- Campaign, the Dock Ward: "The theater stands in the Dock Ward, and its playbills name the owner as Rongquan Mystere." — `campaign/setting/organizations/07-bregan-daerthe.md:57`
- Adventure, the Dock Ward: "Jarlaxle is waiting for them at the Seven Masks Theater in the Dock Ward." — `sources/adventure-wdh.json:9066`
- Adventure, the Trades Ward: "into a theater in the Trades Ward called the Brizzenbright" — `sources/adventure-wdh.json:9115`
- Alexandrian, the ghost moved from the Winter theater: "We'll also transplant Brizzenbright's Ghost from the Winter version of the Theater (see Dragon Heist, p. 76)." — `sources/5. Faction Outposts.pdf`, printed p.37 (transcription)
- The campaign already records the conflict: "The campaign's Malkolm Brizzenbright haunts the Seven Masks Theater in the Dock Ward (`campaign/setting/notable-figures/bregan-daerthe/07-malkolm-brizzenbright.md:7`; `campaign/guides/factions/08-bregan-daerthe.md:101`), so the page does not list a Trades Ward theater." — `campaign/gazetteer/waterdeep/trades-ward.md:248`. This Draft Note cites line 7 of the page for the Dock Ward. Line 7 gives no ward (see E1).
- Ranking: the campaign (Dock Ward) governs. The adventure's Trades Ward theater is a different building in the Winter version, and the Alexandrian PDF supports moving the ghost.

**D2. Owner: "dead owner" or "founder, and Jarlaxle owns it"**
- Adventure: "Named after Malkolm Brizzenbright, its dead owner" (`sources/adventure-wdh.json:9115`)
- Campaign: "The theater's founder, the ghost Malkolm Brizzenbright, still haunts it." and "Jarlaxle owns it under that false name" (`campaign/setting/organizations/07-bregan-daerthe.md:57`)
- Alexandrian: "He's the founder of the Seven Masks Theater, but has been dead for over thirty years." (PDF transcription, printed p.37)
- Ranking: the campaign governs. The page should say "founder" and leave ownership to Jarlaxle's false name, as the organization page does.

**D3. The play in the lobby: "The Mad Mage's Seven Riddles" versus the Autumn version of the theater**
- Page: "during a performance of *The Mad Mage's Seven Riddles*" (`campaign/setting/notable-figures/bregan-daerthe/07-malkolm-brizzenbright.md:25`)
- Alexandrian: "during a performance of The Mad Mage's Seven Riddles" (PDF transcription, printed p.37). No adventure file names this play (Grep: no match).
- Campaign: "Use the Autumn version of the theater (DH p. 75)." (`campaign/guides/factions/08-bregan-daerthe.md:105`). The adventure's Autumn theater stages *Sapphiria's Booty* (`sources/adventure-wdh.json:9073` and `:9074`).
- Adventure, the Winter theater plays *Blood Wedding*: "during a performance of {@i Blood Wedding} -a play about love, jealousy, and death." (`sources/adventure-wdh.json:9132`)
- Campaign uses *Blood Wedding* at the Seven Masks: "He carries a bloodstained Seven Masks Theater playbill for Blood Wedding" (`campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:23`). This conflicts with the Autumn rule above.
- Ranking: the campaign's Autumn rule governs. The page's play title has only the Alexandrian source and sits outside the Autumn bill. The drafter should decide the title or drop it, and report the choice.

**D4. Spelling of the name**
- "Malkolm": `sources/adventure-wdh.json:9115`, `:9122`, `:9123`; the campaign page; the voice heading (`bregan-daerthe.md:134`).
- The gazetteer settles the spelling: "Dragon Heist spells the name \"Malkolm\" (`adventure-wdh.json:9115`) and the pages do too." (`campaign/gazetteer/waterdeep/dock-ward.md:306`).
- "Malcolm": Alexandrian PDF printed p.37 (transcription); `campaign/structure/arc-e-faction-outposts.md:446` ("Profiles for Malcolm Brizzenbright").
- Ranking: "Malkolm". Use "Malkolm".

**D5. Alignment and affiliation: campaign labels only**
- "neutral" appears only in the campaign (`07-malkolm-brizzenbright.md:5`; `07-bregan-daerthe.md:105`). No source conflicts. Not sourced beyond the campaign. Keep, but note it is a campaign decision.

**D6. Voice profile against the gazetteer's removed claims**
- Voice profile: "the machinery in the basement, the secret door he didn't build, the handwriting that isn't Tethyrian" (`.claude/skills/character-voices/voices/bregan-daerthe.md:141`)
- Gazetteer: "The "secret door to the Vault of Dragons", the "Lantanese machinery" and the handwriting claim were invented in an earlier session and are removed." (`campaign/gazetteer/waterdeep/dock-ward.md:306`)
- Ranking: the gazetteer's Session 51 settlement governs. The voice profile is stale on this point. Quoted in full at Finding 3.

---

## E. Stale lines in other files (not to be edited), and routed quest references

**E1. Stale citation.** `campaign/gazetteer/waterdeep/trades-ward.md:248` cites `campaign/setting/notable-figures/bregan-daerthe/07-malkolm-brizzenbright.md:7` for the Dock Ward. Line 7 is the "Featured in" line and names no ward. The page never says "Dock Ward".

**E2. Stale copy in the research bundles (older page text, old filename, not in the current file).** `sources/research/pass3-bundles/vault-of-dragons/campaign-hits.txt:507` quotes an older version of the page (the file path there is `07-malcolm-brizzenbright.md:26`):
> "Malcolm Brizzenbright is the founding ghost of the Seven Masks Theater, the only witness to the secret door between the theater and the Vault of Dragons, and a man whose handwriting analysis of Jarlaxle's correspondence is reliable to anyone with a Harper contact who has seen the original letters."

`sources/research/pass4-bundles/jarlaxle/campaign-hits.txt:1388` carries the same old line. The current page does not say this. No current file puts a secret door between the theater and the Vault (Grep of `campaign/structure/arc-j-vault-of-dragons.md` for Malkolm, Seven Masks and Brizzenbright: no match). The gazetteer removed the claim (`dock-ward.md:306`). Do not write a vault door from these bundle lines.

**E3. Quest-time copies of phrases.** `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:130`:
> "> > That's Malkolm, the founder. He's dead and furious, and he's moved the prop table four times since breakfast. He knows exactly what I am and calls the lot of us the new management, like it's an insult. If you ever talk to him, be polite, because he tells people things when they're polite."

This is Krebbyg's speech in a quest-time event. "since breakfast" and "knows exactly what I am" are event-time and have no source outside the event.

**E4. Other stale spellings.** `docs/plans/bregan-daerthe-research/01-spec-and-faction-rules.md:211` names the voice profile "Malcolm Brizzenbright (:134)". The current heading is "Malkolm".

**E5. Routed quest references (the page's Featured-in quests, and Malkolm's quest-time facts)**
- `campaign/structure/arc-e-faction-outposts.md:321` to `:340` (7B, Seven Masks Theater mini-heist; no quest journal exists). The Malkolm paragraph at line 335 includes the testimony: "A party that treats him with respect earns his testimony: \"Rongquan\" is a false identity, drow use the dressing room at irregular hours, and he overheard a conversation about \"the Faire\" and \"cargo that must not be examined.\""
- `campaign/structure/arc-e-faction-outposts.md:333`: "Stage Manager's Office (P6): *A Letter from K to J* — Krebbyg writing to Jarlaxle — warning that Fenerus's address has become known to a third party and recommending a new message drop." (a quest-time letter the party can find in the outpost; no source links it to Malkolm)
- `campaign/structure/arc-e-faction-outposts.md:293` and `:295`: "Malkolm Brizzenbright's ghost is the emotional counterweight to both: a man who wanted none of this and got all of it." and "Malkolm Brizzenbright is the emotional surprise — a ghost who wants his theater run honestly."
- `campaign/structure/arc-e-faction-outposts.md:451`: "Fenerus's decoded messages and Malkolm Brizzenbright's testimony are Three Clue Rule paths to the Faire as a heist target."
- `campaign/structure/arc-h-sea-maidens-faire.md:335`: "Malkolm Brizzenbright's ghost testimony about \"Rongquan Mystere.\""
- `campaign/structure/arc-h-sea-maidens-faire.md:337`: "Full NPC profiles for Jarlaxle, Soluun, Fel'rekt, Krebbyg, Zelifarn, Margo Verida, Khafeyta Murzan, Fenerus Stormcastle, Malkolm Brizzenbright."
- `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:133`: "> - **Auto:** the character has greeted Malkolm Brizzenbright by name, politely, and listens to what he says (see **The Ghost at the Stair**)."
- `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:138`: "> Malkolm Brizzenbright is moving programs at the foot of the gallery stair, and he is visible to anyone who speaks to him. He greets the party with a complaint, as he does the theater's staff, and warms to anyone who greets him by name without talking down to him. A character who does so hears:"
- `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:142`: "> Malkolm does not know who she works for or what she wants. He says \"my stage\" at least once, complains about the new management by his second sentence, and tells anyone who asks that \"Rongquan Mystere\" is not who he claims. If asked about the Faire, he says the new management talks about nothing else and he knows nothing more."
- `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/overview.md:38`: "Malkolm Brizzenbright, the theater's ghost, helps anyone who speaks to him politely."
- `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/design-notes.md:52`: "Constable Harl Pimm and Malkolm Brizzenbright are used as written in **Kreb Drops the Cover** and Malkolm's page."
- `campaign/quests/faction-events/bregan-daerthe/s02-kreb-drops-the-cover/ev-01-kreb-drops-the-cover.md:130` (quoted at E3).
- `campaign/guides/factions/08-bregan-daerthe.md:143`: "- Speaking with Malkolm Brizzenbright (Seven Masks Theater)" (Revelation List, Sea Maidens Faire lair).

**E6. Faction-label check.** The organization page says Bregan D'aerthe (`campaign/setting/organizations/07-bregan-daerthe.md:105`, Key Members). Consistent with the page. No Doom Raiders, Harper or Threestrings label applies to Malkolm.

---

## F. Gaps a Background needs that no source gives

For each gap, the sourced facts the drafter must stay consistent with.

**F1. Death: cause, year and circumstances.** No source gives a year, cause or circumstances of death.
- Sourced: "dead for over thirty years" (PDF p.37, transcription; `campaign/setting/organizations/07-bregan-daerthe.md:105`).
- Sourced: "its dead owner" (`sources/adventure-wdh.json:9115`) for the Trades Ward theater, which is a different building (D1).
- Sourced: "Malkolm Brizzenbright's soul couldn't bear to leave the place" (`sources/adventure-wdh.json:9123`). The soul stayed; the death is not dated.

**F2. Origin, birthplace, ethnicity, age, family, early life, how he founded the theater.** No source gives any of these. "Chondathan" is unsourced (B).
- Sourced: he is "the founder" of the Seven Masks (`campaign/gazetteer/waterdeep/dock-ward.md:76`; PDF p.37).
- Sourced: the Winter theater is "named after Malkolm Brizzenbright" (`sources/adventure-wdh.json:9115`).

**F3. Ghost powers and combat habits.** "passes through walls" and "terrify intruders" are not sourced. "moves props" is sourced (`dock-ward.md:70`). "He avoids combat because the theater cannot afford the damage" is not sourced. The Factions Guide gives "non-hostile" (`08-bregan-daerthe.md:111`). The drafter should keep "non-hostile" and "moves props", and treat the rest as `[research]`.

**F4. The basement machine and the secret door: removed, not to be restored.** The voice profile names them (`bregan-daerthe.md:141`, `:147`). The gazetteer says they were invented and removed (`dock-ward.md:306`). No current source puts a machine or a secret door in the Seven Masks. The drafter should not write them, and should report the voice-profile change.

**F5. Whether he knows Jarlaxle's face and name.** Sourced: he knows "Rongquan" is false (`dock-ward.md:76`; PDF p.37). Not sourced: whether he knows the person behind "Rongquan" is Jarlaxle. The organization page says "Malkolm Brizzenbright's ghost knows \"Rongquan\" is a false identity." (`07-bregan-daerthe.md:124`). Keep to that.

**F6. Personal goals beyond the theater.** No source gives a person he wants to find, a debt, a craft beyond the theater, or a hope. Sourced wants are the theater's reputation and the theater's honest running (`07-malkolm-brizzenbright.md:15` "protect the Seven Masks Theater's reputation"; `campaign/structure/arc-e-faction-outposts.md:295` "a ghost who wants his theater run honestly"). The drafter must invent under ruling 17 (`[design]`), and must not contradict the Motivations, Emotions and the adventure's "couldn't bear to leave the place" (`sources/adventure-wdh.json:9123`).

**F7. How long he has haunted the place, and what he did while alive.** No source. Sourced: "over the past two years" is the company's transformation of the theater (`arc-e-faction-outposts.md:335`), not Malkolm's tenure.

**F8. Faith and religion.** No source. The company's rule is "The Company Rejects Lolth" (`campaign/setting/organizations/07-bregan-daerthe.md:46`). Nothing says what Malkolm believes. Do not add a god.

**F9. Rank and place in the company.** No source. He is "Ghost, neutral" and "unknowing asset" (`07-bregan-daerthe.md:105`; `m05 overview:83`). He is not a company member in any file. Keep him an asset, not a member.

---

## G. Inner-life facts (exact quotes, for the Background and personal goals)

- **Grief and a refusal to leave.** "It is bound to the theater because Malkolm Brizzenbright's soul couldn't bear to leave the place. If the theater were to close down, the ghost would haunt it still, perhaps becoming more deranged over time. Only razing or burning the theater to the ground can force his spirit to depart forever." — `sources/adventure-wdh.json:9123`
- **Showmanship.** "Locals are accustomed to his spectral form and his stock introduction: \"Let not this harried visage diminish you, gentlesirs and beautiful ladies, for I am but your friendly host. What fine art have we wrought for you this day? Buy your tickets and behold! You shan't be disappointed!\"" — `sources/adventure-wdh.json:9122`
- **Anxiety for the theater.** "he's anxious that his theater not be used for nefarious purposes." — PDF p.37 (transcription).
- **Waiting to be heard.** "Deep down, he has been waiting for someone to tell, and the only question is whether they are worth telling." — `campaign/setting/notable-figures/bregan-daerthe/07-malkolm-brizzenbright.md:21`
- **Pride in the building.** "endearment with his fussy pride in the building's artistic integrity" — `07-malkolm-brizzenbright.md:11`
- **A regret.** "the specific unhappiness of a ghost who died too early to see what his theater would become." — `07-malkolm-brizzenbright.md:13`
- **Watching the company.** "He has watched \"Rongquan Mystere\" transform his theater over the past two years and does not approve." — `campaign/structure/arc-e-faction-outposts.md:335`
- **A witness to murder.** "through asking Malkolm, who witnessed it." — `campaign/structure/arc-e-faction-outposts.md:337` (about Soluun's murders in the audience)
- **A script never performed.** "carrying a script that was never performed." — `campaign/structure/arc-e-faction-outposts.md:335`
- **Pleasure in being taken seriously.** "He's thrilled when anyone takes him seriously." — `.claude/skills/character-voices/voices/bregan-daerthe.md:141`
- **Hates a poor performance.** "He never lets bad acting pass" — `bregan-daerthe.md:144`; "a hiss when someone projects poorly" — `bregan-daerthe.md:137`
- **Never leaves the theatre.** "never leaves the theatre" — `bregan-daerthe.md:144`

Not for the Background's invention, but must not be contradicted: Malkolm "is not a haunting — he is an anxious witness." (`arc-e-faction-outposts.md:335`)

---

## Not found

- **Wiki**: the extracted page reads `NOT FOUND` (the scratchpad file). Grep of `sources/research/pass5-bundles/bregan-daerthe/wiki.txt` and `adventure.txt`: no line for Malkolm, Malcolm, Brizzenbright, Seven Masks or Rongquan.
- **Terms searched in campaign**: "Malkolm", "Malcolm", "Brizzenbright", "Seven Masks", "Rongquan", "Chondathan", "thirty years" across `campaign/` (structure, locations, guides, gazetteer, setting, quests). Results are reported above. No match for a death year, a birthplace or an ethnicity for Malkolm.
- **Terms searched in sources**: "Malkolm|Brizzenbright|Seven Masks|Rongquan|Mystere" in `sources/adventure-wdh.json` (hits at lines 281, 7152, 7154, 9066 to 9096, 9115, 9122, 9123, 12034). "Seven Riddles" in the adventure: none. Appendix B, C, D and `Act_III_Arc_E.md`: Appendix C lines 1223 and 1225 (Doom Raiders outcome) only; no Malkolm text in Appendix B, Appendix D or Act_III_Arc_E.md.
- **Machine and secret door**: no current match for "machine" or "Lantanese" at the Seven Masks in the gazetteer, factions guide or structure docs. The gazetteer's Session 51 note removes them (`dock-ward.md:306`).
- **Vault of Dragons link**: no current file (see E2).

---

## Not readable

- `sources/Other remix files/Jarlaxle Baenre NPC Guide.docx`: listed in `sources/SOURCE_GUIDE.md:690` for the Bregan D'aerthe organization page and Sea Maidens Faire, and so possibly holds Malkolm or the Seven Masks. Not opened (`.docx` cannot be read with these tools). The drafter should extract it and check for Malkolm and the theater.
- Alexandrian PDFs not read: `sources/9. Lair – Sea Maidens Faire.pdf` (the Sea Maidens Faire lair, which the page lists as Featured-in), `sources/11. Lair  Xanathar’s Lair.pdf` (the Seven Masks report X35 in the campaign structure doc), `sources/17. Outpost and Lair Revelation Lists.pdf`. They may mention Malkolm or the theater. Not checked.
