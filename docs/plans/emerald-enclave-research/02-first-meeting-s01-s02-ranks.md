# Emerald Enclave research: 00-first-meeting, s01, s02, r03, r10, r25, r50

Scope: `00-first-meeting`, `s01-a-seat-at-phaulkonmere`, `s02-the-water-table-stirs`, `r03-summerstrider`, `r10-autumnreaver`, `r25-winterstalker`, `r50-master-of-the-wild`. No campaign file was edited. Report 02 of 5.

**Model reading done.** Read in full (events and design notes):
- Force Grey: `force-grey/00-first-meeting/` (ev-01 :1-289, design-notes), `force-grey/s01-the-full-picture/` (ev-01 :1-291, design-notes), `force-grey/r03-junior-griffon/` (ev-01 :1-219, design-notes), `force-grey/r50-force-grey-commander/` (ev-01 :1-414, design-notes).
- Doom Raiders: `doom-raiders/r03-wolf/` (ev-01 :1-257, design-notes).
- Bregan D'aerthe: `bregan-daerthe/r03-soldier/` (ev-01 :1-354, design-notes :1-49).
- Harpers: `harpers/00-first-meeting/` (ev-01 :1-354, design-notes), `harpers/r03-harpshadow/` (ev-01 :1-262, design-notes).
- Also read: `docs/plans/emerald-enclave-research/00-research-brief.md`, CLAUDE.md Standing Rules, `docs/plans/force-grey-conversion-brief.md` (User decisions :41-82, First Meeting brief :209-225), `harpers-conversion-brief.md` (contact-object addendum :451-466), the headings of `force-grey-research/02-first-meeting-s01-ranks.md`, `session 42 handoff.md` (EE lines), `harpers-out-of-scope-notes.md` (EE lines).

**Abbreviations**
- `R` = `/home/user/waterdeep/campaign/quests/faction-events/emerald-enclave/` (restored input; every folder in scope has one `ev-01-*.md` and no design-notes).
- `PREV` = `/tmp/claude-0/-home-user-waterdeep/724ec0d3-1411-5aee-88ce-0e8b98de0e73/scratchpad/ee-prev/campaign/quests/faction-events/emerald-enclave/`.
- `FG`, `DR`, `BD`, `H` = `/home/user/waterdeep/campaign/quests/faction-events/{force-grey,doom-raiders,bregan-daerthe,harpers}/`.
- `G04` = `campaign/guides/factions/04-emerald-enclave.md`; `ORG` = `campaign/setting/organizations/03-emerald-enclave.md`; `NF-M` / `NF-J` = `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md` / `02-jeryth-phaulkon.md`; `VOICE` = `.claude/skills/character-voices/voices/emerald-enclave.md`; `AB` = `sources/Appendix_B_-_Player_Factions.md`; `WDH` / `WDMM` = `sources/adventure-wdh.json` / `adventure-wdmm.json`; `OOS` = `docs/plans/harpers-out-of-scope-notes.md`; `XPHB`/`XDMG`/`XMM` = 5etools-mirror-3 data fetched this session (`.../scratchpad/ee02/`).

Line numbers for R and PREV files are the file's own lines. For the PREV s02 and r25 files I cite the line the block starts on.

---

## 1. What the model pages require (copy these)

**First Meeting (H, FG, DR model).**
- Skeleton: Gamemaster's Summary with a `#### Candidates and Companions` block and a `What Is Actually True` block (H FM :3-24; FG FM :3-25). Then `###` scenes. Each NPC scene has a `[!readaloud]`, a `[!social]` header line `Name (Alignment, Species, pronouns) :: summary`, a "happy to discuss" list, a "will not discuss" line, then `[!qna]` blocks (FG FM :92-185; H FM :120-216).
- Candidate frame: every character who belongs to no other faction is a candidate and answers for themselves; a character already in another faction gets no offer; companions may sit in and gain nothing; if no candidate accepts, the Event ends with no membership outcome (FG FM :13-17; H FM :14-18).
- `### Each Candidate's Answer` with `Recording the Answers`, an accept readaloud, a decline readaloud, and a `... Benefits` box that lists each benefit per member (FG FM :187-226; H FM :278-306). A late acceptance is recorded under the same outcome with the name (FG FM :273; H FM :336-340).
- Party-level help is a separate box because the manor is shared, given once (FG `The Renovation Help` FM :230-236).
- Close: `Event Outcomes` marked per name, `Next Steps` ending "This Event awards no Milestone Points", then `## Overview` and a `## Summary` with "After the Meeting" and "Without a Private Meeting" variants (FG FM :262-289; H FM :330-354).
- No first mission is handed over at the First Meeting; the mission arrives by its own contact later (FG FM :273; H FM design notes "Source Departures").
- Contact object (HB :451-466): describe the contact object in every event, keep one canonical description, and vary only where it finds the member. H's paper bird is described in `The Paper Bird` (H FM :26-42).
- Harper addendum (user request): a tailor scene and background color explicitly irrelevant to the meeting (H FM :44-118). FG has no such request on record. There is no EE request on record; see §10 decision 12.

**Rank event (DR r03, H r03, BD r03, FG r03/r50).**
- Trigger text: "when an individual X member first reaches Renown N, which usually happens right after <mission>" (DR r03 :5; H r03 :5; BD r03 :5; FG r03 :5). Hook delivered at noon the next day; a member away from Waterdeep finds the contact object at their first surface lodging, and the meeting moves a day (DR r03 :11-20; H r03 :14-24; FG r03 :13-27).
- `What Is Actually True` block (DR r03 :22-24; H r03 :26-34; FG r03 :29-36). Benefits are written as per-member procedures: contact, place, notice, how to ask, limit, delay, who else, loss rule (DR r03 :114-126, :160-170, :210-218; H r03 :87-96, :128-135, :223-228; FG r03 :104-121, :135-144, :180-189; BD r03 :157-169, :252-264, :302-313).
- Companions can carry and use what the member gets but cannot ask for anything (DR r03 :236; H r03 :240; FG r03 :197; BD r03 :321).
- Renown loss: the rank is kept and the benefits are suspended until Renown is restored (H r03 :96; FG r03 :112, :144, :189; BD r03 :48).
- `### Renown Opportunities`: "The rank event awards no Renown" (DR r03 :230-232; H r03 :234-236; FG r03 :191-193).
- Outcome per recipient name, read by the next rank event; Next Steps says "This Event awards no Renown and no Milestone Points" (DR r03 :242-249; H r03 :248-254; FG r03 :203-211).
- Degrading channels read earlier outcomes in a table (BD r03 :171-189) and in per-outcome speaker branches (FG s01 :119-203).

**Standalone event (FG s01).**
- Members-only (FG s01 :5, :13); a test with three routes per element (the Three Clue Rule; FG s01 :50-64); an incomplete account earns one question and a return visit (FG s01 :66-81); a 2-Renown award "once in the campaign" (FG s01 :261-263); a late sitting adds a name to the outcome (FG s01 :267-269).

**r50 (FG r50).**
- Hold until the prior rank outcome is marked and the member is on the surface (FG r50 :16); the *Sending* reaches Undermountain except when aimed at Halaster (FG r50 :28); per-member procedures for the team, scroll, reserve (FG r50 :130-143, :179-189, :207-219); CR 2.0 ally tables for 3, 4 and 5 PCs (FG r50 :145-167); a `Below the Surface` block (FG r50 :229-231); the Mad Mage seeds as one-line facts only (FG r50 :370-380); a Public/Sealed choice recorded by name with a tenday to answer and silence counting as Sealed (FG r50 :339-346).

---

## 2. R and PREV: what each folder contains (facts)

R is the original "Arc" draft with retired formats. PREV is the Session 36-40 polish: `[!gamemaster]` / `[!readaloud]` / `[!social]` / `[!qna]` blocks and Event Outcomes, but no `What Is Actually True`, no per-candidate frame, no procedures, no design notes.

