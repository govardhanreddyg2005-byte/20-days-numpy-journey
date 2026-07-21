"""
Day 4 Solutions
"""
import numpy as np

print("--- Solution 1 ---")
ans_1 = np.array([1, 2, 3, 4, 5], dtype=complex)
print(ans_1)

print("\n--- Solution 2 ---")
mixed_floats = np.array([0.0, 1.5, -3.2, 0.0, 0.01])
ans_2 = mixed_floats.astype(bool)
print(ans_2) # 0.0 becomes False, all non-zero numbers become True

print("\n--- Solution 3 ---")
string_numbers = np.array(["10", "20", "30"])
ans_3 = string_numbers.astype(np.int32)
print(ans_3)
print(f"Sum of elements: {ans_3.sum()}")
