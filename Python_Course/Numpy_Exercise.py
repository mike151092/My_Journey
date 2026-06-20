#Numpy exrecise
import numpy as np

a = np.zeros(10)
print(a)

b = np.ones(10)

print(b)


print(np.ones(10)*5)

#Array of integers from 10 to 50 
print(np.linspace(10,50,41))

#create an even integers from 10 to 50
print(np.linspace(10,50,21))

#create a 3x3 matrix ranging from 0 to 8
c = np.array([[0,1,2],[3,4,5],[6,7,8]])
print(c)

d = np.eye(3)
print(d)

print(np.random.rand(1,1))
##Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
print(np.random.randn(25))
#create the following matrix
print(np.linspace(0,1,101))
#create an array 20 lineraly space between 20
print(np.linspace(0,1,20))

#Numpy Indexing and selection

mat = np.arange(1,26).reshape(5,5)

print(mat)

print(mat[2:,1:])

print(mat[3,4])

print(mat[0:3,1:2])

print(mat[4,:])
print(mat[3:,:])

print(mat.sum())
print(mat.std())
print(mat.sum(axis=0))