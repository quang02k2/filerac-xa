


def  strnhap(a):
     k = a.split()
     return (len(k))

def strSAU(a):
    s=a.split()
    d={}
    for i in range(len(a)):
        d[i] = s[i]
    return d

def strcheck(A):
    x = 0
    y = 0
    for i in range(len(A)):
        if A[i] == '(' : x = x +1
        if A[i] == ')' : y = y +1
        if x < y:
            return False
    if x != y:
        return False
    return  True
a = input("s = ")
if strcheck(a):
    print("dung")
else:
    print(" ko dung")
