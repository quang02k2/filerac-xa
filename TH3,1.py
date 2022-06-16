import numpy as np




# def nhap():
#     n = int(input('nhap n: '))
#     a = []
#     for i in range(n):
#         x = int(input(f'nhap a[{i} = '))
#         a.append(x)
#     return a
# def tinh(a):
#     n = int(input('nhap n: '))
#     m = int(input('nhap m: '))
#     b = []
#     if n*m > len(a):
#         print('ko tinh dk')
#     else:
#         c = 0
#         d = [0]*m
#         for i in range(n):
#             d[i] = a[c*m : c*m + m]
#             c +=1
#             b.append(d)
#     return b
# a = nhap()
# b = tinh(a)
# print(b)


# def nhap():
#     n = int(input('nhap n: '))
#     a = []
#     for i in range(n):
#         x = int(input(f'nhap a[{i} = '))
#         a.append(x)
#     return a
#
# def nhapb():
#     n = int(input('nhap n: '))
#     a = []
#     for i in range(n):
#         x =input(f'nhap a[{i} = ')
#         a.append(x)
#     return a
#
# def tinh(a,b):
#     c = []
#     for i in range(min(len(a),len(b))):
#         c.append(a[i])
#         c.append(b[i])
#     if len(a) > len(b):
#         for i in range(len(a)-len(b)):
#             c.append(a[len(b) + i])
#     if len(a) < len(b):
#         for i in range(len(b)-len(a)):
#             c.append(b[len(a)+ i])
#     return c
# a = nhap()
# b = nhapb()
# c = tinh(a,b)
# print(c)

# n = int(input(" nhap n: "))
# a = []
#
# for i in range(n):
#     print(" nhap phan tư: ", i, end=": ")
#     x = int(input())
#     a.append(x)
#
# A = np.array(a)
#
#
# b = sum(a)
# print("tong cac phan tu trong mang: ", b)
#
# x = int(input("nhap vi tri can chen vao: "))
# y = input("nhap ki tu hoac so can tren vao: ")
# a.insert(x, y)
# print(' sau khi tren ta dk: ', a)
#
# z = int(input("nhap vi tri can xoa: "))
# a.pop(z)
# print("sau khi mang a xoa: ", a)
#
# m = int(input(" nhap m: "))
# c = []
#
# for i in range(m):
#     print(" nhap phan tư: ", i, end=": ")
#     y = int(input())
#     c.append(y)
# C = np.array(c)
#
# tong = []
# hieu = []
# def TINH(a, c):
#     if len(a) == len(c):
#         tong = A + C
#         hieu = A - C
#
#         return tong, hieu
#     else:
#         print("ko tinh dk ")
#         return []
#
# print(" ket qua tra ve : ", TINH(a,c))


