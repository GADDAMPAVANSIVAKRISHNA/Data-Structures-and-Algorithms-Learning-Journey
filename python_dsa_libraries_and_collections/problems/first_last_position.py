"""
Problem: Find First and Last Position of Element in Sorted Array
URL: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Description:
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Key Python Library Used:
- `bisect`: Provides binary search utilities. We use `bisect_left` and `bisect_right` 
  to find boundaries of the target range in O(log N) time.
"""

import bisect
from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    # bisect_left returns the first index where target can be inserted to keep order.
    # If target is in the list, left will point to its FIRST occurrence.
    left = bisect.bisect_left(nums, target)
    
    # Check if target is not in the list:
    # 1. left is out of bounds (larger than any element in the list)
    # 2. nums[left] is not equal to target (target is missing but belongs at left index)
    if left >= len(nums) or nums[left] != target:
        return [-1, -1]
        
    # bisect_right returns the index after the last occurrence of target.
    # So, the last occurrence of target is at right - 1.
    right = bisect.bisect_right(nums, target)
    
    return [left, right - 1]

# --- Verification & Test Cases ---
if __name__ == "__main__":
    test_cases = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
        ([2, 2], 2, [0, 1]),
        ([1, 3, 5, 7], 3, [1, 1])
    ]
    
    print("Running tests for Find First and Last Position of Element in Sorted Array...")
    for idx, (nums, target, expected) in enumerate(test_cases, 1):
        result = searchRange(nums, target)
        assert result == expected, f"Test {idx} failed: searchRange({nums}, {target}) expected {expected}, got {result}"
        print(f"Test {idx} passed: nums={nums}, target={target} -> {result}")
        
    print("All test cases passed successfully!\n")
    print("--- Complexity Analysis ---")
    print("Time Complexity: O(log N). bisect_left and bisect_right both perform a standard binary search, which takes logarithmic time.")
    print("Space Complexity: O(1). No auxiliary space is used except index pointers.")
