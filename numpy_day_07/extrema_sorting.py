"""
Day 10: Extremas & Sorting
Concept: Finding values, tracking indices, and sorting arrays using NumPy.
"""

import numpy as np

# Create an unsorted test array
numbers = np.array([15, 42, 8, 23, 42, 4])
print("Original Array:", numbers)

# 1. Finding Values vs. Finding Indices
min_val = np.min(numbers)
max_val = np.max(numbers)
print(f"Minimum Value: {min_val} | Maximum Value: {max_val}")

min_idx = np.argmin(numbers)
max_idx = np.argmax(numbers)
print(f"Index of Min: {min_idx} (Value is {numbers[min_idx]})")
print(f"Index of Max: {max_idx} (Value is {numbers[max_idx]})")
print("-" * 50)

# 2. Sorting Arrays
sorted_numbers = np.sort(numbers)
print("Sorted Array (Ascending):", sorted_numbers)

# 3. Tracking Sort Order with argsort
# This tells you which index from the original array belongs in each sorted slot
sort_indices = np.argsort(numbers)
print("Indices that would sort the array:", sort_indices)
print("-" * 50)

# 4. Multi-dimensional Matrix Operations
matrix = np.array([
    [10,4,6],
    [2,9,3],
    [5,12,1]
])
print("Matrix:\n", matrix)

# Using axis=1 shifts the operation horizontally across columns (evaluates each row)
print("Max value in each row:", np.max(matrix, axis=1))
print("Index of max value in each row:", np.argmax(matrix, axis=1))
