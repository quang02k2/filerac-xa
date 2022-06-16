import numpy as np
import time

# n = int(input("nhap n: "))
# # for i in range(n):
# #     for j in range(n):
# #         if (j == 0 or j == (n-1)) or (i+j==n-1):
# #             print('*', end=' ')
# #         else:
# #             print(' ', end=' ')
# #     print()




# giay = time.time()
# print(giay)
# hientai = time.ctime(giay)
# print(hientai)
# print(' choi game: ')
# time.sleep(5)
# print('het gio')


# thoigian3 = time.localtime()
# print(thoigian3)
# print('nam hien tai: ',thoigian3.tm_year)
#
# thoigian3 = time.strftime("%y/%d/%m, %H:%M:%S",thoigian3)
# print(thoigian3)
# print(type(thoigian3))



# bai tap
# ten = input('nhap ten: ')
# tuoi = int(input("nhap tuoi: "))
# hientai = time.localtime()
# print(hientai)
# nam = hientai.tm_year
# namcan = (100 - tuoi) + nam
# print(namcan)



# a = time.localtime()
# print(a)
# # a = time.strftime('%d/%m/%y, %H:%M:%S',a)
# # print(a)
# b = a.tm_year
# print(b)
#
# ten = input('nhap ten: ')
# tuoi = int(input('nhap tuoi : '))
# nam = time.localtime()
# namcan = nam.tm_year
# candu = (100-tuoi)+namcan
# print(candu)




def nhap():
    n = int(input('nhap n: '))
    m = int(input('nhap n: '))
    a = []
    for i in range(n):
        x = []
        for j in range(m):
            x[j] = int(input('nhap a[{}][{}] = '.format(i,j)))
        a.append(x)
    return a
a = nhap()
print(a)




















