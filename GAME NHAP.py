import numpy as np
import timeit
import matplotlib.pyplot as plt
import math as m


# def nhap():
#     a = []
#     for i in range(10):
#         x = int(input('nhap [{}] = '.format(i)))
#         a.append(x)
# x = nhap()
# y = nhap()

# x = np.array([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5])
# y = np.array([20, 30, 10, 40, 20, 30, 20, 10, 40, 50])
# plt.subplot(121)
# plt.plot(x,y)
#
#
#
# a = np.linspace(-10,10,100)
# b = 3*a*a*a - 3*a*a + 3*a -3
# plt.subplot(122)
# plt.plot(a,b)
# plt.show()







x = np.linspace(-10,10,100)
y = np.linspace(0,1,100)
for i in range(len(x)):
    print(x[i], ' ',m.sin(x[i]))
    y[i] = m.sin(x[i])
plt.subplot(121)
plt.plot(x,y,color='red')
plt.show()














