import ctypes
class IntArray:
    def __init__(self , size):
        self.size = size
        self.type = ctypes.c_int * size
        self.elements = self.type()
    
    def __len__ (self):
        return self.size

    def __getitem__(self , index):
        if not 0 <= index < self.size:
            raise IndexError("Array index is out of range ")
        return self.elements[index]

    def __setitem__(self , index , value):
        if not 0 <= index < self.size:
            raise IndexError("Array index is out of range ")
        self.elements[index] = value

array = IntArray(5)
array[0] = 4
array[0] = 3
array[0] = 4
array[1] = 55
array[1] = 65
array[1] = 65
print(array[1] [0])
print(array.__dir__())
# print(array)
 
# for i in range (len(array)):
#     print(array[i])