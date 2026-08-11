#Workout to study the titanic dataset

import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df= sns.load_dataset('titanic')
#Check the size of the data
print(df.shape)
#check the data types
print(df.dtypes)
#Check for missing values
print(df.isnull().sum())

#check how the data looks like
print(df.head())
#df.info()

#Statistics
print(df.describe())

print(df[df['sex']=='female'])
print(df[df['age'] > 50])

print(df[(df['age'] >50) & (df['sex'] == 'female')])

print(df['age'] > 50)

print(df[(df['sex']== 'female') & (df['pclass']==1) & (df['age'] > 60)])

print(df.loc[500,'age'])

print(df[df['sex']== 'male'])
print(df[(df['sex'] == 'female') & (df['survived']==1)])

print(df[(df['fare'] > 100) & (df['class']== 'First')])
print(df.loc[(df['fare'] > 100) & (df['class']== 'First'),['age','fare','sex']])
print(df.iloc[0:10, 0:4])
print(df.isnull().sum())
print(df['age'].isnull())
print(df['deck'].isnull())
print(df['age'].isnull().sum())

#SORTING
print(df.sort_values('fare'))
print(df.sort_values(['pclass','fare'],ascending=[True, False]))

#GROUPBY
print(df.groupby('class')['fare'].mean())
print(df.groupby('class')['fare'].median())
print(df.groupby('class')['fare'].min())
print(df.groupby('class')['fare'].max())

print(df.groupby('sex')['age'].mean())
print(df.groupby('class')['fare'].max())
print(df.groupby('class')['survived'].sum())


print(df.groupby('class')['survived'].mean()*100)
print(df.groupby('class')['survived'].sum())
print(df.groupby('class').size())

total = df.groupby('class').size()
print(total)
number_of_survivors= df.groupby('class')['survived'].sum()
print(number_of_survivors)
survival_Rate = number_of_survivors/total

print(survival_Rate)

#AGGREGATE

print(df.groupby('class')['fare'].agg(['min','max','mean','median']))

print(df.groupby('class').agg({'age':'mean','fare':'max'}))

print(df.groupby('class').agg({'age':['mean','median'],'fare':['min','max','mean']}))

print(df.groupby('class').agg({'age':['mean','max'],'fare':['mean','max']}))


#print(df.columns)
#print(df['age'])

'''plt.figure(figsize=(8,5))
sns.histplot(df['age'],bins=30)
plt.title('Age Distribution')
plt.show()'''