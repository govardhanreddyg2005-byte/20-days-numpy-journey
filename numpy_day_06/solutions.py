"""
Day 09: Statistical Reductions - Solutions
"""

import numpy as np

# Source matrix
scores = np.array([
    [50,60,75],
    [80,90,95],
    [100, 95, 90] 
])

print("--- Executing Solutions ---")

# Task 1 Solution: Column Minimums
# We need to collapse the row dimension to find a single min value per column -> axis=0
subject_minimums = np.min(scores, axis=0)

print("Task 1 - Minimum score per subject (Columns):")
print(f"Result: {subject_minimums}")
print(f"Math Min: {subject_minimums[0]}, Science Min: {subject_minimums[1]}, History Min: {subject_minimums[2]}")
print(f"Expected: [65 70 78]\n")


# Task 2 Solution: Row-wise Averages
# We need to collapse the column dimension to get a single mean value per student row -> axis=1
student_averages = np.mean(scores, axis=1)

print("Task 2 - Average score per student (Rows):")
print(f"Result: {student_averages}")
for i, avg in enumerate(student_averages):
    print(f"  Student {i} Average: {avg:.2f}")
print(f"Expected: [85.         86.33333333 71.66666667 95.        ]")
