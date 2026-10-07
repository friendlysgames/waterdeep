# Harper faction events: pre-rewrite audit

I changed nothing in the repo. Shorthand used throughout:
- `PREV` = `/tmp/claude-0/-home-user-waterdeep/6f58d0d2-f379-5140-92f5-a2193a7fb83a/scratchpad/harpers-prev`
- `R` = `/home/user/waterdeep`

Coverage:
- I read the overviews, the First Meeting, s01, r03, r10 and the opening halves of r25 and r50 in full.
- I covered the M1–M6 event pages and the Harper design notes by grep and targeted reads, not line by line.
- I did not read the restored first-commit drafts in the repo, since they are being replaced.
- `PREV` has 33 files. The repo folder has 27, because it has no design-notes for 00-first-meeting, r03, r10, r25, r50 or s01.

## 1. Outcome map

Every outcome below is written inside `PREV` and is documented in its Event Outcomes block.

| Writer | Outcomes |
|---|---|
| 00 First Meeting `ev-01:366` | **Harpers Joined** (per character, names recorded) |
| M1 `ev-01:382-386` | Maxeene Relocated, Maxeene Cover Preserved, Maxeene Identified, Vell Neutralized, Shesstra Street Reported |
| M2 `ev-01:329-340` | Harper Cipher Copied, Harper Contacts Relocated, Tessalar Turned / Arrested / Warned Off, Handler Ledger Read / Denied / Recovered / Destroyed / Collected / Burned, Fillipa Rescued |
| M3 `ev-01:340-344` and `ev-02:166-171` | Edric Identified, Edric Report Prevented, Edric Report Delivered, Edric Captured, Bonnie Harper Operative, Bonnie Neutrality Pact, Nethpranter Safehouse Reported, Harper Contacts Relocated (again), Harper M3 Complete |
| M4 `ev-01:306-307`, `ev-02:83-84`, `ev-03:176-180` | Remallia Harper Contact Known, Salon Guest Leads Recorded, BD Signal Site Observed, Erystian Cover Observations Recorded, Jarlaxle Identity Exposed at Harper Salon, Erystian Profile Reported, Mara Coppersail Recovered, Jarlaxle Discretion Agreement |
| M5 `ev-01:387-392` | Harper Mole Identified, Harper Leak Closed, Corene Rescued / Lost / Left in Place, Nihiloor False Report Confirmed |
| M6 `ev-01:263-268` | Stone Study Completed, Jalester Compromise Identified, Splinter Sending Stone Recovered, Splinter Stone Retrieval Prevented, Stone Taken by Splinter, Splinter Raid Observations Delivered |
| s01 `ev-01:171-172` | Harper Leak Known, Harper Private Protocol Adopted |
| r03 `:143` | Harpshadow Reached |
| r10 `:167` | Brightcandle Reached |
| r25 `:222` | Wise Owl Reached |
| r50 `:265-266` | High Harper Reached, Masked Lord Request Invoked |

### Outside readers and writers found by grep (campaign/, docs/, CLAUDE.md)

- **Harper M3 Complete.**
  - Read by Emerald Enclave M3: `R/campaign/quests/faction-events/emerald-enclave/m03-the-doppelganger-problem/ev-01-the-doppelganger-problem.md:16,18,136`, and `design-notes.md:7`.
  - This is the only exact-name reader in any converted quest.
- **Harpers Joined.**
  - `R/campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:97-98` still writes `#### Harpers Joined: True / False`, a retired format.
  - It claims readers in the Harpers guide, the Faction Events and Faction Outposts. The same name, with different semantics, is already the First Meeting's outcome.
- **Free-text citations that don't use the outcome name.**
  - Lords' Alliance M6 cites "Harper Mission 6" for Jalester at `lords-alliance/m06-an-audience-with-the-open-lord/ev-01-an-audience-with-the-open-lord.md:13,96` and `overview.md:28`. It should read **Jalester Compromise Identified**.
  - `R/campaign/structure/arc-j-vault-of-dragons.md:43` cites "Harper Mission 6" (see section 2).
  - `bregan-daerthe/r25-commander/ev-01-commander.md:158,326,330` has BD members naming Mirt as their Seat. It reads no Harper outcome.
- **BD notes.** `docs/plans/bregan-daerthe-research/05-ranks-and-reader-audit.md:88,152,191` and `docs/plans/harpers-out-of-scope-notes.md:375` record that **Jarlaxle Identity Exposed at Harper Salon** and **Jarlaxle Discretion Agreement** have no BD reader.
- **Unconverted lair docs.** No `arc-e` to `arc-j` file uses any Harper outcome name. This confirms `harpers-out-of-scope-notes.md:220-227`.

### Outcomes with no reader anywhere

