# Bubble Sort

## Definition

Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent items, and swaps them if they are in the wrong order. It continues until no swaps are required.

## Rules

- Compare each pair of adjacent elements.
- Swap them if the first element is greater than the second.
- After each pass, the largest unsorted element "bubbles" to the end.
- Continue until the list is sorted.

## Brute Force Approach

The brute force method is the classic bubble sort itself: repeatedly scan the array and swap any adjacent out-of-order pairs.

1. Iterate through the array.
2. Compare adjacent elements.
3. Swap when the left element is larger than the right.
4. Repeat passes until no swaps occur.

## Optimal Approach

An optimized bubble sort stops early when a pass makes no swaps. This saves time when the array is already sorted or nearly sorted.

### Example

Input: [4, 3, 1, 5, 2]

- Pass 1: [3, 1, 4, 2, 5]
- Pass 2: [1, 3, 2, 4, 5]
- Pass 3: [1, 2, 3, 4, 5]

## Time Complexity

- Best case: O(n) with early stop optimization
- Average case: O(n²)
- Worst case: O(n²)

## Space Complexity

- Space: O(1) (in-place)
- Additional storage: constant extra space.

## Practice Questions

### Brute Force Examples

1. Question: After one pass of brute force bubble sort on [4, 1, 3, 2], what is the result?
   - Answer:

```python
arr = [4, 1, 3, 2]
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
print(arr)  # [1, 3, 2, 4]
```

2. Question: Why does brute force bubble sort take O(n²) time?
   - Answer:

```python
def bubble_sort(arr):
    n = len(arr)
    for _ in range(n):
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
```

This keeps scanning the list on each pass and does O(n²) comparisons.

### Optimal Approach Examples

1. Question: How does the optimized bubble sort avoid extra passes on [1, 2, 3, 4]?
   - Answer:

```python
def bubble_sort_optimized(arr):
    n = len(arr)
    for _ in range(n):
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
arr = [1, 2, 3, 4]
bubble_sort_optimized(arr)
print(arr)  # [1, 2, 3, 4]
```

2. Question: What indicates that bubble sort can stop early in the optimized version?
   - Answer:

```python
if not swapped:
    break
```

If the inner loop finds no swaps, the array is sorted and the algorithm stops.
