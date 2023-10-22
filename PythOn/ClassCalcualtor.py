class Calculator:
    def __init__(self, num1 ,num2):
        self.num1 = num1
        self.num2 = num2
        self.result = 0
    def __add__ (self, num1,num2):
        print(f'self {self.num1} and num1 {self.num2}')
        return self.num1 + self.num1
        

    def __sub__(self, num1):
        return self.num - num1.num

    def __mul__(self, num1):
        return self.num * num1.num

    def __div__(self, num1):
        return self.num / num1.num

    def __mod__(self, num1):
        return self.num % num1.num

    def __pow__(self, num1):
        return self.num ** num1.num
    def __repr__(self):
        print(self.result)

calc = Calculator(12,5)

print(calc.__add__(12,7))



