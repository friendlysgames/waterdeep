# Emerald Enclave Conversion Brief (Session 43)

## Context

The user asked for the Emerald Enclave events to be rewritten the way the Harpers (Session 41) and Force Grey (Session 42) were: restore, research, plan, then draft on the DR/BD/Harper/FG page model.

**Inputs**
- **Rewrite input.** Every Enclave file is restored to its first commit (`b4bd3f6`).
- **Previous version** (fact source only): git `bc7655e`. A copy is at `/tmp/claude-0/-home-user-waterdeep/724ec0d3-1411-5aee-88ce-0e8b98de0e73/scratchpad/ee-prev/campaign/quests/faction-events/emerald-enclave/`. It is half converted. Only its settled facts survive; don't copy its structure or prose.
- **Approved plan:** `docs/plans/emerald-enclave-plan.md`.
- **Research reports** in `docs/plans/emerald-enclave-research/`:

  | File | Covers |
  |---|---|
  | `01-spec-and-structure.md` | Page model, R/PREV inventory, gates, the contact object, length targets (§1, §6) |
  | `02-first-meeting-s01-s02-ranks.md` | 00, s01, s02, r03–r50 (§3b, §4c–e, §5b–c, §6, §7, §11) |
  | `03-m01-m03.md` | M1–M3 (§3.2, §3.3, §3.4, §4, §5) |
  | `04-m04-m06.md` | M4–M6 (§4–§6, §7 stat values) |
  | `05-consistency-audit.md` | Outcome map, outside references, Melannor/Jeryth facts, collisions (§1, §2, §5–§8) |

Where a report lists options, this brief has already chosen. Where a report and this brief disagree, this brief wins.

## What went wrong with the restored and previous pages (avoid all of it)

**Format**
- Retired formats everywhere: `[GM]`, True/False flags, `Milestone: None`, `Milestone Overview`, `## Read Aloud` and "Arc E/J" labels.
- No Brief built from `[!social]` and `[!qna]`, and no `Who Knows What` block.
- Renown paid to "the party", with no base renown.
- Rank benefits written as flat lists instead of procedures.

**Rules and facts**
- Animal messages ran 39–70 words. The 2024 *Animal Messenger* allows 25.
- "Manshoon Splinter" appeared in 13 player-facing lines.
- Phaulkonmere was put in the Sea Ward.
- M5 and s02 ran a second intellect-devourer programme.
- Rules errors: "Dazed", the charm texts, *Fabricate*, the Giant Eagle as a Beast, cranium rats, Ambrose as a "Paladin", and the Chuul "Stuns".
- M2's crypt interior contradicts WDH and arc-j.
- M4 and M5 named Faction Outposts (L4) as their reader, after it has already run.

## User decisions (Session 43)

1. **Bonnie.**
   - The Enclave makes the doppelganger crew leave Waterdeep, Bonnie included.
   - The exception: if **Bonnie Harper Operative** is marked, the party can convince the Enclave that Bonnie is not a threat, and she stays.
   - (User: "Bonnie is made to leave, unless she has been made a Harper, in which case the party can convince the Enclave that she's not a threat".)
2. **M6 follows the Force Grey precedent.**
   - It runs at 7th level, after Kolat Towers.
   - Parties that run three heists play it after the Vault, and the Vault does not treat it as a prerequisite.
   - arc-j:47's Jeryth-readiness reader gets an "if not run" default, logged for the Vault conversion.
3. **Kelso is a middleman.**
   - Edric sold the crew's names to Kelso Fiddlewick, who sells to whoever pays.
   - GM text says the Splinter was Kelso's customer. Kelso never names his customers, which matches DR M3.
   - Beldan Rusk stays Harper M3's handler. Kelso's runners may carry paper to Rusk's Nethpranter Street house, but only in GM text.
4. **The renovation help is druid craft plus timber.**
   - The Enclave's 250 gp of Trollskull renovation is delivered by Enclave druids using *Mold Earth*, *Shape Water*, *Plant Growth* and *Stone Shape*, plus donated timber.
   - It is a party-level box at the end of the First Meeting.
   - The oak-tree ask from the manor guide stays: leave the oak undisturbed, and allow silverbark growth.
   - Trollskull ev-04:57 and `trollskull-manor/02-operating-costs.md:82` are corrected in the companion pass.

## Standing defaults

**Secrets**
- **Manshoon.** Use the DR/Harper/FG **Manshoon Named** gate (written by **Faction Outposts**, unconverted).
  - Until it is marked for a member, speakers say "the Splinter" or "the other cell".
  - Overview and Involved Characters labels say "the Splinter". GM text may state the truth.
  - Phaulkonmere is one block south of Kolat Towers (WDH). Nobody points at the towers or says what they are before the gate.
