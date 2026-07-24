"""
Day 07: Extremas & Sorting - Exercises

Instructions:
1. Complete the tasks below using clean, fundamental NumPy operations.
"""

import numpy as np

# Task 1 Dataset: A simulated single-channel digital image matrix (4x4 pixels)
# Values represent light intensity levels from 0 to 255.
image_channel = np.array([
    [100,99,50,20],
    [70,80,85,95],
    [63,142,15,120]
])

print("Image Intensity Channel Matrix:")
print(image_channel)
print("-" * 50)

# =====================================================================
# TASK 1: Find the flat index position of the brightest pixel (highest value).
# Then find the horizontal index position of the highest value in each row.
# =====================================================================
brightest_flat_index = None        # Replace with your code
brightest_per_row_indices = None   # Replace with your code

print("Task 1 Results:")
print("Flat index of overall peak intensity:", brightest_flat_index)
print("Column indices of peak intensity per row:", brightest_per_row_indices)
print("-" * 50)


# Task 2 Dataset: 3 test scores for 3 distinct students
student_scores = np.array([
    [50,60,70],
    [80,85,90],  # Student A,  # Student B
    [99,82,85]   # Student C
])

print("Unsorted Student Scores:")
print(student_scores)
print("-" * 50)

# =====================================================================
# TASK 2: Sort the scores for each student independently in ascending order.
# Hint: You want to sort horizontally across columns, keeping rows separated.
# =====================================================================
sorted_student_scores = None  # Replace with your code

print("Task 2 Results (Each row sorted independently):")
print(sorted_student_scores)
print("-" * 50)
