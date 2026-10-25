"""Helpers for the check cells in the notebooks.

You don't need to read this file. The notebooks use it to tell you
whether your answer is right.
"""


def check(got, expected):
    """Compare your answer with the right one, like a LeetCode test case."""
    if got == expected:
        print("✓ Correct:", repr(got))
    else:
        print("✗ Expected", repr(expected) + ", but got", repr(got))
        if got is None:
            print("  Got None. If this is a function, did you forget `return`?")


def check_answer(question, answer):
    """Check a quiz letter."""
    right, hint = ANSWERS[question]
    answer = str(answer).strip().upper()
    if answer == "?" or answer == "":
        print("Put your letter between the quotes first, then run both cells again.")
    elif answer == right:
        print("✓ Correct!")
    else:
        print("✗ Not yet. You chose", answer + ".")
        print("Hint:", hint)


# The right letter for each quiz question, and a hint for when it's not.
ANSWERS = {
    "01-q1": ("B", "Without quotes, 4 + 4 is maths. What does Python do with maths?"),
    "01-q2": ("A", "With quotes, it's only text. Python shows text exactly as written."),
    "01-q3": ("B", "Look at the 'Errors are normal' part again."),
    "01-q4": ("A", "Look at the 'Comments' part again."),
}
