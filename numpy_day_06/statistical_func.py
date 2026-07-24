"""
Day 06: Statistical Reductions
Concept: Computing aggregations across specific axes using NumPy.
"""

import numpy as np

# 1. Create a dummy 2D dataset (3 rows, 4 columns)
matrix = np.array([
    [10,20,30,40],
    [50,60,70,80],
    [90, 100, 110, 120]
])

print("--- Original Matrix ---")
print(matrix)
print(f"Shape: {matrix.shape}\n")

# 2. Global Reductions (Flattens the array automatically)
print("--- Global Reductions ---")
print(f"Total Sum:       {np.sum(matrix)}")
print(f"Average (Mean):  {np.mean(matrix)}")
print(f"Median:          {np.median(matrix)}")
print(f"Std Deviation:   {np.std(matrix):.2f}")
print(f"Variance:        {np.var(matrix):.2f}\n")

# 3. Axis-Targeted Reductions
# Key Rule: The specified axis is the dimension that gets collapsed/eliminated.

# Axis 0: Collapses rows. Performs operations downward along columns.
# Result shape will match the number of columns: (4,)
print("--- Axis 0 (Column-wise reductions) ---")
col_sum = np.sum(matrix, axis=0)
col_mean = np.mean(matrix, axis=0)
print(f"Sum of each column:  {col_sum}")
print(f"Mean of each column: {col_mean}\n")

# Axis 1: Collapses columns. Performs operations horizontally across rows.
# Result shape will match the number of rows: (3,)
print("--- Axis 1 (Row-wise reductions) ---")
row_sum = np.sum(matrix, axis=1)
row_std = np.std(matrix, axis=1)
print(f"Sum of each row:  {row_sum}")
print(f"Std of each row:  {row_std}")
