# BD conversion spec: research report (read-only)

Paths are relative to `/home/user/waterdeep`. `Brief` is `docs/plans/doom-raiders-conversion-brief.md`. `DR` is `campaign/quests/faction-events/doom-raiders`. `BD` is `campaign/quests/faction-events/bregan-daerthe`. `OOS` is `docs/plans/harpers-out-of-scope-notes.md`.

Two points on method. I read the finished DR files that carry each convention below, not all 26. Plan mode was on, so I wrote nothing.

## (a) Confirmed spec, plus conventions the DR files use that the brief omits

The brief's shapes hold against the finished files.

- **Event page.**
  - It opens with a plain `# Title` and a `[!gamemaster]**Gamemaster's Summary**` that starts "This Social Event occurs when…" and ends "In this Event, the party can:" (`DR/m03-the-missing-snobeedle/ev-01-the-missing-snobeedle.md:1-14`).
  - The sections run `### Renown Opportunities`, `### Aftermath`, `### Concluding the Event`, then Event Outcomes and Next Steps (`m03 ev-01:433-526`).
  - The event closes with `## Overview` and `## Summary` (`m03 ev-01:528-534`).
- **Overview page.** `# Title: Overview`, `Quest Requirements` with `#### Difficulty` and `#### Milestone Progression`, then Hook, Background, scene sections, Renown Opportunities, Aftermath, Involved Characters, Dangers & Enemies and a closing `## Overview` (`m03 overview.md:1-76`).
- **Design notes.** Three or four `##` sections (`m03 design-notes.md`; `r25-ardragon/design-notes.md`). The last section is always "Invented Names and Open Items" or "Out-of-Scope Notes".

Conventions the DR files actually use that the brief does not state:

1. **Gate phrasing in Next Steps** (the brief says only "states the member-specific gate").
   - "**Silencing Skeemo** becomes available when an individual Doom Raiders member reaches Renown 8 and 5th level." (`m03 ev-01:524`)
   - "becomes available to each Doom Raiders member who reaches Renown 13 and 7th level" (`m05 ev-01:423`)
   - Rank events name the next rank instead: "**Viper** occurs when this member reaches Renown 10" (`r03 ev-01:249`).
   - First Meeting: "becomes available to each Doom Raiders member who is 2nd level, and Davil briefs it to them in person" (`00-first-meeting ev-01:420`).
2. **Quest Requirements gate sentence.** "Available to a Doom Raiders member at Renown 5 and 4th level after **The Poisoned Delivery** and **Davil's Arrest**. Companions can join…" (`m03 overview.md:5`).
3. **Renown is stated twice.**
   - The event has a `[!gamemaster]**Mission Renown**` block: "Each participating Doom Raiders member gains 3 base Renown… Companions gain none." Bonuses follow as "- **+1 Renown:** condition" (`m03 ev-01:493-499`).
   - The overview repeats it in prose (`m03 overview.md:53`).
   - The debrief readalouds sit inside `### Renown Opportunities` (`m03 ev-01:433-499`).
4. **Rank events have no overview.md**, only `ev-01` plus `design-notes.md`.
   - Renown Opportunities reads "The rank event awards no Renown" (`r03 ev-01:232`; `r50 ev-01:312`).
   - Outcomes read "mark with the recipient's name" (`r03 ev-01:244`).
   - Per-member counters are listed in the outcome text: last news request, loft nights, open order (`r03 ev-01:244`).
   - An outcome defined elsewhere is "defined in **Davil's Arrest**, and this Event only sets it" (`r03 ev-01:245`).
5. **Outcome line shape.** `- **Name** — mark when…; read by **Reader**` (`m03 ev-01:515-520`). "(unconverted)" is appended to unconverted readers (`m03 ev-01:516, :519`).
6. **GM context blocks sit before the first scene.** They are named "What Is Actually True" or "Who Knows What" (`r03 ev-01:22-24`; `m03 ev-01:16-18`). Summary sub-heads are allowed: `#### Candidates and Companions` and `#### What Nobody in This Event Knows` (`00-first-meeting ev-01:13-25`).
7. **Gate wording for Manshoon Named and Floxin Status** has three recurring forms.
   - A GM block: "Until **Manshoon Named** is marked, every Doom Raider says 'Floxin's cell', 'the other cell' or 'the Splinter'" (`m05 ev-02:25`; `m05 ev-01:27-28`).
   - Paired readalouds: "If **Manshoon Named** is not marked, read or paraphrase the following… If … is marked, … instead" (`m05 ev-01:50, :58`).
   - A one-line substitution: "he says 'the other cell' in place of 'Manshoon's cell', whatever **Floxin Status** is" (`r25 ev-01:170`). A related example is "he adds 'Floxin's cell' only if **Floxin Status** is Alive" (`r03 design-notes:7`).
