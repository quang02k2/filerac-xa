
from ast import Return
import math as m
from pickle import TRUE

def isPrim(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    return False

def isSymmetry(n):
    a = 0
    while (n != 0):
        b = n % 10
        a = a * 10 + b
        n = n // 10
    return a

S = int(input(" nhap S : "))
E = int(input("nhap E : "))
while S > E or E > 100000000:
    print("ko dung voi yeu cau")
    E = int(input("nhap E : "))

tong = 0
for i in range(S, E + 1):
    if isPrim(i) and isSymmetry(i):
        tong += i

print("tong so nguyen to VA doi la : ", tong)