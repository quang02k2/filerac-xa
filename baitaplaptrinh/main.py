from BT import *

S = int(input('nhap S: '))
E = int(input('nhap E: '))
while E>S or E>100000000:
    print('E KO hop le')
    E = int(input(' moi nhap lai E: '))

dem = 0
for i in range(E , S+1):
    if SNT(i) and DX(i):
        dem += 1
print('tong : ',dem)












