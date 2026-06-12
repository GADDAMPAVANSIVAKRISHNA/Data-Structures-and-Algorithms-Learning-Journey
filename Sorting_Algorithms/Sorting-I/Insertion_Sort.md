# Insertion Sort

## Definition

Insertion sort builds the sorted array one element at a time. It takes each element and inserts it into the correct position among the already sorted elements to its left.

## Rules

- Start with the first element as a sorted subarray.
- Take the next element and compare it with sorted elements.
- Shift larger sorted elements one position to the right.
- Insert the current element into the correct sorted location.

## Brute Force Approach

A brute force approach is to compare the current element with each element in the sorted left side and shift elements until the correct spot is found.

1. For each index from 1 to n-1, store the current value.
2. Compare with earlier elements and shift greater values right.
3. Insert the element at the correct position.

## Optimal Approach

Insertion sort is already an optimal algorithm for small or nearly sorted inputs. The algorithm can be considered optimal for its problem class because it minimizes movement while maintaining in-place sorting.

### Example

Input: [3, 1, 4, 2]

- Step 1: insert 1 before 3 → [1, 3, 4, 2]
- Step 2: 4 stays → [1, 3, 4, 2]
- Step 3: insert 2 between 1 and 3 → [1, 2, 3, 4]

## Time Complexity

- Best case: O(n) when input is already sorted
- Average case: O(n²)
- Worst case: O(n²)

## Space Complexity

- Space: O(1) (in-place)
- Additional storage: constant extra space for the key element.

## Practice Questions

### Brute Force Examples

1. Question: Show the first two insertion steps for [3, 1, 4, 2].
   - Answer:

```python
arr = [3, 1, 4, 2]
for i in range(1, 3):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
    print(arr)
# [1, 3, 4, 2]
# [1, 3, 4, 2]
```

2. Question: Why is insertion sort considered brute force for unsorted data?
   - Answer:

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
```

The nested loop and shifts give O(n²) behavior on unsorted data.

### Optimal Approach Examples

1. Question: What is the behavior of insertion sort on [1, 2, 3, 4]?
   - Answer:

```python
arr = [1, 2, 3, 4]
insertion_sort(arr)
print(arr)  # [1, 2, 3, 4]
```

It only makes one comparison per element and runs in O(n). 2. Question: When is insertion sort a good optimal choice?

- Answer:

```python
arr = [1, 2, 4, 3, 5]
insertion_sort(arr)
```

When the array is nearly sorted, only a few shifts are needed, making it efficient.
