# Lambda functions or anonymous functions
# def add(a , b) :
#     return a+b

# minus = lambda x,y : x - y

# # def minus(x,y) :
# #     return x-y
# print("The Value of x-y is :",minus(9,3))

# def a_first(a):
#     return a[1]

a = [[12,34], [4,65], [66,87]]
# a.sort(key= a_first)
a.sort(key= lambda x:x[1])
print(a)