# Order of the Gauntlet Mechanics Reference (Session 45)

CR 2.0 audits for the six Order of the Gauntlet fights (M1 to M6), the ally rules, and the fixed rank-benefit tables. Modelled on `lords-alliance-mechanics-reference.md` (cited as **LA**) and `emerald-enclave-mechanics-reference.md` (**EE**). Every stat value below was read this session from `bestiary-xmm.json` (**XMM**), `spells-xphb.json` (**XPHB**) or `items.json` (**XDMG** entries unless stated) in the scratchpad `5e/` folder; the Verification section gives line ranges. Anything not read is marked "unverified". "Mine" marks a design choice of this reference, not a skill rule. Research reports are cited as **Rep 02/03/04**; the conversion brief as **Brief**.

## Method and conventions

- CR 2.0 only. % HP lost = (Enemy Power / Party Power) squared. Budget = Party Power x multiplier. Bands: Mild 0-20% (Day Cost 2), Bruising 20-40% (4), Bloody 40-60% (6), Brutal 60-80% (8), Oppressive 80-100% (10), Overwhelming 100-130% (13), Crushing 130-170% (17), Devastating 170-250% (25), Impossible 250-500% (50). **Standard = Bruising. Hard = Bloody.** The verdict is the band the percentage falls in; the budget is a guide, a roster up to about 5% over it is accepted, and a roster under it is fine if the band is right.
- Party Power from the level table (skill, Part I): L2 14, L3 18, L4 23, L5 32, L6 35, L7 41, L8 44, L9 49, L10 53, L11 62, L12 68. Budgets: Bruising x0.6, Bloody x0.75, Brutal x0.9.
- Monster Power from the tier-adjusted table (skill, Part II), never the flat table. Tier 1 = party level 1-4, Tier 2 = 5-10, Tier 3 = 11-16. Only the CRs used here:

| CR | 1/8 | 1/4 | 1/2 | 1 | 2 | 3 | 4 | 11 |
|---|---|---|---|---|---|---|---|---|
| Tier 1 | 4 | 10 | 16 | 22 | 28 | 37 | 48 | 140 |
| Tier 2 | 3 | 6 | 12 | 17 | 23 | 30 | 38 | 130 |
| Tier 3 | 3 | 5 | 7 | 15 | 19 | 25 | 32 | 105 |

- Each mission is built at its own level: M1 L2, M2 L3, M3 L4 (Tier 1); M4 L5, M5 L6, M6 L7 (Tier 2).
- Waves and separate rooms are separate encounters only if the party can rest or the noise does not carry; their Day Costs add (skill). Percentages of separate waves are never added.
- **Listed versus effective Power (mine, as EE and LA).** Power is the square root of HP x DPR, so a creature that leaves after losing a fraction f of its hit points contributes about the square root of f of its listed Power (leaving at half is 0.71). Verdicts use listed Power; effective figures appear as notes.
- Combatant counts include non-member companions. Bystanders, captives, residents, Pell and his companions, the household secretary, Orros, Watch officers and a surrendered creature are never counted.
- **First-turn KO ruling (stated once, applies to every Order fight).** Enemies spread their attacks (house tactic, user ruling, Session 45), so **the skill's +4 CR first-turn-KO adjustment is applied to no creature in M1 to M6**. The check below shows what each routine could do if it did focus, against a squishy PC (mine: d6 hit die, Con +2, average rolls: L2 14, L3 20, L4 26, L5 32, L6 38, L7 44 HP). "Spread" is operational (mine): each attack in a routine goes to a different creature when enough legal targets exist; if fewer targets than attacks, no more than two attacks go to one target.

| Creature (XMM) | Routine (verified) | Average if all hit | Maximum | Reading |
|---|---|---|---|---|
| Tough | one Mace 1d6+2, or Heavy Crossbow 1d10+1 | 6 | 11 | No KO |
| Bandit | one Scimitar 1d6+1, or Light Crossbow 1d8+1 | 5 | 9 | No KO |
| Giant Rat | one Bite 1d4+3 | 5 | 7 | No KO |
| Wererat | two attacks, one may be Bite 2d4+3 | 14 | 20 | No KO; curse is Con DC 11 and only matters at 0 HP |
| Imp | one Sting 1d6+3 plus 2d6 poison | 13 | 21 | Max roll equals an L3 squishy PC's HP (about 1 in 200 with a hit); no +4 |
| Spined Devil | two attacks, Fork 1d6+2 +1d6 fire, Tail Spine 1d4+2 +1d6 fire | 16 | 28 | No KO against L5 (32) |
| Cultist Fanatic | one Pact Blade 1d8+2 +2d6 necrotic, or a spell | 13 (crit 25) | 22 (crit 42) | Safeguard below for Hold Person |
| Bearded Devil | Beard 1d8+3, Infernal Glaive 1d10+3, wound 1d10 a turn | 15 | 24 (+10 a turn) | No KO against L6 (38) |
| Horned Devil | three attacks: Searing Fork 2d8+6 +2d8 fire, Hurl Flame 5d8+4 | 72 to 78 | 114 to 132 | **Would KO if focused.** Safeguard below; High-Power Warning |

