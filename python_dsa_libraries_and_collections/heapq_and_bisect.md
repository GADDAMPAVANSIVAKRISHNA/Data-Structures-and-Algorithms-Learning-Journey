# 📐 The `heapq` and `bisect` Modules

These two standard libraries provide optimized implementations of **Heaps (Priority Queues)** and **Binary Search** algorithms, which are vital for solving optimization and search problems.

---

## 1. `heapq` (Min-Heap / Priority Queue)
Python's `heapq` module provides a binary heap implementation using a regular list. By default, it is a **Min-Heap** (where the parent node is always smaller than or equal to its children, and the smallest element is always at index `0`).

### 💡 Essential Operations & Syntax

```python
import heapq

# 1. In-place conversion of list to heap: O(N)
heap = [5, 7, 9, 1, 3]
heapq.heapify(heap)
print(heap)  # [1, 3, 9, 7, 5] (Note: index 0 is the smallest element)

# 2. Push element: O(log N)
heapq.heappush(heap, 4)  # [1, 3, 4, 7, 5, 9]

# 3. Pop element: O(log N)
smallest = heapq.heappop(heap)
print(smallest)  # Returns 1 -> heap is now [3, 5, 4, 7, 9]

# 4. Push-Pop optimization: O(log N)
# Pushes item and pops the smallest in a single, optimized operation.
smallest_now = heapq.heappushpop(heap, 2)
# Since 2 is smaller than the minimum 3, it pushes 2 and pops 2.

# 5. Extract K largest/smallest elements: O(N log K)
nums = [5, 7, 9, 1, 3, 2, 8]
print(heapq.nlargest(3, nums))   # [9, 8, 7]
print(heapq.nsmallest(3, nums))  # [1, 2, 3]
```

### 📈 How to Implement a Max-Heap?
Since `heapq` only supports min-heaps, we can implement a **Max-Heap** by **multiplying numbers by -1** before pushing them onto the heap. When popping, we multiply by -1 again to recover the original number.

```python
import heapq

max_heap = []
values = [10, 20, 5, 15]

# Push elements as negative values
for val in values:
    heapq.heappush(max_heap, -val)

# Pop elements (multiply by -1 to restore original positive value)
largest = -heapq.heappop(max_heap)
print(largest)  # 20 (The maximum value!)
```

### 👥 Custom Objects in Heap
If you want to store custom objects (or tuples) in a heap, Python compares them starting from the first element of the tuple. If there is a tie, it compares the second element, and so on.
```python
# Format: (priority_value, identifier / object)
heapq.heappush(max_heap, (-priority, task_name))
```

---

## 2. `bisect` (Binary Search)
The `bisect` module provides binary search algorithms for finding insert positions in sorted lists, keeping the list sorted without re-sorting it.

### 💡 Essential Operations & Syntax

```python
import bisect

# The list MUST be sorted!
arr = [1, 3, 4, 4, 4, 6, 7]

# 1. bisect_left: Returns insertion index of val. If val is present, index is before (left of) matches.
idx_left = bisect.bisect_left(arr, 4)
print(idx_left)  # 2 (index of the FIRST 4)

# 2. bisect_right: Returns insertion index of val. If val is present, index is after (right of) matches.
idx_right = bisect.bisect_right(arr, 4)
print(idx_right)  # 5 (index after the LAST 4)

# 3. insort_left: Inserts element in sorted order (O(N) time because of list shift)
bisect.insort_left(arr, 5)
print(arr)  # [1, 3, 4, 4, 4, 5, 6, 7]
```

### 🧠 DSA Use Cases
#### A. Finding bounds in a sorted array
To find the range of indices where a value exists in a sorted array, use `bisect_left` and `bisect_right`:
```python
def find_range(arr, target):
    left = bisect.bisect_left(arr, target)
    right = bisect.bisect_right(arr, target)
    
    # Check if target actually exists in the array
    if left < len(arr) and arr[left] == target:
        return [left, right - 1]
    return [-1, -1]
```

#### B. Range Lookup (e.g. Grades mapping)
```python
def get_grade(score):
    # Cutoffs: 60 -> D, 70 -> C, 80 -> B, 90 -> A
    cutoffs = [60, 70, 80, 90]
    grades = ['F', 'D', 'C', 'B', 'A']
    idx = bisect.bisect_right(cutoffs, score)
    return grades[idx]

print(get_grade(85))  # Output: 'B'
```
