import numpy
#
#
# # các hàm sử lý
#
# # strip() # xóa kí tự nếu ko viết thì mặc định xóa khoảng trắng
#
# # chuoi = ' 123  '
# # a = chuoi.strip()
# # print(chuoi)
# # print(a)
# # chuoi2 = '-----hai----'
# # print(chuoi2)
# # b = chuoi2.strip('-')
# # print(b)
# # chuoi3 = '----hai--- --'
# # print(chuoi3)
# # c = chuoi3.strip('-')
# # print(c)
#
#
# # count('chars','start,end)
# # đếm số lần xuất hiện của chars xuất hiện trong str từ
# # index start đến end, mặc định bắt đầu là ko.
# #vd
#
#
# # vd = 'hayquabanoi'
# # print(vd.count('a'))
# # print(vd.count('a',1,4))
#
# # hàm viết hoa kí tự đầu tiên
#
# # vd1 = 'abs sd'
# # a = vd1.capitalize()
# # print(a)
#
# # đổi kí tự : replace()
# # vd3 = 'hay qua ban oi'
# # new = vd3.replace('hay','vui')
# # print(new)
#
# # tìm kiếm vị trí đầu tiên xuất hiện kí tự:
# # find('char',start,end)
# #vd
# # vd4 = 'ok ban la nhat'
# # print(vd4.find('a'))
#
#
# # isalnum : (có chữ cái hoặc số thì trả về True)
#  #           nếu chứa cả kí tự @#$%% thì trả về Flase
# # vd
# vd = '12adasd3###'
# print(vd.isalnum())
#
# #  isdigit()  kiểm tra xem nó có phải số hay ko
# # nếu đúng thì trả về True còn chứa các kí tự khác số thì Flase
# vd5 = '233'
# print(vd5.isdigit())
#
# # isalpha() : True nếu chuỗi chỉ gồm chữ cái
# vd2 = 'addfasdf'
# print(vd2.isalpha())
#
# # isspace(): True nếu chuỗi chỉ gồm space
# vd3 = '     '
# print(vd3.isspace())
#
# # isslower(): True nếu chuỗi chỉ gồm kí tự viết thường
# vd4 = 'anh yeu ak'
# print(vd4.islower())
#
# # isupper() : True nếu chuỗi chỉ gồm kí tự viết hoa
# vd6 = 'ANH HEY'
# print(vd6.isupper())
#
#
# # istitle() : chữ cái đầu chuỗi viết hao
# aa = 'hai ba'
# print(aa.istitle())
#
#
#
#VD:


# a = 'hai ba CHA ta Lam sao'
# a2 = str()
# for i in a:
#     if i.islower():
#         i = i.upper()
#     else:
#         i = i.lower()
#     a2 = a2 + i
# print(a2)






# split(sep, maxsplit): tach chuoi

# a = 'haiba lan csasd'
# a1 = a.split()
# print(' , '.join(a1))



# batap

# in ra ki tu a trong chuoi
a = 'hai ba bon nam sau '
for i in range(len(a)):
    if a[i] == 'a':
        print(i,end='\t')




# bai tap


# a = 'English = 18 science = 83 Math = 68 History = 65'
# # tinhtong so
# # tinh TBC
# c = a.split()
# d = str()
# x = 0
# for i in c:
#     if i.isdigit():
#         d += ' +  ' + i
#         x += 1
# print(eval(d))
# print(eval(d)/x)







# # bool : chấp nhận 2 giá trị: True hoac Flase
# n = input('nhap mat khau: ')
# x = bool
# y = bool
#
# for i in n:
#     if i.isdigit():
#         x = True
#         break
#     else:
#         x = False
# for i in n:
#     if i.isalpha():
#         y = True
#         break
#     else:
#         y = False
# if len(n) < 6 or x == False or y == False:
#     print('nhap kis tu can it nhat 6 so va can it nhat 1 so va 1 kis tu:')
#     n = input('nhap mat khau: ')
# else:
#     print('mat khau hop le')
# d = 0
# s = input('nhap mat khau dang nhap: ')
# while s != n:
#     d +=1
#     print('bna nhap sai ')
#     print(f'ban con so lan nhap la {d}/5')
#     s = input('nhap mat khau dang nhap: ')
#     if d == 5:
#         print('ban da het luot')
#         break
# else:
#     print('ban da mo dung')









#
# n = input('nhap mat khau he thong: ')
# x = bool
# y = bool
#
# def nhapham(n):
#     while True:
#         def nhapx(n, x):
#             for i in n:
#                 if i.isalpha():
#                     x = True
#                     break
#                 else:
#                     x = False
#             return x
#
#         def nhapy(n, y):
#             for i in n:
#                 if i.isdigit():
#                     y = True
#                     break
#                 else:
#                     y = False
#             return y
#
#         a = nhapy(n, y)
#         b = nhapx(n, x)
#
#         if len(n) < 6 or a == False or b == False :
#             print('ban da nhap sai')
#             n = input('nhap mat khau he thong: ')
#         else:
#             print('ban da mo dung ')
#             break
#
#
# def ham(n):
#     nhap = input('nhap mat khau cua ban: ')
#     dem = 0
#     while nhap != n:
#         dem += 1
#         print('ban da nhap sai ')
#         print(f'so lan nhap cua ban con {5-dem}/5 ')
#         nhap = input('nhap mat khau cua ban: ')
#         if dem == 5:
#             print('ban da het lan nhap mk')
#             break
#     else:
#         print('ban da mo dung mat khau ')
#
# nhapham = nhapham(n)
# print(nhapham)
# ham = ham(n)
# print(ham)




# bai tap

# a = 'abcdefghijklmnopqrstuvwxyz'
# b = 'zxcvbnmasdfghjklqwertyuiop'
# n = input('nhap ki tu: ')
# s = ' '
# for i in n:
#     index = a.find(i)
#     s = s + b[index]
# print(s)


# bai tap

# a = 'abc123'
# print(a)
# s = ''
# d = ''
# for i in a:
#     if i.isalpha():
#         s += i
# print(s)
# for i in a:
#     if i.isdigit():
#         d += i
# print(d)



