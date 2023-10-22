# def fun():
#     print("Sk Aryan Khan Parwana jAAn")
# func = fun
# # deleting the function now by using del command
# del fun
# func()
# fun() this will through error because because we already have deleted

# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return int
# a = funcret(1)
# print(a)

# by using decorators 
def dec(funca):
    def nowexec():
        print("Executing now")
        funca()
        print("Executed!")
    return nowexec()

@dec
def sk():
    print("This is Sk Aryan")

# sk= dec(sk)