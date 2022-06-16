import os
import time

import numpy as np
import cv2
import hand as htm
import sys



cap = cv2.VideoCapture(0)


foder = 'Finger'
lit = os.listdir(foder)
lst = []
for i in lit:
    img = cv2.imread(f'{lst}/{i}')
    lst.append(img)

Ptime = 0
dicterid = htm.handDetector(detectionCon=1)
b = [4,8,12,16,20]
while True:
    ret,frame = cap.read()
    frame = dicterid.findHands(frame)
    lmHan = dicterid.findPosition(frame,draw=False)
    if (len(lmHan))!=0:
        a = []
        if lmHan[b[0]][1] < lmHan[b[0]-1][1]:
            a.append(1)
        else:
            a.append(0)
        for i in range(1,5):
            if lmHan[b[i]][2] < lmHan[b[i]-2][2]:
                a.append(1)
            else:
                a.append(0)

        demngontay  = a.count(1)

        h,w,c = lst[demngontay].shape
        frame[0:h,0:w] = lst[demngontay]

    cv2.imshow('hien thi',frame)
    if cv2.waitKey(1) == ord("s"):
        break
cap.release()
cv2.VideoCapture()
