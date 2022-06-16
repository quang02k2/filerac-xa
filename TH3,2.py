import numpy as np
import sys
# n = int(input("nhap so phan tu: "))
# a = []
# for i in range(n1):
#     print("nhap so phan tu: ", i, end=":")
#     k = int(input())
#     a.append(k)
# print(a)
# n = int(input("n="))
# a = [0]*n
# for i in range(n):
#     a[i] = int(input("a[{}]=".format(i)))

n = int(input("n="))
m = int(input("m="))
b = []
def mang(x):
    for i in range(n):
        k = [0]*m
        for j in range(m):
            k[j] = float(input("b[{}][{}] = ". format(i, j)))
        b.append(k)
    return x
d = mang(b)
print(d)
# if n * m <= len(a):
#     for i in range(n):
#         a = [0] * m
#         for j in range(m):
#             a[j] = float(input("b[{}][{}] = ".format(i, j)))
#         b.append(a)
# else:
#     print(" ko the say ma tran ")
#
# print(b)
c = []
ad = []
if len(a) < n * m:
    sys.exit()
else:
    for i , x in enumerate(a):
        ad.append(x)
    if i % m == m - 1:
        c.append(ad)
        ad.clear()
print(c)










