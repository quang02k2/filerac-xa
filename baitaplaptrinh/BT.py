import math
import numpy as np
import os
import shutil as st

# bài 1


# n = int(input('nhap n: '))
# while n < 0 or n >= 10000:
#     print('ko thoa man ')
#     n = int(input('moi nhap n: '))
#
#
# a = n//1000
# b = (n%1000)//100
# c = (n%100)//10
# d = n%10
# print("{} ngan {} tram {} truc {} don vi ".format(a,c,b,d))







# bai 2

# x1 = int(input('nhap x1: '))
# y1 = int(input('nhap y1: '))
# x2 = int(input("nhap x2: "))
# y2 = int(input("nhap y2: "))
#
# D = math.sqrt((x2-x1)**2 + (y2-y1)**2)
# M = math.fabs((x2-x1)+ (y2-y1))
# C = 1 - (x1*x2 + y1*y2)/(math.sqrt(x1**2 + y1**2)*(x2**2 + y2**2))
#
# print("d: ",D)
# print("m: ",M)
# print("c",round(C,2))


# bai 3

# a = int(input('nhap a: '))
# b = int(input('nhap b: '))
# c = int(input('nhap c: '))
# if a==0:
#     if b==0 and c==0:
#         print('pt vo  so nghiem ')
#     elif b==0 and c!=0:
#         print('pt vo nghiem')
#     else:
#         print('pt co nghiem duy nhat : ',-c/b)
# else:
#     deta = b**2 - 4*a*c
#     if deta==0:
#         print('pt co nghiem kep : ',-b/(2*a))
#     elif deta <0:
#         print('pt vo nghiem ')
#     else:
#         print('nghiem thu nhat : ',(-b+math.sqrt(deta))/(2*a))
#         print("nghiem thu hai : ",(-b-math.sqrt(deta))/(2*a))




# bai 4

# x = float(input('nhap x: '))
# n = int(input('nhap n : '))
# if n%2==0:
#     S = 2016*x + x**n/(pow(3,n-1))
#     print('S :',S)
# else:
#     S = 0
#     print('s', S)



# BAI 5

# n = int(input('nhap n: '))
# while n < 0 or n>10000000:
#     print('ko hop le')
#     n = int(input('moi nhap lai n: '))
# d = True
# for i in range(2, n):
#     if n% i == 0:
#         d = False
# x = True
# if str(n)[::-1] == str(n):
#     x = False
#
# if d :
#     print('hop le')
# else:
#     print('ko hop le')





# bai 2.1
#
def SNT(n):
    while n<0 or n>10000000:
        print('ko phai ')
        n = int(input('moi nhap lai : '))
    d = True
    if n==0 or n==1:
        print('n ko phai la so nguyen to')
    for i in range(2,n):
        if n%i ==0:
            d = False
    return d


def DX(n):
    x = True
    if str(n)[::-1] == str(n):
        x = False
    return x



# bai 2.4

# bai 3.1



# def vecinput(n):
#     a = []
#     for i in range(n):
#         k = print('nhap a[{}] '.format(i))
#         a.append(k)
#     np.array(a)
#     return a
#
# def vecsum(a):
#     tong  = 0
#     for i in range(len(a)):
#         tong += a[i]
#     return tong
#
# def vecinsert(a):
#
#     try:
#         m = int(input('phan tu can chen vao mang: '))
#         g = int(input('vi tri can chen : '))
#         while g < len(a) or g > 0:
#             print('vi tri ko thich hop')
#             g = int(input('nhap lai vi tri can chen : '))
#         else:
#             a.insert(m,g)
#         return a
#     except:
# #         print('ok ko thoa man')
#
#
#
# # bai 3.2
#
# def nhap():
#     n = int(input('nhap n: '))
#     a = []
#     for i in range(n):
#         k = int(input('nhap a[{}]'.format(i)))
#         a.append(k)
#     np.array(a)
#     return a
#
# def tinh(n,m, a):
#     c = []
#     if n*m > len(a):
#         print('ko tinh dk')
#     else:
#         for i in range(n):
#             d = a[m*i: m*i + m]
#             c.append(d)
#     return c
#
# a = nhap()
# n = int(input('nhap n: '))
# m = int(input('nhap m: '))
# d = tinh(n,m,a)
# print(d)




# bai 3.3
import CLASS

#
# def nhap_a():
#     n = int(input('nhap n: '))
#     a = []
#     for i in range(n):
#         k = int(input('nhap a[{}]: '.format(i)))
#         a.append(k)
#     np.array(a)
#     return a
#
# def nhap_b():
#     m = int(input('nhap b : '))
#     b = []
#     for i in range(m):
#         c = input('nhap b[{}] :  '.format(i))
#         b.append(c)
#     return b
#
# def tinh(a,b):
#     c = []
#     for i in range(min(len(a),len(b))):
#         c.append(a[i])
#         c.append(b[i])
#     if len(a) > len(b):
#         for i in range(len(a)-len(b)):
#             c.append((a[len(b)+i]))
#     if len(b) > len(a):
#         for i in range(len(b) - len(a)):
#             c.append((b[len(a) + i]))
#     return c
#
# a = nhap_a()
# b = nhap_b()
# d = tinh(a,b)
# print(d)










