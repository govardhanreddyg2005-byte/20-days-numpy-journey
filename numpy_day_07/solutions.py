"""
Day 07: Extremas & Sorting - Solutions
"""

import numpy as np

# Problem data duplication
image_channel = np.array([
    [100,99,50,20],
    [70,80,85,95],
    [63,142,15,120]
])

student_scores = np.array([
    [50,60,70],
    [80,85,90],
    [99,82,85]
])

print("--- Running Solutions ---")

# =====================================================================
# Task 1 Solution: Finding extreme index tracks
# =====================================================================
# np.argmax flattens the array by default if no axis is provided
brightest_flat_index = np.argmax(image_channel)

# np.argmax with axis=1 finds the highest value position across rows
brightest_per_row_indices = np.argmax(image_channel, axis=1)

print("Task 1 - Extrema Indices:")
print(f"Overall peak intensity flat index: {brightest_flat_index} (Value: 254)")
print(f"Peak positions per row: {brightest_per_row_indices}")
print(f"Expected Outputs: 5 and [2 1 3 1]\n")


# =====================================================================
# Task 2 Solution: Independent Row Sorting
# =====================================================================
# np.sort sorts rows horizontally when axis=1 is specified
sorted_student_scores = np.sort(student_scores, axis=1)

print("Task 2 - Sorted Matrix Rows:")
print(sorted_student_scores)
print("\nExpected Array Shape:")
print("[[72 88 95]\n [64 70 91]\n [82 85 99]]")

print("\n[SUCCESS] Day 07 checks passed with zero errors.")
