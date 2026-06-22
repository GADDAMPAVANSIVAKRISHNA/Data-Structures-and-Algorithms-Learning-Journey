"""
Question: Left rotate the array by one place.

Example:
Input: arr = [1, 2, 3, 4, 5]
Output: [2, 3, 4, 5, 1]
"""

from typing import List

def left_rotate_one_brute(arr: List[int]) -> None:
    """
    Brute Force Approach: Create an auxiliary array to hold the rotated result.
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    n = len(arr)
    if n <= 1:
        return
        
    temp = [0] * n
    for i in range(1, n):
        temp[i - 1] = arr[i]
    temp[n - 1] = arr[0]
    
    for i in range(n):
        arr[i] = temp[i]


def left_rotate_one_optimal(arr: List[int]) -> None:
    """
    Optimal Approach: Shift elements left by one and swap the first element to the end.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(arr)
    if n <= 1:
        return
        
    temp = arr[0]
    for i in range(1, n):
        arr[i - 1] = arr[i]
    arr[n - 1] = temp
