# def show():
#     print('hello Sk programming zone ')

# show1 = show
# del show
# show1()

# def func(n):
#     if n == 0:
#         return print
#     if n == 1:
#         return int

# a = func
# print(a(1))

def dec(funcc):
    def nowexec():
        print('Executing Now!')
        funcc()
        print('Executed!')
    return nowexec
@dec
def sk():
    print('Hi programmars , this is sk Aryan Khan')

# sk = dec(sk)
sk()