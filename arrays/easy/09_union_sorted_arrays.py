"""
Question: Find the union of two sorted arrays. The union should be sorted and contain only unique elements.

Example:
Input: a = [1, 2, 3, 4, 5], b = [1, 2, 3, 6, 7]
Output: [1, 2, 3, 4, 5, 6, 7]
"""

from typing import List

def union_sorted_arrays_brute(a: List[int], b: List[int]) -> List[int]:
    """
    Brute Force Approach: Put all elements in a set and sort.
    Time Complexity: O((N + M) log(N + M))
    Space Complexity: O(N + M)
    """
    st = set(a).union(set(b))
    return sorted(list(st))


def union_sorted_arrays_optimal(a: List[int], b: List[int]) -> List[int]:
    """
    Optimal Approach: Two-pointer merge traversal.
    Time Complexity: O(N + M)
    Space Complexity: O(1) auxiliary (excluding the output union list)
    """
    n, m = len(a), len(b)
    i, j = 0, 0
    union_res = []
    
    def add_element(val: int):
        if not union_res or union_res[-1] != val:
            union_res.append(val)

    while i < n and j < m:
        if a[i] <= b[j]:
            add_element(a[i])
            i += 1
        else:
            add_element(b[j])
            j += 1
            
    while i < n:
        add_element(a[i])
        i += 1
        
    while j < m:
        add_element(b[j])
        j += 1
        
    return union_res
