import ctypes
class CtyArray:
    def __init__(self , rows, cols):
        self.rows = rows
        self.cols = cols
        self.array = [[ctypes.c_int  for j in range(cols)] for i in range(rows)]
        


    def get_item(self ,row, col ):
        # now we setting indexError find to debug our program efficiently
          if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of range")
          return self.array[row][col]

    def set_item(self , row, col , value):
        self.array[row][col] = value

aray = CtyArray(3,3) 
aray.set_item(0, 0,  10)
aray.set_item(0, 1,  20)
aray.set_item(0, 2,  30)

aray.set_item(1, 0 , 40)
aray.set_item(1, 1 , 50)
aray.set_item(1, 2,  60)

aray.set_item(2, 0 , 70)
aray.set_item(2, 1 , 80)
aray.set_item(2, 2,  90)
# print(help(CtyArray))
# print(aray.__dir__())
for i in range(aray.rows):
    row = [str(aray.get_item(i,j))
    for j in range(aray.cols)]
    print(" ".join(row))

# This will raise indexError because this is out of range/not found
print(aray.get_item(3,0))