# bai 3.4


# def nhap(a,n):
#     x = []
#     for i in range(n):
#         k = int(input('nhap {}[{}]: '.format(a,i)))
#         x.append(k)
#     np.array(x)
#     c = np.sort(x)
#     return c
#
# def tinh(a,b):
#     c= []
#     i = 0
#     j = 0
#     while i < len(a) and j < len(b):
#         if a[i] < b[j]:
#             c.append(a[i])
#             i += 1
#         else:
#             c.append(b[j])
#             j += 1
#     if i < len(a):
#         for t in range(i, len(a)):
#             c.append(a[t])
#     if j < len(b):
#         for t in range(j ,len(b)):
#             c.append(b[t])
#     return c
#
#
# n = int(input('nhap n: '))
# m = int(input('nhap m: '))
# a = nhap('a',n)
# b = nhap('b',m)
# d = tinh(a,b)
# print(d)






# bai 3.3


# def nhap():
#     n = int(input('nhap a: '))
#     a = []
#     for i in range(n):
#         k = input('nhap a[{}] : '.format(i))
#         a.append(k)
#     np.array(a)
#     return a
#
# def chuyen_b(a):
#     b = tuple(a)
#     return b
#
# def tinh(b):
#     dem = 0
#     for i in b:
#         if i.isdigit():
#             dem += 1
#     return dem
#
# a = nhap()
# b = chuyen_b(a)
# c = tinh(b)
# print(c)






# bai 3.6

#
# a = ('23','67','89','1001')
#
# b = tuple(float(i) for i in a[:])
#
# tbc = sum(b)/len(b)
# print(tbc)


# bai3.7

# def  nhap(a):
#     n = int(input('nhap n: '))
#     s = set()
#     for i in range(n):
#         k = input('{} s[{}] : '.format(a,i))
#         s.add(k)
#     return s
#
# A = nhap('sinh vien dang ki ban 1')
# B = nhap('sinh vien dang ki ban 2')
# print('sinh vien dang ki 2 ban: ',A|B)
# print('sinh vien dang ki ca hai ban: ',A&B)
# print('sinh vien dang ki ban 1 ko dang ki ban 2: ',A-B)







# bai 3.8

#
# def nhap():
#     n = int(input('nhap n: '))
#     d = dict()
#     a = 0
#     while True:
#         key = input('nhap ma sinh vien: ')
#         value = float(input('nhap diem : '))
#         d[key] = value
#         a += 1
#         if a==n:
#             break
#     return d
#
# def tk(d):
#     dem = 0
#     for i in d.values():
#         if 2.5 <= i <= 3.5:
#             dem += 1
#     return dem
#
#
# def bosung(d):
#     x = input('nhap ma sinh vien moi: ')
#     y = float(input('nhap diem : '))
#     d[x] = y
#     return d
#
# def xoa(d):
#     a = {}
#     for i in d.keys():
#         if d[i] < 2:
#             a[i] = d[i]
#     return d
#
#
#
# d = nhap()
# b = tk(d)
# print(b)
# c = bosung(d)
# print(c)
# x = xoa(d)
# print(x)






# bai 3.9


# def nhap():
#     s = input('nhap sau ki tu  :')
#     return s
#
# def sau_con(s,q):
#     if s.find(q) > 0:
#         print('la sau con')
#     else:
#         print('ko la sau con')
#
# def ghep(s,q):
#     x = s + q
#     return x
#
# def thay_the(x):
#     x = x.replace('ha','Ba')
#     return x
#
# def tach(x):
#     d = dict()
#     l = x.split()
#     for i in range(len(l)):
#         d[i] = l[i]
#     return d
#
# s = nhap()
# q = nhap()
# g = sau_con(s,q)
# print(g)
# x = ghep(s,q)
# print(x)
# n = thay_the(x)
# print(n)
# h = tach(n)
# print(h)





# bai 3.10

# CONFIG = {
#     'n' : 1500,
#     'CLUSTERS' : 3,
#     'ITER' : 1000,
#     'METHOD' : 'DCA CLUSTERING',
#     'MEASURE' : 'ECULIDEAN',
#     'YEARS' : 9,
#     'MAX' : 200
# }
# print(CONFIG)
#
# CONFIG['MEASURE'] = 'MANHATAN'
# print(CONFIG['METHOD'])
# CONFIG['LOSS FUNCTION'] = 'SORT MAX'
# print(CONFIG)
# del CONFIG['YEARS']
# print(CONFIG)
# s = input('nhap sau s: ')
# d = 0
# if s in CONFIG.keys():
#     d += 1
# if d>0:
#     print('co trung')
# else:
#     print('ko trung')
#
# xx = set()
# for i in CONFIG.values():
#     xx.add(i)
# print(xx)

