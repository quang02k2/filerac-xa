import numpy as np
import matplotlib.pyplot as plt
from functions import *

ram = np.loadtxt('data2.txt',delimiter=',')

x = np.copy(ram)

x[:,1] = x[:,0]

x[:,0] = 1

y = ram[:,1]


[Thenta,j_hist] = GradientDescent(x,y)
predict=predict(x,Thenta) * 10000
plt.figure(1)
plt.plot(x[:,1],y,'rx')

plt.plot(x[:,1],predict/10000,'-b')
plt.figure(2)
plt.plot(j_hist[:,0],j_hist[:,1],'-b')
plt.show()































