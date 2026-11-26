# Pass 6 research notes: Mattrim "Threestrings" Mereg

Page: `campaign/setting/notable-figures/harpers/03-mattrim-mereg.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR. Brief ruling 6: Threestrings is a Harper agent embedded at the Yawning Portal. He is never Doom Raiders or independent. Cassalanter secrecy and the Lolth rule do not reach this figure.
Organization page: `campaign/setting/organizations/01-harpers.md`
Factions Guide: `campaign/guides/factions/02-harpers.md`
Voice profile: `.claude/skills/character-voices/voices/harpers.md` ("### Mattrim "Threestrings" Mereg", lines 47-61)
Wiki: NOT FOUND. `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-harpers/03-mattrim-mereg.txt` reads `NOT FOUND`. No wiki edition exists for this figure. The wiki's Bonnie page is the only wiki text that names him (see A6).

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes are shown as plain quotes. `{@...}` tags are left as written. The `page` field is given where one exists.
- Alexandrian PDFs: there is no shell, so `pdftotext` could not run. Two PDFs were read as rendered page images and their quotes are transcriptions. Check each with `pdftotext -layout` before any quote goes into prose:
  - `sources/23. Addendum First Impressions.pdf`, PDF p.2 (printed p.163). Read: PDF pp.1-4.
  - `sources/3. Player Character Factions.pdf`, PDF p.2 (printed p.24). Read: PDF pp.1-3. No Mattrim or Bonnie text in that file.
- Alexandrian text files read: `sources/Appendix_B_-_Player_Factions.md`, `sources/Appendix_C_-_Player_Faction_Missions.md` (Harper mission and Enclave mission), `sources/Appendix_D_-_Running_the_Tavern.md`.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **Lodging is open.** The adventure says "He lives at the inn" (`sources/adventure-wdh.json:1526`, page 20, entry 044). No campaign file says he lodges at the Yawning Portal. The page says only "He plays the Yawning Portal most evenings" (L21). See D4.
2. **The two years are the campaign's number, and two sources disagree with it.** The organization page (`01-harpers.md:30`) and the Harper mission (`m03 ev-01:89`) say two years. Appendix C says "three months" (`Appendix_C_-_Player_Faction_Missions.md:264`), and the adventure says "He recently befriended" Bonnie (`adventure-wdh.json:1526`). The m03 design notes chose two years (`m03-the-doppelganger-auditions/design-notes.md:15`). See D3.
3. **Alignment: campaign and adventure say lawful good. Appendix D says chaotic good.** `Appendix_D_-_Running_the_Tavern.md:639` and `:1325` say CG. See D1. A stale line in `milil.md:117` misreports the staff table as CG. The table says LG (`03-staff-and-hiring.md:84`).
4. **Harper status conflicts with one appendix.** `Appendix_D_-_Running_the_Tavern.md:647` says "Mattrim is not a formal Harper agent." Every campaign file says Harper agent. See D2.
5. **Who knows Bonnie's nature conflicts.** The page (L25) and the organization page (`01-harpers.md:100`) say he is "the only person in Waterdeep who knows Bonnie's true nature." The Enclave quest says "Mattrim Mereg is not the only person outside the crew who knows" (`emerald-enclave/m03-the-doppelganger-problem/ev-01-the-doppelganger-problem.md:20`). See D6.
6. **Origin of the three strings conflicts across four sources.** The page says he "broke the others" (L21). The adventure says the lute "has only three strings remaining" (`adventure-wdh.json:1526`). Appendix D says "Missing the ring finger on his left hand — hence the nickname." (`Appendix_D_-_Running_the_Tavern.md:1327`). See D5.
7. **Overview is over the 21-word limit.** L29 is one sentence of 36 words. See C row 11.
8. **Stat block "Performer" is not in any source.** The adventure gives no stat block. Appendix D calls him "Bard of Lore" (`Appendix_D_-_Running_the_Tavern.md:639`, `:1325`). See B.
9. **Two Relationships clauses are quest-time.** "the subject of Harper mission three" and "a Trollskull Manor house bard candidate whose daytime audition is both genuine and convenient" (L25). Route both. See C row 10.
10. **No source gives his birth, home, family, past, or how he became a Harper.** The Background will need invented material tagged `[design]` (section F).

---

## A. Background facts by theme

### A1. Origin, birth, family, former life
No source gives a birth year, home district, family, parents, or former life. The wiki is NOT FOUND. The published adventure's entry is the only character sketch:

> "This socially awkward bard (see {@adventure appendix B|WDH|12}) performs at the Yawning Portal and is a better musician than he pretends to be. He's called \"Threestrings\" because he plays a lute that has only three strings remaining. His secret is that he's a Harper spy, and he's far more eloquent and composed than he lets on. He lives at the inn, where he spends his afternoons and evenings spying on Zhentarim agents and gathering information on other potential troublemakers. He recently befriended {@creature Bonnie|WDH} and wants to help her doppelganger gang settle into the city."
> — `sources/adventure-wdh.json:1526` (entry "Mattrim \"Threestrings\" Mereg", page 20, id 044)

Pronunciation key:
> "Mattrim Mereg"
> "MAT-trim MAIR-egg"
> — `sources/adventure-wdh.json:229`-`:230`

### A2. How he came to the post (Harper spy at the Yawning Portal)
The organization page places his settling in the Yawning Portal in the 1489 to 1491 DR bullet (day-one history):
> "- **1489 to 1491 DR, the Black Network arrives:** The Doom Raiders reached Waterdeep in 1489 DR to found a Zhentarim foothold and have been fending off Harper spies since. About 1490 DR Manshoon's cell began building the Splinter and the Black Network split `[research]`. In the same years Mattrim "Threestrings" Mereg settled into the Yawning Portal, where he has spent two years watching Zhentarim agents and befriending Bonnie's gang, and Mirt began a dossier on the Cassalanters that has not yet broken the surface. About a year ago the Howling Hatred cult led Mirt to suspect Cassalanter money."
> — `campaign/setting/organizations/01-harpers.md:30`

The adventure's recruitment rule (the organization page quotes it at `01-harpers.md:72`, where the full sentence reads "The published adventure says any smart, non-evil character can join the Harpers of Waterdeep, and that bards and wizards are especially welcome"):
> "Any smart, non-evil character can join the Harpers of Waterdeep. Bards and wizards are especially welcome."
> — `sources/adventure-wdh.json:1361` (Harpers section, page 16, id 03b)

### A3. Work and cover
> "Variel Duskwhisper tells one story per set that doubles as an intelligence report, Mattrim Mereg plays a mediocre bard at the Yawning Portal, Corvin Vayle passes folded notes between orders and Maxeene the draft horse listens at the hitching posts."
> — `campaign/setting/organizations/01-harpers.md:36` (the bullet is "Information Is the Currency"; rest of the bullet covers the wiki's informant habit and a Harper maxim)

> "**Fronts and covers:** Most Harper agents live a double life (Forgotten Realms Wiki, *Harpers*, edition not stated). Remi is the gracious lady of House Ulbrinter, Mirt is a moneylender, Mattrim Mereg is a middling bard at the Yawning Portal, Variel Duskwhisper is a touring musician, and Corvin and Nessa Vayle are servers who come as a pair. Maxeene is hired out by the day from a stand off Fillet Lane. The published adventure says the Harpers like to do business in busy inns such as the Yawning Portal, or in quiet places such as the City of the Dead."
> — `campaign/setting/organizations/01-harpers.md:62`

> "- **Gathering information:** Remi sends messages to her spies by a silver raven figurine, Variel's stories carry reports, Corvin passes folded notes, Maxeene listens at hitching posts and Mattrim watches the Zhentarim agents who drink at the Yawning Portal. The wiki says the Harpers keep drop boxes, hidden caches and safe houses, with at least thirty drop-offs in Waterdeep alone, and that they use a sign language, a system of marked runes and spoken code words (Forgotten Realms Wiki, *Harpers*, edition not stated)."
> — `campaign/setting/organizations/01-harpers.md:74` (rest of the bullet covers the raven, the drop boxes and the wiki's codes)

> "- **The Harpers (rival):** The Doom Raiders have fended off Harper spies since they reached Waterdeep, and Mattrim "Threestrings" Mereg, a Harper agent, spends his afternoons and evenings at the Yawning Portal watching Zhentarim agents (*Dragon Heist*, 5e; **Castle Ward**). The wiki says the Harpers and the Zhentarim all but waged war for about a century after 1269 DR (**The Harpers**). The Harpers know only that the Black Network has split."
> — `campaign/setting/organizations/06-doom-raiders.md:81`

> "- Durnan owns it and charges standard prices. Mattrim "Threestrings" Mereg plays here, Bonnie pours, Davil Starsong keeps a room, and a Bregan D'aerthe observer, Ryvarra, watches the well from the balcony."
> — `campaign/gazetteer/waterdeep/castle-ward.md:45`

Staff table, Trollskull Manor (campaign guide; this row is also quest-time, see C row 10):
> "| 1 | **Mattrim "Threestrings" Mereg** | LG Illuskan human | Already inside when the party arrives — was let in by the morning cleaner. Finishes a phrase before looking up. "I told your morning cleaner I was expected. She let me in. I know that's irregular." Holds up one finger. Finishes the phrase. "I'm Threestrings. I'd like the job. I'm the best thing that will walk through that door today." Missing ring finger; plays anyway. Probably right. | Harper agent. Feeds intelligence to Remallia Haventree through Mirt's network. Will pass one piece of street-level intelligence per tenday if asked. | 6 gp + tips (or 8 gp flat) | +1 Fame/tenday. +3 Revenue. |"
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:84`

