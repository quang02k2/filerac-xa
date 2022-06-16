import random

import cv2
import numpy as np


img = cv2.imread('anhmoi.jpg',1)
while True:
    g = cv2.resize(img,(0,0),fx=1.2,fy=1.2)
    cv2.imshow('hien thi ',g)
    if cv2.waitKey(1) == ord('s'):
        break


# copy vung anh






# nháp

# img1 = cv2.resize(img,(960,600))
# vungchon = img1[0:100,100:200]
# img1[200:300,200:300]= vungchon
# cv2.imshow('hien thi ',img1)
# k = cv2.waitKey()

# vungchon = img[0:100,200:350]
# img[200:300,400:550]= vungchon
# cv2.imshow('hien thi ',img)
# k = cv2.waitKey()