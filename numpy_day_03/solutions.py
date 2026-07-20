"""
Day 3 Solutions
"""
import numpy as np

print("--- Solution 1 ---")
arr_1d = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
ans_1 = arr_1d[2:7:2]
print(ans_1) # [30 50 70]

print("\n--- Solution 2 ---")
matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7, 8, 9]
     
])
ans_2 = matrix[1, 1]
print(ans_2) # 5

print("\n--- Solution 3 ---")
ans_3 = matrix[1:, 1:]
print(ans_3)


a = [1,2,3,4]

b = [5,6,7,8]

arr = np.array(a).reshape(1,4)

arr1 = np.array(b).reshape(1,4)

print(np.floor_divide(arr, arr1))
