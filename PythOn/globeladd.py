# l = 20 
# k = 67 
# h = 55
#  # global variable
# def func (n) :
#     l = 5
#     k = 87
#     s = 65
#     # if you want to modify value of h you have to write global keyword
#     global h
#     h = h + 35
#     print(h)
#     print("These are local varibles : ","\nValue of L :",l ,"\nValue of K :", k)
#     print(n, "I have printed")
    
# func("This is me Aryan Khan :")
# print("These are Global varibles : ","\nValue of L :",l,"\nValue of K :", k)
# #  print("we cannot do this because s is a local variable it through error :",s)

def sk():
    x = 38
    def aryan():
        global x
        x = 89
    print("before calling aryan :" , x)
    aryan()
    print("after calling aryan :" , x)
       
sk()
print(x)