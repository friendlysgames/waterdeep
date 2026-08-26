# Commander Archetypes

Commanders are priority-challenge bosses. The party must triage — making cost/benefit decisions about competing targets and objectives under pressure. Every archetype in this document is defined by three elements drawn from the Commander puzzle list:

- **Defining Trait** — The primary split. What the party cannot fully address while also addressing everything else.
- **Strength** — The urgency mechanism. What gets worse while the party is failing to triage correctly.
- **Weakness** — The payoff. What becomes trivially manageable once the Defining Trait is resolved.

Archetypes are organized into three categories based on the *source* of the triage pressure:

- **Field Commanders** — The pressure comes from the boss's deployed assets. The encounter is a battlefield with too many meaningful targets.
- **Siege Commanders** — The pressure comes from a process or system the boss is sustaining. The encounter is a race against something the boss has set in motion.
- **Leverage Commanders** — The pressure comes from objectives and consequences. The encounter forces the party to decide what they are willing to lose.

**Archetype names describe encounter identity, not creature type or origin.** A Warlord may be a dragon directing its brood, a lich commanding undead, or a crime boss running a criminal network. A Puppet Master may be a mind flayer, a hag coven's matriarch, or a manipulative noble with agents throughout the city. The name is a shorthand for the triage structure the encounter imposes — not a template for what the boss looks like or where its power comes from.

---

## Puzzle Type Reference

| Puzzle Type | Triage State |
|---|---|
| **Targeting** | I can't figure out which target to kill first. |
| **Crisis** | I can't figure out which crisis to handle first. |
| **Sacrifice** | I can't figure out which objective to abandon. |
| **Division** | I can't figure out how to split the party. |
| **Escalation** | I can't figure out how to stop things getting worse. |

---

## Field Commanders

Field Commanders generate triage pressure through the assets they deploy and control. The encounter is fundamentally military: there are too many meaningful targets, and the boss is the reason they are all active simultaneously. Killing the boss without addressing the field is often impossible — not because the boss is invulnerable, but because the field keeps making the boss's job easier and the party's job harder.

**What distinguishes Field Commanders from each other** is the relationship between the targets. The Warlord's threats are independent actors that each enable different problems. The Puppet Master's threats are nodes in a hidden hierarchy — the party doesn't know which ones matter most. The Coordinator's threats are mutually dependent positions that cannot be addressed individually.

---

### The Warlord

| Element | Puzzle Type | Expression |
|---|---|---|
| Defining Trait | Targeting | The boss commands multiple key targets that each enable a different problem — a support unit that heals, an artillery unit that deals persistent damage, a melee unit that locks down characters. The threats are functionally distinct, and ignoring any one of them has a specific, predictable cost. |
| Strength | Escalation | Every round the party fails to establish kill priority, the field gets worse. Units that survive accumulate advantages — the healer has topped off the boss, the artillery has stacked a debuff, the melee unit has locked down a second character. The window for clean prioritization narrows. |
| Weakness | Division | Once the correct kill order is established and executed, the remaining threats naturally cluster — the boss and whatever support is left — making the final push a concentrated effort rather than a split one. The encounter that demanded careful coordination simplifies into a straightforward fight. |

**Design notes.** The Warlord's Targeting problem must be legible from round one. Each unit the boss commands needs a clearly readable function: players should be able to look at the field at the start of combat and form a hypothesis about kill order, even if that hypothesis turns out to be wrong. The puzzle is not discovering that priorities exist — it is correctly ranking them under pressure.

The Escalation Strength is what makes the Targeting meaningful. Without it, the party can simply experiment: kill one thing, see what happens, kill another. With it, every round of indecision has a compounding cost. The field should visibly worsen — buffs stacking on the boss, debuffs accumulating on the party, secondary threats becoming primary ones.

The Weakness is the structural reward for solving the puzzle. A party that correctly identifies and executes kill order should find that the back half of the encounter feels earned — the chaos has been reduced to a manageable fight, and the reduction feels like their decision, not luck.

**The key design risk** is making the kill order too obvious or too opaque. If the healer is the clear first target in every fight, the encounter stops being a Warlord and becomes a straightforward fight with a script. If the priorities are genuinely ambiguous, players may not understand what the puzzle was even after they won. The ideal is a kill order that feels non-obvious in round one and satisfying in retrospect.

**Examples from fiction:**

*Frieza commanding his army (Dragon Ball Z, Akira Toriyama — manga/anime).* Frieza fights personally and with devastating effect, but the real triage problem during the Namek arc is his field: the Ginyu Force locks down the party's strongest members, his elite soldiers pursue the Dragon Balls, and his general-tier lieutenants pick off anyone who splits from the group. Each unit enables a different problem, and Frieza himself grows more dangerous the longer his support operates freely. The kill order — Ginyu Force first, then Frieza's direct subordinates, then Frieza — is the Warlord's puzzle worked correctly. Frieza isolated, without his army to buy him time and resources, is still powerful but finite.

