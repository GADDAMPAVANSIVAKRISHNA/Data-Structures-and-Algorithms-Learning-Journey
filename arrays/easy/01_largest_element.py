"""
Question: Find the largest element in an array.

Example:
Input: arr = [3, 2, 1, 5, 2]
Output: 5
"""

from typing import List

def find_largest_element_brute(arr: List[int]) -> int:
    """
    Brute Force Approach: Sort the array and return the last element.
    Time Complexity: O(N log N)
    Space Complexity: O(N) (due to sorted())
    """
    if not arr:
        raise ValueError("Array is empty")
    temp = sorted(arr)
    return temp[-1]


def find_largest_element_optimal(arr: List[int]) -> int:
    """
    Optimal Approach: Single-pass linear scan.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    if not arr:
        raise ValueError("Array is empty")
        
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest
