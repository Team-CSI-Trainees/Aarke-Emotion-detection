import cv2
from deepface import DeepFace

face_casc=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)

cap.set(3,720)              #3 the id for width
cap.set(4,640)              #4 is the id for height
cap.set(10,150)             #10 is the id for brightness

while True:
    success,img=cap.read()
    emotion = DeepFace.analyze(img,actions=['emotion','gender'],enforce_detection=False)
    face=face_casc.detectMultiScale(img,1.1,4)
    for(w,x,y,z) in face:
        cv2.rectangle(img,(w,x),(w+y,x+z),(210,0,210),2)
        font=cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(img,emotion['dominant_emotion'],(w,x-20),font,1,(210,0,210),2)
        cv2.putText(img, emotion['gender'], (w+150, x-20), font, 1, (210, 0, 210), 2)
    cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

