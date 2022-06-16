import cv2
import numpy as np




cap = cv2.VideoCapture(0)# nếu có nhiều thì gọi nhiều 1,2,3
# cap = cv2.VideoCapture('1.mp4)

while True:
    ret,frame = cap.read()
    # print(ret)
    cv2.imshow('cua so cam',frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyWindow()

























