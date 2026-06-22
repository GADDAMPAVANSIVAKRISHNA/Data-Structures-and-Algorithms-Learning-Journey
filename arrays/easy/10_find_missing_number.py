"""
Question: Find the missing number in an array containing elements from 1 to N (or 0 to N).

Example:
Input: arr = [1, 2, 4, 5], N = 5
Output: 3
"""

from typing import List

def find_missing_number_brute(arr: List[int], n: int) -> int:
    """
    Brute Force Approach: Perform a linear search for each number from 1 to n.
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    for i in range(1, n + 1):
        found = False
        for num in arr:
            if num == i:
                found = True
                break
        if not found:
            return i
    return -1


def find_missing_number_optimal(arr: List[int], n: int) -> int:
    """
    Optimal Approach: Use the XOR property to find the missing number in one pass.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    xor1 = 0
    for i in range(1, n + 1):
        xor1 ^= i
        
    xor2 = 0
    for num in arr:
        xor2 ^= num
        
    return xor1 ^ xor2
