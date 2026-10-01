# Out-of-Scope Notes: Knowledge Gates and Membership

Session 35's Harper run set campaign-wide rules and recorded contradictions in other files here without fixing them. That file was lost with the old Codex branch. Session 37 rebuilt it from a fresh read-only audit of every non-Harper page. **Nothing listed here has been fixed yet.** Each item waits for the user to authorize its scope.

## The rules audited

- **R1: Manshoon knowledge gate.** At the campaign's start, nobody in-fiction knows Manshoon runs the Zhentarim splinter. The Doom Raiders believe Floxin leads it. The Harpers and every other faction know only that the Black Network has split, with no specifics. GM-only text may state the truth. (User: "At the beginning of the campaign, nobody knows that Manshoon is running the splinter. The Doom Raiders think Floxin is the leader, and all the harpers and other factions know is that the Black Network is split up, they don't know any specific details".)
- **R2: Cassalanter secrecy.** Nobody knows about the infernalism before the party discovers it. Suspicion is fine.
- **R3: Individual membership.** Recruitment, briefs, Renown and ranks belong to individual members. Non-member companions can help but earn no Renown. Jarlaxle's debrief exception and expressly party-wide gifts stand.

**Reveal timing.** `campaign/structure/arc-e-faction-outposts.md`: Scene 5 (Interrogation House) delivers "the campaign's first named reference to Manshoon" via the *Directive to Zorbog* (l.193, l.211). The sequence is: name at Interrogation House, identity at **Kolat Towers**, motivation at **Vault of Dragons** (l.417). No faction event gates Manshoon knowledge on a named Event Outcome recording that discovery. That is the recommended fix wherever the timing is unclear: gate on an outcome such as **Manshoon Named**, and until it's marked, use "the Splinter" / "the Black Network splinter".

**Levels versus the reveal.** Missions at L2–L3 run before Gralhund Villa ends, so they come before Outposts. L4 can run before or during Outposts. L5 follows the first heist. L6 follows the second. L7 requires all four heists, including Kolat Towers.

Severity key: **V** = violation, **T** = timing unclear, **M** = minor wording.

---

## Lords' Alliance

Base: `campaign/quests/faction-events/lords-alliance/`.

- **m03 ev-01:128** — R1 V. Jalester, readaloud: "The Zhentarim are courting a Red Wizard named Esloon Bezant. Manshoon's people, not Davil's." This is L4 speech. Fix: "the Black Network splinter, not Davil's crew."
- **m03 ev-01:121, :134; overview:25** — R1 V. Player-facing Overview and Summary say "the Manshoon Splinter" and "Manshoon's faction". Fix: "the Splinter".
- **m03 ev-01:61** — R1 T. "A captured Sarvos will not give up Manshoon's identity." Fix: "won't name whoever leads the Splinter".
- **m02 ev-01:110** — R1 T. "Watch surveillance identifies Veralax as a Manshoon Splinter operative" at L3. Fix: "a Black Network splinter operative".
- **m02 ev-01:133; overview:29** — R1 M. The Summary and Overview say "a Manshoon Splinter fixer".
- **m06 ev-01:54** — R1 T. Laeral, speech: "Manshoon's faction has offered me a complete accounting of the Masked Lords…". L7 probably follows the reveal, but the event is gated only on Renown, L7 and M5, and its alternate Cassalanter-thread trigger has no reveal gate. Related GM text assumes Manshoon and Kolat Towers are known: ev-01 :60, :64, :66, :72, :108, :112, :10, :11, :134; overview :32, :40, :42; design-notes :19, :21–25, :29, :31. Fix: gate on the Manshoon-discovery outcome.
- **m06 ev-01:107–108** — R3 M. "+1 if the party…". Fix: "+1 to each Lords' Alliance member present".
- **m06 overview:5** — not a rule issue. It requires L7, but the Writ it grants authorizes **Vault of Dragons**, which 3-heist parties enter at L6.
- **r25 ev-01:64** — R1 M. The lore box says "the Manshoon offer", which inherits M6's gate.
- **s02 ev-01:23** — R1 M/T. "…Xanathar's Guild and Manshoon's Zhentarim" in GM text, for an event that can fire in Act II. Fix: "the Zhentarim splinter".
- **m04 overview:27** — R2 M. The Overview body says "the Cassalanters' infernal timeline". Fix: "a Cassalanter errand".
- **m05 ev-01:107** — R2 M. GM outcome text, "their infernal advisors". It's acceptable as GM truth, but make sure it never surfaces to players.
- **00-first-meeting ev-01:14, :73, :108** — R3 M. "The party accepts or declines". Fix: each character decides. ev-01:77 also still uses a retired `Joined: True / False` flag heading.
- **Style only:** s01, s02, r03, r10 and r50 still use `Flag: True/False` headings.

## Emerald Enclave

Base: `campaign/quests/faction-events/emerald-enclave/`.

