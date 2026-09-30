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
