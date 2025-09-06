# create 4*4 matrix and replace all odd numbers with -1
import numpy as np
a = np.arange(1, 17).reshape(4, 4)
a[a % 2 == 1] = -1
print(a)