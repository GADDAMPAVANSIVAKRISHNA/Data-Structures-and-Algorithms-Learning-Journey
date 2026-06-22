"""
Question: Remove duplicates from a sorted array in-place and return the number of unique elements.

Example:
Input: arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output: 5 (array becomes [0, 1, 2, 3, 4, ...])
"""

from typing import List

def remove_duplicates_brute(arr: List[int]) -> int:
    """
    Brute Force Approach: Insert all elements into a set, sort, and copy back.
    Time Complexity: O(N log N)
    Space Complexity: O(N)
    """
    if not arr:
        return 0
    unique_elements = sorted(list(set(arr)))
    for idx, val in enumerate(unique_elements):
        arr[idx] = val
    return len(unique_elements)


def remove_duplicates_optimal(arr: List[int]) -> int:
    """
    Optimal Approach: Two-pointer technique in-place.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(arr)
    if n == 0:
        return 0
        
    i = 0
    for j in range(1, n):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
            
    return i + 1
