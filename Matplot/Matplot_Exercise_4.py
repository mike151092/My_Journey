import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,100)
y = x*2
z = x**2


fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x,y,color="blue", lw=3, ls='--')
axes[1].plot(x,z,color="red", lw=3, ls='-')
plt.show()