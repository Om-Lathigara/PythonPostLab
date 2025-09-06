# Replace all elements greater than 10 in a 1D array with the string "BIG"
import numpy as np
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [11,12,13,14,15,16,17,18,19,20]
a = np.array(list1) + np.array(list2)
a = a.astype(object)    
a[a > 10] = "BIG"
print(a)
