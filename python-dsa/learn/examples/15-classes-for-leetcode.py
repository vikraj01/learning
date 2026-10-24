# Page 15: Classes for LeetCode
# Run me with:  python3 15-classes-for-leetcode.py


# --- A class is a blank form, an object is one filled-in copy ---

class Student:
    def __init__(self, name, age):   # runs by itself when you make an object
        self.name = name             # write on THIS copy
        self.age = age

a = Student("Tanvi", 20)
b = Student("Riya", 19)
print(a.name, a.age)                 # Tanvi 20
print(b.name, b.age)                 # Riya 19


# --- Linked list: LeetCode's ListNode, with the # removed ---

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# build 1 -> 2 -> 3 by hand, from the back
third = ListNode(3)
second = ListNode(2, third)
head = ListNode(1, second)
print(head.val, head.next.val, head.next.next.val)   # 1 2 3
print(head.next.next.next)                           # None (end of the train)

# walk it
node = head
while node:                 # while there IS a node
    print("node", node.val)
    node = node.next        # step to the next coach

# safe look-ahead: check node.next exists before reading it
node = head
while node and node.next:
    print(node.val, "->", node.next.val)
    node = node.next


# --- Helpers to test linked list problems on your laptop ---

def build_list(values):
    head = None
    for v in values[::-1]:
        head = ListNode(v, head)
    return head

def to_list(head):
    values = []
    node = head
    while node:
        values.append(node.val)
        node = node.next
    return values

print(to_list(build_list([7, 8, 9])))   # [7, 8, 9]
print(build_list([]))                   # None (an empty linked list)


# A made-up problem in the LeetCode shape
class Solution:
    def countNodes(self, head: ListNode | None) -> int:   # a node, or nothing
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        return count

print(Solution().countNodes(build_list([4, 5, 6])))   # 3
print(Solution().countNodes(build_list([])))          # 0


# --- Binary tree: LeetCode's TreeNode, with the # removed ---

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#         4
#       /   \
#      2     7
#     / \
#    1   3
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(root.left.right.val)    # 3  (go left, then right)
print(root.right.left)        # None (7 has no children)

def tree_sum(root):
    if not root:              # an empty tree adds nothing
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)

print(tree_sum(root))         # 17


# --- A class that remembers things between calls ("design" problems) ---

class ScoreBoard:
    def __init__(self):
        self.scores = []      # set up once, kept on the object

    def add(self, score: int) -> None:
        self.scores.append(score)

    def best(self) -> int:
        return max(self.scores)

board = ScoreBoard()
board.add(40)
board.add(75)
board.add(62)
print(board.best())           # 75


# Try changing things:
#   1. Build 10 -> 20 -> 30 -> 40 with build_list and walk it.
#   2. Add a node 9 as the right child of 7. What does tree_sum print now?
#   3. Add a method worst() to ScoreBoard that returns the smallest score.
#   4. Remove the "node and" from the look-ahead loop and start it with node = None.
#      Read the error.
