import numpy as np


# n = int(input("nhap n: "))
# a = []
# for i in range(n):
#     b = int(input("nhap gia tri a[{}] = ".format(i)))
#     a.append(b)
# print(a)
# print('tong cac phan tu mang: ', len(a))
#
# # d = a.remove(2)
#
# m = int(input("nhap n: "))
# b = []
# for i in range(m):
#     l = int(input("nhap gia tri a[{}] = ".format(i)))
#     b.append(l)
# print(b)
#
#
# def tinh(x, y):
#     if len(x) == len(y):
#         tong = x + y
#         hieu = x - y
#         return tong, hieu
#     else:
#         return []
#
#
# xx = np.array(a)
# yy = np.array(b)
# g = tinh(xx,yy)
# print("tinh tong va hieu :", g)





# #bai3,4
# import numpy as np
#
# a = []
# n = int(input("nhap n :"))
# b = []
# m = int(input("nhap m : "))
# for i in range(n):
#     x = int(input("nhap a[{}] = ".format(i)))
#     a.append(x)
# print(a)
# for j in range(m):
#     x = int(input("nhap b[{}] = ".format(j)))
#     b.append(x)
# print(b)
#
# # def sapsep(x,y):
# #     x.sort()
# #     y.sort()
# #     d = x + y
# #     return d.sort()
# # c = sapsep(a,b)
# # print(c)
#
# a.sort()
# b.sort()
# c = a + b
# c.sort()
# print(set(c))











# bai 3.5
import numpy as np

n = int(input("nhap n: "))
a = []
for i in range(n):
    x = input("nhap a[{}] = ".format(i))
    a.append(x)
print(a)
b = tuple(a)
print(b)
# b = ()
# for i in range(len(a)):
#     b = tuple(a[i])
c = np.array(b)
print(c)
# def hai(x):
#     for j in range(len(x)):
#         if x[j] == str(x):
#             print( 'ko co')
#         elif x[j] % 2 ==0 or x[j]%2==1:
#             print("co ra")
#     return x
# print(hai(c))


































































































