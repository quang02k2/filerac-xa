


n = int(input("nhap so sinh vien ban 1: "))
a = set()
for i in range(n):
    print('ma sinh vien: ', end='{} = '.format(i))
    x = input()
    a.add(x)
print(a)

m = int(input("nhap so sinh vien ban 2: "))
b = set()
for j in range(m):
    print("ma sinh vien: ", end='{} = '.format(j))
    y = input()
    b.add(y)
print(b)

if len(b & a) > 0:
    print("co sinh vien dang ki ca 2 ban")
else:
    print("ko co sinh vien nao dang ki ca 2 ban")

c = a | b
print("hop cua 2 ban: ", c)
print("sinh vien dang ki ban 1 ma ko dang ki ban 2: ", (a - b))