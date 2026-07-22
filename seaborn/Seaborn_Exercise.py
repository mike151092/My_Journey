import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
titanic= sns.load_dataset('titanic')

print(titanic.head())

#JOINTPLOT

#sns.jointplot(x='fare',y='age',data=titanic,kind='hex')

#distplot

#sns.distplot(titanic['fare'],kde=False,bins=30,color='green')

#BOXPLOT

#sns.boxplot(x='class', y='age',data = titanic, palette='rainbow')

#swarmplot
#sns.swarmplot(x='class', y ='age', data= titanic, palette='magma')

#COUNTPLOT
#sns.countplot(x = 'sex', data=titanic)

#HEATMAP

#tc=titanic.corr(numeric_only=True)

#sns.heatmap(tc, annot= True, cmap='coolwarm')

#FACETGRID
f = sns.FacetGrid(data=titanic,col='sex')
f.map(plt.hist,'age')

plt.show()