*Doctor Doom commanding the Latverian army (Marvel Comics).* Doom fights directly and at the front — he is not a distant strategist but a combatant who happens to also command. His forces constitute the real Targeting problem: his robots absorb damage and relay targeting data, his sorcerers suppress magic use, his armored troops anchor defensive positions. The party that focuses on Doom while the field operates freely will find the field progressively easier to command. The party that sequences through the field first will find Doom, when finally isolated, facing them without his infrastructure and on far worse terms than he would have chosen.

*The Night King commanding the Army of the Dead (Game of Thrones — television).* The Night King rides a dragon into battle and fights at the front of his forces — he is not directing from safety but leading the advance personally. The triage problem is his field: the White Walkers each animate separate wight formations, and the wights are the immediate threat to everything the party is trying to protect. Kill order matters here in a way that is structurally enforced: the wights cannot be permanently destroyed while their White Walker remains standing, and the Night King cannot be reached while the wights are everywhere. Once the correct sequence is found and executed, the Weakness is total — his death ends the encounter instantly.

---

### The Puppet Master

| Element | Puzzle Type | Expression |
|---|---|---|
| Defining Trait | Targeting | The boss controls multiple threats, but the hierarchy between them is not immediately visible. Some targets appear important and are not; some appear incidental and are critical. The party must determine which targets actually matter — which ones feed the boss's power, protect it, or escalate the situation — while every target is fighting back. |
| Strength | Division | While the party is sorting the hierarchy, the threats demand presence across the battlefield. The boss's agents are not clustered — they are spread, positioned to force the party to split attention spatially while also solving the targeting puzzle cognitively. Splitting the party to cover the field means splitting the resources available to solve the hierarchy problem. |
| Weakness | Escalation | Once the true hierarchy is understood and the key nodes are eliminated, the boss's ability to escalate collapses. The remaining threats, no longer fed or coordinated, become predictable and static. The escalation engine was always downstream of the hierarchy; destroying the hierarchy dismantles it entirely. |

**Design notes.** The Puppet Master's Targeting problem is epistemic, not tactical. The Warlord's priorities are legible from round one — the puzzle is ranking them correctly. The Puppet Master's priorities are *obscured* — some targets are decoys, some are sleeper threats, and the relationships between them are not obvious until the party has gathered information by engaging the field.

This means the encounter needs a discovery mechanic. Players need a way to learn the hierarchy through play: a minion that visibly panics when a specific other minion is threatened, a buff on the boss that drops when a particular node is destroyed, an action the boss takes to protect one target above all others. The puzzle is not guessable from a distance — it is readable through engagement.

The Division Strength creates the pressure that makes discovery costly. The party cannot simply stand back and observe — the field is hurting them while they think. But splitting up to cover the field means splitting the cognitive bandwidth available to map the hierarchy. The party must balance gathering information against absorbing damage against maintaining enough concentration to act on what they learn.

The Weakness is the payoff for correct deduction. Once the key nodes fall, the boss is not just weakened — its toolkit for making things worse is gone. The escalation that felt inevitable reveals itself as entirely dependent on infrastructure the party has just destroyed.

**The key design risk** is the hierarchy being unreadable — players guessing rather than deducing, or discovering the solution by accident and not understanding what they did. Every node's role in the hierarchy should have at least one tell: a behavior, a reaction from the boss, a pattern in how the field responds when that node is threatened.

**Examples from fiction:**

*Madara Uchiha commanding the reanimated Kage (Naruto, Masashi Kishimoto — manga/anime).* Madara fights at full combat capacity — he is one of the most dangerous individual combatants in the series — while simultaneously commanding a field of reanimated shinobi whose threat hierarchy is non-obvious. The party's instinct is to engage the most visually threatening targets, but the structural anchor of Madara's power in several encounters is not his direct combat ability but the specific assets sustaining his offensive continuity. Identifying which nodes are critical — which reanimated combatants are enabling Madara's most dangerous capabilities versus which are decoys or secondary threats — is the Puppet Master's puzzle. The Division Strength is explicit: his forces are never clustered, always demanding presence across multiple fronts simultaneously.

*Thanos commanding the Black Order (Avengers: Infinity War, 2018 — film).* Thanos fights personally and at the front — his individual combat power is the terminal threat — but the Black Order each enable a different component of his operation across separate fronts. Ebony Maw suppresses the party's mystic assets, Proxima Midnight and Corvus Glaive pressure the physical defenders, Cull Obsidian anchors the melee front. The hierarchy among them is not obvious: addressing the most immediately dangerous Black Order member does not necessarily dismantle the node that is most critical to Thanos's overall offensive continuity. The Division Strength is structural — the fronts are geographically separated, demanding presence across locations — and the Escalation Weakness triggers when the key nodes fall: Thanos without his Order is a more finite, isolated problem than Thanos supported by them.

