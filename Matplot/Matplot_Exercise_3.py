import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,100)
y = x*2
z = x**2


fig = plt.figure()
ax1 = fig.add_axes([0.05,0.05,0.9,0.9])
ax2= fig.add_axes([0.2,0.5,0.4,0.4])
ax1.set_xlim(left=0,right=99)
ax1.set_ylim(bottom=0,top=9801)
ax1.set_xlabel('X')
ax1.set_ylabel('Z')
ax1.set_title('Outter Plot X VS Z')
ax1.plot(x,z)

ax2.set_xlim(left=20,right=22)
ax2.set_ylim(bottom=30,top=50)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title("Zoomed X VS Y")
ax2.plot(x,y)
plt.show()