# 🔑 Hashing Basics

**Hashing** is a technique used to uniquely identify an object from a group of similar objects. In computer science, it maps keys to specific values using a mathematical function known as a **Hash Function**. It is the underlying mechanism behind Python's `set` and `dict`.

---

## 🏗️ How a Hash Table Works

A **Hash Table** (or Hash Map) uses an array to store key-value pairs. 
1. The **Key** is passed into a **Hash Function**.
2. The function outputs an integer index within the array range:
   $$\text{index} = \text{hash}(key) \pmod{\text{array\_size}}$$
3. The key-value pair is stored at that index.

```text
Key (String)          Hash Function             Index            Array / Buckets
┌─────────┐          ┌─────────────┐          ┌───────┐         ┌───────────────┐
│ "apple" │  ───>    │  h("apple") │  ───>    │   2   │  ───>   │ 0:            │
└─────────┘          └─────────────┘          └───────┘         │ 1:            │
                                                                │ 2: ("apple",1)│
                                                                │ 3:            │
                                                                └───────────────┘
```

---

## 💥 Collisions and Resolution Strategies

A **Collision** occurs when two distinct keys hash to the exact same index. Since array slots are finite, collisions are inevitable (by the *Pigeonhole Principle*).

There are two primary ways to resolve collisions:

### 1. Separate Chaining (Open Hashing)
Each slot of the hash table array contains a pointer to a **Linked List** (or chain) of entries that hash to the same slot.
* **Insertion**: Append the new key-value pair to the linked list at `array[index]`.
* **Search**: Compute the index, then linearly traverse the linked list to find the key.
* **Worst Case**: If all elements hash to the same index, search degrades to $O(N)$.

### 2. Open Addressing (Closed Hashing)
All entry elements are stored directly in the array itself. When a collision occurs, we probe (search) for the next empty slot in the array.
* **Linear Probing**: Look at index $i+1, i+2, i+3 \dots$ sequentially. (Prone to clustering).
* **Quadratic Probing**: Look at index $i+1^2, i+2^2, i+3^2 \dots$.
* **Double Hashing**: Look at index $i + k \cdot \text{hash}_2(\text{key})$.

---

## 📈 Load Factor ($\alpha$) & Rehashing

The **Load Factor ($\alpha$)** measures how full a hash table is:
$$\alpha = \frac{\text{Number of elements stored } (N)}{\text{Size of the table array } (M)}$$

* If $\alpha$ becomes too high (typically $> 0.7$), lookups become slow because of frequent collisions.
* **Rehashing**: To maintain $O(1)$ operations, the table dynamically doubles its array size, recalculates the hash indices for all existing elements, and inserts them into the new, larger array.

---

## 🚀 Time Complexities

| Operation | Average Case | Worst Case | Notes |
| :--- | :--- | :--- | :--- |
| **Insertion** | $O(1)$ | $O(N)$ / $O(1)$ amortized | $O(N)$ occurs during rehashing or extreme collisions. |
| **Deletion** | $O(1)$ | $O(N)$ | Requires locating the key first. |
| **Search / Lookup**| $O(1)$ | $O(N)$ | Collision storms degrade lookup to linear search. |
