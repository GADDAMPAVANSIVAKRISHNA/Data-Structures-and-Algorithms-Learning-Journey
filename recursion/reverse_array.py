"""
Concept: Recursion with Pointers (Array Reversal)
--------------------------------------------------
To reverse an array recursively, we swap the leftmost and rightmost elements, 
then recursively call the function on the remaining inner subarray.

Base Case:
  - When the left pointer meets or crosses the right pointer (left >= right).
Recursive Relation:
  - swap(arr[left], arr[right])
  - reverse(arr, left + 1, right - 1)
"""

from typing import List

def reverse_array_recursive(arr: List[int], left: int, right: int) -> None:
    # 1. Base Case: If pointers cross or meet, the array is fully reversed
    if left >= right:
        return
        
    # 2. Swap elements at left and right indices
    arr[left], arr[right] = arr[right], arr[left]
    
    # 3. Recursive Step: Move pointers inward
    reverse_array_recursive(arr, left + 1, right - 1)


def reverse_array_iterative(arr: List[int]) -> None:
    """
    Iterative alternative using a standard while loop.
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


# --- Verification & Test Cases ---
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        ([9], [9]),
        ([], [])
    ]
    
    print("Running tests for Array Reversal...")
    for idx, (original, expected) in enumerate(test_cases, 1):
        # We copy the list to avoid modifying the test case data in-place
        arr_rec = original.copy()
        reverse_array_recursive(arr_rec, 0, len(arr_rec) - 1)
        
        arr_iter = original.copy()
        reverse_array_iterative(arr_iter)
        
        assert arr_rec == expected, f"Recursive failed for {original}: got {arr_rec}, expected {expected}"
        assert arr_iter == expected, f"Iterative failed for {original}: got {arr_iter}, expected {expected}"
        print(f"Test {idx} passed: {original} -> {arr_rec}")
        
    print("All test cases passed successfully!\n")
    print("--- Complexity Analysis ---")
    print("Time Complexity: O(N) because we make N/2 swaps, each takes O(1) time.")
    print("Space Complexity: O(N) auxiliary space due to the call stack of depth N/2.")
