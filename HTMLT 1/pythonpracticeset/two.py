class TwoDArray:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.array = [[None] * cols for _ in range(rows)]

    def get(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of range")
        return self.array[row][col]

    def set(self, row, col, val):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of range")
        self.array[row][col] = val

# Create a 2D array with 3 rows and 4 columns
arr = TwoDArray(3, 3)

#Now we are Setting some values in the array

arr.set(0, 0,  1)
arr.set(0, 1,  2)
arr.set(0, 2,  4)

arr.set(1, 0 , 5)
arr.set(1, 1 , 9)
arr.set(1, 2,  6)

arr.set(2, 0 , 10)
arr.set(2, 1 , 15)
arr.set(2, 2,  16)


# Get some values from the array
print(arr.get(0, 0))  # Output: 1
print(arr.get(0, 1))  # Output: 2
print(arr.get(1, 2))  # Output: 4
print(arr.get(2, 2))  # Output: 16

for i in range(arr.rows):
    row = [str(arr.get(i,j))
    for j in range(arr.cols)]
    print(" ".join(row))

# Try to access an out-of-range index
arr.get(3, 0)  # Raises an IndexError

