# Pass 6 research notes: Osco Salibuck

Page: `campaign/setting/notable-figures/independents-allies/09-osco-salibuck.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 19, user rulings Session 53)
Day one: Ches 1, 1492 DR.
Organization page: none. No `campaign/setting/organizations/` page names Osco or the Black Tears. Affiliation label is on the page at line 6 (see D4).
Factions Guide: none names Osco.
Voice profile: `.claude/skills/character-voices/voices/independents-allies.md` lines 174 to 188.
Model format: `docs/plans/setting-compendium-research-notes/pass6/trollskull-community/01-talisolvanar-fellbranch.md`

## Method and caveats

- Campaign files: Grep and Read. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json` has no line naming Osco or Salibuck (grep). Undermountain (`sources/adventure-wdmm.json`): no match for Osco, Salibuck, Black Tears or Brandobaris.
- Alexandrian: `sources/Appendix_D_-_Running_the_Tavern.md` (markdown transcription). `sources/27. Addendum A Night in Trollskull Manor.pdf` PDF pages 7 and 8 (printed p.184 and p.185) read with the Read tool's `pages` parameter; the transcriptions must be checked with `pdftotext -layout`. `sources/26. Addendum Other Collaborators.pdf` (6 pages, printed 173 to 177) and `sources/2. Other Factions.pdf` (3 pages, printed 20 to 22) were read in full: no match for Osco.
- Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-independents-allies/09-osco-salibuck.txt` is a real page (not NOT FOUND). Its only citation is the novel *Blackstaff Tower* (the page links `Blackstaff Tower (novel)`, wiki line 76). Edition is not tagged. Cited as "wiki line N".
- Second wiki hit: `sources/research/pass5-bundles/force-grey/wiki.txt:100` (a different wiki page, City System citation).
- `voicecheck.py` was not run. No shell. No file was edited except this notes file.

## Findings that change how the page is written

1. **Alignment and species are campaign-assigned, not sourced.** The session log says the six Black Tears stat lines were given alignments in Session 5 (`session 5 handoff.md:73`). The wiki's alignment field is blank (wiki line 52). "Lightfoot" appears only on the campaign page. The wiki says "Halfling" (wiki line 14).
2. **The wiki gives Osco a family, a patron god and a 1479 DR meeting with Renaer.** None of these appear on the campaign page. The patron god (Brandobaris, wiki line 18) conflicts with the campaign's line that no halfling Notable Figure "gives a god" (D1). The family and the 1479 DR story have no campaign conflict (A1 to A3).
3. **Osco's only campaign placement outside the page is the Renaer's Friends table, which is tavern-time.** The table is used for nights at the party's tavern (`campaign/guides/trollskull-manor/06-tavern-time.md:5`). The tavern is closed on day one (`campaign/gazetteer/waterdeep/north-ward.md:63`). See C2.

---

## A. Background facts by theme

### A1. Origin and family (wiki, Blackstaff Tower novel, edition not tagged)

> "'''Osco Salibuck''' was a [[halfling]] [[rogue]] from [[Waterdeep]].<ref name="BST">{{Cite book/Blackstaff Tower}}</ref>"
> — `scratchpad/wiki-independents-allies/09-osco-salibuck.txt`, wiki line 56

> "Osco had chestnut-brown curly hair with sideburns. He also had silver rings in his left nostril and earlobe. He was quite young-looking in [[1479 DR]].<ref name="BST-p123-125">{{Cite book/Blackstaff Tower|123-125}}</ref>"
> — wiki line 59 (section "Description")

> "Osco was the son of [[Ellial Salibuck]] and grandson of [[Madrak]], a servant at [[Neverember Manor]].<ref name="BST-p123-125">{{Cite book/Blackstaff Tower|123-125}}</ref> He had an aunt named [[Delalar]].<ref name="BST-p157">{{Cite book/Blackstaff Tower|157}}</ref>"
> — wiki line 72 (section "Relationships")

> "He was tested by [[Blackstaff Tower]], where he met two ghosts, [[Pikar Salibuck]] and [[Osco Salibuck the Elder]] (his ancestors; Osco the Elder's ghost was actually being impersonated by the ghost of [[Khelben "Blackstaff" Arunsun]]).<ref name="BST-p208-209">{{Cite book/Blackstaff Tower|208-209}}</ref>"
> — wiki line 64

### A2. How he met Renaer and joined the group (wiki, 1479 DR)

> "In [[Nightal]] [[1479 DR]], [[Renaer Neverember]] and his companions (including [[Vajra Safahr]], soon to be the seventh [[Blackstaff]]) were lying low at [[Varadras]] when they discovered Osco had discovered the way to travel to the mansion and was trying to avoid capture by the [[City Watch (Waterdeep)|City Watch]] for posing as a member of the [[Cellarers' & Plumbers' Guild]]. Since Osco didn't know any of the [[magical]] pass phrases to open doors or return to Waterdeep, he became trapped in the mansion.<ref name="BST"/>"
> — wiki line 62

> "Osco joined Renaer's group and helped return Vajra to Waterdeep so that she could claim the title of Blackstaff. He was tested by [[Blackstaff Tower]], where he met two ghosts, [[Pikar Salibuck]] and [[Osco Salibuck the Elder]] (his ancestors; Osco the Elder's ghost was actually being impersonated by the ghost of [[Khelben "Blackstaff" Arunsun]]).<ref name="BST-p208-209">{{Cite book/Blackstaff Tower|208-209}}</ref> Osco then helped Vajra and the others to defeat [[Khondar Naomal]], who was attempting to invade the tower.<ref name="BST"/>"
> — wiki line 64 (the first two sentences are quoted again in full here so that the joining line and the ancestor line stay together)

Campaign counterpart (day one, no date): "Deep down, he joined the Black Tears because Renaer treated him like an equal without making a performance of it." — `campaign/setting/notable-figures/independents-allies/09-osco-salibuck.md:21`

Campaign counterpart for Renaer's 1479 DR rescue: "> - **Routed facts:** Renaer's 1479 DR rescue of Vajra at Blackstaff Tower (Patreon, per the findings note) belongs on **Renaer Neverember**." — `campaign/setting/history/06-the-open-lords-fall.md:164`

### A3. The later post and the group (wiki)

> "Osco later became a member of the organization formed by Renaer to replace the [[Moonstars]].<ref name="BST-p305">{{Cite book/Blackstaff Tower|305}}</ref>"
> — wiki line 66

The campaign never names the Black Tears as this organization. Renaer's page says: "Renaer is the estranged son of Dagult Neverember (former Open Lord, current Lord of Neverwinter), the devoted friend of Floon Blagmaar, the closest living friend of Meloon Wardragon (whose changed behavior has him alarmed), a man who rescued Vajra Safahr from Khondar Naomal's agents and left the Blackstaff permanently in his debt, a Harper-adjacent ally of Mirt and Remi Haventree, and the leader of the Black Tears (his personal circle of trusted companions)." — `campaign/setting/notable-figures/independents-allies/02-renaer-neverember.md:25`

On the Moonstars: "The campaign has no Moonstars page, and Khelben is dead in the campaign." — `campaign/setting/organizations/01-harpers.md:187`. The link is wiki-only (see F).

### A4. Equipment (wiki)

> "Osco wielded a [[sling]].<ref name="Blackstaff Tower">{{Cite book/Blackstaff Tower}}</ref> He also carried a dagger named "Osco's Luck"; it was a simple stone dagger with a red, cabochon-cut [[jasper]] stone in its and its name engraved in [[Common|Trade Common]] on its blade. Osco swapped this dagger for one of the keys held by Khondar while attempting to enter Blackstaff Tower.<ref name="BST-p293">{{Cite book/Blackstaff Tower|293}}</ref>"
> — wiki line 69

Campaign morale (day one): "In a fight, Osco would disappear into the shadows and strike from hiding. He fights dirty, fast, and only when running is not an option." — `campaign/setting/notable-figures/independents-allies/09-osco-salibuck.md:23`

### A5. Faith (wiki only)

> "| patron deity   = [[Brandobaris]]<ref name="Blackstaff Tower-p207">{{Cite book/Blackstaff Tower|207}}</ref>"
> — wiki line 18

See D1.

### A6. Time in post

- The only date for his joining is the wiki's 1479 DR (wiki line 64). The campaign page gives no date (line 21).
- Campaign: "Osco is a member of Renaer's Black Tears. Elra handles the threats they can see; Osco handles the ones they cannot." — `campaign/setting/notable-figures/independents-allies/09-osco-salibuck.md:25`

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Summary: "> - *Lightfoot halfling rogue, chaotic good, he/him*. Stat block: **Rogue**." — `campaign/setting/notable-figures/independents-allies/09-osco-salibuck.md:5`
- Campaign-assigned: "All six (Elra, Osco, Torlyn, Eiruk, Harug, Parlek) lacked alignment in their stat lines. Alignments assigned and committed (`c0c6bde`)." — `session 5 handoff.md:73`
- Wiki: "| alignment5e    = " (blank) — wiki line 52
- Appendix D: Osco appears only in the table row "| 11–12 | Osco Salibuck |" (`sources/Appendix_D_-_Running_the_Tavern.md:1137`). No alignment.

**Species**
- Summary: "Lightfoot halfling" (`09-osco-salibuck.md:5`). "Lightfoot" is campaign-only.
- Wiki: "| race           = [[Halfling]]" — wiki line 14. Wiki line 56: "was a [[halfling]] [[rogue]]".

**Pronouns**
- Summary: "he/him" (`09-osco-salibuck.md:5`)
- Wiki: "| sex            = Male" — wiki line 13
- Pronoun table: `docs/plans/npc-pronouns-table-group-a.md:26` ("Osco Salibuck | independents-allies/09-osco-salibuck.md:5 | he/him | from page prose, line 21")

**Stat block**
- Summary: "Stat block: **Rogue**." (`09-osco-salibuck.md:5`)
- Wiki: "| class          = [[Rogue]]" — wiki line 35. Matches.
- Campaign-assigned per the session log (see Alignment).

---

## C. Sentences on the current page that narrate a quest-time event or a day-one conflict

The page has no quest event and no Background section yet. Every sentence on the page was checked.

| Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|
| L7 | "> - **Featured in:** Background figure; no scripted appearance." | Campaign label. Not an event. | Renaer's Friends row: `campaign/guides/trollskull-manor/06-tavern-time.md:91` |
| L11 | "**Resonance.** Osco should inspire amusement with his cheerful irreverence, endearment with his fierce loyalty to friends twice his size, and respect for the skills he keeps understated." | Day one. Keep. | none needed |
| L13 | "**Emotions.** Osco most often feels mischievous good humor, restless energy, sharp protectiveness of the Black Tears, competitive glee, easygoing confidence, and brief flashes of seriousness that vanish before anyone comments." | Day one. Keep. | Renaer page L25 |
| L15 | "**Motivations.** Osco wants to keep the Black Tears out of trouble (or, failing that, keep trouble interesting), maintain his reputation as someone who can get into anywhere, and never be bored." | Day one. Keep. | none needed |
| L21 | "**Persona.** To the world, Osco is a lightfoot halfling who drinks with Renaer's crowd and laughs louder than anyone his size should. To those he trusts, he is the one who scouts ahead, picks the lock, and says nothing about what he heard on the way in. Deep down, he joined the Black Tears because Renaer treated him like an equal without making a performance of it." | Day one in form. "Renaer's crowd" names no place. The joining has no date. | See C2 (place) and A2 (1479 DR wiki story) |
| L23 | "**Morale.** In a fight, Osco would disappear into the shadows and strike from hiding. He fights dirty, fast, and only when running is not an option." | Day one. Keep. | none needed |
| L25 | "**Relationships.** Osco is a member of Renaer's Black Tears. Elra handles the threats they can see; Osco handles the ones they cannot." | Day one. Keep. | Renaer page L25 |
| L29 | "Osco Salibuck is a lightfoot halfling rogue who drinks with Renaer Neverember's crowd, keeps his skills understated, and can get in anywhere." | Day one. Keep. | As L21 |

### C2. Renaer's Friends table (routed; the tavern is the party's only after the quests)

- Campaign: "Use this four-step procedure for each significant night the characters spend at the tavern." — `campaign/guides/trollskull-manor/06-tavern-time.md:5`
- Campaign: "| 11–12 | Osco Salibuck |" under "## Renaer's Friends Table (d20)" — `campaign/guides/trollskull-manor/06-tavern-time.md:91` (heading at line 84)
- Appendix D: "| 11–12 | Osco Salibuck |" — `sources/Appendix_D_-_Running_the_Tavern.md:1137` (heading "### Renaer's Friends Table" at line 1130)
- Addendum PDF, printed p.185 (PDF page 8), transcription: "11-12 Osco Salibuck". Check with pdftotext.
- Tavern status: "The tavern has been closed for years, and the poltergeist **Lif** haunts it." — `campaign/gazetteer/waterdeep/north-ward.md:63`
- Tavern status: "A long-closed tavern, Trollskull Manor, stands at the end of Trollskull Alley among old residences and shops." — `campaign/gazetteer/waterdeep/north-ward.md:203`
- Ownership by the party: "The deed is real. **Trollskull Manor** is real, non-operational, and now the party's property." — `campaign/quests/act-i/finding-floon/ev-04-xanathar-sewer-hideout.md:100`
- Routed: the Renaer's Friends table is a tavern-time tool. It belongs with **Trollskull Alley** and the **Trollskull Manor** guide, not on this page.

### C3. Voice profile quest-time clauses (`.claude/skills/character-voices/voices/independents-allies.md`, lines 174 to 188)

- No clause in lines 177 to 187 names a quest event. Line 186 (Greeting): "*Greeting:* "Ooh, new faces! Bet you a silver I can guess which of you snores."" assumes a first meeting with the party. Not an event. Drafter's call.
- No profile change is needed for a quest-time clause.

---

## D. Conflicts

**D1. Patron god (wiki vs campaign)**
- Wiki: "| patron deity   = [[Brandobaris]]" — wiki line 18
- Campaign, `campaign/setting/deities/yondalla.md:65`: "No Notable Figure names Yondalla. The halflings among them are **Broxley Fairkettle**, **Osco Salibuck**, **Kelso Fiddlewick**, **Corene Wyldath**, **Manafret Cherryport**, **Havia Quickknife** and **Mookie Plush**, and none of their pages gives a god, so this page makes none of them a worshiper."
- Campaign: "Names with no page: Moander, Brandobaris, Erevan Ilesere, Finder Wyvernspur and Tyche are not on the roster, so they are plain text. Meloon Wardragon's quest names (**The Dragon in the Harbor**, **The Trouble with Meloon**, **Destroy the Intellect Factory**, **The Legate's Eyes**) come from his Notable Figures page and are not in the CLAUDE.md Quest Quick Reference. Only **The Trouble with Meloon** is named on this page." — `campaign/setting/deities/tymora.md:126`
- Higher ranked: the campaign. It gives no god to Osco, and no Brandobaris page exists. The wiki claim is not adopted. Do not write a god on the page unless the orchestrator rules otherwise.

**D2. Stat and class: no conflict.** Wiki class Rogue (line 35) matches the summary.

**D3. Species: no conflict.** "lightfoot" is a subrace refinement. Wiki says "Halfling".

**D4. Affiliation label**
- Summary: "> - **Affiliation:** Independent (ally)" — `09-osco-salibuck.md:6`
- Relationships: "**Relationships.** Osco is a member of Renaer's Black Tears. Elra handles the threats they can see; Osco handles the ones they cannot." — `09-osco-salibuck.md:25`
- Renaer: "and the leader of the Black Tears (his personal circle of trusted companions)." — `02-renaer-neverember.md:25`
- No organization page for the Black Tears. The labels are campaign-side and do not clash. The drafter keeps "Independent (ally)" and states the membership in Connections.

**D5. Age**: No conflict. The wiki gives only "He was quite young-looking in [[1479 DR]]." (wiki line 59).

**D6. Same name in another wiki page**
- Force Grey wiki: "* [[Osco Salibuck the Elder]], once a captive of Force Grey, Osco reformed his criminal ways and was invited to join. Although he himself wasn't particularly powerful, he commanded the loyalty of a mighty [[djinn]] servant named [[Amprantines]]. He was active in the mid–14{{th}} century DR.<ref name="CS-p6">{{Cite book/City System|6}}</ref>" — `sources/research/pass5-bundles/force-grey/wiki.txt:100`
- Different date and a different story from the Blackstaff Tower ancestor (wiki line 64). Not a campaign fact. Do not merge.

---

## E. Stale lines in other files (not edited), and routed references

**E1. Stale or sensitive lines**
- `campaign/setting/deities/yondalla.md:65` and `:105` (quoted in D1). Stays true until a god is assigned to Osco.
- `campaign/guides/trollskull-manor/06-tavern-time.md:5`, `:84`, `:91` and `sources/Appendix_D_-_Running_the_Tavern.md:1130` to `:1137`: the Renaer's Friends rows assume the party's tavern (C2).
- `campaign/gazetteer/waterdeep/north-ward.md:63` and `:203`: the tavern is closed on day one. Any text that puts a patron in the tavern on day one conflicts with these (see the Torlyn file, D1).

**E2. Routed quest references (quest-time, not on the page)**
- `campaign/quests/act-i/finding-floon/ev-04-xanathar-sewer-hideout.md:100` (the deed; Trollskull Manor "now the party's property")
- `campaign/guides/trollskull-manor/06-tavern-time.md:5` and `:91` (tavern procedure; Renaer's Friends row)
- `sources/Appendix_D_-_Running_the_Tavern.md:1112` (patron table row "| 7–8 | Renaer's Friends *(roll on Renaer's Friends table)* |") and `:1137`
- Addendum PDF, printed p.184 (PDF page 7), transcription: "I recommend that the guest list should include: Renaer and Floon, assuming the PCs have not alienated them in some way". Osco is not named. It marks the tavern premise. Check with pdftotext.

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]`.

