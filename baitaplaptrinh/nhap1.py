import numpy as np






def nhap_a():
    n = int(input('nhap n: '))
    a = []
    for i in range(n):
        k = int(input('nhap a[{}]: '.format(i)))
        a.append(k)
    np.array(a)
    return a

def nhap_b():
    m = int(input('nhap b : '))
    b = []
    for i in range(m):
        c = input('nhap b[{}] :  '.format(i))
        b.append(c)
    return b

def tinh(a,b):
    c = []
    for i in range(min(len(a),len(b))):
        c.append(a[i])
        c.append(b[i])
    if len(a) > len(b):
        for i in range(len(a)-len(b)):
            c.append((a[len(b)+i]))
    if len(b) > len(a):
        for i in range(len(b) - len(a)):
            c.append((b[len(a) + i]))
    return c

a = nhap_a()
b = nhap_b()
d = tinh(a,b)
print(d)



def nhap():
    n = int(input('nhap phan tu : '))
    a = []
    for i in range(n):
        k = int(input('nhap a[{}] : ').format(i))
        a.append(k)
    a = np.array(a)
    a = np.sort(a)
    return a

# def tinh(a,b):
#     c = []
#     i= 0
#     j = 0
#     while i<len(a) and j < len(b):
#         if a[i] < b[j]:
#             c.append(a[i])
#             i += 1
#         elif a[i] > b[j]:
#             c.append(b[j])
#             j += 1
#     if i < len(a):
#         for t in range(i, len(a)):
#             c.append(a[t])
#     if j < len(b):
#         for t in range(i, len(b)):
#             c.append(b[t])
#     return c