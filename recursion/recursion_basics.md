# 🔄 Recursion Basics

**Recursion** is a programming technique where a function **calls itself** to solve smaller instances of the same problem. It breaks a complex problem down into simpler, manageable sub-problems.

---

## 🏗️ Structure of a Recursive Function

Every recursive function must contain two crucial components:

1. **Base Case(s)**:
   * The condition under which the function stops calling itself.
   * Without a base case, recursion will continue infinitely, leading to a **Stack Overflow**.
2. **Recursive Step / Relation**:
   * The part where the function calls itself with a modified (usually smaller) input, moving closer to the base case.

### 📝 Basic Template:
```python
def recursive_function(parameters):
    # 1. Base Case
    if condition_to_stop:
        return base_value
    
    # 2. Recursive Step
    new_parameters = modify_input(parameters)
    return recursive_function(new_parameters)
```

---

## 🧠 The Execution Call Stack

When a function is called, the operating system allocates a block of memory called a **stack frame** on the **Call Stack**. This frame stores local variables and parameters.

* In recursion, each self-call adds a new stack frame on top of the stack.
* These frames remain active until the base case is reached.
* Once the basecase returns, the stack frames are popped one by one in **LIFO (Last In, First Out)** order, propagating the result back.

```text
Call Stack Execution (e.g. Factorial(3)):

   Call phase (Pushing):             Return phase (Popping):
┌─────────────────────────┐       ┌─────────────────────────┐
│  factorial(1) -> returns 1      │  [Popped]               │
├─────────────────────────┤       ├─────────────────────────┤
│  factorial(2) -> waiting│       │  factorial(2) -> returns 2 * 1 = 2
├─────────────────────────┤       ├─────────────────────────┤
│  factorial(3) -> waiting│       │  factorial(3) -> returns 3 * 2 = 6
└─────────────────────────┘       └─────────────────────────┘
```

---

## ⚠️ Stack Overflow
If the recursion goes too deep (e.g., missing base case or too large inputs), the call stack runs out of memory. In Python, this raises a `RecursionError: maximum recursion depth exceeded`.
* Default recursion limit in Python is usually `1000`. It can be checked or changed using:
  ```python
  import sys
  sys.setrecursionlimit(2000)
  ```

---

## 📈 Analyzing Time and Space Complexity

### 1. Time Complexity
Can be analyzed using **Recurrence Relations** or **Recursion Trees**:
* **Linear Recursion** (e.g., Factorial): Each call spawns one child. For $N$ calls, Time complexity = $O(N)$.
* **Tree Recursion** (e.g., Fibonacci): Each call spawns multiple calls (like 2). The recursion tree branches exponentially. For Fibonacci, Time complexity = $O(2^N)$ because the number of calls doubles at each level.

### 2. Space Complexity
Even if no extra structures are created, recursion consumes memory on the call stack.
* **Auxiliary Space Complexity** = **Maximum Depth of the Recursion Tree** (height of the tree).
* For linear recursion of depth $N$, Space complexity = $O(N)$.
* For Fibonacci of depth $N$, Space complexity = $O(N)$ (not $O(2^N)$), because stack frames are popped as soon as a branch finishes, so the maximum frames active at any instant is equal to the height of the tree.