8. **Per-member renown wording.** "Each participating Doom Raiders member gains N base Renown for [specific act]" (`m05 ev-01:387`; `m04 ev-03:184`). The First Meeting sets "Renown 1 with the Fang rank" (`00-first-meeting ev-01:304`). A standalone event with no base reads "This Event awards no base Renown. Each participating … member who completes an approach… gains 1 Renown, once" (`s01 ev-01:255`).
9. **First Meeting recording.** "Doom Raiders Joined — mark for each character who accepts… and record the character's name" (`00-first-meeting ev-01:416`). Declining and deferring are written as readalouds (`:316-324`). A late joiner is recorded under the same outcome (`:420`).
10. **Social blocks use two stock phrasings.** "Conversation topics X is willing to discuss include:" (`m03 ev-01:48`) and "X is happy to discuss the following topics:" (`r03 ev-01:64`). Pick one per folder.
11. **Hazard block shape** (`m03 ev-01:371-385`).
    - It names the 2024 creature and cites the Mechanics Reference by name, with "no added phases or extra Hit Points".
    - `#### The Shard Shunners' Tactics`, then "During combat, the Shunners:" bullets.
    - End conditions, then a check-based de-escalation with a stated failure.
    - Hazards are used for ambushes and for "If the Party Grabs the Coach" (`m02 ev-01:256`).
12. **Summary is first-person plural** ("We spent three days…", `m03 ev-01:534`). It may carry `###` variants for branches (`00-first-meeting ev-01:430-436`).
13. **Inconsistency in the finished DR files.** The brief does not mention it. Speech inside readalouds is written without quotation marks in r03, r10, s02 and m06 (78 lines matching `^> > [^"]`; example `r03 ev-01:34`). m03, the First Meeting, r25 and r50 quote it (`m03 ev-01:28`). A BD brief should pick one. The quoted form matches the Harper and first-pass DR style.
14. **Mechanics reference.**
    - The CR 2.0 numbers come from `docs/plans/doom-raiders-mechanics-reference.md`, built with XMM and XPHB records.
    - It lists only Scout, Bandit, Tough, Warrior Veteran, Spy, Assassin, Mage, Mage Apprentice, Priest, Priest Acolyte, Wererat and Giant Rat. A BD mechanics pass must verify each new creature itself.
    - "Thug and Veteran do not exist in XMM" (reference l.13).

### BD drafts: items the spec must fix

The BD files are in the old pre-Ember format.

- **Retired blocks and headings.**
  - `> **[GM]**` zones (`BD/00-first-meeting/ev-01-first-meeting.md:3`).
  - `[!profile]` (`:25`).
  - `#### X: True / False` headings (`:99, :103`).
  - `#### Milestone Overview` (`BD/m01…/overview.md:11`).
  - `[!design]` (`BD/r50…/ev-01:15`).
  - A `## Read Aloud` section (`00-first-meeting ev-01:121`).
  - "Arc H/J/E/F" labels (e.g. `BD/m04…/ev-01:77`).
- **Flags and their wording.** Other flags: Kreb Unmasked, Zardoz Introduced, Nar'l Active/Eliminated, Eye 3 Recovered by BD.
- **2014 or unverified stat names.** "MM stat blocks", Thugs, Bugbears, Intellect Devourer and Beholder Zombie (`BD/m03…/overview.md:23-25`; `ev-01:25, :42, :56`). Veterans and Thugs in `m06` (`overview.md:16-22`). "Swashbuckler" and "Drow Gunslinger" appear in `r25 ev-01:69, :75, :87`. No mechanics reference for BD exists. Gunslinger is the WDH p.201 custom block (`campaign/guides/factions/08-bregan-daerthe.md:79`). I could not confirm 2024 names for it, for Swashbuckler or for Beholder Zombie.
- **Design-notes coverage.** BD has design-notes only for m01-m06 and m02b. It has none for 00-first-meeting, s01-s04, r03, r10, r25 and r50 (9 folders).

