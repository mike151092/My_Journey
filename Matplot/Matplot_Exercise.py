import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,100)
y = x*2
z = x**2

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y)
ax.set_xlim(left=0,right=100)
ax.set_ylim(bottom=0,top=200)
ax.grid(True)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Plotting Exercise')
plt.show()