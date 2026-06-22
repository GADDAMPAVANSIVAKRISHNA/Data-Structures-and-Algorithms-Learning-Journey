"""
Question: Move all zeros to the end of the array while maintaining relative order of non-zero elements.

Example:
Input: arr = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
"""

from typing import List

def move_zeros_brute(arr: List[int]) -> None:
    """
    Brute Force Approach: Use temporary list to collect non-zeros, then fill remainder with zeros.
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    n = len(arr)
    temp = [x for x in arr if x != 0]
    while len(temp) < n:
        temp.append(0)
    for i in range(n):
        arr[i] = temp[i]


def move_zeros_optimal(arr: List[int]) -> None:
    """
    Optimal Approach: Two-pointer swapping in-place.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(arr)
    j = -1
    for i in range(n):
        if arr[i] == 0:
            j = i
            break
            
    if j == -1:
        return
        
    for i in range(j + 1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
