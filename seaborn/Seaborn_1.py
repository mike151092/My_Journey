import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head())

#distrubution plot
'''sns.displot(tips['total_bill'],kde=False,bins=20)
plt.show()

#joint plot
sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')
plt.show()



#PairPlot used to plot relationship between the numerical data
sns.pairplot(tips,hue='sex',palette='coolwarm')
plt.show()
'''
#RUG Plot (Similar to histogram)
sns.rugplot(tips['total_bill'])
plt.show()