- **Cassalanters.** Suspicion only. No Enclave speaker knows of the pact.
  - The dying-herbs-and-leaving-birds imagery belongs to the Cassalanter hook, so the Enclave missions don't use it.
  - M5's sign is dead beds and a film on the water. M6's sign is plants growing without direction.
- **Jarlaxle.** Nobody in the Enclave set names Jarlaxle, Zardoz Zord or Bregan D'aerthe to players. Sarna Dath says "the carnival fleet" and "the *Eyecatcher*'s crew".
- **Illuun.**
  - Jeryth never names it before M6. Her words are "old, patient and hungry" (s02), and only s02 uses "hungry".
  - The name reaches a member only through **Illuun Contact** or **Anchor Destroyed**, or if the Stone named it at Full Awakening.
  - Mirt never names it. Harper M6 is untouched.
- **The gold.** The Enclave takes no side. The line "That question is for the Lords to settle." is **Jeryth's** (voice doc). It is a public position, so asking it needs no check.

**Membership**
- **Candidates.** Every character in no other faction is a candidate and answers for themselves.
  - Trollskull ev-04's "nature-aligned" note only decides whom the cat finds first.
  - A character already in another faction gets no offer, and Melannor says so in one qna answer.
- **No Offer Closed outcome.** The gate stays open, and a candidate who defers can come back. Melannor repeats the offer in a few sentences.
- **Members only.**
  - Briefs, debriefs, renown, ranks and benefits belong to individual Enclave members. Companions help with everything else and earn no renown.
  - Every gate reads "becomes available when an individual Emerald Enclave member reaches Renown N and Nth level".
  - Briefs and debriefs at Phaulkonmere: companions wait at the gate or in the outer garden.
- **Party-wide gifts are deliberate.**
  - The *charm of heroism* (M4) goes to each character who fought the grells, member or not.
  - The Phaulkonmere Ward (M6) is a group artifact.
  - The *charm of vitality* (r50) goes to each character present.
  - Say this in GM text, as BD m04 does for its statuette.
- **Response teams** never enter Phaulkonmere or fight inside its walls. They may watch the street.

**Melannor Fellbranch**
- **Stat line:** Neutral Good, Half-Elf, he/him.
  - Druid block, with WDH's traits: Advantage against Charmed, can't be magically put to sleep, Darkvision 60 ft, Common and Elvish.
  - WDH says Chaotic Good. The campaign keeps Neutral Good, and a design note records the change.
- **Voice** (`voices/emerald-enclave.md`):
  - friendly but humourless, plain, even;
  - no contractions, no jokes, never swears;
  - uses his signature lines where they fit: "The soil is uneasy." and "That is not humorous.";
  - calls his brother "Talisolvanar", never "Tally".
- **Tally.** The First Meeting pays off Trollskull ev-03:20 with one Melannor line asking after "Talisolvanar".
- **In person.** He comes in person in M4 (the deliberate break), r10 and M6. s02 Surge One refers to the Fireball! debrief instead of staging a second visit. Never write "for the first time".

**Jeryth Phaulkon**
- **Stat line:** Neutral Good, Chosen of Mielikki, she/her, a disembodied presence in Phaulkonmere's gardens.
- **How long she has been there:** "several years" (Appendix B), never "decades".
- **Voice:**
  - one or two short sentences per turn, spaced far apart;
  - never repeats or explains herself;
  - no mortal politics, and never swears;
  - signature lines: "Something dreams below.", "That question is for the Lords to settle." and "Rest here.";
  - calls Mielikki "the Lady of the Forest".
- She does not dispatch missions. The animals carry Melannor's words, and the urgency is his.

**The contact object: the *Animal Messenger***
- **What it is.** Every Enclave contact is Melannor's *Animal Messenger*.
  - A Tiny Beast finds the recipient by description, speaks the message once in Melannor's low baritone "from somewhere behind its eyes", and leaves.
  - Every message is **25 words or fewer, counted.** The main session will count every one.
  - Others nearby hear it. It carries no reply unless the message asks the recipient to answer, and then the Beast waits for up to 25 words.
- **Stat blocks.** Use the Raven block for crows, pigeons, doves and songbirds, and the Hawk block for falcons. The Cat and Owl are as written. No pigeon, gull or cranium rat block exists.
- **The animal for each event:**

  | Event | Animal |
  |---|---|
  | First Meeting | white cat |
  | s01 | white cat |
  | M1 | grey pigeon |
  | r03 | grey pigeon |
  | M2 | crow |
  | M3 | falcon |
  | M4 | Melannor in person |
  | M5 | crow at dawn |
  | M6 | Melannor in the garden |
  | r10 | Melannor at the door |
  | r25 | owl at dusk |
  | r50 | three animals at once, with no words |

