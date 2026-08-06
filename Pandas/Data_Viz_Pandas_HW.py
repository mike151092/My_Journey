import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('df3')

#print(df.head())

#scatter plot
#df.plot.scatter(x='a',y='b',c='red')

#histogram
#df.plot.hist(x='a',bins=30)
#df['a'].plot.hist(bins=30)
#plt.style.use('ggplot')
#df['a'].plot.hist(bins=25,alpha=0.5)

#box plt
#df.plot.box(column=('a','b'))

#KDE Plot
#df['d'].plot.kde(lw=5,ls='--')

#Area plot
df[0:30].plot.area(alpha=0.4)

plt.show()