1. **Birth, age and early life.** No source. Wiki gives only "He was quite young-looking in [[1479 DR]]." (wiki line 59). Stay consistent with: Waterdeep as the place he is from (wiki line 56), a Salibuck family in the city, and an age that is unknown on day one.
2. **Family after 1479 DR.** Wiki gives father Ellial Salibuck, grandfather Madrak (a servant at Neverember Manor) and aunt Delalar (wiki line 72). Nothing after 1479. Stay consistent with those names as the wiki gives them. Name collision: `campaign/guides/gm-guide/design-notes-running-the-campaign.md:120` lists "Madrak, Jinny (Kraddoc's scribe), Justyn Rassk — too peripheral". That is a campaign design note about a different Madrak. Do not link them.
3. **The Neverember link.** The wiki's grandfather served at Neverember Manor (wiki line 72). Renaer's page gives no servant. A Background may name the manor as the grandfather's place of service. Do not give the manor a day-one role.
4. **How he came to Renaer.** Wiki: he was caught posing as a Cellarers' & Plumbers' Guild member and trapped in the mansion (wiki line 62). Stay consistent with "He was tested by [[Blackstaff Tower]], where he met two ghosts" and "Osco joined Renaer's group" (wiki line 64), and the campaign's "because Renaer treated him like an equal" (page L21).
5. **Money and work.** No source. The campaign says only "a lightfoot halfling rogue" and "can get in anywhere" (page L29).
6. **Faith.** Wiki says Brandobaris (line 18). Campaign: no god (D1). Do not give a god without a ruling.
7. **History with Laraelra.** Campaign: "Elra handles the threats they can see; Osco handles the ones they cannot." (page L25). No source for any history between them.
8. **"Osco's Luck" and the sling.** Wiki gives both (wiki line 69). The campaign uses neither. Whether he still has them on day one is open.
9. **Ancestors in the tower.** The wiki says he met two Salibuck ghosts (wiki line 64). Keep out of the Background unless the drafter wants it as a family-pride detail `[design]`.

