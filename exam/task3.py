#create 2D array, extract 1st column and 1st row and add them
import numpy as np
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
first_row = array_2d[0, :]
first_column = array_2d[:, 0]
result = first_row + first_column
print("First row:", first_row)
print("First column:", first_column)
print("Result of addition:", result)