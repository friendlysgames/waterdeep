# Pass 6 research notes: Harug Shieldsunder

Page: `campaign/setting/notable-figures/independents-allies/12-harug-shieldsunder.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 19, user rulings Session 53)
Day one: Ches 1, 1492 DR.
Organization page: none. No `campaign/setting/organizations/` page covers the Black Tears. Affiliation label is on the page at line 6 (see D4).
Factions Guide: none names Harug.
Voice profile: `.claude/skills/character-voices/voices/independents-allies.md` lines 228 to 242.
Model format: `docs/plans/setting-compendium-research-notes/pass6/trollskull-community/01-talisolvanar-fellbranch.md`

## Method and caveats

- Campaign files: Grep and Read. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json` has no line naming Harug or Shieldsunder (grep). Undermountain (`sources/adventure-wdmm.json`): no match.
- Alexandrian: `sources/Appendix_D_-_Running_the_Tavern.md:1140` (markdown table row only; no profile). `sources/27. Addendum A Night in Trollskull Manor.pdf` PDF page 8 (printed p.185): "16 Harug Shieldsunder". Transcription: check with `pdftotext -layout`. `sources/26. Addendum Other Collaborators.pdf` and `sources/2. Other Factions.pdf` read in full: no match.
- Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-independents-allies/12-harug-shieldsunder.txt` is a real page. Its only citation is the novel *Blackstaff Tower* (the page links `Blackstaff Tower (novel)`, wiki line 76). Edition is not tagged. Cited as "wiki line N".
- `voicecheck.py` was not run. No shell. No file was edited except this notes file.

## Findings that change how the page is written

1. **The wiki has Harug as a Cellarers' and Plumbers' Guild member and tunnel worker.** Wiki line 56 says he was "a [[dwarf]] and member of the [[Cellarers' & Plumbers' Guild]] of [[Waterdeep]]", and line 59 says "one of the guild's best tunnel workers". The campaign's "shield dwarf fighter" and "Veteran" stat block are campaign-only. The campaign never mentions the guild for Harug. See D1.
2. **The wiki names two people in his life that the campaign does not.** Laraelra Harsard, "good friends" (wiki line 62), and Dorn Strongcraft, his nephew (wiki line 62). Dorn appears in no campaign or adventure file (grep).
3. **Harug's page has no origin, date or history.** The Background has to be built from the wiki's guild and friendship facts, plus `[design]`, under ruling 17.

---

## A. Background facts by theme

### A1. Origin, kind and guild (wiki, Blackstaff Tower novel)

> "'''Harug Shieldsunder''' was a [[dwarf]] and member of the [[Cellarers' & Plumbers' Guild]] of [[Waterdeep]].<ref name="BST-p28-30">{{Cite book/Blackstaff Tower|28-30}}</ref>"
> — `scratchpad/wiki-independents-allies/12-harug-shieldsunder.txt`, wiki line 56

> "Harug was called "most cantankerous dwarf in the city," but was considered one of the guild's best tunnel workers.<ref name="BST-p28-30">{{Cite book/Blackstaff Tower|28-30}}</ref>"
> — wiki line 59 (section "Personality")

> "Harug and Laraelra Harsard were good friends.<ref name="BST-p29">{{Cite book/Blackstaff Tower|29}}</ref> Harug was the uncle of [[Dorn Strongcraft]].<ref name="BST-p28-30">{{Cite book/Blackstaff Tower|28-30}}</ref>"
> — wiki line 62 (section "Relationships")

> "| languages      = [[Dwarvish]]<ref name="BST-p86">{{Cite book/Blackstaff Tower|86}}</ref>"
> — wiki line 19

Context: the Cellarers' and Plumbers' Guild exists in the campaign. The governance page lists it in the Trollskull Alley guild checklist: "Cellarers' and Plumbers' Guild (basement and plumbing)" (`campaign/setting/governance-and-guilds/guilds.md:40`). Harug's membership is wiki-only.

### A2. Friends and the circle (campaign)

- "Harug is a member of Renaer's Black Tears and the group's frontline fighter, paired informally with Parlek as the muscle-and-finesse pairing of the circle." — `campaign/setting/notable-figures/independents-allies/12-harug-shieldsunder.md:25`
- "Harug wants to keep the Black Tears alive through whatever Renaer drags them into, and drink in peace. He does not complicate things further." — `12-harug-shieldsunder.md:15`
- Renaer's page: "Renaer is the estranged son of Dagult Neverember (former Open Lord, current Lord of Neverwinter), the devoted friend of Floon Blagmaar, the closest living friend of Meloon Wardragon (whose changed behavior has him alarmed), a man who rescued Vajra Safahr from Khondar Naomal's agents and left the Blackstaff permanently in his debt, a Harper-adjacent ally of Mirt and Remi Haventree, and the leader of the Black Tears (his personal circle of trusted companions)." — `campaign/setting/notable-figures/independents-allies/02-renaer-neverember.md:25`
- Parlek's page: "**Relationships.** Parlek is a member of Renaer's Black Tears, Harug's informal partner in the group's security (brains and brawn), and a man whose past is politely unexamined by his friends." — `campaign/setting/notable-figures/independents-allies/13-parlek-lateriff.md:25`

### A3. Manner, morale and the wall (campaign and voice)

- "In a fight, Harug would step forward, shield up, and hold the line until everyone behind him is clear. He does not retreat while allies are still engaged." — `12-harug-shieldsunder.md:23`
- Voice: "**Word choice:** Plain dwarven bluntness: "Aye", "No", "Drink"." — `.claude/skills/character-voices/voices/independents-allies.md:233`
- Voice: "**Quirks:** He grunts meaningfully. He checks that everyone got home, and says "Home?" to each of them." — `independents-allies.md:236`

### A4. Time in post, dates and places

- No source gives Harug's age, birthplace, how he came to Renaer or when he joined the guild. The wiki gives no date for either (wiki lines 56 to 62).
- Dwarvish is his language (wiki line 19).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Summary: "> - *Shield dwarf fighter, lawful neutral, he/him*. Stat block: **Veteran**." — `campaign/setting/notable-figures/independents-allies/12-harug-shieldsunder.md:5`
- Campaign-assigned: "All six (Elra, Osco, Torlyn, Eiruk, Harug, Parlek) lacked alignment in their stat lines. Alignments assigned and committed (`c0c6bde`)." — `session 5 handoff.md:73`
- Wiki: "| alignment5e    = " (blank) — wiki line 52
- Appendix D: "| 16 | Harug Shieldsunder |" (`sources/Appendix_D_-_Running_the_Tavern.md:1140`). No alignment.

**Species**
- Summary: "Shield dwarf" (`12-harug-shieldsunder.md:5`). "Shield" is campaign-only.
- Wiki: "| race           = [[Dwarf]]" — wiki line 14. Wiki line 56: "was a [[dwarf]]".

**Pronouns**
- Summary: "he/him" (`12-harug-shieldsunder.md:5`)
- Overview: "Harug Shieldsunder is a shield dwarf fighter and the frontline muscle of Renaer Neverember's Black Tears, a man who says little and holds the line." — `12-harug-shieldsunder.md:29`
- Wiki: "| sex            = Male" — wiki line 13

**Stat block**
- Summary: "Stat block: **Veteran**." (`12-harug-shieldsunder.md:5`)
- Wiki: "| class          = " (blank) — wiki line 35. Campaign-only.

**Name spelling**
- Campaign: "Harug Shieldsunder" (page H1; Appendix D `sources/Appendix_D_-_Running_the_Tavern.md:1140`; tavern guide `campaign/guides/trollskull-manor/06-tavern-time.md:94`).
- Wiki: "| name           = Harug Shieldsunder" — wiki line 5. The sort key "{{DEFAULTSORT:Shielfsunder, Harug}}" (wiki line 1) is a typo. Use the campaign spelling.

---

## C. Sentences on the current page that narrate a quest-time event or a day-one conflict

The page has no quest event and no Background section yet. Every sentence on the page was checked.

| Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|
| L7 | "> - **Featured in:** Background figure; no scripted appearance." | Campaign label. Not an event. | Renaer's Friends row: `campaign/guides/trollskull-manor/06-tavern-time.md:94` |
| L11 | "**Resonance.** Harug should inspire confidence with his unshakable physical presence, endearment with his gruff loyalty, and amusement when he expresses complex emotions through one-word answers." | Day one. Keep. | none needed |
| L13 | "**Emotions.** Harug most often feels protective vigilance, gruff contentment, unspoken pride, stubborn refusal to explain himself, comfortable silence, and occasional surprise at how much he enjoys these people." | Day one. Keep. | none needed |
| L15 | "**Motivations.** Harug wants to keep the Black Tears alive through whatever Renaer drags them into, and drink in peace. He does not complicate things further." | Framing. "whatever Renaer drags them into" points at the campaign's events and names none. Drafter's call (C2). | none needed |
| L21 | "**Persona.** To the world, Harug is a shield dwarf who drinks with Renaer's friends and says little. To those he trusts, he is the one who checks that everyone got home safe. Deep down, he has found something worth protecting, and he would rather break a table than admit it." | Day one. "something worth protecting" names nothing; see F6. | none needed |
| L23 | "**Morale.** In a fight, Harug would step forward, shield up, and hold the line until everyone behind him is clear. He does not retreat while allies are still engaged." | Day one. Keep. | none needed |
| L25 | "**Relationships.** Harug is a member of Renaer's Black Tears and the group's frontline fighter, paired informally with Parlek as the muscle-and-finesse pairing of the circle." | Day one. Keep. | Parlek page L25 (A2) |
| L29 | "Harug Shieldsunder is a shield dwarf fighter and the frontline muscle of Renaer Neverember's Black Tears, a man who says little and holds the line." | Day one. Keep. | none needed |

### C2. Framing line (not a quest event; drafter's call)

- L15 "whatever Renaer drags them into" names no event. Keep, or restate as a day-one concern under ruling 1.

### C3. Renaer's Friends table and the tavern (routed; tavern-time)

- Campaign: "| 16 | Harug Shieldsunder |" — `campaign/guides/trollskull-manor/06-tavern-time.md:94` (heading "## Renaer's Friends Table (d20)" at line 84)
- Campaign: "Use this four-step procedure for each significant night the characters spend at the tavern." — `campaign/guides/trollskull-manor/06-tavern-time.md:5`
- Appendix D: "| 16 | Harug Shieldsunder |" — `sources/Appendix_D_-_Running_the_Tavern.md:1140` (heading "### Renaer's Friends Table" at line 1130)
- Addendum PDF page 8 (printed p.185), transcription: "16 Harug Shieldsunder". Check with pdftotext.
- Tavern status: "A long-closed tavern, Trollskull Manor, stands at the end of Trollskull Alley among old residences and shops." — `campaign/gazetteer/waterdeep/north-ward.md:203`
- Ownership by the party: "The deed is real. **Trollskull Manor** is real, non-operational, and now the party's property." — `campaign/quests/act-i/finding-floon/ev-04-xanathar-sewer-hideout.md:100`

### C4. Voice profile (`.claude/skills/character-voices/voices/independents-allies.md`, lines 228 to 242)

- Line 229 (tagline): "*The Black Tears' dwarven wall: one word where others use ten.*" — no quest event.
- Line 240 (Greeting): "*Greeting:* "Aye."" — no quest event.
- Line 241 (Business): "*Business:* "Front. Me."" — no quest event.
- Line 242 (Under pressure): "*Under pressure:* "Behind me. Now."" — no quest event.
- Line 236 (Quirks): "**Quirks:** He grunts meaningfully. He checks that everyone got home, and says "Home?" to each of them." — day one.
- No profile change is needed for a quest-time clause.

---

## D. Conflicts

**D1. Occupation and class (campaign fighter vs wiki guild tunnel worker)**
- Campaign summary: "> - *Shield dwarf fighter, lawful neutral, he/him*. Stat block: **Veteran**." — `campaign/setting/notable-figures/independents-allies/12-harug-shieldsunder.md:5`
- Wiki: "'''Harug Shieldsunder''' was a [[dwarf]] and member of the [[Cellarers' & Plumbers' Guild]] of [[Waterdeep]]." — wiki line 56
- Wiki: "Harug was called "most cantankerous dwarf in the city," but was considered one of the guild's best tunnel workers." — wiki line 59
- Not a direct contradiction. The wiki gives no class or combat role, so "fighter" and "tunnel worker" can both be true. The "fighter" and "Veteran" labels are campaign-only. Higher ranked: the campaign for the page's class; the wiki for the guild membership, marked `[research]` unless the drafter ties it in. Do not write "tunnel worker" as a day-one fact without the drafter's decision.

**D2. Species (no conflict)**
- Campaign: "shield dwarf" (`12-harug-shieldsunder.md:5`). Wiki: "[[dwarf]]" (wiki line 56). "Shield" is a sub-type the wiki does not use.

**D3. Name spelling (no conflict in content)**
- Campaign and Appendix D use "Shieldsunder" (`sources/Appendix_D_-_Running_the_Tavern.md:1140`). Wiki H1 "Harug Shieldsunder" (wiki line 5). Sort key typo "Shielfsunder" (wiki line 1).

**D4. Affiliation label**
- Summary: "> - **Affiliation:** Independent (ally)" — `12-harug-shieldsunder.md:6`
- Relationships: "**Relationships.** Harug is a member of Renaer's Black Tears and the group's frontline fighter, paired informally with Parlek as the muscle-and-finesse pairing of the circle." — `12-harug-shieldsunder.md:25`
- No organization page for the Black Tears. The labels do not clash. The drafter keeps "Independent (ally)" and states the membership in Connections.

---

## E. Stale lines in other files (not edited), and routed references

**E1. Stale or sensitive lines**
- `campaign/gazetteer/waterdeep/north-ward.md:203` and `campaign/guides/trollskull-manor/06-tavern-time.md:84` to `:98`: the Renaer's Friends table presumes an open tavern. The tavern is closed on day one (`north-ward.md:63`: "The tavern has been closed for years, and the poltergeist **Lif** haunts it.").
- `.claude/skills/character-voices/SKILL.md:23`: lists Harug with the Black Tears. Matches.

**E2. Routed quest references (quest-time)**
- Guild inspector and cellar grate: `campaign/quests/act-i/trollskull-alley/ev-02-the-guild-gauntlet.md:40` ("### The Cellarers' and Plumbers' Guild") and `:70` ("> - **Sewer Grate Documented** — mark when the Cellarers' inspector flags the T7 grate for heritage documentation and it goes on the permit record."). The inspector is unnamed. Not Harug.
- Adventure, an unnamed Cellarers' dwarf: "Then he offended a member of the Cellarers' and Plumbers' Guild by comparing the dwarf's beard to barnacles on a ship." — `sources/adventure-wdh.json:4239`. Unnamed; not Harug.
- Guild checklist: `campaign/setting/governance-and-guilds/guilds.md:40`.
- Tavern rows: `campaign/guides/trollskull-manor/06-tavern-time.md:94` and `sources/Appendix_D_-_Running_the_Tavern.md:1140`.

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]`.