---

## G. Inner-life hints in the sources (exact quotes)

- **Loyalty to the group.** "Deep down, he joined the Black Tears because Renaer treated him like an equal without making a performance of it." — `09-osco-salibuck.md:21`
- **Loyalty to friends.** "Osco should inspire amusement with his cheerful irreverence, endearment with his fierce loyalty to friends twice his size, and respect for the skills he keeps understated." — `09-osco-salibuck.md:11`
- **Protectiveness.** "Osco most often feels mischievous good humor, restless energy, sharp protectiveness of the Black Tears, competitive glee, easygoing confidence, and brief flashes of seriousness that vanish before anyone comments." — `09-osco-salibuck.md:13`
- **Motivation.** "Osco wants to keep the Black Tears out of trouble (or, failing that, keep trouble interesting), maintain his reputation as someone who can get into anywhere, and never be bored." — `09-osco-salibuck.md:15`
- **Voice, under the surface.** "Good humour and restless energy. His protectiveness of the Black Tears shows as a sudden flat seriousness that's gone before anyone can comment. He's competitive about locks." — `.claude/skills/character-voices/voices/independents-allies.md:181`
- **Never.** "**Never:** He never gets bored quietly, never brags about what he's stolen, and never leaves a friend inside." — `.claude/skills/character-voices/voices/independents-allies.md:184`
- **Wiki, the boy in the mansion.** "He was quite young-looking in [[1479 DR]]." — wiki line 59. "he became trapped in the mansion." — wiki line 62.
- **Wiki, the family line.** "Osco was the son of [[Ellial Salibuck]] and grandson of [[Madrak]], a servant at [[Neverember Manor]]." — wiki line 72.
- **Wiki, the ancestors.** "He was tested by [[Blackstaff Tower]], where he met two ghosts, [[Pikar Salibuck]] and [[Osco Salibuck the Elder]] (his ancestors; Osco the Elder's ghost was actually being impersonated by the ghost of [[Khelben "Blackstaff" Arunsun]])." — wiki line 64.
