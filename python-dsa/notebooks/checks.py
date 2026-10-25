"""Helpers for the check cells in the notebooks.

You don't need to read this file. The notebooks use it to tell you
whether your answer is right.
"""

# The right letter for each quiz question, and a hint for when it's not.
ANSWERS = {
    "01-q1": ("B", "Without quotes, 4 + 4 is maths. What does Python do with maths?"),
    "01-q2": ("A", "With quotes, it's only text. Python shows text exactly as written."),
    "01-q3": ("B", "Look at the 'Errors are normal' part again."),
    "01-q4": ("A", "Look at the 'Comments' part again."),
}


def check_answer(question, answer):
    right, hint = ANSWERS[question]
    answer = str(answer).strip().upper()
    if answer == "?" or answer == "":
        print("Put your letter between the quotes first, then run both cells again.")
    elif answer == right:
        print("✓ Correct!")
    else:
        print("✗ Not yet. You chose", answer + ".")
        print("Hint:", hint)
