numbers = ["33","54","98"]
numbers =list(map(int , numbers))

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# numbers[1]+=6
# print("the Sum of 54 and 6 is :",numbers[1])

# numbers[2]+=6
# print("the Sum of 54 and 6 is :",numbers[2])

# def sq(a):
#     return a*a

# num = [1,3,4,5,65,76,8,78,76,98,99,77]
# square = list(map(sq, num))
# print(square)

# by using lambda function same logic
# num = [1,3,4,5,65,76,8,78,76,98,99,77]
# cube = list(map(lambda x :x*x*x, num))
# print("The Cube of this list is:",cube)

# def sq(a):
#     return a*a

# def cube(a):
#     return a*a*a

# fun =[sq, cube]
# for i in range(5):
#     val = list(map(lambda x:x(i),fun))
#     print(val)

# using filter function 

# list1 = [1,3,4,5,65,76,8,78,76,98,99,77]

# def greaterThan5(num):
#     return num>5

# greatThn5 = list(filter(greaterThan5,list1))
# print("these are greater than 5 :",greatThn5)

#By using Reduce function in python
from functools import reduce as r
list3 = [1,3,4,5,65,76,8,78,76,98,99,77]
# by using for loop
# num = 0
# for i in list3:
#     num+=i
# print(num)

# by using reduce function
sum = r(lambda x,y:x+y, list3)
print(sum)
prod = r(lambda x,y:x*y, list3)
print(prod)
sub = r(lambda x,y:x-y, list3)
print(sub)
div = r(lambda x,y:x/y, list3)
print(div)