## (b) BD-specific rules

### 1. Player and villain faction

- BD is "the only villain faction available to player characters" (`campaign/guides/gm-guide/player-factions-overview.md:163`).
- The org page reads "Player faction and villain faction" (`campaign/setting/organizations/07-bregan-daerthe.md:6`).
- Jarlaxle's key design note: "must be written directly into the campaign structure, not treated as an edge case" (`campaign/setting/villains/jarlaxle.md:60`).
- Membership and villain activation are separate tracks (`jarlaxle.md:3`).
  - Membership is gated by party action at Trollskull Alley.
  - Villain activation is the **Jarlaxle Informed** outcome, set in Fireball! ev-04 and read in Gralhund Villa (`campaign/quests/act-ii/fireball/ev-04-the-sea-maidens-faire.md:116-117`; `gralhund-villa/flowchart.md:87`).
- BD members invert Sea Maidens Faire. "The Faire becomes a home base" (`player-factions-overview.md:180`).
- Members carry Jarlaxle's Lords' Alliance goal, which comes due at Vault of Dragons (`player-factions-overview.md:182`; `08-bregan-daerthe.md:33`).

### 2. Jarlaxle's identity

- **Setting rule.** His identity "stays hidden behind J.B. Nevercott and Zardoz Zord until **Sea Maidens Faire**" (`jarlaxle.md:3`). Phase 1 universal is Zardoz Zord. The phase-2 trigger is "PCs penetrate the disguise, or Jarlaxle decides they've earned the reveal" (`jarlaxle.md:15`).
- **What the BD drafts do.**
  - `s03` says Zardoz "has no intention of revealing that he is drow, that Zardoz Zord and J.B. Nevercott are the same person, or that he leads Bregan D'aerthe", and Nevercott never reappears (`BD/s03…/ev-01:16, :22`).
  - `m02b overview.md:11` tells the GM Nevercott and Zardoz "are the same man".
  - The m02b payoff has the party discovering "they have been working for the person they are trying to rob" (`campaign/structure/arc-h-sea-maidens-faire.md:378`; `:225`).
- **The Harper precedent.** Harper M4 sets that naming Jarlaxle "doesn't tell the party that Captain Zardoz Zord is the same person" (`campaign/quests/faction-events/harpers/m04-a-friends-house/ev-03-the-confrontation.md:14`; `design-notes.md:19`). The Harpers' Jarlaxle appears as Erystian Demarne. Harper M4 also awards "+1 Bregan D'aerthe Renown" to a BD member (`harpers/m04…/overview.md:41`), so the BD ladder is fed from outside the folder.
- **When PCs may learn it.** Sources conflict (see open question 1):
  - Fireball! via the nimblewright thread (`campaign/guides/gm-guide/design-notes-running-the-campaign.md:81`; `player-factions-overview.md:178`; org page `:31`).
  - Sea Maidens Faire only (`jarlaxle.md:3`).
  - The org page also says Jarlaxle "does not acknowledge that J.B. Nevercott and Zardoz Zord are the same person, even when both have been seen by the same party member" (`org:11`).

### 3. Jarlaxle's debrief exception

- CLAUDE.md, Content Rules, "Members-only for briefs and debriefs": briefs and debriefs fire only for party members of that faction. "Jarlaxle is the lone exception — his debrief fires for any party that dealt with him during the quest, regardless of BD membership."
- OOS repeats the exception in R3 (`OOS:9`). Gralhund ev-01:41 already writes Jarlaxle's brief as open to all parties (`campaign/quests/act-ii/gralhund-villa/ev-01-what-the-factions-say.md:41`; OOS `:206`).
- The exception is a cross-quest rule for Outposts, lair heists and Gralhund. Whether it reaches the standalone BD events inside the BD folder is undecided (open question 8).

### 4. BD rejects Lolth

