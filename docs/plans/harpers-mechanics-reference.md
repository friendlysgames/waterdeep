# Harpers Mechanics Reference

CR 2.0 audits for every Harper faction-event fight, the Gazer conversion, the Occupying Devourer and its Extraction Procedure, and the rank-ally pools, at three, four and five participating combatants. Filled in by the encounter-builder agent, Session 41. Modelled on `doom-raiders-mechanics-reference.md` and `bregan-daerthe-mechanics-reference.md`. Section 5 is written so Force Grey M3 and M5 can cite it.

## Method and conventions

- CR 2.0 only. Party Power from the level table (L2 14, L3 18, L4 23, L5 32, L6 35, L7 41, L8 44). Monster Power from the tier-adjusted table (L1-4 Tier 1; L5-10 Tier 2; L11+ Tier 3).
- % HP lost = (Enemy Power / Party Power) squared. Budget = Party Power x multiplier.
- "Standard" in this file = Bruising (20-40% HP lost, Day Cost 4). "Hard" = Bloody (40-60%, Day Cost 6). Mild = 2, Brutal = 8, Oppressive = 10, Overwhelming = 13, Crushing = 17, Devastating = 25, Impossible = 50.
- Waves are separate encounters; Day Costs add. Where I add wave percentages, that is a rough heuristic of mine, not a skill rule.
- Combatant counts include non-member companions. Bystanders, victims and NPCs who do not fight (Maxeene, Uza, Fillipa, Tessalar, Remallia, Mirt in M1-M5) are not counted.
- Flee-at-half-HP heuristic (mine, not a skill rule): Power is the square root of HP x DPR, so a foe who leaves at half HP contributes about 0.71 of its listed Power. Verdicts use full Power, so real losses run a little lower.
- **Source.** Stat blocks are 2024 *Monster Manual* (XMM) records in `harpers-creatures.json`. Spells are 2024 *Player's Handbook* (XPHB) records in `spells-xphb.json`. Both are in the session scratchpad. CRs read from the records: Spy 1, Doppelganger 3, Mage 6, Mage Apprentice 2, Tough 1/2, Tough Boss 4, Warrior Veteran 3, Intellect Devourer 2, Mind Flayer 7, Scout 1/2, Guard 1/8, Commoner 0, Draft Horse 1/4. Gazer is legacy (VGM p.126, MPMM p.134), CR 1/2. Mirt (CR 9), Remallia Haventree (CR 9) and Vajra Safahr (CR 13) are WDH custom records.
- **Monster Power used (Tier 1):** CR 0 = 1; 1/8 = 4; 1/2 = 16; 1 = 22; 2 = 28; 3 = 37; 4 = 48. **(Tier 2):** CR 0 = 1; 1/8 = 3; 1/2 = 12; 1 = 17; 2 = 23; 3 = 30; 4 = 38; 6 = 65; 9 = 85; CR 10 = 95.
- **First-turn KO check.** The skill adds 4 to CR when a monster can kill or KO a PC on turn one. It applies to the 2024 Mage (three Arcane Burst at 16 force each, range 120 ft; Fireball 2/day). It does not apply to the Spy (one hit averages 12), the Doppelganger (two Slams average 22), the Gazer (at most one Frost Ray, 10 average, 18 maximum) or the Occupying Devourer (stun and 11 psychic). Each section says where the +4 figure is shown.
- **Special CR warning (skill).** Intellect devourer is on the skill's list of HP-bypassing monsters. The Occupying Devourer removes the brain-eating, but it still bypasses HP when it occupies a host. See section 5.6.
- **Day Cost per scene.** Fights that follow each other on one day add their Day Costs. A Taxing day (6) allows one Hard fight; a Draining day (9) allows a Hard and a Standard.

## 1. M1 The Talking Mare (level 2, Tier 1)

Party Power 42 / 56 / 70 for 3 / 4 / 5 PCs. Budgets: Mild (x0.4) 16.8 / 22.4 / 28; Bruising (x0.6) 25.2 / 33.6 / 42; Bloody (x0.75) 31.5 / 42 / 52.5.

Monster Power (Tier 1): Spy CR 1 = 22; Tough CR 1/2 = 16; Bandit CR 1/8 = 4.

Stat block (XMM): **Spy** AC 12, 27 HP, speed 30, climb 30, Perception +6 (passive 16), Stealth +6. One attack (Shortsword +4 melee, or Hand Crossbow +4, range 30/120), 5 piercing + 7 poison = 12 on a hit. Bonus action Cunning Action (Dash, Disengage or Hide). **Tough** AC 12, 32 HP, Mace 5 or Heavy Crossbow 6, Pack Tactics. **Bandit** AC 12, 11 HP, one attack (4-5).

