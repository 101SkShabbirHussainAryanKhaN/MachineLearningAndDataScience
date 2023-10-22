# a = 12
# b = 17
# c = sum((a, b)) #build in function
# print("The Sum of A and B is :", c)

# def function(a,b):
#     print("the Sum :" ,a+b)
# def function2(a,b):
#     average = (a+b)/2
#     # print(average)
#     return average
# function(12,54)
# s = function2(36,4)
# print("The Average value is :", s)

def Average() :
     """\nThis is a function to calculate average of four numbers :"""
     i = int(input("Enter first number :"))
     j = int(input("Enter second number :"))
     k = int(input("Enter 3rd number :"))
     l = int(input("Enter 4th number :"))
     m = int(input("Enter number of Entries :"))
     avrage = (i+j+k+l)/m
     return avrage

print(Average.__doc__)
A = Average()
print("The Average value is :", A)