### A4. Relationship to Mirt
The adventure gives Mattrim's Harper watch on the doppelgangers as a Harper task (the Harper mission, quoted in full in A5 and D8):
> "\"One of our members, Mattrim Mereg, has allied himself with a gang of doppelgangers and believes the Harpers should recruit them. We need an unbiased opinion. Track down and speak with each of the doppelgangers, and gauge their trustworthiness.\""
> — `sources/adventure-wdh.json:3868` (Harper mission, level "4th" at `:3867`)

The campaign's only statement of Mirt's view of him is in the Harper mission (quest time): "Mattrim Mereg is one of ours." (`campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/ev-01-the-doppelganger-auditions.md:40`). Route to the mission (C row 10).

### A5. Relationship to Bonnie and her gang (day-one)
> "This doppelganger posing as a friendly barmaid is the leader of a gang of five doppelgangers that arrived in Waterdeep over a year ago. To help the gang make ends meet, she works for {@creature Durnan|WDH} as a barmaid. Mattrim Mereg (see below) knows her secret."
> — `sources/adventure-wdh.json:1516` (entry "\"Bonnie\"", page 20)

The page (L11, L13, L15, L21) and the organization page (`01-harpers.md:30`, quoted in A2) agree on two years, affection and the secret. Voice profile: "Never: He never brags, never names his employers, and never says anything unkind about Bonnie." (`harpers.md:57`).

