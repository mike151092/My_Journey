import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,5,11)
y = x**2


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='green',linewidth =3,alpha=0.5,linestyle='--',marker='o',markersize=10,
        markerfacecolor='yellow',markeredgewidth=3,markeredgecolor='red') # can use RGB Hex code for different color, alpha is for transparency
plt.show()