- **Special CR warning.** The skill's HP-bypass list (shadow, intellect devourer, sea hag, banshee) has no member here. Two effects that act like it get stated safeguards (mine): **Hold Person** (Cultist Fanatic, 1/day, spell DC 12 Wis; 2024 spell text unverified) is her action, so she makes no Pact Blade attack the turn she casts it, and a held PC is attacked on her next turn at the earliest. **Wererat curse** (Bite, Con DC 11, verified): Kelso bites only in rat or hybrid form, never a creature already cursed, never a creature at 0 HP.
- **Horned Devil safeguards (mine).** Three attacks go to at least two creatures (never three on one); it uses Infernal Tail at most once a round; it never attacks a creature at 0 HP. Two Hurl Flames on one target would average 52 and could drop a squishy L7 (44), which is why the rule exists. Nothing here changes its Power.
- No creature used has resistance or immunity to nonmagical weapon damage (XMM reads: Wererat has none, Horned Devil has fire and poison immunity only), so the skill's -2 CR adjustment applies to none.
- Calendar: campaign year 1492 DR; spans in days or tendays.
## 1. Party Power and ally rules (Savra as a Knight ally; Priest Acolyte, Priests and Guards never counted unless they fight)

| Level | PC Power | 3 PCs | 4 PCs | 5 PCs | Bruising budget (3 / 4 / 5) | Bloody budget (3 / 4 / 5) |
|---|---|---|---|---|---|---|
| 2 | 14 | 42 | 56 | 70 | 25.2 / 33.6 / 42 | 31.5 / 42 / 52.5 |
| 3 | 18 | 54 | 72 | 90 | 32.4 / 43.2 / 54 | 40.5 / 54 / 67.5 |
| 4 | 23 | 69 | 92 | 115 | 41.4 / 55.2 / 69 | 51.75 / 69 / 86.25 |
| 5 | 32 | 96 | 128 | 160 | 57.6 / 76.8 / 96 | 72 / 96 / 120 |
| 6 | 35 | 105 | 140 | 175 | 63 / 84 / 105 | 78.75 / 105 / 131.25 |
| 7 | 41 | 123 | 164 | 205 | 73.8 / 98.4 / 123 | 92.25 / 123 / 153.75 |
| 8 | 44 | 132 | 176 | 220 | 79.2 / 105.6 / 132 | 99 / 132 / 165 |

### Ally Power rules (all Order allies)

1. **Only while it fights.** An ally adds Power only when it is in the fight. **Never counted:** Priest Acolyte couriers and the door-warden; Halls clerks and the armory's lay brother; Watch patrols and Guards; the r10 Scouts (they watch, they do not fight); the high priest of Tyr (non-combatant); the two Priests of Tyr in M6 unless they join the fight (section 7); Orros, Pell, the household secretary, residents and any surrendered creature.
2. **Counted in full, at the party's tier.** Ally Power is the tier-adjusted Power of its block at the party's level, added to Party Power; the fight is then built from the allied total (rosters in M4 and M6 do this). The alternative (EE) is to keep the fight at the base budget and let the ally be a reserve. Each scene says which.
3. **No +4 on allies.** The first-turn KO rule is for enemies (and is not applied to any Order enemy; see Method).
4. **Roster columns stay at PC count.** An ally is not a fourth or fifth PC.
5. **Withdrawal.** Savra withdraws at **20 HP** (Brief); every other Knight at **26 HP or fewer** (half of 52, mine); a Priest at 19 HP (half of 38, mine). Fighting to that point is about 0.71 of listed Power for a half-pool leaver; Savra at 20 of 52 HP has lost 32 and contributes sqrt(32/52) = 0.78 of listed Power.
6. **High-Power Warning.** An ally at twice any PC's Power or more is a reserve, not a damage dealer. The Knight at Tier 1 (37) trips it at level 2 (37 against 28) and level 3 (37 against 36) and not at level 4 (37 against 46). At Tier 2 the Knight is 30 against a level-5 PC's 32 and never trips it. **The enemy Horned Devil (130 against 82) trips it in M6.**
7. **Notice and limits** (days of notice, once per quest) live in the rank events, not here.

### Order ally Power (blocks in section 8)

| Ally | Block | CR | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|---|---|
| Savra, r25 Strike Team (three), r50 mobilization (six) | Knight | 3 | 37 | 30 | 25 |
| Priests of Tyr (M6, r50: two) | Priest | 2 | 28 | 23 | 19 |
| Courier, door-warden | Priest Acolyte | 1/4 | 10 | 6 | 5 |
| r10 surveillance team (two) | Scout | 1/2 | 16 | 12 | 7 |
| Watch patrol | Guard | 1/8 | 4 | 3 | 3 |

### Savra as a Knight ally: allied Party Power

At levels 2 and 3 Savra is a **reserve** (rule 6): do not add her. From level 4 she is counted in full when she fights. M4 and M6 script her fighting; r03 (Marcheon) lets the member ask for her once per quest.

| Level | Base (3 / 4 / 5) | Savra | Allied Party Power | Bruising budget | Bloody budget |
|---|---|---|---|---|---|
| 2 | 42 / 56 / 70 | reserve (37 if counted: 79 / 93 / 107) | base | 25.2 / 33.6 / 42 | 31.5 / 42 / 52.5 |
| 3 | 54 / 72 / 90 | reserve (37 if counted: 91 / 109 / 127) | base | 32.4 / 43.2 / 54 | 40.5 / 54 / 67.5 |
| 4 | 69 / 92 / 115 | +37 | 106 / 129 / 152 | 63.6 / 77.4 / 91.2 | 79.5 / 96.75 / 114 |
| 5 | 96 / 128 / 160 | +30 | 126 / 158 / 190 | 75.6 / 94.8 / 114 | 94.5 / 118.5 / 142.5 |
| 6 | 105 / 140 / 175 | +30 | 135 / 170 / 205 | 81 / 102 / 123 | 101.25 / 127.5 / 153.75 |
| 7 | 123 / 164 / 205 | +30 | 153 / 194 / 235 | 91.8 / 116.4 / 141 | 114.75 / 145.5 / 176.25 |
| 8 | 132 / 176 / 220 | +30 | 162 / 206 / 250 | 97.2 / 123.6 / 150 | 121.5 / 154.5 / 187.5 |
## 2. M1 Breaking Up the Brawl (level 2, Tier 1): Toughs and Bandits in the Field Ward, rosters at 3/4/5 PCs, target Bloody

