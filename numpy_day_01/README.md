# Day 1: Array Creation in NumPy

Today covers the absolute fundamentals of initializing arrays in NumPy. Python lists are slow because they store pointers to objects scattered in memory. NumPy arrays (`ndarrays`) store data in contiguous memory blocks, making numerical operations incredibly fast.

## Concepts Covered

### 1. Converting Lists to Arrays (`np.array`)
Converts standard Python iterables (lists, tuples) into fast NumPy arrays.
* **Syntax:** `np.array(object, dtype=None)`

### 2. Creating Placeholder Arrays (`np.zeros` & `np.ones`)
Allocates memory for a specific shape pre-filled with `0` or `1`. Highly useful for initializing weights in machine learning or placeholders in loops.
* **Syntax:** `np.zeros(shape)`, `np.ones(shape)`

### 3. Numerical Ranges (`np.arange`)
Generates evenly spaced values within a given interval. It is the NumPy equivalent of Python's built-in `range()`, but returns an array.
* **Syntax:** `np.arange(start, stop, step)`

---

## Code Preview & Real-World Analogy
Think of a Python list like a grocery bag containing random loose items. A NumPy array is a perfectly packed egg carton where every slot is identical, allowing you to count and move items instantly.

```python
import numpy as np

# Creating a 1D array from a list
data = [1, 2, 3]
arr = np.array(data)
```

---

## Daily Checklist
- [ ] Understand why NumPy arrays outperform Python lists.
- [ ] Create 1D and 2D arrays from scratch.
- [ ] Complete the practice problems in `exercises.py`.