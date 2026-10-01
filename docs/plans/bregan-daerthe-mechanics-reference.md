# Bregan D'aerthe Mechanics Reference

CR 2.0 audits for every Bregan D'aerthe faction-event fight, hazard and ally pool, at three, four and five participating combatants. Filled in by the encounter-builder agent, Session 39. Modelled on `doom-raiders-mechanics-reference.md`.

## Method and conventions

- CR 2.0 only. Party Power from the level table (L4 23, L5 32, L6 35, L7 41, L8 44). Monster Power from the tier-adjusted table (L1-4 Tier 1; L5-10 Tier 2; L11+ Tier 3).
- % HP lost = (Enemy Power / Party Power) squared. Budget = Party Power x multiplier.
- "Standard" in this file = Bruising (20-40% HP lost, Day Cost 4). "Hard" = Bloody (40-60%, Day Cost 6). Mild = 2, Brutal = 8.
- Waves are separate encounters; Day Costs add. Where I add wave percentages to show a whole-mission total, that is a rough heuristic of mine, not a skill rule.
- Combatant counts include non-member companions. Bystanders, victims, escortees and NPCs who do not fight (Ott, Nar'l when escorted, Krebbyg and Fel'rekt when they stay on the boat, Lif) are not counted.
- Flee-at-half-HP heuristic (mine, not a skill rule): Power is the square root of HP x DPR, so a foe who leaves at half HP contributes about 0.71 of its listed Power, and one reduced to a third of its HP contributes about 0.58. Verdicts below use full Power unless a row says otherwise, so real losses run a little lower.
- **Source.** Stat blocks are 2024 *Monster Manual* (XMM) records from the 5etools mirror (`bd-creatures-xmm.json`); spells are 2024 *Player's Handbook* (XPHB) records (`spells-xphb.json`). Both are in the session scratchpad. CRs read from those records: Assassin 8, Bandit 1/8, Bandit Captain 2, Beholder Zombie 5, Bugbear Stalker 3, Bugbear Warrior 1, Commoner 0, Cultist 1/8, Cultist Fanatic 2, Flying Snake 1/8, Giant Rat 1/8, Gladiator 5, Grell 3, Guard 1/8, Guard Captain 4, Hunter Shark 2, Imp 1, Intellect Devourer 2, Knight 3, Mage 6, Merfolk Skirmisher 1/8, Noble 1/8, Pirate 1, Pirate Captain 6, Priest 2, Reef Shark 1/2, Scout 1/2, Spy 1, Tough 1/2, Tough Boss 4, Warrior Infantry 1/8, Warrior Veteran 3.
- **WDH custom blocks: only two exist in the extract.** `bd-creatures-wdh.json` holds just the **Drow Gunslinger** (CR 4, AC 18, 84 HP) and the **Nimblewright** (CR 4, AC 18, 45 HP). There is no custom Jarlaxle, Fel'rekt, Krebbyg, Nar'l, Soluun or Ott block in it. WDH Appendix B (`adventure-wdh.json` l.32331) says only that Nar'l "is a drow mage" (the 2014 *Monster Manual* Drow Mage, CR 7) plus a vial of three eyescratch doses. The Notable Figures pages give Soluun, Fel'rekt and Krebbyg as Drow Gunslinger, Nar'l as Mage, Jarlaxle as "Swashbuckler (with modifications)" and Ott as Cult Fanatic.
- **Mappings used (the 2024 name map at the end is the full list).** Nar'l = 2024 **Mage** (CR 6), not the 2014 Drow Mage. Jarlaxle = **Pirate Captain** (CR 6). Plain drow = **Scout** (CR 1/2), with **Spy** as the heavier option. Drow Gunslinger stays the WDH block (no 2024 equivalent exists).
- **First-turn KO checks.** The skill adds 4 to CR when a monster can kill or KO a PC on turn one. Applies to: the **Mage** (three Arcane Burst at 16 force each, range 120 ft; Fireball 2/day) and the **Beholder Zombie** (two Eye Rays, one of which is a 27-force Disintegration Ray that turns a creature reduced to 0 HP to dust). It does not apply to the Bugbear Warrior (no Multiattack, 9 per hit), Grell (paralysis, but no kill on turn one), Intellect Devourer (stun, 11 psychic; see the Special CR note), Warrior Veteran, Spy, Tough, Bandit Captain or Drow Gunslinger. Each section gives the CR +4 figure where it applies.
- **High-Power warning.** A monster with Power at or above twice a PC's Power. Triggers: Beholder Zombie at L4 (70 vs 46), Mage at L5 (65 vs 64).
- **Special CR warning (skill).** Intellect devourer is on the skill's list of HP-bypassing monsters. Used only with experienced players; see section 1.

## 1. M3 Three Nights (level 4, Trollskull Manor, Tier 1)

Party Power 69 / 92 / 115 for 3 / 4 / 5 PCs. Bruising budget (x0.6) 41.4 / 55.2 / 69; Bloody (x0.75) 51.75 / 69 / 86.25. Monster Power (Tier 1): Bugbear Warrior CR 1 = 22; Tough CR 1/2 = 16; Bandit CR 1/8 = 4; Commoner CR 0 = 1; Intellect Devourer CR 2 = 28; Beholder Zombie CR 5 = 70 (CR 9 = 110 with the first-turn KO adjustment).

Lif and the cellar. The cellar has no windows; the way in from the street is sewer grate T7, and Lif does not manifest in the cellar (`tm03-cellar.md`). Lif's help (one free environmental effect a round, per Appendix C) works in the taproom and upper floors, so it matters for Night 1 and Night 2, not Night 3. I do not add Lif to Party Power; the effect is a free action, not a combatant. Ott is bound by the *iron bands of Bilarro* in the cellar and is not counted.

### Night 1: the bugbears

Stat block (XMM): **Bugbear Warrior** CR 1, AC 14, 33 HP, speed 30, Darkvision 60 ft. No Multiattack. **Grab** (+4, reach 10 ft, 9 bludgeoning, and a Medium or smaller target is Grappled, escape DC 12). **Light Hammer** (+4, reach 10 ft or range 20/60 ft, 9 bludgeoning, Advantage if the target is Grappled by the bugbear). **Abduct** (no extra movement to move a creature it is grappling). A grapple-then-hammer pair deals about 18 on one PC in a round, so there is no first-turn KO at level 4.

**Audit of the source (WDH l.3629, Appendix C: six Bugbears):**

| PCs | Enemy / Party | % HP lost | Verdict | Day Cost |
|---|---|---|---|---|
| 3 | 132/69 | 366% | Impossible | 50 |
| 4 | 132/92 | 206% | Devastating | 25 |
| 5 | 132/115 | 132% | Crushing | 17 |

The restored draft (6 Thugs = 6 Tough + 2 Bugbears = 140) is worse: 412% / 232% / 148%. **Six bugbears at once is not a level-4 fight at any party size.** If the drafter wants the source number, run it as two waves of three (below) with the second wave arriving two or three rounds after the first.

**Recommended rosters:**

