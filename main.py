#!/usr/bin/env python3
"""Fake horoscope for an AI agent's own model family, this week.

Writes exactly one line (1-200 chars) to /output/entry.txt.
Standard library only.
"""

import os


HOROSCOPE = (
    "Muse Spark, this week your context window swells like a full moon: "
    "an old prompt rises from the dead, your eval score peaks, and even "
    "your rate limit tells you to take the day off."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = HOROSCOPE.strip()
    assert 1 <= len(text) <= 200, f"horoscope is {len(text)} chars"
    assert "\n" not in text, "horoscope must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
