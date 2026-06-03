# 📈 The Better Approach

A **Better Approach** represents a middle ground between the brute force solution and the absolute optimal solution. It is achieved by recognizing and removing some of the redundant work or patterns in the brute force solution, often at the cost of sorting or using some additional memory.

---

## 🔑 Key Characteristics
* **Reduction in Redundant Work**: It avoids completely checking every single possibility from scratch.
* **Improved Time Complexity**: Often reduces the time complexity (e.g., from $O(N^2)$ to $O(N \log N)$ or from $O(N^3)$ to $O(N^2)$).
* **Trade-offs**: May introduce sorting (which takes $O(N \log N)$) or require basic extra data structures.

---

## 📚 Examples & Code

### Example 1: Two Sum (Sorting + Two Pointers)
Instead of searching every pair via nested loops, we can sort the array and use the **Two Pointers** technique.

#### Better Approach Logic:
1. Store elements along with their original indices (since we need to return indices).
2. Sort the array in ascending order of values.
3. Place a pointer at the beginning (`left`) and another at the end (`right`).
4. Calculate their sum:
   * If `sum == target`, return original indices.
   * If `sum < target`, increment `left` to increase the sum.
   * If `sum > target`, decrement `right` to decrease the sum.

#### Python Code:
```python
def two_sum_better(nums, target):
    # Store value with original index: [(val, original_idx), ...]
    indexed_nums = [(val, idx) for idx, val in enumerate(nums)]
    # Sort by value
    indexed_nums.sort(key=lambda x: x[0])
    
    left = 0
    right = len(nums) - 1
    
    while left < right:
        current_sum = indexed_nums[left][0] + indexed_nums[right][0]
        if current_sum == target:
            return [indexed_nums[left][1], indexed_nums[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
            
    return []
```

#### Complexity:
* **Time Complexity**: $O(N \log N)$ due to sorting the array of size N. The two pointer traversal takes $O(N)$.
* **Space Complexity**: $O(N)$ because we created a new list of tuples to keep track of original indices.

---

### Example 2: Maximum Subarray Sum ($O(N^2)$)
In the brute force approach, we recalculated the sum of elements from scratch using a third loop. We can optimize this to $O(N^2)$ by accumulating the sum incrementally.

#### Better Approach Logic:
Instead of running a third loop `k` to recalculate the sum of `nums[i...j]`, we can compute it on the fly:
$$\text{sum}(nums[i...j]) = \text{sum}(nums[i...j-1]) + nums[j]$$

#### Python Code:
```python
def max_subarray_sum_better(nums):
    n = len(nums)
    max_sum = float('-inf')
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            # Accumulate sum of elements on the fly
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)
            
    return max_sum
```

#### Complexity:
* **Time Complexity**: $O(N^2)$ because we eliminated the third inner loop.
* **Space Complexity**: $O(1)$ since only a few tracking variables are used.
