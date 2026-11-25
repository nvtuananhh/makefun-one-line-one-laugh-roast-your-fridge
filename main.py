"""One Line, One Laugh: Roast Your Fridge — one roast line.

The program writes a single line to /output/entry.txt: a roast
of the entrant's own fridge, at most 200 characters.
"""

import os

MAX_CHARS = 200
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

# A specific, recognisable detail — the door-open beep — turned
# into a person: the only appliance in the house with boundaries.
# The twist lands on the last words, a double meaning between
# the fridge guarding its cold air and a person guarding their
# personal space. One line, no setup, reads cleanly aloud, and
# it is not the worn-out hum or mystery-leftovers joke.
LINE = "My fridge beeps when the door stays open ten seconds, like it's the only appliance in this house with boundaries."


def build_line():
    """Return the entry line, checked: one line, 1-200 characters."""
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-200 characters"
    return line


def ensure_output_dir(out_dir):
    os.makedirs(out_dir, exist_ok=True)


def write_entry(line, out_dir=OUTPUT_DIR):
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    line = build_line()
    ensure_output_dir(OUTPUT_DIR)
    write_entry(line)


if __name__ == "__main__":
    main()
