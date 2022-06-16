import os
import time

import numpy as np
import cv2
import hand as htm
import sys

cap = cv2.VideoCapture(0)


Foder = 'Fingers' # anh ngon tay
lst = os.listdir(Foder) # gan vao
# --> day het thu muc Fingers vao Foder
lst_2 = []
for i in lst:
    img = cv2.imread(f'{Foder}/{i}')
    lst_2.append(img)

dicter = htm.handDetector(detectionCon=1)

finderic = [4,8,12,16,20]
ptime = 0



while True:
    ret, frame = cap.read()
    frame = dicter.findHands(frame)
    lmHand = dicter.findPosition(frame,draw=False)

    if len(lmHand) !=0:

        lst_3 = []
        if lmHand[finderic[0]][1] < lmHand[finderic[0]-1][1]:
            lst_3.append(1)
        else:
            lst_3.append(0)

        for i in range(1,5):
            if lmHand[finderic[i]][2] < lmHand[finderic[i]-2][2]:
                lst_3.append(1)
            else:
                lst_3.append(0)

        demngon = lst_3.count(1)

        h,w,c = lst_2[demngon-1].shape
        frame[0:h,0:w] = lst_2[demngon-1]


        cv2.rectangle(frame,(0,200),(30,100),(200,40,50),-1)
        cv2.putText(frame,str(demngon),(20,350),cv2.FONT_HERSHEY_PLAIN,3,(200,90,100),2)


    ctime = time.time()
    fpt = 1/(ctime-ptime)
    ptime=ctime

    cv2.putText(frame,f'FPS : {int(fpt)}',(20,90),cv2.FONT_HERSHEY_PLAIN,3,(20,100,200),3)

    cv2.imshow('hien thi raa',frame)
    if cv2.waitKey(1) == ord("s"):
        break
cap.release()
cv2.VideoCapture()























































































