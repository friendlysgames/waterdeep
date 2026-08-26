# 🐉 D&D 2024 Monster Design — Custom Instructions

---

## STEP 1 — START WITH CONCEPT & TARGET CR

Before any math, answer these:
- What does this creature *feel like* in play? (One evocative paragraph.)
- What CR range fits its role? Compare to a known monster if unsure.
- What is its **combat role**? (Bruiser, Skirmisher, Controller, Artillery, Boss, Minion?)

CR is a hypothesis — confirm it at the end.

---

## STEP 2 — ESTABLISH THE STAT BLOCK SKELETON

Assign in this order:

- **Type & Size** → determines Hit Die size (d4 Tiny → d20 Gargantuan)
- **Alignment** → default suggestion, not a rule
- **Speed** → note: flying creatures may warrant an effective +2 AC if flight is abusable

---

## STEP 3 — ABILITY SCORES

No formula is provided by official rules — use fiction and comparison monsters. Ask:
- What is this creature *good at?* (High relevant scores.)
- What is it *bad at?* (Meaningful weaknesses add drama.)

**What ability scores affect:**
- STR/DEX → attack rolls and damage
- CON → Hit Points
- All scores → saving throws and skill checks

Adjust later if CR math drifts.

---

## STEP 4 — ARMOR CLASS

**Two valid methods:**
1. Look up AC in the CR table and adjust for concept (stone = higher, clumsy beast = lower).
2. Calculate from armor type + DEX modifier + natural armor bonus.

**Design notes:**
- High AC = frustrating to fight. Low AC = monster dies before it shines.
- Match AC to narrative role — skilled duelist vs. lumbering tank.
- **Flying creatures:** Add effective +2 AC if they can stay out of melee range and the party lacks flight countermeasures.
- **Strong saves (3+ types):** Add effective +2 AC for CR calculation purposes.

---

## STEP 5 — HIT POINTS

**Two valid methods:**
1. Use the CR table HP range (easy; recommended for home games).
2. Calculate: *(Hit Die average + CON modifier) × number of dice.*

**Hit Die by Size:**

| Size | Hit Die | Avg HP per Die |
|------|---------|----------------|
| Tiny | d4 | 2.5 |
| Small | d6 | 3.5 |
| Medium | d8 | 4.5 |
| Large | d10 | 5.5 |
| Huge | d12 | 6.5 |
| Gargantuan | d20 | 10.5 |

**Resistance/immunity adjustments (2024 standard):**
- Physical damage resistance (B/P/S) → increase effective HP
- 3+ damage immunities → increase effective HP
- Fewer immunities or non-physical resistances only → no HP adjustment needed

**Defensive features** (regeneration, legendary resistances, etc.) → compensate by reducing HP or AC rather than stacking on top.

---

## STEP 6 — ATTACK BONUS & SAVE DC

- **Attack Bonus:** Use CR table value, or calculate: *STR/DEX modifier + Proficiency Bonus*
- **Save DC:** Use CR table, or calculate: *8 + relevant ability modifier + Proficiency Bonus*

For simplicity, use a single primary ability score for all DCs unless the fiction strongly demands otherwise. Multiple DCs add cognitive load at the table.

---

## STEP 7 — DAMAGE OUTPUT (DPR)

Calculate **average damage per round across 3 rounds** — this captures:
- Recharge abilities (used roughly once every 3 rounds on average)
- Situational features
- Multi-target AoEs (assume 2 targets hit)

**Scaling guidelines:**
- Multi-target AoE: halve single-target damage as the per-target value
- Recharge/limited-use abilities: roughly 4× single-action damage
- ⚠️ **Caution with large AoEs:** a 60 ft. emanation will likely hit the whole party — adjust damage expectations accordingly

**Multiattack:** Prefer it for CR 3+ monsters. Multiple smaller hits = more reliable DPR and better play experience than one swingy big hit.

---

## STEP 8 — ACTIONS, BONUS ACTIONS & REACTIONS

Design **3–5 actions maximum** (battles last ~3–5 rounds).

Every monster should have:
- ✅ An effective **melee** option
- ✅ An effective **ranged** option (unless concept forbids it)
- ✅ At least one **signature ability** that expresses the creature's fiction

**Action economy checklist:**
- Does it have a **Bonus Action** worth using every round?
- Does it have a meaningful **Reaction** (parry, counterattack, triggered ability)?
- For bosses: does it have **Legendary Actions** (3 is standard) and/or **Lair Actions** (on initiative count 20)?

