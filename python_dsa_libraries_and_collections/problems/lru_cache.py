"""
Problem: LRU Cache (Least Recently Used Cache)
URL: https://leetcode.com/problems/lru-cache/

Description:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity): Initialize the LRU cache with positive size capacity.
- get(int key): Return the value of the key if it exists, otherwise return -1.
- put(int key, int value): Update the value of the key if the key exists. 
  Otherwise, add the key-value pair. If the keys exceed the capacity, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Key Python Library Used:
- `collections.OrderedDict`: An ordered dictionary subclass. 
  It provides move_to_end(key, last=True) and popitem(last=False) in O(1) time.
  This allows us to maintain elements in usage order easily.
"""

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # OrderedDict maintains key insertion order.
        # We will keep the most recently used items at the end (right) 
        # and the least recently used items at the front (left).
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Since we accessed the key, move it to the end to mark it as most recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value
            self.cache[key] = value
            # Move to end as it's recently updated/accessed
            self.cache.move_to_end(key)
        else:
            # Check capacity before inserting
            if len(self.cache) >= self.capacity:
                # Evict the least recently used element (the first item / leftmost item)
                # last=False pops in FIFO order (leftmost)
                self.cache.popitem(last=False)
            
            # Insert the new element at the end
            self.cache[key] = value

# --- Verification & Test Cases ---
if __name__ == "__main__":
    print("Running tests for LRU Cache...")
    
    # Initialize cache with capacity 2
    lru = LRUCache(2)
    
    lru.put(1, 1)           # cache is {1: 1}
    lru.put(2, 2)           # cache is {1: 1, 2: 2}
    
    # Test get(1)
    val = lru.get(1)
    assert val == 1, f"Expected 1, got {val}"
    # cache is now {2: 2, 1: 1} (1 was accessed, so it moved to the end)
    
    # Put (3, 3) -> exceeds capacity, evicts key 2 (least recently used)
    lru.put(3, 3)           # cache is {1: 1, 3: 3}
    
    # Verify key 2 is evicted
    val = lru.get(2)
    assert val == -1, f"Expected -1 (evicted), got {val}"
    
    # Put (4, 4) -> exceeds capacity, evicts key 1
    lru.put(4, 4)           # cache is {3: 3, 4: 4}
    
    # Verify key 1 is evicted
    val = lru.get(1)
    assert val == -1, f"Expected -1 (evicted), got {val}"
    
    # Verify key 3 is present
    val = lru.get(3)
    assert val == 3, f"Expected 3, got {val}"
    
    # Verify key 4 is present
    val = lru.get(4)
    assert val == 4, f"Expected 4, got {val}"
    
    print("All test cases passed successfully!\n")
    print("--- Complexity Analysis ---")
    print("Time Complexity: O(1) for both get() and put() because OrderedDict hashing lookup and pointer manipulation are O(1) on average.")
    print("Space Complexity: O(C) where C is the capacity of the cache.")
