# Recursive Bubble Sort

## Definition

Recursive bubble sort is a recursive version of bubble sort. It uses the same comparison and swapping logic but reduces the problem size by handling one fewer element in each recursive call.

## Rules

- Compare adjacent elements and swap if needed.
- After one pass, the largest value moves to the end.
- Recursively sort the remaining first n-1 elements.

## Brute Force Approach

The brute force approach is the iterative bubble sort. It repeatedly scans and swaps adjacent elements until the array is sorted.

## Optimal Approach

Using recursion does not improve the time complexity, but it is an alternate way to express bubble sort. The optimal improvement in bubble sort comes from early stopping when no swaps occur during a pass.

### Example

Input: [4, 2, 1, 3]

- Pass 1: [2, 1, 3, 4]
- Recurse into [2, 1, 3]
- Pass 2: [1, 2, 3, 4]
- Recurse into [1, 2]

## Time Complexity

- Best case: O(n²) without early stop
- Average case: O(n²)
- Worst case: O(n²)

## Space Complexity

- Space: O(n) due to recursion stack
- Additional storage: constant extra space for swapping.

## Practice Questions

### Brute Force Examples

1. Question: What is the output after the first recursive bubble sort pass on [4, 2, 1, 3]?
   - Answer:

```python
arr = [4, 2, 1, 3]
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
print(arr)  # [2, 1, 3, 4]
```

2. Question: Why does recursive bubble sort still follow O(n²) time?
   - Answer:

```python
def recursive_bubble(arr, n):
    if n == 1:
        return
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    recursive_bubble(arr, n - 1)
```

Each recursive call still makes a full pass over the list.

### Optimal Approach Examples

1. Question: Can recursive bubble sort stop early like iterative bubble sort?
   - Answer:

```python
def recursive_bubble_opt(arr, n):
    if n == 1:
        return
    swapped = False
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True
    if not swapped:
        return
    recursive_bubble_opt(arr, n - 1)
```

2. Question: How does recursion change the space complexity for bubble sort?
   - Answer:

```python
# Recursion adds stack frames for each call
recursive_bubble_opt([4, 2, 1, 3], 4)
```

The recursion stack can use O(n) space.
