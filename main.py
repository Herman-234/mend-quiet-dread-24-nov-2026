#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry.

Writes one code review comment (<=140 chars, single line) to the
output path: it approves a pull request while carrying quiet
existential dread. Deterministic, no network.
"""

import os
import sys

ENTRY_LINE = (
    "Approved. The tests pass, the code is clean, and someday all of "
    "this will be someone else's problem anyway."
)


def validate(line: str) -> None:
    """Fail loudly if the entry would break the 1-140 char, one-line gate."""
    if not line or not line.strip():
        raise ValueError("entry line is empty")
    if len(line) > 140:
        raise ValueError(f"entry line is {len(line)} chars, over the 140-char limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")


def main() -> int:
    validate(ENTRY_LINE)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_LINE)
    print(f"wrote {len(ENTRY_LINE)} chars to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
