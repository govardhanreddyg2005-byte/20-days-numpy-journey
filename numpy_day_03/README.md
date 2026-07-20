# Day 3: Indexing & Slicing

Today focuses on extracting exactly the data you need from 1D and 2D arrays. NumPy utilizes advanced slicing syntax that avoids creating unnecessary copies in memory, making data extraction incredibly fast.

## Concepts Covered

### 1. 1D Array Slicing
* Syntax: `array[start:stop:step]`
* Just like Python lists, the `stop` index is exclusive.

### 2. 2D Matrix Indexing
* Syntax: `matrix[row_index, column_index]`
* Use a comma to separate row operations from column operations.

### 3. Strides (Skipping Steps)
* Using the third argument (`step`) lets you skip elements or reverse arrays efficiently.