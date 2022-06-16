import numpy as np


# bai 4,1


def matran():
    n = int(input("nhap n: "))
    m = int(input("nhap m: "))
    a = []
    for i in range(n):
        x = [0]*m
        for j in range(m):
            x[j] = int(input("nhap a[{}][{}] = ".format(i,j)))
            a.append(x)
    return a
def file(a):
    f = open('D:\VUI THOI.txt.txt', mode='w')
    f.write(str(len(a)) + ' ')
    f.write(str(len(a[0])) + '\n')
    for i in range(len(a)):
        for j in range(len(a[0])):
            f.write(str(a[i][j]) + " ")
        f.write('\n')
    f.close()

a = matran()
print(a)
file(a)










# bai 4,2


def file():
    with open('D:\VUI THOI.txt.txt','r') as f:
        a = f.read()
        print(a)
a = file()
def gan(x):
    a = []
    n = m = 0
    with open(x,mode='r') as f:
        n,m = f.readline().split()
        n = int(n)
        m = int(m)
        a = []
        for i in range(n):
            x = f.readline().split()
            for j in range(len(x)):
                x[j] = int(x[j])
            a.append(x)
    return n,m,a

gan('D:\VUI THOI.txt.txt')
n, m, b = gan('D:\VUI THOI.txt.txt')
print(n)
print(m)
print(b)












# bai 4,3: chua cau cuoi

#
def doc(x):
    with open(x, mode='r', encoding='utf-8') as f:
        a = f.readline()
        b = f.read()
    return a,b


def docmang(x):
    n = m = 0
    a = []
    with open(x,'r') as f:
        n, m = f.readline().split()
        n = int(n)
        m = int(m)
        a = []
        for i in range(n):
            k = f.readline().split()
            for j in range(len(k)):
                k[j] = float(k[j])
            a.append(k)
    return n,m,a

def tbc(a,n,m):
    t = 0
    for i in range(n):
        for j in range(m):
            t += a[i][j]
    return t/n
doc('D:\Iris.txt.txt')
x = doc('D:\Iris.txt.txt')
y = doc('D:\Iris.txt.txt')
docmang('D:\Iris.txt.txt')
n, m, a = docmang('D:\Iris.txt.txt')
print(n)
print(m)
print(a)
c = tbc(a,n,m)
print(c)





# bai 4,4
import os
import shutil


os.mkdir('D:/BAI44')
shutil.copy('D:/Iris.txt.txt','D:/BAI44')
os.rename('D:/BAI44/Iris.txt.txt','D:/BAI44/Data.dat')
os.chdir('D:/BAI44')
file = os.listdir()
for file in file:
    print(file)
os.rename('Iris.txt.txt')
os.chdir('D:/')
os.rmdir('BAI44')









# bai 4,5 # chua lam dk


def file(x):
    with open(x,'r') as f:
        a = f.read()
        print(a)
def file1(x):
    with open(x,'r') as f:
        n, m = 0
        k = []
        n, m = f.readline().split()
        n = int(n)
        m = int(m)
        print(n, m)
        for i in range(n):
            a = f.readline().split()
            for j in range(len(a)):
                a[j] = float(a[j])
            k.append(a)
        return n, m, k

def dem(k):
    a = 0
    for i in range(len(k)):
        for j in range(len(k[0])):
            if k[i][j] == 0:
                a +=1
    return a
def thaythe(k,n,m):
    for i in range(len(k)):
        for j in range(len(k[0])):
            if k[i][j] == 0:














































