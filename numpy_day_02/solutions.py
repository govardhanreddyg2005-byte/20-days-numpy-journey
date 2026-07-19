"""
Day 2 Solutions: Reference answers for the exercises.
"""

import numpy as np

print("--- Solution 1 ---\n")

arr = np.array([[1,3,4],[3,6,7],[2,4,8]])

print(f"Shape: {arr.shape}\n")

print("--- Solution 2 ---\n")

arr = np.array([[1,3,4],[3,6,7],[2,4,8]])

print(f"Size: {arr.size}\n")

print("--- Solution 3 ---\n")

arr = np.array([[1,3,4],[3,6,7],[2,4,8]])

print(f"dimensions: {arr.ndim}\n")

print("--- Solution 3 ---\n")

final_array = np.array([[1,2,3],[5,6,7]])

arr_shape = final_array.shape
arr_size = final_array.size
arr_dim = final_array.ndim
arr_bytes = final_array.nbytes

print(arr_shape)
print(arr_size)
print(arr_dim)
print(arr_bytes)
