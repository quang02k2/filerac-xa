# MẢNG 1-D
import numpy as np

# a = np.array([1,2,3,4,4])
# Index : i=0,n-1
# # MANG 2-D
# b = np.array([[1,2,3,4],[3,4,5,6]])
# b [0,0] = 1
# b[0,1] = 2
# b[1,1] = 4
#
# # MANG 0-D
# a = 42
#
# # slicing : sử dụng dấu ':' như list
# # a[start :  end]
# a = [1 2 3 4 5]
# a[1:3] = [2 3]
# a[:]   = [1 2 3 4 5 ]
# a[2:]  = [3 4 5 ]
# a[:2]  = [1 2]
#
# # a[start : end : step]
# a[::2]
# a[1:5:2]

# slicing MANG 2 -D

a = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,23,44,33]])

print(a[1:2,1:4])
m = 3
b = a[:,0:1]
print(b)
c = a[0:,:1]
print(c)


