1. **Origin and early life.** No source. Stay consistent with: dwarf (wiki line 56), Dwarvish (wiki line 19), and a Waterdeep guild member (wiki line 56).
2. **How he joined the Cellarers' and Plumbers' Guild and rose to tunnel work.** Wiki: "one of the guild's best tunnel workers" (wiki line 59). No route. Stay consistent with the wiki's guild membership and the campaign's "fighter" label (D1).
3. **How he met Renaer and joined the circle.** No source. Campaign: "Harug is a member of Renaer's Black Tears" (page L25). No date.
4. **Dorn Strongcraft.** Wiki: Harug is his uncle (wiki line 62). Dorn appears in no campaign or adventure file (grep). Do not name Dorn as a day-one figure without a ruling; a mention as `[research]` is the most the drafter can use.
5. **Laraelra.** Wiki: "Harug and Laraelra Harsard were good friends." (wiki line 62). Campaign: Laraelra's page (`campaign/setting/notable-figures/independents-allies/08-laraelra-elra-harsard.md:25`) says she is "a member of Renaer's Black Tears". No campaign link between the two.
6. **"Found something worth protecting."** Campaign: "Deep down, he has found something worth protecting, and he would rather break a table than admit it." (page L21). No thing or person is named. Any answer is `[design]` (ruling 17).
7. **The Veteran stat block.** Campaign-only (summary, line 5). No wiki or adventure source. Keep as the page states it.

