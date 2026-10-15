# Lords' Alliance faction events: pre-rewrite consistency audit

**Model reading done (in full):** DR m03 `doom-raiders/m03-the-missing-snobeedle/` overview, ev-01 (every section, opening to Overview/Summary) and design-notes; DR r03 `doom-raiders/r03-wolf/` ev-01 and design-notes; BD m02 `bregan-daerthe/m02-the-wazoo-affair/` overview, ev-01 (every section) and design-notes; EE m04 `emerald-enclave/m04-the-grells-in-the-dock-ward/` overview, ev-01, ev-02 (every section) and design-notes. Matching Force Grey and Harper pages: FG m03 `force-grey/m03-the-trouble-with-meloon/` overview, design-notes, ev-01 (Summary, truth box, brief, Concluding the Event) and ev-02 (Event Outcomes and Next Steps); FG s01 `the-full-picture/ev-01` (Summary, test table, correction, outcomes); Harper M6 `harpers/m06-the-stones-other-master/` overview, design-notes and the Jalester passages and Event Outcomes of ev-01 (:18, :320-350, :381, :389-398). Also read: the research brief, the Emerald Enclave audit used as the report model, `session 43 handoff.md` and the Session 42 Rules and Instructions, CLAUDE.md, the Lords' Alliance Factions Guide page, organization page, Jalester's Notable Figures page, the `lords-alliance`, `city-officials`, `xanathars-guild` (Noska) and `independents-allies` (Esloon) voice entries, `sources/Appendix_B` and `Appendix_C` (the LA arcs), and the WDH and WDMM JSON passages on Jalester, Laeral and the LA missions. All 26 R files were read in full. PREV was read through a full diff against R (every non-format change inspected) and a grep of every flag, outcome, sidebar and rule hit. Each cited line below was taken from a grep of the named file, not from a combined listing.

I changed no campaign file. Shorthand:

- `R` = restored folder `/tmp/claude-0/-home-user-waterdeep/f91bf122-6992-582e-a45c-3f8e22918b72/scratchpad/la-orig/lords-alliance/` (26 files, 2,008 lines). Paths are relative to it, for example `R m03 ev-01:61`.
- `PREV` = `/home/user/waterdeep/campaign/quests/faction-events/lords-alliance/` (26 files, 2,076 lines). Where a line number differs from R, both are given.
- `Repo` = `/home/user/waterdeep`. `Notes` = `docs/plans/harpers-out-of-scope-notes.md`. `H42`, `H43` = the Session 42 and 43 handoffs.
- `G03` = `campaign/guides/factions/03-lords-alliance.md`. `Org02` = `campaign/setting/organizations/02-lords-alliance.md`. `NF-Jal` = `campaign/setting/notable-figures/lords-alliance/01-jalester-silvermane.md`. `NF-Lae` = `.../city-officials/01-laeral-silverhand.md`. `Voice` = `.claude/skills/character-voices/voices/lords-alliance.md`.
- `AppB`, `AppC` = `sources/Appendix_B_-_Player_Factions.md`, `sources/Appendix_C_-_Player_Faction_Missions.md`. `WDH`, `WDMM` = the two adventure JSONs.

Rules data (verified against `bestiary-xmm.json` in the scratchpad `5e/` folder, not from memory): 2024 XMM has **Mage** (CR 6, traits none, Spellcasting plus *Misty Step* and **Protective Magic** which casts *Counterspell* or *Shield*), **Spy**, **Bandit**, **Bandit Captain**, **Kenku**, **Noble**, **Guard**, **Commoner**, **Warrior Veteran** (CR 3, 65 HP), **Tough** and **Tough Boss**, **Carrion Crawler**. It has no **Thug** and no plain **Veteran**.

## 0. Coverage and what PREV actually is

- **Both folders hold 26 files**: First Meeting; M1 (overview, 2 events, design-notes); M2-M6 (overview, 1 event, design-notes each); r03, r10, r25, r50; s01, s02. There are no debrief events and no `ev-02` outside M1.
- **R is the original.** It uses `> **[GM]**` boxes (43 in the folder), `#### X: True / False` flags (10 headings, section 1a), `[!design]` (2), `[!profile]` (1) and `[!lore]` (2) callouts, `Milestone Overview` in six overviews (ov:11, M5 :8, M6 :15), `#### Milestone: None` in seven events, and "Arc B/E/F/G/J" labels in nine files (section 4h). It has **no Event Outcomes block anywhere**.
- **PREV is R plus a retrofit, not a rewrite.** The diff shows only five kinds of change:
  - The retired sidebars were added: `[!narrative]` (17), `[!npc-narrative]` (9) and `[!dialogue]` (9). `[!profile]`, `[!design]`, `[!lore]` and 43 `[GM]` boxes survive.
  - "Arc X" labels became quest names (for example PREV m06 ev-01:64, :112), but "Arc E" became **Faction Outposts** even where the sentence now reads oddly (PREV m03 ev-01:101).
  - Calendar words changed: "a week" to "a tenday", "two weeks" to "two tendays" (PREV m02 ev-01:17, :80, :92, :110; m04 overview:18, :27; m04 ev-01:19, :28, :78). "Two weeks" (14 days) became "two tendays" (20 days), a quiet change of length.
  - First Meeting was thinned: PREV dropped R's "Two went dark ... One did not survive the gap" (R 00:19) and "He has taken two assignments back to Laeral" (R 00:53) and turned Jalester's four answers into `[!dialogue]` boxes.
  - Prose trims in r03, r10, r25, r50 and s01 ("with the specificity of a man who has filed this particular paperwork" became "He has filed this paperwork before", PREV r03:27).
- **Not fixed in PREV:** every flag heading, every `Milestone` heading, every `[GM]` box, the Manshoon lines (37 lines, section 4a), the infernal lines (3, section 4b), the party-level wording (section 4c), the gates (section 4d) and the 2014 stat names (section 4g).
- **Which version carries settled facts:** R and PREV agree on every fact except the tenday/week edits, the trimmed First Meeting backstory, and `[!design]` indentation in r50. No outcome name differs between them. So "settled" below means the same in both unless marked.

## 1. Outcome map

### 1a. Written inside the Lords' Alliance folder

"Actual reader" means a reader on a different page. In-event readers are legitimate (Force Grey audit, section 8a). "None" means no page anywhere reads it by name. **No converted file reads any LA outcome by name**; every inbound reference is to an event title or a rank number (section 2).

