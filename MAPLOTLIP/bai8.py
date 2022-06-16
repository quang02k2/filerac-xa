import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.subplot(1,2,1)
plt.bar(x,y,color='b',width=0.7)

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.subplot(1,2,2)
plt.barh(x,y,color='b',height=0.4)
plt.show()