# Pass 6 research notes: Valetta

Page: `campaign/setting/notable-figures/independents-allies/07-valetta.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 19). Ruling used: Ches 1, 1492 DR is day one. Valetta is alive and at the House of Inspired Hands on Ches 1. The fireball, the bounty and the nimblewright hunt are quest time.
Organization page: none. `campaign/setting/organizations/` has no page for the House of Inspired Hands. A Grep for "Inspired Hands|Valetta|Gond" returned one line, `12-house-gralhund.md:155`, a bullet about the nimblewright's origin.
Factions Guide: none. Gond's lore page: `campaign/setting/deities/gond.md`.
Voice profile: `.claude/skills/character-voices/voices/independents-allies.md` lines 138 to 152.
Wiki: `scratchpad/wiki-independents-allies/07-valetta.txt` (full page, not a stub). Editions: WDH5e by ref name; the wiki's `class5e` cites MM5e p.348 (`MM5e-p348`).

## Method and caveats

- No shell. `sources/15. The Nimblewright Investigation.pdf` read in full with the Read tool (10 pages, printed pp.107 to 116). Valetta does not appear. The House section (printed pp.113 to 114) names only "Nim". `sources/29. Addendum Timelines  Starting the Campaign.pdf` page 1 (printed p.225) read: no Valetta.
- `voicecheck.py` was not run. No file was edited except these notes.

## Findings that change how the page is written

1. **The SOURCE_GUIDE gives Valetta a different species.** It says "Valetta the elf cleric" (`sources/SOURCE_GUIDE.md:414`). The adventure, the gazetteer and the page say bronze dragonborn. The adventure is the higher-ranked source (D1).
2. **The runaway nimblewright left before Ches 1, by derivation.** The campaign dates the flight to about Alturiak 22, 1492 DR (`history/08-the-players-arrive.md:87`). The bounty offer is a quest-time event in Fireball! ev-02.
3. **The adventure says the fireball nimblewright was one of Nim's inventions.** The Alexandrian and the campaign say it belonged to House Gralhund (D2).
4. **Most of the page's combat and bounty lines are quest time.** See section C.

---

## A. Background facts by theme

### A1. The temple, Gond and Nim (campaign, then adventure)

> "- Valetta (Neutral, Dragonborn, she/her), a bronze dragonborn priest of Gond, is the senior cleric. Nim, a nimblewright that cannot speak and signs in Common Sign Language, lives in the attic. The temple is mapped in **House of Inspired Hands**."
> — `campaign/gazetteer/waterdeep/sea-ward.md:64`

> "Valetta, the senior cleric, works by day with two junior priests and three lay initiates, and Nim, the temple's nimblewright, lives in the attic. No guards are posted, since the House is a public temple. The temple holds an annual invention competition called Gond's Artifice, and the winning entries stand on display in the main hall."
> — `campaign/setting/deities/gond.md:63` (a bullet under the temple's entry)

> "Regular hours: Valetta and two junior Gond priests circulate the main hall and workshop levels. Three lay initiates maintain the workshop spaces. Nim occupies the attic exclusively."
> — `campaign/locations/house-of-inspired-hands/area-overview.md:21`

> "The House of Inspired Hands, Waterdeep's temple of Gond, sits on the corner of Seawatch Street and Shark Street in the Sea Ward. If the characters visit the temple, they see the following:"
> — `sources/adventure-wdh.json:4565`

> "The creature atop the temple is Nim, a {@creature nimblewright|WDH} (see {@adventure appendix B|WDH|12}). Nim was given to the temple as a gift from a visiting Lantanese wizard and has been creating its own inventions on the sly. One of those inventions was the nimblewright that detonated the fireball in Trollskull Alley. Another less-dangerous invention, a mechanical sparrow, is on an accidental collision course with the party."
> — `sources/adventure-wdh.json:4573` (the fireball claim conflicts with the campaign, D2)

> "Found at the southern entrance to the House of Inspired Hands in the Sea Ward, this alley serves as the testing ground for inventions considered too dangerous to operate inside the temple. The locals are generally unconcerned about the risks, though, and stand watching while food vendors circulate among them."
> — `sources/adventure-wdh.json:31321`

> "Gondwatch Lane, at the southern entrance to the House of Inspired Hands, is the testing ground for inventions too dangerous to run inside the temple. Locals stand and watch while food vendors work the crowd."
> — `campaign/gazetteer/waterdeep/sea-ward.md:151`

> "- **Where it is used:** Gond never appears in person. His faith runs through the House of Inspired Hands, its senior cleric Valetta and the temple's nimblewright, Nim."
> — `campaign/setting/deities/gond.md:8`

### A2. Derived pre-campaign events at the temple (`[research]`)

> "Nim of the House of Inspired Hands built a second nimblewright about three months before the fireball. It fled the temple about one month before, which puts it near Alturiak 22, 1492 DR. `[research]`"
> — `campaign/setting/history/08-the-players-arrive.md:60`

> "About Alturiak 22, 1492 DR (derived): the runaway nimblewright flees the House of Inspired Hands, one month before the fireball."
> — `campaign/setting/history/08-the-players-arrive.md:87`

The Day of Wonders visit (no year in the adventure; Marpenoth 3 and 1491 are derived, `history/08-the-players-arrive.md:82`):
> "The Day of Wonders is the grandest parade of the fall season, and Jarlaxle wants the Sea Maidens Faire to be a part of it. In the guise of Zardoz Zord, he pays a visit the day before the holiday to the House of Inspired Hands, Waterdeep's temple of Gond, to coordinate with the acolytes in charge of organizing the parade. He presents a detailed plan that commingles the attractions of the Sea Maidens Faire with the bizarre inventions of the temple-a plan that is well received."
> — `sources/adventure-wdh.json:26688` (Valetta is not named in this paragraph)

### A3. Appearance, speech and character

> "The temple's senior cleric. A tall bronze dragonborn with amber-yellow eyes; machine oil smell of a woman who considers it a kind of perfume; deliberate, compact movements; the toothed cog worn as a collar clasp. Patient, methodical, protective of the temple's reputation. She was in the main hall when the sparrow was released and meets the party at the entrance."
> — `campaign/quests/act-ii/fireball/ev-02-the-house-of-inspired-hands.md:32` (the last sentence is quest time)

> "She identifies Nim from any physical description — she built the sparrow trap years ago, she says; Nim has a gift for making things that do what she tells them."
> — same file, line 34 (the sparrow trap is a quest-time device; "years ago" is her own claim)

> "The characters are met by {@creature Valetta|wdh}, a dragonborn {@creature priest} of bronze dragon ancestry, with these changes:"
> — `sources/adventure-wdh.json:4610`

> "{@creature Valetta|WDH} is neutral."
> — `sources/adventure-wdh.json:4614`

> "She has these racial traits: She can use her action to exhale a 5-foot-wide, 30-foot line of lightning (but can't do this again until she finishes a short or long rest); each creature in the line must make a {@dc 11} Dexterity saving throw, taking {@dice 2d6} lightning damage on a failed save, or half as much damage on a successful one. She has resistance to lightning damage. She speaks Common and Draconic."
> — `sources/adventure-wdh.json:4615`

Voice profile, day-one lines:
> "- **Word choice:** Artificer's vocabulary: gears, tolerances, animating principles. Gond invoked as \"the Wonderbringer\". She calls constructs \"he\" or \"she\", never \"it\"." — `.claude/skills/character-voices/voices/independents-allies.md:143`
> "- **Quirks:** She tinkers with something small while talking. She asks \"Does it work?\" before \"Is it pretty?\". She blesses finished work: \"Gond sees it.\"" — same file, line 146
> "- **Never:** She never calls a construct a tool, never haggles on principle, and never breaks a deal." — same file, line 148

### A4. Nim's keeper (wiki, Act III)

> "In [[1492 DR]],{{WDH-time}} Valetta was in charge of taking care of the [[nimblewright]] [[Nim]]." — `scratchpad/wiki-independents-allies/07-valetta.txt` line 64 (ref WDH5e-p47)

> "**Valetta** — the temple's senior cleric and unofficial liaison with the outside world — is patient, methodical, and protective of the temple's reputation." — `sources/Act_III_Arc_D.md:295`

> "Valetta has learned enough to hold basic conversations with Nim; she can translate, though she misses nuance and occasionally asks Nim to repeat itself." — `sources/Act_III_Arc_D.md:305` (the sentence before it covers the sign language; the paragraph is quest time)

---

## B. Alignment, species, pronouns, stat block

- Page summary: "> - *Bronze dragonborn priest of Gond, neutral, she/her*. Stat block: **Priest**." — `07-valetta.md:5`
- Adventure: "{@creature Valetta|WDH} is neutral." (`sources/adventure-wdh.json:4614`); "a dragonborn {@creature priest} of bronze dragon ancestry" (`:4610`)
- Pronoun "she": adventure `:4615` ("She has these racial traits"); gazetteer `sea-ward.md:64` ("she/her"); voice `:143` ("She calls constructs 'he' or 'she', never 'it'"); ev-02 `:32` ("machine oil smell of a woman").
- Wiki: "| sex            = Female" (`07-valetta.txt` line 12); "| race           = [[Bronze dragon|Bronze]] [[dragonborn]]" (line 13); "| alignment5e    = [[Neutral]]" (line 56); "| challenge5e    = 2" (line 57); "| class5e        = {{Class table|edition=5e|[[Cleric]]|5}}" (line 58); "| languages      = [[Common]], [[Draconic]]" (line 18)
- Stat block "Priest": page summary; adventure `:4610` ("a dragonborn {@creature priest}").

---

## C. Quest-time sentences on the current page and the voice profile

| # | Where | Sentence (exact) | Where it already lives |
|---|---|---|---|
| C1 | Summary L6 | "> - **Affiliation:** Independent (ally)" | Day one. No organization page names her. Keep. |
| C2 | Summary L7 | "**Featured in:** **Fireball!**, **House of Inspired Hands**" | Fireball! ev-02 (`campaign/quests/act-ii/fireball/ev-02-the-house-of-inspired-hands.md:9` to `:14`). The House is an event title. |
| C3 | Persona L21 | "To the world, Valetta is a bronze dragonborn priest who offers coin for destroying a rogue nimblewright and rewards good work with Gond-blessed inventions. To those she trusts, she will release Nim the nimblewright into the party's custody if they have proven themselves capable. Deep down, she values constructs as Gond's children, and the rogue nimblewright's violence offends her theology as much as her conscience." | "offers coin for destroying a rogue nimblewright": quest time (`ev-02-the-house-of-inspired-hands.md:70` "Valetta's Reward"; adventure `:4655`). "release Nim ... if they have proven themselves capable": quest time (`sources/adventure-wdh.json:13557`: "If the characters have befriended {@creature Valetta|wdh}, the dragonborn priest of Gond (see chapter 3), she happily releases Nim the {@creature nimblewright|wdh} into their custody until they no longer have need of it."). "the rogue nimblewright's violence": quest time. "values constructs as Gond's children": day one (voice `:141` to `:146`). |
| C4 | Morale L23 | "In a fight, Valetta would use her lightning breath weapon and priest spells to defend the House of Inspired Hands. She would rather negotiate, but the rogue nimblewright proved that constructs can kill, and she will not let that happen again." | Lightning breath: `sources/adventure-wdh.json:4615` (day one). "the rogue nimblewright proved that constructs can kill": quest time (`campaign/quests/act-ii/fireball/ev-01-the-fireball.md:8`, the fireball). |
| C5 | Relationships L25 | "Valetta is a priest of Gond at the House of Inspired Hands and the keeper of Nim, the friendly nimblewright. She offers 500 gp for the rogue nimblewright's destruction, a bounty she considers both a civic duty and a theological obligation." | First sentence: day one (`sea-ward.md:64`; `history/08:60`). Second sentence: quest time. `ev-02-the-house-of-inspired-hands.md:72` ("500 gp for proof of the escaped nimblewright's destruction, plus one invention of the party's choosing from the temple's collection."); adventure `:4655`. |
| C6 | Overview L29 | "Valetta is a bronze dragonborn priest of Gond at the House of Inspired Hands who offers a 500 gp bounty for the destruction of a rogue nimblewright and rewards competent work with practical assistance." | The bounty: quest time, as C5. The rest is day one. |
| C7 | Voice L145 (Personality) | "Absorbed and warm toward competence. She's offended by the rogue nimblewright on theological grounds, and says so. Her pride in the House shows as detailed explanations nobody asked for." | "offended by the rogue nimblewright": quest time. The rest is day one. |
| C8 | Voice L147 (Signature) | "\"Five hundred gold. Destroyed, not damaged.\"" | Quest time (the bounty). |
| C9 | Voice L150 (Greeting) | "\"You're here about the nimblewright. Good. Sit, don't touch the bench.\"" | Quest time (the party comes after the fireball, `ev-02-the-house-of-inspired-hands.md:9`). |
| C10 | Voice L151 (Business) | "\"Five hundred gold for the rogue, destroyed. Bring me the core intact and I'll bless your blades too.\"" | Quest time (the bounty, `ev-02:72`). |
| C11 | Voice L152 (Under pressure) | "\"Get back. He's faster than you think and he isn't going to stop.\"" | Quest time (the rogue, after the fireball). |

Quest-time items the page does not carry, routed:
- The bounty and the release: `campaign/quests/act-ii/fireball/ev-02-the-house-of-inspired-hands.md:70` to `:86`.
- The sparrow trap: `ev-02-the-house-of-inspired-hands.md:28` ("The moment the sparrow is released, Nim disappears through a rooftop hatch and retreats to the attic.")
- The runaway's account, through Valetta: `ev-02-the-house-of-inspired-hands.md:49` ("Through Valetta, Nim conveys: it built a second nimblewright three months ago to ease its loneliness. The creation had an incomplete behavioral lattice — it panicked and fled the temple grounds approximately one month ago.")
- The attic door and the DC 17 persuasion: `ev-02:36` to `:41`.
- Stingblade (Lords' Alliance): `campaign/guides/factions/03-lords-alliance.md:68` ("| 10 | **Stingblade** | Once per quest, Jalester arranges an introduction to one of eight named Waterdhavians: Barnibus Blastwind of the Watchful Order, Lord Torlyn Wands, Saeth Cromley, Valetta, ...") and `campaign/quests/faction-events/lords-alliance/r10-stingblade/ev-01-stingblade.md:125`.
- Nim's detector and the reward: `campaign/locations/house-of-inspired-hands/02-nims-attic.md:39` to `:41`.
- Sea Ward gazetteer hook: `campaign/gazetteer/waterdeep/sea-ward.md:65` ("Hook: in **The House of Inspired Hands** the party meets Valetta and Nim after the fireball and leaves with a nimblewright detector.").

---

## D. Conflicts

**D1. Species**
- `sources/SOURCE_GUIDE.md:414`: "- Valetta the elf cleric: temple of Gond, can perform the sending to detect a nimblewright's presence in the city (requires the tracker device)".
- Adventure `:4610`: "a dragonborn {@creature priest} of bronze dragon ancestry"; gazetteer `sea-ward.md:64`: "Valetta (Neutral, Dragonborn, she/her)"; page L5: "Bronze dragonborn".
- Alexandrian PDF 15, read in full: no Valetta line.
- Higher ranked: adventure and campaign (dragonborn). The SOURCE_GUIDE line is stale.

**D2. Whose invention the fireball nimblewright was**
- Adventure `:4573`: "One of those inventions was the nimblewright that detonated the fireball in Trollskull Alley."
- Alexandrian `sources/Act_III_Arc_D.md:37`: "The Gralhund nimblewright — a construct sold to House Gralhund by Jarlaxle Baenre's Sea Maidens Faire operation, armed with a *necklace of fireballs* by Lady Yalah Gralhund — was watching from a nearby rooftop".
- Campaign: the fireball nimblewright is the Gralhund one (`campaign/quests/act-ii/fireball/ev-01-the-fireball.md:32`, "The nimblewright threw the bead from the cooperage rooftop to the east ..."); the House's runaway is a separate creature (`ev-02:49`).
- Higher ranked: campaign (Fireball!). The adventure line is a conflict to report.

**D3. When the runaway left**
- Campaign derived: "About Alturiak 22, 1492 DR (derived): the runaway nimblewright flees the House of Inspired Hands, one month before the fireball." (`history/08:87`)
- `campaign/quests/act-ii/fireball/ev-02-the-house-of-inspired-hands.md:49`: "it panicked and fled the temple grounds approximately one month ago" (quest frame)
- `campaign/setting/history/08-the-players-arrive.md:135`: "- **Conflicts:** The runaway nimblewright. `fireball/overview.md` line 59 says it \"fled a month later\" than its building. `fireball/ev-02-the-house-of-inspired-hands.md` line 50 says it fled \"approximately one month ago\". This page follows ev-02."
- Adventure `:4378`: "that escaped from the House of Inspired Hands, the temple of Gond in the Sea Ward, a month ago."
- Higher ranked: campaign (history 08). The pre-Ches 1 flight is derived only.

**D4. Who built the runaway and when**
- Campaign: "built a second nimblewright three months ago" (`ev-02:49`); `history/08:60`: "built a second nimblewright about three months before the fireball".
- Adventure `:4573`: the fireball creature was one of Nim's inventions. `:4378`: the Gralhund assassin "escaped from the House ... a month ago".
- Higher ranked: campaign (ev-02 and history 08).

**D5. Wiki pronoun for Nim**
- Wiki line 64: "Valetta discovered that a nimblewright of Nim's own creation was involved in the attack and decided to strip Nim of all his construction materials." The wiki says "his". The campaign says "it" (`ev-02:49`, "Nim conveys: it built a second nimblewright"). Not a Valetta fact; for the drafter.

**D6. Stat block**
- Page: "Stat block: **Priest**" (L5). Wiki: "Cleric 5" (line 58). Adventure: "priest" (`:4610`). No conflict in the role.

---

## E. Stale lines in other files (not edited), and routed references

- `sources/SOURCE_GUIDE.md:414`: "Valetta the elf cleric" (D1; stale).
- `campaign/gazetteer/waterdeep/sea-ward.md:207`: "- `campaign/setting/notable-figures/`: ... Valetta (alignment, species, role and GM notes)." (a sources-list line; the page exists)
- `campaign/quests/act-ii/fireball/overview.md:35`: "- **Valetta** (House of Inspired Hands) — senior cleric of Gond; bronze dragonborn; escorts party to Nim's attic; mediates communication" (quest frame)
- `campaign/structure/arc-c-fireball.md:138`: "**Valetta's Reward. (New Content)** 500 gp for proof of the escaped nimblewright's destruction ..." (superseded structure doc; do not use)
- Not readable: none.

---

## F. Gaps a Background needs, and the sourced facts to stay consistent with

1. **Birth, age, family, origin.** No source. Wiki: "| age            = " (line 16), "| dob            = " (line 20), "| parents        = " (line 28), all blank.
2. **Her training and how she came to the House.** No source. Campaign: "senior cleric" (`sea-ward.md:64`); the House is "Waterdeep's temple of Gond" (`adventure-wdh.json:4565`).
3. **Her faith.** Gond (wiki line 17, "| patron deity   = [[Gond]]"). Voice: "Gond invoked as \"the Wonderbringer\"" (voice L143).
4. **Nim's origin.** "Nim was given to the temple as a gift from a visiting Lantanese wizard" (`adventure-wdh.json:4573`). Nim's second nimblewright: `history/08:60`.
5. **Zardoz's visit.** The adventure's Day of Wonders paragraph (A2); no year. Use "the day before the Day of Wonders" only; the year is `[research]`.
6. **Lightning breath.** Racial trait (`adventure-wdh.json:4615`).
7. **The sparrow trap she built.** Quest-time device (ev-02:34, "she built the sparrow trap years ago, she says").

---

## G. Inner-life hints in the sources (exact quotes)

- "Patient, methodical, protective of the temple's reputation." (`ev-02-the-house-of-inspired-hands.md:32`)
- "the temple's senior cleric and unofficial liaison with the outside world" (`sources/Act_III_Arc_D.md:295`)
- "She calls constructs \"he\" or \"she\", never \"it\"." (voice L143)
- "She never calls a construct a tool, never haggles on principle, and never breaks a deal." (voice L148)
- "She blesses finished work: \"Gond sees it.\"" (voice L146)
- "build constructs that serve rather than harm" (page L15, day one)
