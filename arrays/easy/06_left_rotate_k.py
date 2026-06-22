"""
Question: Left rotate the array by K places.

Example:
Input: arr = [1, 2, 3, 4, 5], K = 2
Output: [3, 4, 5, 1, 2]
"""

from typing import List

def left_rotate_k_brute(arr: List[int], k: int) -> None:
    """
    Brute Force Approach: Store first K elements in temporary array and shift the rest.
    Time Complexity: O(N)
    Space Complexity: O(K)
    """
    n = len(arr)
    if n <= 1:
        return
    k = k % n
    if k == 0:
        return
        
    temp = arr[:k]
    for i in range(k, n):
        arr[i - k] = arr[i]
    for i in range(n - k, n):
        arr[i] = temp[i - (n - k)]


def reverse_sublist(arr: List[int], start: int, end: int) -> None:
    """Helper function to reverse a portion of list in-place."""
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def left_rotate_k_optimal(arr: List[int], k: int) -> None:
    """
    Optimal Approach: Reversal Algorithm.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(arr)
    if n <= 1:
        return
    k = k % n
    if k == 0:
        return
        
    # Step 1: Reverse the first k elements
    reverse_sublist(arr, 0, k - 1)
    # Step 2: Reverse the remaining elements
    reverse_sublist(arr, k, n - 1)
    # Step 3: Reverse the entire array
    reverse_sublist(arr, 0, n - 1)
