# Lords' Alliance research: 00-first-meeting, s01, s02, r03, r10, r25, r50

Scope: `00-first-meeting`, `s01-suspension-and-dismissal`, `s02-escalation-to-the-open-lord`, `r03-redknife`, `r10-stingblade`, `r25-warduke`, `r50-lioncrown`. No campaign file was edited. Report 02 of 5.

**Model reading done.** Read in full (events and design notes unless noted):
- Doom Raiders: `doom-raiders/m03-the-missing-snobeedle/` (overview :1-75, ev-01 :1-540, design-notes :1-23) and `doom-raiders/r03-wolf/` (ev-01 :1-257, design-notes :1-17).
- Bregan D'aerthe: `bregan-daerthe/m02-the-wazoo-affair/` (overview :1-73, ev-01 :1-400, design-notes :1-40).
- Emerald Enclave (newest model, matching scope): `emerald-enclave/00-first-meeting/` (ev-01 :1-328, design-notes :1-24), `emerald-enclave/r03-summerstrider/` (ev-01 :1-239, design-notes :1-20), `emerald-enclave/s01-a-seat-at-phaulkonmere/` (ev-01 :1-197, design-notes), `emerald-enclave/s02-the-water-table-stirs/` (ev-01 :1-140 read closely, remainder skimmed; it is the multi-trigger model, not needed for the single-trigger LA s02), `emerald-enclave/r50-master-of-the-wild/` (ev-01 :1-412, design-notes :1-27).
- Force Grey: `force-grey/00-first-meeting/` (ev-01 :1-289, design-notes :1-28), `force-grey/s01-the-full-picture/` (ev-01 :1-291, design-notes :1-23), `force-grey/r50-force-grey-commander/` (ev-01 :1-414, design-notes :1-29).
- Harpers: `harpers/00-first-meeting/` (ev-01 :1-354, design-notes :1-23) and `harpers/r50-high-harper/` (ev-01 :1-438 with the Masked Lord section :325-408 read closely, design-notes :1-21).
- Also read: `docs/plans/emerald-enclave-research/02-first-meeting-s01-s02-ranks.md` (the model report, :1-390), `docs/plans/lords-alliance-research/00-research-brief.md`, `session 42 handoff.md` and `session 43 handoff.md` (Rules and Instructions), the LA lines of `docs/plans/harpers-out-of-scope-notes.md`, `campaign/quests/faction-events/lords-alliance/m01-m06` overviews (gates, outcomes, readers), the Illuun/Jalester links in `harpers/m06-the-stones-other-master` and `emerald-enclave/m06-the-dreamers-reach`, and every cross-file reader of the LA outcomes (section 6).

**Abbreviations**
- `R` = first-commit versions, `/tmp/claude-0/-home-user-waterdeep/f91bf122-6992-582e-a45c-3f8e22918b72/scratchpad/la-orig/lords-alliance/` (one `ev-01-*.md` per folder, no design-notes).
- `PREV` = `/home/user/waterdeep/campaign/quests/faction-events/lords-alliance/` (R plus the retired-sidebar retrofit and a trim pass). Line numbers are PREV's unless marked R. R and PREV differ only in the lines listed in section 2.
- `FG`, `DR`, `BD`, `H`, `EE` = `/home/user/waterdeep/campaign/quests/faction-events/{force-grey,doom-raiders,bregan-daerthe,harpers,emerald-enclave}/`.
- `G03` = `campaign/guides/factions/03-lords-alliance.md`; `G01` = `campaign/guides/factions/01-overview.md`; `PG` = `campaign/guides/players-guide/faction-affiliations.md`; `GMO` = `campaign/guides/gm-guide/player-factions-overview.md`; `ORG` = `campaign/setting/organizations/02-lords-alliance.md`; `NF-J` = `campaign/setting/notable-figures/lords-alliance/01-jalester-silvermane.md`; `NF-L` = `.../city-officials/01-laeral-silverhand.md`; `VOICE` = `.claude/skills/character-voices/voices/lords-alliance.md` and `city-officials.md`; `AB` = `sources/Appendix_B_-_Player_Factions.md`; `WDH` / `WDMM` = `sources/adventure-wdh.json` / `adventure-wdmm.json` (cited by JSON path); `OOS` = `docs/plans/harpers-out-of-scope-notes.md`; `XMM` = `.../scratchpad/5e/bestiary-xmm.json` (queried with `python3 -I` this session).

---

## 1. What the model pages require (copy these)

**First Meeting (H, FG, EE, DR).**
- Summary with a bullet list of what the characters can do, then `#### Candidates and Companions` and `#### What Is Actually True` inside the Summary block (H FM :14-24; FG FM :13-25; EE FM :13-25). Every character who belongs to no other faction is a candidate and answers for themselves; companions listen and gain nothing; if no candidate accepts, the Event ends with no membership outcome (EE FM :15-17; FG FM :14-17).
- Scenes in `###` sections. Each NPC scene has a `[!readaloud]`, a `[!social]` line `Name (Alignment, Species, pronouns) :: summary`, a "happy to discuss" list, a "will not discuss" line, and `[!qna]` blocks (EE FM :90-151; FG FM :72-185). A GM block answers the three forbidden topics (Stone, vault, Manshoon) in one fixed written line (EE FM :145-151; FG FM :180-185).
- `### Each Candidate's Answer`: `Recording the Answers`, an accept readaloud, a decline/defer readaloud, a "late return is recorded the same way" line, and a `... Benefits` box listing each benefit per member (EE FM :210-244; H FM :278-306; FG FM :187-226). Renown 1 and the rank name are stated there.
- Party-level help (the renovation money) is a separate box, given once, because the manor is shared (EE FM :269-276; FG FM :228-236).
- Close: `Event Outcomes` marked per name, `Next Steps` ending "This Event awards no Milestone Points", then `## Overview` and `## Summary` with "After the Meeting" and "Without a Private Meeting" variants (EE FM :296-328; H FM :330-354). No first mission is handed over; it arrives later by its own contact (EE FM :280; H FM design notes).
- The contact object is described once in full, in the First Meeting, and later events point back to it (EE FM :27-49; EE design notes :337).

**Rank events (DR r03, EE r03, EE r50, FG r50, H r50).**
- Trigger text: "when an individual X member first reaches Renown N". The contact object arrives at noon the next day; a member away from Waterdeep meets it at their first surface lodging and the meeting moves a day (DR r03 :5, :11-20; EE r03 :13-15). Several members who cross together attend together and are recorded one by one.
- `What Is Actually True` block (DR r03 :22-24; EE r03 :29-37).
- Every benefit is a per-member procedure with contact, place, notice, limit, who else, loss rule and renown-loss rule (DR r03 :114-126, :160-170, :210-218; EE r03 :91-102, :149-159, :175-193; EE r50 :219-232, :276-288; FG r50 :124-143). Companions use what the member gets but cannot ask for anything.
- Renown loss: the rank stays, the benefits are suspended until Renown is restored (EE r03 :79-81, :102, :159; FG r50 :143).
- `### Renown Opportunities`: "The rank event awards no Renown" (DR r03 :230-232; EE r03 :211-213).
- `### Aftermath` states which parts stay with the member and what to record per member (EE r03 :215-217; FG r50 :386-390).
- Outcome per recipient name, read by the next rank event; the "also reads" paragraph lists outcomes the Event reads (EE r03 :219-231; DR r03 :238-249). Next Steps ends "This Event awards no Renown and no Milestone Points".
- Fixed tables, not "the GM selects": the web (DR r03 :114-150), the network (EE r03 :175-193), the scroll vault (FG r50 :169-198).
- r50: hold until the prior rank outcome is marked and the member is on the surface (FG r50 :14-28; EE r50 :16); CR 2.0 ally tables with "fighting allies = PCs minus one" (FG r50 :124-143; EE r50 :227-245); a one-line-facts `Mad Mage Seeds` block (FG r50 :370-380; EE r50 :368-379); a decision recorded by name (FG r50 :329-368; EE r50 :292-356).

**Standalone event (FG s01, EE s01).** Members-only (FG s01 :5, :13); a test with three routes per element, judged on the facts, no check (FG s01 :48-81); an incomplete account earns exactly one question and a return visit (FG s01 :70-81); a 2-Renown award "once in the campaign" (FG s01 :261-263); a late sitting adds a name and pays the same (FG s01 :265-271); a `Vajra Briefed`-style writer outcome read by named later events (FG s01 :273-283); EE s01 shows the per-member personal-token pattern (key never lent, no refuge from a lawful warrant, loss rule; EE s01 :100-115).

**Mission pages used only as shape models.** DR m03 and BD m02 both open with `Who Knows What` (DR m03 :16-18; BD m02 :16-27), keep the briefing members-only (DR m03 :14, :22; BD m02 :14), mark a named outcome at every branch, and close with `Mission Renown` bullets of `+1 Renown:` plus a conditional (DR m03 :499-505; BD m02 :364-370). Jarlaxle's persona is voiced from the profile and nobody says "Jarlaxle" before the gate (BD m02 design notes :98).

**Folder shape.** Each model folder has `ev-01-<slug>.md` plus a `design-notes.md` (sections: what changed, departures from the source, invented names and open items; e.g. EE FM design notes :331-352, DR r03 design notes :260-273). None of the seven LA folders in scope has a design-notes file.

---

## 2. R and PREV: what each folder contains (facts)

R is the original draft with `> **[GM]**`, `**Background (DM only)**`, `[!design]`, `[!lore]`, `[!info]`, `[!warning]`, `#### X: True / False` and a separate `## Read Aloud` section. PREV changes: it adds `[!npc-narrative]` and `[!dialogue]` blocks to the First Meeting, adds `[!narrative]` openers to the Read Aloud sections, and trims about twenty sentences. It has no `What Is Actually True`, no candidate frame, no per-member procedures, no design notes, no contact object.

