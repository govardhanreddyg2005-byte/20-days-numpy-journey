"""
Day 2: Checking Array Attributes using .shape, .ndim, .size, .dtype. 
This Script Shows the properties of an NumPy array.
"""

import numpy as np

# Create the following NumPy array and print its shape(.shape).

arr = np.array([[10, 20],[30, 40],[50, 60]])

arr_shape = arr.shape

print(f"Array Shape: {arr_shape}\n")

# Create the following NumPy array and print the number of dimensions(.ndim).

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

arr_dim = arr.ndim

print(f"Array dimensions: {arr_dim}\n")

# Create the following NumPy array and print its datatype and print total number of elements.

arr = np.array([5,6,7,8,9])

dtype = arr.dtype
arr_size = arr.size

print(f"Array type: {dtype}")
print(f"Array size: {arr_size}")

