# Recursive Insertion Sort

## Definition

Recursive insertion sort is a recursive version of insertion sort. It inserts the last element into its correct position in the already sorted prefix by recursively sorting the prefix first.

## Rules

- Base case: a list of size 0 or 1 is already sorted.
- Recursively sort the first n-1 elements.
- Insert the nth element into the correct position among the sorted prefix.

## Brute Force Approach

The brute force version is the iterative insertion sort, which shifts elements and inserts the current element into the sorted portion.

## Optimal Approach

The recursive version is mainly a conceptual variant. The algorithm still uses the same insertion logic and time complexity. It highlights divide-and-conquer thinking while preserving the in-place insertion strategy.

### Example

Input: [3, 1, 4, 2]

- Recursively sort [3, 1, 4] → [1, 3, 4]
- Insert 2 into [1, 3, 4] → [1, 2, 3, 4]

## Time Complexity

- Best case: O(n) when input is already sorted
- Average case: O(n²)
- Worst case: O(n²)

## Space Complexity

- Space: O(n) due to recursion stack
- Additional storage: constant extra space for element insertion.

## Practice Questions

### Brute Force Examples

1. Question: How does recursive insertion sort sort [3, 1, 4, 2]?
   - Answer:

```python
def recursive_insertion_sort(arr, n):
    if n <= 1:
        return
    recursive_insertion_sort(arr, n - 1)
    last = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last

arr = [3, 1, 4, 2]
recursive_insertion_sort(arr, len(arr))
print(arr)  # [1, 2, 3, 4]
```

2. Question: Why is recursive insertion sort still O(n²) in the average case?
   - Answer:

```python
def recursive_insertion_sort(arr, n):
    if n <= 1:
        return
    recursive_insertion_sort(arr, n - 1)
    # insertion step may shift up to n elements
```

The recursion does not reduce the total number of shifts or comparisons.

### Optimal Approach Examples

1. Question: When does recursive insertion sort perform best?
   - Answer:

```python
arr = [1, 2, 3, 4, 5]
recursive_insertion_sort(arr, len(arr))
print(arr)  # [1, 2, 3, 4, 5]
```

Nearly sorted input means very few shifts and O(n) time. 2. Question: What is the main benefit of the recursive version of insertion sort?

- Answer:

```python
def recursive_insertion_sort(arr, n):
    if n <= 1:
        return
    recursive_insertion_sort(arr, n - 1)
    # then insert the nth element
```

It shows recursion over a smaller prefix, while preserving insertion behavior.