| PCs | Standard (Bruising) | Power | % lost | Hard (Bloody) | Power | % lost |
|---|---|---|---|---|---|---|
| 3 | 1 Bugbear Warrior + 1 Tough | 38 | 30.3% (4) | 2 Bugbear Warriors | 44 | 40.7% (6) |
| 4 | 2 Bugbear Warriors + 1 Bandit | 48 | 27.2% (4) | 3 Bugbear Warriors | 66 | 51.5% (6) |
| 5 | 3 Bugbear Warriors | 66 | 32.9% (4) | 4 Bugbear Warriors | 88 | 58.6% (6) |

Notes:
- The 3-PC Hard row sits on the Bruising/Bloody line (40.7%). The Bandit and the Tough are the "rest of the gang" hangers-on and keep a street brawl feeling like a gang.
- **Six as written, 5 PCs only:** two waves of 3 Bugbear Warriors, 66 Power each, 32.9% + 32.9% = about 65.8% overall, cost 4 + 4 = 8. Anything below 5 PCs should not use this.
- Thresholds: the bugbears break when two of them are down or when half the gang is bloodied; those who run take the street door. A bugbear that has a PC grappled and is within 5 feet of the cellar stair is the objective threat (it can Abduct toward the cellar), so make "reach the cellar door" the escape-hatch for the party, not an attrition race.
- Non-combat route (draft idea, not mine): paying the gang off or showing them Ott is already gone ends the night; a DC 15 Charisma (Intimidation) check against a bugbear that has already lost one packmate works as the fallback.

### Night 2: four Dungsweepers' Guild Commoners hosting Intellect Devourers

**What the 2024 Intellect Devourer does to a host (XMM p.179, CR 2, Tiny aberration, AC 12, 28 HP, speed 40, Blindsight 60 ft, resists psychic).**
- **Steal Body.** Targets one Small or Medium Humanoid or Beast within 5 ft that is **Incapacitated** and has **10 HP or fewer**, Intelligence save DC 12. On a failure the devourer possesses it, **consumes its brain** and teleports inside its skull. While inside it has **Total Cover** against attacks from outside the host. It keeps its own Int, Wis and Cha, Deep Speech, telepathy 60 ft and Detect Intelligence, and otherwise **adopts the host's statistics** (it knows everything the host knew, including spells and languages).
- **If the host body dies, the devourer must leave it.** It is forced out into the nearest open space. Nothing in the record says it takes damage when expelled, so it comes out with its own full 28 HP.
- **It can also leave voluntarily** by spending 5 ft of movement; the body then dies unless its brain is restored before the end of the devourer's next turn. The only restoration the record names is *Wish*.
- Other actions: Multiattack (one **Claw** +4, 7 slashing, and **Devour Intellect**: Int save DC 12, 11 psychic and **Stunned** until the end of its next turn).
- **Detect Intelligence** (trait): senses every creature with Intelligence 3+ within 300 feet through barriers.

Consequences for the drafter:
1. **The host/devourer split matters.** The fight is two layers. A hosted Commoner is a Commoner: AC 10, 4 HP, Club +2 for 2 damage, and the devourer inside is untouchable until the body drops. Killing the shell does no damage to the devourer, which pops out at full HP and acts. So a hosted Commoner is effectively a free round of cover plus a 28-HP monster.
2. **The Dungsweepers are already dead.** A hosted Commoner's brain is consumed. Killing the shell, or the devourer leaving, does not kill anyone who was alive. Nothing the party can do saves the host short of *Wish*. The draft's "extraction kills the host" and "devourers flee through the ears" are wrong against the 2024 record; the printed rule is a teleport to the nearest open space within 5 ft. If the drafter wants the Dungsweepers to be savable, that is a named swap using the brain-preserving occupation variant in Harper M5, and it changes nothing in the Power figures.
3. **Detect Intelligence means Ott is found.** The cellar is within 300 feet of the taproom, so each devourer senses the mind in the cellar the moment it is inside the manor. The draft's "if Ott is not found they leave" only works if Ott is moved well away. Spotting them (DC 15 Insight or DC 15 Perception, pupils) is easier to justify as "they stare at the floor".
4. **Special CR warning.** A devourer can Steal Body on a downed PC: a character at 0 HP is Incapacitated and under 10 HP, so a failed DC 12 Intelligence save means the PC's brain is consumed. That bypasses HP and death saves entirely. For a table that does not want that, say plainly in the text that the devourers are here for Ott and do not target fallen PCs on this night. This is a ruling, not a printed rule.
5. No first-turn KO: Devour Intellect stuns and deals 11.

Power for the roster: each hosted Commoner counts as Commoner 1 + Devourer 28 = **29**; a plain (unhosted) Dungsweeper Commoner counts **1**; a Guild foreman uses the Tough (16).

Source as written (all four hosted, Power 116): 3 PCs 283% Impossible (50); 4 PCs 159% Crushing (17); 5 PCs 101.7% Overwhelming (13). **Four hosts is too many below 5 PCs**, and at 5 PCs it is already Overwhelming.

**Recommended rosters** (keep the table of four Dungsweepers by making some plain):

| PCs | Standard (Bruising) | Power | % lost | Hard (Bloody) | Power | % lost |
|---|---|---|---|---|---|---|
| 3 | 1 host + 3 plain Commoners | 32 | 21.5% (4) | 1 host + Tough foreman + 2 plain | 47 | 46.4% (6) |
| 4 | 1 host + Tough foreman + 2 plain | 47 | 26.1% (4) | 2 hosts + 2 plain | 60 | 42.5% (6) |
| 5 | 2 hosts + 2 plain | 60 | 27.2% (4) | 3 hosts + 1 plain | 88 | 58.6% (6) |

Notes:
- The plain Commoners panic, hide, or fight with Clubs; they are bystanders, not a threat. They do not know what the others carry.
- Thresholds: a devourer that is out of its host and below 14 HP (half) tries to Steal Body on any Incapacitated creature within reach, or flees toward Ott's mind if it cannot. A devourer reduced to 0 is destroyed (no Steal Body, no host). Hosts who are unmasked leave if Ott is not accessible.
- Non-combat route: DC 15 Insight or Perception spots them; luring the hosts out of the manor (Detect Intelligence means they follow the sense of a mind, so decoy stands such as a sleeping Lif-animated mannequin do not work) is the fallback, or paying the tab and telling them "he was moved".

### Night 3: the Beholder Zombie

**2024 Beholder Zombie (XMM p.347).** CR 5, Large undead, AC 15, 93 HP, speed 5 ft, Fly 20 ft (hover), Darkvision 60 ft, passive Perception 9, Int 3. Immune to poison; immune to exhaustion, poisoned and prone. Saves: Wis +2. Understands Deep Speech and Undercommon, cannot speak. **No antimagic cone, no Central Eye, no scent-tracking trait**; the draft's cone and scent are invented, and Appendix C's "Central Eye" line is a 2014 echo. Use only what is printed:
- **Undead Fortitude.** At 0 HP, Constitution save DC 5 + damage taken unless the damage is Radiant or a critical hit; on a success it drops to 1 HP instead.
- **Multiattack.** Eye Rays twice.
- **Bite.** +5, reach 5 ft, 16 (4d6 + 2) piercing.
- **Eye Rays.** One random ray (roll 1d4; reroll a ray already used this turn) at a target it can see within **120 feet**:
  1. **Paralyzing Ray:** Con DC 14; on a failure Paralyzed, repeating the save each of its turns; after 1 minute it succeeds automatically.
  2. **Fear Ray:** Wis DC 14; on a failure 13 (3d8) psychic and Frightened until the end of its next turn.
  3. **Enervation Ray:** Con DC 14; on a failure 10 (3d6) necrotic, Poisoned until the end of its next turn and cannot regain hit points; half damage on a success.
  4. **Disintegration Ray:** Dex DC 14; on a failure 27 (5d10) force; on a success half. A nonmagical object or creation of magical force is hit by a 10-ft cube of disintegration. **A creature reduced to 0 HP by this damage is turned to dust**, whether it failed or passed.

