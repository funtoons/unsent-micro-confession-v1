"""Unsent: The Micro-Confession Sprint -- entry generator.

Writes one two-part micro-confession to /output/entry.txt: a To: line
naming who it was meant for, and the unsent message itself, one line,
written exactly as it was typed, with no explanation after it.

Python standard library only. Offline and deterministic: no randomness,
no network, no clock, no environment reads. The entry text is a fixed
original confession written for this competition.
"""

import os

ENTRY = (
    "To: Dad\n"
    "I sold the watch you gave me for graduation to pay rent in March "
    "and I still check the pawn shop window every time I pass it.\n"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    lines = text.split("\n")
    # Gate assertions: total 1-260 characters, exactly two parts.
    assert 1 <= len(text) <= 260, "entry must be 1-260 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert lines[0].startswith("To: "), "first line must be the To: line"
    assert lines[0][4:].strip(), "To: line must name someone"
    message = lines[1]
    assert message, "message line must not be empty"
    assert len(message) <= 200, "message must be at most 200 characters"
    assert len(lines) == 3 and lines[2] == "", "entry must be exactly two lines"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
