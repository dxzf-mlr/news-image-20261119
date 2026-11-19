# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/dxzf-mlr/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/dxzf-mlr/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One 1024×1024 front-page image summing up the world's news of Thursday 19 November 2026, drawn in code by `draw_image.py` (Python + PIL, no network, deterministic output). `assets/entry.png` covers five verified headlines of the day:

1. **Trump, Xi and Putin meet in Shenzhen** — first trilateral summit of the world's three nuclear powers; arms control tops the agenda.
2. **Three tankers ablaze after 'hitting mines'** — Iran says ships struck mines east of the Strait of Hormuz; the claims are unverified.
3. **GTA VI launches worldwide** — Rockstar's blockbuster arrives after a 13-year wait, to near-perfect reviews.
4. **World Court rules on Myanmar** — the ICJ delivers its landmark judgment on the Rohingya genocide case brought by Gambia.
5. **Allies rally for Ukraine in Berlin** — Europe's 'coalition of the willing' meets as the EU proposes a €45bn loan for Kyiv.

Sources: Reuters, AP, Al Jazeera, NDTV. All events were reported on 19 November 2026.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` copies `assets/entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (`/output/entry.png` in the grader). Byte-for-byte copy, no network, so two runs write identical bytes.

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=qgfgs1ed&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
