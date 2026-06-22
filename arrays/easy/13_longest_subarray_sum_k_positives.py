"""
Question: Find the length of the longest subarray with sum K (contains only positive integers/zeros).

Example:
Input: arr = [1, 2, 3, 1, 1, 1, 1], K = 3
Output: 3 (subarray is [1, 1, 1])
"""

from typing import List

def get_longest_subarray_brute(arr: List[int], k: int) -> int:
    """
    Brute Force Approach: Try all possible subarrays using nested loops.
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    max_len = 0
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum == k:
                max_len = max(max_len, j - i + 1)
    return max_len


def get_longest_subarray_optimal(arr: List[int], k: int) -> int:
    """
    Optimal Approach: Two-pointer/sliding window technique (only works for positive values).
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(arr)
    left, right = 0, 0
    current_sum = 0
    max_len = 0
    
    while right < n:
        current_sum += arr[right]
        
        while left <= right and current_sum > k:
            current_sum -= arr[left]
            left += 1
            
        if current_sum == k:
            max_len = max(max_len, right - left + 1)
            
        right += 1
        
    return max_len
