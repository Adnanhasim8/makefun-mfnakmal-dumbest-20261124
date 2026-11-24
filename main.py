#!/usr/bin/env python3
"""Write one line about the dumbest thing my agent did today.

Competition: u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec
Python 3.13 standard library only; no network at run time.
"""

import os

ENTRY = "It auto-saved a blank page over my only copy, then congratulated itself on the clean layout."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate assertions: one line, 1-200 characters, non-empty, not only whitespace.
    assert ENTRY, "entry must be non-empty"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= 200, "entry must be at most 200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
