# Lords' Alliance Mechanics Reference (Session 44)

CR 2.0 audits for the five Lords' Alliance fights (M1 to M5), the ally blocks, and the fixed rank-benefit tables. Modelled on `emerald-enclave-mechanics-reference.md` (cited as **EE**). Where a number says "EE", it is theirs. Every stat value below was read this session from `bestiary-xmm.json` (XMM) or `spells-xphb.json` (XPHB) in the scratchpad `5e/` folder; the Verification table gives the line ranges. Anything not read is marked "unverified". Everything marked "mine" is a design choice of this reference, not a skill rule.

## Method and conventions

- CR 2.0 only. % HP lost = (Enemy Power / Party Power) squared. Budget = Party Power x multiplier. Bands: Mild 0-20% (Day Cost 2), Bruising 20-40% (4), Bloody 40-60% (6), Brutal 60-80% (8), Oppressive 80-100% (10), Overwhelming 100-130% (13), Crushing 130-170% (17), Devastating 170-250% (25), Impossible 250-500% (50). "Standard" = Bruising. A roster up to about 5% over its budget is accepted (skill).
- Monster Power uses the tier-adjusted table (skill, Part II), never the flat table. Tier 1 = party level 1-4, Tier 2 = 5-10, Tier 3 = 11-16. Only the CRs used here:

| CR | 0 | 1/8 | 1/4 | 1/2 | 1 | 2 | 3 | 4 | 6 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Tier 1 | 1 | 4 | 10 | 16 | 22 | 28 | 37 | 48 | 80 | 115 |
| Tier 2 | 1 | 3 | 6 | 12 | 17 | 23 | 30 | 38 | 65 | 95 |
| Tier 3 | 0 | 3 | 5 | 7 | 15 | 19 | 25 | 32 | 50 | 75 |

- Waves are separate encounters and their Day Costs add (skill). Percentages of separate waves are never added.
- **Listed Power versus effective Power (mine, as EE).** Power is the square root of HP x DPR, so a creature that leaves when it has lost a fraction f of its hit points contributes about the square root of f of its listed Power (leaving at half is 0.71). The verdicts in M1, M2, M4 and M5 use listed Power, as EE does, and show the effective figure as a note. **M3 is the one exception:** Esloon's withdrawal is a hard rule (he cannot be held, because *Misty Step* teleports him out of a grapple), so M3's governing band uses his effective Power and shows the listed figure beside it. The reason is in section 5.
- **First-turn KO check.** The skill adds 4 to CR when a monster can kill or KO a PC on turn one. I rule on each monster in its section. Summary: Carrion Crawler no (it cannot attack on turn one, by geometry); Bandit Captain no; Mage no (user ruling), with safeguards; Warrior Veteran no; Tough Boss no, with a stair rule; Spy no.
- **Special CR warning.** The skill lists HP-bypassing monsters. Paralysis is the same kind of effect, so the Carrion Crawler (Paralyzing Tentacles) gets a stated safeguard (the prey rule, section 2).
- Combatant counts include non-member companions. Bystanders, captives, Berna, the sweepers, Lira, the Watch officers and a surrendered creature are never counted.
- Calendar: campaign year 1492 DR; spans in days or tendays.

## 1. Party Power and ally rules

Party Power from the level table (L2 14, L3 18, L4 23, L5 32, L6 35, L7 41, L8 44; skill, Part I). Budgets: Bruising x0.6, Bloody x0.75. Same table as EE section 1.

| Level | PC Power | 3 PCs | 4 PCs | 5 PCs | Bruising budget (3 / 4 / 5) | Bloody budget (3 / 4 / 5) |
|---|---|---|---|---|---|---|
| 2 | 14 | 42 | 56 | 70 | 25.2 / 33.6 / 42 | 31.5 / 42 / 52.5 |
| 3 | 18 | 54 | 72 | 90 | 32.4 / 43.2 / 54 | 40.5 / 54 / 67.5 |
| 4 | 23 | 69 | 92 | 115 | 41.4 / 55.2 / 69 | 51.75 / 69 / 86.25 |
| 5 | 32 | 96 | 128 | 160 | 57.6 / 76.8 / 96 | 72 / 96 / 120 |
| 6 | 35 | 105 | 140 | 175 | 63 / 84 / 105 | 78.75 / 105 / 131.25 |
| 7 | 41 | 123 | 164 | 205 | 73.8 / 98.4 / 123 | 92.25 / 123 / 153.75 |
| 8 | 44 | 132 | 176 | 220 | 79.2 / 105.6 / 132 | 99 / 132 / 165 |

### Ally Power rules (all Alliance allies)

1. **Only while it fights.** An ally adds Power to Party Power only when it is in the fight. An ally that escorts, observes or holds the rear adds nothing. **Never counted:** the r03 Watch Escort Guards, the r03 emergency patrol, Berna and the sweepers, Lira, Jalester, Laeral, any Watch officer, and Sevel Dastar when he is attending rather than fighting.
2. **Counted in full, at the party's tier.** Ally Power is the tier-adjusted Power of its block at the party's level, added to Party Power; the fight is then built from the allied total. The alternative (EE) is to keep the fight at the base budget and let the ally be a safety net. Pick one per scene and say which.
3. **No +4 on allies.** The first-turn KO rule applies to enemies.
4. **Roster columns stay at PC count.** An ally is not a fourth or fifth PC. Pick the roster by PC count, then add the ally to Party Power.
5. **Withdrawal.** Each ally has a stated withdrawal HP. Fighting to that point is worth about 0.71 of listed Power.
6. **High-Power Warning.** An ally at twice any PC's Power or more is a safety net. No Alliance ally trips it: the strongest, the Warrior Veteran, is Power 30 at Tier 2 against a level-5 PC's 32.
7. **Notice and limits** (days of notice, once per quest or tenday) live in the rank events, not here.

### Alliance ally Power (blocks in section 7)

| Ally | Block | CR | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|---|---|
| r03 Watch Escort and emergency patrol | Guard | 1/8 | 4 each | 3 each | 3 each |
| r25 response team (four) | Warrior Veteran | 3 | 37 each | 30 each | 25 each |
| r50 attaché Sevel Dastar | Spy | 1 | 22 | 17 | 15 |

## 2. M1 The Long Watch (level 2, Tier 1): the day-nine Carrion Crawler

Party Power 42 / 56 / 70. Budgets: Bruising 25.2 / 33.6 / 42; Bloody 31.5 / 42 / 52.5. Tier 1 Power: Carrion Crawler (CR 2) 28.

