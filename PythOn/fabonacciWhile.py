limitFab = int(input('enter the value to find fabonacci Series :'))
a , b = 0 , 1

while a < limitFab:
    print(a)
    a , b = b 
    a = a + b