- **The First Meeting message** keeps WDH's question. Suggested text (21 words), to be counted when drafted: "Interested in joining the Emerald Enclave? Come meet us at Phaulkonmere in the Southern Ward. The gate will be open."
- **Phaulkonmere's constants**, written once per event in the arrival readaloud:
  - The gate stands open before they arrive.
  - The garden is older than the street around it.
  - Jeryth's voice has no source.
  - The oldest oak is the point of reference.
- **s01's east gate key** gives entry at any hour. It is personal and never lent.

**Rules**
- **2024 rules and names only.** Use Knight, never "Paladin"; Warrior Veteran, never "Veteran"; no Thug.
  - Every roster comes from `docs/plans/emerald-enclave-mechanics-reference.md`.
  - Checks read "**DC N Ability (Skill)**" with a stated fallback. No single check settles a mission.
  - Fights go in `[!hazard]` with `#### X's Tactics`, an end or retreat condition, and a non-combat route.
- **No "Dazed".**
  - M5's exposure: Poisoned until a Short Rest.
  - M6's entry save: Incapacitated until the end of the character's next turn.
- **Charms** (2024 DMG p. 99):
  - *charm of restoration*: 3 charges; *lesser restoration* costs 1 and *greater restoration* costs 2. The charm vanishes when the charges are spent.
  - *charm of heroism*: a Magic action gives the benefit of a *potion of heroism*, then the charm vanishes.
  - *charm of vitality*: a Magic action gives the benefit of a *potion of vitality*, then the charm vanishes.
- **No intellect devourers in the Enclave set.** Nihiloor owns that programme (Harper reference §5; FG M4). M5's waste is residue from the Splinter's thrall-conditioning, the alchemy that keeps the Splinter's mind-controlled servants docile.
- **Undermountain rule for r50.**
  - Teleportation, *plane shift* and *word of recall* fail in Undermountain.
  - Spells can't reshape its walls, floors or ceilings.
  - *Sending* never reaches Halaster.
  - Beasts can't cross between levels except on foot.
  - *Control Weather* needs the outdoors.
- **Calendar.** Give spans in tendays. Bonnie's grace period is two tendays.

**Geography**
- Phaulkonmere is in the **Southern Ward**.
- **Gerrick's tunnel** is brick-lined. It runs **west** from the southern Undercliff terraces to the Castle Ward cistern access. Undercliff lies east of the city (WDH).
  - Drop "Trollgate", which is invented and not in WDH. The outlet is "below the southern terraces, where the cliff path meets the city wall".
  - It was sealed six years ago, after something came up through it. That was a chuul scout from Illuun's brood, which Gerrick's neighbours drove back with fire. Gerrick never learned what it was, and M6 pays it off.
- **Kelso** is in the Field Ward. He uses the Wererat block, as in DR M3 and OotG M3.

**Renames (collisions)**

| Old | New | Collides with |
|---|---|---|
| Gerrick Goodbarrel (M1, M5) | **Gerrick Thatchley** | Marda Goodbarrel (DR M3); Gerrick stays as the first name |
| Raeve Solnath (M5) | **Imre Daskov** | Vira Solkan (FG M6) |

Edric Tanner is Harper M3's traitor, and the Enclave uses the same doppelganger. The crew is Bonnie, Edric, Kael, Syla and the Scholar (Harper M3). Kept invented names: Mirsa (seamstress), Sarna Dath (south-quay fisher, blue-and-white boat), Bertio Caskwall (s02 ward-seal). New invented minor NPCs are listed in each folder's design notes under "Invented Names and Open Items".

## Gates and renown (shared ladder)

| Mission | Gate | Base | `+1` bonuses (each once, each tied to a named condition) |
|---|---|---|---|
| M1 | joining, 2nd level | 2 | all three scarecrows destroyed before more livestock or people are hurt; the testing-site page reported to Melannor; no farm burned (**Farm Damaged by Fire** unmarked) |
| M2 | Renown 3, 3rd level | 2 | pattern documented and reported to Melannor and Ambrose before night ten; all ten nights held with no bones taken; Ambrose asked about the crypt rather than told |
| M3 | Renown 5, 4th level | 3 | traitor identified and Kelso named; Bonnie leaves or stays without violence, as the outcome falls; Bonnie handles Edric herself |
| M4 | Renown 8, 5th level | 3 | Mirsa rescued before a grell escapes; both grells destroyed; Pier 17 reported to Melannor and the Watch |
| M5 | Renown 10, 6th level | 4 | cache destroyed before a cultist reports; logbook decoded and Imre Daskov named; a cultist taken alive and questioned |
| M6 | Renown 13, 7th level, after Kolat Towers | 4 | anchor destroyed with both chuul beaten or driven off; the contact reported to Melannor in full; finished inside Jeryth's 48 hours |