| Outcome (flag) | R writer | PREV writer | Claimed readers | Actual reader found |
|---|---|---|---|---|
| **Lords' Alliance Joined** (`True / False`, "at least one party member") | R 00:61-63 | PREV 00:77 | every LA mission ("missions fire only for enrolled party members", R 00:63), s01 (R 00:63) | **Duplicate writer** at `act-i/trollskull-alley/ev-04-the-factions-come-calling.md:100-101` (`#### Lords' Alliance Joined: True / False`, party-level). No LA page reads it by name: the M1 gate (R m01 overview:6) is "from the campaign's first session". Same defect the Enclave audit logged for `ev-04:103`. |
| **Redknife Reached** | R r03:47-49 | PREV r03:47 | r10 ("does not fire until True", R r03:49) | r10 only, and r10 does not check it (r10 fires on Renown 10, R r10:7). No mission reads it. |
| **Stingblade Reached** | R r10:65-67 | PREV r10:65 | r25 | r25 only (same non-check, R r25:7). |
| **Warduke Reached** | R r25:68-70 | PREV r25:68 | r50 | r50 only. |
| **Lioncrown Reached** | R r50:151-153 | PREV r50:152 | "Vault of Dragons if it has not yet resolved", Mad Mage content | **None by name.** `structure/arc-j-vault-of-dragons.md` has no Lioncrown reader. |
| **Undermountain Commission Accepted** (`True / False`) | R r50:155-157 | PREV r50:156 | Mad Mage events | None. The **collision with the Enclave is gone**: Enclave r50 now writes **Illuun Watch Accepted** (H43:124). Notes:761 and H43:147 still list this as an open LA item (the name is fine, the format is not). |
| **LA Suspended**, **LA Reinstated**, **LA Dismissed** | R s01:121-131 | PREV s01:122-132 | every later LA mission brief; "Reinstatement Path"; **Vault of Dragons** for Laeral's attitude (R s01:131) | Only **Vault of Dragons** (unconverted). `arc-j-vault-of-dragons.md` does not mention suspension or dismissal at all (grep clean). The mission briefs do not read them (no LA mission has a "skip suspended members" line). |
| **LA Grand Game Escalated** (`True / False`, party-level) | R s02:91-93 | PREV s02:92-94 | **Faction Outposts**, **Cassalanter Villa**, **Sea Maidens Faire**, **Kolat Towers**, **Vault of Dragons** (R s02:93) | **None.** `arc-e`, `arc-g`, `arc-h`, `arc-i` have no Laeral-informed line. `arc-j:45` reads "If Lords' Alliance Mission 6 succeeded" instead. Overlaps **Vajra Briefed** (section 7.6). |
| Implicit state, no heading in R or PREV | | | | |
| Delvon Harsk's fate (arrested / warned off / never found) | R m01 ev-02:68-76 | PREV :76-84 | "Jalester responds differently to each ... shapes future missions" (R m01 design-notes:23-25, ev-02:101) | **None.** No later LA event reads it. |
| Pirn captured; Krentz named | R m01 ev-02:34-42 | PREV :40-47 | "flags the Xanathar Guild's Dock Ward cell for increased Watch scrutiny during the first two arcs" (R m01 ev-02:42) | None. Krentz is a Finding Floon NPC (section 6), so the "flag" has no reader in Act I either. |
| Herath's sewer note held | R m01 ev-02:78-89 | PREV :86-97 | **Xanathar's Lair** (Sewer Route) | **None.** `structure/arc-f-xanathars-lair.md` has no Herath, no Coin Alley checkpoint and no sewer-note entry (grep clean). The R text promises an entry path arc-f never lists. |
| Lira handled (honest / lied / threatened) | R m02 ev-01:73-83 | PREV :76-86 | "Jalester notices ... harder assignments" (R m02 ev-01:83) | None. |
| Harko taken to custody → Thayan file on Esloon | R m02 ev-01:105 | PREV :108 | M3 Option B (R m03 ev-01:41), M3 Option C DC "reduces by 2" (R m02 design-notes:21) | In folder only: M3 Option B reads it. The "-2 DC to locate Esloon" (R m02 design-notes:21) has no counterpart in M3, which never has the party locate Esloon. |
| Veralax reported → arrested | R m02 ev-01:103, :107 | PREV :106, :110 | "the Splinter response team in Arc E is missing one of its usual liaisons" | **None.** No Faction Outposts text or guide roster has a liaison to remove (section 2c). |
| Sarvos captured; checkpoint strike exposed | R m03 ev-01:61, :99 | PREV :61, :109 | "the strike fails when it fires in Arc E" (R m03 ev-01:99) | **None.** `arc-e-faction-outposts.md` has no Watch-checkpoint strike. |
| Deal concluded → Splinter team +2 members | R m03 ev-01:85 | PREV :95 | Faction Outposts | None (same). |
| Esloon's question carried to Jalester | R m03 ev-01:77-79 | PREV :87-89 | "a seed for a later session's conversation with Laeral" (R m03 design-notes:17) | None. Nothing later returns to it. |
| Vhaspar alive; Halek named | R m04 ev-01:60, :86 | PREV :63, :89 | the Alliance's Cassalanter dossier | **arc-g:533** and **G03:14, :28** read "Mission 4's Aftermath" in prose. No outcome name. |
| Villa address identified and reported | R m04 ev-01:69-79 | PREV :72-82 | **Cassalanter Villa** ("Alliance's Arc G intelligence package") | Same two prose readers. |
| Ledger delivered / lost to Noska / lost to Emira | R m05 ev-01:100-104, :80 | PREV :103-107 | M6 trigger; Faction Outposts / lair opposition states | M6 overview:8-10 (in folder). `arc-f` and `arc-g` do not read "Guild had the ledger" or "Cassalanters had the ledger" (grep clean for Fentree, Dunberton and ledger). |
| Emira Volstren identified | R m05 ev-01:84-86, :98 | PREV :87-89, :101 | "pre-Arc G dossier" (R m05 design-notes:19) | None. |
| Masked Lord's Writ issued; Manshoon offer accepted/declined; Laeral's "Keep an eye on them"; Jalester compromise told or kept | R m06 ev-01:44, :56-66, :72-86, :88-96 | PREV :48, :60-70, :76-90, :92-100 | **Vault of Dragons** | `arc-j:45` reads the Writ terms and the offer in prose (section 2c); `arc-j:166` and `gm-guide/design-notes-running-the-campaign.md:107` read the Writ as an Aurinax oath-release instrument. No outcome names. |

Gaps in what LA events record: no mission writes "member completed" in the form FG writes **M3 Complete** (FG m03 ev-02:261), so the gate "available after Mission N is complete" (R m02 overview:6 and so on) has no outcome behind it. No rank event writes a recipient name, as DR r03 does ("mark with the recipient's name", DR r03 ev-01:243). No outcome records the **Redknife** or **Stingblade** benefit counters (one escort per tenday, one introduction per quest). The Cloak rank and the 200 gp renovation grant have no event at all (section 7.8).

### 1b. Outcomes other factions write that the Lords' Alliance needs to read

- **Harper M6**: **Jalester Compromise Identified** (`harpers/m06.../ev-01:392`, defined as "mark when a member asks Mirt for the name and he gives it; read by Vault of Dragons and by An Audience with the Open Lord, whose Jalester Question treats it as a free-text reference"). R m06 reads it as "identified as Illuun-compromised (Harper Mission 6)" in free text (R m06 ev-01:13, :92; overview:28). It must be wired by name. Notes:598 already asks for this. The Illuun name is itself gated (section 4j).
- **Force Grey M5**: no outcome. FG m05 ev-02 offers the two Guild names to Jalester as an optional scene, "Nothing is marked and no Renown is awarded" (`force-grey/m05-the-legates-eyes/ev-02-the-extraction.md:242`). Notes:686 ("no event reads M5's Guild names for Jalester. Optional.") stands.
- **Force Grey s01**: **Vajra Briefed** (`force-grey/s01-the-full-picture/ev-01:277-279`), read by Vault of Dragons "to decide whether the Open Lord arrives prepared". This is the same job as **LA Grand Game Escalated** (section 7.6).
- **Doom Raiders s01** and **BD m03** read an LA member's rank, not an outcome (section 2b).
- **Faction Outposts (unconverted)** is the writer of **Manshoon Named**. Every LA event that names Manshoon needs it (section 4a).
- **Xanathar's Lair (unconverted)**: DR r03 and the Enclave read its Pool/Pier outcomes; none concern LA. Herath's note needs an arc-f entry (section 2c).
- **Kolat Towers (unconverted)**: **Manshoon operational?** (a result, not yet an outcome name; DR m06 overview:21 and the Kolat Towers summary in CLAUDE.md). LA M6's Manshoon offer branch should read it (section 4a and 7.4).

## 2. Inbound references: every file outside the folder that touches the Lords' Alliance

### 2a. Act I-II quest journals

| File | Line | What it says | Status |
|---|---|---|---|
| `act-i/trollskull-alley/ev-04-the-factions-come-calling.md` | :26 | Jalester "visits Trollskull or finds them at the Yawning Portal"; eligibility "City residents; civic-minded track record" | Agrees with R 00:9. |
| same | :36 | Link to `lords-alliance/00-first-meeting/ev-01-first-meeting.md` | Keep the path. |
| same | :56 | "Jalester's civic grant: 200 gp, no repayment; civic goodwill expected" | **R First Meeting has no grant, no Cloak rank, no renovation scene.** Compare the Enclave First Meeting's "Renovation Help" box (`emerald-enclave/00-first-meeting/ev-01:269-275`) and the Force Grey box (`force-grey/00-first-meeting/ev-01:230`). Gap (section 7.8). |
| same | :72 | "The Long Watch: Ten-day guard duty; carrion crawler on day nine" | **Contradicts R M1** (a Xanathar ambush on Night Three, no crawler; R m01 ev-02:9). Matches the source. Section 7.1. |
| same | :100-101 | `#### Lords' Alliance Joined: True / False` | Duplicate party-level writer (section 1a). |
| `structure/arc-b-trollskull-alley.md` | :122, :131, :138 | Same delivery row, the 200 gp grant, and "Protecting the Dungsweepers: Ten-day guard duty; carrion crawler on day nine" | Same three conflicts. Superseded by the converted quest journal for content, but still names the crawler. |
| `act-ii/fireball/ev-01-the-fireball.md` | :88, :196 | Faction channel at "Renown 1+" for *Speak with Dead*; Jalester's Faire docking-arrangements hook "(Renown 1+)" | Agrees with G03:25. **Renown 1+ means Cloak**, which no event grants (section 7.8). The hook is not read by any LA event; the Faire is only mentioned again by `arc-h:35`. |
| `act-ii/fireball/ev-06-the-death-mark.md` | :72 | Jalester "Reports to Laeral Silverhand. Returns within two hours ... Offers 72-hour Watch ID papers ... flagged as a possible Black Network safe house" | Consistent with Laeral as his superior. "Black Network safe house" is correctly un-named. No LA event reads the ID papers. |
| `act-ii/gralhund-villa/ev-01-what-the-factions-say.md` | :31-35, :91-92 | Jalester's Cromley path (forty-eight hours, signed statement); `#### Jalester Brief Received: True / False` | The True/False heading is a legacy flag, read by ev-09 only. No LA event refers to the Cromley path. |
| `act-ii/gralhund-villa/ev-09-aftermath.md` | :111 | Jalester's debrief: the Saerdoun Street beat was transferred a week before the raid, "source is unknown" | Not read or continued by any LA event. A thread LA M1 or M2 could pick up (the Watch leak). |
| `act-ii/gralhund-villa/ev-02-saerdoun-street.md` | :34; `ev-03b-the-front-door.md:33`; `overview.md:35` | Jalester as a source of Watch timing; a "Lords' Alliance seal" opens a gate | Reads the Redknife-level Watch access; not defined by any LA event. |

### 2b. Other factions' events

