try :
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))
    num3 = num1 + num2
    print("the Sum is :" ,num3)
except Exception as e:
    print(e)

print("This is very important Portion")