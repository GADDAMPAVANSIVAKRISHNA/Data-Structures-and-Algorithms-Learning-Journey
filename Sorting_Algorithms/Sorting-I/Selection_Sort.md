# Selection Sort

## Definition

Selection sort is a simple comparison-based sorting algorithm. It repeatedly selects the minimum element from the unsorted portion of the list and swaps it with the first unsorted element.

## Rules

- Work on the unsorted portion of the array.
- Find the smallest element in the unsorted region.
- Swap it with the first element in that unsorted region.
- Move the boundary between sorted and unsorted regions one step forward.

## Brute Force Approach

The brute force way to sort an array is to compare every pair of elements and move the smallest each time. Selection sort uses this idea directly:

1. For each position in the array, scan the remaining unsorted elements.
2. Find the smallest value.
3. Swap it into the current position.

## Optimal Approach

Selection sort itself is already the canonical approach for this algorithm. While it is not the fastest algorithm for large inputs, it is optimal for the algorithm design as a simple in-place, comparison-based method.

### Example

Input: [5, 2, 9, 1, 5]

- Pass 1: select 1, swap with 5 → [1, 2, 9, 5, 5]
- Pass 2: select 2, swap with 2 → [1, 2, 9, 5, 5]
- Pass 3: select 5, swap with 9 → [1, 2, 5, 9, 5]
- Pass 4: select 5, swap with 9 → [1, 2, 5, 5, 9]

## Time Complexity

- Best case: O(n²)
- Average case: O(n²)
- Worst case: O(n²)

## Space Complexity

- Space: O(1) (in-place)
- Additional storage: constant extra space for temporary swaps.

## Practice Questions

### Brute Force Examples

1. Question: Using selection sort on [6, 3, 8, 1], what is the array after the first two passes?
   - Answer:

```python
arr = [6, 3, 8, 1]
for i in range(2):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print(arr)  # [1, 3, 8, 6]
```

2. Question: Why is selection sort considered a brute force style algorithm?
   - Answer:

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

This code scans all remaining elements for each position, giving O(n²) comparisons.

### Optimal Approach Examples

1. Question: What happens if the input is already sorted for selection sort?
   - Answer:

```python
arr = [1, 2, 3, 4, 5]
selection_sort(arr)
print(arr)  # [1, 2, 3, 4, 5]
```

Selection sort still performs the same comparisons and keeps O(n²) time. 2. Question: How does selection sort minimize extra space compared to other sorts?

- Answer:

```python
arr = [5, 2, 4, 1]
# swap uses only constant extra space
i, j = 0, 3
arr[i], arr[j] = arr[j], arr[i]
```

Selection sort only uses one temporary swap, so it is O(1) extra space.
