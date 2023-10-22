import math

# F String
me = "Sk Aryan Khan"
a = "This is %s"%me
print(a)

me = "Sk Aryan Khan"
d = 4
a = "This is %s %s"%(me,d)
a = "This is {} {}"
b = a.format(me,d)
print(b)
a = f"This is : {me} {d} {math.cos(65)}"
print(a)

def average(*numbers):
    sum =0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)

a = average(4,7,4,7,6,8)
print(f"the average of is : {a}")

def Addition(*numbers):
    sum =0
    for i in numbers:
        sum = sum + i
    return sum

a = Addition(4,7,4,7,6,8)
print(f"the Sum of is : {a}")

