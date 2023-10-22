class Calculator:
    "this is simple calculator pogramme"
    def __init__(self):
        
        num1 = float(input("Enter first Number :"))
        num2 = float(input("Enter Second Number :"))
        operator= input("Enter any operator from these -,+,/,*,%,**, \n Q to Quit!:")
    
        if operator == "+":
            print(f"The of Sum {num1} and {num2} is :", num1+num2)

        elif operator == "-":   
           print(f"The of Subtraction {num1} and {num2} is :", num1-num2)

        elif operator == "/":   
            print(f"The of Division {num1} and {num2} is :", num1/num2)

        elif operator == "*":   
            print(f"The of Multiplication {num1} and {num2} is :", num1*num2)

        elif operator == "%":   
            print(f"The of Remainder {num1} and {num2} is :", num1%num2)

        elif operator == "**":  
            print(f"The of power {num1} and {num2} is :", num1**num2)
        elif operator == "Q".lower():
            exit()

Calc = Calculator()
print(__doc__)