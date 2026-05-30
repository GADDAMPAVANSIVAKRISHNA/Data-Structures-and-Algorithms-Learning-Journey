# Lists, Tuples, and Strings in Python

## Concept

Python stores ordered data in lists, tuples, and strings.

- `list` can change its items.
- `tuple` cannot change after creation.
- `str` is text made of characters.

## Examples

### 1. Working with a list

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
fruits.append("date")
print(fruits)
```

### 2. Working with a string

```python
text = "Hello"
print(text[1])
print(text.upper())
print(text + " world")
```

### 3. Looping through items

```python
for fruit in fruits:
    print(fruit)

for char in text:
    print(char)
```

## Practice Questions

1. Create a list of three colors, then print the second color.
2. Ask the user for a word and print its length.
3. Make a tuple of three numbers and print the sum of those numbers.
