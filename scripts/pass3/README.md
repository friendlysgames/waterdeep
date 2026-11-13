# Pass 3 tooling

`bundle_pass3.py` builds one research bundle per Pass 3 page (wards, geography, governance, lore) from Dragon Heist Chapter 9, the offline wiki index and the campaign files. Run it from the repo root with `SCRATCH=<dir> python3 -I scripts/pass3/bundle_pass3.py`; it writes to `$SCRATCH/research/pass3`. The committed copy is `sources/research/pass3-bundles/`. It needs the wiki index (`scripts/fandom-dump/README.md`). `scripts/pass2/check_quotes.py` verifies the quotes in a notes file against the bundles.