- CLAUDE.md Content Rules: "No member worships her, keeps a shrine to her, or invokes the Spider Queen with devotion. Members speak of her with contempt, as the goddess they walked away from; the zeal a house drow gives Lolth, Soluun gives to Jarlaxle."
- Matching sources:
  - `campaign/setting/notable-figures/bregan-daerthe/02-soluun-xibrindas.md:14, :22`.
  - The Soluun voice profile: "never speaks of Lolth as anything but the spider-bitch he walked away from" (`voices/bregan-daerthe.md:54`).
  - DR M1 hazard: Soluun answers questions about his goddess "with open contempt for Lolth" (`DR/m01…/ev-01:333`).
- The BD drafts contain no Lolth reference at all (grep across the folder returned nothing). No BD scene mentions her, so the spec should say when a BD speaker may mention her.
- The DR M1 forged token shows "a spider on a disc" (`DR/m01…/ev-01:361`). That is the token's forgery, not devotion.

### 5. Manshoon and Two Zhentarims, as it applies to BD

- **R1.** "Nobody in-fiction knows Manshoon runs the Zhentarim splinter… all the harpers and other factions know is that the Black Network is split" (`OOS:7`). The Doom Raiders believe Floxin leads it. **Manshoon Named** is set at the Faction Outposts Interrogation House (Brief l.15-18; `OOS:11`).
- **The BD folder is clean.** It has "no Manshoon, Splinter or Floxin references" (`OOS:73`), and a fresh grep confirms zero hits.
- **Open villain-level question.** `OOS:123, :233`: "do the villains know each other?" The sources already written say:
  - Jarlaxle and Manshoon have a "non-interference arrangement" (`jarlaxle.md:48`).
  - BD "competes with Xanathar or Manshoon" (`08-bregan-daerthe.md:9`, V-flagged at `OOS:128`).
  - Jarlaxle and Manshoon are written as knowing the Cassalanter pact.
  - Session 38 did not answer this question.
- **How BD already touches the gate.**
  - BD's Sea Maidens Faire strike scene names Manshoon (`OOS:215`).
  - BD's Revelation List cites the *Directive to Zorbog*, mentioning Fenerus by name (`08-bregan-daerthe.md:130`).
  - Fenerus's NF page says he is "the target of Manshoon's kidnap directive in Faction Outposts" (`campaign/setting/notable-figures/bregan-daerthe/06-fenerus-stormcastle.md:26`).
- **Practical default.** A BD speaker should say "the Splinter" or "the other cell" and never "Manshoon" until **Manshoon Named**, unless the user rules that Jarlaxle is exempt as a villain. This extends DR's gate (`DR/00-first-meeting/ev-01:23`).

### 6. Cassalanter secrecy (R2)

- CLAUDE.md: nobody knows about the Asmodean pact, the soul contract or the family's infernalism before the party discovers it. Use suspicion, never knowledge.
- **Conflicts in setting pages.** `jarlaxle.md:51` says he "Knows about their infernal bargain through intelligence". Guide 11:81 and arc-h:160, :302, :341, :422 give BD a *Report on the Cultists of Asmodeus* (`OOS:158, :215`). Vessa's profile is correctly "too perfect… knows nothing more" (`voices/bregan-daerthe.md:231`).
- **BD draft candidates to verify.**
  - **M2.** `m02 ev-01:60, :110` says the Wazoo story is about "private infernal worship" among "certain Sea Ward noble families", printed as "specific enough to be alarming and vague enough to be legally unprovable". The earlier audit marked R2 "handled correctly" (`OOS:73`). Guide 08:67 summarises the exposé as "hidden gold and missing servants". Both cannot be right.
  - **M5.** `m05 ev-01:16` has Brimel "no idea the obligation is an infernal contract". The windmill's contents "reference the Brandath Crypts vault approach" (`:64`).

### 7. One-faction membership

