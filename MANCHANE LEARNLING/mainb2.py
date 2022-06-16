from functions import *



ram = np.loadtxt('data.txt',delimiter=',')

y = ram[:,2]

x = np.zeros((np.size(y),np.size(ram,1)))

x[:,0] = 1

x[:,1:] = ram[:,0:2]
Thenta = np.array([1,2,3])
print(computeCost(x,y,Thenta),computerCOST_VEC(x,y,Thenta))
















