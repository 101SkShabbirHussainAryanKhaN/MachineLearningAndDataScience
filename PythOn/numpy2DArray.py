import numpy as np

# Define a custom data structure for the 2D array
class CustomArray:
    def _init_(self, rows, cols):
        self.data = np.zeros((rows, cols), dtype=np.int32)
    
    def get_element(self, row, col):
        return self.data[row][col]
    
    def set_element(self, row, col, value):
        self.data[row][col] = value

# Define a custom algorithm to populate the 2D array
def populate_array(array):
    for row in range(array.data.shape[0]):
        for col in range(array.data.shape[1]):
            array.set_element(row, col, row * col)

# Create a 2D array using the custom data structure and algorithm
array = CustomArray(3, 4)
populate_array(array)

# Print the contents of the array
for row in range(array.data.shape[0]):
    for col in range(array.data.shape[1]):
        print(array.get_element(row, col), end=" ")
    print()