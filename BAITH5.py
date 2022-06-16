import numpy as np








# bai 5,1

#
# n = int(input('nhap n: '))
# a = np.random.rand(n)
# print(a)
# print('so chieu: ',a.ndim)
# print('kich thuoc moi chieu: ',a.shape)
# print('do dai : ',len(a))
# print('... ',a.itemsize)
# print('kieu : ',a.dtype)
#
#
# m = int(input("nhap m: "))
# b = np.linspace(1, m, 100)
# print(b)
# print("so chieu : ",np.ndim(b))
# print('kich thuoc: ',np.shape(b))
# print('do dai: ',len(b))
# print('... ',b.itemsize)
# print('kieu: ',b.dtype)

#
# c = np.arange(0,100,2)
# print(c)
#
# d = np.ones(100)
# print(d)
#
# e = np.zeros(100)
# print(e)
#
# h = np.random.randn(100)
# print(h)
#
# n = int(input('nhap n: '))
# m = int(input('nhap m: '))
# k = np.ones((n,m))
# print(k)
#
# p = np.eye(n)
# print(p)
#
# x = [2,3,4,5]
# q = np.diag(x)
# print(q)














# bai 5,2

#
def mang():
    a = []
    for i in range(10,20):
        x = float(input("nhap a[{}] = ".format(i)))
        a.append(x)
    return a
# def vecto(a,b):
#     x = np.array(a)
#     y = np.array(b)
#     c = x + y
#     return c
#
# def tinh(a,b):
#     x = np.array(a)
#     y = np.array(b)
#     d = x - y
#     e = x*y
#     f = x/y
#     return d,e,f
#
# def tinhc(c):
#     x = np.array(c)
#     tong = sum(x)
#     max = x.max()
#     min = x.min()
#     return tong,max,min
#
# def chan(c):
#     t = 0
#     for i in range(len(c)):
#         if c[i] % 2==0:
#             print(c[i],end='\t')
#             t += c[i]
#     print('\ntong ',t)
#

a = mang()
# b = mang()
# c = vecto(a,b)
# print(c)
# d, e, f = tinh(a,b)
# print(d)
# print(e)
# print(f)
# h,t,g = tinhc(c)
# print(h)
# print(t)
# print(g)
# x = chan(c)
# print(x)
#
# print(len(c))
# try :
#     t = int(input("nhap t: "))
#     if n % t != 0:
#         raise ValueError
#     k = np.reshape(c,(t,len(c)//t))
#     print('ma tran thu dk : \n', k)
# except:
#     print(ValueError,': ko tinh dk')
#
#














# bai 5,3





def mang():
    global n
    n = int(input("nhap n: "))
    a = []
    for i in range(n):
        x = float(input('nhap a[{}] = '.format(i)))
        a.append(x)
    return a
def chuyenmt(a):
    try:
        x = int(input("nhap x: "))
        if n % x != 0:
            raise ValueError
        k = np.reshape(a,(x,n//x))
        print('ma tran : \n', k)
    except :
        print(ValueError,'ko tinh dk')

a = mang()
print(a)
chuyenmt(a)



































































