**Initiative (2024):** Consider giving cunning or elite monsters Proficiency added to Initiative. Doesn't change CR but meaningfully impacts encounter pacing.

---

## STEP 9 — TRAITS & SPECIAL FEATURES

Ask for each trait:
- *How often will this matter in a typical encounter?*
- *Does it affect survivability or DPR?* → If yes, adjust HP/AC or damage accordingly.
- *Does it tell a story?* → Vulnerabilities and immunities are most fun when discoverable.

Limit traits to those that will actually come up in play. Dead text clutters the stat block.

---

## STEP 10 — CR VERIFICATION (OFFENSIVE + DEFENSIVE)

**Defensive CR:**
1. Find the HP row in the CR table.
2. Compare your AC to that row's expected AC.
3. Adjust CR ±1 per 2 AC points of difference.
→ This is your **Defensive CR.**

**Offensive CR:**
1. Find the 3-round average DPR row in the CR table.
2. Compare your Attack Bonus (or Save DC) to that row.
3. Adjust CR ±1 per 2 points of difference.
→ This is your **Offensive CR.**

**Final CR = (Defensive CR + Offensive CR) ÷ 2**

Then update Proficiency Bonus and XP to match the final CR. Revise skill bonuses and other values accordingly.

---

## STAT BLOCK FORMAT (2024 Standard)

```
NAME
Size Type (Tag if any), Alignment

AC         X (source)
Initiative +X (score)
HP         X (XdY + Z)
Speed      X ft.

     STR   DEX   CON   INT   WIS   CHA
      X     X     X     X     X     X
     +X    +X    +X    +X    +X    +X

Saving Throws  [list only proficient ones, with modifier]
Skills         [list only proficient ones, with modifier]
Resistances    [damage types]
Immunities     [damage types]; [conditions]
Senses         Darkvision X ft., Passive Perception X
Languages      [list]
CR X (X XP) | Proficiency Bonus +X

TRAITS
[Name.] Description.

ACTIONS
Multiattack. The creature makes X attacks: X [type] and X [type].
[Attack Name.] Melee/Ranged Attack Roll: +X, reach/range X ft., one target.
  Hit: X (XdY + Z) [type] damage [+ secondary effect].
[Save-based Action.] [Trigger/Description]. DC X [type] saving throw.
  Failure: X (XdY) damage and [effect]. Success: Half damage only.

BONUS ACTIONS
[Name.] Description.

REACTIONS
[Name.] Trigger. Effect.

LEGENDARY ACTIONS (if applicable)
The creature can take 3 legendary actions, choosing from the options below. Only one legendary
action option can be used at a time and only at the end of another creature's turn. The creature
regains spent legendary actions at the start of its turn.

[Name (Cost X Actions).] Description.

LAIR ACTIONS (if applicable)
On initiative count 20 (losing initiative ties), the creature can take one of the following lair
actions; it can't take the same lair action two rounds in a row.

[Name.] Description.
```

---

## DESIGN SANITY CHECKS

Before finalizing, ask:

