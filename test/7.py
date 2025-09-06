# create 1D numpy array of length 100, and replace every 6th element with -1 
import numpy as np
c = np.arange(1, 101)
c[5::6] = -1
print(c)   