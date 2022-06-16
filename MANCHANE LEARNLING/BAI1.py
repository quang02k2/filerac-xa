
import numpy as np
import matplotlib.pyplot as plt

# np.loadtxt(fname=,dtype=,delimiter=)

# fname : tên file cần load data( nếu không cùng thư mục gốc với file*.py phải truyền toàn bộ đường dẫn
# dtype: kiểu dữ liệu của các element trong file( mặc định là float)
# delimiter : kí tự dùng để phân tách các cột trong file ( mặc định là khoảng trắng)

# LƯU Ý: trừ fname, các paramater khác khi truyền vào phải có kye_arg

# vd: np.loadtxt('hai',dtype=',')

# A = np.loadtxt('1a.txt', delimiter=',')
# print(A[0:2,:])
#
#
# np.savetxt('12a.txt', A,fmt='%.2f',delimiter=',')


X = np.loadtxt('univariate.txt',delimiter=',')
theta = np.loadtxt('univariate_theta.txt')

# lưu cột Y
y = np.copy(X[:-1])
#  Chuyển cột dầu sang cột 2
X[:,1] = X[:,0]
# đổi cột đầu = số 1
X[:,0] = 1
# tính lợi nhuận(đv 1000$)
preist = X@theta
# chuyển đơn vị $
preist = preist*1000
# in cặp dân số - lợi nhuận
print('%d người: %.2f'%(X[0,1]*1000,preist[0]))
np.savetxt('preist.txt',preist,fmt='%.6f')
P = np.loadtxt('preist.txt',delimiter='.')

plt.plot(X[1:,:],y,'rx')
plt.plot(P[1:,:],y,color='b')

plt.show()






















