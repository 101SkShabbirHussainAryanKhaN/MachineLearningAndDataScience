# def intro(strf):
    #   intro()
#     print("This is : " + strf)

# intro("Aryan Khan")

# def factorailIterative(n) :
#     fact = 1
#     for i in range(n):
#         fact = fact * (i+1)
#     return fact
#     """
#     param n: integer
#     return: n*n-1*n-2*n-3.......1"""
    
    
#     # By using Recursive function method 
# def factorailRecursive(n) :
#     if n == 1:
#         return 1
#     else :
#         return n*factorailRecursive(n-1)
#     """
#     param n: integer
#     return: n*n-1*n-2*n-3.......1"""

# number = int(input("Enter a number you factorial of :"))
# print("The factorial of iterative method ",number ,"is :",factorailIterative(number))

# print("The factorial of recursive function ",number ,"is :",factorailRecursive(number))

# function is to print fabonacci series
# 0 1 1 2 3 5 8 13
def fabonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else :
        return fibonacci (n-1) + fibonacci (n-2)
    
    
number = int(input("Enter a number you factorial of :"))
print("The fabonacci series ",number ,"is :",fabonacci(number))
