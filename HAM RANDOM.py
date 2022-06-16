
import random

# a = randrange(1,20)
# print(a)


# bai tap
# a = random.randrange(1,20)
# print(a)
# nhap = int(input('nhap so ban chon: '))
# d = 0
# while nhap != a:
#     d += 1
#     if nhap > a:
#         print('lon qua roi ')
#         print('ban co so lan nhap la d{}/5'.format(d))
#     if nhap < a:
#         print('be qua roi ')
#         print('ban co so lan nhap la d{}/5'.format(d))
#     nhap = int(input('nhap so ban chon: '))
#     if d == 5:
#         print('ket thuc! ban da thua')
#         break
#
# print('ban da: WIN')








a = random.randint(2,20)
print(a)
x = int(input("nhap gia tri cua ban: "))
d = 0
while a != x:
    d  += 1
    if x > a:
        print('lon qua roi ban ')
        print(f'so lan nhap cua ban la {d}/5.')
    if x < a:
        print('nho qua roi ban ')
        print(f'so lan nhap cua ban la {d}/5.')
    if d == 5:
        print('ban da het luot nhap ')
        print('Ba da thua ')
        break
    x = int(input("Moi ban nhap lai gia tri : "))

print('BAN THANG:  WINN ')








