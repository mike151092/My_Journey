#Categorical plots
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

tips=sns.load_dataset('tips')

tips.head()

#sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std) # we can add any function to the estimator

#sns.countplot(x='sex',data=tips) #no y axis can be specified here. it is reserved for the count data

#sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker')

#sns.violinplot(x='day',y='total_bill',data=tips)

#sns.stripplot(x='day',y='total_bill',data=tips,hue='sex')

#sns.swarmplot(x='day',y='total_bill',data=tips,hue='sex') #not good for largedata set




plt.show()