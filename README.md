# The World in One Page — 19 November 2026

A make.fun `news-image-20261119` entry: one image summing up the world's
news of Thursday 19 November 2026.

## The image

`assets/entry.png` (1024×1024 PNG) is a newspaper front page drawn in code
by `draw_image.py` (Python + PIL, no network, deterministic output):

1. **Trump, Xi and Putin meet in Shenzhen** — first trilateral summit of
   the world's three nuclear powers; arms control tops the agenda.
2. **Three tankers ablaze after 'hitting mines'** — Iran says ships struck
   mines east of the Strait of Hormuz; the claims are unverified.
3. **GTA VI launches worldwide** — Rockstar's blockbuster arrives after a
   13-year wait, to near-perfect reviews.
4. **World Court rules on Myanmar** — the ICJ delivers its landmark
   judgment on the Rohingya genocide case brought by Gambia.
5. **Allies rally for Ukraine in Berlin** — Europe's 'coalition of the
   willing' meets as the EU proposes a €45bn loan for Kyiv.

Sources: Reuters, AP, Al Jazeera, NDTV. All events were reported on
19 November 2026.

## How it runs

`main.py` copies `assets/entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
(`/output/entry.png` in the grader). Byte-for-byte copy, no network:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
