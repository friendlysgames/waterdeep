# Harper faction events research: first meeting, s01 and rank events (r03, r10, r25, r50)

Scope covered: `00-first-meeting`, `s01-the-cell-is-compromised`, `r03-harpshadow`, `r10-brightcandle`, `r25-wise-owl`, `r50-high-harper`. Nothing was edited and no plan file was written.

**Abbreviations**
- `H` = `/home/user/waterdeep/campaign/quests/faction-events/harpers/`
- `P` = `/tmp/claude-0/-home-user-waterdeep/6f58d0d2-f379-5140-92f5-a2193a7fb83a/scratchpad/harpers-prev/`
- `BD` = `/home/user/waterdeep/campaign/quests/faction-events/bregan-daerthe/`
- `DR` = `/home/user/waterdeep/campaign/quests/faction-events/doom-raiders/`

**Source limits**
- The `.docx` files in `sources/Other remix files/` cannot be opened with the tools available, so they were not checked. Per SOURCE_GUIDE, the Mirt/Harper material in them is the Waterdavian's Guide and the Renaer Guide.
- `3. Player Character Factions.pdf` is only 3 pages (pp. 23–25) and has a single Harper paragraph.
- The Harper rank and mission detail lives in Appendix B and Appendix C.
- There is no `harpers-mechanics-reference.md` in `docs/plans/` (only BD and DR have one), so the previous version's numeric claims are unverifiable.

---

## 1. What the restored first-commit drafts contain

**Retired formats used by every restored file in scope**
- `> **[GM]**` zones, with a `#### Gamemaster's Summary` heading inside them.
- `> [!profile]` blocks, in all of them except s01 (`**Running Mirt**` and similar).
- `> [!design]` in `r50:16`.
- `#### X: True / False` flag headings.
- `#### Milestone: None` (`s01:91`).
- `## Read Aloud` headings (`00:84`, `s01:99`, `r50:130`).
- `> > "…"` double-quote speech.
- `[!sidebar]` (`r25:64`) and `[!warning]`/`[!info]` (`s01:15`, `s01:74`).
- Missing from all six folders: a design-notes file.
- r03, r10 and r25 have no Read Aloud section at all.

**`00-first-meeting/ev-01-first-meeting.md`**
- **Trigger and tickets**
  - Fires when at least one Good-aligned party member gets the paper bird in **The Factions Come Calling**. Renaer's vouching is a prerequisite (:7).
  - The bird carries two tickets to *The Fall of Tiamat* (:26, and the guide at `02-harpers.md:37`).
- **Setting**
  - Lightsinger Theater is in the Castle Ward, a half-hour walk from Trollskull Alley (:20).
  - Delzorin Street tailor, free outfitting, fitting under an hour (:20).
  - *Tiamat* is "a recent dramatic work" about political will (:22).
- **Beats**
  - Mirt is already in Private Box C, half in shadow, watching the party and the stage (:32–36).
  - DC 12 Intelligence (Investigation) on the invitation: the sender "did not need to sign it" (:28).
  - DC 14 Wisdom (Insight): he is measuring them against unstated criteria (:36).
  - Intermission: he explains the Harpers (no guild, no government, no cell names, no first mission) (:44–54).
  - Banned topics: the Stone, Manshoon, the Cassalanters, the vault (:52).
  - Allowed topics: the Harpers, Renaer ("brief, genuine warmth"), and the theater's architecture "at greater length than warranted" (:46–50).
  - Acceptance: a silver harp-and-crescent pin is already in his hand (:58).
  - Decline: he refills his glass and leaves at the bell (:56).
  - Parting line either way: *"I am almost never home."* (:62)
- **Flag**: `Harpers Joined: True / False`, true if at least one party member accepted. Read by the Harpers Factions guide and by missions starting with **The Talking Mare** (:68–70).
- **Next Steps**
  - Renown 1, Watcher rank, and North Ward safe house access "through Remi Haventree" (:76).
  - Talking Mare is available at 2nd level (:76).
  - No Milestone line.
- **Problems**
  - Party-level accept/decline wording throughout.
  - `Remi` is named at :76, but `organizations/01-harpers.md:7` and `:23` hide her Harper identity until Mission 4.
  - Mirt's speech is stage-direction heavy: "(Chaotic Good, Illuskan human, he/him), the Old Wolf, a moneylender of prodigious girth who holds two offices no one openly names" (:32).

**`s01-the-cell-is-compromised/ev-01-the-cell-is-compromised.md`**
- **Trigger**: after **A Friend's House** is complete and the party has met Davil (:7).
- **Scene**
  - Mirt summons them to a rented North Ward room by a plain note, "Come alone. Be careful." (:34).
  - Cash, no ledger entry, sealed wine left unopened (:9, :36–38).
- **What he says**
  - The cell is compromised and the Splinter acted on Harper-only information.
  - He does not know who the double agent is. He has fourteen people who touched the leaked material (:48).
  - A GM warning says the name is the Mission 5 reveal (:15–16).
- **Incident table**
  - Gated on missions complete: M1 Shesstra Street address burned (:24), M2 Tessalar killed (:26), M4 Jelenn Urmbrusk query coached (:28).
  - Davil mentions the corroborating detail by accident (:30).
- **Checks**
  - DC 15 Charisma (Persuasion): "I know it's not you." (:54)
  - DC 13 Wisdom (Insight): Mirt has been working this longer than a tenday (:56).
  - Davil answers: "Starsong mentioned something that fit a gap." (:58)
- **Protocol** (:62–68)
  - Operational intelligence goes only to Mirt, in person.
  - Paper birds carry meeting times only.
  - Anything already told to another Harper contact gets reported to Mirt.
- **Leak rule** (:75)
  - A d4 is rolled behind the screen for any non-Mirt channel; on a 1, Kolat Towers receives it within two days.
  - Shared items are tracked as foreknowledge for **Kolat Towers**, and Corene's debrief can show Nihiloor already held the information.
- **Flag**: `Harper Leak Known: True`. The note at :75 says the flag is set in **The Sleeping Asset**, but the structure says s01 sets it. This is confused (:75 vs :81–83).
- **Next Steps**
  - Sleeping Asset becomes available at Renown 10 and 6th level, after A Friend's House (:89).
  - `#### Milestone: None` (:91).
- **Problems**
  - R1 (Manshoon knowledge gate) violations: "Manshoon's people" in the Gamemaster's Summary (:11), "Splinter" and "Kolat Towers" in :75, and "Manshoon's people" in :83.
  - The Persuasion check applies to "any character", which is party-level wording.

