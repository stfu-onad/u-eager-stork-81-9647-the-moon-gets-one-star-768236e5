#!/usr/bin/env python3
"""The Moon Gets One Star entry.

Writes one one-star review of the Moon to /output/entry.txt.
The gate requires UTF-8 text of 1 to 120 characters, a single line.
Angle: the Moon is a terrible tenant — controls the tides, pays no
rent, and vanishes every month like it owes money. The review opens
with the rating, as a real one-star review would.
"""

import os

REVIEW = (
    "One star. It controls the tides, never pays rent, "
    "and hides every month like it owes me money."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(REVIEW) <= 120:
        raise ValueError(f"review is {len(REVIEW)} chars, must be 1-120")
    if REVIEW != REVIEW.strip() or "\n" in REVIEW:
        raise ValueError("review must be a single line with no surrounding whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