- **m01 ev-01:165; overview:14** — R1 V. At L2, the earliest mission, the Summary and Overview say "a Manshoon Splinter arcanist". ev-01:10 (Gamemaster's Summary) is T. Fix: "a Splinter arcanist".
- **m03 ev-01:147, :151; overview:16, :31** — R1 V. The Overview and Summary name "the Manshoon Splinter" at L4.
- **m03 ev-01:141** — R1 T. The Next Steps treat Kelso's name as "early intelligence on Manshoon's information network" for Mirt and Jalester. Fix: "the Splinter's information network". The design-notes at :13 and :15 carry the same label as GM truth.
- **m05 ev-01:168; overview:16** — R1 T. At L6, "a Manshoon Splinter cache".
- **m05 sequencing conflict:** M5 is L6, which is after Outposts, but its outcomes are "Read by **Faction Outposts**" (ev-01:147–149). s02 :183 and :189 also let M5 run after the Full Awakening.
- **s02 ev-01:69, :127, :160** — R3 M. Renown is awarded to "the party".
- **s01 ev-01:5, :14, :38–45, :82** — R3 M. Party-level wording. The gate key may be meant as a party-wide gift; if so, say so.
- **00-first-meeting ev-01:126, :128, :135** — R3 M. Party-level accept or decline.
- **Mission availability** — R3 M. "When the party reaches Renown N" appears in m01 ev-01:157, m03 ev-01:143, m02 ev-02:92, m04 ev-01:179 and m05 ev-01:160. Fix: "when an Enclave member reaches Renown N".
- **Clean:** the legitimate party-wide gifts (m04 charm of heroism, m06 Phaulkonmere Ward, r50 charm of vitality), Jeryth's Illuun discipline, and no Cassalanter-documentation claims.

## Doom Raiders

Base: `campaign/quests/faction-events/doom-raiders/`. No Doom Raiders page currently uses the Floxin belief. Floxin appears only in s01, and there he acts for "Manshoon's cell". **The whole faction needs the Floxin premise written in.**

- **00-first-meeting ev-01:74, :102, :112** — R1 V. In Act I speech, Davil says "The other one is Manshoon's operation", "Manshoon runs the other cell. He wants Waterdeep under his boot…" and asks the party to report on "Manshoon's operation". This is the known lead from Session 35. Fix: Davil believes Floxin fronts the other cell and asks about "the other cell".
- **00-first-meeting ev-01:84, :87** — R1 V. GM text says Davil has a "personal history with Manshoon's faction". **:144** (Summary) — V.
- **00-first-meeting ev-01:11, :122** — R3 M. "Accepting makes them Doom Raiders", "If the party accepts".
- **s01 ev-01:17, :45, :64, :74** — R1 V. This event fires about Ches 25–27, before Outposts. Floxin is written as acting for "Manshoon's cell", and Tashlyn says "I know more about Manshoon's cell than he does". :74 sends the party looking for Manshoon evidence. :78 ("Floxin's name") is correct.
- **r03 ev-01:43** — R1 V. At Renown 3, speech mentions "Manshoon's Splinter communications".
- **m04 (L5)** — R1 T. ev-01-the-approach :26 ("selling us to Manshoon's cell"), :34, :68, :72 (Kolat Towers named as the splinter's base in NPC speech), :126, :177. overview :22, :38. ev-02-the-chase :87, :89 ("reporting directly to Manshoon"), :104, :134 (Vevette Blackwater at Kolat Towers). Arc E holds the base's identity back for Kolat Towers.
- **s02 ev-01:19, :41, :74** — R1 T. "Manshoon has that file now… Kolat Towers."
- **m05 (L6)** — R1 T. ev-01 :29 (Yellowspire's circle "linked directly to Kolat Towers"), :33, :182, :212; overview :16, :20, :37. Yellowspire and its pass-amulet route are also a Faction Outposts intel yield, so the two overlap.
- **m06 (L7)** — R1 T. ev-01 :26, :5, :216, :222, :240; overview :36. **Structural conflict:** L7 requires Kolat Towers to be done, yet **Force Field Gap Intel** (ev-01:222) is "Read by Kolat Towers Scene 1".
- **r25 ev-01:45, :8, :77, :81** — R1 T. "sources inside Manshoon's cell", with no gate.
- **r50** — R1 fine, since it runs in the Mad Mage era. **:144** — R3 M, rank benefit written party-wide.
- **R3 M, systemic:** "when the party reaches Renown N" appears in m01 ev-01:219, m02 ev-01:160, m03 ev-01:194, m04 ev-02:126 and m05 ev-01:204. Next Steps "Award +N Renown" never limits the award to members.
- **R2:** clean.

## Bregan D'aerthe

Base: `campaign/quests/faction-events/bregan-daerthe/`. **R1:** clean, with no Manshoon, Splinter or Floxin references. **R2:** handled correctly (m02 design-notes:11, m05 ev-01:15).

- **00-first-meeting ev-01:8, :85, :190, :196** — R3 V. One PC reporting the surveillance to the Watch marks **BD Contact Severed** and closes recruitment for every PC. That contradicts :177 ("Any party member may accept"). Fix: scope the outcome to the reporting PC, or keep the approach open to the others. **:206** (Summary) — M.
- **s04-contact-severed ev-01:14, :34, :40, :53, :65, :74** — R3 V. It closes BD membership for the whole campaign and assumes no PC joined another way.
- **m03 ev-01:122** — R3 M. "If the party has Lords' Alliance Renown 3".
- **s02 ev-01:7, :25, :51** — R3 M. A members-only briefing written as if the whole party attends.
- **r03 ev-01:41; r10 ev-01:59** — R3 M. Individual rank benefits written as "the party".
- **Not rule issues, but broken:**
  - m04 ev-01:134, :159 send **Nar'l Extracted** to Kolat Towers, but the knowledge involved is Xanathar-lair knowledge.
  - r03:15 and r10 call **Three Nights** "Mission 4". It is Mission 3.
  - The coin-pouch timing disagrees between m02 ev-01:187, s01/m03 ev-01:196 and 00-first-meeting:194.
  - r03, r10, r25, r50 and s01–s04 still use retired blocks (`> **[GM]**`, `[!design]`, `[!profile]`, `[!dialogue]`, …) and `True / False` flags.

## Force Grey

Base: `campaign/quests/faction-events/force-grey/`.

- **m01-consulting-hlam** — R1 V (the worst Force Grey leak). The mission is available from Renown 0 and L2. Hlam tells the party "An archmage thought dead has returned. He is rebuilding…" and the GM note says "He means Manshoon" (ev-01:80–82). Vajra "hears the Manshoon warning first" (:101) and afterwards "knows… Manshoon's Splinter is actively rebuilding" (:118, :122). The Overview and Summary name it too (:128, :132; overview:18, :32). The mission also contradicts itself: :10 says the DC 15 answer names Manshoon, :82 says he won't confirm the name, and design-notes:13 says failure gives "only the Manshoon-shape answer". Fix: Hlam senses a wrongness shaped like the city's old Zhentarim, without naming Manshoon or anything about his return.
- **s01-the-full-picture ev-01:19, :62** — R1 T. Vajra has "known an archmage operated [at Kolat Towers] since Hlam's first report". That contradicts M1 and gives her the base before **Kolat Towers**. The event fires after the first lair heist. :33 is fine.
- **s01 ev-01:63, :69, :72** — R2 M. Vajra's scrying finds "binding circles of significant scale" under the villa. The Cassalanter Rule block limits it, but check that it can't be read as summoning knowledge.
- **s01 ev-01:13, :101, :107** — R3 M. "The party earns +2 renown", which contradicts :45.
- **m06 (Renown 14, L7)** — R1 T, plus an internal contradiction. L7 implies Kolat Towers is done, yet the text treats the captured agent's "Kolat Towers. Manshoon personally directed the operation." as new (ev-01:63; overview:33) and Kolat Towers as still ahead (:85). Vajra's readaloud at :102 says "a Manshoon Splinter asset". GM tags are at :9, :18, :22, :54 and overview :16, :21. Fix: settle the gate and write to it.
- **m06 ev-01:14, :79, :82; overview:35** — R3 M. Commander commissions go to "the party".
- **m04 ev-02:86, :102** — R3 M. "A written commission for each member of the party… full status".
- **00-first-meeting ev-01:14, :90–95, :110–111, :121, :125** — R3 M. The decline and **Force Grey Offer Closed** logic is party-wide. :104 is correctly per character.
- **r03:67, r10:77, r50:10–11, :87, :138** — R3 M. Personal rank benefits are written as the party's. r50:120 names Manshoon, which is fine in the Mad Mage era.
- **Not rule issues:** Vajra's alignment and origin disagree between files (Lawful Neutral and Calishite in the First Meeting and M2, Neutral and Tethyrian in M3 and M4). The rank events, s01/s02, m05 and m06 still use retired blocks and True/False flags.

## Order of the Gauntlet

Base: `campaign/quests/faction-events/order-of-the-gauntlet/`.

- **m01 ev-01:55, :115 (speech), :23, :106 (GM)** — R1 V. At Renown 0 and L2, Savra keeps "the Manshoon file". Fix: "the Splinter file". The GM tags at overview :20 and :23 are fine.
- **m02 ev-02:8–11, :62–64, :117** — R2 T (minor). At L3, the Order formally files that "an infernal creature was deployed to watch Trollskull Manor", and **Imp Captured** is read by **Cassalanter Villa**. The text keeps this at suspicion ("They do not say who bound it"), but it is an official record.
- **m04 ev-01:135–158** — R2 is legitimate here: it is the discovery beat at L5, and it matches arc-e l.475. **:193** (Summary: "We have the grounds now") contradicts Savra's ruling at :158.
- **m05 ev-01:129, :17–21; overview:9** — R2 T. The ledger reveals the Asmodean soul-bargain, its twelve acts, the Founders' Day deadline and the Reckoning *before* **Cassalanter Villa**. Arc-e l.475 reserves the pact's terms and the deadline for the villa. **:154–156**: Savra's petition makes the Lords and the Halls of Justice holders of the contract's documentation before the villa. Fix: trim the ledger reveal, or update arc-e and Cassalanter Villa to expect it.
- **m05 :171 vs m06 overview:6** — M6 "follows Cassalanter Villa", but M5 lets it run "concurrently if the party delays the heist".
- **m06 overview:14, :20, :29; ev-01:17, :28** — R2 T. This is the Session 32 lead about "Victoro's infernal patron" and its "contractual counterpart". Savra's readaloud reports a petition from "Lord Victoro's contractual counterpart". That's fine after the villa, but it leaks if M6 runs concurrently. The rider mechanics have no discovery beat. Fix: hard-gate M6 after Cassalanter Villa, and keep the rider in GM text. **ev-01:152–173**: **Order Recognized** is "read by Cassalanter Villa", which can't happen if M6 follows the villa.
- **m06 ev-01:135–150, :184** — R3 M. Recognition goes to "each member" of the party.
- **r10:12, :17, :57–61, :77, :101** — R2 is safe on its own, but it clashes with M5. Both fire at Renown 10, and Savra still wants "something admissible" after M5 gave her the ledger. :97 is R3 M.
- **r25:45, :97** — R2 T. The r10 "suspicion file" becomes "sufficient predicate" for a diabolism inquiry, which contradicts :37 and r10.
- **s01-the-tithe:8–12, :52–56, :68–74, :84** — R3 M. The tithe's consequences, **Tithe Paid** and **Quietly Reassigned**, land party-wide.
- **s02:9** — R3 M. "The party holds OotG Renown 3".
- **R3 M, systemic:** Renown awards never say "members only".
- **Clean:** m03, r03, r50, 00-first-meeting and s02's Cassalanter handling.

## Guides and Setting

Method: every guide page, organization page and villain page was read in full. The 122 NPC pages were keyword-grepped, and every hit was read. NPC prose that implies the leader without the keywords could have been missed.

**Decision needed first: do the villains know each other?** Xanathar and Jarlaxle are written as knowing Manshoon by name: Xanathar's kill orders, and a Jarlaxle–Manshoon non-interference pact. Jarlaxle and Manshoon are also written as knowing the Cassalanter pact. The user's rule names "the harpers and other factions". It's unclear whether it covers villain factions. The findings below mark these V, pending that answer.

### R1
- **Starting-knowledge tables** (`setting/grand-game.md:28–36`, `guides/gm-guide/running-the-villains.md:34–41`) don't violate R1, but they have gaps. Neither records what each faction knows about the splinter, and neither has the Floxin belief. `running-the-villains` has no Doom Raiders row. Fix: add a splinter-knowledge column (Doom Raiders: "Floxin leads"; everyone else: "the Black Network has split").
- **`guides/factions/07-doom-raiders.md:19, :23, :45, :46, :31`** — V. The Doom Raiders' asks and Renown conditions name "Manshoon's cell". The Outposts hook at :31 calls Yellowspire "Manshoon's Trades Ward relay point". :59 is M. :70 and :71 are T. :7 is M: GM truth sits unmarked inside the stance section.
- **`guides/factions/08-bregan-daerthe.md:9`** — V (pending the villain decision). Jarlaxle is described as competing "with Xanathar or Manshoon".
- **`guides/factions/06-force-grey.md:21`** — V/T. The goal is "Manshoon's arcane operations dismantled", which contradicts :7 ("Manshoon's shape without the name").
- **`guides/factions/05-order-of-the-gauntlet.md:7`** — V. Savra's stance says "In Manshoon's or Xanathar's hands".
- **`guides/factions/03-lords-alliance.md:42, :47`** — M/T. **:67** — T (the L4 mission "Prevent Manshoon's Zhentarim…"). The player guide version correctly says "Splinter".
- **`guides/factions/02-harpers.md:48, :30`** — M. **:61** — T (Wise Owl: "informants embedded in… Manshoon's Splinter").
- **`guides/factions/04-emerald-enclave.md:67`** — T (the L6 "Manshoon Splinter contamination").
- **`guides/factions/10-manshoons-zhentarim.md:39`** — T. Avareen's note at Yellowspire O2 names Manshoon. Yellowspire can be hit before the Interrogation House (:45), which breaks arc-e's "name only at Interrogation House". `setting/villains/manshoon.md:22` gives a different reveal trigger ("two separate intelligence threads").
- **`guides/gm-guide/structural-rules.md:7`** — V. The Doom Raiders "don't acknowledge Manshoon's cell".
- **`guides/gm-guide/grand-game-in-play.md:61, :65`** — V (pending the villain decision). Xanathar's kill order on Manshoon, and the Jarlaxle–Manshoon peer arrangement.
- **`guides/gm-guide/player-factions-overview.md:159, :186, :188`** — V. The Doom Raiders want "Intelligence on Manshoon's cell" and "Manshoon destroyed". :188 also says a Doom Raider PC would "protect Manshoon's rival operation", which is probably a wording error. The player subset at :18 and :122 is compliant.
- **`guides/gm-guide/debts-of-the-city.md:133`** — V. Davil compares himself with "Manshoon's methods".
- **`guides/trollskull-manor/08-notable-patrons.md:57`** — T. Vajra, as an ungated patron, mentions "Lights… in Kolat Towers". (`09-response-teams:47, :49`, where Vevette never names her employer, is the model to follow.)
- **`setting/villains/xanathar.md:32, :39`** — V (pending). Xanathar has "ordered Manshoon killed twice", and his goal is "Eliminate Manshoon". His own NPC page (`xanathars-guild/01-xanathar.md:17`) doesn't say this.
- **`setting/villains/manshoon.md:34`; `setting/villains/jarlaxle.md:48`** — V (pending). Mutual knowledge through the non-interference pact.
- **`setting/organizations/01-harpers.md:6, :17`** — V. The Harpers' "primary concern… is Manshoon's clone and his consolidation". They know the leader, and that he's a clone.
- **`setting/organizations/02-lords-alliance.md:17`** — V. The Alliance is "deeply alarmed by Manshoon's activities".
- **`setting/organizations/06-doom-raiders.md:6, :11, :15, :25, :27, :29`** — V. Throughout, the page has them at war with Manshoon and says Tashlyn built "sources inside Manshoon's cell". It also contradicts itself: :25 says information won't reach Manshoon's agents, while :38 makes Skeemo a traitor who feeds it to them.
- **Notable Figures:**
  - `doom-raiders/01-davil-starsong.md:16` and `02-yagra-stonefist.md:16` — V.
  - `04-skeemo-weirdbottle.md:16, :22, :26` — T. He's an insider, so this may be fine.
  - `gralhunds/01-yalah-gralhund.md:16` — V. It contradicts its own :26 ("not realizing their true master is Manshoon").
  - `force-grey/01-vajra-safahr-the-blackstaff.md:26` — T. An ungated quote, "Manshoon tried to kill me…".
  - `city-officials/04-jelenn-urmbrusk.md:14–26` — T. She knows Manshoon blackmails her, and she appears in Harper M4 at L5.
  - `manshoons-zhentarim/05-agorn-fuoco.md:22` — T. He can be captured at Yellowspire before the Interrogation House.
  - Compliant models: `02-urstul-floxin.md:14, :22` ("will not divulge his master's name") and `01-manshoon.md:31`.
- **Minor:** `setting/waterdeep-lore.md:17` ("Kolat Towers (Manshoon's fortress)" with no GM framing) and `setting/grand-game.md:18`.

### R2
- **`setting/villains/jarlaxle.md:51`** — V (pending). Jarlaxle "knows about their infernal bargain through intelligence".
- **`setting/villains/manshoon.md:35`** — V (pending). "Their infernal connections could have been leveraged."
- **`guides/factions/11-cassalanters.md:81`** — V. BD holds a *Report on the Cultists of Asmodeus* in the Revelation List at the Sea Maidens Faire. **:82** — T. The Harpers hire the party to investigate the shrine.
- **`gralhunds/04-hurv-taldred.md:7, :12, :14, :22`** — T. A Cassalanter cultist with a devotional mark appears in Gralhund Villa in Act II, before discovery. It also implies Cassalanter worship at the Gralhund house.
- **`guides/factions/02-harpers.md:28`** — T. Mirt tells a Harper "the Cassalanters funded the Howling Hatred cult".
- **`guides/trollskull-manor/03-staff-and-hiring.md:64`; `independents-allies/15-hadra-stonebread.md:22, :30`** — T. Hadra knows "which cult members attended private suppers".
- **Minor:** `gm-guide/player-factions-overview.md:157` (Savra knows about a plan and the Founders' Day deadline), `factions/06-force-grey.md:30` (binding circles), `setting/grand-game.md:20` ("galas are recruitment screens").

### R3
- **V: one PC in several factions.** This contradicts the user's rule that "each party member may join one faction":
  - `guides/players-guide/faction-affiliations.md:3` and `guides/gm-guide/player-factions-overview.md:3` ("Your character can belong to more than one faction at once")
  - `guides/factions/01-overview.md:7, :9` (a Harper who is also a Doom Raider, with primary and secondary ranks)
  - `guides/trollskull-manor/02-operating-costs.md:31` (stacking Harper, Lords' Alliance and Emerald Enclave standing)
- **V-leaning: BD membership as a party state.**
  - `gm-guide/grand-game-in-play.md:88`
  - `gm-guide/player-factions-overview.md:171–182` (one Watch report closes BD "for the entire campaign")
  - `setting/villains/jarlaxle.md:3`
  - `trollskull-manor/09-response-teams-at-the-tavern.md:96`
  - This matches the BD s04 finding above.
- **M: rank benefits and missions addressed to "the party":**
  - `factions/07-doom-raiders.md:11, :21`
  - `factions/08-bregan-daerthe.md:14, :31, :32`
  - `factions/06-force-grey.md:55–58`
  - `factions/02-harpers.md:45`
  - `trollskull-manor/09-response-teams-at-the-tavern.md:45, :51`
  - `trollskull-manor/02-operating-costs.md:78–86`
  - `trollskull-manor/03-staff-and-hiring.md:58`
  - `gm-guide/session-zero.md:53`
  - `notable-figures/doom-raiders/07-senna-vael.md:12`
  - `notable-figures/harpers/01-mirt.md:26`
  - `organizations/02-lords-alliance.md:7, :23`
  - `organizations/07-bregan-daerthe.md:11, :13`
  - `factions/04-emerald-enclave.md:57` (a party-wide charm, arguably fine)

### Other inconsistencies
- The Harpers guide places the double-agent warning after Mission 4 (:11) but has the agent exposed in Mission 5 (:22).
- Istrid's loan is 200 gp in `factions/07-doom-raiders.md:14` but 400 gp in `trollskull-manor/02-operating-costs.md:84`.
- `organizations/09-manshoons-zhentarim.md:13` says the splinter broke from the Doom Raiders' network. `history.md:39` says the reverse.

## Main Quests, Locations and Unconverted Lair Docs

The exact reveal beat is `arc-e-faction-outposts.md:207`, Scene 5A (the Interrogation House, Brindul Alley). A *Directive to Zorbog* "signed **Manshoon**" arrives there. The outposts are "the recommended on-ramp, not a hard gate" (arc-e:395), so **no lair heist can assume the reveal has happened**. Gralhund Villa ev-09:42 already records the intent ("Manshoon's name | Not revealed; Floxin never gave it").

### Act I–II quests
- **`act-i/finding-floon/overview.md:51, :53`** — R1 V. The player-facing Overview of the first quest says "Manshoon's Splinter" and "Manshoon's cell". **:49** says "two nights before", which breaks the standing "last night" rule. So does `locations/zhentarim-warehouse/z02-storage-closet.md:14`.
- **`act-i/finding-floon/design-notes.md:21`** — R1 M. Renaer "knows what Manshoon's cell wanted".
- **`act-i/trollskull-alley/ev-04-the-factions-come-calling.md:83–87`** — R1 V. At L2, Davil explains the Doom Raiders / "Manshoon's Splinter" split. Fix: "a rival cell under Floxin". :83 and :63 are R3 M. **:97–98** still emits a retired `Harpers Joined: True / False` flag, while the Harper First Meeting's **Harpers Joined** records each joining character by name.
- **`act-i/trollskull-alley/ev-03-the-neighbors.md:63`** — R1 M.
- **`act-ii/fireball/ev-01-the-fireball.md:204`** — R1 V. Davil calls Floxin "Manshoon's blade". **:194** — R2 T. Mirt: "The Cassalanters funded the Howling Hatred cult…", which contradicts arc-e:81 and :473. **:192, :196, :200, :88** — R3 M. Contacts reach the whole party.
- **`act-ii/fireball/ev-06-the-death-mark.md:68`** — R1 V. Mirt: "Manshoon has placed double agents in the network." **:53** — Yellowspire is placed in the North Ward here but in Castle Ward in arc-e.
- **`act-ii/gralhund-villa/ev-01-what-the-factions-say.md:9, :17, :62, :85–98, :107`** — R3 V. The six faction briefs fire with no members-only gate. Only Jarlaxle's is legitimately open to everyone.
- **`act-ii/gralhund-villa/ev-09-aftermath.md:59`** — R1 M. **:77, :79, :107** — R3 M. **:115** — R2 V/T. Savra has already linked the Cassalanters to the villa and to "infernal corruption".
- **Act II R2 seeding conflict:** `locations/gralhund-villa/g16-master-bedroom.md:12–14`, `gralhund-villa ev-05:11, :49` and `ev-09:39, :144` give the party "the first physical evidence" of a Gralhund–Cassalanter Asmodean cult in Act II. Discovery by the party is legitimate, but arc-e:259 and :473 make Faction Outposts the first evidence. `ev-06:66` and `ev-07:76` also have BD's Fel'rekt offer "Yalah's Asmodean contact". **Decide which act owns the first Cassalanter cult evidence.**
- **Timeline:** Gralhund ev-05:51, ev-03b:92 and ev-03:67 say Renaer was abducted "two tendays ago".

### Structure docs (arc-e to arc-j)
- **arc-e:83, :87, :91** — R1 V. In the pre-reveal Scene 2 consultations, Jalester mentions "the Manshoon thread", Savra has "intelligence on Manshoon", and Tashlyn says "every Manshoon agent carries a pass-amulet to Kolat Towers". Tashlyn's line also contradicts the Floxin belief. **:351, :371, :377, :379** — T. Response teams and debriefs name Manshoon and Kolat Towers even if the Interrogation House was never hit. Gate them on the Directive. **:495** — R3 M, and "Renown 30+" matches no Harper rank (3/10/25/50). `guides/factions/02-harpers.md:30` repeats it.
- **arc-f:147** — R1 V/T. Prisoner Samara: "Manshoon's organization is based in a tower". **:175, :344, :410** — T (Nihiloor's Manshoon file and map of Kolat Towers). **:9, :13, :286** — T (Xanathar at war with Manshoon by name; this depends on the villain decision). **:27, :214** — R3 M.
- **arc-g:531, :537** — **R2 V.** The Harpers "hold documentation of the Cassalanters' infernal contract", and Vajra holds "provenance, specific terms". **:535** — R2 V. The Enclave attributes the infernal ritual to the Cassalanters. **:47** — R2 T. Jarlaxle knows about the ninety-nine cups. **:133, :43** — R2 T. **:197, :203, :397, :437, :499** — R1 T. Victoro's *Report on the Grand Game* names Manshoon and Kolat Towers, and it can be found before the Interrogation House. The same applies to `locations/cassalanter-villa/04-victoros-office.md:27, :29` and `07-ammalias-study.md:22`. **:31, :365–388** — R3 M.
- **arc-h:206, :216, :217, :342, :293** — R1 V/T. Jarlaxle, the Zhentarim strike team and the Doom Raiders' debrief all name Manshoon and Kolat Towers. **:160** — T. **:160, :302, :341, :422** — R2 V. Jarlaxle's *Report on the Cultists of Asmodeus* (see also `factions/11-cassalanters.md:81`). **:29** — R3 M.
- **arc-i:33, :43, :357, :275** — R1 V. Mirt's "Manshoon's couriers", and the Doom Raiders "building toward Kolat Towers… since Trollskull Alley". **:25, :39, :45, :57, :63, :65** — T. Scene 1 assumes the name is known. The identity reveal at :213–223 is correct. **:43, :93** — R3 M.
- **arc-j:49, :51** — R3 V. The Order's recognition and Force Grey's Commander rank go to "the party". **:43–55** — R3 M. **:75, :322** call the Converted Windmill a "Manshoon outpost", but it's a Cassalanter outpost (arc-e 6B).

### Harper outcomes versus their named readers
None of the five unconverted docs uses a Harper Event Outcome by name. These Harper outcomes name a reader that doesn't read them:
- **Faction Outposts:** Shesstra Street Reported (M1), Nethpranter Safehouse Reported (M3), BD Signal Site Observed and Erystian Profile Reported (M4). Arc-e has no Shesstra, Nethpranter or Shield Street lead.
- **Xanathar's Lair:** Corene Rescued / Lost / Left in Place (M5). Arc-f has no Corene, and its Harper hook (:426) says "three Harper assets" were compromised.
- **Sea Maidens Faire:** Jarlaxle Identity Exposed at Harper Salon, and Erystian Profile Reported (M4).
- **Kolat Towers:** Edric Report Delivered (M3), Harper Leak Closed (M5), Splinter Raid Observations Delivered (M6), and S01's leak.
- **Vault of Dragons:** High Harper Reached and Masked Lord Request Invoked (R50), and Jalester Compromise Identified (M6). Arc-j:43 matches M6 only loosely and adds a "Renaer" branch that M6 rules out. **Level conflict:** Harper M6 needs L7, but 3-heist parties enter the Vault at L6.

These get wired in when each lair doc is converted to a quest journal.

---

## Decisions Needed Before Fixing

1. **Do villain factions count under R1 and R2?** This covers Xanathar's kill orders on Manshoon, the Jarlaxle–Manshoon pact, and Jarlaxle and Manshoon knowing the Cassalanter bargain.
2. **Should the Manshoon reveal become a hard gate?** One option is a named outcome such as **Manshoon Named**, set at the Interrogation House, that every later reader checks, with "the Splinter" as the fallback wording. Otherwise, every lair heist's briefings need rewriting for a party that skipped the outposts.
3. **Which act owns the first Cassalanter cult evidence?** Act II (Gralhund g16) or Faction Outposts (arc-e:259, :473)?
4. **OotG M5/M6 pact terms.** Trim the ledger, or let Cassalanter Villa expect a party that already knows the terms?
5. **BD Contact Severed.** Should it be per reporting PC, or remain a party-wide lockout? Per PC would match individual membership.
6. **Level gates that contradict readers.** Harper M6 at L7 versus the L6 Vault; Doom Raiders M6 (L7) versus its Kolat Towers Scene 1 reader; Force Grey M6; Emerald Enclave M5 (L6) versus its Faction Outposts readers.

---

## Doom Raiders event rewrite (Session 38)

Session 38 restored the 26 Doom Raiders faction-event files to their first commits. It then rewrote them into finished adventure text and added design notes to the seven folders that lacked them. The user's decisions for that run:

- **Manshoon Named.** Doom Raider speech names Manshoon, and calls Kolat Towers his home, only when this outcome is marked. Until then they say "Floxin's cell", "the other cell" or "the Splinter".
- **Force Field Gap Intel** moved from M6 to M5.
- **Yellowspire in M5** is a return visit.
- **Scope.** Only the event files were rewritten. Everything below was logged and **not fixed**.

This section supersedes the Doom Raiders line numbers in the section above, which refer to the old drafts.

### New outcomes other quests must write or read

- **Faction Outposts (arc-e):**
  - It must **write Manshoon Named** at the Interrogation House.
  - It must write **Yellowspire Raided** when 5B is entered, because M5 branches on it.
  - **Yellowspire scope change (user, Session 38):** if **Yellowspire Raided** is marked, M5 no longer sends the party back. It runs only its new page, **The Debrief** (`m05-the-yellowspire-job/ev-02-the-debrief.md`), where the members report to Davil's inner circle. For that page to pay out, arc-e 5B must add a relay ledger and three coded letters to Yellowspire, and must write **Yellowspire Ledger Taken**, **Yellowspire Letters Taken** and **Yellowspire Clean Exit**.
  - It should read **Seven Masks Lead** (M1), **Shard Shunners Goodwill** and **Dasher Location Given Up** (M3).
  - arc-e ~l.121 and ~l.325 say the Seven Masks lead needs no check.
- **Xanathar's Lair (arc-f:41):** read **Tashlyn Contact** (s01) and **Davil Released** (s02). Today it reads "Mission 4 complete".
- **Cassalanter Villa (arc-g):** read **Poison Delivered** and **Esvele Warned** (M2) for Esvele's parallel heist. The Black Viper NF page still calls her "Lady Esvele".
- **Sea Maidens Faire (arc-h):** read **Soluun Captured / Escaped / Killed** (M1). Today only an "if the party killed Soluun" clause exists.
- **Kolat Towers (arc-i):**
  - Read **Force Field Gap Intel** (now from M5, not M6; l.43, l.75).
  - Read **Relay Ledger Recovered**, **Vevette Letters Recovered**, **Yellowspire Alarm Sounded** and **Yellowspire Circle Destroyed**. Scene 2's K22 circle and the Lockdown row assume the circle survives.
  - Read **Skeemo at Kolat Towers** in place of "survived Gralhund Villa or Faction Outposts" (l.104, l.168), and **Davil Released**.
  - The ledger's Advantage on the Alert-tier recalibration check and the gap-cycle dusk anchor are M5 inventions to adopt or cut.
- **Kolat Towers outcomes read by M6 Ziraj's Last Hunt:** M6 keys the kill team's motive, Ondra's answers and Davil's debrief to arc-i's **Manshoon operational?** (Destroyed / Simulacrum Only / Alive), Vevette Blackwater's fate (captured / killed / escaped), whether the K18 rune fell and the force field went down, and the result of the Doom Raiders' parallel operation. arc-i has formal names only for the first, so the conversion must name the rest to match.
- **Vault of Dragons (arc-j:53, :262):**
  - Replace "if Mission 6 succeeded" with **Ziraj Survived / Ziraj Fell**, **Splinter Kill Team Broken**, **Splinter Survivor Escaped** and **Splinter Remnant Plan Learned**. The Scene 1/5/6 effects are M6 inventions to match on conversion.
  - Skeemo appears only if **Skeemo at Kolat Towers**. **Skeemo Exiled / Handed to the Watch / Executed** (s02) keep him away.
  - **Vault Partnership Agreed** (r50) ties to Scenes 2, 5 and 6.
  - arc-j's "Tashlyn commits a four-person team at renown 10+" isn't reproduced in the events.
- **No later reader yet:** **Dasher Silence Bought**, **Snobeedle Walked Away**, **Snobeedle Meeting Brokered**, **Emmek Funding Reported** (M3) and **Council Nomination Accepted / Declined** (r50).
- **Name collision fixed:** M5's outcome is now **Relay Ledger Recovered**. Order of the Gauntlet M5 keeps **Ledger Recovered**.

### Guides and setting pages

- **`guides/factions/07-doom-raiders.md`:**
  - It names Manshoon in DR-facing text (l.7, 11, 19, 31, 45–46) and in Earning Renown and Grand Game.
  - l.11: Davil "suspected Skeemo for months" and Tashlyn "confirmed it during his arrest". In the events, Davil learns at M4 and release.
  - l.32 and l.71: Ziraj gives the force-field diagram (now M5), and "three" agents remain.
  - l.33: Skeemo is at the Vault whenever alive.
  - **Retired format:** **Yagra Courteous** is written as a True/False flag (l.37).
  - **Mission table:** it lacks an availability column (now Renown 0/3/5/8/10/13).
  - **Arrest timing:** Tashlyn's first message and the snake are separate deliveries (l.30).
  - **Davil-assist award:** "any substantive effort" (l.49); s01 gives 1 Renown once per member in total (s01:233, :255), not once per approach (corrected in Session 39).
  - **Rank benefits:** Viper "veteran" muscle, and Ardragon benefits "per quest" versus Appendix B's "per arc".
  - **Outposts hook:** "two months" of watching Yellowspire.
- **`setting/organizations/06-doom-raiders.md`:** the arrest comes "after Mission 2" (l.15, l.29); Davil is "always in the taproom" with a lute; and it names Manshoon (l.25, 38, 53).
- **Notable Figures:**
  - **Manshoon lines:** Davil, Yagra and Skeemo.
  - **Featured-in lists:** old "Doom Raiders Mission N — …" names on the Davil, Tashlyn, Skeemo and Kelso pages. Tashlyn's also omits M6, s01 and s02. Yagra's omits the First Meeting and M1.
  - **Kelso:** Dock Ward and "Spy (wererat)", versus Field Ward and Wererat in Order of the Gauntlet M3 and DR M3.
  - **Tashlyn:** "uses flying snakes exclusively", but she briefs in person.
  - **Yagra:** stat block "Thug (with modifications)"; Thug isn't a 2024 name, and r10 uses Warrior Veteran.
  - **Amath:** "Seccent" on the NF page, "Sercent" in WDH.
  - **Floxin:** his page omits the Kolat Towers punishment.
- **GM Guide:** `structural-rules.md:9` has "Manshoon regards the Doom Raiders as deserters". `player-factions-overview.md:186` names Manshoon. `design-notes-running-the-campaign.md:127` calls Heldar a single-scene NPC, but he now appears over two nights.
- **Other guides:** `guides/factions/09-xanathars-guild.md` gives Korgstrod's crew as three duergar in one place and four in another. `guides/factions/03-lords-alliance.md:68` says *The Archer Above* locates Ziraj, but the LA M4 archer is Vhaspar Holmbridge.
- **`setting/waterdeep-lore.md`:** Istrid's lending is in the South Ward; the events use her Dock Ward warehouse.

### Act I–II quest journals

- **`finding-floon/ev-01-yawning-portal.md:115`:**
  - **Yagra Courteous** is still a True/False flag, with "Award Yagra's Courtesy attunement".
  - There is no failed-peace branch; the DR First Meeting infers one.
  - Krentz's crew kills the Doom Raider operative, but the page's own visibility note blames the Splinter.
- **`trollskull-alley/ev-04`:**
  - The Istrid loan is 400 gp; guide and events say 200 gp.
  - The Filthy Meg referral isn't carried by the events.
  - True/False flags remain, including a party-wide **Doom Raiders Joined**.
  - "When the party joins" is written party-wide.
- **`fireball/ev-01:204`:** Davil calls Floxin "Manshoon's blade", which is ungated.
- **`gralhund-villa/ev-01`:** **Davil Brief Received** isn't read by s01. It is also a True/False flag.
- **`gralhund-villa/flowchart.md:101` (Floxin Status: Alive / Dead / Captured):** lists only **Kolat Towers** as a reader. The Doom Raiders events now read it too (Davil's Arrest, and the later events' "Floxin's cell" lines), and it should be turned into named Event Outcomes when Gralhund's flags are converted.
- **`gralhund-villa/ev-09`:** "Keep a low profile. I'll be in touch." is presented as a snake message (s01 makes it Tashlyn's closing line). The Istrid Renown changes "if reported to Tashlyn" now happen at the s01 meeting. **Istrid Horn Helped / Turned In** are True/False flags with no DR reader.
- **Soluun after The Dockside Killer (user note, Session 38):** if Soluun survives M1 (**Soluun Captured** or **Soluun Escaped**), Jarlaxle has to decide what to do about him, most likely throwing him out of Bregan D'aerthe for good. The cover-story disownment becomes real once an agent has killed openly in Waterdeep and been seen doing it. Sea Maidens Faire (arc-h) and the Bregan D'aerthe missions (M4 especially) need a scene or GM note that settles it.
- **`bregan-daerthe/m04-the-compromised-eye` ev l.37:** Krebbyg calls Soluun "disowned" (it's a cover story) and mentions DR M1 without reading an outcome.
- **`emerald-enclave` M3:** it names Kelso as a Splinter buyer. DR M3 doesn't use it.

### Source discrepancies resolved in the events

These were resolved one way in the events; check them if the sources are revisited.

| Item | Sources | Events use |
|---|---|---|
| Waymoot | Appendix C "small square in the Dock Ward"; WDH southern crossroads | WDH |
| Dasher's absence | Appendix C 8 months; WDH 6 months | WDH, 6 months |
| God Catcher height | Appendix C "hundred-foot"; WDH 90 feet | No height given |
| Kolat Towers ward | WDH Southern Ward; arc-i Trades Ward | arc-i, Trades Ward |
| Interrogation House ward | arc-i North Ward; arc-e Trade Ward, Brindul Alley | Brindul Alley only |
| M2 base Renown | Appendix B/C +1 | Guide and brief, +2 |

**Renown 25 and 50 are out of reach on mission base awards.** Base awards total 19 including the join. Guide 07 lists few other sources, and Renown 50 depends on Mad Mage content that doesn't exist yet.

### Invented names and details to accept or replace

- **s01 and s02:** Sergeant Ilmra Dunfell; advocate Corvin Hallowell; the Poplar Walk bench; the kitchen back booth; the salt cog to Baldur's Gate.
- **M1:** Luskan hirelings; Ship Street watchhouse; Rongquan's surety release.
- **M2:** Rallygar's lawsuit; Esvele believing the vials loosen tongues.
- **M3:** Pippa Underbough; Tolliver Greenbottle; Marda Goodbarrel; Tashlyn's 10% cut.
- **M4:** the new third event *The Reckoning*; the accident score.
- **M6:** kill-team commander Ondra Kell; Ziraj's modified Assassin numbers.
- **r03:** Wenna Tarrow and Tarrow's Tallow and Wick, 22 Sail Street.
- **r10:** the Dusty Ladle; Halric Sennet; Brenna Dolgar; Loria Finch; Odalys Quenn; Brannoc Hale.
- **r25:** Drell Hask's and Nessa Thorne's crews; informants Wren Tolliver, Bastian Quill and Hesper Lund.
- **r50:** Toben Ash; the Network Seal; the Council dues.
- **Minor NPCs** without voice profiles are listed in each folder's design notes.

---

## Bregan D'aerthe event rewrite (Session 39)

Session 39 restored the Bregan D'aerthe faction-event folder (`campaign/quests/faction-events/bregan-daerthe/`) to its first commits, rewrote it into finished adventure text, and added design notes to the folders that lacked them. A consistency pass then fixed 14 blocking findings inside the folder (rulings in `docs/plans/bregan-daerthe-research/08-qa-fix-rulings.md`). The user's decisions for that run:

- **M2b is cut.** The Betrayal Pitch has no event in this folder.
- **M6 is the limpet charge.** *The Dive* is a Guild limpet-charge job on the *Scarlet Marpenoth*, not an Eye #3 recovery. The Eye plot, Krenick Durr and the ketch wreck are gone.
- **The Wazoo piece is a suspicion-only fishing expedition.** It names no infernalism as fact.
- **Jarlaxle is gated on Jarlaxle Unmasked.** His name appears in speech or readaloud only when that outcome is marked.
- **Soluun's fate lands in s05.** **Soluun Expelled** is marked per member.
- **Contact Severed is per member.** The closure runs "for the rest of Acts I through III".
- **Nevercott's descriptor.** GM-facing he is a drow in a hat of disguise. In-fiction he looks like a human haberdasher.
- **Scope.** Only the folder was edited. Everything below was logged and **not fixed**.

Sources for this section are the Session 39 research files in `docs/plans/bregan-daerthe-research/` (`05` §2.2, `06` out-of-scope log, `07` drafter reports), the Phase D list in `docs/plans/bregan-daerthe-conversion-brief.md`, and a spot check of the finished folder. Line numbers outside the folder are unchanged by the rewrite. Items taken from `05` §2.2 and not rechecked against the finished events are marked **(05)**.

### 1. Outcomes that need a writer or reader outside the folder

- **Jarlaxle Unmasked (no writer anywhere).**
  - Fireball ev-04 :116–123 still uses True/False headings and sets only **Jarlaxle Informed**. It never marks Unmasked.
  - Sea Maidens Faire (arc-h) is unconverted and names no such outcome.
  - Readers inside the folder: the r25 Jarlaxle-open branch, and every BD line that says "Jarlaxle" aloud.
  - Harper M4 writes **Jarlaxle Identity Exposed at Harper Salon** and **Jarlaxle Discretion Agreement**, and says "BD follow-up reads those commitments" (`harpers/m04.../ev-03:176–179`). No BD event reads either. Harper M4 (L5) also has Jarlaxle admit he "belongs to BD" (ev-03:32) before s02 teaches the BD name **(05)**.
  - See Decisions 1 and 3 below.
- **Nimblewright Noticed.**
  - M1 and Trollskull ev-07:84 write it. Trollskull's version is True/False.
  - No converted quest reads it. Grep finds nothing under `act-ii/fireball/`, though M1's old text claimed Fireball! reads it.
  - Trollskull ev-07:57 puts Vessin "along the parade route". M1 keeps her at her crate at Net and Dock.
  - r10 branches on Fireball's **Nimblewright Ledger Stolen**. Fireball ev-04 ~:85 and ~:110 still hand the ledger to BD members as old True/False text, with no outcome name **(05)**.
- **Faction Outposts (arc-e) writers and readers.**
  - **Windmill Raided**, **Windmill Map Taken**, **Windmill Clean Exit** and **Seven Masks Raided** have no writer. M5 (*The Theater's Back Room*) reads them. arc-e 7B's dressing-room raid sends escalation to Alert, while M5 drops it to Suspicious.
  - **Manshoon Named** is already owed to arc-e from Session 38. BD GM text may name Manshoon (ruling), so BD needs no reader unless it starts gating speech on it.
  - **Ott Kept / Ott Lost** (M3) have no reader. arc-e still has Ott as a gnome (~:209). Every other source has a dwarf.
  - arc-e :93 and :327–331 read "BD renown 3+" in free text, not **BD Soldier Reached**.
  - arc-e :485 and :337 treat "He's useful" as Jarlaxle's standing view of Soluun. s05 has expelled him.
- **Sea Maidens Faire (arc-h) readers.**
  - **Soluun Captured / Escaped / Killed** (DR M1), **Soluun Expelled** and **Soluun Sold the Mooring** (s05). Today arc-h only has an "if the party killed Soluun" clause.
  - **BD Watchers Sold** has no reader.
  - **BD Contact Severed** has no by-name reader. arc-h Paths 2 and 3 still gate on party-level BD membership.
  - **Krebbyg's and Fel'rekt's fates.** No outcome records them. s05 and r50 treat the Faire as the place that sets them.
  - **Zardoz Introduced.** s03 promises arc-h reads it. arc-h doesn't.
  - **Eye 3 Recovered by BD** is dead, since M6 no longer writes it. arc-h :270–276 reads a five-state "BD operational?" instead.
- **Cassalanter Villa (arc-g) readers.**
  - **Florette Reported** and the Wazoo outcomes have no reader.
  - Gralhund ev-06:66 and ev-07:76 have Fel'rekt offering "Yalah's Asmodean contact". That is a third owner of first Cassalanter cult evidence, beside Gralhund g16 and Faction Outposts (Decision 3 in "Decisions Needed Before Fixing").
- **Order of the Gauntlet M2 (`m02-the-black-viper-investigation`).**
  - BD M2 names **Black Viper Source Noted** as a reader and calls the mission "unconverted". It is converted, and it doesn't read the outcome.
  - design-notes.md:7 calls BD M2 the "hidden-gold exposé". It is a devil-worship fishing piece.
  - Gaxly is "unaligned" at ev-01:48. BD M2 has him Neutral.
- **Vault of Dragons (arc-j) readers.**
  - **Marpenoth Saved / Crippled / Lost** (the sub as 500,000 gp transport), **Guild Survivor Escaped**, **Brandath Lead from Brimel** (a second independent path under the Three Clue Rule) and r25's BD Commander proposal.
  - arc-j :55 reads only "completed Mission 6" and "Dread Lord renown". :75 and :322 call the windmill a "Manshoon outpost".
  - Level gate: BD M6 is L7 and fires after Kolat Towers.
- **Xanathar's Lair (arc-f).**
  - It reads none of **Nar'l Active / Extracted / Eliminated / Cleared**, **Nar'l Bypass Learned** or the smokepowder handoff. arc-f assumes Nar'l is alive in X35 (:99–111, :184).
  - Force Grey M4 still has Nar'l alive in the lair (ev-01:103) and has Soluun as a prisoner in X24 "claiming BD affiliation" (ev-01:141, :145; ev-02:75; design-notes:15). That contradicts DR M1 and s05.
  - M4 writes **Fence Settled / Gone / Untouched**. Only Settled has a reader.
- **Doom Raiders M1 (`doom-raiders/m01-the-dockside-killer/ev-01:456–458`).** It tells Sea Maidens Faire that a Captured Soluun is "back aboard" and an Escaped Soluun "returns". s05 expels him, so both lines are wrong. DR M1 also calls his disc forged. s05 treats it as BD's own work **(Notable Figures: see section 4)**.

### 2. Guide 08 and `player-factions-overview.md`

`campaign/guides/factions/08-bregan-daerthe.md`:

- **:9** — Jarlaxle competes "with Xanathar or Manshoon" (R1, pending the villain decision). Also says Jarlaxle holds Eye #3 aboard the *Marpenoth* from before the campaign. The events cut that plot.
- **:11** — The Cassalanters hold a "deadline", which arc-g:47 repeats.
- **:14** — Pouches arrive "at the party's door". The events give the first pouch to one named member.
- **:16** — A Renown 5+ *Scarlet Marpenoth* extraction after M4. It was never implemented, and r03 excludes the *Eyecatcher*.
- **:29** — M1 is delivered via theater tickets to Kreb Sorrush. Now Nevercott briefs at the manor on Ches 20.
- **:33** — The Vault proposal at "Dread Lord renown". BD has no such rank. r25 delivers it at Commander.
- **:36–37** — Joined and Severed are party-wide and permanent. The events make both per member, and Severed lasts through Act III.
- **:56–60** — The three-favor list, Uncommon item, assessment and 20% fence discount aren't in Appendix B l.790–796 **(05)**.
  - :57 says Jarlaxle shares the intelligence. In r03, Nevercott delivers it.
  - :58 says Jarlaxle assigns the Spy. In r10, the contact does.
  - :59 and the rank rows say "the party" where the events are individual.
  - :60 gives the ship and network unconditionally. r50 now needs a favor and a price.
- **:66–71** — Lists six missions including M2b, which is cut.
  - :67 describes the Wazoo piece as "hidden gold and missing servants". The event is suspicion-only devil-worship.
  - :69 says "Jarlaxle forbids killing him" and lists approaches. The event uses a tiered order.
  - :70 says a "false name" for the windmill. arc-e:277 has tenants.
  - :71 has the sub "moored under the *Eyecatcher*". M6 now matches the limpet charge, but the berth is the old Faire pier at Smugglers' Dock, not under the Eyecatcher.
- **Rank benefits** (Initiate safe house aboard the *Heartbreaker*) have no event. Appendix B writes "Hellbreaker" **(05)**.

`campaign/guides/gm-guide/player-factions-overview.md`:

- **:169, :173, :176** — Joined, Severed and Acknowledged are party-wide. One Watch report closes BD "for the entire campaign". **BD Acknowledged** is never written by the BD first meeting.
- **:182** — "Dread Lord renown".

Appendix B (sources): l.715 says BD recruits "only drow", and l.761 has Nevercott name BD outright. The repo takes any PC and has him say it once, if pressed. Appendix B writes "ends contact for now", so Severed may be reversible. Nothing in the guide says so.

### 3. Organization page and villain pages

- **`organizations/07-bregan-daerthe.md`**:
  - :8 M1 via theater tickets (now the manor on Ches 20).
  - :11 and :13 use "the party". :11's "After Mission 4" retirement for Nevercott is right, but s03:16 retires him after M4 while r03 and r10 still use him.
  - :38 a velvet pouch signed "J." The events use black linen, unsigned.
- **`villains/jarlaxle.md`**:
  - :3 membership as a party state.
  - :6 and :8 (Notable Figures page): see section 4.
  - **:13 and the Zord cover descriptor.** Three versions exist: "Illuskan" (s03:38, the org page), "Waterdavian carnival operator" (Fireball ev-04:30), "Calishite eccentric" (:13).
  - :48 a Manshoon non-interference pact (R1, pending).
  - **:51 Jarlaxle "knows about their infernal bargain through intelligence".** That breaks Cassalanter secrecy (R2, pending).
- **`villains/manshoon.md:34–35`** — Mutual knowledge through the pact, and "infernal connections could have been leveraged".
- **`villains/` and guides on Eye #3.** `running-the-villains.md:25` and arc-h :9, :11, :15 say Jarlaxle holds Eye #3 aboard the *Marpenoth*. The BD events no longer touch the Eye.
- **`gm-guide/grand-game-in-play.md`** — :88 BD membership as a party state, :65 a Jarlaxle–Manshoon "peer arrangement".
- **`gm-guide/design-notes-running-the-campaign.md`** — :122 says Vessin is "covered by Krebbyg's entry", but his page doesn't cover her. :126 calls Gaxly a "single-mission NPC", but he is also in OotG M2.
- **`trollskull-manor/09-response-teams-at-the-tavern.md:96` and `08-notable-patrons.md:129–133`** — Jarlaxle appears in disguise at the tavern each time. s03 has Nevercott disappear.
- **R2 and the Wazoo piece.** The older M2 text had Jarlaxle's exposé "match the Cassalanter villa's lower temple" **(05)**. The rewrite keeps it to suspicion. The org page, guide 08 and arc-g's Jarlaxle lines (:47, the ninety-nine cups) still assume more.

### 4. Notable Figures pages

- **Stat names.**
  - **Soluun** (`02-soluun-xibrindas.md`) lists the Drow Gunslinger. Ruling: Soluun is the 2024 **Scout** everywhere, as in DR M1 and s05. **Krebbyg and Fel'rekt** keep the WDH **Drow Gunslinger**, since 2024 has no equivalent.
  - **Ott** (`06`:6) lists "Cult Fanatic". The 2024 name is Cultist Fanatic.
  - **Jarlaxle** (`01-jarlaxle-baenre.md:6`) lists "Swashbuckler".
- **Featured-in lists that still name The Betrayal Pitch.** Jarlaxle (:8), **Krebbyg** (`04`:8) and **Nar'l** (`03-narl-xibrindas.md:8`). Nar'l also lists *The Wazoo Affair* as Featured-in.
- **Nar'l's tenure.** His page (:8, :22) says "three years". The events use "a year" (WDH), and arc-f :17, :216 and arc-h :15 say eleven years. His page also needs the Wazoo entry checked.
- **Ryvarra** (`09-ryvarra.md:14, :22`) — "weekly" reports. The First Meeting says every tenday. Her NF page says three months, while Finding Floon ev-01:29 says "two weeks" and "a drow woman".
- **Soluun's cover story** (`02-soluun-xibrindas.md:22, :26`) — disownment as a cover story with a forged BD ID. s05 makes it real and treats the disc as BD's own work. DR M1 still calls it forged.
- **Lif** — the NF page has a half-elf. His voice profile has him guarding the cellar hatch, while trollskull-manor tm03 has no manifest in the cellar.
- **Ammalia** — Featured-in lacks Florette. **Victoro** `:9` lists "The Shrine on Aveen Street", unverified.
- **Krebbyg's age and tenure (05).** NF:22 says young and rash. The older drafts had "twenty years", "sixteen months removed from the Underdark" and "worked with Vessin for three years". Not rechecked against the finished events.
- **No pages exist** for Vessin, Ilphrin Quiss, Pelsha, Vorn, Sarev Oust, Brimel Crestfall, Florette Cressyn, Krenick Durr, Mirilin Ashford or Marek Dunmere. See section 8.

### 5. Act I–II quest journals

- **`act-i/finding-floon/ev-01`:29** — Ryvarra "two weeks" and "a drow woman", against three months on her page.
- **`act-i/trollskull-alley/ev-03`:45, :47, :57** — a visibility gate and an alley placement for Ryvarra, and a retired flag. It writes **Ryvarra Identified**, which the First Meeting also treats as a second chance.
- **`act-i/trollskull-alley/ev-04`:**
  - :45 and :115–122 emit **Joined**, **Acknowledged** and **Severed** party-wide and permanent (Severed "permanently"). The First Meeting and s04 make them per character. Nevercott still calls on Ches 13.
  - :115 is a second writer of Joined. :118 writes **BD Acknowledged**, which BD never reads.
  - :60 renovation financing and Quilm are unused.
- **`act-i/trollskull-alley/ev-07`:** :24 parade route against the Twin Parades addendum, :26 the Faire arriving Ches 21, :55–57 Vessin placement and a free-text "BD operative", :84 **Nimblewright Noticed** in True/False.
- **`act-i/trollskull-alley` ev-01 and ev-06** — a retired **Lif Appeased** flag.
- **`act-ii/fireball/ev-01`:108** — cites Trollskull ev-05/06 for the parade sighting. It is ev-07.
- **`act-ii/fireball/ev-04`:**
  - :28 Zord's office, and a Waterdavian descriptor at :30. s03:9 says Zardoz "meets the party in person for the first time", and Trollskull ev-05 already has Zord sponsoring.
  - :85 and :110 the ledger given to BD members with no outcome name.
  - :106 a party-level "BD operative" check, :112 Renown in True/False, :116–123 **Jarlaxle Informed**, with no **Jarlaxle Unmasked**.
- **`act-ii/gralhund-villa/ev-01`:** :11, :65 and :97 party-level BD checks, and **Jarlaxle Brief Received** in True/False. **ev-02:94** is **BD Team Spotted**. Nothing in BD reads either.
- **`act-ii/gralhund-villa/ev-09`:125** — Renown in True/False.

### 6. Structure docs and SOURCE_GUIDE

- **arc-e:** the Ott gnome entry (~:209); the windmill's ward and "Manshoon outpost" label (arc-e 6B is a Cassalanter outpost); :277 tenants against guide 08's "false name"; 7B's Alert against M5's Suspicious; :93 and :327–331 free-text BD renown; :337 and :485 "He's useful". The writers in section 1 are owed.
- **arc-f:** Nar'l's eleven-year tenure (:17, :216); X35 assumes Nar'l alive (:99–111, :184); :43 and :105 free-text BD operative; no Nar'l branches, **Nar'l Bypass Learned** or smokepowder handoff; the App C route under the Dock Ward against WDH's Castle Ward stair; the 2024 Mage has no Sending (swapped in by M4).
- **arc-h:**
  - **The Betrayal Pitch.** :105–109 and :378 are now the sole owner, since M2b was cut. The Pitch has a 500 gp artifact job in Zord's quarters and a Nevercott reveal, and it assumes Zord in the quarters.
  - **Pier.** :9 and :71 put the ships at a Mistshore pier. A drow mage is at the Eyecatcher's helm.
  - **Ranks.** :45 and :103 use "Operative rank (Renown 10+)" and "Initiate or Soldier (Renown 1–9)". The ranks are Initiate 1–2, Soldier 3–9, Officer 10–24.
  - **Nevercott.** :79 and :107 use him at the Shipwright's Ball and for the Pitch. s03:16 retires him after M4.
  - **Eye 3.** :9, :11, :15 and :270–276 (see sections 1 and 3).
  - :162 a BD identification token.
  - :9 Jarlaxle arrives in the last tenday of Ches, which predates s02's and Krebbyg's "months".
  - Party-level BD gating, and no reader for **BD Contact Severed**.
  - The "Operative" rank label and the Eye 3 handling both need rewriting when arc-h is converted.
- **arc-j:** :55 reads "completed Mission 6" and "Dread Lord renown"; :75 and :322 "Manshoon outpost"; nothing wired to the **Marpenoth** outcomes or **Guild Survivor Escaped**.
- **SOURCE_GUIDE.md** (~:219) puts the windmill in the North Ward. Appendix C l.1507 says Southern Ward, and the BD M5 events use the North Ward. It also claims Sargauth as a BD seat, which WDMM doesn't support.

### 7. Location pages

- **J10 labelling.**
  - `locations/sea-maidens-faire/02` calls J10 the *Heartbreaker*'s captain's cabin.
  - arc-h :85 and :152 call it the Eyecatcher office with a drow mage.
  - WDH's J10 is the Eyecatcher dining cabin.
- **Smugglers' Dock against Mistshore.** The Faire area overview puts the *Heartbreaker* and *Hellraiser* at a private pier at Smugglers' Dock. arc-h :9 and :71 say Mistshore. M4 now says the Dock Ward pier, and M6 uses the old Faire pier at Smugglers' Dock. The M6 reserve berth is invented.
- **The *Marpenoth* crew roster.**
  - The area-overview roster has "three drow gunslingers (U3, U4, U5)", but U4 is Jarlaxle's stateroom.
  - Marpenoth access is only via J30 or underwater. s05 adds a blindfolded passage.
  - The costume room and rehearsal booth (r03) aren't in the Faire location files.
- **Trollskull Manor area overview** (~:41) has Lif as a dwarf. His NF page says half-elf.

### 8. Invented names to accept or replace

None of these has a Notable Figures page or an Ember source. Each is voiced from its event text.

- **Vessin** (about eleven; the older M1 had a tiefling of sixteen, Appendix C has "Mira, about 11"). She appears in about eleven places. `design-notes-running-the-campaign.md:122` says Krebbyg's page covers her. It doesn't. Replace or write a page.
- **Nevercott's voice** has no profile. He is voiced from his persona in the First Meeting. A profile belongs in `character-voices`, written by the main session if the user asks.
- **Marek Dunmere**, in the First Meeting and s04 (constable walking the alley two nights).
- **s01:** Dunstan Rook, Orla Pennick, Hanna Voss, and the playbill *The Duke's Last Supper*. Squiddly is used from Trollskull Alley without a voice line.
- **s02:** Constable Harl Pimm (also in M5, with Malcolm Brizzenbright as written on his page), the grey coat on peg seven, the torn-ticket signal, the playbill's circled price.
- **s04:** the flower pot, Fel'rekt's note with the returned card, the ten-day window and Ches 20 cutoff, the 50 gp price, and the rule that a severed character may stand beside a member in public scenes.
- **r03:** Odalys Vane, Ostrin Brindle, Brindle and Daughter on Dock Street, the cover names Pell Harrowgate, Tamsin Orr and Corwin Alder, and the 300 gp, three-visit and twenty-day numbers.
- **r10 spy roster:** Ilphrin Quiss, Nyrae Zauvir, Dhaer Oussen, Velkyn Hune and Ghaena Tormyl. Ilphrin has no page and no mechanics line (**05**).
- **r25 and r50 crews:** Ilmra Kelnozz and Brythe Mizzrym (r25 Crew Two, absent from r50), plus Pelsha, Vorn and Sarev Oust (**05**; Sarev Oust was to be dropped or justified in r50).
- **M4:** Tarn Hobble and Dorrim Ketch, and Arannis Nur'zekk as spokesman for the four drow (WDH names them but not who speaks). The grell, the Guild's response and Ahmaergo's clerks have no profiles.
- **M5:** Brimel Crestfall and Florette Cressyn (draft names, no pages), Marra Selby (the lease name, which Brimel says does not exist), Captain Ilsa Dalloway, the household wine merchant (on BD's books "a year"; design-notes:5 may still say "two years"), the Net Street sailmaker's doorway, the printed berth pass and the seat phrase.
- **M6:** Orlo Stannick, Nell Corvane and Hesk Rooke. The ruling renames Tamsin Rooke to Hesk Rooke because Tamsin Orr (r03) shares the first name. The rename is applied across M6. The limpet charge figures, the Dawn Clock, the 150 gp bribe, the 250/100/0 gp purses and the 05:30 first light are invented.
- **r50:** the Rizzeryl letter. Rizzeryl is a WDMM drow mage of House Auvryndar in the Base de Résistance, but the favor is invented: a safe road for an Auvryndar courier in exchange for the Xanathar Guild's mooring list. The Skullport water route is invented too. SOURCE_GUIDE's Sargauth claim is unsupported.
- **Dropped with the Eye plot:** Krenick Durr (M6). **Unchecked:** Mirilin Ashford and Lady Ashford's reception (M1) appear only in the older reports (**05**). Check whether the finished M1 still uses them before replacing.
- **Other details to accept or replace:** the spider-and-blade coin (r50) and the spider chalk mark (M4), which the user was asked to settle as a rejected symbol.

- **Cassalanter ruling follow-ups (Session 39):** `villains/jarlaxle.md:51` should name Vessa as Jarlaxle's source. **Cassalanter Villa** (unconverted) must read **Cassalanter Pact Shared with BD**, which BD M5, s03, r03, r10, r25 and r50 set, and in which Vessa helps that member openly. Guide 08:67 still describes the exposé as "hidden gold and missing servants".

### Decisions for the user

1. **Does Jarlaxle know the Cassalanter pact?** **Answered (Session 39):** yes, through Vessa, his doppelganger spy, and he doesn't tell members unless they work it out ("Jarlaxle knows about the Cassalanters, he has a spy there. He won't tell the members unless they figure it out themselves"). `villains/jarlaxle.md:51` now matches. Still out of line: `manshoon.md:35`, arc-g:47 and guide 08:11 and :67 where they give the knowledge to anyone else.
2. **Where does the Zord cover come from?** Illuskan, a Waterdavian carnival operator, or a Calishite eccentric. Fireball ev-04, s03, the org page and `jarlaxle.md` each pick one.
3. **Does Fireball ev-04 set Jarlaxle Unmasked?** If yes, ev-04's ledger becomes the writer and the Faire isn't the only one. If no, arc-h must write it, and the Harper M4 exposure stays unrelated.
4. **Does guide 08 adopt per-member wording?** The events are individual. The guide rows, `player-factions-overview.md` and `trollskull-manor/09` say "the party".
5. **Where does Renown 25 and 50 come from, for every faction?** BD base awards total 19, and bonus lines supply roughly 37 at most, per the ruling "bonus lines and Earning Renown supply the rest". The Doom Raiders run reached the same gap. 50 may belong to the Mad Mage.

## Doom Raiders consistency pass (Session 39)

The Session 39 DR QA (`docs/plans/doom-raiders-consistency-pass-s39.md`) fixed everything inside the DR folder (`docs/plans/doom-raiders-qa-fix-rulings-s39.md`). These are the findings outside the folder:
- **Istrid in Gralhund ev-09.** `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:71-79` has Istrid flee to Baldur's Gate or be taken by the Watch. DR M3, the M5 Debrief, r03 and r50 still use her at her Dock Ward warehouse. Gralhund needs an outcome that DR reads, or Istrid must stay in the city.
- **First-name collisions with BD.** These pairs share a first name:
  - Ilmra Dunfell (DR s01) and Ilmra Kelnozz (BD r25/r50);
  - Odalys Quenn (DR r10) and Odalys Vane (BD r03);
  - Ilsa Carrow (DR r25) and Captain Ilsa Dalloway (BD M5).
  Rename one of each pair when the invented names are reviewed.
- **Wererats in OotG M3.** `order-of-the-gauntlet/m03-the-shard-shunners/overview.md:22` and `ev-01:16, :149` say "Silver or magic weapons required". The 2024 Wererat has no such rule. Its DC 17 Intimidation dispersal also differs from DR's DC 15 Persuasion.
- **Senna Vael.** `setting/notable-figures/doom-raiders/07-senna-vael.md`, org page 06 and `guides/trollskull-manor/03-staff-and-hiring.md` use her, but no DR event does.
- **Seven Masks Lead.** No BD event reads it. Its readers are Faction Outposts and Sea Maidens Faire (both unconverted).

