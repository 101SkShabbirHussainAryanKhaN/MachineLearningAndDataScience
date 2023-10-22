# this function will return the fibonacci series of any number

def fibo(n):
    if n < 0:
        print("Please Enter any positive integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # this is formula to find fabonacci series
        return fibo(n - 1) + fibo(n - 2)
# 5 - 1 = 4,      5 - 2 = 3  ,            4 + 3 = 7
# 4 - 1 = 3,      4 - 2 = 2  ,            3 + 2 = 5
# 3 - 1 = 2,      3 - 2 = 1  ,            2 + 1 = 3
# 2 - 1 = 1,      2 - 2 = 0  ,            1 + 0 = 1
# 1 - 1 = 0,      1 - 2 = 0  ,            1 + 0 = 1
nterm = int(input("Enter limit to find fabonacci Series :"))
fibo(nterm)
for i in range(nterm):
    # we use this for loop to acces all values of fabonacci series
    if fibo(i)>=100:
        print(f"loop is being terminated due to {fibo(i)} ,which is greater than 100")
        break
        
    print(f"Fibonacci series of {i}: ",fibo(i))


    