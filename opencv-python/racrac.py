

import hand
import numpy as np
import cv2


#######################

def fingersUp(self):
    fingers = []
    # Thumb, we will compare x, not y
    if self.landmarksList[self.fingerTops[0]][1] > self.landmarksList[self.fingerTops[0] - 1][1]:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers, y will be taken
    for id in range(1, 5):
        if self.landmarksList[self.fingerTops[id]][2] < self.landmarksList[self.fingerTops[id] - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers
fingers = fingersUp()


brushThickness = 1
drawColor = (255, 0, 255)
headerColor = [(255, 0, 255), (255, 255, 0), (0, 255, 255), (0, 0, 0)]
########################

# HD webcam will be (720, 1280, 3), sorry but my webcam support only for standard VGA :(
WINDOW_SIZE = (480, 640, 3)
HEADER_SIZE = (int(WINDOW_SIZE[1]), int(WINDOW_SIZE[0]/20))

imgCanvas = np.zeros(WINDOW_SIZE, np.uint8)
# print(WINDOW_SIZE[:-1]/4)
header = np.zeros(WINDOW_SIZE, np.uint8)
header[:] = headerColor[1]
# print(header.shape)
header[0:WINDOW_SIZE[0], 0:(WINDOW_SIZE[1]//4)] = headerColor[0]
header[0:WINDOW_SIZE[0], (WINDOW_SIZE[1]//4)
                          :(WINDOW_SIZE[1]//2)] = headerColor[1]
header[0:WINDOW_SIZE[0], (WINDOW_SIZE[1]//2)
                          :(WINDOW_SIZE[1]//4*3)] = headerColor[2]
header[0:WINDOW_SIZE[0], (WINDOW_SIZE[1]//4*3)
                          :(WINDOW_SIZE[1])] = headerColor[3]
header = cv2.resize(header, HEADER_SIZE)

# 1. Handfree Mode - 5 finger up and nothing happends except for moving hands and pointer
if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
    xp, yp = 0, 0

# 2. Erase Mode - All fingers go down
elif checkErase:
    xp, yp = 0, 0
    imgCanvas = np.zeros(WINDOW_SIZE, np.uint8)

# 3. Thickness Changing Mode - Thumb and first finger go up
elif fingers[0] == 0 and fingers[1]:
    cv2.rectangle(img, (x1, y1 - 25),
                  (x2, y2 + 25), drawColor, cv2.FILLED)
    # print(abs(x1-x2)*(abs(y1-25-(y2+25))))
    calibrator = math.sqrt((x2-x3)**2+(y2-y3)**2)
    print(calibrator)
    brushThickness = max(
        int(abs(x1-x2)*(abs(y1-25-(y2+25)))/(calibrator*15)), 1)
    print(brushThickness)
    xp, yp = 0

# 4. Selection Color Mode - first and second fingers go up
elif fingers[1] and fingers[2]:
    xp, yp = 0, 0
    if y1 < HEADER_SIZE[1]:
        if 0 < x1 < WINDOW_SIZE[1]//4:
            drawColor = headerColor[0]
        elif WINDOW_SIZE[1]//4 < x1 < WINDOW_SIZE[1]//2:
            drawColor = headerColor[1]
        elif WINDOW_SIZE[1]//2 < x1 < WINDOW_SIZE[1]//4*3:
            drawColor = headerColor[2]
        elif WINDOW_SIZE[1]//4*3 < x1 < WINDOW_SIZE[1]:
            drawColor = headerColor[3]

# 5. Drawing Mode - Only first fingers go up
elif checkDraw:
    cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
    if xp == 0 and yp == 0:
        xp, yp = x1, y1
    cv2.line(imgCanvas, (xp, yp), (x1, y1),
             drawColor, brushThickness)

    xp, yp = x1, y1


img = cv2.add(img, imgCanvas)
# Optionally stack both frames and show it.
stacked = np.hstack((imgCanvas, img))
cv2.imshow('Trackbars', cv2.resize(stacked, None, fx=0.6, fy=0.6))
img[(WINDOW_SIZE[1]-HEADER_SIZE[0]):HEADER_SIZE[1],
    (WINDOW_SIZE[1]-HEADER_SIZE[0]):WINDOW_SIZE[1]] = header
cv2.imshow("Image", img)