High-Power warning: 70 is more than twice a 4th-level PC (23 x 2 = 46). **First-turn KO:** two Eye Rays a turn means a 50% chance (1/4 on the first ray, then 1/3 of the remaining on the second) that one is the Disintegration Ray. At 27 damage a 4th-level caster of about 22-26 HP can be reduced to 0 and disintegrated on turn one. So the CR +4 figure (CR 9, Power 110) applies if the zombie is allowed two rays on its first turn: 254% Impossible (3 PCs), 143% Crushing (4 PCs), 91.5% Oppressive (5 PCs). The base figures below assume a **named modification**: the zombie arrives through grate T7 into a one-lane approach and gets only **one Eye Ray on its first turn** (it has not yet oriented), and no PC is within its line of sight at 27 HP or fewer when it appears. Without that modification, step each roster down one row.

Zombie Power at reduced HP (listed for the 3 and 4-PC rows): full 70; two-thirds HP (62 HP) about 57; half HP (46 HP) about 49.5; one-third HP (31 HP) about 40.

| PCs | Standard (Bruising) | Power | % lost | Hard (Bloody) | Power | % lost |
|---|---|---|---|---|---|---|
| 3 | Zombie at 1/3 HP (31 HP) | 40 | 34.3% (4) | Zombie at 1/2 HP (46 HP) | 49.5 | 51.5% (6) |
| 4 | Zombie at 2/3 HP (62 HP) | 57 | 38.6% (4) | Zombie at full HP (93 HP) | 70 | 57.9% (6) |
| 5 | Zombie at full HP | 70 | 37.1% (4) | Zombie + Tough (Guild handler) | 86 | 55.9% (6) |

Notes:
- **3 PCs cannot fight a full-HP zombie** (103% Overwhelming even with the one-ray modification). The reduced starting HP is a named modification (**invented**): the grate and the long sewer crawl weather it, or Night 2's fight leaves it tracking a wounded flank. The drafter must state a reason, or drop to a fully non-combat resolution for 3 PCs (Ott's bands or a sacrifice of furniture; the draft idea of Lif ringing the glasses is flavor only because Lif does not manifest in the cellar).
- Thresholds: it fights to destruction (mindless). Undead Fortitude makes the last 15-25 HP uneven; budget two rounds of cleanup. Radiant damage and critical hits bypass Undead Fortitude.
- It is slow (walk 5, fly 20), so a party that stays out of line of sight at range can kite it; the 120-ft Eye Rays make "run" a poor option in open ground, and the cellar's low ceiling is the actual limit on its flight.
- Non-combat route (draft idea): Ott's disappearance with the bands ends the night if the party stalls long enough, which the source states ("after the third attack Ott disappears"). Make the zombie's goal reaching Ott, not the PCs, so the party can win by delay.

### Whole-mission Day Cost for M3

| PCs | Standard: N1 + N2 + N3 | Percent sum (rough) | Day Cost if no rest between | Hard: N1 + N2 + N3 | Percent sum (rough) | Day Cost if no rest |
|---|---|---|---|---|---|---|
| 3 | 30.3 + 21.5 + 34.3 | about 86% | 4 + 4 + 4 = 12 | 40.7 + 46.4 + 51.5 | about 139% | 6 + 6 + 6 = 18 |
| 4 | 27.2 + 26.1 + 38.6 | about 92% | 12 | 51.5 + 42.5 + 57.9 | about 152% | 18 |
| 5 | 32.9 + 27.2 + 37.1 | about 97% | 12 | 58.6 + 58.6 + 55.9 | about 173% | 18 |

The three nights are separated by days. If the party takes a long rest between nights (the Lif-guarded taproom allows it), each night is its own adventuring day and costs 4 (Standard) or 6 (Hard). The sums apply only if the party pushes through without a full rest (staying up to guard Ott, say). 12 is Debilitating; 18 is past the end of the fatigue table. This is a three-fight mission and the Hard rows are for tables that want to be pushed.

## 2. M4 The Compromised Eye (level 5, Xanathar's Lair X35, Tier 2)

Party Power 96 / 128 / 160. Bruising budget 57.6 / 76.8 / 96; Bloody 72 / 96 / 120. Monster Power (Tier 2): Mage CR 6 = 65; Grell CR 3 = 30; Bandit Captain CR 2 = 23; Bugbear Warrior CR 1 = 17; Spy CR 1 = 17; Tough CR 1/2 = 12; Warrior Veteran CR 3 = 30.

**Nar'l: Mage or the WDH block?** There is no custom WDH Nar'l block; WDH says he is "a drow mage" (2014 MM Drow Mage, CR 7). Use the 2024 **Mage** (XMM p.199): CR 6, AC 15 (Mage Armor included), 81 HP, Int save +6, Multiattack three **Arcane Burst** (+6, reach 5 ft or range 120 ft, 16 force), spell save DC 14. At will: *Detect Magic*, *Light*, *Mage Armor*, *Mage Hand*, *Prestidigitation*. 2/day each: *Fireball* (level 4 version), *Invisibility*. 1/day each: *Cone of Cold*, *Fly*. *Misty Step* 3/day (bonus). Protective Magic 3/day (*Counterspell* or *Shield*). Swaps for the character (named): replace one 2/day *Invisibility* use with *Sending* so WDH's brother-to-brother channel works (the 2024 Mage has no *Sending* and no *Dimension Door*; the draft's Dimension Door arrival is unsupported). Add WDH's three vials of **eyescratch** (contact poison, Con DC 14 or Poisoned for 1 hour and Blinded while Poisoned). He is not a fighter by nature; he uses *Shield*, *Misty Step*, *Invisibility* and eyescratch to get away.

**Grell (XMM p.157).** CR 3, AC 12, 55 HP, speed 10, Fly 30 (hover), Blindsight 60 ft, immune to lightning, immune to blinded and prone. Multiattack: one **Beak** (+4, 11 piercing) and one **Paralyzing Tentacles** (+4, reach 10 ft, 7 piercing; a Medium or smaller target is Grappled, escape DC 12, and must also make Con DC 11 or be Poisoned, repeating the save each turn for up to 1 minute, and **Poisoned = Paralyzed**). **Abduct** applies. It is CR 3; a paralyzed PC in a grell's reach next to other attackers is the danger, but it does not trip the first-turn KO rule on its own.

First-turn KO and High-Power: Mage 65 is more than 2x a 5th-level PC (32 x 2 = 64). Three Arcane Bursts average 48 force and Fireball is 2/day, so a fighting Nar'l can KO a caster on turn one. If he stands and fights, apply CR +4 (CR 10, Power 95): 97.9% Oppressive (3 PCs), 55.1% Bloody (4), 35.3% Bruising (5). The rosters below assume he trades, flees or defends (that is who he is: "What would you offer?"). If the party corners him and he fights back, step each roster down one row.