### 2a. 00-first-meeting
- **R / PREV (:1-108).** Fires "when the **Factions Come Calling** Event reaches the Lords' Alliance row" (PREV :7). Jalester finds the party "at the Yawning Portal if they are regular presences there, at Trollskull Manor if they rarely venture out" (:9, :26; AB :204). He cites the Candle Lane warehouse without prompting (:10, :28). Pitch: the Alliance works "off-duty, off-record" and provides "Watch access, safe houses, direct lines to authority" (:34). Four questions: who he reports to (Laeral), what the Alliance wants, what it pays, what the first assignment looks like (PREV :38-48; R :35). The Condition: "Assignments from us are not optional. If that changes your answer, now is the time to say so." He waits three seconds, then leaves (:54-56; AB :228). If pressed he explains once and "will not move on the condition" (:62-69). Declining: "Jalester does not approach them again" (:71-73). Outcome `#### Lords' Alliance Joined: True / False`, "True if at least one party member accepted ... and enrolled" (:77-79). Next Steps: M1 for 2nd-level characters, delivered in person (:85); if False, "Jalester does not follow up" and the Alliance is an "uncertain variable" at the Vault (:87).
- **R-only lines that PREV trimmed.** R :17 "He was not at the warehouse — the Watch's formal investigation was already two hours behind"; R :19 "the Alliance has lost operatives ... Two went dark on operations they judged low priority. One did not survive the gap"; R :51 "One of those gaps cost a contact's life"; R :53 "He has taken two assignments back to Laeral in his career. Both times it mattered"; R :69 "becomes available once any enrolled character reaches 2nd level ... within the tenday". These are the richest character facts in the folder.
- **Holes (both versions).**
  1. Nobody answers. The Condition is the last beat, Jalester leaves (PREV :54-56), and the Event then says "the party accepts or declines" (PREV :9-13 in the Summary list, :75-79). There is no accept scene, no enrolment mechanic, no Cloak rank and no benefits box. `Lords' Alliance Joined` is party-level ("at least one party member", :79).
  2. The Cloak rank (Renown 1) and its benefit are never delivered. G03 :55 gives "Watch officers treat the character as a trusted civilian informant and overlook minor legal infractions once per tenday"; AB :252 matches.
  3. The 200 gp civic grant that `ev-04-the-factions-come-calling.md:56` and `campaign/guides/trollskull-manor/02-operating-costs.md:81` promise is not delivered (FG and EE deliver their renovation help in the First Meeting for the same reason; FG FM design notes :309-310).
  4. "Jalester does not return to recruit a second time" (R :11 / PREV :13) is the opposite of every finished First Meeting, where a deferred candidate returns to an open door and is recorded under the same outcome (EE FM :236, :312; H FM :336; FG FM :258).
  5. The invitation row in ev-04 (:26) gives the Alliance eligibility as "City residents; civic-minded track record". No file in `act-i/finding-floon/` writes a "civic-minded" outcome.
- **PREV npc-narrative / dialogue / narrative blocks (:23-24, :38-48, :68-69, :95-104) are retired formats.**

### 2b. s01-suspension-and-dismissal
- **R / PREV (:1-161).** Fires "when a Lords' Alliance member refuses or fails a mission explicitly assigned by Jalester Silvermane without compelling reason" (PREV :7). Jalester delivers it in person at Trollskull Manor "at a time he calculates the rest of the party is unlikely to be present" (:37). Compelling reason: a consistent moral or practical position the character has maintained (assassination, betrayal of a named ally, an illegal act visibly objected to); not qualifying: danger, disagreement with politics, other quests, abandonment after acceptance (:21-25; G01 :11). Suspension covers Watch escorts, safe house access, introductions, legal coverage, Watch file access, intelligence briefings, the attaché (:29, :66-75). Renown "cannot drop below 0", "A suspended character keeps their current score and retains their rank title on paper, but cannot earn new Renown and cannot access any rank benefits" (:33, :79, :82-83). Speech: "You're suspended from active operations ... I'm not touching [your Renown]. ... I had you down as reliable." (:41-55); one extra sentence on **DC 13 Charisma (Persuasion)**, "I don't enjoy this. That's not the point." (:57-62; R :57 phrases the check differently). Reinstatement: "verified intelligence on a villain faction operation: a specific address, a confirmed operative identity, or a planned action the Watch can act on within a tenday" from "firsthand observation or a documented source" (:87-93). Dismissal: a second refusal while suspended, or "a serious offense" (betrays a mission, harms Alliance members, works against the Alliance), which "bypass[es] suspension" (:95-105); Jalester "knocks once", sets a folded termination note on the nearest surface, "This is done. Your Renown stays on the books. It doesn't do anything." / "I was wrong about you." (:105-113). Dismissal is permanent (:117-118). Outcomes `LA Suspended`, `LA Reinstated`, `LA Dismissed`, all True / False (:122-132).
- **Holes.**
  1. Nothing fires it. No LA mission (R or PREV, m01-m06) contains a refusal branch, a deadline or a hand-off to s01 (grep of m01-m06 for suspen / dismiss / compelling / refus returns no hit). The line "The mission you were assigned is past its window" (:41) refers to a window no mission states.
  2. "Fails" collides with G01's "A clean failure forfeits the award but costs nothing" (G01 :25; the Failure paragraph is G01 :23; PG :26 and AB :193 say "refusing or failing"). WDH says "Refusing to accept or complete" (WDH `data/3/entries/4/entries/8/entries/1/entries/1`).
  3. The suspension list omits Laeral's private audience, the Masked Lord request (both Warduke) and the outstanding-charge removal (Lioncrown). It lists the Renown 10, 25 and 50 benefits by Renown number (:73-75) rather than by what they are.
  4. "Renown is never reduced by suspension or dismissal" (:14, :33, :79) conflicts with the player-facing "Losing Renown. Serious offenses cost 2 Renown each: betraying a mission, harming faction members, or working against the faction's interests" (PG :25; GMO :25). A "serious offense" is the same three acts in s01 (:101).
  5. A suspended character "cannot earn new Renown" (:83), but the reinstatement path is delivering intelligence, which the Alliance otherwise pays +1 (G03 :44). The Event does not say whether the reinstating delivery earns it.
  6. Readers named in the file (`every subsequent Lords' Alliance Faction Mission brief`, `Vault of Dragons`) read nothing: no mission and no structure doc reads `LA Suspended`, `LA Reinstated` or `LA Dismissed` by name (grep of `campaign/` and `docs/plans/`: none outside this folder).
  7. Scene staging: Jalester waits until "the rest of the party is unlikely to be present" (:37). A table cannot run a scene the other players are absent from unless the GM sets it up.
  8. Dismissal "bypasses" suspension for harm to members, but no event defines "harms Alliance members" (the Alliance has no named members besides Jalester and Laeral).

### 2c. s02-escalation-to-the-open-lord
- **R / PREV (:1-131).** "Fires when a Lords' Alliance member presents Jalester Silvermane with intelligence meeting the escalation threshold" (:7). Threshold (all three): the Stone's current location or holder; "The vault is in Waterdeep" (evidence beyond rumor: "the Stone's own revelation, Fentree's Ledger (Mission 5), or other documented confirmation"); at least two confirmed villain factions, where Cassalanter suspicion does not count (:25-33). +2 Renown to "the character who delivered the briefing", once in the campaign (:12, :35-36, :59). Jalester at his "usual position at a table near the far wall" of the Yawning Portal (:40). Readaloud "Sit there a minute." (:44-57). DC 12 Wisdom (Insight) reveals he knows Laeral's answer but will not say (:61). Three clarifying questions: who has the Stone, how many Eyes are active, which factions have been seen "at the vault district or at a location connected to it" (:63-73). Next morning a runner brings a two-line note signed "J.S." (:75-83). `[!lore]` "What Changes After This" (:85-88). Outcome `LA Grand Game Escalated: True / False`, read in Faction Outposts, Cassalanter Villa, Sea Maidens Faire, Kolat Towers, Vault of Dragons (:92-94). Next Steps: M6 "requires Renown 10, 7th level, and Mission 5 completion (or its alternate trigger)" (:100-102).
- **Holes.**
  1. The second element ("correct Laeral's Neverwinter assumption") overlaps M5. If M5's ledger reached Jalester, "Laeral's intelligence corrected" (`m05-fentrees-ledger/overview.md:30`; `m05/ev-01:103`), so the briefing cannot "correct" anything. If M5 has not run, the party's "documented confirmation" is undefined (the Stone reveals the location only at three Eyes: `arc-e-faction-outposts.md:51, :63`; `arc-f-xanathars-lair.md:264, :274`). The Gralhund texts (`act-ii/gralhund-villa/ev-03-daytime-infiltration.md:64`, `ev-05-the-guest-suite.md:45`) already tell the party the Stone "holds the location of a hidden vault beneath Waterdeep".
  2. The test is a paragraph, not a table with three routes per element (FG s01 :48-81 is the model).
  3. "Mission 6 requiring Renown 10" (:13, :100) uses R's gate; the brief's gate is Renown 13 and 7th level.
  4. "The character who delivered the briefing" (one character) vs the party of members (FG s01 pays every present member once).
  5. Order of events: s02 is "available from early Act III" (:15) while the Illuun link runs through Jalester at the well (section 7); everything the party tells Jalester here "has potentially reached Illuun's network" (`m06-an-audience-with-the-open-lord/ev-01:96`).
  6. The Read Aloud (:108-127) duplicates the Briefing readaloud (:44-57).

