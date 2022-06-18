import numpy as np
import os
import shutil


# bai4.5

#
# def doc(x):
#     with open(x,mode='r') as f:
#         n,m = map(int,f.readline().split())
#         print(n,' ',m)
#         for i in range(n):
#             print(f.readline().split(),end='')
#
#
# def gan_bien(x):
#     with open(x,mode='r') as f:
#         n,m  = map(int,f.readline().split())
#         a = []
#         for i in range(n):
#             x = f.readline().split()
#             for j in range(m):
#                 x[j] = float(x[j])
#                 a.append(x)
#         a = np.array(a)
#     return n,m, a
#
#
# def sum_0(n,m,a):
#     dem = 0
#     for i in range(n):
#         for j in range(m):
#             if a[i][j] == 0:
#                 dem +=1
#     return dem

#
# def tbc(a,col):
#     k = 0.0
#     for i in range(len(a)):
#         k += a[i][col]
#     return k/len(a[0])
#
#
# def thay_the(n,m,a):
#     for i in range(m):
#         h = tbc(a,i)
#         for j in range(n):
#             if a[j][i] == 0:
#                 a[j][i] = h
#     return a
#
#
# def file(d,a):
#     with open(d,mode='w') as f:
#         f.write(str(len(a)) + ' ')
#         f.write(str(len(a[0])) + '\n')
#         for i in range(len(a)):
#             for j in range(len(a[0])):
#                 f.write(str(a[i][j]) + ' ')
#             f.write('\n')
#
#
#
# def saves(file1, file2,a):
#     with open(file1,mode='w') as f:
#         f.write(str(100) + ' ')
#         f.write(str(len(a[0])) + '\n')
#         for i in range(100):
#             for j in range(len(a[0])):
#                 f.write(str(a[i][j]) + ' ')
#             f.write('\n')
#     with open(file2,mode='w') as f:
#         f.write(str(len(a)-100) + ' ')
#         f.write(str(len(a[0])) + '\n')
#         for i in range(len(a)-100):
#             for j in range(len(a[0])):
#                 f.write(str(a[i][j]) + ' ')
#             f.write('\n')
#
#
# def main():
#     x = 'D:/DATA45.data'
#     n,m,a = gan_bien(x)
#     aa = thay_the(n,m,a)
#     d = 'D:/image2.txt'
#     file(d,a)
#     file1 = 'D:/file1.txt'
#     file2 = 'D:/file2.txt'
#     saves(file1,file2,a)
#     os.mkdir('D:/THUMUC1')
#     shutil.copy('D:/image2.txt','D:/THUMUC1')
#     os.remove('D:/image2.txt')
#
#
# main()





# bai5.1


# n = int(input('nhap n: '))
#
# a = np.random.randn(n)
# print('a',a)
# print('so chieu ',a.ndim)
# print('kich thước mỗi chiều ',a.shape)
# print('do dai : ',len(a))
# print('do dai cau pt : ',a.itemsize)
# print('kieu du lieu a: ',a.dtype)
#
# b = np.linspace(1,n,100)
# print('b: ',b)
# print('so chieu ',b.ndim)
# print('so dai ',len(b))
# print('kich thuoc moi chieu: ',b.shape)
# print('do dai pt : ',b.itemsize)
# print('kieu pt : ',b.dtype)

# c = np.arange(2,201,2)
# print(c)
#
# d = np.ones(100)
# e = np.zeros(100)
# h = np.random.randn(100)
# k = np.zeros((2,3))
# p = np.eye(3)
# q = np.diag(c)




# bai 5.2

#
# def nhap(x,n):
#     a = []
#     for i in range(n):
#         k = int(input('nhap {}[{}]'.format(x,i)))
#         a.append(k)
#     a = np.array(a)
#     return a
#
#
# def mang_2c(c):
#     try :
#         n = int(input('nhap so chieu : '))
#         if len(c) % n != 0:
#             raise ValueError
#         k = c.reshape(n,len(c)//n)
#         print('mang 2 chieu: ',k)
#     except:
#         print('ko thoa man ')
#
# def main():
#     n = int(input('nhap n: '))
#     a = nhap('a',n)
#     b = nhap('b',n)
#     c = a + b
#     d = a - b
#     e = a/b
#     f = a*b
#     sum_c = sum(c)
#     max_c = max(c)
#     min_c = min(c)
#     mag = mang_2c(c)
#
#
# main()





