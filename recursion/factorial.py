"""
Concept: Linear Recursion (Factorial)
--------------------------------------
Factorial of N (written as N!) is the product of all positive integers less than or equal to N.
Mathematical definition:
  - 0! = 1 (Base Case)
  - N! = N * (N - 1)! (Recursive Step)

This is a classic linear recursion example since each function call makes exactly one recursive call.
"""

def factorial_recursive(n: int) -> int:
    # 1. Base Case: factorial of 0 or 1 is 1
    if n <= 1:
        return 1
        
    # 2. Recursive Step: N * factorial(N - 1)
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Iterative alternative using a loop.
    Optimizes space since it doesn't use the recursion stack.
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# --- Verification & Test Cases ---
if __name__ == "__main__":
    test_cases = [
        (0, 1),
        (1, 1),
        (5, 120),
        (10, 3628800)
    ]
    
    print("Running tests for Factorial...")
    for idx, (n, expected) in enumerate(test_cases, 1):
        res_rec = factorial_recursive(n)
        res_iter = factorial_iterative(n)
        
        assert res_rec == expected, f"Recursive failed for N={n}: got {res_rec}, expected {expected}"
        assert res_iter == expected, f"Iterative failed for N={n}: got {res_iter}, expected {expected}"
        print(f"Test {idx} passed: {n}! = {res_rec}")
        
    print("All test cases passed successfully!\n")
    print("--- Complexity Analysis ---")
    print("Time Complexity: O(N) because there are N recursive calls, each doing O(1) multiplication work.")
    print("Space Complexity: O(N) due to the call stack frames created for each number from N down to 1.")
