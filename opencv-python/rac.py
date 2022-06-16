import random
import sys
import cv2
import numpy as np


# cap = cv2.VideoCapture(0)
# while True:
#     a,b = cap.read()
#     c = int(cap.get(4))
#     d = int(cap.get(3))
#
#     g = cv2.resize(b,(0,0),fx=0.5,fy=0.5)
#     e = np.ones(b.shape, np.uint8)
#     e[:c//2,:d//2] = g
#     e[:c//2,d//2:] = g
#     e[c//2:,:d//2] = g
#     e[c//2:,d//2:] = g
#     cv2.imshow('hienthi',e)
#     if cv2.waitKey(1)==ord("s"):
#         break
# cap.release()
# cv2.VideoCapture()








# cap = cv2.imread('anhmoi.jpg',1)
# cv2.imshow('hien thi di',cap)
# cv2.waitKey()

def nhap1():
    cap = cv2.imread('anhmoi.jpg',1)
    cv2.imshow('hien thi di',cap)
    return cv2.waitKey()

def nhap2():
    cap = cv2.imread('anhmoi.jpg',1)
    cv2.imshow('hien thi',cap)
    while cv2.waitKey()==ord('s'):
        break
# a = nhap2()

def nhap3():
    cap = cv2.imread('anhmoi.jpg',1)
    img = cv2.resize(cap,(600,600))
    cv2.imshow('hien thi',img)
    cv2.waitKey()
# a = nhap3()

def nhap4():
    cap = cv2.imread('anhmoi.jpg',1)
    img = cv2.resize(cap,(0,0),fx=1.2,fy=1.2)
    cv2.imshow('hien thi di',img)
    cv2.waitKey()
# a = nhap4()

def nhap5():
    cap = cv2.imread('anhmoi.jpg',1)
    img = cv2.resize(cap,(0,0),fx=1.2,fy=1.2)
    cv2.imshow('hien thi',img)
    if cv2.waitKey()==ord('s'):
        cv2.imwrite('anh_moi_nhat.jpg',img)
# a = nhap5()

def nhap6():
    cap = cv2.imread('anh_moi_nhat.jpg',1)
    for i in range(200):
        for j in range(100):
            cap[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    cv2.imshow('hien thi',cap)
    cv2.waitKey()
# a = nhap6()


def nhap7():
    cap = cv2.VideoCapture(0)
    while True:
        ret,framd = cap.read()
        cv2.imshow('hien thi di',framd)
        if cv2.waitKey(1)==ord('s'):
            break
    cap.release()
    cv2.VideoCapture()
# a = nhap7()


def nhap8():
    cap = cv2.VideoCapture(0)
    while True:
        ret,frame = cap.read()
        a = int(cap.get(4))
        b = int(cap.get(3))
        g = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
        img = np.zeros(frame.shape,np.uint8)
        img[:a//2,:b//2] = g
        img[:a//2,b//2:] = g
        img[a//2:,:b//2] = g
        img[a//2:,b//2:] = g
        cv2.imshow('hien thi ',img)
        if cv2.waitKey(1) == ord('s'):
            break
    cap.release()
    cv2.VideoCapture()

# a = nhap8()


def nhap9():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        a = int(cap.get(4))
        b = int(cap.get(3))
        g = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)


        img = np.zeros(frame.shape,np.uint8)
        img[:a//2,:b//2] = cv2.rotate(g,cv2.ROTATE_180)
        img[:a//2,b//2:] = g
        img[a//2:,:b//2] = cv2.rotate(g,cv2.ROTATE_180)
        img[a//2:,b//2:] = g
        cv2.imshow('hien thi',img)
        if cv2.waitKey(1) == ord('s'):
            break
    cap.release()
    cv2.VideoCapture()
# a = nhap9()
cap = cv2.VideoCapture(0)
while True:
    ret , frame = cap.read()
    withd = int(cap.get(4))
    hight = int(cap.get(3))

    img = cv2.line(frame,(0,0),(withd,hight),(20,20,40),10)
    img = cv2.circle(frame,(50,50),50,(10,20,40),10)
    img = cv2.rectangle(frame,(0,0),(200,100),(20,34,70),10)

    fodin = cv2.FONT_HERSHEY_PLAIN
    img = cv2.putText(frame,'hien thi ra di',(0,hight-200),fodin,10,5)

    cv2.imshow('hien thi',frame)
    if cv2.waitKey(1)==ord('s'):
        break


