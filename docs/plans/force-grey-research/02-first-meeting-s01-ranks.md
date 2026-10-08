# Force Grey research: 00-first-meeting, s01, r03, r10, r25, r50

Scope: `00-first-meeting`, `s01-the-full-picture`, `r03-junior-griffon`, `r10-senior-griffon`, `r25-force-grey`, `r50-force-grey-commander`. No campaign file edited.

**Abbreviations**
- `R` = `/home/user/waterdeep/campaign/quests/faction-events/force-grey/` (restored input). Every R file has only `ev-01-*.md`; none has a design-notes file.
- `PREV` = `/tmp/claude-0/-home-user-waterdeep/a2f34fba-baef-54d3-97ed-3a637e207a74/scratchpad/fg-prev/campaign/quests/faction-events/force-grey/`
- `DR`, `BD`, `H` = `/home/user/waterdeep/campaign/quests/faction-events/{doom-raiders,bregan-daerthe,harpers}/`
- `HR2` = `docs/plans/harpers-research/02-first-meeting-s01-ranks.md`; `HB` = `docs/plans/harpers-conversion-brief.md`; `HM` = `docs/plans/harpers-mechanics-reference.md`; `DM` = `docs/plans/doom-raiders-mechanics-reference.md`; `OOS` = `docs/plans/harpers-out-of-scope-notes.md`.
- `G06` = `campaign/guides/factions/06-force-grey.md`; `NF` = `campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md`; `VOICE` = `.claude/skills/character-voices/voices/force-grey.md`.

**Source limits.** The `.docx` files in `sources/Other remix files/` (including `Vajra Safahr, Zelifarn, and Deepwater Harbor quests.docx`, SOURCE_GUIDE.md:697) cannot be opened with the tools available. Anything that lives only there is unverified: the origin of the "Underclock" badge (zero hits in `sources/`), Tower staff, the scroll vault. `PREV` ranks, s01 and first meeting are R with light edits, so PREV adds little (section 2).

---

## 1. What the page model requires (copy these)

**First Meeting (DR/H model).**
- Skeleton: Gamemaster's Summary with `#### Candidates and Companions` and a secrets block (`What Nobody in This Event Knows` DR:19; `What Is Actually True` H:20). Then `###` scenes, each with `[!readaloud]`, a `[!social]` header line (`Name (Alignment, Species, pronouns) :: summary`), a "happy to discuss" list and a "will not discuss" line, then `[!qna]` blocks (DR:109-150; H:155-197).
- `### Each Candidate's Answer` with `Recording the Answers` (DR:300-306; H:278-290), accept/decline readalouds, a benefits box (`Fang Benefits` DR:326; `Watcher Benefits` H:300), and `### Leaving ...` (DR:334; H:308).
- Close: `Event Outcomes` per character name, `Next Steps` ending "This Event awards no Milestone Points" (DR:412-422; H:330-340), then `## Overview` and a `## Summary` with "After the Meeting" and "Without a Private Meeting" variants (DR:424-436; H:342-354).
- Rules: each candidate answers for themselves; a character already in another faction gets no offer; companions sit in and gain nothing; late acceptance is recorded under the same outcome (DR:420; H:338).
- Harper addendum (HB:451-466): describe the contact object in every event, keep one canonical description, and vary only where it finds the member. A detailed "tailor-scene" plus background colour that is explicitly irrelevant to the meeting was added for the Harpers. Force Grey has no such request on record; the contact object rule does apply (section 5).

**Rank event (DR r03, H r03, BD/DR r50).**
- Trigger: "when an individual member first reaches Renown N" (DR r03:5; H r03:5). Hook delivered the next noon (DR r03:13-18; H r03:14-24). Away rule: the contact object waits at the first surface lodging, meeting moves a day (DR r03:18; H r03:24).
- `What Is Actually True` block (DR r03:22; H r03:26-34). Benefits written as procedures: contact, place, notice, how to order, limit, delay, who else, loss rule (DR r03:110-236; H r03:87-96, 128-135; BD r50:299-318).
- `### Renown Opportunities`: "The rank event awards no Renown" (DR r03:230; DR r50:312). Renown loss: rank kept, benefits suspended (H r03:96; H r50:415).
- Outcome per recipient name read by the next rank; Next Steps says "This Event awards no Milestone Points" (DR r03:242-249).
- r50: hold until the prior rank is marked, fire on the first evening back in Waterdeep (BD r50:17; H r50:18); two-way answer window "10 days, silence is refusal" (DR r50:278-282; BD r50:468-476); Ally Power blocks with CR 2.0 tier-adjusted numbers (DR r50:147-160; BD r50:353-380); Undermountain seeds as a GM block (BD r50:308-318); full branching "empty seats" through speaker lines (DR r50:40-102; BD r50:133-221).

**s01 (H s01, DR s01).** `What Is Actually True` first (H s01:15-21), a plain contact object when the change is itself the signal (H s01:23-33), an evidence list where each line reads a named outcome (H s01:79-145), checks given in the text (H s01:147-157), a GM-only procedure block (`The Fixed Leak Rule` H s01:181-188), no Renown/gold/Milestone (H s01:190-192), 2 outcomes (H s01:204-209). DR s01 sets three outcomes and fixes dates (DR s01:273-277, design notes :3-5).

---

## 2. R and PREV: what each folder contains

### 2a. 00-first-meeting (R `00-first-meeting/ev-01-first-meeting.md`)

**Beats and NPCs.**
- Trigger: "reaches the Force Grey delivery row" of **The Factions Come Calling** (:7). Vajra Safahr sends a *Sending* mid-morning, "exactly 25 words" (:29-31); recipient may reply with up to 25 words; refusal gets silence (:33).
- Decline logic: next morning a different member gets the same *Sending*; second decline files both refusals and sets **Force Grey Offer Closed: True** until the party advances a level (:35, :104-105, :113). Going alone: "Vajra expected the whole party. She says so once" (:37).
- Tower: Castle Ward, "base of Mount Waterdeep", no signage, door opens before they reach the steps, narrow stair, smell of old parchment and metal (:41-43). Vajra at a standing desk, annotating a map; the Blackstaff leans against the desk (:47).
- Offer: Renaer's report; "Renaer tells me you pulled him out of Xanathar's sewer. He also tells me the warehouse had a Zhentarim operation... the Watch missed for three months" (:71); Gray Hands status, entry tier, "Not full membership" (:73); priority "magic being used against people's will" (:75).
- Four `[!dialogue]` answers: What is Force Grey, Why us, What do you want, What do we get (:81-91). On acceptance: a brief note, folded twice, one-line authorization on Tower letterhead "signed with her mark"; the door opens by itself; closing line "Try to get some sleep. The work does not wait for people to be rested." (:93-97).

**Outcomes.** `Force Grey Joined: True / False` ("at least one party member accepts", read by Force Grey missions and s01, :101-102). `Force Grey Offer Closed: True / False` (:104-105). `#### Milestone: None` (:115).

**Gates and rewards.** Gray Hand = Renown 1 (G06:54). No gold. G06:54 lists the Gray Hand benefits (enter Tower at any hour, one situational consumable before missions that need it, Watch officers Friendly). R names none of them beyond the note (:91, :97).

**PREV differences (PREV 00).** Adds a 25th-word sentence to the *Sending* ("Renaer has told me about you.", PREV:27); adds a `[!social]` block with alignment "Lawful Neutral, Calishite human" (PREV:52); adds a DC 14 Insight check (PREV:58); moves outcomes to a proper block (PREV:106-111); drops "pulled him out of Xanathar's sewer" (PREV:76 now says "The warehouse"). Still `[!readaloud]` blocks of 3-5 sentences with first-draft "Up here." entry; no per-candidate recording.

