"""
Concept: Frequency Counting using Hashing
------------------------------------------
Frequency counting is the most fundamental application of hashing. 
It maps values to their occurrences.

We demonstrate two techniques:
  1. Array-based Hashing (Pre-allocated list):
     Used when the elements are in a known, small range (e.g., lowercase characters a-z, index 0 to 25).
     Provides extremely fast, low-overhead lookup.
  2. Hash Map (Dictionary):
     Used when the keys are arbitrary, sparse, or of unknown types.
"""

from typing import List, Dict

def count_char_frequencies_array(s: str) -> List[int]:
    """
    Counts frequency of lowercase letters 'a' through 'z' using a pre-allocated array.
    Index of character 'char' is: ord(char) - ord('a')
    """
    # Create an array of size 26 initialized with 0
    freq = [0] * 26
    
    for char in s:
        if 'a' <= char <= 'z':
            index = ord(char) - ord('a')
            freq[index] += 1
            
    return freq


def count_element_frequencies_map(nums: List[int]) -> Dict[int, int]:
    """
    Counts frequency of arbitrary numbers using a Hash Map (dict).
    """
    freq_map = {}
    for num in nums:
        # If key is already in map, increment; else initialize to 1
        freq_map[num] = freq_map.get(num, 0) + 1
    return freq_map


# --- Verification & Test Cases ---
if __name__ == "__main__":
    print("Running tests for Frequency Counting...")
    
    # Test character counting
    char_test = "abracadabra"
    char_freq = count_char_frequencies_array(char_test)
    # 'a' (5 times), 'b' (2 times), 'c' (1 time), 'd' (1 time), 'r' (2 times)
    assert char_freq[ord('a') - ord('a')] == 5
    assert char_freq[ord('b') - ord('a')] == 2
    assert char_freq[ord('c') - ord('a')] == 1
    assert char_freq[ord('z') - ord('a')] == 0
    print(f"Character counting test passed for string: '{char_test}'")
    
    # Test hash map counting
    num_test = [4, 5, 4, 1, 5, 4, 9]
    num_freq = count_element_frequencies_map(num_test)
    expected_map = {4: 3, 5: 2, 1: 1, 9: 1}
    assert num_freq == expected_map, f"Expected {expected_map}, got {num_freq}"
    print(f"Map-based counting test passed for array: {num_test}")
    
    print("All test cases passed successfully!\n")
    print("--- Complexity Analysis ---")
    print("Character Counting (Array):")
    print("  - Time Complexity: O(N) where N is length of string.")
    print("  - Space Complexity: O(1) auxiliary space (size of array is fixed at 26).")
    print("Map Counting (Dictionary):")
    print("  - Time Complexity: O(N) where N is number of elements in array.")
    print("  - Space Complexity: O(U) where U is the number of UNIQUE elements stored in the map.")
