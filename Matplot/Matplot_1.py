import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y= x ** 2

print(x)
print(y)

#functional
'''
plt.plot(x,y)
plt.grid(True)
plt.xlabel('Distance')
plt.ylabel('Exponents')
plt.title('Learning Matplot')
plt.show()

#subplot
plt.subplot(1,2,1)
plt.plot(x,y,'r')
plt.grid(True)
plt.subplot(1,2,2)
plt.plot(y,x,'b')
plt.grid(True)
plt.show()
'''

#Object oriented
fig = plt.figure()
axes =fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.grid(True)
axes.set_xlim(left=0)
axes.set_xlim(right=5)
axes.set_ylim(bottom=0)
axes.set_ylim(top=25)
axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_title('Learning Matplot')
plt.show()