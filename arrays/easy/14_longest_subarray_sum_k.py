"""
Question: Find the length of the longest subarray with sum K (includes positives, negatives, and zeros).

Example:
Input: arr = [1, -1, 5, -2, 3], K = 3
Output: 4 (subarray is [1, -1, 5, -2])
"""

from typing import List

def get_longest_subarray_all_brute(arr: List[int], k: int) -> int:
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


def get_longest_subarray_all_optimal(arr: List[int], k: int) -> int:
    """
    Optimal Approach: Prefix Sum with Hash Map (works with positive, negative, and zero values).
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    n = len(arr)
    pre_sum_map = {}
    current_sum = 0
    max_len = 0
    
    for i in range(n):
        current_sum += arr[i]
        
        if current_sum == k:
            max_len = max(max_len, i + 1)
            
        rem = current_sum - k
        if rem in pre_sum_map:
            length = i - pre_sum_map[rem]
            max_len = max(max_len, length)
            
        if current_sum not in pre_sum_map:
            pre_sum_map[current_sum] = i
            
    return max_len