- **Never read, though the text claims a reader.**
  - Shesstra Street Reported. Prev M1 says Faction Outposts reads it, but arc-e has no Shesstra lead.
  - Nethpranter Safehouse Reported, BD Signal Site Observed and Erystian Profile Reported. The claimed readers are Faction Outposts and Sea Maidens Faire.
  - Corene Rescued, Corene Lost and Corene Left in Place. The claimed reader is Xanathar's Lair. Arc-f has no Corene and its hook at `:426` says "three Harper assets".
  - Edric Report Delivered, Harper Leak Closed and Splinter Raid Observations Delivered. The claimed reader is Kolat Towers.
  - Stone Study Completed, High Harper Reached and Masked Lord Request Invoked. The claimed reader is Vault of Dragons. Arc-j never reads them by name.
  - Jalester Compromise Identified. Lords' Alliance M6 and the Vault read it only in free text.
  - Jarlaxle Identity Exposed at Harper Salon. The claimed reader is Sea Maidens Faire.
  - Jarlaxle Discretion Agreement. The claimed reader is "BD follow-up".
- **Claimed readers inside the Harper folder that don't read them.**
  - M2 `:331` says **Tessalar Turned** is read by s01 and M5. Neither mentions it: s01 `:67` is only generic ("Tessalar... where you left him"), and M5 has no Tessalar reference.
  - M2 `:335` says **Handler Ledger Denied** is read by M5. M5 `ev-01:99` lists only Recovered, Destroyed, Collected and Burned, so Denied is missing.
- **No reader at all.**
  - Harper Cipher Copied, Fillipa Rescued, Salon Guest Leads Recorded and Mara Coppersail Recovered. Only r25 `:95` mentions Mara, in free text.
  - Bonnie Harper Operative and Bonnie Neutrality Pact.
  - Splinter Sending Stone Recovered, Splinter Stone Retrieval Prevented and Stone Taken by Splinter.
  - Maxeene Relocated, Maxeene Cover Preserved, Maxeene Identified, Vell Neutralized and Edric Captured. Only vague "later contacts" are named.
- **Duplicate writers inside the folder.**
  - Harper Contacts Relocated is written by M2 and by M3 ev-02.
  - Edric Identified and Harper M3 Complete are written in both M3 ev-01 and ev-02.
  - Remallia Harper Contact Known is written in M4 ev-01 and ev-03.

### Other factions' state that Harper events read

- **Read by name inside `PREV`.** Only the Harper outcomes above, at `s01:31-32`, `r03:105,111,135`, `r10:159`, `m05:99` and `r50:23,55`.
- **Read as free-text campaign state.** There are no DR, BD, Lords' Alliance, Emerald Enclave, Force Grey or OotG outcome names.
  - First Meeting `:5,14`: "Renaer recommends the party", a Good-aligned trigger, and "characters who have already joined another faction".
  - s01 `:5,24`: "once the party has met Davil".
  - M4 `ev-01`: a BD helper present, and Jelenn Urmbrusk's response.
  - M5 `:309`: Xanathar Guild sites rise to at least Alert for 14 days.
  - M6 `overview:5`: "at least one Eye restored".
  - r50 `:23`: whether the Vault has resolved.
- **Gaps against the other folders' outcome names.**
  - `doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:275` writes **Davil Arrested**. The Doom Raiders s02 events write **Davil Released**. Harper s01 uses "Davil's contacts" and "Davil mentioned" and reads none of these.
  - No outcome records "Renaer recommends the party to Mirt". The First Meeting's trigger depends on that.

## 2. Inbound references and cross-document agreement

### Facts consistent across documents (keep)

- **Ranks.** Watcher 1, Harpshadow 3, Brightcandle 10, Wise Owl 25 and High Harper 50 agree across `R/campaign/guides/factions/02-harpers.md:56-62`, `players-guide/faction-affiliations.md:46-50`, `gm-guide/player-factions-overview.md:48-52`, `PREV/r03`, `r10`, `r25` and `r50`.
- **Mission levels and base Renown.**
  - Guide table `02-harpers.md:68-73`: levels 2/3/4/5/6/7, base +2/+2/+3/+3/+4/+4.
  - Prev gates: join at 2nd level, then Renown 3 and 3rd level, 5 and 4th, 8 and 5th, 10 and 6th, 13 and 7th. These match the Doom Raiders pattern.
  - Calibration matches CLAUDE.md. All Harper events say "awards no Milestone Points" (no violation).
  - Base totals 19 including the join, so every gate is reachable on base awards alone.
