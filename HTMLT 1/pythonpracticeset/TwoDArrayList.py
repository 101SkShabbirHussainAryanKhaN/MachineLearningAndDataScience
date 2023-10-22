class TwoDArray:
    def __init__(self ,rows, cols):
        self.rows = rows
        self.cols = cols
        # self.array = [[0 for j in range(cols)] for i in range(rows)]

    def get_element(self, row , col):
        return self.array[row][col]

    def set_element(self, row , col ,value):
        if not isinstance(value, int):
            raise TypeError("Arraylist only accepts Integer")
        self.array[row][col] = value
    
    def get_row(self, row):
        return self.aray[row]

    def get_col(self, col):
        return [row[col] for row in self.aray]

aray = TwoDArray(3,3)
# aray[0] [0]= 4
# aray[0] [1]= 3
# aray[0] [2]= 4
# aray[1] [0]= 55
# aray[1] [1]= 65
# aray[1] [2]= 65
# aray[2][0]= 43
# aray[2][1]= 33
# aray[2][2]= 19
aray.set_element(0, 0,  1)
aray.set_element(0, 1,  2)
aray.set_element(0, 2, 4)

aray.set_element(1, 0 , 5)
aray.set_element(1, 1 , 9)
aray.set_element(1, 2,  6)

aray.set_element(2, 0 , 10)
aray.set_element(2, 1 , 15)
aray.set_element(2, 2,  16)

# print(aray.get_row(0))
# print(aray.get_row(1))
# print(aray.get_col(2))

for i in range(aray.rows):
    row = [str(aray.get_element(i,j))
    for j in range(aray.cols)]
    print(" , ".join(row))