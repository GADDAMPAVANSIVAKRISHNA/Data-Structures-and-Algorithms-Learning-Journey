# For Loops in Python

## Concept

A `for` loop runs a block of code once for each item in a sequence.

- Use it when you want to process every item in a list, string, or range.
- The loop variable gets each value in turn.
- The number of steps is usually known from the sequence.

## Examples

### 1. Loop through a list

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
```

### 2. Loop through a string

```python
word = "Python"
for letter in word:
    print(letter)
```

### 3. Loop with `range()`

```python
for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)
```

## Practice Questions

1. Print each item in the list `['cat', 'dog', 'bird']`.
2. Use `range(2, 7)` to print numbers from 2 to 6.
3. Ask the user for a word and print each character on a new line.
