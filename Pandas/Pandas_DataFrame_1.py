import numpy as np
import pandas as pd

np.random.seed(101)

df =pd.DataFrame(np.random.randn(5,4),['A','B','C','D',"E"],['W','X','Y','Z'])

print(df)

print(df['W'])
print(df[['W','Z','X']]) #when we need multiple columns we pass it as a list to the dataFrame

df['new'] =df['W'] + df['Y']

print(df)
df.drop('new',axis=1,inplace=True) #in the drop method default axis=0 is set to rows and set inplace = True to make the changes

print(df)

#df.drop('E',axis=0,inplace=True)
#print(df)

print(df.loc['A'])# variable name based location
print(df.iloc[2]) #integer based location

print(df.loc['B','Y'])

print(df.loc[['A','B'],['W','Y']])