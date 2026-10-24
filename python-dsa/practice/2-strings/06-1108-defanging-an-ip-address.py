"""
1108. Defanging an IP Address  (Easy)
https://leetcode.com/problems/defanging-an-ip-address/

In plain words:
    You get an IP address as text, like "1.1.1.1". (An IP address is four
    numbers with dots between them.) Return the same text, but with every
    "." changed into "[.]".

Example:
    address = "1.1.1.1"       ->  "1[.]1[.]1[.]1"
    address = "255.100.50.0"  ->  "255[.]100[.]50[.]0"

You'll need: the string method replace (page 6), return (page 4)

Run this file:  python3 06-1108-defanging-an-ip-address.py
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (address, expected answer)
    ("1.1.1.1", "1[.]1[.]1[.]1"),
    ("255.100.50.0", "255[.]100[.]50[.]0"),
    ("0.0.0.0", "0[.]0[.]0[.]0"),
]

for address, expected in tests:
    got = Solution().defangIPaddr(address)
    # repr() prints text with its quotes, so you can see spaces at the start or end
    if got == expected:
        print("✓", repr(address), "->", repr(got))
    else:
        print("✗", repr(address), "-> got", repr(got), "but expected", repr(expected))

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: You are swapping one piece of text for another, everywhere it appears.
# Hint 2: Page 6 has a string method that does exactly that.
# Hint 3: address.replace(old, new) with old = "." and new = "[.]".
