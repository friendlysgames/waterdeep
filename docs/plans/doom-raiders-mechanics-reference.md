# Doom Raiders Mechanics Reference

CR 2.0 audits for every Doom Raiders faction-event hazard, at three, four and five participating combatants. Filled in by the encounter-builder agent, Session 38.

## Method and conventions

- CR 2.0 only. Party Power from the level table (L2 14, L4 23, L5 32, L6 35, L7 41, L8 44). Monster Power from the tier-adjusted table (L1-4 Tier 1; L5-10 Tier 2).
- % HP lost = (Enemy Power / Party Power) squared. Budget = Party Power x multiplier.
- "Standard" in this file = Bruising (20-40% HP lost, Day Cost 4). "Hard" = Bloody (40-60%, Day Cost 6). Mild = 2, Brutal = 8.
- Waves are separate encounters; Day Costs add. Where I add wave percentages to show a whole-mission total, that is a rough heuristic of mine, not a skill rule.
- Combatant counts include non-member companions. Bystanders, victims and NPCs who do not fight (Heldar, the commuters, Ziraj by default) are not counted.
- Flee-at-half-HP heuristic (mine, not a skill rule): Power is the square root of HP x DPR, so a foe who leaves at half HP contributes about 0.71 of its listed Power. Verdicts below use full Power, so real losses run a little lower.
- **Stat-block caveat.** No 2024 Monster Manual text exists in the repo and no rules-lookup tool was available to me. Every CR and stat below is from memory and must be checked (see Verification at the end).

## 1. M1 The Dockside Killer (level 2, Tier 1)

| PCs | Party Power | Bruising budget (x0.6) | Bloody budget (x0.75) |
|---|---|---|---|
| 3 | 42 | 25.2 | 31.5 |
| 4 | 56 | 33.6 | 42 |
| 5 | 70 | 42 | 52.5 |

Monster Power (Tier 1): Scout CR 1/2 = 16; Bandit CR 1/8 = 4; Tough CR 1/2 = 16.

**Draft roster (Soluun alone, Scout = 16):**

| PCs | Enemy / Party | % HP lost | Verdict | Day Cost |
|---|---|---|---|---|
| 3 | 16/42 | 14.5% | Mild | 2 |
| 4 | 16/56 | 8.2% | Below Mild | 2 |
| 5 | 16/70 | 5.2% | Below Mild | 2 |

Verdict: trivial as a fight at every size, and he leaves at 8 HP, so the pursuit carries the scene. Yes, he needs help. Because he kills from personal hatred with no authorization, do not give him Bregan D'aerthe muscle. Give him one or two hired hands from the docks (Luskan sailors he paid to watch the flanks), who never know his name.

**Recommended rosters:**

| PCs | Standard (Bruising) | Power | % lost | Hard (Bloody) | Power | % lost |
|---|---|---|---|---|---|---|
| 3 | Scout + 2 Bandits | 24 | 32.7% (cost 4) | Scout + Tough | 32 | 58.0% (cost 6) |
| 4 | Scout + Tough | 32 | 32.7% (cost 4) | Scout + Tough + Bandit | 36 | 41.3% (cost 6) |
| 5 | Scout + Tough + 2 Bandits | 40 | 32.7% (cost 4) | Scout + 2 Tough | 48 | 47.0% (cost 6) |

Thresholds:
- Soluun disengages at 8 HP (half) and takes the roofline; this is already in the draft.
- Hired hands flee when Soluun flees or when either of them is reduced to 0. They surrender if cornered.
- A cornered Soluun surrenders instead of jumping (draft: three DC 14 Athletics successes before three failures).
- Non-combat route: spotting him first (DC 18 Perception) lets the party walk Heldar out and talk to Soluun; the hirelings then have no reason to fight.

Notes: the ambush round is about 10 damage from two Scout attacks, enough to drop a 2nd-level caster on 8 HP but not to trip the "kills a PC on turn one" CR +4 rule. Drow Sunlight Sensitivity is not on a Scout; ignore it.

## 2. M3 The Missing Snobeedle (level 4, optional Shard Shunner fight, Tier 1)

Wererat CR 2 = 28; Giant Rat CR 1/8 = 4; Tough CR 1/2 = 16. Party Power 69 / 92 / 115. Bruising budget 41.4 / 55.2 / 69; Bloody 51.75 / 69 / 86.25.

| Wererats | Power | 3 PCs (69) | 4 PCs (92) | 5 PCs (115) |
|---|---|---|---|---|
| 2 | 56 | 65.9% Brutal (8) | 37.1% Bruising (4) | 23.7% Bruising (4) |
| 3 | 84 | 148% Crushing (17) | 83.4% Oppressive (10) | 53.4% Bloody (6) |
| 4 | 112 | 263% Impossible (50) | 148% Crushing (17) | 94.9% Oppressive (10) |

