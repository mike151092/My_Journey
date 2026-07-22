#Regression plots (plot linear model with seaborn)
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

#sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','v'])

sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex', aspect=0.6)

plt.show()