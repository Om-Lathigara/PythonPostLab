import numpy as np

array_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

# sub_matrix = array_2d[0:3, 0:3]

# diagonal_elements = sub_matrix.diagonal()

# sum_diagonal = np.sum(diagonal_elements)
# print("Diagonal elements:", diagonal_elements)

print(array_2d[0,0]+array_2d[1,1]+array_2d[2,2])