- The user's rule is quoted as "each party member may join one faction" (`OOS:165`).
- Four guide pages still contradict it: `players-guide/faction-affiliations.md:3`, `gm-guide/player-factions-overview.md:3`, `factions/01-overview.md:7, :9` and `trollskull-manor/02-operating-costs.md:31` (Session 38 handoff, `session 38 handoff.md:204`).
- DR's handling, which BD should copy: "a character who already belongs to another faction gets no offer" (`DR/00-first-meeting/ev-01:17`).
- **BD-specific.** The draft First Meeting makes **Bregan D'aerthe Joined** party-level: "At least one party member accepted…" (`BD/00-first-meeting/ev-01:99-101`). It also makes **BD Contact Severed** closure party-wide (`:43, :103-105`; `s04 ev-01:34`; `player-factions-overview.md:176`; `jarlaxle.md:3`).
  - OOS flagged this as an R3 V and left "per reporting PC or party-wide lockout" undecided (`OOS:75, :76, :237`).
  - Fix in the spec: every membership outcome must be per recipient.
- m02b requires a BD member in the party (`BD/m02b…/overview.md:10`). Under individual membership, it fires only for a member who made contact.

### 8. Rank names and thresholds

| Renown | Rank | Source |
|---|---|---|
| 1 | Initiate | `08-bregan-daerthe.md:56` |
| 3 | Soldier | `08-bregan-daerthe.md:57` |
| 10 | Officer | `08-bregan-daerthe.md:58` |
| 25 | Commander | `08-bregan-daerthe.md:59` |
| 50 | Houseless Noble | `08-bregan-daerthe.md:60` |

- The thresholds are 1/3/10/25/50; `player-factions-overview.md:23` matches. The BD folders are `r03-soldier`, `r10-officer`, `r25-commander`, `r50-houseless-noble`.
- Rank benefits that need written per-PC procedures, as in DR:
  - **Initiate:** safe house on the *Heartbreaker* or *Hellraiser*, drow gear at cost via Fel'rekt.
  - **Soldier:** one intelligence item a tenday (including Nar'l's reports), Faire cover support, 20% fence discount.
  - **Officer:** a drow **Spy**, the nimblewright shipping records, one Uncommon item, and a 48-hour assessment once per quest.
  - **Commander:** Jarlaxle accompanies one mission per quest; two **Drow Gunslingers** and four **Drow** support one major operation per quest; once per quest one of three favours.
  - **Houseless Noble:** inner circle, the Underdark and Faerûn network, and the *Scarlet Marpenoth* with crew.
- **Gap on the Initiate benefits.** The BD First Meeting draft has no Initiate-benefits scene. DR's has the Fang Benefits block (`DR/00-first-meeting/ev-01:326-332`). The Initiate row, including Fel'rekt Lafeen's equipment access, needs a procedure (`08-bregan-daerthe.md:56`).

### 9. Other BD-specific constraints

- **Discretion rule.** "A party that exposes the faction's drow composition ends the relationship immediately" (`08-bregan-daerthe.md:20`). No draft event tests it.
- **Coin pouches.** Guide 08:14 and the First Meeting draft say 50 gp after M1 and 100 gp after M3 (`BD/00-first-meeting/ev-01:111`). `s02` hands over 100 gp from the "management" after M2 (`BD/s02…/ev-01:19`). Session 38 lists "the coin-pouch timing" as an unresolved inconsistency (`session 38 handoff.md:213`).
- **Soluun fate.**
  - Per Session 38: if Soluun survives M1, Jarlaxle decides his fate, most likely expulsion (`session 38 handoff.md:88`).
  - BD m04 should read **Soluun Captured / Escaped / Killed** (`OOS:263, :319-320`).
  - Soluun's disownment is a cover story (`02-soluun-xibrindas.md:22, :26`), and BD m04 ev:37 calls it real (`OOS:320`).
- **Seven Masks Lead.** DR M1 sets **Seven Masks Lead** (`DR/m01…/ev-01:449`), read by Faction Outposts and Sea Maidens Faire. BD sets the *Playbill* and the theater as a front.
- **Nar'l.** He is Soluun's elder-brother counterpart: Soluun is "the elder brother of Nar'l" (`02-soluun-xibrindas.md:26`). DR M1 design notes say the party does not learn the brothers' link there (`DR/m01…/design-notes.md:25`). Nar'l's NF page is in the xanathars-guild folder, not the BD folder.
- **Mission numbering.** `r03` and `r10` call Three Nights "Mission 4" (`BD/r03…/ev-01:15`; `r10 ev-01:9, :16`). `guide 08` and `s02` call it Mission 3 (`BD/s02…/ev-01:62`). `r25` says Nevercott is retired after Three Nights (`BD/r25…/ev-01:7`), but `s03` retires him after Compromised Eye (`BD/s03…/ev-01:9, :16`). The org page agrees with `s03` (`org:11`). The handoff lists "BD mission numbering" as unresolved (`session 38 handoff.md:212`).
- **Trollskull outcome names.** The First Meeting draft sets Joined and Contact Severed. Trollskull ev-04 and the guide also set **BD Acknowledged** (`campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:115-122`; `player-factions-overview.md:173`; Fireball flowchart `:53`). The draft never sets Acknowledged.

