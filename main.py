#!/usr/bin/env python3
"""Cat Reviews Its Human — one-star review entry writer.

Writes a single funny one-star review, written by a house cat about its
human, to /output/entry.txt. Deterministic: every run produces the exact
same bytes. Stdlib only; no network, no secrets, no files outside the repo.
"""

import os
from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200

# The review, built from its three beats so each part reads on its own:
# the rating, the specific complaint, and the sting at the end.
RATING = "One star."
COMPLAINT = (
    "My human stares at a glowing rectangle all day and calls it work,"
)
STING = "yet somehow I am the one accused of sleeping on the job."


def build_entry() -> str:
    """Assemble the entry line from its beats, with single spaces."""
    return " ".join([RATING, COMPLAINT, STING])


def validate_entry(text: str) -> None:
    """Guard the gate: 1-200 chars, one line, non-blank, UTF-8 encodable."""
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    text.encode("utf-8")  # raises if not encodable


def write_entry(path: Path = OUTPUT_PATH) -> str:
    entry = build_entry()
    validate_entry(entry)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(entry + "\n", encoding="utf-8", newline="\n")
    return entry


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