### 2a. 00-first-meeting
- **R** (:1-106). `> **[GM]**` Summary (:3-14): "fires for each EE-eligible character when the white cat invitation arrives during The Factions Come Calling"; "at Phaulkonmere, in the Sea Ward" (:7). White cat at the Trollskull window speaks in Melannor's baritone (:24-26), 17 words: "Melannor Fellbranch, Phaulkonmere. The gate will be open when you arrive. The gardens are worth seeing." The cat vanishes. A DC 12 Intelligence (Arcana) check recognizes *animal messenger* (:28). Melannor meets them at the gate, humorless but not cold (:32). Topics: purpose (disruption), the beholder, why this party ("watched Xanathar sewer hideout in Finding Floon", :40), and the vault gold on a DC 12 Charisma (Persuasion) check (:42). Jeryth speaks "midway through the gardens" (:46-56): sanctuary, the disturbance under the Castle Ward (:52), and her requests, including the Stone not remaining in Waterdeep (:54). Accepting is "plain" and the *charm of restoration* settles in with no announcement (:63). Outcome heading `#### Emerald Enclave Joined: True / False`, "at least one party member accepted" (:67-68). Melannor's exit line "I'll be in touch" (:74). Next: M1 at 2nd level (:76). Retired items: `> **[GM]**`, `**Background (DM only)**`, `> [!profile]+` (:58), a separate `## Read Aloud` section (:82-102). No `[!social]` block, no qna.
- **PREV** (:1-164). Same beats in current blocks. Adds `[!social]` for Melannor (:44-56) and Jeryth (:95-106), qna (:58-80, :108-122), a DC 14 Wisdom (Insight) tell (:56) that Melannor's pace changes near the disturbance, separate decline and accept gate lines (:128-140). Outcome `**Emerald Enclave Joined**` (:150): "mark when at least one party member accepted"; read by every EE mission, by **A Seat at Phaulkonmere**, and by **The Factions Come Calling**.
- **Neither** names the ward correctly, handles candidates per character, gives the Springwarden benefits as a box, or delivers the renovation help that **The Factions Come Calling** (`campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:57`) and the manor guide (`campaign/guides/trollskull-manor/02-operating-costs.md:82`) promise.

### 2b. s01-a-seat-at-phaulkonmere
- **R** (:1-91). Fires "after the party completes their first Emerald Enclave mission (any mission)" (:5). Same white cat, 8 words: "You've done the work. Come when you're ready." (:30). Melannor at the east gate gives "a plain iron key" (:40-42): "East gate. Opens from either side. No need to knock or announce yourselves." Jeryth: "I know what you did." / "This garden is yours now. Come when you need it. There are no conditions." (:49, :53). "No flags are set" (:63). Next: **The Water Table Stirs** "begins from Fireball! onward" (:71). Says "No renown is awarded. No new mechanical benefit is introduced" (:9).
- **PREV** (:165-256, i.e. s01 :1-92). Same, in current blocks. "This event sets no outcomes" (listing :242).

### 2c. s02-the-water-table-stirs
- **R** (:1-169). One file, five "surges" (:7-17), each with trigger, city symptom, a speaker (Melannor for One, Two and Five; Jeryth direct for Three and Four), a request, and a renown line.
  - Surge One: Stone first activated during or after **Fireball!**; starlings (:34); Melannor visits Trollskull Manor in person (:36); request: report aberrant activity in the Dock Ward sewers or below (:42); +1 if "useful" (:44).
  - Surge Two: Stone attuned at the start of **Faction Outposts**; oak roots moved two inches (:50); "keep the Stone moving; not more than a tenday in one place" (:52, :56); no renown (:58).
  - Surge Three: first Eye restored; seven cistern workers dream of a vast eye (:64); Jeryth speaks (:68-83); request: report any creature "directing other creatures" before pursuing it (:81); +1 (:83).
  - Surge Four: second Eye restored; fish beaching on the south quay (:89); Jeryth: "I am asking" (:101); request: complete **The Fouled Channel** before the third Eye (:105); if the third Eye opens first, she adds a go-back line (:107-112); +2 (:114).
  - Surge Five: third Eye / Full Awakening; black well water (:120); Melannor reads Jeryth's dictated line at the gate (:122-132); request: M6 "within the tenday" (:134); renown comes from M6 (:143).
  - Jeryth never names the presence; GM text names it Illuun (:15). `[!lore]` block says "Illuun does not appear in Dragon Heist" (:26-28). Ends `#### Milestone: None` (:155-157), "no flags of its own" (:147).
- **PREV** (:1-207). Same skeleton, but the requests are concrete scenes:
  - Surge One: cranium rats nesting forty feet into the eastern branch of a Coin Alley storm drain, +1 for destroying them (:65-69).
  - Surge Three: two intellect devourers in the Selduth Street cistern tunnel, Trades Ward, before they implant workers; +1 (:125-127).
  - Surge Four: a ward-seal pressed into an exposed ley node in the cellar of wine merchant Bertio Caskwall, Selduth Street; DC 12 Persuasion or a credential to get in; DC 10 Perception to find the crack; +2 (:144-160). **PREV's Surge Four does not ask for The Fouled Channel at all**, so its Surge Five (:183-189) reads as if M5 were still outstanding.
  - No outcomes (:193-195).

### 2d. r03-summerstrider
- **R** (:1-84). Fires "at the first natural pause after one character's Enclave renown reaches 3": next visit, or a pigeon after a tenday (:7). Grey pigeon in Melannor's baritone, 9 words: "Phaulkonmere, when you have a spare hour. No urgency." (:25). Three benefits: *animal messenger* relay "once per tenday ... any address in Waterdeep or the surrounding environs" (:37); Jeryth heals injuries "sustained on Enclave business" at Phaulkonmere, no cost (:41, :56); the network gives "one briefing per ward per tenday" (:45), with content "any ward the GM selects" and "flavor" (:49-50, :74). Flag `#### Summerstrider Reached: True / False` (:66-68). Next: r10 at Renown 10 (:76).
- **PREV** (:1-114). Same, with qna and an outcome `**Summerstrider Reached**` "mark when the promoted character leaves Phaulkonmere" (:100). Adds Melannor's pruning shears (:35).

### 2e. r10-autumnreaver
- **R** (:1-104). Fires at Renown 10; Melannor arrives at Trollskull Manor in person (:7, :22-26). Jeryth: "Once per quest. Any druid spell of fifth level or lower. No components from you" (:44); lists *mass cure wounds*, *conjure elemental*, *wall of stone*, *contagion* (:50); cadence "Once is the agreement" (:52-53). Charcoal map, three routes: a drainage channel behind the Sea Ward dyer's district; a sealed tunnel from the Southern Ward's deep cisterns; a sealed entry in the Dock Ward's abandoned fishmeal warehouse (:57-61); maintained twelve years, marked with three horizontal lines over a leaf (:63). Paddock: brown bear, dire wolf, giant eagle (:71); one assists in one operation per quest; returns after (:73). Flag `Autumnreaver Reached: True / False` (:86-88). Beast appears at the stable yard next morning (:94).
- **PREV** (:115-261). Same; outcome `**Autumnreaver Reached**` (:243-247); stat blocks "from the 2024 *Monster Manual*" (:237).

### 2f. r25-winterstalker
- **R** (:1-100). Fires at Renown 25; an owl at dusk, 4 words: "Winterstalker. Come tomorrow morning." (:27). Pavilion in the eastern garden (:33). Melannor accompanies in person "one mission per quest", Druid stat block, terrain-control spells (:39-44). Jeryth to 8th level, once per quest, naming *sunburst*, *control weather*, *earthquake*, *animal shapes* (:50-57; *tsunami* and *antipathy/sympathy* in the tip). Advance intelligence: a Giant Crocodile in the Southern Ward cisterns, "Advantage on Wisdom (Animal Handling) checks. Advantage on first Initiative roll within this location", 24-hour turnaround (:61-63). Letter from Sarna Dath, south quay, blue-and-white boat, ship manifests and departure schedules; gull reports once per tenday, "Sea Maidens Faire fleet" departures (:71-78). Flag `Winterstalker Reached: True / False` (:82-84). "Parties are not expected to reach Renown 50 during Dragon Heist" (:92).
- **PREV** (:1-135). Same; outcome `**Winterstalker Reached**` (:119-123).

