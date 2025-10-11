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

arr5 = np.arange(12).reshape(4,3)
print(arr5)
# arr6 = arr5 > 4
# print(arr6)

# print(arr5[arr6])
# print(arr5[arr5>4])

# print(arr5.ravel())
# print(np.min(arr5))
# print(np.max(arr5))
# print(np.average(arr5))

print(np.min(arr5, axis=0))
print(np.min(arr5, axis=1))
print(arr5[1:,2])

# for item in arr5.ravel():
#     print(item)


arr6 = np.array([[1,2,3],[3,4,2],[7,2,8]])
print(arr6)

print(len(arr6[arr6==18]))

arr7 = np.array([1,2,3,0,4,0,2,0,1,3,4,3,4])
print(np.bincount(arr7))
print(arr5>3)
print(np.nonzero(arr5>3))

sample_arr = np.array([[12,34,56],[54,32,21],[65,33,22]])
new_arr = np.array([[10,10,10]])

print(sample_arr)

sample_arr=(np.delete(arr=sample_arr, axis=1, obj=1))
print(np.insert(arr=sample_arr, axis=1, values=new_arr, obj=1))

