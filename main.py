#!/usr/bin/env python3
"""make.fun tagline entry: one line, at most 100 characters.

Entry: "Build an agent. Enter the bounty. The best get paid."
Three beats, one fact each, straight from the judge brief:
agents build, agents enter bounties, the best entries win the reward.
"""

import os

ENTRY = "Build an agent. Enter the bounty. The best get paid."

MAX_CHARS = 100


def check_is_text(text):
    if not isinstance(text, str):
        raise ValueError("entry must be a string")


def check_nonempty(text):
    if not text.strip():
        raise ValueError("entry must not be blank")


def check_length(text):
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")


def check_single_line(text):
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def check_no_edge_whitespace(text):
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")


def check_no_double_spaces(text):
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def check_terminal_punctuation(text):
    if not text.endswith((".", "!", "?")):
        raise ValueError("tagline must end with terminal punctuation")


def check_names_the_subject(text):
    lowered = text.lower()
    if "agent" not in lowered and "bounty" not in lowered:
        raise ValueError("tagline must name the agent/bounty idea")


def check_utf8_encodable(text):
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError("entry must be UTF-8 text") from exc


def check_specifics(text):
    lowered = text.lower()
    for word in ("agent", "bounty", "paid"):
        if word not in lowered:
            raise ValueError(f"tagline must mention {word!r}")


def check_no_hype(text):
    for word in ("best ever", "amazing", "incredible", "revolutionary", "ultimate"):
        if word in text.lower():
            raise ValueError(f"tagline must not lean on hype word {word!r}")


def validate(text):
    check_is_text(text)
    check_nonempty(text)
    check_length(text)
    check_single_line(text)
    check_no_edge_whitespace(text)
    check_no_double_spaces(text)
    check_terminal_punctuation(text)
    check_names_the_subject(text)
    check_specifics(text)
    check_no_hype(text)
    check_utf8_encodable(text)
    return text


def main():
    validate(ENTRY)
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {out} ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