---

## G. Inner-life hints in the sources (exact quotes)

- **Protecting the others.** "To those he trusts, he is the one who checks that everyone got home safe." — `12-harug-shieldsunder.md:21`
- **The worth he will not admit.** "Deep down, he has found something worth protecting, and he would rather break a table than admit it." — `12-harug-shieldsunder.md:21`
- **Goal.** "Harug wants to keep the Black Tears alive through whatever Renaer drags them into, and drink in peace. He does not complicate things further." — `12-harug-shieldsunder.md:15`
- **Emotions.** "Harug most often feels protective vigilance, gruff contentment, unspoken pride, stubborn refusal to explain himself, comfortable silence, and occasional surprise at how much he enjoys these people." — `12-harug-shieldsunder.md:13`
- **Voice, pride.** "**Personality in speech:** Complex emotions come out as one word. Pride and affection show in actions, not speech. Surprised enjoyment of the group is a grunt." — `independents-allies.md:235`
- **Voice, never.** "**Never:** He never explains himself, never makes speeches, and never breaks the line." — `independents-allies.md:238`
- **Wiki, the cantankerous dwarf (guild is `[research]`).** "Harug was called "most cantankerous dwarf in the city," but was considered one of the guild's best tunnel workers." — wiki line 59
- **Wiki, the friend.** "Harug and Laraelra Harsard were good friends." — wiki line 62
