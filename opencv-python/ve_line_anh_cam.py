
import numpy as np
import cv2
# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     widrh = int(cap.get(3))
#     height = int(cap.get(4))
#     cv2.imshow('hien thi',frame)
#     if cv2.waitKey(1)==ord('s'):
#         break
# cap.release()
# cv2.VideoCapture()



cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))


    # vẽ line
    # img = cv2.line(frame,(0,0),(width,height),(100,100,100),10)
    # imt = cv2.line(frame,(0,height),(width,0),(255,255,255),10)
    # imf = cv2.line(frame,(width//2,height//2),(width//2,height//2),(200,200,200),20)

    # vẽ hình chứ nhật
    # img = cv2.rectangle(frame,(10,10),(20,50),(10,30,40),10)

    # ve hinh tron
    img = cv2.circle(frame,(50,50),50,(20,40,10),10)


    # chèn text
    font = cv2.FONT_HERSHEY_PLAIN
    img = cv2.putText(frame,'vui qua di',(0,height-30),font,3,10)





    cv2.imshow('hien thi',frame)
    if cv2.waitKey(1)==ord('s'):
        break
cap.release()
cv2.VideoCapture()





















