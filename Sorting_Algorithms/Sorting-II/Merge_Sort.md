# Merge Sort

## Definition

Merge sort is a divide-and-conquer sorting algorithm. It splits the list into smaller sublists, sorts each sublist, and merges the sorted sublists to produce the final sorted list.

## Rules

- Divide the input array into two halves.
- Recursively sort each half.
- Merge the two sorted halves into one sorted array.

## Brute Force Approach

A brute force alternative is to use a simple O(n²) comparison-based sort such as bubble sort or insertion sort on the whole list. Merge sort improves on that by dividing the problem.

## Optimal Approach

Merge sort is the optimal divide-and-conquer approach for comparison sorting with guaranteed O(n log n) time.

### Example

Input: [7, 2, 6, 3]

- Split into [7, 2] and [6, 3]
- Sort left: [2, 7]
- Sort right: [3, 6]
- Merge: [2, 3, 6, 7]

## Time Complexity

- Best case: O(n log n)
- Average case: O(n log n)
- Worst case: O(n log n)

## Space Complexity

- Space: O(n) due to temporary arrays used during merging.
- Additional storage: extra array of size proportional to the input.

## Practice Questions

### Brute Force Examples

1. Question: Why is using bubble sort or insertion sort on a large list considered brute force compared to merge sort?
   - Answer:

```python
def bubble_sort(arr):
    n = len(arr)
    for _ in range(n):
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
```

This brute force method requires O(n²) time, unlike merge sort's O(n log n). 2. Question: For [7, 2, 6, 3], what are the two halves after the first split?

- Answer:

```python
arr = [7, 2, 6, 3]
left = arr[:len(arr)//2]
right = arr[len(arr)//2:]
print(left, right)  # [7, 2] [6, 3]
```

### Optimal Approach Examples

1. Question: How does merge sort combine sorted halves of [2, 7] and [3, 6]?
   - Answer:

```python
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
print(merge([2, 7], [3, 6]))  # [2, 3, 6, 7]
```

2. Question: Why is merge sort considered optimal for comparison-based sorting?
   - Answer:

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
```

This recursive divide-and-conquer approach guarantees O(n log n) time.