Party Power 42 / 56 / 70. Budgets: Bloody 31.5 / 42 / 52.5. Tier 1 Power: Tough (CR 1/2) 16; Bandit (CR 1/8) 4.

**Tough (XMM p. 307, verified).** Small or Medium Humanoid, Neutral. CR 1/2, AC 12, HP 32 (5d8 + 10), Speed 30 ft., Str 15 Dex 12 Con 14. *Pack Tactics.* *Mace:* +4, reach 5 ft., 5 (1d6 + 2) bludgeoning. *Heavy Crossbow:* +3, range 100/400 ft., 6 (1d10 + 1) piercing. No Multiattack.

**Bandit (XMM p. 27, verified).** CR 1/8, AC 12, HP 11 (2d8 + 2), Speed 30 ft. *Scimitar:* +3, reach 5 ft., 4 (1d6 + 1) slashing. *Light Crossbow:* +3, range 80/320 ft., 5 (1d8 + 1) piercing.

Pell (Bandit) and his two companions guard Pell and take no part; they are not in the numbers. Neither is the dog or the crowd. The four paid hands are the roster.

| PCs | Roster | Roster Power | (E/P) squared | Band | Day Cost |
|---|---|---|---|---|---|
| 3 | 1 Tough + 3 Bandits | 16 + 12 = 28 | (28/42)^2 = 44.4% | **Bloody** | 6 |
| 4 | 2 Toughs + 2 Bandits | 32 + 8 = 40 | (40/56)^2 = 51.0% | **Bloody** | 6 |
| 5 | 3 Toughs + 1 Bandit | 48 + 4 = 52 | (52/70)^2 = 55.2% | **Bloody** | 6 |

- Four hands at every size (the source shape), with the weight moved from Bandits to Toughs as the party grows. Budgets: 28 against 31.5, 40 against 42, 52 against 52.5.
- **Why not four Toughs.** 64 Power is 232.2% (Devastating) at 3 PCs, 130.6% (Crushing) at 4 and 83.6% (Oppressive) at 5, so R's roster is unusable.
- **Break rule (mine).** The hands break and run when two of the four have fallen, or when the crowd turns on them (each Intimidation success already scored counts as one free round). Effective Power at that break (0.71 of listed): 19.9 / 28.4 / 36.9, which is 22.4% / 25.7% / 27.8% (Bruising). A pure show-of-force win is Mild.
- **Pack Tactics** counts any conscious ally of the Tough within 5 feet; the spread rule keeps the crossbow Bandits from stacking Advantage on one target.
- **First-turn KO:** none (Method table). No +4.
- **Non-combat route.** Three DC 12 Intimidation successes before three failures disperse the hands without a roll of initiative (event text).
## 3. M2 The Black Viper Investigation (level 3, Tier 1): guards at the tea house exit and the raven imp, rosters at 3/4/5 PCs

Party Power 54 / 72 / 90. Budgets: Bruising 32.4 / 43.2 / 54. Tier 1 Power: Tough 16; Bandit 4; Imp (CR 1) 22; Spy (CR 1) 22.

**Imp (XMM p. 177, verified).** Tiny Fiend (devil), Lawful Evil. CR 1, AC 13, HP 21 (6d4 + 6), Speed 20 ft., Fly 40 ft., Dex 17, Stealth +5, Darkvision 120 ft. (unimpeded by magical Darkness), Resistance cold, Immunity fire and poison, Poisoned. *Magic Resistance* (Advantage on saves against spells and magical effects). *Invisibility* (casts it on itself at will, as an action, no components). *Sting:* +5, reach 5 ft., 6 (1d6 + 3) piercing plus 7 (2d6) poison. *Shape-Shift:* rat (Speed 20), **raven (20 ft., Fly 60 ft.)** or spider (20 ft., Climb 20 ft.), or true form; statistics otherwise the same.

**Spy (XMM p. 295, verified)**, for the household secretary only if she is run down: CR 1, AC 12, HP 27 (6d8), Speed 30 ft., Climb 30 ft., *Shortsword* +4 5 plus 7 poison, *Hand Crossbow* +4 range 30/120 5 plus 7 poison, *Cunning Action* (bonus: Dash, Disengage, Hide). No Multiattack.

The guards are hired household hands, so **Tough** and **Bandit**, not Watch **Guards** (a Guard is CR 1/8, AC 16, HP 11, Spear +3 4, XMM p. 162, verified, and is the Watch patrol).

### The tea house exit (Day 2, highsun)

The secretary leaves by the kitchen on her first turn and is not counted. Her guards hold the door.

| PCs | Roster | Roster Power | (E/P) squared | Band | Day Cost |
|---|---|---|---|---|---|
| 3 | 2 Toughs | 32 | (32/54)^2 = 35.1% | **Bruising** | 4 |
| 4 | 2 Toughs + 2 Bandits | 32 + 8 = 40 | (40/72)^2 = 30.9% | **Bruising** | 4 |
| 5 | 3 Toughs + 1 Bandit | 48 + 4 = 52 | (52/90)^2 = 33.4% | **Bruising** | 4 |

- Budgets: 32 against 32.4, 40 against 43.2, 52 against 54.
- **Hold and break (mine).** The guards hold the door for three rounds; a real Watch patrol (two Guards) turns in at the **end of round 4**. They break when the secretary is out, or surrender if grappled. Effective Power at a half-pool break: 0.71 of listed.
- **If the secretary is run down** and fights as a Spy next to the guards: 3 PCs 2 Toughs + Spy = 54 (100%, Overwhelming); do not run it. Alone, the Spy is the same 22 as the Imp (below).

