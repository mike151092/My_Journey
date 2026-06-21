import numpy as np
import pandas as pd

data={'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
      'Person':['Mike','Serene','Vinodh','Lydia','Raj','Dorthy'],
      'Sales':[200,400,500,700,250,600]}

df = pd.DataFrame(data)
print(df)

x = df.groupby('Company')
print(x)
print(x.mean('Sales'))
print(df.groupby('Company').describe())