"""
Day 5: Broadcasting Arrays and Mathematical Operations Demonstrations.
"""

import numpy as np

# Performing Addition an array A with B they are compatible.
A = np.array([1,2,3,4])
B = 2

print(A + B)

# Performing Multiplication on two array observe the result how numpy multiply every element.

A = np.array([2,4,6,8])
B = np.array([1,3,6,7])

print(A * B)

# Adding two arrays where arrays and performing broadcasting operations.
A = np.array([1,2,3,4])
B = np.array([
    [10],
    [20],
    [30],
    [40]
    ])

print(A + B)

# Performing broadcasting Mathematical operations on two non compatible arrays.

A = np.arange(8).reshape(2,4)[:, np.newaxis]

B = np.arange(12).reshape(3,4)[np.newaxis, :]

#print(A - B) # raises Value error operands not broadcastable with shape (2,4) and (3,4). 
# Explanation Checkout Markdown file at Line 38 to 42.

print(A - B)
