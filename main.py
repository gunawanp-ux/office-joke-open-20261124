"""One-line office joke for make.fun's "Make the AI Judge Laugh: the Office Joke Open".

Construction of the joke in LINE:
- Setup: the reply-all storm, the most specific and universally dreaded
  ritual of office life, pinned down with a concrete headcount (400
  coworkers).
- Misdirection: the speaker joins the storm in the very act of condemning
  it. He is not the victim of the reply-all; he is its newest contributor,
  which sets up the turn.
- Payoff, saved for the last three words: instead of being punished, he is
  promoted "for demonstrating leadership." The laugh is the flash of
  recognition that in office life, being loudly visible in everyone's
  inbox reads as leadership, whatever you actually said.
- Economy: every clause either loads the setup or fires the payoff; no
  word can be cut without losing the headcount, the hypocrisy, or the
  promotion.

The program writes the single line to /output/entry.txt, as the
competition's grader expects.
"""

import os

LINE = "I hit reply-all to 400 coworkers to say 'please stop replying all,' then got promoted for demonstrating leadership."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "joke must be between 1 and 200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "joke must be a single line"
    assert "  " not in LINE, "joke must not contain double spaces"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
