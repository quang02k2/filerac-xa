import cv2
import numpy as np




cap = cv2.VideoCapture(0)# nếu có nhiều thì gọi nhiều 1,2,3
# cap = cv2.VideoCapture('1.mp4)

while True:

    ret,frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    small_frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)

    inage = np.zeros(frame.shape,np.uint8)
    inage[:height//2,:width//2] = cv2.rotate(small_frame,cv2.ROTATE_180)
    inage[:height//2,width//2:] = small_frame
    inage[height//2:,:width//2] = small_frame
    inage[height//2:,width//2:] = small_frame
    cv2.imshow('cua so cam',inage)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyWindow()

























