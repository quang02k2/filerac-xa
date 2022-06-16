import numpy as np

# bai 3,2


#
# def mang():
#     a = []
#     n = int(input("nhap n: "))
#     for i in range(n):
#         x = int(input("nhap a[{}] = ".format(i)))
#         a.append(x)
#     return a
#
# #
# def tinh(a):
#     n = int(input("nhap n: "))
#     m = int(input("nhap m: "))
#     b = []
#     if n*m > len(a):
#         print('ko tinh dk')
#     else:
#         c = 0
#         d = [0]*m
#         for i in range(n):
#             d[i] = a[c*m: c*m + m]
#             c += 1
#             b.append(d)
#         return b
# a = mang()
# print(a)
# b = tinh(a)
# print(b)









# bai 3,3
#
# #
# #
# def manga():
#     a = []
#     n = int(input("nhap n: "))
#     for i in range(n):
#         x = int(input("nhap [{}] = ".format(i)))
#         a.append(x)
#     return a
# def mangb():
#     a = []
#     m = int(input("nhap m: "))
#     for i in range(m):
#         x = input("nhap [{}] = ".format(i))
#         a.append(x)
#     return a
# def tinh(a,b):
#     c = []
#
#     for i in range(min(len(a),len(b))):
#         c.append(a[i])
#         c.append(b[i])
#     if len(a) > len(b):
#         for i in range(len(a)-len(b)):
#             c.append((a[len(b)+i]))
#     if len(a) < len(b):
#         for i in range(len(b)-len(a)):
#             c.append((b[len(a) + i]))
#     return c
#
#
# a = manga()
# b = mangb()
# c = tinh(a,b)
# print(c)













# bai 3,4

#
# def mang():
#     a = []
#     n = int(input("nhap n: "))
#     for i in range(n):
#         x = int(input("nhap a[{}] = ".format(i)))
#         a.append(x)
#     return a
# def tron(a,b):
#     c = []
#     for i in range(min(len(a),len(b))):
#         c.append(a[i])
#         c.append(b[i])
#     return c
# def sapxep(a):
#     return sorted(a)
#
#
# a = mang()
# b = mang()
# sapxep(a)
# print(a)
# sapxep(b)
# print(b)
# c = tron(a, b)
# d = sapxep(c)
# print(d)








# bai 3,5


# def mang():
#     a = []
#     n = int(input("nhap n: "))
#     for i in range(n):
#         x = input("nhap n: a[{}] = ".format(i))
#         a.append(x)
#     return a
#
# def tupy(x):
#     b = tuple(x)
#     return b
# def ktra(y):
#     x = 0
#     for i in y:
#         if i.isdigit():
#             x += 1
#     return x
#
#
# a = mang()
# b = tupy(a)
# print(b)
# print('so phan tu dang so trong b: ', ktra(b))






#bai 3,6


def tupy():
    a = []
    b = ()
    n = int(input("nhap n: "))
    for i in range(n):
        x = input("nhap a[{}] = ".format(i))
        a.append(x)
        b = tuple(a)
    return b

def tinh(a):
    x = 0
    for i in a[:]:
        x += i
    return ('tong: ',x/len(a))

a = tupy()
print(a)
b = tuple(int(i) for i in a[:])
print(b)
print(type(b))
c = tinh(b)
print(c)




# bai 3,7


# def nhap():
#     a = set()
#     n = int(input("nhap n: "))
#     for i in range(n):
#         x = int(input("nhap a[{}] = ".format(i)))
#         a.add(x)
#     return a
#
#
# def sv(a,b):
#     c = len(a & b)
#     if c > 0:
#         print("co sinh vien dang ki ca 2 ban")
#     else:
#         print("ko co sinh vien nao ca ")
#
#
# a = nhap()
# b = nhap()
# c = sv(a,b)
# print("danh sach sinh vien dang ki ca 2 ban la: ", a & b)
# print("danh sach sinh vien da dang ki ban 1 ma ko dang ki ban 2 la:  ", a-b)





#BAI 3,8

#
def nhap():
    n = int(input("nhap n: "))
    m = int(input("nhap m: "))
    a = dict()
    for i in range(n):
        for j in range(m):
            a = {('{}'.format(i)) : ('{}'.format(j))}
    return a
a = nhap()
print(a)

















# bai 3,9


# def nhap():
#     s = input()
#     return s
# def saucon(s,q):
#     if q.find(s) >= 0:
#         print('la sau con')
#     else:
#         print("ko la sau con ")
# def ghep(s,q):
#     d = s + q
#     return d
# def thaythe(s):
#     x = input('nhap ki tu can thay the: ')
#     y = input('nhap ki tu thay the : ')
#     return s.replace(x,y)
#
# def tach(s):
#     a = []
#     b = list(s.split())
#     for i in range(len(b)):
#         x = {i:b[i]}
#         a.append(x)
#     return a
#
# s = nhap()
# print(s)
# q = nhap()
# print(q)
# saucon(s, q)
# d = ghep(s,q)
# print('sau con khi ghep s vs q: ',d)
# h = thaythe(d)
# print(h)
# c = tach(d)
# print(c)












# bai 3,10

#
# def tao():
#     a = {
#         'n':  1500,
#         'CLUSTERS': 3,
#         'INTER': 1000,
#         'METHOD': 'DCA CLUSTERING',
#         'MEASURE': 'EUCLIDEAN',
#         'YEARS': 9,
#         'MAX': 200
#     }
#     return a
# def fileset(x):
#     s = set()
#     for d in x.values():
#         s.add(d)
#     return s
# def filelist(x):
#     s = []
#     for d in x.values():
#         s.append(d)
#     return s
# a = tao()
# print(a)
#
# c = fileset(a)
# print(c)
# d = filelist(a)
# print(d)

























