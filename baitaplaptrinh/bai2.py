import numpy as np

m = 3
p = np.array([[8,9,9],[9,7,9],[8,8,8],[7,6,6],[7,6,5],[6,7,6],[2,2,1],[1,2,1],[2,1,2]])
test = np.array([[8,7,9]])
t = [0,1]
w = np.array([[2,-9,3]])
b = 98
a = 0
k = 0
while True:
    d = True
    k += 1
    print("lan lap thu K :",k)
    for i in range(m):
        x = np.array([p[i]])
        n = w.dot(x.T) + b
        if n < 1:
            a = 1
        elif n < 2:
            a = 2
        else:
            a = 3
        if np.array_equal(t[i],a) == False:
            e = t[i]-a
            w = w+np.dot(e,x)
            b = b+e
            d = False
    print("w = ",w)
    print("b = ",b)
    if(d == True):
        break


n = w.dot(test.T) + b
if n < 1:
    wr = "1"
elif n < 2:
    wr = "2"
else:
    wr = "3"
print(" THUOC LOP " + "\""+wr+"\"")





























































































