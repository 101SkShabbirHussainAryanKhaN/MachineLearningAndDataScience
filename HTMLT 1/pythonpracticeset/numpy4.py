import numpy as n
# n.arrang(start, end , steps)
# ar_id = n.arange(1,13,2) 
ar_id = n.arange(1,13)
print(ar_id)

line = n.linspace(1,5,4)
print(line)

shape = ar_id.reshape(2, 6)
print(shape)

shape = ar_id.reshape(3, 4)
print(shape)
shape = ar_id.reshape(2, 3,2)
print(shape)

s2d = n.arange(1,13).reshape(2,6)
print(s2d)

# Ravl function is used to convert 3D array into !D array
ravl = s2d.ravel()
print(ravl)

# Flattten() function is used to convert multi dimensional array into !D array
flat = s2d.flatten()
print(flat)

# Transpose() function is used to convert multi dimensional array into !D array
tansp = s2d.transpose()
print(tansp)
tanp = s2d.T ()
print(tanp)