- **House Ulbrinter.** Delzorin Street, North Ward, between Vhezoar Street and Brondar's Way. This is in `PREV/m04/overview:17`, `R/sources/Appendix_C_-_Player_Faction_Missions.md:328` and NF Remallia. The Session 37 fix is intact.
- **Remi's lodging.** The Watcher safe house at 12 Delzorin Street is separate from the villa (First Meeting `:314`).
- **Individual membership.** The prev First Meeting is per character (`:14`, `:302`, `:366`). Rank events and s01 are members-only.
- **Corene.** Four months undercover in the Dock Ward (NF Corene, `PREV/m05/overview:21`).
- **Mattrim.** "Two years" at the Portal (NF Mattrim `:12,22`, voice profile, `PREV/m03`).
- **Maxeene.**
  - She speaks Common through a druid's permanent enchantment and is a Beast with Intelligence 10.
  - Prev M1 uses the Harper-friendly druid and a draft horse, matching NF Maxeene `:6`.
  - Her sun-elf and half-orc passengers are cameo Davil and Yagra, matching Appendix C line 104 ("matches Davil Starsong and Yagra Stonefist"). The session-37 handoff supports this (Maxeene as a Harper asset).
- **Oswin Bell.** Courier renamed from "Oren" so he can't be confused with Orren Vale (`PREV/r50:129`).

### Contradictions between the Harper rewrite inputs and other documents

**Remallia's identity and first appearance**
- `PREV/00-first-meeting/ev-01:314` and the Harper org page `:7,23` say Remi neither appears nor signs anything before M4.
- Contradicting that:
  - `trollskull-alley/ev-04:91` and `structure/arc-b:149,294` have Remallia name Filthy Meg in Act I.
  - `act-ii/fireball/ev-02-the-house-of-inspired-hands.md:96` and `structure/arc-c:121` make Remallia the Harper who knows the Gond high priest.
  - `guides/trollskull-manor/03-staff-and-hiring.md:84` has Threestrings feed Remallia.
  - NF Remallia `:8` lists "Trollskull Alley, Fireball!" as appearances.
- Resolve this by defining her public noble identity versus her Harper identity.

**Guide 02, First Meeting summary** (`02-harpers.md:37`)
- It says "two theater tickets" and that Mirt presses the pin "into the nearest open hand".
- Prev is one ticket per candidate and one pin per accepting character (`design-notes:5`).

**Guide 02, mission summaries**
- `02-harpers.md:71` says "House Haventree". The events and sources say House Ulbrinter.
- `:70` says "Only their leader Bonnie passes scrutiny". Prev M3 leaves four colleagues plus Bonnie, and offers Bonnie a choice.

**Guide 02, response-team warning** (`02-harpers.md:12`)
- It gives advance response-team warning at "Renown 15+". No rank sits at 15, and Wise Owl's warning (`r25`, priority-target) is a different thing.

**Guide 02, Wise Owl row** (`02-harpers.md:61` and `players-guide/faction-affiliations.md:49`)
- The players' guide says informants give "one specific intelligence request each per quest". The Harper guide has no per-quest limit.
- Prev r25 `:98` lets a member keep trying new specific requests after an answered one. All three sources disagree.

**Guide 02, Outposts hook** (`02-harpers.md:30` and `structure/arc-e:495`)
- Both say "Renown 30+". Harper ranks are 3/10/25/50 only.

**Renown thresholds in structure docs versus ranks**
- `arc-f:31` (a Harper distraction at Renown 10+), `arc-g:35` (a Harper operative at the ball at Renown 10+), `arc-h:33` (an informant embedded in the Faire at Renown 10+, DC 13) and `arc-i:33` (a 48-hour surveillance rotation at Renown 10+).
- In prev the matching services sit at different ranks. Prev r25 `:43-44` gives the distraction and documents at Renown 25, and the Faire informant Canvas at Renown 25. Prev r10 gives one Spy per quest and a requisition.
- Arc-h/arc-g/arc-f/arc-i thresholds and mechanics don't match.

**Arc-j `:43` versus Harper M6**
- It says Mirt "already had his three days with the Stone before the third Eye was seated" and adds a Renaer branch. Prev M6 `overview:5` is Renown 13 and 7th level, with "at least one Eye", and `ev-01:26` says "Renaer never takes his place".
- At 7th level the party has finished all four heists (Kolat Towers is always one), so the Stone has three Eyes. That makes arc-j wrong, or the M6 gate wrong.
- This is also the Vault level conflict: 3-heist parties enter the Vault at 6th level, but M6 is 7th level.

**Arc-f `:31,91,426` versus the Harper material**
- Thorvin has been a Harper informant for six years (arc-f `:31,91`). NF Thorvin (`xanathars-guild/07-thorvin-twinbeard.md:22`) says three years.
- The arc-f hook says "three Harper assets" were compromised. Prev M5 has one (Corene), and Thorvin is watched by a gazer but not occupied.

**Cassalanter secrecy**
- `arc-g:531,537` says the Harpers "hold documentation of the Cassalanters' infernal contract" and Vajra holds "provenance, specific terms". This breaks R2, and contradicts the prev tone (M4 `design-notes:15`, r50 `:159`, `PREV/00:260`).
- `act-ii/fireball/ev-01-the-fireball.md:194` and `guides/factions/02-harpers.md:28` have Mirt telling a Harper "the Cassalanters funded the Howling Hatred cult". Order of the Gauntlet s02 `:11` reads this as Trigger B.