*Alduin commanding the dragons (The Elder Scrolls V: Skyrim, Bethesda — games).* Alduin fights directly and at the front — his combat power is genuine and his presence in any encounter is the terminal threat — but his field is a distributed network of resurrected dragons whose individual functions are not equally important. Some dragons are simply attacking; others are actively resurrecting additional dragons from burial mounds, feeding the escalation loop that makes the overall threat unmanageable. The hierarchy is non-obvious: the most visually dangerous dragon in any given encounter is not necessarily the one enabling Alduin's broader operation. Identifying which dragons are load-bearing nodes in the resurrection network — and prioritizing them over the more immediate combat threats — is the Puppet Master's puzzle. Once those nodes are dismantled and Alduin is stripped of his ability to replenish his field, his individual combat power, though formidable, becomes finite and addressable.

---

### The Coordinator

| Element | Puzzle Type | Expression |
|---|---|---|
| Defining Trait | Division | The boss's forces hold multiple positions that each require active attention — not because any single position is overwhelming, but because the positions support each other. Abandoning any one front allows that front to reinforce the others. The party cannot concentrate because concentration on one point leaves the others free to converge. |
| Strength | Targeting | While managing the spatial demand, the party also faces genuine ambiguity about which position to prioritize. Each front presents a credible threat, and the mutual support structure means that the "correct" position to strike is not the one that looks most dangerous — it is the one that, when removed, causes the others to collapse. |
| Weakness | Crisis | Once the mutual support structure is broken — once one position falls and the others lose their reinforcement — the remaining threats develop in a predictable, readable pattern. The crisis that each remaining front poses is no longer hidden or ambiguous; it unfolds on a visible clock that the party can manage. |

**Design notes.** The Coordinator's Division problem is structural, not numerical. It is not that the party is outnumbered — it is that the positions are load-bearing. Each front is keeping the others viable. A party that ignores one front to concentrate on another will find that front reinforcing the boss, buffing another unit, or opening a new threat axis. The positions must demonstrably interact, or the encounter collapses into a straightforward multi-target fight.

The Targeting Strength is what makes Division dangerous rather than merely inconvenient. The party needs to split up, but they also need to figure out which split point matters most — which position, if taken, collapses the network rather than simply removes one node. This requires spatial and tactical reasoning simultaneously, which is where the cognitive demand peaks.

The Weakness is the structural payoff. A Coordinator whose mutual support network is intact feels overwhelming. A Coordinator with one position eliminated feels suddenly readable — the remaining fronts are now isolated threats with visible timelines rather than a self-reinforcing system. The encounter should feel dramatically different on either side of that threshold.

**The key design risk** is the mutual support structure being invisible at the table — players do not realize the positions are connected until they have already paid the cost of ignoring one. The connections must be legible from round one: a front that visibly heals another unit, a position that grants cover to the boss, an angle that enables a flanking attack the party cannot otherwise avoid.

**Examples from fiction:**

*Voldemort at the Battle of Hogwarts (Harry Potter, J.K. Rowling — literature).* Voldemort fights directly and commands simultaneously — he is present in the battle, personally dueling, while his Death Eaters hold multiple positions throughout the castle that demonstrably support each other. The castle's defensive fronts are not independent: Death Eaters holding the lower corridors prevent escape routes, those holding the upper towers provide overlapping fire, those pursuing specific targets draw the defenders' attention away from the main push. The party cannot concentrate on Voldemort while the positions are active, and they cannot address all the positions while Voldemort is acting. The Targeting puzzle is identifying which Death Eater position, when collapsed, causes the others to lose their coordination — the structural anchor hidden among individually credible threats.

*Sauron at the Black Gate (The Lord of the Rings, Peter Jackson — film).* In the Second Age prologue, Sauron fights personally and at devastating scale — he is the most dangerous combatant on the field — while his forces hold multiple interlocking positions across the battlefield that demonstrably support each other. The flanking columns protect the center advance, the center advance pins the Alliance forces, and Sauron himself operates from within a formation that his positions are actively keeping intact. The party cannot concentrate on Sauron while those positions are feeding his freedom of movement, and they cannot address all the positions while Sauron is acting. The Targeting puzzle is identifying which position, when collapsed, causes the others to lose their mutual reinforcement — the structural anchor that is less visible than the most immediately threatening front.

*Apocalypse commanding the Four Horsemen (X-Men — comics).* Apocalypse fights directly and at the front — his individual combat power is genuine and extreme — while his Four Horsemen each hold a distinct front that supports the others. War anchors the melee engagement and prevents concentration, Famine degrades the party's resources over time, Pestilence suppresses specific capabilities, and Death applies terminal pressure. These fronts interact: the Horsemen's sustained pressure makes it impossible to disengage and address Apocalypse directly, while Apocalypse's presence prevents the party from safely concentrating on any single Horseman. The Targeting puzzle is identifying which Horseman, when removed, collapses the load-bearing element of the formation — not the most immediately dangerous one, but the one whose absence causes the others to lose their coordination.

---

## Siege Commanders

Siege Commanders generate triage pressure through a process or system they are sustaining, accelerating, or protecting. The encounter is not simply a fight — it is a race against something the boss has set in motion. The boss may not be the most dangerous thing in the room; it is the reason the most dangerous thing in the room is still running.

