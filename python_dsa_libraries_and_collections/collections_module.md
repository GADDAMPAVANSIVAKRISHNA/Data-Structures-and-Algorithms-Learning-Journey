# 🧳 The `collections` Module

Python's built-in `collections` module provides specialized, high-performance container data types designed to solve complex data arrangement problems elegantly.

---

## 1. `deque` (Double-Ended Queue)
A `deque` (pronounced "deck") is a list-like container designed for **$O(1)$ appends and pops from both ends**. Lists are optimized for fast $O(1)$ operations at the right end but have $O(n)$ cost for left side insertion/deletion. Under the hood, `deque` is implemented as a doubly linked list of block arrays.

### 💡 Essential Operations & Syntax

```python
from collections import deque

# Initialization
q = deque([2, 3, 4])

# O(1) Right side operations
q.append(5)         # [2, 3, 4, 5]
val = q.pop()       # Returns 5 -> [2, 3, 4]

# O(1) Left side operations
q.appendleft(1)     # [1, 2, 3, 4]
val = q.popleft()   # Returns 1 -> [2, 3, 4]

# O(N) Rotating elements
q.rotate(1)         # Shift right by 1: [4, 2, 3]
q.rotate(-1)        # Shift left by 1: [2, 3, 4]

# Fixed size queue (automatically discards old elements)
bounded = deque(maxlen=3)
bounded.append(1)
bounded.append(2)
bounded.append(3)
bounded.append(4)   # '1' is automatically dropped from the left!
print(bounded)      # deque([2, 3, 4], maxlen=3)
```

### 🧠 DSA Use Cases
* **Breadth-First Search (BFS)**: Tracking visited nodes level by level using `popleft()` and `append()`.
* **Sliding Window**: Storing indices of elements in the current window to solve min/max window problems.

---

## 2. `Counter`
A `Counter` is a dictionary subclass for counting hashable objects. It is a **multiset** representation where elements are stored as dictionary keys and their counts are stored as values.

### 💡 Essential Operations & Syntax

```python
from collections import Counter

# Initialization
counts = Counter("abracadabra")
print(counts)  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# Get frequency (returns 0 if not found, never raises KeyError)
print(counts["z"])  # 0

# Retrieve top K elements by frequency
# O(N log K) time complexity
top_two = counts.most_common(2)
print(top_two)  # [('a', 5), ('b', 2)]

# Arithmetic operations between Counters
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(c1 + c2)  # Counter({'a': 4, 'b': 3})
print(c1 - c2)  # Counter({'a': 2})  # Subtract counts, keeps positive values
```

---

## 3. `defaultdict`
A `defaultdict` is a dictionary subclass that calls a factory function (like `int`, `list`, `set`) to supply a **default value** when a missing key is accessed. This avoids messy `if key not in dict` checks.

### 💡 Essential Operations & Syntax

```python
from collections import defaultdict

# 1. Grouping/Graphs using defaultdict(list)
adj_list = defaultdict(list)
adj_list["A"].append("B")  # Automatically initializes empty list for "A" first!
adj_list["A"].append("C")
print(adj_list)  # defaultdict(<class 'list'>, {'A': ['B', 'C']})

# 2. Count mappings using defaultdict(int)
char_count = defaultdict(int)
for char in "hello":
    char_count[char] += 1  # No KeyError! Initializes to 0, then adds 1
```

---

## 4. `OrderedDict`
An `OrderedDict` is a dictionary subclass that remembers the order in which keys were first inserted. While standard `dict` also preserves order in modern Python (3.7+), `OrderedDict` has unique features and algorithms.

### 💡 Essential Operations & Syntax

```python
from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

# Move a key to the end or beginning
od.move_to_end('a', last=True)   # Move 'a' to the very end
od.move_to_end('c', last=False)  # Move 'c' to the very beginning (left)

# LIFO / FIFO popping
last_item = od.popitem(last=True)   # Pops from right end (LIFO)
first_item = od.popitem(last=False) # Pops from left end (FIFO)
```

### 🧠 DSA Use Cases
* **LRU Cache (Least Recently Used Cache)**: Quickly moving items to the end when read/written, and popping from the left when full.

---

## 5. `namedtuple`
`namedtuple` returns a new tuple subclass with named fields, allowing you to access fields by name (like an object attribute) as well as index.

### 💡 Essential Operations & Syntax

```python
from collections import namedtuple

# Define the structure
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p = Point(11, y=22)

# Access by index or by name
print(p[0] + p[1])  # 33 (tuple index)
print(p.x, p.y)     # 11 22 (readable attributes)
```
