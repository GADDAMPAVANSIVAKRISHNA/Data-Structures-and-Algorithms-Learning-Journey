# `switch` / `match` in Python

## Concept

Python uses `match` or `if`/`elif` to choose one action from many possibilities.

- `match` is a clear way to test many values.
- Before Python 3.10, use `if` / `elif` chains.
- Dictionaries can also map values to actions.

## Examples

### 1. `match` statement

```python
command = input("Enter command (start, stop, pause): ")

match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
    case "pause":
        print("Pausing")
    case _:
        print("Unknown command")
```

### 2. `if` / `elif` chain

```python
command = input("Enter command: ")
if command == "start":
    print("Starting")
elif command == "stop":
    print("Stopping")
elif command == "pause":
    print("Pausing")
else:
    print("Unknown command")
```

### 3. Dictionary mapping

```python
actions = {
    "start": lambda: print("Starting"),
    "stop": lambda: print("Stopping"),
    "pause": lambda: print("Pausing"),
}

command = input("Enter command: ")
actions.get(command, lambda: print("Unknown command"))()
```

## Practice Questions

1. Read a day name and print whether it is a weekday or weekend.
2. Use `match` or `if`/`elif` to print the number of letters in a color name when the color is red, green, or blue.
3. Map three commands to different greetings and print a default message for other input.
