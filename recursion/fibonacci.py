"""
Concept: Multiple Recursion (Fibonacci)
---------------------------------------
The Fibonacci sequence is defined as:
  - F(0) = 0, F(1) = 1 (Base Cases)
  - F(N) = F(N-1) + F(N-2) (Recursive Step)

This is a tree recursion problem because the function calls itself twice, 
leading to a tree-like execution graph.
"""

def fibonacci_recursive(n: int) -> int:
    # 1. Base Cases
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    # 2. Recursive Step
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n: int) -> int:
    """
    Iterative approach using dynamic programming variables.
    Optimizes time to O(N) and space to O(1).
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1


# --- Verification & Test Cases ---
if __name__ == "__main__":
    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (10, 55),
        (15, 610)
    ]
    
    print("Running tests for Fibonacci...")
    for idx, (n, expected) in enumerate(test_cases, 1):
        res_rec = fibonacci_recursive(n)
        res_iter = fibonacci_iterative(n)
        
        assert res_rec == expected, f"Recursive failed for N={n}: got {res_rec}, expected {expected}"
        assert res_iter == expected, f"Iterative failed for N={n}: got {res_iter}, expected {expected}"
        print(f"Test {idx} passed: F({n}) = {res_rec}")
        
    print("All test cases passed successfully!\n")
    print("--- Complexity Analysis ---")
    print("Time Complexity (Recursive): O(2^N) because each call spawns two other calls, creating a binary tree of depth N.")
    print("Space Complexity (Recursive): O(N) due to the call stack height (max depth of the recursion tree).")