### 2b. s01-the-full-picture (R `s01-the-full-picture/ev-01-the-full-picture.md`)

**Beats.** Fires when "the party requests an audience with Vajra and can demonstrate a complete Grand Game picture" (:7), "no earlier than the first completed lair heist" (:15).
- Four-element test (:29-41): all four factions with what each wants of the vault; the Stone (three Eyes); the vault (about 500,000 dragons, Neverember's embezzlement, location beneath Waterdeep); a live deadline (Founders' Day, Tarsakh 20). Three of four: she asks one direct question and neither pays out nor writes (:41).
- Access: Force Grey members at Renown 1 have standing access; non-members must be vouched for (:45).
- Briefing (:55-79): she confirms three items (Nihiloor's intellect devourer programme; a Kolat Towers arcane signature, "an archmage operated there since Hlam's first report"; Cassalanter residue "consistent with binding circles"). She corrects one assumption ("The Stone tells you where to go... You follow the Stone." :67). DC 13 Wisdom (Perception): the Blackstaff shifts when "500,000" is named (:74). DC 14 Wisdom (Insight): her pause is about what it means to do it (:87).
- She writes a sealed message to Laeral Silverhand (:91-97): "Laeral needs to know the full scope... Keep your operations quiet until she engages." "This was the most consequential thing you could have brought me."
- "+2 renown" "the highest single-act renown in the faction... awarded once in the campaign" (:101; G06:44).
- Outcome `Vajra Briefed: True` (:105-107). Read by Vault of Dragons for Laeral's arrival state (:107, :119) and G06:31.
- Next Steps (:113-121): Vajra will attend the vault opening if wanted; a quiet inquiry to the Lords' Alliance about treasury records; "Harper Mission 2 — The Dead Drop" mention (:121, cross-faction filler).

**PREV (PREV s01)** is R with minor smoothing. The Cassalanter Rule block is retained (PREV:71) and the "+2 renown" line unchanged.

### 2c. r03-junior-griffon (R :1-77)
- Fires at Renown 3 "at the first natural pause" (:7). Sending (:27): "Junior Griffon. Come to the Tower when you're free. New arrangements." (10 words).
- Meets Vajra at the desk. She hands a signed requisition for the quartermaster **Merris** ("a heavyset man on the third floor", "does not ask where things are going", :37), explains the second-floor library behind an iron-latched door (books removed only with her written authorization, :41), and offers one preparatory spell of 3rd level or below, once a tenday, with notice (*nondetection*, *water breathing*, *see invisibility*, *speak with dead*, :43-47). "I don't cast blind."
- Two `[!dialogue]` answers (:51-55). Outcome `Junior Griffon Reached: True / False` read by r10 and "Force Grey Missions 3-6" (:59-61). Next Steps: Mission 2 "remains next in sequence" (:69).

### 2d. r10-senior-griffon (R :1-86)
- Renown 10 (:7). Sending (:32): "Senior Griffon. Blackstaff Tower. I have staff to assign and a requisition to make." (14 words).
- Vajra assigns **Aldris Maeven**, a young researcher "from Vajra's reference division", one deployment per quest (:42-46); produces a *wand of secrets* "if the party has not acquired one" (:12, :22, :40); states that "City officials and Masked Lords are Friendly to you by default" (:50); written authorization for restricted areas (City of the Dead at night, sealed evidence vaults, private Watch armories) at DC 12 Charisma "during a non-crisis period" (:26, :52-56).
- Two `[!dialogue]` answers (:58-62). Outcome `Senior Griffon Reached` read by r25 and "Missions 4-6" (:66-68). Next Steps: M3 or M4 pending (:78).

### 2e. r25-force-grey (R :1-90)
- Renown 25 (:7). Sending (:31): "Full Force Grey. Blackstaff Tower. We have arrangements to formalize and a veteran to brief." (15 words).
- Underclock badge: dark metal disc, Tower seal, Advantage on Charisma checks with city officials and military officers "while the badge is visible" (:39-41). Charge suspension, once per operative, bring the case number (:43-49). **Rhendar Solne**, grey-haired dwarf, eleven years with Force Grey, "two words at a time", one mission per quest up to seven days, "reports to me on return" (:51-55). A 7th-level preparatory spell once per quest (:57). Two `[!dialogue]` answers (:63-67), including "If the operation genuinely requires his death, tell me before it happens." Outcome `Force Grey Rank Reached` read by r50 and "Missions 5-6" (:71-73).

### 2f. r50-force-grey-commander (R :1-167)
- Renown 50, expected in Mad Mage (`[!design]` :17-20). Sending early morning: "Force Grey Commander. Blackstaff Tower before noon. I have made arrangements. Bring your party." (:34).
- At the narrow back window, not the desk. "I've been Blackstaff for three years. This is the third time I've given this rank." (:42).
- The commission: four **veterans** and one **mage**, "constituted as a standing unit for any mission the party chooses" (:50). Aldris leads the arcane element. The four veterans are "named in the commission document" and not introduced (:54). Scroll vault: "One Rare Spell Scroll" from "the full range of Rare-rarity spells from the 2024 Player's Handbook" (:60, :68-69). A final spell "of any level", once (:66).
- Laeral Silverhand arrives unannounced; two readaloud variants ([Standard] and [Post-Vault], :79-81); gives a sealed letter naming every party member who took part in Force Grey operations (:87); Vajra explains Public (names and record published) or Private (sealed with the Open Lord's office) (:107-109, :119-122).
- Outcomes `Force Grey Commander Reached` and `Recognition Public: True / False` (:126-132), read by "Dungeon of the Mad Mage content".

**PREV r03-r50** equal R with bold-term cleanups and `[!npc-narrative]` boxes for Aldris (PREV r10:46) and Rhendar (PREV r25:53). No new facts.

### 2g. Settled facts that must survive (keep verbatim or by name)
- Vajra's first *Sending* text (WDH:3769, App. B:842) plus PREV's Renaer sentence (25 words, PREV 00:27). Closing line "Try to get some sleep. The work does not wait for people to be rested." (G06:35; App. B:892). "Door opens before they knock", standing desk, no sitting room (App. B:874; R 00:15).
- Decline procedure: second Sending to a different member the next day, then wait until the party levels (WDH:3772; App. B:845, 862).
- Rank names and thresholds: Gray Hand 1, Junior Griffon 3, Senior Griffon 10, Force Grey 25, Force Grey Commander 50 (G06:54-58; App. B:916-920). Note WDH:1194 uses different rank names; Appendix B/guide win.
- Every rank benefit in G06:54-58 (section 3 lists the exact text). Outcome names: **Force Grey Joined**, **Force Grey Offer Closed**, **Vajra Briefed**, **Junior Griffon Reached**, **Senior Griffon Reached**, **Force Grey Rank Reached**, **Force Grey Commander Reached**, **Recognition Public**.
- Names: Merris (quartermaster, third floor), Aldris Maeven, Rhendar Solne (invented in Session 32; flagged "accept or replace" in `session 33/35/36/38 handoff.md`; no NF page, no voice profile).
- s01: four-element test, the +2 renown rule once in the campaign, the three confirmations, the vault-location correction, the Blackstaff-shifts and pause checks (DC 13 Perception, DC 14 Insight), Cassalanter Rule (R s01:71-72), sealed message to Laeral, 500,000 dragons.
- r50: three years as Blackstaff, "third time I've given this rank", Public/Private choice, Laeral hands the letter herself.

---

## 3. Guide, organization, NF and source facts the pages must match

**G06 (`campaign/guides/factions/06-force-grey.md`).**
- First Meeting summary :35 (Sending to one member; second refusal closes the offer until the party advances a level; standing desk; Gray Hand; Renaer and the Finding Floon warehouse; closing line). Link :37.
- Rank table :54-58 (verbatim benefits): Gray Hand "may enter Blackstaff Tower at any hour without appointment... one situational consumable... Watch... officers are Friendly by default"; Junior Griffon "one preparatory spell of up to 3rd level on the party before a mission, once per tenday... reference library... mundane equipment and Common potions from the Tower's quartermaster at no cost"; Senior Griffon "one **mage**... one operation per quest... *wand of secrets* (if not already acquired through mission rewards)... City officials and Masked Lords are Friendly... DC 12 Charisma check during a non-crisis period"; Force Grey "suspend one active charge or Watch investigation... one spell of up to 7th level... once per quest... One Veteran Force Grey member accompanies... one mission per quest for up to 7 days... Underclock badge"; Commander "four **veterans** and one **mage**, for any mission they choose... Laeral Silverhand is formally briefed... Open Lord's personal recognition... scroll vault: choose any one Rare Spell Scroll... one spell of any level on the party's behalf, once".
- Grand Game stance (:7-9): Vajra knows Xanathar's mind-control operation and Nihiloor; Hlam's message gave her "Manshoon's shape without the name"; she "doesn't yet know the Stone has resurfaced, or that four factions are competing". She learns incrementally; the full briefing makes her "go still for a long time and then begin writing".
- Renown earners (:43-48): +2 "Bring the Grand Game fully to Vajra's attention"; this is s01's award.
- Missions table (:62-69): +2, +2, +3, +3, +4, +4 (base total 18, plus 1 for joining = 19; plus s01's 2 = 21).

**Organization page (`campaign/setting/organizations/05-force-grey.md`).** Vajra delivers briefings by *Sending* (25 words), summons to the Tower when more is needed (:13); "Characters who join the Gray Hands... are not yet full Force Grey operatives" (:21); Grand Game agenda: Vajra informs Laeral, Laeral "will move quickly to reclaim the 500,000 dragons" (:31).

**NF (Vajra).** "Tethyrian human archmage, neutral" (NF:6 in the header; stat block **Archmage**); Blackstaff three years, aged ten (NF:22); the staff holds Khelben's soul, and Laeral sees her as "an insecure child holding her dead husband's weapon" (NF:22). Includes the line "Manshoon tried to kill me through a junior arcanist" (NF:26), which is an R1 hit if lifted into a player-facing page.

**VOICE (Vajra).** `.claude/skills/character-voices/voices/force-grey.md`:
- Short efficient sentences; Sendings "exactly 25 words, telegraphic and complete" (:9); she counts them on her fingers (:13); sample Sending is exactly 25 words ("Blackstaff here. Rogue construct, Castle Ward, two hours ago. You are closest. Contain it, do not destroy it. Report to Blackstaff Tower by dusk tonight.", :17).
- Calls Laeral "the Open Lord", precisely, and never mentions Khelben (:10); never discusses what is in the Blackstaff (:15).
- Swearing: casual, colourful, frequent in private; "clean in public, barely" (:11).
- Signature phrases: "Irrelevant." / "Force Grey will handle it." / "Next." (:14); answers "Are you alright?" with "Irrelevant." (:13).

**City-officials voice (Laeral).** `.claude/skills/character-voices/voices/city-officials.md:7-20`: cool, measured, never swears in office; calls Vajra "the Blackstaff" in public and "Vajra" in private, pointedly; speaks of Khelben "only by name, and rarely"; never admits her power is diminished; signatures "The city comes first." / "Tell me what you're not telling me." / "That will be all."; lets silence run. Laeral NF: `campaign/setting/notable-figures/city-officials/01-laeral-silverhand.md:12-26`.

**Sources.**
- WDH Joining text and procedure: `sources/adventure-wdh.json:3760-3772`. The *Sending* is 19 words: "I am Vajra Safahr, the Blackstaff. Come to Blackstaff Tower in the Castle Ward at once. Bring your friends." (:3769). R's "exactly 25 words" claim (R 00:29-31) is wrong.
- WDH Vajra: "mid-thirties", "youngest person ever to hold the position", handpicked by Khelben, "rarely makes a decision without first soliciting the advice of the Blackstaff, which contains Khelben Arunsun's spirit as well as the spirits of all the other Blackstaffs" (:32679); runs Blackstaff Academy at the Tower (:32680); only the Open Lord can strip her title (:32682).
- Appendix B First Meeting, `sources/Appendix_B_-_Player_Factions.md:852-895`: Tower "near Swords Street in the Castle Ward", taller than its base should allow (:867); "The door responds to a spoken name. You do not have to speak yours" (:868); standing desk, "She does not move to a sitting room" (:874); appearance: dark unruly hair, sharp green eyes, long blackish-purple coat with shifting elven designs, the Blackstaff "hums at a frequency just below hearing" and she drums fingers on it (:877). Her speech: "Renaer told me about the warehouse..." (:883); "I am not recruiting you for Force Grey... the Gray Hands" (:884); "Waterdeep has a problem with magical coercion right now" (:886); "I speak from experience." (:894). She "does not discuss Undermountain, the Stone of Golorr, or the Grand Game's broader dimensions" (:889).
- Appendix C Force Grey missions: `sources/Appendix_C_-_Player_Faction_Missions.md:1650-1929`; "Gray Hand characters" elevated to Force Grey at the end of M4 (:1927) is a rank clash (section 5).
- PDF 3 p.24: "Force Grey is allied to the Open Lord. If members of the Grey Hands or Force Grey bring the Grand Game to their attention, the Open Lord will quickly figure out what actually happened to the missing 500,000 gold dragons and she's going to get the money back."
- WDMM `sources/adventure-wdmm.json:536`: "No spell other than *wish* can be used to enter Undermountain, leave it, or transport oneself from one level to another. *Astral projection*, *teleport*, *plane shift*, *word of recall*... simply fail." `Sending` still works except to Halaster (:546). WDMM:457-461: Laeral's magic is waning; Jalester hires adventurers for a Runestone fragment on level 20 (12th-level prerequisite).
- Renaer NF (`campaign/setting/notable-figures/independents-allies/02-renaer-neverember.md:26`): Renaer "rescued Vajra Safahr from Khondar Naomal's agents and left the Blackstaff permanently in his debt". Neither R nor PREV uses this. It explains why Vajra acts on his word.
- Finding Floon (`campaign/quests/act-i/finding-floon/overview.md:17-18, 53-55`): Renaer is found in the Zhentarim **warehouse** (ev-03); Floon is rescued from the **sewer hideout** (ev-04). The warehouse was already wiped by a Xanathar Guild raid; four kenku were searching it.

---

## 4. Contradictions, rule hits, and the Vajra / Sending / Offer Closed problems

### 4a. Contradictions (R vs guide/org/NF/sources/other quest files)
1. **Sending word count.** R 00:7, :29 says "exactly 25 words"; the text at :31 is 19 words (WDH:3769). VOICE:9 says exactly 25. PREV fixed the first Sending only. R's four rank Sendings are 10 / 14 / 15 / 14 words (r03:27, r10:32, r25:31, r50:34), against NF:22 "often exactly 25". Recommendation: every Vajra Sending is exactly 25 words and the drafter counts.
2. **Who Renaer rescued and from where.** R 00:71 "pulled him out of Xanathar's sewer" is wrong (Renaer was in the warehouse, Floon in the sewer: Finding Floon overview:53-55). "The Watch missed for three months" (R 00:71) is unsourced; the Splinter warehouse cell was wiped before the party arrived. R 00:21 "Vajra has been watching since the Xanathar sewer hideout" also conflicts. Use "warehouse" (App. B:883, PREV 00:76, G06:35).
3. **Vajra's origin and alignment.** NF header: Tethyrian, neutral. `guides/trollskull-manor/08-notable-patrons.md:55`: NG Calishite. PREV 00:52: Lawful Neutral Calishite. OOS:99 already logs this. I could not confirm the WDH stat line (alignment in a long line). Recommend the NF value (Tethyrian, Neutral) for every `[!social]` header.
4. **Offer Closed vs per-candidate membership.** R 00:7, :14, :35, :104-105 treat the Sending, decline and Offer Closed as party-level (OOS:97 logs R3 M). WDH procedure is party-level. Only the answers at the Tower can be per-candidate (section 6a).
5. **Trollskull Alley ev-04.** Delivery row (`ev-04:31`): "Vajra Safahr sends a *Sending* spell to one party member | Renaer's rescue brought the party to Vajra's attention". Heading `#### Force Grey Joined: True / False` at ev-04:109-110 is the retired party-level flag (same defect OOS:599 logs for Harpers). Financing row (`ev-04:61`): "Tiny Hut and vault scrolls | no gold, but security value; Vajra notes the obligation"; manor guide `02-operating-costs.md:86` gives the exact deal (one *Leomund's Tiny Hut* casting, one item from the Tower's confiscated vault: a *Glyph of Warding* scroll or two *Alarm* scrolls, logged as Gray Hands disbursement). Neither R nor PREV delivers this. Level 2 missions "unlock once enrollment is confirmed" (ev-04:12).
6. **Rank vs mission titles.** R M4 ev-02:61 and Appendix C:1927 say Gray Hands are "elevated to Force Grey status" at the end of M4; R M6 overview:35 and `arc-j-vault-of-dragons.md:51` say the party "leaves as Force Grey Commanders" after M6. G06:57-58 gives those titles to Renown 25 and 50. M4 earns Renown 11 at most on base awards; M6 earns 19 plus s01's 2. The rank events cannot fire at M4 and M6. A decision is needed (section 6e).
7. **Wand of secrets.** R r10:22 says "skip if the party acquired one through Mission 2 rewards". R M3 gives it (M3 overview:31; M3 ev-02:70; WDH:3807 gives the wand for rescuing Meloon at M3). G06:56 says "through mission rewards". Because r10 fires after M4 on base renown, the wand is nearly always already held.
8. **"Masked Lords are Friendly" (r10 :50).** Masked Lords' identities are secret (Harper r50 reveals Mirt's seat only at Renown 50: H r50:26-34, :329-355). A rank that makes "Masked Lords" Friendly by default needs the clause "any Masked Lord whose identity the character has learned".
9. **Rare Spell Scroll (r50:68-69).** The 2024 PHB gives spells no rarity; scroll rarity depends on the scroll's spell level (Rare = 4th or 5th). "Rare-rarity spells from the 2024 PHB" is wrong. A scroll in the Tower's collection is also a "work with the player" placeholder (zero-prep violation).
10. **Vajra says "Laeral" (R s01:93, :137; r50:42-60 via Laeral lines).** VOICE:10 says she says "the Open Lord". Laeral's lines call Vajra "Vajra" in the party's presence (R r50:79), while VOICE says "the Blackstaff" in public.
11. **Rank gating by base renown.** Join 1, M1 +2 = 3, M2 +2 = 5, M3 +3 = 8, M4 +3 = 11, M5 +4 = 15, M6 +4 = 19, s01 +2 = 21. R r03 (Renown 3) fires right after M1; r10 (10) after M4; r25 (25) needs about 4 bonus points beyond s01; r50 (50) is Mad Mage. R r10:78 "M3 or M4 pending" and r25:81 "M5 or M6 pending" ignore this. R mission overview gates (M2 Renown 2, M3 Renown 4, M4 Renown 7, M5 10, M6 14) use an older +1/+2/+2/+3/+3 ladder. Compare HB:78-92 for the Harper gating convention (3/5/8/10/13).
12. **"Exclusive" faction.** `player-factions-overview.md:13` says Force Grey is "Exclusive; earning the leadership's trust first". The same page (:3) says characters can belong to several factions. No R page enforces exclusivity.
13. **"Once per quest" has no definition in Mad Mage.** G06:56-57 and R r10:11, r25:55-57 use "per quest" (App. B says "per arc", retired). Quests are named Dragon Heist entries; Undermountain content has none. Define it in design notes (e.g. one use per descent) or follow the DR/H pattern of fixed single uses.

### 4b. Standing-rule hits
- **R1 (Manshoon knowledge gate).**
  - R 00:65 (Profile): quotes "Manshoon tried to kill me through a junior arcanist", which is M6 content, in the First Meeting.
  - R s01:33 "Manshoon's Zhentarim (the Splinter)"; :19, :62 "an archmage at Kolat Towers", "since Hlam's first report" (OOS:91: R1 T, and it contradicts M1's gating, which gives Hlam only a wrongness shaped like the old Zhentarim). Use "the Splinter" in speech and player-facing text until **Manshoon Named** is marked; Kolat Towers as his home is gated too (HB:68-72).
  - R r50:120 ("Manshoon's Zhentarim, Xanathar's Guild, and possibly Bregan D'aerthe") is a GM warning in a Mad Mage-era event; use the DR r50:22 gate anyway.
  - NF:26 carries the same quote (fix is out of scope; flag).
  - `guides/trollskull-manor/08-notable-patrons.md:57`: Vajra mentions Kolat Towers to an un-gated patron (OOS:139).
- **R2 (Cassalanter secrecy).** R s01:63, :69, :72 ("binding circles of significant scale", "infernal involvement"): the Cassalanter Rule block limits it, but "binding circles" implies summoning knowledge. Keep "conjuration and abjuration residue", cut "binding circles" and the scale; Vajra's `I'll file what you saw. Not what you concluded.` stays (R s01:72). G06:30 uses "consistent with binding circles" too (guide fix out of scope; flag).
- **R3 (members-only).** R 00:7, :14, :35, :101, :111, :113; s01:13, :101, :107; r03:67; r10:77; r25:85; r50:10-11, :50, :87, :138-140. Briefs, renown, rank benefits, the commission, the letter and the scroll are per member.
- **Renown calibration.** s01 +2 is an Earning Renown award (G06:44), not a mission, and is outside the L2-L7 calibration. Keep as written but per member.
- **Event Outcomes instead of flags.** All six R files use `#### X: True / False` headings (00:101-105; s01:105; r03:59; r10:66; r25:71; r50:126-132).
- **Retired formats.** `> **[GM]**` (all six); `> > "…"` (all); `[!profile]` (00:49, r50:95); `[!dialogue]` (00, r03, r10, r25); `[!warning]` (s01:71, r50:119); `[!lore]` (s01:78); `[!design]` (r50:17); `[!item]` (r50:68; not in the foundry-journal block list, foundry-journal/SKILL.md:37-49); `## Read Aloud` heading (00:123, s01:127, r50:150); `#### Milestone: None` (00:115); no `design-notes.md` anywhere. PREV adds `[!narrative]` (PREV s01:129, r50:152) and `[!npc-narrative]` (PREV r10:46, r25:53).
- **Zero-prep placeholders.** r50:69 ("Work with the player to identify a spell"); r50:54 (veterans "named in the commission document" with no names); r10:22 ("Skip this if..."); r25:63 ("That's the full list" with the Underclock effect scattered); 00 "She names the benefits" (:91) without naming them.
- **Milestone.** No Milestone awards in any of these files (00:115 explicitly none).
- **Quests, not arcs.** None in scope. `arc-j` refers to "Force Grey Mission 6" (retained name).
- **Wish.** R M3 overview:29 and PREV use *wish* to remove Meloon's devourer. This is outside scope but affects r50: "one spell of any level" includes *wish* by letter, and WDMM:536 makes *wish* the only spell that works across Undermountain levels. See 5d.
- **2024 stat names.** "Veteran" does not exist in 2024 XMM; use **Warrior Veteran** (HM:571; DM:13). "Mage" is correct (CR 6).

### 4c. The three problems named in the brief

**Trollskull Alley ev-04 delivery row.**
- It names one recipient ("one party member") and a loose eligibility ("Renaer's rescue brought the party to Vajra's attention"); no alignment test, no timing.
- Fix on the First Meeting side: define candidates as every character who belongs to no other faction (BD pattern, BD 00:16). Fix on the ev-04 side (out of scope): replace the `#### Force Grey Joined` heading with the per-character outcome and add the date. HB and OOS already log the same fix for Harpers (OOS:599).
- Missing piece: the Tiny Hut and vault-scroll "renovation help" (5a).

**Vajra's *Sending*.**
- 2024 *Sending* (3rd level): 25 words or fewer to a creature the caster is familiar with; the recipient answers in 25 words or fewer. A stranger recipient is a RAW quirk. WDH ignores it; the Renaer-descriptions-and-Watch-reports background in R 00:21 is enough, and the PREV tail ("Renaer has told me about you") supplies the familiarity.
- Voice rules: exactly 25 words, telegraphic, counted on fingers (VOICE:9, :13). A refusal gets silence; a bare acknowledgment gets no answer (R 00:33).
- Undermountain: *Sending* works inside Undermountain (WDMM:546 excludes only Halaster). That matters for r50 and for anything Vajra sends to a party below the Well.

**Offer Closed logic.**
- Current: party-level True/False; if True and no level-up since, the event does not fire again (R 00:7, :104-105).
- Problem 1 (R3): closed for the whole party, while each candidate answers for themselves.
- Problem 2: R has no rule for a candidate who walks into the Tower after the offer is closed.
- Problem 3: nothing reads it except 00 itself.
- Recommended logic: see 6a.

---

## 5. What each event needs beyond the restored text

### 5a. 00-first-meeting
- **Contact object.** The *Sending* is not an object: describe the experience once (a voice arriving behind the eyes, fast and flat, with no greeting; the recipient hears it while doing something else) and reuse the description in every Sending. The Tower letter note is the Gray Hand's physical credential (R 00:97).
- **Door and Tower.** Use Appendix B's building (taller than its footprint allows, geometry that will not hold up, stone at the top a different shade, near Swords Street) and its door ("responds to a spoken name... opens anyway"). R 00:41-43's "base of Mount Waterdeep" and "no signage" are inventions; keep "no signage" only if you accept it as invented.
- **Vajra's introduction.** She is at the desk annotating a map; she does not sit; the Blackstaff stands within reach. Appearance per Appendix B (dark unruly hair, green eyes, blackish-purple coat). She does not name the debt to Renaer (VOICE:15 "never asks for sympathy"), but a GM block states why she acts on his word (Renaer NF:26).
- **What Is Actually True** (GM block): she decided before they arrived; Renaer vouched; the Gray Hand tier lets her use and test them and revoke cleanly; she suspects a link between the mind-control operations and the gang war but has not confirmed it (App. B:889); she knows nothing of the Stone or the Grand Game's four factions (G06:7). She will not discuss Undermountain, the Stone, the vault, Manshoon, the Cassalanters, the staff, her youth or Khelben. No speaker names Manshoon; **Manshoon Named** gate applies.
- **qna list (6-8, no filler).** What is Force Grey / Why us / What do you want from us / What do we get / Can we keep our other loyalties (address "Exclusive" in one answer) / What happens if we say no / What are the Gray Hands for (the entry tier) / "Are you alright?" ("Irrelevant."). Hold R's four `[!dialogue]` answers as source for the first four.
- **Checks.** Insight DC 14: she decided before they arrived (PREV 00:58). Optional Perception/Arcana at the Tower door (DC 13 Intelligence (Arcana): the door was reading them as they climbed). No more than two.
- **Gray Hand Benefits box** (per accepting candidate; Renown 1, Gray Hand): enter the Tower at any hour; one situational consumable before missions that need it (*potion of water breathing*, *potion of climbing*, or similar; fix a list of two or three and a limit, e.g. one per mission); Watch officers Friendly by default; the letter of authorization. Add a renovation line (party-level, because the manor is a party asset): Tiny Hut casting and the vault item (manor guide 02-operating-costs.md:86).
- **Ends cleanly.** Vajra closes with the settled line; the door opens by itself; no first mission handed over (WDH has none at the pin; App. B:892 says "an assignment within the next few days"; **Consulting Hlam** arrives by its own *Sending* at 2nd level).

### 5b. s01-the-full-picture
- Needs a **What Is Actually True** block up front: Vajra knows more than the party suspects about the Xanathar programme and little about the rest; the Blackstaff's reaction is Khelben and she never comments on it (VOICE:15); Laeral "cannot afford to improvise" is GM-only (R s01:27).
- The four-element test becomes a table of three independent routes per element (Three Clue Rule) so the GM never judges "complete" ad hoc, plus a short incomplete-briefing line per missing element.
- **Remove or soften:** "Kolat Towers arcane signature"; "since Hlam's first report"; "binding circles of significant scale"; the Harper Mission 2 cross-reference (R s01:121).
- **Confirmations (three).** Recommended replacements that satisfy R1 and R2: (1) Nihiloor's programme (as R s01:61); (2) a larger cell behind the Splinter than the party's names for it, which she has traced from Watch incident reports (name Manshoon only if **Manshoon Named** is marked); (3) persistent conjuration and abjuration residue under the Cassalanter villa, only if the Cassalanter Villa Quest Hook (G06:30) has run; otherwise a different third item (Hlam's "buried thing", G06:9).
- **Renown.** +2 to each Force Grey member present at the briefing, once, awarded in the scene. Companions in the room gain nothing. Outcome is marked with their names, and the Vault of Dragons reads it at party level (Laeral prepared, G06:31). A party with no Force Grey member can still brief Vajra only if a member vouches (R s01:45), but the event then marks nothing and awards nothing; Vajra's response is the Lords' Alliance inquiry only. (Option: cut the vouched-non-member route; recommend cutting it, since the org page makes the briefing a member action.)
- **Timing.** The event fires no earlier than the first completed lair heist (R s01:15); G06:9 says she learns of the four factions through the party. Put "after **Fireball!** and the Stone's attunement" in the trigger as a fallback; no new readers.
- **Voice.** Vajra says "the Open Lord" (VOICE:10), and clean in the Tower with strangers. She counts her words aloud only in a Sending.
- **Aftermath.** She does not say when Laeral will move (R s01:117); the party is asked to stay quiet about Laeral's involvement.

### 5c. r03, r10, r25 as procedures
- All three need a `What Is Actually True` block, a per-member hook, and benefits as procedures (contact, notice, limit, who else, loss rule), exactly like DR r03 (110-236) and H r03 (87-135). R has no such structure. Detail:
  - **r03.** Sending (25 words) at noon the day after the threshold; meeting at the Tower; away rule. Spell list: fix a short utility list (the four named in R r03:43 plus a few more), 2 days' notice, once per tenday per member (the spell is for the member and companions; the rank is the member's). Library: define what is in the stacks and give one question per visit answered from the campaign record, using the Harper archive method (H r50:107-114). Quartermaster Merris: cap the free gear (e.g., a gold value per tenday) and fix "Common potions" (the 2024 DMG Common potion list is short: potion of healing, climbing, and so on; confirm before settling). Missing: Merris and the library have no `[!social]` block.
  - **r10.** Aldris Maeven: **Mage** stat block (2024 XMM CR 6) as a Tower ally, Ally Power tier-adjusted (Tier 2 = 65 per DM:217; the Mage's first-turn-KO +4 rule is documented at HM:15; DR chose 65), deployment once per quest per member, 3 days' notice, meets at the surface point or the Yawning Portal, debriefs to Vajra. A `[!social]` block and qna for Aldris. Fix the *wand of secrets* line to read "if the party has no *wand of secrets*" (a party item). Rewrite the Masked Lord line (4a-8). Written authorization: a Persuasion check or a plain yes/no on a clear request; keep DC 12 only if it stays a Charisma check as G06:56 says.
  - **r25.** Underclock badge: define "visible" and scope (city officials and military officers); the charge suspension (once per operative, one case number, what it does and does not remove); Rhendar as a **Warrior Veteran** ally (Tier 2 = 30, Tier 3 = 25; DM:218); 7th-level spell: a fixed list of wizard 7th-level spells she will cast, and where (see 5d). Death qna for Rhendar stays but gets a non-combat alternative. `[!social]` blocks for Rhendar and Vajra.
- **Away rule and per-member tracking** each need a line: where the Sending waits, last-use dates per benefit, who has used the charge suspension.
- Cross-faction: Masked Lord and city-official Friendly benefit stacks with Mirt, Lords' Alliance and BD benefits; one line saying "does not change the Harper r50 secret."

### 5d. r50 (needed because the event fires during Dungeon of the Mad Mage)
- **Timing and hold.** Hold until **Force Grey Rank Reached** is marked for the member; fire the first morning the member is on the surface after crossing 50. The *Sending* reaches a party underground (WDMM:546) and tells them to come up. This mirrors BD r50:17 and DR r50:16.
- **Default is post-Vault.** Replace "[Standard] / [Post-Vault]" dual lines with a primary post-Vault version and a short pre-Vault branch read from **Vajra Briefed**. Make Laeral's Post-Vault line quote an outcome (R r50:81 "funds arrived"), not "the treasury records".
- **Per-member recognition.** Each qualifying member receives their own letter naming themselves. Public/Private is per member; companions are not named unless the member asks Vajra to add them as witnesses (one optional line).
- **The team.** Four **Warrior Veterans** and one **Mage** (Aldris leads). Name them: Rhendar plus three others or leave the three unnamed ("three of Rhendar's colleagues"). Do not leave "named in the commission document" as a placeholder. Ally Power from DM:215-230 numbers: Mage 65 + 4 x Warrior Veteran 30 = 185 at Tier 2 (levels 5-10); Mage 50 + 4 x 25 = 150 at Tier 3 (level 11+). Level-8 base Party Power 132 / 176 / 220 (DM:211). The team more than doubles a party of three, so state the DR rule: rebuild the fight or send a smaller package (DR r50:151).
- **Marching orders.** They meet at the Yawning Portal and go "as far down as you take them" (DR r50:131). Teleportation, plane shift and word of recall fail (WDMM:536). They leave by the first safe exit.
- **The scroll.** Fix a list: spell scrolls of 4th or 5th level (Rare). A short list of 8-12 wizard spells that suit Undermountain, avoiding anything that transports or banishes (those fail, WDMM:536). Candidates to verify against the 2024 PHB before listing: *Arcane Eye*, *Greater Invisibility*, *Dimension Door* (works within one level only), *Wall of Force*, *Cone of Cold*, *Telekinesis*, *Scrying*, *Dominate Person*-free utility options. Not verified in this pass.
- **The final reserve (one spell of any level).** Four decisions needed (6f). Mechanically the problem is WDMM:536: Vajra on the surface cannot cast a transport spell to or from a party in Undermountain, and Touch spells need her presence.
- **Laeral.**
  - Keep Laeral's lines in her voice (VOICE city-officials: measured, formal, silence). She must not reveal her decline (NF; WDMM:458 states it as a secret); the R profile line about the party glimpsing "how diminished she truly is" (R r50:97) is a GM-only note and not a scene.
  - She does not swear.
  - If the party also has a Lords' Alliance member who reached Renown 50, Laeral appears in LA r50 (`lords-alliance/r50-lioncrown/ev-01-lioncrown.md:9-13`, which also has her "private request about missing Alliance agents in Undermountain"); do not duplicate her private asks. Link the two in design notes.
- **Mad Mage seeds** (BD r50:308-318 model, GM block): (1) Laeral's decline and the Runestone fragment (WDMM:457-461, 12th-level quest from Jalester); (2) Halaster is not reachable by *Sending* (WDMM:546); (3) Force Grey's team can take Undermountain assignments from Vajra; keep each seed a one-line fact and say what the adventure does and does not hold.
- **Spell scope.** "Any level" includes *wish*. The standing rule removes *wish* from Force Grey M3/M5 (OOS:586). Recommend: any level, any wizard-list spell except *wish*, and the list of 8-10 spells she will actually cast is in the event.

---

## 6. Recommendations (options, then pick)

### 6a. Candidate, Sending and Offer Closed (00)
- **Option A (recommended).** Candidates = every character who belongs to no other faction (BD 00:16). The first *Sending* goes to one candidate chosen by a fixed rule (the candidate who spoke to Renaer last in the warehouse; if the GM cannot tell, the candidate with the highest Wisdom score). It says "Bring your friends." Anyone who goes can answer at the Tower, each for themselves. If the recipient ignores it, the second goes to a different candidate the next morning. If nobody goes, mark **Force Grey Offer Closed** with the names of the candidates who have not answered; it reopens when the party advances a level (the event re-fires, same 25 words, no reference to the refusals). A candidate who arrives later is recorded under **Force Grey Joined** (DR:324).
- Option B. Per-candidate Sendings the same morning. Cleaner for R3 but departs from the WDH procedure (WDH:3772). Not recommended.
- Option C. Keep party-level logic. Violates R3 and OOS:97. Not recommended.
- **Exclusive faction.** Treat "Exclusive" (player-factions-overview.md:13) as: a character already in another faction gets no offer (same rule as DR/BD/H), and Vajra says so in one qna answer. No mechanic bars later joining other factions. Flag as decision.

### 6b. Scene lists

**00-first-meeting** (scenes in order; `###` headings):
1. `### The Sending` (contact object; recipient rule; re-fire/decline block; eligibility; **What Is Actually True** above in the summary section).
2. `### Blackstaff Tower` (Appendix B exterior; the door; Tower staff glimpsed; one exploration).
3. `### The Standing Desk` (Vajra social + 6-8 qna + Insight DC 14; "If a Player Raises Manshoon" block per DR 264; Stone/Grand Game not discussed).
4. `### Each Candidate's Answer` (`Recording the Answers`; accept/decline readalouds; **Gray Hand Benefits** box).
5. `### Leaving the Tower` (the closing line; renovation help: Tiny Hut casting and the vault item; Next Steps).
6. `### Concluding the Event` (Event Outcomes: **Force Grey Joined**, **Force Grey Offer Closed**; Next Steps: **Consulting Hlam**; "This Event awards no Milestone Points").
- `## Overview`, `## Summary` with "After the Meeting" and "Without a Private Meeting".

**s01-the-full-picture:**
1. `### Asking for the Tower` (how members call: *Sending* or a knock; hold conditions; the first-lair-heist gate).
2. `### What Counts` (GM table of routes per element).
3. `### The Briefing` (Vajra social; qna; the three confirmations; the vault correction).
4. `### The Staff Moves` (Perception DC 13; GM block; Vajra does not look).
5. `### She Writes` (Insight DC 14; sealed message; the Open Lord; lines).
6. `### What Vajra Will Say` (3 qna: attend the vault opening, the Lords' Alliance inquiry, keeping the Open Lord's name out).
7. `### Renown Opportunities` (+2 each present member, once), `### Aftermath`, `### Concluding the Event`.

**r03-junior-griffon:** `### The Sending`, `### The Standing Desk` (naming the rank), `### The Preparatory Spell` (procedure, list), `### The Library` (procedure; Library Research), `### The Quartermaster` (Merris social; stock; limits), `### Renown Opportunities` (none), `### Aftermath`, `### Concluding the Event`.

**r10-senior-griffon:** `### The Sending`, `### The Standing Desk`, `### The Wand` (condition), `### Aldris Maeven` (social + qna + Ally Power block + tactics), `### City Officials and Written Authorization` (procedure), `### Aftermath`, `### Concluding the Event`.

**r25-force-grey:** `### The Sending`, `### The Standing Desk` (names the rank, pen down), `### The Underclock` (badge procedure), `### The Charge Suspension`, `### Rhendar Solne` (social + qna + Ally Power), `### The Seventh-Level Spell` (procedure), `### Aftermath`, `### Concluding the Event`.

**r50-force-grey-commander:** `### The Sending` (before dawn; reaches below ground), `### The Back Window`, `### The Commission` (the team; Ally Power; tactics), `### The Scroll Vault` (list), `### The Final Reserve` (procedure), `### The Open Lord` (Laeral social; Standard/Post-Vault branches), `### The Choice` (Public/Sealed), `### The Answer` (10-day window, silence = Sealed? choose), `### Mad Mage Seeds` (GM block), `### Renown Opportunities` (none), `### Aftermath`, `### Concluding the Event`.

### 6c. Contact objects (HB:451-466 equivalent)
- **Sending.** One canonical description (no object). Variation: what the recipient is doing, who hears, whether it speaks the name. Every Sending is 25 words. Ranks open with the rank name (R r03:27 pattern), then the order.
- **Tower letter.** The Gray Hand credential: folded twice, Tower letterhead, her mark (R 00:97). A separate note for each accepting candidate (not one per party).
- **Underclock badge.** A dark metal disc "the size of a coin but thicker" with the Tower seal (R r25:39); the badge is a Force Grey item given at r25.
- **Commander commission.** Heavy stock, sealed in Tower wax, one per member (R r50:50).
- **Open Lord's letter.** Formal stock, the Open Lord's seal, the member's name (R r50:87).
- **r50 variant.** No Sending at mid-morning: early, before the city is awake (R r50:32); a Tower door-attendant in person is the M6 variant (R M6 overview:25), so do not use it here.

### 6d. Event Outcomes (2-6 per event; all marked per name unless stated)

| Event | Outcomes | Writer | Readers |
|---|---|---|---|
| 00 | **Force Grey Joined** (name per candidate) | 00 | G06; every FG mission (M1 onward, rewritten events); s01; rank events; Trollskull Alley ev-04 (heading to be replaced) |
| 00 | **Force Grey Offer Closed** (names of unanswered candidates) | 00 | 00 on re-fire |
| s01 | **Vajra Briefed** (names of members present) | s01 | Vault of Dragons (unconverted; `arc-j:51`); r50 (branch); G06:31 |
| r03 | **Junior Griffon Reached** | r03 | r10 |
| r10 | **Senior Griffon Reached** | r10 | r25 |
| r25 | **Force Grey Rank Reached**, **Charge Suspension Used** (name, case, date; optional) | r25 | r50; Vault of Dragons / Mad Mage (unconverted) |
| r50 | **Force Grey Commander Reached**, **Recognition Public**, **Recognition Sealed**, **Commander Reserve Spent** (optional) | r50 | Vault of Dragons (unconverted, `arc-j:41, :51`); Mad Mage |

- Readers claimed in R that do not exist: "Force Grey Missions 3-6 where Junior Griffon... is required" (R r03:61), "Missions 4-6" (r10:68), "Missions 5-6" (r25:73). No M-file reads any rank outcome (grep of `m0*` is empty). Cut these claims or wire readers in the M rewrites.
- **Recognition Public** keeps its established name; add **Recognition Sealed** so the choice is recorded explicitly rather than inferred from absence (BD marks Accepted/Declined pairs, BD r50:515-517).
- **Charge Suspension Used** and **Commander Reserve Spent** are optional (only if a later event reads them). Harper r50 keeps **Masked Lord Request Invoked** under the same logic (H r50:426).

### 6e. Decisions the caller must make
1. M4 "graduation" (R M4 ev-02:61, App. C:1927) and M6 "leaves as Force Grey Commanders" (R M6 overview:35; arc-j:51) vs rank events at 25 and 50. Recommend: M4 and M6 give a commission/title only as narrative, no rank, and the ranks stay Renown-based; confirm.
2. Candidate rule and who gets the first *Sending* (6a).
3. Exclusive faction (6a).
4. Whether to add the Tiny Hut / vault-scroll renovation help to 00 (recommend yes, party-level) or cut it from ev-04 and the manor guide.
5. Names: accept Aldris Maeven, Rhendar Solne, Merris, or rename (see 7). Name the three extra r50 veterans or leave them unnamed.
6. Final reserve mechanism (5d): choose (a) cast on the surface or at the Yawning Portal only; (b) Vajra travels down once by the stairs (takes a day per level); (c) a sealed casting she makes at the commission and the party carries (a *spell scroll* in all but name). Recommend (a), with the party's *Sending* as the call; for resurrection-type needs the body comes up.
7. Public/Sealed: per member or per party (recommend per member).
9. Tenure: three years (NF, org page, R r50) vs Blackstaff since 1479 DR (docx, section 10). Recommend three years.
8. Spell lists: the Junior (3rd-level), Gray Hand consumable, Force Grey (7th-level) and Commander scroll lists are not in any source; the 2024 Archmage block and the Common potion list need checking.

---

## 7. NPCs and voice constraints

| NPC | In scope events | NF page | Voice profile | Constraint |
|---|---|---|---|---|
| Vajra Safahr | all | yes (NF) | yes (VOICE:5-19) | clean in public "barely"; swears privately; "the Open Lord"; Sendings exactly 25 words; never discusses the staff; never asks for sympathy; "Irrelevant." |
| Laeral Silverhand | r50, s01 (offstage) | yes (`city-officials/01-laeral-silverhand.md`) | yes (`city-officials.md:7-20`) | formal; no swearing in office; "That will be all."; never admits decline |
| Aldris Maeven | r10, r25 (mention), r50 | none | none | invented Session 32; female per R r10:44 ("She shakes hands once"); Tower research division; speech "very little". Name collides with Aldric Talmost (H M4 salon guest) and Aldric (Trollskull staff guide :67). |
| Rhendar Solne | r25, r50 | none | none | invented; dwarf, eleven years, "two words at a time". Surname resembles Vira Solkan (M6 mole, `manshoons-zhentarim/09-vira-solkan.md`). |
| Merris | r03 | none | none | invented; "does not ask where things are going". |
| Renaer Neverember | offstage (the reason for the Sending) | yes (`independents-allies/02-renaer-neverember.md`) | `independents-allies.md` voice file | his rescue of Vajra is in NF:26 and is unused. |
| Meloon Wardragon | none in scope | yes | yes | not in scope events; do not mention. |
| Griffon Cavalry / City Guard | none | n/a | n/a | WDH:31167 makes the Cavalry City Guard riders; sources do not link them to Force Grey. "Griffon" in rank names comes from App. B. No recurring Force Grey griffon NPC exists; do not invent one. |

- Blackstaff Tower staff: WDH says "a fortress and a wizard training academy" and Vajra "runs Blackstaff Academy" (WDH:3779, :32680). That supports a research division, a quartermaster and a library. Nothing sources a "scroll vault"; the guide has it (G06:58).
- Voice docs for Aldris, Rhendar, Merris do not exist. Follow the DR/H pattern: voice them from the event text and log them in design notes under "Invented Names and Open Items" (as DR s01 notes :21-23).
- Ember-voice targets for all of the above: readaloud about 17-21 words a sentence; NPC speech about 11-15 words; Vajra's speech is shorter (VOICE:9). R's Vajra and Laeral lines are 20-35 words and need cutting.

---

## 8. r50 set-piece, shortened

What the event must give a party that is expected to be in Undermountain:
- **Fires when:** Renown 50 crossed, **Force Grey Rank Reached** marked, first surface morning.
- **Brings:** commission, team (Ally Power in section 5d), scroll, final reserve, the Open Lord's recognition, the Public/Sealed choice.
- **Limits that matter below ground:** transport magic fails (WDMM:536); *Sending* works except to Halaster (WDMM:546); the team goes in through the Yawning Portal.
- **Seeds:** Laeral's decline and the Runestone (WDMM:457-461); LA r50's missing Alliance agents; Halaster.
- **Rules:** Public/Sealed per member; no Renown or Milestone; no *wish*; Manshoon only if **Manshoon Named**.

---

## 10. Docx guide (`Vajra Safahr, Zelifarn, and Deepwater Harbor quests.txt`, plus `Meloon Wardragon NPC Guide.txt`)

Paths: `/tmp/claude-0/-home-user-waterdeep/a2f34fba-baef-54d3-97ed-3a637e207a74/scratchpad/docx-text/`. The Vajra guide is 41 lines; the Meloon guide was searched for Vajra/Force Grey/griffon and read at :96-143.

**Facts.**
- Vajra "the youngest Blackstaff in Waterdeep's history, ascended... in 1479 DR". Predecessor and mentor Samark Dhanzscul was assassinated by Khondar "Ten-Rings" Naomal, a Watchful Order guildmaster; Vajra was captured and tortured in a Neverember family property (Vajra guide :2-3).
- Renaer, Laraelra Harsard and Meloon Wardragon freed her and she completed the rite at the Tower (:3). Meloon guide :125-128 and :153-165: Meloon charged in with Azuredge; Vajra "owes Meloon her life" (:143); she then "welcomed him into our Force Grey special forces as a Protector of the Peace" (:128); she is "the seventh Blackstaff" (:165).
- 1492 DR is the Dragon Heist year, so she has held the staff about 13 years (:4).
- Renaer "personally vouches for the adventurers and brings them to Blackstaff Tower" (:7); "she assesses their skills and offers them a trial mission" (:8). The first trial missions are Zelifarn and the Deepwater Harbor (:10-25), then Meloon (:37).
- Rewards: "Access to Blackstaff Tower and its resources (1 renown)"; "Entrance to Tower as a Mage of the Academy or a member of Force Grey (minor magical boons)" (:35-36). Vajra later activates the Walking Statues (:38); the statues need the Blackstaff (WDH:32723).
- Meloon guide :132: the author offered "a promotion from a Gray Hand to a Force Gray rank" for carrying out the Meloon orders. Vajra's voice at that scene: "always cool, collected... always in control" and "torn between duty and friendship" (:142-143). Her dialogue there is long and emotional, which breaks VOICE:9 and :15.

**What it does not contain (so these stay unverified):** Vajra's species, origin or alignment; the Underclock badge; a scroll vault; Aldris Maeven, Rhendar Solne, Merris; any griffon or Griffon Cavalry link; Sending word counts; the Gray Hand/Junior/Senior rank ladder.

**Open questions it settles.**
- Why Vajra trusts Renaer: confirmed and expanded. NF:26 and Renaer NF:26 are consistent with it. Use as the GM-block reason and as one lore line for Vajra, not as speech: she never asks for sympathy.
- Whether "Renaer's rescue" in ev-04:31 means the warehouse: no new information; Appendix B:883 stays the source.
- "Academy" support: "Mage of the Academy" (:36) agrees with WDH:32680 (Blackstaff Academy), so a Tower research division, an Academy mage like Aldris and a library are plausible. This raises Aldris from invention to supported-in-kind. Names still invented.
- Meloon as Vajra's protege/Force Grey veteran: supports the r25 "Veteran Force Grey member" as a Force Grey fighter type (Meloon himself is the canonical example, Meloon NF).

**Open questions it does not settle.** Origin and alignment (NF Tethyrian/neutral vs Calishite elsewhere), Underclock, scroll vault, griffons, names. The griffon item stays "no Force Grey link".

**New contradictions.**
1. **Tenure.** Docx: Blackstaff since 1479 DR (about 13 years in 1492). NF:22, org page :11 and R r50:42 say "three years", "aged ten". The Meloon guide says "over a decade ago" (:125). Rank r50 ("third time in three years") and the NF "aged ten years in three" depend on the three-year version. Needs a decision; recommend keeping the NF/guide three-year version (the campaign pages agree with each other and with WDH:32679 "youngest ever... mid-thirties") and treating the docx dates as homebrew.
2. **Who introduces the party.** Docx: Renaer brings the party to the Tower in person. WDH and Appendix B: Vajra sends a *Sending*. The remix follows WDH. Option: Renaer vouches offstage only; do not add him as a guide at the door.
3. **Mission order.** Docx puts Meloon after Zelifarn (consistent with R M2 then M3) and offers a Gray Hand to Force Grey rank promotion for Meloon; this is a fourth source for the M-event rank-title clash (4a-6).
4. **Rank benefit.** Docx has "1 renown" for Tower access; the remix gives Renown 1 for joining. No conflict, but do not add a second renown award.
5. **Meloon cure.** Meloon guide :56 says only *wish* can fix his brain. The standing rule replaces this with the Occupying Devourer extraction (OOS:586); not in scope here.
6. **Vajra dialogue in the Meloon scene** (:121-131) lists "Fleetswake" distraction and "a decade ago"; Fleetswake is Ches 21-30 (structural-rules.md:44), after the first-meeting window. M3 timing is out of scope.

**Changes to earlier recommendations.**
- 4a-3 and 7 (origin): docx adds nothing; keep NF values.
- 5a: add one GM sentence in "What Is Actually True": Renaer's rescue of Vajra and Meloon's part in it (docx :3, NF:26) is why she acts on his word. Do not put the 1479 date or Khondar in player-facing text until the tenure contradiction is settled.
- 6e: add decision 9, tenure (three years vs 1479 DR).
- 7: Aldris is Academy-consistent (docx :36); Meloon is the canonical Force Grey veteran.

---

## 9. Report-back list for the Session out-of-scope log
- Trollskull Alley `ev-04:109-110` (retired heading), `ev-04:61` (Tiny Hut and vault scrolls not delivered by any event), `ev-04:31` (delivery row has no recipient rule or date).
- `guides/trollskull-manor/08-notable-patrons.md:55` (NG Calishite), :57 (Kolat Towers mention), `02-operating-costs.md:86`.
- `NF:26` (Manshoon line), NF:6 vs 08-notable-patrons:55 (origin), Force Grey org page lacks the Gray Hand benefits.
- `G06:30` ("binding circles"), G06:9, G06:35 (Sending described without word count).
- R M1 overview:10, :82 (Manshoon named), M3 overview:29 (*wish*), M4 ev-02:61 and M6 overview:35 (rank titles), overview gates (2/4/7/10/14).
- `campaign/structure/arc-j-vault-of-dragons.md:51` (M6 "named Force Grey Commanders"), :41 ("Force Grey's Commander standing").
- `player-factions-overview.md:13` ("Exclusive") vs :3.
- Missing readers: no Vault of Dragons, Dungeon of the Mad Mage or M-event reads any rank or briefing outcome by name.
