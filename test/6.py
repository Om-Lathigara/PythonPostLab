# create 3*3 1 to 9 matrix and sort each row in the ascending order
import numpy as np
a = np.array([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
a.sort(axis=1)
print(a)