"""
Day 4: Data Types & Casting Demonstrations
"""
import numpy as np

print("--- Checking and Forcing dtypes ---")
# NumPy infers the type automatically
arr1 = np.array([1, 2, 3])
print(f"Inferred type: {arr1.dtype}")

# Forcing a float type on integers
arr2 = np.array([1, 2, 3], dtype=np.float32)
print(f"Forced type: {arr2.dtype} -> {arr2}\n")

print("--- Casting with .astype() ---")
float_arr = np.array([1.9, 2.5, 3.1])
# Casting floats to ints truncates the decimal part (it does not round!)
int_arr = float_arr.astype(np.int32)
print(f"Original Floats: {float_arr}")
print(f"Casted Integers: {int_arr}")