**What distinguishes Siege Commanders from each other** is the nature of the process and how it creates competing demands. The Ritualist runs multiple independent processes simultaneously, each developing into a different problem. The Swarm Lord runs a single process that compounds — one thing getting worse at an accelerating rate. The Saboteur attacks multiple locations at once, creating a spatial crisis that the party cannot fully cover.

---

### The Ritualist

| Element | Puzzle Type | Expression |
|---|---|---|
| Defining Trait | Crisis | The boss sustains multiple independent processes simultaneously — rituals, summoning sequences, environmental corruptions, cascading magical effects. Each develops at its own rate and produces a different problem when it completes. The party cannot address all of them. |
| Strength | Sacrifice | While managing the crises, the party faces compounding resource costs. Stopping one process requires committing resources that cannot be applied to the others. Every intervention is a sacrifice — and the wrong sacrifice leaves a worse problem running. |
| Weakness | Targeting | Once the processes are dismantled or reduced to a manageable number, the encounter simplifies into a direct confrontation with the boss. The complexity that made targeting feel impossible resolves into clarity: one enemy, one threat, no competing demands on attention. |

**Design notes.** The Ritualist's Crisis problem requires that each process be genuinely distinct — not three versions of the same threat, but three threats that demand different responses. If all the processes do the same thing, the party simply addresses them in order without a real triage decision. The puzzle is that stopping the fast-moving process might be less valuable than stopping the more dangerous one that is nearly complete.

The Sacrifice Strength is what gives the Crisis genuine weight. Resources spent stopping one process are resources not spent on another — and not spent on the boss, who is still fighting. The party must commit to a triage order and accept the cost of the processes they let run. Healing resources, spell slots, action economy: all of these are the currency of the Sacrifice.

The Weakness is the structural reward for solving the puzzle. A Ritualist with all its processes running feels chaotic and overwhelming. A Ritualist with its processes dismantled is simply a boss fight — and the party that reaches that point should feel the chaos resolve into a clean, manageable confrontation.

**The key design risk** is making the processes too symmetrical or too opaque. If all processes complete at the same time, there is no triage — just a simultaneous crisis. If the processes are unreadable, the party cannot form a strategy and the encounter becomes a matter of luck. Each process needs a visible timer, a readable consequence, and enough asymmetry that the choice of which to address first is genuinely meaningful.

**Examples from fiction:**

