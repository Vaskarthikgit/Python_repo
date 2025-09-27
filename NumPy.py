import numpy as np
from numpy.linalg import det, inv

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([2,4,6,8,20])
# print(arr1+arr2)
# print(arr1*arr2)
# print(arr2-arr1)
# print(np.add(arr1,arr2))
# print(np.multiply(arr1,arr2))
# print(np.subtract(arr2,arr1))

arr3 = np.array([[1,2],[3,4]])
arr4 = np.array([[4,2],[3,6]])

print(np.matmul(arr3,arr4))
print(det(arr4))
print(inv(arr4))

# 1 2    4 2 
# 3 4    3 6 


# 6 -2
# -3 4

# 0.33  -1.94 
# -2.95 0.2 