# bai 5.3

#
# def nhap(x):
#     n = int(input('nhap n: '))
#     a = np.random.randn(n)
#     for i in range(n):
#         a[i] = int(input('nhap {}[{}] : '.format(x,i)))
#     return a
#
#
# def chuyen2c(a):
#     try:
#         n = int(input('nhap so chieu: '))
#         if len(a) % n !=0:
#             raise ValueError
#         k = a.reshape(n,len(a)//n)
#         return k
#     except:
#         print('ko co')
#
# def tach(a):
#     b = a[:,:1]
#     c = a[:,1:2]
#     return b,c
#
# def vitri(d):
#     x = []
#     for i in range(len(d)):
#         if d[i] > 1:
#             x.append(i)
#     return x
# def main():
#     k = nhap('a')
#     a = chuyen2c(k)
#     b,c = tach(a)
#     b = np.reshape(b,-1)
#     c = np.reshape(c,-1)
#     d = np.concatenate((b,c))
#     x = vitri(d)
#     dd = np.sort(d)
#     kk = int(input('nhap k: '))
#     vt = np.searchsorted(dd,kk)
#     print('vi tri thich hop de chen: ',vt)
#     ddd = np.insert(dd,vt,kk)
#     print(ddd)
#
# main()




# bai 5.4


def doc(x):
    with open(x,mode='r') as f:
        n,m = map(int,f.readline().split())
        a = []
        for i in range(n):
            k = f.readline().split()
            a.append(k)
        a = np.array(a)
    return n,m,a


def tach(m,a):
    x = a[:,:m-1]
    y = a[:,-1]
    y = np.reshape(y,-1)
    y = y.astype(int)
    return x,y


def khac_y(y):
    k = np.bincount(y)
    d = np.count_nonzero(k)
    print('so phan tu khac nhau: ',d)
    for i in range(len(k)):
        if k[i] !=0:
            print('so lan ',i, 'xua hien ',k[i])


def tbc(x):
    b = np.zeros(len(x[0]))
    for i in range(len(x[0])):
        k = x[:,i]
        k = np.reshape(k,-1)
        d = 0
        for j in range(len(k)):
            if k[j] != '?':
                b[i] += float(k[j])
            else:
                d += 1
        b[i] /= (len(x) - d)
    return b


def thay_the(x,b):
    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i,j] == '?':
                x[i,j] = str(b[j])
    return x


def luu(filex,filey,x,y):
    with open(filex,mode='w') as f:
        f.write(str(len(x)) + ' ')
        f.write(str(len(x[0])) + '\n')
        for i in range(len(x)):
            for j in range(len(x[0])):
                f.write(str(x[i][j]) + '/n')
            f.write('\n')
    with open(filey,mode='w') as f:
        f.write(str(len(y)) + ' ')
        f.write(str(len(y[0])) + '\n')
        for i in range(len(y)):
            for j in range(len(y[0])):
                f.write(str(y[i][j]) + ' ')
            f.write('\n')


def tach_train(x,y,tram):
    n = len(x)
    n_train = int(n*tram)
    n_test = n - n_train
    x_test = []
    y_test = []
    for i in range(n_test):
        pos = np.random.randint(0,n-1)
        k = list(x[pos,:])
        x_test.append(k)
        y_test.append(y[pos])
        x = np.delete(x,pos,0)
        y = np.delete(y,pos,0)
        n = len(x)
    x_train = np.array(x)
    y_train = np.array(y)
    y_test = np.array(y_test)
    x_test = np.array(x_test)
    return  x_train,x_test,y_train,y_test


def main():
    x = 'D:/DATA54.txt'
    n,m,a = doc(x)
    x,y = tach(m,a)
    # print(x)
    # khac = khac_y(y)
    b = tbc(x)
    # print(b)
    thay = thay_the(x,b)
    tram = 70/100
    x1,x2,y1,y2 = tach_train(x,y,tram)
    print(x1,x2)
    print('*'*100)
    print(y1,y1)

main()