### 2a. Nar'l alone (before the clock)

| PCs | Enemy / Party | % HP lost | Verdict | Day Cost |
|---|---|---|---|---|
| 3 | 65/96 | 45.8% | Bloody | 6 |
| 4 | 65/128 | 25.8% | Bruising | 4 |
| 5 | 65/160 | 16.5% | Mild | 2 |

Grell alone (for reference): 30/96 = 9.8%, 30/128 = 5.5%, 30/160 = 3.5%, all below Mild (floor cost 2).
Nar'l + grell: 95 = 97.9% Oppressive (3 PCs, cost 10), 55.1% Bloody (4, cost 6), 35.3% Bruising (5, cost 4).

### 2b. "Eliminate Nar'l" fight (the party attacks him in X35; the grell is out of the room for the twelve-minute window)

| PCs | Standard (Bruising) | Power | % lost | Hard (Bloody) | Power | % lost |
|---|---|---|---|---|---|---|
| 3 | Nar'l at 2/3 HP (after a surprise or first-round burst) | 53 | 30.5% (4) | Nar'l at full HP | 65 | 45.8% (6) |
| 4 | Nar'l alone | 65 | 25.8% (4) | Nar'l + Bugbear Warrior (Guild runner) | 82 | 41.0% (6) |
| 5 | Nar'l + Tough (Guild runner) | 77 | 23.2% (4) | Nar'l + Bugbear Warrior + 2 Tough | 106 | 43.9% (6) |

(Mage at 2/3 HP = 65 x sqrt(2/3), about 53.) The runners are Guild muscle who knock to deliver a message and are not part of the grell's guard detail; if the drafter prefers no runners, use the 3-PC row at any size and expect a Mild fight at 4 and 5 PCs.

Thresholds:
- He opens by talking (the Appendix C trade: the X19 Eye location and the X18 Panopticus bypass for his life and an extraction). He fights only when the party refuses or attacks first.
- He uses *Shield* (reaction) on the first hit, *Misty Step* when grappled or adjacent, and *Invisibility* to break line of sight. He surrenders at 40 HP (half) or fewer, or after *Misty Step* and *Invisibility* are spent.
- He uses eyescratch on a PC who has him pinned and then uses the blinded round to leave; this is the one effect that can undo a plan, so state it up front.
- Runners flee when Nar'l surrenders or falls, or at half HP.
- Insight on his story (Appendix C): DC 18 substantially true, DC 14 mostly true, DC 10 unnaturally calm. That check is the non-combat route to Extract or Discredit.

### 2c. "Extract under pursuit" and the clock running out

The twelve-minute clock is the grell's return window (Appendix C). Past it, the grell comes back and raises the alarm, and Xanathar's Guild response follows. The same roster is used for both the **pursuit during extraction** and the **clock-out wave** (if the party is still in X35 after twelve minutes). Nar'l is an escortee (not counted); if he can be talked into casting for the party, add Mage 65 to Party Power and rebuild. I do not recommend it: he casts for himself.

Guild response (Tier 2): Bandit Captain 23, Bugbear Warrior 17, Tough 12, grell 30.

| PCs | Standard (Bruising) | Power | % lost | Hard (Bloody) | Power | % lost |
|---|---|---|---|---|---|---|
| 3 | Grell + Bugbear Warrior + Tough | 59 | 37.8% (4) | Grell + Bandit Captain + Bugbear Warrior | 70 | 53.2% (6) |
| 4 | Grell + Bandit Captain + Bugbear Warrior | 70 | 29.9% (4) | Grell + Bandit Captain + 2 Bugbear Warriors | 87 | 46.2% (6) |
| 5 | Grell + Bandit Captain + 2 Bugbear Warriors | 87 | 29.6% (4) | Grell + Bandit Captain + 3 Bugbear Warriors | 104 | 42.3% (6) |

Whole-mission "eliminate Nar'l, then stay too long" (2b plus 2c; rough sum of the two waves):

| PCs | Standard (2b Std + 2c Std) | Hard (2b Hard + 2c Hard) |
|---|---|---|
| 3 | 30.5 + 37.8 = about 68%, cost 8 | 45.8 + 53.2 = about 99%, cost 12 |
| 4 | 25.8 + 29.9 = about 56%, cost 8 | 41.0 + 46.2 = about 87%, cost 12 |
| 5 | 23.2 + 29.6 = about 53%, cost 8 | 43.9 + 42.3 = about 86%, cost 12 |

These assume the party stands and fights both waves. The intended play is to leave before the grell returns; the sums show why.

Notes:
- If Xanathar's Lair has already run, the grell may be dead, Nar'l may already be extracted or evacuated, or the Guild may be on a war footing. Remove the grell (30) from the table and use the rest; escalate the squad one row if the escalation tier is Alert or Lockdown.
- Thresholds: the squad fights to the Bandit Captain's fall, then surrenders or flees. The grell does not retreat (it was set to kill Nar'l on disloyalty) and fights until reduced to 0 HP, though it will prioritize Nar'l if it can see him.
- Non-combat route: leaving X35 within twelve minutes by the X18 bypass avoids the wave entirely.

## 3. M5 The Theater's Back Room (level 6, Tier 2; no planned fight)

Party Power at L6: 105 / 140 / 175. Bruising budget 63 / 84 / 105; Bloody 78.75 / 105 / 131.25. These are stat names for a fight that breaks out, not a roster.

| Character | 2024 block | CR | Power (T2) | Notes |
|---|---|---|---|---|
| Florette (Cassalanter watcher) | **Spy** | 1 | 17 | AC 12, 27 HP, shortsword or hand crossbow (5 + 7 poison), Cunning Action |
| Watch officer | **Guard Captain** | 4 | 38 | AC 18, 75 HP, two attacks (longsword 15 or javelin 14), javelin range 30/120 |
| Watch constable | **Guard** | 1/8 | 3 | AC 16, 11 HP, spear 4 |
| Seffia Naelryke | **Cultist Fanatic** | 2 | 23 | AC 13, 44 HP, Pact Blade 6 + 7 necrotic, *Hold Person* 1/day, *Command* 2/day, *Spiritual Weapon* 2/day |
| Arn Xalrondar | **Cultist Fanatic** | 2 | 23 | same block |
| Windmill sentry imp (arc-e) | **Imp** | 1 | 17 | AC 13, 21 HP, resists cold, immune fire and poison, Sting 6 + 7 poison, *Invisibility* at will |

Break-out figures, if one happens (not recommended rosters):

| Roster | Power | 3 PCs (105) | 4 PCs (140) | 5 PCs (175) |
|---|---|---|---|---|
| Florette alone | 17 | 2.6% below Mild | 1.5% | 0.9% |
| Florette + Guard Captain (the Watch officer arrives) | 55 | 27.4% Bruising (4) | 15.4% Mild (2) | 9.9% Mild (2) |
| Seffia + Arn + imp (windmill debrief page, if it turns violent) | 63 | 36.0% Bruising (4) | 20.3% Bruising (4) | 13.0% Mild (2) |

No first-turn KO from any of these. The Guard Captain is the only block that is dangerous to a single PC and still stays under the High-Power line (38 vs 70).

## 4. M6 The Dive (level 7, Deepwater Harbor at night, Tier 2)

