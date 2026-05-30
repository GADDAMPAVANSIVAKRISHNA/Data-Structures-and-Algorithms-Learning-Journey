# While Loops in Python

## Concept

A `while` loop keeps running while a condition is true.

- Use it when you do not know the exact number of repetitions ahead of time.
- The loop checks the condition before each iteration.
- The loop must eventually make the condition false.

## Examples

### 1. Count from 1 to 5

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

### 2. Ask until correct input

```python
password = ""
while password != "python123":
    password = input("Enter password: ")
print("Access granted")
```

### 3. Use `break` inside a loop

```python
count = 0
while True:
    count += 1
    if count == 3:
        break
    print(count)
```

## Practice Questions

1. Use `while` to print numbers 1 through 3.
2. Ask the user to type "yes" until they do it.
3. Loop until a number entered by the user becomes negative.
