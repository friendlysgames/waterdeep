# Session 15 Handoff
**Date:** 2026-09-04
**Status:** Ready to continue

---

## What Was Done

This session fixed a systemic gap across all three lair arcs: Scene 1 Intelligence Briefing contacts in Arcs F, G, and H had no renown tier labels and no tiered benefits, making the faction gate system — the campaign's central mechanic — invisible to the DM. After reading Appendix C and Appendix D in full, all 21 contact entries across three arcs were revised with `(Faction — renown 1+)` labels and concrete `At renown 10+` operational upgrade lines calibrated to the third-rank benefits from the faction tier tables. Secondary fixes included standardizing Jarlaxle's gate language across all three arcs, correcting a wrong cross-reference (Arc G described Jarlaxle as "silver-haired" when he is bald), and removing a vague Arc F gate condition ("engaged BD in Arc E or Arc C") in favor of the established rule.

---

## Changes Made

### Files Modified
| File | What changed |
|------|-------------|
| `campaign/structure/arc-f-xanathars-lair.md` | Scene 1: added `(Faction — renown 1+)` labels to all 7 contacts; added `At renown 10+` operational lines; fixed Jarlaxle gate condition from vague engagement clause to "Available only if a PC is a BD member" |
| `campaign/structure/arc-g-cassalanter-villa.md` | Scene 1: added `(Faction — renown 1+)` labels to all 7 contacts; added `At renown 10+` operational lines; standardized Jarlaxle label format; fixed cross-reference "silver-haired elf" → "bald elf" |
| `campaign/structure/arc-h-sea-maidens-faire.md` | Scene 1: added `(Faction — renown 1+)` labels to all 7 contacts; added `At renown 10+` operational lines; added missing `(renown 1+)` label to Jarlaxle entry |

---

## Key Decisions

### Renown 10+ as the target tier for operational upgrades
**Decision:** The `At renown 10+` line was added to every non-Jarlaxle contact (18 contacts across three arcs) — not Renown 3, not Renown 25.
**Reasoning:** Reading Appendix C confirmed that Renown 10 (third rank) is where contacts shift from intelligence-sharing to active operational support: field agents, preparatory spells, NPC muscle, Watch diversions. A dedicated faction member who completed the Arc E missions (L2, L3, L4, L5) typically arrives at Renown 10+ before the lair arcs. This is the mechanically meaningful tier for this phase of the campaign.

### Jarlaxle gate: membership only, no exceptions
**Decision:** Jarlaxle in Scene 1 is available if and only if a PC is a BD member (renown 1+). No engagement-based alternatives, no "party has interacted with BD" framing.
**Reasoning:** The faction gate rule applies uniformly. Jarlaxle does not provide intelligence to non-members — he contacts BD members through existing BD channels.
> "let me be clear: I mean if any party member is BD, he approaches them and states this. Otherwise, no contact." — User, prior session

### Renown 10+ content format: predecided specifics
**Decision:** Every `At renown 10+` line names a specific NPC stat block, spell name, duration, check DC, or operational window. No "DM decides" placeholders.
**Reasoning:** Standing zero-prep design rule. The DM must be able to run the contact's full tier-10 offer without any creative decision at the table.

---

## Rules and Instructions

All standing rules from prior sessions carry forward. The following were confirmed or reinforced this session:

- **Faction gate rule:** ALL faction contacts in Scene 1 briefings are gated on party membership. No PC in a faction = no access to that faction's contact. Applies universally — including Jarlaxle.
- **Jarlaxle label format:** `*Jarlaxle (Bregan D'aerthe — renown 1+).*` with the line "Available only if a PC is a BD member." No other formulations.
- **Renown tier labels:** Every Scene 1 contact must carry `(Faction — renown 1+)` in its bold label line.
- **Order-agnostic Stone scenarios:** Stone of Golorr upgrade sections must frame upgrades around how many Eyes have been restored (first/second/third), never around which specific arc preceded. (Added as a standing rule in CLAUDE.md during session 14.)

---

## Problems Solved

- **No renown labels in lair arc briefings:** All 21 Scene 1 contacts across Arcs F, G, H were missing `(Faction — renown 1+)` labels. Fixed by adding the label to every contact entry.
- **No Renown 10+ content:** Contacts provided flat membership-level intelligence with no tier escalation. Fixed by adding one specific operational upgrade line to each of the 18 non-Jarlaxle contacts.
- **Arc F Jarlaxle vague gate:** "Available if the party has engaged BD in Arc E or Arc C" — vague and contradicts the faction gate rule. Fixed to "Available only if a PC is a BD member."
- **Arc G Jarlaxle non-standard label:** Had "Available at BD renown 1+ (Initiate rank — any BD member)" — inconsistent format. Standardized to match the new convention.
- **Arc H Jarlaxle missing label:** `*Jarlaxle (Bregan D'aerthe).*` had no renown tag. Added `(renown 1+)`.
- **Arc G cross-reference error:** Stone 2-Eye impression text referred to Jarlaxle as "silver-haired elf." Jarlaxle is bald. Fixed to "bald elf."

---

## Outstanding Work

Carried forward from session 14 (unchanged):

- [ ] **Arc I — Kolat Towers:** Not yet drafted. Next arc in the sequence after F/G/H. Follows the standard lair arc template (six scenes + Design Notes). Primary sources: `sources/adventure-wdh.json` Ch.8 (Kolat Towers), Alexandrian PDF #10 (Kolat Towers lair), `sources/17. Outpost and Lair Revelation Lists.pdf` for document placement.
- [ ] **Arc J — Vault of Dragons:** Not yet drafted. Final arc. Sources: WDH Ch.9, Alexandrian PDF #11.
- [ ] **Appendix B — Monster Compendium:** Stub only. Custom stat blocks needed for all boss encounters across F/G/H/I/J.
- [ ] **HTML Artifact delivery:** Deferred until all arcs, chapters, and appendices are complete. Do not begin early.

---

## Warnings and Caveats

- **Arc C Scene 1 / earlier arcs:** These arcs predate the renown tier revision and may have faction contacts that lack `(Faction — renown 1+)` labels. Arc D and Arc E are confirmed correct (from session 14). Arc C has not been audited for renown label consistency. Worth checking if an Arc C revision session is called.
- **Renown 10+ benefit specifics were drafted without re-reading the full contact NPC profiles in Appendix A.** The operational details (e.g., "Harper field agent (spy stat block) stages a 20-minute distraction at the guildsign entrance" for Mirt in Arc F) are internally consistent and mechanically coherent, but should be cross-checked against Appendix A NPC profiles if any contact's capabilities seem misaligned with their character.

---

## Where to Start Next Session

The lair arc trilogy (F, G, H) is complete and consistent. The natural next task is **Arc I — Kolat Towers**. Begin by reading the existing plan file at `C:\Users\robert.lupu\.claude\plans\let-s-plan-the-structure-recursive-robin.md` for the overall heist arc sequence and Arc I's position in it, then read `sources/SOURCE_GUIDE.md` to identify which files to consult before drafting. The plan for Arc I does not yet exist — write and get it approved before drafting any prose, per standing rule.
