import numpy as np



#bai 5,1

# n = int(input('nhap n: '))
# a = np.random.rand(n)
# print(a)
# def thong_so(x):
#     print(np.ndim(x))
#     print(np.shape(x))
#     print(len(x))
#     print(x.itemsize)
#     print(a.dtype)
# thong_so(a)
# b = np.linspace(1,n,100)
# print(b)
# thong_so(b)
# c = np.arange(1,100,2)
# print(c)
# d = np.ones(100)
# print(d)
# e = np.zeros(100)
# print(e)
# h = np.random.randn(100)
# n = int(input('nhap n: '))
# m = int(input("nhap M:"))
# k = np.ones((n,m))
# print(k)
# p = np.eye(n)
# print(p)
# q = np.diag(a)
# print(q)









#  bai5,2

# def nhap(x, n):
#     b = []
#     for i in range(n):
#         a = int(input(x + "[{}] = ".format(i)))
#         b.append(a)
#     return b
# def tinh(a,b):
#     a = np.array(a)
#     b =  np.array(b)
#     c = a + b
#     return c
# def tinh_pt(a,b):
#     a = np.array(a)
#     b = np.array(b)
#     d = a - b
#     e = a*b
#     f = a / b
#     return d, e, f
# def chan(c):
#     t = 0
#     for i in range(len(c)):
#         if c[i] % 2==0:
#             print(c[i],end='\t')
#             t += c[i]
#     print('\n tong: ',t)
#
#
#
# n = int(input("nhap n: "))
# a = nhap('a',n)
# b = nhap('b',n)
# c = tinh(a,b)
# print(c)
# d, e, f = tinh_pt(a,b)
# print(d)
# print(e)
# print(f)
#
# print(np.sum(c))
# print(np.max(c))
# print(np.min(c))
# print(chan(c))
#
# try:
#     x = int(input("nhap x: "))
#     if n % x != 0:
#         raise ValueError
#     else:
#         y = np.reshape(c,(n,n//x))
#         print(y)
# except:
#     print(EOFError,'xxxx')












# bai 5,3


# def nhap():
#     n = int(input('nhap n: '))
#     a = []
#     for i in range(n):
#         x = int(input("nhap a[{}] = ".format(i) ))
#         a.append(x)
#     return a








































# bai 5,4
# readfile('D:/DATA54.txt.txt')

def file(x):
    n = m =0
    data = []
    with open(x,'r') as f:
        n, m = f.readline().split()

        n = int(n)
        m = int(m)
        for i in range(n):
            k = f.readline().split()
            data.append(k)
        data = np.array(data)
        return n, m, data

def arrsplit(a,n, m):
    x = a[:, :m-1]
    y = a[:, m-1:]
    y = np.reshape(y, -1)
    y = y.astype(int)
    return x, y

def

n, m, data = file('D:\DATA54.txt.txt')
print(n)
print(m)
print(data)
x, y = arrsplit(data,n,m)
print(x)
print(y)



























































