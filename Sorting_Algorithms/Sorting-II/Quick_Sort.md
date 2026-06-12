# Quick Sort

## Definition

Quick sort is a divide-and-conquer sorting algorithm that selects a pivot element and partitions the array into elements less than the pivot and elements greater than the pivot. It then sorts the partitions recursively.

## Rules

- Choose a pivot element from the array.
- Partition the array so elements less than the pivot come before it and elements greater come after.
- Recursively quick sort the left partition and right partition.
- Combine the sorted partitions and pivot.

## Brute Force Approach

A brute force alternative is a simple O(n²) sort such as bubble sort or insertion sort. Quick sort improves on that with partitioning and recursive division.

## Optimal Approach

Quick sort is optimal on average for comparison sorting, using partitioning and recursion. Choosing a good pivot (random or median-of-three) helps achieve O(n log n) average performance.

### Example

Input: [8, 4, 2, 9, 5]

- Choose pivot 5
- Partition: [4, 2] pivot [5] [8, 9]
- Sort left → [2, 4]
- Sort right → [8, 9]
- Result: [2, 4, 5, 8, 9]

## Time Complexity

- Best case: O(n log n)
- Average case: O(n log n)
- Worst case: O(n²) if pivot selection is poor

## Space Complexity

- Space: O(log n) on average due to recursion stack
- Worst-case space: O(n) if recursion is unbalanced

## Practice Questions

### Brute Force Examples

1. Question: What is the brute force alternative to quick sort for [8, 4, 2, 9, 5]?
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

arr = [8, 4, 2, 9, 5]
insertion_sort(arr)
print(arr)  # [2, 4, 5, 8, 9]
```

2. Question: Why is quick sort better than brute force sorts for large arrays?
   - Answer:

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

print(quick_sort([8, 4, 2, 9, 5]))
```

Quick sort usually splits the array and uses recursion, giving O(n log n) average time.

### Optimal Approach Examples

1. Question: How does choosing a good pivot affect quick sort?
   - Answer:

```python
def median_of_three(arr, low, high):
    mid = (low + high) // 2
    candidates = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
    return sorted(candidates)[1][1]
```

A good pivot helps keep partitions balanced. 2. Question: What happens when quick sort receives a nearly sorted array and uses a median-of-three pivot?

- Answer:

```python
def quick_sort_median(arr):
    if len(arr) <= 1:
        return arr
    pivot = sorted([arr[0], arr[len(arr)//2], arr[-1]])[1]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort_median(left) + mid + quick_sort_median(right)

print(quick_sort_median([1, 2, 3, 4, 5]))
```

Using a better pivot keeps performance near O(n log n).