### 2g. r50-master-of-the-wild
- **R** (:1-153). Fires at Renown 50 (:7). Three animals (pigeon, white cat, owl) arrive silent (:30-36). Six rangers and druids wait in the garden: four humans, a half-elf, a wood elf, unnamed (:40-44). Jeryth names the rank and gives every party member present a *charm of vitality*, "once per campaign" (:50-72); the tip says it "typically grants advantage on Constitution saving throws" (:75). Melannor: the six are "yours for one operation. One only" (:81); "any beast of moderate danger that can understand a clear instruction will do one thing" (:85). The choice: accept the Enclave's commission into Undermountain to track "whatever is sleeping below" and report where the root is anchored (:95-111). Flags `Master of the Wild Reached` and `Undermountain Commission Accepted` (:115-121); if accepted, a slip with three signal marks (:127). A `[!design]` block says the event "may fire before or after the Vault of Dragons resolution" and branches Jeryth's closing remarks on whether **Vault of Dragons** has resolved (:15-18).
- **PREV** (:1-144). Same; outcomes `**Master of the Wild Reached**` and `**Illuun Watch Accepted**` (:123-128); branch is "If **The Dreamer's Reach** (Mission 6) is complete" (:25); beasts "of CR 2 or lower" (:96); *charm of vitality* described correctly as a *potion of vitality* as a Magic action (:83); no Constitution-save line.

---

## 3. Contact object, who recruits, where, and the members-only frame

### 3a. Facts
- **Recruiter and place.** Melannor Fellbranch recruits at Phaulkonmere (R 00:7, :32; WDH 3700, 3717; AB 295). Jeryth offers membership and the *charm of restoration* (WDH 3717; AB 297, 346). WDH and AB place Phaulkonmere in the **Southern Ward** (WDH 1320, 3690, 3700; AB 292, 309; ORG :19; `arc-b-trollskull-alley.md:123`; `arc-e-faction-outposts.md:85`). R 00:7 and :80 say **Sea Ward**. WDH 3700 puts it "one block south of Kolat Towers", which WDH 560 puts in the Trades Ward.
- **Delivery.** AB 289-312 and WDH 3690: a white cat speaks "Interested in joining the Emerald Enclave? Come meet us at Phaulkonmere in the Southern Ward." R 00:26 drops the "interested in joining" question.
- **Contact objects across the rank events (R/PREV):** white cat (FM, s01), grey pigeon (r03, and M1: R m01 ev-01:86), Melannor in person (r10), owl at dusk (r25), three animals at once (r50), a letter at the gate and gulls (r25: Sarna), an iron key (s01), a charcoal map and a paddock choice (r10), a slip of three signal marks (r50). Each event describes its animal in different words; there is no canonical description (PREV 00:23, r03:22, r25:26).
- **Mechanic behind the animals.** *Animal Messenger* (XPHB): a Tiny Beast, within 30 ft, "must succeed on a Charisma saving throw" unless CR 0; the caster names "a location you have visited" and a recipient by general description; **a message of up to twenty-five words**; the Beast covers 25 miles per 24 hours (50 if it flies); duration 24 hours. Cat, Owl and Raven are XMM Tiny Beasts at CR 0. **There is no XMM Pigeon or Gull.**
- **The members-only frame in R/PREV.** R 00:7 says "for each EE-eligible character" but its outcome is party-level (00:68). PREV's outcome is "at least one party member" (PREV 00:150). `ev-04-the-factions-come-calling.md:27` gives the EE eligibility as "Druids, rangers, nature clerics; nature-aligned behavior in Finding Floon" and :17-18 says invitations are "per-character, not per-party". AB 289 says the Enclave "seeks out ... naturalists, healers, or ... concern for the natural world". No Finding Floon file writes a "nature-aligned" outcome (grep of `campaign/quests/act-i/finding-floon/`: no hits).
- **Rank events** are individual in R/PREV ("one character's Enclave renown", R r03:7), but they carry no per-member counters, no "companions cannot ask" rule and no loss rule.
- **Tally.** `ev-03-the-neighbors.md:20` says Tally Fellbranch is Melannor's brother and "the party will not make the connection until Emerald Enclave recruitment arrives in ev-04." `08-notable-patrons.md:15` has Tally introduce Melannor. VOICE :10, :14 has Melannor call him "Talisolvanar" and say "Talisolvanar should visit." Neither R nor PREV FM mentions him.

### 3b. Recommendations
1. **Candidates (decision 1 below).** Recommend the Harper/FG rule: every character who belongs to no other faction is a candidate and answers for themselves. Use the nature-aligned trigger from ev-04 only for who the cat finds first and what Melannor notices, as H FM does with its "Good-aligned" trigger ("only decides when the bird arrives, and nobody is tested for alignment at the door", H FM :16).
2. **No Offer Closed outcome.** The Enclave's gate is open (R 00:26). Drop the *Sending* machinery FG needed. A candidate who defers is welcome later; Melannor repeats the offer in a few sentences (mirrors FG FM :54, :215).
3. **Canonical contact objects** (one paragraph each, reused in every event; vary where it finds the member). Recommended text for the drafter:
   - **The white cat.** A white cat with folded paws, Tiny Beast, CR 0 (XMM Cat). It sits on the sill with composure, speaks in Melannor's low baritone from "somewhere behind its eyes" (PREV 00:23), delivers the message once, drops to the street. The message is at most 25 words (the *Animal Messenger* limit, not a house rule). Suggested FM message, 21 words: "Melannor Fellbranch, Phaulkonmere, Southern Ward. The gate will be open when you arrive. Bring anyone who wants to see the gardens." Verify the count when drafting.
   - **The grey pigeon, the owl, the three animals.** Pigeon: use the XMM **Raven** or **Owl** block if a stat block is ever needed (no XMM pigeon). Owl at dusk. Three animals at once (a pigeon, a white cat, an owl) with no words.
   - **GM-only:** the animals are Tiny Beasts under Melannor's *Animal Messenger*; every message is 25 words or fewer; Melannor must have visited the delivery location. A message that needs a reply holds the Beast for the answer. Beasts cannot cross Undermountain levels except on foot (see §7).
4. **Per-character frame.** Put `#### Candidates and Companions` and `#### What Is Actually True` in the Summary, as H FM :14-24 and FG FM :13-25 do. Content for `What Is Actually True`: Jeryth decided before the party arrived; the offer has no hidden price (AB 285; ORG :17); the Enclave has no stake in the gold; Jeryth has felt a dreaming presence for months and does not know its name; Melannor does not know what the presence is; the Splinter and Cassalanters are not named by anyone (§6).
5. **Tally payoff (zero-prep).** One Melannor line at the gate asks after "Talisolvanar", pays off ev-03 :20, and costs nothing else. If the manor guide's oak-tree string is used (§4c), Tally is also the one who noted the oak "acting strange" (`08-notable-patrons.md:18`).

---

## 4. What each rank grants: R, PREV, guide, Appendix B, WDH

### 4a. Side-by-side

| Rank | R / PREV event | G04 table (:51-57) | AB (:373-377) | WDH |
|---|---|---|---|---|
| R1 Springwarden | haven; *charm of restoration* | same | same, "each new recruit" | *charm of restoration* on joining; haven "for enclave members and their friends" (3717) |
| R3 Summerstrider | relay once per tenday; Jeryth healing for injuries on Enclave business; network, one briefing per ward per tenday | same | relay + healing only | none |
| R10 Autumnreaver | Jeryth casts druid spells of 5th level or lower once per quest; one beast (bear, eagle or dire wolf) per operation per quest; three hidden sewer routes | same | spells and beast "once per arc"; no routes | Jeryth casts a spell if renown equals or exceeds its level (3718) |
| R25 Winterstalker | Jeryth to 8th level once per quest; Melannor accompanies on one mission per quest; advance intelligence; harbor network | same | spells and Melannor "once per arc"; no intelligence or harbor | none |
| R50 Master of the Wild | *charm of vitality* for every party member present, once per campaign; six rangers and druids for one operation; beasts of CR 2 or lower perform one task | same, plus "once per quest" on the beasts | **charm of heroism**; six rangers and druids | none |

- G04 :51-57 and the Players' Guide (`faction-affiliations.md:77-81`) and GM overview (`player-factions-overview.md:82-86`) match R. Nothing in them is a procedure (no contact, place, notice, limit, loss rule), which is the gap the rank events must close, as FG r03 closed it (FG r03 design notes :222-226).
- The charm change from AB's *heroism* to *vitality* is a remix decision; M4 awards *charm of heroism* party-wide (R m04 ev-01:62), so r50 uses a different gift (PREV r50:83).
- AB uses "arc"; the remix says "quest" (CLAUDE.md). R/PREV r10 and r25 already say "once per quest" with a tip that "each named quest in the Quest Quick Reference counts as one" (R r10:52; R r25 none; PREV r10:193).