*The Lernaean Hydra (Greek mythology — myth).* The Hydra is a Ritualist encounter made literal: each head is an independent process that, when addressed incorrectly, generates two new problems. Heracles cannot simply fight the Hydra — he must manage the regrowth mechanic while fighting, which means committing resources (fire, Iolaus's assistance) to stopping the process rather than dealing damage. The Sacrifice is explicit: burning the stumps costs time and resources that cannot be applied to the heads still active. The Weakness triggers when the immortal head is finally isolated — the complexity resolves into a single, addressable threat.

*Ego the Living Planet (Guardians of the Galaxy Vol. 2, 2017 — film).* Ego fights personally and at enormous scale while his Expansion tendrils spread simultaneously across dozens of planets, each operating as an independent process developing toward the same catastrophic completion. The party cannot address all the tendrils — they must triage, choosing which planets to protect and which to abandon while also fighting Ego directly. The Sacrifice is the planets they cannot reach in time. The Weakness is Ego's brain — once the singular node sustaining all the processes is destroyed, every tendril collapses simultaneously. The complexity was always downstream of one target.

*Yhwach distributing the Schrift (Bleach, Tite Kubo — manga/anime).* Yhwach fights personally and at the apex of combat power while his distribution of abilities to the Sternritter creates multiple independent crisis vectors — each Sternritter's Schrift develops into a different catastrophic problem on its own timeline, with its own consequences. The party cannot address all of them without splitting resources that are already stretched against Yhwach's direct pressure. The Sacrifice is deciding which Sternritter crises to allow to complete. The Weakness is Yhwach himself: once isolated and stripped of his distributed network, the crises that were feeding off his power collapse or become individually manageable.

---

### The Swarm Lord

| Element | Puzzle Type | Expression |
|---|---|---|
| Defining Trait | Escalation | The boss commands a force that grows. Units multiply, reinforce, or evolve over time — and the rate of growth accelerates as the encounter progresses. The party is not fighting a fixed field; they are fighting a field that is becoming harder to fight with every round they fail to control it. |
| Strength | Crisis | As the swarm escalates, it generates secondary crises — new threats appearing in new locations, overwhelmed positions that demand immediate attention, cascading problems that branch from the core escalation. The party cannot focus on stopping the growth because the growth keeps producing emergencies. |
| Weakness | Sacrifice | Once the escalation is controlled — the source of growth identified and dismantled — the remaining swarm becomes a fixed, finite threat. The party can now make deliberate choices about which elements to address and which to temporarily abandon. The encounter that felt out of control resolves into a manageable resource problem. |

**Design notes.** The Swarm Lord's Escalation problem must be visibly compounding, not just incrementally worsening. The party needs to feel the curve — round one is manageable, round two is harder, round three is noticeably worse — so that the urgency of finding the escalation source is self-evident from the encounter's behavior. If the swarm simply adds one unit per round, the encounter is a Warlord with extra steps. The Swarm Lord's growth should feel multiplicative.

The Crisis Strength is what prevents the party from simply ignoring the swarm and attacking the boss. The escalation produces genuine emergencies — a healer surrounded, a flank overrun, a secondary objective being destroyed — that pull attention away from the source. The party must constantly react to the swarm's output while also trying to address the cause.

The Weakness is the payoff for finding and eliminating the source. A Swarm Lord with its escalation engine intact is a pressure machine. A Swarm Lord with its engine destroyed is simply a boss with minions — a finite, stable problem that the party can now approach deliberately.

**The key design risk** is the escalation feeling unfair rather than urgent. If the swarm grows faster than any party action can address, the encounter stops being a puzzle and becomes an attrition race the party cannot win. The escalation source — the node, the ability, the mechanic that drives growth — must be reachable and destroyable within the encounter's natural pacing.

**Examples from fiction:**

*The Horned King commanding the Cauldron-Born (The Black Cauldron, Lloyd Alexander — literature).* The Horned King fights personally while the Black Cauldron raises an ever-expanding army of undead warriors that cannot be permanently destroyed by conventional means. The escalation is compounding: each fallen warrior feeds the Cauldron's output, and the Cauldron's output makes the field progressively more unmanageable. The Crisis Strength is explicit — the Cauldron-Born spreading to new positions, cutting off escape routes, surrounding isolated party members — forcing constant reactive decisions while the core escalation continues. The Weakness is the Cauldron itself: once destroyed, every Cauldron-Born falls simultaneously, and the encounter resolves into a direct confrontation with the Horned King stripped of his engine.

*Annihilus commanding the Annihilation Wave (Annihilation — comics).* Annihilus fights directly and at the front — his personal combat power is extreme — while the Annihilation Wave expands across the galaxy at an accelerating rate, each new sector consumed feeding the next wave's momentum. The Crisis Strength is the simultaneous emergencies the Wave produces: inhabited systems falling, defensive lines collapsing, allies being cut off. The party cannot simply fight Annihilus while the Wave operates freely, because the Wave keeps generating crises that demand immediate attention. The Weakness is Annihilus himself as the singular source: once he is destroyed, the Wave loses its central direction and becomes a finite if massive threat rather than an accelerating one.

*The Zerg Swarm commanded by the Overmind (StarCraft, Blizzard — games).* The Overmind directs the Swarm from a position of active command while the Zerg expand across multiple planets simultaneously, each infestation feeding the next wave's scale. The escalation is multiplicative — infested terrans generate more zerglings, creep spread enables faster movement and reinforcement, each lost position makes the next one harder to hold. The Crisis Strength is the emergencies the spread produces: bases under assault, evacuation corridors being cut off, key installations moments from being overrun. The Weakness is the Overmind's cerebrates — destroy the command nodes, and the Swarm's coordination collapses from a directed escalation into a chaotic but manageable mob.

---

### The Saboteur

| Element | Puzzle Type | Expression |
|---|---|---|
| Defining Trait | Division | The boss strikes multiple locations or assets simultaneously, demanding party presence across positions that cannot all be covered. The threats are not clustered — they are distributed by design, positioned to force the party to split in ways that leave every position undermanned. |
| Strength | Sacrifice | While the party is divided across positions, each position represents something that can be permanently lost — an NPC, an objective, a resource, an escape route. The division problem compounds because the cost of each position that goes undefended is not just tactical but consequential: something is destroyed, captured, or corrupted that cannot be recovered. |
| Weakness | Targeting | Once the Saboteur's distributed operation is contained — enough positions addressed that the remaining threats are manageable — the encounter simplifies into a direct confrontation. The boss that seemed to be everywhere resolves into a single, locatable target, and the complexity of the encounter collapses into a straightforward fight. |

**Design notes.** The Saboteur's Division problem is deliberately manufactured. Unlike the Coordinator, whose positions support each other through mutual reinforcement, the Saboteur's positions are independent — each is a separate operation, attacking a separate target, imposing a separate cost. The party cannot address one position and watch the others weaken; they must physically cover the field or accept that uncovered positions will be lost.

The Sacrifice Strength is what gives the Division genuine stakes. If the positions the Saboteur threatens are interchangeable or replaceable, the party has no real triage decision — they simply cover what they can and accept the losses. The Sacrifice means each uncovered position has a distinct, permanent cost: the wrong choice cannot be undone. This is what separates the Saboteur from a simple multi-target encounter.

The Weakness is the structural payoff for containment. A Saboteur with all its operations running is a chaos machine. Once enough operations are contained that the party can concentrate, the boss loses the distributed pressure that was making it dangerous — and the party can bring full resources to bear on what remains.

**The key design risk** is making the distributed operations feel arbitrary rather than purposeful. Each position the Saboteur threatens should have a clear, distinct cost that the party can read and weigh before committing to defend or sacrifice it. If all positions feel equally important, there is no triage — just paralysis. If all positions feel equally disposable, the Sacrifice Strength has no teeth.

**Examples from fiction:**

*Loki at Ragnarök (Norse mythology — myth).* Loki fights personally at Ragnarök while simultaneously enabling catastrophic operations across multiple fronts — his children Fenrir, Jörmungandr, and Hel each strike a different location with a different consequence. The division is spatial and irreversible: the Norse gods cannot be everywhere at once, and each position that goes uncovered falls permanently. The Sacrifice is explicit in the mythology — which gods die where is a function of which fronts they chose to defend and which they could not reach. The Targeting Weakness is Loki himself: once the distributed chaos is contained enough to locate and engage him directly, the encounter resolves.

*Silva (Skyfall, 2012 — film).* Silva fights directly — he is a genuine close-quarters combatant, not a remote operator — while his network simultaneously strikes multiple critical targets across London. The party must split to cover the targets while also engaging Silva personally, and each target that goes uncovered is permanently lost: people die, assets are destroyed, positions are compromised. The Sacrifice is which targets to defend and which to abandon, knowing the abandoned ones will not be recoverable. Once Silva's operations are contained enough to concentrate, the Targeting Weakness emerges: he is a single, locatable individual, and the complexity of the encounter collapses into a direct confrontation.

*Handsome Jack commanding Hyperion forces (Borderlands 2, Gearbox — games).* Handsome Jack fights personally in the final encounter while simultaneously directing Hyperion forces against multiple critical positions across Pandora. The party cannot simply fight Jack while his forces operate freely — each uncovered position represents a permanent loss: an evacuation point destroyed, a resistance cell wiped out, a resource that cannot be replaced. The Division is enforced by geography and by Jack's deliberate sequencing of attacks designed to keep the party reactive. The Sacrifice is which losses to accept in order to maintain enough concentration to eventually address Jack directly — at which point, with his field operations dismantled or accepted as losses, the Targeting Weakness makes the encounter resolvable.

---

## Leverage Commanders

Leverage Commanders generate triage pressure through objectives, costs, and consequences. The encounter forces the party to decide what they are willing to lose — not just what to fight first. These archetypes require emotional and strategic stakes alongside mechanical ones: the boss must be threatening things the party cares about, not just assets that happen to be on the map.

**What distinguishes Leverage Commanders from each other** is the nature of the cost being imposed. The Field Marshal forces a conscious, deliberate abandonment — the party must choose what to sacrifice to win. The Spymaster buries the costs in ambiguity — the party cannot tell which crisis is the real threat and which is misdirection until they have committed resources. The Taskmaster converts delay into compounding cost — the longer the party takes to make a decision, the less any option is worth.

---

### The Field Marshal

| Element | Puzzle Type | Expression |
|---|---|---|
| Defining Trait | Sacrifice | The encounter presents more objectives than the party can protect — NPCs, assets, positions, or outcomes that each have genuine value. The party must consciously choose which objectives to abandon, knowing those choices are permanent. The boss is not simply creating threats; it is forcing deliberate losses. |
| Strength | Division | The objectives that must be abandoned are distributed across positions that each require active presence. The party cannot simply decide to sacrifice one objective remotely — they must physically not be somewhere, which means splitting to attempt coverage while knowing full coverage is impossible. |
| Weakness | Crisis | Once the sacrifices are made and the party has committed to a set of objectives they will defend, the remaining threats develop on a predictable, visible timeline. The crisis that felt overwhelming while every objective was in play becomes manageable once the party has accepted what they are not protecting. |

**Design notes.** The Field Marshal's Sacrifice problem is the most demanding in the Commander category to design correctly, because it requires the party to genuinely care about the objectives being threatened. An NPC the party met ten minutes ago is not a Sacrifice; an NPC who has been part of the campaign is. A generic resource cache is not a Sacrifice; the archive containing the only copy of the information they need is. The Field Marshal only works if the threatened objectives have weight before the encounter begins.

The Division Strength is what prevents the Sacrifice from being resolved through pure calculation. If the party could address all the objectives sequentially, they would — the Sacrifice would be theoretical rather than real. The Division forces the choice to be spatial and physical: they are making a commitment by where they stand, not just by what they plan.

The Weakness is the emotional and tactical release that follows commitment. A party that has accepted its sacrifices and committed to its objectives fights the back half of the encounter with clarity. The crisis that each remaining threat represents unfolds predictably — and predictability, after the chaos of the Sacrifice decision, feels like relief.

**The key design risk** is the Sacrifice feeling punishing rather than meaningful. If the party loses something they care about and the encounter rewards them inadequately, the Sacrifice feels like failure with extra steps. The payoff for making hard choices must be commensurate with the cost of making them — the party should feel that their decision, not luck or optimization, determined the outcome.

**Examples from fiction:**

*Saruman commanding the siege of Helm's Deep (The Lord of the Rings, J.R.R. Tolkien — literature).* Saruman fights through proxy — his Uruk-hai assault force — but the encounter he designs is a pure Field Marshal: the defenders must choose which sections of the wall to abandon as the assault concentrates pressure faster than the available forces can cover. Each sacrifice is permanent and spatial. Abandoning the culvert saves the wall but loses the drainage; holding the gate means thinning the battlements. Théoden's decisions about where to commit his forces are Sacrifice decisions under Division pressure, and the Crisis Weakness emerges once the decision is made: the remaining threats unfold on a readable timeline that the defenders can finally manage.

*Ares commanding the Trojans (The Iliad, Homer — myth).* Ares fights personally and at the front, directing the Trojan offensive while simultaneously pressuring multiple Greek positions — the ships, the defensive wall, the line of heroes. The Greeks cannot protect everything: the ships and the wall cannot both be fully manned, and the heroes cannot be everywhere at once. The Sacrifice decisions the Greek commanders face are irreversible — positions abandoned to the Trojans are not easily reclaimed. Ares's presence on the field is the Division Strength made explicit: his personal combat pressure prevents concentration while the positions bleed. The Crisis Weakness emerges when he is wounded and withdraws — suddenly the Greek losses are visible, fixed, and the remaining threat is readable.

*Red Skull commanding HYDRA's final operation (Captain America: The First Avenger — comics).* Red Skull fights directly and personally while HYDRA's simultaneous strikes against multiple Allied cities force a choice that cannot be reversed: which cities to protect, which to abandon, which assets to commit and which to sacrifice. The party's resources are finite, the strikes are simultaneous, and every uncovered city is permanently lost. The Sacrifice is the deliberate, conscious decision about which populations and objectives to defend — not a tactical choice about kill order, but a moral and strategic commitment to what is worth saving. The Crisis Weakness triggers once the sacrifice decisions are made: HYDRA's remaining operation, stripped of the complexity of simultaneous strikes, resolves into a direct confrontation with Red Skull.

---

### The Spymaster

| Element | Puzzle Type | Expression |
|---|---|---|
| Defining Trait | Crisis | The boss generates multiple simultaneous crises, but their relative severity is deliberately obscured. Some crises are genuine emergencies; others are misdirection designed to draw resources away from the real threat. The party cannot tell which crises are the actual priorities without committing resources to investigate — and investigation has a cost. |
| Strength | Targeting | While the party is sorting real crises from misdirection, the boss and its key assets remain difficult to locate or prioritize. The ambiguity of the crisis field bleeds into ambiguity about the boss itself — which asset is the real threat, which is the decoy, where the boss actually is within its own operation. |
| Weakness | Escalation | Once the real crises are identified and the misdirection is dismantled, the boss's capacity to sustain pressure collapses quickly. The escalation that felt inevitable was entirely dependent on the party not knowing where to look — once they know, the Spymaster's toolkit depletes faster than it can be replenished. |

**Design notes.** The Spymaster's Crisis problem is epistemic before it is tactical. The Ritualist's crises are all real — the puzzle is which to address first. The Spymaster's crises are mixed — some real, some false — and the puzzle is distinguishing between them under time pressure. The party must gather information while also managing the genuine crises that are running, which means spending resources on investigation rather than intervention.

The Targeting Strength creates urgency. The party cannot simply pause and analyze — the real crises are developing, and the boss is using the ambiguity to protect itself and its key assets from concentrated attention. The misdirection is not just wasting the party's resources; it is actively creating cover for the Spymaster's actual operation.

The Weakness is the Spymaster's structural fragility once exposed. The misdirection network is expensive to maintain — it requires assets, attention, and coordination. Once the party decodes the real priorities and commits to them, the Spymaster's resources deplete rapidly, because everything that was sustaining the misdirection is now useless.

**The key design risk** is the misdirection being unresolvable — crises that look identical from the outside, with no tells that allow the party to distinguish real from false. The Spymaster's puzzle must be solvable through play: each false crisis should have at least one observable tell, and the real crises should have consequences that are distinguishable from the misdirection's consequences in retrospect.

**Examples from fiction:**

*Aizen commanding the Espada (Bleach, Tite Kubo — manga/anime).* Aizen fights personally and at a level that makes direct engagement nearly impossible, while his Espada generate simultaneous crisis vectors whose relative severity is deliberately unclear. Some Espada fronts are genuine emergencies; others are pressure designed to draw the party's strongest assets away from the real threat. The Targeting Strength is explicit — Aizen's own position and intentions remain ambiguous until he chooses to reveal them, and the ambiguity of the crisis field is what maintains that concealment. The Weakness triggers when his Kyōka Suigetsu is decoded: once the party understands which crises are real and which are illusions, his toolkit collapses faster than he can sustain it.

*The Operative conducting simultaneous operations (Serenity, 2005 — film).* The Operative fights directly — he is a genuine close-quarters combatant and highly dangerous in personal confrontation — while simultaneously running multiple crisis operations across locations that the party cannot all address. Some operations are genuine threats to the party's objectives; others are misdirection designed to keep the party reactive and prevent them from identifying his actual priority. The Targeting Strength is the Operative himself: his true position and primary objective are obscured by the simultaneous operations he is running, making it difficult to locate and engage him without first sorting real from false. The Weakness is his singular focus — once his real objective is identified, everything else he is doing is revealed as misdirection, and his escalation capacity collapses.

*Senator Armstrong's network (Metal Gear Rising: Revengeance, Platinum Games — games).* Armstrong fights directly and at devastating personal scale while his political and military network runs multiple crisis operations simultaneously — some genuine, some designed to misdirect the party's attention from his actual plan. The Crisis problem is that the party cannot tell which of his operations are the real threat and which are cover. The Targeting Strength is Armstrong himself: his true position within his own network is obscured by the crisis field he is generating, and engaging him directly without first identifying his real operation leaves the party fighting without understanding what they are actually trying to stop. The Weakness is the clarity that follows decoding: once his actual plan is understood, his escalation capacity — entirely dependent on misdirection — collapses, and the encounter resolves into a direct confrontation on known terms.

---

### The Taskmaster

| Element | Puzzle Type | Expression |
|---|---|---|
| Defining Trait | Escalation | The boss's operation becomes more efficient over time. Its forces coordinate better, its attacks become more precise, its defenses adapt. The party is not fighting a fixed threat — they are fighting a threat that is actively learning and improving, and every round of delay makes the eventual confrontation more costly. |
| Strength | Division | As the operation escalates in efficiency, it demands presence across an increasing number of positions. More fronts become active, more locations require attention, more assets come under threat. The Division pressure grows as a function of the Escalation — the more efficient the boss becomes, the more it can sustain simultaneously. |
| Weakness | Sacrifice | Once the escalation is interrupted — the efficiency engine disrupted, the coordination broken — the remaining operation becomes a fixed set of problems that the party can now address through deliberate sacrifice. They can choose which positions to abandon, which assets to lose, and commit fully to the ones they intend to hold. |

**Design notes.** The Taskmaster's Escalation problem is qualitative, not just quantitative. The Swarm Lord's field gets bigger; the Taskmaster's field gets smarter. The distinction matters for design: a Taskmaster's escalation should manifest as behavioral changes, not numerical accumulation. Minions that start uncoordinated begin flanking. Attacks that start predictable become adaptive. Defenses that start porous begin closing. The party should feel the field learning, not just growing.

The Division Strength is the output of that efficiency. A Taskmaster in round one holds two positions. A Taskmaster in round four holds five, because it has optimized its forces to cover more ground with the same assets. The Division pressure is not the encounter's starting condition — it is what the Escalation builds toward. This makes the early rounds feel manageable in a way that is deliberately misleading.

The Weakness is the reset that follows disrupting the efficiency engine. A Taskmaster that has been interrupted loses its accumulated coordination — and the party faces its original, less efficient form. The Sacrifice decisions that were impossible while the Escalation was running become straightforward once the field is static.

**The key design risk** is the Escalation feeling unfair rather than urgent — the party losing not because they made wrong choices but because the encounter outpaced any possible response. The Taskmaster's efficiency engine must be interruptible from round one: the party should be able to see the mechanism, understand that disrupting it is an option, and choose when to commit to that approach versus addressing other pressing needs.

**Examples from fiction:**

*Morgoth commanding the War of Wrath (The Silmarillion, J.R.R. Tolkien — literature).* Morgoth fights personally — his individual power is the apex of the encounter — while his war machine escalates across multiple fronts with increasing efficiency. His forces do not simply accumulate; they adapt, coordinate, and optimize their pressure across the fronts they hold. The Division Strength is the output of that optimization: more fronts under pressure, more positions requiring simultaneous defense, as Morgoth's operation reaches peak efficiency. The Sacrifice Weakness is the Valar's strategic acceptance of what must be lost to interrupt the engine — the destruction of Beleriand itself is the ultimate Sacrifice made to break Morgoth's operational capacity and force the encounter into a direct confrontation.

*Ultron commanding his replication network (Age of Ultron — comics).* Ultron fights personally and at a level that makes direct engagement extremely costly, while his replication network escalates across multiple locations simultaneously — each new Ultron body more refined, more efficient, better adapted to counter the party's specific responses. The Division Strength is explicit: as the network grows, more locations require immediate attention, more assets come under threat, and the party's ability to concentrate erodes. The Sacrifice Weakness is the Vision Protocol — a deliberate, irreversible commitment that sacrifices the integrity of the network in order to break its escalation. Once the efficiency engine is disrupted, the remaining Ultron bodies are a finite, addressable threat.

*Kronos commanding the Titans (Greek mythology — myth).* Kronos fights personally and at the apex of divine combat power while his Titan generals escalate pressure across multiple fronts with increasing coordination. The early stages of the Titanomachy are manageable — the Titans hold their positions but do not yet coordinate. As the war progresses, the Titan fronts begin to reinforce each other, adapt to the Olympians' tactics, and press positions that were previously stable. The Division pressure grows as a direct function of the Escalation — more fronts become simultaneously active as the Titans reach operational efficiency. The Sacrifice Weakness is the Olympians' use of the Hecatoncheires and Cyclopes — assets that impose an irreversible cost on the war's conduct in exchange for breaking the Titans' coordination. Once the efficiency engine is disrupted, the Titanomachy resolves into a direct confrontation with Kronos stripped of his operational network.
