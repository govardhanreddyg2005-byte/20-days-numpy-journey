"""
Day 5 Exercises: Test your math and broadcasting skills!
"""

import numpy as np

# Exercise 1: You have prices in USD. Convert them all to EUR by multiplying 
# the array by the exchange rate scalar (e.g., 0.92) using broadcasting.
usd_prices = np.array([10.0, 25.5, 100.0, 5.99])
# Your code here:


# Exercise 2: Given a 3x3 matrix, use broadcasting to subtract the 
# mean values array from each corresponding column. 
# (This is a common feature scaling technique in Machine Learning).
data_matrix = np.array([
    [10,20,30],
    [40,50,60],
    [70, 80, 90]
])
column_means = np.array([40, 50, 60])
# Your code here:


# Exercise 3: Try to add these two arrays. Will it work? 
# If it fails, explain why based on broadcasting rules in a comment.
x = np.array([[1, 2], [3, 4]]) # Shape (2, 2)
y = np.array([1, 2, 3])        # Shape (3,)
# Your code here: