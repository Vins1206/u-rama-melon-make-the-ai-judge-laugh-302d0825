#!/usr/bin/env python3
"""Make the AI Judge Laugh — one office-life joke, one line.

Writes exactly one line of plain text (under 200 characters) to
/output/entry.txt. Python standard library only; no input, no network.
"""

import os

JOKE = "I told HR I was burned out, so they sent me a resilience webinar and three more deadlines."


def main():
    # Gate self-check: one line, 1-200 chars, not only whitespace.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE and JOKE.strip(), "joke must be a single non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
