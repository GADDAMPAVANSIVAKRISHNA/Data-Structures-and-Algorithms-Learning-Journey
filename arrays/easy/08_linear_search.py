"""
Question: Linear Search. Find the first occurrence index of a target element in an array.

Example:
Input: arr = [1, 2, 3, 4, 5], target = 3
Output: 2
"""

from typing import List

def linear_search_brute(arr: List[int], target: int) -> int:
    """
    Brute Force Approach: Standard sequential scan from beginning to end.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def linear_search_optimal(arr: List[int], target: int) -> int:
    """
    Optimal Approach: Search from both ends simultaneously (two-pointer search).
    Increases likelihood of early exit in practical scenarios.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        if arr[left] == target:
            return left
        if arr[right] == target:
            return right
        left += 1
        right -= 1
        
    return -1
