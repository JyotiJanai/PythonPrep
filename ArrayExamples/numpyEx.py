import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
print("number of dimension of this array: ", arr.ndim)

# creating 2 dimensional (2D) array

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print("number of dimension of this array: ", a.ndim)

# creating 3 dimensional (3D) array

a1 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a1)
print("number of dimension of this array: ", a1.ndim)

a2 = np.array([1, 2, 3, 4], ndmin=5)
print("number of dimension of this array: ", a2.ndim)