### 2d. r03-redknife (:1-63)
Fires "at the first natural pause — Jalester's next visit, or within a tenday" after Renown 3 (:7). Promotion line "You're a Redknife. That means a few things change." (:21). Benefits: **Watch Escort** "Two guards, one errand per tenday. Give me a day's notice — written, through the usual drop" (:29); **Safe Houses** a folded paper with two addresses (Castle Ward and Trades Ward), keys with the building manager, phrase "Alliance weather", "Don't bring anyone inside who hasn't been vetted" (:31-33); **String-Pulling** "Minor charges. A Watch report that could be quietly revisited. Once per tenday" (:35-37). Outcome `Redknife Reached: True / False`, read by Stingblade (:47-49). R :27 has "with the specificity of a man who has filed this particular paperwork himself" (PREV :27 trimmed).

### 2e. r10-stingblade (:1-81)
Fires after Renown 10 (:7). "Stingblade. The rank used to mean something more martial than it does now." (:19). **Introductions** one per quest, "tell me who and tell me why", arranged "before your next operation" (:27-33); **Legal Coverage** "bail, fines, and damages — one incident per quest", "The incident must be genuine" (:35-37); **Watch Files** "Standard cases take an hour ... Classified cases ... four hours and a conversation with the file officer ... DC 12", a failed check is flagged and retried after a tenday (:39-53); a volunteered detail: the files include partial informant identifications (:55-61). Outcome `Stingblade Reached` (:65-67).

### 2f. r25-warduke (:1-84)
Fires after Renown 25 (:7). Jalester sends a note the day before, "be at the Yawning Portal at the ninth bell" (:22). **Laeral Silverhand** is present near the wall "in a traveling cloak with no visible escort" (:22). Jalester gives three benefits: **Response Team** four Veterans, one operation per quest, "I authorize them personally" (:30-32); **Intelligence on Faction Response Teams** a folded map grid, "Updated every three days ... If the positions haven't updated in four days, assume something changed" (:34-36); **The Masked Lord** "once per quest, if you submit a written request through me ... that Lord will use their authority to open a door, seal an investigation, or apply political pressure. ... No attribution." (:38-44). Laeral says four sentences: "Private audiences. One per quest." / "I'm not doing this to make you feel important." / "Good work." (:48-58). Background: "This is her first direct contact with the character unless the **Escalation to the Open Lord** event has already fired" (:10; GM text :16). The Masked Lord is "predecided by the campaign but their identity is never revealed" (:18). Outcome `Warduke Reached` (:68-70).

### 2g. r50-lioncrown (:1-181)
Fires after Renown 50 "at the first natural pause" (:7). Laeral chairs in a working annex at Piergeiron's Palace; the outstanding charge removed (or held in reserve); the character asks three questions, Laeral answers honestly; Sevel Dastar (Spy) offered as attaché who "reports what [he] observe[s]. To Jalester."; a private request about two missing handlers and a cartography team (:5-13, :29, :31-43, :45-148). `[!design]` "Expected During Dungeon of the Mad Mage" branches on whether **Vault of Dragons** has resolved (:15-21). Scene headings `Act 1 ... Act 6` (:45-122). Honest answers in GM text (:33-41), among them "How diminished are you really?" — "Less than my enemies assume. More than my staff knows." (:36). Outcomes `Lioncrown Reached` and `Undermountain Commission Accepted: True / False` (:152-158). Next Steps: confirm the commission "in the session record" (:164-166).
- **Holes.** The call to attend arrives as "a formal note ... wax-sealed vellum, in Jalester's handwriting ... two days before" (:47), which cannot reach a member below ground. The hold rule (on the surface) is absent. The attaché's Spy block has no ally rules. "Act 5" (:37) is mis-numbered; the request is Act 6.

---

## 3. Contact object, who recruits, where, and the members-only frame

### 3a. Facts
- **Recruiter and place.** Jalester recruits; Laeral is "reachable only through Jalester" (ORG :7, :23). WDH: Jalester "spends a lot of time here [the Yawning Portal], usually seated by himself in a quiet corner. Durnan knows that Jalester works for Laeral and leaves the young man alone" (WDH `data/1/entries/12/entries/5/entries/5/entries/1`). AB: "Jalester Silvermane finds the party himself — at the Yawning Portal, where he spends much of his time, or at Trollskull Manor if the party rarely ventures out" (AB :204); corner table, an untouched tankard, "He watches the door" (AB :210); the handshake is "firm and brief", a City Watch badge on his belt (AB :213-214). Harper M6 and EE M6 both place him "beside the Yawning Portal's well" (`harpers/m06-the-stones-other-master/ev-01-the-stones-other-master.md:18`; `emerald-enclave/m06-the-dreamers-reach/overview.md:30`).
- **Delivery.** In person at the First Meeting and M1 (PREV 00:26; `m01-the-long-watch/ev-01-the-tenday-watch.md:22-24`). Other contact objects in R/PREV, each different: a Watch-sealed note (M2 overview), "plain-paper courier in a more formal style" (M5 overview), summons "on formal vellum" via two Watch officers in dress uniform (M6 ev-01:125), a note "the day before" (r25 :22), a runner with a folded note (s02 :77), wax-sealed vellum "in Jalester's handwriting" (r50 :47). The "usual drop" / "Alliance drop" (r03 :29; r25 :36) is never located. There is no canonical description.
- **Eligibility.** WDH: a Waterdavian citizen; "Those with criminal records can also join, provided they demonstrate their allegiance" (`data/1/entries/11/entries/9/entries/0`); the faction-mission chapter says "Potential recruits must be residents of Waterdeep" (`data/3/entries/4/entries/8/entries/0`). ev-04 gives "City residents; civic-minded track record" (:26). AB :183 "Waterdeep residents and who place the security of the city ahead of personal gain".
- **Members-only frame in R/PREV.** The Summary calls it a party Event ("the party accepts or declines", PREV :13); the outcome is party-level (PREV :79). Every rank event is individual in its trigger (PREV r03 :7) but carries no per-member counter, no "companions get nothing" line and no loss rule.
- **"Not optional" is source-backed.** WDH: "A character who belongs to a faction other than the Lords' Alliance can turn down a mission without consequence" (`data/3/entries/4/entries/1`); AB :193 "the only faction that will formally suspend or dismiss"; GMO :26.
- **Jalester's description conflicts.** AB :213 "a lean man, thinning dark hair", AB :210 "middle-aged"; NF-J :22 "lean, thinning-haired" ; WDH `data/12/entries/17/entries/0` "An earnest man in his mid-twenties" and WDMM `data/0/entries/5/entries/2/entries/3/entries/1` "a young captain of the City Watch". NF-J stat block **Spy**; WDH LG Chondathan fighter; `08-notable-patrons.md:107` N Veteran. The voices doc and R follow NF-J.
- **Tally.** Not relevant here (he is Enclave).

### 3b. Recommendations
1. **Candidates (decision 1).** Use the H/FG/EE rule: every character who belongs to no other faction is a candidate and answers for themselves. Use the ev-04 "civic-minded" line only to decide whom Jalester addresses first, as H FM does with its Good-aligned trigger ("nobody is tested for alignment at the door", H FM :16) and EE FM :15. Nobody is tested for residence at the table; all PCs own a manor in Waterdeep by then.
2. **Placement, deterministic (zero-prep).** Jalester waits at his corner table by the Portal's well at dusk on the day the Alliance row fires; the candidate who reaches the Portal first is addressed first and the others may come. If no candidate has reached the Portal by dusk of the second day he comes to Trollskull Manor's taproom on the third morning and sits at a table for a morning. A deferred candidate finds him at the same table any evening (WDH `data/1/entries/12/entries/5/entries/5/entries/1`: "usually seated by himself"). This replaces R's "if they are regular presences" (a judgment).
3. **Offer handling.** Replace "Jalester does not return to recruit" with the open-table rule: no second pitch, the offer stands at the Portal table, a late acceptance is recorded under the same outcome with the name. This keeps his character beat (he will not chase) and matches EE/H/FG.
4. **Answer scene.** After the Condition (kept verbatim, with the three-second wait), Jalester asks each candidate for their answer. This closes the hole in 2a-1. The accept readaloud gives the rank name Cloak and Renown 1; the decline readaloud has him "thank them for their time" (PREV :73) and leave.
5. **Canonical contact object (one description, reused).** Recommended text for the drafter, built from the R/PREV usages in 3a:
   - **The runner.** A City Watch runner in a plain tabard (Commoner, 2024 XMM) carries a letter folded in thirds and sealed with a thumbprint of grey wax, the member's name on the outside in Jalester's small, precise script. Formality rises with rank: Cloak and Redknife spoken or on plain paper; Stingblade sealed; Warduke a numbered time and place; Lioncrown wax-sealed vellum from the Palace chancery (R/PREV r50 :47). The runner hands it to the named member only and waits for no reply.
   - **The drop.** Fix it at the Yawning Portal: Durnan holds letters left for "Silvermane's friends" in a ledger behind the bar. WDH has Durnan already know Jalester's role (WDH `data/1/entries/12/entries/5/entries/5/entries/1`). One line in the First Meeting names it; later events say "the drop at the Portal". Alternatives: the Castle Ward Watch station message desk (rejected: the Alliance's value is off-record), a stationer (invents a new NPC).
   - **GM-only:** The runner and the drop are Jalester's; if Jalester is removed (Harper M6 / LA M6 "The Jalester Question") the drop passes to whoever replaces him (decision 10).
