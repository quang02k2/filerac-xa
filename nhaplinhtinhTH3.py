import numpy as np

# arr = np.array([1, 2, 3, 4], dtype='S')
#
# print(arr)
# print(arr.dtype)


# import numpy as np
#
# arr = np.array([1.1, 2.1, 3.1])
#
# newarr = arr.astype('S')
#
# print(newarr)
# print(newarr.dtype)




# arr = np.array([[1, 2, 3], [4, 5, 6], [8, 9, 10], [11, 12, 14]])
# print(arr)
# newarr = arr.reshape(-1)
# print(newarr)



# noi 2 mang thanh 1 mang duy nhat
# arr1 = np.array([1, 2, 3])
#
# arr2 = np.array([4, 5, 6])
#
# arr = np.concatenate((arr1, arr2))


# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
#
# newarr = arr.reshape(2,4)
#
# print(newarr)
# np.nditer()



# a = np.arange(0,60,6)
# a = a.reshape(5,2)
# print('Original array is:')
# print (a)
# print ('\n')
#
# for x in np.nditer(a, op_flags=['readwrite']):
#    x[...] = 2*x
# print ('Modified array is:')
# print (a)



# Liệt kê các phần tử sau mảng 1D:

# arr = np.array([1, 2, 3])
#
# for idx, x in np.ndenumerate(arr):
#   print(idx, x)


# Nối các mảng bằng cách sử dụng các hàm ngăn xếp

# arr1 = np.array([1, 2, 3])
#
# arr2 = np.array([4, 5, 6])
#
# arr = np.stack((arr1, arr2), axis=1)
#
# print(arr)










# Xếp chồng lên hàng
# NumPy cung cấp một chức năng trợ giúp: hstack() xếp chồng dọc theo hàng.


# arr1 = np.array([1, 2, 3])
#
# arr2 = np.array([4, 5, 6])
#
# arr = np.hstack((arr1, arr2))
#
# print(arr)



# Xếp chồng dọc theo các cột
# NumPy cung cấp một chức năng trợ giúp: vstack()  xếp chồng dọc theo các cột.

# arr1 = np.array([1, 2, 3])
# 
# arr2 = np.array([4, 5, 6])
# 
# arr = np.vstack((arr1, arr2))
# 
# print(arr)






# Xếp chồng dọc theo chiều cao (chiều sâu)
# NumPy cung cấp một chức năng trợ giúp: dstack() xếp chồng theo chiều cao, bằng với chiều sâu.

# arr1 = np.array([1, 2, 3])
#
# arr2 = np.array([4, 5, 6])
#
# arr = np.dstack((arr1, arr2))
#
# print(arr)



# Chia mảng thành 3 phần:

# arr = np.array([1, 2, 3, 4, 5, 6])
#
# newarr = np.array_split(arr, 3)
#
# print(newarr)



# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
#
# newarr = np.array_split(arr, 3)
#
# print(newarr)





# Tạo một mảng bộ lọc sẽ chỉ trả về các phần tử chẵn từ mảng ban đầu:

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = []

for element in arr:

  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)



arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