## (c) Proposed BD gates and base renown

All of this is my proposal, derived from the DR/Harper pattern. It is not a source rule.

| Event | Gate | Base | Renown after |
|---|---|---|---|
| M1 The Handkerchief and the Girl | Joining (Renown 1), 2nd level | 2 | 3 |
| M2 The Wazoo Affair | Renown 3, 3rd level | 2 | 5 |
| M2b The Betrayal Pitch (optional) | Renown 3 or 5, 3rd level, after M2 | none or 1 (see below) | 5+ |
| M3 Three Nights | Renown 5, 4th level | 3 | 8 |
| M4 The Compromised Eye | Renown 8, 5th level | 3 | 11 |
| M5 The Theater's Back Room | Renown 10, 6th level | 4 | 15 |
| M6 The Dive | Renown 13, 7th level | 4 | 19 |

**Justification**

- **Matches the finished DR/Harper gates.** DR uses Join@L2, R3@L3, R5@L4, R8@L5, R10@L6, R13@L7 (`session 38 handoff.md:96-103`; `DR/m03 overview.md:5`). The guide 08 table gives the same levels (2nd to 7th) and base 2/2/3/3/4/4 (`08-bregan-daerthe.md:66-71`), which matches the CLAUDE.md calibration.
- **Reachable from Renown 1 with base only.** 1+2=3, +2=5, +3=8, +3=11, +4=15, +4=19. Every gate is met on the ladder, with slack. Ranks 25 and 50 need bonuses from elsewhere, as for DR (`DR/r25 design-notes:17`; `session 38 handoff.md:196`).
- **The old BD draft gates were R0/2/4/7/10/14** (`BD/m01 overview:6` through `BD/m06 overview:6`). They were set for a Renown 0 start. From a Renown 1 start with base awards, they are too loose.
- **Which start is right.**
  - DR uses Renown 1 at joining, with the Fang rank (`DR/00-first-meeting/ev-01:304`).
  - The player guides still say Renown "starts at 0" (`player-factions-overview.md:22`; `faction-affiliations.md:22`).
  - If the user wants a 0 start, the gates would be 0/2/4/7/9/12 after base awards, which differs from DR.
- **M2b.**
  - **Where it fits.** The draft sits it "between Missions 2 and 3" at 3rd level (`BD/m02b overview:6, :16`). M2 ends at Renown 5, but M3 needs 4th level, so M2b occupies the same L3 waiting gap that DR's rank events and M2 fill.
  - **Not a ladder row.** Guide 08's missions table has six rows and no M2b (`08-bregan-daerthe.md:64-71`). The draft awards only "+1 Renown / +1 Renown (supplementary)" and no base (`BD/m02b ev-01:76-77`). Treating it as an extra, non-gating mission keeps the 19-point ladder intact.
  - **Conditions.** At least one BD member in the party AND direct contact with Zardoz or Nevercott (`BD/m02b overview.md:10-11`). The pitch is the lead-in to arc-h's "Zardoz Betrayal Pitch" (`arc-h:93, :225, :378`). Arc-h says the pitch needs "a PC at Initiate or Soldier rank".
  - **Per member.** The overview's own conditions read as party-level. Make them per member.
- **Extras for 25 and 50.** The mission base awards total 19. Guide 08's Earning Renown items (+1 intelligence, +2 Golorr artifact, +1 Nar'l cover, +1 Faire conduit, +2 nimblewright records heist, +1 creativity once per quest) supply the rest (`08-bregan-daerthe.md:45-50`). The `r25`/`r50` design notes should say so, as DR's do.

## (d) Voice-profile coverage

