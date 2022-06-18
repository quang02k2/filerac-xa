import numpy as np
import math
import sys

def calc_total_price(x,y):
    return x*y


def calc_return(x,y):

    a = y - x
    if y < x:
        return -1
    else:
        return a


def tien_tra(x):
    a = [500,200,100,50,20,10,5,2,1]
    b = dict()
    for i in a:
        count_x = int(x/i)
        x = x - i*count_x
        dem = +1
        if count_x!= 0:
            b[str('so tien ' + str(i))] = count_x
            if dem == len(a):
                break
    return b




def main():
    kg_apple =  20
    apple_weight = float(input('so can tao: '))
    money_given = float(input('so tien cua khach dua : '))

    total_price = calc_total_price(apple_weight,kg_apple)#tong so tien
    money_return = calc_return(total_price,money_given) # so tien can tra lai

    if money_return == -1:
        print('dua thieu tien ')
        print('so tien thieu : ',total_price-money_given)
    else:
        print(' so tien can tra lai: ',money_return)
        a = tien_tra(money_return)
        print(a)


main()


















































































