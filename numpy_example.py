import numpy as np


array1 = np.array([1,2,3,4,5])
array2 = np.array([[1,2], [2,4]])
array3 = np.array([[[1,2], [2,4]], [[1,2], [2,4]]])
#print(array2)
#print(array3)
#print(np.zeros((3, 4)))
#print(np.ones((2,2)))
#print(np.eye(4))
#print(np.arange(1, 12, 1)) # start from end, end , step
#print(np.linspace(0, 2, 5))
 
ar1 = np.array([1,3,4,6,8])
ar2 = np.array([2,4,9,7,5])

#print(ar1 + ar2)
#print(ar1 - ar2)
#print(ar1 * ar2)
#print(ar1 / ar2)   
 
 
 
#print("Multiply by 3:", ar1 * 3)
#print("Add 5:", ar2 + 5)

#print(ar1 > 2 )
#print(ar1 == 2 )

#print(np.logical_and(ar1,ar2))
#print(np.logical_or(ar1,ar2))
#print(np.logical_not(ar1,ar2))

print(np.dot(ar1, ar2))
""" 
print(np.sum(array1))
print(np.mean(array1))
print(np.sqrt(array1)) """
