import numpy as np
import matplotlib.pyplot as plt
from functions import *

ram = np.loadtxt('data.txt',delimiter=',')

y = ram[:,2]

x = np.zeros((np.size(y),np.size(ram,1)))

x[:,0] = 1

x[:,1:] = ram[:,0:2]


Thenta = np.array([2303230,2,3])
print(computeCost(x,y,Thenta),computerCOST_VEC(x,y,Thenta))

plt.plot(computeCost(x,y,Thenta),computerCOST_VEC(x,y,Thenta),color='k')
plt.show()






















