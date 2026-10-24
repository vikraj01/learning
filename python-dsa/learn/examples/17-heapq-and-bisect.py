# Page 17: heapq and bisect
# Run me with:  python3 17-heapq-and-bisect.py

import heapq
import bisect


# --- A heap: smallest out first ---

heap = []
for n in [5, 1, 8, 3, 9, 2]:
    heapq.heappush(heap, n)
print(heap)                    # looks unsorted, but heap[0] is the smallest
print(heap[0])                 # 1  (peek)
print(heapq.heappop(heap))     # 1
print(heapq.heappop(heap))     # 2

nums = [7, 2, 9, 4, 1]
heapq.heapify(nums)            # in place, returns None
print(nums[0])                 # 1


# --- Biggest first: store with a minus sign ---

max_heap = []
for n in [7, 2, 9, 4, 1]:
    heapq.heappush(max_heap, -n)
print(-heapq.heappop(max_heap))    # 9
print(-heapq.heappop(max_heap))    # 7


# --- (priority, item) tuples: ties are broken by the second item ---

patients = []
heapq.heappush(patients, (2, "Riya"))
heapq.heappush(patients, (1, "Aman"))
heapq.heappush(patients, (3, "Tanvi"))
heapq.heappush(patients, (1, "Kabir"))
while patients:
    urgency, name = heapq.heappop(patients)
    print("next:", name, "(urgency", urgency, ")")


# --- The k biggest ---

scores = [55, 92, 78, 99, 63, 85]
print(heapq.nlargest(3, scores))   # [99, 92, 85]
print(heapq.nsmallest(2, scores))  # [55, 63]

# keep only the k biggest as numbers arrive; heap[0] is the k-th biggest
k = 3
top = []
for score in scores:
    heapq.heappush(top, score)
    if len(top) > k:
        heapq.heappop(top)         # throw out the smallest
print("3rd biggest:", top[0])      # 85


# --- bisect: where does x go in a sorted list? ---

nums = [10, 20, 30, 30, 40]
print(bisect.bisect_left(nums, 30))    # 2  (before the 30s)
print(bisect.bisect_right(nums, 30))   # 4  (after the 30s)
print(bisect.bisect_left(nums, 25))    # 2  (25 would go between 20 and 30)

bisect.insort(nums, 25)                # insert, keeping it sorted
print(nums)                            # [10, 20, 25, 30, 30, 40]


# --- The same as bisect_left, by hand ---

def my_bisect_left(nums, x):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2      # // : an index must be a whole number
        if nums[mid] < x:
            left = mid + 1             # answer is right of mid
        else:
            right = mid - 1            # mid might be it; look left too
    return left

nums = [10, 20, 30, 30, 40, 50, 60]
for x in [5, 30, 45, 60, 70]:
    print(x, "->", my_bisect_left(nums, x), "and bisect says", bisect.bisect_left(nums, x))


# Try changing things:
#   1. Push your own numbers into a heap and pop them all. Are they sorted?
#   2. Change k to 2. What's the 2nd biggest score?
#   3. Add (2, "Zoya") to the patients. Where does she come out?
#   4. Add a print inside my_bisect_left to watch left, right and mid.