6. **Suspension/dismissal staging.** Because other players sit at the table, add one GM line: Jalester finds the member alone at the manor "when the others are out" or, if every member is present, the scene is run at the table as a private conversation after the GM asks the others to listen without speaking. State this as procedure.
7. **`What Is Actually True` content (zero-prep).** Jalester picked these candidates because the Watch put them at the warehouse (his own "since the warehouse", AB :215); Laeral did not tell him to; the Alliance's condition is real because it has lost operatives (R :19); he reports to Laeral and she does not know the candidates by name; nobody at the table, Jalester included, knows what a future audience will ask. Jalester is loyal and honest and will not know that anything he is told at the well may reach Illuun (section 7).
8. **Renovation help (party-level, once).** The 200 gp grant "up to 200 gp from Laeral's discretionary fund ... Ongoing compliance oversight — Jalester checks in" (`02-operating-costs.md:81`; ev-04 :56 "No repayment; civic goodwill expected"). Deliver it as a party-level box in the First Meeting, given once when the first candidate accepts. The "compliance oversight" becomes a rule: Jalester sits at a Trollskull table once in the first tenday after the grant. The manor-guide Fellowship-line reduction (`02-operating-costs.md:27`) is passive ("active standing required"), needs no event, and goes in the log (rule: passive benefits need no delivering event, session 43 handoff, "it's just a passive thing").
9. **Cloak Benefits box.** Per member: Renown 1; the token (decision 2); how the Watch recognizes it; the once-per-tenday overlook (G03 :55). Resolve the overlap with Redknife's string-pulling by wording: Cloak is an officer's discretion before a charge is written (on the spot, no paperwork); Redknife's string-pull revises or removes a charge or report after it is written (via Jalester, in writing). State the Cloak "minor infraction" list in one line (brawling without grievous injury, unlicensed weapon, trespass without theft, breach of the peace). Loss rule: a Watch citation entered against the member resets the tenday count; the rank stays if Renown falls (model).

---

## 4. What each rank grants: R, PREV, guide, Appendix B, WDH

### 4a. Side-by-side

| Rank | R / PREV event | G03 table (:55-59) | AB (:252-256) | WDH |
|---|---|---|---|---|
| R1 Cloak | none delivered | Watch treat as trusted civilian informant; overlook minor infractions once per tenday | same | "City Watch officials are notified that the characters are on 'official business' ... instructed to provide support" (`data/1/entries/11/entries/9/entries/5`); a "brief audience with Laeral" |
| R3 Redknife | 2 Guards, 1 errand/tenday, 24 h notice; 2 safe houses; 1 string-pull/tenday | same, plus Watch patrol schedules "for any ward, once per tenday ... (Renown 3+)" (G03 :12) | escort + safe houses only | "A character who has at least 4 renown in the Lords' Alliance can arrange a meeting with Laeral" (`data/5/entries/11/entries/4/entries/2/items/1`); 3 renown lends a Persuasion edge at trial (`data/5/entries/11/entries/4/entries/2/items/4/entries/2/items/0`) |
| R10 Stingblade | 1 intro/quest; legal cover 1 incident/quest; Watch files (standard 1 h, classified 4 h + DC 12) | same | intro + legal "once per arc" only | at Renown 4 or higher Jalester "offers to join the party" in Xanathar's lair (`data/6/entries/7/entries/3/entries/3/entries/2`) |
| R25 Warduke | 1 Laeral audience/quest; 4 Veterans 1 operation/quest; response-team intel every 3 days; 1 Masked Lord request/quest | same; "all four villain faction response teams" | audience + veterans only | none |
| R50 Lioncrown | charge dropped; 3 honest answers; attaché Sevel; Undermountain request | same | charge + attaché only; G03 adds the three answers | none |

- G03 :53-59, PG :63-66 and GMO :67-71 all say "per quest"; AB says "per arc". Rewrite follows the remix word.
- PG/GMO Warduke row says "major faction response teams" (PG :65) and "all four villain faction" (G03 :58). Which four is not defined: villain factions are Xanathar, the Splinter, the Cassalanters and Bregan D'aerthe, but G03 names no list.
- The rank events nowhere deliver the Watch patrol schedules that G03 :12 and :27, `arc-e-faction-outposts.md:83`, `arc-f-xanathars-lair.md:33` and `arc-i-kolat-towers.md:35` all depend on. G03 :12 gives the threshold "Renown 3+".
- AB's Warduke "veterans" is the 2014 stat name; the 2024 name is **Warrior Veteran** (see 4b).

### 4b. Rules checked against XMM
- **Guard** CR 1/8, AC 16, 11 HP. **Warrior Veteran** CR 3, AC 17, 65 HP (G03 :56 and :58, AB and PG say "Guards" and "Veterans"; the second is not a 2024 name). **Spy** CR 1, AC 12, 27 HP (Sevel; NF-J). **Archmage** CR 12 (NF-L). **Commoner** CR 0 (the runner). **Knight** CR 3, **Guard Captain** CR 4, **Noble** CR 1/8, **Scout** CR 1/2 also exist.
- No spell is named in the seven files; no *wish*. (grep of the seven folders for `wish` returned nothing.)
- **Mad Mage limits** (WDMM alterations, quoted in the EE report :263 and in FG r50 :370-380): no teleportation, *plane shift*, *astral projection*, *word of recall*; *Sending* works except aimed at Halaster. Nothing in the LA rank benefits depends on magic, so the only effects are who can reach a member below ground (section 9).

### 4c. Ally Power for Warduke and Lioncrown (derived from `docs/plans/emerald-enclave-mechanics-reference.md`: the monster Power table under "Method and conventions" and the Party Power table in its section 1)
- Party Power by level: L6 35, L7 41, L8 44, per PC.
- Warrior Veteran, Tier 2 Power 30 (Tier 3: 25). Rule borrowed from FG r50 :124-143 and EE r50 :227-245: allies who fight number one fewer than the PCs; the rest hold the rear.
  - 3 PCs: 2 Veterans add 60; at L7 Party Power 123 -> 183. 4 PCs: 3 add 90; 164 -> 254. 5 PCs: 4 add 120; 205 -> 325. (L6: 165 / 230 / 295. L8: 192 / 266 / 340.)
  - A Warrior Veteran (30) is below 2x a 6th-8th-level PC (35-44), so the High-Power Warning does not apply.
  - From level 11 Veteran Power is 25 (50 / 75 / 100 for 3 / 4 / 5 PCs).
- Sevel as an ally (Spy CR 1): Tier 2 17, Tier 3 15. One ally; add it only while he fights (EE reference rule 2).
- Redknife Guards (CR 1/8) are escort, not fighters. BD m03 (`bregan-daerthe/m03-three-nights/ev-01-three-nights.md:226`) already treats them as non-combatants.
- These totals are mine from the reference and are not re-audited here; the mechanics reference (report 05 / later) owns the audit.

### 4d. Procedures the rank events must write (zero-prep, from the model)

**Redknife (r03).**
- *Watch Escort.* Contact: the drop at the Portal, in writing, 24 hours' notice (R/PREV r03 :29). The errand: one "dangerous errand", surface Waterdeep only, up to one day, no Undermountain (the Guards are Watch officers who cannot leave their duty). The two Guards (XMM **Guard**) do not fight unless attacked and do not count as combatants (BD m03 :226 rule). Limit: one per member per tenday counted from that member's own last request. Loss rule: using them for a crime ends it for a tenday; a Watch officer is never ordered to break the law (R :29 "Don't use them for anything the Watch itself couldn't do officially").
- *Safe Houses.* Two fixed addresses (Castle Ward, Trades Ward). The drafter fixes street, key-holder name (the building manager), phrase "Alliance weather" (R :33), who may enter (member plus vetted guests, a number), duration, notice, and a loss rule (bringing in a pursuer, fighting, or "cleaning up a scene" loses it for a tenday: R :33). The Trades Ward address must not sit on the same block as Kolat Towers or Phaulkonmere (WDH `data/1/entries/3/entries/7/entries/0`, `data/12/entries/20/entries/3`; Manshoon gate).
- *String-Pulling.* One per member per tenday; what it covers (a minor charge or a Watch report, G03 :56); what it does not (anything above "minor"; Jalester says "come to me before you go to the desk sergeant", R :37); how to ask (the drop, a day to resolve). Write the Cloak/Redknife split from 3b-9.
- *Patrol schedules.* One ward's current patrol schedule per tenday, free, on request at the drop (G03 :12). Fixed contents are not needed: the schedule is "the Watch's three daily windows" (`arc-f-xanathars-lair.md:33`).

**Stingblade (r10).**
- *Introductions.* One per quest, requested in advance; a fixed table (no "the GM chooses"). Existing Notable Figures pages cover only officials and nobles: Magistrate Barnibus Blastwind (`city-officials/02`), Jelenn Urmbrusk (`city-officials/04`), Lord Torlyn Wands (`independents-allies/10`). There is no page for a guild factor, merchant-class principal or a "Lords' ally", so either the table stays at these three plus a few invented guild names (flag as invented) or the benefit says "a named NPC who has a Notable Figures page" (decision 6).
- *Legal Coverage.* One incident per quest; "genuine" (not a business debt); no cover for crimes against the Alliance; payment by the Alliance's solicitor.
- *Watch Files.* The R rule is fine; add who the file officer is (name or "the file officer" with a fixed description), what a standard case returns, and the retry rule. Classified files that reference the Splinter say "the Splinter" (Manshoon gate); files on the Cassalanters hold only dismissed inquiries (Cassalanter secrecy).

