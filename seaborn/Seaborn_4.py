#Grids

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

iris=sns.load_dataset('iris')
tips = sns.load_dataset('tips')
print(iris.head())

#g = sns.PairGrid(iris)

#g.map_diag(sns.displot)
#g.map_upper(plt.scatter)
#g.map_lower(sns.kdeplot)
f = sns.FacetGrid(data=tips,col='time',row='smoker')

f.map(plt.scatter,'total_bill','tip')

plt.show()