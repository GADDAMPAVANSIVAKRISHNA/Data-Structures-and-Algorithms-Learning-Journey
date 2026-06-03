"""
Problem: Valid Parentheses
URL: https://leetcode.com/problems/valid-parentheses/

Description:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Key Python Library Used:
- `collections.deque`: Used as a LIFO (Last-In-First-Out) Stack because of its O(1) append/pop.
"""

from collections import deque

def isValid(s: str) -> bool:
    # We use deque as a Stack. 
    # Under the hood, deque has O(1) push (append) and pop (pop).
    stack = deque()
    
    # Map each closing bracket to its corresponding opening bracket
    bracket_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    for char in s:
        # If it is a closing bracket
        if char in bracket_map:
            # Pop the top element if stack is not empty, else assign a dummy character '#'
            top_element = stack.pop() if stack else '#'
            
            # If the mapping doesn't match the popped element, it's invalid
            if bracket_map[char] != top_element:
                return False
        else:
            # It's an opening bracket, push to the stack
            stack.append(char)
            
    # If stack is empty, all opening brackets were matched and closed correctly
    return len(stack) == 0

# --- Verification & Test Cases ---
if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("(", False),
        (")", False),
        ("((", False)
    ]
    
    print("Running tests for Valid Parentheses...")
    for idx, (s, expected) in enumerate(test_cases, 1):
        result = isValid(s)
        assert result == expected, f"Test {idx} failed: isValid('{s}') expected {expected}, got {result}"
        print(f"Test {idx} passed: '{s}' -> {result}")
    
    print("All test cases passed successfully!\n")
    print("--- Complexity Analysis ---")
    print("Time Complexity: O(N) since we traverse the string of length N exactly once.")
    print("Space Complexity: O(N) in the worst case to store all open brackets in the stack (e.g. '((((').")
