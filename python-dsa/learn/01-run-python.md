# Run Python

After this page you'll be able to run Python, print things on the screen, and write and run your own `.py` file.

## A program is a recipe

A recipe is a list of steps: boil water, add tea, add milk, wait two minutes. You follow the steps from top to bottom, one at a time.

A **program** is the same thing for a computer. It's a list of steps, written down, that the computer follows from top to bottom. **Python** is the language we write those steps in. It looks a bit like English, which makes it a good first language.

The computer is a very careful cook, though. It does exactly what the recipe says, nothing more. If a word is misspelled, it stops and tells you. That's normal, and you'll see it happen on this page.

## Check that Python is there

Open a **terminal** (the window where you type commands) and type:

```bash
python3 --version
```

You'll see something like:

```
Python 3.12.3
```

The exact number may be a bit different. Anything starting with `Python 3` is fine.

## Talk to Python directly

Type `python3` on its own and press Enter:

```bash
python3
```

```
Python 3.12.3 (main, Aug 31 2026, 10:18:26) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The `>>>` is called the **prompt**. It means "Python is listening, type a line". Whatever you type, Python runs it straight away and shows the answer. This is called the **interactive prompt**, and it's a good place to try small things.

Type these, one line at a time:

```
>>> print("Hello")
Hello
>>> print(2 + 3)
5
>>> print("2 + 3")
2 + 3
```

- **`print(...)`** shows whatever is inside the brackets on the screen.
- Text goes inside **quotes** (`"Hello"`). Python shows it exactly as written.
- Without quotes, `2 + 3` is maths, so Python works out the answer first and prints `5`.
- With quotes, `"2 + 3"` is only text, so it prints `2 + 3`.

To leave, type:

```
>>> exit()
```

You're back in the normal terminal.

## Write a program in a file

The interactive prompt forgets everything when you close it. To keep a program, write it in a **file**. Python files end in **`.py`**.

Make a new file called `hello.py` in your editor and put this one line in it:

```python
print("Hello, Tanvi!")
```

Save it. In the terminal, go to the folder where you saved it and run:

```bash
python3 hello.py
```

```
Hello, Tanvi!
```

That's your first program. `python3 hello.py` means "Python, read this file and follow the steps in it".

## Many steps, top to bottom

Change `hello.py` to this:

```python
print("Hello, Tanvi!")
print("I am learning Python.")
print("I have", 3, "cats")
print()
print("The end.")
```

Run it again:

```bash
python3 hello.py
```

```
Hello, Tanvi!
I am learning Python.
I have 3 cats

The end.
```

- Python ran the lines in order, top to bottom, like a recipe.
- You can give `print` several things, separated by **commas**. It puts a space between them.
- `print()` with nothing inside prints an empty line.

## Comments: notes for people

A line that starts with **`#`** is a **comment**. Python skips it completely. Comments are notes for whoever reads the code (including you, next week).

```python
# This line is a comment. Python ignores it.
print("This line runs.")   # a comment can also sit at the end of a line
```

```
This line runs.
```

## Errors are normal

Everyone who writes code sees errors every day. An error isn't you breaking something. It's Python saying "I didn't understand this line, here's where and why".

Make a small typo on purpose. Put this in `hello.py` (notice `prnt`, with a missing `i`):

```python
print("Hello")
prnt("Bye")
```

Run it:

```
Hello
Traceback (most recent call last):
  File "/home/tanvi/hello.py", line 2, in <module>
    prnt("Bye")
    ^^^^
NameError: name 'prnt' is not defined. Did you mean: 'print'?
```

(The path after `File` will be wherever your file is saved.)

That block of text is called a **traceback**. It looks scary, but read it like this:

1. **Read the last line first.** It says what went wrong: `NameError: name 'prnt' is not defined`. Python doesn't know any word called `prnt`. It even guesses what you meant: `Did you mean: 'print'?`
2. **Then look up for the line number.** `line 2` tells you where. The `^^^^` points at the exact word.
3. Notice that `Hello` was printed first. Python followed the recipe until it hit the step it didn't understand, then stopped.

Fix the typo, run it again, and it works.

## Try it

From the `learn` folder, run `examples/01-run-python.py`:

```bash
python3 examples/01-run-python.py
```

```
Hello, Tanvi!
This is my first Python program.
7
5
2 + 3
5
I have 3 cats

The end.
```

Then open the file and change things: print your own name, print `12 * 12` (`*` means "times"), and remove one letter from a `print` to see the error.

## Common mistakes

**Forgetting a closing bracket or quote.** If you write `print("one"` with no `)` at the end, you'll see:

```
SyntaxError: '(' was never closed
```

A **SyntaxError** means Python couldn't even read the line, because something is missing or out of place. Here, a `(` was opened and never closed. Count your brackets and quotes: every `(` needs a `)`, every `"` needs another `"`.

**Typing `python3 hello.py` inside the `>>>` prompt.** That's a terminal command, not Python. If you see `>>>`, type `exit()` first, then run the file.

## Check yourself

1. What's the difference between `print(4 + 4)` and `print("4 + 4")`?
2. In a traceback, which line do you read first?
3. What does a line starting with `#` do?

## Next

Next you'll store values in named boxes and do maths with them: [Variables and numbers](02-variables-and-numbers.md).
