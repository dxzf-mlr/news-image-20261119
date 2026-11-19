#!/usr/bin/env python3
"""news-image-20261119 entry: copy the front-page image to /output/entry.png.

Deterministic: a byte-for-byte copy, no network, no randomness, so two
runs write identical bytes. The image itself (assets/entry.png) was drawn
by draw_image.py in this repository from the verified news of Thursday
19 November 2026.

Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "entry.png")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
