import numpy as np


s = 2 # số noron
r = 2 # số thành phần dữ liệu đầu vào
m = 8 # số mẫu dữ liệu traiining
p = np.array([[1,1],[2,2],[8,1],[9,3],[2,7],[3,8],[8,8],[9,9]]) # dữ liệu traning
t = np.array([[0,0],[0,0],[1,0],[1,0],[0,1],[0,1],[1,1],[1,1]]) # dữ liệu đầu ra thực tế
a = np.array([[0,0]]) # khai báo và khởi tạo đầu ra của mạng
# khởi tạo
w = np.array([[1,0],[2,8]])
b = np.array([[-6,-9]])
k=0
while True:
    d = True
    k +=1
    print('lap lai : ',k)
    for i in range(m):
        x = np.array([p[i]])
        n = w.dot(x.T) +b
        for j in range(s):
            if n[j][0] >=0 :
                a[0][j] = 1
            else:
                a[0][j] = 0
            if (np.array_equal([t[i]],a) == False):
                e = t[i] -a
                e1 = e.T
                w = w + e1.dot(x)
                b = b + e
        print('w = ',w)
        print('b = ',b)
    if d==True:
        break
f = np.array([[9,2]])
n = w.dot(f.T) +b.T
for j in range(s):
    if(n[j][0] >=0):
        a[0][j] = 1
    else:
        a[0][j] = 0
print('lop cua f la : ',a)

























