### The raven imp (Night 2)

A separate encounter on a separate night. The imp flies away when seen; it fights only if cornered (Tiny, AC 13, 21 HP).

| PCs | Roster | Roster Power | (E/P) squared | Band | Day Cost |
|---|---|---|---|---|---|
| 3 | 1 Imp | 22 | (22/54)^2 = 16.6% | **Mild** | 2 |
| 4 | 1 Imp | 22 | (22/72)^2 = 9.3% | **Mild** | 2 |
| 5 | 1 Imp | 22 | (22/90)^2 = 6.0% | **Mild** | 2 |

- If both encounters happen, Day Cost is 4 + 2 = 6 (Taxing).
- **First-turn KO:** none. Imp Sting maximum 21 (Method table); it never opens by fighting. No +4.
- **A held imp is still Invisible only if it cast Invisibility.** The spell ends when it attacks, deals damage or casts a spell (XPHB *Invisibility*, read in earlier sessions; text unverified this session). The raven form is not Invisible.
- **Combined, for reference only:** guards and imp together would be 54 / 62 / 74 against 54 / 72 / 90, which is 100.0% / 74.2% / 67.6% (Overwhelming / Brutal / Brutal). The day table keeps them apart.
## 4. M3 The Shard Shunners (level 4, Tier 1): Kelso (Wererat) with Giant Rats / a Tough / Brynn per DR m03 shape, target Bruising

Party Power 69 / 92 / 115. Budgets: Bruising 41.4 / 55.2 / 69. Tier 1 Power: Wererat (CR 2) 28; Giant Rat (CR 1/8) 4; Tough (CR 1/2) 16.

**Wererat (XMM p. 325, verified).** Small or Medium Monstrosity (lycanthrope), Lawful Evil. CR 2, AC 13, HP 60 (11d8 + 11), Speed 30 ft., Climb 30 ft., Dex 16, Perception +4, Stealth +5, Darkvision 60 ft. **No resistances, no immunities, no Regeneration, no silver rule** (the 2014 text is gone). *Multiattack:* two attacks, using Scratch or Hand Crossbow in any combination; it can replace one attack with a Bite. *Bite (Rat or Hybrid Form Only):* +5, reach 5 ft., 8 (2d4 + 3) piercing; a Humanoid target makes a Con DC 11 save or is cursed (if the cursed target drops to 0 HP it becomes a Wererat under the DM's control with 10 HP; on a success it is immune to this wererat's curse for 24 hours). *Scratch:* +5, reach 5 ft., 6 (1d6 + 3) slashing. *Hand Crossbow (Humanoid or Hybrid Form Only):* +5, range 30/120 ft., 6 (1d6 + 3) piercing. *Shape-Shift (bonus action):* Medium rat-humanoid hybrid, Small rat, or true humanoid form.

**Giant Rat (XMM p. 358, verified).** Small Beast, Unaligned. CR 1/8, AC 13, HP 7 (2d6), Speed 30 ft., Climb 30 ft., Dex 16, Darkvision 60 ft., Perception +2. *Pack Tactics.* *Bite:* +5, reach 5 ft., 5 (1d4 + 3) piercing. **Tough** as in section 2.

