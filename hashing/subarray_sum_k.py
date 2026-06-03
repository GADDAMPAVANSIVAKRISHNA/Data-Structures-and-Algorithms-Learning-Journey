"""
Concept: Prefix Sum Hashing (Subarray Sum Equals K)
-----------------------------------------------------
Problem: Given an array of integers nums and an integer k, 
find the total number of continuous subarrays whose sum equals k.

Algorithm:
  If a subarray nums[i...j] sums to k, then:
     PrefixSum[j] - PrefixSum[i-1] = k
     PrefixSum[i-1] = PrefixSum[j] - k

  We traverse the array, maintaining a running prefix sum (PrefixSum[j]):
    - Calculate complement: target_prefix = running_sum - k
    - If target_prefix exists in our hash map, add its frequency to our count.
    - Add the running_sum to our hash map (or increment its count).
    
  Initialize hash map with {0: 1} to handle subarrays starting from index 0.
"""

from typing import List

def subarray_sum_k(nums: List[int], k: int) -> int:
    count = 0
    running_sum = 0
    # Map to store frequency of prefix sums: {prefix_sum: frequency}
    # Initialized with {0: 1} to account for subarrays starting at index 0
    prefix_sums = {0: 1}
    
    for num in nums:
        running_sum += num
        
        # Check if there is a prefix subarray that can be removed to yield sum k
        target_prefix = running_sum - k
        if target_prefix in prefix_sums:
            count += prefix_sums[target_prefix]
            
        # Record the current prefix sum in the hash map
        prefix_sums[running_sum] = prefix_sums.get(running_sum, 0) + 1
        
    return count

# --- Verification & Test Cases ---
if __name__ == "__main__":
    test_cases = [
        ([1, 1, 1], 2, 2),        # Subarrays: [1, 1] at index 0-1, [1, 1] at index 1-2
        ([1, 2, 3], 3, 2),        # Subarrays: [1, 2] at index 0-1, [3] at index 2
        ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4), # Subarrays: [3, 4], [7], [7, 2, -3, 1], [2, -3, 1, 4, 3...]
        ([9, 4, 20, 3, 10, 5], 33, 2)
    ]
    
    print("Running tests for Subarray Sum Equals K...")
    for idx, (nums, k, expected) in enumerate(test_cases, 1):
        result = subarray_sum_k(nums, k)
        assert result == expected, f"Test {idx} failed: got {result}, expected {expected}"
        print(f"Test {idx} passed: nums={nums}, k={k} -> {result}")
        
    print("All test cases passed successfully!\n")
    print("--- Complexity Analysis ---")
    print("Time Complexity: O(N) since we iterate through the list of length N exactly once and perform O(1) hash map operations.")
    print("Space Complexity: O(N) to store prefix sums in the hash map in the worst case.")
