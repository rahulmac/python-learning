import numpy as np



arr = np.array([1,2,3,4,5,6])

print(arr.reshape(3,2)) # first element number of rows , second element number of columns


# 2d to 1d using flatten or ravel
arr2d = np.array([[1, 2], [3, 4]])

print(arr2d.flatten())
print(arr2d.ravel   ())



print('other')
print(np.sum(arr))
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))