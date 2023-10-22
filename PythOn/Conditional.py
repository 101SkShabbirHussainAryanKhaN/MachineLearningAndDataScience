var2 = 65
#To print Message on Screen 
print("Enter any number : ")
#To take input from User
var3 = int(input())

# indentation ka ka khayal rakhna hai.....
# to check whether var3 is greater , equal or Smaller
if var3>var2:
    print(f"{var3} is Greater than {var2}")
elif var3==var2:
    print("Equal")
else:
    print(f"{var3} is Smaller than {var2}")

# Declare a List
List1 = [1, 5, 7 ,9 ,2,3,4]
# To print Message on Screen 
print("Enter any number to check in list : ")
#To take input from User
var3 = int(input())
# to check whether var3 is in list or not
if var3 in List1:
        print("yes its in the List :" ,var3)
elif var3  not in List1:
        print ("This is not present in the List :" ,var3)
else:
    print ("This is not Matched the creteria :" ,var3)


#To print Message on Screen 
print("Enter your Age: ")
#To take input from User
age = 18
var3 = int(input())
if var3 > 18 and var3 < 70:
        print("yes you can drive :" ,var3)
elif var3 < age and var3 > 7:
        print ("No you can not drive : " ,var3)
elif var3 == age:
         print ("I will think about you, you Should visit our Company : " ,var3)
else:
    print ("This is not Matched the Creteria : " ,var3)
