# 🛡️ The Brute Force Approach

The **Brute Force** approach is the most straightforward and intuitive way to solve a problem. It solves the problem by directly applying the problem statement, often by checking **every single possibility** (exhaustive search) without applying any optimizations.

---

## 🔑 Key Characteristics
* **Intuitiveness**: It is usually the first solution that comes to mind.
* **Correctness**: Since it checks all possible cases, it is guaranteed to find the correct solution (if one exists).
* **High Time Complexity**: Because it does not avoid redundant calculations, it is typically slow and often results in a **Time Limit Exceeded (TLE)** error on large inputs.
* **Low Space Complexity**: It usually requires minimal extra memory (often $O(1)$) as it operates directly on the input structure.

---

## 📚 Examples & Code

### Example 1: Two Sum
**Problem**: Find two numbers in an array `nums` that add up to a specific `target` and return their indices.

#### Brute Force Logic:
We check every single pair of numbers in the array using nested loops.
* Outer loop picks index `i`.
* Inner loop picks index `j` (where `j > i`).
* If `nums[i] + nums[j] == target`, we return `[i, j]`.

#### Python Code:
```python
def two_sum_brute_force(nums, target):
    n = len(nums)
    # Check every possible pair
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

#### Complexity:
* **Time Complexity**: $O(N^2)$ because of two nested loops traversing the array.
* **Space Complexity**: $O(1)$ as we do not use any extra memory.

---

### Example 2: Maximum Subarray Sum
**Problem**: Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

#### Brute Force Logic:
We generate the sum of every possible contiguous subarray.
* Loop `i` starts the subarray.
* Loop `j` ends the subarray.
* Loop `k` calculates the sum from index `i` to `j`.
* We keep track of the maximum sum found so far.

#### Python Code:
```python
def max_subarray_sum_brute_force(nums):
    n = len(nums)
    max_sum = float('-inf')
    
    # Generate all possible subarrays
    for i in range(n):
        for j in range(i, n):
            current_sum = 0
            # Calculate sum of subarray nums[i...j]
            for k in range(i, j + 1):
                current_sum += nums[k]
            max_sum = max(max_sum, current_sum)
            
    return max_sum
```

#### Complexity:
* **Time Complexity**: $O(N^3)$ due to three nested loops.
* **Space Complexity**: $O(1)$ as we only track a few variables.