**Manshoon gate, outside the folder**
- `act-ii/fireball/ev-06-the-death-mark.md:68`: at L3, Mirt says "Manshoon has placed double agents in the network".
- `guides/factions/02-harpers.md:19,22,48,61` and `setting/organizations/01-harpers.md:6,17,19` name Manshoon, a clone, and Kolat Towers for the Harpers.
- This contradicts the rule that Harpers know only "the Black Network has split" (prev r03 `:117-121`).

**Doom Raiders s01 dependency**
- Harper s01 requires "the party has met Davil" and talks about "Davil's contacts" seeing the leak. Davil is arrested on Ches 26 (`davils-arrest ev-01:5,275`) and released in s02. Nothing in prev reads **Davil Arrested** or **Davil Released**.

**Emerald Enclave M3 versus Harper M3**
- EE `ev-01:147,151` and `overview:16-18,22-23` have five doppelgangers, with the traitor sold to Kelso Fiddlewick, and Bonnie's crew leaving Waterdeep within two tendays.
- Prev M3 has a six-person crew (Bonnie, Edric, Kael, Syla, the Scholar and the Merchant), with Edric reporting to Beldan Rusk's customs-house channel. It also offers Bonnie a Harper role or a neutrality pact that keeps the crew in the city.
- NF Bonnie and the voice profile say "five" crew.
- EE `design-notes:13-15` says Kelso is the Splinter buyer across EE, DR and OotG M3.

**NF Bonnie**
- It says she is "one of the three keys required to open the Vault of Dragons" (`04-bonnie.md:26`). Arc-j opens the vault with dragonscale, sunlight and a mithral hammer.

**Mirt's statistics**
- NF Mirt (`01-mirt.md:6`) lists "Veteran (with modifications)".
- Prev r50 `:91-93` uses "his CR 9 statistics from the mechanics reference and not a generic Veteran" (HP 153, AC 16), and M6 overview `:60` says "CR 9 contribution".
- That reference no longer exists (below).

**Threestrings labels**
- `guides/trollskull-manor/03-staff-and-hiring.md:84` calls him "Harper-adjacent" and CG. NF is "Harper spy, lawful good". CLAUDE.md requires "Harper agent".
- NF Mattrim `:26` calls the doppelganger assessment "Harper mission four". It is Mission 3.
- NF Mattrim "Featured in" omits The Dead Drop's Mirt-related events. NF Bonnie "Featured in" omits The Dead Drop.

**Corene's timeline**
- Guide `02-harpers.md:72` says missing "three tendays" (30 days).
- Org page `01-harpers.md:31` says compromised "three tendays before Mission 5".
- NF Corene `:22` says shifted "three weeks ago".
- Prev M5 `overview:21` has the last check-in three weeks ago and implantation twelve days ago.

**Trollskull financing**
- `trollskull-alley/ev-04:55` and `guides/trollskull-manor/02-operating-costs.md:80,94` have Mirt's personal loan of 500 gp "once contact is established".
- Prev First Meeting `:158,296` offers no loan and no assignment.
- Operating costs `:26` adds "Harpers (Renown 3+): Mirt arranges −1 gp/tenday". Prev r03 grants no such thing; it grants a 10% supplier discount at three shops.

**Trollskull Parades** (`ev-07-the-twin-parades.md:51`)
- "A Harper contact has two opera tickets going unused and hands one to an enrolled party member". Prev uses a paper bird and the Lightsinger Theater.

**Gralhund Villa**
- `ev-01-what-the-factions-say.md:19-21,85` writes "Mirt Brief Received: True / False".
- `ev-03b-the-front-door.md:33` has "a Harper identification card" carry weight. Prev gives a pin, a key and an address card only.
- `ev-09-aftermath.md:109` has Mirt's note ("I heard Saerdoun Street was lively"). Prev s01 puts Harper rooms on Saerdoun Street too (the Gralhund Villa street): `s01:14` (No. 6), `s01:33,83` (No. 14), `m05 ev-01:43` (No. 22).
- The Gralhund briefs fire for all, with no members-only gate (also in the notes at `:206`).

**Fireball overview** (`act-ii/fireball/overview.md:35`)
- It calls Renaer "Harper contact". NF Renaer `:26` says "Harper-adjacent ally".

**Wards and addresses**
- Prev r03 `:51` and r50 `:53` put Shield Street (a barber at No. 3, a cartwright at No. 6) in the Castle Ward. WDH (`R/sources/adventure-wdh.json:1087`) puts Shield Street in the Sea Ward (Rosznar Villa).
- BD Signal Site in M4 `ev-02:83` is 4 Shield Street, next door to Bram Pell.
- Candle Lane (`PREV/m01`, `Hessa Dorn` stables) is also the Dock Ward Zhentarim warehouse street in Finding Floon (`ev-03-zhentarim-warehouse.md:7`).
- Felzoun's Folly is "two streets from" Uza's shop in `PREV/m02/overview:17`, but WDH/App C put it on the corner of Sorn and Salabar. Hence "Sorn Street" is the shop's street and the tavern's too.