Verdict: 2 wererats is right for 4-5 PCs only. Three or four are lethal below 5 PCs.

**Recommended rosters:**

| PCs | Standard (Bruising) | Power | % lost | Hard (Bloody) | Power | % lost |
|---|---|---|---|---|---|---|
| 3 | 1 Wererat + 2 Giant Rats | 36 | 27.2% (4) | 1 Wererat + Tough | 44 | 40.7% (6) |
| 4 | 2 Wererats | 56 | 37.1% (4) | 2 Wererats + 2 Giant Rats | 64 | 48.4% (6) |
| 5 | 2 Wererats + Tough | 72 | 39.2% (4) | 3 Wererats | 84 | 53.4% (6) |

Thresholds:
- Kelso calls the fight off when Dasher or a wererat is bloodied, or when any PC drops to 0.
- Each wererat yields at 1/3 HP (20) and retreats to the den; the Shunners stop chasing at the den door.
- Non-combat route: DC 14 Persuasion or Kelso's arranged terms end it at any point (draft).
- Lycanthropy: the Shunners fight in halfling (humanoid) form with weapons unless enraged, so the party is not cursed by a routine brawl. If the DM uses the bite, name the save and the cure up front; Dasher's own path is a choice, not an infection.
- Silvered or magical weapons: I believe the 2024 Wererat resists nonmagical, non-silvered damage in some forms. A 4th-level party has no consistent magic, so no CR reduction applies, but that resistance would raise the difficulty one step. Verify.

## 3. M4 Silencing Skeemo (level 5, Tier 2)

Mage CR 6 = 65; Tough CR 1/2 = 12; Warrior Veteran CR 3 = 30. Party Power 96 / 128 / 160. Bruising budget 57.6 / 76.8 / 96; Bloody 72 / 96 / 120.

| PCs | Enemy / Party | % HP lost | Verdict | Day Cost |
|---|---|---|---|---|
| 3 | 65/96 | 45.8% | Bloody | 6 |
| 4 | 65/128 | 25.8% | Bruising | 4 |
| 5 | 65/160 | 16.5% | Mild | 2 |

High-Power warning: 65 is more than 2x a 5th-level PC (32 x 2 = 64), so Skeemo can drop a PC with one Fireball. The dray full of commuters is what stops him from casting it, so do not let him.

**Recommended rosters:**

| PCs | Standard (Bruising) | Power | % lost | Hard (Bloody) | Power | % lost |
|---|---|---|---|---|---|---|
| 3 | Mage at 2/3 HP (54) after the shop scuffle | 53 | 30.5% (4) | Mage at full HP | 65 | 45.8% (6) |
| 4 | Mage alone | 65 | 25.8% (4) | Mage + Warrior Veteran (escort) | 95 | 55.1% (6) |
| 5 | Mage + Tough (escort) | 77 | 23.2% (4) | Mage + Veteran + Tough | 107 | 44.7% (6) |

(A Mage at 2/3 HP = 65 x sqrt(2/3) = about 53.) The escorts trail the dray on foot; the driver and five commuters stay bystanders.

**Concentration rules for the chase (fixes the draft):**
- *Fly* (3rd level, Concentration, 10 minutes) and *greater invisibility* (4th level, Concentration, **1 minute**, not 10) cannot run together. Casting the second ends the first and he falls.
- Rooftop chase: he casts *Fly* on round 1 and stays visible. Do not add invisibility.
- Street/crowd chase: he casts *greater invisibility* and runs on foot for at most 10 rounds; DC 20 Perception or *detect magic* follows him.
- I do not think the 2024 Mage lists *greater invisibility* (I recall *invisibility* and *fly* among its 1/day spells). Treat it as a swap for one of them and keep Skeemo's spell list otherwise as printed. Verify.

Thresholds:
- He flees from round 1 by design. He surrenders when cornered at 40 HP (half) or fewer, or after both Misty Step and Fly are spent.
- Escorts flee when Skeemo is captured, or at half HP.
- Non-combat route: the double-agent gambit (Insight DC 18 partial truth, DC 14 fear) ends the fight in a capture.

## 4. M5 The Yellowspire Job (level 6, Tier 2)

Mage CR 6 = 65; Priest Acolyte CR 1/4 = 6 (unverified; see below); Spy CR 1 = 17; Warrior Veteran CR 3 = 30. Party Power 105 / 140 / 175. Bruising budget 63 / 84 / 105; Bloody 78.75 / 105 / 131.25.

**Draft roster as written** (Mage + 3 Spies on the two floors = 116 Power; reinforcement wave of 4 Spies = 68):

