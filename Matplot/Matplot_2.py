import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0,5,11)
y = x**2

#subplot using object oriented
'''fig,axes =plt.subplots(nrows=1,ncols=2) #the subplot handles fig.add_axes automatically based on the no of rows and columns
axes[0].plot(x,y)
axes[0].set_title('First Plot')
axes[1].plot(y,x)
axes[1].set_title('Second Plot')


plt.show()


#figure size and DPI

fig=plt.figure(figsize=(3,3),dpi=500)
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y)
plt.show()
'''
fig= plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(x,y, label='First plot')
ax.set_xlim(0,5)
ax.set_ylim(0,25)
ax.legend()
plt.show()