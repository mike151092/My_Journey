#series in pandas
import numpy as np
import pandas as pd 

Labels =['a','b','c']
my_data =[10,20,30]
my_array=np.array(my_data)
my_dict={'a':10,'b':20,'c':30}

print(pd.Series(data=my_data)) #in series we can choose the index of the data

print(pd.Series(data=my_data,index=Labels))

ex_dict = pd.Series(my_dict)

print(ex_dict)

#grabing informations from series using pandas
my_series_1 = pd.Series([1,2,3,4],['Madurai','Thoothukudi','Chennai','Coimbatore'])
print(my_series_1)

my_series_2= pd.Series([1,2,6,8],['Trichy','Thoothukudi','Chennai','Coimbatore'])
print(my_series_2)

print(my_series_1['Madurai'])