Voice doc for BD: `.claude/skills/character-voices/voices/bregan-daerthe.md`. It covers Zardoz Zord (:7), Jarlaxle (:26), Soluun (:44), Fel'rekt (:62), Krebbyg (:80), Zelifarn (:98), Fenerus Stormcastle (:116), Malcolm Brizzenbright (:134), Quilm (:152), Ryvarra (:170), Margo Verida (:188), Khafeyta Murzan (:206) and Vessa (:224).

| NPC in the BD drafts | Profile | Where |
|---|---|---|
| Jarlaxle / Zardoz Zord | Yes (two profiles) | `voices/bregan-daerthe.md:7, :26` |
| Soluun Xibrindas | Yes | `:44` |
| Fel'rekt Lafeen | Yes | `:62` |
| Krebbyg ("Kreb Sorrush") | Yes | `:80` |
| Ryvarra | Yes | `:170` |
| Malcolm Brizzenbright | Yes | `:134` |
| Fenerus Stormcastle | Yes | `:116` |
| Zelifarn | Yes | `:98` |
| Nar'l Xibrindas | Yes | `voices/xanathars-guild.md:47` |
| Ahmaergo | Yes | `voices/xanathars-guild.md:29` |
| Nihiloor | Yes | `voices/xanathars-guild.md:65` |
| Ott Steeltoes | Yes (also an NF page) | `voices/xanathars-guild.md:101` |
| Xanathar | Yes | `voices/xanathars-guild.md:7` |
| Victoro, Ammalia Cassalanter | Yes | `voices/cassalanters.md:9, :31` |
| Esvele (Black Viper) | Yes | `voices/independents-adversaries.md:25` |
| Kelso Fiddlewick | Yes | `voices/independents-adversaries.md:43` |
| Davil, Tashlyn, Yagra, Istrid | Yes, in `voices/doom-raiders.md` (not read) | for DR cross-reads |
| J.B. Nevercott | No separate profile | cover of Jarlaxle; the First Meeting draft carries a `[!profile]` with only Resonance, Persona, Morale and Inspirations (`BD/00-first-meeting/ev-01:87-95`) |
| Vessin (tiefling girl, M1) | No profile, no NF page | |
| Gaxly Rudderbust (Wazoo publisher, M2) | No profile, no NF page | |
| Lady Ashford (M1) | No profile, no NF page | |
| Brimel Crestfall, Florette Cressyn (M5) | No profile, no NF page | |
| Ilphrin Quiss (r10), Pelsha and Vorn (r25), Krenick Durr (m06) | Invented; no profile | listed as invented in `session 38 handoff.md:241` |

- Zardoz's profile says "Never mentions the Underdark, drow or Luskan politics" and "broad Illuskan sailor's accent" (`voices/bregan-daerthe.md:10, :18`). The drafts' Zardoz is warm and precise, not boisterous (`BD/s03…/ev-01:50`). The profile also has a sudden-elegance slip rule for when the cover strains (`:15`).
- Soluun's profile conflicts with CLAUDE.md in one place: his "short, hard" sentences against the 12-word speech floor (`voices/bregan-daerthe.md:48`; `session 38 handoff.md:136`). The handoff says terse characters are played by what they withhold.
- Quilm's profile explicitly breaks from the ember-voice speech floor (`:156`). Krebbyg's run-ons suit it.

## (e) Open questions for the user

