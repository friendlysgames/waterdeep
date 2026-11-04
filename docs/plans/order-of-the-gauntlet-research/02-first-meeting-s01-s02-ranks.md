# Order of the Gauntlet research: 00-first-meeting, s01, s02, r03, r10, r25, r50

Scope: `00-first-meeting`, `s01-the-tithe`, `s02-savras-past`, `r03-marcheon`, `r10-whitehawk`, `r25-vindicator`, `r50-righteous-hand`. No campaign file was edited. Report 02 of 5.

**Model reading done.** Read in full:
- Lords' Alliance (newest model, matching scope): `lords-alliance/00-first-meeting/` (ev-01 :1-321, design-notes), `lords-alliance/s01-suspension-and-dismissal/` (ev-01 :1-324, design-notes :1-37), `lords-alliance/r50-lioncrown/` (ev-01 :1-140 and :330-423 in full, headings of :140-330; design-notes :1-28). Headings and rules of `lords-alliance/r03-redknife`, `r10-stingblade`, `r25-warduke` and `s02-escalation-to-the-open-lord` were taken from the Session 44 LA report (`docs/plans/lords-alliance-research/02-first-meeting-s01-s02-ranks.md`, read in full) and spot-checked, not re-read line by line.
- Doom Raiders: `doom-raiders/r03-wolf/` (ev-01 :1-257, design-notes :1-17); `doom-raiders/m03-the-missing-snobeedle/` (overview :1-75, design-notes :1-23; ev-01 not re-read, shape only).
- Bregan D'aerthe: `bregan-daerthe/m02-the-wazoo-affair/` (overview :1-40, design-notes :1-40; ev-01 not re-read).
- Emerald Enclave: `emerald-enclave/00-first-meeting/ev-01` (:1-130 in full, remainder via the LA report), `emerald-enclave/r03-summerstrider/ev-01` (:1-75 in full), `emerald-enclave/s01-a-seat-at-phaulkonmere/ev-01` (:1-30).
- Force Grey: `force-grey/s01-the-full-picture/ev-01` (:1-75 in full, remainder via the LA report), `force-grey/r50-force-grey-commander/ev-01` (:100-175 and :360-380 in full).
- Harpers: not re-read this session (the Harper FM and r50 shapes are taken from the LA report :23-47).
- Also read: all seven OotG folders in R (identical to the live folder, verified with `diff -rq`) and PREV (diffed per file), `campaign/guides/factions/05-order-of-the-gauntlet.md`, `campaign/setting/organizations/04-order-of-the-gauntlet.md`, the Savra and Valdra Notable Figures pages, `.claude/skills/character-voices/voices/order-of-the-gauntlet.md`, `sources/Appendix_B_-_Player_Factions.md` :396-500, `3. Player Character Factions.pdf` (the tithe line), WDH and WDMM JSON (queried with `python3 -I`), the OotG section of `docs/plans/harpers-out-of-scope-notes.md` :101-116, the structure docs `arc-e` to `arc-j` Savra lines, `act-i/trollskull-alley/ev-04`, `act-ii/fireball/ev-01`, `act-ii/gralhund-villa/ev-09`, the M1-M6 overviews of R, and the 2024 data in the scratchpad `5e/` folder.

