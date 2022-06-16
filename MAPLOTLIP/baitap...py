import matplotlib.pyplot as plt
import numpy as np
import math as mt
import cv2
import os

# x = np.random.randn(10)
# y = np.random.randn(10)
#
# plt.subplot(1, 2, 1)
# plt.plot(x, y)
#
# plt.subplot(1, 2, 2)
#
# def nhap():
#     x = []
#     y = []
#     for i in range(-10, 11):
#         x.append(i)
#     for i in range(-10,11):
#         a = 3*pow(i, 3) - 3*pow(i, 2) + 3*i - 3
#         y.append(a)
#     return x, y
# x, y = nhap()
# plt.plot(x,y)
# plt.show()














#
# def nhap():
#     x = []
#     y = []
#     for i in range(-10, 11):
#         x.append(i)
#         a = mt.sin(i)
#         y.append(a)
#     return x,y
# x,y = nhap()
# plt.plot(x,y,ms=5,color='k',marker='*',mfc='r')
# plt.grid(axis='y')
# plt.show()







# a = np.loadtxt('DATA63.txt')
#
# x = a[0]
# y = a[1]
#
# sizes = np.array([100,200,10,500,20,60,350,50,7,20,50,80])
# plt.scatter(x,y,s=sizes,alpha=0.5)
# plt.title('SCATTER CHART')
# plt.xlabel('trục x')
# plt.ylabel('trục y')
# plt.grid(axis='y')
# plt.show()











#
# a = np.loadtxt('DATA63.txt')
# x = a[0]
# y = a[1]
# plt.subplot(1,3,1)
# plt.bar(x,y,width=0.9)
# plt.title('Bar chart')
# plt.subplot(1,3,2)
# plt.hist(y)
# plt.title('HISTOGRAM CHART')
# plt.subplot(1,3,3)
# plt.pie(y)
# plt.title('PIE CHART')
# plt.show()








# x  = [' nhãn',' xoài', ' dứa', 'chuối', ' cam', ' bưởi']
# y = [5800, 3200, 1200, 1700, 2400, 980]
# a = [0.2,0.1,0.2,0.2,0.15,0.1]
#
#
# def tb(x,y):
#     a = 100*x/np.sum(y)
#     return a
#
# d = []
# for i in y:
#     c = tb(i,y)
#     d.append(c)
#
#
# plt.pie(d,labels=x, explode=a,autopct='%1.2f')
# plt.title('BIỂU ĐỒ SẢN LƯỢNG 2022')
# plt.show()
















