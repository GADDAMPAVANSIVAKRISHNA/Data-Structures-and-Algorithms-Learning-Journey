# 🚀 The Optimal Approach

The **Optimal Approach** is the best possible solution to a problem, achieving the lowest theoretical boundaries for **Time Complexity** and/or **Space Complexity**. It is usually derived by utilizing efficient data structures (like Hash Maps, Tries, Heaps) or algorithmic paradigms (like Greedy algorithms, Dynamic Programming, Two Pointers).

---

## 🔑 Key Characteristics
* **Zero Redundant Operations**: Every step of the algorithm processes input data efficiently.
* **Minimal Time Complexity**: Achieves optimal performance bounds (e.g., $O(N)$ or $O(\log N)$).
* **Space-Time Trade-off**: Often uses extra space (e.g., a hash table) to achieve a massive improvement in speed.

---

## 📚 Examples & Code

### Example 1: Two Sum (Hash Map)
Instead of searching or sorting, we can use a **Hash Map** (Python `dict`) to look up complements in $O(1)$ average time.

#### Optimal Approach Logic:
1. Initialize an empty dictionary `seen` to store `{value: index}`.
2. Iterate through the array. For each number `num` at index `i`:
   * Calculate its complement: `complement = target - num`.
   * Check if `complement` is already in `seen`.
   * If yes, return `[seen[complement], i]`.
   * If no, add the current number and its index to `seen`: `seen[num] = i`.

#### Python Code:
```python
def two_sum_optimal(nums, target):
    seen = {} # {value: index}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
        
    return []
```

#### Complexity:
* **Time Complexity**: $O(N)$ because we traverse the array of size N exactly once and perform $O(1)$ hash table lookups.
* **Space Complexity**: $O(N)$ to store up to N elements in the dictionary.

---

### Example 2: Maximum Subarray Sum (Kadane's Algorithm)
We can solve this problem in $O(N)$ time and $O(1)$ space using **Kadane's Algorithm**, which is a classic dynamic programming technique.

#### Optimal Approach Logic:
We traverse the array and maintain two variables:
1. `current_sum`: The maximum sum of subarray ending at the current position.
2. `max_sum`: The global maximum sum found so far.

For each element `x` in the array:
* We decide whether to add `x` to the existing subarray or start a new subarray from `x` itself:
  $$current\_sum = \max(x, current\_sum + x)$$
* Update `max_sum` with `current_sum` if it is larger.

#### Python Code:
```python
def max_subarray_sum_optimal(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    
    for i in range(1, len(nums)):
        # Decides whether to extend the previous subarray or start a new one
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
        
    return max_sum
```

#### Complexity:
* **Time Complexity**: $O(N)$ since we loop through the list of length N exactly once.
* **Space Complexity**: $O(1)$ as we only maintain two scalar values.
