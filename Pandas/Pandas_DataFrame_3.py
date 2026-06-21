import numpy as np
import pandas as pd

#Index Levels
outside=['G1','G1','G1','G2','G2','G2']
inside=[1,2,3,1,2,3]
hier_index=list(zip(outside,inside))
hier_index= pd.MultiIndex.from_tuples(hier_index)

print(hier_index)

df =pd.DataFrame(np.random.randn(6,2),hier_index,['A','B'])

print(df)

x= df.loc['G1']
print(x)
y=df.loc['G1']['A']
print(y)

df.index.names=['Groups','Numbers']
print(df)

print(df.loc['G2']['B'][2])
print(df.loc['G1']['A'][3])

#Cross section
print(df.xs(1,level='Numbers'))