### A6. Wiki
NOT FOUND for Mattrim. The wiki's Bonnie page names him once, at its line 67 (`scratchpad/wiki-harpers/04-bonnie.txt`):
> "[[Mattrim Mereg]], a [[bard]] and [[Harper]] spy, knew her secret and wanted to help Bonnie.<ref name=\"WDH5e-p20\" />"
> — wiki line 67 of `04-bonnie.txt` (the page's citations are *Waterdeep: Dragon Heist*, 5e, page 20; the same line continues with the Harper recruitment and the Emerald Enclave, see the Bonnie notes)

The wiki's Stone of Golorr list names him only as a link (`sources/research/pass3-bundles/stone-of-golorr-and-the-eyes/wiki.txt:697`), so it adds no facts.

### A7. Habits, signature items, faith
- Three strings: see D5. The page says "plays three strings because he broke the others" (L21). The adventure says "a lute that has only three strings remaining" (`adventure-wdh.json:1526`).
- Shortsword: L23 says "draws his shortsword only to cover a retreat." No source gives him a shortsword. Gap, see F6.
- Faith: no devotion. The Milil page says: "The bards and entertainers among the Notable Figures (Mattrim "Threestrings" Mereg, Variel Duskwhisper, Davil Starsong, Margo Verida and Agorn Fuoco) have no stated devotion to him." (`campaign/setting/deities/milil.md:67`)
- Habits (quest-free): "He plays the Yawning Portal most evenings, drinks moderately, and is well-liked in the way that unremarkable people are well-liked." (L21). Voice: "He plucks a string while thinking." (`harpers.md:55`).

### A8. Rank, post, time in post
- Post: Harper agent embedded at the Yawning Portal (L25; `01-harpers.md:100`: "Illuskan human Harper spy embedded at the Yawning Portal under cover as a mediocre bard").
- Time in post: "two years" (L11, L15, L21; `01-harpers.md:30`). Conflicting figures in D3.
- Rank: none in the Factions Guide or org page. The Harpers' five titles are in `01-harpers.md:50` (Watcher through High Harper). No source gives him one.

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Page: "*Illuskan human bard (Harper spy), lawful good, he/him*. Stat block: **Performer**." — `campaign/setting/notable-figures/harpers/03-mattrim-mereg.md:5`
- Adventure: "{@i LG male Illuskan human bard}" — `sources/adventure-wdh.json:1525`
- Quest, m03 ev-01 (quest-time tag, but the label is the same): "Mattrim "Threestrings" Mereg (Lawful Good, Illuskan Human, he/him) :: a Harper agent who plays three strings badly on purpose and has spent two years befriending Bonnie's crew." — `campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/ev-01-the-doppelganger-auditions.md:89`
- Campaign, staff table: "LG Illuskan human" (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:84`)
- Appendix D: "*CG male human, Bard of Lore. The reference standard. See Patron Profiles.*" — `sources/Appendix_D_-_Running_the_Tavern.md:639` (conflict, D1)

**Species**
- Page: "Illuskan human" (L5). Org page: "Illuskan human Harper spy" (`01-harpers.md:100`). Adventure: "{@i LG male Illuskan human bard}" (`adventure-wdh.json:1525`). Appendix D: "*House Bard — CG Illuskan human, Bard of Lore; see Dragon Heist p. 201*" (`Appendix_D_-_Running_the_Tavern.md:1325`, conflict on alignment only).
- The Faerûn ethnicity rule (brief ruling 5) asks for "Tethyrian human" where a city is given. The sources give "Illuskan human," which is a Faerûn ethnicity. Use it as sourced.

**Pronouns**
- Page: "he/him" (L5). Quest tag: "he/him" (`m03 ev-01:89`). Adventure: "male" (`adventure-wdh.json:1525`).

**Stat block**
- Page: "Stat block: **Performer**." (L5). No source gives a stat block for him. The adventure gives none. Appendix D gives "Bard of Lore" (`:639`, `:1325`). The campaign uses "Performer" for other bards (Variel, Agorn), so "Performer" is a campaign convention, not a sourced stat block. `[research]`.

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/harpers/03-mattrim-mereg.md`. The page has no Background, no Personality section and no Connections section yet.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Illuskan human bard (Harper spy), lawful good, he/him*. Stat block: **Performer**." | Day-one. Alignment and pronouns sourced in B. Stat block unsourced | B |
| 2 | L6 | "- **Affiliation:** Harpers" | Day-one | `campaign/setting/organizations/01-harpers.md:100` |
| 3 | L7 | "- **Featured in:** **Finding Floon**, **Trollskull Alley**, **The Doppelganger Auditions**" | Quest-name list, not narrative. Matches the quest files that feature him | `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:8` |
| 4 | L11 | "**Resonance.** Threestrings should inspire warmth with his deliberate ordinariness; respect when the spy underneath the mediocre bard reveals itself; and gratitude when his two years of groundwork at the Yawning Portal proves exactly as valuable as a two-year investment should be." | Day-one (two years from `01-harpers.md:30`). Keep (ruling 3) | A2 |
| 5 | L13 | "**Emotions.** Threestrings most often feels casual sociability masking constant observation, quiet pride in a cover that holds, genuine affection for Bonnie and her gang, private conflict about what an honest assessment will mean for them, and the steady patience of a man who plays the long game." | Day-one feelings. "an honest assessment" points at the mission's deliverable: "Mirt wants the members to interview each one and tell him which they would trust." (`m03-the-doppelganger-auditions/overview.md:19`). Keep (ruling 3); flag the phrase to the drafter | `harpers/m03-.../overview.md:19` |
| 6 | L15 | "**Motivations.** Threestrings wants to maintain his Yawning Portal cover indefinitely, deliver an honest assessment of Bonnie's gang to the Harpers, and protect the people he has spent two years befriending, if he can find a way." | Day-one wants. "deliver an honest assessment" is the mission deliverable (row 5). Keep (ruling 3) | row 5; A5 |
| 7 | L17 | "**Inspirations.** When playing Threestrings, channel Tom Ripley (*The Talented Mr. Ripley*), Sam Malone (*Cheers*), and Elim Garak (*Deep Space Nine*)." | Not a fact. Keep | n/a |
| 8 | L21 | "**Persona.** To the world, Mattrim Mereg is a middling bard who plays three strings because he broke the others and has not gotten around to replacing them. He plays the Yawning Portal most evenings, drinks moderately, and is well-liked in the way that unremarkable people are well-liked. To those he trusts, he is a Harper operative who has spent two years building rapport with Bonnie's gang and knows their secret. Deep down, he has done his job too well — he likes them, and he knows what an honest report will probably recommend." | Day-one. "knows their secret" matches `adventure-wdh.json:1516`. "what an honest report will probably recommend" is the mission deliverable (row 5). "three strings because he broke the others" conflicts with the adventure (D5) | A5; D5 |
| 9 | L23 | "**Morale.** In a fight, Threestrings stays at the edge of it and draws his shortsword only to cover a retreat. He does not break cover for a fight he can avoid." | Encounter register, not a quest event. "shortsword" has no source (F6) | F6 |
| 10 | L25 | "**Relationships.** Threestrings is a Harper agent embedded at the Yawning Portal, the only person in Waterdeep who knows Bonnie's true nature, the subject of Harper mission three (an assessment of the doppelgangers), and a Trollskull Manor house bard candidate whose daytime audition is both genuine and convenient." | The first clause is day-one. "the only person in Waterdeep who knows Bonnie's true nature" conflicts with the quest file (D6). **"the subject of Harper mission three (an assessment of the doppelgangers)"** is quest time. Route to `campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/overview.md` and the Factions Guide `campaign/guides/factions/02-harpers.md:70`. **"a Trollskull Manor house bard candidate whose daytime audition is both genuine and convenient"** is quest time. Route to `campaign/guides/trollskull-manor/03-staff-and-hiring.md:84` and `:95` ("Must be auditioned") | `campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/overview.md:19`; `campaign/guides/factions/02-harpers.md:70`; `campaign/guides/trollskull-manor/03-staff-and-hiring.md:84`, `:95` |
| 11 | L29 | "A middling bard who plays most evenings at the Yawning Portal on a lute missing three strings, well-liked and easy to overlook, with no obvious reason to be watching the room as carefully as he is." | Day-one. **36 words** in one sentence; the brief limit is 21 words per sentence. The drafter must shorten | n/a |

Quest-time facts that the drafter must not carry as day-one (listed for routing):
- "Edric joined two months ago and sells what he learns to the Splinter" (`m03-the-doppelganger-auditions/ev-01-the-doppelganger-auditions.md:18`); "Mattrim learned a week ago that Bonnie had found trouble. She has not told him who." (`ev-01:20`); "Two years of drinks and one bad winter." (`ev-01:109`); "I think she's known for about three weeks" (`ev-01:310`).
- "Durnan's Warning" delivered through him at the Grand Opening (`campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:128`); the Finding Floon opening where he steers the party to a table (`campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:18`, `:96`, `:116`).
- Records room: "two weeks of notes on Mattrim" (`campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/ev-02-the-tail.md:19`). This is quest time.
- Appendix C's briefing (quest): "Mattrim Mereg — you may know him as Threestrings, the bard who busks at the Yawning Portal — has allied himself with a gang of doppelgangers" (`sources/Appendix_C_-_Player_Faction_Missions.md:253`). Mirt's response (quest): "Bonnie. Yes. I thought it might be Bonnie." (`:306`).

### Voice profile (`.claude/skills/character-voices/voices/harpers.md`, lines 47-61)
Quest-time or party-facing clauses (ruling 16 requires a day-one restatement or a flag):
- Line 54: "His loyalty to Bonnie's gang shows in how he steers talk away from them, and with the party he talks around them rather than about them." Day-one except "with the party he talks around them" (party-facing).
- Line 59 (Greeting sample): "Evening, friend. You're new. Don't request anything with a key change; I've only got the three strings and they're tired." "You're new" is addressed to the party. Flag.
- Line 60 (Business sample): "I've drunk with them two years. I know what they are. I'd like you to hear the whole of it before you write anything down." "I've drunk with them two years" is day-one (matches `01-harpers.md:30`). "I'd like you to hear the whole of it before you write anything down" is the assessment (quest). Flag.
- Line 61 (Under pressure sample): "Shit. Keep your voice down and keep smiling. Half this room is listening and the other half's pretending not to." Not quest-specific. Keep.
- Line 52: "Tavern talk: songs, regulars, who owes whom a drink." Day-one.

---

## D. Conflicts

**D1. Alignment: lawful good versus chaotic good**
- Page L5: "*Illuskan human bard (Harper spy), lawful good, he/him*." — `campaign/setting/notable-figures/harpers/03-mattrim-mereg.md:5`
- Adventure: "{@i LG male Illuskan human bard}" — `sources/adventure-wdh.json:1525`
- Campaign quest tag: "Mattrim "Threestrings" Mereg (Lawful Good, Illuskan Human, he/him)" — `campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/ev-01-the-doppelganger-auditions.md:89`
- Campaign staff table: "LG Illuskan human" — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:84`
- Appendix D: "*CG male human, Bard of Lore. The reference standard. See Patron Profiles.*" — `sources/Appendix_D_-_Running_the_Tavern.md:639`; "*House Bard — CG Illuskan human, Bard of Lore; see Dragon Heist p. 201*" — `:1325`
- Higher rank: campaign and adventure agree: lawful good. Appendix D is the conflict. `campaign/setting/deities/milil.md:117` says the staff table lists him "CG human" and cites `03-staff-and-hiring.md:84`; the table says "LG Illuskan human" (stale, E1).

**D2. Harper status: "Harper agent" versus "not a formal Harper agent"**
- Page L6 and L25: "- **Affiliation:** Harpers" (L6); "Threestrings is a Harper agent embedded at the Yawning Portal" (L25).
- Org page: "Illuskan human Harper spy embedded at the Yawning Portal" — `campaign/setting/organizations/01-harpers.md:100`
- Doom Raiders page: "Mattrim "Threestrings" Mereg, a Harper agent," — `campaign/setting/organizations/06-doom-raiders.md:81`
- Staff table: "Harper agent. Feeds intelligence to Remallia Haventree through Mirt's network." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:84`
- Appendix D: "**Faction Note:** Harper-adjacent. Mattrim is not a formal Harper agent but he feeds Remallia Haventree information through Mirt's network. Harper party members will know this and may find his employment at the tavern convenient in both directions." — `sources/Appendix_D_-_Running_the_Tavern.md:647`
- Higher rank: campaign (brief ruling 6). The Appendix D line is stale. Do not write "Harper-adjacent."

**D3. How long he has been befriending the gang: two years, three months, "recently"**
- Campaign, org page: "where he has spent two years watching Zhentarim agents and befriending Bonnie's gang" — `campaign/setting/organizations/01-harpers.md:30`
- Campaign, quest: "has spent two years befriending Bonnie's crew." — `m03-the-doppelganger-auditions/ev-01-the-doppelganger-auditions.md:89`
- Campaign, the m03 design notes: "The Notable Figures page for Mattrim says two years of groundwork, and the source says three months, so the page's two years is used." — `campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/design-notes.md:15`
- Appendix C: "But I've spent three months with them and I know them better than most people know anyone" — `sources/Appendix_C_-_Player_Faction_Missions.md:264`
- Adventure: "He recently befriended {@creature Bonnie|WDH} and wants to help her doppelganger gang settle into the city." — `sources/adventure-wdh.json:1526`
- Higher rank: campaign (two years). The adventure's "recently" and Appendix C's "three months" are lower-ranked.

**D4. Where he lives: at the inn or not**
- Adventure: "He lives at the inn, where he spends his afternoons and evenings spying on Zhentarim agents and gathering information on other potential troublemakers." — `sources/adventure-wdh.json:1526`
- Page L21: "He plays the Yawning Portal most evenings, drinks moderately, and is well-liked in the way that unremarkable people are well-liked." Does not say he lodges.
- Doom Raiders page: "spends his afternoons and evenings at the Yawning Portal watching Zhentarim agents" — `campaign/setting/organizations/06-doom-raiders.md:81`
- Higher rank: no campaign file says he lodges at the inn. Open for the orchestrator. A ruling is needed.

**D5. Why he is called "Threestrings"**
- Page L21: "a middling bard who plays three strings because he broke the others and has not gotten around to replacing them."
- Adventure: "He's called \"Threestrings\" because he plays a lute that has only three strings remaining." — `sources/adventure-wdh.json:1526`
- Appendix D: "**Appearance:** Missing the ring finger on his left hand — hence the nickname. Plays despite this." — `sources/Appendix_D_-_Running_the_Tavern.md:1327`
- Staff table: "Missing ring finger; plays anyway." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:84`
- Campaign quest, the Finding Floon opening: "**Threestrings** (Mattrim Mereg) performs near the back wall, a lute strung on three strings, which is all he claims to need." — `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:18`
- Campaign quest, m03: "plays three strings badly on purpose" — `m03-the-doppelganger-auditions/ev-01-the-doppelganger-auditions.md:89`
- Higher rank: the campaign page (L21) is the day-one line, but the adventure and Appendix D give other causes. Open. The drafter must choose one origin for the nickname.

**D6. Who knows Bonnie's nature**
- Page L25: "the only person in Waterdeep who knows Bonnie's true nature" — `campaign/setting/notable-figures/harpers/03-mattrim-mereg.md:25`
- Org page: "the only person in Waterdeep who knows Bonnie's true nature" — `campaign/setting/organizations/01-harpers.md:100`
- Enclave quest: "Melannor learned what Bonnie is from his animals, cats in the Portal's cellar and gulls over the quay. Mattrim Mereg is not the only person outside the crew who knows." — `campaign/quests/faction-events/emerald-enclave/m03-the-doppelganger-problem/ev-01-the-doppelganger-problem.md:20`
- Enclave design notes: "The Harpers organization page and Bonnie's Notable Figures page say only Mattrim knows her nature, though the Enclave's animals know too." — `campaign/quests/faction-events/emerald-enclave/m03-the-doppelganger-problem/design-notes.md:27`
- Adventure: "Mattrim Mereg (see below) knows her secret." — `sources/adventure-wdh.json:1516`. The adventure does not say "only."
- Higher rank: both are campaign. The Enclave's design note states the difference itself: the organization page and Bonnie's page say only Mattrim knows, "though the Enclave's animals know too." Open for the orchestrator.

**D7. Appearance**
- Appendix C: "He has lanky brown hair, gaudy clothes of purple and green, and the kind of goofy lopsided smile that people deploy to make you underestimate them." — `sources/Appendix_C_-_Player_Faction_Missions.md:261`
- Appendix D: "Missing the ring finger on his left hand" — `Appendix_D_-_Running_the_Tavern.md:1327`
- These describe a quest-time scene and do not conflict with a day-one fact. The page gives no appearance. Left to the drafter.

**D8. Harper mission numbering**
- Page L25: "the subject of Harper mission three (an assessment of the doppelgangers)" — `campaign/setting/notable-figures/harpers/03-mattrim-mereg.md:25`
- Factions Guide: "| 4th | **The Doppelganger Auditions** | Harper agent Mattrim Mereg wants to recruit a crew of five doppelgangers. Interview them and report which you would trust. One of them is selling the Harpers out, and only their leader Bonnie is recruited. | +3 |" — `campaign/guides/factions/02-harpers.md:70`
- Appendix B: "| 4th | **The Doppelganger Assessment** | Harper member Mattrim Mereg wants to recruit a gang of doppelgangers. Investigate their trustworthiness and report back. Only their leader Bonnie passes scrutiny. | +2 |" — `sources/Appendix_B_-_Player_Factions.md:166`
- "mission three" is the folder number (`m03-the-doppelganger-auditions/`). "4th" is the renown-tier level. Not a content conflict. The titles differ: "The Doppelganger Auditions" (Factions Guide) and "The Doppelganger Assessment" (Appendix B).

**D9. Stat block label**
- Page L5: "Stat block: **Performer**." No source uses "Performer" for him. Appendix D: "Bard of Lore" (`Appendix_D_-_Running_the_Tavern.md:639`, `:1325`).

---

## E. Stale lines in other files (do not edit) and routed quest references

**E1. Stale or conflicting lines in other files**
- `campaign/setting/deities/milil.md:117`: "The staff table lists Mattrim as "CG human" (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:84`) while his page says lawful good (`campaign/setting/notable-figures/harpers/03-mattrim-mereg.md:6`)." Stale: the table says "LG Illuskan human" (`03-staff-and-hiring.md:84`). The lawful-good label is on the page's L5, not L6.
- `campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/design-notes.md:21`: "...and Appendix B calls Mattrim not a formal agent." Stale. Appendix B line 166 says "Harper member Mattrim Mereg." The "not a formal agent" line is at `Appendix_D_-_Running_the_Tavern.md:647`.
- Same design-notes line 21: "The Bonnie and Mattrim Notable Figures pages call this "mission three" and "mission four" in different places." The Mattrim page says "mission three" (L25). No "mission four" appears on the Mattrim page.
- `campaign/setting/organizations/01-harpers.md:100` and `harpers/03-mattrim-mereg.md:25`: D6 (not stale in itself; conflicts with the Enclave quest).
- `sources/Appendix_D_-_Running_the_Tavern.md:647`: D2.

**E2. Routed quest references (the quest-time facts on the page)**

Harpers faction events (the day-one page must not restate these):
- `campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/overview.md:19`: "Mirt finds the eligible members in the common room of the Yawning Portal and takes them upstairs. Mattrim Mereg has befriended five doppelgangers and wants the Harpers to recruit them, and Mirt wants the members to interview each one and tell him which they would trust. He adds that, in his considered opinion, one of the five has already sold the party's Harper affiliation."
- `overview.md:31`: "Mirt gives the warning and the assignment in the upstairs room of the Yawning Portal, in his business voice. The members then meet Mattrim, who has arranged both evenings."
- `overview.md:66`: "- **Mattrim "Threestrings" Mereg** (Harpers): the Harper agent at the Portal who arranges the interviews."
- `campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/ev-01-the-doppelganger-auditions.md:40`: "> > "Mattrim Mereg is one of ours. He has made friends with five doppelgangers who live in this city, and he wants us to recruit them. Speak to each one and tell me which arrangement you would trust.""
- `ev-01:89` (the Lawful Good tag, D1); `ev-01:91`: "Mattrim is friendly and a little rueful, and he plucks a string while he thinks. He talks about the crew warmly and steers away from anything that sounds like an accusation. He swears mildly and at himself. He does not know which of them sold the Harpers out."
- `ev-01:109`: "> "Two years of drinks and one bad winter. I know what they are and I like them anyway. Buy a bard a drink and he'll tell you anything. Well. Something.""
- `ev-01:298`-`:310` (What Mattrim Knows): "Bonnie told me a week ago she'd found some trouble, but she wouldn't say who. I think she's known for about three weeks, and she thinks she can fix it herself, which she can't. Shit, I should have pushed her harder."
- `ev-01:407`: "Mattrim is relieved and a little competitive about having a Harper contact in his own tavern."
- `ev-02-the-tail.md:19`: "The records room holds three things: two weeks of notes on Mattrim, a list naming Lysa Fenwick of House Amcathra and Teren Moss of House Rosznar, and letters naming Beldan Rusk as the handler."
- `campaign/guides/factions/02-harpers.md:70` (the mission row, quoted in D8).
- `m03-the-doppelganger-auditions/design-notes.md:15` (two years, D3).

Trollskull Alley and Finding Floon:
- `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:8`: "> - Threestrings (Harper agent embedded at the Yawning Portal) introduces the party's situation and awaits Volo's arrival"
- `ev-01-yawning-portal.md:18`: "**Threestrings** (Mattrim Mereg) performs near the back wall, a lute strung on three strings, which is all he claims to need. He catches the party's eye during a break between songs and steers them to a table."
- `ev-01-yawning-portal.md:60`: "Threestrings picks up his lute and leads the Going Down Song from the back of the room"
- `ev-01-yawning-portal.md:96`: "Volo pushes through the settling crowd, steered to the party's table by Threestrings."
- `ev-01-yawning-portal.md:116`: "Threestrings can point them toward the Dock Ward generally."
- `campaign/quests/act-i/finding-floon/overview.md:23`: "- **Threestrings** (Harpers) — the party's contact at the Yawning Portal; introduces Volo, leads the Going Down Song"
- `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:128`: "**Durnan's Warning** — Durnan sends a one-line message through Threestrings, delivered at the end of the evening: "More activity than usual below. Nothing you need to worry about. Yet." The word "yet" is Threestrings's addition. When asked, he says he's pretty sure Durnan meant it. **Thread: Undermountain Is Active** (third path)."
- `campaign/quests/act-i/trollskull-alley/overview.md:47`: "- **Threestrings / Mattrim Mereg** (Harpers) — Durnan's message carrier at the Grand Opening"
- Structure doc: `campaign/structure/arc-a-finding-floon.md:233`: "2. **Party contact at the Yawning Portal.** **Threestrings** (Mattrim Mereg) — the bard performing at the YP. He greets the party, leads the Going Down Song, and introduces Volo. He is already in Appendix A; no new profile needed."
- `campaign/structure/arc-b-trollskull-alley.md:224`: "*Durnan's Warning.* Durnan sends a one-line message through Threestrings, delivered at the end of the evening" (partial; the sentence continues with the "yet" line).

Trollskull Manor guide (house bard mechanic, quest-time):
- `campaign/guides/trollskull-manor/03-staff-and-hiring.md:84` (the row, A3), `:95`: "| House Bard | +8 gp standard | +1 Fame (good) or −1 Fame (bad)/tenday | Must be auditioned; DC 13 Performance (GM reads it) |"
- `campaign/guides/trollskull-manor/04-fame.md:64`: "| Mattrim "Threestrings" Mereg as house bard (sustained) | +1/tenday |"
- `campaign/guides/trollskull-manor/04-fame.md:94`: "| House Bard audition fails publicly and embarrassingly | −3 |"
- `campaign/guides/trollskull-manor/06-tavern-time.md:29`: row "Tarsakh 11–20" lists "Mattrim "Threestrings" Mereg" among the patrons (the row also holds the Jarlaxle courier beat; rest of the row covers that beat).
- `campaign/guides/trollskull-manor/06-tavern-time.md:70`: "| 14 | Mattrim "Threestrings" Mereg *(reroll if currently employed as House Bard)* |"

Alexandrian appendices (quest-time):
- `sources/Appendix_C_-_Player_Faction_Missions.md:244`: "Harper operative Mattrim "Threestrings" Mereg has befriended a gang of doppelgangers and wants the organization to recruit them."
- `Appendix_C_-_Player_Faction_Missions.md:264` (three months, D3).
- `Appendix_C_-_Player_Faction_Missions.md:291`: "After the party completes all five interviews, Mattrim pulls them aside. He has been thinking. He has come to an uncomfortable conclusion."
- `Appendix_D_-_Running_the_Tavern.md:638`-`:649` (House Bard candidate, quest-time; the faction note at `:647` is D2).
- `Appendix_D_-_Running_the_Tavern.md:1324`-`:1335` (House Bard topics and agendas, quest-time; `:1335`: "Is being followed. He's noticed it, he's not worried, and he finds this reaction to being followed baffling in himself.").
- `Appendix_B_-_Player_Factions.md:166` (mission row).

Alexandrian PDF (quest-time; transcription, check with pdftotext):
- `sources/23. Addendum First Impressions.pdf`, PDF p.2 (printed p.163), STEP THREE: "Note: If they've selected Bonnie or Threestrings as their contact, then they're working. Perfect excuse for them to say, "Get a table and I'll come see you in a minute.""

---

## F. Gaps a Background needs that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes (brief ruling 17). Do not name a new Notable Figure. The adventure's Yawning Portal "Familiar Faces" handout is the only other place a named character is given to the party. Check it before naming anyone.

**F1. Birth year, birth name, home district, family, age.** No source gives any of these. The adventure gives no age. Mattrim has no wiki page. Do not name a relative. A nameless relative or place is allowed.

**F2. Former life before the Yawning Portal and how he became a Harper.** The only sourced line is "His secret is that he's a Harper spy" (`sources/adventure-wdh.json:1526`) and the recruitment rule: "Any smart, non-evil character can join the Harpers of Waterdeep. Bards and wizards are especially welcome." (`adventure-wdh.json:1361`). The wiki's rule, as the org page quotes it, is "a member in good standing must sponsor them and the High Harpers must approve" (`01-harpers.md:72`). Mattrim's sponsor, approval date and first mission are not named anywhere. No source says he was recruited as a bard. The rule says only that bards are "especially welcome."

**F3. Age, appearance on day one.** None as a day-one fact. Quest appearance: "lanky brown hair, gaudy clothes of purple and green" (Appendix C:261). Missing ring finger (Appendix D:1327; staff table:84). The cause of the missing finger is in conflict (D5).

**F4. Why he is called "Threestrings" (origin of the nickname).** Conflicting sources (D5). The drafter must choose one.

**F5. Lodging.** Conflict (D4).

**F6. Weapons and training.** The shortsword in L23 has no source. Any source for weapons would be invented. Mark `[design]` or drop the shortsword (L23 is verbatim, so the drafter decides).

**F7. His cover name and the cover itself.** The page gives "Threestrings" and "Mattrim Mereg." No cover name is sourced. The Factions Guide Brightcandle rank teaches a member a persona: "A Harper mentor teaches one *persona*: a false identity with a cover name, documentation, appropriate clothes, and two Harper contacts who will vouch for the story in person." (`campaign/guides/factions/02-harpers.md:60`). That is a rule for members, not a sourced fact about him. Do not state he has a second name.

**F8. Relationship with Mirt before the campaign.** None in day-one sources. The only sourced line is quest time: "Mattrim Mereg is one of ours" (`m03 ev-01:40`). The org page says Mirt "began a dossier on the Cassalanters" (`01-harpers.md:30`) and does not mention a dossier on Mattrim.

**F9. Losses, grudges, anyone he left behind.** None in any source.

**F10. Personal goals beyond the post.** None in any source. The page's Motivations give his wants (L15): "maintain his Yawning Portal cover indefinitely, deliver an honest assessment of Bonnie's gang to the Harpers, and protect the people he has spent two years befriending, if he can find a way." The Background explains where those come from. Brief ruling 17: the goals may not reveal a secret, an Event Outcome, a quest result or the Grand Game balance, and may not add a quest event. A goal about a person or a place he wants to keep is allowed as `[design]`.

**F11. Whether the Splinter knows he is a Harper.** Day-one sources say the cell is compromised but name no Splinter knowledge of Mattrim: "The Splinter has planted at least one double-agent in the Waterdeep Harper cell, exposed during **The Sleeping Asset**." (`campaign/guides/factions/02-harpers.md:22`, the Infiltration Risk callout, which is in the Factions Guide's Grand Game section). The only statement about the Splinter and Mattrim is quest time: "He has already told his buyer that Mattrim is a Harper agent." (`m03 ev-01:18`). Route. The day-one line about his watch is "Mattrim watches the Zhentarim agents who drink at the Yawning Portal" (`01-harpers.md:74`).

**F12. The three strings and the stat block.** See D5 and D9.

---

## G. Source facts that hint at the figure's inner life (for the backstory; do not contradict)

- "he's far more eloquent and composed than he lets on" — `sources/adventure-wdh.json:1526`
- "This socially awkward bard ... is a better musician than he pretends to be." — `sources/adventure-wdh.json:1526`
- Page L11: "gratitude when his two years of groundwork at the Yawning Portal proves exactly as valuable as a two-year investment should be." (`03-mattrim-mereg.md:11`)
- Page L13: "genuine affection for Bonnie and her gang, private conflict about what an honest assessment will mean for them, and the steady patience of a man who plays the long game." (`03-mattrim-mereg.md:13`)
- Page L21: "Deep down, he has done his job too well — he likes them, and he knows what an honest report will probably recommend." (`03-mattrim-mereg.md:21`)
- Page L15: "protect the people he has spent two years befriending, if he can find a way." (`03-mattrim-mereg.md:15`)
- Voice: "He makes himself small and likeable on purpose. His loyalty to Bonnie's gang shows in how he steers talk away from them" (`.claude/skills/character-voices/voices/harpers.md:54`)
- Voice: "When he's honest, he's careful and slow, and clearly weighing each word." (`harpers.md:54`)
- Voice: "Never: He never brags, never names his employers, and never says anything unkind about Bonnie." (`harpers.md:57`)
- Quest, m03 ev-01:109 (quest time): "I know what they are and I like them anyway." (`campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/ev-01-the-doppelganger-auditions.md:109`)
- Quest, m03 ev-01:310 (quest time): "Shit, I should have pushed her harder." (`ev-01:310`)
- Quest, Appendix C:264 (quest time): "These are my friends. I know what that sounds like." (`sources/Appendix_C_-_Player_Faction_Missions.md:264`)
- Quest, Appendix D:1335 (quest time): "Is being followed. He's noticed it, he's not worried, and he finds this reaction to being followed baffling in himself." (`sources/Appendix_D_-_Running_the_Tavern.md:1335`)
- Quest, m03 ev-01:407 (quest time): "Mattrim is relieved and a little competitive about having a Harper contact in his own tavern." (`ev-01:407`)

---

## Not found

- Mattrim's wiki page: NOT FOUND (the scratchpad file reads `NOT FOUND`).
- Birth, home, family, age, former life, origin of the nickname (no source agrees), cover name, shortsword, appearance on day one, how and when he joined the Harpers, his sponsor. Searched: `campaign/` (Grep for "Threestrings", "Mattrim", "Mereg", 25 files), `campaign/setting/notable-figures/harpers/` (both files), `sources/adventure-wdh.json` (Grep for "Threestrings", "Mattrim", "Mereg", "lute", "Bonnie", "Lymeria"), `sources/*.md` (Grep), `sources/research/` (Grep, all pass bundles, including the wiki bundle for harpers, which has no Mattrim entry), `sources/SOURCE_GUIDE.md`. Shortsword: Grep of `sources/` and `campaign/` for "shortsword" and "short sword" found it only for Soluun, Fel'rekt, Florette and the Dock Ward gunslinger.
- PDFs: `sources/3. Player Character Factions.pdf` (PDF pp.1-3) and `sources/23. Addendum First Impressions.pdf` (PDF pp.1-4) were read. Neither has any other Mattrim text. The Grep tool cannot search PDFs. The other Alexandrian PDFs were not searched for "Mattrim" or "Threestrings." Their text is not searchable here.
- Stat block for him: no source gives one. "Performer" is unsourced.
- Trollskull house bard's employment dates or pay history: `03-staff-and-hiring.md:84` gives the wage, not a history.

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. `sources/SOURCE_GUIDE.md:695` lists "The Waterdavian's Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx" as a "Broad NPC reference." It may hold Mattrim or Bonnie material. Not checked. The guide lists no individual `.docx` for Mattrim or Bonnie.
- The wiki page for Mattrim: not in the scratchpad (NOT FOUND).
