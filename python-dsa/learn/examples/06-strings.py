# Page 6: Strings
# Run me with:  python3 06-strings.py

word = "python"

# Index: position numbers start at 0. Negative ones count from the back.
print(word[0])        # p   (first letter)
print(word[-1])       # n   (last letter)
print(len(word))      # 6   (how many letters)

# Slicing: [start:stop] stops right BEFORE stop
print(word[0:3])      # pyt
print(word[2:])       # thon
print(word[::-1])     # nohtyp  (backwards)

# in: is this piece inside?
print("th" in word)   # True

# Methods give you a NEW string. The old one doesn't change.
name = "  Tanvi Kumar  "
print(name.strip())             # Tanvi Kumar
print(name.strip().lower())     # tanvi kumar  (one tool after another)
print("1.1.1.1".replace(".", "[.]"))   # 1[.]1[.]1[.]1
print("hello".find("l"))        # 2   (first place it appears)
print("hello".find("z"))        # -1  (not there)
print("2024".isdigit())         # True
print("hi!".isalnum())          # False (! is not a letter or digit)

# split makes a list of words. join glues them back.
words = "fly me   to the moon".split()
print(words)              # ['fly', 'me', 'to', 'the', 'moon']
print(words[-1])          # moon (the last word)
print(len(words[-1]))     # 4    (letters in the last word)
print("-".join(words))    # fly-me-to-the-moon

# Strings can't be changed in place. Build a new one instead.
new_word = "j" + word[1:]
print(new_word)           # jython

# Numbers to text and back
n = 1234
print(str(n)[::-1])       # 4321
print(len(str(n)))        # 4   (number of digits)
print(int("42") + 1)      # 43

# f-strings: values inside text
print(f"{word} has {len(word)} letters, backwards it's {word[::-1]}")

# Try changing things:
#   1. Set word to your own name. Predict every line before you run it.
#   2. Is "level" the same backwards? Print  "level" == "level"[::-1]
#   3. Print the first word of "fly me to the moon" in capital letters.
