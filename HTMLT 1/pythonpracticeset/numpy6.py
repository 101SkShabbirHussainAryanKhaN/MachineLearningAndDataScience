import numpy as n
d2aray = n.arange(1,101).reshape(10,10)
print(d2aray)

indexx = d2aray[0,1]
print(indexx)
index1 = d2aray[1,0]
print(index1)
inmax = d2aray[0]
print(inmax)
inmx = d2aray[:,0]
print(inmx)

inm = d2aray[:,0:1]
print(inm)

sizee = d2aray.itemsize
print(sizee)