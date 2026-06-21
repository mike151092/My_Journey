import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}

df=pd.DataFrame(d)

print(df)

print(df.dropna(axis=1))
print(df.dropna(thresh=2)) #it will drop rows with 2 or more nan values
print(df.fillna(value="Fill")) # it fills the nan with Fill
print(df.fillna(value=df['A'].mean()))