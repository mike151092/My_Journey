#numpy Operations
#Array with Array, Array with scalar, Universal Array Functions

import numpy as np

arr = np.arange(0,11)

print(arr)
print(arr + arr)
print(arr-arr)
print(arr*arr)
#print(arr//arr)

#when you add a scalar with array it propgate to the whole list of array
print(100+arr)

#universal Functions operations
print(np.sqrt(arr))