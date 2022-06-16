
n = int(input("nhap n: "))
a = []
for i in range(n):
    print(" nhap thu tu ", i, end=":")
    x = int(input())
    a.append(x)

m = int(input("nhap n: "))
b = []
for i in range(m):
    print(" nhap thu tu ", i, end=": ")
    x = int(input())
    b.append(x)

a.sort()
b.sort()
c = a + b
c.sort()
print(c)











