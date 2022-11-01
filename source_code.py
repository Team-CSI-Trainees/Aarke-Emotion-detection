import time
t1=time.time()
import numpy
import cv2
import deepface

cap=cv2.VideoCapture(0)
cap.set(3,720)              #3 the id for width
cap.set(4,640)              #4 is the id for height
cap.set(10,150)             #10 is the id for brightness
while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
t2=time.time()
print(t2-t1)
