import numpy as np


# def sinhvien():
#     sv = []
#     while True:
#         name = input('nhap ten sv: ')
#         if name =='':
#             break
#         date = int(input('nhap tuoi sinh vien: '))
#         masv = int(input("nhap ma sv: "))
#         clas = input('nhap lop : ')
#         sv.append([name,date,masv,clas])
#     return sv
#
# a = sinhvien()
# b = np.array(a)
# for i in b:
#     print('\t'.join(['ten','tuoi','masv','lop']))
#     print('\t'.join(i))





with open('D:\WEDD\ha.txt', 'w',encoding='utf-8') as f:
    while True:
        name = input('nhap ten sv: ')
        if name == '':
            break
        date = input('nhap tuoi sinh vien: ')
        masv = input("nhap ma sv: ")
        clas = input('nhap lop : ')
        f.write('\t'.join([name,date,masv,clas])+'\n')














