Kelso Fiddlewick is the Wererat in halfling form. **Brynn Hilltopple** (Kelso's second, from the DR m03 shape per Rep 03; name not re-checked) is a second Wererat. Both stay in halfling form until a Shunner drops, then shift to hybrid for the Bite.

| PCs | Roster | Roster Power | (E/P) squared | Band | Day Cost |
|---|---|---|---|---|---|
| 3 | Kelso + 2 Giant Rats | 28 + 8 = 36 | (36/69)^2 = 27.2% | **Bruising** | 4 |
| 4 | Kelso + Brynn | 28 + 28 = 56 | (56/92)^2 = 37.1% | **Bruising** | 4 |
| 5 | Kelso + Brynn + 1 Tough | 28 + 28 + 16 = 72 | (72/115)^2 = 39.2% | **Bruising** | 4 |

- Budgets: 36 against 41.4, 56 against 55.2 (+1.4%), 72 against 69 (+4.3%, inside the 5% allowance).
- **Softer five-PC option:** Kelso + Brynn + 2 Giant Rats = 64, which is (64/115)^2 = 31.0% Bruising.
- **Not allowed:** Kelso + Brynn at 3 PCs is 56 against 69, which is 65.9% (Brutal). R's three Wererats are 84 Power: 148.2% (Crushing) at 3 PCs, 83.4% (Oppressive) at 4, 53.3% (Bloody) at 5.
- **End condition (mine).** The fight ends when a Shunner has fallen and Kelso is offered terms (DC 15 Charisma (Persuasion), DR m03 text), when Kelso is at 30 HP or fewer (half of 60: he yields, "That's enough, partner"), or at the end of round 4, when a Watch patrol turns in. Effective Power at the half-pool yield: Kelso 0.71 x 28 = 19.9.
- **Curse safeguard (Method).** Kelso and Brynn bite only in rat or hybrid form, never a cursed creature and never a creature at 0 HP. Bites are the replaceable half of Multiattack, so a Wererat's turn is one Bite and one Scratch or Hand Crossbow at most.
- **First-turn KO:** none (Method table: 20 maximum against L4 squishy 26). No +4.
- **Kelso is not a Splinter agent** (Brief); the roster has no Splinter members.
## 5. M4 Twelvedog Court (level 5, Tier 2): Spined Devils and Gysheer (Cultist Fanatic) with Savra as a Knight ally; Standard and Hard

Party Power 96 / 128 / 160. **Savra counted in full as a Knight ally (Tier 2 Power 30): allied Party Power 126 / 158 / 190.** Budgets (allied): Bruising 75.6 / 94.8 / 114; Bloody 94.5 / 118.5 / 142.5. Tier 2 Power: Spined Devil (CR 2) 23; Cultist Fanatic (CR 2) 23; Knight (CR 3) 30.

**Spined Devil (XMM p. 296, verified).** Small Fiend (devil), Lawful Evil. CR 2, AC 13, HP 45 (10d6 + 10), Speed 20 ft., Fly 40 ft., Dex 15, Darkvision 120 ft. (unimpeded by magical Darkness), Resistance cold, Immunity fire and poison, Poisoned. *Flyby* (no Opportunity Attack when it flies out of reach). *Magic Resistance.* *Multiattack:* two attacks, using Infernal Fork and Tail Spine in any combination. *Infernal Fork:* +4, reach 5 ft., 5 (1d6 + 2) piercing plus 3 (1d6) fire. *Tail Spine:* +4, range 20/80 ft., 4 (1d4 + 2) piercing plus 3 (1d6) fire. **There is no Hurl Spine and no poison on a hit.**

**Cultist Fanatic (XMM p. 85, verified), used for Gysheer Omfreys.** Small or Medium Humanoid, Neutral. CR 2, AC 13, HP 44 (8d8 + 8), Speed 30 ft., Wis 14 Cha 13, Wis save +4, Deception +3 Persuasion +3 Religion +2. *Spellcasting* (Wisdom, save DC 12, +4 to hit, action): at will *Light*, *Thaumaturgy*; 1/day *Hold Person*; 2/day *Command*. *Spiritual Weapon* (2/day, bonus action). *Pact Blade:* +4, reach 5 ft., 6 (1d8 + 2) slashing plus 7 (2d6) necrotic. No Multiattack.

**Knight (XMM p. 184, verified), used for Savra Belabranta.** Small or Medium Humanoid, Neutral. CR 3, AC 18, HP 52 (8d8 + 16), Speed 30 ft., Str 16 Con 14 Cha 15, saves Con +4 Wis +2, immune to Frightened. *Multiattack:* two attacks, using Greatsword or Heavy Crossbow in any combination. *Greatsword:* +5, reach 5 ft., 10 (2d6 + 3) slashing plus 4 (1d8) radiant. *Heavy Crossbow:* +2, range 100/400 ft., 11 (2d10) piercing plus 4 (1d8) radiant. *Parry (reaction):* +2 AC against a melee hit while holding a weapon. She withdraws at 20 HP.

### The court (Standard and Hard)

The three residents pinned behind the cart are bystanders and are never counted. Savra stands with the party.

| PCs | Standard roster | Power | (E/P) squared | Band | Day Cost | Hard roster | Power | (E/P) squared | Band | Day Cost |
|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 3 Spined Devils | 69 | (69/126)^2 = 30.0% | **Bruising** | 4 | 4 Spined Devils | 92 | (92/126)^2 = 53.3% | **Bloody** | 6 |
| 4 | 4 Spined Devils | 92 | (92/158)^2 = 33.9% | **Bruising** | 4 | 5 Spined Devils | 115 | (115/158)^2 = 53.0% | **Bloody** | 6 |
| 5 | 5 Spined Devils | 115 | (115/190)^2 = 36.6% | **Bruising** | 4 | 6 Spined Devils | 138 | (138/190)^2 = 52.8% | **Bloody** | 6 |

- Rule of thumb: one Spined Devil a PC on Standard, one more on Hard. Budgets: Standard 69 / 92 / 115 against 75.6 / 94.8 / 114 (the 5-PC roster is 0.9% over); Hard 92 / 115 / 138 against 94.5 / 118.5 / 142.5.
- **Use Hard** when **Planted Story Exposed** is not marked (the handlers' lookouts are not thinned), or when the Cassalanter household is at Alert or Lockdown. Otherwise Standard (mine).
- **Without Savra** (she is held back or falls early): Standard is 51.7% at every size (Bloody); Hard is 91.8% / 80.7% / 74.4% (Oppressive / Oppressive / Brutal). **If she withdraws at 20 HP** her effective Power is 30 x 0.78 = 23.5, allied Power 119.5 / 151.5 / 183.5, and Standard is 33.3% / 36.9% / 39.3% (still Bruising).
- **Gysheer, a separate wave** (she arrives after the last devil falls, with a knife): one Cultist Fanatic, 23. (23/126)^2 = 3.3%, (23/158)^2 = 2.1%, (23/190)^2 = 1.5%: **Mild** at every size, Day Cost 2. **Mission Day Cost 6 (Standard + Gysheer) or 8 (Hard + Gysheer).** If she joins the devils instead, add 23 to the roster: Standard becomes 92 / 115 / 138, which is 53.3% / 53.0% / 52.8% (Bloody, Hard's numbers).
- **Gysheer's safeguard.** *Hold Person* is her action: no Pact Blade that turn. She opens with Pact Blade or *Spiritual Weapon* and holds *Hold Person* for a target Savra or an ally cannot reach in a turn. She is taken alive; she yields at 22 HP or fewer (half of 44) or when held.
- **Devil tactics (Flyby, range).** Devils fly 40 ft. and use Tail Spine (range 20/80) from rooflines; Flyby lets them leave reach without an Opportunity Attack. "Prefers range" is a positioning choice, not a trait (unverified that the block implies it).
- **First-turn KO:** none (Spined Devil maximum 28 against L5 squishy 32, and the devils spread). No +4. **High-Power Warning:** none (23 against 32).
- **Non-combat exit:** none needed; a party that retreats leaves the residents (the Brief reads this only for the +1 line).
## 6. M5 The Shrine on Aveen Street (level 6, Tier 2): Bearded Devil, Cultist Fanatics, an Imp in a trimmed two-room roster; Standard and Hard

Party Power 105 / 140 / 175. **No Savra** (she cannot enter a private shrine, Brief). Budgets: Bruising 63 / 84 / 105; Bloody 78.75 / 105 / 131.25. Tier 2 Power: Bearded Devil (CR 3) 30; Cultist Fanatic (CR 2) 23; Imp (CR 1) 17.

**Bearded Devil (XMM p. 33, verified).** Medium Fiend (devil), Lawful Evil. CR 3, AC 13, HP 58 (9d8 + 18), Speed 30 ft., Str 16 Dex 15 Con 15, saves Str +5 Con +4 Cha +4, Darkvision 120 ft. (unimpeded by magical Darkness), Resistance cold, Immunity fire and poison, Poisoned, Frightened. *Magic Resistance.* **No Diabolical Restoration, no grapple, no "Cursed".** *Multiattack:* one Beard attack and one Infernal Glaive attack. *Beard:* +5, reach 5 ft., 7 (1d8 + 3) piercing, and the target is Poisoned until the start of the devil's next turn and **can't regain Hit Points** until that poison ends. *Infernal Glaive:* +5, reach 10 ft., 8 (1d10 + 3) slashing; a creature without an infernal wound makes a **Con DC 12** save or receives one: it loses 5 (1d10) HP at the start of each of its turns; the wound closes after 1 minute, after a spell restores HP to the target, or when the target or a creature within 5 feet takes an action to stanch it with a **DC 12 Wisdom (Medicine)** check.

**Cultist Fanatic** and **Imp**: section 5 and section 3. The Imp is the invisible sentry at the circle (casts *Invisibility* on itself as an action; its first act on seeing intruders is to do so and leave).

### Two rooms (mine)

- **Room 1, the cellar stair room:** Cultist Fanatic(s), the chandler's key-holders.
- **Room 2, the circle room:** the Bearded Devil (bound to the perimeter) and the Imp (3 PCs Standard has no Imp).

If the door between them is open, or a fight carries sound through it, the two rooms are one encounter. If the party closes the door and clears Room 1 quietly, they are two.

| PCs | Standard roster (Room 1 / Room 2) | Power | (E/P) squared | Band | Day Cost | Hard roster | Power | (E/P) squared | Band | Day Cost |
|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 1 CF / Bearded Devil | 23 + 30 = 53 | (53/105)^2 = 25.5% | **Bruising** | 4 | 1 CF / Bearded Devil + Imp | 70 | (70/105)^2 = 44.4% | **Bloody** | 6 |
| 4 | 1 CF / Bearded Devil + Imp | 23 + 30 + 17 = 70 | (70/140)^2 = 25.0% | **Bruising** | 4 | 2 CF / Bearded Devil + Imp | 93 | (93/140)^2 = 44.1% | **Bloody** | 6 |
| 5 | 2 CF / Bearded Devil + Imp | 46 + 30 + 17 = 93 | (93/175)^2 = 28.2% | **Bruising** | 4 | 3 CF / Bearded Devil + Imp | 116 | (116/175)^2 = 43.9% | **Bloody** | 6 |

CF = Cultist Fanatic. Budgets: Standard 53 / 70 / 93 against 63 / 84 / 105 (under); Hard 70 / 93 / 116 against 78.75 / 105 / 131.25 (under). Both bands are right, which is what governs.

**Per room, if the rooms are separate encounters** (Day Costs add):

| PCs | Setting | Room 1 | (E/P) squared | Room 2 | (E/P) squared | Day Cost |
|---|---|---|---|---|---|---|
| 3 | Standard | 23 | 4.8% Mild | 30 | 8.2% Mild | 2 + 2 = 4 |
| 3 | Hard | 23 | 4.8% Mild | 47 | 20.0% Bruising | 2 + 4 = 6 |
| 4 | Standard | 23 | 2.7% Mild | 47 | 11.3% Mild | 2 + 2 = 4 |
| 4 | Hard | 46 | 10.8% Mild | 47 | 11.3% Mild | 2 + 2 = 4 |
| 5 | Standard | 46 | 6.9% Mild | 47 | 7.2% Mild | 2 + 2 = 4 |
| 5 | Hard | 69 | 15.5% Mild | 47 | 7.2% Mild | 2 + 2 = 4 |

Arithmetic: (23/105)^2 = 4.8%, (30/105)^2 = 8.2%, (47/105)^2 = 20.04%; (23/140)^2 = 2.7%, (47/140)^2 = 11.3%, (46/140)^2 = 10.8%; (46/175)^2 = 6.9%, (47/175)^2 = 7.2%, (69/175)^2 = 15.5%. Cleared in two sittings the cost is lower than the single Bloody fight, because the party can rest between rooms. That is the reward for the quiet entry.

- **Use Hard** if the party broke the cellar door instead of using Orros's key or the priest's inspection, if Orros was alarmed, or if the Cassalanter household is at Alert or Lockdown. Otherwise Standard (mine).
- **Imp escape.** The Imp flees to report if it is not killed or held; if it escapes, mark **Cassalanters Alerted** (Brief). At 3 PCs on Standard there is no Imp, so the Alert comes from the filing alone.
- **Break and yield (mine).** The Bearded Devil is bound to the perimeter and fights to 0 HP. A Cultist Fanatic yields at 22 HP or fewer (half of 44) or when held. The Devil's Poisoned Beard (no HP regained) and infernal wound (5 a turn, DC 12 Medicine to stanch) are the cost; the party's healing is cut while Beard poison lasts.
- **First-turn KO:** none (Bearded Devil maximum 24 against L6 squishy 38; Cultist Fanatic *Hold Person* safeguard in Method). No +4. **High-Power Warning:** none (30 against 35).
- **Non-combat route:** Orros's key and the priest-witnessed inspection get the party into Room 2 with the Devil still bound; the Devil does not leave the perimeter (event text).
## 7. M6 The Writ and the Weight (level 7, Tier 2): Horned Devil (CR 11, Power 130) with Savra fighting as a Knight ally; Standard and Hard; High-Power Warning; escorts only if needed; Banishment odds (scroll DC 15 or 17, or a PC's action)

Party Power 123 / 164 / 205. **Savra counted in full as a Knight ally (30): allied Party Power 153 / 194 / 235.** Tier 2 Power: Horned Devil (CR 11) **130**; Priest (CR 2) 23; Imp (CR 1) 17; Bearded Devil (CR 3) 30.

**Horned Devil (XMM p. 174, verified).** Large Fiend (devil), Lawful Evil. **CR 11**, AC 18, HP 199 (19d10 + 95), Speed 30 ft., Fly 60 ft., Str 22 Dex 17 Con 21 Int 12 Wis 16 Cha 18, saves Str +10 Dex +7 Wis +7 **Cha +8**, Darkvision 150 ft. (unimpeded by magical Darkness), Immunity fire and poison, Poisoned. **No other resistances; no Battle Frenzy.** *Diabolical Restoration:* if it dies outside the Nine Hells its body disappears in sulfurous smoke and it revives with all its HP somewhere in the Nine Hells. *Magic Resistance:* Advantage on saving throws against spells and other magical effects. *Multiattack:* three attacks, using Searing Fork or Hurl Flame in any combination; it can replace one attack with Infernal Tail. *Searing Fork:* +10, reach 10 ft., 15 (2d8 + 6) piercing plus 9 (2d8) fire. *Hurl Flame:* +8, range 150 ft., 26 (5d8 + 4) fire; a flammable object that isn't worn or carried starts burning. *Infernal Tail:* Dex DC 17, one creature within 10 ft.: 10 (1d8 + 6) necrotic and an infernal wound (loses 10 (3d6) HP at the start of each turn; closes after 1 minute, after a spell restores HP, or on a **DC 17 Wisdom (Medicine)** check).

**Priest (XMM p. 248, verified), used for the two Priests of Tyr.** Small or Medium Humanoid (cleric), Neutral. CR 2, AC 13, HP 38 (7d8 + 7), Speed 30 ft., Wis 16, Medicine +7 Perception +5 Religion +5. *Spellcasting* (Wisdom): at will *Light*, *Thaumaturgy*; 1/day *Spirit Guardians*. *Divine Aid* (3/day, bonus action): *Bless*, *Dispel Magic*, *Healing Word* or *Lesser Restoration*. *Multiattack:* two attacks, using Mace or Radiant Flame. *Mace:* +5, reach 5 ft., 6 (1d6 + 3) bludgeoning plus 5 (2d4) radiant. *Radiant Flame:* +5, range 60 ft., 11 (2d10) radiant. **No *Banishment* and no 5th-level slots.** The Brief's Priests only stabilize Savra if she falls; a Priest whose action is *Healing Word* or Medicine is not fighting.

### High-Power Warning

The Horned Devil is Power 130 against a level-7 PC's 41. It is 3.2 times a PC and trips the skill's warning (2x). It cannot be a "fair fight" by squad; it is the table's one monster that can remove a PC in a single exchange if its attacks pile up. The warning is answered four ways: Savra and the Priests; the three-attack spread rule (Method); the Hard/Standard split below; and a non-combat option (Banishment, below) that the table can try. **The warning is stated in the hazard block of the event.**

### Rosters (Standard and Hard)

The lone devil is the floor: nothing in this section lowers its Power, so Standard (Bruising) is reachable only where the allied party is large enough. Escorts are added only to reach Hard.

**Setup A:** the devil against the party and Savra, the Priests in the rear (not counted). **Setup B:** the same, and both Priests fight (counted in full, +46). **Setup C:** Setup A plus two Imps (the writ's clerks).

| PCs | Setup A: Party Power | (130/PP) squared | Band | Day Cost | Setup B: Party Power | (130/PP) squared | Band | Day Cost |
|---|---|---|---|---|---|---|---|---|
| 3 | 153 | 72.2% | **Brutal** | 8 | 199 | 42.7% | **Bloody** | 6 |
| 4 | 194 | 44.9% | **Bloody** | 6 | 240 | 29.3% | **Bruising** | 4 |
| 5 | 235 | 30.6% | **Bruising** | 4 | 281 | 21.4% | **Bruising** | 4 |

Arithmetic: (130/153)^2 = 0.722; (130/194)^2 = 0.449; (130/235)^2 = 0.306; (130/199)^2 = 0.427; (130/240)^2 = 0.293; (130/281)^2 = 0.214.

**The two bands, by size:**

| PCs | Standard (Bruising) | Hard (Bloody) | Allied Party Power | Budgets (Bruising / Bloody) |
|---|---|---|---|---|
| 3 | **Not reachable.** The lone devil with Savra and both Priests fighting is 42.7% (Bloody). | Setup B: devil only, Savra and both Priests fight: 130 against 199 = **42.7% Bloody**, Day Cost 6 | 199 | 119.4 / 149.25 |
| 4 | Setup B: devil only, Savra and both Priests fight: 130 against 240 = **29.3% Bruising**, Day Cost 4 | Setup A: devil only, Savra fights: 130 against 194 = **44.9% Bloody**, Day Cost 6 | 240 (B) / 194 (A) | 144 / 180 (B); 116.4 / 145.5 (A) |
| 5 | Setup A: devil only, Savra fights: 130 against 235 = **30.6% Bruising**, Day Cost 4 | Setup C: devil + 2 Imps, Savra fights: 164 against 235 = **48.7% Bloody**, Day Cost 6 | 235 | 141 / 176.25 |

- **Escorts are needed only at 5 PCs, Hard.** Two Imps add 34: (164/235)^2 = 48.7% (Bloody), 164 against a Bloody budget of 176.25. An alternative escort is one Bearded Devil (section 6), 160 against 235 = 46.4% Bloody. At 3 and 4 PCs the lone devil already sits in or above the Hard band.
- **At 3 PCs the plain Setup A roster (the Priests in the rear) is Brutal (72.2%, Day Cost 8), above Hard.** Do not run it; either the Priests fight (Setup B) or the table accepts Brutal.
- **Without Savra** (not an intended branch; she is present by design): 111.7% (Overwhelming) / 62.8% (Brutal) / 40.2% (Bloody) at PP 123 / 164 / 205. **If Savra withdraws at 20 HP** her effective Power is 23.5, allied Power 146.5 / 187.5 / 228.5, and the lone devil is 78.7% / 48.1% / 32.4%.
- **Use Hard** when the Cassalanter Villa result is **Cassalanters Exposed** (the default if not run), when the Cassalanters were at Lockdown, or when the party opens the fight. Otherwise Standard (mine).
- **The wards (mine, no Power change).** A way to bring the Halls' wards to bear shortens the fight (the devil takes the rounds to reach the cabinet); the event states it as a position, not as a modifier to the math.
- **Priests stabilize Savra** if she drops to 0: the Priests' action, not a Power term. Stabilizing rules text (2024 *Stable*, Medicine DC) is unverified here.
- **First-turn KO:** the Horned Devil could KO on turn one if it focused (Method table: 114 to 132 maximum), so the three-attack spread rule is the safeguard; **no +4 is applied** (house tactic). Escort Imps and the Bearded Devil add no KO risk.
- **Sent back, not destroyed.** At 0 HP the devil's *Diabolical Restoration* returns it to the Nine Hells with all its HP (**Devil Sent Back**). It also counts as sent back if Banishment holds for a full minute.

### Banishment odds (the Brief's option: not the plan)

*Banishment* is **level 4**, action, range 30 feet, V S M (a pentacle), concentration up to 1 minute (XPHB, verified). One creature makes a **Charisma saving throw** or is transported to a harmless demiplane for the duration, Incapacitated; **a Fiend that is still banished when the spell lasts for 1 minute does not return** and is transported to a random location on a plane associated with its type. Higher slots add one target per level above 4.

The Horned Devil's save is **Cha +8** (verified) and it has **Magic Resistance** (Advantage on saves against spells). It fails if its total is below the DC, so it fails on a d20 roll of DC minus 9 or less; with Advantage both dice must fail.

| Source | DC | Fails on a roll of | One die | **Chance one cast lands (Advantage: both dice)** | Two casts | Three casts |
|---|---|---|---|---|---|---|
| Level 4 Spell Scroll (rare, XDMG) | **15** | 6 or less | 30% | **9.0%** | 17.2% | 24.6% |
| Level 5 Spell Scroll (rare, XDMG) | **17** | 8 or less | 40% | **16.0%** | 29.4% | 40.7% |
| A level-7 PC casting it, spell DC 14 (8 + proficiency 3 + mod 3) | 14 | 5 or less | 25% | 6.3% | 12.1% | 17.6% |
| A level-7 PC, DC 15 (mod +4) | 15 | 6 or less | 30% | 9.0% | 17.2% | 24.6% |
| A level-7 PC, DC 16 (mod +5) | 16 | 7 or less | 35% | 12.3% | 23.0% | 32.4% |

Arithmetic: chance = (p)^2 with p = (DC - 9) / 20 (fail needs total below DC, so roll at most DC - 9); two casts = 1 - (1 - chance)^2; three casts = 1 - (1 - chance)^3. 0.3^2 = 0.09; 0.4^2 = 0.16; 0.25^2 = 0.0625; 0.35^2 = 0.1225. Scroll DCs are from the scroll text (Level 4: DC 15, +7; Level 5: DC 17, +9; both verified).

- **A landed cast is not a win yet.** The caster must keep concentration for the full 10 rounds. The devil is out of the fight meanwhile, and a banished Fiend that stays gone counts as sent back.
- **A level-7 PC with a spell DC of 17 is not possible by level** (8 + 3 + 5 = 16 is the ceiling without items). The scroll at DC 17 is the best single try.
- **Banishment is on a PC's list only if the class has it** (class lists are not in the downloaded files; unverified).
- **Reading:** the best realistic try, a level 5 scroll, lands one time in six. The Brief is right to call it a chance, not a plan. Do not build the fight around it.
## 8. Allies: Savra (Knight), r03 accompaniment, r25 Strike Team (three Knights), r50 mobilization (six Knights, two Priests), Priest Acolyte, Scout; withdrawal HP and ally Power by tier
## 9. Fixed tables: r03 temple briefings and armory; r10 Uncommon item table (from items.json), potions, 2nd-level spell list, Savra-at-the-lairs table; r25 six-target findings table and +1 weapon table; s01 worthy causes; r50 Knighthood credential
## Verification (line ranges in the data files)
