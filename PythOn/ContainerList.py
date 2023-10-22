#List in python

grocery = ["Harpic ","Vim Bar" ,"Deodrant" ,"Bhindi" ,"Chocolate"]
print(grocery)
grocery1 = ["harpic ","Vim Bar" ,"Deodrant" ,"Bhindi" ,"Chocolate", 67, 45, 32, 89]
print(grocery1)
numbers = [7,55,98,87,76,22,43,45]
numbers[0]= 96
print(numbers)
numbers.sort()
print("This is List of Sorted Data :",numbers)
numbers.reverse()
print("This is List of Reverse Data :",numbers)
numbers.__delitem__(2)
print(numbers)
# Mutable - can be changed
# imMutable - cannot be changed
tp = (1,2,3,4,5)
print(tp)

#Swaping the numbers
a = 4
b = 9
print("Before Swaping the Value of a =" ,a ,"b =", b)
a, b = b, a
# temp = a
# a = b
# b = temp
print("After Swaping the Value of a =" ,a ,"b =", b)