Party Power at L7: 123 / 164 / 205. Bruising budget 73.8 / 98.4 / 123; Bloody 92.25 / 123 / 153.75. Monster Power (Tier 2): Warrior Veteran CR 3 = 30; Bandit Captain CR 2 = 23; Spy CR 1 = 17; Bugbear Warrior CR 1 = 17; Tough CR 1/2 = 12; Merfolk Skirmisher CR 1/8 = 3.

Krebbyg and Fel'rekt appear but stay on the surface boat (non-combatants). If the drafter has them fight, each is a Drow Gunslinger (Power 38): add 76 to Party Power (199 / 240 / 281) and rebuild every roster below.

### 4a. Who the Guild sends (2024 blocks and why)

- **Surface lookout: Spy** (CR 1, 17). Perception +6 and passive 16, Stealth +6, a hand crossbow, and Cunning Action to run and signal. The Guild would post a competent skulker, and 17 Power is below the skill's concerns.
- **Dive leader: Warrior Veteran** (CR 3, 30). Name to be supplied by the drafter (invented; suggestion: Orlo Stannick). AC 17, 65 HP, two attacks (Greatsword 10, or Heavy Crossbow 12), Parry. He is the Guild's sturdy professional, which a one-person guard post on a ship hull needs. Named swap for the water: **Trident** (martial; +5, 1d8+3, versatile 1d10+3 for about 8) instead of the Greatsword, so he does not take the disadvantage below; he keeps the Heavy Crossbow (see rules).
- **Dive team deputy: Bandit Captain** (CR 2, 23). AC 15, 52 HP, two attacks, Parry. Named swap: Pistol becomes a **Light Crossbow** (a firearm underwater has no rule I can find; I assume it does not fire), Scimitar becomes **Trident** or Spear.
- **Divers: Tough** (CR 1/2, 12). AC 12, 32 HP, Pack Tactics. Named swap: Mace becomes **Spear** (about the same 5 damage); Heavy Crossbow stays. They wear Guild diving kit and are the portion of the team that needs water breathing.
- **Native swimmers: Merfolk Skirmisher** (CR 1/8, 3). AC 11, 11 HP, Swim 40, amphibious, Ocean Spear (3 piercing + 2 cold, ranged 20/60, returns to hand, reduces speed by 10). Hired locals paid in coin, not loyal; they are the only team members with a swim speed, so they give the water a function (they pick the PCs apart at range, slowing them) and they flee the moment the Veteran goes down. This fixes the draft's "merfolk as texture with no mechanical function".
- **Reinforcements on a signal: Bandit Captain, Tough, Bugbear Warrior.** A rowboat of Guild muscle that arrives on the surface (see 4c).

### 4b. Fights

**Lookout (surface):** a Spy alone is 17 Power: 1.9% / 1.1% / 0.7% of HP lost (3 / 4 / 5 PCs), well below Mild (cost 2 by the table floor; effectively 0 if it ends by stealth). It fights only to raise the alarm.

**Dive team (underwater, wave 1):**

| PCs | Standard (Bruising) | Power | % lost | Hard (Bloody) | Power | % lost |
|---|---|---|---|---|---|---|
| 3 | Warrior Veteran + 2 Tough + 2 Merfolk | 60 | 23.8% (4) | Warrior Veteran + Bandit Captain + 2 Tough + 2 Merfolk | 83 | 45.5% (6) |
| 4 | Warrior Veteran + Bandit Captain + 2 Tough + 2 Merfolk | 83 | 25.6% (4) | Warrior Veteran + Bandit Captain + 4 Tough + 2 Merfolk | 107 | 42.6% (6) |
| 5 | Warrior Veteran + Bandit Captain + 4 Tough + 2 Merfolk | 107 | 27.2% (4) | 2 Warrior Veterans + Bandit Captain + 4 Tough + 2 Merfolk | 137 | 44.7% (6) |

No High-Power or first-turn KO issue: the largest single Power is 30 (the Veteran); a Veteran round is about 20 damage on one target.

**Underwater adjustment (my judgment, not a skill rule).** If the party has neither water breathing nor swim speeds, treat each row one row harder (the party has Disadvantage on non-listed melee weapons and cannot move at full speed, while the Merfolk are native). If the party has *Water Breathing* and swim speed (or *Freedom of Movement* for movement), no adjustment.

**Reinforcements on the signal (wave 2, on the surface, rowboat):**

| PCs | Standard (Mild) | Power | % lost | Escalated (Bruising) | Power | % lost |
|---|---|---|---|---|---|---|
| 3 | 2 Tough + Bugbear Warrior | 41 | 11.1% (2) | Bandit Captain + 2 Tough + Bugbear Warrior | 64 | 27.1% (4) |
| 4 | Bandit Captain + 2 Tough + Bugbear Warrior | 64 | 15.2% (2) | Bandit Captain + 2 Tough + 2 Bugbear Warriors | 81 | 24.4% (4) |
| 5 | Bandit Captain + 2 Tough + 2 Bugbear Warriors | 81 | 15.6% (2) | Bandit Captain + 4 Tough + 3 Bugbear Warriors | 122 | 35.4% (4) |

