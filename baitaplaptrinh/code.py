import numpy as np


def tien_1_loai(kg,money):
    return kg * money


def tong_thanh_toan(tong_tien_x,tong_tien_y):
    return tong_tien_x + tong_tien_y


def hoan_tien(tong_tien,you_money):
    return you_money - tong_tien


def so_tien_thanh_toan(you_money):
    a = [500,200,100,50,20,10,5,2,1]
    b = dict()
    dem = 0
    for i in a:
        cout = int(you_money/i)
        you_money = you_money - i*cout
        dem += 1
        if cout !=0:
            b[str('so tien can tra ' + str(i))] = cout
            if dem == len(a):
                break
    return b


def main():
    tien_1kg_tao = 10
    tien_1kg_le = 12
    tien_1kg_nhan = 15
    tao = float(input('nhap so can tao : '))
    le = float(input('nhap so can le : '))
    nhan = float(input('nhap so can nhan : '))
    tien_nhan = tien_1_loai(tien_1kg_nhan,nhan)
    tien_tao = tien_1_loai(tien_1kg_tao,tao)
    tien_le = tien_1_loai(tien_1kg_le,le)
    tong_tien = tong_thanh_toan(tong_thanh_toan(tien_le,tien_tao),tien_nhan)
    you_money = float(input('so tien nguoi mua tra : '))
    tien_tra = hoan_tien(tong_tien,you_money)
    b = so_tien_thanh_toan(tien_tra)


    print('so tien tao: ',tien_tao)
    print('so tien nhan: ',tien_nhan)
    print('so tien le: ',tien_le)
    print('tong so tien thanh toan la : ',tong_tien)

    while True:
        if b == -1:
            print('so tien ko du ')
        else:
            print('so tien can tra lai la: ', tien_tra)
            print(b)

main()















