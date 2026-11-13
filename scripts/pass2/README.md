# Pass 2 and Sundering tooling

Scripts that built the Deities journal's research inputs. Run them from the repo root with `python3 -I`.
`SCRATCH` is a working directory outside the repo (default `/tmp/waterdeep-scratch`).

| Script | What it does |
|---|---|
| `bundle_deities.py` | Builds one research bundle per power (`5etools.md`, `wiki.txt`, `campaign-hits.txt`, `adventure-hits.txt`) from `sources/5etools/deities.json`, the offline wiki index and the campaign files. Output goes to `$SCRATCH/research/deities`; the committed copy is `sources/research/pass2-bundles/`. Needs the wiki index. |
| `check_quotes.py <notes file>` | Checks that every quoted block in a research notes file appears at its stated file and line in the bundles. |
| `fix_planned.py` | Retargets "(Deities, page planned)" to "(Deities)" on tracked deity pages whose target now exists. Misses names with an apostrophe or a leading "the". |
| `build_subclass_reference.py` | Regenerates `docs/plans/setting-compendium-pass2-subclass-reference.md` from `sources/5etools/class/`. |
| `extract_sundering_sources.py` | Rebuilds the wiki pages and book text in `sources/research/sundering-sources/`. Needs the wiki index. |

## The offline wiki is not committed

The Forgotten Realms Wiki dump is 59 MB compressed (366 MB indexed), too large for the repo. Rebuild it in about two minutes with `scripts/fandom-dump/README.md`. Everything the Pass 2 and Sundering research took from it is already in the committed bundles and sources folders.

## The 5etools data is committed

`sources/5etools/` holds `deities.json`, `books.json`, `class/class-{cleric,paladin,warlock}.json` and `book/book-{scag,frhof}.json`, taken from the `5etools-mirror-3/5etools-src` mirror (`data/`).

The bundles and the Sundering sources sit in `sources/research/`, not under `docs/`, because the GitHub Pages workflow publishes everything under `docs/` and these files hold raw book text.
