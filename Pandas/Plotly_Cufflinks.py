import pandas as pd
import numpy as np
import chart_studio.plotly as py
from plotly import __version__
import cufflinks as cf 
from plotly.offline import download_plotlyjs, init_notebook_mode,plot, iplot
init_notebook_mode(connected=True)
cf.go_offline()
import matplotlib.pyplot as plt


#Data
df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())

print(df.info())
print(df.describe())

df2=pd.DataFrame({'Category':['A','B','C'],'Values':[32,43,50]})

print(df2)

#CUFFLINKS AND IPLOT 

#it does not work because we are using higher numpy, plotly version hence cufflink fails

#df.iplot(kind='scatter',x='A',y='B',mode='markers',colors= '#ff0000')
#df.iplot(kind='box',colorscale='ylorbr',color='#ff0000')
#df.iplot(kind='bubble')

#df.scatter_matrix()
plt.show()