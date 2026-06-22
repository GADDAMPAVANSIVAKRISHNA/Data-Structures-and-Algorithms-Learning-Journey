"""
Question: Check if the array is sorted and rotated (LeetCode 1752: Check if Array is Sorted II).
An array is sorted and rotated if it was originally sorted in non-decreasing order, 
then rotated some number of positions (including zero).

Example:
Input: nums = [3, 4, 5, 1, 2]
Output: True
"""

from typing import List

def is_sorted_and_rotated_brute(arr: List[int]) -> bool:
    """
    Brute Force Approach: For each rotation index shift, check if it forms a sorted array.
    Time Complexity: O(N^2)
    Space Complexity: O(N)
    """
    n = len(arr)
    if n <= 1:
        return True
        
    for shift in range(n):
        rotated = arr[shift:] + arr[:shift]
        # Check if rotated array is sorted
        is_sorted = True
        for i in range(1, n):
            if rotated[i] < rotated[i - 1]:
                is_sorted = False
                break
        if is_sorted:
            return True
            
    return False


def is_sorted_and_rotated_optimal(arr: List[int]) -> bool:
    """
    Optimal Approach: Count transition drops where arr[i] > arr[(i+1)%n].
    There can be at most one drop in a sorted and rotated array.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(arr)
    if n <= 1:
        return True
        
    count_drops = 0
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            count_drops += 1
            if count_drops > 1:
                return False
                
    return True
