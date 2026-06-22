import numpy as np
import pandas as pd

df =pd.DataFrame({'col1':[1,2,3,4],
                  'col2':[444,555,656,444],
                  'col3':['abc','def','ghi','xyz']})

print(df.head())

#fiding unique values
print(df['col2'].unique)
#value counts
print(df['col2'].value_counts())

#coditional selection
print(df[df['col1']>2])
print(df[(df['col1']>2) & (df['col2']==444)])

#Apply Method
def times2(x):
    return x*2

print(df['col1'].apply(times2)) #using customized functions to the dataframes

print(df['col2'].apply(lambda x: x*2))

print(df.columns)

#Sorting and ordering a data frame
print(df.sort_values(by='col2'))

print(df.isnull())

data_1 = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df1 = pd.DataFrame(data_1)
print(df1)

print(df1.pivot_table(values='D',index=['A','B'],columns=['C']))

