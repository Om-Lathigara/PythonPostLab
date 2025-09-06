# Find all perfect squares in a 6x6 array of numbers from 1 to 36
import numpy as np
a = np.arange(1, 37).reshape(6, 6)
perfect_squares = a[(a**0.5) % 1 == 0]
print(perfect_squares)
