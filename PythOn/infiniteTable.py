"""the is funstion which allow us to find table of any number to need range.
let's enjoy by using this function it will makes your life very easy
"""
def table():

    tableNumber =int(input("Enter a number you want table : "))
    rangeOfTable = int(input("tell the range of table you want : "))
    print("welcome to table of ", tableNumber, " to Range of ", rangeOfTable)
# we use here for loop for iteration
    for t in range(rangeOfTable):
        t = t +1
        print(tableNumber , " x ", t ," = " ,tableNumber*t)

table()
