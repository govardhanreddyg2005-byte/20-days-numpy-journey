"""
Day 5 Solutions
"""

import numpy as np

print("--- Solution 1 ---")
usd_prices = np.array([10.0, 25.5, 100.0, 5.99])
exchange_rate = 0.92
eur_prices = usd_prices * exchange_rate
print(eur_prices)


print("\n--- Solution 2 ---")
data_matrix = np.array([
    [10,20,30],
    [40,50,60],
    [70, 80, 90]
])
column_means = np.array([40, 50, 60])
normalized_matrix = data_matrix - column_means
print(normalized_matrix)


print("\n--- Solution 3 ---")
x = np.array([[1, 2], [3, 4]])
y = np.array([1, 2, 3])  
# Result: This will raise a ValueError!
# Reason: Shape (2, 2) and Shape (3,) are completely incompatible. 
# The trailing dimensions (2 and 3) are neither equal nor is one of them equal to 1.
print("Raises ValueError: operands could not be broadcast together")

# Actual Solution 
x = np.array([[1, 2], [3, 4]])[:, np.newaxis].shape
y = np.array([1, 2, 3]).reshape(3,1)[np.newaxis, :].shape

print(x)
print(y)

