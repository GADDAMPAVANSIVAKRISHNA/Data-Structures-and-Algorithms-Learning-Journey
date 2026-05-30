# Functions in Python

## Concept

A function is a named block of code that does one task and can be reused.

- Define a function with `def` and call it by name.
- Functions can take inputs (arguments) and return values.
- Mutable objects passed into functions can be changed inside them.

## Examples

### 1. Simple function

```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)
```

### 2. Function with a list

```python
def modify_list(lst):
    lst.append(4)

numbers = [1, 2, 3]
modify_list(numbers)
print(numbers)  # [1, 2, 3, 4]
```

### 3. Function with an integer

```python
def modify_number(x):
    x += 5
    return x

value = 10
new_value = modify_number(value)
print(value)
print(new_value)
```

## Practice Questions

1. Write a function that returns the square of a number.
2. Create a function that takes a list and returns its length.
3. Write a function that prints "Hello" followed by a name.
