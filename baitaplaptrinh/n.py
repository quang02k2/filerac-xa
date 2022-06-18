import os
import shutil as st

import numpy as np



# n = int(input('nhap n: '))
# while n < 0 or n>10000000:
#     print('ko hop le')
#     n = int(input('moi nhap lai n: '))
# d = True
# for i in range(2, n):
#     if n% i == 0:
#         d = False
# x = True
# if str(n)[::-1] != str(n):
#     x = False
#
# if d and x:
#     print('hop le')
# else:
#     print('ko hop le')

#
#
# def doc(x):
#     with open(x,mode='r',encoding='utf-8') as f:
#         n,m = map(int, f.readline().split())
#         print(n,  m)
#         for i in range(n):
#             print(f.readline(),end='')
#
#
#
# def gan_bien(x):
#     with open(x,mode='r',encoding='utf-8') as f:
#         n, m =map(int, f.readline().split())
#         a = []
#         for i in range(n):
#             k = f.readline().split()
#             for j in range(m):
#                 k[j] = float(k[j])
#             a.append(k)
#         np.array(a)
#     return n, m, a
#
#
# def tbc(a,col):
#
#     dem = 0
#     for j in range(len(a)):
#        dem += a[j][col]
#     g = dem/len(a)
#     return g
#
# def tinh(a):
#     dem = 0
#     b = []
#     for i in range(len(a[0])):
#         t = tbc(a,i)
#         for j in range(len(a)):
#             if a[j][i] == 0:
#                 dem += a[j][i]
#                 a[j][i] = t
#         b.append(a)
#
#     return b
#
#
# def file(a,x,y):
#     with open(x,mode='w',encoding='utf-8') as f:
#         f.write(str(100) + ' ')
#         f.write(str(len(a[0])) + '\n')
#         for i in range(len(a)):
#             for j in range(len(a[0])):
#                 f.write(str(a[i][j])+ ' ')
#             f.write('\n')
#     with open(y,mode='w',encoding='utf-8') as f:
#         f.write(str(len(a)-100) + ' ')
#         f.write(str(len(a[0])) + '\n')
#         for i in range(101,len(a)):
#             for j in range(len(a[0])):
#                 f.write((str(a[i][j])) + ' ')
#             f.write('\n')
#
#
# x = 'D:/image.data'
# doc(x)
#
# n, m, a = gan_bien(x)
#
# b = tinh(a)
# print('*'*30)
# print(b)
#
# x1= 'D:/OK4.txt'
# y1= 'D:OK5.txt'
# a = file(a,x1,y1)
# os.mkdir('D:/OKBAI4.5')
# st.copy(x1,'D:/OKBAI4.5')
# st.copy(y1,'D:/OKBAI4.5')
# os.remove(x1)
# os.remove(y1)


def doc(x):
    with open(x,mode='r',encoding='utf-8') as f:
        n, m = map(int,f.readline().split())
        a = []
        for i in range(n):
            k = f.readline().split()
            a.append(k)
        a = np.array(a)
    return n, m, a

def tach(a,m):
    x = a[:,: m-1]
    y = a[:,m-1]
    y = np.reshape(y,-1)
    y = y.astype(int)
    return x,y

def khac(y):
    d = np.count_nonzero(y)
    k = np.bincount(y)
    print('so phan tu khac nhau : ',d)
    for i in range(len(k)):
        print(f'phan tu {i} suat hien {k[i]} lan')

def tbc(x):
    b = np.zeros(len(x[0]))
    for i in range(len(x[0])):
        k = x[:,i]
        k = np.reshape(k,-1)
        d = 0
        for j in range(len(x)):
            if k[j] == '?':
                d += 1
            else:
                b[i] += float(k[j])
        b[i] /= (len(x) -d)
    return b


def thaythe(x,tbc):
    for j in range(len(x[0])):
        for i in range(len(x)):
            if x[i, j] == "?":
                x[i, j] = str(tbc[j])
    x = x.astype(float)
    return x


def chia(x,y,type):
    n = len(x)
    n_train = int(n*type)
    n_test = n - n_train
    x_test = []
    y_test = []
    for i in range(n_test):
        pop = np.random.randint(0,n-1)
        k = list(x[pop,:])
        x_test.append(k)
        y_test.append(y[k])
        x = np.delete(x,pop,0)
        y = np.delete(y,pop,0)
        n = len(x)
    x_train = np.array(x)
    y_train = np.array(y)
    x_test = np.array(x_test)
    y_test = np.array(y_test)
    return x_train,x_test,y_train,y_test

x = 'D:/DATA54.txt'
n, m, a = doc(x)

xx,y = tach(a,m)
print(xx)
print(y)
d = khac(y)
print(d)
tbc = tbc(xx)
print(tbc)
print('qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq')
aa = thaythe(xx,tbc)
print(aa)

#








