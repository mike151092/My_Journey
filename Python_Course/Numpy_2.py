#NUMPY Indexing and selection

import numpy as np

a = np.arange(0,11)

print(a)
print(a[2:8]) #similar to slicing in List

print(a[4:])

#broadcasting is setting a slice to particular number
broadcast = a[4:7] # It takes the slice but also impacts the original array
print(broadcast)
broadcast[:] = 88

print(broadcast)
print(a) #it affects the original array

#inorder to protect the original array make a copy

new_broadcast = a.copy()
new_broadcast[:] = 100
print(a)
print(new_broadcast)

#Indexing 2D array

arr_2D = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2D)

print(arr_2D[2,1]) #here we can use comma to print the values
print(arr_2D[1:,:])

#Conditional selection

bb = np.arange(1,11)

print(bb)

print(bb > 5) # gives the boolena values

cc = bb[bb>5] # using this boolean array  to conditionally filter the arrayt
print(cc)

print(bb[bb>5])

#HomeWork

arra_2D = np.arange(50).reshape(5,10)

print(arra_2D)

print(arra_2D[1:4,1:4])