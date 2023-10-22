class ArrayList:
    "Implementing Array on the top of list data structure"
    def __init__(self, size):
        self.size = size
        self.array = [0]*size
        
    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index , value):
        if not isinstance(value, int):
            raise TypeError("Arraylist only accepts Integer")
        self.array[index] = value

    def __len__(self):
        return self.size
    def __repr__(self):
        return f"IntArray :{self.size}"
    def __str__(self):
        return str(self.array)

array = ArrayList(5)
array[0]= 4
array[1]= 3
array[2]= 4
array[3]= 55
array[4]= 65
array[5]= 65
# print(array[1])
print(array)
print(ArrayList.__doc__)


