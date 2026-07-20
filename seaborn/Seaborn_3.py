#matrix plot with Seaborn

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

tips=sns.load_dataset('tips')
flights=sns.load_dataset('flights')

print(flights.head())
tc=tips.corr(numeric_only=True)

#sns.heatmap(tc,annot=True,cmap='coolwarm')
fp = flights.pivot_table(index='month',columns='year',values='passengers')

#sns.heatmap(fp)
#sns.clustermap(fp)

plt.show()