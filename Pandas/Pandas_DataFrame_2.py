import numpy as np
import pandas as pd

np.random.seed(101)

df =pd.DataFrame(np.random.randn(5,4),['A','B','C','D',"E"],['W','X','Y','Z'])

print(df)

#Conditional selection
booldf =df >0

print(booldf)

print(df[booldf])

print(df['W']>0)

resultdf=df[df['W']>0]
print(resultdf['X'])

#line 19 and 20 can be written in a single line
print(df[df['W']>0][['X','Y']])

#Multiple condition
print(df[(df['W']>0) & (df['Y']>1)]) #Pyhton normal and cannot be used here

#Reseting index
print(df.reset_index()) #needs inplace to be True for its proper function

New_Index= 'MDU TN CHE TEN CBE'.split()

df['Cities']= New_Index

print(df)

df.set_index('Cities')#inplace should be set to true for this to take effect

print(df)