# lst = []
# for i in CONFIG.values():
#     lst.append(i)
# print(lst)



# bai 4.1

#
# def nhap():
#     n = int(input('nhap so dong: '))
#     m = int(input('nhap so cot: '))
#     a = []
#     for i in range(n):
#         x = np.zeros(m)
#         for j in range(m):
#             x[j] = float(input('nhap a[{}][{}] : '.format(i,j)))
#             a.append(x)
#     return a
#
# def tinh(a,f):
#     with open(f,mode='w',encoding='utf-8') as f:
#         f.write(str(len(a)))
#         f.write('\t')
#         f.write(str(len(a[0])))
#         f.write('\n')
#         for i in range(len(a)):
#             for j in range(len(a[0])):
#                 f.write(str(a[i][j]) + ' ')
#             f.write('\n')
#
#
# a = nhap()
# tinh(a,'D:\BAIMOI.txt')











# bai 4.2

# def doc(x):
#     with open(x,mode='r', encoding='utf-8') as f:
#         n, m = map(int,f.readline().split())
#         print(n, m)
#         for i in range(n):
#             print(f.readline(), end='')
#
#
# def doc_het(x):
#     with open(x,mode='r',encoding='utf-8') as f:
#         n,m = map(int,f.readline().split())
#         a = []
#         for i in range(n):
#             k = f.readline().split()
#             for j in range(m):
#                 k[j] = float(k[j])
#             a.append(k)
#         np.array(a)
#     return n,m,a
# print('*'*20)
# doc('D:\BAIMOI.txt')
# n, m, a = doc_het('D:\BAIMOI.txt')
# print(a)











# bai 4.3


# def doc(x):
#     with open(x,mode='r',encoding='utf-8') as f:
#         n,m = map(int,f.readline().split())
#         a = []
#         for i in range(n):
#             k = f.readline().split()
#             for j in range(m):
#                 k[j] = float(k[j])
#             a.append(k)
#         np.array(a)
#     return n,m,a
#
# def tbc(a):
#     dem = 0
#     x = []
#     for i in range(len(a[0])):
#         for j in range(len(a)):
#             dem += a[j][i]
#         g = dem/len(a)
#         x.append(g)
#     return x
# print('*'*30)
# n,m,a = doc('D:\BAIMOI.txt')
# print(a)
# b = tbc(a)
# print(b)








# bao 4.4

# os.mkdir('D:\BAIMOI1')
# st.copy('D:/x.txt','D:/BAIMOI1')
# os.rename('D:/BAIMOI1/x.txt','D:/BAIMOI1/x.dat')
# os.chdir('D:/BAIMOI1')
# file = os.listdir()
# for file in file:
#     print(file)
# os.remove('x.xtx')
# os.chdir('D:/')
# st.rmtree('BAIMOI1')













# BAI 4.5

#
# def doc(x):
#     with open(x,mode='r',encoding='utf-8') as f:
#         n,m = map(int, f.readline().split())
#         print(n,  m)
#         for i in range(n):
#             print(f.readline().split(),end='')
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
# def tbc(a):
#     x = []
#     dem = 0
#     for i in range(len(a[0])):
#         for j in range(len(a)):
#            dem += a[j][i]
#         g = dem/len(a)
#         x.append(g)
#     np.array(x)
#     return x
#
# def tinh(a,tbc):
#     dem = 0
#     for i in range(len(a[0])):
#         for j in range(len(a)):
#             if a[j][i] == 0:
#                 dem += a[j][i]
#                 a[j][i] = tbc(i)
#     return a
#







# bai 5.4
#
#
# def doc(x):
#     with open(x,mode='r',encoding='utf-8') as f:
#         n, m = map(int,f.readline().split())
#         a = []
#         for i in range(n):
#             k = f.readline().split()
#             for j in range(m):
#                 k[j] = float(k[j])
#             a.append(k)
#         np.array(a)
#     return n, m, a
#
# def tach(a,n,m):
#     x = a[:,:m-1]
#     y = a[:,-1]
#     y = np.reshape(y,-1)
#     y = y.astype(int)
#     return x,y
#
# def khac(y):
#     d = 0
#     dem = 0
#     c = 0
#     for i in range(len(y)):
#         d = y[i]
#         if d != y[i] :
#             dem += 1
#             c += y[i].count()
#     return d,c
#
# x = 'D:/DATA54.txt'
# n, m, a = doc(x)
#
# x,y = tach(a,n,m)
# d,c = khac(y)
# print(d,c)
#





