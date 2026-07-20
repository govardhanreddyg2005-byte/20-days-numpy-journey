"""
Day 3: Indexing & Slicing Demonstrations
"""
import numpy as np

print("--- 1D Slicing & Strides ---")
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(f"Original: {arr}")
print(f"Slice (indices 2 to 5): {arr[2:6]}")
print(f"Every second element: {arr[::2]}")
print(f"Reverse array: {arr[::-1]}\n")


print("--- 2D Indexing & Slicing ---")
matrix = np.array([
    [7, 8, 9],
    [10,12,13],
    [14,16,17]
     
])

print(f"Specific Element (Row 1, Col 2): {matrix[1, 2]}") # Outputs 6
print(f"First Row: {matrix[0, :]}")
print(f"Last Column:\n{matrix[:, -1]}")
print(f"2x2 Sub-grid from top-left:\n{matrix[:2, :2]}")

