# Day 4: Data Types (`dtype` & Casting)

NumPy arrays are homogeneous, meaning every element must share the same data type. Controlling memory through data types is vital when handling large datasets.

## Concepts Covered

### 1. Forcing Types with `dtype`
* You can define data types during array creation using the `dtype` parameter (e.g., `np.int32`, `np.float64`, `np.bool_`).

### 2. Type Casting with `.astype()`
* Arrays cannot be changed in place. To change an array's type, you must cast it into a brand-new array using the `.astype()` method.

