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
    "02-q1": ("A", "How many whole times does 5 fit into 17?"),
    "02-q2": ("B", "Take away the whole 5s from 17. What's left?"),
    "02-q3": ("B", "Look at the 'Maths' part: what kind of number does / always give?"),
    "02-q4": ("A", "Even numbers split into 2 with nothing left over."),
    "03-q1": ("B", "Look at the '= and == are different' part again."),
    "03-q2": ("A", "Python stops at the first question that's true."),
    "03-q3": ("B", "and needs both sides to be True. Is 2 > 5?"),
    "04-q1": ("B", "What does a function give back when it has no return line?"),
    "04-q2": ("A", "LeetCode never looks at your screen."),
    "04-q3": ("C", "What happens to the lines after a return?"),
    "04-q4": ("B", "Parameters are the names in the def line. What are the values you pass in called?"),
    "05-q1": ("A", "Which button is the final test with hundreds of hidden inputs?"),
    "05-q2": ("B", "Read the type hint after the arrow ->."),
    "05-q3": ("A", "None means nothing came back from your function."),
    "05-q4": ("B", "Look at 'Calling a function that lives in the box' again."),
    "06-q1": ("B", "The slice takes indexes 1, 2 and 3. Index 4 is where it stops, and it isn't taken."),
    "06-q2": ("B", "A negative index counts from the back: -1 is always the last letter."),
    "06-q3": ("A", "upper() makes a new string. Did anything keep it?"),
    "06-q4": ("C", "split() makes a list of the words, and join puts the string before the dot between them."),
    "07-q1": ("A", "sorted() makes a new list. Does it touch the old one?"),
    "07-q2": ("B", "Look at 'The trap: sort() gives back nothing'."),
    "07-q3": ("B", "b = a doesn't copy. Look at 'Two names, one list'."),
    "07-q4": ("A", "Read it left to right: first the inner list, then the box inside it."),
    "08-q1": ("A", "range stops before the end number. Would 10 be included?"),
    "08-q2": ("B", "Write n down after each time round: 1, 3, ... and check n < 20 each time."),
    "08-q3": ("B", "Where is total = 0? It runs every time round."),
    "08-q4": ("A", "enumerate counts from 0, like indexes."),
    "09-q1": ("B", "You want how many, not a sum of words. Look at 'Pattern 2: counter'."),
    "09-q2": ("B", "Does any of the numbers beat the starting value? Look at 'The trap: what does best start as?'."),
    "09-q3": ("B", "You can only say 'no' after looking at everything. Look at 'The classic bug'."),
    "09-q4": ("C", "Count the pairs for each i: i = 0 gives 3, i = 1 gives ..."),
    "10-q1": ("B", "Look at the part '`in` checks the keys, not the values' again."),
    "10-q2": ("C", "Look at the part '`get`: the safe way to ask' again. What does the second thing inside the brackets do?"),
    "10-q3": ("A", "A dictionary can't hold the same key twice. Look at 'Adding and changing' again."),
    "10-q4": ("B", "Look at '1. A plain `for`' in the looping part again."),
    "11-q1": ("B", "get gives 0 when the key is missing. What is 0 + 1, and where is it stored?"),
    "11-q2": ("A", "Look at 'Question 2: which ones appear only once?' again. Why did the first s look unique?"),
    "11-q3": ("C", "You need the number that would complete the answer: target - n."),
    "11-q4": ("B", "Look at 'What goes wrong if you write first' again."),
    "12-q1": ("B", "set() removes the repeats first. Which different numbers are left?"),
    "12-q2": ("B", "Look at 'Common mistakes' again: what type is {}?"),
    "12-q3": ("A", "a - b keeps what's in a but not in b."),
    "12-q4": ("B", "Python builds the tuple on the right first, (q, p), then unpacks it."),
    "13-q1": ("B", "Write down left and right for each step: (0, 5), then (1, 4)... when does left < right stop being true?"),
    "13-q2": ("B", "Look at the read/write table again: which rows change `write`?"),
    "13-q3": ("A", "Look at 'Why left < right, and not left != right?' and the 4-item run."),
    "13-q4": ("C", "3 and 5 are smaller than 8, so they were added inside the loop. What's left in the second list?"),
    "14-q1": ("A", "Write the stack after each step. The pop takes the top, which is the last one pushed."),
    "14-q2": ("A", "Look at 'The order inside and matters' and run those two cells again."),
    "14-q3": ("B", "Look at the table under round_ok: what is left on the stack for '(()'?"),
    "14-q4": ("C", "Think of the pile of plates: which plate do you take?"),
    "15-q1": ("B", "Row first: grid[2] is the third row. Then pick box 1 inside it."),
    "15-q2": ("A", "Look at 'The trap' part: which one repeats the same row?"),
    "15-q3": ("B", "Try each direction from (0, 0): which ones give -1?"),
    "15-q4": ("C", "Run the grid[-1][0] cell again: what did it give?"),
    "16-q1": ("A", "d is 100 and a is 97. Look at 'The trick: position in the alphabet'."),
    "16-q2": ("B", "Look at the number line in '// and % with negative numbers'."),
    "16-q3": ("B", "key=len sorts by length. What does reverse=True do to that order?"),
    "16-q4": ("C", "Look at the first one in 'Common mistakes'."),
    "17-q1": ("B", "The base case answers straight away, without calling itself. Look at 'The two parts'."),
    "17-q2": ("A", "Look at 'No base case: RecursionError' in Common mistakes."),
    "17-q3": ("B", "Nothing prints on the way down. Look at the table under 'Predict, then run'."),
    "17-q4": ("C", "What does a function give back when it never reaches a return?"),
    "18-q1": ("A", "count += 1 means count = count + 1. Look at 'Changing an outer variable: nonlocal'."),
    "18-q2": ("B", "Look at the call counts with and without @cache."),
    "18-q3": ("C", "A method lives inside the class. How does it reach itself?"),
    "18-q4": ("A", "Look at 'Which one when?' under the two styles."),
    "19-q1": ("B", "Look at 'What is self? Watch it happen' again."),
    "19-q2": ("A", "Look at 'Two copies are separate' again."),
    "19-q3": ("A", "Look at 'Why self.scores and not scores?' again."),
    "19-q4": ("C", "Look at 'Forgetting the brackets' in Common mistakes."),
    "20-q1": ("B", "head.next is the 8. What does the last node hold in next?"),
    "20-q2": ("A", "Look at the table in 'Walking the list' again: what stops the loop?"),
    "20-q3": ("B", "Which line answers without calling tree_sum again?"),
    "20-q4": ("C", "Look at 'Forgetting node = node.next' in Common mistakes."),
    "21-q1": ("A", "A Counter gives a count for any letter, even one that never appeared."),
    "21-q2": ("B", "popleft takes from the front. Which end did 8 go in at?"),
    "21-q3": ("A", "Look at 'Why not a list?' again."),
    "21-q4": ("C", "Look at the first one in Common mistakes."),
    "22-q1": ("C", "heap[0] is always the smallest item."),
    "22-q2": ("A", "Look at 'Biggest first: the minus trick' again."),
    "22-q3": ("B", "bisect_right gives the gap after all the 3s. Count the boxes before it."),
    "22-q4": ("B", "Work out (0 + 3) / 2. Is there a box with that number?"),
}
