"""
Question: Find the number that appears once in an array where every other element appears twice.

Example:
Input: arr = [4, 1, 2, 1, 2]
Output: 4
"""

from typing import List

def find_single_number_brute(arr: List[int]) -> int:
    """
    Brute Force Approach: Count frequencies of all elements using a hash map.
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        
    for num, count in freq.items():
        if count == 1:
            return num
            
    raise ValueError("No element with frequency 1 found")


def find_single_number_optimal(arr: List[int]) -> int:
    """
    Optimal Approach: Use the bitwise XOR property (A ^ A = 0) to cancel out pairs in one pass.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    single = 0
    for num in arr:
        single ^= num
    return single
