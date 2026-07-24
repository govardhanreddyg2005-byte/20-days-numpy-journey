"""
Day 06: Statistical Reductions - Exercises

Instructions:
1. Complete the tasks below without using native Python loops (for/while).
2. Run this script to verify your logic or check solutions.py for reference.
"""

import numpy as np

# Mock dataset representing exam scores for 4 students across 3 subjects
# Rows = Students, Columns = Subjects (Math, Science, History)
scores = np.array([
    [50,60,75],
    [80,90,95],
    [100, 95, 90] 
])

print("Student Exam Scores Matrix:")
print(scores)
print("-" * 40)

# =====================================================================
# TASK 1: Find the minimum score achieved in each subject (column minimums).
# Expected Output Shape: (3,)
# Hint: Look closely at your axis choice!
# =====================================================================
subject_minimums = None  # Replace with your code

print("Task 1 - Minimum score per subject:")
print(subject_minimums)
print("-" * 40)


# =====================================================================
# TASK 2: Calculate the average final score for each student (row-wise averages).
# Expected Output Shape: (4,)
# =====================================================================
student_averages = None  # Replace with your code

print("Task 2 - Average score per student:")
print(student_averages)
print("-" * 40)
