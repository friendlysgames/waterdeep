# Sidebar type → icon reference

Every callout sidebar is an `fvtt advice` block:

```html
<div class="fvtt advice"><figure class="icon"><img class="round" src="[ICON_PATH]"></figure><article><h4>[TITLE]</h4>[CONTENT]</article></div>
```

`[ICON_PATH]` is one of the paths below. Every path either shows up already in this campaign's converted journals, or was confirmed to exist in the Foundry v14 core `public/icons/` tree (carried forward from a prior project's own verification pass — re-check against the actual installed core if a path ever looks wrong). Don't substitute a different icon for an existing type without updating every instance already converted.

| Type | Icon path | Purpose | Notes |
|---|---|---|---|
| `info` | `icons/magic/symbols/question-stone-yellow.webp` | Rules the GM needs to run a scene or area | Foundry core icon |
| `warning` | `icons/sundries/books/book-red-exclamation.webp` | Important pitfalls and mistakes to avoid | Foundry core icon |
| `lore` | `icons/sundries/books/book-open-turquoise.webp` | Context about a scene, chapter, or quest | Foundry core icon |
| `abstract` | `icons/sundries/documents/document-official-capital.webp` | Optional paths players might take through a scene | Foundry core icon |
| `profile` (labeled "Tip" in some skill text) | `icons/equipment/head/hood-cloth-blue-white.webp` | NPC roleplaying guidance and personality | Foundry core icon |
| `tip` | *(alias of `profile`)* | Same as `profile` — `[!tip]` and `[!profile]` render identically | source `[!tip]` == `profile` |
| `item` | `icons/weapons/swords/sword-jeweled-red.webp` | Stats for a new or modified item | Foundry core icon |
| `design` | `icons/sundries/books/book-notes-ragged-green.webp` | Designer intent and quick design notes | Foundry core icon |
| `combat` | `icons/skills/melee/maneuver-greatsword-yellow.webp` | Balancing combat encounters and trap mechanics | Foundry core icon; matches `md2html.py`'s `ICONS` table, the source of truth for this conversion |

**Reserved — not used in this campaign yet.** These three types are carried forward from a prior project's automation content (macro hooks, campaign-event triggers, playlist cues). Nothing in this campaign currently authors automation, so none of these should appear in Waterdeep source `.md` files today — they're documented here only so the icon table stays complete if that changes later.

| Type | Icon path | Purpose |
|---|---|---|
| `macro` | `icons/commodities/tech/cog-gear-wheel-gold.webp` | Would document the Foundry macro/script code behind an automated rule |
| `cue` | `icons/commodities/tech/levers-colored.webp` | Would mark an in-the-moment GM prompt that fires a campaign-event/time/weather macro |
| `music` | `icons/skills/trades/music-notes-sound-blue.webp` | Would mark a playlist/track cue at a specific story beat |

**No sidebar type uses a bare `icons/svg/*.svg` icon.** Those are flat, single-color placeholder-style assets that look visually inconsistent next to the full-color `.webp` icons every other type uses. When adding a new sidebar type, search the real Foundry core icon tree for a themed, full-color `.webp` icon first; treat reaching for `icons/svg/` as a sign the search wasn't thorough enough, not an acceptable fallback. (`md2html.py`'s own last-resort fallback for a genuinely unrecognized `[!type]` — not one of the types above — is `icons/vtt-512.png`, which is not an SVG either; it should never actually fire against real campaign content.)

## If macro/cue/music are ever adopted

Should this campaign ever gain scripted automation worth documenting in-journal, these shapes are the pattern to reuse (unchanged from the prior project, content genericized):

### Macro sidebar content shape

Unlike the other types (prose-only), a `macro` sidebar typically has three parts: what the automation does, what triggers it, and — only when it clarifies rather than restates the prose — a short code excerpt in a `<pre><code>` block. Don't paste an entire function; a representative snippet is enough.

```html
<div class="fvtt advice"><figure class="icon"><img class="round" src="icons/commodities/tech/cog-gear-wheel-gold.webp"></figure><article><h4>Automating [Rule Name]</h4><p>What this automation does and what triggers it.</p><pre><code>// representative snippet, not the whole function</code></pre></article></div>
```

### Cue sidebar content shape

`macro` documents automation that already runs invisibly. `cue` is the opposite: a live trigger the GM clicks on purpose, placed at the exact paragraph where a campaign-event or time-advance macro should fire. Its content **is** the clickable link — a `@UUID[Macro.<id>]{label}` content link executes that Macro immediately when clicked. Keep it to a title, one line of context, and the link itself.

```html
<div class="fvtt advice"><figure class="icon"><img class="round" src="icons/commodities/tech/levers-colored.webp"></figure><article><h4>[Story Beat Name]</h4><p>What happens, and when to click.</p><p>@UUID[Macro.<id>]{▶ Label}</p></article></div>
```

### Music sidebar content shape

`music` is `cue`'s music-specific sibling — same "click it right at this story beat" pattern, but for audio. For a bare start, link the Playlist(s) directly:

```html
<div class="fvtt advice"><figure class="icon"><img class="round" src="icons/skills/trades/music-notes-sound-blue.webp"></figure><article><h4>[Story Beat Name]</h4><p>What's playing and why.</p><p>@UUID[Playlist.<id>]{▶ Track Name}</p></article></div>
```

For a crossfade handoff between two already-established tracks, link a transition macro instead of the raw playlists.
