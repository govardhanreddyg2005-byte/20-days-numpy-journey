"""
Day 1: Array Creation Basics 
This script demonstrates how to initializes a array using NumPy functions.
"""

import numpy as np

# Convert a Python list into a NumPy array using np.array().

my_list = [10, 20, 30, 40, 50]

array = np.array(my_list)
print(f"Array from my_list: {array}\n")

# Create an 2D array of zeros using np.zeros().

arr_zeros = np.zeros((2,3), dtype=int)
print(f"2D Zeros:\n {arr_zeros}\n")

# Create an 2D array of ones using np.ones().

arr_ones = np.ones((2,3), dtype=int)
print(f"1D Ones:\n {arr_ones}\n")

# Create an array of range N using np.arange(n).

sequences = np.arange(1,10)
print(f"Sequences of array: {sequences}\n")