**Name collisions**
- Saeth Cromley appears as a salon guest in M4. He is the City Watch sergeant in Fireball (`ev-01-the-fireball.md:37,80`; WDH Veteran, LG).
- Harl Keen (courier, r25/r50) shares a first name with Harl Pimm (BD s02/m05).
- Joss Bell (r25) and Oswin Bell (r50) share a surname. Bram Pell (r03) is a near-match.
- Ilen Castor and Ilmra (DR/BD) are near-matches.

**Timing**
- M4 says Jarlaxle has attended Remi's parties as Erystian Demarne "for three months" (`overview:21`).
- The BD session notes say arc-h `:9` has Jarlaxle arriving in the last tenday of Ches, and s02 treats BD as being in the city "for months" (`harpers-out-of-scope-notes.md:505`).

### Conflicts between Harper input and BD/EE/OotG/LA

- **Jarlaxle's name.** Prev M4 has Jarlaxle admit "he belongs to BD" (`ev-03:32`) and writes **Jarlaxle Identity Exposed at Harper Salon**. BD gates his name on **Jarlaxle Unmasked** (BD notes `:361`), which nothing writes. BD teaches the BD name in s02.
- **Cross-faction Renown.** Prev M4 awards "+1 Bregan D'aerthe Renown" inside a Harper mission (`overview:41`). No BD event reads it, and BD guide 08 doesn't list it as an award source.
- **Jalester.** Lords' Alliance M6 and Emerald Enclave M6 (`ev-01-the-dreamers-reach.md:169`) both name Illuun. In prev M6 Mirt names Illuun through Ivara's study.
- **Force Grey s01** (`force-grey/s01-the-full-picture/ev-01-the-full-picture.md:121`). It cites "Harper Mission 2 — The Dead Drop" by title, which matches.

## 3. Standing-rule check

**Violations in `PREV`**
- **Manshoon gate (R1).** Prev uses "Manshoon Splinter" and "Manshoon's cell" in overviews and GM text. No Harper NPC says it in speech, with one exception.
  - Overviews and character lists: `m01/overview:23,54`, `m03/overview:21,56`, `m05/overview:23,56-57`.
  - GM-only secrets: `m01 ev-01:16`, `m02 ev-01:16`, `m03 ev-02:20`, `m05 ev-01:71`, `s01:24` and `s01:153`.
  - Speech: `m06 ev-01:213-215` has Manshoon himself replying "Bring the Stone to Kolat's outer gate". M6 `:197` says a follower can reveal Kolat Towers as the destination.
  - There is no use of **Manshoon Named**, which DR adopted (`harpers-out-of-scope-notes.md:246`).
  - M6's Kolat references are also timeline-inconsistent: a 7th-level party has already finished Kolat Towers.
- **Mirt's speech about the split** is correct: `r03:121` ("The Black Network has split, that much I know").
- **Jarlaxle** (see section 2).
- **No Lolth content** in prev (grep found none), and none for **Cassalanter infernalism** presented as knowledge: M4 `design-notes:15`, `ev-01:258`, `ev-01:224,230`, r50 `:159,171` and M3 `ev-02:116` all hold suspicion only.
- **Threestrings** is labelled a Harper throughout `PREV`. The mislabelled instances are in the Trollskull staffing table.
- **Individual membership.** Prev passes. Remaining guide problems:
  - `guides/factions/01-overview.md:7` and `players-guide/faction-affiliations.md:3` still say a PC can hold several memberships.
  - Guide 02 `:45` and NF Mirt `:26` use "the party".
- **Milestone Points.** None awarded in `PREV`.
- **Escalation tiers.** Only "Alert" is used (`m05 ev-01:309`, `overview:48`), and it's a valid tier. No invented tier names.
- **Finding Floon "last night".** Not referenced in `PREV`. Out-of-folder: `finding-floon/overview.md:49` ("two nights before") is a separate problem listed in the notes (`:200`).

## 4. `docs/plans/harpers-out-of-scope-notes.md` Harper-touching items

The file has 580 lines. It starts with Harper-run notes for Sessions 35–37, then adds Doom Raiders (Session 38) and BD (Session 39–40) sections.

### Open Harper-relevant items (all still unfixed)

