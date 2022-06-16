import matplotlib.pyplot as plt
import numpy as np

a = np.array([2,3,5,1,7])
b = np.array([4,2,7,9,1])
plt.figure(2)
plt.plot(a,b,color='r',mfc='r',ms=10,mec='k',marker='*')
plt.figure(1)
plt.plot(a,b,linestyle='-.',linewidth='10.8')
plt.show()











