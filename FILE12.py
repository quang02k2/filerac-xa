import numpy as np


def sinhvien():
    sv = []
    while True:
        name = input('nhap ten sv: ')
        date = int(input('nhap tuoi sinh vien: '))
        masv = int(input("nhap ma sv: "))
        clas = input('nhap lop : ')
        sv.append([name,date,masv,clas])
        return sv

a = sinhvien()
print(a)

























































