| File | Line | What it does with the Alliance | Consequence for the rewrite |
|---|---|---|---|
| `bregan-daerthe/s04-contact-severed/ev-01-contact-severed.md` | :9, :23, :155-163, :207, :231, :235 | A severed BD member can sell the watchers' description to Jalester for 50 gp; "A character who already belongs to the Lords' Alliance gives it as a report and takes no coin"; Jalester is "sits at a table by the stairs of the Yawning Portal in the evenings, or at Trollskull Manor"; he is "Lawful Good, Cormyrean Human" and "swears rarely and only at himself"; the scene "becomes available once the character has met Jalester Silvermane at the **Lords' Alliance First Meeting**, whether or not they joined" | The First Meeting must make Jalester findable at the Portal afterwards, and must not forbid a second approach by a character who did not join (R 00:13 "Jalester does not return to recruit a second time" is about recruiting, so it is compatible, but say so). **BD Watchers Sold** is read by Sea Maidens Faire, not by LA. `design-notes.md:47` already logs that the First Meeting is unconverted. |
| `bregan-daerthe/m03-three-nights/ev-01-three-nights.md` | :226 | "If the party includes a member of the Lords' Alliance at Renown 3 or higher (Redknife), a patrol of two **Guards** reaches the front door at the start of the fifth round ... Without a Redknife in the party, no patrol comes before morning." | **Conflicts with Redknife**: R r03:29 gives the escort only on "a day's notice, written, through the usual drop" for "one errand per tenday". An unscheduled rescue is not that benefit. Either the rewrite adds a short-notice clause to r03, or BD m03 changes. Logged in Notes:77 under an old line number (:122, now :226). |
| `doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md` | :162, :239 | Tashlyn: "If one of your friends holds rank in the Lords' Alliance, Jalester Silvermane can lean on her for you"; an LA member of Renown 3+ "asks Jalester ... The approach succeeds without a check. Jalester sends Dunfell a courtesy note the same day" | Compatible with Redknife's "string-pulling" (R r03:37) only if the rewrite defines string-pulling to include a courtesy note to a Watch sergeant on a case that is not the member's own. Say so in r03. |
| `harpers/m06-the-stones-other-master/ev-01:18, :320, :346-350, :381, :392`; `overview.md:21, :39, :47, :53`; `design-notes.md:5, :13, :15` | | Jalester is the unwitting contact; he "spends his evenings beside the Yawning Portal's well" and "is still loyal to Laeral"; Mirt does not approach him; the name is given only when a member asks | Jalester's seat must be **beside the well** wherever the LA pages place him (R uses "a table far enough from the bar", "a table near the far wall"; WDH says "a quiet corner"). Section 7.5. |
| `emerald-enclave/m06-the-dreamers-reach/ev-01-the-descent.md:22`; `overview.md:30`; `design-notes.md:13` | | "The anchor is one of two routes that Illuun uses. The other runs through Jalester ... (**The Stone's Other Master**, **An Audience with the Open Lord**). Nobody in this Event knows about it." "so the Harper and Lords' Alliance sixth missions still run as written" | LA M6 must keep running whether or not the anchor was destroyed and whether or not **Illuun Contact** was marked. Do not make the Jalester branch depend on the Enclave. |
| `force-grey/m05-the-legates-eyes/ev-02:228-242`, `overview.md:41, :64`, `design-notes.md:15, :23` | | Optional scene where Jalester receives the two Guild names; no outcome, no Renown | LA M5 or r10 may optionally acknowledge it. No reader exists (Notes:686). |
| `force-grey/r50-force-grey-commander/ev-01:38, :377, :380` | | Laeral's private request "belongs to the Lords' Alliance rank **Lioncrown**"; Mad Mage seed "Jalester Silvermane hires adventurers of 12th level or higher for a fragment of the Runestone, which lies on level 20 of Undermountain" | LA r50's Undermountain request (missing handlers, cartography team; R r50:127) and WDMM's Runestone errand (WDMM `Retrieve a Runestone Fragment`, prerequisite 12th level) are two different Laeral/Jalester Undermountain asks. r50 should either include or defer to the Runestone commission. Section 7.9. |
| `force-grey/s01-the-full-picture/ev-01:101, :243-247, :271` | | "I've sent a discreet inquiry about the treasury records for Neverember's years" (the Lords' Alliance); "The Lords' Alliance inquiry has no result in this Event" | No LA event reads Vajra's inquiry. Optional. |
| `bregan-daerthe/r25-commander/ev-01:10, :312-320, :340, :366` | | Jarlaxle asks a Commander which Masked Lord the member would trust to carry a letter "to the Lords' Alliance council"; the Vault later "delivers Jarlaxle's Lords' Alliance proposal" | Independent of LA events. But **LA r25's anonymous Masked Lord** (R r25:18, :40) and **Harper High Harper's Mirt-as-Masked-Lord reveal** (`factions/02-harpers.md:62`) both touch the same figure (section 7.9). |
| `force-grey/r10-senior-griffon/ev-01:223` | | "it does not stack with the Friendly toward the Watch that a Gray Hand already has, or with a Lords' Alliance or Harper courtesy" | Redknife/Cloak "trusted civilian informant" (G03:55) is the courtesy. Keep Cloak's wording stable. |
| `emerald-enclave` (m01-m05) | | No mention of Jalester or Laeral. The old Enclave Kelso line (Notes:44) was removed in Session 43. | Resolved. |

### 2c. Structure docs (`campaign/structure`)

These are authoritative for the unconverted quests. Each LA outcome has to be read from here when the quest is converted.

- `arc-e-faction-outposts.md:83` (Scene 2 consultation): "Jalester Silvermane (Lords' Alliance, renown 1+). The Alliance has Watch patrol schedules for every ward, available to the party with LA credentials at renown 3 or higher ... he wants the party to share what they find ... the party can earn that information by demonstrating commitment to the **Manshoon thread**." Manshoon gate hit (Notes:212). The "patrol schedules at Renown 3" perk is **not on the Redknife row** (G03:56; G03:12 has it as a "proactively shared" item). Fix in the rewrite: add it to r03 as a passive benefit, or drop it from arc-e.
- `arc-e:371` (Scene 8 debrief): Jalester "Wants all outpost intelligence shared with the Watch ... Offers legal cover for all this quest's operations retroactively in exchange for Manshoon intelligence that will hold up in a Magisters' proceeding." Reads no LA outcome. Possible tie to Stingblade legal coverage and to **Veralax Reported** (a Splinter operative the Watch already holds).
- `arc-f-xanathars-lair.md:33`: "At renown 10+, Jalester provides a letter of introduction to the Dock Ward senior Watch officer ... legal cover story ... keeping Watch patrols clear of the guildsign entrance for two hours." Not what Stingblade grants (R r10:29-45: introductions, legal coverage, Watch files). Sewer Route patrol windows are a Herath-note-adjacent idea; **Herath's note is not read here**.
- `arc-g-cassalanter-villa.md:37`: guest list and Watch rotation; "At renown 10+, Jalester pulls Watch files on the villa's recent contractor logs." That **is** a Watch Files use (Stingblade). `arc-g:533`: "The Vhaspar Holmbridge investigation from Mission 4's Aftermath produces an early Cassalanter dossier ... if Mission 4 was skipped, the Lords' Alliance has no advance intelligence on the villa." Reads M4 by prose; uses the archer's name (section 6).
- `arc-h-sea-maidens-faire.md:35, :430`: Laeral's request for the Faire's cargo manifests (SM3, the captain's office); a harbor inspection "usable once", "Requires 24 hours' notice" at renown 10+; `arc-h:101` makes Jalester the relevant contact for the Luskan alliance path ("Jalester represents the Alliance directly"); `arc-h:289` Jalester briefs Laeral about the submarine. None is an LA outcome. The harbor inspection is a rank benefit nobody grants.
- `arc-i-kolat-towers.md:35` (renown 10+ four-hour reassignment, "he suspects Masked Lord influence"), `:267` (Jalester asks "Is Manshoon neutralized?"). Reads nothing.
- `arc-j-vault-of-dragons.md:45`: if LA M6 succeeded, "the Vault district gate opens to it, Watch officers defer to it within four rounds ... Laeral has one legal intervention available ... If the party argued Laeral out of the Manshoon leverage offer, Jalester confirms it ... If the offer was accepted instead ... Manshoon can still delay Watch cooperation for up to two hours." Matches R m06 ev-01:84-86 and :62, so the Writ's terms and the offer branches are **settled** (section 8). `arc-j:43` reads "if the compromised contact was Jalester" in prose. `arc-j:166` names the Writ as one of three oath-release instruments. `arc-j:238` and `gm-guide/design-notes-running-the-campaign.md:93`: Laeral offers "a 10% finder's fee (50,000 gp)" and "asks only once"; **R m06 ev-01:76 has her say "The gold goes to the treasury. All of it. If you come out with it and take it somewhere else, the writ is void."** Section 7.4.
- `structure/ch1-beginning.md`, `ch2-city-of-splendors.md`, `ch3-running-the-campaign.md` are retired and not read.

### 2d. Guides, setting, Trollskull Manor guide

- **G03** (the Factions Guide page) is stale against R in five places and should be rewritten together with the events: M1 summary "Trades Ward ... carrion crawler emerges from the sewers on day nine" (G03:65, R is the Dock Ward and a Xanathar ambush); M3 "Prevent **Manshoon's Zhentarim** from recruiting" (G03:67, gate hit); M4 "Locate **Ziraj the Hunter**, a Doom Raiders assassin" (G03:68; the quest journal's archer is Vhaspar, and Ziraj belongs to DR M6, `doom-raiders/m06-zirajis-last-hunt/overview.md:19-21`); Redknife row lacks the "patrol schedules" perk that G03:12 and arc-e:83 assume; Earning Renown :42 and :47 say "neutralizing Manshoon's network" and "a named agent of Manshoon's Zhentarim cell" (gate hits, Notes:131). G03:13 puts the Thayan warrant "after Mission 3" and "filed three years ago"; R makes the file a Mission 2 reward (R m02 ev-01:105) and says the warrant is "not active in Waterdeep" (R m03 ev-01:45).
- **Org02** has the same Manshoon line (:17, Notes:143) and says Laeral is "reachable only through Jalester, and only once the PCs have earned sufficient standing (Renown 25+)" (:7, :23). That contradicts M6 (Renown 10, R m06 overview:6, and the shared ladder gives 13) and s02. It also says Jalester "delivers missions in person" (:8); R delivers M2 by "Watch-sealed note" (R m02 overview:25) and M5 by "plain-paper courier" (R m05 overview:24), and Trollskull's patron entry says "verbal, no scroll" (08-notable-patrons:109).
- **NF-Jal**: "Cormyrean human spy, lawful good. Stat block: **Spy**" (:6). WDH says "LG male Chondathan human fighter" and Jalester is "a young captain of the City Watch" in WDMM (`Retrieve a Runestone Fragment`). Three other converted pages agree with NF-Jal (BD s04 :157, FG m05 ev-02 :234, Voice "Cormyrean voice"). `08-notable-patrons.md:107` says "N male Cormyrean human, **Veteran**". The "Featured in" list (:8) uses the retired titles "Lords' Alliance Mission 1 - The Long Watch" and so on and lists **The Doppelganger Problem** and **The Stone's Other Master**. His persona says Faerrel Dunblade "died exposing a plot against the government" (:22); WDH, Org02:8 and the patrons page say "killed in a street fight last year" (WDH Jalester entry; `08-notable-patrons.md:108`).
- **NF-Lae** :8 still lists **Force Grey Mission 2** (Notes:689), and the retired M3/M5/M6 titles. Her Voice entry says "She never admits her power is diminished" (`city-officials.md:20`); R r50:36 has her answer "How diminished are you really?" (section 7.9).
- **NF Noska** (`xanathars-guild/05-noska-urgray.md`) lists "Lords' Alliance Mission 5 - Fentree's Ledger" under Featured in and calls him "the third response team leader", a shield dwarf with a crossbow arm and a rust monster (:22, :26). R m05 makes him "the guild's senior intelligence cell" representative with a Thug block "veteran training" (R m05 ev-01:22). See sections 6 and 7.3.
- **NF Esloon** (`independents-allies/16-esloon-bezant.md:8, :26`): "Featured in" M2 and M3; "they want him detained, not recruited"; "a past he does not discuss" (:22, :30). R m03 has him tell the party why he fled Thay (R m03 ev-01:71-75). Voice: "He never discusses why he left" (`independents-allies.md:277` block). Section 7.2.
- **Players' Guide / GM Guide** (`faction-affiliations.md:52-66`, `player-factions-overview.md:57-71`) carry the rank rows and the discipline line ("formal suspension until reinstated, or outright dismissal"). Consistent with G03 and s01. `player-factions-overview.md:29` and `faction-affiliations.md:29` say "Serious offenses cost 2 Renown each" while s01 says Renown is never reduced and dismissal makes it inert (R s01:13, :33, :82). `factions/01-overview.md:11` agrees with s01 ("not the Renown score itself, which becomes inert"); AppB:193 and WDH say dismissal means "loss of all renown". Settled by the Guide.
- **Trollskull Manor guide**: `02-operating-costs.md:27` "Jalester's civic designation reduces Fellowship line from 3 gp to 1 gp ... Any Watch citation resets this"; `:81` "Civic grant up to 200 gp from Laeral's discretionary fund. Ongoing compliance oversight"; `:19` lists the **Dungsweepers' Guild** as a 1 gp fee (the M1 client); `06-tavern-time.md:30, :34, :71` puts Jalester at the tavern after the first lair heist and on Founders' Day; `08-notable-patrons.md:107-112` gives him "a name: someone asking about the party through a Dock Ward cutpurse" and "what the party plans to do with the gold". The 200 gp grant needs a First Meeting scene (section 7.8). Notes:168, :186 log the multi-membership wording at `02-operating-costs.md:31` and `Org02:7, :23`.
- **Setting**: `setting/grand-game.md:34` lists the Cassalanters as knowing "Vault exists (Lords' Alliance contact)". That implies an Alliance leak. It fits Illuun-through-Jalester only loosely and fits M5's Emira. Decide whether the rewrite gives it a name (section 7.7). `setting/waterdeep-lore.md:32` calls the Dungsweepers' Guild "connected to the Dock Ward underworld", which supports Delvon's leak.

## 3. Items logged against the Lords' Alliance (Notes and handoffs): are they still live?

| Notes line | Item | Status |
|---|---|---|
| Notes:23 | m03 ev-01:128 "Manshoon's people, not Davil's" | **Live** (R m03 ev-01:117; PREV :128). Fix: "the splinter, not Davil's crew". |
| Notes:24 | m03 ev-01:121, :134; overview:25 "the Manshoon Splinter", "Manshoon's faction" in Overview/Summary | **Live** (R :111, :123; overview:25). Player-visible, so a V. |
| Notes:25 | m03 ev-01:61 "Manshoon's identity" | **Live** (R/PREV :61). |
| Notes:26 | m02 ev-01:110 "Manshoon Splinter operative" | **Live** (R :107; PREV :110). |
| Notes:27 | m02 ev-01:133; overview:29 | **Live** (R :129; overview:29). |
| Notes:28 | m06 ev-01:54 plus the GM-text list | **Live** (R :50; PREV :54). The 11 `Manshoon` lines in ev-01, 5 in design-notes, 3 in overview are all ungated. Mitigation: L7 requires **Kolat Towers** (CLAUDE.md), which names Manshoon, so the gate is satisfied by level, not by any outcome. Section 4a. |
| Notes:29 | m06 ev-01:107-108 "+1 if the party" | **Live** (R :103-104; PREV :107-108). |
| Notes:30 | m06 overview:5 L7 vs 3-heist parties at L6 | **Live** and sharper: the ladder now fixes M6 at L7, and the Vault is entered at L6 by 3-heist parties (CLAUDE.md, Vault of Dragons summary). The Writ is still obtainable because M6 is optional, but a party that skips Kolat Towers cannot reach L7 to run M6, so such parties never receive the Writ and `arc-j:45` needs a no-Writ default. |
| Notes:31 | r25 ev-01:64 "the Manshoon offer" | **Live** (R r25:64). |
| Notes:32 | s02 ev-01:23 "Manshoon's Zhentarim" | **Live** (R s02:23 on the Cassalanter paragraph; PREV :23). |
| Notes:33 | m04 overview:27 "the Cassalanters' infernal timeline" | **Live** (PREV overview:27 and ev-01:19 "ritual components connected to ... infernal timeline"). |
| Notes:34 | m05 ev-01:107 "infernal advisors" | **Live** (R :104; PREV :107). GM outcome text; keep out of player-visible text. |
| Notes:35 | 00-first-meeting :14, :73, :108 "The party accepts or declines"; `Joined: True / False` | **Live** (R 00:13, :57, :63). |
| Notes:36 | s01, s02, r03, r10, r50 `Flag: True/False` headings | **Live** (10 headings). |
| Notes:44 | EE m03 sends Kelso to Mirt and Jalester as "Manshoon's information network" | **Resolved**: the EE rewrite removed Jalester from the Enclave pages. |
| Notes:77 | "If the party has Lords' Alliance Renown 3" (BD m03) | **Live under a new line**: `bregan-daerthe/m03-three-nights/ev-01:226`. Plus the substantive conflict with r03's notice requirement (section 2b). |
| Notes:131 | G03:42, :47, :67 | **Live.** |
| Notes:143 | Org02:17 "Manshoon's activities" | **Live.** |
| Notes:168, :186 | multi-membership: `02-operating-costs.md:31`, `Org02:7, :23` | **Live.** |
| Notes:212 | arc-e:83, :87, :91, :351, :371, :377, :379, :495 | **Live** for :83 and :371 (Jalester). |
| Notes:225, :596 | Vault must read **High Harper Reached**, **Jalester Compromise Identified** etc. | **Live** (the LA half is M6 and the Writ). |
| Notes:301 | G03:68 says M4 locates Ziraj | **Live** (DR m06 design-notes:23 repeats it). |
| Notes:598 | LA M6 cites "Harper Mission 6" in free text | **Live** (R m06 overview:28, ev-01:13, :92). |
| Notes:616 | arc-i:19/247/265 "I volunteered" (Mirt Masked Lord) | Not LA, but touches r25's Masked Lord (section 7.9). |
| Notes:679 | Vault needs gold-path outcome names for r50 Laeral readings | **Live.** r50 :38 and :39 speak of the gold and the Vault resolution. |
| Notes:686 | no event reads M5's Guild names for Jalester | **Live**, optional. |
| Notes:689 | NF-Lae :8 lists Force Grey Mission 2 | **Live.** |
| Notes:761, H43:147 | r50 :156 `Undermountain Commission Accepted` and retired blocks | Format live; **name collision gone**. |
| H43:238 | "Remaining faction rewrites: Lords' Alliance and Order of the Gauntlet" | This work. |

## 4. Standing-rule audit

### 4a. Manshoon gate (CLAUDE.md; **Manshoon Named**, written by Faction Outposts, unconverted)

- **Count:** 37 lines mention Manshoon in 9 files (PREV: m02 overview 3, m02 ev-01 4, m03 overview 4, m03 ev-01 5, m06 overview 3, m06 ev-01 11, m06 design-notes 5, r25 1, s02 1). R has the same 37 lines. "Splinter" without the name appears on a further 37 lines (m02 6+4+2, m03 11+4+2, m06 7+2+1). "Kolat" appears twice (PREV m06 ev-01:66; s02:94). Both M2 and M3 are L3 and L4 missions that can run before the Interrogation House is hit.
- **Player-facing hits (V):**
  - Spoken: R m03 ev-01:117 ("Manshoon's people, not Davil's"), R m06 ev-01:50 (Laeral: "Manshoon's faction has offered me a complete accounting of the Masked Lords"), R m06 ev-01:68 (a "moral appeal" example, GM text).
  - Overview/Summary text: R m02 overview:16, :18, :29 and ev-01:129 ("a Manshoon Splinter fixer"), R m03 overview:17, :18, :25, :27 and ev-01:111, :123, R m06 overview:32, :40, :42 and ev-01:128.
- **GM-text hits (T):** R m02 ev-01:17 and :91, :107; R m03 ev-01:19 ("Manshoon's Dock Ward operations") and :61 ("A captured Sarvos will not give up Manshoon's identity"); R m06 ev-01:21, :60-66, :68; R m06 design-notes:19-31; R s02 ev-01:23 ("Xanathar's Guild and Manshoon's Zhentarim"); R r25:64.
- **Pattern to copy** (DR r03, the model): "Nobody in this Event can say Manshoon's name unless **Manshoon Named** has been marked, and the web reports every cell fact as 'the other cell' or 'the Splinter'" (`doom-raiders/r03-wolf/ev-01-wolf.md:22-24`); EE m04's truth box lists what each speaker knows (`emerald-enclave/m04.../ev-01:15-21`).
- **M2 and M3** (L3, L4): Jalester, Harko and the Overview must say "the Splinter" or "the other cell". Harko's "He's Zhentarim - the bad kind, not the ones who do business" (R m02 ev-01:89; PREV :92) is fine under the Two Zhentarims rule as street slang, but it should not become the player-visible Overview name. `Veralax` and `Sarvos Miln` are "Splinter fixers", never "Manshoon's".
- **M6** (L7): the level gate means **Kolat Towers** has run, and Kolat Towers names Manshoon (Notes:197 sequence: name at Interrogation House, identity at Kolat Towers). Recommend: speakers use "the Splinter's master" until **Manshoon Named** is marked for the listener and then "Manshoon"; the offer works without the name. Do not rely on the level to satisfy the gate, because the alternate trigger (R m06 overview:10, :20) has no Kolat Towers requirement stated.
- **s02** (fires "from early Act III"; R s02:15): the confirmed factions "by Act III are Xanathar's Guild and Manshoon's Zhentarim" (R s02:23). Fix: "the Splinter".
- **r25** (Renown 25, usually mid-campaign): "the Manshoon offer" in the lore box (R r25:64) leaks M6's offer into a rank page. Fix by saying "the offer from the Splinter" or cutting the box.
- **G03:42, :47, :67; Org02:17** need the same edits (Notes:131, :143).
- **Knowledge of the Stone/ledger:** R m05 has Emira, a Cassalanter, buying a ledger that says the vault is in Waterdeep. That leaks nothing about Manshoon. Pass.

### 4b. Cassalanter secrecy (suspicion only; only Jarlaxle knows; the Enclave may sense unattributed infernal influence)

- **Inside the folder (hits):**
  - R m04 ev-01:19 (GM Background) "ritual components connected to Arc G's infernal timeline", PREV :19 "**Cassalanter Villa**'s infernal timeline". GM-only, but it tells the GM the Cassalanters buy ritual components; the players' evidence is "Cassalanter-hired fence" and "Halek Farran, a Cassalanter household steward" (R m04 overview:17), which is **evidence of a crime** (three murders ordered by a household steward), not of infernalism. That is acceptable as suspicion. Fix the wording to "an errand the family wanted kept quiet".
  - R m04 overview:27 (player-visible Overview) repeats the "infernal timeline" (Notes:33). Strip it.
  - R m05 ev-01:104 "share it with their infernal advisors", PREV :107. GM-only outcome text. Keep out of anything players read.
- **Clean:** R s02:23 handles it correctly ("Nobody in the room knows what those things are ... 'unconfirmed, credible'"). Keep that paragraph and its Jalester line almost verbatim: it is the best treatment of the rule in the folder.
- **Source of knowledge:** Halek names the family only through a Cassalanter signet "kept turning it inward" (R m04 ev-01:62) and a partial address; Emira is identified by the same inward ring (R m05 ev-01:84). The ring is a nice repeated motif. It points at the household, not at the pact.
- **Hits outside:** `setting/grand-game.md:34` ("Vault exists (Lords' Alliance contact)") and `villains/cassalanters.md:39` ("political intelligence through Lords' Alliance contacts") imply a Cassalanter source inside the Alliance. Not a secrecy violation. It needs a name if Illuun-through-Jalester is the only leak (the Harper M6 text says the Stone's answer goes to Illuun, not to the Cassalanters).
- **Jarlaxle exception:** no LA event involves Jarlaxle or Vessa. The Faire alliance path (`arc-h:101`) casts Jalester as the Alliance's face; nothing there needs Cassalanter knowledge.

### 4c. Membership (one faction per PC; rank per individual; members-only briefs and debriefs)

- **Party-level wording in R:**
  - R 00:13 ("The party accepts or declines"), :57 ("If the party declines ... He does not approach them again"), :63 (flag: "at least one party member"), :69 ("once any enrolled character reaches 2nd level"), :71 ("If Lords' Alliance Joined is False: Jalester does not follow up"). The model writes the outcome per character with the character's name (`emerald-enclave/00-first-meeting/ev-01` Event Outcomes, quoted in section 1a above).
  - R m01 overview:6 "Available from the campaign's first session": the model gates M1 on joining plus L2 (DR m03 overview:3-4 pattern).
  - Mission briefs and debriefs: every R brief is written to "the party" (R m01 ev-01:122, m02 overview:25, m03 ev-01:117, m04 ev-01:103, m05 overview:24, m06 overview:36). There is no member-only line and no companion-wait line. DR m03 ev-01:3-14 and EE m04 ev-01:3-14 state "Only [faction] members attend the brief and debrief; companions can help with every other part".
  - R s02:9 ("The party briefs Jalester") and :58 ("The character who delivered the briefing earns +2 Renown"); the briefing is the party's, the Renown is one character's.
  - R m06: "Laeral summons the party" by Watch officers at Trollskull (R m06 ev-01:120). A summons to the party cannot also be members-only. The Writ "authorizes the party by name" (R m06 ev-01:82), which is a shared legal instrument.
  - Notes:35, :29 and :77 already flag the First Meeting, m06 :107-108 and BD m03.
- **Rank events are per character in R and PREV** (r03:7, r10:7, r25:7, r50:7: "after one Lords' Alliance member's Renown reaches N"), which is on-model. Their outcomes carry no recipient (section 1a).
- **Suspension and dismissal are per character** (R s01:15 "This event fires only for the character who refused or failed the assignment"). On-model. But s01 also says "Laeral Silverhand will know this character as someone Jalester dismissed" (R s01:114) and sets one `LA Dismissed` flag with no name (R s01:131). The Vault must read it per member.
- **Companions:** r03's safe houses admit "anyone ... vetted" (R r03:33). r25's "four Veterans" and Laeral's audiences, r10's introductions, r50's attaché are all single-character benefits (R r25:30; R r50:101-115). Companions get nothing; say so in each.
- **Multi-membership wording** remains in `faction-affiliations.md:3`, `player-factions-overview.md:3`, `factions/01-overview.md:7, :9`, `02-operating-costs.md:31`.

### 4d. Renown calibration (L2-3 = 2, L4-5 = 3, L6-7 = 4) and the shared gate ladder

- **The Guide's per-mission renown is calibrated** (G03:65-70): M1 +2, M2 +2, M3 +3, M4 +3, M5 +4, M6 +4.
- **The pages are not**: no mission states a base. They list bonuses only. M1 has one line in prose, "He offers two renown on completion" (R m01 ev-01:28).

| Mission | Guide base | R bonuses (R lines) | Sum of all bonuses |
|---|---|---|---|
| M1 | +2 | +1, +1 (R m01 ev-02:96-97) | 2 |
| M2 | +2 | +1, +1 (R m02 ev-01:102-103) | 2 |
| M3 | +3 | +1, +1 (R m03 ev-01:98-99) | **2 (short by 1)** |
| M4 | +3 | +1, +1 (R m04 ev-01:86-87) | **2 (short by 1)** |
| M5 | +4 | +1, +1 (R m05 ev-01:97-98); the second bundles two conditions with "or" | **2 (short by 2)** |
| M6 | +4 | +1, +1 (R m06 ev-01:103-104) | **2 (short by 2)** |

- **R gates are off the ladder at every step.** R: M1 "campaign's first session", M2 Renown 2/L3, M3 4/L4, M4 6/L5, M5 8/L6, M6 10/L7 (R overview:6 in each folder). The shared ladder (brief line 41, CLAUDE.md): **M1 joining/L2, M2 R3/L3, M3 R5/L4, M4 R8/L5, M5 R10/L6, M6 R13/L7**. The R gates are lower by 1, 1, 2, 2, 3 at M2-M6. Every R "Next Steps" line also repeats the old gate ("available at Lords' Alliance Renown 4 and 4th level", R m02 ev-01:111; "Renown 6 and 5th level", R m03 ev-01:103; "Renown 8 and 6th level", R m04 ev-01:91; "Renown 10 and 7th level", R m05 ev-01:108).
- **Reachability under the ladder with base values only**: join 1; M1 +2 = 3 (Redknife and M2 gate R3); M2 +2 = 5 (M3 gate R5); M3 +3 = 8 (M4 gate R8); M4 +3 = 11 (M5 gate R10; **Stingblade** at 10 arrives here, before M5); M5 +4 = 15 (M6 gate R13). With all three bonuses each: 1+5+5+6+6+7 = 30 before M6. The ladder is reachable on base alone. **Warduke (25)** needs bonuses or s02's +2; **Lioncrown (50)** is Mad Mage only (R r50:17).
- **Candidate +1 bonuses to fill the three-per-mission slots** (each must be a listed condition, not general good play):

  | Mission | Existing | Candidate additions already in the text |
  |---|---|---|
  | M1 | no further successful attack (R m01 ev-02:96); Delvon identified and arrested, or Pirn captured and his link exposed (:97) | split the second: **Delvon arrested** (R :68-72) and **Pirn captured** (R :33-42); a third could be keeping Herath's note |
  | M2 | Harko eliminated or in custody (R m02 ev-01:102); Veralax identified and the meeting address reported (:103) | Lira handled honestly (R :77) is the mission's stated test (R m02 design-notes:7-9) |
  | M3 | deal scuttled (R m03 ev-01:98); Sarvos captured and checkpoint named (:99) | Esloon's question carried to Jalester (R :79, design-notes:17) |
  | M4 | Vhaspar alive and naming Halek (R m04 ev-01:86); address identified and reported (:87) | the longshoreman target is saved or warned (R :65, the fourth name) |
  | M5 | ledger reaches Jalester within 24 hours (R m05 ev-01:97); Noska captured **or** Emira identified (:98) | split the "or": **Noska captured**, **Emira identified** (R :84-86), keep the 24-hour condition |
  | M6 | accurate Stone and two-faction intelligence (R m06 ev-01:103); successful argument against the offer (:104) | honest audience, no lie detected (R :44); or the Jalester question told to Laeral (R :90-96) |

- **Rank thresholds 1/3/10/25/50** (G03:55-59, `faction-affiliations.md:60-66`) match r03/r10/r25/r50. **Cloak (Renown 1)** has no event.
- **Source renown values** differ: AppC gives +1, +1, +2, +2 for M1-M4 (AppC:465, :546, :612, :681); the Guide raised them (G03:65-70). Not a violation.
- **"Award" language**: R has "+1 if ..." under `**Renown:**` in `[GM]` boxes in every mission and s02's "earns +2 Renown immediately" (R s02:58). Move to the DR format (`doom-raiders/m03.../ev-01:499-513`, base + three listed +1s, "Companions gain none").
- **s02**: +2 once per campaign for the character who delivers the briefing (R s02:11, :36, :58); G03:45 gives the same. Treat as additional to base. It is a single-character award in a party scene; say "each Lords' Alliance member who gives the account" or keep one recipient and name the rule.
- **Level bands**: R M1 L2 (R m01 overview:9), M2 L3, M3 L4, M4 L5, M5 no Difficulty section at all (R m05 overview), M6 L7. G03:65-70 agrees. **M6 at L7** requires all four heists (Notes:30, 4a).

### 4e. "The renown ladder wins" / no mission grants rank

- **Mostly pass.** No mission names a rank. Rank titles appear only in the rank events and the Guide.
- **Two breaks:**
  - R 00:25-71 never names **Cloak** (Renown 1), so the join event grants nothing the table can see. By the model, the First Meeting names the first rank (as FG names Gray Hand in `force-grey/00-first-meeting/ev-01-first-meeting.md`; the Enclave names Springwarden).
  - R s01:114-139 says "the political weight of that knowledge surfaces in **Vault of Dragons**, where ... every member's standing" and R s02:93 says the Vault reads whether Laeral is a "prepared ally". Neither is a rank. Fine.
- **M6 and r25 both give Laeral audiences.** R r25:64 separates them ("Warduke audiences are consultations ... She is not a quest dispenser"). Keep that; M6 is a plot audience gated by Renown 13 and the ladder, not a rank benefit.

### 4f. Event Outcomes instead of flags; one writer per outcome

- R and PREV: no Event Outcomes block; 10 `True / False` headings (section 1a). `Next Steps` blocks mix gating text and flags. The model puts outcomes in a `> [!gamemaster]**Event Outcomes**` list "name - when to mark; read by ..." followed by `**Next Steps**` (`doom-raiders/m03.../ev-01:519-532`; `emerald-enclave/m04.../ev-02:304-312`).
- **Writer duplication:** **Lords' Alliance Joined** (First Meeting and Trollskull ev-04), **Jalester Brief Received** (Gralhund ev-01:91 writes a flag read by ev-09).
- **Two writers for one fact** inside the folder: Laeral learns the vault is in Waterdeep from M5's ledger (R m05 ev-01:100) and from s02's briefing (R s02:31, :91-93), and the Vault reads s02's flag, M6 reads M5's result. One state, two writers (section 7.6).
- **Outcome naming in R**: "LA Grand Game Escalated", "LA Suspended" etc. use the "LA" abbreviation; the model avoids abbreviations in outcome names (DR "Davil Arrested", Enclave "Illuun Contact").
- **Readers that cannot exist yet** (retarget as the Enclave did, H43:110): **Veralax Reported** and **Sarvos Captured** are read by "Faction Outposts" in R, but M2 is L3 and M3 is L4, and Outposts is the Act III on-ramp (arc-e:395: "the recommended on-ramp, not a hard gate"). Those missions can run before or during Outposts. Only the Outposts text that runs after them can read them; they cannot be a hard prerequisite.

### 4g. Wish, intellect devourers, and 2024 names

- **Wish / devourer:** grep clean (no *Wish*, no intellect devourer, no Occupying Devourer needed). FG m03 owns Meloon (`force-grey/m03.../overview.md:8-9`); nothing in LA touches him.
- **2014 stat names (verified against XMM):**
  - **Thug** (no such 2024 block; use **Tough**, CR 1/2, 32 HP, or **Tough Boss**, CR 4): R m01 overview:23; ev-02:9-10, :23, :27, :29, :55 (three Thugs plus Pirn); R m05 ev-01:22, :73 ("Thug stat block, veteran training"); R m05 overview:20. R m03's six "Thugs" (R m03 overview:21; ev-01:17).
  - **Veteran** (2024 name is **Warrior Veteran**, CR 3, 65 HP): R m03 overview:21 and ev-01:37 ("two Veterans" at the door); R m04 overview:21 (Vhaspar "use Veteran stat block"); R r25:30 and G03:58 ("four **Veterans**"); `08-notable-patrons.md:107` (Jalester "Veteran"). The rank benefit should name the **Warrior Veteran**.
  - **Mage with "Arcane Recovery replaced by a once-per-day *Counterspell* as a Reaction"** (R m03 overview:21; ev-01:17): a 2024 **Mage** has no Arcane Recovery (traits are empty) and already has **Protective Magic (3/Day)**, which casts *Counterspell* or *Shield* as a reaction. The "modification" is a 2014 invention that duplicates a standard feature. Use the stock block.
  - **Bandit Captain**, **Kenku**, **Bandit**, **Spy**, **Noble**, **Guard**, **Commoner**, **Carrion Crawler**: all exist in XMM with the names used. Pirn and Sarvos as **Spy** (R m01 overview:23; m03 ev-01:19), Rezka as **Spy** (R m05 overview:20), Emira as **Noble** (R m05 ev-01:22), Berna as **Commoner**, Sevel Dastar as **Spy** (R r50:29). The 2024 **Spy** has 27 HP and *Cunning Action*; the encounter math needs rebuilding with CR 2.0 (rosters in R m02 and m03 are untested).
  - "Thug stat block, veteran training" (R m05) is not a thing in either edition.
- **Action names** in R: "Utilize", "Magic action", "Study" appear nowhere; the events use 2014 "Strength (Athletics)" style checks, which are fine in 2024. DCs are plain numbers with no stat-block cross-checks, so the Mechanics Reference will need to audit M2 (Harko 52 HP, two Bandits 11 HP each, two Kenku), M3 (Esloon + 6 + 2), M5 (Noska + 2 Bandits), and the one-fight M1 ambush at 3, 4 and 5 characters. None of them lists a 3/4/5 roster.

### 4h. Quests, not arcs

- **Hits (R):** "Arc B" (m01 ev-02:42), "Arc E" (m02 ev-01:13, :107; m02 design-notes:17, :19; m03 ev-01:12, :85, :87, :91, :99; m03 design-notes:19, :21), "Arc F" (m01 design-notes:17; m01 ev-02:89; m05 design-notes:7; m05 ev-01:102), "Arc G" (m04 ev-01:13, :75, :77, :87; m04 design-notes:5, :7, :9; m05 design-notes:19; m05 ev-01:104; m06 design-notes:7), "Arc J" (m05 design-notes:5; m06 design-notes:21-31; m06 ev-01:11, :60, :62, :84, :86, :94, :108) and "Arcs C-H" (m06 design-notes:17), plus "Arc G Overview" (m04 ev-01:77).
- **PREV** converted them to quest titles (Faction Outposts, Cassalanter Villa, Vault of Dragons, Xanathar's Lair, Trollskull Alley), but **two are wrong**: Krentz "appears in **Trollskull Alley**'s sewers sequence" (PREV m01 ev-02:47; he is in Finding Floon, section 6) and "the first two quests" (PREV m01 ev-02:47).
- Mission names carry "Lords' Alliance Mission N - Title" in R next-steps and in the NF pages' Featured-in lists. The model names missions by title only.

### 4i. Bregan D'aerthe rejects Lolth

- Pass. No Lolth, no BD content in the folder. BD appears only inbound (section 2b).

### 4j. Jarlaxle hidden identity, Two Zhentarims, and the Illuun name

- **Jarlaxle:** no LA event names him; the Faire alliance path is in `arc-h`. Pass.
- **Two Zhentarims:** R m03 ev-01:117 is the one place that names both cells in one line ("Manshoon's people, not Davil's"). That does the Two Zhentarims job and trips the Manshoon gate. Fix: "the splinter, not Davil's crew" (Notes:23). R m02 ev-01:89 (PREV :92) Harko's "He's Zhentarim - the bad kind, not the ones who do business" is on-model slang for a street speaker. G03:67 and Org02:17 should say "the Splinter".
- **Illuun name gate:** the Enclave organization page gives the rule: the name reaches an Enclave member only through **Anchor Destroyed**, **Illuun Contact**-plus-attunement or the Stone at Full Awakening (`organizations/03-emerald-enclave.md:37-38`). R m06 names Illuun in four places (R m06 overview:28; ev-01:13, :92, :96). They are GM text, but R m06 overview:28 is an **Involved Characters** line (player-facing in the Ember page model) and ev-01:13 is the Gamemaster's Summary. The Harper M6 event says "something old and patient" and names Jalester without naming Illuun to the player (`harpers/m06.../ev-01:350`). Use the Harper wording in anything a player reads: "the link", "something answered from below".

## 5. Jalester, Laeral and the other persons: every fact on every page

### 5.1 Jalester Silvermane

| Fact | Source | Conflict |
|---|---|---|
| Cormyrean human spy, lawful good, Stat block **Spy** | NF-Jal:6 | WDH: "LG male Chondathan human fighter" (Appendix B entry); WDMM: "a young captain of the City Watch". Patrons page: "N male Cormyrean human, Veteran" (`08-notable-patrons.md:107`). |
| Thinning hair, dark doublet, collar fastened; asks one question more specific than the conversation needs | NF-Jal:22; R 00:23; Voice | None. |
| Lonely; boyfriend Faerrel Dunblade | NF-Jal:14-16; WDH; Org02:8 | NF-Jal:22 says Faerrel "died exposing a plot against the government"; WDH/Org02/patrons say "killed in a street fight last year". |
| Former Steel Shadows (Cormyr) mercenary | NF-Jal:26 | Only place it appears. |
| Reports to Laeral; field agent; "delivers missions in person" | NF-Jal:26; Org02:8 | M2 note and M5 courier (R m02 overview:25; R m05 overview:24); patrons "verbal, no scroll" (`08-notable-patrons.md:109`). |
| Sits at the Yawning Portal | WDH ("usually seated by himself in a quiet corner"); R m01 ev-01:24, R s02:40 ("a table near the far wall") | **Harper M6** needs him "beside the well" (`harpers/m06.../overview.md:21`); BD s04:157 "table by the stairs". |
| Never disobeys Laeral, never breaks cover carelessly, never talks about Faerrel unless asked twice | Voice | R m06 has him obey; R r50 has him bring Sevel. Pass. |
| Swears: stingy, self-directed; one "fuck" if Faerrel is used against him | Voice | R/PREV Jalester never swears. Pass. |
| "Understood." / "One more detail, if you don't mind." / "Discreetly, please." | Voice | R uses none of the signature phrases; R m01 and m02 lines are in a different register ("Do the work.", "I said quietly."). Check in the rewrite against `character-voices`. |
| His Voice greeting references "the Gralhund villa on the night in question" | Voice | R 00:25 references **Candle Lane** (Finding Floon). Both fine; First Meeting happens during Trollskull Alley, before Gralhund (Ches 20 vs Ches 24, `structural-rules.md:43-47`), so Candle Lane is right. |
| WDMM: hires adventurers of 12th level for a Runestone fragment | WDMM Retrieve a Runestone Fragment | Not in any LA page; FG r50:377 carries it. |

### 5.2 Laeral Silverhand

- NF-Lae: moon elf archmage, **Archmage** block, chaotic good; "unease when the party glimpses how diminished she truly is"; "Deep down, only Elminster knows the extent of her decline" (:22, :26). Voice: "Her concealed decline shows as deflection whenever magic is discussed directly" and **Never**: "never admits her power is diminished" (`city-officials.md:20`).
- R r50:36: "How diminished are you really?" - "Less than my enemies assume. More than my staff knows." It is a partial admission. FG r50 seed: "Laeral's magic has begun to wane, and only her closest confidants know it. No line in this Event says so" (`force-grey/r50-force-grey-commander/ev-01:377`). WDMM: "Unbeknownst to anyone but her closest confidants".
- R r50:38 says Laeral "did not know the vault existed until the intelligence that set Mission 5 in motion". Every other LA page says she **knew it existed and believed it was in Neverwinter** (R m05 design-notes:5; R s02:19; G03:9; Org02:17). Contradiction.
- R m06 overview:36-42 and G03:30, :70 put Laeral at **Piergeiron's Palace**; WDH says she "spends most of her time in the Palace of Waterdeep". In the published setting these are one building, but no setting page in this repo says so (grep of `campaign/setting` and `campaign/guides` finds only G03). Add one sentence to the Waterdeep lore page or pick one name.
- NF-Lae :8 "Featured in" lists FG Mission 2, which does not feature her.

### 5.3 Other persons

| Person | R location | Other pages | Notes |
|---|---|---|---|
| Mareva Coile, 45, Dungsweepers' Guild route coordinator | R m01 overview:16; ev-01:32 | none | No NF page, no Voice entry. Voice from event text. |
| Berna, dwarf, ~60, grey braid, field crew leader | R m01 ev-01:38; AppC:429 | none (AppC: "dwarf **Commoner**") | Source: "Trades Ward circuit, twenty years, seventeen of them"; R: "Dock and Trades Ward circuits". |
| Herath, young Calishite sweeper | R m01 ev-01:74 | none | Coin purse 12 gp; sewer note (source and R). |
| Delvon Harsk, route supervisor | R m01 overview:19 | none | PREV fixed the name to "Delvon Harsk" across files (H43 mention in the brief). R/PREV agree now. |
| Orryn Saltwick, Bremma Dunnet, Cass Fildura | R m01 ev-02:54 | none | "Orryn" collides in first name only with Orryn Tetch (Trollskull staff, `03-staff-and-hiring.md:45`). |
| Pirn (Xanathar street agent) | R m01 ev-01:84 | none | Spy block. |
| Harko Swornhold, 50, exiled three years ago for bribing Magister Kylynne Silmerhelve | R m02 ev-01:125; AppC | WDH line | Source says he "will not surrender"; R has him surrender at half HP (R m02 ev-01:49-53). |
| Lira, Calishite server at the Muleskull | R m02 ev-01:69 | AppC, no other page | The Muleskull is also DR m01's stakeout (`doom-raiders/m01-the-dockside-killer/ev-01:37, :92`) on Ship Street; consistent. DR m01 never mentions a server. |
| Veralax, Splinter fixer, "dresses like a gem merchant" | R m02 ev-01:89 | none | Meets at the "Bent Nail alehouse, Dock Ward, every Highsun, middle booth" - **collides with Tally's Bent Nail** (section 6). |
| Esloon Bezant | R m03 | NF Esloon | "left Thay four years ago" (R m03 ev-01:17) vs "in this city for five years" (R m03 ev-01:71 and AppC); NF: neutral, R: Chaotic Neutral, AppC/WDH: LE. |
| Sarvos Miln | R m03 ev-01:19 | none | Spy block; alias "Holvar" is the booking name. |
| Vhaspar Holmbridge, 57 | R m04 | none | **Collides with WDH's Vhaspar Holmdreg** (section 6). |
| Halek Farran, Cassalanter steward | R m04 | none; `cassalanters/` NF pages list no steward; Willifort Crowelle is the butler (a doppelganger) | Not on any Cassalanter roster. |
| Yander Coirn, Pell Street feed store | R m04 | none | Pell Street is not elsewhere in the campaign. |
| Orvane Fentree, 71, retired trade investigator | R m05 | listed in NF-Lae, Noska, Dagult pages as a title only | See date problem (7.3). |
| Rezka, Emira Volstren, Pravin Cloth, Orlass Hemmet | R m05 | none | Rezka and Pravin names are clean. |
| Noska Ur'gray | R m05 | NF Noska, voice, response-team ladder in DR r03 | Section 7.3. |
| Sevel Dastar, Spy | R r50:29 | none | WDMM's Alliance spy is **Joroth Brighthelm** (a dwarf), with Falkir's Fist as the missing party. Free to rename or merge. |

## 6. NPC name collisions

Checked every LA name and place against all of `campaign/` (grep, case-insensitive) and the WDH/WDMM JSON.

| LA name | Collides with | Verdict |
|---|---|---|
| **Vhaspar Holmbridge** (M4 archer) | **Vhaspar Holmdreg**, WDH's old Ilmater priest who keeps Kalain's key and lives beside the Vault trapdoor (WDH Brandath/Kalain's residence entry) | **Rename.** Same first name, near-identical surname, and a WDH NPC who matters to Vault of Dragons. G03:14/:28, arc-g:533 and DR m06 design-notes:23 carry the old name. |
| **The Bent Nail** (Veralax's alehouse, R m02 ev-01:89-94, :103) | **The Bent Nail**, Tally Fellbranch's woodshop in Trollskull Alley (`trollskull-community/01-talisolvanar-fellbranch.md:24, :30`; `ev-01-welcome-to-trollskull-alley.md:22`; Trollskull guide) | **Rename** the alehouse. Different ward, different business. |
| **Noska Ur'gray** as an intelligence-cell go-between (M5) | Noska Ur'gray, the Guild's heavy and **third response-team leader** (shield dwarf, crossbow arm, rust monster, "very short sentences", `xanathars-guild.md` Voice block; DR r03 ev-01:125 ladder "Noska Ur'gray with six bugbears and a gazer") | **Rename or replace** the M5 buyer. If he stays: use his own block and voice, and say what happens to the third response team when he is captured. NF Noska already lists "Lords' Alliance Mission 5". |
| **Krentz** (Pirn's authorizer) | Krentz, the Xanathar thug leader in Finding Floon `ev-01-yawning-portal.md:33`, who may reappear in the sewer hideout Q05 (`ev-04-xanathar-sewer-hideout.md:57`) | **Same character, wrong quest label** (R says "Arc B"; PREV says "Trollskull Alley"). If kept, say Finding Floon. He is a street thug in Act I; a street agent who authorizes a Dock Ward operation is plausible. |
| **The Tenday Watch** (M1 ev-01 title) | **The Tenday Watch**, FG m03 ev-01 title (`force-grey/m03-the-trouble-with-meloon/ev-01-the-tenday-watch.md:1`) | **Rename the LA event** (two events with the same H1). |
| **Skewered Dragon Tavern** (M3 setting; M4 Vhaspar's fallback cellar) | The Skewered Dragon in Finding Floon (Dock Ward; "Floon was last at the Skewered Dragon") and Harper M3 (`ev-01-the-doppelganger-auditions.md:211`) | Same tavern, reuse is consistent. But source M3 uses the **Rusted Anchor** (AppC:573) and the Skewered Dragon is a plot location elsewhere; check M3 does not contradict Finding Floon's layout (`act-i/finding-floon/ev-02-dock-ward-investigation.md:41`). |
| **Muleskull Tavern, Ship Street** | DR m01 and BD s05 (`bregan-daerthe/s05-the-killers-fate/ev-01:385`) | Shared, consistent (Dock Ward, Ship Street, quay steps). Keep. |
| **Margaster Street** (M1 watcher) | A. Margaster, Margaster House, North Ward (`act-ii/fireball/ev-03-the-nimblewright-hunt.md:30`) | Different thing (a family/house vs a Dock Ward street). Low risk; rename to avoid confusion. |
| **Orryn Saltwick** | Orryn Tetch (Trollskull staff) | First name only; low risk. |
| **A ship chandler on Sail Street** (R m02 ev-01:29, the first Harko lead) | Tarrow's Tallow and Wick, 22 Sail Street, the Doom Raiders' Wolf safe house (`doom-raiders/r03-wolf/ev-01-wolf.md`, "The Loft on Sail Street") | Different trade (ship chandler vs tallow chandler) but the same short street. Move the lead to another street or name the chandler so the two never read as one shop. |
| **Candle Lane** | the Zhentarim warehouse (Finding Floon) | Correct reference in the First Meeting (R 00:25). |
| Berna, Herath, Delvon Harsk, Pirn, Mareva Coile, Lira, Veralax, Sarvos Miln, Halek Farran, Yander Coirn, Rezka, Emira Volstren, Pravin Cloth, Orlass Hemmet, Sevel Dastar, Kylynne Silmerhelve, Harko Swornhold, Holvar, Dunberton Holdings | none (grep clean) | Free. |
| Esloon Bezant, Jalester, Laeral | NF pages exist | Same characters. |

## 7. Contradictions to resolve before drafting

### 7.1 M1: the guide, Trollskull Alley and arc-b promise a carrion crawler; R has a Xanathar ambush

- **Facts:** The source (WDH row 2nd; AppC:447-460) is a ten-day detail in the **Trades Ward**, with a **carrion crawler** on day nine, Berna as "dwarf Commoner" and Herath's sewer note (AppC:465-467). R replaces the crawler with a Night Three ambush by Xanathar thugs, Pirn, and a leak (Delvon), set in the **Dock Ward** (R m01 overview:23, ev-02:7-14). G03:65, `ev-04:72` and `arc-b:138` still carry the crawler.
- **Internal timeline break:** ev-01 covers Days 1-7 and says "Night Three comes tonight" after Day 7 (R m01 ev-01:106). ev-02 is "the third night of the tenday" (R m01 ev-02:7). Herath's note comes on "the final day" (day 10) (R m01 ev-02:80). The ambush is Night Three but is placed after Day 7.
- **Options:** (a) keep the ambush and update three external lines; (b) restore the source crawler on Day 9 and keep the Delvon leak, so a Xanathar crew dug the tunnel that released the crawler on the day Delvon's timing said Mareva's crew would be exposed (the source already says the crawler "likely [came] up through the sewer system, disturbed by Xanathar Guild activity"); (c) both, ambush on Night Three and crawler on Day 9. Recommend **(b)**: it keeps what the source, G03 and two Act I files already promise, keeps the best R idea (the insider and Herath's note), and needs only a time fix (Night Three becomes a Day-9 noon event). Choose the 2024 **Carrion Crawler** (CR 2, 51 HP; `Paralyzing Tentacles`, `Bite`; verified).

### 7.2 M3: Esloon's confession vs his voice, his NF page, and the source

- R m03 ev-01:71-75 gives Esloon a long speech ("I fled Thay because they were going to kill me ... I have been in this city for five years"), the mission's centrepiece beat. His Voice entry says "He never discusses why he left" and "He refers to Thay as 'home, formerly'" (`independents-allies.md`, Esloon block), and NF says "a past he does not discuss" (`16-esloon-bezant.md:22, :30`).
- Internal: "left Thay four years ago" (R m03 ev-01:17) vs "in this city for five years" (R m03 ev-01:71). Alignment: R "Chaotic Neutral"; NF "neutral"; AppC/WDH "LE".
- Source M3 offers three paths (forged letter DC 16, confrontation DC 15, bribery 500 gp) and the "another offer?" question (AppC:586-607; WDH row 4th). R keeps the question but replaces the three paths with four (R m03 ev-01:35-61).
- **Recommend:** keep the question (it is the source's own and the mission's point), cut the Thay backstory speech to the two lines the Voice allows ("Home, formerly. They don't forget."), settle one number (five years in the city, so "left Thay five years ago" everywhere), and fix the NF "Featured in" (Esloon is in M3 only; he appears in M2 only as a file). Keep NF's "detained, not recruited" or drop it: R Option C turns him.
- R m03 ev-01:79: Jalester's answer ("I'll look into whether there's something we can formalize") duplicates AppC verbatim (AppC:606). Fine; it is source text.

### 7.3 M5: Noska, the date, the ledger's years, and who learns what

- **Noska** is the Guild's third response-team leader with six bugbears and a gazer (DR r03 ev-01:125 ladder; NF Noska:26) and a Voice of very short sentences who "never negotiates". R m05 has him bidding at the Green Dragon as a representative of the "senior intelligence cell" with a **Thug** block and two **Bandits**. As the third response team he may already be beaten by M5 (L6, after two heists). Replace him with an invented Guild buyer, or keep him and let the DR r03 ladder know M5's outcome (**Noska captured** removes team three).
- **"Greengrass morning"** (R m05 ev-01:124): Greengrass is Tarsakh 1. The campaign calendar has Faction Outposts begin ~Ches 25 and the lair phase run into Flamerule (`structural-rules.md:42-52`). M5 is L6, after two heists, so it cannot fall on Tarsakh 1-3 ("the missing volume was pulled within the last two days", R m05 ev-01:31). Drop the date; say "ten days ago".
- **"1244 DR"** (R m05 ev-01:18, :88): the ledger is "twenty years" old and Fentree is 71 and retired, yet the entries are dated about 250 years before the campaign. Neverember left office "eleven years ago" (arc-e:33). Use a date inside that span.
- **"Vault district" / "vault custodian"** (R m05 ev-01:88): Waterdeep has no Vault district. The vault lies under the Brandath Crypts (`running-the-villains.md:9`). Give the ledger a real address (the City of the Dead or a trade house) so it points at Waterdeep without naming the crypts, which the party discovers at Full Awakening.
- **What the ledger proves:** that "the vault is active and located in Waterdeep" (R m05 overview:26). Laeral knowing that is the whole point of s02 too (7.6).
- **Emira is Cassalanter**; the Cassalanter pages list neither her nor Halek (section 5.3). Either attach both to the household roster in the Cassalanter Villa conversion or make them hired agents.

### 7.4 M6: the Writ and the gold; two alternate triggers; the Jalester choice

- R m06 ev-01:76: "The gold goes to the treasury. All of it. If you come out with it and take it somewhere else, the writ is void." The Vault's Scene 6 offers five paths, one a 10% finder's fee Laeral "asks once" (`arc-j:238`; `gm-guide/design-notes-running-the-campaign.md:93`), another leaving the gold in place and drawing on it. A Writ that is "void" if the gold goes elsewhere pre-empts those paths. Recommend: the Writ never becomes void; Laeral's request is stated, and her reaction (disappointment, the 10% offer, silence) is resolved in the Vault.
- **Two different alternate triggers** in one overview: "Mission 5 failed (ledger did not reach Laeral)" (R m06 overview:10) and "the Cassalanter thread has advanced sufficiently for Laeral to seek the party out" (R m06 overview:20); G03:30 has a third ("Jalester asks them to provide direct testimony about the vault"). Pick one. Recommend: M6 is available at R13/L7 once **Kolat Towers** has run; the ledger changes only what Laeral already knows, as the Notes:28 pattern (a no-reader default) suggests.
- **Level conflict:** L7 requires all four heists (Notes:13, :30). 3-heist parties enter the Vault at L6 and never reach M6. State the no-Writ default for the Vault (`arc-j:45` assumes the Writ exists).
- **Writ and companions:** "authorizes the party by name" (R m06 ev-01:82) vs members-only briefs. Name each member and "companions they vouch for at the gate", or the Watch rule becomes unusable for a mixed party.
- **The Jalester Question** (R m06 ev-01:88-96): reads the Harper outcome by free text. Wire it to **Jalester Compromise Identified**. "She removes Jalester from active duty ... disrupts Alliance operations in the Vault" and "Jalester ... still loyal to Laeral" (Harper overview:21) need to coexist; M6 should say what Jalester does if told (steps aside, stays loyal, asks to be watched).
- **Manshoon offer** consequences are read by `arc-j:45` (delay Watch cooperation two hours / expose one Masked Lord). Keep both numbers.
- **Source:** the 4th LA arc in AppC is Ziraj; M5 and M6 are remix inventions with no source mission (AppC stops at LA-4), so M5-M6 are all design, with no source text to preserve.

### 7.5 Where Jalester sits, and how missions are delivered

- Sources of place: WDH "usually seated by himself in a quiet corner", R M1 "a table far enough from the bar", R s02 "his usual position at a table near the far wall", BD s04 "a table by the stairs", Harper M6 "beside the Yawning Portal's well", Trollskull patrons page "ordering a drink between briefing sips". **Recommend:** a table beside the well in every LA page, and say so in the First Meeting, so Harper M6's Ivara tracing makes sense and BD s04 can find him.
- Delivery: Org02:8 and NF-Jal:26 "in person"; R M2 note, R M5 courier, R M6 Watch summons. The patrons page says "verbal, no scroll". Recommend: in person at the well table for M1, M3, M4; at Trollskull for a sensitive house call (M2, M5 can be "in person at Trollskull", not by note); a summons only for M6.

### 7.6 s02 and FG s01 do the same job; neither reads the other; s02's evidence is circular

- LA s02 (R s02:9-15, :27-33): the party briefs Jalester with the Stone's holder, the vault in Waterdeep, and two confirmed villain factions; +2 once; Laeral informed. FG s01 (`force-grey/s01.../ev-01:5-11, :50-60`): the party briefs Vajra with four elements; 2 Renown once; "a sealed message on its way to the Open Lord"; **Vajra Briefed** read by Vault and Commander.
- Both set a Laeral-is-prepared state for the Vault (R s02:93 and FG s01:279). Two writers, no merge. Recommend: keep both, name them separately (**Laeral Informed by Jalester** / **Vajra Briefed**), and let the Vault read "either".
- **Circular evidence in s02:** the second requirement is "The vault is in Waterdeep ... the Stone's own revelation, Fentree's Ledger (Mission 5), or other documented confirmation" (R s02:31). The Stone reveals location only at Full Awakening (Vault Scene 1); M5 is L6. So s02 "from early Act III" (R s02:15) cannot fire before the second heist unless papers exist. FG s01's table (`:50-60`) solves it with three routes (the Stone named the sum or place, papers from a lair/outpost/Neverember household, or an enemy named the gold) and "available once the party has completed any one lair heist". Recommend s02 copy that structure (same threshold, LA's own questions).
- **Jalester "has read Fentree's notes"** (R s02:68). If s02 fires before M5, he cannot have. Drop the line or key it to M5.
- **Cassalanter rule in s02** (R s02:23, :33) is correct and should survive.

### 7.7 The leak: Jalester, Illuun, the Cassalanters

- Harper M6 gives Illuun a living contact: Jalester. `grand-game.md:34` gives the Cassalanters an "LA contact". R m05 has the Cassalanters buy the ledger. These are three unconnected facts about "information leaves the Alliance". Decide what leaks: Illuun hears everything Jalester hears (Harper M6); the Cassalanter "Alliance contact" is someone else. Keep them separate or the Cassalanters learn the vault from Illuun (an aboleth would not).
- M2-M3 (Harko and Esloon) tie to the Splinter; M4-M5 to the Cassalanters. Nothing connects M1's Xanathar leak (Delvon) to any later beat. Fine; M1's thread (Herath, the sewer) feeds Xanathar's Lair.

### 7.8 First Meeting is missing the things the rest of the set reads

- **Cloak rank** (Renown 1) is never named (R 00:25-71). Every other First Meeting names the first rank and grants Renown 1.
- **Renovation help:** `ev-04:56` and Trollskull `02-operating-costs.md:81` give a 200 gp civic grant "from Laeral's discretionary fund" with "ongoing compliance oversight". R 00 has no scene for it. The Enclave and Force Grey First Meetings have a "Renovation Help" box.
- **Ward-fee reduction** (`02-operating-costs.md:27`): "Jalester's civic designation reduces Fellowship line from 3 gp to 1 gp ... Any Watch citation resets this." Per H43, passive perks need no event, but the Cloak and the grant should be in the scene.
- **Gating:** R 00:69 says M1 becomes available once "any enrolled character reaches 2nd level"; the model says "each member who is 2nd level, and the contact briefs it".
- **Declining:** R 00:57 ("He does not approach them again") is per party; make it per character, and say a character who has not met Jalester can still meet him through BD s04's route (section 2b).

### 7.9 Rank-event interactions

- **r03 vs BD m03/DR s01** (section 2b): the 24-hour written notice vs an automatic rescue patrol; a courtesy note via "string-pulling".
- **r03 safe houses:** Castle Ward and Trades Ward, key phrase "Alliance weather" (R r03:31-33). No other faction uses Castle Ward safe houses for this; Wolf's loft is Sail Street. Fine.
- **r10 Watch Files:** informants and "classified" material (Masked Lords, Watch command) at a DC 12 Charisma (Persuasion) check (R r10:45, :53). `arc-g:37` uses it for contractor logs; arc-f/-h/-i use other perks at "renown 10+" (letter of introduction, harbor inspection, reassignment) that r10 does not grant. Those three should be rewritten to use r10's three tools.
- **r25 Masked Lord** (R r25:18, :40): "predecided ... identity never revealed to the character, to Jalester, or to the party". Harper r50 reveals Mirt as a Masked Lord (`factions/02-harpers.md:62`); Kolat Towers' ledger names five Masked Lords (`arc-i:247`). Nothing contradicts, but a party that has met Mirt, Corylus and Jelenn can guess. Decide whether the r25 Lord is one of them; recommend "never named".
- **r25 Laeral** says four sentences and leaves (R r25:60). FG r50 also has Laeral appear (`:38`, "asks the party for nothing tonight"). Two "Laeral appears and leaves" scenes; fine.
- **r50:** the commission (missing handlers and cartography team, R r50:127) vs WDMM's Runestone errand and its **Joroth Brighthelm / Falkir's Fist** errand (WDMM: Joroth is "a dwarf spy for the Lords' Alliance"). FG r50 already tells the GM Jalester hires for the Runestone. Recommend r50's commission names Joroth's team as the missing agents and mentions the Runestone as a separate Jalester errand. R r50:38 ("did not know the vault existed") needs the fix in 5.2. R r50:36 ("How diminished are you really?") conflicts with the Voice rule; either rewrite the answer or update the Voice entry to "never admits ... except to a Lioncrown who asks".
- **r50 outcome** **Undermountain Commission Accepted** is fine to keep (collision gone). Add recipient names.

### 7.10 Suspension and dismissal details

- R s01 uses "party" language in the Next Steps ("if the character is dismissed, remove their Alliance missions from the active queue", R s01:139). OK.
- "Compelling reason" definition (R s01:21-25) is thin and GM-judgement heavy ("the refusal reflects a consistent moral or practical position"). The zero-prep rule wants named triggers: which mission, which refusal. Recommend a table keyed to M1-M6 (which refusals count) in the rewrite.
- s01 only mentions Jalester delivering the suspension at Trollskull when "the rest of the party is elsewhere" (R s01:37): a party in a single Trollskull taproom (the typical situation) breaks it. Give the Yawning Portal well table as the alternate.
- R s01:19 says "Jalester said them plainly at First Meeting: assignments are not optional". A character who joined without hearing that scene (absent from the table, or enrolled later) never heard it. Add the condition to the join scene or to s01.

### 7.11 Other contradictions

- G03:13 puts the Esloon warrant "filed three years ago ... after Mission 3"; R has the file after M2 and "not active in Waterdeep".
- R m02 Harko's note: the source's coded note to "K" at the Terasse Estate (AppC:519, :546) is dropped from R. `arc-e:143-155` has the Terasse Estate as a mini-heist with three entry paths; restoring Harko's note would supply one (Keln Trigos is "K").
- R m02: "A Watch patrol arrives in four rounds" (R m02 ev-01:47), M3 Option B: "A Watch patrol responds in three rounds" (R m03 ev-01:41), M3 Option A: "within four rounds" (R :37). Settle one Watch response time for LA (Alliance members have a reason to expect the same speed in every mission).
- R m02 ev-01:47 vs BD m02: BD's Watch patrol of two **Guards** arrives in about five minutes. Not a collision.
- G03:55 Cloak "overlook minor legal infractions once per tenday" vs r03 string-pulling "Once per tenday ... Minor." Two overlapping once-per-tenday perks. Decide whether Cloak is the standing look-away and Redknife the paperwork fix, and word them differently.
- `g03:70` M6 "advice on a dangerous offer from Manshoon's Splinter" names Manshoon.
- R r10 is called "the middle rank" (R r10 Overview) while Stingblade is the third of five; harmless.

## 8. Settled facts to keep (survive the rewrite)

- **Names and roles:** Jalester Silvermane; Laeral Silverhand; Mareva Coile (45, route coordinator); Berna (dwarf, ~60, grey braid); Herath (young Calishite); Delvon Harsk (300 gp debt); Pirn; the supervisors Orryn Saltwick, Bremma Dunnet, Cass Fildura (R m01 ev-02:54); Harko Swornhold with two kenku and two bandits; Lira; Veralax; Esloon Bezant; Sarvos Miln; the "Holvar" booking; Halek Farran (cedar smell, signet turned inward); Yander Coirn ("Belvor"); Orvane Fentree (71); Rezka; Emira Volstren; Pravin Cloth; Sevel Dastar. (Rename Vhaspar, the Bent Nail and Noska's role, section 6.)
- **Places:** the Muleskull Tavern on Ship Street (Dock Ward, six bells); Shank Street; Mudwagon Row, the rope warehouse and the Wharf Mast Lane cooperage; the Skewered Dragon with the Dock Lane exit (or the Rusted Anchor if the user prefers the source); Pell Street; Copper Street; the Green Dragon Inn (rooms 3, 4, 6); Piergeiron's Palace annex.
- **Mechanics already shared with other files:** discipline is per character (G03 and Guides); rank thresholds 1/3/10/25/50; Redknife = two Guards, one errand per tenday, safe houses in Castle and Trades Wards, one string-pull per tenday; Stingblade = one introduction per quest, legal coverage for one incident per quest, Watch files with a DC 12 Charisma check for classified cases and four hours; Warduke = one Laeral audience per quest, four Warrior Veterans for one operation per quest, response-team map every three days, one anonymous Masked Lord request per quest; Lioncrown = one charge cleared, an attaché, three honest answers. The Writ terms (gate deference within four rounds; one legal intervention; Manshoon offer branches) are what `arc-j:45` reads.
- **Plot beats other files depend on:** the Vault of Dragons being located in Waterdeep (M5); Laeral's three questions and the Manshoon offer (M6); the Writ as an oath-release instrument (arc-j:166; GM guide design-notes:107); the inward-turned Cassalanter signet; Herath's note (for the Sewer Route); the Veralax/Esloon file chain as "Splinter" intelligence.
- **Titles other files cite:** *Lords' Alliance First Meeting* (BD s04, Trollskull ev-04, G03), *The Long Watch*, *The Exile's Return*, *The Red Wizard's Price*, *The Archer Above*, *Fentree's Ledger*, *An Audience with the Open Lord* (Harper M6, EE M6, GM guide), *Lioncrown* (FG r50). Do not retitle these. M1's second event and the first event's H1 can change.
- **Drop:** the `[GM]` boxes, `[!design]`, `[!profile]`, `[!lore]`, `[!narrative]`, `[!npc-narrative]`, `[!dialogue]`, the 10 True/False headings, `Milestone Overview/None`, the "Arc X" labels, the Manshoon names in player-visible text, the modified Mage, "Thug stat block, veteran training", 2014 "Veteran", Greengrass and 1244 DR, the voided Writ, and the Bent Nail.

## 9. Decisions the user will need to make

1. **M1 shape.** (a) Keep the ambush. (b) Restore the crawler on Day 9, keep the leak. (c) Both. **Recommend (b)** (section 7.1).
2. **M2 Terasse thread.** Restore Harko's coded note as an optional third path into the Terasse mini-heist, or leave the thread out. **Recommend restore** (7.11).
3. **M3 setting.** Skewered Dragon (R) or Rusted Anchor (source). **Recommend Skewered Dragon** (it is already an Act I location) with its Dock Lane exit.
4. **Esloon's backstory** speech cut to the Voice's two lines? **Recommend yes** (7.2).
5. **M4 archer's name** and whether the longshoreman target gets a name. **Recommend rename** and make the fourth target a bonus (4d).
6. **M5 buyer.** Keep Noska or replace him? **Recommend replace** with a new Guild buyer; give DR r03's ladder no change.
7. **M5 date and years.** Drop Greengrass and 1244 DR. **Recommend** "ten days ago" and a date in the last 11-20 years.
8. **M6 Writ.** Void if the gold goes elsewhere (R) or never void (arc-j:238). **Recommend never void** (7.4).
9. **M6 alternate trigger.** One condition only. **Recommend** R13/L7 after Kolat Towers (7.4).
10. **s02 evidence.** Use FG s01's three-routes table and "after any lair heist"? **Recommend yes** (7.6).
11. **First Meeting scope.** Add Cloak, the 200 gp grant and the ward-fee note. **Recommend yes** (7.8).
12. **Jalester's seat.** The well table everywhere (7.5).
13. **r03 vs BD m03/DR s01.** Add a short-notice clause to r03, or edit BD m03 (out of scope here). **Recommend** an "emergency whistle" clause in r03 (one use per tenday) so BD m03 stays valid.
14. **r50 commission.** Name Joroth's team as the missing agents, mention the Runestone separately (7.9).
15. **Laeral's decline** at Lioncrown: Voice "never admits" vs R r50:36. **Recommend** keep the admission and amend the Voice entry; this is the highest rank's payoff.
16. **Event title for M1 ev-01** ("The Tenday Watch" collides with FG). **Recommend** a new title.
17. **Cassalanter staff.** Add Halek Farran and Emira Volstren to the Cassalanter Villa roster when that quest is converted, or rename them as hired agents.

## 10. What the model reading changed

- **DR m03 and BD m02 show the event shape LA must reach.** Both open the event with a Gamemaster's Summary that says "Only [faction] members attend the brief and the debrief" and a truth box (`Who Knows What`, `What Is Actually True`) before the first scene (`doom-raiders/m03.../ev-01:3-16`; `bregan-daerthe/m02.../ev-01:3-30`). Every R LA event opens with `[GM] Gamemaster's Summary` that lists "In this Event" bullets and a "Background (DM only)" paragraph instead. The truth boxes are where the Manshoon and Cassalanter gates belong; LA has none.
- **Debrief scenes.** DR m03 ends with Tashlyn's report scene, BD m02 with the payment scene, EE m04 with Melannor's garden report. R LA has no debrief scene in any mission; reports to Jalester are only mentioned in bonus conditions ("reported to Jalester", R m02 ev-01:103; "reaches Jalester within 24 hours", R m05 ev-01:97). The rewrite needs a short Jalester debrief per mission, at the well table, that reads the mission's outcomes.
- **Per-member Renown** is stated in a `Mission Renown` block with "Companions gain none" (DR m03 ev-01:499-513; EE m04 ev-02:284). R has `**Renown:**` bullets inside `[GM]`.
- **Outcome format.** The model uses "name - when to mark; read by" and names the reader as an event title or "(unconverted)" (`doom-raiders/m03.../ev-01:519-527`; `harpers/m06.../ev-01:389-394`). LA's readers are all unconverted quests, except the in-folder M6 reads of M5 and s02/r50.
- **Rank events.** DR r03 shows the shape LA r03-r50 should take: a per-member Summary, a members-only procedure, counters (one piece of news per tenday, nights at the loft, one open order), a named contact, and `Next Steps` stating the next rank's trigger (`doom-raiders/r03-wolf/ev-01:238-249`). LA's rank events deliver each benefit as a speech but track no counters, name no recipient, and give the string-pull and escort no limits beyond "once per tenday".
- **FG m03 shows how to put a mission's two halves in two events** (the Watch, the Extraction) and how to give each member an outcome (**M3 Complete**) to gate the next mission. LA M1 already splits cleanly; M2-M6 are single events of 120+ lines each that mix investigation, combat, and a moral choice, and M3 and M6 would read better as two events (the meeting and the aftermath; the audience and the Writ).
- **Cross-faction.** EE m04 (`ev-02:304-312`) reads outcomes from Xanathar's Lair and Autumnreaver by title. LA's Faction Outposts/Cassalanter Villa readers should be written the same way, with "(unconverted)".
- **The newest lesson (H43):** passive perks need no event, but Cloak and the 200 gp grant are not passive: they are things the First Meeting hands over.
