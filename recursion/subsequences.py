"""
Concept: Backtracking & Subsequence Generation
---------------------------------------------
A subsequence is a sequence that can be derived from another sequence by 
deleting some or no elements without changing the order of the remaining elements.

For every element in the input list, we have two choices:
  1. Take the element into the current subsequence.
  2. Do NOT take the element into the current subsequence.

This "Take or Not Take" logic generates a binary decision tree of depth N, 
yielding all 2^N subsequences.
"""

from typing import List

def get_subsequences(arr: List[int]) -> List[List[int]]:
    result = []
    
    def solve(index: int, current: List[int]):
        # Base Case: If we have made decisions for all elements in the array
        if index == len(arr):
            result.append(current.copy()) # Store a copy of the current subsequence
            return
            
        # Decision 1: Take the current element
        current.append(arr[index])
        solve(index + 1, current)
        
        # Backtrack: Remove the element to reset the state for the next decision
        current.pop()
        
        # Decision 2: Do NOT take the current element
        solve(index + 1, current)
        
    solve(0, [])
    return result

# --- Verification & Test Cases ---
if __name__ == "__main__":
    test_cases = [
        ([1, 2], [[1, 2], [1], [2], []]),
        ([3], [[3], []]),
        ([], [[]])
    ]
    
    print("Running tests for Subsequence Generation...")
    for idx, (arr, expected) in enumerate(test_cases, 1):
        # We sort sublists to make comparison order-independent
        result = get_subsequences(arr)
        
        sorted_result = sorted([sorted(sub) for sub in result])
        sorted_expected = sorted([sorted(sub) for sub in expected])
        
        assert sorted_result == sorted_expected, f"Failed for {arr}: got {sorted_result}, expected {sorted_expected}"
        print(f"Test {idx} passed: Subsequences of {arr} -> {result}")
        
    print("All test cases passed successfully!\n")
    print("--- Complexity Analysis ---")
    print("Time Complexity: O(2^N * N). There are 2^N leaf nodes in the decision tree, and at each leaf, we copy the current array of length up to N.")
    print("Space Complexity: O(N) due to the call stack height and recursion depth.")
