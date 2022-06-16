import numpy as np
import cv2
import time
import os

import hand as htm


cap = cv2.VideoCapture(0)
# them
folderpath = 'Fingers'
lst = os.listdir(folderpath)
lst_2= []

pTime = 0

for i in lst:
    img = cv2.imread(f'{folderpath}/{i}')
    lst_2.append(img)

derctor = htm.handDetector(detectionCon=1)

fingerid = [4,8,12,16,20]

while True:
    ret, frame = cap.read()
    # widrh = int(cap.get(3))
    # height = int(cap.get(4))

    frame = derctor.findHands(frame)
    lmList = derctor.findPosition(frame,draw=False)  # phat hien vi tri







    if len(lmList) !=0:

        fingers = []

        # viet cho ngon cai
        if lmList[fingerid[0]][1] < lmList[fingerid[0]-1][1]:

            fingers.append(1)
        else:
            fingers.append(0)


        # viết cho ngón dài
        for id in range(1,5):

            # if lmList[8][2]< lmList[6][2]:
            if lmList[fingerid[id]][2] < lmList[fingerid[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        print(fingers)



        songontay = fingers.count(1)


        # h,w,c = lst_2[0].shape
        # frame[0:h,0:w]=lst_2[0]
        h,w,c = lst_2[songontay-1].shape
        frame[0:h,0:w]=lst_2[songontay-1]



    # vẽ hình chữ nhật hiện ngón tay
        cv2.rectangle(frame,(0,200),(150,400),(20,40,200),-1)

        cv2.putText(frame,str(songontay),(30,350),cv2.FONT_HERSHEY_PLAIN,10,(20,200,29),3)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(frame,f"FPS: {int(fps)}",(150,70),cv2.FONT_HERSHEY_PLAIN,3,(230,0,5),4)

    g = cv2.resize(frame,(0,0),fx=1.5,fy=1.5)




    cv2.imshow('hien thi',g)
    if cv2.waitKey(1)==ord('s'):
        break
cap.release()
cv2.VideoCapture()



# C = 50
# H = 30
# D = [ x for x in input('nhap d: ').split(',')]
# value = []
# for i in D:
#     value.append(str(int(round(m.sqrt((2*C*float(i)))/H))))
# print(','.join(value))



#Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều.
# Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.

# Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1.
#
# Ví dụ: Giá trị X, Y nhập vào là 3,5 thì đầu ra là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
# #


# X = int(input('nhap x: '))
# Y = int(input('nhap y: '))


# a = input("Nhập số a: ")
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# n4 = int( "%s%s%s%s" % (a,a,a,a) )
# # Bài tập Python 18, Code by Quantrimang.com
# print ("Tổng cần tính là: ",n1+n2+n3+n4)



# import re
#
# str = 'Hoc lap trinh Toidicode.com'
# match = re.search(r'(.*) Toidicode.com', str)
# if match: #nếu tồn tại chuỗi khớp
#     print (match.groups()) # in ra chuỗi đó
# else:
#     print ('Khong tim thay!')



# import re
#
# str = 'Hoc lap trinh Toidicode.com'
# match = re.search("[0-9]", str)
# if match: #nếu tồn tại chuỗi khớp
#     print ('tim thay') # in ra chuỗi đó
# else:
#     print ('Khong tim thay!')





# import sys
# import matplotlib
# matplotlib.use('Agg')

# import matplotlib.pyplot as plt
# import numpy as np
#
# ypoints = np.array([3, 8, 1, 10])
#
# plt.plot(ypoints, 'o:r')
# plt.show()




















































































