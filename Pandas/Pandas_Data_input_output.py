import numpy as np
import pandas as pd

df =pd.read_csv('example.csv')

print(df)

df.to_csv('My_Output', index=False) #index is False means that index will not be saved as a column

df1 = pd.read_csv('My_Output')

print(df1)

df2 =pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet1')

#print(df2)
df.to_excel('Excel_Sample2.xlsx',sheet_name='NewSheet',index=False)

df3 = pd.read_excel('Excel_Sample2.xlsx',sheet_name='NewSheet')
print(df3)

data = pd.read_html('https://www.fdic.gov/bank-failures/failed-bank-list')

print(type(data)) #list of data

#print(data)

print(data[0].head()) # this the data neeed

from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')

df.to_sql('my_table',engine)

sqldf = pd.read_sql('my_table', con=engine)

print(sqldf)