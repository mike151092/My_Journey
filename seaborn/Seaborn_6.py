#seting style and color with seaborn

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')


#plt.figure(figsize=(12,3))
#sns.set_context('poster',font_scale=2)
#sns.countplot(x='sex',data=tips)
#sns.set_style('ticks')

sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='seismic')


plt.show()