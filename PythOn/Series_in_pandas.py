import pandas as p

# ser = p.Series([1,2,3,4,5,6,7,8,9,10])
# print(ser)
# To check version of pandas 
# version = p.__version__
# print(version)

# list_s = [1,2,3,4,-4,-6,8.5,'hello world ']
# general method to print list
# print(list_s)
# series = p.Series(list_s)
# Special method to print list by using pandas
# print(series)
# sries = p.Series([1,2,3,4,5])
# print(sries)
# emp = p.Series([])
# print(emp)

# to change index and data type and give naem to series 

# sries_s = p.Series([1,2,3,4,5], index = ['a', 'b','c','d','e'], dtype = float,name = 'sk jaan')
# print(sries_s)

# scalar_s = p.Series(0.5 ,index=[1,2,3,4,5])
# scalar_s += 1.5
# print(scalar_s)

dict_s = {a:'sk jaan', b: 'Aryan Khan'}
dic = p.Series(dict_s)
print(dic)
