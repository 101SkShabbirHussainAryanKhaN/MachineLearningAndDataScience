import numpy as n
"""ar2d = n.ones((4,4),dtype = int, order='C')
print(ar2d)
str2d = n.ones((4,4),dtype = str, order='C')
print(str2d)

zerod = n.zeros((3,4))
print(zerod)
zerodd = n.zeros((3,4), dtype= bool)
print(zerodd)
zeroda = n.zeros((3,4), dtype = str)
print(zeroda)

emp = ""
print(bool(emp))

empt = n.empty((3,3))
print(empt)"""

# Mathtematics operation Using Numpy

arr1 = n.arange(1,10).reshape(3,3)
arr2 = n.arange(1,10).reshape(3,3)
print(arr1,arr2)

print('The addition of Two Arrays',arr1 + arr2)

addition = n.add(arr1,arr2)
print(addition)

print('The substraction of Two Arrays',arr1 - arr2)

subtrcation = n.subtract(arr1,arr2)
print(subtrcation)
import numpy as n
"""ar2d = n.ones((4,4),dtype = int, order='C')
print(ar2d)
str2d = n.ones((4,4),dtype = str, order='C')
print(str2d)

zerod = n.zeros((3,4))
print(zerod)
zerodd = n.zeros((3,4), dtype= bool)
print(zerodd)
zeroda = n.zeros((3,4), dtype = str)
print(zeroda)

emp = ""
print(bool(emp))

empt = n.empty((3,3))
print(empt)"""

# Mathtematics operation Using Numpy

arr1 = n.arange(1,10).reshape(3,3)
arr2 = n.arange(1,10).reshape(3,3)
print(arr1,arr2)

print('The addition of Two Arrays',arr1 + arr2)

addition = n.add(arr1,arr2)
print(addition)

print('The substraction of Two Arrays',arr1 - arr2)

subtrcation = n.subtract(arr1,arr2)
print(subtrcation)

print('The Division of Two Arrays',arr1 / arr2)
div= n.divide(arr1,arr2)
print(div)

print('The Multiplication of Two Arrays',arr1 * arr2)
mul= n.multiply(arr1,arr2)
print(mul)

print('The Multiplication first row and first column of Two Arrays',arr1 @ arr2)
rowColumn= arr1.dot(arr2)
print(rowColumn)

maxi = rowColumn.max()
print(maxi)

maxindex = rowColumn.argmax()
print(maxindex)

maxinCol= rowColumn.max(axis = 0)
print(maxinCol)

maxinRow= rowColumn.max(axis = 1)
print(maxinRow)

minn = rowColumn.min()
print(minn)

minindex = rowColumn.argmin()
print(minindex)

minnCol= rowColumn.max(axis = 0)
print(minnCol)

mininRow= rowColumn.max(axis = 1)
print(mininRow)

add = n.sum(rowColumn)
print(add)

addcol = n.sum(rowColumn, axis= 0)
print(addcol)

addrow = n.sum(rowColumn, axis= 1)
print(addrow)

means = n.mean(rowColumn)
print(means)

sqroot = n.sqrt(rowColumn)
print(sqroot)

standardd = n.std(rowColumn)
print(standardd)

expo = n.exp(rowColumn)
print(expo)

nlog = n.log(rowColumn)
print(nlog)

nlog10 = n.log10(rowColumn)
print(nlog10)