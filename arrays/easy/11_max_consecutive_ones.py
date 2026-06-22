"""
Question: Find the maximum number of consecutive 1s in a binary array.

Example:
Input: arr = [1, 1, 0, 1, 1, 1]
Output: 3
"""

from typing import List

def find_max_consecutive_ones_brute(arr: List[int]) -> int:
    """
    Brute Force Approach: Check all subarrays to find the longest one containing only 1s.
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    max_count = 0
    for i in range(n):
        for j in range(i, n):
            # Check if subarray arr[i...j] contains only 1s
            only_ones = True
            for k in range(i, j + 1):
                if arr[k] != 1:
                    only_ones = False
                    break
            if only_ones:
                max_count = max(max_count, j - i + 1)
    return max_count


def find_max_consecutive_ones_optimal(arr: List[int]) -> int:
    """
    Optimal Approach: Single-pass linear scan counting consecutive 1s.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    max_count = 0
    current_count = 0
    
    for num in arr:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
            
    return max_count
