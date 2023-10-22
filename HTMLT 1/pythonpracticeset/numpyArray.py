import numpy as n
from array import *
import sys
arr1 = n.array([1,3,5,7,9])
print(arr1)
print(f'The type of Array is : {type(arr1)}')
print(f'The Dimension of Array is : {arr1.ndim}')

arr = n.array([[1,2,3,4],[5,6,7,8]])
print(arr)
print(f'The Dimension of Array is : {arr1.ndim}')
print(f'The Size of Array is : {arr.size}')
# it will print (2 , 4) it means 2 rows and 4 columns
print(f'The shape of Array is {arr.shape}')
print(arr.dtype)
# arr1.append(10)
# print(arr1)

# n_arr = n.array([1,3,5,7,9])
# print(n_arr)

# narr = n.zeros((2,))