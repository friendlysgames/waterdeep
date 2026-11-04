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

Ally Power rules are in section 1. Blocks: **Knight** (section 5), **Priest** (section 7), **Guard** (section 3).

**Priest Acolyte (XMM p. 247, verified).** Small or Medium Humanoid (cleric), Neutral. CR 1/4, AC 13, HP 11 (2d8 + 2), Speed 30 ft., Wis 14, Medicine +4 Religion +2. *Spellcasting* (Wisdom): at will *Light*, *Thaumaturgy*; *Divine Aid* (1/day, bonus action): *Bless*, *Healing Word* or *Sanctuary*. *Mace:* +4, reach 5 ft., 5 (1d6 + 2) bludgeoning plus 2 (1d4) radiant. *Radiant Flame:* +4, range 60 ft., 7 (2d6) radiant. No Multiattack. **Role: the courier** in a plain grey surcoat. Not counted; Tier 1 Power 10, Tier 2 6.

**Scout (XMM p. 270, verified).** Small or Medium Humanoid, Neutral. CR 1/2, AC 13, HP 16 (3d8 + 3), Speed 30 ft., Dex 14, Nature +4 Perception +5 Stealth +6 Survival +5. *Multiattack:* two attacks, using Shortsword and Longbow in any combination. *Shortsword:* +4, reach 5 ft., 5 (1d6 + 2) piercing. *Longbow:* +4, range 150/600 ft., 6 (1d8 + 2) piercing. **Role: r10 surveillance, two Scouts for three days.** Not counted (they watch). If they do fight: Tier 1 16, Tier 2 12, Tier 3 7 each; withdraw at 8 HP.

### r03 Marcheon: Savra at your side

One operation per quest, asked by the member; she answers in a day, and she refuses an operation she believes will get the party killed (Brief). She is a Knight ally with a withdrawal of 20 HP, takes the member's direction, and will not kill a surrendered creature. The allied Party Power table is in section 1. **Levels 2 and 3: a reserve** (37 against 28 and 36, High-Power Warning): keep the fight at the base budget. **From level 4: counted in full.** Effective Power at the withdrawal (20 HP) is 0.78 of listed: 29 at Tier 1, 23.5 at Tier 2. The r03 Watch escort or emergency patrol (Guards, Tier 1 4, Tier 2 3 each) is never counted.

### r25 Vindicator: the Strike Team (three Knights)

One operation per quest, three days' notice (invented names, the rank event owns them). **Fighting count = PCs minus 1, to a cap of three** (EE rule): 2 / 3 / 3 Knights at 3 / 4 / 5 PCs. Knight Tier 2 Power 30 each (Tier 3: 25); a Knight (30) is below twice a level-6 PC (35), so no warning. They refuse to attack the Watch, a Lord, a captive or a surrendered creature. Withdrawal: each at 26 HP or fewer.

| Level | Base (3 / 4 / 5) | Knights fighting | Ally Power | Allied Party Power | Bruising budget | Bloody budget |
|---|---|---|---|---|---|---|
| 6 | 105 / 140 / 175 | 2 / 3 / 3 | 60 / 90 / 90 | 165 / 230 / 265 | 99 / 138 / 159 | 123.75 / 172.5 / 198.75 |
| 7 | 123 / 164 / 205 | 2 / 3 / 3 | 60 / 90 / 90 | 183 / 254 / 295 | 109.8 / 152.4 / 177 | 137.25 / 190.5 / 221.25 |
| 8 | 132 / 176 / 220 | 2 / 3 / 3 | 60 / 90 / 90 | 192 / 266 / 310 | 115.2 / 159.6 / 186 | 144 / 199.5 / 232.5 |

At 3 PCs the two Knights add 60 to a base of 105 to 132, which is a 45 to 57 percent increase. Either rebuild the fight on the allied total or treat the team as a reserve, and say which per scene. Keep Hard rosters for allied scenes only (LA convention).

### r50 Righteous Hand: the Mobilization (six Knights, two Priests)

One major operation per quest, three days' notice (Brief). **Fighting Knights = PCs minus 1** (up to six); the two Priests hold the rear and are not counted. Knight Power 30 at Tier 2, 25 at Tier 3 (from level 11). Withdrawal 26 HP (Knights).

