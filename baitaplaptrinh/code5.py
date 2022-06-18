import numpy as np


def money_Soort(gia,user):
    money = gia*user
    return money

def sum_money(money_coca,money_pepsi):
    return money_coca + money_pepsi


def money_thua(money_tra):
    money = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    tra_money = dict()
    dem = 0
    for i in money:
        count = int(money_tra/i)
        money_tra = money_tra - i*count
        dem += 1
        if count !=0:
            tra_money[f'so to tien {i} can dua '] = count*(-1)
            if dem == len(money):
                break
    return tra_money


def main():
    gia_coca = 20
    gia_pepsi = 15
    user_coca = int(input('nhap so chai coca: '))
    user_pepsi = int(input('nhap so chai pepsi: '))
    money_coca = money_Soort(gia_coca, user_coca)
    money_pepsi = money_Soort(gia_pepsi, user_pepsi)
    sum_moneys = sum_money(money_coca,money_pepsi)
    you_money = float(input('nhap so tien ban dua ra : '))
    print('so tien ban can tra la: ',sum_moneys)
    while True:
        money_tien = sum_moneys - you_money
        if money_tien > 0:
            print('ko dua du tien de tra, so tien ban can them de tra la : ', money_tien)
            you_money = float(input('nhap so tien ban dua them : '))
            sum_moneys = money_tien
        elif money_tien == 0:
            print('ko can thoi lai ')
            break
        else:
            print('tien can dua lai la ')
            money = money_thua(money_tien)
            print(money)
            break
main()




