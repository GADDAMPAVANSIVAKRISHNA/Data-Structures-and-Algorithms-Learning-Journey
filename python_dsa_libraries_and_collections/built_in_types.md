# 📦 Python Built-in Collections

Python offers four core built-in collections: **List**, **Tuple**, **Set**, and **Dictionary**. Understanding their internals, syntax, and time complexities is crucial for writing efficient DSA solutions.

---

## 1. Lists (`list`)
A Python list is a **dynamic array** (re-allocates memory when full). It maintains elements in a linear order and allows duplicate values.

### 💡 Essential Operations & Syntax

```python
# Initialization
arr = [10, 20, 30, 40, 50]

# O(1) Indexing & Modification
print(arr[0])      # 10
arr[1] = 25        # [10, 25, 30, 40, 50]

# O(1) Amortized Append & Pop
arr.append(60)     # [10, 25, 30, 40, 50, 60]
last = arr.pop()   # Removes and returns 60

# O(N) Insertion & Deletion at arbitrary positions
arr.insert(1, 99)  # Insert 99 at index 1 -> [10, 99, 25, 30, 40, 50]
arr.pop(2)         # Removes 25 (shifts rest) -> [10, 99, 30, 40, 50]

# O(K) Slicing (where K is slice size)
sub = arr[1:4]     # [99, 30, 40]

# O(N log N) Sorting
arr.sort()                  # In-place ascending
sorted_arr = sorted(arr)    # Returns new sorted list
arr.sort(reverse=True)      # In-place descending
```

### ⚠️ Common Pitfalls
* **Shallow Copies**: Writing `b = a` doesn't copy the list, it copies the reference. Changing `b` will change `a`. Use `b = a.copy()` or `b = a[:]` for a shallow copy.
* **Inserting at Start**: Doing `arr.insert(0, val)` takes $O(N)$ because every single element has to be shifted in memory. For stack/queue operations, use `collections.deque` instead.

---

## 2. Tuples (`tuple`)
A tuple is an **immutable sequence** of elements. Once initialized, its elements cannot be changed, added, or removed.

### 💡 Essential Operations & Syntax

```python
# Initialization
point = (3, 4)
empty = ()
single_element = (5,)  # Note the trailing comma!

# Packing and Unpacking
x, y = point
print(f"X: {x}, Y: {y}")  # X: 3, Y: 4

# Read-only access
print(point[0])  # 3
```

### 🧠 DSA Use Cases
* **Hash Keys**: Because tuples are immutable, they are **hashable** (if they contain hashable types). This makes them perfect to use as keys in a dictionary (e.g., coordinates in a 2D grid: `visited[(r, c)] = True`).

---

## 3. Sets (`set`)
A set is an **unordered collection** of unique elements. It is implemented internally using a **hash table**, enabling fast lookups.

### 💡 Essential Operations & Syntax

```python
# Initialization
s = {1, 2, 3, 3}  # s becomes {1, 2, 3} (duplicates removed)
empty_set = set() # Note: {} creates an empty dictionary, not a set!

# O(1) Insertion & Deletion
s.add(4)
s.remove(2)       # Raises KeyError if 2 not found
s.discard(99)     # Safe removal: doesn't raise error if key missing

# O(1) Membership test (Extremely fast compared to lists)
if 3 in s:
    print("Found!")

# O(Len(A) + Len(B)) Mathematical Set Operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))            # {1, 2, 3, 4, 5}  (or: a | b)
print(a.intersection(b))     # {3}              (or: a & b)
print(a.difference(b))       # {1, 2}           (or: a - b)
print(a.symmetric_difference(b)) # {1, 2, 4, 5} (or: a ^ b)
```

---

## 4. Dictionaries (`dict`)
A dictionary is an **unordered mapping of key-value pairs** (note: Python 3.7+ preserves key insertion order as an implementation detail). Like sets, it uses a **hash table** under the hood.

### 💡 Essential Operations & Syntax

```python
# Initialization
lookup = {"apple": 1, "banana": 2}

# O(1) Access, Insertion, and Deletion
lookup["cherry"] = 3         # Insert
print(lookup["apple"])       # Access -> 1
del lookup["banana"]         # Delete key "banana"

# Safe Access with default fallback
count = lookup.get("mango", 0)  # Returns 0 since "mango" is not present

# Iteration
for key in lookup:
    print(key)               # Loops through keys

for key, value in lookup.items():
    print(key, value)        # Loops through key-value pairs

for value in lookup.values():
    print(value)             # Loops through values
```

### 🚀 Dictionary Comprehension
A clean way to construct maps in a single line:
```python
squares = {x: x**2 for x in range(5)}
# Result: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```
