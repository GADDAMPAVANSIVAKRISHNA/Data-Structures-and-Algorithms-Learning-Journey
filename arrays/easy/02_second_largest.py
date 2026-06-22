"""
Question: Find the second largest and second smallest elements in an array.

Example:
Input: arr = [1, 2, 4, 7, 7, 5]
Output: Second Smallest = 2, Second Largest = 5
"""

from typing import List, Tuple
import sys

def get_second_elements_brute(arr: List[int]) -> Tuple[int, int]:
    """
    Brute Force Approach: Sort the array, then find second distinct elements.
    Time Complexity: O(N log N)
    Space Complexity: O(N)
    """
    n = len(arr)
    if n < 2:
        return -1, -1
    
    unique_sorted = sorted(list(set(arr)))
    if len(unique_sorted) < 2:
        return -1, -1
        
    return unique_sorted[1], unique_sorted[-2]


def get_second_elements_optimal(arr: List[int]) -> Tuple[int, int]:
    """
    Optimal Approach: Single-pass linear scan keeping track of first and second.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(arr)
    if n < 2:
        return -1, -1
        
    smallest = sys.maxsize
    second_smallest = sys.maxsize
    largest = -sys.maxsize - 1
    second_largest = -sys.maxsize - 1
    
    for x in arr:
        # Update largest and second_largest
        if x > largest:
            second_largest = largest
            largest = x
        elif x > second_largest and x != largest:
            second_largest = x
            
        # Update smallest and second_smallest
        if x < smallest:
            second_smallest = smallest
            smallest = x
        elif x < second_smallest and x != smallest:
            second_smallest = x
            
    s_sec = second_smallest if second_smallest != sys.maxsize else -1
    l_sec = second_largest if second_largest != (-sys.maxsize - 1) else -1
    
    return s_sec, l_sec
