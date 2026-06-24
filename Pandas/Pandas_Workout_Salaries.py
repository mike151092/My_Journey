import numpy as np
import pandas as pd

df =pd.read_csv('Salaries.csv')
print(df)
print(df.head())
print(df.info())
print(df['BasePay'].mean())
print(df['OvertimePay'].max())

print(df[df['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle'])
print(df[df['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits'])
print(df[df['TotalPayBenefits']==df['TotalPayBenefits'].max()])
#built in max method
print(df.iloc[df['TotalPayBenefits'].argmax()])
#minimum total pay
print(df[df['TotalPayBenefits']==df['TotalPayBenefits'].min()]) 
#Built in min
print(df.loc[df['TotalPayBenefits'].argmin()])
#mean basepay of all employees

x =df.groupby('Year')
print(x.mean('Year')['BasePay'])

print(df['JobTitle'].nunique())

print(df['JobTitle'].value_counts().head(5))

print(sum(df[df['Year']==2013] ['JobTitle'].value_counts()==1))

def cheift_String(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False

print(sum(df['JobTitle'].apply(lambda x: cheift_String(x))))