**`r03-harpshadow`** (`H:r03-harpshadow/ev-01-harpshadow.md`)
- **Trigger**: at the first natural pause after one party member's Harper renown reaches 3 (:7).
- **Content**
  - Mirt names the rank, "a readier ear and an extended network" (:10).
  - He hands over a folded paper with three unnamed ward contacts and an opening phrase (:11, :34):
    - chandler on Fillet Lane (Dock Ward);
    - map-seller off the Street of Silks (Trades Ward);
    - barber behind the Castle Ward Watch station (Castle Ward).
  - Each contact pulls street-level intelligence on one faction per tenday, and all three refresh in ten days.
  - He answers one question as the first use of his own channel.
  - Meeting location varies: coffee house, balcony, or the manor "when he actually is home" (:24).
- **Flag**: `Harpshadow Reached: True / False`, read by Brightcandle (:46–48).
- **Problems**
  - The rank's Appendix B "faction-rate pricing" is omitted.
  - The `[!profile]` block calls the contacts' use for personal matters a "short silence" (:42).

**`r10-brightcandle`** (`H:r10-brightcandle/ev-01-brightcandle.md`)
- **Trigger**: renown 10 (:7).
- **Meeting**: Mirt and Remi together (:9). Remi is shown openly with no Remi-reveal gate.
- **Benefits**
  - One potion of healing, or a cantrip/1st-level scroll, per mission via a Trades Ward apothecary. It needs 24 hours' notice and a verbal phrase on a folded note (:10, :19, :27).
  - One Harper Spy as backup once per quest, arriving within a day (:11, :33).
  - Remi builds the first persona. She asks three questions (grew up where, did what before Waterdeep, what trade could you pass for) (:45). The persona has cover name, documentation, clothes and two vouching contacts, and arrives in 3 days (:51).
- **Flag**: `Brightcandle Reached: True / False`. It is read by Wise Owl and by "Harper mission events that check rank prerequisites" (:61).
- **Problems**
  - Spy is treated as an unspecified Harper "operative".
  - `the Harper network's roster` (:21).
  - "If **A Friend's House** (m04) has not yet run" (:69) shows that the first draft assumed Brightcandle can precede m04.