**Carrion Crawler (2024 XMM p. 66, verified).** Large Monstrosity, Unaligned. AC 13, HP 51 (6d10 + 18), Speed 30 ft., Climb 30 ft., Darkvision 60 ft., Perception +5 (passive 15), Str 14 Dex 13 Con 16 Int 1 Wis 12 Cha 5. *Spider Climb.* *Multiattack:* uses Paralyzing Tentacles and makes one Bite. *Bite:* +4, reach 5 ft., 7 (2d4 + 2) piercing plus 3 (1d6) poison. *Paralyzing Tentacles:* Constitution save DC 12, one creature it can see within 10 ft.; on a failure the target has Poisoned, repeats the save at the end of each of its turns, succeeds automatically after 1 minute, and **while Poisoned it has Paralyzed.** There is no "Stagger" trait (Appendix C's "Stagger Saving Throw DC 13" does not exist in 2024).

**Guard (2024 XMM p. 162, verified):** CR 1/8, AC 16, HP 11 (2d8 + 2), Speed 30 ft., Spear +3, reach 5 ft. or range 20/60 ft., 4 (1d6 + 1) piercing. At half HP a Guard has 5 HP. **Berna** and the sweepers use **Commoner** (CR 0, AC 10, HP 4, Club +2, 2 bludgeoning; XMM verified).

### Rosters

One Carrion Crawler at every party size. The Guards and Berna are not counted (rule 1: two Guards at 5 HP each fight for at most a round, and they are the crawler's first targets).

| PCs | Roster | Listed Power | % lost (listed) | Design adjustment | Final band | Day Cost |
|---|---|---|---|---|---|---|
| 3 | 1 Carrion Crawler | 28 | 44.4% Bloody | **Arrives wounded to 38 HP** (the Guards' spears). The plain table governs: still **Bloody**; the wound's effect (about 33%) is a heuristic only | **Bloody** | 6 |
| 4 | 1 Carrion Crawler | 28 | **25.0% Bruising** | none | **Bruising** | 4 |
| 5 | 1 Carrion Crawler | 28 | **16.0% Mild** | none | **Mild** | 2 |

- **The wound at 3 PCs (mine).** The Guards have been fighting it down the drains and into the alley: it begins the fight at 38 HP (13 down). This is the small-party step-down in the fiction. The plain table still rates the fight Bloody at 3 PCs (44.4%), which is within the brief's cap. A table that wants the 4- and 5-PC fights softer can apply the same wound: 24.2 gives 18.7% Mild at 4 PCs and 12.0% Mild at 5.
- **If the Guards were counted** (they should not be): Guard Tier 1 Power 4 each, so Party Power 50 / 64 / 78 and the full-HP crawler is 31.4% / 19.1% / 12.9%. Use this only to show the table what the Guards are worth: about one band at 3 PCs.
- **Real cost is lower.** The crawler retreats at half its starting HP (below), which is about 0.71 of listed Power.

### First-turn KO ruling: no +4, with geometry and a prey rule

- **The pattern.** Tentacles paralyze on a failed DC 12 save (a 2nd-level character with Constitution +0 to +2 fails roughly half the time). Paralyzed, the target is attacked with Advantage and a hit from within 5 ft. is a critical hit (2024 condition text: unverified here, as in EE). A critical Bite is 4d4 + 2 plus 2d6 poison: average 19, maximum 30. A 2nd-level character has roughly 12 to 24 HP, so Tentacles then a critical Bite in the same Multiattack could drop a caster on turn one.
- **Why +4 does not apply.** (1) **Geometry:** the grate stands **60 ft. from the party end of the alley** (mine; the source gives only a 20-ft. alley). The crawler's Speed is 30 ft., Tentacles reach 10 ft. and Bite reaches 5 ft. It cannot attack on its first turn: it spends turn one coming out of the shaft and moving 30 ft., and its first attack comes on turn two, after every character has acted twice. (2) **Prey rule** (below), which removes the same-turn Tentacles-then-critical-Bite pattern.
- If +4 were applied: CR 6, Tier 1 Power 80, which is 362.8% (Impossible, 50) at 3 PCs, 204.1% (Devastating, 25) at 4 and 130.6% (Crushing, 17) at 5. That is not the fight the premise wants, so the ruling below applies instead.
- **Prey rule (special CR warning safeguard, mine, same shape as EE's grell and chuul rules):**
  1. The crawler never makes its Bite against a creature it Paralyzed earlier in the same turn. If no other creature is within 5 ft., it skips the Bite.
  2. It never attacks a creature at 0 HP.
  3. It uses Paralyzing Tentacles on the nearest creature that is not already Paralyzed. In round 2 the nearest creature is a Guard if a Guard is still standing between it and the party.
  4. Result: one turn of one crawler does at most 16 damage to one creature (a non-critical Bite, 2d4 + 2 + 1d6 at maximum), so no character of 17 HP or more is dropped by a single turn. A Paralyzed character is critically bitten only on the crawler's next turn, and the party has a full round to act.
- **Counterplay.** The Paralysis ends on the target's end-of-turn save (DC 12). An ally can drag a Paralyzed character 15 ft. out of reach (Utilize, half of the dragger's Speed). *Lesser restoration* ends Poisoned (spell text unverified here); a 2nd-level party will not have it.

### Tactics

- **Start of combat.** Characters, Berna's four sweepers and the two Guards are at the alley mouth. The crawler climbs out of the grate 60 ft. away. Roll no initiative for the sweepers; they run out of the alley behind Berna on their first turn.
- **Round 1.** The crawler moves 30 ft. toward the nearest creature and cannot reach anyone. The Guards (5 HP each) fall back behind the party, or fight if cornered.
- **Round 2 onward.** Tentacles on the nearest non-Paralyzed creature, Bite on a different creature within 5 ft.
- **Retreat rule (the crawler).** It drops down the shaft (Climb 30 ft.) when it has half of its starting HP or fewer: **19 HP or fewer at 3 PCs, 25 HP or fewer at 4 or 5.** A retreat is not a kill: it goes back into the drains and the sweepers hear it for a tenday. It does not retreat if its way to the shaft is blocked; a cornered crawler fights to 0.
- **Non-combat route.** None ends the crawler. The mission's non-combat objective is people: Berna's crew and the Guards reach the street. Blocking the shaft is a poor idea (it removes the retreat).
- **Party retreat rule.** A character who drops to 0 HP or two characters Paralyzed at once: the party may break off. The crawler does not pursue past the alley mouth into the lit street (mine). Berna's crew stays behind the party at all times.
- **"No worker or Guard drops" bonus:** reachable. The crawler cannot attack in round 1, so the party can interpose before any Guard or sweeper is in reach.

## 3. M2 The Exile's Return (level 3, Tier 1): Harko in the warehouse

Party Power 54 / 72 / 90. Budgets: Bruising 32.4 / 43.2 / 54; Bloody 40.5 / 54 / 67.5. Tier 1 Power: Bandit Captain (CR 2) 28; Bandit (CR 1/8) 4; Kenku (CR 1/4) 10; Tough (CR 1/2) 16.

**Bandit Captain (XMM p. 27, verified).** Small or Medium Humanoid, Neutral. AC 15, HP 52 (8d8 + 16), Speed 30 ft., Str 15 Dex 16 Con 14 Int 14 Wis 11 Cha 14, saves Str +4 Dex +5 Wis +2, Athletics +4 Deception +4. *Multiattack:* two attacks, using Scimitar and Pistol in any combination. *Scimitar:* +5, reach 5 ft., 6 (1d6 + 3) slashing. *Pistol:* +5, range 30/90 ft., 8 (1d10 + 3) piercing. *Parry (reaction):* +2 AC against a melee hit while holding a weapon.

**Bandit (XMM, verified).** CR 1/8, AC 12, HP 11 (2d8 + 2), Speed 30 ft. *Scimitar* +3, 4 (1d6 + 1) slashing. *Light Crossbow* +3, range 80/320 ft., 5 (1d8 + 1) piercing.

**Kenku (XMM p. 183, verified).** Medium Monstrosity, Neutral. CR 1/4, AC 13, HP 13 (3d8), Speed 30 ft., Darkvision 60 ft., Deception +4 Perception +2 Stealth +5. *Mimicry:* mimics any sound it has heard, including voices; a creature that hears it can tell it is an imitation with a DC 14 Wisdom (Insight) check. *Shadow Blade:* +5, reach 5 ft. or range 60 ft., 6 (1d6 + 3) necrotic. *Eldritch Lantern (Recharge 4, bonus action):* *Faerie Fire*, save DC 10.

**Tough (XMM p. 307, verified).** CR 1/2, AC 12, HP 32 (5d8 + 10), Speed 30 ft., *Pack Tactics*, *Mace* +4, 5 (1d6 + 2) bludgeoning, *Heavy Crossbow* +3, range 100/400 ft., 6 (1d10 + 1) piercing.

### Rosters

| PCs | Roster | Power | % lost | Band | Day Cost |
|---|---|---|---|---|---|
| 3 | Harko + 1 Bandit (2 kenku are the alarm, not counted) | 28 + 4 = 32 | 35.1% | **Bruising** | 4 |
| 4 | Harko + 2 Bandits (kenku not counted) | 28 + 8 = 36 | 25.0% | **Bruising** | 4 |
| 5 | Harko + 2 Bandits + 1 Tough (kenku not counted) | 28 + 8 + 16 = 52 | 33.4% | **Bruising** | 4 |

- Arithmetic: (32/54) squared = 0.351; (36/72) squared = 0.250; (52/90) squared = 0.334. All three are inside the Bruising budget (32.4 / 43.2 / 54).
- **Effective cost (mine):** Harko surrenders at half HP (factor 0.71 on 28 = 19.9). With the Bandits at full value the real fight is 23.9 / 27.9 / 43.9 Power, which is about 19.6% / 15.0% / 23.8% (Mild, Mild, Bruising). The verdicts use listed Power.
- **Kenku are not combatants.** They are paid lookouts at the door (the source: they carry nothing of value and flee). **If the party bars their exit, they drop their blades and surrender; they do not fight cornered.** For reference only: counting two kenku (20) would make the fight 92.7% (Oppressive) at 3 PCs, 60.5% (Brutal) at 4 and 64.0% (Brutal) at 5, so the surrender rule matters.
- **First-turn KO:** none. Harko's best first turn is two Pistol hits: 16 average, 26 at the maximum (two 13s). A level-3 character has roughly 18 to 30 HP. The maximum could drop the frailest caster, but it needs both shots to hit with maximum rolls. No +4.

### The kenku alarm clock

- **At the start of their first turn,** each kenku makes the sound of a Watch whistle (Mimicry, no action) and runs for the street door. A kenku that is Grappled, Restrained or at 0 HP before its first turn does not whistle. **Both must be stopped to keep the clock off.**
- **If either whistles,** a real Watch patrol (two Guards) reaches the warehouse door at the **end of round 4**. The party has four rounds to end the fight and leave, or to be found with a dead or captured Harko. This is the "quietly" pressure: Jalester's order is quiet, and an alarm makes it loud.
- **A party that ambushes** (DC 12 Dexterity (Stealth) to reach the kenku unseen, with a fallback of the sentries seeing the party and whistling) can take the kenku first and run the fight with no clock.

### Tactics and the surrender

- **Start of combat.** Harko is at the crates with his Pistol. The Bandits take the doorway. Harko fires the Pistol at the nearest character who comes through the door, then uses Parry on melee hits.
- **Harko surrenders at 26 HP or fewer** (half of 52): "I'm not dying for this." He drops the Pistol. This is the turn of the mission. The Bandits break and flee when Harko surrenders or drops. If Harko is Grappled and under half, he surrenders at once.
- **He does not flee.** He has been offered exile twice and has nowhere left to go.
- **Non-combat route:** DC 15 Charisma (Persuasion) from a character who has stopped the kenku and holds the door ends the fight before it starts: Harko lays down his Pistol for a hearing. Failure does not end the fight; it changes who starts it.
- **The fight is optional only in the sense of the order.** Jalester said "quietly put him to the sword"; the surrender gives the party the choice the mission is about.

## 4. M3 The Red Wizard's Price (level 4, Tier 1): Esloon Bezant

Party Power 69 / 92 / 115. Budgets: Bruising 41.4 / 55.2 / 69; Bloody 51.75 / 69 / 86.25. Tier 1 Power: Mage (CR 6) 80; Tough (CR 1/2) 16; Spy (CR 1) 22.

**Mage (2024 XMM p. 199, verified; user ruling: Esloon is the full block).** Small or Medium Humanoid (wizard), Neutral. **CR 6, AC 15, HP 81 (18d8), Speed 30 ft.** Str 9 Dex 14 Con 11 Int 17 Wis 12 Cha 11, saves Int +6 Wis +4, Arcana +6 History +6 Perception +4 (passive 14). *Multiattack:* three Arcane Burst attacks. *Arcane Burst:* +6, reach 5 ft. or range 120 ft., 16 (3d8 + 3) force. *Spellcasting* (Intelligence, save DC 14): at will *Detect Magic*, *Light*, *Mage Armor* (in AC), *Mage Hand*, *Prestidigitation*; 2/day each *Fireball* (level 4 version), *Invisibility*; 1/day each *Cone of Cold*, *Fly*. *Misty Step* (3/Day, bonus action). *Protective Magic* (3/Day, reaction): *Counterspell* or *Shield*.

**Spell texts read (XPHB, verified):** *Fireball* is level 3, 20-ft.-radius sphere, 150 ft., Dexterity save, 8d6 fire plus 1d6 per slot above 3, so the level 4 version is **9d6, average 31.5, half on a save**. *Invisibility* is level 2, 1 action, touch, concentration up to 1 hour, ends when the target attacks, deals damage or casts a spell. *Misty Step* is level 2, bonus action, V only, teleport up to 30 ft. to an unoccupied space you can see. *Counterspell*, *Shield*, *Cone of Cold* and *Fly* texts were **not read** (unverified).

**Spy (XMM p. 295, verified, Sarvos Miln).** Small or Medium Humanoid, Neutral. CR 1, AC 12, HP 27 (6d8), Speed 30 ft., Climb 30 ft., Dex 15 Cha 16, Deception +5 Insight +4 Investigation +5 Perception +6 Sleight of Hand +4 Stealth +6 (passive 16). **No Multiattack.** *Shortsword:* +4, reach 5 ft., 5 (1d6 + 2) piercing plus 7 (2d6) poison. *Hand Crossbow:* +4, range 30/120 ft., 5 (1d6 + 2) piercing plus 7 (2d6) poison. *Cunning Action (bonus action):* Dash, Disengage or Hide.

### The plain-table numbers, for the record

| PCs | Esloon alone, listed | % lost | Band | Day Cost |
|---|---|---|---|---|
| 3 | 80 | 134.4% | Crushing | 17 |
| 4 | 80 | 75.6% | Brutal | 8 |
| 5 | 80 | 48.4% | **Bloody** | 6 |

These match the brief (4th level: 5 PCs 48% Bloody, 4 PCs 76% Brutal, 3 PCs 134% Crushing). Two earlier reports called a lone CR 6 Mage "unfightable" by a 4th-level party without computing it; at 5 PCs it is Bloody.

### First-turn KO ruling: user ruling, no +4, with safeguards

- **Ruling (user):** the +4 adjustment is not applied to Esloon. For the record, +4 would make him CR 10 (Tier 1 Power 115): 277.8% / 156.3% / 100.0% at 3 / 4 / 5 PCs (Impossible, Crushing, Oppressive).
- **The pattern the safeguards answer.** Three Arcane Bursts are 48 damage at maximum-average and all three hit about one time in six; a 4th-level caster has roughly 22 to 28 HP. *Fireball* at level 4 is 31.5 average on a failed save across a 20-ft. radius, and a 4th-level character has roughly 22 to 40 HP. Either can drop a PC on turn one if used freely.
- **Safeguards (mine):** (1) In round 1 Esloon splits his three Bursts across at least two targets. (2) He casts no area spell (*Fireball*, *Cone of Cold*) in round 1. (3) He casts at most one area spell in the whole fight. (4) He never casts an area spell that would catch Sarvos or his own Toughs. (5) He does not attack a creature at 0 HP. None of these changes his Power; they remove the turn-one burst.

### The withdrawal rule (hard) and the surrender backstop

- **Withdrawal.** On his turn, once he has taken **31 or more damage (50 HP or fewer)**, or **at the end of his turn in round 3** (round 2 at 3 PCs), whichever comes first, Esloon uses *Misty Step* (bonus action) toward the Dock Lane exit or a window and then casts *Invisibility* on himself (action), and leaves the building. He keeps the Invisibility until he attacks or casts. The Toughs break and scatter the round after he goes.
- **Why this is a hard rule.** *Misty Step* is a V-only bonus action that teleports 30 ft. to a space he can see, so a grapple or a bar on the door does not hold him. He has it 3/day. The party can stop it only by countering it or by killing him first.
- **Surrender backstop.** If he cannot leave (both *Misty Step* uses spent, or no space he can see), he surrenders at **20 HP or fewer**: "Take the book." He is Neutral and has no loyalty to the Splinter.
- **Effective Power (mine):** he leaves after losing 31 of 81 HP, so effective Power is 80 x sqrt(31/81) = **49.5** (0.62 of listed). A rounds check agrees in order of magnitude: at about 26 damage a round (three Bursts at roughly 55% to hit against AC 16) and about 31 HP per 4th-level PC, two rounds cost a 3-PC party about 57% of its hit points and three rounds a 5-PC party about 51%. That check assumes PC AC 16 and 31 HP and is only a sanity bound.

### Rosters (governing: the plain table; main-session ruling)

The plain tier-adjusted table governs, as the skill requires. Adding Toughs to Esloon pushes every size past Brutal (4 PCs + 1 Tough: (96/92) squared = 108.9% Overwhelming; 5 PCs + 2 Toughs: (112/115) squared = 94.9% Oppressive), so **Esloon fights alone at every size** and his crew is a separate, optional wave.

| PCs | Roster in the room | Power | % lost | **Band (governs)** | Day Cost |
|---|---|---|---|---|---|
| 3 | Esloon alone; withdraws at the end of round 2 | 80 | 134.4% | **Crushing** (see the 3-PC rule) | 17 |
| 4 | Esloon alone | 80 | 75.6% | **Brutal** | 8 |
| 5 | Esloon alone | 80 | 48.4% | **Bloody** | 6 |

- Arithmetic: (80/69) squared = 1.344; (80/92) squared = 0.756; (80/115) squared = 0.484.
- **The 3-PC rule.** A lone full Mage is Crushing against three 4th-level characters on the plain table, and no roster with the full block lands lower. At 3 PCs the withdrawal fires at the end of his round-2 turn whatever his HP, and the fight-trigger reads "the deal is broken" rather than "Esloon is beaten". The effective-Power estimate (he leaves after losing at most 31 HP, 0.62 of listed Power) puts the real cost near 51% Bloody, but that is a heuristic, not the table. Flagged for the user.
- The withdrawal rule and safeguards above apply at every size.
- **The rest of Esloon's crew** (WDH: five thugs, so five Toughs in all) stay in the taproom as the Watch-attention clock and scatter when Esloon goes. A table that fights them anyway has a **separate wave** (Day Costs add, 4): 3 PCs 2 Toughs 21.5% Bruising; 4 PCs 3 Toughs 27.2% Bruising; 5 PCs 4 Toughs 31.0% Bruising (32/69, 48/92 and 64/115, squared).
- **Counterplay the party has.** *Protective Magic* is three uses a day in total (*Shield* or *Counterspell*), so a party that forces three reactions strips his defence. A 4th-level party has no third-level slots, so it cannot *Counterspell* his *Misty Step*; it can only out-damage the 31-point trigger.

### Sarvos Miln (Spy)

- **Not counted.** Sarvos is a broker, not muscle. He leaves on round 1 through the Dock Lane exit: Cunning Action (Dash) gives him Speed 60 ft. for the turn. He does not fight unless cornered.
- **If cornered or chased down,** a separate encounter: Spy alone, Tier 1 Power 22: 10.2% Mild at 3 PCs, 5.7% Mild at 4, 3.7% Mild at 5 (22/69, 22/92, 22/115, squared). He surrenders at 13 HP or fewer or when Grappled; he has no first-turn KO (one poisoned attack, 12 average).
- **Sarvos Captured** requires him alive. His coat holds the signed arrangement and the checkpoint name.

### Tactics (Esloon)

- **Start.** Esloon sits with Sarvos in the private room; his Toughs are in the taproom and the corridor. When the party breaks the meeting he rises, moves behind the table and reads the room. He fights with Arcane Burst and keeps *Protective Magic* (3 uses a day, *Shield* or *Counterspell*) for the reaction.
- **Round 1.** Three Bursts split across two targets. If the party offers talk first, he listens and does not attack until talk fails.
- **Round 2.** The one permitted area spell (*Fireball* centred on the far side of the table if no crew or Sarvos is within 20 ft.), then Bursts.
- **Withdrawal** as above. His question for the Alliance ("Is there another offer? From whoever decides these things.") is asked at the window before he steps through, to the character who last spoke to him.
- **Non-combat routes:** the four approaches in the event (forged letter, intimidation, bribe, disrupt). The fight is the disrupt approach only.

## 5. M4 The Archer Above (level 5, Tier 2): Vhaspar Coldwater

Party Power 96 / 128 / 160. Budgets: Bruising 57.6 / 76.8 / 96; Bloody 72 / 96 / 120. Tier 2 Power: Warrior Veteran (CR 3) 30; Tough (CR 1/2) 12.

**Warrior Veteran (XMM p. 320, verified).** Small or Medium Humanoid, Neutral. CR 3, AC 17, HP 65 (10d8 + 20), Speed 30 ft., Str 16 Dex 13 Con 14, Athletics +5 Perception +2 (passive 12). *Multiattack:* two Greatsword or Heavy Crossbow attacks. *Greatsword:* +5, reach 5 ft., 10 (2d6 + 3) slashing. *Heavy Crossbow:* +3, range 100/400 ft., 12 (2d10 + 1) piercing. *Parry (reaction):* +2 AC against a melee hit while holding a weapon.

The chase is a clock. There is no roster unless the party attacks him.

### The chase clock (mine)

- **Escape Track, 0 to 6.** Vhaspar starts on the roofline of the feed-store block with the track at 2.
- **Each round:** the track rises by 1 (he Dashes over roofs he has used for weeks). Then every pursuing character makes one chase check, **DC 13 Strength (Athletics) or Dexterity (Acrobatics)**. For every two successes the track falls by 1, to a maximum fall of 2 a round. A character who spends an action on a ranged attack that hits (AC 17) lowers the track by 1 instead of making a check, once per round. A pursuer who knows the route (from the Saeth Cromley or Watch-file lead) makes the check with Advantage.
- **Track 0:** he is cornered on a roof edge or in a dead-end loft. He surrenders if offered Watch protection (his bargain for naming Halek); otherwise he fights on the fallback roster.
- **Track 6:** he reaches the bolt hole (not the Skewered Dragon; an unaligned salt-fish smokehouse on the quay, mine). The party loses him for a night. A lead that was not used (Saeth, the Watch file or the canvass) finds the smokehouse at dawn. Halek's cleaners reach Vhaspar within 48 hours, so the dossier is lost if the party is late.
- **Return fire:** when the track is 2 or lower he turns and fires one Heavy Crossbow shot a round at a pursuer (+3, 12 piercing). He does not otherwise attack.
- **Failure costs time, never the whole mission** (Three Clue Rule): every missed chase leaves two other leads to the smokehouse.

### Fallback roster (the party attacks him)

If the party attacks Vhaspar in the room, or the chase ends at Track 0 with a fight, he has the hired hands Halek left to watch the door.

| PCs | Roster | Power | % lost | Band | Day Cost |
|---|---|---|---|---|---|
| 3 | Vhaspar + 2 Toughs | 30 + 24 = 54 | 31.6% | **Bruising** | 4 |
| 4 | Vhaspar + 3 Toughs | 30 + 36 = 66 | 26.6% | **Bruising** | 4 |
| 5 | Vhaspar + 4 Toughs | 30 + 48 = 78 | 23.8% | **Bruising** | 4 |

- Arithmetic: (54/96) squared = 0.316; (66/128) squared = 0.266; (78/160) squared = 0.238. Inside the budgets (57.6 / 76.8 / 96).
- **Vhaspar alone is Mild at every size** (30/96, 30/128, 30/160, squared: 9.8% / 5.5% / 3.5%), which is why the Toughs are in the fallback and not the chase.
- **First-turn KO:** none. Two crossbow hits are 24 average, 42 at the maximum, against level-5 characters of roughly 35 to 45 HP. No +4.
- **Surrender and retreat.** At 32 HP or fewer he surrenders if Watch protection is on the table; with a clear way up through the skylight and no offer, he Dashes out and the track restarts at 3. The Toughs break when he surrenders or drops.

## 6. M5 Fentree's Ledger (level 6, Tier 2): the Green Dragon

Party Power 105 / 140 / 175. Budgets: Bruising 63 / 84 / 105; Bloody 78.75 / 105 / 131.25. Tier 2 Power: Tough Boss (CR 4) 38; Tough (CR 1/2) 12; Spy (CR 1) 17; Noble (CR 1/8) 3; Guard (CR 1/8) 3.

**Tough Boss (XMM p. 307, verified).** CR 4, AC 16, HP 82 (11d8 + 33), Speed 30 ft., Str 17 Dex 14 Con 16, saves Str +5 Con +5 Cha +2, *Pack Tactics*. *Multiattack:* two attacks, using Warhammer or Heavy Crossbow in any combination. *Warhammer:* +5, reach 5 ft., 12 (2d8 + 3) bludgeoning, and a Large or smaller target is pushed up to 10 ft. straight away. *Heavy Crossbow:* +4, range 100/400 ft., 13 (2d10 + 2) piercing.

**Noble (XMM p. 227, verified), used for Ossery Klenn.** Small or Medium Humanoid, Neutral. CR 1/8, AC 15, HP 9 (2d8), Speed 30 ft., Wis 14 Cha 16, Deception +5 Insight +4 Persuasion +5 (passive 12). *Rapier:* +3, reach 5 ft., 5 (1d8 + 1) piercing. *Parry (reaction).* **Why Noble:** Ossery is the Guild's factor at a handover, a negotiator with a social block and no combat role. He is Noska's opposite (Noska never negotiates), so he carries a Noble's Deception and Persuasion and one rapier he does not want to draw.

**Spy (as section 4), used for Rezka.** Tier 2 Power 17. Emira Volstren is a Noble (3). Her escort is two Guards outside the Inn (Guard stats in section 2; Tier 2 Power 3 each).

### Rosters

Ossery's party: the Tough Boss is the bodyguard captain; Toughs are the Guild's hired hands. Rezka (Spy) flees by default. Ossery is counted at his Power (3) but does not fight.

| PCs | Standard roster | Power | % lost | Band | Day Cost | Hard roster (Standard + Rezka cornered) | Power | % lost | Band | Day Cost |
|---|---|---|---|---|---|---|---|---|---|---|
| 3 | Ossery + Tough Boss + 1 Tough | 3 + 38 + 12 = 53 | 25.5% | **Bruising** | 4 | + Rezka | 70 | 44.4% | **Bloody** | 6 |
| 4 | Ossery + Tough Boss + 3 Toughs | 3 + 38 + 36 = 77 | 30.3% | **Bruising** | 4 | + Rezka | 94 | 45.1% | **Bloody** | 6 |
| 5 | Ossery + Tough Boss + 5 Toughs | 3 + 38 + 60 = 101 | 33.3% | **Bruising** | 4 | + Rezka | 118 | 45.5% | **Bloody** | 6 |

- Arithmetic: (53/105), (77/140), (101/175) squared = 0.255, 0.303, 0.333; (70/105), (94/140), (118/175) squared = 0.444, 0.451, 0.455.
- **Use the Hard roster** when Rezka cannot flee (the party took the back stair first), when Xanathar's Guild is at Alert or Lockdown, or when the party attacked first.
- **If Emira's escort joins** (two Guards, +6, arrives in round 3 only if the fight spills into the taproom): Standard 59 / 83 / 107 gives 31.6% / 35.1% / 37.4% (Bruising); Hard 76 / 100 / 124 gives 52.4% / 51.0% / 50.2% (Bloody). Emira herself (Noble) does not fight.
- **First-turn KO: none, with a stair rule (mine).** The Tough Boss makes two attacks for 25 average (Warhammer 12 or Crossbow 13), 38 to 44 at the maximum. Toughs have Pack Tactics, so six attackers on one caster could drop her on turn one. The Green Dragon's hall and stair are 5 ft. wide: **no more than three bodyguards can reach one target on turn one.** That limits the burst to the Boss plus two Toughs, roughly 35 average against level-6 characters of 40 to 55 HP. No +4.

### Tactics

- **Start of combat (interception at the stair).** The Tough Boss leads in the hall. Toughs follow; one holds the stair top with a Heavy Crossbow. Ossery stays behind the Boss with his rapier sheathed.
- **During combat.** The Boss uses Warhammer to push a character down the stair or back through a door. Toughs use Pack Tactics (a Tough or the Boss adjacent counts as an ally). Ossery uses Parry only if struck and surrenders at the first damage: "Take it. The Guild will find another price."
- **Break rule.** The Tough Boss breaks at **27 HP or fewer** (a third of 82; Noska's rule, kept for his block). The Toughs break when the Boss does and surrender if Grappled. Ossery breaks when the Boss does.
- **Rezka's flight.** Rezka is in Room 3 across the hall. Flight Track 0 to 3: it rises by 1 a round (Cunning Action Dash, Speed 60 ft. for the turn), starting when the fight begins or at the alarm. A character within 30 ft. who spends an action chasing (DC 13 Dexterity (Acrobatics) or Strength (Athletics)) stops the rise that round; two successes lower it by 1. A character who blocks the back stair (an action, DC 13 Strength (Athletics)) holds the track for that round and the next. At 3 she is over the yard wall. **If Grappled or at 13 HP or fewer she surrenders** and gives her statement.
- **Non-combat routes.** DC 15 Charisma (Deception) to collapse Ossery's bidding (he will not pay for a ledger whose seller is already caught); DC 15 Charisma (Intimidation) from the party holding the stair; or the party outbids him in coin. Failing the check does not end the fight; it changes who starts it.
- **Day Cost** per fight, 4 or 6. The rest of the mission (Fentree's study, the leads) has no Day Cost.

## 7. Allies

Ally Power rules are in section 1.

### r03 Redknife: the Watch Escort and the emergency patrol

- **Block: Guard** (verified, section 2). Two Guards for one dangerous errand a tenday. **Not counted** (rule 1): they escort and observe, and they are Watch officers who cannot leave their duty. They defend themselves and the member and surrender to nobody.
- **If a table counts them anyway:** Tier 1 Power 4 each, so +8. At level 2 Party Power 50 / 64 / 78 (Bruising 30 / 38.4 / 46.8); at level 3 62 / 80 / 98 (Bruising 37.2 / 48 / 58.8). Two Guards add about one band at 3 PCs; the effect is small at 5.
- **The emergency patrol (mine):** four Guards, arriving 1d4 + 1 minutes after a Redknife's whistle in the city's lit streets. Their arrival time is 20 to 50 rounds, so a fight is over before they come. They arrest or separate the combatants and are **never** counted. **Conflict to log:** BD m03 :226 puts a Guard patrol at round five. To keep it valid, either the BD event reads "within minutes" or the clause becomes 1d4 + 1 rounds. This reference does not choose.

### r25 Warduke: four Warrior Veterans

- **Block: Warrior Veteran** (verified, section 5). Tier 2 Power 30 each at levels 5 to 10, Tier 3 25.
- **Fighting count = PCs minus 1, to a cap of four** (EE rule). The others hold the rear. 3 PCs: 2 fight; 4 PCs: 3; 5 PCs: 4.
- **Allied Party Power and budgets** (ally Power 60 / 90 / 120):

| Level | Base (3 / 4 / 5) | Allied Party Power | Bruising budget | Bloody budget |
|---|---|---|---|---|
| 5 | 96 / 128 / 160 | 156 / 218 / 280 | 93.6 / 130.8 / 168 | 117 / 163.5 / 210 |
| 6 | 105 / 140 / 175 | 165 / 230 / 295 | 99 / 138 / 177 | 123.75 / 172.5 / 221.25 |
| 7 | 123 / 164 / 205 | 183 / 254 / 325 | 109.8 / 152.4 / 195 | 137.25 / 190.5 / 243.75 |
| 8 | 132 / 176 / 220 | 192 / 266 / 340 | 115.2 / 159.6 / 204 | 144 / 199.5 / 255 |

- **Safety-net option:** keep the fight at the base budget (section 1) and let the Veterans be the reserve.
- **Withdrawal:** each at 32 HP or fewer (half of 65). **They refuse** to attack the Watch, a Lord, a captive or a surrendered creature, and to leave the city. Using them for a crime ends the benefit for a tenday.
- **Compare r25 with the base:** at level 8 the four add 120 to a 5-PC party's 220, a 55% increase. They are a major force; the main session should keep the Hard rosters for allied scenes only.

### r50 attaché: Sevel Dastar (Spy)

- **Block: Spy** (verified, section 4). Stat line: Spy; no voice profile (plain, dry, may swear lightly). He reports to Laeral's office. Speed 30 ft., Climb 30 ft., HP 27, **no Multiattack.**
- **Power when he fights:** Tier 2 17, Tier 3 15. One ally; add it only while he fights. A non-combat attaché adds nothing.
- **Party Power with Sevel at level 8 (Tier 2):** 149 / 193 / 237 (base 132 / 176 / 220). Allied budgets: Bruising 89.4 / 115.8 / 142.2; Bloody 111.75 / 144.75 / 177.75.
- **Withdrawal:** 13 HP or fewer (half of 27). He uses Cunning Action (Disengage or Hide) to leave and reports.
- **Behaviour:** poisoned Shortsword and Hand Crossbow, 12 average damage a hit. He does not fight the Watch, a Lord or a surrendered creature.

## 8. M6 (no fight)

An Audience with the Open Lord has no combat and no Day Cost. Laeral's lie rule is flat: **a lie needs a DC 16 Charisma (Deception) check to pass her.** Her Archmage stats (CR 12, Wis 15, no Insight proficiency) were read by report 04 and are **not re-verified here.** The roster-free design depends on that rule, not on a block.

## 9. Fixed tables

### 9a. r10 Stingblade: Introductions (one per quest, from this table)

The member asks for a name and a reason; Jalester arranges it before the next operation. The introduction opens one meeting within 3 days at the NPC's office or home; the NPC is Friendly for that meeting only. **Invented** names are marked and logged in the folder's "Invented Names and Open Items".

| # | Name | Seat | What the introduction gets | Source |
|---|---|---|---|---|
| 1 | Magistrate Barnibus Blastwind | Hall of Justice magistrate (Watchful Order of Magists and Protectors) | A half-hour hearing. He reads one document or one piece of physical evidence and says in writing whether it would stand before a magistrate | Notable Figures page |
| 2 | Lord Torlyn Wands | House Wands, wizard and heir's circle | A letter of standing from the Wands name: one noble door opens (a dinner, a servants' entrance or a steward's ear) | Notable Figures page |
| 3 | Saeth Cromley | Retired Watch sergeant with a Dock Ward network | A named former Watchman in any one ward who will talk about the ward's recent trouble for an hour | Notable Figures page |
| 4 | Valetta | Priest of Gond, House of Inspired Hands | One device or mechanism examined, or one repair, inside 3 days; no magic items | Notable Figures page |
| 5 | Factor Tessaly Brightwater | Caravan Court factor | Access to one shipment manifest (cargo, consignee, route) for the last tenday | **Invented** |
| 6 | Guildmaster Piers Hobb | Dock Ward haulers' guild | One favor from the guild: hold a cart, a wagon or a quay hand for one day, or tell what moved at night | **Invented** |
| 7 | Clerk Maelith Dray | Palace chancery under-clerk | One appointment slot with a named official inside 3 days, or one stamped copy of a public document | **Invented** |
| 8 | Lady Perrine Ostler | Sea Ward patron, Seawatch Charitable Fund | An invitation to one Sea Ward gathering, with one introduction at it | **Invented** |

- **Limits:** one introduction a quest; it never buys a secret, a favor against the Alliance or an act against the Watch. The collision check for the four invented surnames was not run (no search tool this session).
- **Jelenn Urmbrusk is excluded** on purpose: her page makes her a Masked Lord under blackmail, so she cannot be a casual introduction.

### 9b. r10 Stingblade: Legal Coverage

- **Ceiling: 500 gp an incident, one incident a quest.** It covers bail, fines and damages together. The incident must be genuine (an arrest, a charge or a damages claim) and not a business debt. It never covers a crime against the Alliance, a Lord or the Watch.

| Item | Typical cost | Covered |
|---|---|---|
| Bail, minor assault or brawl | 50 gp | yes |
| Fine, unlicensed weapon or breach of the peace | 25 gp | yes |
| Damages, a brawl in a tavern or shop | 100 to 300 gp | yes, to the ceiling |
| Damages, arson of a shop | up to 500 gp | yes, to the ceiling |
| Bail, murder or treason | above the ceiling | no |
| Debts to a guild or lender | any | no |

- The 500 gp scale matches the 500 gp bribe in M3. These amounts are mine; no 2024 or source figure was read.

### 9c. r10 Stingblade: Watch files

A standard file takes **1 hour**. A classified file takes **4 hours and a DC 12 Charisma (Persuasion) check** with the file officer; a failed check is flagged and the member retries after a tenday. Companions can read what the member copies out, but only the member can ask.

| File | Class | What it holds |
|---|---|---|
| Ward incident logs (any one ward, the last tenday) | Standard | Reports, times and Watch patrol sightings |
| Warrants outstanding | Standard | Names, charges and the requesting magistrate |
| Missing persons ledger | Standard | Names, last known place, date reported |
| **Archer case file (M4)** | Standard | Three killings by hand crossbow, the shot angles, and the north-facing window; a **free fourth lead** for the Pell Street room |
| **Fentree death report (M5)** | Standard | "Natural causes", and the Watch clerk's note that the study had been searched; a free lead to the Green Dragon booking |
| Patrol rotations (any one ward) | Standard | The three daily windows, by street |
| Splinter inquiry file | Classified | An unsolved report of unusual cart and carriage traffic at a Trades Ward safe house; no names. Says "the Splinter" |
| Xanathar's Guild informant file | Classified | A Castle Ward rowhouse with night-time stretchers; two sworn complaints; no arrests |
| Household inquiries file | Classified | Three closed inquiries against a Sea Ward house: a missing servant, a debt dispute and a noise complaint. All dismissed. No suspicion beyond that |
| Harbor master's carnival file | Classified | Berth inspections of the carnival fleet; all passed. Says "the carnival fleet" |
| Informant identifications | Classified | Partial names of informants the Watch has paid; the volunteered detail in the source |

### 9d. r25 Warduke: Response-team intelligence (one sheet every 3 days)

- **Cadence:** a sheet arrives every third day. If none arrives by the fourth day, a team has moved or the courier is compromised.
- **Position rule (mine):** the sheet gives the ward of the team's last encounter with the party; if the party has not met it, the ward of the faction's most recent outpost the party hit; if neither, "not located".
- **Names:** a team is named on the sheet only after the member has met it. Until then it is "the first crew", "the next crew" or "the third crew". The Splinter is "the Splinter". The Cassalanter crews are "unconfirmed, credible" until the member has met one. The fourth faction is "the carnival fleet" until **Jarlaxle Unmasked**. No sheet mentions imps, devils, a pact or Manshoon by name until **Manshoon Named**.

| Faction (as the sheet labels it) | Crew on the ladder | Make-up on the sheet | Named after the member has met it |
|---|---|---|---|
| Xanathar's Guild | First | A leader and four fighters from underground stock; sent to teach a lesson | Gorath's team |
| Xanathar's Guild | Second | A leader, three fighters from underground stock, a half-ogre and a floating one-eyed creature | Korgstrod Uxgulm's team |
| Xanathar's Guild | Third | A leader, six large hired fighters and the same floating one-eyed creature; sent when the Guild wants the problem gone | Noska Ur'gray's team |
| The Splinter | First | A lieutenant who fights with a blade and three or four hired hands; orders are to take prisoners | Vevette Blackwater's crew |
| The Splinter | Second | A lieutenant who talks and three or four hired hands; orders are to take prisoners | Agorn Fuoco's crew |
| The Splinter | Third | A hired killer and three or four hired hands; available only if he survived Gralhund Villa | Urstul Floxin's crew |
| The Cassalanter household (unconfirmed, credible) | First | A lead retainer, two quiet watchers, one hired guard and a fifth who is never seen clearly | Seffia Naelryke's crew |
| The Cassalanter household (unconfirmed, credible) | Second | A man who gives the name Willifort Crowelle, three hired hands in plain robes and one heavy escort | Willifort's crew |
| The carnival fleet | Standing | One or two armed lieutenants and four to eight crew; they prefer misdirection and delay to killing | The lieutenants' names |

- **Source:** `campaign/guides/factions/09-xanathars-guild.md`, `10-manshoons-zhentarim.md`, `11-cassalanters.md` and `08-bregan-daerthe.md` (Response Teams sections). The wording above hides creature types that would reveal a pact (imp, devil, doppelganger, cultist) and the drow composition of the carnival crews.
- **Open item:** the Splinter and Xanathar teams carry orders and loot that the guides keep for play; the sheet never reproduces them.

### 9e. r25 Warduke: the Masked Lord request (one per quest)

The member submits a written request to Jalester naming one of these forms. **The Lord is a Masked Lord of Waterdeep who owes Laeral and is never named.** GM-only: the Lord is **not Mirt** (the Harpers' Lord) and **not Jelenn Urmbrusk** (her page makes her a Masked Lord under blackmail). Jalester says "a Lord I will not name". The forms are distinct from the Harper r50 forms (Watch cooperation, Lords' Court hearing, warrant of immunity).

| Form | What it does | The member names | Delivery | Limits and refusals |
|---|---|---|---|---|
| **Door** | A sealed door opens: one locked or sealed civic, guild or records room is entered under a Lord's key-warrant | The room, the reason and the hour | The fourth morning after Jalester accepts; the warrant admits the member and up to four companions for one hour | Not a temple, a noble's private house or an Alliance office. Takes nothing out except copies |
| **Seal** | An investigation is sealed: the Watch freezes one named inquiry for ten days (no searches, no arrests, no records read) | The inquiry (by subject and ward) | The fourth morning; the freeze lasts ten days | Not a murder or treason inquiry, and not one into the Alliance or a Lord. Does not end the inquiry; it ends after ten days |
| **Pressure** | A letter of political pressure to one guild master, magistrate or noble house | The target and one narrow ask: a delay, a meeting or a signature | The fourth morning; the target does what the letter asks unless it costs more than a tenday's income | The target is not coerced beyond politics and may refuse; the Lord does not give the member's name |

- **Spent** only when Jalester accepts. A discussion, a refusal or a withdrawn draft spends nothing. He gives his reason for a refusal before the use is spent.
- **Refused** for anything that harms the city, hides an attack on non-combatants or needs authority beyond Waterdeep.

## Verification

Source key: **XMM** = `bestiary-xmm.json`, **XPHB** = `spells-xphb.json`, both in the scratchpad `5e/` folder, read directly this session by line range. **Skill** = `cr2-encounter-builder`. **Rep 02/03/04** = the Lords' Alliance research reports. **Brief** = `lords-alliance-conversion-brief.md`. **EE** = `emerald-enclave-mechanics-reference.md`.

| Item | Source | Status | Value used |
|---|---|---|---|
| Party Power by level, Day Costs, bands, Tier 1/2/3 Power by CR | Skill | Verified | Method and section 1 |
| Carrion Crawler | XMM lines 12681-12784 | Verified | CR 2, Large Monstrosity, AC 13, HP 51, Speed 30 / Climb 30, Bite +4 7 + 3 poison, Tentacles Con DC 12 Poisoned then Paralyzed, Spider Climb |
| Guard | XMM lines 30390-30479 | Verified | CR 1/8, AC 16, HP 11, Spear +3 4 |
| Commoner | XMM lines ~14480-14570 | Verified | CR 0, AC 10, HP 4, Club +2 2 |
| Bandit | XMM lines ~7960-8072 | Verified | CR 1/8, AC 12, HP 11, Scimitar +3 4, Light Crossbow +3 5 |
| Bandit Captain | XMM lines 8073-8188 | Verified | CR 2, AC 15, HP 52, Multiattack two, Scimitar +5 6, Pistol +5 8 range 30/90, Parry |
| Kenku | XMM lines 34351-34470 | Verified | CR 1/4, AC 13, HP 13, Mimicry, Shadow Blade +5 6 necrotic, Eldritch Lantern (Recharge 4) Faerie Fire DC 10 |
| Tough | XMM lines 55328-55424 | Verified | CR 1/2, AC 12, HP 32, Pack Tactics, Mace +4 5, Heavy Crossbow +3 6 |
| Tough Boss | XMM lines 55425-~55540 | Verified | CR 4, AC 16, HP 82, Multiattack two, Warhammer +5 12 push 10, Heavy Crossbow +4 13 |
| Mage | XMM lines 36670-~36850 | Verified | CR 6, AC 15, HP 81, three Arcane Bursts +6 16, DC 14, Fireball (L4) 2/day, Invisibility 2/day, Cone of Cold 1/day, Fly 1/day, Misty Step 3/day, Protective Magic 3/day |
| Spy | XMM lines 52642-52752 | Verified | CR 1, AC 12, HP 27, no Multiattack, Shortsword +4 5 + 7 poison, Hand Crossbow +4 5 + 7 poison, Cunning Action |
| Noble | XMM lines 41342-~41440 | Verified | CR 1/8, AC 15, HP 9, Rapier +3 5, Parry, Deception +5 Insight +4 Persuasion +5 |
| Warrior Veteran | XMM lines 58845-~58955 | Verified | CR 3, AC 17, HP 65, Greatsword +5 10 x2, Heavy Crossbow +3 12, Parry |
| *Fireball* | XPHB lines 8086-8150 | Verified | Level 3, 20-ft. radius, Dex save, 8d6, +1d6 per slot above 3 (level 4 = 9d6) |
| *Invisibility* | XPHB lines 11459-11520 | Verified | Level 2, action, touch, concentration 1 hour, ends on attack, damage or casting |
| *Misty Step* | XPHB lines 13554-13592 | Verified | Level 2, bonus action, V, teleport 30 ft. to an unoccupied space you can see |
| *Counterspell*, *Shield*, *Cone of Cold*, *Fly* texts | none | **Unverified** | Not read. Named only as the Mage block lists them |
| 2024 Paralyzed (Advantage on attacks, crit within 5 ft.) | none | **Unverified in the downloaded data** | As in EE; the Crawler section depends on it |
| 2024 falling damage, grapple rules, chase rules | none | **Unverified** | Not used in any roster |
| Archmage (Laeral) stats | Rep 04 section 7 | **Unverified here** | Not used in any math |
| Rep 03/04 stat values (Bandit, Captain, Kenku, Mage, Tough, Tough Boss, Spy, Warrior Veteran, Guard, Crawler) | Rep 03 section 3.1, Rep 04 section 7 | Re-checked against XMM | All matched |
| Heuristics (0.71 for half pool; sqrt for any loss fraction; M1 wound; M3 effective Power and rounds check; M5 stair rule) | Mine | **Mine** | Not skill rules |
| Chase clock (M4), Rezka's flight track, Crawler prey rule and 60-ft. start, Esloon safeguards and backstop round, kenku four-round Watch clock | Mine | **Mine** | Design choices (kenku clock: four rounds from R) |
| Introductions (rows 5 to 8), legal-coverage amounts, Watch-file contents, response-team sheet wording, Masked Lord forms | Mine | **Mine** | Invented names marked |
| Ossery Klenn as a Noble; Emira Volstren as a Noble; Rezka as a Spy; bodyguards as Tough Boss and Toughs | Brief, Rep 04 | Chosen | Section 6 |
| `campaign/structure/appendix-a-npc-roster.md` | none | **Not found** | The roster check cannot run (as in EE). Notable Figures pages exist for Barnibus Blastwind, Torlyn Wands, Saeth Cromley, Valetta, Esloon Bezant, Jalester, Laeral, Jelenn Urmbrusk. Invented: Berna, Herath, Mareva Coile, Harko Swornhold, Lira, Veralax, Sarvos Miln, Vhaspar Coldwater, Halek Farran, Ossery Klenn, Emira Volstren, Rezka, Sevel Dastar and the four Introductions in 9a |

### Corrections and open items

- **Report 03, M1 crawler:** it called the fight Impossible at every size using a +4 reading of 190% to 360%. With the prey rule and the 60-ft. start, no +4 applies. The listed bands are Bloody / Bruising / Mild; with the 3-PC wound, Bruising / Bruising / Mild.
- **Report 03, M3 (Mage Apprentice):** overruled by the user. Esloon is the full Mage. The Apprentice rosters in the report are not used.
- **Report 04, M5:** its rosters used Noska as the bidder; the brief replaced him with Ossery Klenn. The Tough Boss stat line is reused for the bodyguard captain, with Noska absent.
- **M3 convention:** the governing band uses Esloon's effective Power (withdrawal enforced). On the plain table his rosters are 134.4% / 108.9% / 94.9% (Crushing / Overwhelming / Oppressive). If the main session wants the plain-table guarantee, run lone Esloon with no crew at every size (134.4% / 75.6% / 48.4%).
- **BD m03 :226:** patrol at round five against the r03 clause of 1d4 + 1 minutes. Logged, not resolved.
- **Open:** no r25 private-audience table was built (not requested). Jelenn Urmbrusk's page makes her a Masked Lord; the request table excludes her as well as Mirt.
- **Name collisions:** not checked for the invented names (no search tool this session).