### 4b. Rules checked against 5etools data (XPHB/XDMG/XMM)
- **Charm of restoration** (XDMG p. 99): 3 charges; *Greater Restoration* costs 2, *Lesser Restoration* 1; the charm vanishes when all are spent. The restored text treats it as a one-off feeling; a charge count is the real 2024 item.
- **Charm of heroism** (XDMG p. 99): a Magic action to gain a *potion of heroism* (10 Temporary Hit Points for 1 hour plus *Bless* effect); the charm vanishes.
- **Charm of vitality** (XDMG p. 99): a Magic action to gain a *potion of vitality* (removes Exhaustion and the Poisoned condition; for 24 hours regain the maximum for each Hit Point Die spent); the charm vanishes. **R r50:75 says it "typically grants advantage on Constitution saving throws". That is wrong.** PREV r50:83 is correct.
- Spells R names are all druid spells in XPHB: *Mass Cure Wounds*, *Conjure Elemental*, *Wall of Stone*, *Contagion* (5th); *Control Weather*, *Sunburst*, *Earthquake*, *Tsunami*, *Antipathy/Sympathy*, *Animal Shapes* (8th; *Tsunami* and *Animal Shapes* are druid-only).
- **Hidden effects of "any druid spell of fifth level or lower":** *Revivify* (3rd; 300 gp diamond consumed), *Reincarnate* (5th, druid-only; 1,000 gp oils consumed), *Greater Restoration* (5th; 100 gp diamond dust) and *Heal* (6th, at r25) are on the druid list. *Raise Dead* and *Resurrection* are not. With "no components from you" Jeryth would raise the dead through *Revivify* and *Reincarnate* once per quest. FG excluded raising the dead (FG r50 :216); the Enclave brief needs a ruling.
- *Control Weather* needs the caster to be outdoors (XPHB); useless in Undermountain. *Earthquake* "would not trigger a ceiling collapse" in Undermountain (WDMM :538).
- **Fabricate is a Wizard spell (XPHB). It is not on the druid list.** See §4c.
- XMM CRs: Brown Bear 1, Dire Wolf 1, Giant Eagle 1, Druid 2, Scout 1/2, Warrior Veteran 3, Giant Crocodile 5, Aboleth 10, Chuul 4, Intellect Devourer 2, Awakened Tree 2. XMM has **no Cranium Rat, Pigeon or Gull**.
- WDH 3705 makes Melannor "chaotic good" with half-elf traits; NF-M :6 and R/PREV say neutral good (§8, item 14).

### 4c. The renovation help is missing and uses a spell the Enclave cannot cast
- `ev-04-the-factions-come-calling.md:57` lists "*Fabricate* casting: -250 gp off renovation cost ... Melannor visits twice to cast." `02-operating-costs.md:82` says "*Fabricate* on salvaged materials reduces renovation cost by 250 gp. Two craftsmen free for one tenday. Ask: leave the oak tree undisturbed; allow silverbark growth on it." `02-operating-costs.md:28` also has the Enclave replace the Watchful Order ward (2 gp/tenday) with "monthly visits from a druid who will have opinions about the oak tree".
- No EE event delivers any of this (R/PREV FM). FG's FM delivers its renovation help because no other event does (FG FM design notes :310).
- **Recommendation.** Deliver it in `00-first-meeting` as a party-level box, given once. Replace *Fabricate* with druid-list spells that exist in XPHB: *Stone Shape* (4th; Cleric, Druid, Wizard), *Mending* (cantrip; includes Druid), *Wall of Stone* (5th). Keep the 250 gp value, the oak-tree string, and the two craftsmen for one tenday; let Tally supply the timber work. Keep or drop "monthly druid visit" in a decision (§10 decision 4). The edit to ev-04 and the manor guide is out of scope for the pages and goes in the log (§12).

### 4d. Procedures the rank events must write (zero-prep, from the FG/H/DR model)

**Springwarden (FM benefits box).** Per member: Renown 1; the *charm of restoration* (3 charges); the Phaulkonmere haven. Haven procedure to write: who may enter (member plus companions, a stated number), hours (main gate by day; any hour with the s01 key), what it gives (a long rest in the garden; no fee), what it does not give (not a refuge from the Watch; "no faction will openly violate" means Response Teams do not enter and do not fight inside the walls, but may watch the street), and a loss rule for bringing a pursuer in or fighting inside. AB 297 and G04 :53 say only "neutral ground". Needs a ruling on Response Teams (§10 decision 5).

**Summerstrider (r03).**
- *Relay.* Contact: Melannor at the gate, or a written note left in the gate box. Request carries a recipient description and a delivery place Melannor has visited, at most 25 words; one per member per tenday counted from that member's own last request; reply carried back by the same Beast. Wards only; not Undermountain.
- *Healing.* At Phaulkonmere only, free, for injuries from Enclave business since the member's last visit. Fixed list recommended: *Cure Wounds*, *Healing Word*, *Lesser Restoration*, *Protection from Poison* (all XPHB, all on the druid list); *Greater Restoration* with Jeryth supplying the diamond dust once per tenday. State which companions are healed (recommend: none; the member only, matching FG/H/DR "companions get nothing").
- *Network.* Replace "any ward the GM selects" (R r03:74) with a fixed table, one entry per ward, drawn from content the Enclave quest hooks already set: `arc-g-cassalanter-villa.md:39` (Sea Ward butterfly garden), `arc-f-xanathars-lair.md:35` (sewer airflow), `arc-e-faction-outposts.md:85` (Southern Ward disturbance), `arc-h-sea-maidens-faire.md:37` (fish avoiding the *Eyecatcher*), `arc-i-kolat-towers.md:37` (but see §6, Manshoon gate). Each report is one fact the network could see, as the Harper contacts' answers are (H r03 :134).

**Autumnreaver (r10).**
- *Jeryth's spell.* Write the conduit. Jeryth is disembodied and tied to the estate (R 00:48; WDH 3717). WDH has her cast spells only "in defense of her estate" and on petition at the estate (WDH 3718). R r10:44 says "Tell me what you require and when. I'll have it ready", with no place. Options in decision 6. Fix a list (as FG r03 fixed six spells), exclude *Revivify* and *Reincarnate* or rule on them, exclude *Wish* (CLAUDE.md), and state notice, limit per quest, who is the target, who holds Concentration.
- *Beast.* Brown Bear, Dire Wolf or Giant Eagle, all CR 1 (XMM). Counts in Ally Power as a CR 1 ally: Tier 1 Power 22, Tier 2 Power 17 (`harpers-mechanics-reference.md:14`). State the limit (one operation per quest), the loss rule (if it falls, Melannor replaces it once, a tenday later), and that it is the member's alone to call.
- *Sewer routes.* Give the three entries a fixed destination in WDMM Level 1. WDMM Level 1 has an Entry Well through the Yawning Portal and nothing in the key that connects to a Waterdeep sewer; Level 1 area 25 (Excavation Site, a Xanathar goblin tunnel; WDMM :3329) and area 5 (Grell Hideout; :2582) are natural endpoints, and the second links the Dock Ward route to **The Grells in the Dock Ward** (grells in a Dock Ward warehouse). Offer to report 04.