| Level | Base (3 / 4 / 5) | Knights fighting | Ally Power | Allied Party Power | Bruising budget | Bloody budget |
|---|---|---|---|---|---|---|
| 8 | 132 / 176 / 220 | 2 / 3 / 4 | 60 / 90 / 120 | 192 / 266 / 340 | 115.2 / 159.6 / 204 | 144 / 199.5 / 255 |
| 9 | 147 / 196 / 245 | 2 / 3 / 4 | 60 / 90 / 120 | 207 / 286 / 365 | 124.2 / 171.6 / 219 | 155.25 / 214.5 / 273.75 |
| 10 | 159 / 212 / 265 | 2 / 3 / 4 | 60 / 90 / 120 | 219 / 302 / 385 | 131.4 / 181.2 / 231 | 164.25 / 226.5 / 288.75 |
| 11 | 186 / 248 / 310 | 2 / 3 / 4 | 50 / 75 / 100 (Tier 3) | 236 / 323 / 410 | 141.6 / 193.8 / 246 | 177 / 242.25 / 307.5 |

A Knight (30) is below twice a level-8 PC (44), so no warning. At 5 PCs the mobilization is a 55 percent increase at level 8 (120 on 220), a major force: rebuild the fight on the allied total, or use the mobilization as the reserve against Undermountain encounters sized for a base party.

### Withdrawal and Power by tier

| Ally | Block | Withdraws at | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|---|---|
| Savra | Knight | 20 HP (0.78 of listed) | 37 | 30 | 25 |
| Strike Team and mobilization Knights | Knight | 26 HP (0.71 of listed) | 37 | 30 | 25 |
| Priests of Tyr (if they fight) | Priest | 19 HP (0.71) | 28 | 23 | 19 |
| Courier, door-warden | Priest Acolyte | 5 HP | 10 | 6 | 5 |
| r10 Scouts (if they fight) | Scout | 8 HP | 16 | 12 | 7 |
| Watch patrol | Guard | 5 HP | 4 | 3 | 3 |
## 9. Fixed tables: r03 temple briefings and armory; r10 Uncommon item table (from items.json), potions, 2nd-level spell list, Savra-at-the-lairs table; r25 six-target findings table and +1 weapon table; s01 worthy causes; r50 Knighthood credential

Names marked **invented** are mine and are logged for the event design notes. **A name-collision check was not run** (no content search tool this session); the rank-event drafter runs it.

### 9a. r03 Marcheon: the armory and the temple briefings

