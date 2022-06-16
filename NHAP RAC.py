# ex1 : viết chương trình sử dụng dict chưa 10 user name và password.
# Chương trình yêu cầu nhập vào username và pass,
# 1. nếu user name o có trong dict, chương trình báo user name o tồn tại
# 2. nếu user name đúng mà password sai thì báo : PASSWORD SAI
# 3. nếu user, pass đúng thì báo bạn đã login thành công


import  numpy as np


#
# dic={"user1":"123456",
# "user2":"123456",
# "user3":"123456",
# "user4":"123456",
# "user5":"123456",
# "user6":"123456",
# "user7":"123456",
# "user8":"123456",
# "user9":"123456",
# "user10":"123456"}
#
# def nhap(d):
#     n = input('nhap user: ')
#     m = input('nhap password : ')
#     for i in d:
#         if n != i:
#             print('ko ton tai')
#             break
#         elif m != d[i]:
#             print('passwork ko ton tai')
#             break
#         else:
#             print('thanh cong')
#             break
#
#
#
#
# a = nhap(dic)
# print(a)















# ex2: cho
# #1: Tách số và chữ , hiển thị lên màn hình
# #2: tính tổng các số
# #3 chuyển đổi chuỗi : "University of Technology and Education" sang số


# dict_01 = {
#     "A":1,"B":2,"C":3,"D":2,"E":1,"F":4,"G":2,
#     "H":4,"I":1,"J":8,"K":5,"L":1,"M":3,"N":1,
#     "O":1,"P":3,"Q":10,"R":1,"S":1,"T":1,"U":1,
#     "V":4,"W":4,"X":8,"Y":4,"Z":10}
#
# def tach_chu(d):
#     a = []
#     for i in d.keys():
#         a.append(i)
#     return a
# def tach_so(d):
#     a = []
#     for j in d.values():
#         a.append(str(j))
#     return a
#
# def tong(d):
#     a = ' '
#     for i in d:
#         a = a + ' + ' + i
#     return eval(a)
# a = tach_chu(dict_01)
# print(' '.join(a))
# b = tach_so(dict_01)
# print(' '.join(b))
# c = tong(b)
# print(c)




















#ex03
"""
Cho data 1 cửa hàng, dữ liệu kiểu như sau :
d=[{"name":"Tuan","phone":"555-1414","email":"galailaptrinh@gmail.com"},
    {"name":"Hung","phone":"555-1618","email":"galaixapxinh@gmail.com"},
    {"name":"Trung","phone":"555-3141","email":""},
    {"name":"Hoang","phone":"555-2718","email":"loli@gmail.com"},
]

#1. Tìm tất cả user có số điện thoại kết thúc bằng 8
#2: tìm tất cả user o có địa chỉ email
"""

d=[{"name":"Tuan","phone":"555-1414","email":"galailaptrinh@gmail.com"},
    {"name":"Hung","phone":"555-1618","email":"galaixapxinh@gmail.com"},
    {"name":"Trung","phone":"555-3141","email":""},
    {"name":"Hoang","phone":"555-2718","email":"loli@gmail.com"},
]

def tim(d):
    a = []
    for i in d:
        check = i['phone']
        if check[-1] == '8':
            name = i['name']
            phone = i['phone']
            email = i['email']
            print('nam: ',name)
            print('phoe: ',phone)
            print('email : ',email)
            print('-'*20)


a = tim(d)
print(a)













































































