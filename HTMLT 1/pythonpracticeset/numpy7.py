import numpy as n
d2aray = n.arange(1,17).reshape(4,4)
print(d2aray)

arr = n.arange(17,33).reshape(4,4)
print(arr)

conc = n.concatenate([d2aray, arr])
print(conc)

conca = n.concatenate([d2aray, arr] ,axis= 1)
print(conca)

concat = n.vstack((d2aray, arr))
print(concat)

concate = n.hstack((d2aray, arr))
print(concate)

concaten = n.hstack((d2aray, arr,d2aray))
print(concaten)

spl = n.split(d2aray, 4)
print(spl)