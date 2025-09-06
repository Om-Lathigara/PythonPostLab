# Extract the middle 2x2 matrix from a 4x4 matrix

import numpy as np
a = np.array([[[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]]])
matrix_4x4 = a.reshape(4, 4)
print("Original 4x4 matrix:")
print(matrix_4x4)
middle_2x2 = matrix_4x4[1:3, 1:3]
print(middle_2x2)
print(matrix_4x4[1:3,3])