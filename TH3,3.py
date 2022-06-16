
n = int(input("nhap n: "))
a = []
for i in range(n):
    a = a + [int(input(" nhap a[%d] = " %i))]
print(a)
m = int(input("nhap m: "))
b = []
for j in range(m):
    print(" nhap vao b", end="[{}] : ".format(j))
    x = input()
    b.append(x)
print(b)
def tinhf(list1,list2):
    list3 = []
    for i in range(min(len(list1), len(list2))):
        list3.append(list1[i])
        list3.append(list2[i])
    if len(list1) > len(list2):
        for i in range(len(list1)-len(list2)):
            list3.append((list1[len(list2) + i]))
    elif len(list2) > len(list1):
        for i in range(len(list2)-len(list1)):
            list3.append(list2[len(list1) + i])
    return list3


c = tinhf(a, b)
print(c)













