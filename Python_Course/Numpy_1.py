##########################################
# Numpy arrays mostly used in the course #
# vector and matrices                    #
#vector are strictly 1D array            #
# Matrices are 2D                        #
##########################################

import numpy as np

x = np.arange(0,10,2) # Third arugument here is the step size

print(x)

y = np.zeros((3,3))

print(y)

z = np.ones((2,3))

print(z)

i = np.linspace(0,10,15) #thrid argument in linspace divides how many element you wwant in the array

print(i)

#creating identity matrix
j = np.eye(3)

print(j)

#random method
k = np.random.rand(3,3)

print(k)

#Random normal distribution
a = np.random.randn(2,3)
print(a) #gives results from the normal distribution

#Random integer
b = np.random.randint(1,100,10) #the last digit is the number of outputs that is needed between the set of numbers
print(b)

arr = np.arange(25)

print(arr)

ranarr = np.random.randint(0,50,10)

print(ranarr)

g = arr.reshape(5,5)
print(g)

print(ranarr.max()) #gives the maximum value
print(ranarr.min()) #gives the minimum value
print(ranarr.argmax()) #gives the location of the maximum value
print(ranarr.argmin()) #gives the location of the minimum value

print(ranarr.shape) 