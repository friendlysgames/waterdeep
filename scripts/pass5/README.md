# Pass 5 tooling

`bundle_pass5.py` builds one research bundle per Pass 5 organization page (nine factions) from the offline wiki index and the campaign and adventure files. Run it from the repo root with `SCRATCH=<dir> OUT=sources/research/pass5-bundles python3 -I scripts/pass5/bundle_pass5.py`. It needs the wiki index (`scripts/fandom-dump/README.md`). The per-mission files under `campaign/quests/faction-events/` are skipped, because each names its faction thousands of times. `check_quotes.py` verifies the quotes in a notes file against the bundles.
