"""
Problem: Top K Frequent Elements
URL: https://leetcode.com/problems/top-k-frequent-elements/

Description:
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Key Python Libraries Used:
- `collections.Counter`: For O(N) frequency mapping of array elements.
- `heapq`: For extracting the top K elements efficiently in O(N log K) time.
"""

from collections import Counter
import heapq
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    # Step 1: Count frequency of each number -> O(N) time & O(N) space
    count_map = Counter(nums)
    
    # Approach 1: Using heapq.nlargest
    # nlargest takes an iterable, a key, and retrieves the top k.
    # Time Complexity: O(N log K)
    return heapq.nlargest(k, count_map.keys(), key=count_map.get)


def topKFrequentManualHeap(nums: List[int], k: int) -> List[int]:
    """
    Alternative approach demonstrating manual Min-Heap maintenance to limit size to K.
    Time Complexity: O(N log K)
    Space Complexity: O(N)
    """
    count_map = Counter(nums)
    min_heap = []
    
    for num, freq in count_map.items():
        # Push tuple (frequency, number)
        # Python heapq compares elements starting from index 0 of the tuple.
        heapq.heappush(min_heap, (freq, num))
        
        # If heap exceeds size K, pop the smallest frequency element
        if len(min_heap) > k:
            heapq.heappop(min_heap)
            
    # Extract numbers from the heap
    return [num for freq, num in min_heap]


# --- Verification & Test Cases ---
if __name__ == "__main__":
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([4, 1, -1, 2, -1, 2, 3, 2], 2, [2, -1]),
    ]
    
    print("Running tests for Top K Frequent Elements...")
    for idx, (nums, k, expected) in enumerate(test_cases, 1):
        # We sort output lists to compare because order of return doesn't matter
        result1 = sorted(topKFrequent(nums, k))
        result2 = sorted(topKFrequentManualHeap(nums, k))
        expected_sorted = sorted(expected)
        
        assert result1 == expected_sorted, f"Test {idx} Approach 1 failed: got {result1}, expected {expected_sorted}"
        assert result2 == expected_sorted, f"Test {idx} Approach 2 failed: got {result2}, expected {expected_sorted}"
        print(f"Test {idx} passed: nums={nums}, k={k} -> {result1}")
        
    print("All test cases passed successfully!\n")
    print("--- Complexity Analysis ---")
    print("Time Complexity: O(N log K). Building frequency map is O(N). Keeping a heap of size K takes O(log K) for each insert, totaling O(N log K).")
    print("Space Complexity: O(N) to store frequencies in Counter and elements in heap.")
