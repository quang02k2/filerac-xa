


import sys

import matplotlib.pyplot as plt

import numpy as np
# x = tuple(int(i) for i in range(1,4))
# y = (7,3,5)
# plt.plot(x,y,'--sr')

# [<matplotlib.lines.Line2D object at 0x00000000052C0080>]

# plt.show()








# a = np.array([2,5,1,7])
# b = np.array([5,3,1,8])
# plt.plot(a,b)
# plt.show()




# a = np.array([2,5,1,7])
# b = np.array([5,3,1,8])
# plt.plot(a,b,marker='*')#để nhấn mạnh từng điểm bằng một điểm đánh dấu được chỉ định:
# plt.show()






# a = np.array([2,5,1,7])
# b = np.array([5,3,1,8])
# plt.plot(a,b,marker='*',color='k')
# plt.show()




# a = np.array([2,5,1,7])
# b = np.array([5,3,1,8])
# plt.plot(a,b,marker='*',color='k',ms=12)# ms : để đặt kích thước của các điểm đánh dấu
# plt.show()



# a = np.array([2,5,1,7])
# b = np.array([5,3,1,8])
# plt.plot(a,b,marker='o',color='b',ms=12,mec='r')# mec :để đặt màu cho cạnh của các điểm đánh dấu:
# plt.show()




a = np.array([2,5,1,7])
b = np.array([5,3,1,8])
plt.plot(a,b,marker='o',color='b',ms=12,mec='r',mfc='k')# mfc:để đặt màu bên trong cạnh đánh dấu
plt.show()









