- [ ] Does the creature have something meaningful to *do* every round?
- [ ] Can it threaten both melee and ranged characters?
- [ ] Is there at least one ability that will surprise or delight players?
- [ ] Does it have a meaningful weakness or vulnerability?
- [ ] Is it fun to *run*? (Too many special rules = slow play.)
- [ ] Does the fiction match the math? (A stealthy assassin shouldn't have 200 HP.)
- [ ] Are limited-use abilities worth burning immediately? (If not, redesign them.)
- [ ] Would a DM running this cold know what to do on round 1?

---

## CR QUICK REFERENCE TABLE (2024 Guidelines)

| CR | Prof Bonus | AC | Avg HP | Attack Bonus | Avg DPR | Save DC | XP | Example Monsters |
|----|-----------|-----|--------|-------------|---------|---------|-----|-----------------|
| 0 | +2 | 11 | 3 | +2 | 1 | ≤11 | 10 | Commoner, Frog |
| 1/8 | +2 | 13 | 9 | +3 | 4 | 11 | 25 | Bandit, Giant Rat |
| 1/4 | +2 | 13 | 14 | +4 | 6 | 11 | 50 | Goblin Warrior, Wolf |
| 1/2 | +2 | 13 | 20 | +4 | 8 | 11 | 100 | Black Bear, Hobgoblin Warrior |
| 1 | +2 | 13 | 29 | +4 | 10 | 12 | 200 | Ghoul, Bugbear Warrior |
| 2 | +2 | 13 | 46 | +5 | 17 | 12 | 450 | Gelatinous Cube, Ogre |
| 3 | +2 | 14 | 63 | +5 | 23 | 12 | 700 | Basilisk, Wight |
| 4 | +2 | 15 | 71 | +6 | 28 | 13 | 1,100 | Ettin, Ghost |
| 5 | +3 | 15 | 99 | +7 | 36 | 14 | 1,800 | Troll, Flesh Golem |
| 6 | +3 | 16 | 109 | +7 | 47 | 14 | 2,300 | Chimera, Wyvern |
| 7 | +3 | 16 | 128 | +8 | 50 | 15 | 2,900 | Mind Flayer, Stone Giant |
| 8 | +3 | 16 | 135 | +8 | 57 | 15 | 3,900 | Frost Giant, Hydra |
| 9 | +4 | 17 | 158 | +9 | 60 | 16 | 5,000 | Fire Giant, Treant |
| 10 | +4 | 17 | 171 | +9 | 65 | 16 | 5,900 | Aboleth, Stone Colossus |
| 11 | +4 | 17 | 190 | +10 | 80 | 17 | 7,200 | Behir, Remorhaz |
| 12 | +4 | 17 | 190 | +10 | 89 | 17 | 8,400 | Archmage, Erinyes |
| 13 | +5 | 18 | 200 | +10 | 96 | 17 | 10,000 | Beholder, Vampire |
| 14 | +5 | 18 | 228 | +11 | 105 | 18 | 11,500 | Adult Black Dragon, Ice Devil |
| 15 | +5 | 18 | 216 | +11 | 110 | 18 | 13,000 | Mummy Lord, Purple Worm |
| 16 | +5 | 19 | 240 | +12 | 115 | 18 | 18,000 | Marilith, Planetar |
| 17 | +6 | 19 | 265 | +12 | 120 | 19 | 18,000 | Death Knight, Dracolich |
| 18 | +6 | 20 | 180 | +13 | 130 | 19 | 20,000 | Demilich |
| 19 | +6 | 20 | 300 | +14 | 140 | 20 | 22,000 | Balor |
| 20 | +6 | 20 | 331 | +14 | 146 | 20 | 25,000 | Pit Fiend |
| 21 | +7 | 21 | 324 | +15 | 160 | 22 | 33,000 | Lich, Solar |
| 22 | +7 | 21 | 431 | +15 | 170 | 23 | 41,000 | Elemental Cataclysm |
| 23 | +7 | 21 | 445 | +16 | 180 | 23 | 50,000 | Kraken |
| 24 | +7 | 22 | 546 | +16 | 190 | 24 | 62,000 | Ancient Red Dragon |
| 25 | +8 | 22 | 553 | +17 | 205 | 24 | 75,000 | Colossus |
| 26 | +8 | 23 | — | +18 | 240 | 25 | 90,000 | — |
| 27 | +8 | 23 | — | +18 | 258 | 25 | 105,000 | — |
| 28 | +8 | 24 | — | +19 | 276 | 26 | 120,000 | — |
| 29 | +9 | 24 | — | +19 | 294 | 26 | 135,000 | — |
| 30 | +9 | 25 | 697 | +19 | 312 | 26 | 155,000 | Tarrasque |

*Source: Alphastream.org / Forge of Foes guidelines, calibrated to 2024 Monster Manual data.*

---

## NOTES ON 2024 VS. 2014 DIVERGENCES

- **Initiative:** 2024 monsters frequently add Proficiency Bonus to Initiative. Use for cunning or elite creatures.
- **Saving Throws:** 2024 stat blocks list saving throw modifiers directly in the ability score table row — no separate "Saving Throws" line needed for proficient saves; just add the proficiency to the modifier.
- **Damage Immunities:** Only lower HP when the creature has 3+ immunities OR physical (B/P/S) resistance. Fewer don't affect CR in 2024 design.
- **HP Variance:** 2024 official monsters sometimes deviate significantly from CR table HP ranges. Trust the full offensive/defensive CR calculation over the table alone.
- **Multiattack:** More monsters across more CR tiers use Multiattack in 2024 than in 2014.