The base-only path reaches every gate: 1 → 3 → 5 → 8 → 11 → 15 → 19. s01 and r03 fire together at Renown 3.

## Event Outcomes (one writer each; mark with the member's name where individual)

| Outcome | Writer | Readers |
|---|---|---|
| **Emerald Enclave Joined** | 00 | Factions Guide; every Enclave event; Trollskull ev-04 (outside, logged); BD s04 (reads the event "Emerald Enclave First Meeting") |
| **Splinter Site Reported** | M1 | r03 (the network's Undercliff line); **Faction Outposts** (unconverted, logged) |
| **Farm Damaged by Fire** | M1 | M5 (Gerrick's tone) |
| **Drainage Tunnel Learned** | M1 | M5 (the first of three routes); M6 |
| **Pattern Documented** | M2 ev-01 | M2 ev-02 (Ambrose names the crypt unasked) |
| **Bones Kept Safe** | M2 ev-01 | M2 ev-02 (the 100 gp) |
| **Jeryth's Message Received** | M2 ev-01 | M6 brief; **Vault of Dragons** (unconverted) |
| **Brandath Crypts Visited** | M2 ev-02, per member | **Vault of Dragons** (unconverted; Ambrose waves the party through, arc-j:83) |
| **Traitor Identified** | M3 | **DR M3** (`ev-01:285`, exact name); **Faction Outposts** (unconverted) |
| **Doppelgangers Departed** | M3 | Harper M3 (outside, logged); Force Grey M3 and M4 (outside, logged) |
| **Bonnie Departed** | M3 (at the end of the grace period) | Harper M3, Force Grey M3 ev-01, Force Grey M4 ev-02 (all three outside, companion pass) |
| **Mirsa Rescued** | M4 ev-02 | M5 brief (one line) |
| **Grell Escaped** | M4 ev-02 | M4 ev-02 Aftermath; r10 (the Dock Ward route) |
| **Pier 17 Investigated** | M4 ev-02 | **Xanathar's Lair** (unconverted; a casing aid at X4 if the lair has not run) |
| **Cache Destroyed** | M5 | M6 Background |
| **Imre Identified** | M5 | **Kolat Towers** (unconverted) |
| **Cultists Escaped** | M5 | **Vault of Dragons** (unconverted; Watch cooperation in the Trades Ward) |
| **Anchor Destroyed** | M6 ev-02 | r50; **Vault of Dragons** (unconverted, arc-j:47) |
| **Illuun Contact** | M6 ev-02, per character | r50; **Vault of Dragons** (unconverted); Dungeon of the Mad Mage |
| **East Gate Key Held** | s01, per member | r03 (the haven procedure) |
| **Fouled Channel Requested** | s02 Surge Four, per member | M5 brief (Melannor: "as Jeryth asked") |
| **Silence Warning Given** | s02 Surge Five, per member | M6 brief |
| **Summerstrider Reached** | r03 | r10 |
| **Autumnreaver Reached** | r10 | r25 |
| **Winterstalker Reached** | r25 | r50 |
| **Master of the Wild Reached**, **Illuun Watch Accepted** | r50 | Dungeon of the Mad Mage |

**Doppelgangers Departed** and **Bonnie Departed** are separate on purpose. The four other doppelgangers leave whenever the Enclave's demand stands. Bonnie leaves only if the reprieve isn't won.

**Read but not written here**
- **Manshoon Named** (Faction Outposts).
- **Harper M3 Complete** (Harper M3). It is world state: Edric is out of the crew.
- **Bonnie Harper Operative** (Harper M3).
- **Pool Destroyed** (FG M4). M5 may mention it for one line, and it doesn't change the waste.

**Dropped:** Scarecrows Cleared, Bonnie's Method Honored, Undermountain Commission Accepted (the name collides with Lords' Alliance r50), Raeve Identified (renamed). Fold their effects into scene text.

## Per-folder briefs

Each drafter reads its report sections first. These instructions win over the report.

### 00 First Meeting (ev-01 "Emerald Enclave First Meeting", design-notes). Report 02 §3, §4c–e; report 01 §6.2
- **Title.** The H1 is `# Emerald Enclave First Meeting`, because BD s04 and Trollskull read that name.
- **Summary**
  - `#### Candidates and Companions` and `#### What Is Actually True`, as in the Harper and FG First Meetings.
  - What Is Actually True:
    - Jeryth decided before the party arrived.
    - The offer has no hidden price.
    - The Enclave has no stake in the gold.
    - Jeryth has felt a dreaming presence for months and doesn't know its name.
    - Nobody names the Splinter's master or the Cassalanters.
- **Scenes**
  - **The White Cat.** It arrives one morning during the renovation, with the counted message.
  - **The Open Gate.** The Southern Ward, Phaulkonmere's constants, and Melannor at the gate. Melannor asks after Talisolvanar.
  - **The Walk with Melannor.**
    - His social block and 6–8 qna, with no filler: what the Enclave is for; the beholder and the aberrant stir; why us; the gold (the qna answer is Jeryth's line, relayed or heard); what members get; other factions.
    - **Will not discuss:** the Stone, the vault, the dreaming thing's name, the Splinter's master, the house one block north.
  - **Jeryth's Voice.** Her social block and 3–4 qna, each answered in one or two sentences.
  - **Each Candidate's Answer.** Accept and decline readalouds, then a **Springwarden Benefits** box per member:
    - Renown 1;
    - the *charm of restoration*, with its 3 charges as a procedure;
    - the Phaulkonmere haven as a procedure: who may enter, the hours, what it gives, what it doesn't, and the response-team rule.
  - **Leaving Phaulkonmere.** The party-level renovation box (decision 4), and Melannor's "I'll be in touch."
- **No first mission is handed over.** M1 comes by its own pigeon.
- **Summary page:** "After the Meeting" and "Without a Private Meeting" variants.

### M1 The Undercliff Scarecrows (overview, ev-01, design-notes). Report 03 §3.2
- **Structure:** one event. Scenes:
  - The Brief (the pigeon; at Phaulkonmere if a member goes);
  - The Undercliff;
  - Gerrick;
  - The Three Scarecrows;
  - The Testing Site;
  - The Sealed Tunnel;
  - Debrief at Phaulkonmere.
- **Three Clue Rule.** Each beat has three routes:
  - **The territories:** Gerrick; DC 14 Wisdom (Survival) on the tracks; the animals (a horse facing north and stalled sheep), read by *Speak with Animals* or DC 11 Wisdom (Animal Handling).
  - **The site:** Gerrick's aside; DC 13 Intelligence (Investigation) in the north fields; the Sackcloth One's range.
  - **The tunnel:** Gerrick; Melannor knows the Undercliff drains; the outlet is visible in the Blanket's territory.
- **The scarecrows.**
  - Keep the Sackcloth One, the Pumpkin Head and the Blanket, and their habits.
  - They are fought one territory at a time; the hazard text says why (two at once can Paralyze and then crit).
  - Fire works, because the 2024 Scarecrow is vulnerable to fire. A fire clock in the dry fields can burn a farm, which marks **Farm Damaged by Fire**.
- **The site.**
  - The chalk circle, about eight feet across.
  - The journal page: "All three activated simultaneously, unexpected — departed before they could reorient."
  - The arcanist is "the Splinter" in every player-facing line.
- **Gerrick Thatchley** is a halfling farmer of about fifty, thirty years on the land. He swears freely at the Guard.
  - His tunnel is unconditional (a departure from Appendix C, noted in the design notes).
  - His tone reads **Farm Damaged by Fire** only in M5.
- **Renown:** see the ladder table.

### M2 Ten Nights in the City of the Dead (overview, ev-01 The Ten Nights, ev-02 The Final Dawn, design-notes). Report 03 §3.3
- **Delete `ev-02-brandath-crypt-revelation.md`** and write `ev-02-the-final-dawn.md`. Keep `ev-01-the-ten-nights.md`.
- **ev-01 The Ten Nights**
  - The Brief: the crow, and Jeryth's "go", relayed by Melannor.
  - **Sir Ambrose Everdawn.** Lawful Neutral, Tethyrian Human, he/him, Knight block. About sixty, a silver gauntlet pin of Kelemvor, fifteen years in the cemetery.
    - No contractions.
    - He never offers crypt knowledge unasked.
  - The party patrols the north and Ambrose takes the south (Appendix C; WDH has it reversed, noted in the design notes).
  - **The nightly procedure.** Where the party stands, how it splits across the mausoleums, and the two Watch officers.
  - **Fixed skeleton nights: 4, 6 and 8.**
    - One skeleton per character, up to five.
    - At five characters a sixth comes on night 8 only.
    - The skeletons walk the same path from the northeast toward the Brandath crypt, linger one round at the treant's grove edge, and turn back.
  - **The pattern** has three independent routes: the skeletons' path, Ambrose's reports, and the Watch officers' log.
  - **Jeryth's reply**, relayed after three hours of silence: "Tell me if anything below answers."
  - Marks **Pattern Documented**, **Bones Kept Safe** and **Jeryth's Message Received**.
  - Nothing is awarded here. Continue with **The Final Dawn**.
- **ev-02 The Final Dawn**
  - **The tenth dawn.** If **Pattern Documented** is marked, Ambrose names the crypt unasked (the report counts as asking). If not, he names it only when asked.
  - **The Brandath grounds, exterior only:**
    - the sealed doors with BRANDATH over them;
    - the containment-warding residue, DC 13 Intelligence (Arcana);
    - the treant, which watches and does not move for people on the path;
    - nothing opened.
    - The glyph and the interior belong to the Vault. GM text says so in one line.
  - **Debrief at Phaulkonmere.** 100 gp to every character who stood all ten nights, member or not. Mission Renown is awarded here. Marks **Brandath Crypts Visited** per member.

### M3 The Doppelganger Problem (overview, ev-01, design-notes). Report 03 §3.4, §4; decision 1, decision 3
- **Structure:** one event.
- **Who Knows What**
  - Bonnie's crew is the Harper M3 crew: a Tethyrian barmaid form, in Waterdeep over a year.
  - Edric Tanner is the traitor, and "Right," is his tic.
  - The Enclave learned what Bonnie is through its animals. Mattrim isn't the only one who knows, which goes in the out-of-scope log.
  - If **Harper M3 Complete** is marked, Edric is already out of the crew.
- **Scenes**
  - **The Brief.** The falcon, then Melannor at Phaulkonmere. The Enclave's demand: the crew leaves Waterdeep, "peacefully, if possible".
  - **The Portal.** Getting to Bonnie: openly, through Durnan ("Back room's free."), or through the crew.
  - **The Back Room.** After closing. Bonnie never talks about what she is in the taproom.
  - **The Traitor.** Three routes:
    - DC 14 Wisdom (Insight) on Edric's objections;
    - Bonnie's payment trail, if the party engages honestly;
    - the Enclave's animals saw Edric hand paper to a Shard Shunner runner.
    - Bonnie: "He's the one who sold your names." Then she names Kelso as the buyer (decision 3).
  - **The Departure.**
    - **Default:** the crew agrees to go within two tendays. Mark **Doppelgangers Departed**, and **Bonnie Departed** when the grace period ends.
    - **If Bonnie Harper Operative is marked:** the party can argue her case to Melannor. It takes DC 15 Charisma (Persuasion), with Advantage if a member vouches for her Harper terms. On a success, the four others still go and Bonnie stays. Mark **Doppelgangers Departed** only.
    - **If the party sides with Edric:** DC 18, and no Kelso.
    - **If steel is drawn on Bonnie:** she shifts and leaves, and the mission fails.
  - **The Receipt.** The dove with three dots in a triangle, three days later. Melannor: "It is, in its way, a receipt."
- **Grace-period rule** (GM text):
  - If Harper M3 runs inside the two tendays, it can still mark **Bonnie Harper Operative**, and the party can go back to Melannor for the reprieve.
  - After **Bonnie Departed**, Harper M3 is unavailable, and Force Grey M3/M4 use their absence branches (companion pass).
- **No combat expected.** Edric's flee and surrender rules come from the mechanics reference.

### M4 The Grells in the Dock Ward (overview, ev-01 The Search, ev-02 The Nest, design-notes). Report 04 §4
- **Delete `ev-01-the-grells-in-the-dock-ward.md`** and write `ev-01-the-search.md` and `ev-02-the-nest.md`.
- **Premise.** Guild excavation under the harbor disturbed the grells, and the Guild uses the disruption as cover. Three citizens are gone over three nights, and Mirsa is the third.
- **ev-01 The Search**
  - Melannor comes in person to Trollskull Manor. This is the deliberate break from the animals.
  - Three leads to the south-quay warehouse:
    - DC 14 Intelligence (Investigation) on the disappearances;
    - DC 14 Wisdom (Survival) on the ozone and the missing cats;
    - the Summerstrider network's Dock Ward report, or Melannor's sketch.
  - Nothing is awarded. Continue with **The Nest**.
- **ev-02 The Nest**
  - The warehouse has a 30-ft ceiling and loading doors.
  - Two Grells, with rosters per party size from the mechanics reference.
  - Mirsa is freed with an action and DC 12 Strength (Athletics), or DC 14 with a grell within 5 ft.
  - A grell at half hit points flees through the loading doors.
  - Then the return to Phaulkonmere:
    - Jeryth gives the *charm of heroism* to each character who fought.
    - Mirsa's account of Pier 17: two dockhands paid to leave, and a well-dressed third man.
    - The choice of whom to tell: Melannor only, Melannor and the Watch, or nobody.
  - Writes **Mirsa Rescued**, **Grell Escaped** and **Pier 17 Investigated**.
  - **Grell Escaped** consequence (GM-only): Melannor reports two days later that it went under the south quay.

### M5 The Fouled Channel (overview, ev-01, design-notes). Report 04 §5
- **Structure:** one event. Scenes:
  - The Brief: a crow at dawn, then Phaulkonmere's dead beds, with one patch bigger each morning and working west to east.
  - **Three Ways Down:**
    - Gerrick's tunnel, if **Drainage Tunnel Learned** is marked; otherwise Gerrick, found again;
    - Melannor reads the dead edge's direction, DC 13 Intelligence (Nature);
    - the Summerstrider well reports from the Trades Ward.
  - **The Channel.** The iridescent film. Exposure for 10 minutes or more calls for a DC 12 Constitution saving throw. On a failure the character is Poisoned until a Short Rest.
  - **The Cache.** Six vessels and the oilskin logbook. DC 14 Intelligence (Investigation) decodes it and names **Imre Daskov**.
  - **The Cultists.**
    - They arrive at a fixed time, as the party works the cache.
    - Roster from the mechanics reference: a Cultist Fanatic with Tough guards, who run when the Fanatic falls.
    - DC 14 Dexterity, or any holding spell, takes one alive. A captive knows only the delivery task.
  - **The Cutting.** Melannor's herb cutting and Jeryth's ten minutes in the water. The water answers with psychic echoes, a DC 13 Wisdom saving throw every 2 minutes. Something below notices the conduit, which is M6's cause, written in GM text.
  - **Debrief.** No healing mechanic. Melannor's "debt repaid" line is story only.
- **Readers.**
  - **Farm Damaged by Fire:** Gerrick is short with the party.
  - **Mirsa Rescued:** one line.
  - **Fouled Channel Requested:** Melannor says Jeryth asked for this.
- **Background.** The waste is thrall-conditioning residue (see Rules). Imre is "the Splinter's" arcanist, and the same hand wrote M1's journal page.

### M6 The Dreamer's Reach (overview, ev-01 The Descent, ev-02 The Anchor, design-notes). Report 04 §6; decision 2
- **Delete `ev-01-the-dreamers-reach.md`** and write `ev-01-the-descent.md` and `ev-02-the-anchor.md`.
- **Gate.** 7th level after Kolat Towers, R13. Parties that run three heists play it after the Vault. The overview says so, and that the Vault does not require it.
- **ev-01 The Descent**
  - Jeryth has been silent for three days. Melannor waits in the garden, which is growing without direction.
  - He gives the party a *spell scroll* of *water breathing* and the bark that glows near the anchor.
  - The 48-hour clock.
  - Through Gerrick's tunnel and past M5's cistern, by a fitted-stone passage.
  - Three routes to the anchor: the bark, the current, and M5's conduit.
  - The DC 13 Wisdom saving throw on entering the deepest section. On a failure the character is Incapacitated until the end of their next turn.
  - Marks nothing. Continue with **The Anchor**.
- **ev-02 The Anchor**
  - The chuul are Illuun's brood. They swim (Swim 30, Amphibious), and the flood hinders only the party. Rosters from the mechanics reference.
  - **The anchor.** A rule from the mechanics reference: 15 or more fire or radiant damage in one hit destroys it.
  - **Examine it first:** a DC 15 Wisdom saving throw. On a failure the character is Frightened of the anchor and marks **Illuun Contact**. That character knows its age and patience, and learns its name only if the Stone named it.
  - Jeryth wakes. Her two lines: "Make sure no one is watching from the water." and "I don't need notice anymore."
  - **The Phaulkonmere Ward:** a woven ring, with rules from the mechanics reference.
  - No Mirt epilogue.
- **Design notes** state that the anchor and Jalester are two separate routes, so destroying the anchor doesn't end Harper or LA M6.

### s01 A Seat at Phaulkonmere (ev-01, design-notes). Report 02 §4e
- **Timing.** Members only. It fires at the M1 debrief, when the member first reaches Renown 3. r03 follows at noon the next day.
- **Scenes:**
  - The Cat Again;
  - The East Gate (the key and its procedure);
  - Jeryth's Welcome: "This garden is yours now. Come when you need it. There are no conditions."
- **Outcome:** **East Gate Key Held**. No renown.

### s02 The Water Table Stirs (ev-01, design-notes). Report 02 §5c
- **Structure:** one event of five dated surges. Each surge has a trigger, a city symptom, a request and a named `+1 Renown:` line, or none.
- **The surges**

  | Surge | Trigger | Symptom | Request |
  |---|---|---|---|
  | One | Fireball! | starlings | Refers to the Fireball! Melannor debrief. Asks members to report aberrant activity from Finding Floon or Gralhund Villa. |
  | Two | attunement | oak roots move two inches | "Keep the Stone moving." No renown. |
  | Three | first Eye | seven cistern dreamers | Report the first heist's aberrant encounter. A second path: Jeryth's awakened rat shows the Castle Ward sewer staircase (WDH). |
  | Four | second Eye | beached fish | Asks for M5, and marks **Fouled Channel Requested**. Bertio Caskwall's ward-seal is a short task, with no fight. |
  | Five | third Eye | black well water | Jeryth's voice grows intermittent. Marks **Silence Warning Given**. |

- **Surge Five** does not promise M6 within a tenday. Jeryth's full silence (M6's opening) begins when a member meets M6's gate, or at the Vault if no member has.
- **Order-agnostic.** Refer to "how many Eyes are restored".
- **Dropped:** the cranium rats and the devourer surge.

### r03 / r10 / r25 / r50 (ev-01 + design-notes each). Report 02 §4d, §7
- **Model:** DR r03 and FG r03/r50.
  - A `What Is Actually True` block.
  - The animal's arrival.
  - `### Naming the Rank` at Phaulkonmere.
  - One `###` per benefit as a per-member procedure: contact, place, notice, limit, who else, loss rule.
  - "The rank event awards no Renown."
  - A member whose renown drops keeps the rank, and the benefits are suspended.
- **r03 Summerstrider** (the grey pigeon, at noon the day after s01)
  - **Relay:** once per tenday per member, 25 words or fewer, to a place Melannor has visited, with the reply carried back.
  - **Healing at Phaulkonmere only:** the fixed list from the mechanics reference, once per Long Rest, member only, for Enclave-business injuries.
  - **Network:** one report per ward per tenday, from a fixed table in the mechanics reference. The Kolat block is gated on **Manshoon Named**. It reads **Splinter Site Reported**.
- **r10 Autumnreaver** (Melannor at the door; if the member is on a mission, he waits for their return)
  - **Jeryth's living sprig:** one casting per quest from the fixed 5th-level list (mechanics reference §10), on 3 days' notice. *Revivify* and *Reincarnate* are excluded, and *Greater Restoration* lives here with Jeryth covering the diamond dust.
  - **The paddock beast:** Brown Bear, Dire Wolf, or the Giant Eagle (a Celestial ally). One operation per quest, and the beast is replaced once if it falls.
  - **Three sewer routes:**
    - the Sea Ward dyer's-district channel;
    - the Southern Ward deep cisterns;
    - the Dock Ward fishmeal warehouse, which reads **Grell Escaped**.
    - They run to WDMM Level 1 by fixed destinations from the mechanics reference, marked by the three-lines-over-a-leaf sign.
- **r25 Winterstalker** (the owl at dusk)
  - **Melannor in the field:** one mission per quest, using the Druid ally from the mechanics reference.
  - **Jeryth's 8th-level casting:** a fixed list, once per quest.
  - **Advance report on a beast:** Advantage on Wisdom (Animal Handling) for Beasts only. Use Intelligence (Nature) for Plants and Elementals.
  - **Sarna Dath's harbor reports:** the carnival fleet only until it sails on Tarsakh 20, then ships of all four factions.
- **r50 Master of the Wild**
  - Hold the event until the member is on the surface. Three animals arrive at the Yawning Portal courtyard or Trollskull Manor.
  - It branches on **Anchor Destroyed** and **Illuun Contact**.
  - The *charm of vitality* goes to each character present.
  - **The six:** three rangers (Scout block) and three druids (Druid block). The leader is named. Size from the mechanics reference.
  - **The beast compact:** CR 2 or lower, one task per quest.
  - **The commission:** written as **Illuun Watch Accepted**.
  - **Mad Mage seeds** as one-line GM facts:
    - Illuun in the Grotto of Madness (Level 4, area 16) and its projection;
    - Halaster's Bulba-Slopp fingerprint;
    - the svirfneblin druid of Zurkhwood Grove;
    - Wyllow on Level 5;
    - the Undermountain rules.
  - Don't duplicate the Lords' Alliance or FG r50 seeds.

## Companion pages (main session, after the folders merge)

- `campaign/guides/factions/04-emerald-enclave.md`:
  - gates and base renown;
  - the Manshoon line at :67;
  - the M4 premise;
  - the Giant Eagle and Animal Handling wording;
  - the ward;
  - the :31 Vault line.
- `campaign/setting/organizations/` (Emerald Enclave): remove the WDH "renown equals spell level" rule; fix the ward.
- Notable Figures:
  - Melannor and Jeryth: `[GM]` converted to `[!gamemaster]`; "several years"; the gold line is Jeryth's.
  - Sir Ambrose: Knight.
  - Kelso: Field Ward, Wererat.
- Rank rows: `players-guide/faction-affiliations.md`, `gm-guide/player-factions-overview.md` (including :156's Sea Ward).
- Trollskull ev-04:57 and `trollskull-manor/02-operating-costs.md:82`: the renovation help.
- **Bonnie Departed** branches: Harper M3 overview (unavailable after it), Force Grey M3 ev-01 Day 6, Force Grey M4 ev-02:277.
- Everything else goes to the out-of-scope log.
