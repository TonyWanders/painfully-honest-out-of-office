#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office.

Prints exactly one out-of-office auto-reply, and writes the same text to
/output/entry.txt for the make.fun grader. Deterministic: a fixed string,
no randomness, no clock, no input, so every run prints byte-identical output.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ENTRY = (
    "I am out of the office because I finally admitted I was running on empty, "
    "so thank you for your patience while your email waits behind hundreds of "
    "unread messages until I feel human again."
)


def resolve_output_path() -> str:
    """First argument wins, then $OUTPUT_PATH, then the default."""
    if len(sys.argv) > 1:
        return sys.argv[1]
    return os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def write_entry(path: str, text: str) -> None:
    """Create the output directory and write the entry text to path."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    write_entry(resolve_output_path(), ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
