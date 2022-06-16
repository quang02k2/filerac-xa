import sys
import numpy
import cv2  #sử dụng để xuất dự đoán lệnh


# cú pháp:   cv2.imread(path,flag)
# cv2.IMREAD_COLOR :(1) trả về ảnh màu, bỏ qqua kênh alpha(kênh trong suốt)
# cv2.IMREAD_GRAYSCALE :(0) trả về ảnh đen trắng
# cv2.IMREAD_UNCHANGED :(-1) trả về ảnh bao gồm cả kênh alpha


# doc anh
img = cv2.imread("2.jpg",1)
# xuat anh
# cv2.imshow('hien thi',img)
# # thoi gian anh
# k = cv2.waitKey()



# xuất ảnh theo kích thước mong muốn

# img1 = cv2.resize(img,(400,200))
# cv2.imshow('hien thi',img1)
# k = cv2.waitKey()



# xuất ảnh theo tyy lệ ban đầu

# img2 = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
# cv2.imshow('hien thi',img2)
# k = cv2.waitKey()


# print(ord('s')) # trả về ASDII
# if k ==ord('s'):
#     cv2.imwrite('anhmoi.jpg',img2)


# xoay anh
img3 = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
img4 = cv2.rotate(img3,cv2.ROTATE_180)


cv2.imshow('hien thi ra',img4)
k = cv2.waitKey()





