**Warduke (r25).**
- *Laeral audience.* One per quest, arranged through Jalester; define a "consultation" versus M6 (R :62-64) and list what she will not do (no quest, no Stone). Fix a delay (3 days). Laeral's four sentences are kept (R :48-58).
- *Four Warrior Veterans.* One operation per quest; notice (three days); the place (surface Waterdeep or the Portal); the 4 Veterans are named or unnamed (decision 7); "fighting allies = PCs minus one"; "do not ask them to do anything that would end their careers" (R :32) becomes a loss rule; the Veterans refuse to attack the Watch, a Lord or a surrendered creature (FG r50 :143 precedent).
- *Response-team intelligence.* Replace "all four villain faction response teams" with a fixed ladder like DR r03 :114-150: for each of Xanathar's Guild, the Splinter, the Cassalanters and "the carnival fleet", the next team the party has not beaten (names from `guides/factions/09-xanathars-guild.md`, `10-manshoons-zhentarim.md`, `11-cassalanters.md` and `08-bregan-daerthe.md`, Response Teams sections). Gates: the Splinter team is "the Splinter's next crew" until **Manshoon Named**; the Cassalanter team is written without imps or devils (Seffia's team has "1 invisible Imp"; Willifort's has a "Bearded Devil" or Cult Fanatics, `guides/factions/11-cassalanters.md` Response Teams) — "the family's household crew" (Cassalanter secrecy); the fourth faction is "the carnival fleet" until **Jarlaxle Unmasked** (the FG rule, FG s01 :20, :64). The "four days stale" tell (R :36) is the cadence rule.
- *Masked Lord request.* One per quest. Differentiate from Mirt's: H r50 :357-378 already gives the Harpers a request with forms (Watch cooperation, Lords' Court hearing, warrant of immunity), a three-day delivery and three refusals. The LA form is "open a door, seal an investigation, apply political pressure" (G03 :58). Fix the three forms, the three-day delivery and the refusals. Identity: "predecided by the campaign" is a zero-prep violation; the Lord is a named GM-only fact (decision 8); it must not be Mirt (the Harpers' Masked Lord is revealed at H r50 :325-343).

**Lioncrown (r50).**
- *Outstanding charge.* One; the charge removed at the ceremony or held for the next one that accrues within a tenday (R :72); define what counts (arrest warrant, Watch citation, civil damages claim, wanted status; G03 :59). Interaction with H r50 warrant of immunity and FG r50 recognition: different forms; no conflict.
- *Three honest answers.* The set-up GM text (:31-41) is zero-prep-hostile because it lists Q&A "common lines"; replace it with a table of what Laeral knows about each topic and the exact refusal line for the rest. Laeral never admits her decline (VOICE city-officials :17 "Never"; NF-L :22, :24); PREV r50 :36 breaks it (section 7).
- *Attaché Sevel Dastar.* Statline (Spy, XMM), what he does for the member, what he reports and to whom, the withdraw HP, the notice, the loss rule (e.g. he leaves if ordered to harm the Watch). He reports to Jalester; see the Illuun link (section 7).
- *Political backing.* "Unconditional" (R :120). Define in one box: what Lioncrown changes (officials Friendly, Watch cooperation, a Lords' audience on request) or cut the term.

### 4e. Recommended scene lists

**00-first-meeting.** `# Lords' Alliance First Meeting`; Summary (members-only list; Candidates and Companions; What Is Actually True); `### The Corner Table` (placement; the well; the contact object); `### The Offer` (Jalester social block; qna: who do you report to, what does the Alliance want, what does it pay, what is the first job, can we keep other loyalties, what if we think an assignment is wrong; GM line for Stone/vault/Manshoon; a short pitch readaloud); `### The Condition` (verbatim, three seconds); `### Each Candidate's Answer` (Recording, accept, decline/defer, Cloak Benefits); `### The Civic Grant` (party-level box); `### Leaving the Table`; Concluding with outcomes; Overview; Summary with "After the Meeting" and "Without a Private Meeting".

**s01.** Summary (members-only; fires per member); `What Is Actually True`; `### The Window` (the trigger list, one writer line); `### Compelling Reason` (the table, with a decision line per example); `### The Knock` (suspension scene, speech lines kept); `### Suspended Status` (list by benefit name); `### The Reinstatement Path` (three routes per element, FG s01 style); `### Dismissal` (two routes); `### Staging the Scene`; Concluding; Overview; Summary.

**s02.** Summary (members-only); `What Is Actually True`; `### Asking for Jalester` (the Portal table; no summons needed); `### What Counts as the Briefing` (a table with three routes per element, FG s01 :48-64 style); `### When an Element Is Missing` (one question); `### The Briefing`; `### The Clarifying Questions`; `### The Morning Note`; `### Renown Opportunities`; Aftermath; Concluding; Overview; Summary.

**r03/r10/r25/r50.** Summary (trigger, benefits); `### The Runner at Noon` (contact object); `What Is Actually True`; `### Naming the Rank`; one `[!exploration]` box per benefit; `### Renown Opportunities` ("awards no Renown"); `### Aftermath`; Concluding with the outcome and the "reads" paragraph; Overview; Summary. r50 adds `Mad Mage Seeds`.

---

## 5. Standalone events: suspension, dismissal and the s02 shape

### 5a. s01 recommendations
1. **Trigger.** Fires per member when one of these is true and no other reading holds:
   - the member refused a mission Jalester assigned in person (the brief of M1-M6 says so);
   - the member accepted a mission and abandoned it, defined as: the stated window (below) lapsed with no step taken;
   - the member took a step that betrays the mission (a serious offense).
   A mission the member failed honestly (the target escaped, the roll failed, the party was beaten) is not a trigger. This follows G01 :25 ("A clean failure forfeits the award but costs nothing") and removes the "fails" ambiguity. The mission pages (reports 03 and 04) must carry the window: recommend "ten days from the briefing" on every mission hook, with the tenday as the unit.
2. **Compelling reason.** Keep the R test (R/PREV :21-25) as a table of examples with the verdict, to remove the judgment (zero-prep): "the mission asks for an assassination and the member has refused an assassination on screen" = compelling; "the mission is dangerous" = not. Add one rule: only a position the table remembers from play counts, not one asserted after the refusal.
3. **Other factions' members.** Not subject (WDH `data/3/entries/4/entries/1`). Say so in one line, since FM must say it too.
4. **Renown.** Resolve the 2-point rule (decision 4): recommended wording is "Suspension costs no Renown. A serious offense costs the general 2 Renown and then dismissal makes the score inert", or simply "dismissal costs no further Renown." Pick one and mirror it in G01 :11 and PG :25.
5. **Reinstatement.** Three routes per element, as FG s01 :48-64: the intelligence must give a place, a name or a plan and a date; routes are (a) firsthand (the member observed it), (b) a document or prisoner, (c) a named informant. It earns no Renown while suspended and the Alliance pays the +1 once reinstated for the same intel if it was never reported (decision 4 sub-point). It cannot be the same intelligence as a previous reinstatement.
6. **Dismissal.** Permanent; a dismissed member belongs to no faction for the First Meeting rule (decision 5). Define "harms Alliance members" as harming Jalester, a Watch runner or officer carrying Alliance orders, or a named Alliance ally; GM line, not a list of imaginary members.
7. **Readers.** After this Event, every LA mission brief, every rank event and s02 checks the three outcomes; the Vault reads **LA Dismissed** to set Laeral's attitude (PREV :132). Current readers outside the folder that test "Renown 3 or higher" (BD m03 :226; DR s01 ev-01:239; FG m05 ev-02:228) should check these outcomes too.

### 5b. s02 shape (options)
- **A. Keep R's single tripartite test.** Cheapest; the vault element is vague.
- **B. Rebuild as a table with three routes per element (recommended).** Elements and routes:

  | Element | The account must give | Route 1 | Route 2 | Route 3 |
  |---|---|---|---|---|
  | The Stone | Where it is and who holds it now (a name or a place, current to the last tenday) | The party holds it and can say where it sleeps | A faction holder is named with a source | The member watched it change hands or be moved in the last tenday |
  | The vault | That it lies beneath Waterdeep, with evidence beyond rumor | The Fentree ledger (if **M5** is run) | Gralhund/Stone-attunement testimony: the Stone "holds the location of a hidden vault beneath Waterdeep" and cannot give it without Eyes (`arc-e-faction-outposts.md:51`; Gralhund ev-03 :64, ev-05 :45) | Neverember-household or lair papers naming the sum or the place |
  | Two villain factions | For each of two, what it wants from the vault and one thing it has done | Ran an outpost chain or a lair heist against it | Holds a document, prisoner or ledger from it | A named contact or captured agent described its plan |

  The Cassalanters count only on these routes, not on suspicion (R :33). BD is "the carnival fleet" until **Jarlaxle Unmasked**.
- **C. Fold s02 into M5/M6.** Rejected: s02 exists as a "party's own initiative" counterweight to the assigned missions.
- **Interaction with M5.** If **M5**'s ledger reached Jalester, the vault element is already satisfied and Laeral already knows (m05 overview :30). Give s02 two readaloud branches: ledger delivered (Jalester says "She has the ledger. Tell me the rest.") and not.
- **Renown.** +2 to every member present when Jalester seals the note, once per member (G03 :45; AB; FG s01 :261-263), not "the character who delivered it" (R/PREV :12). A member who missed the sitting repeats the account later and earns the same (FG s01 :265-271).
- **Timing.** Remove "early Act III onward" (PREV :15). The trigger is the three elements, not the calendar; since the Stone is in the party's hands after **Gralhund Villa**, the earliest realistic sitting is after **Faction Outposts** (two factions observed) but the table can run it whenever the test passes.
- **M6 gate.** Next Steps states M6 gates as Renown 13 and 7th level (brief); s02 does not unlock M6 and does not change **LA M6**'s alternate trigger.

---

## 6. Outcomes: what each event reads and writes

### 6a. Inventory in R/PREV for this scope

| Outcome (R/PREV) | Writer | Readers (as stated) | Real readers found |
|---|---|---|---|
| **Lords' Alliance Joined** (party) | 00-first-meeting :77; also ev-04 :100 | every LA mission, s01 | ev-04 :27, G03 cross-refs; none in missions (no mission checks it) |
| **LA Suspended** | s01 :122 | "every subsequent mission brief", the Reinstatement Path | none |
| **LA Reinstated** | s01 :126 | missions | none |
| **LA Dismissed** | s01 :130 | Vault of Dragons | none (`arc-j` reads none) |
| **LA Grand Game Escalated** | s02 :92 | Faction Outposts, Cassalanter Villa, Sea Maidens Faire, Kolat Towers, Vault | none (`arc-e..j` read none) |
| **Redknife Reached** | r03 :47 | r10 | r10 header only |
| **Stingblade Reached** | r10 :65 | r25 | r25 header only |
| **Warduke Reached** | r25 :68 | r50 | r50 header only |
| **Lioncrown Reached** | r50 :152 | "Vault of Dragons if it has not yet resolved", Mad Mage | none |
| **Undermountain Commission Accepted** | r50 :156 | Mad Mage events | none yet; EE renamed its own (**Illuun Watch Accepted**, EE r50 :398), OotG has **Undermountain Mandate Accepted** (`order-of-the-gauntlet/r50-righteous-hand/ev-01-righteous-hand.md:134`) |

Cross-file readers keyed on the rank by Renown, not by outcome:
- `bregan-daerthe/m03-three-nights/ev-01-three-nights.md:226`: a member at "Renown 3 or higher (Redknife)" brings a Guard patrol at round five.
- `doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:162, :239`: an LA member of Renown 3 or higher asks Jalester for a courtesy note to Dunfell; succeeds without a check.
- `bregan-daerthe/s04-contact-severed/ev-01-contact-severed.md:155-157, :231`: needs the party to have met Jalester at the LA First Meeting; sells to him; writes **BD Watchers Sold**.
- `force-grey/m05-the-legates-eyes/ev-02-the-extraction.md:228-236`: passes Guild names to Jalester; no Renown.
- `act-ii/gralhund-villa/ev-01-what-the-factions-say.md:91`: **Jalester Brief Received** (old True / False).
- `act-i/trollskull-alley/ev-04-the-factions-come-calling.md:26, :56, :100`: invitation row, civic grant, the party-level True / False heading.

### 6b. Recommended outcomes and readers

Rule: one writer per outcome, marked with the member's name, with a named reader (brief, "Event Outcomes").

| Outcome | Writer | Reader | Note |
|---|---|---|---|
| **Lords' Alliance Joined** | 00-first-meeting, per name | G03; ev-04 (cut its heading); every LA event; **Contact Severed** (BD) if it keeps an LA reading; DR/BD events that test an LA member | per-character; late acceptance same outcome |
| **LA Suspended** | s01, per name | every LA mission brief and rank event (they skip the member); s01 itself | keep the R name |
| **LA Reinstated** | s01, per name | same; clears **LA Suspended** | |
| **LA Dismissed** | s01, per name | Vault of Dragons (Laeral's attitude); Mad Mage; FM (candidate rule) | permanent |
| **LA Grand Game Escalated** | s02, per name | Faction Outposts, lair heists, Vault of Dragons (unconverted; see log); LA M6 and r25 (new reads) | |
| **Redknife Reached** | r03, per name | r10; the Watch-escort, safe-house, string-pull and patrol-schedule procedures; BD m03 and DR s01 | track per member: last escort date, last string-pull date, last schedule date |
| **Stingblade Reached** | r10, per name | r25; the intro, legal and file procedures | track the intro used per quest, the legal use per quest, the last classified-file attempt |
| **Warduke Reached** | r25, per name | r50; the Veterans, intel, Masked Lord procedures | track Veterans used per quest, the audience used per quest, the Masked Lord request used per quest |
| **Lioncrown Reached** | r50, per name | Mad Mage events | |
| **Undermountain Commission Accepted** | r50, per name | Mad Mage events | keep the R name; the collision is gone (EE now writes **Illuun Watch Accepted**) |

What the Events should read:
- s01 reads **LA Suspended** / **LA Reinstated** / **LA Dismissed** (its own state).
- s02 reads **M5**'s ledger outcome (report 04 names it) for the vault element; **Manshoon Named** and **Jarlaxle Unmasked** for the wording.
- r25 reads the **M6** audience outcome (report 04 names it) for Laeral's first lines; **Manshoon Named**; **Jarlaxle Unmasked**; **LA Grand Game Escalated** only if M6 has not run.
- r50 reads **Warduke Reached** (hold) and the M6 audience outcome and the Harper **Jalester Compromise Identified** (section 7); it does not read the Vault's resolution (section 9).

---

## 7. Secrecy gates

- **Manshoon.** The R/PREV files in scope name Manshoon and Kolat Towers only in GM text: s02 :23 ("Xanathar's Guild and Manshoon's Zhentarim"), :33. No speech names him. Keep it that way: until **Manshoon Named** is marked for the listener, Jalester and Laeral say "the Splinter" or "the other cell". Risks: the Warduke intel lists the Splinter's teams; the Stingblade classified files may hold Splinter material; the safe-house addresses (Trades Ward, 4d) must not point at the neighbouring towers; OOS :23-29 and :131 already log the LA M2/M3/M6 hits (not this scope). G03 :42, :47, :67 name Manshoon in the rank/mission text (logged in OOS :131).
- **Cassalanters.** s02 R/PREV :23, :33 gets it right: "Nobody in the room knows what those things are." Keep the "unconfirmed, credible" line. The Warduke intelligence must not name imps or devils (guide 11 team rosters); r50 honest answers must not reveal the pact. Jalester's M4 Holmbridge dossier (G03 :14, :28) is mission content.
- **Jarlaxle / Bregan D'aerthe.** Jalester's R/PREV lines never say Jarlaxle. Keep it: the fourth faction is "the carnival fleet" until **Jarlaxle Unmasked** (FG s01 :20, :64; BD m02 design notes :98 for the BD side). Jarlaxle's goal is Luskan's admission to the Lords' Alliance (WDH `data/8/entries/1`; G03 :29), a fact the Alliance can know as an open bid; Jarlaxle is hidden only until he is unmasked. A BD-member PC cannot be an LA candidate (one faction).
- **Illuun and Jalester.** The Harper and Enclave events establish that Illuun listens through Jalester "beside the Yawning Portal's well", that he does not know and is loyal (H M6 ev-01:18; EE M6 overview:30), that **LA M6** treats it as "The Jalester Question" and may remove him from duty (`m06/ev-01:90-100`), and that `arc-j-vault-of-dragons.md:43, :45` has Jalester escort the party at Renown 10+. Consequences for this scope:
  - The First Meeting and s02 are held at the well. Add a GM-only line to both: anything said at the well may reach Illuun; Jalester does not know.
  - Everything a member tells Jalester in s02 (the Stone's holder) is the information at stake in M6. s02 should not be gated on the compromise; it is the ordinary honest briefing.
  - If the party tells Laeral (M6 option) and she removes Jalester from active duty, every benefit routed "through Jalester" (r03 string-pull, r10 intros, r25 Veterans/intel/Masked Lord/audiences, r50 attaché reports) breaks. Decision 10: name a successor contact or a fallback ("the Alliance clerk at the drop", a named deputy) in the rank events.
- **Laeral's decline.** NF-L :22, :24 and VOICE city-officials :17 ("She never admits her power is diminished") against R/PREV r50 :36 ("Less than my enemies assume. More than my staff knows."). FG r50 :376 and EE r50 :379 treat the wane as a GM-only seed ("No line in this Event says so").
- **Laeral's profanity.** Never in office (VOICE); Jalester stingy, plain, clipped; one raw "fuck" only if Faerrel is used against him (VOICE lords-alliance :11). Sevel has no profile and may swear lightly.
- **Faerrel.** Jalester never talks about Faerrel unless asked twice (VOICE :15). The rank events must not raise him.

---

## 8. Contradictions (R, PREV, guide, org/NF, sources, other quests)

1. **Nobody answers at the First Meeting** (2a-1): the Condition is followed by "He leaves"; the enrolment is undefined.
2. **Party-level outcome** `Lords' Alliance Joined` (PREV 00:79; ev-04 :100) vs the per-character rule.
3. **Open table.** R/PREV 00:73 "does not approach them again" vs EE/H/FG open doors.
4. **Cloak never delivered** (2a-2); the guide and AB list it.
5. **Civic grant** (200 gp) never delivered (2a-3); ev-04 :56 and `02-operating-costs.md:81`.
6. **Patrol schedules** (G03 :12) never delivered (4a).
7. **Gates.** R/PREV s02 :13, :100 say M6 at Renown 10, 7th level; m02-m06 overviews use R gates (m02 R2/L3, m03 R4/L4, m04 R6/L5, m05 R8/L6, m06 R10/L7). The brief's ladder is M2 R3/L3, M3 R5/L4, M4 R8/L5, M5 R10/L6, M6 R13/L7.
8. **r25 "first direct contact".** PREV r25 :10 says the Warduke meeting is Laeral's "first direct contact with the character unless the **Escalation to the Open Lord** event has already fired", but s02 :12 and :83 say Laeral is not present and "does not make direct contact"; the direct contact is **M6** (Renown 13, 7th level), which almost every party reaches before Renown 25 (base Renown through M6 is 1 + 2 + 2 + 3 + 3 + 4 + 4 = 19, plus bonuses).
9. **r25 vs M6 on Laeral.** r25 :62-64 distinguishes the audience from M6 but tells Laeral to confirm it "in person" as a new thing.
10. **Masked Lord identity.** r25 :18 "predecided ... never revealed" vs Mirt's reveal at H r50 :325-343. The LA Lord must not be Mirt.
11. **Lioncrown "the twelve"** (r50 :35): no source gives a number of Masked Lords (WDH has none; `waterdeep-lore.md:25` "anonymous governing council").
12. **Lioncrown "Mission 5"** (r50 :38): "She did not know the vault existed until the intelligence that set Mission 5 in motion". G03 :9 and ORG :17 say she believes it is in Neverwinter, a different statement from "did not know it existed". Lioncrown happens after the Vault in most tables.
13. **r50 hold and branch.** R/PREV r50 :15-21 branches on **Vault of Dragons** resolution. Renown 50 cannot be reached before the Vault in a normal run (calibration "approximately Renown 30-35 by the late heist quests", G01 :9; H r50 design notes "needs about thirty-one more ... The rank is meant for that book"). Branch on the M6 audience outcome and on the Harper compromise instead (section 9).
14. **Summons to a member below ground** (r50 :47) vs Mad Mage magic limits.
15. **Names of Warrior Veteran.** G03 :58, AB :255, PG :65: "Veterans". 2024 XMM name is Warrior Veteran.
16. **"Per arc" vs "per quest"** AB :253-255 vs G03 :56-58; the rewrite uses "per quest".
17. **Jalester's stat and age.** NF-J Spy, thinning hair; manor guide `08-notable-patrons.md:107` Veteran and "N male"; WDH mid-twenties, LG fighter; WDMM "young captain of the City Watch". Faerrel's death: ORG :8 "killed in a street fight a year ago"; NF-J :22 "died exposing a plot against the government"; WDH `data/12/entries/17/entries/1` both.
18. **Laeral's profile vs r50.** Section 7.
19. **Loss of Renown.** s01 :14, :33, :79 vs PG :25, GMO :25 (serious offenses cost 2 Renown).
20. **"Fails" a mission.** s01 :7 vs G01 :25.
21. **Reinstatement vs earning.** s01 :83 vs G03 :44.
22. **Suspension list incomplete** (2b-3).
23. **Warduke Masked Lord** also appears as the M6 "Masked Lord's Writ" (`m06/ev-01`, `overview.md:40`); the two are distinct but undistinguished in the guide (G03 :70 vs :58).
24. **R-only vs PREV-only lines** (2a): R is richer; PREV trimmed.
25. **Retired formats** in all seven files (section 10).
26. **"Act 1 ... Act 6"** headings (r50 :45-122) and the "Act 5" reference (r50 :37) use the mini-arc mission headings the page model drops; Acts in this campaign are I-IV.
27. **Dismissal in WDH** is "loss of membership and the loss of all renown" (`data/3/entries/4/entries/8/entries/1/entries/1`); remix says inert (G01 :11). Remix decision, not an error.

---

## 9. r50 and the Dungeon of the Mad Mage set-up (WDMM integration seeds)

**Facts from WDMM** (`sources/adventure-wdmm.json`):
- **Lords' Alliance already appears in the book.** "Retrieve a Runestone Fragment" (prerequisite 12th level; `data/0/entries/5/entries/2/entries/3`): Volo introduces "a young captain of the City Watch named Jalester Silvermane"; "Unbeknownst to anyone but her closest confidants, Laeral's magic has begun to wane"; Laeral sends Jalester to hire adventurers for a pebble-sized fragment of the Runestone that Halaster created; it is on level 20; the reward is Jalester's friendship or a *luck blade* that belongs to Mirt. Delivering a fragment to Jalester completes the quest (`data/20/entries/3/entries/15/entries/4/entries/3`, `data/20/entries/4/entries/9/entries/2`).
- **Eye of the Spider** (`data/0/entries/5/entries/2/entries/2`): the dwarf Lords' Alliance spy **Joroth Brighthelm** visits the Yawning Portal and asks the party to find the emerald stolen by Falkir's Fist (level 10); "Characters who belong to the Lords' Alliance gain 3 renown ... for returning the Eye of the Spider to Joroth."
- Halaster's fingerprints and the movement limits are the same as in FG r50 :370-380 and EE r50 :368-379 (teleportation/*plane shift*/*astral projection*/*word of recall* fail; *Sending* except at Halaster).
- The user's own note (docx "The Waterdavian's Guide to Waterdeep NPCs", line 156): "Returned the gold and saved the day? ... Laeral Silverhand wants you to find out what her old pal Halaster is up to". This is the origin of the R/PREV Lioncrown request.

**Facts from R/PREV r50.** The request is two Alliance handlers and a cartography team, dark for six tendays, "I don't know if Halaster has them or if they're dead" (PREV r50 :43, :128). The commission is a card with two names, two code phrases and a symbol (PREV r50 :134). Accepting makes "the missing agents ... a thread the character is expected to follow" (PREV :142). The handlers and the cartographers have no names, no last known level, and no connection to WDMM's own cast.

**Recommendations.**
1. **Fire when the member surfaces.** Hold until **Warduke Reached** is marked and the member is above ground, the FG/EE rule (FG r50 :14-16; EE r50 :16). Replace the wax-sealed vellum call by a runner who brings it to the Portal's drop on the first morning the member is on the surface; a member below ground cannot be summoned (no magic is used). This avoids reaching into Undermountain.
2. **Branch on M6 and the Harper compromise, not the Vault.** Laeral's opening line varies on whether **M6** ran and what the party told her (report 04 supplies the outcome names). Do not read the Vault's resolution; Lioncrown at Renown 50 is a Mad Mage event. If **Jalester Compromise Identified** is marked for a member present, Jalester is on leave and Sevel reports to the named successor (decision 10); say so in one line.
3. **Name the missing agents.** Zero-prep: give the two handlers and the cartography team names, last-known level and a code phrase (all invented; flag). Mad Mage level assignments: the cartographers were mapping the upper levels (Levels 1-3); the handlers went to Skullport (Level 3) per the Xanathar link (`arc-f-xanathars-lair.md`, the beholder's tunnels). The fixed facts the Event must supply are the level where each was last seen, what was last reported, and the code phrase that proves a find is genuine. WDMM has no Alliance NPCs in these places (WDMM "Alterations to Magic" and the level keys), so the commission's hooks are invented but compatible.
4. **Seeds block (one-line facts, FG r50 :370-380 style).** Candidates from WDMM: Jalester hires 12th-level adventurers for the Runestone fragment, level 20 (do not duplicate if the Runestone hook is used elsewhere; FG r50 :376-380 already records it); Joroth Brighthelm and the Eye of the Spider, +3 Renown for LA members returning it to Joroth (level 10); Halaster-Laeral history; the movement limits. Decision 9: whether the Runestone is part of the Lioncrown request or stays a GM seed.
5. **Do not duplicate other r50 seeds.** FG r50 and EE r50 both point to "Lioncrown carries Laeral's private request about missing agents" (FG r50 :38, :380; EE r50 design notes :17). LA owns it.
6. **No Sending analogue.** The Alliance has no *Sending*; Laeral does not cast one. Contact is the runner and the drop at the Portal only.
7. **Name of the commission outcome.** Keep **Undermountain Commission Accepted** (R :156). The brief calls it "stale"; the real staleness is the True/False form and the collision, which EE removed by renaming. Near-parallel Mad Mage outcomes: EE **Illuun Watch Accepted**, OotG **Undermountain Mandate Accepted**, BD/others TBD. Recommend keeping the LA name; it is distinct from both.
8. **Sevel Dastar.** Keep the name (no collision: grep of `campaign/` finds it only in r50). Spy block. He is a weak ally at Renown 50 (CR 1 at levels 8-12), so make him a courier/coordinator by default with "fights only to defend, withdraws at 13 Hit Points"; Ally Power 17 at Tier 2, 15 at Tier 3 only while he fights.
9. **Laeral's answers.** Write a fixed table of what she knows: the Masked Lords (she names none), the Vault (what she did), Halaster (she and Halaster were "friends" once: the user note says "old pal"; R :37 says he was "Waterdeep's greatest threat before the Spellplague"), Neverember (the gold's legal status). Keep her answers free of her own decline.

---

## 10. Standing-rule hits

- **Retired formats.** R in scope uses `> **[GM]**` (00:3, :81; s01:3, :134; s02:3, :96; r03:3, :51; r10:3, :69; r25:3, :72; r50:3, :82, :160), `**Background (DM only)**` / `**Background (GM only)**` (00:15; s01:17; s02:17; r25:14; r50:23), `[!design]` (00:58; r50:15), `[!lore]` (s02:85; r25:62), `[!info]` (s01:82; s02:35; r10:49), `[!warning]` (s01:117), `#### ...: True / False` (00:77; s01:122-130; s02:92; r03:47; r10:65; r25:68; r50:152, :156), a separate `## Read Aloud` section (00:93; s01:146; s02:108; r50:172). PREV also has `[!npc-narrative]` (00:23), `[!dialogue]` (00:38-48, :68; s01:59), `[!narrative]` (00:95; s01:148; s02:44, :110; r50:53, :174). The new pages use `[!gamemaster]`, `[!readaloud]`, `[!social]`, `[!qna]`, `[!exploration]` only.
- **Members-only.** Briefs and debriefs fire only for LA members. s01 is per-member by nature. s02 and the rank events are individual. The FM is per candidate. Companions wait at the Portal table and gain nothing; the Events say so.
- **Renown calibration.** s02 +2 matches G03 :45 and AB. Rank events award no Renown. Missions are in reports 03 and 04. The ladder: M1 joining/L2, M2 R3/L3, M3 R5/L4, M4 R8/L5, M5 R10/L6, M6 R13/L7.
- **Renown ladder wins.** No R/PREV event in scope changes rank; titles come only from the r-events. Keep.
- **Event Outcomes** (6b). Per name, one writer, a named reader.
- **No Milestone Points.** Not in R/PREV scope except s02/r50's "Next Steps". New pages end "This Event awards no Milestone Points". (Mission pages use `Milestone: None` — reports 03/04.)
- **Wish.** None present. No spell is named in the seven files; LA benefits are not spells.
- **Intellect devourer.** None in scope.
- **2024 rules.** "Veterans" -> **Warrior Veteran**; **Guard**, **Spy**, **Commoner** match XMM; the *Archmage* label for Laeral matches NF-L. "Constitution (Persuasion)"-style notation: R writes **DC 13 Charisma (Persuasion)**, **DC 12 Charisma (Persuasion)** and **DC 12 Wisdom (Insight)**, all in 2024 form.
- **Quests, not arcs.** r50 :37 "Act 5" and the Act headings (8-26). R/PREV already say "quest" in benefits (r10 :29, :35).
- **Bregan D'aerthe rejects Lolth.** Not touched.
- **Zero-prep.** The R/PREV files have judgment phrases: "if they are regular presences" (00:9), "a moment that is not conspicuously private" (R 00:23), "whatever it is" (r50 R :65), "Remove whatever charge ... would benefit most from removal" (r50 :27), "a Lord ... predecided by the campaign" (r25 :18), and the freeform three-question block (r50 :31-41, :82-96). Each needs a written rule (section 4d).
- **Jarlaxle hidden identity, Two Zhentarims.** Section 7.
- **Profanity.** Jalester stingy and plain; Laeral clean in office; Sevel uncharted, may swear lightly.
- **Rhythm.** Jalester and Laeral speak in full formal sentences; the Condition and the Warduke four sentences are verbatim anchors. The rewrite uses the 11-15-word speech rule except where VOICE or a verbatim anchor says otherwise.

---

## 11. Decisions the user must make

1. **Candidates.** (a) every unaffiliated character (recommended, with "civic-minded" deciding only whom Jalester addresses first); (b) only residents with a civic record per ev-04 (no outcome tests it); (c) hybrid.
2. **Cloak token.** (a) no token, Watch officers simply know the member by Jalester's say-so (recommended: nothing to lose, nothing to forge); (b) a brass tally or stamped paper the member shows an officer (more concrete, adds a loss rule).
3. **Open table.** (a) Jalester sits at the Portal table and accepts a late answer without chasing (recommended); (b) a once-only offer as in R/PREV 00:73, recorded as **Lords' Alliance Offer Closed** with a re-fire rule like FG's.
4. **Renown loss on dismissal.** Whether a serious offense also costs the general 2 Renown (PG :25) before the score goes inert (recommended: no further cost, state it); whether the reinstating intelligence earns its +1 once the member is reinstated.
5. **Dismissed members and other factions.** Whether a dismissed member counts as unaffiliated for other First Meetings (BD **Contact Severed** allows it for severed members; BD s04 :22 shows the model). Recommend yes, Renown 0.
6. **Introductions table.** Use only existing Notable Figures pages (Blastwind, Urmbrusk, Wands) or invent a guild/merchant list (flag as invented).
7. **Warduke Veterans.** Four unnamed Warrior Veterans (recommended, FG r25 names its own) or four named; fighting allies = PCs minus one.
8. **The Warduke Masked Lord.** Name a GM-only identity (not Mirt) or define the "door-opening" as the office's anonymous clerk with no identity at all.
9. **Runestone.** Fold the Runestone fragment (WDMM `data/0/entries/5/entries/2/entries/3`) into the Lioncrown request, keep it a seed, or drop it.
10. **If Jalester is removed from duty (LA M6 option / Harper M6).** Who replaces him at the drop for r10-r50: a named deputy (invented), Sevel Dastar earlier than r50, or the Alliance clerk at the Portal with no name.
11. **The `once per quest` unit in Mad Mage.** Each named quest counts as one; in Undermountain, one use per level the member enters (the EE r50 rule, EE r50 :284).
12. **Safe-house addresses.** Choose streets (not near Kolat Towers or Phaulkonmere) or leave addresses to the drafter's mechanics reference.
13. **Contact object.** The runner and the drop at the Portal (recommended) or another channel.
14. **Lioncrown honest answers.** Rewrite Laeral's lines so she never admits her decline (recommended) or let this one rank event break the profile.
15. **FM background color.** Whether to add an estate-style background scene like H's tailor (H FM :44-118). There is no LA request on record; recommend no.

---

## 12. Settled facts to keep, and parts to drop

**Keep (names, locations, numbers that other files read):**
- Names: Jalester Silvermane, Laeral Silverhand, Sevel Dastar, Faerrel Dunblade (NF-J), Piergeiron's Palace, the Yawning Portal corner table by the well, Trollskull Manor.
- Rank names and thresholds: Cloak 1, Redknife 3, Stingblade 10, Warduke 25, Lioncrown 50 (G03 :53-59; AB :252-256).
- Outcomes: **Lords' Alliance Joined**, **LA Suspended**, **LA Reinstated**, **LA Dismissed**, **LA Grand Game Escalated**, **Redknife Reached**, **Stingblade Reached**, **Warduke Reached**, **Lioncrown Reached**, **Undermountain Commission Accepted**.
- Numbers: two Guards one errand per tenday; two safe houses (Castle Ward, Trades Ward); one string-pull per tenday; one intro, one legal incident per quest; classified files four hours and DC 12; four Veterans one operation per quest; intel every three days; one Masked Lord request per quest; one audience per quest; +2 for the escalation once.
- The Condition verbatim: "Assignments from us are not optional. If that changes your answer, now is the time to say so." and the three-second wait (PREV 00:54-56; AB :228).
- Keeper lines: "Sit there a minute."; "Whatever you do with that is yours."; "I had you down as reliable."; "This is done. Your Renown stays on the books. It doesn't do anything."; "I was wrong about you."; "You're a Redknife. That means a few things change."; Laeral's "Private audiences. One per quest." / "I'm not doing this to make you feel important." / "Good work."; "Lioncrown. Sit down."; "The political backing is unconditional. The attaché is a resource, not a condition."
- The R-only character facts (section 2a): two operatives went dark and one did not survive; Jalester has taken two assignments back to Laeral and both times it mattered.
- Wording of the "compelling reason" examples (section 2b), the reinstatement path (verified intelligence), the two-line note signed "J.S.".

**Drop:**
- All retired blocks (section 10), the separate `## Read Aloud` sections, "Act N" headings, "Mission 5/6" numerals in fiction.
- R :36 / PREV r50 :36 ("How diminished are you really?").
- The `[!design]` box on Vault resolution (r50 :15-21).
- "Jalester does not return to recruit a second time" (00:13, :73) and the party-level outcome.
- "The character who delivered the briefing" +2 (one character).
- "first direct contact ... unless the Escalation event has fired" (r25 :10).
- "three of the twelve" (r50 :35).
- "the Stone's own revelation" as vault proof for s02 (Stone cannot give the location without Eyes).
- "Veterans" (use Warrior Veteran).
- The "Act 1 ... Act 6" scene labels.

---

## 13. Report-back list for the out-of-scope log

- `campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:26, :56, :100`: the LA row invitation, the 200 gp grant (delivered by the new First Meeting), and the party-level `Lords' Alliance Joined: True / False` heading.
- `campaign/guides/trollskull-manor/02-operating-costs.md:27, :81`: the Fellowship-line cut and the civic grant; the cut is passive and needs no event (log only).
- `campaign/guides/trollskull-manor/08-notable-patrons.md:107`: Jalester as "Veteran" and "N male" vs NF-J Spy and lawful good.
- `campaign/guides/factions/03-lords-alliance.md:12, :42, :47, :56-59, :67`: Watch patrol schedules never delivered; Manshoon wording; "Veterans" and "Guards"; `:68` says M4 locates Ziraj (OOS :301); the rank table has no procedures.
- `campaign/guides/factions/01-overview.md:11, :17`: "failing" a mission vs the clean-failure rule.
- `campaign/guides/players-guide/faction-affiliations.md:25`, `gm-guide/player-factions-overview.md:25`: "Serious offenses cost 2 Renown" vs s01.
- `campaign/setting/organizations/02-lords-alliance.md:7, :17, :23`: "Renown 25+" for Laeral access vs M6 at Renown 13; "deeply alarmed by Manshoon" (OOS :143).
- `campaign/setting/notable-figures/lords-alliance/01-jalester-silvermane.md:8`: "Featured in" lists LA missions, no rank or standalone event.
- `campaign/quests/act-ii/gralhund-villa/ev-01-what-the-factions-say.md:91`: **Jalester Brief Received: True / False** (old format).
- `campaign/structure/arc-e..j`: no reader of any LA outcome; `arc-j-vault-of-dragons.md:45` reads LA M6 only; `arc-j:43` and `arc-j:254` read the Jalester compromise loosely.
- `bregan-daerthe/m03-three-nights/ev-01-three-nights.md:226`: Redknife brings a patrol with no notice; conflicts with the 24-hour escort rule.
- `doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:162, :239`: an LA member of Renown 3 or higher gets Jalester's note without a check; a dismissed or suspended member must fail the test.
- `bregan-daerthe/s04-contact-severed/ev-01-contact-severed.md:155-157, :231`: reads the LA First Meeting; confirm the new FM covers a deferred candidate.
- `force-grey/m05-the-legates-eyes/ev-02-the-extraction.md:228-236`: names Jalester as "plain doublet"; keep consistent with the First Meeting description.
- `harpers/m06-the-stones-other-master/ev-01-the-stones-other-master.md:18, :320, :346` and `emerald-enclave/m06-the-dreamers-reach/overview.md:30`: Jalester as the listening post; the LA FM and s02 take place at the well.
- `docs/plans/harpers-out-of-scope-notes.md` LA section (lines 19-29, 44, 77, 131, 143, 225, 596-598, 686, 761): the items for reports 03-05.
- WDMM hooks: `data/0/entries/5/entries/2/entries/3` (Runestone) and `.../entries/2` (Joroth, +3 Renown) have no event.
- WDH vs NF: Jalester's age, class and alignment.
