import numpy as np


def money_product(price,amount):
    return price * amount


def sum_money(coca,pepsi):
    return coca + pepsi


def so_tien_thanh_toan(you_money):
    a = [500,200,100,50,20,10,5,2,1]
    b = dict()
    dem = 0
    for i in a:
        cout = int(you_money/i)
        you_money = you_money - i*cout
        dem += 1
        if cout !=0:
            b[str('so tien can tra ' + str(i))] = cout*(-1)
            if dem == len(a):
                break
    return b



def main():
    coca = 15
    pepsi = 10
    buying_coca = int(input('nhap so luong coca : '))
    buying_pepsi = int(input('nhap so luong pepsi : '))
    money_coca = money_product(coca,buying_coca)
    money_pepsi = money_product(pepsi,buying_pepsi)
    money_sum = sum_money(money_coca,money_pepsi)
    you_money = float(input('nhap so tien khach hanh tra: '))
    print('tong so tien can tra la: ',money_sum)

    while True:
        money = money_sum - you_money
        if money > 0:
            if int(money) <= 0:
                break
            print('so tien khach hang can tra them la: ', money)
            you_money = float(input('nhap so tien khach hanh tra them : '))
            money_sum = money
        elif money <= 0:
            break
    print('ban da du tien mua')
    money_back = so_tien_thanh_toan(money)

    print(money_back)


main()

