- **`:7-11` R1 gate and reveal timing.** The name appears at the Interrogation House (arc-e `:193,211`), identity at Kolat Towers, motivation at the Vault. Status: DR adopted **Manshoon Named** (`:246`); Harper has not.
- **`:132`.** `02-harpers.md:48,30` (M); `:61` (T, informants in "Manshoon's Splinter"). Open, confirmed.
- **`:142`.** `organizations/01-harpers.md:6,17` (V). Open, confirmed.
- **`:160`.** `02-harpers.md:28` Mirt and the Howling Hatred (R2 T). Open.
- **`:166-168`.** One PC in several factions: `factions/01-overview.md:7,9`, `players-guide/faction-affiliations.md:3`, `gm-guide/player-factions-overview.md:3`, `trollskull-manor/02-operating-costs.md:31`. Open.
- **`:179`.** `02-harpers.md:45` and NF Mirt `:26` (R3 M). Open.
- **`:185`.** NF Mirt `:26`. Open.
- **`:191`.** Double-agent warning after M4 (`:11`) versus exposure in M5 (`:22`). It's recorded as an inconsistency, but the prev design (s01 after M4, M5 exposes) makes the guide correct.
- **`:202`.** Trollskull ev-04 `:83-87` (R1 V), `:97-98` (retired flag). Open.
- **`:204-205`.** Fireball ev-01 `:194` (R2 T), `:192,196,200,88` (R3 M); ev-06 `:68` (R1 V), `:53` (Yellowspire placement). Open.
- **`:206-207`.** Gralhund ev-01 briefs with no members-only gate, and ev-09 `:115`. Open.
- **`:212`.** arc-e `:83,87,91,351,371,377,379` (R1), `:495` (R3 M, and "Renown 30+" matches no Harper rank). Open.
- **`:213-217`.** arc-f `:27,214`; arc-g `:531,537` (R2 V); arc-h `:29`; arc-i `:43,93`; arc-j `:49,51`. Open.
- **`:219-227`.** Harper outcomes that name readers that don't read them (list in section 1). Open until each lair doc is converted. Includes the Vault level conflict (Harper M6 needs L7, but 3-heist parties enter at L6).
- **`:375`.** BD reads neither **Jarlaxle Identity Exposed at Harper Salon** nor **Jarlaxle Discretion Agreement**; BD also hasn't taught the BD name yet. Open.
- **`:376`.** The same point with the BD decisions 1 and 3 below. Open.
- **`:548-552`.** Decisions 2–5 (Zord cover, Fireball ev-04's **Jarlaxle Unmasked**, BD per-member wording, Renown 25/50 sources). Open; decision 3 touches the Harper M4 exposure ("the Harper M4 exposure stays unrelated" if no).
- **Session 40 handoff** (`R/session 40 handoff.md:95,148,155`).
  - Run a clarity pass over Harpers under the new ranges (they were drafted under the old floors).
  - Wire the Harper outcomes into their readers.
  - Give the minor Harper NPCs voice profiles. The Session 37 handoff lists Uza, Tessalar, Orren, Harl Keen, Nella, Orin and others.
  - The Harper private phone Site is stale.

### The six "Decisions Needed Before Fixing" (`:231-238`) and status

1. **Do villain factions count under R1 and R2?** Partly answered. Jarlaxle knows the Cassalanters through Vessa (`:548`). The Xanathar–Manshoon and Jarlaxle–Manshoon knowledge are unresolved.
2. **Should the Manshoon reveal become a hard gate?** Answered in effect. The user adopted **Manshoon Named** for the DR run (`:246`, and `:384`). Harper still lacks it, and Faction Outposts still owes the writer.
3. **Which act owns the first Cassalanter cult evidence?** Open. A third owner appeared with BD (`:397`).
4. **OotG M5/M6 pact terms.** Open.
5. **BD Contact Severed per PC or party-wide?** Answered (per member, `:363`).
6. **Level gates that contradict readers** (Harper M6, DR M6, Force Grey M6, EE M5). DR M6 was resolved by moving **Force Field Gap Intel** to M5 (`:247`). Harper M6 (L7 versus the L6 Vault and the Kolat reader), Force Grey M6 and EE M5 remain open.

The decisions at the end of the file (`:546-552`) are the five BD-related ones: decision 1 answered, decisions 2–5 open. The six decisions above sit mid-file at `:231-238`, not at the end.

## 5. Conventions Doom Raiders and Bregan D'aerthe use that the Harper rewrite must match

The DR brief at `R/docs/plans/doom-raiders-conversion-brief.md:26-75` is the spec, derived from the earlier Harper files. Session 40 changed the prose ranges.

- **Voice ranges (CLAUDE.md, `ember-voice` section 2a):** readaloud 17–21 words per sentence, GM text 15–20, speech 11–15, at most two clauses chained. Run `voicecheck.py`. The old "average 12+ speech, 18+ narration" in the DR brief is superseded.
- **Page shape.** Event pages: `# Title` (no "Mission N" prefix); `Gamemaster's Summary` ("This Social Event occurs when…"); descriptive scene headings; `Renown Opportunities`, `Aftermath`, `Concluding the Event` with `Event Outcomes` and `Next Steps`; then `## Overview` and `## Summary`. Overview pages follow the `Quest Requirements` → `Difficulty` → `Milestone Progression` → Hook … Involved Characters → Dangers & Enemies shape (compare `doom-raiders/m01.../overview.md`). Prev already matches this.
- **Outcome format.** `- **Name** — when to mark it; read by **Reader**.` No "Award X" language and no True/False flags. Per-member outcomes say "mark with the recipient's name" (see `doom-raiders/r03-wolf/ev-01-wolf.md:244` and `PREV/r03:143`). Joined outcomes follow `Doom Raiders Joined` / `Bregan D'aerthe Joined` / `Harpers Joined`.
- **Membership.**
  - Gate text reads "when an individual Harper member reaches Renown N". Prev matches. The Harper rewrite must keep it.
  - Briefs and debriefs are members-only. Jarlaxle's debrief to any party that dealt with him is the sole exception.
  - Companions get no Renown or rank. Rank benefits are tracked per PC with a written procedure.
- **Gates.** Join at L2, then Renown 3 and L3, 5 and L4, 8 and L5, 10 and L6, 13 and L7 (matches DR, `doom-raiders-conversion-brief.md:280`).
- **Renown block.** "Each participating Harper member gains N base Renown" and "+1 Renown: condition", each bonus once. Bonuses are explicit conditions only.
- **Manshoon gate.** DR gates every use of "Manshoon" and "Kolat Towers as his home" on **Manshoon Named** (`doom-raiders/m05.../ev-01:27`, `ev-02:25`; `r50-dread-lord`; `s02`). Until then they say "the other cell", "Floxin's cell" (only when **Floxin Status** is Alive) or "the Splinter". The Harpers have no Floxin belief. They should say "the Black Network has split" or "the Splinter" until **Manshoon Named** is marked.
- **BD gating.** Jarlaxle's name only in speech or readaloud when **Jarlaxle Unmasked** is marked. Soluun and Kreb have similar gates.
- **No Lolth worship.** BD members speak of her with contempt.
- **Design notes.** `# Design Notes: Title`, then 3–4 short sections: rationale, source departures, and an "Invented Names and Open Items" section (`doom-raiders/r03-wolf/design-notes.md:15`; `r10-viper`). Prev Harper notes have none of the latter. Six folders have no design notes at all in the current repo.
- **Fights.** Ordinary 2024 stat blocks in `[!hazard]` with "X's Tactics", a surrender or retreat condition and a non-combat route. No boss blocks and no phases.
- **Mechanics reference.** DR and BD each have `docs/plans/<faction>-mechanics-reference.md`. Prev Harper files cite a "Harpers Mechanics Reference" (`m02/overview:10`, `m03/overview:10`, `m05/overview:10`, `m06/overview:10`, `r50:91`, `m05 ev-01:233`), but no such file exists in the repo.
- **Cross-faction NPCs.** DR/BD voice minor NPCs from the event text and list them in design notes. They don't have Notable Figures pages. BD and DR also avoid award text on other factions' Renown.

## Prioritized list

### (a) Facts the rewrite must keep

1. One Harper path: Harpers Joined recorded per character; Watcher at Renown 1; pin, key and address card; 12 Delzorin Street lodging; "I am almost never home".
2. Mission order, titles, levels and gates: The Talking Mare, The Dead Drop, The Doppelganger Auditions, A Friend's House, The Sleeping Asset and The Stone's Other Master, at Renown 0/3/5/8/10/13 and L2–L7, base 2/2/3/3/4/4. Ranks stay at 1/3/10/25/50.
3. Remallia's Harper identity stays hidden until M4. House Ulbrinter on Delzorin Street, North Ward.
4. Mattrim "Threestrings" Mereg is a Harper agent, two years at the Portal. Orren Vale is a records clerk who leaks to Beldan Rusk, 48 hours behind the entry (GM-only, with Mirt saying "a couple of days"). The Sleeping Asset closes it. Oswin Bell is the courier (not Oren).
5. Maxeene speaks Common via a druid's enchantment. The sun-elf and half-orc passengers are cameo Davil and Yagra.
6. Uza Solizeph, Sorn Street, Trades Ward, and Felzoun's Folly. Fillipa, the gazer, and the Tessalar-and-ledger branch.
7. Corene Wyldath, four months undercover as Halla Ironstave in the Dock Ward, with Nihiloor's custom parasite.
8. Jalester Silvermane is always the psychic contact, never Renaer. Jarlaxle appears as Erystian Demarne and does not reveal Zord.
9. No Harper event awards Milestone Points. Alert is the only escalation tier used. No Lolth content.
10. Suspicion-only handling of the Cassalanters at the salon.
11. Existing outcome names that a reader already cites: **Harper M3 Complete** (EE M3), **Harpers Joined**, **Jalester Compromise Identified**, **Jarlaxle Identity Exposed at Harper Salon**.

### (b) Contradictions to fix inside the Harper folder

1. Add a **Manshoon Named** gate to Harper speech and readaloud, and strip "Manshoon" and "Kolat Towers" from player-visible Harper text (M1/M3/M5 overviews and character lists, M6 `:197,213-215`).
2. M6's gate (L7, all four heists done) conflicts with its own reader and with Kolat Towers: it reads "at least one Eye", and the Mage escapes to Kolat. Decide the level and reader before drafting.
3. M5's reader gap: Xanathar's Lair is a heist that may already be done by L6, and the M2 `Handler Ledger Denied` branch is not read by M5.
4. Three different Corene timelines (30, 21 and 12 days), and the "five" versus "six" crew count.
5. Duplicate outcome writers (Harper Contacts Relocated, Edric Identified, Harper M3 Complete, Remallia Harper Contact Known). Pick one writer each.
6. Claimed readers that don't read: Tessalar Turned (s01/M5), Handler Ledger Denied (M5), and the outcomes with no reader.
7. Cross-faction Renown inside M4 (+1 BD) and BD-name use by Jarlaxle before the name is gated.
8. Mirt's stat block (CR 9 versus Veteran) and the missing Harpers Mechanics Reference.
9. s01 depends on Davil without reading Davil Arrested / Davil Released.
10. Name collisions: Saeth Cromley, Harl (Keen/Pimm), the two Bells.
11. Shield Street ward (Castle versus WDH's Sea Ward), Candle Lane reuse, and the Felzoun's Folly location.
12. Design notes missing for six folders, and no "Invented Names and Open Items" in any.
13. Apply the Session 40 clarity ranges: prev was drafted under the old floors.

### (c) Out-of-folder contradictions to log

1. Guide 02: `:12` (Renown 15+), `:30` (Renown 30+), `:37` (two tickets), `:71` (House Haventree), `:70` (Bonnie alone), `:72` (three tendays), `:28` and `:48,61` (R2/R1), `:45` (the party).
2. Org page `01-harpers.md:6,17,19,31` (Manshoon, Kolat Towers, "three tendays").
3. NF pages: Mattrim `:26` (mission four), Bonnie `:8,22,26` (featured-in, "five", vault key), Mirt `:6,26` (stat block, the party), Maxeene `:8,22`, Remallia `:8`, Corene.
4. Trollskull: ev-04 `:55,71,83-87,91,97-98`, ev-07 `:51`, guide `03-staff-and-hiring.md:84`, `02-operating-costs.md:26,31,80,94`.
5. Fireball: ev-01 `:192-200`, ev-02 `:96`, ev-06 `:68`, overview `:35`. Gralhund: ev-01 `:19-21,85`, ev-03b `:33`, ev-09 `:109`.
6. Structure docs: arc-e `:495`, arc-f `:31,91,426`, arc-g `:531,537`, arc-h `:33,101`, arc-i `:33`, arc-j `:43`.
7. Emerald Enclave M3 (crew size, departure, Kelso as handler). Lords' Alliance M6 (free-text Harper Mission 6). BD (no reader for the two Jarlaxle outcomes). Doom Raiders (no reader for Davil Arrested/Released in Harper s01).
8. Players' guide and GM guide multi-faction wording; the "Informants one request each per quest" wording at `faction-affiliations.md:49`.

### (d) Open user decisions

1. Does the Harper rewrite adopt **Manshoon Named**? Faction Outposts must also write it; the Harpers currently know the name from the guide, org page and Fireball ev-06.
2. M6's level gate and Eye count: keep L7 (all four heists, three Eyes) or move it earlier, which changes arc-j `:43`.
3. Remallia's public versus Harper identity: may she appear in Act I and Fireball as a noble, or is she hidden entirely until M4?
4. Is Jarlaxle's name taught in M4 (a Harper outcome) or gated on **Jarlaxle Unmasked** (BD decision 3, still open)? Does M4 still award BD Renown?
5. Bonnie: five or six doppelgangers, and does Emerald Enclave M3 (departure, Kelso) or the Harper M3 (neutrality pact or operative) win?
6. Does Mirt use CR 9 statistics (r50, M6) or the NF Veteran? Recreate or retire the missing Harpers Mechanics Reference.
7. The Harper informants' threshold: Renown 10 (arc-f/g/h/i) or 25 (prev r25), and one request each per quest or repeatable.
8. Which act owns the first Cassalanter cult evidence (decision 3), and whether arc-g `:531,537` may keep "Harpers hold documentation".
9. Villain-faction knowledge under R1 and R2 (decision 1, partly answered).
10. Invented names to accept or replace (Perrin Valt, Evin Talver, Nella Fen, Orin Dask, Bram Pell, Ilen Castor, Dena Voss, Joss Bell, Darron Quill, Della Morn, Harl Keen, Ivara Dunn, Lysa Fenwick, Teren Moss, Hessa Dorn, Orvel, Beldan Rusk, Vell, Edric Tanner, Kael, Syla) and whether any should get a voice profile or Notable Figures page.