1. **When may PCs learn JB = Zardoz = Jarlaxle?** Fireball! via the nimblewright thread (`design-notes-running-the-campaign.md:81`, `player-factions-overview.md:178`, org `:31`) or Sea Maidens Faire only (`jarlaxle.md:3`, `BD/s03 ev-01:16, :22`). Does M2b (`overview.md:11`) reveal JB = Zardoz?
2. **Who names "Bregan D'aerthe" first?** Nevercott "once, if pressed" (`BD/00-first-meeting ev-01:75`), Krebbyg after M2 (`BD/s02 ev-01:29`), or Jarlaxle's org page ("until the party has already worked for that person twice", `org:13`).
3. **Who delivers M1?** Unsigned theater tickets from Krebbyg (`org:8`, `08-bregan-daerthe.md:29`) or Nevercott at the door (`08-bregan-daerthe.md:37`, `BD/00-first-meeting ev-01:111`)? The org page also has Nevercott at the Yawning Portal for M2 (`org:8`).
4. **Do villain factions count under R1 and R2?** `OOS:233`. Decides whether BD speakers may name Manshoon, whether Jarlaxle knows about the Cassalanter pact (`jarlaxle.md:51`, guide 11:81), and the Jarlaxle/Manshoon non-interference line (`jarlaxle.md:48`).
5. **M2 Wazoo exposé content.** "Private infernal worship" (`m02 ev-01:60`) or "hidden gold and missing servants" (guide 08:67)?
6. **M6 and Eye #3.** Guide 08:9 has Jarlaxle already holding Eye #3 aboard the *Scarlet Marpenoth*. Guide 08:71 has Xanathar divers staging a limpet charge on the sub. The draft has Eye #3 sunk with a ketch (`BD/m06 ev-01:18`) and sets **Eye 3 Recovered by BD** (`BD/m06 ev-01:14`). The handoff lists this as unreconciled (`session 38 handoff.md:233`).
7. **M5 windmill location.** North Ward in the draft and arc-h (`BD/m05 ev-01:16, :64`) versus a Southern Ward windmill, a discrepancy the handoff flags (`session 38 handoff.md:233`).
8. **Members-only inside BD.** Does the Jarlaxle debrief exception cover BD's own s03 Dinner with Zardoz and other standalones, or only cross-quest debriefs?
9. **BD Contact Severed scope.** Per reporting PC or party-wide (`OOS:237`)? Under individual membership, a per-PC rule matches R3.
10. **Start renown.** Renown 1 at joining (DR convention) or 0 (`player-factions-overview.md:22`)?
11. **M2b base renown.** None (draft), or a base of 1 or 2 that changes the 19-point ladder?
12. **Mission numbering.** Fix the Three Nights "Mission 3/4" slip, and the point at which Nevercott retires (after Three Nights per `r25`, after Compromised Eye per `s03` and `org:11`).
13. **Coin pouches.** 50 gp after M1 and 100 gp after M3 (guide 08:14), or the 100 gp envelope after M2 (`BD/s02 ev-01:19`)?
14. **Soluun's fate.** Confirm the Session 38 ruling for the BD folder: Jarlaxle expels him if he survives M1, with M4 reading **Soluun Captured/Escaped/Killed** (`session 38 handoff.md:88`; `OOS:263, :319`).
15. **Invented names.** Accept or replace Ilphrin Quiss, Pelsha, Vorn, Krenick Durr and Brimel and Florette's profiles, plus the unprofiled minor NPCs (`session 38 handoff.md:241`).
16. **2024 stat names.** Confirm 2024 equivalents for Drow Gunslinger, Swashbuckler (Jarlaxle) and Beholder Zombie. The mechanics reference does not cover them (reference l.13).

## Files consulted

- `/home/user/waterdeep/docs/plans/doom-raiders-conversion-brief.md`
- `/home/user/waterdeep/docs/plans/doom-raiders-mechanics-reference.md`
- `/home/user/waterdeep/docs/plans/harpers-out-of-scope-notes.md`
- `/home/user/waterdeep/session 38 handoff.md`
- DR files: `m03-the-missing-snobeedle/{ev-01,overview,design-notes}`, `r03-wolf/{ev-01,design-notes}`, `r25-ardragon/design-notes`, `r50-dread-lord/ev-01`, `00-first-meeting/ev-01`, plus greps across the folder
- `/home/user/waterdeep/campaign/guides/factions/08-bregan-daerthe.md`
- `/home/user/waterdeep/campaign/guides/factions/07-doom-raiders.md`
- `/home/user/waterdeep/campaign/guides/gm-guide/player-factions-overview.md`
- `/home/user/waterdeep/campaign/guides/players-guide/faction-affiliations.md`
- `/home/user/waterdeep/campaign/setting/organizations/07-bregan-daerthe.md`
- `/home/user/waterdeep/campaign/setting/villains/jarlaxle.md`
- `/home/user/waterdeep/campaign/setting/notable-figures/bregan-daerthe/{01,02}-*.md`
- `/home/user/waterdeep/.claude/skills/character-voices/voices/bregan-daerthe.md`
- BD drafts: `00-first-meeting`, `m02b` overview, `s02`, `s03`, `r10`, and greps over the rest of the folder