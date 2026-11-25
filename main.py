#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut.

Writes the GPS's one-line excuse for sending the driver down the wrong road
to /output/entry.txt. The line is the GPS speaking in first person, smug and
defensive, blaming the map, with a specific fresh detail (a tunnel that is
actually a pond) and the payoff in the final words.
"""
import os
import sys

LINE = "The map said the tunnel was open. The tunnel is a pond. I have filed a formal complaint with the pond."

def main():
    # Gate: one line of plain text, 1-200 chars, not only whitespace.
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, f"entry length {len(LINE)} out of range"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} chars to /output/entry.txt")

if __name__ == "__main__":
    sys.exit(main())