**The Armory.** East annex of the Halls of Justice. The keeper is an **invented** lay brother, **Brother Dunstan Wickersham** (replaces R's "Tobrin", which collides with Tobrin Ashvale). One mundane weapon or one suit of armor per tenday per member, returned serviceable; a ruined item is replaced at its listed price; no magic items. Companions cannot borrow; the loan ends if the member lends it on. No stat is quoted here (`items-base.json` was not read); the drafter takes the 2024 equipment entry.

| Category | Notice | Fitting | Note |
|---|---|---|---|
| Simple or martial weapon, shield | none | same visit | One weapon or one shield counts as the tenday's item |
| Light armor | none | same visit | One suit |
| Medium armor | 1 day | one day | One suit |
| Heavy armor | 3 days | three days (mine) | One suit; the Order does not stock plate for the member's first loan |

**Temple briefings.** One briefing per **tenday** per member from one named temple, if there is anything worth briefing. Patterns, not names (Tyr's law); nothing that names the Cassalanters, a pact or a devil by name. The door contact is the temple's door-warden, who holds messages "for Savra Belabranta".

| Temple | Where | The briefing covers | It never covers |
|---|---|---|---|
| Halls of Justice (Tyr) | the Halls (ward per the First Meeting drafter; WDH has Castle Ward) | Cases withdrawn after a complaint; wills read early; a witness who changed an account; a warrant requested and then withdrawn | A named defendant; a sealed record |
| Temple of Helm | Castle Ward (R s01) | Posted watchers nobody posted; shuttered watch-houses; a doorway someone pays to have watched; guard hires by the night | The identity of whoever pays |
| Chapel of the Faithful Hand (Torm), **invented** | Trades Ward (invented) | Sworn men who left a post without a word; vows that were paid for; a charity whose books do not close; "known fiendish signs" in general (animals that will not enter a house; a sleeper who talks in a language he does not know) | Any house, family or pact; anything that says whose devils they are |

- The Torm temple's name and ward are invented and flagged for the audit.
- **Renown loss:** the rank stays; accompaniment, armory and briefings wait until the Renown is restored.

### 9b. r10 Whitehawk: the Uncommon item, potions, spells and Savra at the lairs

**The Uncommon item (one, chosen at the meeting; no "GM chooses").** Rarity from XDMG, `items.json`. **Ring of Protection (Rare) and Bracers of Defense (Rare) are excluded** (both verified Rare).

| Item | Rarity (XDMG) | Attunement | Effect (2024 text) |
|---|---|---|---|
| Sentinel Shield | Uncommon | none listed | While holding it, Advantage on Initiative rolls and Wisdom (Perception) checks; +2 AC as a Shield |
| Cloak of Protection | Uncommon | yes | +1 bonus to Armor Class and saving throws while worn |
| Brooch of Shielding | Uncommon | yes | Resistance to Force damage; Immunity to damage from the *Magic Missile* spell |
| Periapt of Wound Closure | Uncommon | yes | Whenever you make a Death Saving Throw, you can change a roll of 9 or lower to a 10 (Life Preservation); Hit Dice rolled to regain HP restore double (Natural Healing Boost) |

- **Generic +1 weapon, armor or shield entries do not exist in `items.json`.** The "+1" block (lines 9 to 345) holds only named items. R's "Armor, Ring, or Weapon" choice is dropped. The +1 weapon belongs to r25 (9c).
- **Potions:** *Potion of Healing* (common, XDMG): a Bonus Action to drink or administer to a creature within 5 feet, regains 2d4 + 2 HP. *Potion of Greater Healing* (uncommon, XDMG): regains 4d4 + 4 HP. One of each before a quest's main operation, from the Halls infirmary, one day's notice.

**Temple spellcasting, level 2 or lower (XPHB), components under 100 gp covered.** Fixed list. *Speak with Dead* (level 3) and *Resurrection* (level 7) are not on it.

| Spell | Level | Casting time | Range | Components | Duration | Note |
|---|---|---|---|---|---|---|
| Aid | 2 | action | 30 ft. | V S M (a strip of white cloth) | 8 hours | up to three creatures, +5 HP max and current |
| Augury | 2 | 1 minute | self | V S M (tokens worth 25+ GP) | instant, ritual | the 25 gp is covered |
| Bless | 1 | action | 30 ft. | V S M (a Holy Symbol worth 5+ GP) | concentration, 1 minute | the temple lends the symbol |
| Calm Emotions | 2 | action | 60 ft. | V S | concentration, 1 minute | Charisma save |
| Cure Wounds | 1 | action | touch | V S | instant | 2d8 + modifier |
| Detect Evil and Good | 1 | action | 30 ft. sphere | V S | concentration, 10 minutes | senses Aberration, Celestial, Elemental, Fey, Fiend or Undead within 30 ft.; whether *Hallow* is active |
| Gentle Repose | 2 | action | touch | V S, M **unread** | **unread** | the header was read; components and duration were not |
| Healing Word | 1 | bonus action | 60 ft. | V | instant | 2d4 + modifier |
| Lesser Restoration | 2 | bonus action | touch | V S | instant | ends Blinded, Deafened, Paralyzed or Poisoned |
| Locate Object | 2 | action | **unread** | **unread** | **unread** | only level and casting time were read |
| Prayer of Healing | 2 | 10 minutes | 30 ft. | V | instant | up to five creatures, a Short Rest plus 2d8 HP |
| Zone of Truth | 2 | action | 60 ft. | V S | 10 minutes | Charisma save; a failed save cannot speak a deliberate lie; may stay silent |

- **Fixed exclusions (Rep 02):** no spell cast against a living named person. *Detect Evil and Good* is cast only at a place the member names that is not the Cassalanter Villa, or after M4 and M5 have made devils known (secrecy). Cost: the temple covers material components under 100 gp (Augury's 25 gp is the dearest row read).

**Savra at the lairs, Renown 10 or higher** (from Rep 02 C16; the `arc-f:37`, `arc-g:41`, `arc-i:39`, `arc-j:49` lines were not re-read this session).

| Lair (level) | What Savra does | Math |
|---|---|---|
| Xanathar's Lair (L5 to L6) | Three *Potion of Healing* before the operation; waits at the extraction point and fights if called | Knight 30; allied PP 126 / 158 / 190 at L5 only if she fights |
| Cassalanter Villa (L5 to L6) | Gives the member a Siamorphe holy symbol if the party holds Faction Outposts evidence of Asmodean worship; attends the ball and makes one improvised intervention | No stat; the item is not in `items.json` (unverified) |
| Kolat Towers (L7) | A Knight at the extraction point; restores 25 HP once to a creature of the member's choice (arc-i text; the Knight block has no such feature) | Knight 30 if it fights; allied PP 153 / 194 / 235 |
| Vault of Dragons (L7) | Stands at the City of the Dead main gate for the approach | Not a combatant; no Power |

### 9c. r25 Vindicator: the six-target findings table and the +1 weapon

**The Investigation.** One target at a time; the predicate is a written exhibit a magistrate would read (the M5 ledger or a party-delivered document), never the r10 dossier. The written report arrives in **two tendays**. Savra files "diabolism" only after the party has found devil evidence. The rows below are mine.

| Target | Predicate needed | The report finds | The report cannot say |
|---|---|---|---|
| Victoro Cassalanter | **Ledger Recovered** (the M5 ledger) | The ledger is in his hand (matched to three signed charity receipts); the Aveen Street cellar was leased through a civic association; devil worship is credibly shown; a petition to the Lords stands | No terms, no deadline, no children; the family is not charged |
| Xanathar's Guild | A Watch complaint or a party-delivered document | A Castle Ward rowhouse with night-time stretcher traffic; two sworn complaints; the owner of record is a front | No named Guild officer; the beholder is not named |
| The Splinter's Trade Ward safe house | The Splinter inquiry file or a party-delivered document | Cart and carriage traffic twice a tenday; three tenants named only by initial; rent paid a quarter ahead through a notary | No names; "Manshoon" appears only after **Manshoon Named** |
| Gysheer Omfreys | Her belongings from M4 (the note sealed "V.C.", the cartage receipt for crates to Aveen Street) | Lodging above the dyer's shop on Crispin Street; courier payments; summoning devils in a residential court is a chargeable act | Her employer is known only by the initials |
| The M2 household secretary | **Forged Record Secured** | The alias is in no register; the forged entry matches a hand in three other filings; the hire-coach is registered to a Sea Ward livery | Whose household she serves, unless the party supplied it |
| A named independent (example: Emmek Frewn) | A written exhibit naming one act (for example the contract that hired Kelso's gang against Trollskull Alley) | He hired the gang; payment ran through a broker; Savra can refer it to the Watch | Nothing about the Grand Game |

**The +1 weapon (permanent, chosen at the meeting; provenance: the seized cache, held three years, the same cache r50 names).**

| Category | Choices | Notes |
|---|---|---|
| Sword | longsword, rapier, shortsword | Savra picks for the member's fighting style |
| Axe | battleaxe, handaxe | |
| Hammer | warhammer, maul | |
| Bow | longbow, shortbow | |

- **Rarity is unverified.** `items.json` has no generic "+1 Weapon" (see 9b). Named items with a +1 bonus in the data are Uncommon (`+1 Wraps of Unarmed Power` lines 315 to 331, `+1 Moon Sickle` lines 141 to 175, `+1 Rod of the Pact Keeper` lines 230 to 249, `+1 Wand of the War Mage` lines 288 on), so the table treats it as Uncommon. Weapon names are from the 2024 *Player's Handbook* and were not checked against `items-base.json`; no weapon stat is quoted.

### 9d. s01 The Tithe: worthy causes

The tithe is 25% of the member's own equal share. The **Order's clerk, not Savra, takes the receipt** (recipient, amount, date, the clerk's signature). Trollskull Alley Rebuilding is dropped from R (the party would tithe to itself).

| Cause | What it does | Note |
|---|---|---|
| Temple of Helm (Castle Ward) | Runs a hospice wing for Watch veterans and their families | Donations go to the healing work |
| Halls of Justice, Legal Aid Fund | Tyr's clergy represent Field Ward residents who cannot afford a hearing before the Lords | The fund is chronically short |
| Field Ward Soup Houses | Three independent kitchens feed about four hundred people a day | All three are underfunded |
| Griffon Cavalry Dependents Fund | Families of Cavalry riders killed or maimed in service | Savra does not name this one; if chosen she nods and says nothing further |

### 9e. r50 Righteous Hand: the Knighthood credential

**The Writ of Knighthood.** A vellum writ under the Order's central seal (not the chapter seal), signed by Savra and the high priest of Tyr (invented name, the rank event owns it). It is a credential, not a command. The investiture prior holder is a senior Knight of the Waterdeep chapter who has since died (Brief); Savra has never held the rank.

| Effect | Rule |
|---|---|
| Standing | The holder may swear as a witness and file a written complaint before a magistrate or temple court in a city where the Order is recognized; the clerk reads it aloud into the record |
| The open door | Advantage on one Charisma (Persuasion) check to obtain a hearing with a Watch captain, a temple head or a magistrate in such a city, once per official per tenday (mine) |
| Lodging | Any temple of Tyr, Helm or Torm lodges the holder and up to four companions for three nights a visit, free (Chevall's bed, extended) |
| Correspondence | Letters under the Order's seal are answered within a tenday by a temple or civic authority that respects the Order |

- **Limits.** It grants no arrest power, no warrant and no immunity. It means nothing to an official or creature that does not respect the Order, and it does nothing in Undermountain (no officials to present it to).
- **Loss rule.** If Renown falls below 50 the writ stays but its effects pause until the Renown is restored.
- Source text kept from R: "Allied temples and civic authorities across the Sword Coast will recognize it as a legitimate credential of the Order... Which isn't all of them. Enough." The Appendix B phrase "quasi-official legal standing" is the intent behind the four effects (Rep 02 5a; not re-read).
## Verification (line ranges in the data files)

Source key: **XMM** = `bestiary-xmm.json`, **XPHB** = `spells-xphb.json`, **ITEMS** = `items.json` (XDMG entries; the older DMG entry sits just above each), all in the scratchpad `5e/` folder, read directly this session by line range (no search tool; blocks were located by page number and read in windows). **Skill** = `cr2-encounter-builder`. **Rep 02/03/04** = the research reports. **Brief** = `order-of-the-gauntlet-conversion-brief.md`. "Name line inferred" means the block header sat just above the window read.

### Creature blocks (XMM)

| Item | Lines | Status | Value used |
|---|---|---|---|
| Tough | 55328-55424 | Verified | CR 1/2, AC 12, HP 32 (5d8+10), Pack Tactics, Mace +4 5, Heavy Crossbow +3 6 |
| Tough Boss | 55425-55538 | Verified (not used in an Order roster) | CR 4, AC 16, HP 82, Multiattack two, Warhammer +5 12 push 10, Heavy Crossbow +4 13 |
| Bandit | 7978-8072 | Verified | CR 1/8, AC 12, HP 11 (2d8+2), Scimitar +3 4, Light Crossbow +3 5 |
| Bandit Captain | 8073-8188 | Verified (not used in an Order roster) | CR 2, AC 15, HP 52, Multiattack two, Scimitar +5 6, Pistol +5 8, Parry |
| Guard | 30390-~30470 (read to 30462) | Verified | CR 1/8, AC 16, HP 11, Spear +3 4 |
| Knight | 34553-~34670 | Verified | CR 3, AC 18, HP 52, Multiattack two, Greatsword +5 10 + 4 radiant, Heavy Crossbow +2 11 + 4 radiant, Parry |
| Priest | 45220-45380 | Verified | CR 2, AC 13, HP 38, Mace +5, Radiant Flame +5, Spirit Guardians 1/day, Divine Aid 3/day; no Banishment |
| Priest Acolyte | 45381-~45520 (read to 45499) | Verified | CR 1/4, AC 13, HP 11, Mace +4 5 + 2, Radiant Flame +4 7, Divine Aid 1/day |
| Scout | 49263-~49345 (read to 49341) | Verified | CR 1/2, AC 13, HP 16, Multiattack two, Shortsword +4 5, Longbow +4 6 |
| Spy | 52642-~52735 | Verified | CR 1, AC 12, HP 27, no Multiattack, Shortsword +4 5 + 7 poison, Hand Crossbow +4 5 + 7 poison, Cunning Action |
| Cultist Fanatic | 15316-15453 | Verified | CR 2, AC 13, HP 44, Pact Blade +4 6 + 7 necrotic, Spellcasting DC 12 (Hold Person 1/day, Command 2/day), Spiritual Weapon 2/day |
| Imp | ~33294-~33440 (page line 33300; read to 33429; name line inferred) | Verified | CR 1, AC 13, HP 21, Sting +5 6 + 7 poison, Invisibility (self, at will), Shape-Shift (rat, raven Fly 60, spider), Magic Resistance |
| Spined Devil | 52228-52350 | Verified | CR 2, AC 13, HP 45, Flyby, Magic Resistance, Infernal Fork +4 5 + 3 fire, Tail Spine +4 4 + 3 fire range 20/80; no Hurl Spine |
| Bearded Devil | 9108-~9232 (stats and actions read 9109-9200) | Verified | CR 3, AC 13, HP 58, Beard +5 7 (Poisoned, no HP regained), Infernal Glaive +5 reach 10 8 (Con DC 12 wound 5/turn), Magic Resistance; no Diabolical Restoration |
| Horned Devil | 32553-~32700 (read 32554-32693) | Verified | CR 11, AC 18, HP 199, Cha save +8, Magic Resistance, Diabolical Restoration, three attacks, Searing Fork +10 15 + 9 fire, Hurl Flame +8 range 150 26 fire, Infernal Tail DC 17; no Battle Frenzy |
| Wererat | 59570-~59690 (read to 59669) | Verified | CR 2, AC 13, HP 60, Multiattack two, Bite +5 8 (Con DC 11 curse), Scratch +5 6, Hand Crossbow +5 6; **no resistances, no Regeneration, no silver rule** |
| Giant Rat | 25215-~25290 (read 25216-25279) | Verified | CR 1/8, AC 13, HP 7, Pack Tactics, Bite +5 5 |
| Barbed Devil | 8613-8709 (partial) | Read, not used | CR 5, AC 15, HP 110 |

All Rep 03 section 3.1 and Rep 04 section 7 stat values for the creatures above were re-checked and matched. Not read: Bone Devil, Chain Devil, Erinyes (Rep 04 values for them are **unverified here** and not used).

### Spells (XPHB)

| Item | Lines | Status | Value used |
|---|---|---|---|
| Banishment | 1448-~1510 | Verified | Level 4, action, 30 ft., V S M (pentacle), concentration 1 minute, Charisma save, Incapacitated in a demiplane; a Fiend does not return if it lasts 1 minute |
| Aid | ~71-123 (name line not on screen; level at 76) | Verified | Level 2, action, 30 ft., V S M (cloth), 8 hours, +5 HP |
| Augury | 1083-1157 | Verified | Level 2, 1 minute, self, V S M (25+ GP), ritual |
| Bless | 1955-2016 | Verified | Level 1, action, 30 ft., V S M (Holy Symbol 5+ GP), concentration 1 minute |
| Calm Emotions | 2395-2449 | Verified | Level 2, action, 60 ft., V S, concentration 1 minute, Cha save |
| Cure Wounds | 4959-5009 | Verified | Level 1, action, touch, V S, 2d8 + mod |
| Detect Evil and Good | ~5396-5443 (name line not on screen; text matches) | Verified | Level 1, action, 30 ft., V S, concentration 10 minutes |
| Gentle Repose | 9007-~9060 | **Partial**: level 2, action, touch, V S read; M and duration unread | |
| Healing Word | 10263-10314 | Verified | Level 1, bonus, 60 ft., V, 2d4 + mod |
| Lesser Restoration | 11829-11868 | Verified | Level 2, bonus, touch, V S |
| Locate Object | 12160-~12200 | **Partial**: level 2, action read; range, components, duration unread | |
| Prayer of Healing | 15030-15080 | Verified | Level 2, 10 minutes, 30 ft., V, 2d8 + Short Rest, up to five |
| Zone of Truth | 22033-22077 | Verified | Level 2, action, 60 ft., V S, 10 minutes, Cha save |
| Speak with Dead | 17822-~17870 | Verified (level only) | Level 3 |
| Resurrection | ~16246-16305 (header partly off screen; level at 16253) | Verified | Level 7, 1 hour, touch, V S M (diamond 1,000+ GP, consumed) |
| Hold Person, Command, Spiritual Weapon, Invisibility, Stable/Medicine rules, 2024 Paralyzed, grapple and chase rules | none | **Unverified** | Named as the Cultist Fanatic and Imp blocks list them; no text relied on |
| Dispel Evil and Good, Hallow, Raise Dead | none | **Unverified** | Not used |
| Class spell lists (who has Banishment) | none | **Unverified** | Class lists are not in the downloaded files |

### Items (ITEMS, XDMG entries)

| Item | Lines (XDMG; DMG entry above) | Status | Rarity and value |
|---|---|---|---|
| Sentinel Shield | 57952-57972 (DMG 57927-57951) | Verified | **Uncommon**; no attunement listed; Advantage on Initiative and Perception |
| Cloak of Protection | 12592-12614 (DMG 12553-12591) | Verified | **Uncommon**, attunement; +1 AC and saves |
| Brooch of Shielding | 9749-9771 (DMG 9717-9748) | Verified | **Uncommon**, attunement; Resistance to Force, Immunity to *Magic Missile* |
| Periapt of Wound Closure | 44980-~45017 (DMG 44951-44979) | Verified | **Uncommon**, attunement; Life Preservation, Natural Healing Boost (the 2024 text differs from the DMG's "stabilize" line) |
| Ring of Protection | 52741-52765 (DMG ~52697-52740) | Verified | **Rare**, attunement: excluded |
| Bracers of Defense | 9319-9339 (DMG ~9290-9318) | Verified | **Rare**, attunement: excluded |
| Potion of Healing | 47505-47541 | Verified | Common; 2d4 + 2; Bonus Action |
| Potion of Greater Healing | 47310-47335 | Verified | Uncommon; 4d4 + 4 |
| Spell Scroll (Level 4) | 61515-61544 | Verified | **Rare**; spell save DC 15, attack +7 |
| Spell Scroll (Level 5) | 61545-61574 | Verified | **Rare**; spell save DC 17, attack +9 |
| Generic +1 Weapon, Armor, Shield | none (the "+1" block, lines 9-345, has named items only) | **Absent from the data** | Rarity unverified; treated as Uncommon from named +1 items (lines 141-175, 230-249, 288 on, 315-331) |
| Siamorphe holy symbol | none | **Unverified** | Story item from `arc-g:41` (Rep 02), not in the data |
| `items-base.json` | not read | **Unverified** | No base item stat is quoted |

### Mine, flagged, and corrections

| Item | Status |
|---|---|
| Heuristics: 0.71 for a half-pool leaver; sqrt(f) for other fractions; Savra 0.78; effective-Power notes | **Mine** (not skill rules) |
| Squishy-PC hit points (L2 14 to L7 44); the "spread" definition; Horned Devil three-attack rule; Gysheer and Wererat safeguards | **Mine** |
| M1 break rule, M2 hold-and-break and Watch round-four patrol, M3 yield at 30 HP, M5 two-room split, M6 setups B and C, Standard/Hard triggers (Planted Story Exposed, escalation tier, villa result) | **Mine** |
| Armory table, temple briefing topics, findings table, weapon table, Knighthood effects, "Savra at the lairs" mechanics | **Mine** |
| Invented names: Brother Dunstan Wickersham, the Chapel of the Faithful Hand (Torm, Trades Ward) | **Invented**; a file-name search of `notable-figures/` found no match, a content search was not run |
| Roster check: Savra (`order-of-the-gauntlet/01-savra-belabranta.md`), Kelso (`independents-adversaries/03-kelso-fiddlewick.md`), Victoro (`cassalanters/01-victoro-cassalanter.md`) and Emmek Frewn (`trollskull-community/10-emmek-frewn.md`) have pages | Checked by file name |
| No page found for Gysheer Omfreys, Orros, Brynn Hilltopple, Pell, Gaxly, Trevar | Event-only or invented names; `campaign/structure/appendix-a-npc-roster.md` does not exist, so the roster check cannot run |
| Rep 04 M6: the first-turn +4 reading (Power 165) and the Bone Devil rosters | **Overruled** by the Session 45 ruling (Brief, user decision 3); the Horned Devil is Power 130 |
| Rep 03 M2 rosters at 4 and 5 PCs (36 and 48) | **Changed** here to 40 and 52 to sit nearer the budget; the 3-PC roster and the Bruising band are unchanged |
| Rep 04 M4, M5 rosters; Rep 03 M1, M3 rosters | **Reproduced** and recomputed; all numbers matched |
| Rep 04 Banishment odds (9.0% at DC 15, 16.0% at DC 17) | **Matched**; multi-cast figures here are new |
| Watch patrols and Guards (r03 escort, M2 round-four patrol) | Never counted; Guard Power is listed in section 1 for reference only |
