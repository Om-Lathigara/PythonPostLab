# Find all border elements in a 5x5 array of numbers from 1 to 25
import numpy as np
a = np.arange(1, 26).reshape(5, 5)
border_elements = list(a[0, :]) + list(a[-1, :]) + list(a[1:-1, 0]) + list(a[1:-1, -1])
print(border_elements)
