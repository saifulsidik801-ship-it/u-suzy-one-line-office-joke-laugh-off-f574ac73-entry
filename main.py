#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to /output/entry.txt.
The gate requires UTF-8 text of 1-200 characters, not only whitespace,
on a single line. The chosen joke is picked from the candidates below
against the judge's criteria, in order: (1) really a one-line office
joke, (2) sharp surprising punchline, (3) clear on one read,
(4) fresh, no office cliches, (5) tight wording, every word earning
its place.
"""

CANDIDATES = [
    # A: printer as coworker -- personification twist, instantly visual.
    "The office printer is the only coworker who can jam, scream, and refuse to work - and still never get fired.",
    # B: performance-review euphemism turned back on management.
    "My review said I 'thrive under pressure' - which is HR for 'we plan to keep crushing you.'",
    # C: mental-health day undercut by the inbox.
    "I asked for a mental health day and my boss said, 'Sure - just answer emails while you recover.'",
    # D: trust falls, literalised by layoffs.
    "Our team-building exercise was trust falls, which is fitting, since the company has been dropping us all year.",
    # E: the job description that describes nothing.
    "HR said my job was 'other duties as assigned,' which is corporate for 'we have no idea what you do either.'",
    # F: the raise that never circles back.
    "I asked for a raise and my manager said he'd 'circle back' - that was three fiscal years ago, and he's still circling.",
]

# Winner: candidate A. It beats the rest on the judge's order:
# 1. unmistakably one line about office life; 2. the punchline
# ("still never get fired") lands a real laugh by flipping the
# usual firing threat onto the machine; 3. clear on one read --
# everyone has fought a printer; 4. fresh -- the printer is a
# prop, never the joke's coworker; 5. tight at 108 characters,
# every word pulling weight. B and C are strong seconds but lean
# on familiar review / mental-health framings; D and F reuse the
# well-worn trust-fall and "circle back" gags.
JOKE = CANDIDATES[0]


def main() -> None:
    text = JOKE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