**`r25-wise-owl`** (`H:r25-wise-owl/ev-01-wise-owl.md`)
- **Trigger**: renown 25 (:7). Mirt is home at the Sea Ward manor (:26).
- **Content**
  - One operational-cover service per quest (forged documents, coordinated distractions, or witnesses), routed through Remi. Ask for nothing needing more than 3 days (:11, :32–34).
  - Three embedded informants (Xanathar Guild, Sea Maidens Faire, Manshoon's Splinter), unnamed. One specific question each, DC 13 Charisma, failure means unavailable for two tendays (:12, :38–42).
  - Priority-target warning: Mirt hears within 24 hours (:13, :50).
  - Silver raven to Laeral; her reply note ends "Mirt speaks well." Mirt: "Don't bring her a problem you could solve on your own." (:52–62)
  - Remi's second persona arrives in 2 days (:14, :74).
  - The `[!sidebar]` on Laeral calls her "one of the Seven Sisters and a former Chosen of Mystra" (:66).
- **Flag**: `Wise Owl Reached: True / False`, "when Mirt hands the character Laeral's reply note" (:78–80).
- **Problems**
  - "a silver raven" (:54) is the manor routine here, versus `[!sidebar]`.
  - "Manshoon's Splinter" in the informant list is an R1 issue.

**`r50-high-harper`** (`H:r50-high-harper/ev-01-high-harper.md`)
- **Trigger and setting**
  - Mirt contacts the member "within a tenday" after renown 50 (:7).
  - Silver raven, wax seal, signet ring (:34). Meeting at 3rd hour of the evening watch, through the garden gate (:36).
  - Mirt's library, with Remi seated and Variel Duskwhisper (wood elf) as courier witness, "mandolin" (:44).
- **`[!design]` at :16**: "Expected in Dungeon of the Mad Mage". If **Vault of Dragons** has resolved, he "names the extraction and immunity options as the most practical remaining uses".
- **Benefits**
  - Archive access for the North (5 years of reports, current operatives excluded) (:28, :54).
  - A three-agent team for one operation, 2 days' notice (:26, :122).
  - Mirt's personal accompaniment on one mission (:58).
  - Covert extraction from anywhere in the city (:60).
  - A formal exposure request to the High Harpers (:60).
  - A third persona, which Remi hands over (:62).
- **The reveal** (:68–84)
  - "I'm a Masked Lord of Waterdeep."
  - "Laeral knows. She put me on the Lords' Council, years ago."
  - Remi "has known for years."
  - He has never told anyone in the field except Remi (:22, :72).
- **Offer** (:86–104)
  - One formal Masked Lord invocation (Watch cooperation, Lords' Court proceedings, or a warrant of immunity), now or held. Three-day effect (:98, :120).
  - If held, "worth more when you know what you need."
- **Flags**: `High Harper Reached: True / False` and `Masked Lord Request Invoked: True / False` (:108–114). Readers named: Vault of Dragons and Dungeon of the Mad Mage content.
- **Problems**
  - `Laeral ... put me on the Lords' Council` is unsourced.
  - A "third persona" is mentioned with no detail.
  - The "(the other three Masked Lords he trusts most have never been told he operates in the field)" line (:22) is another unsourced inference.

---

## 2. Previous (rejected) version: what it settled, what looks wrong

**Format and structure kept in the previous version**
- Ember block model throughout: `[!gamemaster]`, `[!readaloud]`, `[!social]`, `[!qna]`, `[!exploration]`.
- Headings: Hook, Background, scene sections, Renown Opportunities, Aftermath, Concluding the Event, Event Outcomes, Next Steps, Overview, Summary.
- Every folder has a `design-notes.md`.
- Per-member recording throughout. "Companions don't attend."
- "Milestone: None" is replaced by "awards no Milestone Points".

### KEEP list: named outcomes and readers

| Outcome | Set by | Read by | Notes |
|---|---|---|---|
| **Harpers Joined** | First Meeting, per character name | Harpers Factions Guide, Harper Faction Events starting with Talking Mare (`P:00/ev-01:366`) | Later acceptance recorded under same outcome. Left unmarked if everyone declines or no meeting (:366, :370). |
| **Harper Leak Known** | s01 (`P:s01:171`) | Sleeping Asset as awareness only (:171); referenced in Aftermath of r03 (`P:r03:135`), r10 (`P:r10:159`), r25 (`P:r25:214`), r50 (`P:r50:257`) | Awareness, not closure. |
| **Harper Private Protocol Adopted** | s01 (`P:s01:172`) | Sleeping Asset reads which channels were actually used; queued copies keep deadlines | New in previous version. |
| **Harper Mole Identified** | m05 (`P:m05/ev-01:387`), not in scope | Later Harper events | |
| **Harper Leak Closed** | m05 (`P:m05/ev-01:388`) | Referenced by s01 Fixed Leak Rule and r03/r10/r25/r50 Aftermath | Not set by s01 or any rank event. |
| **Harpshadow Reached** | r03, per recipient (`P:r03:143`) | Brightcandle (prior rank) | |
| **Brightcandle Reached** | r10, per recipient (`P:r10:167`) | Wise Owl and later missions | |
| **Wise Owl Reached** | r25, per member, on receiving Laeral's reply (`P:r25:222`) | High Harper and later quests | |
| **High Harper Reached** | r50, per recipient (`P:r50:265`) | Vault of Dragons and Undermountain | |
| **Masked Lord Request Invoked** | r50, with member's name, accepted request and delivery date only when Mirt accepts (`P:r50:266`) | Vault of Dragons; Mad Mage | Declined requests do not spend it (`P:r50:205`, `P:r50:225–241`). |
| **Remallia Harper Contact Known** | m04 (`P:m04/ev-01:306`, `P:m04/ev-03:180`) | r10, r25, r50 (decides who runs persona meetings) | Duplicate writer (see §6). |
| **Shesstra Street Reported**, **Handler Ledger Read** | m01 (`P:m01/ev-01:386`), m02 (`P:m02/ev-01:334`) | s01 incidents, r03 First Question | |

### KEEP list: facts, names, numbers

**First Meeting**
- Tickets and box seats follow the actual recruitment candidates: the unaffiliated characters Renaer recommended (`P:00:14`).
- Nobody is tested for alignment at the door (`P:00:14`).
- Companions attend the public performance only (`P:00:16`).
- Characters already in another faction get no offer (`P:00:14`).
- Timeline, an invention to accept or replace (`P:00:38–62`):
  - noon bird;
  - foyer 5 p.m.;
  - curtain 6:30;
  - intermission 7:15;
  - second-act bell 7:35;
  - final curtain 8:30;
  - recovery appointment the next evening.
- Benefits: Renown 1, Watcher, silver pin, mundane key, and address card for **12 Delzorin Street, North Ward**, a rented lodging with five bunks, water and a hearth (`P:00:312–314`).
- Remi maintains the lodging through intermediaries, unnamed. "She doesn't appear or sign a message until **A Friend's House**" (`P:00:314`).
- DC 12 Investigation (:42) and DC 14 Insight (:152) from the first draft are retained.
- Mirt is a Masked Lord and Laeral's advisor, and mentions neither (:158).

**Standalone (s01)**
- Orren Vale, a records-relay clerk, secretly supplies Manshoon's Splinter through Beldan Rusk (`P:s01:18`).
- The note arrives at 16:00; the meeting is at 19:00 in the third-floor front room of 6 Saerdoun Street, a North Ward tenement (`P:s01:14`).
- Four-incident priority list (`P:s01:26–33`): Salon inquiry (Jelenn), Customs-house inquiry (**Handler Ledger Read**), Shesstra Street inquiry (**Shesstra Street Reported** and residents still free), No recorded site inquiry (14 Saerdoun Street inspection at 18:00 three days later).
- Persuasion DC 15 and Insight DC 13 retained (`P:s01:99`).
- Next appointment at 09:00 two days later in the rear room of Seven Scales Counting House, 18 Sorn Street (`P:s01:129`).
- **Fixed Leak Rule**: every operational entry in Orren's register is copied to Rusk exactly 48 hours later. Private conversations with Mirt are not in the register. Nothing is rolled. Copies already delivered stay delivered (`P:s01:149–155`).
- The Orren/Rusk channel is separate from Corene's parasite and Nihiloor's intelligence, and never reaches Xanathar (`P:s01:155`).
- Mirt names Rusk only if the members identified him and shared the evidence. Otherwise "the recipient" (`P:s01:24`).
- R1 compliance: the Harpers know only that the Black Network has split. Davil believes Floxin leads it (`P:s01:24`).
- No renown, gold or Milestone (`P:s01:159`).

**r03**
- Hook: noon bird the day after the threshold; meeting at 20:00 at Mirt's manor; away members get the next evening after return (`P:r03:13`).
- Contacts (`P:r03:33`, :49–51):
  - Nella Fen, chandler, 16 Fillet Lane, Dock Ward (carts, waterfront);
  - Orin Dask, map-seller, 9 Street of Silks, Trades Ward (premises, cargo routes);
  - Bram Pell, barber, 3 Shield Street, Castle Ward (appointments, Watch routines).
- Opening phrase: "May I leave a receipt for the next delivery?" Contacts are available 09:00–17:00.
- One question per contact per recipient every 10 days, counted from that recipient's own use. Mirt's channel has its own separate 10-day count. Replies arrive sealed at noon the next day (`P:r03:41`, :73).
- Forgotten phrase: Mirt gives a written receipt at 09:00 the next morning, and no question is spent (`P:r03:83–93`).
- Faction rate: 90% of published price, rounded up to the next CP, only at these three suppliers, mundane stock only. This is a concretization of Appendix B's "faction-rate pricing" (`P:r03:77–81`, `P:r03-design-notes:11`).
- First Question: confirmed facts only. Branches on **Shesstra Street Reported**, **Handler Ledger Read**, an unverified Manshoon leader ("The Black Network has split, that much I know."), and an unestablished fact (`P:r03:97–127`).

**r10**
- Brightcandle meeting runs the same hook (20:00).
- Supplier: Evin Talver, Blue Bottle Apothecary, 24 Sorn Street, 09:00–18:00. One potion of healing or one cantrip/1st-level scroll per mission, 24 hours' notice (`P:r10:31–39`).
- Quarterly phrase table (blue / green / white / red "ledger is ready for copying"), with a 3-day grace period after the quarter turns (`P:r10:41`).
- Field operative: Perrin Valt, field name Reed, arrives exactly 24 hours after the request at a named surface point, or at the Yawning Portal if the job is below the city. Uses the 2024 Spy block. One per quest per member. Shared availability ledger with field names in order Reed, Ash, Elm, Briar, Willow, Alder (`P:r10:79–83`).
- Persona default: Vale & Reed Imports traveling order clerk, cover surname Varn, letter dated 3 months earlier, two deliveries confirmed in person by Nella Fen (candle order) and Orin Dask (map order). Player can change name and trade (`P:r10:107–111`).
- Persona packet arrives 3 days after the meeting (`P:r10:151`).
- Remi appears openly only after **Remallia Harper Contact Known**. Before that, Mirt relays and conceals (`P:r10:11`).

**r25**
- Cover service (3 days' notice, one per quest) in three fixed forms (`P:r25:39–47`):
  - Documents: Vale & Reed Imports letter, order and receipts.
  - Distraction: courier Harl Keen stages a broken cart for 10 minutes.
  - Witnesses: Nella and Orin give a counter appointment and later confirm it.
- Informants (`P:r25:91–98`):
  - Lantern, Dena Voss, Guild warehouse courier.
  - Canvas, Joss Bell, Faire ticket clerk (different person from Mara if she was recovered).
  - Slate, Darron Quill, Splinter cargo clerk, with no access to Manshoon's sanctum.
  - DC 13 Charisma, noon answer next day, failure means unavailable for 20 days (the "two tendays").
  - One answer per activation.
- Priority-target warning within 24 hours, covering detection and delivery together (`P:r25:136`).
- Laeral reply: raven sent at 20:15, reply at 21:00 with receipt code "Silver Raven Twenty-Five". It confirms a channel and spends no audience. An urgent audience is 10:00 two days after a specific danger-with-deadline request, in the Palace east reception room (`P:r25:148–168`).
- Second persona: default surname Dale, purchasing agent, 3-year trading history, guild associate Ilen Castor (licensed cartwright, 6 Shield Street) confirms by receipt number (`P:r25:170`).

**r50**
- Silver raven sent at noon the first day the member is in Waterdeep, appointment 20:00 that evening by the garden gate (`P:r50:15`).
- Variel Duskwhisper is a witness (`P:r50:21`). Instrument is a fiddle in the previous version versus a mandolin in the first draft. NF page and voice profile do not name the instrument.
- Archive: named topic, copies brought by Variel at 10:00 the next day for supervised reading, current embedded identities removed (`P:r50:51`).
- Third persona: surname Talar, senior purchasing agent (`P:r50:47–53`).
- Team of three Spies, 2 days' notice, surface point or Yawning Portal (`P:r50:79`, :87).
- Mirt accompanies once, meets at 09:00 the following day. If away, queue and the first 09:00 after return. Mirt keeps his CR 9 statistics (`P:r50:81–91`).
- Extraction: wagon and three Spies arrive 2 hours after the request. Courier order Harl Keen, Della Morn, Oswin Bell, then recipient-surname Tamsin (`P:r50:129`). Guarded locations: 30-minute attempt, withdraw, return 2 hours later. 20-minute drive (`P:r50:119–131`).
- Exposure: dossier the same evening, Laeral's office receipt via Variel at 10:00 three days later. It lists claims, corroborated facts and gaps, and verified crimes enter the Watch process (`P:r50:153–171`). Cassalanter suspicion never gives knowledge of the pact (`P:r50:159`).
- Masked Lord reveal: Mirt says "Laeral knows," and the previous version removed the claim that she appointed him (`P:r50-design-notes:7`). He does not name other Lords. Seat kept out of public accounts.
- Invocation forms with 3-day delivery (`P:r50:197–205`):
  - Watch cooperation: sealed instruction, liaison.
  - Lords' Court: docket receipt plus hearing at 10:00 the next day.
  - Warrant of immunity: sealed warrant plus Watch notice.
- Refusals before the use is spent (`P:r50:205`, :225–241): harm to the city, concealing an attack on uninvolved people, or authority beyond Waterdeep.
- Ally Power for Spies and Mirt is tier-adjusted (`P:r10:85`, `P:r50:93`).

### Things in the previous version that look wrong or risky

1. **Dangling reference**: `P:s01:14` says "the applicable evidence deadline below". No such section exists in the file.
2. **Spy and Mirt ally Power unverifiable**
   - Spy "22/17/15/8 at tiers 1/2/3/4" (`P:r10:85`), and three Spies 66/51/45/24 (`P:r50:93`).
   - `docs/plans/bregan-daerthe-mechanics-reference.md` and BD r10 (`BD:r10-officer/ev-01-officer.md:143`) define three CR 2.0 tiers (L1–4, L5–10, L11+) and a Spy at 17 / 15 for L5–10 / L11+.
   - Mirt at 110/85/70/55 and "HP 153, AC 16, CR 9" is cited as from "the mechanics reference", and none exists for Harpers. The setting page `notable-figures/harpers/01-mirt.md:6` says "Veteran (with modifications)". WDH holds Mirt by creature reference only.
3. **Mirt swears at a "business" meeting**: `P:r03:25` has "Fuck me, that was good work". The voice profile says "In business he doesn't swear at all, and the sudden absence of it is how people know he's serious" (`.claude/skills/character-voices/voices/harpers.md:17`). First meeting public mood swearing (`P:00:84`) is fine per profile; the r03 manor dinner is ambiguous.
4. **Faction rate ruling invented a number** (90%, round up to CP). Appendix B only says "faction-rate pricing at Harper-affiliated suppliers" (`Appendix_B:145`). Guide 02 `:59` omits the rate. This was a judgement call, not a source fact.
5. **Name and first-name collisions**
   - Oswin Bell (courier) vs. Chef Oswin Barr (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:103`).
   - Joss Bell (Canvas) and Oswin Bell share a surname.
   - Harl Keen vs. Constable Harl Pimm (BD s02, per `docs/plans/harpers-out-of-scope-notes.md:532`).
   - Tamsin fallback courier vs. Tamsin Orr (BD r03 cover name).
   - Bram Pell vs. Pell Harrowgate (BD r03).
   - Dena Voss vs. Hanna Voss (BD s01).
   - Orren **Vale** (mole) vs. Vale & Reed Imports (the cover firm that also produces personas and cover documents). Plausible fiction, but in the same page set.
   - Ilmra / Odalys / Ilsa collisions are noted for BD/DR in the out-of-scope notes (:558–562) and do not affect Harpers.
6. **Remallia gating**
   - Brightcandle's Remi-gating (`P:r10:11`) matches `organizations/01-harpers.md:7`, which says her identity is hidden until Mission 4.
   - The first-draft safe house line "through Remi Haventree" (`H:00:76`) contradicts it, and the previous version fixed that.
   - Duplicate setter: **Remallia Harper Contact Known** is set at both `P:m04/ev-01:306` and `P:m04/ev-03:180`.
   - Practical gate: base renown through m04 is 1+2+2+3+3 = 11, so Brightcandle at 10 normally arrives after the m04 salon. Remi's gate in r10 fires only if renown 10 is crossed earlier, for example through bonus renown.
7. **Sealed-wine dependency**: s01 keeps the wine sealed. The previous version retained it (`P:s01:43`, :133). The voice profile lists Mirt's refilling-glasses quirk, which makes the sealed bottle a deliberate signal. That is consistent.
8. **r50 reveal text**
   - The WDH Appendix B Mirt entry says "of all the Masked Lords, he is the least concerned with concealing his identity" (`adventure-wdh.json:32293`).
   - The remix instead has a secret reveal. Guide 02 `:62` and `player-factions-overview.md:55` hold the secret reveal. The Lords' Alliance rank text in WDH and Appendix B describes him openly as a Masked Lord (`adventure-wdh.json:1391`).
   - The previous version's line "Keep my seat out of public accounts" fits the remix, not WDH.
9. **Opera**: the previous version made it an opera sung in Giant with a printed Common libretto and invented timed scenes. WDH and Appendix B say an opera sung in Giant (`adventure-wdh.json:3834`, `Appendix_B:60`). The restored draft said "recent dramatic work".
10. **Tailor/foyer logistics** (45-minute fitting, 30-minute walks, 5:30 cutoff) are invented. They are consistent internally.
11. **Unverified invented content**: the ward-contact addresses, Shield Street, Sorn Street, Saerdoun Street and Fillet Lane numbers, `Silver Raven Twenty-Five`, quarterly phrase table, courier ordering, invention list.

---

## 3. Canonical source material

**WDH (`sources/adventure-wdh.json`)**
- **Joining** (`:3826–3842`)
  - "The Harpers approach good-aligned characters who show promise as spies. One such character receives the following message, written on a paper bird."
  - Invitation text: "Renaer tells us you are a good bet. He bought you tickets to the opera tonight at the Lightsinger Theater in the Sea Ward. If you are interested, meet Mirt at intermission. Private Box C. Formal attire is required for admittance." (:3831)
  - "Enclosed are tickets for the entire party to *The Fall of Tiamat*, an opera sung in Giant describing the evil dragon queen's defeat at the Well of Dragons." (:3834)
  - "If any of the characters join the Harpers, Mirt becomes their main Harper contact throughout the adventure." (:3841)
  - The theater "is a high-end establishment located in the Castle Ward" (:3842). The invitation says Sea Ward and this line says Castle Ward, a WDH inconsistency.
  - Mirt "describes the Harpers and offers membership to eligible characters. Characters who accept receive a silver pin of a harp within a crescent moon, along with their first mission (see the Harpers Missions table)." The manor is in the Sea Ward, "90 percent chance that Mirt isn't home" (:3842).
- **Harpers faction block** (`:1356–1374`)
  - "Any smart, non-evil character can join... Bards and wizards are especially welcome."
  - Harpers "suspect that the Zhentarim is wholly or partially responsible for the escalation of violence".
  - Gathering place: Ulbrinter Villa on Delzorin Street between Vhezoar Street and Brondar's Way, North Ward, just south of Trollskull Alley.
  - Remi is "high-ranking"; other key members are Renaer and Mirt.
  - Business conducted in "bustling inns... or in quiet locations such as the City of the Dead".
  - Support: potions and scrolls at reduced or deferred cost; Remi "feeds useful bits of information... might also offer them temporary shelter"; rescue team of a bard or mage plus 1d4+3 spies or veterans.
- **Mission table** (`:3855–3876`): M2 Maxeene (+1), M3 gazer bookshop (+1), M4 doppelganger (+2, 50 gp), M5 Haventree party (+2, 200 gp). Appendix B uses the same 1/1/2/2. Guide 02 raises these to 2/2/3/3 and adds M6 and M7.
- **Mattrim "Threestrings" Mereg** (`:1521–1526`): LG male Illuskan human bard; Harper spy at the Yawning Portal, three strings, "far more eloquent and composed than he lets on"; spies on Zhentarim agents; recently befriended Bonnie. He is a Harper agent, not Doom Raiders, per CLAUDE.md. Not mentioned in any scope file.
- **Mirt** (`:32279–32304`): Masked Lord, Harper, close advisor to Laeral; "survived the passing of centuries by means of magic"; "least concerned with concealing his identity"; widower of Asper; owns a Lord's ensemble worn only for official Masked Lord meetings. Mansion near the Naval Harbor in the Sea Ward (`:31013`).
- **Other Mirt uses**: Harpers with 4+ renown can get Mirt to free Fenerus (`:10628`) and learn Thorvin Twinbeard is a Harper informant (`:15161`). Mirt knows the Castle Ward sewer entry to Xanathar's lair (`:15159–15160`). These use "renown 4", which matches no remix rank (3/10/25/50).
- **Renown framework** (`:1170–1180`, :1272–1278): optional DMG renown rules; faction agent background rolls a d4 for starting renown; non-members start at 0 and can reach out to an influential NPC member when renown exceeds 0.
- **Renaer** (`:2974`): has Harpers "who can come to the characters' rescue" and can set up meetings with Mirt and Remi.

**Appendix B (`sources/Appendix_B_-_Player_Factions.md`)**
- Joining and first meeting: `:52–122`.
  - Tickets "for the entire party".
  - Lightsinger is in the Sea Ward.
  - Mirt's box description and speech (`:98–113`).
  - "Characters who accept membership receive a silver pin... pressed into their hand from his coat pocket, as if it was already there waiting." (:117)
  - "I should warn you that I am almost never home." / "You'll hear from us soon. The city doesn't give us much time to rest." (:120)
  - He "does not mention the Stone of Golorr, Manshoon, or the gang war's deeper origins. He is assessing, not briefing." (:115)
  - Warning: Harper compromise "is a feature of the campaign, not a problem to be resolved" (:47–48).
- Ranks (`:140–148`): Watcher 1 (safe house in the North Ward maintained by Remallia, pin), Harpshadow 3 (Mirt one question per tenday, faction-rate pricing), Brightcandle 10 (potion/scroll per mission, Spy as backup "once per arc"), Wise Owl 25 (Laeral audience, cover "per arc"), High Harper 50 (archives, 3 agents, Mirt accompanies).
- Renown actions (`:131–138`).
- Harper missions table: `:162–167`.
- Mirt: "He presents himself as a bluff, jovial sea merchant... a senior Harper, a Masked Lord, and a close confidant of Open Lord Laeral Silverhand" (:62). Remi: "A precise, guarded elf widow... lost her husband to political violence" (:64).

**Appendix C (`sources/Appendix_C_-_Player_Faction_Missions.md`)**
- `:19–21` Harper tone: "oblique briefings, information that arrives by trained bird".
- `:40` Mirt delivers a mission "at the Lightsinger Theater or via paper bird... depending on whether the party has attended the opera yet".
- `:94` Showing the silver pin or knowing the "Harper safe house location on Delzorin Street" demonstrates affiliation (to Maxeene).
- `:244–308` Doppelganger Assessment, with Mirt's hint that one of the five sold information about the party's Harper affiliation. This feeds the m03 leak thread.
- `:344` Remallia at the salon.
- `:385–387` Mirt's reaction to the Jarlaxle exposure.

**`3. Player Character Factions.pdf` (p. 24)**
- "The Harpers know that the Cassalanters are actually demon-worshippers and, if they realize the PCs have gotten tangled up with them, will quickly warn them." This conflicts with Cassalanter secrecy (§6).
- "The Harpers are more than happy to let the PCs keep the gold (although they will encourage them to 'do the right thing')."
- They want the Stone "which they believe contains vital intelligence that can help them in their struggle with the Abolethic Sovereignty".
- "The Harpers of Waterdeep are riddled with Zhentarim double-agents, and anything the Harpers learn about the PCs and their activities can very easily fall into Manshoon's hands."

**Source beats the drafts dropped or invented**
- **Dropped (source → drafts)**
  - Tickets for the whole party; individual tickets replace it.
  - First mission handed out at the pin (WDH `:3842`); both drafts hold it back for Talking Mare at level 2.
  - Mirt's "You'll hear from us soon" closing (Appendix B `:120`).
  - Harper support from WDH: potions and scrolls "at a reduced or deferred cost", and rescue teams of a bard or mage plus 1d4+3 spies or veterans.
  - Mirt's manor "90 percent chance he isn't home".
  - Renaer's role as a Harper member.
  - Appendix B's faction-rate pricing (dropped in first draft r03, concretized in previous).
  - Appendix B "once per arc" (guide 02 says "once per quest").
- **Invented**
  - Mirt as Masked Lord revealed at 50.
  - The extraction option.
  - The informants.
  - The persona benefit (the guide has it; the sources do not).
  - Appendix B names no Harper mission beyond M5.

---

## 4. Setting facts the events must match

**Harpers Factions Guide** (`campaign/guides/factions/02-harpers.md`)
- First Meeting summary: two tickets, Private Box C, Delzorin Street tailor, pin, "I am almost never home" (`:37`). Link at :39.
- Ranks table (:56–62):

| Renown | Rank | Guide benefit |
|---|---|---|
| 1 | Watcher | Friendly by default; pin; North Ward safe house "maintained by Remi" |
| 3 | Harpshadow | One direct question per tenday; Dock/Trades/Castle Ward contacts; each refreshes once per tenday |
| 10 | Brightcandle | Potion of healing/spell scroll per mission; one Spy backup once per quest; a Harper mentor teaches one persona |
| 25 | Wise Owl | Laeral audience if urgent; cover for one sensitive operation per quest; informants in Xanathar Guild, Sea Maidens Faire and Manshoon's Splinter (DC 13 Charisma, two tendays); second persona; 24-hour priority-target warning |
| 50 | High Harper | Archives; team of 3 for one operation; Mirt accompanies on one mission; Masked Lord reveal "if the party has not already worked it out" and one request; covert city-wide extraction; formal exposure request; third persona |

- Earning Renown (`:47–52`): +1 credible intelligence per faction per act; +1 expose Manshoon double-agent; +1 protect civilian; +2 identify Cassalanters as diabolists; +3 Stone; +1 refuse civilian harm.
- Missions (`:66–73`): Talking Mare L2 +2; Dead Drop L3 +2; Doppelganger Auditions L4 +3; A Friend's House L5 +3; Sleeping Asset L6 +4; Stone's Other Master L7 +4. Base total including the +1 join is 19. Wise Owl (25) and High Harper (50) need bonus renown or Mad Mage play.
- Infiltration (:19–22): "Information the party shares with Harper contacts can reach Kolat Towers."
- Guide hooks (:28, :30): "Mirt quietly tells a Harper character that the Cassalanters funded the Howling Hatred cult three years ago" (Fireball!); "informants can be activated against Xanathar and Manshoon outposts (Renown 30+)", which is a mismatch with Wise Owl at 25.
- Cross-references (:80–85): links to all six folders in scope.

**Organization page** (`setting/organizations/01-harpers.md`)
- Remi's identity is "hidden from PCs until Mission 4" (:7), "kept hidden... until she chooses to reveal it" (:23).
- Mirt is "Senior Harper, Masked Lord, and close confidant of Open Lord Laeral Silverhand" (:21). His manor is "theoretically available... almost never home".
- The Waterdeep cell is compromised (:19).
- Harpers want the Stone; "happily allow the PCs to keep Neverember's gold" (:38).
- R1 violation: "Manshoon's clone and his consolidation" (:17). Also flagged in `docs/plans/harpers-out-of-scope-notes.md:142`.

**Notable Figures** (`campaign/setting/notable-figures/harpers/`)
- **Mirt** (`01-mirt.md`)
  - Veteran with modifications.
  - Persona: "To those he trusts, he is a Masked Lord, a Harper, and Laeral Silverhand's closest advisor."
  - Widower (Asper). Architecture enthusiast.
  - "Moneylender whose personal loans carry the weight of a favor owed."
  - Trollskull Alley ev-04 shows a 500 gp Harper loan "repayable as a favor" (`ev-04:55`).
- **Remi** (`02-remallia-haventree.md`)
  - Sun elf noblewoman, Mage with modifications; widow of Arthagast Ulbrinter; runs Harper operations from a warded villa; silver raven figurine to message spies.
  - Featured in Trollskull Alley, Fireball!, A Friend's House.
- **Variel Duskwhisper** (`06-variel-duskwhisper.md`)
  - Wood elf bard and courier, neutral good. Touring musician cover. Passes one intelligence piece per tenday inside a tale.
  - "Background figure; no scripted appearance." Instrument unspecified.
- **Mattrim Mereg** (`03-mattrim-mereg.md`) and others: Bonnie, Corene Wyldath, Corvin & Nessa Vayle, Maxeene.

**Voice profiles** (`.claude/skills/character-voices/voices/harpers.md`)
- **Mirt** (:7–25)
  - Two gears: "Old Wolf" public rolling sentences; business gear short, complete, declarative, no swearing ("Sit. The first act is short.").
  - Swearing level: Punctuation · Artisan · Tirade (public only).
  - Calls younger people "lad" or "lass".
  - Quirks: refills glasses; tilts his head; talks architecture.
  - Signatures: "Sit." / "Eat something first." / "That's a debt, not a gift." / "I am almost never home."
  - Never: begs, flatters, uses a Harper code phrase in public, hurries.
- **Remi** (:29–43)
  - Never swears.
  - Pours the tea herself; touches the silver raven figurine.
  - Asks many questions framed as courtesies.
  - "Tell me about yourself; I like to know whom I'm feeding."
  - Authority by requests she never needs to command.
- **Variel** (:101–115): few words, long pauses, one drink, tunes the same string, "Hm.", delivers intelligence inside a tale.

---

## 5. How BD and DR handle the same event types

**Page model (both `BD` and `DR`)**
- `> [!gamemaster]**Gamemaster's Summary**` with bullets of what "the characters can" do.
- First Meeting: `#### Candidates and Companions` and `#### What Is Actually True` (BD) or `#### What Nobody in This Event Knows` (DR).
- Sections with `###` headings, `[!readaloud]`, `[!social]` NPC profile line (name, alignment, species, pronouns `::` description), "is happy to discuss the following topics" bullets, a closing "will not discuss" line, `[!qna]` blocks, `[!exploration]` check blocks, and `[!gamemaster]` rulings.
- Per-candidate answer scene: `### Each Candidate's Answer` / `#### Recording the Answers` (`BD:00:389–395`, `DR:00:300–306`).
- Benefits box (`**Initiate Benefits**` / `**Fang Benefits**`), a Concluding the Event section, `**Event Outcomes**` list and `**Next Steps**` with "This Event awards no Milestone Points".
- Closing `## Overview` and `## Summary` (Summary sections "After the Meeting" / "Without a Private Meeting", plus a "After a Report to the Watch" variant for BD).
- `design-notes.md` in every folder.

**First meeting rules**
- Individual membership: "Each candidate answers for themselves." Joining takes no check. A character already in another faction gets no offer. Companions can sit in but gain nothing.
- Outcome records the character's name.
  - **Doom Raiders Joined** (`DR:00:416`): "mark for each character who accepts... record the character's name... Companions and characters who joined another faction are not enrolled."
  - **Bregan D'aerthe Joined** (`BD:00:463`): same.
- Deferred or later acceptance is recorded under the same outcome (`DR:00:420`, `BD:00:417`).
- Rank 1 is recorded at joining: BD "Initiate"; DR "Fang"; benefits listed in a box.
- Secrets: no speaker names the hidden leader. BD uses "the captain" and "J.", and `Jarlaxle Unmasked` is a later per-member outcome. DR uses "the other cell/Floxin's cell/the Splinter", with a "If a Player Raises Manshoon" block.
- BD alone has a Watch-report severing branch. **BD Contact Severed** is per character.

**Rank events (BD r03/r50, DR r03)**
- **Trigger**: "when an individual member first reaches Renown N" (`BD:r03:5`, `DR:r03:5`). The meeting hook is delivered "at dawn on the second day" for BD (:15) and "at noon the day after" for DR (:13).
- **Away rule**: "A member who is away from Waterdeep finds the snake waiting at their first surface lodging on return" (DR:18); BD: playbill under the door on each of the next three dawns, then Kreb at the counter (:19).
- **Members-only**
  - "Companions who aren't members are not invited" (`BD:r03:17–18`).
  - Several qualifying members attend together and are recorded one by one (`BD:r03:17`, `DR:r03:18`).
- **Gating**: prior-rank outcome is the prerequisite (`DR` Wolf is read by Viper, `BD` Soldier is read by Officer). `BD:r50:17` adds "Hold this Event until **BD Commander** is marked for the member."
- **Mid-state variations on the speaker** (by outcome): BD swaps the speaker on **Kreb Unmasked** and **Zardoz Introduced** (`BD:r03:52–84`); DR swaps Davil for Tashlyn on **Davil Arrested**/**Davil Released** and moves the location (`DR:r03:15–16`).
- **Per-member tracking**: "Track separately for each member the date of the last news request, the nights used at the loft this tenday and any open goods order" (`DR:r03:244`); BD records last report request day, cover name, Faire visits and gp ordered (`BD:r03:335`).
- **Benefit procedure format**: contact, place, notice, how to order, limit, delay, who else, loss rule (`DR:r03:210–218`, `BD:r03:254–264`, :302–313).
- **Renown**: "The rank event awards no Renown." Next Steps say "This Event awards no Renown and no Milestone Points" (`BD:r03:317`, :346; `DR:r03:232`).
- **Renown loss**: a member whose Renown later falls below threshold keeps the rank, and the benefits are suspended (`BD:r03:48`; `BD:r50:500`).
- **Cross-faction secrecy**: Cassalanter pact never stated to a member unless **Cassalanter Pact Shared with BD** is marked (`BD:r03:36`, `BD:r50:27–31`).
- **BD r50 hold/answer window**: 10 days to answer, silence is refusal; the offer is recorded per member (`BD:r50:470–476`).
- **Ally Power** (CR 2.0 tier-adjusted) for allies who join combat (`BD:r50:353–370`, `BD:r10:143`).

---

## 6. Contradictions and recommended rulings

| # | Contradiction | Sources | Recommended ruling |
|---|---|---|---|
| 1 | **Tickets**: whole party vs. recruitment candidates only | WDH `:3834`, Appendix B `:60` vs. restored `00:26` (two tickets) vs. previous `P:00:14` | Individual membership (CLAUDE.md/R3). Previous version: one ticket per Renaer-recommended unaffiliated character. Companions get public admission only. |
| 2 | **Trigger**: "at least one Good-aligned party member" vs. per candidate | Restored `00:7` vs. DR `:15` model | Alignment sets only when the bird arrives; no test at the door. Per-character. |
| 3 | **Lightsinger ward**: Sea Ward vs. Castle Ward | WDH `:3831` and Appendix B `:60` say Sea Ward; WDH `:3842`, guide 02 `:37` and both drafts say Castle Ward | Pick Castle Ward (WDH body text, guide 02, both drafts, WDH is internally inconsistent). Keep. |
| 4 | **Opera**: "recent dramatic work" vs. opera in Giant | Restored `00:22` vs. WDH `:3834`, Appendix B `:60`, previous | Opera in Giant per source. Common libretto (previous version) is a reasonable accessibility device. |
| 5 | **First mission at the pin** | WDH `:3842` vs. both drafts and guide | Source says first mission handed over; remix says none ("This is an assessment, not a briefing," Appendix B `:115`). Keep remix: Talking Mare arrives at level 2 by its own event. |
| 6 | **Remi named at First Meeting vs. hidden until Mission 4** | Restored `00:76`, `r10:9` vs. `01-harpers.md:7/:23`, `player-factions-overview.md:154` | Remi stays hidden until the m04 salon. Gate her openly with **Remallia Harper Contact Known** as the previous version did (`P:r10:11`). Appendix B and the guide name her as safe-house maintainer, so the card says no name. Prefer a single setter in m04. |
| 7 | **Masked Lord secrecy**: WDH "least concerned with concealing his identity" vs. remix secret reveal at 50 | `adventure-wdh.json:32293` vs. `01-mirt.md:22`, guide 02 `:62` | Remix wins by design (guide 02 says "if the party has not already worked it out"). Keep the reveal at r50, but players who guessed it earlier should be allowed to say so (guide wording). |
| 8 | **"Laeral put me on the Lords' Council"** | Restored `r50:82` vs. previous `P:r50:179` ("Laeral knows") | Previous version: delete the appointment claim. Unsourced. |
| 9 | **Leak mechanic**: d4 random vs. fixed 48 hours | Restored `s01:75`; Appendix B `:47–48` "meaningful chance" vs. previous `P:s01:149–155` | Previous version is a settled design decision ("The old random leak chance is gone"). Keep fixed 48-hour copy until **Harper Leak Closed**. |
| 10 | **Who sets Harper Leak Known**: s01 vs. Sleeping Asset | Restored `s01:75` vs. `:81–83` | s01 sets it. Sleeping Asset reads it. Previous version split awareness (Known) from closure (Closed). |
| 11 | **Manshoon knowledge gate (R1)** | Restored `s01:11, :75, :83`, `r25:12`, guide 02 `:61` ("Manshoon's Splinter"), `01-harpers.md:17` ("Manshoon's clone") vs. R1 rule in `harpers-out-of-scope-notes.md:7` | Harpers know only that the Black Network has split. Use "the Splinter" / "the other cell" / "the recipient". Previous s01/r25 wording complies. Fix guide 02 and org page separately. |
| 12 | **Cassalanter secrecy (R2)** | PDF 3 p. 24 and Appendix B `:137` ("The Harpers are aware that the Cassalanters are Asmodeus cultists") vs. CLAUDE.md standing rule | CLAUDE.md wins. Harpers have suspicion only. The previous r50 exposure ruling (evidence enters the dossier only if the party discovered and reported it) is correct. Guide 02 `:28` ("funded the Howling Hatred cult") is a related risk, noted in `harpers-out-of-scope-notes.md:160`. |
| 13 | **Renown 30+ vs. rank 25** for informant activation | Guide 02 `:30` vs. `:61` | Wise Owl = 25 per the table. Fix the hook text separately. |
| 14 | **"Once per arc" vs. "once per quest"** | Appendix B `:146–147` vs. guide 02 `:60–61` | "Arc" is retired. Use per quest. |
| 15 | **Harpshadow benefits**: faction-rate pricing vs. ward contacts | Appendix B `:145` vs. guide 02 `:59` | Guide 02 wins on contacts. Faction-rate pricing was concretized in the previous version (90%). Accept the contacts; either keep the discount as a minor addition or drop it. No source fixes the rate. |
| 16 | **Brightcandle persona teacher**: "a Harper mentor" (guide) vs. Remi (restored, previous gate) | Guide 02 `:60` | Mentor is unnamed before the salon. Previous version's gate resolves this. |
| 17 | **Safe-house address**: unnamed (guide, Appendix B) vs. invented 12 Delzorin Street | `P:00:314` vs. WDH `:1363` (Ulbrinter Villa on Delzorin Street) and Appendix C `:94` ("Harper safe house location on Delzorin Street") | Appendix C supports a Delzorin Street safe house. But WDH puts Remi's own villa on Delzorin too, so previous version's rule that the lodging is "separate from her villa" needs a distinct number or block. Accept 12 Delzorin or replace with a different street. |
| 18 | **Mirt's stat block** | `01-mirt.md:6` Veteran vs. `P:r50:91–93` CR 9 / HP 153 / AC 16 | Unverifiable; no Harper mechanics reference. Resolve from the creature entry before use. |
| 19 | **Spy Power tiers** | `P:r10:85` four tiers vs. BD mechanics reference three tiers | Use BD's three CR 2.0 tiers. |
| 20 | **Variel's instrument**: mandolin (restored) vs. fiddle (previous) | `H:r50:44` vs. `P:r50:37` | No setting fact. NF/voice profile are silent, but "tunes the same string" (voice profile `:109`) works with either. Pick one. |
| 21 | **Renown path to 25/50** | Guide 02 `:66–73` (19 base) | Wise Owl needs about 6 bonus renown, High Harper needs Mad Mage play. Both are expected: r50 text "expected in Dungeon of the Mad Mage". |
| 22 | **s01 trigger** | Guide 02 `:11` ("after Mission 4") vs. `harpers-out-of-scope-notes.md:191` | s01 follows m04. Keep, and treat "met Davil" as a required condition that needs a writer (Doom Raiders First Meeting is not required for non-DR members). |
| 23 | **Harpers Joined legacy flag** | `trollskull-alley/ev-04-the-factions-come-calling.md:97–98` "At least one party member enrolled" (retired True/False) | The ev-04 writer needs updating. Out of scope here. Keep **Harpers Joined** as a per-character list. |
| 24 | **Jelenn / Jarlaxle references in s01 incident** | Previous `P:s01:28` uses Jelenn Urmbrusk and M4 | Jelenn is a Manshoon blackmail victim (`harpers-out-of-scope-notes.md:150`) and appears at L5. Fine as incident, but keep Manshoon out of speech (R1). |

---

## 7. Outcomes set and who reads them (grep)

**Restored first-commit files** (`H`)
- Only these files mention Harper outcomes: the six in scope plus `campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:97` (a retired `#### Harpers Joined: True / False` heading).
- No other restored campaign file reads `Harper Leak Known`, `Harpshadow Reached`, `Brightcandle Reached`, `Wise Owl Reached`, `High Harper Reached`, `Masked Lord Request Invoked`, `Remallia Harper Contact Known`, `Harper Mole Identified` or `Harper Leak Closed`.

**Previous version** (`P`): outcome names in scope are listed in §2. Cross-file readers inside the previous folder:
- `Harper Leak Known`: r03 `:135`, r10 `:159`, r25 `:214`, r50 `:257` (all "Aftermath").
- `Remallia Harper Contact Known`: r10 `:11`, r25 `:11`, r50 `:21`.
- `Shesstra Street Reported`: s01 incident 3 and r03 First Question.
- `Handler Ledger Read`: s01 incident 2 and r03 First Question.

**Outside readers named but not wired**
- `docs/plans/harpers-out-of-scope-notes.md:219–225`: none of the five unconverted lair docs uses a Harper outcome by name.
  - **Faction Outposts** should read Shesstra Street Reported, Nethpranter Safehouse Reported, BD Signal Site Observed and Erystian Profile Reported.
  - **Xanathar's Lair** should read Corene Rescued / Lost / Left in Place.
  - **Sea Maidens Faire** should read Jarlaxle Identity Exposed at Harper Salon and Erystian Profile Reported.
  - **Kolat Towers** should read Edric Report Delivered, Harper Leak Closed, Splinter Raid Observations Delivered and the s01 leak.
  - **Vault of Dragons** should read **High Harper Reached**, **Masked Lord Request Invoked** and Jalester Compromise Identified, with a level conflict (Harper M6 at L7 vs. 3-heist parties entering at L6).
- That file contains no Harper event-rewrite section. Sessions 38 and 39 (DR, BD) added theirs. The Harper rewrite has not been logged there.
- `session 33 handoff.md:98–167` logs open Harper questions: an invented outcome in M4, the Renown 30+ benefit (M5), a DC 12 Perception paraphrase (M4), "Harper Leak Known" as a new outcome name needing confirmation, the Renown-1 safe house vs. Remi's hidden identity, and the Sleeping Asset's missing exposure beat.
- `campaign/guides/gm-guide/player-factions-overview.md:55` reads the r50 reveal.
- `campaign/guides/factions/02-harpers.md:80–85` links all six folders.

---

## 8. Gaps and invention needed (not covered by any source)

- Every concrete address, price and named NPC in the previous version is invented. No source names Harper contacts besides Mirt, Remi, Mattrim, Bonnie and Renaer.
- No source defines persona mechanics, informant postings, extraction logistics, the archive, the "exposure" process, the Masked Lord invocation forms, or Mirt's role in the Lords' Court.
- Mirt's stat block for Harper events has no mechanics reference file.
- No source gives a Harper-specific equivalent to "Initiate/Fang" per-rank benefits beyond the guide's prose.
- The Remi-hidden-until-m04 rule has no first-meeting mechanism except the previous version's unnamed intermediary lodging.
- Orren Vale, Beldan Rusk, Tessalar and Seven Scales Counting House belong to rebuilt m02/m05 content and will need re-sync if those files change.
