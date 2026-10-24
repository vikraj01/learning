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
        # replace() makes a new string where every "." has become "[.]"
        defanged = address.replace(".", "[.]")
        return defanged


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

# ---------- how this works ----------
#
# replace(old, new) finds every copy of old in the string and gives back a
# new string with each one swapped for new. It changes all of them, not
# only the first.
#
# Example: address = "1.1.1.1"
#   "1.1.1.1".replace(".", "[.]")  ->  "1[.]1[.]1[.]1"
#
# Another way: split the address at the dots, then join the pieces back
# with "[.]" between them:
#     return "[.]".join(address.split("."))
