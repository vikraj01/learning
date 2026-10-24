# Page 11: Two pointers and stacks
# Run me with:  python3 11-two-pointers-and-stacks.py


# --- Two pointers from both ends: reverse in place ---

def reverse_in_place(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        print(f"  left={left} right={right}  swap {nums[left]} and {nums[right]}")
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

letters = ["a", "b", "c", "d", "e"]
reverse_in_place(letters)
print(letters)                    # ['e', 'd', 'c', 'b', 'a']


# --- Two pointers from both ends: palindrome check ---

def is_palindrome(word):
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False          # stop as soon as two ends differ
        left += 1
        right -= 1
    return True

print(is_palindrome("racecar"))   # True
print(is_palindrome("rocket"))    # False


# --- Slow "write" pointer, fast "read" pointer ---
# Keep only the positive numbers, packed at the front. Return how many.

def keep_positives(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] > 0:
            nums[write] = nums[read]
            write += 1
        print(f"  read={read} write={write}  {nums}")
    return write

nums = [3, -1, 4, -5, 9]
k = keep_positives(nums)
print(k, nums[:k])                # 3 [3, 4, 9]


# --- Stack: a list where you only use the end ---

stack = []
stack.append(1)                   # push
stack.append(2)                   # push
print(stack[-1])                  # 2  (peek at the top)
print(stack.pop())                # 2  (take the top)
print(stack)                      # [1]
print(len(stack) == 0)            # False (not empty yet)


# Round brackets only: every "(" needs a ")" after it
def round_brackets_ok(s):
    stack = []
    for ch in s:
        if ch == "(":
            stack.append(ch)      # waiting for its partner
        else:
            if len(stack) == 0:
                return False      # a ")" with nothing to close
            stack.pop()           # pair done
    return len(stack) == 0        # anything left was never closed

print(round_brackets_ok("(()())"))   # True
print(round_brackets_ok("(()"))      # False
print(round_brackets_ok("())("))     # False

# Try changing things:
#   1. Reverse a list with an even number of items, like [1, 2, 3, 4].
#      How many swaps happen?
#   2. Change keep_positives to keep only the even numbers.
#   3. Push "a", "b", "c" onto a stack, then pop three times. What order
#      do they come out in?