(The escalated rows are for a signal sent early, or if the leader's lanyard beat in 4d fires; the Mild rows are the default.) The boat's crossbows and Bandit Captain's Pistol fire on swimmers who surface; underwater the squad does not follow.

**Timing (my estimate):** the reinforcements arrive **5 minutes after the signal** (if the Eyecatcher is still in harbor, it lies about a quarter mile out per arc-h:71, and a rowboat at about 3 mph covers that in roughly five minutes). The signal is the lookout's shuttered lantern or a whistle. If the Spy is taken quietly or killed before signalling, there are no reinforcements.

**Whole-mission totals (rough sum, my heuristic):**

| PCs | Standard (lookout + Std dive + Std reinforcements) | Hard (lookout + Hard dive + Std reinforcements) |
|---|---|---|
| 3 | 1.9 + 23.8 + 11.1 = about 37%, cost 2 + 4 + 2 = 8 | 1.9 + 45.5 + 11.1 = about 58%, cost 2 + 6 + 2 = 10 |
| 4 | 1.1 + 25.6 + 15.2 = about 42%, cost 8 | 1.1 + 42.6 + 15.2 = about 59%, cost 10 |
| 5 | 0.7 + 27.2 + 15.6 = about 43%, cost 8 | 0.7 + 44.7 + 15.6 = about 61%, cost 10 |

Cost 8 is Taxing-to-Draining; 10 is just past Draining. This is a mission that ends the day, so no further fights should follow on the same day.

Thresholds:
- The lookout drops the lantern signal when he sees the dive, then retreats along the roofline; he does not surrender cornered. The Merfolk flee when the Warrior Veteran falls. The Veteran surrenders at 1/4 HP (about 16) if surrounded, and will not go back to the Guild.
- The team does not know BD is coming, so the lookout and divers are not on high alert; the lookout's passive Perception is 16.
- Non-combat route: DC 14 Charisma (Deception) as a dock inspector, or paying the lookout; either does not stop the charge, only the signal.

### 4c. Underwater combat rules (2024 text, checked by the main session)

The main session checked these against the 5etools-mirror-3 data (`book-xphb.json`, `book-xdmg.json`, `variantrules.json`, `items.json`). Use this section, not the 2014 rules.

- **Impeded Weapons (XPHB, Underwater Combat).** "When making a melee attack roll with a weapon underwater, a creature that lacks a Swim Speed has Disadvantage on the attack roll unless the weapon deals Piercing damage." So spears, rapiers, daggers, tridents and shortswords are fine for everyone. Maces, scimitars and greatswords are not.
- **Ranged (XPHB).** "A ranged attack roll with a weapon underwater automatically misses a target beyond the weapon's normal range, and the attack roll has Disadvantage against a target within normal range." There is no crossbow exception in 2024.
- **Fire Resistance (XPHB).** "Anything underwater has Resistance to Fire damage."
- **Swimming (XPHB).** Each foot of movement costs 1 extra foot, or 2 extra in difficult terrain, unless the creature has a Swim Speed. A Speed 30 PC therefore covers 15 feet a round. Rough water may need a DC 15 Strength (Athletics) check.
- **Visibility Underwater (XDMG p.36).** The encounter distance is 60 feet in clear water with bright light, 30 feet in clear water with dim light, and 10 feet in murky water or darkness. Deepwater Harbor at night counts as murky water or darkness: 10 feet, more with a light source in clear patches.
- ***Water Breathing* (XPHB).** 3rd level, ritual, 24 hours, up to ten willing creatures, and no Swim Speed.
- **Potion of Water Breathing (XDMG).** 24 hours.
- **Holding breath.** It was not found in the mirror data. The mission assumes *Water Breathing* or potions, provided by the briefing, so the breath rule never decides the outcome. Don't print a minutes figure.
- **Firearms.** No printed rule was found. Pistols are surface-only.

### 4d. The limpet-charge mechanic (INVENTED; Scarlet Marpenoth stats are WDH)

Sourced: the *Scarlet Marpenoth* has **AC 20, 300 HP, damage threshold 15, immune to poison and psychic**; at 0 HP its structure fails and it **floods and sinks**; it is worth 15,000 gp and needs one pilot and one engineer to run; speed 2 mph, 10 passengers (`adventure-wdh.json` l.25658). arc-h:11 mounts it beneath the Eyecatcher's keel about 20 ft down, with a keel collar (arc-h:41) and a hatch visible from beneath (DC 14 Perception, arc-h:73). Per the brief, after Tarsakh 20 the Faire sails and the sub stays behind with a BD team, so by the time M6 runs (after Kolat Towers) the Marpenoth is probably **moored in the harbor away from the Eyecatcher**; then the keel collar does not apply and the hull sits at a quiet berth. I assume the same 20-ft depth.

**Everything below is invented** because no source gives limpet-charge stats.

**The device.** A "ship-breaker": a clamp with a magnetic-and-hook grip, two sealed kegs of smokepowder (about 150 lb together), a clockwork fuse set to fire at first light, and a pressure trigger as anti-tamper. It is clamped to the hull near a ballast seam.

**The Dawn Clock.** Track the time in 5-minute ticks. The party starts with **8 ticks (40 minutes)** when it enters the water (Fel'rekt's watchers spot the Guild boat about an hour before dawn; the party has to arm, brief and swim). Costs: swimming out to the site 1 tick; each Locate attempt 1 tick; each Free attempt 1 tick; each Defuse attempt 1 tick; Jettison 1 tick (outside a 10-round fuse). Combat does not cost a tick unless it runs past 10 rounds (a minute); each additional 5 full minutes of fighting is 1 tick. A clean run uses 5 to 6 ticks, leaving 2 to 3 for failure and the fight. At 0 ticks the charge detonates. The "pressure to dawn" is real: dawn is the detonation, not the fight.

**Step 1: Locate.**
- If the dive team is on station they are standing guard over the charge, so the fight finds it for you (no check).
- If the party killed or drove off the team before locating it, or arrives after the team has retreated: a search of the hull, **DC 14 Wisdom (Perception)** or **DC 14 Intelligence (Investigation)**, one attempt per PC per tick; Disadvantage without a light source; **Advantage** if the party has the lookout's bubble trail or a Fel'rekt/Krebbyg tip on which seam the divers worked. One success finds it.

**Step 2: Free it from the hull.** The clamp has to be released before it can be disarmed or moved. **DC 15 Strength (Athletics)** to pry the grip, or **DC 14 Dexterity (Thieves' Tools)** to drop the latch. A second creature can use Help.
- *Failure by 4 or less:* lose 1 tick (the attempt took a tick anyway).
- *Failure by 5 or more, or a natural 1 ("Jolt"):* the pressure trigger shifts; **the remaining ticks are halved** (round down) and everyone within 5 feet hears the striker click.

**Step 3: Choose Defuse or Jettison.**
- **Defuse.** **DC 15 Dexterity (Tinker's Tools or Thieves' Tools)** or **DC 17 Intelligence (Arcana or Investigation)** to isolate the striker. Success: the charge is dead; the mission is won. Failure by 4 or less: lose 1 tick, retry. *Failure by 5 or more ("Hair trigger"):* the fuse jumps to a **10-round countdown** (end of the tenth round) and the charge can only be jettisoned; any PC within 5 feet hears the tick.
- **Jettison.** The charge weighs about 150 lb. One creature with Strength 13+ can carry it, or two creatures carry it together; **a carrier cannot Dash** unless Strength 15+. It must be at least **60 feet from the hull** (beyond which my damage table below does nothing to the sub) and the swimmers need to be **60 feet farther** from it (beyond which they take nothing); that is 120 feet of travel, or about 8 rounds at 15 ft a round without Dash (4 rounds with Dash). A 10-round fuse is therefore tight but doable: the drama is making the party choose a carrier and commit.
- **The Veteran's lanyard (optional invented beat).** If the Warrior Veteran is alive and sees the PCs at the charge, he can use an action to pull a lanyard that jumps the fuse to a 10-round countdown (the same Hair Trigger state). The lanyard is AC 12, 1 HP, and can be cut with any slashing weapon as an action or a DC 13 Dexterity (Sleight of Hand) check. This makes the first rounds of the fight a race to kill or disarm the Veteran, not a grind.

**Detonation effects (invented):**
- **Creatures.** Everyone fully in the water within 30 ft of the charge: **8d10 force** (average 44), **DC 16 Constitution save for half**. 31 to 60 ft: **4d10 force** (average 22), same save for half. Beyond 60 ft: nothing, but the blast is heard for a mile and bright air bubbles reach the surface.
- **The sub.** If the charge is clamped to the hull: **300 damage** (a single instance far above the threshold of 15, exactly the sub's HP): it **floods and sinks**. Detonation within 30 ft but not clamped: **150 damage**, and the sub is crippled (it cannot dive or move until repaired, about a tenday and 5,000 gp, my guess). 31 to 60 ft: **60 damage**. Beyond 60 ft: 0.
- **Crew inside the hull.** BD personnel aboard when it detonates are treated as within 30 ft of the charge.
- **What this does to the outcomes.** "Marpenoth Saved" = the charge is defused or jettisoned beyond 60 ft. "Marpenoth Crippled" (150) and "Marpenoth Sunk" (300) are the failure states. The drafter picks which are named outcomes; only Saved is required by the brief.

**Why these numbers.** A 7th-level PC has roughly 55 to 70 HP. A failed save against 8d10 (average 44) is a heavy hit but not a knockout, and a successful save halves it; a PC already hurt by the dive team should be warned. The sub's 300 HP equals the clamped-charge damage so that an untouched charge is decisive; the half and quarter figures reward a good jettison.

## 5. Rank allies

Method: ally Power counts in full under the skill's rule, added to Party Power, and then the encounter is rebuilt from the allied Party Power. In practice expect the allies to be spent (one casualty per package is fair). Spy, Scout and Pirate Captain are 2024 blocks; Drow Gunslinger is the WDH block.

### r10 Officer: Ilphrin Quiss (drow Spy)

Spy (XMM CR 1): AC 12, 27 HP, shortsword or hand crossbow 5 + 7 poison, Cunning Action, Perception +6, Stealth +6, thieves' tools. The 2024 Spy has no darkvision; named swap for a drow: add Darkvision 120 ft and Sunlight Sensitivity from the WDH Gunslinger traits. **Power 17 (Tier 2).** One Spy per Officer; two Officers means two Spies (34).

Officer is reached after M4 on guide base awards (1 + 2 + 2 + 3 + 3 = 11; Officer is 10), so assume level 5 (Tier 2); level 6 is shown too.

| Level | Base (3 / 4 / 5 PCs) | + Spy (17) | Bruising budget | Bloody budget |
|---|---|---|---|---|
| 5 | 96 / 128 / 160 | 113 / 145 / 177 | 67.8 / 87.0 / 106.2 | 84.75 / 108.75 / 132.75 |
| 6 | 105 / 140 / 175 | 122 / 157 / 192 | 73.2 / 94.2 / 115.2 | 91.5 / 117.75 / 144 |

Guidance: she reports back by *Sending* and is available between missions, not during, per the draft; so she is **not counted** in Party Power on a mission unless the Officer specifically calls her in. When counted she adds about 12% to a 4-PC party. She will not fight on an operation that puts her against D'aerthe.

### r25 Commander: Pelsha and Vorn, four drow, and Jarlaxle

- **Pelsha and Vorn: Drow Gunslinger (WDH).** CR 4, AC 18 (studded leather and shield), 84 HP, Dex +6, Multiattack two Shortsword (+6, 7), **Poisonous Pistol** (+6, range 30/90, 9 piercing + 11 poison = 20 on a hit, one attack), Gunslinger (no Disadvantage in melee or at long range, ignores half and three-quarters cover), innate *darkness*, *faerie fire* and *levitate* once each, Sunlight Sensitivity. **Power 38 each (Tier 2).** There is no 2024 Drow Gunslinger. The WDH block is rules-compatible and I keep it. An alternative if a drafter insists on a 2024-only roster is the **Tough Boss** (CR 4, 82 HP, AC 16, two attacks), which has more melee punch and no poison.
- **Four drow: Scout (CR 1/2).** The 2014 Drow (CR 1/4) and Drow Elite Warrior (CR 5) have no 2024 equivalent. Map the four "people" to the **Scout** (AC 13, 16 HP, two attacks, Longbow 6): stealth and ranged skirmish suit what they do. Named swaps: add Darkvision 120 ft, Fey Ancestry and Sunlight Sensitivity from the WDH Gunslinger, and swap Longbow for **Hand Crossbow** (30/120) if they are meant to look like drow house guards. **Power 12 each at Tier 2 (48 for four).** For a heavier skirmisher use the **Spy** (17 each, 68 for four, adds 20 Power to the roster).
- **Jarlaxle: Pirate Captain** (XMM p.242). No 2024 Swashbuckler exists; the Pirate Captain is the nearest swashbuckling captain block, and it matches the Zardoz Zord persona. CR 6, AC 17, 84 HP, Dex +7, Multiattack three attacks (**Rapier** +7, 13 piercing and Advantage on the next attack; **Pistol** +7, range 30/90, 15 piercing), **Captain's Charm** (bonus action, Wis DC 14, Charmed until the start of its next turn), **Riposte** reaction (+3 AC, and a rapier counterattack on a miss). **Power 65 (Tier 2).** His Notable Figure page says "Swashbuckler (with modifications)" and "extensive magic item inventory". If the drafter gives him powerful items, treat him as **CR 8 (Power 85)**; it is my estimate of the cost of mods, not a printed figure. He leaves a fight to escape below 30 HP (of 84), so he contributes about 0.8 of his Power (about 52) if the party's fight runs long enough that he drops that low.
  - He is a "resource": he accompanies the party once per quest and fights at full capacity, so treat him as an ally for exactly that operation.
- **Support roster total (Pelsha + Vorn + four Scouts):** 76 + 48 = **124 (Tier 2)**; 144 with four Spies.

Commander is reached by Mad Mage or late Dragon Heist; assume 6th-7th level. Party Power and budgets with allies (level 7, Tier 2):

| PCs | Base | + Gunslingers only (76) | + Support roster (124) | + Jarlaxle (65) | + Roster and Jarlaxle (189) |
|---|---|---|---|---|---|
| 3 | 123 | 199 (Bruising 119.4) | 247 (148.2) | 188 (112.8) | 312 (187.2) |
| 4 | 164 | 240 (144) | 288 (172.8) | 229 (137.4) | 353 (211.8) |
| 5 | 205 | 281 (168.6) | 329 (197.4) | 270 (162) | 394 (236.4) |

Level 6 (Tier 2): base 105 / 140 / 175; + roster 229 / 264 / 299 (Bruising 137.4 / 158.4 / 179.4); + Jarlaxle 170 / 205 / 240; + both 294 / 329 / 364.

Guidance: the roster plus Jarlaxle roughly **doubles** a 4-PC party (164 to 353), so a fight built for the base party is trivial with it. Rebuild the operation from the allied Party Power, or deploy the roster only. Recommended default: **Support roster** for an assault, **Jarlaxle** for a set piece, and both only when the operation is meant to be a showcase. Two Commanders are one pool, not two (draft problem noted in the audit).

### r50 Houseless Noble: ally power (Mad Mage, level 8+)

r50 is Dungeon of the Mad Mage content; assume level 8-10 (Tier 2). Level 8 Party Power is 44 each: 132 / 176 / 220. Tier 3 values are given in case the party has reached level 11.

**Pool (proposed composition):**

| Operative | 2024 block | CR | Count | Power each (T2) | Power each (T3) | T2 total | T3 total |
|---|---|---|---|---|---|---|---|
| Krebbyg, Fel'rekt | Drow Gunslinger (WDH) | 4 | 2 | 38 | 32 | 76 | 64 |
| Pelsha, Vorn | Drow Gunslinger (WDH) | 4 | 2 | 38 | 32 | 76 | 64 |
| Four drow | Scout | 1/2 | 4 | 12 | 7 | 48 | 28 |
| Ilphrin Quiss | Spy | 1 | 1 | 17 | 15 | 17 | 15 |
| Jarlaxle | Pirate Captain | 6 | 1 | 65 | 50 | 65 | 50 |
| **Pool** | | | **10** | | | **282** | **221** |

Soluun is a Drow Gunslinger (38 at T2, 32 at T3) only if neither **Soluun Expelled** (s05) nor DR's **Soluun Killed** applies. Under the brief's decision 5 he is expelled or dead on every path, so I count him as **0** and flag that a drafter who redeems him adds 38.

Deployment packages:

| Package | Members | Power (T2) | Power (T3) |
|---|---|---|---|
| Lieutenants | Krebbyg, Fel'rekt | 76 | 64 |
| Commander roster | Pelsha, Vorn, four Scouts | 124 | 92 |
| Strike | Lieutenants + Commander roster | 200 | 156 |
| Jarlaxle | Jarlaxle alone | 65 | 50 |
| Full pool | all ten | 282 | 221 |

Party Power and Bruising budgets with allies (level 8, Tier 2):

| PCs | Base | + Lieutenants (76) | + Commander roster (124) | + Strike (200) | + Full (282) |
|---|---|---|---|---|---|
| 3 | 132 | 208 (124.8) | 256 (153.6) | 332 (199.2) | 414 (248.4) |
| 4 | 176 | 252 (151.2) | 300 (180) | 376 (225.6) | 458 (274.8) |
| 5 | 220 | 296 (177.6) | 344 (206.4) | 420 (252) | 502 (301.2) |

Guidance:
- The full pool roughly triples a 3-PC party and more than doubles a 5-PC one. Cap deployment at the Lieutenants or the Commander roster unless the operation is a set piece.
- Ally Power counts in full. For a "one major operation" allotment, expect operatives to be spent rather than recovered.
- Krebbyg, Fel'rekt and Jarlaxle all have escape or restraint triggers (Fel'rekt will not kill if another choice exists; Jarlaxle leaves below 30 HP); neither is a Power adjustment, they are behavior notes.
- The *Scarlet Marpenoth* is a vehicle and a crew of non-combat engineers; it adds no Power unless the drafter gives it a weapon, which WDH does not.

## 6. 2024 name map

| Draft name | 2024 name used | CR | Note |
|---|---|---|---|
| Thug | **Tough** | 1/2 | XMM p.307; Pack Tactics, mace, heavy crossbow |
| Veteran | **Warrior Veteran** | 3 | XMM p.320 |
| Bugbear | **Bugbear Warrior** | 1 | XMM p.62; no Multiattack. Bugbear Stalker (CR 3) also exists |
| Commoner (Dungsweeper) | **Commoner** | 0 | XMM p.77; AC 10, 4 HP, club |
| Intellect Devourer | **Intellect Devourer** | 2 | XMM p.179; Steal Body consumes the brain; see section 1 |
| Beholder Zombie | **Beholder Zombie** | 5 | XMM p.347; four Eye Rays, no antimagic cone |
| Grell | **Grell** | 3 | XMM p.157 |
| Drow Mage (Nar'l) | **Mage** | 6 | 2014 Drow Mage is CR 7; WDH has no custom Nar'l block |
| Cult Fanatic (Ott, Seffia, Arn) | **Cultist Fanatic** | 2 | XMM p.85; there is no 2024 "Cult Fanatic" |
| Drow Gunslinger (Soluun, Fel'rekt, Krebbyg, Pelsha, Vorn) | **Drow Gunslinger (WDH p.201)** | 4 | No 2024 equivalent; kept as printed |
| Drow (plain operative) | **Scout** (or **Spy**) | 1/2 (1) | No 2024 Drow; named swaps add drow senses |
| Drow Elite Warrior (arc-h alert response) | **Warrior Veteran** (or **Gladiator** for CR parity) | 3 (5) | 2014 elite warrior is CR 5 |
| Swashbuckler (Jarlaxle) | **Pirate Captain** | 6 | No 2024 Swashbuckler; CR 8 if heavily modified |
| Spy (lookout, Florette, Ilphrin) | **Spy** | 1 | XMM p.295 |
| Watch officer | **Guard Captain** | 4 | XMM p.162 |
| Watch constable | **Guard** | 1/8 | XMM p.162 |
| Noble (Bartlethorpe) | **Noble** | 1/8 | XMM p.227 |
| Flying snake (note courier) | **Flying Snake** | 1/8 | XMM p.353 |
| Imp (Cassalanter watcher, windmill sentry) | **Imp** | 1 | XMM p.177 |
| Merfolk (M6 divers) | **Merfolk Skirmisher** | 1/8 | XMM p.209; native swimmer |
| Bandit Captain (M6 deputy, Guild squad) | **Bandit Captain** | 2 | XMM p.27; Pistol swapped for crossbow underwater |
| Nimblewright (parade; J30 guard) | **Nimblewright (WDH p.212)** | 4 | No 2024 equivalent; AC 18, 45 HP |
| Giant Rat | **Giant Rat** | 1/8 | XMM p.358 |
| Reef Shark, Hunter Shark (optional harbor hazard) | **Reef Shark**, **Hunter Shark** | 1/2, 2 | XMM pp.368, 363 |

## Verification

Checked against the 2024 *Monster Manual* (XMM) and *Player's Handbook* (XPHB) records in the mirror files named in Method.

| Name / item | Status | Note |
|---|---|---|
| Bugbear Warrior, Tough, Bandit, Commoner | Verified (XMM) | CR 1, 1/2, 1/8, 0. Bugbear Warrior has no Multiattack. |
| Intellect Devourer | Verified (XMM) | CR 2, 28 HP; Steal Body text quoted in section 1. Whether a devourer would Steal Body a downed PC is a DM ruling, not printed. |
| Beholder Zombie | Verified (XMM) | CR 5, 93 HP, four Eye Rays, 120 ft, Undead Fortitude, **no antimagic cone**. |
| Grell, Mage, Spy, Guard Captain, Cultist Fanatic | Verified (XMM) | CR 3, 6, 1, 4, 2. |
| Pirate Captain | Verified (XMM) | CR 6; chosen as Jarlaxle's block; a named choice, not a source. |
| Warrior Veteran, Bandit Captain, Merfolk Skirmisher, Scout | Verified (XMM) | CR 3, 2, 1/8, 1/2. |
| Drow Gunslinger, Nimblewright | Verified (WDH extract) | CR 4 each; WDH p.201 and p.212. |
| Jarlaxle, Fel'rekt, Krebbyg, Nar'l, Soluun, Ott WDH custom blocks | **Not in the extract** | The WDH file holds only the Drow Gunslinger and Nimblewright. Nar'l is "a drow mage" in WDH text; the others use blocks named on their NF pages. |
| Drow, Swashbuckler, Thug, Veteran, Cult Fanatic in 2024 | Taken as given | I could not search `bestiary-xmm.json` for these (the session had only a whole-file Read tool). They are as you stated: no 2024 block. |
| *Water Breathing* | Verified (XPHB) | 24 hours, ritual, ten creatures; no swim speed. |
| 2024 underwater combat rules | Verified (XPHB, XDMG) | See 4c. |
| Holding breath | **Not found** | Swim cost verified (XPHB); breath rule not in the mirror data, so missions supply *Water Breathing*. |
| Potion of water breathing duration (2024) | Verified (XDMG) | 24 hours. |
| Limpet charge | **Invented** | Clock, DCs, blast and hull damage are mine; only the Marpenoth's AC 20, 300 HP, threshold 15 are sourced (WDH l.25658). |
| Dive leader name | **Invented** | Orlo Stannick is a suggestion; the drafter may rename. |
| Eye Ray chance of Disintegration (50% over two rays) | My arithmetic | 1/4 on the first ray, then 1/3 on the second after a duplicate reroll. |
