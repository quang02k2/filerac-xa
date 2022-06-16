import numpy as np
import random
from math import sqrt
# append: thêm vào cuối phần tử
# a = [2,3,4,5]
# print(a[::-1])
# a.append(223)
# print(a)

# cout : đếm số phần tử giống nhau trong mảng
# a = [2,23,4,2,1]
# b = a.count(2)
# print(b)

# reverse :  đảo list
# a = [3,2,4,1]
# a.reverse()
# print(a)

# insert : thêm phần tử mới vào vị trí chỉ định
# a = [2,3,4,1,5,6,'hai']
# a.insert(2,'hia')
# print(a)

# index : tìm giá trị đầu tiên nếu ko có thì báo lỗi
# a = [1,2,3,4,'hai']
# b = a.index(2)
# print(b)


# # extends : thêm một list khác nối vào vị trí cuối
# a = [2,3,4,1]
# b = ['ad',33]
# a.extend(b)
# print(a)


# reset list : xóa hết phần tử
# a = [32,4,1]
# print(a)
# a.clear()
# print(a)



# sort : sắp xếp
# a = [2,5,1,4,7,9,6]
# a.sort() # thay đổi giá trị ban đầu
# B = sorted(a)    # ko thay đổi gtri ban đầu
# print(a)
# print(B)


 # BT
# def nhap():
#     n = int(input('nhap n: '))
#     a = [0]*n
#     for i in range(n):
#         a[i] = random.randint(1,101)
#     return a
# a = nhap()
# print(a)

# BT

# def nhap():
#     n = int(input('nhap n: '))
#     a = [0]*n
#     for i in range(n):
#         a[i] = input(f'nhap a[{i}] = ')
#     return a
#
# def nhapx(a):
#     b = []
#     for i in range(len(a)):
#         b.append(int(a[i])**2)
#     return b
# def ham(a):
#     dem = 0
#     for i in range(len(a)):
#         if a[i] > 50:
#             dem += 1
#     return dem
# a = nhap()
# print(a)
# b = nhapx(a)
# print(b)
# c = ham(b)
# print(c)




# BT

quest = ['2 + 5 + 7 =','5 * 10 =','sqrt(16) =','12%2 =','5//2 =']
def nhap(a):
    for i in a:
        b = i.strip('=')
        c = eval(b)
        nhap = float(input(i))
        dem = 0
        while nhap != c:
            dem += 1
            print('ban da sai ')
            print(f'ban con so lan nhap la {dem}/2')
            nhap = float(input(i))
            if dem == 2 :
                print('ban het so lan nhap ')
                break
        else:
            print('ban da nhap dung ')

a = nhap(quest)
print(a)

















