Maxeene is a non-combatant (Draft Horse, XMM CR 1/4, with Intelligence 10 and Common from the druid's enchantment). She bolts if a fight starts and is not counted.

### As drafted

| Roster | Power | 3 PCs (42) | 4 PCs (56) | 5 PCs (70) |
|---|---|---|---|---|
| Vell alone (Spy) | 22 | 27.4% Bruising (4) | 15.4% Mild (2) | 9.9% Mild (2) |
| Shesstra Street residents (2 Spies) | 44 | 109.8% Overwhelming (13) | 61.7% Brutal (8) | 39.5% Bruising (4) |
| Vell + 2 residents together | 66 | 246.9% Devastating (25) | 138.9% Crushing (17) | 88.9% Oppressive (10) |

Verdict: Vell alone is a fair opener. Two resident Spies are right only for 5 PCs. Putting all three Spies on the board is not a level-2 fight at any party size. The second resident has to be scaled down, or Vell has to stand in for one of the two residents.

### Recommended rosters

| PCs | Vell: Standard | Power | % lost | Vell: Hard | Power | % lost |
|---|---|---|---|---|---|---|
| 3 | Vell alone | 22 | 27.4% (4) | Vell + 2 Bandits (hired runners) | 30 | 51.0% (6) |
| 4 | Vell + Bandit | 26 | 21.6% (4) | Vell + Tough (coach driver) | 38 | 46.0% (6) |
| 5 | Vell + Tough | 38 | 29.5% (4) | Vell + 2 Tough | 54 | 59.5% (6) |

| PCs | Safehouse: Standard | Power | % lost | Safehouse: Hard | Power | % lost |
|---|---|---|---|---|---|---|
| 3 | Spy + Bandit (minder) | 26 | 38.3% (4) | Spy + 2 Bandits | 30 | 51.0% (6) |
| 4 | Spy + 2 Bandits | 30 | 28.7% (4) | Spy + Tough | 38 | 46.0% (6) |
| 5 | 2 Spies (as drafted) | 44 | 39.5% (4) | 2 Spies + 2 Bandits | 52 | 55.2% (6) |

**Vell and the safehouse together.** Vell takes the place of one resident Spy. Use the safehouse rows above and call the second Spy or minder "the resident". If the party fights Vell first and then the building, run them as two encounters: Day Costs add (3 PCs Standard: 4 + 4 = 8).

Thresholds:
- Vell disengages at 13 HP (half) with Cunning Action and heads for the roofline or the hire-coach. She surrenders only if cornered, at 13 HP or fewer. She never speaks first.
- Resident Spies yield at 13 HP and flee over the rear roof. They surrender if cornered at 9 HP or fewer. The second resident yields as soon as the first does.
- Bandit minders (11 HP) yield at 5 HP or fewer, or when a Spy yields. Tough hirelings (32 HP) yield at 16 HP or when Vell yields.
- A cornered Vell surrenders to a party that holds her (Grappled or Restrained) and has hit her at least once. She trades the Shesstra Street address only if she is below 13 HP.
- Hirelings never know Vell's employer. They know a woman who paid by the day.

Notes:
- A Spy hit averages 12 and can reach 20. A 2nd-level caster of about 12 HP can drop to a lucky ambush hit. This does not trip the +4 rule. The rosters assume the party is not ambushed. If Vell opens with a ranged ambush from the hire-coach, step each roster down one row.
- Pack Tactics matters: a Tough has Advantage against any PC that stands within 5 feet of Vell or another conscious ally of his.

## 2. M2 The Dead Drop (level 3, Tier 1)

Party Power 54 / 72 / 90. Budgets: Mild 21.6 / 28.8 / 36; Bruising 32.4 / 43.2 / 54; Bloody 40.5 / 54 / 67.5.

Monster Power (Tier 1): Gazer CR 1/2 = 16.

| Roster | Power | 3 PCs (54) | 4 PCs (72) | 5 PCs (90) |
|---|---|---|---|---|
| 1 Gazer (as written) | 16 | 8.8% below Mild (2) | 4.9% below Mild (2) | 3.2% below Mild (2) |
| 2 Gazers (optional) | 32 | 35.1% Bruising (4) | 19.8% Mild (2) | 12.6% Mild (2) |
| 3 Gazers (not recommended) | 48 | 79.0% Brutal (8) | 44.4% Bloody (6) | 28.4% Bruising (4) |

Verdict: one gazer is a nuisance on HP at every party size. The scene's pressure is the stock, the stairs and the cat, not the HP. If a table wants a Standard fight, use two gazers at 3 PCs only. At 4 or 5 PCs two gazers are still Mild; leave it at one and let the stock rule carry the scene.

The gazer is a stray. It has no handler and no Splinter link. It fights to the death. It is hungry and fixated on Fillipa.

### 2.1 Gazer (2024 format, converted from MPMM)

### Gazer

*Tiny Aberration (Beholder), Typically Neutral Evil*

**AC** 13 **Initiative** +3 (13)

**HP** 13 (3d4 + 6)

**Speed** 0 ft., Fly 30 ft. (hover)

|            | MOD  | SAVE |            | MOD  | SAVE |            | MOD  | SAVE |
| :--------- | :--- | :--- | :--------- | :--- | :--- | :--------- | :--- | :--- |
| **Str 3**  | -4   | -4   | **Dex 17** | +3   | +3   | **Con 14** | +2   | +2   |
| **Int 3**  | -4   | -4   | **Wis 10** | +0   | +2   | **Cha 7**  | -2   | -2   |

**Skills** Perception +4, Stealth +5

**Immunities** Prone

**Senses** Darkvision 60 ft., Passive Perception 14

**Languages** None

**CR** 1/2 (XP 100; PB +2)

#### Traits

***Mimicry.*** The gazer can mimic simple sounds of speech it has heard, in any language. A creature that hears the sounds can tell they are imitations with a successful DC 10 Wisdom (Insight) check.

#### Actions

***Bite.*** *Melee Attack Roll:* +5, reach 5 ft. *Hit:* 1 Piercing damage.

***Eye Rays.*** The gazer uses two different rays chosen at random: roll 1d4 twice and reroll duplicates. Each ray targets one creature the gazer can see within 60 feet. The two rays can target the same creature or different ones.

- **1. Dazing Ray.** *Wisdom Saving Throw:* DC 12. *Failure:* The target has the Charmed condition until the start of the gazer's next turn. While Charmed this way, its Speed is halved and it has Disadvantage on attack rolls.
- **2. Fear Ray.** *Wisdom Saving Throw:* DC 12. *Failure:* The target has the Frightened condition until the start of the gazer's next turn.
- **3. Frost Ray.** *Dexterity Saving Throw:* DC 12. *Failure:* 10 (3d6) Cold damage.
- **4. Telekinetic Ray.** *Strength Saving Throw:* DC 12, one Medium or smaller creature. *Failure:* The target is moved up to 30 feet straight away from the gazer. Alternatively, the ray moves one unattended Tiny object up to 30 feet in any direction, or manipulates a simple tool or container.

#### Bonus Actions

***Aggressive.*** The gazer moves up to its Speed toward a hostile creature it can see.

### 2.2 Gazer audit

- **Source.** MPMM p.134 (VGM p.126 is the original). Both give the same numbers. The 2014 VGM version lists Aggressive as a trait with "as a bonus action" in the text; MPMM, and this block, make it a Bonus Action entry.
- **What changed from MPMM.** Saves moved into the ability table (Wis +2 is the only proficient save). Conditions and damage types are capitalised. Eye Rays gain the explicit "two different rays" wording. The ray list keeps MPMM's numbers. No spell slots, resistances or nonmagical-weapon clauses exist, so nothing else needed converting.
- **The 2024 point you asked about.** The rays already use saving throws in MPMM (DC 12 each), so there are no ray attack rolls to convert. The Bite is the only attack roll. The Frost Ray has no half-damage clause in MPMM. It stays all-or-nothing to keep the CR. The old Appendix C "miss" language does not apply; section 2.3 replaces it.
- **CR math.** Defensive: 13 HP sits between CR 1/8 (9) and CR 1/4 (14). AC 13 matches the row. Effective AC +2 for a hovering flier with a 30-ft speed that kites: AC 15 against a base of 13 lifts defensive CR by one step to about 1/2. Offensive: Frost Ray is the only damage ray. Expected DPR is about 1.75 (half the time it is in the pair, 10 damage, about 35% fail rate at level 3) plus 1 for the Bite, about 3. That is CR 1/8 to 1/4 on damage alone. DC 12 is one above the CR 1/2 row (11). Averaged, the raw math lands at CR 1/4 to 1/2.
- **Decision.** Keep CR 1/2 as requested. The rays control the table more than they hurt: Charmed with halved Speed and Disadvantage, Frightened, and a 30-foot shove. Tier 1 Power for CR 1/2 is 16. Dropping to CR 1/4 would change Power to 10 and make every figure above lower; the fight is already trivial on HP, so the choice does not change a recommendation.
- **First-turn KO.** None. A gazer cannot repeat a ray, so a turn holds at most one Frost Ray: 18 damage at most, against level 3 casters of 16-22 HP. No +4.
- **Table warning.** Telekinetic Ray into a stairwell or off the attic floor is a fall. Count the drop and use ordinary falling damage.

### 2.3 Stock-damage rule

The Sorn Street shelves are the second hit point pool. Use the rule below in place of a timer.

- **Trigger.** A Frost Ray that a target saves against, or a Telekinetic Ray that moves a target, strikes stock if a bookshelf stands within 30 feet behind the target. Most of the shop qualifies. A target standing in a clear aisle with no shelf in line does not trigger it.
- **Cost.** Each strike ruins 10 gp of stock. Tally it as you go.
- **Cap.** Total loss stops at 100 gp. Uza has a policy, Mirt makes up the rest, and nothing worse than 100 gp happens.
- **Playing around it.** A PC who moves the target out of line, or who stands with a wall at their back, avoids the cost. Taking a Frost Ray hit on the chin costs nothing (the damage is the cost).
- **Reading the result.** 0-30 gp: Uza says nothing. 40-100 gp: Uza sighs and asks Mirt to cover it. No renown change either way. Base renown needs the shop cleared and the keys returned.

### 2.4 Fillipa on the ridge beam

- Fillipa sits on the attic's ridge beam, 12 feet up. The shop's ceilings elsewhere are 8 feet.
- She has 2 HP (my assumption: the cat record is not in the data I read). The gazer wants to eat her. Its Bite is the only attack that can touch her.
- The gazer goes for Fillipa only when no PC is within 10 feet of it. Aggressive carries it up the beam in one bonus action. A bite deals 1 damage. She bolts to the far end of the beam. A second bite kills her.
- Reaching the beam without flying: DC 10 Strength (Athletics) to climb the rafters, DC 12 to carry her down. A thrown rope or ladder from the floor needs no check.
- Fillipa comes down 30 seconds after the gazer dies, and goes to the first character who crouches without staring at her.

Thresholds:
- The gazer does not flee. It fights until it is dead or Fillipa is out of the room.
- Non-combat route: a character who removes Fillipa through the door ends the gazer's reason to stay. It follows her for 1 round per 30 feet and then loses interest.

## 3. M3 The Doppelganger Auditions (level 4, Tier 1)

Party Power 69 / 92 / 115. Budgets: Bruising 41.4 / 55.2 / 69; Bloody 51.75 / 69 / 86.25.

Monster Power (Tier 1): Doppelganger CR 3 = 37; Spy CR 1 = 22; Tough = 16; Bandit = 4.

Stat block (XMM): **Doppelganger** AC 14, 52 HP, speed 30, Darkvision 60 ft., immune to Charmed. Multiattack: two Slams (+6, 11 bludgeoning), plus Unsettling Visage if available. Slam has Advantage during the first round of each combat. **Unsettling Visage (Recharge 6):** Wis save DC 12, 15-foot Emanation, Frightened (save each turn, ends after 1 minute). **Shape-Shift** (bonus action): Medium or Small Humanoid; equipment does not transform. **Read Thoughts:** *Detect Thoughts* at will, spell save DC 12, no components. Skills Deception +6, Insight +3.

### Edric alone, if cornered at the Portal

| Roster | Power | 3 PCs (69) | 4 PCs (92) | 5 PCs (115) |
|---|---|---|---|---|
| Edric (Doppelganger) | 37 | 28.7% Bruising (4) | 16.2% Mild (2) | 10.3% Mild (2) |

Verdict: Standard at 3 PCs, Mild at 4-5. That is correct for an infiltrator whose goal is escape. His fight is the chase, not the damage race. Durnan and the Portal's patrons are bystanders.

### The Nethpranter Street safehouse (The Tail)

| Roster | Power | 3 PCs (69) | 4 PCs (92) | 5 PCs (115) |
|---|---|---|---|---|
| 2 resident Spies (Edric away) | 44 | 40.7% Bloody (6) | 22.9% Bruising (4) | 14.6% Mild (2) |
| Edric + 2 Spies (as drafted) | 81 | 137.8% Crushing (17) | 77.5% Brutal (8) | 49.6% Bloody (6) |

Verdict: the drafted roster is right for 5 PCs only. Scale the residents down below 5 PCs.

| PCs | Standard | Power | % lost | Hard | Power | % lost |
|---|---|---|---|---|---|---|
| 3 | Edric + Bandit (minder) | 41 | 35.3% (4) | Edric + 2 Bandits | 45 | 42.5% (6) |
| 4 | Edric + 2 Bandits | 45 | 23.9% (4) | Edric + Spy | 59 | 41.1% (6) |
| 5 | Edric + Spy | 59 | 26.3% (4) | Edric + 2 Spies | 81 | 49.6% (6) |

If Edric is not in the building, drop him and use the Spy and Bandit rows above (a 4-PC party meets Spy + 2 Bandits at 28.7%).

### Shape-Shift escape rules

- Edric changes face as a bonus action. His clothes, hat, bag and boots do not change. A PC tracking him in a crowd picks him out with DC 12 Wisdom (Perception) or Intelligence (Investigation) each round, because he keeps the same coat.
- He loses the tracker by changing clothes (an Utilize action) or by breaking line of sight, changing face and Hiding. He needs both a corner and an action. He gets neither in the same turn unless he Dashes first.
- Cutting him off in a street: DC 13 Strength (Athletics) to tackle or block an alley. A success Grapples him (escape DC 11); a failure lets him past.
- Searching him: DC 14 Intelligence (Investigation) finds the Nethpranter address. If he is Grappled, the check is automatic.
- Unsettling Visage in a crowd frightens bystanders as well as PCs. A panicked crowd is difficult terrain in the 15-foot Emanation.

### Surrender limit

- Edric flees at 26 HP (half) with Dash plus Shape-Shift. If he is cornered at 26 HP or fewer, or Grappled and below half, he surrenders and trades the safehouse address.
- He fights on only while the way out is open. He will not die for the Splinter. He does die for his own face: a PC who strips his disguise (hat or coat, an action) makes him surrender at once.
- Resident Spies: as section 1 (flee at 13 HP, surrender if cornered at 9, the second yields with the first). Bandit minders yield at 5 HP.

Notes:
- Two Slams average 22 against level 4 characters of 28-40 HP. No first-turn KO. The first-round Advantage matters for a PC who is not ready.
- Read Thoughts: Edric can cast *Detect Thoughts* at will. At the Portal interviews he may read surface thoughts. The DM does not need to use this unless the party announces that it is hiding something; a PC who thinks about the Harpers by name should be warned.

## 4. M4 A Friend's House (level 5, Tier 2)

No planned fight. Party Power 96 / 128 / 160. Budgets: Bruising 57.6 / 76.8 / 96; Bloody 72 / 96 / 120. Monster Power (Tier 2): Spy 17; Scout 12; Guard CR 1/8 = 3.

### Jarlaxle is not a fight

- Erystian Demarne is Jarlaxle in a hat of disguise. WDH's Jarlaxle is CR 15 per the brief. I could not read his block in the data I was given. At Tier 2, CR 15 is Power 165: 295% HP lost at 3 PCs (Impossible, 50), 166% at 4 (Crushing, 17), 106% at 5 (Overwhelming, 13). He is not a fight at level 5 at any party size.
- The Bregan D'aerthe reference uses Pirate Captain (CR 6, Power 65) as his allied block for r25. That is an ally figure and does not apply here.
- **If the party draws steel.** Do not roll initiative for Jarlaxle.
  - He raises a hand, says one line in the voice he wants to be remembered for, and withdraws through the nearest door, balcony or crowd. His hat, a changed face and his magic items do the rest.
  - Remallia steps between the party and the guests before a second attack lands. She does not fight a guest in her own house.
  - Lethan interposes and fights (see below), buying two rounds.
  - Consequences are social. Jarlaxle's card carries a different message ("Better luck next time"). **Jarlaxle Discretion Agreement** is lost. The salon ends.

### Lethan, the disguised BD guard

Use the Spy block (Power 17) for a rooftop watcher who fights in melee, or the Scout block (Power 12) for one with a bow.

| Roster | Power | 3 PCs (96) | 4 PCs (128) | 5 PCs (160) |
|---|---|---|---|---|
| Lethan (Spy) | 17 | 3.1% below Mild (2) | 1.8% below Mild (2) | 1.1% below Mild (2) |
| Lethan (Spy) + second guard (Scout) | 29 | 9.1% below Mild (2) | 5.1% below Mild (2) | 3.3% below Mild (2) |

Verdict: Lethan is a delay, not an attrition fight. His job is to cover Jarlaxle's exit.
- Lethan holds the door or the bridge for 2 rounds. He uses Cunning Action to Disengage and to Hide.
- He leaves at 13 HP (half) by the roofline. A BD guard does not surrender. If held, he gives his name and nothing else.
- Remallia's household has no guards beyond two Guards (CR 1/8, Power 3 each) at the gate. They arrest a party that attacks a guest; they do not fight.

No first-turn KO from these blocks. No +4.

## 5. M5 The Sleeping Asset: Nihiloor's Occupying Devourer (level 6, Tier 2)

The user's ruling: Nihiloor's variant does not devour the host's brain. It rides the host and keeps the brain alive. The host can be saved by forcing the devourer out. This is a named custom block, a variant of the 2024 Intellect Devourer (XMM p.179, CR 2). Hosts: Corene Wyldath (Spy), Force Grey's Meloon Wardragon (Warrior Veteran), Orvyn Dall (block not found in the data).

Other factions cite this section. Force Grey M3 (level 4) and M5 (level 6) use the same stat block and the same procedure.

### 5.1 Occupying Devourer

### Occupying Devourer

*Tiny Aberration, Lawful Evil*

**AC** 12 **Initiative** +2 (12)

**HP** 28 (8d4 + 8)

**Speed** 40 ft.

|            | MOD  | SAVE |            | MOD  | SAVE |            | MOD  | SAVE |
| :--------- | :--- | :--- | :--------- | :--- | :--- | :--------- | :--- | :--- |
| **Str 6**  | -2   | -2   | **Dex 14** | +2   | +2   | **Con 13** | +1   | +1   |
| **Int 14** | +2   | +2   | **Wis 11** | +0   | +0   | **Cha 10** | +0   | +0   |

**Skills** Perception +2, Stealth +4

**Resistances** Psychic

**Senses** Blindsight 60 ft., Passive Perception 12

**Languages** Understands Deep Speech but can't speak; telepathy 60 ft.

**CR** 2 (XP 450; PB +2)

#### Traits

***Detect Intelligence.*** The devourer magically senses the location of any creature within 300 feet of itself that has an Intelligence score of 3 or higher, regardless of interposing barriers.

***Occupation.*** While occupying a host, the devourer has Total Cover against attacks and other effects originating outside the host. It keeps its Intelligence, Wisdom and Charisma scores, its understanding of Deep Speech, its telepathy and its Detect Intelligence trait, and otherwise adopts the host's game statistics, including AC and Hit Points. Damage dealt to the body is dealt to the host. The devourer knows everything the host knew. The host's brain is not harmed: the host is aware but can't act, speak or cast spells. The devourer is forced out into the nearest unoccupied space within 5 feet when the host dies or when its Hold reaches 0.

***Hold.*** The devourer's Hold is 3 while it occupies a host. Each Break reduces Hold by 1 (see the Extraction Procedure). Hold returns to 3 one hour after the last Break.

#### Actions

***Multiattack.*** The devourer makes one Claw attack and uses Devour Intellect.

***Claw.*** *Melee Attack Roll:* +4, reach 5 ft. *Hit:* 7 (2d4 + 2) Slashing damage.

***Devour Intellect.*** *Intelligence Saving Throw:* DC 12, one creature the devourer can see within 5 feet. *Failure:* 11 (2d10) Psychic damage, and the target has the Stunned condition until the end of the devourer's next turn.

***Occupy Body.*** *Intelligence Saving Throw:* DC 12, one Small or Medium creature within 5 feet that has the Incapacitated condition, is a Humanoid or Beast, and has 10 Hit Points or fewer. *Failure:* The devourer enters the target's skull and occupies it without harming the brain (see Occupation). Its Hold becomes 3.

#### Bonus Actions

***Slip Out.*** The devourer leaves its host and appears in the nearest unoccupied space within 5 feet of it. The host is alive and has the Incapacitated condition until the end of its next turn.

### 5.2 Design notes (monster-designer method)

- **Concept.** A skirmisher-infiltrator that wears a person. It fights like the host and thinks like itself.
- **What was kept from XMM.** Every number: AC 12, 28 HP, speed 40, Blindsight 60, resists psychic, Claw +4 for 7, Devour Intellect DC 12 for 11 and a stun, Detect Intelligence 300 feet, Total Cover while inside, host statistics, host knowledge.
- **What was replaced.** Steal Body. The printed trait consumes the brain, and only *Wish* restores it. Occupy Body keeps the same target limits (Incapacitated, 10 HP or fewer, Small or Medium Humanoid or Beast, Intelligence DC 12) and drops the brain-eating. The printed "forced out when the host dies" stays.
- **What is new.** Hold (3) and Breaks give the party a way to force the devourer out without a single roll and without *Wish*. Slip Out replaces the printed "spend 5 feet of movement to leave" with a bonus action, because the host survives.
- **CR check.** Defensive: 28 HP lies on the CR 1 row (29). AC 12 is one below the CR 1 row (13), so about CR 1. Offensive: Claw 7 plus Devour Intellect 11 (half the time) is about 12 damage a round, between the CR 1 and CR 2 rows (10 and 17). Attack +4 is one below the CR 2 row. DC 12 matches it. The raw average is CR 1 to 1.5. The XMM block carries CR 2 on identical numbers because of the stun and the body-theft. The changes here do not alter any number, so CR 2 stands. Tier 1 Power 28, Tier 2 Power 23.
- **Sanity checks.** Does something every round: yes (Claw, Devour Intellect, or Occupy Body). Weakness: AC 12, 28 HP, no ranged option. Fun to run: the procedure below is the fun, and it is bounded.

### 5.3 Extraction Procedure

**Terms.** *Hold* is the devourer's grip, 3 at the start. A *Break* reduces Hold by 1. At Hold 0 the devourer is *expelled*. *Strain* is the psychic damage the host takes when an attempt fails. Breaks from every source add together. Hold returns to 3 one hour after the last Break.

**(a) Detection**

| Method | Check | Result |
|---|---|---|
| Eye contact and speech | DC 15 Wisdom (Insight) | The host's answers arrive a beat late and the eyes do not track. Something is wrong with the mind, not the story. |
| Fishing questions | DC 14 Wisdom (Insight) | The host asks about people and places in a way the real person would not. |
| Close study, 5 minutes | DC 12 Intelligence (Arcana) or Wisdom (Medicine) | No spell, no disease. The pupils lag. Something is riding in the skull. |
| *Detect Thoughts* | None | *Sense Thoughts* reveals two thinking minds in one head (one muffled). *Read Thoughts* gives the devourer's cover thought. Per the spell, the target learns it is being probed. **The devourer is alerted**: it acts at once (attack, Slip Out, or flee) and stops pretending. |
| *Detect Evil and Good* | None | XPHB: senses any Aberration within 30 feet. Ruling: it senses the devourer through the host's body. It does not alert the devourer. |

Each Insight or study check is one attempt per minute of contact. A failed check teaches the devourer nothing.

**(b) Forcing it out.** Any combination of the three routes works. Breaks stack and can come from different people in the same round.

**Before you start.**
- The host must be held: Restrained, Grappled, or Incapacitated without being killed. The devourer fights with the host's attacks and tries to Slip Out when Hold is 1.
- A touch spell needs a hand on the host. A free-moving host must be Grappled or Restrained; otherwise the caster makes an attack roll against the host's AC.
- The host's mind is willing. The devourer's refusal does not make the target unwilling for spells that require a willing creature.

**Route 1: Ward, then Contest of Wills.**
- *Protection from Evil and Good* (XPHB: Touch, 1 action, 10 minutes, Concentration, holy water worth 25+ gp consumed) is cast on the host. The spell lists Aberrations, says the target can't be possessed by them, and gives Advantage on new saves against existing possession.
- At the start of each of the host's turns while the ward lasts, the host makes a **DC 12 Intelligence saving throw with Advantage**. This is the contest: the host's will against the devourer's grip. A success is **1 Break**. A failure deals **Strain**.
- A host with Intelligence +1 (Corene) succeeds about 75% of the time. A host with +0 (Meloon) succeeds about 70%.
- Expected pace: four or five rounds for three Breaks. The caster must keep Concentration while the body fights. Damage forces a Constitution save.
- A warded host cannot be re-occupied. Casting the ward first is the safe order.

**Route 2: Magic that breaks magical hold.** One casting gives at most one Break (except *Greater Restoration*).

| Spell | Roll | Result | Failure cost |
|---|---|---|---|
| *Dispel Magic* (3rd-level slot) | The caster's spellcasting-ability check, **DC 14** | 1 Break. The Occupation counts as a 4th-level effect (DC 10 + 4). | Strain |
| *Dispel Magic* cast with a 4th-level or higher slot | None | Automatically 1 Break (XPHB: the slot's level ends a spell of equal or lower level). | None |
| *Remove Curse* | The devourer makes an **Intelligence save** (+2) against the caster's spell save DC | 1 Break on a failed save. | Strain on a successful save |
| *Greater Restoration* (5th level, diamond dust worth 100+ gp consumed) | None | **2 Breaks.** The Occupation is treated as a curse. | None |

Does not work:
- *Dispel Evil and Good*. XPHB lists Celestials, Elementals, Fey, Fiends and Undead for Break Enchantment. Aberrations are not on that list.
- *Banishment*, *Telekinesis* and any spell that must target the devourer. Total Cover blocks it. Banishing the host would banish Corene.
- *Remallia's list* (WDH): she has *Dispel Magic* and *Banishment* but no *Remove Curse* and no *Greater Restoration*. If Mirt calls her in, she can supply *Dispel Magic* (an automatic Break at 4th level). Cap her at one Break so the party still does the work.

**Route 3: Anchor and Charisma checks (no magic).**
- A helper stays within 5 feet and speaks to the host's buried mind. Each round the helper uses an action and makes a **Charisma (Persuasion) check**.
- The check is **DC 14 with an anchor** and **DC 18 without**. An anchor is something the host's mind clings to: a person she loves and trusts, a spoken oath, an object she touched daily. Deception does not work.
- A success is **1 Break**. A failure deals Strain.
- Advantage if the helper is the anchor and the host knows them. Disadvantage if the helper is a stranger shouting.
- **Surfacing.** When Hold drops to 1 by this route, the host's will surfaces for one sentence in her own voice, then goes under. Further anchor checks have Advantage. In play, read it aloud in the host's voice.
- Corene's anchors (suggested): her Harper pin, the cover name "Halla Ironstave" spoken as a question, and Dalen Voss if **Salon Guest Leads Recorded** and the party carries Saeth Cromley's account of him.

**Strain.**
- Every failed attempt costs the host **2d6 psychic damage** (average 7).
- Strain cannot exceed half the host's maximum HP (round up) per attempt and cannot reduce the host below 1 HP.
- At 1 HP, the next failure resets Hold to 3, the devourer digs in for 1 hour, and only *Greater Restoration* can earn Breaks until it passes.
- A host at 0 HP takes a failed death saving throw instead of Strain.

**Pace.** Alone, a ward takes four or five rounds, three castings of *Dispel Magic* take three rounds, and a patient anchor takes five or six. With all three running, expect two or three rounds.

**What the devourer does while it is worked on.** It controls the body. A Spy host attacks with Shortsword or Hand Crossbow. A Warrior Veteran host uses Greatsword twice and Parry. At Hold 1 the devourer Slips Out and runs (speed 40). If the host is warded, it cannot re-occupy her.

**When it is expelled.**
- It appears within 5 feet of the host at full HP. It is hostile, Tiny, 28 HP, AC 12.
- On its first turn it uses Occupy Body on the nearest eligible creature, **Intelligence save DC 12**. Eligible means Incapacitated, a Small or Medium Humanoid or Beast, and 10 HP or fewer. The freed host is eligible if Strain left her at 10 HP or fewer and she is Incapacitated. A warded host is immune.
- If nobody is eligible, it uses Devour Intellect on the nearest creature, Dashes and flees toward cover. It cannot speak. It reports to Nihiloor only by telepathy within 60 feet, and Detect Intelligence lets it find minds within 300 feet.
- The freed host has the Incapacitated condition until the end of her next turn.

**(c) Killing the host while it is occupied**
- The devourer has Total Cover while the host lives. Weapons and spells that target "it" cannot. Damage dealt to the body is dealt to the host.
- At 0 HP the host is Unconscious and dying under the usual death-saving-throw rules. The devourer stays inside. It cannot act (the body is unconscious) and can use Slip Out.
- Healing a 0-HP host above 0 wakes the body, and the devourer controls it again. Knocking the host out does not expel it. Extraction can proceed on a stabilised, unconscious host. Strain then counts as a failed death saving throw.
- If the host dies, the devourer is forced out within 5 feet at its full 28 HP, and acts on its next turn. The host is lost. Raising her needs *Raise Dead* or stronger. Corene Lost.
- If the devourer Slips Out of a dying host, the host is stable only if someone stabilises her. DC 10 Wisdom (Medicine).

**(d) Recovery**
- The freed host takes 1 level of Exhaustion and is shaken. She remembers the occupation as a long dream in which she saw and heard everything and could do nothing.
- Until a Long Rest she speaks in fragments. The DM gives one clear fact per hour on request. A Long Rest ends the Exhaustion level and returns her memory in full, including the occupation weeks and the four months before them.
- Strain damage heals as normal.
- A host who was left occupied for weeks (Corene) remembers what she saw and heard, but not what the devourer passed to Nihiloor by telepathy. Its telepathy reaches only 60 feet, so a hosted devourer reports through a Guild minder or courier who meets the host.

**If a PC is the host.** The player keeps awareness and plays the Contest of Wills rolls. The DM plays the body. The same procedure applies.

### 5.4 Audit: the expelled devourer and the hosted fight at level 6 (Tier 2)

Party Power 105 / 140 / 175. Budgets: Bruising 63 / 84 / 105; Bloody 78.75 / 105 / 131.25.

Monster Power (Tier 2): Occupying Devourer CR 2 = 23; Spy 17; Tough 12; Warrior Veteran 30.

| Roster | Power | 3 PCs (105) | 4 PCs (140) | 5 PCs (175) |
|---|---|---|---|---|
| Expelled devourer alone | 23 | 4.8% below Mild (2) | 2.7% below Mild (2) | 1.7% below Mild (2) |
| Corene hosted (Spy 17) + devourer (23), counted sequentially | 40 | 14.5% Mild (2) | 8.2% below Mild (2) | 5.2% below Mild (2) |

The devourer does not fight while it is hosted; the host does. The host's HP pool comes first. A devourer expelled after the host is wounded fights at full HP. Adding the two powers is conservative.

**Guild minders.** Nihiloor's plaza watchers tail Corene. Tough hold the street; a Warrior Veteran leads on a Hard day.

| PCs | Standard | Power | % lost | Hard | Power | % lost |
|---|---|---|---|---|---|---|
| 3 | Hosted Corene + devourer + 2 Tough | 64 | 37.2% (4) | + Spy minder | 81 | 59.5% (6) |
| 4 | Hosted Corene + devourer + 3 Tough | 76 | 29.5% (4) | + 3 Tough + Warrior Veteran | 106 | 57.3% (6) |
| 5 | Hosted Corene + devourer + 4 Tough | 88 | 25.3% (4) | + 4 Tough + Warrior Veteran | 118 | 45.5% (6) |

Day Cost: 4 Standard, 6 Hard. Extraction itself adds nothing (it is a scene, not a fight).

**Level 4 line (Force Grey M3, Tier 1).** Party Power 69 / 92 / 115. Powers (Tier 1): devourer 28; Warrior Veteran 37.

| Roster | Power | 3 PCs (69) | 4 PCs (92) | 5 PCs (115) |
|---|---|---|---|---|
| Expelled devourer alone | 28 | 16.5% Mild (2) | 9.3% below Mild (2) | 5.9% below Mild (2) |
| Meloon hosted (Warrior Veteran 37) + devourer (28) | 65 | 88.7% Oppressive (10) | 49.9% Bloody (6) | 31.9% Bruising (4) |

Verdict: the hosted Veteran is right for 4 PCs (Hard) and 5 PCs (Standard). At 3 PCs run it as a non-combat extraction (Vajra's ward and three 4th-level *dispel magic* casts are Force Grey Path 1) or start Meloon at half HP, which brings him to about 54 and 61.2% Brutal. Meloon's axe Azuredge is not in the numbers. If the host uses it as a combat weapon, treat the Veteran as CR 4 (Tier 1 Power 48), for a total of 76.

**Level 6 hosts for Force Grey M5.** Orvyn Dall's block is not in the data. If he is a Commoner (CR 0, 4 HP, Power 1), hosted plus devourer is 24: 5.2% / 2.9% / 1.9% (all below Mild). Strain then caps at 2 per attempt (half of 4), so the ward route is gentle on him.

### 5.5 Resolutions for the event writer

- **Extract.** Corene lives. She needs a Long Rest, then gives four months of Dock Ward intel.
- **Kill the host.** Corene Lost. The Guild goes to Alert at its Dock Ward sites for 14 days.
- **Leave in place.** The double-agent play. *Detect Thoughts* or a failed Insight-aloud spoils it, because the devourer is alerted.

### 5.6 Special CR warning

- The skill lists intellect devourers as HP-bypassing. The Occupying Devourer fixes the worst of it: the host's brain survives and the host can be saved.
- It still bypasses HP for an Incapacitated, 10-HP-or-fewer target. A PC at 0 HP qualifies. Rule: Nihiloor's devourers take hosts for his orders, not at random. They do not target downed PCs unless the scene says so.
- If a PC does become a host, the procedure above applies at once. No permanent loss.

## 6. M6 The Stone's Other Master (level 7, after Kolat Towers, Tier 2)

Party Power 123 / 164 / 205. Budgets: Bruising 73.8 / 98.4 / 123; Bloody 92.25 / 123 / 153.75. Monster Power (Tier 2): Mage CR 6 = 65 (CR 10 = 95 with the +4 rule); Tough Boss CR 4 = 38; Spy 17; Tough 12.

Stat blocks (XMM):
- **Mage** AC 15, 81 HP, Int save +6, Multiattack three Arcane Burst (+6, 16 force, melee or range 120). Spells (DC 14): at will *Detect Magic*, *Light*, *Mage Armor*, *Mage Hand*, *Prestidigitation*; 2/day *Fireball* (level 4 version) and *Invisibility*; 1/day *Cone of Cold* and *Fly*; *Misty Step* 3/day; Protective Magic 3/day (*Counterspell* or *Shield*). **There is no *Contingency***: the 2024 Mage has none, and nothing here adds it.
- **Tough Boss** AC 16, 82 HP, two attacks (Warhammer 12 with a 10-foot push, or Heavy Crossbow 13), Pack Tactics.
- **Spy** and **Tough** as above.

### The First-turn KO and the Stone plan

The Mage can KO on turn one: three bursts average 48, plus Fireball. At CR 10 (Power 95) the same rosters are much harder. This reference uses the Stone plan as a named modification that keeps the base figures honest:

- The leader spends round 1 on the Stone, not on bursts. That is the point of the raid.
- **Taking the Stone.**
  - An unattended Stone within 30 feet: the Mage casts *Mage Hand* (a Magic action, 30-foot range, up to 10 pounds) and the hand brings the Stone to him in the same action. He has it at once.
  - A Stone in a satchel or on a PC: a raider takes the Utilize action and makes an Athletics check contested by the holder. A Spy or Tough has no Athletics proficiency (Strength +0 or +2).
  - A Stone that a PC holds in hand: the raider must Grapple the holder first.
  - Whoever holds the Stone needs a bonus action Dash (Spy: Cunning Action) to get clear. **Stone Taken** when a raider with it leaves the building.
- **Covering the escape.** The Mage uses *Misty Step* (bonus action) and *Fly* (1/day) to leave once he holds it. A Spy can carry it out by Dashing.
- Unless the Stone is lost, the Mage opens round 1 on the Stone and starts his volleys from round 2. If a PC forces him to fight from round 1 (an ambush, a held door), apply the +4 figures below.

### Rosters (Hard, Bloody)

| PCs | Roster | Power | % lost | Mage opens with bursts (CR 10) | Power | % lost |
|---|---|---|---|---|---|---|
| 3 | Mage + Spy | 82 | 44.4% (6) | Mage + Spy | 112 | 82.9% Oppressive (10) |
| 4 | Mage + Tough Boss + Spy | 120 | 53.5% (6) | same | 150 | 83.6% Oppressive (10) |
| 5 | Mage + Tough Boss + 2 Spies + Tough | 149 | 52.8% (6) | same | 179 | 76.2% Brutal (8) |

Day Cost 6 on the base figures. A party that arrives hurt steps down one row (drop a Spy or Tough).

### Splinter survivors

- **What they are.** Spies and Toughs are survivors of the Splinter's Waterdeep cell. The Mage is the senior survivor and speaks for what is left of their master. GM text: if Kolat Towers left Manshoon alive, the Mage acts on his last orders. If it did not, the Mage acts on the Splinter's own orders. Neither is spoken aloud by the raiders.
- **Sending stone.** The Mage carries one stone of a matched pair. Plain description: a smooth grey stone that fits the palm. The holder touches it, speaks up to 25 words, and an answer comes back in the same minute. One message each way per day. The data I read has no 2024 item text for it; the XDMG sending-stone entry should be checked before the page cites it.
  - The Mage spends an action to send "Stone taken" or "Failed" as soon as the outcome is clear.
  - If the party takes it intact, it carries the reply. The voice is not one a member can place unless **Manshoon Named** is marked.
- **Threshold.**
  - The Mage retreats at 40 HP (half) if he holds the Stone, using *Misty Step* and *Fly*. Without the Stone he retreats at 40 HP and sends his message.
  - He surrenders if cornered at 20 HP or fewer. He gives up the stone and the cell's location in exchange for his life.
  - Spies disengage when two raiders are down or the Stone leaves the building. Toughs fight until the leader leaves, then surrender.
- **Non-combat route.** DC 16 Charisma (Persuasion or Intimidation) offers the leader safe passage for the Stone, once the raid has stalled. Insight DC 15 shows he does not want to die for this.

## 7. Rank allies

r10 and r50 are ally boons. Ally Power counts in full under the skill's rule, added to Party Power. Then rebuild the encounter from the allied Party Power.

### Mirt (r50, Tier 2)

Mirt is the WDH record (p.211), CR 9, AC 16, 153 HP. The block below is reformatted to 2024 style from that record. The numbers are unchanged.

### Mirt (Ally)

*Medium Humanoid (Human), Chaotic Good*

**AC** 16 **Initiative** +4 (14)

**HP** 153 (18d8 + 72)

**Speed** 30 ft.

|            | MOD  | SAVE |            | MOD  | SAVE |            | MOD  | SAVE |
| :--------- | :--- | :--- | :--------- | :--- | :--- | :--------- | :--- | :--- |
| **Str 18** | +4   | +4   | **Dex 18** | +4   | +8   | **Con 18** | +4   | +4   |
| **Int 15** | +2   | +2   | **Wis 12** | +1   | +5   | **Cha 15** | +2   | +2   |

**Skills** Acrobatics +8, Athletics +8, Perception +5, Persuasion +6, Stealth +8

**Gear** Bracers of Defense, Ring of Regeneration, +1 Longsword, +1 Dagger

**Senses** Passive Perception 15

**Languages** Common, Dwarvish

**CR** 9 (XP 5,000; PB +4)

#### Traits

***Brute.*** A melee weapon deals one extra die of its damage when Mirt hits with it (included in the attacks below).

***Evasion.*** If Mirt is subjected to an effect that allows a Dexterity saving throw to take only half damage, he instead takes no damage if he succeeds and only half damage if he fails. He can't use this trait if he has the Incapacitated condition.

***Sneak Attack (1/Turn).*** Mirt deals an extra 14 (4d6) damage when he hits a target with a weapon attack and has Advantage on the attack roll, or when the target is within 5 feet of an ally of Mirt's that doesn't have the Incapacitated condition and Mirt doesn't have Disadvantage on the attack roll.

#### Actions

***Multiattack.*** Mirt makes three attacks: two with his +1 Longsword and one with his +1 Dagger.

***+1 Longsword.*** *Melee Attack Roll:* +9, reach 5 ft. *Hit:* 14 (2d8 + 5) Slashing damage, or 16 (2d10 + 5) Slashing damage if used with two hands.

***+1 Dagger.*** *Melee or Ranged Attack Roll:* +9, reach 5 ft. or range 20/60 ft. *Hit:* 10 (2d4 + 5) Piercing damage in melee, or 7 (1d4 + 5) Piercing damage at range.

#### Reactions

***Parry.*** *Trigger:* Mirt is hit by a melee attack roll while holding a melee weapon. *Response:* Mirt adds 2 to his AC against that attack, possibly causing it to miss.

**Mirt's Power.** CR 9: **Tier 2 = 85**, Tier 3 = 70. The High-Power warning does not apply (85 is under twice a level-8 PC's 44, which is 88). His NF page names the block "Veteran with modifications"; the WDH record is the one used here.

### Spy ally Power

- r10 Perrin Valt ("Reed"): one Spy. Tier 1 Power 22, Tier 2 Power 17, Tier 3 Power 15.
- r50 team: three Spies, 51 at Tier 2, 45 at Tier 3. Wagon and a courier add no Power.

**r10: one Spy.** Renown 10 is reached after M3 or M4. Assume level 4 to 6.

| Level | Base (3 / 4 / 5 PCs) | + Spy | Bruising budget | Bloody budget |
|---|---|---|---|---|
| 4 | 69 / 92 / 115 | 91 / 114 / 137 (Spy 22) | 54.6 / 68.4 / 82.2 | 68.25 / 85.5 / 102.75 |
| 5 | 96 / 128 / 160 | 113 / 145 / 177 (Spy 17) | 67.8 / 87.0 / 106.2 | 84.75 / 108.75 / 132.75 |
| 6 | 105 / 140 / 175 | 122 / 157 / 192 (Spy 17) | 73.2 / 94.2 / 115.2 | 91.5 / 117.75 / 144 |

He arrives 24 hours after the request and is not counted in Party Power unless the Harper calls him into the fight.

**r50: Mirt and three Spies.** Level 8, Tier 2. Base 132 / 176 / 220.

| Package | Power | Party Power (3 / 4 / 5) | Bruising budget | Bloody budget |
|---|---|---|---|---|
| Three Spies | 51 | 183 / 227 / 271 | 109.8 / 136.2 / 162.6 | 137.25 / 170.25 / 203.25 |
| Mirt alone | 85 | 217 / 261 / 305 | 130.2 / 156.6 / 183 | 162.75 / 195.75 / 228.75 |
| Mirt + three Spies | 136 | 268 / 312 / 356 | 160.8 / 187.2 / 213.6 | 201 / 234 / 267 |

Tier 3 (level 11 and up): Mirt 70, three Spies 45, both 115.

### Ally Power notes

- Ally Power counts in full. Mirt alone adds about a third more to a 4-PC party (176 to 261).
- Rebuild the fight from the allied Party Power, or keep the fight at the base budget and let the ally act as a safety net.
- Mirt accompanies once, at 09:00, and does not fight in public against the Watch or a Lord. In a fight he withdraws at 50 HP (a third), which makes him contribute about 0.58 of his Power over a long fight. Treat that as a behaviour note.
- The three Spies are a disposable force. Expect one casualty per use.
- The wagon-and-three-Spies extraction is a non-combat resource and adds no Power unless the party must fight their way out.

## 8. 2024 name map

| Draft name | 2024 name used | CR | Note |
|---|---|---|---|
| Thug | **Tough** | 1/2 | XMM p.307. Pack Tactics, Mace 5, Heavy Crossbow 6. |
| Veteran (Mirt NF, Saeth NF) | **Warrior Veteran** | 3 | XMM p.320. Mirt uses the WDH CR 9 record instead. |
| Bard (Mattrim, Agorn) | **Performer** (CR 1/2) or **Performer Maestro** (CR 6) | 1/2 or 6 | XMM pp.236-237. Mattrim is not a combatant in the Harper pages. |
| Spy (Vell, Corene, Jalester, Perrin Valt, residents, field agents) | **Spy** | 1 | XMM p.295. |
| Doppelganger (Edric, Bonnie) | **Doppelganger** | 3 | XMM p.100. |
| Gazer | **Gazer** (converted here) | 1/2 | MPMM p.134; section 2.1. |
| Intellect Devourer (Nihiloor's) | **Occupying Devourer** (custom) | 2 | Section 5.1. XMM Intellect Devourer (CR 2) is the base. |
| Mind Flayer (Nihiloor) | **Mind Flayer** | 7 | XMM p.214. |
| Mage (Splinter leader) | **Mage** | 6 | XMM p.199. |
| Mage with modifications (Remallia) | **Remallia Haventree (WDH record)** | 9 | 13th-level wizard; has *Dispel Magic* and *Banishment*; no *Remove Curse*. |
| Tough Boss (Splinter sergeant) | **Tough Boss** | 4 | XMM p.307. |
| Scout (second BD guard) | **Scout** | 1/2 | XMM p.270. |
| Pirate Captain (Jarlaxle, ally block) | **Pirate Captain** | 6 | Not used here. Jarlaxle's WDH block is CR 15 per the brief. |
| Maxeene (draft horse, Int 10) | **Draft Horse** | 1/4 | XMM p.352. Non-combatant. |
| Uza, Orvel, Tessalar | **Commoner** | 0 | XMM p.77. |
| Guard (Remallia's gate) | **Guard** | 1/8 | XMM p.162. |
| Archmage (reference) | **Archmage** | 12 | XMM. Not used. |
| Vajra Safahr | **Vajra Safahr (WDH record)** | 13 | WDH p.217. Not used in a Harper fight. |

## Verification

Checked against the records in `harpers-creatures.json` and `spells-xphb.json`.

| Name / item | Status | Note |
|---|---|---|
| Spy, Doppelganger, Mage, Tough, Tough Boss, Warrior Veteran, Scout, Guard, Commoner | Verified (XMM) | CR 1, 3, 6, 1/2, 4, 3, 1/2, 1/8, 0. |
| Intellect Devourer | Verified (XMM) | CR 2, AC 12, 28 HP. Steal Body consumes the brain and only *Wish* restores it. Occupy Body is a custom replacement. |
| Gazer | Verified (VGM and MPMM) | Same numbers in both; CR 1/2; 2024 conversion is mine. Raw math lands between CR 1/4 and 1/2. |
| Mirt, Remallia, Vajra | Verified (WDH records) | Mirt CR 9, AC 16, 153 HP; Remallia CR 9, no *Remove Curse*; Vajra CR 13. |
| *Protection from Evil and Good* | Verified (XPHB) | 10 minutes, Concentration, holy water 25+ gp consumed, lists Aberrations, prevents possession, Advantage on new saves against existing possession. |
| *Dispel Magic* | Verified (XPHB) | Level 3 or lower ends; level 4+ needs a check at DC 10 + level; a higher slot ends spells of equal or lower level. |
| *Remove Curse* | Verified (XPHB) | Ends all curses on one creature. The Hold rule is mine. |
| *Greater Restoration* | Verified (XPHB) | Removes a curse, among other effects; diamond dust 100+ gp consumed. 2 Breaks is mine. |
| *Dispel Evil and Good* | Verified (XPHB) | Break Enchantment lists Celestials, Elementals, Fey, Fiends and Undead; Aberrations excluded. |
| *Detect Thoughts* | Verified (XPHB) | The target knows it is being probed. |
| *Detect Evil and Good* | Verified (XPHB) | Senses Aberrations within 30 feet. That it works through the host is a ruling. |
| *Mage Hand* | Verified (XPHB) | Range 30 feet, up to 10 pounds, Magic action to control and move 30 feet. Whether the Stone weighs 10 pounds or less is not stated in the data I read. |
| 2024 Mage | Verified | No *Contingency*. |
| Hold, Break, Strain, Contest of Wills, anchor DCs | **Mine** | Numbers and procedure are my design, not printed. |
| Stock rule (10 gp per strike, 100 gp cap) | **Mine** | Replaces the 2014 "miss" language. |
| Stone plan (grab and carry) | **Mine** | Named modification keeping the Mage's base Power. |
| Fillipa (2 HP) | **Unverified** | No Cat record in the data I read. 2 HP is an assumption. |
| Jarlaxle CR 15 | **Taken from the brief** | I could not read his WDH block in the data I was given. |
| Orvyn Dall block | **Unverified** | No Notable Figures page found. Commoner assumed for the Force Grey M5 line. |
| Sending stone (2024 item text) | **Unverified** | Not in the data. Plain description used: 25 words, one message each way per day. |
| Mirt "Veteran with modifications" (NF page) | Disagrees with WDH | The WDH record is used. |
| Wardragon's block | NF page | Warrior Veteran per the page; Azuredge not in the numbers. |
| Maxeene white blaze | Brief | Not a mechanical matter. |
