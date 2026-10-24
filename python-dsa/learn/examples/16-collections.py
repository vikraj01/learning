# Page 16: The collections toolbox
# Run me with:  python3 16-collections.py

from collections import defaultdict, Counter, deque


# --- defaultdict(int): counting without .get ---

counts = defaultdict(int)          # a new key starts at 0
for ch in "mississippi":
    counts[ch] += 1
print(dict(counts))                # {'m': 1, 'i': 4, 's': 4, 'p': 2}


# --- defaultdict(list): grouping ---

words = ["apple", "banana", "avocado", "cherry", "blueberry"]
groups = defaultdict(list)         # a new key starts as []
for w in words:
    groups[w[0]].append(w)
print(dict(groups))


# --- Grouping pairs: students by section ---

students = [("Tanvi", "10A"), ("Riya", "10B"), ("Aman", "10A"), ("Kabir", "10C"), ("Zoya", "10B")]
by_section = defaultdict(list)
for name, section in students:
    by_section[section].append(name)
for section in sorted(by_section):
    print(section, "->", by_section[section])


# --- defaultdict(set): no repeats ---

sign_ins = [("Tanvi", "Mon"), ("Riya", "Mon"), ("Tanvi", "Mon"), ("Tanvi", "Wed")]
days = defaultdict(set)            # a new key starts as set()
for name, day in sign_ins:
    days[name].add(day)
print(dict(days))                  # Tanvi's Mon is there once


# --- Counter ---

c = Counter("mississippi")
print(c.most_common(2))                          # [('i', 4), ('s', 4)]
print(c["z"])                                    # 0, not an error
print(Counter("listen") == Counter("silent"))    # True: anagrams
print(Counter("banana") - Counter("bnaxa"))      # what's missing: one a, one n


# --- deque: a queue ---

q = deque()
q.append("Tanvi")       # join at the back
q.append("Riya")
q.append("Aman")
print(q.popleft())      # Tanvi: first in, first served
print(q)                # deque(['Riya', 'Aman'])


# --- A ticket counter: one ticket per turn, then back of the queue ---

queue = deque([("Tanvi", 2), ("Riya", 1), ("Aman", 3)])   # (name, tickets needed)
turn = 0
while queue:                              # until nobody is left
    name, needed = queue.popleft()        # out of the front
    turn += 1
    needed -= 1
    print("turn", turn, ":", name, "buys one, needs", needed, "more")
    if needed > 0:
        queue.append((name, needed))      # back in at the back


# --- maxlen: keep only the last few ---

recent = deque(maxlen=3)
for n in [1, 2, 3, 4, 5]:
    recent.append(n)
print(recent)                             # deque([3, 4, 5], maxlen=3)


# Try changing things:
#   1. Group the words by their length instead of their first letter.
#   2. Add ("Riya", "10C") to students. Where does she appear?
#   3. Give Riya 4 tickets to buy. Which turn does she finish on?
#   4. Change maxlen to 2. What's left in recent?
