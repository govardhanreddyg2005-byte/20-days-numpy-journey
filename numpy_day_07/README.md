# Day 10: Extremas & Sorting

Locating maximum or minimum values and ordering data are fundamental operations in data processing. NumPy offers built-in tools to find values, track their exact positions, and sort structures efficiently.

## Concepts Covered

### 1. Value Locating Functions
* `np.min()`: Returns the lowest value found in an array or along a specific axis.
* `np.max()`: Returns the highest value found in an array or along a specific axis.

### 2. Index Tracking Functions (`arg` Functions)
* `np.argmin()`: Finds and returns the index position of the minimum value instead of the value itself.
* `np.argmax()`: Finds and returns the index position of the maximum value instead of the value itself.

### 3. Sorting Arrays
* `np.sort()`: Rearranges elements into ascending order and outputs a fresh, sorted copy of the array without altering the original variable.
* `np.argsort()`: Returns the integer indices that would sort the array, allowing you to track how the items moved during ordering.