**Winterstalker (r25).**
- *Melannor in the field.* Recommend the XMM Druid block (CR 2, 44 HP, AC 13), with WDH's racial changes and NF-M's alignment (not WDH's chaotic good). Tier 2 Power 23, which is light for a "capable combat ally" at the level Renown 25 arrives; alternatives: the Druid with fixed prepared spells, or a custom block (a decision for the boss-design pass; FG used the 2024 **Mage** for Ysmay, FG r50 :147).
- *Jeryth, 8th level.* Fixed list: *Sunburst*, *Earthquake* (no collapse below), *Tsunami*, *Antipathy/Sympathy*, *Animal Shapes*, *Heal*, *Heroes' Feast*; *Control Weather* only with the outdoors note. State that *Wall of Stone*, *Stone Shape* and *Earthquake* cannot reshape Undermountain walls, floors or ceilings (WDMM :538).
- *Advance intelligence.* G04 :56 gives "Advantage on Wisdom (Animal Handling) checks and on their first Initiative roll" for a Beast, Plant or Elemental. **Animal Handling affects Beasts only.** Fix per creature type (Wisdom (Animal Handling) for Beasts; Intelligence (Nature) for Plants and Elementals) or use one check for all. The R example (a Giant Crocodile, XMM CR 5) sits in "Southern Ward cisterns", which overlaps the Castle Ward cisterns of M5 and M6; rename the place.
- *Sarna Dath.* Fixed contents of the reports: the Sea Maidens Faire fleet is "the carnival fleet" and "the *Eyecatcher*'s crew" to her. Her reports can feed the Tarsakh 20 deadline (Faire sails at dawn; `structural-rules.md` calendar). **Timing risk:** Tarsakh 20 is about day 50 after Ches 1, and Renown 25 is late (G04 calibration: "approximately Renown 30-35 by the late heist quests", `01-overview.md:7`). If r25 arrives after Tarsakh 20, the Faire reports are moot; widen her beat to "ships of all four factions" and the Faire only until it sails.

**Master of the Wild (r50).** See §7.

### 4e. Recommended scene lists

**00-first-meeting** (`# <Title>`; "A Message from the Gate" or similar): Summary with Candidates and Companions and What Is Actually True; `### The White Cat`; `### Phaulkonmere` (Melannor: social block, qna on the Enclave, the beholder, why us, the gold, Talisolvanar); `### Jeryth's Voice` (social block, qna: safe, the disturbance, what she wants); `### Each Candidate's Answer` (Recording, accept and decline readalouds, `Springwarden Benefits`); `### Leaving the Gate` (the renovation help, "I'll be in touch"); Concluding with outcomes. If the user wants the H-style background color (§10 decision 12), add a short garden/estate scene (estate oaks, birds, the paddock) with no clue.

**s01**: Summary (members only; fires per member after their own M1 is complete, §5b); `### The Cat Again`; `### The East Gate` (key; haven at any hour); `### Jeryth's Welcome` (two lines, unchanged); Concluding; the key is personal and not lent (as the Tower letter, FG FM :225). Outcomes: **East Gate Key Given** (per name; read by r03, the haven procedure).

**s02**: see §5c.

**r03/r10/r25/r50**: Summary (trigger, three or four benefits), `### The <animal>` (contact object), `What Is Actually True`, `### At Phaulkonmere` with Melannor/Jeryth social blocks, one `[!exploration]` box of procedures per benefit, `Renown Opportunities` ("awards no Renown"), `Aftermath`, `Concluding` with outcome and "reads" line, Overview, Summary.

---

## 5. Outcomes: what each event reads and writes

### 5a. Outcome inventory in R/PREV that touches this scope

| Outcome (PREV name) | Writer | Reader (as stated) |
|---|---|---|
| **Emerald Enclave Joined** (party-level) | 00-first-meeting; also written by `ev-04:103-104` | every EE mission, s01, ev-04 |
| (none) | s01 | (none) |
| (none) | s02 (flag tracking is "in M6", PREV :195) | (none) |
| **Summerstrider Reached** | r03 | r10; "any mission that checks the relay or healing" |
| **Autumnreaver Reached** | r10 | r25; "mission events that check beast or 5th-level spells" |
| **Winterstalker Reached** | r25 | r50; "any quest that checks Melannor in the field or 8th-level spells" |
| **Master of the Wild Reached** | r50 | any Mad Mage event |
| **Undermountain Commission Accepted** (R) / **Illuun Watch Accepted** (PREV) | r50 | Mad Mage events |

Mission outcomes the rank and standalone events could read (names from PREV; M-scope reports own them): M1 **Scarecrows Cleared**, **Splinter Site Reported**, **Farm Damaged by Fire**; M2 **Pattern Documented**, **Bones Kept Safe**, **Jeryth's Message Received**, **Brandath Crypts Visited**; M3 **Doppelgangers Departed**, **Traitor Identified**, **Bonnie's Method Honored**; M4 **Mirsa Rescued**, **Pier 17 Investigated**, **Grell Escaped**; M5 **Cache Destroyed**, **Raeve Identified**, **Cultists Escaped**; M6 **Anchor Destroyed**, **Illuun Contact**. No R/PREV rank or standalone event reads any of them except r50's PREV branch on M6 completion (PREV r50:25).

### 5b. Recommended outcomes and readers for this scope

Rule: one writer per outcome, marked with the member's name, with a named reader (brief, "Event Outcomes").

| Outcome | Writer | Reader | Note |
|---|---|---|---|
| **Emerald Enclave Joined** | 00-first-meeting, per name | G04, ev-04, every EE event | per-character; late acceptance same outcome |
| **East Gate Key Given** | s01, per name | r03 (haven wording) | small, optional; or fold the key into the haven box and write no outcome |
| **Summerstrider Reached** | r03, per name | r10; the relay, healing, network procedures | track per member: last relay date, ward reports taken, last healing |
| **Autumnreaver Reached** | r10, per name | r25; M5/M6 beast and spell support | track the beast chosen and spell use per quest |
| **Winterstalker Reached** | r25, per name | r50; the Vault of Dragons (Jeryth/Melannor at the opening) | track Melannor's mission per quest, 8th-level spell use per quest |
| **Master of the Wild Reached** | r50, per name | Dungeon of the Mad Mage (unconverted) | |
| **Undermountain Commission Accepted** | r50, per name | Dungeon of the Mad Mage (unconverted) | keep the R name (it is not Illuun-specific, §6); see §8 item 11 |
| (s02 outcomes, §5c) | s02 | M5, M6, Vault of Dragons | |

What the rank events should read from the missions (recommendations; M-scope reports decide the rest):
- r03 reads **Splinter Site Reported** (M1) for one network line about the Undercliff, if marked.
- r10 reads **Grell Escaped** (M4) for the Dock Ward route line: if a grell escaped, the fishmeal-warehouse entry is where it went.
- r25 reads **Cache Destroyed** (M5) and **Raeve Identified** only if Sarna's first report needs them; avoid Cassalanter content.
- r50 reads **Anchor Destroyed** and **Illuun Contact** (M6), not the Vault's resolution (§7).

### 5c. s02 shape
**Facts.** R is one file with five surges. PREV adds three concrete sites. Both have the same trigger chain: Fireball! (One), Faction Outposts attunement (Two), first Eye (Three), second Eye (Four), third Eye (Five). `arc-e-faction-outposts.md:67` independently seeds Illuun's dreaming "compressed within the Stone", which leaks slightly more when a character attunes. `arc-j-vault-of-dragons.md:47, :256, :274` reads M6 for Jeryth's readiness and an Illuun vision.

**Gate conflict.** The shared gate ladder (brief) has M5 at Renown 10 and 6th level, M6 at Renown 13 and 7th level. Level 6 comes after two lair heists, Level 7 after the fourth (CLAUDE.md Milestone ladder; "Level 7 requires Kolat Towers"). FG decision 2 plays M6 "at 7th level, after Kolat Towers ... Parties that run three heists play M6 after the Vault" (FG conversion brief :41-48). R s02 Surge Five fires at the **third Eye** and tells the party to do M6 "within the tenday" (R s02:134), when most parties are 6th level and M6 is gated at 7th. Surge Four (second Eye, level 6) is consistent with M5's gate.

**Options**
- **A. Reports only (R).** Cheapest, but the requests and the renown triggers are vague ("if Melannor confirms 'useful'", R s02:44), which is the zero-prep gap.
- **B. PREV's concrete sites.** Concrete, but adds three encounters (cranium rats, not in XMM; two intellect devourers, which must use the Occupying Devourer, Harper reference §5; a ward-seal scene), overlaps the M5/M6 cistern thread and FG's and Harper's devourer scenes, and PREV Surge Four never asks for M5.
- **C. Hybrid (recommended).** Keep five short information/social events (one folder, five event files; each with its own trigger, symptom, request and outcome). Make the requests small, organic and tied to content that already exists, with no new fights:
  - One: report any aberrant activity from **Finding Floon**'s sewer hideout or **Gralhund Villa** (Nihiloor's movements; `arc-d-gralhund-villa.md:340`) to Melannor. +1.
  - Two: Jeryth's "keep the Stone moving". No renown; the reward is Illuun's reduced attention.
  - Three: report a coordinated aberrant encounter from the first lair heist (Xanathar's Lair's intellect-devourer implants, or Nihiloor's wing). +1. A second path: Jeryth's awakened rat shows the way to the staircase in the Castle Ward sewers (WDH 15181), which is the Three Clue Rule path to Xanathar's Lair for EE members that WDH gives and no R/PREV event carries.
  - Four: ask for M5 (as R). +2 when M5 is finished before the third Eye (the guide's "assist Jeryth at her request", G04 :47).
  - Five: wording must not promise "within the tenday"; say Jeryth's voice grows intermittent and M6 is the answer; tie to the actual M6 gate (decision 7).
- Renown stays inside the guide's Earning Renown list (G04 :43-47) or in named `+1 Renown:` lines (FG decision 5).

**Outcomes (recommended names, one writer each, marked per member briefed).** **First Stirring Reported** (One), **Stone Kept Moving** (Two), **Cistern Dreams Reported** (Three), **Fouled Channel Requested** (Four; read by M5 and by Five), **Silence Warning Given** (Five; read by M6 and by **Vault of Dragons** (unconverted) for Jeryth's presence). The brief says titles come only from rank events; none of these touches rank.

---

## 6. Secrecy gates

- **Manshoon.** R/PREV in this scope never name Manshoon or Kolat Towers. Keep it that way: until **Manshoon Named** is marked for the listener, Melannor and Jeryth say "the Splinter" or "the other cell" (brief; FG FM :25, FG s01 :19, :63, FG r50 :37). Risks:
  - Phaulkonmere is "one block south of Kolat Towers" (WDH 3700); Kolat Towers sits in the Trades Ward (WDH 560). If the ward is corrected to Southern, Melannor must not point at the neighbouring towers. `arc-i-kolat-towers.md:37` has Melannor describe dead birds and killed grass around the force field; that is the Kolat Towers quest's content and only works after Manshoon Named (or as an unnamed landmark observation).
  - The r03 network table must not use the Kolat block until **Manshoon Named** is marked for that member.
  - G04 :67 names "Manshoon Splinter contamination" in the M5 summary (OOS :133 already logs this as a T hit).
- **Cassalanters.** Nobody in this scope may say they are infernalists or bound to a devil. G04 :30 and `arc-e-faction-outposts.md:85` have Jeryth sense an "infernal" resonance in the Sea/Southern Ward that she "cannot trace to a specific address". Treat that as a druid's sense of fiendish presence, not knowledge of a family: allowed in the Cassalanter Villa quest hook, not in these events. `arc-g-cassalanter-villa.md:535` has the Enclave attribute the ritual to the Cassalanters (OOS :214 logs it).
- **Jarlaxle / Bregan D'aerthe.** Sarna Dath's reports (R r25:71-78) cover the Sea Maidens Faire fleet and "unusual night cargo in the deep harbor". She calls it "the carnival fleet". She never says Jarlaxle, Zardoz Zord or Bregan D'aerthe (only the Cassalanter secret and Jarlaxle's own identity are special-cased in BD r03 :27-38). If a BD-member PC is present, Sarna still has nothing on the company.
- **Illuun.** Jeryth never names it ("old, patient, and hungry", R s02:15). WDMM names it (Level 4 `Aboleth` entry, WDMM :11344). Recommend: the name enters play only through **Illuun Contact** or **Anchor Destroyed** (M6), so r50 may say "Illuun" only for a member for whom either is marked; otherwise Melannor says "whatever is sleeping below" (R r50:99).
- **Vault, Stone, gold.** The Enclave has no stake in the gold (AB 285; ORG :17; WDH-style). R 00:42 gates the gold answer behind a DC 12 Persuasion check; as a stated position it needs no check (the position is public in the guide) and a check would waste the line. Keep it as a question the player can ask.

---

## 7. r50 and the Dungeon of the Mad Mage set-up (WDMM integration seeds)

**Facts from WDMM** (`sources/adventure-wdmm.json`):
- **Illuun is in WDMM.** Level 4 (Twisted Caverns) features "Illuun the aboleth, along with its pet chuuls and enslaved troglodytes", in the lake cavern, area 16 Grotto of Madness (:11344, :12834). Its presence has tainted the underground river; it "plans to take over the entire level as a step toward gaining control of Undermountain and then Waterdeep" and "rarely leaves its watery lair" (:11344). It sends an intangible **magical projection** to talk to intruders (Level 4 key). Level 4 is "designed for four 8th-level characters" (:11330), which matches r50 timing.
- **Halaster placed the kuo-toa's old god, Bulba-Slopp, in that grotto** (area 16a, :12834): "Halaster turned it to stone and lured kuo-toa to the grotto." That is a ready-made Halaster fingerprint for CLAUDE.md's "Halaster may be ... subtly interfering".
- A svirfneblin druid left the **Zurkhwood Grove** (Level 4, area 13) when the aboleth arrived, after casting *awaken* on seven zurkhwoods (:12756). A natural Enclave-adjacent NPC (no name in WDMM).
- **Wyllowwood** (Level 5): Wyllow, a moon elf archdruid, chaotic neutral, with a displacer beast, grief, and no memory of the surface; she "turns violent whenever her forest or its peaceful denizens are threatened"; Halaster made the forest with *wish* spells (WDMM :13213). A strong Enclave seed: Jeryth might know the name; she is the kind of person the Master of the Wild is asked to find.
- **Alterations to Magic** (WDMM :532-538): no spell other than *wish* can enter, leave or move between levels; teleport, plane shift, word of recall, astral projection fail; banishment fails; magic from deities still works; spells cannot reshape Undermountain's walls, floors or ceilings; *Sending* cannot reach Halaster (it is redirected to the nothic secretary, Level 9 area 31).
- WDMM Level 1 has an Entry Well from the Yawning Portal; area 25 and area 5 are Xanathar and grell content (see §4d).

**Facts from R/PREV r50.**
- The event is "designed for Dungeon of the Mad Mage" (R r50:15-18; R r25:92).
- Hold and branch: R reads "Vault of Dragons has already resolved" (:18); PREV reads "The Dreamer's Reach (Mission 6) is complete" (:25).
- The six rangers and druids, the beast compact and the commission are unnamed and mechanically undefined (R r50:40-44, :81-85, :95-111). The compact's CR line is "moderate danger" in R (:85) and "CR 2 or lower" in PREV (:96), G04 :57.
- Outcomes: R names **Undermountain Commission Accepted**; PREV **Illuun Watch Accepted** (§8 item 11).

**Recommendations.**
1. **Fire when the member surfaces.** Hold until **Winterstalker Reached** is marked and the member is above ground (FG r50 :16). Animals cannot reach a member below ground unless they walk through the r10 routes; Undermountain levels are not connected for Beasts by gates. Recommend: three animals arrive at the Yawning Portal's courtyard or Trollskull Manor the first morning the member is on the surface. (No *Sending* analogue exists; do not invent one.)
2. **Branch on M6, not the Vault.** Read **Anchor Destroyed** and **Illuun Contact**, as PREV did. If **Anchor Destroyed** is marked, Jeryth's remarks refer to the dreamer's "surface hold" being broken; if not, they are forward-looking. If **Illuun Contact** is marked for a member present, Jeryth adds one line that Illuun knows that member (G04 / `arc-j-vault-of-dragons.md:47`).
3. **Name the six.** Recommend three rangers and three druids as Scout (CR 1/2) and Druid (CR 2) blocks, unnamed except the leader (a decision). Ally Power (Tier 2): Druid 23, Scout 12; compute with the CR 2.0 builder at the 8th-level Party Power for 3, 4 and 5 PCs, and use FG's rule that the allies who fight number one fewer than the PCs (FG r50 :138, :145-167). The party-level gift and the ally block are different things: the charm goes to every character present, the six serve the promoted member (CLAUDE.md "Members only" for briefs; OOS :51 treats the charm as a legitimate party-wide gift).
4. **Define the beast compact.** Beast of CR 2 or lower, Intelligence enough to follow one clear instruction, one task per quest, not endangering it. The CR 2 cap matches G04 :57 and `player-factions-overview.md:86`.
5. **Define the commission.** What the Enclave provides below, by WDMM fact:
   - *Supply and relay:* through the r10 routes to Level 1 only; no animal messenger reaches Levels 2-4 faster than 25-50 miles per day and cannot cross gates.
   - *Jeryth's reach:* she cannot enter; she can feel the tainted river. Her contact is the groundwater/root link and, below Level 1, the signal marks (the three marks in R r50:127). State in one line that the marks work on Levels 1 to 3 (the surface-adjacent levels) and that the Enclave's information about Level 4 comes only from the member.
   - *The target:* Melannor names where the root is anchored only as "below the Castle Ward", as GM text names it Level 4 area 16.
6. **Seeds block (one-line facts, as FG r50 :370-380).** Use: Illuun's lair is Level 4 area 16 and its projection; the Bulba-Slopp fingerprint; the svirfneblin druid of Zurkhwood Grove; Wyllow of Level 5; teleportation and *Sending* limits (the same Halaster facts FG records); earthquake and stone-shaping limits; **Control Weather** requires outdoors. Say that WDMM has no Enclave content, so these are the only hooks.
7. **Do not duplicate other r50 seeds.** Laeral's wane and the Runestone belong to Lords' Alliance and FG (FG r50 :376-380).
8. **Mad Mage interference.** Halaster aware of or interfering in the Enclave's thread: the grotto fingerprint is canon. Do not make him the cause of the surges.

---

## 8. Contradictions (R, PREV, guide, org/NF, sources, other quests)

1. **Ward.** R 00:7, :80 "Sea Ward"; `arc-g-cassalanter-villa.md:535` "ley line running through the Sea Ward beneath Phaulkonmere" vs WDH 1320, 3690, 3700, AB 292, 309, ORG :19, `arc-b:123`, `arc-e:85` "Southern Ward". Recommendation: Southern Ward; log arc-g.
2. **Cat message.** R 00:26 drops the WDH/AB line "Interested in joining the Emerald Enclave?" (WDH 3690; AB 292).
3. **Party-level outcome.** R 00:7 says each eligible character; R 00:68, PREV 00:150 and `ev-04:103-104` mark one party flag.
4. **Fabricate.** `ev-04:57`, `02-operating-costs.md:28, :82` use *Fabricate* (Wizard-only, XPHB); `ev-04:57` says Melannor "visits twice to cast", `02-operating-costs.md:82` says "two craftsmen free for one tenday". No EE event delivers either.
5. **Charm.** AB 377 *heroism*; G04 :57, `faction-affiliations.md:81`, `player-factions-overview.md:86`, R r50:11 *vitality*; R r50:75 describes it wrongly; PREV r50:83 correctly. M4 gives *heroism* (R m04 ev-01:62).
6. **"Spoke directly for the first time."** R m04 overview:17 and ev-01:97 say Jeryth "speaks directly to the party for the first time" at M4, but she speaks in R 00:46-56, R s01:49-53, R s02:68 (Surge Three) and R r03:56. Out of scope to fix (report 03/04), but it breaks the s01 beat "I know what you did."
7. **Mission gates.** R missions: M1 R0/L2 (m01 overview:6), M2 R1/L3 (m02:6), M3 R3/L4 (m03:6), M4 R6/L5 (m04:6), M5 R9/L6 (m05:6), M6 R12/L7 (m06:6). Brief: M2 R3/L3, M3 R5/L4, M4 R8, M5 R10/L6, M6 R13/L7. s02 and the rank events do not state gates; the new pages must use the brief's.
8. **s02 Surge Five vs the gate ladder.** See §5c.
9. **s01 vs r03 timing.** M1 base 2 plus joining 1 reaches Renown 3 exactly at M1's end, so s01 ("after the first EE mission", R s01:5) and r03 (Renown 3, R r03:7) fire the same day, both at Phaulkonmere, both with Jeryth speaking briefly. Recommend: s01 by cat in the M1 debrief evening (key and "I know what you did"), r03 by pigeon at noon next day (BD r03 design notes :29 and DR r03 :11-20 use the same next-noon rule). Option: merge s01's key into FM and drop s01 (rejected: the folder exists in G04 :79).
10. **Per-character vs party-level benefits.** R r03:41 "Any character injured on Enclave business" and R r10 "the character" are individual in intent; R s01:69 "Any party member with the east gate key" is per key. R r50 gives the *charm of vitality* to "every party member present" (a party-wide gift), but also R r50:121 says the flag is for "the character". Resolve with per-member outcomes and a party-wide gift line.
11. **Commission outcome name.** R `Undermountain Commission Accepted` (r50:119) vs PREV `Illuun Watch Accepted` (r50:128). Recommend the R name; the PREV name forces Illuun's name into the outcome for a member who has never learned it.
12. **r50 branch.** R r50:18 branches on **Vault of Dragons** resolution; PREV r50:25 on M6.
13. **Animal messenger vs the benefit.** R r03:37 "any address in Waterdeep ... by morning, usually" vs XPHB (visited location, Tiny Beast, 25 words, 24 hours).
14. **Melannor's alignment.** WDH 3705 "chaotic good"; NF-M :6, R/PREV "Neutral Good".
15. **Guide mission renown vs AB.** AB 393-396 +1/+1/+2/+2 (four missions); G04 :63-68 +2/+2/+3/+3/+4/+4 (six). The guide matches the calibration rule. No change.
16. **PREV s02 vs R s02.** Concrete sites in PREV (:65-69, :125-127, :144-160) vs R's reports. PREV's Surge Four ward-seal replaces R's M5 request; the s02 Next Steps (PREV :199) then lacks M5 as a prerequisite. R's M5 request (R s02:105) is what the M5 and M6 files expect.
17. **Occupying Devourer.** PREV s02 Surge Three (:125) has "two intellect devourers ... implants a larva" (the XMM brain-eating block). Harper reference §5 is binding wherever an intellect devourer appears.
18. **Cranium rats.** PREV s02:65-67 uses a cranium rat colony; XMM has no Cranium Rat (`bestiary-xmm.json`).
19. **Gate hook for Xanathar's Lair.** G04 :29 (herb sprig) and `arc-f-xanathars-lair.md:428` and WDH 15181 (Jeryth's awakened rat shows EE members the lair stairs) are delivered by no EE event.
20. **R / WDH on the vault gold check.** R 00:42 puts a DC 12 Persuasion check on a stated public position (§6).
21. **Illuun as "Stone-compressed" vs "Level 4 aboleth".** `arc-e-faction-outposts.md:67` says "the aboleth consciousness compressed within the Stone"; R s02:20-22 and R m06:18 say Illuun is anchored to Level 4 and the Stone "resonates"; WDMM has a single aboleth Illuun in area 16. Both can be true (the Stone holds a link), but one sentence in the design notes must state it.
22. **NF-M page.** "Featured in" lists Trollskull Alley, Fireball! and the lair quests, which suits the network content; it lists no rank event. Not a contradiction.

---

## 9. Standing-rule hits

- **Retired formats.** R in scope uses `> **[GM]**` (00:3, 70; s01:3, 146, 171; s02:3, 107, 136, 149; r03:3, 70; r10:3, 90; r25:3, 86; r50:3, 107, 123), `**Background (DM only)**` (00:16; s01:121; s02:19; r03:15; r10:14; r25:15; r50:20), `[!profile]` (00:58; s01:163; r10:79), `[!design]` (r50:15), `[!lore]` (s02:26), `[!tip]` (r03:49; r10:52; r25:43, 56, 77; r50:74), `#### ... : True / False` (00:67; r03:66; r10:86; r25:82; r50:115, 119), `#### Milestone: None` (s02:155), a separate `## Read Aloud` section (00:82; s01:183; s02:163; r50:137). PREV removes most of these. The new pages use `[!gamemaster]`, `[!readaloud]`, `[!social]`, `[!qna]`, `[!exploration]` only.
- **Members-only.** R r03, r10, r25, r50 are individual in the trigger, but no event says companions get nothing; s01 and s02 say "the party" (R s01:5, s02:7); FM outcome is party-level. Fix per §3b and §5b. Late sittings: a member who missed a surge or a rank can climb later and gets the same award (FG s01 :269).
- **Renown calibration.** s02 R lines: +1/+1/+2 with vague conditions; new pages use the guide's ordinary rewards and named `+1 Renown:` lines. Rank events award no Renown (§1).
- **Renown ladder wins.** No R/PREV mission or standalone event changes rank. The Winterstalker and Master of the Wild text says rank is by renown; keep.
- **Event Outcomes.** R uses `True / False` headings and PREV party-level names; see §5b.
- **No Milestone Points.** R s02:155-157 uses `Milestone: None`; PREV uses "This event does not award a Milestone Point"; the new pages end with "This Event awards no Milestone Points."
- **Wish.** Not mentioned in R/PREV; Jeryth's list needs an explicit "except *wish*" line (druid list excludes it anyway, XPHB).
- **Intellect devourer.** PREV s02:125; must use the Occupying Devourer (Harper reference §5).
- **2024 rules.** Items in §4b. Also: the Druid XMM block replaces "Druid stat block" (R r25:44 lacks the 2024 label).
- **Quests, not arcs.** `ev-04:57` etc. fine. AB uses "arc"; R/PREV use "quest". R s02:105 uses "(Mission 5)"; the new pages call it **The Fouled Channel**.
- **BD rejects Lolth.** Not touched in scope.
- **Profanity.** Melannor and Jeryth never swear (VOICE :11, :29). Sarna Dath (a harbor fisher) has no profile; she is voiced from the event text and may swear moderately.
- **Dialogue voice.** Jeryth speaks one or two sentences, spaced out (VOICE :27), a deliberate break from the 11-15 word rule.

---

## 10. Decisions the user must make

1. **Candidates.** (a) every unaffiliated character is a candidate (recommended); (b) only nature-aligned characters (ev-04 eligibility, with no outcome to test it); (c) a hybrid. Recommend (a), with the nature-aligned trigger deciding only who the cat finds first.
2. **Ward.** Southern Ward (WDH, AB, ORG, arc-b, arc-e) or Sea Ward (R, arc-g). Recommend Southern; then arc-g:535 is logged.
3. **Offer handling.** No Offer Closed; open gate (recommended) vs a re-fire rule like FG.
4. **Renovation help.** Replace *Fabricate* with druid spells (Stone Shape, Mending, Wall of Stone) and craftsmen, keep 250 gp, and deliver it in the FM (recommended). Also decide whether "monthly druid visit replaces the Watchful Order ward" (manor guide :28) is kept.
5. **Haven.** What "no faction will openly violate" means for Response Teams: (a) they never enter the estate and never wait at the gate; (b) they never enter but may watch the street (recommended); (c) they may enter at Lockdown.
6. **Jeryth's casting.** (a) at Phaulkonmere only; (b) through a charged conduit the member carries (acorn, sprig; the herb sprig already exists as a G04 :29 hook) (recommended); (c) anywhere she has roots. Include a ruling on *Revivify* and *Reincarnate* (exclude both; or allow *Reincarnate* at the estate only).
7. **s02 shape and the Surge Five/M6 gate.** Option C hybrid (recommended). Decide whether Surge Five promises M6 "within the tenday" at the third Eye, or ties to Level 7 like FG decision 2.
8. **s01/r03 sequencing.** s01 at the M1 debrief by cat, r03 next noon by pigeon (recommended).
9. **r50 beasts and the six.** Define the six (3 Scouts, 3 Druids?) and the compact's CR cap (2, per guide).
10. **Commission outcome name.** **Undermountain Commission Accepted** (recommended) vs **Illuun Watch Accepted**.
11. **Melannor's stat line.** XMM Druid with NF-M's alignment, or a custom block for r25.
12. **First Meeting background scene.** Whether to add an H-style estate/garden background scene (explicitly irrelevant, no clue), as the user asked for the Harpers. No Enclave request on record.
13. **Charm of restoration charges.** Whether to give it the XDMG 3-charge text and track charges, or to keep it a one-off feeling.
14. **Sarna Dath's timing.** Whether Faire-fleet departures stay central given Tarsakh 20 (day ~50) vs Renown 25.

---

## 11. Settled facts to keep, and parts to drop

**Keep (names, locations, numbers that other files read):**
- Names: Melannor Fellbranch (half-elf druid, brother of Talisolvanar "Tally" Fellbranch; NF-M :26), Jeryth Phaulkon (Chosen of Mielikki, disembodied), Phaulkonmere, Sarna Dath (south quay, blue-and-white boat), Gerrick Goodbarrel and Bertio Caskwall (mission and s02 PREV; no collisions found outside the folder).
- Rank names and thresholds: Springwarden 1, Summerstrider 3, Autumnreaver 10, Winterstalker 25, Master of the Wild 50 (G04 :51-57; AB 373-377).
- The contact animals and their order: cat (FM, s01), pigeon (r03, M1), in person (r10), owl at dusk (r25), three at once (r50).
- Lines worth keeping verbatim: "I'll be in touch."; "East gate. Opens from either side. No need to knock or announce yourselves."; "I know what you did."; "This garden is yours now. Come when you need it. There are no conditions."; "Once is the agreement."; "This is the rank where I stop sending things and come myself."; "Find another way." (R/PREV; VOICE fits).
- The cat's characteristic: Melannor's baritone from behind its eyes (PREV 00:23).
- The sewer routes: the three entries (Sea Ward dyer's district drainage channel, Southern Ward deep cisterns, Dock Ward fishmeal warehouse), the twelve years, the three-lines-over-a-leaf mark (R r10:59-63).
- The paddock: brown bear, dire wolf, giant eagle (R r10:71).
- r50: three animals, six rangers and druids (four humans, a half-elf, a wood elf), the *charm of vitality* for every member present, "once per campaign", the commission choice, three signal marks (R r50:30-44, :60-72, :127).
- Gift sequence: *charm of restoration* (joining), *charm of heroism* (M4), *charm of vitality* (r50).
- Illuun unnamed in Jeryth's mouth until contact (R s02:15).
- The surge beats: starlings, oak roots two inches, seven cistern dreamers, beaching fish, black well water (R s02:34, :50, :64, :89, :120).

**Drop:**
- All retired blocks (§9). The separate `## Read Aloud` section. `Mission 5/6` numerals in fiction.
- R r50:75 (wrong *charm of vitality* text).
- "Any ward the GM selects" (R r03:74); "GM selects" is a zero-prep violation.
- PREV s02's cranium rats and two intellect devourers with larvae (unless rebuilt on the Occupying Devourer).
- R 00:42's check on a public position.
- "Parties are not expected to reach Renown 50 during Dragon Heist" as a `[!design]` sidebar; put it in one GM line.
- R r10 "Melannor appears at the door" if the member is on a mission; keep, add the hold rule.

---

## 12. Report-back list for the out-of-scope log

- `ev-04-the-factions-come-calling.md:57` and `:103-104`: *Fabricate* (Wizard-only), "Melannor visits twice", and the party-level `Emerald Enclave Joined: True / False`.
- `campaign/guides/trollskull-manor/02-operating-costs.md:28, :82`: *Fabricate*, the monthly druid visit, "two craftsmen".
- `campaign/structure/arc-g-cassalanter-villa.md:535`: Phaulkonmere in the "Sea Ward"; the Enclave attributes the ritual to the Cassalanters (OOS :214).
- `campaign/guides/factions/04-emerald-enclave.md:56`: Animal Handling on Plants and Elementals; :67: "Manshoon Splinter" (OOS :133); :29: the herb sprig has no delivering event; :53-57 lack procedures.
- `campaign/quests/faction-events/emerald-enclave/m04-the-grells-in-the-dock-ward/overview.md:17` and `ev-01:97`: Jeryth "speaks directly ... for the first time".
- `campaign/quests/faction-events/emerald-enclave/m0*/overview.md:6`: R-based gates versus the shared ladder.
- `campaign/guides/gm-guide/player-factions-overview.md:86`, `players-guide/faction-affiliations.md:81`: fine against R; they need the procedures when the pages exist.
- WDH 3705 Melannor "chaotic good" versus NF-M :6.
- `arc-f-xanathars-lair.md:428` and WDH 15181: the Enclave's Xanathar's Lair paths (sprig; awakened rat) are delivered by no event.
- `arc-j-vault-of-dragons.md:47, :274`: reads M6 in the old True/False form (not an EE-file problem).
- `ev-03-the-neighbors.md:20`: the Tally-Melannor connection is promised for EE recruitment; the FM must pay it off.
