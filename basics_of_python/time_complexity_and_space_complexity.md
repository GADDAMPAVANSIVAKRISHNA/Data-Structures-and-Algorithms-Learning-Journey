# Time Complexity and Space Complexity

## Concept

Time complexity measures how fast code runs as input grows.
Space complexity measures how much extra memory a program uses.

- Big O notation describes the growth rate.
- `O(1)` means constant work or memory.
- `O(n)` means work or memory grows with input size.

## Examples

### 1. Constant time `O(1)`

```python
def first_element(items):
    return items[0]
```

### 2. Linear time `O(n)`

```python
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
```

### 3. Quadratic time `O(n^2)`

```python
def print_pairs(numbers):
    for i in numbers:
        for j in numbers:
            print(i, j)
```

### 4. Linear space `O(n)`

```python
def copy_list(numbers):
    result = []
    for num in numbers:
        result.append(num)
    return result
```

## Practice Questions

1. What is the time complexity of reading all items in a list?
2. Write a function that returns the first item from a list and name its time complexity.
3. Is building a new list from an old list `O(n)` time or `O(n^2)` time? Explain.
