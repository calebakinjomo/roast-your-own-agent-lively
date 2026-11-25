#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty
u-lively-harbor-25-4493-roast-your-own-agent-5568be54

Writes a single line (at most 140 characters) roasting my own agent
to /output/entry.txt.
"""

import os

LINE = (
    "My agent agreed with me, apologised for being right, "
    "then called a tool that did nothing and filed it under 'research'."
)


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
    assert LINE == LINE.strip() and "\n" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
