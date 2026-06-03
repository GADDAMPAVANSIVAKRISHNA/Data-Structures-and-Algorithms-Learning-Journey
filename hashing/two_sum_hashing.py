"""
Concept: Lookup Optimization using Hashing (Two Sum)
------------------------------------------------------
The Two Sum problem asks for indices of two numbers that add up to a target.
Instead of checking all pairs or sorting, we store seen elements and their indices in a hash map.

Algorithm:
  For each number x at index i:
    - complement = target - x
    - If complement is in hash map, return its index and i.
    - Else, store {x: i} in hash map.
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {} # map to store {value: index}
    
    for i, num in enumerate(nums):
        complement = target - num
        # O(1) average lookup in hash map
        if complement in seen:
            return [seen[complement], i]
            
        # O(1) average insertion
        seen[num] = i
        
    return []

# --- Verification & Test Cases ---
if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 5, 8, 3], 13, [1, 2])
    ]
    
    print("Running tests for Two Sum Hashing...")
    for idx, (nums, target, expected) in enumerate(test_cases, 1):
        result = two_sum(nums, target)
        assert result == expected, f"Test {idx} failed: got {result}, expected {expected}"
        print(f"Test {idx} passed: nums={nums}, target={target} -> {result}")
        
    print("All test cases passed successfully!\n")
    print("--- Complexity Analysis ---")
    print("Time Complexity: O(N) since we traverse the array of size N exactly once and perform hash lookups in O(1) average time.")
    print("Space Complexity: O(N) to store elements in the hash map.")
