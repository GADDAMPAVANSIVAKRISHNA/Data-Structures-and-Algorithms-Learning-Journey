# `if`, `elif`, `else` in Python

## Concept

Use `if`, `elif`, and `else` to make decisions in your code.

- `if` checks the first condition.
- `elif` checks another condition if the first is false.
- `else` runs when no condition is true.

## Examples

### 1. Positive, negative, or zero

```python
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number == 0:
    print("Zero")
else:
    print("Negative")
```

### 2. Grade by score

```python
score = 85
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Needs improvement")
```

### 3. Multiple checks with `and` / `or`

```python
age = 20
if age >= 18 and age < 65:
    print("Adult")
else:
    print("Not an adult")
```

## Practice Questions

1. Read a number and print "Even" or "Odd".
2. Ask for a temperature and print "Cold" if below 15, else "Warm".
3. Read two numbers and print the larger one.