| PCs | Wave 1 % lost | Wave 2 % lost | Costs |
|---|---|---|---|
| 3 | 122% Overwhelming | 41.9% Bloody | 13 + 6 |
| 4 | 68.7% Brutal | 23.6% Bruising | 8 + 4 |
| 5 | 43.9% Bloody | 15.1% Mild | 6 + 2 |

Verdict: overwhelming at 3 PCs if the floors ever fight together, and the wave is a fixed size regardless of party. The mission is a stealth heist, so the floors should fight separately; the sizing below assumes the worst case.

**Recommended (standard visit, acolytes replace the sleeping agent):**

| PCs | Wave 1 | Power | % lost (cost) | Wave 2 (10-minute clock) | Power | % lost (cost) | Whole mission |
|---|---|---|---|---|---|---|---|
| 3 | Mage + 1 Priest Acolyte | 71 | 45.7% Bloody (6) | 2 Spies | 34 | 10.5% Mild (2) | about 56%, cost 8 |
| 4 | Mage + 2 Priest Acolytes | 77 | 30.3% Bruising (4) | 3 Spies | 51 | 13.3% Mild (2) | about 44%, cost 6 |
| 5 | Mage + 4 Priest Acolytes | 89 | 25.9% Bruising (4) | 4 Spies | 68 | 15.1% Mild (2) | about 41%, cost 6 |

**Reinforced return visit (Faction Outposts 5B ran):**

| PCs | Wave 1 | Power | % lost (cost) | Wave 2 | Power | % lost (cost) | Whole mission |
|---|---|---|---|---|---|---|---|
| 3 | Mage + 2 Priest Acolytes | 77 | 53.8% Bloody (6) | 3 Spies | 51 | 23.6% Bruising (4) | about 77%, cost 10 |
| 4 | Mage + 4 Priest Acolytes | 89 | 40.4% Bloody (6) | 4 Spies | 68 | 23.6% Bruising (4) | about 64%, cost 10 |
| 5 | Mage + 4 Priest Acolytes + Warrior Veteran | 119 | 46.2% Bloody (6) | 5 Spies | 85 | 23.6% Bruising (4) | about 70%, cost 10 |

Cost 10 sits between Draining (9) and Debilitating (12) on the fatigue table. Agorn Fuoco (one-in-three per arc-e) is a named NPC; his stats are not set here. If he appears, remove the Veteran and one Spy per Power swapped, and stat him through boss-design or as a Mage.

Sensitivity: if Priest Acolyte turns out to be CR 2 (Power 23), replace each acolyte's 6 with 23 and drop two acolytes at every size.

Thresholds:
- Acolytes flee or yield when the first ally falls or at half HP.
- The Mage counterspells the first visible spell of 1st level or higher, then falls back toward the circle; she yields at 1/4 HP (about 20) and will not use the circle while the party is adjacent.
- Wave 2 Spies disengage once two of them are down or the ledger holder has left the building.
- Clock trigger: the wave arrives ten minutes after anyone steps into the circle without pressing the northeast plate, or after the Mage raises an alarm.
- Non-combat routes: coded knock, rooftop, referral cover (draft).

## 5. M6 Ziraj's Last Hunt (level 7, after Kolat Towers, Tier 2)

Assassin CR 8 = 85; Warrior Veteran CR 3 = 30; Spy CR 1 = 17. Party Power 123 / 164 / 205. Bruising budget 73.8 / 98.4 / 123; Bloody 92.25 / 123 / 153.75.

**Draft roster (3 Spies = 51):**

| PCs | % HP lost | Verdict | Day Cost |
|---|---|---|---|
| 3 | 17.2% | Mild | 2 |
| 4 | 9.7% | Below Mild | 2 |
| 5 | 6.2% | Below Mild | 2 |

Verdict: trivial for a mission that closes the chain.

**Leader options:**

| Roster | Power | 3 PCs | 4 PCs | 5 PCs |
|---|---|---|---|---|
| Assassin alone | 85 | 47.8% Bloody | 26.9% Bruising | 17.2% Mild |
| Assassin + 1 Spy | 102 | 68.8% Brutal | 38.7% Bruising | 24.8% Bruising |
| Assassin + 2 Spies | 119 | 93.6% Oppressive | 52.7% Bloody | 33.7% Bruising |
| Assassin + 3 Spies | 136 | - | - | 44.0% Bloody |
| Assassin + Veteran + 2 Spies | 149 | - | - | 52.8% Bloody |
| Veteran + 2 Spies | 64 | 27.1% Bruising | - | - |

**Recommended rosters:**

