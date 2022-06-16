import numpy as np
import math

# bai 3,1

# def vecinput():
#     n = int(input("nhap n: "))
#     a = []
#     for i in range(n):
#         x = int(input("nhap a[{}] = ".format(i)))
#         a.append(x)
#     return a
# def vecsum(a):
#     np.sum(a)
#     return a
# def vecinsert(a):
#     x = int(input("nhap vi tri can tren : "))
#     y = int(input("nhap so can tren vao: "))
#     a.insert(x,y)
#     return a
# def vecdel(a):
#     x = int(input("nhap so can xoa: "))
#     del a[x]
#     return a
# def vecdd(a,b):
#     if len(a) == len(b):
#         return np.array(a) + np.array(b)
#     else:
#         return []
#
# a = vecinput()
# b = vecinput()
# print('tong : ',vecsum(a))
# print('chen: ',vecinsert(a))
# print('xoa: ',vecdel(a))
# print(vecdd(a,b))









# bai 3,2

# def nhap():
#     n = int(input("nhap n: "))
#     a = []
#     for i in range(n):
#         x = int(input("nhap a[{}] = ".format(i)))
#         a.append(x)
#     return a
# def mang(a):
#     n = int(input("nhap n: "))
#     m = int(input("nhap m: "))
#     b = []
#
#     if n*m > len(a):
#         print('ko the tao ra dk ma tran ')
#     else:
#         c = 0
#         d = [0]*m
#         for i in range(n):
#             d[i] = a[c*m : c*m +m]
#             b.append(d)
#         return b
#
#         # b = np.reshape(a,(n,m))
#         # return b
# a  = nhap()
# print(a)
# c = mang(a)
# print(c)














# bai 3,3

# def nhap():
#     n = int(input("nhap n: "))
#
#     a = []
#     b = []
#     for i in range(n):
#         x = int(input("nhap a[{}] = ".format(i)))
#         a.append(x)
#     m = int(input("nhap m: "))
#     for i in range(m):
#         x = input("nhap b[{}] = ".format(i))
#         b.append(x)
#     return a, b
#
# def mang(a,b):
#     c = []
#     for i in range(min(len(a),len(b))):
#         c.append(a[i])
#         c.append(b[i])
#     if len(a) > len(b):
#         for i in range(len(a)- len(b)):
#             c.append(a[len(b)+i])
#     if len(b) > len(a):
#         for i in range(len(b) - len(a)):
#             c.append(b[len(a)+ i])
#     return c
#
#
# a, b = nhap()
# print(a)
# print(b)
# c = mang(a,b)
# print(c)










# bai 3,4


# def nhap():
#     n = int(input("nhap n: "))
#     a = []
#     for i in range(n):
#         x = int(input("nhap a[{}] = ".format(i)))
#         a.append(x)
#     m = int(input("nhap m: "))
#     b = []
#     for i in range(m):
#         x = int(input("nhap b[{}] = ".format(i)))
#         b.append(x)
#     return a, b
# def tron_mang(a,b):
#     c = a + b
#     return np.sort(c)
# a, b = nhap()
#
# c = tron_mang(a,b)
# print(c)






# bai 3,5

#
# def mang():
#     n = int(input("nhap n: "))
#     a = []
#     for i in range(n):
#         x = input("nhap a[{}]: ".format(i))
#         a.append(x)
#     return a
#
# def dem(a):
#     b = tuple(i for i in a[:])
#     t = 0
#     for i in b[:]:
#         if i.isdigit() == True:
#             t += 1
#     return t
#
# a = mang()
# b = dem(a)
# print(b)









# bai 3,6

#
# def nhap():
#     n = int(input("nhap n: "))
#     a = []
#     for i in range(n):
#         x = input("nhap a[{}] = ".format(i))
#         a.append(x)
#         b = tuple(a)
#     return b
#
# def tinh(a):
#     t = 0
#     b = tuple(float(i) for i in a[:])
#     for j in b[:]:
#         t += j
#     return t
# a = nhap()
# print(a)
# b = tinh(a)
# print(b)










# bai 3,7

#
# def tap_A():
#     n = int(input('nhap n: '))
#     a = set()
#     for i in range(n):
#         x = int(input("nhap ma sv ban 1 a[{}] = ".format(i)))
#         a.add(x)
#     return a
# def tap_B():
#     m = int(input("nhap m: "))
#     a = set()
#     for i in range(m):
#         x = int(input("nhap ma sv ban 2 a[{}] = ".format(i)))
#         a.add(x)
#     return a
#
# def thong_tin(a,b):
#     if len(a & b) > 0:
#         print(" co sinh vien dang ki ca 2 ban ")
#     else:
#         print('ko co sinh vien nao ')
#
#     print('sinh vien dang ki ca 2 ban la: ', a & b)
#     print("sinh vien dang ki ban 1 ma khong dag ki ban 2: ", a - b)
#
#
#
# a = tap_A()
# b = tap_B()
# print(a)
# print(b)
# print(thong_tin(a,b))










# bai 3,8

#
# Thong_Tin = {
#     2020: 9,
#     2010: 5,
#     2134: 4,
#     2345: 4,
#     1234: 6,
#     3241: 3.4,
#     2234: 1.2,
#     2341: 2
# }

# def tinh(x):
#     t = 0
#     for i in x.values():
#         if i >= 2.5 and i < 3.5:
#             t += i
#     return t
# def them(x):
#     n = int(input("key : "))
#     m = int(input('values :'))
#     x[n] = m
#     return x
# a = Thong_Tin
#
# def xoa(x):
#     for i in x.values():
#         if i < 2:
#             x.pop(x[i])
#     return x
# print(a)
# a = tinh(Thong_Tin)
# print(a)
# b = them(Thong_Tin)
# print(b)
# c = xoa(Thong_Tin)
# print(c)









# bai3,9


# def xau_S():
#     n = input('nhap xau S: ')
#     return n
# def xau_Q():
#     n = input("nhap xau Q: ")
#     return n
# def cac_ham_tinh(S,Q):
#     d = Q.find(S)
#     if d >= 0:
#         print('la ham con')
#     else:
#         print(" ko la ham con")
# def ghep(S,Q):
#     P = S + Q
#     return P
# def thay_the(S):
#     n = input('cum tu can thay the: ')
#     m = input('cum tu thay the: ')
#     S.replace(n,m)
#     return S
# def thay_the_P(S):
#     a = []
#     b = list(S.split())
#     for i in range(len(b)):
#         x = {i:b[i]}
#         a.append(x)
#     return a
# s = xau_S()
# q = xau_Q()
# cac_ham_tinh(s,q)
# P = ghep(s,q)
# a = thay_the(P)
# b = thay_the_P(a)
# print(a)
# print(b)











# bai 3,10


# CONFIG = {
#     'n':  1500,
#     'CLUSTERS': 3,
#     'INTER': 1000,
#     'METHOD': 'DCA CLUSTERING',
#     'MEASURE': 'EUCLIDEAN',
#     'YEARS': 9,
#     'MAX': 200
# }
# print(CONFIG)
# CONFIG['MEASURE'] = 'MANHATAN'


































