**Abbreviations**
- `R` = first-commit versions, identical to the live folder `campaign/quests/faction-events/order-of-the-gauntlet/` (line numbers below are R's). `PREV` = `.../scratchpad/ootg-prev/order-of-the-gauntlet/` (R plus retired sidebars and a trim pass).
- `LA`, `EE`, `FG`, `DR`, `BD` = `campaign/quests/faction-events/{lords-alliance,emerald-enclave,force-grey,doom-raiders,bregan-daerthe}/`.
- `G05` = `campaign/guides/factions/05-order-of-the-gauntlet.md`; `G01` = `.../01-overview.md`; `PG` = `campaign/guides/players-guide/faction-affiliations.md`; `GMO` = `campaign/guides/gm-guide/player-factions-overview.md`; `ORG` = `campaign/setting/organizations/04-order-of-the-gauntlet.md`; `NF-S` / `NF-V` = Savra / Valdra Notable Figures pages; `VOICE` = the OotG voice doc; `AB` = `sources/Appendix_B_-_Player_Factions.md`; `WDH` / `WDMM` = adventure JSON, cited by JSON path; `OOS` = `docs/plans/harpers-out-of-scope-notes.md`; `XMM`/`XPHB`/`XDMG` = the 2024 data in the scratchpad `5e/` folder; `LAR` = the Session 44 LA report above.

---

## 0. Top findings (read this first)

1. **No First Meeting in R has an answer scene, a candidate frame, a Chevall benefit, or the renovation help.** The oath is hand-waved as "members who accept"; the outcome is party-level; the Chevall rank (Renown 1) is never delivered (R FM :73-90; G05 :54). WDH says Savra gives a first mission after the oath (`data/3/entries/4/entries/9/entries/1/entries/0`); R gives none (FM :84-86).
2. **Savra's timeline cannot hold.** R r50 :42 has Savra award Righteous Hand "four years ago" in Waterdeep; R FM :18 and s02 :49-59 put her in the cult until three years ago, and the Order took her in afterward. The cult length also disagrees (FM :18 "three years"; s02 :33 "four years"). FM :86 calls her "the only Order member in Waterdeep" while r25 and r50 field a rotation of knights, a "Waterdeep chapter" and "senior council".
3. **The tithe event contradicts the guide.** R s01 :10 pays Renown "whether unprompted or when asked". G05 :46, PG (Renown section), AB (Earning Renown) and ORG :17 all say only an **unprompted** tithe earns it; "those who must be reminded earn only the reminder". It is also a party-level lockout (OOS R3 M), reads a Vault of Dragons that does not read it, and routes the fallout to Sister Valdra, who NF-V says is unsanctioned and unknown to Savra.
4. **Rules errors that must not survive:** Resurrection is a **7th-level** spell with a 1,000 gp diamond in 2024 (R r50 :80 says 5th level); **Ring of Protection and Bracers of Defense are Rare**, not Uncommon (R r10 :51); "weekly" priest briefings (R r03 :39; PREV already changed it to tenday).
5. **Rank-event timing is mostly consistent with the renown ladder, once checked:** Marcheon (R3) lands right after M1 and before M2; Whitehawk (R10) lands before M5 (the gate); Vindicator (R25) lands after M5. So the Whitehawk dossier precedes M5 and the Vindicator "predicate" must be the ledger, not the dossier (R r25 :45 is wrong; OOS r25 R2 T).
6. **Cassalanter secrecy is mostly respected in these seven files** (OOS: "Clean: r03, r50, 00-first-meeting, s02's Cassalanter handling"). The live risks are r10 (temple divination), r25 (the inquiry names "diabolism"), the Savra Past `Cult Funding Linked` arithmetic, and AB :402, which states as fact that the Cassalanters are "active Asmodeus cultists".
7. **Recommended shape:** one `ev-01` plus `design-notes.md` per folder; a per-candidate First Meeting at the Halls of Justice with a deterministic summons (Savra knocks, leaves a sealed note if nobody answers); per-member rank procedures; the tithe asked of each member's own share, with the "unprompted" window stated as a clock; s02 rebuilt on a three-route test; r50 holding for the surface with Mad Mage seeds from WDMM levels 15, 21, 22 and 23.

---

## 1. What the model pages require (copy these)

All page models are summarised in `LAR` §1 (:21-46). Additional observations from this session's reading:

- **First Meeting (LA, EE).** Summary + bulleted abilities, then `#### Candidates and Companions` and `#### What Is Actually True` inside the Summary block (LA FM :14-26; EE FM :13-25). Placement rule is deterministic (LA FM :16 background, then Charisma, then alphabetical; EE FM :15 class, then Wisdom, then alphabetical). The contact object is written once, in full, and "later events refer back to this description" (LA FM :32; EE FM :52-57). A `[!social]` block per NPC with a "happy to discuss" list and a fixed refusal line for Stone, vault and Manshoon (LA FM :104-160). `### Each Candidate's Answer` has Recording, accept, decline and ask-for-time readalouds plus a Benefits box (LA FM :188-250). Party-level help is its own box, given once (LA FM :254-261). Close: `Event Outcomes`, `Next Steps` ending "This Event awards no Milestone Points", `## Overview`, `## Summary` with "After the Meeting" and "Without a Private Meeting" (LA FM :291-321).
- **Rank events (DR r03, EE r03).** Noon-next-day contact object, away-from-Waterdeep rule, several members who cross together attend together (DR r03 :11-20; EE r03 :13-15). `What Is Actually True` (DR r03 :22-24). Each benefit is an `[!exploration]` box with contact, notice, limit, who else, loss rule (DR r03 :114-126). "The rank event awards no Renown" (DR r03 :230-232). Outcome per recipient name.
- **Standalone with a one-time Renown award (FG s01).** Three-route test per element (FG s01 :48-64 table), exactly one question for an incomplete account (FG s01 :66-75), 2 Renown once in the campaign.
- **Consequence event (LA s01).** A trigger table keyed to each mission's own deadline words (LA s01 :34-48), a verdict table of compelling reasons (:50-70), a runner's note at noon (:72-90), suspended-status list by benefit name (:150-165), three ways back (:167-215), dismissal list (:217-250), staging for a table (:260-270), Renown "never reduced" (:272-274).
- **r50 (LA, FG, EE).** Hold until the prior-rank outcome is marked and the member is on the surface (LA r50 :19; FG r50 :14-28). "Fighting allies = PCs minus one" (FG r50 :124-143). `Mad Mage Seeds` is a block of one-line facts (LA r50 :381-390; FG r50 :370-380). The decision is recorded as a named outcome (LA r50 :406-411).
- **Folder shape.** `ev-01-<slug>.md` + `design-notes.md` (What the Source Gave / What Changed / Departures / Invented Names and Open Items; e.g. LA r50 design-notes :1-28). None of the seven OotG folders has design notes.

---

## 2. R and PREV: what each folder contains (facts)

R is the original draft (`> **[GM]**`, `**Background (DM only)**`, `[!profile]`, `[!info]`, `[!design]`, `[!lore]`, `#### X: True / False`, a separate `## Read Aloud`). PREV adds a Savra `[!social]`-style block, extra dialogue and a trim pass. Differences that matter (from `diff` of R against PREV):
- PREV FM Background drops "for three years" (R :18) and adds "Savra has been watching the party since they arrived in Waterdeep. She does not recruit strangers." It rewrites the Cassalanter paragraph with "their bloodline too carefully maintained". Neither is in R.
- PREV s02 drops "four years" (R :33, :49) and "two years" of the tower (R :25). It converts the four outcome headings to `**True:** / **False:**` bullets.
- PREV r03 changes "One briefing per week" (R :39) to "per tenday" (correct for Faerun).
- PREV s01, r10, r25, r50 differ only in punctuation.

### 2a. 00-first-meeting (R :1-116)
- **Trigger.** "When the Order of the Gauntlet row activates in **The Factions Come Calling**", Savra arrives "without advance notice", "at any point during the renovation period". Eligible: "paladins, clerics, characters who demonstrated strong moral conviction during **Finding Floon**" (R :7). `ev-04-the-factions-come-calling.md:28` has the same eligibility and "Savra Belabranta visits Trollskull in person; no advance invitation". WDH: "Any non-evil character can join" (`data/1/entries/11/entries/10/entries/0`); Savra "visits the characters' residence" if the party "includes one or more likely recruits" (`data/3/entries/4/entries/9/entries/1/entries/0`).
- **Scenes.** The Knock (:24-31), the Pitch (:34-52; two targets, the beholder empire "whose upper agents use intellect devourers" and "a mind flayer named Nihiloor" at :38, and an unnamed Sea Ward family at :40), Answering Questions with a **DC 14 Charisma (Persuasion)** gate (:44-52), The Darker Exchange (:54-64; the cult name is given, not the deed; pressing ends the talk, she returns the next morning once, a second press and she does not return), The Decision (:68-74), The Oath (:76-84; silver gauntlet, priest of Tyr, "three commitments", "No coin changes hands. No scroll to sign."), the closing line (:84), the brawl hook (:86).
- **Background (GM) at :16-22.** Cult "three years"; the family is the Cassalanters, "building a case against them for months"; "She says nothing about diabolism or the infernal"; "Both become heist objectives in Act III".
- **Outcome.** `#### Order of the Gauntlet Joined: True / False` (:90), "True if at least one party member took the oath". Next Steps: M1 "unlocks immediately" if True; if False, Savra "returns after **Fireball!**" or "**Gralhund Villa**" with "more specific information about the unnamed family" (:96-100).
- **Holes.**
  1. No answer scene: the Decision (:68-74) ends "If members of the party accept", with no per-candidate mechanic.
  2. Chevall (Renown 1) and its benefit (G05 :54: vouching to temples, healing at cost, free *Cure Wounds* once per day per temple, a bed) are never delivered.
  3. The renovation help: `ev-04:58` promises "Net 100 gp savings; Savra is visible at the site"; `02-operating-costs.md:83` says "No money. Accompanies party to guild meetings in Order insignia -> favorable rates and prompt scheduling. Informal Watch watch-list placement". Two different offers, neither written as a scene.
  4. WDH has Savra give the first mission at the ceremony; R gives none (:84-86) and M1's overview still says "delivers the mission in person at Trollskull Manor" (`m01/overview.md`).
  5. Re-offer: R :72 and :100 have Savra return after Fireball/Gralhund with Cassalanter information for non-members. Fireball (`act-ii/fireball/ev-01:200`) and Gralhund (`ev-09:115`) give Savra hooks for **Renown 1+** only, so a non-member has no such contact.
  6. The oath (:80) says "to act against active evil, to protect the innocent where possible, to hold one another accountable". AB :450 and WDH say "to find evil, to pursue it, to destroy it; to protect those who cannot protect themselves; to stand when standing is required." r50 (:52) repeats the R wording. The two forms differ.
  7. Location: R :78 "a short walk into the Temple District"; WDH `data/3/entries/4/entries/9/entries/1/entries/0` "the Halls of Justice, the temple of Tyr (located west of the Market in the Castle Ward)"; `setting/waterdeep-lore.md:36` lists Tyr among the Sea Ward temples; AB :410 says Castle Ward.
  8. Knowledge: Savra names "Nihiloor" and "intellect devourers" to a party that has "Nihiloor Sighted" only if it ran Q07 in `act-i/finding-floon/ev-04` (:69-93). Naming the mind flayer is information beyond what a party that skipped the hideout holds.
  9. FM :86 "a Zhentarim-funded brawl": which Zhentarim is the Two Zhentarims rule's trap (see §10).

### 2b. s01-the-tithe (R :1-94)
- **Trigger.** "The first time the party recovers a haul of 1,000 gp or more in a single operation ... and at least one party member holds OotG Renown 1 (Chevall)" (:7). Savra arrives "within two days of the windfall becoming known". "Fires once per campaign" (:82).
- **Ask.** "A quarter of it goes somewhere useful ... The choice is yours. The expectation isn't." (:20). Five worthy causes (:24-32): Temple of Helm (Castle Ward), Halls of Justice Legal Aid Fund, Field Ward Soup Houses, Griffon Cavalry Dependents Fund (Savra "does not name this one"), Trollskull Alley Rebuilding.
- **Pay.** "Good." and a nod (:34-42), "they earn the renown and Savra's nod" (:10).
- **Refuse.** "All right." (:44-50). Two days later "a written instruction ... in a clerk's hand" reassigns the party to routine work; "Sister Valdra becomes their contact"; Savra "doesn't come in person. Written notes only"; the Cassalanter thread, surveillance and Savra's combat support "are not formally withdrawn. They stop being offered" (:52-56). Remedy: pay the declined 25% later, Savra appears once and says "Thank you." (:58-62).
- **Outcomes.** `Tithe Paid: True` and `False`, `Quietly Reassigned: True` (:66-76), read in **Vault of Dragons - The Final Approach**. Next Steps (:82-86): "the Order's Cassalanter dossier remains accessible when the party reaches Renown 10".
- **Holes.** See §6.

### 2c. s02-savras-past (R :1-133)
- **Triggers.** A: "The party holds OotG Renown 3 (Marcheon) and Savra has fought beside them at least once ... She chooses the moment" (:9). B: "A party member shares Mirt's intel with Savra" (Fireball Harper debrief) (:11); fires "regardless of renown", abbreviated below Renown 3 (:125).
- **The Howling Hatred (:21-27).** An "elemental air cult", ranks Initiate, Windwalker, Windcaller, Feather of Yan-C-Bin; a derelict Dock Ward tower; funding "through intermediaries"; collapse "in a single tenday".
- **What she did (:47-63).** Four years with the cult (:33, :49); three years ago a storm-night rite; four junior initiates bound to ring-bolts at forty feet; she "held the outer ritual circle" at the stairwell door; stopped two; two went over, one caught a drainpipe and lived; she walked out and two days later asked the Halls of Justice for a cleric of Tyr (:59). The survivor: "She never asked" (:69).
- **The Cult's Money (:73-85).** Trigger B only: "old Waterdhavian money ... smiling in temple every Godsday".
- **The Ask (:87-97).** "Now you know. What will you do with it?" Evasion is named: "That's not an answer."
- **Outcomes.** `Savra's Past Known`, `Cult Funding Linked` (True/False each, :101-115), read in **Cassalanter Villa** and **Vault of Dragons**; fires once (:121).
- **Holes.** §7.

### 2d. r03-marcheon (R :1-71)
- Fires "at the first natural pause after one party member's OotG Renown reaches 3 - Savra's next visit to Trollskull Manor, or ... the Halls of Justice within a tenday" (:7). "The rest of the party is present" (:7).
- Benefits: (1) Savra accompanies "into one dangerous operation per quest as a combat ally", she may refuse (:27-33); (2) the armory, Halls of Justice east annex, "a cleric named Tobrin holds the key", one mundane weapon or armor per tenday, returned serviceable (:23); (3) the temple network, "one briefing per week" (:37-43). Outcome `Marcheon Reached: True / False`, "read by the **Whitehawk** rank event" (:55-57).

### 2e. r10-whitehawk (R :1-105)
- Savra "sends word within a tenday", meets at the Halls of Justice antechamber (:7).
- Benefits: surveillance on one named target per quest, two-person team, three days (:35); a *potion of healing* and a *potion of greater healing* "before each major operation", one day's notice (:37); an Uncommon item grant "Armor, Ring, or Weapon" (:45-51); the Cassalanter dossier (:17-25, :53-77); Triad spellcasting of 2nd level or lower free (:81-85).
- The dossier: partial ground-floor layout, twelve years of donations, four Watch complaints "between 1479 and 1492 DR", a servant's unfinished account (:17-25). "Savra built this file herself" (:17). The layout gives "Advantage on the character's initial orientation check in **Cassalanter Villa**" (:91).
- Outcome `Whitehawk Reached: True / False` (:89). The dossier file is "in the party's possession" (:97), though the rank is individual.

### 2f. r25-vindicator (R :1-107)
- Written summons "one day in advance" with the Halls of Justice seal (:7, :15-21), main chamber, two knight witnesses (:25).
- Benefits: formal inquiry into a named individual or organization, findings "admissible before the Lords" (:35), "one inquiry at a time" (:37); the Strike Team, "Three Order members (use the **Knight** stat block)", one operation per quest, "will not execute orders they judge clearly unrighteous" (:51-61); a *+1 weapon* (:65-73); the history line "Three of the four people who've held Vindicator in Waterdeep in the last fifteen years are dead" (:81).
- "The Cassalanter dossier received at Whitehawk is sufficient predicate to name Lord Victoro Cassalanter" (:45, :97). Outcome `Vindicator Reached: True / False` (:89).

### 2g. r50-righteous-hand (R :1-170)
- Written summons "three days in advance" (:7, :28); main hall (:36); six senior Order members "including Sister Valdra" and two priests of Tyr (:36); a `[!design]` note "Expected in Dungeon of the Mad Mage" (:16-18).
- Investiture with Savra's sword; "the title carries weight outside Waterdeep" (:44-62); Sister Valdra presses a "finer" gauntlet pin (:60-62).
- Charge (:64-86): six **Knights** and two **Priests** from "the Order's Waterdeep chapter" for one major operation (:68); a Resurrection funded once, recorded by the high priest of Tyr (:70-80, "5th-level spell, 2024 rules", 1,000 gp component); the weapon's origin (:82-86).
- The Mandate (:88-130): the Undermountain Mandate, accept or decline.
- Outcome `Undermountain Mandate Accepted: True / False` (:134-138). There is **no** `Righteous Hand Reached` outcome.
- **Holes.** The summons goes to Trollskull Manor, so cannot reach a member below ground (no hold rule). Savra "has given [Righteous Hand] once before in Waterdeep ... four years ago" (:42) contradicts her biography (§0.2). The "Order's Waterdeep chapter" and "senior council" (:24, :68) have no setting page. Valdra's presence conflicts with NF-V. The weapon's origin conflicts with r25 :67. The Resurrection block has the wrong spell level and no caster. "Unconditional" mobilization has no ally rules. "One mobilization per significant threat, at the character's request" (:148) is a different limit from "one major operation" (:68).

---

## 3. Contradictions and conflicts (R, PREV, guides, setting, sources, other factions)

| # | Conflict | Where | Settled by (recommendation) |
|---|---|---|---|
| C1 | Savra awarded Righteous Hand "four years ago" in Waterdeep; she left the cult three years ago and "the Order took her in afterward". | R r50 :42; R FM :18; R s02 :49-59 | Delete the line. Say the rank was "awarded in Waterdeep once before, before my time" (Savra reports it from the Order's roll). |
| C2 | Cult length: "three years" vs "four years"; the tower's last "two years". | R FM :18 vs R s02 :33, :49; R s02 :25 | One number. Recommend: four years inside, left three years ago (s02 is the scene that tells the story; FM background must match). |
| C3 | "Only Order member in Waterdeep" vs knight rotation, chapter, council, Valdra among "senior members". | R FM :86 vs R r25 :25, :51, R r50 :24, :36, :68 | Define a small Waterdeep chapter in the plan (Savra, a rotation of knights who serve elsewhere in the Sword Coast, a clerk's office at the Halls of Justice). Reword FM :86 to "the only Order knight working the Field Ward". |
| C4 | Tithe Renown for "unprompted or when asked" vs "unprompted only". | R s01 :10, :36-42 vs G05 :46, PG (Renown section), AB (Earning Renown), ORG :17 | Keep the guide: only a tithe made before Savra asks earns the +1. The rewrite needs an explicit clock (§6). |
| C5 | Sister Valdra's status. NF-V: unofficial, "unsanctioned by Savra", "no scripted appearance", Trollskull bouncer candidate; staff guide: "Savra Belabranta does not know she is here", "+1 OotG Renown/tenday, cap +3" for employing her. R makes her the reassigned contact and a witness at the investiture with a gauntlet pin. | NF-V :32-35, :46-47; `trollskull-manor/03-staff-and-hiring.md:77`; ORG :24; R s01 :11, :54, :86; R r50 :9, :36, :60 | Keep Valdra out of all seven events. Use a named clerk of the Order's Waterdeep office and a named senior knight. Log the staff-guide Renown line for the consistency audit. |
| C6 | Dossier age. "Twelve years of observation", complaints 1479-1492 DR, "Savra built this file herself" vs "months" of watching. | R r10 :17-25, :61 vs R FM :20, G05 :9, ORG :17; G05 :56 "years of compiled observation"; `arc-g:41` "for years" | Recommend "the Order's file, opened by a predecessor, carried on by Savra for months". Keep the 1479-1492 span for the complaints only; drop "Savra built this file herself". |
| C7 | Servant's account appears in the dossier (r10 :25) and in Valdra's three pieces (NF-V :52, "a servant's story the Watch dismissed six months ago"); `arc-g:41` has Savra report it too. Same servant? | as listed | Say it is the same servant. Valdra is the source of the account that Savra copied into the file; this stays outside these events (Trollskull staff). Note for the audit. |
| C8 | The pin. AB :431 puts "a silver gauntlet pin at her collar" on Savra. R FM gives a gauntlet "passed hand to hand" (:80) and no pin; r50 :60 has "a gauntlet pin ... finer than the one given at Chevall". | AB :431; R FM :80; R r50 :60 | Chevall token = a plain silver gauntlet pin given at the oath. Rank events add nothing physical until r50 (a finer pin). |
| C9 | The +1 weapon's provenance. "Out of a cache from a diabolist estate, held three years" vs "recovered from a devil's effects ... the devil took it from someone". | R r25 :67; R r50 :84 | Pick one: the cache. Cut r50's reveal or make it explicit that the cache is the same: "the cache was a devil's effects". |
| C10 | The Halls of Justice' location: Temple District (R FM :78), Castle Ward west of the Market (WDH `data/3/entries/4/entries/9/entries/1/entries/0`; AB :410), Sea Ward (`waterdeep-lore.md:36`, which lists Tyr among Sea Ward temples). | as listed | Use WDH. Log `waterdeep-lore.md:36` for the audit. |
| C11 | Eligibility. WDH: "any non-evil character"; R and `ev-04:28`: "paladins, clerics, characters with strong moral conviction"; LA/EE: nobody tested. | WDH `data/1/entries/11/entries/10/entries/0`; R FM :7 | Decision D1. |
| C12 | First mission. WDH: "After the ceremony, Savra gives new recruits their first mission." R: none; Next Steps says M1 "unlocks immediately". | WDH `.../entries/9/entries/1/entries/0`; R FM :98 | Decision D4. |
| C13 | Gate ladder. R overviews: M1 R0/L2, M2 R2/L3, M3 R4/L4, M4 R7/L5, M5 R10/L6, M6 R14/L7. Shared ladder: M1 joining/L2, M2 R3/L3, M3 R5/L4, M4 R8/L5, M5 R10/L6, M6 R13/L7. | `m0N/overview.md` Quest Requirements | Reports 03 and 04 own the fix. Effect here: r03 (Renown 3) precedes M2; r10 (Renown 10) precedes M5; R25 follows M5. |
| C14 | AB states the Cassalanters are "active Asmodeus cultists conducting devil-bargain rituals"; AB's rank text also says "Cassalanter diabolism". | AB :402, :464 | The standing rule wins; AB is a source, not a rule. No OotG event may repeat it. |
| C15 | M2 is delivered by paper bird; ORG :7 says Savra delivers in person, "no paper birds". | `m02/overview.md`, ORG :7 | Report 03 owns M2. The contact object here must say what Savra sends when she cannot come (§4). |
| C16 | Lair-support promises of Savra that no rank event writes: Xanathar's Lair (Renown 10+: three potions of healing, extraction backup), Cassalanter Villa (a Siamorphe holy symbol, Renown 10+: attends the ball, one improvised intervention), Kolat Towers (Renown 10+: a Knight and 25 HP of lay on hands at the extraction point), Vault of Dragons (Renown 10+: City of the Dead main gate). | `arc-f:37`, `arc-g:41`, `arc-i:39`, `arc-j:49` | These are Whitehawk-era Renown-10 favours. Recommend they become a short table in r10 ("Savra at the Lairs"), so the structure docs have a source (§5). |
| C17 | "Per arc" (AB) vs "per quest" (G05, PG, GMO). | AB :476-482 | Quests, not arcs. |
| C18 | The Fireball and Gralhund hooks for Savra apply at **Renown 1+** (member). R FM :72, :100 have Savra approach non-members again after those quests. | `fireball/ev-01:200`; `gralhund-villa/ev-09:115` | Drop the re-approach. The offer stands at the Halls of Justice (§4). |
| C19 | R s02 trigger B needs "a party member shares Mirt's intel". Mirt tells **a Harper member** privately (`fireball/ev-01:194`). A non-Harper OotG member knows it only if told. | R s02 :11 | State that the Harper member must pass the line on; any member present when it is passed on counts. |
| C20 | Appendix B Chevall text says "good faith ... access to healing services at cost"; G05, PG and GMO add free *Cure Wounds* and a bed. | AB :474; G05 :54 | Use G05 (the later text). |

---

## 4. Contact object, who recruits, where, and the members-only frame

### 4a. Facts
- **Recruiter and place.** Savra recruits in person at the characters' residence; the oath is at the Halls of Justice (WDH `data/3/entries/4/entries/9/entries/1/entries/0`; AB :410; R FM :26-31, :76-84). `ev-04:28` and ORG :7 say "in person", "no advance invitation", "no paper birds, no messengers, no flying snakes unless urgent".
- **Delivery in R for every other event.** r03: "Savra's next visit to Trollskull Manor, or ... the Halls of Justice within a tenday" (R r03 :7). r10: "she sends word within a tenday" (R r10 :7). r25: "a written summons one day in advance - formal, in her hand, bearing the Halls of Justice seal" with a text (R r25 :7, :15-21). r50: the same, three days ahead, to Trollskull (R r50 :28-32). M2: "paper bird" (`m02/overview.md`). There is no canonical description, and no reply channel.
- **Savra's voice and look.** NF-S :22: late twenties, dark hair worn back, strong jaw. AB :431: a dark riding coat, good boots, the gauntlet pin. VOICE: stingy, plain, clipped swearing; "I'll tell you plainly"; nod tell; she calls Tyr "the Maimed God". R FM :46 (PREV :64-66) keeps the nod tell.
- **Candidate frame in R.** Party-level. The Summary says "Characters who accept" (:13) and the outcome "at least one party member" (:92). `ev-04:106` writes its own `Order of the Gauntlet Joined: True / False` heading (the LA and EE rows have already been converted: `ev-04` states "The ... First Meeting marks this for each character who accepts, so this Event does not").
- **Members-only.** R r03 :7 says "the rest of the party is present". No rank event says companions gain nothing. OOS names this "R3 M, systemic: Renown awards never say 'members only'".

### 4b. Recommendations
1. **Candidates (D1).** Follow LA/EE: every character who belongs to no other faction is a candidate and answers for themselves; companions listen and gain nothing; if every candidate declines, the Event ends with no membership outcome (LA FM :14-18). Use the R eligibility only to choose whom Savra addresses first: the candidate with the Cleric, Paladin or Acolyte background or class, then a worshipper of Helm, Torm or Tyr, then the highest Wisdom, then alphabetical. Nobody is tested at the door. WDH's "non-evil" is the one outlier: keep it as a line in `What Is Actually True`, not a test: the oath asks three questions (below), and a candidate who answers that they do not mean to oppose evil is not sworn; this decides nothing for a character who answers honestly.
2. **Summons and placement (deterministic).** The morning the Order row fires, Savra knocks at Trollskull Manor at the third bell and waits for an invitation (R FM :26-31, kept). If no candidate is at the manor, she leaves a sealed note with whoever is on site (the carpenter Tally Fellbranch is the named neighbour who works on the doors: `act-i/trollskull-alley/ev-03-the-neighbors.md:20`; flag as a dependency for the audit) and the note says: "Halls of Justice, the antechamber, the third bell past noon, any day for a tenday." This is the one place the party is told to go; it satisfies the Session 44 rule that every contact has an in-fiction summons.
3. **Contact object (canonical, written once in the First Meeting).** Savra's left-slanting hand, on paper with the Halls of Justice seal (R r25 :17, R r50 :28), folded once. When she cannot come, an acolyte of Tyr in a plain grey surcoat (2024 **Priest Acolyte**, CR 1/4, XMM) delivers it to the named member only and waits for no reply. The **drop** is the door-warden at the Halls of Justice, who holds messages "for Savra Belabranta". Formality rises with rank: Chevall and Marcheon spoken or a single line; Whitehawk a numbered time; Vindicator a formal summons the day before (R r25 :7); Righteous Hand a formal summons three days before and delivered above ground only (§8). Savra herself comes in person for the promotion at Marcheon and Whitehawk because ORG :7 says she does.
4. **Answer scene.** After the pitch, Savra asks each candidate the oath's three questions (below) and then "Will you swear it?". Add the accept, decline and ask-for-time readalouds (LA FM :198-220). R :74 has Savra say "Let's finish it at the Halls of Justice" at once; recommend she names the Halls and leaves the oath as a separate scene (`### The Oath`, R :76-84) so a candidate who asks for time can swear any day (D3).
5. **Oath text.** Use AB :450 and WDH, not R :80: three commitments - "to find evil, to pursue it, to destroy it"; "to protect those who cannot protect themselves"; "to stand when standing is required" - spoken while wearing the silver gauntlet. The priest of Tyr seals it with "a brief invocation of Tyr". R :80's "hold one another accountable" moves to the r50 investiture (R r50 :52), which is where it was meant to answer the first oath.
6. **Open door, not Offer Closed (D3).** The Order wants recruits (WDH: "The surge of violence ... spurs members of the order to find adventurers"). Record a late acceptance under the same outcome with the name. A character dismissed by nobody can always return. Do not add an `Offer Closed` outcome. Drop R :72 and :100 (the second approach).
7. **First mission (D4).** WDH hands the first mission at the ceremony. R's M1 needs L2 and R0 (R) or the joining rank (ladder). Recommend: after the oath Savra says the closing line, and M1 is briefed to the member in person at the manor the next morning (a one-line Next Steps handoff), not in this Event. This copies LA FM :263-271 ("The Long Watch reaches each new member at this table").
8. **`What Is Actually True` (zero-prep).** (a) Savra chose these candidates from what Renaer and the Floon rescue told her, and the Order has no one else to send. (b) The family she will not name is the Cassalanters; she suspects, she cannot prove, and she does not say diabolism (R FM :20, G05 :9). (c) The Howling Hatred is real and she is ashamed; what she did is hers (R FM :18). (d) The Order is small in Waterdeep: Savra, a clerk's office, and the priests of the Triad who speak to her without being Order members. (e) She names the Splinter's brawl only as "someone is paying for it" until M1 tells her more (§10). (f) Savra does not know what the Cassalanters worship before the party tells her (G05 :9; the standing rule).
9. **Renovation help (party-level, once; D5).** The two promises differ (`ev-04:58` "Net 100 gp savings"; `02-operating-costs.md:83` no money, guild meetings and a Watch watch-list). Recommend the manor guide's version, because it is non-monetary and the FG and EE precedent delivers the party-level help in the First Meeting (EE FM :269-276; LA FM :254-261): Savra walks the party to one Guild hall, in Order insignia, and the permit queue closes in a day. Fix numbers: the renovation total drops by 100 gp once (matching `ev-04`); the Watch watch-list is a passive line (a Watch patrol answers a disturbance at the manor within the hour; no event). `ev-04` and the manor guide must be reconciled in report 05.
10. **Chevall Benefits box (per member; companions get nothing).** WDH and G05 give four things: (a) Savra vouches to any temple of Tyr, Helm or Torm in Waterdeep (healing at cost); (b) free healing, one *Cure Wounds* (a 1st-level spell, one action, touch: XPHB) per day per temple, and a bed; (c) in trouble with the law, a member "puts in a good word" and tends to the character's affairs while incarcerated (WDH `data/1/entries/11/entries/10/entries/4/items/1`); (d) the faction channel for *Speak with Dead* at Renown 1+ (`act-ii/fireball/ev-01:88`). Write each as a procedure: the temple, the front-desk contact (the door-warden), the limit (once per day per temple, the temple list fixed at the Halls of Justice, the Temple of Helm in the Castle Ward as named in R s01 :28, and a Torm temple whose name is an invented fix and must be flagged), and the loss rule (lose Renown: the rank stays, the benefits wait). The *Speak with Dead* channel is a Fireball! requirement, so it must be in the box.

### 4c. Scene list for 00-first-meeting
`# Order of the Gauntlet First Meeting`. Summary (abilities; Candidates and Companions; What Is Actually True). `### The Knock` (placement, the note, the contact object). `### The Pitch` (Savra social block; qna: why us, what does the Order do, what does it cost, the family, the beholder, can we keep other loyalties; a GM block for Stone / vault / Manshoon). `### The Darker Exchange` (R :54-64, with the "ask sincerely" rule restated and the cult length from C2). `### Each Candidate's Answer` (Recording; accept / decline / ask for time; the Chevall box). `### The Oath` (Halls of Justice, the priest of Tyr, the silver gauntlet). `### The Guild Hall` (party-level help, once). `### Leaving` (closing line; handoff to M1). Concluding: `Order of the Gauntlet Joined` per name; Next Steps; Overview; Summary with "After the Meeting" and "Without a Private Meeting".

---

## 5. What each rank grants: R, PREV, guide, Appendix B, WDH

### 5a. Side-by-side

| Rank | R / PREV event | G05 (:54-58) | AB (:472-486) | WDH |
|---|---|---|---|---|
| R1 Chevall | none delivered | Savra vouches; healing services at cost; free *Cure Wounds* once per day per temple; a bed | "good faith ... healing services at cost" | priests facilitate healing; "a good word" and affairs tended while jailed (`data/1/entries/11/entries/10/entries/4`) |
| R3 Marcheon | Savra as combat ally, once per quest; armory one mundane item per tenday; temple briefings | same | one dangerous mission "per arc"; armory | none |
| R10 Whitehawk | surveillance on one target per quest; two potions before major operations; an "Uncommon" item; dossier; free Triad spells up to 2nd level | same | surveillance and potions only | none |
| R25 Vindicator | formal inquiry; Strike Team of three Knights; +1 weapon | same | inquiry and +1 weapon only | none |
| R50 Righteous Hand | six Knights, two Priests; Resurrection once; knighthood; Undermountain Mandate | six Knights and two Priests; investiture and knighthood; one Resurrection | six knights and two priests; "agents of the Order, granting quasi-official legal standing" | none |

### 5b. Rules checked against XMM, XPHB and XDMG
- **Knight** CR 3, AC 18, HP 52 (XMM). Used for Savra, the Strike Team and the six-Knight mobilization. **Priest** CR 2, AC 13, HP 38, Wisdom spellcasting. **Priest Acolyte** CR 1/4, HP 11 (the messenger). **Guard** CR 1/8, **Scout** CR 1/2, **Spy** CR 1, **Commoner** CR 0. The 2024 names are *Knight*, *Priest*, *Priest Acolyte*; none of the R names is retired.
- **Resurrection** is **level 7**, 1 hour, touch, diamond worth 1,000+ gp consumed (XPHB). *Raise Dead* is level 5 with a 500+ gp diamond. R r50 :80 says "5th-level spell": wrong. No XMM stat block can cast a 7th-level spell: the Priest's list tops out far lower. The caster is a 13th-level (or higher) cleric of Tyr, who needs no stat block (non-combatant), and the Order supplies the diamond.
- **Potions.** *Potion of Healing* is common; *Potion of Greater Healing* is uncommon (XDMG). Fine as written.
- **Items.** *Ring of Protection* and *Bracers of Defense* are **Rare** (XDMG), not Uncommon. *Sentinel Shield*, *Cloak of Protection*, *Brooch of Shielding*, *Periapt of Wound Closure*, *Amulet of Proof against Detection and Location* are uncommon (XDMG). The generic +1 weapon and +1 armor entries were not found in the downloaded `items.json` under those names; their rarity (+1 weapon uncommon; +1 armor rare) is from the 2024 DMG in my memory and unverified.
- **Spells for Whitehawk's free temple casting (level 2 or lower, XPHB):** Cure Wounds (1), Healing Word (1), Detect Evil and Good (1), Bless (1; a holy symbol worth 5+ gp as a component), Aid (2), Lesser Restoration (2), Prayer of Healing (2), Calm Emotions (2), Zone of Truth (2), Augury (2, ritual, 25+ gp tokens), Locate Object (2), Gentle Repose (2, ritual). Nothing in the seven files names a spell; no *wish*. 2024 *Speak with Dead* is level 3 and does not qualify.
- **Mad Mage limits** (WDMM alterations; quoted in FG r50 :370-380 and LA r50 :388): teleportation, *plane shift*, *astral projection* and *word of recall* fail; *Sending* works except aimed at Halaster. Relevant to who reaches a member below ground (§8).

### 5c. Procedures the rank events must write (zero-prep, from the model)

**Marcheon (r03).**
- *Trigger and place.* "When an individual Order of the Gauntlet member first reaches Renown 3" (DR r03 :5; EE r03 :13-15). At noon the next day an acolyte brings Savra's note to the member's lodging; the meeting is at the Halls of Justice, east annex, at the third bell past noon. Away from Waterdeep: first surface lodging, a day later.
- *Savra as a combat ally.* The member asks Savra for one operation per quest, naming the place and the day; she answers in a day. She refuses an operation she believes will get the party killed (R r03 :27-33, kept). She is a **Knight** (XMM), withdraws at 20 HP, takes orders from the member, and will not kill a surrendered creature. **CR 2.0:** Knight Power is 37 (Tier 1), 30 (Tier 2), 25 (Tier 3). At levels 2 and 3 a Knight (37) is twice or more a PC's Power (14 -> 28, 18 -> 36), so the **High-Power Warning** trips and Savra is a safety net there: do not add her to Party Power. From level 4 she counts in full. Party Power with Savra: L4 69 / 92 / 115 -> 106 / 129 / 152 (3 / 4 / 5 PCs); L5 96 / 128 / 160 -> 126 / 158 / 190; L6 105 / 140 / 175 -> 135 / 170 / 205; L7 123 / 164 / 205 -> 153 / 194 / 235. An effective figure at withdrawal is about 0.71 of listed Power.
- *Armory.* The east annex of the Halls of Justice; a lay brother holds the key (rename R's "Tobrin": **Tobrin Ashvale** is the Xanathar bartender at Trollskull, `notable-figures/xanathars-guild/13-tobrin-ashvale.md:1`; collision). One mundane weapon or armor from the 2024 equipment list, one per tenday per member, returned serviceable; heavy armor needs three days' notice to fit; a ruined item is replaced at its listed price; the loan ends if the member lends it to a non-member (companions cannot borrow).
- *Temple briefings.* One briefing per **tenday** (R says "week"; correct it) per member, from one of three temples the member names: Halls of Justice, the Temple of Helm in the Castle Ward, a Torm temple (invented). The priest tells patterns, not names (R r03 :41). Fix what a briefing may contain: unusual activity, "fiendish signs" in general, nothing that names the Cassalanters or a pact (§10).
- *Renown loss.* The rank stays; accompaniment, armory and briefings wait until the Renown is restored.

**Whitehawk (r10).**
- *Surveillance.* One named suspect or location per quest per member, two **Scouts** for three days, a written report at the end (R r10 :35). The member names the target; Savra approves. Fixed limits: no named Cassalanter family member before **Cassalanter Villa** has run, because the team would find an Asmodean temple (§10); surveillance of the villa's public ground floor is allowed and returns "visitors, deliveries, a carriage after dark".
- *Potions.* One *Potion of Healing* and one *Potion of Greater Healing* from the Halls of Justice infirmary before each quest's main operation, one day's notice; not before every combat.
- *The item.* A fixed table of Uncommon items (Sentinel Shield, Cloak of Protection, Brooch of Shielding, Periapt of Wound Closure; weapons per R :51 only if the generic +1 entry is confirmed uncommon). Remove Ring of Protection and Bracers of Defense (Rare). The member picks one from the table at the meeting; no "GM chooses" (R :51).
- *The dossier.* R :17-25 content, with C6 fixed. Make the dossier a party document delivered to the member; companions may read it. The "Advantage on orientation check" (R :91) becomes a stated Villa benefit: Cassalanter Villa's Scene 1 allows one Intelligence (Investigation) check with Advantage to place the ground-floor rooms. The upper floors and basement are not on any record (R :63-65), which is the true gap.
- *Temple casting.* The 2nd-level list in 5b. Fixed exclusions: no spell cast against a living named person; **Detect Evil and Good** is cast only at a place the member names that is not the Cassalanter Villa, or cast on the member's behalf only after M4/M5 have made devils known (the secrecy rule, §10). Cost: the temple covers material components under 100 gp.
- *Savra at the lairs.* Convert `arc-f:37`, `arc-g:41`, `arc-i:39`, `arc-j:49` Renown-10 support into a short table of what Savra does at each lair (the potions, the extraction backup, one improvised intervention at the ball, a Siamorphe holy symbol if the party has evidence from Faction Outposts), so the unconverted structure docs have a source (C16).
- *Renown loss.* The item and the dossier stay; the surveillance, potions and temple casting wait.

**Vindicator (r25).**
- *Summons.* Savra's formal note the day before (R r25 :7, :15-21). Two witnesses; give them names (invented) so the Strike Team has a face.
- *Formal inquiry.* One at a time per member; the target needs predicate: the **M5 ledger** (not the dossier, C-fix OOS r25 R2 T), a recovered cult document, or a sworn witness; written report in two tendays (R r25 :45). The inquiry's findings are admissible to the Lords but the Lords act at their own pace; Savra files "diabolism" only after the party has found devil evidence (§10).
- *The Strike Team.* Three **Knights** named at the meeting (invented names, none from other factions), one operation per quest, three days' notice, surface Waterdeep or the Portal if the mission begins below, "will not follow an order they consider clearly unrighteous" (R :55) restated as a loss rule (they refuse to attack the Watch, a Lord, or a surrendered creature). **CR 2.0:** Knight Tier 2 Power 30. Fighting allies are one fewer than the PCs, to a maximum of three (the team's size): L6 (35/PC) 105 / 140 / 175 -> 165 / 230 / 265; L7 123 / 164 / 205 -> 183 / 254 / 295; L8 132 / 176 / 220 -> 192 / 266 / 310 (3 / 4 / 5 PCs; allies counted 2 / 3 / 3). A Knight (30) is below twice any level-5 or higher PC (32), so no warning. The mobilization more than doubles a party of three below level 6: either rebuild the fight on the allied total or treat the team as a safety net, and say which per scene.
- *The weapon.* A fixed table of +1 weapons by category (sword, axe, hammer, bow) from the seized cache; the member picks. Provenance per C9.
- *Renown loss.* The rank, the weapon and the filed inquiry stay; new inquiries and the Strike Team wait.

**Righteous Hand (r50).** See §8.

### 5d. Scene lists
**r03 / r10 / r25.** `# Marcheon` etc. Summary (trigger, benefits, companions). `### The Note at Noon` (the contact object and the away-from-Waterdeep rule). `What Is Actually True`. `### Naming the Rank` (Savra social block, qna: what does the rank give me, why is it mine and not the party's). One `[!exploration]` box per benefit. `### Renown Opportunities` ("The rank event awards no Renown"). `### Aftermath`. Concluding with the outcome per name and the "reads" paragraph. Overview. Summary.

---

## 6. s01 The Tithe: standalone event, and suspension or dismissal

### 6a. Facts
- Sources of the tithe: `3. Player Character Factions.pdf` p.25 ("The Order of the Gauntlet will expect the PCs to tithe at least 25% of the horde": the horde is the vault gold); AB :464 and G05 :46 ("Tithe at least 25% of a major recovered hoard ... +1 ... without prompting"); ORG :17, :28; PG and GMO ("unprompted"). R's 1,000 gp threshold and "first haul" trigger are inventions (R s01 :7).
- Known early hauls after joining: the Gralhund coach house trade bars, "2,000 gp total" (`locations/gralhund-villa/g03-coach-house.md:13`). The Zhentarim warehouse secret room, 1,050 gp (`locations/zhentarim-warehouse/z03-secret-room.md:17`), comes before any First Meeting. Lair treasure totals are in unconverted structure docs.
- Only the Lords' Alliance suspends or dismisses: WDH `data/3/entries/4/entries/1` ("A character who belongs to a faction other than the Lords' Alliance can turn down a mission without consequence"); PG Renown section; G01 :11. Serious offenses cost 2 Renown for every faction (PG).

### 6b. Holes in R
1. Renown for a prompted tithe (C4).
2. Party-level frame: "the party pays", `Quietly Reassigned` hits the whole party (OOS R3 M), though loot is shared and some players are not Order members.
3. "Within two days of the windfall becoming known" is a judgment; "unprompted" has no clock.
4. Reassignment via **Sister Valdra** (C5). "Not formally withdrawn. They stop being offered" (R :56) is the same thing as withdrawn; the list is not written.
5. Reassignment collides with M4 and M6, where Savra fights beside the party (`m04/overview.md`, `m06/overview.md`), and with M5's Cassalanter ledger, which is the "Cassalanter thread" R says stops being offered.
6. The Vault of Dragons "Final Approach" does not read these: `arc-j:49` has no tithe reference (grep returns none). The Next Steps claim that the dossier stays "accessible at Renown 10" (R :84) is not read by r10.
7. The worthy-cause list, the Griffon Cavalry fund (Savra "does not name this one", R :31) and the Trollskull fund are good; the Trollskull option lets the party tithe to itself. Rule it out.
8. 2024 rule check: none needed; no stat blocks or spells in the file.

### 6c. Recommendations
1. **Trigger (deterministic).** Fires per Order member when the party carries a haul of **1,000 gp or more** (coin, trade goods, gems at face value; magic items excluded) out of one operation for the first time after that member took the oath. Name the known first cases (Gralhund coach house, 2,000 gp). For a member who joins after a haul, the first haul after joining counts.
2. **The ask is made of each member's own share.** The haul is divided evenly among the party; the member owes 25% of their own equal share. Example: 2,000 gp, five PCs: 400 gp each, 100 gp tithe per member. Non-members owe nothing and are never pressed. This removes the party-wide lockout (OOS R3 M) and fits the corrected members-only frame.
3. **The clock.** Savra knocks at dusk on the second day after the haul reaches Waterdeep. A member who shows her a receipt, names a recipient and pays **before that knock** has tithed unprompted and earns **+1 Renown** once. A member who pays after she asks has "earned only the reminder" (ORG :17): no Renown, Savra says "Good." and nothing else. A member who refuses or pays under 25% is *Quietly Reassigned*. Renown is awarded once per member in the campaign ("once in the campaign", FG s01 :261-263); a late sitting for a member who was absent follows FG s01 :265-271.
4. **Worthy causes.** Keep R :24-32 minus Trollskull Alley Rebuilding. Add that the Order's clerk, not Savra, takes the receipt, to keep her out of the transaction.
5. **No suspension or dismissal for the Order (D6).** The rule is LA's alone (WDH; PG). The Order's analogue is *Quietly Reassigned*, written as a list, not a punishment:
   - Savra stops volunteering the *optional* extras to that member: the Marcheon accompaniment (unless the member asks; she then answers in writing in a tenday), the temple briefings' "extra" requests, the r10 surveillance offer, and her Vault testimony.
   - **Missions still arrive** from Savra, by a clerk's note instead of in person, because M4 to M6 are about devils loose in the Field Ward and she will not hold them back to make a point. In M4 and M6, where Savra fights beside the party, she does so coldly and says only "This isn't about you." (Report 04 must check this against its encounters.)
   - The contact for the extras is the Order's Waterdeep clerk (invented name, no Valdra).
   - **Remedy:** the member pays the declined 25% to a worthy cause; Savra appears once and says "Thank you." (R :62). Reassignment ends the next morning.
   - Reassignment costs no Renown.
6. **Outcomes (per member name).** `Tithe Paid` (paid unprompted; marks the +1), `Tithe Paid After Asking` (paid late; no Renown; replaces the "False" shortfall wording), `Quietly Reassigned` (refused or underpaid). Clear `Quietly Reassigned` on remedy. Readers: the Vault of Dragons Final Approach (unconverted; for the plan, record that `arc-j:49` must be updated), r03/r10 (the extras), and s01 itself. Drop the Next Steps sentence about the dossier (R :84) and write it in r10.
7. **Scene list.** Summary (members-only; what happens per member); `What Is Actually True`; `### The Receipt` (the clock); `### The Ask` (R :14-22); `### Worthy Causes`; `### Paying Before She Asks`; `### Paying After`; `### Refusing`; `### Reassigned` (the list in 5); `### Remedy`; Renown Opportunities (+1 once; late sitting adds a name); Aftermath; Concluding; Overview; Summary.

---

## 7. s02 Savra's Past

### 7a. Holes in R
1. **Trigger A** reads "The party holds OotG Renown 3" (OOS R3 M) and "Savra has fought beside them at least once" (R :9). A member can reach Renown 3 with no Savra accompaniment on record. State both as per-member.
2. **Trigger B** depends on a Harper (C19). Mirt's intel: "Cassalanter money was behind the Howling Hatred cult three years ago, because the Watch released two of its members after a quiet word from someone at Cassalanter Villa" (`fireball/ev-01:194`). That is a suspicion with a named family, delivered by a Harper to Harpers. When an OotG member says it to Savra, the Event passes the Cassalanter name to a faction that is otherwise not told it (R :37, :79-85 show Savra refusing to name them). Legitimate as suspicion; flag it for the audit.
3. **The timeline** (C1, C2): the number of years, and "Close to taking the Windcaller's oath". The cult's ranks are invented (WDH only points to *Princes of the Apocalypse*, `data/3/entries/4/entries/9/entries/1/entries/1`; no PotA file is in the sources, so the Windwalker/Windcaller/Feather ranks are unverified).
4. **Outcome readers are not wired.** `Savra's Past Known` and `Cult Funding Linked` are "read in Cassalanter Villa and Vault of Dragons" (R :103, :111). `arc-g:370-390` and `arc-j:49, :258` do not read them. Record for the unconverted quests.
5. **The Ask has no table.** "She will know the difference" (R :93) is a judgment. Provide the answers she accepts (hold it, it changes nothing, I don't know) and the one she rejects (evasion) as a fixed list, with her reply to each.
6. **Members-only.** Savra tells the members present, and companions are told to listen (it is a private confession). Each member present marks the outcome by name.
7. **No Renown.** R awards none, and G05 :43-48 has no entry for it. Keep none.

### 7b. Recommendations
- **Trigger A, concrete:** fires for a member at Renown 3 or higher who has seen Savra fight alongside them at least once (M4, or a Marcheon operation). Savra says it at the Halls of Justice east annex after dark, not "wherever she is". She sends no note; she comes to the manor at dusk and asks the member to walk with her (so there is a place and a time).
- **Trigger B, concrete:** fires at once, in the scene, the first time a member tells Savra that Cassalanter money lay behind the Howling Hatred. Run the abbreviated scene if the member is below Renown 3 (R :125), and the full scene the next time Savra meets that member after Renown 3.
- **What Is Actually True:** Savra has never traced the funding; she suspects an old family but names none; she never learned if the survivor lived (R :69). The deed is hers to tell; she tells it flat.
- **The Ask:** a table of answers and replies (R :97), plus the "nod" rule (single nod, given only to the honest ones).
- **Outcomes:** `Savra's Past Known` per member; `Cult Funding Linked` per member (only Trigger B). Readers named: `Cassalanter Villa`, `Vault of Dragons` (unconverted; the audit must record the lines to add), and r50 (the investiture speech can echo it).
- **Scene list:** Summary (members-only; triggers); `What Is Actually True`; `### Savra Chooses the Hour`; `### The Howling Hatred` (lore, not read aloud); `### What She Did`; `### The Cult's Money` (Trigger B); `### The Ask`; Renown Opportunities (none); Aftermath; Concluding; Overview; Summary.

---

## 8. r50 Righteous Hand and the Mad Mage set-up

### 8a. Rules and hold
- **Hold rule (copy LA r50 :19, FG r50 :14-28):** hold until `Vindicator Reached` is marked for the member and the member is on the surface. A written summons cannot reach a member in Undermountain (teleportation and *word of recall* fail below, §5b). The acolyte finds the member at their first surface lodging at noon on the first day above ground, and the investiture is on the third day after (R r50 :7 says "three days in advance"). Several members who surface together attend together.
- **Chapter and council.** Define in the plan: the Waterdeep chapter keeps at least six Knights and two Priests available for a mobilization; the senior council is in another city (invented), and Savra reports to it by courier. Remove Valdra (C5). The high priest of Tyr is the same cleric who casts the Resurrection (non-combatant, 13th level or higher; invented name).
- **Resurrection.** A 7th-level spell with a diamond worth 1,000+ gp (XPHB). The pledge funds the diamond and the casting once, for the member or one ally named in writing before the need arises (R r50 :80). Body must reach the Halls of Justice alive-to-be: carried up by stairs, not teleported. Loss rule: if the member's Renown falls below 50 the pledge stays recorded and the Order refuses to fund it until the Renown is restored.
- **Mobilization (CR 2.0).** Six **Knights** and two **Priests**, one operation per quest, three days' notice (R says "one major operation" at :68 and "one mobilization per significant threat" at :148; pick the former). Fighting allies are one fewer than the PCs, Knights first; Priests do not fight and hold the rear. Knight Power 30 (Tier 2), 25 (Tier 3); Priest Power 23 and 19 (not counted):
  - Level 9 (49 per PC): Party Power 147 / 196 / 245 -> 207 / 286 / 365 (3 / 4 / 5 PCs; allies 2 / 3 / 4 Knights = 60 / 90 / 120).
  - Level 10 (53): 159 / 212 / 265 -> 219 / 302 / 385.
  - Level 11 (62; Tier 3, Knight 25): 186 / 248 / 310 -> 236 / 323 / 410 (allies 50 / 75 / 100).
  - No High-Power Warning: a Knight (30) is below twice a level-9 PC (98). A party of three fighting beside two Knights gains about 40% Power; rebuild the fight or treat it as a safety net, and say which.
- **Knighthood.** "Allied temples and civic authorities across the Sword Coast will recognize it" (R :58, kept). Define the effect: a written credential the member can show; Friendly attitude from clergy of the Triad and a Watch captain's hearing; nothing legal in Waterdeep that Vindicator's inquiry does not already give.
- **The Mandate** (R :88-130). Per member. Accepting is an outcome `Undermountain Mandate Accepted`, kept (no collision now: EE writes `Illuun Watch Accepted`, LA writes `Undermountain Commission Accepted`). Define its effect in one box: one aid call per Undermountain level the member enters, answered by the next Order courier up and down the stairs (no *Sending* from the Order), up to the mobilization already owed. R :148's "one mobilization per significant threat" becomes "one task per level".
- **Branch on the Vault.** R :142-144 branches on Vault of Dragons resolving. Cut; the other r50s do not read the Vault. Replace with the two Mad Mage seeds below.

### 8b. Mad Mage Seeds (one-line facts, from WDMM; add no others)
- Level 15, Obstacle Course: the ghost of **Fidelio**, a paladin of Tyr, haunts the level; a follower of Tyr can persuade him to move on with a DC 20 Charisma (Persuasion) check, and a non-follower can pose as one (DC 10 Deception). (`data/15/entries/3/entries/9`.)
- Level 21, Terminus Level: **Fazrian**, once a planetar of Torm, is corrupted; a character judged innocent can call it to judge itself (DC 26), and its death by its own hand earns Torm's *blessing of protection*. The slain cleric **Brythia Mulspeer** wears Torm's white gauntlet. (`data/21/entries/4/entries/2`, `data/21/entries/5/entries/8/entries/1`, `data/21/entries/5/entries/24/entries/2`.)
- Level 22, Shadowdusk Hold: **Dezmyr** and **Zalthar Shadowdusk** are former paladins of Torm turned death knights; a Torm shrine with a white gauntlet fresco stands there. (`data/22/entries/2/entries/1/entries/2`, `data/22/entries/5/entries/8`.)
- Level 23, vaults: a deva named **Aryx**, sent by Tyr to reach Fazrian, is trapped in a shield (`data/23/entries/3/entries/10/entries/2`); a fiend-bound shield hangs in a neighbouring vault.
- The WDMM has no Order of the Gauntlet. Savra's symbol, the white gauntlet, is Torm's.
- The transport and *Sending* limits are recorded in the Force Grey r50 and are not repeated.

### 8c. Scene list
Summary; `### The Note at Noon`; `What Is Actually True`; `### The Hall` (R :34-42); `### The Investiture` (R :44-62); `### The Charge` (Knighthood; Mobilization; Resurrection; the weapon's provenance fixed by C9); `### The Mandate` (accept / decline); Renown Opportunities (none); `### Mad Mage Seeds`; Aftermath; Concluding; Overview; Summary.

---

## 9. Outcomes: what each event reads and writes

| Outcome (R) | Writer | Readers (R states) | Recommendation |
|---|---|---|---|
| `Order of the Gauntlet Joined: True / False` (party) | FM :90; also `ev-04:106` | all missions (R :92); s02 | Keep the name. Per candidate name. Delete `ev-04:106`'s heading as LA and EE already did. Late acceptance recorded the same way. Readers: G05 and every OotG event. |
| `Tithe Paid`, `Quietly Reassigned` (True/False) | s01 :66-76 | Vault Final Approach (no such reader exists) | Per member. Rename as §6c-6: `Tithe Paid`, `Tithe Paid After Asking`, `Quietly Reassigned`. |
| `Savra's Past Known`, `Cult Funding Linked` (True/False) | s02 :101-115 | Cassalanter Villa, Vault | Per member. Keep names. |
| `Marcheon Reached` | r03 :55 | r10 | Per name. Track last armory date, last temple briefing date, Savra-accompanied operations per quest. |
| `Whitehawk Reached` | r10 :89 | r25 | Per name. Track surveillance used per quest, potions used per quest, item chosen. |
| `Vindicator Reached` | r25 :89 | r50 | Per name. Track inquiry open, Strike Team used per quest. |
| `Righteous Hand Reached` | **missing** | Mad Mage | Add. Per name. |
| `Undermountain Mandate Accepted: True / False` | r50 :134 | Mad Mage | Per member. Keep the name. |

All Events should also read `Manshoon Named` and `Jarlaxle Unmasked` (wording gates only), and s01's `Quietly Reassigned` (r03 and r10 extras). One writer per outcome and a named reader, per the Session 44 rule.

---

## 10. Secrecy gates and standing-rule hits

| Rule | Hit | Where | Fix |
|---|---|---|---|
| Two Zhentarims | "a Zhentarim-funded brawl" | R FM :86 | "a brawl someone is paying for"; the Splinter is named in M1 as "the other cell" until `Manshoon Named`. |
| Manshoon gate | None in speech in the seven files; M1's "Manshoon file" is in report 03's scope (OOS m01 R1 V). `arc-e:87`, `arc-i`, `G05 :7` mention Manshoon in GM text. | | Keep all seven free of the name. |
| Cassalanter secrecy | Savra's FM speech names no family, no pact, no devils (R :40, :48). Clean. | R FM | Keep. Add GM line: a Persuasion success gives only "their charity doesn't trace to any principle" (R :48). |
| Cassalanter secrecy | The temple briefings ("known fiendish signs"), r10's temple divination and *Detect Evil and Good*, and r10 surveillance could reveal the villa's devils before the party discovers them | R r03 :39; R r10 :81-85, :35 | Fixed exclusions in §5c. Briefings may name general fiendish signs only after M4 (spined devils). |
| Cassalanter secrecy | The Vindicator inquiry for "diabolism" and "Lord Victoro" | R r25 :35, :45 | Legitimate once M4/M5 evidence exists; the predicate is the ledger. Before then Savra files nothing. |
| Cassalanter secrecy | s02 "old Waterdhavian ... smiling in temple every Godsday" | R s02 :79-85 | Suspicion only; she names no family. Keep. |
| Cassalanter secrecy | AB :402, :464 state the family are Asmodeus cultists | AB | Source text; the rule wins. Do not echo. |
| Members-only briefs | Rank events "rest of the party is present" (R r03 :7); tithe is party-wide (R s01) | | Per-member throughout (§4, §6). |
| Renown calibration | s01's award is unspecified; s02 awards none | | +1 once, unprompted only; s02 none. No event awards base mission Renown. |
| "The renown ladder wins" | Rank events grant no Renown and no mission grants rank. | | State "awards no Renown" in each rank event. |
| Milestone Points | None awarded. | | Every `Next Steps` ends "This Event awards no Milestone Points". |
| Retired formats | `> **[GM]**`, `[!profile]`, `[!info]`, `[!design]`, `[!lore]`, `#### X: True / False`, `## Read Aloud` | all seven R files | Rewrite into gamemaster/readaloud/social/qna/exploration blocks. |
| *Wish* / devourer | No *wish*. The intellect devourer is named in FM :38 as a Guild tool. | R FM :38 | If a devourer appears in a scene it is the Occupying Devourer (Harper reference §5). FM only mentions them. |
| 2024 rules | Resurrection level; Ring of Protection and Bracers of Defense rarity; "week" | §5b | Fixed. |
| Quests, not arcs | AB "per arc"; R `m05/overview.md` "Arc G" | AB :476-482 | "per quest". |
| Bregan D'aerthe rejects Lolth | Not engaged. | | n/a |
| Jarlaxle hidden identity | Not engaged. "the carnival fleet" is the only wording if it comes up | | n/a |
| Zero-prep | "The GM selects" the item (R r10 :51); "the designation" of the weapon type (R r25 :73); the Strike Team "gives their names" with no names | | Fixed tables; invented names listed in §12. |
| Savra's nod and swearing | VOICE: stingy, plain, clipped; "Maimed God" | | Keep. Savra uses at most one oath, aimed at wrongdoing. |

---

## 11. Decisions needed (option, recommendation)

- **D1. Who is a candidate.** (a) Every unaffiliated character, nobody tested (LA/EE). (b) Non-evil only (WDH). (c) Class and background only (R). Recommend (a), with WDH's line as `What Is Actually True` and the oath questions as the filter.
- **D2. Where the oath happens.** (a) At the Halls of Justice, a separate scene; open door. (b) In the same visit (R). Recommend (a).
- **D3. Refused offers.** (a) Open door, late acceptance recorded the same way (Order wants recruits). (b) Final refusal (LA). Recommend (a); drop R's second approach.
- **D4. First mission.** (a) Savra briefs M1 at the manor the next morning. (b) She briefs it at the ceremony (WDH). Recommend (a) so the First Meeting hands out no assignment, as in LA/EE.
- **D5. Renovation help.** (a) 100 gp saving via a guild hall visit (`ev-04`). (b) No money, a passive Watch line (manor guide). Recommend (a) with the passive line also kept.
- **D6. Suspension and dismissal.** (a) None; Quietly Reassigned as a list (§6c-5). (b) Copy LA s01. Recommend (a): WDH and PG say only the LA suspends.
- **D7. Tithe frame.** (a) Party-level (R). (b) 25% of each member's own share (recommended). Recommend (b).
- **D8. Valdra.** (a) Out of all seven events (recommended). (b) Rewrite NF-V and the staff guide so she is an official Order cleric. Recommend (a).
- **D9. Mad Mage hook.** (a) The Undermountain Mandate as an Order commitment plus WDMM seeds (recommended). (b) Add an invented Order team below. Recommend (a).
- **D10. Waterdeep chapter.** Define it (Savra, a rotation of Knights, a clerk's office, the Triad clergy) rather than leaving "the only member" and "the chapter" in conflict. Recommend defining it in the plan.

---

## 12. Invented names and open items for the plan

- **Invented in R and kept:** Tobrin (rename; collision with the Xanathar bartender), "Order's Waterdeep office", the Howling Hatred ranks and the tower rite (unverified against PotA), the worthy-cause list, the dossier contents, the "Temple District".
- **To invent in the rewrite (flag all as invented):** the door-warden at the Halls of Justice; the Order's clerk; the acolyte messenger; the two Vindicator witnesses and three Strike Team Knights; the high priest of Tyr and the senior council's seat; the Torm temple's name; the lay brother who keeps the armory.
- **Dependencies on files outside this scope (report 05 / other reports):** `ev-04-the-factions-come-calling.md:28, :58, :106` (eligibility, renovation row, True/False heading); `02-operating-costs.md:83`; `03-staff-and-hiring.md:77` (Valdra, "+1 OotG Renown/tenday"); `waterdeep-lore.md:36` (Tyr's temple ward); `arc-f:37`, `arc-g:41`, `arc-i:39`, `arc-j:49, :258` (Savra's support); `arc-j` has no tithe reader; `m01`-`m06` overview gates (C13) and `m02/overview.md` (paper bird); `G05 :7` (Manshoon), `G05 :56` ("years" of observation); `PG`/`GMO` Chevall row (add the Fireball *Speak with Dead* channel and the good word at trial).
- **Verification still open:** generic +1 weapon and +1 armor rarity (not found in `items.json`); the Howling Hatred's ranks against *Princes of the Apocalypse* (no source file); Tally Fellbranch as the on-site receiver of Savra's note.