| PCs | Standard (Bruising) | % lost (cost) | Hard (Bloody) | % lost (cost) |
|---|---|---|---|---|
| 3 | Warrior Veteran + 2 Spies | 27.1% (4) | Assassin alone | 47.8% (6) |
| 4 | Assassin + 1 Spy | 38.7% (4) | Assassin + 2 Spies | 52.7% (6) |
| 5 | Assassin + 2 Spies | 33.7% (4) | Assassin + Veteran + 2 Spies | 52.8% (6) |

Notes:
- High-Power warning: Assassin (85) is more than 2x a 7th-level PC (82). With surprise it can kill a caster in one turn, which would trigger CR +4. The draft gives the party the initiative advantage; keep that, and if the Assassin ever gets a surprise round, treat the fight as a step harder.
- Ziraj is not counted: wounded, Disadvantage on the bow, and a potential objective. If he fights, that adds a second Assassin-class ally (Power 85 at full strength, roughly half if wounded), which erases the challenge. Keep him as a sniper for two rounds at most.
- Modify the leader with a Splinter-issue tell (a grooved-tip crossbow bolt, per Fala's report), not with extra stats.

Thresholds:
- Spies disengage and report when two of the team are down or when the leader falls (draft).
- Leader retreats at half HP if an ally has fallen; the Assassin will not surrender, but will trade information for her life if paralyzed or held.
- The team is not a suicide squad: a kill team that reports back is worth more than one that dies (draft).
- Non-combat route: leading them away from Ziraj (DC 14 Deception or a planted trail).

## 6. r50 Ally Power: Dread Lord operatives (8-operative pool)

r50 is Dungeon of the Mad Mage content; assume level 8-10 (Tier 2). Level 8 Party Power is 44 each: 132 / 176 / 220. Tier 3 is provided in case the party has reached level 11.

**Pool (proposed composition):**

| Operative | CR | Count | Power each (T2) | Power each (T3) | T2 total | T3 total |
|---|---|---|---|---|---|---|
| Mage | 6 | 1 | 65 | 50 | 65 | 50 |
| Warrior Veteran | 3 | 2 | 30 | 25 | 60 | 50 |
| Spy | 1 | 2 | 17 | 15 | 34 | 30 |
| Tough | 1/2 | 2 | 12 | 7 | 24 | 14 |
| Priest Acolyte | 1/4 | 1 | 6 | 5 | 6 | 5 |
| **Pool** | | **8** | | | **189** | **149** |

Deployment packages (Davil sets operational limits; use one package per operation):

| Package | Members | Power (T2) |
|---|---|---|
| Strike Team | Mage, Warrior Veteran, Spy, Tough | 124 |
| Cover Team | Warrior Veteran, Spy, Tough, Priest Acolyte | 65 |
| Full pool | all eight | 189 |

**Party Power and budgets with allies (level 8):**

| PCs | Base | + Cover (65) | + Strike (124) | + Full (189) |
|---|---|---|---|---|
| 3 | 132 | 197 (Bruising budget 118) | 256 (154) | 321 (193) |
| 4 | 176 | 241 (145) | 300 (180) | 365 (219) |
| 5 | 220 | 285 (171) | 344 (206) | 409 (245) |

Guidance:
- The full pool roughly doubles a 4-PC party, so a fight built for the base party is trivial with it. Rebuild the encounter from the allied Party Power, or cap deployment at the Cover Team unless the operation is meant to be a set piece.
- Ally Power counts in full under the skill's rule. For a "one major operation" allotment, expect operatives to be spent (one casualty per package is a fair cost) rather than recovered.
- Recommended default: Strike Team for assault operations, Cover Team for extraction and distraction. The Vault partnership crews (distraction, locksmith, wagon team) are non-combat and add no Power.

## Verification

Confirm each against the 2024 Monster Manual before drafting.

| Name | Status | Note |
|---|---|---|
| Scout, Bandit, Spy, Assassin, Mage, Wererat | Names confident | CRs 1/2, 1/8, 1, 8, 6, 2. Mage spell list and Assassin details unverified. |
| Warrior Veteran | Name confident | Renamed from Veteran; CR 3. |
| Tough | Fairly confident | Replaces Thug in 2024, CR 1/2. Verify the exact name and that Thug is gone. |
| Priest Acolyte | **Unverified CR** | Name given by caller; I assumed CR 1/4. If CR 2, see sensitivity note in section 4. |
| Giant Rat | Confident | CR 1/8. |
| Wererat form resistances | **Unverified** | Affects section 2 difficulty. |
| Mage *greater invisibility* | **Unverified** | Probably not on the 2024 list; treat as a swap. |
| *Greater invisibility* duration | Confident | 1 minute, Concentration. The draft's ten minutes is wrong. |
| Agorn Fuoco | Not statted | Named NPC, out of scope here. |
